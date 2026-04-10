# W11-28: Fixup 1 for L4-phase4.md (1 citation)

## Task
Apply Fixup 1 to ONE file: `appendix-L/L4-phase4.md`. Add an Appendix N pointer to 1 raw "Paper X" citation identified by the Wave 10 audit. You own this file — no other agent will edit it during Wave 11.

## The citation (from W10-25 audit table)

| Line | Current citation | Add pointer |
|:-----|:----------------|:------------|
| 322 | "Paper 10, Route 05" | Appendix N, §N.2.5 (Weyl anomaly) |

## Critical first step
**Read `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md` to verify the EXACT section number for the Weyl anomaly (Theorem 4.3, Wess-Zumino) in the actual N file.** The audit's §N.2.5 is from memory; verify against the file.

## How to apply
Use the Edit tool to APPEND (not replace) the Appendix N pointer.
- Before: `Paper 10, Route 05`
- After: `Paper 10, Route 05 (Appendix N, §N.x)`

## Bonus: Search for any other Paper X references
While you're in L4-phase4.md, do a grep for `Paper [0-9]` and verify each occurrence either:
(a) Already has an "Appendix N" pointer, or
(b) Gets one added (if missed by the audit).

The audit found only 1 instance, but it's worth confirming there are no others.

## What you must NOT do
- Don't remove the original "Paper X" citation
- Don't rewrite sentences
- Don't touch any other file

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W10-25-final-audit.md`

## What to write
1. Edit `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L4-phase4.md`
2. Status memo: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W11-28-l4-fixups.md` — list the change(s) with line numbers and before/after, plus the result of the bonus grep

## Verification
After the change, grep for `Paper [0-9]` in L4-phase4.md and verify every occurrence has "Appendix N" nearby.
