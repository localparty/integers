# Independent Audit Run

*The dual of `strategy/universal-approval-run.md`. Generates its own referee resources from primary sources, builds a Canonical Ruleset dynamically from the union of prize rules and programme discipline, audits every deliverable point-by-point across four reading modes, and publishes reciprocity hardening preprints for every retained external dependency. IDEMPOTENT, SELF-HEALING, and designed to co-evolve with the Universal Approval Run until byte-identical convergence.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## WHAT THIS RUN DOES

Where `universal-approval-run.md` *synthesizes* deliverables meeting prize requirements, this run *audits* those deliverables against independently-extracted rules. Specifically:

1. Harvests primary-source prize documents (Clay problem statements, Bakuage Collatz terms of reference, historical Hilbert sources) into its own resources dir, independent of UA's `_research/` outputs
2. Generates a **Canonical Ruleset** dynamically: union of prize-extracted rules + programme-discipline rules distilled from paper1, paper08 math-referee, UA bare-mode discipline, and every other self-referential standard the programme already holds itself to
3. Audits the **dependency-closure** of UA's deliverables — every programme paper that appears as a dependency of any UA pillar gets tested against the Canonical Ruleset BEFORE downstream vertices are touched. Leaves first, topological order
4. Runs **point-by-point compliance audits** per pillar (A Comply / B Independence / C Harden) per vertex — zero collapsing, max-effort per point, verdicts tied to both a rule ID and a location in the deliverable
5. Hardens every retained external dep with PAC primitives (VERIFY / CONSTRUCT / EXCISE / BYPASS / DECOMPOSE / TRANSPOSE) and drafts publishable reciprocity preprints honoring the original authors
6. Assembles a **quadruple-mode judge dossier** per vertex: compliance checklist + adversarial referee report + narrative proof walkthrough + interactive HTML dashboard
7. Emits a global `AUDIT-REPORT.md` and a global interactive `audit-visualization.html` rolling up the programme
8. **Self-improves**: every failure pattern encountered feeds back into the Canonical Ruleset; cycle N+1 is stricter than cycle N
9. **Co-evolves with UA**: when audit finds a gap, UA resynthesizes; when UA ships new deliverables, audit re-tests. Convergence = two consecutive cycles produce byte-identical state AND every verdict is PASS or CLOSABLE

## THE UNIVERSAL MOAT — FOUR READING MODES

Every vertex ships `judge-dossier.md` + `audit-dashboard.html` together containing four modes of reading the same audit:

### MODE 1 — Compliance Checklist (tabular)

Every rule ID from the Canonical Ruleset → verdict (PASS / PARTIAL / FAIL / CLOSABLE / GENUINE) + citation + deliverable location + PAC action if failing. Machine-readable, scannable, definitive.

### MODE 2 — Adversarial Referee Report (prose)

Hostile-skeptical read of the deliverable. Every attack attempted, every attack's resolution documented. Failures surfaced honestly. No marketing language. Modeled on `solutions-with-prize/paper08-yang-mills/math-referee/02-point-by-point-yang-mills.md`.

### MODE 3 — Narrative Proof Walkthrough

Hand-holding tour from axiom through every intermediate claim to the final theorem, with every step cross-referenced to a checklist ID so the reader can verify as they go. This is the mode a graduate student uses.

### MODE 4 — Interactive Dashboard (HTML)

Per-vertex HTML visualization: pie/histogram of verdicts per pillar, heatmap of rules × pillars, externals dependency graph with hardening arrows, timeline of verification events, click-through from any cell to the verdict + deliverable location. Colors: PASS=green, PARTIAL=yellow, CLOSABLE=orange, FAIL=red, GENUINE=purple.

**Why four modes**: judges read differently. Some want hostile skepticism, some want tabular compliance, some want narrative, some want visual exploration. Delivering all four from the same audit means *whatever lens the judge picks up, the answer is already there*. No contender does this. This is the Universal Moat.

## THE DEPENDENCY-CLOSURE DISCIPLINE

We do not audit QG5D in isolation. We audit every programme paper that appears as a dependency of any UA pillar deliverable.

Concretely: Phase 1 walks every `<vertex>-comply-bare.md`, `<vertex>-independence-bare.md`, `<vertex>-harden-bare.md`, and `<vertex>-beyond-bare.md` under `strategy/*/deliverables/`, extracts every `paperNN-` and every cross-programme citation, builds a directed dependency graph, and topologically sorts it. Leaves (papers depending on nothing programme-internal — at minimum paper1) are audited first. Each paper's audit-gate must reach PASS or CLOSABLE before anything that depends on it is audited.

This prevents the failure mode where a downstream vertex appears to pass only because its foundation wasn't checked.

## HOW TO INVOKE

```
You are the Independent Audit orchestrator. Execute the full pipeline at
/Users/gsix/quantum-geometry-in-5d-latex following the protocol below.
Work idempotently — do not redo work that is already current. Self-heal
missing resources. Log every decision and delta.

Read strategy/independent-audit-run.md for the full protocol and execute it.
```

Pass this to a local Claude Code agent (or fire as a sub-agent via the Agent tool).

## PHASE 0 — RESOURCE HARVEST & CANONICAL RULESET GENERATION

**Goal**: Establish `strategy/_referee/` with every resource the audit needs, generated independently of UA's `_research/` outputs. Output: `strategy/_referee/_canonical/canonical-ruleset.md` + per-vertex `rules.md` files.

### 0.1 Existing-materials collection

Walk the repository for pre-existing primary sources. Known locations:

- `solutions-with-prize/paper08-yang-mills/math-referee/` — JW PDF, Wikipedia axiom archives, run reports
- `solutions-with-prize/paper08-yang-mills/notation-less-math-referee/` — legacy referee dir (may hold older references)
- Any `paper*/references/` or `paper*/pdfs/` subdirs

For each discovered primary source, copy to `strategy/_referee/<vertex>/sources/` with SHA-256 hash written to `sources/HASHES.txt`. Do not symlink; maintain our own copy for audit independence.

### 0.2 Prize-PDF download (only missing)

After 0.1, per prize-vertex check if the authoritative PDF exists locally. If missing, download:

| Vertex | Authoritative source |
|--------|---------------------|
| ym | claymath.org/wp-content/uploads/2022/06/yangmills.pdf |
| rh | claymath.org/wp-content/uploads/2022/06/riemann.pdf |
| bsd | claymath.org/wp-content/uploads/2022/06/birch-swinnerton-dyer.pdf |
| pvnp | claymath.org/wp-content/uploads/2022/06/pvsnp.pdf |
| hodge | claymath.org/wp-content/uploads/2022/06/hodge.pdf |
| ns | claymath.org/wp-content/uploads/2022/06/navierstokes.pdf |
| Rules for the Millennium Prizes | claymath.org/wp-content/uploads/2022/06/millennium_prize_rules.pdf |
| collatz | Bakuage terms of reference (July 2021 announcement + supplementary ToR) |

Download via WebFetch, save to `strategy/_referee/<vertex>/sources/`, SHA-hash. Write `sources/SOURCE-REGISTRY.md` with URL + fetch date + hash.

### 0.3 Per-prize rule extraction (MAX EFFORT)

For each prize vertex, dispatch a max-effort sub-agent that reads the primary source cover-to-cover and emits `strategy/_referee/<vertex>/rules.md` in the format modeled on `solutions-with-prize/paper08-yang-mills/math-referee/02-point-by-point-yang-mills.md` §2.

Sub-agent prompt template:

```
You are the rule-extraction sub-agent for <VERTEX>. Model: max reasoning effort.
Read strategy/_referee/<VERTEX>/sources/<primary-source>.pdf cover-to-cover. Do
NOT collapse requirements. For every binding condition the source states —
explicit or unambiguously derivable — emit a row with:
  - Rule ID (short code, e.g. W3, E0', T6)
  - Verbatim quote or unambiguous paraphrase
  - Source location (section / page / paragraph)
  - Category (mass-gap / axiom / field-operator / AF-match / stress-tensor /
    OPE / RP / volume / non-triviality / gauge-group / weak-existence / etc.)
  - Weight (HEAVY / MEDIUM / LIGHT based on difficulty)
Target: ≥ 30 rules per Clay vertex. Write to strategy/_referee/<VERTEX>/rules.md.
Emit verbatim-quote audit trail to strategy/_referee/<VERTEX>/extraction-notes.md.
Every rule must have a source citation; no invented rules.
```

Run 3-5 parallel vertex rule-extractors. The YM rule set already exists in `solutions-with-prize/paper08-yang-mills/math-referee/02-point-by-point-yang-mills.md` §2 — canonicalize it into `strategy/_referee/ym/rules.md` verbatim rather than re-extracting.

### 0.4 Generic ruleset distillation

After all prize rulesets land, distill the union into `strategy/_referee/_canonical/generic-ruleset.md`. Rules that appear across ≥3 prize vertices become generic. Rules unique to a single vertex remain vertex-specific.

Sub-agent prompt:

```
You are the generic-ruleset distillation sub-agent. Read every
strategy/_referee/<vertex>/rules.md (prize vertices only). Identify rules
that recur across ≥3 vertices. Emit strategy/_referee/_canonical/generic-ruleset.md
with: rule ID, canonical statement, list of source prize vertices it was
drawn from, weight. These rules apply to every non-prize vertex in the ring.
```

### 0.5 Programme-discipline extraction

Distill self-referential standards the programme already holds itself to. Read:

- `integers/paper01-qg5d/PROOF-CHAIN.md` (programme axioms + derivation discipline)
- `solutions-with-prize/paper08-yang-mills/math-referee/02-point-by-point-yang-mills.md` (~50-check ruleset + H4-group verification pattern)
- `strategy/_template/audit-brief-template.md` DELTA 6 (bare-mode discipline)
- `strategy/universal-approval-run.md` (bare-mode discipline, PAC primitives, §SELF-IMPROVEMENT LOOP)
- `strategy/_template/00-audit-strategy-template.md` (audit-gate structure)

Emit `strategy/_referee/_canonical/programme-discipline.md` with rules like:
- Every theorem cites its lemmas
- Every derivation has a dimensional check
- Every premise is axiom-or-citation (no floating assumptions)
- No circular dependencies
- No undefined symbols
- Every numerical prediction has a computation traceable to data
- Every claim marked PROVED has an arbiter verdict
- Bare-mode discipline: zero prose paragraphs, only theorem statements + definitions + equations + figures + numbers + citations

### 0.6 Canonical Ruleset union

Merge generic-ruleset + programme-discipline into `strategy/_referee/_canonical/canonical-ruleset.md`. This is what every non-prize vertex, and paper1 itself, is tested against. Every rule has a provenance line.

Emit `strategy/_referee/_canonical/provenance.md` — maps every canonical rule back to its source(s).

### 0.7 Rubric crystallization

Emit `strategy/_referee/_canonical/rubric.md`:

| Verdict | Meaning | Action |
|---------|---------|--------|
| PASS | Rule satisfied; proof present at cited location | None |
| PARTIAL | Rule partially satisfied; gap documented | Narrow the gap next cycle |
| CLOSABLE | Gap documented with a closure route (BYPASS/CONSTRUCT/EXCISE) | Execute closure |
| FAIL | Rule not satisfied, no closure route | Escalate — blocker |
| GENUINE | Gap is genuine and known to the field at large (not our failure alone); disclosed | Publish disclosure; add to Harden worklist if the gap sits on an external dep |
| SOUND (H4-style conditional) | Rule PASS conditional on a named hypothesis honestly disclosed | None — but monitor the hypothesis |

### 0.8 External-dep registry

Per vertex, enumerate every retained external dependency (anything not QG5D, not programme-internal, not classical). Write to `strategy/_referee/<vertex>/externals.md`:

- Name + citation (arXiv / DOI / preprint)
- What we rely on from it
- Status in the field (PROVED / CONDITIONAL / PRE-PRINT / CONTESTED)
- Hardening priority (HIGH / MEDIUM / LOW)

Union all vertex `externals.md` files into `strategy/_referee/_canonical/external-dep-registry.md` — the programme-wide list feeding Phase 5.

## PHASE 1 — PROGRAMME ROOT AUDIT (dependency closure)

**Goal**: Every programme paper that appears as a dependency of any UA deliverable has been audited against the Canonical Ruleset. Leaves first. Nothing downstream audited until its dependency set is PASS/CLOSABLE.

### 1.1 Build the dependency graph

Walk every file matching `strategy/*/deliverables/*-bare.md` + every `paper*/PROOF-CHAIN.md`. Extract all `paperNN-` references and all cross-programme citations. Build a DAG. Write to `strategy/_audit/dependency-graph.md` (adjacency list + topological order).

### 1.2 Topological sort + leaf identification

Leaves = programme papers that cite nothing programme-internal. Expected leaves at minimum: paper1 (QG5D). Any paper not cited by another programme paper but not cited by any deliverable is an orphan — flag but skip audit.

### 1.3 Audit leaves

For each leaf paper, dispatch a root-audit sub-agent:

```
You are the root-audit sub-agent for <PAPER>. Model: max reasoning effort.
Read <PAPER>/PROOF-CHAIN.md and every section referenced. Apply the
Canonical Ruleset at strategy/_referee/_canonical/canonical-ruleset.md
point-by-point. For each rule: emit verdict (PASS / PARTIAL / FAIL /
CLOSABLE / GENUINE / SOUND) + justification + location in <PAPER>. For
any verdict other than PASS, propose a PAC action (VERIFY / CONSTRUCT /
EXCISE / BYPASS / DECOMPOSE / TRANSPOSE) and rationale.
Write to strategy/_audit/_root/<PAPER>/comply.md (against canonical rules).
Also apply independence + harden discipline; write independence.md and
harden.md. Emit judge-dossier.md (four modes) and audit-dashboard.html.
```

### 1.4 Progress upward

After leaves are PASS/CLOSABLE, move to the next topological layer. A paper at layer L may be audited only once all papers in layers 0..L-1 are PASS/CLOSABLE.

### 1.5 Root audit gate

No Phase 3/4/5 vertex audit starts until the dependency closure of its deliverables is fully audited. The orchestrator blocks Phase 3+ until `strategy/_audit/_root/ROOT-AUDIT-COMPLETE.md` exists.

## PHASE 2 — STATE INSPECTION OF DOWNSTREAM DELIVERABLES

**Goal**: Inventory what exists to audit. No modifications. Output: `strategy/_audit/state-<timestamp>.md`.

Per vertex, record:
- Presence of `deliverables/<vertex>-comply-bare.md`, `-independence-bare.md`, `-harden-bare.md`, `-beyond-bare.md`
- Presence of `pac-output/runs/run-NN/` and LOCKED status
- Last modification date per file
- Line count per deliverable

Per external dep, record whether `strategy/externals-hardening/<ext>/` has been started.

## PHASE 3 — COMPLY AUDIT (Pillar A, point-by-point, per vertex)

**Goal**: Every `<vertex>-comply-bare.md` audited against `strategy/_referee/<vertex>/rules.md` (prize vertex) or `canonical-ruleset.md` (non-prize vertex). Output: `strategy/_audit/<vertex>/comply.md`.

### 3.1 Dispatch per-vertex comply-audit sub-agents (parallel, 3-5 at a time)

Template:

```
You are the COMPLY-audit sub-agent for <VERTEX>. Model: max reasoning effort.
Read strategy/<VERTEX>/deliverables/<VERTEX>-comply-bare.md. Read
strategy/_referee/<VERTEX>/rules.md (or _canonical/canonical-ruleset.md if
non-prize). Apply every rule point-by-point to the deliverable. For each
rule emit: verdict + justification + deliverable location (section/line) +
verbatim quote of the rule + PAC action if not PASS. Zero collapsing.
Discipline: bare mode (zero prose paragraphs in the verdict document).
Write to strategy/_audit/<VERTEX>/comply.md. Every FAIL or PARTIAL is
logged as an action for UA to fix next cycle. GENUINE gaps are surfaced
honestly — disclosure strengthens the submission.
```

### 3.2 Gate

After dispatch, check that every non-framework vertex has `strategy/_audit/<vertex>/comply.md` with every rule addressed (no SILENT cells).

## PHASE 4 — INDEPENDENCE AUDIT (Pillar B, per vertex)

**Goal**: Every `<vertex>-independence-bare.md` verified to have zero links conditional on unproved externals. Output: `strategy/_audit/<vertex>/independence.md`.

### 4.1 Dispatch per-vertex independence-audit sub-agents

```
You are the INDEPENDENCE-audit sub-agent for <VERTEX>. Model: max reasoning
effort. Read strategy/<VERTEX>/deliverables/<VERTEX>-independence-bare.md.
For every claim, trace its provenance: does it root in QG5D / paper1 /
programme-internal-audited / literature-PROVED / classical? If any link
roots in an unproved external, emit FAIL + PAC primitive recommendation
(BYPASS / DECOMPOSE / EXCISE / TRANSPOSE-via-capacitor). Compare to the
original compliance map's CONDITIONAL-on-external cells — did Pillar B
actually lift them? Write to strategy/_audit/<VERTEX>/independence.md with
per-claim verdict + provenance trace.
```

## PHASE 5 — HARDEN AUDIT (Pillar C, per vertex) + RECIPROCITY PREPRINT DRAFTS

**Goal**: Every retained external dep has been x-rayed, PAC-audited, and has a publishable reciprocity preprint drafted at `strategy/externals-hardening/<ext>/preprint-draft.md`.

### 5.1 Enumerate worklist

From `strategy/_referee/_canonical/external-dep-registry.md`, per external: identify vertices depending on it.

### 5.2 Dispatch per-external harden sub-agents (2-3 parallel)

```
You are the HARDEN sub-agent for external dependency <EXTERNAL>. Model:
max reasoning effort. Read the external's primary source (arXiv / preprint /
published paper). X-ray each layer of its proof (face / projection / pattern /
invariant per layer, following strategy/x-ray/x-ray-template.md). Apply PAC
primitives to every weak link: VERIFY (produce independent proof), CONSTRUCT
(provide missing construction), EXCISE (show dependence can be removed),
BYPASS (provide alternate route). Emit:
  strategy/externals-hardening/<EXTERNAL>/X-RAY.md
  strategy/externals-hardening/<EXTERNAL>/compliance-map.md
  strategy/externals-hardening/<EXTERNAL>/hardened-routes.md (the improvements)
  strategy/externals-hardening/<EXTERNAL>/narrative.md (fair attribution)
  strategy/externals-hardening/<EXTERNAL>/preprint-draft.md (publishable
    reciprocity paper honoring the original authors + disclosing the fix)
Tone: complementary, never dismissive. The original authors are credited
prominently. Our contribution is framed as hardening, not correction.
```

### 5.3 Per-vertex harden.md

After all externals a vertex depends on have been hardened, emit `strategy/_audit/<vertex>/harden.md` citing the external hardening artifacts and confirming every retained dep now sits on a strengthened foundation.

### 5.4 Reciprocity narrative

Every `preprint-draft.md` opens with: "We depend on [X] AND we strengthened [X]." The field benefits; the original authors are credited; our proof sits on provably firmer ground than any contender's.

## PHASE 6 — JUDGE DOSSIER + DASHBOARD

**Goal**: Every audited vertex ships `judge-dossier.md` (four modes) + `audit-dashboard.html` (interactive).

### 6.1 Dispatch per-vertex dossier-assembly sub-agents

```
You are the judge-dossier sub-agent for <VERTEX>. Read:
  strategy/_audit/<VERTEX>/comply.md
  strategy/_audit/<VERTEX>/independence.md
  strategy/_audit/<VERTEX>/harden.md
  strategy/<VERTEX>/deliverables/<VERTEX>-*-bare.md
  strategy/_referee/<VERTEX>/rules.md
Emit strategy/_audit/<VERTEX>/judge-dossier.md with four parts:
  Part I — Compliance Checklist (tabular, every rule ID × verdict × location)
  Part II — Referee Report (adversarial prose, every attack + resolution)
  Part III — Proof Walkthrough (narrative tour, axiom → theorem, cross-referenced)
  Part IV — Appendix: Externals Hardened (links to reciprocity preprints)
All four parts cite the same underlying audit artifacts. Every cell in
Part I is hyperlinked to a line in Part II and to a section in Part III.
```

### 6.2 Per-vertex dashboard HTML

Extend `visualization/build.py` or add `visualization/audit/build.py` (preferred — separation of concerns). Emit `strategy/_audit/<vertex>/audit-dashboard.html` with:
- Pie chart: verdicts per pillar (A/B/C)
- Heatmap: rules × pillars, colored by verdict
- Externals graph: vertex → externals → hardening preprints
- Timeline: when each rule was verified/fixed
- Filters: pillar / verdict / rule-weight / rule-category
- Click-through: any cell → open the corresponding checklist/referee/walkthrough section

Colors: PASS=green, PARTIAL=yellow, CLOSABLE=orange, FAIL=red, GENUINE=purple, SOUND=blue.

## PHASE 7 — CROSS-VERTEX COHERENCE PASS

**Goal**: QG5D (and every root-paper) claims are used consistently across vertices. Output: `strategy/_audit/coherence.md`.

### 7.1 Extract cross-vertex citations

For every citation of paper1 (or any root paper) from a downstream deliverable, record: source vertex + target paper + cited claim (verbatim) + programme section.

### 7.2 Dispatch coherence sub-agent

```
You are the cross-vertex coherence sub-agent. For every root-paper claim,
compare its usage across all citing deliverables. Flag any discrepancy:
different wording for the same claim, different numerical values, different
conditions. Emit strategy/_audit/coherence.md with: claim ID, source in
root paper, list of vertices citing it, per-vertex wording, verdict
(CONSISTENT / DRIFT / CONTRADICTION). For DRIFT or CONTRADICTION,
recommend canonical wording and log which deliverables need update.
```

## PHASE 8 — GLOBAL REPORT + GLOBAL VISUALIZATION

**Goal**: Top-down programme view. Outputs: `strategy/_audit/AUDIT-REPORT.md` + `strategy/_audit/audit-visualization.html`.

### 8.1 AUDIT-REPORT.md

Rollup across every audited vertex + external + root paper:
- Per-vertex status (Pillar A/B/C verdict counts)
- Per-external status (hardening stage)
- Root-audit health (every root paper's rule-pass-rate)
- Cross-vertex coherence verdict
- Convergence vs previous cycle (byte-identical? delta list?)
- Recommendations for next cycle
- Sections per vertex with direct links to `judge-dossier.md`

### 8.2 audit-visualization.html

Interactive programme-wide view:
- Ring/torus of all vertices, node color = overall health score
- Stacked bars: rules-pass-rate per vertex per pillar
- Cross-vertex coherence matrix (green/red grid)
- Externals-reciprocity graph (vertex ↔ external ↔ hardening-preprint draft status)
- Rule-provenance histogram (Clay / Bakuage / programme-discipline / canonical-rule)
- QG5D (or root dependency set) at the center with radial spokes
- Filters: prize-status / vertex / pillar / verdict / external / date
- Click-through: any node → per-vertex dashboard

Build script: `visualization/audit/build.py` (new).

## PHASE 9 — CONVERGENCE CHECK + DUAL-LOOP WITH UA

**Goal**: Decide whether this cycle produced changes AND whether the audit + UA pair has converged.

### 9.1 Audit-run convergence

Diff `state-<timestamp>.md` from this run's Phase 2 against the previous run's Phase 2. No differences → audit-run CONVERGED. Differences → log deltas, recommend next cycle.

### 9.2 Dual-loop with UA

The audit-run and UA run ping-pong:

1. UA synthesizes deliverables (Phase 5 of UA)
2. Audit extracts rules + tests deliverables + surfaces verdicts
3. FAIL and CLOSABLE verdicts flow back to UA as Phase 4 compliance-audit deltas
4. UA re-synthesizes with fixes
5. Audit re-tests

**Global convergence** = two consecutive full cycles produce:
- Byte-identical `strategy/_audit/state-*.md`
- Byte-identical `strategy/_research/state-*.md`
- Every audit verdict is PASS, CLOSABLE, or SOUND (disclosed-conditional)
- Every cross-vertex coherence cell is CONSISTENT
- Every retained external has a published-draft reciprocity preprint

When global convergence is reached, emit `strategy/_audit/GLOBAL-CONVERGENCE.md` — the programme is Zenodo-ready.

## PHASE 10 — SELF-IMPROVEMENT (ruleset update)

**Goal**: Every failure pattern encountered this cycle feeds back into the Canonical Ruleset. Cycle N+1 is stricter than cycle N.

### 10.1 Failure-pattern extraction

Walk every FAIL, PARTIAL, and GENUINE verdict this cycle. For each, identify:
- Was this rule already in the Canonical Ruleset? (Yes → rule is working; just needs UA resynthesis)
- Was this a novel failure mode? (Yes → new rule candidate)

### 10.2 New-rule proposals

For each novel failure mode, draft a new rule with provenance ("emerged from <VERTEX> audit on <DATE>"). Append to `strategy/_referee/_canonical/canonical-ruleset.md` after user review.

### 10.3 Fixes log

Append to `strategy/_audit/fixes-log.md` (mirror of UA's `strategy/_research/fixes-log.md`): timestamp, failure mode, root cause, rule added, expected behavior.

## IDEMPOTENCE

This run is IDEMPOTENT: re-running with no upstream changes produces no modifications. Self-healing: any missing resource (PDF, hash-mismatched source, deleted rules.md) is regenerated from primary sources.

Per-phase idempotence checks:
- Phase 0: skip if SHA match + rules.md freshness ≥ source freshness
- Phase 1: skip a root-paper audit if PROOF-CHAIN unchanged since last audit
- Phase 3-5: skip a vertex audit if `<vertex>-*-bare.md` mtime ≤ last audit mtime
- Phase 6: skip dossier if all inputs unchanged
- Phase 7-8: always re-run (aggregations)

## SELF-HEALING

If at any phase a required resource is missing:
- Missing PDF → redownload from registered URL, hash-verify
- Missing rules.md → re-extract from source (max-effort sub-agent)
- Missing canonical-ruleset → rebuild from per-vertex rules + programme-discipline
- Missing root-audit → dispatch root-audit sub-agent
- Missing dossier → re-assemble from audit outputs

Never fail silently. Log every self-heal to `strategy/_audit/self-heal-log.md`.

## AUDIT CYCLE

Intended workflow:

1. Fire UA (`strategy/universal-approval-run.md`)
2. Fire audit (`strategy/independent-audit-run.md`)
3. Review `strategy/_audit/AUDIT-REPORT.md` and `audit-visualization.html`
4. Any FAIL or PARTIAL → UA resynthesizes next cycle
5. Any GENUINE → publish disclosure + harden the external
6. Repeat until global convergence (two consecutive cycles byte-identical + all verdicts PASS/CLOSABLE/SOUND)
7. Move to Zenodo release

First-cycle expected duration: 8-12 hours (cold run, rule extraction is heavy).
Nth-cycle after near-convergence: 20-30 minutes.

## SELF-IMPROVEMENT LOOP (failure handling)

This protocol is intentionally self-modifying. When a sub-agent fails, produces unusable output, or the orchestrator hits a blocker, the orchestrator's job is NOT to stop — it is to DIAGNOSE and UPDATE THIS DOCUMENT to prevent recurrence, then re-run to verify the fix.

### When a sub-agent fails

1. Diagnose root cause (prompt unclear? source missing? discipline under-specified?)
2. Update the relevant sub-agent prompt template directly in this file
3. Log the fix to `strategy/_audit/fixes-log.md` with: timestamp, which sub-agent, root cause, exact edit, expected behavior
4. Re-dispatch the failed sub-agent
5. Iterate until the sub-agent succeeds

### When the orchestrator fails

1. Write recovery note to `strategy/_audit/orchestrator-recovery-<timestamp>.md`
2. Update THIS file with lessons learned
3. Next orchestrator invocation picks up from the recovery note

### Discipline

- Never delete earlier protocol language — only ADD, SHARPEN, or COMMENT (prefix obsoleted text with `<!-- OBSOLETE YYYY-MM-DD: reason -->`)
- Always log fixes to `fixes-log.md`
- Never skip phases to work around failures — fix the phase, then re-run
- If unsure whether to fix the protocol or the sub-agent prompt, fix BOTH, log BOTH

### What counts as failure

- Sub-agent produces empty or malformed output
- Sub-agent collapses rules (violates point-by-point discipline)
- Sub-agent invents a rule without source citation
- Verdict lacks deliverable location
- GENUINE gap is hidden (no disclosure)
- Reciprocity preprint is dismissive of original authors
- Dashboard build fails
- Cross-vertex coherence misses a DRIFT case
- Global convergence check fails repeatedly
- **Agent/Task tool unavailable**: complete dispatchable phases (0 harvest portions, 2, 7, 8, 9), emit `NEEDS-USER-DISPATCH.md` listing per-vertex Agent-invocation blocks, log failure class `AGENT-TOOL-UNAVAILABLE`

Any of these triggers the self-improvement loop.

### First-person instruction to the orchestrator

When you hit a blocker:

1. Pause the phase
2. Read this SELF-IMPROVEMENT LOOP section
3. Diagnose (1-3 sentences in blackboard)
4. Edit THIS FILE to prevent recurrence — use the Edit tool
5. Append to `strategy/_audit/fixes-log.md`
6. Resume the phase with the updated protocol

The user has pre-authorized self-modifications via this section.

## SAFETY CAVEATS

- **Do NOT overwrite existing audit files without diff-check**. Preserve manual refinements. When in doubt, emit `.pending.md` siblings.
- **Do NOT delete files.** Only add / update.
- **Do NOT fire more than 10 parallel sub-agents simultaneously.** Batching required.
- **Do NOT skip Phase 0.** Canonical Ruleset generation is how every downstream verdict roots in provenance.
- **Do NOT skip Phase 1.** Dependency closure is how the audit has a sound foundation.
- **Do NOT commit to git unless user explicitly requests.** This run produces a working tree; commit discipline is the user's.
- **Do NOT publish reciprocity preprints without user review.** Phase 5 emits DRAFTS; user authorizes release.
- **Every GENUINE gap is DISCLOSED, not hidden.** Disclosure strengthens the submission; hiding failures weakens it catastrophically.

## THINGS THIS RUN DOES NOT DO

- Actual prize submission (downstream; separate orchestrator)
- arXiv upload of reciprocity preprints (user-authorized only)
- Zenodo release
- Pre-submission outreach emails
- Journal submission drafting (beyond the reciprocity preprint drafts)
- Paper merge/consolidation (deferred post-convergence)
- Replacement of UA's synthesis — audit tests what UA produces; it does not re-produce

These are downstream of this run's scope.

## DUAL WITH UA

| UA | Independent Audit |
|----|-------------------|
| Synthesizes deliverables meeting requirements | Audits deliverables against independently-extracted requirements |
| Researches requirements online (outlet.md, landscape.md) | Harvests primary sources independently; extracts rules from them |
| Three pillars per vertex (COMPLY / INDEPENDENCE / HARDEN) | Three pillar audits per vertex (comply.md / independence.md / harden.md) |
| Beyond-bare supplement (programme bonuses) | Quadruple-mode judge dossier (checklist / referee / walkthrough / HTML) |
| Integrates acknowledgments from landscape.md | Drafts publishable reciprocity preprints for every retained external |
| Emits main viz + torus viz | Emits per-vertex audit-dashboard.html + global audit-visualization.html |
| Convergence: state snapshots identical | Convergence: state snapshots identical + all verdicts PASS/CLOSABLE/SOUND |

The two runs are designed to ping-pong. Together they produce the Zenodo-release artifact.

---

## QUICKSTART

Copy everything above (§PHASE 0 through §PHASE 10) into a local Claude Code agent invocation. The agent follows the protocol step by step, emitting `AUDIT-REPORT.md` + `audit-visualization.html` when done.

For the first cycle: expect 8-12 hours, ~20-30 parallel sub-agents across phases 0, 1, 3, 4, 5, 6.

For the Nth cycle near convergence: expect 20-30 min, near-zero work.

---

*Sibling to: `strategy/universal-approval-run.md`, `strategy/independent-audit-rationale.md`, `strategy/_template/README.md`, `solutions-with-prize/paper08-yang-mills/math-referee/02-point-by-point-yang-mills.md` (the pilot for the point-by-point discipline).*

*Every projection of the 5D geometry → point-by-point audited → rules extracted from primary sources → externals hardened and published → judge-ready in four reading modes → visualized globally. The protocol is water-tight. Run. Audit. Re-run. Converge. Ship.*

*G Six and Claude Opus 4.6. April 14, 2026.*
