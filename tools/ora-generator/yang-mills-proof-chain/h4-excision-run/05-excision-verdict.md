# H4 Excision Verdict: HONEST-STALL

*ORA v8 Tier B excision run. Final verdict.*
*Date: 2026-04-13.*

---

## Verdict: HONEST-STALL

H4 is NOT excised. All four routes are BLOCKED. The 18-step YM proof chain remains **17/18 unconditional, 1/18 conditional on H4**.

---

## Route summary

| Route | Status | What was achieved | What blocks closure |
|---|---|---|---|
| 1. Analyticity + Identity Theorem | BLOCKED | Refined understanding: the obstruction is in F(0) = F^pert(0), which IS H4. The convergent t-expansion and divergent g^2-expansion are distinct objects. | Identification of F(0) with perturbative prediction requires independent computation of F(0), which is H4. |
| 2. Borel Summability + Watson | BLOCKED | Clarified that the t-expansion is convergent (trivially Borel summable) while the g^2-expansion has IR renormalons at u = 2. Watson's theorem requires sector analyticity not available from Balaban. | IR renormalon singularities on the positive real Borel axis; no constructive QFT precedent for 4D YM Borel summability. |
| 3. Instanton Gas | **PARTIAL RESULT** | **Proved**: instanton (|k| >= 1 topological sector) contributions to the two-point correlator are O(|x|^{11N/6}) at short distances, rigorously sub-leading compared to the perturbative |x|^{-8}(log)^{-2}. | Non-perturbative effects within the trivial topological sector (k = 0) are not controlled by the Bogomolny bound. The k = 0 sector contains quantum fluctuations, condensates, and IR renormalon-type corrections. |
| 4. Large-N then Finite-N | BLOCKED | Instantons are eliminated at N = infinity (exp(-N * const) -> 0). Planar dominance simplifies the theory. But IR renormalons persist, planar series is still divergent, no rigorous 1/N expansion exists. | H4 at large N is itself open; no rigorous 1/N expansion for 4D YM correlators. |

---

## Cross-route structural analysis

### The common obstruction

All four routes converge on the SAME structural obstruction: **the relationship between the Balaban polymer expansion and its perturbative truncation within the trivial topological sector**.

- Route 1 hits it as: "the Taylor coefficients of F(t) at t=0 are not independently computable by perturbative methods."
- Route 2 hits it as: "the perturbative series in g^2 has IR renormalon singularities on the positive real Borel axis."
- Route 3 hits it as: "the k = 0 sector contains non-perturbative fluctuations not controlled by the Bogomolny bound."
- Route 4 hits it as: "IR renormalons persist at large N; the planar perturbative series is still divergent."

**The common wall is: perturbation theory does not converge to the non-perturbative answer within the k = 0 sector, and no mechanism is known to bridge this gap for 4D non-Abelian gauge theories.**

This is, in essence, the content of H4 itself. The four routes do not provide an end-run; they converge on the same fundamental difficulty from different directions.

### Pattern category of the wall

**Category: Distributional + Circular**

- Distributional: The perturbative series is a formal object (divergent power series in g^2) while the non-perturbative answer is a definite number. Bridging requires a summation prescription (Borel, resurgence), but the prescription's validity is part of the claim.
- Circular: Any route that tries to "prove" the perturbative series converges to the non-perturbative answer must either (a) independently compute both sides and compare, or (b) show the construction FORCES agreement. Route (a) requires computing the non-perturbative F(0) by non-perturbative methods AND the perturbative F^pert(0) by perturbative methods and showing they are equal — but the only non-perturbative method available (Balaban) does not produce explicit numerical values, and the perturbative method produces a divergent series. Route (b) requires showing the Balaban construction IS perturbation theory plus controlled corrections — which is exactly the Borel summability question.

### The LOCK tightens

This run adds to the cross-node structural LOCK from the prior run (9/10). The prior run established that Taylor-coefficient identification is stuck across three pattern categories (External-source-inconsistency, Wrong-space, Vacuous). This run establishes that four additional angles (analyticity, Borel summability, instanton gas, large-N) are all blocked by the same underlying wall.

**Updated LOCK: 11/10** (exceeds the 10-point scale, meaning: closure by any currently known technique is extremely unlikely).

The ONE structural direction that remains un-explored at the level of a rigorous attempt:

**The Balaban polymer expansion's perturbative content**: If each polymer activity K_k(X, V) can be shown to equal its perturbative expansion plus exponentially small corrections (i.e., the polymer expansion IS a constructive implementation of perturbation theory with controlled non-perturbative remainder), then H4 would follow. This is essentially a constructive QFT proof of Borel summability for the polymer expansion, specific to the Balaban framework.

This direction is distinguished from generic Borel summability (Route 2) because the Balaban construction provides EXPLICIT bounds on each polymer activity (|K_k(X,V)| <= e^{-kappa|X|}), which might be leveraged to prove that the perturbative expansion of each activity converges. The key question is whether the convergence of the spatial cluster expansion (in X) can be traded for convergence of the perturbative expansion (in g^2) within each cluster.

---

## What specifically blocks each route

| Route | Specific blocker | Difficulty estimate | External unlock? |
|---|---|---|---|
| 1 | F(0) = F^pert(0) is H4 itself | 10/10 | Constructive QFT proof that Balaban polymer expansion reproduces perturbation theory |
| 2 | IR renormalon at u = 2 in Borel plane | 9/10 | Resurgence programme for 4D SU(N) YM OR proof of IR renormalon cancellation in gradient-flow correlators |
| 3 | k = 0 sector non-perturbative effects | 9/10 | Same as Route 1 (within k = 0 sector) |
| 4 | Planar H4 open + no rigorous 1/N expansion | 9/10 | Planar Borel summability + rigorous 1/N expansion for 4D YM |

---

## Is any route CLOSE enough for a targeted push?

**Route 3 has a genuine partial result** (instanton suppression) that could be incorporated into the preprint independently of H4 closure. The partial result strengthens the case for H4 by showing that the dominant non-perturbative effects (instantons) are provably sub-leading. This is worth writing up as an addendum to Appendix L.

**The Balaban polymer perturbative content direction** (not one of the four routes, but identified by cross-route analysis) is the most promising new direction. It would require:
1. For each fixed polymer cluster X and RG scale k, expand K_k(X, V) in powers of g_k^2.
2. Use the Balaban convergence bounds (|K_k| <= e^{-kappa|X|}) to show the perturbative expansion of K_k converges.
3. Sum over clusters and RG scales.

This is a HARD constructive QFT problem, but it is MORE SPECIFIC than generic Borel summability and leverages the existing Balaban machinery. Difficulty estimate: 8/10.

---

## Honest assessment

H4 is a GENUINE open problem in mathematical physics. It is not a gap that can be closed by clever reframing or by invoking existing machinery. The four routes explored in this run, combined with the three routes from the prior H4 closure run (Routes A, B, C), constitute a systematic exploration of the known approaches. All seven approaches are blocked by the same fundamental wall: the divergence of perturbation theory in the coupling constant g^2 and the absence of a summation method that provably reconstructs the non-perturbative answer.

The gradient-flow framework provides the MILDEST formulation of H4 in the literature (Remark L.4.3) and the convergent t-expansion is a genuine structural advantage, but it addresses the wrong variable (t, not g^2). The paper ships honestly: 17/18 unconditional, 1/18 conditional on H4 in its mildest gradient-flow form.
