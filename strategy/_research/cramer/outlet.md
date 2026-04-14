# Cramér's Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture
- **Original paper:** Cramér, H. (1936). "On the order of magnitude of the difference between consecutive prime numbers." *Acta Arithmetica* 2, 23–46.
- **Modern corrective work:** Granville, A. (1995). "Harald Cramér and the distribution of prime numbers." *Scandinavian Actuarial Journal* 1, 12–28.

## 2. Problem statement

**Cramér's Conjecture (1936):**
> p_{n+1} − p_n = O((log p_n)²),
> where p_n is the n-th prime.

**Stronger form (sometimes called "Cramér's strong conjecture"):**
> lim sup_{n → ∞} (p_{n+1} − p_n) / (log p_n)² = 1.

**Granville's refined form (1995):**
> lim sup_{n → ∞} (p_{n+1} − p_n) / (log p_n)² ≥ 2 e^{-γ} ≈ 1.1229,
> suggesting the stronger Cramér form is *false* (constant > 1), but Cramér's big-O version is likely correct.

## 3. Prize

**None.** No monetary prize. Cramér's conjecture sits alongside other classical prime-gap results without a foundation-backed prize.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics** — Ford-Green-Konyagin-Tao (2014/2016) published here; Maynard (2016) also.
- **Inventiones Mathematicae**
- **JAMS**
- **Acta Mathematica**
- **Duke Mathematical Journal**
- **Compositio Mathematica**
- **Forum of Mathematics, Pi / Sigma**
- **Journal of the London Mathematical Society**
- **Proceedings of the London Mathematical Society**
- **Journal of Number Theory**
- **Acta Arithmetica**
- **Mathematics of Computation** — computational verification of maximal gaps.

## 5. Formulation variants

- **Classical (1936):** p_{n+1} − p_n = O((log p_n)²).
- **Lim-sup = 1 (strong):** limit equals exactly 1.
- **Granville refinement:** limit ≥ 2e^{-γ} ≈ 1.1229, constant > 1 (implicit denial of Cramér's strong form).
- **Under RH:** p_{n+1} − p_n = O(√{p_n} · log p_n) (Cramér 1920).
- **Conditional on GRH / strong hypotheses:** tighter bounds.
- **Shanks form (1964):** p_{n+1} − p_n ~ (log p_n)². (Even stronger.)
- **Cramér probabilistic model:** integers are "random" with density 1/log n; conjecture follows from this model.
- **Short-interval conjecture:** π(x + (log x)²) − π(x) > 0 for all large x.

## 6. Known partial results + named walls

**Unconditional bounds on maximal prime gaps:**
- p_{n+1} − p_n ≪ p_n^{0.525} (Baker-Harman-Pintz 2001).
- This is much weaker than (log p_n)² but unconditional.

**Conditional (on RH):**
- p_{n+1} − p_n = O(√{p_n} log p_n) (Cramér 1920).

**Lower bounds on maximal gaps (Rankin-type):**
- Rankin (1938): infinitely often, gap ≥ c · log p · log log p · log log log log p / (log log log p)².
- **Ford, Green, Konyagin, Tao (2016, *Annals Math.*):** gap ≥ c · log p · log log p · log log log log p / (log log log p) — improved constant, removing a factor.
- **Ford, Green, Konyagin, Maynard, Tao (2018):** further refinements.

**Counter-heuristic (Maier 1985):** Maier's theorem implies that the naive Cramér model fails on short intervals, giving Granville's refined prediction c ≥ 2e^{-γ}.

**Named walls:**
- *Maier wall (1985)* — Maier's theorem shows that the Cramér probabilistic model undercounts prime-rich and prime-poor intervals.
- *RH-dependence wall* — the best conditional bound O(√{p} log p) is much weaker than (log p)².
- *Sieve wall* — sieve methods plateau at the 0.525 exponent (Baker-Harman-Pintz).
- *Large-gaps ground zero* — Rankin-type constructions show the lower bound is transcendental-growth-like, but cannot reach the full Cramér prediction.
- *Model refinement wall* — refined probabilistic models (Granville, Pintz) give different constants; which is correct is open.

## 7. Key references

**Original:**
- Cramér, H. (1936). "On the order of magnitude of the difference between consecutive prime numbers." *Acta Arith.* 2, 23–46.
- Cramér, H. (1920). "Some theorems concerning prime numbers." *Ark. Mat. Astr. Fys.* 15.

**Best modern surveys:**
- Granville, A. (1995). "Harald Cramér and the distribution of prime numbers." *Scand. Actuar. J.* 1, 12–28.
- Pintz, J. (2007). "Cramér vs. Cramér: on Cramér's probabilistic model for primes." *Funct. Approx. Comment. Math.* 37, 361–376.
- Soundararajan, K. (2007). "The distribution of prime numbers." in *Equidistribution in number theory, an introduction*.

**Key breakthroughs:**
- Ford, K., Green, B., Konyagin, S., Tao, T. (2016). "Large gaps between consecutive prime numbers." *Annals of Math.* 183, 935–974.
- Maynard, J. (2016). "Large gaps between primes." *Annals of Math.* 183, 915–933.
- Ford, K., Green, B., Konyagin, S., Maynard, J., Tao, T. (2018). "Long gaps between primes." *JAMS* 31, 65–105.
- Maier, H. (1985). "Primes in short intervals." *Michigan Math. J.* 32, 221–225.
- Baker, R. C., Harman, G., Pintz, J. (2001). "The difference between consecutive primes, II." *Proc. LMS* 83, 532–562.

## Status: OPEN; likely false in its strong form (constant 1) per Granville. No prize. Target journal: Annals of Math / JAMS / Inventiones.
