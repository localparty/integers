# Agentic Referee-Fix-Verify Pipeline

## Architecture

Three-phase pipeline using two models for cross-verification, with
auto-commit gates between phases. **Commits happen only after a
phase verifies clean.** If a phase finds issues that cannot be
fully resolved, the pipeline halts and surfaces the problem.

```
┌────────────────────────────────────────────────────────────────┐
│ Phase 1a: REFEREE (Opus max effort)                            │
│   Input:  19-focused-referee-opus.md                           │
│   Output: hot-zone reports + summary                           │
│   Commit: NONE (read-only audit)                               │
└────────────────────────────────────────────────────────────────┘
                           ↓
┌────────────────────────────────────────────────────────────────┐
│ Phase 1b: FIX (same Opus session)                              │
│   Input:  "thanks now address each gap"                        │
│   Output: surgical edits to preprint                           │
│   Commit: NONE — wait for Phase 2 verification                 │
└────────────────────────────────────────────────────────────────┘
                           ↓
┌────────────────────────────────────────────────────────────────┐
│ Phase 2: VERIFY (Sonnet, fresh session)                        │
│   Input:  20-surgical-verify-sonnet.md                         │
│   Action: git diff → check each hunk for:                      │
│           - dimensional errors                                  │
│           - inequality direction                                │
│           - reference accuracy                                  │
│           - stale-copy regression (grep changed formulas)      │
│           - consistency with surrounding text                   │
│   Output: verify-cN.md + direct fixes if any                   │
│   Gate:   if all VERIFIED → proceed to commit                  │
│           if errors found and fixed → re-run Phase 2 once      │
│           if errors found and NOT fixable → HALT              │
└────────────────────────────────────────────────────────────────┘
                           ↓
┌────────────────────────────────────────────────────────────────┐
│ Phase 3: COMMIT + META-VERIFY (Opus, original session)         │
│   Action: Read Sonnet's verify-cN.md                           │
│   If clean: commit with descriptive message, declare cycle     │
│             converged                                           │
│   If issues remain: HALT, do not commit, surface to user       │
└────────────────────────────────────────────────────────────────┘
```

## Commit policy

**Auto-commit rule:** Only commit when Phase 2 returns all-VERIFIED
AND Phase 3 (Opus meta-check on Sonnet's report) confirms.

**Halt rule:** Do NOT commit if any of:
- Phase 2 finds an error that Sonnet cannot self-fix
- Phase 3 disagrees with Phase 2's verdict
- A fix touches a load-bearing claim (the proof chain
  $\Delta_0^{\text{KK}} > 0 \to \Delta_0^{\text{std}} > 0 \to
  \Delta_\infty > 0$)
- Any file outside `preprint/sections/` is modified unexpectedly

**Commit message format:**
```
Cycle N (scope): K real fixes, M fix-errors caught by Sonnet

- <one line per fix>
- Verify report: math-referee/verify-cN.md
```

## Why two models?

- **Opus** is better at deep mathematical reasoning and structural
  analysis. It catches logical gaps and conceptual errors (e.g., the
  rank-8 vs rank-1 error for $E_8/\mathrm{SO}(16)$, the F3
  thermodynamic limit circularity).
- **Sonnet** is better at fast, precise algebraic verification and
  cross-referencing. It catches formula typos and stale copies (e.g.,
  the 4 stale references after the $s \to s{-}1$ change in cycle 8,
  the arithmetic error $30 \times 248/(2 \times 128) \neq 30$).
- Using both means each model catches the other's blind spots.
- The "fix introduces new error" pattern is broken because every fix
  is immediately verified by a different model BEFORE being committed.

## Convergence criteria

A cycle is **converged** when:
1. Phase 1 finds 0 substantive issues, OR
2. Phase 1 finds issues, all are fixed, and Phase 2 returns clean

The pipeline as a whole has **converged** when 3 consecutive cycles
on different scopes return clean.

Historical convergence (cycles 1-8):
- Cycle 1: 4 issues found, 4 fix-errors caught, fixed
- Cycle 2: 0 issues (hot zones re-verify) — CLEAN
- Cycle 3: 7 issues found, 0 fix-errors, fixed
- Cycle 4: 2 cross-file mismatches, fixed
- Cycle 5: 0 issues (edge cases) — CLEAN
- Cycle 6: 0 issues (proof chain) — CLEAN
- Cycle 7: 0 issues (deep spectral lemma) — CLEAN
- Cycle 8: 5 issues found, 4 fix-errors caught, fixed

## Cycle scopes (for sequential planning)

| Cycle | Scope | Prompt source |
|-------|-------|--------------|
| 1     | 8 hot zones (algebra audit) | 19-focused-referee-opus.md |
| 2     | Hot zones re-verify | 19-focused-referee-opus.md |
| 3     | Cold-zone appendices | inline (cold-zone sweep) |
| 4     | Cross-file formula consistency | inline (8 key formulas) |
| 5     | Edge cases (N=2, k=0, k→∞, large N, L→∞) | inline |
| 6     | Proof chain walkthrough (7 links) | inline |
| 7     | Deep spectral lemma (line-by-line) | inline |
| 8     | Deep Section 5.7 (line-by-line) | inline |
| 9     | Reference accuracy sweep (every citation) | TBD |
| 10    | Adversarial (try to break the proof) | TBD |
| 11+   | Re-runs of converging cycles for confidence | as needed |

## Session continuation

When resuming after a break (e.g., new credit window):
1. Read this file and `19-focused-referee-opus.md`, `20-surgical-verify-sonnet.md`
2. Read the latest `math-referee/` reports to see where we left off
3. Run `git log --oneline -10` to see recent commits
4. Pick up at the next cycle in the sequence above

## How to run a cycle (revised, with auto-commit)

```bash
# Phase 1a: Opus referee
claude --model opus --effort max
# user: "read /Users/gsix/yang-mills/etc/19-focused-referee-opus.md and execute"
# wait for reports

# Phase 1b: Opus fix (same session)
# user: "address each gap surgically"
# wait for edits

# Phase 2: Sonnet verify (fresh session, NEW agent)
# user: "read /Users/gsix/yang-mills/etc/20-surgical-verify-sonnet.md and execute"
# wait for verification + any self-fixes

# Phase 3: Back in Opus session, paste Sonnet's report
# Opus: meta-verifies, then either:
#   - COMMITS automatically with the cycle-N message format, OR
#   - HALTS and surfaces the issue to the user
```

## Tracking

Each cycle produces:
- `math-referee/` reports (Opus and Sonnet outputs)
- One git commit per cycle (after Phase 3 clean)
- Updated convergence table in this file

The pipeline is fully auditable via git history.
