# Link 10 Critic Verdict: dev(δE_k^{d=6}) ≥ 2 non-perturbatively

**Verdict: SURVIVED**

## Attack-by-attack summary

**AV1 — Lattice bound degrades at coarse k.** For early steps k < k_0,
the paper replaces the Kato-Rellich/threshold argument with a direct
non-perturbative polymer bound (§5.4.5 / lines 973-992): |K_k(X,V)| ≤
e^{-κ|X|} uniformly in k, giving C_np · Δ̂_{k+1}^2 without invoking the
threshold gap at all. No degradation at coarse k. Attack fails.

**AV2 — Borel-summability hidden in perturbative-to-non-perturbative
bridge.** (B1) invokes Kotecky-Preiss to establish a *convergent* (not
asymptotic) polymer expansion. The dimension classification in Part III.3
is algebraic and symmetry-based, not perturbative. No Borel summation
enters. The caveat is that (B1) is extracted from Balaban's implicit
construction, not an explicit standalone theorem (Remark, line 1660),
and the paper self-labels this claim "Conditional on (B1)-(B2)" in the
status table. This conditionality is stated, not hidden. Attack fails to
find a novel break.

**AV3 — dev defined only asymptotically, not step-by-step.** Definition
D.2 (§5.5.3) defines Boltzmann deviation order pointwise in k via the
transfer-matrix spectral sum at each RG step. The classification argument
(Part III.3) is applied to each δE_k^{d=6} independently. No asymptotic
issue. Attack fails.

**AV4 — k=0: two-particle threshold coincides with UV cutoff.** Same as
AV1: the polymer bound route does not require a spectral gap above the
two-particle threshold. For k < k_0, the polymer bound applies directly.
For k = 0 on the AF trajectory at large K, k_0(K) = 0 and the
strong-coupling block is empty (line 988). Attack fails.

**AV5 — δE_k^{d=6} is only the local part; long-range tails excluded.**
Polymer activities are quasi-local (bounded support ≤ R_0 block units).
Multi-site activities of size ≥ 2 sites with field content equivalent
to dimension d ≥ 8 fall in Class IV (dev ≥ 4 ≥ 2), so non-local tails
only strengthen the bound. The paper applies the Stability Lemma to each
O_i individually (lines 1504-1518) before summing. The locality hypothesis
is satisfied per-activity with uniformly bounded diameter. Attack fails.

## Conclusion

No attack vector breaks Link 10. The claim survives as **Conditional on
(B1)-(B2)**, which is the paper's own stated status and not a novel
weakness introduced by this review.

**SURVIVED**
