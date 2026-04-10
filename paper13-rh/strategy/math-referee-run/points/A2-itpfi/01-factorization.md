# A2.01 — The Factorization Proof

## Proof 1 assessment (the rigorous one)

The chain is:

(S1) **Laca–Raeburn 1996, Theorem 2.1:** the p-local sub-Hecke
algebra 𝒜_p has a unique KMS₁ state ω₁^{(p)}, with
ω₁^{(p)}(μ_p^k μ_p^{*k}) = p^{−k}. Standard result, widely cited.

(S2) **Bratteli–Robinson Proposition 5.3.23:** for product flows
on tensor products of C*-algebras, the product of KMS states is
KMS. Standard result from the OAQSM textbook.

(S3) **Bost–Connes 1995, Theorem 25:** on 𝒜_BC the KMS₁ state is
unique (single extreme point of the KMS₁ simplex). Canonical
source.

(S4) **Chain:** define φ := ⊗_p ω₁^{(p)} on ⊗̄_p 𝒜_p ≅ 𝒜_BC (as
a restricted tensor product). By S2, φ is KMS₁. By S3, uniqueness
forces φ = ω₁.

Each individual step is a standard, published result. The only
substantive question is whether 𝒜_BC truly admits the restricted
tensor product structure ⊗̄_p 𝒜_p *as a C\*-algebra*. The
Bost–Connes algebra is indeed the semigroup crossed product
C(ℤ̂) ⋊ ℕ^× and ℕ^× = ⊕_p ℕ under prime factorization, so the
crossed product decomposes accordingly. This is well-known in the
literature (Laca–Raeburn, Connes–Marcolli's textbook *Noncommutative
Geometry, Quantum Fields and Motives*, chapter III).

**Verdict on Proof 1:** PASS. The three cited results are
standard, the crossed-product decomposition is standard, and the
uniqueness-driven identification is correct.

## Proof 2 assessment (amenability / Bauer simplex)

Uses Laca–Neshveyev 2004 (or similar) for amenable semigroup
crossed products: the KMS simplex is Bauer and its extreme points
are product states. At β = 1 the simplex collapses to a single
point, which must therefore factor as a product.

The argument is **too compressed** in Paper 13 Section 4.3 to
evaluate rigorously. The claim that "an extreme point of a Bauer
simplex that is the unique KMS state must factor over the tensor
product decomposition" is not obvious without more detail. However,
since Proof 1 is independent and complete, Proof 2 serves only as
a cross-check and I do not need to validate it in depth.

**Verdict on Proof 2:** Not independently verified here; not
required since Proof 1 suffices.

## Proof 3 assessment (Araki–Woods)

The GNS von Neumann algebra π₁(𝒜_p)'' is claimed to be a type
III_{1/p} factor. This is standard (Bost–Connes 1995,
Connes–Marcolli). The infinite tensor product of type III_{λ_p}
factors with λ_p = 1/p and ∏ λ_p = 0 is an ITPFI factor of type
III₁ (Araki–Woods 1968, canonical classification).

The Paper 13 argument further says "the factorization of the state
follows from the factorization of the modular flow
σ_t^{ω₁} = ⊗_p σ_t^{ω₁^{(p)}}." This is the right idea but is
stated without verifying that the modular flow actually decomposes
as a product — on an ITPFI factor of type III₁ this is a property
of the specific decomposition, not automatic from having
III_{1/p} factors.

**Verdict on Proof 3:** Plausible and traditional, but as stated
in Paper 13 it leans on a one-line justification where a
paragraph is warranted. Again, not required since Proof 1 suffices.

## Overall

**PASS on Proof 1.** The factorization is a standard consequence of
Bost–Connes KMS uniqueness, Laca–Raeburn p-local uniqueness, and
Bratteli–Robinson product KMS states. This is well-trodden
operator-algebraic territory.

One editorial note: Paper 13 Section 4 is slightly over-enthusiastic
("three independent proofs") when Proof 1 alone is rigorous and
the other two are cross-checks whose compressed exposition would
not pass a careful referee on their own.
