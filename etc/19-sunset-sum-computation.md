# Two-Loop Sunset Sum Computation

> **Date:** April 5, 2026
> **Purpose:** Compute W_{S²}(-j) and W_{CP²}(-j) numerically using exact
> rational arithmetic. Verify single spectral zeta values independently.
> **Depends on:** 14c-two-loop-vertex-on-curved-spaces.md

---

## 1. Method

The two-loop sunset sum on a compact space X is:

    W_X(s) = Σ (degeneracy factors) × [λ₁ + λ₂]^{-s}

At negative integers s = -j, this diverges and requires zeta regularization.
The binomial theorem gives the exact factorization:

    W_X(-j) = Σ_{p=0}^{j} C(j,p) Z_X(-p) Z_X(-(j-p))

where Z_X(-k) is the single spectral zeta function at s = -k, itself
computed by polynomial expansion into Riemann zeta values ζ(-n).

All arithmetic uses Python `fractions.Fraction` for exact results.

---

## 2. Single Spectral Zeta Values

### 2.1 Riemann Zeta at Negative Integers

    ζ(0)  = -1/2
    ζ(-1) = -1/12
    ζ(-2) = 0
    ζ(-3) = 1/120
    ζ(-5) = -1/252
    ζ(-7) = 1/240
    ζ(-9) = -1/132

(All ζ(-2k) = 0 for k ≥ 1, i.e., trivial zeros.)

### 2.2 Z_{S²}(-j)

    Z_{S²}(-j) = Σ_{l=1}^∞ (2l+1) [l(l+1)]^j    (regularized)

Computed by expanding (2l+1)[l(l+1)]^j as a polynomial in l, then
replacing Σ l^k → ζ(-k).

| j | Z_{S²}(-j) | Decimal |
|---|-----------|---------|
| 0 | -2/3 | -0.6667 |
| 1 | -1/15 | -0.0667 |
| 2 | 8/315 | +0.0254 |
| 3 | -2/105 | -0.0190 |
| 4 | 32/1155 | +0.0277 |
| 5 | -3056/45045 | -0.0678 |

### 2.3 Z_{CP²}(-j)

    Z_{CP²}(-j) = Σ_{k=1}^∞ (k+1)³ [k(k+2)]^j    (regularized)

Substituting m = k+1: = Σ_{m=2}^∞ m³ (m²-1)^j. Since (m²-1)^j vanishes
at m = 1 for j ≥ 1, this equals Σ_{m=1}^∞ m³ (m²-1)^j, which expands
by the binomial theorem into Riemann zeta values.

| j | Z_{CP²}(-j) | Decimal |
|---|------------|---------|
| 0 | -119/120 | -0.9917 |
| 1 | -31/2520 | -0.0123 |
| 2 | 103/5040 | +0.0204 |
| 3 | -149/3696 | -0.0403 |
| 4 | 5179/51480 | +0.1006 |
| 5 | -120503/360360 | -0.3344 |

**Erratum:** The value Z_{CP²}(-2) = 103/5040 corrects 313/5040 stated in
etc/14c. The derivation:

    Z_{CP²}(-2) = ζ(-7) - 2ζ(-5) + ζ(-3)
                = 1/240 + 1/126 + 1/120
                = (21 + 40 + 42)/5040
                = 103/5040

The incorrect value 313/5040 in etc/14c propagated into W_{CP²}(-2) there.
The corrected value is used throughout this document.

---

## 3. Sunset Sums W_{S²}(-j)

Using W_{S²}(-j) = Σ_{p=0}^{j} C(j,p) Z_{S²}(-p) Z_{S²}(-(j-p)):

### j = 0

    W_{S²}(0) = [Z_{S²}(0)]² = (-2/3)² = 4/9

### j = 1

    W_{S²}(-1) = 2 × Z(0) × Z(-1)
               = 2 × (-2/3)(-1/15)
               = 2 × (2/45)
               = **4/45**

### j = 2

    W_{S²}(-2) = Z(0)Z(-2) + 2 Z(-1)² + Z(-2)Z(0)
               = 2(-2/3)(8/315) + 2(1/15)²
               = -32/945 + 2/225
               = -160/4725 + 42/4725
               = **-118/4725**

### j = 3

    W_{S²}(-3) = Z(0)Z(-3) + 3Z(-1)Z(-2) + 3Z(-2)Z(-1) + Z(-3)Z(0)
               = 2(-2/3)(-2/105) + 6(-1/15)(8/315)
               = 8/315 - 48/4725
               = 40/1575 - 16/1575
               = **8/525**

### Summary

| j | W_{S²}(-j) | Decimal |
|---|-----------|---------|
| 0 | 4/9 | +0.4444 |
| 1 | 4/45 | +0.0889 |
| 2 | -118/4725 | -0.0250 |
| 3 | 8/525 | +0.0152 |
| 4 | -8336/363825 | -0.0229 |
| 5 | 19648/315315 | +0.0623 |

---

## 4. Sunset Sums W_{CP²}(-j)

Using W_{CP²}(-j) = Σ_{p=0}^{j} C(j,p) Z_{CP²}(-p) Z_{CP²}(-(j-p)):

### j = 0

    W_{CP²}(0) = (-119/120)² = **14161/14400**

### j = 1

    W_{CP²}(-1) = 2 × (-119/120)(-31/2520)
                = 2 × (3689/302400)
                = 7378/302400 = 3689/151200
                = **527/21600**  (dividing by GCD = 7)

### j = 2 (corrected)

    W_{CP²}(-2) = 2(-119/120)(103/5040) + 2(-31/2520)²
                = 2(-12257/604800) + 2(961/6350400)
                = -24514/604800 + 1922/6350400

    Common denominator 6350400:
                = -257397/6350400 + 1922/6350400
                = -255475/6350400

    Simplify: GCD(255475, 6350400) = 25
                = **-10219/254016**

    Decimal: -0.04023

### j = 3

    W_{CP²}(-3) = 2(-119/120)(-149/3696) + 6(-31/2520)(103/5040)
                = 2 × 17731/443520 + 6 × (-3193/12700800)
                = 35462/443520 - 19158/12700800

    Common denominator: LCM(443520, 12700800)
                = 35462/443520 - 19158/12700800

    Simplify each: 35462/443520 = 17731/221760
                   19158/12700800 = 3193/2116800

    LCM(221760, 2116800) = 2116800
    17731/221760 × (2116800/221760 = 9.55...) -- let me use computer result:

    **W_{CP²}(-3) = 228329/2910600**

    Decimal: +0.07845

### Summary

| j | W_{CP²}(-j) | Decimal |
|---|------------|---------|
| 0 | 14161/14400 | +0.9834 |
| 1 | 527/21600 | +0.0244 |
| 2 | -10219/254016 | -0.0402 |
| 3 | 228329/2910600 | +0.0784 |
| 4 | -116876029/605404800 | -0.1931 |
| 5 | 576072239/908107200 | +0.6344 |

---

## 5. Two-Loop Coefficient Ratio

### 5.1 Leading Order (j = 0)

At leading order, the two-loop coefficient is dominated by the figure-eight
topology, which equals the sunset at j = 0:

    c₂^{S²}  ∝ [Z_{S²}(0)]²  = 4/9
    c₂^{CP²} ∝ [Z_{CP²}(0)]² = 14161/14400

The spectral ratio:

    R_ζ = [Z_{S²}(0)/Z_{CP²}(0)]² = W_{S²}(0)/W_{CP²}(0)

        = (4/9) / (14161/14400) = 57600/127449 = **6400/14161**

        ≈ 0.4519

This is the ratio (80/119)², since Z_{S²}(0)/Z_{CP²}(0) = (-2/3)/(-119/120) = 80/119.

### 5.2 Comparison with etc/14c

The values W_{S²}(-1) = 4/45 and W_{S²}(-2) = -118/4725 agree with etc/14c.

The value W_{CP²}(-1) = 527/21600 agrees with etc/14c.

The value W_{CP²}(-2) = -10219/254016 **differs** from etc/14c (which has
-156053/1270080), because etc/14c used the incorrect Z_{CP²}(-2) = 313/5040
instead of 103/5040. Cross-check: with the wrong value,

    2(-119/120)(313/5040) + 2(31/2520)² = -74494/604800 + 1922/6350400

which gives -780265/6350400 = -156053/1270080 as in etc/14c. With the correct
Z_{CP²}(-2) = 103/5040, we get -10219/254016.

---

## 6. Erratum Summary

**Z_{CP²}(-2):** 313/5040 → 103/5040

The error: in the expansion ζ(-7) - 2ζ(-5) + ζ(-3), the coefficient of
ζ(-5) was apparently applied with the wrong sign or the wrong Bernoulli
number. The correct computation:

    ζ(-7) = 1/240,  ζ(-5) = -1/252,  ζ(-3) = 1/120

    1/240 - 2(-1/252) + 1/120 = 1/240 + 1/126 + 1/120

    LCD = 5040:  21/5040 + 40/5040 + 42/5040 = 103/5040  ✓

This propagates to:
- W_{CP²}(-2): -156053/1270080 → -10219/254016
- All downstream quantities using W_{CP²}(-2) in etc/14c §3.2 onward

---

## Appendix: Python Script

```python
#!/usr/bin/env python3
"""
Compute two-loop sunset sums W_{S²}(-j) and W_{CP²}(-j)
via binomial factorization through single spectral zeta values.
All arithmetic exact using fractions.Fraction.
"""

from fractions import Fraction
from math import comb


def bernoulli_numbers(N):
    """Compute B_0 ... B_N as exact fractions."""
    B = [Fraction(0)] * (N + 1)
    B[0] = Fraction(1)
    for m in range(1, N + 1):
        s = Fraction(0)
        for k in range(m):
            s += Fraction(comb(m + 1, k)) * B[k]
        B[m] = -s / Fraction(m + 1)
    return B

BERN = bernoulli_numbers(30)


def riemann_zeta_neg(n):
    """ζ(-n) for n >= 0 integer."""
    if n == 0:
        return Fraction(-1, 2)
    return ((-1)**n) * BERN[n + 1] / Fraction(n + 1)


def poly_mul(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


def poly_power(coeffs, n):
    if n == 0:
        return [Fraction(1)]
    result = coeffs[:]
    for _ in range(n - 1):
        result = poly_mul(result, coeffs)
    return result


def Z_S2_neg(j):
    """Z_{S²}(-j) = Σ_{l≥1} (2l+1)[l(l+1)]^j  (regularized)."""
    if j == 0:
        return 2 * riemann_zeta_neg(1) + riemann_zeta_neg(0)
    base = [Fraction(0), Fraction(1), Fraction(1)]  # l + l²
    p = poly_power(base, j)
    # Multiply by (2l+1)
    lp = [Fraction(0)] + p
    rp = [Fraction(0)] * max(len(lp), len(p))
    for i in range(len(p)):
        rp[i] += p[i]
    for i in range(len(lp)):
        rp[i] += 2 * lp[i]
    return sum(ck * riemann_zeta_neg(k) for k, ck in enumerate(rp) if ck)


def Z_CP2_neg(j):
    """Z_{CP²}(-j) = Σ_{k≥1} (k+1)³[k(k+2)]^j  (regularized)."""
    if j == 0:
        return riemann_zeta_neg(3) - Fraction(1)
    return sum(
        Fraction(comb(j, r)) * ((-1)**(j - r)) * riemann_zeta_neg(2*r + 3)
        for r in range(j + 1)
    )


def W_sunset(Z_vals, j):
    """W(-j) = Σ_{p=0}^{j} C(j,p) Z(-p) Z(-(j-p))."""
    return sum(
        Fraction(comb(j, p)) * Z_vals[p] * Z_vals[j - p]
        for p in range(j + 1)
    )


if __name__ == "__main__":
    Z_S2 = {j: Z_S2_neg(j) for j in range(8)}
    Z_CP2 = {j: Z_CP2_neg(j) for j in range(8)}
    W_S2 = {j: W_sunset(Z_S2, j) for j in range(6)}
    W_CP2 = {j: W_sunset(Z_CP2, j) for j in range(6)}

    for j in range(6):
        print(f"j={j}: Z_S2={Z_S2[j]}, Z_CP2={Z_CP2[j]}, "
              f"W_S2={W_S2[j]}, W_CP2={W_CP2[j]}")

    R = (Z_S2[0] / Z_CP2[0])**2
    print(f"\nSpectral ratio R_zeta = {R} = {float(R):.10f}")
```

Script verified: all values match the hand calculations in §§3-4 above.
