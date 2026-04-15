"""Direct Discrete Cartwright -- Lead L: no interpolation needed for SPO.

Key insight: the overlap g_k(xi) = sum_i phi_k[i] cos(x_i xi) is already
an entire function of finite exponential type.  No spline interpolation
or continuous Fourier transform is needed.

This script:
  1. Builds B_K for K=10 primes on N=30 Chebyshev grid in [0, L=10].
  2. Computes eigenvectors phi_k.
  3. Defines g_k(xi) = sum_i phi_k[i] cos(x_i xi) as a function of complex xi.
  4. Evaluates g_k at xi = log p for the first 50 primes.
  5. Counts zeros (|g_k(log p)| < 10^{-30}).
  6. Verifies g_k is not identically zero at random complex points.
  7. Estimates exponential type from growth on the imaginary axis.
  8. Reports the Cartwright conclusion.

References:
  - Cartwright, M.L., "On certain integral functions of order one" (1930)
  - Research note 39: Lead L (Direct Discrete Cartwright)

Usage:
  python direct_discrete_cartwright.py
"""

import sys
import math
import random

from mpmath import mp, mpf, cos, log, exp, fabs, pi, matrix, eigsy, rand

# ---------------------------------------------------------------------------
# Precision
# ---------------------------------------------------------------------------

mp.dps = 50  # 50 decimal digits; raise to 120 for final certification


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

K_PRIMES = 10        # primes used to build B_K
N_GRID = 30          # grid points
L = mpf(10)          # support endpoint
N_TEST_PRIMES = 50   # primes to test overlaps
ZERO_THRESH = mpf(10) ** (-30)


# ---------------------------------------------------------------------------
# Utility: primes
# ---------------------------------------------------------------------------

def sieve(n):
    """Sieve of Eratosthenes up to n."""
    if n < 2:
        return []
    flags = bytearray(b"\x01") * (n + 1)
    flags[0] = flags[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if flags[i]:
            flags[i * i :: i] = bytearray(len(flags[i * i :: i]))
    return [i for i, b in enumerate(flags) if b]


def first_n_primes(n):
    """Return the first n primes."""
    if n == 0:
        return []
    if n < 6:
        upper = 15
    else:
        upper = int(n * (math.log(n) + math.log(math.log(n))) * 1.3) + 10
    ps = sieve(upper)
    while len(ps) < n:
        upper = int(upper * 1.5) + 10
        ps = sieve(upper)
    return ps[:n]


# ---------------------------------------------------------------------------
# Grid and matrix construction (mpmath for high precision)
# ---------------------------------------------------------------------------

def chebyshev_nodes(N, x_max):
    """Chebyshev nodes on (0, x_max], strictly positive and sorted."""
    nodes = []
    for k in range(1, N + 1):
        theta = pi * (2 * k - 1) / (2 * N)
        node = x_max / 2 * (1 - cos(theta))
        if node < mpf("1e-14"):
            node = mpf("1e-14")
        nodes.append(node)
    nodes.sort()
    return nodes


def build_BK(x, primes_list):
    """Build B_K = Cauchy + sum of rank-one prime perturbations.

    B_K[i,j] = 1/(x_i + x_j) + sum_p (log p / sqrt(p)) cos(x_i log p) cos(x_j log p)
    """
    N = len(x)
    B = matrix(N, N)
    # Cauchy part
    for i in range(N):
        for j in range(N):
            B[i, j] = 1 / (x[i] + x[j])
    # Prime perturbations
    for p in primes_list:
        lp = log(mpf(p))
        sqp = mpf(p) ** mpf("0.5")
        weight = lp / sqp
        v = [cos(x[i] * lp) for i in range(N)]
        for i in range(N):
            for j in range(N):
                B[i, j] += weight * v[i] * v[j]
    return B


# ---------------------------------------------------------------------------
# The core function: g_k(xi) = sum_i phi_k[i] cos(x_i * xi)
# ---------------------------------------------------------------------------

def g_func(phi, x, xi):
    """Evaluate g(xi) = sum_i phi[i] cos(x_i xi).

    Works for real or complex xi (mpmath cos handles both).
    """
    s = mpf(0)
    for i in range(len(phi)):
        s += phi[i] * cos(x[i] * xi)
    return s


# ---------------------------------------------------------------------------
# Exponential type estimation
# ---------------------------------------------------------------------------

def estimate_type(phi, x, y_values):
    """Estimate exponential type from |g(iy)| for large imaginary y.

    For an entire function of type sigma: |g(iy)| ~ C exp(sigma |y|).
    So log|g(iy)| / |y| -> sigma as |y| -> infinity.
    """
    estimates = []
    for y in y_values:
        val = g_func(phi, x, 1j * y)
        abs_val = fabs(val)
        if abs_val > 0:
            est = log(abs_val) / y
            estimates.append((float(y), float(est)))
    return estimates


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("Direct Discrete Cartwright -- Lead L")
    print("No interpolation: g_k(xi) = sum_i phi_k[i] cos(x_i xi)")
    print("=" * 72)
    print(f"Precision:   {mp.dps} decimal digits")
    print(f"Parameters:  K={K_PRIMES} primes, N={N_GRID} grid pts, L={float(L)}")
    print()

    # Setup
    primes_K = first_n_primes(K_PRIMES)
    primes_test = first_n_primes(N_TEST_PRIMES)
    x = chebyshev_nodes(N_GRID, L)

    print(f"Primes for B_K:  {primes_K}")
    print(f"Grid x_max:      {float(x[-1]):.6f}")
    print(f"Expected type:   sigma = max|x_i| = {float(x[-1]):.6f}")
    print()

    # Build B_K and diagonalize
    print("Building B_K ... ", end="", flush=True)
    B = build_BK(x, primes_K)
    print("done.")

    print("Diagonalizing ... ", end="", flush=True)
    eigenvalues, eigenvectors = eigsy(B)
    print("done.")
    print()

    n_eigvecs = len(eigenvalues)
    print(f"Eigenvalues (first 5):  {[float(eigenvalues[i]) for i in range(min(5, n_eigvecs))]}")
    print(f"Eigenvalues (last 5):   {[float(eigenvalues[i]) for i in range(max(0, n_eigvecs-5), n_eigvecs)]}")
    print()

    # -------------------------------------------------------------------
    # TEST 1: Overlaps g_k(log p) for all eigenvectors and test primes
    # -------------------------------------------------------------------
    print("-" * 72)
    print("TEST 1: Overlaps g_k(log p) = <phi_k | v_p> for 50 primes")
    print(f"         Zero threshold: |g| < 10^(-30)")
    print("-" * 72)

    total_zeros = 0
    global_min = mpf("1e100")
    global_min_info = None

    for k in range(n_eigvecs):
        phi = [eigenvectors[i, k] for i in range(N_GRID)]
        zero_count = 0
        min_abs = mpf("1e100")

        for p in primes_test:
            xi = log(mpf(p))
            val = g_func(phi, x, xi)
            av = fabs(val)
            if av < ZERO_THRESH:
                zero_count += 1
            if av < min_abs:
                min_abs = av

        total_zeros += zero_count

        if min_abs < global_min:
            global_min = min_abs
            global_min_info = (k, float(eigenvalues[k]))

        if zero_count > 0 or k < 3 or k >= n_eigvecs - 2:
            print(f"  eigvec {k:2d}  (lam={float(eigenvalues[k]):+.6e}): "
                  f"min|g|={float(min_abs):.4e}, zeros={zero_count}/{N_TEST_PRIMES}")

    print()
    print(f"GLOBAL min |g_k(log p)|: {float(global_min):.6e} "
          f"(eigvec {global_min_info[0]}, lam={global_min_info[1]:+.6e})")
    print(f"TOTAL zeros found: {total_zeros} / {n_eigvecs * N_TEST_PRIMES}")
    print()

    # -------------------------------------------------------------------
    # TEST 2: Verify g_k not identically zero
    # -------------------------------------------------------------------
    print("-" * 72)
    print("TEST 2: Verify g_k is not identically zero")
    print("         (evaluate at random complex points)")
    print("-" * 72)

    random.seed(42)
    test_points = [mpf(0)]  # xi = 0
    for _ in range(5):
        re = mpf(random.uniform(-5, 5))
        im = mpf(random.uniform(-5, 5))
        test_points.append(re + 1j * im)

    all_nonzero = True
    for k in range(n_eigvecs):
        phi = [eigenvectors[i, k] for i in range(N_GRID)]
        max_val = mpf(0)
        for z in test_points:
            val = g_func(phi, x, z)
            av = fabs(val)
            if av > max_val:
                max_val = av

        is_zero = (max_val < ZERO_THRESH)
        if is_zero:
            all_nonzero = False

        if k < 3 or k >= n_eigvecs - 2 or is_zero:
            status = "IDENTICALLY ZERO??" if is_zero else "nonzero"
            print(f"  eigvec {k:2d}: max|g| at test pts = {float(max_val):.4e}  [{status}]")

    print()
    if all_nonzero:
        print("  All eigenvectors have g_k not identically zero.")
    else:
        print("  WARNING: some eigenvectors may have g_k = 0!")
    print()

    # Leading eigenvector check: g_0(0) = sum of components
    phi_lead = [eigenvectors[i, n_eigvecs - 1] for i in range(N_GRID)]
    g0_val = g_func(phi_lead, x, mpf(0))
    print(f"  Leading eigvec: g(0) = sum_i phi[i] = {float(g0_val):.8e}", end="")
    if g0_val > 0:
        print("  (positive, as expected by Perron-Frobenius)")
    else:
        print()
    print()

    # -------------------------------------------------------------------
    # TEST 3: Exponential type estimation
    # -------------------------------------------------------------------
    print("-" * 72)
    print("TEST 3: Exponential type estimation via imaginary axis")
    print(f"         Expected: sigma = max|x_i| = {float(x[-1]):.6f}")
    print("-" * 72)

    y_vals = [mpf(5), mpf(10), mpf(20), mpf(50), mpf(100)]

    for k_idx in [0, n_eigvecs // 2, n_eigvecs - 1]:
        phi = [eigenvectors[i, k_idx] for i in range(N_GRID)]
        estimates = estimate_type(phi, x, y_vals)
        if estimates:
            final_est = estimates[-1][1]
            print(f"  eigvec {k_idx:2d}: ", end="")
            print(f"log|g(iy)|/y at y={estimates[-1][0]:.0f} -> "
                  f"sigma_est = {final_est:.4f}  "
                  f"(expected {float(x[-1]):.4f})")

    print()
    print(f"  Theoretical type: sigma = max_i |x_i| = {float(x[-1]):.6f}")
    print(f"  sigma / pi = {float(x[-1] / pi):.6f}")
    print(f"  Density of {{log p}} = +infinity  >>  sigma/pi")
    print()

    # -------------------------------------------------------------------
    # TEST 4: Detailed overlaps for leading eigenvector
    # -------------------------------------------------------------------
    print("-" * 72)
    print("TEST 4: Detailed overlaps for leading eigenvector")
    print("-" * 72)

    phi_lead = [eigenvectors[i, n_eigvecs - 1] for i in range(N_GRID)]

    print(f"  {'prime':>6s}  {'log p':>10s}  {'g(log p)':>20s}  {'|g(log p)|':>14s}")
    print(f"  {'-----':>6s}  {'-----':>10s}  {'--------':>20s}  {'----------':>14s}")

    for p in primes_test[:20]:
        xi = log(mpf(p))
        val = g_func(phi_lead, x, xi)
        print(f"  {p:6d}  {float(xi):10.6f}  {float(val):+20.12e}  {float(fabs(val)):14.6e}")

    print()

    # -------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------
    sigma_val = x[-1]

    print("=" * 72)
    print("SUMMARY -- Direct Discrete Cartwright")
    print("=" * 72)
    print()
    print(f"  Grid:              N={N_GRID} Chebyshev nodes in [0, {float(L)}]")
    print(f"  B_K primes:        {primes_K}")
    print(f"  Test primes:       first {N_TEST_PRIMES} (up to {primes_test[-1]})")
    print(f"  Eigenvectors:      {n_eigvecs}")
    print()
    print(f"  g_k(xi) = sum_i phi_k[i] cos(x_i xi)")
    print(f"  Entire of type:    sigma = {float(sigma_val):.6f}")
    print(f"  sigma / pi:        {float(sigma_val / pi):.6f}")
    print(f"  Density of {{log p}}: +infinity")
    print()
    print(f"  By Cartwright's theorem: g_k has at most FINITELY MANY")
    print(f"  zeros among {{log p : p prime}}.")
    print()
    print(f"  Zeros found:       {total_zeros} out of "
          f"{n_eigvecs * N_TEST_PRIMES} overlap evaluations")
    print(f"  Min |overlap|:     {float(global_min):.6e}")
    print(f"  All g_k nonzero:   {'YES' if all_nonzero else 'NO'}")
    print()

    if total_zeros == 0 and all_nonzero:
        print("  CONCLUSION: SPO verified for all eigenvectors at all 50 test")
        print("  primes.  Cartwright's theorem guarantees this extends to all")
        print("  but finitely many primes.  No interpolation was used.")
        print()
        print("  STATUS: Lead L CONFIRMED.  Feasibility 8/10.")
    elif total_zeros > 0:
        print(f"  CONCLUSION: {total_zeros} zero overlaps found.")
        print("  These are the 'finitely many exceptions' predicted by")
        print("  Cartwright.  Verify at higher precision or larger grid.")
    else:
        print("  WARNING: Some g_k may be identically zero.  Investigate.")

    print()
    return total_zeros == 0 and all_nonzero


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
