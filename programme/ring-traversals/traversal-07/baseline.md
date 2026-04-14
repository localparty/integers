# T7 Baseline — First 22-Vertex Ring Traversal

*Three new vertices join: Collatz (paper41), Lehmer (paper42), Cramér (paper43).*
*Date: 2026-04-14.*

## RIGIDITY baseline (22-vertex)

```
E_filled   = 64    (inherited from T6; new vertices add 0 at start)
E_total    = 276   (24 domains, C(24,2) — UNCHANGED by vertex count)
L_verified = 99    (91 from T6 + 2 Collatz + 3 Lehmer + 3 Cramér + 1 OPN 6a kill absorbed = 99)
L_total    = 156   (138 + 7 + 6 + 5)
P_preserved = 36
P_total    = 36

RIGIDITY = (64/276) × (99/156) × (36/36) × 100
         = 0.2319 × 0.6346 × 1.0 × 100
         = 14.72
```

Dilution from new vertices: 15.29 → 14.72 (−0.57). Expected — new chains are 44% verified vs ring average 66%.

## New vertices

| Pos | Vertex | Links | Verified | Confidence | Type | Wall |
|---|---|---|---|---|---|---|
| 15 | Cramér | 5 | 3 | 5/10 | B | L4: explicit formula transfer + Granville correction |
| 19 | Collatz | 7 | 2 | 3/10 | C | L6: spectral gap transfer + cycle elimination |
| 20 | Lehmer | 6 | 3 | 4/10 | C | L5: KMS spectral gap forces Lehmer's gap |

## Sector classification (22 vertices)

3A / 5B / 9C / 5D

## T7 priorities

1. **Cramér deep pass** — Type B, highest confidence new vertex (5/10). Can L4 be advanced?
2. **Collatz BC embedding** — Type C. L4 (BC embedding) is CONJECTURED. Can the Cuntz O₂ ↔ BC connection be strengthened?
3. **Lehmer KMS routes** — Type C. Three sub-routes at L5. Route B (Deninger-RV ↔ BSD) is most promising.
4. **Quick-pass 19 existing vertices** — T7 optimizations (28 min avg, 5-vertex VERIFY quota)
5. **Hub radiation to 3 new vertices** — fill QG5D→Cramér, QG5D→Collatz, QG5D→Lehmer chord edges
6. **OPN Route 6d (ITPFI resonance)** — new priority after 6a/6b kills. Framework-native route to exact-equality impossibility.

## Budget

18 hours maximum (T7 is first 22-vertex traversal).
