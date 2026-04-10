# Referee Report E1: Inductive Stability

**Classification:** MEDIUM
**Verdict:** SOUND

---

## Overview

The RG recursion for the connected matrix element takes the form
C_{k+1} = C_k/4 + C_new + O(g_k^2 C_k), with fixed point
C* = (4/3)C_new. This report verifies the three ingredients that make the
recursion contractive: the kinematic 1/4 factor, the wave function correction
controlled by Kato perturbation theory, and the Gronwall bound on the
accumulated product.

---

## Sub-point analysis

### (a) The 1/4 contraction factor

The contraction C_k -> C_k/4 originates from the kinematic relation
Delta-hat_k^2 = Delta-hat_{k+1}^2 / 4, which holds because doubling the
lattice spacing doubles Delta-hat (the dimensionless gap in lattice units).
This is purely kinematic: it reflects the rescaling of energies when measuring
the same physical gap Delta in units of the coarsened lattice.

The matrix element <1|E_k-down(0)|1>_c in the coarsened theory evaluates the
old state |1>_k on the new lattice Lambda_{k+1}. The change of lattice
introduces corrections through the wave function change |delta 1> (Term A2),
which is bounded by C g_k^4 / Delta-hat_k. These corrections enter the
recursion as O(g_k^2 C_k) and are explicitly accounted for in the recursion
relation.

The factor of 1/4 is exact at the kinematic level. The corrections are
multiplicative perturbations of order g_k^2, which vanish on the AF trajectory
and do not spoil the contraction for k >= k_0.

**Finding:** SOUND. The 1/4 contraction is a kinematic identity from lattice
rescaling, and the corrections from the change of lattice are properly absorbed
into the O(g_k^2 C_k) error term of the recursion.

**Impact on the claimed result:** The contraction factor is the engine of the
inductive scheme. Its kinematic origin makes it robust against perturbative
corrections.

### (b) Wave function correction (Term A2)

Term A2 accounts for the change in the ground state wave function when passing
from lattice Lambda_k to Lambda_{k+1}. The bound uses Kato perturbation theory
with inputs:

    ||E_k|| <= C g_k^4    (operator norm of the perturbation)
    gap = Delta-hat_k      (spectral gap of the unperturbed Hamiltonian)

The condition for Kato perturbation theory to apply is ||E_k|| << Delta-hat_k,
i.e., the perturbation must be small compared to the spectral gap. On the
asymptotically free trajectory:

- g_k^4 -> 0 as k -> infinity (logarithmically),
- Delta-hat_k = a_k Delta > 0, where Delta is the fixed physical mass gap
  and a_k is the lattice spacing, which grows with k.

Therefore g_k^4 / Delta-hat_k -> 0 as k -> infinity, and the Kato condition
is satisfied for all k >= k_0 with k_0 depending on the initial coupling g_0.

For the finitely many initial steps k < k_0, the cluster expansion from
Section 4 (Theorem 4) handles the bounds directly, without needing the
perturbative Kato framework. The transition from cluster expansion control to
Kato perturbative control is smooth because both yield finite bounds on C_k,
and the recursion picks up from whichever starting point k_0 is chosen.

**Finding:** SOUND. The Kato condition g_k^4 / Delta-hat_k -> 0 is guaranteed
by asymptotic freedom combined with the growth of the dimensionless gap, and
the initial steps are handled non-perturbatively by the cluster expansion.

**Impact on the claimed result:** Term A2 is the only source of corrections
that could destabilize the 1/4 contraction. The Kato bound ensures these
corrections are O(g_k^2 C_k), preserving the contractive structure.

### (c) The Gronwall bound

The accumulated product from the O(g_k^2 C_k) corrections is:

    Pi_{j=0}^{k-1} (1 + alpha g_j^2) <= k^{alpha / (b_0 ln 2)} = k^gamma

where the exponent is gamma = alpha / (b_0 ln 2). For SU(N) gauge theory:

    b_0 = 11N / (48 pi^2)

so:

    gamma = 48 pi^2 alpha / (11 N ln 2)

This exponent decreases with N, meaning the polynomial growth is milder for
larger gauge groups. For SU(2), gamma = 24 pi^2 alpha / (11 ln 2); for SU(3),
gamma = 16 pi^2 alpha / (11 ln 2).

The convergence of the sum Sigma C_k g_k^4 Delta-hat_k^2 is guaranteed by the
4^{-k} factor from Delta-hat_k^2, regardless of the polynomial growth k^gamma.
Specifically, k^gamma * 4^{-k} is summable for any finite gamma, since
exponential decay dominates polynomial growth.

The derivation of the Gronwall bound uses:

    ln Pi(1 + alpha g_j^2) = Sigma ln(1 + alpha g_j^2)
                            <= Sigma alpha g_j^2
                            ~ alpha Sigma 1/(b_0 j ln 2)
                            ~ (alpha / (b_0 ln 2)) ln k

which gives the polynomial bound k^gamma. The passage from the sum to the
logarithm is standard (ln(1+x) <= x for x > 0), and the asymptotic
g_j^2 ~ 1/(b_0 j ln 2) follows from one-loop running.

**Finding:** SOUND. The Gronwall bound yields polynomial growth that is
harmless against the exponential decay 4^{-k}. The N-dependence of gamma is
favorable for larger gauge groups.

**Impact on the claimed result:** The Gronwall bound ensures that the
accumulated errors from the O(g_k^2) corrections at each step do not
overwhelm the 4^{-k} convergence. This is the final ingredient needed to
close the induction.

---

## Summary

The inductive stability of the RG recursion is sound. The 1/4 contraction is
kinematic, the wave function corrections satisfy the Kato condition on the AF
trajectory, and the Gronwall bound yields only polynomial growth that cannot
compete with the exponential 4^{-k} decay. All three sub-points check out
without gaps.
