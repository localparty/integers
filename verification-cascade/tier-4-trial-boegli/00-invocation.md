# Tier 4 Trial: Boegli Spectral Exactness Verification

*The pilot run. Smallest target, cleanest proofs. Validates the verification cascade architecture before committing to larger targets (CCM, Balaban, Bulatov-Zhuk).*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-13.*

---

## The 4-line invocation

Paste this into a new Claude Code session:

---

read your instructions from
verification-cascade/strategy/01-tier-4-trial/01-ora-instructions.md

the run brief is
verification-cascade/strategy/01-tier-4-trial/02-run-brief.md

the toolkit for this run is
verification-cascade/strategy/01-tier-4-trial/03-capacitor.md

the run output directory is
verification-cascade/strategy/01-tier-4-trial/output/

---

## What this does

1. The ORA reads its instructions (how to be a runner -- condensed pilot version)
2. The ORA reads the brief (what to verify: Boegli Theorem 2.6 spectral exactness)
3. The ORA reads the capacitor (compiled domain knowledge + kills + correspondences + escalation routes)
4. The ORA creates a blackboard in the output directory and begins cycling

## Expected behavior

- Wave 1: 5 parallel Verifiers (one per load-bearing step) + 5 parallel Re-derivers
  - Verifier reads Boegli's paper section, restates claim, checks assumptions, compares to primary source
  - Re-deriver attempts independent derivation without reading the proof
- Wave 2: Synthesis cross-checks + any escalations
  - Cross-check: do Steps 2 and 3 agree on the spectral inclusion mechanism?
  - Cross-check: does Step 5 (Teschl interface) correctly invoke Step 1 (gsrc definition)?
- Wave 3+: Critics on WEAKENED steps, construction on BROKEN steps
  - If any step is WEAKENED: escalate to Tier B (excise via Stummel-Vainikko or direct proof)
  - If any step is BROKEN: escalate to Tier C (construct alternative route for RH Layer 4)
- Target: 2-4 waves, ~15-25 agents total

## Runtime optimizations active

- Compiled capacitor (single file, no file reads at runtime beyond the brief and capacitor)
- Effort-tiered dispatch (standard effort for non-LB Verifiers, maximum effort for LB steps)
- Kill list in every agent's core (I-v6-5 safety: agents see what has been tried and failed)
- Escalation routes pre-identified per step (agents know where to go if a step breaks)
- Honest-first discipline: expect SURVIVED on all steps (published paper) but verify as if expecting BROKEN

## After the run completes

1. Read the blackboard in `output/blackboard.md` for the SURVIVED/WEAKENED/BROKEN table
2. If all 5 steps SURVIVED: RH Layer 4 is secure. Proceed to build the Tier 1 (CCM) capacitor.
3. If any step WEAKENED: review the Tier B escalation routes in the capacitor. Decide whether to excise.
4. If any step BROKEN: review the Tier C construction routes. This would be a significant finding.
5. Merge results back into the capacitor (update version to v2, add new cards, new kills if any)

## Amplification targets

If the pilot SURVIVES:
- The verification METHOD (brief format, capacitor structure, dispatch pattern, agent protocol) amplifies to Tier 1 (CCM)
- The spectral convergence verification technique amplifies to Tier 2 (Balaban has spectral-gap arguments)
- The SURVIVED verdict on Boegli strengthens Paper 13's Layer 4 from "depends on published theorem" to "depends on independently verified published theorem"

If the pilot finds something:
- ANY finding on a published, peer-reviewed paper is itself a publishable result
- Even WEAKENED is valuable: it identifies what needs repair before the Clay submission
- The finding amplifies as a warning to all other tiers: check published results, not just preprints
