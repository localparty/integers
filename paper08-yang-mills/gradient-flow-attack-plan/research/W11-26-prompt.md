# W11-26: Fixups for L1-phase1.md (Fixup 1 + Fixup 2)

## Task
Apply two mechanical fixups to ONE file: `appendix-L/L1-phase1.md`. Do them SEQUENTIALLY within this agent (Fixup 1 first, then Fixup 2). You own this file — no other agent will edit it during Wave 11.

## Fixup 1: Add Appendix N pointers (3 instances)

The Wave 10 audit identified 3 raw "Paper X" citations in L1-phase1.md that need parallel "Appendix N, §N.x" pointers added. From W10-25 audit:

| Line | Current citation | Add pointer |
|:-----|:----------------|:------------|
| 417 | "Theorem K.1 of Paper 1" | "; Appendix N, §N.1.5" (or whatever Theorem K.1 maps to in actual N file) |
| 527 | "(Theorem K.1, Paper 1)" | "; Appendix N, §N.1.5" |
| 557 | "frozen dilaton (Section 4.1; Theorem K.1, Paper 1)" | "; Appendix N, §N.1.5 + §N.3.1" |

**STEP 1:** Read `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md` to get the EXACT N section numbers for Theorem K.1 (Epstein vanishing) and the frozen dilaton (Theorem F.1 / Proposition A.1 from Paper 6).

**STEP 2:** For each of the 3 citations, use the Edit tool to APPEND (not replace) the Appendix N pointer. Do not remove the original "Paper X" citation.

**Format:** Change `Theorem K.1 of Paper 1` to `Theorem K.1 of Paper 1 (Appendix N, §N.x)`. Use the actual N section number from your Step 1 reading.

## Fixup 2: Renumber L.1 equations from flat to hierarchical

L1-phase1.md uses flat equation numbering (L.1, L.2, ..., L.24). Other L sections use hierarchical (L.2.1, L.3.1, etc.). Rename all 24 L.1 equations.

**STEP 1:** Find all `\tag{L.k}` for k = 1..24 in L1-phase1.md.

**STEP 2:** For each, change `\tag{L.k}` to `\tag{L.1.k}`.

**STEP 3:** Find all body-text references like `(L.k)` or `equation (L.k)` and change to `(L.1.k)`.

**STEP 4:** Verify count: should have exactly 24 instances of `\tag{L.1.k}` for k=1..24, and 0 instances of `\tag{L.k}` (flat).

## What you must NOT do
- Don't remove the original "Paper X" citations (only append the pointer)
- Don't rewrite any sentences
- Don't change Lemma numbering (L.1.1, L.1.2, etc. stay)
- Don't touch any other file

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md` (for the exact N section numbers)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W10-25-final-audit.md` (for the exact citation locations)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/14-fixups-n-section-coverage-citations-and-equation-numbering.md` (for context)

## What to write
1. Edit `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L1-phase1.md` (using Edit tool, multiple calls)
2. Status memo: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W11-26-l1-fixups.md` — list each change made, with line numbers and before/after

## Verification before reporting done
- 3 "Appendix N, §N.x" pointers added (verify by grep)
- 24 `\tag{L.1.k}` (verify by grep)
- 0 flat `\tag{L.k}` for k <= 24 (verify by grep)
- All body-text equation references updated
