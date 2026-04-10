"""R56 Thread 1 — Relative entropy analysis of Q_W = A − B.

Decomposes Q_W into archimedean piece A = (W02 − WR) and arithmetic piece
B = Wprimes on the even sector, then investigates whether matrix relative
entropy can establish ε ≥ 0.

Uses mpmath throughout for 80-digit precision (needed for ε ~ 10^{-58}).
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


def build_components(lam, N, dps=80, verbose=True):
    """Build W02, WR, Wprimes separately on full basis, then project to even sector.
    Returns (A_ev, B_ev, QW_ev, L) where A = W02 - WR, B = Wprimes, QW = A - B."""
    mp.mp.dps = dps
    L = 2 * mp.log(lam)
    K_max = int(mp.floor(lam * lam + mp.mpf("1e-30")))
    if verbose:
        print(f"Building components: λ={float(lam):.6f}, L={float(L):.6f}, N={N}, K_max={K_max}, dps={dps}")

    t0 = time.time()
    W02 = build_W02(N, L)
    if verbose: print(f"  W02 done [{time.time()-t0:.1f}s]")

    t1 = time.time()
    alpha, diag = precompute_abc(N, L, verbose=verbose)
    WR = build_WR(N, L, alpha, diag)
    if verbose: print(f"  WR done [{time.time()-t1:.1f}s]")

    t2 = time.time()
    Wp = build_Wprimes(N, L, K_max, verbose=verbose)
    if verbose: print(f"  Wp done [{time.time()-t2:.1f}s]")

    # Build WR from r49
    from r49_fourier_circle import build_WR as _bwr
    # A_full = W02 - WR (archimedean), B_full = Wp (arithmetic)
    dim = 2 * N + 1
    A_full = mp.matrix(dim)
    B_full = Wp  # already built
    for i in range(dim):
        for j in range(dim):
            A_full[i, j] = W02[i, j] - WR[i, j]

    # Project to even sector
    A_ev = project_to_even(A_full, N)
    B_ev = project_to_even(B_full, N)

    # QW_ev = A_ev - B_ev
    dim_ev = N + 1
    QW_ev = mp.matrix(dim_ev)
    for i in range(dim_ev):
        for j in range(dim_ev):
            QW_ev[i, j] = A_ev[i, j] - B_ev[i, j]

    # Symmetrise
    for M in [A_ev, B_ev, QW_ev]:
        for i in range(dim_ev):
            for j in range(i+1, dim_ev):
                avg = (M[i, j] + M[j, i]) / 2
                M[i, j] = avg
                M[j, i] = avg

    if verbose: print(f"  Total build: {time.time()-t0:.1f}s")
    return A_ev, B_ev, QW_ev, L


def matrix_log(M, n):
    """Compute log(M) for positive definite symmetric n×n mpmath matrix.
    Uses eigendecomposition: log(M) = Q diag(log(λ_i)) Q^T."""
    vals, Q = eigh_mp(M)
    log_vals = [mp.log(v) for v in vals]
    # Reconstruct: log(M) = Q diag(log_vals) Q^T
    result = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            s = mp.mpf(0)
            for k in range(n):
                s += Q[i, k] * log_vals[k] * Q[j, k]
            result[i, j] = s
            result[j, i] = s
    return result


def matrix_power(M, alpha, n):
    """Compute M^alpha for positive definite symmetric n×n matrix."""
    vals, Q = eigh_mp(M)
    pow_vals = [v ** alpha for v in vals]
    result = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            s = mp.mpf(0)
            for k in range(n):
                s += Q[i, k] * pow_vals[k] * Q[j, k]
            result[i, j] = s
            result[j, i] = s
    return result


def matrix_sqrt(M, n):
    """Compute M^{1/2}."""
    return matrix_power(M, mp.mpf("0.5"), n)


def matrix_inv_sqrt(M, n):
    """Compute M^{-1/2}."""
    return matrix_power(M, mp.mpf("-0.5"), n)


def mat_mul(A, B, n):
    """Multiply two n×n mpmath matrices."""
    C = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            s = mp.mpf(0)
            for k in range(n):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    return C


def trace(M, n):
    """Trace of n×n matrix."""
    s = mp.mpf(0)
    for i in range(n):
        s += M[i, i]
    return s


def log_det(M, n):
    """log det(M) for positive definite M."""
    vals, _ = eigh_mp(M)
    s = mp.mpf(0)
    for v in vals:
        s += mp.log(v)
    return s


def run_at_lambda(lam, N, dps, label, results):
    """Run the full analysis at a given lambda."""
    mp.mp.dps = dps
    print(f"\n{'='*76}")
    print(f"  λ = {label}, N = {N}, dps = {dps}")
    print(f"{'='*76}")

    t0 = time.time()
    A_ev, B_ev, QW_ev, L = build_components(lam, N, dps=dps)
    dim = N + 1

    # ---- PART 1: Verify Q_W = A - B and compute spectra ----
    print("\n--- Part 1: Decomposition and spectra ---")

    # Verify Q_W = A - B
    max_diff = mp.mpf(0)
    for i in range(dim):
        for j in range(dim):
            d = abs(QW_ev[i, j] - (A_ev[i, j] - B_ev[i, j]))
            if d > max_diff:
                max_diff = d
    print(f"  max |Q_W - (A-B)| = {mp.nstr(max_diff, 6)}")

    vals_A, Q_A = eigh_mp(A_ev)
    vals_B, Q_B = eigh_mp(B_ev)
    vals_QW, Q_QW = eigh_mp(QW_ev)

    trA = trace(A_ev, dim)
    trB = trace(B_ev, dim)

    A_posdef = all(v > 0 for v in vals_A)
    B_posdef = all(v > 0 for v in vals_B)

    print(f"\n  A = W02 - WR (archimedean):")
    print(f"    Positive definite: {A_posdef}")
    print(f"    Tr(A) = {mp.nstr(trA, 18)}")
    print(f"    Min eigenvalue: {mp.nstr(vals_A[0], 18)}")
    print(f"    Max eigenvalue: {mp.nstr(vals_A[-1], 18)}")
    print(f"    Bottom 3: {[mp.nstr(v, 12) for v in vals_A[:3]]}")
    print(f"    Top 10:   {[mp.nstr(v, 12) for v in vals_A[-10:]]}")

    print(f"\n  B = Wprimes (arithmetic):")
    print(f"    Positive definite: {B_posdef}")
    print(f"    Tr(B) = {mp.nstr(trB, 18)}")
    print(f"    Min eigenvalue: {mp.nstr(vals_B[0], 18)}")
    print(f"    Max eigenvalue: {mp.nstr(vals_B[-1], 18)}")
    print(f"    Bottom 3: {[mp.nstr(v, 12) for v in vals_B[:3]]}")
    print(f"    Top 10:   {[mp.nstr(v, 12) for v in vals_B[-10:]]}")

    # Rank of B (count eigenvalues > threshold)
    rank_threshold = mp.mpf("1e-60")
    rank_B = sum(1 for v in vals_B if abs(v) > rank_threshold)
    print(f"    Effective rank (|λ| > 1e-60): {rank_B}")

    print(f"\n  Q_W = A - B:")
    print(f"    ε (min eigenvalue) = {mp.nstr(vals_QW[0], 18)}")
    print(f"    ε positive: {vals_QW[0] > 0}")
    if abs(vals_QW[0]) > 0:
        print(f"    log10(|ε|) = {float(mp.log10(abs(vals_QW[0]))):.2f}")

    rec = {
        "label": label,
        "N": N, "dim_ev": dim, "dps": dps,
        "L": float(L),
        "QW_AB_max_diff": float(max_diff),
        "A_posdef": A_posdef,
        "B_posdef": B_posdef,
        "trA": str(trA), "trA_float": float(trA),
        "trB": str(trB), "trB_float": float(trB),
        "A_min_eig": str(vals_A[0]), "A_min_eig_float": float(vals_A[0]),
        "A_max_eig": str(vals_A[-1]), "A_max_eig_float": float(vals_A[-1]),
        "B_min_eig": str(vals_B[0]), "B_min_eig_float": float(vals_B[0]),
        "B_max_eig": str(vals_B[-1]), "B_max_eig_float": float(vals_B[-1]),
        "B_effective_rank": rank_B,
        "epsilon": str(vals_QW[0]), "epsilon_float": float(vals_QW[0]),
        "A_bottom3": [float(v) for v in vals_A[:3]],
        "A_top10": [float(v) for v in vals_A[-10:]],
        "B_bottom3": [float(v) for v in vals_B[:3]],
        "B_top10": [float(v) for v in vals_B[-10:]],
    }

    if not (A_posdef and B_posdef):
        print("\n  WARNING: A or B not positive definite. Entropy direction blocked.")
        if not A_posdef:
            print(f"    A has {sum(1 for v in vals_A if v <= 0)} non-positive eigenvalues")
        if not B_posdef:
            print(f"    B has {sum(1 for v in vals_B if v <= 0)} non-positive eigenvalues")
            # Check if B is positive SEMI-definite
            B_psd = all(v >= -rank_threshold for v in vals_B)
            print(f"    B positive semi-definite (tol 1e-60): {B_psd}")
            rec["B_psd"] = B_psd
        rec["entropy_blocked"] = True
        results.append(rec)
        return rec

    # ---- PART 2: Löwner order A ≥ B ----
    print("\n--- Part 2: Löwner order check ---")

    epsilon = vals_QW[0]
    print(f"  ε = min eig(A-B) = {mp.nstr(epsilon, 18)}")
    print(f"  A ≥ B (Löwner): {epsilon >= 0}")

    # Compute A^{-1/2} B A^{-1/2}
    print("  Computing A^{-1/2} B A^{-1/2}...")
    Ainvhalf = matrix_inv_sqrt(A_ev, dim)
    AiBA = mat_mul(Ainvhalf, mat_mul(B_ev, Ainvhalf, dim), dim)
    # Symmetrise
    for i in range(dim):
        for j in range(i+1, dim):
            avg = (AiBA[i, j] + AiBA[j, i]) / 2
            AiBA[i, j] = avg
            AiBA[j, i] = avg
    vals_AiBA, _ = eigh_mp(AiBA)
    max_AiBA = vals_AiBA[-1]
    print(f"  max eig(A^{{-1/2}} B A^{{-1/2}}) = {mp.nstr(max_AiBA, 18)}")
    print(f"  All eigenvalues ≤ 1: {max_AiBA <= 1}")

    rec["lowner_epsilon"] = str(epsilon)
    rec["lowner_A_geq_B"] = bool(epsilon >= 0)
    rec["AiBA_max_eig"] = float(max_AiBA)
    rec["AiBA_all_leq_1"] = bool(max_AiBA <= 1)

    # ---- PART 3: Matrix relative entropy ----
    print("\n--- Part 3: Matrix relative entropy ---")

    # S(A || B) = Tr(A(log A - log B))
    print("  Computing matrix logarithms...")
    logA = matrix_log(A_ev, dim)
    logB = matrix_log(B_ev, dim)

    diff_log = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            diff_log[i, j] = logA[i, j] - logB[i, j]

    A_diff_log = mat_mul(A_ev, diff_log, dim)
    S_AB = trace(A_diff_log, dim)
    print(f"  S(A || B) = Tr(A(log A - log B)) = {mp.nstr(S_AB, 18)}")
    print(f"  S(A || B) ≥ 0: {S_AB >= 0}  (Klein's inequality)")

    # Petz-Rényi α-divergence: D_α(A || B) = (1/(α-1)) log Tr(A^α B^{1-α})
    print("  Computing Petz-Rényi divergences...")
    alphas = [mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("1.5"), mp.mpf("2.0")]
    renyi = {}
    for al in alphas:
        A_al = matrix_power(A_ev, al, dim)
        B_1mal = matrix_power(B_ev, 1 - al, dim)
        prod = mat_mul(A_al, B_1mal, dim)
        tr_prod = trace(prod, dim)
        if tr_prod > 0:
            D_al = mp.log(tr_prod) / (al - 1)
        else:
            D_al = mp.mpf("nan")
        print(f"  D_{float(al):.1f}(A || B) = {mp.nstr(D_al, 18)}")
        renyi[f"alpha_{float(al):.1f}"] = float(D_al)

    # Quantum fidelity: F(A,B) = (Tr sqrt(sqrt(A) B sqrt(A)))^2
    print("  Computing quantum fidelity...")
    sqrtA = matrix_sqrt(A_ev, dim)
    sqrtA_B_sqrtA = mat_mul(sqrtA, mat_mul(B_ev, sqrtA, dim), dim)
    # Symmetrise
    for i in range(dim):
        for j in range(i+1, dim):
            avg = (sqrtA_B_sqrtA[i, j] + sqrtA_B_sqrtA[j, i]) / 2
            sqrtA_B_sqrtA[i, j] = avg
            sqrtA_B_sqrtA[j, i] = avg
    vals_sABsA, _ = eigh_mp(sqrtA_B_sqrtA)
    tr_sqrt = mp.mpf(0)
    for v in vals_sABsA:
        if v > 0:
            tr_sqrt += mp.sqrt(v)
    fidelity = tr_sqrt ** 2
    print(f"  F(A, B) = {mp.nstr(fidelity, 18)}")

    rec["S_AB"] = float(S_AB)
    rec["renyi"] = renyi
    rec["fidelity"] = float(fidelity)

    # ---- PART 4: Candidate lower bounds on ε ----
    print("\n--- Part 4: Candidate lower bounds on ε ---")

    eps_float = float(epsilon)
    candidates = {}

    # f1 = S(A || B) / Tr(A)
    f1 = S_AB / trA
    candidates["S_AB_over_TrA"] = float(f1)
    print(f"  f1 = S(A||B)/Tr(A) = {mp.nstr(f1, 18)}")
    print(f"       f1 ≤ ε? {float(f1) <= eps_float}   f1 ≥ 0? {f1 >= 0}")

    # f2 = 1 - F(A,B)^{1/2}  -- but we need to normalize first
    # For density matrices (trace 1), fidelity ≤ 1. Our A,B aren't normalized.
    # Normalize: ρ = A/Tr(A), σ = B/Tr(B)
    rhoA = mp.matrix(dim)
    sigB = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            rhoA[i, j] = A_ev[i, j] / trA
            sigB[i, j] = B_ev[i, j] / trB
    sqrtRho = matrix_sqrt(rhoA, dim)
    sR_B_sR = mat_mul(sqrtRho, mat_mul(sigB, sqrtRho, dim), dim)
    for i in range(dim):
        for j in range(i+1, dim):
            avg = (sR_B_sR[i, j] + sR_B_sR[j, i]) / 2
            sR_B_sR[i, j] = avg
            sR_B_sR[j, i] = avg
    vals_norm, _ = eigh_mp(sR_B_sR)
    tr_sqrt_norm = mp.mpf(0)
    for v in vals_norm:
        if v > 0:
            tr_sqrt_norm += mp.sqrt(v)
    fid_norm = tr_sqrt_norm ** 2
    f2 = 1 - mp.sqrt(fid_norm)
    candidates["fidelity_gap"] = float(f2)
    print(f"  f2 = 1 - √F(ρ,σ) = {mp.nstr(f2, 18)}  (normalized)")
    print(f"       f2 ≤ ε? {float(f2) <= eps_float}   f2 ≥ 0? {f2 >= 0}")

    # f3 = Tr(A) - Tr(B)
    f3 = trA - trB
    candidates["trace_diff"] = float(f3)
    print(f"  f3 = Tr(A) - Tr(B) = {mp.nstr(f3, 18)}")
    print(f"       f3 ≤ ε? {float(f3) <= eps_float}   f3 ≥ 0? {f3 >= 0}")

    # f4 = log det(A) - log det(B) (divided by dim for scale)
    ldA = log_det(A_ev, dim)
    ldB = log_det(B_ev, dim)
    f4_raw = ldA - ldB
    f4 = f4_raw / dim
    candidates["logdet_diff_per_dim"] = float(f4)
    candidates["logdet_diff_raw"] = float(f4_raw)
    print(f"  f4 = (log det A - log det B)/dim = {mp.nstr(f4, 18)}")
    print(f"       f4 ≤ ε? {float(f4) <= eps_float}   f4 ≥ 0? {f4 >= 0}")

    # Also: min eigenvalue of A - B vs these
    print(f"\n  ε = {mp.nstr(epsilon, 18)}")
    print(f"  Summary of candidates:")
    for name, val in candidates.items():
        is_lower = val <= eps_float
        is_nonneg = val >= 0
        tight = "TIGHT" if (is_lower and is_nonneg) else ("lower but negative" if is_lower and not is_nonneg else "not a lower bound")
        print(f"    {name:30s} = {val:+.10e}  ≤ε:{is_lower}  ≥0:{is_nonneg}  {tight}")

    rec["candidates"] = candidates

    # ---- PART 6: Low-rank structure ----
    print("\n--- Part 6: Low-rank structure of B ---")
    print(f"  dim(even sector) = {dim}")
    print(f"  rank(B) ≈ {rank_B}")
    print(f"  B eigenvalue distribution:")
    nonzero_B = [(i, float(v)) for i, v in enumerate(vals_B) if abs(v) > float(rank_threshold)]
    for i, v in nonzero_B:
        print(f"    λ_{i} = {v:.6e}")
    # The null space of B has dimension dim - rank_B
    null_dim = dim - rank_B
    print(f"  null(B) dimension: {null_dim}")
    print(f"  On null(B), A-B = A restricted. A|_null(B) is positive definite")
    print(f"  → only rank_B = {rank_B} directions matter for Löwner order")

    rec["B_nonzero_eigs"] = nonzero_B
    rec["B_null_dim"] = null_dim

    elapsed = time.time() - t0
    rec["elapsed_s"] = elapsed
    print(f"\n  Elapsed: {elapsed:.1f}s")

    results.append(rec)
    return rec


def main():
    results = []

    # Primary: λ=√13, N=60, dps=80
    mp.mp.dps = 80
    lam1 = mp.sqrt(13)
    rec1 = run_at_lambda(lam1, N=60, dps=80, label="sqrt13", results=results)

    # Part 5: Scaling — also run at λ=5 and λ=10 if A,B > 0 at sqrt13
    if not rec1.get("entropy_blocked"):
        for label, lam_f, N, dps in [("5", lambda: mp.mpf(5), 60, 80),
                                      ("10", lambda: mp.mpf(10), 60, 80)]:
            mp.mp.dps = dps
            lam = lam_f()
            run_at_lambda(lam, N=N, dps=dps, label=label, results=results)

    # Save JSON
    out_path = os.path.join(CODE_DIR, "r56t1_relative_entropy.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nJSON saved to {out_path}")

    # Print scaling summary if multiple λ
    if len(results) > 1:
        print(f"\n{'='*76}")
        print("SCALING SUMMARY")
        print(f"{'='*76}")
        print(f"{'λ':>8} {'ε':>14} {'S(A||B)':>14} {'F(ρ,σ)':>14} {'Tr(A)-Tr(B)':>14} {'rank(B)':>8}")
        for r in results:
            if r.get("entropy_blocked"):
                print(f"{r['label']:>8}  BLOCKED")
                continue
            print(f"{r['label']:>8} {r.get('epsilon_float',0):>14.6e} "
                  f"{r.get('S_AB',0):>14.6e} {r.get('fidelity',0):>14.6e} "
                  f"{r.get('trA_float',0)-r.get('trB_float',0):>14.6e} "
                  f"{r.get('B_effective_rank',0):>8}")


if __name__ == "__main__":
    main()
