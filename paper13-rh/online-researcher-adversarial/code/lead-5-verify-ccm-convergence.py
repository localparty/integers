"""
Lead 5: Re-verify CCM-2025 D(λ,N) eigenvalue convergence — FIX of Lead 1.

PRECISION DECLARATION (Round 003 rule e.3):
  mp.dps = 200, matching Connes' convention in CCM-2025. At (λ=4, N=30) the
  L1 reconciliation memo found that the smallest eigenvalue gap cascades into
  the 10^-47 .. 10^-53 range at dps=60, which is within 13 orders of magnitude
  of the precision floor 10^-60 — i.e. we CAN NOT tell a real gap from a
  numerical-floor artifact at dps=60. Bumping to dps=200 pushes the floor
  to 10^-200 and leaves ~140 orders of headroom above any putative real gap,
  which is necessary to decide whether the matrix is "simple" at this point.

FIXES vs lead-1-verify-ccm-convergence.py (per research/01-reconciliation §3):

  1. γ_L(n) additive constant: replace the (incorrect) page-15 reduced form
     `c(L)+w(L) = (1/2)log((e^{L/2}-1)/(e^{L/2}+1)) + atan(e^{L/2}) - π/4
                  + γ_E/2 + (1/2)log(8π)`
     with the page-14 direct form
     `w(L) = (1/2)(γ_E + log(4π)) - (1/2)log((e^L+1)/(e^L-1))`.
     The CCM 2025 paper has a transcription inconsistency between eqs
     (4.11)/(4.14) on p.14 and the "simplified" form on p.15; the p.14 form
     is the correct one. L1 used the p.15 form, producing a uniform diagonal
     shift of -1.38832·I. See §D row `CCM-page-14-15-inconsistency`.

  2. Precision bump dps 60 -> 200 (§D row `Precision-floor-rule`).

  3. Golden-reference cross-check: directly-from-eq(4.4) quadrature of
     W_R(V_n,V_n) per the reconciliation memo,
       W_R(V_n,V_n) = (γ_E + log(4π(e^L-1)/(e^L+1)))
                    + int_0^L [e^(x/2) * 2(1-x/L) cos(2π n x/L) - 2]
                              / (e^x - e^(-x)) dx
     is used to VERIFY the closed-form computation at n=0..3 to ≥40 digits.

  4. Expanded simplicity-gap reporting: we compute and report μ_1-μ_0,
     μ_2-μ_1, μ_3-μ_2 at dps=200 (so we can tell a real gap from a
     numerical-floor artifact).

  5. Decay-rate fit: at (λ, N=30) for λ ∈ {2, 3, 4, 5, 6, 7, 8} we compute
     |γ_1 - eig_1(λ)| and do a least-squares log-|err| vs λ² fit to extract
     the decay slope. The Cycle-1 L1 Adversary corrected L1's overstated
     slope of -4.5 to a true slope of ~-3.37; we will independently reproduce.
"""

import time
import math
from mpmath import (
    mp, mpf, pi, log, exp, sin, cos, sqrt, matrix, eig, atan,
    findroot, euler, zetazero, quad, nstr,
)

# ---- Precision (Round 003 declaration) ------------------------------------
mp.dps = 200
PRECISION_DECLARED = 200
# ----------------------------------------------------------------------------


def alpha_L(n, L):
    """α_L(n) = (1/π) · ∫_0^L sin(2π n x / L) · ρ(x) dx, ρ(x)=e^(x/2)/(e^x-e^(-x))."""
    if n == 0:
        return mpf(0)
    L = mpf(L)
    n = mpf(n)
    rho = lambda x: exp(x / 2) / (exp(x) - exp(-x))
    f = lambda x: sin(2 * pi * n * x / L) * rho(x)
    return quad(f, [0, L]) / pi


def beta_L(n, L):
    """β_L(n) = (1/L) · ∫_0^L x cos(2π n x / L) ρ(x) dx."""
    L = mpf(L)
    n = mpf(n)
    rho = lambda x: exp(x / 2) / (exp(x) - exp(-x))
    f = lambda x: x * cos(2 * pi * n * x / L) * rho(x)
    return quad(f, [0, L]) / L


def gamma_L_fixed(n, L):
    """γ_L(n) per CCM 2025 eqs (4.11)/(4.14) on page 14 (the correct form).

    γ_L(n) = ∫_0^L (cos(2πnx/L) − e^(−x/2)) ρ(x) dx + w(L)
    where
        w(L) = (1/2)(γ_E + log(4π)) − (1/2) log((e^L+1)/(e^L−1))   [PAGE 14]

    NOT the "simplified" page-15 c(L)+w(L) that L1 used. See research/01
    reconciliation §3 Error 1 and §D `CCM-page-14-15-inconsistency`.
    """
    L = mpf(L)
    n = mpf(n)
    rho = lambda x: exp(x / 2) / (exp(x) - exp(-x))
    integrand = lambda x: (cos(2 * pi * n * x / L) - exp(-x / 2)) * rho(x)
    val = quad(integrand, [0, L])
    wL = (mpf(1) / 2) * (euler + log(4 * pi)) - (mpf(1) / 2) * log(
        (exp(L) + 1) / (exp(L) - 1)
    )
    return val + wL


def WR_diag_from_eq44(n, L):
    """GOLDEN REFERENCE: direct-from-eq(4.4) quadrature of W_R(V_n,V_n).

    Per research/01-reconciliation end-of-§3:
      W_R(V_n,V_n) = (γ_E + log(4π (e^L-1)/(e^L+1)))
                     + int_0^L [e^(x/2) · 2(1-x/L) cos(2π n x/L) - 2]
                               / (e^x - e^(-x)) dx
    This is algebraically independent of γ_L_fixed and β_L, so agreement
    between this and `2 γ_L_fixed(n) - 2 β_L(n)` at ≥ 40 digits is a
    cross-validation of the fix.
    """
    L = mpf(L)
    n = mpf(n)
    const = euler + log(4 * pi * (exp(L) - 1) / (exp(L) + 1))
    integrand = lambda x: (
        exp(x / 2) * 2 * (1 - x / L) * cos(2 * pi * n * x / L) - 2
    ) / (exp(x) - exp(-x))
    return const + quad(integrand, [0, L])


def build_QW_matrix(N, lam, verbose=True):
    """Assemble the full (2N+1)x(2N+1) symmetric matrix QW^N_λ.

    QW^N_λ = W_{0,2} − W_R − Σ_p W_p   (eq (3.10)/(3.19) of CCM-2025).
    """
    L = 2 * log(mpf(lam))
    lam_sq = mpf(lam) ** 2
    dim = 2 * N + 1
    indices = list(range(-N, N + 1))

    if verbose:
        print(f"    precomputing α/β/γ for |n| ≤ {N}...")
    t0 = time.time()
    alphas = {0: mpf(0)}
    betas = {}
    gammas = {}
    for n in range(N + 1):
        alphas[n] = alpha_L(n, L) if n != 0 else mpf(0)
        alphas[-n] = -alphas[n]
        betas[n] = beta_L(n, L)
        betas[-n] = betas[n]
        gammas[n] = gamma_L_fixed(n, L)
        gammas[-n] = gammas[n]
    if verbose:
        print(f"    α/β/γ done in {time.time()-t0:.1f}s")

    from sympy import primerange
    pp_list = []
    for p in primerange(2, int(lam_sq) + 2):
        pj = p
        while pj <= lam_sq:
            pp_list.append((pj, log(mpf(p))))
            pj *= p

    M = matrix(dim, dim)
    if verbose:
        print(f"    assembling {dim}x{dim} matrix, |pp|={len(pp_list)}...")
    t0 = time.time()
    for i, n in enumerate(indices):
        for j, m in enumerate(indices):
            if j < i:
                continue
            sh = (exp(L / 4) - exp(-L / 4)) / 2
            num = 32 * L * sh * sh * (L * L - 16 * pi * pi * mpf(n) * mpf(m))
            den = (L * L + 16 * pi * pi * mpf(m) * mpf(m)) * (
                L * L + 16 * pi * pi * mpf(n) * mpf(n)
            )
            w02 = num / den

            if n != m:
                w_r = (alphas[m] - alphas[n]) / (n - m)
            else:
                w_r = 2 * gammas[n] - 2 * betas[n]

            w_p = mpf(0)
            for (k, log_p) in pp_list:
                y = log(mpf(k))
                if n != m:
                    qval = (
                        sin(2 * pi * mpf(m) * y / L) - sin(2 * pi * mpf(n) * y / L)
                    ) / (pi * (n - m))
                else:
                    qval = 2 * (1 - y / L) * cos(2 * pi * mpf(n) * y / L)
                w_p += log_p / sqrt(mpf(k)) * qval

            entry = w02 - w_r - w_p
            M[i, j] = entry
            if i != j:
                M[j, i] = entry
    if verbose:
        print(f"    matrix assembly done in {time.time()-t0:.1f}s")
    return M


def even_subspace_matrix(M, N):
    dim_e = N + 1
    Me = matrix(dim_e, dim_e)

    def idx(n):
        return n + N

    for a in range(dim_e):
        for b in range(dim_e):
            if a == 0 and b == 0:
                Me[a, b] = M[idx(0), idx(0)]
            elif a == 0:
                Me[a, b] = (M[idx(0), idx(b)] + M[idx(0), idx(-b)]) / sqrt(mpf(2))
            elif b == 0:
                Me[a, b] = (M[idx(a), idx(0)] + M[idx(-a), idx(0)]) / sqrt(mpf(2))
            else:
                Me[a, b] = (
                    M[idx(a), idx(b)]
                    + M[idx(a), idx(-b)]
                    + M[idx(-a), idx(b)]
                    + M[idx(-a), idx(-b)]
                ) / 2
    return Me


def smallest_eigenpair(M_even):
    n = M_even.rows
    E, ER = eig(M_even, left=False, right=True)
    eigvals_real = [e.real for e in E]
    idx_min = min(range(n), key=lambda i: eigvals_real[i])
    eps_min = eigvals_real[idx_min]
    v = matrix(n, 1)
    for i in range(n):
        v[i, 0] = ER[i, idx_min].real
    s = sqrt(sum(v[i, 0] ** 2 for i in range(n)))
    for i in range(n):
        v[i, 0] /= s
    return eps_min, v


def expand_even_to_full(v_even, N):
    xi = [mpf(0)] * (2 * N + 1)
    xi[N] = v_even[0, 0]
    for k in range(1, N + 1):
        comp = v_even[k, 0] / sqrt(mpf(2))
        xi[N + k] = comp
        xi[N - k] = comp
    return xi


def find_D_double_prime_roots(xi_full, N):
    js = list(range(-N, N + 1))

    def f(s):
        total = mpf(0)
        for j_idx, j in enumerate(js):
            xi_j = xi_full[j_idx]
            if xi_j == 0:
                continue
            total += xi_j / (j - s)
        return total

    eps_supp = mpf(10) ** (-30)
    support = [js[i] for i in range(len(js)) if abs(xi_full[i]) > eps_supp]
    if not support:
        return []
    bracket_eps = mpf("1e-6")

    def manual_bisect(fl, lo, hi, max_iter=600, tol=mpf(10) ** (-120)):
        flo = fl(lo)
        fhi = fl(hi)
        if flo * fhi > 0:
            return None
        for _ in range(max_iter):
            mid = (lo + hi) / 2
            fm = fl(mid)
            if fm == 0 or (hi - lo) < tol:
                return mid
            if flo * fm < 0:
                hi = mid
                fhi = fm
            else:
                lo = mid
                flo = fm
        return (lo + hi) / 2

    roots = []
    for k in range(len(support) - 1):
        a = mpf(support[k]) + bracket_eps
        b = mpf(support[k + 1]) - bracket_eps
        try:
            r = manual_bisect(f, a, b)
            if r is not None:
                r = findroot(f, r, solver="secant")
                roots.append(r)
        except Exception:
            pass
    roots.sort()
    return roots


# ==========================================================================
# PART A.2 — Golden-reference cross-check of the fix at n=0..3
# ==========================================================================

def part_A2_golden_check():
    print("\n=" * 1)
    print("PART A.2 — Golden-reference check of fixed γ_L against direct-eq(4.4)")
    print("  (agreement ≥ 40 digits would confirm the fix)")
    L = 2 * log(mpf(4))  # the critical point (λ=4, N=30)
    for n in range(4):
        closed_form = 2 * gamma_L_fixed(n, L) - 2 * beta_L(n, L)
        direct = WR_diag_from_eq44(n, L)
        diff = abs(closed_form - direct)
        print(
            f"  n={n}:  (2γ_L-2β_L) = {nstr(closed_form, 15)}"
            f"   direct = {nstr(direct, 15)}"
            f"   |diff| = {nstr(diff, 4)}"
        )
    print()


# ==========================================================================
# PART A.4 — Main convergence grid + simplicity gaps
# ==========================================================================

def run_for_lambda(lam, N, num_zeros=10, report_gaps=True):
    L = 2 * log(mpf(lam))
    print(f"\n--- λ = {nstr(lam,8)}, N = {N}, L = {nstr(L,8)} ---")
    t0 = time.time()
    M = build_QW_matrix(N, lam, verbose=True)
    print(f"  built QW in {time.time()-t0:.1f}s")

    Me = even_subspace_matrix(M, N)
    t0 = time.time()
    E_all = eig(Me, left=False, right=False)
    eigs_even_sorted = sorted([e.real for e in E_all])
    print(f"  even-sector diag in {time.time()-t0:.1f}s, dim={N+1}")
    print(f"  smallest 5 even eigenvalues:")
    for k in range(min(5, len(eigs_even_sorted))):
        print(f"     μ_{k} = {nstr(eigs_even_sorted[k], 12)}")
    if report_gaps and len(eigs_even_sorted) >= 4:
        g1 = eigs_even_sorted[1] - eigs_even_sorted[0]
        g2 = eigs_even_sorted[2] - eigs_even_sorted[1]
        g3 = eigs_even_sorted[3] - eigs_even_sorted[2]
        print(f"  gaps:  μ_1-μ_0 = {nstr(g1, 6)}")
        print(f"         μ_2-μ_1 = {nstr(g2, 6)}")
        print(f"         μ_3-μ_2 = {nstr(g3, 6)}")
        # At dps=200 the floor is ~10^-200. Anything above 10^-50 is real.
        thr = mpf(10) ** (-50)
        print(
            f"  simplicity-gap test (threshold 10^-50): μ_1-μ_0 "
            f"{'>' if g1 > thr else '<='} 10^-50"
        )

    eps_min, v_even = smallest_eigenpair(Me)
    xi_full = expand_even_to_full(v_even, N)

    t0 = time.time()
    s_roots = find_D_double_prime_roots(xi_full, N)
    print(f"  found {len(s_roots)} s-roots in {time.time()-t0:.1f}s")

    eigs = [(2 * pi / L) * s for s in s_roots]
    pos_eigs = sorted([e for e in eigs if e > 0], key=lambda x: float(x))

    print(f"\n  k    D(λ,N) eigenvalue              γ_k                         |diff|")
    diffs = []
    for k in range(1, num_zeros + 1):
        if k - 1 >= len(pos_eigs):
            break
        eig_k = pos_eigs[k - 1]
        gamma_k = zetazero(k).imag
        diff = abs(eig_k - gamma_k)
        diffs.append(diff)
        print(
            f"  {k:2d}   {nstr(eig_k, 22)}   {nstr(gamma_k, 22)}   {nstr(diff, 4)}"
        )
    return diffs, eps_min, eigs_even_sorted


if __name__ == "__main__":
    print(f"mp.dps = {mp.dps}  (declared {PRECISION_DECLARED})")
    print("Lead 5 verification: FIXED γ_L, high precision, full grid\n")

    # PART A.2 — Golden check
    part_A2_golden_check()

    # PART A.4 — main grid
    print("\n=" * 1)
    print("PART A.4 — main convergence grid")
    schedule = [
        (mpf("2"), 30),
        (mpf("3"), 30),
        (mpf("4"), 30),
        (mpf("4"), 50),
        (mpf("8"), 30),
    ]
    results = {}
    for lam, N in schedule:
        try:
            diffs, eps, eigs_even = run_for_lambda(lam, N, num_zeros=10)
            results[(float(lam), N)] = (diffs, eps, eigs_even)
        except Exception as e:
            print(f"  EXCEPTION at (λ={float(lam)}, N={N}): {type(e).__name__}: {e}")

    print("\n\n========== SUMMARY (PART A.4) ==========")
    print(f"{'λ':>6}  {'N':>4}  {'eps_min':>18}  ", end="")
    for k in range(1, 11):
        print(f"  |Δγ_{k}|  ", end="")
    print()
    for (lam, N), (diffs, eps, _) in results.items():
        print(f"{lam:>6.3f}  {N:>4}  {float(eps):>18.6e}  ", end="")
        for d in diffs:
            print(f"  {float(d):8.2e}", end="")
        print()

    # PART A.5 — decay-rate fit for |γ_1 − eig_1(λ)| vs λ²
    print("\n=" * 1)
    print("PART A.5 — decay rate: log|γ_1 − eig_1(λ)| vs λ² for λ∈{2..8}, N=30")
    decay_lams = [mpf(k) for k in (2, 3, 4, 5, 6, 7, 8)]
    decay_pts = []
    for lam in decay_lams:
        try:
            diffs, eps, _ = run_for_lambda(lam, 30, num_zeros=2, report_gaps=False)
            if len(diffs) >= 1:
                err = diffs[0]
                if err > 0:
                    log_err = log(err)
                    lam_sq = lam * lam
                    decay_pts.append((float(lam_sq), float(log_err), float(err)))
                    print(f"  λ={float(lam)}  λ²={float(lam_sq)}  "
                          f"|γ_1-eig_1|={float(err):.3e}  log|err|={float(log_err):.3f}")
        except Exception as e:
            print(f"  EXCEPTION at λ={float(lam)}: {e}")

    if len(decay_pts) >= 2:
        xs = [p[0] for p in decay_pts]
        ys = [p[1] for p in decay_pts]
        n = len(xs)
        mx = sum(xs) / n
        my = sum(ys) / n
        num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
        den = sum((xs[i] - mx) ** 2 for i in range(n))
        slope = num / den
        intercept = my - slope * mx
        print(f"\n  LEAST-SQUARES FIT: log|γ_1 − eig_1(λ)| ≈ {slope:.4f} * λ² + {intercept:.4f}")
        print(f"  (Cycle 1 L1 Adversary reported slope ≈ -3.37; L1 executor had reported -4.5.)")
