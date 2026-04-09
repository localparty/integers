"""R44: Pin down the N_basis -> infinity limit of mu_1 in the Hermite basis.

R43 (research/97-r43-hermite-basis.md) found that mu_1 in the Hermite-basis
Connes-Consani builder sits near -200 at (lam=68.63, N_primes=11) and
descends LOG-LIKE in N_basis up to N_basis=320, with a plausible finite
limit ~ -210.

R44 pushes the test much harder:
  1) push N_basis up to 1500-2000 at fixed (lam, N_primes=11, sigma=L/4)
  2) fit four candidate trajectories (1/N, 1/log N, N^-alpha, -log N)
  3) cross-sigma stability at large N_basis
  4) N_primes scaling at large fixed N_basis
  5) joint diagonal limit (N_basis = 10 * N_primes)
  6) the key diagnostic: at largest tractable, is mu_1 bounded away from 0?

Reuses code/r43_hermite_basis.py.
"""

import json
import os
import sys
import time
import numpy as np
from math import log, sqrt

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r43_hermite_basis import (
    build_QW_hermite,
    even_eigs_hermite,
    primes_up_to,
)


def mu12(lam, sigma, Nb, primes, n_per_sigma=30, pad_sigma=5.0):
    Q, _, _, _, _ = build_QW_hermite(
        lam, sigma, Nb, primes, n_per_sigma=n_per_sigma, pad_sigma=pad_sigma
    )
    vals, _, _ = even_eigs_hermite(Q, Nb)
    mu1 = float(vals[0]) if len(vals) else float("nan")
    mu2 = float(vals[1]) if len(vals) > 1 else float("nan")
    return mu1, mu2


# ----------------------------------------------------------------------
# Fits
# ----------------------------------------------------------------------

def fit_inv_N(Ns, mus):
    # mu = a + b/N
    x = 1.0 / np.asarray(Ns, dtype=float)
    y = np.asarray(mus, dtype=float)
    A = np.vstack([np.ones_like(x), x]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    a, b = sol
    pred = A @ sol
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    return {"form": "a + b/N", "a": float(a), "b": float(b),
            "limit": float(a), "rmse": rmse}


def fit_inv_log(Ns, mus):
    # mu = a + b/log(N)
    x = 1.0 / np.log(np.asarray(Ns, dtype=float))
    y = np.asarray(mus, dtype=float)
    A = np.vstack([np.ones_like(x), x]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    a, b = sol
    pred = A @ sol
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    return {"form": "a + b/log(N)", "a": float(a), "b": float(b),
            "limit": float(a), "rmse": rmse}


def fit_power(Ns, mus):
    # mu = a + b * N^(-alpha); nonlinear in alpha. Grid search alpha then linear fit.
    Ns = np.asarray(Ns, dtype=float)
    y = np.asarray(mus, dtype=float)
    best = None
    for alpha in np.linspace(0.05, 2.0, 196):
        x = Ns ** (-alpha)
        A = np.vstack([np.ones_like(x), x]).T
        sol, *_ = np.linalg.lstsq(A, y, rcond=None)
        pred = A @ sol
        rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
        if best is None or rmse < best["rmse"]:
            best = {"form": "a + b*N^(-alpha)", "a": float(sol[0]),
                    "b": float(sol[1]), "alpha": float(alpha),
                    "limit": float(sol[0]), "rmse": rmse}
    return best


def fit_neg_log(Ns, mus):
    # mu = a - b * log(N) (slow divergence)
    x = np.log(np.asarray(Ns, dtype=float))
    y = np.asarray(mus, dtype=float)
    A = np.vstack([np.ones_like(x), x]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    a, b = sol
    pred = A @ sol
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    return {"form": "a + b*log(N)", "a": float(a), "b": float(b),
            "limit": (float("-inf") if b < 0 else float("+inf")),
            "slope": float(b), "rmse": rmse}


def all_fits(Ns, mus):
    return {
        "inv_N": fit_inv_N(Ns, mus),
        "inv_log": fit_inv_log(Ns, mus),
        "power": fit_power(Ns, mus),
        "neg_log": fit_neg_log(Ns, mus),
    }


# ----------------------------------------------------------------------
# Tasks
# ----------------------------------------------------------------------

def task_Nbasis_push(lam=68.63, N_primes=11, Nb_list=None, sigma=None):
    if sigma is None:
        sigma = 2.0 * log(lam) / 4.0
    if Nb_list is None:
        Nb_list = [80, 120, 200, 300, 400, 600, 800, 1000, 1500]
    primes = primes_up_to(2000)[:N_primes]
    rows = []
    for Nb in Nb_list:
        t0 = time.time()
        try:
            mu1, mu2 = mu12(lam, sigma, Nb, primes)
            row = {"N_basis": Nb, "mu1": mu1, "mu2": mu2,
                   "gap": mu2 - mu1, "t": time.time() - t0}
        except Exception as e:
            row = {"N_basis": Nb, "error": str(e), "t": time.time() - t0}
        rows.append(row)
        if "mu1" in row:
            print(f"  [push] lam={lam} Nb={Nb:5d}  mu1={row['mu1']:+.4f}  "
                  f"mu2={row['mu2']:+.4f}  gap={row['gap']:.3f}  "
                  f"[{row['t']:.1f}s]")
        else:
            print(f"  [push] Nb={Nb:5d}  ERROR: {row['error']}")
    return {"lam": lam, "sigma": sigma, "N_primes": N_primes, "rows": rows}


def task_sigma_stability(lam=68.63, Nb=600, N_primes=11,
                         sigma_factors=(0.15, 0.25, 0.35, 0.50)):
    L = 2.0 * log(lam)
    primes = primes_up_to(2000)[:N_primes]
    rows = []
    for f in sigma_factors:
        sigma = f * L
        t0 = time.time()
        mu1, mu2 = mu12(lam, sigma, Nb, primes)
        rows.append({"sigma_over_L": f, "sigma": sigma,
                     "mu1": mu1, "mu2": mu2, "gap": mu2 - mu1,
                     "t": time.time() - t0})
        print(f"  [sigma] sigma/L={f:.2f}  mu1={mu1:+.4f}  mu2={mu2:+.4f}  "
              f"gap={mu2 - mu1:.3f}  [{rows[-1]['t']:.1f}s]")
    return {"lam": lam, "N_basis": Nb, "N_primes": N_primes, "rows": rows}


def task_Nprimes_scaling(lam=68.63, Nb=600, sigma=None,
                         Np_list=(5, 10, 20, 30, 50, 80)):
    if sigma is None:
        sigma = 2.0 * log(lam) / 4.0
    rows = []
    for Np in Np_list:
        primes = primes_up_to(5000)[:Np]
        t0 = time.time()
        mu1, mu2 = mu12(lam, sigma, Nb, primes)
        rows.append({"N_primes": Np, "p_max": primes[-1],
                     "mu1": mu1, "mu2": mu2, "gap": mu2 - mu1,
                     "t": time.time() - t0})
        print(f"  [Np] Np={Np:4d}  pmax={primes[-1]:5d}  mu1={mu1:+.4f}  "
              f"mu2={mu2:+.4f}  gap={mu2 - mu1:.3f}  [{rows[-1]['t']:.1f}s]")
    return {"lam": lam, "N_basis": Nb, "sigma": sigma, "rows": rows}


def task_diagonal(lam=68.63, sigma=None,
                  pairs=((20, 5), (50, 5), (100, 10), (200, 20),
                         (300, 30), (500, 50))):
    if sigma is None:
        sigma = 2.0 * log(lam) / 4.0
    rows = []
    for Nb, Np in pairs:
        primes = primes_up_to(5000)[:Np]
        t0 = time.time()
        mu1, mu2 = mu12(lam, sigma, Nb, primes)
        rows.append({"N_basis": Nb, "N_primes": Np,
                     "mu1": mu1, "mu2": mu2, "gap": mu2 - mu1,
                     "t": time.time() - t0})
        print(f"  [diag] Nb={Nb:5d} Np={Np:4d}  mu1={mu1:+.4f}  "
              f"mu2={mu2:+.4f}  gap={mu2 - mu1:.3f}  [{rows[-1]['t']:.1f}s]")
    return {"lam": lam, "sigma": sigma, "rows": rows}


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    report = {}
    print("=" * 72)
    print("R44 - pin down the Hermite-basis mu_1 limit")
    print("=" * 72)

    # 1) main push at lam=68.63
    print("\n[1] N_basis push (lam=68.63, Np=11, sigma=L/4)")
    push_main = task_Nbasis_push(
        lam=68.63, N_primes=11,
        Nb_list=[80, 120, 200, 300, 400, 600, 800, 1000, 1500, 2000])
    report["push_main"] = push_main
    Ns = [r["N_basis"] for r in push_main["rows"] if "mu1" in r]
    mus = [r["mu1"] for r in push_main["rows"] if "mu1" in r]
    push_main["fits"] = all_fits(Ns, mus)
    for k, fit in push_main["fits"].items():
        print(f"  fit[{k}]: {fit}")

    # 1b) sanity at second lam
    print("\n[1b] N_basis push (lam=20, Np=11, sigma=L/4)")
    push_lam20 = task_Nbasis_push(
        lam=20.0, N_primes=11,
        Nb_list=[80, 200, 400, 600])
    report["push_lam20"] = push_lam20
    Ns2 = [r["N_basis"] for r in push_lam20["rows"] if "mu1" in r]
    mus2 = [r["mu1"] for r in push_lam20["rows"] if "mu1" in r]
    if len(Ns2) >= 3:
        push_lam20["fits"] = all_fits(Ns2, mus2)
        for k, fit in push_lam20["fits"].items():
            print(f"  fit[{k}]: {fit}")

    # 3) sigma stability at large Nb
    print("\n[3] sigma stability at Nb=600, Np=11")
    sig = task_sigma_stability(lam=68.63, Nb=600, N_primes=11,
                               sigma_factors=(0.15, 0.25, 0.35, 0.50))
    report["sigma_stability"] = sig

    # 4) N_primes scaling at large Nb
    print("\n[4] N_primes scaling at Nb=600, sigma=L/4")
    nps = task_Nprimes_scaling(
        lam=68.63, Nb=600,
        Np_list=(5, 10, 20, 30, 50, 80))
    report["nprimes_scaling"] = nps

    # 5) joint diagonal limit
    print("\n[5] diagonal joint limit (Nb ~ 10*Np)")
    diag = task_diagonal(lam=68.63,
                         pairs=((50, 5), (100, 10), (200, 20),
                                (300, 30), (500, 50)))
    report["diagonal"] = diag

    out_path = os.path.join(CODE, "r44_hermite_limit.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nSaved -> {out_path}")
    return report


if __name__ == "__main__":
    main()
