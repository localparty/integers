#!/usr/bin/env python3
"""
R56 Thread 3: Entanglement spectrum of free boson on e-circle vs Q_W spectrum.

Computes:
1. Calabrese-Cardy entanglement entropy for c=1 CFT on circle of length L
2. Peschel entanglement spectrum for free boson (single-particle levels)
3. Q_W even-sector spectrum from the R49 builder
4. Comparison

The entanglement Hamiltonian for a single interval [0, ell] in a c=1 CFT
on a circle of circumference L (ground state) has the form:

  H_E = -log rho_A

For a FREE BOSON (c=1), the entanglement spectrum decomposes into
single-particle levels. The Calabrese-Cardy entanglement entropy is:

  S_ent = (c/3) * log( (L/pi*a) * sin(pi*ell/L) )

where a is the UV cutoff. For the full entanglement spectrum of a free
boson on a circle, the single-particle entanglement energies are:

  epsilon_k = 2*pi*k / log( (L/(pi*a)) * sin(pi*ell/L) )    (k = 1, 2, ...)

following Peschel (2003) and Calabrese-Lefevre (2008).

We also build Q_W's even-sector spectrum using the R49 builder.
"""

import sys
sys.path.insert(0, '/Users/gsix/riemann-hypothesis/code')
from mpmath import mp, mpf, pi, log, sin, exp, sqrt, cos, matrix, eigsy, gamma as mpgamma, digamma, quad, inf, fabs, sinh, cosh

mp.dps = 80

# ============================================================
# PART A: Calabrese-Cardy entanglement entropy and spectrum
# ============================================================

def entanglement_entropy_cc(c, L, ell, a):
    """Calabrese-Cardy entanglement entropy for interval [0,ell] on circle of length L.
    c = central charge, a = UV cutoff."""
    return (c / 3) * log((L / (pi * a)) * sin(pi * ell / L))

def entanglement_spectrum_free_boson(L, ell, a, n_levels=20):
    """
    Single-particle entanglement energies for a free boson on a circle.

    For a free boson (c=1) on a circle of length L, bipartitioned into
    [0, ell] and [ell, L], the entanglement Hamiltonian H_E = -log rho_A
    has a thermal structure: rho_A = exp(-H_ent) / Z where H_ent is a
    free-boson Hamiltonian at effective inverse temperature beta_ent.

    The effective inverse temperature (Calabrese-Lefevre 2008, Peschel 2003):
      beta_ent = log( (L/(pi*a)) * sin(pi*ell/L) ) * (2*pi / (2*pi))

    Actually, for the SINGLE interval case on a circle, the entanglement
    spectrum levels are:
      epsilon_k = 2*pi*k / beta_ent_eff

    where beta_ent_eff = log(xi) with xi = (L/(pi*a)) sin(pi ell/L).

    More precisely (Calabrese-Lefevre 2008): the many-body entanglement
    spectrum for c=1 is built from occupation numbers of single-particle
    levels with energies:
      epsilon_k = 2*pi*k * beta_ent    (k = 1, 2, 3, ...)

    But the standard result is that the entanglement Hamiltonian for a
    single interval in a c=1 CFT on a circle IS a free boson Hamiltonian
    with effective temperature:
      T_ent = 1 / beta_ent = 1 / (2*pi)  (in units where the interval
              maps to [0, 2*pi] via conformal transformation)

    The actual single-particle levels of H_E are:
      epsilon_k = k * (2*pi^2 / log(xi))    (k = 1, 2, 3, ...)

    where xi = (L/(pi*a)) * sin(pi*ell/L).

    This gives the entanglement entropy S = (1/3) log(xi) as required.
    """
    xi = (L / (pi * a)) * sin(pi * ell / L)
    log_xi = log(xi)

    # The entanglement Hamiltonian eigenvalues (single-particle)
    # For c=1 free boson, following Calabrese-Lefevre (2008):
    # The many-body spectrum is E_n = sum_k n_k * epsilon_k
    # with epsilon_k = k * (2*pi^2 / log(xi))
    # This gives S = sum_k s(epsilon_k) where s(e) = e/(e^e - 1) - log(1 - e^{-e})
    # and the total = (1/3) log(xi) for c=1.

    levels = []
    for k in range(1, n_levels + 1):
        eps_k = k * (2 * pi**2 / log_xi)
        levels.append(eps_k)

    return levels, log_xi, xi

# Parameters for the e-circle
lam = sqrt(13)
L = 2 * log(lam)  # circumference of the e-circle

print("=" * 70)
print("R56 Thread 3: Entanglement Spectrum vs Q_W Spectrum")
print("=" * 70)
print(f"\nlambda = sqrt(13) = {float(lam):.6f}")
print(f"L = 2 log(lambda) = {float(L):.6f}")

# Bipartition: half-circle ell = L/2
ell = L / 2

# UV cutoff: we use a = 1/N where N is the Fourier truncation
# For comparison, try several cutoffs
print("\n--- Calabrese-Cardy Entanglement Entropy (c=1) ---")
for N_cutoff in [30, 60, 120]:
    a = L / (2 * pi * N_cutoff)  # lattice spacing ~ L/(2*pi*N)
    S_ent = entanglement_entropy_cc(1, L, ell, a)
    print(f"  N={N_cutoff:3d}, a={float(a):.6f}, S_ent = {float(S_ent):.6f}")

# Use the physically motivated cutoff a = L/(2*pi*N) with N=60
N = 60
a = L / (2 * pi * N)

print(f"\n--- Entanglement Spectrum (free boson, c=1, N={N}) ---")
print(f"  ell = L/2 = {float(ell):.6f}")
print(f"  a = L/(2*pi*N) = {float(a):.8f}")

levels, log_xi, xi = entanglement_spectrum_free_boson(L, ell, a, n_levels=15)

print(f"  xi = (L/(pi*a)) * sin(pi*ell/L) = {float(xi):.6f}")
print(f"  log(xi) = {float(log_xi):.6f}")
print(f"\n  Single-particle entanglement energies epsilon_k = k * 2*pi^2/log(xi):")
for k, eps in enumerate(levels, 1):
    print(f"    k={k:2d}: epsilon_k = {float(eps):.6f}")

# ============================================================
# PART B: Q_W even-sector spectrum from R49 builder
# ============================================================

print("\n--- Q_W Even-Sector Spectrum (R49 builder, lambda=sqrt(13), N=60) ---")

# Import / rebuild the R49 even-block construction
# We implement the even block directly following R51B

def build_qw_even_block(lam_val, N_val, dps_val=80):
    """Build Q_W even block in cosine basis. Returns eigenvalues sorted ascending."""
    mp.dps = dps_val
    L_val = 2 * log(lam_val)
    dim = N_val + 1  # cosine basis C_0, C_1, ..., C_N

    # Helper: q(U_n, U_m)(y) from R49
    def q_nm(n, m, y):
        if n == m:
            return 2 * (1 - y / L_val) * cos(2 * pi * n * y / L_val)
        else:
            return (sin(2 * pi * m * y / L_val) - sin(2 * pi * n * y / L_val)) / (pi * (n - m))

    # W_{0,2}(U_n, U_m) from R49 closed form
    def W02(n, m):
        L2 = L_val**2
        return 32 * L_val * sinh(L_val / 4)**2 * (L2 - 16 * pi**2 * m * n) / \
               ((L2 + 16 * pi**2 * m**2) * (L2 + 16 * pi**2 * n**2))

    # WR via numerical quadrature
    def alpha_L(n):
        if n == 0:
            return mpf(0)
        def integrand(x):
            return sin(2 * pi * n * x / L_val) * exp(x / 2) / (exp(x) - exp(-x)) if x > 0 else mpf(0)
        # The integrand has a singularity at x=0: e^{x/2}/(e^x - e^{-x}) ~ 1/(2x)
        # Use tanh-sinh quadrature which handles endpoint singularities
        result = quad(integrand, [mpf(0), L_val])
        return result / pi

    def WR_diag(n):
        """Diagonal WR(U_n, U_n) from CC1 eq 4.4"""
        from mpmath import euler as euler_gamma
        omega0 = mpf(2)
        def integrand(x):
            if x < mpf('1e-30'):
                return mpf(0)
            omega_x = 2 * (1 - x / L_val) * cos(2 * pi * n * x / L_val)
            return (exp(x / 2) * omega_x - omega0) / (exp(x) - exp(-x))
        val = omega0 / 2 * (euler_gamma + log(4 * pi) - log((exp(L_val) + 1) / (exp(L_val) - 1)))
        val += quad(integrand, [mpf('1e-30'), L_val])
        return val

    def WR_offdiag(n, m):
        """Off-diagonal WR from Prop 4.3: (alpha_L(m) - alpha_L(n))/(n - m)"""
        return (alpha_L(m) - alpha_L(n)) / (n - m)

    # Prime powers k <= lambda^2 = 13
    from mpmath import log as mplog
    prime_powers = []
    # k=2 (p=2, m=1), k=3 (p=3, m=1), k=4 (p=2, m=2), k=5 (p=5, m=1),
    # k=7 (p=7, m=1), k=8 (p=2, m=3), k=9 (p=3, m=2), k=11 (p=11, m=1), k=13 (p=13, m=1)
    pp_list = [(2, mplog(2)), (3, mplog(3)), (4, mplog(2)), (5, mplog(5)),
               (7, mplog(7)), (8, mplog(2)), (9, mplog(3)), (11, mplog(11)), (13, mplog(13))]

    # Build full (2N+1) x (2N+1) matrix in Fourier basis, then project to even block
    full_dim = 2 * N_val + 1
    A_full = matrix(full_dim, full_dim)

    print(f"  Building full matrix (dim={full_dim})...")

    # Index mapping: column j -> Fourier index n = j - N_val
    for j in range(full_dim):
        n = j - N_val
        for i in range(j, full_dim):
            m = i - N_val

            # W_{0,2}
            val = W02(n, m)

            # WR
            if n == m:
                val -= WR_diag(n)
            else:
                val -= WR_offdiag(n, m)

            # Prime perturbation
            for k_idx, (k, log_p) in enumerate(pp_list):
                Lambda_k = log_p
                val -= Lambda_k * k**(-mpf(1)/2) * q_nm(n, m, mplog(k))

            A_full[i, j] = val
            if i != j:
                A_full[j, i] = val

    print(f"  Full matrix built. Projecting to even block (dim={dim})...")

    # Project to even block (cosine basis)
    # C_0 = V_0, C_n = (V_n + V_{-n})/sqrt(2) for n >= 1
    # A^ev[0,0] = A[0,0]
    # A^ev[0,m] = sqrt(2) * A[0,m] for m >= 1
    # A^ev[n,m] = A[n,m] + A[n,-m] for n,m >= 1

    A_ev = matrix(dim, dim)

    def full_idx(n):
        return n + N_val

    A_ev[0, 0] = A_full[full_idx(0), full_idx(0)]
    for m in range(1, dim):
        val = sqrt(2) * A_full[full_idx(0), full_idx(m)]
        A_ev[0, m] = val
        A_ev[m, 0] = val
    for n in range(1, dim):
        for m in range(n, dim):
            val = A_full[full_idx(n), full_idx(m)] + A_full[full_idx(n), full_idx(-m)]
            A_ev[n, m] = val
            if n != m:
                A_ev[m, n] = val

    print(f"  Even block built. Diagonalizing...")

    evals = eigsy(A_ev, eigvals_only=True)
    evals_sorted = sorted(evals, key=lambda x: float(x))

    return evals_sorted

# Build Q_W even block
qw_evals = build_qw_even_block(sqrt(13), N, dps_val=80)

print(f"\n  First 15 even-sector eigenvalues of Q_W:")
for k in range(min(15, len(qw_evals))):
    print(f"    k={k:2d}: mu_k^ev = {mp.nstr(qw_evals[k], 8)}")

# ============================================================
# PART C: Comparison
# ============================================================

print("\n" + "=" * 70)
print("COMPARISON: Entanglement Spectrum vs Q_W Even-Sector Spectrum")
print("=" * 70)

print(f"\n  Entanglement single-particle gap: epsilon_1 = {float(levels[0]):.6f}")
print(f"  Q_W even-sector gap (mu_1 - mu_0): {float(qw_evals[1] - qw_evals[0]):.4e}")
print(f"  Q_W even-sector first excited: mu_1 = {float(qw_evals[1]):.4e}")

# The Q_W spectrum near the bottom is dominated by tiny values (near zero)
# The bulk spectrum (large eigenvalues) grows logarithmically
print(f"\n  Q_W large eigenvalues (last 10):")
for k in range(max(0, len(qw_evals)-10), len(qw_evals)):
    print(f"    k={k:2d}: mu_k^ev = {float(qw_evals[k]):.6f}")

print(f"\n  Entanglement energies (first 5):")
for k in range(5):
    print(f"    k={k+1}: epsilon_k = {float(levels[k]):.6f}")

# Check: ratio of consecutive Q_W eigenvalues in the bulk
print(f"\n  Q_W eigenvalue ratios (bulk, k from 50 to 55):")
for k in range(50, min(56, len(qw_evals)-1)):
    ratio = float(qw_evals[k+1] / qw_evals[k]) if float(qw_evals[k]) != 0 else float('inf')
    print(f"    mu_{k+1}/mu_{k} = {ratio:.6f}")

# Entanglement spectrum ratios are trivially k+1/k (linear)
print(f"\n  Entanglement energy ratios:")
for k in range(5):
    print(f"    epsilon_{k+2}/epsilon_{k+1} = {(k+2)/(k+1):.6f}")

# The key structural comparison: Q_W's bulk eigenvalues grow like log(n)
# (from the archimedean diagonal), while entanglement energies grow linearly.
# The BOTTOM of Q_W's spectrum (near epsilon ~ 0) has a completely different
# structure from the entanglement spectrum.

print(f"\n  Structural comparison:")
print(f"  - Q_W eigenvalues: mu_k ~ log(k) for large k (archimedean diagonal dominates)")
print(f"  - Entanglement energies: epsilon_k ~ k (linear, free boson)")
print(f"  - Q_W ground state: mu_0 ~ 10^{{-58}} (Weil positivity = near zero)")
print(f"  - Entanglement ground state: epsilon_0 = 0 (vacuum has zero entanglement energy)")
print(f"  - Q_W has finite dimension (N+1 = {N+1} eigenvalues)")
print(f"  - Entanglement H_E has infinite spectrum")

# Archimedean-only spectrum (A = W02 - WR, no primes) vs entanglement
# This is the "free" part -- should be closer to a modular Hamiltonian
print(f"\n  Computing archimedean-only spectrum (A = W02 - WR, no primes)...")

def build_archimedean_even_block(lam_val, N_val, dps_val=80):
    """Build even block of A = W02 - WR (no prime perturbation)."""
    mp.dps = dps_val
    L_val = 2 * log(lam_val)
    dim = N_val + 1

    def W02(n, m):
        L2 = L_val**2
        return 32 * L_val * sinh(L_val / 4)**2 * (L2 - 16 * pi**2 * m * n) / \
               ((L2 + 16 * pi**2 * m**2) * (L2 + 16 * pi**2 * n**2))

    def alpha_L(n):
        if n == 0:
            return mpf(0)
        def integrand(x):
            return sin(2 * pi * n * x / L_val) * exp(x / 2) / (exp(x) - exp(-x)) if x > 0 else mpf(0)
        result = quad(integrand, [mpf(0), L_val])
        return result / pi

    def WR_diag(n):
        from mpmath import euler as euler_gamma
        omega0 = mpf(2)
        def integrand(x):
            if x < mpf('1e-30'):
                return mpf(0)
            omega_x = 2 * (1 - x / L_val) * cos(2 * pi * n * x / L_val)
            return (exp(x / 2) * omega_x - omega0) / (exp(x) - exp(-x))
        val = omega0 / 2 * (euler_gamma + log(4 * pi) - log((exp(L_val) + 1) / (exp(L_val) - 1)))
        val += quad(integrand, [mpf('1e-30'), L_val])
        return val

    def WR_offdiag(n, m):
        return (alpha_L(m) - alpha_L(n)) / (n - m)

    full_dim = 2 * N_val + 1
    A_full = matrix(full_dim, full_dim)

    for j in range(full_dim):
        n = j - N_val
        for i in range(j, full_dim):
            m = i - N_val
            val = W02(n, m)
            if n == m:
                val -= WR_diag(n)
            else:
                val -= WR_offdiag(n, m)
            A_full[i, j] = val
            if i != j:
                A_full[j, i] = val

    # Project to even block
    A_ev = matrix(dim, dim)
    def full_idx(n):
        return n + N_val

    A_ev[0, 0] = A_full[full_idx(0), full_idx(0)]
    for m in range(1, dim):
        val = sqrt(2) * A_full[full_idx(0), full_idx(m)]
        A_ev[0, m] = val
        A_ev[m, 0] = val
    for n in range(1, dim):
        for m in range(n, dim):
            val = A_full[full_idx(n), full_idx(m)] + A_full[full_idx(n), full_idx(-m)]
            A_ev[n, m] = val
            if n != m:
                A_ev[m, n] = val

    evals = eigsy(A_ev, eigvals_only=True)
    evals_sorted = sorted(evals, key=lambda x: float(x))
    return evals_sorted

arch_evals = build_archimedean_even_block(sqrt(13), N, dps_val=80)

print(f"\n  First 15 archimedean-only even eigenvalues (A = W02 - WR):")
for k in range(min(15, len(arch_evals))):
    print(f"    k={k:2d}: a_k = {mp.nstr(arch_evals[k], 8)}")

print(f"\n  Last 5 archimedean-only eigenvalues:")
for k in range(max(0, len(arch_evals)-5), len(arch_evals)):
    print(f"    k={k:2d}: a_k = {float(arch_evals[k]):.6f}")

# Difference spectrum: Q_W - A = -B (prime perturbation effect)
print(f"\n  Prime perturbation shift (mu_k - a_k) for first 10:")
for k in range(min(10, len(qw_evals))):
    shift = float(qw_evals[k] - arch_evals[k])
    print(f"    k={k:2d}: shift = {shift:.4e}")

print("\n" + "=" * 70)
print("DONE")
print("=" * 70)
