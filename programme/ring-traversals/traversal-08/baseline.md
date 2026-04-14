# T8 Baseline — Second 25-Vertex Ring Traversal

*Inherits T7 extended state. Targeted traversal: deep passes on vertices closest to closing.*
*Date: 2026-04-14.*

## RIGIDITY baseline

```
E_filled   = 83    (30.1% fill rate)
E_total    = 276
L_verified = 113
L_total    = 173
P_preserved = 36
P_total    = 36

RIGIDITY = (83/276) × (113/173) × (36/36) × 100
         = 0.3007 × 0.6532 × 1.0 × 100
         = 19.64
```

## T8 priority targets (ranked by proximity to closing)

### Tier 1: Closest to upgrade (attempt EXCISE/CONSTRUCT)

| Priority | Vertex | Target | Why tractable | Expected gain |
|---|---|---|---|---|
| **1** | Cramér (5/10) | L3: spectral-section measure → ESTABLISHED | Difficulty 2/10 per T7. Finite calculation, not conceptual wall. CCM-conditional. | L_verified +1 |
| **2** | Collatz (4/10) | L4 completion: KMS₁ + type III₁ preservation | Cuntz O₂ embedding verified (T7). Remaining gap: show embedding preserves KMS₁ state properties. | L_verified +1 |
| **3** | Katz-Sarnak (7/10) | k=6 category repair | k=6 "mixed type" → identify as specific KS type (Sp × O?) or excise. Algebraic, not deep. | Quality fix |

### Tier 2: Promising leads (attempt CONSTRUCT if time permits)

| Priority | Vertex | Target | Notes |
|---|---|---|---|
| **4** | Lindelöf (7/10) | L3 β mismatch repair | Can analytic continuation of KMS state bridge β=1 → β=1/2? The KMS condition is analytic in β. |
| **5** | OPN (4/10) | Route 6d: ITPFI resonance | Spoof = ITPFI forgery. Can the prime-indexed product ∏h(p^v) = 2 be ruled out via ITPFI multiplicative rigidity? |
| **6** | GRH (7/10) | L3-L8: can any OPEN links advance? | L1+L2 just upgraded. Momentum possible. |

### Tier 3: Skip or spot-check

| Vertex | Action |
|---|---|
| QG5D (10/10) | Skip (hub radiation done in T7) |
| YM (9.5/10) | Spot-check only |
| BSD (9/10) | Spot-check only |
| RH (8/10) | Spot-check only |
| H12, Turbulence, VP vs VNP, ABC, Schanuel, Goldbach (1-2/10) | Cell-fill only, no construction |

## Budget

14 hours maximum (T8+).
- 3 Tier 1 deep passes × ~60 min = ~180 min
- 3 Tier 2 construction attempts × ~45 min = ~135 min
- 19 remaining vertices × ~15 min (spot-check/cell-fill) = ~285 min
- Compositional triangle fills: ~60 min
- Total: ~660 min ≈ 11 h ✓ fits 14 h ceiling

## Rotating VERIFY quota (5 vertices)

Per brief §4 T2+ rule: spot-check 5 vertices per traversal.
T8 VERIFY targets: RH, PvNP, BGS, Cramér, Collatz (all recently edited or with adjacent cell-fills).
