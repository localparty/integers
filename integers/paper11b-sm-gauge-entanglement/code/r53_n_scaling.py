"""R53 — N-scaling of eps at fixed lambda.

The key question: at fixed lambda, does eps_N -> 0 as N -> infinity?
Also: at fixed N, does eps vary with lambda?

This distinguishes the Galerkin convergence rate from the lambda dependence.
"""

import os, sys, time, math
import mpmath as mp

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r49_fourier_circle import (
    build_W02, precompute_abc, build_WR, q_UnUm, eigh_mp,
)
from r51b_evenblock import project_to_even


def primes_up_to(n):
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


def build_Wp_singleprime(N, L, p):
    M = mp.matrix(2 * N + 1)
    coeff = mp.log(p) / mp.sqrt(mp.mpf(p))
    y = mp.log(mp.mpf(p))
    for i in range(2 * N + 1):
        n = i - N
        for j in range(i, 2 * N + 1):
            m = j - N
            v = coeff * q_UnUm(n, m, y, L)
            M[i, j] = v
            M[j, i] = v
    return M


def compute_eps(lam, N, dps):
    """Compute smallest even eigenvalue of QW^{lambda,N}."""
    mp.mp.dps = dps
    L = 2 * mp.log(lam)

    W02 = build_W02(N, L)
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)

    Q_full = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q_full[i, j] = W02[i, j] - WR[i, j]

    lam_sq = float(lam * lam)
    prime_list = primes_up_to(int(math.floor(lam_sq)))
    for p in prime_list:
        Wp = build_Wp_singleprime(N, L, p)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q_full[i, j] -= Wp[i, j]

    Q_ev = project_to_even(Q_full, N)
    vals, _ = eigh_mp(Q_ev)
    return float(vals[0]), float(vals[1]), len(prime_list)


def main():
    dps = 50

    # Part 1: N-scaling at fixed lambda = sqrt(13)
    print("="*70)
    print("PART 1: N-scaling at lambda = sqrt(13)")
    print("="*70)
    lam = mp.sqrt(mp.mpf(13))
    for N in [10, 20, 30, 40, 60, 80]:
        t0 = time.time()
        eps, mu2, np_ = compute_eps(lam, N, dps)
        dt = time.time() - t0
        print(f"  N={N:>3d}: eps = {eps:>14.8f}, mu2 = {mu2:>14.8f}, "
              f"gap = {mu2-eps:>12.8f}, #p={np_}, [{dt:.1f}s]")

    # Part 2: lambda-scaling at fixed N = 30
    print(f"\n{'='*70}")
    print("PART 2: lambda-scaling at fixed N = 30")
    print("="*70)
    N = 30
    for lam_val in [3.6056, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0]:
        lam = mp.mpf(lam_val)
        t0 = time.time()
        eps, mu2, np_ = compute_eps(lam, N, dps)
        dt = time.time() - t0
        print(f"  lam={lam_val:>7.3f}: eps = {eps:>14.8f}, mu2 = {mu2:>14.8f}, "
              f"gap = {mu2-eps:>12.8f}, #p={np_:>3d}, [{dt:.1f}s]")

    # Part 3: At large N with fixed lambda, does eps approach 0?
    # The R49 result at N=120 showed eps ~ 3.5e-59 at dps=110.
    # Let's check at N=120 with dps=50.
    print(f"\n{'='*70}")
    print("PART 3: High N check at lambda = sqrt(13), dps=50")
    print("="*70)
    lam = mp.sqrt(mp.mpf(13))
    for N in [100, 120]:
        t0 = time.time()
        eps, mu2, np_ = compute_eps(lam, N, dps)
        dt = time.time() - t0
        print(f"  N={N:>3d}: eps = {eps:>20.12e}, mu2 = {mu2:>20.12e}, "
              f"gap = {mu2-eps:>14.6e}, [{dt:.1f}s]")


if __name__ == "__main__":
    main()
