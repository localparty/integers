## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim is that the standard SU($N$) theory has $\Delta_0^{\mathrm{std}} \geq \Delta_0^{\mathrm{KK}} - Ce^{-m_1 a} > 0$, proved via the reduced transfer matrix and Feshbach projection through four lemmas.

**(a) The Feshbach decomposition.** Lemma 4 uses the Feshbach projection $H_{\mathrm{eff}}(z) = H_{00} + W(z - H_{QQ})^{-1}W^\dagger$ to compare the KK and standard spectra. The condition $z < \inf\sigma(H_{QQ})$ is verified: $\inf\sigma(H_{QQ}) \geq m_1 - 2C_W e^{-m_1 a} \geq m_1/2$ for $m_1 a$ sufficiently large, while the low-lying eigenvalues $E_n \ll m_1$ (since $\Delta_0^{\mathrm{KK}}$ is at the QCD scale while $m_1 \sim 10^{15}$ GeV). The resolvent exists and is bounded by $\|(z - H_{QQ})^{-1}\| \leq 2/m_1$. The Feshbach effective Hamiltonian is well-defined, and the off-diagonal correction $\|W(z-H_{QQ})^{-1}W^\dagger\| \leq 2C_W^2 e^{-2m_1 a}/m_1$ is negligible.

**(b) The trace-norm bound.** Lemma 2 bounds $\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}} \leq C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. The volume factor $|\Lambda_t^1|$ appears but is handled by the min-max comparison approach (Step 3 of the Theorem 5 assembly), not the trace-norm perturbation route. The paper's proof uses the **pointwise multiplicative kernel bound** $|\hat{T}_{\mathrm{red}}(U';U) - \hat{T}_{\mathrm{std}}(U';U)| \leq \bar{\epsilon} \hat{T}_{\mathrm{std}}(U';U)$ with $\bar{\epsilon} = 2C_1 |\Lambda_t^1| e^{-m_1 a}$, which gives the operator inequality $(1-\bar{\epsilon})\hat{T}_{\mathrm{std}} \leq \hat{T}_{\mathrm{red}} \leq (1+\bar{\epsilon})\hat{T}_{\mathrm{std}}$. The min-max principle then controls eigenvalue ratios without requiring delocalization cancellation. The resulting mass gap comparison $|\Delta_0^{\mathrm{std}} - \Delta_0^{\mathrm{red}}| \leq 4\bar{\epsilon}/a \leq C'' e^{-m_1 a/2}$ is free of the trace-norm volume factor because the polynomial $|\Lambda_t^1|$ is negligible compared to $e^{m_1 a/2}$ ($m_1 a \sim 10^{15}$). This is correct.

**(c) The factorization of low-lying states.** Lemma 4, Step 4 establishes $|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle$ with $\|\delta_n\| \leq 2C_W e^{-m_1 a}/m_1$ for $n = 0, 1$. For the ground state, the factorization follows from the spectral gap $m_1$ of the internal Hamiltonian (any state with a KK excitation has energy $\geq m_1$ above the ground state). For the first excited state (the glueball), the same argument applies: the glueball at energy $\hat{\Delta}_k \ll m_1$ couples to KK-excited states through $W = P_0 \hat{V} Q_0$ with $\|W\| \leq C_W e^{-m_1 a}$, and perturbation theory gives $\|\delta_1\|$ of the same order. The factorization is proved (not assumed) via the Feshbach projection, with error controlled by $\|W\|/m_1 \sim e^{-m_1 a}/m_1$.

The assembly of Theorem 5 is clean: Lemma 4 gives $\Delta_0^{\mathrm{red}} = \Delta_0^{\mathrm{KK}} + O(e^{-2m_1 a})$, and the min-max comparison (Steps 3-4) gives $|\Delta_0^{\mathrm{std}} - \Delta_0^{\mathrm{red}}| \leq C'' e^{-m_1 a/2}$. Since $\Delta_0^{\mathrm{KK}} > 0$ (Theorem 4) and the corrections are exponentially small, $\Delta_0^{\mathrm{std}} > 0$.

**Impact on the claimed result:**
No impact. The IR equivalence argument is rigorous and successfully transfers the KK mass gap to the standard Yang–Mills theory. The Feshbach projection is a well-established technique (Bach–Fröhlich–Sigal 1998) applied correctly here.
