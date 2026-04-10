## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim: the propagator between neighboring lattice sites satisfies |g_b| <= C_0 e^{-2sqrt(3) a/r_3}.

**(a) Transfer matrix estimate.** The bound is derived from the lattice transfer matrix with spectral gap m_1. In the c_2 = 0 topological sector, the KK modes phi_n(x) have lattice propagator:

  G_n(a) = |<phi_n(x) phi_n(x + a hat{mu})^dagger>| <= (C_1 / m_n a) e^{-m_n a}

This is a standard lattice propagator bound obtained from the transfer matrix representation: G_n(a) = <0|hat{phi}_n e^{-aH_n} hat{phi}_n^dagger|0> <= ||hat{phi}_n||^2 e^{-m_n^{latt} a}, where m_n^{latt} is the lattice dispersion energy satisfying cosh(m_n^{latt} a) = 1 + m_n^2 a^2/2. For m_n a >= 1, this gives m_n^{latt} a >= m_n a - O(ln(m_n a)).

CP^{N-1} is compact, so the transfer matrix is trace-class (the spectrum is discrete with eigenvalues growing as Weyl's law dictates). There are no boundary corrections because CP^{N-1} has no boundary. No finite-volume effects arise because CP^{N-1} is already a finite-volume (compact) space. The estimate is standard and rigorous.

**(b) The constant C_0.** The bond activity sums over all KK modes:

  Sum_{n >= 1} d_n (C_1 / m_n a) e^{-m_n a} <= C_3 e^{-m_1 a}

where d_n ~ n^{N-2} are the degeneracies (from Weyl asymptotics on CP^{N-1}) and m_n ~ n^{1/(N-1)}/r_3. The sum converges because the gap m_n - m_1 >= c(n-1)/r_3 grows with n, and the exponential e^{-(m_n - m_1)a} dominates the polynomial d_n.

The constant C_0 = C_3 depends on N. From the I.3 supplement: C_0 ~ O(N^{N-1}), which is unfavorable but finite for each N. The key point is that C_0 enters the cluster expansion through C_0^{1/6} e^{-m_1 a/6}, and the exponential e^{-m_1 a/6} with m_1 a ~ 10^{15} overwhelms any polynomial or sub-exponential function of N. For each fixed N, the cluster expansion converges with enormous margin.

No error found. The propagator bound is a straightforward consequence of the transfer matrix on a compact internal space with spectral gap.

**Impact on the claimed result:** None. This step is sound and provides the key input for the Kotecky-Preiss cluster expansion convergence.
