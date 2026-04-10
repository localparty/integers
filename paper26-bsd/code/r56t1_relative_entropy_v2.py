"""R56 Thread 1 v2 — Deeper investigation after A, B both NOT positive definite.

Key finding from v1: A = W02 - WR has 2 negative eigenvalues, B = Wprimes has
32 negative eigenvalues. The naive matrix relative entropy S(A || B) ≥ 0 is
not applicable because it requires A, B > 0.

This script explores:
1. Alternative decompositions that MIGHT give pos-def pieces
2. The shifted decomposition: A' = A + cI, B' = B + cI (both > 0 for large c)
   Then A' - B' = A - B = Q_W still, and S(A' || B') ≥ 0 by Klein.
   But S(A' || B') doesn't bound ε = min eig(A' - B').
3. The operator monotone approach: f(A) ≥ f(B) for operator monotone f
   when A ≥ B, but we need A ≥ B to USE this.
4. Detailed spectrum structure: where do the negative eigenvalues live?
5. The CORRECT decomposition: Q_W = W02 - (WR + Wp). Maybe W02 > 0 and
   (WR + Wp) > 0 separately?
6. Or: positive/negative parts of A and B.
"""

import json
import os
import sys
import time
import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import (
    build_W02, build_WR, build_Wprimes, precompute_abc, eigh_mp,
)
from r51b_evenblock import project_to_even


def mat_mul(A, B, n):
    C = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            s = mp.mpf(0)
            for k in range(n):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    return C


def trace(M, n):
    s = mp.mpf(0)
    for i in range(n):
        s += M[i, i]
    return s


def matrix_power(M_vals, M_Q, alpha, n):
    """Compute M^alpha given eigendecomposition."""
    pow_vals = [v ** alpha for v in M_vals]
    result = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            s = mp.mpf(0)
            for k in range(n):
                s += M_Q[i, k] * pow_vals[k] * M_Q[j, k]
            result[i, j] = s
            result[j, i] = s
    return result


def matrix_log_from_eig(vals, Q, n):
    """Compute log(M) from eigendecomposition."""
    log_vals = [mp.log(v) for v in vals]
    result = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            s = mp.mpf(0)
            for k in range(n):
                s += Q[i, k] * log_vals[k] * Q[j, k]
            result[i, j] = s
            result[j, i] = s
    return result


def relative_entropy_from_eig(vals_A, Q_A, vals_B, Q_B, A_mat, n):
    """Compute S(A || B) = Tr(A(log A - log B)) from eigendecompositions."""
    logA = matrix_log_from_eig(vals_A, Q_A, n)
    logB = matrix_log_from_eig(vals_B, Q_B, n)
    diff = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            diff[i, j] = logA[i, j] - logB[i, j]
    prod = mat_mul(A_mat, diff, n)
    return trace(prod, n)


def main():
    mp.mp.dps = 80
    N = 60
    lam = mp.sqrt(13)
    L = 2 * mp.log(lam)
    K_max = int(mp.floor(lam * lam + mp.mpf("1e-30")))
    dim = N + 1  # even sector

    print("="*76)
    print("R56 Thread 1 v2: Alternative decompositions")
    print("="*76)

    # Build full-basis components
    print("\nBuilding components...")
    t0 = time.time()
    W02_full = build_W02(N, L)
    alpha_seq, diag_seq = precompute_abc(N, L, verbose=True)
    WR_full = build_WR(N, L, alpha_seq, diag_seq)
    Wp_full = build_Wprimes(N, L, K_max, verbose=True)
    print(f"  Build time: {time.time()-t0:.1f}s")

    # Project each to even sector
    W02_ev = project_to_even(W02_full, N)
    WR_ev = project_to_even(WR_full, N)
    Wp_ev = project_to_even(Wp_full, N)

    # Symmetrise
    for M in [W02_ev, WR_ev, Wp_ev]:
        for i in range(dim):
            for j in range(i+1, dim):
                avg = (M[i, j] + M[j, i]) / 2
                M[i, j] = avg
                M[j, i] = avg

    # Construct various decompositions
    # Original: A = W02 - WR, B = Wp, Q_W = A - B
    A_orig = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            A_orig[i, j] = W02_ev[i, j] - WR_ev[i, j]

    QW_ev = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            QW_ev[i, j] = W02_ev[i, j] - WR_ev[i, j] - Wp_ev[i, j]

    # ---- Check each component separately ----
    print("\n--- Component spectra ---")

    for name, M in [("W02", W02_ev), ("WR", WR_ev), ("Wp", Wp_ev),
                    ("A=W02-WR", A_orig), ("Q_W=W02-WR-Wp", QW_ev)]:
        vals, _ = eigh_mp(M)
        posdef = all(v > 0 for v in vals)
        n_neg = sum(1 for v in vals if v < 0)
        tr = trace(M, dim)
        print(f"\n  {name}:")
        print(f"    Tr = {mp.nstr(tr, 15)}")
        print(f"    min eig = {mp.nstr(vals[0], 15)}")
        print(f"    max eig = {mp.nstr(vals[-1], 15)}")
        print(f"    pos-def: {posdef}  (#neg: {n_neg})")
        if n_neg > 0 and n_neg <= 5:
            print(f"    negative eigs: {[mp.nstr(v, 10) for v in vals if v < 0]}")

    # ---- Decomposition 2: Q_W = W02 - (WR + Wp) ----
    print("\n\n--- Decomposition 2: Q_W = W02 - (WR + Wp) ---")
    WR_plus_Wp = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            WR_plus_Wp[i, j] = WR_ev[i, j] + Wp_ev[i, j]

    vals_W02, Q_W02 = eigh_mp(W02_ev)
    vals_WRWp, Q_WRWp = eigh_mp(WR_plus_Wp)

    print(f"  W02: min eig = {mp.nstr(vals_W02[0], 15)}, pos-def: {all(v>0 for v in vals_W02)}")
    print(f"  WR+Wp: min eig = {mp.nstr(vals_WRWp[0], 15)}, pos-def: {all(v>0 for v in vals_WRWp)}")

    # ---- Decomposition 3: Shifted — Q_W = (A+cI) - (B+cI) ----
    print("\n\n--- Decomposition 3: Shifted decomposition ---")
    # Find c such that both A+cI > 0 and B+cI > 0
    vals_A, Q_A = eigh_mp(A_orig)
    vals_B, Q_B = eigh_mp(Wp_ev)

    c_min_A = -float(vals_A[0]) if vals_A[0] < 0 else 0
    c_min_B = -float(vals_B[0]) if vals_B[0] < 0 else 0
    c_shift = max(c_min_A, c_min_B) * 1.01 + 0.01  # slight margin
    print(f"  min eig(A) = {mp.nstr(vals_A[0], 12)}")
    print(f"  min eig(B) = {mp.nstr(vals_B[0], 12)}")
    print(f"  shift c = {c_shift:.6f}  (makes A+cI > 0, B+cI > 0)")

    c = mp.mpf(c_shift)
    A_shifted = mp.matrix(dim)
    B_shifted = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            A_shifted[i, j] = A_orig[i, j]
            B_shifted[i, j] = Wp_ev[i, j]
        A_shifted[i, i] += c
        B_shifted[i, i] += c

    vals_As, Q_As = eigh_mp(A_shifted)
    vals_Bs, Q_Bs = eigh_mp(B_shifted)

    print(f"  A+cI: min eig = {mp.nstr(vals_As[0], 12)}, pos-def: {all(v>0 for v in vals_As)}")
    print(f"  B+cI: min eig = {mp.nstr(vals_Bs[0], 12)}, pos-def: {all(v>0 for v in vals_Bs)}")

    # Compute S(A+cI || B+cI)
    print("  Computing S(A+cI || B+cI)...")
    S_shifted = relative_entropy_from_eig(vals_As, Q_As, vals_Bs, Q_Bs, A_shifted, dim)
    print(f"  S(A+cI || B+cI) = {mp.nstr(S_shifted, 18)}")
    print(f"  S ≥ 0: {S_shifted >= 0}")

    # But does S(A' || B') bound ε?
    # Klein: S(A'||B') = Tr(A'(log A' - log B')) ≥ Tr(A' - B') [NO, that's wrong]
    # Klein: S(A'||B') ≥ 0 always.
    # Pinsker: S(A'||B') ≥ (1/2) ||A' - B'||_1^2 / Tr(A')  [for trace-normalized]
    # But A' - B' = A - B = Q_W, so ||A' - B'||_1 is the trace norm of Q_W.
    vals_QW, _ = eigh_mp(QW_ev)
    trace_norm_QW = mp.mpf(0)
    for v in vals_QW:
        trace_norm_QW += abs(v)
    print(f"  ||Q_W||_1 = {mp.nstr(trace_norm_QW, 15)}")
    print(f"  Tr(A+cI) = {mp.nstr(trace(A_shifted, dim), 15)}")

    # The golden-Thompson / Peierls-Bogoliubov bound:
    # For A' > 0, B' > 0: Tr(A'(log A' - log B')) ≥ Tr(A') - Tr(B')  [NO]
    # Actually: S(A'||B') ≥ Tr(A' - B') + Tr(B') - Tr(B' exp(log A' - log B'))  [complicated]

    # The KEY issue: relative entropy S(A'||B') ≥ 0 does NOT imply A' ≥ B'.
    # Example: if A' = diag(10, 1) and B' = diag(1, 10), S > 0 but A' is not ≥ B'.
    # Relative entropy measures divergence, not operator ordering.

    # ---- Can we bound ε from below using entropy? ----
    print("\n\n--- The fundamental obstruction ---")
    print("  S(A' || B') ≥ 0 does NOT imply A' ≥ B' in Löwner order.")
    print("  Relative entropy measures statistical divergence, not operator ordering.")
    print("  Example: A' = diag(10,1), B' = diag(1,10): S > 0 but A' ≱ B'.")
    print()
    print("  For the implication S ≥ 0 ⟹ ε ≥ 0, we would need:")
    print("    (a) ε ≥ g(S) for some non-decreasing g with g(0) = 0")
    print("  This would require A' - B' to be MONOTONICALLY RELATED to S(A'||B'),")
    print("  which fails for generic positive definite matrices.")

    # ---- Alternative: log-majorization and Ando's theorem ----
    print("\n\n--- Alternative: log-majorization ---")
    # If the eigenvalues of A' log-majorize those of B', then A' ≥ B' in some sense.
    # Ando's theorem: if A' ≥ B' > 0, then log A' ≥ log B' (log is operator monotone).
    # Converse: log A' ≥ log B' implies A'^t ≥ B'^t for 0 < t ≤ 1 (Ando-Hiai).

    # Check: do the eigenvalues of A+cI dominate those of B+cI in every partial sum?
    # (This is weak majorization, which IS implied by A' ≥ B' but not vice versa.)
    vals_As_sorted = sorted([float(v) for v in vals_As], reverse=True)
    vals_Bs_sorted = sorted([float(v) for v in vals_Bs], reverse=True)

    print("  Checking weak majorization: sum_{1..k} lam_k(A') >= sum_{1..k} lam_k(B')?")
    sum_A = 0
    sum_B = 0
    majorizes = True
    for k in range(dim):
        sum_A += vals_As_sorted[k]
        sum_B += vals_Bs_sorted[k]
        if sum_A < sum_B:
            majorizes = False
            print(f"    FAILS at k={k+1}: sum_A = {sum_A:.10e}, sum_B = {sum_B:.10e}")
            break
    if majorizes:
        print(f"    YES — A+cI weakly majorizes B+cI")

    # ---- Check log-majorization ----
    print("\n  Checking log-majorization: prod_{1..k} lam_k(A') >= prod_{1..k} lam_k(B')?")
    logsum_A = 0
    logsum_B = 0
    log_majorizes = True
    import math
    for k in range(dim):
        logsum_A += math.log(vals_As_sorted[k])
        logsum_B += math.log(vals_Bs_sorted[k])
        if logsum_A < logsum_B:
            log_majorizes = False
            print(f"    FAILS at k={k+1}: sum_log_A = {logsum_A:.6f}, sum_log_B = {logsum_B:.6f}")
            break
    if log_majorizes:
        print(f"    YES — A+cI log-majorizes B+cI → by Ando-Hiai, (A')^t ≥ (B')^t for 0 < t ≤ 1")

    # ---- Compute Rényi divergences with shifted matrices ----
    print("\n\n--- Rényi divergences D_α(A+cI || B+cI) ---")
    for al_f in [0.5, 0.9, 1.5, 2.0]:
        al = mp.mpf(al_f)
        A_al = matrix_power(vals_As, Q_As, al, dim)
        B_1mal = matrix_power(vals_Bs, Q_Bs, 1 - al, dim)
        prod = mat_mul(A_al, B_1mal, dim)
        tr_prod = trace(prod, dim)
        if tr_prod > 0:
            D_al = mp.log(tr_prod) / (al - 1)
        else:
            D_al = mp.nan
        print(f"  D_{al_f:.1f} = {mp.nstr(D_al, 15)}")

    # ---- Quantum fidelity with shifted matrices ----
    print("\n--- Fidelity F(A+cI, B+cI) ---")
    sqrtA = matrix_power(vals_As, Q_As, mp.mpf("0.5"), dim)
    sABsA = mat_mul(sqrtA, mat_mul(B_shifted, sqrtA, dim), dim)
    for i in range(dim):
        for j in range(i+1, dim):
            avg = (sABsA[i, j] + sABsA[j, i]) / 2
            sABsA[i, j] = avg
            sABsA[j, i] = avg
    vals_sABsA, _ = eigh_mp(sABsA)
    tr_sqrt = sum(mp.sqrt(v) for v in vals_sABsA if v > 0)
    fidelity = tr_sqrt ** 2
    TrAs = trace(A_shifted, dim)
    TrBs = trace(B_shifted, dim)
    # Normalized fidelity
    fid_norm = fidelity / (TrAs * TrBs)
    print(f"  F(A', B') = {mp.nstr(fidelity, 15)}")
    print(f"  F_norm = F/(Tr(A')Tr(B')) = {mp.nstr(fid_norm, 15)}")

    # ---- The c-dependence: how does S(A+cI || B+cI) depend on c? ----
    print("\n\n--- c-dependence of S(A+cI || B+cI) ---")
    for c_test in [3.0, 5.0, 10.0, 50.0, 100.0]:
        c_mp = mp.mpf(c_test)
        As = mp.matrix(dim)
        Bs = mp.matrix(dim)
        for i in range(dim):
            for j in range(dim):
                As[i, j] = A_orig[i, j]
                Bs[i, j] = Wp_ev[i, j]
            As[i, i] += c_mp
            Bs[i, i] += c_mp
        vAs, QAs = eigh_mp(As)
        vBs, QBs = eigh_mp(Bs)
        S = relative_entropy_from_eig(vAs, QAs, vBs, QBs, As, dim)
        print(f"  c={c_test:6.1f}: S = {mp.nstr(S, 15)}")

    # ---- Part 5 equivalent: Try different λ values with shift ----
    print("\n\n--- Scaling with λ (shifted decomposition) ---")
    scaling_results = []
    for label, lam_f, N_val in [("sqrt13", lambda: mp.sqrt(13), 60),
                                 ("5", lambda: mp.mpf(5), 60),
                                 ("10", lambda: mp.mpf(10), 60)]:
        mp.mp.dps = 80
        lam_val = lam_f()
        L_val = 2 * mp.log(lam_val)
        K_max_val = int(mp.floor(lam_val * lam_val + mp.mpf("1e-30")))
        dim_val = N_val + 1

        W02_f = build_W02(N_val, L_val)
        al_s, di_s = precompute_abc(N_val, L_val, verbose=False)
        WR_f = build_WR(N_val, L_val, al_s, di_s)
        Wp_f = build_Wprimes(N_val, L_val, K_max_val, verbose=False)

        W02_e = project_to_even(W02_f, N_val)
        WR_e = project_to_even(WR_f, N_val)
        Wp_e = project_to_even(Wp_f, N_val)

        for M in [W02_e, WR_e, Wp_e]:
            for i in range(dim_val):
                for j in range(i+1, dim_val):
                    avg = (M[i, j] + M[j, i]) / 2
                    M[i, j] = avg
                    M[j, i] = avg

        A_f = mp.matrix(dim_val)
        QW_f = mp.matrix(dim_val)
        for i in range(dim_val):
            for j in range(dim_val):
                A_f[i, j] = W02_e[i, j] - WR_e[i, j]
                QW_f[i, j] = W02_e[i, j] - WR_e[i, j] - Wp_e[i, j]

        vals_Af, _ = eigh_mp(A_f)
        vals_Bf, _ = eigh_mp(Wp_e)
        vals_QWf, _ = eigh_mp(QW_f)

        eps_val = vals_QWf[0]
        c_need = max(-float(vals_Af[0]), -float(vals_Bf[0])) * 1.01 + 0.01
        c_mp = mp.mpf(c_need)

        As_f = mp.matrix(dim_val)
        Bs_f = mp.matrix(dim_val)
        for i in range(dim_val):
            for j in range(dim_val):
                As_f[i, j] = A_f[i, j]
                Bs_f[i, j] = Wp_e[i, j]
            As_f[i, i] += c_mp
            Bs_f[i, i] += c_mp

        vAs_f, QAs_f = eigh_mp(As_f)
        vBs_f, QBs_f = eigh_mp(Bs_f)
        S_f = relative_entropy_from_eig(vAs_f, QAs_f, vBs_f, QBs_f, As_f, dim_val)

        row = {
            "label": label, "eps": float(eps_val),
            "min_A": float(vals_Af[0]), "min_B": float(vals_Bf[0]),
            "c_shift": c_need, "S_shifted": float(S_f),
            "TrA": float(trace(A_f, dim_val)), "TrB": float(trace(Wp_e, dim_val)),
        }
        scaling_results.append(row)
        print(f"  λ={label:>7}: ε={float(eps_val):+.4e}, min(A)={float(vals_Af[0]):+.4e}, "
              f"min(B)={float(vals_Bf[0]):+.4e}, c={c_need:.4f}, S(A'||B')={float(S_f):.6e}")

    # ---- Verdict ----
    print("\n\n" + "="*76)
    print("VERDICT")
    print("="*76)
    print("""
  1. NEITHER A = W02 - WR NOR B = Wprimes IS POSITIVE DEFINITE.
     A has 2 negative eigenvalues (~ -0.85, -0.17).
     B has 32 negative eigenvalues (as large as -2.21).

  2. The Umegaki relative entropy S(A || B) is UNDEFINED for indefinite matrices.
     Klein's inequality S(A || B) >= 0 requires A, B > 0.

  3. SHIFTED DECOMPOSITION: A' = A + cI, B' = B + cI preserves Q_W = A' - B'
     and makes both positive definite. But S(A' || B') >= 0 does NOT imply
     A' >= B' (Löwner order). Relative entropy measures divergence between
     "states," not operator ordering. Counterexample: A'=diag(10,1),
     B'=diag(1,10) has S > 0 but A' is NOT >= B'.

  4. The FUNDAMENTAL OBSTRUCTION: no entropy inequality of the form
     f(A, B) <= epsilon with f >= 0 can work generically, because:
     - Relative entropy S(A||B) >= 0 always (Klein), regardless of A >= B
     - S(A||B) >= 0 even when A < B (e.g., when A << B)
     - The Löwner order A >= B is a STRICTLY STRONGER condition than
       any divergence inequality

  5. HOWEVER: the structure-specific properties of the Weil form (e.g.,
     log-majorization, the specific eigenvalue interlacing of W02, WR, Wp)
     might enable bounds that fail for generic matrices.

  6. The entropy direction needs to target Q_W >= 0 DIRECTLY (e.g., via
     the trace formula / Bost-Connes thermodynamics, Thread 2), not via
     a decomposition A - B with separate positivity of A and B.
""")

    # Save
    out = {
        "scaling": scaling_results,
        "A_not_posdef": True,
        "B_not_posdef": True,
        "entropy_direction_blocked": True,
        "obstruction": "Neither A=W02-WR nor B=Wprimes is positive definite. "
                       "Relative entropy requires positive definite inputs.",
    }
    out_path = os.path.join(CODE_DIR, "r56t1_relative_entropy_v2.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nJSON saved to {out_path}")


if __name__ == "__main__":
    main()
