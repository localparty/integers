## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim is that OS1–OS5 hold simultaneously for the limiting Schwinger functions.

**(a) OS0' linear growth condition.** The preprint gives $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$. The corrected OS reconstruction theorem (1975) requires $|S_n(f)| \leq C^n n! \cdot p_N(f)^n$ for some Schwartz seminorm $p_N$. The $L^1$ norm is not itself a Schwartz seminorm. However, for Schwartz functions $f \in \mathcal{S}(\mathbb{R}^{4n})$: $\|f\|_{L^1} \leq C_N \cdot p_N(f)$ for a sufficiently high Schwartz seminorm $p_N$ (because Schwartz functions decay faster than any polynomial, so $\int |f| dx$ is bounded by a seminorm involving polynomial weights and derivatives). This is a standard functional analysis fact, but it should be stated explicitly in the paper.

**Update:** Upon closer examination, Section 5.7(f) OS1 provides the full bound $|S_n(f)| \leq n! C_0^n \omega_{4n,4n+1} p_{4n+1}(f)$ with Schwartz seminorm index $N(n) = 4n+1$ linear in $n$. This satisfies OS0' with the corrected (1975) regularity condition. The passage from $L^1$ norm to Schwartz seminorms IS in the paper. No gap.

**(b) The diagonal extraction.** A single Banach–Alaoglu subsequence $a_j \to 0$ is extracted such that $S_n^{(a_j)} \to S_n$ for all $n$ simultaneously. The proof uses a diagonal argument over $n = 1, 2, 3, \ldots$. This requires the test function space to be separable. $\mathcal{S}(\mathbb{R}^{4n})$ is separable (it is a nuclear Fréchet space with a countable dense subset given by polynomials times Gaussians, or equivalently Hermite functions). This is standard and does not need explicit statement, though it would be pedantic to require it.

**(c) Coincident-point singularities.** The bound $|S_n| \leq n! C_0^n$ is a bound on the integrated Schwinger functions, not a pointwise bound. At coincident points ($x_i = x_j$), the Schwinger functions have UV singularities regulated on the lattice. For a massive gapped theory, these singularities are expected to be mild (power-law in $|x_i - x_j|$ with exponents determined by the canonical dimension). The paper addresses this through the distributional nature of $S_n$: the Schwinger functions are tempered distributions (by OS0'), and the UV singularities are controlled by the Källén–Lehmann representation plus the linked cluster expansion (mentioned in Appendix L as unconditional progress). A complete treatment of coincident-point singularities would require establishing the OPE (Conjecture L.4), which is acknowledged as open.

**Impact on the claimed result:**
Affects (iii) Clay prize eligibility only marginally. The OS0' → Schwartz seminorm gap is trivially closable. The diagonal extraction is standard. The coincident-point issue is more subtle but does not affect the mass gap claim — it is part of the OPE/field operator structure that the paper explicitly defers to Conjectures L.1–L.4.
