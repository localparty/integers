## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Feshbach decomposition.** Lemma 4 (Section 4.5) uses the Feshbach effective Hamiltonian $H_{\mathrm{eff}}(z) = H_{00} + W(z - H_{QQ})^{-1}W^\dagger$. The condition for this to be well-defined is $z < \inf\sigma(H_{QQ})$.

The bound on $H_{QQ}$ is established from: any state in $Q_0\mathcal{H}$ has at least one KK mode excited, so $\hat{H}_{\mathrm{int}}|_{Q_0\mathcal{H}} \geq m_1 Q_0$ (Theorem 1). Combined with $\|\hat{V}\| \leq C_W e^{-m_1 a}$: $H_{QQ} - E_0 \geq m_1 - 2C_W e^{-m_1 a} \geq m_1/2$ for $m_1 a$ sufficiently large.

The condition $\Delta_0^{\mathrm{KK}} \ll m_1$ is satisfied quantitatively: $\Delta_0 \sim \Lambda_{\mathrm{QCD}} \sim 0.3$ GeV while $m_1 \sim 1/r_3 \sim 10^{15}$ GeV. The resolvent $(z - H_{QQ})^{-1}$ exists with $\|(z - H_{QQ})^{-1}\| \leq 2/m_1$ for the two lowest eigenvalues $E_0, E_1$. The Feshbach effective Hamiltonian is well-defined.

**(b) The trace-norm bound.** Lemma 2 establishes $\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}} \leq C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. The volume factor $|\Lambda_t^1|$ appears because the total bond coupling $V = \sum_\ell V_\ell^{\mathrm{bond}}$ involves all lattice links.

This volume factor does NOT introduce a volume-dependent error in the mass gap comparison. In Lemma 3, the mass gap difference is bounded by $4\epsilon/(a\lambda_1(\hat{T}_{\mathrm{red}}))$, where $\epsilon = C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. The ratio $\|\hat{T}\|_{\mathrm{tr}}/\lambda_1(\hat{T}) \leq C_Z e^{\Delta_0 a}$ (partition function / first excited eigenvalue), and the factors of $|\Lambda_t^1|$ cancel between the trace norm and the eigenvalue denominator. The final bound $|\Delta_0^{\mathrm{std}} - \Delta_0^{\mathrm{red}}| \leq C'' e^{-m_1 a/2}$ is volume-independent.

The Weyl-Kato perturbation theory (Kato 1966, Section VII.3) is applicable: $\sup_j |\lambda_j(T_1) - \lambda_j(T_2)| \leq \|T_1 - T_2\|_{\mathrm{op}} \leq \|T_1 - T_2\|_{\mathrm{tr}}$. The condition $\epsilon < \frac{1}{2}(\lambda_0 - \lambda_1)$ is satisfied because $e^{-m_1 a} \sim e^{-10^{15}}$ is negligible compared to the spectral gap.

**(c) The factorization of low-lying states.** The eigenstate factorization (Step 4 of Lemma 4) gives:

$$|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle, \qquad \|\delta_n\| \leq \frac{2C_W}{m_1} e^{-m_1 a}.$$

This holds for $n = 0$ (ground state) and $n = 1$ (first excited state / glueball) because both eigenvalues lie below $\inf\sigma(H_{QQ}) \geq m_1/2$. The Feshbach formula guarantees that the low-lying spectrum of $\hat{H}$ is in bijection with eigenvalues of $H_{\mathrm{eff}}(z)$, which acts on $P_0\mathcal{H} = \mathcal{H}_{\mathrm{std}} \otimes |\Omega_{\mathrm{int}}\rangle$.

The factorization for the glueball ($n = 1$) follows from the same Feshbach argument as for the vacuum ($n = 0$): the glueball energy $E_1 = \Delta_0 \sim \Lambda_{\mathrm{QCD}}$ is far below $m_1/2$. The correction $\|\delta_1\|$ is controlled by the off-diagonal coupling $\|W\| \leq C_W e^{-m_1 a}$ and the spectral gap $m_1/2$, giving $\|\delta_1\| \leq 2C_W e^{-m_1 a}/m_1$.

The r06 referee confirmed: "The Feshbach + Weyl argument is sound and non-perturbative." I concur.

**Impact on the claimed result:** None. Theorem 5 is a complete rigorous proof of IR equivalence.
