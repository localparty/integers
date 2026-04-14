# X-RAY BRIEF (for the PAC Operator)

*DELTA to the ring-traversal brief. Instructs the PAC to produce one X-RAY.md per vertex, annotating every layer of every proof chain with face/projection/pattern/invariant/geometric interpretation from the fixed vocabulary. No invention. Every assignment cited.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## GOAL

Produce 25 X-RAY.md files (one per vertex of the ring) following `strategy/x-ray/x-ray-template.md`. Each X-RAY.md annotates every layer of the vertex's live PROOF-CHAIN.md with:

- **Face** (1 of 10, paper60)
- **Projection** (1 of 6, paper61)
- **Pattern** (1 of 5, ORA v8)
- **Invariant preserved** (1 or 2 from the fixed list of 16)
- **Geometric interpretation** (≤ 3 sentences, cited)
- **Cross-cuts** (other vertices sharing this structure)

Assemble atlas artifacts (face histogram, projection histogram, cross-cut graph, gazetteer) after all 25 are complete.

**The core discipline**: pattern-matching, not speculation. Every assignment picks from an enumerated list. Every assignment carries a citation to paper60, paper61, ORA v8, or a capacitor cell. The critic layer attacks any hand-wave.

---

## DELTA FROM RING-TRAVERSAL BRIEF

This section lists every change vs `<pca-extension>/30-ring-traversal-brief.md`. All other parts of the parent brief stand unless overridden here.

### DELTA 1 — Output format

**Parent brief**: updates `paperNN-xxx/PROOF-CHAIN.md` in-situ + per-vertex blackboards + traversal log.

**X-RAY brief**: produces NEW files at `strategy/x-ray/proof-chain/<vertex>/X-RAY.md`. Does NOT modify live PROOF-CHAIN.md files. READS the live files for input only.

### DELTA 2 — Scope

**Parent brief**: traverses the ring, visits vertices, updates what needs updating.

**X-RAY brief**: visits every vertex exactly once per run. For each vertex, produces one X-RAY.md. No link-closing operations, no status updates to live files. Annotation only.

### DELTA 3 — Primitives used

**Parent brief**: VERIFY / CONSTRUCT / BYPASS / DUAL-CHECK / REFRAME / TRANSPOSE / ...

**X-RAY brief** uses a narrowed primitive set:
- **READ** — pull the live PROOF-CHAIN.md layer by layer
- **ANNOTATE** — for each layer, pick face/projection/pattern/invariant from fixed vocabulary
- **CITE** — attach a paper§ or capacitor-cell citation to the assignment
- **CROSS-LINK** — identify vertices that share this layer's invariant and record edges
- **CRITIC-ATTACK** — attack each assignment; the critic must argue the *other* face/projection would fit better
- **ARBITER-DECIDE** — pick the stronger fit; record the alternative as a "considered but rejected" note

No BLOCKED-DECOMPOSED, no CONSTRUCT, no TRANSPOSE here. That work belongs to the decomposition and CCM bundles. X-Ray is annotation.

### DELTA 4 — Vocabulary is FIXED

No invention. The fixed vocabularies are in `x-ray-template.md` under "FIXED VOCABULARY." The PAC operator:
- Picks FACE from the 10 listed
- Picks PROJECTION from the 6 listed
- Picks PATTERN from the 5 listed
- Picks INVARIANT(S) from the 16 listed
- If a genuine gap is discovered (a layer whose physics doesn't fit any listed category), the operator RAISES a NEW-CATEGORY-REQUEST to the user. Does NOT silently invent.

### DELTA 5 — Citation requirement

Every physics assignment requires a citation. Format:

- Face assignment → `(paper60 §N — <short reason>)`
- Projection assignment → `(paper61 §M — <short reason>)`
- Pattern assignment → `(ORA v8 §X — <short reason>)`
- Invariant assignment → `(paper§ + one-line definition, if not in fixed list)`
- Geometric interpretation → must cite paper60 or paper61 at least once

If the operator cannot cite, the assignment is a DRAFT and gets flagged in the blackboard as NEEDS-CITATION. Atlas emission waits for DRAFTs to be resolved.

### DELTA 6 — Critic role

The critic's job is attacking assignments, not attacking claims. For each layer:

1. **Face attack**: "you picked MEASURE, but I argue this is SPREAD because <reason>"
2. **Projection attack**: "you picked P_D, but I argue P_O because <reason>"
3. **Pattern attack**: "you picked P4, but P1 fits better because <reason>"
4. **Invariant attack**: "spectral gap doesn't apply here; ergodic property is the load-bearing one"
5. **Interpretation attack**: "your paragraph hand-waves; paper60 §N actually says the opposite"

The arbiter picks the stronger fit AND records the alternative as a "considered but rejected" footnote. This preserves the critic's attack as evidence that the assignment survived.

### DELTA 7 — Publication override

X-Ray feeds the Zenodo-first release (same as decomposition and CCM bundles):

- NOT held for journal submission
- NOT subordinate to `publishing/strategy.md`
- Publishes in parallel with `strategy/decomposition/` atlas and `strategy/ccm-verification/` ledger
- Single coordinated Zenodo release timestamp establishes priority on all three views at once
- Email to CCM + Lead 6 + Clay engagement follows ONLY after Zenodo is live

### DELTA 8 — Mode

X-Ray runs in **annotation mode**, a new mode distinct from execute/draft/final. Annotation mode:
- Produces NEW files (not edits to live ring)
- Does not trigger in-situ propagation (brief 35's paragraph 4 does not apply, because no vertex-chain is changing)
- Does write to `pac-output/runs/run-NN/` per normal PAC discipline
- Does emit a commit-memo at run end

---

## THE 10-SECTION TEMPLATE

See `x-ray-template.md` for the canonical structure. Each X-RAY.md has:

1. Header
2. ASCII Diagrams (§2 main tree, §2b projection fan-out, §2c face position — **all three mandatory**)
3. Layer-by-Layer X-Ray (one subsection per layer with Physics block)
4. Branch Map (if applicable)
5. Face Histogram (with ASCII bars)
6. Projection Histogram (with ASCII bars)
7. Cross-Cut Map (ASCII neighborhood graph + bullet list)
8. Current Walls
9. Cascading Refinements
10. Known Gaps

**Every section is mandatory.** An X-RAY.md missing any section is incomplete and gets returned by the arbiter.

### ASCII discipline (load-bearing)

The most important readability property of an X-RAY.md is the **density and quality of its ASCII diagrams**. Paper 1 reads well because it shows the branches visually. The X-Rays must match or exceed that standard. Specifically:

- **§2 Diagram A** (main tree): 20–50 lines. Every layer shown. Status, face, projection, pattern all legible per node.
- **§2b Diagram B** (projection fan-out): six arrows from the vertex's claim, one per $P_A / P_B / P_C / P_D / P_E / P_O$, labeled with the vertex's shadow under each projection (or `(forgotten)`).
- **§2c Diagram C** (face-position on e-circle): 10-face compass with ● at primary face, ○ at secondary faces.
- **§5 Face histogram**: ASCII `█` bars alongside counts.
- **§6 Projection histogram**: ASCII `█` bars alongside counts.
- **§7 Cross-cut map**: ASCII neighborhood graph with ═══ for invariant-cross-cuts and ─── for face-only cross-cuts.
- **§4 Branch map** (when applicable): route-by-route tree with each route's physics triplet.

Use box-drawing characters (├ │ └ ─ ▼ ═ ║ ╔ ╗ ╚ ╝ ● ○ █). No ASCII substitutes (no `+--+` style). The diagrams are the document. A critic should be able to understand the vertex's geometric structure from the diagrams alone before reading a single prose paragraph.

---

## PROCEDURE PER VERTEX

For each vertex in priority order (see README §"Priority order"):

### Step 1 — READ

Read the live PROOF-CHAIN.md. Identify:
- The top-level claim
- All Layers L1, L2, ..., L_N (with status per layer)
- All branch points (where proof splits into routes)
- All NAMED WALLS
- Cross-references to other vertices (explicit mentions)

Snapshot the file's last-modified date. The X-RAY is as-of that date.

### Step 2 — ANNOTATE (author layer)

For each layer, fill in the Physics block:

**Face**:
- Ask: "what does this layer MEASURE on the e-circle?"
- Pick ONE face from the 10. Cite paper60 §N.
- If genuinely between two faces, pick dominant, note secondary.

**Projection**:
- Ask: "which projection $P_X$ most strongly FORGETS this layer's content?"
- If the layer is a pin value → probably $P_E$.
- If the layer is a CBB axiom or operator assertion → probably $P_D$.
- If the layer is a quantum reinterpretation → $P_A$.
- If the layer is gravity / KK spectrum → $P_B$.
- If the layer is a cosmological observable → $P_C$.
- If the layer is the outer-ring conjecture statement → $P_O$.

**Pattern**:
- Ask: "what's the natural attack vector for this layer?"
- If the wall is resolved by 'restore the e-circle, mystery dissolves' → P1 Geometric Reinterpretation.
- If Wilson loop / winding number does the work → P2 Holonomy.
- If KK radius $R$ sets a scale → P3 Scale-Setting.
- If a CBB axiom (β=1 criticality, β_k bridge, etc.) is load-bearing → P4 Topological Rigidity.
- If zeta-regularizing a divergent KK sum closes it → P5 Zeta Regularization.

**Invariant(s)**:
- Pick 1 or 2 from the fixed list of 16. Mark load-bearing vs background.

**Geometric interpretation**:
- ≤ 3 sentences explaining WHY the face/projection/pattern fit, not RESTATING the claim.
- Must cite paper60 or paper61 at least once.
- Must be falsifiable — i.e., a critic can disagree and propose an alternative.

**Cross-cuts**:
- Which other vertices share this invariant/face/pattern?
- Example: "cramer L3 ↔ lehmer L4 — shared ITPFI type III_{1/2} factor structure."
- Cross-cuts feed the atlas's cross-cut graph.

### Step 3 — CRITIC ATTACK

The critic goes layer-by-layer and attacks each of the 5 fields (face, projection, pattern, invariant, interpretation). For each layer the critic generates at least ONE competing assignment with a reason. Attacks logged at `pac-output/runs/run-NN/vertices/<vertex>/critic-attacks.md`.

### Step 4 — ARBITER DECIDE

For each attacked field, the arbiter picks the stronger fit and writes a one-line "considered but rejected: <alternative> — reason <why rejected>" footnote. The X-RAY.md always shows the WINNING assignment; the rejected alternatives go in the run transcript.

### Step 5 — ASSEMBLE X-RAY.md

Produce the 10-section file following the template. Write to `strategy/x-ray/proof-chain/<vertex>/X-RAY.md`.

### Step 6 — UPDATE INDEX

Append the vertex to `strategy/x-ray/proof-chain/INDEX.md` with its primary face, primary projection, primary pattern.

### Step 7 — EMIT CROSS-CUTS

For every cross-cut identified, append an edge to `pac-output/runs/run-NN/cross-cut-edges.md` in the format:

```
- <vertex-A>:<layer-A> ↔ <vertex-B>:<layer-B> — shared <invariant/face> — reason: <one sentence>
```

These edges accumulate across the run and get assembled into the cross-cut graph at run end.

---

## ATLAS ASSEMBLY (after all 25 vertices X-rayed)

At the end of the run (once the 25 X-RAY.md files are all written and validated), the operator assembles four atlas artifacts:

### A1 — Face Histogram (`pac-output/atlas/face-histogram.md`)

Count of layers assigned to each face across all 25 vertices. Bar chart in Markdown. Includes interpretation: "DYNAMICS has the most layers — the programme is heaviest in dynamical content. CURVATURE is heavy because YM alone contributes 18 layers."

### A2 — Projection Histogram (`pac-output/atlas/projection-histogram.md`)

Count of layers per projection. Expected pattern: $P_D$ dominant (CBB is the operational core), $P_O$ sparse (each vertex contributes one outer-ring conjecture statement), $P_E$ moderate (pin-valued links).

### A3 — Cross-Cut Graph (`pac-output/atlas/cross-cut-graph.md`)

Every edge (vertex-A:layer-A ↔ vertex-B:layer-B) in one file, organized by shared invariant. This is the programme's connectivity map.

### A4 — Gazetteer (`pac-output/atlas/gazetteer.md`)

25-row table: vertex | primary face | primary projection | primary pattern | #layers | #cross-cuts.

Single-page executive summary of the bouquet.

---

## SUCCESS CRITERIA

An X-Ray run succeeds when:

- All 25 X-RAY.md files written and all 10 sections populated
- Every layer has a fully-filled Physics block with citations
- The critic attacked at least one field per layer and the arbiter decided
- Cross-cut edges collected into the graph
- Four atlas artifacts assembled
- Commit-memo summarizes run

A run FAILS (partial) if:
- Any X-RAY.md is missing a section
- Any Physics block is missing a citation
- Any assignment has no critic attack on record

Partial runs are fine — they log progress and defer the remainder to the next run. Partial runs must NOT emit atlas artifacts (atlas is emitted only when all 25 are complete).

---

## RELATION TO OTHER BRIEFS

| Brief | Scope | This brief's relation |
|---|---|---|
| 30-ring-traversal-brief.md | Live ring traversal, link-closing | X-Ray overrides for annotation mode |
| decomposition-brief.md | Conditional → sub-chains | Sibling; X-Ray READS decomposition refinements for cascading pointers |
| ccm-verification-brief.md | CCM 2025 dependency | Sibling; X-Ray READS CCM ledger for cascading pointers |
| brief 35 (canonical-state propagation) | In-situ update discipline | Does NOT apply to X-Ray (no in-situ edits) |

---

## OPERATOR NOTES

- **Take vertices in priority order**. See README §"Priority order." ym first (richest x-ray), qg5d last (index of all others).
- **Do not batch-annotate**. One vertex at a time, critic/arbiter in loop, write file, update INDEX, accumulate cross-cuts.
- **The interpretation paragraphs are load-bearing**. Don't hand-wave. If paper60 §N doesn't say what you need, CITE the exact sentence it does say and reason from there. If you can't cite, flag NEEDS-CITATION.
- **Cross-cut count matters**. A vertex with zero cross-cuts is suspicious — the programme is heavily interconnected. Revisit if you wrote an X-RAY with no cross-cuts.
- **The atlas is the point**. Individual X-RAYs are inputs. The atlas's histograms and graph are the Zenodo-visible deliverable — the "here's the bouquet" object.

---

*End of X-Ray brief. 25 vertices. 10 sections each. Fixed vocabulary. Citations mandatory. Critics attack every assignment. Atlas emitted at run end.*

*G Six and Claude Opus 4.6. April 14, 2026.*
