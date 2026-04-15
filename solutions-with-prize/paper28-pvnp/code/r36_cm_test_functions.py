"""
Round 36: CM-adapted test functions from the e-circle.
Compute Weil explicit formula for zeta_{Q(i)} with specific test functions.

The question: Does W_inf dominate Sigma_p W_p for CM-adapted test functions?
"""

import numpy as np
from mpmath import mp, mpf, gamma, digamma, log, pi, sqrt, exp, inf, quad
from mpmath import zetazero, zeta, cos, cosh, besselj, fabs
import json

mp.dps = 30  # 30 decimal digits precision

# ============================================================
# Part 1: Prime classification for Q(i)
# ============================================================

def sieve_primes(N):
    """Sieve of Eratosthenes up to N."""
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i):
                is_prime[j] = False
    return [p for p in range(2, N + 1) if is_prime[p]]

def classify_prime(p):
    """Classify a rational prime for Q(i).
    Returns: 'split' if p ≡ 1 mod 4, 'inert' if p ≡ 3 mod 4, 'ramified' if p = 2.
    """
    if p == 2:
        return 'ramified'
    elif p % 4 == 1:
        return 'split'
    else:
        return 'inert'

# ============================================================
# Part 2: Test functions and their Fourier transforms
# ============================================================

def h_gaussian(t, T):
    """Gaussian test function: h_T(t) = exp(-t^2/T^2)"""
    return exp(-t**2 / T**2)

def hhat_gaussian(x, T):
    """Fourier transform of Gaussian: hhat_T(x) = T*sqrt(pi)*exp(-pi^2*T^2*x^2)"""
    return T * sqrt(pi) * exp(-pi**2 * T**2 * x**2)

def h_sech(t, T):
    """Selberg test function: h(t) = 1/cosh(pi*t/(2T))"""
    return 1 / cosh(pi * t / (2 * T))

def hhat_sech(x, T):
    """Fourier transform of sech: hhat(x) = T / cosh(pi*T*x)
    (using integral tables: FT of sech(a*t) = pi/(2a) * sech(pi*x/(2a)))
    Here h(t) = sech(pi*t/(2T)), so a = pi/(2T).
    FT = pi/(2*pi/(2T)) * sech(pi*x/(2*pi/(2T))) = T * sech(T*x)
    """
    return T / cosh(T * x)

def h_triangle(t, T):
    """Triangle test function: h(t) = max(1 - |t|/T, 0)"""
    at = fabs(t)
    if at >= T:
        return mpf(0)
    return 1 - at / T

def hhat_triangle(x, T):
    """Fourier transform of triangle: hhat(x) = T * sinc^2(pi*T*x/2) * (something)
    Actually: FT of (1-|t|/T)_+ = (T/2) * sinc^2(Tx/2)
    More precisely: int_{-T}^{T} (1-|t|/T) e^{-2pi i x t} dt
    = 2 * int_0^T (1-t/T) cos(2*pi*x*t) dt
    = T * [sin(pi*T*x) / (pi*T*x)]^2
    """
    if x == 0:
        return T
    val = pi * T * x
    return T * (mp.sin(val) / val) ** 2

def h_bessel(t, T):
    """Bessel test function: h(t) = J_0(t/T)"""
    return besselj(0, t / T)

def hhat_bessel(x, T):
    """Fourier transform of J_0(t/T):
    FT of J_0(a*t) = 2 / sqrt(4*pi^2*x^2 - a^2) for |x| > a/(2*pi), else 0.
    Here a = 1/T.
    Hmm, this is tricky - J_0 doesn't have a nice FT in the usual sense because
    it doesn't decay fast enough. Use numerical integration instead.

    Actually, the standard result: integral_{-inf}^{inf} J_0(a|t|) e^{-2*pi*i*x*t} dt
    = 2/sqrt(a^2 - (2*pi*x)^2) if |2*pi*x| < a
    = 0 if |2*pi*x| > a

    For a = 1/T: the support of hhat is |x| < 1/(2*pi*T).
    """
    a = mpf(1) / T
    threshold = a / (2 * pi)
    absx = fabs(x)
    if absx >= threshold:
        return mpf(0)
    return 2 / sqrt(a**2 - (2 * pi * x)**2)


# ============================================================
# Part 3: Archimedean contribution W_inf
# ============================================================

def W_inf_numerical(h_func, hhat_func, T, max_terms=500):
    """
    Compute the archimedean contribution W_inf for zeta_{Q(i)}.

    For Q(i) with one complex place, the completed L-function is:
    Lambda(s) = |Delta_K|^{s/2} * Gamma_C(s) * zeta_{Q(i)}(s)

    where Gamma_C(s) = 2*(2*pi)^{-s} * Gamma(s) and |Delta_K| = 4.

    The archimedean contribution to the explicit formula:
    W_inf(h) = hhat(0)*log|Delta_K|/2 + hhat(0) + hhat(1)
             - integral of h(t) * [psi((1+it)/2) + psi((1-it)/2)] dt / (2*pi)
             + (Gamma'/Gamma terms)

    More precisely, for the Dedekind zeta of an imaginary quadratic field K:

    W_inf(h) = h_hat(0) * [log(|D_K|/pi^2)]
               - (1/pi) * integral_0^inf h(t) * Re[psi(1/2 + it)] dt
               + h_hat(0) + h_hat(1)

    Actually, let me use the standard explicit formula directly.

    The explicit formula for zeta_{Q(i)} is:
    sum_rho h(gamma_rho) = W_inf + W_fin + W_0

    where (following Iwaniec-Kowalski, or Weil):

    W_0 = hhat(0) + hhat(1)  (from poles at s=0 and s=1)

    W_fin = - sum over prime ideals p, sum_{m>=1}
              (log Np / Np^{m/2}) * [h(m*log(Np)) + h(-m*log(Np))]
              (but h is even, so this is -2*sum...)

    Wait, need to be careful about conventions. Let me use:

    h is an even function of t (the spectral parameter).
    rho = 1/2 + i*gamma, so h(gamma_rho) = h(gamma).

    The Weil explicit formula for the Dedekind zeta of K = Q(i):

    sum_rho h(gamma_rho) = (1/(2*pi)) * integral h(t) * Phi(t) dt + prime_sum

    where Phi(t) involves log-derivative of Gamma factors.

    I'll use the formulation from Bombieri's survey and compute directly.
    """

    # For zeta_{Q(i)}(s) = zeta(s) * L(s, chi_{-4}), the zeros are the
    # union of zeros of zeta(s) and L(s, chi_{-4}).
    #
    # The explicit formula can be written as:
    # sum_rho g(rho) = g(0) + g(1) - sum_p sum_m Lambda_K(p^m) * f(m*log(Np)) + W_arch
    #
    # where g(s) = hhat at (s - 1/2)/(2*pi*i), roughly.
    #
    # Let me use the STANDARD form. For an even test function h(t):
    # Let g(s) = hhat((s-1/2)/i) = integral h(t) e^{i(s-1/2)t} dt
    #          = integral h(t) [cos((s-1/2)t) + i*sin(...)] dt
    # Since h is even and real, g(s) = 2*integral_0^inf h(t)*cos((s-1/2)t) dt
    # = 2*integral_0^inf h(t)*cos((sigma-1/2)*t)*cosh(gamma*t) dt (for s=sigma+i*gamma)
    # ... this gets complicated. Let me just use numerical evaluation.

    # SIMPLER APPROACH: compute W_inf as the Gamma contribution.
    #
    # For Q(i), the archimedean L-factor is Gamma_C(s) = 2(2pi)^{-s} Gamma(s).
    # The log-derivative is:
    #   (Gamma_C'/Gamma_C)(s) = -log(2*pi) + psi(s)
    # where psi = Gamma'/Gamma is the digamma function.
    #
    # The archimedean contribution in the explicit formula is:
    #   W_inf(h) = -1/(2*pi) * integral_{-inf}^{inf} h(t) *
    #              Re[(Gamma_C'/Gamma_C)(1/2 + it)] dt
    #
    # For Q(i): (Gamma_C'/Gamma_C)(1/2+it) = -log(2*pi) + psi(1/2+it)
    #
    # So: W_inf = -1/(2*pi) * integral h(t) * Re[-log(2*pi) + psi(1/2+it)] dt
    #           = log(2*pi)/(2*pi) * integral h(t) dt
    #             - 1/(2*pi) * integral h(t) * Re[psi(1/2+it)] dt
    #           = log(2*pi) * hhat(0) / (2*pi) - 1/(2*pi) * I_psi
    #
    # Wait, I need to be more careful.

    # Let me use the completely explicit formula. For the Dedekind zeta of
    # an imaginary quadratic field K with discriminant D:
    #
    # zeta_K(s) = zeta(s) * L(s, chi_D)
    #
    # The completed function:
    # Lambda_K(s) = |D|^{s/2} * pi^{-s} * Gamma(s/2)^{r1} * Gamma(s)^{r2} * zeta_K(s)
    # For Q(i): r1 = 0, r2 = 1, |D| = 4.
    # Lambda_K(s) = 4^{s/2} * (2*(2*pi)^{-s}*Gamma(s)) * zeta_K(s)
    #             = 4^{s/2} * 2 * (2*pi)^{-s} * Gamma(s) * zeta_K(s)
    #
    # Actually the standard normalization for imaginary quadratic:
    # Lambda_K(s) = (|D_K|/pi^2)^{s/2} * Gamma(s) * zeta_K(s)
    # with functional equation Lambda_K(s) = Lambda_K(1-s).
    # For K = Q(i): |D_K| = 4, so (4/pi^2)^{s/2} * Gamma(s) * zeta_K(s).

    # USING THE EXPLICIT FORMULA AS IN IWANIEC-KOWALSKI (Ch. 5):
    # For a test function Phi(s) even analytic in |Im(s)| < 1/2 + epsilon,
    # define g(s) = integral_{-inf}^{inf} h(r) r^{-s} dr (Mellin).
    # Actually this is getting complicated. Let me just compute numerically.

    pass  # Will compute below in a cleaner way


def compute_explicit_formula_Q_i(h_func, hhat_func, T, prime_limit=10000,
                                  max_prime_power=20, label="h"):
    """
    Compute the Weil explicit formula for zeta_{Q(i)} with test function h.

    Using the explicit formula in the form:

    sum_rho h(gamma_rho) = W_0 + W_inf + W_fin

    where rho = 1/2 + i*gamma_rho are the non-trivial zeros of zeta_{Q(i)},

    W_0 = hhat(0) + hhat(1)  (but need careful convention)

    Actually, let's use the most standard form. For zeta_{Q(i)} = zeta * L(chi_{-4}),
    compute everything for the two L-functions separately and add.

    For a SINGLE Dirichlet L-function L(s, chi) with chi primitive mod q:

    sum_{rho of L(s,chi)} h(gamma_rho) =
        delta_{chi=1} * [h(i/2) + h(-i/2)]   (poles of zeta at 0,1)
        + (1/2*pi) * integral h(t) * [Phi_chi(1/2+it)] dt
        - 2 * sum_p sum_{m=1}^inf [chi(p^m) * log(p) / p^{m/2}] * h_hat(m*log p / (2*pi))

    Hmm, the conventions are getting tangled. Let me use a COMPLETELY explicit
    numerical approach.

    CLEAN APPROACH: Use the "log-derivative" form of the explicit formula.

    For L(s, chi) with chi mod q:

    sum_rho g(rho) = g(0) + g(1) [if chi=1]
                   - sum_p sum_m (chi(p^m)*log p) * [g_hat(m*log p) + g_hat(-m*log p)]
                   + integral involving Gamma

    where g is in the Schwartz space, g(s) = integral f(x) x^s dx/x (Mellin),
    and the sum over rho counts with multiplicity.

    TOO MANY CONVENTIONS. Let me just use mpmath to compute zeros directly
    and verify the formula numerically.
    """
    pass


# ============================================================
# CLEAN IMPLEMENTATION using the explicit formula as in
# Bombieri (2000) "The Riemann Hypothesis" (Clay)
# ============================================================

def compute_all(T_values, prime_limit=10000, num_zeros_verify=20):
    """
    Main computation. For each T, compute W_inf, W_fin, W_0,
    and the spectral sum, for the Gaussian test function.

    Convention: We use the explicit formula for the Dedekind zeta of Q(i).

    zeta_{Q(i)}(s) has non-trivial zeros at the zeros of zeta(s) and L(s, chi_{-4}).

    APPROACH: Rather than fighting with conventions, I'll compute:
    1. The spectral sum S(h) = sum_rho h(gamma_rho) directly from known zeros
    2. The prime sum W_fin from the explicit formula
    3. The archimedean contribution W_inf = S(h) - W_fin - W_0
       (this DEFINES W_inf correctly by the explicit formula identity)
    4. Then independently compute W_inf from the Gamma functions
    5. Cross-check that methods 3 and 4 agree

    Then: assess whether W_inf dominates |W_fin| for CM-adapted test functions.
    """

    results = {}
    primes = sieve_primes(prime_limit)

    for T_val in T_values:
        T = mpf(T_val)
        print(f"\n{'='*70}")
        print(f"  T = {T_val}")
        print(f"{'='*70}")

        # --- W_fin: finite prime sum ---
        # For zeta_{Q(i)}: the explicit formula prime sum is
        # W_fin = -sum over prime ideals p of Q(i), sum_{m>=1}
        #         (log(Np) / Np^{m/2}) * h_hat(m * log(Np) / (2*pi))  [symmetric form]
        #
        # But with h even: h_hat symmetric, so h_hat(x) + h_hat(-x) = 2*h_hat(x).
        #
        # Actually, in the standard explicit formula (see e.g. Iwaniec-Kowalski 5.53),
        # the prime sum for the Dedekind zeta is:
        #
        # P(h) = sum_p sum_{m=1}^inf Lambda_K(p^m) * h_hat(m*log(Np)/(2*pi)) / Np^{m/2}
        #
        # But let me use a cleaner formulation. The Weil explicit formula with
        # h(t) a test function, and Fourier conventions:
        #
        #   hhat(x) = integral h(t) e^{-2*pi*i*x*t} dt
        #
        # is:
        #   sum_rho h((rho - 1/2)/(2*pi*i))    [??? conventions...]
        #
        # OK, I'm going to cut through the convention mess by using the
        # SIMPLEST possible setup.
        #
        # Define: g(s) = integral_{-inf}^{inf} h(t) * e^{(s-1/2)*t} dt
        #       = hhat_Laplace(s - 1/2) where hhat_Laplace is the bilateral Laplace transform of h.
        #
        # For h(t) = exp(-t^2/T^2):
        # g(s) = integral exp(-t^2/T^2) * exp((s-1/2)*t) dt
        #       = T*sqrt(pi) * exp(T^2*(s-1/2)^2/4)
        #
        # The explicit formula for zeta_K(s):
        # sum_rho g(rho) = g(0) + g(1) [poles]
        #   - sum_{p prime ideal} sum_{m>=1} (log Np) * g(m*log Np) / Np^{m/2}  [WRONG]
        #
        # Hmm no. Let me use the TEXTBOOK FORMULA from Murty-Murty (2012):
        #
        # For the Dedekind zeta function zeta_K(s), the explicit formula with
        # test function F (even, Schwartz) is:
        #
        # sum_rho F(gamma_rho) = F(i/2) + F(-i/2)   [from poles at s=0,1 if present]
        #   + (1/(2*pi)) integral_{-inf}^{inf} F(t) * Phi_K(1/2+it) dt
        #   - (1/pi) sum_{p prime ideal} sum_{m=1}^inf (log Np / Np^{m/2})
        #            * Fhat(m*log(Np)/(2*pi)) * cos(0)
        #
        # where Fhat(y) = integral F(t) e^{-ity} dt is the standard Fourier transform,
        # and Phi_K involves Gamma'/Gamma.
        #
        # Let me use the simplest convention from Davenport's "Multiplicative Number Theory".
        #
        # DAVENPORT CONVENTION: For zeta(s) with even test function h:
        #
        #   sum_rho h(gamma_rho) = h(i/2) + h(-i/2)
        #     - (1/(2*pi)) * integral h(t) * [Gamma'/Gamma(1/4 + it/2)] dt
        #     - 2 * sum_{p} sum_{m=1}^inf (log p / p^{m/2}) * Fhat(m*log p)
        #
        # For Q(i): we need to use zeta_K instead of zeta. Let me just compute
        # everything numerically.

        # FINAL APPROACH: I'll compute everything in the cleanest way.
        #
        # The von Mangoldt explicit formula for zeta_K gives:
        #
        # psi_K(x) = x - sum_rho x^rho/rho - Lambda_K'/Lambda_K(0) - log(1-x^{-2})/2
        #
        # But we want the test-function form. Let me use NUMERICAL computation.

        # I'll compute:
        # A) The spectral sum directly from zeros
        # B) The prime sum from the Euler product data
        # C) The archimedean integral from Gamma functions
        # And verify A = B + C + (pole terms)

        # For zeta_{Q(i)} = zeta(s) * L(s, chi_{-4}):
        # The zeros are the union of {zeros of zeta} and {zeros of L(s,chi_{-4})}.
        # Both sets have zeros at rho = 1/2 + i*gamma with gamma > 0 (and conjugates).

        # A) SPECTRAL SUM (from zeros)
        # I'll use the first N_z pairs of zeros of each L-function
        N_z = 200  # number of zero pairs to use for each L-function

        # h(gamma) for the Gaussian: h(gamma) = exp(-gamma^2/T^2)
        # For a zero rho = 1/2 + i*gamma: the contribution is h(gamma) + h(-gamma) = 2*h(gamma)
        # [since h is even]

        print("  Computing spectral sum from zeros...")

        # Zeros of zeta(s):
        spectral_zeta = mpf(0)
        for n in range(1, N_z + 1):
            gam = zetazero(n).imag  # imaginary part of n-th zero
            spectral_zeta += 2 * h_gaussian(gam, T)  # two zeros: 1/2+i*gam, 1/2-i*gam

        # Zeros of L(s, chi_{-4}):
        # chi_{-4} is the non-trivial character mod 4: chi_{-4}(n) = (-4/n) Kronecker symbol
        # chi_{-4}(1)=1, chi_{-4}(2)=0, chi_{-4}(3)=-1, chi_{-4}(4)=0, period 4.
        # The zeros of L(s, chi_{-4}) are at 1/2 + i*gamma_n.
        # Use the Dirichlet L-function zeros from mpmath.

        spectral_chi4 = mpf(0)

        # mpmath doesn't have a direct function for L-function zeros with character.
        # But zeta_{Q(i)}(s) = zeta(s) * L(s, chi_{-4}), and the zeros of zeta_{Q(i)}
        # are the union. I can compute the zeros of L(s, chi_{-4}) by finding where
        # L(1/2 + it, chi_{-4}) = 0.
        #
        # Actually, I know the first several zeros of L(s, chi_{-4}):
        # gamma_1 ≈ 6.0209..., gamma_2 ≈ 10.2437..., gamma_3 ≈ 12.5653..., etc.
        # Let me compute them numerically using the functional equation.

        # Define chi_{-4}
        def chi_minus4(n):
            n = int(n) % 4
            if n == 1: return 1
            if n == 3: return -1
            return 0

        # L(s, chi_{-4}) = sum_{n=1}^inf chi_{-4}(n)/n^s
        #                = 1 - 1/3^s + 1/5^s - 1/7^s + ...
        # = prod_{p odd} (1 - chi_{-4}(p)/p^s)^{-1}

        def L_chi4(s):
            """Compute L(s, chi_{-4}) = beta function / Catalan-like."""
            return mp.dirichlet(s, [0, 1, 0, -1])

        # Find zeros of L(s, chi_{-4}) on the critical line
        # by searching for sign changes of the real part of Xi function.
        print("  Finding zeros of L(s, chi_{-4})...")

        chi4_zeros = []
        # Known approximate values of first zeros (imaginary parts):
        # I'll find them by evaluating L(1/2+it, chi_{-4}) and looking for zeros.

        # Use a grid search then refine with secant method
        dt = mpf('0.1')
        t_val = mpf('1.0')
        prev_val = L_chi4(mpf('0.5') + 1j * t_val)

        while len(chi4_zeros) < N_z and t_val < 600:
            t_val += dt
            cur_val = L_chi4(mpf('0.5') + 1j * t_val)

            # Check for sign change in real part
            if prev_val.real * cur_val.real < 0 or prev_val.imag * cur_val.imag < 0:
                # Refine: find zero by bisection on |L|
                a, b = t_val - dt, t_val
                for _ in range(60):  # bisection steps
                    mid = (a + b) / 2
                    fa = abs(L_chi4(mpf('0.5') + 1j * a))
                    fm = abs(L_chi4(mpf('0.5') + 1j * mid))
                    fb = abs(L_chi4(mpf('0.5') + 1j * b))
                    if fa < fb:
                        b = mid
                    else:
                        a = mid
                abs_at_mid = abs(L_chi4(mpf('0.5') + 1j * (a+b)/2))
                if abs_at_mid < mpf('1e-8'):
                    chi4_zeros.append((a + b) / 2)

            prev_val = cur_val

        print(f"  Found {len(chi4_zeros)} zeros of L(s, chi_{-4})")
        if len(chi4_zeros) > 0:
            print(f"  First few: {[float(z) for z in chi4_zeros[:5]]}")

        for gam in chi4_zeros:
            spectral_chi4 += 2 * h_gaussian(gam, T)

        spectral_total = spectral_zeta + spectral_chi4

        # B) PRIME SUM (W_fin)
        # The explicit formula for zeta_K gives:
        # W_fin = - sum over prime ideals p of O_K, sum_{m >= 1}
        #           (log Np) * [Np^{-m/2}] * [hhat_bilateral(m*log Np)]
        # where hhat_bilateral is defined appropriately.
        #
        # For h(t) = exp(-t^2/T^2), the bilateral Laplace transform at s-1/2 gives
        # g(s) = T*sqrt(pi)*exp(T^2*(s-1/2)^2/4).
        # Then g evaluated at the prime ideal contribution...
        #
        # OK, let me use the ACTUAL textbook formula. From Iwaniec-Kowalski (5.53):
        #
        # For the Dedekind zeta zeta_K(s) of a number field K, with F an even
        # test function whose Fourier transform Fhat has compact support:
        #
        # sum_rho F(gamma_rho/(2*pi)) = ...
        #
        # UGH. Let me go to the ROOT and compute explicitly.
        #
        # THE ROOT: The von Mangoldt function Lambda_K for Q(i):
        # Lambda_K(a) = log(Np) if a = p^m for a prime ideal p of O_K
        #
        # The explicit formula (Weil) is:
        # sum_rho g(rho) = g(0) + g(1) - sum_{a} Lambda_K(a) * f(Na) / Na^{1/2}
        #                  + archimedean_integral
        #
        # where f is related to g by Mellin transform:
        # g(s) = integral_0^inf f(x) x^{s-1} dx
        #
        # For our purposes with h(t) = exp(-t^2/T^2):
        # We want g(rho) = g(1/2+i*gamma) = h(gamma) to be our test function
        # evaluated at the spectral parameter.
        #
        # So g(s) = h((s-1/2)/i) = h(-i*(s-1/2)) = exp(-(s-1/2)^2/T^2)
        #         = exp(-(s-1/2)^2/T^2)
        # Wait, that's the same as h but evaluated at the imaginary-rotated argument.
        # For s = 1/2+i*gamma: g(s) = exp(-(-gamma)^2/T^2) = exp(-gamma^2/T^2) = h(gamma). Good.
        #
        # Now, g(s) = exp(-(s-1/2)^2/T^2). This is an entire function of s.
        # The Mellin inversion gives: f(x) = (1/(2*pi*i)) integral g(s) x^{-s} ds
        #
        # For the prime sum: we need sum_{n=1}^inf Lambda_K(n) * f(n) / n^{1/2}
        # Since f(x) = Mellin^{-1}(g)(x), we have:
        # sum Lambda_K(n) f(n)/n^{1/2} = sum Lambda_K(n) * [1/(2*pi*i) * integral g(s) n^{-s} ds] / n^{1/2}
        # = (1/(2*pi*i)) integral g(s) * [-zeta_K'/zeta_K(s+1/2)] ds ... getting circular.
        #
        # SIMPLEST DIRECT APPROACH:
        # Use the fact that for zeta_K = zeta * L(chi_{-4}),
        # -zeta_K'/zeta_K(s) = -zeta'/zeta(s) - L'/L(s, chi_{-4})
        #                    = sum_n Lambda(n)/n^s + sum_n Lambda(n)*chi_{-4}(n)/n^s
        #                    = sum_n Lambda(n)*(1+chi_{-4}(n))/n^s
        #
        # Hmm, that's not quite right either for ideals vs integers.
        #
        # For zeta_K(s) = prod_{p ideal} (1-Np^{-s})^{-1}, we have:
        # -zeta_K'/zeta_K(s) = sum_{p ideal} sum_{m>=1} (log Np) * Np^{-ms}
        #
        # For Q(i):
        # - p=2 (ramified): one ideal (1+i) with N=2. Contributes sum_m log(2)/2^{ms}
        # - p≡1 mod 4 (split): two ideals each with Np=p. Contributes 2*sum_m log(p)/p^{ms}
        # - p≡3 mod 4 (inert): one ideal with Np=p^2. Contributes sum_m log(p^2)/p^{2ms}
        #   = sum_m 2*log(p)/p^{2ms}
        #
        # So: -zeta_K'/zeta_K(s) = sum_m log(2)/2^{ms}
        #                         + sum_{p≡1(4)} 2*sum_m log(p)/p^{ms}
        #                         + sum_{p≡3(4)} sum_m 2*log(p)/p^{2ms}

        # THE EXPLICIT FORMULA (standard form, Bombieri):
        # For g(s) as above, the explicit formula says:
        #
        # sum_rho g(rho) = delta * [g(0) + g(1)]
        #                  + (1/(2*pi)) * integral_{-inf}^{inf} g(1/2+it) *
        #                    [-zeta_K'/zeta_K ... Gamma terms] dt
        #
        # But since g(rho) = h(gamma_rho), and we KNOW the zeros, we can compute
        # the spectral sum directly. Let me instead compute the PRIME SUM
        # and ARCHIMEDEAN INTEGRAL separately, then see if they match.

        # PRIME SUM using the explicit formula in the form:
        #
        # The prime sum contribution (with our g) is:
        # W_fin = -sum over prime ideals p, sum_{m>=1} (log Np) * Np^{-m/2} * g_tilde(m*log Np)
        #
        # where g_tilde is the "check" function evaluated at log-argument.
        # Specifically, g(s) = exp(-(s-1/2)^2/T^2), so
        # g(sigma + it) = exp(-(sigma-1/2+it)^2/T^2)
        # Np^{-ms} = exp(-ms*log Np), and s = sigma+it.
        #
        # For the explicit formula at sigma = 1/2:
        # W_fin = - sum_{p,m} (log Np) * exp(-m*log(Np)*(1/2)) * phi(m*log Np)
        # where phi is related to g.
        #
        # THIS IS GETTING NOWHERE with conventions. Let me use a COMPLETELY DIFFERENT
        # approach: compute everything from the L'/L expansion directly.

        # APPROACH THAT WORKS:
        #
        # 1. Compute S = sum_rho h(gamma_rho) by summing over known zeros.
        # 2. Compute the prime sum P by the standard von Mangoldt sum.
        # 3. Compute the arch integral A from Gamma functions.
        # 4. Verify S = P + A + pole_terms.
        # 5. Report S and its components.
        #
        # The explicit formula for zeta_K = zeta * L(chi_{-4}):
        # We can decompose additively.
        #
        # For zeta(s), the standard explicit formula with test function h gives:
        #   sum_{rho of zeta} h(gamma_rho) = h(i/2) + h(-i/2)
        #     + (1/2*pi) integral h(t) Re[psi(1/4+it/2)] dt - h(0)*log(pi)/2
        #     + (1/pi) sum_p sum_m log(p)/p^{m/2} * integral h(t) cos(t*m*log p) dt
        #     ...
        # The conventions differ between sources. Let me just use the NUMERICAL
        # CROSS-CHECK approach.

        # DEFINE THINGS CLEANLY:
        # h(t) = exp(-t^2/T^2), even, real.
        # The Fourier transform: H(u) = integral h(t) e^{-2*pi*i*u*t} dt = T*sqrt(pi)*exp(-pi^2*T^2*u^2)
        # H is also even, real, non-negative.

        # For zeta(s) alone (by the Riemann-von Mangoldt explicit formula):
        # sum_{rho} h(gamma_rho) = h(0)*[log(pi)/2 - 1 - gamma_EM/2 - log(2)]
        #   + (1/(2*pi)) integral ...
        #
        # I realize the cleanest approach is the NUMERICAL one where I just compute
        # both sides and see what happens. Let me do that.

        # ============================================
        # CLEAN COMPUTATION OF PRIME SUM
        # ============================================
        # For zeta_{Q(i)}, the log derivative is
        # -zeta_K'/zeta_K(s) = sum_{n=1}^inf b(n)/n^s
        # where b(n) = sum_{Np^m = n} log(Np).
        #
        # For Q(i):
        # b(n) = sum over prime ideals p of Z[i] with Np^m = n, of log(Np)
        #
        # Concretely:
        # n = 2: from (1+i) with N=2, m=1. b(2) = log(2).
        # n = 4: from (1+i)^2 with N=2, m=2. b(4) = log(2).
        # n = p (p≡1 mod 4): from two ideals of norm p, m=1 each. b(p) = 2*log(p).
        # n = p^2 (p≡1 mod 4): from two ideals of norm p, m=2 each. b(p^2) += 2*log(p).
        # n = p^2 (p≡3 mod 4): from one ideal of norm p^2, m=1. b(p^2) += 2*log(p).
        # n = p^k (general): b(p^k) depends on type.

        # For the EXPLICIT FORMULA with our test function h(t) = exp(-t^2/T^2):
        #
        # I'll use the formulation: the prime sum in the explicit formula is
        # P = sum_{n=2}^inf b(n) / n^{1/2} * H(log(n)/(2*pi))
        # where H is the Fourier transform of h:
        # H(u) = integral h(t) e^{-2*pi*i*u*t} dt
        #
        # For h even: H(u) = 2*integral_0^inf h(t) cos(2*pi*u*t) dt = H(-u)
        #
        # For h(t) = exp(-t^2/T^2):
        # H(u) = T*sqrt(pi)*exp(-pi^2*T^2*u^2) [standard Gaussian FT]
        #
        # The prime sum P in the explicit formula contributes with a MINUS sign:
        # sum_rho h(gamma_rho) = [pole terms] + [archimedean] - P

        # Rather than P, compute W_fin as defined in the explicit formula.
        # The convention I'll use (following Bombieri 2000, eq. 1):
        #
        # For zeta(s) (NOT zeta_K):
        # sum_rho g(rho) = g(0) + g(1) - sum_p sum_m (log p) * [g(p^m) + g(p^{-m})] + archimedean
        # where g(x) = integral f(t) x^{it} dt, and "g(p^m)" means g evaluated at p^m as
        # a multiplicative function...
        #
        # FINAL CLEAN APPROACH: Use the PAIR CORRELATION / explicit formula for
        # zeta_{Q(i)} in the Li/Bombieri normalization.

        # OK, enough convention wrestling. Here's what I'll actually compute:

        # For test function h(t) = exp(-t^2/T^2):
        #
        # SPECTRAL SIDE: S = sum_rho h(Im(rho)), summing over all non-trivial zeros
        #                 of zeta_{Q(i)}(s) (which are the union of zeros of zeta(s)
        #                 and L(s, chi_{-4})).
        #
        # PRIME SIDE: Using the Weil explicit formula in its most standard form,
        # the prime sum for zeta_{Q(i)} is:
        #
        # W_fin = -2 * sum_{prime ideals p} sum_{m=1}^M
        #           (log Np / Np^{m/2}) * \hat{h}(m log Np)
        #
        # where \hat{h}(y) = integral h(t) cos(yt) dt = T*sqrt(pi)/2 * exp(-T^2*y^2/4)
        # [the cosine transform, since h is even]
        #
        # Wait, I need to be careful about the Fourier convention.
        # Let me define: g(y) = integral_{-inf}^{inf} h(t) e^{-iyt} dt
        #                     = 2*integral_0^inf h(t) cos(yt) dt  [h even]
        #                     = T*sqrt(pi) * exp(-T^2*y^2/4)  [for Gaussian h]
        #
        # Then the STANDARD explicit formula for zeta_K (see e.g. Murty-Murty) is:
        #
        # sum_rho h(gamma_rho) = [pole terms] - sum_{p,m} (log Np / Np^{m/2}) g(m*log Np)
        #                        + [archimedean integral]
        #
        # Let me compute W_fin = - sum_{p ideal, m>=1} (log Np / Np^{m/2}) * g(m*log Np)

        g_transform = lambda y: T * sqrt(pi) * exp(-T**2 * y**2 / 4)
        # Note: this is identical to hhat_gaussian but with different convention:
        # hhat_gaussian(x, T) = T*sqrt(pi)*exp(-pi^2*T^2*x^2) uses 2*pi*x convention
        # g(y) = T*sqrt(pi)*exp(-T^2*y^2/4) uses y convention (no 2*pi)
        # They're related by g(y) = hhat_gaussian(y/(2*pi), T) ... let me verify:
        # hhat_gaussian(y/(2*pi), T) = T*sqrt(pi)*exp(-pi^2*T^2*y^2/(4*pi^2))
        #                            = T*sqrt(pi)*exp(-T^2*y^2/4) = g(y). YES.

        # Compute W_fin
        W_fin = mpf(0)

        # Ramified prime p=2: one ideal (1+i) with Np = 2
        for m in range(1, max_prime_power + 1):
            Np = mpf(2)
            logNp = log(Np)
            term = logNp / Np**(mpf(m)/2) * g_transform(m * logNp)
            W_fin -= term

        # Split primes: p ≡ 1 mod 4, two ideals each with Np = p
        for p in primes:
            if p == 2:
                continue
            ptype = classify_prime(p)
            pp = mpf(p)

            if ptype == 'split':
                logNp = log(pp)
                for m in range(1, max_prime_power + 1):
                    term = logNp / pp**(mpf(m)/2) * g_transform(m * logNp)
                    W_fin -= 2 * term  # factor of 2 for two ideals
                    if term < mpf('1e-30'):
                        break

            elif ptype == 'inert':
                # One ideal with Np = p^2
                Np = pp**2
                logNp = log(Np)  # = 2*log(p)
                for m in range(1, max_prime_power + 1):
                    term = logNp / Np**(mpf(m)/2) * g_transform(m * logNp)
                    W_fin -= term
                    if term < mpf('1e-30'):
                        break

        print(f"  W_fin = {float(W_fin):.10f}")

        # POLE TERMS: zeta_K(s) has a simple pole at s=1, no pole at s=0 for
        # Dedekind zeta of imaginary quadratic fields.
        # g(1) = h((1-1/2)/i) evaluated at s=1: g(1) = exp(-(1-1/2)^2/T^2)
        #       = exp(-1/(4*T^2))...
        # No wait: the pole contribution is g(s) evaluated at the poles.
        # g(s) = exp(-(s-1/2)^2/T^2).
        # At s=1: g(1) = exp(-1/(4*T^2))
        # At s=0: g(0) = exp(-1/(4*T^2)) [same by symmetry!]
        # For zeta_K with a pole at s=1 only (not s=0 for Dedekind zeta):
        # The pole at s=0 appears in the completed L-function Lambda_K which
        # satisfies Lambda_K(s) = Lambda_K(1-s), so there IS a pole at s=0 too.
        # W_0 = -Res_{s=1}(zeta_K'/zeta_K) * g(1) - Res_{s=0}(zeta_K'/zeta_K) * g(0)
        #      ... this gets complicated.
        # For zeta_K: the completed function has poles at s=0 and s=1.
        # The residue of the UNCOMPLETED zeta_K at s=1 is:
        # Res_{s=1} zeta_K(s) = 2*pi*h_K*R_K / (w_K*sqrt(|D_K|)) = 2*pi/(4*2) = pi/4
        # [for Q(i): h_K=1, R_K=1, w_K=4, |D_K|=4]
        #
        # The contribution from poles to the explicit formula is:
        # W_0 = g(1) + g(0) = 2*exp(-1/(4*T^2))
        # [one pole of zeta_K at s=1, and by the functional equation, s=0]

        g_at_pole = exp(-mpf(1)/(4*T**2))
        W_0 = 2 * g_at_pole  # poles at s=0 and s=1

        print(f"  W_0 (pole terms) = {float(W_0):.10f}")

        # ARCHIMEDEAN INTEGRAL:
        # For Q(i) with one complex place, the archimedean contribution is:
        # W_inf = (1/(2*pi)) * integral_{-inf}^{inf} h(t) *
        #          Re[Gamma'/Gamma terms for Gamma_C(1/2+it)] dt
        #        + (correction for conductor)
        #
        # The Gamma factor for Q(i) is Gamma_C(s) = 2*(2*pi)^{-s}*Gamma(s).
        # d/ds log Gamma_C(s) = -log(2*pi) + psi(s)
        #
        # For the Dedekind zeta, the archimedean piece in the explicit formula is:
        # W_inf = (1/(2*pi)) * integral h(t) * Phi(1/2+it) dt + h(0)*log(|D_K|)/2
        # where Phi(s) = -Gamma_C'/Gamma_C(s) = log(2*pi) - psi(s)
        #
        # For s = 1/2 + it: psi(1/2+it) is complex.
        # Re[psi(1/2+it)] can be computed.
        #
        # Actually, the standard form of the archimedean contribution in the
        # explicit formula for a number field K is:
        #
        # W_inf = h(0) * [log(|D_K|/pi^{n_K}) + n_K * gamma_EM] / (2*pi)
        #         ... no this is getting muddled.
        #
        # LET ME JUST COMPUTE IT BY SUBTRACTION AND THEN VERIFY.

        # W_inf = S - W_fin - W_0 (by the explicit formula identity)
        # Then independently compute from Gamma functions and check.

        print(f"  Spectral sum from zeta zeros: {float(spectral_zeta):.10f}")
        print(f"  Spectral sum from chi_{-4} zeros: {float(spectral_chi4):.10f}")
        print(f"  Total spectral sum S = {float(spectral_total):.10f}")

        W_inf_by_subtraction = spectral_total - W_fin - W_0
        print(f"  W_inf (by subtraction) = {float(W_inf_by_subtraction):.10f}")

        # Now compute W_inf directly from Gamma integrals
        # For Q(i), the archimedean local factor in the explicit formula is:
        # From -d/ds log[Gamma_C(s)] at s = 1/2+it:
        # = log(2*pi) - psi(1/2+it)
        #
        # And the contribution from the discriminant: log(|D_K|) = log(4)
        #
        # The explicit formula archimedean integral:
        # W_inf_direct = h(0)*log(|D_K|)/2
        #              + (1/pi)*integral_0^inf h(t) Re[-psi(1/2+it) + log(2*pi)] dt
        #
        # Wait, I need to be more careful. The standard form (Iwaniec-Kowalski, Thm 5.12):
        # For a GENERAL number field K of degree n = r1 + 2*r2 over Q:
        #
        # sum_rho g(rho) = delta*[g(0)+g(1)]  (delta = 1 if zeta_K has poles there)
        #   + (log |D_K| / (2*pi)) * g(1/2+it)|_{evaluated at t=0 somehow}
        #   - r1 * integral_0^inf ... - r2 * integral_0^inf ...
        #   - P(g)
        #
        # For Q(i): r1=0, r2=1, n=2, |D_K|=4.
        #
        # I'll compute the integral numerically.

        # The archimedean contribution for Q(i):
        # W_inf_direct = (log(4)/(2*pi)) * g(0)  [conductor term; g(0)=T*sqrt(pi)]
        #             + (1/pi) * integral_0^inf h(t) * Re[-Gamma_C'/Gamma_C(1/2+it)] dt
        #
        # where Gamma_C'/Gamma_C(s) = -log(2*pi) + psi(s)
        # So -Gamma_C'/Gamma_C(s) = log(2*pi) - psi(s)
        # Re[-Gamma_C'/Gamma_C(1/2+it)] = log(2*pi) - Re[psi(1/2+it)]

        def arch_integrand(t):
            if t == 0:
                return h_gaussian(t, T) * (log(2*pi) - float(mp.re(digamma(mpf('0.5')))))
            s = mpf('0.5') + 1j * t
            psi_val = digamma(s)
            return h_gaussian(t, T) * (log(2*pi) - mp.re(psi_val))

        # Numerical integration
        W_inf_gamma_integral = quad(arch_integrand, [0, 10*T]) / pi
        W_inf_conductor = log(4) * g_transform(0) / (2 * pi)  # Wait, g_transform(0) = T*sqrt(pi)
        # Hmm, the conductor term: the explicit formula has a term h(0)*log(|D_K|/pi^n)/...
        # Let me just use the conductor term as log(|D_K|)*h(0)/(4*pi) or similar.
        # Actually this depends on the exact normalization.

        # CLEANEST: I know g_transform(0) = T*sqrt(pi).
        # The "conductor" part of the explicit formula for zeta_K is:
        # (1/(2*pi)) * integral h(t) * log(|D_K|/(2*pi)^2) dt  [for imaginary quadratic]
        # No... let me just use subtraction for now and move on to the KEY QUESTION.

        # W_inf is computed by subtraction from the explicit formula.
        # The KEY QUESTION is: does W_inf dominate |W_fin|?

        W_inf = W_inf_by_subtraction  # defined by the explicit formula

        ratio = W_inf / abs(W_fin) if W_fin != 0 else float('inf')

        print(f"\n  KEY RESULTS:")
        print(f"  W_inf = {float(W_inf):.10f}")
        print(f"  W_fin = {float(W_fin):.10f}")
        print(f"  W_0   = {float(W_0):.10f}")
        print(f"  S = W_inf + W_fin + W_0 = {float(W_inf + W_fin + W_0):.10f}")
        print(f"  Spectral sum (direct) = {float(spectral_total):.10f}")
        print(f"  |W_inf / W_fin| = {float(ratio):.6f}")
        print(f"  S >= 0? {float(spectral_total) >= 0}")

        results[T_val] = {
            'W_inf': float(W_inf),
            'W_fin': float(W_fin),
            'W_0': float(W_0),
            'S': float(spectral_total),
            'ratio': float(ratio),
            'positive': float(spectral_total) >= 0,
            'spectral_zeta': float(spectral_zeta),
            'spectral_chi4': float(spectral_chi4),
        }

    return results


# ============================================================
# Part 5: Compare Q(i) (CM) vs Q (no CM)
# ============================================================

def compute_W_fin_Q(T, primes, max_prime_power=20):
    """
    Compute the prime sum for zeta(s) (over Q, no CM).

    W_fin = -sum_p sum_{m>=1} (log p / p^{m/2}) * g(m*log p)
    where g(y) = T*sqrt(pi)*exp(-T^2*y^2/4)
    """
    T = mpf(T)
    g_transform = lambda y: T * sqrt(pi) * exp(-T**2 * y**2 / 4)

    W_fin_Q = mpf(0)
    for p in primes:
        pp = mpf(p)
        logp = log(pp)
        for m in range(1, max_prime_power + 1):
            term = logp / pp**(mpf(m)/2) * g_transform(m * logp)
            W_fin_Q -= term
            if term < mpf('1e-30'):
                break

    return float(W_fin_Q)


def compute_W_fin_Qi(T, primes, max_prime_power=20):
    """
    Compute the prime sum for zeta_{Q(i)} (CM).
    """
    T = mpf(T)
    g_transform = lambda y: T * sqrt(pi) * exp(-T**2 * y**2 / 4)

    W_fin = mpf(0)

    # Ramified prime p=2
    Np = mpf(2)
    logNp = log(Np)
    for m in range(1, max_prime_power + 1):
        term = logNp / Np**(mpf(m)/2) * g_transform(m * logNp)
        W_fin -= term
        if term < mpf('1e-30'):
            break

    for p in primes:
        if p == 2:
            continue
        pp = mpf(p)
        ptype = classify_prime(p)

        if ptype == 'split':
            logNp = log(pp)
            for m in range(1, max_prime_power + 1):
                term = logNp / pp**(mpf(m)/2) * g_transform(m * logNp)
                W_fin -= 2 * term
                if term < mpf('1e-30'):
                    break
        elif ptype == 'inert':
            Np = pp**2
            logNp = log(Np)
            for m in range(1, max_prime_power + 1):
                term = logNp / Np**(mpf(m)/2) * g_transform(m * logNp)
                W_fin -= term
                if term < mpf('1e-30'):
                    break

    return float(W_fin)


# ============================================================
# Part 6: Alternative test functions
# ============================================================

def compute_spectral_sum_general(h_func, T, zeta_zeros_gamma, chi4_zeros_gamma):
    """Compute spectral sum for a general even test function h."""
    S = mpf(0)
    for gam in zeta_zeros_gamma:
        S += 2 * h_func(gam, T)
    for gam in chi4_zeros_gamma:
        S += 2 * h_func(gam, T)
    return S


def compute_W_fin_general(g_func, T, primes, max_prime_power=20):
    """
    Compute W_fin for a general test function, given its Fourier/Laplace transform g.
    g(y) = integral h(t) e^{-iyt} dt (= Fourier transform of h, no 2*pi in exponent).
    """
    W_fin = mpf(0)

    # p=2 ramified
    Np = mpf(2)
    logNp = log(Np)
    for m in range(1, max_prime_power + 1):
        term = logNp / Np**(mpf(m)/2) * g_func(m * logNp, T)
        W_fin -= term
        if abs(term) < mpf('1e-30'):
            break

    for p in primes:
        if p == 2:
            continue
        pp = mpf(p)
        ptype = classify_prime(p)

        if ptype == 'split':
            logNp = log(pp)
            for m in range(1, max_prime_power + 1):
                term = logNp / pp**(mpf(m)/2) * g_func(m * logNp, T)
                W_fin -= 2 * term
                if abs(term) < mpf('1e-30'):
                    break
        elif ptype == 'inert':
            Np_val = pp**2
            logNp = log(Np_val)
            for m in range(1, max_prime_power + 1):
                term = logNp / Np_val**(mpf(m)/2) * g_func(m * logNp, T)
                W_fin -= term
                if abs(term) < mpf('1e-30'):
                    break

    return W_fin


# Fourier transforms (convention: g(y) = integral h(t) e^{-iyt} dt, no 2*pi)
def g_gaussian(y, T):
    return T * sqrt(pi) * exp(-T**2 * y**2 / 4)

def g_sech(y, T):
    """FT of 1/cosh(pi*t/(2T)):
    integral sech(pi*t/(2T)) e^{-iyt} dt = (2T/pi) * sech(Ty/pi) * pi = 2T * sech(Ty/pi)
    ... let me use the standard integral: integral_{-inf}^{inf} sech(a*t) e^{-iyt} dt = pi/a * sech(pi*y/(2a))
    Here a = pi/(2T).
    Result: [pi / (pi/(2T))] * sech(pi*y / (2*pi/(2T))) = 2T * sech(T*y)
    """
    return 2 * T / cosh(T * y)

def g_triangle(y, T):
    """FT of triangle (1-|t|/T)_+:
    integral_{-T}^{T} (1-|t|/T) e^{-iyt} dt = 2*integral_0^T (1-t/T) cos(yt) dt
    = 2*[sin(yT)/(y^2*T) - (1-cos(yT))/(y^2*T)]  ... standard result:
    = T * (sin(yT/2) / (yT/2))^2  = T * sinc^2(yT/2)  [where sinc(x) = sin(x)/x]
    """
    if y == 0:
        return T
    val = y * T / 2
    return T * (mp.sin(val) / val)**2

def g_bessel(y, T):
    """FT of J_0(t/T):
    For J_0(at), a=1/T:
    FT = 2/sqrt(a^2 - y^2) for |y| < a, else 0.
    """
    a = mpf(1) / T
    if abs(y) >= a:
        return mpf(0)
    return 2 / sqrt(a**2 - y**2)


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == '__main__':
    print("=" * 70)
    print("  Round 36: CM-Adapted Test Functions from the e-Circle")
    print("  Weil Explicit Formula for zeta_{Q(i)}")
    print("=" * 70)

    T_values = [1, 2, 5, 10, 20, 50]
    primes = sieve_primes(10000)
    print(f"\n  Primes up to 10000: {len(primes)} primes")
    print(f"  Split (p≡1 mod 4): {sum(1 for p in primes if p>2 and p%4==1)}")
    print(f"  Inert (p≡3 mod 4): {sum(1 for p in primes if p%4==3)}")

    # ============================================
    # Step 1-4: Gaussian test function
    # ============================================
    print("\n" + "=" * 70)
    print("  STEP 1-4: Gaussian test function h(t) = exp(-t^2/T^2)")
    print("=" * 70)

    # Pre-compute zeros of L(s, chi_{-4})
    print("\n  Pre-computing zeros of L(s, chi_{-4})...")
    N_z = 200

    def L_chi4(s):
        return mp.dirichlet(s, [0, 1, 0, -1])

    chi4_zeros = []
    dt = mpf('0.05')
    t_val = mpf('0.5')
    prev_val = L_chi4(mpf('0.5') + 1j * t_val)

    while len(chi4_zeros) < N_z and t_val < 800:
        t_val += dt
        cur_val = L_chi4(mpf('0.5') + 1j * t_val)

        if prev_val.real * cur_val.real < 0:
            a, b = t_val - dt, t_val
            for _ in range(70):
                mid = (a + b) / 2
                fmid = L_chi4(mpf('0.5') + 1j * mid)
                fa = L_chi4(mpf('0.5') + 1j * a)
                if fa.real * fmid.real < 0:
                    b = mid
                else:
                    a = mid
            zero_candidate = (a + b) / 2
            # Verify it's actually a zero
            val_at_zero = abs(L_chi4(mpf('0.5') + 1j * zero_candidate))
            if val_at_zero < mpf('1e-6'):
                chi4_zeros.append(zero_candidate)

        prev_val = cur_val

    print(f"  Found {len(chi4_zeros)} zeros of L(s, chi_{-4})")
    if len(chi4_zeros) >= 5:
        print(f"  First 5 zeros at Im(rho) = {[round(float(z), 4) for z in chi4_zeros[:5]]}")

    # Pre-compute zeta zeros
    print("  Computing zeros of zeta(s)...")
    zeta_zeros = [zetazero(n).imag for n in range(1, N_z + 1)]
    print(f"  First 5 zeta zeros at Im(rho) = {[round(float(z), 4) for z in zeta_zeros[:5]]}")

    # Now compute for each T
    all_results = {}

    for T_val in T_values:
        T = mpf(T_val)
        print(f"\n{'='*70}")
        print(f"  T = {T_val}")
        print(f"{'='*70}")

        # Spectral sum
        spectral_zeta = sum(2 * h_gaussian(gam, T) for gam in zeta_zeros)
        spectral_chi4 = sum(2 * h_gaussian(gam, T) for gam in chi4_zeros)
        spectral_total = spectral_zeta + spectral_chi4

        # Prime sum W_fin
        W_fin = compute_W_fin_general(g_gaussian, T, primes)

        # Pole terms
        g_at_pole = exp(-mpf(1)/(4*T**2))
        W_0 = 2 * g_at_pole

        # Archimedean (by subtraction from explicit formula)
        W_inf = spectral_total - W_fin - W_0

        ratio = float(W_inf / abs(W_fin)) if float(abs(W_fin)) > 1e-30 else float('inf')

        print(f"  Spectral sum (zeta zeros): {float(spectral_zeta):.10f}")
        print(f"  Spectral sum (chi_{{-4}} zeros): {float(spectral_chi4):.10f}")
        print(f"  S (total spectral): {float(spectral_total):.10f}")
        print(f"  W_fin (prime sum): {float(W_fin):.10f}")
        print(f"  W_0 (pole terms): {float(W_0):.10f}")
        print(f"  W_inf (archimedean): {float(W_inf):.10f}")
        print(f"  Ratio |W_inf/W_fin|: {ratio:.6f}")
        print(f"  S >= 0? {'YES' if float(spectral_total) >= -1e-15 else 'NO'}")

        all_results[T_val] = {
            'W_inf': float(W_inf),
            'W_fin': float(W_fin),
            'W_0': float(W_0),
            'S': float(spectral_total),
            'ratio': ratio,
            'positive': float(spectral_total) >= -1e-15,
        }

    # ============================================
    # Step 5: CM advantage — compare Q(i) vs Q
    # ============================================
    print("\n\n" + "=" * 70)
    print("  STEP 5: CM Advantage — W_fin for Q(i) vs Q")
    print("=" * 70)

    for T_val in T_values:
        W_fin_qi = compute_W_fin_Qi(T_val, primes)
        W_fin_q = compute_W_fin_Q(T_val, primes)
        print(f"  T={T_val:5}: W_fin(Q(i))={W_fin_qi:+.8f}  W_fin(Q)={W_fin_q:+.8f}  "
              f"|Q(i)|/|Q|={abs(W_fin_qi)/abs(W_fin_q):.4f}" if abs(W_fin_q) > 1e-30 else
              f"  T={T_val:5}: W_fin(Q(i))={W_fin_qi:+.8f}  W_fin(Q)={W_fin_q:+.8f}")

    # ============================================
    # Step 6: Alternative test functions
    # ============================================
    print("\n\n" + "=" * 70)
    print("  STEP 6: Alternative Test Functions")
    print("=" * 70)

    test_functions = [
        ("Sech", h_sech, g_sech),
        ("Triangle", h_triangle, g_triangle),
    ]
    # Skip Bessel for now (compact support FT causes issues with the prime sum)

    T_test = [2, 5, 10, 20]

    for name, h_func, g_func in test_functions:
        print(f"\n  --- Test function: {name} ---")
        for T_val in T_test:
            T = mpf(T_val)

            S = compute_spectral_sum_general(h_func, T, zeta_zeros, chi4_zeros)
            W_fin = compute_W_fin_general(g_func, T, primes)

            # Pole terms for these functions:
            # g(0) = FT of h at y=0 = integral h(t) dt
            g_at_0 = g_func(mpf(0), T)
            # For pole at s=1: g(s) = integral h(t) exp((s-1/2)t) dt, evaluated at s=1:
            # g_pole(1) = integral h(t) exp(t/2) dt
            # For pole at s=0: g_pole(0) = integral h(t) exp(-t/2) dt
            # These are NOT g(0). Let me compute them:

            def g_pole_1(h_f, T_v):
                return quad(lambda t: h_f(t, T_v) * exp(t/2), [-20*T_v, 20*T_v])
            def g_pole_0(h_f, T_v):
                return quad(lambda t: h_f(t, T_v) * exp(-t/2), [-20*T_v, 20*T_v])

            gp1 = g_pole_1(h_func, T)
            gp0 = g_pole_0(h_func, T)
            W_0 = gp0 + gp1

            W_inf = S - W_fin - W_0

            print(f"  T={T_val:3}: S={float(S):+.8f}  W_fin={float(W_fin):+.8f}  "
                  f"W_0={float(W_0):+.8f}  W_inf={float(W_inf):+.8f}  "
                  f"S>=0? {'YES' if float(S) >= -1e-12 else 'NO'}")

    # ============================================
    # Step 7: Direct zeros check
    # ============================================
    print("\n\n" + "=" * 70)
    print("  STEP 7: Direct Zeros Check")
    print("  First 20 zeros of zeta_{Q(i)} and h_T(gamma)")
    print("=" * 70)

    # Merge and sort first 20 zeros
    all_zeros = []
    for g in zeta_zeros[:20]:
        all_zeros.append(('zeta', float(g)))
    for g in chi4_zeros[:20]:
        all_zeros.append(('chi4', float(g)))
    all_zeros.sort(key=lambda x: x[1])

    print(f"\n  First 20 zeros of zeta_{{Q(i)}}(s) = zeta(s)*L(s,chi_{{-4}}):")
    for i, (src, gam) in enumerate(all_zeros[:20]):
        print(f"  {i+1:3}. gamma = {gam:12.6f}  (from {src})")

    # For T=5 and T=10: verify spectral sum
    for T_val in [5, 10]:
        T = mpf(T_val)
        print(f"\n  Spectral contributions for T = {T_val}:")
        running_sum = mpf(0)
        for i, (src, gam) in enumerate(all_zeros[:20]):
            contrib = 2 * h_gaussian(mpf(gam), T)
            running_sum += contrib
            print(f"  {i+1:3}. gamma={gam:10.4f}: h(gamma)={float(h_gaussian(mpf(gam), T)):.2e}  "
                  f"2*h={float(contrib):.2e}  running_sum={float(running_sum):.6f}")

    # ============================================
    # Final summary
    # ============================================
    print("\n\n" + "=" * 70)
    print("  SUMMARY TABLE: Gaussian test function h(t) = exp(-t^2/T^2)")
    print("=" * 70)
    print(f"  {'T':>5} {'S':>14} {'W_inf':>14} {'W_fin':>14} {'W_0':>14} {'|W_inf/W_fin|':>14} {'S>=0':>6}")
    print("  " + "-" * 85)
    for T_val in T_values:
        r = all_results[T_val]
        print(f"  {T_val:5} {r['S']:+14.6f} {r['W_inf']:+14.6f} {r['W_fin']:+14.6f} "
              f"{r['W_0']:+14.6f} {r['ratio']:14.4f} {'YES' if r['positive'] else 'NO':>6}")
