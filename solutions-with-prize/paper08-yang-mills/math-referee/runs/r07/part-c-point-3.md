# Referee Report C3: Coupling Regime Overlap

**Classification:** LIGHT
**Verdict:** SOUND

---

## Overview

The proof requires two distinct analytic tools operating in different coupling
regimes: the cluster expansion at strong coupling (small beta) and Balaban's
renormalization group at weak coupling (large beta, equivalently small g_0).
This report verifies that the two regimes overlap and that the transition is
handled correctly.

---

## Sub-point analysis

### (a) Overlap region

The cluster expansion is valid for beta < beta_max, where beta_max ~ 10^{14}
(a generous but finite bound established by the convergence radius of the
polymer expansion at strong coupling).

Balaban's RG construction requires g_0^2 < epsilon_0 for some epsilon_0
depending on the lattice geometry but not on the lattice size. Since
beta = 2N/g_0^2, the condition g_0^2 < epsilon_0 translates to
beta > 2N/epsilon_0 =: beta_min. In practice, epsilon_0 = O(1), so
beta_min = O(N).

For any N, the overlap region is

    beta_min < beta < beta_max

which is a wide interval (roughly [O(N), 10^{14}]). Within this interval, both
tools apply simultaneously, and the mass gap can be established by either
method. The preprint uses the cluster expansion result as input and Balaban's
RG to propagate it to the continuum.

**Finding:** SOUND. The overlap is wide and no fine-tuning is required.

### (b) Transition through the first RG steps

The first few RG steps (k = 0, 1, 2) have g_k^4 = O(1), so the perturbative
smallness that simplifies later steps is not yet available. This is handled
non-perturbatively: the cluster expansion (Section 5.7, Remark 1) controls
these initial steps without relying on g_k being small.

The bounded contribution K_0 from these finite-many non-perturbative steps is
absorbed into the overall constant C_0 in the mass gap bound. Since K_0 is
bounded (finitely many steps, each contributing a bounded amount), this
absorption is legitimate and does not affect the asymptotic behavior.

**Finding:** SOUND. The non-perturbative treatment of the initial RG steps is
the standard approach in constructive field theory.

---

## Summary

The coupling regime overlap is correctly handled. The cluster expansion and
Balaban's RG have a wide overlapping validity region, and the transition
through the first (non-perturbative) RG steps is controlled by the cluster
expansion. No gaps identified.
