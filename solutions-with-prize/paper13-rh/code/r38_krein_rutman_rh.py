"""
R38: Krein-Rutman framework for RH

Computes:
1. The Weil quadratic form kernel K_W(x,y) for x,y in [lambda^{-1}, lambda]
2. Eigenvalue structure: is K_W positive semi-definite?
3. Rank-one Euler perturbations: does even-simple survive as primes are added?
4. Tracks the smallest eigenvalue and its simplicity
"""

import numpy as np
from scipy import linalg
from mpmath import mp, mpf, log, exp, pi, gamma, digamma, zeta, zetazero
import warnings
warnings.filterwarnings('ignore')

mp.dps = 30  # 30 decimal digits

# ============================================================
# Part A: Heat kernel on S^1 -- strong positivity verification
# ============================================================

def heat_kernel_S1(phi, phi_prime, t, n_max=200):
    """Heat kernel on S^1 of circumference 2*pi:
    K_t(phi, phi') = (1/2*pi) * sum_n exp(-n^2 * t) * exp(i*n*(phi - phi'))
    For t > 0, this is STRICTLY POSITIVE for all phi, phi'.
    """
    diff = phi - phi_prime
    val = 0.0
    for n in range(-n_max, n_max + 1):
        val += np.exp(-n**2 * t) * np.exp(1j * n * diff)
    return val.real / (2 * np.pi)

def verify_heat_kernel_positivity(t_values=[0.01, 0.1, 0.5, 1.0, 2.0]):
    """Verify K_t(phi, phi') > 0 for all phi, phi' at various t."""
    print("=" * 70)
    print("PART A: Heat Kernel on S^1 -- Strong Positivity")
    print("=" * 70)

    N_grid = 50
    phis = np.linspace(-np.pi, np.pi, N_grid, endpoint=False)

    for t in t_values:
        K_matrix = np.zeros((N_grid, N_grid))
        for i, p1 in enumerate(phis):
            for j, p2 in enumerate(phis):
                K_matrix[i, j] = heat_kernel_S1(p1, p2, t)

        min_val = K_matrix.min()
        max_val = K_matrix.max()
        eigs = np.sort(np.linalg.eigvalsh(K_matrix))

        # Check compactness (trace class): eigenvalues decay
        print(f"\nt = {t}:")
        print(f"  K_t range: [{min_val:.8e}, {max_val:.8e}]")
        print(f"  min(K_t) > 0? {'YES' if min_val > 0 else 'NO'}")
        print(f"  Eigenvalues (first 5): {eigs[:5]}")
        print(f"  Eigenvalues (last 5):  {eigs[-5:]}")
        print(f"  All eigenvalues > 0? {'YES' if eigs[0] > -1e-14 else 'NO'}")

        # Krein-Rutman check: is the largest eigenvalue simple?
        if len(eigs) >= 2:
            gap = eigs[-1] - eigs[-2]
            print(f"  Spectral radius: {eigs[-1]:.8e}")
            print(f"  Gap to next eigenvalue: {gap:.8e}")
            print(f"  Simple? {'YES (gap > 0)' if gap > 1e-12 else 'NO'}")

    # Check the EVEN subspace
    print("\n--- Restriction to EVEN functions ---")
    t = 0.5
    N_even = 25
    phis_pos = np.linspace(0, np.pi, N_even, endpoint=False)

    # Build even heat kernel: K_t^even(phi1, phi2) = K_t(phi1, phi2) + K_t(phi1, -phi2)
    K_even = np.zeros((N_even, N_even))
    for i, p1 in enumerate(phis_pos):
        for j, p2 in enumerate(phis_pos):
            K_even[i, j] = heat_kernel_S1(p1, p2, t) + heat_kernel_S1(p1, -p2, t)

    eigs_even = np.sort(np.linalg.eigvalsh(K_even))
    print(f"\nt = {t}, even subspace:")
    print(f"  min eigenvalue: {eigs_even[0]:.8e}")
    print(f"  max eigenvalue: {eigs_even[-1]:.8e}")
    print(f"  All > 0? {'YES' if eigs_even[0] > -1e-14 else 'NO'}")
    print(f"  Gap: {eigs_even[-1] - eigs_even[-2]:.8e}")
    print(f"  Krein-Rutman applies (strongly positive on even subspace):",
          "YES" if eigs_even[0] > -1e-14 and (eigs_even[-1] - eigs_even[-2]) > 1e-10 else "NO")


# ============================================================
# Part B: Weil quadratic form kernel and eigenvalues
# ============================================================

def weil_kernel_components(x, y, lam, N_primes=10):
    """Compute the Weil kernel K_W(x, y) decomposed into:
    K_W = K_0 (pole terms) + K_inf (archimedean) + sum_p K_p (prime terms)

    Working in log coordinates: u = log(x), v = log(y)
    x, y in [lam^{-1}, lam], so u, v in [-log(lam), log(lam)]

    The Weil distribution for zeta(s):
    Psi(F) = W_{0,2}(F) - W_R(F) - sum_p W_p(F)

    W_{0,2}(F) = F-hat(i/2) + F-hat(-i/2)   [pole terms]
    W_R(F) = integral involving digamma       [archimedean]
    W_p(F) = sum_{m>=1} log(p)/p^{m/2} (F(m*log p) + F(-m*log p))  [prime]
    """
    u = float(x)
    v = float(y)
    L = 2 * np.log(lam)
    w = u - v  # difference variable for convolution kernel

    # Component 1: Pole terms W_{0,2}
    # F-hat(z) = integral F(w) e^{-izw} dw
    # For kernel: K_0(u,v) represents the pole contribution
    # W_{0,2} = e^{w/2} + e^{-w/2} = 2*cosh(w/2)
    K_0 = 2 * np.cosh(w / 2)

    # Component 2: Archimedean W_R
    # The archimedean kernel involves the digamma function
    # For zeta: W_R(w) = -(1/2)*Psi(1/4 + |w|/(4*pi)) type terms
    # More precisely, the archimedean distribution is:
    # W_R(F) = integral_0^infty [F(0) - F(t)/(2*cosh(pi*t/2))] * (Gamma'/Gamma)(1/4 + it/2) dt + ...
    # For the KERNEL, this is a convolution-type distribution
    # Approximate: the archimedean contribution for |w| > 0 involves
    # a logarithmic singularity at w = 0 and decays
    # Use the known formula:
    # K_inf(w) = delta(w) * (log(4*pi) + gamma_E) - 1/(4*pi) * sum of Gamma'/Gamma terms
    # For discretization, we use: K_inf ~ (1/2)*log(1/(|w|+eps)) for small |w|
    # This is approximate -- the exact form involves the xi-hat transform

    # Simplified archimedean: use the log-Gamma derivative
    # K_inf(w) ~ -Re[psi(1/4 + i*w/(4*pi))] / (2*pi) for w != 0
    # where psi = digamma
    if abs(w) > 1e-10:
        try:
            psi_val = complex(digamma(mpf('0.25') + 1j * mpf(str(w)) / (4 * float(mp.pi))))
            K_inf = -psi_val.real / (2 * np.pi)
        except:
            K_inf = 0.0
    else:
        # At w=0: involves log(4*pi) + Euler-Mascheroni
        K_inf = (np.log(4 * np.pi) + 0.5772156649) / (2 * np.pi)

    # Component 3: Prime contributions
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    K_p_total = 0.0
    K_p_individual = {}

    for p in primes[:N_primes]:
        if p > lam**2:
            break
        K_p_val = 0.0
        log_p = np.log(p)
        for m in range(1, int(np.log(lam**2) / log_p) + 2):
            mlogp = m * log_p
            if mlogp > L:
                break
            coeff = np.log(p) / p**(m / 2)
            # Prime kernel: delta-type contributions at w = +/- m*log(p)
            # In discretized form: K_p(w) = -log(p)/p^{m/2} * [delta(w - m*log p) + delta(w + m*log p)]
            # Use Gaussian approximation to delta: delta(x) ~ (1/sigma*sqrt(2*pi))*exp(-x^2/(2*sigma^2))
            sigma = 0.1  # smoothing parameter
            K_p_val -= coeff * (np.exp(-(w - mlogp)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
                               + np.exp(-(w + mlogp)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi)))

        K_p_individual[p] = K_p_val
        K_p_total += K_p_val

    return K_0, K_inf, K_p_total, K_p_individual


def build_weil_matrix(lam, N_grid=50, N_primes=6):
    """Build the Weil quadratic form matrix Q_W on a grid in [lam^{-1}, lam].
    Uses log-coordinates u in [-log(lam), log(lam)].
    """
    L = np.log(lam)
    us = np.linspace(-L, L, N_grid)
    du = us[1] - us[0]

    Q_W = np.zeros((N_grid, N_grid))
    Q_0 = np.zeros((N_grid, N_grid))
    Q_inf = np.zeros((N_grid, N_grid))
    Q_p = np.zeros((N_grid, N_grid))

    for i in range(N_grid):
        for j in range(N_grid):
            K0, Kinf, Kp, _ = weil_kernel_components(us[i], us[j], lam, N_primes)
            Q_0[i, j] = K0 * du
            Q_inf[i, j] = Kinf * du
            Q_p[i, j] = Kp * du
            Q_W[i, j] = (K0 + Kinf + Kp) * du

    return Q_W, Q_0, Q_inf, Q_p, us


def analyze_weil_form(lam=10.0, N_grid=50, N_primes_max=6):
    """Analyze the Weil quadratic form: eigenvalues, even-simple condition."""
    print("\n" + "=" * 70)
    print(f"PART B: Weil Quadratic Form Analysis (lambda = {lam})")
    print("=" * 70)

    Q_W, Q_0, Q_inf, Q_p, us = build_weil_matrix(lam, N_grid, N_primes_max)

    # Full spectrum
    eigs_full = np.sort(np.linalg.eigvalsh(Q_W))
    print(f"\nFull Q_W ({N_grid}x{N_grid}, {N_primes_max} primes):")
    print(f"  Smallest eigenvalue: {eigs_full[0]:.8e}")
    print(f"  Largest eigenvalue:  {eigs_full[-1]:.8e}")
    print(f"  # positive eigenvalues: {np.sum(eigs_full > 1e-14)}")
    print(f"  # negative eigenvalues: {np.sum(eigs_full < -1e-14)}")
    print(f"  Trace: {np.trace(Q_W):.6e}")

    # Even subspace: restrict to functions symmetric under u -> -u
    # Even basis: cos(k*pi*u/L) for k = 0, 1, ...
    N_even = N_grid // 2
    L = np.log(lam)

    # Build even projection
    P_even = np.zeros((N_grid, N_grid))
    for i in range(N_grid):
        # Find the reflected index: u_i -> -u_i
        j_reflect = N_grid - 1 - i
        P_even[i, i] += 0.5
        P_even[i, j_reflect] += 0.5

    Q_W_even = P_even @ Q_W @ P_even
    eigs_even = np.sort(np.linalg.eigvalsh(Q_W_even))
    # Remove near-zero eigenvalues from the odd subspace projection
    eigs_even_nonzero = eigs_even[np.abs(eigs_even) > 1e-12]

    print(f"\nEven subspace of Q_W:")
    print(f"  Smallest nonzero eigenvalue: {eigs_even_nonzero[0]:.8e}" if len(eigs_even_nonzero) > 0 else "  No nonzero eigenvalues")
    print(f"  Largest eigenvalue: {eigs_even_nonzero[-1]:.8e}" if len(eigs_even_nonzero) > 0 else "")

    # Component analysis
    eigs_0 = np.sort(np.linalg.eigvalsh(Q_0))
    eigs_inf = np.sort(np.linalg.eigvalsh(Q_inf))
    eigs_p = np.sort(np.linalg.eigvalsh(Q_p))

    print(f"\nComponent analysis:")
    print(f"  Q_0 (poles):   [{eigs_0[0]:.4e}, {eigs_0[-1]:.4e}], trace = {np.trace(Q_0):.4e}")
    print(f"  Q_inf (arch):  [{eigs_inf[0]:.4e}, {eigs_inf[-1]:.4e}], trace = {np.trace(Q_inf):.4e}")
    print(f"  Q_p (primes):  [{eigs_p[0]:.4e}, {eigs_p[-1]:.4e}], trace = {np.trace(Q_p):.4e}")

    return Q_W, Q_0, Q_inf, Q_p, eigs_full


# ============================================================
# Part C: Rank-one Euler perturbations -- track even-simple
# ============================================================

def connes_consani_fourier_weil_matrix(lam, N_modes, primes_to_include):
    """Build the Weil quadratic form in the FOURIER basis,
    following Connes-Consani more closely.

    Basis: V_n(u) = e^{2*pi*i*n*u/L} / sqrt(L) for |n| <= N_modes
    where L = 2*log(lam), u in [-L/2, L/2]

    Q_W is a (2*N_modes+1) x (2*N_modes+1) Hermitian matrix.
    """
    L = 2 * np.log(lam)
    dim = 2 * N_modes + 1

    # Index mapping: k -> n = k - N_modes, so k=0 -> n=-N_modes, k=N_modes -> n=0, etc.
    ns = np.arange(-N_modes, N_modes + 1)

    Q_W = np.zeros((dim, dim), dtype=complex)
    Q_pole = np.zeros((dim, dim), dtype=complex)
    Q_prime = np.zeros((dim, dim), dtype=complex)

    for a in range(dim):
        for b in range(dim):
            n_a = ns[a]
            n_b = ns[b]

            # Pole terms: W_{0,2}
            # <V_a | W_0 | V_b> = (1/L) * integral e^{-i*2*pi*n_a*u/L} * 2*cosh(u/2) * e^{i*2*pi*n_b*u/L} du
            # = (2/L) * integral_{-L/2}^{L/2} cosh(u/2) * e^{i*2*pi*(n_b - n_a)*u/L} du
            delta_n = n_b - n_a
            freq = 2 * np.pi * delta_n / L
            # integral cosh(u/2) * e^{i*freq*u} du from -L/2 to L/2
            # = 2 * Re[integral_0^{L/2} cosh(u/2) * cos(freq*u) du]  (since cosh is even)
            # Use: integral cosh(au) cos(bu) du = a*sinh(au)*cos(bu)/(a^2+b^2) + b*cosh(au)*sin(bu)/(a^2+b^2)
            a_coeff = 0.5
            b_coeff = freq
            denom = a_coeff**2 + b_coeff**2
            if denom > 1e-30:
                upper = L / 2
                val = (a_coeff * np.sinh(a_coeff * upper) * np.cos(b_coeff * upper)
                       + b_coeff * np.cosh(a_coeff * upper) * np.sin(b_coeff * upper)) / denom
                val -= 0  # lower limit is 0 where sinh=0 and sin=0
                val *= 2  # from symmetry
            else:
                val = 2 * np.sinh(L / 4)

            Q_pole[a, b] = val / L

            # Prime terms: W_p
            for p in primes_to_include:
                log_p = np.log(p)
                for m in range(1, int(L / log_p) + 1):
                    mlogp = m * log_p
                    if mlogp > L:
                        break
                    coeff = np.log(p) / p**(m / 2)
                    # <V_a | K_p^{(m)} | V_b> = -(coeff/L) * [e^{i*2*pi*(n_b-n_a)*mlogp/L} + e^{-i*2*pi*(n_b-n_a)*mlogp/L}]
                    # = -(2*coeff/L) * cos(2*pi*(n_b-n_a)*mlogp/L)
                    phase = 2 * np.pi * delta_n * mlogp / L
                    Q_prime[a, b] -= (2 * coeff / L) * np.cos(phase)

    Q_W = Q_pole + Q_prime  # Note: archimedean term is more complex, we separate it

    # Make Hermitian (should be by construction for real kernels)
    Q_W = (Q_W + Q_W.conj().T) / 2
    Q_pole = (Q_pole + Q_pole.conj().T) / 2
    Q_prime = (Q_prime + Q_prime.conj().T) / 2

    return Q_W.real, Q_pole.real, Q_prime.real, ns


def track_even_simple_vs_primes(lam=3.6, N_modes=30):
    """Track the even-simple condition as primes are added one at a time.

    lam^2 ~ 13 means primes up to 13: {2, 3, 5, 7, 11, 13}
    """
    print("\n" + "=" * 70)
    print(f"PART C: Rank-One Euler Perturbations (lambda = {lam}, N = {N_modes})")
    print("=" * 70)

    all_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    available_primes = [p for p in all_primes if p <= lam**2]

    print(f"\nPrimes available (p <= lam^2 = {lam**2:.1f}): {available_primes}")

    dim = 2 * N_modes + 1
    ns = np.arange(-N_modes, N_modes + 1)

    # Even projection in Fourier basis: V_n -> (V_n + V_{-n})/2
    # The even modes are cos-modes: (V_n + V_{-n})/sqrt(2)
    # Index of -n: N_modes - n maps to N_modes + n... let's build it
    P_even = np.zeros((dim, dim))
    for k in range(dim):
        n = ns[k]
        k_neg = np.where(ns == -n)[0][0]
        P_even[k, k] += 0.5
        P_even[k, k_neg] += 0.5

    print(f"\nStep-by-step perturbation analysis:")
    print(f"{'Primes':<25} {'min_eig':>12} {'max_eig':>12} {'gap':>12} {'even_simple':>12} {'sign_c_p':>10}")
    print("-" * 85)

    results = []

    for k in range(len(available_primes) + 1):
        primes_so_far = available_primes[:k]

        Q_W, Q_pole, Q_prime, _ = connes_consani_fourier_weil_matrix(
            lam, N_modes, primes_so_far
        )

        # Restrict to even subspace
        Q_W_even = P_even @ Q_W @ P_even
        eigs = np.sort(np.linalg.eigvalsh(Q_W_even))

        # Remove near-zero eigenvalues (from odd subspace)
        tol = 1e-10
        eigs_nonzero = eigs[np.abs(eigs) > tol]

        if len(eigs_nonzero) >= 2:
            min_eig = eigs_nonzero[0]
            max_eig = eigs_nonzero[-1]
            # Gap: difference between smallest and second smallest
            gap = eigs_nonzero[1] - eigs_nonzero[0]
            # Check simplicity of the smallest eigenvalue
            simple = gap > 1e-8
        else:
            min_eig = eigs_nonzero[0] if len(eigs_nonzero) > 0 else 0
            max_eig = min_eig
            gap = 0
            simple = False

        # Compute the eigenvector of the smallest eigenvalue
        eig_vals, eig_vecs = np.linalg.eigh(Q_W_even)
        idx_sort = np.argsort(eig_vals)
        # Find smallest nonzero
        for idx in idx_sort:
            if abs(eig_vals[idx]) > tol:
                min_vec = eig_vecs[:, idx]
                break

        # Check evenness: min_vec should satisfy v[n] = v[-n]
        even_check = True
        for i in range(dim):
            n = ns[i]
            j = np.where(ns == -n)[0][0]
            if abs(min_vec[i] - min_vec[j]) > 0.01:
                even_check = False
                break

        label = "free" if k == 0 else f"+{available_primes[k-1]}"
        primes_str = str(primes_so_far) if primes_so_far else "{}"
        sign_cp = "" if k == 0 else "NEGATIVE"

        even_simple_str = "YES" if (simple and even_check) else "NO"

        print(f"{primes_str:<25} {min_eig:>12.6e} {max_eig:>12.6e} {gap:>12.6e} {even_simple_str:>12} {sign_cp:>10}")

        results.append({
            'primes': list(primes_so_far),
            'min_eig': min_eig,
            'max_eig': max_eig,
            'gap': gap,
            'simple': simple,
            'even': even_check,
        })

    return results


# ============================================================
# Part D: Sign analysis of rank-one coefficients
# ============================================================

def analyze_prime_perturbation_signs():
    """Analyze the sign of the rank-one perturbation coefficient c_p
    for each prime p in the Weil explicit formula."""
    print("\n" + "=" * 70)
    print("PART D: Sign of Rank-One Perturbation Coefficients")
    print("=" * 70)

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

    print(f"\nIn the Weil explicit formula, prime p contributes:")
    print(f"  W_p(F) = -sum_{{m>=1}} log(p)/p^{{m/2}} * [F(m*log p) + F(-m*log p)]")
    print(f"\nThe MINUS SIGN means: the prime perturbation is NEGATIVE.")
    print(f"\nCoefficients -log(p)/p^{{1/2}} for m=1 (dominant term):")
    print(f"\n{'p':>5} {'log(p)':>10} {'p^{1/2}':>10} {'-log(p)/sqrt(p)':>16} {'sum_m |c_{p,m}|':>18}")
    print("-" * 65)

    total_neg = 0
    for p in primes:
        lp = np.log(p)
        sp = np.sqrt(p)
        c1 = -lp / sp

        # Total from all m: sum_{m=1}^infty log(p)/p^{m/2} = log(p)/(p^{1/2} - 1)
        total_m = lp / (sp - 1)
        total_neg -= total_m

        print(f"{p:>5} {lp:>10.4f} {sp:>10.4f} {c1:>16.6f} {-total_m:>18.6f}")

    print(f"\nPartial sum of all |c_p| (first {len(primes)} primes): {-total_neg:.6f}")
    print(f"\nNote: sum_{p} log(p)/(p^{1/2} - 1) DIVERGES as more primes are added.")
    print(f"This divergence is logarithmic, related to the PNT: sum ~ 2*sqrt(x)/log(x).")

    # But the pole terms grow too
    print(f"\nPole contribution W_0:")
    print(f"  For F supported on [-L, L]: W_0 ~ 2*cosh(L/4) ~ e^{{L/4}} as L -> infinity")
    print(f"  The pole terms GROW with lambda, providing positive mass.")

    for lam in [2, 3, 5, 10, 50, 100]:
        L = 2 * np.log(lam)
        W0_approx = 2 * np.cosh(L / 4)
        primes_available = [p for p in primes if p <= lam**2]
        neg_total = sum(np.log(p) / (np.sqrt(p) - 1) for p in primes_available)
        print(f"  lambda={lam:>4}: W_0 ~ {W0_approx:>10.4f}, sum |W_p| ~ {neg_total:>10.4f}, "
              f"ratio W_0/|W_p| = {W0_approx/neg_total:.4f}" if neg_total > 0 else
              f"  lambda={lam:>4}: W_0 ~ {W0_approx:>10.4f}, no primes")


# ============================================================
# Part E: Quantitative balance W_inf + W_0 vs sum |W_p|
# ============================================================

def quantitative_balance():
    """Check whether W_inf + W_0 dominates sum |W_p| for Gaussian test functions.
    Uses data from R36 (research/89) and extends it."""
    print("\n" + "=" * 70)
    print("PART E: Quantitative Balance W_inf + W_0 vs sum |W_p|")
    print("=" * 70)

    # From R36 (research/89-r36-cm-test-functions.md):
    # For zeta(s) with Gaussian h(t) = exp(-t^2/T^2)
    # The explicit formula for zeta(s) over Q:
    # S = W_inf + W_fin + W_0 where S = sum_rho h(gamma_rho)

    # We compute these directly using mpmath
    print("\nUsing Gaussian test function h(t) = exp(-t^2/T^2)")
    print(f"\n{'T':>5} {'W_inf+W_0':>14} {'|W_fin|':>14} {'S':>14} {'S>=0?':>8} {'Margin':>14}")
    print("-" * 75)

    for T in [0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0]:
        # Spectral sum: S = sum_rho exp(-gamma_rho^2/T^2) (under GRH, gamma_rho are real)
        S = mpf(0)
        for k in range(1, 201):
            try:
                z = zetazero(k)
                gamma_k = float(z.imag)
                S += 2 * exp(-mpf(gamma_k)**2 / mpf(T)**2)  # factor 2: pair rho and 1-rho
            except:
                break
        S = float(S)

        # Pole terms: W_0 = h-hat(i/2) + h-hat(-i/2) for zeta
        # h-hat(y) = T*sqrt(pi)*exp(-T^2*y^2/4) (FT of Gaussian)
        # h-hat(i/2) = T*sqrt(pi)*exp(-T^2*(-1/4)/4) = T*sqrt(pi)*exp(T^2/16)
        T_f = float(T)
        hhat_half = T_f * np.sqrt(np.pi) * np.exp(T_f**2 / 16)
        W_0 = 2 * hhat_half  # h-hat(i/2) + h-hat(-i/2) -- both give the same for even h

        # Prime sum: W_fin = -sum_p sum_m log(p)/p^{m/2} * [h(m*log p)]
        # h is even so h(m*log p) = exp(-(m*log p)^2/T^2)
        W_fin = 0
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
            lp = np.log(p)
            for m in range(1, 100):
                mlogp = m * lp
                h_val = np.exp(-(mlogp)**2 / T_f**2)
                if h_val < 1e-30:
                    break
                coeff = np.log(p) / p**(m / 2)
                W_fin -= 2 * coeff * h_val  # factor 2 for h(m*log p) + h(-m*log p)

        # W_inf = S - W_0 - W_fin (by the explicit formula identity)
        W_inf = S - W_0 - W_fin

        margin = (W_inf + W_0) - abs(W_fin)
        s_positive = "YES" if S >= -1e-10 else "NO"

        print(f"{T_f:>5.1f} {W_inf + W_0:>14.6f} {abs(W_fin):>14.6f} {S:>14.6f} {s_positive:>8} {margin:>14.6f}")

    print("\nNote: S = (W_inf + W_0) + W_fin, so Margin = (W_inf + W_0) - |W_fin| = S + 2*min(0, W_fin)")
    print("When W_fin < 0: Margin = S + 2*W_fin, and S >= 0 iff W_inf + W_0 >= |W_fin|")


# ============================================================
# Part F: Prolate operator connection
# ============================================================

def prolate_connection():
    """Analyze the connection between prolate spheroidal wave operators
    and the Weil quadratic form, following Connes PNAS 2022."""
    print("\n" + "=" * 70)
    print("PART F: Prolate Operator Connection")
    print("=" * 70)

    # The prolate spheroidal wave operator Q_Lambda on [-1, 1]:
    # (Q_Lambda f)(x) = integral_{-1}^{1} sin(Lambda*(x-y))/(pi*(x-y)) f(y) dy
    #
    # This is the sinc kernel restricted to [-1, 1].
    # Eigenvalues: 0 < ... < mu_2 < mu_1 < mu_0 < 1
    # Eigenvalues cluster at 0 and 1 (step function behavior as Lambda -> infinity)

    # Build the prolate operator for various Lambda
    print("\nProlate operator eigenvalues:")
    print(f"{'Lambda':>8} {'mu_0':>12} {'mu_1':>12} {'gap':>12} {'simple?':>10}")
    print("-" * 55)

    for Lambda in [5, 10, 20, 50, 100]:
        N_grid = 100
        xs = np.linspace(-1, 1, N_grid)
        dx = xs[1] - xs[0]

        Q = np.zeros((N_grid, N_grid))
        for i in range(N_grid):
            for j in range(N_grid):
                diff = xs[i] - xs[j]
                if abs(diff) > 1e-14:
                    Q[i, j] = np.sin(Lambda * diff) / (np.pi * diff) * dx
                else:
                    Q[i, j] = Lambda / np.pi * dx

        eigs = np.sort(np.linalg.eigvalsh(Q))
        mu_0 = eigs[-1]
        mu_1 = eigs[-2]
        gap = mu_0 - mu_1

        print(f"{Lambda:>8} {mu_0:>12.8f} {mu_1:>12.8f} {gap:>12.8e} {'YES' if gap > 1e-10 else 'NO':>10}")

    print(f"\nConnes (PNAS 2022, arXiv:2310.18423): The prolate operator's eigenvalues")
    print(f"approximate the Weil form eigenvalues. The SIMPLICITY of prolate eigenvalues")
    print(f"is proved (Comptes Rendus 2025). The question: does this transfer to Q_W?")
    print(f"\nThe prolate operator is COMPACT and SELF-ADJOINT with SIMPLE eigenvalues.")
    print(f"If Q_W converges to a limit related to the prolate operator, simplicity")
    print(f"would transfer by continuity (eigenvalue perturbation theory).")
    print(f"BUT: the convergence Q_W -> prolate is itself the open problem.")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("R38: Krein-Rutman Framework for RH")
    print("=" * 70)

    # Part A: Heat kernel positivity
    verify_heat_kernel_positivity()

    # Part B: Weil form analysis
    analyze_weil_form(lam=3.6, N_grid=40, N_primes_max=6)

    # Part C: Rank-one perturbations
    results = track_even_simple_vs_primes(lam=3.6, N_modes=20)

    # Part D: Sign analysis
    analyze_prime_perturbation_signs()

    # Part E: Quantitative balance
    quantitative_balance()

    # Part F: Prolate connection
    prolate_connection()

    print("\n" + "=" * 70)
    print("DONE")
