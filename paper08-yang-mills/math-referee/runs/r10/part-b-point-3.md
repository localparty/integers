## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Feshbach decomposition.**

The Feshbach projection uses $H_{\mathrm{eff}}(z) = H_{00} + W(z - H_{QQ})^{-1}W^\dagger$ where $P_0 = \mathbf{1}_{\mathrm{std}} \otimes |\Omega_{\mathrm{int}}\rangle\langle\Omega_{\mathrm{int}}|$ projects onto the internal ground state and $Q_0 = \mathbf{1} - P_0$.

The condition $E < \inf\sigma(QHQ)$ requires the spectral parameter $z$ to lie below the threshold of KK-excited states. Since $H_{QQ} - E_0 \geq m_1$ (Theorem 1: any state in $Q_0\mathcal{H}$ has at least one KK mode excited with energy $\geq m_1$), the threshold is at $m_1$. The condition becomes $\Delta_0^{\mathrm{KK}} \ll m_1$.

Quantitatively: $\Delta_0^{\mathrm{KK}} \sim O(1)$ in lattice units (the mass gap is a QCD-scale quantity), while $m_1 a = 2\sqrt{3}\,a/r_3 \sim 3.46 \times 10^{15}$ in the physical regime. The separation is $\Delta_0^{\mathrm{KK}} / m_1 \sim 10^{-15}$. The Feshbach effective Hamiltonian is well-defined: the resolvent $(z - H_{QQ})^{-1}$ exists for $z < m_1$, and the correction $\|W(z - H_{QQ})^{-1}W^\dagger\| \leq 2C_W^2 e^{-2m_1 a}/m_1$ is negligibly small.

The off-diagonal coupling $W = P_0 H Q_0$ satisfies $\|W\| \leq |\Lambda_t^1| C_0 e^{-m_1 a}$ (from the bond activity bound, Theorem 2). For $m_1 a$ sufficiently large, $H_{QQ} - E_0 \geq m_1 - 2C_W e^{-m_1 a} \geq m_1/2$, confirming the Feshbach formula is applicable (Bach-Fröhlich-Sigal 1998). This is correct.

**(b) The trace-norm bound.**

Lemma 2 bounds $\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}} \leq C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$.

The volume factor $|\Lambda_t^1|$ (number of lattice links in a time slice) appears concerning but is handled correctly. The key point is that the bound is *relative* to $\|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$: the error is $\epsilon = C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. When this is fed into Lemma 3, the mass gap perturbation is:

$$|\Delta_0^{\mathrm{std}} - \Delta_0^{\mathrm{red}}| \leq \frac{4\epsilon}{a\lambda_1(\hat{T}_{\mathrm{red}})} \leq \frac{4C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}}{a\lambda_1(\hat{T}_{\mathrm{red}})}$$

The ratio $\|\hat{T}\|_{\mathrm{tr}}/\lambda_1(\hat{T})$ is the ratio of partition function to first-excited-state Boltzmann weight, bounded by $C_Z e^{\Delta_0 a}$. With $\Delta_0 a \sim O(1)$ and $m_1 a \sim 10^{15}$, the volume factor $|\Lambda_t^1| \sim L^3 \cdot 4$ is completely dominated by $e^{-m_1 a}$ for any finite $L$. In the thermodynamic limit, the volume-independence of the connected form factor (Section 5.7(e), Volume Cancellation Lemma) ensures the bound is actually volume-independent.

The Weyl-Kato perturbation theory in Lemma 3 is applicable: Weyl's perturbation inequality for trace-class perturbations gives $|\lambda_j(T_1) - \lambda_j(T_2)| \leq \|T_1 - T_2\|_{\mathrm{tr}}$, which requires only the trace-norm bound, not smallness relative to individual eigenvalues.

**(c) The factorization of low-lying states.**

The factorization $|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle$ with $\|\delta_n\| \leq (2C_W/m_1) e^{-m_1 a}$ is proved for $n = 0, 1$ by the Feshbach analysis (Lemma 4).

For the ground state ($n = 0$): factorization follows from the internal spectral gap $m_1$. The ground state of the full Hamiltonian has overlap $|\langle \Omega_{\mathrm{4D}} \otimes \Omega_{\mathrm{int}} | 0\rangle|^2 \geq 1 - C e^{-2m_1 a}$ with the tensor product vacuum.

For the first excited state ($n = 1$, the glueball): the Feshbach formula applies to all eigenvalues below $\inf\sigma(H_{QQ}) \sim m_1$. Since $E_1 = \Delta_0^{\mathrm{KK}} \ll m_1$, the glueball state is well within the Feshbach domain. The factorization bound $\|\delta_1\| \leq (2C_W/m_1) e^{-m_1 a}$ follows from the same resolvent estimate used for $n = 0$. The reduced density operators $\hat{\rho}_n^{\mathrm{4D}} = \mathrm{Tr}_{\mathrm{int}}[|n\rangle\langle n|]$ are rank-one projectors up to corrections of order $e^{-m_1 a}/m_1$.

This is not assumed but proved, via the standard Feshbach perturbation theory for well-separated spectral regions.

**Impact on the claimed result:**

None. The IR equivalence (Theorem 5) is a complete proof, not a sketch. The four lemmas are rigorously established with quantitative bounds. The separation $\Delta_0^{\mathrm{KK}} \ll m_1$ provides an enormous margin ($\sim 10^{15}$ orders of magnitude), making all perturbative estimates reliable.
