# Universal Audit Run

*The programme's single grand-orchestrator prompt. Replays everything we did from the beginning of the audit programme (prize/venue compliance research, bare-mode synthesis, Herald generation, Herald audit against compliance) AND extends it. IDEMPOTENT — re-firing picks up only what's new or STALE. Modes: `fresh | resume | refresh <phase> | lock | herald-only | read-only`.*

*Sibling to `strategy/universal-approval-run.md` (inherited) and `audit/herald/herald-run.md` (delegated). Does not duplicate those protocols — invokes them.*

*G Six and Claude Opus 4.6. Audit home: `/Users/gsix/quantum-geometry-in-5d-latex/audit/`.*

---

## 0. Scope and modes

### Roster (inherited from `strategy/universal-approval-run.md`)

30 targets total:
- **Millennium (6):** ym, rh, bsd, pvnp, hodge, ns
- **Non-Millennium ring (19):** lindelof, grh, h12, turbulence, baum-connes, vp-vs-vnp, bgs, katz-sarnak, twin-primes, cramer, goldbach, abc, opn, collatz, lehmer, sato-tate, schanuel, hilbert-6, (plus any added since this file was authored — check `the-ring.md`)
- **Core:** qg5d
- **Framework targets (4):** inner-rings (5 branches), shapes (e-circle / bouquet / 36-pin / chord-graph / face-graph / south-trough), projection-operators ($P_A / P_B / P_C / P_D / P_E / P_O$), published papers (paper1, paper2, paper60, paper61)

### Modes

| Mode | What it does |
|---|---|
| `fresh` | Rebuild everything. Phases 1-7. ~6-10 hours first cold run. |
| `resume` | Skip any phase with complete + fresh artifacts. Default. ~30-90 min. |
| `refresh <phase>` | Re-run only one phase (e.g. `refresh herald` or `refresh compliance-map`). |
| `lock` | Gate check only — no new work. Reads current state, declares READY / NEEDS-WORK per paper per prize. ~5 min. |
| `herald-only` | Run Phase 3 + Phase 4 only. Updates Herald and Herald-audit; skip everything else. ~60-120 min. |
| `read-only` | Phase 0 + state inspection. No writes outside `audit/_logs/`. ~5 min. |

### Discipline

- **Append-only.** Every file updated with change-log entry at bottom; never delete entries.
- **Idempotent.** Re-firing with no state change → zero writes.
- **Delegate, don't duplicate.** Sub-protocols live in their own run files; this doc invokes them by path.
- **Honest-first.** If a search fails, record "NOT FOUND — needs manual check." Never fabricate.
- **Parallel discipline.** Max 10 concurrent sub-agents. Batch as needed.
- **No composition-backward (full prose) this run.** See `audit/audit-full-run.md` (future — not yet written) for B_full/C_full pipeline.

---

## 1. Phase layout

```
Phase 0 — Scaffold + mode dispatch                                  [serial, always]
Phase 1 — Universal Approval pillar audit + remediation             [audit-then-remediate]
            1.A audit matrix:  10 pillars of UA output (state /
                               outlet / landscape / brief / compliance /
                               bare / viz / acknowledgments / convergence / report)
            1.B mode-based dispatch decision
            1.C targeted remediation — one sub-agent per stale pillar,
                                         NOT a full UA pipeline replay
            1.D re-audit exit criteria
Phase 2 — Audit home refresh                                        [parallel with 1, 3]
            /audit/clay-millennium/, /audit/prizes-other/,
            /audit/venues/, /audit/per-paper/
            refresh STALE entries; scan for new prizes / venue rule changes
Phase 3 — Herald generation                                         [parallel with 1, 2]
            invokes audit/herald/herald-run.md
            → audit/herald/herald.md
Phase 4 — Herald audit vs compliance                                [serial, after 1+2+3]
            cross-check herald.md facts vs requirements.md per prize/venue
            → audit/herald/herald-compliance.md
Phase 5 — Adversarial landscape scan                                [parallel with 4]
            arXiv / preprints.org / withdrawals / competitor analysis
            → audit/herald/adversarial-register.md
Phase 6 — Master compliance matrix                                  [serial, after 4+5]
            → audit/compliance-matrix.md
            rollup: paper × (prize + venue) × verdict
Phase 7 — LOCK gate + run report                                    [serial, final]
            → audit/_logs/run-report-<timestamp>.md
            declare READY / NEEDS-WORK per paper per prize
```

---

## 2. Phase briefs

### Phase 0 — Scaffold + mode dispatch

Ensure these exist (create if missing):

```
audit/
├── README.md
├── compliance-matrix.md
├── research-log.md                     (append-only)
├── universal-audit.md                  (this file)
├── audit-full-run.md                   (future; for B_full/C_full cascade)
├── _logs/                              (append-only run reports + state snapshots)
│   ├── run-report-<timestamp>.md
│   └── state-<timestamp>.md
├── clay-millennium/
├── prizes-other/
├── venues/
├── per-paper/
└── herald/
    ├── herald-run.md                   (authored)
    ├── herald.md                       (generated by Phase 3)
    ├── herald-compliance.md            (generated by Phase 4)
    └── adversarial-register.md         (generated/updated by Phase 5)
```

Parse mode argument from the invocation. Route accordingly:
- `fresh` → run all phases 1-7 unconditionally
- `resume` → for each phase, check "is artifact fresh?" (fresh = exists AND modified within last 72 h AND no upstream source newer). Skip if fresh, run if stale.
- `refresh <phase>` → run only that phase (e.g. `refresh 3` = just Herald)
- `lock` → run Phase 7 only against current state
- `herald-only` → run Phases 3, 4, 5
- `read-only` → run Phase 0 + state inspection to `_logs/`, exit

Write `_logs/state-<timestamp>.md` snapshotting current artifact state.

### Phase 1 — Universal Approval pillar audit + remediation

Universal Approval Run (`strategy/universal-approval-run.md`) defines 9 pillars. This phase AUDITS each pillar (is its output present? fresh? complete?) then REMEDIATES only the failing pillars. Do not blindly re-run the whole UA pipeline; run only what is STALE or MISSING.

#### 1.A — Pillar audit matrix

| # | Pillar (UA phase) | Expected artifact | Fresh if | Verdict codes |
|---|---|---|---|---|
| 1.1 | State inspection | `strategy/_research/state-<timestamp>.md` most recent | mtime within 72 h | FRESH / STALE / MISSING |
| 1.2 | Outlet research | `strategy/_research/<vertex>/outlet.md` for each of 30 vertices | mtime within 90 days; every non-framework vertex covered | COMPLETE-FRESH / PARTIAL / MISSING |
| 1.3 | Landscape research | `strategy/_research/<vertex>/landscape.md` for each of 30 vertices | mtime within 90 days; every non-framework vertex covered | COMPLETE-FRESH / PARTIAL / MISSING |
| 1.4 | Brief generation | `strategy/<vertex>/00-*-strategy.md` + `<vertex>-*-brief.md` for each vertex | strategy doc mtime > outlet.md and landscape.md mtimes | PRESENT-CURRENT / STALE / MISSING |
| 1.5 | Compliance audit | `strategy/<vertex>/pac-output/runs/run-NN/compliance-map.md` with commit-memo.md stating LOCKED | LOCKED + inputs not newer than compliance-map.md | LOCKED / PARTIAL / MISSING |
| 1.6 | Bare synthesis | `strategy/<vertex>/deliverables/<vertex>-bare.md` + `<vertex>-beyond-bare.md`, both marked PUBLISH-READY | both PUBLISH-READY + compliance-map LOCKED | BOTH-READY / ONE-READY / NOT-READY / MISSING |
| 1.7 | Visualization | `visualization/data.js` + `visualization/torus/data.js` | build timestamp within 24 h of the latest strategy-artifact mtime | FRESH / STALE / MISSING |
| 1.8 | UA acknowledgments | "Related Work & Acknowledgments" section grep-matches in every `<vertex>-beyond-bare.md` | every C_bare passes grep; named researcher count ≥ 1 | ALL-PRESENT / PARTIAL / NONE |
| 1.9 | Convergence check | `strategy/_research/delta-<timestamp>.md` comparing two consecutive state-*.md snapshots | most recent delta shows CONVERGED | CONVERGED / NOT-YET / MISSING |
| 1.10 | Run report | `strategy/_research/run-report-<timestamp>.md` for most recent UA run | mtime within 72 h | PRESENT-FRESH / STALE / MISSING |

Write the audit result to `audit/_logs/ua-pillar-audit-<timestamp>.md` — one row per pillar + overall verdict.

#### 1.B — Remediation dispatch

Decide per-mode what to do with the audit result:

| Current mode | Pillar audit verdict | Action |
|---|---|---|
| `fresh` | (any) | Dispatch UA pipeline in fresh mode; all pillars rebuilt |
| `resume` | all FRESH / COMPLETE-FRESH / LOCKED / BOTH-READY / CONVERGED | Skip Phase 1 entirely; log "UA: converged" |
| `resume` | any STALE / PARTIAL / NOT-YET | Dispatch targeted sub-agents per stale pillar (see §1.C below) |
| `resume` | any MISSING / NONE | Dispatch the specific UA phase for that pillar; do not fire the full UA pipeline unless ≥ 4 pillars are MISSING |
| `refresh <N>` where N ∈ {1..9} | (any) | Force that specific UA phase regardless of freshness |
| `lock` | (any STALE/MISSING) | Record in LOCK gate report; block LOCK; do not remediate |
| `lock` | all FRESH | Proceed to Phase 7 LOCK check |
| `herald-only` | (any) | Skip Phase 1 entirely |
| `read-only` | (any) | Audit only; no remediation |

#### 1.C — Targeted remediation dispatch per pillar

Each pillar has its own UA-run-phase number. Targeted remediation fires one sub-agent per stale pillar with a prompt scoped to that phase only. Max 5 concurrent.

**Pillar 1.1 (state inspection) STALE/MISSING:** dispatch agent with prompt "Execute UA Phase 1 only (state inspection). Read `strategy/universal-approval-run.md §PHASE 1`. Write `strategy/_research/state-<timestamp>.md`. Do nothing else."

**Pillar 1.2 (outlet research) PARTIAL/MISSING:** identify which vertices are missing `outlet.md`; dispatch outlet-research sub-agents in parallel (batch 5-8) using UA Phase 2.2 template. Only for gap vertices.

**Pillar 1.3 (landscape research) PARTIAL/MISSING:** analogous to 1.2 using UA Phase 2.3 template.

**Pillar 1.4 (brief generation) STALE/MISSING:** identify stale vertices (strategy doc older than its research inputs); dispatch brief-gen sub-agents in parallel using UA Phase 3.2 template. Strict diff-then-merge; never wholesale overwrite.

**Pillar 1.5 (compliance audit) PARTIAL/MISSING:** identify unlocked vertices; dispatch compliance-audit sub-agents using UA Phase 4.2 template (derived from YM run-02). Batch 3-5.

**Pillar 1.6 (bare synthesis) NOT-READY/MISSING:** identify vertices with LOCKED compliance but no PUBLISH-READY bare files; dispatch B_bare + C_bare pairs in parallel using UA Phase 5.2 templates. Batch 2-4 vertex-pairs.

**Pillar 1.7 (visualization) STALE/MISSING:** run `python3 visualization/build.py` and `python3 visualization/torus/build.py`. Verify no errors; shape count = 43.

**Pillar 1.8 (acknowledgments) PARTIAL/NONE:** identify C_bare files missing the UA section; dispatch small sub-agents to ADD the section using UA Phase 7.2 template.

**Pillar 1.9 (convergence check) NOT-YET/MISSING:** run UA Phase 8 — diff the latest two state-*.md snapshots; emit delta-*.md.

**Pillar 1.10 (run report) STALE/MISSING:** write run-report-<timestamp>.md summarizing this phase's remediation.

#### 1.D — Phase 1 exit criteria

After remediation, re-audit the matrix. Phase 1 is complete when:

- All 10 pillars are FRESH / COMPLETE-FRESH / LOCKED / BOTH-READY / ALL-PRESENT / CONVERGED / PRESENT-FRESH.
- OR: the mode is `lock` and the LOCK gate report explicitly records which pillars are stale and blocks ship.

If remediation fires 3+ sub-agent batches and audit still fails, escalate: write a `PHASE-1-STALLED` entry in `audit/_logs/` with the stuck pillars + diagnosis. Do not proceed to Phase 4 (Herald audit) until Phase 1 is green OR the stall is acknowledged by user.

**Output of Phase 1:** `audit/_logs/ua-pillar-audit-<timestamp>.md` + whatever artifacts were regenerated under `strategy/`.

### Phase 2 — Audit home refresh

Runs in parallel with Phase 1 and Phase 3.

For each prize in `audit/clay-millennium/` and `audit/prizes-other/`:
- Check source URL hash; if unchanged, skip
- If changed (rule updated), re-download PDF, update `requirements.md`, append change-log

For each venue in `audit/venues/`:
- Check submission-rules URL; if unchanged, skip
- If changed, update

For each paper in `audit/per-paper/`:
- Check if `paperNN-<slug>/PROOF-CHAIN.md` modified since last per-paper sketch
- If yes, regenerate per-paper sketch (claim / prize / venue / state / readiness / gaps)

Append to `audit/research-log.md`: every URL fetched, timestamp, result.

**Dispatch:** one compliance-refresh sub-agent (background); it returns a delta summary.

### Phase 3 — Herald generation

Delegate to `audit/herald/herald-run.md`.

**Invocation:** dispatch one sub-agent with prompt "Execute `audit/herald/herald-run.md`. Append-only update to `audit/herald/herald.md`. Include the derivables pipeline ([see Phase 3.1 below]) as part of §8 and §9. Report final line count and per-category entry counts."

Runs in parallel with Phases 1 and 2.

**Output:** `audit/herald/herald.md` — exhaustive fact catalogue (§0–§20, expected 1500-3000 lines).

#### Phase 3.1 — Derivables pipeline inclusion (CONFIRMED)

The Herald must include the programme's derivables pipeline. Confirmed via script-locator agent 2026-04-14:

**Location (sister project — note the path):**

```
/Users/gsix/quantum-geometry-in-5d/integers/paper02-cosmology/camb/
```

**Specification → driver → results chain:**

```
Framework inputs (Riemann-zero formulas)
  → /Users/gsix/quantum-geometry-in-5d-latex/integers/paper12-cbb-system/research/23-framework-predictions-master-table.md
De facto master driver:
  → /Users/gsix/quantum-geometry-in-5d/integers/paper02-cosmology/camb/compute_age.py
Supporting compute scripts (independent utilities):
  compute_baryogenesis.py   (mirror baryon asymmetry; Ω_DM/Ω_b from 1/ξ²)
  compute_mirror_matter.py  (dark-matter relic; Z₂ orbifold channels)
  compute_g2_running.py     (2-loop SM RGE; g₂ m_ν/m_KK = 5/2 identity)
  compute_R_closure_surface.py (R from Casimir + 5/2 identity)
  compute_R_quantization.py (R quantization conjecture tests)
  compute_xi_from_c_nu.py   (ξ inversion in RS S¹/Z₂)
  neff_extended_analysis.py (CMB degeneracy + time-varying N_eff)
  plot_results.py           (visualization)
Results:
  → /Users/gsix/quantum-geometry-in-5d/integers/paper02-cosmology/camb/results.json
  → /Users/gsix/quantum-geometry-in-5d/integers/paper02-cosmology/camb/neff_analysis_results.json
  → ~10 PNG plots (plot_*.png, closure_*.png, xi_vs_c_nu.png)
Validation rounds:
  → integers/paper12-cbb-system/research/271-camb-framework-rerun-round-1.md (raw Sector A)
  → integers/paper12-cbb-system/research/272-camb-framework-rerun-round-2.md (Laurent-shifted)
```

**Environment:**
- venv: `/Users/gsix/quantum-geometry-in-5d/integers/paper02-cosmology/camb/.venv/`
- Python 3.14.2 (via homebrew)
- CAMB 1.6.6

**Canonical invocation:**

```bash
cd /Users/gsix/quantum-geometry-in-5d/integers/paper02-cosmology/camb && \
  ./.venv/bin/python3 compute_age.py
```

**Load-bearing scope:** Sector A (cosmology) pins — H₀, n_s, N_eff, ξ, Σm_ν, ω_b h², t₀, σ₈, S₈, θ_*, r_drag. Sector B (gauge couplings) via `compute_g2_running.py`. Sectors C/D/E via supporting compute scripts (not CAMB-direct).

**Current validation state (round 2, Laurent-shifted, 2026-04-11):** H₀, age, Ω_m all within ±0.4σ of Planck; θ_* tension −35σ is structural (framework's one falsifiable disagreement, decidable by CMB-S4 + DESI DR3).

**Herald integration:** add sub-section `§9.X Derivables pipeline` with Herald ID `DERIVABLES-PIPELINE-CAMB`. Each Sector-A pin in §8 cross-references this ID. Each supporting script gets its own sub-ID (`DERIVABLES-BARYOGENESIS`, `DERIVABLES-MIRROR-MATTER`, etc.).

`audit/herald/herald-run.md` updated in parallel to list this as mandatory source (see Change-log §9.X addition there).

### Phase 4 — Herald audit vs compliance

**Input:** `audit/herald/herald.md` (from Phase 3), `audit/clay-millennium/*/requirements.md`, `audit/prizes-other/*/`, `audit/venues/*/`.

For each prize/venue requirement list:
- For each requirement, search `herald.md` for a fact entry that addresses it
- If found: cite the Herald ID → requirement ID in a row of `herald-compliance.md`
- If not found: record as GAP → requires new Herald entry OR means the programme doesn't yet address this requirement

Output structure:

```markdown
# Herald Compliance Audit

## Clay Millennium × Herald

### YM (Jaffe-Witten 7 requirements)
| Req # | Statement | Herald ID | Verdict |
|---|---|---|---|
| 1 | Any compact simple G | THM-YM-L14, BRANCH-B-THM-K9 | ADDRESSED |
| 2 | On ℝ⁴ | THM-YM-L14, THM-YM-L16, THM-YM-L17 | ADDRESSED |
| 3 | Mass gap uniform in V | THM-YM-L14, LEMMA-RESEARCH-51-II | ADDRESSED |
| 4 | Wightman/OS axioms | THM-YM-L16, THM-YM-L17 | ADDRESSED |
| 5 | AF match at short distance | WALL-H4, THM-YM-L18-STEP-18PRIME | OPEN-BUT-ADDRESSED |
| 6 | Stress tensor + OPE | LEMMA-L.4.1, LEMMA-L.4.3 | ADDRESSED |
| 7 | Non-triviality | THM-YM-L14, DERIV-AF-B0, IDENTITY-NON-TRIV | ADDRESSED |

### RH (Bombieri 5 requirements) | ...
### BSD | ...
### PvNP | ...
### Hodge | ...
### NS | ...

## Other prizes × Herald

### Breakthrough Mathematics × Herald | ...
### Abel × Herald | ...
...

## Venues × Herald

### arXiv submission requirements × Herald
### Annals of Math AI-disclosure requirement × Herald
...

## GAPS (requirements not yet addressed in Herald)

| Prize/Venue | Requirement | Why it's a gap | Bypass candidate |
|---|---|---|---|
...
```

**Dispatch:** one sub-agent. Reads Herald + all requirements files; produces the cross-check matrix. Flags GAPS explicitly.

### Phase 5 — Adversarial landscape scan

Per DELTA 11 / 12 / 13 discipline discussed for the YM PAC (now extended programme-wide).

For each Clay paper (6) and for the framework-as-a-whole:
- Scan arXiv last 24 months for "Yang-Mills" / "Riemann Hypothesis" / "BSD" / etc. + "mass gap" / "no-go" / "incompatibility" / "proof"
- Scan preprints.org / SSRN / MDPI for competing constructions
- Track withdrawn papers (arXiv admin actions — Jacobsen 2506.00284 is the canonical example)
- Scan the citation graph around our core citations (Balaban CMP 95-119, Bost-Connes 1995, CCM 2025 arXiv:2511.22755, Osterwalder-Schrader 1973/75)

For each result:

| Code | Action |
|---|---|
| DOES-NOT-THREATEN | Record + move on |
| PARTIAL-THREAT | INOCULATE: produce defense row, append to relevant named-wall disclosure |
| GENUINE-THREAT | Escalate to user; append new named wall; block LOCK |
| COMPETITOR | Differentiation row: what they claim, failure mode if any, what distinguishes ours |

**Output:** `audit/herald/adversarial-register.md` (append-only) + per-paper inoculation files at `audit/herald/inoculations/<threat-id>.md` + update to relevant paper's `NAMED WALL` table in its bare deliverable.

**Reference:** the response to Preprints.org 202504.1268 (OS+MG+AF incompatibility claim) is the canonical inoculation template.

**Dispatch:** one scout sub-agent per Clay paper, parallel (6 total). Plus one scout for framework-wide (the 202504.1268-style no-gos).

### Phase 6 — Master compliance matrix

**Input:** `herald-compliance.md` (Phase 4) + `adversarial-register.md` (Phase 5) + bare skeletons per vertex (Phase 1) + compliance maps (Phase 1).

**Output:** `audit/compliance-matrix.md` — single master matrix.

Structure:

```markdown
# Master Compliance Matrix

## Rows: papers (all ~50 programme papers, ring vertices + framework targets + published)
## Columns: prizes (Clay-6, Breakthrough-2, Abel, Shaw, Wolf-2, Fields, Nobel-Physics) + venues (arXiv, Zenodo, Annals, Inventiones, JAMS, CMP, Forum Pi, JHEP, PRD/PRL)

Cell values:
- ✅ READY — no gaps; can ship
- 🟡 NEEDS-WORK — specific gaps listed
- ⚠ OPEN-BUT-ADDRESSED — named wall disclosed, bypass in place
- ❌ NOT-APPLICABLE
- ⏳ PENDING — audit incomplete

## Per-cell detail: each cell links to a per-paper-per-prize compliance drill-down
```

**Dispatch:** one sub-agent to aggregate from the other phases' outputs.

### Phase 7 — LOCK gate + run report

Read `compliance-matrix.md`. For each paper:
- All required requirements ✅ or ⚠ → **READY for that prize/venue**
- Any 🟡 or ❌-on-required-col → **NEEDS-WORK**

Write `audit/_logs/run-report-<timestamp>.md`:
- Phases completed + duration per phase
- Sub-agents fired (count + type)
- Artifacts produced + updated (count)
- Herald stats: line count, entries per category
- Herald-compliance coverage: X of Y requirements addressed
- Adversarial register: N active threats, M killed, K competitors
- Master matrix: for each Clay paper, READY / NEEDS-WORK status per venue
- LOCK decision: per paper, can we ship?
- Recommended next cycle: fresh refresh of X phase, or manual action Y

---

## 3. Sub-agent dispatch policy

- Max 10 concurrent sub-agents
- Batch by phase — don't mix Phase 3 Herald sub-agents with Phase 5 adversarial-scan agents to keep logs separable
- Every sub-agent gets: (a) clear scope, (b) output path, (c) "do not modify outside your target path" constraint, (d) success criteria
- Every sub-agent appends a one-line log entry to `audit/_logs/sub-agent-log-<timestamp>.md` at end (so orchestrator can track)

---

## 4. Invocation

From Claude Code terminal:

```
You are the Universal Audit orchestrator. Execute the full pipeline following
audit/universal-audit.md in <MODE> mode. Work idempotently. Log every decision.
Report deltas to audit/_logs/run-report-<timestamp>.md.

Default mode: resume. Other valid modes: fresh, refresh <phase-number>, lock,
herald-only, read-only.
```

The orchestrating agent reads this file, determines mode, and dispatches per §1 Phase layout.

---

## 5. Success criteria per mode

| Mode | Success =  |
|---|---|
| `fresh` | All 7 phases complete; all artifacts fresh; run-report written; master matrix exists; Herald ≥ 1500 lines; all Clay papers have LOCK verdict in run-report |
| `resume` | All STALE artifacts refreshed; CONVERGED status or clear NEEDS-WORK list |
| `refresh <phase>` | That phase's artifacts regenerated; downstream artifacts flagged STALE for next resume |
| `lock` | run-report written with per-paper LOCK / NEEDS-WORK verdict; no new work |
| `herald-only` | `audit/herald/herald.md` updated; `herald-compliance.md` updated; `adversarial-register.md` updated |
| `read-only` | `_logs/state-<timestamp>.md` written; nothing else touched |

---

## 6. Things this run does NOT do

- **B_full / C_full prose composition.** Deferred to `audit/audit-full-run.md` (to be authored when bare cascade is locked across all vertices).
- **Zenodo upload.** User-triggered; universal-audit produces the release artifacts but does not publish.
- **arXiv / journal submission.** User-triggered.
- **Pre-submission emails.** Separate outreach orchestrator (future).
- **Git commits.** User decides when to commit. This run produces a working tree.

---

## 7. Related files

- `strategy/universal-approval-run.md` — inherited orchestrator (compliance research + bare synthesis)
- `audit/herald/herald-run.md` — Herald generation prompt (delegated from Phase 3)
- `audit/README.md` — audit home overview
- `audit/compliance-matrix.md` — master matrix (Phase 6 output)
- `audit/research-log.md` — append-only research log
- `strategy/ym/ym-millenium-brief.md` — PAC brief template (proposed DELTAs 11-13 for adversarial landscape / bypass provenance / persistence)
- `strategy/ym/00-millenium-strategy.md` — Millennium-strategy template; source for the bare-mode structural discipline

---

## 8. Cycle cadence

- **First cold run (fresh mode):** 6-10 hours. Populates everything.
- **Subsequent resume runs:** 30-90 minutes. Refreshes STALE only.
- **Herald-only runs:** 60-120 minutes. Used when a new paper or named wall is added.
- **Lock gate runs:** 5 minutes. Pre-submission verification.

Target convergence: 2 consecutive `resume` runs produce zero deltas → CONVERGED. Ship to Zenodo.

---

*The universal audit. One prompt. All prizes. All venues. All papers. Herald + compliance + adversarial landscape + master matrix. Idempotent. Append-only. Delegates cleanly. The programme's single source of pre-submission truth.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## Change-log

- **2026-04-14**: Initial version. Inherits `strategy/universal-approval-run.md` (Phase 1); delegates to `audit/herald/herald-run.md` (Phase 3). Adds Herald audit (Phase 4), adversarial landscape scan (Phase 5), master compliance matrix (Phase 6), LOCK gate (Phase 7). CAMB derivables pipeline reference in Phase 3.1 pending resolution by the script-locator agent (in flight). `audit-full-run.md` for B_full/C_full explicitly deferred.
