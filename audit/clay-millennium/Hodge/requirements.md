# Hodge Conjecture — Requirements (itemized)

**Source:** `00-problem-statement.md` (Deligne 2000)

## Formal requirements

| # | Requirement | Source |
|---|---|---|
| 1 | X is a projective non-singular algebraic variety over C | Statement quantifier |
| 2 | For every Hodge class α ∈ H^{2p}(X, Q) ∩ H^{p,p}(X), α is a **Q-linear** combination of classes cl(Z) of algebraic cycles of codimension p | Main statement |
| 3 | Must hold for ALL p, 0 ≤ p ≤ n (dim X = n) | Universal quantifier |
| 4 | Result is over Q, not Z (Atiyah-Hirzebruch obstruction) | §2(iv) |
| 5 | The variety X must be algebraic; Kähler is NOT sufficient | §2(v) |

## Cases already known (do not have to be re-proved, but must be compatible)

- Hodge (1,1): Lefschetz theorem — must be consistent with.
- Abelian varieties: partial results (Mumford-Tate, etc.).
- Ribet / Deligne absolute Hodge cycles framework.

## Permissible forms of proof

- Direct construction: for each Hodge class, exhibit algebraic Z_i and rationals a_i with α = Σ a_i cl(Z_i).
- Via motives / absolute Hodge / tannakian argument.
- Reduction to a sufficiently large family of test cases (abelian, complete intersections, etc.) then deformation.
- Via variation-of-Hodge-structure / algebraicity of Hodge loci (Cattani-Deligne-Kaplan partial).

## Non-required but natural corollaries

- Standard conjectures of Grothendieck
- Algebraicity of Hodge loci
- Tate conjecture (l-adic analog) — separate, not part of Hodge Clay problem.

## Clay §5(c) note

Counterexample = a rational Hodge class not a Q-linear combination of algebraic cycles on some projective non-singular variety over C. Full-prize §5(c)(i) material.
