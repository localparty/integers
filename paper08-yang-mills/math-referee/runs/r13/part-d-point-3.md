## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: for dev(O) >= p, |<1|O|1>_c| <= C_p M hat{Delta}^p, with C_p independent of k, g_k, and the volume.

**(a) The deviation extraction (Step 1).** The proof extracts p factors (e^{E_m - E_{n_j}} - 1) from the spectral weight. For m = 1 (one-particle state):

- n_j = 1 (diagonal): factor = 0 (exact vanishing)
- n_j = 0 (vacuum): |e^{hat{Delta}} - 1| <= C_* hat{Delta} where C_* = e^{hat{Delta}_max} is k-independent (since hat{Delta}_k is bounded on the AF trajectory: hat{Delta}_k = a_k Delta_k with Delta_k bounded and a_k -> 0 gives hat{Delta}_k -> 0; at the starting scale hat{Delta}_0 ~ O(1))
- n_j >= 2 (multi-particle): |e^{E_1 - E_{n_j}} - 1| <= 1 (not O(hat{Delta}))

The proof claims that at least p of the extracted factors are O(hat{Delta}). This is ensured by the DEFINITION of dev >= p: the factorization involves p factors where each factor is (e^{E_m - E_{n_sigma(j)}} - 1). For the diagonal channel (n_j = m), these factors vanish. For the near-vacuum channel (n_j = 0), each gives O(hat{Delta}). The multi-particle channels (n_j >= 2) give O(1) factors but are suppressed by the Boltzmann weight e^{-(E_{n_j} - E_1)}.

The total bound: each spectral channel contributes at most |tilde{W}| (C_* hat{Delta})^{p_near} 1^{p_far} e^{-Sum(E_{n_j} - E_1)}, where p_near + p_far >= p. The sum over channels gives the zeta bound (Step 3). For the connected matrix element, the diagonal channel (all n_j = 1) vanishes, and the surviving channels have at least one deviation factor O(hat{Delta}). For a two-derivative operator (p = 2), the two deviation factors both come from the two-derivative structure, giving (hat{Delta})^2.

**(b) The zeta bound and two-particle threshold.** zeta = Sum_{n >= 1} e^{-(E_n - E_1)} requires E_2 - E_1 > 0.

The two-particle threshold bound: E_2 - E_1 >= hat{Delta}_k(1 - 2 C_B g_k^4) >= hat{Delta}_k / 2. This uses:

**Perturbative part:** Kato-Rellich perturbation theory in the small-field domain. The interaction V_k is relatively bounded: ||V_k|| / (2 hat{Delta}_k) <= C g_k^2 / (2 hat{Delta}_k) << 1 on the AF trajectory. The binding energy: epsilon_B^{pert} <= C_B g_k^4 hat{Delta}_k.

**Non-perturbative part:** Large-field correction epsilon_B^{lf} <= C' e^{-c/g_k^{1/2}}, which is negligible compared to g_k^4 hat{Delta}_k on the AF trajectory.

Could a deeply bound two-glueball state exist at some RG step? In the small-field domain, the Kato-Rellich theorem with relative bound << 1 prevents the spectrum from shifting by more than ||V_k|| ~ C g_k^4. A bound state at energy E_2 < E_1 would require ||V_k|| > hat{Delta}_k, which is impossible when g_k^4 << hat{Delta}_k/C (satisfied on the AF trajectory for k sufficiently large). For the first few steps (k small), the cluster expansion provides direct control.

**(c) Volume independence via Combes-Thomas.** The Combes-Thomas estimate requires the operator hat{A}^{(s)} to be local with support radius R_0.

Is R_0 bounded uniformly in k? Yes. Balaban's polymer activities K_k(X) have |K_k(X)| <= e^{-kappa|X|} with kappa > 0 k-independent. The effective support radius is R_0 = O(1/kappa) lattice spacings at scale k. In physical units, this is R_0 a_k = O(a_k/kappa). Since kappa is k-independent, R_0 (in lattice units) is k-independent.

The Combes-Thomas bound gives exponential suppression of contributions from distant regions: the sum over states decomposes into a local part (within distance R_0) and a tail exponentially suppressed by e^{-m|x|} (where m is the mass gap). The local part is bounded by a constant depending on R_0 and N but independent of the volume. Therefore zeta <= C(R_0, N) is volume-independent and k-independent.

No error found. The spectral lemma is a clean application of transfer matrix spectral theory with well-controlled bounds.

**Impact on the claimed result:** None. The spectral lemma correctly converts dev >= 2 into the quantitative bound C_new g_k^4 hat{Delta}^2.
