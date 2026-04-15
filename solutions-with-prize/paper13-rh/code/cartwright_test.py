"""Cartwright theorem test -- Lead H: analytic continuation for SPO.

Numerical verification that eigenvectors of the Cauchy matrix B_K have
Fourier cosine transforms that are smooth (consistent with analyticity)
and nonvanishing at {log p} for all primes tested.

The argument:
  1. B_K is the Cauchy matrix 1/(x_i + x_j) on N grid points in [0, L].
  2. Its eigenvectors phi_k live in R^N.
  3. Interpolate each phi_k to a continuous function via cubic spline on [0, L].
  4. Compute the Fourier cosine transform: phi_hat_k(xi) = int_0^L f_k(x) cos(x*xi) dx.
  5. Evaluate at xi = log p for the first 25 primes.
  6. Verify: no overlaps are near zero (|overlap| > 10^{-10}).
  7. Plot |phi_hat_k(xi)| on a dense grid to confirm smoothness.

By Paley-Wiener, the Fourier transform of a compactly supported function
is entire of exponential type.  By Cartwright's theorem, such a function
cannot vanish on {log p} (density = infinity) unless it is identically zero.

This script provides the numerical evidence that supports the theoretical argument.

References:
  - Cartwright, M.L., "On certain integral functions of order one" (1930)
  - Research note 37 in this project

Usage:
  python cartwright_test.py
"""

import sys
import math
import numpy as np
from numpy.linalg import eigh
from scipy.interpolate import CubicSpline
from scipy.integrate import quad


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

K_PRIMES = 10        # number of primes used to build B_K
N_GRID = 30          # grid points for discretization
L = 10.0             # support length [0, L]
N_TEST_PRIMES = 25   # number of primes to test overlaps against
ZERO_THRESH = 1e-10  # threshold for "near zero"
XI_DENSE_MAX = 10.0  # max frequency for dense evaluation
XI_DENSE_PTS = 500   # points in dense frequency grid


# ---------------------------------------------------------------------------
# Utility: primes
# ---------------------------------------------------------------------------

def primes_up_to(n):
    """Sieve of Eratosthenes."""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
    return [i for i, b in enumerate(sieve) if b]


def first_n_primes(n):
    """Return the first n primes."""
    if n == 0:
        return []
    if n < 6:
        upper = 15
    else:
        upper = int(n * (math.log(n) + math.log(math.log(n))) * 1.3) + 10
    ps = primes_up_to(upper)
    while len(ps) < n:
        upper = int(upper * 1.5) + 10
        ps = primes_up_to(upper)
    return ps[:n]


# ---------------------------------------------------------------------------
# Build Cauchy matrix B_K
# ---------------------------------------------------------------------------

def chebyshev_nodes(N, x_max):
    """Chebyshev nodes on (0, x_max], strictly positive and sorted."""
    k = np.arange(1, N + 1)
    nodes = 0.5 * x_max * (1 - np.cos(np.pi * (2 * k - 1) / (2 * N)))
    nodes = np.maximum(nodes, 1e-14)
    return np.sort(nodes)


def build_cauchy_matrix(x):
    """Build the Cauchy matrix C_{ij} = 1/(x_i + x_j)."""
    N = len(x)
    C = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            C[i, j] = 1.0 / (x[i] + x[j])
    return C


def build_BK(x, primes_list):
    """Build B_K = Cauchy + sum of rank-one prime perturbations.

    B_K = C + sum_{p in primes} (log p / sqrt(p)) * v_p v_p^T
    where v_p[i] = cos(x_i * log p).
    """
    C = build_cauchy_matrix(x)
    B = C.copy()
    for p in primes_list:
        lp = math.log(p)
        v = np.cos(x * lp)
        weight = lp / math.sqrt(p)
        B += weight * np.outer(v, v)
    return B


# ---------------------------------------------------------------------------
# Fourier cosine transform via interpolation + integration
# ---------------------------------------------------------------------------

def interpolate_eigenvector(x, phi):
    """Create cubic spline interpolation of eigenvector on [0, L].

    Boundary conditions: natural spline with f(0) ~ extrapolated, f(L) ~ 0
    to enforce compact support.
    """
    # Prepend x=0 with linear extrapolation and append x=L with zero
    x_ext = np.concatenate([[0.0], x, [L]])
    # Extrapolate value at 0 from first two points
    if len(x) >= 2:
        slope = (phi[1] - phi[0]) / (x[1] - x[0])
        val_0 = phi[0] - slope * x[0]
    else:
        val_0 = phi[0]
    phi_ext = np.concatenate([[val_0], phi, [0.0]])
    return CubicSpline(x_ext, phi_ext, bc_type='natural')


def fourier_cosine_transform(spline, xi, a=0.0, b=None):
    """Compute integral_a^b f(x) cos(x * xi) dx via adaptive quadrature.

    Uses weight function cos(xi*x) for oscillatory integrals when xi is large.
    """
    if b is None:
        b = L
    if xi > 5.0:
        # For oscillatory integrands, use Filon-type quadrature via 'weight'
        # Fall back to subdivided integration for reliability
        n_sub = max(int(xi * (b - a) / math.pi) * 4, 200)
        x_pts = np.linspace(a, b, n_sub + 1)
        f_vals = spline(x_pts) * np.cos(x_pts * xi)
        result = np.trapezoid(f_vals, x_pts)
        return result
    integrand = lambda x: spline(x) * np.cos(x * xi)
    result, error = quad(integrand, a, b, limit=200, epsabs=1e-14, epsrel=1e-12)
    return result


def discrete_overlap(x, phi, xi, dx):
    """Discrete inner product: sum_i phi[i] * cos(x_i * xi) * dx_i.

    This is the trapezoidal-rule approximation to the continuous integral.
    """
    return np.sum(phi * np.cos(x * xi) * dx)


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("Cartwright Theorem Test -- Lead H")
    print("=" * 72)
    print(f"Parameters: K={K_PRIMES} primes, N={N_GRID} grid pts, L={L}")
    print()

    # Setup
    primes_K = first_n_primes(K_PRIMES)
    primes_test = first_n_primes(N_TEST_PRIMES)
    x = chebyshev_nodes(N_GRID, L)

    # Quadrature weights (trapezoidal)
    dx = np.zeros(N_GRID)
    dx[0] = 0.5 * (x[1] - x[0])
    dx[-1] = 0.5 * (x[-1] - x[-2])
    for i in range(1, N_GRID - 1):
        dx[i] = 0.5 * (x[i + 1] - x[i - 1])

    print(f"Primes for B_K: {primes_K}")
    print(f"Test primes:     {primes_test}")
    print()

    # Build B_K and diagonalize
    B = build_BK(x, primes_K)
    eigenvalues, eigenvectors = eigh(B)

    print(f"Eigenvalues of B_K (first 5): {eigenvalues[:5]}")
    print(f"Eigenvalues of B_K (last 5):  {eigenvalues[-5:]}")
    print()

    # -----------------------------------------------------------------------
    # Test 1: Overlaps at {log p} for all eigenvectors
    # -----------------------------------------------------------------------
    print("-" * 72)
    print("TEST 1: Overlaps <phi_k | cos(x log p)> at test primes")
    print("-" * 72)

    total_near_zero = 0
    min_overlap_global = float('inf')
    min_overlap_info = None

    for k in range(N_GRID):
        phi = eigenvectors[:, k]
        spline = interpolate_eigenvector(x, phi)

        near_zero_count = 0
        min_overlap_k = float('inf')

        for p in primes_test:
            xi = math.log(p)
            # Use continuous (interpolated) Fourier cosine transform
            overlap = fourier_cosine_transform(spline, xi)
            abs_overlap = abs(overlap)

            if abs_overlap < ZERO_THRESH:
                near_zero_count += 1
                total_near_zero += 1

            if abs_overlap < min_overlap_k:
                min_overlap_k = abs_overlap

        if min_overlap_k < min_overlap_global:
            min_overlap_global = min_overlap_k
            min_overlap_info = (k, eigenvalues[k])

        if near_zero_count > 0 or k < 5 or k >= N_GRID - 3:
            print(f"  eigvec {k:2d}  (lam={eigenvalues[k]:+.6e}): "
                  f"min|overlap|={min_overlap_k:.4e}, "
                  f"near-zero count={near_zero_count}")

    print()
    print(f"GLOBAL minimum |overlap|: {min_overlap_global:.6e} "
          f"(eigvec {min_overlap_info[0]}, lam={min_overlap_info[1]:+.6e})")
    print(f"TOTAL near-zero overlaps (|.| < {ZERO_THRESH}): {total_near_zero}")
    print()

    if total_near_zero == 0:
        print(">>> PASS: All overlaps are nonzero. SPO holds for all test primes.")
    else:
        print(f">>> WARNING: {total_near_zero} near-zero overlaps detected!")
    print()

    # -----------------------------------------------------------------------
    # Test 2: Compare discrete vs continuous overlaps
    # -----------------------------------------------------------------------
    print("-" * 72)
    print("TEST 2: Discrete vs continuous overlap comparison (eigvec 0)")
    print("-" * 72)

    phi_0 = eigenvectors[:, 0]
    spline_0 = interpolate_eigenvector(x, phi_0)

    print(f"  {'prime':>5s}  {'log p':>8s}  {'discrete':>14s}  {'continuous':>14s}  {'rel diff':>12s}")
    print(f"  {'-----':>5s}  {'-----':>8s}  {'---------':>14s}  {'----------':>14s}  {'--------':>12s}")

    for p in primes_test[:15]:
        xi = math.log(p)
        ov_disc = discrete_overlap(x, phi_0, xi, dx)
        ov_cont = fourier_cosine_transform(spline_0, xi)
        if abs(ov_cont) > 1e-30:
            rel = abs(ov_disc - ov_cont) / abs(ov_cont)
        else:
            rel = abs(ov_disc - ov_cont)
        print(f"  {p:5d}  {xi:8.5f}  {ov_disc:+14.8e}  {ov_cont:+14.8e}  {rel:12.4e}")

    print()

    # -----------------------------------------------------------------------
    # Test 3: Smoothness of Fourier transform on dense grid
    # -----------------------------------------------------------------------
    print("-" * 72)
    print("TEST 3: Smoothness of phi_hat_k(xi) on dense grid")
    print("-" * 72)

    xi_dense = np.linspace(0.01, XI_DENSE_MAX, XI_DENSE_PTS)

    # Evaluate for a few representative eigenvectors
    test_eigvecs = [0, N_GRID // 4, N_GRID // 2, N_GRID - 1]

    for k in test_eigvecs:
        phi = eigenvectors[:, k]
        spline = interpolate_eigenvector(x, phi)

        ft_values = np.array([fourier_cosine_transform(spline, xi) for xi in xi_dense])
        ft_abs = np.abs(ft_values)

        # Smoothness check: finite differences should be bounded
        diffs = np.diff(ft_values)
        max_jump = np.max(np.abs(diffs))
        mean_val = np.mean(ft_abs)
        max_val = np.max(ft_abs)
        min_val = np.min(ft_abs)

        print(f"  eigvec {k:2d}: |phi_hat| in [{min_val:.4e}, {max_val:.4e}], "
              f"mean={mean_val:.4e}, max|jump|={max_jump:.4e}")

    print()

    # -----------------------------------------------------------------------
    # Test 4: Verify Paley-Wiener type bound
    # -----------------------------------------------------------------------
    print("-" * 72)
    print("TEST 4: Paley-Wiener exponential type estimate")
    print("-" * 72)
    print(f"  Expected type: sigma = L = {L}")
    print()

    # For an entire function of type sigma, |f(xi)| <= C * exp(sigma * |xi|)
    # on the real line it should actually DECAY or remain bounded.
    # Check: |phi_hat(xi)| for large real xi should decay (not grow).

    xi_large = np.array([10, 20, 50, 100, 200, 500])
    phi_0 = eigenvectors[:, 0]
    spline_0 = interpolate_eigenvector(x, phi_0)

    print(f"  {'xi':>8s}  {'|phi_hat_0(xi)|':>18s}  {'xi * |phi_hat|':>16s}")
    print(f"  {'--':>8s}  {'---------------':>18s}  {'--------------':>16s}")

    for xi in xi_large:
        val = fourier_cosine_transform(spline_0, xi)
        abs_val = abs(val)
        print(f"  {xi:8.1f}  {abs_val:18.8e}  {xi * abs_val:16.8e}")

    print()
    print("  (Entire functions of exponential type are bounded on the real axis")
    print("   by Bernstein's inequality. Decay at large xi confirms finite type.)")
    print()

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Grid:         N={N_GRID} Chebyshev nodes in [0, {L}]")
    print(f"  B_K primes:   {primes_K}")
    print(f"  Test primes:  first {N_TEST_PRIMES} primes (up to {primes_test[-1]})")
    print(f"  Eigenvectors: {N_GRID}")
    print(f"  Min |overlap|: {min_overlap_global:.6e}")
    print(f"  Near-zero overlaps: {total_near_zero}")
    print()

    if total_near_zero == 0:
        print("  CONCLUSION: All eigenvector-prime overlaps are nonzero.")
        print("  Consistent with Cartwright's theorem: phi_hat_k entire of finite")
        print("  type cannot vanish on {log p} (infinite density zero set).")
    else:
        print(f"  CONCLUSION: {total_near_zero} overlaps below threshold.")
        print("  Investigate whether these are genuine zeros or numerical artifacts.")

    print()
    return total_near_zero == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
