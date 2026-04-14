# Universal Approval Run

*A single self-contained agent prompt that executes the full Universal Approval pipeline end-to-end. IDEMPOTENT — re-firing picks up only what's new or updated since last run. Designed for cycle-based convergence: run → audit → run → audit → ... until the programme stabilizes.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## WHAT THIS RUN DOES

This single prompt replays (and extends) the work-flow executed 2026-04-13 → 2026-04-14 that produced the programme's Zenodo-priority deliverables:

1. Inspects the `strategy/`, `visualization/`, and `paper*` directories to establish current state
2. Scans the web for prizes, outlets, journal targets, and competitor-landscape per vertex (Universal Approval research)
3. Generates or updates PAC strategy documents and briefs per vertex, parameterized from `strategy/_template/`
4. Dispatches compliance audits per vertex (Phase A of the 3-run cadence)
5. Dispatches bare-synthesis runs per vertex (B_bare + C_bare in parallel; Phase B)
6. Rebuilds both visualizations (main 43-shape viewer + torus viz)
7. Integrates Universal Approval acknowledgments into all C_bare files
8. Diffs the state, logs deltas, emits recommendations for the next cycle

## HOW TO INVOKE

```
You are the Universal Approval orchestrator. Execute the full pipeline at
/Users/gsix/quantum-geometry-in-5d-latex following the protocol below.
Work idempotently — do not redo work that is already current.
Log every decision and delta.

Read strategy/universal-approval-run.md for the full protocol and execute it.
```

Pass this to a local Claude Code agent (or fire as a sub-agent via the Agent tool).

## PHASE 1 — STATE INSPECTION

**Goal**: Establish what exists NOW. No modifications. Output: `strategy/_research/state-<timestamp>.md`.

Inspect and record:

### 1.1 Strategy directory inventory

For each directory under `strategy/`, list:
- Presence of `00-*-strategy.md` (millennium-strategy or audit-strategy)
- Presence of `<vertex>-*-brief.md`
- Presence of `pac-output/runs/run-NN/` and whether commit-memo.md says LOCKED
- Presence of `deliverables/<vertex>-bare.md` and `<vertex>-beyond-bare.md`

### 1.2 Paper directory inventory

For each `paper*/PROOF-CHAIN.md`, record:
- Line count
- Last modification date
- Status tags (PROVED / CONDITIONAL / PARTIAL / OPEN)
- Named walls mentioned

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
live paper<NN>-<vertex>/PROOF-CHAIN.md (if exists). Generate or UPDATE
strategy/<VERTEX>/00-audit-strategy.md and strategy/<VERTEX>/<VERTEX>-audit-brief.md
following the template verbatim — customize only the six parameters
(SHAPE_NAME, PAPER_REFERENCE, SOURCE_OF_REQUIREMENTS, N-REQUIREMENTS-LIST,
NAMED-WALLS, SPECIAL-PROVISIONS). Preserve any existing content that remains
valid (diff-then-merge, do NOT wholesale overwrite).
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
00-*-strategy.md and <VERTEX>-*-brief.md. Read paper<NN>-<vertex>/PROOF-CHAIN.md
and strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md (if exists). Build M×N
compliance map per DELTA 4 format. Address all SILENT verdicts. Write to
strategy/<VERTEX>/pac-output/runs/run-NN/ with lock status in commit-memo.md.
Do NOT produce B_bare or C_bare this run.
```

Run 3-5 parallel compliance audits. Pause before proceeding to Phase 5 — let the user review lock verdicts.

## PHASE 5 — BARE SYNTHESIS DISPATCH (parallel)

**Goal**: Every vertex with LOCKED compliance has B_bare + C_bare in PUBLISH-READY state.

### 5.1 Identify gaps

- Any vertex with LOCKED compliance but no `deliverables/<vertex>-bare.md` → schedule B_bare
- Any vertex with LOCKED compliance but no `deliverables/<vertex>-beyond-bare.md` → schedule C_bare
- Any vertex with bare files but newer landscape data → regenerate to pick up acknowledgments

### 5.2 Dispatch bare-synthesis sub-agents (2 per vertex, run in parallel)

Per-vertex B_bare prompt: derived from `strategy/ym/` run-03 prompt
Per-vertex C_bare prompt: derived from `strategy/ym/` run-04 prompt

Fire B_bare and C_bare sub-agents in parallel per vertex. Run 2-4 vertex-pairs simultaneously (that's 4-8 sub-agents). Each sub-agent includes the Universal Approval acknowledgments in its output structure.

### 5.3 Gate check

After synthesis, verify every LOCKED vertex now has both bare files with "PUBLISH-READY" verdict.

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
- Convergence status: CONVERGED / NOT-YET (with gap summary)
- Recommendations for next cycle

## IDEMPOTENCE

This run is IDEMPOTENT: running it again after nothing has changed in `strategy/_research/`, `paper*/`, or upstream landscape produces no modifications. It only DOES what is NEW or STALE.

## AUDIT CYCLE

The intended workflow:

1. Fire this run (`strategy/universal-approval-run.md`)
2. Review the run-report-<timestamp>.md
3. If anything needs correction (a sub-agent produced a bad output, a wall was misclassified, a name was mis-acknowledged): fix it
4. Fire the run AGAIN — confirm the fix sticks and nothing regresses
5. Repeat until two consecutive runs produce identical state-<timestamp>.md files → CONVERGED
6. Move to Zenodo release

Each cycle should take ~30-60 min for incremental work, or 4-6 hours for a fresh cold run (first time on new vertices).

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

*Sibling to: `strategy/_template/README.md`, `strategy/_research/outlet-survey.md`, `strategy/_research/landscape-survey.md` (once landscape agent completes), `strategy/_research/universal-approval-protocol.md` (once landscape agent completes).*

*Every projection of the 5D geometry → compliance-audited → bare skeleton → acknowledgments integrated → visualized. The protocol is water-tight. Run. Audit. Re-run. Converge. Ship.*

*G Six and Claude Opus 4.6. April 14, 2026.*
