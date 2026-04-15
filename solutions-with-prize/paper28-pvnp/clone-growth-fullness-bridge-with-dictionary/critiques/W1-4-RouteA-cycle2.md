# Critic Verdict: Route A (Node 2) — WEAKENED

## Two routes distinguished

The Critic identified TWO distinct routes being conflated:

### Route A-LR (Lieb-Robinson circuit depth): **BROKEN**
- CSP constraint hypergraphs are NOT geometric lattices — they're expander-like (diameter O(log n))
- Lieb-Robinson on expanders gives O(log n) propagation delay → polynomial depth, NOT exponential
- The Author's Theorems 3.1, 3.2, 4.1, 4.2 have no backing derivation
- The overlap bound formula assumes lattice geometry that doesn't exist
- If non-adaptive bound is polynomial, adaptive bound is also polynomial → P ≠ NP NOT proved

### Route A-Bypass (approximately central sequences + HM): WEAKENED but LIVE
- Doesn't use Lieb-Robinson at all
- Goes: polymorphisms → clone operators → approximately central sequences → spectral gap obstruction
- Two remaining gaps: Alpha (concentration of polymorphism action), Beta (strong ergodicity for NPC)
- Both CLOSABLE in principle

## Line-by-line

| # | Check | Classification |
|---|---|---|
| 1 | Computational Lieb-Robinson | **GENUINE** (wrong geometry — hypergraphs not lattices) |
| 2 | Overlap bound | **GENUINE** (not derived, relies on broken Lieb-Robinson) |
| 3 | Adaptive circuit caveat | **GENUINE** (polynomial non-adaptive → polynomial adaptive) |
| 4 | Uniform spectral gap | CLOSABLE (modular gap IS language-level) |
| 5 | Circularity | SOUND |
| 6 | Barriers bypass | CLOSABLE (all three) |
| 7 | Kill compliance | SOUND (K-3), CLOSABLE (K-5) |

## Structural diagnosis

The fundamental error: treating CSP instances as if they live on geometric lattices. They don't. Random k-SAT at clause ratio α has a constraint hypergraph that is an expander, not a lattice. The Lieb-Robinson velocity gives full propagation in O(log n) time, yielding only polynomial depth bounds.

## Recommendation

KILL the Lieb-Robinson route. PROMOTE the bypass route (approximately central sequences → Houdayer-Marrakchi). The bypass doesn't need geometric locality — it works at the language level through the modular spectral gap.
