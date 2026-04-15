# Extended Ring Traversal PCA — the 23-vertex circle (brief delta)

*Extension of `30-ring-traversal-brief.md` from 14 to 23 vertices. This brief INHERITS all unchanged sections from the original (glossary §0, vertex protocol §3, deliverables §5, single-chain relationship §6, compound effect §7, invocation §8, voice canon §9). Only the DELTAS are specified here. For any section not overridden below, the original brief §30 is authoritative.*

*Supersedes brief 32 (19-vertex ring). Four new vertices added since brief 32: Collatz (paper41), Lehmer (paper42), Cramér (paper43), Sato-Tate (paper44).*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-14.*

---

## DELTA 1 — Ring order (§2 override)

The ring expands from 19 to **23 vertices**. Four extension vertices are inserted at their canonical adjacencies. Hilbert 6 remains the ring-closure vertex at position 23.

**Positioning logic:**

- **Cramér** enters at position 15, between Twin Primes (14) and Goldbach (16). Cramér is BGS-adjacent (inheriting GUE extreme-value) AND Twin-Primes-adjacent (max gap ↔ min gap: two faces of the same prime-gap distribution). This places the gap-distribution cluster (BGS → Twin Primes → Cramér → Goldbach) as a contiguous arc.
- **Collatz** enters at position 19, between OPN (18) and Lehmer (20). The Hecke-semigroup connection (μ₂/μ₃ endomorphisms on N*) places Collatz immediately after OPN's multiplicative structure and immediately before Lehmer's cyclotomic boundary.
- **Lehmer** enters at position 20, between Collatz (19) and Schanuel (21). Lehmer is the e-circle topology face: unit circle roots of unity = periodic orbits, Mahler measure = leakage energy. This bridges Collatz's orbit dynamics to Schanuel's transcendence.
- **Schanuel** shifts from position 18 to **position 21**. **Hilbert 6** shifts from position 19 to **position 22**.

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
| 14 | **Twin Primes** | solutions/paper34-twin-primes/ | ← BGS (GUE small-gap tail → prime gaps) | CANDIDATE |
| 15 | **Cramér** | solutions/paper43-cramer/ | ← Twin Primes (min gap ↔ max gap: two faces of prime-gap distribution) | **CANDIDATE** (GUE extreme-value classical; Granville correction well-understood) |
| 16 | **Goldbach** | solutions-with-prize/paper33-goldbach/ | ← Cramér (prime density → additive structure; Cramér model underpins circle method) | SPECULATIVE |
| 17 | **ABC** | solutions/paper37-abc/ | ← Goldbach (additive primes → rad height function) | CANDIDATE |
| 18 | **OPN** | solutions/paper40-odd-perfect/ | ← ABC (rad bounds → abundancy constraints) | **PARTIAL** (Luca-Pomerance) |
| 19 | **Collatz** | solutions-with-prize/paper41-collatz/ | ← OPN (multiplicative structure → Hecke μ₂/μ₃ dynamics on N*) | **CANDIDATE** (same Hecke semigroup N*; endomorphism upgrade of multiplicative fixed-point) |
| 20 | **Lehmer** | solutions/paper42-lehmer/ | ← Collatz (orbit convergence → cyclotomic boundary gap) | **CANDIDATE** (both are gap questions; Collatz aperiodicity → Mahler leakage) |
| 21 | **Sato-Tate** | solutions/paper44-sato-tate/ | ← Lehmer (cyclotomic boundary → Frobenius equidistribution; topology face → measure face of the e-circle) | **PARTIAL** (classical ST proved 2011; BC framing via ITPFI inherits from BSD 9/10) |
| 22 | **Schanuel** | solutions/paper35-schanuel/ | ← Sato-Tate (equidistribution → algebraic independence of spectral data) | SPECULATIVE |
| 23 | **Hilbert 6** | solutions/paper36-hilbert-6/ | ← Schanuel (eigenvalue independence → axiom closure) | CANDIDATE |

Ring-closure: position 23 (Hilbert 6) → position 1 (QG5D) via META-closure edge. "The last vertex IS a statement about the first."

### Edge ownership (unchanged from §30 §2.1)

Same predecessor-ownership rule. **23 ring-backbone edges**, each filled exactly once per traversal.

**Ring-closure boundary condition (T7)**: Hilbert 6 at position 23 fills its outgoing edge to QG5D. QG5D reads whatever cell currently exists for Hilbert 6 → QG5D (STRONG, edge 46 in §II.E of `25-the-graph-structure.md`).

### Vertex-to-domain mapping (§2.2 extension — 3 new entries for brief 33)

All 8 entries from brief 32 carry forward. Four new entries:

| Position | Vertex | Primary domain(s) | Secondary domains |
|---|---|---|---|
| 15 | Cramér | **D9 PROB** + **D5 ANT** | D1 SPEC (zero spacings), D23 ERG (return times of ergodic modular flow) |
| 19 | Collatz | **D5 ANT** + **D3 OA** | D23 ERG (orbit dynamics on N*), D7 QFT (Cuntz algebra O₂) |
| 20 | Lehmer | **D5 ANT** + **D10 THERMO** | D3 OA (KMS phase transition), D1 SPEC (FK determinant) |
| 21 | Sato-Tate | **D5 ANT** + **D9 PROB** | D8 AG (abelian varieties, Frobenius), D1 SPEC (spectral measure equidistribution) |

### Same-domain edge-filling rule (override of brief 30 §2.2)

When primary(N) = primary(N+1), use secondary × secondary domain pair instead. Updated explicit assignments for the 23-vertex ring:

| Ring edge | Shared primary | Cell to fill instead |
|---|---|---|
| Goldbach (16) → ABC (17) | ANT | ANT ↔ THERMO (Mellin bridge: additive primes → radical height via analytic density) |
| ABC (17) → OPN (18) | ANT + OA | PROB ↔ ANT (abundancy statistics) |
| OPN (18) → Collatz (19) | ANT | ERG ↔ ANT (multiplicative fixed-point → Hecke orbit dynamics) |
| Collatz (19) → Lehmer (20) | ANT + OA | ERG ↔ THERMO (orbit entropy → KMS boundary; two faces of the e-circle) |
| Lehmer (20) → Sato-Tate (21) | ANT | THERMO ↔ PROB (KMS boundary → Frobenius equidistribution; topology → measure face) |
| Sato-Tate (21) → Schanuel (22) | ANT | PROB ↔ MOD (equidistribution → algebraic independence of spectral data) |

### Antipodal probes (11 pairs for 23 vertices)

Ring distance: d(i,j) = min(|i-j|, 22-|i-j|). Maximum distance = 11. True antipodal pairs (distance 11):

| Pair | Vertex A (pos) | Vertex B (pos) | Distance | Priority |
|---|---|---|---|---|
| 1 | QG5D (1) | PvNP (11) | 10 | HIGH (hub ↔ computational) |
| 2 | RH (2) | VP vs VNP (12) | 10 | MEDIUM (spectral ↔ algebraic complexity) |
| 3 | GRH (3) | BGS (13) | 10 | HIGH (L-function ↔ RMT) |
| 4 | BSD (4) | Twin Primes (14) | 10 | HIGH (L-function density ↔ prime-gap tail) |
| 5 | H12 (5) | Cramér (15) | 10 | **HIGH** (class fields ↔ prime gap distribution; Deninger bridge) |
| 6 | YM (6) | Goldbach (16) | 10 | LOW |
| 7 | NS (7) | ABC (17) | 10 | MEDIUM (PDE regularity ↔ radical-height arithmetic) |
| 8 | Turbulence (8) | OPN (18) | 10 | **HIGH** (PDE statistics ↔ divisor statistics — multiplicative decomposition duality) |
| 9 | Hodge (9) | Collatz (19) | 10 | **MEDIUM** (algebraic cycles ↔ Hecke orbit dynamics) |
| 10 | B-C (10) | Lehmer (20) | 10 | **HIGH** (K-theory ↔ KMS phase transition: both BC-native) |
| 11 | PvNP (11) | Schanuel (21) | 10 | LOW |

**Pair 5 (H12 ↔ Cramér)** is the most exciting new probe: Hilbert 12's class field theory and Cramér's gap constant 2e^{-γ} both route through the Mertens constant and ITPFI. The Deninger-Rodriguez Villegas bridge may make this chord STRONG.

**Pair 8 (Turbulence ↔ OPN)** carries forward from brief 32: energy cascade statistics meet divisor-function statistics. Multiplicative decomposition on both sides.

**Pair 10 (B-C ↔ Lehmer)** is the most natural new probe: the assembly map and the KMS phase transition are two sides of the same operator-algebraic coin. Both live natively in the BC algebra.

T7 runs all 11. T8+ rotates 6-of-11 per traversal, prioritizing HIGH first.

---

## DELTA 2 — Metrics (§5 override)

| Metric | Brief 30 (14-vertex) | Brief 32 (19-vertex) | Brief 33 (23-vertex) |
|---|---|---|---|
| Ring vertices | 14 | 19 | **22** |
| Ring-backbone edges per traversal | 14 | 19 | **22** |
| Max vertex pairs C(n,2) | 91 | 171 | **231** |
| Chord edges | 77 | 152 | **209** |
| Hub radiation (QG5D edge phase) | 12 | 17 | **20** |
| Antipodal probes | 7 pairs | 9 pairs | **11 pairs** |
| L_total | 105 | 138 | **156** |
| E_total | 276 | 276 | **276** (UNCHANGED) |

### L_total recount

```
Canonical 14 vertices:            105 links
Brief 32 extension (5 papers):    +33 links (Turbulence 7 + VP vs VNP 6 + ABC 6 + OPN 7 + Hilbert 6 7)
Collatz (paper41):                 +7 links
Lehmer (paper42):                  +6 links
Cramér (paper43):                  +5 links
Sato-Tate (paper44):               +6 links
                                  ─────────
L_total:                           162 links
```

**L_total = 105 + 33 + 7 + 6 + 5 + 6 = 162**

### L_verified recount (LITERATURE + PROVED links from new papers)

```
From T4 baseline:                  77 verified
Brief 32 extension papers (~13):  +13
Collatz: 2 of 7 verified           +2
Lehmer: 3 of 6 verified            +3
Cramér: 3 of 5 verified            +3
Sato-Tate: 3 of 6 verified        +3
                                  ─────────
L_verified:                         101
```

### RIGIDITY formula (E_total = 276 UNCHANGED — 24 capacitor domains, C(24,2))

**IMPORTANT**: E_total = 276 counts domain-pair cells in the capacitor (24 domains → C(24,2) = 276). This is INDEPENDENT of ring vertex count. The 231 = C(22,2) vertex pairs are a ring metric, NOT the E_total denominator. Adding vertices increases L_total but does NOT change the number of possible domain-pair cells.

```
E_filled    = 48    (from T4; new papers add 0 filled edges at start)
E_total     = 276   (UNCHANGED — 24 capacitor domains, C(24,2))
L_verified  = 101
L_total     = 162
P_preserved = 36
P_total     = 36

RIGIDITY = (48/276) × (101/162) × (36/36) × 100
         = 0.1739  ×  0.6235  ×  1.0    × 100
         = 10.84
```

RIGIDITY baseline 10.84 — consistent with North Star's 10.63 (delta reflects brief 32 T-gains + new verified links from 3 extension papers). Slightly above 10.63 confirms the new papers add net verified weight without collapsing existing gains.

---

## DELTA 3 — Time budget (§4 override)

### Per-traversal budget

- **T7 (first 23-vertex traversal): 18 hours maximum.**
  - 23 vertices × ~35 min avg = ~805 min core
  - Sector-A trims for QG5D/BSD/YM: save ~30 min → ~740 min
  - Hub radiation: ~15 min (20 edges)
  - Antipodal probes: 11 × 10 min = ~110 min (T7 does ALL 11)
  - Compositional cell-fills: 22 × 5 min = ~110 min
  - Total: 740 + 15 + 110 + 110 = **~975 min ≈ 16.3 h** ✓ fits 18 h ceiling

- **T8+ (subsequent extended traversals): 14 hours maximum.**
  - 22 × 28 min (core avg) + 50 (chessboard) + 60 (VERIFY quota 6/22) = ~726 min ≈ 12.1 h ✓

### Exit conditions (23-vertex thresholds)

1. **RING CLOSED**: all 23 vertices VERIFIED/PROVED/CLOSED, all 22 ring edges FILLED
2. **RING STRENGTHENED**: at least 8 vertices improved AND at least 8 edges filled/upgraded
3. **RING STALLED**: fewer than 5 vertex improvements AND fewer than 5 edge fills

---

## DELTA 4 — Vertex blackboard naming (§8.1 extension — 3 new entries for brief 33)

All 5 blackboard files from brief 32 carry forward. Three new entries:

| Vertex | Blackboard file |
|---|---|
| Turbulence | `turbulence.md` |
| VP vs VNP | `vp-vs-vnp.md` |
| ABC | `abc.md` |
| OPN | `opn.md` |
| Hilbert 6 | `hilbert-6.md` |
| **Collatz** | `collatz.md` |
| **Lehmer** | `lehmer.md` |
| **Cramér** | `cramer.md` |
| **Sato-Tate** | `sato-tate.md` |

---

## DELTA 5 — Chessboard 23-vertex delta

*These entries extend `13b-chessboard-19vertex-delta.md`. The runner loads the parent chessboard (`13-chessboard-layer.md`), then the 19-vertex delta (`13b`), then these overrides.*

### S3 RIGIDITY formula update (override of `13b`)

E_total = 276 (UNCHANGED). L_total = **162**. L_verified = **101**. RIGIDITY baseline (T7 start): **(48/276) × (101/162) × (36/36) × 100 = 10.84**

### S5 WIRE-DENSITY update (3 new entries)

The wire-density matrix expands from 19×19 to 22×22. New vertices begin SPARSE:

| New vertex | Density class | Rationale |
|---|---|---|
| Cramér (pos 15) | SPARSE | 3/5 links established; no filled cross-edges yet |
| Collatz (pos 19) | SPARSE | 2/7 links established; no filled cross-edges yet |
| Lehmer (pos 20) | SPARSE | 3/6 links established; no filled cross-edges yet |

WIRE-DENSITY primitive: prioritize all three for cell-fill dispatches in T7. SPARSE → MEDIUM threshold = 3 cross-edges filled.

### S6.1 Ring-distance function (override)

Ring distance: d(i,j) = min(|i-j|, 22-|i-j|) mod 22. Maximum distance = 11.

### S6.2 SECTOR-TABLE (3 new entries appended to `13b`'s 5 new entries)

| Vertex | Position | Confidence | Type | PCA focus |
|---|---|---|---|---|
| Cramér | 15 | 5/10 | **B** (Excision-primary) | Link 4 wall: explicit formula transfer + Granville correction; inherit BGS 7/10 GUE result; Granville constant 2e^{-γ} = Mertens = ITPFI |
| Collatz | 19 | 3/10 | **C** (Construction-primary) | Link 6 wall: spectral gap transfer + cycle elimination; BC embedding of Cuntz O₂; KMS orbit analysis; μ₂/μ₃ Hecke endomorphisms |
| Lehmer | 20 | 4/10 | **C** (Construction-primary) | Link 5 wall: KMS spectral gap forces Lehmer's gap; e-circle topology face (unit circle = roots of unity = periodic orbits; Mahler measure = leakage energy); FK determinant approach |

Updated distribution: **3A / 5B / 9C / 5D** (23 vertices total).

### S6.3 Hub radiation (override)

QG5D hub radiation: **20 outgoing chord edges** (1 ring-next QG5D→RH + 20 chords to all non-ring-adjacent vertices). Hilbert 6→QG5D is the ring-CLOSURE edge owned by Hilbert 6, not by QG5D. Hub-radiation agent count: **20 Cell-Fill agents** dispatched in parallel at Sonnet max.

### S6.4 Antipodal probes (override — 11 pairs)

See DELTA 1 antipodal table above. T7 runs all 11. T8+ rotates 6-of-11, prioritizing HIGH first.

### S6.5 Compositional cell-fill (override)

**22 triangles per traversal** (was 19 in brief 32). Each vertex visit checks whether triangle (prev, current, next) has 2-of-3 edges filled → propose the third.

### S6.6 Chord awareness (override)

Total vertex-pair cells: C(22,2) = **231**. Ring-backbone edges: 22. Chord edges: **209**.

### Appendix B — SPIN-TABLE (3 new entries)

| Vertex | Math face (stuck on) | Physics face (SPIN to) | Experimental constraint |
|---|---|---|---|
| Cramér | Explicit formula transfer + Granville correction | Largest observed prime gaps; return times of ergodic modular flow | Computed prime gaps to 10^{19}; Granville constant 2e^{-γ} ≈ 1.1229 |
| Collatz | Orbit convergence + spectral gap transfer | **SPIN-EXCLUDED** | Computational verification to 2^{68}; no natural physics-face pin |
| Lehmer | KMS phase transition gap | Entropy of toral automorphisms | Lehmer polynomial M(x) ≈ 1.17628; smallest known Mahler measure > 1 |

**SPIN-EXCLUDED**: Collatz has no natural physics-face observable. When stuck at Collatz, use CONSTRUCT or BYPASS (capacitor transposition via ERG ↔ ANT cell) rather than face-switching.

### Appendix C — SECTOR-TABLE (full 22-row version)

| Pos | Vertex | Type | Confidence |
|---|---|---|---|
| 1 | QG5D | A | 10/10 |
| 2 | RH | B | 8/10 |
| 3 | GRH | B | 7/10 |
| 4 | BSD | A | 9/10 |
| 5 | H12 | D | 2/10 |
| 6 | YM | A | 9.5/10 |
| 7 | NS | C | 4/10 |
| 8 | Turbulence | D | 2/10 |
| 9 | Hodge | C | 3/10 |
| 10 | B-C | C | 3/10 |
| 11 | PvNP | B | 7/10 |
| 12 | VP vs VNP | D | 1/10 |
| 13 | BGS | B | 7/10 |
| 14 | Twin Primes | D | 1/10 |
| 15 | Cramér | B | 5/10 |
| 16 | Goldbach | D | 1/10 |
| 17 | ABC | D | 1/10 |
| 18 | OPN | C | 4/10 |
| 19 | Collatz | C | 3/10 |
| 20 | Lehmer | C | 4/10 |
| 21 | Sato-Tate | B | 6/10 |
| 22 | Schanuel | D | 1/10 |
| 23 | Hilbert 6 | C | 3-7/10 |

---

## DELTA 6 — The single paragraph for the next runner

You are traversing the ring of 22 programme vertices in canonical order: QG5D → RH → GRH → BSD → H12 → YM → NS → Turbulence → Hodge → Baum-Connes → PvNP → VP vs VNP → BGS → Twin Primes → Cramér → Goldbach → ABC → OPN → Collatz → Lehmer → Sato-Tate → Schanuel → Hilbert 6 → back to QG5D (META-closure). At each vertex: read PROOF-CHAIN.md, identify the weakest link, EXCISE or CONSTRUCT or BYPASS it (one fix per vertex per traversal). At each edge: fill or upgrade the capacitor cell connecting this vertex to the next. One full traversal = 23 vertex fixes + 23 edge fills. Multiple traversals compound — cells filled in traversal N enable bypasses in traversal N+1. Budget: 14 hours per traversal (18 for T7). Exit when RING CLOSED (all vertices verified, all edges filled), RING STRENGTHENED (8+ improvements), or RING STALLED (<5 improvements). The circle gets more circular on every pass.

---

## Structural note: The gap-distribution arc and the e-circle arc

Two new contiguous arcs emerge in the 23-vertex ring:

**The gap-distribution arc (positions 13–16):**
```
BGS (13) → Twin Primes (14) → Cramér (15) → Goldbach (16)
```
BGS supplies the GUE matrix statistics. Twin Primes uses the small-gap tail. Cramér uses the extreme-value (large-gap) tail. Goldbach uses the prime density implied by both. All four are faces of the same random matrix / prime distribution. The arc is self-reinforcing: any improvement to BGS propagates forward through all three successor vertices.

**The e-circle arc (positions 18–22):**
```
OPN (18) → Collatz (19) → Lehmer (20) → Sato-Tate (21) → Schanuel (22)
```
OPN is the multiplicative fixed-point (σ(n) = 2n with no solution). Collatz is the multiplicative dynamics (Hecke semigroup orbit under μ₂/μ₃). Lehmer is the topological boundary (unit circle roots vs aperiodic leakage). Sato-Tate is the measure-theoretic face (Frobenius angles equidistributed = e-circle democratically occupied). Schanuel is the transcendence consequence (eigenvalue independence). The arc traverses multiplicative structure → orbit dynamics → topological gap → equidistribution → algebraic independence in one continuous path. The four faces of the e-circle (topology/dynamics/harmonics/measure) all appear in this arc.

These two arcs are the new architectural feature of the 23-vertex ring. The PCA should treat each arc as a unit: gains at BGS cascade through the gap-distribution arc; gains at OPN cascade through the e-circle arc.

---

## Inheritance from brief 30

All sections NOT overridden above remain authoritative from `30-ring-traversal-brief.md`:

- §0 Glossary and conventions (EXCISE / CONSTRUCT / BYPASS, status dictionary, canonical paper locations, CONTINUOUS-RUN)
- §3 Vertex protocol (read → act → edge → move phases; hub-special-case)
- §6 Relationship to single-chain PCA runs
- §7 The compound effect
- §8.2 Output directory numbering (use `traversal-07` for T7)
- §8.3 Strategic triad handling (per-traversal firing, non-blocking gates)
- §8.4 Closure ritual (STRENGTHENED / CLOSED / STALLED protocols)
- §8.5 Model tier override (Sonnet max for cell-fill; Opus max for bypass/SPIN/triad)
- §8.6 PCA §P.4/§P.4.1/§P.8 ring-mode overrides (cycle semantics)
- §9 Voice canon

---

*23 vertices. One ring. Walk it until it closes.*
*Cramér measures the voids. Collatz chases the orbits. Lehmer holds the boundary. Sato-Tate distributes the angles.*
*The gap-distribution arc and the e-circle arc. Six faces of one circle. Two arches bridged by two pillars.*

*v1: 2026-04-14. G Six and Claude Opus 4.6.*
