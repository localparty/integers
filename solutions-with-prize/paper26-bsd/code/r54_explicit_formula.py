"""R54 — Explicit-formula identity investigation.

Numerical investigation of the relationship between:
  epsilon_lambda = <xi | Q_W | xi> / <xi | xi>
and the Weil explicit formula:
  QW(f,f) = sum_rho |f_tilde(rho)|^2

where the sum is over nontrivial zeros rho = 1/2 + i*gamma_n of zeta.

Key questions:
1. Compute epsilon_lambda directly (should be ~10^{-dps})
2. Compute sum_rho |xi_hat(rho)|^2 for first K zeros
3. Decompose QW into W02 - WR - Wp and see if epsilon = 0 is a cancellation
4. Compare primes-only vs full-prime-powers to see what prime powers contribute
"""

import sys
import os
import time
import mpmath as mp

# Import from r49
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r49_fourier_circle import (
    build_QW, build_W02, build_WR, build_Wprimes,
    precompute_abc, eigh_mp, parity_projector_indices, parity_score,
    xi_hat, find_xi_hat_zero_near, von_mangoldt_terms,
    GAMMAS_50DIG
)


def compute_quadratic_form(M, vec):
    """Compute <vec | M | vec> for mpmath matrix M and list vec."""
    n = len(vec)
    result = mp.mpf(0)
    for i in range(n):
        for j in range(n):
            result += mp.conj(vec[i]) * M[i, j] * vec[j]
    return result


def compute_norm_sq(vec):
    """Compute <vec | vec>."""
    return sum(mp.conj(v) * v for v in vec)


def xi_mellin_at_rho(xi_coeffs, rho_im, L, N):
    """Compute xi_tilde(rho) where rho = 1/2 + i*gamma.

    The ground state xi lives on [0, L] with Fourier coefficients xi_j.
    xi(x) = sum_{|j|<=N} xi_j * exp(2*pi*i*j*x/L) / sqrt(L)

    The Mellin transform on [lambda^{-1}, lambda] with du/u measure:
    Under kappa: x = log(u) + L/2, so u = exp(x - L/2).

    xi_tilde(s) = int_{lambda^{-1}}^{lambda} xi(log u + L/2) u^{s-1} du/u
                = int_0^L xi(x) exp((s-1)(x - L/2)) dx   [u = exp(x-L/2), du/u = dx]
                = exp(-(s-1)L/2) int_0^L xi(x) exp((s-1)x) dx

    For s = 1/2 + i*gamma:
    xi_tilde(s) = exp(-(s-1)L/2) * sum_j xi_j / sqrt(L) * int_0^L exp(2*pi*i*j*x/L) exp((s-1)x) dx

    int_0^L exp((2*pi*i*j/L + s - 1)x) dx = [exp((2*pi*i*j/L + s-1)L) - 1] / (2*pi*i*j/L + s - 1)

    For s = 1/2 + i*gamma, s-1 = -1/2 + i*gamma:
    """
    s = mp.mpf('0.5') + mp.mpc(0, rho_im)
    s_minus_1 = s - 1  # = -1/2 + i*gamma

    prefactor = mp.exp(-s_minus_1 * L / 2)

    total = mp.mpc(0)
    for j in range(-N, N + 1):
        alpha_j = 2 * mp.pi * mp.mpc(0, 1) * j / L + s_minus_1
        if abs(alpha_j) < mp.mpf('1e-200'):
            # alpha_j ~ 0: integral = L
            integral = L
        else:
            integral = (mp.exp(alpha_j * L) - 1) / alpha_j
        total += xi_coeffs[j + N] * integral / mp.sqrt(L)

    return prefactor * total


def run_investigation():
    """Main R54 numerical investigation."""

    # ============================================================
    # PART 4a: Compute epsilon_lambda and the quadratic form pieces
    # ============================================================
    print("=" * 72)
    print("R54 — EXPLICIT FORMULA IDENTITY INVESTIGATION")
    print("=" * 72)

    DPS = 80
    N = 60
    mp.mp.dps = DPS
    lam = mp.sqrt(13)
    L = 2 * mp.log(lam)
    K_max = int(mp.floor(lam * lam + mp.mpf("1e-30")))

    print(f"\nConfiguration: lambda = sqrt(13), N = {N}, dps = {DPS}")
    print(f"L = {float(L):.6f}, K_max = {K_max}")

    # Build the full matrix
    print("\n--- Building full QW ---")
    A, L = build_QW(lam, N, dps=DPS, verbose=True)

    # Also build the three components separately
    print("\n--- Building components separately ---")
    W02 = build_W02(N, L)
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)
    Wp = build_Wprimes(N, L, K_max, verbose=True)

    # Diagonalize
    print("\n--- Diagonalizing ---")
    t0 = time.time()
    vals, Q = eigh_mp(A)
    print(f"  Done in {time.time()-t0:.1f}s")

    eps_N = vals[0]
    print(f"\n  epsilon_N (lowest eigenvalue) = {mp.nstr(eps_N, 20)}")

    pair = parity_projector_indices(N)
    chi = parity_score(Q.column(0), pair)
    print(f"  Parity of ground state: {chi:+.6f} ({'EVEN' if chi > 0.5 else 'ODD'})")

    # Extract ground state
    xi = [Q[i, 0] for i in range(2 * N + 1)]
    norm_sq = compute_norm_sq(xi)
    print(f"  ||xi||^2 = {mp.nstr(norm_sq, 12)}")

    # ============================================================
    # PART 4b: Decompose <xi|QW|xi> into components
    # ============================================================
    print("\n" + "=" * 72)
    print("PART 4b: QUADRATIC FORM DECOMPOSITION")
    print("=" * 72)

    qf_total = compute_quadratic_form(A, xi)
    qf_W02 = compute_quadratic_form(W02, xi)
    qf_WR = compute_quadratic_form(WR, xi)
    qf_Wp = compute_quadratic_form(Wp, xi)

    print(f"\n  <xi | QW | xi>  = {mp.nstr(mp.re(qf_total), 20)}")
    print(f"  <xi | W02 | xi> = {mp.nstr(mp.re(qf_W02), 20)}")
    print(f"  <xi | WR  | xi> = {mp.nstr(mp.re(qf_WR), 20)}")
    print(f"  <xi | Wp  | xi> = {mp.nstr(mp.re(qf_Wp), 20)}")
    print(f"\n  Check: W02 - WR - Wp = {mp.nstr(mp.re(qf_W02 - qf_WR - qf_Wp), 20)}")
    print(f"  Direct:               = {mp.nstr(mp.re(qf_total), 20)}")
    print(f"\n  Cancellation ratio: W02 / (WR + Wp) = {mp.nstr(mp.re(qf_W02) / mp.re(qf_WR + qf_Wp), 12)}")

    # ============================================================
    # PART 4c: Spectral side — sum_rho |xi_tilde(rho)|^2
    # ============================================================
    print("\n" + "=" * 72)
    print("PART 4c: SPECTRAL SIDE — sum_rho |xi_tilde(rho)|^2")
    print("=" * 72)

    n_zeros = 10
    print(f"\n  Computing xi_tilde(rho) for first {n_zeros} nontrivial zeros...")

    spectral_sum = mp.mpf(0)
    for k in range(n_zeros):
        gamma_k = mp.mpf(GAMMAS_50DIG[k])
        # Each zero rho = 1/2 + i*gamma contributes |xi_tilde(rho)|^2
        # The conjugate zero rho_bar = 1/2 - i*gamma also contributes the same
        # (since xi is real and even)
        xi_tilde_rho = xi_mellin_at_rho(xi, gamma_k, L, N)
        contrib = abs(xi_tilde_rho)**2
        # Factor of 2 for rho and rho_bar (conjugate pair)
        spectral_sum += 2 * contrib
        print(f"  rho_{k+1} = 1/2 + i*{float(gamma_k):.6f}:  "
              f"|xi_tilde|^2 = {mp.nstr(contrib, 8)},  "
              f"running sum (x2) = {mp.nstr(spectral_sum, 8)}")

    print(f"\n  Partial spectral sum (first {n_zeros} zero pairs) = {mp.nstr(spectral_sum, 12)}")
    print(f"  epsilon_N (from eigenvalue)                      = {mp.nstr(eps_N, 12)}")
    print(f"  <xi | QW | xi> (from quadratic form)             = {mp.nstr(mp.re(qf_total), 12)}")

    # ============================================================
    # PART 4d: Primes-only vs full prime powers
    # ============================================================
    print("\n" + "=" * 72)
    print("PART 4d: PRIMES-ONLY vs FULL PRIME POWERS")
    print("=" * 72)

    # Build primes-only version (k in {2,3,5,7,11,13} only, no prime powers)
    pp_full = von_mangoldt_terms(K_max)
    primes_only = [(k, p) for (k, p) in pp_full if k == p]
    prime_powers_only = [(k, p) for (k, p) in pp_full if k != p]

    print(f"  Full prime powers: {[k for k,p in pp_full]}")
    print(f"  Primes only:      {[k for k,p in primes_only]}")
    print(f"  Powers (not prime):{[k for k,p in prime_powers_only]}")

    # Build Wp for primes only
    def build_Wprimes_custom(N, L, terms):
        """Build Wp matrix from a custom list of (k, p) terms."""
        twopi_over_L = 2 * mp.pi / L
        M = mp.matrix(2 * N + 1)
        for (k, p) in terms:
            logp = mp.log(p)
            coeff = logp / mp.sqrt(mp.mpf(k))
            y = mp.log(k)
            one_minus_yL = 1 - y / L
            for i in range(2 * N + 1):
                n = i - N
                ang_n = twopi_over_L * n * y
                cos_n = mp.cos(ang_n)
                sin_n = mp.sin(ang_n)
                # Diagonal
                M[i, i] += coeff * 2 * one_minus_yL * cos_n
                # Off-diagonal
                for j in range(i + 1, 2 * N + 1):
                    m = j - N
                    ang_m = twopi_over_L * m * y
                    sin_m = mp.sin(ang_m)
                    val = coeff * (sin_m - sin_n) / (mp.pi * (n - m))
                    M[i, j] += val
                    M[j, i] += val
        return M

    # Build full QW with primes only
    Wp_primes = build_Wprimes_custom(N, L, primes_only)
    A_primes = mp.matrix(2 * N + 1)
    for i in range(2 * N + 1):
        for j in range(2 * N + 1):
            A_primes[i, j] = W02[i, j] - WR[i, j] - Wp_primes[i, j]
    # Symmetrize
    for i in range(2 * N + 1):
        for j in range(i + 1, 2 * N + 1):
            avg = (A_primes[i, j] + A_primes[j, i]) / 2
            A_primes[i, j] = avg
            A_primes[j, i] = avg

    vals_p, Q_p = eigh_mp(A_primes)
    eps_primes = vals_p[0]

    # Build contribution from prime powers (4, 8, 9)
    Wp_powers = build_Wprimes_custom(N, L, prime_powers_only)

    xi_p = [Q_p[i, 0] for i in range(2 * N + 1)]
    qf_powers_on_primegs = compute_quadratic_form(Wp_powers, xi_p)

    print(f"\n  epsilon (primes only): {mp.nstr(eps_primes, 12)}")
    print(f"  epsilon (full):       {mp.nstr(eps_N, 12)}")
    print(f"  <xi_primes | Wp_powers | xi_primes> = {mp.nstr(mp.re(qf_powers_on_primegs), 12)}")

    # Per-prime-power contribution to the quadratic form (evaluated on FULL ground state)
    print(f"\n  Per-prime-power <xi_full | W_k | xi_full>:")
    for (k, p) in pp_full:
        Wk = build_Wprimes_custom(N, L, [(k, p)])
        qfk = compute_quadratic_form(Wk, xi)
        print(f"    k={k:3d} (p={p}):  <xi|W_k|xi> = {mp.nstr(mp.re(qfk), 12)}")

    # ============================================================
    # PART 4e: The truncation effect
    # ============================================================
    print("\n" + "=" * 72)
    print("PART 4e: TRUNCATION — QW AT FINITE lambda vs INFINITE")
    print("=" * 72)

    # The key question: at finite lambda, QW only includes primes up to lambda^2.
    # The spectral side sum_rho |xi_tilde(rho)|^2 is INFINITE (all zeros).
    # But QW_lambda only sees finitely many primes.
    # So QW_lambda(xi, xi) != full sum_rho |xi_tilde(rho)|^2.
    # QW_lambda(xi, xi) = W02(xi) - WR(xi) - sum_{k <= lambda^2} Wp_k(xi)
    # The FULL Weil explicit formula would be:
    # sum_rho |xi_tilde(rho)|^2 = W02(xi) - WR(xi) - sum_{ALL k} Wp_k(xi)
    # So QW_lambda(xi, xi) = sum_rho |xi_tilde(rho)|^2 + sum_{k > lambda^2} Wp_k(xi)
    # i.e., QW_lambda = spectral_sum + tail_correction

    # The tail correction involves prime powers k > lambda^2 = 13.
    # Let's estimate the tail by adding a few more prime powers.

    # Compute Wp for k in {16, 17, 19, 23, 25, 27, 29, 31, 32, ...} up to some cutoff
    K_extended = 100
    pp_tail = [(k, p) for (k, p) in von_mangoldt_terms(K_extended) if k > K_max]

    if pp_tail:
        print(f"\n  Tail prime powers (k > {K_max}, up to {K_extended}):")
        print(f"  {[k for k,p in pp_tail[:20]]}{'...' if len(pp_tail)>20 else ''}")

        Wp_tail = build_Wprimes_custom(N, L, pp_tail)
        qf_tail = compute_quadratic_form(Wp_tail, xi)
        print(f"  <xi | Wp_tail | xi> = {mp.nstr(mp.re(qf_tail), 12)}")
        print(f"\n  QW_lambda(xi,xi)                    = {mp.nstr(mp.re(qf_total), 12)}")
        print(f"  QW_lambda(xi,xi) - Wp_tail(xi,xi)   = {mp.nstr(mp.re(qf_total) - mp.re(qf_tail), 12)}")
        print(f"  (This would be QW with primes up to {K_extended})")

    print("\n" + "=" * 72)
    print("INVESTIGATION COMPLETE")
    print("=" * 72)


if __name__ == "__main__":
    run_investigation()
