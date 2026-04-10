## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Transfer matrix estimate.**

The bound $|g_b| \leq C_0 e^{-m_1 a}$ (Theorem 2) is derived from the transfer matrix on $\mathbb{CP}^{N-1}$. The bond activity $g_{\langle xy \rangle} = e^{-V(U, A_x, A_y)} - 1$ measures the coupling between internal connections at neighboring lattice sites.

The transfer matrix on $\mathbb{CP}^{N-1}$ is trace-class because $\mathbb{CP}^{N-1}$ is compact and the spectrum of the Hodge Laplacian is discrete with eigenvalues growing as $\lambda_n \sim n^{2/(N-1)}$ (Weyl asymptotics on a $(2N-2)$-dimensional manifold). The propagator bound follows from the spectral decomposition: the lattice propagator for the $n$-th KK mode satisfies $G_n(a) \leq (C_1/m_n a) e^{-m_n a}$ for $m_n a \geq 1$ (standard estimate from Seiler 1982, Lüscher 1977). Summing over all modes:

$$|g_b| \leq \sum_{n \geq 1} d_n G_n(a) \leq C_0 e^{-m_1 a}$$

The sum converges because the degeneracies $d_n \sim n^{N-2}$ (polynomial) are overwhelmed by the exponential decay $e^{-m_n a}$ with $m_n \sim n/r_3$ and $a/r_3 \gg 1$. There are no boundary corrections on $\mathbb{CP}^{N-1}$ because it is a compact manifold without boundary. There are no finite-volume effects either — the internal space has fixed size $r_3$.

**(b) The constant $C_0$.**

$C_0$ depends on $N$ through the Weyl asymptotics: $d_n$ grows as $n^{N-2}$, so the sum $\sum_{n \geq 1} d_n e^{-(m_n - m_1)a}/m_n a$ grows with $N$. For fixed $a/r_3$ (which is $\sim 10^{15}$ in the physical regime), the $N$-dependence of $C_0$ is at most $O(N^{N-1})$ — a polynomial in $N$ for fixed $N$, but potentially large.

However, $C_0$ enters the cluster expansion only through the product $C_0 e^{-m_1 a}$, where $m_1 a = 2\sqrt{N} a/r_3 \sim 10^{15}\sqrt{N}$. The exponential suppression $e^{-10^{15}\sqrt{N}}$ is so extreme that even exponential growth in $C_0$ is utterly negligible. For any fixed $N$, $C_0(N)$ is finite, and $C_0(N) e^{-m_1 a}$ is effectively zero.

The $N$-dependence of $C_0$ is tracked in Appendix I.3 and confirmed to be harmless at each step.

**Impact on the claimed result:** None. The propagator bound is a straightforward consequence of the spectral gap and transfer matrix estimates.
