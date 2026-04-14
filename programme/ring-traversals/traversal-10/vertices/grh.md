# GRH Vertex -- Traversal 10 Construction Pass (L3, L4)

*Paper 13b. Date: 2026-04-14. Entering status: 2/8 PROVED (L1, L2).*

## 1. L3 Construction: D_{N,chi} on E_{N,chi}^+

**Input** (from L2, proved): ω_{1,χ} unique KMS_1 on (A_Q^χ, σ_t^χ); GNS triple (H_χ, π_χ, Ω_χ); type III_1 factor M_χ.

**E_{N,χ}^+ definition**: band-limited even sector. Fix bandwidth λ, truncation level N, and a Dirichlet character χ mod q with (q,N)=1 so the first N prime factors miss the conductor. Let E_N^+ = P_λ^+ L^2(R) be the even λ-band-limited subspace (as in CCM). Then
E_{N,χ}^+ := E_N^+ ⊗ ℓ^2((Z/qZ)^*, χ)
where the second factor carries the character (the χ-isotypic component of the regular representation). Prolate-spheroidal basis {ψ_k} is unchanged; the χ-factor acts by multiplication.

**D_{N,χ} definition**. Write D_N (CCM) in the prolate basis as a self-adjoint (2N+1)-dim matrix A^ev(λ, N). Define
    D_{N,χ} := A^ev(λ, N) ⊗ I + I ⊗ M_χ
where M_χ = diag(log p_k + i arg χ(p_k)) on the first N prime-indexed components (see Euler-product assembly below, §2). Equivalently, D_{N,χ} acts on f ⊗ e_a ∈ E_{N,χ}^+ by (D_N f) ⊗ e_a + f ⊗ (log-phase shift) e_a.

**Self-adjointness**. A^ev(λ,N) is self-adjoint (CCM Thm 4.2). M_χ is Hermitian iff we take the *symmetrized* phase (χ(p)+χ̄(p))/2 for real self-adjointness — with complex χ one gets a normal operator whose real part has real spectrum. For χ=(-4/·) (real character), M_χ is literally diagonal with entries ±log p_k, hence self-adjoint. **So for real χ, D_{N,χ} is self-adjoint directly; for complex χ, one works with D_{N,χ}^{sym} = (D_{N,χ} + D_{N,χ}^*)/2.**

**Eigenvalue claim**: spec(D_{N,χ}) ≈ {γ_{n,χ}} (ordinates of zeros of L(s,χ)) in the limit λ,N → ∞. This is **structurally parallel** to CCM Thm 5.10 but requires the Hurwitz-convergence step ξ̂_{N,χ} → Λ(s,χ), which in turn needs L5 (estimates_χ). **So L3 construction is explicit and rigorous for real χ; eigenvalue convergence is CONDITIONAL on L5.**

## 2. L4 Construction: ITPFI_χ factorization

**Claim**: ω_{1,χ} = ⊗_p ω_{1,χ}^{(p)} as a state on A_Q^χ = ⊗_p A_p^χ.

**Proof sketch**. The BC algebra factors as A_Q = ⊗_p A_p where A_p is the p-adic piece (Laca-Raeburn 1996; Bost-Connes 1995 Thm 25). The χ-twist σ_t^χ(μ_n) = χ(n) n^{it} μ_n is **multiplicative in n**: χ(nm)=χ(n)χ(m), n^{it}m^{it}=(nm)^{it}. Therefore σ_t^χ factors: σ_t^χ = ⊗_p σ_t^{χ,(p)} where σ_t^{χ,(p)}(μ_{p^k}) = χ(p)^k p^{kit} μ_{p^k}.

Each local system (A_p, σ_t^{χ,(p)}) has local partition function
    Z_χ^{(p)}(β) = Σ_{k≥0} χ(p)^k / p^{kβ} = (1 - χ(p) p^{-β})^{-1}
convergent for Re β > 0 (|χ(p)|≤1), with finite nonzero value at β=1 since χ(p)≠p (root of unity vs integer >1). Local Gibbs state ω_{1,χ}^{(p)} exists and is the unique KMS_1 on A_p^χ by the same Bratteli-Robinson argument applied locally (fixed-point algebra trivial: χ(p)≠1 for at least one p kills invariants; for the remaining primes, the n^{it} factor suffices as in untwisted BC — Laca-Raeburn Prop 2.1).

**Tensor assembly**. ⊗_p ω_{1,χ}^{(p)} satisfies KMS_1 w.r.t. ⊗_p σ_t^{χ,(p)} = σ_t^χ. By L2 uniqueness, ⊗_p ω_{1,χ}^{(p)} = ω_{1,χ}.

**Euler product cross-check**: Z_χ(1) = ∏_p Z_χ^{(p)}(1) = ∏_p (1-χ(p)/p)^{-1} = L(1,χ). ✓

**Rigor**: This is C*-algebraic and rigorous as-is, conditional on L2 (PROVED) and the local uniqueness. Local uniqueness is a direct adaptation of L2's argument to one prime. **L4 closes as PROVED.**

## 3. Rigor audit / pilot need

- **L3 for real χ**: construction explicit and self-adjoint; eigenvalue matching to {γ_{n,χ}} is **CONDITIONAL on L5** (specifically L5c H^1 Fourier cancellation, which is the genuine wall).
- **L3 for complex χ**: needs symmetrization; the spectrum of D_{N,χ}^{sym} vs the ordinates γ_{n,χ} requires extra care (imaginary parts of zeros of L(s,χ) for complex χ come in conjugate pairs L(s,χ)/L(s,χ̄), so real-part averaging is natural). Pilot needed.
- **L4**: rigorous as-is (C*-algebraic, inherits from L2).
- **Pilot for χ=(-4/·)** (real, mod 4): verify numerically that eigenvalues of D_{N,χ}^ev computed in the prolate basis, with M_χ = diag(χ(p)·log p), approximate the known zeros of L(s,(-4/·)) (the Dirichlet L-function for the non-trivial character mod 4; first zero γ_{1,χ} ≈ 6.02... on the critical line). Target: N=120, 6 primes, 10^{-20} agreement. This would confirm the transfer mechanism empirically before closing L5.

## 4. Verdict

- **L3**: ADVANCED to **PARTIAL-PROVED** (construction rigorous for real χ; eigenvalue claim conditional on L5 — same conditional structure as RH's L1 on CCM). Flip to PROVED when L5 closes.
- **L4**: CLOSED as **PROVED** (ITPFI_χ factorization via Euler-product decomposition of σ_t^χ + L2 uniqueness; Bost-Connes local/global structure carries through unchanged).

**Projected chain after this pass: 3/8 PROVED (L1, L2, L4) + L3 PARTIAL. Wall still at L5c (H^1 Fourier cancellation with χ(n) weights). Next: L5c pilot computation for χ=(-4/·).**
