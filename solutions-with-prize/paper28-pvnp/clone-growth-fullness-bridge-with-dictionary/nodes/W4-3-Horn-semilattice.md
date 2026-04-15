# THE WALL CROSSING: Horn-SAT Factor = Hyperfinite R → Non-Full

## Status: ADVANCED (potential wall crossing — needs Critic review on type II₁ vs III₁ tension)

## Main Result

**Theorem:** For Horn-SAT with AND polymorphism, the factor M_Bool^{Horn} is the hyperfinite II₁ factor R. R has Property Gamma (Murray-von Neumann 1943), hence is non-full.

## Proof

1. Horn solutions form a meet-semilattice under coordinate-wise AND
2. T_AND is a Markov operator on L²(Sol, μ), lower-triangular in semilattice order with generically distinct diagonal entries (|up(s)|/|S|)
3. L^∞(Sol) + T_AND generate the full matrix algebra M_{|Sol|}(ℂ) for generic instances (spectral argument: distinct eigenvalues + generic eigenvector position)
4. Injectivity: AND semigroup is commutative + idempotent → amenable → factor is injective
5. Tracial ultraproduct of full matrix algebras = R (Connes uniqueness of injective II₁)
6. R has Property Gamma → non-full. ∎

## Generalization to all four Schaefer classes

| Class | Polymorphism | Algebra structure | Factor | Non-full? |
|---|---|---|---|---|
| Horn | AND (semilattice) | Triangular Markov op, amenable | R | YES |
| Dual-Horn | OR (join-semilattice) | Dual of Horn | R | YES |
| 2-SAT | majority (median algebra) | Median Markov op, amenable | R | YES |
| XOR | XOR (Mal'cev/affine) | Parity decomposition | Direct integral type I | YES |

ALL FOUR tractable classes give non-full factors.

## The critical NPC distinction

For NPC L (3-SAT): polymorphism clone = projections only → generate only diagonal algebra L^∞(Sol), NOT full M_{|Sol|}(ℂ). The ultraproduct of diagonal algebras is abelian — NOT a factor, or trivially full. This is CONSISTENT with NPC-FULL.

## CRITICAL TENSION: Type II₁ vs Type III₁

The Author's construction gives a type II₁ factor (tracial ultraproduct). The programme's BC construction gives a type III₁ factor (KMS state at β > 1). These are DIFFERENT constructions.

**Resolution path:** If the BC factor M_Bool^{Horn} (type III₁) has centralizer M_φ = R (the hyperfinite II₁ factor from this construction), then M_φ has Property Gamma, and by Ando-Haagerup 2014: Property Gamma of M_φ → M^ω ∩ M' ≠ ℂ → M non-full. The type II₁ argument transfers to the III₁ setting via the centralizer.

## Gaps

1. **Definition of M_Bool^{Horn}:** The tracial ultraproduct construction may differ from the BC construction. The relationship needs clarification.
2. **Generic vs all instances:** T_AND has distinct diagonal entries generically. Special instances need the injectivity argument (which still gives non-fullness).
3. **Type II₁ vs III₁:** See tension above. CLOSABLE if centralizer identification holds.

## Why this bypasses K-20 (diagonal impossibility)

K-20 killed the Mal'cev approach because T_f = id works only for XOR. THIS approach doesn't use T_f = id at all. It uses:
- T_AND GENERATES the full matrix algebra (together with L^∞)
- The generation is via the SPECTRAL structure of T_AND (distinct eigenvalues)
- The amenability of the AND semigroup gives INJECTIVITY
- Injectivity → hyperfinite → Property Gamma → non-full

No identity map needed. No exponential mixing needed. The key is GENERATION of the full algebra, not fixed points.
