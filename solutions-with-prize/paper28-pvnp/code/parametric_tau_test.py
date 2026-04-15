"""Parametric tau-tracking for spectral disjointness -- Lead F.

Defines the one-parameter interpolation B(tau) = B_arch + tau * B_prime
for tau in [0, 1], where B_arch = -WR_ev (archimedean Loewner) and
B_prime = -Wp_ev (prime Euler sum).

At each tau, computes:
  - Eigenvalues of B(tau) and M_a(tau) (principal submatrix of A^ev(tau))
  - Spectral gap: min_{k,j} |lambda_k(B) - mu_j(M_a)|
  - det(C(tau)) where C = B(tau) direct-sum (-M_a(tau))
  - Sign changes in det(C(tau)) across the sweep

The Arithmetic Theorem requires spec(B) intersect spec(M_a) = empty.
At tau = 0 (pure Cauchy), this holds by strict interlacing (STP).
At tau = 1 (full Weil), this is the target.

References:
  - Research notes 27, 29, 30, 34 in this project
  - Kato, Perturbation Theory for Linear Operators, IV.3
  - von Neumann-Wigner (1929), Arnold (1972)

Usage:
  python parametric_tau_test.py [--N 10] [--lambda 14] [--ntau 200] [--dps 50]
"""

import argparse
import os
import sys
import time
import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import (
    build_W02,
    build_WR,
    build_Wprimes,
    precompute_abc,
    eigh_mp,
)
from r51b_evenblock import project_to_even


# ---------------------------------------------------------------------------
# Matrix construction helpers
# ---------------------------------------------------------------------------

def build_even_components(N, lam, dps=50):
    """Build the even-sector components: W02_ev, WR_ev, Wp_ev, and derived
    quantities B_arch, B_prime, sigma, a_vec.

    Returns dict with all components.
    """
    mp.mp.dps = dps
    L = 2 * mp.log(lam)

    # Build full (2N+1) x (2N+1) matrices
    W02 = build_W02(N, L)
    alpha_vals, diag_vals = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha_vals, diag_vals)
    K_max = int(mp.floor(lam * lam + mp.mpf("1e-30")))
    Wp = build_Wprimes(N, L, K_max, verbose=False)

    # Project to even sector (dimension N+1)
    W02_ev = project_to_even(W02, N)
    WR_ev = project_to_even(WR, N)
    Wp_ev = project_to_even(Wp, N)

    dim_ev = N + 1

    # B_arch = -WR_ev, B_prime = -Wp_ev
    B_arch = mp.matrix(dim_ev)
    B_prime = mp.matrix(dim_ev)
    for i in range(dim_ev):
        for j in range(dim_ev):
            B_arch[i, j] = -WR_ev[i, j]
            B_prime[i, j] = -Wp_ev[i, j]

    # Symmetrise
    for M in [B_arch, B_prime]:
        for i in range(dim_ev):
            for j in range(i + 1, dim_ev):
                avg = (M[i, j] + M[j, i]) / 2
                M[i, j] = avg
                M[j, i] = avg

    # Extract rank-1 structure from W02_ev: sigma and a_vec
    vals_W02, vecs_W02 = eigh_mp(W02_ev)
    sigma = vals_W02[-1]
    a_vec = [vecs_W02[i, dim_ev - 1] for i in range(dim_ev)]

    return {
        'N': N,
        'lam': lam,
        'L': L,
        'dim_ev': dim_ev,
        'W02_ev': W02_ev,
        'WR_ev': WR_ev,
        'Wp_ev': Wp_ev,
        'B_arch': B_arch,
        'B_prime': B_prime,
        'sigma': sigma,
        'a_vec': a_vec,
    }


def build_B_tau(B_arch, B_prime, tau):
    """Build B(tau) = B_arch + tau * B_prime."""
    dim = B_arch.rows
    B = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            B[i, j] = B_arch[i, j] + tau * B_prime[i, j]
    return B


def build_A_ev_tau(B_tau, sigma, a_vec):
    """Build A^ev(tau) = B(tau) + sigma * |a><a|."""
    dim = B_tau.rows
    A = mp.matrix(dim)
    for i in range(dim):
        for j in range(dim):
            A[i, j] = B_tau[i, j] + sigma * a_vec[i] * a_vec[j]
    return A


def principal_submatrix(M, row_to_delete):
    """Delete row and column row_to_delete to get principal submatrix."""
    dim = M.rows
    sub = mp.matrix(dim - 1)
    ri = 0
    for i in range(dim):
        if i == row_to_delete:
            continue
        ci = 0
        for j in range(dim):
            if j == row_to_delete:
                continue
            sub[ri, ci] = M[i, j]
            ci += 1
        ri += 1
    return sub


def find_dominant_a_index(a_vec):
    """Find the index of the largest component of |a| for the principal
    submatrix deletion.  The Arithmetic Theorem uses M_a = principal
    submatrix obtained by deleting the row/column most aligned with a."""
    return max(range(len(a_vec)), key=lambda i: abs(a_vec[i]))


# ---------------------------------------------------------------------------
# Spectral gap computation
# ---------------------------------------------------------------------------

def spectral_gap(eigs_B, eigs_M):
    """Compute min_{k,j} |lambda_k - mu_j| between two eigenvalue lists."""
    min_gap = mp.inf
    for lk in eigs_B:
        for mj in eigs_M:
            g = abs(lk - mj)
            if g < min_gap:
                min_gap = g
    return min_gap


def closest_pair(eigs_B, eigs_M):
    """Find the closest pair (k, j) between eigenvalue lists."""
    min_gap = mp.inf
    best_k, best_j = 0, 0
    for k, lk in enumerate(eigs_B):
        for j, mj in enumerate(eigs_M):
            g = abs(lk - mj)
            if g < min_gap:
                min_gap = g
                best_k, best_j = k, j
    return best_k, best_j, min_gap


# ---------------------------------------------------------------------------
# Main sweep
# ---------------------------------------------------------------------------

def tau_sweep(N, lam, n_tau=200, dps=50):
    """Sweep tau from 0 to 1, tracking eigenvalues and spectral gaps."""
    mp.mp.dps = dps
    t_start = time.time()

    print("=" * 78)
    print("PARAMETRIC TAU-TRACKING -- Lead F")
    print("=" * 78)
    print(f"  lambda       = {mp.nstr(lam, 10)}")
    print(f"  N (even dim) = {N} (matrix size {N+1}x{N+1})")
    print(f"  tau points   = {n_tau}")
    print(f"  precision    = {dps} digits")
    print()

    # ------------------------------------------------------------------
    # Step 1: Build components
    # ------------------------------------------------------------------
    print("--- Step 1: Building even-sector components ---")
    t0 = time.time()
    comp = build_even_components(N, lam, dps)
    B_arch = comp['B_arch']
    B_prime = comp['B_prime']
    sigma = comp['sigma']
    a_vec = comp['a_vec']
    dim_ev = comp['dim_ev']
    print(f"  Built components [{time.time()-t0:.1f}s]")
    print(f"  sigma = {mp.nstr(sigma, 15)}")
    print(f"  |a_vec| = {mp.nstr(mp.norm(mp.matrix(a_vec)), 10)}")

    # Determine which row to delete for M_a
    # Use index 0 (the n=0 component, typically the largest)
    a_del = find_dominant_a_index(a_vec)
    print(f"  Deleting row/col {a_del} for principal submatrix M_a "
          f"(|a[{a_del}]| = {mp.nstr(abs(a_vec[a_del]), 8)})")

    # ------------------------------------------------------------------
    # Step 2: Norm of B_prime (the perturbation)
    # ------------------------------------------------------------------
    eigs_prime = sorted([float(x) for x in mp.eigsy(B_prime)[0]])
    norm_prime = max(abs(eigs_prime[0]), abs(eigs_prime[-1]))
    print(f"\n  ||B_prime||_op = {norm_prime:.6e}")

    # ------------------------------------------------------------------
    # Step 3: Tau sweep
    # ------------------------------------------------------------------
    print(f"\n--- Step 2: Tau sweep ({n_tau} points) ---\n")

    tau_vals = [mp.mpf(k) / (n_tau - 1) for k in range(n_tau)]
    gaps = []
    det_C_vals = []
    det_B_vals = []
    det_M_vals = []
    eig_data = []

    # Header for condensed output
    print(f"  {'tau':>8s}  {'gap_min':>14s}  {'closest(k,j)':>12s}  "
          f"{'det(B)':>14s}  {'det(M_a)':>14s}  {'det(C) sign':>12s}")
    print("  " + "-" * 80)

    for idx, tau in enumerate(tau_vals):
        # Build B(tau) and A^ev(tau)
        B_tau = build_B_tau(B_arch, B_prime, tau)
        A_tau = build_A_ev_tau(B_tau, sigma, a_vec)

        # Principal submatrix M_a(tau) from A^ev(tau)
        M_a_tau = principal_submatrix(A_tau, a_del)

        # Eigenvalues
        eigs_B_tau = sorted(mp.eigsy(B_tau)[0], key=lambda x: float(x))
        eigs_M_tau = sorted(mp.eigsy(M_a_tau)[0], key=lambda x: float(x))

        # Spectral gap
        k_close, j_close, gap = closest_pair(eigs_B_tau, eigs_M_tau)
        gaps.append((tau, gap, k_close, j_close))

        # Determinants
        det_B = mp.det(B_tau)
        det_M = mp.det(M_a_tau)
        det_C = det_B * ((-1)**M_a_tau.rows) * det_M

        det_B_vals.append((tau, det_B))
        det_M_vals.append((tau, det_M))
        det_C_vals.append((tau, det_C))

        # Store eigenvalue snapshots at a few tau values
        if idx % max(1, n_tau // 10) == 0 or idx == n_tau - 1:
            eig_data.append({
                'tau': float(tau),
                'eigs_B': [float(x) for x in eigs_B_tau],
                'eigs_M': [float(x) for x in eigs_M_tau],
                'gap': float(gap),
            })

        # Condensed print (every 10th point + first + last)
        if idx % max(1, n_tau // 20) == 0 or idx == n_tau - 1:
            sign_C = "+" if det_C > 0 else ("-" if det_C < 0 else "ZERO")
            print(f"  {float(tau):8.4f}  {mp.nstr(gap, 8):>14s}  "
                  f"({k_close:2d},{j_close:2d})     "
                  f"{mp.nstr(det_B, 6):>14s}  {mp.nstr(det_M, 6):>14s}  "
                  f"{sign_C:>12s}")

    # ------------------------------------------------------------------
    # Step 4: Analysis
    # ------------------------------------------------------------------
    print(f"\n\n{'='*78}")
    print("ANALYSIS")
    print(f"{'='*78}")

    # Gap statistics
    gap_vals = [(float(t), float(g), k, j) for t, g, k, j in gaps]
    min_gap_entry = min(gap_vals, key=lambda x: x[1])
    max_gap_entry = max(gap_vals, key=lambda x: x[1])

    print(f"\n  SPECTRAL GAP (min_{{k,j}} |lambda_k(B) - mu_j(M_a)|):")
    print(f"    Minimum gap = {min_gap_entry[1]:.6e}  at tau = {min_gap_entry[0]:.6f}"
          f"  (pair k={min_gap_entry[2]}, j={min_gap_entry[3]})")
    print(f"    Maximum gap = {max_gap_entry[1]:.6e}  at tau = {max_gap_entry[0]:.6f}")
    print(f"    Gap at tau=0 = {gap_vals[0][1]:.6e}")
    print(f"    Gap at tau=1 = {gap_vals[-1][1]:.6e}")
    print(f"    Gap ever zero? {'YES -- SPECTRAL COINCIDENCE' if min_gap_entry[1] == 0 else 'NO'}")

    # det(C) sign changes
    sign_changes = 0
    prev_sign = 1 if det_C_vals[0][1] > 0 else (-1 if det_C_vals[0][1] < 0 else 0)
    for tau, dc in det_C_vals[1:]:
        curr_sign = 1 if dc > 0 else (-1 if dc < 0 else 0)
        if curr_sign != 0 and prev_sign != 0 and curr_sign != prev_sign:
            sign_changes += 1
        if curr_sign != 0:
            prev_sign = curr_sign

    print(f"\n  det(C(tau)) = det(B(tau)) * (-1)^N * det(M_a(tau)):")
    print(f"    det(C(0)) = {mp.nstr(det_C_vals[0][1], 10)}")
    print(f"    det(C(1)) = {mp.nstr(det_C_vals[-1][1], 10)}")
    print(f"    Sign changes in [0,1]: {sign_changes}")
    if sign_changes == 0:
        print(f"    No sign change => det(C) is single-signed (necessary for no zero crossing)")
    else:
        print(f"    WARNING: {sign_changes} sign change(s) detected in det(C)")

    # det(B) sign changes (zero eigenvalue of B(tau))
    sign_changes_B = 0
    prev_sign = 1 if det_B_vals[0][1] > 0 else (-1 if det_B_vals[0][1] < 0 else 0)
    for tau, db in det_B_vals[1:]:
        curr_sign = 1 if db > 0 else (-1 if db < 0 else 0)
        if curr_sign != 0 and prev_sign != 0 and curr_sign != prev_sign:
            sign_changes_B += 1
        if curr_sign != 0:
            prev_sign = curr_sign

    print(f"\n  det(B(tau)):")
    print(f"    det(B(0)) = {mp.nstr(det_B_vals[0][1], 10)}")
    print(f"    det(B(1)) = {mp.nstr(det_B_vals[-1][1], 10)}")
    print(f"    Sign changes: {sign_changes_B}")

    # ------------------------------------------------------------------
    # Step 5: Eigenvalue tracking at snapshots
    # ------------------------------------------------------------------
    print(f"\n  EIGENVALUE SNAPSHOTS:")
    for snap in eig_data:
        tau = snap['tau']
        print(f"\n    tau = {tau:.4f}  (gap = {snap['gap']:.4e}):")
        eB = snap['eigs_B']
        eM = snap['eigs_M']
        n_show = min(6, len(eB))
        for k in range(n_show):
            bval = f"{eB[k]:+.8e}" if k < len(eB) else ""
            mval = f"{eM[k]:+.8e}" if k < len(eM) else ""
            print(f"      lambda_{k}(B) = {bval:>20s}    mu_{k}(M_a) = {mval:>20s}")
        if len(eB) > n_show:
            print(f"      ... ({len(eB) - n_show} more eigenvalues)")

    # ------------------------------------------------------------------
    # Step 6: Strict interlacing check at tau = 0 and tau = 1
    # ------------------------------------------------------------------
    print(f"\n  STRICT INTERLACING CHECK (B vs M_a from A=B+sigma|a><a|):")
    for check_tau in [mp.mpf(0), mp.mpf(1)]:
        B_check = build_B_tau(B_arch, B_prime, check_tau)
        A_check = build_A_ev_tau(B_check, sigma, a_vec)
        M_check = principal_submatrix(A_check, a_del)
        eB = sorted(mp.eigsy(B_check)[0], key=lambda x: float(x))
        eM = sorted(mp.eigsy(M_check)[0], key=lambda x: float(x))

        # For rank-1 pert with sigma > 0: beta_k <= mu_k <= beta_{k+1}
        # M_a has eigenvalues that interlace with A_ev. And A_ev = B + sigma*aa^T.
        # The spectral disjointness we check is between B and M_a.
        violations = 0
        for k in range(len(eB)):
            for j in range(len(eM)):
                if abs(float(eB[k]) - float(eM[j])) < 1e-40:
                    violations += 1

        _, _, g = closest_pair(eB, eM)
        print(f"    tau = {float(check_tau):.1f}: min gap = {mp.nstr(g, 8)}, "
              f"near-coincidences (|diff| < 1e-40): {violations}")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print(f"\n{'='*78}")
    print("SUMMARY")
    print(f"{'='*78}")
    print(f"  tau_min (smallest gap) = {min_gap_entry[0]:.6f}")
    print(f"  gap_min                = {min_gap_entry[1]:.6e}")
    print(f"  det(C) sign changes    = {sign_changes}")
    print(f"  det(B) sign changes    = {sign_changes_B}")
    print(f"  Spectral coincidence   = {'YES' if min_gap_entry[1] == 0 else 'NO'}")
    print(f"\n  Conclusion: {'Gap remains positive across full tau sweep.' if min_gap_entry[1] > 0 else 'SPECTRAL COINCIDENCE DETECTED.'}")
    print(f"  Consistent with Arithmetic Theorem: {'YES' if min_gap_entry[1] > 0 else 'NEEDS INVESTIGATION'}")

    print(f"\n  Total runtime: {time.time() - t_start:.1f}s")
    print("=" * 78)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Parametric tau-tracking for spectral disjointness (Lead F)")
    parser.add_argument("--N", type=int, default=10,
                        help="Even-sector truncation N (matrix size N+1)")
    parser.add_argument("--lam", type=float, default=14.0,
                        help="lambda^2 value (default 14, so lambda=sqrt(14))")
    parser.add_argument("--ntau", type=int, default=200,
                        help="Number of tau points in [0,1]")
    parser.add_argument("--dps", type=int, default=50,
                        help="Decimal digits of precision")
    args = parser.parse_args()

    lam = mp.sqrt(mp.mpf(args.lam))
    tau_sweep(args.N, lam, n_tau=args.ntau, dps=args.dps)


if __name__ == "__main__":
    main()
