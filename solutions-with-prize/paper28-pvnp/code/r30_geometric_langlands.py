"""
R30: Geometric Langlands on the Torus T^2 = S^1_e x S^1_beta

Computations:
1. The L-function of E_i: y^2 = x^3 - x (CM by Z[i])
2. a_p values for small primes (traces of Frobenius)
3. Verify Ramanujan bound |a_p| <= 2*sqrt(p)
4. Verify that a_p = 0 for p = 3 mod 4 (inert primes)
5. The Euler product convergence
6. Moduli space dimensions for G = SU(3) x SU(2) x U(1)
7. The Hecke L-function identification via Grossencharacter
"""

import numpy as np
from mpmath import mp, mpf, mpc, zeta, gamma, pi, sqrt, log, exp, fac
from mpmath import power as mppower

mp.dps = 30  # 30 decimal places

print("=" * 70)
print("R30: Geometric Langlands on the Torus T^2")
print("=" * 70)

# ===================================================================
# Part 1: The elliptic curve E_i: y^2 = x^3 - x
# ===================================================================
print("\n## Part 1: The Elliptic Curve E_i: y^2 = x^3 - x")
print("   CM by Z[i], j-invariant = 1728, conductor = 32\n")

# Count points on E: y^2 = x^3 - x over F_p
def count_points_Ei(p):
    """Count |E_i(F_p)| for the curve y^2 = x^3 - x."""
    count = 1  # point at infinity
    for x in range(p):
        rhs = (x**3 - x) % p
        if rhs == 0:
            count += 1  # y = 0
        else:
            # Check if rhs is a quadratic residue mod p
            leg = pow(rhs, (p - 1) // 2, p)
            if leg == 1:
                count += 2  # two solutions y
    return count

def a_p_Ei(p):
    """Compute a_p = p + 1 - |E_i(F_p)| for the CM curve y^2 = x^3 - x."""
    if p == 2:
        return 0  # bad reduction
    return p + 1 - count_points_Ei(p)

# Compute a_p for small primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print("| p   | p mod 4 | |E(F_p)| | a_p  | |a_p|/2sqrt(p) | Ramanujan |")
print("|-----|---------|---------|------|----------------|-----------|")

for p in primes:
    if p == 2:
        print(f"| {p:3d} | {p%4:7d} | {'bad':>7s} | {'bad':>4s} | {'N/A':>14s} | bad red.  |")
        continue
    Np = count_points_Ei(p)
    ap = a_p_Ei(p)
    bound = abs(ap) / (2 * np.sqrt(p))
    ramanujan = "YES" if bound <= 1.0 else "NO"
    print(f"| {p:3d} | {p%4:7d} | {Np:>7d} | {ap:>4d} | {bound:>14.6f} | {ramanujan:>9s} |")

# Verify the CM pattern: a_p = 0 for p = 3 mod 4
print("\n## Verification: a_p = 0 for primes p = 3 mod 4")
inert_primes = [p for p in primes if p % 4 == 3 and p > 2]
all_zero = all(a_p_Ei(p) == 0 for p in inert_primes)
print(f"Primes p = 3 mod 4: {inert_primes}")
print(f"All a_p = 0? {all_zero}")

# For split primes p = 1 mod 4, a_p = 2*Re(pi) where p = pi*bar(pi) in Z[i]
print("\n## Split primes p = 1 mod 4: a_p from Gaussian integer factorization")
split_primes = [p for p in primes if p % 4 == 1]

print("| p   | a_p  | p = a^2 + b^2        | a_p = +-2a (choose a odd) |")
print("|-----|------|----------------------|---------------------------|")
for p in split_primes:
    ap = a_p_Ei(p)
    # Find a, b with p = a^2 + b^2
    for a in range(1, int(np.sqrt(p)) + 1):
        b2 = p - a * a
        b = int(np.sqrt(b2) + 0.5)
        if b * b == b2 and b >= 0:
            print(f"| {p:3d} | {ap:>4d} | {p} = {a}^2 + {b}^2{' '*(14-len(f'{p} = {a}^2 + {b}^2'))} | a_p = {'+' if ap > 0 else ''}{ap}, 2a = {2*a}, 2b = {2*b} |")
            break


# ===================================================================
# Part 2: L-function of E_i -- partial Euler product
# ===================================================================
print("\n\n## Part 2: Partial Euler Product of L(E_i, s)")

def euler_product_L_Ei(s, max_p=1000):
    """
    Compute partial Euler product of L(E_i, s).
    L(E_i, s) = prod_p L_p(s)
    where:
      p = 2 (conductor): L_2 = (1 + 2^{-s})^{-1} (actually depends on model)
      p = 1 mod 4: L_p = (1 - a_p*p^{-s} + p^{1-2s})^{-1}
      p = 3 mod 4: L_p = (1 + p^{1-2s})^{-1} (since a_p = 0)
    """
    s = mpc(s)
    product = mpc(1)
    p = 2
    while p <= max_p:
        if p == 2:
            # Bad reduction -- skip or use conductor-specific factor
            p += 1
            continue

        # Check primality
        is_prime = True
        for d in range(2, int(float(p)**0.5) + 1):
            if p % d == 0:
                is_prime = False
                break

        if is_prime:
            ap = a_p_Ei(p)
            ps = mppower(p, -s)
            local = 1 / (1 - mpc(ap) * ps + mppower(p, 1 - 2*s))
            product *= local

        p += 1

    return product

# Evaluate at several points
print("\n| s        | L(E_i, s) via Euler (P<=200) | L(E_i, s) via Euler (P<=1000) |")
print("|----------|------------------------------|-------------------------------|")

for s_val in [2.0, 3.0, 4.0, 1.5]:
    L200 = euler_product_L_Ei(s_val, max_p=200)
    L1000 = euler_product_L_Ei(s_val, max_p=1000)
    print(f"| {s_val:<8.1f} | {float(L200.real):>28.15f} | {float(L1000.real):>29.15f} |")


# ===================================================================
# Part 3: Moduli space dimensions
# ===================================================================
print("\n\n## Part 3: Moduli Space Dimensions for G-bundles on T^2")

groups = [
    ("U(1)", 1, 1, "U(1)"),
    ("SU(2)", 2, 1, "SO(3) = PGL(2)"),
    ("SU(3)", 3, 2, "PGL(3)"),
    ("SU(3)xSU(2)xU(1)", None, 4, "PGL(3)xPGL(2)xGL(1)"),
]

print("\n| G                    | rank(G) | dim_C Bun^ss_G(E) | dim_C M_flat(G,E) | G^L               |")
print("|----------------------|---------|-------------------|-------------------|-------------------|")
for name, n, rank, dual in groups:
    dim_flat = 2 * rank  # for semisimple: 2*rank(G)
    dim_bun = rank  # for semistable bundles on elliptic curve
    print(f"| {name:<20s} | {rank:>7d} | {dim_bun:>17d} | {dim_flat:>17d} | {dual:<17s} |")


# ===================================================================
# Part 4: The Epstein zeta check (cross-ref R29)
# ===================================================================
print("\n\n## Part 4: Cross-check -- Epstein zeta E_2(s) = 4*zeta(s)*L(s, chi_{-4})")

def chi_neg4(n):
    """The Dirichlet character chi_{-4}: the non-principal char mod 4."""
    n = n % 4
    if n == 1: return 1
    if n == 3: return -1
    return 0

def L_chi_neg4(s, terms=10000):
    """L(s, chi_{-4}) = sum_{n=1}^{infty} chi_{-4}(n) * n^{-s}."""
    s = mpc(s)
    result = mpc(0)
    for n in range(1, terms + 1):
        c = chi_neg4(n)
        if c != 0:
            result += c * mppower(n, -s)
    return result

def epstein_2_direct(s, N=200):
    """E_2(s; I_2) = sum'_{(m,n)} (m^2+n^2)^{-s}, direct computation."""
    s = mpc(s)
    result = mpc(0)
    for m in range(-N, N+1):
        for n in range(-N, N+1):
            if m == 0 and n == 0:
                continue
            result += mppower(m*m + n*n, -s)
    return result

print("\n| s   | E_2 direct (N=100) | 4*zeta*L         | Rel. error  |")
print("|-----|---------------------|------------------|-------------|")
for s_val in [mpf(2), mpf(3), mpf(4)]:
    e2_direct = epstein_2_direct(s_val, N=100)
    e2_factor = 4 * zeta(s_val) * L_chi_neg4(s_val)
    rel_err = abs(e2_direct - e2_factor) / abs(e2_factor)
    print(f"| {float(s_val):.0f}   | {float(e2_direct.real):>19.12f} | {float(e2_factor.real):>16.12f} | {float(rel_err):.2e}   |")


# ===================================================================
# Part 5: The Sato-Tate distribution for split primes
# ===================================================================
print("\n\n## Part 5: Sato-Tate Distribution for E_i at Split Primes")
print("For CM curves, the Sato-Tate measure is NOT the semicircle.")
print("It is the UNIFORM distribution on [0, pi] (for the angle theta_p).")

# Compute theta_p = arccos(a_p / (2*sqrt(p))) for split primes p = 1 mod 4
print("\n| p   | a_p  | a_p/(2*sqrt(p)) | theta_p/pi    |")
print("|-----|------|-----------------|---------------|")

thetas = []
for p in range(5, 1000):
    # primality check
    is_prime = True
    for d in range(2, int(p**0.5) + 1):
        if p % d == 0:
            is_prime = False
            break
    if not is_prime or p % 4 != 1:
        continue

    ap = a_p_Ei(p)
    ratio = ap / (2 * np.sqrt(p))
    if abs(ratio) <= 1:
        theta = np.arccos(ratio)
        thetas.append(theta / np.pi)
        if p <= 97:
            print(f"| {p:3d} | {ap:>4d} | {ratio:>15.6f} | {theta/np.pi:>13.6f} |")

# Simple histogram
n_bins = 4
hist, edges = np.histogram(thetas, bins=n_bins, range=(0, 1))
total = len(thetas)
print(f"\nHistogram of theta_p/pi for {total} split primes p < 1000:")
print(f"| Bin              | Count | Fraction | Expected (uniform) |")
print(f"|------------------|-------|----------|---------------------|")
for i in range(n_bins):
    frac = hist[i] / total
    print(f"| [{edges[i]:.2f}, {edges[i+1]:.2f}) | {hist[i]:>5d} | {frac:>8.4f} | {1.0/n_bins:>19.4f} |")

# But CM Sato-Tate also has a delta function at theta = pi/2 (the inert primes)
print(f"\nNote: For CM curves, inert primes (p = 3 mod 4) have a_p = 0,")
print(f"giving theta_p = pi/2. These contribute a delta function at theta/pi = 0.5")
print(f"in the full Sato-Tate distribution.")


# ===================================================================
# Part 6: Flat connections on T^2 for various gauge groups
# ===================================================================
print("\n\n## Part 6: Flat Connections on T^2 = Commuting Pairs in G")
print("M_flat(G, T^2) = {(A, B) in G x G : [A, B] = 1} / conj")

print("\nFor G = U(1): M_flat = U(1) x U(1) = T^2")
print("  dim_R = 2, dim_C = 1")
print("  All pairs commute (U(1) is abelian)")

print("\nFor G = SU(2): M_flat = (T x T) / W = (U(1) x U(1)) / Z_2")
print("  T = U(1) (maximal torus of SU(2))")
print("  W = Z_2 (Weyl group, acting by z -> z^{-1})")
print("  dim_R = 2, dim_C = 1")
print("  Topologically: the pillowcase P^1")

print("\nFor G = SU(3): M_flat = (T^2 x T^2) / S_3")
print("  T = U(1)^2 (maximal torus of SU(3))")
print("  W = S_3 (Weyl group of SU(3))")
print("  dim_R = 4*2 = 8... wait:")
print("  Actually: rank(SU(3)) = 2, so T = U(1)^2")
print("  M_flat = (T x T) / W = (U(1)^2 x U(1)^2) / S_3")
print("  dim_R = 4 * 2 = 8? No: dim_R(T x T) = 2*rank + 2*rank = 8")
print("  Wait: T = U(1)^2, so T has dim_R = 2*rank(SU(3)) = 4")
print("  And T x T (two copies, for the two generators of pi_1(T^2)) has dim_R = 8")
print("  Modding by S_3 (discrete) doesn't change dimension")
print("  So dim_R M_flat(SU(3), T^2) = 8, dim_C = 4")

print("\nFor G = SU(3) x SU(2) x U(1):")
print("  dim_C M_flat = dim_C(SU(3) part) + dim_C(SU(2) part) + dim_C(U(1) part)")
print(f"              = 4 + 1 + 1 = 6")
print("  Wait, let me reconsider:")
print("  SU(2): rank = 1, so dim_C M_flat(SU(2), T^2) = 2*1 = 2")
print("  SU(3): rank = 2, so dim_C M_flat(SU(3), T^2) = 2*2 = 4")
print("  U(1):  rank = 1, so dim_C M_flat(U(1), T^2) = 2*1 = 2")
print("  Total: dim_C = 4 + 2 + 2 = 8")


# ===================================================================
# Part 7: Summary table
# ===================================================================
print("\n\n" + "=" * 70)
print("SUMMARY: What Geometric Langlands on T^2 Gives")
print("=" * 70)

print("""
Setting                  | Hecke eigensheaves | L-functions | RH status
-------------------------|--------------------|-----------  |-----------
E/C (geometric GL)       | EXIST (theorem)    | NO          | N/A
E/F_q (function field)   | EXIST (theorem)    | YES (Euler) | PROVED (Deligne)
E/Q, G=GL(2) (classical) | via modularity     | YES (Euler) | OPEN (GRH)
E/Q, G=SU(3)xSU(2)xU(1) | geometric: YES     | classical: NO | OPEN
                         | (Gaitsgory)        | (no GL bridge)|

The gap: geometric Langlands (over C) -> classical L-functions (over Q)
requires the arithmetic Langlands, which is NOT a consequence of
the geometric theorem.
""")

print("Done.")
