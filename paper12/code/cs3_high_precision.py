"""CS-2 full evaluation: N-convergence + Scenario C direct test + boundary decay.

Builds on cs1_5_parity_projected.py (parity-projected even subspace).
Three sub-experiments in one driver:
  1. N-convergence ladder for each λ
  2. ξ̂_λ(z) = 2 L^{-1/2} sin(zL/2) Σ_j ξ_j / (z - 2πj/L) at fixed z
  3. boundary value |ξ_λ(λ^{±1})| power-law fit
"""

import json, os, sys, time
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r49_fourier_circle import build_QW, eigh_mp, parity_projector_indices, parity_score
from cs1_5_parity_projected import project_even, even_vec_to_full

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
DPS = 200  # bumped from 40 for round-10 precision diagnostic; cs3 trimmed N ladder

# ---------------------------------------------------------------------------
# Core solver: returns full even eigenvector (length N+1) for lowest even state
# ---------------------------------------------------------------------------
def solve_even_ground(lam, N, dps=DPS):
    mp.mp.dps = dps
    A, L = build_QW(lam, N, dps=dps, verbose=False)
    Qe = project_even(A, N)
    vals, V = eigh_mp(Qe)
    eps = vals[0]
    xi_even = [V[i, 0] for i in range(N+1)]  # in orthonormal even basis e_j
    # Fix sign: make first nonzero component positive (for reproducibility)
    for v in xi_even:
        if abs(v) > mp.mpf("1e-20"):
            if v < 0:
                xi_even = [-x for x in xi_even]
            break
    # Parity check
    pair = parity_projector_indices(N)
    full = even_vec_to_full(xi_even, N)
    chi0 = parity_score(full, pair)
    # second eigenvalue (gap)
    eps2 = vals[1] if len(vals) > 1 else None
    return {
        "L": L, "eps": eps, "eps2": eps2, "xi_even": xi_even,
        "chi0": chi0,
    }

# ---------------------------------------------------------------------------
# Sub-experiment 1: N-convergence
# ---------------------------------------------------------------------------
def sub1_full_disabled():
    lam_list = [
        ("sqrt13", mp.sqrt(13)),
        ("5",      mp.mpf(5)),
        ("10",     mp.mpf(10)),
        ("20",     mp.mpf(20)),
        ("50",     mp.mpf(50)),
        ("100",    mp.mpf(100)),
    ]
    # N ladder -- be honest about cost
    N_by_lam = {
        "sqrt13": [40, 60, 80, 120, 160],
        "5":      [40, 60, 80, 120, 160],
        "10":     [40, 60, 80, 120, 160],
        "20":     [40, 60, 80, 120, 160],
        "50":     [40, 60, 80, 120],
        "100":    [40, 60, 80],
    }
    results = {}
    for label, lam in lam_list:
        results[label] = {"lam": mp.nstr(lam, 20), "runs": []}
        prev_xi0 = None
        for N in N_by_lam[label]:
            t0 = time.time()
            try:
                r = solve_even_ground(lam, N)
            except Exception as e:
                results[label]["runs"].append({"N": N, "error": repr(e)})
                print(f"  λ={label} N={N} FAIL {e}")
                continue
            wall = time.time() - t0
            xi0 = r["xi_even"][0]
            xi_j = [mp.nstr(r["xi_even"][j], 14) for j in range(min(6, N+1))]
            entry = {
                "N": N,
                "wall_s": wall,
                "chi0": r["chi0"],
                "eps": mp.nstr(r["eps"], 8),
                "eps2": mp.nstr(r["eps2"], 8),
                "gap": mp.nstr(r["eps2"] - r["eps"], 8),
                "xi_j": xi_j,
                "xi0_float": float(xi0),
            }
            results[label]["runs"].append(entry)
            print(f"  λ={label} N={N:3d} wall={wall:5.1f}s χ0={r['chi0']:.4f} "
                  f"ε={mp.nstr(r['eps'],4)} gap={mp.nstr(r['eps2']-r['eps'],4)} "
                  f"ξ0={float(xi0):+.6e}")
            prev_xi0 = xi0
        # Determine N_converged: smallest N where ξ0 and ξ_{0..5} agree with
        # the best (largest-N) run to some tolerance
        runs = [r for r in results[label]["runs"] if "xi_j" in r]
        if len(runs) >= 2:
            best = runs[-1]
            def agrees(run, tol=1e-3):
                try:
                    for j in range(min(len(best["xi_j"]), len(run["xi_j"]))):
                        a = float(mp.mpf(best["xi_j"][j]))
                        b = float(mp.mpf(run["xi_j"][j]))
                        if abs(a-b) > tol * max(1.0, abs(a)):
                            return False
                    return True
                except Exception:
                    return False
            Nc = None
            for r in runs:
                if agrees(r):
                    Nc = r["N"]; break
            results[label]["N_converged"] = Nc
            results[label]["best_N"] = best["N"]
        else:
            results[label]["N_converged"] = None
    return results

# ---------------------------------------------------------------------------
# Sub-experiment 2: Scenario C direct test via ξ̂_λ(z)
# ---------------------------------------------------------------------------
def xi_hat(z, xi_even, L):
    """ξ̂_λ(z) = 2 L^{-1/2} sin(zL/2) Σ_j ξ_j / (z - 2πj/L).

    Here ξ_even is a length N+1 vector in the orthonormal even basis e_j.
    The positions are 2πj/L for j=0..N (even basis labels j).
    Near a pole (z = 2πj/L) sin(zL/2) vanishes, giving finite limit.
    Use full precision mpmath.
    """
    z = mp.mpc(z)
    L = mp.mpf(L)
    total = mp.mpc(0)
    # Treat the j=0 term: position 0; sin(zL/2)/z is entire
    # For generic z:
    # We need to watch for exact hit to a pole at 2πj/L. Use limit via L'Hopital if needed.
    two_pi = 2*mp.pi
    sinz = mp.sin(z*L/2)
    for j, xj in enumerate(xi_even):
        pole = two_pi*j/L
        denom = z - pole
        if abs(denom) < mp.mpf("1e-30"):
            # sin(zL/2) at z = 2πj/L equals sin(πj) = 0; L'Hopital:
            # lim (sin(zL/2))/(z-pole) = (L/2) cos(πj) = (L/2)(-1)^j
            term = xj * (L/2) * ((-1)**j)
            total += 2 * mp.power(L, mp.mpf(-1)/2) * term
        else:
            total += xj / denom
    if abs(total) > 0 and not (abs(denom) < mp.mpf("1e-30")):
        return 2 * mp.power(L, mp.mpf(-1)/2) * sinz * total
    # If we had a pole case, total already absorbed it plus other j terms — redo cleanly:
    # Re-do more carefully: separate pole terms from regular terms
    total = mp.mpc(0)
    for j, xj in enumerate(xi_even):
        pole = two_pi*j/L
        denom = z - pole
        if abs(denom) < mp.mpf("1e-30"):
            # contribution from this term is xj * (L/2)*(-1)^j, and needs the 2 L^{-1/2} prefactor
            total += xj * (L/2) * ((-1)**j)  # but without sin factor — it's already the limit
        else:
            total += sinz * xj / denom
    return 2 * mp.power(L, mp.mpf(-1)/2) * total


def sub2_scenario_C(trustworthy):
    """trustworthy: dict label -> (lam, N, xi_even, L)"""
    z_points = {
        "z=0":       mp.mpc(0, 0),
        "z=i*gamma1": mp.mpc(0, mp.mpf("14.1347251417346937904572519836")),
        "z=i*gamma2": mp.mpc(0, mp.mpf("21.0220396387715549926284795938")),
        "z=i*gamma3": mp.mpc(0, mp.mpf("25.0108575801456887632137909925")),
        "z=1+0.5i":  mp.mpc(1, mp.mpf("0.5")),
    }
    table = {}
    for zname, z in z_points.items():
        table[zname] = {}
        for label, (lam, N, xi_even, L) in trustworthy.items():
            val = xi_hat(z, xi_even, L)
            table[zname][label] = {
                "lam": float(lam),
                "re": float(mp.re(val)),
                "im": float(mp.im(val)),
                "abs": float(mp.fabs(val)),
            }
    return table

# ---------------------------------------------------------------------------
# Sub-experiment 3: boundary values
# ---------------------------------------------------------------------------
def boundary_value(xi_even, L):
    """Compute |ξ_λ(x=0)| and |ξ_λ(x=L)| where
        ξ_λ(x) = Σ_j ξ_j e_j(x),
    with e_0 = 1/√L, e_j = √(2/L) cos(2πj x /L) for j>=1 (even basis on [0,L])
    (these are the standard orthonormal cosine basis on [0,L]; V_n + V_{-n})/√2
    = √(2/L) cos(2πn x/L) in the Fourier convention of the module).

    At x=0: e_0 = 1/√L, e_j = √(2/L). At x=L: e_j(L) = √(2/L) cos(2πj)=√(2/L).
    Both endpoints give the same value by evenness.
    ξ_λ(0) = (1/√L) ξ_0 + √(2/L) Σ_{j>=1} ξ_j.
    """
    L = mp.mpf(L)
    s = xi_even[0] / mp.sqrt(L)
    s2 = mp.mpf(0)
    for j in range(1, len(xi_even)):
        s2 += xi_even[j]
    s += mp.sqrt(2/L) * s2
    return s  # boundary value at x=0 (equals at x=L by evenness)

def sub3_boundary(trustworthy):
    rows = []
    for label, (lam, N, xi_even, L) in trustworthy.items():
        bv = boundary_value(xi_even, L)
        rows.append({
            "label": label,
            "lam": float(lam),
            "L": float(L),
            "bv": float(bv),
            "abs_bv": float(mp.fabs(bv)),
            "log_lam": float(mp.log(lam)),
            "log_abs_bv": float(mp.log(mp.fabs(bv) + mp.mpf("1e-300"))),
        })
    # Power-law fit |bv| ~ C λ^{-β}  =>  log|bv| = log C - β log λ
    xs = np.array([r["log_lam"] for r in rows])
    ys = np.array([r["log_abs_bv"] for r in rows])
    if len(xs) >= 2:
        # Linear fit
        A = np.vstack([xs, np.ones_like(xs)]).T
        sol, res, rank, sv = np.linalg.lstsq(A, ys, rcond=None)
        slope, intercept = sol
        beta = -slope
        # Residual-based stderr
        yhat = A @ sol
        resid = ys - yhat
        dof = max(1, len(xs) - 2)
        sigma2 = float(np.sum(resid**2) / dof)
        cov = sigma2 * np.linalg.inv(A.T @ A)
        beta_err = float(np.sqrt(cov[0,0]))
    else:
        beta = None; beta_err = None; intercept = None
    return rows, beta, beta_err, intercept

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    out = {}
    print("\n=== Sub-experiment 1: N-convergence ===", flush=True)
    sub1 = sub1_n_convergence()
    out["sub1_n_convergence"] = sub1

    # Build trustworthy set: pick best_N for each λ, store the full xi_even
    print("\n=== Building trustworthy set (best_N per λ) ===", flush=True)
    trustworthy = {}
    lam_map = {
        "sqrt13": mp.sqrt(13), "5": mp.mpf(5), "10": mp.mpf(10),
        "20": mp.mpf(20), "50": mp.mpf(50), "100": mp.mpf(100)
    }
    for label, entry in sub1.items():
        best_N = entry.get("best_N")
        if best_N is None:
            continue
        lam = lam_map[label]
        r = solve_even_ground(lam, best_N)
        trustworthy[label] = (lam, best_N, r["xi_even"], r["L"])
        print(f"  {label}: N={best_N}, L={float(r['L']):.4f}, "
              f"‖xi‖2≈{float(sum(x*x for x in r['xi_even']))**0.5:.4f}")

    print("\n=== Sub-experiment 2: Scenario C direct test ===", flush=True)
    sub2 = sub2_scenario_C(trustworthy)
    out["sub2_scenario_C"] = sub2
    for zname, tbl in sub2.items():
        print(f"  {zname}:")
        for label, v in sorted(tbl.items(), key=lambda kv: kv[1]["lam"]):
            print(f"    λ={label:8s} |ξ̂|={v['abs']:.6e}  re={v['re']:+.4e} im={v['im']:+.4e}")

    print("\n=== Sub-experiment 3: boundary decay ===", flush=True)
    rows, beta, beta_err, intercept = sub3_boundary(trustworthy)
    out["sub3_boundary"] = {
        "rows": rows, "beta": beta, "beta_err": beta_err, "intercept": intercept,
    }
    for r in sorted(rows, key=lambda x: x["lam"]):
        print(f"  λ={r['lam']:8.3f} L={r['L']:.3f} |ξ_λ(L)|={r['abs_bv']:.4e}")
    if beta is not None:
        print(f"  Power-law fit: β = {beta:.4f} ± {beta_err:.4f}")

    # ---- Plots ----
    # (2) |ξ̂_λ(z)| vs λ for each z
    fig, ax = plt.subplots(figsize=(8, 5))
    for zname, tbl in sub2.items():
        pts = sorted(tbl.items(), key=lambda kv: kv[1]["lam"])
        xs = [v[1]["lam"] for v in pts]
        ys = [v[1]["abs"] + 1e-300 for v in pts]
        ax.plot(xs, ys, marker="o", label=zname)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("λ"); ax.set_ylabel("|ξ̂_λ(z)|")
    ax.set_title("CS-2: Scenario C direct test")
    ax.legend(); ax.grid(True, alpha=0.3)
    fig.tight_layout()
    p2 = os.path.join(CODE_DIR, "cs2_scenario_C.png")
    fig.savefig(p2, dpi=120); plt.close(fig)

    # (3) boundary decay log-log
    fig, ax = plt.subplots(figsize=(8, 5))
    rs = sorted(rows, key=lambda x: x["lam"])
    lx = [r["log_lam"] for r in rs]
    ly = [r["log_abs_bv"] for r in rs]
    ax.plot(lx, ly, "o-", label="data")
    if beta is not None:
        xf = np.linspace(min(lx), max(lx), 30)
        yf = intercept - beta * xf
        ax.plot(xf, yf, "--", label=f"fit: β={beta:.3f}±{beta_err:.3f}")
    ax.set_xlabel("log λ"); ax.set_ylabel("log |ξ_λ(boundary)|")
    ax.set_title("CS-2: boundary value decay")
    ax.legend(); ax.grid(True, alpha=0.3)
    fig.tight_layout()
    p3 = os.path.join(CODE_DIR, "cs2_boundary_decay.png")
    fig.savefig(p3, dpi=120); plt.close(fig)

    # (1) N-convergence: ξ_0 vs N for each λ
    fig, ax = plt.subplots(figsize=(8, 5))
    for label, entry in sub1.items():
        Ns = [r["N"] for r in entry["runs"] if "xi0_float" in r]
        ys = [r["xi0_float"] for r in entry["runs"] if "xi0_float" in r]
        ax.plot(Ns, ys, marker="o", label=f"λ={label}")
    ax.set_xlabel("N"); ax.set_ylabel("ξ_0")
    ax.set_title("CS-2: N-convergence of ξ_0")
    ax.legend(); ax.grid(True, alpha=0.3)
    fig.tight_layout()
    p1 = os.path.join(CODE_DIR, "cs2_n_convergence.png")
    fig.savefig(p1, dpi=120); plt.close(fig)

    out["plots"] = [p1, p2, p3]
    with open(os.path.join(CODE_DIR, "cs2_full_evaluation.json"), "w") as f:
        json.dump(out, f, indent=2, default=str)
    print("\nDone. JSON + plots saved.")

if __name__ == "__main__":
    main()
