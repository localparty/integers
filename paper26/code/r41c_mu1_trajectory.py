"""R41 Lead C: μ_1(N) trajectory for Connes-Consani Weil quadratic form.

Question (R40 Path 4 reframing): does μ_1, the smallest (most-negative) eigenvalue
of Q_W on the even subspace, descend to a finite negative limit, asymptote to 0,
or cross 0 as we add primes?  R38 saw monotone descent to ~ -13.10 over the
first 5 primes.  We push to 50-100 primes and fit the descent law.
"""

import numpy as np
import json
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r38_krein_rutman_rh import connes_consani_fourier_weil_matrix


def primes_up_to(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]


def even_projector(N_modes):
    dim = 2 * N_modes + 1
    ns = np.arange(-N_modes, N_modes + 1)
    P = np.zeros((dim, dim))
    for k in range(dim):
        n = ns[k]
        k_neg = int(np.where(ns == -n)[0][0])
        P[k, k] += 0.5
        P[k, k_neg] += 0.5
    return P, ns


def even_eigs(Q_W, P_even, tol=1e-9):
    """Project to even subspace and return sorted nonzero eigenvalues."""
    Q_e = P_even @ Q_W @ P_even
    Q_e = (Q_e + Q_e.T) / 2
    eigs = np.linalg.eigvalsh(Q_e)
    eigs = np.sort(eigs)
    eigs_nz = eigs[np.abs(eigs) > tol]
    return eigs_nz


def trajectory(lam, N_modes, primes, verbose=True):
    P_even, ns = even_projector(N_modes)
    rows = []
    t0 = time.time()
    for k in range(1, len(primes) + 1):
        primes_so_far = primes[:k]
        Q_W, _, _, _ = connes_consani_fourier_weil_matrix(lam, N_modes, primes_so_far)
        eigs = even_eigs(Q_W, P_even)
        if len(eigs) >= 2:
            mu1 = float(eigs[0])
            mu2 = float(eigs[1])
        else:
            mu1 = float(eigs[0]) if len(eigs) else 0.0
            mu2 = mu1
        gap = mu2 - mu1
        row = {
            "N": k,
            "p_N": int(primes_so_far[-1]),
            "log_pN": float(np.log(primes_so_far[-1])),
            "mu1": mu1,
            "mu2": mu2,
            "gap": float(gap),
            "sign_mu1": int(np.sign(mu1)),
        }
        rows.append(row)
        if verbose and (k % 5 == 0 or k <= 10 or k == len(primes)):
            dt = time.time() - t0
            print(f"  N={k:3d} p={primes_so_far[-1]:4d}  mu1={mu1:+.6e}  mu2={mu2:+.6e}  gap={gap:.3e}  [{dt:.1f}s]")
    return rows


def fit_descents(rows):
    Ns = np.array([r["N"] for r in rows], dtype=float)
    pNs = np.array([r["p_N"] for r in rows], dtype=float)
    mu1 = np.array([r["mu1"] for r in rows], dtype=float)
    log_pN = np.log(pNs)
    log_N = np.log(Ns)
    fits = {}

    # Fit 1: mu1 ~ A - B * log N
    A1, B1 = np.polyfit(log_N, mu1, 1)  # mu1 = A1*log_N + B1 -> slope=A1, intercept=B1
    pred1 = A1 * log_N + B1
    res1 = float(np.sqrt(np.mean((mu1 - pred1) ** 2)))
    fits["log_N"] = {"slope_A": float(A1), "intercept_B": float(B1), "rmse": res1, "form": "mu1 ~ B + A*log(N)"}

    # Fit 2: mu1 ~ A - B * N^alpha (try alpha grid)
    best = None
    for alpha in np.linspace(0.1, 1.5, 29):
        x = Ns ** alpha
        s, b = np.polyfit(x, mu1, 1)
        pred = s * x + b
        rmse = float(np.sqrt(np.mean((mu1 - pred) ** 2)))
        if best is None or rmse < best["rmse"]:
            best = {"alpha": float(alpha), "slope_A": float(s), "intercept_B": float(b), "rmse": rmse,
                    "form": "mu1 ~ B + A*N^alpha"}
    fits["power_N"] = best

    # Fit 3: mu1 ~ A - B*(log p_N)^k
    best3 = None
    for kk in np.linspace(0.5, 3.0, 26):
        x = log_pN ** kk
        s, b = np.polyfit(x, mu1, 1)
        pred = s * x + b
        rmse = float(np.sqrt(np.mean((mu1 - pred) ** 2)))
        if best3 is None or rmse < best3["rmse"]:
            best3 = {"k": float(kk), "slope_A": float(s), "intercept_B": float(b), "rmse": rmse,
                     "form": "mu1 ~ B + A*(log p_N)^k"}
    fits["log_pN_pow"] = best3

    # Fit 4: mu1 ~ A - B*log(p_N)*log(log p_N)  (Riemann-von Mangoldt-ish per-zero density)
    # T log T form: imagine N(T)=T log T / 2pi → invert
    # also try linear in log p_N
    s, b = np.polyfit(log_pN, mu1, 1)
    pred = s * log_pN + b
    rmse = float(np.sqrt(np.mean((mu1 - pred) ** 2)))
    fits["log_pN_linear"] = {"slope_A": float(s), "intercept_B": float(b), "rmse": rmse,
                             "form": "mu1 ~ B + A*log(p_N)"}

    return fits


def ascii_plot(rows, width=70, height=20):
    Ns = [r["N"] for r in rows]
    mu1 = [r["mu1"] for r in rows]
    xmin, xmax = min(Ns), max(Ns)
    ymin, ymax = min(mu1), max(mu1)
    if ymax == ymin:
        ymax = ymin + 1
    grid = [[" "] * width for _ in range(height)]
    for x, y in zip(Ns, mu1):
        cx = int((x - xmin) / (xmax - xmin) * (width - 1))
        cy = int((1 - (y - ymin) / (ymax - ymin)) * (height - 1))
        grid[cy][cx] = "*"
    # zero line
    if ymin <= 0 <= ymax:
        zy = int((1 - (0 - ymin) / (ymax - ymin)) * (height - 1))
        for x in range(width):
            if grid[zy][x] == " ":
                grid[zy][x] = "-"
    lines = []
    lines.append(f"  mu1 vs N    y in [{ymin:.3f}, {ymax:.3f}]   x in [{xmin}, {xmax}]")
    for row in grid:
        lines.append("  |" + "".join(row) + "|")
    lines.append("  +" + "-" * width + "+")
    return "\n".join(lines)


def main():
    # Parameters
    N_PRIMES = 60      # number of primes to include
    primes = primes_up_to(2000)[:N_PRIMES]
    p_max = primes[-1]
    log_pmax = np.log(p_max)
    # Need L = 2 log(lam) > log(p_max) so the m=1 term of biggest prime fits.
    # Choose lam so L is comfortably larger.
    lam_main = float(np.exp(0.75 * log_pmax))   # L = 1.5*log(p_max)
    N_modes_main = 80

    print("=" * 78)
    print(f"R41C: mu_1 trajectory, N_PRIMES={N_PRIMES}, p_max={p_max}")
    print(f"      lam={lam_main:.3f}, L=2*log(lam)={2*np.log(lam_main):.3f}, log(p_max)={log_pmax:.3f}")
    print(f"      N_modes={N_modes_main}, dim={2*N_modes_main+1}")
    print("=" * 78)

    rows = trajectory(lam_main, N_modes_main, primes)
    fits = fit_descents(rows)

    # Sensitivity to N_modes
    print("\n" + "-" * 78)
    print("SENSITIVITY: vary N_modes at small N (first 15 primes)")
    print("-" * 78)
    sens_modes = {}
    for Nm in [40, 60, 80, 100]:
        print(f" N_modes={Nm}:")
        rs = trajectory(lam_main, Nm, primes[:15], verbose=False)
        for r in rs[::5]:
            print(f"   N={r['N']:2d}  mu1={r['mu1']:+.6e}")
        sens_modes[Nm] = rs

    # Sensitivity to lambda
    print("\n" + "-" * 78)
    print("SENSITIVITY: vary lambda at small N (first 15 primes), N_modes=80")
    print("-" * 78)
    sens_lam = {}
    for lam_try in [lam_main * 0.7, lam_main, lam_main * 1.4]:
        L = 2 * np.log(lam_try)
        print(f" lam={lam_try:.3f} (L={L:.3f}):")
        rs = trajectory(lam_try, 80, primes[:15], verbose=False)
        for r in rs[::5]:
            print(f"   N={r['N']:2d}  mu1={r['mu1']:+.6e}")
        sens_lam[f"{lam_try:.3f}"] = rs

    # Output
    out = {
        "params": {
            "N_PRIMES": N_PRIMES,
            "p_max": int(p_max),
            "lam": lam_main,
            "L": 2 * float(np.log(lam_main)),
            "N_modes": N_modes_main,
        },
        "trajectory": rows,
        "fits": fits,
        "sensitivity_N_modes": {str(k): v for k, v in sens_modes.items()},
        "sensitivity_lambda": sens_lam,
    }
    out_path = "/Users/gsix/riemann-hypothesis/code/r41c_mu1_trajectory.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved -> {out_path}")

    print("\n" + "=" * 78)
    print("FITS")
    print("=" * 78)
    for name, fit in fits.items():
        print(f"  {name}: {fit}")

    print("\n" + ascii_plot(rows))

    # Riemann-von Mangoldt comparison
    # N(T) ~ (T/2pi) log(T/2pi).  In Connes-Consani spectral picture, the
    # smallest |eigenvalue|s of Q_W in the right scaling correspond to the
    # imaginary parts of zeros.  If mu_1 ~ -gamma_1 ~ -14.1347... then we
    # would predict mu_1 -> -14.1347 (asymptote negative).
    print("\nRiemann-von Mangoldt comparison:")
    print(f"  First nontrivial zero: gamma_1 = 14.13472514...")
    print(f"  Final mu_1 = {rows[-1]['mu1']:+.6f}")
    print(f"  Final mu_1/(-gamma_1) = {rows[-1]['mu1']/-14.13472514:+.4f}")


if __name__ == "__main__":
    main()
