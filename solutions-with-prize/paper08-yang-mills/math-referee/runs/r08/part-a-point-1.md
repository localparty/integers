## Part A, Point 1: Weitzenböck Spectral Gap on CP^{N-1}

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

(a) The Weitzenböck formula claim is verified. The Fubini-Study metric on CP^{N-1} is Einstein with Ric_{ab} = (2N/r_3^2) g_{ab}. The Weitzenböck identity gives Δ_Hodge a = ∇*∇ a + Ric(a) ≥ (2N/r_3^2) a for 1-forms, since ∇*∇ ≥ 0. For N=3, this gives μ_1 ≥ 6/r_3^2. For general N ≥ 2, the bound is 2N/r_3^2, which improves with N. The preprint correctly states the general N bound and specializes to N=3 for the physical case. The absence of zero modes follows from H^1(CP^{N-1};R) = 0 for all N ≥ 2. The actual first eigenvalue μ_min^{(1)} = 12/r_3^2 (from Ikeda-Taniguchi 1978 and representation-theoretic calculations) exceeds the Weitzenböck bound by a factor of 2. The proof uses only the weaker bound 6/r_3^2, building in a safety factor.

(b) The KK mass m_1 = 2√3/r_3 is derived from the actual spectral gap μ_min^{(1)} = 12/r_3^2 (not from the Weitzenböck lower bound 6/r_3^2). The factor 2√3 = √12 is the square root of 12, which is correct: m_1 = √(λ_1^{(1)})/r_3 = √(12/r_3^2)/r_3... wait, let me recalculate. The eigenvalue is λ_1^{(1)} = 12/r_3^2 (dimensionless eigenvalue times 1/r_3^2 from the Laplacian scaling). The KK mass is m_n = √(λ_n^{(1)})/r_3 — but actually examining the preprint more carefully: Section 1.4 states m_n = √(λ_n^{(1)})/r_3, and from Section 4.2 (Theorem 2 proof, Step 1), the eigenvalues λ_n^{(1)} of the Hodge Laplacian are on (CP^{N-1}, g_FS) with the actual first eigenvalue 12/r_3^2. So m_1 = √(12/r_3^2) = 2√3/r_3. This is correct. The mass is the square root of the eigenvalue of the Laplacian, which is already in units of 1/r_3^2, so m_1 = √(12)/r_3 = 2√3/r_3. Correct.

**Impact on the claimed result:** None. The spectral gap is rigorously established with a safety factor of 2 over the Weitzenböck lower bound.
