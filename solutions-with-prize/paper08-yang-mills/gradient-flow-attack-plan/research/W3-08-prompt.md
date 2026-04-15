# W3-08: Flowed Polymer Activity Decay + K-Uniformity (Lemmas 1.3 + 1.4)

## Task
Write a rigorous proof memo establishing that the flowed polymer activities satisfy exponential decay with constant κ(t) ≥ κ_B > 0, and that all constants are K-uniform (independent of the bare theory index K). Lemma 1.4 is an immediate corollary of 1.3, so they are combined.

## Statements to prove

**Lemma 1.3.** For each polymer X in Balaban's expansion at RG scale k, the flowed polymer activity satisfies |K_k^{(t)}(X, V)| ≤ e^{-κ(t)|X|}, κ(t) ≥ κ_B > 0, for all t ≥ 0 and all k, where κ_B is Balaban's polymer decay constant (CMP 109, Theorem 1).

**Lemma 1.4.** The constants κ(t), C(t) in Lemma 1.3 are K-uniform: they depend on N, (R, r_3), and t, but not on the bare theory index K.

## Key inputs from previous waves

### From Wave 1:
- **W1-01** (flow well-posedness): V_t ∈ SU(N) for all t, action monotone decreasing
- **W1-02** (flow contractivity): flow drives toward vacuum, Lyapunov function
- **W1-05** (analyticity in t): Balaban analyticity (B1) with k-independent radius ρ = min(κ/2d, m_W·a/2C_D, r_proj(N))

### From Wave 2:
- **W2-06** (preserves Ω_s): flow maps Ω_s into itself for all t ≥ 0, with k-independent bounds

### From mass gap preprint:
- **Lemma M.1.2** (Appendix M, line 77): unflowed polymer activities satisfy |K_k^{(K)}(X,V)| ≤ e^{-κ_B|X|} with κ_B independent of both k and K
- **Lemma M.1.1** (Appendix M, line 20): cluster expansion converges with physical rate κ_cl^phys = m_1/6, K-independent
- **Corollary M.1.3** (Appendix M, line 132): hypotheses (H1)-(H2) of the Cluster-Balaban Handoff Lemma satisfied with K-uniform constants
- **Handoff Lemma** (Section 5.4.5, lines 854-933): hypotheses (H1), (H2), (H3) and their K-uniformity

### From Balaban's papers:
- **CMP 109, Theorem 1**: polymer expansion convergence, κ k-independent
- **CMP 95, Proposition 1.2**: propagator decay |G_k(x,y)| ≤ O(1)e^{-δ₀|x-y|}, δ₀ depends on d only
- KK mode n propagator: G_k^{(n)} = (-D² + m_W² + m_n²)⁻¹ with decay rate δ₀ + m_n > δ₀

## Proof strategy

**For Lemma 1.3:**
1. Define flowed polymer activities: K_k^{(t)}(X,V) := K_k(X, V_t) where V_t is the gradient-flow evolution of V.
2. By Lemma 1.2 (W2-06), V_t ∈ Ω_s, so K_k(X, V_t) is in the domain of Balaban's estimates.
3. By the unflowed estimate (Lemma M.1.2), |K_k(X, V_t)| ≤ e^{-κ_B|X|}.
4. The flow improves decay: κ(t) ≥ κ_B because the flow drives toward smaller field values.

**For Lemma 1.4:**
- K-uniformity inherited from unflowed K-uniformity (Lemma M.1.2, Corollary M.1.3).
- Flow introduces no K-dependent parameters (deterministic ODE, coefficients from S_KK independent of g₀(K) at t > 0).

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W2-06-preserves-small-field.md` — Wave 2 output
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-05-analyticity-in-t.md` — Balaban (B1) details
- `/Users/gsix/yang-mills/preprint/sections/M-gap-closures-r00.md` — Appendix M: Lemmas M.1.1, M.1.2, Corollary M.1.3
- `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` — Section 5.4.5 (Handoff Lemma) and Section 5.6 Part I (B1)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/00-formal-argument.md` — Section 3.1 (Estimate 1)

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W3-08-polymer-decay.md`

## Output format
Self-contained proof memo: (1) Define flowed polymer activities precisely, (2) Prove Lemma 1.3 using W2-06 + M.1.2, (3) Prove Lemma 1.4 using Corollary M.1.3, (4) Discuss how KK mass tower strengthens decay (additional m_n in exponent), (5) Verify all constants are (k,K)-uniform with explicit table. Reference all Wave 1-2 outputs and preprint appendices. Publication-quality.
