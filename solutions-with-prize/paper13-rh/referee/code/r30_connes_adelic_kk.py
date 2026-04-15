"""
Round 30: Computational verification of adelic spectral zetas.

Compares:
1. Connes's spectral picture (absorption spectrum on L^2(A_Q/Q*))
2. QG5D adelic KK spectral zeta (product over local spectral zetas)
3. The Riemann zeta function zeta(s)

Key computation: prod_p Z_{Z_p}(s) vs zeta(s)
"""

import numpy as np
from mpmath import mp, mpf, zeta, log, pi, gamma, inf, fsum

mp.dps = 30  # 30 decimal places

def local_spectral_zeta_Zp(s, p, version="laplacian"):
    """
    Spectral zeta of the p-adic Laplacian (Vladimirov operator) on Z_p.

    For the Laplacian (second-order, eigenvalues p^{2k}):
        Z_{Z_p}(s) = (1 - p^{-2s}) / (1 - p^{1-2s})

    For the "Dirac" analogue (first-order, eigenvalues p^k):
        Z_{Z_p}^{Dirac}(s) = (1 - p^{-s}) / (1 - p^{1-s})
    """
    p = mpf(p)
    s = mpf(s)
    if version == "laplacian":
        return (1 - p**(-2*s)) / (1 - p**(1-2*s))
    elif version == "dirac":
        return (1 - p**(-s)) / (1 - p**(1-s))
    else:
        raise ValueError(f"Unknown version: {version}")


def product_local_zetas(s, N_primes=100, version="laplacian"):
    """
    Compute prod_{p <= P_N} Z_{Z_p}(s) for the first N_primes primes.
    """
    s = mpf(s)
    primes = get_primes(N_primes)
    product = mpf(1)
    for p in primes:
        product *= local_spectral_zeta_Zp(s, p, version)
    return product


def get_primes(n):
    """Get first n primes."""
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


def s1_spectral_zeta(s, R=1):
    """
    Spectral zeta of S^1 Laplacian: Z_{S^1}(s) = 2R^{2s} zeta(2s)
    """
    s = mpf(s)
    R = mpf(R)
    return 2 * R**(2*s) * zeta(2*s)


def s1_dirac_zeta(s, R=1):
    """
    Spectral zeta of S^1 Dirac operator: Z_D(s) = 2R^s zeta(s)
    """
    s = mpf(s)
    R = mpf(R)
    return 2 * R**s * zeta(s)


print("=" * 70)
print("ROUND 30: ADELIC KK vs CONNES -- SPECTRAL ZETA COMPARISON")
print("=" * 70)

# =====================================================================
# Test 1: Local spectral zeta at individual primes
# =====================================================================
print("\n--- Test 1: Local spectral zeta Z_{Z_p}(s) at individual primes ---")
print(f"{'p':>5} {'s':>6} {'Z_Lapl':>20} {'Z_Dirac':>20} {'(1-p^-s)^-1':>20}")
print("-" * 75)

for p in [2, 3, 5, 7, 11]:
    for s in [1.5, 2.0, 3.0]:
        z_lapl = local_spectral_zeta_Zp(s, p, "laplacian")
        z_dirac = local_spectral_zeta_Zp(s, p, "dirac")
        euler = 1 / (1 - mpf(p)**(-mpf(s)))
        print(f"{p:>5} {s:>6.1f} {float(z_lapl):>20.10f} {float(z_dirac):>20.10f} {float(euler):>20.10f}")

# =====================================================================
# Test 2: Product of local "Dirac" zetas vs zeta(s)
# =====================================================================
print("\n--- Test 2: Product of local Dirac zetas vs known functions ---")
print("\nIf Z_{Z_p}^{Dirac}(s) = (1-p^{-s})/(1-p^{1-s}), then:")
print("prod_p Z_{Z_p}^{Dirac}(s) = prod_p (1-p^{-s}) / prod_p (1-p^{1-s})")
print("                          = [1/zeta(s)] / [1/zeta(s-1)]")
print("                          = zeta(s-1) / zeta(s)")
print()

N_primes = 200
primes = get_primes(N_primes)
print(f"Using first {N_primes} primes (up to {primes[-1]})")
print()
print(f"{'s':>6} {'prod Z_Dirac':>22} {'zeta(s-1)/zeta(s)':>22} {'zeta(s)':>18} {'Match?':>8}")
print("-" * 80)

for s in [2.5, 3.0, 4.0, 5.0, 6.0]:
    prod_val = product_local_zetas(s, N_primes, "dirac")
    ratio = zeta(mpf(s) - 1) / zeta(mpf(s))
    zeta_val = zeta(mpf(s))
    match = "YES" if abs(prod_val - ratio) / abs(ratio) < 1e-5 else "NO"
    print(f"{s:>6.1f} {float(prod_val):>22.12f} {float(ratio):>22.12f} {float(zeta_val):>18.12f} {match:>8}")

# =====================================================================
# Test 3: Product of local Laplacian zetas vs known functions
# =====================================================================
print("\n--- Test 3: Product of local Laplacian zetas vs known functions ---")
print("\nIf Z_{Z_p}^{Lapl}(s) = (1-p^{-2s})/(1-p^{1-2s}), then:")
print("prod_p Z_{Z_p}^{Lapl}(s) = prod_p (1-p^{-2s}) / prod_p (1-p^{1-2s})")
print("                         = [1/zeta(2s)] / [1/zeta(2s-1)]")
print("                         = zeta(2s-1) / zeta(2s)")
print()

print(f"Using first {N_primes} primes (up to {primes[-1]})")
print()
print(f"{'s':>6} {'prod Z_Lapl':>22} {'zeta(2s-1)/zeta(2s)':>22} {'zeta(2s)':>18} {'Match?':>8}")
print("-" * 80)

for s in [1.5, 2.0, 2.5, 3.0, 4.0]:
    prod_val = product_local_zetas(s, N_primes, "laplacian")
    ratio = zeta(2*mpf(s) - 1) / zeta(2*mpf(s))
    zeta2s = zeta(2*mpf(s))
    match = "YES" if abs(prod_val - ratio) / abs(ratio) < 1e-5 else "NO"
    print(f"{s:>6.1f} {float(prod_val):>22.12f} {float(ratio):>22.12f} {float(zeta2s):>18.12f} {match:>8}")

# =====================================================================
# Test 4: What WOULD give zeta(s) as a product?
# =====================================================================
print("\n--- Test 4: What local factor gives zeta(s) as a product? ---")
print("\nThe Euler product: zeta(s) = prod_p (1 - p^{-s})^{-1}")
print("Each Euler factor (1 - p^{-s})^{-1} is the partition function")
print("of a SINGLE harmonic oscillator with frequency log(p).")
print()
print("The QG5D local zeta Z_{Z_p}(s) = (1-p^{-2s})/(1-p^{1-2s})")
print("is NOT equal to (1-p^{-s})^{-1}.")
print()

print(f"{'p':>5} {'s':>6} {'Euler (1-p^-s)^-1':>22} {'Z_Zp Laplacian':>22} {'Z_Zp Dirac':>22}")
print("-" * 80)
for p in [2, 3, 5, 7]:
    for s in [2.0, 3.0]:
        euler = 1 / (1 - mpf(p)**(-mpf(s)))
        z_lapl = local_spectral_zeta_Zp(s, p, "laplacian")
        z_dirac = local_spectral_zeta_Zp(s, p, "dirac")
        print(f"{p:>5} {s:>6.1f} {float(euler):>22.12f} {float(z_lapl):>22.12f} {float(z_dirac):>22.12f}")

# =====================================================================
# Test 5: The BC partition function vs spectral zetas
# =====================================================================
print("\n--- Test 5: BC partition function vs S^1 spectral zetas ---")
print("\nZ_BC(beta) = zeta(beta)")
print("Z_{S^1}(s) = 2R^{2s} zeta(2s) [Laplacian]")
print("Z_{S^1}^D(s) = 2R^s zeta(s) [Dirac]")
print()
print("Mapping: beta = 2s (Laplacian) or beta = s (Dirac)")
print()

print(f"{'beta':>6} {'zeta(beta)':>18} {'Z_S1(beta/2)/2':>18} {'Z_D(beta)/2':>18}")
print("-" * 65)
for beta in [2.0, 3.0, 4.0, 5.0]:
    z_beta = zeta(mpf(beta))
    z_s1 = s1_spectral_zeta(mpf(beta)/2, R=1) / 2
    z_d = s1_dirac_zeta(mpf(beta), R=1) / 2
    print(f"{beta:>6.1f} {float(z_beta):>18.12f} {float(z_s1):>18.12f} {float(z_d):>18.12f}")

# =====================================================================
# Test 6: The gap -- what the adelic product actually gives
# =====================================================================
print("\n--- Test 6: The adelic product gap ---")
print("\nThe adelic product of Dirac-type local zetas gives zeta(s-1)/zeta(s),")
print("NOT zeta(s). The ratio tells us what multiplicative factor is missing:")
print()
print("  [zeta(s-1)/zeta(s)] * X(s) = zeta(s)")
print("  => X(s) = zeta(s)^2 / zeta(s-1)")
print()
print(f"{'s':>6} {'zeta(s-1)/zeta(s)':>22} {'zeta(s)':>18} {'X(s) needed':>22}")
print("-" * 70)
for s in [2.5, 3.0, 4.0, 5.0]:
    ratio = zeta(mpf(s)-1) / zeta(mpf(s))
    z = zeta(mpf(s))
    X = z**2 / zeta(mpf(s)-1)
    print(f"{s:>6.1f} {float(ratio):>22.12f} {float(z):>18.12f} {float(X):>22.12f}")

# =====================================================================
# Summary
# =====================================================================
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
1. The S^1 Dirac spectral zeta IS related to zeta(s):
   Z_D(s) = 2R^s zeta(s)  [EXACT, Identity 1]

2. The S^1 Laplacian spectral zeta gives zeta(2s):
   Z_{S^1}(s) = 2R^{2s} zeta(2s)  [EXACT, Identity 1]

3. The local p-adic spectral zeta Z_{Z_p}(s) is NOT the Euler factor:
   Z_{Z_p}^{Dirac}(s) = (1-p^{-s})/(1-p^{1-s})  =/=  (1-p^{-s})^{-1}

4. The product of local p-adic zetas gives zeta(s-1)/zeta(s),
   NOT zeta(s):
   prod_p Z_{Z_p}^{Dirac}(s) = zeta(s-1)/zeta(s)

5. The MISSING factor to get zeta(s) is zeta(s)^2/zeta(s-1).
   This factor has NO known geometric origin in the QG5D framework.

6. CONCLUSION: The spectral zeta of the QG5D adelic KK operator
   is NOT equal to zeta(s). The operators are related but fundamentally
   different.
""")
