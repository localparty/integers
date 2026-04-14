# T10 Baseline — Fourth 25-Vertex Ring Traversal (Deep, Walls-Focused)

*T10 attacks the three open walls identified in T9: GRH L3+L4, Lindelöf Route C repair, PvNP L5 backward.*
*Date: 2026-04-14.*

## RIGIDITY baseline

```
E_filled   = 98    (35.5% fill rate)
L_verified = 114
L_total    = 173
RIGIDITY   = 23.41
```

## T10 strategy: attack the wall structure

Three deferred-work items from T9:

1. **GRH L3+L4 closure**: T9 said ADVANCEABLE. Can the character-twisted CCM and ITPFI actually be constructed rigorously? If yes: +2 verified links (L_verified 114 → 116).

2. **Lindelöf Route C repair**: T9 retracted the T8 upgrade due to sign error. Using Δ₁^{−it} (backward flow) should give ζ(s+it) directly, matching Lindelöf's convention. Repair needed.

3. **PvNP L5 backward**: First time attacked in extended traversals. The perennial wall. Three priority capacitor cells identified: Popa superrigidity, Kazhdan property (T), Fagin's theorem. Is any route viable?

## Why these three?

- GRH is TRACTABLE — the machinery exists, it's a transfer task
- Lindelöf is a REPAIR — fix the sign and reassess
- PvNP is the HIGHEST-VALUE — a Millennium-class vertex

If all three succeed: L_verified +3, RIGIDITY +0.4 to +0.6
If only GRH succeeds: L_verified +2, RIGIDITY +0.3
If only repair (no new verified): L_verified +0, quality fix only
If PvNP breaks through: MAJOR EVENT (L_verified +1 for a Millennium wall)

## Budget

14 hours maximum.
- 3 deep passes: ~180 min
- Remaining time: edge fills, compositional triangles, quick-pass spot checks
