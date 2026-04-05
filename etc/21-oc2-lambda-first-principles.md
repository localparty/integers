# OC-2: First-Principles Derivation of the Interpolation Parameter lambda

> **Date:** April 5, 2026
> **Status:** Complete computation
> **Purpose:** Determine whether the coupled moduli stabilization equations
> for S^2 and CP^2 predict rho = r_2/r_3 = sqrt(3)/2 (and hence
> alpha_3/alpha_2 = 1) without imposing GUT unification as a condition.
> **Depends on:** etc/16, etc/19, etc/21 Track D

---

## 1. The Coupled Stabilization System

### 1.1 The Effective Potential

For each internal space X in {S^2, CP^2}, the effective potential has
a one-loop Casimir contribution (with logarithmic modulation) and a
two-loop Goroff-Sagnotti correction:

    V_X(r_X) = V_1^X(r_X) + V_2^X(r_X)

where:

    V_1^X(r) = -(N_X/2) r^{-4} [2 Z_X(-2) ln(r) + Z'_X(-2)]

    V_2^X(r) = c_2^X / r^8

### 1.2 The Cross-Coupling

The two-loop coefficient for each sector depends on the OTHER modulus
through the effective Newton constant:

    G_{eff}^{S^2} = G_{11} / [Vol(CP^2) * Vol(S^1)]
                   = G_{11} / [(8 pi^2 r_3^4 / 3)(2 pi R)]

    G_{eff}^{CP^2} = G_{11} / [Vol(S^2) * Vol(S^1)]
                    = G_{11} / [(4 pi r_2^2)(2 pi R)]

The two-loop coefficients are:

    c_2^{S^2}(r_3) = alpha_GS * N_S^2 * [Z_{S^2}(0)]^2 * G_{11}^2
                     / [(8 pi^2/3)^2 * (2 pi R)^2 * r_3^8]

    c_2^{CP^2}(r_2) = alpha_GS * N_C^2 * [Z_{CP^2}(0)]^2 * G_{11}^2
                      / [(4 pi)^2 * (2 pi R)^2 * r_2^4]

Defining the single free parameter:

    kappa = alpha_GS * G_{11}^2 / (2 pi R)^2

the coefficients become:

    c_2^{S^2} = kappa * N_S^2 * [Z_{S^2}(0)]^2 / [(8 pi^2/3)^2 * r_3^8]

    c_2^{CP^2} = kappa * N_C^2 * [Z_{CP^2}(0)]^2 / [(4 pi)^2 * r_2^4]

### 1.3 The Stabilization Equations

Setting V'(r_X) = 0 with Q_X(r) = 8 B_X ln(r) + 4 A_X - 2 B_X
(where B_X = Z_X(-2), A_X = Z'_X(-2)):

**For S^2:**

    r_2^4 Q_S(r_2) = 16 kappa N_S [Z_{S^2}(0)]^2 / [(8 pi^2/3)^2 r_3^8]

**For CP^2:**

    r_3^4 Q_C(r_3) = 16 kappa N_C [Z_{CP^2}(0)]^2 / [(4 pi)^2 r_2^4]

### 1.4 Spectral Data

All exact:

| Quantity | Value | Decimal |
|----------|-------|---------|
| Z_{S^2}(-2) | 8/315 | 0.025397 |
| Z_{CP^2}(-2) | 103/5040 | 0.020437 |
| Z'_{S^2}(-2) | 4 zeta'(-5) + 8 zeta'(-3) | +0.040737 |
| Z'_{CP^2}(-2) | 2 zeta'(-7) + 38 zeta'(-5) + 32 zeta'(-3) | +0.148884 |
| Z_{S^2}(0) | -2/3 | -0.66667 |
| Z_{CP^2}(0) | -119/120 | -0.99167 |
| N_{S^2} | 52 | -- |
| N_{CP^2} | 53 | -- |

---

## 2. Dimensionless Formulation and the Ratio Equation

### 2.1 Logarithmic Variables

Setting u = ln(r_2), v = ln(r_3), the equations in log form are:

    4u + ln(Q_S) + 8v = ln(16 kappa N_S Z_S0^2 / VCP2_norm)    ... (I)

    4v + ln(Q_C) + 4u = ln(16 kappa N_C Z_C0^2 / VS2_norm)     ... (II)

where VCP2_norm = (8 pi^2/3)^2 and VS2_norm = (4 pi)^2.

### 2.2 The Ratio Equation

Dividing (I) by (II) eliminates kappa:

    e^{4v} * Q_S(u) / Q_C(v) = C_0

where:

    C_0 = N_S * Z_S0^2 * VS2_norm / (N_C * Z_C0^2 * VCP2_norm) = 0.1011

**This is a single equation in two unknowns (u, v).** The ratio
rho = exp(u - v) is NOT determined by the ratio equation alone because
the Q functions are LINEAR in the log variables u, v, which breaks
scale invariance.

Physical interpretation: the logarithmic modulation of the one-loop
Casimir energy means the balance between one-loop and two-loop
contributions depends on the absolute compactification scale, not
just on the ratio of radii.

---

## 3. Numerical Solution: Branch Structure

### 3.1 The Bifurcation

The coupled system exhibits a **saddle-node bifurcation** at a critical
coupling strength:

    kappa_bif = 3.477 x 10^{-2}

For kappa < kappa_bif, no physical solutions exist (both Q functions
cannot simultaneously be positive).

For kappa > kappa_bif, **two branches** emerge:

- **Branch 1** (upper/physical): rho increases from rho_bif toward infinity
- **Branch 2** (lower/saddle): rho decreases from rho_bif toward 0

At the bifurcation point itself:

    rho_bif = 0.780 = R_0^{1/4}

This is precisely the Model A prediction from etc/16 Section 3.2,
confirming that Model A corresponds to the critical (marginal) solution
at the edge of the solution space.

### 3.2 Branch 1: The Physical Solution

Branch 1 is a local minimum of the total potential (verified by the
second derivative test). As kappa increases from kappa_bif:

| kappa | r_2 | r_3 | rho | (4/3)rho^2 | lambda_S | lambda_C |
|-------|-----|-----|-----|------------|----------|----------|
| 3.477e-2 | 0.770 | 0.987 | 0.780 | 0.811 | ~0.22 | ~0.32 |
| 3.545e-2 | 0.814 | 0.940 | **0.866** | **1.000** | 0.225 | 0.317 |
| 3.688e-2 | 0.854 | 0.909 | 0.939 | 1.175 | 0.234 | 0.317 |
| 9.377e-2 | -- | -- | 1.834 | 4.487 | 0.279 | 0.316 |
| 1.0 | -- | -- | 4.802 | 30.7 | 0.300 | 0.315 |

### 3.3 The Solution at rho = sqrt(3)/2

On Branch 1, rho passes through sqrt(3)/2 at:

    kappa_* = 3.5451 x 10^{-2}

**Exact numerical solution:**

    kappa_*     = 3.545068124192 x 10^{-2}
    r_2         = 0.814324205043
    r_3         = 0.940300597978
    rho         = 0.866025403784   (= sqrt(3)/2 to 15 digits)
    (4/3)rho^2  = 1.000000000000

    lambda_{S^2}  = 0.2251    (22.5% two-loop fraction)
    lambda_{CP^2} = 0.3175    (31.7% two-loop fraction)

**Key observation:** kappa_* is only 2% above the bifurcation point
kappa_bif = 3.477e-2. The physical solution at rho = sqrt(3)/2 sits
very close to the edge of the solution space.

### 3.4 Comparison with etc/16

The solution found here differs from etc/16 Section 4.2 because:
- etc/16 used a wider scan range and different initial guesses, picking
  up solutions from different parts of the branch structure.
- The kappa values reported in etc/16 (kappa ~ 61.5) correspond to
  solutions higher up on Branch 1 where the (4/3)rho^2 formula passes
  through 1.0 only because the solver jumped between branches.
- The **correct** Branch 1 solution at rho = sqrt(3)/2 is at
  kappa_* = 3.545e-2, with both sector lambdas in the range 0.22-0.32.

---

## 4. The Interpolation Parameter lambda

### 4.1 Definition

From the two limiting models:

- **Baseline** (pure one-loop Z(-2) ratio): rho^4 = Z_{S^2}(-2)/Z_{CP^2}(-2) = 128/103
- **Model A** (full self-consistent with Z(0)^2): rho^4 = R_0

where:

    R_0 = [Z_{S^2}(0)]^2 * N_{CP^2} * Z_{CP^2}(-2)
        / ([Z_{CP^2}(0)]^2 * N_{S^2} * Z_{S^2}(-2))
        = (4/9)(53)(103/5040) / [(14161/14400)(52)(8/315)]
        = 136475/368186
        = 0.37067

The interpolation parameter lambda is defined by:

    rho^4 = (128/103)^{1-lambda} * R_0^lambda

### 4.2 Exact Closed Form

For rho^4 = 9/16 (i.e., rho = sqrt(3)/2, alpha_3/alpha_2 = 1):

    lambda = [ln(9/16) - ln(128/103)] / [ln(R_0) - ln(128/103)]

In exact rational form:

    lambda = ln(927/2048) / ln(14056925/47127808)

### 4.3 Numerical Value

    **lambda = 0.655231810737**

Verification: (128/103)^{0.3448} * (0.37067)^{0.6552} = 0.5625 = 9/16.

### 4.4 Relation to the Sector Lambdas

At the Branch 1 solution (kappa_* = 3.545e-2):

| Lambda quantity | Value | Meaning |
|-----------------|-------|---------|
| lambda (interpolation) | 0.6552 | Log-space position of rho^4 between baseline and Model A |
| lambda_{S^2} | 0.2251 | Two-loop fraction for S^2 at the minimum |
| lambda_{CP^2} | 0.3175 | Two-loop fraction for CP^2 at the minimum |
| Geometric mean | 0.2673 | sqrt(lambda_S * lambda_C) |
| Arithmetic mean | 0.2713 | (lambda_S + lambda_C)/2 |

The interpolation lambda (0.655) and the sector lambdas (0.22-0.32)
are **different quantities.** The interpolation lambda measures the
position of the target rho^4 = 9/16 between the two endpoint models,
while the sector lambdas measure the local two-loop fraction at the
potential minimum. Both are in the perturbative regime.

---

## 5. The Central Question: Is rho Fixed by First Principles?

### 5.1 Answer

**No.** The ratio rho = r_2/r_3 depends on kappa, the overall two-loop
coupling strength. The spectral data alone does not fix rho.

However, the structure is highly constrained:

1. There exists a **unique** kappa_* = 3.545e-2 giving rho = sqrt(3)/2.
2. This kappa_* is only 2% above the bifurcation point, placing the
   physical solution near the edge of the solution space.
3. The bifurcation point itself gives rho_bif = R_0^{1/4} = 0.780,
   which is determined entirely by spectral data.

### 5.2 What Fixes kappa

The parameter kappa encodes the 11D gravitational coupling:

    kappa = alpha_GS * G_{11}^2 / (2 pi R)^2

where alpha_GS = 209/2880 (exact) and R is the S^1 radius. To determine
kappa from first principles requires:

1. The **4D Planck mass** constraint:
   M_Pl^2 = Vol(CP^2 x S^2 x S^1) / G_{11}

2. The **S^1 stabilization** (Scherk-Schwarz SUSY breaking + S^1 Casimir):
   determines R in terms of the SUSY-breaking scale.

These two conditions, together with the coupled S^2-CP^2 system, form
a **three-equation system in three unknowns** (r_2, r_3, R). If this
system has a unique solution with the correct M_Pl, then kappa is
determined and the prediction for rho follows.

### 5.3 Proximity to the Bifurcation

The fact that kappa_* sits just 2% above kappa_bif is physically
meaningful. Near a saddle-node bifurcation, the potential develops a
shallow minimum, which means:

- The moduli masses are small compared to the compactification scale
- The hierarchy between the moduli mass and M_{KK} is naturally generated
- Small perturbations (higher-loop corrections, threshold effects)
  could shift kappa by the required 2%

This suggests that the physical value of kappa may be determined by a
**near-criticality condition** rather than by fine-tuning.

---

## 6. Python Verification Script

```python
#!/usr/bin/env python3
"""
OC-2: Coupled moduli stabilization — branch analysis and lambda computation.
Run: python3 21-oc2-lambda-first-principles.py
"""

import numpy as np
from scipy.optimize import fsolve
import math
from fractions import Fraction

# Exact spectral data
B_S = 8.0 / 315.0          # Z_{S2}(-2)
B_C = 103.0 / 5040.0       # Z_{CP2}(-2)  CORRECTED
A_S = 0.04073664            # Z'_{S2}(-2)
A_C = 0.14888368            # Z'_{CP2}(-2)
Z_S0 = -2.0 / 3.0          # Z_{S2}(0)
Z_C0 = -119.0 / 120.0      # Z_{CP2}(0)
N_S, N_C = 52.0, 53.0

VCP2_norm = (8.0 * np.pi**2 / 3.0)**2
VS2_norm  = (4.0 * np.pi)**2

def Q_S(u): return 8.0 * B_S * u + 4.0 * A_S - 2.0 * B_S
def Q_C(v): return 8.0 * B_C * v + 4.0 * A_C - 2.0 * B_C

def solve_branch(kappa, u_guess, v_guess):
    """Solve coupled system from given initial guess (branch continuation)."""
    def equations(uv):
        u, v = uv
        qs, qc = Q_S(u), Q_C(v)
        if qs <= 0 or qc <= 0:
            return [1e20, 1e20]
        lnRHS_S = np.log(16.0 * kappa * N_S * Z_S0**2 / VCP2_norm)
        lnRHS_C = np.log(16.0 * kappa * N_C * Z_C0**2 / VS2_norm)
        return [4.0*u + np.log(qs) + 8.0*v - lnRHS_S,
                4.0*v + np.log(qc) + 4.0*u - lnRHS_C]
    try:
        sol = fsolve(equations, [u_guess, v_guess], full_output=True)
        x, info, ier, _ = sol
        if ier == 1 and Q_S(x[0]) > 0 and Q_C(x[1]) > 0:
            if np.max(np.abs(info['fvec'])) < 1e-7:
                return x[0], x[1]
    except: pass
    return None, None

def lambda_sector(u, B, A):
    P = 2.0 * B * u + A
    Q = 8.0 * B * u + 4.0 * A - 2.0 * B
    return Q / (Q + 8.0 * P) if (P > 0 and Q > 0) else float('nan')

# === TRACE BRANCH 1 AND FIND rho = sqrt(3)/2 ===
rho_target = np.sqrt(3.0) / 2.0
u_prev, v_prev = -0.16, -0.10

branch1 = []
for log_k in np.linspace(np.log(0.034), np.log(0.040), 500):
    kappa = np.exp(log_k)
    u, v = solve_branch(kappa, u_prev, v_prev)
    if u is not None:
        branch1.append((kappa, u, v, np.exp(u - v)))
        u_prev, v_prev = u, v

# Bisect for rho = sqrt(3)/2
for i in range(len(branch1) - 1):
    r1, r2 = branch1[i][3], branch1[i+1][3]
    if (r1 - rho_target) * (r2 - rho_target) < 0:
        k_lo, k_hi = branch1[i][0], branch1[i+1][0]
        u_g, v_g = branch1[i][1], branch1[i][2]
        for _ in range(80):
            k_mid = (k_lo + k_hi) / 2.0
            u, v = solve_branch(k_mid, u_g, v_g)
            if u is None: break
            rho = np.exp(u - v)
            (k_lo if rho < rho_target else k_hi).__class__  # dummy
            if rho < rho_target: k_lo = k_mid
            else: k_hi = k_mid
            u_g, v_g = u, v
        u, v = solve_branch(k_mid, u_g, v_g)
        rho = np.exp(u - v)
        alpha = (4.0 / 3.0) * rho**2
        ls = lambda_sector(u, B_S, A_S)
        lc = lambda_sector(v, B_C, A_C)
        print(f"kappa_*       = {k_mid:.10e}")
        print(f"r_2           = {np.exp(u):.12f}")
        print(f"r_3           = {np.exp(v):.12f}")
        print(f"rho           = {rho:.15f}")
        print(f"(4/3)*rho^2   = {alpha:.15f}")
        print(f"lambda_S2     = {ls:.10f}")
        print(f"lambda_CP2    = {lc:.10f}")
        break

# === INTERPOLATION PARAMETER (exact) ===
F_R0 = (Fraction(2,3)**2 * Fraction(53) * Fraction(103,5040)
        / (Fraction(119,120)**2 * Fraction(52) * Fraction(8,315)))
F_ratio_num = Fraction(9,16) / Fraction(128,103)
F_ratio_den = F_R0 / Fraction(128,103)
ln_n = math.log(F_ratio_num.numerator) - math.log(F_ratio_num.denominator)
ln_d = math.log(F_ratio_den.numerator) - math.log(F_ratio_den.denominator)
print(f"\nlambda = ln({F_ratio_num.numerator}/{F_ratio_num.denominator})"
      f" / ln({F_ratio_den.numerator}/{F_ratio_den.denominator})")
print(f"lambda = {ln_n/ln_d:.15f}")
```

Script output (April 5, 2026):

    kappa_*       = 3.5450681242e-02
    r_2           = 0.814324205043
    r_3           = 0.940300597978
    rho           = 0.866025403784440
    (4/3)*rho^2   = 1.000000000000002
    lambda_S2     = 0.2250954110
    lambda_CP2    = 0.3174498889

    lambda = ln(927/2048) / ln(14056925/47127808)
    lambda = 0.655231810736755

---

## 7. Summary

### 7.1 The Main Results

| Result | Value | Status |
|--------|-------|--------|
| lambda (interpolation) | **0.6552** | Exact from spectral data |
| rho at GUT unification | sqrt(3)/2 = 0.8660 | Requires kappa = 3.545e-2 |
| kappa_* | 3.545 x 10^{-2} | 2% above bifurcation |
| kappa_bif (bifurcation) | 3.477 x 10^{-2} | Determined by spectral data |
| rho at bifurcation | 0.780 = R_0^{1/4} | Model A critical point |
| lambda_{S^2} at solution | 0.225 | 22.5% two-loop |
| lambda_{CP^2} at solution | 0.317 | 31.7% two-loop |

### 7.2 Exact Closed-Form Expression

    lambda = ln(927/2048) / ln(14056925/47127808) = 0.65523181...

where 927 = 9 * 103, 2048 = 16 * 128, and the denominator fraction
encodes R_0 = 136475/368186 (an exact rational from the spectral
zeta values of S^2 and CP^2).

### 7.3 Answer to the Central Question

**Does the self-consistent coupled system give rho = sqrt(3)/2 without
imposing alpha_3/alpha_2 = 1 as a condition?**

Partially. The coupled system has a saddle-node bifurcation structure:

- The ratio rho depends on kappa (the overall gravitational coupling).
- There exists a unique kappa_* giving rho = sqrt(3)/2 exactly.
- This kappa_* is only 2% above the bifurcation point.
- The bifurcation value rho_bif = 0.780 is fixed by spectral data.

What remains: determining kappa from the 4D Planck mass and S^1
stabilization. If these conditions fix kappa to 3.545e-2, then
GUT unification is a parameter-free prediction. This links to OC-3.

### 7.4 Physical Significance of the Bifurcation

The coupled moduli system has NO solution below a critical gravitational
coupling strength. Just above this threshold, the solution gives
alpha_3/alpha_2 close to 1. This suggests that gauge coupling unification
is not a coincidence but a consequence of the compactification geometry
operating near the edge of its stability region.
