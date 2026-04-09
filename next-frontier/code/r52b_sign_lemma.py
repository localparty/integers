"""R52b — Sign lemma diagnostic.

For the even ground state ξ_m of Q_W^{λ,N}, compute the first-order
RS shift ⟨ξ_m | Q_p | ξ_m⟩ when adding successive primes p ∈
{2,3,5,7,11,13}, and compare ε_{m+1} − ε_m against the predicted
Δε^{(1)} + Δε^{(2)}.

Q_p denotes the SIGNED contribution as it enters Q_W = W02 − WR − Σ Wp:
   Q_p := −Λ(p) p^{−1/2} q(U_n, U_m)(log p)
i.e. minus the Wp matrix for that single prime.

λ = √13, N = 120, dps = 80, even-block builder from r51b.
"""
import os, sys, json, time
import mpmath as mp

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r49_fourier_circle import (
    build_W02, precompute_abc, build_WR, q_UnUm, eigh_mp,
)
from r51b_evenblock import project_to_even


def build_Wp_singleprime(N, L, p):
    """Single-prime Wp matrix: Σ_{j: p^j ≤ ?} Λ(p^j) (p^j)^{-1/2} q(log p^j).
    For this diagnostic we restrict to j=1 (the prime itself) — that is the
    'one new perturbation per step' interpretation used by R50A's recursion."""
    M = mp.matrix(2 * N + 1)
    coeff = mp.log(p) / mp.sqrt(mp.mpf(p))
    y = mp.log(mp.mpf(p))
    for i in range(2 * N + 1):
        n = i - N
        for j in range(i, 2 * N + 1):
            m = j - N
            v = coeff * q_UnUm(n, m, y, L)
            M[i, j] = v
            M[j, i] = v
    return M


def quad_form(A_ev, v_ev):
    """⟨v | A | v⟩ for an even-block vector."""
    Nev = len(v_ev)
    s = mp.mpf(0)
    for i in range(Nev):
        row = mp.mpf(0)
        for j in range(Nev):
            row += A_ev[i, j] * v_ev[j]
        s += v_ev[i] * row
    return s


def matvec(A_ev, v_ev):
    Nev = len(v_ev)
    out = [mp.mpf(0)] * Nev
    for i in range(Nev):
        s = mp.mpf(0)
        for j in range(Nev):
            s += A_ev[i, j] * v_ev[j]
        out[i] = s
    return out


def main():
    dps = 80
    N = 120
    mp.mp.dps = dps
    lam = mp.sqrt(mp.mpf(13))
    L = 2 * mp.log(lam)
    print(f"R52b sign lemma: λ=√13, N={N}, dps={dps}, L={float(L):.6f}")

    print("Building W02 ...", flush=True)
    t0 = time.time()
    W02 = build_W02(N, L)
    print(f"  W02 done [{time.time()-t0:.1f}s]")

    print("Building WR ...", flush=True)
    t0 = time.time()
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)
    print(f"  WR  done [{time.time()-t0:.1f}s]")

    # Base operator with NO primes: Q0 = W02 - WR.
    primes = [2, 3, 5, 7, 11, 13]

    # Pre-build per-prime full Wp matrices.
    Wp_full = {}
    for p in primes:
        print(f"  Wp(p={p}) ...", flush=True)
        Wp_full[p] = build_Wp_singleprime(N, L, p)

    # Project base & each Wp.
    def full_to_ev(M):
        return project_to_even(M, N)

    Q_cur_full = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q_cur_full[i, j] = W02[i, j] - WR[i, j]

    rows = []
    Q_cur_ev = full_to_ev(Q_cur_full)
    vals, Q = eigh_mp(Q_cur_ev)
    eps_m = vals[0]
    xi_m = [Q[i, 0] for i in range(N + 1)]
    print(f"\nm=0  ε_0 = {mp.nstr(eps_m, 18)}  (no primes added)")

    for step, p in enumerate(primes, 1):
        # Q_p signed addition (as it enters Q_W: minus Wp).
        Wp_ev = full_to_ev(Wp_full[p])
        Qp_ev = mp.matrix(N + 1)
        for i in range(N + 1):
            for j in range(N + 1):
                Qp_ev[i, j] = -Wp_ev[i, j]

        # First-order shift on the EVEN block using current ξ_m.
        de1 = quad_form(Qp_ev, xi_m)

        # Second-order: Δε^(2) = Σ_{k>0} |⟨ξ_k|Qp|ξ_m⟩|² / (ε_m − μ_k).
        # Use the current eigenbasis (vals, Q) for the perturbation expansion.
        de2 = mp.mpf(0)
        # Qp · xi_m
        Qpxi = matvec(Qp_ev, xi_m)
        for k in range(1, N + 1):
            xi_k = [Q[i, k] for i in range(N + 1)]
            num = mp.mpf(0)
            for i in range(N + 1):
                num += xi_k[i] * Qpxi[i]
            denom = eps_m - vals[k]   # ε_m − μ_k < 0 for k>0
            if denom != 0:
                de2 += (num * num) / denom

        # Update operator and re-diagonalise.
        for i in range(N + 1):
            for j in range(N + 1):
                Q_cur_ev[i, j] = Q_cur_ev[i, j] + Qp_ev[i, j]
        vals_new, Q_new = eigh_mp(Q_cur_ev)
        eps_new = vals_new[0]
        actual_de = eps_new - eps_m

        rs_pred = de1 + de2

        print(f"\nm={step}  add p={p}")
        print(f"  Δε^(1)            = {mp.nstr(de1,    14)}   sign={'+' if de1>0 else '-' if de1<0 else '0'}")
        print(f"  Δε^(2)            = {mp.nstr(de2,    14)}   sign={'+' if de2>0 else '-' if de2<0 else '0'}")
        print(f"  Δε^(1)+Δε^(2)     = {mp.nstr(rs_pred,14)}")
        print(f"  actual ε_{step}-ε_{step-1} = {mp.nstr(actual_de,14)}")
        print(f"  ε_{step}             = {mp.nstr(eps_new, 18)}")
        rows.append({
            "step": step, "p": p,
            "eps_before": str(eps_m), "eps_after": str(eps_new),
            "actual_de": str(actual_de),
            "de1": str(de1), "de2": str(de2),
            "rs_pred": str(rs_pred),
            "de1_float": float(de1), "de2_float": float(de2),
            "actual_de_float": float(actual_de),
            "rs_pred_float": float(rs_pred),
        })

        eps_m = eps_new
        xi_m = [Q_new[i, 0] for i in range(N + 1)]
        vals, Q = vals_new, Q_new

    out = {"lam": "sqrt(13)", "N": N, "dps": dps, "L": float(L), "rows": rows}
    with open(os.path.join(CODE, "r52b_sign_lemma.json"), "w") as f:
        json.dump(out, f, indent=2, default=str)
    print("\nJSON ->", os.path.join(CODE, "r52b_sign_lemma.json"))


if __name__ == "__main__":
    main()
