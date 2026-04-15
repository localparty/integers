"""
SDP v4: Paired-zero test using the Approximate Functional Equation.

The AFE for a Dirichlet L-function L(s) = Σ a_n n^{-s} is:

  L(s) = Σ_{n≤X} a_n n^{-s} V(n/X) + ε χ(s) Σ_{n≤Y} ā_n n^{-(1-s)} V(n/Y) + R

where XY = |t|/(2π), V is a smooth cutoff, and R = O(e^{-c√N}).

Key advantage: the functional equation is BUILT IN.
If L(s) = 0 at s = σ+it, the AFE constrains both the s-sum and
the (1-s)-sum simultaneously — with the SAME coefficients.

For completely multiplicative a_n with |a_p| ≤ 2 (Ramanujan),
we test: can the AFE expression vanish at σ+it for σ ≠ 1/2?
"""

import numpy as np
from scipy.special import gamma as Gamma
from scipy.optimize import minimize

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
K = len(PRIMES)


def prime_factorize(n, primes):
    exps = []
    r = n
    for p in primes:
        e = 0
        while r % p == 0:
            r //= p
            e += 1
        exps.append(e)
    return exps if r == 1 else None


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


def chi_factor(s):
    """The chi factor: χ(s) = π^{s-1/2} Γ((1-s)/2) / Γ(s/2)"""
    try:
        return np.pi**(s - 0.5) * Gamma((1.0 - s) / 2.0) / Gamma(s / 2.0)
    except (ValueError, ZeroDivisionError):
        return np.inf


def smooth_cutoff(u, method='erfc'):
    """Smooth cutoff V(u) for the AFE. V(0)=1, V(∞)=0."""
    if method == 'sharp':
        return 1.0 if u <= 1.0 else 0.0
    elif method == 'erfc':
        # Smooth Gaussian-type cutoff
        from scipy.special import erfc
        return 0.5 * erfc(2.0 * (u - 1.0))
    elif method == 'exp':
        # Exponential cutoff
        if u <= 0.5:
            return 1.0
        elif u >= 2.0:
            return 0.0
        else:
            return np.exp(-((u - 0.5) / (2.0 - u))**2)


def L_afe(a, s, X, epsilon=1.0):
    """
    Compute L(s) via the Approximate Functional Equation:

    L(s) = Σ_{n≤2X} a_n n^{-s} V(n/X) + ε χ(s) Σ_{n≤2Y} a_n n^{-(1-s)} V(n/Y)

    where XY = |Im(s)|/(2π), ε = root number (1 for real coefficients).
    """
    t = abs(s.imag)
    if t < 1.0:
        t = 1.0  # avoid division by zero

    Y = t / (2.0 * np.pi * X) if X > 0 else X

    N_max = len(a) - 1

    # First sum: Σ a_n n^{-s} V(n/X)
    sum1 = 0.0
    for n in range(1, min(int(2*X) + 1, N_max + 1)):
        V = smooth_cutoff(n / X, 'erfc')
        sum1 += a[n] * n**(-s) * V

    # Second sum: ε χ(s) Σ a_n n^{-(1-s)} V(n/Y)
    chi_s = chi_factor(s)
    sum2 = 0.0
    for n in range(1, min(int(2*Y) + 1, N_max + 1)):
        V = smooth_cutoff(n / Y, 'erfc')
        sum2 += a[n] * n**(-(1.0 - s)) * V

    return sum1 + epsilon * chi_s * sum2


def test_afe_zero(sigma_0, t_0, n_trials=80, n_max=500):
    """
    Test: can multiplicative Ramanujan-bounded a_p make L_AFE(σ₀+it₀) = 0?

    The AFE has the functional equation BUILT IN, so this automatically
    tests the paired-zero condition.
    """
    s = sigma_0 + 1j * t_0
    X = np.sqrt(t_0 / (2.0 * np.pi))  # symmetric choice X = Y = √(t/2π)

    def objective(a_p):
        a = extend_coefficients(a_p, PRIMES, n_max)
        Ls = L_afe(a, s, X)
        return abs(Ls)**2

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


def run_diagnostics():
    print("=" * 70)
    print("RH SDP v4: APPROXIMATE FUNCTIONAL EQUATION")
    print("=" * 70)
    print(f"K = {K} primes: {PRIMES}")
    print(f"AFE with smooth (erfc) cutoff, symmetric X = Y = √(t/2π)")
    print()

    # --- Sanity: Check AFE accuracy for ζ(s) at known zeros ---
    print("--- Sanity: AFE for ζ(s) at known zeros ---")
    a_trivial = extend_coefficients(np.ones(K), PRIMES, 500)
    for t0 in [14.1347, 21.0220, 25.0109]:
        s = 0.5 + 1j * t0
        X = np.sqrt(t0 / (2 * np.pi))
        Ls = L_afe(a_trivial, s, X)
        print(f"  ζ_AFE(0.5 + {t0:.4f}i) = {Ls:.6f},  |ζ| = {abs(Ls):.6f}")

    # --- v2 comparison: raw vs AFE ---
    print()
    print("--- Paired-zero test: AFE vs raw Dirichlet series ---")
    print("  (AFE has functional equation built in)")
    print()

    for t0 in [14.1347]:
        print(f"  t_0 = {t0}")
        for sigma in [0.500, 0.510, 0.520, 0.530, 0.540, 0.550,
                      0.600, 0.650, 0.700, 0.800, 0.900]:
            val, ap = test_afe_zero(sigma, t0)
            tag = "FEASIBLE" if val < 1e-6 else ("MARGINAL" if val < 1e-3 else "INFEASIBLE")
            print(f"    σ={sigma:.3f}: min|L_AFE|² = {val:.3e}  {tag}")

    # --- Fine grid near 0.5 ---
    print()
    print("--- Fine grid near critical line (t_0 = 14.1347) ---")
    for sigma in np.arange(0.500, 0.560, 0.005):
        val, ap = test_afe_zero(sigma, 14.1347)
        tag = "FEASIBLE" if val < 1e-6 else ("MARGINAL" if val < 1e-3 else "INFEASIBLE")
        print(f"    σ={sigma:.3f}: min|L_AFE|² = {val:.3e}  {tag}")

    # --- Different heights ---
    print()
    print("--- Different heights at σ=0.55 ---")
    for t0 in [14.1347, 21.022, 25.011, 30.425, 40.0, 50.0]:
        val, ap = test_afe_zero(0.55, t0)
        tag = "FEASIBLE" if val < 1e-6 else ("MARGINAL" if val < 1e-3 else "INFEASIBLE")
        print(f"    t_0={t0:7.3f}, σ=0.55: min|L_AFE|² = {val:.3e}  {tag}")

    # --- Convergence with K ---
    print()
    print("--- Convergence: infeasibility vs number of primes (σ=0.6, t=14.135) ---")
    for k in [3, 5, 8, 10, 15]:
        primes_k = PRIMES[:k]
        s = 0.6 + 1j * 14.1347
        X = np.sqrt(14.1347 / (2 * np.pi))
        best = np.inf
        for trial in range(60):
            a0 = np.ones(k) if trial == 0 else np.random.uniform(-2, 2, k)
            def obj(ap, primes=primes_k, nm=300):
                a = extend_coefficients(ap, primes, nm)
                return abs(L_afe(a, s, X))**2
            r = minimize(obj, a0, method='L-BFGS-B', bounds=[(-2,2)]*k,
                        options={'maxiter':500, 'ftol':1e-16})
            if r.fun < best: best = r.fun
        tag = "FEASIBLE" if best < 1e-6 else "INFEASIBLE"
        print(f"    K={k:2d}: min|L_AFE|² = {best:.3e}  {tag}")


if __name__ == "__main__":
    run_diagnostics()
