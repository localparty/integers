## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: Delta_0^{std} >= Delta_0^{KK} - C e^{-m_1 a} > 0, proved via the reduced transfer matrix and Feshbach projection.

**(a) The Feshbach decomposition.** Lemma 4 uses the Feshbach formula H_eff(z) = H_{00} + W(z - H_{QQ})^{-1} W^dagger, which requires z < inf sigma(Q H Q). The paper shows:

  H_{QQ} - E_0 >= m_1 - 2C_W e^{-m_1 a} >= m_1/2

for m_1 a sufficiently large. The condition Delta_0^{KK} << m_1 holds quantitatively: Delta_0^{KK} ~ Lambda_QCD ~ 200 MeV while m_1 ~ 10^{15} GeV, giving Delta_0^{KK}/m_1 ~ 10^{-13}. The resolvent (z - H_{QQ})^{-1} exists with norm bound ||(z - H_{QQ})^{-1}|| <= 2/m_1 for z < m_1/2. The Feshbach effective Hamiltonian is well-defined by enormous margin.

**(b) The trace-norm bound.** Lemma 2 gives ||T_red - T_std||_tr <= C_tr |Lambda_t^1| e^{-m_1 a} ||T_std||_tr. The volume factor |Lambda_t^1| (number of spatial links) appears.

The mass gap perturbation via Lemma 3 involves |Delta_0^{std} - Delta_0^{red}| <= 4 epsilon / (a lambda_1). Here epsilon = C_tr |Lambda_t^1| e^{-m_1 a} ||T||_tr and lambda_1 ~ ||T||_tr e^{-Delta_0 a}. The ratio ||T||_tr / lambda_1 includes a volume-dependent factor. Combining:

  |Delta Delta_0| <= C(N, L/a) e^{-m_1 a}

where C(N, L/a) is polynomial in L/a. For m_1 a ~ 10^{15}, the factor e^{-m_1 a} ~ e^{-10^{15}} is so fantastically small that no polynomial in L/a can overcome it. Even for (L/a)^{100}, the product (L/a)^{100} e^{-10^{15}} = 0 for all practical purposes. The bound is finite for any fixed lattice.

Crucially, Theorem 5 is applied at FIXED (a_0, L_0), not in a limit. The thermodynamic limit L -> infinity is taken separately (Section 5.7(e)), using the cluster decomposition property of the standard theory with Delta_0^{std} > 0. The continuum limit a -> 0 is then taken using Balaban's RG, which operates on the STANDARD theory. No step requires Theorem 5 to hold uniformly in L.

**(c) The factorization of low-lying states.** The paper proves: |n> = |psi_n>_{4D} tensor |Omega_int> + |delta_n> with ||delta_n|| <= 2C_W e^{-m_1 a}/m_1 for n = 0, 1.

For the ground state (n = 0): factorization follows from the spectral gap m_1 of the internal Hamiltonian. The ground state of H is approximately the product of the 4D ground state and the internal ground state.

For the first excited state (n = 1, the glueball): the same Feshbach argument applies because E_1 ~ Delta_0^{KK} << m_1 = inf sigma(QHQ). The Feshbach effective Hamiltonian describes ALL low-lying states (those with E < m_1/2), not just the ground state. Since E_1 << m_1, the glueball state factorizes with the same error bound.

The paper's Lemma 4 makes this explicit: the eigenvalue perturbation gives Delta_0^{red} = Delta_0^{KK} + O(e^{-2m_1 a}), with the correction coming from the off-diagonal coupling W between the P_0 and Q_0 sectors.

No error found. The Feshbach projection is a clean, well-constructed argument with conditions satisfied by enormous margins.

**Impact on the claimed result:** None. This step correctly transfers the mass gap from the KK-enhanced theory to the standard SU(N) lattice gauge theory.
