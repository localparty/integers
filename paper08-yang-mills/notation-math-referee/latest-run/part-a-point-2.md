## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim is that the propagator between neighboring lattice sites satisfies $|g_b| \leq C_0 e^{-2\sqrt{N}\,a/r_3}$ (integrated bond activity in the $c_2 = 0$ sector).

**(a) Transfer matrix estimate.** The bound is derived in Theorem 2 (Section 4.3) through four steps:

1. The KK reduction expands internal connections in eigenmodes of the Hodge Laplacian: $A(x,y) = \sum_n \phi_n(x) \omega_n(y)$ with mass $m_n = \sqrt{\lambda_n^{(1)}}/r_3$.
2. The nearest-neighbor propagator $G_n(a) = |\langle \phi_n(x) \phi_n(x+a\hat{\mu})^\dagger \rangle|$ admits a transfer matrix representation with lattice energy $\cosh(m_n^{\mathrm{latt}} a) = 1 + m_n^2 a^2/2$.
3. For $m_n a \geq 1$: $G_n(a) \leq (C_1/m_n a) e^{-m_n a}$ (standard lattice propagator bound, Lüscher 1977, Seiler 1982).
4. Sum over KK modes: the polynomial degeneracy $d_n \sim n^{N-2}$ is dominated by the exponential suppression $e^{-(m_n - m_1)a}$ for $a/r_3 \gg 1$.

The transfer matrix on $\mathbb{CP}^{N-1}$ is trace-class because the Hodge Laplacian on a compact manifold has discrete spectrum with eigenvalues growing without bound, and $e^{-t\Delta_{\mathrm{Hodge}}}$ is trace-class for $t > 0$. The propagator bound follows from the spectral gap via the standard spectral representation. No boundary corrections or finite-volume effects modify the exponential decay on $\mathbb{CP}^{N-1}$ because $\mathbb{CP}^{N-1}$ is compact and the spectrum is discrete with gap $\mu_1 > 0$.

**(b) The constant $C_0$.** The constant $C_0$ is computed as $C_0 = C_4$, where $C_4$ absorbs the mode sum $\sum_n d_n e^{-(m_n - m_1)a}/(m_n a)$. This depends on $N$ through the Weyl asymptotics ($d_n \sim n^{N-2}$, $m_n \sim n^{1/(2(N-1))}/r_3$) but is finite for each fixed $N$ and independent of $\beta$ and $a/r_3$.

The crucial point is that $C_0$ does not grow faster than the exponential decay: the mode sum $\sum_{n \geq 2} n^{N-2} e^{-c n^{1/(2(N-1))} a/r_3}$ converges for $a/r_3 \gg 1$ with a bound that is polynomial in $N$. For the cluster expansion, what matters is $C_0 e^{-m_1 a} \ll 1$, which is astronomically satisfied ($e^{-10^{15}}$) for physical parameters. The $N$-dependence of $C_0$ is tracked in Appendix I.3: $C_0 = O(\mathrm{poly}(N))$, which does not compromise the cluster expansion for any fixed $N$.

The paper correctly distinguishes between the **integrated** bond activity (expectation under the free Gaussian measure for internal fields) and the pointwise value. The KP criterion applies to the integrated activity, which is the correct quantity.

**Impact on the claimed result:**
No impact. The propagator bound is correct and feeds cleanly into the Kotecký–Preiss convergence criterion.
