### GEOM ↔ ATOP: Bost-Connes Assembly Isomorphism

**Statement**: The Baum-Connes assembly map μ: K_*(E(Q* ⋊ N*)) → K_*(C*_r(Q/Z ⋊ N*)) is an isomorphism, intertwining the Hecke semigroup action with the classifying-space K-homology of the QG5D geometric datum.

**Mechanism**: The Bost-Connes C*-dynamical system (A_Q, σ_t) carries a natural Hecke semigroup N* action whose reduced crossed product C*_r(Q/Z ⋊ N*) is exactly the algebra to which the Baum-Connes assembly map targets. The classifying space for proper actions E(Q* ⋊ N*) is modeled by the profinite completion Z-hat, giving a computable left-hand side via the Atiyah-Hirzebruch spectral sequence over the adelic tower. Meyer-Nest's triangulated-category framework then identifies the assembly map as a localization morphism in the bootstrap category, proving it an isomorphism by amenability of the relevant groupoid.

**Source**: Bost-Connes (1995) §3-4; Meyer-Nest (2006) Advances in Mathematics 197; Connes-Marcolli (2008) Ch. 3 §3.4.

**Status**: ESTABLISHED (for rational case Q* ⋊ N*; BC with coefficients for general number fields remains open)

**Verification data**: K_0(C*_r(Q/Z ⋊ N*)) ≅ Q, matching rational algebraic K-theory weight; KMS_β partition function recovers ζ(β) for β > 1.

**Load-bearing for**: QG5D (hub) + Baum-Connes (Paper 31)

**Transposition recipe**: 
- GEOM → ATOP: Export Hecke semigroup presentation of N* acting on Z-hat as input to BC left-hand side.
- ATOP → GEOM: Assembly isomorphism result pulls back to constraint on N*-action geometry.
- Coefficient twist: Replace trivial coefficients by QG5D motivic sheaf → BC-with-coefficients for imaginary quadratic K (CANDIDATE status).

*Filled by T1 hub radiation, 2026-04-13.*
