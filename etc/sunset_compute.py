#!/usr/bin/env python3
"""
Compute two-loop sunset sums W_{S²}(-j) and W_{CP²}(-j)
using binomial factorization through single spectral zeta values.

Also verify single spectral zeta values Z_{S²}(-j) and Z_{CP²}(-j)
via polynomial expansion + Riemann zeta regularization.
"""

from fractions import Fraction
from math import comb

# ─────────────────────────────────────────────────
# Riemann zeta at negative integers: ζ(-n) = -B_{n+1}/(n+1)
# where B_k are Bernoulli numbers
# ─────────────────────────────────────────────────

# Bernoulli numbers B_0 through B_20 (B_odd>1 = 0)
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
    """ζ(-n) for n >= 0 integer. Uses ζ(-n) = (-1)^n B_{n+1}/(n+1)."""
    if n == 0:
        return Fraction(-1, 2)
    return ((-1)**n) * BERN[n + 1] / Fraction(n + 1)


# ─────────────────────────────────────────────────
# Verify known values
# ─────────────────────────────────────────────────
print("=" * 60)
print("Riemann zeta at negative integers")
print("=" * 60)
for n in range(10):
    print(f"  ζ(-{n}) = {riemann_zeta_neg(n)}")

# ─────────────────────────────────────────────────
# Z_{S²}(-j) via polynomial expansion
#
# Z_{S²}(-j) = Σ_{l=1}^∞ (2l+1) [l(l+1)]^j
#
# Let x = l. Then l(l+1) = l² + l.
# Expand [l² + l]^j by multinomial, then each term is l^k.
# Σ_{l=1}^∞ (2l+1) l^k = 2 ζ(-k-1) + ζ(-k)
# ─────────────────────────────────────────────────

def poly_power(coeffs, n):
    """Raise polynomial (given as list of coefficients, index = degree) to power n."""
    if n == 0:
        return [Fraction(1)]
    result = coeffs[:]
    for _ in range(n - 1):
        result = poly_mul(result, coeffs)
    return result

def poly_mul(a, b):
    """Multiply two polynomials."""
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result

def Z_S2_neg(j):
    """
    Z_{S²}(-j) = Σ_{l=1}^∞ (2l+1) [l(l+1)]^j  (regularized)

    [l(l+1)]^j = [l² + l]^j = Σ_k c_k l^k  (polynomial in l of degree 2j)

    Then Z_{S²}(-j) = Σ_k c_k [2 ζ(-(k+1)) + ζ(-k)]
    """
    if j == 0:
        # (2l+1) summed: 2ζ(-1) + ζ(0) = 2(-1/12) + (-1/2) = -1/6 - 1/2 = -2/3
        return 2 * riemann_zeta_neg(1) + riemann_zeta_neg(0)

    # Polynomial [l² + l]^j
    base = [Fraction(0), Fraction(1), Fraction(1)]  # 0 + l + l²
    p = poly_power(base, j)

    # Multiply by (2l + 1): coefficients of (2l+1) * p(l)
    # (2l+1)*p = 2*l*p + p
    # l*p shifts coefficients up by 1
    lp = [Fraction(0)] + p  # l * p(l)
    # 2*l*p + p
    result_poly = [Fraction(0)] * max(len(lp), len(p))
    for i in range(len(p)):
        result_poly[i] += p[i]
    for i in range(len(lp)):
        result_poly[i] += 2 * lp[i]

    # Now sum: Σ_{l=1}^∞ result_poly[k] * l^k = Σ_k result_poly[k] * ζ(-k)
    total = Fraction(0)
    for k, ck in enumerate(result_poly):
        if ck != 0:
            total += ck * riemann_zeta_neg(k)
    return total


def Z_CP2_neg(j):
    """
    Z_{CP²}(-j) = Σ_{k=1}^∞ (k+1)³ [k(k+2)]^j  (regularized)

    Substitute m = k+1 (m ≥ 2):
    = Σ_{m=2}^∞ m³ [(m-1)(m+1)]^j = Σ_{m=2}^∞ m³ [m²-1]^j

    Expand [m²-1]^j = Σ_r C(j,r) (-1)^{j-r} m^{2r}

    Then m³ [m²-1]^j = Σ_r C(j,r) (-1)^{j-r} m^{2r+3}

    Sum from m=1 to ∞ (regularized) minus m=1 term.

    m=1 term of m³[m²-1]^j = 1³ × [1-1]^j = 0 for j ≥ 1.
    For j=0: m³ × 1 at m=1 gives 1, so we subtract 1.

    Regularized: Σ_{m=1}^∞ m^{2r+3} = ζ(-(2r+3))
    """
    # [m² - 1]^j expanded
    # base polynomial in m: [-1, 0, 1] = -1 + 0*m + 1*m²
    if j == 0:
        # Σ_{m=2}^∞ m³ = ζ(-3) - 1 = 1/120 - 1 = -119/120
        return riemann_zeta_neg(3) - Fraction(1)

    # For j >= 1, m=1 term vanishes (since (1²-1)^j = 0), so sum from m=2 = sum from m=1
    # Expand [m²-1]^j using binomial theorem
    total = Fraction(0)
    for r in range(j + 1):
        coeff = Fraction(comb(j, r)) * ((-1) ** (j - r))
        power = 2 * r + 3  # m^{2r+3}
        total += coeff * riemann_zeta_neg(power)
    return total


# ─────────────────────────────────────────────────
# Compute and display single spectral zeta values
# ─────────────────────────────────────────────────

print("\n" + "=" * 60)
print("Z_{S²}(-j) values")
print("=" * 60)
Z_S2_vals = {}
for j in range(8):
    val = Z_S2_neg(j)
    Z_S2_vals[j] = val
    print(f"  Z_{{S²}}(-{j}) = {val}  ({float(val):.10f})")

print("\n" + "=" * 60)
print("Z_{CP²}(-j) values")
print("=" * 60)
Z_CP2_vals = {}
for j in range(8):
    val = Z_CP2_neg(j)
    Z_CP2_vals[j] = val
    print(f"  Z_{{CP²}}(-{j}) = {val}  ({float(val):.10f})")


# ─────────────────────────────────────────────────
# Sunset sums via binomial factorization
#
# W_X(-j) = Σ_{p=0}^{j} C(j,p) Z_X(-p) Z_X(-(j-p))
# ─────────────────────────────────────────────────

def W_sunset(Z_vals, j):
    """Compute W(-j) = Σ_{p=0}^{j} C(j,p) Z(-p) Z(-(j-p))."""
    total = Fraction(0)
    for p in range(j + 1):
        term = Fraction(comb(j, p)) * Z_vals[p] * Z_vals[j - p]
        total += term
    return total


print("\n" + "=" * 60)
print("W_{S²}(-j) sunset sums")
print("=" * 60)
W_S2_vals = {}
for j in range(6):
    val = W_sunset(Z_S2_vals, j)
    W_S2_vals[j] = val
    print(f"  W_{{S²}}(-{j}) = {val}  ({float(val):.10f})")
    # Show breakdown
    terms = []
    for p in range(j + 1):
        t = Fraction(comb(j, p)) * Z_S2_vals[p] * Z_S2_vals[j - p]
        terms.append(f"    C({j},{p}) × Z(-{p}) × Z(-{j-p}) = {comb(j,p)} × ({Z_S2_vals[p]}) × ({Z_S2_vals[j-p]}) = {t}")
    if terms:
        print("\n".join(terms))

print("\n" + "=" * 60)
print("W_{CP²}(-j) sunset sums")
print("=" * 60)
W_CP2_vals = {}
for j in range(6):
    val = W_sunset(Z_CP2_vals, j)
    W_CP2_vals[j] = val
    print(f"  W_{{CP²}}(-{j}) = {val}  ({float(val):.10f})")
    terms = []
    for p in range(j + 1):
        t = Fraction(comb(j, p)) * Z_CP2_vals[p] * Z_CP2_vals[j - p]
        terms.append(f"    C({j},{p}) × Z(-{p}) × Z(-{j-p}) = {comb(j,p)} × ({Z_CP2_vals[p]}) × ({Z_CP2_vals[j-p]}) = {t}")
    if terms:
        print("\n".join(terms))


# ─────────────────────────────────────────────────
# c₂ ratio (leading order)
# ─────────────────────────────────────────────────
print("\n" + "=" * 60)
print("Two-loop coefficient ratio (leading order, figure-eight = sunset at j=0)")
print("=" * 60)

# At leading order: c₂ ∝ G_eff² × [Z(0)]²
# The spectral ratio:
R_zeta = (Z_S2_vals[0] / Z_CP2_vals[0]) ** 2
print(f"  [Z_{{S²}}(0) / Z_{{CP²}}(0)]² = ({Z_S2_vals[0]}) / ({Z_CP2_vals[0]})]² = {R_zeta}  ({float(R_zeta):.10f})")
print(f"  = W_{{S²}}(0) / W_{{CP²}}(0) = {W_S2_vals[0]} / {W_CP2_vals[0]} = {W_S2_vals[0] / W_CP2_vals[0]}")

# Verify: 4/9 / (14161/14400) = (4 × 14400)/(9 × 14161)
check = Fraction(4, 9) / Fraction(14161, 14400)
print(f"  Cross-check: (4/9)/(14161/14400) = {check} = {float(check):.10f}")

print("\n" + "=" * 60)
print("Summary table")
print("=" * 60)
print(f"{'j':>3} | {'Z_{S²}(-j)':>20} | {'Z_{CP²}(-j)':>20} | {'W_{S²}(-j)':>20} | {'W_{CP²}(-j)':>20}")
print("-" * 95)
for j in range(6):
    print(f"{j:>3} | {str(Z_S2_vals[j]):>20} | {str(Z_CP2_vals[j]):>20} | {str(W_S2_vals[j]):>20} | {str(W_CP2_vals[j]):>20}")
