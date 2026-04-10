# W11-29 Status Memo: Fixup 3 for `appendix-L/L0-L5-L6-L7.md`

## Task
Apply Fixup 3 per W11-29-prompt.md, Option (b): replace every reference
to §§N.6-N.10 (which do not exist in `appendix-N/N-qg5d-infrastructure.md`)
with references to existing L sections/lemmas or to the valid §§N.0-N.5.

## Source of truth
- `appendix-N/N-qg5d-infrastructure.md` contains only §§N.0-N.5 (N.0
  Purpose and scope; N.1 Paper 1 Epstein; N.2 Paper 10 Seeley--DeWitt,
  Z_2 parity, Poisson bridge, Weyl anomaly; N.3 Paper 6 frozen dilaton;
  N.4 Paper 4 CP^2 x S^2 x S^1; N.5 Note on gravitational physics).
  These are QG5D inputs; none contain gradient-flow lemmas.
- The gradient-flow lemmas L.x.y actually live in:
  - Lemmas L.1.1--L.1.5 in `L1-phase1.md`
  - Lemmas L.2.1--L.2.4 in `L2-phase2.md`
  - Lemmas L.3.1--L.3.9 in `L3-phase3.md`
  - Lemmas L.4.1--L.4.3 in `L4-phase4.md`

## Edits applied to `L0-L5-L6-L7.md`

### Edit 1 (L.0 stage map, lines 50-56 pre-edit -> 50-63 post-edit)
**Old:**
> The proof chain comprises 19 lemmas (Appendix N, Table N.1) organised
> into four stages: (I) flow well-posedness and small-field preservation
> (Appendix N, \S N.1--N.3), (II) continuum flowed limit (Appendix N,
> \S N.4), (III) composite-operator extraction and stress tensor
> (Appendix N, \S N.5--N.7), (IV) short-distance match and OPE
> (Appendix N, \S N.8--N.9). The dependency graph is a directed acyclic
> graph with no circular dependencies (Appendix N, \S N.10).

**New:**
> The proof chain comprises 21 lemmas (Lemmas L.1.1--L.1.5, L.2.1--L.2.4,
> L.3.1--L.3.9, L.4.1--L.4.3) organised into four stages: (I) flow
> well-posedness and small-field preservation (Section L.1), (II)
> continuum flowed limit at fixed t>0 (Section L.2), (III)
> small-flow-time limit, renormalised composite operators, and stress
> tensor (Sections L.3 and L.4, Lemma L.4.1), (IV) short-distance match
> and leading-order OPE (Section L.4, Lemmas L.4.2--L.4.3). The QG5D
> spectral inputs... are collected in Appendix N, §§ N.1--N.2. The
> dependency graph is a directed acyclic graph with no circular
> dependencies: each lemma depends only on earlier lemmas in the
> L.1 -> L.2 -> L.3 -> L.4 chain together with the QG5D inputs of
> Appendix N.

Individual fixes within this edit:
- `§N.1--N.3` (Stage I) -> `Section L.1`. Reason: **option (b)**. Stage I
  is flow well-posedness, handled by Lemmas L.1.1--L.1.5 in L1-phase1.md.
  The true location is Section L.1, not anything in Appendix N.
- `§N.4` (Stage II) -> `Section L.2`. Reason: **option (b)**. Stage II is
  continuum flowed limit, handled by Lemmas L.2.1--L.2.4 in L2-phase2.md.
- `§N.5--N.7` (Stage III) -> `Sections L.3 and L.4, Lemma L.4.1`. Reason:
  **option (b)**. Stage III = composite-operator extraction (Lemmas
  L.3.1--L.3.9 in L3-phase3.md) + stress tensor (Lemma L.4.1 in
  L4-phase4.md).
- `§N.8--N.9` (Stage IV) -> `Section L.4, Lemmas L.4.2--L.4.3`. Reason:
  **option (b)**. Stage IV = AF match (Lemma L.4.2) + leading-order OPE
  (Lemma L.4.3), both in L4-phase4.md.
- `§N.10` (dependency DAG) -> descriptive sentence "each lemma depends
  only on earlier lemmas in the L.1 -> L.2 -> L.3 -> L.4 chain together
  with the QG5D inputs of Appendix N." Reason: **option (b)**. No §N
  section contains the DAG; the DAG structure is inherent to the L
  section ordering.
- Lemma count corrected 19 -> 21 (actual total: 5 + 4 + 9 + 3 = 21).
- "Table N.1" removed (no such table exists).
- Added "The QG5D spectral inputs ... are collected in Appendix N, §§
  N.1--N.2" to preserve the (correct) link to the existing N sections
  for the QG5D inputs that really do feed the gradient-flow argument.

### Edit 2 (L.5 sub-clause table, lines 76-88 pre-edit -> 77-94 post-edit)
Table column header renamed: `Appendix N ref.` -> `Proof location`.
Descriptive sentence above table: "its proof location in Appendix N"
-> "its proof location within Appendix L".

Row-level changes (all option **(b)**):
- L.1(i): `Lemma 3.8 | \S N.5, \S N.7` -> `Lemma L.3.8 | Section L.3`.
  Lemma L.3.8 (extraction of [TrF^2]_R) is in L3-phase3.md.
- L.1(ii): `Lemma 3.8 + Lemma 2.4 | \S N.5, \S N.4` ->
  `Lemma L.3.8 + Lemma L.2.4 | Sections L.3 and L.2`.
  Lemma L.2.4 (OS reconstruction at fixed flow time) is in L2-phase2.md.
- L.1(iii): `Lemma 4.2 | \S N.8` -> `Lemma L.4.2 | Section L.4`.
- L.2: `Lemma 4.2 | \S N.8` -> `Lemma L.4.2 | Section L.4`.
- L.3(i): `Lemma 4.1 | \S N.9.1` -> `Lemma L.4.1 | Section L.4
  (Lemma L.4.1, Step 1)`. Sub-clauses are verified as steps inside the
  Lemma L.4.1 proof.
- L.3(ii): `Lemma 4.1 | \S N.9.2` -> `Lemma L.4.1 | Section L.4
  (Lemma L.4.1, Step 2)`.
- L.3(iii): `Lemma 4.1 | \S N.9.3` -> `Lemma L.4.1 | Section L.4
  (Lemma L.4.1, Step 3)`.
- L.3(iv): `Lemma 4.1 | \S N.9.4` -> `Lemma L.4.1 | Section L.4
  (Lemma L.4.1, Step 4)`.
- L.3(v): `Lemma 4.1 | \S N.9.5` -> `Lemma L.4.1 | Section L.4
  (Lemma L.4.1, Step 5)`.
- L.4(leading): `Lemma 4.3 | \S N.9.6` -> `Lemma L.4.3 | Section L.4
  (Lemma L.4.3)`. (Note: the `§N.9.6` reference used "9" and hence
  matched the §N.[6-9] pattern and was part of the required fixes.)
- Lemma shorthand "Lemma 3.8 / 2.4 / 4.1 / 4.2 / 4.3" -> fully-qualified
  "Lemma L.3.8 / L.2.4 / L.4.1 / L.4.2 / L.4.3" throughout the table to
  match the canonical labels in L1-L4 files.

### Edit 3 (L.6.1 proof, formerly lines 150, 153 -> now 157, 160-161)
**Old:**
> (ii) follows from (i) and Lemma 4.1 (Appendix N, \S N.9). The
> Suzuki formula constructs $T_{\mu\nu}^R$ ... The five sub-clauses
> are verified in \S N.9.1--N.9.5.

**New:**
> (ii) follows from (i) and Lemma L.4.1 (Section L.4). The Suzuki
> formula constructs $T_{\mu\nu}^R$ ... The five sub-clauses are
> verified in the five steps of the proof of Lemma L.4.1 (Section L.4).

- `Lemma 4.1 (Appendix N, \S N.9)` -> `Lemma L.4.1 (Section L.4)`.
  Reason: **option (b)**.
- `\S N.9.1--N.9.5` -> `the five steps of the proof of Lemma L.4.1
  (Section L.4)`. Reason: **option (b)**. The five sub-clauses of L.3
  correspond to the five steps of the proof of Lemma L.4.1 in
  L4-phase4.md.

### Edit 4 (L.6.1 clause (iii), formerly line 157 -> now 165)
**Old:**
> (iii) follows from (i) and Lemma 4.3 (Appendix N, \S N.9.6).

**New:**
> (iii) follows from (i) and Lemma L.4.3 (Section L.4).

- `Lemma 4.3 (Appendix N, \S N.9.6)` -> `Lemma L.4.3 (Section L.4)`.
  Reason: **option (b)**.

### Edit 5 (L.6.2 proof, formerly lines 184, 192 -> now 192, 200)
**Old:**
> *Proof.* (i) and (ii) follow from Lemma 4.2 (Appendix N, \S N.8),
> which assembles the existence of $[\mathrm{Tr}\,F^2]_R$ (Lemma 3.8,
> unconditional), ...
> (iii) follows from Lemma 4.3 (Appendix N, \S N.9.6), which combines

**New:**
> *Proof.* (i) and (ii) follow from Lemma L.4.2 (Section L.4), which
> assembles the existence of $[\mathrm{Tr}\,F^2]_R$ (Lemma L.3.8,
> unconditional), ...
> (iii) follows from Lemma L.4.3 (Section L.4), which combines

- `Lemma 4.2 (Appendix N, \S N.8)` -> `Lemma L.4.2 (Section L.4)`.
  Reason: **option (b)**.
- `Lemma 3.8` -> `Lemma L.3.8`. Cosmetic alignment with canonical label.
- `Lemma 4.3 (Appendix N, \S N.9.6)` -> `Lemma L.4.3 (Section L.4)`.
  Reason: **option (b)**.

## Verification
- `grep -n '§N\.[6-9]|§N\.10'` on L0-L5-L6-L7.md: **0 matches**.
- `grep -n 'N\.(6|7|8|9|10)'` on L0-L5-L6-L7.md: **0 matches**.
- All Lemma L.x.y references in the edited file point to lemmas that
  exist:
  - Lemma L.2.4: present at L2-phase2.md:398
  - Lemma L.3.8: present at L3-phase3.md:563
  - Lemma L.4.1: present at L4-phase4.md:33
  - Lemma L.4.2: present at L4-phase4.md:246
  - Lemma L.4.3: present at L4-phase4.md:368
- Section L.1, L.2, L.3, L.4 are the actual section titles of
  L1-phase1.md, L2-phase2.md, L3-phase3.md, L4-phase4.md (verified by
  reading the file headers).

## Out-of-scope §§N.6-N.10 references found in other L files
(read-only; not touched by this agent, but reported per prompt Step 4)

`research/appendix-L/L4-phase4.md`:
- Line 29: `(Lemmas 3.7--3.8, Appendix N, SS N.5--N.6; GNS reconstruction,`
- Line 30: `Appendix N, SS N.7) and verify all five sub-clauses of Conjecture L.3.`
- Line 248: `$[\mathrm{Tr}\,F^2]_R$, Appendix N, SS N.6), the renormalised`
- Line 266: `(Appendix N, SS N.6) constructs the renormalised two-point function as`
- Line 370: `$[\mathrm{Tr}\,F^2]_R$, Appendix N, SS N.6), the renormalised`

These all need the same treatment (§N.6, §N.7 -> Section L.3 / Section
L.4 for the gradient-flow lemma references) but belong to a different
agent's file in Wave 11.

`research/appendix-L/L1-phase1.md`, `L2-phase2.md`, `L3-phase3.md`: no
matches for §N.[6-9]|§N.10 found.

## Notes on what was NOT changed (deliberate)
- References to `§N.1--N.2`, `§N.5` (the existing N sections) were
  preserved where they were correct attributions for QG5D inputs.
- Remark L.5.2 (line 101) and L.7.3 (lines 273, 293, 296) contain
  references like `Appendix N, \S N.5, Lemma 3.1/3.7`. §N.5 *exists*
  (it is "Note on gravitational physics"), but it does not contain
  Lemma 3.1 or Lemma 3.7 -- those live in L3-phase3.md as Lemma L.3.1
  and Lemma L.3.7. This is a *separate* bug (misrouted reference within
  an existing §N.x section), not a §§N.6-N.10 bug. The prompt for this
  agent is narrowly scoped to §§N.6-N.10 (see prompt §"Step 1" and
  verification criterion "0 matches for `§N\.[6-9]|§N\.10`"), so these
  were left for a follow-up fixup.
- The proof sentence at the current line 147 "Lemmas 1.1--1.4, 2.2--2.4,
  3.1--3.8 of Appendix N" is another instance of the same misrouting
  (these lemmas are in L1-L3, not Appendix N), but contains no
  §§N.6-N.10 reference so it is outside this agent's scope.
- The L.5 table structure was preserved: only column content and the
  header `Appendix N ref.` -> `Proof location` were modified, per
  prompt "Don't change the L.5 table structure (only the references
  inside it)" -- interpreted as "don't change which conjectures/rows
  appear"; the column name change was necessary because the column no
  longer points into Appendix N.
