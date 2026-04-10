## Part A, Point 1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$

**Weight:** LIGHT
**Verdict:** CLOSABLE GAP (notation drift; the underlying inequality is correct for each fixed $N$ but the universal statement $\mu_1 \geq 6/r_3^2$ is FALSE for $N=2$ and the universal value $m_1 = 2\sqrt{3}/r_3$ is FALSE for every $N \neq 3$).

**Finding:**

(a) **The Ricci coefficient is correctly $2N/r_3^2$, not the universal $6/r_3^2$.**
The Weitzenböck identity $\Delta_H = \nabla^*\nabla + \mathrm{Ric}$ on 1-forms is standard. For the Fubini–Study metric on $\mathbb{CP}^{N-1}$ (holomorphic sectional curvature $4/r_3^2$), the Ricci tensor is Einstein with constant $2N/r_3^2$ — verified symbolically against the standard $\mathbb{CP}^n$ formula $\mathrm{Ric} = 2(n+1)/r^2 \cdot g$ with $n = N-1$. Section 02 (Theorem 1, Step 2) states this correctly: "$R_{ab} = (2N/r_3^2)g_{ab}$".

The trouble is that **immediately afterward (Step 4), the proof writes "$\mu_1 = 6/r_3^2$" without the qualifier "for $N = 3$"**, and this value is then used universally throughout the abstract, Section 4.3 (cluster expansion), Section 4.4 (Theorem 4), Section 4.5 (Theorem 5), and the propagator bound. For $N = 2$, the Weitzenböck lower bound is $4/r_3^2$, not $6/r_3^2$. The bound $\mu_1 \geq 6/r_3^2$ is **literally false for $\mathrm{SU}(2)$** under the convention used in Sections 02 and 04.

(b) **The KK mass $m_1 = 2\sqrt{3}/r_3$ is N=3-specific.**
Computationally:

| $N$ | I.3.2 formula $m_1 = 2\sqrt{N}/r_3$ | Universal claim $2\sqrt{3}/r_3$ | Relative error |
|-----|---|---|---|
| 2 | $2.83/r_3$ | $3.46/r_3$ | 18.4% |
| 3 | $3.46/r_3$ | $3.46/r_3$ | 0% |
| 4 | $4.00/r_3$ | $3.46/r_3$ | 15.5% |
| 5 | $4.47/r_3$ | $3.46/r_3$ | 29.1% |

The value $2\sqrt{3}/r_3$ corresponds to the "actual" eigenvalue $\mu_{\min}^{(1)} = 12/r_3^2$ (Ikeda–Taniguchi for $\mathbb{CP}^2$), which is the $N = 3$ case of the formula $\mu_{\min}^{(1)} = 4N/r_3^2$ stated in **Appendix I.3.2 item 1**. But Appendix I.3 gives a *different* formula for the actual eigenvalue ($4N$, hence $m_1 = 2\sqrt{N}$) than Section 04.3 line 561 ("$m_1 = 2\sqrt{N}/r_3$ from $\lambda_1^{(1)} = 4N/r_3^2$") — and *yet another* than the abstract and Theorem 5 ("$m_1 = 2\sqrt{3}/r_3$"). These three statements are mutually inconsistent for $N \neq 3$.

Worse, **Appendix H (SU(2) warm-up)** gives the lowest 1-form eigenvalue on $S^2$ of "radius" $r_2$ as $\lambda_1^{(1)} = 2/r_2^2$, hence $m_1 = \sqrt{2}/r_2$ — disagreeing with Appendix I.3's universal "$4N/r_3^2$" formula by a factor of 2 for $N=2$ (which would give $8/r_2^2$). The discrepancy can only be reconciled if "$r_3$" in I.3 and "$r_2$" in Appendix H denote *different* radii (presumably one is the FS radius, the other the standard sphere radius differing by $\sqrt{2}$). The preprint never makes this convention switch explicit, and a Clay referee will flag the resulting inconsistency immediately.

(c) **What this actually breaks (and what it doesn't).**
The cluster expansion convergence threshold "$\beta < a/(2\sqrt{3}\,r_3)$" used in Theorem 4 should read "$\beta < a/(2\sqrt{N}\,r_3)$" for general $N$ (or "$\beta < a/(2\sqrt{2}\,r_2)$" for $N=2$ with the appropriate radius). In the physical regime $a/r_3 \sim 10^{15}$ this still leaves a vast convergence window for every $N \geq 2$, so **lattice mass-gap positivity is unaffected**. But:

- Every quantitative numerical claim that uses "$2\sqrt{3}$" (e.g. "$\sqrt{\sigma} = 437$ MeV" in §3) must be re-derived for each $N$.
- The abstract's universal claim "we prove for any compact simple gauge group $G$" is at best sloppy and at worst misleading: the body of the paper repeatedly substitutes $N=3$ values into formulas labeled as universal.
- For $N = 2$, the problem is more pointed: the preprint's formal "Theorem 1" with $\mu_1 \geq 6/r_3^2$ is **false** under the convention of Sections 02–04. A separate (and inconsistent) bound is given in Appendix H.

**To close:** rewrite Theorem 1 as $\mu_1 \geq 2N/r_3^2$ (the genuine Weitzenböck statement), reconcile the conventions of $r_3$ between Sections 02–05 and Appendix H, and propagate the $N$-dependent constants through Theorems 2–5 and the cluster expansion bound. **Difficulty: 1 page.** No new mathematics is required, only a notation cleanup and a $\sqrt{N}$ substitution.

**Impact on the claimed result:** None at the level of $\Delta_0 > 0$ or $\Delta_\infty > 0$, since the qualitative bound is positive for every $N$. **Impact at the level of Clay eligibility:** moderate — a referee will require a clean version where the $N$-dependence is explicit and consistent across sections.
