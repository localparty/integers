"""R46: Extract full spectrum (smallest / near-zero / largest) of Q_W at
multiple lambda and test whether any eigenvalue tracks Riemann zeros γ_n
under any natural candidate map.

Reuses the Hermite Q_W builder from r43_hermite_basis.py and the prime
saturation / choose_Nbasis conventions from r45_large_lambda.py.

Outputs:
  code/r46_spectrum_scan.json  -- raw spectra + tracking analysis
(the human-readable report is written separately to research/100...)
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
from r45_large_lambda import choose_Nbasis

# First ten non-trivial Riemann zeros (imaginary parts)
GAMMAS = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
          37.586178, 40.918719, 43.327073, 48.005151, 49.773832]


# ----------------------------------------------------------------------
# Spectrum extraction
# ----------------------------------------------------------------------

def even_full_spectrum(Q, N_basis):
    """Return the FULL even-subspace spectrum (sorted ascending)."""
    even_idx = np.arange(0, N_basis, 2)
    Qe = Q[np.ix_(even_idx, even_idx)]
    Qe = 0.5 * (Qe + Qe.T)
    vals = np.linalg.eigvalsh(Qe)
    vals.sort()
    return vals


def spectrum_features(vals, k_edge=10):
    """Return smallest k, nearest-zero k, largest k."""
    smallest = vals[:k_edge].tolist()
    largest  = vals[-k_edge:][::-1].tolist()
    order = np.argsort(np.abs(vals))
    nearest_zero = vals[order[:k_edge]].tolist()
    return smallest, nearest_zero, largest


# ----------------------------------------------------------------------
# Candidate maps γ_n -> target in the spectrum
# ----------------------------------------------------------------------

def candidate_maps():
    return {
        "gamma":              lambda g: g,
        "-gamma":             lambda g: -g,
        "gamma^2":            lambda g: g * g,
        "-gamma^2":           lambda g: -g * g,
        "1/4 + gamma^2":      lambda g: 0.25 + g * g,
        "-(1/4 + gamma^2)":   lambda g: -(0.25 + g * g),
        "gamma/(2pi)":        lambda g: g / (2.0 * pi),
        "log gamma":          lambda g: log(g),
    }


def tracking_scores(vals, gammas=GAMMAS):
    """For each candidate map f, each γ_n in gammas, find the eigenvalue
    closest to f(γ_n) and record (idx_from_low, mu, dist, rel_dist)."""
    maps = candidate_maps()
    scores = {}
    vals = np.asarray(vals)
    for name, f in maps.items():
        rows = []
        for n, g in enumerate(gammas, 1):
            target = f(g)
            k = int(np.argmin(np.abs(vals - target)))
            mu = float(vals[k])
            d = abs(mu - target)
            rel = d / max(1e-12, abs(target))
            rows.append({"n": n, "gamma": g, "target": target,
                         "idx": k, "mu": mu, "abs_err": d, "rel_err": rel})
        # Best over n under this map
        best = min(rows, key=lambda r: r["rel_err"])
        scores[name] = {"rows": rows, "best_rel": best["rel_err"],
                        "best_n": best["n"], "best_idx": best["idx"],
                        "best_mu": best["mu"], "best_target": best["target"]}
    return scores


# ----------------------------------------------------------------------
# Primes at lambda (full saturation)
# ----------------------------------------------------------------------

def saturated_primes(lam):
    L = 2.0 * log(lam)
    p_limit = int(exp(L)) + 1
    return [p for p in primes_up_to(p_limit) if log(p) <= L], L


# ----------------------------------------------------------------------
# Main driver
# ----------------------------------------------------------------------

def measure_point(lam, Nb, primes, sigma_factor=0.25, n_per_sigma=16,
                  pad_sigma=3.5, k_edge=10, label=""):
    L = 2.0 * log(lam)
    sigma = sigma_factor * L
    t0 = time.time()
    Q, _, _, _, _ = build_QW_hermite(lam, sigma, Nb, primes,
                                     n_per_sigma=n_per_sigma,
                                     pad_sigma=pad_sigma)
    vals = even_full_spectrum(Q, Nb)
    smallest, near_zero, largest = spectrum_features(vals, k_edge=k_edge)
    scores = tracking_scores(vals)
    dt = time.time() - t0
    # How many eigenvalues within |mu|<=1 of zero
    near1 = int(np.sum(np.abs(vals) <= 1.0))
    near5 = int(np.sum(np.abs(vals) <= 5.0))
    rec = {
        "label": label,
        "lam": lam, "L": L, "sigma": sigma,
        "N_basis": Nb, "N_primes": len(primes),
        "p_max": int(primes[-1]) if primes else None,
        "n_even": int(len(vals)),
        "mu_min": float(vals[0]), "mu_max": float(vals[-1]),
        "n_abs_le_1": near1, "n_abs_le_5": near5,
        "smallest": smallest,
        "nearest_zero": near_zero,
        "largest": largest,
        "tracking_best": {name: {"rel": sc["best_rel"],
                                  "n": sc["best_n"],
                                  "idx": sc["best_idx"],
                                  "mu": sc["best_mu"],
                                  "target": sc["best_target"]}
                          for name, sc in scores.items()},
        "tracking_full": scores,
        "time_s": dt,
    }
    return rec


def main():
    report = {"points": [], "n_primes_diag": [], "cc6_scan": None}
    print("=" * 72); print("R46 -- spectrum scan"); print("=" * 72)

    # PART 1: scan across lambda with full prime saturation
    lam_list = [10.0, 20.0, 40.0, 68.63, 100.0, 150.0, 200.0, 300.0]
    for lam in lam_list:
        Nb = choose_Nbasis(lam)
        # cap Nb for speed -- we care about low / near-zero eigenvalues
        Nb = min(Nb, 700)
        primes, L = saturated_primes(lam)
        print(f"\n[lam={lam}] Nb={Nb} Np={len(primes)} L={L:.3f}")
        try:
            rec = measure_point(lam, Nb, primes, sigma_factor=0.25,
                                n_per_sigma=14, pad_sigma=3.0,
                                label=f"saturated_lam={lam}")
        except Exception as e:
            print(f"  ERROR: {e}")
            continue
        print(f"  mu_min={rec['mu_min']:+.4f} mu_max={rec['mu_max']:+.4f}"
              f" n_even={rec['n_even']} |mu|<=1:{rec['n_abs_le_1']}"
              f" |mu|<=5:{rec['n_abs_le_5']} [{rec['time_s']:.1f}s]")
        print(f"  smallest[0..4] = {[f'{v:+.3f}' for v in rec['smallest'][:5]]}")
        print(f"  near_zero[0..4]= {[f'{v:+.3f}' for v in rec['nearest_zero'][:5]]}")
        print(f"  largest[0..4]  = {[f'{v:+.3f}' for v in rec['largest'][:5]]}")
        print(f"  best map tracking scores (rel_err, n, idx, mu):")
        for name, b in rec["tracking_best"].items():
            print(f"    {name:22s} rel={b['rel']:.3e} gamma_{b['n']} "
                  f"idx={b['idx']} mu={b['mu']:+.4f} target={b['target']:+.4f}")
        report["points"].append(rec)

    # PART 4: N_primes diagnostic at lam=68.63
    print("\n" + "=" * 72)
    print("PART 4 -- N_primes diagnostic at lam=68.63")
    print("=" * 72)
    lam = 68.63
    Nb = min(choose_Nbasis(lam), 700)
    full_primes, L = saturated_primes(lam)
    sigma = 0.25 * L
    N_primes_list = [6, 11, 50, 100, 635]
    for Np_cap in N_primes_list:
        primes = full_primes[:Np_cap]
        if len(primes) < Np_cap and Np_cap > len(full_primes):
            continue
        try:
            rec = measure_point(lam, Nb, primes, sigma_factor=0.25,
                                n_per_sigma=14, pad_sigma=3.0,
                                label=f"lam=68.63 Np={Np_cap}")
        except Exception as e:
            print(f"  Np={Np_cap} ERROR: {e}"); continue
        print(f"\n[lam=68.63 Np={Np_cap}] mu_min={rec['mu_min']:+.4f} "
              f"mu_max={rec['mu_max']:+.4f} n_even={rec['n_even']}")
        print(f"  smallest[0..4] = {[f'{v:+.3f}' for v in rec['smallest'][:5]]}")
        print(f"  near_zero[0..4]= {[f'{v:+.3f}' for v in rec['nearest_zero'][:5]]}")
        for name, b in rec["tracking_best"].items():
            print(f"    {name:22s} rel={b['rel']:.3e} gamma_{b['n']} "
                  f"idx={b['idx']} mu={b['mu']:+.4f} target={b['target']:+.4f}")
        report["n_primes_diag"].append(rec)

    # PART 5: CC 6-prime reproduction
    print("\n" + "=" * 72)
    print("PART 5 -- CC 2511.22755 reproduction: lam=68.63 N_primes=6")
    print("=" * 72)
    primes6 = full_primes[:6]
    rec_cc = measure_point(68.63, Nb, primes6, sigma_factor=0.25,
                           n_per_sigma=14, pad_sigma=3.0,
                           label="CC6")
    print(f"  primes={primes6}")
    print(f"  mu_min={rec_cc['mu_min']:+.4f} mu_max={rec_cc['mu_max']:+.4f} "
          f"n_even={rec_cc['n_even']}")
    # Dump a bigger chunk of the spectrum for CC6
    Q, _, _, _, _ = build_QW_hermite(68.63, 0.25 * L, Nb, primes6,
                                     n_per_sigma=14, pad_sigma=3.0)
    vals_cc = even_full_spectrum(Q, Nb)
    rec_cc["full_spectrum_first_60"] = [float(v) for v in vals_cc[:60]]
    rec_cc["full_spectrum_last_20"]  = [float(v) for v in vals_cc[-20:]]
    report["cc6_scan"] = rec_cc

    out_path = os.path.join(CODE, "r46_spectrum_scan.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nSaved -> {out_path}")
    return report


if __name__ == "__main__":
    main()
