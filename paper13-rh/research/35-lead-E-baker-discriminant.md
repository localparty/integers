# Research 35 -- Lead E: Baker's Theorem and the Discriminant/Resultant Approach

*Date: 2026-04-09*
*Status: HARD. Feasibility 3/10 general, 5/10 small N. Worth scoping the N=2 case.*

---

## 1. Setup and the spectral disjointness condition

RH is reduced to: spec(B) cap spec(M_a) = emptyset. The operator B has entries involving log p (prime logarithms) and digamma/archimedean corrections; M_a is the arithmetic companion. The goal is to show their spectra never overlap.

## 2. Discriminant gives simplicity, not disjointness

The discriminant of the characteristic polynomial of B is

    Disc(B) = prod_{i<j} (lambda_i - lambda_j)^2

If Disc(B) != 0, all eigenvalues of B are simple. By DPTZ, simplicity plus a genericity condition yields the overlap condition -- but only IF we additionally show no eigenvalue of B coincides with one of M_a.

**The discriminant alone is insufficient.** Disc(B) != 0 tells us nothing about spec(B) vs spec(M_a).

## 3. The correct object: the resultant

The quantity that vanishes iff B and M_a share an eigenvalue is the resultant:

    R = Res(det(B - lambda I), det(M_a - lambda I))

This is the resultant of the two characteristic polynomials, viewed as polynomials in lambda. It satisfies:

    R = prod_{k,j} (lambda_k(B) - lambda_j(M_a))

Hence R = 0 iff spec(B) cap spec(M_a) != emptyset. We need R != 0.

## 4. Baker's theorem and transcendence

Baker's theorem (1966): if alpha_1, ..., alpha_n are nonzero algebraic numbers and beta_1, ..., beta_n are algebraic with not all beta_i = 0, then

    |beta_1 log alpha_1 + ... + beta_n log alpha_n| > exp(-C(n, h))

where C depends on n and the heights of the alpha_i, beta_i. In particular, the linear form is nonzero (and quantitatively bounded away from zero).

The entries of B involve log 2, log 3, log 5, ..., as well as pi and gamma_E (via digamma terms). Baker's theorem certifies that these are "sufficiently independent" -- no nontrivial algebraic linear combination vanishes.

## 5. The obstacle: resultant is polynomial, not linear

Baker's theorem controls LINEAR forms in logarithms. The resultant R is a POLYNOMIAL function of the entries of B and M_a. When expanded, R is a sum of monomials in {log p_i, pi, gamma_E, ...} with integer (or rational) coefficients coming from the matrix structure.

To apply Baker, we would need: at least one monomial in the expansion of R that Baker (or Lindemann-Weierstrass, or Nesterenko) certifies is nonzero, and that this monomial does not cancel against others.

This is an algebraic independence question, not a linear independence question. Baker does not directly reach it.

## 6. What would be needed

For the Baker route to work on R, one would need:

- (a) Expand R explicitly as a polynomial in the transcendental entries.
- (b) Identify a "leading monomial" (in some ordering) that is nonzero by transcendence theory.
- (c) Show no cancellation occurs among lower-order terms.

Step (c) is the hard part. For general N, the resultant of two NxN characteristic polynomials has O(N!) terms. Controlling cancellation in such expressions is a major open problem in transcendental number theory.

## 7. Small N as proof of concept

For N = 2: the characteristic polynomials are quadratic, and the resultant is a degree-4 polynomial in the matrix entries. One can write it out by hand.

For N = 3: the resultant is degree-9 and still tractable with computer algebra.

**Concrete programme for N = 2:**
1. Write B and M_a as explicit 2x2 matrices in {log 2, log 3, pi, gamma_E}.
2. Compute det(B - lambda I) and det(M_a - lambda I) as quadratics in lambda.
3. Compute R = Res(p_B, p_M) as a polynomial in the transcendental constants.
4. Apply Nesterenko's theorem (pi and e^pi are algebraically independent) or Lindemann-Weierstrass to certify R != 0.

This is feasible if the polynomial expression for R is "generic enough" in the transcendental constants.

## 8. Feasibility assessment

| Scope | Feasibility | Notes |
|-------|-------------|-------|
| General N | 3/10 | Resultant has factorial complexity; no tool controls polynomial (not linear) forms in logarithms for general degree. |
| Small N (N=2,3) | 5/10 | Explicit computation possible. Success depends on whether the resulting polynomial expression is amenable to known transcendence results. |

**Recommendation:** Compute the N=2 resultant explicitly. If it reduces to a form where Lindemann-Weierstrass or Nesterenko applies, this validates the approach for small N and clarifies what new transcendence results would be needed for general N.

---

*Next step: explicit 2x2 computation (Research 36).*
