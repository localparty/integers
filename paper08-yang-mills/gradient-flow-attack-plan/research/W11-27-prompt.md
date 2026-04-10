# W11-27: Fixup 1 for L3-phase3.md (17 citations)

## Task
Apply Fixup 1 to ONE file: `appendix-L/L3-phase3.md`. Add Appendix N pointers to 17 raw "Paper X" citations identified by the Wave 10 audit. You own this file — no other agent will edit it during Wave 11.

## The 17 citations (from W10-25 audit table)

| Line | Current citation | Add pointer to |
|:-----|:----------------|:---------------|
| 99 | "By Paper 1, Appendix S, Section S.3.1" | Appendix N, §N.1.3 (heat kernel factorization) |
| 155 | "established in the preprint and in Paper 10" | Appendix N |
| 203 | "By Appendix K, Theorem K.1 (Paper 1, Section K.7b)" | Appendix N, §N.1.5 |
| 219 | "By Paper 10, Section 3.3, Proposition 3.1" | Appendix N, §N.2.2 |
| 225 | "(Paper 10, Section 3.4)" | Appendix N, §N.2.2 |
| 233 | "By Paper 10, Theorem 1, Section 4.6" | Appendix N, §N.2.4 |
| 246 | "(Paper 10, Theorem 4.3)" | Appendix N, §N.2.5 |
| 325 | "(Paper 10, Theorem 4.3)" | Appendix N, §N.2.5 |
| 543 | "(Paper 10, Proposition 3.1)" | Appendix N, §N.2.2 |
| 893 | "Lemma A2 (Paper 10, Section 5.2b)" | Appendix N, §N.2.3 |
| 900 | "(Paper 10, Proposition 3.1)" | Appendix N, §N.2.2 |
| 904 | "(Eq. (Z.1) of Paper 10, Section 3.2)" | Appendix N, §N.2.2 |
| 930 | "Lemma A2 (Paper 10, Section 5.2b)" | Appendix N, §N.2.3 |
| 932 | "mixed-sector gap of Paper 10, Section 3.6" | Appendix N, §N.2.2 |
| 958 | "Paper 10, Thm 1" | Appendix N, §N.2.4 |
| 985 | "Paper 10" (in summary diagram) | Appendix N |
| 994 | "Paper 10 (Theorems 1, 4.3)" | Appendix N, §N.2.4-N.2.5 |

## Critical first step
**Read `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md` to verify the EXACT section numbers in the actual N file.** The mapping above is from the audit memory; the actual N file may use slightly different numbers (e.g., §N.1.5 might actually be §N.1.6). USE THE ACTUAL FILE'S NUMBERS.

## How to apply each fix
For each citation, use the Edit tool to APPEND (not replace) the Appendix N pointer. Format:
- Before: `Theorem K.1 of Paper 1`  
- After: `Theorem K.1 of Paper 1 (Appendix N, §N.x)`

Do not remove the original "Paper X" reference. Only append the pointer.

For citations that lack a sufficiently unique surrounding context, use a few lines of context in the Edit tool's `old_string` parameter.

## What you must NOT do
- Don't remove the original "Paper X" citations
- Don't rewrite any sentences
- Don't touch any other file
- Don't change Lemma numbering or equation numbering (that's other agents' jobs)

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md` (for exact N numbers)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W10-25-final-audit.md` (for full audit context)

## What to write
1. Edit `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L3-phase3.md` (multiple Edit calls)
2. Status memo: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W11-27-l3-fixups.md` — list each change with line numbers and before/after

## Verification
After all 17 changes, run a grep for `Paper [0-9]` in L3-phase3.md and verify EVERY occurrence is followed (within the same line or paragraph) by "Appendix N". Report the count: should be 17 (or higher if there were Paper references not in the audit list — those still need pointers).
