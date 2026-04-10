"""CS-3 precision diagnostic (round-10).

Goal: at dps=200, can we resolve the lowest two even eigenvalues of Q_W^{λ,N}?

If yes → CS-1.5/CS-2's "near-degenerate ground state" finding was a precision-floor
artifact, and the proper move is the full-sweep cs3_high_precision.py at dps=200.

If no → there is a real (or near-real) multiplicity in the lowest even eigenspace,
and the program needs reframing.

Trimmed N ladder, dps=200:
  - λ ∈ {sqrt13, 5, 10, 20, 50, 100} at the largest N each previously ran
  - Plus an extra (λ=20, N=80) sanity check matching where CS-1.5 caught the bug
  - Plus an extra (λ=20, N=120) to confirm convergence at the diagnostic point

Writes results to cs3_diagnostic.json and prints progress to stdout.
"""

import json, os, sys, time
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cs3_high_precision import solve_even_ground

CODE_DIR = os.path.dirname(os.path.abspath(__file__))

# Trimmed ladder: just the diagnostic points
RUNS = [
    ("sqrt13", mp.sqrt(13), 160),
    ("5",      mp.mpf(5),   160),
    ("10",     mp.mpf(10),  160),
    ("20",     mp.mpf(20),   80),   # the original bug point
    ("20",     mp.mpf(20),  120),   # confirm convergence at λ=20
    ("50",     mp.mpf(50),  120),
    ("100",    mp.mpf(100),  80),
]

def main():
    out = {"runs": [], "dps": 200, "started": time.time()}
    print(f"\n=== CS-3 PRECISION DIAGNOSTIC at dps=200 ===", flush=True)
    print(f"  {len(RUNS)} runs planned\n", flush=True)
    for label, lam, N in RUNS:
        t0 = time.time()
        try:
            r = solve_even_ground(lam, N, dps=200)
        except Exception as e:
            entry = {"label": label, "N": N, "error": repr(e),
                     "wall_s": time.time() - t0}
            out["runs"].append(entry)
            print(f"  λ={label} N={N} FAIL {e}", flush=True)
            continue
        wall = time.time() - t0
        eps = r["eps"]
        eps2 = r["eps2"]
        gap = eps2 - eps if eps2 is not None else None
        # Compute the numerical "distinguishability" — log10(eps2-eps) tells us how
        # many digits of precision we'd need to see the gap
        gap_str = mp.nstr(gap, 12) if gap is not None else "N/A"
        eps_str = mp.nstr(eps, 12)
        eps2_str = mp.nstr(eps2, 12) if eps2 is not None else "N/A"
        log10_gap = float(mp.log10(abs(gap))) if gap is not None and gap != 0 else None
        log10_eps = float(mp.log10(abs(eps))) if eps != 0 else None
        entry = {
            "label": label, "lam": float(lam), "N": N,
            "wall_s": wall,
            "chi0": r["chi0"],
            "eps": eps_str, "eps2": eps2_str, "gap": gap_str,
            "log10_eps": log10_eps, "log10_gap": log10_gap,
            "L": float(r["L"]),
        }
        out["runs"].append(entry)
        print(
            f"  λ={label:8s} N={N:3d} wall={wall:6.1f}s "
            f"χ0={r['chi0']:+.4f}  ε={eps_str}  gap={gap_str}",
            flush=True,
        )
        # Save incrementally so we don't lose work if interrupted
        with open(os.path.join(CODE_DIR, "cs3_diagnostic.json"), "w") as f:
            json.dump(out, f, indent=2, default=str)
    out["finished"] = time.time()
    out["total_wall_s"] = out["finished"] - out["started"]
    with open(os.path.join(CODE_DIR, "cs3_diagnostic.json"), "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nDone. Total wall: {out['total_wall_s']:.1f}s", flush=True)
    print("Results saved to cs3_diagnostic.json", flush=True)

if __name__ == "__main__":
    main()
