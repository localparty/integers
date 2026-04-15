"""R53 — Envelope descent: three approaches to proving ε(S) → 0.

Approach 2: Trace identity — compute Tr(Q_W^{ev,(S)}) as primes are added.
Approach 1: Averaged descent — running average of Δε_m over many primes.
Approach 3: Operator-norm convergence — does Σ log p / √p converge?

Uses r49_fourier_circle builders and r51b_evenblock projection.
"""

import os, sys, json, time, math
import mpmath as mp

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r49_fourier_circle import (
    build_W02, precompute_abc, build_WR, q_UnUm, eigh_mp,
    von_mangoldt_terms,
)
from r51b_evenblock import project_to_even


def build_Wp_singleprime(N, L, p):
    """Single prime p: Λ(p) p^{-1/2} q(U_n,U_m)(log p).
    Returns the POSITIVE Wp matrix (before sign flip)."""
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
    """Trace of an even-block matrix."""
    s = mp.mpf(0)
    for i in range(Nev):
        s += M_ev[i, i]
    return s


def quad_form(A_ev, v_ev):
    Nev = len(v_ev)
    s = mp.mpf(0)
    for i in range(Nev):
        row = mp.mpf(0)
        for j in range(Nev):
            row += A_ev[i, j] * v_ev[j]
        s += v_ev[i] * row
    return s


def frobenius_norm(M, size):
    """Frobenius norm of a matrix."""
    s = mp.mpf(0)
    for i in range(size):
        for j in range(size):
            s += M[i, j] ** 2
    return mp.sqrt(s)


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


# ==========================================================================
# APPROACH 2: Trace identity
# ==========================================================================
def approach2_trace(N, lam, dps):
    """Compute Tr(Q_W^{ev}) as primes are added one at a time.
    Track: trace, ε (smallest eigenvalue), number of even modes."""
    mp.mp.dps = dps
    L = 2 * mp.log(lam)
    Nev = N + 1  # even block dimension

    print(f"\n{'='*70}")
    print(f"APPROACH 2: Trace identity at lambda={float(lam):.4f}, N={N}, dps={dps}")
    print(f"  L = {float(L):.6f}, even-block dim = {Nev}")
    print(f"{'='*70}")

    # Build base operator Q0 = W02 - WR (no primes)
    t0 = time.time()
    W02 = build_W02(N, L)
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)

    Q_cur_full = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q_cur_full[i, j] = W02[i, j] - WR[i, j]

    Q_cur_ev = project_to_even(Q_cur_full, N)
    print(f"  Base operator built [{time.time()-t0:.1f}s]")

    # Diagonalize base
    vals, Q = eigh_mp(Q_cur_ev)
    eps_m = vals[0]
    xi_m = [Q[i, 0] for i in range(Nev)]
    tr0 = trace_ev(Q_cur_ev, Nev)

    print(f"\n  m=0 (no primes): ε = {mp.nstr(eps_m, 12)}, Tr = {mp.nstr(tr0, 12)}")

    # Primes to add
    lam_sq = float(lam * lam)
    prime_list = primes_up_to(int(math.floor(lam_sq)))
    print(f"  Will add {len(prime_list)} primes: {prime_list}")

    rows = []
    rows.append({
        "step": 0, "p": None,
        "eps": float(eps_m), "trace": float(tr0),
        "trace_per_prime_contrib": 0.0,
    })

    for step, p in enumerate(prime_list, 1):
        # Build Wp for this prime, project to even
        Wp_full = build_Wp_singleprime(N, L, p)
        Wp_ev = project_to_even(Wp_full, N)

        # The signed contribution to Q_W is -Wp
        Qp_ev = mp.matrix(Nev)
        for i in range(Nev):
            for j in range(Nev):
                Qp_ev[i, j] = -Wp_ev[i, j]

        # Trace contribution from this prime
        tr_contrib = trace_ev(Qp_ev, Nev)

        # Update current operator
        for i in range(Nev):
            for j in range(Nev):
                Q_cur_ev[i, j] = Q_cur_ev[i, j] + Qp_ev[i, j]

        # New trace and eigenvalues
        tr_new = trace_ev(Q_cur_ev, Nev)
        vals_new, Q_new = eigh_mp(Q_cur_ev)
        eps_new = vals_new[0]

        # Eigenvalue sum check: Tr should equal sum of all eigenvalues
        ev_sum = mp.fsum(vals_new)

        print(f"  m={step} p={p:>3d}: ε = {mp.nstr(eps_new, 10)}, "
              f"Tr = {mp.nstr(tr_new, 10)}, "
              f"ΔTr(p) = {mp.nstr(tr_contrib, 10)}, "
              f"Σeigs = {mp.nstr(ev_sum, 10)}")

        rows.append({
            "step": step, "p": p,
            "eps": float(eps_new),
            "trace": float(tr_new),
            "trace_per_prime_contrib": float(tr_contrib),
            "eig_sum_check": float(ev_sum),
            "delta_eps": float(eps_new - eps_m),
        })

        eps_m = eps_new
        xi_m = [Q_new[i, 0] for i in range(Nev)]
        vals, Q = vals_new, Q_new

    return rows


# ==========================================================================
# APPROACH 1: Averaged descent over many primes
# ==========================================================================
def approach1_averaged(N, lam, dps):
    """Track per-step Δε and the running average over many primes."""
    mp.mp.dps = dps
    L = 2 * mp.log(lam)
    Nev = N + 1

    print(f"\n{'='*70}")
    print(f"APPROACH 1: Averaged descent at lambda={float(lam):.4f}, N={N}, dps={dps}")
    print(f"{'='*70}")

    t0 = time.time()
    W02 = build_W02(N, L)
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)

    Q_cur_full = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            Q_cur_full[i, j] = W02[i, j] - WR[i, j]

    Q_cur_ev = project_to_even(Q_cur_full, N)
    print(f"  Base operator built [{time.time()-t0:.1f}s]")

    vals, Q = eigh_mp(Q_cur_ev)
    eps_m = vals[0]

    lam_sq = float(lam * lam)
    prime_list = primes_up_to(int(math.floor(lam_sq)))

    rows = []
    cum_delta = mp.mpf(0)

    for step, p in enumerate(prime_list, 1):
        Wp_full = build_Wp_singleprime(N, L, p)
        Wp_ev = project_to_even(Wp_full, N)
        Qp_ev = mp.matrix(Nev)
        for i in range(Nev):
            for j in range(Nev):
                Qp_ev[i, j] = -Wp_ev[i, j]

        for i in range(Nev):
            for j in range(Nev):
                Q_cur_ev[i, j] = Q_cur_ev[i, j] + Qp_ev[i, j]

        vals_new, Q_new = eigh_mp(Q_cur_ev)
        eps_new = vals_new[0]
        delta = eps_new - eps_m

        cum_delta += delta
        running_avg = cum_delta / step

        rows.append({
            "step": step, "p": p,
            "eps": float(eps_new),
            "delta_eps": float(delta),
            "cum_delta": float(cum_delta),
            "running_avg": float(running_avg),
        })

        if step <= 10 or step % 5 == 0:
            print(f"  m={step:>3d} p={p:>3d}: Δε = {float(delta):+.6f}, "
                  f"Σ = {float(cum_delta):+.6f}, avg = {float(running_avg):+.6f}")

        eps_m = eps_new
        vals, Q = vals_new, Q_new

    return rows


# ==========================================================================
# APPROACH 3: Operator-norm convergence (Σ log p / √p)
# ==========================================================================
def approach3_opnorm():
    """Check whether Σ_{p prime} log p / √p converges or diverges.
    This is a pure arithmetic check — no matrix building needed."""
    print(f"\n{'='*70}")
    print(f"APPROACH 3: Operator-norm convergence check")
    print(f"{'='*70}")

    # Compute partial sums of Σ log p / √p
    thresholds = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    all_primes = primes_up_to(1000000)

    cum = 0.0
    cum_sq = 0.0  # Σ (log p)^2 / p  (the Mertens sum)
    results = []
    pi = 0
    for p in all_primes:
        cum += math.log(p) / math.sqrt(p)
        cum_sq += (math.log(p))**2 / p
        pi += 1
        if p + 1 > thresholds[0] if thresholds else False:
            results.append({
                "p_max": p, "pi": pi,
                "sum_logp_sqrtp": cum,
                "sum_logp2_p": cum_sq,
            })
            thresholds.pop(0)
            if not thresholds:
                break

    # Also check Σ (log p)^2 / p^{3/2} (convergent?)
    cum_conv = 0.0
    for p in all_primes:
        cum_conv += (math.log(p))**2 / (p ** 1.5)

    print(f"\n  Σ_{{p≤x}} log p / √p  (operator-norm series):")
    print(f"  {'p_max':>10s} {'π(p)':>8s} {'Σ log p/√p':>14s} {'Σ (log p)²/p':>14s}")
    for r in results:
        print(f"  {r['p_max']:>10d} {r['pi']:>8d} {r['sum_logp_sqrtp']:>14.4f} {r['sum_logp2_p']:>14.4f}")

    print(f"\n  Σ_{{p≤10⁶}} (log p)² / p^{{3/2}} = {cum_conv:.6f}  (convergent? {'YES' if cum_conv < 100 else 'check'})")
    print(f"  Σ_{{p≤10⁶}} log p / √p = {cum:.4f}  (divergent: grows like 2√x)")

    # Theoretical prediction: Σ_{p≤x} log p / √p ~ 2√x by PNT
    # Check: 2√(10^6) = 2000. Actual sum should be close.
    print(f"  2√(10⁶) = {2*math.sqrt(1000000):.1f}")
    print(f"  Ratio: Σ / (2√p_max) = {cum / (2*math.sqrt(all_primes[-1])):.4f}")

    # Frobenius norm of the full prime perturbation at finite truncation
    # ||Q_W^(all) - Q_W^(S)||_F ≤ Σ_{p > p_max(S)} log p / √p × ||q||_op
    # Since Σ log p / √p diverges, the full operator is NOT norm-convergent.
    # BUT: the individual perturbation norms are log p / √p, and
    # the EIGENVALUE perturbation (Weyl) is bounded by operator norm,
    # which for rank-1 perturbation ≈ log p / √p.
    # Σ log p / √p DIVERGES => the operator Q_W^(S) does NOT converge
    # in norm to a limit as S → all primes.

    return results, cum_conv, cum


# ==========================================================================
# APPROACH 2b: Trace at multiple λ values (quick, small N)
# ==========================================================================
def approach2_multi_lambda(dps=50):
    """Quick trace computation at multiple λ with small N."""
    mp.mp.dps = dps
    N = 40  # small for speed

    print(f"\n{'='*70}")
    print(f"APPROACH 2b: Trace across λ values, N={N}, dps={dps}")
    print(f"{'='*70}")

    lambdas = [mp.sqrt(mp.mpf(13)), mp.mpf(5), mp.mpf(10)]
    results = []

    for lam in lambdas:
        L = 2 * mp.log(lam)
        Nev = N + 1
        lam_sq = float(lam * lam)
        prime_list = primes_up_to(int(math.floor(lam_sq)))

        # Build full Q_W with all primes
        W02 = build_W02(N, L)
        alpha, diag = precompute_abc(N, L, verbose=False)
        WR = build_WR(N, L, alpha, diag)

        # Base (no primes)
        Q_base_full = mp.matrix(2 * N + 1)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q_base_full[i, j] = W02[i, j] - WR[i, j]
        Q_base_ev = project_to_even(Q_base_full, N)
        tr_base = trace_ev(Q_base_ev, Nev)

        # Accumulate prime contributions
        tr_primes_total = mp.mpf(0)
        Q_full = mp.matrix(2 * N + 1)
        for i in range(2 * N + 1):
            for j in range(2 * N + 1):
                Q_full[i, j] = Q_base_full[i, j]

        for p in prime_list:
            Wp = build_Wp_singleprime(N, L, p)
            for i in range(2 * N + 1):
                for j in range(2 * N + 1):
                    Q_full[i, j] -= Wp[i, j]

        Q_ev = project_to_even(Q_full, N)
        tr_full = trace_ev(Q_ev, Nev)
        tr_prime_contrib = tr_full - tr_base

        # Eigenvalues
        vals, _ = eigh_mp(Q_ev)
        eps = vals[0]

        # Sum of eigenvalues except the smallest
        rest_sum = mp.fsum(vals[1:])

        print(f"\n  λ = {float(lam):.4f}: {len(prime_list)} primes, L = {float(L):.4f}")
        print(f"    Tr(Q_base^ev)  = {mp.nstr(tr_base, 12)}")
        print(f"    Tr(Q_full^ev)  = {mp.nstr(tr_full, 12)}")
        print(f"    ΔTr (primes)   = {mp.nstr(tr_prime_contrib, 12)}")
        print(f"    ε (smallest)   = {mp.nstr(eps, 12)}")
        print(f"    Sum_{{k>=2}} mu_k = {mp.nstr(rest_sum, 12)}")
        print(f"    Nev = {Nev}, so Tr/Nev = {mp.nstr(tr_full/Nev, 12)}")

        results.append({
            "lambda": float(lam),
            "n_primes": len(prime_list),
            "tr_base": float(tr_base),
            "tr_full": float(tr_full),
            "tr_prime_contrib": float(tr_prime_contrib),
            "eps": float(eps),
            "rest_sum": float(rest_sum),
            "Nev": Nev,
        })

    return results


# ==========================================================================
# MAIN
# ==========================================================================
def main():
    results = {}

    # Approach 3 first — pure arithmetic, instant
    a3_results, a3_conv, a3_div = approach3_opnorm()
    results["approach3"] = {
        "partial_sums": a3_results,
        "sum_logp2_p32_million": a3_conv,
        "sum_logp_sqrtp_million": a3_div,
        "verdict": "Σ log p / √p DIVERGES. Operator-norm convergence FAILS.",
    }

    # Approach 2b: quick multi-lambda trace
    a2b = approach2_multi_lambda(dps=50)
    results["approach2b_multi_lambda"] = a2b

    # Approach 2: detailed trace at λ=√13 with N=60 (moderate)
    a2 = approach2_trace(N=60, lam=mp.sqrt(mp.mpf(13)), dps=50)
    results["approach2_trace_sqrt13"] = a2

    # Approach 1: averaged descent at λ=√13 with N=60
    # (reuses same computation, just tracks running average)
    # Already captured in approach 2. Let's do a slightly larger λ.
    a1 = approach1_averaged(N=40, lam=mp.mpf(5), dps=50)
    results["approach1_averaged_lam5"] = a1

    # Also do averaged at λ=10 for more primes
    a1b = approach1_averaged(N=30, lam=mp.mpf(10), dps=50)
    results["approach1_averaged_lam10"] = a1b

    # Save
    out_path = os.path.join(CODE, "r53_envelope_descent.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n\nJSON written to {out_path}")


if __name__ == "__main__":
    main()
