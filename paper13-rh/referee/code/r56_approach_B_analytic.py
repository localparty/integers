"""R56 -- Approach B: Analytic perturbation theory for even-sector simplicity.

Track lambda_1(t) and lambda_2(t) as functions of t = log(lambda) for
lambda from 2 to 100 at N = 10. Tabulate the gap delta^ev = lambda_2 - lambda_1.

Investigates whether eigenvalue crossings exist via Kato-Rellich theory.
"""

import json
import os
import sys
import time
import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import build_QW, eigh_mp
from r51b_evenblock import project_to_even


def scan_gap_vs_lambda(N, lam_values, dps=50):
    """For each lambda, build QW, project to even sector, compute gap."""
    results = []
    for lam_val in lam_values:
        mp.mp.dps = dps
        lam = mp.mpf(lam_val)
        t_param = float(mp.log(lam))
        try:
            A, L = build_QW(lam, N, dps=dps, verbose=False)
            Aev = project_to_even(A, N)
            vals_ev, _ = eigh_mp(Aev)
            mu1 = vals_ev[0]
            mu2 = vals_ev[1]
            mu3 = vals_ev[2] if len(vals_ev) > 2 else None
            delta = mu2 - mu1
            delta12 = None
            if mu3 is not None:
                delta12 = mu3 - mu2
            results.append({
                "lam": float(lam_val),
                "t": t_param,
                "mu1": float(mu1),
                "mu2": float(mu2),
                "mu3": float(mu3) if mu3 is not None else None,
                "delta_01": float(delta),
                "delta_12": float(delta12) if delta12 is not None else None,
                "log10_delta_01": float(mp.log10(delta)) if delta > 0 else None,
            })
            print(f"  lam={lam_val:8.3f}  t={t_param:.4f}  "
                  f"mu1={float(mu1):+.6e}  mu2={float(mu2):+.6e}  "
                  f"gap={float(delta):.3e}")
        except Exception as e:
            print(f"  lam={lam_val:8.3f}  FAILED: {e}")
            results.append({"lam": float(lam_val), "t": t_param, "error": str(e)})
    return results


def compute_derivatives(results):
    """Finite differences for dmu1/dt, dmu2/dt."""
    for i in range(1, len(results) - 1):
        if "error" in results[i] or "error" in results[i-1] or "error" in results[i+1]:
            continue
        dt_fwd = results[i+1]["t"] - results[i]["t"]
        dt_bwd = results[i]["t"] - results[i-1]["t"]
        dt = (dt_fwd + dt_bwd) / 2
        results[i]["dmu1_dt"] = (results[i+1]["mu1"] - results[i-1]["mu1"]) / (2 * dt)
        results[i]["dmu2_dt"] = (results[i+1]["mu2"] - results[i-1]["mu2"]) / (2 * dt)
    return results


def main():
    N = 10
    dps = 50

    # Lambda values: from 2 to 100 in ~40 steps
    lam_values = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0,
                  9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 25.0,
                  30.0, 35.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]

    print(f"R56 -- Approach B: Analytic perturbation theory")
    print(f"N = {N}, dps = {dps}")
    print(f"Scanning {len(lam_values)} lambda values from {lam_values[0]} to {lam_values[-1]}")
    print()

    t0 = time.time()
    results = scan_gap_vs_lambda(N, lam_values, dps=dps)
    results = compute_derivatives(results)
    elapsed = time.time() - t0

    # Summary statistics
    gaps = [r["delta_01"] for r in results if "error" not in r]
    min_gap = min(gaps)
    max_gap = max(gaps)
    min_gap_lam = [r["lam"] for r in results if "error" not in r and r["delta_01"] == min_gap][0]

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  N = {N}")
    print(f"  Lambda range: [{lam_values[0]}, {lam_values[-1]}]")
    print(f"  Min gap: {min_gap:.6e} at lambda = {min_gap_lam}")
    print(f"  Max gap: {max_gap:.6e}")
    print(f"  All gaps positive: {all(g > 0 for g in gaps)}")
    print(f"  Elapsed: {elapsed:.1f}s")

    # Check monotonicity of gap
    gap_increasing = all(gaps[i+1] >= gaps[i] for i in range(len(gaps)-1))
    gap_decreasing = all(gaps[i+1] <= gaps[i] for i in range(len(gaps)-1))
    print(f"  Gap monotone increasing: {gap_increasing}")
    print(f"  Gap monotone decreasing: {gap_decreasing}")

    # Check derivative separation
    deriv_rows = [r for r in results if "dmu1_dt" in r]
    if deriv_rows:
        always_separated = all(r["dmu1_dt"] < r["dmu2_dt"] for r in deriv_rows)
        print(f"  dmu1/dt < dmu2/dt always: {always_separated}")

    # Tabulate
    print()
    print(f"{'lam':>8s}  {'t':>7s}  {'mu1':>13s}  {'mu2':>13s}  "
          f"{'gap':>10s}  {'log10gap':>9s}  {'dmu1/dt':>10s}  {'dmu2/dt':>10s}")
    for r in results:
        if "error" in r:
            print(f"{r['lam']:>8.2f}  ERROR")
            continue
        dm1 = f"{r['dmu1_dt']:+.3e}" if "dmu1_dt" in r else "    --"
        dm2 = f"{r['dmu2_dt']:+.3e}" if "dmu2_dt" in r else "    --"
        lg = f"{r['log10_delta_01']:+.2f}" if r.get("log10_delta_01") is not None else "   --"
        print(f"{r['lam']:>8.2f}  {r['t']:>7.4f}  {r['mu1']:+.6e}  {r['mu2']:+.6e}  "
              f"{r['delta_01']:>10.3e}  {lg:>9s}  {dm1:>10s}  {dm2:>10s}")

    out = {
        "N": N, "dps": dps,
        "results": results,
        "min_gap": min_gap,
        "min_gap_lam": min_gap_lam,
        "max_gap": max_gap,
        "all_gaps_positive": all(g > 0 for g in gaps),
        "gap_monotone_increasing": gap_increasing,
        "gap_monotone_decreasing": gap_decreasing,
        "elapsed_s": elapsed,
    }
    out_path = os.path.join(CODE_DIR, "r56_approach_B_analytic.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nJSON -> {out_path}")


if __name__ == "__main__":
    main()
