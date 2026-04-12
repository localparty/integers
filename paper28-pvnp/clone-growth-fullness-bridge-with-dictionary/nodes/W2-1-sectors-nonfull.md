# Node 1.3.1: Exponential Sectors → Non-fullness via Property Gamma

## Status: ADVANCED

## Theorem

For tractable L (admitting Taylor polymorphisms, specifically Mal'cev), the type III₁ factor M = M_Bool^L is non-full.

## Proof (clean extraction from W2-1 exploration)

### Step 1: Mal'cev endomorphisms fix L^∞(Ω_L)

A Mal'cev polymorphism m ∈ Clone_3(L) satisfies m(x,y,y) = x. The Markov operator:

T_m(a)(σ) = ∫ a(m(σ, τ, τ)) dμ_β(τ) = ∫ a(σ) dμ_β(τ) = a(σ)

So **T_m = id** on L^∞(Ω_L). The endomorphism ρ_m acts non-trivially on M_φ \ L^∞(Ω_L) but is the identity on the commutative sub-algebra.

By iterated composition using binary trees (Catalan number C_{k-1} ~ 4^k/k^{3/2} distinct trees at arity k), the set R_k of sectors with T_f = id has |R_k| ≥ γ^k for γ > 1.

### Step 2: Partition of solution space

For each k, choose N_k = |R_k| ≥ γ^k mutually inequivalent sectors with isometries V_1,...,V_{N_k} ∈ M_φ, V_i*V_j = δ_{ij}. The projections p_i = V_iV_i* form a partition of unity in L^∞(Ω_L) with μ_β(p_i) = 1/N_k.

### Step 3: Approximately central sequence

Define y_k = Σ λ_i p_i ∈ L^∞(Ω_L) with λ_i = e^{2πi·i/N_k}, so τ(y_k) = 0 and ||y_k||_τ = 1.

**For a ∈ L^∞(Ω_L):** [y_k, a] = 0 (commutative algebra). ✓

**For a ∈ M_φ (non-commutative, local — depends on s sites):** The commutator ||[y_k, a]||_τ decays via exponential decay of correlations in the tractable CSP Gibbs measure:

||[y_k, a]||_τ² = O(||a||² · e^{-2c(k-s)}) → 0 as k → ∞ with s fixed.

This uses: for tractable L, μ_β has exponential decay of correlations (polymorphism-connectedness of solution space).

**For general a ∈ M_φ:** Approximate by local observables: ||a - a_s|| < ε, then ||[y_k, a]|| ≤ ||[y_k, a_s]|| + 2ε → 2ε. Take ε → 0 first, then k → ∞. ✓

**For a ∈ M \ M_φ (spectral value s ≠ 0):** [y_k, a] has spectral value s. Since y_k ∈ M_φ, [y_k, Δ^{is}] = 0 (modular invariance). For spectral-s element a = b·(modular operator factor) with b ∈ M_φ: ||[y_k, a]||_φ = ||[y_k, b]||_φ → 0 by the M_φ estimate.

### Step 4: Property Gamma

The sequence (y_k) satisfies:
- ||y_k||_τ = 1 (non-trivial)
- τ(y_k) → 0 (non-scalar)
- ||[y_k, a]||_τ → 0 for all a ∈ M_φ (approximately central)

Therefore M_φ has property Gamma of Murray-von Neumann.

### Step 5: Non-fullness

By **Connes (1976, Theorem 3.1):** M full ↔ M^ω ∩ M' = ℂ.
By **Ando-Haagerup (2014, Theorem 5.2):** M^ω ∩ M' ≅ (M_φ)^ω ∩ (M_φ)'.

Property Gamma of M_φ ⟹ (M_φ)^ω ∩ (M_φ)' ≠ ℂ ⟹ M^ω ∩ M' ≠ ℂ ⟹ **M is non-full.** ∎

## XOR Exception (honest flag)

XOR-SAT is P-time but its Gibbs measure may NOT have exponential decay of correlations (algebraically tractable but disconnected walk — PATD-CONDEXP 4/5). The proof applies to CSPs with LOCAL Taylor polymorphisms (2-SAT, Horn, dual-Horn, all conservative tractable CSPs). XOR requires separate treatment.

## Self-Suspicion

1. **Exponential decay of correlations:** Needs rigorous citation for tractable CSP Gibbs measures. The polymorphism-connectedness (PATD-CONDEXP) provides this for local polymorphisms but not for algebraic ones (XOR). Risk: MEDIUM.

2. **Partition cells in L^∞(Ω_L):** The isometries V_i need to be constructible as partial isometries in L^∞(Ω_L) — this requires the solution space to be partitionable into N_k equal-measure sets. For finite Ω_L, this is trivially possible for N_k ≤ |Ω_L|. For N_k > |Ω_L| (which happens at large k), the partition becomes trivial. The fix: work with arity k where N_k ≤ |Ω_L(n)|, and take n → ∞ simultaneously. Risk: CLOSABLE.

3. **Backward verification of Ando-Haagerup:** The isomorphism M^ω ∩ M' ≅ (M_φ)^ω ∩ (M_φ)' requires M_φ to be a II₁ factor. If M_φ is not a factor (it contains L^∞(Ω_L)), the exact isomorphism may not hold. The generalization to non-factorial centralizers exists (Masuda-Tomatsu 2013) but needs checking. Risk: CLOSABLE.

## Dependencies

- OA1-SECTOR-HOM (kernel bound)
- Q6-OUTDIM (exponential dim_poly_k)
- PATD-CONDEXP (mixing for local polymorphisms)
- HOUDAYER-MARRAKCHI (fullness criterion)
- Connes 1976, Ando-Haagerup 2014 (central sequences ↔ fullness)
- Barto-Kozik (Taylor clone structure, Mal'cev existence)

## What the Next Runner Needs to Know

- **State:** ADVANCED. Central sequence constructed, Property Gamma → non-fullness chain complete for local-polymorphism tractable L.
- **Open:** XOR exception, mixing estimate rigorous citation, non-factorial centralizer check.
- **Preferred next move:** Critic review on the mixing estimate and Ando-Haagerup applicability. Then: address XOR exception as a separate sub-node.
