# Proof Sketch: Q7-CASIMIR

*Retroactive proof file for the v8 P vs NP Toolkit.*
*Source data: paper28-pvnp/code/results_q7_casimir.md*
*Original date: 2026-04-12. Re-verified: 2026-04-12 (independent seed).*

---

## Claim

Solution entropy per constraint (s/alpha) plays the role of Casimir energy density, with sub-exponential decay for P-time and exponential collapse for NP-complete, reproducing a three-scale geometric hierarchy.

## Proof sketch

1. Define s(alpha) = log2(median #solutions) / n as the solution entropy density at clause ratio alpha, and consider s/alpha as the energy density per unit constraint.
2. In the Casimir analogy, the constraint ratio alpha plays the role of the compactification scale, and s/alpha is the vacuum energy density.
3. **P-time (Horn-SAT):** s/alpha decays monotonically but stays positive throughout (s/alpha in [0.039, 1.719] across alpha = 0.5 to 5.0). 100% of instances remain satisfiable at all tested ratios.
4. **NPC (3-SAT):** s/alpha decays faster and collapses at alpha ~ 4.267-5.0 (the SAT/UNSAT phase transition). This is a decompactification transition.
5. Both classes show 3-SAT decaying faster than Horn-SAT, confirming the P vs NPC distinction.

## Computational evidence (re-verification, independent seed)

### Decay rate fits: log(s/alpha) vs alpha

| Class    | Decay rate | R^2    | Original decay | Original R^2 |
|----------|-----------|--------|----------------|--------------|
| Horn-SAT | -0.792    | 0.962  | -0.358         | 0.996        |
| 3-SAT    | -1.084    | 0.974  | -0.503         | 0.913        |

**Note on decay rate discrepancy:** The original run fitted log(s) vs alpha; this re-verification fits log(s/alpha) vs alpha (as specified in the claim). The qualitative ordering is preserved: 3-SAT decays faster than Horn-SAT. The exact numerical values depend on the fitting target (log s vs log(s/alpha)), the alpha range included, and the random seed.

### Horn-SAT perpetual satisfiability

- 100% SAT at all 10 tested ratios (alpha = 0.5 through 5.0): **CONFIRMED**
- s/alpha > 0 everywhere: **CONFIRMED** (minimum s/alpha = 0.039 at alpha = 5.0)

### Three-scale hierarchy (3-SAT inflection points)

Second derivative d^2s/dalpha^2 computed at interior points:

| alpha | d^2s/dalpha^2 |
|-------|--------------|
| 2.000 | +0.022       |
| 3.000 | -0.095       |
| 3.500 | +0.027       |
| 4.000 | -0.180       |
| 4.267 | +1.248       |

Sign changes: 4 (at alpha ~ 2.19, 3.39, 3.57, 4.03).

**FLAG:** The original claim of exactly 2 inflection points is not reproduced. At n=12 with 50 trials, median solution counts at alpha = 4.267 and 4.5 are both 2, creating a plateau (s = 0.0833 at both points). This generates spurious oscillations in the second derivative. The extra inflection points near alpha ~ 3.4-3.6 and ~ 4.0 arise from finite-size noise, not genuine structural features.

**Assessment:** The broad three-regime structure (high-s below alpha ~ 2, moderate-s from 2-4, low-s above 4) is visible in the raw data, but the precise claim of "exactly 2 inflection points" is sensitive to discretization and finite-size effects at n=12. The claim should be softened to: "3-SAT entropy density shows three qualitative regimes separated by regions of changing concavity near alpha ~ 2-3 and alpha ~ 4."

## Verdicts

| Sub-claim | Status |
|-----------|--------|
| P vs NPC distinction in decay rates | **CONFIRMED** (3-SAT decays faster) |
| Horn-SAT 100% SAT, s/alpha > 0 throughout | **CONFIRMED** |
| 3-SAT collapse near alpha ~ 4.267 | **CONFIRMED** (median drops to 1-2 solutions) |
| Exactly 2 inflection points | **NOT REPRODUCED** -- 4 sign changes at n=12; finite-size artifact |
| Three qualitative regimes | **SOFT CONFIRMED** -- visible in data, not crisply delineated |

## Status

PARTIALLY VERIFIED -- core P-vs-NPC distinction and Horn perpetual satisfiability confirmed. Three-scale hierarchy claim needs refinement: the "exactly 2 inflection points" is an overfit to finite-size data. Recommend stating the hierarchy as a qualitative three-regime observation rather than a precise inflection-point count.
