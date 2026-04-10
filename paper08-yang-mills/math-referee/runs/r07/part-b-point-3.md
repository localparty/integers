## Part B3, Point 3: IR Equivalence / Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

(a) *Feshbach decomposition validity.* The Feshbach (Schur complement) projection decomposes the Hilbert space into P (low-energy, pure gauge) and Q (KK-excited) sectors and requires that the energy of interest E satisfies E < inf sigma(QHQ), where QHQ is the Hamiltonian restricted to the Q-sector. The lowest eigenvalue of QHQ is of order m_1, the first KK mass. The target energy scale is Delta_0^{KK} ~ Lambda_QCD. Since m_1 ~ 10^{15} Lambda_QCD, the condition E < inf sigma(QHQ) is satisfied by fifteen orders of magnitude. This margin is not merely comfortable -- it renders the Feshbach projection essentially exact, with corrections that are non-perturbatively small.

(b) *Trace-norm bound and volume factor.* The error in the Feshbach projection carries a volume factor |Lambda_t^1| (the number of sites in the spatial lattice at the relevant scale). The full error bound is

    epsilon = C |Lambda_t^1| e^{-m_1 a}

The volume factor |Lambda_t^1| grows polynomially (as a power of 1/a), but the exponential suppression e^{-m_1 a} with m_1 a ~ 10^{15} overwhelms any polynomial volume factor. Even for astronomically large lattices, epsilon remains negligible (e^{-10^{15}} multiplied by any physically relevant volume is still effectively zero). The Weyl-Kato perturbation theorem then applies because epsilon is vastly smaller than the spectral gap Delta_0^{KK}, ensuring that the eigenvalue shift from the Feshbach correction does not close the gap.

(c) *Factorization of low-lying states.* Lemma 4 of the Feshbach projection section proves that the n = 0 (vacuum) and n = 1 (first excited / glueball) states of the full KK theory factorize as

    |psi_n^{KK}> = |psi_n^{SU(N)}> tensor |0_{KK}> + |delta_n>

where the remainder satisfies ||delta_n|| <= 2 C_W e^{-m_1 a} / m_1. For the ground state (n = 0), this is the standard Feshbach ground-state projection. For the first excited state (n = 1, the glueball), the Feshbach formula applies because the glueball energy E_1 is of order Lambda_QCD, which lies well below inf sigma(QHQ) ~ m_1. The glueball is deep in the P-sector and its KK admixture is exponentially suppressed.

The proof proceeds through four lemmas and a five-step assembly:
- Lemma 1 establishes the block decomposition of H into PP, PQ, QP, QQ sectors.
- Lemma 2 bounds the off-diagonal coupling ||PH_int Q|| using the KK propagator decay.
- Lemma 3 constructs the effective Hamiltonian H_eff = PHP - PHQ (QHQ - E)^{-1} QHP and bounds its distance from H_{SU(N)}.
- Lemma 4 proves the state factorization and remainder bound.
- The five-step assembly chains these lemmas to conclude that Delta_0^{KK} = Delta_0^{SU(N)} + O(e^{-m_1 a}).

This structure was reviewed in the previous round (referee r05, Point 4) and found sound. The current version is a clean rewrite that makes each step explicit. No new issues have been introduced.

**Impact on the claimed result:**

None. The Feshbach projection is the bridge between the KK-enhanced theory (where the mass gap is proved) and standard SU(N) Yang-Mills (where the mass gap is claimed). The projection is valid because the KK scale m_1 is astronomically larger than the QCD scale, making the effective theory correction non-perturbatively small. The four-lemma structure is complete and each bound is verified. This section is mathematically sound and the transfer of the mass gap from the KK theory to SU(N) Yang-Mills is established.
