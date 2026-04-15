## Part F, Point 1: The OS Axioms -- Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) OS0' linear growth condition.** The preprint establishes $|S_n(f)| \leq n!\,C_0^n\,\|f\|_{L^1}$. The OS0' condition (Osterwalder-Schrader 1975) requires $|S_n(f)| \leq \sigma_n\,p_N(f)^n$ where $\sigma_n \leq A\,(n!)^B$ and $p_N$ is a Schwartz seminorm.

The $L^1$ norm is NOT a Schwartz seminorm (it does not involve derivatives or polynomial weights). However, for Schwartz-class functions $f \in \mathcal{S}(\mathbb{R}^{4n})$:

$$\|f\|_{L^1} = \int |f(x)|\,dx \leq C_{4n,N}\,p_N(f)$$

for any Schwartz seminorm $p_N(f) = \sup_x (1+|x|)^N \sum_{|\alpha| \leq N} |D^\alpha f(x)|$ with $N > 4n$ (ensuring integrability of the weight $(1+|x|)^{-N}$). So $\|f\|_{L^1} \leq C_{4n,N}\,p_N(f)$ holds for $N > 4n$.

This means the preprint's bound DOES satisfy OS0', but with $N$ depending on $n$ (the number of points). The OS0' condition allows this: $p_N$ can depend on $n$. The bound becomes:

$$|S_n(f)| \leq n!\,C_0^n\,C_{4n,N}^n\,p_N(f)^n$$

This satisfies OS0' with $\sigma_n = n!\,(C_0 C_{4n,N})^n$ and growth bound $\sigma_n \leq A\,(n!)^B$ for appropriate $A, B$ (taking $C_{4n,N} \sim (4n)!^C$ gives $\sigma_n \leq (n!)^{1+C'}$, polynomial in $n!$).

The argument is correct but **should be stated explicitly** in the preprint. Currently, the bound $|S_n| \leq n!\,C_0^n\,\|f\|_{L^1}$ is given without the explicit passage to Schwartz seminorms. This is a standard functional analysis step (1 paragraph), but its omission could raise questions from a pedantic Clay SAB reviewer.

**(b) The diagonal extraction.** A single Banach-Alaoglu subsequence $a_j \to 0$ is extracted such that $S_n^{(a_j)} \to S_n$ for all $n$ simultaneously, via a diagonal argument over $n = 1, 2, 3, \ldots$.

This requires the test function space $\mathcal{S}(\mathbb{R}^{4n})$ to be separable (so that weak-$*$ sequential compactness holds on bounded subsets). Schwartz space IS separable: it is a Frechet space with a countable family of seminorms, and its topology has a countable base (via rational polynomial-weighted smooth functions). This is standard (Treves, "Topological Vector Spaces," 1967) but not stated in the preprint.

The diagonal argument itself is textbook: extract a subsequence for $n = 1$; from that, extract a sub-subsequence for $n = 2$; etc. The diagonal subsequence works for all $n$.

**(c) Coincident-point singularities.** This is the most substantive issue in this point.

The bound $|S_n| \leq n!\,C_0^n$ is established for test functions $f$ supported AWAY from coincident points (where $x_i \neq x_j$ for all $i \neq j$). At coincident points, the lattice Schwinger functions are bounded (SU($N$) link variables take values in a compact group, so all lattice correlators are bounded). But in the continuum limit $a \to 0$, coincident-point singularities may emerge.

For a massive gapped theory, coincident-point singularities are expected to be mild (at worst power-law in $|x_i - x_j|$, controlled by the operator product expansion). The lattice regulator provides an explicit UV cutoff. The continuum limit of $S_n$ exists as a tempered distribution (by the Banach-Alaoglu argument applied to the test function space). At coincident points, the distributional nature is encoded in the Schwartz seminorm bounds.

However, the preprint does not explicitly address the passage from pointwise bounds (away from coincident points) to distributional bounds (including coincident points). For a complete proof, one should state:

*"The lattice Schwinger functions $S_n^{(a)}(f)$ are defined for all $f \in \mathcal{S}(\mathbb{R}^{4n})$ (including test functions with support at coincident points) and satisfy $|S_n^{(a)}(f)| \leq n!\,C_0^n\,\|f\|_{L^1}$ uniformly in $a$. The continuum limit $S_n(f) = \lim_{j\to\infty} S_n^{(a_j)}(f)$ is therefore a tempered distribution."*

The uniform bound is available because lattice correlators of gauge-invariant operators are bounded (compact group values), but this step should be explicit.

**Difficulty:** 1 paragraph to close. The functional analysis is standard.

**Impact on the claimed result:** Does not affect the main claim $\Delta_\infty > 0$. Affects the completeness of the OS axiom verification for Clay eligibility. The gap is purely presentational: the mathematical content is correct, but two standard steps (Schwartz seminorm passage, coincident-point treatment) should be stated explicitly for a prize-level proof.
