# Node W4-1: The Wall Attack — Endomorphism Algebra Growth

## Status: ADVANCED (p = 0.40-0.55)

## Approach

Iterated endomorphism rho_f^k has End(ρ_f^k) ⊂ M_φ with growing dimension. Growth comes from fusion category theory for sectors with d(ρ) > 1. The growing algebra provides approximately central sequences.

## Why this avoids K-19 and K-20

- K-19 (Lieb-Robinson): no geometric locality assumed — works at sector level
- K-20 (Mal'cev): uses PROPER endomorphisms (T_f ≠ id, d > 1), not identity maps

## Proof skeleton

1. UA1 → ≥(1/2)·2^k polymorphisms at arity k
2. OA1 → distinct proper endomorphisms ρ_f with d(ρ_f) > 1
3. ρ_f^k (iterated k times) has dim(End(ρ_f^k)) growing exponentially (fusion rules, Longo-Roberts 1997)
4. End(ρ_f^k) ⊂ M_φ contains elements commuting with ρ_f^k(M)
5. For local a ∈ M_φ: ||[y, a]|| ≤ 2||y|| · ||a − E_{ρ_f^k}(a)|| → 0 (conditional expectation contracts)
6. Property Gamma → non-fullness (Connes + Ando-Haagerup)

## Four remaining gaps

| Gap | Description | Severity |
|---|---|---|
| (ii) Fusion rules | Compute dim(End(ρ_AND^k)) explicitly | MEDIUM |
| (iii) Hecke contraction | Prove E_{ρ_f^k} contracts non-commutative (Hecke) part of M_φ | MEDIUM-HIGH |
| M_φ factoriality | Verify M_φ is II₁ factor for tractable L | MEDIUM |
| Ando-Haagerup applicability | Verify isomorphism under our conditions | LOW-MEDIUM |

## Relationship to W4-3 (Horn semilattice)

W4-3 gives a simpler path: AND generates M_{|Sol|}(ℂ) → hyperfinite R → Property Gamma. But W4-3 has type II₁/III₁ tension. W4-1 works directly in III₁ but has more gaps. The two approaches are complementary and could combine: W4-3 establishes the II₁ part (centralizer structure), W4-1 provides the III₁ transfer mechanism.
