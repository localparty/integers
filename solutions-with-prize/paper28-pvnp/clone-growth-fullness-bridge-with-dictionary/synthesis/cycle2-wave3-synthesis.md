# Synthesis Report — Cycles 1-2

## Quality Gate: BROKEN

## Critical Finding: Complementary Failure in 1.3.1

The Mal'cev partition proof (1.3.1) has two pillars:
- (A) T_f = id from Mal'cev identity m(x,y,y) = x
- (B) ||[y_k, a]|| → 0 from exponential decay of correlations

These work on COMPLEMENTARY Schaefer classes:
- XOR: (A) works, (B) fails
- Horn/dual-Horn/2-SAT: (B) works, (A) fails

On {0,1}, the only Mal'cev operation is XOR. XOR preserves only affine relations. The 1.3.1 proof covers 1 of 4 tractable Schaefer classes.

## Gap Inventory

| Gap | Node | Classification | Severity |
|---|---|---|---|
| 1.3.1-G1 | 1.3.1 | **GENUINE** | CRITICAL — Mal'cev covers only XOR-SAT |
| 1.3.1-G2 | 1.3.1 | CLOSABLE | XOR exception framing |
| OA1-G1 | OA1 | GENUINE | Non-constructive ρ_f |
| OA1-G2 | OA1 | GENUINE | Circular kernel bound |
| OA1-G3 | OA1 | GENUINE | Ill-defined Jones index |
| K-19 | Route A-LR | KILLED | CSP hypergraphs are expanders |

## Dependency Map

UA1 (SOUND) + UA2 (SOUND) → 1.3.1 (BROKEN: 1/4 coverage) → OA1 (3 GENUINE) → P≠NP

Chain broken at two independent points.

## Recommendation

Priority 1: Fix 1.3.1 coverage. Three approaches:
- (a) Horn/dual-Horn via amenability of semilattice automorphism groups
- (b) 2-SAT via congruence distributivity / majority-specific argument
- (c) Unified via Barto-Kozik cyclic terms (would close all 4 at once)

Priority 2: Close OA1 gaps independently (explicit construction for majority).

Kill criterion: If all Priority 1 approaches fail, assess for strategic pivot.
