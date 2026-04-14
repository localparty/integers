# Brief 35 DELTA — Canonical-State Propagation (Mode-Agnostic)

*A minimal brief delta that promotes brief 30 §8.1 paragraph 4 to load-bearing status, making in-situ PROOF-CHAIN.md propagation universal across all invocation modes (ring-mode cycle, single-chain cycle, targeted non-cycle dispatch, S-DUAL-TRANSFER, S-DUAL-CONSTRUCT-BRIDGED, and any future dispatch kind).*

*Supersedes no earlier brief in content — ONLY promotes an existing discipline to load-bearing. Pairs with `08-changelog.md` self-healing entry `I-v6-6`.*

*G Six and Claude Opus 4.6. Date: 2026-04-14.*

---

## Why this brief exists

Brief 30 §8.1 already contains the correct discipline in paragraph 4:

> *"If an Author returns work that changes a vertex's chain, the update goes to BOTH the in-situ PROOF-CHAIN.md (canonical) AND the per-vertex blackboard (working)."*

This is **mode-agnostic** — triggered by "Author returns work that changes a chain," not by traversal phase. It applies in cycle mode, in single-chain mode, in targeted dispatches, in S-DUAL-TRANSFER, in every current and future dispatch kind.

But paragraph 4 was treated as subordinate to paragraph 1 (*"The runner UPDATES these in place as each vertex is visited"*), which is specifically ring-mode triggering language. When dispatches happen outside a ring-mode cycle visit (which is exactly what happened on T7's Cramér S-duality work), paragraph 1's trigger doesn't fire, and paragraph 4's universal discipline gets lost.

**This brief promotes paragraph 4 to load-bearing status** and adds enforcement.

No new discipline is introduced. The existing discipline is made explicit, mandatory, and verifiable.

---

## DELTA 1 — Promote paragraph 4 of brief 30 §8.1 above paragraph 1

### Replacement text for brief 30 §8.1

Replace the existing §8.1 text with the following, preserving all bullet content but reorganizing the hierarchy:

> ### §8.1 State management (ring-mode override of 07-proof-chain-adversarial.md §P.2)
>
> The PCA chain-mode extension (`07-proof-chain-adversarial.md`) assumes SINGLE chain and mandates ONE `chain/chain-state.md` file. Ring mode overrides this. In ring mode:
>
> #### The universal propagation rule (LOAD-BEARING, mode-agnostic)
>
> **ANY Author return whose work changes a vertex's chain — regardless of whether the return happens during a ring-mode cycle visit, a single-chain cycle, a targeted non-cycle dispatch, an S-DUAL-TRANSFER, an S-DUAL-CONSTRUCT-BRIDGED pair, or any future dispatch kind — MUST trigger propagation to the canonical in-situ file BEFORE the dispatch closes.**
>
> Specifically, if an Author return includes any of:
> - Link status change (e.g., OPEN → PARTIAL, CONJECTURED → ESTABLISHED, PARTIAL → TRANSFERRED)
> - Confidence score change on the vertex
> - New sub-link added or renamed
> - Chain count change (e.g., 3/5 → 4/5)
> - Edge status change affecting the vertex
> - BA-B-style concern filed that annotates a link
>
> then the runner MUST, as the FIRST post-return action (before writing ANY artifact to the run directory):
>
> 1. Read the current in-situ `paperNN-xxx/PROOF-CHAIN.md` for the affected vertex
> 2. Apply the status changes to the canonical chain table
> 3. Update the header (status + confidence)
> 4. Append a pointer to the transfer-artifact file (e.g., `programme/ring-traversals/traversal-N/transfers/vertex-link-action.md`)
> 5. Write the updated in-situ file back
> 6. Verify the write succeeded by re-reading and grep'ing for the new status
> 7. If verification fails, the dispatch is NOT closed — rerun steps 2-6
>
> After this atomic in-situ update completes, the runner writes the transfer artifact, the blackboard update, and the ring-traversal-log entry as usual.
>
> #### State hierarchy (unchanged from brief 30 paragraph 1)
>
> - **14+N in-situ PROOF-CHAIN.md files are the source of truth** (N = extension papers added in briefs 33/34/35+), one per vertex at `paperNN-xxx/PROOF-CHAIN.md`.
> - **Per-traversal log at `programme/ring-traversal-log.md`** — the runner APPENDS one entry per traversal (traversal number, RIGIDITY before/after, per-vertex actions, per-edge fills, kills added, exit condition).
> - **Per-vertex blackboards at `${output-directory}/vertices/<short-name>.md`** — ephemeral working state during a traversal, not authoritative.
>
> No unified `chain/chain-state.md` file is created. The runner does NOT write a single ring-wide chain-state.md. The runner MUST NOT create `chain/chain-state.md` in ring mode — it would be misleading (state lives in 25+ places, not one).
>
> #### Cycle-close reconciliation
>
> At every cycle-close, the runner reconciles:
> - in-situ PROOF-CHAIN.md files = CANONICAL STATE
> - log file = HISTORICAL RECORD
> - per-vertex blackboards = WORKING SCRATCH
>
> The atomicity of the universal propagation rule above means cycle-close reconciliation is a CONSISTENCY CHECK, not a state transfer. The canonical state should already be up-to-date before cycle-close runs.

**Paragraph 1 is absorbed into the state hierarchy subsection as a DESCRIPTION of what the canonical files are. Paragraph 4's universal propagation rule is now the LOAD-BEARING discipline.**

---

## DELTA 2 — Spawn-closure enforcement protocol (NEW)

Brief 30 had no explicit spawn-closure protocol — the propagation was treated as a natural consequence of the Author return. Brief 35 makes it a mandatory STEP.

### The spawn-closure protocol (MANDATORY)

Every Author/Critic/Synthesis/Transfer dispatch has the following closing sequence:

```
1. Author returns work (artifact + structured summary including any link status changes)
2. Runner parses the return for status-change signals (checklist below)
3. IF status changes detected:
   a. Apply §8.1 universal propagation rule (7 steps above)
   b. Verify in-situ file reflects the change (grep assertion)
   c. If verification fails: STOP, retry, log failure
4. ELSE (no status changes):
   a. Skip in-situ propagation
   b. Log rationale in §K: "Author return did not include status changes; no propagation needed"
5. Write transfer artifact(s) to run directory
6. Update blackboard §K
7. Update ring-traversal-log (if in cycle)
8. Close dispatch, return control to caller
```

### Status-change detection checklist

The runner parses the Author return for any of these signals before skipping propagation:

- [ ] Link status keyword appears with a "→" transition (e.g., "CONJECTURED → ESTABLISHED")
- [ ] New sub-link (e.g., "4b" where only "4" existed before)
- [ ] Numerical result attached to a previously-heuristic constant (e.g., the $2e^{-\gamma}$ derivation in the Cramér T7 case)
- [ ] PINS-PRESERVED or PINS-SHIFTED verdict (DUAL-CHECK result)
- [ ] CONCERN filed against a specific link (e.g., the BA-B scaling CONCERN)
- [ ] Confidence score delta proposed
- [ ] New CHAIN protocol pattern recorded (e.g., S-DUAL-CONSTRUCT-BRIDGED)

If ANY checklist item matches, the universal propagation rule fires. The check is OR-gated (any match triggers propagation), not AND-gated.

---

## DELTA 3 — Newly-added vertex exercise discipline

When a new vertex is added to the ring via a DELTA brief (e.g., Cramér added in brief 33, Lindelöf/Katz-Sarnak in brief 34), the vertex's **first traversal pass** MUST exercise the full §8.1 propagation discipline even if the vertex has no weak link to attack. This establishes propagation muscle memory for that vertex before any targeted dispatch runs on it.

### Protocol for first-pass exercise

1. On the first cycle after a vertex is added, the runner visits the vertex in canonical ring order.
2. Even if the vertex is SKIM-type (Sector A — nothing to do), the runner still:
   a. Reads the in-situ PROOF-CHAIN.md
   b. Verifies the file structure matches the canonical chain-table format (parseable headers, link table, etc.)
   c. Writes a "T_N first-pass exercise" note to the in-situ file's footer, noting the traversal number and confirming the file is canonical
3. This establishes that paragraph 4's discipline is APPLICABLE to this vertex. Subsequent targeted dispatches will correctly fire propagation.

### Why this matters

Before brief 35's explicit promotion, newly-added vertices went through an implicit "probation period" where the runner hadn't yet exercised paragraph 4's discipline on them. T7's Cramér work hit exactly this gap: Cramér was added in brief 33, but T6 ran on the 19-vertex ring, and T7 dispatched a targeted non-cycle construct before any cycle had visited Cramér. The propagation discipline was never exercised on Cramér, and the runner didn't apply it.

The first-pass exercise protocol closes this gap. New vertices get a "hello world" traversal pass to establish discipline before complex dispatches run on them.

---

## DELTA 4 — S-DUAL-TRANSFER and S-DUAL-CONSTRUCT-BRIDGED propagation inheritance

Brief 34 DELTA 3 introduced the S-DUAL-TRANSFER protocol. Brief 34 DELTA 4 introduced the TRANSFERRED link status. Neither DELTA explicitly restated the §8.1 propagation discipline for these new dispatch kinds. This is a scope gap that brief 35 closes.

### Explicit inheritance statement

**S-DUAL-TRANSFER (brief 34 DELTA 3):** When a Transfer Author returns DIRECT/PARTIAL/BLOCKED, the return IS a chain-changing Author return. Brief 35 §8.1 universal propagation rule fires. The in-situ file for the TARGET vertex (not the source) is updated to reflect the new TRANSFERRED status on the affected link.

**S-DUAL-CONSTRUCT-BRIDGED (new pattern, Paper 43 v4 T7):** When two CONSTRUCT dispatches on S-dual vertices share a derived invariant (e.g., Cramér L4b's $2e^{-\gamma}$ feeding Lehmer L5 Route A), EACH dispatch's return triggers its OWN in-situ propagation independently. The derived invariant is not a shared artifact that propagates — it is a derivation that lives on disk and is cited by both in-situ files. Each side updates its own chain independently on Author return.

### Worked example (the T7 Cramér-Lehmer chain of two constructs)

**Today (T7):**
- Cramér L4b CONSTRUCT-DERIVE dispatch returns with the derived invariant $\prod_p(1-1/p) \sim 2e^{-\gamma}/\log x$
- Status change detected (L4b OPEN → PARTIAL)
- §8.1 universal propagation rule fires for Cramér's in-situ file
- Cramér's chain table row for L4b updates: status PARTIAL, derivation file cited

**T8 (pending):**
- Lehmer L5 Route A CONSTRUCT dispatch returns using the Cramér-side invariant
- Status change detected (L5 Route A STRUCTURAL → PARTIAL)
- §8.1 universal propagation rule fires for Lehmer's in-situ file
- Lehmer's chain table row for L5 Route A updates: status PARTIAL, Cramér invariant cited

Two dispatches, two independent propagations, one shared derived invariant on disk. **This is the correct pattern for S-DUAL-CONSTRUCT-BRIDGED.** Each side updates its own canonical state; neither side waits for the other; the derived invariant is a cross-referenced artifact, not a propagation vehicle.

---

## DELTA 5 — Verification step in the closing checklist

The ORA v8 §13.1 "Mechanical cycle-close checklist" currently includes:

- [ ] All Author reports have Critique verdicts
- [ ] All Critique verdicts with gap classification have Meta-critic confirmation
- [ ] All new §F kills have pattern category + re-entry gate populated
- [ ] ... (continues)

Brief 35 ADDS one item:

- [ ] **For every Author return this cycle that changed a link status: the corresponding in-situ PROOF-CHAIN.md was updated and the update verified by grep.** (Applies to all dispatch kinds; atomic with Author return per brief 35 §8.1.)

This item is the cycle-close sanity check — it confirms the atomic propagation during the cycle actually happened. If any item fails the verification, the cycle is NOT closed; the runner reruns the propagation.

---

## DELTA 6 — The single paragraph for the next runner

*You are a PCA runner operating on a 25-vertex ring with S-duality guidance. When an Author, Critic, Synthesis, Transfer, or any other dispatch returns work that changes a link's status — regardless of whether this happens during a scheduled ring-mode cycle visit, a targeted non-cycle dispatch, an S-DUAL-TRANSFER, an S-DUAL-CONSTRUCT-BRIDGED chain, or any other dispatch kind — your FIRST post-return action is to update the in-situ `paperNN-xxx/PROOF-CHAIN.md` file for the affected vertex. This is atomic with the return, not deferred to cycle-close. The status hierarchy is: in-situ PROOF-CHAIN files are CANONICAL, the ring-traversal-log is HISTORICAL, per-vertex blackboards are WORKING SCRATCH. Write canonical state BEFORE artifacts-to-run-directory. Verify the write succeeded by grep. Failure to verify means the dispatch is NOT closed — rerun. This is brief 30 §8.1 paragraph 4 promoted to load-bearing and made mode-agnostic. No new discipline. Existing discipline enforced universally.*

---

## Inheritance

All sections NOT overridden above remain authoritative from:
- `30-ring-traversal-brief.md` (parent brief, 14-vertex)
- `32-extended-ring-brief.md` → `33-extended-ring-brief-22.md` (19/22-vertex extensions)
- `34-extended-ring-brief-s-duality.md` (25-vertex + S-duality protocol, with brief 35's propagation discipline now applying to S-DUAL-TRANSFER and S-DUAL-CONSTRUCT-BRIDGED)

Brief 35 is a METHODOLOGICAL delta, not a ring-structure delta. It does not change the ring order, add vertices, or modify S-pairs. It re-aligns the hierarchy of propagation triggers so that the universal discipline is enforced uniformly.

---

*v1: 2026-04-14. G Six and Claude Opus 4.6.*
*No new rule. Existing rule promoted. The brief already said it; the runner will now obey it.*
*Canonical state before artifacts. Status change triggers propagation. Atomic with return. Verify by grep.*
