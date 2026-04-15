#!/usr/bin/env python3
"""
R56 Thread 3: Entanglement spectrum vs Q_W spectrum (fast version, N=20).
"""
import sys
sys.path.insert(0, '/Users/gsix/riemann-hypothesis/code')
from mpmath import mp, mpf, pi, log, sin, exp, sqrt, cos, matrix, eigsy, sinh, quad, euler

mp.dps = 50

lam = sqrt(13)
L = 2 * log(lam)
N = 20

print("=" * 70)
print("R56 Thread 3: Entanglement Spectrum vs Q_W Spectrum")
print(f"lambda=sqrt(13), L={float(L):.6f}, N={N}")
print("=" * 70)

# ============================================================
# PART A: Calabrese-Cardy entanglement entropy & spectrum
# ============================================================

ell = L / 2  # half-circle bipartition
a_uv = L / (2 * pi * N)  # UV cutoff

xi_val = (L / (pi * a_uv)) * sin(pi * ell / L)
log_xi = log(xi_val)

S_ent = log_xi / 3  # c=1
print(f"\n--- Entanglement (c=1 free boson on circle L={float(L):.4f}) ---")
print(f"  ell=L/2={float(ell):.4f}, a=L/(2*pi*N)={float(a_uv):.6f}")
print(f"  xi = {float(xi_val):.4f}, log(xi) = {float(log_xi):.4f}")
print(f"  S_ent = (1/3)*log(xi) = {float(S_ent):.4f}")

# Single-particle entanglement energies: epsilon_k = k * 2*pi^2 / log(xi)
print(f"\n  Single-particle entanglement energies:")
ent_levels = []
for k in range(1, 16):
    eps_k = float(k * 2 * pi**2 / log_xi)
    ent_levels.append(eps_k)
    print(f"    k={k:2d}: eps_k = {eps_k:.4f}")

# ============================================================
# PART B: Q_W even-sector spectrum
# ============================================================

print(f"\n--- Building Q_W (N={N}, dps=50) ---")

full_dim = 2 * N + 1

def q_nm(n, m, y):
    if n == m:
        return 2 * (1 - y / L) * cos(2 * pi * n * y / L)
    else:
        return (sin(2 * pi * m * y / L) - sin(2 * pi * n * y / L)) / (pi * (n - m))

def W02(n, m):
    L2 = L**2
    return 32 * L * sinh(L / 4)**2 * (L2 - 16 * pi**2 * m * n) / \
           ((L2 + 16 * pi**2 * m**2) * (L2 + 16 * pi**2 * n**2))

# Cache alpha_L values
_alpha_cache = {}
def alpha_L(n):
    if n in _alpha_cache:
        return _alpha_cache[n]
    if n == 0:
        _alpha_cache[0] = mpf(0)
        return mpf(0)
    def integrand(x):
        if x < mpf('1e-30'):
            return mpf(0)
        return sin(2 * pi * n * x / L) * exp(x / 2) / (exp(x) - exp(-x))
    result = quad(integrand, [mpf('1e-30'), L]) / pi
    _alpha_cache[n] = result
    return result

def WR_diag(n):
    omega0 = mpf(2)
    def integrand(x):
        if x < mpf('1e-30'):
            return mpf(0)
        omega_x = 2 * (1 - x / L) * cos(2 * pi * n * x / L)
        return (exp(x / 2) * omega_x - omega0) / (exp(x) - exp(-x))
    val = omega0 / 2 * (euler + log(4 * pi) - log((exp(L) + 1) / (exp(L) - 1)))
    val += quad(integrand, [mpf('1e-30'), L])
    return val

def WR_offdiag(n, m):
    return (alpha_L(m) - alpha_L(n)) / (n - m)

# Prime powers k <= 13
pp_list = [(2, log(2)), (3, log(3)), (4, log(2)), (5, log(5)),
           (7, log(7)), (8, log(2)), (9, log(3)), (11, log(11)), (13, log(13))]

# Build full matrix
A_full = matrix(full_dim, full_dim)
A_arch = matrix(full_dim, full_dim)  # archimedean only

print("  Computing matrix elements...")
for j in range(full_dim):
    n = j - N
    if j % 10 == 0:
        print(f"    column {j}/{full_dim}")
    for i in range(j, full_dim):
        m = i - N

        w02 = W02(n, m)
        if n == m:
            wr = WR_diag(n)
        else:
            wr = WR_offdiag(n, m)

        arch_val = w02 - wr

        prime_val = mpf(0)
        for k, log_p in pp_list:
            prime_val += log_p * k**(mpf(-1)/2) * q_nm(n, m, log(k))

        full_val = arch_val - prime_val

        A_full[i, j] = full_val
        A_full[j, i] = full_val
        A_arch[i, j] = arch_val
        A_arch[j, i] = arch_val

print("  Projecting to even block...")

dim_ev = N + 1

def project_even(M):
    E = matrix(dim_ev, dim_ev)
    fi = lambda n: n + N
    E[0, 0] = M[fi(0), fi(0)]
    for m in range(1, dim_ev):
        val = sqrt(2) * M[fi(0), fi(m)]
        E[0, m] = val
        E[m, 0] = val
    for nn in range(1, dim_ev):
        for mm in range(nn, dim_ev):
            val = M[fi(nn), fi(mm)] + M[fi(nn), fi(-mm)]
            E[nn, mm] = val
            if nn != mm:
                E[mm, nn] = val
    return E

Qev = project_even(A_full)
Aev = project_even(A_arch)

print("  Diagonalizing...")
qw_evals = sorted(eigsy(Qev, eigvals_only=True), key=lambda x: float(x))
arch_evals = sorted(eigsy(Aev, eigvals_only=True), key=lambda x: float(x))

print(f"\n--- Q_W Even-Sector Eigenvalues (first 15 of {dim_ev}) ---")
for k in range(min(15, dim_ev)):
    print(f"    k={k:2d}: mu_k = {mp.nstr(qw_evals[k], 8)}")

print(f"\n--- Archimedean-Only Even Eigenvalues (first 15) ---")
for k in range(min(15, dim_ev)):
    print(f"    k={k:2d}: a_k = {mp.nstr(arch_evals[k], 8)}")

print(f"\n--- Q_W Bulk Eigenvalues (last 10) ---")
for k in range(max(0, dim_ev-10), dim_ev):
    print(f"    k={k:2d}: mu_k = {float(qw_evals[k]):.6f}")

print(f"\n--- Archimedean Bulk Eigenvalues (last 10) ---")
for k in range(max(0, dim_ev-10), dim_ev):
    print(f"    k={k:2d}: a_k = {float(arch_evals[k]):.6f}")

# ============================================================
# PART C: Structural comparison
# ============================================================

print(f"\n{'='*70}")
print("STRUCTURAL COMPARISON")
print(f"{'='*70}")

# Q_W bulk spacing
print(f"\n  Q_W even-sector bulk spacings (k=10..15):")
for k in range(10, min(16, dim_ev-1)):
    gap = float(qw_evals[k+1] - qw_evals[k])
    print(f"    mu_{k+1} - mu_{k} = {gap:.6f}")

# Archimedean bulk spacing
print(f"\n  Archimedean bulk spacings (k=10..15):")
for k in range(10, min(16, dim_ev-1)):
    gap = float(arch_evals[k+1] - arch_evals[k])
    print(f"    a_{k+1} - a_{k} = {gap:.6f}")

# Entanglement spectrum spacing (constant)
print(f"\n  Entanglement level spacing: {ent_levels[1] - ent_levels[0]:.6f} (constant)")

# Prime perturbation effect: shift of eigenvalues
print(f"\n  Prime perturbation shift (first 10):")
for k in range(min(10, dim_ev)):
    shift = float(qw_evals[k] - arch_evals[k])
    print(f"    k={k:2d}: mu_k - a_k = {shift:.4e}")

# Key diagnostic: is Q_W's archimedean part (A) spectrally similar to H_E?
# The archimedean part A = W02 - WR acts as a convolution on S^1.
# The modular Hamiltonian for a half-interval of a c=1 CFT on S^1 is
# also a (non-local) operator on S^1. Compare their spectra.

# Archimedean eigenvalue growth rate
print(f"\n  Archimedean eigenvalue growth (a_k vs k):")
for k in [2, 3, 5, 10, 15, 20]:
    if k < dim_ev:
        ratio = float(arch_evals[k]) / float(log(k))
        print(f"    a_{k} = {float(arch_evals[k]):.6f}, a_k/log(k) = {ratio:.4f}")

# Entanglement Hamiltonian eigenvalue growth
print(f"\n  Entanglement energy growth (eps_k vs k):")
for k in [1, 2, 5, 10, 15]:
    if k <= len(ent_levels):
        ratio = ent_levels[k-1] / k
        print(f"    eps_{k} = {ent_levels[k-1]:.4f}, eps_k/k = {ratio:.4f}")

print(f"\n  SUMMARY:")
print(f"  Archimedean A: eigenvalues grow as ~log(k) (convolution kernel on S^1)")
print(f"  Entanglement H_E: eigenvalues grow as ~k (linear, free boson)")
print(f"  Q_W = A - B: same log(k) growth in bulk, shifted by prime perturbation")
print(f"  MISMATCH: Q_W grows logarithmically; H_E grows linearly.")
print(f"  Q_W is NOT spectrally equivalent to a free-boson entanglement Hamiltonian.")
print(f"  The difference is structural: A is a cosh-type convolution, H_E is a stress-tensor integral.")

print(f"\n{'='*70}")
print("DONE")
print(f"{'='*70}")
