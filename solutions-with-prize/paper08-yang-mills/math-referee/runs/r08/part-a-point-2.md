## Part A, Point 2: KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

(a) The transfer matrix estimate for the propagator is standard. The lattice energy m_n^{latt} satisfies cosh(m_n^{latt} a) = 1 + m_n^2 a^2/2, giving m_n^{latt} a ≥ m_n a - O(ln(m_n a)) for m_n a ≥ 1. The bound G_n(a) ≤ (C_1/(m_n a)) e^{-m_n a} follows from the trace-class property of the transfer matrix on CP^{N-1}. Since CP^{N-1} is compact with positive-definite metric, the Hodge Laplacian has discrete spectrum with no zero modes (H^1 = 0), so the transfer matrix is trace-class. The exponential decay follows from the spectral gap. There are no boundary corrections because CP^{N-1} is a closed manifold — there is no boundary. Finite-volume effects are absent at the level of the internal space: each site carries a separate copy of the full CP^{N-1}.

(b) The constant C_0 depends on N through two mechanisms: (i) the Weyl asymptotics of the eigenvalue degeneracies d_n ~ n^{N-2}, and (ii) the dimension of the adjoint representation (N^2-1). The sum over KK modes converges because m_n - m_1 ≥ c(n-1)/r_3 grows linearly, dominating the polynomial growth d_n ~ n^{N-2}. For each fixed N, C_0 is a finite computable constant. The proof explicitly tracks this N-dependence in the Weyl sum (Step 4 of Theorem 2) and notes that C_0 depends on N but not on β or a/r_3. The growth of C_0 with N is at most polynomial (from the Weyl asymptotics and adjoint dimension), which does not compromise the cluster expansion because the exponential suppression e^{-m_1 a} with m_1 a ~ 10^{15} provides a margin of ~10^{14} orders of magnitude.

**Impact on the claimed result:** None. The propagator bound is rigorously established. The N-dependence of C_0 is finite for each fixed N and does not affect the convergence of the cluster expansion.
