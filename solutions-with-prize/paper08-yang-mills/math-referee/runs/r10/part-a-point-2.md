## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Transfer matrix estimate.**

The bound $|g_b| \leq C_0 e^{-2\sqrt{3}\,a/r_3}$ is derived via a standard transfer matrix argument on the lattice. The derivation in Section 4 (Theorem 2) proceeds in four steps:

1. The lattice propagator for KK mode $n$ admits a transfer matrix representation with lattice energy $\cosh(m_n^{\mathrm{latt}} a) = 1 + m_n^2 a^2/2$.

2. For nearest neighbors at separation $a$: $G_n(a) = \langle 0|\hat{\phi}_n e^{-aH_n}\hat{\phi}_n^\dagger|0\rangle \leq \|\hat{\phi}_n\|^2 e^{-m_n^{\mathrm{latt}} a}$.

3. For $m_n a \geq 1$, the lattice energy satisfies $m_n^{\mathrm{latt}} a \geq m_n a - O(\ln(m_n a))$, giving $G_n(a) \leq (C_1/(m_n a))\,e^{-m_n a}$.

4. Summing over KK modes with degeneracies $d_n \sim n^{N-2}$ (Weyl asymptotics) and masses $m_n \sim n/r_3$ (growing linearly), the sum $\sum_{n \geq 1} d_n e^{-(m_n - m_1)a}$ converges because the polynomial factor $d_n$ is dominated by the exponential $e^{-c(n-1)a/r_3}$. The total is bounded by $C_0 e^{-m_1 a}$.

The transfer matrix on $\mathbb{CP}^{N-1}$ is trace-class because $\mathbb{CP}^{N-1}$ is compact and the spectrum is discrete with eigenvalues growing as $\lambda_n \sim n^{2/(N-1)}$. The Weyl asymptotics ensure the heat kernel trace $\sum_n e^{-t\lambda_n}$ converges for all $t > 0$.

There are no boundary corrections on $\mathbb{CP}^{N-1}$ because it is a closed manifold (compact without boundary). Finite-volume effects arise only on the 4D lattice (spatial periodicity $L$), not on the internal space, which is fixed at radius $r_3$.

The propagator bound follows from standard estimates (Lüscher 1977, Seiler 1982 Ch. 4). The argument is rigorous.

**(b) The constant $C_0$.**

$C_0$ is bounded (not computed explicitly) and depends on $N$ through:
- The Weyl asymptotics: degeneracy $d_n \sim n^{N-2}$ of KK modes on $\mathbb{CP}^{N-1}$ ($\dim_{\mathbb{R}} = 2N-2$)
- The dimension of the adjoint representation: $\dim(\mathrm{ad}) = N^2 - 1$

$C_0$ does not depend on $\beta$, $a/r_3$, or the lattice size $L$.

The concern that an $N$-dependent $C_0$ growing faster than the exponential decay $e^{-m_1 a}$ could compromise the cluster expansion is addressed in Appendix I.3 (N-dependence tracking). The relevant quantity is $\ln C_0$, which enters the convergence criterion as $\beta_{\max} = m_1 a/6 - \ln(c_d K C_0^{1/6})$. Even with $C_0 = O(N^{N-1})$ (worst case from Weyl sum), $\ln C_0 = O(N \ln N)$, while $m_1 a/6 = O(a/(r_3 \sqrt{N})) \sim 10^{14}/\sqrt{N}$. For any fixed $N$, the exponential suppression overwhelms the polynomial $N$-dependence of $C_0$. The cluster expansion converges with enormous margin.

**Impact on the claimed result:**

None. The propagator bound is correctly derived with standard methods. The $N$-dependence of $C_0$ does not compromise the proof for any fixed $N \geq 2$.
