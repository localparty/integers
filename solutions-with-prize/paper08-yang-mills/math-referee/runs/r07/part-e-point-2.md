# Referee Report E2: Convergence of the Sum

**Classification:** LIGHT
**Verdict:** SOUND

---

## Overview

The final convergence argument requires that the sum Sigma C_k g_k^4
Delta-hat_k^2 is finite. This report verifies the doubly exponential
convergence arising from the interplay of polynomial coefficients and
exponential decay, and confirms that the starting constant C_0 is finite.

---

## Sub-point analysis

### (a) Doubly exponential convergence

The three factors in each summand have the following k-dependence:

- C_k ~ k^gamma (from the Gronwall bound, E1c),
- g_k^4 ~ 1/(b_0 k ln 2)^2 ~ 1/k^2 (from two-loop AF running),
- Delta-hat_k^2 ~ 4^{-k} * Pi_{j=0}^{k-1}(1 + O(g_j^4)).

The accumulated correction to 4^{-k} in Delta-hat_k^2 requires analysis.
The product Pi_{j=0}^{k-1}(1 + O(g_j^4)) converges to a finite nonzero limit
because the series Sigma g_j^4 ~ Sigma 1/j^2 < infinity (p-series with p=2).
By the standard criterion for infinite products, convergence of the sum of
terms implies convergence of the product. Therefore:

    Delta-hat_k^2 ~ C_prod * 4^{-k}

where C_prod = Pi_{j=0}^{infinity}(1 + O(g_j^4)) is a finite positive
constant.

The full summand is then:

    C_k g_k^4 Delta-hat_k^2 ~ C_prod * k^{gamma - 2} * 4^{-k}

The sum Sigma k^{gamma - 2} * 4^{-k} converges for ALL values of gamma.
This is immediate: for any polynomial p(k), the sum Sigma p(k) r^k converges
when |r| < 1 (here r = 1/4). The exponential decay 4^{-k} dominates any
polynomial growth in k.

The convergence is "doubly exponential" in the sense that 4^{-k} = e^{-k ln 4},
which decays exponentially in k, while k^{gamma-2} grows at most polynomially.
The ratio of consecutive terms approaches 1/4, giving a geometric rate of
convergence.

**Finding:** SOUND. The convergence of Sigma g_j^4 guarantees that the
accumulated corrections to Delta-hat_k^2 produce only a finite multiplicative
constant, and the resulting sum converges geometrically due to the 4^{-k}
factor.

**Impact on the claimed result:** This establishes that the infinite-volume
connected matrix element is a convergent sum, which is the final quantitative
input for the mass gap bound.

### (b) Starting constant C_0

At k=0, the lattice is at the finest scale, and:

- Delta-hat_0 ~ O(1) in lattice units (the physical gap times the initial
  lattice spacing),
- C_0 comes from the cluster expansion of Theorem 4, which provides
  exponential decay bounds on connected correlators.

The cluster expansion bound is governed by the Kotecky-Preiss criterion:
the activity of the polymer expansion must satisfy Sigma |z(gamma)| e^{a|gamma|}
<= a for each lattice site, where the sum is over polymers containing that
site. This is established in Section 4.3 under the small coupling condition
g_0 < g_crit. The resulting bound on C_0 is explicit and finite.

The fixed-point convergence formula:

    C_k = C* + (C_0 - C*) * 4^{-k} + corrections

requires only that C_0 < infinity to guarantee convergence to C*. Since the
Kotecky-Preiss constant provides a finite bound on C_0, this condition is
satisfied. The corrections (from the O(g_k^2 C_k) terms) are controlled by
the Gronwall bound and do not affect the convergence.

**Finding:** SOUND. The starting constant C_0 is explicitly bounded by the
Kotecky-Preiss criterion from the cluster expansion, and the recursion
converges to the fixed point C* = (4/3)C_new regardless of the precise value
of C_0.

**Impact on the claimed result:** The finiteness of C_0 is the base case of
the induction. Combined with the contractive recursion (E1), it establishes
that C_k remains bounded for all k and converges to C*.

---

## Summary

The convergence of the sum is sound. The doubly exponential convergence from
the 4^{-k} factor overwhelms all polynomial growth from the Gronwall bound
and the AF running coupling. The accumulated corrections to Delta-hat_k^2
produce only a finite multiplicative constant thanks to Sigma g_j^4 < infinity.
The starting constant C_0 is controlled by the cluster expansion. No gaps are
identified.
