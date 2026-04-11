"""
Lead 8: Rebuild of L2's CF-even-simple verification from scratch.

PRECISION DECLARATION (Round 003 e.3):
    mp.dps = 200.
    Justification: The reconciliation note (research/01) and the Cycle-2
    benchmark show that at (λ=4, N=30) the smallest eigenvalue of the
    corrected QW^N_λ matrix is O(1e-53) and the first simplicity gap
    μ_1 − μ_0 is O(1e-47). dps=60 (Cycle-1 L2) is numerically below
    this floor. dps=200 gives ~150 digits of headroom above even the
    smallest tested quantity, matching CCM-2025's own precision.

This script rebuilds lead-2-verify-cf-even-simple.py by applying the
two-line matrix fix from research/01-reconciliation-L1-L2-matrix.md:

  (i)  γ_L(n) uses w(L) ALONE, not c(L)+w(L). Integrand is
       (cos(2πnx/L) − e^(−x/2)) · ρ(x); reference: CCM-2025 page 14
       eqs (4.11) and (4.14) (the page-14 form, NOT the "simplified"
       page-15 form; the two are inconsistent by a constant — see §D
       `CCM-page-14-15-inconsistency`).

  (ii) W_R off-diagonal sign is /(n − m), per CCM-2025 Proposition 4.3
       page 15 (NOT /(m − n)).

Sanity checks implemented:
  - real entries, symmetry, γ-commutation, Toeplitz/CF form
    (CCM Lemma 5.1): τ_{i,j} = (b_i − b_j)/(i − j) for i ≠ j,
    with a_{−n} = a_n and b_{−n} = −b_n.
  - golden-reference cross-check of the diagonal W_R(V_n, V_n)
    against direct quadrature of CCM eq (4.4), i.e.
      W_R(V_n, V_n) = (γ_E + log(4π(e^L − 1)/(e^L + 1)))
                    + ∫₀^L [e^(x/2) · 2(1 − x/L) cos(2π n x/L) − 2]
                           / (e^x − e^(−x)) dx
    which is algebraically independent of α_L, β_L, γ_L closed forms.
  - cross-check of my matrix entries against Lead 5's matrix at the
    shared canonical point (λ=4, N=30). Round 003 d.2.
"""

import time
import sys
from mpmath import (
    mp, mpf, pi, log, exp, sin, cos, sqrt, matrix, eig, euler, quad, nstr,
)

mp.dps = 200
PRECISION_DECLARED = 200

# ============================================================================
# §1. Closed-form building blocks (CCM-2025 §4).
# ============================================================================


def rho_integrand_factor(x):
    """ρ(x) = exp(x/2) / (exp(x) − exp(−x))."""
    return exp(x / 2) / (exp(x) - exp(-x))


def alpha_of_L(n, L):
    """α_L(n) = (1/π) ∫_0^L sin(2π n x / L) ρ(x) dx,   odd in n, α_L(0) = 0.
    Ref: CCM-2025 eq (4.12). Evaluated by mpmath adaptive quadrature
    (agrees with the closed form (4.5) to dps).
    """
    if n == 0:
        return mpf(0)
    L = mpf(L)
    n = mpf(n)
    integrand = lambda x: sin(2 * pi * n * x / L) * rho_integrand_factor(x)
    return quad(integrand, [0, L]) / pi


def beta_of_L(n, L):
    """β_L(n) = (1/L) ∫_0^L x cos(2π n x / L) ρ(x) dx.
    Ref: CCM-2025 eq (4.13). Even in n.
    """
    L = mpf(L)
    n = mpf(n)
    integrand = lambda x: x * cos(2 * pi * n * x / L) * rho_integrand_factor(x)
    return quad(integrand, [0, L]) / L


def w_correction(L):
    """w(L) = (1/2)(γ_E + log(4π)) − (1/2) log((e^L + 1)/(e^L − 1)).
    CCM-2025 page 14 (unnumbered display between eqs (4.11) and (4.14)).
    This is the CORRECT additive constant per research/01-reconciliation.
    """
    L = mpf(L)
    return (mpf(1) / 2) * (euler + log(4 * pi)) - (mpf(1) / 2) * log(
        (exp(L) + 1) / (exp(L) - 1)
    )


def gamma_of_L(n, L):
    """γ_L(n) = ∫_0^L (cos(2πnx/L) − exp(−x/2)) ρ(x) dx + w(L).

    *** REBUILD FIX ***: the page-14 integrand is (cos − exp(−x/2))
    (eq 4.11/4.14), NOT (cos − 1). The additive constant is w(L) ALONE,
    NOT c(L) + w(L). See research/01-reconciliation §3 Error 1.
    Ref: CCM-2025 page 14 eqs (4.11)/(4.14) + `CCM-page-14-15-inconsistency`.
    """
    L = mpf(L)
    n = mpf(n)
    integrand = lambda x: (
        (cos(2 * pi * n * x / L) - exp(-x / 2)) * rho_integrand_factor(x)
    )
    val = quad(integrand, [0, L])
    return val + w_correction(L)


def W02_entry(n, m, L):
    """Lemma 4.1: W_{0,2}(V_n, V_m) closed form.

      W_{0,2}(V_n, V_m) =
          32 L sinh²(L/4) · (L² − 16 π² n m)
        / [(L² + 16 π² m²) · (L² + 16 π² n²)]
    """
    L = mpf(L)
    n = mpf(n)
    m = mpf(m)
    sh = (exp(L / 4) - exp(-L / 4)) / 2
    num = 32 * L * sh * sh * (L * L - 16 * pi * pi * n * m)
    den = (L * L + 16 * pi * pi * m * m) * (L * L + 16 * pi * pi * n * n)
    return num / den


def WR_entry(n, m, alphas, betas, gammas):
    """W_R(V_n, V_m), Proposition 4.3 of CCM-2025 page 15.

    *** REBUILD FIX ***: off-diagonal denominator is (n − m),
    NOT (m − n) as in the buggy Cycle-1 L2 script.
    """
    if n != m:
        return (alphas[m] - alphas[n]) / (n - m)
    else:
        return 2 * gammas[n] - 2 * betas[n]


def WR_diag_from_eq44(n, L):
    """GOLDEN REFERENCE — direct quadrature of W_R(V_n,V_n) from CCM eq (4.4).

    Algebraically independent of the α/β/γ closed-form path.
    Purpose: cross-check the γ_L fix at n = 0, 1, 2, 3, 5, 10.
    """
    L = mpf(L)
    n = mpf(n)
    const_term = euler + log(4 * pi * (exp(L) - 1) / (exp(L) + 1))
    integrand = lambda x: (
        exp(x / 2) * 2 * (1 - x / L) * cos(2 * pi * n * x / L) - 2
    ) / (exp(x) - exp(-x))
    return const_term + quad(integrand, [0, L])


def q_UU_at_y(n, m, y, L):
    """q(U_n, U_m)(y) per CCM eqs (2.9)/(2.10) and Lemma 2.3.

    n != m: (sin(2π m y / L) − sin(2π n y / L)) / (π (n − m))
    n == m: 2 (1 − y/L) cos(2 π n y / L)
    """
    L = mpf(L)
    y = mpf(y)
    n = mpf(n)
    m = mpf(m)
    if n != m:
        return (sin(2 * pi * m * y / L) - sin(2 * pi * n * y / L)) / (pi * (n - m))
    else:
        return 2 * (1 - y / L) * cos(2 * pi * n * y / L)


def prime_power_list(lam_sq):
    """(p^j, log p) pairs for all prime powers p^j ≤ λ²."""
    from sympy import primerange
    out = []
    upper = int(lam_sq) + 2
    for p in primerange(2, upper):
        pj = p
        while pj <= lam_sq:
            out.append((pj, log(mpf(p))))
            pj *= p
    return out


# ============================================================================
# §2. Matrix assembly (CCM-2025 eqs (3.10)/(3.19)).
# ============================================================================


def build_QW_matrix_rebuild(N, lam, verbose=False):
    """Build QW^N_λ = W_{0,2} − W_R − Σ_p W_p, full (2N+1)x(2N+1) form.

    Independent implementation of the same object as Lead 5's script.
    """
    L = 2 * log(mpf(lam))
    lam_sq = mpf(lam) ** 2
    dim = 2 * N + 1
    idx = lambda n: n + N  # map n ∈ [-N,N] to row/col ∈ [0, 2N]

    # Precompute α/β/γ with parity
    if verbose:
        print(f"  [rebuild] precomputing α/β/γ for |n| ≤ {N} ...")
    t0 = time.time()
    alphas = {}
    betas = {}
    gammas = {}
    alphas[0] = mpf(0)
    for n in range(1, N + 1):
        alphas[n] = alpha_of_L(n, L)
        alphas[-n] = -alphas[n]
    for n in range(N + 1):
        betas[n] = beta_of_L(n, L)
        betas[-n] = betas[n]
        gammas[n] = gamma_of_L(n, L)
        gammas[-n] = gammas[n]
    if verbose:
        print(f"  [rebuild] α/β/γ done in {time.time()-t0:.1f}s")

    pp = prime_power_list(lam_sq)
    if verbose:
        print(f"  [rebuild] {len(pp)} prime powers ≤ λ² = {float(lam_sq)}")

    T = matrix(dim, dim)
    t0 = time.time()
    for n in range(-N, N + 1):
        for m in range(n, N + 1):  # upper triangle + diag
            w02 = W02_entry(n, m, L)
            wr = WR_entry(n, m, alphas, betas, gammas)
            # Σ_p W_p
            wp = mpf(0)
            for (k, logp) in pp:
                y = log(mpf(k))
                qv = q_UU_at_y(n, m, y, L)
                wp += logp / sqrt(mpf(k)) * qv
            entry = w02 - wr - wp
            T[idx(n), idx(m)] = entry
            if n != m:
                T[idx(m), idx(n)] = entry
    if verbose:
        print(f"  [rebuild] matrix assembly done in {time.time()-t0:.1f}s")
    return T


def even_sector_matrix(T, N):
    """Restrict to the +1 eigenspace of γ : V_n ↔ V_{−n}.
    Even basis: e_0 = V_0; e_k = (V_k + V_{−k})/√2 for k = 1..N.
    """
    d = N + 1
    Me = matrix(d, d)

    def I(n):
        return n + N

    for a in range(d):
        for b in range(d):
            if a == 0 and b == 0:
                Me[a, b] = T[I(0), I(0)]
            elif a == 0:
                Me[a, b] = (T[I(0), I(b)] + T[I(0), I(-b)]) / sqrt(mpf(2))
            elif b == 0:
                Me[a, b] = (T[I(a), I(0)] + T[I(-a), I(0)]) / sqrt(mpf(2))
            else:
                Me[a, b] = (
                    T[I(a), I(b)] + T[I(a), I(-b)] + T[I(-a), I(b)] + T[I(-a), I(-b)]
                ) / 2
    return Me


# ============================================================================
# §3. Sanity checks against CCM Lemma 5.1.
# ============================================================================


def sanity_check(T, N, label=""):
    """Verify: real, symmetric, γ-commuting, CF/Toeplitz form.

    CCM Lemma 5.1 structural properties:
        τ_{i,i} = a_i    (even in i)
        τ_{i,j} = (b_i − b_j) / (i − j)    (b odd)
    where the basis is indexed by j ∈ [−N, N] and γ acts as j ↔ −j.

    The CF structure holds only up to the diagonal and only for entries
    that come ENTIRELY from the W_R block; W_{0,2} and Σ_p W_p are NOT
    of CF form individually, but their SUM with −W_R gives the full
    matrix τ and CCM Lemma 5.1 claims that the FULL matrix τ has the
    CF form τ_{i,j} = (b_i − b_j)/(i − j) for i ≠ j with b_n given in
    eq (5.2)/(5.3).
    """
    d = 2 * N + 1
    # 1. Real
    max_imag = mpf(0)
    for i in range(d):
        for j in range(d):
            v = T[i, j]
            if hasattr(v, "imag"):
                if abs(v.imag) > max_imag:
                    max_imag = abs(v.imag)
    # 2. Symmetric
    max_sym = mpf(0)
    for i in range(d):
        for j in range(d):
            e = abs(T[i, j] - T[j, i])
            if e > max_sym:
                max_sym = e
    # 3. γ-commuting: T[i, j] = T[2N-i, 2N-j]
    max_gam = mpf(0)
    for i in range(d):
        for j in range(d):
            e = abs(T[i, j] - T[d - 1 - i, d - 1 - j])
            if e > max_gam:
                max_gam = e
    # 4. CF/Toeplitz form: τ_{i,j} (i != j) = (b_i − b_j)/(i − j)
    #    with b_n = −(i − j) τ_{i,j} for any reference (i, j).
    #    Method: pick b from the n=0 row: b_n := −n · τ_{N, N+n} + const.
    #    Actually, use the well-known extraction: define
    #        b_n − b_0 = n · τ_{idx(0), idx(n)}   for n ≠ 0
    #    then check τ_{idx(i), idx(j)} (i ≠ j, both ≠ 0) equals
    #    ((b_i − b_0) − (b_j − b_0)) / (i − j).
    idx = lambda n: n + N
    b_shift = {0: mpf(0)}
    for n in range(-N, N + 1):
        if n != 0:
            b_shift[n] = n * T[idx(0), idx(n)]
    max_cf = mpf(0)
    for i in range(-N, N + 1):
        for j in range(-N, N + 1):
            if i == j or i == 0 or j == 0:
                continue
            pred = (b_shift[i] - b_shift[j]) / (i - j)
            err = abs(T[idx(i), idx(j)] - pred)
            if err > max_cf:
                max_cf = err
    # 5. b_n odd: b_shift[−n] = −b_shift[n]
    max_bodd = mpf(0)
    for n in range(1, N + 1):
        e = abs(b_shift[n] + b_shift[-n])
        if e > max_bodd:
            max_bodd = e
    # 6. a_n even: diagonal
    max_aeven = mpf(0)
    for n in range(1, N + 1):
        e = abs(T[idx(n), idx(n)] - T[idx(-n), idx(-n)])
        if e > max_aeven:
            max_aeven = e

    print(f"\n  === SANITY CHECK {label} ===")
    print(f"    max|Im T_ij|              = {nstr(max_imag, 4)}")
    print(f"    max|T_ij − T_ji|          = {nstr(max_sym, 4)}   (symmetry)")
    print(f"    max|T_ij − T_{{-i,-j}}|     = {nstr(max_gam, 4)}   (γ-commute)")
    print(f"    max|T_ij − (b_i−b_j)/(i−j)| = {nstr(max_cf, 4)}   (CF/Toeplitz)")
    print(f"    max|b_n + b_{{-n}}|          = {nstr(max_bodd, 4)}   (b odd)")
    print(f"    max|a_n − a_{{-n}}|          = {nstr(max_aeven, 4)}   (a even)")
    tol = mpf(10) ** (-150)
    all_pass = (
        max_imag < tol and max_sym < tol and max_gam < tol
        and max_cf < tol and max_bodd < tol and max_aeven < tol
    )
    print(f"    all within 10^{{-150}}?      {all_pass}")
    return all_pass


def golden_reference_check(N, lam, ns=(0, 1, 2, 3, 5, 10)):
    """Compare γ_L path vs eq (4.4) direct quadrature for W_R(V_n, V_n)."""
    L = 2 * log(mpf(lam))
    print(f"\n  === GOLDEN-REFERENCE W_R(V_n, V_n) CHECK (λ={float(lam)}) ===")
    print(f"    n     via 2γ_L(n) − 2β_L(n)                    via eq (4.4)                              |diff|")
    max_diff = mpf(0)
    for n in ns:
        via_ab = 2 * gamma_of_L(n, L) - 2 * beta_of_L(n, L)
        via_44 = WR_diag_from_eq44(n, L)
        d = abs(via_ab - via_44)
        if d > max_diff:
            max_diff = d
        print(f"    {n:2d}   {nstr(via_ab, 14):>40}   {nstr(via_44, 14):>40}   {nstr(d, 4):>10}")
    print(f"    max diff = {nstr(max_diff, 4)}")
    return max_diff


# ============================================================================
# §4. Eigenpair extraction and parity defect.
# ============================================================================


def eigeninfo(Me):
    """Return sorted eigenvalues and the normalized lowest eigenvector."""
    n = Me.rows
    E, ER = eig(Me, left=False, right=True)
    reals = [e.real for e in E]
    order = sorted(range(n), key=lambda i: reals[i])
    sorted_evals = [reals[i] for i in order]
    v0 = matrix(n, 1)
    i0 = order[0]
    for i in range(n):
        v0[i, 0] = ER[i, i0].real
    s = sqrt(sum(v0[i, 0] ** 2 for i in range(n)))
    for i in range(n):
        v0[i, 0] /= s
    return sorted_evals, v0


def full_space_eig_parity(T, N):
    """Diagonalize FULL (2N+1)x(2N+1) T and compute odd-sector norm of min
    eigenvector (the parity defect). This doubles as a check that the
    smallest eigenvector lies in the even sector.
    """
    d = 2 * N + 1
    E, ER = eig(T, left=False, right=True)
    reals = [e.real for e in E]
    order = sorted(range(d), key=lambda i: reals[i])
    i0 = order[0]
    v = matrix(d, 1)
    for i in range(d):
        v[i, 0] = ER[i, i0].real
    s = sqrt(sum(v[i, 0] ** 2 for i in range(d)))
    for i in range(d):
        v[i, 0] /= s
    # odd component: v_odd_k = (v[N+k] − v[N−k]) / √2 for k ≥ 1
    odd_norm_sq = mpf(0)
    even_norm_sq = v[N, 0] ** 2
    for k in range(1, N + 1):
        odd_c = (v[N + k, 0] - v[N - k, 0]) / sqrt(mpf(2))
        even_c = (v[N + k, 0] + v[N - k, 0]) / sqrt(mpf(2))
        odd_norm_sq += odd_c ** 2
        even_norm_sq += even_c ** 2
    return reals[i0], odd_norm_sq, even_norm_sq


# ============================================================================
# §5. Driver.
# ============================================================================


def run_point(lam, N, check_sanity=False, check_golden=False):
    t_all = time.time()
    lam_mpf = lam if isinstance(lam, type(mpf(1))) else mpf(lam)
    print(f"\n========== (λ = {float(lam_mpf)}, N = {N}) ==========")
    t0 = time.time()
    T = build_QW_matrix_rebuild(N, lam_mpf, verbose=False)
    print(f"  build time: {time.time()-t0:.1f}s")

    if check_sanity:
        sanity_check(T, N, label=f"(λ={float(lam_mpf)}, N={N})")
    if check_golden:
        golden_reference_check(N, lam_mpf)

    # Full-space parity defect
    mu0_full, odd_norm_sq, even_norm_sq = full_space_eig_parity(T, N)

    # Even-sector simplicity gap
    Me = even_sector_matrix(T, N)
    ev, v0 = eigeninfo(Me)
    mu0 = ev[0]
    mu1 = ev[1]
    gap = mu1 - mu0
    print(f"  μ_0 (even-sector)   = {nstr(mu0, 20)}")
    print(f"  μ_1 (even-sector)   = {nstr(mu1, 20)}")
    print(f"  μ_1 − μ_0           = {nstr(gap, 20)}")
    print(f"  μ_0 (full-space)    = {nstr(mu0_full, 20)}")
    print(f"  ‖v_odd‖² (parity defect) = {nstr(odd_norm_sq, 8)}")
    print(f"  ‖v_even‖²                = {nstr(even_norm_sq, 8)}")
    print(f"  total point time: {time.time()-t_all:.1f}s")
    return {
        "lam": float(lam_mpf),
        "N": N,
        "mu0": mu0,
        "mu1": mu1,
        "gap": gap,
        "odd_norm_sq": odd_norm_sq,
        "mu0_full": mu0_full,
    }


def cross_lead_check_against_L5(T_rebuild, N=30):
    """Load Lead 5's build of the same matrix and compare entries at
    (0,0), (0,1), (1,0), (5,5), (10,10) (in the [−N, N] indexing; here
    (a,b) in the problem statement means n=a, m=b, which corresponds
    to row/col n+N, m+N in the full matrix).
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "lead5",
        "/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/online-researcher-adversarial/code/lead-5-verify-ccm-convergence.py",
    )
    mod = importlib.util.module_from_spec(spec)
    # Monkeypatch to prevent __main__ execution
    mod.__name__ = "lead5"
    spec.loader.exec_module(mod)
    print(f"\n  === CROSS-LEAD L8 vs L5 MATRIX CHECK (λ=4, N={N}) ===")
    T5 = mod.build_QW_matrix(N, mpf(4), verbose=False)
    idx = lambda n: n + N
    pts = [(0, 0), (0, 1), (1, 0), (5, 5), (10, 10)]
    print(f"    (n,m)     L8 rebuild                         L5                                |diff|")
    max_diff = mpf(0)
    for (n, m) in pts:
        a = T_rebuild[idx(n), idx(m)]
        b = T5[idx(n), idx(m)]
        d = abs(a - b)
        if d > max_diff:
            max_diff = d
        print(f"    ({n:2d},{m:2d})  {nstr(a, 14):>35}   {nstr(b, 14):>35}   {nstr(d, 4):>10}")
    print(f"    max diff = {nstr(max_diff, 4)}")
    return max_diff


if __name__ == "__main__":
    print("=" * 72)
    print(f"Lead 8 — CF-even-simple REBUILD    mp.dps = {mp.dps}")
    print(f"PRECISION_DECLARED = {PRECISION_DECLARED}")
    print("=" * 72)

    # ---- Part A step 4: sanity check at (λ=4, N=30) ------------------------
    lam0, N0 = mpf(4), 30
    print(f"\n[Part A.4] Sanity check at (λ={float(lam0)}, N={N0})")
    T_anchor = build_QW_matrix_rebuild(N0, lam0, verbose=True)
    sanity_check(T_anchor, N0, label=f"(λ={float(lam0)}, N={N0})")

    # ---- Part A golden reference -------------------------------------------
    golden_reference_check(N0, lam0)

    # ---- Part A step 5: cross-lead vs L5 at (λ=4, N=30) --------------------
    print(f"\n[Part A.5] Cross-lead L8 vs L5 at (λ={float(lam0)}, N={N0})")
    cross_lead_check_against_L5(T_anchor, N=N0)

    # ---- Part B step 6: simplicity gap at the standard grid ---------------
    print("\n[Part B.6] Simplicity and parity at the standard grid")
    grid = [
        (mpf(2), 30),
        (mpf(3), 30),
        (mpf(4), 30),  # can reuse T_anchor if we want; recompute for clean log
        (mpf(4), 50),
        (mpf(8), 30),
    ]
    results = []
    for (lam, N) in grid:
        try:
            r = run_point(lam, N)
            results.append(r)
        except Exception as e:
            print(f"  EXCEPTION at (λ={float(lam)}, N={N}): {e}")

    # ---- Part B step 9: extension test at non-integer λ -------------------
    print("\n[Part B.9] Extension test — non-integer λ")
    ext_grid = [
        (mpf("1.5"), 20),
        (mpf("5.5"), 20),
        (mpf("10.5"), 15),
    ]
    ext_results = []
    for (lam, N) in ext_grid:
        try:
            r = run_point(lam, N)
            ext_results.append(r)
        except Exception as e:
            print(f"  EXCEPTION at (λ={float(lam)}, N={N}): {e}")

    # ---- Summary ------------------------------------------------------------
    print("\n" + "=" * 72)
    print("SUMMARY TABLE")
    print("=" * 72)
    print(f"{'λ':>7}  {'N':>3}  {'μ_0 (even)':>26}  {'gap μ_1−μ_0':>26}  {'‖v_odd‖²':>14}")
    for r in results + ext_results:
        print(
            f"{r['lam']:>7.3f}  {r['N']:>3}  "
            f"{nstr(r['mu0'], 6):>26}  "
            f"{nstr(r['gap'], 6):>26}  "
            f"{nstr(r['odd_norm_sq'], 4):>14}"
        )
    print("=" * 72)
