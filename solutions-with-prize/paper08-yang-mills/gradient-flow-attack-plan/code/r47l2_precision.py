"""R47 Lead 2 -- precision push on the Q_W spectrum matches to gamma_n.

Strategy:
  - Reuse r43_hermite_basis.build_QW_hermite with high quadrature
    resolution (n_per_sigma up to 80, pad_sigma up to 8).
  - For each target gamma_n, locate the closest eigenvalue of the even
    Q_W, then apply inverse-iteration (Rayleigh-quotient) refinement
    to push precision past the raw eigh() result.
  - Sweep N_basis, sigma/L, and lambda.
  - Track convergence rate in N_basis for gamma_{1,2,3}.

Output:
  code/r47l2_precision.json

The Gauss-Hermite route was abandoned: at Nq >> Nb the w_i * exp(x_i^2)
weights overflow, and the band-limited cosh kernel prevents a clean
factorization. The grid builder with fine n_per_sigma gives identical
spectral precision at acceptable cost for Nb <= 1200, and the dominant
source of residual error at the eigh() output is float64 arithmetic in
the dense diagonaliser, which Rayleigh refinement bypasses.
"""

import json
import os
import sys
import time
import numpy as np
from math import log, sqrt, pi, exp

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r43_hermite_basis import build_QW_hermite, primes_up_to

# Higher-precision Riemann zeros (Odlyzko).
GAMMAS = [14.134725141734693790,
          21.022039638771554993,
          25.010857580145688763,
          30.424876125859513210,
          32.935061587739189691]


def even_spectrum(Q, N_basis):
    even_idx = np.arange(0, N_basis, 2)
    Qe = Q[np.ix_(even_idx, even_idx)]
    Qe = 0.5 * (Qe + Qe.T)
    vals, vecs = np.linalg.eigh(Qe)
    return vals, vecs, Qe


def rayleigh_refine(Qe, mu0, v0, n_iter=3):
    """Inverse iteration to refine eigen-pair (mu0, v0). Returns (mu, v, hist)."""
    n = Qe.shape[0]
    mu = float(mu0)
    v = v0 / np.linalg.norm(v0)
    I = np.eye(n)
    hist = [mu]
    for _ in range(n_iter):
        try:
            w = np.linalg.solve(Qe - mu * I, v)
        except np.linalg.LinAlgError:
            break
        w /= np.linalg.norm(w)
        mu_new = float(w @ (Qe @ w))
        v = w
        hist.append(mu_new)
        if abs(mu_new - mu) < 1e-16 * (abs(mu) + 1):
            mu = mu_new
            break
        mu = mu_new
    return mu, v, hist


def closest_idx(vals, target):
    return int(np.argmin(np.abs(vals - target)))


def measure(lam, Nb, sigma_factor, primes, targets, n_per_sigma=40,
            pad_sigma=6.0, refine=True):
    L = 2.0 * log(lam)
    sigma = sigma_factor * L
    t0 = time.time()
    Q, _, _, _, _ = build_QW_hermite(lam, sigma, Nb, primes,
                                      n_per_sigma=n_per_sigma,
                                      pad_sigma=pad_sigma)
    vals, vecs, Qe = even_spectrum(Q, Nb)
    out = {"lam": lam, "L": L, "sigma": sigma, "sigma_over_L": sigma_factor,
           "N_basis": Nb, "n_per_sigma": n_per_sigma, "pad_sigma": pad_sigma,
           "n_even": int(len(vals)),
           "targets": {}}
    for name, tgt in targets.items():
        k = closest_idx(vals, tgt)
        mu_raw = float(vals[k])
        if refine:
            mu_ref, _, hist = rayleigh_refine(Qe, mu_raw, vecs[:, k], n_iter=3)
        else:
            mu_ref, hist = mu_raw, [mu_raw]
        err_raw = abs(mu_raw - tgt)
        err_ref = abs(mu_ref - tgt)
        rel_raw = err_raw / abs(tgt)
        rel_ref = err_ref / abs(tgt)
        out["targets"][name] = {
            "target": tgt, "idx": k,
            "mu_raw": mu_raw, "mu_refined": mu_ref,
            "abs_err_raw": err_raw, "rel_err_raw": rel_raw,
            "abs_err_refined": err_ref, "rel_err_refined": rel_ref,
            "refine_hist": hist,
        }
    out["mu_min"] = float(vals[0])
    out["mu_max"] = float(vals[-1])
    out["t_s"] = time.time() - t0
    return out


def primes_cc6():
    return primes_up_to(20)[:6]


def part2_convergence(lam=68.63, sigma_factor=0.25, n_per_sigma=40,
                      Nb_list=(200, 400, 600, 800, 1000, 1200)):
    primes = primes_cc6()
    targets = {"g1": GAMMAS[0], "g2": GAMMAS[1], "g3": GAMMAS[2]}
    print(f"\n[PART 2] lam={lam} sigma/L={sigma_factor} primes={primes} nps={n_per_sigma}")
    rows = []
    for Nb in Nb_list:
        rec = measure(lam, Nb, sigma_factor, primes, targets,
                      n_per_sigma=n_per_sigma, pad_sigma=6.0)
        rows.append(rec)
        t = rec["targets"]
        print(f"  Nb={Nb:4d}  "
              f"g1 raw={t['g1']['rel_err_raw']:.3e} ref={t['g1']['rel_err_refined']:.3e}  "
              f"g2 raw={t['g2']['rel_err_raw']:.3e} ref={t['g2']['rel_err_refined']:.3e}  "
              f"g3 raw={t['g3']['rel_err_raw']:.3e} ref={t['g3']['rel_err_refined']:.3e}  "
              f"[{rec['t_s']:.1f}s]")
    return rows


def part3_sigma_sweep(lam=68.63, Nb=800, n_per_sigma=40,
                      sigma_factors=(0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50)):
    primes = primes_cc6()
    targets = {"g1": GAMMAS[0]}
    print(f"\n[PART 3] sigma sweep  lam={lam}  Nb={Nb}")
    rows = []
    for f in sigma_factors:
        rec = measure(lam, Nb, f, primes, targets,
                      n_per_sigma=n_per_sigma, pad_sigma=6.0)
        rows.append(rec)
        t = rec["targets"]
        print(f"  sigma/L={f:.2f}  "
              f"g1 raw={t['g1']['rel_err_raw']:.3e} ref={t['g1']['rel_err_refined']:.3e}  "
              f"mu={t['g1']['mu_refined']:.10f}  [{rec['t_s']:.1f}s]")
    return rows


def part4_lambda_scan(lam_list=(40.0, 100.0, 200.0), Nb=800,
                      sigma_factor=0.25, n_per_sigma=40):
    targets = {"g1": GAMMAS[0], "g2": GAMMAS[1]}
    out = {}
    for lam in lam_list:
        L = 2.0 * log(lam)
        p_limit = int(exp(L)) + 1
        full = [p for p in primes_up_to(p_limit) if log(p) <= L]
        primes = full[:6]
        print(f"\n[PART 4] lam={lam}  primes={primes}")
        rec = measure(lam, Nb, sigma_factor, primes, targets,
                      n_per_sigma=n_per_sigma, pad_sigma=6.0)
        out[str(lam)] = rec
        t = rec["targets"]
        print(f"  g1 ref={t['g1']['rel_err_refined']:.3e}  "
              f"g2 ref={t['g2']['rel_err_refined']:.3e}  "
              f"[{rec['t_s']:.1f}s]")
    return out


def part5_mu1_trajectory(lam=68.63, sigma_factor=0.25, n_per_sigma=40,
                         Nb_list=(200, 400, 600, 800, 1000, 1200)):
    """Track mu_1 (the smallest even eigenvalue) across N_basis at the
    same parameters as Part 2. Compared to gamma_1 convergence, mu_1
    should drift (band-edge artifact per R46)."""
    primes = primes_cc6()
    print(f"\n[PART 5] mu_1 vs N_basis stability")
    rows = []
    for Nb in Nb_list:
        L = 2.0 * log(lam)
        sigma = sigma_factor * L
        Q, _, _, _, _ = build_QW_hermite(lam, sigma, Nb, primes,
                                          n_per_sigma=n_per_sigma,
                                          pad_sigma=6.0)
        vals, _, _ = even_spectrum(Q, Nb)
        rows.append({"N_basis": Nb, "mu_min": float(vals[0]),
                     "mu_2nd": float(vals[1]),
                     "mu_3rd": float(vals[2])})
        print(f"  Nb={Nb:4d}  mu_1={vals[0]:+.6f}  mu_2={vals[1]:+.6f}  mu_3={vals[2]:+.6f}")
    return rows


def main():
    report = {}
    print("=" * 72); print("R47 Lead 2 -- precision push"); print("=" * 72)

    # Part 2: convergence
    report["part2"] = part2_convergence(
        Nb_list=(200, 400, 600, 800, 1000, 1200),
        n_per_sigma=40)

    # Part 3: sigma sweep
    report["part3"] = part3_sigma_sweep(Nb=800, n_per_sigma=40)

    # Part 4: lambda cross-check
    report["part4"] = part4_lambda_scan(
        lam_list=(40.0, 100.0, 200.0), Nb=800, n_per_sigma=40)

    # Part 5: mu_1 trajectory
    report["part5"] = part5_mu1_trajectory(
        Nb_list=(200, 400, 600, 800, 1000, 1200), n_per_sigma=40)

    out_path = os.path.join(CODE, "r47l2_precision.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nSaved -> {out_path}")
    return report


if __name__ == "__main__":
    main()
