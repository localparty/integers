# A1 Weitzenböck Notation Patch — Applied to Small Files

Source patch: `tier-2-fixes/A1-weitzenboeck-notation-patch.md`
Scope: Five preprint files (`00-abstract.md`, `02-geometric-framework.md`,
`A-laplacian-spectrum.md`, `E-weitzenboeck.md`, `08-conclusion.md`).
Applied: 2026-04-08.

All replacements push $N=3$-specific numeric values
($6/r_3^2$, $12/r_3^2$, $2\sqrt{3}/r_3$, $2\sqrt{3}\,a/r_3$) into the
general-$N$ Weitzenböck / Ikeda–Taniguchi forms
($2N/r_3^2$, $4N/r_3^2$, $2\sqrt{N}/r_3$, $2\sqrt{N}\,a/r_3$), while
keeping the $N=3$ substitution as an explicit parenthetical so the
physical SU(3) numerics remain visible.

---

## 1. `00-abstract.md`

**Edit 1** (abstract bullet list, lines 27–37 of current file).
Replaced the single bullet "*Trivial sector* ($c_2 = 0$): ..." block:

- "$\mu_1 \geq 6/r_3^2$" → "$\mu_1 \geq 2N/r_3^2$ (equals $6/r_3^2$
  for $N=3$)".
- "$m_1 = 2\sqrt{3}/r_3$" → "$m_1 = 2\sqrt{N}/r_3$".
- "$Ce^{-2\sqrt{3}\,a/r_3}$" → "$Ce^{-2\sqrt{N}\,a/r_3}$".
- "$\beta < a/(2\sqrt{3}\,r_3)$" → "$\beta < a/(2\sqrt{N}\,r_3)$".
- "$\beta$ up to $\sim 10^{14}$" → "$\beta$ up to $\sim
  (1/(2\sqrt{N}))\cdot 10^{15}$ (i.e., $\sim 2.9\times 10^{14}$ for
  $N=3$)".

One Edit tool call.

---

## 2. `02-geometric-framework.md`

**Edit 1** (§2.3, around line 66).
"$\text{Ric}_{a\bar b} = \frac{6}{r_3^2} g_{a\bar b}$" →
"$\text{Ric}_{a\bar b} = \frac{2N}{r_3^2} g_{a\bar b}$ ... which
equals $6/r_3^2$ for the physical case $N = 3$ (i.e., $\mathbb{CP}^2$)".

One Edit tool call.

---

## 3. `A-laplacian-spectrum.md`

**Edit 1** (§A.1 eigenvalue formula).
Added a "Remark ($N$-dependence)" paragraph after the $\lambda_{p,q}$
formula explaining that this is the $\mathbb{CP}^2$ ($N=3$) case,
that the general $\mathbb{CP}^{N-1}$ first non-trivial eigenvalue is
$4N/r_3^2$ (Ikeda–Taniguchi 1978), and that the Weitzenböck lower
bound is $\mu_1 \geq 2N/r_3^2$; cross-references Theorem 1 of §02.

**Edit 2** (§A.2 "First non-trivial eigenvalue" display).
Header changed to "First non-trivial eigenvalue ($N=3$ specific;
general form $\lambda_1 = 4N/r_3^2$)". Lichnerowicz derivation line
now notes "(general $N$: $\text{Ric} = (2N/r_3^2) g$)".

Two Edit tool calls.

---

## 4. `E-weitzenboeck.md`

**Edit 1** (top-of-appendix convention note).
Inserted a "**Convention note ($N$-dependence)**" paragraph directly
after the introductory paragraph explaining that the entire appendix
specializes to $N = 3$, and stating the general-$N$ formulas
$\text{Ric} = (2N/r_3^2) g$, $\mu_1 \geq 2N/r_3^2$,
$\mu_{\min}^{(1)} = 4N/r_3^2$, $m_1 = 2\sqrt{N}/r_3$, with
cross-reference to Theorem 1 of §02.

**Edit 2** (§G.2 Weitzenböck formula block).
Five separate display equations in the block rewritten from
$6/r_3^2$ to $2N/r_3^2$ with explicit parenthetical "$= 6/r_3^2$ for
$N=3$". Final bold statement now reads "every eigenvalue of the
Hodge Laplacian on one-forms is at least $2N/r_3^2$ (which is
$6/r_3^2$ for $N = 3$)".

**Edit 3** (§G.3 "Consequences for the Gauge Field Spectrum").
"$\mu_n \geq 6/r_3^2$" display → "$\mu_n \geq 2N/r_3^2\ (= 6/r_3^2\
\text{for}\ N = 3)$". Prose "$\mu_1 \geq 6/r_3^2$" → "$\mu_1 \geq
2N/r_3^2$ (i.e., $6/r_3^2$ for $N = 3$)". Mass scale "$\sqrt 6/r_3$"
→ "$\sqrt{2N}/r_3$". $H^1(\mathbb{CP}^2)$ → $H^1(\mathbb{CP}^{N-1})$.

**Edit 4** (§G.5 full spectrum and lightest KK vector display).
"$\mu_{\min}^{(1)} = 12/r_3^2$" display → "$\mu_{\min}^{(1)} =
4N/r_3^2\ (= 12/r_3^2\ \text{for}\ N=3)$", with prose added that the
$N=3$ assignment to $(\mathbf 3,\mathbf 1)\oplus(\mathbf 1,\bar{\mathbf
3})$ is specifically the $N=3$ case. "$m_{\text{KK vector}} =
\sqrt{12}/r_3 = 2\sqrt{3}/r_3$" display → "$m_{\text{KK vector}} =
\sqrt{4N}/r_3 = 2\sqrt{N}/r_3\ (= \sqrt{12}/r_3 = 2\sqrt{3}/r_3
\approx 3.46\, M_{\text{KK}}\ \text{for}\ N = 3)$".

**Edit 5** (§G.6 "Massless vectors" bullet).
"$H^1(\mathbb{CP}^2) = 0$" → "$H^1(\mathbb{CP}^{N-1}) = 0$" and
"$\mu \geq 6/r_3^2$" → "$\mu \geq 2N/r_3^2$ ($= 6/r_3^2$ for $N = 3$)".

Five Edit tool calls.

---

## 5. `08-conclusion.md`

**Edit 1** (§12.1 proof chain steps 1–3, lines 8–21 of original).
Step 1: "$\mu_1 \geq 6/r_3^2$" → "$\mu_1 \geq 2N/r_3^2$ (equals
$6/r_3^2$ for $N = 3$)". Step 2: "$m_1 = 2\sqrt{3}/r_3$" →
"$m_1 = 2\sqrt{N}/r_3$ (equals $2\sqrt{3}/r_3$ for $N = 3$)". Step 3:
"$\beta < a/(2\sqrt{3}\,r_3)$" → "$\beta < a/(2\sqrt{N}\,r_3)$";
"$\sim 10^{14}$" → "$\sim (1/(2\sqrt{N}))\cdot 10^{15}$ (i.e.,
$\sim 2.9 \times 10^{14}$ for $N = 3$)".

**Edit 2** (§12.3 "The Contribution", line 95 of original).
"$e^{-2\sqrt{3}\,a/r_3}$" → "$e^{-2\sqrt{N}\,a/r_3}$ (which is
$e^{-2\sqrt{3}\,a/r_3}$ for $N = 3$)".

**Edit 3** (§12.6 "The Honest Bottom Line", line 154 of original).
"$\mu_1 \geq 6/r_3^2$" → "$\mu_1 \geq 2N/r_3^2$ (equal to $6/r_3^2$
for $N = 3$)".

Three Edit tool calls.

---

## Summary table

| File | Tool calls | Patch items covered |
|------|-----------|---------------------|
| `00-abstract.md` | 1 | L29, L31–32, L34–37 |
| `02-geometric-framework.md` | 1 | L66 Ricci tensor |
| `A-laplacian-spectrum.md` | 2 | §A.1 eigenvalue formula, §A.2 $\lambda_1$ |
| `E-weitzenboeck.md` | 5 | L28, L31, L35, L39, L42, L56, L109, L115, L131, L134 |
| `08-conclusion.md` | 3 | L9, L14, L20, L95, L154 |
| **Total** | **12** | |

## Verification

Post-edit grep on each file confirms that every remaining occurrence
of $6/r_3^2$, $12/r_3^2$, $2\sqrt{3}/r_3$, or $2\sqrt{3}\,a/r_3$ is
inside an explicit "equals / for $N = 3$" parenthetical or inside a
dimension-specific Lichnerowicz substitution that uses $n = 4$
(i.e., the Obata derivation for $\mathbb{CP}^2$, which is
intrinsically a real-4-dimensional identity and remains labelled as
the $N = 3$ case).

No universal "$\mu_1 = 6/r_3^2$" or "$m_1 = 2\sqrt{3}/r_3$" claim
remains in any of the five files; every instance either now reads
"$2N/r_3^2$" / "$2\sqrt{N}/r_3$" or carries an explicit "for $N = 3$"
label. Patch A1 is fully applied to this file set.
