# Hodge Conjecture — Official Problem Statement

**Author of official statement:** Pierre Deligne, "The Hodge Conjecture"
**Source:** https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf
**Local copy:** `../00-clay-rules/hodge-deligne.pdf`
**Text extract:** `../00-clay-rules/hodge-deligne.txt`
**Retrieved:** 2026-04-14

---

## The Problem (verbatim)

Deligne sets up: X a projective non-singular algebraic variety over C, Hodge decomposition H^n(X, C) = ⊕_{p+q=n} H^{p,q}. A closed analytic subspace Z of complex codimension p defines a class cl(Z) ∈ H^{2p}(X, Z) that is of type (p,p). Rational (p,p)-classes are called **Hodge classes**:

> H^{2p}(X, Q) ∩ H^{p,p}(X) = H^{2p}(X, Q) ∩ F^p ⊂ H^{2p}(X, C)

> **Hodge Conjecture.** On a projective non-singular algebraic variety over C, any Hodge class is a rational linear combination of classes cl(Z) of algebraic cycles.

## Key remarks (§2 of Deligne)

- (ii) Integral linear combinations of cl(Z) = integral linear combinations of products of Chern classes of algebraic vector bundles.
- (iii) Lefschetz (1,1)-theorem: the conjecture holds for H^2 (proved by Lefschetz; also Kodaira-Spencer via exp exact sequence).
- (iv) **Atiyah-Hirzebruch:** the Hodge conjecture CANNOT hold integrally — it must be Q-rational. Any proof must respect this.
- (v) The assumption that X is algebraic CANNOT be weakened to X merely Kähler (counterexamples exist where X is a complex torus).
- (vi) Hodge's original formulation also had a stronger conjecture that Grothendieck observed to be false and corrected in [Grothendieck].

## Known cases

- H^0, H^1, H^{2n-1}, H^{2n} trivial.
- **H^2** (Lefschetz (1,1) theorem): proved.
- H^{2n-2} (hard Lefschetz + Poincaré duality): follows from H^2.
- Abelian varieties, certain Shimura varieties: many partial results.
- **General case open** for H^{2p} with 2 ≤ p ≤ n-2.

## Clay §5(c) note

Hodge is NOT §5(b). A counterexample (rational Hodge class not algebraic) falls under §5(c).
