# Gap A1 — Weitzenböck notation patch ($N$-dependence and convention reconciliation)

## 1. Statement of the gap

The preprint writes "$\mu_1 = 6/r_3^2$" and "$m_1 = 2\sqrt 3/r_3$" as if they
were universal features of the Weitzenböck bound on $\mathbb{CP}^{N-1}$, and
then propagates these N=3-specific values through the abstract, Section 4.3
(Theorems 2–3), Section 4.4 (Theorem 4), Section 4.5 (Theorem 5), the
cluster-expansion convergence window $\beta < a/(2\sqrt 3\,r_3)$, the §3
numerical predictions, and the §12 conclusion. For $N\neq 3$ these values are
wrong: the Weitzenböck lower bound is $2N/r_3^2$ and the actual first
eigenvalue (Ikeda–Taniguchi) is $4N/r_3^2$, so $m_1 = 2\sqrt N/r_3$. Worse,
Appendix H's $\mathrm{SU}(2)$ warm-up gives $\lambda_1^{(1)}=2/r_2^2$ on the
round $S^2$, and the preprint never states the convention that relates $r_2$
and $r_3$, so the $N=2$ number in I.3 ($\mu_1\geq 4/r_3^2$) and the $N=2$
number in Appendix H ($\mu_1\geq 1/r_2^2$) appear to contradict one another.
Both Section 02/Appendix E Theorem 1 ($\mu_1\geq 6/r_3^2$) and the
Appendix I.3.2 formula ($m_1 = 2\sqrt N/r_3$) cannot be simultaneously correct
for general $N$.

## 2. The reconciled $N$-dependent statement of Theorem 1

**Theorem 1 ($N$-dependent form).** *Let $\mathbb{CP}^{N-1}$ ($N\geq 2$)
carry the FS metric with holomorphic sectional curvature $4/r_3^2$, so the
Ricci tensor is Einstein, $\mathrm{Ric}=(2N/r_3^2)\,g$. The Weitzenböck
identity $\Delta_H=\nabla^*\nabla+\mathrm{Ric}$ on $\mathfrak g$-valued
1-forms, with $\nabla^*\nabla\geq 0$, gives*
$$\mu_1(\mathbb{CP}^{N-1})\ \geq\ \frac{2N}{r_3^2}.$$
*Since $H^1(\mathbb{CP}^{N-1};\mathbb R)=0$ for all $N\geq 2$, the bound is
strict: every eigenvalue satisfies $\mu_n\geq 2N/r_3^2$.*

**Actual first eigenvalue (Ikeda–Taniguchi 1978).** Same FS normalization:
$$\mu_{\min}^{(1)}=\frac{4N}{r_3^2},\qquad m_1=\frac{2\sqrt N}{r_3}.$$
This is exactly twice the Weitzenböck lower bound (the standard Kähler
"extra factor of 2" from the $(1,0)\oplus(0,1)$ decomposition). For $N=3$
these give $\mu_{\min}^{(1)}=12/r_3^2$ and $m_1=2\sqrt 3/r_3$, reproducing
the often-cited values used in the abstract and §3. For general $N$ these
values are **N=3-specific** and must not be written as universal.

The proof of Theorem 1 uses only the Weitzenböck bound $2N/r_3^2$;
Ikeda–Taniguchi's tighter $4N/r_3^2$ improves the safety factor by 2 but
is not required.

## 3. Convention reconciliation: $r_3$ (FS scale) vs $r_2$ (round scale)

§02 and App. E define $r_3$ by holomorphic sectional curvature $4/r_3^2$
on $\mathbb{CP}^{N-1}$; App. H defines $r_2$ as the round-sphere radius of
$S^2$ with Gaussian curvature $1/r_2^2$. For $N=2$ both describe the same
manifold $\mathbb{CP}^1 = S^2$. Equating Riccis ($2N/r_3^2 = 4/r_3^2$ in
FS, $1/r_2^2$ in round):
$$\boxed{\ r_2 = \tfrac{1}{2}r_3,\qquad r_3 = 2 r_2.\ }$$
Sanity check: Ikeda–Taniguchi gives $\lambda_1^{(1)}=4N/r_3^2=8/r_3^2$ for
$N=2$, which with $r_3=2r_2$ becomes $8/(2r_2)^2 = 2/r_2^2$ — exactly the
value reported in App. H.4 (`04-lattice-proof-part1.md` L1441). The
formulas are consistent; the referee's "$\sqrt 2$" is a convention slip,
not a real inconsistency.

**Proposed fix.** Add a one-paragraph convention note at the start of
Appendix H:

> "Throughout Appendix H we use the round-sphere radius $r_2$ of $S^2$,
> related to the FS radius $r_3$ used elsewhere by $r_3 = 2 r_2$
> (the FS metric with holomorphic sectional curvature $4/r_3^2$ on
> $\mathbb{CP}^1$ is the round metric of radius $r_3/2$). Under this
> translation the Appendix H bound $\mu_1\geq 1/r_2^2$ agrees with the
> general $\mu_1\geq 2N/r_3^2$ of Theorem 1."

This is less invasive than re-deriving Appendix H in $r_3$ variables and
preserves its pedagogical role.

## 4. Inventory of "$2\sqrt 3$" / "$6/r_3^2$" sites to patch

Numbers below are line references in
`/Users/gsix/yang-mills/preprint/sections/<file>`.

**Abstract — `00-abstract.md`.**
- L29: "$\mu_1 \geq 6/r_3^2$" → "$\mu_1\geq 2N/r_3^2$ (equals $6/r_3^2$ for $N=3$)".
- L31–32: "$m_1 = 2\sqrt 3/r_3$ ... $Ce^{-2\sqrt 3 a/r_3}$" →
  "$m_1 = 2\sqrt N/r_3$ ... $Ce^{-2\sqrt N\,a/r_3}$".
- L34–37: "$\beta<a/(2\sqrt 3\,r_3)$ ... $\sim 10^{14}$" →
  "$\beta<a/(2\sqrt N\,r_3)$ ... $\sim (1/(2\sqrt N))\cdot 10^{15}$".
- L78: keep "$\sqrt\sigma = 437$ MeV" but mark it as the $\mathrm{SU}(3)$
  phenomenological prediction of §3 (already group-specific, so no change
  required — but flag that the $0^{++}$ glueball mass formula in §7.1 that
  follows from $m_1$ is $N$-dependent).

**§02 / Appendix E — `02-geometric-framework.md`, `E-weitzenboeck.md`.**
- `02-geometric-framework.md` L66: "$\mathrm{Ric}_{a\bar b}=(6/r_3^2)g_{a\bar b}$"
  → "$\mathrm{Ric}_{a\bar b}=(2N/r_3^2)g_{a\bar b}$, which equals $6/r_3^2$
  for the physical case $N=3$". (Confirmed numerically in I.3.2 item 1.)
- `E-weitzenboeck.md` L28, L31, L35, L39, L42, L56, L109, L131, L134: replace
  every "$6/r_3^2$" by "$2N/r_3^2$" with a parenthetical "$=6/r_3^2$ for
  $N=3$". The whole appendix is written in the $\mathbb{CP}^2$ special case;
  the simplest fix is a header note "Throughout this appendix, $N=3$;
  see Theorem 1 of §02 for the general-$N$ statement."
- `E-weitzenboeck.md` L115: "$m_{\mathrm{KK\,vector}}=\sqrt{12}/r_3 =
  2\sqrt 3/r_3$" — this is correct *for $N=3$*; add "(for $N=3$; in general
  $m_1 = 2\sqrt N/r_3$)".

**§4.3 — `04-lattice-proof-part1.md`, Theorem 1 statement and proof.**
- L189, 241–242, 252–259, 272–276: already partially patched (L241 does
  mention "$2N/r_3^2$ for general $N$"), but the Statement box at L187–189
  still reads "$\mu_1 = 6/r_3^2$". Rewrite Statement box to "$\mu_1\geq
  2N/r_3^2$" and add a proof line "for $N=3$ this is $6/r_3^2$".

**§4.3 — `04-lattice-proof-part1.md`, Theorem 2 statement and proof.**
- L401: "$m_1 = 2\sqrt 3/r_3$" → "$m_1 = 2\sqrt N/r_3$". (Already correctly
  $N$-dependent at L556–561 in the boxed conclusion; only the statement
  prose needs updating.)
- L658: "$m_1 a = 2\sqrt 3\,a/r_3$" → "$m_1 a = 2\sqrt N\,a/r_3$".
- L663: "$\frac{m_1 a}{6} = \frac{a}{\sqrt 3\,r_3}$" → "$\frac{m_1 a}{6}
  = \frac{\sqrt N\,a}{3 r_3}$", with the $N=3$ numerical evaluation kept
  as a side remark.
- L683: "$a_{\mathrm{cross}}\approx 2\sqrt 3\,r_3\,\beta$" → "$a_{\mathrm{cross}}
  \approx 2\sqrt N\,r_3\,\beta$".
- L726: "$\beta < a_0/(2\sqrt 3\,r_3)\sim 10^{14}$" → "$\beta < a_0/(2\sqrt N\,r_3)
  \sim (1/(2\sqrt N))\cdot 10^{15}$", with the $N=3$ evaluation "$\sim
  2.9\times 10^{14}$" as a parenthetical.

**§4.4 — `04-lattice-proof-part1.md`, Theorem 4.**
- L770: "$\lambda_1^{(1)}\geq 6/r_3^2$" → "$\lambda_1^{(1)}\geq 2N/r_3^2$".
- L772: "$m_1 = 2\sqrt 3/r_3$" → "$m_1 = 2\sqrt N/r_3$".
- L877: "$\beta < a/(2\sqrt 3\,r_3)$" → "$\beta < a/(2\sqrt N\,r_3)$".
- L746 (the hypothesis "$r_3/a < \sqrt{3/(4N)}$"): this is already
  $N$-dependent, but the numerics that follow at L777 ("$5.8\times 10^{14}$")
  should be rewritten in terms of $\sqrt N$.

**§4.5 — `04-lattice-proof-part1.md`, Theorem 5.**
- L906: "$m_1 = 2\sqrt 3/r_3$" → "$m_1 = 2\sqrt N/r_3$".

**§4.6 Appendix H — `04-lattice-proof-part1.md` (SU(2) warm-up).**
- Add header convention note (see §3 above).
- L1795 ("Weitzenböck gap") table: fix "$\mathrm{SU}(3)$" column to
  "$2N/r_3^2\ (=6/r_3^2)$" and "$\mathrm{SU}(2)$" column to
  "$1/r_2^2\ (=4/r_3^2\text{ in FS convention, }r_3=2r_2)$".

**§5.1 — `05-continuum-limit.md`.**
- L33: "$\beta < a_0/(2\sqrt 3\,r_3)$" → "$\beta < a_0/(2\sqrt N\,r_3)$".

**§12 Conclusion — `08-conclusion.md`.**
- L9, L14, L20, L95, L154: replace "$6/r_3^2$" and "$2\sqrt 3/r_3$" everywhere
  with the $N$-dependent forms. (These are paraphrases of the abstract and
  will read correctly once the abstract is patched.)

**§3 Quantitative Predictions — `03-quantitative-predictions.md`.**
- L11–16, L82, L118: keep "$\sqrt\sigma = 437$ MeV" but explicitly label
  "evaluated for $\mathrm{SU}(3)$". The formula $\sqrt\sigma \propto 1/r_3$
  is $N$-independent once $g_3$ is fixed; the 437 MeV number is the
  phenomenological $\mathrm{SU}(3)$ case.
- L27: the glueball eigenvalue formula $\lambda_{p,q}= 4[\cdot]/r_3^2$ is
  independent of $N$ only for the scalar Laplacian; the gauge-field 1-form
  spectrum *is* $N$-dependent. Cross-reference to the corrected Theorem 1.

**Appendix I.3 — `I3-N-dependence-tracking.md`.**
- Items 1–4 already state the correct $N$-dependent formulas (this is the
  reference version). Add a cross-reference box to Theorem 1 stating "the
  clean $N$-dependent version of Theorem 1 used throughout is the form
  given here in I.3.2 item 1". Also note that I.3.2 item 1 gives
  $\mu_1\geq 2N/r_3^2$, which is the *Weitzenböck lower bound*; the
  *actual* first eigenvalue is $4N/r_3^2$ and item 2 derives $m_1
  = 2\sqrt N/r_3$ from that tighter value. Clarify which is which.

**Appendix I.4 — `I4-other-gauge-groups.md`.** Already group-specific
(no universal "$6/r_3^2$" claims); no edits needed.

## 5. Convergence window for $N = 2, 3, 4, 5, 8$

Theorem 3 gives $\beta < a/(2\sqrt N\,r_3)$ (ignoring the subleading
$\ln(c_d K C_0^{1/6})$ correction). At the physical $a/r_3\sim 10^{15}$
(§4.1 L130), the convergence window is $\sim 10^{15}/(2\sqrt N)$:

| $N$ | $\sqrt N$ | $\beta_{\max}$ at $a/r_3=10^{15}$ | Margin over $\beta\sim 6$ |
|-----|----------|----------|---------|
| 2 | $1.414$ | $3.54\times 10^{14}$ | $5.9\times 10^{13}$ |
| 3 | $1.732$ | $2.89\times 10^{14}$ | $4.8\times 10^{13}$ |
| 4 | $2.000$ | $2.50\times 10^{14}$ | $4.2\times 10^{13}$ |
| 5 | $2.236$ | $2.24\times 10^{14}$ | $3.7\times 10^{13}$ |
| 8 | $2.828$ | $1.77\times 10^{14}$ | $2.9\times 10^{13}$ |

For every $N\in\{2,3,4,5,8\}$ the margin exceeds $10^{13}$. The
$N$-dependent correction shrinks the window by at most a factor of 2
from $N=2$ to $N=8$, negligible against the $10^{15}$ hierarchy. Larger
$N$ is mildly *worse* through $\sqrt N$ but mildly *better* through
stronger bond suppression $e^{-2\sqrt N\,a/r_3}$; they partially cancel in
the final cluster bound. Lattice mass-gap positivity is robust under the
$N$-dependent patch for every physically relevant $N$.

**Conclusion.** The patch is purely notational: no step of the proof
chain breaks, no constant becomes negative, no convergence radius shrinks
below the physical coupling. It is a 1-page cleanup that makes every
"$6/r_3^2$" and "$2\sqrt 3/r_3$" $N$-dependent and adds a one-paragraph
convention note at the start of Appendix H.
