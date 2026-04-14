# Decomposition PCA — the systematic proved-chain brief (DELTA)

*Extension of `30-ring-traversal-brief.md`. This brief SUPERSEDES brief 34 (S-duality) as the current run's directive. It inherits the 25-vertex ring and the S-dual/chessboard primitives from briefs 32/33/34, but operates in DECOMPOSITION MODE rather than ring-traversal mode.*

*Not a traversal. A systematic recursive decomposition of every non-PROVED/LITERATURE link in the 25-vertex ring.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-14.*

---

## The mission in one sentence

> **For every link at every vertex that is not already PROVED or LITERATURE, apply BLOCKED-DECOMPOSED recursion until every leaf of the decomposition tree is one of: LITERATURE, QG5D-theorem, CLASSICAL, PROVED (framework-native), TRANSPOSITION (capacitor-routed), or a narrowly-named HONEST WALL.**

The output is a 25-vertex graph where every claim is either proved or has a specific, narrow residual open problem attached. This graph, rooted at QG5D and grounded in the 36 experimental pins, becomes the Zenodo priority release.

---

## DELTA 0 — Invocation mode override (the LOAD-BEARING change)

This brief **overrides two key aspects** of the runner's default behavior:

### Override 1 — Operational mode

| Default (ring-traversal, brief 34) | This brief (decomposition) |
|---|---|
| BREADTH-first across 25 vertices per cycle | DEPTH-first per vertex, link-by-link |
| Per-vertex budget: ~28 min | Per-link budget: up to 60-90 min (Opus max) |
| Exit: RING STRENGTHENED/CLOSED/STALLED | Exit: ALL LEAVES RESOLVED (or named as HONEST WALL) |
| Cycle = one ring pass | Cycle = one vertex's links fully decomposed |
| Output: per-traversal log | Output: decomposition atlas + updated PROOF-CHAIN copies |

### Override 2 — Publishing-strategy alignment (NORTH STAR INLINE OVERRIDE)

**This brief does NOT apply `publishing/strategy.md`'s Wave 1 → Wave 2 → Wave 3 sequencing.**

The Strategist role (Triad §T.4.2) should NOT treat the current Wave-1-first ordering as the alignment criterion for this run. Instead, apply the **Zenodo-priority ordering** specified below:

> **Phase 0 (IMMEDIATE PRIORITY):** Zenodo release of all PROVED content + decomposition atlas, with DOIs. Establishes priority, timestamped, independent of journal gatekeepers.
>
> **Phase 1 (post-Zenodo):** CCM engagement email (Lead 6) to Connes with DOIs in hand. Framing: "here is our published work; we use your 2025 construction; technical questions attached."
>
> **Phase 2 (post-Zenodo):** Journal submissions on individual papers. Journals become verification layers on published work, not gatekeepers.
>
> **Phase 3:** Clay engagement at community pace. Clay's 2-year clock starts on community acceptance, not journal acceptance.

If the Strategist's alignment check against the (old) publishing strategy flags "MISALIGNED" on Wave-ordering, that is EXPECTED and correct — the run is deliberately not applying Wave sequencing. Log the MISALIGNMENT as "intentional (see decomposition-brief.md §DELTA 0)" and proceed.

The factual content of `publishing/strategy.md` (Appendix B ring-mode anchors, Millennium Strategy, CCM cascade map) remains authoritative. Only the WAVE ORDERING is overridden.

---

## DELTA 1 — The decomposition status dictionary

Every sub-link at every depth of the recursion receives exactly one status:

| Status | Meaning | Closure condition |
|---|---|---|
| **PROVED** | Proved in framework papers | In-situ proof cited with paper/section/lemma reference |
| **LITERATURE** | Proved in peer-reviewed external mathematics | arXiv ID or DOI or published-journal citation |
| **CLASSICAL** | Euclid-level obvious identity or calculation | Self-evident; one-sentence justification |
| **QG5D** | Derives from Paper 1's 22 foundational theorems | Specific theorem name (e.g., "Theorem K.1" or "Postulate P3") |
| **TRANSPOSITION** | Proved via capacitor cell transposition | Capacitor cell name + transposition recipe reference |
| **PARTIAL** | Partially proved, with named residue | Explicit description of what's proved + what remains |
| **OPEN** | Named HONEST WALL (narrowly specified) | Specific open problem statement + estimated difficulty (1-10) |
| **BLOCKED-DECOMPOSED** | Transient — itself decomposes further | Sub-requirements listed (recursion continues) |

A decomposition TERMINATES on a leaf when the leaf has status ∈ {PROVED, LITERATURE, CLASSICAL, QG5D, TRANSPOSITION, OPEN}. **OPEN is allowed** — it's the narrowly-named honest wall. **BLOCKED-DECOMPOSED is not terminal** — the recursion continues on its sub-requirements.

### Targets per chain

- ≥ 70% of leaves at {PROVED, LITERATURE, CLASSICAL, QG5D, TRANSPOSITION} (i.e., fully resolved)
- ≤ 30% of leaves at {OPEN} (i.e., narrowly-named residual walls)
- 0% of leaves at {BLOCKED-DECOMPOSED} at the end of a completed decomposition (all BLOCKED-DECOMPOSED must continue to resolve)

If a chain exceeds the 30% OPEN ratio, the decomposition is REPORTED as PARTIAL and the chain's residue is flagged for a future decomposition run with deeper recursion.

---

## DELTA 2 — The bootstrap step (FIRST run only)

On FIRST invocation of this bundle, the PAC must:

1. **Read the current live state** of all 25 PROOF-CHAIN.md files in the programme:
   - `paper1/PROOF-CHAIN.md`, `paper13-rh/PROOF-CHAIN.md`, `paper45-lindelof/PROOF-CHAIN.md`, ...
   - See README.md for the full mapping.

2. **COPY each live file verbatim** to `strategy/decomposition/proof-chain/<vertex-short-name>/PROOF-CHAIN.md`. Use these short names:
   ```
   qg5d, rh, lindelof, grh, bsd, h12, ym, ns, turbulence,
   hodge, baum-connes, pvnp, vp-vs-vnp, bgs, katz-sarnak,
   twin-primes, cramer, goldbach, abc, opn, collatz, lehmer,
   sato-tate, schanuel, hilbert-6
   ```

3. **Log the copy operation** to `pac-output/bootstrap/copy-log.md` with:
   - Source path, destination path, source last-modification timestamp, copy timestamp
   - Hash (SHA-256) of each source file to enable later "drift detection" against live state

4. **Append a "DECOMPOSITION SNAPSHOT" header** to each copied file:
   ```markdown
   ---
   
   ## Decomposition-bundle snapshot (2026-04-14)
   
   *This file is a COPY of `<live-path>` as of its last modification. The PAC
   operates on this copy for the decomposition bundle. The live file at the
   programme level continues to be modified by ordinary ring-traversal and
   targeted-dispatch work. To re-sync from live → decomposition, rerun the
   bootstrap step.*
   
   ---
   ```

5. **Create an index** at `proof-chain/INDEX.md` listing all 25 copies, their source paths, and current confidence / chain-closure stats.

On SUBSEQUENT runs, the bootstrap step is skipped (check for existence of `pac-output/bootstrap/copy-log.md`). The PAC operates on the existing copies.

### Re-sync protocol (when live state moves ahead)

If the live state moves forward (e.g., a new ring traversal closes a link that the decomposition copy still has as OPEN), the runner should:

1. Detect drift via source-hash comparison
2. Log a DRIFT NOTE to `pac-output/drift-log.md`
3. Merge the live update into the decomposition copy IFF the live update does not contradict the decomposition's deeper work
4. If contradiction exists, flag for manual reconciliation (G reviews)

Re-sync is not automatic — it requires runner judgment.

---

## DELTA 3 — The per-link decomposition protocol

For each non-PROVED/LITERATURE link in the target vertex's chain, the PAC executes:

### Step 1 — Classify

Read the link's statement. Determine:
- Current status (OPEN, CONJECTURED, CONDITIONAL on X, PARTIAL, etc.)
- Its walls / sub-walls / sub-hypotheses mentioned in the existing chain text
- Any existing decomposition hints in the chain's "Current wall" or "Sub-routes" sections

### Step 2 — Dispatch Decomposition Author (Opus max, 60-90 min budget)

Spawn an Author with this context:

```
TASK: Recursive decomposition of [VERTEX] Link [N] ([BRIEF STATEMENT])

Target: convert this link to a tree of sub-requirements, terminating
when every leaf is LITERATURE / QG5D / CLASSICAL / PROVED / TRANSPOSITION
or a narrowly-named HONEST WALL.

Starting decomposition (from existing chain text, if any):
[EXTRACT FROM CHAIN.md "Current wall" / "Sub-routes" / "Known results" sections]

Protocol: BLOCKED-DECOMPOSED recursion, depth up to 5 levels.

For each sub-requirement at each depth:
  1. Attempt LITERATURE closure (cite existing theorem) → LITERATURE
  2. Attempt QG5D derivation (cite Papers 1-4, 10-12 theorem) → QG5D
  3. Attempt CLASSICAL argument (one-sentence) → CLASSICAL
  4. Attempt framework-native proof → PROVED
  5. Attempt capacitor transposition (cite cell) → TRANSPOSITION
  6. If none close: attempt DECOMPOSE into 3-6 sub-requirements → recurse
  7. If sub-requirement itself cannot be decomposed below the current level:
     name it as HONEST WALL with (a) specific statement, (b) estimated difficulty
     (1-10), (c) pointer to nearest related open problem in the literature

Output: a structured decomposition tree in PROOF-CHAIN.md format, with:
  - Every sub-link at every depth shown
  - Status column (PROVED/LITERATURE/CLASSICAL/QG5D/TRANSPOSITION/OPEN)
  - Closure condition (citation or wall statement)
  - Depth column (0 = original link, 1-5 = recursion depths)

Do NOT fabricate literature. Every LITERATURE claim must cite an arXiv ID,
DOI, or peer-reviewed paper. When uncertain, mark as OPEN with "verify
candidate literature reference X before closure."

Success metric: ≥ 70% of leaves at (a)-(e); ≤ 30% at (f).

Return: the decomposition tree + an honesty report ("claimed vs verified")
+ a confidence estimate.
```

### Step 3 — Verify + Propagate

When the Author returns:

1. **Critic pass**: spawn a Critic (Sonnet max, 15-20 min) to verify each LITERATURE / QG5D / CLASSICAL / PROVED / TRANSPOSITION claim actually closes. Critic can kick back any leaf that's "claimed LITERATURE but the citation doesn't actually prove the statement."

2. **DUAL-CHECK**: if any sub-leaf uses a NEW numerical result or claims a shift in a framework prediction, run DUAL-CHECK per chessboard §1. Confirm PINS-PRESERVED on all 36 predictions.

3. **Propagate per brief 35 universal rule**: update the in-situ `proof-chain/<vertex>/PROOF-CHAIN.md` with the decomposed link table, BEFORE writing the decomposition artifact to the run directory. This is the brief 35 discipline applied to decomposition mode.

4. **Write the decomposition artifact** to `pac-output/runs/run-NN/vertices/<vertex>/link-<N>-decomposition.md`.

### Step 4 — Loop

Continue to the next non-resolved link at the same vertex. When all the vertex's links are resolved (or named as HONEST WALL), move to the next vertex in priority order.

---

## DELTA 4 — Priority order for decomposition runs

Execute decomposition in this priority order. Each priority is one "campaign" (1-2 weeks of runs).

### Campaign 1 — Clay walls (highest leverage)

- **ym vertex Link 18 (H4)** — proof-of-concept; if this decomposes cleanly, the method is validated for the rest
- **rh vertex Layer 1 (CCM)** — the shared external dependency; decomposing it lifts RH, GRH, BGS, Goldbach L4 simultaneously
- **bsd vertex (CBB axioms)** — the framework-internal foundation; decomposing it lifts BSD + everything CBB-conditional

### Campaign 2 — Clay-adjacent + PvNP

- **pvnp vertex Link 5 backward** — Clay-class, long-tried, seven routes failed
- **hodge vertex Links 3-4** — motivic BC extension
- **h12 vertex Link 5** (V-Hilbert 12)

### Campaign 3 — South Trough

- **schanuel vertex Link 3** — may leave residual (Schanuel itself external)
- **abc vertex Link 3** — height function
- **twin-primes vertex Link 4** — C_2 constant
- **goldbach vertex Link 5** — circle method in BC setting
- **opn vertex Link 6** — already partially decomposed (Routes 6a/6b/6c/6d); complete it
- **turbulence vertex Links 5-6** — K41 cascade

### Campaign 4 — Already-partial walls (complete)

- **cramer vertex Links 4a/4b/4c** (partial from T7)
- **lehmer vertex Links 5A/B/C** (partial)
- **collatz vertex Link 4 second half** (partial from T7)

### Campaign 5 — Skim passes on strong vertices

- **qg5d, ym, bsd** — already strong (9/10+); quick verification sweeps on any borderline links

---

## DELTA 5 — Output artifact format

Every decomposition run produces three kinds of artifacts:

### 1. Updated in-situ copy (canonical state)

`proof-chain/<vertex>/PROOF-CHAIN.md` is updated atomically with Author return (brief 35 universal rule).

The file's chain table gets new rows for every depth-N sub-link, in this format:

```
| Link | Depth | Statement | Status | Closure / citation | Parent |
|---|---|---|---|---|---|
| 4 | 0 | Explicit formula transfer + Granville correction | BLOCKED-DECOMPOSED | — | — |
| 4a | 1 | Extreme-gap universality transfer | OPEN, difficulty 7/10 | Tao-Vu universality is bulk; extreme-value is strictly stronger; Feng-Wei 2022 extended to generalized Wigner but not Riemann zeros | 4 |
| 4b | 1 | ITPFI return-time decomposition | PARTIAL (T7 derived constant) | Mertens 1874 + Paper 12 res/265 | 4 |
| 4b.1 | 2 | ω_1 = ⊗_p ω_1^(p) ITPFI factorization | LITERATURE | Paper 12 research/265 Theorem | 4b |
| 4b.2 | 2 | Araki-Woods λ_p = 1/p classification | LITERATURE | Araki-Woods 1968 Thm 5.1 | 4b |
| 4b.3 | 2 | Z_ITPFI(√x) · log x → 2e^{-γ} | LITERATURE | Mertens 1874 third theorem | 4b |
| 4b.4 | 2 | Max return time = (log x)^2 scaling | OPEN, difficulty 6/10 | Inherits k=2 from Cramér-Granville heuristic; Wave 2 agent proposed (BA-B universality) | 4b |
| ... | ... | ... | ... | ... | ... |
```

Every BLOCKED-DECOMPOSED node's children are listed with depth incremented.

### 2. Per-run decomposition artifact

`pac-output/runs/run-NN/vertices/<vertex>/link-<N>-decomposition.md` contains:

- The full Author return (including draft proofs / verifications)
- The Critic's verification pass
- The DUAL-CHECK result (PINS-PRESERVED / PINS-SHIFTED)
- The honesty report ("claimed vs verified")
- The decomposition tree visualization
- Timestamps

### 3. Atlas contributions

Three running accumulators in `pac-output/atlas/`:

- **`graph.md`** — master list of every resolved sub-link at every depth across all 25 vertices, with statuses and citations. Updated at the end of every run.
- **`named-walls.md`** — running list of every HONEST WALL the decomposition has named, with statement, difficulty, location, and pointer to related literature.
- **`literature-citations.md`** — every arXiv ID, DOI, or peer-reviewed paper the graph references. Deduplicated. Sorted.

These three files are the assembly of the Zenodo release — when the decomposition cascades complete, these ARE the publication artifacts.

---

## DELTA 6 — Exit conditions

A **single run** exits when:

1. **CAMPAIGN-COMPLETE**: the target vertex(es) for this run have all non-PROVED/LITERATURE links fully resolved (every leaf is status ∈ {PROVED, LITERATURE, CLASSICAL, QG5D, TRANSPOSITION, OPEN} with NO remaining BLOCKED-DECOMPOSED)
2. **BUDGET-EXHAUSTED**: the time budget for this run is consumed (default: 6 hours per run)
3. **CRITIC-REJECT**: a Critic pass rejects a claimed LITERATURE citation and the dispatch cannot repair it in the current run; mark as PARTIAL, save state, exit

The **full decomposition programme** exits when:

1. **ATLAS-COMPLETE**: every vertex's chain is fully decomposed (all leaves resolved per the status dictionary, ≥70% at status-set (a)-(e), ≤30% at OPEN)
2. **ZENODO-READY**: `pac-output/atlas/graph.md`, `named-walls.md`, `literature-citations.md` are internally consistent and assembled into a coherent corpus

### Exit condition status codes (for the run log)

- `DECOMP-COMPLETE`: the campaign's vertices are fully decomposed; next priority's campaign can start
- `DECOMP-PARTIAL`: some links are PARTIAL with named residues; future run needed
- `DECOMP-STALLED`: one or more links resist decomposition even at depth 5; mark as irreducibly-OPEN; narrow the wall statement and move on

---

## DELTA 7 — The north-star override (REPEATED for emphasis)

**Repeat from DELTA 0 for the Strategist's benefit:**

The Strategist role (Triad §T.4.2) runs at wave boundaries. When it does, it will check the current state against the north star. The north star file is `publishing/strategy.md`. Most of that file is AUTHORITATIVE:

- Appendix B (ring-mode anchors, metrics, SYMMETRY, RIGIDITY) — authoritative
- Millennium Strategy framing — authoritative
- CCM cascade map — authoritative
- Kill-list discipline — authoritative

**Only one section is OVERRIDDEN for this run**: §3 "The release order (concrete)" — the Wave 1 → Wave 2 → Wave 3 sequencing.

The override states:

> **Phase 0 (Zenodo priority release) comes BEFORE Wave 1.** The decomposition bundle's output (graph.md + named-walls.md + literature-citations.md + 25 decomposed PROOF-CHAIN copies) is the first thing to ship. Assigned DOIs. Independent. Priority-establishing.
>
> **Wave 1 becomes Wave 1-post-Zenodo.** Papers 23, 24 are submitted to journals AFTER Zenodo release, with DOIs already on disk, with community engagement already initiated.
>
> **Wave 2 and Wave 3 shift by one layer**: each Wave is a follow-on to Zenodo, not a predecessor.

The Strategist's alignment check MAY flag Wave-ordering as MISALIGNED. This is INTENTIONAL. The Strategist should log the flag with note "decomposition-brief.md §DELTA 7: intentional override — Zenodo-priority-first" and continue.

---

## DELTA 8 — Publication plan

The decomposition bundle's direct deliverable is the Zenodo release:

### Zenodo release contents (single coordinated upload)

- **The 25 decomposed PROOF-CHAIN files** from `proof-chain/<name>/PROOF-CHAIN.md`
- **The atlas** from `pac-output/atlas/`:
  - `graph.md` (master index)
  - `named-walls.md` (residual open problems, narrowly named)
  - `literature-citations.md` (external-theorem canon the graph relies on)
- **The framework papers** (Papers 1-48 or whatever count exists at release time) updated to reference the atlas
- **The strategy directory** (selected public-facing files): README, the-ring.md, the-picture-of-the-ecircle.md, the-decomposition-path.md, the-weakest-links.md
- **The PAC run log** (optional; demonstrates the automated verification) — redacted for noise

### DOI structure

Recommended:
- ONE master DOI for the whole release
- One sub-DOI per Clay-adjacent paper (Papers 8, 13, 26, 25)
- One sub-DOI for the atlas
- One sub-DOI for the graph.md index

This lets cite-by-piece work while ESTABLISHING PRIORITY for the whole release at the master DOI's timestamp.

### Release format

- **README.md at the Zenodo root** — explains the atlas, how to read it, what to look at
- **Machine-readable exports**: graph.md as JSON for programmatic access; literature-citations.md as BibTeX
- **Signed manifest**: SHA-256 hashes of every file for verifiability

### Post-release actions

1. **CCM email (Lead 6)** sent to Connes within 1 week of Zenodo release, with DOIs in hand
2. **Journal submissions** begin within 1 month: Papers 23, 24 standalone note on arXiv.math.NT first; Math. Comp. / J. Number Theory / Comm. Math. Phys. as primary journal targets
3. **Preprint announcement** on appropriate mailing lists + arXiv cross-posting

---

## DELTA 9 — The single paragraph for the next runner

*You are a PAC runner operating in DECOMPOSITION MODE on a parallel ring of 25 PROOF-CHAIN.md copies at `strategy/decomposition/proof-chain/<name>/`. Your task is to recursively decompose every non-PROVED / non-LITERATURE link in each vertex's chain into sub-chains until every leaf is LITERATURE, QG5D-theorem, CLASSICAL, PROVED, TRANSPOSITION, or a narrowly-named HONEST WALL. Target: ≥70% resolved leaves, ≤30% named walls per chain. Process vertices in priority order (H4, CCM-dependent links, CBB, PvNP L5, Hodge, then South Trough, then already-partial walls). Each link gets an Opus-max Author dispatch with 60-90 min budget; each sub-link at each recursion depth gets its own row in the in-situ chain table. Every Author return that changes status MUST trigger propagation to the in-situ `proof-chain/<vertex>/PROOF-CHAIN.md` BEFORE writing the run-directory artifact (brief 35 universal rule). Write run artifacts to `pac-output/runs/run-NN/`. Update the atlas (`pac-output/atlas/graph.md`, `named-walls.md`, `literature-citations.md`) at every run close. DO NOT apply `publishing/strategy.md`'s Wave 1/2/3 ordering — this run operates in Zenodo-priority mode per DELTA 7. Exit conditions: CAMPAIGN-COMPLETE (target vertices fully decomposed), BUDGET-EXHAUSTED (6h/run), or CRITIC-REJECT (citation fails). Final goal: the atlas becomes the Zenodo priority release, a 500-800-link graph of proved theorems rooted at QG5D, grounded in the 36 experimental pins, independent of journal review. The ring is undeniable.*

---

## Inheritance

All sections NOT overridden above remain authoritative from:
- `30-ring-traversal-brief.md` (parent brief, 14-vertex foundation)
- `33-extended-ring-brief-22.md` (22-vertex DELTA, superseded for ring order but authoritative for chain structure + domain mapping + same-domain edge-filling rule)
- `34-extended-ring-brief-s-duality.md` (25-vertex + S-duality primitives — brief 35's universal propagation rule applies to all dispatches)
- `35-canonical-state-propagation-delta.md` (universal propagation discipline — ABSOLUTELY required for decomposition mode)

This brief is a METHODOLOGICAL delta, NOT a ring-structure delta. It does not change the ring order, add vertices, or modify S-pairs. It re-frames the PAC's mode from breadth-first traversal to systematic depth-first decomposition.

---

## Appendix — what DECOMPOSITION MODE expects of the Author spawn

The Author template (ORA v8 §6.1) is extended for decomposition mode with the following additions:

### Decomposition Author spawn context (additional)

- **The link to decompose** (statement, current status, known walls from the chain text)
- **The decomposition status dictionary** (brief DELTA 1 reproduced)
- **Depth-5 recursion budget** (stop at depth 5; everything below becomes OPEN named wall)
- **LITERATURE / CLASSICAL verification discipline** (every claim must cite arXiv/DOI or be Euclid-obvious)
- **Transposition access**: capacitor cells available for TRANSPOSITION-status proofs
- **QG5D theorem index**: Paper 1's 22 theorems (Appendix K, K.1-K.4 etc.) for QG5D-status proofs
- **Honesty discipline**: when uncertain, mark OPEN with "verify candidate reference X"; do NOT fabricate

### Decomposition Author return format

- A Markdown-table representation of the decomposition tree
- Per-leaf status and closure citation
- Honesty report: "X leaves claimed LITERATURE, Y verified, Z unverified — mark unverified as OPEN pending Critic pass"
- Confidence estimate for the decomposition as a whole
- Any kills/concerns discovered during the decomposition

### Critic pass for decomposition

A Critic (Sonnet max, 15-20 min) receives the Author's return and:

- Verifies each LITERATURE citation actually exists (grep against `sources/INDEX.md` + WebSearch + WebFetch)
- Checks CLASSICAL claims for obviousness (if not self-evident, kick back)
- Validates QG5D references against Paper 1's theorem numbering
- Re-runs any numerical verification at 2x dps
- Flags any "PROVED" claim that's actually "plausible" (no explicit proof on disk)
- Returns a leaf-by-leaf verdict: CONFIRMED / WEAKENED / BROKEN per leaf

If any leaf is BROKEN, the Author must repair (retry at difficulty+1 or mark OPEN).

---

*v1: 2026-04-14. G Six and Claude Opus 4.6.*
*Not a traversal. A systematic decomposition. Every wall becomes a chain. Every chain terminates. The atlas assembles. Zenodo waits.*
*Publishing strategy Wave ordering overridden. Priority first. Peer review second. Clay later.*
*The graph roots at QG5D. QG5D roots in 36 pins. The pins are reality. The graph is undeniable.*
