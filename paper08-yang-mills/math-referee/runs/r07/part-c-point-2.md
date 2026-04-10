# Referee Report C2: Large-Field / Small-Field Decomposition

**Classification:** MEDIUM
**Verdict:** SOUND

---

## Overview

The large-field / small-field decomposition is a standard ingredient of
constructive field theory that separates the functional integral into a region
where perturbative control holds (small field) and a region suppressed by the
Boltzmann weight (large field). This report verifies the three components of
the decomposition as used in the preprint.

---

## Sub-point analysis

### (a) Small-field condition

The small-field region Omega_s is defined by the condition |F_{mu nu}| < p(g_k)
where

    p(g_k) = g_k^{1 - epsilon},    epsilon ~ 1/10 fixed.

Within Omega_s, the polymer expansion converges and the analyticity properties
(B1)-(B2) hold. The dimension-6 classification of irrelevant operators is valid
in Omega_s because the Taylor expansion of polymer activities converges in the
small-field domain.

The choice of exponent 1 - epsilon is standard: it must satisfy two competing
requirements. The threshold must be large enough that the large-field region is
exponentially suppressed (requiring 1 - epsilon > 1/2), and small enough that
the polynomial bounds on the effective action hold (requiring 1 - epsilon < 1).
The value epsilon ~ 1/10 satisfies both with room to spare.

**Finding:** SOUND.

### (b) Large-field suppression

The large-field contribution is bounded by O(e^{-c/g_k^{2 epsilon}}). On the
asymptotically free trajectory, g_k^2 ~ C/ln(k), so

    e^{-c/g_k^{2 epsilon}} ~ e^{-c (ln k)^epsilon}

which decays faster than any power of 1/k. Meanwhile, the small-field
contribution to the mass gap bound is

    g_k^4 Delta_k^2 ~ k^{-2} 4^{-k}

(the 4^{-k} coming from the volume factor at scale k). Therefore the
large-field contribution is negligible compared to the small-field error at
every RG step, and the sum over steps converges.

**Finding:** SOUND. The hierarchy of scales is correctly identified and the
suppression is more than sufficient.

### (c) Gauge invariance of the small-field condition

The condition |F_{mu nu}| < p(g_k) as literally stated is NOT gauge-invariant,
since F_{mu nu} transforms in the adjoint representation. However, Balaban's
actual construction uses a gauge-invariant formulation. The small-field
condition is imposed on the plaquette variable U_P:

    Re Tr U_P > 1 - a^4 p(g_k)^2

This condition IS gauge-invariant (the trace of the plaquette is unchanged
under gauge transformations U_P -> g U_P g^{-1}). For small lattice spacing,
the two formulations agree to leading order since

    Re Tr U_P = N - (a^4 / 2) |F_{mu nu}|^2 + O(a^6).

The preprint's notation is slightly informal but the underlying construction
is correct.

**Finding:** SOUND. The gauge-invariant formulation via plaquette variables is
the one actually used, consistent with Balaban's framework.

---

## Summary

All three components of the large-field / small-field decomposition are sound.
The small-field threshold is standard, the large-field suppression is more than
sufficient on the AF trajectory, and the gauge invariance of the decomposition
is correctly handled through the plaquette formulation. No gaps identified.
