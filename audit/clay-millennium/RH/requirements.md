# Riemann Hypothesis — Requirements (itemized)

**Source:** `00-problem-statement.md` (Bombieri 2000)
**Clay §5d discipline:** every requirement must be ADDRESSED.

## Formal requirements

| # | Requirement | Bombieri source |
|---|---|---|
| 1 | **Every nontrivial zero** ρ of ζ(s) satisfies Re(ρ) = 1/2 | "Riemann hypothesis" statement |
| 2 | Argument must cover the **full critical strip** 0 < Re(s) < 1 (not just Re(s) = 1 boundary already known) | Implicit (trivial-zero / functional-equation symmetry) |
| 3 | Must not depend on unverified external conjectures (circularity) | Standard refereeing (§6e) |
| 4 | Analytic continuation / functional equation of ζ — already established, but the proof should be consistent with them | Bombieri §I setup |

## Acceptable proof shapes (Bombieri's survey)

Bombieri's survey lists classes of approaches; any of these, executed rigorously, qualifies:
- Direct analytic methods (zero-free regions extended to the whole strip)
- Operator-theoretic Hilbert-Pólya approach (spectrum of a self-adjoint operator = zeros)
- Connes-style noncommutative-geometry approach
- Random-matrix / Montgomery-Odlyzko heuristics upgraded to theorem
- Algebraic-geometry / Weil-style approach over a suitable curve

None is preferred by Clay; only correctness + §5d completeness matter.

## Non-required but customary

- Extension to Dirichlet L-functions (GRH) — NOT required for the Millennium prize; handled in our programme by a separate paper (paper13b-grh).
- Rate of convergence to Li(x) — follows as a corollary.

## Clay §5(c) note

Counterexample = off-critical-line zero. If exhibited, §5(c)(i) applies: full prize.
