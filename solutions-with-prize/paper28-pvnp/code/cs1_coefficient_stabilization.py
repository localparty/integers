"""CS-1 coefficient stabilization experiment.

For each λ in a list, build Q_W^{λ,N} via r49_fourier_circle, diagonalise,
extract the even ground state ξ in the V_n Fourier basis on [0, L]
(L = 2 log λ), and record ξ_j and L^{1/2} ξ_j for j ∈ {0..J_MAX}.

Because the V_n basis indexes n ∈ {-N..N} and the ground state is even,
the coefficient "ξ_j" of F5a means the real symmetric combination
(column[N+j] + column[N-j])/sqrt(2) for j>=1, and column[N] for j=0.
We also cross-check: parity of column 0 should be ~+1 (even), and
the raw entries should satisfy Q[N+j,0] ≈ Q[N-j,0].
"""

import json, os, sys, time
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r49_fourier_circle import build_QW, eigh_mp, parity_projector_indices, parity_score

J_MAX = 5

def run_lambda(lam, N, dps, label):
    t0 = time.time()
    A, L = build_QW(lam, N, dps=dps, verbose=False)
    vals, Q = eigh_mp(A)
    eps_N = vals[0]
    pair = parity_projector_indices(N)
    chi0 = parity_score(Q.column(0), pair)
    # Extract ξ_j for j = 0..J_MAX using even-symmetric combinations.
    raw = [Q[i, 0] for i in range(2*N+1)]
    # Sanity: Q[N+j,0] vs Q[N-j,0]
    sym_resid = []
    xi = []
    for j in range(J_MAX+1):
        a = raw[N+j]; b = raw[N-j]
        sym_resid.append(float(abs(a-b)))
        if j == 0:
            xi.append(a)
        else:
            # Real-symmetric combination normalized so ξ_j is the coefficient
            # of the even basis (V_j+V_{-j})/sqrt(2). If raw is already even
            # then a == b and the even-basis coefficient is a*sqrt(2).
            xi.append(a * mp.sqrt(2))
    sqrtL = mp.sqrt(L)
    out = {
        "lam_label": label,
        "lam": mp.nstr(lam, 20),
        "L": mp.nstr(L, 20),
        "N": N,
        "dps": dps,
        "wall_s": time.time()-t0,
        "eps_N": mp.nstr(eps_N, 10),
        "parity_chi0": chi0,
        "max_sym_residual": max(sym_resid),
        "xi": [mp.nstr(x, 18) for x in xi],
        "sqrtL_xi": [mp.nstr(sqrtL*x, 18) for x in xi],
        "positions_2pij_over_L": [mp.nstr(2*mp.pi*j/L, 12) for j in range(J_MAX+1)],
    }
    return out

def main():
    # (label, lam-expression, N, dps)
    # Heavier λ need larger N and L means larger K_max=λ² prime sum cost.
    # Keep modest to fit wall time; this is a stabilization test, not CC1 benchmark.
    runs = [
        ("sqrt13", mp.sqrt(13), 60, 50),
        ("5",      mp.mpf(5),   60, 50),
        ("10",     mp.mpf(10),  60, 50),
        ("20",     mp.mpf(20),  60, 50),
        ("50",     mp.mpf(50),  60, 50),
        ("100",    mp.mpf(100), 60, 50),
    ]
    report = []
    for (label, lam, N, dps) in runs:
        print(f"\n=== λ = {label}  N={N}  dps={dps} ===", flush=True)
        mp.mp.dps = dps
        try:
            res = run_lambda(lam, N, dps, label)
            print(f"  wall = {res['wall_s']:.1f}s  chi0={res['parity_chi0']:.4f}  "
                  f"eps_N={res['eps_N']}  symresid={res['max_sym_residual']:.2e}")
            print(f"  ξ_j        : {res['xi']}")
            print(f"  √L ξ_j     : {res['sqrtL_xi']}")
            print(f"  2πj/L      : {res['positions_2pij_over_L']}")
        except Exception as e:
            res = {"lam_label": label, "error": repr(e)}
            print(f"  FAILED: {e}")
        report.append(res)
        # Save incrementally
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "cs1_coefficient_stabilization.json")
        with open(out_path, "w") as f:
            json.dump(report, f, indent=2, default=str)
    print("\nSaved:", out_path)

if __name__ == "__main__":
    main()
