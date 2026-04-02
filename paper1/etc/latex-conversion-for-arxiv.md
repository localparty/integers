# LaTeX Conversion Instructions — Quantum Geometry in 5D

> **For the agent doing the LaTeX conversion.**
> Read this file completely before writing a single line of LaTeX.
> G will review all output before submitting to arXiv.

---

## What This Project Is

A theoretical physics paper claiming perturbative finiteness of 5D
Kaluza-Klein quantum gravity. The central result: the Goroff-Sagnotti R³
divergence that proved 4D gravity non-renormalizable in 1986 vanishes
identically in the 5D theory via the Epstein-Terras theorem.

This goes to arXiv:hep-th with cross-listing to quant-ph and gr-qc.
Target journal after arXiv: Physical Review Letters.

---

## Source Files

All source files are Markdown at:

```
/Users/gsix/quantum-geometry-in-5d/paper1/
├── abstract.md
├── paper-section-1-introduction.md
├── paper-section-2-framework.md
├── paper-section-3-five-phenomena.md
├── paper-section-4-1-aharonov-bohm.md
├── paper-section-4-2-spin-statistics.md
├── paper-section-5-gravity-bridge.md
├── paper-section-5x-quantization-bridge.md
├── paper-section-6-connections.md
├── paper-section-7-philosophy.md
├── paper-section-8-conclusion.md
└── appendices/
    ├── appendix-A-quantum-dictionary.md
    ├── appendix-B-spin-statistics-derivation.md
    ├── appendix-C-quantitative-demonstrations.md
    ├── appendix-D-5d-einstein-equations.md
    ├── appendix-E-quantum-consistency.md
    ├── appendix-F-one-loop-computation.md
    ├── appendix-G-two-loop-computation.md
    ├── appendix-H-testable-predictions.md
    ├── appendix-I-cassini-fifth-force.md
    ├── appendix-J-non-perturbative-stability.md
    ├── appendix-K-higher-loop-epstein.md
    ├── appendix-L-non-abelian-extension.md
    ├── appendix-M-hydrogen-atom.md
    ├── appendix-N-gravitational-waves.md
    ├── appendix-O-black-hole-entropy.md
    ├── appendix-P-cpt-theorem.md
    ├── appendix-Q-frw-cosmology.md
    ├── appendix-R-running-couplings.md
    ├── appendix-S-finiteness-theorem.md
    ├── appendix-T-rigorous-verification.md
    ├── appendix-U-goroff-sagnotti-verification.md
    ├── appendix-V-vertex-computation.md
    ├── appendix-W-orbifold-dark-sector.md
    ├── appendix-X-strong-cp.md
    ├── appendix-Y-hubble-tension.md
    └── appendix-Z-neutrino-mass-ordering.md
```

---

## Output Target

Produce a single self-contained LaTeX file:

```
/Users/gsix/quantum-geometry-in-5d/paper1/etc/arxiv/main.tex
```

Plus a bibliography file:

```
/Users/gsix/quantum-geometry-in-5d/paper1/etc/arxiv/refs.bib
```

Create the directory if it doesn't exist.

---

## Document Class and Preamble

Use the `revtex4-2` document class — this is the standard for Physical
Review Letters and is accepted by arXiv:

```latex
\documentclass[aps,prl,twocolumn,showpacs,superscriptaddress]{revtex4-2}
```

For the full paper (which is too long for PRL as a single submission),
use `\documentclass[aps,prd,preprint,superscriptaddress]{revtex4-2}`.

**For now, produce the preprint version** (single column, double spaced)
which is appropriate for arXiv. It can be reformatted for PRL submission
separately.

```latex
\documentclass[aps,prd,preprint,superscriptaddress,longbibliography]{revtex4-2}
```

### Required packages

```latex
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{amsthm}
\usepackage{mathtools}
\usepackage{physics}      % for \ket{}, \bra{}, etc.
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{booktabs}     % for \toprule etc. in tables
\usepackage{array}
\usepackage{graphicx}
\usepackage{dcolumn}
\usepackage{bm}           % bold math
```

### Theorem environments

```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

### Custom macros (use throughout for consistency)

```latex
% The e-dimension
\newcommand{\edim}{e}
\newcommand{\ecircle}{S^1}

% Common objects
\newcommand{\Mfour}{M^4}
\newcommand{\ebundle}{P(M^4, \mathrm{U}(1))}
\newcommand{\KKmetric}{\hat{G}_{AB}}

% The central zeta result
\newcommand{\Snought}{S_0^{(L)}}

% Epstein zeta
\newcommand{\Epstein}[2]{E_{#1}(s;\, #2)}

% Units and constants
\newcommand{\lP}{l_{\mathrm{P}}}
\newcommand{\GN}{G_{\mathrm{N}}}
\newcommand{\GFive}{\hat{G}_5}
```

---

## Math Conversion Rules

The Markdown source uses Unicode math symbols inline and indented
code-block style for displayed equations. Convert as follows:

### Inline Unicode → LaTeX

| Markdown | LaTeX |
|---------|-------|
| `ψ` | `\psi` |
| `φ` | `\varphi` (e-coordinate) or `\phi` (scalar field) |
| `α` | `\alpha` |
| `β` | `\beta` |
| `γ` | `\gamma` |
| `ε` | `\varepsilon` |
| `δ` | `\delta` |
| `μ`, `ν` | `\mu`, `\nu` |
| `ρ`, `σ` | `\rho`, `\sigma` |
| `τ` | `\tau` |
| `θ` | `\theta` |
| `λ` | `\lambda` |
| `Λ` | `\Lambda` |
| `π` | `\pi` |
| `Σ` | `\Sigma` (summation) |
| `∫` | `\int` |
| `∇` | `\nabla` |
| `∂` | `\partial` |
| `∞` | `\infty` |
| `→` | `\to` or `\rightarrow` |
| `←` | `\leftarrow` |
| `↔` | `\leftrightarrow` |
| `⟨`, `⟩` | `\langle`, `\rangle` |
| `√` | `\sqrt{}` |
| `×` | `\times` |
| `·` | `\cdot` |
| `≈` | `\approx` |
| `≠` | `\neq` |
| `≤`, `≥` | `\leq`, `\geq` |
| `∈` | `\in` |
| `ℤ` | `\mathbb{Z}` |
| `ℝ` | `\mathbb{R}` |
| `ℂ` | `\mathbb{C}` |
| `ℏ` | `\hbar` |
| `†` | `\dagger` |
| `⊗` | `\otimes` |
| `↑`, `↓` | `\uparrow`, `\downarrow` |

### Displayed equations

Indented code blocks containing equations become `\begin{equation}...\end{equation}`
or `\begin{align}...\end{align}` for multi-line systems.

Example Markdown:
```
    ∇²Φ = 4πGρ
```
Becomes:
```latex
\begin{equation}
    \nabla^2 \Phi = 4\pi G \rho
\end{equation}
```

Example multi-line:
```
    E(â, b̂) = −cos θ = −â · b̂
```
Becomes:
```latex
\begin{equation}
    E(\hat{a}, \hat{b}) = -\cos\theta = -\hat{a} \cdot \hat{b}
\end{equation}
```

### Subscripts and superscripts

Markdown uses Unicode sub/superscripts: `e₁`, `m_n`, `G₄`, `Ĝ₅`, `R̂`.
Convert:
- `₁`, `₂`, `ₙ` → `_1`, `_2`, `_n`
- `⁴`, `⁵` → `^4`, `^5`
- `ĝ` (hat) → `\hat{g}`
- `Ĝ`, `R̂` → `\hat{G}`, `\hat{R}`
- `ĥ` → `\hat{h}`
- `Â`, `B̂` → `\hat{A}`, `\hat{B}`

### The central equation (appears in abstract and multiple sections)

```
S₀^{(L)} = [1 + 2ζ(0)]^L = 0
```
Becomes:
```latex
S_0^{(L)} = \bigl[1 + 2\zeta(0)\bigr]^L = 0
```

### Epstein zeta function (appears in Appendices F, G, K, S, T, U, V)

```
E_L(s; Q_L)
```
Becomes:
```latex
E_L(s;\, Q_L)
```

---

## Document Structure

The LaTeX document should follow this structure exactly:

```
\begin{document}
\title{...}
\author{...}
\affiliation{...}
\date{\today}
\begin{abstract}
  [contents of abstract.md]
\end{abstract}
\maketitle
\tableofcontents   % for preprint; remove for PRL submission

% Section 1
\section{Introduction}
[paper-section-1-introduction.md]

% Section 2
\section{The Five-Dimensional Framework}
[paper-section-2-framework.md]

% Section 3
\section{Five Quantum Phenomena Reinterpreted}
[paper-section-3-five-phenomena.md]

% Section 4
\section{Two Derivations}
\subsection{The Aharonov-Bohm Effect}
[paper-section-4-1-aharonov-bohm.md]
\subsection{The Spin-Statistics Theorem}
[paper-section-4-2-spin-statistics.md]

% Section 5
\section{Toward Quantum Gravity: The E-Space Bridge}
[paper-section-5-gravity-bridge.md]

% Section 6: The Quantization Bridge
% (source file is named "5x" but it becomes Section 6 in LaTeX;
%  all subsequent sections shift by one: 6→7, 7→8, 8→9)
\section{The Quantization Bridge}
[paper-section-5x-quantization-bridge.md]

% Section 7
\section{Connections to Modern Physics}
[paper-section-6-connections.md]

% Section 8
\section{Philosophical Resolution}
[paper-section-7-philosophy.md]

% Section 9
\section{Conclusion}
[paper-section-8-conclusion.md]

\bibliography{refs}

% Appendices
\appendix

\section{Quantum Dictionary}
[appendix-A]

\section{Spin-Statistics Derivation}
[appendix-B]

... etc through appendix-Z (include all: W, X, Y, Z) ...

\end{document}
```

---

## Section Header Conversion

Markdown headers map to LaTeX commands as follows:

| Markdown | LaTeX |
|---------|-------|
| `# Section N — Title` | `\section{Title}` |
| `## N.M Title` | `\subsection{Title}` |
| `### N.M.P Title` | `\subsubsection{Title}` |

The Markdown files use formats like `## 2.1 Five Coordinates` —
convert to `\subsection{Five Coordinates}` (LaTeX handles the numbering).

For appendices, the letter prefix (B.1, B.2, etc.) is also handled
automatically by LaTeX once `\appendix` is declared.

---

## Tables

Markdown tables (using `|---|---` syntax) become `\begin{table}` environments.

Example:
```markdown
| Loop order | 4D gravity | 5D KK gravity |
|---|---|---|
| 1-loop | Finite | Finite |
| 2-loop | **Divergent** | **Finite** |
```
Becomes:
```latex
\begin{table}[h]
\centering
\begin{tabular}{lll}
\toprule
Loop order & 4D gravity & 5D KK gravity \\
\midrule
1-loop & Finite & Finite \\
2-loop & \textbf{Divergent} & \textbf{Finite} \\
\bottomrule
\end{tabular}
\caption{UV behavior comparison.}
\label{tab:loop-comparison}
\end{table}
```

---

## Theorem Environments

The Markdown source contains named theorems, stated in bold or with
explicit "Theorem X.Y" labeling. Convert these to proper theorem
environments:

```markdown
**Theorem S.1 (Perturbative Finiteness).** The L-loop effective action...
```
Becomes:
```latex
\begin{theorem}[Perturbative Finiteness]
\label{thm:S1}
The $L$-loop effective action...
\end{theorem}
```

Similarly for **Proof**, **Definition**, **Lemma**:
```latex
\begin{proof}
...
\end{proof}
```

---

## Citations

The Markdown source contains inline citations in formats like:
- `(Goroff & Sagnotti 1986)`
- `(Epstein 1903, Terras 1985)`
- `Bertotti, Iess, & Tortora 2003`
- `Hensen et al. (2015)`

Convert all of these to `\cite{key}` format and collect all references
into `refs.bib`.

### Bibliography keys to use

Use the format `AuthorYYYY` or `AuthorAuthorYYYY`:

| Paper | Key |
|-------|-----|
| Goroff & Sagnotti, Nucl. Phys. B 266 (1986) | `GoroffSagnotti1986` |
| 't Hooft & Veltman, Ann. IHP 20 (1974) | `tHooftVeltman1974` |
| van de Ven, Nucl. Phys. B 378 (1992) | `vandeVen1992` |
| Epstein, Math. Ann. 56 (1903) | `Epstein1903` |
| Terras, Harmonic Analysis (1985) | `Terras1985` |
| Seeley, Proc. Symp. (1967) | `Seeley1967` |
| Minakshisundaram & Pleijel (1949) | `MinakshisundaramPleijel1949` |
| Vassilevich, Phys. Reports (2003) | `Vassilevich2003` |
| Kaluza (1921) | `Kaluza1921` |
| Klein (1926) | `Klein1926` |
| Cho (1975) | `Cho1975` |
| Bailin & Love (1987) | `BailinLove1987` |
| Bertotti, Iess & Tortora, Nature (2003) | `BertottiIessTortora2003` |
| Appelquist & Chodos (1983) | `AppelquistChodos1983` |
| Witten (1981) | `Witten1981` |
| Witten (1982) | `Witten1982` |
| Coleman & De Luccia (1980) | `ColemanDeLuccia1980` |
| Bell (1964) | `Bell1964` |
| CHSH (1969) | `CHSH1969` |
| Tsirelson (1980) | `Tsirelson1980` |
| Aspect, Grangier & Roger (1982) | `AspectGrangierRoger1982` |
| Hensen et al. (2015) | `Hensenetal2015` |
| Bekenstein (1973) | `Bekenstein1973` |
| Hawking (1975) | `Hawking1975` |
| Strominger & Vafa (1996) | `StromingerVafa1996` |
| Aharonov & Bohm (1959) | `AharonovBohm1959` |
| Berry & Robbins (1997) | `BerryRobbins1997` |
| Leinaas & Myrheim (1977) | `LeinaasMyrhei1977` |
| Bartolomei et al. (2020) | `Bartolomeietal2020` |
| Nakamura et al. (2020) | `Nakamuraetal2020` |
| Lee et al. (2020) | `Leeetal2020` |
| Overduin & Wesson (1997) | `OverduinWesson1997` |
| Ryu & Takayanagi (2006) | `RyuTakayanagi2006` |
| Woodhouse (1992) | `Woodhouse1992` |
| Maldacena & Susskind (2013) | `MaldacenaSusskind2013` |
| Hawking, Perry & Strominger (2016) | `HawkingPerryStrominger2016` |
| DeWitt (1967) | `DeWitt1967` |
| Sannan (1986) | `Sannan1986` |
| BOGOLIUBOV et al. BPH forest | `Bogoliubov1957`, `Hepp1966`, `Zimmermann1969` |

Populate `refs.bib` with complete BibTeX entries for all of these.
Use standard BibTeX formats: `@article`, `@book`, `@incollection`.

---

## Author and Affiliation

Use:
```latex
\author{G. Six}
\affiliation{Independent researcher}
```

---

## Important Formatting Notes

**Bold text** in Markdown (`**text**`) → `\textbf{text}` in LaTeX.
Only use this where the original uses it for emphasis of key terms or
theorem statements — do not bold ordinary prose.

*Italic text* (`*text*`) → `\textit{text}`. Use sparingly.

**Horizontal rules** (`---`) in Markdown separate subsections. In LaTeX,
these are handled by `\subsection` headers — do not add `\hrule` or
decorative lines.

**Code blocks** used for equations (indented 4 spaces) → displayed
math environments as described above.

**Inline code** used for variable names (`` `e₁ + e₂ = C` ``) →
inline math `$e_1 + e_2 = C$`.

---

## Quality Checks Before Finishing

Run these checks before handing the output to the human:

1. **Compile test:** Run `pdflatex main.tex` twice and `bibtex refs`
   to check for errors. Fix all errors. Warnings are acceptable.

2. **Equation numbering:** Every displayed equation that is referenced
   in the text should have a `\label{}` and be referenced with `\eqref{}`.

3. **Cross-references:** Every `(Appendix B)`, `(Section 5.X)`,
   `(Theorem S.1)` etc. should be a `\ref{}` to a proper `\label{}`.

4. **Bibliography:** Every `\cite{}` key should have a matching entry
   in `refs.bib`. Run `bibtex` and check for missing entries.

5. **No orphaned Unicode:** Search the `.tex` file for any Unicode math
   characters (ψ, φ, α, ∇, ∂, ℏ, etc.) that were missed in conversion.
   All math must be in LaTeX math mode.

6. **Abstract word count:** The file `paper/abstract.md` contains the
   FULL abstract (~800 words) which is too long for arXiv. Produce TWO versions:

   (a) Full abstract in the paper PDF (\begin{abstract}...\end{abstract}).

   (b) Short abstract (~250 words, under 1,920 characters) for the arXiv
       submission form. Condense: keep paragraphs 1-3 intact; paragraph 4
       keep only the Goroff-Sagnotti sentence and two-parameter finiteness
       claim; paragraph 5 reduce to two sentences (dark matter, dark photon,
       alpha); paragraph 6 keep only the 19-phenomena and 7-predictions
       sentences plus the honest disclaimer. Save as `etc/arxiv/abstract-short.txt`.

   Check the short version with `wc -m abstract-short.txt` (target: under 1,920).

---

## File Structure to Produce

```
/Users/gsix/quantum-geometry-in-5d/paper1/etc/arxiv/
├── main.tex        ← the complete paper
└── refs.bib        ← all bibliography entries
```

No figures are included in this submission — the paper contains only
tables and equations. The JSX files in `paper1/figures/` are conceptual
sketches for reference only; they are not part of the arXiv submission.

---

## What NOT to Do

- Do not split the paper into multiple `.tex` files — one `main.tex` only
- Do not change any mathematical content — convert notation faithfully
- Do not add or remove sections
- Do not rewrite any prose — convert only
- Do not use `\input{}` or `\include{}` — everything inline in `main.tex`
- Do not use deprecated packages (`times`, `epsfig`, etc.)
- Do not use `eqnarray` — use `align` instead
- Do not use `$$...$$` — use `\begin{equation}` or `\[...\]`

---

## When You're Done

1. Confirm the file compiles cleanly with `pdflatex` + `bibtex`
2. Report the total line count of `main.tex`
3. Report any equations or citations you were uncertain about
4. Do NOT commit anything — leave the files for the human to review

The human will check the output, make any corrections, then commit
and submit to arXiv.

---

## Cross-references to Paper 2

Paper 1's abstract and Section 6 (Connections) reference Paper 2's
cosmological results. In the LaTeX:

- "Paper~II" for the companion cosmology paper
- If submitting both simultaneously, arXiv allows cross-referencing
  between papers in the same submission batch. Use a placeholder
  `eprint = {YYMM.NNNNN}` in refs.bib and update after the first
  paper's ID is assigned.
- If Paper 2 is already on arXiv, cite by arXiv ID.

Key Paper 2 results referenced from Paper 1:
- $t_0 = 13.47$~Gyr, $S_8 = 0.753$--$0.785$
- $H_0 = 68.7$--$69.5$~km/s/Mpc
- $\Omega_{\rm DM}/\Omega_b = 1/\xi^2$ (cosmic coincidence)
- $N_{\rm eff} = 3.31$--$3.39$

---

## arXiv Submission

### What to upload

Pack into a single `.tar.gz`:

```
main.tex            — the complete paper
refs.bib            — bibliography (from paper1/etc/refs.bib)
```

No subdirectories. No .aux, .log, or .out files.

You have two options for the bibliography:
(a) Include `refs.bib` and let arXiv run BibTeX.
(b) Pre-build the `.bbl` locally and include it instead of `.bib`.

### Categories

- **Primary:** hep-th (High Energy Physics - Theory)
- **Cross-list:** quant-ph, gr-qc

### First-time gotchas

- **BibTeX:** arXiv runs `pdflatex → bibtex → pdflatex → pdflatex`.
  If you use `\bibliography{refs}`, the file must be `refs.bib`.
- **revtex4-2:** Already on arXiv's TeX Live. No need to upload.
- **`\bibliographystyle`:** revtex4-2 sets this automatically. Do NOT
  add a `\bibliographystyle{}` command.
- **Compilation timeout:** arXiv has a ~5 minute compile limit. With
  26 appendices this paper is large — should still be fine, but if
  it times out, switch to the pre-built `.bbl` approach.
- **Abstract field:** arXiv has a separate plain-text abstract field
  on the submission form. Use `$...$` for inline math (arXiv renders
  it). The full abstract (~800 words) may exceed the character limit
  (~1920 chars) — use the short version from `abstract-short.txt`.
- **Moderation hold:** First-time authors sometimes get held for
  manual review (~1-2 days). Normal — just wait.
- **Paper 2 cross-reference:** If submitting both simultaneously,
  arXiv lets you cross-reference between papers in the same batch.
