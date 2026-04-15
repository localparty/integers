"""R53 — The crossing analysis.

At lambda=sqrt(13), N=60: after adding k=9 (p=3, p^2), eps = -0.267.
After adding k=11, eps = 10^{-50}. A jump of 0.267 in one step.

This is the "sticking" phenomenon: eps reaches its floor of 0 at a
SPECIFIC prime power (k=11 at lambda=sqrt(13)).

Questions:
1. Is this behavior consistent across lambda?
2. At larger lambda, does the crossing happen earlier or later?
3. Can we identify WHICH prime power causes the sticking?

For the envelope proof: the key is that eps converges to 0 AS LAMBDA
GROWS. At each lambda, eps is already ~0 (precision floor). The
question CC1 asks is whether the LIMIT eps_lambda as lambda -> infinity
is 0.

Since eps_lambda ~ 10^{-50} at every lambda tested (with enough prime
powers), the evidence is overwhelming. But we need a PROOF.

THE PROOF IDEA (refined from all three approaches):

The operator Q_W^{lambda,N} = W02 - WR - Sigma_{k<=lambda^2} Lambda(k) k^{-1/2} q(log k)

At each lambda, this is a FINITE rank perturbation of W02 - WR.
The finite-rank perturbation adds O(pi(lambda^2) + ...) rank-1 terms.

R44E: even ground state is simple at every (lambda, N).
R49: xi-hat's zeros match gamma_n to 10^{-47}.
R52c: Galerkin interchange (N -> inf limit commutes with lambda -> inf).
R51A: spectral gap delta^ev <= 3 uniformly.

The MISSING piece is: does the operator-level fact "eps_lambda ~ 0 at
each tested lambda" extend to a PROOF that eps_lambda -> 0?

THE ANSWER IS IN THE BLOCK DECOMPOSITION.

R51A + R52d: Q_W decomposes as a direct sum L_inf OPLUS bigoplus L_p.
Each L_p block has ground state mu_0(L_p) = -p^{-1/2}(1-p^{-1/2}).
The archimedean block L_inf has its own ground state.

Under the (H_S) hypothesis, the GLOBAL ground state is the archimedean
one, and eps_lambda = mu_0(L_inf).

But mu_0(L_inf) is the ground state of the W02 - WR operator projected
to the infinite-dimensional Hermite-like block. This is LAMBDA-INDEPENDENT
in the block decomposition (it comes from the archimedean contribution alone).

Wait -- that can't be right. If mu_0(L_inf) is lambda-independent, then
eps_lambda is constant, not -> 0. And indeed the data shows eps ~ 10^{-50}
at ALL lambda tested. So eps IS essentially 0 at every lambda (once all
prime powers are included).

THE ACTUAL QUESTION: is eps exactly 0 in the N->infinity limit?

CC1 Cor 3.8 asks: lim_{N->inf} mu_1^ev(lambda, N) = ? and then
lim_{lambda->inf} of that.

At finite N, mu_1^ev is a very small negative number (10^{-50} to 10^{-59}
depending on N and dps). As N -> infinity, this approaches some
eps_lambda. CC1 conjectures eps_lambda -> 0 as lambda -> inf.

But OUR DATA shows eps ~ 10^{-50} already at lambda = sqrt(13)!
It doesn't need lambda -> infinity. The convergence to 0 happens
in the N -> infinity limit at FIXED lambda.

This suggests: the proof should be about N -> infinity convergence,
not about lambda -> infinity convergence. And R52c already handles that.

Let me verify: is eps getting closer to 0 as N increases?
"""

import os, sys, time, math
import mpmath as mp

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r49_fourier_circle import (
    build_W02, precompute_abc, build_WR, q_UnUm, eigh_mp,
    von_mangoldt_terms,
)
from r51b_evenblock import project_to_even


def build_Wp_single_primepower(N, L, k, p):
    M = mp.matrix(2 * N + 1)
    coeff = mp.log(p) / mp.sqrt(mp.mpf(k))
    y = mp.log(mp.mpf(k))
    if y > L:
        return M
    for i in range(2 * N + 1):
        n = i - N
        for j_idx in range(i, 2 * N + 1):
            m = j_idx - N
            v = coeff * q_UnUm(n, m, y, L)
            M[i, j_idx] = v
            M[j_idx, i] = v
    return M


def compute_full_eps(lam, N, dps):
    """Compute eps with ALL prime powers."""
    mp.mp.dps = dps
    L = 2 * mp.log(lam)

    W02 = build_W02(N, L)
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)

    Q = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q[i, j] = W02[i, j] - WR[i, j]

    lam_sq = float(lam * lam)
    pp = von_mangoldt_terms(int(math.floor(lam_sq)))

    for k, p in pp:
        Wp = build_Wp_single_primepower(N, L, k, p)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q[i, j] -= Wp[i, j]

    Q_ev = project_to_even(Q, N)
    vals, _ = eigh_mp(Q_ev)
    return vals[0], vals[1], len(pp)


def main():
    print("="*78)
    print("R53 CROSSING ANALYSIS")
    print("="*78)

    # Part 1: N-scaling at fixed lambda=sqrt(13) with ALL prime powers
    print("\nPart 1: N-scaling at lambda=sqrt(13), full prime powers")
    lam = mp.sqrt(mp.mpf(13))
    for dps_val, N_list in [(30, [10, 20, 30, 40]), (50, [60, 80])]:
        for N in N_list:
            t0 = time.time()
            eps, mu2, npp = compute_full_eps(lam, N, dps_val)
            dt = time.time() - t0
            print(f"  N={N:>3d} dps={dps_val:>3d}: eps = {mp.nstr(eps, 15)}, "
                  f"mu2 = {mp.nstr(mu2, 15)}, "
                  f"#pp={npp}, [{dt:.1f}s]")

    # Part 2: N-scaling at lambda=5 with ALL prime powers
    print(f"\nPart 2: N-scaling at lambda=5, full prime powers")
    lam = mp.mpf(5)
    for dps_val, N_list in [(30, [10, 20, 30, 40]), (50, [60])]:
        for N in N_list:
            t0 = time.time()
            eps, mu2, npp = compute_full_eps(lam, N, dps_val)
            dt = time.time() - t0
            print(f"  N={N:>3d} dps={dps_val:>3d}: eps = {mp.nstr(eps, 15)}, "
                  f"mu2 = {mp.nstr(mu2, 15)}, "
                  f"#pp={npp}, [{dt:.1f}s]")

    # Part 3: Lambda-scaling at fixed N=40, dps=50 with ALL prime powers
    print(f"\nPart 3: Lambda-scaling at N=40, dps=50, full prime powers")
    N = 40
    for lam_val in [mp.sqrt(mp.mpf(13)), mp.mpf(4), mp.mpf(5), mp.mpf(7), mp.mpf(10)]:
        t0 = time.time()
        eps, mu2, npp = compute_full_eps(lam_val, N, 50)
        dt = time.time() - t0
        print(f"  lam={float(lam_val):>7.3f}: eps = {mp.nstr(eps, 15)}, "
              f"mu2 = {mp.nstr(mu2, 15)}, "
              f"#pp={npp:>3d}, [{dt:.1f}s]")


if __name__ == "__main__":
    main()
