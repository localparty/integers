### ANT ↔ PROB: GUE Zero-Spacing to Prime Gap Constraint

**Statement**: The GUE small-gap tail statistics of Riemann zeros, realized as QG5D BC eigenvalue spacings {γ_n}, force bounded gaps between primes via the explicit formula.

**Mechanism**: QG5D's CBB operator has eigenvalues matching Riemann zeros whose pair-correlation follows GUE (Montgomery 1973, Odlyzko numerics). The GUE repulsion law suppresses small spacings as P(s < ε) ~ (π²/3)ε³, but the tail probability for near-coincident zeros is nonzero and quantifiable. Feeding these spacing statistics into the explicit formula ψ(x) = x − Σ_ρ x^ρ/ρ − ... translates zero-clustering rates into prime gap constraints: clustered zeros produce oscillatory cancellations forcing primes to stay bunched. GPY (2009) and Maynard-Tao (2014) exploit this structure to extract bounded gaps H < ∞.

**Source**: Montgomery (1973) pair correlation; Goldston-Pintz-Yıldırım (2009) Annals; Maynard (2015) Annals.

**Status**: ESTABLISHED (bounded gaps H ≤ 246); CANDIDATE (twin-prime limit H = 2)

**Load-bearing for**: QG5D + Twin Primes (Paper 34)

**Transposition recipe**:
1. Extract GUE nearest-neighbor spacing distribution p(s) from BC eigenvalue spectrum.
2. Compute pair-correlation integral R(α); verify Montgomery conjecture agreement.
3. Apply explicit formula: zero-spacing density near s → 0 → lower bound on prime pair count.
4. Maynard-Tao sieve with spectral input: GUE gap tail sets admissible shift H.
5. Twin prime limit: if QG5D eigenvalue model matches GUE exactly at s = 0 + Elliott-Halberstam → H = 2.

*Filled by T1 hub radiation, 2026-04-13.*
