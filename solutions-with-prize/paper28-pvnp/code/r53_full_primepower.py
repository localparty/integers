"""R53 — Full prime-power computation for all three approaches.

CRITICAL FIX: use ALL prime powers (2,3,4,5,7,8,9,11,13 at lambda=sqrt(13)),
not just primes. The von Mangoldt function Lambda(p^j) = log(p) applies to
all prime powers, and R49's build_QW includes them all.

This changes everything: with primes only, eps = -0.626.
With all prime powers, eps ~ 10^{-59} (R49 result).
"""

import os, sys, time, math, json
import mpmath as mp

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r49_fourier_circle import (
    build_W02, precompute_abc, build_WR, q_UnUm, eigh_mp,
    von_mangoldt_terms,
)
from r51b_evenblock import project_to_even


def build_Wp_single_primepower(N, L, k, p):
    """Single prime power k = p^j: Lambda(k) * k^{-1/2} * q(U_n,U_m)(log k).
    Lambda(k) = log(p). Returns the POSITIVE Wp matrix."""
    M = mp.matrix(2 * N + 1)
    coeff = mp.log(p) / mp.sqrt(mp.mpf(k))
    y = mp.log(mp.mpf(k))
    if y > L:
        return M  # skip if log k > L (shouldn't happen if k <= lambda^2)
    for i in range(2 * N + 1):
        n = i - N
        for j_idx in range(i, 2 * N + 1):
            m = j_idx - N
            v = coeff * q_UnUm(n, m, y, L)
            M[i, j_idx] = v
            M[j_idx, i] = v
    return M


def trace_ev(M, Nev):
    s = mp.mpf(0)
    for i in range(Nev):
        s += M[i, i]
    return s


def main():
    dps = 50
    mp.mp.dps = dps

    print("="*78)
    print("R53 FULL PRIME-POWER ANALYSIS")
    print("="*78)

    # =====================================================================
    # Part 1: Verify that including all prime powers gives eps ~ 0
    # =====================================================================
    print("\nPart 1: Verify prime-power vs prime-only at lambda=sqrt(13), N=60")

    lam = mp.sqrt(mp.mpf(13))
    L = 2 * mp.log(lam)
    N = 60
    Nev = N + 1

    W02 = build_W02(N, L)
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)

    # Build base Q0 = W02 - WR
    Q_base = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q_base[i, j] = W02[i, j] - WR[i, j]

    Q_base_ev = project_to_even(Q_base, N)
    vals0, _ = eigh_mp(Q_base_ev)
    print(f"  Base (no primes): eps = {mp.nstr(vals0[0], 12)}")

    # Add prime powers one at a time
    pp_terms = von_mangoldt_terms(int(mp.floor(lam * lam + mp.mpf("1e-30"))))
    print(f"  Prime powers <= {int(lam*lam)}: {[(k,p) for k,p in pp_terms]}")

    Q_cur = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q_cur[i, j] = Q_base[i, j]

    for k, p in pp_terms:
        Wp = build_Wp_single_primepower(N, L, k, p)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q_cur[i, j] -= Wp[i, j]

        Q_ev = project_to_even(Q_cur, N)
        tr = trace_ev(Q_ev, Nev)
        vals, _ = eigh_mp(Q_ev)
        eps = vals[0]
        mu2 = vals[1]
        print(f"  After k={k:>2d} (p={p}): eps = {mp.nstr(eps, 12)}, "
              f"mu2 = {mp.nstr(mu2, 12)}, "
              f"gap = {mp.nstr(mu2-eps, 8)}, Tr = {mp.nstr(tr, 10)}")

    # =====================================================================
    # Part 2: APPROACH 2 (Trace) with full prime powers
    # =====================================================================
    print(f"\n{'='*78}")
    print("Part 2: TRACE with full prime powers at lambda=sqrt(13), N=60")
    print(f"{'='*78}")

    # Already computed above. Let's also check the trace decomposition.
    Q_full_ev = project_to_even(Q_cur, N)
    tr_full = trace_ev(Q_full_ev, Nev)
    vals_full, _ = eigh_mp(Q_full_ev)
    eps_full = vals_full[0]

    print(f"  Tr(Q_W^ev) = {mp.nstr(tr_full, 12)}")
    print(f"  eps = {mp.nstr(eps_full, 12)}")
    print(f"  Nev = {Nev}")
    print(f"  Tr - eps = {mp.nstr(tr_full - eps_full, 12)}")
    print(f"  Tr / Nev = {mp.nstr(tr_full / Nev, 12)}")

    # =====================================================================
    # Part 3: APPROACH 1 (Averaged descent) with full prime powers
    # =====================================================================
    print(f"\n{'='*78}")
    print("Part 3: AVERAGED DESCENT with full prime powers")
    print(f"{'='*78}")

    # Reset
    Q_cur2 = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q_cur2[i, j] = Q_base[i, j]

    Q_ev2 = project_to_even(Q_cur2, N)
    vals_prev, _ = eigh_mp(Q_ev2)
    eps_prev = vals_prev[0]

    cum_delta = mp.mpf(0)
    for step, (k, p) in enumerate(pp_terms, 1):
        Wp = build_Wp_single_primepower(N, L, k, p)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q_cur2[i, j] -= Wp[i, j]

        Q_ev2 = project_to_even(Q_cur2, N)
        vals_new, _ = eigh_mp(Q_ev2)
        eps_new = vals_new[0]
        delta = eps_new - eps_prev
        cum_delta += delta
        avg = cum_delta / step

        print(f"  step={step} k={k:>2d} (p^j): eps = {mp.nstr(eps_new, 12)}, "
              f"Delta_eps = {mp.nstr(delta, 10)}, "
              f"cum = {mp.nstr(cum_delta, 10)}, "
              f"avg = {mp.nstr(avg, 10)}")

        eps_prev = eps_new

    # =====================================================================
    # Part 4: lambda-scaling with full prime powers, N=60
    # =====================================================================
    print(f"\n{'='*78}")
    print("Part 4: Lambda-scaling with full prime powers, N=40, dps=50")
    print(f"{'='*78}")

    N = 40
    Nev = N + 1

    for lam_val in [mp.sqrt(mp.mpf(13)), mp.mpf(5), mp.mpf(7)]:
        L = 2 * mp.log(lam_val)
        lam_sq = float(lam_val * lam_val)
        pp = von_mangoldt_terms(int(math.floor(lam_sq)))

        W02 = build_W02(N, L)
        alpha, diag = precompute_abc(N, L, verbose=False)
        WR = build_WR(N, L, alpha, diag)

        Q = mp.matrix(2 * N + 1)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q[i, j] = W02[i, j] - WR[i, j]

        for k, p in pp:
            Wp = build_Wp_single_primepower(N, L, k, p)
            for i in range(2 * N + 1):
                for j in range(2 * N + 1):
                    Q[i, j] -= Wp[i, j]

        Q_ev = project_to_even(Q, N)
        tr = trace_ev(Q_ev, Nev)
        vals, _ = eigh_mp(Q_ev)
        eps = vals[0]
        mu2 = vals[1]

        print(f"  lam={float(lam_val):>7.3f}: #pp={len(pp):>3d}, "
              f"eps = {mp.nstr(eps, 12)}, "
              f"mu2 = {mp.nstr(mu2, 12)}, "
              f"gap = {mp.nstr(mu2-eps, 8)}, "
              f"Tr = {mp.nstr(tr, 10)}")

    # =====================================================================
    # Part 5: Critical convergence analysis
    # =====================================================================
    print(f"\n{'='*78}")
    print("Part 5: CONVERGENCE ANALYSIS")
    print(f"{'='*78}")

    # sum log(p) / sqrt(p^j) over all prime powers p^j
    all_pp = von_mangoldt_terms(1000000)
    cum = 0.0
    milestones = {100: None, 1000: None, 10000: None, 100000: None, 1000000: None}
    for k, p in all_pp:
        cum += math.log(p) / math.sqrt(k)
        if k in milestones or (milestones and k >= min(m for m in milestones if milestones[m] is None)):
            for m in sorted(milestones):
                if milestones[m] is None and k >= m:
                    milestones[m] = cum
                    break

    print("  Partial sums of Sigma Lambda(k) / sqrt(k) over prime powers k:")
    for m in sorted(milestones):
        if milestones[m] is not None:
            print(f"    k <= {m:>8d}: {milestones[m]:>12.4f}")

    # Now the REFINED convergence: sum (Lambda(k))^2 / k
    cum2 = 0.0
    for k, p in all_pp:
        cum2 += (math.log(p))**2 / k

    print(f"\n  Sigma (Lambda(k))^2 / k over prime powers <= 10^6: {cum2:.4f}")
    print(f"  (This is the Mertens-like sum that diverges as (log x)^2)")

    # And: sum (Lambda(k))^2 / k^{3/2}
    cum3 = 0.0
    for k, p in all_pp:
        cum3 += (math.log(p))**2 / (k ** 1.5)

    print(f"  Sigma (Lambda(k))^2 / k^{{3/2}} over prime powers <= 10^6: {cum3:.6f}")
    print(f"  (This CONVERGES)")


if __name__ == "__main__":
    main()
