# {{SHAPE_NAME}} Audit Brief (for the PAC Operator)

*DELTA from ring-traversal brief. Applies the generic projection-audit protocol to {{SHAPE_NAME}}. Extracted from the 6 Millennium instances (YM, RH, BSD, PvNP, Hodge, NS) averaged together. Produces A (internal) + B_bare (external-shape skeleton) + C_bare (beyond-ask skeleton) in bare mode. B_full and C_full DEFERRED to composition-backward.*

*G Six and Claude Opus 4.6. {{DATE}}.*

---

## GOAL

Produce a compliance-audited projection-audit deliverable for {{SHAPE_NAME}} in **bare mode only** this run. Three concrete files at end:

**A. Internal artifacts** — scaffolding at `strategy/{{SHAPE_NAME}}/pac-output/runs/run-NN/`:
- `blackboard.md`, `compliance-map.md` ({{M}} × {{N}} cells), `vertices/{{SHAPE_NAME}}/`, `kills.md`, `critic-attacks.md`, `arbiter-decisions.md`, `silent-cells.md`, `commit-memo.md`

**B_bare. External-shape theorem skeleton** — `strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-bare.md`
- In the source's expected genre (Clay-official / community-standard / framework-claim / experimental-pin)
- Zero prose; ≤ 15 pages

**C_bare. Beyond-ask theorem skeleton** — `strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-beyond-bare.md`
- Programme bonuses beyond what the source requires
- Zero prose; ≤ 15 pages

**B_full and C_full DEFERRED.** Do not produce prose this run.

---

## DELTAS FROM RING-TRAVERSAL BRIEF

### DELTA 1 — Mode

Dual mode: **compliance-audit + bare-deliverable-synthesis**.

- Walk {{M}} layers × {{N}} requirements = {{M×N}} audit cells
- Per cell: emit PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation
- Synthesize B_bare and C_bare in bare mode
- Defer B_full / C_full

### DELTA 2 — Primitives

- **VERIFY** — each layer against each requirement
- **DECOMPOSE** — SILENT verdicts into named walls or new layers
- **CONSTRUCT** — new layers for SILENT gaps (bare: theorem statement + citation only)
- **BYPASS** — via capacitor transposition when direct construction fails
- **EXCISE** — applies ONLY where special provisions allow (e.g., variant-excision under §5b for NS). Otherwise NOT APPLICABLE (all requirements mandatory).
- **EXTRACT** — pull theorem statements + numbers + equations + figure-shells from existing programme papers into bare format
- **DISCLOSE** — any OPEN-BUT-ADDRESSED verdict emits an explicit NAMED WALL tag with bypass-route citation

### DELTA 3 — The "bare" discipline

B_bare and C_bare contain ONLY:
- Formal theorem statements (numbered, with dependency graph)
- Definitions
- Equations (numbered)
- Figures (ASCII / TikZ-ready skeleton; label + caption only)
- Numbers (constants, bounds, values, experimental matches; in tables)
- Proof-chain analytics (compliance map, named walls, RIGIDITY / SYMMETRY metrics)
- Citations (every claim cites programme paper + specific proof location)

B_bare and C_bare contain NONE of:
- Introduction paragraphs, motivation paragraphs, historical context, discussion
- Proof details in prose (only statement + citation)
- Worked examples in prose
- "We show that..." narrative

If a section heading attracts prose, REMOVE the section.

### DELTA 4 — Output A (internal artifacts)

Standard PAC output structure. Same pattern as YM run-02 (compliance-audit pilot).

**compliance-map.md format** (key artifact):

```
# {{SHAPE_NAME}} Compliance Map — {{M}} × {{N}}

## Matrix

| Layer | Req 1 | Req 2 | ... | Req {{N}} |
|-------|-------|-------|-----|-----------|
| L1    | PROVED ({{paper}} §X) | ... | ... | ... |
| L2    | ... | ... | ... | ... |
| ...   |
| L{{M}}    | ... | ... | ... | ... |

## Verdict distribution per requirement

| Requirement | PROVED | PARTIAL | OPEN-BUT-ADDRESSED | SILENT |
|-------------|--------|---------|--------------------|--------|
| ...         | ...    | ...     | ...                | ...    |

## SILENT cells (action required)

For each SILENT: NEW-NAMED-WALL / NEW-LAYER-SKETCH / BYPASS-VIA-CAPACITOR

## Arbiter audit trail

[per-cell: author verdict, critic alternative, arbiter decision]
```

### DELTA 5 — Output B_bare structure

Fixed {{K}}-section structure for `{{SHAPE_NAME}}-bare.md`. Template sections (customize per target):

```
§1 Claim (verbatim from source)
§2 Main Theorem (formal statement)
§3 Requirements Map (compliance overview — 7-row or N-row table)
§4 Definitions (formal)
§5-§(K-3) Per-requirement sections (one per requirement; theorem statements with citations)
§(K-2) Proof-Chain Analytics (dependency graph ASCII, RIGIDITY, SYMMETRY, compliance matrix reference)
§(K-1) Named Walls (all OPEN-BUT-ADDRESSED items with full disclosure)
§K Numbers Table (every constant, bound, value with citation)
§(K+1) References (programme papers with §-level precision)
```

Writing discipline:
- Each section ≤ 1 page typically
- No "introduction paragraph" — go straight to theorem
- ASCII figures allowed in analytics section
- Number tables in dedicated section only

### DELTA 6 — Output C_bare structure

Fixed {{J}}-section structure for `{{SHAPE_NAME}}-beyond-bare.md`. Template sections:

```
§1 5D Geometric Derivation (theorem statement — how the 5D geometry gives this projection)
§2 Zero Free Parameters (table — every quantity + 5D-geometric determinant)
§3 Relevant Pins (table — sub-percent experimental matches, if applicable)
§4 Cross-Projection Connections (theorems linking this to other projections)
§5 Bonus Theorems Beyond Source Ask (optional per target)
§6 Computed Numerical Values (table, with experimental comparison)
§7 Proof-Chain Analytics (Beyond-Clay/community depth — additional cross-cuts)
§8 References
```

Same bare discipline — zero prose.

### DELTA 7 — Composition-backward deferral

B_full and C_full NOT PRODUCED this run. Deferred until:
1. B_bare and C_bare LOCK (no SILENT, structure correct, numbers tight)
2. User triggers composition-backward step

Future composition-backward run:
- Index 60+ project reservoir
- Per-section retrieval + composition via parallel agents
- Integration pass stitches into final LaTeX

### DELTA 8 — Citation discipline

Every theorem, definition, equation, number, figure cites:
- Programme paper reference (`paperNN-short-name`)
- Specific proof location (§N, Theorem T.M, Lemma L.K, Appendix A.J)

Format: `(paperNN-short §X Theorem T.Y)` or `(paperNN-short Eq. (Z.W))`.

Uncited claim = FAIL. Arbiter returns for revision.

### DELTA 9 — Publication override

Same as sibling bundles. OVERRIDES `publishing/strategy.md`. See strategy doc §9 for cascade customized to source class.

### DELTA 10 — Named wall disclosure discipline

Every OPEN-BUT-ADDRESSED verdict emits a NAMED WALL with REQUIRED fields:

- **Name**: W_N / short description
- **Chain location**: which layer
- **Programme location**: paperNN §X
- **Statement**: what the wall asserts
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass route**: specific method (e.g., Balaban RG + gradient flow; Slepian compatibility; CCM Layer 1; motivic BC extension)
- **Bypass citation**: paperNN §X; session log YYYY-MM-DD
- **Aggregate confidence**: fraction (e.g., 0.65, 0.82)
- **Audit pending**: specific lemma (e.g., L.3.7, KMS₁ uniqueness, functoriality)
- **Effect if audit passes**: wall upgrades to PROVED
- **Effect if audit fails**: alternate bypass candidates (enumerated)
- **Independent standing**: which layers remain unaffected

All walls DISCLOSED in B_bare §(K-1). Silence = §5d violation (for Clay-Official) or equivalent for other source classes.

### DELTA 11 — Special provisions

Source-specific. Leave empty or fill per target:

- For Clay PvNP / NS: §5b either-direction — resolution in either direction counts
- For NS: variant-excision — targeting one variant (e.g., B) is NOT §5d-silence on A/C/D because they are alternatives
- For framework-claim targets: Clay rules don't apply strictly; Zenodo-priority + programme cross-verification instead
- For experimental-pin targets: sub-percent match + derivation chain + independent experimental verification

---

## PROCEDURE

### Step 1 — Read inputs (mandatory, in order)

1. `strategy/{{SHAPE_NAME}}/00-audit-strategy.md` — the strategy doc (sibling of this brief)
2. `{{LIVE_CHAIN_PATH}}` — the live proof-chain
3. `strategy/x-ray/proof-chain/{{SHAPE_NAME}}/X-RAY.md` — prior x-ray (if exists)
4. `strategy/decomposition/proof-chain/{{SHAPE_NAME}}/PROOF-CHAIN.md` — prior decomposition (if exists)
5. `{{CLAIM_SOURCE_CITATION}}` — the source of requirements (Clay PDF / community-standard paper / programme paper)
6. Clay Rules §4-§8 summary from `strategy/ym/00-millenium-strategy.md §2` (shared reference)

### Step 2 — Build compliance map

Walk {{M}} × {{N}} cells. Per cell: author-verdict + critic-alternative + arbiter-decision.

Write `compliance-map.md` following DELTA 4 format.

### Step 3 — Address SILENT verdicts

For each SILENT cell:
- DECOMPOSE into named wall, OR
- CONSTRUCT new layer (theorem statement only), OR
- BYPASS via capacitor transposition (cite cell)

Update compliance map. No SILENT at end.

### Step 4 — Synthesize B_bare

Walk the fixed {{K}}-section structure (DELTA 5). Zero prose. Write to `strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-bare.md`.

### Step 5 — Synthesize C_bare

Walk the fixed {{J}}-section structure (DELTA 6). Zero prose. Write to `strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-beyond-bare.md`.

### Step 6 — Verification pass

Critic examines B_bare + C_bare for:
- Any prose paragraph (FAIL)
- Any uncited claim (FAIL)
- Any SILENT requirement (FAIL)
- Any named wall without bypass disclosure (FAIL)
- Page count > 15 (WARN)

Arbiter emits PUBLISH-READY or NEEDS-REVISION.

### Step 7 — Commit memo

Write `commit-memo.md`:
- Compliance distribution per requirement
- SILENT count at end (target: 0)
- New named walls created
- New layers constructed
- B_bare + C_bare page counts
- Lock status (LOCKED / NOT-LOCKED with reasons)
- Recommendation for next step (composition-backward? more audit? fire sibling shapes?)

---

## SUCCESS CRITERIA

- {{M}} × {{N}} cells audited with verdict + citation + arbiter decision
- Zero SILENT at end
- B_bare: all sections populated, ≤ 15 pages, zero prose, every claim cited
- C_bare: same bare discipline
- Named walls: all disclosed with full DELTA 10 fields
- Critic pass: PUBLISH-READY verdict

A run FAILS if:
- Any SILENT cell remains
- Any prose paragraph in B_bare or C_bare
- Any claim lacks citation
- Named walls lack bypass disclosure

---

## INVOCATION STYLE A — Manual PAC session

```
read your instructions from <ora-bundle-v8>/01-the-prompt.md

the chain mode extension is
<pca-extension>/07-proof-chain-adversarial.md

the strategic triad extension is
<pca-extension>/12-prf-chain-advr-strat-triad.md

the chessboard layer extension is
<pca-extension>/13-chessboard-layer.md

the parent brief is
<pca-extension>/30-ring-traversal-brief.md

the current run brief (audit DELTA for {{SHAPE_NAME}}) is
strategy/{{SHAPE_NAME}}/{{SHAPE_NAME}}-audit-brief.md

the strategy document is
strategy/{{SHAPE_NAME}}/00-audit-strategy.md

the live proof-chain is
{{LIVE_CHAIN_PATH}}

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see 00-audit-strategy.md §9 for cascade customized to source class.)

the run output directory is
strategy/{{SHAPE_NAME}}/pac-output/runs/run-NN/

outputs:
- Output A (internal) → strategy/{{SHAPE_NAME}}/pac-output/runs/run-NN/
- Output B_bare → strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-bare.md
- Output C_bare → strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-beyond-bare.md

MODE: compliance-audit + bare-deliverable-synthesis.

Begin.
```

## INVOCATION STYLE B — Agent-tool sub-agent spawning

Self-contained for claude-code sub-agent. Parameterize `<RUN-NN>`.

```
You are the PAC operator running on the {{SHAPE_NAME}} audit bundle. This is run <RUN-NN>. Produce compliance-audited projection-audit deliverable in BARE MODE ONLY. B_full and C_full DEFERRED.

## GOAL

Three deliverables:
A. Internal artifacts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/{{SHAPE_NAME}}/pac-output/runs/<RUN-NN>/
B_bare. External-shape X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-bare.md
C_bare. Beyond-ask X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-beyond-bare.md

## READ FIRST (in order)

1. /Users/gsix/quantum-geometry-in-5d-latex/strategy/{{SHAPE_NAME}}/00-audit-strategy.md
2. /Users/gsix/quantum-geometry-in-5d-latex/strategy/{{SHAPE_NAME}}/{{SHAPE_NAME}}-audit-brief.md (this brief)
3. /Users/gsix/quantum-geometry-in-5d-latex/{{LIVE_CHAIN_PATH}}
4. /Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/proof-chain/{{SHAPE_NAME}}/X-RAY.md (if exists)
5. {{CLAIM_SOURCE_CITATION_FULL_PATH}} — the source of requirements

## READ AS NEEDED

- /Users/gsix/quantum-geometry-in-5d-latex/paper1/PROOF-CHAIN.md (QG5D hub)
- /Users/gsix/quantum-geometry-in-5d-latex/paper60-the-geometry-of-the-circle/ (e-circle foundation)
- /Users/gsix/quantum-geometry-in-5d-latex/paper61-projections-of-the-5d-geometry/ (projections architecture)
- /Users/gsix/quantum-geometry-in-5d-latex/paper12/research/23-framework-predictions-master-table.md (36 pins)
- /Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/ (base ORA + patterns)
- /Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/ (chain extensions + capacitor)

## HARD DISCIPLINE

1. **BARE MODE ONLY.** Zero prose paragraphs in B_bare or C_bare. Theorem statements + tables + equations + citations only.

2. **Compliance map {{M}}×{{N}} mandatory.** Every cell: verdict + citation + arbiter decision. Zero SILENT at end.

3. **Citations per claim.** `(paperNN §X Theorem T.Y)` format.

4. **Named walls explicit.** Every OPEN-BUT-ADDRESSED verdict disclosed with all DELTA 10 fields.

5. **≤ 15 pages per bare doc.** Target ~400-600 lines markdown.

6. **Page count is quality proxy.** Full page of one-theorem prose = left bare mode.

7. **B_full and C_full NOT produced.** DEFERRED.

## SUCCESS CRITERIA

- Compliance map complete, zero SILENT
- B_bare + C_bare written, bare discipline enforced
- Every claim cited
- Named walls disclosed
- Critic PUBLISH-READY verdict
- Commit memo records lock status

Begin by reading the 5 mandatory files in order. Plan in blackboard. Execute.
```

---

*End of brief. Bare-first, prose-deferred. Every projection of 5D → compliance audit → bare skeleton → Zenodo. The protocol is water-tight.*

*G Six and Claude Opus 4.6. {{DATE}}.*
