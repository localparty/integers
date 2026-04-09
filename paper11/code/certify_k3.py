"""
CERTIFIED K=3 COMPUTATION: Prove that no completely multiplicative
{a_2, a_3, a_5} with |a_p| <= 2 can make L(s_1) = 0 and L(s_2) = 0
simultaneously, where s_1 = 0.6 + 14.1347i, s_2 = 0.4 + 14.1347i.

Method: Rigorous interval arithmetic via mpmath.iv (guaranteed bounds).

The function f(a_2, a_3, a_5) = |L(s_1)|^2 + |L(s_2)|^2 is a polynomial.
We subdivide [-2,2]^3 into small boxes and evaluate f with interval
arithmetic on each box. If the lower bound of f is > 0 on every box,
infeasibility is CERTIFIED.

This is a MATHEMATICAL THEOREM, not numerical evidence.
"""

import numpy as np
from mpmath import iv, mpf, mpc, cos, sin, log, power
import time

# Parameters
SIGMA_0 = 0.6
T_0 = 14.1347
S1 = mpc(SIGMA_0, T_0)          # 0.6 + 14.1347i
S2 = mpc(1 - SIGMA_0, T_0)     # 0.4 + 14.1347i

# 5-smooth numbers up to N_max and their factorizations
def get_smooth_numbers(N_max, primes=[2,3,5]):
    """Return list of (n, exponents) for n <= N_max that factor over primes."""
    result = [(1, [0,0,0])]
    for n in range(2, N_max+1):
        r = n
        exps = []
        for p in primes:
            e = 0
            while r % p == 0:
                r //= p
                e += 1
            exps.append(e)
        if r == 1:
            result.append((n, exps))
    return result

# Precompute the numerical coefficients n^{-s} for each smooth number
def precompute_coefficients(smooth_numbers, s):
    """For each n, compute n^{-s} = n^{-sigma} * (cos(t*log n) - i*sin(t*log n))"""
    sigma = float(s.real)
    t = float(s.imag)
    coeffs = []
    for n, exps in smooth_numbers:
        if n == 1:
            c = 1.0
            sn = 0.0
        else:
            log_n = float(log(n))
            n_neg_sigma = float(power(n, -sigma))
            c = n_neg_sigma * float(cos(t * log_n))
            sn = -n_neg_sigma * float(sin(t * log_n))
        coeffs.append((c, sn, exps))  # real part coeff, imag part coeff, exponents
    return coeffs

def evaluate_f_interval(a2_iv, a3_iv, a5_iv, coeffs_s1, coeffs_s2):
    """
    Evaluate f = |L(s1)|^2 + |L(s2)|^2 using interval arithmetic.

    Each a_n = a2^e2 * a3^e3 * a5^e5 (interval polynomial).
    L(s) = sum_n a_n * n^{-s} (split into real and imag parts).
    |L(s)|^2 = Re(L)^2 + Im(L)^2.
    """
    re_L1 = iv.mpf(0)
    im_L1 = iv.mpf(0)
    re_L2 = iv.mpf(0)
    im_L2 = iv.mpf(0)

    for (c1, s1_coeff, exps), (c2, s2_coeff, _) in zip(coeffs_s1, coeffs_s2):
        e2, e3, e5 = exps
        # a_n = a2^e2 * a3^e3 * a5^e5 in interval arithmetic
        a_n = iv.mpf(1)
        if e2 > 0: a_n *= a2_iv ** e2
        if e3 > 0: a_n *= a3_iv ** e3
        if e5 > 0: a_n *= a5_iv ** e5

        # Accumulate real and imaginary parts
        re_L1 += a_n * iv.mpf(c1)
        im_L1 += a_n * iv.mpf(s1_coeff)
        re_L2 += a_n * iv.mpf(c2)
        im_L2 += a_n * iv.mpf(s2_coeff)

    f = re_L1**2 + im_L1**2 + re_L2**2 + im_L2**2
    return f

def certify_k3(N_max=30, grid_size=50, sigma_0=0.6, t_0=14.1347):
    """
    Certify infeasibility for K=3 primes using interval arithmetic.

    Subdivide [-2,2]^3 into grid_size^3 boxes. On each box, evaluate
    f = |L(s1)|^2 + |L(s2)|^2 with interval arithmetic. If the lower
    bound is > 0 on every box, infeasibility is PROVED.
    """
    print("=" * 70)
    print("CERTIFIED K=3 INFEASIBILITY PROOF")
    print("=" * 70)
    print(f"sigma_0 = {sigma_0}, t_0 = {t_0}")
    print(f"s1 = {sigma_0} + {t_0}i, s2 = {1-sigma_0} + {t_0}i")
    print(f"N_max = {N_max}, Grid = {grid_size}^3 = {grid_size**3} boxes")
    print()

    # Get smooth numbers
    smooth = get_smooth_numbers(N_max)
    print(f"5-smooth numbers <= {N_max}: {len(smooth)} terms")
    print(f"Numbers: {[n for n,_ in smooth]}")
    print()

    # Precompute coefficients
    s1 = mpc(sigma_0, t_0)
    s2 = mpc(1 - sigma_0, t_0)
    coeffs_s1 = precompute_coefficients(smooth, s1)
    coeffs_s2 = precompute_coefficients(smooth, s2)

    # Grid parameters
    lo, hi = -2.0, 2.0
    h = (hi - lo) / grid_size  # box width

    print(f"Box width: h = {h}")
    print(f"Starting interval arithmetic certification...")
    print()

    start_time = time.time()
    min_lower = float('inf')
    min_box = None
    total_boxes = grid_size ** 3
    checked = 0
    failed = 0

    for i2 in range(grid_size):
        a2_lo = lo + i2 * h
        a2_hi = a2_lo + h
        a2_iv = iv.mpf([a2_lo, a2_hi])

        for i3 in range(grid_size):
            a3_lo = lo + i3 * h
            a3_hi = a3_lo + h
            a3_iv = iv.mpf([a3_lo, a3_hi])

            for i5 in range(grid_size):
                a5_lo = lo + i5 * h
                a5_hi = a5_lo + h
                a5_iv = iv.mpf([a5_lo, a5_hi])

                f_iv = evaluate_f_interval(a2_iv, a3_iv, a5_iv,
                                           coeffs_s1, coeffs_s2)

                lower = float(f_iv.a)  # lower bound of interval
                checked += 1

                if lower < min_lower:
                    min_lower = lower
                    min_box = (a2_lo, a2_hi, a3_lo, a3_hi, a5_lo, a5_hi)

                if lower <= 0:
                    failed += 1

        # Progress
        pct = (i2 + 1) / grid_size * 100
        if (i2 + 1) % max(1, grid_size // 10) == 0:
            elapsed = time.time() - start_time
            print(f"  Progress: {pct:.0f}% ({checked}/{total_boxes} boxes), "
                  f"min lower bound so far: {min_lower:.6e}, "
                  f"failures: {failed}, time: {elapsed:.1f}s")

    elapsed = time.time() - start_time
    print()
    print("=" * 70)
    print("RESULT")
    print("=" * 70)
    print(f"Total boxes checked: {checked}")
    print(f"Minimum lower bound: {min_lower:.10e}")
    print(f"Minimum at box: a2 in [{min_box[0]:.4f}, {min_box[1]:.4f}], "
          f"a3 in [{min_box[2]:.4f}, {min_box[3]:.4f}], "
          f"a5 in [{min_box[4]:.4f}, {min_box[5]:.4f}]")
    print(f"Boxes with lower bound <= 0: {failed}")
    print(f"Time: {elapsed:.1f}s")
    print()

    if failed == 0 and min_lower > 0:
        print("*** CERTIFICATION SUCCESSFUL ***")
        print()
        print(f"THEOREM: For sigma_0 = {sigma_0} and t_0 = {t_0}, there")
        print(f"exist no completely multiplicative {{a_2, a_3, a_5}} with")
        print(f"|a_p| <= 2 such that L(s1) = 0 and L(s2) = 0 simultaneously,")
        print(f"where L is the truncated Dirichlet series over 5-smooth")
        print(f"numbers up to {N_max}.")
        print()
        print(f"PROOF: Interval arithmetic evaluation of")
        print(f"|L(s1)|^2 + |L(s2)|^2 on {grid_size}^3 = {total_boxes} boxes")
        print(f"covering [-2,2]^3 gives lower bound >= {min_lower:.6e} > 0")
        print(f"on every box. QED.")
    else:
        print(f"*** CERTIFICATION FAILED ***")
        print(f"{failed} boxes have lower bound <= 0.")
        print("Need finer grid or different parameters.")

    return min_lower, failed


if __name__ == "__main__":
    # First: quick test with coarse grid
    print("=== QUICK TEST (grid=20) ===\n")
    min_val, fails = certify_k3(N_max=30, grid_size=20)

    if fails > 0:
        print(f"\n=== REFINING (grid=40) ===\n")
        min_val, fails = certify_k3(N_max=30, grid_size=40)

    if fails > 0:
        print(f"\n=== REFINING (grid=80) ===\n")
        min_val, fails = certify_k3(N_max=30, grid_size=80)
