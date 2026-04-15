# Referee Report D4: Single-Step Coefficient Bound

**Classification:** LIGHT
**Verdict:** SOUND

---

## Overview

The single-step coefficient bound combines the operator norm from Balaban's
effective action with the spectral lemma to produce the quantitative estimate
driving the RG induction. This report verifies the g_k^4 factor and confirms
that non-perturbative corrections are negligible.

---

## Sub-point analysis

### (a) The g_k^4 factor

The bound on the dimension-6 contribution to the effective action is:

    ||delta E_k^{d=6}|| <= C g_k^4

This follows from Balaban's operator norm bound: the dimension-6 coefficients
in the effective action satisfy |c_n^{(k)}| <= C_n g_k^{6-4} = C_n g_k^2 (by
the general bound |c_n^{(k)}| <= C_n g_k^{d_n - 4} from C1). The operator
norm of each dimension-6 basis element is O(g_k^2) per unit volume (from the
two additional field strengths beyond S_YM). Combining these gives
||delta E_k^{d=6}|| <= C g_k^4 per unit volume.

The spectral lemma (D3) with input M = C g_k^4 and dev >= 2 produces:

    |<1|delta E_k^{d=6}|1>_c| <= C_2 * C g_k^4 * Delta-hat^2
                                = C_new g_k^4 Delta-hat^2

The constant C_new = C_2 * C absorbs the spectral lemma constant C_2 and the
operator norm constant C. Both are k-independent (C_2 depends only on the
support radius R_0, and C is a Balaban constant).

**Finding:** SOUND. The g_k^4 prefactor arises cleanly from the dimension
counting, and the Delta-hat^2 suppression follows from dev >= 2 via the spectral
lemma.

### (b) Non-perturbative corrections

Two sources of non-perturbative corrections must be controlled:

1. **Large-field contributions:** Configurations outside Balaban's small-field
   domain Omega_s contribute O(e^{-c/g_k^{2 epsilon}}) to expectation values.
   On the asymptotically free trajectory g_k^2 ~ C/ln(k), this gives:

       e^{-c/g_k^{2 epsilon}} = e^{-c (ln k)^epsilon}

   which decays faster than any power of 1/ln(k). In particular, for any fixed
   power N:

       e^{-c/g_k^{2 epsilon}} << g_k^{2N} for k >> 1

   So large-field corrections are negligible compared to the perturbative
   g_k^4 Delta-hat^2 bound.

2. **Instanton contributions:** Classical instantons contribute
   O(e^{-8 pi^2/g_k^2}) to the path integral. On the AF trajectory:

       e^{-8 pi^2/g_k^2} = e^{-8 pi^2 ln(k)/C} = k^{-8 pi^2/C}

   This is power-law suppressed in k, hence negligible compared to
   g_k^4 = O(1/(ln k)^2). More precisely, the instanton contribution is
   exponentially small in 1/g_k^2 while the perturbative bound is polynomial
   in g_k^2, so the instanton contribution is beyond all orders.

   Furthermore, instanton contributions to gauge-invariant C-even operators
   themselves carry the instanton suppression factor, which is already included
   in Balaban's non-perturbative effective action. They do not represent an
   additional correction.

Both sources of non-perturbative corrections are exponentially suppressed
relative to the g_k^4 Delta-hat^2 bound. The single-step estimate is therefore
dominated by its perturbative content, with non-perturbative corrections
absorbed into the constant C_new.

**Finding:** SOUND. The exponential suppression of both large-field and
instanton contributions ensures they are negligible compared to the polynomial
bound g_k^4 Delta-hat^2.

---

## Summary

The single-step coefficient bound is sound. The g_k^4 prefactor follows from
standard dimension counting in Balaban's effective action, the Delta-hat^2
suppression follows from the spectral lemma with dev >= 2, and non-perturbative
corrections (large-field and instanton) are exponentially negligible on the
asymptotically free trajectory. No gaps are identified.
