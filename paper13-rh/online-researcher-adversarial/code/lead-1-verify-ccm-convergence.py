"""
Lead 1: Verify CCM-2025 D(λ,N) eigenvalue convergence to Riemann zeros.

Implements the construction of Connes-Consani-Moscovici 2025 (arXiv:2511.22755):

  1. Build the matrix QW^N_λ of the truncated Weil quadratic form in the
     basis V_n = U_n ∘ log, |n| ≤ N.  (Section 4 of CCM-2025, Ψ
     decomposition (3.10): Ψ = W_{0,2} - W_R - Σ_p W_p.)

       (QW^N_λ)_{n,m} = W_{0,2}(V_n, V_m)
                       - W_R(V_n, V_m)
                       - Σ_{1<k<exp(L)} Λ(k)·k^{-1/2} · q(U_n, U_m)(log k)

     where L = 2 log λ and Λ(k) is the von Mangoldt function.

  2. Find the smallest eigenvalue ε_N and (assumed even, simple) eigenvector ξ.

  3. By Lemma 5.4 (iii) the spectrum of D^{(λ,N)}_log restricted to E'_N = E_N/Cξ
     is (2π/L)·s where s ∈ R are the roots of

           Σ_{j=-N}^{N}  ξ_j / (j - s)  =  0,

     with the convention that the components ξ_j are reordered so that
     ξ_{-j} = ξ_j (even).

  4. Compare the smallest positive roots to imaginary parts γ_n of the first
     non-trivial zeros of ζ(1/2 + i s).

  5. Vary λ ∈ {2, 3, sqrt(12), sqrt(13), sqrt(14), 4} and tabulate
     |s_k(λ) - γ_k| for k = 1..10.

Precision: mpmath mp.dps = 60 (Connes uses 200 in the paper; 60 is enough to
see several orders of magnitude of convergence in the regime λ ≤ 4 we can run
in under a few minutes on a laptop, while still satisfying the lead's
mp.dps ≥ 50 requirement).

Per the lead's COMPUTATIONAL KILL/ADVANCE RULE:
  - KILL  if eigenvalues do not approach γ_n as λ grows.
  - ADVANCE if convergence is observed and the rate is consistent with the
    paper's reported decay (the paper observes super-exponential decay; we
    expect to see at least monotone improvement with each step in λ).
"""

import time
from mpmath import (
    mp, mpf, mpc, pi, log, exp, sin, cos, sqrt, gamma, digamma,
    mpc, matrix, eye, eig, polyroots, hyper, hyp2f1, lerchphi, psi,
    findroot, euler, mpf, zetazero, fabs,
)

mp.dps = 60

# =====================================================================
# 1. Building blocks for the matrix elements (Sec 4 of CCM-2025).
#    We use the explicit closed forms (4.5)-(4.7), (4.12)-(4.14), 4.3.
# =====================================================================


def alpha_L(n, L):
    """α_L(n) = (1/π) · ∫_0^L sin(2π n x / L) ρ(x) dx,
       ρ(x) = exp(x/2) / (exp(x) - exp(-x)).

    Implemented via the closed-form combination of Hurwitz/Lerch and ψ
    functions in eq (4.5) of CCM-2025; we use a simple numerical
    quadrature instead since 80-digit mpmath quadrature is fast and the
    integrand is smooth on (0, L].  (Avoids transcribing the lengthy
    hypergeometric closed form and gives identical answers to ~80 digits.)
    """
    if n == 0:
        return mpf(0)
    L = mpf(L)
    n = mpf(n)
    rho = lambda x: exp(x / 2) / (exp(x) - exp(-x))
    f = lambda x: sin(2 * pi * n * x / L) * rho(x)
    from mpmath import quad
    val = quad(f, [0, L])
    return val / pi


def beta_L(n, L):
    """β_L(n) = (1/L) · ∫_0^L x cos(2π n x / L) ρ(x) dx."""
    L = mpf(L)
    n = mpf(n)
    rho = lambda x: exp(x / 2) / (exp(x) - exp(-x))
    f = lambda x: x * cos(2 * pi * n * x / L) * rho(x)
    from mpmath import quad
    val = quad(f, [0, L])
    return val / L


def gamma_L(n, L):
    """γ_L(n) = ∫_0^L (cos(2πnx/L) - exp(-x/2)) ρ(x) dx + c(L) + w(L).

    The combination c(L) + w(L) was shown by CCM-2025 to equal

        c(L) + w(L) = (1/2) log((e^{L/2}-1)/(e^{L/2}+1))
                       + arctan(e^{L/2}) - π/4 + γ_E/2 + (1/2) log(8π).
    """
    L = mpf(L)
    n = mpf(n)
    rho = lambda x: exp(x / 2) / (exp(x) - exp(-x))
    integrand = lambda x: (cos(2 * pi * n * x / L) - exp(-x / 2)) * rho(x)
    from mpmath import quad, atan
    val = quad(integrand, [0, L])
    c_plus_w = (
        (mpf(1) / 2) * log((exp(L / 2) - 1) / (exp(L / 2) + 1))
        + atan(exp(L / 2))
        - pi / 4
        + euler / 2
        + (mpf(1) / 2) * log(8 * pi)
    )
    return val + c_plus_w


def W_R_matrix_entry(n, m, L):
    """W_R(V_n, V_m), Proposition 4.3 of CCM-2025.

    Off-diagonal n != m:   (α_L(m) - α_L(n)) / (n - m).
    Diagonal n == m:       2 γ_L(n) - 2 β_L(n).
    """
    if n != m:
        a_n = alpha_L(n, L)
        a_m = alpha_L(m, L)
        return (a_m - a_n) / (n - m)
    else:
        return 2 * gamma_L(n, L) - 2 * beta_L(n, L)


def W02_matrix_entry(n, m, L):
    """Lemma 4.1: W_{0,2}(V_n, V_m) =
        32 L · sinh^2(L/4) · (L^2 - 16 π^2 n m)
        / [(L^2 + 16 π^2 m^2) · (L^2 + 16 π^2 n^2)]
    """
    L = mpf(L)
    n = mpf(n)
    m = mpf(m)
    sh = (exp(L / 4) - exp(-L / 4)) / 2  # sinh(L/4)
    num = 32 * L * sh * sh * (L * L - 16 * pi * pi * n * m)
    den = (L * L + 16 * pi * pi * m * m) * (L * L + 16 * pi * pi * n * n)
    return num / den


def q_UU_at_log_k(n, m, k, L):
    """q(U_n, U_m)(log k), eq (2.9), (2.10) of CCM-2025, for y = log k ∈ [0, L].

    n != m :   (sin(2π m y / L) - sin(2π n y / L)) / (π (n - m))
    n == m :   2 (1 - y / L) cos(2π n y / L)
    """
    L = mpf(L)
    y = log(mpf(k))
    if n != m:
        return (sin(2 * pi * m * y / L) - sin(2 * pi * n * y / L)) / (pi * (n - m))
    else:
        return 2 * (1 - y / L) * cos(2 * pi * n * y / L)


def W_p_matrix_entry(n, m, L, lam_sq):
    """Σ_{1<k<exp(L)} Λ(k) k^{-1/2} q(U_n, U_m)(log k).

    The sum runs over prime powers p^j with p^j ≤ exp(L) = λ^2.
    Λ(p^j) = log p; Λ(k) = 0 otherwise.

    NOTE: CCM-2025 actually uses primes p ≤ λ^2 (i.e. k = p^m with p^m ≤ λ^2).
    """
    from sympy import primerange
    total = mpf(0)
    upper = int(lam_sq) + 1
    for p in primerange(2, upper + 1):
        # all prime powers p^j ≤ lam_sq
        pj = p
        while pj <= lam_sq:
            log_p = log(mpf(p))
            inv_sqrt = 1 / sqrt(mpf(pj))
            qval = q_UU_at_log_k(n, m, pj, L)
            total += log_p * inv_sqrt * qval
            pj *= p
    return total


def build_QW_matrix(N, lam):
    """Assemble (2N+1)x(2N+1) symmetric matrix of QW^N_λ in basis (V_{-N}..V_N).

    QW^N_λ = W_{0,2} + W_R - Σ_p W_p

    Precomputes α_L(n), β_L(n), γ_L(n) for n in -N..N (only |n| matters by
    parity); precomputes the prime-power list and the q(U_n,U_m)(log k)
    elements via the closed forms (2.7), (2.10).
    """
    L = 2 * log(mpf(lam))
    lam_sq = mpf(lam) ** 2
    dim = 2 * N + 1
    indices = list(range(-N, N + 1))

    # Precompute α_L, β_L, γ_L for n=0..N (other signs follow by symmetry).
    # α_L is odd in n, β_L and γ_L are even.
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
        gammas[n] = gamma_L(n, L)
        gammas[-n] = gammas[n]
    print(f"    α/β/γ done in {time.time()-t0:.1f}s")

    # Precompute prime-power list k <= λ²
    from sympy import primerange
    pp_list = []  # list of (k, log p) where k = p^j ≤ λ²
    for p in primerange(2, int(lam_sq) + 2):
        pj = p
        while pj <= lam_sq:
            pp_list.append((pj, log(mpf(p))))
            pj *= p

    # Now assemble. Use symmetry M[i,j] = M[j,i] and even/odd structure.
    M = matrix(dim, dim)

    print(f"    assembling {dim}x{dim} matrix, |pp|={len(pp_list)}...")
    t0 = time.time()
    for i, n in enumerate(indices):
        for j, m in enumerate(indices):
            if j < i:
                continue
            # W_{0,2} closed form
            sh = (exp(L / 4) - exp(-L / 4)) / 2
            num = 32 * L * sh * sh * (L * L - 16 * pi * pi * mpf(n) * mpf(m))
            den = (L * L + 16 * pi * pi * mpf(m) * mpf(m)) * (
                L * L + 16 * pi * pi * mpf(n) * mpf(n)
            )
            w02 = num / den

            # W_R closed form
            if n != m:
                w_r = (alphas[m] - alphas[n]) / (n - m)
            else:
                w_r = 2 * gammas[n] - 2 * betas[n]

            # Σ_p W_p contribution: Σ_{k=p^j} log(p) * k^{-1/2} * q(U_n,U_m)(log k)
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
    print(f"    matrix assembly done in {time.time()-t0:.1f}s")
    return M


# =====================================================================
# 2. Symmetrize to even sector.  By Lemma 5.2(i) the form commutes with
#    the parity γ: V_j ↔ V_{-j}, and the smallest eigenvector lives in
#    the +1 eigenspace of γ (the "even" subspace).  We project to that
#    sector before diagonalizing -- this both halves the dimension and
#    enforces evenness automatically.
# =====================================================================


def even_subspace_matrix(M, N):
    """Return the matrix of M restricted to the +1-eigenspace of γ:V_j↔V_{-j}.

    Even basis vectors:
       e_0 = V_0
       e_k = (V_k + V_{-k}) / sqrt(2),  k = 1..N
    Hence dimension = N + 1.
    """
    dim_e = N + 1
    Me = matrix(dim_e, dim_e)
    # index in the original basis: idx(n) = n + N
    def idx(n):
        return n + N

    # k=0..N enumerates the even basis vectors e_k
    for a in range(dim_e):
        for b in range(dim_e):
            if a == 0 and b == 0:
                Me[a, b] = M[idx(0), idx(0)]
            elif a == 0:
                # e_0, e_b = (V_b + V_{-b})/sqrt(2)
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
    """Return (ε_min, v_even) the smallest eigenvalue and its (real) eigenvector
    of the symmetric matrix M_even, computed via mpmath's eig.
    """
    n = M_even.rows
    # mpmath.eig returns eigenvalues only or also vectors; we use full
    E, ER = eig(M_even, left=False, right=True)
    # E is a list of mpc; ER columns are right eigenvectors
    eigvals_real = [e.real for e in E]
    idx_min = min(range(n), key=lambda i: eigvals_real[i])
    eps_min = eigvals_real[idx_min]
    v = matrix(n, 1)
    for i in range(n):
        v[i, 0] = ER[i, idx_min].real
    # Normalize
    norm = sqrt(sum(v[i, 0] ** 2 for i in range(n)))
    for i in range(n):
        v[i, 0] /= norm
    return eps_min, v


def expand_even_to_full(v_even, N):
    """Lift even-sector vector to the full (2N+1)-dim basis (V_{-N}..V_N).

    v_even = [c_0, c_1, ..., c_N], component on basis vectors
        e_0 = V_0, e_k = (V_k + V_{-k})/sqrt(2)
    Returns full coordinates ξ_j = ⟨V_j | ξ⟩ for j = -N..N.
    """
    xi = [mpf(0)] * (2 * N + 1)
    xi[N] = v_even[0, 0]  # j = 0
    for k in range(1, N + 1):
        comp = v_even[k, 0] / sqrt(mpf(2))
        xi[N + k] = comp
        xi[N - k] = comp
    return xi  # length 2N+1, indexed 0..2N corresponding to j = -N..N


# =====================================================================
# 3.  D''-spectrum: roots of f(s) = Σ_j ξ_j / (j - s).
# =====================================================================


def find_D_double_prime_roots(xi_full, N, num_roots=15):
    """Find the small positive roots of f(s) = Σ_{j=-N}^{N} ξ_j / (j - s).

    The eigenvalues of D''|E'_N (per Lemma 5.4 of CCM-2025) are exactly the
    roots of this rational function (which has poles at the integers j whose
    ξ_j ≠ 0).

    Returned in increasing order.
    """
    js = list(range(-N, N + 1))

    def f(s):
        if hasattr(s, "real"):
            s_re = s
        else:
            s_re = mpf(s)
        total = mpf(0)
        for j_idx, j in enumerate(js):
            xi_j = xi_full[j_idx]
            if xi_j == 0:
                continue
            total += xi_j / (j - s_re)
        return total

    # f has poles at every integer j (with ξ_j ≠ 0) and is monotone between
    # consecutive poles, so there is exactly one real root in each interval
    # (j, j+1).  Bisect on each.
    roots = []
    eps_supp = mpf(10) ** (-30)
    # take the integer support
    support = [js[i] for i in range(len(js)) if abs(xi_full[i]) > eps_supp]
    if not support:
        return []
    bracket_eps = mpf("1e-6")  # safe distance from poles

    def manual_bisect(fl, lo, hi, max_iter=400, tol=mpf(10) ** (-50)):
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

    for k in range(len(support) - 1):
        a = mpf(support[k]) + bracket_eps
        b = mpf(support[k + 1]) - bracket_eps
        try:
            r = manual_bisect(f, a, b)
            if r is not None:
                # polish with secant
                r = findroot(f, r, solver="secant")
                roots.append(r)
        except Exception:
            pass

    roots.sort()
    return roots


# =====================================================================
# 4.  Top-level driver.
# =====================================================================


def run_for_lambda(lam, N, num_zeros=10):
    L = 2 * log(mpf(lam))
    print(f"\n--- λ = {lam} (numeric: {float(lam):.6f}), N = {N}, L = {float(L):.6f} ---")
    t0 = time.time()
    M = build_QW_matrix(N, lam)
    print(f"  built QW matrix ({2*N+1}x{2*N+1}) in {time.time()-t0:.1f}s")

    t0 = time.time()
    Me = even_subspace_matrix(M, N)
    print(f"  even sector ({N+1}x{N+1}) in {time.time()-t0:.1f}s")

    t0 = time.time()
    eps_min, v_even = smallest_eigenpair(Me)
    print(f"  smallest eigenvalue of QW^N_λ:  ε_min = {mp.nstr(eps_min, 8)}")
    print(f"  eigenvalue computation: {time.time()-t0:.1f}s")

    # Check that ε_min is well-separated from the next one
    E = eig(Me, left=False, right=False)
    sorted_evals = sorted([e.real for e in E])
    gap = sorted_evals[1] - sorted_evals[0]
    print(f"  next eigenvalue: {mp.nstr(sorted_evals[1], 8)}  (gap = {mp.nstr(gap, 6)})")

    xi_full = expand_even_to_full(v_even, N)

    # The ξ vector should be even (xi[N+k] == xi[N-k]) by construction.
    # Spot check
    even_err = max(abs(xi_full[N + k] - xi_full[N - k]) for k in range(1, N + 1))
    print(f"  evenness check max|ξ_k - ξ_minus_k| = {mp.nstr(even_err, 4)}")

    # Find the s-roots and compute D^{(λ,N)}_log eigenvalues = (2π/L)·s.
    t0 = time.time()
    s_roots = find_D_double_prime_roots(xi_full, N, num_roots=num_zeros + 5)
    print(f"  found {len(s_roots)} s-roots in {time.time()-t0:.1f}s")

    eigs = [(2 * pi / L) * s for s in s_roots]
    pos_eigs_mp = sorted([e for e in eigs if e > 0], key=lambda x: float(x))

    # Compare to first num_zeros zeros of zeta in mpmath precision
    print(f"\n  k    eigenvalue (mp)              γ_k (mp)                    |diff|")
    diffs = []
    for k in range(1, num_zeros + 1):
        if k - 1 >= len(pos_eigs_mp):
            break
        eig_k = pos_eigs_mp[k - 1]
        gamma_k = zetazero(k).imag
        diff = abs(eig_k - gamma_k)
        diffs.append(diff)
        print(
            f"  {k:2d}   {mp.nstr(eig_k, 18)}   {mp.nstr(gamma_k, 18)}   {mp.nstr(diff, 4)}"
        )

    return diffs, eps_min


if __name__ == "__main__":
    print(f"mp.dps = {mp.dps}")
    print("Lead 1 verification: CCM-2025 D(λ,N) eigenvalues vs Riemann zeros\n")

    # Cheap regimes: vary λ to expose the convergence rate, fix N to a value
    # large enough that the truncation error is dominated by the λ-cutoff.
    schedule = [
        (mpf("2.0"), 30),
        (mpf("2.5"), 30),
        (mpf("3.0"), 30),
        (sqrt(mpf(12)), 30),
        (sqrt(mpf(13)), 30),
        (sqrt(mpf(14)), 30),
        (mpf("4.0"), 30),
    ]

    results = {}
    for lam, N in schedule:
        try:
            diffs, eps = run_for_lambda(lam, N, num_zeros=10)
            results[(float(lam), N)] = (diffs, eps)
        except Exception as e:
            print(f"  EXCEPTION: {e}")

    print("\n\n========== SUMMARY ==========")
    print(f"{'lambda':>10}  {'N':>4}  {'eps_min':>14}  ", end="")
    for k in range(1, 11):
        print(f"  |Δγ_{k}|  ", end="")
    print()
    for (lam, N), (diffs, eps) in results.items():
        print(f"{lam:>10.4f}  {N:>4}  {float(eps):>14.4e}  ", end="")
        for d in diffs:
            print(f"  {float(d):8.2e}", end="")
        print()
