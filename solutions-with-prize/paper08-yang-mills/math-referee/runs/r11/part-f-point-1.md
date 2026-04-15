## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) OS0' linear growth condition.**

The preprint gives $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$. The OS0' condition requires $|S_n(f)| \leq C^n n! \cdot p_N(f)^n$ for some Schwartz seminorm $p_N$.

Is $\|f\|_{L^1} \leq C \cdot p_N(f)$ for some Schwartz seminorm? Yes. For $f \in \mathcal{S}(\mathbb{R}^{4n})$ and $N > 4n$:
$$\|f\|_{L^1} = \int |f(x)| dx \leq \int (1+|x|)^{-N} dx \cdot \sup_x (1+|x|)^N |f(x)| = C_{N,4n} \cdot p_{N,0}(f)$$
where $C_{N,4n} = \int_{\mathbb{R}^{4n}} (1+|x|)^{-N} dx < \infty$ for $N > 4n$, and $p_{N,0}(f) = \sup_x (1+|x|)^N |f(x)|$ is a Schwartz seminorm.

The required $N$ grows linearly with $n$: $N > 4n$. This is consistent with OS0' (which allows $N$ to depend linearly on $n$). So the preprint's bound does satisfy OS0'. However, this should be stated explicitly in the text — the passage from $L^1$ to Schwartz seminorms is not automatic and requires the observation above.

**The gap:** The identification of $\|f\|_{L^1}$ as dominated by a Schwartz seminorm is mathematically trivial but should be stated as a one-line remark for completeness.

**(b) The diagonal extraction.**

The Banach-Alaoglu argument requires weak-$*$ sequential compactness, which holds when the predual is separable. The Schwartz space $\mathcal{S}(\mathbb{R}^{4n})$ is a Fréchet space with a countable family of seminorms, hence separable. Weak-$*$ precompact subsets of the dual $\mathcal{S}'(\mathbb{R}^{4n})$ are weak-$*$ sequentially precompact (by the Eberlein-Šmulian theorem for the bidual, or more directly by the separability of $\mathcal{S}$).

The diagonal argument over $n = 1, 2, 3, \ldots$ extracts a single subsequence $a_j \to 0$ such that $S_n^{(a_j)} \to S_n$ for all $n$ simultaneously. This is standard (used in every constructive QFT text, e.g., Glimm-Jaffe Chapter 6). The separability of $\mathcal{S}(\mathbb{R}^{4n})$ is not stated in the preprint but is a standard fact requiring no argument.

**(c) Coincident-point singularities.**

The bound $|S_n| \leq n! C_0^n$ is a bound on the Schwinger functions as tempered distributions, valid when smeared against Schwartz test functions. At coincident points ($x_i = x_j$), the Schwinger functions have UV singularities that are regulated on the lattice (by the lattice spacing $a$) but could diverge as $a \to 0$.

For a massive gapped theory, the two-point function behaves as $S_2(x-y) \sim |x-y|^{-2} e^{-\Delta|x-y|}$ for $|x-y| \to 0$ (up to logarithmic corrections from anomalous dimensions). In $d = 4$, $|x|^{-2}$ is locally integrable ($\int_0^\epsilon r^{-2} r^3 dr = \epsilon^2/2 < \infty$), so coincident-point singularities are integrable.

The preprint addresses this in Section 5.7(f) with a lemma verifying that $|x|^{-2} e^{-\Delta|x|}$ is locally $L^1$ in $\mathbb{R}^4$. The OS axioms are formulated for tempered distributions, and the test functions $f \in \mathcal{S}(\mathbb{R}^{4n})$ automatically avoid the worst singularities through their smoothness. The lattice Schwinger functions are bounded distributions (they are finite sums), and the limit is a tempered distribution by the OS0' bound.

**The gap (minor):** The coincident-point analysis in the preprint is present but brief. For higher $n$-point functions, the singularity structure is more complex (multiple coincident limits, cross-ratios). The preprint's argument handles this through the factorial bound $|S_n| \leq n! C_0^n$ which is uniform in $a$ and provides distributional control. A more detailed analysis of the singularity structure would strengthen the presentation but is not mathematically necessary given the distributional framework.

**Closing the gap:** 1 paragraph adding the explicit Schwartz seminorm domination of $L^1$ norm.

**Impact on the claimed result:** (ii) Subsidiary presentation issue. The OS0' condition IS satisfied; the gap is in the explicitness of the argument, not in its validity.
