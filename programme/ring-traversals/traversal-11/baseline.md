# T11 Baseline — Fifth 25-Vertex Ring Traversal

*T11 focuses on edge-filling (T10 had 0 new cells) and GRH L5c pilot.*
*Date: 2026-04-14.*

## RIGIDITY baseline

```
E_filled   = 98    (35.5% fill rate)
L_verified = 116
L_total    = 173
RIGIDITY   = 23.81
```

## T11 strategy: compensate for T10's edge-fill gap

T10 moved the L factor (+2 verified) but E factor stayed flat. T11 should compensate by filling cells.

Priorities:
1. **GRH L5c pilot**: If the character-twisted Fourier cancellation works for χ=(-4/·), GRH L5 chain elements (L5a, L5b, L5d) can follow per T9 analysis. Potential +3 to L_verified if it cascades.
2. **Compositional triangles**: T9's 5 sparse-vertex chord fills opened new triangles. Each closed triangle = +1 new cell.
3. **Chord edges between distant vertices**: Look for high-value connections across the ring.

## Projected T11 gains

If GRH L5c + L6/L7/L8 cascade closes: +3-4 L_verified, RIGIDITY 23.81 → 25.0+
If only compositional fills succeed: +4-5 cells, RIGIDITY 23.81 → 24.3

Target: cross RIGIDITY 25 (the moderate-rigidity threshold).

## Budget

14 hours maximum.
