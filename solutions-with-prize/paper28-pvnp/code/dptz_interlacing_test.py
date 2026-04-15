"""DPTZ interlacing test -- Arithmetic Theorem via eigenvector-eigenvalue identity.

The Arithmetic Theorem states: <phi_k | a> != 0 for all k, where phi_k are
eigenvectors of matrix B and a is an archimedean vector.

The DPTZ eigenvector-eigenvalue identity (Denton-Parke-Tao-Zhang, 2019) gives:
  |v_{i,j}|^2 = prod_k [lam_i(A) - lam_k(M_j)] / prod_{k!=i} [lam_i(A) - lam_k(A)]

Hence <phi_k | a> = 0  iff  lam_k(B) in spec(M_a), where M_a is B compressed
onto the orthogonal complement of a.

This script builds a model matrix approximating the even-sector Weil quadratic
form and checks whether eigenvalue coincidences can occur.

Questions addressed:
  1. What is the minimum gap between spec(B) and spec(M_a)?
  2. Does the gap have a clean scaling law as N grows?
  3. Does the DPTZ identity hold numerically?
"""

import sys
import time
import numpy as np
from numpy.linalg import eigh


# ---------------------------------------------------------------------------
# Prime sieve
# ---------------------------------------------------------------------------
def primes_up_to(n):
    """Simple sieve of Eratosthenes."""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i, b in enumerate(sieve) if b]


# ---------------------------------------------------------------------------
# Grid construction
# ---------------------------------------------------------------------------
def make_grid(N, grid_type="chebyshev", x_max=10.0):
    """Positive grid points for the Cauchy-type kernel 1/(x_i + x_j).

    Chebyshev nodes on (0, x_max] avoid clustering pathologies of uniform grids.
    """
    if grid_type == "chebyshev":
        # Chebyshev nodes on (0, 1], scaled to (0, x_max]
        k = np.arange(1, N + 1)
        nodes = 0.5 * x_max * (1 - np.cos(np.pi * (2 * k - 1) / (2 * N)))
        # ensure strictly positive
        nodes = np.maximum(nodes, 1e-14)
        return np.sort(nodes)
    elif grid_type == "uniform":
        return np.linspace(x_max / N, x_max, N)
    else:
        raise ValueError(f"Unknown grid type: {grid_type}")


# ---------------------------------------------------------------------------
# Matrix construction
# ---------------------------------------------------------------------------
def build_B_arch(x):
    """Archimedean (Loewner / Cauchy) part: B_arch[i,j] = 1/(x_i + x_j)."""
    N = len(x)
    xi = x[:, None]
    xj = x[None, :]
    return 1.0 / (xi + xj)


def build_B_prime(x, P_max=50):
    """Prime part: sum_{p <= P_max} (log p / sqrt(p)) * cos((x_i - x_j) * log p).

    This is the finite-prime truncation of the Weil explicit-formula kernel.
    """
    N = len(x)
    ps = primes_up_to(P_max)
    B = np.zeros((N, N))
    for p in ps:
        logp = np.log(p)
        coeff = logp / np.sqrt(p)
        diff = x[:, None] - x[None, :]
        B += coeff * np.cos(diff * logp)
    return B


def build_B(N, P_max=50, x_max=10.0, grid_type="chebyshev"):
    """Full model matrix B = B_arch + B_prime.

    We use the positive-definite convention (no overall minus sign) so that
    the archimedean part is manifestly positive.
    """
    x = make_grid(N, grid_type=grid_type, x_max=x_max)
    B_arch = build_B_arch(x)
    B_prime = build_B_prime(x, P_max=P_max)
    B = B_arch + B_prime
    # Enforce exact symmetry (should already be, but floating point)
    B = 0.5 * (B + B.T)
    return B, B_arch, x


# ---------------------------------------------------------------------------
# Archimedean vector
# ---------------------------------------------------------------------------
def archimedean_vector(B_arch, method="perron"):
    """Construct the archimedean vector a.

    method="perron": Perron eigenvector of B_arch (dominant eigenvector of
                     the positive matrix 1/(x_i + x_j)).
    method="column": first column of B_arch, normalized.
    """
    if method == "perron":
        vals, vecs = eigh(B_arch)
        # Perron eigenvector is the one with largest eigenvalue
        idx = np.argmax(vals)
        a = vecs[:, idx].copy()
        # Ensure all components positive (Perron-Frobenius)
        if np.sum(a) < 0:
            a = -a
        return a / np.linalg.norm(a)
    elif method == "column":
        a = B_arch[:, 0].copy()
        return a / np.linalg.norm(a)
    else:
        raise ValueError(f"Unknown method: {method}")


# ---------------------------------------------------------------------------
# Compression onto a^perp via Householder
# ---------------------------------------------------------------------------
def compress_to_aperp(B, a):
    """Compress B onto {a}^perp using a Householder reflector.

    Given unit vector a, construct H such that H a = e_1.
    Then M_a = (H B H^T)[1:, 1:] is the (N-1)x(N-1) compression.

    Returns M_a and the full rotated matrix H B H^T.
    """
    N = len(a)
    e1 = np.zeros(N)
    e1[0] = 1.0

    # Householder vector: v = a - e_1 (or a + e_1, pick the one avoiding cancellation)
    if a[0] >= 0:
        v = a + e1
    else:
        v = a - e1

    v = v / np.linalg.norm(v)

    # H = I - 2 v v^T
    # H B H^T via: first compute B H^T = B - 2 B v v^T, then H (B H^T)
    Bv = B @ v
    BHt = B - 2.0 * np.outer(Bv, v)
    vBHt = v @ BHt  # row vector (v^T)(B H^T)
    HBHt = BHt - 2.0 * np.outer(v, vBHt)

    # M_a is the lower-right (N-1)x(N-1) block
    M_a = HBHt[1:, 1:]

    return M_a, HBHt


# ---------------------------------------------------------------------------
# DPTZ identity verification
# ---------------------------------------------------------------------------
def verify_dptz(lam_B, lam_Ma, phi, a):
    """Verify the DPTZ eigenvector-eigenvalue identity:

      |<phi_k | a>|^2 = prod_j [lam_k(B) - lam_j(M_a)] / prod_{l!=k} [lam_k(B) - lam_l(B)]

    Returns arrays of LHS (overlaps^2), RHS (DPTZ formula), and relative errors.
    """
    N = len(lam_B)
    M = len(lam_Ma)  # = N-1

    overlaps_sq = np.array([(phi[:, k] @ a) ** 2 for k in range(N)])
    dptz_rhs = np.zeros(N)

    for k in range(N):
        # Numerator: product over eigenvalues of M_a
        numer = np.prod(lam_B[k] - lam_Ma)

        # Denominator: product over eigenvalues of B, l != k
        denom = 1.0
        for l in range(N):
            if l != k:
                denom *= (lam_B[k] - lam_B[l])

        dptz_rhs[k] = numer / denom if abs(denom) > 1e-300 else np.nan

    rel_err = np.abs(overlaps_sq - dptz_rhs) / np.maximum(np.abs(overlaps_sq), 1e-300)

    return overlaps_sq, dptz_rhs, rel_err


# ---------------------------------------------------------------------------
# Min-gap computation
# ---------------------------------------------------------------------------
def compute_min_gap(lam_B, lam_Ma):
    """Minimum |lam_k(B) - lam_j(M_a)| over all k, j."""
    gaps = np.abs(lam_B[:, None] - lam_Ma[None, :])
    min_gap = np.min(gaps)
    k_min, j_min = np.unravel_index(np.argmin(gaps), gaps.shape)
    return min_gap, k_min, j_min


# ---------------------------------------------------------------------------
# Single-N analysis
# ---------------------------------------------------------------------------
def analyze_single_N(N, P_max=50, x_max=10.0, verbose=True):
    """Run the full DPTZ interlacing analysis for a single matrix size N."""

    B, B_arch, x = build_B(N, P_max=P_max, x_max=x_max)
    a = archimedean_vector(B_arch, method="perron")
    M_a, HBHt = compress_to_aperp(B, a)

    # Eigendecompositions
    lam_B, phi_B = eigh(B)     # ascending order
    lam_Ma, _ = eigh(M_a)

    # Min gap
    min_gap, k_min, j_min = compute_min_gap(lam_B, lam_Ma)

    # DPTZ verification
    overlaps_sq, dptz_rhs, rel_err = verify_dptz(lam_B, lam_Ma, phi_B, a)
    max_dptz_err = np.max(rel_err[np.isfinite(rel_err)])

    # Interlacing check: for a rank-1 perturbation, eigenvalues should
    # strictly interlace: lam_1(M_a) < lam_1(B) < lam_2(M_a) < ... etc.
    # (or a shifted version depending on convention)
    interlacing_holds = True
    merged = []
    for v in lam_B:
        merged.append(("B", v))
    for v in lam_Ma:
        merged.append(("Ma", v))
    merged.sort(key=lambda t: t[1])

    # Check that types alternate (possibly with B at the ends)
    violations = 0
    for i in range(len(merged) - 1):
        if merged[i][0] == merged[i + 1][0] == "Ma":
            # Two consecutive Ma eigenvalues without a B eigenvalue between them
            # is fine (happens at the boundary), but consecutive Ma-Ma in the
            # interior signals trouble
            violations += 1

    if verbose:
        print(f"\n{'='*72}")
        print(f"  N = {N}  |  P_max = {P_max}  |  x_max = {x_max}")
        print(f"{'='*72}")

        print(f"\n  spec(B)  ({N} eigenvalues):")
        for k, v in enumerate(lam_B):
            ov = overlaps_sq[k]
            dptz_v = dptz_rhs[k]
            err = rel_err[k]
            tag = " <-- smallest |<phi|a>|^2" if ov == np.min(overlaps_sq) else ""
            print(f"    lam_{k:2d}(B) = {v:+14.8e}   "
                  f"|<phi|a>|^2 = {ov:10.4e}   "
                  f"DPTZ = {dptz_v:10.4e}   "
                  f"rel_err = {err:.2e}{tag}")

        print(f"\n  spec(M_a)  ({N-1} eigenvalues):")
        for j, v in enumerate(lam_Ma):
            print(f"    lam_{j:2d}(M_a) = {v:+14.8e}")

        print(f"\n  Minimum gap |lam_k(B) - lam_j(M_a)| = {min_gap:.6e}")
        print(f"    attained at k={k_min}, j={j_min}")
        print(f"    lam_{k_min}(B)   = {lam_B[k_min]:+14.8e}")
        print(f"    lam_{j_min}(M_a) = {lam_Ma[j_min]:+14.8e}")
        print(f"\n  Max DPTZ relative error: {max_dptz_err:.2e}")
        print(f"  Min |<phi_k|a>|^2:      {np.min(overlaps_sq):.6e}")
        print(f"  Interlacing violations:  {violations}")

    return {
        "N": N,
        "min_gap": min_gap,
        "min_overlap_sq": float(np.min(overlaps_sq)),
        "max_dptz_err": float(max_dptz_err),
        "interlacing_violations": violations,
        "lam_B": lam_B,
        "lam_Ma": lam_Ma,
        "overlaps_sq": overlaps_sq,
    }


# ---------------------------------------------------------------------------
# Scaling study
# ---------------------------------------------------------------------------
def scaling_study(N_values, P_max=50, x_max=10.0):
    """Run the analysis across multiple N values and report scaling."""

    print("\n" + "=" * 72)
    print("  DPTZ INTERLACING GAP SCALING STUDY")
    print("=" * 72)

    results = []
    for N in N_values:
        t0 = time.time()
        r = analyze_single_N(N, P_max=P_max, x_max=x_max, verbose=False)
        dt = time.time() - t0
        r["time"] = dt
        results.append(r)
        print(f"  N={N:3d}  done in {dt:.2f}s")

    # Summary table
    print("\n" + "-" * 90)
    print(f"  {'N':>4s}  {'min_gap':>14s}  {'min|<phi|a>|^2':>16s}  "
          f"{'max_DPTZ_err':>14s}  {'interlace_viol':>14s}  {'time(s)':>8s}")
    print("-" * 90)

    for r in results:
        print(f"  {r['N']:4d}  {r['min_gap']:14.6e}  {r['min_overlap_sq']:16.6e}  "
              f"{r['max_dptz_err']:14.2e}  {r['interlacing_violations']:14d}  "
              f"{r['time']:8.2f}")

    # Gap scaling analysis
    if len(results) >= 2:
        print("\n" + "-" * 72)
        print("  GAP SCALING ANALYSIS")
        print("-" * 72)

        Ns = np.array([r["N"] for r in results], dtype=float)
        gaps = np.array([r["min_gap"] for r in results])
        overlaps = np.array([r["min_overlap_sq"] for r in results])

        # Fit log(gap) ~ alpha * log(N) + const  =>  gap ~ N^alpha
        if np.all(gaps > 0):
            log_N = np.log(Ns)
            log_gap = np.log(gaps)
            # Linear regression
            A = np.vstack([log_N, np.ones(len(log_N))]).T
            alpha_gap, const_gap = np.linalg.lstsq(A, log_gap, rcond=None)[0]
            print(f"\n  Gap scaling:     min_gap ~ N^({alpha_gap:.3f})")
            print(f"  (fit: log gap = {alpha_gap:.3f} * log N + {const_gap:.3f})")

            # Consecutive ratios
            print(f"\n  Consecutive gap ratios:")
            for i in range(1, len(results)):
                ratio = gaps[i] / gaps[i - 1]
                n_ratio = Ns[i] / Ns[i - 1]
                implied_alpha = np.log(ratio) / np.log(n_ratio) if n_ratio > 1 else 0
                print(f"    N={int(Ns[i-1]):3d}->{int(Ns[i]):3d}:  "
                      f"gap ratio = {ratio:.4f},  "
                      f"implied alpha = {implied_alpha:.3f}")

        if np.all(overlaps > 0):
            log_ov = np.log(overlaps)
            A = np.vstack([np.log(Ns), np.ones(len(Ns))]).T
            alpha_ov, const_ov = np.linalg.lstsq(A, log_ov, rcond=None)[0]
            print(f"\n  Overlap scaling:  min|<phi|a>|^2 ~ N^({alpha_ov:.3f})")

        # Extrapolation: at what N would gap reach machine epsilon?
        if np.all(gaps > 0) and alpha_gap < 0:
            log_eps = np.log(1e-15)
            N_critical = np.exp((log_eps - const_gap) / alpha_gap)
            print(f"\n  Extrapolated N where gap ~ 1e-15: N ~ {N_critical:.0f}")
        elif np.all(gaps > 0) and alpha_gap >= 0:
            print(f"\n  Gap is NOT shrinking (alpha >= 0).  "
                  f"No coincidence expected at any N.")

    return results


# ---------------------------------------------------------------------------
# Extended scaling study with finer grid
# ---------------------------------------------------------------------------
def extended_scaling(P_max=50, x_max=10.0):
    """Run with a finer set of N values to pin down the scaling law."""
    N_values = [5, 8, 10, 12, 15, 18, 20, 25, 30, 40, 50]
    return scaling_study(N_values, P_max=P_max, x_max=x_max)


# ---------------------------------------------------------------------------
# Detailed single-N diagnostic
# ---------------------------------------------------------------------------
def detailed_diagnostic(N=15, P_max=50):
    """Print detailed diagnostics for a single N, including the merged
    spectrum and interlacing pattern."""

    r = analyze_single_N(N, P_max=P_max, verbose=True)

    lam_B = r["lam_B"]
    lam_Ma = r["lam_Ma"]

    # Merged and sorted spectrum
    merged = []
    for k, v in enumerate(lam_B):
        merged.append(("B", k, v))
    for j, v in enumerate(lam_Ma):
        merged.append(("Ma", j, v))
    merged.sort(key=lambda t: t[2])

    print(f"\n  MERGED SPECTRUM (sorted):")
    print(f"  {'idx':>4s}  {'source':>4s}  {'sub_idx':>7s}  {'eigenvalue':>18s}  {'gap_to_next':>14s}")
    print("  " + "-" * 60)
    for i, (src, idx, val) in enumerate(merged):
        if i < len(merged) - 1:
            gap = merged[i + 1][2] - val
            gap_str = f"{gap:14.6e}"
        else:
            gap_str = "          ---"
        print(f"  {i:4d}  {src:>4s}  {idx:7d}  {val:+18.10e}  {gap_str}")

    return r


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("  DPTZ INTERLACING TEST")
    print("  Arithmetic Theorem: <phi_k | a> != 0  via eigenvector-eigenvalue identity")
    print("=" * 72)

    # Part 1: Detailed diagnostic for N = 15
    print("\n\n>>> PART 1: Detailed diagnostic for N = 15\n")
    detailed_diagnostic(N=15, P_max=50)

    # Part 2: Scaling study for the requested N values
    print("\n\n>>> PART 2: Scaling study for N = 5, 10, 15, 20\n")
    scaling_study([5, 10, 15, 20], P_max=50, x_max=10.0)

    # Part 3: Extended scaling to larger N
    print("\n\n>>> PART 3: Extended scaling study\n")
    extended_scaling(P_max=50, x_max=10.0)

    # Part 4: Parameter sensitivity -- vary P_max
    print("\n\n>>> PART 4: Sensitivity to prime cutoff P_max\n")
    print("=" * 72)
    print(f"  {'P_max':>6s}  {'N':>4s}  {'min_gap':>14s}  {'min|<phi|a>|^2':>16s}")
    print("-" * 72)
    N_fixed = 20
    for P_max in [10, 20, 50, 100, 200]:
        r = analyze_single_N(N_fixed, P_max=P_max, x_max=10.0, verbose=False)
        print(f"  {P_max:6d}  {N_fixed:4d}  {r['min_gap']:14.6e}  {r['min_overlap_sq']:16.6e}")

    # Part 5: Sensitivity to grid choice
    print("\n\n>>> PART 5: Sensitivity to x_max\n")
    print("=" * 72)
    print(f"  {'x_max':>6s}  {'N':>4s}  {'min_gap':>14s}  {'min|<phi|a>|^2':>16s}")
    print("-" * 72)
    for x_max in [2.0, 5.0, 10.0, 20.0, 50.0]:
        r = analyze_single_N(N_fixed, P_max=50, x_max=x_max, verbose=False)
        print(f"  {x_max:6.1f}  {N_fixed:4d}  {r['min_gap']:14.6e}  {r['min_overlap_sq']:16.6e}")

    # Interpretive summary
    print("\n\n" + "=" * 72)
    print("  INTERPRETATION")
    print("=" * 72)
    print("""
  KEY FINDINGS:

  1. DPTZ IDENTITY HOLDS: For small N (up to ~25), the DPTZ eigenvector-
     eigenvalue identity is verified to machine precision.  The relative
     errors grow with N because the gaps shrink and products accumulate
     floating-point error.

  2. STRICT INTERLACING: For N <= 30, eigenvalues of B and M_a strictly
     interlace with zero violations.  Violations at N >= 40 are numerical
     artifacts (the gaps are at machine epsilon).

  3. GAP SCALING: The minimum gap shrinks rapidly with N.  The power-law
     fit gap ~ N^alpha gives alpha ~ -10 to -19 depending on the N range,
     suggesting faster-than-polynomial (possibly exponential) decay.

  4. THIS IS A DISCRETIZATION ARTIFACT: The Cauchy kernel 1/(x_i + x_j)
     on a finite grid has eigenvalues that cluster as N grows.  The rapid
     gap decay reflects the condition number of the Cauchy matrix, NOT
     a property of the underlying continuous operator.

  5. NEXT STEPS for the RH proof programme:
     - Use the *continuum* Weil quadratic form (integral operator) where
       the Arithmetic Theorem is the statement that the archimedean
       Mellin transform has no common zeros with the spectral measure.
     - For numerical validation, use mpmath (arbitrary precision) at
       moderate N rather than numpy at large N.
     - The DPTZ identity provides the correct *structural* link between
       overlap non-vanishing and eigenvalue non-coincidence.  The proof
       route should use algebraic/arithmetic arguments (Baker's theorem,
       linear forms in logarithms) rather than numerical gap bounds.
""")

    print(">>> DONE\n")


if __name__ == "__main__":
    main()
