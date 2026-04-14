# Lehmer's Totient Problem — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Lehmer%27s_totient_problem
- **MathWorld:** https://mathworld.wolfram.com/LehmersTotientProblem.html
- **Original paper:** Lehmer, D. H. (1932). "On Euler's totient function." *Bulletin of the American Mathematical Society* 38, 745–751.
- **Wikenigma page:** https://wikenigma.org.uk/content/mathematics/lehmer_totient_problem
- **Archive reference:** Pomerance, C. (1977/1980). "On composite integers n for which φ(n) | n − 1." https://math.dartmouth.edu/~carlp/Lehmer0.5.pdf

## 2. Problem statement

**Lehmer's Totient Problem (1932):**
> Does there exist a *composite* integer n such that Euler's totient function φ(n) divides n − 1?

Equivalently (Lehmer's conjecture): the answer is NO — if φ(n) | n − 1 then n is prime.

**Background:** For every prime p, φ(p) = p − 1, so trivially φ(p) | p − 1. The question is whether any composite has this property.

## 3. Prize

**None.** No monetary prize. Research community open problem.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics** — for a full resolution.
- **Inventiones Mathematicae**
- **JAMS**
- **Duke Mathematical Journal**
- **Compositio Mathematica**
- **Journal of Number Theory**
- **Mathematics of Computation** — computational constraints and bounds land here.
- **Acta Arithmetica**
- **Int. J. Number Theory**
- **Mathematische Annalen**
- **Bulletin of the AMS** (Lehmer's original venue)

## 5. Formulation variants

- **Classical Lehmer:** does φ(n) | n − 1 for any composite n?
- **Stronger form:** φ(n) = (n − 1)/k for fixed k; "Lehmer quotient k."
- **Carmichael-type:** any Lehmer counterexample must be a Carmichael number (i.e., a^{n-1} ≡ 1 mod n for all a coprime to n).
- **Rotkiewicz generalization:** question about larger divisors.
- **Polynomial analog (Lehmer over F_q[x]):** proven — see arXiv:1312.3107.
- **Number field analog:** over rings of integers in number fields; studied by Schettler and others.
- **Lehmer in Carmichael's lambda:** variant using the Carmichael function λ(n).
- **Generalized to φ(n) | n − c:** for constants c = 2, 3, etc. (partially studied).

## 6. Known partial results + named walls

**Proven constraints on any Lehmer counterexample n (if it exists):**

| Property | Bound | Year / Author |
|---|---|---|
| n is odd and squarefree | — | Lehmer (1932) |
| n is a Carmichael number | — | Lehmer (1932) |
| Distinct prime factors ω(n) | ≥ 7 | Lehmer (1932), early |
| Magnitude | n > 10^{20} | Cohen-Hagis (1980) |
| With constraint 3 ∤ n | ω(n) ≥ 14 | Cohen-Hagis (1980) |
| If 3 \| n | n > 10^{1937042}, ω(n) ≥ 298848 | Hagis (1988) |
| Strengthened (if 3 \| n) | n > 10^{360000000}, ω(n) ≥ 4 × 10^7 | Burcsi-Czirbusz-Farkas (2011) |
| Density of solutions < X | ≤ X^{1/2} / (log X)^{1/2 − o(1)} | Luca-Pomerance (2011) |

**Proven (polynomial analog):** in F_q[x], the Lehmer-type analog is TRUE (no composite polynomial satisfies).

**Named walls:**
- *Carmichael wall* — any Lehmer counterexample is Carmichael; Carmichael numbers are known infinite (Alford-Granville-Pomerance 1994), but constraints tighten for Lehmer.
- *Prime factor count wall* — forcing ≥ 7 distinct primes is classical; pushing beyond requires new sieve/analytic methods.
- *No non-existence proof* — despite constraints making counterexamples astronomically large, no uniform non-existence argument is known.
- *Heuristic vs proof* — heuristic arguments (Pomerance) suggest counterexamples are extremely rare or nonexistent, but no proof.

## 7. Key references

**Original:**
- Lehmer, D. H. (1932). "On Euler's totient function." *Bull. AMS* 38, 745–751.

**Best modern surveys:**
- Pomerance, C. (1977). "On composite n for which φ(n) | n − 1, II." *Pacific J. Math.* 69, 177–186. (early survey)
- Guy, R. K. (2004). *Unsolved Problems in Number Theory* (3rd ed.), Problem B37. Springer.
- Luca, F. & Pomerance, C. (2011). "On composite integers n for which φ(n) | n − 1." *Bol. Soc. Mat. Mex.* 17, 13–21.

**Key constraint results:**
- Cohen, G. L. & Hagis, P. (1980). "On the number of prime factors of n if φ(n) | (n − 1)." *Nieuw Arch. Wisk.* (3) 28, 177–185.
- Hagis, P. (1988). "On the equation M · φ(n) = n − 1." *Nieuw Arch. Wisk.* (4) 6, 255–261.
- Burcsi, P., Czirbusz, S., Farkas, G. (2011). "Computational investigation of Lehmer's totient problem." *Annales Univ. Sci. Budapest., Sect. Comp.* 35, 43–49.

## Status: OPEN. No monetary prize. Target journal: Annals / Math. Comp. / Inventiones.
