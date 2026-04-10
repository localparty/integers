# Wave 11 Execution Strategy: Fixups

*How to launch the three fixups identified by the Wave 10 audit.*
*Companion to `14-fixups-n-section-coverage-citations-and-equation-numbering.md`*
*(the spec). This document is the launch plan.*

*Date: 2026-04-08*

---

## 0. What This Document Is

**Spec (file 14):** What needs to change and why.
**Strategy (this file):** How to launch agents to do it.

The spec already decided:
- Fixup 3: Option (b) — update L.0 / L.5 references rather than expand Appendix N
- Fixup 1: Append Appendix N pointers, don't replace Paper X citations
- Fixup 2: Renumber L.1 equations from flat to hierarchical
- Sequential constraint: Fixup 3 first (it changes the target structure for Fixup 1)
- Recommended agent count: single agent, sequential

This document calibrates that recommendation against our 25-agent
multi-wave precedent and produces a concrete launch plan.


---


## 1. Single Agent or Multi-Agent?

The spec recommends a single sequential agent. Let me reconsider in
light of Waves 1-10.

### What argues for single-agent

- Total effort is small (~60 min wall-clock)
- All three fixups touch the same set of files
- Coordination overhead between agents is real (the analyticity-in-t
  numerical script in Wave 1 had Combes-Thomas convention errors that
  W2-07 caught — a parallel agent could create similar issues)
- The fixups are sequential anyway: Fixup 3 must finish before Fixup 1
  can map to the right N sections

### What argues for multi-agent

- Fixups 1 and 2 are independent of each other once Fixup 3 is done
- The spec acknowledges parallel execution saves ~15 minutes
- Wave 9's 7-agent parallel run showed no coordination issues when
  agents wrote to different files

### Decision

**Single agent, sequential.** Confirmed.

The reason: Fixups 1 and 2 both edit the same `L1-phase1.md` file
(Fixup 1 changes 3 citations there; Fixup 2 renumbers 24 equations
there). Two agents editing the same file in parallel is a coordination
trap. Better to do them sequentially in one agent.

This is **Wave 11**, single agent: `W11-26`.


---


## 2. Wave 11 Plan

### Slot W11-26: Three sequential fixups + re-audit

| Phase | Task | File(s) | Effort |
|:------|:-----|:--------|:-------|
| 1 | Fixup 3: Update §§N.6-N.10 references in L.0/L.5 | `L0-L5-L6-L7.md` | 15 min |
| 2 | Fixup 1: Add Appendix N pointers next to Paper X citations | `L1-phase1.md`, `L3-phase3.md`, `L4-phase4.md` | 30 min |
| 3 | Fixup 2: Renumber L.1 equations (flat → hierarchical) | `L1-phase1.md` | 15 min |
| 4 | Re-audit: re-run Wave 10's 10 checks | (read-only) | 15 min |
| | **Total** | | **~75 min** |

The agent must complete each phase before starting the next:
- Phase 1 changes the target structure (which N sections exist),
  needed for Phase 2's mapping.
- Phase 2 modifies `L1-phase1.md`, which Phase 3 also modifies — must
  be sequential to avoid edit conflicts on the same file.
- Phase 4 verifies the outcome of all three.


---


## 3. The Mapping Lookup (Critical for Phase 2)

The spec's Section 2.2 gives a candidate mapping for Fixup 1, but the
exact Appendix N section numbers must come from the **actual**
`N-qg5d-infrastructure.md` file (575 lines, written by W9-23).

The agent must:

1. **Read `N-qg5d-infrastructure.md` first.** Build a lookup table from
   QG5D result name → exact N section number.

2. **For each "Paper X" citation in L.1, L.3, L.4:** identify which
   QG5D result it cites and look up the N section in the table.

3. **Append the pointer:** change `Paper X (Y)` to
   `Paper X (Y); Appendix N, §N.k`.

The audit (W10-25) found 21 instances. The mapping is from W10-25
itself — the audit listed the file, line, and intended N section for
each. The agent should use that table as the starting point and verify
each entry against the actual N file.


---


## 4. Quality Gate (Phase 4)

After all three fixups, the re-audit runs the same 10 checks from
Wave 10. Expected results:

| Check | Wave 10 result | Wave 11 expected |
|:------|:---------------|:-----------------|
| 1. Dependency chain | PASS | PASS (unchanged) |
| 2. QG5D citation consistency | **ISSUE (21 raw)** | **PASS (0 raw)** |
| 3. H4-conditional flagging | PASS | PASS (unchanged) |
| 4. PROOF-CHAIN consistency | PASS | PASS (unchanged) |
| 5. Abstract/conclusion/IV.5 | PASS | PASS (unchanged) |
| 6. Stale language | PASS | PASS (unchanged) |
| 7. Notation consistency | PASS | PASS (unchanged) |
| 8. Equation numbering | PASS (with note) | **PASS (cleaner)** |
| 9. Completeness (19 lemmas) | PASS | PASS (unchanged) |
| 10. Sub-clause coverage | PASS | PASS (unchanged) |

Plus three Wave-11-specific checks:

| Check | Expected |
|:------|:---------|
| Search `§N\.[6-9]` or `§N\.10` in `appendix-L/` | 0 matches |
| Search `Paper [0-9]` not followed by `Appendix N` in `appendix-L/` | 0 matches |
| Search flat `\\tag{L\.[0-9]+}` (not preceded by `1\.`) in `L1-phase1.md` | 0 matches |

If all 13 pass: **READY FOR ASSEMBLY**.

If any fail: agent reports the failure, lists the remaining issues,
and we decide whether to launch a Wave 11.5 fixup pass.


---


## 5. The Agent Prompt (Concrete)

The agent receives:

1. **Spec document:** `strategy/14-fixups-...numbering.md` (the existing one)
2. **Audit report:** `research/W10-25-final-audit.md`
3. **Working files:**
   - `appendix-L/L0-L5-L6-L7.md`
   - `appendix-L/L1-phase1.md`
   - `appendix-L/L2-phase2.md` (read-only, for cross-reference)
   - `appendix-L/L3-phase3.md`
   - `appendix-L/L4-phase4.md`
   - `appendix-N/N-qg5d-infrastructure.md` (read-only)

4. **Instruction:** Execute Phases 1, 2, 3, 4 sequentially. After each
   phase, write a one-paragraph status to the output memo. After
   Phase 4, write the re-audit table and final verdict.

5. **Output:** `research/W11-26-fixups-and-reaudit.md`

6. **Style rules:**
   - Use `Edit` tool, not `Write` (preserves the rest of the file)
   - One Edit call per change for Fixup 1 and Fixup 2 to keep the
     audit trail clean
   - Before each Edit, verify the `old_string` is unique in the file
     (use a few lines of context if not)
   - Do NOT remove the original "Paper X" citation in Fixup 1 — only
     append the Appendix N pointer


---


## 6. What NOT to Do (Wave 11 Edition)

The spec already lists what not to do for each fixup. Two more rules
specific to the agent execution:

1. **Don't rewrite paragraphs.** Even if a sentence reads awkwardly
   after the citation append, leave it. The fixup is mechanical;
   stylistic improvements are out of scope.

2. **Don't touch the research memos.** `W1-01` through `W10-25`
   are frozen. Only `appendix-L/`, `appendix-N/`, and the new
   `W11-26-fixups-and-reaudit.md` may be edited.

3. **Don't expand Appendix N.** Option (a) is rejected. Appendix N
   stays at §§N.0-N.5.

4. **Don't change Lemma numbering.** The Lemma L.1.1, L.1.2, ...,
   L.4.3 sequence is final. Only equation numbers in L.1 change
   (L.1 → L.1.1, L.2 → L.1.2, etc.).

5. **Don't introduce new cross-references.** If a Paper X citation
   has no corresponding N section, leave it as raw "Paper X" — don't
   invent a new N section. (The audit found 21 instances; all 21
   should map to existing N.1-N.5 entries.)


---


## 7. Decision Points and Escalation

### Decision point 1: After Phase 1 (Fixup 3)

**Question:** Did all §§N.6-N.10 references get updated?

**Check:** `grep -E '§N\\.[6-9]|§N\\.10' appendix-L/L0-L5-L6-L7.md`

**If clean:** Continue to Phase 2.
**If not:** Escalate. Report the remaining references and STOP.

### Decision point 2: After Phase 2 (Fixup 1)

**Question:** Did the Appendix N pointers get added correctly?

**Check:** Sample 5 of the 21 changed lines and verify the format:
`Paper X (Y); Appendix N, §N.k`

**If correct:** Continue to Phase 3.
**If miscoded:** Report and STOP. Do not start Phase 3 (which would
make rollback harder).

### Decision point 3: After Phase 3 (Fixup 2)

**Question:** Did all 24 equations renumber correctly?

**Check:** `grep -c '\\\\tag{L\\.1\\.[0-9]+}' appendix-L/L1-phase1.md`
should return 24.

**If correct:** Continue to Phase 4.
**If not:** Report which numbers are missing or duplicated. STOP.

### Decision point 4: After Phase 4 (Re-audit)

**Question:** All 13 checks pass?

**If yes:** **READY FOR ASSEMBLY**. Wave 11 done.
**If no:** Report which checks failed. We decide whether to launch
Wave 11.5 or accept the residual issues.


---


## 8. Schedule

```
W11-26 (single agent, sequential)

  Phase 1 ████             15 min   Fixup 3
  Phase 2 ████████         30 min   Fixup 1
  Phase 3 ████             15 min   Fixup 2
  Phase 4 ████             15 min   Re-audit
                           ─────
                           75 min total wall-clock
```

After Wave 11 completes:

| Task | Effort | Total elapsed |
|:-----|:-------|:--------------|
| Wave 11 fixups | 75 min | 75 min |
| Paste preprint update fragments | 15 min | 90 min |
| Assemble Appendix L from sections | 30 min | 120 min |
| Insert Appendix N | 15 min | 135 min |
| Final visual inspection | 30 min | 165 min |

**~2.75 hours from now to a complete Clay Millennium Prize submission.**


---


## 9. Risk Adjustment

The spec's Section 6 lists risks. With single-agent sequential
execution, two risks are reduced:

| Risk | Spec severity | Wave 11 severity |
|:-----|:--------------|:-----------------|
| Fixup 3 missing references | Low | Low (Phase 1 verifies) |
| Fixup 1 wrong N section pointer | Low | Low (mapping table from W10-25) |
| Fixup 2 missed equation reference | Medium | **Low** (single agent owns the file) |
| Re-audit reveals new issue | Low | Low (Phase 4 catches it) |
| Fixup introduces typo | Low | Low (Edit tool, mechanical) |
| **NEW: agent edits wrong file** | --- | Low (file paths in prompt) |
| **NEW: agent rewrites prose** | --- | Low (Section 6 forbids it) |

The single-agent approach eliminates the multi-agent coordination risk
entirely.


---


## 10. Definition of Done (Wave 11)

Wave 11 is complete when:

- [ ] Phase 1: 0 §§N.6-N.10 references remain in `appendix-L/`
- [ ] Phase 2: All 21 raw "Paper X" citations have Appendix N pointers
- [ ] Phase 3: All 24 L.1 equations are L.1.1 through L.1.24
- [ ] Phase 4: 10/10 Wave 10 checks still PASS, plus 3 Wave 11 checks PASS
- [ ] Output memo `W11-26-fixups-and-reaudit.md` exists
- [ ] No stale language introduced
- [ ] No new gaps discovered
- [ ] No mathematics changed

When all boxes are checked, the publication text is **READY FOR
ASSEMBLY** into the preprint.


---


## 11. One Sentence

One agent, four phases, seventy-five minutes — and Appendix L is
internally consistent, fully cross-referenced, and ready to paste
into the final Clay submission.


---


*Spec:* `14-fixups-n-section-coverage-citations-and-equation-numbering.md`
*Audit:* `research/W10-25-final-audit.md`
*Output (when complete):* `research/W11-26-fixups-and-reaudit.md`
