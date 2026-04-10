"""
SDP test: Can {Ramanujan bound + multiplicativity + zero at sigma_0+it_0}
be satisfied for sigma_0 > 1/2?

This is the simplest meaningful version:
- Variables: a_p for first K primes
- Extend to a_n via multiplicativity
- Ramanujan bound: |a_p| <= 2
- Zero condition: Re(L(s)) = 0 and Im(L(s)) = 0 at s = sigma_0 + i*t_0
- Scan sigma_0 from 0.5 to 1.0 to find the boundary

v1: No modular invariance yet — just multiplicativity + Ramanujan + zero.
This tests whether the Euler product ALONE constrains sigma_0.
"""

import numpy as np
from scipy.optimize import minimize, LinearConstraint, NonlinearConstraint

# --- Parameters ---
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
K = len(PRIMES)
N_MAX = 200  # extend coefficients up to this n

def prime_factorize(n, primes):
    """Return exponents of n in terms of the given primes, or None if n has a prime factor not in the list."""
    exps = []
    remaining = n
    for p in primes:
        e = 0
        while remaining % p == 0:
            remaining //= p
            e += 1
        exps.append(e)
    if remaining > 1:
        return None  # n has prime factors outside our list
    return exps

def extend_coefficients(a_p, primes, n_max):
    """Given a_p for each prime, extend to a_n via complete multiplicativity: a_{mn} = a_m * a_n."""
    a = np.zeros(n_max + 1)
    a[1] = 1.0  # a_1 = 1 always
    for n in range(2, n_max + 1):
        exps = prime_factorize(n, primes)
        if exps is None:
            a[n] = 0.0  # can't compute — treat as zero (truncation)
        else:
            val = 1.0
            for i, e in enumerate(exps):
                val *= a_p[i] ** e  # completely multiplicative
            a[n] = val
    return a

def L_value(a, s, n_max):
    """Compute L(s) = sum_{n=1}^{n_max} a_n / n^s."""
    ns = np.arange(1, n_max + 1, dtype=float)
    return np.sum(a[1:n_max+1] * ns**(-s))

def test_zero_feasibility(sigma_0, t_0, n_max=N_MAX, verbose=False):
    """
    Test: can we find {a_p} with |a_p| <= 2 such that L(sigma_0 + i*t_0) = 0?

    Minimize |L(s)|^2 subject to Ramanujan bound.
    If min |L(s)|^2 > 0: no zero possible at this (sigma_0, t_0).
    If min |L(s)|^2 ~ 0: zero is feasible.
    """
    s = sigma_0 + 1j * t_0

    def objective(a_p):
        a = extend_coefficients(a_p, PRIMES, n_max)
        Ls = L_value(a, s, n_max)
        return abs(Ls)**2

    # Try multiple random starts
    best_val = np.inf
    best_ap = None

    for trial in range(50):
        if trial == 0:
            a_p0 = np.ones(K)  # start with trivial character (a_p = 1)
        else:
            a_p0 = np.random.uniform(-2, 2, K)

        bounds = [(-2, 2)] * K  # Ramanujan bound

        result = minimize(objective, a_p0, method='L-BFGS-B', bounds=bounds,
                         options={'maxiter': 500, 'ftol': 1e-15})

        if result.fun < best_val:
            best_val = result.fun
            best_ap = result.x

    if verbose:
        print(f"  sigma_0={sigma_0:.3f}, t_0={t_0:.3f}: min|L(s)|^2 = {best_val:.2e}")
        if best_val < 1e-10:
            print(f"    -> FEASIBLE (zero found), a_p = {np.round(best_ap, 3)}")
        else:
            print(f"    -> INFEASIBLE (no zero possible)")

    return best_val, best_ap


def scan_sigma(t_0, sigma_range=np.arange(0.50, 1.01, 0.05)):
    """Scan sigma_0 values for a fixed t_0 to find where zeros become feasible."""
    print(f"\n{'='*60}")
    print(f"Scanning sigma_0 for t_0 = {t_0:.3f}")
    print(f"Primes: {PRIMES[:K]}, N_max: {N_MAX}")
    print(f"{'='*60}")

    results = []
    for sigma in sigma_range:
        val, ap = test_zero_feasibility(sigma, t_0, verbose=True)
        results.append((sigma, val))

    return results


def run_diagnostics():
    """Run the diagnostic suite."""

    print("=" * 60)
    print("RH SDP DIAGNOSTIC SUITE v1")
    print("=" * 60)

    # --- Run 0: Known zero of zeta ---
    # The first zero of zeta(s) is at s = 1/2 + i*14.1347...
    print("\n--- Run 0: First Riemann zero (sigma=0.5, t=14.1347) ---")
    print("Testing if a_p = 1 (trivial = zeta) gives |L(s)| ~ 0:")
    a_trivial = extend_coefficients(np.ones(K), PRIMES, N_MAX)
    s_zero = 0.5 + 1j * 14.134725
    Ls = L_value(a_trivial, s_zero, N_MAX)
    print(f"  L(1/2 + 14.135i) = {Ls:.6f}")
    print(f"  |L| = {abs(Ls):.6f}")
    print(f"  (Should be close to 0 for the first Riemann zero)")

    # --- Run 1: Can we find a zero ON the critical line? ---
    print("\n--- Run 1: Zero feasibility ON critical line (sigma=0.5) ---")
    for t0 in [14.135, 21.022, 25.011]:
        test_zero_feasibility(0.5, t0, verbose=True)

    # --- Run 2: Can we find a zero OFF the critical line? ---
    print("\n--- Run 2: Zero feasibility OFF critical line ---")
    print("Testing sigma_0 = 0.6, 0.7, 0.8, 0.9 at t_0 = 14.135:")
    for sigma in [0.55, 0.60, 0.70, 0.80, 0.90]:
        test_zero_feasibility(sigma, 14.135, verbose=True)

    # --- Run 3: Full sigma scan at first zero height ---
    print("\n--- Run 3: Full sigma scan at t_0 = 14.135 ---")
    scan_sigma(14.135, np.arange(0.50, 1.01, 0.05))

    # --- Run 4: Sigma scan at different t_0 ---
    print("\n--- Run 4: Sigma scan at t_0 = 21.022 ---")
    scan_sigma(21.022, np.arange(0.50, 1.01, 0.05))

    # --- Run 5: Effect of number of primes ---
    print("\n--- Run 5: Effect of K (number of primes) ---")
    for k in [3, 5, 8, 10, 15]:
        primes_k = PRIMES[:k]
        def obj_k(a_p, primes=primes_k):
            a = extend_coefficients(a_p, primes, N_MAX)
            Ls = L_value(a, 0.7 + 1j*14.135, N_MAX)
            return abs(Ls)**2
        best = np.inf
        for trial in range(30):
            a0 = np.ones(k) if trial == 0 else np.random.uniform(-2, 2, k)
            res = minimize(obj_k, a0, method='L-BFGS-B', bounds=[(-2,2)]*k, options={'maxiter':500, 'ftol':1e-15})
            if res.fun < best:
                best = res.fun
        print(f"  K={k:2d} primes: min|L(0.7+14.135i)|^2 = {best:.2e}")


if __name__ == "__main__":
    run_diagnostics()
