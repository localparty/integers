"""
SDP v3: Approximate Functional Equation + Scale-Up

Building on v2 (paired-zero test with multiplicativity + functional equation).

Key findings from this round:
1. The AFE at t=14.135 uses only X=Y=2 terms (too few for meaningful test)
2. The AFE needs t >> 100 for enough terms to involve multiple primes
3. With K >= 10 primes and sufficient optimization, the Dirichlet paired-zero
   test becomes FEASIBLE even off-line -- more parameters give the optimizer
   more freedom
4. For small K (3-8), the Dirichlet test remains INFEASIBLE off-line
5. The AFE with safe chi factor (loggamma) is FEASIBLE at all K for large t

The v2 infeasibility signal (K=15, sigma>0.5) does NOT reproduce with
sufficient optimization trials. This suggests the original v2 result
was either from a different configuration or insufficient optimization.
"""

import numpy as np
from scipy.optimize import minimize
from scipy.special import loggamma
import time
import sys

sys.stdout.reconfigure(line_buffering=True)

# =============================================================================
# Configuration
# =============================================================================

PRIMES_ALL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71]

# =============================================================================
# Core arithmetic — precomputed factorization table
# =============================================================================

def build_factorization_table(primes, n_max):
    """Precompute exponent vectors for all n in [1, n_max]."""
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


def extend_coefficients_fast(a_p, fact_table, n_max):
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
# chi(s) factor — safe version using loggamma
# =============================================================================

def chi_factor(s):
    """chi(s) = pi^{s-1/2} * Gamma((1-s)/2) / Gamma(s/2).
    Uses loggamma to avoid overflow for large Im(s)."""
    log_chi = (s - 0.5) * np.log(np.pi) + loggamma((1.0 - s) / 2.0) - loggamma(s / 2.0)
    return np.exp(log_chi)


# =============================================================================
# Paired-zero test
# =============================================================================

def test_paired_zeros(sigma_0, t_0, primes, n_max, fact_table,
                      n_trials=50, use_afe=False):
    """Test if a_p exist (|a_p| <= 2, multiplicative) such that:
      L(sigma_0 + i*t_0) = 0  AND  L((1-sigma_0) + i*t_0) = 0.

    use_afe=True: use AFE representation (includes chi(s) factor)
    use_afe=False: use plain Dirichlet sum
    """
    K = len(primes)
    s1 = sigma_0 + 1j * t_0
    s2 = (1.0 - sigma_0) + 1j * t_0

    # Precompute n^{-s} arrays
    ns = np.arange(1, n_max + 1, dtype=float)
    pow_s1 = ns ** (-s1)
    pow_s2 = ns ** (-s2)

    # AFE setup
    use_afe_actual = use_afe
    t = abs(t_0)
    if t < 2 * np.pi:
        use_afe_actual = False

    if use_afe_actual:
        XY = t / (2 * np.pi)
        X = min(int(np.sqrt(XY)) + 1, n_max)
        Y = X
        chi_s1 = chi_factor(s1)
        chi_s2 = chi_factor(s2)
        pow_1ms1 = ns ** (-(1.0 - s1))
        pow_1ms2 = ns ** (-(1.0 - s2))

    def objective(a_p_real):
        a = extend_coefficients_fast(a_p_real.astype(complex), fact_table, n_max)
        coeffs = a[1:n_max+1]

        if use_afe_actual:
            L1 = np.sum(coeffs[:X] * pow_s1[:X]) + chi_s1 * np.sum(coeffs[:Y] * pow_1ms1[:Y])
            L2 = np.sum(coeffs[:X] * pow_s2[:X]) + chi_s2 * np.sum(coeffs[:Y] * pow_1ms2[:Y])
        else:
            L1 = np.sum(coeffs * pow_s1)
            L2 = np.sum(coeffs * pow_s2)

        return abs(L1)**2 + abs(L2)**2

    best_val = np.inf
    best_ap = None

    for trial in range(n_trials):
        if trial == 0:
            a_p0 = np.ones(K)
        elif trial == 1:
            a_p0 = -np.ones(K)
        elif trial == 2:
            a_p0 = np.zeros(K)
        elif trial < 8:
            a_p0 = 2.0 * np.cos(np.arange(K) * trial * np.pi / K)
        else:
            a_p0 = np.random.uniform(-2, 2, K)

        bounds = [(-2.0, 2.0)] * K
        result = minimize(objective, a_p0, method='L-BFGS-B', bounds=bounds,
                         options={'maxiter': 2000, 'ftol': 1e-18})

        if result.fun < best_val:
            best_val = result.fun
            best_ap = result.x.copy()

        if best_val < 1e-15:
            break

    return best_val, best_ap


# =============================================================================
# Main experiments
# =============================================================================

def run_diagnostics():
    print("=" * 70)
    print("RH SDP v3: AFE + SCALE-UP DIAGNOSTICS")
    print("=" * 70)

    t_0 = 14.135

    # ==================================================================
    # PART A: Dirichlet paired-zero test — varying K
    # ==================================================================
    print()
    print("=" * 70)
    print("PART A: DIRICHLET PAIRED-ZERO TEST — CONVERGENCE WITH K")
    print(f"N_max=300, t_0={t_0}")
    print("=" * 70)

    n_max = 300
    K_values = [3, 5, 8, 10, 15, 20]

    for sigma in [0.50, 0.55, 0.60, 0.70]:
        print(f"\nsigma_0 = {sigma:.2f}")
        for K in K_values:
            primes = PRIMES_ALL[:K]
            fact = build_factorization_table(primes, n_max)
            val, _ = test_paired_zeros(sigma, t_0, primes, n_max, fact,
                                        n_trials=50, use_afe=False)
            status = "FEASIBLE" if val < 1e-8 else "INFEASIBLE"
            print(f"  K={K:2d} (up to p={primes[-1]:3d}): min = {val:.3e} -> {status}")

    # ==================================================================
    # PART B: AFE at t=14.135 (X=2 terms — degenerate case)
    # ==================================================================
    print()
    print("=" * 70)
    print("PART B: AFE AT t=14.135 (X=Y=2 — DEGENERATE)")
    print("NOTE: Only 2 terms in each AFE sum. Not a meaningful test.")
    print("=" * 70)

    K = 10
    primes = PRIMES_ALL[:K]
    fact = build_factorization_table(primes, n_max)

    for sigma in [0.50, 0.55, 0.60]:
        val, _ = test_paired_zeros(sigma, t_0, primes, n_max, fact,
                                    n_trials=30, use_afe=True)
        status = "FEASIBLE" if val < 1e-8 else "INFEASIBLE"
        print(f"  sigma_0={sigma:.2f}: min = {val:.3e} -> {status}")

    # ==================================================================
    # PART C: AFE at larger t values (where it has enough terms)
    # ==================================================================
    print()
    print("=" * 70)
    print("PART C: AFE AT LARGER t VALUES")
    print("=" * 70)

    K = 10
    primes = PRIMES_ALL[:K]
    fact = build_factorization_table(primes, n_max)

    for t_test in [100, 500, 1000, 5000]:
        XY = t_test / (2 * np.pi)
        X = min(int(np.sqrt(XY)) + 1, n_max)
        print(f"\nt_0={t_test}, AFE terms X=Y={X}")
        for sigma in [0.50, 0.55, 0.60]:
            val_dir, _ = test_paired_zeros(sigma, t_test, primes, n_max, fact,
                                            n_trials=30, use_afe=False)
            val_afe, _ = test_paired_zeros(sigma, t_test, primes, n_max, fact,
                                            n_trials=30, use_afe=True)
            st_d = "F" if val_dir < 1e-8 else "I"
            st_a = "F" if val_afe < 1e-8 else "I"
            print(f"  sigma={sigma:.2f}: Dir={val_dir:.3e}({st_d})  AFE={val_afe:.3e}({st_a})")

    # ==================================================================
    # PART D: Scaled-up v2 (K=20, N_max=500)
    # ==================================================================
    print()
    print("=" * 70)
    print("PART D: SCALED-UP (K=20, N_max=500)")
    print("=" * 70)

    K_big = 20
    primes_big = PRIMES_ALL[:K_big]
    n_max_big = 500
    fact_big = build_factorization_table(primes_big, n_max_big)
    smooth_count = sum(1 for n in range(1, n_max_big+1) if fact_big[n] is not None)
    print(f"\n{smooth_count} / {n_max_big} integers are {primes_big[-1]}-smooth")

    print(f"\n--- Fine sigma grid: 0.500 to 0.520 (step 0.004) ---")
    for sigma in np.arange(0.500, 0.521, 0.004):
        val, _ = test_paired_zeros(sigma, t_0, primes_big, n_max_big, fact_big,
                                    n_trials=50, use_afe=False)
        status = "FEASIBLE" if val < 1e-8 else "INFEASIBLE"
        print(f"  sigma_0={sigma:.3f}: min = {val:.3e} -> {status}")

    print(f"\n--- Coarse grid: 0.52 to 0.60 ---")
    for sigma in np.arange(0.52, 0.61, 0.02):
        val, _ = test_paired_zeros(sigma, t_0, primes_big, n_max_big, fact_big,
                                    n_trials=50, use_afe=False)
        status = "FEASIBLE" if val < 1e-8 else "INFEASIBLE"
        print(f"  sigma_0={sigma:.2f}: min = {val:.3e} -> {status}")

    # ==================================================================
    # PART E: Convergence with K at large t (AFE meaningful)
    # ==================================================================
    print()
    print("=" * 70)
    print("PART E: CONVERGENCE WITH K AT t=5000 (AFE: X=29)")
    print("=" * 70)

    t_large = 5000
    K_values = [3, 5, 8, 10, 15, 20]

    for sigma in [0.55, 0.60]:
        print(f"\nsigma_0 = {sigma}")
        print(f"{'K':>4}  {'Dir min':>12}  {'AFE min':>12}  {'Dir':>4}  {'AFE':>4}")
        print("-" * 42)
        for K in K_values:
            primes_k = PRIMES_ALL[:K]
            fact_k = build_factorization_table(primes_k, n_max)
            val_dir, _ = test_paired_zeros(sigma, t_large, primes_k, n_max, fact_k,
                                            n_trials=30, use_afe=False)
            val_afe, _ = test_paired_zeros(sigma, t_large, primes_k, n_max, fact_k,
                                            n_trials=30, use_afe=True)
            st_d = "F" if val_dir < 1e-8 else "I"
            st_a = "F" if val_afe < 1e-8 else "I"
            print(f"{K:4d}  {val_dir:12.3e}  {val_afe:12.3e}  {st_d:>4}  {st_a:>4}")

    # ==================================================================
    # SUMMARY
    # ==================================================================
    print()
    print("=" * 70)
    print("SUMMARY AND INTERPRETATION")
    print("=" * 70)
    print("""
FINDING 1: DIRICHLET PAIRED-ZERO TEST
  - With K <= 8 primes (8 free parameters): INFEASIBLE off-line.
    The system is genuinely over-determined.
  - With K >= 10 primes (10+ free parameters): FEASIBLE off-line.
    More parameters give the optimizer enough freedom.

FINDING 2: THE K-DEPENDENCE PROBLEM
  The paired-zero constraint has K free parameters (one per prime)
  and 4 real constraints (Re/Im of L(s1)=0 and L(s2)=0). When K < ~9,
  the system is over-determined (4 constraints, K unknowns). When K >= 10,
  it becomes under-determined (4 constraints, K >= 10 unknowns).

  This means the v2 infeasibility at K=15 either:
  (a) was from a different code version, or
  (b) used insufficient optimization trials

FINDING 3: AFE AT t=14.135 IS DEGENERATE
  The AFE at t=14.135 uses only X=Y=2 terms. The "infeasibility" is
  an artifact of having too few terms, not genuine arithmetic obstruction.

FINDING 4: AFE AT LARGE t IS FEASIBLE
  With enough terms (t=5000, X=29), the AFE paired-zero test is FEASIBLE
  at all sigma values and all K. The chi(s) factor does not create
  additional constraints strong enough to block off-line zeros.

CONCLUSION:
  The paired-zero test as currently formulated (optimize K free a_p
  to zero out L at two points) does NOT provide reliable evidence for
  RH when K >= 10. The test only works when K is small enough that
  4 constraints > K unknowns.

  To make this approach work, we need EITHER:
  (a) Many more constraint points (not just s1, s2, but a whole curve)
  (b) A proper SDP/convex formulation (not local optimization)
  (c) Additional constraints beyond just L(s)=0 at two points
""")


if __name__ == "__main__":
    np.random.seed(42)
    start = time.time()
    run_diagnostics()
    elapsed = time.time() - start
    print(f"\nTotal runtime: {elapsed:.1f} seconds")
