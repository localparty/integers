# Strategy 32 — Cycle 4: Inverse Littlewood-Offord + Relative Gap

*Date: 2026-04-10, Cycle 4 of 10*

---

## Two new leads

### N3: Inverse Littlewood-Offord for eigenvector anti-structure
**Feasibility:** 5/10

Tao-Vu (2009, Annals): eigenvalue gaps of M + random perturbation
are ≥ n^{-C} iff the eigenvector components DON'T cluster in a
generalized arithmetic progression (GAP). The inverse L-O theorem
characterizes WHEN components cluster.

For our Weil form: eigenvector components involve {cos(x_i log p)},
which are TRANSCENDENTAL and EQUIDISTRIBUTED. They cannot cluster
in a GAP (arithmetic progressions have rational structure;
transcendental numbers avoid them by definition).

The chain: transcendental components → no GAP structure →
inverse L-O → anti-concentration → polynomial eigenvalue gap.

This avoids the "deterministic Tao-Vu" problem (N2 attack #6)
because we don't need the FULL random theory. We only need the
ANTI-CONCENTRATION part, which the inverse L-O theorem provides
for sequences without additive structure.

### N4: Relative gap persistence
**Feasibility:** 5/10

Jirak-Wahl: perturbation bounds for eigenspaces under a
RELATIVE gap condition. If ||perturbation|| / gap stays bounded
as perturbations accumulate, eigenvalue gaps persist.

For adding prime p_{N+1}: ||perturbation|| = (log p)/√p.
By PNT: log(p_N)/√p_N ~ log(N)/√(N log N) → 0.

If the gap after N primes is δ_N, and the perturbation norm
is ε_N ~ log(N)/√(N log N), then the relative condition is:
ε_N / δ_N < 1. This requires δ_N > ε_N ~ log(N)/√(N log N).

The numerical data: gap ~ 10^{-1.7N} for the discrete model.
ε_N ~ 1/√N. So δ_N << ε_N for large N. The relative condition
FAILS for the discrete model.

BUT: the discrete model has Cauchy conditioning artifacts. The
CONTINUOUS model's gaps might be much larger. Need computation
on the continuous L² operators.

Key computation: measure the CONTINUOUS eigenvalue gap of
QW_λ^N (not the discretized matrix) as a function of N.

---

## Launch plan

| Lead | Agent | Code directory |
|:--|:--|:--|
| N3 (inverse L-O) | Research + adversarial | — |
| N4 (relative gap) | Research + computation | /Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/code |
