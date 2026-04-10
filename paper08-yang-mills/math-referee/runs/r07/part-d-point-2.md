# Referee Report D2: Stability of Boltzmann Deviation Order

**Classification:** HEAVY
**Verdict:** SOUND

---

## Overview

This is THE critical point of the entire paper. The mass gap preservation
argument rests on showing that dev(delta E_k^{d=6}) >= 2 non-perturbatively at
every RG step. This ensures that the dimension-6 correction to the effective
action cannot destabilize the mass gap. The argument chain is:

1. By (B1), delta E_k^{d=6} has a convergent Taylor expansion.
2. The dim-6, C-even, gauge-invariant operators are exhaustively classified.
3. All classified operators have dev >= 2.
4. The linear combination lemma: convergent sums preserve deviation order.
5. Therefore dev(delta E_k^{d=6}) >= 2 non-perturbatively.

Each link in this chain is examined below.

---

## Sub-point analysis

### (a) Definition of Boltzmann deviation order

Definition D.2 defines dev(O) >= p in terms of factoring p powers of
(e^{E_m - E_{n_j}} - 1) from the spectral weight of the operator O. This is
STRONGER than the intuitive notion "matrix element vanishes to order p in
Delta-hat" because it requires the factorization at the level of individual
spectral weights w(alpha, n_1, ..., n_R), not just at the level of the summed
expectation value.

The spectral lemma (D3) then converts this microscopic factorization into the
macroscopic bound:

    |<1|O|1>_c| <= C_p M Delta-hat^p

where M = ||O|| is the operator norm. The two-level structure (definition at the
level of individual weights, consequence at the level of the sum) is essential:
it ensures that cancellations between terms in the spectral sum cannot reduce
the deviation order below p.

**Finding:** SOUND. The definition is well-posed, the spectral lemma correctly
extracts the consequence, and the two-level structure is the right approach.

### (b) Linear combination lemma

**Statement:** If each O_i has dev >= p with bounded norm, and
sum |c_i| ||O_i|| < infinity, then sum c_i O_i has dev >= p.

**Proof (Section 5.5.3):** The spectral representation of the sum is indexed by
pairs (i, alpha_i), where alpha_i ranges over the spectral labels of O_i. Each
term inherits the factorization from its parent operator O_i. The sum over i is
absolutely convergent by hypothesis, so the combined spectral weight is
well-defined.

The one subtlety: different operators O_i may have different temporal extents
R_i. This is handled by zero-padding: an operator of extent R_i < R_max is
embedded into extent R_max by inserting identity time-slices. At these identity
slots, the Boltzmann factors are:

- Diagonal (n_j = m): (e^{E_m - E_m} - 1) = 0. The zero is preserved.
- Off-diagonal (n_j != m): (e^{E_m - E_{n_j}} - 1) contributes a nonzero
  deviation factor. The factorization count is not reduced.

Since the identity insertion does not reduce the number of extractable deviation
factors, the padded operator retains dev >= p. The sum then inherits dev >= p
by absolute convergence.

**Finding:** SOUND. The zero-padding construction is correct and the absolute
convergence condition is verified by (B1).

### (c) Role of (B1) analyticity

The convergent Taylor expansion from (B1) ensures that delta E_k^{d=6} is a
genuine linear combination of monomials (dimension-6 gauge-invariant operators)
within the analyticity domain. The spectral lemma requires this expansion to
converge on configurations contributing to <1|delta E_k^{d=6}|1>_c.

In the gapped phase, typical configurations (those dominating the path integral)
lie well within the small-field region Omega_s. This is the content of
Balaban's large-field suppression: configurations outside Omega_s are suppressed
by factors of exp(-c/g_k^{2 epsilon}), contributing negligibly to expectation
values.

The one-particle state |1> is a low-energy state. Its overlap with large-field
configurations is exponentially suppressed because large-field configurations
carry action of order 1/g_k^2 >> 1 per unit volume, while the one-particle
state has energy Delta-hat above the vacuum. The energy gap Delta-hat is O(1) in
lattice units, much smaller than the large-field threshold.

Therefore the Taylor expansion converges on the configurations that matter, and
the linear combination lemma applies.

**Finding:** SOUND. The interplay between (B1) analyticity and Balaban's
large-field suppression is correctly exploited.

### (d) Perturbative to non-perturbative transition

The previous referee (r05, Point 1d) initially flagged this as a GENUINE GAP,
later revised to CLOSABLE after careful examination. The concern was: the
dimension-6 operators are classified perturbatively (by their engineering
dimension), but the deviation order argument must hold non-perturbatively.

The resolution rests on the EXHAUSTIVENESS of the classification:

1. The dimension-6 projection is defined non-perturbatively by the scaling
   dimension of operators in Balaban's effective action. The (B1) convergent
   expansion gives an unambiguous decomposition by dimension.

2. S_YM is the UNIQUE dimension-4 operator. This is a structural fact
   (confirmed in Part B), not a perturbative approximation. It means the
   dimension-6 projection is well-defined: delta E_k^{d=6} is everything in the
   effective action except the S_YM/g_k^2 term and the remainder E_k.

3. The non-perturbative operator delta E_k^{d=6} is not "identified with
   Tr(DF)^2 perturbatively." Rather, it IS a convergent sum of operators, all
   of which belong to structural classes with dev >= 2. The convergence is
   guaranteed by (B1), and the classification is guaranteed by completeness of
   the Luscher-Weisz basis (D1).

4. The deviation order of each structural class (dev >= 2 for all dim-6 C-even
   operators) is a consequence of having two covariant derivatives, which is a
   structural property independent of the coupling strength.

**Finding:** SOUND. The classification + linear combination approach correctly
bridges the perturbative/non-perturbative divide. No operator is being
"identified perturbatively" -- the entire argument is structural.

### (e) Structural vs kinematic zero

The diagonal vanishing (e^{E_1 - E_1} - 1)^2 = 0 is structural: it follows
from the operator class (two derivatives produce two deviation factors). The
concern is whether cancellations in the spectral sum could effectively reduce
dev below 2.

This cannot happen because the linear combination lemma (sub-point b) operates
at the level of individual (alpha, n) terms in the spectral representation.
Each term carries at least 2 deviation factors by construction. When terms are
summed with alternating signs, the deviation factors are not affected:

    sum_alpha c_alpha * [prod_{j in S} (e^{E_m - E_{n_j}} - 1)] * w_alpha

The factors (e^{E_m - E_{n_j}} - 1) multiply w_alpha, and the sum over alpha
preserves the factored form. Cancellation between different alpha terms can
reduce the magnitude of the sum but cannot remove the (e^{...} - 1) factors
because these are multiplicative, not additive, in each term.

**Finding:** SOUND. The distinction between structural zeros (multiplicative
factors in each term) and kinematic zeros (cancellations between terms) is
correctly maintained.

---

## Summary

The stability of Boltzmann deviation order is the heart of the mass gap
preservation argument. All five sub-points are sound:

- The definition of deviation order is well-posed and stronger than naive
  vanishing conditions.
- The linear combination lemma correctly handles sums, including the
  zero-padding subtlety for different temporal extents.
- The (B1) analyticity condition ensures convergence on the relevant
  configuration space.
- The perturbative-to-non-perturbative transition is handled by exhaustive
  structural classification, not by perturbative identification.
- Structural zeros (deviation factors) are preserved under linear combination.

The previous referee's concerns (r05) have been adequately addressed by the
classification + linear combination lemma approach. No gaps remain.
