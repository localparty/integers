## Part A, Point 2: The KK Propagator Bound

**Weight:** LIGHT
**Verdict:** SOUND (with the same N-dependence caveat as A1)

**Finding:**

(a) **Transfer matrix estimate.** Section 04.3 ("Theorem 2") proves the bond activity bound by combining the lattice propagator on $\mathbb{CP}^{N-1}$ with the transfer matrix estimate $G_n(a) \leq (C_1/(m_n a)) e^{-m_n^{\mathrm{latt}} a}$, with the lattice dispersion $\cosh(m^{\mathrm{latt}} a) = 1 + m^2 a^2/2$. For $m_n a \gg 1$, $m_n^{\mathrm{latt}} a \to m_n a + O(\ln(m_n a))$, giving the claimed exponential decay with a logarithmic prefactor. This is a standard Lüscher/Seiler estimate and is correct.

A subtlety: for *very heavy* KK modes, $m_n^{\mathrm{latt}} a$ saturates at $\sim \ln(m_n^2 a^2)$, giving polynomial (not exponential) decay $G_n(a) \sim 1/(m_n a)^2$. The preprint addresses this in the "Heavy modes and lattice dispersion" remark and shows that the polynomial bound suffices because $\sum_n d_n/(m_n a)^2 \leq C(N) r_3^2/a^2$, which is small compared to $e^{-m_1 a}$ in the physical regime $a \gg r_3$. Sound.

The "trace-class" question (whether the transfer matrix is well-defined as a Hilbert-space operator) is handled implicitly: the path integral is over compact group variables and a Gaussian internal sector, both of which give a positive bounded transfer matrix. Section 4.5 Lemma 1 then proves trace-class membership of the *reduced* transfer matrix.

(b) **The constant $C_0$ and N-dependence.** Theorem 2 line 558–562 writes
$$|g_b|_{\mathrm{integrated}} \leq C_0 e^{-m_1 a} = C_0 e^{-2\sqrt{N}\,a/r_3}$$
with "$m_1 = 2\sqrt{N}/r_3$ from Theorem 1 ($\lambda_1^{(1)} = 4N/r_3^2$)". This *contradicts* the value $2\sqrt{3}/r_3$ used everywhere else (abstract, Theorem 4, Theorem 5). The bound itself is fine — the $N$-dependent version is the correct one — but the proof should standardize on the $N$-dependent expression rather than silently substituting $N = 3$ in some places and $\sqrt{N}$ in others.

The constant $C_0$ comes from the Weyl mode-counting sum
$$\sum_{n \geq 1} d_n e^{-(m_n - m_1)a}/m_n a$$
with $d_n \sim n^{N-2}$. The preprint notes (correctly) that $C_0$ grows polynomially in $N$ but is absorbed by the exponential factor $e^{-m_1 a}$ at $a/r_3 \sim 10^{15}$. Concretely, for the cluster expansion threshold $\beta < m_1 a/6 - \ln(c_d K C_0^{1/6})$, the $\ln C_0$ correction is $O(N \ln N)$, far smaller than $m_1 a/6 \sim \sqrt{N} \cdot 10^{14}$.

(c) **Boundary corrections on $\mathbb{CP}^{N-1}$.** None: $\mathbb{CP}^{N-1}$ is closed (no boundary). Finite-volume effects on the spatial 4D lattice $\Lambda_L$ are bounded by $e^{-m L}$ (Section 5.7(e), volume-cancellation lemma), which is exponentially small for $L \gg 1/\Delta_\infty$. Sound.

**Impact on the claimed result:** None directly. The notation inconsistency between "$2\sqrt{3}$" and "$2\sqrt{N}$" should be cleaned up (this is the same issue as A1), but the propagator bound itself stands.
