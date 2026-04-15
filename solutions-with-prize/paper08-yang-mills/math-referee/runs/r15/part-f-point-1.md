## Part F, Point 1: The OS Axioms -- Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The preprint (Section 5.7(f)) verifies OS1--OS5 for the continuum Schwinger functions obtained as the a -> 0 limit of the lattice theory. I interrogated three specific sub-points.

**(a) OS0' linear growth condition.**

The preprint gives the bound |S_n(f)| <= n! C_0^n ||f||_{L^1} (equation OS1.4). The interrogation asks whether the L^1 norm is dominated by a Schwartz seminorm. The preprint explicitly addresses this (lines 2315--2349, "Lemma (OS0' verification)"):

> "We use the standard Schwartz seminorms... For f in S(R^{4n}) and M > 4n: ||f||_{L^1} <= omega_{4n,M} p_M(f) where omega_{4n,M} < infinity because the integrand decays as |x|^{-M} with M > 4n."

Taking M = 4n+1, the bound becomes |S_n(f)| <= n! C_0^n omega_{4n,4n+1} p_{4n+1}(f), which is the OS0' condition with seminorm index N(n) = 4n+1 growing linearly in n. This is correct and complete. The 1975 corrected OS reconstruction theorem requires exactly this linear growth, and the preprint provides it. The key mathematical fact -- that L^1 norm on Schwartz space is controlled by a Schwartz seminorm because Schwartz functions decay faster than any polynomial -- is not merely asserted but proved with an explicit computation. Sound.

**(b) Separability and the diagonal argument.**

The preprint explicitly states (lines 2355--2363):

> "The Schwartz space S(R^{4n}) is separable (it is a Frechet space with countable seminorm family; see Reed--Simon, Vol. I, Section V.3), so weak-* precompact subsets are weak-* sequentially precompact. A diagonal argument over n = 1, 2, 3, ... extracts a subsequence a_j -> 0 such that S_n^{(a_j)} -> S_n for all n simultaneously."

This is the correct argument. Separability of S(R^{4n}) implies the weak-* topology on bounded subsets of S'(R^{4n}) is metrizable, which upgrades the Banach-Alaoglu precompactness from nets to sequences. The diagonal argument over countably many n is standard. The preprint cites the correct reference (Reed-Simon Vol. I). Sound.

**(c) Coincident-point singularities.**

This was the most substantive concern. The bound |S_n| <= n! C_0^n is stated as a pointwise bound, but Schwinger functions have UV singularities at coincident points. The preprint addresses this in a dedicated subsection (lines 2244--2313, "Coincident-point singularities"):

The argument has two layers:

First, on the lattice, all Schwinger functions are bounded pointwise -- uniformly in all configurations of points, including coincident points -- because gauge fields take values in compact SU(N) and lattice observables are bounded continuous functions. The smeared Schwinger functions S_n^{(a)}(f) satisfy the uniform bound |S_n^{(a)}(f)| <= n! C_0^n ||f||_{L^1} for every a > 0 and every f in S(R^{4n}).

Second, the continuum Schwinger functions S_n = lim S_n^{(a_j)} are tempered distributions by the uniform bound and Banach-Alaoglu. They need not be pointwise functions at coincident points -- the OS framework requires only the distributional (smeared) formulation.

The preprint then provides a detailed analysis of the singularity structure (Kallen-Lehmann form for the two-point function, local integrability lemma for the n-point singularities), which is mathematically careful: the worst-case singularity prod_{i<j} |x_i - x_j|^{-2} is locally integrable in R^{4n} for n <= 4 (verified by power counting: the exponent 4(n-1) - 2 C(n,2) > -1 holds for n <= 4), and for n >= 5 the argument uses iterated partial coincidences.

The essential point is that the distributional formulation -- which is all the OS axioms require -- is fully controlled by the uniform lattice bounds. The pointwise singularity analysis is supplementary. Sound.

**One minor observation:** The local integrability lemma's argument for n >= 5 (using iterated partial coincidences and the OPE) is somewhat informal. The statement "simultaneous collision of all n points has measure zero" is true but not the right reason; what matters is that the singularity is integrable, which requires the OPE estimate. However, the preprint's main argument does not depend on this: the distributional bound |S_n(f)| <= n! C_0^n ||f||_{L^1} is the primary result, and it holds without any analysis of pointwise singularities. The local integrability discussion is supplementary context, not load-bearing.

**Impact on the claimed result:**
None. The OS axioms verification is complete. OS0' is explicitly verified with the correct growth condition. The diagonal argument is correctly stated with separability. Coincident-point singularities are handled by the distributional formulation with uniform lattice bounds.
