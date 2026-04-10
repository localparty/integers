# Riemann Hypothesis — Official Clay Problem Description

**Author:** Enrico Bombieri
**Source:** https://www.claymath.org/millennium/riemann-hypothesis/
**PDF:** https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf
**Saved:** 2026-04-10

---

## The Statement

**Riemann Hypothesis.** The nontrivial zeros of ζ(s) have real part equal to 1/2.

Equivalently: all zeros of the function ξ(t) = (1/2)s(s−1)π^{−s/2}Γ(s/2)ζ(s)
with s = 1/2 + it are real.

## The Zeta Function

ζ(s) := Σ_{n=1}^∞ 1/n^s, defined for Re(s) > 1, extends to all of C as a
meromorphic function with only a simple pole at s = 1, residue 1.

**Functional equation:**
    π^{−s/2} Γ(s/2) ζ(s) = π^{−(1−s)/2} Γ((1−s)/2) ζ(1−s)

**Euler product:**
    ζ(s) = ∏_p (1 − p^{−s})^{−1}, valid for Re(s) > 1

**Trivial zeros:** s = −2, −4, −6, ...
**Non-trivial zeros:** All in the critical strip 0 < Re(s) < 1.
RH asserts they all have Re(s) = 1/2.

## Key Points from Bombieri's Description

### Section I: The Problem
- The functional equation in symmetric form (equation 1)
- Riemann's original memoir (1859) obtained an analytic formula for
  the number of primes up to a preassigned limit
- The zeros counting: N(T) ~ (T/2π)log(T/2π) − T/2π
- Riemann's original statement: "it is very likely that all zeros are real"

### Section II: History and Significance
- Connection to prime distribution: π(x) = Li(x) + O(√x log x) iff RH
- The Riemann Hypothesis is the prototype for a general class: L-functions
  (automorphic representations, arithmetic varieties) should satisfy GRH
- The Ramanujan property: local factors satisfy a local RH
- L-functions of Maass waveforms: simplest non-geometric example
- Hecke operators T_n, eigenvalues λ_f(n), associated L-functions
- "Not a single example of validity or failure of a Riemann hypothesis
  for an L-function is known to this date"
- "may require attacking much more general problems, by means of
  entirely new ideas"

### Section III: Evidence
- Numerical verification for first 10^13 zeros
- Selberg's theorem: positive proportion of zeros on the critical line
- Levinson: at least 1/3 of zeros on the critical line
- Conrey: at least 2/5 of zeros
- GUE conjecture (Montgomery-Odlyzko): zero spacing statistics match
  random matrix theory

### Section IV: Approaches
- The Hilbert-Polya conjecture: zeros as eigenvalues of a self-adjoint operator
- Connes' trace formula approach
- The function field analogue (Weil, Deligne) — proved
- de Branges' approach via de Branges spaces

### Section V: Further Reading
- Iwaniec and Sarnak survey of analytic properties

## What Constitutes a Proof

A proof must rigorously establish that ALL nontrivial zeros of ζ(s)
have Re(s) = 1/2. This means:
1. Every zero ρ with 0 < Re(ρ) < 1 satisfies Re(ρ) = 1/2
2. The proof must be unconditional (not assume GRH for other L-functions)
3. Numerical evidence alone is insufficient

Bombieri notes that the solution "may require attacking much more general
problems, by means of entirely new ideas" — suggesting that approaches
through L-functions and the Langlands program are legitimate.

## The Extension to L-Functions (GRH)

Bombieri emphasizes that RH is "the prototype of a general class" — the
Generalized Riemann Hypothesis (GRH) for all L-functions. The most
important cases:
- Dirichlet L-functions L(s, χ)
- Hecke L-functions (modular forms)
- L-functions of Maass waveforms
- Artin L-functions
- Automorphic L-functions on GL(n)

## References

- Bombieri, E. "Problems of the Millennium: The Riemann Hypothesis."
  Clay Mathematics Institute official problem description.
- Riemann, B. "Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse." 1859.
- Iwaniec, H. and Sarnak, P. "Perspectives on the analytic theory of L-functions." 2000.
- Connes, A. "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function." 1999.
- Deligne, P. "La conjecture de Weil. I." Publ. Math. IHES 43, 1974.

## Web Sources

- Clay Mathematics Institute: https://www.claymath.org/millennium/riemann-hypothesis/
- Wikipedia: https://en.wikipedia.org/wiki/Riemann_hypothesis
