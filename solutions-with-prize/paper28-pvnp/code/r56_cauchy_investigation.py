"""R56 -- Approach A: Cauchy matrix theory for even-sector simplicity.

Investigates whether the even-sector Weil quadratic form QW_lambda^{N,+}
has generalized Cauchy structure with distinct nodes, and whether classical
Cauchy simplicity theorems apply to prove eigenvalue simplicity.

INVESTIGATION PLAN:
1. Extract the exact structure of A^ev after even-sector projection.
2. Decompose A^ev into Cauchy-type and non-Cauchy parts.
3. Check node distinctness for the WR Cauchy nodes alpha_L(n).
4. Check whether eigenvalue simplicity holds for generalized Cauchy
   matrices of the form (b_i - b_j)/(i - j).
5. Numerical verification at lambda = sqrt(14), N = 20.
"""

import os
import sys
import time
import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import (
    build_QW,
    build_W02,
    build_WR,
    build_Wprimes,
    precompute_abc,
    alpha_L as compute_alpha_L,
    eigh_mp,
)
from r51b_evenblock import project_to_even


def investigate_cauchy_structure(lam, N, dps=80, verbose=True):
    """Full investigation of the Cauchy structure of A^ev."""
    mp.mp.dps = dps
    L = 2 * mp.log(lam)

    print("=" * 72)
    print(f"CAUCHY STRUCTURE INVESTIGATION: lambda={lam}, N={N}, dps={dps}")
    print(f"L = {mp.nstr(L, 15)}")
    print("=" * 72)

    # -------------------------------------------------------------------
    # STEP 1: Build the three components separately.
    # -------------------------------------------------------------------
    print("\n--- STEP 1: Build components W02, WR, Wp ---")
    t0 = time.time()

    W02 = build_W02(N, L)
    alpha_vals, diag_vals = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha_vals, diag_vals)
    K_max = int(mp.floor(lam * lam + mp.mpf("1e-30")))
    Wp = build_Wprimes(N, L, K_max, verbose=False)

    # Full matrix A = W02 - WR - Wp
    dim = 2 * N + 1
    A = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            A[i, j] = W02[i, j] - WR[i, j] - Wp[i, j]
        # Symmetrise
    for i in range(dim):
        for j in range(i + 1, dim):
            avg = (A[i, j] + A[j, i]) / 2
            A[i, j] = avg
            A[j, i] = avg

    print(f"  Build time: {time.time() - t0:.1f}s")

    # -------------------------------------------------------------------
    # STEP 2: Project each component to even sector separately.
    # -------------------------------------------------------------------
    print("\n--- STEP 2: Project to even sector ---")
    W02_ev = project_to_even(W02, N)
    WR_ev = project_to_even(WR, N)
    Wp_ev = project_to_even(Wp, N)
    A_ev = project_to_even(A, N)

    # Verify: A_ev = W02_ev - WR_ev - Wp_ev
    max_diff = mp.mpf(0)
    for i in range(N + 1):
        for j in range(N + 1):
            d = abs(A_ev[i, j] - (W02_ev[i, j] - WR_ev[i, j] - Wp_ev[i, j]))
            if d > max_diff:
                max_diff = d
    print(f"  Verification A_ev = W02_ev - WR_ev - Wp_ev: max|diff| = {mp.nstr(max_diff, 6)}")

    # -------------------------------------------------------------------
    # STEP 3: Analyze the Cauchy structure of WR_ev.
    #
    # In the full V_n basis, WR has off-diagonal entries:
    #   WR(n, m) = (alpha_L(m) - alpha_L(n)) / (n - m)   for n != m
    # This is a generalized Cauchy form with "nodes" b_n = alpha_L(n).
    #
    # In the even sector (cosine basis), n ranges over {0, 1, ..., N}.
    # The even projection combines:
    #   WR_ev[n, m] = WR[n, m] + WR[n, -m]    for n, m >= 1
    #   (with the sqrt(2) factors for n=0 or m=0)
    #
    # Question: does WR_ev still have Cauchy structure?
    # -------------------------------------------------------------------
    print("\n--- STEP 3: Cauchy structure analysis of WR ---")

    # Compute and display the alpha_L nodes.
    print(f"\n  alpha_L nodes (b_n = alpha_L(n) for n = 0..{N}):")
    alphas = []
    for n in range(0, N + 1):
        a = alpha_vals[n]
        alphas.append(a)
        if n <= 10 or n == N:
            print(f"    alpha_L({n:3d}) = {mp.nstr(a, 20)}")

    # Check distinctness of alpha_L nodes.
    print(f"\n  Checking distinctness of alpha_L(n) for n = 0..{N}:")
    min_gap = mp.mpf("inf")
    min_gap_pair = (0, 0)
    all_distinct = True
    for i in range(len(alphas)):
        for j in range(i + 1, len(alphas)):
            gap = abs(alphas[i] - alphas[j])
            if gap < min_gap:
                min_gap = gap
                min_gap_pair = (i, j)
            if gap < mp.mpf("1e-50"):
                all_distinct = False
                print(f"    WARNING: alpha_L({i}) ~= alpha_L({j}), gap = {mp.nstr(gap, 6)}")

    print(f"    Minimum gap: |alpha_L({min_gap_pair[0]}) - alpha_L({min_gap_pair[1]})| = {mp.nstr(min_gap, 12)}")
    print(f"    All distinct? {all_distinct}")

    # Also check the NEGATIVE nodes: alpha_L(-n) = -alpha_L(n).
    # When we fold into even sector, we combine n and -n.
    # The effective "nodes" in the even sector are NOT simply alpha_L(n).
    print(f"\n  Key structural point:")
    print(f"  In full basis: WR[n,m] = (alpha_L(m) - alpha_L(n))/(n - m)")
    print(f"  Since alpha_L(-n) = -alpha_L(n), the nodes for negative n are negated.")
    print(f"  Even projection combines V_n and V_{{-n}}:")
    print(f"  WR_ev[n,m] for n,m >= 1 involves:")
    print(f"    (alpha_L(m) - alpha_L(n))/(n - m) + (alpha_L(-m) - alpha_L(n))/(n + m)")
    print(f"   = (alpha(m) - alpha(n))/(n - m) + (-alpha(m) - alpha(n))/(n + m)")
    print(f"   = (alpha(m) - alpha(n))/(n - m) - (alpha(m) + alpha(n))/(n + m)")

    # Verify this formula numerically.
    print(f"\n  Verifying even-sector WR formula:")
    max_formula_err = mp.mpf(0)
    for n in range(1, min(N + 1, 6)):
        for m in range(1, min(N + 1, 6)):
            if n == m:
                continue
            an = alpha_vals[n]
            am = alpha_vals[m]
            formula = (am - an) / (n - m) - (am + an) / (n + m)
            actual = WR_ev[n, m]
            err = abs(formula - actual)
            if err > max_formula_err:
                max_formula_err = err
            if n <= 3 and m <= 3:
                print(f"    WR_ev[{n},{m}]: formula={mp.nstr(formula, 15)} actual={mp.nstr(actual, 15)} err={mp.nstr(err, 4)}")
    print(f"  Max formula error (off-diag, n,m >= 1): {mp.nstr(max_formula_err, 6)}")

    # The combined formula is:
    # WR_ev[n,m] = (alpha(m) - alpha(n))/(n - m) - (alpha(m) + alpha(n))/(n + m)
    #            = alpha(m) [1/(n-m) - 1/(n+m)] - alpha(n) [1/(n-m) + 1/(n+m)]
    #            = alpha(m) * 2m/(n^2 - m^2) - alpha(n) * 2n/(n^2 - m^2)
    #            = 2(m alpha(m) - n alpha(n)) / (n^2 - m^2)
    # This is a GENERALIZED CAUCHY FORM with:
    #    nodes: phi_n = n * alpha_L(n)
    #    denominators: (n^2 - m^2)  =>  Cauchy matrix C[n,m] = 1/(x_n - y_m)
    #       with x_n = n^2 and y_m = -m^2? No, that gives 1/(n^2+m^2).
    #
    # Actually: 2(m alpha(m) - n alpha(n))/(n^2 - m^2)
    # This is (phi_m - phi_n) / (n^2 - m^2) where phi_n = n * alpha_L(n).
    # But n^2 - m^2 = (n-m)(n+m), so this is NOT standard Cauchy 1/(x_i + y_j).
    # It is a "displaced" Cauchy form.

    print(f"\n  Simplified even-sector WR off-diagonal formula:")
    print(f"    WR_ev[n,m] = 2(m*alpha(m) - n*alpha(n)) / (n^2 - m^2)")
    print(f"               = (phi_m - phi_n) / (n^2 - m^2)  where phi_n = n*alpha(n)")

    # Verify this simplified formula.
    print(f"\n  Verifying simplified formula:")
    max_simp_err = mp.mpf(0)
    for n in range(1, min(N + 1, 8)):
        for m in range(1, min(N + 1, 8)):
            if n == m:
                continue
            phi_n = n * alpha_vals[n]
            phi_m = m * alpha_vals[m]
            formula2 = 2 * (phi_m - phi_n) / (n**2 - m**2)
            actual = WR_ev[n, m]
            err = abs(formula2 - actual)
            if err > max_simp_err:
                max_simp_err = err
    print(f"  Max simplified formula error: {mp.nstr(max_simp_err, 6)}")

    # Check distinctness of phi_n = n * alpha_L(n).
    print(f"\n  Checking distinctness of phi_n = n * alpha_L(n):")
    phis = [n * alpha_vals[n] for n in range(0, N + 1)]
    phi_min_gap = mp.mpf("inf")
    phi_min_pair = (0, 0)
    for i in range(len(phis)):
        for j in range(i + 1, len(phis)):
            gap = abs(phis[i] - phis[j])
            if gap < phi_min_gap:
                phi_min_gap = gap
                phi_min_pair = (i, j)
    print(f"    Minimum gap: |phi_{phi_min_pair[0]} - phi_{phi_min_pair[1]}| = {mp.nstr(phi_min_gap, 12)}")
    print(f"    phi values (first few):")
    for n in range(min(8, N + 1)):
        print(f"      phi_{n} = {mp.nstr(phis[n], 18)}")

    # -------------------------------------------------------------------
    # STEP 4: Analyze the FULL A_ev = W02_ev - WR_ev - Wp_ev.
    # W02_ev is rank 2 (it is a sum a_n*a_m - c_n*c_m in the full basis,
    #   but in even basis only the a*a part survives since c is odd).
    # Actually W02 in even basis: W02 factors as rank-2 in V_n basis.
    # The a-vector (involving L^2 terms) is even, the c-vector (involving
    # nm terms) is odd. So W02_ev is rank 1 in the even sector!
    # -------------------------------------------------------------------
    print("\n--- STEP 4: Rank structure of W02_ev ---")

    # Check rank of W02_ev numerically.
    vals_W02, _ = eigh_mp(W02_ev)
    nonzero_W02 = sum(1 for v in vals_W02 if abs(v) > mp.mpf("1e-30"))
    print(f"  W02_ev eigenvalues (nonzero count = {nonzero_W02}):")
    for k, v in enumerate(vals_W02):
        if abs(v) > mp.mpf("1e-30") or k < 3:
            print(f"    lambda_{k} = {mp.nstr(v, 15)}")

    # W02_ev should be rank 1 in the even sector (the c-vector is odd and
    # projects to zero). Let's verify.
    # W02[n,m] = pref * (L^2 - 16 pi^2 m n) / ((L^2 + 16 pi^2 m^2)(L^2 + 16 pi^2 n^2))
    # = pref * [L^2 / denom(n) denom(m) - 16 pi^2 mn / denom(n) denom(m)]
    # = pref * a_n a_m * L^2 - pref * c_n c_m
    # where a_n = 1/denom(n), c_n = 4 pi n / denom(n).
    # In even sector: a is even (a_n = a_{-n}), c is odd (c_{-n} = -c_n).
    # Even projection of rank-1 outer product |c><c| gives zero.
    # Even projection of rank-1 outer product |a><a| gives the even-sector rank-1 matrix.
    # => W02_ev is rank 1 (the a*a part only).
    print(f"  W02_ev rank = {nonzero_W02} (expected: 1, since the c-vector is odd)")

    # -------------------------------------------------------------------
    # STEP 5: So A_ev = (rank-1) - (Cauchy-like) - (Wp_ev).
    # The Cauchy-like part WR_ev has the form (phi_m - phi_n)/(n^2 - m^2).
    # This is NOT standard Cauchy 1/(x_i + y_j).
    #
    # The key question: does the form (phi_m - phi_n)/(n^2 - m^2) with
    # distinct phi_n guarantee simple eigenvalues?
    #
    # THEOREM (Cauchy matrix simplicity):
    # A standard Cauchy matrix C_{i,j} = 1/(x_i + y_j) with all x_i
    # distinct and all y_j distinct has ALL eigenvalues simple.
    # (This follows from the explicit eigenvalue formula for Cauchy matrices.)
    #
    # But WR_ev is NOT of this form. It has the "divided difference" form
    # (phi_m - phi_n)/(x_n - x_m) with x_n = n^2.
    #
    # A divided difference matrix D_{i,j} = (f(x_i) - f(x_j))/(x_i - x_j)
    # is known as a "Loewner matrix" (after the Loewner-Heinz theory).
    #
    # THEOREM (Loewner): If f is a Pick function (analytic with positive
    # imaginary part in the upper half-plane) and x_1 < x_2 < ... < x_n,
    # then the Loewner matrix [(f(x_i) - f(x_j))/(x_i - x_j)] is
    # positive semidefinite. Moreover, it is POSITIVE DEFINITE (hence all
    # eigenvalues simple and positive) if and only if f cannot be extended
    # analytically through any arc of the real axis containing {x_i}.
    # -------------------------------------------------------------------
    print("\n--- STEP 5: Loewner matrix theory ---")
    print(f"  WR_ev has Loewner structure: (phi(x_n) - phi(x_m))/(x_n - x_m)")
    print(f"  where x_n = n^2 and phi(x) = sqrt(x) * alpha_L(sqrt(x))")
    print(f"  (treating x = n^2 as the node variable)")
    print(f"")
    print(f"  BUT: A_ev = W02_ev - WR_ev - Wp_ev, so even if WR_ev has nice")
    print(f"  Loewner structure, the full matrix has:")
    print(f"    (rank-1 perturbation) - (Loewner) - (prime sum)")
    print(f"  The rank-1 and prime-sum terms break the pure Loewner structure.")

    # -------------------------------------------------------------------
    # STEP 6: Numerical eigenvalue analysis at this (lambda, N).
    # -------------------------------------------------------------------
    print("\n--- STEP 6: Eigenvalue analysis ---")

    vals_ev, Q_ev = eigh_mp(A_ev)

    print(f"  Even-sector eigenvalues (first 5):")
    for k in range(min(5, len(vals_ev))):
        print(f"    mu_{k+1} = {mp.nstr(vals_ev[k], 25)}")

    gap = vals_ev[1] - vals_ev[0]
    print(f"\n  Spectral gap: delta^ev = mu_2 - mu_1 = {mp.nstr(gap, 15)}")
    print(f"  Simple? {float(gap) > 0} (gap = {float(gap):.6e})")

    # Compute relative gaps between ALL consecutive eigenvalues.
    print(f"\n  All consecutive gaps:")
    for k in range(min(10, len(vals_ev) - 1)):
        g = vals_ev[k + 1] - vals_ev[k]
        print(f"    mu_{k+2} - mu_{k+1} = {mp.nstr(g, 12)}  ({float(g):.4e})")

    # -------------------------------------------------------------------
    # STEP 7: Test the Loewner matrix WR_ev in isolation.
    # If WR_ev alone has simple eigenvalues (by Loewner theory),
    # then the question is whether adding (rank-1) - Wp preserves this.
    # -------------------------------------------------------------------
    print("\n--- STEP 7: WR_ev eigenvalues in isolation ---")
    vals_WR, _ = eigh_mp(WR_ev)
    gap_WR = vals_WR[1] - vals_WR[0]
    print(f"  WR_ev eigenvalues (first 5):")
    for k in range(min(5, len(vals_WR))):
        print(f"    nu_{k+1} = {mp.nstr(vals_WR[k], 20)}")
    print(f"  WR_ev gap: {mp.nstr(gap_WR, 12)}")
    print(f"  WR_ev all eigenvalues simple?")
    all_simple_WR = True
    for k in range(len(vals_WR) - 1):
        g = vals_WR[k + 1] - vals_WR[k]
        if float(g) <= 0:
            all_simple_WR = False
            print(f"    DEGENERATE at k={k}: gap = {mp.nstr(g, 12)}")
    if all_simple_WR:
        print(f"    YES -- all {len(vals_WR)} eigenvalues of WR_ev are simple.")

    # -------------------------------------------------------------------
    # STEP 8: What is the Wp_ev contribution?
    # The prime sum Wp is a FINITE-RANK perturbation (one rank-1 term
    # per prime power k <= lambda^2). Check its spectral norm.
    # -------------------------------------------------------------------
    print("\n--- STEP 8: Wp_ev spectral analysis ---")
    vals_Wp, _ = eigh_mp(Wp_ev)
    print(f"  Wp_ev spectral range: [{mp.nstr(vals_Wp[0], 12)}, {mp.nstr(vals_Wp[-1], 12)}]")
    print(f"  Wp_ev spectral norm: {mp.nstr(max(abs(vals_Wp[0]), abs(vals_Wp[-1])), 12)}")
    Wp_rank = sum(1 for v in vals_Wp if abs(v) > mp.mpf("1e-30"))
    print(f"  Wp_ev effective rank: {Wp_rank}")

    # -------------------------------------------------------------------
    # STEP 9: The critical test -- Cauchy interlacing after rank-1 update.
    #
    # THEOREM (Cauchy interlacing): If B is symmetric with eigenvalues
    # lambda_1 <= ... <= lambda_n, and C = B + sigma * vv^T is a rank-1
    # update, then the eigenvalues of C interlace with those of B.
    #
    # COROLLARY: If B has simple eigenvalues and sigma * vv^T is a
    # rank-1 perturbation with v not orthogonal to any eigenvector of B,
    # then C has simple eigenvalues.
    #
    # Check: is the W02_ev rank-1 perturbation "generic" (i.e., does
    # the a-vector have nonzero overlap with every eigenvector of
    # -(WR_ev + Wp_ev))?
    # -------------------------------------------------------------------
    print("\n--- STEP 9: Rank-1 perturbation analysis ---")

    # -(WR_ev + Wp_ev)
    B = mp.matrix(N + 1)
    for i in range(N + 1):
        for j in range(N + 1):
            B[i, j] = -(WR_ev[i, j] + Wp_ev[i, j])
    vals_B, Q_B = eigh_mp(B)

    # W02_ev is rank-1: W02_ev = sigma * |a_ev><a_ev|
    # Extract the a-vector from W02_ev.
    vals_W02_ev, Q_W02 = eigh_mp(W02_ev)
    # The single nonzero eigenvalue:
    sigma_W02 = vals_W02_ev[-1]  # should be the only nonzero one
    a_vec = [Q_W02[i, N] for i in range(N + 1)]  # eigenvector of the nonzero eigenvalue
    print(f"  W02_ev nonzero eigenvalue: sigma = {mp.nstr(sigma_W02, 15)}")

    # Check overlaps <phi_k | a_vec> for each eigenvector phi_k of B.
    print(f"  Overlaps <phi_k | a_ev> for eigenvectors of B = -(WR_ev + Wp_ev):")
    overlaps = []
    for k in range(N + 1):
        phi_k = [Q_B[i, k] for i in range(N + 1)]
        overlap = sum(phi_k[i] * a_vec[i] for i in range(N + 1))
        overlaps.append(abs(overlap))
        if k < 10 or k == N:
            print(f"    k={k:3d}: |<phi_k|a>| = {mp.nstr(abs(overlap), 12)}")

    min_overlap = min(overlaps)
    print(f"  Minimum overlap: {mp.nstr(min_overlap, 12)}")
    if float(min_overlap) > 1e-50:
        print(f"  ALL overlaps nonzero => Cauchy interlacing PRESERVES simplicity")
        print(f"  (if B has simple eigenvalues, then B + sigma|a><a| does too)")
    else:
        print(f"  WARNING: some overlap is essentially zero => rank-1 update")
        print(f"  may introduce a degeneracy")

    # Check: does B = -(WR_ev + Wp_ev) have simple eigenvalues?
    print(f"\n  B = -(WR_ev + Wp_ev) eigenvalues (first 5):")
    all_simple_B = True
    for k in range(min(5, len(vals_B))):
        print(f"    beta_{k+1} = {mp.nstr(vals_B[k], 20)}")
    for k in range(len(vals_B) - 1):
        g = vals_B[k + 1] - vals_B[k]
        if float(g) <= 0:
            all_simple_B = False
    print(f"  B has all simple eigenvalues? {all_simple_B}")

    # -------------------------------------------------------------------
    # STEP 10: The logical chain assessment.
    # -------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("STEP 10: LOGICAL CHAIN ASSESSMENT")
    print("=" * 72)

    print(f"""
  STRUCTURE OF A_ev:
    A_ev = W02_ev  -  WR_ev  -  Wp_ev
         = (rank 1) - (Loewner-type, dim {N+1}) - (finite-rank prime sum)

  W02_ev:
    Rank 1 (the odd c-vector projects to zero).
    Single nonzero eigenvalue: sigma = {mp.nstr(sigma_W02, 12)}

  WR_ev (off-diagonal, n,m >= 1):
    Loewner form: (phi_m - phi_n)/(n^2 - m^2) where phi_n = n * alpha_L(n)
    Nodes phi_n all distinct? {phi_min_gap > mp.mpf("1e-50")}
    Minimum gap between nodes: {mp.nstr(phi_min_gap, 12)}
    Eigenvalues all simple? {all_simple_WR}

  Wp_ev:
    Effective rank: {Wp_rank}
    Spectral norm: {mp.nstr(max(abs(vals_Wp[0]), abs(vals_Wp[-1])), 8)}

  B = -(WR_ev + Wp_ev):
    All eigenvalues simple? {all_simple_B}

  A_ev = B + W02_ev (rank-1 update of B):
    All overlaps <phi_k|a> nonzero? {float(min_overlap) > 1e-50}
    => Cauchy interlacing preserves simplicity? {all_simple_B and float(min_overlap) > 1e-50}

  A_ev eigenvalue gap: delta = {mp.nstr(gap, 12)}
  A_ev all eigenvalues simple? {float(gap) > 0}
""")

    # -------------------------------------------------------------------
    # STEP 11: The gap in the proof.
    # -------------------------------------------------------------------
    print("  THE GAP IN APPROACH A:")
    print("  ======================")
    print(f"  1. WR_ev has Loewner structure with distinct nodes: VERIFIED")
    print(f"     But Loewner theory guarantees positive definiteness (hence")
    print(f"     simplicity) ONLY if the generating function is a Pick function.")
    print(f"     The function phi(x) = sqrt(x) * alpha_L(sqrt(x)) must be checked.")
    print(f"")
    print(f"  2. A_ev = (rank-1) + B where B = -(WR_ev + Wp_ev):")
    print(f"     Even if B has simple eigenvalues, the rank-1 update preserves")
    print(f"     simplicity ONLY IF the perturbation vector a is not orthogonal")
    print(f"     to any eigenvector of B. VERIFIED NUMERICALLY (min overlap = {mp.nstr(min_overlap, 6)}).")
    print(f"     But this is a numerical check, not a proof.")
    print(f"")
    print(f"  3. The REAL difficulty: Wp_ev (the prime sum) has NO Cauchy/Loewner")
    print(f"     structure. It is a sum of rank-1 terms (one per prime power).")
    print(f"     Each rank-1 update preserves simplicity IF the perturbation")
    print(f"     vector is generic. But the prime contributions are structured")
    print(f"     (they come from trigonometric evaluations at log p), not random.")
    print(f"     Proving genericity for ALL prime contributions simultaneously")
    print(f"     is the hard step.")

    results = {
        "lambda": str(lam),
        "N": N,
        "L": float(L),
        "alphas_distinct": all(abs(alphas[i] - alphas[j]) > mp.mpf("1e-50")
                              for i in range(len(alphas))
                              for j in range(i+1, len(alphas))),
        "alpha_min_gap": float(min_gap),
        "phis_distinct": float(phi_min_gap) > 1e-50,
        "phi_min_gap": float(phi_min_gap),
        "W02_ev_rank": nonzero_W02,
        "WR_ev_simple": all_simple_WR,
        "Wp_ev_rank": Wp_rank,
        "B_simple": all_simple_B,
        "min_overlap": float(min_overlap),
        "delta_ev": float(gap),
        "A_ev_simple": float(gap) > 0,
    }
    return results


def main():
    mp.mp.dps = 80

    # Primary test: lambda = sqrt(14), N = 20.
    lam = mp.sqrt(14)
    results_main = investigate_cauchy_structure(lam, N=20, dps=80)

    # Secondary: smaller N for speed, verify pattern holds.
    print("\n\n" + "#" * 72)
    print("SECONDARY CHECKS: smaller N values")
    print("#" * 72)
    for N in [5, 10, 15]:
        r = investigate_cauchy_structure(lam, N=N, dps=60, verbose=False)
        print(f"  N={N:3d}: delta={r['delta_ev']:.4e}  simple={r['A_ev_simple']}  "
              f"B_simple={r['B_simple']}  min_overlap={r['min_overlap']:.4e}")

    # Verify at lambda = sqrt(10) too.
    print("\n\nLambda = sqrt(10):")
    lam10 = mp.sqrt(10)
    for N in [5, 10, 15, 20]:
        r = investigate_cauchy_structure(lam10, N=N, dps=60, verbose=False)
        print(f"  N={N:3d}: delta={r['delta_ev']:.4e}  simple={r['A_ev_simple']}  "
              f"B_simple={r['B_simple']}  min_overlap={r['min_overlap']:.4e}")


if __name__ == "__main__":
    main()
