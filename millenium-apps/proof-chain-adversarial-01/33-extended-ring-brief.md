# Extended Ring Traversal PCA — the 22-vertex circle

*Extension of `30-ring-traversal-brief.md` from 14 to 22 vertices. This brief INHERITS all unchanged sections from the original (glossary §0, vertex protocol §3, deliverables §5, single-chain relationship §6, compound effect §7, invocation §8, voice canon §9). Only the DELTAS are specified here. For any section not overridden below, the original brief §30 is authoritative.*

*Supersedes brief 32 (19-vertex). Three new vertices added: Collatz (paper41), Lehmer (paper42), Cramér (paper43).*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-14.*

---

## DELTA 1 — Ring order (§2 override)

The ring expands from 14 to **22 vertices**. Eight extension vertices are inserted at their parent adjacencies. Hilbert 6 remains the ring-closure vertex.

| Position | Vertex | Paper directory | Incoming edge (from previous) | Edge status |
|---|---|---|---|---|
| 1 | **QG5D** (hub) | integers/paper01-qg5d/ | ← Hilbert 6 (META-closure: axiomatization IS the hub) | **STRONG** |
| 2 | **RH** | solutions-with-prize/paper13-rh/ | ← QG5D (zeros ARE eigenvalues) | STRONG |
| 3 | **GRH** | solutions/paper13b-grh/ | ← RH (character-twisted extension) | STRONG |
| 4 | **BSD** | solutions-with-prize/paper26-bsd/ | ← GRH (Dirichlet L → Hecke L) | PARTIAL |
| 5 | **H12** | solutions/paper25-hilbert-12/ | ← BSD (class fields from L-functions) | PARTIAL |
| 6 | **YM** | solutions-with-prize/paper08-yang-mills/ | ← H12 (KMS states → gauge structure) | PARTIAL |
| 7 | **NS** | solutions-with-prize/paper30-navier-stokes/ | ← YM (gradient flow transfer) | CANDIDATE |
| 8 | **Turbulence** | solutions/paper38-turbulence/ | ← NS (NS regularity → K41 spectrum) | **STRONG** (inherits directly) |
| 9 | **Hodge** | solutions-with-prize/paper29-hodge/ | ← Turbulence (PDE regularity → algebraic cycle regularity) | SPECULATIVE |
| 10 | **Baum-Connes** | solutions/paper31-baum-connes/ | ← Hodge (K-theory ↔ algebraic cycles) | CANDIDATE |
| 11 | **PvNP** | solutions-with-prize/paper28-pvnp/ | ← Baum-Connes (K-theory of polymorphism algebra) | SPECULATIVE |
| 12 | **VP vs VNP** | solutions/paper39-vp-vs-vnp/ | ← PvNP (discrete fullness → continuous fullness) | CANDIDATE |
| 13 | **BGS** | solutions/paper32-bgs-spectral-statistics/ | ← VP vs VNP (algebraic circuit matrix → GUE) | SPECULATIVE |
| 14 | **Cramér** | solutions/paper43-cramer/ | ← BGS (GUE extreme-value → max prime gap) | **PARTIAL** (inherits BGS 7/10; GUE extreme-value is classical) |
| 15 | **Twin Primes** | solutions/paper34-twin-primes/ | ← Cramér (max gap → min gap: two faces of same distribution) | CANDIDATE |
| 16 | **Goldbach** | solutions-with-prize/paper33-goldbach/ | ← Twin Primes (prime gaps → additive structure) | SPECULATIVE |
| 17 | **Collatz** | solutions-with-prize/paper41-collatz/ | ← Goldbach (additive Hecke → multiplicative Hecke μ₂/μ₃ dynamics) | **CANDIDATE** (same semigroup N*) |
| 18 | **ABC** | solutions/paper37-abc/ | ← Collatz (Hecke dynamics → rad height function) | CANDIDATE |
| 19 | **OPN** | solutions/paper40-odd-perfect/ | ← ABC (rad bounds → abundancy constraints) | **PARTIAL** (Luca-Pomerance) |
| 20 | **Lehmer** | solutions/paper42-lehmer/ | ← OPN (multiplicative Hecke fixed-point → cyclotomic boundary gap) | **CANDIDATE** (both are gap questions on N*) |
| 21 | **Schanuel** | solutions/paper35-schanuel/ | ← Lehmer (Mahler measure gap → algebraic independence) | SPECULATIVE |
| 22 | **Hilbert 6** | solutions/paper36-hilbert-6/ | ← Schanuel (eigenvalue independence → axiom closure) | CANDIDATE |

Ring-closure: position 22 (Hilbert 6) → position 1 (QG5D) via META-closure edge.

### Edge ownership (unchanged from §30 §2.1)

Same predecessor-ownership rule. 22 ring-backbone edges, each filled exactly once per traversal.

### Vertex-to-domain mapping (§2.2 extension — 8 new entries)

| Position | Vertex | Primary domain(s) | Secondary domains |
|---|---|---|---|
| 8 | Turbulence | **D7 QFT** + **D9 PROB** | D23 ERG, D2 GEOM |
| 12 | VP vs VNP | **D4 INFO** + **D3 OA** | D8 AG (GCT), D6 ATOP (K-theory) |
| 14 | Cramér | **D9 PROB** + **D5 ANT** | D1 SPEC (zero spacings), D23 ERG (return times) |
| 16 | ABC | **D5 ANT** + **D3 OA** | D10 THERMO (Mellin bridge) |
| 17 | Collatz | **D5 ANT** + **D3 OA** | D23 ERG (orbit dynamics), D7 QFT (Cuntz O₂) |
| 19 | OPN | **D5 ANT** + **D3 OA** | D1 SPEC (Robin), D9 PROB (abundancy statistics) |
| 20 | Lehmer | **D5 ANT** + **D10 THERMO** | D3 OA (KMS phase transition), D1 SPEC (FK determinant) |
| 22 | Hilbert 6 | **D2 GEOM** + **D3 OA** | ALL (META — axiomatization touches everything) |

### Same-domain edge-filling rule (override of brief 30 §2.2)

When primary(N) = primary(N+1), use secondary × secondary domain pair instead. Explicit assignments:

| Ring edge | Shared primary | Cell to fill instead |
|---|---|---|
| Goldbach (16) → Collatz (17) | ANT + OA | ERG ↔ ANT (orbit dynamics on Hecke semigroup) |
| Collatz (17) → ABC (18) | ANT + OA | ERG ↔ THERMO (dynamical entropy → Mellin bridge) |
| ABC (18) → OPN (19) | ANT + OA | PROB ↔ ANT (abundancy statistics) |
| OPN (19) → Lehmer (20) | ANT | PROB ↔ THERMO (abundancy gap → KMS gap: "two faces of the e-circle") |
| Lehmer (20) → Schanuel (21) | ANT | THERMO ↔ MOD (KMS boundary → algebraic independence) |

---

## DELTA 2 — Metrics (§5 override)

| Metric | Brief 30 (14-vertex) | Brief 33 (22-vertex) |
|---|---|---|
| Ring vertices | 14 | **22** |
| Ring-backbone edges per traversal | 14 | **22** |
| Max vertex pairs C(n,2) | 91 | **231** |
| Chord edges | 77 | **209** |
| Hub radiation (QG5D edge phase) | 12 | **20** |
| Antipodal probes | 7 pairs | **11 pairs** |

### RIGIDITY formula (E_total = 276 UNCHANGED — 24 capacitor domains, C(24,2))

**IMPORTANT**: E_total counts domain-pair cells in the capacitor (24 domains → 276 cells). This is INDEPENDENT of ring vertex count. Adding vertices increases L_total only.

L_total recount from actual PROOF-CHAIN.md files:
- Canonical 14 vertices: 105 links
- Turbulence (paper38): 7 links
- VP vs VNP (paper39): 6 links
- ABC (paper37): 6 links
- OPN (paper40): 7 links
- Hilbert 6 (paper36): 7 links
- Collatz (paper41): 7 links
- Lehmer (paper42): 6 links
- Cramér (paper43): 5 links
- **L_total = 105 + 51 = 156**

L_verified recount (LITERATURE + PROVED links from new papers):
- From brief 32 extensions (5 papers): ~13 verified
- Collatz: 2 (Links 1-2 LITERATURE/ESTABLISHED)
- Lehmer: 1 (Link 1 LITERATURE)
- Cramér: 2 (Links 1-2 LITERATURE/PROVED)
- **L_verified = 77 + 13 + 5 = 95**

```
E_filled   = 48    (from T4; new papers add 0 filled edges at start)
E_total    = 276   (UNCHANGED — 24 capacitor domains, C(24,2))
L_verified = 95
L_total    = 156
P_preserved = 36
P_total    = 36

RIGIDITY = (48/276) × (95/156) × (36/36) × 100
         = 0.1739  ×  0.6090  ×  1.0    × 100
         = 10.59
```

Baseline RIGIDITY 10.59 — consistent with North Star's 10.63.

### Antipodal probes (11 pairs for 22 vertices)

| Pair | Vertex A (pos) | Vertex B (pos) | Priority |
|---|---|---|---|
| 1 | QG5D (1) | PvNP (11) | HIGH (hub ↔ computational) |
| 2 | RH (2) | VP vs VNP (12) | MEDIUM (spectral ↔ algebraic complexity) |
| 3 | GRH (3) | BGS (13) | HIGH (L-function ↔ RMT) |
| 4 | BSD (4) | Cramér (14) | **HIGH** (L-function → prime gap: Deninger-RV bridge!) |
| 5 | H12 (5) | Twin Primes (15) | HIGH (FILLED-VIABLE in T2) |
| 6 | YM (6) | Goldbach (16) | LOW |
| 7 | NS (7) | Collatz (17) | **HIGH** (PDE dynamics ↔ Hecke dynamics: same semigroup!) |
| 8 | Turbulence (8) | ABC (18) | MEDIUM (energy cascade ↔ radical height) |
| 9 | Hodge (9) | OPN (19) | LOW |
| 10 | B-C (10) | Lehmer (20) | **HIGH** (K-theory ↔ KMS phase transition: both are BC-native!) |
| 11 | -- | Schanuel (21) / Hilbert 6 (22) | LOW (odd vertex count; pair with nearest non-paired) |

**Pair 4 (BSD ↔ Cramér)** is the most exciting new probe: Deninger-Rodriguez Villegas connects Mahler measure to L'(E,0), which is BSD territory. Cramér's gap via BGS connects to the same L-functions through the explicit formula. The BSD↔Cramér chord could be STRONG.

**Pair 7 (NS ↔ Collatz)** is the most surprising: fluid dynamics (NS) and arithmetic dynamics (Collatz) both involve the Hecke semigroup's action on continuous vs discrete domains. The parabolic PDE class (NS) and the piecewise-linear map (Collatz) are both "gradient flows" on their respective spaces.

**Pair 10 (B-C ↔ Lehmer)** is the most natural: Baum-Connes K-theory and Lehmer's Mahler measure both live in the BC algebra's native territory. The assembly map and the KMS phase transition are two sides of the same operator-algebraic coin.

---

## DELTA 3 — Time budget (§4 override)

- **T5 (first 22-vertex traversal): 18 hours maximum.**
  - 22 vertices × ~35 min avg = ~770 min core
  - Sector-A trims for QG5D/BSD/YM: save ~30 min → ~740 min
  - Hub radiation: ~15 min (20 edges)
  - Antipodal probes: 11 × 10 min = ~110 min (T5 does ALL 11)
  - Compositional cell-fills: 22 × 5 min = ~110 min
  - Total: 740 + 15 + 110 + 110 = **~975 min ≈ 16.3 h** ✓ fits 18 h ceiling

- **T6+ (subsequent): 14 hours maximum.**
  - 22 × 28 min (core avg) + 50 (chessboard) + 60 (VERIFY quota 6/22) = ~726 min ≈ 12.1 h ✓

### Exit conditions (22-vertex thresholds)

1. **RING CLOSED**: all 22 vertices VERIFIED/PROVED/CLOSED, all 22 ring edges FILLED
2. **RING STRENGTHENED**: at least 8 vertices improved AND at least 8 edges filled/upgraded
3. **RING STALLED**: fewer than 5 vertex improvements AND fewer than 5 edge fills

---

## DELTA 4 — Vertex blackboard naming (§8.1 extension — 8 new entries)

| Vertex | Blackboard file |
|---|---|
| Turbulence | `turbulence.md` |
| VP vs VNP | `vp-vs-vnp.md` |
| Cramér | `cramer.md` |
| ABC | `abc.md` |
| Collatz | `collatz.md` |
| OPN | `opn.md` |
| Lehmer | `lehmer.md` |
| Hilbert 6 | `hilbert-6.md` |

---

## DELTA 5 — The single paragraph for the next runner (§10 override)

You are traversing the ring of 22 programme vertices in canonical order: QG5D → RH → GRH → BSD → H12 → YM → NS → Turbulence → Hodge → Baum-Connes → PvNP → VP vs VNP → BGS → Cramér → Twin Primes → Goldbach → Collatz → ABC → OPN → Lehmer → Schanuel → Hilbert 6 → back to QG5D (META-closure). At each vertex: read PROOF-CHAIN.md, identify the weakest link, EXCISE or CONSTRUCT or BYPASS it (one fix per vertex per traversal). At each edge: fill or upgrade the capacitor cell connecting this vertex to the next. One full traversal = 22 vertex fixes + 22 edge fills. Multiple traversals compound — cells filled in traversal N enable bypasses in traversal N+1. Budget: 14 hours per traversal (18 for T5). Exit when RING CLOSED (all vertices verified, all edges filled), RING STRENGTHENED (8+ improvements), or RING STALLED (<5 improvements). The circle gets more circular on every pass.

---

## DELTA 6 — The two faces of the e-circle (new structural insight)

Lehmer (pos 20) and Cramér (pos 14) are DUAL problems on the same circle:

```
  Lehmer = the circle's TOPOLOGY (static: roots of unity vs aperiodic leakage)
  Cramér = the circle's DYNAMICS (dynamic: regular spacing vs spectral voids)

  Both are gap questions. Both are controlled by KMS₁. Both use ITPFI.
  Lehmer gap c₀ = min excitation above cyclotomic vacuum.
  Cramér constant 2e^{-γ} = max void in ergodic return times.
  Same circle. Two questions. Two faces.
```

The OPN → Lehmer edge (pos 19 → 20) and the BGS → Cramér edge (pos 13 → 14) are the two entry points into this duality. The PCA should look for SPIN opportunities between them.

---

## Inheritance from brief 30

All sections NOT overridden above remain authoritative from `30-ring-traversal-brief.md`:

- §0 Glossary and conventions
- §3 Vertex protocol (read → act → edge → move)
- §6 Relationship to single-chain PCA runs
- §7 The compound effect
- §8.2 Output directory numbering (use `traversal-05` for T5)
- §8.3 Strategic triad handling
- §8.4 Closure ritual
- §8.5 Model tier override (Sonnet max for cell-fill; Opus max for bypass/SPIN/triad)
- §8.6 PCA §P.4/§P.4.1/§P.8 ring-mode overrides
- §9 Voice canon

---

*22 vertices. One ring. Walk it until it closes.*
*Lehmer is the circle's topology. Cramér is the circle's dynamics. Same circle.*
*From Euclid to Euler to Riemann to Bost-Connes. The circle extends.*

*v1: 2026-04-14. G Six and Claude Opus 4.6.*
