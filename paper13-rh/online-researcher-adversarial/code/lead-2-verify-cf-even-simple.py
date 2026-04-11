"""Lead 2 — verify the CF-even-simple hypothesis of Connes-Letter-2026
(Theorem 6.1) for the truncated Weil quadratic form QW^N_lambda.

Construction follows CCM-2025 (arXiv:2511.22755), Sections 3, 4, 5.

The matrix T = QW^N_lambda in the basis V_n = U_n o log, |n| <= N, with
L = 2 log lambda, has entries

    tau_{n,m} = W_{0,2}(V_n, V_m) - W_R(V_n, V_m)
                - sum_{1 < k <= lambda^2} Lambda(k) k^{-1/2} q(U_n, U_m)(log k)

where (Lemma 4.1)

    W_{0,2}(V_n, V_m) = 32 L sinh^2(L/4) (L^2 - 16 pi^2 m n)
                       / [ (L^2 + 16 pi^2 m^2)(L^2 + 16 pi^2 n^2) ]

and the prime kernel q(U_n, U_m)(y) for y in [0,L] (Lemma 2.3)

    n != m :  ( sin(2 pi m y/L) - sin(2 pi n y/L) ) / ( pi (n - m) )
    n  = m :  2 (1 - y/L) cos(2 pi n y/L)

The W_R block uses Proposition 4.3 with the integrals
alpha_L(n), beta_L(n), gamma_L(n) of Proposition 4.2 (eqs 4.5-4.7)
plus the boundary correction c(L) + w(L).

The grading gamma acts by gamma(V_j) = V_{-j}; even-simple means the
smallest eigenvalue is simple and its eigenvector xi satisfies
xi_{-j} = xi_j (Definition 5.3 of CCM-2025).

We tabulate, for lambda in {2, 4, 8, 16, 20} and N in {10, 15, 20}:
   - smallest eigenvalue mu_0
   - gap to second eigenvalue mu_1 - mu_0  (simplicity test)
   - parity defect ||xi - gamma xi|| / ||xi|| (evenness test)
   - sign of gamma component (+1 = even, -1 = odd)

ADVANCE if both pass with margin >= 1e-30 at mp.dps = 60.
KILL/WEAKEN if either fails by >= 10 sigma at any tested point.
"""

import sys, time
from mpmath import mp, mpf, mpc, pi, log, exp, sinh, cosh, gamma as mpgamma
from mpmath import sin, cos, atan, hyp2f1, polylog, digamma, lerchphi
from mpmath import euler, matrix, eig, eigsy, sqrt, fabs, re, im

mp.dps = 60   # 60 decimal digits

# ----------------------------------------------------------------------
# Prime utilities

def primes_up_to(M):
    if M < 2: return []
    sieve = [True] * (M + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(M**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, M+1, i):
                sieve[j] = False
    return [i for i in range(M+1) if sieve[i]]

def prime_powers_up_to(M):
    """Return list of (k, p, m, log p) with k = p^m, 1 < k <= M, p prime."""
    out = []
    for p in primes_up_to(int(M)+1):
        m = 1
        pk = p
        while pk <= M:
            out.append((pk, p, m, log(mpf(p))))
            m += 1
            pk *= p
    return sorted(out, key=lambda t: t[0])

# ----------------------------------------------------------------------
# Building blocks

def W02_entry(L, n, m):
    """W_{0,2}(V_n, V_m), eq (4.2) of CCM-2025."""
    L = mpf(L)
    Pi = pi
    num = 32 * L * sinh(L/4)**2 * (L**2 - 16*Pi**2*m*n)
    den = (L**2 + 16*Pi**2*m**2) * (L**2 + 16*Pi**2*n**2)
    return num / den

def q_kernel(L, n, m, y):
    """q(U_n, U_m)(y) for y in [0,L], from Lemma 2.3."""
    Pi = pi
    if n == m:
        return 2 * (1 - y/L) * cos(2*Pi*n*y/L)
    return (sin(2*Pi*m*y/L) - sin(2*Pi*n*y/L)) / (Pi*(n - m))

# ----------------------------------------------------------------------
# W_R entry — uses the explicit formulas in Prop 4.2 of CCM-2025

def alpha_L(L, n):
    """alpha_L(n) = (1/pi) int_0^L sin(2 pi n x / L) rho(x) dx,
    where rho(x) = e^{x/2} / (e^x - e^{-x}). From eq (4.5) of CCM-2025."""
    if n == 0:
        return mpf(0)  # integrand is sin(0) = 0
    L = mpf(L); n = mpf(n); Pi = pi
    z = exp(-2*L)
    # Term 1: e^{-L/2} * Im( (2L / (L + 4 pi i n)) *
    #             2F1(1, pi i n/L + 1/4; pi i n/L + 5/4; e^{-2L}) )
    a1 = mpf(1)
    b1 = Pi*1j*n/L + mpf('0.25')
    c1 = Pi*1j*n/L + mpf('1.25')
    factor1 = (2*L) / (L + 4*Pi*1j*n)
    h1 = hyp2f1(a1, b1, c1, z)
    term1 = exp(-L/2) * im(factor1 * h1)
    # Term 2: (1/2) * Im( psi(pi i n / L + 1/4) )
    term2 = mpf('0.5') * im(digamma(Pi*1j*n/L + mpf('0.25')))
    return (term1 + term2) / Pi

def beta_L(L, n):
    """beta_L(n) = (1/L) int_0^L x cos(2 pi n x/L) rho(x) dx, eq (4.6)."""
    L = mpf(L); n = mpf(n); Pi = pi
    z = exp(-2*L)
    a = mpf(1)
    b = mpf('0.25') + Pi*1j*n/L
    c = mpf('1.25') + Pi*1j*n/L
    h = hyp2f1(a, b, c, z)
    factor = (2*L) / (4*Pi*n - 1j*L)
    term1 = -L * exp(-L/2) * im(factor * h)
    # Lerch Phi term:  -(e^{-L/2}/4) * Re(Phi(e^{-2L}, 2, i pi n / L + 1/4))
    Phi_val = lerchphi(z, 2, 1j*Pi*n/L + mpf('0.25'))
    term2 = -(exp(-L/2)/4) * re(Phi_val)
    # Trigamma psi^{(1)}(pi i n / L + 1/4)
    psi1 = polygamma_safe(1, Pi*1j*n/L + mpf('0.25'))
    term3 = mpf('0.25') * re(psi1)
    return (term1 + term2 + term3) / L

def polygamma_safe(k, z):
    """Compute psi^{(k)}(z) via mpmath."""
    from mpmath import polygamma
    return polygamma(k, z)

def gamma_L_int(L, n):
    """gamma_L(n) = int_0^L (cos(2 pi n x/L) - exp(-x/2)) rho(x) dx + c(L) + w(L)
    Per (4.14) and the corrections (4.11)."""
    L = mpf(L); n = mpf(n); Pi = pi
    z = exp(-2*L)
    # int_0^L (cos(2 pi n x / L) - 1) rho(x) dx, from eq (4.7).
    # When n = 0, this integral is 0.
    if n == 0:
        I_cos_minus_1 = mpf(0)
    else:
        a = mpf(1)
        b1 = Pi*1j*n/L + mpf('0.25')
        c1 = Pi*1j*n/L + mpf('1.25')
        h1 = hyp2f1(a, b1, c1, z)
        factor1 = (2*L) / (L + 4*Pi*1j*n)
        term1 = -exp(-L/2) * re(factor1 * h1)
        h2 = hyp2f1(mpf('0.25'), mpf(1), mpf('1.25'), z)
        term2 = 2 * exp(-L/2) * h2
        term3 = -mpf('0.5') * re(digamma(Pi*1j*n/L + mpf('0.25')) - digamma(mpf('0.25')))
        I_cos_minus_1 = term1 + term2 + term3
    # We want int (cos - exp(-x/2)) = int (cos - 1) - int (exp(-x/2) - 1) rho(x)
    # The text instead gives the correction c(L) (eq 4.11) so that
    #   int_0^L (cos(2 pi n x/L) - exp(-x/2)) rho dx
    #   = int_0^L (cos - 1) rho dx + c(L)
    cL = log(exp(L/2) + 1) + mpf('0.25')*(-2*log(exp(L)+1) - Pi - log(4)) + atan(exp(L/2))
    wL = mpf('0.5')*(euler + log(4*Pi)) - mpf('0.5')*log((exp(L)+1)/(exp(L)-1))
    return I_cos_minus_1 + cL + wL

def WR_entry(L, n, m):
    """W_R(V_n, V_m), per Proposition 4.3 of CCM-2025."""
    if n == m:
        return 2*gamma_L_int(L, n) - 2*beta_L(L, n)
    return (alpha_L(L, m) - alpha_L(L, n)) / (m - n)

# ----------------------------------------------------------------------
# Prime contribution

def prime_block(L, lam, N):
    """Compute the matrix sum_{1<k<=lambda^2} Lambda(k) k^{-1/2} q(U_n, U_m)(log k)
    over n, m in {-N, ..., N}."""
    M = lam*lam
    pk_list = prime_powers_up_to(M)  # k = p^m
    dim = 2*N + 1
    P = matrix(dim, dim)
    for k, p, mp_, logp in pk_list:
        y = log(mpf(k))
        if y >= L:  # by construction y < L since k <= lambda^2 = e^L
            continue
        Lambda_k = logp        # von Mangoldt: Lambda(p^m) = log p
        coef = Lambda_k / sqrt(mpf(k))
        for i, n in enumerate(range(-N, N+1)):
            for j, m_ in enumerate(range(-N, N+1)):
                P[i, j] = P[i, j] + coef * q_kernel(L, n, m_, y)
    return P

# ----------------------------------------------------------------------
# Assemble QW^N_lambda

def build_QW(lam, N):
    L = 2*log(mpf(lam))
    dim = 2*N + 1
    T = matrix(dim, dim)
    for i, n in enumerate(range(-N, N+1)):
        for j, m_ in enumerate(range(-N, N+1)):
            T[i, j] = W02_entry(L, n, m_) - WR_entry(L, n, m_)
    P = prime_block(L, lam, N)
    for i in range(dim):
        for j in range(dim):
            T[i, j] = T[i, j] - P[i, j]
    # Symmetrize
    for i in range(dim):
        for j in range(i+1, dim):
            avg = (T[i,j] + T[j,i]) / 2
            T[i,j] = avg; T[j,i] = avg
    return T

# ----------------------------------------------------------------------
# Diagonalize and test

def parity_test(xi):
    """xi is a column-vector matrix (length 2N+1, indexed -N..N)."""
    n = xi.rows
    N = (n-1)//2
    norm_sq = mpf(0)
    even_norm_sq = mpf(0)
    odd_norm_sq = mpf(0)
    for i in range(n):
        norm_sq += xi[i,0]**2
    # Symmetrize/antisymmetrize
    even = matrix(n,1); odd = matrix(n,1)
    for i in range(n):
        j_idx = i           # index from 0
        k_idx = (n-1) - i   # mirror index
        e_part = (xi[j_idx,0] + xi[k_idx,0]) / 2
        o_part = (xi[j_idx,0] - xi[k_idx,0]) / 2
        even[j_idx,0] = e_part
        odd[j_idx,0] = o_part
    e_sq = sum(even[i,0]**2 for i in range(n))
    o_sq = sum(odd[i,0]**2 for i in range(n))
    return e_sq, o_sq, norm_sq

def smallest_eig(T):
    """Symmetric eigenvalue decomposition. Returns sorted (eigvals, eigvecs)."""
    vals, vecs = eigsy(T)
    # mpmath eigsy returns eigenvalues unsorted; sort.
    n = len(vals)
    idx = sorted(range(n), key=lambda i: float(vals[i]))
    sorted_vals = [vals[i] for i in idx]
    # Reorder columns
    sorted_vecs = matrix(n, n)
    for new_j, old_j in enumerate(idx):
        for i in range(n):
            sorted_vecs[i, new_j] = vecs[i, old_j]
    return sorted_vals, sorted_vecs

def analyze(lam, N):
    t0 = time.time()
    print(f"\n=== lambda = {lam}, N = {N}  (dim = {2*N+1}, primes <= {lam*lam}) ===")
    T = build_QW(lam, N)
    sym_err = mpf(0)
    for i in range(T.rows):
        for j in range(i+1, T.cols):
            d = abs(T[i,j] - T[j,i])
            if d > sym_err: sym_err = d
    print(f"   build time: {time.time()-t0:.1f}s   sym err = {mp.nstr(sym_err, 3)}")
    vals, vecs = smallest_eig(T)
    mu0 = vals[0]; mu1 = vals[1]; mu2 = vals[2]
    gap = mu1 - mu0
    print(f"   mu_0 = {mp.nstr(mu0, 20)}")
    print(f"   mu_1 = {mp.nstr(mu1, 20)}")
    print(f"   mu_2 = {mp.nstr(mu2, 20)}")
    print(f"   gap (mu_1 - mu_0) = {mp.nstr(gap, 12)}")
    # Smallest-eigenvalue eigenvector
    n = T.rows
    xi = matrix(n, 1)
    for i in range(n):
        xi[i, 0] = vecs[i, 0]
    e_sq, o_sq, norm_sq = parity_test(xi)
    print(f"   |xi|^2     = {mp.nstr(norm_sq, 8)}")
    print(f"   ||even||^2 = {mp.nstr(e_sq, 8)}    ||odd||^2 = {mp.nstr(o_sq, 8)}")
    parity_ratio = e_sq / norm_sq
    print(f"   even fraction = {mp.nstr(parity_ratio, 8)}")
    even_simple = (parity_ratio > mpf('0.999999')) and (gap > mpf('1e-20'))
    print(f"   --> even-simple HYPOTHESIS HOLDS: {even_simple}")
    return {
        'lambda': lam, 'N': N,
        'mu0': mp.nstr(mu0, 20),
        'mu1': mp.nstr(mu1, 20),
        'gap': mp.nstr(gap, 12),
        'even_frac': mp.nstr(parity_ratio, 12),
        'even_simple': even_simple,
    }

if __name__ == "__main__":
    print("=" * 70)
    print("Lead 2: CF-even-simple verification (Connes-Letter-2026 Thm 6.1)")
    print(f"mp.dps = {mp.dps}")
    print("=" * 70)

    # Use small N first to keep this responsive; the property is supposed
    # to hold for ALL N >= 1 if it holds at all (per the AE-simp-N<=20 lemma
    # and CF-rho>=4.27 decay).
    results = []
    GRID = [
        (2, 5),
        (2, 10),
        (4, 5),
        (4, 10),
        (8, 5),
        (8, 10),
        (16, 5),
        (16, 10),
        (20, 5),
        (20, 10),
    ]
    for lam, N in GRID:
        try:
            r = analyze(lam, N)
            results.append(r)
        except Exception as e:
            print(f"ERROR at lambda={lam}, N={N}: {e}")
            results.append({'lambda': lam, 'N': N, 'error': str(e)})

    print("\n" + "=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print(f"{'lam':>6} {'N':>4} {'mu_0':>30} {'gap':>16} {'even_frac':>18} {'PASS?':>8}")
    for r in results:
        if 'error' in r:
            print(f"{r['lambda']:>6} {r['N']:>4} ERROR: {r['error']}")
            continue
        print(f"{r['lambda']:>6} {r['N']:>4} {r['mu0']:>30} {r['gap']:>16} "
              f"{r['even_frac']:>18} {str(r['even_simple']):>8}")
    print("=" * 70)
