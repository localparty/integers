"""R45: push lambda much higher, fit the mu_1(lambda) scaling law.

Builds on r44_hermite_limit.py. At each lambda in a large grid:
  - use the FULL prime set {p : log p <= L = 2 log lambda}
  - pick N_basis large enough for basis convergence (scaled with lambda)
  - sample sigma across the stable window, record the band
  - record mu_1 with an uncertainty estimate

Then fit several candidate scaling laws:
  (a) mu_1 = -c log lambda + d                (pure log)
  (b) mu_1 = -c log lambda log log lambda     (RvM-like)
  (c) mu_1 = -c (log lambda)^alpha            (power of log)
  (d) mu_1 = -c log lambda + d/lambda         (log + subleading)

Compare constant c to known analytic constants.

Writes: code/r45_large_lambda.json
"""

import json
import os
import sys
import time
import numpy as np
from math import log, sqrt, pi, exp

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r43_hermite_basis import (
    build_QW_hermite,
    even_eigs_hermite,
    primes_up_to,
)


# ----------------------------------------------------------------------
# Single-point measurement at (lambda, sigma, N_basis)
# ----------------------------------------------------------------------

def mu1_single(lam, sigma, Nb, primes, n_per_sigma=24, pad_sigma=5.0):
    Q, _, _, _, _ = build_QW_hermite(
        lam, sigma, Nb, primes, n_per_sigma=n_per_sigma, pad_sigma=pad_sigma
    )
    vals, _, _ = even_eigs_hermite(Q, Nb)
    mu1 = float(vals[0]) if len(vals) else float("nan")
    mu2 = float(vals[1]) if len(vals) > 1 else float("nan")
    return mu1, mu2


def measure_lambda(lam, Nb, sigma_factors=(0.20, 0.25, 0.30),
                   n_per_sigma=24, pad_sigma=5.0, p_bound=None):
    """At one lambda, compute mu_1 across several sigma values.

    Returns dict with the band [min, max], the central value (sigma=L/4),
    the number of primes, N_basis used, and per-sigma rows.
    """
    L = 2.0 * log(lam)
    p_limit = int(exp(L)) + 1  # p <= lambda^2
    if p_bound is not None:
        p_limit = min(p_limit, p_bound)
    primes = [p for p in primes_up_to(p_limit) if log(p) <= L]
    Np = len(primes)
    rows = []
    for f in sigma_factors:
        sigma = f * L
        t0 = time.time()
        try:
            mu1, mu2 = mu1_single(lam, sigma, Nb, primes,
                                  n_per_sigma=n_per_sigma,
                                  pad_sigma=pad_sigma)
            err = None
        except Exception as e:
            mu1 = float("nan"); mu2 = float("nan"); err = str(e)
        dt = time.time() - t0
        rows.append({"sigma_over_L": f, "sigma": sigma,
                     "mu1": mu1, "mu2": mu2, "t": dt, "error": err})
        if err is None:
            print(f"    sigma/L={f:.2f}  mu1={mu1:+.4f}  mu2={mu2:+.4f}  [{dt:.1f}s]")
        else:
            print(f"    sigma/L={f:.2f}  ERROR {err}  [{dt:.1f}s]")
    mus = [r["mu1"] for r in rows if r.get("error") is None and np.isfinite(r["mu1"])]
    if mus:
        mu_min = float(min(mus)); mu_max = float(max(mus))
        mu_central = next((r["mu1"] for r in rows if abs(r["sigma_over_L"] - 0.25) < 1e-9), mus[0])
        band = 0.5 * (mu_max - mu_min)
    else:
        mu_min = mu_max = mu_central = float("nan"); band = float("nan")
    return {
        "lam": lam, "L": L, "N_primes": Np, "p_max": primes[-1] if primes else None,
        "N_basis": Nb, "sigma_factors": list(sigma_factors),
        "rows": rows, "mu1_central": mu_central,
        "mu1_min": mu_min, "mu1_max": mu_max, "band_half": band,
    }


# ----------------------------------------------------------------------
# Scaling-law fits
# ----------------------------------------------------------------------

def fit_log_linear(lams, mus):
    # mu = -c*log lam + d
    x = np.log(np.asarray(lams, dtype=float))
    y = np.asarray(mus, dtype=float)
    A = np.vstack([x, np.ones_like(x)]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    slope, intercept = sol
    pred = A @ sol
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    return {"form": "mu = -c*log(lam) + d",
            "c": float(-slope), "d": float(intercept),
            "rmse": rmse,
            "limit_lam_inf": ("+inf" if slope > 0 else "-inf")}


def fit_loglog(lams, mus):
    # mu = -c log lam log log lam + d
    lams = np.asarray(lams, dtype=float)
    x = np.log(lams) * np.log(np.log(lams))
    y = np.asarray(mus, dtype=float)
    A = np.vstack([x, np.ones_like(x)]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    slope, intercept = sol
    pred = A @ sol
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    return {"form": "mu = -c*log(lam)*log(log(lam)) + d",
            "c": float(-slope), "d": float(intercept), "rmse": rmse,
            "limit_lam_inf": ("+inf" if slope > 0 else "-inf")}


def fit_power_of_log(lams, mus):
    # mu = a - c * (log lam)^alpha
    lams = np.asarray(lams, dtype=float)
    y = np.asarray(mus, dtype=float)
    best = None
    for alpha in np.linspace(0.2, 3.0, 281):
        x = np.log(lams) ** alpha
        A = np.vstack([x, np.ones_like(x)]).T
        sol, *_ = np.linalg.lstsq(A, y, rcond=None)
        pred = A @ sol
        rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
        if best is None or rmse < best["rmse"]:
            best = {"form": "mu = -c*(log lam)^alpha + d",
                    "c": float(-sol[0]), "d": float(sol[1]),
                    "alpha": float(alpha), "rmse": rmse,
                    "limit_lam_inf": ("+inf" if sol[0] > 0 else "-inf")}
    return best


def fit_log_plus_sub(lams, mus):
    # mu = -c log lam + d + e/lam
    lams = np.asarray(lams, dtype=float)
    y = np.asarray(mus, dtype=float)
    A = np.vstack([np.log(lams), np.ones_like(lams), 1.0 / lams]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ sol
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    return {"form": "mu = -c*log(lam) + d + e/lam",
            "c": float(-sol[0]), "d": float(sol[1]), "e": float(sol[2]),
            "rmse": rmse,
            "limit_lam_inf": ("+inf" if sol[0] > 0 else "-inf")}


def fit_saturating(lams, mus):
    # mu = a + b/log(lam)   (if saturating to finite a<0)
    lams = np.asarray(lams, dtype=float)
    y = np.asarray(mus, dtype=float)
    x = 1.0 / np.log(lams)
    A = np.vstack([x, np.ones_like(x)]).T
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    pred = A @ sol
    rmse = float(np.sqrt(np.mean((pred - y) ** 2)))
    return {"form": "mu = a + b/log(lam)",
            "a": float(sol[1]), "b": float(sol[0]),
            "rmse": rmse, "limit_lam_inf": float(sol[1])}


def all_scaling_fits(lams, mus):
    return {
        "log_linear": fit_log_linear(lams, mus),
        "loglog":     fit_loglog(lams, mus),
        "power_log":  fit_power_of_log(lams, mus),
        "log_plus_sub": fit_log_plus_sub(lams, mus),
        "saturating": fit_saturating(lams, mus),
    }


# ----------------------------------------------------------------------
# Identify c against known constants
# ----------------------------------------------------------------------

def identify_constant(c):
    EULER = 0.5772156649015329
    candidates = {
        "1/(2*pi)":        1.0 / (2 * pi),
        "1/(4*pi)":        1.0 / (4 * pi),
        "1/pi":            1.0 / pi,
        "2/pi":            2.0 / pi,
        "1/2":             0.5,
        "1":               1.0,
        "2":               2.0,
        "e/pi":            exp(1) / pi,
        "log(2*pi)/2":     log(2 * pi) / 2,
        "log(2*pi)":       log(2 * pi),
        "gamma_Euler":     EULER,
        "1/2 + gamma/2":   0.5 + EULER / 2,
        "log 2":           log(2),
        "log pi":          log(pi),
        "pi/2":            pi / 2,
        "pi":              pi,
        "3/(2*pi)":        3.0 / (2 * pi),
    }
    best = sorted(
        [(name, val, abs(c - val), abs(c - val) / abs(val) if val != 0 else float("inf"))
         for name, val in candidates.items()],
        key=lambda x: x[2],
    )
    return [{"name": n, "value": v, "abs_err": e, "rel_err": r}
            for n, v, e, r in best[:6]]


# ----------------------------------------------------------------------
# Main driver
# ----------------------------------------------------------------------

def choose_Nbasis(lam):
    """Scale N_basis with lam. R44 found Nb=1000 enough at lam<=100."""
    if lam <= 25:    return 500
    if lam <= 50:    return 700
    if lam <= 110:   return 900
    if lam <= 160:   return 900
    if lam <= 220:   return 1000
    if lam <= 320:   return 1100
    if lam <= 550:   return 1300
    return 1500


def main():
    report = {"r44_baseline": {}, "points": [], "fits": {}, "identify_c": None}
    print("=" * 72)
    print("R45 -- large lambda mu_1 scaling")
    print("=" * 72)

    # Reuse R44's points for lambda <= 100 directly (do not recompute to save time)
    r44_path = os.path.join(CODE, "r44_hermite_limit.json")
    r44_known = {
        10.0:    {"mu1_central": -3.699,  "band_half": None, "N_basis": 800,  "N_primes": 25},
        20.0:    {"mu1_central": -4.726,  "band_half": None, "N_basis": 800,  "N_primes": 78},
        40.0:    {"mu1_central": -7.157,  "band_half": None, "N_basis": 1000, "N_primes": 251},
        68.63:   {"mu1_central": -8.097,  "band_half": 2.5,  "N_basis": 1000, "N_primes": 635},
        100.0:   {"mu1_central": -12.132, "band_half": None, "N_basis": 1000, "N_primes": 1229},
    }
    # We will still recompute a few of these in-script at fresh settings to verify.

    # Reuse all R44 values for lam <= 100; compute new ones above.
    new_lams = [150.0, 200.0, 300.0, 500.0]

    points = []
    for lam in [10.0, 20.0, 40.0, 68.63, 100.0]:
        rec = r44_known[lam]
        points.append({
            "lam": lam, "L": 2.0 * log(lam),
            "mu1_central": rec["mu1_central"], "band_half": rec["band_half"],
            "N_basis": rec["N_basis"], "N_primes": rec["N_primes"],
            "source": "r44_reused",
        })

    for lam in new_lams:
        Nb = choose_Nbasis(lam)
        print(f"\n[new] lam={lam}  Nb={Nb}")
        sigma_facs = (0.22, 0.25, 0.28) if lam <= 220 else (0.25, 0.28)
        n_per_sigma = 18 if lam <= 220 else 14
        pad = 4.0 if lam <= 220 else 3.5
        res = measure_lambda(lam, Nb, sigma_factors=sigma_facs,
                             n_per_sigma=n_per_sigma, pad_sigma=pad)
        res["source"] = "r45_new"
        points.append(res)

    # ---- Fits ----
    lams_fit = []
    mus_fit = []
    for pt in points:
        mu = pt.get("mu1_central")
        if mu is not None and np.isfinite(mu):
            lams_fit.append(pt["lam"])
            mus_fit.append(mu)

    print("\n[scaling fits]")
    print("  lam     mu1_central    L=2log(lam)")
    for l, m in zip(lams_fit, mus_fit):
        print(f"  {l:7.2f}  {m:+10.4f}     {2*log(l):.3f}")

    fits = all_scaling_fits(lams_fit, mus_fit)
    for name, fit in fits.items():
        print(f"  fit[{name}]: {fit}")

    # Identify constant from the best-fitting log_linear form.
    c_log = fits["log_linear"]["c"]
    ident = identify_constant(c_log)
    print(f"\n[identify c] from log_linear: c = {c_log:.6f}")
    for row in ident:
        print(f"  {row['name']:20s}  value={row['value']:.6f}  "
              f"abs_err={row['abs_err']:.4f}  rel_err={row['rel_err']*100:.2f}%")

    report["points"] = points
    report["lams_fit"] = lams_fit
    report["mus_fit"] = mus_fit
    report["fits"] = fits
    report["identify_c"] = ident

    out_path = os.path.join(CODE, "r45_large_lambda.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nSaved -> {out_path}")
    return report


if __name__ == "__main__":
    main()
