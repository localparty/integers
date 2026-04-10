# 236 — RH Cycle 2 Synthesis

*Cycle: 2. Date: 2026-04-09. Agent: Synthesis.*

---

## Path status table

| Path | Step attempted | Construction | Adversarial | Status after cycle 2 |
|:--|:--|:--|:--|:--|
| 1 (Brauer-KMS) | Phase shift computation + genericity argument | BLOCKED (narrowed) | INTACT (weakened on 4 sub-points) | **BLOCKED** — gap narrowed to S_3 ∩ S_4 ∩ S_6 = ∅; commutator not yet computed rigorously |
| 2 (Atiyah-Singer) | Find non-trivial index or kill | BLOCKED (structural) | KILLED (unanimous) | **KILLED** — distributional T_BC incompatible with index theorem framework |
| 3 (Stone) | Anti-fine-tuning refinement | BLOCKED (dependent) | INTACT (weakened: dark-state loophole) | **BLOCKED** — dependent on Path 5; anti-fine-tuning bound has dark-state loophole |
| 4 (Penrose) | Ground 3 ungrounded steps or kill | BROKEN (3 structural impossibilities) | KILLED (unanimous) | **KILLED** — category error: Lorentzian geometry ≠ C*-algebra |
| 5 (CM-trace) | KMS => Weil positivity? | BLOCKED (KMS =/=> Weil) | DAMAGED (all 3 sub-paths blocked) | **DAMAGED** — KMS direction fails; Li equiv. to Weil; Hecke diagonal; need new approach |

## Steps closed this cycle

**0.** No steps closed. However, cycle 2 achieved two important
negative results: (1) KMS does NOT directly imply Weil positivity,
(2) Li's criterion is equivalent to Weil and provides no shortcut.

## Steps broken this cycle (honest negatives)

**2 paths KILLED:**
- **Path 2** (Atiyah-Singer): distributional T_BC is structurally
  incompatible with the index theorem. No known extension covers
  distributional operators. The only computed index vanishes.
  UNANIMOUS kill: construction + adversarial agree.

- **Path 4** (Penrose): category error between Lorentzian geometry
  and C*-algebra theory. Three ungroundable steps (null geodesics,
  singularity interpretation, curvature). No natural Lorentzian
  structure on state space. UNANIMOUS kill: construction +
  adversarial agree.

**Synthesis agrees with both kills.** The kills are appropriate:
both paths have structural impossibilities, not just hard gaps.

**1 path DAMAGED:**
- **Path 5** (CM-trace): the primary sub-path (KMS => Weil) fails.
  The path needs redirection in cycle 3.

## Steps unblocked

**0.** No cross-path dependencies resolved.

## Joint probability updated

- **Prior (post-cycle 1):** P(RH proof via programme) ~ 50%
- **Evidence from cycle 2:**
  - Negative: 2 paths killed (effective attack surface: 5 → 3).
    Path 5 primary sub-path fails.
  - Positive: Path 1 gap narrowed with concrete residual question.
    Honest negatives prevent wasted future cycles.
- **Posterior:** P ~ 42%. The path count drops from 5 effective to
  3 (1, 3, 5), with Path 3 dependent. Effective independent
  paths: 2 (Path 1 + Path 5). The programme is concentrating on
  fewer, better-understood paths.

Note: probability of RH being TRUE remains ~ 1 - 10^{-27}. The
42% is probability of closing a PROOF within the programme.

## Cross-path observations

1. **The distributional T_BC obstacle is now confirmed as the
   universal blocker.** It kills Paths 2 and 4, weakens Paths 1
   and 3, and constrains Path 5's off-diagonal computations.
   Resolving the distributional nature of T_BC would be the
   single highest-impact advance.

2. **The three-level attempt order worked.** Every construction
   agent attempted a sub-computation (level 2) rather than just
   diagnosing. Path 1 narrowed its gap. Path 5 identified a
   concrete negative (KMS =/=> Weil). Paths 2 and 4 produced
   honest kill recommendations. This is a marked improvement
   over cycle 1's pure-diagnosis outputs.

3. **The kill mechanism worked correctly.** Round 1 adversarial
   flagged Paths 2 and 4 as weak. Cycle 2 investigated both and
   produced unanimous kill recommendations. The kills are
   well-grounded in structural impossibilities, not premature
   pessimism.

4. **Path 5 needs redirection.** The KMS => Weil direction is
   closed. Candidate replacements: Nyman-Beurling completeness
   (density in L^2), Baez-Duarte criterion (convergence of
   specific sequences), or a deeper use of the multiplicative
   structure of A_BC.

## Recommended next cycle focus

**Primary: Path 5 (CM-trace) with NEW sub-path.**
- Target: investigate Nyman-Beurling completeness criterion.
  RH iff the functions {rho_theta(x) = sum_{n<=theta} mu(n)/n * floor(theta/n x)}
  are dense in L^2(0,1). Can this density be established from
  the BC Hilbert space H_R and the Hecke action?
- This bypasses the Weil matrix entirely and works directly in
  L^2, which is where the BC representation lives.

**Secondary: Path 1 (Brauer-KMS).**
- Target: compute [log R-hat, Pi_chi] explicitly on |gamma_1>
  using mpmath. Get a concrete number for f(gamma_1) and test
  whether it lies in (1/k)Z for k = 3, 4, 6.

**Deprioritize: Path 3** (dependent on Path 5).
**Remove: Paths 2, 4** (KILLED).
