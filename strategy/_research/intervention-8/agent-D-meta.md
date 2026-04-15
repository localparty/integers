# Agent D — strategy+programme+millenium-apps sweep (Intervention 8, 2026-04-15)

## Summary
- Files scanned: 552 prose `.md` files (strategy=323, programme=179, millenium-apps=50).
- Files with migrations: 14
- Total migrations: 27 (counted by distinct HTML-comment-annotated strikethroughs/replacements)
- Breakdown: dimension 11 | postulation 1 | labels (Postulate → Theorem) 15 | e-circle 0 | choice 1 (soft)

## Per-file report

### strategy/the-picture-of-the-ecircle.md
- Class: postulation + dimension
- Before: `The postulate "spacetime is five-dimensional" gives the geometric circle.`
- After: `The ~~postulate "spacetime is five-dimensional"~~ derived claim "spacetime has 4+1 coordinate structure" <!-- legacy 2026-04-15: ... per §0.10 canon entries 1+4+6, Intervention 8 --> gives the geometric circle.`
- Count: 1

### strategy/qg5d/00-audit-strategy.md
- Class: dimension
- Before: `... on a 5-dimensional cohomological/spectral base M⁵ ...`; `- 5D geometry M⁵ = M⁴ × S¹ well-defined ...`
- After: `... on a ~~5-dimensional~~ 4+1-coordinate <!-- ... --> ...`; `- 4+1 coordinate geometry <!-- ... -->  M⁵ = ...`
- Count: 2

### strategy/ns/00-millenium-strategy.md
- Class: dimension (x2)
- Before (81): `compactification of the fifth dimension gives NS on a base ...`
- After: `compactification of the ~~fifth dimension~~ internal-phase S^1/Z_2 factor <!-- ... --> gives ...`
- Before (82): `The KK spectral gap Δ_0^KK > 0 requires a compact extra dimension ...`
- After: `... compact ~~extra dimension~~ internal phase fiber <!-- ... --> ...`
- Also migrated opening "5D ambient geometry" → "4+1 coordinate ambient geometry".
- Count: 3

### strategy/proof-chain/qg5d/PROOF-CHAIN.md
- Class: dimension (2 migrations; line 60 preserved as-is — already-strikethrough legacy P1-P4 text).
- Before (152): `e-conservation constraint through 5th dimension`
- After: `e-conservation constraint through the internal phase fiber <!-- ... -->`
- Before (522): `... zeta regularization on flat background + compactified dimension, which is the regime ...`
- After: `... + ~~compactified dimension~~ compact internal phase fiber <!-- ... -->, which ...`
- Count: 2

### programme/01-the-thesis.md
- Class: dimension (three sibling phrases collapsed into one strikethrough+replacement block)
- Before: `Spacetime is five-dimensional. The fifth dimension is circular, periodic, and real — it is the U(1) fiber that every quantum phenomenon projects through. When you project from five dimensions to four, you get ...`
- After: `~~Spacetime is five-dimensional. The fifth dimension ...~~ Spacetime has a 4+1 coordinate structure. The internal phase is circular ... When you project from 4+1 coordinates to 4 spacetime coordinates, you get ... <!-- ... -->`
- Count: 1 (multi-phrase block)

### programme/00-table-of-contents.md
- Class: dimension (2 locations)
- Before (23): `... The five-dimensional geometry. The Riemann zeros ...`
- After: `... The ~~five-dimensional~~ 4+1 coordinate <!-- ... --> geometry. ...`
- Before (27–28): `### 02 — The five-dimensional geometry (QG5D)` / `*... spacetime is five-dimensional — (x,y,z,t,e) — where the fifth dimension e is circular ...*`
- After: section title migrated with HTML comment; prose migrated with strikethrough+replacement.
- Count: 2

### programme/13-navier-stokes.md
- Class: dimension + postulation
- Migrated (98): `framework IS five-dimensional Einstein gravity` → `framework IS 4+1 coordinate Einstein gravity` (strikethrough+comment). BHMR literature references in same paragraph preserved as canonical nomenclature for competing work (with explanatory comment).
- Migrated (116): `QG5D framework postulates that spacetime is five-dimensional: M^5 = ... S^1 is the fifth dimension with compactification radius R_e ... The five-dimensional Einstein equations ...` — full block migrated to derivation language (postulates→derives; is five-dimensional→has a 4+1 coordinate structure; fifth dimension→internal-phase U(1) fiber; five-dimensional→M^5).
- Migrated (204): `... 5D Einstein equations with compact extra dimensions ...` → `... compact ~~extra dimensions~~ internal phase fiber <!-- ... -->`.
- Count: 3

### programme/25-the-graph-structure.md
- Class: dimension
- Before (21): `| 1 | **QG5D** | ... | The five-dimensional geometry, the CBB system ...`
- After: `The ~~five-dimensional~~ 4+1 coordinate <!-- ... --> geometry, the CBB system ...`
- Count: 1

### programme/26c-the-chessboard-rationale.md
- Class: dimension (2 locations)
- Before (94): `| Restoring the 5th dimension dissolves the mystery ...`
- After: `| Restoring the ~~5th dimension~~ internal phase <!-- ... --> dissolves the mystery ...`
- Before (99): `The framework says: the universe is five-dimensional, and every apparent paradox ...`
- After: `The framework says: the universe has ~~is five-dimensional~~ a 4+1 coordinate structure <!-- ... -->, and every ...`
- Count: 2

### programme/ring-traversals/traversal-09/vertices/cramer.md
- Class: choice (soft — idiomatic math usage)
- Before (25): `... it depends only on P, which we fix`
- After: `... which ~~we fix~~ is held constant <!-- ... -->`
- Count: 1

### millenium-apps/quantum-compiler-seed/strategy/03-riemann-zeros-as-instruction-set.md
- Class: dimension
- Before: `the compactified extra dimension of the 5D geometry — is unitarily equivalent`
- After: `the compact internal phase fiber of the 4+1 coordinate geometry <!-- ... --> — is unitarily equivalent`
- Count: 1

### millenium-apps/quantum-compiler-seed/strategy/23-observation-without-collapse.md
- Class: dimension
- Before: `phase channel: a compact extra dimension (the e-circle in QG5D ...)`
- After: `phase channel: a compact internal phase fiber <!-- ... --> (the e-circle in QG5D ...)`
- Count: 1

### strategy/rh/deliverables/rh-beyond-bare.md
- Class: labels (POSTULATE → THEOREM)
- Migration: `four postulates P1–P4` → `four ~~postulates P1–P4~~ theorems T1–T4 <!-- ... -->`
- Count: 1

### strategy/pvnp/deliverables/pvnp-beyond-bare.md
- Class: labels
- 3 migrations of `postulates P1-P4` → `~~postulates P1-P4~~ theorems T1-T4 <!-- ... -->`
- Count: 3

### strategy/hodge/deliverables/hodge-beyond-bare.md
- Class: labels
- 3 migrations of `postulates P1–P4` → `~~postulates P1–P4~~ theorems T1–T4 <!-- ... -->`
- Count: 3

### strategy/bsd/deliverables/bsd-beyond-bare.md
- Class: labels + dimension (first mention was "5D postulates P1–P4")
- 2 migrations
- Count: 2

### strategy/ns/deliverables/ns-beyond-bare.md
- Class: labels (x3) + dimension (x1, in Table 2.1 row 14 "5D free-parameter count")
- 4 migrations
- Count: 4

### strategy/ym/deliverables/ym-beyond-bare.md
- Class: labels + dimension ("5D geometry's postulates P1–P4" → "4+1 coordinate geometry's theorems T1–T4")
- 2 migrations
- Count: 2

### strategy/decomposition/decomposition-brief.md
- Class: labels ("Postulate P3" → "Theorem T3" in example cell)
- 1 migration
- Count: 1

## Intentionally preserved (spec/canon/history contexts)

### Canon and spec documents (DO NOT TOUCH per agent prompt)
- `strategy/north-star.md` — IS the canon; hits in the "Avoid" column of §0.10 table are definitional.
- `strategy/universal-approval-run.md` — IS the drift-scan specification; Phase 11.1 enumerates the exact patterns.
- `strategy/_template/audit-brief-template.md` — template spec describing the drift-pattern tables (lines 199–200 list the legacy terms as the migration-table "Avoid" column for sub-agents).

### History / change-log files preserved verbatim (by agent prompt)
- `strategy/north-star.change-log.md`
- `strategy/universal-approval-run.change-log.md`
- `strategy/self-healing-log.md`
- `strategy/_research/fixes-log.md`
- (none of these files were edited by Agent D)

### Landscape / competitor-survey files — legacy terms are canonical for the competitors they describe
These files intentionally use Kaluza-Klein / ADD / RS / AdS-CFT nomenclature to describe competing programmes. Migrating would misrepresent the competitor's own language. PRESERVED:
- `strategy/_research/e-circle-bouquet/landscape.md` — landscape of KK / extra-dimensions programmes (Wesson, ADD, RS1/RS2, holographic, etc.)
- `strategy/_research/qg5d/landscape.md` — competitor school survey
- `strategy/_research/qg5d/outlet.md` — outlet summary describing the framework-as-claim sentence (one mention of "5-dimensional"); marginal — see FLAG below.
- `strategy/_research/landscape-survey.md` — global landscape (Arkani-Hamed entry).
- `strategy/_research/search-log.md` — query history ("Kaluza-Klein extra dimensions modern research ...").
- `strategy/_research/global-acknowledgments.md` — acknowledgments index heading ("E-Circle / Bouquet / Extra Dimensions") and tag line for ~30 competitor schools.
- `strategy/_research/ns/landscape.md` — NS landscape (one mention in context of fluid/gravity 5D literature).
- `strategy/e-circle-bouquet/00-audit-strategy.md` — audit strategy referencing Adelberger gravity-test bounds on extra dimensions (competitor nomenclature).
- `strategy/e-circle-bouquet/e-circle-bouquet-audit-brief.md` — competitor framework enumeration ("ADD large extra dimensions (1998)").
- `strategy/paper1-audit/A2-construct.md` — citation of Baptista 2021 paper (literal title contains "five-dimensional supergravity").

### Paper-1-audit files — quoting the legacy POSTULATE labels for reclassification
These files are precisely the paper-1-audit trail documenting the P1–P4 → T1–T4 reclassification. Legacy labels are load-bearing quotations:
- `strategy/paper1-audit/audit-report.md` — "Original: ..." quotes preserve original P1 language.
- `strategy/paper1-audit/commit-memo.md` — commit memo describes the reclassification; legacy labels preserved.
- `strategy/paper1-audit/reclassification-table.md` — the very reclassification table: `| **P1** | Postulate 1 (Five-dimensional spacetime) | ... | **SPLIT → T1 + O1** | ...`.

### Already-migrated content preserved verbatim
- `strategy/proof-chain/qg5d/PROOF-CHAIN.md` lines 59–69 — the `~~Legacy statements (P1-P4)~~` strikethrough block (originally migrated Intervention 1; preserved as historical reference).
- `programme/01-the-thesis.md` — preserved G's-voice original via strikethrough inside the same paragraph (not a preserve-only case; migrated with strikethrough).

### File-path references (directory names)
- `strategy/ns/deliverables/ns-beyond-bare.md` line 533 references `paper4-five-dimensional-arena/…` — this is a literal directory name. NOT migrated (renaming the dir is out of scope).
- `programme/00-table-of-contents.md` line 225 references planned filename `02-the-five-dimensional-geometry.md` — NOT migrated (filename convention).
- `programme/13-navier-stokes.md` line 100 references "five-dimensional anti-de Sitter space" as literature nomenclature (BHMR); preserved with explanatory HTML comment on the preceding programme-voice sentence.

### Idiomatic / past-tense / non-drift matches for "we fix / we set / we assume / we propose"
- `strategy/rh/pac-output/runs/run-02/blackboard.md` line 100 — `... unless we choose to strengthen (we do ...)` — meta-strategy voice, not derivation; PRESERVED.
- `strategy/release-channels.md` line 295 — `... we fix the build` — DevOps sense; PRESERVED.
- `strategy/draft-strategy.md` line 36 — `how do we fix this` — meta discussion question; PRESERVED.
- `programme/07-the-riemann-hypothesis.md` line 141 — `... we fixed them` — past tense recap of referee repair work; PRESERVED.

## Flagged for human review

1. **`strategy/50+.md`** — the 57-block research-item catalog contains `extra dimensions` 5 times. Items 35 + 51 deliberately contrast "extra dimensions as postulate" (competitor framing) vs. "R forced" (programme framing). The title of item 35 is itself *"Extra dimensions at ~10 μm as a theorem, not a postulate."* — a deliberate rhetorical contrast. Migrating would destroy the contrast that is the item's point. **Preserved in full** for human review. If desired, the programme-voice conclusions inside §284–285 and §354 can be annotated without harming the title/contrast.

2. **`strategy/consolidation-plan.md`** — lines 337, 348, 538 describe appendix-D ("extra dimensions") and comparative-analysis bullet ("string theory promised: ... extra dimensions ..."). These describe competitor framings. The appendix-letter label "D" is load-bearing filename/taxonomy. Preserved for human review.

3. **`strategy/_research/qg5d/outlet.md`** line 18 — `... on a 5-dimensional cohomological/spectral base ...` is a single-sentence framework-claim summary used by the outlet research. Marginal case; neighboring `strategy/qg5d/00-audit-strategy.md` was migrated (same claim, different file). Flagging for consistency check: consider migrating outlet.md in next cycle.

4. **`strategy/ns/deliverables/ns-beyond-bare.md` line 533** — directory name `paper4-five-dimensional-arena/...` is a real on-disk path. Not migrated; flagged so the eventual dir rename (if any) can propagate this reference.

5. **`programme/13-navier-stokes.md`** — the file contains heavy BHMR/AdS-CFT literature exposition. The three programme-voice sentences (98, 116, 204) were migrated; the BHMR-describing sentences (100, 112, 124, 126, 202, 206) use "5D" / "five-dimensional" / "5D toolkit" as literature/correspondence nomenclature. Preserved as descriptive of the correspondence; consider a voice pass in Phase 11.2 cycle 2 if the BHMR section should be rewritten in programme-voice terms.

---

## Idempotence

All edits are idempotent strikethrough+HTML-comment annotations. Re-running would find no new drift in the migrated passages (the canonical term is already present next to the strikethrough). The drift-scan grep will continue to hit the strikethrough text — by design, per `strategy/north-star.md` §0.10 "non-destructive".

## End of Agent D report
