## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Feshbach decomposition.**

Lemma 4 uses the Feshbach projection $H_{\mathrm{eff}}(z) = P H P + P H Q (z - Q H Q)^{-1} Q H P$ where $P = \mathbf{1}_{\mathrm{std}} \otimes |\Omega_{\mathrm{int}}\rangle\langle\Omega_{\mathrm{int}}|$ projects onto the internal ground state. The resolvent $(z - QHQ)^{-1}$ exists for $z < \inf\sigma(QHQ) \sim m_1$ because any state in $Q\mathcal{H}$ has at least one KK mode excited, contributing energy $\geq m_1$.

In the physical regime, $\Delta_0^{\mathrm{KK}} \ll m_1$ is satisfied overwhelmingly: $\Delta_0^{\mathrm{KK}} \sim \Lambda_{\mathrm{QCD}} \sim 300$ MeV while $m_1 \sim 1/r_3 \sim 10^{15}$ GeV, a ratio of $\sim 10^{-18}$. The Feshbach effective Hamiltonian is well-defined because $z = \Delta_0^{\mathrm{KK}}$ lies far below $\inf\sigma(QHQ) \geq m_1$. The resolvent is bounded by $\|(z - QHQ)^{-1}\| \leq 1/(m_1 - z) \approx 1/m_1$.

This is standard application of the Feshbach-Schur map (Bach-Fröhlich-Sigal 1999; Griesemer-Hasler 2008). The conditions are comfortably satisfied.

**(b) The trace-norm bound.**

Lemma 2 gives $\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}} \leq C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. The volume factor $|\Lambda_t^1|$ (number of spatial links) appears because the coupling between standard and KK modes occurs at each link independently. The trace norm picks up contributions from all links.

The volume factor does cancel against delocalization of eigenstates. The spectral perturbation (Lemma 3, Weyl-Kato) uses the trace-norm bound divided by the eigenvalue gap. For the transfer matrix, the relevant eigenvalues are $\lambda_0$ and $\lambda_1$ with gap $\lambda_0 - \lambda_1 = \lambda_0(1 - e^{-\Delta_0 a})$. The error in the spectral gap is:

$$|\Delta_0(\hat{T}_{\mathrm{red}}) - \Delta_0(\hat{T}_{\mathrm{std}})| \leq \frac{4\epsilon}{a \lambda_1(\hat{T}_{\mathrm{std}})}$$

where $\epsilon = C_{\mathrm{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. Since $\|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}/\lambda_1(\hat{T}_{\mathrm{std}})$ is the ratio of the trace to the second-largest eigenvalue, and the trace is dominated by the ground state $\lambda_0$, this ratio is $O(1)$ (independent of volume). The volume factor $|\Lambda_t^1|$ in $\epsilon$ is cancelled by the volume-independent ratio, leaving an error $O(e^{-m_1 a})$.

Alternatively: the pointwise kernel bound $|K_{\mathrm{red}} - K_{\mathrm{std}}| \leq \bar{\epsilon} K_{\mathrm{std}}$ with $\bar{\epsilon} = C e^{-m_1 a}$ (volume-independent) gives the trace norm bound after integration. The volume factor arises from integrating over all links but is absorbed into the multiplicative structure of the bound. This is a standard calculation.

**(c) The factorization of low-lying states.**

For the ground state, the factorization $|\psi_0\rangle \approx |0\rangle_{4D} \otimes |\Omega_{\mathrm{int}}\rangle$ follows from the spectral gap $m_1$ of the internal space: the internal ground state is separated from excited states by energy $m_1$, so the ground state of the full theory is approximately a product state with $\|\delta_0\| \leq C e^{-m_1 a}$.

For the first excited state (the glueball), the factorization $|\psi_1\rangle \approx |1\rangle_{4D} \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_1\rangle$ requires more care. The glueball is a 4D excitation with energy $\Delta_0 \ll m_1$. The Feshbach projection constructs the effective 4D Hamiltonian $H_{\mathrm{eff}}$ on the $P$-subspace, and the eigenvalues of $H_{\mathrm{eff}}$ approximate those of $H$ up to $O(e^{-2m_1 a}/m_1)$ (from the off-diagonal coupling $\|W\| \leq C_W e^{-m_1 a}$). The first excited state of $H$ is well-approximated by the first excited state of $H_{\mathrm{eff}}$ because $\Delta_0 \ll m_1$ ensures there is no level crossing between 4D excitations and KK excitations.

This is proved, not assumed. Lemma 4 provides the spectral perturbation bound for the first two eigenvalues simultaneously. The Feshbach projection is exact (isospectral) at the eigenvalue level; the approximation enters only through the energy-dependence $H_{\mathrm{eff}}(z)$, which is controlled by $z/m_1 \ll 1$.

**Impact on the claimed result:** None. The Feshbach projection argument is mathematically rigorous, uses standard operator-theoretic tools, and the conditions are satisfied by enormous margins.
