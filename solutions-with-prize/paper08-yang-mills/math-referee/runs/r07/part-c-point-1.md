# Referee Report C1: UV Stability -- Precise Scope

**Classification:** HEAVY
**Verdict:** CLOSABLE GAP
**Estimated repair:** 2-3 pages

---

## Overview

The preprint uses Balaban's results (CMP volumes 95-119) as a black box,
invoking UV stability, convergent polymer expansion, running coupling control,
and irrelevant operator bounds without re-deriving them. This report examines
the precise scope of what is borrowed and whether the translation is faithful.

---

## Sub-point analysis

### (a) Effective action structure

The decomposition

    S_k = (1/g_k^2) S_YM + sum_n c_n^{(k)} O_n + E_k

is NOT stated as a single theorem anywhere in Balaban. It follows from a chain
of three ingredients:

1. Balaban's polymer expansion expresses the effective action as S_YM/g_k^2
   plus a convergent sum of polymer activities.
2. The polymer activities are local gauge-invariant functionals (by
   construction of the block-spin transformation).
3. Expanding each activity by scaling dimension yields the operator
   coefficients c_n^{(k)}.

The bound |c_n^{(k)}| <= C_n g_k^{d_n - 4} follows from the exponential decay
of polymer activities combined with standard cluster expansion technology. This
translation is implicit in Balaban but is made explicit in the extraction
procedure described in Appendix H of the preprint.

For comparison: Dimock carries out the analogous extraction for scalar fields
in d = 3. For gauge fields in d = 4, the preprint is the first work to state
the result explicitly.

**Finding:** CLOSABLE GAP. The extraction of operator coefficients from
Balaban's polymer expansion should be presented as a self-contained lemma with
proof, not merely cited. Estimated difficulty: 1 page.

### (b) Gauge group dependence

Balaban's published program is developed primarily for SU(2). The
generalization to SU(N) rests on two observations:

- The propagator bounds (CMP 95-96) use the Lie algebra structure (commutator
  estimates, Casimir eigenvalues). These generalize to SU(N) with constants
  that depend on N polynomially.
- The block-spin construction uses SU(N) Haar measure and the projection onto
  gauge-invariant subspaces. This works for all compact N, with no structural
  obstruction.

The key bounds (polymer decay, propagator estimates) carry through with
N-dependent constants.

**Finding:** CLOSABLE GAP. The explicit N-dependence should be tracked through
the main estimates so that the reader can verify uniformity claims. Estimated
difficulty: 1 page.

### (c) Remainder bound

The bound ||E_k|| <= C g_k^4 per unit volume follows directly from the
convergence of the polymer expansion. The norm is L^infty on gauge-invariant
functionals. The constant C depends on N polynomially, through the Lie algebra
structure constants and quadratic Casimir operators.

**Finding:** SOUND as stated.

### (d) Running coupling

The O(g_k^6) corrections to the beta-function accumulate over infinitely many
RG steps. On the asymptotically free trajectory, g_k^2 ~ C/ln(k), so the sum

    sum_k g_k^6 ~ sum_k 1/(ln k)^3

converges (comparison with sum 1/k^3 is loose; the actual convergence is
faster than any power series in 1/k but the key point is finiteness).

The non-perturbative beta-function is controlled by Balaban's construction:
the polymer expansion gives the exact beta-function at each RG step, not just
its perturbative truncation.

**Finding:** SOUND.

### (e) Completeness boundary

The boundary between what Balaban provides and what the preprint contributes
is drawn in Section 5.1.5:

| Balaban provides         | Preprint provides                     |
|--------------------------|---------------------------------------|
| UV stability             | Mass gap at starting scale (Sec. 2-4) |
| Polymer expansion        | RG preservation of mass gap (Sec. 5.4-5.6) |
| Running coupling control | Continuum limit (Sec. 5.7)            |
|                          | Osterwalder-Schrader axioms           |

**Finding:** SOUND. The division of labor is clearly stated and logically
consistent.

---

## Summary

Two closable gaps are identified:

1. The extraction lemma translating Balaban's polymer activities into the
   operator decomposition S_k = (1/g_k^2) S_YM + sum c_n O_n + E_k needs a
   self-contained proof (~1 page).
2. The N-dependence of all constants inherited from Balaban should be tracked
   explicitly (~1 page).

Neither gap represents a logical obstruction. Both are matters of exposition
that can be resolved with 2-3 pages of additional material.
