"""R56 -- Estimate (a): Uniform H1 bounds for ALL eigenvectors of QW_lambda^{N,+}.

For each eigenvector phi_k of QW_lambda^{N,+} (the even-sector matrix):
  (a) Compute the H1 norm: ||phi_k||_{H1} = sqrt(sum (1+j^2)|phi_k(j)|^2)
  (b) Fit the Fourier coefficient decay: |phi_k(j)| ~ C_k * rho_k^{-|j|}
  (c) Check: does ||phi_k||_{H1} grow polynomially in k?

If yes: discrete compactness follows for ALL resolvent images, not just ground state.

CLI:  python r56_all_eigvecs_h1.py
"""

import json
import os
import sys
import time
import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import build_QW, eigh_mp
from r51b_evenblock import project_to_even, even_eigvec_to_full


def compute_h1_norm(coeffs_ev, N):
    """Compute ||phi||_{H1} = sqrt(sum_{j=0}^{N} (1+j^2)|c_j|^2)
    for an even-sector eigenvector with cosine-basis coefficients c_j."""
    s = mp.mpf(0)
    for j in range(N + 1):
        s += (1 + j * j) * coeffs_ev[j] ** 2
    return mp.sqrt(s)


def compute_l2_norm(coeffs_ev, N):
    """Compute ||phi||_{L2} = sqrt(sum |c_j|^2)."""
    s = mp.mpf(0)
    for j in range(N + 1):
        s += coeffs_ev[j] ** 2
    return mp.sqrt(s)


def fit_exponential_decay(coeffs_ev, N):
    """Fit |c_j| ~ C * rho^{-j} for j >= 1 using least squares on log|c_j| vs j.
    Returns (C, rho, r_squared)."""
    # Collect points where |c_j| > 0
    pts = []
    for j in range(1, N + 1):
        v = abs(coeffs_ev[j])
        if v > mp.mpf("1e-300"):
            pts.append((j, float(mp.log(v))))
    if len(pts) < 3:
        return (None, None, None)

    n = len(pts)
    sx = sum(x for x, y in pts)
    sy = sum(y for x, y in pts)
    sxx = sum(x * x for x, y in pts)
    sxy = sum(x * y for x, y in pts)

    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return (None, None, None)

    slope = (n * sxy - sx * sy) / denom
    intercept = (sy - slope * sx) / n

    C = float(mp.exp(mp.mpf(intercept)))
    rho = float(mp.exp(mp.mpf(-slope)))  # |c_j| ~ C * rho^{-j}, so log|c_j| = log C - j log rho

    # R-squared
    y_mean = sy / n
    ss_tot = sum((y - y_mean) ** 2 for x, y in pts)
    ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in pts)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    return (C, rho, r2)


def analyze_all_eigenvectors(lam, N, dps=80, verbose=True):
    """Build QW^{N,+}, diagonalize, compute H1 norms for ALL eigenvectors."""
    mp.mp.dps = dps

    if verbose:
        print(f"\n{'='*72}")
        print(f"ALL EIGENVECTORS: lambda={lam}, N={N}, dps={dps}")
        print(f"{'='*72}")

    t0 = time.time()
    A, L = build_QW(lam, N, dps=dps, verbose=verbose)
    Aev = project_to_even(A, N)
    vals_ev, Q_ev = eigh_mp(Aev)
    t_build = time.time() - t0

    if verbose:
        print(f"  Built and diagonalized in {t_build:.1f}s")
        print(f"  Even sector dimension: {N+1}")
        print(f"  Eigenvalue range: [{mp.nstr(vals_ev[0], 10)}, {mp.nstr(vals_ev[-1], 10)}]")

    results = []
    for k in range(N + 1):
        # Extract eigenvector k (cosine basis coefficients)
        coeffs = [Q_ev[j, k] for j in range(N + 1)]

        # Normalize to L2 = 1
        l2 = compute_l2_norm(coeffs, N)
        if l2 > mp.mpf("1e-300"):
            coeffs_norm = [c / l2 for c in coeffs]
        else:
            coeffs_norm = coeffs

        # H1 norm
        h1 = compute_h1_norm(coeffs_norm, N)

        # Eigenvalue
        mu_k = vals_ev[k]

        # Spectral theorem bound: ||phi_k||_{H1}^2 <= 1 + mu_k^2
        # (only exact for the operator's OWN H1 norm, but gives a comparison)
        spectral_bound = float(mp.sqrt(1 + mu_k ** 2))

        # Fit exponential decay
        C_fit, rho_fit, r2_fit = fit_exponential_decay(coeffs_norm, N)

        row = {
            "k": k,
            "eigenvalue": float(mu_k),
            "h1_norm": float(h1),
            "l2_norm": float(l2),
            "spectral_bound": spectral_bound,
            "decay_C": C_fit,
            "decay_rho": rho_fit,
            "decay_r2": r2_fit,
        }
        results.append(row)

        if verbose and (k < 5 or k == N or k % max(1, (N+1)//10) == 0):
            print(f"  k={k:3d}  mu_k={float(mu_k):+12.4e}  "
                  f"||phi||_H1={float(h1):8.4f}  "
                  f"rho={rho_fit if rho_fit else '---':>8}  "
                  f"C={C_fit if C_fit else '---':>10}")

    return vals_ev, results


def analyze_h1_growth(results):
    """Analyze how H1 norms grow with k."""
    ks = [r["k"] for r in results]
    h1s = [r["h1_norm"] for r in results]
    mus = [abs(r["eigenvalue"]) for r in results]

    # Fit: H1(k) ~ a * k^alpha
    # log H1 = log a + alpha * log k (for k >= 1)
    pts = [(k, h) for k, h in zip(ks, h1s) if k >= 1 and h > 0]
    if len(pts) >= 3:
        log_ks = [float(mp.log(k)) for k, h in pts]
        log_h1s = [float(mp.log(h)) for k, h in pts]
        n = len(log_ks)
        mx = sum(log_ks) / n
        my = sum(log_h1s) / n
        sxx = sum((x - mx) ** 2 for x in log_ks)
        sxy = sum((log_ks[i] - mx) * (log_h1s[i] - my) for i in range(n))
        alpha = sxy / sxx if sxx > 0 else float("nan")
        log_a = my - alpha * mx
        a = float(mp.exp(mp.mpf(log_a)))
    else:
        alpha, a = None, None

    # Fit: H1(k) ~ b * mu_k (linear in eigenvalue)
    pts_mu = [(m, h) for m, h in zip(mus, h1s) if m > 0 and h > 0]
    if len(pts_mu) >= 2:
        slope_mu = sum(m * h for m, h in pts_mu) / sum(m * m for m, h in pts_mu)
    else:
        slope_mu = None

    # Max H1 norm
    max_h1 = max(h1s) if h1s else 0
    max_h1_k = ks[h1s.index(max_h1)] if h1s else -1

    # Eigenvalue growth: fit mu_k ~ c * k^beta
    pts_ev = [(k, abs(m)) for k, m in zip(ks, mus) if k >= 1 and m > 0]
    if len(pts_ev) >= 3:
        log_ks_ev = [float(mp.log(k)) for k, m in pts_ev]
        log_mus = [float(mp.log(m)) for k, m in pts_ev]
        n_ev = len(log_ks_ev)
        mx_ev = sum(log_ks_ev) / n_ev
        my_ev = sum(log_mus) / n_ev
        sxx_ev = sum((x - mx_ev) ** 2 for x in log_ks_ev)
        sxy_ev = sum((log_ks_ev[i] - mx_ev) * (log_mus[i] - my_ev) for i in range(n_ev))
        beta = sxy_ev / sxx_ev if sxx_ev > 0 else float("nan")
    else:
        beta = None

    return {
        "h1_growth_exponent_alpha": alpha,
        "h1_growth_prefactor_a": a,
        "h1_vs_eigenvalue_slope": slope_mu,
        "max_h1_norm": max_h1,
        "max_h1_at_k": max_h1_k,
        "eigenvalue_growth_exponent_beta": beta,
    }


def discrete_compactness_check(results, N):
    """Check whether the resolvent regularity sum converges.

    For z = i: sum_k |c_k|^2 * ||phi_k||_{H1}^2 / |mu_k - i|^2
    If this is bounded as N -> infinity, discrete compactness holds.
    """
    # For unit vector f = sum c_k phi_k with sum |c_k|^2 = 1,
    # worst case is c_k = delta_{k,K} for some K.
    # Then the resolvent H1 norm^2 = ||phi_K||_{H1}^2 / |mu_K - i|^2
    # = ||phi_K||_{H1}^2 / (mu_K^2 + 1)

    ratios = []
    for r in results:
        mu = r["eigenvalue"]
        h1 = r["h1_norm"]
        ratio = h1 ** 2 / (mu ** 2 + 1)
        ratios.append(ratio)

    max_ratio = max(ratios) if ratios else 0
    sum_ratio = sum(ratios)

    # For uniform f (c_k = 1/sqrt(N+1)):
    # sum = (1/(N+1)) * sum_k ||phi_k||_{H1}^2 / (mu_k^2 + 1)
    avg_ratio = sum_ratio / (N + 1) if N > 0 else 0

    return {
        "max_single_ratio": max_ratio,
        "sum_all_ratios": sum_ratio,
        "average_ratio": avg_ratio,
        "compactness_holds": max_ratio < 100,  # generous threshold
    }


def main():
    mp.mp.dps = 80

    print("R56 -- Estimate (a): H1 bounds for ALL eigenvectors")
    print("=" * 72)

    all_results = {}

    # Run at lambda = sqrt(14), N = 20 (the target case)
    for N in [5, 10, 15, 20]:
        lam = mp.sqrt(14)
        vals, results = analyze_all_eigenvectors(lam, N, dps=80)
        growth = analyze_h1_growth(results)
        compact = discrete_compactness_check(results, N)

        print(f"\n  --- H1 Growth Analysis (N={N}) ---")
        print(f"  H1 ~ a * k^alpha: alpha = {growth['h1_growth_exponent_alpha']}")
        print(f"                     a     = {growth['h1_growth_prefactor_a']}")
        print(f"  Eigenvalue ~ k^beta:      beta = {growth['eigenvalue_growth_exponent_beta']}")
        print(f"  Max H1 norm = {growth['max_h1_norm']:.4f} at k = {growth['max_h1_at_k']}")

        print(f"\n  --- Discrete Compactness Check (N={N}) ---")
        print(f"  Max single ratio ||phi_k||_H1^2/(mu_k^2+1) = {compact['max_single_ratio']:.6f}")
        print(f"  Sum all ratios = {compact['sum_all_ratios']:.6f}")
        print(f"  Average ratio = {compact['average_ratio']:.6f}")
        print(f"  Compactness holds? {compact['compactness_holds']}")

        all_results[f"N={N}"] = {
            "eigenvectors": results,
            "growth": growth,
            "compactness": compact,
        }

    # Cross-N analysis: does the max H1 ratio grow with N?
    print(f"\n{'='*72}")
    print("CROSS-N SUMMARY")
    print(f"{'='*72}")
    print(f"{'N':>4s}  {'max H1':>10s}  {'max k':>6s}  {'alpha':>8s}  {'beta':>8s}  "
          f"{'max ratio':>12s}  {'sum ratio':>12s}")
    for key in sorted(all_results.keys(), key=lambda x: int(x.split("=")[1])):
        N_val = int(key.split("=")[1])
        g = all_results[key]["growth"]
        c = all_results[key]["compactness"]
        print(f"{N_val:>4d}  {g['max_h1_norm']:>10.4f}  {g['max_h1_at_k']:>6d}  "
              f"{g['h1_growth_exponent_alpha']:>8.4f}  "
              f"{g['eigenvalue_growth_exponent_beta']:>8.4f}  "
              f"{c['max_single_ratio']:>12.6f}  {c['sum_all_ratios']:>12.4f}")

    # Save
    out_path = os.path.join(CODE_DIR, "r56_all_eigvecs_h1.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nJSON -> {out_path}")


if __name__ == "__main__":
    main()
