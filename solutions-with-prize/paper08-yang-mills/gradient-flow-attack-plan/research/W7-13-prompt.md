# W7-13: Stress-Energy Tensor via Gradient Flow (Lemma 4.1 → Conjecture L.3)

## Task
Write a rigorous proof memo constructing the stress-energy tensor T_μν via Suzuki's gradient-flow formula and verifying all five sub-clauses of Conjecture L.3.

## Statement
Given [Tr F²]_R and [Tr(F_μρ F_ν^ρ)]_R from Phases 1-3, construct T_μν^R(x) = lim_{t→0⁺}[c₁(t)U_μν(t,x) + c₂(t)δ_μν E(t,x) + c₃(t)δ_μν⟨E(t)⟩·1] and verify L.3 sub-clauses (i)-(v).

## L.3 sub-clauses (from Appendix L, line 332)
- (i) Symmetry T_μν = T_νμ
- (ii) Gauge invariance
- (iii) Conservation ∂^μ T_μν = 0 (distributional Ward identity)
- (iv) H_OS = ∫ T₀₀ d³x (operator identification)
- (v) Trace anomaly T^μ_μ = (β(g)/2g)[Tr F²]_R

## Already unconditional (from preprint)
- H_OS ≥ 0 with H_OS Ω = 0 (Section 5.7, OS2, lines 2321-2372)
- Conservation at Schwinger function level (Section 5.7(f))

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W5-10-cauchy-estimate-and-extraction.md` — [Tr F²]_R exists
- `/Users/gsix/yang-mills/preprint/sections/L-clay-conjectures.md` — Conjecture L.3 exact text
- `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` — Section 5.7 (OS axioms, H_OS ≥ 0)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/l1-gradient-flow-attack-plan.md` — Section 4.2 (Suzuki formula, Ward identities, trace anomaly)

## What to write
Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W7-13-stress-tensor.md`

## Output format
(1) Suzuki formula statement with coefficients c₁, c₂, c₃, (2) each sub-clause verified separately with proof, (3) references to Del Debbio-Patella-Rago (JHEP 11 (2013) 212) for Ward identity, Collins-Duncan-Joglekar (PRD 16 (1977) 438) for trace anomaly, Spiridonov-Chetyrkin for the identity, (4) explicit statement of what is unconditional vs conditional on L.1.
