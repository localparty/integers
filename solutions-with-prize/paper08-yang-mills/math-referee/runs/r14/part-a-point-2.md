## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Transfer matrix estimate.** The propagator bound $|g_b| \leq C_0 e^{-m_1 a}$ (Theorem 2) is derived from the transfer matrix on $\mathbb{CP}^{N-1}$ via standard lattice estimates (Luscher 1977, Seiler 1982). The transfer matrix on the compact space $\mathbb{CP}^{N-1}$ is trace-class because the spectrum of the Hodge Laplacian is discrete with finite degeneracies (Weyl asymptotics: $d_n \sim n^{N-2}$). The propagator bound follows from the spectral representation:

$$G_n(a) \leq \frac{C_1}{m_n a}\,e^{-m_n a} \quad\text{for}\; m_n a \geq 1$$

There are no boundary corrections or finite-volume effects on $\mathbb{CP}^{N-1}$ because $\mathbb{CP}^{N-1}$ is a compact manifold without boundary. The entire KK spectrum is discrete from the start.

The sum over KK modes converges: the lightest mode $m_1 = 2\sqrt{N}/r_3$ is factored out, and the remainder forms a geometric series using Weyl asymptotics ($d_n \sim n^{N-2}$, $m_n \sim n^{1/(N-1)}/r_3$). The integrated bond activity is $|g_{\langle xy\rangle}|_{\mathrm{int}} \leq C_0\,e^{-2\sqrt{N}\,a/r_3}$.

**(b) The constant $C_0$.** The constant $C_0$ is explicitly bounded but depends on $N$. From Appendix I.3: $C_0 = \sum_n d_n\,e^{-(m_n - m_1)a}/(m_n a) = O(N^{N-1})$ (crude upper bound from Weyl asymptotics). This $N$-dependence is polynomial in $N$ raised to a power that itself depends on $N$, which could be concerning for large $N$. However:

1. The cluster expansion convergence requires $C_0\,e^{-m_1 a} \ll 1$. With $m_1 a = 2\sqrt{N}\,a/r_3$ and $a/r_3 \sim 10^{15}$ in the physical regime, the exponential suppression $e^{-10^{15}\sqrt{N}}$ vastly overwhelms any polynomial growth in $N$. Even $C_0 = N^{N^N}$ would be negligible against this exponential.

2. For the Clay prize, the proof is required for each fixed $N$, not uniformly in $N$. For any fixed $N$, $C_0(N)$ is a finite constant.

**Impact on the claimed result:** None. The propagator bound is standard lattice QFT, the transfer matrix is trace-class on compact spaces, and the $N$-dependence of $C_0$ is absorbed by the exponential suppression $e^{-m_1 a}$ with astronomical margin.
