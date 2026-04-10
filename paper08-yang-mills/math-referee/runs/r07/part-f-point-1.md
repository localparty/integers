# Referee Report F1: OS Axioms - Simultaneous Verification

**Classification:** MEDIUM
**Verdict:** CLOSABLE GAP
**Estimated repair:** 1 sentence (Schwartz seminorm domination of L^1)

---

## Overview

The Osterwalder-Schrader axioms must be verified simultaneously for the
continuum Schwinger functions obtained from the lattice limit. The preprint
establishes the distributional bound |S_n(f)| <= n! C_0^n ||f||_{L^1}, which
must be reconciled with the corrected OS reconstruction theorem (1975) requiring
the stronger form OS0': |S_n(f)| <= C^n n! * p_N(f)^n for some Schwartz
seminorm p_N. This report examines the bound, the diagonal extraction, and the
treatment of coincident-point singularities.

---

## Sub-point analysis

### (a) OS0' linear growth condition

The preprint gives the distributional bound |S_n(f)| <= n! C_0^n ||f||_{L^1}.
The corrected OS reconstruction theorem (Osterwalder-Schrader 1975) requires
OS0': |S_n(f)| <= C^n n! * p_N(f)^n for some Schwartz seminorm p_N. The
question is whether the L^1 norm is controlled by a Schwartz seminorm.

For f in S(R^{4n}), the L^1 norm is dominated by a Schwartz seminorm:

    ||f||_{L^1} <= C * p_N(f)

where p_N(f) = sup_x (1+|x|)^{4n+1} |f(x)| is a Schwartz seminorm involving
polynomial weights. This follows immediately from the integrability of
(1+|x|)^{-(4n+1)} over R^{4n}: the polynomial weight in the seminorm provides
enough decay to make the integral converge, and the supremum controls the
pointwise values. The constant C depends only on the dimension 4n.

This domination is trivially true and entirely standard in distribution theory.
However, the preprint does not state it, leaving a presentational gap between
the bound as written and the OS0' condition as required by the 1975 theorem.

**Finding:** CLOSABLE GAP. The L^1 norm is dominated by Schwartz seminorms, so
the preprint's bound implies OS0'. A single sentence stating this domination
closes the gap. Estimated difficulty: 1 sentence.

**Impact on the claimed result:** Without this sentence, the bound appears to
use a weaker norm than OS0' requires. With it, the OS0' condition is satisfied
and the reconstruction theorem applies.

### (b) Diagonal extraction

The continuum Schwinger functions are obtained as subsequential limits of the
lattice Schwinger functions S_n^{(a)} as a -> 0. The diagonal argument extracts
a single subsequence a_j -> 0 along which S_n^{(a_j)} -> S_n for ALL n
simultaneously (not just for each n individually).

This diagonal extraction requires separability of the test function space
S(R^{4n}) for each n. Separability of S(R^{4n}) is standard: it is a nuclear
Frechet space, hence separable (with a countable dense subset given, e.g., by
polynomials times Gaussians with rational coefficients). The diagonal argument
over the countable index n is standard functional analysis (a countable
intersection of subsequences extracted by Banach-Alaoglu compactness).

**Finding:** SOUND. The separability of S(R^{4n}) and the diagonal extraction
are standard results requiring no additional argument.

**Impact on the claimed result:** The diagonal extraction ensures that a single
subsequence works for all n, which is necessary for the OS axioms to be verified
simultaneously (the axioms involve relations between S_n for different n, e.g.,
symmetry and positivity conditions).

### (c) Coincident-point singularities

For a massive gapped theory, the Schwinger functions have mild (integrable)
singularities at coincident points x_i = x_j. The lattice regularization
controls these singularities for all a > 0, and the mass gap ensures that the
regulated Schwinger functions converge to distributions (not pointwise
functions) as a -> 0.

The bound |S_n(f)| <= n! C_0^n ||f||_{L^1} is a distributional bound: it holds
after smearing with test functions f in S(R^{4n}), not as a pointwise bound on
S_n(x_1, ..., x_n). The preprint correctly treats S_n as elements of S'(R^{4n})
(tempered distributions), never as pointwise-defined functions. This is the
appropriate framework: the OS axioms require the Schwinger functions to be
tempered distributions satisfying certain positivity and symmetry conditions.

The coincident-point singularities are automatically handled by the
distributional framework. The smearing with Schwartz-class test functions
integrates over the singular set (which has measure zero) and produces finite
values bounded by the distributional estimate.

**Finding:** SOUND. The distributional treatment is correct and standard. The
coincident-point singularities pose no additional difficulty beyond what is
already handled by the distributional bounds.

**Impact on the claimed result:** This confirms that the Schwinger functions are
well-defined tempered distributions in the continuum limit, as required for the
OS reconstruction theorem.

---

## Summary

The OS axioms verification has one closable gap: the preprint should state
explicitly that ||f||_{L^1} <= C * p_N(f) for a Schwartz seminorm p_N, thereby
connecting its distributional bound to the OS0' condition required by the 1975
reconstruction theorem. This is a single sentence invoking a standard estimate.
The diagonal extraction and coincident-point treatment are sound. Total repair:
1 sentence.
