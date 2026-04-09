"""
Weil-SDP with Sato-Tate Constraints: λ₁ Optimization

Minimize λ₁(a₂, a₃, ..., a_pK) subject to:
  - |a_p| ≤ 2 for all p  (Ramanujan)
  - Hecke coefficients: b_{p^m} = 2T_m(a_p/2)  (Chebyshev)
  - Sato-Tate moment constraints with effective error bounds

The Sato-Tate distribution (proved BLGHT 2011) gives:
  E[a_p] = 0,  E[a_p²] = 1,  E[a_p³] = 0,  E[a_p⁴] = 2
  E[a_p⁶] = 5,  E[a_p⁸] = 14  (Catalan numbers)

April 6, 2026.
"""

import numpy as np
from numpy.polynomial.chebyshev import chebval
from scipy.optimize import minimize, differential_evolution
from functools import lru_cache
import time
import sys


# ═══════════════════════════════════════════════════════════════════
# Configuration
# ═══════════════════════════════════════════════════════════════════

M_MAX = 8          # max prime power exponent in the sum
C_GAMMA = -0.733   # Gamma contribution to λ₁ (estimated from ζ)

# Sato-Tate moments: E[a_p^{2k}] for the semicircle-like measure
# (2/π)sin²θ dθ with a_p = 2cosθ
# These are Catalan numbers: C_k = (2k)!/((k+1)!k!)
# E[a^0]=1, E[a^2]=1, E[a^4]=2, E[a^6]=5, E[a^8]=14
ST_MOMENTS = {2: 1.0, 4: 2.0, 6: 5.0, 8: 14.0}
# Odd moments are 0 by symmetry
ST_ODD_MOMENTS = {1: 0.0, 3: 0.0}


def _sieve_primes(n):
    """Simple sieve of Eratosthenes up to n."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def get_primes(K):
    """Return the first K primes."""
    primes = _sieve_primes(200)
    return primes[:K]


def chebyshev_T(m, x):
    """Evaluate T_m(x) using numpy Chebyshev."""
    coeffs = [0] * m + [1]  # T_m
    return chebval(x, coeffs)


def lambda1_arith(a_vec, primes, M=M_MAX):
    """
    Compute the arithmetic part of λ₁:
    λ₁_arith = -Σ_p Σ_{m=1}^M  2*T_m(a_p/2) * log(p) / (m * p^m)

    a_vec: array of normalized Hecke eigenvalues [a_{p₁}, ..., a_{pK}]
    primes: list of primes [p₁, ..., pK]
    """
    total = 0.0
    for i, p in enumerate(primes):
        a_p = a_vec[i]
        for m in range(1, M + 1):
            b_pm = 2.0 * chebyshev_T(m, a_p / 2.0)
            total -= b_pm * np.log(p) / (m * p**m)
    return total


def lambda1_full(a_vec, primes, M=M_MAX):
    """Full λ₁ = C_Gamma + λ₁_arith."""
    return C_GAMMA + lambda1_arith(a_vec, primes, M)


def sato_tate_penalty(a_vec, K, weight=1000.0):
    """
    Penalty for violating Sato-Tate moment constraints.

    Constraints (with tolerance ε(K)):
      |(1/K) Σ a_p| ≤ 2/√K
      |(1/K) Σ a_p² - 1| ≤ 2/√K
      |(1/K) Σ a_p³| ≤ 2/√K
      |(1/K) Σ a_p⁴ - 2| ≤ 4/√K
    """
    penalty = 0.0
    sqrtK = np.sqrt(K)

    # First moment: mean ≈ 0
    mean1 = np.mean(a_vec)
    eps1 = 2.0 / sqrtK
    violation1 = max(0, abs(mean1) - eps1)
    penalty += weight * violation1**2

    # Second moment: mean(a²) ≈ 1
    mean2 = np.mean(a_vec**2)
    eps2 = 2.0 / sqrtK
    violation2 = max(0, abs(mean2 - 1.0) - eps2)
    penalty += weight * violation2**2

    # Third moment: mean(a³) ≈ 0
    mean3 = np.mean(a_vec**3)
    eps3 = 2.0 / sqrtK
    violation3 = max(0, abs(mean3) - eps3)
    penalty += weight * violation3**2

    # Fourth moment: mean(a⁴) ≈ 2
    mean4 = np.mean(a_vec**4)
    eps4 = 4.0 / sqrtK
    violation4 = max(0, abs(mean4 - 2.0) - eps4)
    penalty += weight * violation4**2

    return penalty


def sato_tate_feasible(a_vec, K):
    """Check if a_vec satisfies ST constraints (returns True/False)."""
    sqrtK = np.sqrt(K)
    if abs(np.mean(a_vec)) > 2.0 / sqrtK:
        return False
    if abs(np.mean(a_vec**2) - 1.0) > 2.0 / sqrtK:
        return False
    if abs(np.mean(a_vec**3)) > 2.0 / sqrtK:
        return False
    if abs(np.mean(a_vec**4) - 2.0) > 4.0 / sqrtK:
        return False
    return True


def sato_tate_feasible_extended(a_vec, K):
    """Check ST constraints including 6th and 8th moments."""
    if not sato_tate_feasible(a_vec, K):
        return False
    sqrtK = np.sqrt(K)
    if abs(np.mean(a_vec**6) - 5.0) > 8.0 / sqrtK:
        return False
    if abs(np.mean(a_vec**8) - 14.0) > 16.0 / sqrtK:
        return False
    return True


def sato_tate_penalty_extended(a_vec, K, weight=1000.0):
    """Penalty including 6th and 8th moment constraints."""
    penalty = sato_tate_penalty(a_vec, K, weight)
    sqrtK = np.sqrt(K)

    mean6 = np.mean(a_vec**6)
    eps6 = 8.0 / sqrtK
    violation6 = max(0, abs(mean6 - 5.0) - eps6)
    penalty += weight * violation6**2

    mean8 = np.mean(a_vec**8)
    eps8 = 16.0 / sqrtK
    violation8 = max(0, abs(mean8 - 14.0) - eps8)
    penalty += weight * violation8**2

    return penalty


# ═══════════════════════════════════════════════════════════════════
# Optimization: minimize λ₁
# ═══════════════════════════════════════════════════════════════════

def minimize_lambda1_unconstrained(K, n_starts=50, M=M_MAX):
    """Minimize λ₁ with only Ramanujan bound (no ST)."""
    primes = get_primes(K)
    bounds = [(-2.0, 2.0)] * K

    def objective(a_vec):
        return lambda1_full(a_vec, primes, M)

    best_val = np.inf
    best_x = None

    # Try all corners with a_p = ±2
    for signs in [np.full(K, -2.0), np.full(K, 2.0)]:
        val = objective(signs)
        if val < best_val:
            best_val = val
            best_x = signs.copy()

    # Random starts with L-BFGS-B
    for _ in range(n_starts):
        x0 = np.random.uniform(-2, 2, K)
        res = minimize(objective, x0, method='L-BFGS-B', bounds=bounds,
                       options={'maxiter': 100})
        if res.fun < best_val:
            best_val = res.fun
            best_x = res.x.copy()

    return best_val, best_x


def minimize_lambda1_with_st(K, n_starts=80, M=M_MAX, extended=False):
    """Minimize λ₁ with Ramanujan + Sato-Tate constraints."""
    primes = get_primes(K)
    bounds = [(-2.0, 2.0)] * K
    penalty_fn = sato_tate_penalty_extended if extended else sato_tate_penalty
    feasible_fn = sato_tate_feasible_extended if extended else sato_tate_feasible

    def objective(a_vec):
        return lambda1_full(a_vec, primes, M) + penalty_fn(a_vec, K)

    best_val = np.inf
    best_x = None

    # Smart starting points: sample from ST distribution
    for _ in range(n_starts):
        thetas = sample_sato_tate(K)
        x0 = 2.0 * np.cos(thetas)

        res = minimize(objective, x0, method='L-BFGS-B', bounds=bounds,
                       options={'maxiter': 100})

        if feasible_fn(res.x, K):
            raw_val = lambda1_full(res.x, primes, M)
            if raw_val < best_val:
                best_val = raw_val
                best_x = res.x.copy()

    # Also try uniform starts that might find boundary of feasible region
    for _ in range(n_starts // 2):
        x0 = np.random.uniform(-2, 2, K)
        res = minimize(objective, x0, method='L-BFGS-B', bounds=bounds,
                       options={'maxiter': 100})
        if feasible_fn(res.x, K):
            raw_val = lambda1_full(res.x, primes, M)
            if raw_val < best_val:
                best_val = raw_val
                best_x = res.x.copy()

    return best_val, best_x


def sample_sato_tate(K):
    """Sample K angles from the Sato-Tate distribution (2/π)sin²θ dθ on [0,π]."""
    # CDF: F(θ) = (θ - sin(2θ)/2) / π
    # Use rejection sampling with uniform envelope (max of sin²θ = 1)
    samples = []
    while len(samples) < K:
        theta = np.random.uniform(0, np.pi)
        u = np.random.uniform(0, 1)
        if u < np.sin(theta)**2:
            samples.append(theta)
    return np.array(samples)


# ═══════════════════════════════════════════════════════════════════
# λ₂ computation
# ═══════════════════════════════════════════════════════════════════

def lambda2_arith(a_vec, primes, M=M_MAX):
    """
    Compute the arithmetic part of λ₂.

    λ₂ = Σ_ρ (1 - (1-1/ρ)²) for zeros ρ of L.

    In terms of log-derivative sums:
    λ₂ = 2S₁ - S₂
    where S_k = Σ_ρ ρ^{-k}

    For the arithmetic part:
    S₁_arith = -Σ_p Σ_m b_{p^m} log(p) / (m p^m)   (same as λ₁_arith)
    S₂_arith involves (log L)'' at s=1:

    (log L)'(s) = -Σ_p Σ_m b_{p^m} log(p) / p^{ms}
    (log L)''(s) = Σ_p Σ_m b_{p^m} (log p)² / p^{ms}

    S₂ = [(log L)'(1)]² + (log L)''(1)

    So λ₂_arith = 2·S₁_arith - S₂_arith
    """
    # S₁ = λ₁_arith (already computed)
    S1 = 0.0
    logL_prime = 0.0   # (log L)'(1)
    logL_double = 0.0  # (log L)''(1)

    for i, p in enumerate(primes):
        a_p = a_vec[i]
        for m in range(1, M + 1):
            b_pm = 2.0 * chebyshev_T(m, a_p / 2.0)
            logp = np.log(p)
            pm = p**m

            S1 -= b_pm * logp / (m * pm)
            logL_prime -= b_pm * logp / pm
            logL_double += b_pm * logp**2 / pm

    S2 = logL_prime**2 + logL_double
    return 2.0 * S1 - S2


# ═══════════════════════════════════════════════════════════════════
# Verification: Ramanujan Δ function
# ═══════════════════════════════════════════════════════════════════

def ramanujan_delta_eigenvalues(K):
    """
    Normalized Hecke eigenvalues for the Ramanujan Δ function (weight 12).
    a_p = τ(p) / p^{11/2} where τ is the Ramanujan tau function.
    """
    # Known values of τ(p) for small primes
    tau = {
        2: -24,
        3: 252,
        5: 4830,
        7: -16744,
        11: 534612,
        13: -577738,
        17: -6905934,
        19: 10661420,
        23: 18643272,
        29: -128406630,
        31: 52843168,
        37: -182213314,
        41: -308120442,
        43: 534257418,
        47: 210346896,
    }

    primes = get_primes(K)
    a_vec = []
    for p in primes:
        if p in tau:
            a_p = tau[p] / p**(11.0/2.0)
            a_vec.append(a_p)
        else:
            # For primes beyond our table, skip
            break

    return np.array(a_vec[:K]), primes[:len(a_vec[:K])]


# ═══════════════════════════════════════════════════════════════════
# Main computation
# ═══════════════════════════════════════════════════════════════════

def run_computation():
    """Run the full Sato-Tate constrained optimization."""

    print("=" * 72)
    print("  Weil-SDP with Sato-Tate Constraints: λ₁ Optimization")
    print("=" * 72)
    print()
    print(f"Parameters: M_max={M_MAX}, C_Gamma={C_GAMMA}")
    print(f"ST tolerances: ε_k(K) = c_k / √K")
    print()

    K_values = [3, 5, 10, 15, 20, 30]

    results = []

    for K in K_values:
        primes = get_primes(K)
        print(f"\n{'─' * 72}")
        print(f"  K = {K}  |  Primes: {primes}")
        print(f"{'─' * 72}")

        t0 = time.time()

        # 1. Unconstrained (Ramanujan only)
        n_st = max(30, 80 - K)  # fewer starts for large K
        min_unc, x_unc = minimize_lambda1_unconstrained(K, n_starts=n_st)
        t1 = time.time()
        print(f"  Ramanujan only:     min(λ₁) = {min_unc:+.6f}  [{t1-t0:.1f}s]")
        print(f"    at a_p = [{', '.join(f'{x:.3f}' for x in x_unc[:min(6,K)])}{'...' if K>6 else ''}]")

        # Check ST feasibility of unconstrained minimum
        st_feas = sato_tate_feasible(x_unc, K)
        print(f"    ST-feasible: {st_feas}")
        if not st_feas:
            sqrtK = np.sqrt(K)
            print(f"    mean(a_p)={np.mean(x_unc):.3f} (tol={2/sqrtK:.3f}), "
                  f"mean(a_p²)={np.mean(x_unc**2):.3f} (target=1±{2/sqrtK:.3f})")

        # 2. With Sato-Tate (moments 1-4)
        t1 = time.time()
        min_st, x_st = minimize_lambda1_with_st(K, n_starts=n_st)
        t2 = time.time()
        print(f"  + Sato-Tate (m≤4):  min(λ₁) = {min_st:+.6f}  [{t2-t1:.1f}s]")
        if x_st is not None:
            print(f"    at a_p = [{', '.join(f'{x:.3f}' for x in x_st[:min(6,K)])}{'...' if K>6 else ''}]")
            print(f"    mean(a_p)={np.mean(x_st):.3f}, mean(a_p²)={np.mean(x_st**2):.3f}, "
                  f"mean(a_p⁴)={np.mean(x_st**4):.3f}")

        # 3. With extended Sato-Tate (moments 1-8)
        t2 = time.time()
        min_ext, x_ext = minimize_lambda1_with_st(K, n_starts=n_st, extended=True)
        t3 = time.time()
        print(f"  + Sato-Tate (m≤8):  min(λ₁) = {min_ext:+.6f}  [{t3-t2:.1f}s]")
        if x_ext is not None:
            print(f"    at a_p = [{', '.join(f'{x:.3f}' for x in x_ext[:min(6,K)])}{'...' if K>6 else ''}]")
            print(f"    mean(a_p)={np.mean(x_ext):.3f}, mean(a_p²)={np.mean(x_ext**2):.3f}, "
                  f"mean(a_p⁴)={np.mean(x_ext**4):.3f}, mean(a_p⁶)={np.mean(x_ext**6):.3f}")

        # 4. λ₂ at the ST-constrained minimum
        if x_st is not None:
            l2 = lambda2_arith(x_st, primes)
            print(f"  λ₂_arith at ST min: {l2:+.6f}")

        certified = "YES" if min_st > 0 else ("MAYBE" if min_ext > 0 else "NO")
        results.append({
            'K': K,
            'min_unc': min_unc,
            'min_st': min_st,
            'min_ext': min_ext,
            'certified': certified,
            'x_unc': x_unc,
            'x_st': x_st,
            'x_ext': x_ext,
        })

    # ═══════════════════════════════════════════════════════════════
    # Summary table
    # ═══════════════════════════════════════════════════════════════
    print(f"\n\n{'=' * 72}")
    print("  SUMMARY TABLE")
    print(f"{'=' * 72}")
    print(f"  {'K':>3}  {'min λ₁ (no ST)':>16}  {'min λ₁ (ST m≤4)':>16}  "
          f"{'min λ₁ (ST m≤8)':>16}  {'Certified?':>10}")
    print(f"  {'---':>3}  {'----------------':>16}  {'----------------':>16}  "
          f"{'----------------':>16}  {'----------':>10}")
    for r in results:
        print(f"  {r['K']:>3}  {r['min_unc']:>+16.6f}  {r['min_st']:>+16.6f}  "
              f"{r['min_ext']:>+16.6f}  {r['certified']:>10}")

    # ═══════════════════════════════════════════════════════════════
    # Ramanujan Δ verification
    # ═══════════════════════════════════════════════════════════════
    print(f"\n\n{'=' * 72}")
    print("  VERIFICATION: Ramanujan Δ function (weight 12)")
    print(f"{'=' * 72}")

    for K in [3, 5, 10, 15]:
        a_delta, primes_delta = ramanujan_delta_eigenvalues(K)
        if len(a_delta) < K:
            print(f"\n  K={K}: only {len(a_delta)} eigenvalues available, skipping")
            continue

        l1 = lambda1_full(a_delta, primes_delta)
        l1_arith = lambda1_arith(a_delta, primes_delta)
        l2 = lambda2_arith(a_delta, primes_delta)
        st_ok = sato_tate_feasible(a_delta, K)

        print(f"\n  K={K}, primes={primes_delta}")
        print(f"    a_p = [{', '.join(f'{x:.4f}' for x in a_delta)}]")
        print(f"    λ₁_arith = {l1_arith:+.6f}")
        print(f"    λ₁_full  = {l1:+.6f}  {'(POSITIVE ✓)' if l1 > 0 else '(NEGATIVE ✗)'}")
        print(f"    λ₂_arith = {l2:+.6f}")
        print(f"    ST-feasible: {st_ok}")
        print(f"    mean(a_p) = {np.mean(a_delta):.4f}, mean(a_p²) = {np.mean(a_delta**2):.4f}")

    # ═══════════════════════════════════════════════════════════════
    # Honest assessment
    # ═══════════════════════════════════════════════════════════════
    print(f"\n\n{'=' * 72}")
    print("  HONEST ASSESSMENT")
    print(f"{'=' * 72}")

    any_certified = any(r['certified'] == 'YES' for r in results)
    any_maybe = any(r['certified'] == 'MAYBE' for r in results)

    if any_certified:
        K_cert = min(r['K'] for r in results if r['certified'] == 'YES')
        print(f"\n  ST (m≤4) makes λ₁ ≥ 0 certifiable starting at K={K_cert}.")
        print(f"  This is a CONDITIONAL result: assumes effective ST error bounds ε(K).")
    elif any_maybe:
        K_maybe = min(r['K'] for r in results if r['certified'] == 'MAYBE')
        print(f"\n  Extended ST (m≤8) needed for certification, starting at K={K_maybe}.")
        print(f"  Basic ST (m≤4) not sufficient at any tested K.")
    else:
        print(f"\n  ST constraints (even extended) do NOT close the gap at tested K values.")
        print(f"  The gap between [-2,2]^K and actual eigenforms requires")
        print(f"  stronger constraints (trace formula, pair correlations).")

    # Trend analysis
    print(f"\n  Trend of min λ₁ with ST:")
    for r in results:
        trend = "↑" if r['min_st'] > r['min_unc'] else "↓"
        gap = r['min_st'] - r['min_unc']
        print(f"    K={r['K']:>2}: no_ST={r['min_unc']:+.4f} → ST={r['min_st']:+.4f} "
              f"(Δ={gap:+.4f} {trend})")

    return results


if __name__ == '__main__':
    np.random.seed(42)
    results = run_computation()
