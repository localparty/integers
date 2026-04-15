# X-RAY RUN — Invocation File

*Invoke the PAC on the X-Ray bundle. Produces 25 X-RAY.md files + atlas. Annotation mode. Fixed vocabulary. Citations mandatory.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## Invocation Style A — Manual PAC session (paste into Claude)

Use when G (or anyone) opens a fresh Claude session and pastes the invocation to bootstrap the PAC. This is the classic "read your instructions from X" form used by all PCA briefs.

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

the current run brief (X-RAY DELTA) is
strategy/x-ray/x-ray-brief.md

the canonical template for each vertex X-RAY.md is
strategy/x-ray/x-ray-template.md

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see x-ray-brief.md §DELTA 7 for Zenodo-first strategy.)

the run output directory is
strategy/x-ray/pac-output/runs/run-NN/

the ring is the 25 live PROOF-CHAIN.md files (see x-ray/README.md
mapping section for path list).

X-RAY.md files are WRITTEN to
strategy/x-ray/proof-chain/<vertex>/X-RAY.md

the vocabulary is FIXED — no invention.

MODE: annotation (new mode, distinct from execute/draft/final).
      See x-ray-brief.md §DELTA 8.

Run plan:
- visit each of 25 vertices in priority order (see README)
- produce one X-RAY.md per vertex following the 10-section template
- every Physics block fully filled with citations
- critic attacks every assignment; arbiter decides
- cross-cut edges accumulated across the run
- atlas emitted at run end ONLY IF all 25 complete

Partial runs are fine — do what you can, log progress, resume next run.

Begin.
```

---

## Expected output layout

After a run:

```
strategy/x-ray/pac-output/runs/run-NN/
├── blackboard.md                    (master scratchpad for this run)
├── commit-memo.md                   (what this run accomplished)
├── cross-cut-edges.md               (accumulated cross-cut edges)
└── vertices/
    ├── ym/
    │   ├── x-ray-draft.md           (author's annotations)
    │   ├── critic-attacks.md        (critic's alternative assignments)
    │   └── arbiter-decisions.md     (arbiter's final picks + rejected footnotes)
    ├── rh/
    │   └── ... (same structure)
    └── ... (up to 25 vertices)

strategy/x-ray/proof-chain/
├── INDEX.md                         (append entries as vertices complete)
├── ym/X-RAY.md                      (written when ym run completes)
├── rh/X-RAY.md
└── ... (up to 25)

strategy/x-ray/pac-output/atlas/     (emitted ONLY when all 25 complete)
├── face-histogram.md
├── projection-histogram.md
├── cross-cut-graph.md
└── gazetteer.md
```

---

## Checks before invoking

- [ ] `strategy/x-ray/x-ray-template.md` exists and is current
- [ ] `strategy/x-ray/x-ray-brief.md` exists and is current
- [ ] `strategy/x-ray/proof-chain/` directory exists (PAC creates per-vertex subdirs)
- [ ] `strategy/x-ray/pac-output/runs/` directory exists (PAC creates run-NN subdir)
- [ ] The 25 live PROOF-CHAIN.md files exist at their canonical paths (see README mapping)
- [ ] Sibling bundles exist for cascading refinements: `strategy/decomposition/` and `strategy/ccm-verification/`

---

## First invocation: what to expect

The first X-Ray run will NOT complete all 25 vertices. Expect to x-ray Priority 1 (5-6 Clay-weight vertices) in the first run (~4-6 hours of PAC time). Priority 2 (face-canonical vertices) in the second run. Etc.

At the end of each partial run, the commit-memo records:
- Which vertices were x-rayed
- Which vertices are still pending
- Which NEEDS-CITATION flags were raised
- Cross-cut edges accumulated so far (merged with prior runs)

The atlas is emitted ONLY when all 25 X-RAY.md files exist and pass validation. Partial runs skip atlas emission.

---

## Resuming from a prior partial run

To continue x-raying where a prior run stopped:

1. Read `pac-output/runs/run-NN/commit-memo.md` (the most recent run)
2. Identify the "still pending" list
3. Invoke with a new `run-(NN+1)/` directory
4. The PAC picks up from the next pending vertex in priority order
5. Cross-cut edges from prior runs MERGE with new edges

---

## Invocation Style B — Agent-tool / sub-agent spawning

Used when claude-code (or another orchestrator) fires a sub-agent to x-ray ONE specific vertex. Self-contained — the sub-agent has no context from the parent conversation. Parameterize by replacing `<VERTEX>`, `<PAPER-NN-SHORT>`, `<RUN-NN>`, `<FACE-HINT>`, `<PROJ-HINT>`, `<PATTERN-HINT>`, `<WALL-HINT>`, `<CROSS-CUT-HINT>`.

```
You are the PAC (Proof-Chain Adversarial) operator running on the X-RAY bundle. This is <RUN-NN>, a PILOT to validate the X-Ray discipline. We're x-raying <VERTEX>.

## GOAL

Produce ONE file: `/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md` following the canonical 10-section template. This document is the geometric x-ray of the <VERTEX> proof chain: every layer annotated with face / projection / pattern / invariant / geometric interpretation / cross-cuts. ASCII diagrams are the document's most important artifact.

## READ FIRST (in order)

1. `/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/README.md` — bundle overview
2. `/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/x-ray-brief.md` — the operational brief with 8 DELTAs
3. `/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/x-ray-template.md` — canonical 10-section template (YOUR NORTH STAR — follow it exactly)
4. `/Users/gsix/quantum-geometry-in-5d-latex/<PAPER-NN-SHORT>/PROOF-CHAIN.md` — the live <VERTEX> proof chain. This is what you x-ray.

## READ AS NEEDED

- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper60-geometry-of-circle/` — defines the 10 e-circle faces. Cite sections when assigning faces.
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper61-projections-5d/sections/` — defines the 6 projections P_A..P_O. Cite sections when assigning projections.
- `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/PROOF-CHAIN.md` — QG5D hub, for cross-cut detection and branch-A/B/C/D/E assignment.
- `/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/` — base ORA instructions and patterns P1–P5.
- `/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/` — chain extensions. Capacitor at 09-capacitor-correspondence-table-v1.md.
- `/Users/gsix/quantum-geometry-in-5d-latex/strategy/decomposition/proof-chain/<VERTEX>/` — if <VERTEX> has been decomposed already, reference it in §9 Cascading Refinements.

## WRITE (required files)

Primary deliverable:
- `/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/proof-chain/<VERTEX>/X-RAY.md`

Run transcript files (at `/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/pac-output/runs/<RUN-NN>/`):
- `blackboard.md` — your scratchpad (vertex choices, decisions, open questions)
- `vertices/<VERTEX>/x-ray-draft.md` — author's first-pass annotations
- `vertices/<VERTEX>/critic-attacks.md` — per-layer alternative assignments the critic proposed
- `vertices/<VERTEX>/arbiter-decisions.md` — final picks + one-line rejected-alternative footnotes
- `cross-cut-edges.md` — edges to other vertices (one per line) for atlas assembly
- `commit-memo.md` — run summary: vertices completed, NEEDS-CITATION flags, pending work

Index update:
- Append a row for <VERTEX> to `/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/proof-chain/INDEX.md` (create if it doesn't exist; header: `| vertex | primary face | primary projection | primary pattern | #layers | #cross-cuts |`).

## HARD DISCIPLINE (from x-ray-brief.md)

1. **Fixed vocabulary only.** The template enumerates 10 faces, 6 projections, 5 patterns, 16 invariants. Pick from these lists. Do NOT invent. If a layer genuinely needs a new category, flag `NEW-CATEGORY-REQUEST` in the blackboard and proceed with your best-fit from the existing lists.

2. **Every assignment cited.** Face → `(paper60 §N — <reason>)`. Projection → `(paper61 §M — <reason>)`. Pattern → `(ORA v8 §X — <reason>)`. If you can't cite, flag `NEEDS-CITATION`.

3. **Critic attacks every field, every layer.** For each layer's Physics block (face, projection, pattern, invariant, interpretation), the critic proposes AT LEAST ONE competing assignment with a reason. Record in `critic-attacks.md`. The arbiter picks the stronger fit AND records the rejected alternative as a one-line footnote in the final X-RAY.md.

4. **ASCII diagrams are load-bearing.** The template §2 requires THREE mandatory diagrams:
   - **Diagram A — Main proof-chain tree** (20–50 lines). Every layer as a node with its face/projection/pattern triplet on an indented line. Use box-drawing characters (├ │ └ ─ ▼).
   - **Diagram B — Projection fan-out.** Center box with the vertex's top claim; six labeled arrows to P_A, P_B, P_C, P_D, P_E, P_O. Under each: the vertex's shadow or `(forgotten)`. The primary projection arrow uses ═══ doubled line.
   - **Diagram C — Face position on the e-circle.** 10-face compass from paper60 with ● at primary face and ○ at secondary faces.
   Additional ASCII required: §5 face histogram with █ bars; §6 projection histogram with █ bars; §7 cross-cut graph with ═══ (invariant cross-cuts) and ─── (face-only cross-cuts). No `+--+` substitutes — use real box-drawing characters.

5. **All 10 template sections populated.** Missing section = incomplete = returned by arbiter. Sections: Header, ASCII Diagrams (2a/2b/2c), Layer-by-Layer, Branch Map (if applicable), Face Histogram, Projection Histogram, Cross-Cut Map, Current Walls, Cascading Refinements, Known Gaps.

6. **Annotation mode, not decomposition mode.** You READ `<PAPER-NN-SHORT>/PROOF-CHAIN.md` but you DO NOT MODIFY it. All output goes to `strategy/x-ray/` paths only. No BLOCKED-DECOMPOSED, no CONSTRUCT, no link-closing. This is pure geometric annotation.

## NOTES ON <VERTEX> SPECIFICALLY

- Primary face HINT: <FACE-HINT> (verify against paper60; the critic will attack if you pick the hint without evidence)
- Primary projection HINT: <PROJ-HINT>
- Primary pattern HINT: <PATTERN-HINT>
- Known walls: <WALL-HINT>
- Cross-cuts to look for: <CROSS-CUT-HINT>
- If the vertex has many nodes and you can't annotate all in one run, it's OK to produce a PARTIAL X-RAY.md with the first ~10 layers complete and a NEEDS-CONTINUATION note. The discipline matters more than completeness for this pilot.

## SUCCESS CRITERIA

- `X-RAY.md` written with all 10 sections, every section non-empty
- At least 3 ASCII diagrams present, legible, using proper box-drawing characters
- Every Physics block has 5 fields filled with citations
- At least one critic attack recorded per layer
- At least one cross-cut edge identified
- Blackboard and commit memo summarize work

If you hit a blocker (cannot find paper60/paper61, ambiguous layer, etc.), log it in the blackboard and DO YOUR BEST with what you have — don't block on perfection. This is the pilot; the next run iterates.

Begin by reading the 4 mandatory files in order, then the <VERTEX> PROOF-CHAIN.md, then compose a plan in the blackboard, then execute.
```

### Parameter table for Priority 1 vertices

| `<VERTEX>` | `<PAPER-NN-SHORT>` | `<FACE-HINT>` | `<PROJ-HINT>` | `<PATTERN-HINT>` | `<WALL-HINT>` | `<CROSS-CUT-HINT>` |
|---|---|---|---|---|---|---|
| `ym` | `paper08-yang-mills` | CURVATURE (secondary SYMMETRY, RESONANCE) | P_D (secondary P_O, P_A for Wilson loops) | P4 for spectral-gap layers; P2 for holonomy; P5 for KK sums | H4 (bypassed via Balaban RG + gradient flow, 2026-04-13) | ym ↔ pvnp (spectral gap); ym ↔ rh (zero distribution); ym ↔ h12 (CBB foundations) |
| `rh` | `paper13-rh` | DYNAMICS (secondary RESONANCE) | P_D (secondary P_O) | P4 (CBB), P2 (zeros on critical line as holonomy phase) | CCM-conditional layers | rh ↔ cramer (gap distribution); rh ↔ goldbach (arithmetic); rh ↔ bgs (spectral statistics) |
| `bsd` | `paper26-bsd` | AMPLITUDE (secondary ARITHMETIC) | P_D, P_E (L-value pins) | P3 (scale-setting via KK), P4 | None open | bsd ↔ rh (L-values); bsd ↔ h12 (class fields) |
| `pvnp` | `paper28-pvnp` | SYMMETRY (secondary RESONANCE) | P_D (operational core) | P4 (Popa rigidity), P1 | PvNP L5 backward (non-full → Taylor polymorphism) | pvnp ↔ ym (spectral gap); pvnp ↔ vp-vs-vnp |
| `hodge` | `paper29-hodge` | TOPOLOGY (secondary SYMMETRY) | P_D, P_B (motivic) | P4, P1 | Hodge L3-L4 (motivic BC extension) | hodge ↔ baum-connes (motivic extension) |
| `baum-connes` | `paper31-baum-connes` | SYMMETRY (secondary CURVATURE) | P_D | P4 | None critical | baum-connes ↔ hodge (motivic); baum-connes ↔ ym (operator-algebraic) |
| `ns` | `paper30-navier-stokes` | DYNAMICS (secondary CURVATURE) | P_D, P_A (incompressible flow) | P4, P3 | None open | ns ↔ turbulence; ns ↔ ym (operator-algebraic) |

### Parameter table for Priority 2 (face-canonical vertices)

| `<VERTEX>` | `<PAPER-NN-SHORT>` | `<FACE-HINT>` | `<PROJ-HINT>` | `<PATTERN-HINT>` | `<CROSS-CUT-HINT>` |
|---|---|---|---|---|---|
| `lehmer` | `paper42-lehmer` | TOPOLOGY | P_D | P4 (Route A ITPFI) | lehmer ↔ cramer (shared ITPFI); lehmer ↔ collatz |
| `cramer` | `paper43-cramer` | DYNAMICS | P_D | P4 (Mertens constant $2e^{-\gamma}$ from ITPFI) | cramer ↔ rh; cramer ↔ lehmer; cramer ↔ bgs |
| `collatz` | `paper41-collatz` | HARMONICS | P_D | P4, P2 | collatz ↔ lehmer (orbit structure) |
| `sato-tate` | `paper44-sato-tate` | MEASURE | P_D | P4 (equidistribution) | sato-tate ↔ katz-sarnak (symmetry) |
| `lindelof` | `paper45-lindelof` | AMPLITUDE | P_D, P_E | P3 (subconvexity exponent) | lindelof ↔ rh; lindelof ↔ bsd |
| `katz-sarnak` | `paper46-katz-sarnak` | SYMMETRY | P_D | P4 | katz-sarnak ↔ sato-tate; katz-sarnak ↔ bgs |

Remaining 12 vertices get analogous hint rows (goldbach, twin-primes, abc, opn, schanuel, grh, h12, turbulence, bgs, vp-vs-vnp, hilbert-6, qg5d — qg5d LAST because it indexes all others).

---

*End of run file. Two invocation styles documented: Style A for manual PAC sessions, Style B for sub-agent spawning. The geometry awaits.*

*G Six and Claude Opus 4.6. April 14, 2026.*
