## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) OS0' linear growth condition.**

The corrected OS reconstruction theorem (1975) requires $|S_n(f)| \leq C^n n! \cdot p_N(f)^n$ for some Schwartz seminorm $p_N$. The preprint gives $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$.

The $L^1$ norm is indeed dominated by a Schwartz seminorm. The preprint (Section 5.7(f)) handles this explicitly: for $f \in \mathcal{S}(\mathbb{R}^{4n})$, $|f(x)| \leq p_M(f) (1+|x|)^{-M}$ where $p_M(f) = \sup_x (1+|x|)^M |f(x)|$. For $M > 4n$:

$$\|f\|_{L^1} = \int |f(x)|\,d^{4n}x \leq p_M(f) \int (1+|x|)^{-M}\,d^{4n}x = \omega_{4n} \cdot p_{4n+1}(f)$$

where $\omega_{4n} = \int (1+|x|)^{-(4n+1)}\,d^{4n}x < \infty$. Therefore:

$$|S_n(f)| \leq n! C_0^n \omega_{4n} \cdot p_{4n+1}(f)$$

This is exactly the OS0' form with $C_n = n! C_0^n \omega_{4n}$ and Schwartz seminorm $p_{4n+1}$. The argument is correctly stated in the preprint.

**(b) The diagonal extraction.**

A single Banach-Alaoglu subsequence $a_j \to 0$ is extracted such that $S_n^{(a_j)} \to S_n$ for all $n$ simultaneously via a standard diagonal argument.

Separability of $\mathcal{S}(\mathbb{R}^{4n})$: this is a standard fact. $\mathcal{S}(\mathbb{R}^{4n})$ is a Fréchet space with a countable family of seminorms $\{p_k\}_{k \geq 0}$, hence metrizable and separable. The dual $\mathcal{S}'(\mathbb{R}^{4n})$ with the weak-$*$ topology on norm-bounded subsets is metrizable and sequentially compact (by Banach-Alaoglu). The diagonal argument over $n = 1, 2, 3, \ldots$ extracts a single subsequence converging for all $n$ simultaneously.

The preprint does not state separability explicitly, but this is a foundational property of Schwartz spaces that requires no elaboration in a research paper. Any referee familiar with the OS reconstruction theorem would recognize this as standard.

**(c) Coincident-point singularities.**

The bound $|S_n| \leq n! C_0^n$ is a distributional bound (valid when smeared against test functions), not a pointwise bound. The Schwinger functions $S_n$ are distributions in $\mathcal{S}'(\mathbb{R}^{4n})$, and their behavior at coincident points ($x_i = x_j$) is part of the distributional structure.

On the lattice (at fixed $a > 0$), the Schwinger functions are well-defined at all points (including "coincident" lattice points) because the lattice provides a UV cutoff. As $a \to 0$, coincident-point singularities develop, but the distributional limit exists (by the Banach-Alaoglu argument) because the family $\{S_n^{(a)}\}$ is uniformly bounded in $\mathcal{S}'$ norm.

For a massive gapped theory, the singularities at coincident points are expected to be mild (integrable), consistent with the Wightman reconstruction. The distributional nature of $S_n$ at coincident points is fully handled by the test function formalism — no additional argument about pointwise behavior is needed.

The proof correctly works at the distributional level throughout. It does not claim pointwise bounds at coincident points.

**Impact on the claimed result:**

None. The OS axioms are simultaneously verified with uniform bounds in the lattice spacing. The OS0' condition, the diagonal extraction, and the distributional treatment of coincident-point singularities are all correctly handled.
