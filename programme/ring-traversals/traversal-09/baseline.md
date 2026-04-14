# T9 Baseline — Third 25-Vertex Ring Traversal (Deep)

*Per brief §4 multi-traversal strategy: T9 is the "deep" traversal — extra time on the 2-3 hardest remaining walls.*
*Date: 2026-04-14.*

## RIGIDITY baseline

```
E_filled   = 93    (33.7% fill rate)
L_verified = 114
L_total    = 173
RIGIDITY   = 22.21
```

## T9 strategy: push toward moderate rigidity (25+)

To reach RIGIDITY 25, need either:
- E_filled = 93 → ~105 (+12 cells) with L unchanged, OR
- L_verified = 114 → ~120 (+6 links) with E unchanged, OR
- Some combination

**The L factor is the bottleneck.** At 65.9%, it drags the formula. Each VERIFIED link adds ~0.38% to L_verified/L_total → ~0.13 to RIGIDITY. Each filled cell adds ~0.36% to E_filled/E_total → ~0.08 to RIGIDITY. **Link closures are 1.6× more impactful than cell fills.**

## T9 priority targets (wall-specific)

| Target | Current | Goal | Impact |
|---|---|---|---|
| Cramér L3 residual | PARTIAL | ESTABLISHED | L_verified +1, RIGIDITY +0.13 |
| Lindelöf Route C verification | PROVED-WITH-CONTINUATION | Critic verdict | Quality (sign check) |
| GRH L3-L5 | OPEN | Any advance | L_verified +1 to +3 |
| OPN Route 6d | OPEN | PARTIAL or advance | L_verified +1 |

## Budget

14 hours maximum.
- 4 deep passes: ~240 min
- Edge fills: ~60 min
- Remaining vertices spot-check: ~180 min
- Total: ~480 min ≈ 8 h ✓
