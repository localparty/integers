# CONCERN — Adaptive Circuit Caveat in Route A

**Raised by:** W1-4 Author (Route A), Self-suspicion #1
**Cycle:** 1
**Node:** 2 (Route A)

## The issue

The Route A spectral gap → circuit depth argument gives a clean exponential lower bound for **non-adaptive** circuits (NC hierarchy). For **adaptive** circuits (with classical feedback / measurements), the 2^D branching factor weakens the overlap bound:

- Non-adaptive: D ≥ exp(δn/(kd))  — exponential ✓
- Adaptive: D ≥ Ω(n/log n)  — barely polynomial ✗

## Why it matters

P vs NP is about Turing machines (adaptive algorithms), not just circuits. A proof that only works for non-adaptive circuits proves P/poly ≠ NP (which is weaker but still major), not P ≠ NP.

## Proposed fix

The Author identified that the topological confinement structure from A5-AREA-LAW should restore the exponential bound for adaptive algorithms: holonomy is topological, so adaptive measurements don't help with cycle unwinding. This needs full formalization.

## Classification

**CLOSABLE** — the path via RULE9-GATE × A5-AREA-LAW topological counting is clear. Not a new research programme, but a non-trivial formalization step.

## Action

Assign an Author to formalize the adaptive-circuit extension in cycle 2, using RULE9-GATE and A5-AREA-LAW as the tools.
