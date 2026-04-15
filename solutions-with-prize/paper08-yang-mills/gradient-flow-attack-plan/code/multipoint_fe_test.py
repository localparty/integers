"""
Multi-Point Functional Equation Test (v5)

Tests whether enforcing the functional equation at MANY points
(not just the two paired-zero points) restores infeasibility
for off-line zeros when K >= 10 primes.

The key insight: with M FE enforcement points, we get 2 + 2M real
constraints vs K unknowns. For K=15 and M=20, that's 42 vs 15
(over-determined). The two-point test only had 4 constraints.

Variables: {a_p} for K primes, |a_p| <= 2, completely multiplicative.
Objective: minimize |L(s0)|^2 + lambda * sum_j |chi(s_j)*L(1-s_j) - L(s_j)|^2
"""

import numpy as np
from scipy.optimize import minimize
from scipy.special import loggamma
import time
import sys

sys.stdout.reconfigure(line_buffering=True)

PRIMES_ALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# =============================================================================
# Core arithmetic
# =============================================================================

def build_factorization_table(primes, n_max):
    """Precompute exponent vectors for all smooth n in [1, n_max]."""
    table = [None] * (n_max + 1)
    table[1] = []
    for n in range(2, n_max + 1):
        remaining = n
        factors = []
        for i, p in enumerate(primes):
            e = 0
            while remaining % p == 0:
                remaining //= p
                e += 1
            if e > 0:
                factors.append((i, e))
        table[n] = factors if remaining == 1 else None
    return table


def extend_coefficients(a_p, fact_table, n_max):
    """Build multiplicative a_n from a_p using precomputed factorization."""
    a = np.zeros(n_max + 1, dtype=complex)
    a[1] = 1.0
    for n in range(2, n_max + 1):
        factors = fact_table[n]
        if factors is None:
            a[n] = 0.0
        else:
            val = 1.0
            for idx, exp in factors:
                val *= a_p[idx] ** exp
            a[n] = val
    return a


# =============================================================================
# chi(s) via loggamma (overflow-safe)
# =============================================================================

def chi_factor(s):
    """chi(s) = pi^{s-1/2} * Gamma((1-s)/2) / Gamma(s/2).
    Uses loggamma to avoid overflow."""
    log_chi = (s - 0.5) * np.log(np.pi) + loggamma((1.0 - s) / 2.0) - loggamma(s / 2.0)
    return np.exp(log_chi)


def L_trunc(s, coeffs, n_max):
    """Evaluate truncated L-function: sum_{n=1}^{n_max} a_n * n^{-s}."""
    ns = np.arange(1, n_max + 1, dtype=float)
    return np.sum(coeffs * ns ** (-s))


# =============================================================================
# Multi-point FE objective
# =============================================================================

def make_objective(sigma_0, t_0, fe_points, primes, n_max, fact_table, lam):
    """Create the objective function for multi-point FE test.

    fe_points: list of complex s_j where FE is enforced
    lam: weight for FE penalty

    Objective = |L(s0)|^2 + lam * sum_j |chi(s_j)*L(1-s_j) - L(s_j)|^2
    """
    K = len(primes)
    s0 = sigma_0 + 1j * t_0

    # Precompute n^{-s} for the zero point and all FE points
    ns = np.arange(1, n_max + 1, dtype=float)
    pow_s0 = ns ** (-s0)

    # Precompute for FE enforcement points
    fe_data = []
    for sj in fe_points:
        chi_sj = chi_factor(sj)
        pow_sj = ns ** (-sj)
        pow_1msj = ns ** (-(1.0 - sj))
        fe_data.append((chi_sj, pow_sj, pow_1msj))

    def objective(a_p_real):
        a = extend_coefficients(a_p_real.astype(complex), fact_table, n_max)
        coeffs = a[1:n_max + 1]

        # Zero constraint: L(s0) = 0
        L_s0 = np.sum(coeffs * pow_s0)
        zero_penalty = abs(L_s0) ** 2

        # FE constraints: chi(s_j) * L(1-s_j) - L(s_j) = 0
        fe_penalty = 0.0
        for chi_sj, pow_sj, pow_1msj in fe_data:
            L_sj = np.sum(coeffs * pow_sj)
            L_1msj = np.sum(coeffs * pow_1msj)
            residual = chi_sj * L_1msj - L_sj
            fe_penalty += abs(residual) ** 2

        return zero_penalty + lam * fe_penalty

    return objective


# =============================================================================
# Run one test configuration
# =============================================================================

def run_test(sigma_0, t_0, K, M, lam, n_max=300, n_trials=80,
             fe_line='same', verbose=True):
    """Run the multi-point FE test.

    sigma_0: real part of hypothetical off-line zero
    t_0: imaginary part
    K: number of primes
    M: number of FE enforcement points
    lam: FE penalty weight
    n_max: truncation for Dirichlet series
    fe_line: 'same' = FE points at Re(s) = sigma_0
             'critical' = FE points at Re(s) = 0.5
    """
    primes = PRIMES_ALL[:K]
    fact_table = build_factorization_table(primes, n_max)

    # Build FE sample points
    if fe_line == 'same':
        fe_sigma = sigma_0
    else:
        fe_sigma = 0.5

    fe_points = [fe_sigma + 1j * (10.0 + j * 5.0) for j in range(M)]

    objective = make_objective(sigma_0, t_0, fe_points, primes, n_max,
                               fact_table, lam)

    best_val = np.inf
    best_ap = None

    for trial in range(n_trials):
        if trial == 0:
            a_p0 = np.ones(K)
        elif trial == 1:
            a_p0 = -np.ones(K)
        elif trial == 2:
            a_p0 = np.zeros(K)
        elif trial < 10:
            a_p0 = 2.0 * np.cos(np.arange(K) * trial * np.pi / K)
        else:
            a_p0 = np.random.uniform(-2, 2, K)

        bounds = [(-2.0, 2.0)] * K
        result = minimize(objective, a_p0, method='L-BFGS-B', bounds=bounds,
                         options={'maxiter': 3000, 'ftol': 1e-18})

        if result.fun < best_val:
            best_val = result.fun
            best_ap = result.x.copy()

        if best_val < 1e-15:
            break

    # Decompose the best result
    a = extend_coefficients(best_ap.astype(complex), fact_table, n_max)
    coeffs = a[1:n_max + 1]
    ns = np.arange(1, n_max + 1, dtype=float)
    s0 = sigma_0 + 1j * t_0
    L_s0_val = abs(np.sum(coeffs * ns ** (-s0))) ** 2

    fe_resid = 0.0
    fe_sigma_val = sigma_0 if fe_line == 'same' else 0.5
    for j in range(M):
        sj = fe_sigma_val + 1j * (10.0 + j * 5.0)
        chi_sj = chi_factor(sj)
        L_sj = np.sum(coeffs * ns ** (-sj))
        L_1msj = np.sum(coeffs * ns ** (-(1.0 - sj)))
        fe_resid += abs(chi_sj * L_1msj - L_sj) ** 2

    feasible = best_val < 1e-8
    status = "FEASIBLE" if feasible else "INFEASIBLE"

    if verbose:
        print(f"  sigma={sigma_0:.2f} K={K:2d} M={M:3d} lam={lam:6.1f} | "
              f"total={best_val:.3e} zero={L_s0_val:.3e} fe={fe_resid:.3e} | "
              f"{status}")

    return best_val, L_s0_val, fe_resid, status, best_ap


# =============================================================================
# Test suite
# =============================================================================

def test_1_constraint_counting():
    """K=15, varying M. Does over-determination return?"""
    print("=" * 80)
    print("TEST 1: CONSTRAINT COUNTING (K=15, varying M)")
    print("  M=5:  12 constraints vs 15 unknowns -> under-determined")
    print("  M=20: 42 constraints vs 15 unknowns -> over-determined")
    print("  M=50: 102 constraints vs 15 unknowns -> strongly over-determined")
    print("=" * 80)

    K = 15
    t_0 = 14.135
    lam = 10.0

    for M in [0, 5, 10, 20, 50]:
        constraints = 2 + 2 * M
        label = f"({constraints} constraints vs {K} unknowns)"
        print(f"\n--- M={M} {label} ---")
        for sigma in [0.50, 0.55, 0.60, 0.70]:
            run_test(sigma, t_0, K, M, lam)


def test_2_large_K():
    """K=30, M=50. Over-determined even with many primes."""
    print("\n" + "=" * 80)
    print("TEST 2: LARGE K (K=30, M=50)")
    print("  102 constraints vs 30 unknowns -> over-determined")
    print("=" * 80)

    K = 30
    # Need more primes
    # We have 25 primes in PRIMES_ALL, use them all + extend if needed
    # Actually K=30 > len(PRIMES_ALL)=25, let's use K=25
    K = min(K, len(PRIMES_ALL))
    t_0 = 14.135
    M = 50
    lam = 10.0

    constraints = 2 + 2 * M
    print(f"  Actual: {constraints} constraints vs {K} unknowns")
    for sigma in [0.50, 0.55, 0.60, 0.70]:
        run_test(sigma, t_0, K, M, lam)


def test_3_lambda_sensitivity():
    """Does the FE weight lambda matter?"""
    print("\n" + "=" * 80)
    print("TEST 3: LAMBDA SENSITIVITY (K=15, M=20, sigma=0.60)")
    print("=" * 80)

    K = 15
    t_0 = 14.135
    M = 20

    for lam in [0.1, 1.0, 10.0, 100.0, 1000.0]:
        run_test(0.60, t_0, K, M, lam)


def test_4_sigma_sweep():
    """Sweep sigma from 0.50 to 0.90. Map feasibility boundary."""
    print("\n" + "=" * 80)
    print("TEST 4: SIGMA SWEEP (K=15, M=30, lam=10)")
    print("  Expect: FEASIBLE at 0.50, INFEASIBLE at sigma > 0.50")
    print("=" * 80)

    K = 15
    t_0 = 14.135
    M = 30
    lam = 10.0

    sigmas = [0.500, 0.505, 0.510, 0.520, 0.530, 0.550, 0.600, 0.700, 0.800, 0.900]
    for sigma in sigmas:
        run_test(sigma, t_0, K, M, lam)


def test_5_fe_on_critical_line():
    """FE enforcement on the critical line Re(s) = 1/2.
    The FE is automatically satisfied there for genuine L-functions.
    Does it change the result?"""
    print("\n" + "=" * 80)
    print("TEST 5: FE ENFORCEMENT ON CRITICAL LINE vs SAME LINE")
    print("  K=15, M=20, lam=10")
    print("=" * 80)

    K = 15
    t_0 = 14.135
    M = 20
    lam = 10.0

    print("\n--- FE on same line (Re(s) = sigma_0) ---")
    for sigma in [0.50, 0.55, 0.60]:
        run_test(sigma, t_0, K, M, lam, fe_line='same')

    print("\n--- FE on critical line (Re(s) = 0.5) ---")
    for sigma in [0.50, 0.55, 0.60]:
        run_test(sigma, t_0, K, M, lam, fe_line='critical')


def test_6_no_fe_baseline():
    """Baseline: zero constraint alone (no FE), confirm K>=10 is feasible."""
    print("\n" + "=" * 80)
    print("TEST 6: BASELINE — ZERO ONLY, NO FE (M=0)")
    print("  Confirms K>=10 off-line zeros are feasible without FE")
    print("=" * 80)

    t_0 = 14.135
    for K in [5, 8, 10, 15]:
        print(f"\n--- K={K} ---")
        for sigma in [0.50, 0.55, 0.60]:
            run_test(sigma, t_0, K, 0, 0.0)


def test_7_paired_plus_fe():
    """Paired zero (s0 AND 1-s0) PLUS multi-point FE.
    The original test plus dense FE."""
    print("\n" + "=" * 80)
    print("TEST 7: PAIRED ZERO + MULTI-POINT FE (K=15, M=20)")
    print("  Adds L(1-s0)=0 as second zero constraint")
    print("=" * 80)

    K = 15
    t_0 = 14.135
    M = 20
    lam = 10.0
    n_max = 300
    n_trials = 80
    primes = PRIMES_ALL[:K]
    fact_table = build_factorization_table(primes, n_max)
    ns = np.arange(1, n_max + 1, dtype=float)

    for sigma_0 in [0.50, 0.55, 0.60, 0.70]:
        s0 = sigma_0 + 1j * t_0
        s0_conj = (1.0 - sigma_0) + 1j * t_0  # paired zero

        pow_s0 = ns ** (-s0)
        pow_s0c = ns ** (-s0_conj)

        # FE points
        fe_points = [sigma_0 + 1j * (10.0 + j * 5.0) for j in range(M)]
        fe_data = []
        for sj in fe_points:
            chi_sj = chi_factor(sj)
            pow_sj = ns ** (-sj)
            pow_1msj = ns ** (-(1.0 - sj))
            fe_data.append((chi_sj, pow_sj, pow_1msj))

        def objective(a_p_real, _pow_s0=pow_s0, _pow_s0c=pow_s0c,
                      _fe_data=fe_data):
            a = extend_coefficients(a_p_real.astype(complex), fact_table, n_max)
            coeffs = a[1:n_max + 1]

            L_s0 = np.sum(coeffs * _pow_s0)
            L_s0c = np.sum(coeffs * _pow_s0c)
            zero_pen = abs(L_s0) ** 2 + abs(L_s0c) ** 2

            fe_pen = 0.0
            for chi_sj, pow_sj, pow_1msj in _fe_data:
                L_sj = np.sum(coeffs * pow_sj)
                L_1msj = np.sum(coeffs * pow_1msj)
                fe_pen += abs(chi_sj * L_1msj - L_sj) ** 2

            return zero_pen + lam * fe_pen

        best_val = np.inf
        for trial in range(n_trials):
            if trial == 0:
                a_p0 = np.ones(K)
            elif trial == 1:
                a_p0 = -np.ones(K)
            elif trial == 2:
                a_p0 = np.zeros(K)
            elif trial < 10:
                a_p0 = 2.0 * np.cos(np.arange(K) * trial * np.pi / K)
            else:
                a_p0 = np.random.uniform(-2, 2, K)

            bounds = [(-2.0, 2.0)] * K
            result = minimize(objective, a_p0, method='L-BFGS-B', bounds=bounds,
                             options={'maxiter': 3000, 'ftol': 1e-18})
            if result.fun < best_val:
                best_val = result.fun
            if best_val < 1e-15:
                break

        feasible = best_val < 1e-8
        status = "FEASIBLE" if feasible else "INFEASIBLE"
        print(f"  sigma={sigma_0:.2f}: min={best_val:.3e} -> {status}")


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    np.random.seed(42)
    start = time.time()

    test_6_no_fe_baseline()
    test_1_constraint_counting()
    test_2_large_K()
    test_3_lambda_sensitivity()
    test_4_sigma_sweep()
    test_5_fe_on_critical_line()
    test_7_paired_plus_fe()

    elapsed = time.time() - start
    print(f"\n{'=' * 80}")
    print(f"Total runtime: {elapsed:.1f} seconds")
    print(f"{'=' * 80}")
