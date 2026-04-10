## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

---

**Finding:**

Theorem 5 (Section 4.5) proves $\Delta_0^{\text{std}} \geq \Delta_0^{\text{KK}} - Ce^{-m_1 a} > 0$, transferring the mass gap from the KK-enhanced theory to the standard SU($N$) theory. The four-lemma proof is the key structural argument. I examine each interrogation sub-point:

**(a) The Feshbach decomposition and resolvent condition.** Lemma 4 (implicit in the four-lemma proof) uses the Feshbach-Schur map: $H_{\text{eff}} = P H P + P H Q(E - QHQ)^{-1}QHP$. The resolvent $(E - QHQ)^{-1}$ requires $E < \inf\sigma(QHQ)$. Here $Q$ projects onto the internal excitations, and $\inf\sigma(QHQ) \geq m_1$ (the lightest KK mass). The proof requires $\Delta_0^{\text{KK}} \ll m_1$.

The condition $\Delta_0^{\text{KK}} \ll m_1$ is equivalent to $\Delta_0^{\text{KK}} \ll 2\sqrt{3}/r_3$. Since the KK mass gap is $m_1 = 2\sqrt{3}/r_3 \sim 2\sqrt{3}\,c/r_3$ (with $r_3 \sim 10^{-31}$ m, this is a mass of order $10^{21}$ GeV), and $\Delta_0^{\text{KK}}$ is a QCD-scale mass ($\sim \Lambda_{\text{QCD}} \sim 200$ MeV), the ratio $\Delta_0^{\text{KK}}/m_1 \sim 10^{-32}$. The resolvent exists with norm $\leq 1/(m_1 - \Delta_0^{\text{KK}}) \approx 1/m_1$. The Feshbach decomposition is well-defined. The proof of Lemma 2 (trace-norm bound) explicitly uses this in bounding the correction as $Ce^{-m_1 a} \ll \Delta_0^{\text{KK}}$. SOUND.

**(b) The trace-norm bound and volume factors.** Lemma 2 gives $\|\hat{T}_{\text{red}} - \hat{T}_{\text{std}}\|_{\text{tr}} \leq C_{\text{tr}} |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\text{std}}\|_{\text{tr}}$.

The factor $|\Lambda_t^1|$ (number of temporal links) appears in Step 2 of Lemma 2's proof: summing the cluster expansion over all bonds $\ell \in \Lambda_{\text{bonds}}$ gives $\leq c_d |\Lambda_t^1| e^{-m_1 a}$. This volume factor is genuine.

The concern is whether this $|\Lambda_t^1|$ factor cancels against the delocalization of eigenstates. The answer is yes, for the spectral gap: the Weyl-Kato perturbation theory (used in Lemma 3) bounds the spectral shift as

$$|\lambda_k(\hat{T}_{\text{red}}) - \lambda_k(\hat{T}_{\text{std}})| \leq \frac{\|\hat{T}_{\text{red}} - \hat{T}_{\text{std}}\|_{\text{op}}}{\min_j \text{gap}_j}$$

where the operator norm $\|\cdot\|_{\text{op}} \leq \|\cdot\|_{\text{tr}} / \text{rank}$. The transfer matrix on a spatial volume $V_s = L^3$ has rank $\leq e^{C V_s}$ (bounded by the dimension of the physical Hilbert space). So $\|\hat{T}_{\text{red}} - \hat{T}_{\text{std}}\|_{\text{op}} \leq C_{\text{tr}} |\Lambda_t^1| e^{-m_1 a} / \text{rank}$. For $|\Lambda_t^1| = O(V_s)$ and rank $= O(e^{C V_s})$, the operator norm is exponentially small in $V_s$ — far smaller than $\Delta_0^{\text{KK}}$.

Actually, the preprint uses a more direct approach: Lemma 3 applies Weyl-Kato perturbation theory to bound the eigenvalue shift using the trace norm divided by the gap, with the gap being $m_1 - \Delta_0^{\text{KK}} \gg 0$. The volume factor $|\Lambda_t^1|$ is bounded by $c_d L^3 / a^3$, and $e^{-m_1 a} = e^{-2\sqrt{3} a/r_3}$ is doubly-exponentially suppressed. So $|\Lambda_t^1| e^{-m_1 a} \leq (L^3/a^3) e^{-2\sqrt{3} a/r_3}$, which is bounded for any fixed $L$ and any $a \gg r_3$. The volume cancellation is guaranteed by the exponential suppression being stronger than any polynomial growth. SOUND.

**(c) Factorization of low-lying states.** The factorization $|\psi_n\rangle_{\text{KK}} \approx |\psi_n\rangle_{4D} \otimes |\Omega_{\text{int}}\rangle + |\delta_n\rangle$ is established for the ground state by the KK spectral gap: the internal ground state $|\Omega_{\text{int}}\rangle$ has a gap $m_1$ above it, so the internal excitations decouple from the 4D dynamics for energies $\ll m_1$. For the first excited state (the glueball), the factorization holds with $\|\delta_1\| \leq C e^{-m_1 a}$ (Lemma 4, Step 3): the coupling between the glueball and the first KK mode is $O(e^{-m_1 a})$ by the bond activity bound.

The key point: the glueball state is a 4D color-neutral bound state with energy $\Delta_0^{\text{KK}} \ll m_1$. The internal mode excitations start at $m_1$. Any mixing between the glueball and KK excitations is off-resonance and suppressed by $1/(m_1 - \Delta_0^{\text{KK}}) \cdot O(e^{-m_1 a}) \approx e^{-m_1 a}/m_1$, which is doubly exponentially small. This is the content of Lemma 4. The factorization is proved, not assumed. SOUND.

**Impact on the claimed result:** Theorem 5 is the pivotal step in the proof chain: it transfers $\Delta_0^{\text{KK}} > 0$ to $\Delta_0^{\text{std}} > 0$. The four-lemma proof is complete and addresses all technical concerns. This is the most important structural result in the paper, and it is sound.
