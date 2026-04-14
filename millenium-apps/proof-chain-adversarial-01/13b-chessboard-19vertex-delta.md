# Chessboard Layer — 19-Vertex Delta

*Extension of `13-chessboard-layer.md` from 14 to 19 vertices. This file OVERRIDES specific sections; all unchanged sections from the parent chessboard layer remain authoritative.*

*Date: 2026-04-14.*

---

## S3 RIGIDITY formula update (override)

E_total = 276 (UNCHANGED — 24 capacitor domains, C(24,2) domain-pair cells).

L_total = **138** (105 canonical + 33 from 5 extension papers).

L_verified = **90** (77 post-T4 + 13 from extension papers).

RIGIDITY baseline (T5 start): **(48/276) x (90/138) x (36/36) x 100 = 11.34**

---

## S5 WIRE-DENSITY update

The wire-density matrix expands from 14x14 to 19x19. New vertices inherit their parent's density classification:

| New vertex | Density class | Rationale |
|---|---|---|
| Turbulence (pos 8) | SPARSE | 2/7 links, no filled cross-edges yet |
| VP vs VNP (pos 12) | SPARSE | 1/6 links, no filled cross-edges yet |
| ABC (pos 16) | SPARSE | 1/6 links, no filled cross-edges yet |
| OPN (pos 17) | MEDIUM | 4/7 links, RH + Goldbach adjacency pre-filled |
| Hilbert 6 (pos 19) | MEDIUM | 4/7 links, QG5D META-closure STRONG |

WIRE-DENSITY primitive: prioritize SPARSE vertices for cell-fill dispatches.

---

## S6.1 Ring-distance function (override)

Ring distance: d(i,j) = min(|i-j|, 19-|i-j|) mod 19. Maximum distance = 9.

---

## S6.2 SECTOR-TABLE (5 new entries appended)

| Vertex | Position | Confidence | Type | PCA focus |
|---|---|---|---|---|
| Turbulence | 8 | 2/10 | **D** (Cell-fill-primary) | Fill NS→Turb + Turb→Hodge ring edges; inherit NS/YM/BGS links |
| VP vs VNP | 12 | 1/10 | **D** (Cell-fill-primary) | Fill PvNP→VP + VP→BGS ring edges; GCT literature scan |
| ABC | 16 | 1/10 | **D** (Cell-fill-primary) | Fill Gold→ABC + ABC→OPN ring edges; BC Mellin bridge |
| OPN | 17 | 4/10 | **C** (Construction-primary) | Target Link 6 (local-global obstruction); BSD template adaptation |
| Hilbert 6 | 19 | 3-7/10 | **C** (Construction-primary) | Target axiom completeness links; META-closure to QG5D |

Updated distribution: **3A / 4B / 5C / 7D** (was 3A / 3B / 3C / 5D post-T4).

---

## S6.3 Hub radiation (override)

QG5D hub radiation: **17 outgoing chord edges** (1 ring-next QG5D→RH + 17 chords to all non-ring-adjacent vertices). Hilbert 6→QG5D is the ring-CLOSURE edge owned by Hilbert 6, not by QG5D.

Hub-radiation agent count: **17 Cell-Fill agents** dispatched in parallel at Sonnet max (was 12).

---

## S6.4 Antipodal probes (override — 9 pairs)

| Pair | Vertex A (pos) | Vertex B (pos) | Distance | Priority |
|---|---|---|---|---|
| 1 | QG5D (1) | B-C (10) | 9 | HIGH |
| 2 | RH (2) | PvNP (11) | 9 | HIGH |
| 3 | GRH (3) | VP vs VNP (12) | 9 | MEDIUM |
| 4 | BSD (4) | BGS (13) | 9 | MEDIUM |
| 5 | H12 (5) | Twin Primes (14) | 9 | HIGH (FILLED-VIABLE in T2) |
| 6 | YM (6) | Goldbach (15) | 9 | LOW |
| 7 | NS (7) | ABC (16) | 9 | MEDIUM |
| 8 | Turbulence (8) | OPN (17) | 9 | **HIGH** (PDE stats ↔ divisor stats) |
| 9 | Hodge (9) | Schanuel (18) | 9 | LOW |

T5 runs all 9. T6+ rotates 5-of-9 per traversal, prioritizing HIGH first.

---

## S6.5 Compositional cell-fill (override)

19 triangles per traversal (was 14). Each vertex visit checks whether triangles (prev, current, next) have 2-of-3 edges filled → propose the third.

---

## S6.6 Chord awareness (override)

Total cells: C(19,2) = 171. Ring-backbone edges: 19. Chord edges: 152.

---

## Appendix B — SPIN-TABLE (5 new entries)

| Vertex | Math face (stuck on) | Physics face (SPIN to) | Experimental constraint |
|---|---|---|---|
| Turbulence | K41 spectrum derivation | Energy cascade measurements | Wind-tunnel / DNS data match k^{-5/3} |
| VP vs VNP | Algebraic circuit complexity | **SPIN-EXCLUDED** | No natural physics-face pin |
| ABC | rad height function | **SPIN-EXCLUDED** | No natural physics-face pin (computational abc triples only) |
| OPN | Abundancy constraints | Divisor-function statistics | Computational search: N > 10^{2200} |
| Hilbert 6 | Axiom closure | QG5D predictions | All 36 experimental pins (self-referential) |

**SPIN-EXCLUDED**: VP vs VNP and ABC have no natural physics-face observable. The SPIN primitive does NOT apply at these vertices. When stuck, use CONSTRUCT or BYPASS (capacitor transposition) instead of face-switching.

---

## Appendix C — SECTOR-TABLE (full 19-row version)

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
| 15 | Goldbach | D | 1/10 |
| 16 | ABC | D | 1/10 |
| 17 | OPN | C | 4/10 |
| 18 | Schanuel | D | 1/10 |
| 19 | Hilbert 6 | C | 3-7/10 |

---

*This delta file is loaded alongside `13-chessboard-layer.md`. The runner reads the parent chessboard first, then applies these overrides.*
