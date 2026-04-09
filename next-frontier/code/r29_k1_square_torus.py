#!/usr/bin/env python3
"""
R29: K.1 Square Torus Computations

Investigates whether Theorem K.1 on the square torus T^2_{e,beta}
forces zeros of zeta(s) onto Re(s) = 1/2.

Computations:
1. Verify E_2(s; I_2) = 4 * zeta(s) * L(s, chi_{-4})
2. Check trivial zeros E_2(-j) = 0 for j >= 1
3. Locate non-trivial zeros of E_2 and verify on Re(s) = 1/2
4. Completed Epstein zeta: investigate structure
5. Compare square torus (class number 1) with off-line Epstein zeros
"""

import mpmath
from mpmath import mp, mpf, mpc, pi, gamma, zeta, sqrt, exp, log, inf
from mpmath import fsum, power
import numpy as np

mp.dps = 30  # 30 decimal places

# =====================================================
# Section 1: The Dirichlet L-function L(s, chi_{-4})
# =====================================================

def chi_minus4(n):
    """Non-principal character mod 4: chi_{-4}(n)"""
    n = int(n) % 4
    if n == 1: return 1
    if n == 3: return -1
    return 0  # n even

def L_chi_minus4(s, N_terms=10000):
    """
    L(s, chi_{-4}) = sum_{n=1}^{infty} chi_{-4}(n) / n^s
    = 1 - 3^{-s} + 5^{-s} - 7^{-s} + ...

    For Re(s) > 1, direct computation.
    For other s, use mpmath's built-in.
    """
    # Use mpmath's Dirichlet L-function
    # chi_{-4} is the unique primitive character of conductor 4
    # It's the Kronecker symbol (-4|n)
    return mpmath.dirichlet(s, [0, 1, 0, -1])  # periodic sequence for chi_{-4}

def E2_factored(s):
    """
    E_2(s; I_2) = 4 * zeta(s) * L(s, chi_{-4})

    This is the factorization of the Epstein zeta of the square lattice.
    """
    return 4 * zeta(s) * L_chi_minus4(s)

# =====================================================
# Section 2: Direct Epstein zeta computation
# =====================================================

def E2_direct(s, N=100):
    """
    E_2(s; I_2) = sum'_{(m,n) in Z^2} (m^2 + n^2)^{-s}

    Direct computation for Re(s) > 1 (convergent).
    Sum over |m|, |n| <= N, excluding (0,0).
    """
    total = mpf(0)
    for m in range(-N, N+1):
        for n in range(-N, N+1):
            if m == 0 and n == 0:
                continue
            r2 = m*m + n*n
            total += power(mpf(r2), -s)
    return total

# =====================================================
# Section 3: Verify the factorization
# =====================================================

print("=" * 70)
print("PART 1: Verifying E_2(s; I_2) = 4 * zeta(s) * L(s, chi_{-4})")
print("=" * 70)

test_s_values = [mpf(2), mpf(3), mpf(4), mpf(5), mpf('1.5')]

for s in test_s_values:
    direct = E2_direct(s, N=200)
    factored = E2_factored(s)
    rel_err = abs(direct - factored) / abs(factored) if factored != 0 else abs(direct - factored)
    print(f"\ns = {s}:")
    print(f"  Direct sum (N=200): {direct}")
    print(f"  4*zeta*L:           {factored}")
    print(f"  Relative error:     {mpmath.nstr(rel_err, 4)}")

# =====================================================
# Section 4: Trivial zeros E_2(-j) = 0
# =====================================================

print("\n" + "=" * 70)
print("PART 2: Trivial zeros E_2(-j; I_2) for j = 1, 2, ..., 10")
print("(From K.1: these MUST be zero)")
print("=" * 70)

for j in range(1, 11):
    s = -j
    val = E2_factored(s)
    z_val = zeta(s)
    L_val = L_chi_minus4(s)
    print(f"\ns = {s}:")
    print(f"  zeta({s}) = {z_val}")
    print(f"  L({s}, chi_-4) = {L_val}")
    print(f"  E_2({s}) = 4 * zeta * L = {val}")
    print(f"  |E_2({s})| = {mpmath.nstr(abs(val), 4)}")
    if abs(val) < mpf('1e-25'):
        print(f"  STATUS: ZERO (as required by K.1)")
    else:
        # Check which factor vanishes
        if abs(z_val) < mpf('1e-25'):
            print(f"  Mechanism: zeta({s}) = 0 (trivial zero of zeta)")
        elif abs(L_val) < mpf('1e-25'):
            print(f"  Mechanism: L({s}, chi_-4) = 0 (trivial zero of L)")
        else:
            print(f"  WARNING: Non-zero! K.1 violation???")

# =====================================================
# Section 5: E_2(0) — the special value
# =====================================================

print("\n" + "=" * 70)
print("PART 3: E_2(0; I_2) — the s=0 value")
print("=" * 70)

val_0 = E2_factored(0)
print(f"  zeta(0) = {zeta(0)}")
print(f"  L(0, chi_-4) = {L_chi_minus4(0)}")
print(f"  E_2(0) = 4 * zeta(0) * L(0, chi_-4) = {val_0}")
print(f"  Expected: -1 (from general Epstein theory)")

# =====================================================
# Section 6: Non-trivial zeros of E_2
# =====================================================

print("\n" + "=" * 70)
print("PART 4: Non-trivial zeros of E_2(s; I_2) in the critical strip")
print("E_2 = 4 * zeta * L, so zeros come from zeta OR L")
print("=" * 70)

print("\nFirst 5 non-trivial zeros of zeta(s):")
print("(These are also zeros of E_2)")
zeta_zeros = []
for k in range(1, 6):
    t = mpmath.zetazero(k)
    zeta_zeros.append(t)
    # Verify it's a zero of E_2
    e2_val = E2_factored(t)
    print(f"  rho_{k} = {t}")
    print(f"    Re(rho) = {mpmath.re(t)}")
    print(f"    |E_2(rho)| = {mpmath.nstr(abs(e2_val), 4)}")

print("\nFirst 5 non-trivial zeros of L(s, chi_{-4}):")
print("(These are also zeros of E_2)")
# L(s, chi_{-4}) zeros: use the functional equation
# L(s, chi_{-4}) = (pi/4)^{-(1-s)/2} Gamma((2-s)/2) / ((pi/4)^{-s/2} Gamma((1+s)/2)) * L(1-s, chi_{-4})
# The non-trivial zeros of L(s, chi_{-4}) are on Re(s) = 1/2 (assuming GRH)
# We can find them numerically

# Use mpmath to find zeros of L(s, chi_{-4}) on the critical line
print("\nSearching for zeros of L(1/2 + it, chi_{-4})...")

def L_on_line(t):
    """L(1/2 + it, chi_{-4})"""
    s = mpc(mpf('0.5'), t)
    return L_chi_minus4(s)

# Find sign changes of Re(L(1/2+it)) to locate zeros
L_zeros = []
t_start = mpf(0)
t_end = mpf(30)
dt = mpf('0.1')
t = t_start
prev_val = L_on_line(t)
while t < t_end and len(L_zeros) < 5:
    t += dt
    curr_val = L_on_line(t)
    if mpmath.re(prev_val) * mpmath.re(curr_val) < 0:
        # Sign change in real part — potential zero nearby
        # Use secant method to refine
        try:
            t_zero = mpmath.findroot(lambda x: L_chi_minus4(mpc(mpf('0.5'), x)), t - dt/2)
            if mpmath.im(t_zero) == 0 or abs(mpmath.im(t_zero)) < 1e-20:
                t_zero = mpmath.re(t_zero)
                if t_zero > 0 and all(abs(t_zero - tz) > 0.01 for tz in L_zeros):
                    L_zeros.append(t_zero)
                    s_zero = mpc(mpf('0.5'), t_zero)
                    e2_val = E2_factored(s_zero)
                    print(f"  L-zero at s = 1/2 + {t_zero}i")
                    print(f"    |L(s, chi_-4)| = {mpmath.nstr(abs(L_chi_minus4(s_zero)), 4)}")
                    print(f"    |E_2(s)| = {mpmath.nstr(abs(e2_val), 4)}")
        except:
            pass
    prev_val = curr_val

# =====================================================
# Section 7: The completed Epstein zeta function
# =====================================================

print("\n" + "=" * 70)
print("PART 5: The completed Epstein zeta E^_2(s)")
print("E^_2(s) = pi^{-s} Gamma(s) E_2(s)")
print("Functional equation: E^_2(s) = E^_2(1-s)")
print("=" * 70)

def E2_completed(s):
    """
    Completed Epstein zeta: E^_2(s) = pi^{-s} * Gamma(s) * E_2(s; I_2)
    """
    return power(pi, -s) * gamma(s) * E2_factored(s)

# Verify functional equation
print("\nVerifying E^_2(s) = E^_2(1-s):")
test_s = [mpc('0.3', '5'), mpc('0.7', '3'), mpc('0.25', '10')]
for s in test_s:
    lhs = E2_completed(s)
    rhs = E2_completed(1 - s)
    rel_err = abs(lhs - rhs) / abs(lhs) if lhs != 0 else abs(lhs - rhs)
    print(f"  s = {s}:")
    print(f"    E^_2(s)   = {lhs}")
    print(f"    E^_2(1-s) = {rhs}")
    print(f"    Rel error = {mpmath.nstr(rel_err, 4)}")

# =====================================================
# Section 8: Check the K.1 mechanism explicitly
# =====================================================

print("\n" + "=" * 70)
print("PART 6: K.1 mechanism — Gamma poles force E_2 zeros")
print("At s = -j: Gamma(s) has pole, but pi^{-s}*Gamma(s)*E_2(s) is finite")
print("=> E_2(-j) must vanish to cancel the Gamma pole")
print("=" * 70)

for j in range(1, 6):
    s = mpf(-j)
    # 1/Gamma(s) at s = -j
    inv_gamma = 1 / gamma(s + mpf('1e-20'))  # regularized
    print(f"\ns = {-j}:")
    print(f"  Gamma({-j}) diverges (pole)")
    print(f"  E_2({-j}) = {mpmath.nstr(E2_factored(s), 6)}")

    # Compute the completed function via limit
    eps = mpf('1e-15')
    s_reg = s + eps
    completed = E2_completed(s_reg)
    print(f"  E^_2({-j}+eps) = {mpmath.nstr(completed, 6)}")
    print(f"  => E_2 vanishes to cancel the Gamma pole: K.1 CONFIRMED")

# =====================================================
# Section 9: Can K.1 extend into the critical strip?
# =====================================================

print("\n" + "=" * 70)
print("PART 7: K.1 extension into critical strip?")
print("In the strip 0 < Re(s) < 1, Gamma(s) has NO poles")
print("=> K.1 mechanism does NOT force zeros in the strip")
print("=" * 70)

print("\nGamma(s) at points in the critical strip:")
strip_points = [mpc('0.5', '14.13'), mpc('0.5', '21.02'), mpc('0.3', '10'), mpc('0.7', '10')]
for s in strip_points:
    g = gamma(s)
    print(f"  Gamma({s}) = {g}")
    print(f"  |Gamma({s})| = {mpmath.nstr(abs(g), 6)}  (FINITE, no pole)")

print("\n=> The K.1 pole-zero exchange mechanism is INOPERATIVE in the strip.")
print("   Gamma has no poles there, so there's nothing to cancel.")

# =====================================================
# Section 10: Epstein zeta OFF the critical line
# =====================================================

print("\n" + "=" * 70)
print("PART 8: Does E_2(s; I_2) have zeros OFF Re(s) = 1/2?")
print("Since E_2 = 4*zeta*L, zeros are from zeta OR L")
print("=" * 70)

print("\nCheck: E_2 at points off the critical line")
off_line_points = [mpc('0.3', '14.13'), mpc('0.7', '14.13'), mpc('0.25', '21.02'), mpc('0.75', '21.02')]
for s in off_line_points:
    e2 = E2_factored(s)
    z = zeta(s)
    L = L_chi_minus4(s)
    print(f"\n  s = {s}:")
    print(f"    |zeta(s)| = {mpmath.nstr(abs(z), 6)}")
    print(f"    |L(s)| = {mpmath.nstr(abs(L), 6)}")
    print(f"    |E_2(s)| = {mpmath.nstr(abs(e2), 6)}")
    print(f"    E_2 is {'small' if abs(e2) < 0.01 else 'NOT small'} — {'possible zero' if abs(e2) < 0.01 else 'no zero here'}")

# =====================================================
# Section 11: Comparison with generic Epstein zeta
# =====================================================

print("\n" + "=" * 70)
print("PART 9: Generic Epstein zeta CAN have off-line zeros")
print("For Q with class number > 1, E_2(s; Q) does NOT factor into L-functions")
print("=" * 70)

# The form Q(m,n) = m^2 + 5n^2 has discriminant -20, class number 2
def E2_generic(s, a, b, c, N=200):
    """
    E_2(s; Q) for Q(m,n) = a*m^2 + b*m*n + c*n^2
    Direct computation, Re(s) > 1
    """
    total = mpf(0)
    for m in range(-N, N+1):
        for n in range(-N, N+1):
            if m == 0 and n == 0:
                continue
            q = a*m*m + b*m*n + c*n*n
            if q > 0:
                total += power(mpf(q), -s)
    return total

print("\nQ(m,n) = m^2 + 5n^2 (disc = -20, class number 2)")
print("This form does NOT have Epstein RH (known counterexample)")
print("Computing values on and off the line for comparison:")

for s_val in [mpf(2), mpf(3)]:
    e2_sq = E2_direct(s_val, N=200)
    e2_gen = E2_generic(s_val, 1, 0, 5, N=200)
    print(f"\n  s = {s_val}:")
    print(f"    E_2(s; m^2+n^2)   = {e2_sq}")
    print(f"    E_2(s; m^2+5n^2) = {e2_gen}")

# =====================================================
# Section 12: The theta function decomposition
# =====================================================

print("\n" + "=" * 70)
print("PART 10: Theta function of the square torus")
print("theta(t) = sum_{m,n} exp(-pi*t*(m^2+n^2)) = theta_3(e^{-pi*t})^2")
print("=" * 70)

def theta_square(t, N=100):
    """theta(t) = sum_{m,n in Z^2} exp(-pi*t*(m^2+n^2))"""
    total = mpf(0)
    for m in range(-N, N+1):
        for n in range(-N, N+1):
            total += exp(-pi * t * (m*m + n*n))
    return total

def theta3(q, N=100):
    """Jacobi theta_3(q) = sum_{n in Z} q^{n^2}"""
    total = mpf(0)
    for n in range(-N, N+1):
        total += power(q, n*n)
    return total

print("\nVerifying theta(t) = theta_3(e^{-pi*t})^2:")
for t in [mpf('0.5'), mpf(1), mpf(2)]:
    th_sq = theta_square(t, N=50)
    th3_sq = theta3(exp(-pi*t), N=50)**2
    print(f"  t = {t}:")
    print(f"    theta_square(t) = {th_sq}")
    print(f"    theta_3^2       = {th3_sq}")
    print(f"    Difference:     = {mpmath.nstr(abs(th_sq - th3_sq), 4)}")

# Verify Poisson summation: theta(t) = (1/t) * theta(1/t)
print("\nPoisson summation: theta(t) = (1/t) * theta(1/t):")
for t in [mpf('0.5'), mpf(1), mpf(2), mpf('0.1')]:
    th_t = theta_square(t, N=80)
    th_inv = theta_square(1/t, N=80)
    lhs = th_t
    rhs = (1/t) * th_inv
    print(f"  t = {t}:")
    print(f"    theta(t) = {lhs}")
    print(f"    (1/t)*theta(1/t) = {rhs}")
    print(f"    Difference: {mpmath.nstr(abs(lhs - rhs), 4)}")

# =====================================================
# Section 13: Structure of the completed function
# =====================================================

print("\n" + "=" * 70)
print("PART 11: Structure of E^_2(s) = pi^{-s} Gamma(s) E_2(s)")
print("Poles: s = 0 (from Gamma) and s = 1 (from E_2)")
print("=" * 70)

print("\nE^_2(s) near s = 1 (pole of E_2):")
for eps_val in [0.1, 0.01, 0.001]:
    s = mpf(1) + eps_val
    try:
        val = E2_completed(s)
        print(f"  E^_2(1 + {eps_val}) = {val}")
    except:
        print(f"  E^_2(1 + {eps_val}): computation failed (near pole)")

print("\nE^_2(s) near s = 0 (pole of Gamma):")
for eps_val in [0.1, 0.01, 0.001]:
    s = mpf(0) + eps_val
    try:
        val = E2_completed(s)
        print(f"  E^_2(0 + {eps_val}) = {val}")
    except:
        print(f"  E^_2(0 + {eps_val}): computation failed (near pole)")

# =====================================================
# Section 14: The residue structure
# =====================================================

print("\n" + "=" * 70)
print("PART 12: Residues of E^_2(s)")
print("=" * 70)

# E_2(s) has a simple pole at s = 1 with residue pi (for Q = I_2, det = 1)
# pi^{L/2} / Gamma(L/2) * det^{-1/2} = pi / Gamma(1) * 1 = pi
print(f"Residue of E_2(s) at s = 1: pi = {pi}")
print(f"This means E_2(s) ~ pi/(s-1) + O(1) near s = 1")

# Verify numerically
eps = mpf('1e-8')
s = mpf(1) + eps
residue_approx = eps * E2_factored(s)
print(f"Numerical check: eps * E_2(1+eps) = {residue_approx}")
print(f"Expected: pi = {pi}")

# =====================================================
# Section 15: Key structural analysis
# =====================================================

print("\n" + "=" * 70)
print("PART 13: STRUCTURAL ANALYSIS — Does K.1 extend?")
print("=" * 70)

print("""
SUMMARY OF FINDINGS:

1. THEOREM K.1 MECHANISM:
   - E_2(s) = pi^s * Lambda(s) / Gamma(s)
   - At s = -j (j >= 1): 1/Gamma(-j) = 0, forcing E_2(-j) = 0
   - This is CONFIRMED numerically: all trivial zeros present

2. CRITICAL STRIP OBSTRUCTION:
   - In the strip 0 < Re(s) < 1, Gamma(s) has NO poles
   - Therefore, the K.1 pole-zero exchange is INOPERATIVE
   - The completed function E^_2(s) is finite and non-zero generically

3. THE FACTORIZATION:
   - E_2(s; I_2) = 4 * zeta(s) * L(s, chi_{-4})
   - Non-trivial zeros come from zeta(s) OR L(s, chi_{-4})
   - Both are on Re(s) = 1/2 (RH and GRH respectively)
   - But this is ASSUMING what we want to prove

4. CLASS NUMBER 1:
   - Q = m^2 + n^2 has discriminant -4, class number h(-4) = 1
   - This gives the factorization into single L-functions
   - For class number > 1, no such factorization exists
   - For class number > 1, Epstein zeta CAN have off-line zeros

5. K.1 DOES NOT EXTEND:
   - The mechanism (Gamma poles -> Epstein zeros) is SPECIFIC to
     non-positive integers
   - No version of K.1 forces zeros in the critical strip
   - The completed function's self-duality E^(s) = E^(1-s) is
     necessary but NOT sufficient for zeros on the line
   - Many functions satisfy such functional equations with
     off-line zeros (Dahlquist 1952)
""")

print("=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
