# W2-06: Flow Preserves the Small-Field Domain Ω_s (Lemma 1.2)

## Task
Write a rigorous proof memo establishing that the lattice gradient flow maps Balaban's small-field domain Ω_s into itself for all flow times t ≥ 0.

## Statement to prove
Let Ω_s denote Balaban's small-field domain at RG step k, defined by ‖A‖ < ε_k. If the initial configuration (V, A) lies in Ω_s, then the flowed configuration (V_t, A_t) lies in Ω_s for all t ≥ 0.

## Key inputs from Wave 1
- **W1-01** (flow well-posedness): The flow exists globally, V_t ∈ SU(N) for all t ≥ 0, and the action decreases monotonically: ∂_t S_KK[V_t] = -g₀² Σ_ℓ ‖∂_{V,ℓ} S_KK‖² ≤ 0.
- **W1-02** (flow contractivity): The flow converges to the KK vacuum (Q=0) or instanton (Q≠0, exponentially suppressed). The vacuum is isolated by the KK mass gap Δ₀^KK > 0 (Theorem 4).

## Proof strategy (from the lemma catalog)
1. Show S_KK[V_t, A_t] ≤ S_KK[V_0, A_0] for all t (monotone decrease from W1-01).
2. In Ω_s, the action is uniformly bounded: S_KK ≤ C·ε_k².
3. The quadratic coercivity of the action in Ω_s (from m_W > 0 at each RG step) gives ‖A_t‖² ≤ (2/m_W²)·S[V_t, A_t] ≤ (2/m_W²)·S[V_0, A_0] < ε_k².

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-01-flow-wellposedness.md` — Wave 1 output: monotone decrease
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-02-flow-contractivity.md` — Wave 1 output: contractivity + vacuum isolation
- `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md` — Theorem 4 (Δ₀^KK > 0, Section 4.4)
- `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` — Section 5.6 Part I for Balaban's small-field domain Ω_s definition and the fluctuation mass m_W
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/00-formal-argument.md` — context

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W2-06-preserves-small-field.md`

## Output format
Self-contained proof memo with: (1) Definition of Ω_s from Balaban's framework, (2) Statement of Lemma 1.2, (3) Proof in three steps (monotone decrease → action bound → coercivity), (4) Discussion of what happens at the boundary of Ω_s, (5) Explicit dependence of bounds on m_W, ε_k, and verification these are k-independent. Publication-quality mathematical writing. Reference W1-01 and W1-02 outputs explicitly.
