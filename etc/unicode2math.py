#!/usr/bin/env python3
"""
Phase 0: Fence inline math expressions with backticks in markdown.

Conservative mode: only fences expressions it's confident about.
Flags ambiguous multi-token expressions for manual review.

Usage:
    python3 etc/unicode2math.py                              # dry-run, show diff
    python3 etc/unicode2math.py --write                      # write changes
    python3 etc/unicode2math.py --file paper1/abstract.md    # single file
    python3 etc/unicode2math.py --flag                       # show flagged lines
"""

import re
import sys
import difflib
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).resolve().parent.parent

# ─────────────────────────────────────────────────────────────
# Math-triggering characters
# ─────────────────────────────────────────────────────────────

GREEK = set("αβγδεζηθικλμνξπρστφχψωΓΔΘΛΠΣΦΨΩ")
MATH_OPS = set("∂∇∫∮∞ℏ†√×·≈≠≤≥≡∈∝±∓⊗⊕⟨⟩≪≫≳≲∼≅⊃□∎✓✗")
SUBSCRIPTS = set("₀₁₂₃₄₅₆₇₈₉ₐₑₒₓₖₗₘₙₚₛₜ₋₊ᵢⱼᵣᵤᵥᵧ")
SUPERSCRIPTS = set("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺⁽⁾ⁿᵀᵅᵝᵘᵛ")
DIACRITICAL = set("ĜĝĥŜŝÂâêẋẊḢḣȧḃṘṙĠġḡĀā")
COMBINING = set("\u0302\u0304\u0307\u0303\u0308\u030C")

MATH_TRIGGER = GREEK | MATH_OPS | SUBSCRIPTS | SUPERSCRIPTS | DIACRITICAL | COMBINING


def has_math(s):
    return any(c in MATH_TRIGGER for c in s)


# ─────────────────────────────────────────────────────────────
# Token-level fencing (conservative)
#
# Strategy: split line into whitespace-separated tokens,
# identify contiguous runs of tokens that form a math expression,
# fence each run with backticks.
# ─────────────────────────────────────────────────────────────

# Tokens that bridge between math tokens (operators, connectors)
BRIDGE_TOKENS = {
    "=", "+", "-", "/", "×", "·", "±", "≈", "≠", "≤", "≥",
    "≡", "∈", "→", "←", "↔", "∼", "~",
}


def classify_token(tok):
    """Classify a token as 'math', 'bridge', or 'text'.

    'math': contains math Unicode or is a known math pattern
    'bridge': operator that connects math tokens (=, +, -, etc.)
    'text': regular prose word
    """
    # Strip leading/trailing punctuation for classification
    core = tok.strip("(),;:.!?\"'[]{}*")

    if not core:
        return "text"

    # Known bridge operators
    if core in BRIDGE_TOKENS:
        return "bridge"

    # Contains math-triggering Unicode → math
    if has_math(core):
        return "math"

    # Bare underscore pattern like N_eff, w_a, Ω_DM
    if "_" in core and not core.startswith("_") and len(core) < 20:
        parts = core.split("_")
        if len(parts) == 2 and parts[0].isalnum() and parts[1].isalnum():
            return "math"

    # Bare caret pattern like S^2, (-1)^F
    if "^" in core and len(core) < 20:
        return "math"

    # Single letter that could be a math variable — NOT confident enough
    # (could be "a", "I", etc.)

    return "text"


def fence_line(line):
    """Fence math expressions in a line using backticks.

    Returns (fenced_line, flagged_expressions) where flagged_expressions
    is a list of expressions that need manual review.
    """
    # Don't touch lines with existing backticks
    if "`" in line:
        return line, []

    # Tokenize preserving whitespace structure
    # We need to know the exact positions to reconstruct the line
    tokens = []  # list of (start, end, text, classification)
    for m in re.finditer(r'\S+', line):
        tok = m.group()
        cls = classify_token(tok)
        tokens.append((m.start(), m.end(), tok, cls))

    if not tokens:
        return line, []

    # Group consecutive math/bridge tokens into runs
    runs = []  # list of (start_idx, end_idx) into tokens array
    i = 0
    while i < len(tokens):
        if tokens[i][3] == "math":
            run_start = i
            run_end = i + 1
            # Extend through bridges and more math
            while run_end < len(tokens):
                cls = tokens[run_end][3]
                if cls == "math":
                    run_end += 1
                elif cls == "bridge":
                    # Bridge: only include if followed by math
                    if run_end + 1 < len(tokens) and tokens[run_end + 1][3] == "math":
                        run_end += 2  # include bridge + next math
                    else:
                        break
                else:
                    break
            runs.append((run_start, run_end))
            i = run_end
        else:
            i += 1

    if not runs:
        return line, []

    # Build the fenced line
    flagged = []
    result = []
    prev_end = 0  # character position

    for run_start, run_end in runs:
        char_start = tokens[run_start][0]
        char_end = tokens[run_end - 1][1]
        span_text = line[char_start:char_end]

        # Text before this run
        result.append(line[prev_end:char_start])

        # Strip trailing punctuation that got absorbed
        trail = ""
        while span_text and span_text[-1] in ",.;:":
            trail = span_text[-1] + trail
            span_text = span_text[:-1]
        # Strip trailing ) only if unmatched (more ) than ()
        while span_text and span_text[-1] == ")" and span_text.count(")") > span_text.count("("):
            trail = ")" + trail
            span_text = span_text[:-1]
        # Strip leading ( if unmatched
        if span_text.startswith("(") and span_text.count("(") > span_text.count(")"):
            result.append("(")
            span_text = span_text[1:]

        if not span_text.strip():
            result.append(span_text + trail)
            prev_end = char_end
            continue

        # Decide: fence or flag?
        n_tokens = run_end - run_start
        if n_tokens <= 3:
            result.append(f"`{span_text}`{trail}")
        else:
            flagged.append(span_text)
            result.append(f"`{span_text}`{trail}")

        prev_end = char_end

    result.append(line[prev_end:])
    return "".join(result), flagged


# ─────────────────────────────────────────────────────────────
# File processing
# ─────────────────────────────────────────────────────────────

def process_file(filepath):
    """Process a .md file. Returns (new_text, flagged_items)."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.split("\n")
    output = []
    all_flagged = []

    for i, line in enumerate(lines, 1):
        # Don't touch indented equation blocks
        if line.startswith("    ") and line.strip():
            output.append(line)
            continue

        # Don't touch horizontal rules
        if re.match(r"^---+\s*$", line.strip()):
            output.append(line)
            continue

        # Don't touch empty lines
        if not line.strip():
            output.append(line)
            continue

        # Process blockquotes: fence the content after >
        if line.strip().startswith(">"):
            m = re.match(r"^(\s*>\s?)(.*)", line)
            if m:
                prefix, content = m.group(1), m.group(2)
                fenced, flagged = fence_line(content)
                output.append(prefix + fenced)
                for f in flagged:
                    all_flagged.append((filepath, i, f))
                continue

        # Process headers: fence the title content
        if line.strip().startswith("#"):
            m = re.match(r"^(#{1,4}\s+)(.*)", line)
            if m:
                prefix, content = m.group(1), m.group(2)
                fenced, flagged = fence_line(content)
                output.append(prefix + fenced)
                for f in flagged:
                    all_flagged.append((filepath, i, f))
                continue

        # Regular line
        fenced, flagged = fence_line(line)
        output.append(fenced)
        for f in flagged:
            all_flagged.append((filepath, i, f))

    return "\n".join(output), all_flagged


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

def main():
    write_mode = "--write" in sys.argv
    flag_mode = "--flag" in sys.argv
    single_file = None
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--file" and i + 1 < len(sys.argv):
            single_file = sys.argv[i + 1]

    if single_file:
        p = Path(single_file)
        if not p.is_absolute():
            p = BASE / p
        files = [p]
    else:
        files = sorted(BASE.glob("paper1/**/*.md")) + sorted(BASE.glob("paper2/**/*.md"))
        files = [f for f in files if "/etc/" not in str(f) and "/figures/" not in str(f)]

    total_changes = 0
    all_flagged = []

    for filepath in files:
        original = filepath.read_text(encoding="utf-8")
        converted, flagged = process_file(filepath)
        all_flagged.extend(flagged)

        if original != converted:
            total_changes += 1
            rel = filepath.relative_to(BASE)

            if write_mode:
                filepath.write_text(converted, encoding="utf-8")
                print(f"  WROTE: {rel}")
            elif not flag_mode:
                diff = difflib.unified_diff(
                    original.splitlines(), converted.splitlines(),
                    fromfile=str(rel), tofile=str(rel) + " (fenced)",
                    lineterm=""
                )
                diff_lines = list(diff)
                if diff_lines:
                    print(f"\n{'='*60}")
                    print(f"  {rel}")
                    print(f"{'='*60}")
                    for line in diff_lines[:40]:
                        print(line)
                    if len(diff_lines) > 40:
                        print(f"  ... ({len(diff_lines) - 40} more lines)")

    if flag_mode:
        print(f"\n{'='*60}")
        print(f"  FLAGGED: {len(all_flagged)} expressions need manual review")
        print(f"{'='*60}")
        by_file = defaultdict(list)
        for fp, lineno, expr in all_flagged:
            by_file[fp.relative_to(BASE)].append((lineno, expr))
        for rel, items in sorted(by_file.items()):
            print(f"\n  {rel}:")
            for lineno, expr in items:
                print(f"    L{lineno}: {expr}")
    else:
        print(f"\n{total_changes} files would change. {len(all_flagged)} expressions flagged for review.")
        if not write_mode:
            print("Run with --write to apply.  Run with --flag to see flagged items.")


if __name__ == "__main__":
    main()
