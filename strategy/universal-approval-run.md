# Universal Approval Run

*A single self-contained agent prompt that executes the full Universal Approval pipeline end-to-end. IDEMPOTENT — re-firing picks up only what's new or updated since last run. Designed for cycle-based convergence: run → audit → run → audit → ... until the programme stabilizes.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## WHAT THIS RUN DOES

This single prompt replays (and extends) the work-flow executed 2026-04-13 → 2026-04-14 that produced the programme's Zenodo-priority deliverables:

1. Inspects the `strategy/`, `visualization/`, `integers/paper*`, `solutions/paper*`, and `solutions-with-prize/paper*` directories to establish current state <!-- legacy 2026-04-14: was `paper*` (flat at repo root); migrated to three-corpus paths (Intervention 6). -->
2. Scans the web for prizes, outlets, journal targets, and competitor-landscape per vertex (Universal Approval research)
3. Generates or updates PAC strategy documents and briefs per vertex, parameterized from `strategy/_template/`
4. Dispatches compliance audits per vertex (Phase A of the 3-run cadence)
5. Dispatches **three-pillar bare-synthesis** runs per vertex (COMPLY / INDEPENDENT / CONTRIBUTE in parallel; Phase B)
6. Rebuilds both visualizations (main 43-shape viewer + torus viz)
7. Integrates Universal Approval acknowledgments into all beyond-bare files
8. Diffs the state, logs deltas, emits recommendations for the next cycle

## THE THREE PILLARS (the Universal Strategy)

Every vertex ships **three compliance-class deliverables** plus the programme-bonuses supplement. Together they form the water-tight Universal Approval claim — complete in compliance, free where possible, hardened where dependent.

### PILLAR A — COMPLY

Satisfies the prize's stated requirements (Clay / community / framework). Named walls transparently disclosed per §5d. Journal-submittable as-is even with open named walls.

- **Bar**: every requirement ADDRESSED (not necessarily PROVED); walls disclosed with bypass route
- **Deliverable**: `strategy/<vertex>/deliverables/<vertex>-comply-bare.md` (pure theorem skeleton, zero prose, ≤ 15 pages)

### PILLAR B — INDEPENDENCE

Dependency-free where possible. Every external conditional is BYPASSED or EXCISED via PAC primitives (BYPASS / DECOMPOSE / EXCISE / TRANSPOSE-via-capacitor). No link survives as "conditional on external unproved claim"; every leaf roots in QG5D / paper1 / literature / classical.

- **Bar**: zero links CONDITIONAL on external unproved claims; every open wall is smaller and more specific than what Pillar A admits
- **Deliverable**: `strategy/<vertex>/deliverables/<vertex>-independence-bare.md`
- **Competitive moat**: this is where other contenders stall — their proofs retain external conditionality. Our PAC primitives exist precisely for this work.

### PILLAR C — CONTRIBUTE (the double kill)

Every external dep we RETAIN (non-QG5D, non-paper1, non-literature, non-classical — i.e., unproved externals like CCM 2025, Standard Conjecture D, motivic BC extension, preprint claims we rely on) gets the PAC treatment applied to ITS chain: x-ray it, visualize it, compliance-audit it, apply VERIFY / CONSTRUCT / BYPASS / DECOMPOSE / EXCISE to its weak links. We depend on it AND we publish it stronger.

- **Bar**: every retained external dep has a published hardening artifact showing what we improved
- **Deliverable**: `strategy/<vertex>/deliverables/<vertex>-harden-bare.md`
- **Narrative**: *"We depend on X AND we strengthened X. The field is now stronger. No other contender has done this."*

### Plus the programme-bonuses supplement (orthogonal)

- **Deliverable**: `strategy/<vertex>/deliverables/<vertex>-beyond-bare.md` (5D derivation, pins, cross-Clay connections, bonus theorems, **§N Related Work & Acknowledgments** drawn from landscape.md)
- This is NOT a pillar — it is the "what the programme offers beyond what the prize asks" supplement, sibling to all three pillars

### Relation to existing bundles

- `strategy/ccm-verification/` = Pillar C instance for CCM 2025 (generalizes to `strategy/externals-hardening/<external>/` per major retained external)
- `strategy/decomposition/` = feeds Pillar B (provides the sub-chain expansions)
- `strategy/x-ray/` = feeds all three pillars (geometric annotation applied to our layers AND to external layers in Pillar C)
- `strategy/_research/<vertex>/landscape.md` = feeds the beyond-bare Acknowledgments AND the Pillar B/C competitive narrative

### Per-vertex full deliverable set

For each vertex in the roster, the first cycle produces (bare fidelity):

1. `<vertex>-comply-bare.md` (Pillar A)
2. `<vertex>-independence-bare.md` (Pillar B)
3. `<vertex>-harden-bare.md` (Pillar C)
4. `<vertex>-beyond-bare.md` (programme bonuses)

Full-fidelity prose versions (suffix `-full.md`) are DEFERRED to composition-backward.

### Visualization

The main viewer's per-vertex ladder gains **three tracks**:

- Comply-status: strategy / brief / compliance / comply-bare / comply-full / ...
- Independence-status: independence-bare / independence-full / locked
- Harden-status: externals enumerated / x-rayed / hardened / published

Readers instantly see which pillar each vertex has reached.

## HOW TO INVOKE

```
You are the Universal Approval orchestrator. Execute the full pipeline at
/Users/gsix/quantum-geometry-in-5d-latex following the protocol below.
Work idempotently — do not redo work that is already current.
Log every decision and delta.

Read strategy/universal-approval-run.md for the full protocol and execute it.
```

Pass this to a local Claude Code agent (or fire as a sub-agent via the Agent tool).

## PHASE 0 — READ THE NORTH STAR (MANDATORY, NOT OPTIONAL)

**Goal**: Load the programme's north star as the governing variable. The north star defines vision, strategy, and success criteria — if anything in this protocol conflicts with it, the north star wins.

### 0.1 Read

Read the full content of `/Users/gsix/quantum-geometry-in-5d-latex/strategy/north-star.md`. Do NOT skim. Do NOT skip this phase. Any cycle that skips Phase 0 is non-compliant and must be re-run.

### 0.2 Apply

Hold the following in working memory throughout every subsequent phase:

- **Vision**: Universal Approval (all 25 ring + framework vertices water-tight, rooted in QG5D, ship to Zenodo, contribute back more than we take)
- **Three pillars**: COMPLY / INDEPENDENT / CONTRIBUTE (+ beyond-bonuses supplement)
- **Mode matrix**: {COMPLY, INDEPENDENT, CONTRIBUTE} × {MATH, PROSE}; default `all:math`
- **Publication cascade**: Zenodo → GitHub → arXiv → journal → 2-year Clay clock
- **Fair-attribution ethic**: HONOR / RECOGNIZE / SHOWCASE / POSITION / SOURCE
- **Competitive moat**: Pillar C (CONTRIBUTE) is the unique move no contender has made
- **Ring architecture**: bouquet of 6 circles at QG5D; every mathematical shape = projection of 5D into 4D
- **Success criteria**: cycle-level (convergence = byte-identical snapshots) + deliverable-level + publication-level + field-level + universal-approval-level

### 0.3 Variable discipline

If the north star changes between cycles (user edits it), the next run picks up the new variable values automatically. The protocol is NORTH-STAR-DRIVEN, not self-contained.

If the north star is MISSING at Phase 0 (file doesn't exist), the orchestrator MUST HALT and emit a critical-error log. Do not proceed to Phase 1 without it.

---

## THE MODE MATRIX (reference — defined in north-star.md §3)

Three pillars × two fidelity modes = 6 deliverable classes per vertex:

| Pillar \ Mode | MATH (science, no prose) | PROSE (full paper) |
|---|---|---|
| COMPLY | `<vertex>-comply-math.md` | `<vertex>-comply-prose.md` (deferred) |
| INDEPENDENT | `<vertex>-independent-math.md` | `<vertex>-independent-prose.md` (deferred) |
| CONTRIBUTE | `<vertex>-contribute-math.md` | `<vertex>-contribute-prose.md` (deferred) |

Plus orthogonal beyond-bonuses: `<vertex>-beyond-math.md` (always produced) + `<vertex>-beyond-prose.md` (deferred).

**Default: `all:math`** — produce all three pillars in math mode. PROSE mode deferred to composition-backward (separate future phase, not in cycle N).

**Naming transition (as of 2026-04-15)**: existing `<vertex>-{comply,independence,harden,beyond}-bare.md` files are equivalent to the new `-math.md` suffix naming; Pillar B "INDEPENDENCE" renamed to "INDEPENDENT"; Pillar C "HARDEN" renamed to "CONTRIBUTE". Internal cross-references in existing files remain valid during the rename transition. A dedicated convergence cycle can perform the file-rename pass when the orchestrator has capacity.

### PROSE-mode Verification Appendix discipline (mandatory)

Every PROSE-mode deliverable (`<vertex>-<pillar>-prose.md` for any pillar A/B/C and beyond) MUST include a final section titled `## Appendix V — Verification`. For every theorem, lemma, or named claim in the paper's body, the Verification Appendix contains one traceable entry:

- **Label** (T.N / L.M / Theorem-name)
- **Statement** (repeated for reviewer convenience)
- **Derivation chain** — the step-by-step chain from ℤ + ZFC to the claim (drawn from `strategy/<vertex>/pac-output/*/compliance-map.md`)
- **PAC VERIFY status** — PROVED / PARTIAL / OPEN-BUT-ADDRESSED + citation to the specific run
- **Arbiter verdict** — PUBLISH-READY (or repairs applied)
- **Critic attacks resolved** — dissents raised during audit + arbiter decisions
- **Transcript links** — absolute paths to blackboard / critic-attacks / arbiter-decisions for that theorem's audit
- **Projection discipline** — which $P_i$ preservation class the claim sits in (per `strategy/north-star.md` §0.9)

**Composition-backward**: when the future composition-backward phase generates PROSE deliverables, the Verification Appendix is assembled by a parallel sub-agent-per-theorem. The PAC work was already done in earlier cycles; the appendix surfaces it.

**Why this exists (G's observation, 2026-04-15)**:

> *"i haven't figured out how to collect the demonstrations of the APPROVED of every theorem of Integers, maybe we need to include a phase in the PROSE mode that will collect/generate EVERY verification as an appendix?"*

The Verification Appendix is the resolution. Every theorem in every PROSE paper ships with its audit trail attached. Reviewers don't take the theorem on trust — they see the demonstration. Pillar C (CONTRIBUTE) reciprocity intensifies: we don't just claim to have derived things; we ship the derivations in auditable form.

Uniform naming across 62 papers (`Appendix V — Verification`) signals rigor and cohesion.

---

## PHASE 1 — STATE INSPECTION

**Goal**: Establish what exists NOW. No modifications. Output: `strategy/_research/state-<timestamp>.md`.

Inspect and record:

<!-- legacy 2026-04-14 (Intervention 6): Phase 1.1 scanned flat paper dirs at repo root. After three-corpus reorganization, paper dirs live under `integers/` (Corpus 1, 13 foundational papers), `solutions/` (Corpus 2, 16 non-prize conjecture papers), and `solutions-with-prize/` (Corpus 3, 8 prize-carrying papers). Paper 9 remains deprecated at root (`paper9/` with redirect README); papers 49/50 remain at root as ABSORBED stubs. -->

### 1.1 Strategy directory inventory

For each directory under `strategy/`, list:
- Presence of `00-*-strategy.md` (millennium-strategy or audit-strategy)
- Presence of `<vertex>-*-brief.md`
- Presence of `pac-output/runs/run-NN/` and whether commit-memo.md says LOCKED
- Presence of `deliverables/<vertex>-bare.md` and `<vertex>-beyond-bare.md`

### 1.1.bis Three-corpus paper roster scan (post-Intervention 6, 2026-04-14)

Scan the three corpus directories — NOT flat `paper*/` at repo root:
- `integers/` — 13 foundational derivation papers (Corpus 1). See `integers/README.md`.
- `solutions/` — 16 non-prize community-standard conjecture papers (Corpus 2). See `solutions/README.md`.
- `solutions-with-prize/` — 8 prize-carrying papers (Corpus 3). See `solutions-with-prize/README.md`.

Also scan (but do NOT treat as corpus members): `paper9/` (deprecated redirect), `paper49-ccm-replacement/` and `paper50-h4-replacement/` (ABSORBED stubs), and the unclassified paper14-25, paper27-hodge, paper27-navier dirs still at repo root.

### 1.2 Canonical PROOF-CHAIN inventory

<!-- legacy 2026-04-15: "For each `paper*/PROOF-CHAIN.md`, record: ..." (before centralization). After Intervention 2, live PROOF-CHAIN files are canonical at `strategy/proof-chain/<vertex>/PROOF-CHAIN.md`; paper dirs hold `PROOF-CHAIN-MOVED.md` stubs only. See `strategy/proof-chain/README.md` and `strategy/self-healing-log.md` (2026-04-15 Intervention 2). -->

For each `strategy/proof-chain/<vertex>/PROOF-CHAIN.md`, record:
- Vertex name (from directory name)
- Line count
- Last modification date
- Status tags (PROVED / CONDITIONAL / PARTIAL / OPEN)
- Named walls mentioned

The canonical live PROOF-CHAINs are under `strategy/proof-chain/`. Paper dirs hold only the `PROOF-CHAIN-MOVED.md` stub (reference pointer); do NOT scan paper dirs for live chain state. The preprint-subdir `{integers,solutions,solutions-with-prize}/paper*/preprint/PROOF-CHAIN.md` files are referee-facing publication snapshots, NOT live state — skip them here. <!-- legacy 2026-04-14 Intervention 6: was `paper*/preprint/PROOF-CHAIN.md` (flat at repo root); migrated to three-corpus paths. -->

### 1.3 X-ray / decomposition / ccm-verification status

For each bundle, list which vertices have artifacts.

### 1.4 Research status

For each `strategy/_research/<vertex>/`, record:
- Presence of `outlet.md`
- Presence of `landscape.md`
- Last modification

### 1.5 Visualization status

Inspect `visualization/data.js` and `visualization/torus/data.js`:
- Build timestamp
- Shape count
- AUDIT PENDING count

### 1.6 Ring vertex roster

Canonical list (25 vertices + 4 framework target classes = 29 entries):

**Millennium (6):** ym, rh, bsd, pvnp, hodge, ns

**Non-Millennium ring (19):** lindelof, grh, h12, turbulence, baum-connes, vp-vs-vnp, bgs, katz-sarnak, twin-primes, cramer, goldbach, abc, opn, collatz, lehmer, sato-tate, schanuel, hilbert-6

**Core:** qg5d

**Framework targets:** inner-rings (5 branches), shapes (e-circle, bouquet, 36-pin, chord-graph, face-graph, south-trough), projection-operators (P_A, P_B, P_C, P_D, P_E, P_O)

## PHASE 2 — WEB RESEARCH (parallel)

**Goal**: Fill or refresh outlet and landscape data per vertex. Only works on GAPS or STALE entries.

### 2.1 Identify gaps

- Any non-framework vertex without `strategy/_research/<vertex>/outlet.md` → schedule outlet research
- Any non-framework vertex without `strategy/_research/<vertex>/landscape.md` → schedule landscape research
- Any entry older than 90 days → flag STALE, schedule refresh

### 2.2 Dispatch outlet research (parallel sub-agents, batch 5-8 at a time)

Per-vertex outlet research sub-agent prompt template:

```
You are the outlet-research sub-agent for <VERTEX>. WebSearch for the official
problem statement, any prize (foundation, amount, year, conditions), typical
publication journals, community-accepted formulation variants, and key references.
Write output to strategy/_research/<VERTEX>/outlet.md using the 7-field structure
from strategy/_research/outlet-survey.md. Save PDFs of authoritative documents
to strategy/_research/<VERTEX>/pdfs/.
```

Run 5-8 per-vertex outlet agents in parallel. Accumulate. Merge updates into `strategy/_research/outlet-survey.md`.

### 2.3 Dispatch landscape research (parallel sub-agents, batch 5-8 at a time)

Per-vertex landscape research sub-agent prompt template:

```
You are the landscape-research sub-agent for <VERTEX>. WebSearch for current
key researchers, major approaches, named milestones, recent preprints (2023-2026),
key surveys. Write output to strategy/_research/<VERTEX>/landscape.md using the
6-field structure from strategy/_research/landscape-survey.md. Honor every
approach; tone is complementary, never dismissive. Acknowledgment suggestions
per Universal Approval protocol.
```

Run 5-8 per-vertex landscape agents in parallel. Merge updates into `strategy/_research/landscape-survey.md`.

### 2.4 Gate check

After research lands, verify every non-framework vertex now has both `outlet.md` AND `landscape.md`. Flag any NEEDS-VERIFICATION for later review.

## PHASE 3 — BRIEF GENERATION / UPDATE

**Goal**: Every vertex in the roster has a strategy doc + brief that reflects current research. Idempotent — only touch GAPS or STALE.

### 3.1 Identify gaps

- Any non-framework vertex without `strategy/<vertex>/00-*-strategy.md` → generate
- Any vertex with a strategy doc but newer outlet.md or landscape.md than the strategy → regenerate (data may have changed)
- Any framework target (qg5d, inner-rings, shapes, projection-operators) — use `framework-claim` source type from `strategy/_template/`

### 3.2 Dispatch brief-generation sub-agents (parallel)

Per-vertex brief-gen prompt template:

```
You are the brief-generation sub-agent for <VERTEX>. Read strategy/_template/
(README + 00-audit-strategy-template.md + audit-brief-template.md). Read
strategy/_research/<VERTEX>/outlet.md AND landscape.md (if exists). Read the
live canonical PROOF-CHAIN at strategy/proof-chain/<VERTEX>/PROOF-CHAIN.md
(if exists). Generate or UPDATE
strategy/<VERTEX>/00-audit-strategy.md and strategy/<VERTEX>/<VERTEX>-audit-brief.md
following the template verbatim — customize only the six parameters
(SHAPE_NAME, PAPER_REFERENCE, SOURCE_OF_REQUIREMENTS, N-REQUIREMENTS-LIST,
NAMED-WALLS, SPECIAL-PROVISIONS). Preserve any existing content that remains
valid (diff-then-merge, do NOT wholesale overwrite).

<!-- legacy 2026-04-15: "Read the live paper<NN>-<vertex>/PROOF-CHAIN.md (if exists)." Migrated to strategy/proof-chain/<VERTEX>/PROOF-CHAIN.md per Intervention 2 (2026-04-15). -->
```

For Millennium vertices (ym/rh/bsd/pvnp/hodge/ns) that already have `00-millenium-strategy.md` and `<vertex>-millenium-brief.md`, UPDATE them with new landscape data rather than renaming.

### 3.3 Universal Approval integration (subsumed into brief-gen)

Every brief's DELTA 6 (C_bare structure) must now include:

```
§N Related Work & Acknowledgments

Table: Researcher | Institution | Contribution
(Drawn from strategy/_research/<VERTEX>/landscape.md)

Paragraph per major approach:
(Drawn from landscape.md §"Major Approaches")

Our programme's position paragraph:
(Drawn from landscape.md §"Our programme's position")
```

Brief-gen sub-agents inject this section into the C_bare structure when generating or updating.

## PHASE 4 — COMPLIANCE AUDIT DISPATCH (parallel)

**Goal**: Every non-framework vertex with a strategy+brief has a LOCKED compliance map.

### 4.1 Identify gaps

- Any vertex with strategy+brief but no `pac-output/runs/run-NN/compliance-map.md` → schedule compliance audit
- Any vertex where compliance-map.md exists but commit-memo.md does NOT say LOCKED → schedule re-run

### 4.2 Dispatch compliance-audit sub-agents (parallel, 3-5 at a time)

Per-vertex compliance-audit prompt template: derived from `strategy/ym/pac-output/runs/run-02/` prompt (the YM compliance-audit pilot). The master orchestrator should template this:

```
You are the PAC compliance-audit operator for <VERTEX>. Read strategy/<VERTEX>/
00-*-strategy.md and <VERTEX>-*-brief.md. Read the canonical live PROOF-CHAIN
at strategy/proof-chain/<VERTEX>/PROOF-CHAIN.md and the x-ray annotation at
strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md (if exists). Build M×N
compliance map per DELTA 4 format. Address all SILENT verdicts. Write to
strategy/<VERTEX>/pac-output/runs/run-NN/ with lock status in commit-memo.md.
Do NOT produce B_bare or C_bare this run.

<!-- legacy 2026-04-15: "Read paper<NN>-<vertex>/PROOF-CHAIN.md and strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md ..." Migrated per Intervention 2 (2026-04-15). -->
```

Run 3-5 parallel compliance audits. Pause before proceeding to Phase 5 — let the user review lock verdicts.

## PHASE 5 — THREE-PILLAR BARE SYNTHESIS DISPATCH (parallel)

**Goal**: Every vertex with LOCKED compliance has four bare deliverables in PUBLISH-READY state: comply + independence + harden + beyond.

Phase 5 splits into three pillar dispatches plus the bonuses supplement, each its own sub-agent type. Fire per vertex in parallel where possible.

### 5A — COMPLY synthesis

**Goal**: Pillar A deliverable per vertex.

#### 5A.1 Identify gaps

- Any vertex with LOCKED compliance but no `deliverables/<vertex>-comply-bare.md` → schedule COMPLY synthesis

Note: for the 6 Millennium vertices that already have `<vertex>-bare.md` (from run-03 era), rename in spirit to `<vertex>-comply-bare.md` — preserve the file content, update naming going forward. New vertices go straight to the new name.

#### 5A.2 Dispatch COMPLY sub-agents

Per-vertex prompt template (derived from `strategy/ym/` run-03):

```
You are the PAC COMPLY-synthesis operator for <VERTEX>. Read strategy/<VERTEX>/
00-*-strategy.md and <VERTEX>-*-brief.md. Read the locked compliance-map.md.
Produce <vertex>-comply-bare.md in BARE MODE — theorem skeleton satisfying every
prize/community/framework requirement. Named walls disclosed per DELTA 10. Zero
prose. Target ≤ 15 pages.
```

Run 3-5 parallel vertex COMPLY synthesizers.

### 5B — INDEPENDENCE synthesis

**Goal**: Pillar B deliverable per vertex. This is where PAC primitives do the heavy lifting.

#### 5B.1 Identify gaps

- Any vertex with LOCKED compliance but no `deliverables/<vertex>-independence-bare.md` → schedule INDEPENDENCE synthesis

#### 5B.2 Dispatch INDEPENDENCE sub-agents

Per-vertex prompt template:

```
You are the PAC INDEPENDENCE-synthesis operator for <VERTEX>. For each
CONDITIONAL or OPEN-BUT-ADDRESSED cell in the compliance map, apply one of:
- BYPASS: route via a different proof path
- DECOMPOSE: break into PROVED sub-links
- EXCISE: remove as unnecessary
- TRANSPOSE: route via capacitor cell (09-capacitor-correspondence-table-v1.md)
For each successful lift, record the primitive used + the new proof route.
Produce <vertex>-independence-bare.md in BARE MODE showing the dep-free chain.
Every leaf must root in QG5D / paper1 / literature / classical. Zero
prose, ≤ 15 pages.
```

This sub-agent is HEAVIER than COMPLY because it actively runs PAC primitives per conditional cell. Expect 2-4x the work time. Run 2-3 parallel vertex INDEPENDENCE synthesizers max.

If a conditional cell CANNOT be lifted (genuinely unbypassable external dep), that dep goes on the Pillar C worklist.

### 5C — CONTRIBUTE synthesis (the double kill)

**Goal**: Pillar C deliverable per vertex + new bundles under `strategy/externals-hardening/<external>/` per major retained external.

#### 5C.1 Enumerate retained external deps

For each vertex, pull the list of external deps that SURVIVED Pillar B (i.e., the deps we retained because they couldn't be bypassed). Common examples across the ring:

- **CCM 2025 (arXiv:2511.22755)** — primary retained external for RH / bgs / grh / goldbach / cramer
- **Standard Conjecture D (motivic)** — Hodge / Baum-Connes
- **Balaban RG** — YM (though much is already LITERATURE — verify)
- **Kolyvagin's theorem + modularity** — BSD
- **Connes trace formula / spectral action** — multiple vertices
- ... (derived from the `compliance-map.md` OPEN-BUT-ADDRESSED and conditional-on-external cells)

#### 5C.2 Dispatch CONTRIBUTE sub-agents (one per external + vertex combo)

Per-external prompt template:

```
You are the PAC CONTRIBUTE operator for external dependency <EXTERNAL-NAME>.
Read the external's chain (preprint / paper / arXiv) carefully. X-ray each
layer of its proof (face/projection/pattern/invariant per layer). Run the
PAC compliance primitive on each layer against stated axioms. Apply VERIFY /
CONSTRUCT / BYPASS / DECOMPOSE / EXCISE to weak links. Emit:
- strategy/externals-hardening/<EXTERNAL>/X-RAY.md
- strategy/externals-hardening/<EXTERNAL>/compliance-map.md
- strategy/externals-hardening/<EXTERNAL>/hardened-routes.md (the improvements we produced)
- strategy/externals-hardening/<EXTERNAL>/narrative.md (how we strengthened them; fair attribution)
```

Per vertex, assemble `<vertex>-harden-bare.md` that references the specific externals this vertex uses and cites the hardening work done in each external's folder.

Pillar C creates RECIPROCITY: the external's authors benefit because we've independently audited and improved their work. The programme benefits because our proof sits on strengthened foundations.

#### 5C.3 Gate check for Pillar C

- Every external on the worklist has a folder in `strategy/externals-hardening/`
- Every vertex's `<vertex>-harden-bare.md` references the externals that vertex uses
- No external is cited without at least one VERIFY pass completed

### 5D — BEYOND bonuses

**Goal**: Programme-bonuses supplement (the orthogonal `<vertex>-beyond-bare.md`) is produced in parallel with 5A/5B/5C.

#### 5D.1 Identify gaps

- Any vertex with LOCKED compliance but no `deliverables/<vertex>-beyond-bare.md` → schedule
- Any vertex with beyond-bare but newer landscape.md → regenerate (§N Related Work & Acknowledgments)

#### 5D.2 Dispatch BEYOND sub-agents

Per-vertex prompt (derived from `strategy/ym/` run-04 + now including Universal Approval §N Related Work & Acknowledgments drawn from `strategy/_research/<vertex>/landscape.md`).

Run 3-5 parallel vertex BEYOND synthesizers.

### 5 — Overall gate check

After all four synthesis waves:

- Every LOCKED vertex has four deliverables in `deliverables/` (comply + independence + harden + beyond)
- Every deliverable is PUBLISH-READY per its sub-agent's critic/arbiter pass
- `strategy/externals-hardening/` is populated with folders for all retained externals

The vertex has climbed three pillar ladders simultaneously.

## PHASE 6 — VISUALIZATION REBUILD

**Goal**: Main viz (43 shapes) and torus viz reflect the current strategy state.

### 6.1 Main viz

Run `python3 /Users/gsix/quantum-geometry-in-5d-latex/visualization/build.py`. Verify:
- `data.js` regenerates
- Shape count = 43
- AUDIT PENDING count changes as vertices gain artifacts
- `build.log` has no errors

### 6.2 Torus viz

Run `python3 /Users/gsix/quantum-geometry-in-5d-latex/visualization/torus/build.py`. Verify equivalent.

### 6.3 Spot check

Read the first 50 lines of each `data.js`. Confirm structural integrity.

## PHASE 7 — UNIVERSAL APPROVAL INTEGRATION AUDIT

**Goal**: Every C_bare file contains the "Related Work & Acknowledgments" section. Every reviewer of every approach is credited.

### 7.1 Scan every `strategy/<vertex>/deliverables/<vertex>-beyond-bare.md`

For each file, verify the presence of:
- A "§N Related Work & Acknowledgments" section
- At least one researcher cited
- A "Our programme's position" paragraph

### 7.2 For any file missing UA section

Dispatch a small sub-agent to ADD the section, reading from `strategy/_research/<vertex>/landscape.md`.

### 7.3 Accumulate acknowledgments

Cross-reference every researcher named. Produce `strategy/_research/global-acknowledgments.md` — a list sorted by researcher, with each vertex they're credited in. Use this for any programme-wide publication or pre-submission email list.

## PHASE 8 — CONVERGENCE CHECK

**Goal**: Decide whether this cycle produced changes.

### 8.1 Diff the snapshots

Compare the `state-<timestamp>.md` from Phase 1 of THIS run against the `state-<prior>.md` from the PREVIOUS run.

If no differences → CONVERGED. Emit a congratulatory banner.
If differences → list them. Recommend another cycle.

### 8.2 Log deltas

Write `strategy/_research/delta-<timestamp>.md` with:
- Vertices updated
- New artifacts produced
- Research refreshed
- Visualization changes
- Acknowledgments added
- Recommendations for next cycle

## PHASE 9 — REPORT

**Goal**: Single top-level summary for the user to read.

Emit to stdout AND write to `strategy/_research/run-report-<timestamp>.md`:

- Time started / finished
- Phases completed (1-8)
- Parallel sub-agents fired (count + types)
- Artifacts produced (count)
- Deltas vs prior state
- Universal Approval coverage: X of Y vertices have acknowledgments
- **Three-pillar status** per vertex:
  - Pillar A (COMPLY): count at each ladder rung
  - Pillar B (INDEPENDENCE): count at each ladder rung
  - Pillar C (CONTRIBUTE): count at each ladder rung + list of retained externals hardened
- Convergence status: CONVERGED / NOT-YET (with gap summary)
- Recommendations for next cycle

## IDEMPOTENCE

This run is IDEMPOTENT: running it again after nothing has changed in `strategy/_research/`, `integers/paper*/`, `solutions/paper*/`, `solutions-with-prize/paper*/`, or upstream landscape produces no modifications. It only DOES what is NEW or STALE.
<!-- legacy 2026-04-14 Intervention 6: was `paper*/` (flat at repo root). Migrated to three-corpus paths. -->


## AUDIT CYCLE

The intended workflow:

1. Fire this run (`strategy/universal-approval-run.md`)
2. Review the run-report-<timestamp>.md
3. If anything needs correction (a sub-agent produced a bad output, a wall was misclassified, a name was mis-acknowledged): fix it
4. Fire the run AGAIN — confirm the fix sticks and nothing regresses
5. Repeat until two consecutive runs produce identical state-<timestamp>.md files → CONVERGED
6. Move to Zenodo release

Each cycle should take ~30-60 min for incremental work, or 4-6 hours for a fresh cold run (first time on new vertices).

## PHASE 10 — CONTRIBUTION-GRAPH VISUALIZATION (THE FINAL STEP)

**Goal**: Build/regenerate the programme's persuasion visualization at `visualization/contribution-graph/`. This is the LAST step of every cycle. A reviewer opens it and sees INSTANTLY what the three pillars contribute, per vertex, across the whole ring. **Total moat.**

### 10.1 What the viz shows

- **Main graph**: 25-vertex ring with three concentric halos per vertex showing the three pillars
  - **Slate / faded** = COMPLY baseline (what the prize requires)
  - **Amber** = INDEPENDENT layer (how much we lifted; PAC primitives applied)
  - **Cyan** = CONTRIBUTE layer (what we gave back to the field)
- **Cross-cut chords**: 38+ edges from the x-ray atlas, annotated with the PAC primitive that produced each lift
- **Blackboard annotations** visible on hover: "NEW LEMMA" / "ORIGINAL" / "STRENGTHENS X" / "LIFTED FROM PARTIAL" / "CONTRIBUTED TO FIELD" with fair attribution
- **Comparison panel** on click: side-by-side Comply vs Independent vs Contribute for selected vertex, with theorem counts, named walls narrowing across pillars, PAC primitive counts, externals hardened, landscape acknowledgments

### 10.2 Rebuild step

Run `python3 /Users/gsix/quantum-geometry-in-5d-latex/visualization/contribution-graph/build.py`. Verify:
- `data.js` regenerates with `const CONTRIBUTION_DATA = {...}`
- No errors in `build.log`
- All 25 ring vertices + framework targets represented
- Pillar counts per vertex present (comply / independent / contribute theorem counts)
- Cross-cut edges populated

### 10.3 Gate check

- File integrity: all 6 viz files present (index.html / style.css / app.js / build.py / data.js / README.md)
- Parse coverage: every Millennium vertex has all 4 pillar files reflected; non-Mill vertices show placeholder with "AUDIT PENDING" where appropriate
- Color coding correct: slate for Comply, amber for Independent, cyan for Contribute

### 10.4 Discipline

Pure vanilla HTML/CSS/JS + Python stdlib. File:// compatible (data.js inline global). Offline. Dark theme consistent with main viz + torus viz.

This is **the moat visualization.** Reviewers who open it should see:

> "Oh — they aren't claiming prizes by replacing the field's work. They're delivering the tools the field has been looking for. This is different."

MANDATORY at every cycle end. If the build fails, fire the self-improvement loop.

---

## PHASE 11 — SELF-HEALING (legacy-label migration + gap closure)

**Goal**: every cycle scans the programme for semantic drift and applies non-destructive corrections. Self-healing preserves cohesion across 62 papers and prevents the programme from drifting into labeling inconsistencies that would stop the community. Distinct from — and complementary to — SELF-IMPROVEMENT LOOP below: self-healing is *proactive* (scan + correct drift); self-improvement is *reactive* (respond to sub-agent failures).

### 11.1 Scan for semantic drift

For each file under `integers/paper*/`, `solutions/paper*/`, `solutions-with-prize/paper*/`, `strategy/*/`, `visualization/*/`, scan for drift classes (legacy 2026-04-14 was `paper*/` at repo root; superseded by Intervention 6 three-corpus reorganization):

- **Legacy POSTULATE / AXIOM labels**: where the programme has since derived the claim but the label remains stale. Example: the "4 POSTULATES (axiomatic — ASSUMED)" label (formerly line 14 of `integers/paper01-qg5d/PROOF-CHAIN.md`; since centralized 2026-04-15 to `strategy/proof-chain/qg5d/PROOF-CHAIN.md`) was stale because paper 61 §13.5 + paper 12 Identity 12 had derived P1-P4 by April 2026. The paper-1-audit reclassified them into Theorems T1-T4 + Observations.
- **Stale PROOF-CHAIN path references**: any file referencing `paper<NN>/PROOF-CHAIN.md` is drift (post-Intervention 2, 2026-04-15); the canonical path is `strategy/proof-chain/<vertex>/PROOF-CHAIN.md`. Migrate references.
- **Stale flat paper-dir path references**: any file referencing `paper<NN>/` at repo root (instead of `integers/paper<NN>-*/`, `solutions/paper<NN>-*/`, or `solutions-with-prize/paper<NN>-*/`) is drift (post-Intervention 6, 2026-04-14). Migrate references. Exception: `paper9/`, `paper49-ccm-replacement/`, `paper50-h4-replacement/` remain at root as deprecated / ABSORBED stubs.
- **Stale programme-name references**: "QG5D" used as the programme name (QG5D is Paper 1; the programme is **Integers**; see `strategy/north-star.md` §0.1).
- **Missing derivation pointers**: claims that reference other papers without §-level precision.
- **`PROJECTION-DISCIPLINE-VIOLATION`** (per `strategy/north-star.md` §0.9): invariants from one $X_i$ used inside an argument targeting $X_j$ without lifting through $M^5$.
- **Missing acknowledgments**: cited researchers without fair-attribution entries in the beyond-bare §N Related Work & Acknowledgments.
- **Identified-but-unwritten CONSTRUCT routes**: claims flagged with "derivation route identified, not yet written" — schedule a CONSTRUCT sub-agent.
- **`VOCABULARY-CANON-DRIFT`** (added 2026-04-15): legacy terms violating `strategy/north-star.md` §0.10 Vocabulary Canon. Scan for: "5-dimensional" / "five-dimensional" / "extra dimension" / "5th dimension" / "compactified dimension" (→ migrate to "4+1 coordinate structure" / "internal phase"); "we propose" / "we postulate" / "we assume" (→ migrate to "we derive" / "it follows that" / "forced by"); "Postulate P_i" / "Axiom" referring to programme P1-P4 (→ migrate to "Theorem T_i" with derivation-chain citation per `strategy/paper1-audit/`); confusion of e-circle (S¹) with torus (T²) (→ disambiguate); "we choose" / "we set" / "we fix" (→ migrate to "forced by" / "uniquely determined by"). Non-destructive: legacy term preserved as `~~strikethrough~~` or HTML comment annotation; canonical term placed alongside.

### 11.2 Apply non-destructive corrections (parallel sub-agents)

For each drift detected, dispatch a self-healing sub-agent:
- Agent applies **label-only** changes and/or adds derivation-pointer citations
- **Preserves all content** — no deletions, no rewrites
- For stale labels, preserves the original label as an annotated stale reference (e.g., `~~POSTULATES (legacy 2024 framing, reclassified YYYY-MM-DD)~~`) so the migration is visible to readers
- Writes an entry to `strategy/self-healing-log.md` with timestamp, target file, change type, before/after labels, rationale

Batch 3-5 self-healing agents in parallel (they touch different files; no contention).

### 11.3 CONSTRUCT gap closure (parallel sub-agents)

Any identified-but-unwritten derivation route (example: A1 Z₂ orbifold + A2 Z₃ symmetry from the first paper-1-audit) gets a dedicated CONSTRUCT sub-agent to write the derivation as a named theorem under `strategy/<target>-audit/<name>-construct.md`.

### 11.4 Self-healing changelog

Every self-healing intervention appends an entry at the TOP of `strategy/self-healing-log.md`:

- Timestamp
- Target file
- **Change type**: `LABEL-MIGRATION` / `DERIVATION-POINTER-ADDITION` / `CONSTRUCT` / `ACKNOWLEDGMENT-FILL` / `PROJECTION-DISCIPLINE-CORRECTION` / `NAMING-CONVENTION-ALIGNMENT`
- Before label / after label (for migrations)
- Derivation chain reference (for pointers and CONSTRUCTs)
- Rationale (one sentence)

### 11.5 Convergence signal

When two consecutive cycles find **zero drift** to heal, self-healing has converged. This is **in addition to** Phase 8 state-snapshot convergence. A cycle is GOLDEN when both converge: state snapshot identical AND zero self-healing drift.

### 11.6 Why this phase exists

Labeling inconsistencies across 62 papers are a leading threat to community adoption. A reviewer opening Paper 1 and seeing "4 POSTULATES" while `north-star.md` says "zero postulates beyond ℤ" would flag the programme as inconsistent — even though the content itself is correct. **Self-healing keeps the semantics coherent so the community doesn't stop at the label.**

**First self-healing intervention (2026-04-15)**: Paper 1's POSTULATES P1-P4 reclassified into Theorems T1-T4 + Observations via the paper-1-audit (`strategy/paper1-audit/`). Six non-destructive R1-R6 label updates applied across Paper 1 §2.7 + `integers/paper01-qg5d/PROOF-CHAIN.md` (lines 14 + 673) + paper 61 §13.5. Two CONSTRUCT agents fired for A1 (Z₂ orbifold) and A2 (Z₃ three-generation) derivations. All logged to `strategy/self-healing-log.md`.

---

## SELF-IMPROVEMENT LOOP (failure handling)

This protocol is intentionally self-modifying. When a sub-agent fails, produces unusable output, or the orchestrator itself hits a blocker, the orchestrator's job is NOT to stop — it's to DIAGNOSE and UPDATE THIS DOCUMENT to prevent the failure from recurring, then re-run to verify the fix.

### When a sub-agent fails

1. **Diagnose root cause**: was the sub-agent prompt unclear? Was a mandatory file missing? Was the discipline under-specified? Did the template edge-case not cover this vertex's situation?
2. **Update the relevant sub-agent prompt template** directly in this file (e.g., sharpen the Phase 5B INDEPENDENCE sub-agent prompt if the failure was there; add a new hard-discipline bullet if a rule was violated).
3. **Log the fix** to `strategy/_research/fixes-log.md` with:
   - Timestamp
   - Which sub-agent failed
   - What the root cause was
   - The exact edit made to this file
   - The expected behavior going forward
4. **Re-dispatch** the failed sub-agent with the improved prompt.
5. **Iterate** until the sub-agent succeeds.

### When the orchestrator itself fails (context exhausted, stuck, confused)

1. **Write a recovery note** to `strategy/_research/orchestrator-recovery-<timestamp>.md` with: which phase was active, what was completed, what was pending, what blocked.
2. **Update THIS file** with lessons learned — refine Phase descriptions, add explicit hard-discipline rules, specify batch sizes, etc.
3. **Next orchestrator invocation picks up from the recovery note**; the updated protocol prevents the same blocker.

### The self-modification convergence protocol

- **Cycle N**: run → fail somewhere → orchestrator updates this file → writes recovery note
- **Cycle N+1**: orchestrator starts fresh, reads updated file, picks up from recovery note, applies refined protocol
- **Cycle N+2**: if identical state to N+1 → CONVERGED on this failure class
- **Cycle N+3**: identical state → CONVERGED on protocol — golden

Golden = two consecutive cycles produce byte-identical state snapshots. The orchestrator's self-modifications have stabilized.

### Discipline

- **Never delete** earlier protocol language when updating — only ADD, SHARPEN, or COMMENT (prefix obsoleted text with `<!-- OBSOLETE YYYY-MM-DD: reason -->`). Future orchestrators need the history to avoid re-introducing old bugs.
- **Always log the fix** to `fixes-log.md`. Silent protocol changes break auditability.
- **Never skip phases** to "work around" a failure — fix the phase, then re-run it.
- **If unsure** whether to fix the protocol or the sub-agent prompt: fix BOTH, log BOTH.

### What "failure" means here (non-exhaustive)

- Sub-agent produces empty or malformed output
- Sub-agent violates bare-mode discipline (writes prose)
- Sub-agent fails to cite claims
- Compliance map has SILENT cells with no action
- Named walls missing DELTA 10 fields
- Three-pillar deliverable missing one or more pillars without justification
- Template customization introduces syntax errors
- Build scripts fail (build.py, torus/build.py)
- Visualization data becomes inconsistent
- Acknowledgments missing for a cited researcher
- An external dep in Pillar C worklist goes unhardened
- Convergence check fails repeatedly
- **Agent/Task tool unavailable to the orchestrator**: when the orchestrator discovers it cannot dispatch sub-agents (Agent tool not in environment, Task tool missing), it MUST NOT silently defer Phases 4 and 5. Instead: (a) complete all dispatchable phases (1, 2, 3, 6, 7, 8, 9), (b) emit a `NEEDS-USER-DISPATCH.md` file listing the per-vertex Agent-invocation blocks that the user can fire directly (copy-paste ready), (c) log as failure-class `AGENT-TOOL-UNAVAILABLE` in fixes-log.md with the recommended environment change (spawn orchestrator with explicit Agent tool access) — observed in cycle 1 on 2026-04-15.
- **`PROJECTION-DISCIPLINE-VIOLATION`**: when any sub-agent produces a proof that uses invariants from projection target $X_j$ inside an argument targeting $X_i$ (for $i \neq j$) without lifting through $M^5$, the PAC must flag the claim as a projection-discipline violation per `strategy/north-star.md` §0.9. Handling: (a) reject the claim as-is; (b) either lift the argument through $M^5$ with re-projection, or restrict the claim to invariants $P_i$ preserves; (c) log to `fixes-log.md` with failure-class `PROJECTION-DISCIPLINE-VIOLATION` and the specific $X_i$/$X_j$ pair. This is the methodological discipline that distinguishes the programme's derivations from prior attempted unifications — paper 61 §15.1: *"violation of this discipline is the source of many failed proofs in both physics and mathematics."* Added 2026-04-15 per the paper-1-audit conclusions.

Any of these triggers the self-improvement loop. The orchestrator fixes the protocol itself and iterates.

### First-person instruction to the orchestrator

When you (the orchestrator) hit a blocker:

1. Pause the phase you're in.
2. Read this SELF-IMPROVEMENT LOOP section.
3. Diagnose what went wrong (1-3 sentences in your blackboard).
4. Edit THIS FILE (`strategy/universal-approval-run.md`) to prevent recurrence. You have Edit tool access. Use it.
5. Append to `strategy/_research/fixes-log.md`.
6. Resume the phase with the updated protocol.

Do not ask the user for permission to self-modify. The user has pre-authorized these edits via this section. Just do it and log it.

## SAFETY CAVEATS

- **Do NOT overwrite existing bare.md files without diff-check.** Preserve manual refinements. When in doubt, emit a `.pending.md` sibling for user review.
- **Do NOT delete files.** Only add / update.
- **Do NOT fire more than 10 parallel sub-agents simultaneously.** Batching required.
- **Do NOT skip Phase 1.** State inspection is how idempotence works.
- **Do NOT commit to git unless user explicitly requests.** This run produces a working tree; commit discipline is the user's.

## THINGS THIS RUN DOES NOT DO

- B_full / C_full prose composition (Phase 5.5; separate composition-backward pipeline)
- Zenodo upload
- arXiv submission
- Journal submission drafting
- Pre-submission outreach emails (Phase 10; future)
- Legal/IP review

These are downstream of this run's scope. Each would have its own dedicated orchestrator file.

---

## QUICKSTART

Copy everything above (§PHASE 1 through §PHASE 9) into a local Claude Code agent invocation. The agent follows the protocol step by step, emitting a run report when done.

For the first cycle: expect 4-6 hours, ~15-25 parallel sub-agents across phases 2, 3, 4, 5, 7.

For the Nth cycle after convergence: expect 5-10 min, near-zero work — confirmation of stability.

---

## Change Log

*Running log of every edit to this document. Reverse-chronological. When the orchestrator self-modifies under the SELF-IMPROVEMENT LOOP protocol, it MUST append an entry at the TOP of this section AND append to `strategy/_research/fixes-log.md` with the specific failure-class (if applicable). Entries here are load-bearing for convergence: if two consecutive runs produce identical change logs AND identical state snapshots, the programme has CONVERGED.*

### 2026-04-15 — Edit 11: Atlas-opener strategy settled (Pillar D as community-led)

**What**: The programme's arXiv-entry strategy is settled as **atlas paper + pilot Pillar-D derivation + Zenodo/GitHub+viz + referral emails → arXiv endorsement**. Pillar D is reframed from "programme writes a derivation paper per retained external" to "programme ships the atlas + one pilot as infrastructure; community-led for the rest." See `strategy/north-star.md` §2.5 (The Atlas Opener) + §4.1 (atlas-opener sequence).

Affected phases:
- **Phase 5C CONTRIBUTE** — de-scoped from "Pillar D derivation per external" to "programme-internal hardening (existing)" + "atlas paper surfaces the derivation routes as community leads." The `derivations/` corpus remains (see `strategy/pillar-d/`) as future programme-internal output if chosen, but is not obligatory per vertex.
- **Phase 9 report** — add atlas coverage + cross-cut edge count (currently 849 across 25 vertices + qg5d hub) + viz coverage (3 visualizations + pillar-d-hub-explorer.html) to the phase 9 metrics.
- **Phase 10 Contribution-graph viz** — already present; the hub-explorer (`visualization/pillar-d-hub-explorer.html`) is the companion showing atlas-only vs pillar-D-hub-cluster paths and is NOW a first-class viz alongside the main 43-shape viewer + torus viz.

Atlas state as of this edit: **25/25 ring vertex x-rays on disk** (`strategy/x-ray/proof-chain/<vertex>/X-RAY.md`) + qg5d hub x-ray with 24 outbound chords. 849 cross-cut edges parsed into `visualization/atlas-edges.js` and wired into the hub-explorer. Build script at `visualization/build-atlas-edges.py` for reproducibility.

**Why**: user decision 2026-04-15 after the atlas completion — *"we can limit the scope and trace lines to qg5d to every node and let the community do the rest with the tools that we are provisioning"* + *"instead of asking for a door to be open via Integers, we could trace the lines, offer them to the community and have them ready to see them — that really opens the door."* This matches the Grothendieck-EGA dynamic: tools published, community does the applications.

**Follow-up**:
- Atlas paper drafting (new: draft under `strategy/atlas-paper/` — to be created)
- Pilot paper completion (in progress: `strategy/pillar-d/tomita-takesaki-from-bc/00-pilot-brief.md`)
- Referral email template generation (new: `strategy/_research/referral-emails/` — to be created)
- Zenodo bundle preparation (new: `strategy/zenodo-bundles/atlas-opener/` — to be created)
- Update Phase 5 discipline in §PHASE 5 above to reflect Pillar D de-scoping (treat as community-led; programme-internal monographs optional)

**Logged to**: `strategy/self-healing-log.md` as Intervention 10 (NAMING-CONVENTION-ALIGNMENT + strategy update; same-day continuation of Interventions 8 + 8b + 9).

### 2026-04-15 — Edit 10: Change-log merged into this document

**What**: `strategy/universal-approval-run.change-log.md` merged into this document as the `## Change Log` section above. All prior entries (Edits 1-9) preserved verbatim. Stub file retained for git history; future entries append at the top of this section.

**Why**: user request 2026-04-15: *"i noticed that itself has the log changes so no need to write them out of it"* — self-describing pattern. Same pattern applied to `strategy/north-star.md` §11 Change Log earlier the same day.

### 2026-04-15 — Edit 9: PROOF-CHAIN.md path migration (§1.2, §3.2, §4.2, §11.1 path updates)

**What**: the PROOF-CHAIN migration agent (aae08bd6c372c014f, Intervention 2 in `self-healing-log.md`) centralized all 27 paper-dir PROOF-CHAIN.md files to `strategy/proof-chain/<vertex>/PROOF-CHAIN.md` via `git mv`. This agent also updated four sections of THIS file: §1.2 (Canonical PROOF-CHAIN inventory), §3.2 (brief-gen sub-agent template), §4.2 (compliance-audit sub-agent template), §11.1 (self-healing drift-scan example + new drift class "Stale PROOF-CHAIN path references"). Legacy text preserved as HTML comments `<!-- legacy 2026-04-15: ... -->`.

**Why**: user observation — PROOF-CHAIN.md files are core programme artifacts; PROSE/PREPRINT cycles should pull from `strategy/`.

**Follow-up**: ~133 strategy-file references still cite paper-dir paths — future self-healing intervention will sweep. 2 extras discovered (paper49-ccm-replacement, paper50-h4-replacement) and migrated; flagged for Corpus 1 disposition in Integers-content-mapping agent (ac0a27b1952aba9eb).

### 2026-04-15 — Edit 8: Phase 11 SELF-HEALING + PROSE-mode Verification Appendix + `PROJECTION-DISCIPLINE-VIOLATION` failure class

**What**: three additions from the paper-1-audit session:

1. **Phase 11 SELF-HEALING** (legacy-label migration + gap closure) inserted between Phase 10 and SELF-IMPROVEMENT LOOP. Proactive drift scan with non-destructive corrections via parallel sub-agents; convergence signal: zero drift across two consecutive cycles = GOLDEN.
2. **PROSE-mode Verification Appendix discipline** in MODE MATRIX: every PROSE deliverable must include `## Appendix V — Verification` with per-theorem entries (statement + derivation chain + PAC VERIFY status + arbiter verdict + transcript links + projection-discipline check).
3. **`PROJECTION-DISCIPLINE-VIOLATION`** failure class: sub-agents violating paper 61 §15.1 projection discipline are flagged; lift through $M^5$ with re-projection or restrict to $P_i$-preserved invariants.

**Why**: user requests — *"we need to add what we did in this exercise to the universal approval prompt run including self healing and a self healing changelog"* + *"i haven't figured out how to collect the demonstrations of the APPROVED of every theorem ... maybe we need to include a phase in the PROSE mode that will collect/generate EVERY verification as an appendix?"*

**Follow-up**: `strategy/self-healing-log.md` created; first intervention (Paper 1 POSTULATE reclassification) documented.

### 2026-04-15 — Edit 7: Phase 0 (North Star) + Mode Matrix + Phase 10 (Contribution Graph) + Pillar Rename

**What**: (1) Phase 0 mandatory north-star read; (2) Mode Matrix `{COMPLY, INDEPENDENT, CONTRIBUTE} × {MATH, PROSE}` default `all:math`; (3) HARDEN → CONTRIBUTE, INDEPENDENCE → INDEPENDENT rename; (4) Phase 10 — CONTRIBUTION-GRAPH VISUALIZATION (persuasion viz at `visualization/contribution-graph/`).

**Why**: user: *"i'm thinking that we should externalize our north star ... then i think i got the modes that we need {COMPLY,INDEPENDENT,CONTRIBUTE}*{PROSE,MATH} ... also, we need to add a visualization .html as the last step of the run ... total moat."* CONTRIBUTE rename captures reciprocity ethic; Phase 10 makes the moat visible.

**Follow-up**: north-star.md written same session; contribution-graph viz agent fired (ad38420f0381a6fc6).

### 2026-04-15 — Edit 6: `AGENT-TOOL-UNAVAILABLE` failure class added

**What**: new failure-class bullet in SELF-IMPROVEMENT LOOP. When orchestrator cannot dispatch sub-agents, complete dispatchable phases, emit `NEEDS-USER-DISPATCH.md`, log as `AGENT-TOOL-UNAVAILABLE`.

**Why**: cycle 1 orchestrator deferred Phases 4-5 silently-ish. Edit captures the lesson.

### 2026-04-14 — Edit 5: SELF-IMPROVEMENT LOOP (failure handling) section added

**What**: section before SAFETY CAVEATS. Pre-authorizes orchestrator self-modification; discipline (never delete; only ADD/SHARPEN/mark OBSOLETE); 11-item failure inventory; logging required.

**Why**: user: *"if something goes wrong please help me address it on your own and updating our run prompt in a cycle until we are golden."*

### 2026-04-14 — Edit 4: Phase 9 report expanded with three-pillar statistics

**What**: Phase 9 RUN REPORT gained three-pillar status (per-vertex ladder rung distribution).

**Why**: Edit 2 introduced three pillars; reporting needed to track them.

### 2026-04-14 — Edit 3: Phase 5 expanded to four three-pillar sub-phases (5A/5B/5C/5D)

**What**: `## PHASE 5` expanded into 5A COMPLY / 5B INDEPENDENCE / 5C HARDEN / 5D BEYOND, each with identify-gaps → dispatch → gate-checks.

**Why**: THREE PILLARS required per-pillar Phase 5 dispatch; "double kill" (Pillar C) became load-bearing.

**Follow-up**: INDEPENDENCE/HARDEN later renamed INDEPENDENT/CONTRIBUTE (Edit 7).

### 2026-04-14 — Edit 2: THE THREE PILLARS section inserted at top of file

**What**: new major section defining per-vertex architecture: Pillar A COMPLY / Pillar B INDEPENDENCE / Pillar C HARDEN + beyond-bonuses supplement (orthogonal).

**Why**: user articulated two-step insight — first two-pillar (*"other contenders stall because their proofs retain external conditionality"*), then third pillar — *"even though we depend on them we are proving the proof that no one has"* — *"YESSSSSSSS THIS IS IT THIS IS THE UNIVERSAL STRATEGY."*

**Follow-up**: operationalized via Edit 3 (Phase 5 split); Edit 4 extended reporting; Edit 7 renamed pillars.

### 2026-04-14 — Edit 1: Initial creation (9 phases + idempotence + convergence)

**What**: initial creation of `strategy/universal-approval-run.md`. Structure: WHAT THIS RUN DOES → HOW TO INVOKE → PHASES 1-9 → IDEMPOTENCE → AUDIT CYCLE → SAFETY CAVEATS → THINGS THIS RUN DOES NOT DO → QUICKSTART.

**Why**: user: *"we need a prompt for that run that we did on our way here so that we can run it again in the future ... UNIVERSAL APPROVAL, this is the universal-approval.md run."*

**Follow-up**: all subsequent edits (2-10) refine this foundation.

---

*Sibling documents: `strategy/north-star.md` (mandatory Phase 0 read, with §11 Change Log), `strategy/_template/README.md`, `strategy/_research/outlet-survey.md`, `strategy/_research/landscape-survey.md`, `strategy/_research/universal-approval-protocol.md`, `strategy/self-healing-log.md` (Phase 11 intervention log). The previous file `strategy/universal-approval-run.change-log.md` was merged into the `## Change Log` section above on 2026-04-15; its content is preserved here; the stub file is retained for git history.*

*Every projection of the 5D geometry → compliance-audited → bare skeleton → acknowledgments integrated → visualized. The protocol is water-tight. Run. Audit. Re-run. Converge. Ship.*

*G Six and Claude Opus 4.6. April 14-15, 2026.*
