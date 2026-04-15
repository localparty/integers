# W11-27: L3-phase3.md Fixup 1 Status Memo

**File edited:** `research/appendix-L/L3-phase3.md`
**Agent:** W11-27 (sole owner during Wave 11)
**Date:** 2026-04-08
**Task:** Append Appendix N pointers to 17 raw "Paper X" citations (from W10-25 audit)

## N-section number verification

Verified against actual `research/appendix-N/N-qg5d-infrastructure.md`:

| Result                                    | N section |
|:------------------------------------------|:----------|
| Heat kernel factorisation                 | §N.1.3    |
| Theorem K.1 (Epstein vanishing)           | §N.1.5    |
| Proposition 3.1 (Z_2 cancellation)        | §N.2.2    |
| Lemma A2 / Poisson bridge (Lemmas A1--A3) | §N.2.3    |
| Theorem 1 (Goroff--Sagnotti)              | §N.2.4    |
| Theorem 4.3 (Weyl anomaly)                | §N.2.5    |

All six match the W10-25 audit mapping; no renumbering needed.

## The 17 applied changes

| # | Line | Before (key phrase)                                         | After (appended)                              |
|---|-----:|:------------------------------------------------------------|:----------------------------------------------|
|  1 |   99 | `By Paper 1, Appendix S, Section S.3.1`                     | `... Section S.3.1 (Appendix N, §N.1.3)`      |
|  2 |  155 | `established in the preprint and in Paper 10`               | `... in Paper 10 (Appendix N)`                |
|  3 |  203 | `By Appendix K, Theorem K.1 (Paper 1, Section K.7b)`        | `... Section K.7b; Appendix N, §N.1.5`        |
|  4 |  219 | `By Paper 10, Section 3.3, Proposition 3.1`                 | `... Proposition 3.1 (Appendix N, §N.2.2)`    |
|  5 |  225 | `scheme-independent (Paper 10, Section 3.4)`                | `... Section 3.4; Appendix N, §N.2.2`         |
|  6 |  233 | `By Paper 10, Theorem 1, Section 4.6`                       | `... Section 4.6 (Appendix N, §N.2.4)`        |
|  7 |  246 | `(Paper 10, Theorem 4.3)` (Lemma L.3.6 proof)               | `... Theorem 4.3; Appendix N, §N.2.5`         |
|  8 |  325 | `(Paper 10, Theorem 4.3)` (Step 1 of L.3.7)                 | `... Theorem 4.3; Appendix N, §N.2.5`         |
|  9 |  543 | `(Paper 10, Proposition 3.1)` (Step 6 Z_2 confirmation)     | `... Proposition 3.1; Appendix N, §N.2.2`     |
| 10 |  893 | `Lemma A2 (Paper 10, Section 5.2b)` (Argument A.4)          | `... Section 5.2b; Appendix N, §N.2.3`        |
| 11 |  900 | `Lemma L.3.5 (Paper 10, Proposition 3.1)` (B.1)             | `... Proposition 3.1; Appendix N, §N.2.2`     |
| 12 |  904 | `(Eq. (Z.1) of Paper 10, Section 3.2)`                      | `... Section 3.2; Appendix N, §N.2.2`         |
| 13 |  930 | `Lemma A2 (Paper 10, Section 5.2b)` (Remark L.3.9)          | `... Section 5.2b; Appendix N, §N.2.3`        |
| 14 |  932 | `mixed-sector gap of Paper 10, Section 3.6`                 | `... Section 3.6 (Appendix N, §N.2.2)`        |
| 15 |  958 | `Paper 10, Thm 1` (in boxed summary diagram)                | `Paper 10, Thm 1 (Appendix N, §N.2.4)`        |
| 16 |  985 | `Section 4.5; Paper 10` (in boxed summary diagram)          | `Section 4.5; Paper 10 (Appendix N)`          |
| 17 |  994 | `Paper 10 (Theorems 1, 4.3)` (H4-conditional results)       | `... Theorems 1, 4.3; Appendix N, §N.2.4-N.2.5` |

Note: items 13 and 14 sit in a shared 6-line `**Remark L.3.9.**` block and
were applied in a single `Edit` call covering both sentences.

## Verification

Grep `Paper [0-9]` in the edited file: **17 matches** (exact audit count).
Grep `Appendix N`: **17 matches**.

Every single "Paper X" citation in `L3-phase3.md` now has a companion
"Appendix N" pointer in the same sentence (most on the same line; lines
99 and 325 have the companion pointer on the immediately following
continuation line within the same sentence, which complies with the
"within the same line or paragraph" criterion).

## Constraints honored

- No original "Paper X" references removed.
- No sentences rewritten; each edit is a pure append inside the existing
  parenthetical (or a single parenthetical inserted alongside it).
- No Lemma / equation numbering touched.
- No files other than `L3-phase3.md` and this memo modified.

## Status: COMPLETE
