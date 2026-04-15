## Part A, Point 1: The Weitzenböck Spectral Gap on CP^{N-1}

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim: the Hodge Laplacian on 1-forms on (CP^{N-1}, g_FS) has spectral gap mu_1 >= 6/r_3^2, driving KK mass m_1 = 2sqrt(3)/r_3.

**(a) The spectral bound.** The Weitzenböck formula Delta_H = nabla*nabla + Ric on 1-forms is standard (Besse, "Einstein Manifolds," Ch. 12; Bochner 1946). For CP^{N-1} with Fubini-Study metric normalized to holomorphic sectional curvature 4/r_3^2, the Ricci tensor is:

  Ric_{ab} = (2N/r_3^2) g_{ab}

This follows from CP^{N-1} being Kähler-Einstein of complex dimension N-1 with Einstein constant 2N/r_3^2 (Kobayashi-Nomizu Vol. II, Ch. IX). Since nabla*nabla >= 0, the Weitzenböck formula gives:

  mu_1 >= 2N/r_3^2

For N = 3 (CP^2): mu_1 >= 6/r_3^2. Correct. For N = 2 (CP^1 = S^2): mu_1 >= 4/r_3^2. For general N >= 2: the bound *improves* with N.

The preprint states mu_1 >= 6/r_3^2 specifically in the context of CP^2. For general CP^{N-1}, the bound mu_1 >= 2N/r_3^2 is stated in Section I.3 (N-dependence tracking) and is correct. The fact that H^1(CP^{N-1}) = 0 means there are no harmonic 1-forms, so the gap is strict (no zero eigenvalue).

**(b) The connection to KK mass.** The actual first eigenvalue of the Hodge Laplacian on 1-forms on CP^2 is mu_1 = 12/r_3^2 (Appendix E, computed from SU(3) representation theory for the (3,1) + (1,bar{3}) representations). The Weitzenböck bound 6/r_3^2 is not tight — the actual value exceeds it by a factor of 2, as expected for Kähler manifolds.

The KK mass is m_1 = sqrt(mu_1) = sqrt(12)/r_3 = 2sqrt(3)/r_3. This is the square root of the spectral gap — standard for KK reduction (the mass-squared of a 4D field equals the Laplacian eigenvalue on the internal space). The factor 2sqrt(3) is correct for the actual eigenvalue, not the Weitzenböck lower bound.

For general CP^{N-1}, the actual first eigenvalue on 1-forms is mu_1 = 4N/r_3^2 (from the (N,1) representation of SU(N)), giving m_1 = 2sqrt(N)/r_3. This scales as sqrt(N), which is favorable (the KK mass increases with N). The I.3 supplement confirms this scaling.

No error found. The spectral gap is a rigorous consequence of the Weitzenböck formula applied to a well-understood compact Einstein manifold. The numerical values are exact (from representation theory), not just bounds.

**Impact on the claimed result:** None. This step is sound and provides the foundation for the cluster expansion (the exponential suppression e^{-m_1 a} of KK modes).
