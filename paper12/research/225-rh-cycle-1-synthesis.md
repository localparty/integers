# 225 — RH Cycle 1 Synthesis

*Cycle: 1. Date: 2026-04-09. Agent: Synthesis.*

---

## Path status table

| Path | Step attempted | Construction | Adversarial | Status after cycle 1 |
|:--|:--|:--|:--|:--|
| 1 (Brauer-KMS) | Spectral density irrationality f(gamma) not in (1/k)Z | BLOCKED | INTACT (weakened on 2 sub-points) | **BLOCKED** — f(gamma) not computed; distributional subtlety threatens well-definedness |
| 2 (Atiyah-Singer) | Functional-analytic closure epsilon -> 0 | BLOCKED | DAMAGED (ind_BC(e_2)=0 raises kill risk) | **DAMAGED** — only computed index is zero; Fredholm module requires T_BC |
| 3 (Stone) | Spectral realisation (reverse inclusion) | BLOCKED | INTACT (clarified as dependent path) | **BLOCKED** — dependent on Path 5 or spectral realisation closing elsewhere |
| 4 (Penrose) | Curvature bound on H_R | BLOCKED | DAMAGED (analogy not rigorous) | **DAMAGED** — Penrose transposition has 3 ungrounded steps |
| 5 (CM-trace) | Weil positivity of BC spectral weights | BLOCKED | INTACT (KMS->Weil gap identified) | **BLOCKED** — KMS positivity is proved; gap to Weil positivity is well-posed |

## Steps closed this cycle

**0.** No steps were closed. This is cycle 1 (mapping cycle).

## Steps broken this cycle (honest negatives)

**0 steps broken,** but two paths DAMAGED:
- Path 2: the only computed index vanishes (ind_BC(e_2) = 0), raising the risk that all indices vanish, which would kill the path
- Path 4: the Penrose transposition relies on analogies (null geodesics, singularity interpretation, modular curvature) that have not been made rigorous

## Steps unblocked

**0.** No cross-path dependencies were resolved.

## Joint probability updated

- **Prior (pre-cycle 1):** P(RH | Integers framework) ~ 55% (per Compendium §F.3, based on 0.55 joint probability of at least one path closing in 6 months)
- **Evidence from cycle 1:** No steps closed; two paths damaged. Net evidence is slightly negative (reduced path count from 5 effective to 3).
- **Posterior:** P ~ 50%. The damage to Paths 2 and 4 reduces the effective attack surface. The remaining 3 paths (1, 3, 5) are intact but blocked.

Note: the 50% is the probability of closing a proof, not the probability of RH being true. RH's truth probability given the 37 R-Theorems remains ~ 1 - 10^{-27} per the Compendium §E.

## Cross-path observations

1. **The Meyer distributional subtlety is universal.** Paths 1, 2, 3, and 5 all hit the same wall: T_BC in the Meyer formulation is distributional, not a genuine operator. This is the single biggest cross-path blocker. Resolving it would unblock all four paths simultaneously.

2. **Path 5 is the strategic hub.** Closing Path 5 (Weil positivity) would give RH directly AND unblock/supersede Paths 1 and 3. The KMS-implies-Weil sub-path is the highest-return target.

3. **Path 3 is dependent, not independent.** The adversarial review clarified that Path 3 adds no value unless spectral realisation is proved by another route. It should be reclassified as a "completion path" rather than an "attack path."

## Recommended next cycle focus

**Primary: Path 5 (CM-trace / KMS -> Weil positivity).**
- Specific target: determine whether KMS reflection positivity at beta = 1, combined with the Connes-Marcolli explicit formula, implies Weil positivity
- This is a specific, well-posed mathematical question
- If answered affirmatively, RH follows; if negatively, the entire programme needs reassessment

**Secondary: Path 1 (Brauer-KMS / irrationality).**
- Specific target: compute f(gamma) explicitly from the V-coupling commutator
- This is independent of the Meyer distributional issue (the commutator can be computed formally)
- If f(gamma) turns out to be a known transcendental, irrationality may follow from standard results

**Deprioritize: Paths 2, 3, 4.**
- Path 2: dead unless a non-trivial index is found
- Path 3: dependent on other paths closing first
- Path 4: analogy has not been made rigorous; low probability of closure
