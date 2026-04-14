# Goldbach's Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
- **MathWorld:** https://mathworld.wolfram.com/GoldbachConjecture.html
- **Original statement:** Letter from Christian Goldbach to Leonhard Euler, 7 June 1742. (Reproduced in Euler's correspondence.)
- **Prize source (expired):** https://www.math.tugraz.at/~elsholtz/WWW/papers/papers14faber.html (note on Faber/Bloomsbury prize)
- **AMS Notices article (million-dollar math):** https://www.ams.org/notices/200008/comm-millennium.pdf

## 2. Problem statement

**Strong (binary) Goldbach:**
> Every even integer n > 2 can be expressed as the sum of two primes:
> n = p + q,  p, q prime.

**Weak (ternary) Goldbach:**
> Every odd integer n > 5 can be expressed as the sum of three primes.
> (Equivalent formulation: every odd integer n > 7 is a sum of three odd primes.)

**Hardy-Littlewood quantitative (Strong):**
> The number r_2(n) of representations n = p + q satisfies
> r_2(n) ~ 2 C_2 · n / (log n)² · ∏_{p | n, p > 2} (p - 1)/(p - 2),
> where C_2 ≈ 0.66016 is the twin-prime constant.

## 3. Prize

**Faber & Faber / Bloomsbury Publishing USA prize (EXPIRED):**
- Amount: **$1,000,000 USD**.
- Offered: 20 March 2000 (coincident with publication of Apostolos Doxiadis's novel *Uncle Petros and Goldbach's Conjecture*).
- Conditions: "Submission by 15 March 2002; publication by 15 March 2004; solution must be published in a reputable mathematical journal and approved by a panel of judges appointed by Faber and Faber."
- **Status: EXPIRED** — the prize went unclaimed. No current monetary prize.

**Currently: no active prize.** Goldbach has historical publicity but no foundation-backed prize as of 2026.

Confirmation sources:
- C. Elsholtz, "Faber offers one million dollars for proof of Goldbach conjecture" (archived summary).
- Plus Maths: "Gold for Goldbach" (2000 launch announcement).
- Science Magazine (2000): "Million-Dollar Assault on Goldbach."

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics** — top target for a full proof of strong Goldbach.
- **Inventiones Mathematicae**
- **Publications Mathématiques de l'IHES**
- **Acta Mathematica**
- **JAMS**
- **Duke Mathematical Journal**
- **Compositio Mathematica**
- **Journal of Number Theory**
- **Mathematika**
- **Acta Arithmetica**

Historically significant venues:
- Helfgott's 2013 weak Goldbach was published as a monograph: *Annals of Mathematics Studies* 217 (Princeton UP).
- Chen's theorem (1973): *Scientia Sinica*.

## 5. Formulation variants

- **Strong (binary) Goldbach:** every even n > 2 = p + q. **OPEN.**
- **Weak (ternary) Goldbach:** every odd n > 5 = p + q + r. **PROVED (Helfgott 2013).**
- **Chen's theorem:** every sufficiently large even n = p + (P_2), where P_2 is a product of at most two primes. Proven 1973.
- **Goldbach-like conjectures:** every even n > 7 = sum of two odd primes (same as strong, refined).
- **Hardy-Littlewood quantitative form:** r_2(n) asymptotic.
- **Extended Goldbach:** every integer > 5 is sum of three primes. (Weaker; follows from weak Goldbach.)
- **Levy's conjecture:** every odd n > 5 = p + 2q, p, q primes.
- **Lemoine's conjecture:** every odd n > 5 = p + 2q.
- **Goldbach for polynomials over F_q:** analog; substantially different.

## 6. Known partial results + named walls

**Proven:**
- **Weak Goldbach (ternary) – Helfgott 2013:** every odd integer > 5 is a sum of three primes. Announced 2013, monograph 2015 (Princeton, *Annals of Math Studies* 217). Uses circle method + computer verification up to bound ~10³⁰.
- **Vinogradov (1937):** every sufficiently large odd integer is a sum of three primes (ineffective).
- **Chen (1973):** every sufficiently large even n = p + P_2.
- **Computational verification (Strong):** T. Oliveira e Silva verified for all even n ≤ 4 × 10^{18} (later extended to 10^{19} region).
- **Mostly-Goldbach:** the set of even integers NOT expressible as p + q has density 0 (Montgomery-Vaughan 1975).

**Named walls:**
- *Parity problem (Selberg)* — same wall as for twin primes; pure sieve methods cannot handle both primes simultaneously.
- *Circle method boundary* — for strong Goldbach, the major-arc/minor-arc decomposition leaks one prime compared to three-prime case.
- *Bilinear-form wall* — modern analytic methods rely on bilinear forms (Vaughan, Heath-Brown); doesn't suffice for strong Goldbach.
- *Explicit bound wall* — even if we could push Vinogradov's proof down from ~10^^^, Helfgott style, we'd still need a matching computational verification; for the strong Goldbach the tail is fundamentally different.

## 7. Key references

**Original:**
- Goldbach, C. Letter to Euler, 7 June 1742.

**Best modern surveys:**
- Wang, Y. (ed.) (2002). *Goldbach Conjecture*. World Scientific, Series in Pure Mathematics 4.
- Ribenboim, P. (1996). *The New Book of Prime Number Records*. Springer.
- Pintz, J. (2006). "Landau's problems on primes." *J. Théor. Nombres Bordeaux* 21, 357–404.

**Key breakthroughs:**
- Vinogradov, I. M. (1937). "Representation of an odd number as a sum of three primes." *Dokl. Akad. Nauk SSSR* 15, 291–294.
- Chen, J. R. (1973). "On the representation of a larger even integer as the sum of a prime and the product of at most two primes." *Scientia Sinica* 16, 157–176.
- Helfgott, H. A. (2013+). "The ternary Goldbach conjecture is true." arXiv:1312.7748. Monograph: *Annals of Math. Studies* 217 (2024/in prep.).
- Oliveira e Silva, T. Computational verification: https://sweet.ua.pt/tos/goldbach.html

## Status: OPEN (strong/binary); weak (ternary) PROVED 2013 by Helfgott. Prize EXPIRED (Faber/Bloomsbury, 2000–2002). Target journal: Annals of Mathematics.
