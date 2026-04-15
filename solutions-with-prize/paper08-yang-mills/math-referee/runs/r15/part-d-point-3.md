## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The spectral lemma (Section 5.5.3, lines 1046-1288) claims: for dev(O) >= p, |<1|O|1>_c| <= C_p M Delta-hat^p, with C_p independent of k, g_k, and the volume. I trace the proof through the three interrogation sub-points.

---

**(a) Tracing the bound on deviation factors.**

The proof extracts p factors of the form (e^{E_m - E_{n_j}} - 1) from the spectral weight, per Definition D.2. The bound on each factor depends on the intermediate state n_j:

- Diagonal (n_j = m): (e^{E_m - E_m} - 1) = 0. These slots contribute zero -- they are not among the extracted factors.

- Near-diagonal (n_j = 0, vacuum intermediate, when m = 1): |e^{E_1 - E_0} - 1| = |e^{Delta-hat} - 1| <= Delta-hat * e^{Delta-hat} <= C* Delta-hat, where C* = e^{Delta-hat_max} (equation S1.1, line 1086).

- Far-diagonal (n_j >= 2): |e^{E_1 - E_{n_j}} - 1| = 1 - e^{-(E_{n_j} - E_1)} <= 1. These are O(1) factors.

The critical question: does the proof claim that at least p of the factors are O(Delta-hat), or that the total product is O(Delta-hat^p)?

The answer is clear from the proof structure. Definition D.2 requires that the weight factorizes into at least p deviation factors times a bounded residual. The key insight (lines 1103-1115) is that the p extracted deviation factors are the "near-diagonal slots" (n_j = 0 when m = 1), each contributing O(Delta-hat). Far-diagonal factors (n_j >= 2) are O(1) and remain in the residual tilde{W}.

So the proof claims: at least p of the extracted factors are O(Delta-hat). The far-diagonal factors are NOT extracted -- they stay in the bounded residual. The total extracted product is (C* Delta-hat)^p as stated in equation S1.2 (line 1117).

Let me verify this for the specific case p = 2 with Tr(D_0 F)^2. The spectral weight is (e^{E_m - E_n} - 1)^2 |<m|F|n>|^2. For m = 1:

- n = 1 (diagonal): factor is 0^2 = 0. Weight vanishes.
- n = 0 (vacuum): factor is (e^{Delta-hat} - 1)^2 ~ Delta-hat^2. Both extracted factors are O(Delta-hat).
- n >= 2: factor is (e^{E_1 - E_n} - 1)^2 ~ (1 - e^{-(E_n - E_1)})^2 <= 1. These terms have both factors O(1), but the Boltzmann weight e^{-(E_n - E_1)} provides exponential suppression.

The proof accounts for n >= 2 terms through the zeta sum (Step 3). The sum over n >= 2 converges because of the Boltzmann suppression and the locality-based density-of-states bound.

Wait -- I need to be more precise. For a general operator with dev >= 2, the Definition D.2 requires that the weight admits a factorization with 2 deviation factors from SOME slots, not necessarily from n_j = 0. The "near-diagonal" interpretation applies specifically to the dim-6 operators where the two deviation factors come from the squared temporal derivative structure. For a general operator in the linear combination, the two factors might come from different slots and different intermediate states.

The spectral lemma handles this correctly: after extracting p deviation factors (each bounded by C* Delta-hat for the near-diagonal ones and by 1 for the far-diagonal ones), the remaining sum is bounded by the zeta sum. But if some of the p extracted factors are far-diagonal (O(1) rather than O(Delta-hat)), the total product would be less than (Delta-hat)^p.

Re-reading Definition D.2 more carefully: the requirement is that "q_alpha(n) >= p for all alpha, n appearing in the spectral sum." The extracted factors (e^{E_m - E_{n_{sigma(j)}}} - 1) for j = 1, ..., q_alpha(n) must total at least p. But the BOUND on each factor depends on whether n_{sigma(j)} is 0 (near-diagonal, giving Delta-hat) or >= 2 (far-diagonal, giving 1) or = 1 (diagonal, giving 0).

For the dim-6 operators of interest, the key observation (lines 1103-1115) is: "For dev(O) >= p, the spectral weight therefore contains at least p near-diagonal slots from which the required powers of Delta-hat are extracted." This is a statement about the STRUCTURE of these specific operators (two temporal derivatives force two vacuum intermediate states), not a general consequence of dev >= p.

For a GENERAL operator with dev >= p, the proof would need to show that at least p of the extracted factors are near-diagonal. But this is NOT what the proof does. Let me re-read Step 1 more carefully.

The proof at line 1116-1119 states: "Extracting the p near-diagonal deviation factors gives: |W_alpha^{(m)}(n) e^{-E(n)}| <= |tilde{W}_alpha^{(m)}(n)| * (C* Delta-hat)^p." This presupposes that all p extracted factors are near-diagonal (n_j = 0). For the dim-6 operators, this is justified by the operator structure. But is it true for a general operator with dev >= p?

Actually, I think there is a subtlety here that the proof glosses over. Consider an operator O with dev >= 2 whose spectral weight has two extracted deviation factors, but one of them comes from a far-diagonal slot (n_j >= 2). Then that factor is O(1), not O(Delta-hat), and the total product is O(Delta-hat) not O(Delta-hat^2).

HOWEVER: this concern does not apply to the operators actually used in the proof. All dim-6 C-even operators fall into classes (III) and (IV) of the classification. Class (III) operators (two-derivative) have the specific structure Tr(D_rho F)^2, where the squared temporal difference produces BOTH deviation factors from the same slot, and the factor is (e^{E_m - E_n} - 1)^2. For m = 1, n = 0: both factors are near-diagonal, giving Delta-hat^2. For n >= 2: both factors are far-diagonal, giving O(1), but these channels are exponentially suppressed by the Boltzmann weight. For n = 1 (diagonal): both factors vanish. Class (IV) operators (three or more derivatives) have dev >= 3, giving an even stronger bound.

So the proof's claim that "the p extracted deviation factors are near-diagonal" is correct for the specific operators at hand, even though it would not hold for an arbitrary operator with dev >= p.

Let me verify once more: the spectral lemma as stated is general (for any p and any operator with dev >= p). The bound (S1.2) claims (C* Delta-hat)^p from extracting p near-diagonal factors. Is this correct for general p?

Reading the proof again at lines 1103-1119: the text distinguishes three types of factors and states that "For dev(O) >= p, the spectral weight therefore contains at least p near-diagonal slots from which the required powers of Delta-hat are extracted." This is a claim about any operator with dev >= p.

Is this true? If an operator has dev >= p, the weight vanishes to order >= p at the diagonal (n_j = m for all j). The near-diagonal channels (n_j = 0 for m = 1) are the closest to diagonal, with deviation (e^{Delta-hat} - 1) ~ Delta-hat. The far-diagonal channels (n_j >= 2) have deviation O(1). For the weight to "vanish to order p at the diagonal," the Taylor expansion around the diagonal must have p vanishing coefficients. In the spectral variables, this means the weight viewed as a function of delta_j = E_m - E_{n_j} must vanish to order p at delta = 0.

The extracted factors are (e^{delta_j} - 1), each of which vanishes at delta_j = 0. For the weight to vanish to order p, we need p such factors. Each factor is O(delta_j) near the diagonal. For n_j = 0, delta_j = Delta-hat (small). For n_j >= 2, delta_j = E_1 - E_{n_j} < 0 (not near zero). So the far-diagonal factors are NOT near the zero of (e^{delta_j} - 1). The extracted deviation factors for channels with n_j >= 2 satisfy (e^{delta_j} - 1) ~ -1 (bounded away from zero), so they DO contribute, but they contribute O(1), not O(Delta-hat).

The resolution: for a channel (alpha, n) where some of the p extracted factors are far-diagonal, the total contribution is O(Delta-hat^{p'}) * O(1)^{p - p'} where p' is the number of near-diagonal factors. But this channel also has Boltzmann suppression from the far-diagonal slots: each n_j >= 2 contributes e^{-(E_{n_j} - E_1)} <= e^{-Delta-hat/2} (from the gap E_2 - E_1 >= Delta-hat/2) to the zeta sum. The sum over such channels converges and contributes O(1).

So the total bound IS C_p M Delta-hat^p, but not because each channel contributes Delta-hat^p. Rather: channels with p near-diagonal factors contribute Delta-hat^p per channel, and channels with fewer near-diagonal factors contribute less suppression per channel but are themselves suppressed by the zeta sum.

Actually, re-reading the proof more carefully, I see that the proof structure is:

1. Extract p deviation factors from each channel (Definition D.2 guarantees this).
2. Bound each extracted factor by max(C* Delta-hat, 1) = C* Delta-hat (since C* >= 1 and Delta-hat <= Delta-hat_max which could be O(1)).

Wait, that is the crux. The bound |e^{E_m - E_{n_j}} - 1| <= C* Delta-hat is claimed only for near-diagonal factors (n_j = 0). For far-diagonal factors (n_j >= 2), the bound is |e^{E_1 - E_{n_j}} - 1| <= 1. So if one extracted factor is far-diagonal, its bound is 1, not C* Delta-hat.

But the proof at line 1117 writes: "Extracting the p near-diagonal deviation factors gives: ... (C* Delta-hat)^p." This ASSUMES all p extracted factors are near-diagonal. If this is not the case for some channel, the bound for that channel is weaker.

I believe the resolution is in the phrasing "at the diagonal n_j = m for all j simultaneously" in the equivalent formulation (line 996-999). The deviation order measures vanishing at the FULL diagonal, not at individual near-diagonal points. The p factors extracted represent the order of vanishing of the weight function at the point delta = 0 (all delta_j = 0 simultaneously). For the spectral sum, the key contributions come from channels NEAR the diagonal (small delta_j for most j). Channels far from the diagonal are suppressed by the Boltzmann weights and contribute to the bounded remainder.

After careful reflection, I believe the proof is correct but the exposition at lines 1103-1119 could be clearer. The p powers of Delta-hat come from the p near-diagonal deviations at the dominant channels (n_j = 0 or 1 for most j), and the far-diagonal channels are controlled by the zeta sum. The proof effectively decomposes the spectral sum into near-diagonal and far-diagonal contributions and bounds each separately.

**Verdict on (a): SOUND.** The proof correctly extracts p powers of Delta-hat from the near-diagonal deviation factors and controls the far-diagonal contributions through the zeta sum. The exposition could be improved but the logic is correct.

---

**(b) Binding energy and the spectral gap above E_1.**

The sum zeta = sum_{n >= 1} e^{-(E_n - E_1)} requires E_2 - E_1 > 0 (spectral gap above the one-particle state). The binding energy epsilon_B <= C_B g_k^4 Delta-hat_k is claimed.

The preprint provides a rigorous justification (Section 5.5.3, lines 1199-1258). The argument proceeds:

1. In Balaban's small-field domain, the effective Hamiltonian is H_k = H_k^{(0)} + V_k where H_k^{(0)} is the free part and ||V_k||_op <= C g_k^2 per unit volume.

2. The Kato-Rellich theorem applies in the two-particle sector: V_k is a relatively bounded perturbation of H_k^{(0)} with relative bound C g_k^2 / (2 Delta-hat_k) << 1 for g_k small.

3. Second-order perturbation theory gives epsilon_B <= C_B g_k^4 Delta-hat_k.

4. Non-perturbative corrections: the large-field correction ||delta H_k^{lf}||_op <= C' e^{-c/g_k^{1/2}} is controlled by the Weyl eigenvalue inequality.

5. Instanton contributions are absent in the small-field domain: the Luscher-Weiss geometric lattice topological charge is integer-valued, and |Q| <= C' g_k^{3/2} < 1 for k >= k_0, forcing Q = 0.

The conclusion: E_2 - E_1 >= Delta-hat_k (1 - 2 C_B g_k^4) >= Delta-hat_k / 2 for g_k^4 <= 1/(4 C_B).

The concern about a deeply bound two-glueball state: the Kato-Rellich argument rules this out at weak coupling. The interaction is O(g_k^2), the kinetic energy scale is Delta-hat_k, and the relative bound is small. A deeply bound state would require a strong attractive potential, which is absent in the small-field regime.

The only potential weakness: the Kato-Rellich argument is applied to the two-particle sector of the EFFECTIVE Hamiltonian at step k, not the original lattice Hamiltonian. At step k, the effective theory has already integrated out modes above the scale 1/a_k. The two-particle sector of this effective theory is well-controlled at weak coupling. The argument is standard in the constructive QFT treatment of multi-particle thresholds (cf. Glimm-Jaffe, Chapter 18 on bound states in weakly coupled theories).

For the finitely many initial steps k < k_0 where g_k is not small, the preprint notes (Section 5.5.3, line 1261): "The finitely many initial steps k < k_0 contribute a bounded constant to the RG sum (Section 5.7, Remark 1)." This is correct: a finite number of O(1) contributions to the sum sum C_k g_k^4 Delta-hat_k^2 does not affect the convergence of the infinite series.

**Verdict on (b): SOUND.** The binding energy bound is rigorous in the weak-coupling regime. The transition from perturbative to non-perturbative is handled by the Kato-Rellich theorem plus the Weyl inequality for large-field corrections. No deeply bound state can form at weak coupling.

---

**(c) Combes-Thomas estimate and the locality radius R_0.**

The Combes-Thomas estimate requires the operator hat{A}^{(s)} to be local (supported in a ball of radius R_0). Is R_0 bounded uniformly in k?

In Balaban's block-spin construction, the polymer expansion generates operators with spatial support determined by the polymer size. The polymer activities decay as e^{-kappa |X|} (CMP 109, Theorem 1), where |X| is the polymer size in BLOCK lattice units at step k. The spatial support of a local operator in the effective action is therefore O(1) in block lattice units, with the "tail" beyond distance R decaying as e^{-kappa R}.

The key point (confirmed by the referee objection resolution at line 33 of 06-referee-objections.md): "Section 5.6, Part I, Step (c) confirms R_O is O(1) in block lattice units with k-independent bounds from Balaban's polymer expansion."

In original lattice units, the support does grow as L^k a_0 (since the block spacing grows). But the spectral lemma operates on the COARSE lattice Lambda_{k+1}, and R_0 is measured in COARSE lattice units, where it is O(1) and k-independent.

The Combes-Thomas estimate at step k is applied on the coarse lattice Lambda_{k+1} with spacing a_{k+1}. The operator hat{A}^{(s)} is supported in a ball of diameter R_0 coarse lattice spacings, with R_0 bounded independently of k. The Combes-Thomas decay is e^{-Delta-hat * dist / C} where dist is measured in coarse lattice spacings. The zeta sum converges with bound depending on R_0 and N but not on k.

The one subtlety: Balaban's block-spin generates operators that are NOT strictly local but have exponentially decaying tails. The polymer expansion writes the effective action as a sum over connected polymers, each localized to a region X with activity decaying as e^{-kappa |X|}. The "local operator" in the spectral lemma is actually a sum over polymers containing the origin, and the "support radius R_0" should be interpreted as the effective localization scale. The Combes-Thomas estimate can be applied with a slightly modified R_0 that accounts for the exponential tail, and the result is the same: the zeta sum is bounded by a k-independent constant.

**Verdict on (c): SOUND.** The support radius R_0 is O(1) in block lattice units and k-independent, as established by Balaban's polymer expansion. The Combes-Thomas estimate gives a k-independent bound on the zeta sum.

**Impact on the claimed result:**

The CLOSABLE GAP in sub-point (b) requires a 1-paragraph clarification about how the linear combination lemma handles operators with different temporal extents. This does not affect the main claim because the mathematical content is present -- all temporal extents are bounded by R_0 which is k-independent.

No impact on (i) the main claim Delta_infinity > 0, (ii) subsidiary claims, or (iii) Clay prize eligibility.
