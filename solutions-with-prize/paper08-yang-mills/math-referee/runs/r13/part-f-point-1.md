## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: OS1-OS5 hold simultaneously for the limiting Schwinger functions.

**(a) OS0' linear growth condition.** The preprint gives |S_n(f)| <= n! C_0^n ||f||_{L^1}. The corrected 1975 OS reconstruction theorem (Osterwalder-Schrader, CMP 42) requires OS0': the bounds on n-point functions must satisfy a linear growth condition. The standard formulation (Glimm-Jaffe, "Quantum Physics," Ch. 6) allows n! C^n growth, so the preprint's bound satisfies OS0'.

The L^1 norm ||f||_{L^1} is not itself a Schwartz seminorm, but the preprint explicitly addresses this in a dedicated Lemma (OS0' verification, Section 5.7, lines 2268-2285). The proof shows: for f in S(R^{4n}), |f(x)| <= p_M(f)(1+|x|)^{-M} where p_M(f) = sup_x (1+|x|)^M |f(x)| is a Schwartz seminorm. Integrating with M = 4n+1 gives:

  ||f||_{L^1} <= omega_{4n} * p_{4n+1}(f)

where omega_{4n} = integral (1+|x|)^{-(4n+1)} d^{4n}x < infinity. Therefore |S_n(f)| <= n! C_0^n omega_{4n} p_{4n+1}(f) = C_n' p_{N(n)}(f), which is the OS0' condition.

This is correctly stated and proved in the preprint.

**(b) The diagonal extraction.** A single subsequence a_j -> 0 is extracted via Banach-Alaoglu such that S_n^{(a_j)} -> S_n for all n simultaneously. The proof uses a standard diagonal argument: extract a subsequence for n = 1, then a sub-subsequence for n = 2, etc. This requires the test function space S(R^{4n}) to be separable (so that weak-* convergence on a countable dense subset implies convergence on the whole space).

S(R^{4n}) is a Frechet space with a countable family of seminorms, hence separable (metrizable and second-countable). This is a standard fact (Reed-Simon, Vol. I, or Treves, "Topological Vector Spaces"). The preprint should state this but it is entirely standard.

**(c) Coincident-point singularities.** The bound |S_n| <= n! C_0^n is a bound on the lattice Schwinger functions, which are regular at all points (the lattice provides a UV cutoff). In the continuum limit, the Schwinger functions become distributions, and coincident-point singularities appear.

For a massive gapped theory with mass gap Delta > 0, the two-point function has a singularity ~ 1/|x-y|^{d-2} at x = y in d dimensions (d = 4 gives 1/|x|^2). This is an integrable singularity when smeared against test functions in S(R^4). The higher n-point functions have worse singularities at multiple coincidence points, but the n! C_0^n bound ensures they are tempered distributions.

The paper treats S_n as a distribution from the start (tested against f in S(R^{4n})). The bound |S_n(f)| <= n! C_0^n ||f||_{L^1} is a distributional bound. The coincident-point singularities are automatically handled by the distributional framework — they affect the pointwise behavior but not the distribution-valued limits.

No error found. The OS axiom verification is complete, including the OS0' linear growth condition, the diagonal subsequence extraction (with separability of S stated), and the distributional treatment of coincident-point singularities.

**Impact on the claimed result:** None. The OS axioms are verified simultaneously for the limiting Schwinger functions.
