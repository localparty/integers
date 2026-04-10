# W11-26b: Resume L1-phase1 Fixup 2 (renumbering only)

## Context
W11-26 partially completed: Fixup 1 (3 Appendix N pointers) is DONE, but the agent crashed with an API error after only renumbering ~1 of 24 equations. This agent resumes Fixup 2 only.

## Task
Renumber the remaining flat-numbered equations in `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L1-phase1.md` from `\tag{L.k}` to `\tag{L.1.k}`.

Current state (from grep):
- 23 flat tags `\tag{L.k}` remain (k = 1..24, minus 1 already converted)
- 1 hierarchical tag `\tag{L.1.k}` already exists
- DO NOT touch the 3 Appendix N pointers (they are already done)

## Step 1: Identify which equations are still flat
Read L1-phase1.md and find every `\tag{L.k}` where k is a single number (1..24). Also identify the one already converted to `\tag{L.1.k}` so you don't double-renumber it.

## Step 2: Renumber the equation tags
For each flat `\tag{L.k}`, change it to `\tag{L.1.k}`. Use the Edit tool with sufficient context. Be careful: if multiple equations on different lines have similar surrounding text, use enough lines of context to make `old_string` unique.

## Step 3: Update body-text equation references
After renumbering the tags, find all body-text references like `(L.k)` or `equation (L.k)` or `Eq. (L.k)` for k = 1..24, and change them to `(L.1.k)`. Search for `(L.1)`, `(L.2)`, ..., `(L.24)` patterns and update each.

CAUTION: Be careful not to replace `(L.1.5)` (already hierarchical) or `(L.2)` if it's actually pointing to a different L section's equation. Equation references inside L1-phase1.md to its OWN equations are the targets — references to L.2 sections or L2 equations are NOT.

A safer approach: search for `\b(L\.([0-9]+))\b` (a single L.k not followed by another dot) inside L1-phase1.md only. For each match where k <= 24, replace with `(L.1.k)`.

## Step 4: Verify
After all edits:
- `grep -c '\\tag{L\.1\.[0-9]' L1-phase1.md` should return 24
- `grep -c '\\tag{L\.[0-9]\+}' L1-phase1.md` should return 0 (no more flat tags)
- The 3 "Appendix N" pointers should still be present (don't touch them)

## What to write
Status memo: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W11-26-l1-fixups.md`

List:
- Confirmation that Fixup 1 (3 pointers) is intact (don't re-add, just verify)
- Each Fixup 2 renumbering with line number and before/after
- Final verification grep counts
- Any body-text references updated

## What you must NOT do
- Don't touch the 3 Appendix N pointers (already correct)
- Don't change Lemma numbering (Lemma L.1.1, L.1.2, etc. are NOT equation tags)
- Don't touch any other file
- Don't restart Fixup 1 (it's done)
