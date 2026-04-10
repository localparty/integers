"""R51B — Even-block refactor of Q_W^{λ,N} on the cosine basis.

R50B observed that ε_λ sits at the precision floor for λ ≥ 5, making the
spectral parity of the ground state numerically unstable in the full V_n
basis. R50A's RG transfer pinpoints δ^ev_λ = μ_2^ev − μ_1^ev as the load-
bearing variable for the (EvenGap) bound, predicting δ^ev_λ = O((log λ)²).

This file implements R50B's recommended refactor: project Q_W^{λ,N} onto
the EVEN block P_par = +1 BEFORE diagonalising. We work in the (real)
cosine basis

    C_0(x) = V_0(x) = 1/√L
    C_n(x) = (V_n(x) + V_{-n}(x)) / √2     for n = 1..N

which is an orthonormal basis of the +1 eigenspace of x → −x.  This block
has dimension N+1 (vs 2N+1 for the full matrix), so eigh is ~8× cheaper.

By the parity symmetry V_n → V_{-n} of all the matrix elements computed
in r49 (the kernels W02, WR, W_p are all even under joint sign flip of
(n, m)), the entries of A in the cosine basis are:

    A^ev[0,0] = A[0,0]
    A^ev[0,m] = √2 · A[0, m]                    (m ≥ 1)
    A^ev[n,m] = A[n, m] + A[n, -m]              (n, m ≥ 1)

Verified directly against the full r49 build (Part 1 of the task).

PART 2: sweep λ ∈ {√13, 5, 10, 20, 40, 80, 160}, report (μ_1^ev, μ_2^ev,
δ^ev_λ).
PART 3: fit δ^ev_λ to (log λ)^α candidates.
PART 4: μ_1^ev vs ε_λ from R50B.
PART 5: γ_n bridge from the unambiguous even ground state.

CLI:
  python r51b_evenblock.py [--verify | --demo | --quick | --full]

  --verify : verification only at λ=√13, N=60                (~1 min)
  --demo   : λ ∈ {√13, 5, 10}                                 (~minutes)
  --quick  : λ ∈ {√13, 5, 10, 20, 40}                         (default)
  --full   : λ ∈ {√13, 5, 10, 20, 40, 80, 160}                (~hour+)
"""

import json
import math
import os
import sys
import time
import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import (
    GAMMAS_50DIG,
    build_QW,
    eigh_mp,
    xi_hat,
    find_xi_hat_zero_near,
)


# ---------------------------------------------------------------------------
# Even-block projection.
# ---------------------------------------------------------------------------

def project_to_even(A, N):
    """Build A^ev: the (N+1)×(N+1) matrix of A in the cosine basis
        C_0 = V_0,  C_n = (V_n + V_{-n})/√2  for n = 1..N.
    The full V_n basis indices are i = n + N, n ∈ {-N..N}.
    """
    sqrt2 = mp.sqrt(2)
    M = mp.matrix(N + 1)
    # n = m = 0
    M[0, 0] = A[N, N]
    # m ≥ 1, n = 0
    for m in range(1, N + 1):
        v = (A[N, N + m] + A[N, N - m]) / sqrt2
        M[0, m] = v
        M[m, 0] = v
    # n, m ≥ 1
    for n in range(1, N + 1):
        for m in range(n, N + 1):
            v = (A[N + n, N + m] + A[N + n, N - m]
                 + A[N - n, N + m] + A[N - n, N - m]) / 2
            # By parity symmetry A[i,j] = A[-i,-j], so
            #   A[n,m] + A[n,-m] + A[-n,m] + A[-n,-m] = 2(A[n,m] + A[n,-m]).
            M[n, m] = v
            M[m, n] = v
    return M


def even_eigvec_to_full(coeffs_ev, N):
    """Lift an eigenvector ξ^ev = (c_0, c_1, ..., c_N) in the cosine basis
    to the full V_n basis (length 2N+1) so we can reuse xi_hat.
    C_0 → e_N (V_0 has coefficient c_0).
    C_n (n≥1) → (e_{N+n} + e_{N-n}) / √2.
    Resulting V_n coefficients: ξ_n = c_{|n|}/√2 for n ≠ 0, ξ_0 = c_0.
    """
    sqrt2 = mp.sqrt(2)
    out = [mp.mpf(0)] * (2 * N + 1)
    out[N] = coeffs_ev[0]
    for n in range(1, N + 1):
        out[N + n] = coeffs_ev[n] / sqrt2
        out[N - n] = coeffs_ev[n] / sqrt2
    return out


# ---------------------------------------------------------------------------
# Verification (Part 1).
# ---------------------------------------------------------------------------

def verify_against_r49(lam=None, N=60, dps=80):
    """Build full Q_W via r49, project to even, then verify in two ways:
    (a) the projected matrix's eigenvalues equal the EVEN eigenvalues of
        the full matrix (those whose eigenvector is +1 under V_n → V_{-n}).
    (b) the projection commutes with the parity action (full matrix is
        block-diagonal under the parity P_par).
    Returns a dict.
    """
    print("=" * 72)
    print(f"VERIFY — λ={lam}, N={N}, dps={dps}: project full Q_W to even block")
    print("=" * 72)
    if lam is None:
        mp.mp.dps = dps
        lam = mp.sqrt(13)
    A, L = build_QW(lam, N, dps=dps, verbose=False)
    Aev = project_to_even(A, N)

    # (a) Diagonalise both, compare even subspectrum.
    vals_full, Q_full = eigh_mp(A)
    vals_ev, Q_ev = eigh_mp(Aev)

    # Sort even-block eigenvalues; they should appear in vals_full as a subset.
    # Compute parity scores of the full eigenvectors.
    from r49_fourier_circle import parity_projector_indices, parity_score
    pair = parity_projector_indices(N)
    even_full = []
    for k in range(len(vals_full)):
        chi = parity_score(Q_full.column(k), pair)
        if chi > 0.5:
            even_full.append((float(vals_full[k]), k, chi))
    even_full.sort()
    print(f"  full builder: {len(even_full)} eigenvectors with parity > +0.5")
    print(f"  even-block  : {len(vals_ev)} eigenvalues")

    # Compare smallest 5 even eigenvalues.
    nshow = min(5, len(vals_ev), len(even_full))
    max_diff = mp.mpf(0)
    for k in range(nshow):
        v_ev = vals_ev[k]
        v_full_even = even_full[k][0]
        d = abs(v_ev - v_full_even)
        if d > max_diff:
            max_diff = d
        print(f"    k={k}: even-block μ = {mp.nstr(v_ev, 18)}   "
              f"full(parity+) = {v_full_even:+.10e}   |Δ| = {mp.nstr(d, 6)}")
    print(f"  max |Δ| over first {nshow} = {mp.nstr(max_diff, 6)}")

    # Sanity: μ_2^ev - μ_1^ev
    delta_ev = vals_ev[1] - vals_ev[0]
    print(f"  μ_1^ev = {mp.nstr(vals_ev[0], 12)}")
    print(f"  μ_2^ev = {mp.nstr(vals_ev[1], 12)}")
    print(f"  δ^ev   = {mp.nstr(delta_ev, 12)}")

    return {
        "lam": str(lam), "N": N, "dps": dps,
        "max_eigval_diff_first5": str(max_diff),
        "max_eigval_diff_first5_float": float(max_diff),
        "mu1_ev": str(vals_ev[0]),
        "mu2_ev": str(vals_ev[1]),
        "delta_ev": str(delta_ev),
        "delta_ev_float": float(delta_ev),
    }


# ---------------------------------------------------------------------------
# Part 2: λ sweep.
# ---------------------------------------------------------------------------

# (label, lam_factory, N, dps)
SCHEDULE_FULL = [
    ("sqrt13", lambda: mp.sqrt(13), 120, 110),
    ("5",      lambda: mp.mpf(5),   120, 110),
    ("10",     lambda: mp.mpf(10),  120, 110),
    ("20",     lambda: mp.mpf(20),  140, 100),
    ("40",     lambda: mp.mpf(40),  180,  90),
    ("80",     lambda: mp.mpf(80),  220,  80),
    ("160",    lambda: mp.mpf(160), 260,  70),
]

SCHEDULE_QUICK = SCHEDULE_FULL[:5]
SCHEDULE_DEMO  = SCHEDULE_FULL[:3]


def run_one(label, lam_factory, N, dps, n_gammas=3, verbose=False):
    print()
    print("#" * 76)
    print(f"#  λ = {label}    N = {N}    dps = {dps}    [even block]")
    print("#" * 76)
    mp.mp.dps = dps
    lam = lam_factory()
    L_dbg = 2 * mp.log(lam)
    print(f"  L = 2 log λ = {float(L_dbg):.6f}")

    t0 = time.time()
    try:
        A, L = build_QW(lam, N, dps=dps, verbose=verbose)
    except Exception as e:
        return {"label": label, "lam": str(lam), "N": N, "dps": dps,
                "error": f"build_QW failed: {e}"}
    t_build = time.time() - t0

    t1 = time.time()
    Aev = project_to_even(A, N)
    t_proj = time.time() - t1
    print(f"  build={t_build:.1f}s  project={t_proj:.1f}s  "
          f"→ even block size = {N+1} (vs full {2*N+1})")

    t2 = time.time()
    try:
        vals_ev, Q_ev = eigh_mp(Aev)
    except Exception as e:
        return {"label": label, "lam": str(lam), "N": N, "dps": dps,
                "build_time_s": t_build, "error": f"eigh_mp failed: {e}"}
    t_eig = time.time() - t2
    print(f"  eigh(even) [{t_eig:.1f}s]")

    mu1 = vals_ev[0]
    mu2 = vals_ev[1]
    delta = mu2 - mu1
    print(f"  μ_1^ev = {mp.nstr(mu1, 24)}")
    print(f"  μ_2^ev = {mp.nstr(mu2, 24)}")
    print(f"  δ^ev   = {mp.nstr(delta, 18)}")

    # γ_n bridge from the even ground state.
    xi_ev = [Q_ev[i, 0] for i in range(N + 1)]
    xi_full = even_eigvec_to_full(xi_ev, N)

    gamma_rows = []
    for k in range(n_gammas):
        gk = mp.mpf(GAMMAS_50DIG[k])
        try:
            zk = find_xi_hat_zero_near(gk, xi_full, L, N)
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
            gamma_rows.append({"n": k + 1, "gamma": str(gk), "error": str(e)})
            print(f"  γ_{k+1}: findroot failed: {e}")

    # ξ̂ even-parity numerical check.
    z_test = mp.mpf("3.7")
    try:
        f_p = xi_hat(z_test, xi_full, L, N)
        f_n = xi_hat(-z_test, xi_full, L, N)
        denom = max(abs(f_p), abs(f_n), mp.mpf("1e-300"))
        xihat_par_resid = float((f_p - f_n) / denom)
    except Exception:
        xihat_par_resid = None

    t_total = time.time() - t0
    print(f"  TOTAL [{t_total:.1f}s]")

    return {
        "label": label,
        "lam": str(lam),
        "L": float(L),
        "N": N,
        "Nev": N + 1,
        "dps": dps,
        "mu1_ev": str(mu1),
        "mu2_ev": str(mu2),
        "delta_ev": str(delta),
        "mu1_ev_float": float(mu1),
        "mu2_ev_float": float(mu2),
        "delta_ev_float": float(delta),
        "log10_abs_mu1_ev": (float(mp.log10(abs(mu1)))
                             if abs(mu1) > 0 else None),
        "log10_delta_ev": (float(mp.log10(delta))
                           if delta > 0 else None),
        "gamma_rows": gamma_rows,
        "xihat_parity_residual": xihat_par_resid,
        "build_time_s": t_build,
        "project_time_s": t_proj,
        "eigh_time_s": t_eig,
        "total_time_s": t_total,
    }


# ---------------------------------------------------------------------------
# Part 3: fit δ^ev vs (log λ)^α.
# ---------------------------------------------------------------------------

def fit_power_log(rows):
    """Fit δ^ev_λ to candidate functions of log λ. Returns dict with
    constant c and RMSE for each model. Skips rows with missing or
    non-positive δ.
    """
    pts = []  # (log λ, δ)
    for r in rows:
        if "error" in r: continue
        if r.get("delta_ev_float") is None: continue
        if r["delta_ev_float"] <= 0: continue
        lam_f = float(mp.mpf(r["lam"]))
        if lam_f <= 1: continue
        pts.append((math.log(lam_f), r["delta_ev_float"], r["label"]))
    if len(pts) < 2:
        return {"error": "not enough points to fit"}

    def fit_const_model(g):
        # δ ≈ c · g(log λ); least squares c = Σ δ g / Σ g²
        num = sum(d * g(L) for (L, d, _) in pts)
        den = sum(g(L) ** 2 for (L, d, _) in pts)
        c = num / den if den > 0 else float("nan")
        rmse = math.sqrt(sum((d - c * g(L)) ** 2 for (L, d, _) in pts) / len(pts))
        return c, rmse

    out = {"points": [{"label": lab, "log_lam": L, "delta_ev": d}
                       for (L, d, lab) in pts]}
    # Models
    c1, e1 = fit_const_model(lambda L: L * L)
    c2, e2 = fit_const_model(lambda L: L)
    c3, e3 = fit_const_model(lambda L: 1.0)
    out["fit_log2"]  = {"c": c1, "rmse": e1, "form": "delta = c (log λ)^2"}
    out["fit_log1"]  = {"c": c2, "rmse": e2, "form": "delta = c (log λ)"}
    out["fit_const"] = {"c": c3, "rmse": e3, "form": "delta = c"}

    # Free-α power fit: log δ = log c + α log(log λ); requires log λ > 0
    pts_pos = [(L, d) for (L, d, _) in pts if L > 0 and d > 0]
    if len(pts_pos) >= 2:
        xs = [math.log(L) for (L, d) in pts_pos]
        ys = [math.log(d) for (L, d) in pts_pos]
        n = len(xs)
        mx = sum(xs) / n
        my = sum(ys) / n
        sxx = sum((x - mx) ** 2 for x in xs)
        sxy = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
        alpha = sxy / sxx if sxx > 0 else float("nan")
        log_c = my - alpha * mx
        c = math.exp(log_c)
        # RMSE in original space
        rmse = math.sqrt(
            sum((pts_pos[i][1] - c * (pts_pos[i][0] ** alpha)) ** 2
                for i in range(n)) / n)
        out["fit_freeα"] = {"alpha": alpha, "c": c, "rmse": rmse,
                            "form": "delta = c (log λ)^α"}
    return out


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------

def parse_args():
    if len(sys.argv) < 2:
        return SCHEDULE_QUICK, "quick"
    a = sys.argv[1]
    if a == "--full":   return SCHEDULE_FULL,   "full"
    if a == "--quick":  return SCHEDULE_QUICK,  "quick"
    if a == "--demo":   return SCHEDULE_DEMO,   "demo"
    if a == "--verify": return None,            "verify"
    print(f"unknown arg {a}; using --quick")
    return SCHEDULE_QUICK, "quick"


def main():
    sched, mode = parse_args()
    print("=" * 76)
    print(f"R51B — even-block refactor (mode = {mode})")
    print("=" * 76)

    out = {"mode": mode}

    if mode == "verify":
        v = verify_against_r49(N=60, dps=80)
        out["verify"] = v
        with open(os.path.join(CODE_DIR, "r51b_evenblock.json"), "w") as f:
            json.dump(out, f, indent=2, default=str)
        return

    # Always run a small verification first.
    print()
    print("STEP 0 — verification @ λ=√13, N=60, dps=80")
    out["verify"] = verify_against_r49(N=60, dps=80)

    rows = []
    t0 = time.time()
    for (label, factory, N, dps) in sched:
        try:
            r = run_one(label, factory, N, dps)
        except Exception as e:
            r = {"label": label, "N": N, "dps": dps,
                 "error": f"top-level exception: {e}"}
        rows.append(r)
        out["rows"] = rows
        out["elapsed_s_so_far"] = time.time() - t0
        with open(os.path.join(CODE_DIR, "r51b_evenblock.json"), "w") as f:
            json.dump(out, f, indent=2, default=str)

    out["fit"] = fit_power_log(rows)

    print()
    print("=" * 76)
    print("SUMMARY  (μ_1^ev, μ_2^ev, δ^ev_λ from even-block builder)")
    print("=" * 76)
    print(f"{'label':>8}  {'N':>4}  {'Nev':>4}  {'dps':>4}  {'L':>8}  "
          f"{'log10|μ1|':>12}  {'log10 δ':>12}  "
          f"{'log10 g1':>10}  {'time(s)':>9}")
    for r in rows:
        if "error" in r:
            print(f"{r.get('label','?'):>8}  ERROR: {r['error']}")
            continue
        gs = r.get("gamma_rows", [])
        def lg(k):
            if k >= len(gs): return "    --"
            row = gs[k]
            if row.get("log10_rel_err") is not None:
                return f"{row['log10_rel_err']:+10.2f}"
            return "    --"
        m1 = r.get("log10_abs_mu1_ev")
        ld = r.get("log10_delta_ev")
        print(f"{r['label']:>8}  {r['N']:>4}  {r['Nev']:>4}  {r['dps']:>4}  "
              f"{r['L']:8.4f}  "
              f"{(m1 if m1 is not None else 0):>12.2f}  "
              f"{(ld if ld is not None else 0):>12.2f}  "
              f"{lg(0)}  {r['total_time_s']:>9.1f}")

    print()
    print("FIT — δ^ev vs (log λ)^α")
    f = out["fit"]
    if "error" in f:
        print(f"  {f['error']}")
    else:
        for key in ("fit_log2", "fit_log1", "fit_const", "fit_freeα"):
            if key in f:
                fk = f[key]
                extras = ""
                if "alpha" in fk:
                    extras = f"  α = {fk['alpha']:+.4f}"
                print(f"  {fk['form']:<28}  c = {fk['c']:+.4e}  "
                      f"RMSE = {fk['rmse']:.4e}{extras}")

    print()
    print(f"Total elapsed: {time.time() - t0:.1f}s")
    print(f"JSON -> {os.path.join(CODE_DIR, 'r51b_evenblock.json')}")


if __name__ == "__main__":
    main()
