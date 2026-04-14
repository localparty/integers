# Generalized Riemann Hypothesis (GRH) — Outlet Report

## 1. Official outlet

- **Wikipedia (authoritative secondary):** https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis
- **AIM RH portal:** https://aimath.org/WWN/rh/rh.pdf (American Institute of Mathematics, Conrey survey)
- **Encyclopedia of Mathematics:** https://encyclopediaofmath.org/wiki/Riemann_hypothesis_ (Generalized section)
- **Foundational paper:** Piltz, A. (1884) [first formulation for Dirichlet L-functions].

No dedicated prize foundation page; GRH is not on the Clay list, though the ordinary RH is.

## 2. Problem statement (verbatim-ish)

> All non-trivial zeros of every Dirichlet L-function L(s, χ) attached to a primitive Dirichlet character χ have real part equal to 1/2.

Equivalently: for every primitive χ, no Dirichlet L-function L(s, χ) has zeros in the open strip 0 < Re(s) < 1 off the critical line Re(s) = 1/2.

## 3. Prize

**None directly.** GRH is *not* a Clay Millennium Problem — only the classical RH is. Proving GRH would imply RH (take χ the trivial character) and thus claim the Clay $1M prize for RH, but a proof of RH alone would not prove GRH.

From the Clay Rules: the Clay prize is specifically for "the Riemann Hypothesis" as stated on their problem page. A proof restricted to ζ(s) alone suffices; GRH is a stronger statement.

## 4. Publication expectation

In descending prestige:

- **Annals of Mathematics** (Princeton) — primary target.
- **Inventiones Mathematicae** (Springer)
- **Acta Mathematica**
- **Publications Mathématiques de l'IHES**
- **Journal of the American Mathematical Society (JAMS)**
- **Duke Mathematical Journal**
- **Compositio Mathematica**

Partial progress / zero-density / explicit verification results typically land in:
- *Mathematics of Computation* (computational verification, e.g., Platt's verification up to 3.8 × 10¹³ zeros across 29B L-functions)
- *Journal of Number Theory*
- *Acta Arithmetica*

## 5. Formulation variants

- **GRH (Dirichlet):** standard — primitive Dirichlet L-functions.
- **Extended Riemann Hypothesis (ERH):** Dedekind zeta functions ζ_K(s) of arbitrary number fields K.
- **Grand Riemann Hypothesis (GRH_grand):** all automorphic L-functions in the Selberg class.
- **GRH for Hecke L-functions:** number-field analog for Hecke characters.
- **GRH for Artin L-functions:** with Artin conjecture, extends to non-abelian Galois L-functions.
- **Selberg class formulation:** axiomatic, covers all "reasonable" L-functions simultaneously.

Conditional statements on GRH are numerous (e.g., Miller-Rabin primality test polynomial runtime, Chebyshev's bias, Goldbach weak, primitive root bounds).

## 6. Known partial results + named walls

**Proven unconditionally:**
- Zero-free regions (log-free, Vinogradov-Korobov type) for Dirichlet L-functions.
- Infinitely many zeros on the critical line (Hardy's theorem adapted).
- Positive proportion on the critical line (Conrey 40% for ζ; analogous percentages for L-functions via Levinson-Conrey method).
- **Numerical verification:** Platt (2016) verified GRH for all primitive Dirichlet characters of conductor ≤ 400,000 up to height 10⁸; subsequent work has extended this significantly (30+ billion L-functions as of 2025).

**Named walls:**
- *Landau-Siegel zeros* — the long-standing failure to exclude real zeros near s=1 for real Dirichlet characters. Related to the Deuring-Heilbronn phenomenon.
- *Korobov-Vinogradov wall* — zero-free regions still log-free, not polynomial.
- *Selberg zero-density wall* — density estimates like N(σ,T) are limited by standard analytic methods.
- *GRH ↔ automorphy wall* — GRH for automorphic L-functions requires understanding of the automorphic spectrum (Langlands).

## 7. Key references

**Original statement:**
- Piltz, A. (1884). [formulated GRH for Dirichlet L-functions, per Wikipedia; primary sources lost/obscure]
- Riemann, B. (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Grösse." *Monatsber. Berlin. Akad.* (original ζ-only RH; predecessor).

**Best modern surveys:**
- Conrey, J. B. (2003). "The Riemann Hypothesis." *Notices AMS* 50, 341–353.
- Iwaniec, H. & Kowalski, E. (2004). *Analytic Number Theory*. AMS Colloquium Publications 53.
- Murty, M. R. & Murty, V. K. (1997). *Non-vanishing of L-functions and Applications*. Birkhäuser.

**Computational frontier:**
- Platt, D. J. (2016). "Numerical computations concerning the GRH." *Mathematics of Computation* 85, 3009–3027.

## Status: OPEN. No monetary prize (stronger than Clay RH, not on their list). Target journal: Annals of Mathematics.
