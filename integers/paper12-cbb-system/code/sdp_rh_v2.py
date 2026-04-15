"""
SDP v2: Add functional equation constraint.

v1 showed: Ramanujan + multiplicativity alone allow off-line zeros.
v2 adds: The functional equation L(s) = chi(s) * L(1-s), which is
the MODULAR INVARIANCE constraint in analytic form.

For a Dirichlet L-function L(s, chi) with conductor q:
  Lambda(s) = (q/pi)^{s/2} Gamma((s+a)/2) L(s) = epsilon * Lambda(1-s)

where a = 0 (even) or 1 (odd), epsilon = root number (|epsilon| = 1).

The functional equation constrains: if L(sigma + it) = 0, then
L(1-sigma + it) must also relate through chi(s). For a zero at
sigma_0 + it_0 with sigma_0 != 1/2, there must be a PAIRED zero
at (1-sigma_0) + it_0.

Strategy: search for a_p satisfying:
1. Ramanujan: |a_p| <= 2
2. Multiplicativity: a_{mn} = a_m * a_n
3. Simultaneous zeros: L(sigma_0 + it_0) = 0 AND L(1-sigma_0 + it_0) = 0
4. The a_n must be consistent between the two zeros (same L-function)

If no a_p can satisfy all four: zeros must be on the line.
"""

import numpy as np
from scipy.optimize import minimize

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
K = len(PRIMES)
N_MAX = 300

def prime_factorize(n, primes):
    exps = []
    remaining = n
    for p in primes:
        e = 0
        while remaining % p == 0:
            remaining //= p
            e += 1
        exps.append(e)
    if remaining > 1:
        return None
    return exps

def extend_coefficients(a_p, primes, n_max):
    a = np.zeros(n_max + 1)
    a[1] = 1.0
    for n in range(2, n_max + 1):
        exps = prime_factorize(n, primes)
        if exps is None:
            a[n] = 0.0
        else:
            val = 1.0
            for i, e in enumerate(exps):
                val *= a_p[i] ** e
            a[n] = val
    return a

def L_value(a, s, n_max):
    ns = np.arange(1, n_max + 1, dtype=float)
    return np.sum(a[1:n_max+1] * ns**(-s))


def test_paired_zeros(sigma_0, t_0, n_max=N_MAX, n_trials=100):
    """
    Test: can we find {a_p} with |a_p| <= 2 such that BOTH:
      L(sigma_0 + it_0) = 0  AND  L(1 - sigma_0 + it_0) = 0 ?

    The functional equation requires zeros to come in pairs
    symmetric about Re(s) = 1/2. If sigma_0 != 1/2, we need
    BOTH to vanish simultaneously with the SAME coefficients.
    """
    s1 = sigma_0 + 1j * t_0
    s2 = (1.0 - sigma_0) + 1j * t_0

    def objective(a_p):
        a = extend_coefficients(a_p, PRIMES, n_max)
        L1 = L_value(a, s1, n_max)
        L2 = L_value(a, s2, n_max)
        # Must vanish at BOTH points
        return abs(L1)**2 + abs(L2)**2

    best_val = np.inf
    best_ap = None

    for trial in range(n_trials):
        if trial == 0:
            a_p0 = np.ones(K)
        elif trial == 1:
            a_p0 = -np.ones(K)
        else:
            a_p0 = np.random.uniform(-2, 2, K)

        bounds = [(-2, 2)] * K
        result = minimize(objective, a_p0, method='L-BFGS-B', bounds=bounds,
                         options={'maxiter': 1000, 'ftol': 1e-16})

        if result.fun < best_val:
            best_val = result.fun
            best_ap = result.x

    return best_val, best_ap


def run_paired_diagnostics():
    print("=" * 70)
    print("RH SDP v2: PAIRED ZEROS (Functional Equation Constraint)")
    print("=" * 70)
    print(f"Primes: {PRIMES[:K]}, K={K}, N_max={N_MAX}")
    print()

    # --- Test: sigma_0 = 0.5 (on line: s1 = s2, trivially paired) ---
    print("--- sigma_0 = 0.5 (ON critical line) ---")
    print("Here s1 = s2, so only ONE zero needed (trivially paired).")
    for t0 in [14.135, 21.022, 25.011]:
        val, ap = test_paired_zeros(0.5, t0)
        status = "FEASIBLE" if val < 1e-8 else "INFEASIBLE"
        print(f"  t_0={t0:.3f}: min(|L(s1)|^2 + |L(s2)|^2) = {val:.2e} -> {status}")

    # --- Test: sigma_0 != 0.5 (off line: need TWO simultaneous zeros) ---
    print()
    print("--- sigma_0 != 0.5 (OFF critical line, need PAIRED zeros) ---")
    for sigma in [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.90]:
        for t0 in [14.135, 21.022]:
            val, ap = test_paired_zeros(sigma, t0)
            status = "FEASIBLE" if val < 1e-8 else "INFEASIBLE"
            marker = " ***" if val >= 1e-8 else ""
            print(f"  sigma_0={sigma:.2f}, t_0={t0:.3f}: min = {val:.2e} -> {status}{marker}")

    # --- Boundary scan: find the critical sigma_0 ---
    print()
    print("--- Boundary scan: finest resolution near sigma_0 = 0.5 ---")
    for sigma in np.arange(0.50, 0.62, 0.01):
        val, ap = test_paired_zeros(sigma, 14.135, n_trials=200)
        status = "FEASIBLE" if val < 1e-8 else "INFEASIBLE"
        marker = " <-- BOUNDARY?" if 1e-8 > val > 1e-4 else ""
        if val >= 1e-8:
            marker = " ***"
        print(f"  sigma_0={sigma:.3f}: min = {val:.2e} -> {status}{marker}")


if __name__ == "__main__":
    run_paired_diagnostics()
