# W11-29: Fixup 3 for L0-L5-L6-L7.md (§§N.6-N.10 references)

## Task
Apply Fixup 3 to ONE file: `appendix-L/L0-L5-L6-L7.md`. The L.0 theorem and L.5 sub-clause table reference Appendix N sections §§N.6-N.10 that DO NOT EXIST in the actual `N-qg5d-infrastructure.md` (which has §§N.0-N.5 only). You own this file — no other agent will edit it during Wave 11.

## Decision (from spec, file 14): Option (b)
Update L.0/L.5 to reference L sections directly instead of expanding Appendix N. Appendix N stays at §§N.0-N.5 (its purpose is QG5D inputs, not gradient-flow outputs).

## Step 1: Find all §§N.6-N.10 references
Read `appendix-L/L0-L5-L6-L7.md` and search for:
- `§N.6`, `§N.7`, `§N.8`, `§N.9`, `§N.10`
- `§§N.6`, `§§N.7`, etc.
- `Appendix N, §N.6` and similar

List every occurrence with its line number and the surrounding context (what it's trying to reference).

## Step 2: Determine the correct target for each
For each §§N.6-N.10 reference, identify what it's actually trying to point to:

(a) **If it's pointing to a QG5D input** (like Theorem K.1, Proposition 3.1, etc.) → change to the correct EXISTING N section (one of §§N.1-N.5). Read `appendix-N/N-qg5d-infrastructure.md` to find the right number.

(b) **If it's pointing to a gradient-flow lemma** (like Lemma L.3.7, Lemma L.4.1, etc.) → change to the L.x.y reference directly. Example: `Appendix N, §N.6` → `Lemma L.3.7`.

(c) **If it's pointing to the sub-clause map itself** → change to `§L.5` (self-reference).

## Step 3: Apply the edits
Use the Edit tool for each change. Use enough context to make `old_string` unique.

## Step 4: Verify
After all edits, grep `appendix-L/L0-L5-L6-L7.md` for `§N\.[6-9]` or `§N\.10` and confirm 0 matches.

Also grep the OTHER L files (L1, L2, L3, L4) for §§N.6-N.10 — if found, those are OUT OF SCOPE for this agent (they should not exist), but report them in the status memo.

## What you must NOT do
- Don't expand Appendix N (Option (a) is rejected)
- Don't rename §§N.0-N.5 (those are correct)
- Don't change the L.5 table structure (only the references inside it)
- Don't touch any other file (other than reading appendix-N for verification)

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L0-L5-L6-L7.md` (the file you're editing)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md` (to find correct N section numbers)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L1-phase1.md`, `L2-phase2.md`, `L3-phase3.md`, `L4-phase4.md` (for L lemma references — read-only, do not edit)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/14-fixups-n-section-coverage-citations-and-equation-numbering.md` (Section 1 for the Option (b) decision)

## What to write
1. Edit `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L0-L5-L6-L7.md`
2. Status memo: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W11-29-l0-fixup3.md` — list each change with line numbers, the old reference, the new reference, and the reason (option a/b/c above)

## Verification
- 0 matches for `§N\.[6-9]|§N\.10` in `L0-L5-L6-L7.md` after edits
- All L.x.y references in the file are valid (point to lemmas that exist in L1-L4)
- Report any out-of-scope §§N.6-N.10 references found in other L files
