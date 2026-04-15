## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

The preprint obtains the continuum theory as a subsequential limit via Banach-Alaoglu. This is the standard approach in constructive QFT (it is how all rigorous continuum limits are constructed -- including the phi^4_2, phi^4_3, and Gross-Neveu models). The interrogation raises the question of whether different subsequences could yield different continuum theories, and whether this affects the claimed result. I interrogated four sub-points.

**(a) Different subsequences could give different QFTs.**

The preprint explicitly acknowledges this (lines 2473--2498, "Remark (Uniqueness and subsequence-independence of the mass gap)"):

> "Different subsequences a_{j_1} -> 0 and a_{j_2} -> 0 could in principle yield different limiting Schwinger functions. We do not claim uniqueness of the continuum limit (universality). What is proved is that every subsequential limit satisfies OS1--OS5 with mass gap Delta_infinity > 0, because the RG telescoping sum converges absolutely (independently of the subsequence)."

This is the correct and honest statement. The preprint does not claim universality (uniqueness of the continuum limit). It claims existence of at least one continuum QFT satisfying the Wightman axioms with mass gap Delta_infinity > 0, and further claims that every subsequential limit has the same mass gap. This is sufficient for the Clay prize (see (d) below).

**(b) Universality.**

Universality -- the statement that the continuum limit is unique regardless of the lattice action used or the subsequence chosen -- is a much stronger claim that the preprint correctly does not attempt. For asymptotically free gauge theories, universality is expected on physical grounds (renormalization group universality) but has never been proved rigorously in any 4D interacting QFT. The preprint correctly identifies this as a separate question:

> "Uniqueness of the continuum limit (universality) is a separate question not required for the prize."

The fact that the preprint does not prove universality is not a gap. No construction of an interacting QFT in 4 dimensions has ever established universality. The Jaffe-Witten problem does not require it. Sound.

**(c) Subsequence-independence of Delta_infinity.**

This is the most substantive sub-point. Even if the full set of Schwinger functions depends on the subsequence, does the mass gap value Delta_infinity depend on the subsequence?

The preprint argues (lines 2482--2493):

> "The mass gap value Delta_infinity is subsequence-independent. The RG analysis gives Delta_infinity = C_infinity * Lambda_infinity where C_infinity = C_0 - sum delta C_k with the series converging absolutely (Section 5.4.6), and Lambda_infinity = lim Lambda_k is determined by the convergent infinite product prod(1 + O(g_j^4)) (Section 5.1.4). Both C_infinity and Lambda_infinity are defined as limits of sequences determined entirely by the RG flow -- they do not depend on which subsequence of lattice spacings is used for the Banach-Alaoglu extraction."

This argument is correct and is the key insight. The mass gap is determined by the RG flow -- specifically by the convergent series C_infinity = C_0 - sum delta C_k and the convergent product Lambda_infinity. These are determined by the sequence of running couplings g_k and the one-step mass gap shifts delta C_k, which are intrinsic to the RG trajectory and do not depend on the Banach-Alaoglu subsequence. The Banach-Alaoglu extraction determines which Schwinger functions the subsequence converges to, but the mass gap is already determined before the extraction.

To be precise: the mass gap of any subsequential limit is determined by the exponential decay rate of the two-point function, which in turn is determined by the spectral gap of the transfer matrix. The RG analysis shows that this spectral gap converges to Delta_infinity = C_infinity Lambda_infinity > 0 as k -> infinity, independently of the subsequence. Any subsequential limit of the Schwinger functions must have this same mass gap, because the mass gap is visible in the long-distance behavior of the two-point function, and the two-point function at large separations is determined by the lowest-lying spectral contribution, which converges to e^{-Delta_infinity t}.

A pedantic objection: could a different subsequence of Schwinger functions have a mass gap strictly larger than Delta_infinity? That is, could the one-particle pole disappear in some subsequential limit? The preprint addresses this implicitly through the non-triviality argument (Proposition, lines 2545--2662): the connected two-point function has a lower bound S_2^c(0,t) >= |<1|s_P|0>|^2 e^{-Delta t} with strictly positive coefficient, and this lower bound is a-independent and carries through to the continuum limit. So the one-particle state is present in every subsequential limit, and the mass gap is exactly Delta_infinity (not larger).

Sound. The mass gap is uniquely determined by the RG flow and is the same for all subsequential limits.

**(d) The Jaffe-Witten requirement.**

The Jaffe-Witten problem statement (Jaffe-Witten 2000) asks for the existence of "a quantum Yang-Mills theory" (indefinite article) satisfying the Wightman axioms with mass gap. It does not require uniqueness.

The preprint constructs at least one such theory (via any convergent Banach-Alaoglu subsequence). Every such construction satisfies:
- OS1--OS5 (verified in Section 5.7(f))
- Mass gap Delta_infinity > 0 (verified in Sections 5.1--5.7(d))
- Non-triviality (verified in the Proposition, Section 5.7(f))
- Yang-Mills dynamics (verified via Ward identities and Schwinger-Dyson equations)

If multiple continuum limits exist (which is not excluded), they are all Yang-Mills theories in the sense that they all satisfy the lattice Ward identities that converge to the continuum Ward-Takahashi identities. They all have the same mass gap. They all satisfy the Wightman axioms. Any one of them satisfies the Clay prize requirements.

The preprint also addresses the Jaffe-Witten "compactness warning" explicitly (lines 2499--2516):

> "The mass gap Delta_infinity > 0 is NOT inferred from the lattice mass gap Delta(a) > 0 by a naive compactness argument. Rather, the RG analysis establishes that the ratio C(a) = Delta(a)/Lambda(a) converges to a positive limit C_infinity > 0 as a -> 0, via an absolutely convergent telescoping series whose convergence is proved independently of the subsequence."

This is an important clarification. The preprint does not fall into the trap that Jaffe-Witten warned about (inferring spectral properties of the limit from spectral properties of approximants via compactness alone). The mass gap is established by a quantitative convergence argument (the RG sum), not by compactness. Sound.

**Impact on the claimed result:**
None. The preprint correctly does not claim uniqueness. It establishes that every subsequential limit is a Wightman QFT with mass gap Delta_infinity > 0 (uniquely determined by the RG flow). This is sufficient for the Jaffe-Witten problem, which asks for existence of "a" theory, not uniqueness. The non-uniqueness of the continuum limit is a standard feature of constructive QFT constructions and does not affect Clay prize eligibility.
