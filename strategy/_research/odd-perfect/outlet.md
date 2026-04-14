# Odd Perfect Number (OPN) Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia (Perfect number, OPN section):** https://en.wikipedia.org/wiki/Perfect_number
- **MathWorld:** https://mathworld.wolfram.com/OddPerfectNumber.html
- **Oldest open problem source:** Knill, O. "The oldest open problem in mathematics." https://people.math.harvard.edu/~knill/seminars/perfect/handout.pdf
- **Quanta Magazine survey (2020):** https://www.quantamagazine.org/mathematicians-open-a-new-front-on-an-ancient-number-problem-20200910/
- **AMS blog:** https://blogs.ams.org/mathgradblog/2013/07/25/odd-perfect-numbers-exist/

## 2. Problem statement

**Definition:** n is *perfect* if σ(n) = 2n, where σ(n) = ∑_{d | n} d is the sum-of-divisors function.

**Odd Perfect Number Conjecture (ancient; attributed to Nicomachus ~100 CE):**
> No odd perfect number exists.
> Equivalently: for every odd n, σ(n) ≠ 2n.

Euclid (c. 300 BCE) showed 2^{p-1}(2^p − 1) is perfect when 2^p − 1 is a Mersenne prime. Euler (1747) proved the converse: every *even* perfect number has this form. The odd case is OPEN and has been since antiquity.

## 3. Prize

**None.** Despite being the "oldest open problem in mathematics" (Knill, Erdős), no monetary prize has ever been offered. No foundation, no prize.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics** — would be the top venue for a full resolution.
- **Inventiones Mathematicae**
- **JAMS**
- **Acta Mathematica**
- **Duke Mathematical Journal**
- **Journal of Number Theory**
- **Mathematics of Computation** — computational/constraint-type results routinely land here.
- **Acta Arithmetica**
- **International Journal of Number Theory**
- **Fibonacci Quarterly**
- **Integers** (online journal)

Computational verification and structural constraints tend to appear in:
- *Math. Comp.*
- *Integers*
- *JP Journal of Algebra, Number Theory and Applications*

## 5. Formulation variants

- **Classical:** does an odd perfect number exist?
- **Quantitative:** if it exists, what is its minimal size?
- **Euler's form (proven):** any odd perfect number must be N = q^α · m² where q ≡ α ≡ 1 (mod 4), q prime, gcd(q, m) = 1. Called Eulerian form.
- **Descartes number / spoof odd perfect number:** a number that is perfect if one "cheats" by allowing a single composite factor to be prime. Studied because their structure could reveal or rule out OPNs.
- **Abundant / deficient variations:** weaker versions studying σ(n)/n ratios.
- **Generalized for multiperfect (k-fold perfect):** σ(n) = kn. Some multiperfect numbers known; odd multiperfect open.
- **Fibonacci odd perfect, arithmetic progression odd perfect, etc.:** many specific families ruled out.

## 6. Known partial results + named walls

**Constraints on any OPN (if one exists):**

| Property | Bound | Year / Author |
|---|---|---|
| Magnitude | N > 10^{1500} | Ochem-Rao (2012) |
| Prior bound | N > 10^{300} → 10^{1500} | Progressive improvements |
| Number of distinct prime factors (ω(N)) | ω(N) ≥ 10 | Nielsen (2015) |
| Total prime factors with multiplicity (Ω(N)) | Ω(N) ≥ 101 | Ochem-Rao (2012) |
| Largest prime factor | > 10^8 | Goto-Ohno (2008) |
| Second largest prime factor | > 10^4 | lannucci (1999) |
| Third largest prime factor | > 100 | Iannucci (2000) |
| Smallest prime factor | ≤ 2k − 1 for k = ω(N) | Grün (1952) |
| Form (Eulerian) | N = q^α m², q ≡ α ≡ 1 (mod 4) | Euler (1747) |
| Total form (Nielsen) | N ≡ 1 mod 12 or N ≡ 117 mod 468 | Nielsen |

**Density result (Pomerance):** the count of N ≤ x that are odd perfect is o(x) with a specific density bound (essentially, heuristic arguments suggest the total count over all x is bounded, i.e., none might exist).

**Named walls:**
- *Euler form wall* — we've exploited the q^α m² structure maximally; further constraints require new ideas.
- *Descartes number wall* — spoof odd perfect numbers exist (Descartes 1638); distinguishing them rigorously from real OPNs is subtle.
- *Heuristic vs proof gap* — Pomerance and others give strong heuristic evidence against OPN existence, but no proof.
- *Sylvester-Dickson size-bound wall* — every size improvement (10^{300} → 10^{1500}) has been via computer search + structural refinement, never a uniform bound.
- *No unconditional non-existence strategy* — unlike some number-theoretic problems, there's no known "if X then no OPN" with X plausibly provable.

## 7. Key references

**Original:**
- Nicomachus of Gerasa (c. 100 CE). *Introduction to Arithmetic*.
- Euclid (c. 300 BCE). *Elements*, Book IX, Proposition 36.
- Euler, L. (1747). "De numeris amicibilibus." (Posthumous; various collected works.)

**Best modern surveys:**
- Sandor, J. & Crstici, B. (2004). *Handbook of Number Theory II*. Kluwer.
- Ribenboim, P. (1996). *The New Book of Prime Number Records*. Springer.
- Guy, R. K. (2004). *Unsolved Problems in Number Theory* (3rd ed.). Springer.
- Pollack, P. & Shevelev, V. (various dates). Surveys on perfect numbers.

**Key constraint results:**
- Ochem, P. & Rao, M. (2012). "Odd perfect numbers are greater than 10^{1500}." *Math. Comp.* 81, 1869–1877.
- Nielsen, P. P. (2015). "Odd perfect numbers, Diophantine equations, and upper bounds." *Math. Comp.* 84, 2549–2567.
- Goto, T. & Ohno, Y. (2008). "Odd perfect numbers have a prime factor exceeding 10^8." *Math. Comp.* 77, 1859–1868.
- Pomerance, C. (1974). "Multiply perfect numbers, Mersenne primes, and effective computability." *Math. Ann.* 226, 195–206.

## Status: OPEN since ancient times. No monetary prize. Target journal: Annals / Math. Comp. / Inventiones.
