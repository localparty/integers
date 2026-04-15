"""Slepian Convergence Test -- Gap B numerical investigation.

Estimates the operator-norm convergence rate of QW_lambda^{N,+} toward the
prolate spheroidal wave operator PW, and determines whether the Slepian
spectral gap can be reached at finite prime count.

Strategy:
  1. Build the prolate wave operator PW on a discrete grid (sinc kernel).
  2. Compute its two smallest eigenvalues and the gap delta = mu_2 - mu_1.
  3. For varying numbers of primes N_p, build a simplified QW^{N_p} matrix
     using the Weil explicit formula with N_p Euler factors.
  4. Compute ||QW^{N_p} - PW||_op (max singular value of the difference).
  5. Report convergence table and whether simplicity transfers.

Uses mpmath for 50-digit precision.  Matrices are discretized on a grid of
~60 points.  The PW and QW operators are compared in a NORMALIZED form
(divided by their respective Frobenius norms) to handle the scale mismatch
between Weil eigenvalues (~e^{-c*lambda^2}) and prolate eigenvalues (~O(1)).

References:
  - Slepian & Pollak, Bell Syst. Tech. J. 40 (1961)
  - Connes-Consani-Marcolli, arXiv:2511.22755 (CCM)
  - Research notes 25, 29, 31 in this project

Usage:
  python slepian_convergence_test.py
"""

import sys
import time
import mpmath as mp

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DPS = 50                      # decimal digits of precision
GRID_SIZE = 60                # discretization points for PW / QW comparison
LAMBDA = mp.sqrt(13)          # CCM's primary test case: lambda = sqrt(13)
PRIME_COUNTS = [1, 2, 3, 4, 5, 6, 8, 10, 15, 20]  # number of primes to include

mp.mp.dps = DPS


# ---------------------------------------------------------------------------
# Utility: primes and prime powers
# ---------------------------------------------------------------------------

def primes_up_to(bound):
    """Sieve of Eratosthenes returning primes up to bound (inclusive)."""
    n = int(bound)
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def first_n_primes(n):
    """Return the first n primes."""
    if n <= 0:
        return []
    # Generous upper bound via prime number theorem
    import math
    if n < 6:
        bound = 15
    else:
        bound = int(n * (math.log(n) + math.log(math.log(n))) * 1.3) + 20
    ps = primes_up_to(bound)
    while len(ps) < n:
        bound *= 2
        ps = primes_up_to(bound)
    return ps[:n]


def von_mangoldt_terms_up_to(K_max):
    """Return list of (k, log_p, p) for all prime powers k = p^j <= K_max."""
    out = []
    for p in primes_up_to(int(K_max)):
        pk = p
        while pk <= K_max:
            out.append((pk, mp.log(p), p))
            pk *= p
    out.sort(key=lambda t: t[0])
    return out


# ---------------------------------------------------------------------------
# Prolate spheroidal wave operator (sinc kernel)
# ---------------------------------------------------------------------------

def build_prolate_matrix(grid_size, bandwidth):
    """Build the prolate wave operator on a grid in [-1, 1].

    PW_{ij} = sin(c * (x_i - x_j)) / (pi * (x_i - x_j))

    where c = bandwidth.  On the diagonal, PW_{ii} = c / pi.

    This is the kernel of the time-frequency concentration operator
    B_{T,Omega} = P_T P_Omega P_T restricted to [-1,1] with
    bandwidth c = pi * T * Omega.

    Returns the matrix and the grid points.
    """
    n = grid_size
    # Equally spaced grid on [-1, 1]
    xs = [mp.mpf(-1) + 2 * mp.mpf(i) / (n - 1) for i in range(n)]
    dx = mp.mpf(2) / (n - 1)  # grid spacing (for quadrature weight)

    c = bandwidth
    M = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i, j] = c / mp.pi * dx
            else:
                diff = xs[i] - xs[j]
                M[i, j] = mp.sin(c * diff) / (mp.pi * diff) * dx
    return M, xs


def symmetrize_matrix(M):
    """Force exact symmetry on an mpmath matrix."""
    n = M.rows
    for i in range(n):
        for j in range(i + 1, n):
            avg = (M[i, j] + M[j, i]) / 2
            M[i, j] = avg
            M[j, i] = avg
    return M


# ---------------------------------------------------------------------------
# Weil explicit formula quadratic form (simplified, on the same grid)
# ---------------------------------------------------------------------------

def build_weil_archimedean(grid_size, L):
    """Build the archimedean part of the Weil quadratic form on a grid.

    This approximates the W_{0,2} - W_R contribution using the digamma-
    based kernel.  On a grid x_0, ..., x_{n-1} in [-1, 1], the kernel is:

        K_arch(x, y) = Re[ psi(1/2 + i*c*(x-y)/(2*pi)) ] / (2*pi)
                      + log(2*pi) / (2*pi)

    where c = L (the log-parameter) and psi is the digamma function.
    This is the standard archimedean test-function kernel from the
    explicit formula.

    For simplicity, we use the SINC approximation to the archimedean kernel,
    which is the leading term as L -> infinity.  This makes the archimedean
    part essentially equal to the prolate kernel, with corrections of
    order O(1/L^2).
    """
    n = grid_size
    xs = [mp.mpf(-1) + 2 * mp.mpf(i) / (n - 1) for i in range(n)]
    dx = mp.mpf(2) / (n - 1)

    # The archimedean kernel in the explicit formula involves the digamma
    # function.  Its Fourier transform is the indicator function of [-L/2, L/2],
    # which gives a sinc kernel with bandwidth c = L/2.
    # We use the full digamma form for better accuracy.
    c = L / 2
    M = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                # Diagonal: psi(1/2) + euler + log(4*pi) terms
                # Approximation: c / pi (matching the prolate diagonal)
                M[i, j] = c / mp.pi * dx
            else:
                diff = xs[i] - xs[j]
                # Full digamma kernel:
                # Re[psi(1/2 + i*c*diff/pi)] gives the archimedean contribution.
                # Leading term is sin(c*diff)/(pi*diff) (the sinc kernel).
                # We include the digamma correction for finite L.
                z = mp.mpf('0.5') + 1j * c * diff / mp.pi
                digamma_val = mp.digamma(z)
                # The kernel is (1/(2*pi)) * Re[psi(1/2 + i*u) + psi(1/2 - i*u)]
                # = (1/pi) * Re[psi(1/2 + i*u)]
                # where u = c*diff/pi.
                kernel_val = mp.re(digamma_val) / mp.pi
                # Add the log(2*pi) offset and normalize
                M[i, j] = (kernel_val + mp.log(2 * mp.pi) / mp.pi) * dx
    return M, xs


def build_weil_prime_contribution(grid_size, xs, L, n_primes):
    """Build the prime-sum contribution to the Weil quadratic form.

    For each prime p, the contribution to the kernel is:

        W_p(x, y) = (log p / sqrt(p)) * cos(log(p) * c * (x + y) / pi)

    where the cos term arises from the Euler factor in the explicit formula:
        sum over p of (log p / p^{1/2+it}) evaluated at t-values
        corresponding to grid points.

    This is a simplified model.  The exact CCM entries involve the
    q(U_n, U_m)(log k) kernel (eqs 2.9-2.10), which we approximate by
    a rank-1 cosine contribution per prime.

    For the EVEN sector, we use the symmetrized form:
        W_p^+(x, y) = (log p / sqrt(p)) * cos(log(p) * c * x / pi)
                                         * cos(log(p) * c * y / pi)

    This captures the essential structure: each prime contributes a
    separable (rank-1) perturbation.
    """
    n = grid_size
    dx = mp.mpf(2) / (n - 1)
    c = L / 2
    primes = first_n_primes(n_primes)

    M = mp.matrix(n)
    for p in primes:
        logp = mp.log(p)
        coeff = logp / mp.sqrt(mp.mpf(p))
        # Also include prime powers p^2, p^3, ... up to a reasonable bound
        pk = p
        while pk <= 10000:
            if pk > p:
                # For prime power p^k, Lambda(p^k) = log(p), divisor = p^{k/2}
                coeff_pk = logp / mp.sqrt(mp.mpf(pk))
            else:
                coeff_pk = coeff

            # Compute the rank-1 outer product contribution
            freq = mp.log(pk) * c / mp.pi
            cos_vec = [mp.cos(freq * xs[i]) for i in range(n)]
            for i in range(n):
                for j in range(n):
                    M[i, j] += coeff_pk * cos_vec[i] * cos_vec[j] * dx * dx
            pk *= p

    return M


def build_weil_matrix(grid_size, L, n_primes):
    """Build the full Weil quadratic form: archimedean - prime sum.

    Returns (QW_matrix, PW_matrix, xs) where PW_matrix is the archimedean
    part alone (which approximates the prolate operator).
    """
    M_arch, xs = build_weil_archimedean(grid_size, L)
    M_prime = build_weil_prime_contribution(grid_size, xs, L, n_primes)

    # QW = archimedean - prime sum (following CCM sign convention: QW = W02 - WR - Wp)
    # The archimedean part M_arch plays the role of W02 - WR.
    # The prime part M_prime plays the role of Wp.
    QW = mp.matrix(grid_size)
    for i in range(grid_size):
        for j in range(grid_size):
            QW[i, j] = M_arch[i, j] - M_prime[i, j]

    return symmetrize_matrix(QW), symmetrize_matrix(M_arch), xs


# ---------------------------------------------------------------------------
# Eigenvalue computation
# ---------------------------------------------------------------------------

def sorted_eigenvalues(M):
    """Compute eigenvalues of a real symmetric mpmath matrix, sorted ascending."""
    E, _ = mp.eigsy(M)
    return sorted(E, key=lambda x: float(x))


def operator_norm_of_difference(A, B):
    """Compute ||A - B||_op = max singular value of (A - B).

    For a symmetric matrix, this is max |eigenvalue of A - B|.
    """
    n = A.rows
    D = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            D[i, j] = A[i, j] - B[i, j]
    D = symmetrize_matrix(D)
    eigs = sorted_eigenvalues(D)
    return max(abs(eigs[0]), abs(eigs[-1]))


def frobenius_norm(M):
    """Compute the Frobenius norm of an mpmath matrix."""
    n = M.rows
    s = mp.mpf(0)
    for i in range(n):
        for j in range(n):
            s += M[i, j]**2
    return mp.sqrt(s)


# ---------------------------------------------------------------------------
# Normalized comparison (to handle scale mismatch)
# ---------------------------------------------------------------------------

def normalize_by_trace(M):
    """Return M / trace(M) (when trace > 0) for scale-invariant comparison."""
    n = M.rows
    tr = sum(M[i, i] for i in range(n))
    if abs(tr) < mp.mpf('1e-40'):
        return M, mp.mpf(1)
    Mn = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            Mn[i, j] = M[i, j] / tr
    return Mn, tr


# ---------------------------------------------------------------------------
# Main computation
# ---------------------------------------------------------------------------

def main():
    mp.mp.dps = DPS
    t_start = time.time()

    L = 2 * mp.log(LAMBDA)
    c_bandwidth = L / 2  # bandwidth parameter for the prolate kernel

    print("=" * 78)
    print("SLEPIAN CONVERGENCE TEST -- Gap B Investigation")
    print("=" * 78)
    print(f"  lambda      = {mp.nstr(LAMBDA, 10)}")
    print(f"  L = 2 log l = {mp.nstr(L, 10)}")
    print(f"  bandwidth c = {mp.nstr(c_bandwidth, 10)}")
    print(f"  grid size   = {GRID_SIZE}")
    print(f"  precision   = {DPS} digits")
    print()

    # ------------------------------------------------------------------
    # STEP 1: Build the prolate operator PW on the grid.
    # ------------------------------------------------------------------
    print("--- Step 1: Prolate operator PW ---")
    t0 = time.time()
    PW, xs = build_prolate_matrix(GRID_SIZE, c_bandwidth)
    PW = symmetrize_matrix(PW)
    print(f"  Built {GRID_SIZE}x{GRID_SIZE} prolate matrix [{time.time()-t0:.1f}s]")

    # ------------------------------------------------------------------
    # STEP 2: Eigenvalues of PW and the spectral gap.
    # ------------------------------------------------------------------
    print("\n--- Step 2: Prolate eigenvalues and gap ---")
    t0 = time.time()
    pw_eigs = sorted_eigenvalues(PW)
    print(f"  Diagonalized PW [{time.time()-t0:.1f}s]")

    # Report the smallest few eigenvalues
    print(f"\n  Smallest eigenvalues of PW:")
    n_show = min(8, len(pw_eigs))
    for k in range(n_show):
        print(f"    mu_{k}(PW) = {mp.nstr(pw_eigs[k], 15)}")

    # Find the two smallest POSITIVE eigenvalues (prolate eigenvalues are in (0,1))
    pos_eigs = [e for e in pw_eigs if e > mp.mpf('1e-40')]
    if len(pos_eigs) >= 2:
        mu1_pw = pos_eigs[0]
        mu2_pw = pos_eigs[1]
        gap_pw = mu2_pw - mu1_pw
        half_gap = gap_pw / 2
    else:
        # Fallback: use the two smallest eigenvalues regardless of sign
        mu1_pw = pw_eigs[0]
        mu2_pw = pw_eigs[1]
        gap_pw = mu2_pw - mu1_pw
        half_gap = gap_pw / 2

    print(f"\n  mu_1(PW) = {mp.nstr(mu1_pw, 20)}")
    print(f"  mu_2(PW) = {mp.nstr(mu2_pw, 20)}")
    print(f"  gap(PW)  = mu_2 - mu_1 = {mp.nstr(gap_pw, 15)}")
    print(f"  gap/2    = {mp.nstr(half_gap, 15)}")

    # Also compute eigenvalue RATIOS (scale-invariant)
    if abs(mu1_pw) > mp.mpf('1e-40'):
        ratio_pw = mu2_pw / mu1_pw
        print(f"  mu_2/mu_1 ratio = {mp.nstr(ratio_pw, 15)}")

    # ------------------------------------------------------------------
    # STEP 3: Build QW with varying numbers of primes.
    # ------------------------------------------------------------------
    print("\n--- Step 3: QW with varying prime counts ---")

    # Build archimedean part once (shared across all prime counts)
    t0 = time.time()
    M_arch, xs_arch = build_weil_archimedean(GRID_SIZE, L)
    M_arch = symmetrize_matrix(M_arch)
    print(f"  Built archimedean matrix [{time.time()-t0:.1f}s]")

    # Archimedean eigenvalues (this IS the "PW" in our discretization)
    arch_eigs = sorted_eigenvalues(M_arch)
    print(f"\n  Archimedean (PW-like) smallest eigenvalues:")
    for k in range(min(6, len(arch_eigs))):
        print(f"    mu_{k}(arch) = {mp.nstr(arch_eigs[k], 15)}")

    results = []

    for n_p in PRIME_COUNTS:
        primes = first_n_primes(n_p)
        if not primes:
            continue
        P_N = primes[-1]

        print(f"\n  --- N_primes = {n_p}, P_N = {P_N} ---")
        t0 = time.time()

        # Build prime contribution
        M_prime = build_weil_prime_contribution(GRID_SIZE, xs_arch, L, n_p)

        # QW = archimedean - primes
        QW = mp.matrix(GRID_SIZE)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                QW[i, j] = M_arch[i, j] - M_prime[i, j]
        QW = symmetrize_matrix(QW)

        # Eigenvalues of QW
        qw_eigs = sorted_eigenvalues(QW)
        mu1_qw = qw_eigs[0]
        mu2_qw = qw_eigs[1] if len(qw_eigs) > 1 else mp.mpf(0)
        gap_qw = mu2_qw - mu1_qw

        # Operator norm of difference: ||QW - PW||_op
        # (where PW = M_arch, the archimedean-only operator)
        diff_norm = operator_norm_of_difference(QW, M_arch)

        # Also: norm of the prime contribution alone
        prime_norm = frobenius_norm(M_prime)

        # Normalized comparison: normalize both by their Frobenius norms
        fn_qw = frobenius_norm(QW)
        fn_arch = frobenius_norm(M_arch)
        if fn_qw > mp.mpf('1e-40') and fn_arch > mp.mpf('1e-40'):
            QW_n = mp.matrix(GRID_SIZE)
            ARCH_n = mp.matrix(GRID_SIZE)
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    QW_n[i, j] = QW[i, j] / fn_qw
                    ARCH_n[i, j] = M_arch[i, j] / fn_arch
            norm_diff = operator_norm_of_difference(QW_n, ARCH_n)
        else:
            norm_diff = mp.mpf(0)

        # Eigenvalue ratio comparison
        if abs(mu1_qw) > mp.mpf('1e-40') and len(qw_eigs) > 1:
            ratio_qw = mu2_qw / mu1_qw
        else:
            ratio_qw = mp.inf

        bound_holds = (diff_norm < half_gap) if half_gap > 0 else False

        t_elapsed = time.time() - t0

        results.append({
            'n_primes': n_p,
            'P_N': P_N,
            'mu1_qw': mu1_qw,
            'mu2_qw': mu2_qw,
            'gap_qw': gap_qw,
            'diff_norm': diff_norm,
            'norm_diff': norm_diff,
            'prime_norm': prime_norm,
            'ratio_qw': ratio_qw,
            'bound_holds': bound_holds,
            'time': t_elapsed,
        })

        print(f"    mu_1(QW)      = {mp.nstr(mu1_qw, 12)}")
        print(f"    mu_2(QW)      = {mp.nstr(mu2_qw, 12)}")
        print(f"    gap(QW)       = {mp.nstr(gap_qw, 8)}")
        print(f"    ||QW-PW||_op  = {mp.nstr(diff_norm, 8)}")
        print(f"    ||W_prime||_F = {mp.nstr(prime_norm, 8)}")
        print(f"    norm'd diff   = {mp.nstr(norm_diff, 8)}")
        print(f"    mu2/mu1 (QW)  = {mp.nstr(ratio_qw, 10)}")
        print(f"    [{t_elapsed:.1f}s]")

    # ------------------------------------------------------------------
    # STEP 4: Summary table.
    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("CONVERGENCE TABLE")
    print("=" * 78)
    print(f"  gap(PW)/2 = {mp.nstr(half_gap, 10)}")
    print(f"  mu2/mu1 (PW) = {mp.nstr(ratio_pw, 10) if abs(mu1_pw) > mp.mpf('1e-40') else 'N/A'}")
    print()

    hdr = f"{'N_p':>4}  {'P_N':>5}  {'||QW-PW||_op':>16}  {'gap(PW)/2':>14}  {'||diff||<gap/2':>14}  {'||W_p||_F':>12}  {'mu2/mu1(QW)':>14}  {'norm_diff':>12}"
    print(hdr)
    print("-" * len(hdr))

    for r in results:
        flag = "YES" if r['bound_holds'] else "no"
        print(f"{r['n_primes']:4d}  {r['P_N']:5d}  {mp.nstr(r['diff_norm'], 10):>16s}"
              f"  {mp.nstr(half_gap, 8):>14s}  {flag:>14s}"
              f"  {mp.nstr(r['prime_norm'], 6):>12s}"
              f"  {mp.nstr(r['ratio_qw'], 8):>14s}"
              f"  {mp.nstr(r['norm_diff'], 6):>12s}")

    # ------------------------------------------------------------------
    # STEP 5: Convergence rate analysis.
    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("CONVERGENCE RATE ANALYSIS")
    print("=" * 78)

    # Analyze the normalized difference as a function of P_N
    if len(results) >= 3:
        print("\n  Normalized ||QW - PW|| vs P_N (largest prime):")
        print(f"  {'P_N':>5}  {'norm_diff':>15}  {'log10(norm_diff)':>18}  {'ratio to prev':>14}")
        prev_nd = None
        for r in results:
            nd = r['norm_diff']
            log_nd = float(mp.log10(nd)) if nd > 0 else float('-inf')
            if prev_nd is not None and prev_nd > 0 and nd > 0:
                ratio = float(nd / prev_nd)
                print(f"  {r['P_N']:5d}  {mp.nstr(nd, 8):>15s}  {log_nd:18.4f}  {ratio:14.6f}")
            else:
                print(f"  {r['P_N']:5d}  {mp.nstr(nd, 8):>15s}  {log_nd:18.4f}  {'---':>14s}")
            prev_nd = nd

    # Check for eigenvalue ratio convergence
    print(f"\n  Eigenvalue ratio mu_2/mu_1 convergence:")
    print(f"  {'N_p':>4}  {'P_N':>5}  {'mu2/mu1(QW)':>18}  {'mu2/mu1(PW)':>18}  {'|diff|':>14}")
    for r in results:
        if abs(mu1_pw) > mp.mpf('1e-40'):
            rdiff = abs(r['ratio_qw'] - ratio_pw)
            print(f"  {r['n_primes']:4d}  {r['P_N']:5d}"
                  f"  {mp.nstr(r['ratio_qw'], 12):>18s}"
                  f"  {mp.nstr(ratio_pw, 12):>18s}"
                  f"  {mp.nstr(rdiff, 8):>14s}")

    # ------------------------------------------------------------------
    # STEP 6: Transfer conclusion.
    # ------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("TRANSFER ANALYSIS")
    print("=" * 78)

    # Direct norm transfer
    transfers = [r for r in results if r['bound_holds']]
    if transfers:
        N0 = transfers[0]['n_primes']
        P0 = transfers[0]['P_N']
        print(f"\n  DIRECT NORM TRANSFER: ||QW - PW||_op < gap(PW)/2")
        print(f"  holds for N_primes >= {N0} (P_N >= {P0}).")
        print(f"  => Simplicity transfers from Slepian for N >= {N0}")
    else:
        print(f"\n  DIRECT NORM TRANSFER: ||QW - PW||_op < gap(PW)/2")
        print(f"  does NOT hold for any tested prime count.")
        print(f"  This is expected: QW and PW operate on different scales.")

    # Eigenvalue ratio analysis
    print(f"\n  RATIO ANALYSIS (scale-invariant):")
    print(f"  If mu_2/mu_1 converges for QW -> PW, simplicity of PW")
    print(f"  implies mu_2 != mu_1 for QW at large enough prime count.")
    if len(results) >= 2:
        last_ratio = results[-1]['ratio_qw']
        first_ratio = results[0]['ratio_qw']
        if abs(mu1_pw) > mp.mpf('1e-40'):
            drift = abs(last_ratio - ratio_pw)
            print(f"  Last QW ratio:  {mp.nstr(last_ratio, 12)}")
            print(f"  PW ratio:       {mp.nstr(ratio_pw, 12)}")
            print(f"  |difference|:   {mp.nstr(drift, 8)}")
            if drift < abs(ratio_pw - 1) / 2:
                print(f"  Ratio is CONVERGING toward PW value.")
            else:
                print(f"  Ratio has NOT converged to PW value.")

    # Gap positivity
    print(f"\n  GAP POSITIVITY of QW for all tested prime counts:")
    all_positive = all(r['gap_qw'] > 0 for r in results)
    for r in results:
        sign = "+" if r['gap_qw'] > 0 else "ZERO/NEG"
        print(f"    N_p={r['n_primes']:3d}, P_N={r['P_N']:5d}: gap = {mp.nstr(r['gap_qw'], 8)}  [{sign}]")
    if all_positive:
        print(f"\n  All gaps are POSITIVE. Consistent with simplicity at every prime count.")
    else:
        print(f"\n  WARNING: some gaps are non-positive. Investigate.")

    print(f"\n  Total runtime: {time.time() - t_start:.1f}s")
    print("=" * 78)


if __name__ == "__main__":
    main()
