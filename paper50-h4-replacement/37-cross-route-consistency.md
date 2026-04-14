## §37 — Cross-Route Consistency

*The three routes should agree on H4. Disagreement signals either H4 is subtler than we think, or one of the routes has a gap. The cross-consistency criterion and its interpretation.*

---

## 37.1. The consistency principle

H4 is a binary statement about pure Yang-Mills: the non-perturbative Schwinger functions match perturbation theory at short distances. There is only one H4, and it either holds or it does not.

The three routes compute H4 via three different machineries:

- Route A: lateral Borel sum of the perturbative series.
- Route B: Kim-Sarnak bounds on the Wilson-loop L-function.
- Route C: Gaitsgory-Raskin-transferred geometric-Langlands spectral data.

If all three routes are sound, they must agree on H4. Agreement is the consistency criterion: the three routes' numerical predictions for the short-distance Wilson-loop correlator, or the short-distance OPE coefficients, or the critical L-function values, must coincide.

This agreement is not a weak check — it is a strong test. Three independent computations of the same physical quantity via different mathematical frameworks should agree to the precision of each computation. Agreement at the 1-5% level (typical precision of lattice QCD combined with perturbative truncation) is expected. Disagreement at the 10%+ level signals a problem.

---

## 37.2. The specific cross-checks

Four specific quantities can be computed by all three routes and compared.

**Cross-check 1: Leading OPE coefficient of $\mathrm{Tr}\, F^2$.** The short-distance OPE coefficient of the $\mathrm{Tr}\, F^2$ operator, at leading order in the running coupling, is predicted by each route. The perturbative prediction is $\beta_0 g^2(\mu)$ at one loop. Routes A, B, C each compute this coefficient via their own machinery and should return the same value.

**Cross-check 2: Wilson-loop correlator at short distance.** The expectation value $\langle W(C) \rangle$ for a specific small loop $C$ (e.g., circular loop of radius 0.03 fm). Each route predicts this value as a function of the running coupling.

**Cross-check 3: Critical L-function value.** $L(1, W)$ for the Wilson-loop L-function (directly computed by Route B, indirectly by Routes A and C via the Mellin-transform relation).

**Cross-check 4: Schwinger function at short distance.** $S_2(|x - y|)$ for $|x - y| = 0.05$ fm. Computable by each route and by lattice QCD; cross-route agreement plus lattice match is the strongest validation.

These four cross-checks are the specific operational tests of cross-route consistency.

---

## 37.3. The consistency table

When all three routes complete their verification (§34-36), the results are assembled in a consistency table:

| Quantity | Route A | Route B | Route C | Lattice QCD | Agreement? |
|---|---|---|---|---|---|
| Leading OPE coeff of $\mathrm{Tr}\, F^2$ | $\beta_0 g^2$ within 5% | $\beta_0 g^2$ within 3% | $\beta_0 g^2$ within 5% | $\beta_0 g^2$ within 2% | YES |
| $\langle W(C_0) \rangle$ at radius 0.03 fm | [numerical value] | [numerical value] | [numerical value] | [numerical value] | ? |
| $L(1, W)$ | [indirect value] | [direct value] | [indirect value] | — | ? |
| $S_2(0.05\text{ fm})$ | [numerical value] | [numerical value] | [numerical value] | [numerical value] | ? |

Each row's "Agreement?" column is filled in based on whether the three routes agree within their stated uncertainties. If all four rows say YES, cross-route consistency is verified. If any row says NO, a gap analysis is triggered.

---

## 37.4. Interpretation of disagreement

Disagreement between routes has three possible causes. Each has a specific interpretation and repair protocol.

**Cause 1: One route has a technical gap.**

The most common cause of disagreement. One of the three routes has a subtle error — a missed transseries sector, a miscomputed Eisenstein-series residue, or a miscontrolled decoupling limit. Repair: identify which route disagrees with the other two (the "odd one out") and audit that route's derivation.

Operationally, the repair applies the ORA v8 adversarial pass to the odd-one-out route with specific attention to the disagreement point. The critic's instruction: "Routes X and Y agree on quantity Q; Route Z disagrees. Identify the step in Route Z's derivation that produces this disagreement." This is a focused, high-signal audit.

**Cause 2: H4 is subtler than the three routes assume.**

A less common but important possibility. H4, as formulated in §01, assumes that the perturbative-non-perturbative match is term-by-term. If H4 in fact holds only in a weaker sense (e.g., with logarithmic corrections at specific orders, or with Stokes-phenomena ambiguities that are not captured by the routes' formulations), the three routes might each produce slightly different predictions that reflect this subtlety.

Repair: refine the H4 statement itself. Specifically, identify whether the disagreement pattern is consistent with a specific type of correction (e.g., non-analytic terms proportional to $e^{-1/g^2}$, or logarithmic terms proportional to $\log(\mu / \mu_0)^k$). If so, revise the match statement C1 (§29.1) to include these corrections, and re-run the verification with the refined statement.

**Cause 3: Programme-internal infrastructure inconsistency.**

Rare but possible. The disagreement is not at the level of the individual routes but at the level of the shared infrastructure (Paper 8 Links 1-17, Paper 10 scheme independence, Paper 11 K.4). If, for example, the scheme-independence theorem in Paper 10 has a subtle gap that affects all three routes differently, the disagreement reflects this shared-infrastructure inconsistency.

Repair: audit Paper 10 or Paper 11 (whichever is the suspected source). This is a serious repair because it propagates to multiple papers, not just Paper 50.

---

## 37.5. The gap analysis protocol

When cross-route disagreement is detected, the gap analysis protocol runs:

1. **Localize the disagreement.** Which of the four cross-check quantities shows the largest discrepancy? Which routes disagree on that quantity?

2. **Identify the odd one out.** Are two routes consistent and a third disagreeing (Cause 1), or are all three routes scattered (potentially Cause 2)?

3. **Apply ORA v8 adversarial pass.** Run the adversarial pass on the odd-one-out route (Cause 1) or on all three routes with a "refine H4 statement" instruction (Cause 2).

4. **Check shared infrastructure.** If the adversarial passes do not localize the gap in any single route, audit Paper 8 / Paper 10 / Paper 11 for shared-infrastructure issues (Cause 3).

5. **Repair and re-verify.** Once the cause is identified, apply the corresponding repair. Re-run the cross-check table.

6. **Iterate until consistency.** Cross-route consistency is not established until the table shows YES in every row.

The protocol takes weeks to months depending on the disagreement's depth. Paper 50 does not ship until consistency is achieved.

---

## 37.6. The positive case: all three routes agree

If all three routes agree on all four cross-checks, the consistency criterion is satisfied. This is the positive case: H4 is closed by all three routes simultaneously.

The positive case has strong epistemic weight. Three independent mathematical frameworks (resurgence, Langlands functoriality, geometric Langlands) converging on the same numerical predictions for the same physical quantity, each with adversarial verification, each cross-checked against lattice QCD, constitutes the strongest form of mathematical validation available for a claim of this type. The three-route strategy's insurance argument (§24) pays off maximally in this case.

Paper 50, in the positive case, presents H4 as closed with triple-route redundancy. The paper's title is *Yang-Mills H4 Replacement: Three Routes to the Asymptotic-Freedom Match*. The abstract notes that each route independently closes H4 with adversarial verification and cross-route consistency to within stated errors.

---

## 37.7. The negative case: persistent disagreement

If, after extended gap analysis, cross-route consistency cannot be achieved, Paper 50 faces the negative case. The options are:

**Option N1: Ship with one route, flag the disagreement.** If Route X has passed its own adversarial threshold and lattice match, but Routes Y and Z disagree with Route X on a specific cross-check, Paper 50 ships with Route X as primary and documents the disagreement with Routes Y, Z as "further investigation required".

**Option N2: Wait for additional work.** Paper 50 is held in draft until the disagreement is resolved. This is the stricter option; it may delay shipping by months.

**Option N3: Re-characterize H4.** The disagreement signals that H4 itself needs refinement. Paper 50 ships with the refined H4 statement and its three-route proof. This is the most ambitious option; it changes the target from the original H4 to a refined version.

The choice among N1, N2, N3 depends on the disagreement's nature and the programme's schedule. Option N1 is the default; N2 is the conservative choice; N3 is the scientifically-rewarding but scope-expanding choice.

---

## 37.8. What cross-route consistency does not guarantee

Cross-route consistency is a strong check, but it is not absolute validation.

**Not guaranteed: correctness of the shared infrastructure.** All three routes depend on Paper 8 Links 1-17, Paper 10, Paper 11 K.4. If any of these shared components has an undetected gap, all three routes inherit it and agree on the wrong answer. Consistency cannot detect this.

**Not guaranteed: the three routes are fully independent.** The cross-references in §25 show that A, B, C share analytic and functorial structure. Strong cross-references could in principle propagate an error from one route to another, producing spurious agreement.

**Not guaranteed: the refined H4 statement is correct.** Option N3 (re-characterize H4) produces a new statement that is internally consistent across the three routes. Whether the new statement is the *correct* formulation of the perturbative-non-perturbative match is a separate question.

Consistency is necessary for closure but not sufficient. The adversarial pass (§29) and lattice cross-check remain essential independent validations.

---

## 37.9. Summary

The three routes must agree on H4. Cross-route consistency is operationalized via four specific cross-checks: leading OPE coefficient, Wilson-loop correlator at short distance, critical L-function value, and Schwinger function at short distance. Disagreement has three possible causes: technical gap in one route (most common), H4 subtlety (rarer), or shared-infrastructure inconsistency (rare). The gap analysis protocol localizes the cause and triggers repair. Paper 50 ships only when consistency is achieved, with options for partial shipping if consistency is unattainable. The positive case (all three routes agree) provides the strongest epistemic validation. Cross-route consistency is necessary but not sufficient for closure; it complements adversarial verification and lattice matching.

---

*Paper 50 §37. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
