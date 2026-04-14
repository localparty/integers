# Lindelöf Hypothesis — Outlet Report

## 1. Official outlet

- **Wikipedia (authoritative secondary):** https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis
- **Original paper:** Lindelöf, E. (1908). "Quelques remarques sur la croissance de la fonction ζ(s)," *Bull. Sci. Math.* 32, pp. 341–356.
- **Canonical reference:** Titchmarsh, *The Theory of the Riemann Zeta-Function* (2nd ed., Heath-Brown, Oxford 1986), Chapter XIII.
- **Modern reference:** Hugh L. Montgomery & Robert C. Vaughan, *Multiplicative Number Theory I*, Cambridge (2007).

No official prize foundation problem page — Lindelöf is treated as a corollary / partial-progress target of the Clay RH problem, not as a standalone prized problem.

## 2. Problem statement (verbatim-ish)

> For every ε > 0, ζ(1/2 + it) = O(t^ε) as |t| → ∞.

Equivalently: μ(1/2) = 0, where
μ(σ) = inf { a ∈ ℝ : ζ(σ + iT) = O(T^a) }.

A further equivalent form (Backlund, 1918–1919): for every ε > 0, the number of zeros of ζ in the rectangle { σ ≥ 1/2 + ε, T ≤ t ≤ T + 1 } is o(log T).

## 3. Prize

**None.** No standalone monetary prize. The problem is implicit in the Clay RH prize: the Clay $1M is contingent on proving RH, which would imply Lindelöf immediately. Proving Lindelöf alone would not claim the Clay prize but would be a landmark result.

## 4. Publication expectation

Expected journals for a resolution of Lindelöf (unconditional) in descending prestige:

- **Annals of Mathematics** (Princeton) — primary target; most recent major zeta/L-function breakthroughs appear here (Zhang bounded gaps 2014, Maynard small gaps 2015).
- **Inventiones Mathematicae** (Springer)
- **Journal of the American Mathematical Society (JAMS)**
- **Acta Mathematica**
- **Publications Mathématiques de l'IHES** (for deep structural breakthroughs)
- **Duke Mathematical Journal**
- **Compositio Mathematica**

Partial progress (e.g., μ(1/2) bound improvements) typically appears in:
- *Journal of the London Mathematical Society*
- *Mathematika*
- *Acta Arithmetica*
- *Transactions of the AMS*

## 5. Formulation variants

- **Classical form:** ζ(1/2 + it) = O(t^ε) for all ε > 0.
- **Convexity form:** μ(1/2) = 0.
- **Density form:** Backlund's zero-counting equivalent (above).
- **Mean-value form:** For every k ∈ ℕ, ∫₀ᵀ |ζ(1/2 + it)|^{2k} dt = O(T^{1+ε}).
- **Generalized Lindelöf:** same bounds for Dirichlet L-functions (implied by GRH).
- **Strong Lindelöf vs weak:** sometimes "weak" means μ(1/2) ≤ 1/6 (Hardy-Littlewood 1916–1923), "classical" is μ(1/2) = 0.

## 6. Known partial results + named walls

| Year | Author(s) | μ(1/2) bound |
|------|-----------|--------------|
| 1908 | Lindelöf (convexity) | ≤ 1/4 |
| 1916–1923 | Hardy–Littlewood | ≤ 1/6 |
| 1922 | Weyl (Weyl sums) | ≤ 1/6 refined |
| 1942 | Titchmarsh | ≤ 19/116 |
| 1963 | Min | ≤ 15/92 |
| 1986 | Bombieri–Iwaniec | ≤ 9/56 |
| 2002 | Huxley | ≤ 32/205 |
| 2017 | **Bourgain** | ≤ 13/84 ≈ 0.1548 |

**Named walls:**
- *Convexity barrier* — until Weyl sums, any bound below 1/4 required new techniques (van der Corput, Weyl differencing, exponent pairs).
- *Bombieri–Iwaniec method* — exponent pair methodology plateau.
- *Huxley's method* — geometric analytic method via Bombieri–Iwaniec plus large sieve.
- *Decoupling wall* — Bourgain's 2017 result uses decoupling inequalities (Bourgain–Demeter); further progress likely needs stronger decoupling or a fundamentally new approach.

## 7. Key references

**Original statement:**
- Lindelöf, E. (1908). *Bull. Sci. Math.* 32, 341–356.

**Best modern survey:**
- Ivić, A. (1985/2003). *The Riemann Zeta-Function: Theory and Applications*. Dover reprint. — comprehensive.
- Titchmarsh, E. C. (rev. Heath-Brown, 1986). *The Theory of the Riemann Zeta-Function*. Oxford. — canonical.
- Bourgain, J. (2017). "Decoupling, exponential sums and the Riemann zeta function." *JAMS* 30, 205–224.

**Recent surveys / progress:**
- Heath-Brown, D. R. (2017). "A new kth derivative estimate for exponential sums via Vinogradov's mean value theorem." *Proc. Steklov Inst. Math.* 296, 88–103.
- Huxley, M. N. (2005). "Exponential sums and the Riemann zeta function V." *Proc. LMS* 90, 1–41.

## Status: OPEN. No monetary prize (subsumed by Clay RH). Target journal: Annals of Mathematics.
