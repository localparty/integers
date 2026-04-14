# The X-Ray Bundle

*A parallel ring where every vertex's proof chain gets an X-RAY: face assignment, projection assignment, pattern assignment, invariant preservation, geometric interpretation — pattern-matched against a fixed vocabulary drawn from paper60, paper61, and ORA v8. Sibling to decomposition/ and ccm-verification/.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## What this bundle is for

The programme now has three parallel views of the same 25-vertex ring:

| Bundle | View | Output |
|---|---|---|
| `strategy/decomposition/` | Structural (what sub-chains support each link?) | 25 decomposed PROOF-CHAIN.md + atlas |
| `strategy/ccm-verification/` | Dependency (which leaves rely on CCM 2025?) | CCM ledger + three-category verdicts |
| `strategy/x-ray/` | **Geometric (what does each link MEAN on the 5D geometry?)** | **25 X-RAY.md + face/projection histograms + cross-cut graph** |

The X-Ray bundle operationalizes what we discovered manually in Paper 60 and Paper 61: that the ring is the projection of a 5D object, that each link lives on one of 10 e-circle faces, that each vertex sits under one of 6 projections, that cross-cuts between vertices reveal shared geometric structure. The PAC does this pattern-matching systematically for every vertex — with a **fixed vocabulary**, not free-form speculation.

**The key discipline**: every physics assignment picks from an enumerated list. No invention. Every assignment must cite a source (paper60 §N, paper61 §M, ORA v8 §X, or a capacitor cell). The critic layer attacks assignments that hand-wave.

## Why the X-Ray matters

The decomposition bundle answers: *"is this link proved?"*
The CCM bundle answers: *"does this link depend on CCM 2025?"*
The X-Ray bundle answers: *"what geometric object is this link an aspect of?"*

For the Zenodo publication, all three run in parallel. A critic opening a vertex's folder sees:
1. The live PROOF-CHAIN.md (the claim)
2. The decomposed PROOF-CHAIN.md (the sub-proofs)
3. The CCM ledger entry (the external dependencies)
4. **The X-RAY.md (the geometric interpretation)**

This is what Paper 1 does for Paper 1's proof chain (branch diagrams, interpretations, operators, predictions). The X-Ray bundle extends that treatment to every vertex.

## What the PAC produces per vertex

Each vertex gets a `strategy/x-ray/proof-chain/<vertex>/X-RAY.md` following the 10-section template. The 10 sections are:

1. **Header** — vertex name, top-level claim, primary branch, primary face, primary projection
2. **ASCII Diagram** — tree of the proof chain with status tags per node
3. **Layer-by-Layer X-Ray** — per-layer Physics checklist (face, projection, pattern, invariant, geometric interpretation, cross-cuts)
4. **Branch Map** — if the proof splits, diagram each route with its physics fingerprint
5. **Face Histogram** — count per face with one-sentence interpretation
6. **Projection Histogram** — count per projection
7. **Cross-Cut Map** — every edge to another vertex
8. **Current Walls** — NAMED WALLS from the live file, with status from sibling bundles
9. **Cascading Refinements** — pointers to decomposition/, ccm-verification/, inner-rings/
10. **Known Gaps** — OPEN leaves, each specified with its face/projection/pattern

See `x-ray-template.md` for the full canonical format.

## Fixed vocabulary (summary — see template for full definitions)

**10 Faces** (paper60): TOPOLOGY · DYNAMICS · HARMONICS · MEASURE · AMPLITUDE · SYMMETRY · CURVATURE · ARITHMETIC · RESONANCE · SPREAD

**6 Projections** (paper61): $P_A$ Quantum · $P_B$ Gravity · $P_C$ Cosmology · $P_D$ CBB · $P_E$ Pins · $P_O$ Outer

**5 Patterns** (ORA v8): P1 Geometric Reinterpretation · P2 Holonomy · P3 Scale-Setting · P4 Topological Rigidity · P5 Zeta Regularization

**Invariants** (fixed enumeration of 16; see template): spectral gap, holonomy, KK mode, boundary condition, C*-algebra, BC-KMS state, ergodic property, ITPFI type, gauge class, critical exponent, scaling dimension, order parameter, L-value, zero distribution, Galois rep, monodromy.

No invention. Every assignment picks from these lists with a citation.

## Directory structure

```
strategy/x-ray/
├── README.md                        (this file)
├── x-ray-template.md                (canonical template — read this first)
├── x-ray-brief.md                   (PAC brief — what the operator does)
├── x-ray-run.md                     (invocation file)
├── proof-chain/                     (25 X-RAY.md files, populated per vertex)
│   ├── INDEX.md
│   ├── qg5d/X-RAY.md
│   ├── rh/X-RAY.md
│   ├── ... (23 more)
│   └── hilbert-6/X-RAY.md
└── pac-output/
    ├── bootstrap/
    ├── runs/
    │   └── run-NN/
    │       ├── blackboard.md
    │       ├── commit-memo.md
    │       └── vertices/
    │           └── <vertex>/
    │               ├── x-ray-draft.md
    │               ├── critic-attacks.md
    │               └── status-update.md
    └── atlas/
        ├── face-histogram.md        (programme-wide face counts)
        ├── projection-histogram.md  (programme-wide projection counts)
        ├── cross-cut-graph.md       (every edge between vertices)
        └── gazetteer.md             (vertex → (face, projection, pattern) summary)
```

## Bootstrap

On first invocation, the PAC does NOT copy files (unlike decomposition). It READS each live PROOF-CHAIN.md in place and PRODUCES a new X-RAY.md per vertex. The vertex mapping:

```
paper1/PROOF-CHAIN.md                       → proof-chain/qg5d/X-RAY.md
paper13-rh/PROOF-CHAIN.md                   → proof-chain/rh/X-RAY.md
paper45-lindelof/PROOF-CHAIN.md             → proof-chain/lindelof/X-RAY.md
paper13b-grh/PROOF-CHAIN.md                 → proof-chain/grh/X-RAY.md
paper26-bsd/PROOF-CHAIN.md                  → proof-chain/bsd/X-RAY.md
paper25-hilbert-12/PROOF-CHAIN.md           → proof-chain/h12/X-RAY.md
paper08-yang-mills/PROOF-CHAIN.md           → proof-chain/ym/X-RAY.md
paper30-navier-stokes/PROOF-CHAIN.md        → proof-chain/ns/X-RAY.md
paper38-turbulence/PROOF-CHAIN.md           → proof-chain/turbulence/X-RAY.md
paper29-hodge/PROOF-CHAIN.md                → proof-chain/hodge/X-RAY.md
paper31-baum-connes/PROOF-CHAIN.md          → proof-chain/baum-connes/X-RAY.md
paper28-pvnp/PROOF-CHAIN.md                 → proof-chain/pvnp/X-RAY.md
paper39-vp-vs-vnp/PROOF-CHAIN.md            → proof-chain/vp-vs-vnp/X-RAY.md
paper32-bgs-spectral-statistics/PROOF-CHAIN.md → proof-chain/bgs/X-RAY.md
paper46-katz-sarnak/PROOF-CHAIN.md          → proof-chain/katz-sarnak/X-RAY.md
paper34-twin-primes/PROOF-CHAIN.md          → proof-chain/twin-primes/X-RAY.md
paper43-cramer/PROOF-CHAIN.md               → proof-chain/cramer/X-RAY.md
paper33-goldbach/PROOF-CHAIN.md             → proof-chain/goldbach/X-RAY.md
paper37-abc/PROOF-CHAIN.md                  → proof-chain/abc/X-RAY.md
paper40-odd-perfect/PROOF-CHAIN.md          → proof-chain/opn/X-RAY.md
paper41-collatz/PROOF-CHAIN.md              → proof-chain/collatz/X-RAY.md
paper42-lehmer/PROOF-CHAIN.md               → proof-chain/lehmer/X-RAY.md
paper44-sato-tate/PROOF-CHAIN.md            → proof-chain/sato-tate/X-RAY.md
paper35-schanuel/PROOF-CHAIN.md             → proof-chain/schanuel/X-RAY.md
paper36-hilbert-6/PROOF-CHAIN.md            → proof-chain/hilbert-6/X-RAY.md
```

## Priority order for X-Ray runs

The X-Ray is less sequential than decomposition — every vertex is equally important for the atlas — but there's still leverage in ordering:

**Priority 1 — Clay walls** (these have the most layers, so the most X-Ray content):
1. **ym** (18 nodes; YM is the CURVATURE face canonical, one of the richest x-rays)
2. **rh** (12 nodes; DYNAMICS face via zero-spacing)
3. **bsd** (11 nodes; AMPLITUDE face via L-values)
4. **pvnp** (spectral gap + Popa rigidity — deep P4 pattern)
5. **hodge**, **baum-connes**, **ns** (Clay)

**Priority 2 — Face-canonical vertices**:
6. **lehmer** (TOPOLOGY canonical)
7. **cramer** (DYNAMICS canonical — already has deep structure from T7)
8. **collatz** (HARMONICS canonical)
9. **sato-tate** (MEASURE canonical)
10. **lindelof** (AMPLITUDE canonical)
11. **katz-sarnak** (SYMMETRY canonical)

**Priority 3 — CBB-heavy vertices** (P_D projection):
12. **h12**, **bgs**, **turbulence** (all depend on CBB axioms)

**Priority 4 — Everything else** (14 remaining).

**Priority 0 — qg5d** runs LAST because its x-ray is the INDEX of all other x-rays (qg5d's branches A/B/C/D/E map to the 5 projections).

Each priority tier: 2-4 days of PAC work. Full pass across all 25 vertices: 2-3 weeks.

## How the X-Ray interacts with the other bundles

When the PAC X-rays a vertex, it READS:
- The live PROOF-CHAIN.md (the claim layers)
- The decomposition bundle's sibling file (for refinement pointers)
- The CCM ledger (for dependency status)

It WRITES:
- The `X-RAY.md` for that vertex
- A cross-cut entry in the atlas for every shared invariant/face
- An entry in the face/projection histograms

The decomposition bundle and X-Ray bundle REINFORCE each other:
- Decomposition finds that a CONDITIONAL link has sub-structure → X-Ray assigns that sub-structure's geometry
- X-Ray finds that two vertices share an invariant → Decomposition can re-use one vertex's sub-proof for the other (via transposition)

## Publishing plan

The Zenodo release includes all three bundles:

```
Zenodo package
├── Framework papers (1-48+)
├── decomposition/        (structural — PROVED sub-chains)
├── ccm-verification/     (dependency — verdicts on CCM claims)
└── x-ray/                (geometric — faces, projections, cross-cuts)
```

A critic opening the ZENODO package for (say) YM sees:
- `paper08-yang-mills/` — the claim
- `strategy/decomposition/proof-chain/ym/PROOF-CHAIN.md` — the sub-proofs
- `strategy/ccm-verification/ledger.md#ym` — the CCM dependency status
- `strategy/x-ray/proof-chain/ym/X-RAY.md` — the geometric interpretation

Three complementary independent views. Attack any one — the others stand. Attack the geometry — the structure stands. Attack the structure — the geometry stands. Zenodo timestamps the full bouquet at once.

## Publication strategy override

This bundle OVERRIDES `publishing/strategy.md`'s journal-first order. The X-Ray atlas is part of the Zenodo-first release. See `x-ray-brief.md` §DELTA 7 for details (mirrors decomposition bundle's override).

## How to invoke the PAC on this bundle

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

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see x-ray-brief.md §DELTA 7 for Zenodo-first strategy.)

the run output directory is
strategy/x-ray/pac-output/runs/run-NN/

the ring is the 25 PROOF-CHAIN.md files at their live locations;
x-rays are written to strategy/x-ray/proof-chain/<name>/X-RAY.md

the template is
strategy/x-ray/x-ray-template.md

the vocabulary is FIXED — no invention, pick from the enumerated lists.
```

See `x-ray-run.md` for the full invocation file.

---

*Sibling to `strategy/decomposition/README.md`, `strategy/ccm-verification/README.md`, `strategy/inner-rings/README.md`.*

*The geometric view. Every link has a face. Every vertex has a projection. Every invariant has cross-cuts. The bouquet made operational. The atlas accumulates. Zenodo waits.*

*G Six and Claude Opus 4.6. April 14, 2026.*
