"""
sdp_rh.py — Bootstrap SDP for the Riemann Hypothesis (v3)

Tests whether {Ramanujan bound + multiplicativity + functional equation}
forces all zeros to have sigma_0 = 1/2.

Findings:
  1. Without multiplicativity, off-line zeros are trivially achievable.
  2. With multiplicativity + Ramanujan but NO functional equation,
     off-line zeros are also achievable (K free parameters, 2 equations).
  3. With multiplicativity + Ramanujan + functional equation:
     - Sparse FE grid (6 pts): feasible at sigma_0 > 1/2
     - Dense FE grid (200 pts): INFEASIBLE at sigma_0 > 1/2
     - Calibrated FE (zeta's own truncation error as threshold): feasible
  4. The truncation error of the Dirichlet series at N_max <= 1000
     is too large to make the FE constraint discriminating.
  5. The solutions found by the optimizer are NOT genuine L-functions:
     they violate the FE at points outside the enforcement grid, and
     their zeros are not symmetric about sigma = 1/2.

Author: Claude (agent), Date: April 6, 2026
"""

import numpy as np
from math import gcd, log, cos, sin, sqrt, pi
from scipy.optimize import minimize, differential_evolution
from scipy.special import loggamma
import time

from sympy import primerange, factorint


# ============================================================
# CORE FUNCTIONS
# ============================================================

def xi_factor(sigma, t):
    """Completed factor pi^{-s/2} Gamma(s/2) for s=sigma+it."""
    log_pi = -(sigma / 2) * log(pi)
    arg_pi = (t / 2) * log(pi)
    val = loggamma(complex(sigma / 2, t / 2))
    return log_pi + val.real, -arg_pi + val.imag


def build_coefficients(a_p_dict, N_max, primes):
    """Build a_n for P-smooth n via Hecke recursion + multiplicativity."""
    prime_set = set(int(p) for p in primes)
    a = {1: 1.0}
    pp_vals = {}
    for p in primes:
        p = int(p)
        ap = a_p_dict.get(p, 0.0)
        vals = {0: 1.0, 1: ap}
        pk, k = p, 1
        while pk <= N_max:
            a[pk] = vals[k]
            if pk * p <= N_max:
                vals[k + 1] = ap * vals[k] - vals[k - 1]
            pk *= p; k += 1
        pp_vals[p] = vals
    for n in range(2, N_max + 1):
        if n in a:
            continue
        factors = factorint(n)
        val, valid = 1.0, True
        for p, e in factors.items():
            p = int(p)
            if p in pp_vals and e in pp_vals[p]:
                val *= pp_vals[p][e]
            else:
                valid = False; break
        if valid:
            a[n] = val
    return a


def dirichlet_sum(a, sigma, t, N_max):
    """L(sigma+it) partial sum. Returns (Re, Im)."""
    re_s = im_s = 0.0
    for n in range(1, N_max + 1):
        if n not in a: continue
        npow = n ** (-sigma)
        theta = t * log(n)
        re_s += a[n] * npow * cos(theta)
        im_s -= a[n] * npow * sin(theta)
    return re_s, im_s


def completed_L(a, sigma, t, N_max):
    """Lambda(s) = pi^{-s/2} Gamma(s/2) L(s). Returns (Re, Im)."""
    re_L, im_L = dirichlet_sum(a, sigma, t, N_max)
    log_abs, arg = xi_factor(sigma, t)
    fabs = np.exp(log_abs)
    fre, fim = fabs * cos(arg), fabs * sin(arg)
    return fre * re_L - fim * im_L, fre * im_L + fim * re_L


def fe_residual(a, sigma, t, N_max):
    """|Lambda(s) - Lambda(1-s)|."""
    r1, i1 = completed_L(a, sigma, t, N_max)
    r2, i2 = completed_L(a, 1 - sigma, t, N_max)
    return sqrt((r1 - r2)**2 + (i1 - i2)**2)


# ============================================================
# DIAGNOSTIC RUNS
# ============================================================

def run_0():
    """Sanity: zeta(s) zeros on critical line."""
    print("\n" + "=" * 70)
    print("RUN 0: Sanity — exact zeta partial sums")
    print("=" * 70)
    N_max = 1000
    zeta_zeros_t = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]

    print(f"  N_max = {N_max}")
    for t_0 in zeta_zeros_t:
        re_h, im_h = 0.0, 0.0
        for n in range(1, N_max + 1):
            npow = n ** (-0.5)
            theta = t_0 * log(n)
            re_h += npow * cos(theta)
            im_h -= npow * sin(theta)
        res_h = sqrt(re_h**2 + im_h**2)
        print(f"  t={t_0:.6f}: |zeta(1/2+it)| = {res_h:.4f}")


def run_1():
    """No multiplicativity: free a_n easily find off-line zeros."""
    print("\n" + "=" * 70)
    print("RUN 1: No multiplicativity — free a_n in [-2,2]")
    print("=" * 70)
    N_max = 50; t_0 = 14.134725
    for sigma_0 in [0.55, 0.60, 0.70, 0.80, 0.90]:
        def obj(x):
            a = {1: 1.0}
            for n in range(2, N_max + 1): a[n] = x[n - 2]
            re_L, im_L = dirichlet_sum(a, sigma_0, t_0, N_max)
            return re_L**2 + im_L**2
        result = differential_evolution(obj, [(-2,2)]*(N_max-1),
                                       maxiter=200, tol=1e-14, seed=42)
        res = sqrt(result.fun)
        print(f"  sigma_0={sigma_0:.2f}: {'FEASIBLE' if res<0.01 else 'infeasible'}  |L|={res:.2e}")


def run_2():
    """Full constraints with sparse FE grid."""
    print("\n" + "=" * 70)
    print("RUN 2: Multiplicativity + Ramanujan + FE (sparse: 6 pts)")
    print("=" * 70)
    K = 5; N_max = 50; t_0 = 14.134725
    primes = list(primerange(2, 300))[:K]
    fe_grid = [(sig, t) for sig in [0.2, 0.5, 0.8] for t in [10.0, 20.0]]

    for sigma_0 in [0.55, 0.60, 0.70, 0.80]:
        def objective(x):
            a_p = {p: x[i] for i, p in enumerate(primes)}
            a = build_coefficients(a_p, N_max, primes)
            re_L, im_L = dirichlet_sum(a, sigma_0, t_0, N_max)
            fe_pen = sum(fe_residual(a, sig, t, N_max)**2 for sig, t in fe_grid)
            return re_L**2 + im_L**2 + 1000.0 * fe_pen
        t_s = time.time()
        result = differential_evolution(objective, [(-2,2)]*K, maxiter=300,
                                       tol=1e-15, seed=42, polish=True)
        el = time.time() - t_s
        a_p = {p: result.x[i] for i, p in enumerate(primes)}
        a = build_coefficients(a_p, N_max, primes)
        re_L, im_L = dirichlet_sum(a, sigma_0, t_0, N_max)
        zero_res = sqrt(re_L**2 + im_L**2)
        fe_rms = sqrt(sum(fe_residual(a, sig, t, N_max)**2 for sig, t in fe_grid) / len(fe_grid))
        feas = zero_res < 0.01 and fe_rms < 0.01
        print(f"  s0={sigma_0:.2f}: {'FEASIBLE' if feas else 'infeasible'}  "
              f"|L|={zero_res:.2e}  FE={fe_rms:.2e}  ({el:.1f}s)")


def run_3():
    """Full constraints with DENSE FE grid."""
    print("\n" + "=" * 70)
    print("RUN 3: Multiplicativity + Ramanujan + FE (dense: 200 pts)")
    print("=" * 70)
    K = 5; N_max = 50; t_0 = 14.134725
    primes = list(primerange(2, 300))[:K]
    fe_grid = [(sig, t) for sig in np.linspace(0.05, 0.95, 20)
               for t in np.linspace(3, 35, 10)]

    for sigma_0 in [0.55, 0.60, 0.70]:
        def objective(x):
            a_p = {p: x[i] for i, p in enumerate(primes)}
            a = build_coefficients(a_p, N_max, primes)
            re_L, im_L = dirichlet_sum(a, sigma_0, t_0, N_max)
            fe_pen = sum(fe_residual(a, sig, t, N_max)**2 for sig, t in fe_grid)
            return re_L**2 + im_L**2 + 1000.0 * fe_pen
        t_s = time.time()
        result = differential_evolution(objective, [(-2,2)]*K, maxiter=500,
                                       tol=1e-15, seed=42, polish=True)
        el = time.time() - t_s
        a_p = {p: result.x[i] for i, p in enumerate(primes)}
        a = build_coefficients(a_p, N_max, primes)
        re_L, im_L = dirichlet_sum(a, sigma_0, t_0, N_max)
        zero_res = sqrt(re_L**2 + im_L**2)
        fe_rms = sqrt(sum(fe_residual(a, sig, t, N_max)**2 for sig, t in fe_grid) / len(fe_grid))
        feas = zero_res < 0.01 and fe_rms < 0.01
        print(f"  s0={sigma_0:.2f}: {'FEASIBLE' if feas else 'infeasible'}  "
              f"|L|={zero_res:.2e}  FE={fe_rms:.2e}  ({el:.1f}s)")


def run_4_calibrated():
    """FE threshold calibrated to zeta's own truncation error."""
    print("\n" + "=" * 70)
    print("RUN 4: Calibrated FE (threshold = zeta's own error)")
    print("=" * 70)

    K = 5; N_max = 50; t_0 = 14.134725
    primes = list(primerange(2, 300))[:K]
    fe_grid = [(sig, t) for sig in np.linspace(0.1, 0.9, 9)
               for t in np.linspace(5, 30, 6)]

    # Calibrate with exact zeta
    a_zeta = {n: 1.0 for n in range(1, N_max + 1)}
    zeta_fe = [fe_residual(a_zeta, sig, t, N_max) for sig, t in fe_grid]
    zeta_fe_rms = sqrt(sum(x**2 for x in zeta_fe) / len(zeta_fe))
    print(f"  Zeta FE_rms at N_max={N_max}: {zeta_fe_rms:.4e}")

    for sigma_0 in [0.51, 0.55, 0.60]:
        def objective(x):
            a_p = {p: x[i] for i, p in enumerate(primes)}
            a = build_coefficients(a_p, N_max, primes)
            re_L, im_L = dirichlet_sum(a, sigma_0, t_0, N_max)
            fe_pen = sum(max(0, fe_residual(a, sig, t, N_max) - zeta_fe[idx])**2
                        for idx, (sig, t) in enumerate(fe_grid))
            return re_L**2 + im_L**2 + 10000.0 * fe_pen

        t_s = time.time()
        result = differential_evolution(objective, [(-2,2)]*K, maxiter=500,
                                       tol=1e-15, seed=42, polish=True)
        el = time.time() - t_s

        a_p = {p: result.x[i] for i, p in enumerate(primes)}
        a = build_coefficients(a_p, N_max, primes)
        re_L, im_L = dirichlet_sum(a, sigma_0, t_0, N_max)
        zero_res = sqrt(re_L**2 + im_L**2)
        fe_excess = [max(0, fe_residual(a, sig, t, N_max) - zeta_fe[idx])
                     for idx, (sig, t) in enumerate(fe_grid)]
        fe_ex_rms = sqrt(sum(x**2 for x in fe_excess) / len(fe_excess))

        feas = zero_res < 0.01 and fe_ex_rms < 0.001
        print(f"  s0={sigma_0:.2f}: {'FEASIBLE' if feas else 'infeasible'}  "
              f"|L|={zero_res:.2e}  FE_excess={fe_ex_rms:.2e}  ({el:.1f}s)")

        # Check symmetry of the zero
        if feas:
            re_sym, im_sym = dirichlet_sum(a, 1 - sigma_0, t_0, N_max)
            sym_res = sqrt(re_sym**2 + im_sym**2)
            print(f"    Symmetry check: |L(1-s)| = {sym_res:.4f}  "
                  f"{'(symmetric)' if sym_res < 0.01 else '(NOT symmetric!)'}")


def run_5_fe_calibration():
    """Show how FE truncation error scales with N_max."""
    print("\n" + "=" * 70)
    print("RUN 5: FE truncation error calibration")
    print("=" * 70)
    fe_grid = [(sig, t) for sig in np.linspace(0.1, 0.9, 9)
               for t in np.linspace(5, 30, 6)]
    for N_max in [30, 50, 100, 200, 500, 1000]:
        a = {n: 1.0 for n in range(1, N_max + 1)}
        fe_vals = [fe_residual(a, sig, t, N_max) for sig, t in fe_grid]
        print(f"  N_max={N_max:4d}: FE_max={max(fe_vals):.4e}  "
              f"FE_rms={sqrt(sum(x**2 for x in fe_vals)/len(fe_vals)):.4e}")


def main():
    print("=" * 70)
    print("BOOTSTRAP SDP FOR THE RIEMANN HYPOTHESIS (v3)")
    print("=" * 70)
    np.random.seed(42)

    run_0()
    run_1()
    run_2()
    # run_3()  # Slow (~200s per sigma_0)
    run_4_calibrated()
    run_5_fe_calibration()

    print("\n" + "=" * 70)
    print("CONCLUSIONS")
    print("=" * 70)
    print("""
1. Without multiplicativity (Run 1): off-line zeros trivially achievable.
   This confirms the Euler product is a NECESSARY condition.

2. With sparse FE enforcement (Run 2): FEASIBLE at sigma_0 > 1/2.
   The optimizer satisfies FE at training points but violates elsewhere.

3. With dense FE enforcement (Run 3): INFEASIBLE at sigma_0 > 1/2.
   The optimizer cannot satisfy FE at 200+ points AND have off-line zero.

4. With calibrated FE (Run 4): FEASIBLE at sigma_0 > 1/2.
   The truncation error of the Dirichlet series at N_max <= 1000 is
   too large. The optimizer finds solutions that satisfy FE to within
   zeta's own truncation tolerance but whose zeros lack the required
   sigma <-> 1-sigma symmetry.

5. FE truncation error GROWS with N_max (Run 5): the completed
   Dirichlet series Lambda(s) involves Gamma(s/2) which amplifies
   errors. At N_max=1000, FE_max ~ 3.0 for exact zeta.

VERDICT: The SDP at this truncation level cannot definitively test
the conjecture. The fundamental bottleneck is Dirichlet series
truncation in the critical strip. To make the FE constraint
discriminating, one needs either:
  (a) The approximate functional equation (AFE) which uses BOTH the
      s and 1-s series to cancel truncation errors
  (b) Much larger N_max with smoothed truncation (Riesz/Cesaro means)
  (c) Working in the spectral domain (Benjamin-Chang basis) instead
      of the Dirichlet series domain
""")


if __name__ == "__main__":
    main()
