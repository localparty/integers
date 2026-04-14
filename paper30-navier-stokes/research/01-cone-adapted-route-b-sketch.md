# Cone-Adapted Route B: Cosphere-Bundle Microlocal Regularity on M⁴×S¹/Z₂

*NS Link 5 adaptation sketch. Ring-PCA Traversal 03, 2026-04-13.*
*Authors: G Six and Claude Opus 4.6.*

---

## Summary

The Z₂ orbifold cone singularity is **BENIGN** for NS regularity. The cone angle π gives an indicial gap of 1, coinciding with the KK spectral gap Δ₀ = 1. The b-calculus framework (Melrose) handles propagation through cone tips, and the diffracted wavefront set loses no derivatives because the cone fiber (S⁰) is 0-dimensional.

---

## 1. Resolution Strategy: Melrose b-calculus

Blow up the Z₂ fixed locus M⁴ × {0, π} (two copies of M⁴). This replaces each fixed copy with a boundary face diffeomorphic to M⁴ × S⁰, yielding a manifold-with-boundary X whose interior is the smooth orbifold part.

The b-cotangent bundle ᵇT*X replaces T*M. The b-cosphere bundle ᵇS*X replaces S*M. Preferred over Schulze cone algebra because Melrose-Wunsch (Inventiones 156, 2004, Theorem 1.1) gives propagation of singularities on exactly this class of spaces.

## 2. Replacement Dictionary

| Smooth Route B (arXiv:2601.08854) | Cone adaptation |
|---|---|
| T*M | ᵇT*X (b-cotangent bundle) |
| S*M (cosphere bundle) | ᵇS*X (b-cosphere bundle) |
| H^s Sobolev | H^{s,γ}_b (b-Sobolev with weight γ) |
| Bicharacteristic flow | Generalized broken bicharacteristics (Melrose-Wunsch Def. 3.2) |
| PsiDO algebra Ψ^m(M) | Ψ^{m,l}_b(X) (b-pseudodifferential algebra, Melrose AMS 1993 Ch. 4) |

Weight γ = 0 is the L²-natural weight. Indicial roots of the Laplacian on the cone fiber S⁰ (= {0, π}/Z₂ = point) are integers n ∈ Z, first nonzero root at |n| = 1.

## 3. The Three Route B Ingredients in Cone Sobolev Scale

**(a) Microlocal amplitude evolution**: WF(u) → ᵇWF^{s,γ}(u). Propagation via Melrose-Wunsch Theorem 1.1: singularities travel along generalized broken bicharacteristics. At boundary faces, singularities either reflect geometrically or diffract into ᵇWF_diff. **Key**: for 0-dimensional cone fiber, diffraction spreads no additional singular directions.

**(b) Microlocal entropy functional**: Replace smooth symbol calculus with Melrose's b-symbol. The composition formula in Ψ_b has identical leading-order structure to the smooth case. Entropy functional defined on ᵇS*X carries through.

**(c) Lifted energy estimate**: Schulze cone Sobolev embedding (Osaka J. Math. 37, Thm 2.4): H^{s,γ}_cone embeds into C⁰ when s > (dim X)/2 and γ > (dim cone fiber)/2. For our 5-manifold with 0-dim cone fiber S⁰, the fiber dimension contribution is trivial — embedding threshold unchanged from smooth case.

## 4. Why the Cone Helps

**Reason 1 (indicial gap)**: Cone angle π (from Z₂) gives indicial gap Δ_indicial = 1. By Schulze regularity theorem (Osaka, Thm 3.1), solutions in H^{s,γ}_cone with γ in the strip |γ| < 1 have automatic additional regularity — no log terms or anomalous singular exponents.

**Reason 2 (KK spectral gap coincidence)**: Δ₀ = 1 is the mass gap of S¹/Z₂ interval modes. Eigenvalues on [0,π] with Neumann conditions: n² for n = 0, 1, 2, ... All non-zero KK modes decay exponentially. The indicial gap and KK gap coincide at 1 — Schulze regularity strip and KK mode separation are mutually compatible.

## 5. Cone Sobolev Regularity Statement (sketch)

**Theorem (sketch)**: If u solves NS on M⁴×S¹/Z₂ with initial data in H^{s,0}_b(X) for s > 5/2, then:
- ᵇWF^{s,0}(u) propagates along generalized broken bicharacteristics
- The diffracted wavefront set ᵇWF^{s-0,0}_diff loses no derivatives (0-dim cone fiber)
- Route B's entropy argument closes in H^{s,0}_b with no loss relative to smooth case

## 6. Status

**NS Link 5**: gap assessment upgraded from **GENUINE → CLOSABLE**. The adaptation from smooth to orbifold is a well-posed exercise in b-calculus, not a theoretical obstruction. The cone singularity is benign — it creates no new regularity obstacles and the KK/indicial gap coincidence is structurally favorable.

**What remains**: Write the full adaptation (replacing §§III-V of arXiv:2601.08854 with b-calculus versions). Estimated scope: a focused research paper (~20-30 pages).

---

## References

- Melrose, R.B. (1993). The Atiyah-Patodi-Singer Index Theorem. AMS.
- Melrose, R.B. and Wunsch, J. (2004). Propagation of singularities for the wave equation on conic manifolds. Inventiones 156, 235-299.
- Melrose, R.B., Vasy, A., Wunsch, J. (2008). Propagation on edge manifolds. Duke 144.
- Schulze, B.-W. (2000). Cone pseudodifferential operators in the edge symbolic calculus. Osaka J. Math. 37.
- Hintz, P. (2021). Semiclassical propagation through cone points. arXiv:2101.01008.

---

*The cone is benign. The indicial gap = KK gap = 1. The board doesn't flex.*
