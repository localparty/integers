# Tier 1 Trial: CCM Zeta Spectral Triples Verification

*The main event. Highest-value verification target in the cascade. The RH proof chain (Paper 13) depends on CCM at Layer 1. This is a PREPRINT -- not yet peer-reviewed. Independent verification is critical.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-13.*

---

## The 4-line invocation

Paste this into a new Claude Code session:

---

read your instructions from
verification-cascade/tier-1-trial-ccm/01-ora-instructions.md

the run brief is
verification-cascade/tier-1-trial-ccm/02-run-brief.md

the toolkit for this run is
verification-cascade/tier-1-trial-ccm/03-capacitor.md

the run output directory is
verification-cascade/tier-1-trial-ccm/output/

---

## What this does

1. The ORA reads its instructions (how to be a runner -- adapted from Tier 4 pilot with LESSON-1 amplification)
2. The ORA reads the brief (what to verify: CCM Theorems 4.2, 5.10, Lemmas 5.2(i), 7.2, 7.3 and their dependencies)
3. The ORA reads the capacitor (compiled domain knowledge + kills + correspondences + escalation routes)
4. The ORA creates a blackboard in the output directory and begins cycling

## Expected behavior

- Wave 1: 7 parallel Verifiers (one per load-bearing step) + 7 parallel Re-derivers = 14 agents
  - Verifier reads CCM paper section, restates claim, checks assumptions, compares to primary sources
  - Re-deriver attempts independent derivation without reading the proof
- Wave 2: Synthesis cross-checks + any escalations = 4-8 agents
  - Cross-check: do Steps 1 and 5 agree on the spectral identification mechanism?
  - Cross-check: does Step 6 (uniform convergence) correctly invoke Step 2 (simplicity of eigenvalue)?
  - Cross-check: does Step 4 (Tgamma = gammaT) actually preserve all operations in Steps 5-6?
  - Standing hypothesis audit: for every cited external result, verify ALL hypotheses including ambient/standing ones (LESSON-1 from Tier 4)
- Wave 3: Critics on WEAKENED steps + deeper analysis of medium-high risk steps = 4-8 agents
  - If any step is WEAKENED: classify as CLOSABLE or GENUINE
  - If GENUINE: escalate to Tier B (Connes-van Suijlekom alternative) or Tier C (direct construction bypassing CCM)
- Wave 4+: Construction/escalation agents if needed = 2-6 agents
  - Tier B: attempt excision via alternative spectral realization
  - Tier C: attempt bypass via ITPFI + Boegli direct route
- Target: 3-5 waves, ~20-35 agents total

## Amplification from Tier 4

This run incorporates all lessons from the Tier 4 pilot (Boegli verification):

1. **LESSON-1**: Always verify standing hypotheses of cited theorems. The Tier 4 run found that Teschl's standing hypothesis (2.1) fails for Galerkin projections. CCM cites multiple external results -- each citation is an attack surface for standing-hypothesis issues.

2. **TK-6** (Galerkin gnrc): Imported as background. If CCM uses finite-dimensional approximations with compact-resolvent limits, TK-6 provides an independent verification route.

3. **TK-7** (gsr sufficiency): Boegli's spectral inclusion requires only gsr, not gnr. If CCM's eigenvalue identification route through Boegli needs only spectral inclusion, gsr is an easier fallback.

4. **K-T4-1** (direct Teschl invocation with Galerkin projections): Killed approach. If CCM uses a similar construction, agents know this route is dead.

## Runtime optimizations active

- Compiled capacitor (single file, ~450 lines, no file reads at runtime beyond the brief and capacitor)
- Effort-tiered dispatch (maximum effort for all starred LB steps, standard for non-LB)
- Kill list in every agent's core (agents see what has been tried and failed across all tiers)
- Escalation routes pre-identified per step (agents know where to go if a step breaks)
- Standing-hypothesis audit protocol (LESSON-1: every cited theorem's ambient hypotheses are checked)
- Honest-first discipline: expect most steps to SURVIVE (Connes/Consani/Moscovici are top-tier) but verify as if expecting BROKEN. Preprint status = higher scrutiny than Tier 4.

## After the run completes

1. Read the blackboard in `output/blackboard.md` for the SURVIVED/WEAKENED/BROKEN table
2. If all 7 steps SURVIVED: RH Layer 1 upgrades from "depends on preprint" to "depends on independently verified preprint". Confidence: 8/10 -> 9/10. Proceed to Tier 2 (Balaban).
3. If any step WEAKENED:
   - CLOSABLE: repair in Paper 13 + note in Clay submission. Confidence stays at 8/10.
   - GENUINE: escalate to Tier B (Connes-van Suijlekom) or Tier C (bypass CCM entirely). Confidence drops to 6/10.
4. If any step BROKEN: this is a significant finding. A gap in a Connes preprint. Escalate to Tier C immediately. Confidence drops to 4/10 pending bypass construction.
5. Merge results back into the capacitor (update version to v2, add new cards, new kills if any)

## Risk profile (preprint vs published)

| Factor | Tier 4 (Boegli, published) | Tier 1 (CCM, preprint) |
|---|---|---|
| Peer review status | Published (IEOT, 2017) | Preprint (arXiv, Nov 2025) |
| Author caliber | Boegli (strong, active) | Connes (Fields Medal) + Consani + Moscovici |
| P(fundamental gap) | ~5-10% | ~5-10% (author caliber compensates for no review) |
| P(presentation gap) | ~10-15% | ~20-30% (preprint, first draft) |
| P(standing hypothesis issue) | Found one (K-T4-1) | ~30-40% (LESSON-1 amplified) |
| Expected agents | ~15 | ~25-35 |
| Expected cycles | 2-3 | 3-5 |

## Amplification targets

If CCM SURVIVES:
- The verification result is itself a publishable finding: "Independent adversarial verification of Connes-Consani-Moscovici's spectral realization of Riemann zeros"
- RH Layer 1 is secured. The full RH chain's weakest link moves from CCM (preprint) to whatever is next weakest
- The CCM verification technique amplifies to Tier 2 (Balaban uses spectral methods too)
- The SURVIVED verdict goes into the Clay submission

If CCM finds something:
- ANY finding on a Connes preprint is significant
- Even WEAKENED-CLOSABLE is valuable: it identifies what the authors should fix before journal submission
- BROKEN would be historic: an independent verification catching a gap that the mathematical community missed
- The finding amplifies as a warning to all future work building on CCM
