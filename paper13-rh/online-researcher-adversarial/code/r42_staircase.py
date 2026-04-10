"""R42: Is the μ_1(N) staircase real or a basis artifact?

Re-runs r41c at multiple (N_modes, λ); applies the same analysis to the
R40 P4 random ensembles; computes eigenvector Fourier content at each
plateau; and probes the drop-prime structure.

Outputs: code/r42_staircase.json plus a printed report digestible into
research/96-r42-staircase.md.
"""

import json
import os
import sys
import time
import numpy as np
from math import log

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r38_krein_rutman_rh import connes_consani_fourier_weil_matrix
from r40p4_mechanism import build_QW_from_logset, gen_uniform, gen_Q_dependent, gen_resonant
from r41c_mu1_trajectory import primes_up_to, even_projector


# ---------- Vectorized fast builder (delta_n-only structure) ----------

def build_pole(lam, N_modes):
    L = 2 * np.log(lam)
    dim = 2 * N_modes + 1
    ns = np.arange(-N_modes, N_modes + 1)
    delta = ns[None, :] - ns[:, None]   # delta_n[a,b] = n_b - n_a
    freq = 2 * np.pi * delta / L
    a_c = 0.5
    denom = a_c * a_c + freq * freq
    upper = L / 2
    val = (a_c * np.sinh(a_c * upper) * np.cos(freq * upper)
           + freq * np.cosh(a_c * upper) * np.sin(freq * upper)) / denom
    val *= 2
    Q_pole = val / L
    return Q_pole, ns, L, delta


def atom_contrib(coeff, ell, L, delta):
    """Single -log term contribution: -(2*coeff/L) * cos(2π * delta * ell / L)."""
    phase = 2 * np.pi * delta * ell / L
    return -(2.0 * coeff / L) * np.cos(phase)


def prime_contrib(p, L, delta):
    """All m>=1 contributions of prime p, summed."""
    log_p = np.log(p)
    out = np.zeros_like(delta, dtype=float)
    for m in range(1, int(L / log_p) + 1):
        mlogp = m * log_p
        if mlogp > L:
            break
        coeff = log_p / p ** (m / 2)
        out += atom_contrib(coeff, mlogp, L, delta)
    return out


# First few nontrivial Riemann zero imaginary parts
GAMMAS = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
          37.586178, 40.918719, 43.327073, 48.005151, 49.773832]


def even_eig_full(Q, P_even, tol=1e-9):
    Qe = P_even @ Q @ P_even
    Qe = (Qe + Qe.T) / 2
    vals, vecs = np.linalg.eigh(Qe)
    order = np.argsort(vals)
    vals = vals[order]
    vecs = vecs[:, order]
    keep = np.abs(vals) > tol
    return vals[keep], vecs[:, keep]


def trajectory_primes(lam, N_modes, primes, want_vecs=False):
    P_even, _ = even_projector(N_modes)
    Q_pole, ns, L, delta = build_pole(lam, N_modes)
    Q = Q_pole.copy()
    rows = []
    vecs_at_N = {}
    for k in range(1, len(primes) + 1):
        Q = Q + prime_contrib(primes[k - 1], L, delta)
        Q_sym = (Q + Q.T) / 2
        vals, vecs = even_eig_full(Q_sym, P_even)
        mu1 = float(vals[0]) if len(vals) else 0.0
        rows.append({"N": k, "p_N": int(primes[k - 1]), "mu1": mu1})
        if want_vecs:
            vecs_at_N[k] = (vals[0], vecs[:, 0].real.tolist(), ns.tolist())
    return rows, vecs_at_N


def trajectory_logset(lam, N_modes, log_set_full, coeffs_full):
    P_even = even_projector(N_modes)[0]
    Q_pole, ns, L, delta = build_pole(lam, N_modes)
    Q = Q_pole.copy()
    rows = []
    for k in range(1, len(log_set_full) + 1):
        ell = log_set_full[k - 1]
        c = coeffs_full[k - 1]
        if ell <= L:
            Q = Q + atom_contrib(c, ell, L, delta)
        Q_sym = (Q + Q.T) / 2
        vals, _ = even_eig_full(Q_sym, P_even)
        mu1 = float(vals[0]) if len(vals) else 0.0
        rows.append({"N": k, "ell": float(ell), "mu1": mu1})
    return rows


def detect_plateaus(rows, eps=0.05, min_len=3):
    """Plateaus: maximal runs where |Δμ_1| < eps between consecutive N."""
    mus = [r["mu1"] for r in rows]
    plateaus = []
    i = 0
    n = len(mus)
    while i < n:
        j = i
        while j + 1 < n and abs(mus[j + 1] - mus[j]) < eps:
            j += 1
        if j - i + 1 >= min_len:
            seg = mus[i:j + 1]
            plateaus.append({
                "N_start": i + 1, "N_end": j + 1,
                "len": j - i + 1,
                "mu_mean": float(np.mean(seg)),
                "mu_std": float(np.std(seg)),
            })
        i = j + 1
    return plateaus


def detect_drops(rows, thresh=0.5):
    drops = []
    for k in range(1, len(rows)):
        d = rows[k]["mu1"] - rows[k - 1]["mu1"]
        if d < -thresh:
            drops.append({
                "N": rows[k]["N"],
                "p_N": rows[k].get("p_N", None),
                "ell": rows[k].get("ell", None),
                "delta_mu1": float(d),
                "mu1_after": float(rows[k]["mu1"]),
            })
    return drops


def nearest_gamma(mu_neg):
    target = -mu_neg
    idx = int(np.argmin([abs(target - g) for g in GAMMAS]))
    return idx + 1, GAMMAS[idx], target - GAMMAS[idx]


def fourier_content(vec, ns, L):
    """Identify dominant frequency in even-eigenvector. Returns dominant
    physical frequency in units of 'rad' on [-L/2,L/2]: omega = 2π n / L."""
    v = np.asarray(vec)
    ns = np.asarray(ns)
    # Combine +n and -n weights since vector is even
    weights = {}
    for k, n in enumerate(ns):
        an = abs(int(n))
        weights[an] = weights.get(an, 0.0) + v[k] ** 2
    items = sorted(weights.items(), key=lambda kv: -kv[1])
    # Express dominant n as omega = 2π n / L
    return [(int(n), float(w), float(2 * np.pi * n / L)) for n, w in items[:5]]


def part1_truncations(report):
    primes_all = primes_up_to(2000)[:60]
    p_max = primes_all[-1]
    log_pmax = log(p_max)
    lams = {
        48:  float(np.exp(0.732 * log_pmax)),  # ~ 48
        69:  float(np.exp(0.751 * log_pmax)),  # ~ 69 (matches r41c main)
        96:  float(np.exp(0.811 * log_pmax)),  # ~ 96
        140: float(np.exp(0.876 * log_pmax)),  # ~140
    }
    # Pick lam values near the labels
    lam_values = {48: 48.0, 69: 68.63, 96: 96.09, 140: 140.0}
    Nm_values = [40, 60, 80, 100, 120]

    grid = {}
    print("\n=== PART 1: Truncation grid ===")
    for Nm in Nm_values:
        for lam_label, lam in lam_values.items():
            t0 = time.time()
            rows, _ = trajectory_primes(lam, Nm, primes_all, want_vecs=False)
            plats = detect_plateaus(rows, eps=0.05, min_len=3)
            drops = detect_drops(rows, thresh=0.5)
            for p in plats:
                idx, g, dev = nearest_gamma(p["mu_mean"])
                p["nearest_gamma_idx"] = idx
                p["nearest_gamma"] = g
                p["dev_from_minus_gamma"] = dev
            key = f"Nm{Nm}_lam{lam_label}"
            grid[key] = {
                "lam": lam, "N_modes": Nm,
                "rows": rows, "plateaus": plats, "drops": drops,
            }
            dt = time.time() - t0
            drop_primes = [d["p_N"] for d in drops]
            mu_final = rows[-1]["mu1"]
            print(f"  Nm={Nm:3d} lam={lam_label:3d}  mu1_final={mu_final:+.3f}  "
                  f"plateaus={len(plats)}  drop_p={drop_primes}  [{dt:.1f}s]")
    report["part1_grid"] = grid
    return grid


def part2_controls(report):
    print("\n=== PART 2: Random ensemble controls ===")
    # Match r41c main run (lam ~ 68.63, N_modes 80) but use 40 atoms (faster, comparable to ~40 primes)
    lam = 68.63
    N_modes = 80
    N_atoms = 40
    n_trials = 5
    rng = np.random.default_rng(2026)

    out = {}
    for name, gen in [("uniform", gen_uniform),
                      ("Q_dependent", gen_Q_dependent),
                      ("resonant", gen_resonant)]:
        trials_out = []
        for t in range(n_trials):
            log_set = gen(N_atoms, lam, rng)
            log_set = [ell for ell in log_set if ell <= 2 * log(lam) - 1e-6]
            coeffs = [0.5 * ell * np.exp(-ell / 2) for ell in log_set]
            rows = trajectory_logset(lam, N_modes, log_set, coeffs)
            plats = detect_plateaus(rows, eps=0.05, min_len=3)
            drops = detect_drops(rows, thresh=0.5)
            for p in plats:
                idx, g, dev = nearest_gamma(p["mu_mean"])
                p["nearest_gamma_idx"] = idx
                p["nearest_gamma"] = g
                p["dev_from_minus_gamma"] = dev
            trials_out.append({
                "log_set": log_set, "rows": rows,
                "plateaus": plats, "drops": drops,
                "mu_final": rows[-1]["mu1"],
            })
            print(f"  {name} t{t}: mu_final={rows[-1]['mu1']:+.3f}  "
                  f"plats={len(plats)}  drops={len(drops)}")
        # Aggregate: do plateau means from this ensemble fall near {-γ_n}?
        all_plat_means = [p["mu_mean"] for tr in trials_out for p in tr["plateaus"]]
        out[name] = {"trials": trials_out, "plateau_means": all_plat_means}
    report["part2_controls"] = out
    return out


def part3_eigenvectors(report):
    print("\n=== PART 3: Eigenvector content at plateaus ===")
    primes_all = primes_up_to(2000)[:60]
    lam = 68.63
    N_modes = 80
    L = 2 * log(lam)
    rows, vecs_at_N = trajectory_primes(lam, N_modes, primes_all, want_vecs=True)
    plats = detect_plateaus(rows, eps=0.05, min_len=3)
    out_plats = []
    for p in plats:
        # Take midpoint of plateau
        N_mid = (p["N_start"] + p["N_end"]) // 2
        mu, vec, ns = vecs_at_N[N_mid]
        fc = fourier_content(vec, ns, L)
        idx, g, dev = nearest_gamma(p["mu_mean"])
        # Connection to γ: in u-coords, γ would correspond to omega = γ
        # so dominant n_dom * 2π/L should be near γ ?
        n_dom = fc[0][0]
        omega_dom = fc[0][2]
        out_plats.append({
            "N_start": p["N_start"], "N_end": p["N_end"], "N_mid": N_mid,
            "mu_mean": p["mu_mean"], "nearest_gamma_idx": idx, "nearest_gamma": g,
            "fourier_top5": fc, "n_dom": n_dom, "omega_dom": omega_dom,
            "gamma_over_omega": (g / omega_dom) if omega_dom != 0 else None,
        })
        print(f"  Plateau N={p['N_start']}..{p['N_end']}  μ={p['mu_mean']:+.3f}  "
              f"~ -γ_{idx} ({-g:.3f})  dom n={n_dom} ω={omega_dom:.3f}  γ/ω={out_plats[-1]['gamma_over_omega']}")
    report["part3_eigenvectors"] = {"plateaus": out_plats, "L": L}
    return out_plats


def part4_drops(report):
    print("\n=== PART 4: Drop prime number theory ===")
    drops = [19, 73, 79, 109, 281]
    rows = []
    for p in drops:
        lp = log(p)
        # Compare to γ_n
        nearest = []
        for idx, g in enumerate(GAMMAS, 1):
            nearest.append({
                "n": idx,
                "gamma": g,
                "log_p_minus_log_gamma": lp - log(g),
                "p_minus_gamma": p - g,
                "p_over_exp_gamma": p / np.exp(g),
                "log_p_over_log_gamma": lp / log(g),
            })
        # closest by |p - gamma|
        nearest.sort(key=lambda r: abs(r["p_minus_gamma"]))
        rows.append({
            "p": p, "log_p": lp,
            "closest_gamma": nearest[0],
            "all": nearest[:3],
        })
        print(f"  p={p:4d}  log p={lp:.4f}  closest γ_{nearest[0]['n']}={nearest[0]['gamma']:.3f} "
              f"Δ={nearest[0]['p_minus_gamma']:+.3f}")
    report["part4_drops"] = rows
    return rows


def main():
    report = {}
    part1_truncations(report)
    part2_controls(report)
    part3_eigenvectors(report)
    part4_drops(report)
    out_path = os.path.join(CODE, "r42_staircase.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nSaved -> {out_path}")


if __name__ == "__main__":
    main()
