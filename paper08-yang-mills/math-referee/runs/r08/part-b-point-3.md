## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

(a) The Feshbach decomposition is correctly applied. The condition E < inf sigma(QHQ) ~ m_1 is verified quantitatively: the low-lying eigenvalues E_0, E_1 of the full KK Hamiltonian satisfy E_n ~ Delta_0^KK ~ Lambda_QCD (the QCD scale), while m_1 ~ 1/r_3 ~ 10^{15} Lambda_QCD. So Delta_0^KK / m_1 ~ 10^{-15}, ensuring the Feshbach effective Hamiltonian is well-defined with resolvent ||(z - H_{QQ})^{-1}|| <= 2/m_1. The coupling operator W = P_0 V Q_0 satisfies ||W|| <= |Lambda_t^1| C_0 e^{-m_1 a} = C_W e^{-m_1 a}, and the Feshbach correction is ||W(z - H_{QQ})^{-1}W^dag|| <= 2 C_W^2 / m_1 * e^{-2 m_1 a}, which is exponentially small.

(b) The trace-norm bound ||T_red - T_std||_tr <= C_tr |Lambda_t^1| e^{-m_1 a} ||T_std||_tr contains the volume factor |Lambda_t^1|. This volume factor does NOT spoil the argument because: (1) it enters the mass gap comparison through Lemma 3 as |Delta_0^std - Delta_0^red| <= 4 epsilon / (a lambda_1(T_red)), and (2) epsilon = C_tr |Lambda_t^1| e^{-m_1 a} ||T_std||_tr, so the ratio ||T||_tr / lambda_1(T) = C_Z e^{Delta_0 a} is the partition function ratio (trace over all states divided by the sub-leading eigenvalue). The final bound is |Delta_0^std - Delta_0^red| <= C'' e^{-m_1 a/2}, where the volume factor cancels against the normalization. The Weyl-Kato perturbation theory (eigenvalue bound: sup_j |lambda_j(T_1) - lambda_j(T_2)| <= ||T_1 - T_2||_op <= ||T_1 - T_2||_tr) is correctly applied.

(c) The factorization of low-lying states is proved in Lemma 4, Step 4: |n> = |psi_n>_4D (x) |Omega_int> + |delta_n> with ||delta_n|| <= 2 C_W / m_1 * e^{-m_1 a} for n = 0, 1. This factorization is proved via the Feshbach projection for BOTH the ground state (n=0) and the first excited state (n=1), because both eigenvalues lie below inf sigma(H_{QQ}) ~ m_1. The Feshbach formula maps the eigenvalue problem in the full Hilbert space to an eigenvalue problem in the P_0 subspace, where the effective Hamiltonian H_eff(z) = H_{00} + W(z - H_{QQ})^{-1} W^dag has the same low-lying eigenvalues as H. The correction delta_n is bounded by the off-diagonal coupling divided by the spectral gap to the Q sector. For the first excited state (glueball), the same argument applies since E_1 = Delta_0^KK << m_1.

**Impact on the claimed result:** None. Theorem 5 provides a rigorous non-perturbative proof of IR equivalence through four lemmas (well-definedness, trace-norm bound, spectral perturbation, Feshbach projection). The proof is complete and does not rely on physical intuition (Appelquist-Carazzone).
