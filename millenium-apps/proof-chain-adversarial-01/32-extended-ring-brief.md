# Extended Ring Traversal PCA — the 19-vertex circle

*Extension of `30-ring-traversal-brief.md` from 14 to 19 vertices. This brief INHERITS all unchanged sections from the original (glossary §0, vertex protocol §3, deliverables §5, single-chain relationship §6, compound effect §7, invocation §8, voice canon §9). Only the DELTAS are specified here. For any section not overridden below, the original brief §30 is authoritative.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-14.*

---

## DELTA 1 — Ring order (§2 override)

The ring expands from 14 to **19 vertices**. Five extension vertices are inserted at their parent adjacencies. Hilbert 6 replaces Schanuel as the ring-closure vertex.

| Position | Vertex | Paper directory | Incoming edge (from previous) | Edge status |
|---|---|---|---|---|
| 1 | **QG5D** (hub) | paper1/ | ← Hilbert 6 (META-closure: axiomatization IS the hub) | **STRONG** |
| 2 | **RH** | paper13-rh/ | ← QG5D (zeros ARE eigenvalues) | STRONG |
| 3 | **GRH** | paper13b-grh/ | ← RH (character-twisted extension) | STRONG |
| 4 | **BSD** | paper26-bsd/ | ← GRH (Dirichlet L → Hecke L) | PARTIAL |
| 5 | **H12** | paper25-hilbert-12/ | ← BSD (class fields from L-functions) | PARTIAL |
| 6 | **YM** | paper08-yang-mills/ | ← H12 (KMS states → gauge structure) | PARTIAL |
| 7 | **NS** | paper30-navier-stokes/ | ← YM (gradient flow transfer) | CANDIDATE |
| 8 | **Turbulence** | paper38-turbulence/ | ← NS (NS regularity → K41 spectrum) | **STRONG** (inherits directly) |
| 9 | **Hodge** | paper29-hodge/ | ← Turbulence (PDE regularity → algebraic cycle regularity) | SPECULATIVE |
| 10 | **Baum-Connes** | paper31-baum-connes/ | ← Hodge (K-theory ↔ algebraic cycles) | CANDIDATE |
| 11 | **PvNP** | paper28-pvnp/ | ← Baum-Connes (K-theory of polymorphism algebra) | SPECULATIVE |
| 12 | **VP vs VNP** | paper39-vp-vs-vnp/ | ← PvNP (discrete fullness → continuous fullness) | **CANDIDATE** (PvNP L5 still OPEN; GCT content is independent) |
| 13 | **BGS** | paper32-bgs-spectral-statistics/ | ← VP vs VNP (algebraic circuit matrix → GUE) | **SPECULATIVE** (downgrade from brief 30's PvNP→BGS CANDIDATE — new source vertex is weaker) |
| 14 | **Twin Primes** | paper34-twin-primes/ | ← BGS (GUE small-gap tail → prime gaps) | CANDIDATE |
| 15 | **Goldbach** | paper33-goldbach/ | ← Twin Primes (prime gaps → additive structure) | SPECULATIVE |
| 16 | **ABC** | paper37-abc/ | ← Goldbach (additive primes → rad height function) | **CANDIDATE** (shared Hecke semigroup) |
| 17 | **OPN** | paper40-odd-perfect/ | ← ABC (rad bounds → abundancy constraints) | **PARTIAL** (Luca-Pomerance) |
| 18 | **Schanuel** | paper35-schanuel/ | ← OPN (multiplicative fixed-point → algebraic independence) | SPECULATIVE |
| 19 | **Hilbert 6** | paper36-hilbert-6/ | ← Schanuel (eigenvalue independence → axiom closure) | CANDIDATE |

Ring-closure: position 19 (Hilbert 6) → position 1 (QG5D) via META-closure edge. "The last vertex IS a statement about the first."

### Edge ownership (unchanged)

Same predecessor-ownership rule as §30 §2.1. Each vertex fills its OUTGOING edge. 19 ring-backbone edges, each filled exactly once per traversal.

**Ring-closure boundary condition (T5)**: Hilbert 6 at position 19 fills its outgoing edge to QG5D. On T5 (first extended traversal), QG5D reads whatever cell currently exists for Hilbert 6 → QG5D (STRONG, already documented as edge 46 in §II.E of `25-the-graph-structure.md`).

### Vertex-to-domain mapping (§2.2 extension)

Five new entries added to the §30 domain table:

| Position | Vertex | Primary domain(s) | Secondary domains |
|---|---|---|---|
| 8 | Turbulence | **D7 QFT** + **D9 PROB** | D23 ERG, D2 GEOM |
| 12 | VP vs VNP | **D4 INFO** + **D3 OA** | D8 AG (GCT), D6 ATOP (K-theory) |
| 16 | ABC | **D5 ANT** + **D3 OA** | D10 THERMO (Mellin bridge) |
| 17 | OPN | **D5 ANT** + **D3 OA** | D1 SPEC (Robin), D9 PROB (abundancy statistics) |
| 19 | Hilbert 6 | **D2 GEOM** + **D3 OA** | ALL (META — axiomatization touches everything) |

---

## DELTA 2 — Metrics (§5 override)

| Metric | Brief 30 | Brief 32 |
|---|---|---|
| Ring vertices | 14 | **19** |
| Ring-backbone edges per traversal | 14 | **19** |
| Max capacitor cells C(n,2) | 91 | **171** |
| Chord edges | 77 | **152** |
| Hub radiation (QG5D edge phase) | 12 | **17** |
| Antipodal probes | 7 pairs | **9 pairs** |
| L_total (RIGIDITY denominator) | 105 | **138** (105 + 33 new chain links from 5 extension papers) |
| E_total (RIGIDITY denominator) | 276 | **276** (UNCHANGED — 24 capacitor domains, C(24,2) domain-pair cells) |

### RIGIDITY formula (unchanged formula, L_total updated only)

```
RIGIDITY = (E_filled / E_total) × (L_verified / L_total) × (P_preserved / P_total) × 100
```

**IMPORTANT**: E_total = 276 counts domain-pair cells in the capacitor (24 domains → C(24,2) = 276). This is INDEPENDENT of ring vertex count. The 171 = C(19,2) vertex pairs are a ring metric, NOT the E_total denominator. Adding vertices increases L_total (more chain links) but does NOT change the number of possible domain-pair cells.

L_total recount from actual PROOF-CHAIN.md files:
- Canonical 14 vertices: 105 links (unchanged)
- Turbulence (paper38): 7 links (2 INHERITED-PROVED)
- VP vs VNP (paper39): 6 links (1 LITERATURE)
- ABC (paper37): 6 links (1 LITERATURE)
- OPN (paper40): 7 links (4 PROVED/LITERATURE)
- Hilbert 6 (paper36): 7 links (4 PROVED)
- **Total new: 33 links, ~13 verified**
- **L_total = 105 + 33 = 138**

At T5 start (inheriting T4 state + 5 new papers):
```
E_filled   = 48    (from T4; new papers add 0 filled edges at start)
E_total    = 276   (UNCHANGED — 24 capacitor domains, C(24,2))
L_verified = 90    (77 from T4 + 13 LITERATURE/PROVED from new papers)
L_total    = 138   (105 + 33 new chain links)
P_preserved = 36
P_total    = 36

RIGIDITY = (48/276) × (90/138) × (36/36) × 100
         = 0.1739  ×  0.6522  ×  1.0    × 100
         = 11.34
```

**RIGIDITY baseline consistency**: 11.34 is consistent with the North Star's 10.63 (delta reflects T4 gains + new verified links from extension papers). No apparent drop — the E_total denominator is unchanged.

### Same-domain edge-filling rule (override of brief 30 §2.2 for shared-domain vertex pairs)

When primary(N) = primary(N+1) (both vertices share a primary domain), the capacitor cell lookup would hit a diagonal or pre-filled cell. Override rule:

1. If primary domains overlap: use **secondary × secondary** domain pair instead.
2. If a specific capacitor cell is already ESTABLISHED and load-bearing for another chain, the Cell-Fill Author writes a **vertex-specific annotation** (e.g., `ant-oa-opn-t05.md`) rather than overwriting the existing cell.
3. Explicit edge-to-cell assignments for same-domain pairs:

| Ring edge | Shared primary | Cell to fill instead |
|---|---|---|
| Goldbach (15) → ABC (16) | ANT | ANT ↔ THERMO (Mellin bridge) |
| ABC (16) → OPN (17) | ANT + OA | PROB ↔ ANT (abundancy statistics) |
| OPN (17) → Schanuel (18) | ANT | ANT ↔ MOD (algebraic independence of σ) |

### Antipodal probes (9 pairs for 19 vertices)

| Pair | Vertex A | Vertex B | Priority |
|---|---|---|---|
| 1 | QG5D (1) | B-C (10) | HIGH (hub ↔ K-theory) |
| 2 | RH (2) | PvNP (11) | HIGH (spectral ↔ computational) |
| 3 | GRH (3) | VP vs VNP (12) | MEDIUM (L-function ↔ algebraic complexity) |
| 4 | BSD (4) | BGS (13) | MEDIUM (L-function ↔ RMT) |
| 5 | H12 (5) | Twin Primes (14) | HIGH (already FILLED-VIABLE in T2) |
| 6 | YM (6) | Goldbach (15) | LOW |
| 7 | NS (7) | ABC (16) | MEDIUM (PDE ↔ arithmetic) |
| 8 | Turbulence (8) | OPN (17) | **HIGH** (PDE statistics ↔ divisor statistics — novel!) |
| 9 | Hodge (9) | Schanuel (18) | LOW |

Pair 8 (Turbulence ↔ OPN) is the most intriguing new antipodal: energy cascade statistics meet divisor-function statistics. Both involve multiplicative decomposition (Fourier modes for turbulence, prime factors for OPN). A correspondence here would be a genuine discovery.

---

## DELTA 3 — Time budget (§4 override)

### Per-traversal budget

- **T5 (first extended traversal): 16 hours maximum.**
  - 19 vertices × ~35 min avg = ~665 min core
  - Sector-A trims for QG5D/BSD/YM: save ~30 min → ~635 min
  - Hub radiation: ~15 min (17 edges)
  - Antipodal probes: 9 × 10 min = ~90 min (T5 does ALL 9; T6+ rotates 5/9)
  - Compositional cell-fills: 19 × 5 min = ~95 min
  - Total: 635 + 15 + 90 + 95 = **~835 min ≈ 13.9 h** ✓ fits 16 h ceiling

- **T6+ (subsequent extended traversals): 12 hours maximum.**
  - 19 × 28 min (core avg) + 50 (chessboard) + 50 (VERIFY quota 5/19) = ~582 min ≈ 9.7 h ✓

### Exit conditions (unchanged thresholds, updated counts)

1. **RING CLOSED**: all 19 vertices VERIFIED/PROVED/CLOSED, all 19 ring edges FILLED
2. **RING STRENGTHENED**: at least 7 vertices improved AND at least 7 edges filled/upgraded (was 5/5 for 14-vertex ring)
3. **RING STALLED**: fewer than 4 vertex improvements AND fewer than 4 edge fills across 19 vertices (was 3/3 for 14)

---

## DELTA 4 — Vertex blackboard naming (§8.1 extension)

Five new short-name files added:

| Vertex | Blackboard file |
|---|---|
| Turbulence | `turbulence.md` |
| VP vs VNP | `vp-vs-vnp.md` |
| ABC | `abc.md` |
| OPN | `opn.md` |
| Hilbert 6 | `hilbert-6.md` |

---

## DELTA 5 — The single paragraph for the next runner (§10 override)

You are traversing the ring of 19 programme vertices in canonical order: QG5D → RH → GRH → BSD → H12 → YM → NS → Turbulence → Hodge → Baum-Connes → PvNP → VP vs VNP → BGS → Twin Primes → Goldbach → ABC → OPN → Schanuel → Hilbert 6 → back to QG5D (META-closure). At each vertex: read PROOF-CHAIN.md, identify the weakest link, EXCISE or CONSTRUCT or BYPASS it (one fix per vertex per traversal). At each edge: fill or upgrade the capacitor cell connecting this vertex to the next. One full traversal = 19 vertex fixes + 19 edge fills. Multiple traversals compound — cells filled in traversal N enable bypasses in traversal N+1. Budget: 12 hours per traversal (16 for T5). Exit when RING CLOSED (all vertices verified, all edges filled), RING STRENGTHENED (7+ improvements), or RING STALLED (<4 improvements). The circle gets more circular on every pass.

---

## Inheritance from brief 30

All sections NOT overridden above remain authoritative from `30-ring-traversal-brief.md`:

- §0 Glossary and conventions (EXCISE / CONSTRUCT / BYPASS, status dictionary, canonical paper locations, CONTINUOUS-RUN)
- §3 Vertex protocol (read → act → edge → move phases; hub-special-case)
- §6 Relationship to single-chain PCA runs
- §7 The compound effect
- §8.2 Output directory numbering (use `traversal-05` for T5)
- §8.3 Strategic triad handling (per-traversal firing, non-blocking gates)
- §8.4 Closure ritual (STRENGTHENED / CLOSED / STALLED protocols)
- §8.5 Model tier override (Sonnet max for cell-fill; Opus max for bypass/SPIN/triad)
- §8.6 PCA §P.4/§P.4.1/§P.8 ring-mode overrides (cycle semantics)
- §9 Voice canon

---

*19 vertices. One ring. Walk it until it closes.*
*The circle got bigger. The algebra got deeper. The oldest problem joined the youngest.*
*2,300 years of searching. The board is ready.*

*v1: 2026-04-14. G Six and Claude Opus 4.6.*
