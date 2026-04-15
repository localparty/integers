# Agent C — solutions-with-prize/ sweep (Intervention 8, 2026-04-15)

## Summary

- Files scanned: 1,592 prose files (`*.md` + `*.tex`) across 8 prize papers
- Files with migrations: 6
- Total migrations: 8 inline strikethrough + HTML-comment annotations
- Breakdown: dimension 8 | postulation 0 | labels 0 | e-circle 0 | choice 0

Most candidate hits turned out to be legitimate usage (standard math hypothesis verbs like "we assume CP-1", "we fix notation"; comparison to competing programmes like AdS/CFT; reference titles in quotations; technical KK-scaffolding terminology describing external formalism). Only clear cases of self-description of the Integers programme using legacy "5-dimensional / five-dimensional / extra dimension / fifth dimension" language were migrated.

## Per-file report (grouped by paper)

### solutions-with-prize/paper08-yang-mills/

- **preprint/sections/L-clay-conjectures.md** (line 2657): migrated "The five-dimensional origin of the construction introduces a KK tower..." → "The 4+1 coordinate-structure origin..." (strikethrough + canonical + HTML comment citing §0.10 entries 1-2).
- **preprint/sections/07-previous-approaches.md** (lines 113-117): migrated self-description "KK approach uses extra dimensions as the *actual geometry*" → "uses the 4+1 coordinate structure as the *actual geometry*". Kept the other two "extra dimensions" in the paragraph — they compare to AdS/CFT and introduce the comparison.
- **gradient-flow-attack-plan/research/W7-14-af-match.md** (lines 424, 522, 550): migrated 3 occurrences — "dimensional reduction from a five-dimensional theory on M^4 × S^1/Z_2" → "theory on the 4+1 coordinate structure M^4 × S^1/Z_2"; "five-dimensional origin" → "4+1 coordinate-structure origin" (two sites).
- **gradient-flow-attack-plan/research/appendix-L/L4-phase4.md** (line 319): migrated "The five-dimensional origin" → "The 4+1 coordinate-structure origin".
- **research/09-why-previous-approaches-failed.md** (line 115): migrated self-description — parallel of the preprint 07 migration.

### solutions-with-prize/paper30-navier-stokes/

- **preprint/00-proof-skeleton.md** (lines 157, 167): migrated two occurrences — "extra dimension S^1" → "internal phase fiber S^1 (the e-circle)"; "compactness of the fifth dimension" → "compactness of the internal phase (the e-circle S^1)". Cites §0.10 entries 1-2.

### solutions-with-prize/paper13-rh/, paper26-bsd/, paper28-pvnp/, paper29-hodge/, paper33-goldbach/, paper41-collatz/

No migrations needed. All candidate hits were legitimate:
- paper13-rh/research/53: "what we propose" inside a prose discussion of Conrey-Li — not a postulation verb about the programme structure.
- paper13-rh/research/03-dir5.md:32 "from extra dimensions" — metaphor for level-repulsion from absent eigenvalues, not the Integers 4+1 structure.
- paper28-pvnp — all "we propose" / "we assume" instances are in conjecture statements or standing-hypothesis blocks (H1, H2, CP-1). Standard math writing; not drift.

## Notes / edge cases

- **Reference titles preserved verbatim**: "Paper 1: 'Quantum Mechanics from Five-Dimensional Geometry.'" appears in paper08 preprint/sections/references.md:223 and research/19-references.md:160. These are historical citation titles — skipped per the "don't migrate inside verbatim quotations" rule.
- **Code blocks skipped**: paper08 gradient-flow-attack-plan/research/W11-28-l4-fixups.md:43 occurrence is inside a ``` fenced block documenting the before/after of a prior edit. Skipped.
- **Comparison-to-other-programmes preserved**: "extra dimensions" used to describe AdS/CFT, general holographic framing, KK scaffolding as a technical term of art, and "the theory does not use extra dimensions" rebuttals were left intact. These are about external theories or about distinguishing the final 4D theory from its scaffold.
- **Frozen snapshots honored**: `preprint/PROOF-CHAIN.md` files in paper08/13/26/28 were not touched. `preprint/sections/*.md` were treated as editable prose (not frozen) per scope definition.
- **Legitimate math verbs left intact**: "we fix notation", "we fix the representation to be minimal", "we fix ε* = 0.49 throughout", "we assume (H1) ... (H2)", "we choose λ not in the countable union", "we propose [a conjecture/rule/route]" — these are standard math writing for hypothesis statements and notation fixing, not programme-structure postulation. Canon §0.10 entry 4 targets propositional framing of the Integers programme, not local proof hypotheses.
- **"5D" shorthand not migrated**: ~95 occurrences of "5D" across 30 files (esp. paper30-navier-stokes, paper08 preprint/sections/N-qg5d-infrastructure.md). Not in the explicit Step 2 drift pattern list ("5-dimensional" / "five-dimensional" with hyphen/word-form). Flagged below for future intervention.

## Flagged for human review

1. **"5D" shorthand** (not in Step 2 explicit list). ~95 occurrences; canon §0.10 entry 1 targets "5-dimensional / five-dimensional" but programme shorthand "5D" is adjacent. If future sweeps include "5D", the migration would be extensive (paper30 alone has 10 in preprint/00-proof-skeleton.md — Link diagrams, KK-reduction tables). Suggest a separate targeted sweep.
2. **QG5D as programme name** (Phase 11.1 drift class, not Step 2 Intervention 8 scope). 5 occurrences across paper08 closing-H4/. Defer to dedicated Intervention.
3. **Paper 1 title "Quantum Mechanics from Five-Dimensional Geometry"** — this is the published title cited across references.md files. Title change would be a separate editorial decision (retroactive rename of paper 1). Left as citation.
4. **paper08 research/path-A-multiscale-rg/05-obstacles-and-ideas.md:307** "The extra dimensions are COMPACT (size r_3)" — describes the KK formal construction with classical KK terminology ("extra dimensions" is the KK-theory term of art). Borderline; left as technical terminology but flag for review.
5. **paper08 research/22-closing-the-gaps.md:209, 264** — the prose explicitly rebuts "It's 'really 11D'" framing from imagined reviewers. The "extra dimensions" references function as quoted framing being rebutted. Kept intact to preserve the rebuttal's rhetorical structure.
6. **preprint/sections/* status** — treated as editable; if these are in fact frozen publication state, revert the two edits in paper08 preprint/sections/ (L-clay-conjectures.md, 07-previous-approaches.md) and paper30 preprint/00-proof-skeleton.md.

## Idempotence

All migrations use the canonical `~~legacy~~ canonical<!-- legacy 2026-04-15: ... per §0.10, Intervention 8 -->` pattern. Re-running Intervention 8 will match the already-struck text and either pass (already-migrated preserve rule) or leave as-is since the canonical text is now present.
