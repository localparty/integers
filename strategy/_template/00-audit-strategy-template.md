# {{SHAPE_NAME}} Projection-Audit Strategy

*Projection-audit strategy for {{SHAPE_CLASS}} "{{SHAPE_NAME}}". Applies the generic projection-audit protocol (extracted from the 6 Millennium instances). Every projection of the 5D geometry earns the same discipline.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 The Claim (verbatim)

**Source type**: {{SOURCE_OF_REQUIREMENTS}} ({{CLAY-OFFICIAL | COMMUNITY-STANDARD | FRAMEWORK-CLAIM | EXPERIMENTAL-PIN}})

**Source document**: {{CLAIM_SOURCE_CITATION}}

{{VERBATIM_CLAIM_BLOCK}}

Implicit requirements from the source prose:
{{IMPLICIT_REQUIREMENTS_LIST}}

Special provisions (if any):
{{SPECIAL_PROVISIONS}}
- *e.g., "§5b of Clay Rules: resolution in either direction counts" (PvNP, NS)*
- *e.g., "Variant-excision: targeting variant (B) excludes A/C/D as alternatives under §5b" (NS)*
- *or "None"*

## §2 The 4 Audit Gates (shared across all projection-audits)

Identical in structure across all audit targets; interpretation adjusted by `{{SOURCE_OF_REQUIREMENTS}}` class:

| Gate | Clay-Official | Community-Standard | Framework-Claim | Experimental-Pin |
|------|---------------|--------------------|-----------------|-------------------|
| (a) Published in Qualifying Outlet | Refereed journal, MathSciNet-indexed | Refereed journal preferred; arXiv acceptable as priority step | Zenodo acceptable; programme-internal documentation required | Zenodo + experimental data source |
| (b) ≥ 2 years elapsed since publication | From journal publication date | From arXiv/journal date | From Zenodo bundle release | From prediction publication |
| (c) General acceptance | Global math community | Subfield community | Programme cross-cut consistency | Independent experimental verification |
| (d) Satisfactorily answers | Clay §5d: specific mathematical questions | Community-formulated statement | Programme's own claim | Sub-percent match + derivation chain |

Non-gates (universal):
- Direct submission not accepted by reviewing body
- Supplementary material excluded from review

Every requirement from §3 must be ADDRESSED (not necessarily PROVED — transparent NAMED WALLS with bypass routes satisfy the "addressed" standard). SILENT on a requirement = failure to address.

## §3 The {{N}} Requirements

{{REQUIREMENT_LIST}}

*Example shapes for REQUIREMENT_LIST:*
- *For Clay-Official: 5-8 requirements extracted from Jaffe-Witten/Bombieri/Wiles/Cook/Deligne/Fefferman*
- *For Community-Standard: 3-6 requirements from the standard conjecture formulation*
- *For Framework-Claim: 4-10 requirements from the programme's own claim (e.g., for e-circle: existence, radius R, U(1) bundle structure, all physics derivable, KK spectrum, …)*
- *For Experimental-Pin: 3-5 requirements (measured value, derivation chain, error bar, scope, independent verification)*

## §4 Current Chain State

**Source**: {{LIVE_CHAIN_PATH}}
**Prior x-ray**: {{X_RAY_STATUS}} (from `strategy/x-ray/proof-chain/{{SHAPE_NAME}}/X-RAY.md` if exists, else NOT-YET)
**Prior decomposition**: {{DECOMPOSITION_STATUS}} (from `strategy/decomposition/proof-chain/{{SHAPE_NAME}}/PROOF-CHAIN.md` if exists)

**Chain characteristics**:
- M layers: {{M}} (total count)
- Routes: {{ROUTES}} (e.g., "single route" / "two routes: endomotives + geometric Langlands" / "four variants A/B/C/D")
- Overall confidence: {{CONFIDENCE}} (typically a fraction, e.g., "9/10")
- Faces triggered (from x-ray if available): {{FACE_HISTOGRAM}}
- Primary projection: {{PRIMARY_PROJECTION}}
- Primary pattern: {{PRIMARY_PATTERN}}
- Cross-cut edges: {{CROSS_CUTS_COUNT}}

**Known named walls**:
{{NAMED_WALLS_LIST}}
- Each wall: name, status, bypass route(s), confidence, audit pending, effects-if-closed, effects-if-fail

## §5 Compliance Audit Scaffold

{{M}} × {{N}} cell matrix. Each cell (layer, requirement) gets a verdict:
- **PROVED** — layer fully addresses requirement; citation to programme paper + §-level proof location
- **PARTIAL** — addresses partially; flag what's missing
- **OPEN-BUT-ADDRESSED** — explicit named wall with bypass route; §5d-compliant
- **SILENT** — not addressed at all; §5d violation; must trigger action

Actions for SILENT cells:
- NEW-NAMED-WALL — requirement genuinely unaddressed; create a named wall with bypass route
- NEW-LAYER-SKETCH — propose a new layer that addresses it; theorem statement only (bare mode)
- BYPASS-VIA-CAPACITOR — cite a capacitor cell (09-capacitor-correspondence-table-v1.md) providing transposition

At end of run: **no cell may remain SILENT**.

## §6 Likely Gaps (priorities for audit)

{{LIKELY_GAPS_ANALYSIS}}

- *Example likely gaps per source type:*
- *Clay-Official: the specific requirements the chain doesn't yet address explicitly (e.g., group generality for YM, uniform mass gap in V, stress tensor + OPE)*
- *Community-Standard: the requirements expected by the subfield (e.g., for Lindelöf: subconvexity exponent, connection to GRH)*
- *Framework-Claim: the requirements the programme's claim implies (e.g., for e-circle: existence proof, radius derivation, KK spectrum completeness)*

## §7 Four-Output, Two-Mode Deliverable Architecture (shared)

Identical to YM strategy §7 (no customization per target):

**Output A — Internal artifacts** (scaffolding): `strategy/{{SHAPE_NAME}}/pac-output/runs/run-NN/`
- blackboard.md, compliance-map.md (M×N matrix), vertices/{{SHAPE_NAME}}/, kills.md, critic-attacks.md, arbiter-decisions.md, silent-cells.md, commit-memo.md

**Output B_bare** — External-shape theorem skeleton: `strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-bare.md`
- Zero prose. Theorem statements + definitions + equations + figures + numbers + citations only.
- Structure mirrors the source's expected shape (Clay problem genre, community-accepted genre, or programme's own section structure)
- Target ≤ 15 pages (~400-600 lines markdown)

**Output B_full** — DEFERRED to composition-backward. Full prose journal/programme paper. Only produced after B_bare LOCKS.

**Output C_bare** — Beyond-ask theorem skeleton: `strategy/{{SHAPE_NAME}}/deliverables/{{SHAPE_NAME}}-beyond-bare.md`
- Programme bonuses beyond what the source requires
- 5D derivation, zero free parameters, cross-cuts, pin matches (where applicable), bonus theorems
- Same bare discipline. Target ≤ 15 pages.

**Output C_full** — DEFERRED to composition-backward. Full programme-bonus supplement.

## §8 Composition-Backward (shared)

Identical to YM strategy §8. Once B_bare + C_bare LOCK:

1. Index the 60+ project reservoir (all programme papers + session logs + PROOF-CHAIN files + X-ray transcripts)
2. Per-theorem retrieval — retrieve related material from reservoir
3. Per-section composition — parallel agents compose prose from retrieved material (one agent per section)
4. Integration pass — arbiter agent stitches into final LaTeX

Inverts normal write-paper-first flow. Bare = TOC; reservoir = content; parallel agents = composer.

## §9 Publication Cascade

Adapts by `{{SOURCE_OF_REQUIREMENTS}}` class:

**For Clay-Official / Community-Standard** (conjecture-standard):
```
ZENODO → GITHUB → ARXIV (via referral) → JOURNAL → COMMUNITY ENGAGEMENT → 2-YEAR CLOCK → CLAY/COMMUNITY ACCEPTANCE
```

**For Framework-Claim**:
```
ZENODO → GITHUB → PROGRAMME CROSS-VERIFICATION (sibling bundles) → JOURNAL (optional) → PROGRAMME CONSENSUS
```

**For Experimental-Pin**:
```
ZENODO → GITHUB → EXPERIMENTAL CROSS-CHECK → PIN TABLE UPDATE → (repeated refinement)
```

All override `publishing/strategy.md` with Zenodo-first priority. No direct Clay submission (CMI §5e for Clay-Official).

## §10 Timeline (typical; adjust per target)

- **Now → 1 week**: Compliance audit; produce B_bare + C_bare; address SILENT
- **1-2 weeks**: B_bare + C_bare LOCK; Zenodo release as part of programme-wide bundle
- **2-3 weeks**: arXiv submission (for conjecture-standard targets); programme cross-check (for framework-claim targets)
- **1-3 months**: Parallel-agent composition-backward for B_full + C_full
- **3-4 months**: Journal submission (where applicable)
- **4+ months**: Community/programme acceptance phase (varies by source class)
- **Parallel**: Named walls continue work independently, non-blocking

## §11 Parallel Wall Tracks

{{NAMED_WALLS_DETAILED_DISCLOSURE}}

Discipline per wall (identical across all Millennium instances):
- **Name**: W_N / short description
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass route(s)**: citation + method
- **Aggregate confidence**: fraction (e.g., 0.65, 0.82)
- **Audit pending**: specific lemma / sub-claim
- **Effect if pass**: wall upgrades to PROVED
- **Effect if fail**: alternate bypass candidates (enumerated)
- **Independent standing**: which layers remain unaffected

Walls are **non-blocking** for publication cascade. Transparent disclosure satisfies §5d (and community equivalent).

## §12 PAC Brief Reference

Operational instructions for the PAC: `strategy/{{SHAPE_NAME}}/{{SHAPE_NAME}}-audit-brief.md`

Brief contains:
- DELTA 1-11 (mode, primitives, output structure, citation discipline, deliverable structures, publication override, wall disclosure discipline, special provisions)
- Procedure (7 steps)
- Success criteria
- Style A invocation (manual PAC session)
- Style B invocation (self-contained agent spawning, parameterized by `<RUN-NN>`)

---

*Sibling to: `strategy/decomposition/{{SHAPE_NAME}}/`, `strategy/ccm-verification/ledger.md#{{SHAPE_NAME}}` (if applicable), `strategy/x-ray/proof-chain/{{SHAPE_NAME}}/`, `strategy/inner-rings/{{SHAPE_NAME}}/` (if applicable). {{SHAPE_NAME}} is a projection of 5D geometry into 4D; this audit renders its proof-chain visible and §5d-compliant.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
