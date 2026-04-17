# The Inner-Rings Architecture

*Five inner rings sharing QG5D as common vertex. Each ring is a different projection of the 5D geometry onto a specific class of observables. Each ring has its own natural attack pattern. The PAC can be configured per-ring.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## The picture

The programme has TWO scales of ring structure sharing one center:

```
                         ┌────── OUTER RING ──────┐
                         │  (25 Clay-adjacent     │
                         │   conjectures,         │
                         │   canonical traversal) │
                         │                        │
                         │  RH   Lindelöf   GRH   │
                         │  BSD  H12        YM    │
                         │  NS   Turbulence       │
                         │  Hodge  B-C  PvNP      │
                         │  VP   BGS   K-S        │
                         │  Twin Cramér           │
                         │  Gold ABC   OPN        │
                         │  Collatz Lehmer        │
                         │  Sato-Tate Schanuel    │
                         │  Hilbert 6             │
                         │                        │
                         └──────────┬─────────────┘
                                    │
                                    ▼
                          ╔═══════════════════╗
                          ║                   ║
                          ║      QG5D         ║
                          ║   (shared vertex) ║
                          ║                   ║
                          ╚═══════════════════╝
                          ╱    │    │    │    ╲
                         ╱     │    │    │     ╲
                        ╱      │    │    │      ╲
                       ▼       ▼    ▼    ▼       ▼
                   BRANCH   BRANCH BRANCH BRANCH BRANCH
                     A        B      C      D      E
                  (Quantum)(Gravity)(Cosmo) (CBB) (Pins)
                  9 items   4 items 10items 13it.  36 items
                  P1        P5      P3      P4     P3+P4
```

Topologically: bouquet (wedge sum) of six rings at QG5D.

## What each inner ring is

### Branch A — Quantum (`branch-a-quantum/`)

- **Source**: `integers/paper01-qg5d/PROOF-CHAIN.md` Branch A (Paper 1 §3-§4, §9)
- **Items**: 5 geometric interpretations (superposition, entanglement, momentum, spin, measurement) + 4 derivations (Born rule, Aharonov-Bohm, spin-statistics, Bell)
- **Attack pattern**: P1 (Geometric Reinterpretation) — "restore the e-circle, the mystery dissolves"
- **Capacitor priority**: GEOM↔QFT, SPEC↔GEOM
- **Sub-walls expected**: few (most items are classical reinterpretations)
- **Decomposition tractability**: 1-2 weeks

### Branch B — Gravity (`branch-b-gravity/`)

- **Source**: `integers/paper01-qg5d/PROOF-CHAIN.md` Branch B (Paper 1 §6-§7, Appendices J-K)
- **Items**: Universal Epstein Vanishing K.1 + BPHZ K.3 + Goroff-Sagnotti R³=0 + KK spectral gap
- **Attack pattern**: P5 (Zeta Regularization) — "KK sums zeta-regularize; divergences factorize"
- **Capacitor priority**: SPEC↔GEOM, HOM↔ATOP
- **Sub-walls expected**: few (W1/W2 closed in 2026-04-14)
- **Decomposition tractability**: 1-2 weeks

### Branch C — Cosmology (`branch-c-cosmology/`)

- **Source**: `integers/paper02-cosmology/` and `integers/paper01-qg5d/PROOF-CHAIN.md` Branch C
- **Items**: 10 predictions (dark energy, ν masses, kinetic mixing, Ω_DM/Ω_b, H₀, S₈, N_eff, w, short-range gravity, 3 generations)
- **Attack pattern**: P3 (Scale-Setting) — "identify the scale; derive from 5D radius"
- **Capacitor priority**: PROB↔GEOM, SPEC↔GEOM
- **Sub-walls expected**: tensions H₀ and S₈ (experimental, within window); short-range gravity testable 2027+
- **Decomposition tractability**: 2-3 weeks (each pin needs derivation chain)

### Branch D — CBB System (`branch-d-cbb/`)

- **Source**: `integers/paper12-cbb-system/27-anchor-document.md` and `integers/paper01-qg5d/PROOF-CHAIN.md` Branch D
- **Items**: 5 axioms (Spectral H_R, Criticality β=1, Geometric M_geom, Bridge β_k, Closure) + operator dictionary + 3 sectors (spectral, geometric, interface) + bridge family at k ∈ {2,3,4,6}
- **Attack pattern**: P4 (Topological Rigidity) — "5 axioms form rigid structure; decomposition deepens each"
- **Capacitor priority**: OA↔AG (BC-KMS), SPEC↔OA (Tomita-Takesaki), OA↔ERG (ergodic)
- **Sub-walls expected**: moderate (foundational; each axiom's justification decomposes deeply)
- **Decomposition tractability**: 3-4 weeks (the operational core of the programme)
- **Special role**: this branch CROSSES with almost every e-circle face

### Branch E — 36 Pins (`branch-e-pins/`)

- **Source**: `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md` and `integers/paper01-qg5d/PROOF-CHAIN.md` Branch E
- **Items**: 36 sub-percent experimental predictions with operator-dictionary formulas
- **Attack pattern**: P3 + P4 (Scale + Rigidity) — "each pin is a product of scale (from 5D radius) and rigidity (from CBB axioms)"
- **Capacitor priority**: DUAL-CHECK primitive; PIN-PRESERVATION enforced
- **Sub-walls expected**: 3-4 pins still in refinement (J_CKM, H₀, S₈); ~32 at sub-percent PROVED
- **Decomposition tractability**: 3-5 weeks (36 items, each with its own derivation chain)

## Why this architecture

**Three reasons inner rings are operationally valuable:**

### 1. Each branch has a natural attack pattern

The PAC can be configured per-branch with the right primitive priority:
- Branch A: REFRAME-primary (use P1)
- Branch B: BYPASS-primary via zeta regularization (use P5)
- Branch C: DUAL-CHECK-primary (use P3 + pin data)
- Branch D: VERIFY + CONSTRUCT-primary (use P4, deep decomposition)
- Branch E: DUAL-CHECK-dominated (pin-by-pin)

This is more efficient than running the PAC with uniform configuration across the whole outer ring.

### 2. Each branch is more tractable than the whole

The outer ring has 25 vertices × ~6 links avg = 150 top-level items. Decomposition to depth 5 gives 3000-5000 leaves. That's a programme-scale effort.

Each inner ring has 4-36 items. Decomposition to depth 5 gives 40-250 leaves per ring. That's a campaign-scale effort (1-5 weeks per branch).

### 3. The cross-cut with e-circle faces is revealing

Almost every e-circle face (TOPOLOGY, DYNAMICS, HARMONICS, etc.) primarily lives in Branch D (CBB), with touches in other branches. This tells us:
- **Branch D is the operational core** of the programme
- The other branches are SPECIALIZATIONS of the CBB structure
- Decomposing Branch D deeply lifts confidence on every e-circle face simultaneously

This is a higher-leverage target than the outer ring's individual vertices.

## Directory structure (identical per branch)

```
strategy/inner-rings/<branch-name>/
├── README.md                   (branch-specific overview)
├── <branch>-brief.md            (PAC directive for this branch)
├── <branch>-run.md              (invocation file)
├── proof-chain/                 (per-item PROOF-CHAIN.md files)
│   ├── INDEX.md
│   └── item-NN-<short-name>/
│       └── PROOF-CHAIN.md
└── pac-output/
    ├── bootstrap/
    ├── runs/
    │   └── run-NN/
    └── atlas/
        └── branch-<letter>-atlas.md
```

## How the inner-rings bundles relate to the others

Three parallel bundles (sibling to each other):

| Bundle | Target | Output |
|---|---|---|
| `strategy/decomposition/` | 25-vertex outer ring | Decomposition atlas (3000-5000 leaves) |
| `strategy/ccm-verification/` | CCM 2025 external dependency | CCM ledger + Lead 6 email |
| `strategy/inner-rings/` | QG5D's 5 branches (internal structure) | 5 branch atlases (~400-650 leaves total) |

All three feed the **same Zenodo priority release**. The outer ring gets wide coverage; the CCM ledger classifies external dependency; the inner rings deepen the QG5D-rooted foundations.

## Operational plan

### Phase 1 — Bootstrap (same for all 5 branches)

For each branch:
1. Extract the branch's items from `integers/paper01-qg5d/PROOF-CHAIN.md` (or `integers/paper02-cosmology/`, `integers/paper12-cbb-system/`, etc.)
2. Create `proof-chain/item-NN-<short-name>/PROOF-CHAIN.md` per item
3. Record: source reference, current status (most are PROVED), framework dependents, cross-cut to e-circle faces

### Phase 2 — Branch-by-branch decomposition

Priority order based on leverage:

**Branch D first** (operational core; deepest leverage — lifts every e-circle face)
**Branch E second** (pins; highest pedagogical value for Zenodo release)
**Branch A third** (quantum; mostly classical, easy wins)
**Branch B fourth** (gravity; already mostly PROVED, refinements)
**Branch C fifth** (cosmology; depends on Paper 2 content, longer chains)

### Phase 3 — Atlas assembly

Each branch produces its own atlas. The five branch atlases + the outer-ring decomposition atlas + the CCM ledger = the complete Zenodo release.

## What this adds to the programme

Before inner rings: the programme was a 25-vertex ring with QG5D as a hub. Hub radiation filled chord edges. Good, but treated QG5D as ONE vertex.

After inner rings: QG5D is revealed as SIX RINGS meeting at a point (outer + 5 branches). The programme's full graph is a bouquet of six circles. Each ring has its own character and can be attacked with its own protocol.

**This is the correct mathematical model of what Paper 1 actually is.** Paper 1 isn't one paper — it's the CENTER OF THE PROGRAMME with five branches radiating outward. The inner-rings bundle makes this operational.

---

*The programme is a bouquet. QG5D is the common point. Five branches + one outer ring = six circles meeting at one center. Each has its own protocol. Each contributes to the atlas. The Zenodo release assembles the bouquet.*

*Sibling to `strategy/decomposition/README.md` and `strategy/ccm-verification/README.md`.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
