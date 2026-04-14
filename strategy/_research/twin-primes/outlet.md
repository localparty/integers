# Twin Primes Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Twin_prime
- **MathWorld:** https://mathworld.wolfram.com/TwinPrimeConjecture.html
- **Original quantitative form:** Hardy, G. H. & Littlewood, J. E. (1923). "Some problems of partitio numerorum III: on the expression of a number as a sum of primes." *Acta Mathematica* 44, 1–70.
- **Modern survey:** Soundararajan, K. (2007). "Small gaps between prime numbers: the work of Goldston-Pintz-Yıldırım." *Bull. AMS* 44, 1–18.

## 2. Problem statement

**Classical Twin Prime Conjecture:**
> There exist infinitely many primes p such that p + 2 is also prime.

**Quantitative (First Hardy–Littlewood conjecture):**
> The twin-prime counting function π_2(x) = #{ p ≤ x : p, p+2 both prime } satisfies
> π_2(x) ~ 2 C_2 · x / (log x)²    as x → ∞,
> where the twin-prime constant
> C_2 = ∏_{p prime, p ≥ 3} (1 - 1/(p-1)²) ≈ 0.660161815846869573927812...

**Generalized k-tuple form:** For any admissible tuple (h_1, ..., h_k), there are infinitely many n such that n + h_1, ..., n + h_k are all prime; with an explicit asymptotic density (Hardy-Littlewood k-tuple conjecture).

## 3. Prize

**None.** No standalone monetary prize. (Often referenced alongside Goldbach, but Twin Primes has no Faber-style publicity prize.)

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics** — Zhang (2014) published here; Maynard (2015) published here.
- **Inventiones Mathematicae** — Goldston-Pintz-Yıldırım partial results.
- **Acta Mathematica**
- **JAMS**
- **Duke Mathematical Journal**
- **Publications Mathématiques de l'IHES**
- **Compositio Mathematica**
- **Forum of Mathematics, Pi / Sigma**
- **Journal of Number Theory**
- **Acta Arithmetica**

## 5. Formulation variants

- **Classical (qualitative):** infinitely many twin primes.
- **Quantitative (Hardy-Littlewood):** π_2(x) ~ 2C_2 x/(log x)².
- **Bounded gaps (post-Zhang):** lim inf (p_{n+1} − p_n) < ∞ — PROVEN 2013 (Zhang), bound ≤ 246 unconditionally (Polymath8b + Maynard 2014).
- **Specific gap k = 2:** the twin-prime case, still open.
- **Generalized k-tuple (Hardy-Littlewood):** infinitely many k-tuples for any admissible pattern.
- **Polignac's conjecture (1849):** every even h has infinitely many prime pairs (p, p+h).
- **Chen's theorem (1973):** infinitely many primes p such that p+2 is prime-or-semiprime (product of at most two primes).
- **Elliott-Halberstam conjecture-conditional:** bounded-gaps bound ≤ 12 (Polymath8b) or 6 (Maynard, conditional).
- **Dense Divisibility conjecture (generalized Elliott-Halberstam):** gets bounded gap ≤ 6.

## 6. Known partial results + named walls

**Proven:**
- **Brun (1919):** sum of reciprocals of twin primes converges (Brun's theorem); twin primes are "thin."
- **Chen (1973):** infinitely many primes p with p+2 having at most 2 prime factors. (*Chen's theorem*)
- **Goldston-Pintz-Yıldırım (2009, *Annals Math.*):** lim inf (p_{n+1} − p_n)/log(p_n) = 0.
- **Zhang (2014, *Annals Math.*):** lim inf (p_{n+1} − p_n) ≤ 70,000,000. First bounded-gaps result.
- **Maynard (2015, *Annals Math.*); Tao (concurrent):** lim inf (p_{n+1} − p_n) ≤ 600 (and for k-th primes). Simpler method.
- **Polymath8b (2014):** bound reduced to ≤ 246 unconditionally.
- **Under GEH:** bound ≤ 6 (Polymath8b, conditional on Elliott-Halberstam).

**Named walls:**
- *Parity problem (Selberg)* — sieve methods cannot distinguish primes from integers with an even number of prime factors. Any pure sieve approach to twin primes runs into this.
- *Level of distribution wall* — Bombieri-Vinogradov gives level θ < 1/2; Elliott-Halberstam would give θ approaching 1; full θ = 1 is needed for bound = 2.
- *246 → 2 wall* — current unconditional bound is 246; reducing to 2 requires a new idea (the parity problem or a way around it).
- *π_2(x) lower bound wall* — unconditionally, we don't know π_2(x) > 0 infinitely often with any density, only the bounded-gaps version.

## 7. Key references

**Original:**
- Hardy, G. H. & Littlewood, J. E. (1923). "Some problems of partitio numerorum III." *Acta Math.* 44, 1–70.
- De Polignac, A. (1849). "Recherches nouvelles sur les nombres premiers." *Nouv. Ann. Math.*

**Best modern surveys:**
- Granville, A. (2015). "Primes in intervals of bounded length." *Bulletin AMS* 52, 171–222.
- Soundararajan, K. (2007). "Small gaps between prime numbers: the work of Goldston-Pintz-Yıldırım." *Bull. AMS* 44, 1–18.
- Heath-Brown, D. R. (2015). "Yitang Zhang proof of bounded gaps: a history." Lecture notes.

**Key breakthroughs:**
- Goldston, D., Pintz, J., Yıldırım, C. Y. (2009). "Primes in tuples I." *Annals of Math.* 170, 819–862.
- Zhang, Y. (2014). "Bounded gaps between primes." *Annals of Math.* 179, 1121–1174.
- Maynard, J. (2015). "Small gaps between primes." *Annals of Math.* 181, 383–413.
- Polymath, D. H. J. (2014). "Variants of the Selberg sieve, and bounded intervals containing many primes." *Res. Math. Sci.* 1:12.

## Status: OPEN. Bounded-gaps resolved since 2013. No prize. Target journal: Annals of Mathematics.
