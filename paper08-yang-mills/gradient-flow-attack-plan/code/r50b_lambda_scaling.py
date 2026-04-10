"""R50B — λ-scaling of ε_λ (smallest eigenvalue of Q_W^{λ,N}) and the
γ_n rel-errs via the ξ̂ pipeline, the empirical companion to R50A.

The empirical half of CC1 Cor 3.8: does ε_λ → 0 as λ → ∞?

Strategy: REUSE the R49 builder verbatim — `build_QW`, `eigh_mp`,
`parity_projector_indices`, `parity_score`, `commutator_norm`,
`xi_hat`, `find_xi_hat_zero_near`, `GAMMAS_50DIG`. Sweep λ over a
configurable list, with (N_modes, dps) chosen per-λ to keep cost
tractable while still resolving ε_λ down to a small precision floor.

Output:
  code/r50b_lambda_scaling.json   — full results table
  research/104-r50b-lambda-scaling.md — written manually from JSON

CLI:
  python r50b_lambda_scaling.py [--quick|--full|--demo]

  --demo  : λ ∈ {√13, 5, 10}                  (smoke test, ~minutes)
  --quick : λ ∈ {√13, 5, 10, 20, 40}          (default; ~tens of minutes)
  --full  : λ ∈ {√13, 5, 10, 20, 40, 80, 160, 320, 1000}
            (intended; cost grows like N^3 + #primes·N)

Per-λ schedule (N_modes, K_max, dps):
  λ ≤ 10  : N=120, dps=110, K_max = floor(λ²)        (matches R49)
  λ = 20  : N=140, dps=100, K_max = 400
  λ = 40  : N=180, dps= 90, K_max = 1600
  λ = 80  : N=220, dps= 80, K_max = 6400
  λ = 160 : N=260, dps= 70, K_max = 25600
  λ = 320 : N=300, dps= 60, K_max = 102400
  λ = 1000: N=360, dps= 50, K_max = 1_000_000

Cost-dominant operations:
  - build_W02 : O(N²) trivial closed form
  - precompute_abc : 2N quadratures (each O(dps^?·iters)), DOMINANT for large dps
  - build_WR : O(N²)
  - build_Wprimes : O(N²·#primes)  ←  dominant for very large λ
  - eigh_mp : O(N³) at the active dps  ←  dominant for large N

We log each piece's runtime so the precision/cost tradeoff is documented.
"""

import json
import os
import sys
import time
import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

# Reuse the R49 builder verbatim.
from r49_fourier_circle import (
    GAMMAS_50DIG,
    build_QW,
    eigh_mp,
    parity_projector_indices,
    parity_score,
    commutator_norm,
    xi_hat,
    find_xi_hat_zero_near,
)


# (label, lam_factory, N_modes, dps)
SCHEDULE_FULL = [
    ("sqrt13", lambda: mp.sqrt(13), 120, 110),
    ("5",      lambda: mp.mpf(5),   120, 110),
    ("10",     lambda: mp.mpf(10),  120, 110),
    ("20",     lambda: mp.mpf(20),  140, 100),
    ("40",     lambda: mp.mpf(40),  180,  90),
    ("80",     lambda: mp.mpf(80),  220,  80),
    ("160",    lambda: mp.mpf(160), 260,  70),
    ("320",    lambda: mp.mpf(320), 300,  60),
    ("1000",   lambda: mp.mpf(1000),360,  50),
]

SCHEDULE_QUICK = SCHEDULE_FULL[:5]
SCHEDULE_DEMO  = SCHEDULE_FULL[:3]


def run_one(label, lam_factory, N, dps, n_gammas=3, verbose=True):
    """Run a single λ point. Returns a dict (JSON-safe)."""
    print()
    print("#" * 76)
    print(f"#  λ = {label}    N = {N}    dps = {dps}")
    print("#" * 76)
    mp.mp.dps = dps
    lam = lam_factory()
    L_dbg = 2 * mp.log(lam)
    print(f"  L = 2 log λ = {float(L_dbg):.6f}")

    t_total0 = time.time()
    try:
        A, L = build_QW(lam, N, dps=dps, verbose=verbose)
    except Exception as e:
        return {
            "label": label, "lam": str(lam), "N": N, "dps": dps,
            "error": f"build_QW failed: {e}",
        }
    t_build = time.time() - t_total0

    pair = parity_projector_indices(N)

    print("  diagonalising QW_λ^N ...")
    t_e0 = time.time()
    try:
        vals, Q = eigh_mp(A)
    except Exception as e:
        return {
            "label": label, "lam": str(lam), "N": N, "dps": dps,
            "build_time": t_build,
            "error": f"eigh_mp failed: {e}",
        }
    t_eig = time.time() - t_e0
    print(f"  diagonalisation done [{t_eig:.1f}s]")

    eps_lam = vals[0]
    gap01 = vals[1] - vals[0]
    chi0 = parity_score(Q.column(0), pair)
    chi1 = parity_score(Q.column(1), pair)

    # Commutator norm of P_par with the matrix — should be at the precision
    # floor (the basis is exactly parity-symmetric).
    try:
        cn = commutator_norm(A, pair)
        cn_str = mp.nstr(cn, 6)
    except Exception as e:
        cn_str = f"err:{e}"

    print(f"  ε_λ = {mp.nstr(eps_lam, 30)}")
    print(f"  gap = {mp.nstr(gap01, 12)}")
    print(f"  parity(ξ_0) = {chi0:+.6f}    parity(ξ_1) = {chi1:+.6f}")
    print(f"  ‖[A,P_par]‖_F = {cn_str}")

    # ξ̂ pipeline: γ_1, γ_2, γ_3 rel errs.
    xi = [Q[i, 0] for i in range(2 * N + 1)]

    gamma_rows = []
    for k in range(n_gammas):
        gk = mp.mpf(GAMMAS_50DIG[k])
        try:
            zk = find_xi_hat_zero_near(gk, xi, L, N)
            rel = abs(zk - gk) / gk
            rel_f = float(rel) if rel > 0 else 0.0
            log10rel = float(mp.log10(rel)) if rel > 0 else None
            gamma_rows.append({
                "n": k + 1,
                "gamma": str(gk),
                "zero": str(zk),
                "rel_err": str(rel),
                "rel_err_float": rel_f,
                "log10_rel_err": log10rel,
            })
            print(f"  γ_{k+1}: rel_err = {rel_f:.3e}")
        except Exception as e:
            gamma_rows.append({"n": k + 1, "gamma": str(gk),
                               "error": str(e)})
            print(f"  γ_{k+1}: findroot failed: {e}")

    # ξ̂ even-parity numerical check.
    z_test = mp.mpf("3.7")
    try:
        f_p = xi_hat(z_test, xi, L, N)
        f_n = xi_hat(-z_test, xi, L, N)
        denom = max(abs(f_p), abs(f_n), mp.mpf("1e-300"))
        xihat_par_resid = float((f_p - f_n) / denom)
    except Exception as e:
        xihat_par_resid = None

    t_total = time.time() - t_total0
    print(f"  TOTAL [{t_total:.1f}s]   build={t_build:.1f}s   eigh={t_eig:.1f}s")

    return {
        "label": label,
        "lam": str(lam),
        "L": float(L),
        "N": N,
        "dps": dps,
        "eps_lam": str(eps_lam),
        "eps_lam_float": float(eps_lam),
        "log10_abs_eps_lam": (float(mp.log10(abs(eps_lam)))
                              if abs(eps_lam) > 0 else None),
        "gap01": str(gap01),
        "gap01_float": float(gap01),
        "parity_xi0": chi0,
        "parity_xi1": chi1,
        "commutator_fro": cn_str,
        "xihat_parity_residual": xihat_par_resid,
        "gamma_rows": gamma_rows,
        "build_time_s": t_build,
        "eigh_time_s": t_eig,
        "total_time_s": t_total,
    }


def ascii_plot_eps(rows):
    """Tiny ASCII plot of log10|ε_λ| versus log10 λ."""
    pts = []
    for r in rows:
        if "error" in r: continue
        if r.get("log10_abs_eps_lam") is None: continue
        lam_f = float(mp.mpf(r["lam"]))
        pts.append((mp.log10(lam_f), r["log10_abs_eps_lam"], r["label"]))
    if not pts: return "(no points)"
    xmin, xmax = min(p[0] for p in pts), max(p[0] for p in pts)
    ymin, ymax = min(p[1] for p in pts), max(p[1] for p in pts)
    if xmax == xmin: xmax = xmin + 1
    if ymax == ymin: ymax = ymin + 1
    W, H = 60, 18
    grid = [[" "] * W for _ in range(H)]
    for (x, y, lab) in pts:
        ix = int((float(x) - float(xmin)) / float(xmax - xmin) * (W - 1))
        iy = int((float(y) - float(ymin)) / float(ymax - ymin) * (H - 1))
        iy = H - 1 - iy
        grid[iy][ix] = "*"
    lines = ["".join(row) for row in grid]
    out = []
    out.append(f"log10|ε_λ|  vs  log10 λ   "
               f"(y∈[{float(ymin):.1f},{float(ymax):.1f}], "
               f"x∈[{float(xmin):.2f},{float(xmax):.2f}])")
    for line in lines:
        out.append("| " + line + " |")
    out.append("+" + "-" * (W + 2) + "+")
    return "\n".join(out)


def parse_args():
    if len(sys.argv) < 2:
        return SCHEDULE_QUICK, "quick"
    a = sys.argv[1]
    if a == "--full":  return SCHEDULE_FULL,  "full"
    if a == "--quick": return SCHEDULE_QUICK, "quick"
    if a == "--demo":  return SCHEDULE_DEMO,  "demo"
    print(f"unknown arg {a}; using --quick")
    return SCHEDULE_QUICK, "quick"


def main():
    schedule, mode = parse_args()
    print("=" * 76)
    print(f"R50B — λ scaling of ε_λ (mode = {mode})")
    print(f"  schedule: {[s[0] for s in schedule]}")
    print("=" * 76)

    rows = []
    t0 = time.time()
    for (label, factory, N, dps) in schedule:
        try:
            r = run_one(label, factory, N, dps, n_gammas=3, verbose=False)
        except Exception as e:
            r = {"label": label, "N": N, "dps": dps,
                 "error": f"top-level exception: {e}"}
        rows.append(r)
        # Persist after every λ so we don't lose work.
        out = {"mode": mode, "rows": rows,
               "elapsed_s_so_far": time.time() - t0}
        with open(os.path.join(CODE_DIR, "r50b_lambda_scaling.json"), "w") as f:
            json.dump(out, f, indent=2, default=str)

    print()
    print("=" * 76)
    print("SUMMARY")
    print("=" * 76)
    print(f"{'label':>8}  {'N':>4}  {'dps':>4}  {'L':>8}  "
          f"{'log10|eps|':>12}  {'parity':>8}  "
          f"{'log10 g1':>10}  {'log10 g2':>10}  {'log10 g3':>10}  {'time(s)':>9}")
    for r in rows:
        if "error" in r:
            print(f"{r.get('label','?'):>8}  ERROR: {r['error']}")
            continue
        gs = r["gamma_rows"]
        def lg(k):
            if k >= len(gs): return "  --"
            row = gs[k]
            if "log10_rel_err" in row and row["log10_rel_err"] is not None:
                return f"{row['log10_rel_err']:+10.2f}"
            return "    --"
        print(f"{r['label']:>8}  {r['N']:>4}  {r['dps']:>4}  "
              f"{r['L']:8.4f}  "
              f"{(r['log10_abs_eps_lam'] if r['log10_abs_eps_lam'] is not None else 0):>12.2f}  "
              f"{r['parity_xi0']:>+8.4f}  "
              f"{lg(0)}  {lg(1)}  {lg(2)}  "
              f"{r['total_time_s']:>9.1f}")

    print()
    print(ascii_plot_eps(rows))

    print()
    print(f"Total elapsed: {time.time() - t0:.1f}s")
    print(f"JSON -> {os.path.join(CODE_DIR, 'r50b_lambda_scaling.json')}")


if __name__ == "__main__":
    main()
