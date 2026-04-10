# A2.02 — Weak-* State Convergence

## Claim (Corollary 4.2)

> ω₁^{(≤P_N)} := ⊗_{p ≤ P_N} ω₁^{(p)} → ω₁ weak-*.

## Assessment

The argument given in Section 4.5 is the standard approximation-by-
finite-subproducts argument: for any a ∈ 𝒜_BC and ε > 0, there
exists N₀ such that a is ε-approximated by an element of
⊗_{p ≤ P_{N₀}} 𝒜_p, and on such elements the finite product
states agree with ω₁ for N ≥ N₀.

This is **correct** provided the restricted tensor product
structure is dense in 𝒜_BC, which it is by definition of the
infinite restricted tensor product. Standard.

**Verdict:** PASS.

One caveat: weak-* convergence is the *weakest* natural notion of
state convergence. It is not the same as norm convergence, and in
particular it does *not* automatically give Hilbert-space
convergence of GNS vectors. The subsequent inference to form
convergence (Proposition 4.3) uses only the entry-by-entry
stabilization property of the matrix elements, which is a
consequence of the algebraic direct-limit structure and does not
actually require weak-* state convergence. See A2.03.
