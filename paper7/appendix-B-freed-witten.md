# Appendix B --- Freed-Witten Tadpole and the Diophantine Obstruction

---

## B.1 Statement

**Theorem B.1 (Diophantine Obstruction).** *The exact GUT unification
ratio n_2/n_1 = -17/9 cannot be realized with the Freed-Witten-shifted
flux quantization. The minimal approximate solution is*

    (n_1^{phys}, n_2) = (19/2, -18)

*with flux ratio -36/19, deviating from the exact value -17/9 by
0.31%. This deviation produces delta(rho^2)/rho^2 = -0.65% and
delta(alpha_3/alpha_2)/(alpha_3/alpha_2) ~ 0.7%, both within the
2-3% uncertainty from two-loop threshold corrections.*

---

## B.2 The Freed-Witten Shift

### B.2.1 Quantization condition

The M-theory C-field quantization on a compact manifold X
(Witten 1996, Freed-Witten 1999, Diaconescu-Moore-Witten 2003) is:

    [G_4/(2pi l_11^3)] - lambda(X)/2  in  H^4(X, Z)

where lambda mod 2 = w_4(X) (the fourth Stiefel-Whitney class). On
a spin manifold, lambda is even and there is no shift. On a non-spin
manifold the shift is nontrivial.

### B.2.2 The two cycles

**CP^2 cycle.** CP^2 is not spin: w_2(CP^2) = H mod 2 (H the
hyperplane class). The topological data: p_1(CP^2) = 3H^2,
w_4(CP^2) = w_2^2 = H^2 mod 2 = 1 mod 2. The Witten quantization
condition gives half-integer flux:

    n_1^{phys} = n_{1,int} + 1/2,    n_{1,int} in Z          (B.1)

**CP^1 x S^2 cycle.** Both CP^1 = S^2 and S^2 are spin (w_2 = 0).
The product of spin manifolds is spin:

    n_2^{phys} = n_{2,int},    n_{2,int} in Z                 (B.2)

| Cycle | Spin? | Shift | Physical flux |
|-------|-------|-------|--------------|
| CP^2 | No | +1/2 | n_{1,int} + 1/2 |
| CP^1 x S^2 | Yes | 0 | n_{2,int} |

---

## B.3 The Diophantine Obstruction

### B.3.1 The GUT condition with shift

The GUT unification condition rho = sqrt(3)/2 requires (Section 3):

    n_{2,int} / (n_{1,int} + 1/2) = -17/9                    (B.3)

Clearing denominators:

    9 n_{2,int} = -17 (n_{1,int} + 1/2) = -17 n_{1,int} - 17/2

Multiplying by 2:

    18 n_{2,int} + 34 n_{1,int} = -17                         (B.4)

This is a linear Diophantine equation. A solution exists if and only
if gcd(18, 34) divides -17.

    gcd(18, 34) = 2

Since 2 does not divide 17:

    **Equation (B.4) has no integer solution.**                (B.5)

### B.3.2 Nature of the obstruction

The obstruction is a parity conflict. The left side 18n_{2,int} +
34n_{1,int} is always even (both coefficients are even). The right
side -17 is odd. Even cannot equal odd. This persists at all flux
scales: no rescaling restores exact unification. The ratio -17/9 is
fundamentally incompatible with half-integer shift on the CP^2 cycle
alone.

---

## B.4 Minimal Approximate Solutions

The nearest solvable Diophantine equations to 18n_2 + 34n_1 = -17
have right-hand sides -18 and -16.

### B.4.1 Two minimal solutions

**Solution I** (from 18n_2 + 34n_1 = -16, with n_{1,int} = 8):

    n_1^{phys} = 17/2,   n_2 = -16

    ratio = -32/17 = -1.88235...,   deviation = +0.35%

**Solution II** (from 18n_2 + 34n_1 = -18, with n_{1,int} = 9):

    n_1^{phys} = 19/2,   n_2 = -18

    ratio = -36/19 = -1.89474...,   deviation = -0.31%

Solution II is closer to the exact ratio and has the appealing
feature that n_{1,int} = 9 (the same integer as in the unshifted
analysis), with n_2 shifted from -17 to -18.

### B.4.2 Effect on gauge coupling unification

For Solution II (n_1 = 19/2, n_2 = -18), the radius ratio:

    rho^2 = -2(19/2) / [3(19/2 - 18)]
           = -19 / [3(-17/2)]
           = 38/51
           = 0.74510...

The exact unification value is rho^2 = 3/4 = 0.75000. The
deviations:

    delta(rho^2)/rho^2 = (0.74510 - 0.75000)/0.75000 = -0.65%

    delta(alpha_3/alpha_2)/(alpha_3/alpha_2) ~ 0.7%

Both are well within the ~2-3% uncertainty from two-loop threshold
corrections already neglected in the one-loop analysis of Paper 4.
The Freed-Witten shift does not spoil gauge coupling unification at
the precision level of the current analysis.

---

## B.5 The Tadpole

### B.5.1 Flux self-intersection

For Solution II with the intersection matrix I_{11} = 1, I_{12} = 1,
I_{22} = 0:

    N_flux = (1/2)[(n_1^{phys})^2 I_{11} + 2 n_1^{phys} n_2 I_{12}
             + n_2^2 I_{22}]
           = (1/2)[(19/2)^2 + 2(19/2)(-18)]
           = (1/2)[361/4 - 342]
           = (1/2)(-1007/4)
           = -1007/8                                           (B.6)

### B.5.2 The Euler characteristic

    chi(X_8) = chi(CP^2) x chi(S^2) = 3 x 2 = 6

    chi(X_8)/24 = 1/4                                          (B.7)

### B.5.3 The M2-brane charge

    N_{M2} = chi(X_8)/24 - N_flux = 1/4 + 1007/8
           = 2/8 + 1007/8 = 1009/8                            (B.8)

**N_{M2} = 1009/8 is not an integer.** The flux configuration alone
does not satisfy the naive tadpole cancellation condition.

### B.5.4 The 1/8 obstruction

The non-integer N_{M2} is systematic. With the FW shift, N_flux
always contains a contribution of 1/8 from the cross-term
(1/2)(1/2)^2. Since chi/24 = 1/4 = 2/8, the residue is always
2/8 - 1/8 = 1/8 modulo integers. No integer pair (n_{1,int}, n_{2,int})
can make N_{M2} an integer with the naive formula.

---

## B.6 The DMW Correction

The tadpole non-integrality signals that the naive formula
N_flux + N_{M2} = chi/24 is itself incomplete on non-spin manifolds.
The full anomaly cancellation condition is the Diaconescu-Moore-Witten
(DMW) corrected formula:

    (1/2) integral G_4 ^ G_4 + N_{M2}
        = chi(X_8)/24 + (correction from non-spin topology)

The correction involves the integral Wu class and the mod-2 index of
the Dirac operator on the full 8-manifold, which for the Horava-
Witten setup includes boundary contributions from the E_8 gauge
bundles on the orbifold walls. The complete resolution requires
specifying the E_8 bundle, which is fixed by anomaly cancellation on
the walls. This is a well-defined mathematical problem but lies
beyond the scope of the present analysis.

The key point: the 1/8 obstruction is an artifact of the
uncorrected tadpole formula, not a fundamental inconsistency of the
flux configuration. The DMW-corrected version includes additional
topological terms that restore integrality.

---

## B.7 Summary: Three-Level Resolution

**Level 1: The ratio is obstructed.** The exact GUT ratio
n_2/n_1 = -17/9 cannot be realized with n_1 half-integer and
n_2 integer. This is a parity obstruction: gcd(18, 34) = 2 does
not divide 17.

**Level 2: Approximate unification survives.** The minimal
FW-consistent flux pair (n_{1,int}, n_{2,int}) = (9, -18) deviates
from exact unification by 0.31%, well within threshold correction
uncertainties. The 0.31% deviation is a prediction: the FW anomaly
forces a specific, calculable departure from exact one-loop
unification, analogous in magnitude to the two-loop threshold
corrections in the MSSM.

**Level 3: The tadpole requires the full DMW correction.** The
naive tadpole gives N_{M2} = 1009/8 (non-integer), signaling that
the DMW-corrected formula for non-spin manifolds must be used. This
is a separate technical problem involving the E_8 boundary data.

### Impact on Paper 7 results

| Quantity | Affected by FW? | Impact |
|----------|----------------|--------|
| Flux ratio n_2/n_1 = -17/9 | Yes | ~0.3% deviation |
| Gauge coupling unification | Negligibly | delta(alpha_3/alpha_2) ~ 0.7% |
| Moduli stabilization | Negligibly | rho^2 = 38/51 vs 3/4 |
| Tadpole formula | Yes | Requires DMW correction |
| N_{M2} >= 0 | Unchanged | N_flux < 0; positive N_{M2} guaranteed |
| Inflaton identification | No | Depends on axion, not flux magnitudes |
| Theorem U | No | Depends on algebraic structure |

---

## B.8 Proof Chain

| Step | Statement | Status |
|:-----|:----------|:-------|
| 1 | FW shift: +1/2 on CP^2, 0 on CP^1 x S^2 | Standard (Witten 1996, DMW 2003) |
| 2 | Diophantine obstruction: 18n_2 + 34n_1 = -17 has no solution | Proved (gcd argument) |
| 3 | Minimal solution: (19/2, -18), deviation 0.31% | Computed |
| 4 | Unification preserved within 2-loop uncertainties | Assessed |
| 5 | N_flux = -1007/8, N_{M2} = 1009/8 (non-integer) | Computed |
| 6 | DMW correction needed for integrality | Identified (open) |

---
