# Capacitor Patch — H4 Excision Run

*Updates for yang-mills-capacitor-v2 based on the Tier B excision run of 2026-04-13.*

---

## New kills

| Kill # | What failed | WHY | Pattern category | Re-entry gate |
|---|---|---|---|---|
| K-3 | Borel summability + Watson's theorem for 4D SU(N) YM | IR renormalon singularity at u = 2 in the Borel plane is on the positive real integration axis, making the perturbative series for <Tr F^2 Tr F^2> NOT Borel summable in the standard sense. Watson's theorem requires sector analyticity in g^2 (opening > pi); Balaban (B1) gives only disk analyticity (|g^2| < rho). No constructive QFT precedent for 4D gauge theory Borel summability exists. | Distributional (formal series vs definite number) + External-dependency (requires Borel summability theorem that does not exist) | Either (a) proof of IR renormalon cancellation in gradient-flow-rescaled correlator F(t) = S_{2,t}^c/c_1(t)^2, or (b) constructive proof of medial Borel summability for the polymer expansion |
| K-4 | Large-N then finite-N approach to H4 | IR renormalons persist at N = infinity (position u_IR = 48pi^2/11 in planar Borel plane); planar perturbative series is still factorially divergent; H4 at large N is itself open; no rigorous 1/N expansion exists for 4D YM correlators. Chatterjee (2016) lattice large-N results do not extend to continuum correlator perturbative matching. | External-dependency (requires large-N results that do not exist) + Circular (H4 at large N is a prerequisite, but is itself open) | Rigorous large-N continuum limit for Balaban construction + planar Borel summability |

## New cards

| Card # | Name | Content |
|---|---|---|
| Card 15 | Instanton Suppression at Short Distances | **WHAT**: In topological sectors |k| >= 1, the contribution to S_2^ren(x,y) is O(|x|^{11N/6}) as |x| -> 0 (from Bogomolny bound + AF). **WHY**: PARTIAL RESULT from Route 3. Proves instantons are rigorously sub-leading at short distances. Does NOT close H4 (k = 0 sector uncontrolled). **STATUS**: PROVED (within existing framework). Worth adding to Appendix L as a supporting result. |
| Card 16 | Convergent t-Expansion vs Divergent g^2-Expansion | **WHAT**: The small-flow-time expansion F(t) = sum a_n t^n converges for |t| < r_t (Lemma L.3.7 Step 2). The perturbative expansion in g^2 at fixed t is a formal power series with factorial growth from IR renormalons. These are DIFFERENT expansions in DIFFERENT variables. **WHY**: Prevents the confusion of conflating flow-time convergence with coupling-constant convergence. The t-expansion is a Taylor series of the non-perturbative F. The g^2-expansion is perturbation theory. **STATUS**: CLARIFICATION (structural insight, not a new result). |
| Card 17 | Common Wall: Polymer vs Perturbative Within k = 0 | **WHAT**: All four excision routes (analyticity, Borel, instanton, large-N) converge on the same obstruction: the relationship between the Balaban polymer expansion and its perturbative truncation within the trivial topological sector (k = 0). **WHY**: Identifies the SPECIFIC mathematical question that would close H4: does the Balaban polymer activity K_k(X, V) equal its perturbative expansion plus exponentially small corrections? **STATUS**: STRUCTURAL DIAGNOSIS. Difficulty 8/10. Most promising remaining direction. |

## Corrections to existing capacitor entries

| Entry | Correction |
|---|---|
| H.8 Escalation Route 2 (Borel summability) | UPDATE status from OPEN to KILLED (K-3). IR renormalon obstruction is fundamental, not just "requires proof of Borel summability." |
| H.8 Escalation Route 4 (Large-N) | UPDATE status from OPEN to KILLED (K-4). H4 at large N is itself open; the route does not simplify the problem enough. |
| H.8 Escalation Route 3 (Instanton gas) | UPDATE status from OPEN to PARTIAL. Instantons (|k| >= 1 sectors) are proved sub-leading. k = 0 sector remains the wall. |
| H.3 Pattern analysis Step 18* | ADD: The LOCK now stands at 11/10 (7 routes attempted, 7 blocked by the same wall). The single un-explored direction is "Balaban polymer perturbative content" — whether the polymer expansion is a constructive implementation of perturbation theory with controlled non-perturbative remainder. |

## Updated LOCK status

**Prior LOCK**: 9/10 (Taylor-coefficient identification stuck across 3 pattern categories from Routes A, B, C).

**Updated LOCK**: 11/10 (4 additional routes blocked: analyticity, Borel, instanton partial, large-N). All 7 routes converge on the same wall: perturbative series divergence in g^2 within the k = 0 topological sector.

**Residual direction**: Balaban polymer perturbative content (difficulty 8/10, most specific remaining approach). Not attempted in this run because it requires deep engagement with the Balaban CMP 95-119 construction at the level of individual polymer activities, which is a multi-month research programme.

## Updated joint probability

Prior: P(H4 closure) cascaded to 0.9910 via the R.D editorial honest-stall.

This run does not change the editorial honest-stall (Route D). The mathematical closure probability updates:

| Route | Prior p | Updated p | Reason |
|---|---|---|---|
| Analyticity (prior Route A) | 0.50 | 0.10 | BLOCKED, same obstruction confirmed from new angle |
| Borel (new Route 2) | -- | 0.05 | KILLED (K-3) |
| Instanton (new Route 3) | -- | 0.02 | PARTIAL only; k=0 uncontrolled |
| Large-N (new Route 4) | -- | 0.03 | KILLED (K-4) |
| Polymer perturbative content (new) | -- | 0.15 | Un-attempted; most specific remaining direction |
| Editorial honest-stall (Route D) | 0.99 | 0.99 | Unchanged |

P(mathematical closure by any route) = 1 - (0.90)(0.95)(0.98)(0.97)(0.85) = 1 - 0.688 = 0.312

P(paper ships, counting editorial) = 1 - (1 - 0.312)(1 - 0.99) = 1 - 0.00688 = 0.993

The paper ships with high confidence. H4 mathematical closure probability has decreased from ~0.74 (prior) to ~0.31 (updated), reflecting the systematic exploration and blocking of routes.
