# W1-02: Flow Contractivity on the KK Background (Lemma 1.5)

## Task
Write a rigorous proof memo establishing that the Yang-Mills gradient flow is contractive: the action decreases monotonically, and on the KK background the flow converges to the vacuum (Q=0 sector) or instanton (Q≠0, exponentially suppressed).

## Statement to prove
For any initial configuration U ∈ Ω_s, the Yang-Mills energy density E(t,x) := (1/4)G^a_{μν}(t,x)G^a_{μν}(t,x) satisfies E(t,x) ≤ E(0,x) for all t ≥ 0. On the KK background, the flow converges to the KK vacuum (Q=0) or self-dual instanton (Q≠0, suppressed by e^{-8π²|Q|/g²}).

## Key inputs
- The gradient flow is ∂_t B_μ = D_ν G_{νμ}, which is the negative gradient of S_YM
- ∂_t S_YM[B_t] = -2∫|D_ν G_{νμ}|² d⁴x ≤ 0 (monotone decrease)
- Feehan (arXiv:1409.1525): global existence + convergence near minimizers via Lojasiewicz-Simon
- Struwe, Calc. Var. PDE 2 (1994) 123: YM heat flow in 4D
- Theorem 4 of the mass gap preprint (Section 4.4, lines 749-769): Δ₀^KK > 0 means vacuum is isolated
- Paper 6, Theorem F.1: dilaton frozen, Casimir potential V(R)=c/R⁴ exact to all orders
- Paper 1, Appendix K, Theorem K.1: Epstein vanishing ensures perturbative finiteness

## What to read
- `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md` — Theorem 4
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/l1-gradient-flow-attack-plan.md` — Section 2.1
- `/Users/gsix/quantum-geometry-in-5d-latex/paper6/` — Theorem F.1 (frozen dilaton)

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-02-flow-contractivity.md`
2. Code: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/flow-contractivity/`

## Output format
Self-contained proof memo. Include: (a) monotone decrease proof, (b) vacuum isolation from Theorem 4, (c) instanton sector exponential suppression argument, (d) role of the frozen dilaton (Paper 6).
