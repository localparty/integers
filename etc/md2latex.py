#!/usr/bin/env python3
"""
Markdown → LaTeX converter for the Quantum Geometry in 5D papers.

Converts Paper 1 and Paper 2 markdown sources into arXiv-ready LaTeX.
Each paper gets its own output directory under paperN/etc/arxiv/.

Usage:
    python3 etc/md2latex.py          # convert both papers
    python3 etc/md2latex.py paper1   # convert paper 1 only
    python3 etc/md2latex.py paper2   # convert paper 2 only
"""

import os
import re
import sys
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # quantum-geometry-in-5d/


# ─────────────────────────────────────────────────────────────
# Unicode → LaTeX mapping (comprehensive)
# ─────────────────────────────────────────────────────────────

# Characters that do NOT need math mode (text-mode replacements)
TEXT_UNICODE = {
    "\u2014": "---",      # em dash —
    "\u2013": "--",       # en dash –
    "\u00a7": r"\S{}",    # section sign §
    "\u00b0": r"$^{\circ}$",  # degree sign °
    # Accented letters (for author names etc.)
    "\u00f6": r'\"{o}',   # ö
    "\u00fc": r'\"{u}',   # ü
    "\u00e4": r'\"{a}',   # ä
    "\u00e9": r"\'{e}",   # é
    "\u00e8": r"\`{e}",   # è
    "\u00e0": r"\`{a}",   # à
    "\u00f1": r"\~{n}",   # ñ
}

# Characters that need math mode: mapped to LaTeX command (without $ wrapping)
MATH_UNICODE = {
    # Greek lowercase
    "\u03C8": r"\psi",
    "\u03B1": r"\alpha",
    "\u03B2": r"\beta",
    "\u03B3": r"\gamma",
    "\u03B4": r"\delta",
    "\u03B5": r"\varepsilon",
    "\u03B6": r"\zeta",
    "\u03B7": r"\eta",
    "\u03B8": r"\theta",
    "\u03B9": r"\iota",
    "\u03BA": r"\kappa",
    "\u03BB": r"\lambda",
    "\u03BC": r"\mu",
    "\u03BD": r"\nu",
    "\u03BE": r"\xi",
    "\u03C0": r"\pi",
    "\u03C1": r"\rho",
    "\u03C3": r"\sigma",
    "\u03C4": r"\tau",
    "\u03C6": r"\varphi",
    "\u03C7": r"\chi",
    "\u03C9": r"\omega",
    # Greek uppercase
    "\u0393": r"\Gamma",
    "\u0394": r"\Delta",
    "\u0398": r"\Theta",
    "\u039B": r"\Lambda",
    "\u03A0": r"\Pi",
    "\u03A3": r"\Sigma",
    "\u03A6": r"\Phi",
    "\u03A8": r"\Psi",
    "\u03A9": r"\Omega",
    # Math operators / symbols
    "\u222B": r"\int",
    "\u2207": r"\nabla",
    "\u2202": r"\partial",
    "\u221E": r"\infty",
    "\u221A": r"\sqrt{}",
    "\u00D7": r"\times",
    "\u00B7": r"\cdot",
    "\u2248": r"\approx",
    "\u2260": r"\neq",
    "\u2264": r"\leq",
    "\u2265": r"\geq",
    "\u2261": r"\equiv",
    "\u2208": r"\in",
    "\u221D": r"\propto",
    "\u00B1": r"\pm",
    "\u2213": r"\mp",
    "\u2297": r"\otimes",
    "\u2295": r"\oplus",
    "\u2020": r"\dagger",
    "\u210F": r"\hbar",
    "\u2192": r"\to",
    "\u2190": r"\leftarrow",
    "\u2194": r"\leftrightarrow",
    "\u2191": r"\uparrow",
    "\u2193": r"\downarrow",
    "\u27E8": r"\langle",
    "\u27E9": r"\rangle",
    "\u2026": r"\ldots",
    "\u2032": r"'",
    "\u223C": r"\sim",
    "\u2273": r"\gtrsim",
    "\u2272": r"\lesssim",
    "\u222E": r"\oint",        # contour integral ∮
    "\u25A1": r"\square",      # □
    "\u220E": r"\blacksquare", # tombstone ∎
    "\u2713": r"\checkmark",   # ✓
    "\u2717": r"\times",       # ✗ (ballot X)
    "\u2609": r"_{\odot}",     # ☉ (sun)
    "\u25CB": r"\circ",        # ○
    "\u2154": r"\tfrac{2}{3}", # ⅔
    "\u2283": r"\supset",      # ⊃
    "\u226A": r"\ll",          # ≪ much less than
    "\u226B": r"\gg",          # ≫ much greater than
    "\u2245": r"\cong",        # ≅ congruent
    "\u27F9": r"\Longrightarrow",  # ⟹ long right double arrow
    "\u21BB": r"\circlearrowright", # ↻ clockwise
    "\u21BA": r"\circlearrowleft",  # ↺ counterclockwise
    # Pre-composed dot-above letters
    "\u1E8B": r"\dot{x}",     # ẋ
    "\u1E8A": r"\dot{X}",     # Ẋ
    "\u1E22": r"\dot{H}",     # Ḣ
    "\u1E23": r"\dot{h}",     # ḣ
    "\u0227": r"\dot{a}",     # ȧ
    "\u1E03": r"\dot{b}",     # ḃ
    "\u1E58": r"\dot{R}",     # Ṙ
    "\u1E59": r"\dot{r}",     # ṙ
    "\u1E56": r"\dot{P}",     # Ṗ
    "\u1E57": r"\dot{p}",     # ṗ
    "\u0120": r"\dot{G}",     # Ġ
    "\u0121": r"\dot{g}",     # ġ
    "\u010E": r"\dot{D}",     # Ď (caron, but close)
    # Pre-composed bar/macron letters
    "\u1E21": r"\bar{g}",     # ḡ
    "\u0100": r"\bar{A}",     # Ā
    "\u0101": r"\bar{a}",     # ā
    "\u00FD": r"\'{y}",       # ý (y acute — author names)
    "\u00F4": r"\^{o}",       # ô (o circumflex — author names)
    # Blackboard bold
    "\u2124": r"\mathbb{Z}",
    "\u211D": r"\mathbb{R}",
    "\u2102": r"\mathbb{C}",
    "\u2115": r"\mathbb{N}",
    # Fractions
    "\u00BD": r"\tfrac{1}{2}",
    "\u00BC": r"\tfrac{1}{4}",
    "\u00BE": r"\tfrac{3}{4}",
    # Unicode minus (U+2212) — needs math mode
    "\u2212": "-",
}

# Unicode subscript characters → LaTeX subscript
SUBSCRIPT_MAP = {
    "\u2080": "0", "\u2081": "1", "\u2082": "2", "\u2083": "3",
    "\u2084": "4", "\u2085": "5", "\u2086": "6", "\u2087": "7",
    "\u2088": "8", "\u2089": "9",
    "\u2090": "a",  # ₐ
    "\u2091": "e",  # ₑ
    "\u2092": "o",  # ₒ
    "\u2093": "x",  # ₓ
    "\u1D62": "i",  # ᵢ
    "\u2C7C": "j",  # ⱼ
    "\u2096": "k",  # ₖ
    "\u2097": "l",  # ₗ
    "\u2098": "m",  # ₘ
    "\u2099": "n",  # ₙ
    "\u209A": "p",  # ₚ
    "\u1D63": "r",  # ᵣ
    "\u209B": "s",  # ₛ
    "\u209C": "t",  # ₜ
    "\u1D64": "u",  # ᵤ
    "\u1D65": "v",  # ᵥ
    "\u208B": "-",  # ₋ subscript minus
    "\u208A": "+",  # ₊ subscript plus
    "\u1D67": r"\gamma",  # ᵧ subscript gamma
}

# Additional superscript modifier letters
SUPERSCRIPT_MAP_EXTRA = {
    "\u207F": "n",   # ⁿ
    "\u1D40": "T",   # ᵀ (superscript T — transpose)
    "\u1D45": r"\alpha",  # ᵅ (superscript alpha)
    "\u1D5D": r"\beta",   # ᵝ (superscript beta)
}

# Unicode superscript characters → LaTeX superscript
SUPERSCRIPT_MAP = {
    "\u2070": "0", "\u00B9": "1", "\u00B2": "2", "\u00B3": "3",
    "\u2074": "4", "\u2075": "5", "\u2076": "6", "\u2077": "7",
    "\u2078": "8", "\u2079": "9",
    "\u207B": "-",   # superscript minus ⁻
    "\u207A": "+",   # superscript plus ⁺
    "\u207D": "(",   # superscript left paren ⁽
    "\u207E": ")",   # superscript right paren ⁾
    "\u1D58": "u",   # ᵘ
    "\u1D5B": "v",   # ᵛ
}

# Combining diacritics (U+0300 range) — these follow a base character
COMBINING_DIACRITICS = {
    "\u0302": r"\hat",      # combining circumflex accent  ̂
    "\u0304": r"\bar",      # combining macron  ̄
    "\u0307": r"\dot",      # combining dot above  ̇
    "\u0303": r"\tilde",    # combining tilde  ̃
    "\u0308": r'\"',        # combining diaeresis  ̈
    "\u030C": r"\check",    # combining caron  ̌
}

# Pre-composed hat characters (some systems use these instead of combining)
HAT_CHARS = {
    "\u011C": r"\hat{G}",  # Ĝ
    "\u011D": r"\hat{g}",  # ĝ
    "\u0125": r"\hat{h}",  # ĥ
    "\u015C": r"\hat{S}",  # Ŝ
    "\u015D": r"\hat{s}",  # ŝ
    "\u00C2": r"\hat{A}",  # Â
    "\u00E2": r"\hat{a}",  # â
    "\u0108": r"\hat{C}",  # Ĉ
    "\u0109": r"\hat{c}",  # ĉ
    "\u0134": r"\hat{J}",  # Ĵ
    "\u0135": r"\hat{j}",  # ĵ
    "\u0174": r"\hat{W}",  # Ŵ
    "\u0175": r"\hat{w}",  # ŵ
    "\u00EA": r"\hat{e}",  # ê
}

# Box drawing chars → remove or replace
BOX_DRAWING = set(chr(c) for c in range(0x2500, 0x2580))


# ─────────────────────────────────────────────────────────────
# Citation patterns: author(s) (year) → \cite{key}
# ─────────────────────────────────────────────────────────────

CITATION_MAP = [
    # Multi-author first (more specific patterns before less specific)
    (r"Bertotti,?\s*Iess\s*(?:&|and)\s*Tortora\s*\(?2003\)?", "BertottiIessTortora2003"),
    (r"Hawking,?\s*Perry\s*(?:&|and)\s*Strominger\s*\(?2016\)?", "HawkingPerryStrominger2016"),
    (r"Aspect,?\s*Grangier\s*(?:&|and)\s*Roger\s*\(?1982\)?", "AspectGrangierRoger1982"),
    (r"Maldacena\s*(?:&|and)\s*Susskind\s*\(?2013\)?", "MaldacenaSusskind2013"),
    (r"Goroff\s*(?:&|and)\s*Sagnotti\s*\(?1986\)?", "GoroffSagnotti1986"),
    (r"'t\s*Hooft\s*(?:&|and)\s*Veltman\s*\(?1974\)?", "tHooftVeltman1974"),
    (r"Minakshisundaram\s*(?:&|and)\s*Pleijel\s*\(?1949\)?", "MinakshisundaramPleijel1949"),
    (r"Appelquist\s*(?:&|and)\s*Chodos\s*\(?1983\)?", "AppelquistChodos1983"),
    (r"Coleman\s*(?:&|and)\s*De\s*Luccia\s*\(?1980\)?", "ColemanDeLuccia1980"),
    (r"Strominger\s*(?:&|and)\s*Vafa\s*\(?1996\)?", "StromingerVafa1996"),
    (r"Aharonov\s*(?:&|and)\s*Bohm\s*\(?1959\)?", "AharonovBohm1959"),
    (r"Berry\s*(?:&|and)\s*Robbins\s*\(?1997\)?", "BerryRobbins1997"),
    (r"Leinaas\s*(?:&|and)\s*Myrheim\s*\(?1977\)?", "LeinaasMyrhei1977"),
    (r"Overduin\s*(?:&|and)\s*Wesson\s*\(?1997\)?", "OverduinWesson1997"),
    (r"Ryu\s*(?:&|and)\s*Takayanagi\s*\(?2006\)?", "RyuTakayanagi2006"),
    (r"Bailin\s*(?:&|and)\s*Love\s*\(?1987\)?", "BailinLove1987"),
    (r"Bernal,?\s*Verde\s*(?:&|and)\s*Riess\s*\(?2016\)?", "BernalVerdeRiess2016"),
    (r"Goldberger\s*(?:&|and)\s*Wise\s*\(?1999\)?", "GoldbergerWise1999"),
    (r"Horava\s*(?:&|and)\s*Witten\s*\(?1996\)?", "HoravaWitten1996"),
    (r"Gross\s*(?:&|and)\s*Perry\s*\(?1983\)?", "GrossPerryMonopole1983"),
    (r"Caldwell[\s-]*Linder\s*\(?2005\)?", "CaldwellLinder2005"),
    # et al. patterns
    (r"Hensen\s*et\s*al\.?\s*\(?2015\)?", "Hensenetal2015"),
    (r"Bartolomei\s*et\s*al\.?\s*\(?2020\)?", "Bartolomeietal2020"),
    (r"Nakamura\s*et\s*al\.?\s*\(?2020\)?", "Nakamuraetal2020"),
    (r"Lee\s*et\s*al\.?\s*\(?2020\)?", "Leeetal2020"),
    (r"Tonomura\s*et\s*al\.?\s*\(?1986\)?", "Tonomuraetal1986"),
    (r"Gonzalo\s*et\s*al\.?\s*\(?2024\)?", "GonzaloNeutrinoTowers2024"),
    (r"Cooke\s*et\s*al\.?\s*\(?2018\)?", "Cooke2018_DH"),
    (r"Kapner\s*et\s*al\.?\s*\(?2007\)?", "Kapneretal2007"),
    (r"Webb\s*et\s*al\.?\s*\(?2011\)?", "Webbetal2011"),
    (r"Abbott\s*et\s*al\.?\s*\(?2016\)?", "LIGO2016"),
    (r"Abbott\s*et\s*al\.?\s*\(?2017\)?", "LIGOMultimessenger2017"),
    (r"Obied\s*et\s*al\.?\s*\(?2023\)?", "ObiedDarkDimensionS82023"),
    (r"Bedroya\s*et\s*al\.?\s*\(?2025\)?", "BedroyaVafa2025"),
    (r"Vafa\s*et\s*al\.?\s*\(?2022\)?", "VafaDarkDimension2022"),
    (r"Ashtekar\s*et\s*al\.?\s*\(?1998\)?", "Ashtekar1998"),
    # Single author
    (r"van\s*de\s*Ven\s*\(?1992\)?", "vandeVen1992"),
    (r"Epstein\s*\(?1903\)?", "Epstein1903"),
    (r"Terras\s*\(?1985\)?", "Terras1985"),
    (r"Seeley\s*\(?1967\)?", "Seeley1967"),
    (r"Vassilevich\s*\(?2003\)?", "Vassilevich2003"),
    (r"Kaluza\s*\(?1921\)?", "Kaluza1921"),
    (r"Klein\s*\(?1926\)?", "Klein1926"),
    (r"Cho\s*\(?1975\)?", "Cho1975"),
    (r"Witten\s*\(?1981\)?", "Witten1981"),
    (r"Witten\s*\(?1982\)?", "Witten1982"),
    (r"Witten\s*\(?1995\)?", "Witten1995"),
    (r"Bell\s*\(?1964\)?", "Bell1964"),
    (r"CHSH\s*\(?1969\)?", "CHSH1969"),
    (r"Tsirelson\s*\(?1980\)?", "Tsirelson1980"),
    (r"Bekenstein\s*\(?1973\)?", "Bekenstein1973"),
    (r"Hawking\s*\(?1975\)?", "Hawking1975"),
    (r"Woodhouse\s*\(?1992\)?", "Woodhouse1992"),
    (r"DeWitt\s*\(?1967\)?", "DeWitt1967"),
    (r"DeWitt\s*\(?1965\)?", "DeWitt1965"),
    (r"Sannan\s*\(?1986\)?", "Sannan1986"),
    (r"Chambers\s*\(?1960\)?", "Chambers1960"),
    (r"Bogoliubov\s*\(?1957\)?", "Bogoliubov1957"),
    (r"Hepp\s*\(?1966\)?", "Hepp1966"),
    (r"Zimmermann\s*\(?1969\)?", "Zimmermann1969"),
    (r"Hosotani\s*\(?1983\)?", "Hosotani1983"),
    (r"Sorkin\s*\(?1983\)?", "SorkinMonopole1983"),
    (r"Rovelli\s*\(?1996\)?", "Rovelli1996"),
    (r"Pauli\s*\(?1940\)?", "Pauli1940"),
    (r"Dirac\s*\(?1931\)?", "Dirac1931"),
    (r"Srednicki\s*\(?1993\)?", "Srednicki1993"),
    (r"Nahm\s*\(?1978\)?", "Nahm1978"),
    (r"Planck\s*\(?2018\)?", "Planck2018_VI"),
    # More single authors
    (r"Fuchs\s*\(?2010\)?", "Fuchs2010"),
    (r"Everett\s*\(?1957\)?", "Everett1957"),
    (r"Bohm\s*\(?1952\)?", "Bohm1952"),
    (r"Casimir\s*\(?1948\)?", "Casimir1948"),
    # More multi-author
    (r"Streater\s*(?:&|and)\s*Wightman", "StreaterWightman1964"),
    (r"Duck\s*(?:&|and)\s*Sudarshan", "DuckSudarshan1997"),
    (r"Lewis,?\s*Challinor\s*(?:&|and)\s*Lasenby\s*\(?2000\)?", "LewisChallinorLasenby2000"),
    (r"Chevallier\s*(?:&|and)\s*Polarski\s*\(?2001\)?", "ChevallierPolarski2001"),
    (r"Linder\s*\(?2003\)?", "Linder2003"),
    (r"Maldacena\s*\(?1997\)?", "Maldacena1997"),
    (r"Cohen\s*(?:&|and)\s*Kaplan\s*\(?1987\)?", "CohenKaplan1987"),
    (r"Carniani\s*et\s*al\.?\s*\(?2024\)?", "Carnianietal2024"),
    (r"Heymans\s*et\s*al\.?\s*\(?2021\)?", "Heymansetal2021"),
    (r"Dalal\s*et\s*al\.?\s*\(?2023\)?", "Dalaletal2023"),
    (r"Abel\s*et\s*al\.?\s*\(?2020\)?", "Abeletal2020"),
    (r"Berezhiani\s*\(?2005\)?", "Berezhiani2005"),
]


# ─────────────────────────────────────────────────────────────
# Core Unicode conversion
# ─────────────────────────────────────────────────────────────

def final_unicode_pass(text: str) -> str:
    """Comprehensive final pass to convert ALL remaining Unicode to LaTeX.

    Strategy: wrap each math symbol in $...$, then aggressively merge
    adjacent $...$ groups so expressions like $\partial$e/$\partial$x
    become $\partial e/\partial x$.
    """
    # 1. Text-mode replacements (em/en dashes, accented chars)
    for uni, latex in TEXT_UNICODE.items():
        text = text.replace(uni, latex)

    # 2. Box drawing / bracket characters → remove
    for c in BOX_DRAWING:
        text = text.replace(c, "")
    for c in "\u239B\u239C\u239D\u239E\u239F\u23A0\u239A":
        text = text.replace(c, "")

    # 3. Pre-composed hat characters
    for uni, latex in HAT_CHARS.items():
        if uni in text:
            text = text.replace(uni, f"${latex}$")

    # 4. Combining diacritics
    for combining, cmd in COMBINING_DIACRITICS.items():
        pattern = re.compile(r'([a-zA-Z])' + re.escape(combining))
        text = pattern.sub(lambda m: f"${cmd}{{{m.group(1)}}}$", text)
    # Fix combining diacritics after $...$: $\varphi$̇ → $\dot{\varphi}$
    for combining, cmd in COMBINING_DIACRITICS.items():
        text = re.sub(
            r'\$([^$]+)\$' + re.escape(combining),
            lambda m: f"${cmd}{{{m.group(1)}}}$",
            text
        )

    # 5. Subscript sequences
    sub_pattern = re.compile(
        '([' + ''.join(re.escape(k) for k in SUBSCRIPT_MAP) + ']+)'
    )
    text = sub_pattern.sub(
        lambda m: "$_{" + "".join(SUBSCRIPT_MAP.get(c, c) for c in m.group(1)) + "}$",
        text
    )

    # 6. Superscript sequences
    all_sups = {**SUPERSCRIPT_MAP, **SUPERSCRIPT_MAP_EXTRA}
    sup_pattern = re.compile(
        '([' + ''.join(re.escape(k) for k in all_sups) + ']+)'
    )
    text = sup_pattern.sub(
        lambda m: "$^{" + "".join(all_sups.get(c, c) for c in m.group(1)) + "}$",
        text
    )

    # 7. Math-mode Unicode symbols
    for uni, latex in MATH_UNICODE.items():
        if uni in text:
            if uni == "\u2212":
                text = text.replace(uni, "-")
            else:
                text = text.replace(uni, f"${latex}$")

    # 8. AGGRESSIVE merge of adjacent $...$ groups
    # This is the key step: merge $X$<bridge>$Y$ → $X bridge Y$
    # where <bridge> is short math-compatible text (letters, digits, =, +, -, /, etc.)
    text = _merge_adjacent_math(text)

    # 9. Fix bare _ and ^ in text mode
    text = _fix_bare_sub_super(text)

    # 10. Targeted fixes for known broken patterns
    text = _fix_known_patterns(text)

    return text


def _fix_known_patterns(text: str) -> str:
    """Fix specific known broken LaTeX patterns from the conversion."""

    # Pattern 1: e^{i$\cmd$} → $e^{i\cmd}$ ($ inside exponent braces)
    text = re.sub(
        r'e\^\{([^$]*)\$([^$]+)\$([^}]*)\}',
        lambda m: f'$e^{{{m.group(1)}{m.group(2)}{m.group(3)}}}$',
        text
    )

    # Pattern 6: \textbf{X_Y} → \textbf{$X_Y$} (bare _ inside \textbf)
    text = re.sub(
        r'\\textbf\{([A-Za-z]+)_([A-Za-z0-9]+)\}',
        r'\\textbf{$\1_{\2}$}',
        text
    )

    # Pattern 10: } instead of ) for common text patterns
    text = re.sub(r'\((Section [^)}]{1,20})\}', r'(\1)', text)
    text = re.sub(r'\((Appendix [^)}]{1,20})\}', r'(\1)', text)

    return text


def _merge_adjacent_math(text: str) -> str:
    """Merge adjacent $...$ groups separated by short math-compatible bridges.

    $\partial$e/$\partial$x → $\partial e/\partial x$
    $\alpha$_{EM} → $\alpha_{EM}$
    |$S$| = 2$\sqrt{}$2 → $|S| = 2\sqrt{2}$
    """
    # Pattern: $...$ followed by short bridge then $...$
    # Bridge: very short math-compatible content (NO spaces — spaces usually mean prose)
    # Allow: single letters/digits, =, +, -, /, |, (, ), _, ^, {, }
    bridge = r'[a-zA-Z0-9=+\-*/().|,^_{}]{0,8}'

    # Merge $A$bridge$B$ → $A bridge B$
    merge_pat = re.compile(r'\$([^$]+)\$(' + bridge + r')\$([^$]+)\$')

    # Iterate because merging creates new adjacent pairs
    for _ in range(10):
        new_text = merge_pat.sub(r'$\1 \2 \3$', text)
        if new_text == text:
            break
        text = new_text

    # Also merge $X$_{a} → $X_{a}$ and $X$^{b} → $X^{b}$
    for _ in range(3):
        text = re.sub(r'\$([^$]+)\$([_^]\{[^}]*\})', r'$\1\2$', text)

    # Clean up double spaces inside $...$
    text = re.sub(r'\$([^$]*)\$', lambda m: '$' + re.sub(r'  +', ' ', m.group(1)).strip() + '$', text)

    # Remove empty math: $$
    text = text.replace("$$", "")

    return text


def _fix_bare_sub_super(text: str) -> str:
    """Wrap bare subscript/superscript expressions in math mode.

    Processes only text-mode lines (not inside equation environments).
    """
    lines = text.split('\n')
    in_math_env = False
    result = []

    math_envs = {'equation', 'align', 'gather', 'multline',
                 'equation*', 'align*', 'gather*', 'multline*'}

    for line in lines:
        stripped = line.strip()

        for env in math_envs:
            if f'\\begin{{{env}}}' in stripped:
                in_math_env = True
            if f'\\end{{{env}}}' in stripped:
                in_math_env = False

        if in_math_env:
            result.append(line)
            continue

        # Merge fragmented math: $\cmd$_{x} → $\cmd_{x}$
        for _ in range(3):
            line = re.sub(r'\$([^$]+)\$([_^]\{[^}]*\})', r'$\1\2$', line)

        # Wrap bare word_{...} or word^{...} NOT inside $...$
        line = _wrap_bare_in_line(line)

        result.append(line)

    return '\n'.join(result)


def _wrap_bare_in_line(line: str) -> str:
    """Find bare subscript/superscript in text portions of a line and wrap in $."""
    parts = re.split(r'(\$[^$]*\$)', line)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            result.append(part)
        else:
            # Wrap: Word_{stuff} or Word^{stuff} with braces (not after \)
            part = re.sub(
                r'(?<!\\)([A-Za-z][A-Za-z0-9]*)([_^]\{[^}]*\}(?:[_^]\{[^}]*\})*)',
                lambda m: f'${m.group(1)}{m.group(2)}$',
                part
            )
            # Bare _{...} not preceded by letter or $
            part = re.sub(
                r'(?<![A-Za-z\\$])([_^]\{[^}]*\}(?:[_^]\{[^}]*\})*)',
                lambda m: f'${m.group(1)}$',
                part
            )
            # Bare word_word or word^word WITHOUT braces (e.g., N_eff, M_P, w_a)
            part = re.sub(
                r'(?<!\\)([A-Za-z][A-Za-z0-9]*)_([A-Za-z][A-Za-z0-9]*)',
                lambda m: f'${m.group(1)}_{{{m.group(2)}}}$',
                part
            )
            part = re.sub(
                r'(?<!\\)([A-Za-z][A-Za-z0-9]*)\^([A-Za-z0-9]+)',
                lambda m: f'${m.group(1)}^{{{m.group(2)}}}$',
                part
            )
            result.append(part)
    return ''.join(result)


def convert_unicode_in_math(text: str) -> str:
    """Replace Unicode math symbols with LaTeX commands inside math context.
    Used inside equation environments where we DON'T want $ wrapping.
    """
    # Pre-composed hats
    for uni, latex in HAT_CHARS.items():
        text = text.replace(uni, latex)

    # Combining diacritics
    for combining, cmd in COMBINING_DIACRITICS.items():
        pattern = re.compile(r'([a-zA-Z])' + re.escape(combining))
        text = pattern.sub(lambda m: f"{cmd}{{{m.group(1)}}}", text)

    # Subscripts
    sub_pattern = re.compile(
        '([' + ''.join(re.escape(k) for k in SUBSCRIPT_MAP) + ']+)'
    )
    text = sub_pattern.sub(
        lambda m: "_{" + "".join(SUBSCRIPT_MAP.get(c, c) for c in m.group(1)) + "}",
        text
    )

    # Superscripts
    all_sups = {**SUPERSCRIPT_MAP, **SUPERSCRIPT_MAP_EXTRA}
    sup_pattern = re.compile(
        '([' + ''.join(re.escape(k) for k in all_sups) + ']+)'
    )
    text = sup_pattern.sub(
        lambda m: "^{" + "".join(all_sups.get(c, c) for c in m.group(1)) + "}",
        text
    )

    # Math symbols (no $ wrapping needed — we're already in math)
    for uni, latex in MATH_UNICODE.items():
        text = text.replace(uni, latex)

    # Text-mode replacements that also apply in math
    text = text.replace("\u2014", "---")
    text = text.replace("\u2013", "--")

    return text


# ─────────────────────────────────────────────────────────────
# Markdown → LaTeX conversion functions
# ─────────────────────────────────────────────────────────────

def is_math_line(line: str) -> bool:
    """Heuristic: does this indented line look like a math equation?"""
    stripped = line.strip()
    if not stripped:
        return False
    math_indicators = [
        "=", "+", "∫", "∂", "∇", "Σ", "Π",
        "^{", "_{", "^(", "→", "≈", "≡", "≤", "≥",
        "sin", "cos", "tan", "exp", "log", "ln",
        "lim", "sup", "inf", "det", "dim",
        "ψ", "φ", "α", "β", "γ", "δ", "ε", "ζ", "η", "θ",
        "λ", "μ", "ν", "ρ", "σ", "τ", "ω", "Λ", "Γ", "Δ",
        "ℏ", "∞", "diag(", "Tr[", "Tr(",
        "d⁴x", "d⁵x", "d^4x", "d^5x",
        "\\frac", "\\int", "\\sum", "\\partial",
    ]
    for ind in math_indicators:
        if ind in stripped:
            return True
    if re.search(r'[a-zA-Z][_^][{(0-9a-zA-Z]', stripped):
        return True
    if len(stripped) < 100 and re.search(r'[=<>≈≡]', stripped):
        return True
    return False


def convert_equation_block(block_lines: list[str]) -> str:
    """Convert an indented equation block to LaTeX equation/align environment."""
    math_count = sum(1 for l in block_lines if is_math_line(l))
    if math_count == 0:
        return "\n".join(block_lines)

    converted = [convert_unicode_in_math(line) for line in block_lines]

    # Remove markdown bold markers from equations
    converted = [re.sub(r'\*\*(.+?)\*\*', r'\1', l) for l in converted]

    # Filter blank lines
    non_empty = [l for l in converted if l.strip()]

    if len(non_empty) == 1:
        return f"\\begin{{equation}}\n    {non_empty[0].strip()}\n\\end{{equation}}"
    else:
        align_lines = []
        for line in non_empty:
            stripped = line.strip()
            if "=" in stripped and not stripped.startswith("where") and not stripped.startswith("with"):
                parts = stripped.split("=", 1)
                align_lines.append(f"    {parts[0].rstrip()} &= {parts[1].lstrip()}")
            else:
                align_lines.append(f"    & {stripped}")
        content = " \\\\\n".join(align_lines)
        return f"\\begin{{align}}\n{content}\n\\end{{align}}"


def convert_table(lines: list[str]) -> str:
    """Convert a markdown table to LaTeX tabular."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if all(re.match(r'^[-:]+$', c) for c in cells):
            continue
        rows.append(cells)

    if not rows:
        return ""

    ncols = len(rows[0])
    col_spec = "l" * ncols

    result = []
    result.append("\\begin{table}[h]")
    result.append("\\centering")
    result.append(f"\\begin{{tabular}}{{{col_spec}}}")
    result.append("\\toprule")

    for i, row in enumerate(rows):
        while len(row) < ncols:
            row.append("")
        cells = [convert_inline_formatting(cell) for cell in row]
        result.append(" & ".join(cells) + " \\\\")
        if i == 0:
            result.append("\\midrule")

    result.append("\\bottomrule")
    result.append("\\end{tabular}")
    result.append("\\end{table}")
    return "\n".join(result)


def convert_inline_formatting(text: str) -> str:
    """Convert markdown inline formatting to LaTeX."""
    # Bold: **text** → \textbf{text}
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    # Italic: *text* → \textit{text}
    text = re.sub(r'(?<!\w)\*([^*]+?)\*(?!\w)', r'\\textit{\1}', text)
    # Inline code: `text` → $text$ (if math) or \texttt{text}
    def code_replace(m):
        content = m.group(1)
        if is_math_line(content) or re.search(r'[=+*/^_αβγδεζηθλμνρστφψωΛΣΔΓ∂∇∫ℏ\-]', content):
            converted = convert_unicode_in_math(content)
            return f"${converted}$"
        return f"\\texttt{{{content}}}"
    text = re.sub(r'`([^`]+)`', code_replace, text)
    return text


def convert_citations(text: str) -> str:
    """Convert inline author-year citations to \\cite{key}."""
    for pattern, key in CITATION_MAP:
        # Parenthesized: (Author YYYY) → \cite{key}
        text = re.sub(r'\(' + pattern + r'\)', r'\\cite{' + key + '}', text, flags=re.IGNORECASE)
        # Bare: Author YYYY → \cite{key} (but not inside existing \cite)
        text = re.sub(r'(?<!\\cite\{)(?<!\w)' + pattern + r'(?!\w)',
                       r'\\cite{' + key + '}', text, flags=re.IGNORECASE)
    # Fix double-nested \cite{\cite{...}}
    text = re.sub(r'\\cite\{\\cite\{([^}]+)\}\}', r'\\cite{\1}', text)
    # Fix multi-cite with parens: (\cite{A}, \cite{B}) → \cite{A,B}
    text = re.sub(
        r'\(\\cite\{([^}]+)\},\s*\\cite\{([^}]+)\}\)',
        r'\\cite{\1,\2}', text
    )
    text = re.sub(
        r'\(\\cite\{([^}]+)\},\s*\\cite\{([^}]+)\},\s*\\cite\{([^}]+)\}\)',
        r'\\cite{\1,\2,\3}', text
    )
    # Fix remaining (\cite{...}. → \cite{...}  (dangling parens)
    text = re.sub(r'\(\\cite\{([^}]+)\}([^)]*)\.\s*$', r'\\cite{\1}\2.', text, flags=re.MULTILINE)
    text = re.sub(r'\(\\cite\{([^}]+)\}([^)]{0,50})\)', r'\\cite{\1}\2', text)
    return text


def convert_theorem_block(text: str) -> str:
    """Detect and convert theorem/proof/definition/lemma blocks."""
    # Theorem: **Theorem X.Y (Title).**
    text = re.sub(
        r'\\textbf\{Theorem\s+(\S+)\s+\(([^)]+)\)\.\}',
        lambda m: f"\\begin{{theorem}}[{m.group(2)}]\n\\label{{thm:{m.group(1).replace('.', '')}}}",
        text
    )
    # Also catch the bold-only format from markdown conversion
    text = re.sub(
        r'\*\*Theorem\s+(\S+)\s+\(([^)]+)\)\.\*\*',
        lambda m: f"\\begin{{theorem}}[{m.group(2)}]\n\\label{{thm:{m.group(1).replace('.', '')}}}",
        text
    )

    # Lemma
    text = re.sub(
        r'\\textbf\{Lemma\s+(\S+)\s+\(([^)]+)\)\.\}',
        lambda m: f"\\begin{{lemma}}[{m.group(2)}]\n\\label{{lem:{m.group(1).replace('.', '')}}}",
        text
    )

    # Proposition
    text = re.sub(
        r'\\textbf\{Proposition\s+(\S+)\s+\(([^)]+)\)\.\}',
        lambda m: f"\\begin{{proposition}}[{m.group(2)}]\n\\label{{prop:{m.group(1).replace('.', '')}}}",
        text
    )

    # Definition
    text = re.sub(
        r'\\textbf\{Definition\s+(\S+)\s+\(([^)]+)\)\.\}',
        lambda m: f"\\begin{{definition}}[{m.group(2)}]\n\\label{{def:{m.group(1).replace('.', '')}}}",
        text
    )

    # Corollary
    text = re.sub(
        r'\\textbf\{Corollary\s+(\S+)\s+\(([^)]+)\)\.\}',
        lambda m: f"\\begin{{corollary}}[{m.group(2)}]\n\\label{{cor:{m.group(1).replace('.', '')}}}",
        text
    )

    # Proof blocks: **Proof.** ... ∎ or **Proof:**
    text = re.sub(r'\\textbf\{Proof\.\}', r'\\begin{proof}', text)
    text = re.sub(r'\\textbf\{Proof:\}', r'\\begin{proof}', text)
    text = re.sub(r'\*\*Proof\.\*\*', r'\\begin{proof}', text)
    text = re.sub(r'\*\*Proof:\*\*', r'\\begin{proof}', text)

    # Close theorem-like environments: insert \end before the next \subsection, \section, or \begin{theorem/lemma/...}
    # Also close proofs: insert \end{proof} before the next section/theorem or at QED marker
    # Handle QED marker (blacksquare) → \end{proof}
    text = text.replace('$\\blacksquare$', '\\end{proof}')
    text = re.sub(r'\s*\\qed\b', '\n\\\\end{proof}', text)

    # For each unclosed \begin{env}, find where it should close and insert \end{env}
    for env in ['theorem', 'lemma', 'proposition', 'corollary', 'definition']:
        text = _close_environments(text, env)

    # Close any remaining unclosed proofs before section breaks
    text = _close_environments(text, 'proof')

    return text


def _close_environments(text: str, env: str) -> str:
    """Insert \\end{env} before the next structural break for unclosed environments."""
    begin_tag = f'\\begin{{{env}}}'
    end_tag = f'\\end{{{env}}}'

    # Work through the text tracking open/close balance
    result_parts = []
    remaining = text
    while begin_tag in remaining:
        # Find next \begin{env}
        idx = remaining.index(begin_tag)
        result_parts.append(remaining[:idx])
        remaining = remaining[idx:]

        # Count opens/closes from here forward to find if this one is already closed
        # Look for the next structural break (section, subsection, or another begin of same type)
        after_begin = remaining[len(begin_tag):]

        # Find where this environment should end
        # Candidates: next \subsection, \section, next \begin{same env}, or explicit \end{env}
        close_candidates = []
        for marker in [f'\\subsection{{', f'\\section{{', begin_tag]:
            pos = after_begin.find(marker)
            if pos >= 0:
                close_candidates.append(pos)

        # Check if there's already an \end{env} before any structural break
        end_pos = after_begin.find(end_tag)
        earliest_break = min(close_candidates) if close_candidates else len(after_begin)

        if end_pos >= 0 and end_pos < earliest_break:
            # Already closed properly — skip
            result_parts.append(remaining[:len(begin_tag)])
            remaining = after_begin
        else:
            # Need to insert \end{env} before the structural break
            if close_candidates:
                insert_at = earliest_break
            else:
                insert_at = len(after_begin)

            # Insert \end{env} with a blank line before the break
            result_parts.append(remaining[:len(begin_tag)])
            result_parts.append(after_begin[:insert_at])
            result_parts.append(f'\n{end_tag}\n\n')
            remaining = after_begin[insert_at:]

    result_parts.append(remaining)
    return ''.join(result_parts)

    # Result / named result blocks
    text = re.sub(
        r'\\textbf\{Result\s+(\d+)\s*[-]+\s*(.+?)\.\}',
        lambda m: f"\\textbf{{Result {m.group(1)} --- {m.group(2)}.}}",
        text
    )

    return text


def convert_section_header(line: str, header_offset: int = 0) -> str:
    """Convert markdown header to LaTeX section command.

    header_offset: shift header levels (e.g., -1 promotes ## to \\section)
    """
    m = re.match(r'^(#{1,4})\s+(.+)$', line)
    if not m:
        return line
    level = len(m.group(1)) + header_offset
    title = m.group(2).strip()

    # Strip section numbers: "Section 2 —", "2.1", "S.3.1", "A.2", etc.
    title = re.sub(r'^(?:Section\s+)?\d+[Xx]?\s*[:\u2014\u2013-]\s*', '', title)
    title = re.sub(r'^(?:Appendix\s+)?[A-Z]\s*[:\u2014\u2013-]\s*', '', title)
    title = re.sub(r'^\d+(?:\.\d+)*\s+', '', title)
    title = re.sub(r'^[A-Z]\.\d+(?:\.\d+)*\s+', '', title)

    title = convert_inline_formatting(title)

    commands = {1: "section", 2: "subsection", 3: "subsubsection", 4: "paragraph"}
    level = max(1, min(4, level))  # clamp
    cmd = commands[level]

    return f"\\{cmd}{{{title}}}"


def convert_blockquote(lines: list[str]) -> str:
    """Convert > blockquote to LaTeX quote environment."""
    content = []
    for line in lines:
        stripped = re.sub(r'^>\s?', '', line)
        content.append(stripped)
    text = "\n".join(content)
    text = convert_inline_formatting(text)
    return f"\\begin{{quote}}\n{text}\n\\end{{quote}}"


def convert_list_block(lines: list[str]) -> str:
    """Convert markdown list to LaTeX itemize/enumerate."""
    # Detect if numbered list
    is_numbered = any(re.match(r'^\d+\.\s', l.strip()) for l in lines if l.strip())
    env = "enumerate" if is_numbered else "itemize"

    result = [f"\\begin{{{env}}}"]
    current_item = []

    for line in lines:
        stripped = line.strip()
        if re.match(r'^[-*]\s', stripped):
            if current_item:
                result.append("  \\item " + " ".join(current_item))
            current_item = [convert_inline_formatting(stripped[2:])]
        elif re.match(r'^\d+\.\s', stripped):
            if current_item:
                result.append("  \\item " + " ".join(current_item))
            current_item = [convert_inline_formatting(re.sub(r'^\d+\.\s', '', stripped))]
        elif stripped and current_item:
            current_item.append(convert_inline_formatting(stripped))

    if current_item:
        result.append("  \\item " + " ".join(current_item))

    result.append(f"\\end{{{env}}}")
    return "\n".join(result)


def process_markdown_file(filepath: Path, header_offset: int = 0,
                          skip_top_header: bool = True) -> str:
    """Convert a single markdown file to LaTeX body content.

    header_offset: shift header levels (e.g., -1 promotes ## to \\section)
    skip_top_header: if True, skip the first # header (handled by document structure)
    """
    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")
    output = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip the top-level header — handled by document structure
        if skip_top_header and i == 0 and re.match(r'^#\s+', line):
            i += 1
            continue

        # Horizontal rule — skip
        if re.match(r'^---+\s*$', stripped):
            i += 1
            continue

        # Section headers
        if re.match(r'^#{1,4}\s+', line):
            output.append("")
            output.append(convert_section_header(line, header_offset))
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i])
                i += 1
            output.append("")
            output.append(convert_blockquote(block))
            continue

        # Table
        if "|" in stripped and i + 1 < len(lines) and re.search(r'\|[-:]+\|', lines[i + 1]):
            table_lines = []
            while i < len(lines) and "|" in lines[i].strip():
                table_lines.append(lines[i])
                i += 1
            output.append("")
            output.append(convert_table(table_lines))
            continue

        # Indented block (potential equation)
        if line.startswith("    ") and stripped:
            block_lines = []
            while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
                if lines[i].strip():
                    block_lines.append(lines[i][4:])
                elif block_lines:
                    block_lines.append("")
                i += 1
                if not lines[i - 1].strip() and i < len(lines) and not lines[i].startswith("    "):
                    break
            while block_lines and not block_lines[-1].strip():
                block_lines.pop()
            if block_lines:
                output.append("")
                output.append(convert_equation_block(block_lines))
            continue

        # List
        if re.match(r'^[-*]\s', stripped) or re.match(r'^\d+\.\s', stripped):
            list_lines = []
            while i < len(lines):
                s = lines[i].strip()
                if re.match(r'^[-*]\s', s) or re.match(r'^\d+\.\s', s):
                    list_lines.append(lines[i])
                    i += 1
                elif s and list_lines and not re.match(r'^#{1,4}\s', s) and not s.startswith(">"):
                    list_lines.append(lines[i])
                    i += 1
                elif not s:
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and (re.match(r'^[-*]\s', lines[j].strip()) or
                                            re.match(r'^\d+\.\s', lines[j].strip())):
                        list_lines.append(lines[i])
                        i += 1
                    else:
                        break
                else:
                    break
            output.append("")
            output.append(convert_list_block(list_lines))
            continue

        # Empty line
        if not stripped:
            output.append("")
            i += 1
            continue

        # Regular paragraph
        para_lines = []
        while i < len(lines):
            s = lines[i].strip()
            if not s:
                break
            if re.match(r'^#{1,4}\s', s):
                break
            if s.startswith(">"):
                break
            if lines[i].startswith("    "):
                break
            if "|" in s and i + 1 < len(lines) and re.search(r'\|[-:]+\|', lines[i + 1]):
                break
            if re.match(r'^[-*]\s', s):
                break
            if re.match(r'^---+\s*$', s):
                break
            para_lines.append(s)
            i += 1

        if para_lines:
            para = " ".join(para_lines)
            para = convert_inline_formatting(para)
            output.append(para)

    result = "\n".join(output)

    # Post-process: convert Unicode inside equation environments
    def convert_math_env(m):
        return convert_unicode_in_math(m.group(0))

    result = re.sub(r'\$[^$]+\$', convert_math_env, result)
    result = re.sub(
        r'\\begin\{(?:equation|align|gather|multline)\*?\}.*?\\end\{(?:equation|align|gather|multline)\*?\}',
        convert_math_env, result, flags=re.DOTALL
    )

    # Convert theorem environments
    result = convert_theorem_block(result)

    # Convert citations
    result = convert_citations(result)

    # Escape bare % (not already escaped)
    result = re.sub(r'(?<!\\)%', r'\\%', result)

    # Fix e^(iθ) patterns → e^{iθ}
    result = result.replace("e^(i", r"e^{i")
    result = re.sub(r"e\^\{i([^}]+)\)", r"e^{i\1}", result)

    return result


# ─────────────────────────────────────────────────────────────
# Missing bibliography entries
# ─────────────────────────────────────────────────────────────

def append_missing_bib_entries(bib_path: Path, entries: str):
    """Append missing bib entries to a .bib file, skipping any keys already present."""
    existing = bib_path.read_text(encoding="utf-8")
    # Extract existing keys
    existing_keys = set(re.findall(r'@\w+\{(\w+),', existing))
    # Parse entries to add
    new_entries = []
    for block in re.split(r'\n(?=@)', entries.strip()):
        if not block.strip():
            continue
        m = re.match(r'@\w+\{(\w+),', block)
        if m and m.group(1) not in existing_keys:
            new_entries.append(block.strip())
    if new_entries:
        with open(bib_path, "a", encoding="utf-8") as f:
            f.write("\n\n% === Auto-added missing entries ===\n\n")
            f.write("\n\n".join(new_entries))
            f.write("\n")
        print(f"  Added {len(new_entries)} missing bib entries to {bib_path.name}")


EXTRA_BIB_PAPER1 = r"""
@article{Chambers1960,
  author  = {Chambers, R. G.},
  title   = {Shift of an Electron Interference Pattern by Enclosed Magnetic Flux},
  journal = {Phys. Rev. Lett.},
  volume  = {5},
  pages   = {3--5},
  year    = {1960},
  doi     = {10.1103/PhysRevLett.5.3},
}

@article{DeWitt1965,
  author    = {DeWitt, Bryce S.},
  title     = {Dynamical Theory of Groups and Fields},
  publisher = {Gordon and Breach},
  year      = {1965},
}

@article{BernalVerdeRiess2016,
  author  = {Bernal, Jos{\'e} Luis and Verde, Licia and Riess, Adam G.},
  title   = {The trouble with $H_0$},
  journal = {J. Cosmol. Astropart. Phys.},
  volume  = {2016},
  number  = {10},
  pages   = {019},
  year    = {2016},
  doi     = {10.1088/1475-7516/2016/10/019},
}

@article{Planck2018_VI,
  author  = {{Planck Collaboration}},
  title   = {Planck 2018 results. {VI}. Cosmological parameters},
  journal = {Astron. Astrophys.},
  volume  = {641},
  pages   = {A6},
  year    = {2020},
  doi     = {10.1051/0004-6361/201833910},
}

@article{Cooke2018_DH,
  author  = {Cooke, Ryan J. and Pettini, Max and Steidel, Charles C.},
  title   = {One Percent Determination of the Primordial Deuterium Abundance},
  journal = {Astrophys. J.},
  volume  = {855},
  pages   = {102},
  year    = {2018},
  doi     = {10.3847/1538-4357/aaab53},
}

@article{GonzaloNeutrinoTowers2024,
  author  = {Gonzalo, Eduardo and Montero, Miguel and Obied, Georges and Vafa, Cumrun},
  title   = {Dark Dimension Gravitinos and Missing Corners in the String Landscape},
  journal = {arXiv preprint},
  eprint  = {2401.03730},
  year    = {2024},
}

@article{Dirac1931,
  author  = {Dirac, P. A. M.},
  title   = {Quantised Singularities in the Electromagnetic Field},
  journal = {Proc. R. Soc. Lond. A},
  volume  = {133},
  pages   = {60--72},
  year    = {1931},
  doi     = {10.1098/rspa.1931.0130},
}

@article{Nahm1978,
  author  = {Nahm, Werner},
  title   = {Supersymmetries and their Representations},
  journal = {Nucl. Phys. B},
  volume  = {135},
  pages   = {149--166},
  year    = {1978},
  doi     = {10.1016/0550-3213(78)90218-3},
}

@article{Rovelli1996,
  author  = {Rovelli, Carlo},
  title   = {Relational Quantum Mechanics},
  journal = {Int. J. Theor. Phys.},
  volume  = {35},
  pages   = {1637--1678},
  year    = {1996},
  doi     = {10.1007/BF02302261},
}

@article{Ashtekar1998,
  author  = {Ashtekar, Abhay and Baez, John and Corichi, Alejandro and Krasnov, Kirill},
  title   = {Quantum Geometry and Black Hole Entropy},
  journal = {Phys. Rev. Lett.},
  volume  = {80},
  pages   = {904--907},
  year    = {1998},
  doi     = {10.1103/PhysRevLett.80.904},
}

@article{Everett1957,
  author  = {Everett, Hugh},
  title   = {``Relative State'' Formulation of Quantum Mechanics},
  journal = {Rev. Mod. Phys.},
  volume  = {29},
  pages   = {454--462},
  year    = {1957},
  doi     = {10.1103/RevModPhys.29.454},
}

@article{Bohm1952,
  author  = {Bohm, David},
  title   = {A Suggested Interpretation of the Quantum Theory in Terms of ``Hidden'' Variables. {I}},
  journal = {Phys. Rev.},
  volume  = {85},
  pages   = {166--179},
  year    = {1952},
  doi     = {10.1103/PhysRev.85.166},
}

@article{Fuchs2010,
  author  = {Fuchs, Christopher A.},
  title   = {QBism, the Perimeter of Quantum Bayesianism},
  journal = {arXiv preprint},
  eprint  = {1003.5209},
  year    = {2010},
}

@article{Maldacena1997,
  author  = {Maldacena, Juan},
  title   = {The Large {N} Limit of Superconformal Field Theories and Supergravity},
  journal = {Adv. Theor. Math. Phys.},
  volume  = {2},
  pages   = {231--252},
  year    = {1998},
  doi     = {10.4310/ATMP.1998.v2.n2.a1},
}

@article{Abeletal2020,
  author  = {Abel, Steven A. and Sherrill, Michael F.},
  title   = {Dark Photon Portal into Mirror Particles},
  journal = {Phys. Rev. D},
  volume  = {101},
  pages   = {095031},
  year    = {2020},
  doi     = {10.1103/PhysRevD.101.095031},
}

@article{Berezhiani2005,
  author  = {Berezhiani, Zurab},
  title   = {Mirror World and its Cosmological Consequences},
  journal = {Int. J. Mod. Phys. A},
  volume  = {19},
  pages   = {3775--3806},
  year    = {2004},
  doi     = {10.1142/S0217751X04020075},
}
"""

EXTRA_BIB_PAPER2 = r"""
@article{Leeetal2020,
  author  = {Lee, Jae-Weon and Koh, Inwoo and Jee, M. James},
  title   = {Anyonic statistics in Hall-type systems},
  journal = {Phys. Rev. B},
  volume  = {102},
  pages   = {165150},
  year    = {2020},
}

@article{LewisChallinorLasenby2000,
  author  = {Lewis, Antony and Challinor, Anthony and Lasenby, Anthony},
  title   = {Efficient Computation of Cosmic Microwave Background Anisotropies in Closed Friedmann-Robertson-Walker Models},
  journal = {Astrophys. J.},
  volume  = {538},
  pages   = {473--476},
  year    = {2000},
  doi     = {10.1086/309179},
}

@article{Heymansetal2021,
  author  = {Heymans, Catherine and others},
  title   = {KiDS-1000 Cosmology: Multi-probe weak gravitational lensing and spectroscopic galaxy clustering constraints on cosmological parameters},
  journal = {Astron. Astrophys.},
  volume  = {646},
  pages   = {A140},
  year    = {2021},
  doi     = {10.1051/0004-6361/202039063},
}

@article{Dalaletal2023,
  author  = {Dalal, Ruit and others},
  title   = {Hyper Suprime-Cam Year 3 Results: Cosmology from Cosmic Shear Power Spectra},
  journal = {Phys. Rev. D},
  volume  = {108},
  pages   = {123519},
  year    = {2023},
  doi     = {10.1103/PhysRevD.108.123519},
}

@article{Carnianietal2024,
  author  = {Carniani, Stefano and others},
  title   = {Spectroscopic confirmation of two luminous galaxies at a redshift of 14},
  journal = {Nature},
  volume  = {633},
  pages   = {318--322},
  year    = {2024},
  doi     = {10.1038/s41586-024-07860-9},
}
"""


# ─────────────────────────────────────────────────────────────
# Paper 1 assembly
# ─────────────────────────────────────────────────────────────

PAPER1_PREAMBLE = r"""\documentclass[aps,prd,preprint,superscriptaddress,longbibliography]{revtex4-2}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{amsthm}
\usepackage{mathtools}
\usepackage{physics}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{array}
\usepackage{graphicx}
\usepackage{dcolumn}
\usepackage{bm}

% Theorem environments
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% Custom macros
\newcommand{\edim}{e}
\newcommand{\ecircle}{S^1}
\newcommand{\Mfour}{M^4}
\newcommand{\ebundle}{P(M^4, \mathrm{U}(1))}
\newcommand{\KKmetric}{\hat{G}_{AB}}
\newcommand{\Snought}{S_0^{(L)}}
\newcommand{\Epstein}[2]{E_{#1}(s;\, #2)}
\newcommand{\lP}{l_{\mathrm{P}}}
\newcommand{\GN}{G_{\mathrm{N}}}
\newcommand{\GFive}{\hat{G}_5}
"""

PAPER1_SECTIONS = [
    ("paper-section-1-introduction.md", "Introduction"),
    ("paper-section-2-framework.md", "The Five-Dimensional Framework"),
    ("paper-section-3-five-phenomena.md", "Five Quantum Phenomena Reinterpreted"),
]

PAPER1_SECTION4 = [
    ("paper-section-4-1-aharonov-bohm.md", "The Aharonov--Bohm Effect"),
    ("paper-section-4-2-spin-statistics.md", "The Spin--Statistics Theorem"),
]

PAPER1_SECTIONS_AFTER4 = [
    ("paper-section-5-gravity-bridge.md", "Toward Quantum Gravity: The E-Space Bridge"),
    ("paper-section-5x-quantization-bridge.md", "The Quantization Bridge"),
    ("paper-section-6-connections.md", "Connections to Modern Physics"),
    ("paper-section-7-philosophy.md", "Philosophical Resolution"),
    ("paper-section-8-conclusion.md", "Conclusion"),
]

PAPER1_APPENDICES = [
    ("appendix-A-quantum-dictionary.md", "Quantum Dictionary"),
    ("appendix-B-spin-statistics-derivation.md", "Spin--Statistics Derivation"),
    ("appendix-C-quantitative-demonstrations.md", "Quantitative Demonstrations"),
    ("appendix-D-5d-einstein-equations.md", "5D Einstein Equations"),
    ("appendix-E-quantum-consistency.md", "Quantum Consistency"),
    ("appendix-F-one-loop-computation.md", r"One-Loop Effective Action for 5D Gravity on $M^4 \times S^1$"),
    ("appendix-G-two-loop-computation.md", "Two-Loop Computation"),
    ("appendix-H-testable-predictions.md", "Testable Predictions"),
    ("appendix-I-cassini-fifth-force.md", "Cassini Fifth-Force Constraint"),
    ("appendix-J-non-perturbative-stability.md", "Non-Perturbative Stability"),
    ("appendix-K-higher-loop-epstein.md", "Higher-Loop Epstein Zeta Analysis"),
    ("appendix-L-non-abelian-extension.md", "Non-Abelian Extension"),
    ("appendix-M-hydrogen-atom.md", "Hydrogen Atom"),
    ("appendix-N-gravitational-waves.md", "Gravitational Waves"),
    ("appendix-O-black-hole-entropy.md", "Black Hole Entropy"),
    ("appendix-P-cpt-theorem.md", "CPT Theorem"),
    ("appendix-Q-frw-cosmology.md", "FRW Cosmology"),
    ("appendix-R-running-couplings.md", "Running Couplings"),
    ("appendix-S-finiteness-theorem.md", "Perturbative Finiteness Under Zeta Regularization"),
    ("appendix-T-rigorous-verification.md", "Rigorous Verification"),
    ("appendix-U-goroff-sagnotti-verification.md", "Goroff--Sagnotti Verification"),
    ("appendix-V-vertex-computation.md", "Vertex Computation"),
    ("appendix-W-orbifold-dark-sector.md", "Orbifold Dark Sector"),
    ("appendix-X-strong-cp.md", "Strong CP"),
    ("appendix-Y-hubble-tension.md", "Hubble Tension"),
    ("appendix-Z-neutrino-mass-ordering.md", "Neutrino Mass Ordering"),
]


def build_paper1():
    """Build Paper 1 LaTeX."""
    paper_dir = BASE / "paper1"
    appendix_dir = paper_dir / "appendices"
    out_dir = paper_dir / "etc" / "arxiv"
    out_dir.mkdir(parents=True, exist_ok=True)

    parts = []
    parts.append(PAPER1_PREAMBLE)
    parts.append("\\begin{document}\n")

    parts.append("\\title{The 5D e-Dimension Framework: Quantum Mechanics as Geometry}")
    parts.append("\\author{G.~Six}")
    parts.append("\\affiliation{Independent researcher}")
    parts.append("\\date{\\today}\n")

    # Abstract
    abstract_text = process_markdown_file(paper_dir / "abstract.md")
    parts.append("\\begin{abstract}")
    parts.append(abstract_text)
    parts.append("\\end{abstract}\n")
    parts.append("\\maketitle")
    parts.append("\\tableofcontents\n")

    # Main sections 1-3
    for fname, title in PAPER1_SECTIONS:
        parts.append(f"\n\\section{{{title}}}")
        parts.append(process_markdown_file(paper_dir / fname))

    # Section 4 with subsections
    parts.append("\n\\section{Two Derivations}")
    for fname, title in PAPER1_SECTION4:
        parts.append(f"\n\\subsection{{{title}}}")
        parts.append(process_markdown_file(paper_dir / fname))

    # Sections 5-9 (5x becomes Section 6; subsequent sections shift by one)
    for fname, title in PAPER1_SECTIONS_AFTER4:
        parts.append(f"\n\\section{{{title}}}")
        parts.append(process_markdown_file(paper_dir / fname))

    # Appendices FIRST, then bibliography
    parts.append("\n\\appendix\n")
    for fname, title in PAPER1_APPENDICES:
        parts.append(f"\n\\section{{{title}}}")
        parts.append(process_markdown_file(appendix_dir / fname))

    # Bibliography AFTER appendices
    parts.append("\n\\bibliography{refs}")
    parts.append("\n\\end{document}")

    tex_content = "\n".join(parts)

    # Final comprehensive Unicode pass
    tex_content = final_unicode_pass(tex_content)

    (out_dir / "main.tex").write_text(tex_content, encoding="utf-8")

    # Copy refs.bib and append missing entries
    shutil.copy2(paper_dir / "etc" / "refs.bib", out_dir / "refs.bib")
    append_missing_bib_entries(out_dir / "refs.bib", EXTRA_BIB_PAPER1)

    # Preserve existing short abstract if present (may be hand-edited)
    short_abs = out_dir / "abstract-short.txt"
    if not short_abs.exists():
        generate_short_abstract(paper_dir / "abstract.md", short_abs)

    line_count = tex_content.count("\n") + 1
    print(f"Paper 1: wrote {out_dir / 'main.tex'} ({line_count} lines)")
    print(f"Paper 1: copied {out_dir / 'refs.bib'}")
    print(f"Paper 1: wrote {out_dir / 'abstract-short.txt'}")


def generate_short_abstract(abstract_path: Path, out_path: Path):
    """Generate a shortened abstract placeholder for the arXiv submission form."""
    text = abstract_path.read_text(encoding="utf-8")
    out_path.write_text(
        "% SHORT ABSTRACT FOR ARXIV SUBMISSION FORM\n"
        "% Target: ~250 words, under 1920 characters\n"
        "% Condense from the full abstract below.\n"
        "% Keep paragraphs 1-3 intact; paragraph 4 keep only Goroff-Sagnotti\n"
        "% and two-parameter finiteness; paragraph 5 reduce to 2 sentences;\n"
        "% paragraph 6 keep 19-phenomena + 7-predictions + disclaimer.\n\n"
        + text,
        encoding="utf-8"
    )


# ─────────────────────────────────────────────────────────────
# Paper 2 assembly
# ─────────────────────────────────────────────────────────────

PAPER2_PREAMBLE = r"""\documentclass[prd,twocolumn,nofootinbib,superscriptaddress]{revtex4-2}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{array}
\usepackage{bm}

% Convenience macros
\newcommand{\LCDM}{\Lambda\text{CDM}}
\newcommand{\Neff}{N_{\rm eff}}
\newcommand{\Omegab}{\Omega_b}
\newcommand{\OmegaDM}{\Omega_{\rm DM}}
"""

PAPER2_APPENDICES = [
    ("appendix-A-age-computation.md", "Age of the Universe"),
    ("appendix-B-expansion-history.md", r"Expansion History $H(z)$"),
    ("appendix-C-s8-tension.md", r"$S_8$ Tension Resolution"),
    ("appendix-D-sound-horizon.md", "Sound Horizon"),
    ("appendix-E-mirror-baryogenesis.md", "Mirror Baryogenesis and Cosmic Coincidence"),
    ("appendix-F-thawing-dilaton.md", "Thawing Dilaton"),
    ("appendix-G-cmb-angular-scale.md", "CMB Angular Scale"),
    ("appendix-H-jwst-galaxies.md", "JWST Early Galaxies"),
    ("appendix-I-decisive-tests.md", "Decisive Tests"),
]

PAPER2_FIGURES = {
    "plot_summary.png": "fig_summary.png",
    "plot_s8.png": "fig_s8.png",
    "plot_Hz.png": "fig_Hz.png",
    "plot_wz.png": "fig_wz.png",
    "plot_ages.png": "fig_ages.png",
}

# Figure LaTeX from the conversion guide — inserted at specific locations
PAPER2_FIGURE_LATEX = {
    "section4": r"""
\begin{figure*}
  \includegraphics[width=\textwidth]{fig_summary}
  \caption{Cosmological predictions for the three Paper~2 scenarios
    compared to Planck~\LCDM and the 5D minimal (tower-only) case.
    Scenario~A ($\xi=0.47$, $\theta^*$-matched),
    Scenario~B ($\xi=0.432$, $1/\xi^2$ law), and
    Scenario~C ($\xi=0.4375$, self-consistent $\omega_b$)
    bracket the framework's prediction.}
  \label{fig:summary}
\end{figure*}
""",
    "s8": r"""
\begin{figure}
  \includegraphics[width=\columnwidth]{fig_s8}
  \caption{$S_8$ predictions from the three scenarios compared to
    Planck~2018~(CMB) and three weak lensing surveys (DES~Y3,
    KiDS-1000, HSC~Y3). All three scenarios resolve the $4\sigma$
    tension between CMB and weak lensing.}
  \label{fig:s8}
\end{figure}
""",
    "Hz": r"""
\begin{figure*}
  \includegraphics[width=\textwidth]{fig_Hz}
  \caption{\textit{Left:} Expansion history $H(z)$ for the three
    scenarios and Planck~\LCDM. \textit{Right:} Ratio to \LCDM,
    showing the characteristic 4--5\% peak at $z \sim 0.3$--$0.5$
    from the thawing dilaton. DESI~DR3 will test this at $8\sigma$.}
  \label{fig:Hz}
\end{figure*}
""",
    "wz": r"""
\begin{figure}
  \includegraphics[width=\columnwidth]{fig_wz}
  \caption{Dark energy equation of state $w(z)$. The framework's
    thawing dilaton ($w_0=-0.85$, $w_a=-0.23$; orange) lies within
    the DESI~DR2 $2\sigma$ contour but predicts milder evolution
    than the DESI best-fit (red).}
  \label{fig:wz}
\end{figure}
""",
    "ages": r"""
\begin{figure}
  \includegraphics[width=\columnwidth]{fig_ages}
  \caption{Age of the universe for each scenario. Scenarios~A and~B
    predict $t_0 = 13.47$~Gyr, 327~Myr younger than Planck~\LCDM.
    All values are consistent with independent stellar age constraints
    ($t \gtrsim 12.5$~Gyr from globular clusters).}
  \label{fig:ages}
\end{figure}
""",
}


def build_paper2():
    """Build Paper 2 LaTeX."""
    paper_dir = BASE / "paper2"
    appendix_dir = paper_dir / "appendices"
    out_dir = paper_dir / "etc" / "arxiv"
    out_dir.mkdir(parents=True, exist_ok=True)

    parts = []
    parts.append(PAPER2_PREAMBLE)
    parts.append("\\begin{document}\n")

    parts.append("\\title{The 5D e-Dimension Framework II: Precision Cosmology from Geometry}")
    parts.append("\\author{G.~Six}")
    parts.append("\\affiliation{Independent researcher}")
    parts.append("\\date{\\today}\n")

    # Abstract — skip both # and ## headers in abstract.md
    abstract_text = process_markdown_file(paper_dir / "abstract.md", skip_top_header=True)
    # Also strip any remaining \subsection from inside the abstract
    abstract_text = re.sub(r'\\subsection\{[^}]*\}\s*', '', abstract_text)
    # Remove any \section that crept in
    abstract_text = re.sub(r'\\section\{[^}]*\}\s*', '', abstract_text)
    parts.append("\\begin{abstract}")
    parts.append(abstract_text)
    parts.append("\\end{abstract}\n")
    parts.append("\\maketitle\n")

    # Section 1: Introduction
    parts.append("\\section{Introduction}")
    parts.append(process_markdown_file(paper_dir / "paper2-section-1-introduction.md"))

    # Sections 2-7: combined file — use header_offset=-1 to promote ## to \section
    parts.append(process_markdown_file(
        paper_dir / "paper2-sections-2-to-7.md",
        header_offset=-1
    ))

    # Insert figures at appropriate locations (after main body sections)
    parts.append(PAPER2_FIGURE_LATEX["section4"])
    parts.append(PAPER2_FIGURE_LATEX["s8"])
    parts.append(PAPER2_FIGURE_LATEX["Hz"])
    parts.append(PAPER2_FIGURE_LATEX["wz"])
    parts.append(PAPER2_FIGURE_LATEX["ages"])

    # Section 8: Conclusion
    parts.append("\\section{Conclusion}")
    parts.append(process_markdown_file(paper_dir / "paper2-section-8-conclusion.md"))

    # Appendices
    parts.append("\n\\appendix\n")
    for fname, title in PAPER2_APPENDICES:
        parts.append(f"\n\\section{{{title}}}")
        parts.append(process_markdown_file(appendix_dir / fname))

    # Bibliography after appendices
    parts.append("\n\\bibliography{refs}")
    parts.append("\n\\end{document}")

    tex_content = "\n".join(parts)

    # Final comprehensive Unicode pass
    tex_content = final_unicode_pass(tex_content)

    (out_dir / "paper2.tex").write_text(tex_content, encoding="utf-8")

    # Copy refs.bib and append missing entries
    shutil.copy2(paper_dir / "etc" / "refs.bib", out_dir / "refs.bib")
    append_missing_bib_entries(out_dir / "refs.bib", EXTRA_BIB_PAPER2)

    # Copy and rename figures
    fig_src = BASE / "etc" / "age"
    for src_name, dst_name in PAPER2_FIGURES.items():
        src = fig_src / src_name
        if src.exists():
            shutil.copy2(src, out_dir / dst_name)
            print(f"Paper 2: copied figure {dst_name}")
        else:
            print(f"Paper 2: WARNING --- figure not found: {src}")

    # Preserve existing short abstract if present (may be hand-edited)
    short_abs_path = out_dir / "abstract-short.txt"
    if short_abs_path.exists():
        print(f"Paper 2: preserving existing {short_abs_path.name}")
    else:
        short_abstract = (
            "We compute the complete cosmological predictions of the 5D e-dimension "
            "framework using the CAMB Boltzmann solver with parameters derived "
            "entirely from the e-circle geometry --- fitting zero parameters to CMB "
            "data. Two observational inputs (the dark energy density and the "
            "dark-to-visible matter ratio) together with the Standard Model field "
            "content determine every observable. The results: $t_0 = 13.47$ Gyr; "
            "$S_8 = 0.753$--$0.785$ (resolving the $4\\sigma$ clustering tension); "
            "$H_0 = 68.7$--$69.5$ km/s/Mpc; $r_d = 145.8$--$146.2$ Mpc. The scaling "
            "law $\\Omega_{\\rm DM}/\\Omega_b = 1/\\xi^2$, derived from bulk "
            "leptogenesis on the $Z_2$ orbifold, explains the cosmic coincidence. "
            "The expansion history $H(z)$ peaks 4--6\\% above $\\Lambda$CDM at "
            "$z \\sim 0.3$--$0.7$, testable by DESI DR3. CMB-S4 will confirm or "
            "exclude the mirror sector at $> 9\\sigma$ ($N_{\\rm eff} = 3.31$--$3.39$)."
        )
        short_abs_path.write_text(short_abstract, encoding="utf-8")

    line_count = tex_content.count("\n") + 1
    print(f"Paper 2: wrote {out_dir / 'paper2.tex'} ({line_count} lines)")
    print(f"Paper 2: copied {out_dir / 'refs.bib'}")
    print(f"Paper 2: wrote {out_dir / 'abstract-short.txt'}")


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "both"

    if target in ("paper1", "both", "1"):
        print("=" * 60)
        print("Building Paper 1...")
        print("=" * 60)
        build_paper1()

    if target in ("paper2", "both", "2"):
        print("=" * 60)
        print("Building Paper 2...")
        print("=" * 60)
        build_paper2()

    print("\nDone. Review the output before submitting to arXiv.")
    print("Run pdflatex + bibtex to verify compilation.")


if __name__ == "__main__":
    main()
