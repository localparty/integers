## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) OS0' linear growth condition.** The bound $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ is claimed to satisfy the corrected OS0' condition (Osterwalder-Schrader 1975). OS0' requires $|S_n(f)| \leq C^n n! \cdot p_N(f)^n$ for some Schwartz seminorm $p_N$.

The preprint argues: $\|f\|_{L^1} \leq C_{4n} \cdot p_{4n+1}(f)$ where $p_M(f) = \sup_x (1+|x|)^M |f(x)|$ is a standard Schwartz seminorm. This follows from $|f(x)| \leq p_M(f)(1+|x|)^{-M}$ and $\int (1+|x|)^{-M} d^{4n}x < \infty$ for $M > 4n$.

This is correct. The $L^1$ norm IS dominated by a Schwartz seminorm, specifically $\|f\|_{L^1} \leq C_{4n} p_{4n+1}(f)$. The resulting bound $|S_n(f)| \leq n! C_0^n C_{4n} p_{4n+1}(f)$ has the right form for OS0'. The Schwartz seminorm depends on $n$ (through $4n+1$), which is allowed by the OS0' formulation.

**The gap:** The argument should be stated as an explicit lemma rather than a parenthetical remark. For a Millennium Prize paper, the verification of the specific version of the OS reconstruction theorem being used (1973 vs. 1975) deserves a dedicated paragraph.

**(b) The diagonal extraction.** The proof uses a diagonal argument over $n = 1, 2, 3, \ldots$ to extract a single subsequence $a_j \to 0$ such that $S_n^{(a_j)} \to S_n$ for all $n$ simultaneously.

Separability of $\mathcal{S}(\mathbb{R}^{4n})$ IS stated (Section 5.7(f), line 2163): "The Schwartz space $\mathcal{S}(\mathbb{R}^{4n})$ is separable (it is a Fréchet space with countable seminorm family; see Reed-Simon, Vol. I, Section V.3)." This ensures weak-$*$ precompact subsets are weak-$*$ sequentially precompact, validating the diagonal argument.

**(c) Coincident-point singularities.** The preprint addresses this explicitly (lines 2143-2153):

> "On the lattice, all Schwinger functions are bounded pointwise (the gauge fields take values in the compact group SU($N$))... The OS axiom framework is formulated entirely in terms of the smeared Schwinger functions $S_n(f)$ for Schwartz test functions $f$."

The distributional nature handles UV singularities automatically. For the massive gapped theory, the Källén-Lehmann representation gives two-point singularities of the form $|x-y|^{-2} e^{-\Delta|x-y|}$ (up to logarithms), which are locally integrable in $d = 4$.

**The gap:** The statement "locally integrable in $d = 4$" is correct but should be proved, not asserted. The singularity $|x|^{-2}$ is locally integrable in $\mathbb{R}^4$ (it has the right scaling: $\int_{|x|<\epsilon} |x|^{-2} d^4x = C\epsilon^2 < \infty$). This is a one-line calculation that should be included.

**Closable with:** Two short paragraphs: (1) an explicit lemma showing $\|f\|_{L^1} \leq C_n p_{4n+1}(f)$, and (2) a one-line verification that $|x|^{-2}$ is locally integrable in $\mathbb{R}^4$.

**Impact on the claimed result:** None if closed. The OS axioms are correctly verified; the gaps are presentational.
