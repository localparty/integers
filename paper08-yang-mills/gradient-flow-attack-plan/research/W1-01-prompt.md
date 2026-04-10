# W1-01: Flow Well-Posedness on the KK-Enhanced Lattice (Lemma 1.1)

## Task
Write a rigorous proof memo establishing that the lattice Yang-Mills gradient flow equation on the KK-enhanced lattice gauge theory has a unique global solution for all flow times t >= 0.

## Statement to prove
The lattice gradient flow equation ∂_t V_t(ℓ) = -g₀²(∂_{V,ℓ} S_KK[V_t])V_t(ℓ), V_0(ℓ) = U(ℓ), on the KK-enhanced lattice of Section 4.1 of the mass gap preprint, has a unique global solution V_t(ℓ) ∈ SU(N) for all t ≥ 0 and all initial link configurations {U(ℓ)}.

## Key inputs
- The KK-enhanced action S_KK is a smooth function on compact SU(N)^|links|
- Picard-Lindelof theorem on compact manifolds: smooth vector field on compact Lie group → global existence and uniqueness
- Luscher 2010 (JHEP 08 (2010) 071) established this for the Wilson plaquette action
- Chatterjee 2018 (arXiv:1803.01950) in the probabilistic setting
- The KK enhancement (CP^{N-1} harmonics from mass gap preprint Section 4.1) modifies the coupling structure but not the compactness

## What to read
- `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md` — Section 4.1 for the KK-enhanced action
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/l1-gradient-flow-attack-plan.md` — Section 2.1-2.2 for the flow equation definition
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/00-formal-argument.md` — context

## What to write
1. Output file: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-01-flow-wellposedness.md`
2. Code (optional): `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/flow-wellposedness/`

## Output format
A self-contained proof memo with: Statement, Proof, References. Publication-quality mathematical writing. Include gauge covariance of the flow (if B_μ solves with initial data A_μ, then B_μ^g solves with initial data A_μ^g).
