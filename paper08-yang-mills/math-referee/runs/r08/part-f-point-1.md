## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

(a) The bound $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ satisfies the corrected OS0' linear growth condition (Osterwalder-Schrader 1975). The $L^1$ norm is not itself a Schwartz seminorm, but the preprint explicitly proves $\|f\|_{L^1} \leq C_{4n} \cdot p_{4n+1}(f)$ where $p_M(f) = \sup_x (1+|x|)^M |f(x)|$ is a Schwartz seminorm. The bound uses $|f(x)| \leq p_M(f)(1+|x|)^{-M}$ and $\int (1+|x|)^{-M} d^{4n}x < \infty$ for $M > 4n$. This is stated explicitly in the preprint (Section 5.7(f), OS1). SOUND.

(b) The diagonal extraction uses Banach-Alaoglu on each $n$ sequentially, then a diagonal argument over $n = 1, 2, 3, ...$. This requires the test function space to be separable. The space $\mathcal{S}(\mathbb{R}^{4n})$ IS separable (it is a Frechet space with a countable family of seminorms, and Schwartz functions can be approximated by functions with rational coefficients). However, the preprint does not state this explicitly. **This is a minor presentation gap** — the separability of $\mathcal{S}$ is a standard fact in functional analysis (e.g., Reed-Simon, Vol. I, Section V.3). Closable with one sentence.

(c) Coincident-point singularities are regulated on the lattice. In the continuum limit, the Schwinger functions are distributions (not pointwise functions). The bound $|S_n| \leq n! C_0^n$ is a distributional bound: it controls the smeared Schwinger functions $S_n(f)$ for Schwartz test functions $f$. At coincident points, the lattice regularization prevents divergences, and the distributional nature of the limit handles the UV singularities automatically. For a massive gapped theory, the OPE singularities at coincident points are controlled by the mass gap: the Kallen-Lehmann representation gives $S_2(x,y) \sim |x-y|^{-2} e^{-\Delta|x-y|}$ (up to logs), which is locally integrable and defines a distribution. The preprint addresses this implicitly through the distributional framework (all axioms are verified for smeared Schwinger functions), but does not discuss pointwise singularities explicitly. **This is a presentation gap, not a mathematical gap** — the distributional nature of Schwinger functions is built into the OS axiom framework.

**Impact on the claimed result:** Minor presentation gaps (separability of Schwartz space, coincident-point singularities) closable with standard references. No mathematical gap.
