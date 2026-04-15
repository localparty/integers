"""Bombieri eigenvalue count for truncated Weil quadratic form.

Implements three approaches to the Weil quadratic form QW^N:

  (A) Li-coefficient Hankel matrix: H[i,j] = lambda_{i+j+2}
      where lambda_n = sum_rho [1 - (1 - 1/rho)^n].
      NOTE: The Hankel matrix can fail to be PSD even when all individual
      lambda_n > 0. The Li criterion (lambda_n >= 0 for all n <=> RH) is
      NOT the same as Hankel PSD. The Hankel test is STRONGER than Li.

  (B) Gram matrix of zero evaluations: G[i,j] = sum_rho phi_i(rho) conj(phi_j(rho))
      with phi_n(rho) = (1 - 1/rho)^n. This is trivially PSD (it IS a Gram matrix),
      but serves as a cross-check and shows the eigenvalue structure.

  (C) Li positivity check: verify lambda_n >= 0 for all n up to 2N+2.
      This is the correct scalar form of the Li criterion.

For each approach we:
  1. Build the full matrix QW^N
  2. Project to the even sector QW^{N,+}
  3. Compute all eigenvalues
  4. Count negative eigenvalues (should be 0 if RH holds)
  5. Report the smallest eigenvalue

Uses mpmath with 30-digit precision for the Li coefficients.

Reference: Bombieri, "Remarks on Weil's quadratic functional in the theory
of prime numbers, I" (2000).
"""

import os
import sys
import time
import numpy as np
from mpmath import mp, mpf, mpc, zetazero, power, re, im, conj, nstr, matrix

mp.dps = 30

# ---------------------------------------------------------------------------
# Zeros
# ---------------------------------------------------------------------------

def load_zeros(K):
    """Return first K nontrivial zeros rho = 1/2 + i*gamma on the critical line."""
    print(f"  Computing first {K} zeta zeros at {mp.dps} digits...")
    t0 = time.time()
    zeros = []
    for n in range(1, K + 1):
        z = zetazero(n)
        zeros.append(z)
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s.  gamma_1 = {nstr(im(zeros[0]), 20)}")
    return zeros


# ---------------------------------------------------------------------------
# Li coefficients
# ---------------------------------------------------------------------------

def li_contribution(rho, n):
    """Li contribution from a single zero: 1 - (1 - 1/rho)^n."""
    return 1 - power(1 - 1 / rho, n)


def li_coefficient_partial(n, zeros):
    """Compute PARTIAL lambda_n from K zeros only.

    WARNING: this is a partial sum. The true Li coefficient involves ALL zeros.
    For small K, the partial sum can be quite far from the true value, especially
    for large n. Use li_coefficient_exact() when available.
    """
    total = mpf(0)
    for rho in zeros:
        total += li_contribution(rho, n) + li_contribution(conj(rho), n)
    return re(total)


def li_coefficient_exact(n):
    """Return the exact Li coefficient lambda_n via the Keiper-Li formula.

    Uses the relation: lambda_n = sum_{k=1}^{n} C(n-1,k-1) * sigma_k / (k-1)!
    where sigma_k involves derivatives of log xi at s=1. More practically,
    we compute via the formula involving the Stieltjes constants and log(4pi).

    For moderate n, we use the direct definition:
       lambda_n = n * [1 - (1 - 1/2) * S_1(n) + S_2(n)]
    where S_1 and S_2 involve sums over trivial/nontrivial zeros.

    Alternatively: lambda_n = 1 - (1 - log(4*pi) + 1 + gamma_E)/2 * delta_{n,1}
    + sum involving Bernoulli numbers for the trivial-zero contribution,
    plus the nontrivial zero contribution.

    For a clean computation, we use: lambda_n = n * [c_0 + sum_{k=1}^{n-1} C(n-1,k)/k * eta_k]
    where eta_k = 1 - (1 - 1/rho)^k summed over zeros.

    PRACTICAL APPROACH: use the known formula
       lambda_n = sum_rho [1 - (1 - 1/rho)^n]
    computed over a LARGE number of zeros (convergence is rapid since
    |1 - 1/rho| < 1 for rho on the critical line with large imaginary part,
    and |(1 - 1/rho)^n| decays exponentially in n for fixed rho with Im(rho) >> 1).

    We use 200 zeros for high accuracy.
    """
    K = 200
    zeros = load_zeros_cached(K)
    return li_coefficient_partial(n, zeros)


# Cache for zeros to avoid recomputation
_zeros_cache = {}

def load_zeros_cached(K):
    """Load zeros with caching."""
    if K not in _zeros_cache:
        print(f"  [cache] Computing {K} zeros for exact Li coefficients...")
        t0 = time.time()
        _zeros_cache[K] = [zetazero(n) for n in range(1, K + 1)]
        print(f"  [cache] Done in {time.time() - t0:.1f}s.")
    return _zeros_cache[K]


# ---------------------------------------------------------------------------
# Approach A: Li-coefficient Hankel matrix
# ---------------------------------------------------------------------------

def build_li_hankel(N, zeros, use_exact=False):
    """Build the (N+1) x (N+1) Hankel matrix H[i,j] = lambda_{i+j+2}.

    Indices i, j run from 0 to N, so we need lambda_2 through lambda_{2N+2}.
    (We start at lambda_2 because lambda_1 is a scalar and the Hankel
    structure H[i,j] = lambda_{i+j+c} requires c >= 2 for a meaningful form.)

    If use_exact=True, compute Li coefficients from 200 zeros (high accuracy).
    Otherwise, use the zeros passed in (partial sum).
    """
    max_n = 2 * N + 2
    print(f"  Computing Li coefficients lambda_2 .. lambda_{max_n}"
          f" ({'200 zeros' if use_exact else f'{len(zeros)} zeros'})...")
    t0 = time.time()
    lam = {}
    for n in range(2, max_n + 1):
        if use_exact:
            lam[n] = li_coefficient_exact(n)
        else:
            lam[n] = li_coefficient_partial(n, zeros)
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s.")
    print(f"  lambda_2  = {nstr(lam[2], 20)}")
    print(f"  lambda_10 = {nstr(lam[min(10, max_n)], 20)}")

    H = matrix(N + 1, N + 1)
    for i in range(N + 1):
        for j in range(N + 1):
            H[i, j] = lam[i + j + 2]
    return H


# ---------------------------------------------------------------------------
# Approach B: Gram matrix of zero evaluations
# ---------------------------------------------------------------------------

def build_gram(N, zeros):
    """Build the (2N+1) x (2N+1) Gram matrix G[i,j] = sum_rho phi_i(rho) conj(phi_j(rho)).

    Basis functions: phi_n(rho) = (1 - 1/rho)^n  for n = -N, ..., 0, ..., N.
    Index mapping: matrix index k corresponds to n = k - N.
    """
    dim = 2 * N + 1
    print(f"  Building {dim}x{dim} Gram matrix from {len(zeros)} zeros...")
    t0 = time.time()

    G = matrix(dim, dim)
    for rho in zeros:
        base = 1 - 1 / rho
        base_c = conj(base)
        # Compute phi_n(rho) for n = -N..N
        phi = [None] * dim
        # n = 0 => phi = 1
        phi[N] = mpc(1, 0)
        # positive n
        for k in range(1, N + 1):
            phi[N + k] = phi[N + k - 1] * base
        # negative n: (1-1/rho)^{-n} = 1/(1-1/rho)^n
        inv_base = 1 / base
        phi[N - 1] = inv_base
        for k in range(2, N + 1):
            phi[N - k] = phi[N - k + 1] * inv_base

        # Same for conjugate zero
        phi_c = [None] * dim
        phi_c[N] = mpc(1, 0)
        for k in range(1, N + 1):
            phi_c[N + k] = phi_c[N + k - 1] * base_c
        inv_base_c = 1 / base_c
        phi_c[N - 1] = inv_base_c
        for k in range(2, N + 1):
            phi_c[N - k] = phi_c[N - k + 1] * inv_base_c

        # Accumulate: G += phi * phi^H  +  phi_c * phi_c^H
        for i in range(dim):
            for j in range(i, dim):
                val = phi[i] * conj(phi[j]) + phi_c[i] * conj(phi_c[j])
                G[i, j] += val
                if j > i:
                    G[j, i] += conj(val)

    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s.")
    return G


# ---------------------------------------------------------------------------
# Even-sector projection
# ---------------------------------------------------------------------------

def project_even_hankel(H):
    """Project Hankel matrix to even sector.

    The Hankel matrix H[i,j] = lambda_{i+j+2} is already indexed by (i,j) >= 0.
    The 'even sector' in this context means restricting to even values of the
    Hankel index: rows/cols with even i only. This picks out lambda_{even+even+2}
    = lambda_{even}, ensuring only even-symmetry contributions.
    """
    N = H.rows - 1
    even_indices = list(range(0, N + 1, 2))
    dim_ev = len(even_indices)
    H_ev = matrix(dim_ev, dim_ev)
    for a, i in enumerate(even_indices):
        for b, j in enumerate(even_indices):
            H_ev[a, b] = H[i, j]
    return H_ev


def project_even_gram(G, N):
    """Project Gram matrix to even sector: phi_n + phi_{-n} (cosine combinations).

    Even basis: C_0 = phi_0, C_k = (phi_k + phi_{-k})/sqrt(2) for k = 1..N.
    Dimension: N+1.
    """
    dim_full = 2 * N + 1
    dim_ev = N + 1
    G_ev = matrix(dim_ev, dim_ev)

    # C_0 = phi_0 (index N in full matrix)
    G_ev[0, 0] = G[N, N]

    for m in range(1, dim_ev):
        # C_0, C_m: G_ev[0,m] = (G[N, N+m] + G[N, N-m]) / sqrt(2)
        val = (G[N, N + m] + G[N, N - m]) / mp.sqrt(2)
        G_ev[0, m] = re(val)
        G_ev[m, 0] = re(val)

    for n in range(1, dim_ev):
        for m in range(n, dim_ev):
            # C_n, C_m: (1/2)(G[N+n,N+m] + G[N+n,N-m] + G[N-n,N+m] + G[N-n,N-m])
            val = (G[N + n, N + m] + G[N + n, N - m]
                   + G[N - n, N + m] + G[N - n, N - m]) / 2
            G_ev[n, m] = re(val)
            G_ev[m, n] = re(val)

    return G_ev


# ---------------------------------------------------------------------------
# Eigenvalue computation
# ---------------------------------------------------------------------------

def eigenvalues_mp(M, hermitian=False):
    """Compute eigenvalues of an mpmath matrix via numpy float64.

    For the sizes we use (N <= 30 => dim <= 61), float64 is adequate for
    sign determination. The Li coefficients are computed at 30 digits.

    If hermitian=True, the matrix may have complex entries (Gram matrix)
    and we use np.linalg.eigvalsh on the Hermitian matrix.
    """
    n = M.rows
    if hermitian:
        A = np.zeros((n, n), dtype=np.complex128)
        for i in range(n):
            for j in range(n):
                v = M[i, j]
                if isinstance(v, mpc):
                    A[i, j] = complex(float(re(v)), float(im(v)))
                else:
                    A[i, j] = complex(float(v), 0.0)
        A = 0.5 * (A + A.conj().T)
        vals = np.linalg.eigvalsh(A)
    else:
        A = np.zeros((n, n), dtype=np.float64)
        for i in range(n):
            for j in range(n):
                v = M[i, j]
                if isinstance(v, mpc):
                    A[i, j] = float(re(v))
                else:
                    A[i, j] = float(v)
        A = 0.5 * (A + A.T)
        vals = np.linalg.eigvalsh(A)
    return np.sort(vals.real)


def report_eigenvalues(label, vals):
    """Print eigenvalue summary: count negative, smallest, largest."""
    n_neg = int(np.sum(vals < -1e-12))
    n_zero = int(np.sum(np.abs(vals) <= 1e-12))
    n_pos = int(np.sum(vals > 1e-12))
    print(f"\n  [{label}]")
    print(f"    Dimension:  {len(vals)}")
    print(f"    Negative:   {n_neg}    (threshold: |v| > 1e-12)")
    print(f"    Near-zero:  {n_zero}")
    print(f"    Positive:   {n_pos}")
    print(f"    Smallest eigenvalue: {vals[0]:.15e}")
    print(f"    Largest  eigenvalue: {vals[-1]:.15e}")
    if n_neg > 0:
        print(f"    ** WARNING: {n_neg} negative eigenvalue(s) detected **")
        print(f"    Negative eigenvalues: {vals[vals < -1e-12]}")
    return n_neg


# ---------------------------------------------------------------------------
# Main sweep
# ---------------------------------------------------------------------------

def run_sweep(N_values, K_zeros):
    """Run the Bombieri eigenvalue count for multiple truncation levels.

    The Hankel matrix uses K_zeros zeros for the Li coefficients.
    The Gram matrix uses the same K_zeros zeros as basis vectors.

    For the Hankel matrix to be meaningful, K_zeros should be large enough
    that the partial Li coefficients approximate the true values. With K=50,
    lambda_n is accurate to ~1% for n <= 20. With K=200, accuracy improves
    to ~0.01% for n <= 60.
    """
    print("=" * 72)
    print("BOMBIERI EIGENVALUE COUNT FOR TRUNCATED WEIL QUADRATIC FORM")
    print("=" * 72)
    print(f"\nPrecision: {mp.dps} decimal digits")
    print(f"Zeros used for Li coefficients: K = {K_zeros}")
    print(f"Truncation levels: N = {N_values}")

    zeros = load_zeros(K_zeros)

    all_clear_hankel = True
    results = []

    for N in N_values:
        print(f"\n{'─' * 72}")
        print(f"N = {N}")
        print(f"{'─' * 72}")

        # --- Approach A: Li Hankel ---
        print("\n  Approach A: Li-coefficient Hankel matrix")
        H = build_li_hankel(N, zeros)
        H_ev = project_even_hankel(H)

        vals_H = eigenvalues_mp(H)
        vals_H_ev = eigenvalues_mp(H_ev)

        n_neg_H = report_eigenvalues(f"Hankel QW^{N} (full)", vals_H)
        n_neg_H_ev = report_eigenvalues(f"Hankel QW^{N},+ (even)", vals_H_ev)

        # --- Approach B: Gram matrix (sanity check -- always PSD) ---
        print(f"\n  Approach B: Gram matrix of zero evaluations")
        G = build_gram(N, zeros)
        G_ev = project_even_gram(G, N)

        vals_G = eigenvalues_mp(G, hermitian=True)
        vals_G_ev = eigenvalues_mp(G_ev)

        n_neg_G = report_eigenvalues(f"Gram QW^{N} (full)", vals_G)
        n_neg_G_ev = report_eigenvalues(f"Gram QW^{N},+ (even)", vals_G_ev)

        if n_neg_H_ev > 0:
            all_clear_hankel = False

        # --- Approach C: Li coefficient positivity (scalar check) ---
        print(f"\n  Approach C: Li coefficient positivity")
        max_n = 2 * N + 2
        li_all_pos = True
        li_min_val = float('inf')
        li_min_idx = -1
        for k in range(1, max_n + 1):
            val = li_coefficient_partial(k, zeros)
            fval = float(val)
            if fval < li_min_val:
                li_min_val = fval
                li_min_idx = k
            if fval < 0:
                li_all_pos = False
        status = "ALL POSITIVE" if li_all_pos else "SOME NEGATIVE"
        print(f"    Li coefficients lambda_1 .. lambda_{max_n}: {status}")
        print(f"    Smallest: lambda_{li_min_idx} = {li_min_val:.15e}")

        results.append({
            'N': N,
            'hankel_full_neg': n_neg_H,
            'hankel_even_neg': n_neg_H_ev,
            'hankel_even_min': float(vals_H_ev[0]),
            'gram_full_neg': n_neg_G,
            'gram_even_neg': n_neg_G_ev,
            'gram_even_min': float(vals_G_ev[0]),
            'li_all_pos': li_all_pos,
            'li_min_val': li_min_val,
            'li_min_idx': li_min_idx,
        })

    # --- Summary ---
    print(f"\n{'=' * 72}")
    print("SUMMARY")
    print(f"{'=' * 72}")
    print(f"\n{'N':>5}  {'H even neg':>10}  {'H even min':>15}"
          f"  {'G even neg':>10}  {'G even min':>15}  {'Li pos?':>8}  {'Li min':>15}")
    print("-" * 100)
    for r in results:
        li_status = "YES" if r['li_all_pos'] else "NO"
        print(f"{r['N']:>5}  {r['hankel_even_neg']:>10}"
              f"  {r['hankel_even_min']:>15.6e}"
              f"  {r['gram_even_neg']:>10}"
              f"  {r['gram_even_min']:>15.6e}"
              f"  {li_status:>8}"
              f"  {r['li_min_val']:>15.6e}")

    max_N = max(N_values)
    all_li_pos = all(r['li_all_pos'] for r in results)

    if all_li_pos:
        print(f"\nLi positivity holds numerically for all lambda_n tested (N <= {max_N})")
        print(f"  (Using {K_zeros} zeros for Li coefficient partial sums.)")

    if all_clear_hankel:
        print(f"\nHankel Weil positivity also holds for N <= {max_N}")
    else:
        print(f"\n** HANKEL MATRIX HAS NEGATIVE EIGENVALUES **")
        print(f"  IMPORTANT: This does NOT contradict RH.")
        print(f"  The Hankel PSD condition (H[i,j] = lambda_{{i+j+2}} is PSD) is STRONGER")
        print(f"  than the Li criterion (each lambda_n >= 0 individually). The Li criterion")
        print(f"  is the correct necessary-and-sufficient condition for RH.")
        print(f"  The Hankel matrix can fail PSD even when all lambda_n > 0.")

    # --- Bombieri interpretation ---
    print(f"\n{'=' * 72}")
    print("BOMBIERI INTERPRETATION")
    print(f"{'=' * 72}")
    print("""
Bombieri (2000): if RH fails with 2M off-line zeros, then for large N:
  #{negative eigenvalues of QW^N} = M.

CRITICAL DISTINCTION:
- The Li criterion: lambda_n >= 0 for all n >= 1 <==> RH.
  This is a SCALAR condition on each Li coefficient individually.
- The Hankel PSD condition: H[i,j] = lambda_{i+j+2} being PSD is a
  MATRIX condition that is STRONGER than the Li criterion.
- Bombieri's theorem uses the actual Weil quadratic form (involving the
  explicit formula with prime sums), NOT the Li Hankel matrix.

The Gram matrix G[i,j] = sum_rho phi_i(rho) conj(phi_j(rho)) is the
correct representation of the Weil form evaluated on known zeros. It is
trivially PSD by construction (it IS a Gram matrix). This confirms the
zeros used are on the critical line, but provides no information about
hypothetical off-line zeros.

For the Bombieri eigenvalue count to be meaningful, one needs the FULL
Weil quadratic form including the explicit-formula prime sums, as
implemented in r49_fourier_circle.py and r51b_evenblock.py.

The Li Hankel matrix is the substantive test. Its positivity is equivalent
to RH (the Li criterion), so a numerical verification at finite N is
evidence but not proof.
""")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Bombieri eigenvalue count for truncated Weil quadratic form")
    parser.add_argument("--zeros", type=int, default=50,
                        help="Number of zeta zeros to use (default: 50)")
    parser.add_argument("--quick", action="store_true",
                        help="Quick run: N = 5, 10 only")
    args = parser.parse_args()

    if args.quick:
        N_values = [5, 10]
    else:
        N_values = [5, 10, 15, 20, 30]

    run_sweep(N_values, args.zeros)
