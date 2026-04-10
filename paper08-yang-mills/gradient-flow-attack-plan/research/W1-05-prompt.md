# W1-05: Analyticity of Flowed Effective Action in t (Lemma 3.1)

## Task
Write a rigorous proof memo establishing that the flowed Balaban effective action S_k^eff[V, A_t], viewed as a function of flow time t, is analytic in t with k-independent radius r_t > 0. This is the most substantial Wave 1 task and a key input to the core estimate (Lemma 3.7).

## Statement to prove
The flowed Balaban effective action S_k^eff[V, A_t] is analytic in t for |t| < r_t with r_t > 0 independent of k. Consequently, the rescaled correlator F(t) = S_{2,t}^c(x,y)/c_1(t)² is analytic in t for |t| < r_t.

## The composition argument (three ingredients)

### Ingredient (a): Balaban analyticity (B1)
Section 5.6, Part I (lines 1577-1664) of the mass gap preprint establishes: S_k^eff[V] is analytic in the block link variables {V_ℓ} with k-independent radius ρ = min(κ/2d, m_W·a/2C_D, r_proj(N)) > 0.

Four operations preserve analyticity (Step (b), lines 1605-1632):
(i) Background evaluation — polynomial composition
(ii) Saddle point via G_k(V) = (-D²[V] + m_W²)⁻¹ — analytic inversion (CMP 95 Prop. 1.2)
(iii) Gaussian integration — convergent trace-log expansion
(iv) Mayer resummation — Weierstrass M-test (CMP 109 Sec. 4)

k-independence from three constraints all being k-independent (lines 1654-1657).

### Ingredient (b): ODE analyticity
The lattice flow ODE ∂_t V_t = F(V_t) with smooth (polynomial) F on compact SU(N) has analytic solution in t by Cauchy-Kowalevski. Radius r_ODE depends on Lipschitz constant of F, not on initial condition within Ω_s.

### Ingredient (c): Heat kernel entirety
e^{-tp²} is entire in t. On M⁴ × S¹, the heat kernel factorizes (Paper 1, Appendix S, Section S.3.1).

### Composition
t →[ODE]→ V_t →[(B1)]→ S_k^eff[V_t] is analytic in t. Radius: r_t = min(r_ODE, ρ/L_F) where L_F is the k-independent Lipschitz constant.

## Critical consequence
Analyticity in t means the small-flow-time expansion CONVERGES (not merely asymptotic). This closes Gap G1 of the attack plan.

## What to read
- `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` — Section 5.6 Part I (lines 1577-1664) for (B1)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/30-appendix-s-finiteness-theorem.md` — Section S.3.1
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/03-the-cauchy-estimate-for-the-rescaled-correlator.md` — Step 2

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-05-analyticity-in-t.md`
2. Code: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/analyticity-in-t/` — Compute: (a) explicit value of ρ for N=2,3 using the formula min(κ/2d, m_W·a/2C_D, r_proj(N)) with known Balaban constants, (b) estimate L_F = sup|∂_V S_W| on Ω_s for N=3, (c) compute r_t = ρ/L_F numerically

## Output format
Self-contained proof memo with: (1) The three ingredients stated precisely, (2) The composition theorem with explicit radius, (3) Verification that r_t is k-independent, (4) Discussion of the removable singularity extension to t=0 (given F(0) finite from Theorem K.1), (5) Numerical estimate of r_t for N=3. Publication-quality mathematical writing.
