# Collatz Conjecture (3n+1 Problem) — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Collatz_conjecture
- **MathWorld:** https://mathworld.wolfram.com/CollatzProblem.html
- **Bakuage prize announcement:** https://www.prnewswire.com/news-releases/bakuage-offers-prize-of-120-million-jpy-to-whoever-solves-collatz-conjecture-math-problem-unsolved-for-84-years-301326629.html
- **Lagarias's annotated bibliography:** Lagarias, J. C. (various updates). "The 3x + 1 Problem: An Annotated Bibliography." arXiv.
- **Original paper:** Collatz, L. (1937). Unpublished notes / problem stated in 1937.

## 2. Problem statement

Define the Collatz function on positive integers:
T(n) = n / 2   if n even;
T(n) = 3n + 1   if n odd.

**Collatz Conjecture:**
> For every positive integer n, the iterated sequence n, T(n), T(T(n)), ... eventually reaches 1.

**Alternative formulation (Syracuse function):**
For n odd, define S(n) = (3n + 1) / 2^{ν_2(3n+1)} (divide out all 2s). Then Collatz ≡ for every odd n > 1, the iterated S-sequence reaches 1.

**Stopping-time form:** For every n, the total stopping time σ(n) = min{k : T^k(n) = 1} is finite.

**Strong Collatz:** σ(n) ≤ C · log n for some constant C (believed true; stronger than bare Collatz).

## 3. Prize

Multiple prizes have been offered over time:

**Active prize:**
- **Bakuage Co., Ltd. (Japan, 2021):** 120,000,000 JPY (~US$1.085M at 2021 JPY/USD rates).
  - Announced: 7 July 2021.
  - Condition: must be published in a reputable mathematical journal and verified by a committee.
  - Source: https://www.prnewswire.com/news-releases/bakuage-offers-prize-of-120-million-jpy-to-whoever-solves-collatz-conjecture-math-problem-unsolved-for-84-years-301326629.html
  - Status as of 2026: still active per MathPrize.net and Bakuage announcements.

**Historical / informal prizes:**
- **Paul Erdős (personal):** US$500. Famous quote: "Mathematics may not be ready for such problems." Erdős died 1996; the $500 is likely subsumed in the general Erdős prize system (administered by his literary executors / collaborators).
- **John Conway:** reportedly offered $1,000 for a proof (per informal reports, not verified on his estate's page).
- **Althöfer (Jena, Germany):** a small list of prizes documented at https://althofer.de/collatz-prizes.html.

**Informal:** numerous other individual mathematicians have offered small prizes over the years.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics** — would be the top venue for a full resolution.
- **Forum of Mathematics, Pi** — Tao's 2019 almost-all-orbits result published here.
- **Inventiones Mathematicae**
- **JAMS**
- **Duke Mathematical Journal**
- **Acta Mathematica**
- **Compositio Mathematica**
- **The American Mathematical Monthly** — many historical/pedagogical papers.
- **Journal of Number Theory**
- **Math. Comp.** — computational verification.
- **Experimental Mathematics**

Tao's 2022 paper on Collatz almost-all orbits: *Forum of Mathematics, Pi* (2022).

## 5. Formulation variants

- **Standard (3n+1):** as stated.
- **"Shortcut" / Syracuse (3n+1)/2^k:** iterate only on odd steps.
- **Generalized Collatz (αn + β):** replace 3 with α, 1 with β, generic dynamics.
- **Hailstone numbers:** the sequence is sometimes called hailstone.
- **Stopping-time form:** finiteness of σ(n).
- **No non-trivial cycles:** no cycle other than the trivial (1 → 4 → 2 → 1) cycle.
- **No divergent trajectories:** no starting n produces an unbounded orbit.
- **Almost-all orbits:** for "almost every" n, orbit reaches below 1/2^k · n (Tao 2019, *Forum of Math. Pi*).
- **Density Collatz:** lower density of n with stopping time ≤ f(n) = 1 for various f.
- **Undecidability (Conway-type):** Conway (1972) showed some generalized Collatz-type functions are Turing-undecidable.
- **p-adic Collatz:** reformulate via 2-adic integers.

## 6. Known partial results + named walls

**Proven:**
- **Verified for all n ≤ 2.95 × 10^{20}** (Barina 2020; distributed computations ongoing).
- **Terras (1976):** almost every n has finite stopping time (in the density sense).
- **Korec (1994):** every n has a subsequent iterate below n^{0.7925}.
- **Tao (2022, *Forum Math. Pi*):** "Almost all orbits of the Collatz map attain almost bounded values." For almost every n (logarithmic density), there exists k with T^k(n) ≤ f(n) for any fixed function f → 0. This is the strongest known general result.
- **Conway (1972):** generalized Collatz problems can be Turing-undecidable (FRACTRAN); interpreted by some as evidence that a simple proof is unlikely.
- **No short cycles:** computational verification — no non-trivial cycle of length ≤ 186,265,759,595 (Simons-Lagarias 2003; many extensions).

**Named walls:**
- *Undecidability analog wall* — Conway (1972) showed Collatz generalizations are Turing-undecidable. This is often cited as explanation why the problem is hard.
- *Parity wall* — proving finiteness requires bounding the *expected* growth rate; on average, Collatz steps shrink n by factor 3/4, but proving this rigorously for all n (not just almost-all) is open.
- *Unbounded orbit wall* — no proof excludes infinite orbits.
- *Cycle non-existence wall* — no proof that trivial cycle is the only cycle.
- *Tao's log-density wall* — Tao (2019) reached "almost all orbits" in log-density sense; extending to *all* n is the remaining gap.
- *Erdős's ready-mathematics wall* — "Mathematics may not be ready" — there is no established machinery that directly attacks random-like iterated dynamics over ℤ.

## 7. Key references

**Original:**
- Collatz, L. (1937). Problem stated; formally attributed in Lagarias's bibliography.
- Conway, J. H. (1972). "Unpredictable iterations." *Proc. 1972 Number Theory Conf.*, Univ. of Colorado, 49–52.

**Best modern surveys:**
- Lagarias, J. C. (1985). "The 3x + 1 problem and its generalizations." *Amer. Math. Monthly* 92, 3–23.
- Lagarias, J. C. (ed.) (2010). *The Ultimate Challenge: The 3x+1 Problem*. AMS.
- Tao, T. (2019 blog post): https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/

**Key breakthrough:**
- Tao, T. (2022). "Almost all orbits of the Collatz map attain almost bounded values." *Forum Math. Pi* 10, e12.
- Terras, R. (1976). "A stopping time problem on the positive integers." *Acta Arith.* 30, 241–252.
- Korec, I. (1994). "A density estimate for the 3x+1 problem." *Math. Slovaca* 44.

**Computational:**
- Barina, D. (2020). "Convergence verification of the Collatz problem." *J. Supercomput.*

## Status: OPEN. Bakuage prize ACTIVE (120M JPY ≈ $1.08M). Target journal: Annals / Forum Math. Pi.
