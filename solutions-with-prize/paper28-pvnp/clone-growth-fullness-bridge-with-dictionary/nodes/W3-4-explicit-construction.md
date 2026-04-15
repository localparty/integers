# Node: Explicit Construction of ρ_XOR on M_Bool^L

## Status: CLOSED (for the XOR case)

## Key Result

ρ_XOR is constructed EXPLICITLY on M_Bool^L generators without Connes absorption:
- ρ_XOR(e(m)) = e(m) (identity on phases — T_XOR = id by Mal'cev)
- ρ_XOR(μ_C) = ∫_{Ω_L²} μ_{C+C(τ)+C(ρ)} dμ_β(τ)dμ_β(ρ)

**Jones index:** [M : ρ_XOR(M)] = 1 — it's an AUTOMORPHISM, not a proper endomorphism.

**Why:** Mal'cev polymorphisms give bijections σ ↦ σ+τ+ρ of Ω_L for each (τ,ρ). The range projections are preserved. The construction is canonical (uses only internal generators + unique KMS measure).

## Refined sector taxonomy

| Polymorphism type | ρ_f action | Jones index | Sector |
|---|---|---|---|
| Essentially unary (projection) | Identity | 1 | Trivial |
| Mal'cev (m(x,y,y)=x), e.g. XOR | Automorphism, fixes L^∞ | 1 | Automorphic |
| Non-Mal'cev genuinely k-ary (AND/OR/maj) | Proper endomorphism, T_f ≠ id | > 1 | Proper |

## Addresses OA1 Critic Priority 1

The construction is fully explicit — no Connes absorption invoked. Uses the semigroup crossed product structure A_BC^Bool(L) = C*((Z/2)^∞)|_{Ω_L} ⋊ PCirc^+(L).
