# Research 29 Summary — Von Neumann-Wigner + Slepian

*Status: COMPLETED (research note)*
*Type: Lead (feasibility 6/10 — HIGHEST)*
*Date: 2026-04-10*

---

## Result

VNW no-crossing theorem verified for QW_λ^{N,+}:
- Real symmetric ✓
- Analytic in λ ✓ (piecewise, with care at λ = √p)
- Single symmetry class (even sector) ✓

Combined with Slepian (PW has simple eigenvalues), simplicity
propagates from the prolate limit to all λ at each fixed N.

## Two gaps identified

**Gap A (arithmetic exclusion):** VNW says crossings are
"non-generic" (codimension 2). Need to promote to "impossible."
Requires arithmetic argument that the specific QW entries cannot
produce the codim-2 coincidence.

**Gap B (quantitative Slepian convergence):** Show
‖QW^{N,+} − PW‖ < gap(PW)/2 for N ≥ N₀. Then simplicity
transfers from Slepian directly. This is the MORE TRACTABLE gap.
It's a concrete operator-norm estimate, not a transcendence question.

## Recommended next step

Attack Gap B via operator-norm bounds. This is Lead A in
strategy/17.

## Files
- Research note: research/29-lead-vnw-slepian-simplicity.md
