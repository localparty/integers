## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Transfer matrix estimate.** The bound $|g_b| \leq C_0 e^{-m_1 a}$ (Theorem 2, Section 4.3) is derived via a four-step argument:

1. The KK mode decomposition expands the internal connection in eigenmodes of $\Delta_1^H$.
2. The lattice propagator $G_n(a)$ at one-step separation admits a transfer matrix representation.
3. The bound $G_n(a) \leq (C_1/m_n a)\,e^{-m_n a}$ for $m_n a \geq 1$ follows from the lattice energy $\cosh(m_n^{\mathrm{latt}} a) = 1 + m_n^2 a^2/2$, which gives $m_n^{\mathrm{latt}} a \geq m_n a - O(\ln(m_n a))$. Standard transfer matrix estimates (Lüscher 1977, Seiler 1982).
4. The sum over KK modes converges: by Weyl's law, $d_n \sim n^{N-2}$ and $m_n \sim n/r_3$, so the polynomial growth is dominated by $e^{-(m_n - m_1)a}$ with $m_n - m_1 \geq c(n-1)/r_3$.

The transfer matrix on $\mathbb{CP}^{N-1}$ IS trace-class because $\mathbb{CP}^{N-1}$ is compact (finite-dimensional internal space, discrete spectrum with eigenvalues growing to infinity). There are no boundary corrections or finite-volume effects because $\mathbb{CP}^{N-1}$ is compact without boundary.

**(b) The constant $C_0$.** The constant $C_0$ depends on $N$ through:
- The Weyl asymptotics: $d_n \sim n^{N-2}$ (polynomial in $n$ with exponent $N-2$).
- The dimension of the adjoint representation: $\dim(\mathrm{adj}) = N^2 - 1$ (affects the number of color components).
- The propagator prefactor $C_1/(m_n a)$.

The sum $C_0 = C_4 = 2\sum_{n \geq 1} d_n C_1/(m_n a) \cdot e^{-(m_n - m_1)a}$ converges for each fixed $N$. For large $N$, the polynomial growth $d_n \sim n^{N-2}$ increases, but for the cluster expansion, only the exponential factor $e^{-m_1 a}$ with $m_1 a \sim a/r_3 \sim 10^{15}$ matters. The constant $C_0(N)$ is finite for each $N$ and enters the Kotecký-Preiss criterion only inside a logarithm (Section 4.3, convergence condition). Since $\ln C_0(N)$ is polynomial in $N$ while $m_1 a/6 \sim 10^{14}$, the $N$-dependence does not compromise the cluster expansion for any finite $N$.

**Impact on the claimed result:** None. The propagator bound is correct with controlled $N$-dependence.
