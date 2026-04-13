# Yang-Mills Verification Brief — Tier A

*For use with ORA v8 in `execute` mode (verification-and-repair).*

---

## Objective

Verify every step of the Yang-Mills mass gap proof chain (18 steps, 8 load-bearing). For each step, produce a SURVIVED / WEAKENED / BROKEN verdict. For any WEAKENED or BROKEN step, repair it before moving on.

## Target

`paper08-yang-mills/preprint/PROOF-CHAIN.md` — 18 steps for Δ∞ > 0.

- 17/18 unconditional. Step 18 conditional on H4.
- 8 load-bearing steps (Steps 1*, 3*, 4*, 6*, 10*, 12*, 14*, 18*).
- Prior adversarial review (Run 2, 2026-04-12): 10 SOUND, 8 WEAKENED, 0 BROKEN — all 8 repaired in Run 3.

## Mode

**VERIFY** — Tier A of the three-tier escalation (verify → excise → construct).

## Instructions

### Phase 1: Verification (all 18 steps)

For EACH step in the proof chain:

1. **Read** the step's source (section/appendix referenced in PROOF-CHAIN.md)
2. **Read** the capacitor entry (H.1 chain, H.2 correspondences, H.3 patterns, H.4 grammar)
3. **Test** the logical dependency: does this step follow from its stated dependencies?
4. **Test** the mathematical content: is the argument correct? Are bounds tight? Are assumptions stated?
5. **Test** the literature claims: do cited results (Balaban CMP 95–119, Dimock, etc.) actually say what is claimed?
6. **Produce verdict:** SURVIVED / WEAKENED / BROKEN with specific justification

**Effort allocation:**
- MAX effort on all 8 load-bearing steps (marked with *)
- MEDIUM effort on routine steps
- MAX effort on Step 18* (the only conditional step — the H4 interface)

**Dispatch ALL steps in parallel.** Do not serialize. Each step is independent at the verification stage.

### Phase 2: Repair (any WEAKENED or BROKEN steps)

For each WEAKENED step:
1. Identify the specific weakness
2. Spawn an Author to strengthen the argument
3. Re-verify the repair with a fresh Critic
4. If re-verification passes → SURVIVED. If not → escalate.

For each BROKEN step:
1. Check the capacitor's escalation routes (H.8) for pre-identified alternatives
2. Spawn an Author to find an alternative route
3. If Tier B (excision) succeeds → dependency eliminated
4. If Tier B fails → attempt Tier C (construction) using the Six Patterns
5. If Tier C fails → HONEST-STALL with named blocker

### Phase 3: Capacitor update

After all steps are verified/repaired:
1. Update the META table with final SURVIVED/WEAKENED/BROKEN counts
2. Add any new kills to H.7
3. Add any new cards to H.10
4. Log all changes in MERGE LOG
5. Write the updated capacitor as v2

## Output structure

Write all output to the run output directory. Create:

```
00-blackboard.md          — running state: open leads, verdicts, dispatches
01-verification-verdicts.md — per-step verdicts with justification
02-repairs.md              — any repairs performed (empty if all SURVIVED)
03-capacitor-v2.md         — updated capacitor with verification results
04-summary.md              — executive summary: what survived, what broke, what was repaired
```

## Key references in the preprint

The YM preprint is at `paper08-yang-mills/preprint/`. Key sections:
- Section 4: KK spectral gap (Thm 4), IR equivalence (Thm 5)
- Section 5.3–5.7: RG preservation chain (Steps 6–14)
- Appendix H: Balaban extraction
- Appendix I: Operator extraction + gauge group extension
- Appendix J: Symanzik classification
- Appendix L: Gradient-flow OS reconstruction (Steps 15–18)
- Appendix M: Continuum limit uniqueness

## What NOT to do

- Do NOT re-derive the entire paper. Verify the CHAIN, not every sentence.
- Do NOT weaken a step just because you'd prove it differently. WEAKENED means the argument has a gap.
- Do NOT mark literature results as BROKEN unless you find a specific error. "I haven't read the original" is not BROKEN — it's PENDING with a note.
- Do NOT ask questions. Execute autonomously. Log uncertainties on the blackboard.
