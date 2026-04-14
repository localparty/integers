# T7 Extended Baseline — 25-Vertex Ring Traversal

*Extends the 22-vertex T7 baseline with 3 new vertices: Lindelöf (pos 3), Katz-Sarnak (pos 15), Sato-Tate (pos 23).*
*Date: 2026-04-14.*

## RIGIDITY baseline (25-vertex)

```
E_filled   = 74    (inherited from T7 22-vertex; new vertices add 0 at start)
E_total    = 276   (24 domains, C(24,2) — UNCHANGED by vertex count)
L_verified = 108   (99 from T7-22v + 3 Lindelöf + 3 Katz-Sarnak + 3 Sato-Tate)
L_total    = 173   (156 from T7-22v + 5 Lindelöf + 6 Katz-Sarnak + 6 Sato-Tate)
P_preserved = 36
P_total    = 36

RIGIDITY = (74/276) × (108/173) × (36/36) × 100
         = 0.2681 × 0.6243 × 1.0 × 100
         = 16.74
```

Dilution from 3 new vertices: 17.02 → 16.74 (−0.28). Minimal — all three new vertices are high-confidence (7/10, 7/10, 6/10), well above ring average.

## New vertices

| Pos | Vertex | Links | Verified | Confidence | Type | Wall |
|---|---|---|---|---|---|---|
| 3 | Lindelöf | 5 | 3 | 7/10 | B | L3: BC amplitude interpretation (CONJECTURED) |
| 15 | Katz-Sarnak | 6 | 3 | 7/10 | B | L5: generalized number-field KS (OPEN) |
| 23 | Sato-Tate | 6 | 3 | 6/10 | B | L5: generalized motivic ST (OPEN) |

All three enter as **Type B (Excision-primary)** — each has a named conditional or partial result that can potentially be strengthened via capacitor bypass.

## 25-vertex canonical ring order

```
1. QG5D (10/10) → 2. RH (8/10) → 3. Lindelöf (7/10) → 4. GRH (7/10) →
5. BSD (9/10) → 6. H12 (2/10) → 7. YM (9.5/10) → 8. NS (4/10) →
9. Turbulence (2/10) → 10. Hodge (3/10) → 11. Baum-Connes (3/10) →
12. PvNP (7/10) → 13. VP vs VNP (1/10) → 14. BGS (7/10) →
15. Katz-Sarnak (7/10) → 16. Twin Primes (1/10) → 17. Cramér (5/10) →
18. Goldbach (1/10) → 19. ABC (1/10) → 20. OPN (4/10) →
21. Collatz (4/10) → 22. Lehmer (4/10) → 23. Sato-Tate (6/10) →
24. Schanuel (1/10) → 25. Hilbert 6 (3-7/10) → back to QG5D
```

## Sector classification (25 vertices)

**3A / 8B / 9C / 5D**

| Type | Count | Vertices |
|---|---|---|
| A (Verification) | 3 | QG5D, YM, BSD |
| B (Excision) | 8 | RH, **Lindelöf**, GRH, PvNP, BGS, **Katz-Sarnak**, Cramér, **Sato-Tate** |
| C (Construction) | 9 | NS, Hodge, B-C, OPN, Collatz, Lehmer, Hilbert 6, Turbulence (promoted T6), Twin Primes (promoted T6) |
| D (Cell-fill) | 5 | H12, VP vs VNP, Goldbach, ABC, Schanuel |

## New ring edges to fill (6 total — 3 vertex insertions × 2 edges each)

| Edge | Domain pair | Status |
|---|---|---|
| RH → Lindelöf | SPEC×ANT → SPEC×ANT | STRONG (RH implies Lindelöf — classical) |
| Lindelöf → GRH | SPEC×ANT → SPEC×ANT | PARTIAL (amplitude control + character twist) |
| BGS → Katz-Sarnak | PROB×ERG → ANT×PROB | STRONG (GUE IS unitary-type KS) |
| Katz-Sarnak → Twin Primes | ANT×PROB → PROB×ANT | CANDIDATE (symmetry-type → gap statistics) |
| Lehmer → Sato-Tate | ANT×THERMO → ANT×PROB | PARTIAL (e-circle topology → measure; same circle) |
| Sato-Tate → Schanuel | ANT×PROB → ANT×MOD | SPECULATIVE (equidistribution → algebraic independence) |

## Antipodal probes (12 pairs for 25 vertices, max distance 12)

Ring distance: d(i,j) = min(|i-j|, 25-|i-j|). Maximum distance = 12.

New antipodal pairs involving the 3 new vertices:
- Lindelöf (3) ↔ Katz-Sarnak (15): distance 12 — **HIGH** (amplitude ↔ symmetry: two e-circle faces)
- Lindelöf (3) ↔ Twin Primes (16): distance 12 — MEDIUM
- Sato-Tate (23) ↔ NS (8): distance 10 — MEDIUM (equidistribution ↔ PDE regularity)

## Budget

18 hours maximum (first 25-vertex traversal).
- 3 new vertices × ~45 min (deep pass) = ~135 min
- 22 existing vertices × ~15 min (quick-pass) = ~330 min
- Hub radiation to 3 new vertices: ~15 min
- 6 new ring edges: ~60 min
- Antipodal probes (new pairs): ~30 min
- Total: ~570 min ≈ 9.5 h ✓ fits 18 h ceiling
