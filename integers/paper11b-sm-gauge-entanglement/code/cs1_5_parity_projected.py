"""CS-1.5 — Parity-projected coefficient stabilization.

Fix for the bug in cs1_coefficient_stabilization.py: the original script
diagonalised Q_W^{λ,N} on the full V_n basis (n ∈ {-N..N}, dim 2N+1) and
extracted the even ground state by post-hoc symmetrisation. At small λ
near-degeneracies caused the eigenvectors to mix even/odd sectors.

Fix: build Q_even, the restriction of Q_W to the even subspace
{e_0=V_0, e_j=(V_j+V_{-j})/√2, j=1..N}, dimension N+1, and diagonalise
Q_even directly. Eigenvectors are even by construction.

Coefficients ξ_j (j=0..J_MAX) are read off the lowest eigenvector of Q_even
in the e_j basis directly — no post-hoc symmetrisation. (Note: ξ_j here is
the coefficient in the orthonormal even basis, matching CS-1's convention.)
"""

import json, os, sys, time
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r49_fourier_circle import build_QW, eigh_mp, parity_projector_indices, parity_score

J_MAX = 5
CODE_DIR = os.path.dirname(os.path.abspath(__file__))


def project_even(A, N):
    """Restrict (2N+1)x(2N+1) matrix A to the even subspace.
    Returns (N+1)x(N+1) mpmath matrix Q_even in the basis
        e_0 = V_0           (row index N in A)
        e_j = (V_j + V_{-j}) / sqrt(2)   for j = 1..N
              (rows N+j and N-j in A)
    """
    sqrt2 = mp.sqrt(2)
    n = N + 1
    Qe = mp.matrix(n)
    # Index map: even basis index j -> list of (coef, A-row).
    def vec(j):
        if j == 0:
            return [(mp.mpf(1), N)]
        return [(1/sqrt2, N+j), (1/sqrt2, N-j)]
    for j in range(n):
        vj = vec(j)
        for k in range(n):
            vk = vec(k)
            s = mp.mpf(0)
            for (cj, rj) in vj:
                for (ck, rk) in vk:
                    s += cj * ck * A[rj, rk]
            Qe[j, k] = s
    # Symmetrise (numerical safety).
    for i in range(n):
        for j in range(i+1, n):
            avg = (Qe[i,j] + Qe[j,i]) / 2
            Qe[i,j] = avg
            Qe[j,i] = avg
    return Qe


def even_vec_to_full(vec_even, N):
    """Embed an even-basis vector (length N+1) back into the full V_n basis
    (length 2N+1) so we can compute the parity score as a sanity check."""
    sqrt2 = mp.sqrt(2)
    full = [mp.mpf(0)] * (2*N + 1)
    full[N] = vec_even[0]
    for j in range(1, N+1):
        full[N+j] = vec_even[j] / sqrt2
        full[N-j] = vec_even[j] / sqrt2
    return full


def run_lambda(lam, N, dps, label):
    t0 = time.time()
    A, L = build_QW(lam, N, dps=dps, verbose=False)
    Qe = project_even(A, N)
    vals, V = eigh_mp(Qe)
    eps_N = vals[0]
    # Lowest eigenvector in even basis.
    xi_even = [V[i, 0] for i in range(N+1)]
    # Sanity: parity in full basis
    pair = parity_projector_indices(N)
    full = even_vec_to_full(xi_even, N)
    chi0 = parity_score(full, pair)
    sqrtL = mp.sqrt(L)
    xi = xi_even[:J_MAX+1]
    out = {
        "lam_label": label,
        "lam": mp.nstr(lam, 20),
        "L": mp.nstr(L, 20),
        "N": N,
        "dps": dps,
        "wall_s": time.time() - t0,
        "eps_N": mp.nstr(eps_N, 10),
        "parity_chi0": chi0,
        "xi": [mp.nstr(x, 18) for x in xi],
        "sqrtL_xi": [mp.nstr(sqrtL*x, 18) for x in xi],
        "positions_2pij_over_L": [mp.nstr(2*mp.pi*j/L, 12) for j in range(J_MAX+1)],
    }
    return out, xi, sqrtL


def main():
    runs = [
        ("sqrt13", mp.sqrt(13), 60, 50),
        ("5",      mp.mpf(5),   60, 50),
        ("10",     mp.mpf(10),  60, 50),
        ("20",     mp.mpf(20),  60, 50),
        ("50",     mp.mpf(50),  60, 50),
        ("100",    mp.mpf(100), 60, 50),
    ]
    report = []
    plot_data = []
    for (label, lam, N, dps) in runs:
        print(f"\n=== λ = {label}  N={N}  dps={dps} ===", flush=True)
        mp.mp.dps = dps
        try:
            res, xi, sqrtL = run_lambda(lam, N, dps, label)
            print(f"  wall = {res['wall_s']:.1f}s  chi0 = {res['parity_chi0']:.6f}  eps_N = {res['eps_N']}")
            print(f"  ξ_j     : {res['xi']}")
            print(f"  √L ξ_j  : {res['sqrtL_xi']}")
            plot_data.append({
                "label": label,
                "L": float(mp.mpf(res["L"])),
                "xi": [float(x) for x in xi],
                "sqrtL_xi": [float(sqrtL * x) for x in xi],
                "pos": [float(2*mp.pi*j/mp.mpf(res["L"])) for j in range(J_MAX+1)],
            })
        except Exception as e:
            res = {"lam_label": label, "error": repr(e)}
            print(f"  FAILED: {e}")
        report.append(res)
        with open(os.path.join(CODE_DIR, "cs1_5_parity_projected.json"), "w") as f:
            json.dump(report, f, indent=2, default=str)

    # N-convergence at λ = 20
    print("\n=== N-convergence at λ = 20 ===")
    nconv = []
    for N in (40, 60, 80):
        mp.mp.dps = 50
        try:
            res, _, _ = run_lambda(mp.mpf(20), N, 50, f"20_N{N}")
            print(f"  N={N}: chi0={res['parity_chi0']:.6f} eps={res['eps_N']} ξ={res['xi']}")
            nconv.append(res)
        except Exception as e:
            nconv.append({"N": N, "error": repr(e)})
    report.append({"N_convergence_lambda20": nconv})
    with open(os.path.join(CODE_DIR, "cs1_5_parity_projected.json"), "w") as f:
        json.dump(report, f, indent=2, default=str)

    # Plots
    if plot_data:
        # Plot 1: ξ_j vs λ for each j
        fig, ax = plt.subplots(figsize=(8, 5))
        lams = [float(mp.mpf({"sqrt13": mp.sqrt(13), "5":5, "10":10, "20":20, "50":50, "100":100}[d["label"]])) for d in plot_data]
        for j in range(J_MAX+1):
            ys = [d["xi"][j] for d in plot_data]
            ax.plot(lams, ys, marker="o", label=f"j={j}")
        ax.set_xscale("log"); ax.set_xlabel("λ"); ax.set_ylabel("ξ_j")
        ax.set_title("CS-1.5: ξ_j(λ) (parity-projected)")
        ax.legend(); ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(os.path.join(CODE_DIR, "cs1_5_xi_j_vs_lambda.png"), dpi=120)
        plt.close(fig)

        # Plot 2: density collapse
        fig, ax = plt.subplots(figsize=(8, 5))
        for d in plot_data:
            ax.plot(d["pos"], d["sqrtL_xi"], marker="o", label=f"λ={d['label']}")
        ax.set_xlabel("2πj/L"); ax.set_ylabel("√L · ξ_j")
        ax.set_title("CS-1.5: density collapse test")
        ax.legend(); ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(os.path.join(CODE_DIR, "cs1_5_density_collapse.png"), dpi=120)
        plt.close(fig)
        print("\nPlots saved.")

    print("\nDone.")


if __name__ == "__main__":
    main()
