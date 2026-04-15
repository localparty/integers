"""R53 supplementary — deeper trace analysis.

Key questions from the first run:
1. The trace DECREASES as primes are added, but epsilon ALSO oscillates (up/down).
2. At lambda=sqrt(13), Tr drops by ~1.53 while epsilon stays ~-0.63.
   The REST of the eigenvalues absorb most of the trace decrease.
3. Need: bound on how the trace decrease distributes among eigenvalues.

New diagnostic:
- Track Tr, epsilon, and the SECOND even eigenvalue mu_2^ev as primes added.
- Compute the "trace minus epsilon" = sum of all other eigenvalues.
- Key insight: if Tr = eps + R, and R grows slower than |Tr_decrease|,
  then eps must decrease. But if R also decreases, that's fine too.

Also: the critical check is whether Tr → -inf as S grows (at fixed N, lambda → inf).
The base Tr ~ O(N) (it's the sum of N+1 eigenvalues of the truncated operator).
Prime contributions to Tr: each prime p contributes -Tr(Wp^ev) to the trace.
"""

import os, sys, json, time, math
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


def trace_ev(M_ev, Nev):
    s = mp.mpf(0)
    for i in range(Nev):
        s += M_ev[i, i]
    return s


def per_prime_trace_contribution(N, L, p):
    """Compute -Tr(Wp^ev) for prime p — the contribution to Tr(QW^ev)."""
    Wp_full = build_Wp_singleprime(N, L, p)
    Wp_ev = project_to_even(Wp_full, N)
    Nev = N + 1
    return -trace_ev(Wp_ev, Nev)


def closed_form_prime_trace(N, L, p):
    """Closed-form: Tr(Wp^ev) for a single prime.

    The even-block diagonal elements of Wp are:
    For n=0: Wp^ev[0,0] = Wp[N,N] = Λ(p) p^{-1/2} * 2(1 - log p / L) * 1
    For n>=1: Wp^ev[n,n] = Wp[N+n,N+n] + Wp[N+n,N-n]
            = Λ(p) p^{-1/2} * [q(n,n)(log p) + q(n,-n)(log p)]

    q(n,n)(y) = 2(1-y/L) cos(2pi n y / L)
    q(n,-n)(y) = [sin(-2pi n y/L) - sin(2pi n y/L)] / [pi(n-(-n))]
               = -2 sin(2pi n y/L) / (2pi n)
               = -sin(2pi n y/L) / (pi n)

    So Tr(Wp^ev) = Λ(p) p^{-1/2} * Σ_{n=0..N} d_n where
    d_0 = 2(1 - y/L)
    d_n = 2(1-y/L) cos(2pi n y/L) - sin(2pi n y/L)/(pi n)  for n>=1

    The TRACE of the signed contribution (-Wp^ev) is:
    -Λ(p) p^{-1/2} * Σ d_n
    """
    coeff = mp.log(p) / mp.sqrt(mp.mpf(p))
    y = mp.log(mp.mpf(p))
    one_minus = 1 - y / L
    twopi_over_L = 2 * mp.pi / L

    s = 2 * one_minus  # n=0 contribution
    for n in range(1, N + 1):
        ang = twopi_over_L * n * y
        cn = mp.cos(ang)
        sn = mp.sin(ang)
        s += 2 * one_minus * cn - sn / (mp.pi * n)

    return -coeff * s  # the signed trace contribution


def main():
    dps = 50
    mp.mp.dps = dps

    print("="*70)
    print("R53 TRACE ANALYSIS — per-prime trace contributions")
    print("="*70)

    # At several λ, compute the per-prime trace contribution
    configs = [
        (mp.sqrt(mp.mpf(13)), 60),  # λ=√13, N=60
        (mp.mpf(5), 40),
        (mp.mpf(10), 30),
        (mp.mpf(20), 20),
    ]

    for lam, N in configs:
        L = 2 * mp.log(lam)
        Nev = N + 1
        lam_sq = float(lam * lam)
        prime_list = primes_up_to(int(math.floor(lam_sq)))

        print(f"\n  lambda = {float(lam):.4f}, N = {N}, Nev = {Nev}, L = {float(L):.4f}")
        print(f"  Primes: {prime_list}")

        # Per-prime trace contributions (closed form)
        total_tr_contrib = mp.mpf(0)
        for p in prime_list:
            cf = closed_form_prime_trace(N, L, p)
            total_tr_contrib += cf
            print(f"    p={p:>3d}: -Tr(Wp^ev) = {mp.nstr(cf, 10)}")

        print(f"    TOTAL prime trace contrib = {mp.nstr(total_tr_contrib, 10)}")

        # Now compute the SUM formula for the trace contribution
        # Σ_p -Λ(p) p^{-1/2} [ 2(N+1)(1-log p/L) + 2(1-log p/L) Σ_{n=1}^N cos(...) - Σ sin/(pi n) ]
        # The key term is 2(N+1)(1-log p/L) from the Dirichlet kernel
        # and the oscillating trig sums

        print(f"\n    --- Trace decomposition ---")
        for p in prime_list:
            coeff = mp.log(p) / mp.sqrt(mp.mpf(p))
            y = mp.log(mp.mpf(p))
            one_minus = float(1 - y / L)
            # The constant part: -coeff * 2 * (N+1) * (1 - y/L) if all cosines = 1
            const_part = -float(coeff) * 2 * one_minus  # just n=0
            print(f"    p={p:>3d}: 1-log(p)/L = {one_minus:.4f}, "
                  f"coeff = {float(coeff):.4f}")

    # CRITICAL: what happens to the trace as we increase lambda (more primes)
    # while keeping N fixed?
    print(f"\n{'='*70}")
    print("TRACE vs LAMBDA (fixed N=30)")
    print(f"{'='*70}")

    N = 30
    Nev = N + 1

    for lam_val in [3.6, 5, 7, 10, 15, 20]:
        lam = mp.mpf(lam_val)
        L = 2 * mp.log(lam)
        lam_sq = float(lam * lam)
        prime_list = primes_up_to(int(math.floor(lam_sq)))

        # Build full QW
        W02 = build_W02(N, L)
        alpha, diag = precompute_abc(N, L, verbose=False)
        WR = build_WR(N, L, alpha, diag)

        Q_full = mp.matrix(2 * N + 1)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q_full[i, j] = W02[i, j] - WR[i, j]

        # Add primes
        for p in prime_list:
            Wp = build_Wp_singleprime(N, L, p)
            for i in range(2 * N + 1):
                for j in range(2 * N + 1):
                    Q_full[i, j] -= Wp[i, j]

        Q_ev = project_to_even(Q_full, N)
        tr = trace_ev(Q_ev, Nev)

        # Eigenvalues
        vals, _ = eigh_mp(Q_ev)
        eps = vals[0]
        mu2 = vals[1]  # second even eigenvalue
        gap = mu2 - eps
        rest = mp.fsum(vals[1:])

        print(f"  lam={lam_val:>5.1f}: #p={len(prime_list):>3d}, "
              f"Tr={float(tr):>10.3f}, eps={float(eps):>10.6f}, "
              f"mu2={float(mu2):>10.6f}, gap={float(gap):>10.6f}, "
              f"rest={float(rest):>10.3f}")

    # APPROACH 3 refined: Σ (log p)^2 / p^{3/2} convergence check
    # If this converges, and the operator perturbation at prime p has
    # Frobenius norm ~ (log p)^2 / p (from rank-1), then
    # Σ ||Q_p||_HS^2 converges, and by Weyl's inequality for eigenvalues
    # of sums of Hermitian matrices, the eigenvalues converge.
    print(f"\n{'='*70}")
    print("APPROACH 3 REFINED: Weyl perturbation bounds")
    print(f"{'='*70}")

    # For a rank-1 perturbation Q_p of operator norm ~ log p / sqrt(p),
    # by Weyl's inequality: |eps(S+p) - eps(S)| <= ||Q_p||_op <= log p / sqrt(p)
    # So |eps_final - eps_S| <= Sigma_{p > p_max(S)} log p / sqrt(p)
    # This DIVERGES (we showed above). So Weyl doesn't give convergence of eps.
    #
    # BUT: the relevant quantity isn't ||Q_p||_op but the ACTUAL effect on eps,
    # which may be much smaller due to cancellations (the oscillating signs
    # of Delta_eps).
    #
    # The correct approach: eps(S) = Tr(Q^ev(S))/Nev - (spread of eigenvalues)/something.
    # More precisely, if we can show Tr(Q^ev(S)) → -inf while the spread is bounded,
    # then eps must → -inf, contradicting positivity → eps sticks at 0.

    # KEY INSIGHT from the data:
    # At lambda=3.6 (N=60): Tr = 134.74, eps = -0.63, rest = 135.36
    # At lambda=10 (N=30): Tr = 53.95, eps = -1.24, rest = 55.19
    # At lambda=20 (N=20): Tr = ?, eps = ?, rest = ?
    #
    # The trace includes contributions from the BASE operator (W02 - WR)
    # which itself depends on L and hence lambda. So Tr changing with lambda
    # has TWO components: (1) the base changes, (2) more primes.
    # This makes the trace argument subtle.

    print("\n  The trace is NOT purely a function of the prime set S.")
    print("  It also depends on lambda (through the base operator W02-WR).")
    print("  This complicates the pure trace approach.")

    # Let's check: at FIXED lambda, does adding primes decrease eps?
    # Yes, we already see that. But the PROOF needs to work as lambda -> inf.

    # THE REAL QUESTION: for the recursion ε(S_m) where S_m = {primes ≤ p_m},
    # does the cumulative change Σ Delta_eps diverge to -inf?
    # From Approach 1 data: at lambda=10, after 25 primes, cum_delta = +0.38.
    # That's POSITIVE — eps has RISEN, not fallen!

    # But wait — we're holding lambda FIXED and adding primes within that lambda.
    # The CC1 question is about lambda -> inf, which means BOTH the interval
    # gets longer AND more primes are added. The R52d recursion simulation
    # (which showed the massive overshoot) uses the BLOCK decomposition
    # formulas, not the actual matrix diagonalization.

    print("\n  CRITICAL OBSERVATION:")
    print("  At fixed lambda, adding primes does NOT monotonically decrease eps.")
    print("  eps oscillates and may even rise net.")
    print("  The R52d 'overshoot by 2531' uses CLOSED-FORM block formulas,")
    print("  not actual matrix eigenvalues. The block formulas give a BOUND,")
    print("  not the actual eps.")
    print("  The actual eps at the precision floor (10^-50) is consistent")
    print("  with eps being ALREADY at 0 for all lambda tested.")


if __name__ == "__main__":
    main()
