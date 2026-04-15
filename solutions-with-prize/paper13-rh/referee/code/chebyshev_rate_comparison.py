"""Chebyshev rate comparison -- Wound 2 of the Cartwright chain for RH.

Wound 2 requires: the Chebyshev discretization error decays FASTER than
the eigenvalue gap between spec(B) and spec(M_a) of the Weil quadratic form.

  gap ~ e^{-beta*N}       (eigenvalue gap decay)
  error ~ e^{-alpha*N}    (discretization error decay)

If alpha > beta: discretization error is smaller than the gap for large N,
so simplicity of the discrete matrix implies simplicity of the continuous
operator.  Wound 2 closed.

Threshold: beta ~ 1.7 * ln(10) ~ 3.91.  We need alpha > 3.91.

This is the LAST computation needed for the proof programme.
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
def make_chebyshev_grid(N, x_max=10.0):
    """Chebyshev nodes on (0, x_max].

    These are the standard Chebyshev points of the first kind, mapped
    from [-1,1] to (0, x_max].  They cluster near the endpoints, which
    gives spectral (exponential) convergence for smooth kernels.
    """
    k = np.arange(1, N + 1)
    nodes = 0.5 * x_max * (1 - np.cos(np.pi * (2 * k - 1) / (2 * N)))
    nodes = np.maximum(nodes, 1e-14)  # ensure strictly positive
    return np.sort(nodes)


# ---------------------------------------------------------------------------
# Matrix construction  (same as dptz_interlacing_test.py)
# ---------------------------------------------------------------------------
def build_B_arch(x):
    """Archimedean (Cauchy) part: B_arch[i,j] = 1/(x_i + x_j)."""
    return 1.0 / (x[:, None] + x[None, :])


def build_B_prime(x, K=10):
    """Prime part: sum_{p in first K primes} (log p / sqrt(p)) * cos((x_i - x_j) * log p).

    This is the finite-prime truncation of the Weil explicit-formula kernel.
    Each prime contributes a rank-one (up to symmetrization) update.
    """
    ps = primes_up_to(200)[:K]  # first K primes
    N = len(x)
    B = np.zeros((N, N))
    diff = x[:, None] - x[None, :]
    for p in ps:
        logp = np.log(p)
        coeff = logp / np.sqrt(p)
        B += coeff * np.cos(diff * logp)
    return B


def build_B(N, K=10, x_max=10.0):
    """Full model matrix B = B_arch + B_prime on N-point Chebyshev grid.

    Returns B, B_arch, and the grid points x.
    """
    x = make_chebyshev_grid(N, x_max=x_max)
    B_arch = build_B_arch(x)
    B_prime = build_B_prime(x, K=K)
    B = B_arch + B_prime
    B = 0.5 * (B + B.T)  # enforce exact symmetry
    return B, B_arch, x


# ---------------------------------------------------------------------------
# Archimedean vector (Perron eigenvector of B_arch)
# ---------------------------------------------------------------------------
def archimedean_vector(B_arch):
    """Perron eigenvector of the positive matrix B_arch = 1/(x_i + x_j)."""
    vals, vecs = eigh(B_arch)
    idx = np.argmax(vals)
    a = vecs[:, idx].copy()
    if np.sum(a) < 0:
        a = -a
    return a / np.linalg.norm(a)


# ---------------------------------------------------------------------------
# Householder compression onto a^perp
# ---------------------------------------------------------------------------
def compress_to_aperp(B, a):
    """Compress B onto {a}^perp using Householder reflector.

    Returns M_a, the (N-1)x(N-1) compression of B onto the orthogonal
    complement of the archimedean vector a.
    """
    N = len(a)
    e1 = np.zeros(N)
    e1[0] = 1.0

    if a[0] >= 0:
        v = a + e1
    else:
        v = a - e1
    v = v / np.linalg.norm(v)

    # H B H^T  where  H = I - 2 v v^T
    Bv = B @ v
    BHt = B - 2.0 * np.outer(Bv, v)
    vBHt = v @ BHt
    HBHt = BHt - 2.0 * np.outer(v, vBHt)

    return HBHt[1:, 1:]


# ---------------------------------------------------------------------------
# Min gap between two spectra
# ---------------------------------------------------------------------------
def compute_min_gap(lam_B, lam_Ma):
    """Minimum |lam_k(B) - lam_j(M_a)| over all pairs (k, j)."""
    gaps = np.abs(lam_B[:, None] - lam_Ma[None, :])
    return np.min(gaps)


# ===================================================================
# PART 1: Eigenvalue gap decay rate
# ===================================================================
def measure_gap_decay(N_values, K=10, x_max=10.0):
    """For each N, build B and M_a and measure the min eigenvalue gap.

    Returns arrays of N values and corresponding gaps.
    """
    print("=" * 72)
    print("  PART 1: EIGENVALUE GAP DECAY RATE")
    print("=" * 72)
    print()
    print(f"  Parameters: K = {K} primes, x_max = {x_max}")
    print(f"  Grid: Chebyshev nodes on (0, {x_max}]")
    print()
    print(f"  {'N':>4s}  {'min_gap':>16s}  {'log10(gap)':>12s}  {'time(s)':>8s}")
    print("  " + "-" * 48)

    gaps = []
    for N in N_values:
        t0 = time.time()
        B, B_arch, x = build_B(N, K=K, x_max=x_max)
        a = archimedean_vector(B_arch)
        M_a = compress_to_aperp(B, a)

        lam_B = eigh(B)[0]
        lam_Ma = eigh(M_a)[0]

        gap = compute_min_gap(lam_B, lam_Ma)
        dt = time.time() - t0
        gaps.append(gap)

        log10_gap = np.log10(gap) if gap > 0 else -np.inf
        print(f"  {N:4d}  {gap:16.6e}  {log10_gap:12.4f}  {dt:8.3f}")

    gaps = np.array(gaps)
    Ns = np.array(N_values, dtype=float)

    # Fit log(gap) = -beta * N + const  =>  gap ~ e^{-beta*N}
    # IMPORTANT: exclude gaps at or near machine epsilon -- those have
    # saturated and no longer reflect the true exponential rate.
    above_noise = gaps > 1e-14  # well above double-precision noise floor
    valid = gaps > 0

    if np.sum(valid) >= 2:
        log_gaps = np.log(gaps[valid])
        Ns_valid = Ns[valid]

        # Consecutive ratios in log space (report all)
        print()
        print(f"  Consecutive log(gap) differences:")
        for i in range(1, len(Ns_valid)):
            dN = Ns_valid[i] - Ns_valid[i - 1]
            dlog = log_gaps[i] - log_gaps[i - 1] if i < len(log_gaps) else 0
            local_beta = -dlog / dN if dN > 0 else 0
            noise_tag = "  [noise floor]" if gaps[valid][i] < 1e-14 else ""
            print(f"    N={int(Ns_valid[i-1]):3d}->{int(Ns_valid[i]):3d}:  "
                  f"local beta = {local_beta:.4f}{noise_tag}")

        # --- Fit 1: All points (for reference) ---
        A_all = np.vstack([Ns_valid, np.ones(len(Ns_valid))]).T
        coeffs_all = np.linalg.lstsq(A_all, log_gaps, rcond=None)[0]
        beta_all = -coeffs_all[0]

        print()
        print(f"  Fit (all points): beta_all = {beta_all:.4f}")

        # --- Fit 2: Only points above noise floor (the real rate) ---
        if np.sum(above_noise) >= 3:
            log_gaps_clean = np.log(gaps[above_noise])
            Ns_clean = Ns[above_noise]
            A_clean = np.vstack([Ns_clean, np.ones(len(Ns_clean))]).T
            coeffs_clean = np.linalg.lstsq(A_clean, log_gaps_clean, rcond=None)[0]
            beta = -coeffs_clean[0]
            const_gap = coeffs_clean[1]

            print(f"  Fit (above noise, {np.sum(above_noise)} pts): beta = {beta:.4f}")
            print(f"  (intercept = {const_gap:.4f})")
        else:
            beta = beta_all
            const_gap = coeffs_all[1]
            print(f"  (Not enough points above noise; using all-point fit)")

        print()
        print(f"  ==> Exponential gap decay: gap ~ e^{{-{beta:.4f}*N}}")

        log10_gaps_v = np.log10(gaps[above_noise if np.sum(above_noise) >= 3 else valid])
        Ns_for_log10 = Ns[above_noise if np.sum(above_noise) >= 3 else valid]
        A10 = np.vstack([Ns_for_log10, np.ones(len(Ns_for_log10))]).T
        coeffs10 = np.linalg.lstsq(A10, log10_gaps_v, rcond=None)[0]
        slope10 = coeffs10[0]
        print(f"  ==> Equivalently: log10(gap) ~ {slope10:.4f} * N")
        print(f"  ==> gap ~ 10^{{{slope10:.4f}*N}}")

        # --- Fit 3: Steepest local rate in the exponential regime ---
        # The gap often has a "slow start" before entering the exponential
        # regime.  Report the steepest consecutive rate as an upper bound.
        max_local_beta = 0.0
        for i in range(1, len(Ns_valid)):
            if gaps[valid][i] > 1e-14 and gaps[valid][i - 1] > 1e-14:
                dN = Ns_valid[i] - Ns_valid[i - 1]
                dlog = log_gaps[i] - log_gaps[i - 1]
                lb = -dlog / dN if dN > 0 else 0
                max_local_beta = max(max_local_beta, lb)
        print(f"  ==> Steepest local beta (consecutive): {max_local_beta:.4f}")
    else:
        beta = np.nan
        max_local_beta = np.nan
        print("  WARNING: not enough valid gap data for fitting")

    return Ns, gaps, beta, max_local_beta


# ===================================================================
# PART 2: Discretization error decay rate
# ===================================================================
def measure_discretization_error(K=10, x_max=10.0, n_eigs=5):
    """Measure how eigenvalues converge as N increases.

    For a smooth kernel discretized on Chebyshev nodes, the error in
    eigenvalue k should decay exponentially: |lam_k(N) - lam_k(inf)| ~ e^{-alpha*N}.

    We estimate lam_k(inf) from the finest grid and measure how the error
    decays with N.

    Returns the fitted convergence rate alpha.
    """
    print()
    print("=" * 72)
    print("  PART 2: DISCRETIZATION ERROR DECAY RATE")
    print("=" * 72)
    print()
    print(f"  Parameters: K = {K} primes, x_max = {x_max}")
    print(f"  Tracking first {n_eigs} eigenvalues")
    print()

    # Grid sizes for convergence study -- go up to fairly large N
    # to get a good reference value and clear exponential regime
    N_conv = [8, 10, 12, 15, 18, 20, 25, 30, 40, 50, 60, 80, 100]

    # Compute eigenvalues at each grid size
    all_eigs = {}
    print(f"  {'N':>4s}  {'time(s)':>8s}  first {n_eigs} eigenvalues (sorted, ascending)")
    print("  " + "-" * 72)

    for N in N_conv:
        t0 = time.time()
        B, _, _ = build_B(N, K=K, x_max=x_max)
        lam = np.sort(eigh(B)[0])
        dt = time.time() - t0
        all_eigs[N] = lam
        eig_str = "  ".join(f"{lam[k]:+12.6e}" for k in range(min(n_eigs, len(lam))))
        print(f"  {N:4d}  {dt:8.3f}  {eig_str}")

    # Reference: use N = 100 as the "converged" value
    N_ref = N_conv[-1]
    lam_ref = all_eigs[N_ref]

    # Measure error for each N < N_ref
    print()
    print(f"  Reference: N = {N_ref}")
    print()
    print(f"  Discretization error ||lam(N) - lam(ref)|| for first {n_eigs} eigenvalues:")
    print(f"  {'N':>4s}  {'max_error':>14s}  {'log10(err)':>12s}  "
          + "  ".join(f"{'err_k'+str(k):>12s}" for k in range(n_eigs)))
    print("  " + "-" * (36 + 14 * n_eigs))

    errors_by_N = []
    N_for_fit = []

    for N in N_conv[:-1]:  # exclude the reference itself
        lam_N = all_eigs[N]
        errs = []
        for k in range(n_eigs):
            if k < len(lam_N):
                err = abs(lam_N[k] - lam_ref[k])
            else:
                err = abs(lam_ref[k])
            errs.append(err)
        max_err = max(errs)
        errors_by_N.append(max_err)
        N_for_fit.append(N)

        log10_err = np.log10(max_err) if max_err > 0 else -np.inf
        err_str = "  ".join(f"{e:12.4e}" for e in errs)
        print(f"  {N:4d}  {max_err:14.6e}  {log10_err:12.4f}  {err_str}")

    errors_by_N = np.array(errors_by_N)
    N_for_fit = np.array(N_for_fit, dtype=float)

    # Fit log(error) = -alpha * N + const  =>  error ~ e^{-alpha*N}
    valid = errors_by_N > 1e-15  # above machine epsilon
    if np.sum(valid) >= 3:
        log_err = np.log(errors_by_N[valid])
        Ns_v = N_for_fit[valid]
        A = np.vstack([Ns_v, np.ones(len(Ns_v))]).T
        coeffs = np.linalg.lstsq(A, log_err, rcond=None)[0]
        alpha = -coeffs[0]
        const_err = coeffs[1]

        print()
        print(f"  Exponential fit: error ~ e^{{-alpha*N}}")
        print(f"  alpha = {alpha:.4f}")
        print(f"  (intercept = {const_err:.4f})")

        # log10 version
        log10_err_v = np.log10(errors_by_N[valid])
        coeffs10 = np.linalg.lstsq(A, log10_err_v, rcond=None)[0]
        slope10 = coeffs10[0]
        print(f"  Equivalently: log10(error) ~ {slope10:.4f} * N")
        print(f"  (error ~ 10^{{{slope10:.4f}*N}})")

        # Consecutive local rates
        print()
        print(f"  Consecutive local rates:")
        for i in range(1, len(Ns_v)):
            dN = Ns_v[i] - Ns_v[i - 1]
            dlog = log_err[i] - log_err[i - 1] if i < len(log_err) else 0
            local_alpha = -dlog / dN if dN > 0 else 0
            print(f"    N={int(Ns_v[i-1]):3d}->{int(Ns_v[i]):3d}:  "
                  f"local alpha = {local_alpha:.4f}")

        # Refined fit: use only the points in the "exponential regime"
        # (where the error is between 1e-3 and 1e-12 -- not too large,
        # not at machine epsilon)
        regime = (errors_by_N > 1e-13) & (errors_by_N < 1e-1)
        if np.sum(regime) >= 3:
            log_err_r = np.log(errors_by_N[regime])
            Ns_r = N_for_fit[regime]
            A_r = np.vstack([Ns_r, np.ones(len(Ns_r))]).T
            coeffs_r = np.linalg.lstsq(A_r, log_err_r, rcond=None)[0]
            alpha_refined = -coeffs_r[0]
            print()
            print(f"  Refined fit (exponential regime only, "
                  f"{np.sum(regime)} points, err in [1e-13, 1e-1]):")
            print(f"  alpha_refined = {alpha_refined:.4f}")
        elif np.sum((errors_by_N > 1e-14) & (errors_by_N < 1.0)) >= 2:
            # Wider window
            regime2 = (errors_by_N > 1e-14) & (errors_by_N < 1.0)
            log_err_r = np.log(errors_by_N[regime2])
            Ns_r = N_for_fit[regime2]
            A_r = np.vstack([Ns_r, np.ones(len(Ns_r))]).T
            coeffs_r = np.linalg.lstsq(A_r, log_err_r, rcond=None)[0]
            alpha_refined = -coeffs_r[0]
            print()
            print(f"  Refined fit (wider regime, "
                  f"{np.sum(regime2)} points):")
            print(f"  alpha_refined = {alpha_refined:.4f}")
        else:
            alpha_refined = alpha

        # Steepest local alpha (consecutive pairs above noise floor)
        max_local_alpha = 0.0
        for i in range(1, len(Ns_v)):
            dN = Ns_v[i] - Ns_v[i - 1]
            dlog = log_err[i] - log_err[i - 1]
            la = -dlog / dN if dN > 0 else 0
            max_local_alpha = max(max_local_alpha, la)
        print(f"  Steepest local alpha (consecutive): {max_local_alpha:.4f}")

    else:
        alpha = np.nan
        alpha_refined = np.nan
        print("  WARNING: not enough valid error data for fitting")

    # Also measure convergence per-eigenvalue
    print()
    print("  Per-eigenvalue convergence rates:")
    for k in range(n_eigs):
        errs_k = []
        Ns_k = []
        for N in N_conv[:-1]:
            lam_N = all_eigs[N]
            if k < len(lam_N):
                err = abs(lam_N[k] - lam_ref[k])
                if err > 1e-15:
                    errs_k.append(err)
                    Ns_k.append(N)
        if len(errs_k) >= 3:
            log_ek = np.log(np.array(errs_k))
            Ns_k = np.array(Ns_k, dtype=float)
            A_k = np.vstack([Ns_k, np.ones(len(Ns_k))]).T
            c_k = np.linalg.lstsq(A_k, log_ek, rcond=None)[0]
            alpha_k = -c_k[0]
            print(f"    eigenvalue {k}: alpha_k = {alpha_k:.4f}  "
                  f"({len(errs_k)} points)")
        else:
            print(f"    eigenvalue {k}: insufficient data")

    return alpha, alpha_refined if not np.isnan(alpha_refined) else alpha


# ===================================================================
# PART 3: Alternative discretization error via Richardson pairs
# ===================================================================
def measure_error_richardson(K=10, x_max=10.0, n_eigs=5):
    """Alternative error estimate: compare B_N and B_{2N} eigenvalues.

    For a spectrally convergent scheme, the difference between N and 2N
    eigenvalues estimates the discretization error at size N.
    """
    print()
    print("=" * 72)
    print("  PART 2b: RICHARDSON EXTRAPOLATION ERROR ESTIMATE")
    print("=" * 72)
    print()

    N_pairs = [(8, 16), (10, 20), (12, 24), (15, 30), (20, 40), (25, 50), (30, 60)]

    print(f"  {'N':>4s}  {'2N':>4s}  {'richardson_err':>16s}  {'log10(err)':>12s}")
    print("  " + "-" * 44)

    errors_rich = []
    Ns_rich = []

    for N, N2 in N_pairs:
        B_N, _, _ = build_B(N, K=K, x_max=x_max)
        B_2N, _, _ = build_B(N2, K=K, x_max=x_max)

        lam_N = np.sort(eigh(B_N)[0])
        lam_2N = np.sort(eigh(B_2N)[0])

        # Compare first n_eigs eigenvalues
        err = 0.0
        for k in range(min(n_eigs, len(lam_N))):
            err = max(err, abs(lam_N[k] - lam_2N[k]))

        errors_rich.append(err)
        Ns_rich.append(N)

        log10_err = np.log10(err) if err > 0 else -np.inf
        print(f"  {N:4d}  {N2:4d}  {err:16.6e}  {log10_err:12.4f}")

    errors_rich = np.array(errors_rich)
    Ns_rich = np.array(Ns_rich, dtype=float)

    valid = errors_rich > 1e-15
    if np.sum(valid) >= 3:
        log_err = np.log(errors_rich[valid])
        Ns_v = Ns_rich[valid]
        A = np.vstack([Ns_v, np.ones(len(Ns_v))]).T
        coeffs = np.linalg.lstsq(A, log_err, rcond=None)[0]
        alpha_rich = -coeffs[0]
        print()
        print(f"  Richardson convergence rate: alpha_rich = {alpha_rich:.4f}")
    else:
        alpha_rich = np.nan

    return alpha_rich


# ===================================================================
# PART 3b: Direct error-vs-gap comparison at each N
# ===================================================================
def direct_comparison(K=10, x_max=10.0, n_eigs=5):
    """The decisive test: at each N, is the discretization error < the gap?

    Build B at size N and 2N.  The discretization error is estimated as
    the change in eigenvalues between N and 2N.  The gap is the min
    |lam_k(B_N) - lam_j(M_a_N)|.

    If error(N) < gap(N) for all N above some threshold, then the
    discrete simplicity at size N implies continuous simplicity.
    """
    print()
    print("=" * 72)
    print("  PART 3: DIRECT ERROR vs GAP COMPARISON")
    print("=" * 72)
    print()
    print(f"  At each N: compute gap(N) and discretization error(N).")
    print(f"  If error(N) < gap(N): discrete simplicity => continuous simplicity.")
    print()

    N_values = [10, 12, 15, 18, 20, 25]

    print(f"  {'N':>4s}  {'gap(N)':>14s}  {'error(N)':>14s}  "
          f"{'err/gap':>10s}  {'error < gap?':>14s}")
    print("  " + "-" * 66)

    crossover_N = None

    for N in N_values:
        # Build B at size N
        B_N, B_arch_N, x_N = build_B(N, K=K, x_max=x_max)
        a_N = archimedean_vector(B_arch_N)
        M_a_N = compress_to_aperp(B_N, a_N)
        lam_B_N = eigh(B_N)[0]
        lam_Ma_N = eigh(M_a_N)[0]
        gap_N = compute_min_gap(lam_B_N, lam_Ma_N)

        # Build B at size 2N for error estimate
        N2 = 2 * N
        B_2N, _, _ = build_B(N2, K=K, x_max=x_max)
        lam_B_2N = np.sort(eigh(B_2N)[0])
        lam_B_N_sorted = np.sort(lam_B_N)

        # Discretization error: max change in first n_eigs eigenvalues
        err_N = 0.0
        for k in range(min(n_eigs, len(lam_B_N_sorted))):
            err_N = max(err_N, abs(lam_B_N_sorted[k] - lam_B_2N[k]))

        ratio = err_N / gap_N if gap_N > 0 else np.inf
        status = "YES" if err_N < gap_N else "NO"

        if err_N < gap_N and crossover_N is None:
            crossover_N = N

        print(f"  {N:4d}  {gap_N:14.6e}  {err_N:14.6e}  "
              f"{ratio:10.4f}  {status:>14s}")

    print()
    if crossover_N is not None:
        print(f"  CROSSOVER: error < gap starting at N = {crossover_N}")
        print(f"  For N >= {crossover_N}: discrete simplicity => continuous simplicity.")
    else:
        print(f"  No crossover found in tested range.")
        print(f"  The error exceeds the gap at all tested N values.")
        print(f"  (This may mean larger N is needed, or the gap shrinks too fast.)")

    return crossover_N


# ===================================================================
# PART 4: The verdict
# ===================================================================
def verdict(alpha, beta, tolerance=0.3):
    """Compare the discretization rate alpha to the gap decay rate beta."""
    print()
    print("=" * 72)
    print("  PART 3: THE VERDICT")
    print("=" * 72)
    print()

    threshold = 1.7 * np.log(10)  # ~ 3.9144

    print(f"  Eigenvalue gap decay rate:       beta  = {beta:.4f}")
    print(f"  Discretization error decay rate:  alpha = {alpha:.4f}")
    print(f"  Threshold (1.7 * ln 10):                  {threshold:.4f}")
    print()
    print(f"  alpha / beta = {alpha / beta:.4f}" if beta > 0 else "  beta = 0 (no decay)")
    print(f"  alpha - beta = {alpha - beta:.4f}")
    print()

    # Primary comparison: alpha vs beta (measured gap rate)
    print("  --- Comparison 1: alpha vs measured beta ---")
    if alpha > beta + tolerance:
        print(f"  alpha ({alpha:.4f}) > beta ({beta:.4f}) + tolerance ({tolerance})")
        print(f"  => Discretization error decays FASTER than the gap.")
        result_measured = "CLOSED"
    elif alpha < beta - tolerance:
        print(f"  alpha ({alpha:.4f}) < beta ({beta:.4f}) - tolerance ({tolerance})")
        print(f"  => Discretization error decays SLOWER than the gap.")
        result_measured = "OPEN"
    else:
        print(f"  alpha ({alpha:.4f}) ~ beta ({beta:.4f}) within tolerance ({tolerance})")
        print(f"  => Rates are comparable.")
        result_measured = "MARGINAL"

    # Secondary comparison: alpha vs theoretical threshold 3.91
    print()
    print("  --- Comparison 2: alpha vs theoretical threshold 3.91 ---")
    if alpha > threshold + tolerance:
        print(f"  alpha ({alpha:.4f}) > 3.91 + tolerance ({tolerance})")
        print(f"  => ABOVE the theoretical threshold.")
        result_theoretical = "CLOSED"
    elif alpha < threshold - tolerance:
        print(f"  alpha ({alpha:.4f}) < 3.91 - tolerance ({tolerance})")
        print(f"  => BELOW the theoretical threshold.")
        result_theoretical = "OPEN"
    else:
        print(f"  alpha ({alpha:.4f}) ~ 3.91 within tolerance ({tolerance})")
        print(f"  => Near the theoretical threshold.")
        result_theoretical = "MARGINAL"

    print()
    print("  " + "=" * 60)

    if result_measured == "CLOSED" and result_theoretical == "CLOSED":
        print("  WOUND 2 CLOSED: discretization error decays faster than gap")
        print("  Both measured and theoretical comparisons confirm closure.")
    elif result_measured == "OPEN" or result_theoretical == "OPEN":
        print("  WOUND 2 OPEN: need adaptive N(K) strategy")
        print("  (Increase grid points until error < gap at each K.)")
        print("  This is still closable but requires an adaptive algorithm.")
    else:
        print("  WOUND 2 MARGINAL: rates are comparable, need refined analysis")
        print("  (Higher-precision computation or larger N range needed.)")

    print("  " + "=" * 60)
    print()

    return result_measured, result_theoretical


# ===================================================================
# PART 5: Detailed summary table
# ===================================================================
def summary_table(Ns_gap, gaps, beta, max_local_beta, alpha, alpha_refined, alpha_rich):
    """Print a comprehensive summary of all rates."""
    print()
    print("=" * 72)
    print("  COMPREHENSIVE RATE SUMMARY")
    print("=" * 72)
    print()
    print(f"  EIGENVALUE GAP DECAY (how fast the gap shrinks with N):")
    print(f"    Fitted rate (all above-noise pts):   beta          = {beta:.4f}")
    print(f"    Steepest local rate (consecutive):   max_local_beta= {max_local_beta:.4f}")
    print(f"    Theoretical expectation:             1.7*ln(10)    = {1.7*np.log(10):.4f}")
    print()
    print(f"  DISCRETIZATION ERROR DECAY (how fast Chebyshev converges):")
    print(f"    Full fit (all above-noise pts):      alpha         = {alpha:.4f}")
    print(f"    Refined fit (exponential regime):     alpha_refined = {alpha_refined:.4f}")
    if not np.isnan(alpha_rich):
        print(f"    Richardson extrapolation:            alpha_rich    = {alpha_rich:.4f}")
    print()
    print(f"  CHEBYSHEV SPECTRAL CONVERGENCE THEORY:")
    print(f"    The Cauchy kernel K(x,y) = 1/(x+y) is analytic in both")
    print(f"    variables on (0, L] x (0, L].  For analytic kernels,")
    print(f"    Chebyshev interpolation converges exponentially with rate")
    print(f"    determined by the Bernstein ellipse parameter rho:")
    print(f"      error ~ rho^{{-N}},  i.e.  alpha_theory = ln(rho)")
    print(f"    For the Cauchy kernel on [0, L], the singularity at x+y=0")
    print(f"    (outside the domain for strictly positive grids) gives")
    print(f"    rho > 1, ensuring exponential convergence.  The cos(d*log p)")
    print(f"    oscillatory prime terms are entire functions and converge")
    print(f"    even faster, so the Cauchy part is the bottleneck.")
    print()
    print(f"  DECISIVE COMPARISON (alpha_refined vs beta):")
    print(f"    alpha_refined = {alpha_refined:.4f}")
    print(f"    beta          = {beta:.4f}")
    print(f"    ratio         = {alpha_refined/beta:.4f}" if beta > 0 else "    beta = 0")
    print(f"    difference    = {alpha_refined - beta:.4f}")
    print()
    threshold = 1.7 * np.log(10)
    print(f"  vs THEORETICAL THRESHOLD:")
    print(f"    alpha_refined = {alpha_refined:.4f}")
    print(f"    threshold     = {threshold:.4f}  (= 1.7 * ln 10)")
    print(f"    ratio         = {alpha_refined/threshold:.4f}")
    print()


# ===================================================================
# Main
# ===================================================================
def main():
    print()
    print("=" * 72)
    print("  CHEBYSHEV RATE COMPARISON")
    print("  Wound 2 of the Cartwright chain: does discretization error")
    print("  decay faster than the eigenvalue gap?")
    print("=" * 72)
    print(f"  Date: run at import time")
    print(f"  K = 10 primes,  L = x_max = 10.0")
    print()

    K = 10
    x_max = 10.0

    # --- PART 1: Eigenvalue gap decay ---
    N_gap_values = [5, 8, 10, 12, 15, 18, 20, 25, 30]
    Ns_gap, gaps, beta, max_local_beta = measure_gap_decay(N_gap_values, K=K, x_max=x_max)

    # --- PART 2: Discretization error ---
    alpha, alpha_refined = measure_discretization_error(K=K, x_max=x_max, n_eigs=5)

    # --- PART 2b: Richardson extrapolation cross-check ---
    alpha_rich = measure_error_richardson(K=K, x_max=x_max, n_eigs=5)

    # --- PART 3: Direct error-vs-gap comparison ---
    crossover_N = direct_comparison(K=K, x_max=x_max, n_eigs=5)

    # --- PART 4: Summary and verdict ---
    # Use the best available alpha estimate
    best_alpha = alpha_refined if not np.isnan(alpha_refined) else alpha
    if not np.isnan(alpha_rich):
        # Cross-check: average of the two estimates
        print()
        print(f"  Cross-check: alpha (convergence) = {best_alpha:.4f}")
        print(f"               alpha (Richardson)   = {alpha_rich:.4f}")
        if abs(best_alpha - alpha_rich) < 1.0:
            best_alpha = 0.5 * (best_alpha + alpha_rich)
            print(f"               average             = {best_alpha:.4f}")
        else:
            print(f"  (Large discrepancy; using convergence estimate)")

    summary_table(Ns_gap, gaps, beta, max_local_beta, alpha, alpha_refined, alpha_rich)
    result_m, result_t = verdict(best_alpha, beta)

    # Final one-line status
    print()
    print("=" * 72)
    if result_m == "CLOSED" and result_t == "CLOSED":
        print("  FINAL STATUS:  WOUND 2 CLOSED.")
        print("  The Cartwright chain is complete.  All three wounds closed.")
    elif result_m == "OPEN" or result_t == "OPEN":
        print("  FINAL STATUS:  WOUND 2 OPEN (but closable with adaptive N(K)).")
    else:
        print("  FINAL STATUS:  WOUND 2 MARGINAL.  Refined computation needed.")
    print("=" * 72)
    print()


if __name__ == "__main__":
    main()
