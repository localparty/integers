"""
R37: UV Completion Computations

Compare:
1. QG5D KK operator eigenvalues vs first Riemann zeros
2. The Connes-Consani rank-one perturbation structure
3. The Weil quadratic form at small lambda
"""

import numpy as np
from scipy import linalg
import mpmath
mpmath.mp.dps = 50  # 50 decimal places

print("=" * 70)
print("R37: UV COMPLETION COMPUTATIONS")
print("=" * 70)

# ============================================================
# Part 1: KK eigenvalues on S^1 vs Riemann zeros
# ============================================================
print("\n--- Part 1: KK Eigenvalues vs Riemann Zeros ---\n")

# First 10 non-trivial zeros of zeta(1/2 + it)
# (imaginary parts, known to high precision)
zeta_zeros = [
    14.134725141734693790,
    21.022039638771554993,
    25.010857580145688763,
    30.424876125859513210,
    32.935061587739189690,
    37.586178158825671257,
    40.918719012147495187,
    43.327073280914999519,
    48.005150881167159727,
    49.773832477672302182,
]

# KK eigenvalues on S^1: n/R for Dirac, n^2/R^2 for Laplacian
# With R = 1: eigenvalues are n (Dirac) or n^2 (Laplacian)
# These are 0, 1, 1, 4, 4, 9, 9, 16, 16, ...
# NOT the zeta zeros. They are the KK MASSES, not the zeros.

print("First 10 non-trivial zeta zeros (Im part):")
for i, z in enumerate(zeta_zeros):
    print(f"  rho_{i+1} = {z:.15f}")

print("\nKK eigenvalues on S^1 (Dirac, R=1):")
kk_dirac = list(range(-5, 6))
for n in kk_dirac:
    print(f"  n = {n:+d}  ->  eigenvalue = {n}")

print("\nKK eigenvalues on S^1 (Laplacian, R=1):")
kk_lapl = [n**2 for n in range(6)]
for n in range(6):
    print(f"  n = {n}  ->  eigenvalue = {n**2}")

print("\nConclusion: KK eigenvalues are {n} or {n^2}, NOT the zeta zeros.")
print("The spectral zeta SUM over KK eigenvalues gives zeta(s),")
print("but individual eigenvalues are integers, not transcendental numbers.\n")

# ============================================================
# Part 2: The Connes-Consani scaling operator spectrum
# ============================================================
print("\n--- Part 2: Scaling Operator Spectrum at Finite Lambda ---\n")

# D_log^{(lambda)} = -i d/d(log u) on [-L/2, L/2] with periodic BC
# Eigenvalues: 2*pi*n / L, n in Z
# L = 2*log(lambda)

for lam_sq in [7, 11, 13, 14]:
    lam = np.sqrt(lam_sq)
    L = 2 * np.log(lam)
    print(f"lambda^2 = {lam_sq} (lambda = {lam:.4f}, L = {L:.4f}):")
    print(f"  Number of primes p <= lambda^2: {sum(1 for p in [2,3,5,7,11,13] if p <= lam_sq)}")
    print(f"  Eigenvalue spacing: 2*pi/L = {2*np.pi/L:.4f}")
    print(f"  First few eigenvalues: ", end="")
    for n in range(-3, 4):
        print(f"{2*np.pi*n/L:.3f}", end="  ")
    print()

    # The first zeta zero is at ~14.135
    # How many eigenvalues of D_log below the first zero?
    n_below = int(14.135 * L / (2*np.pi))
    print(f"  Eigenvalues below first zeta zero: ~{n_below}")
    print()

# ============================================================
# Part 3: The Weil quadratic form (simplified model)
# ============================================================
print("\n--- Part 3: Simplified Weil Form Model ---\n")

# The Weil form on the Fourier basis {e^{2*pi*i*n*x/L} : |n| <= N}
# Q_W(V_n, V_m) involves the explicit formula contributions

# For a simplified model with p primes contributing:
# The prime contribution at prime p for modes n, m is proportional to
# log(p) * p^{-1/2} * [overlap integral of V_n, V_m with p^{it}]

def weil_form_matrix(N, lam_sq, verbose=False):
    """
    Simplified Weil form matrix.

    The actual Connes-Consani matrix involves the explicit formula.
    We approximate the structure to illustrate the rank-one perturbation
    pattern.
    """
    lam = np.sqrt(lam_sq)
    L = 2 * np.log(lam)
    dim = 2*N + 1

    # Free part: diagonal with eigenvalues 2*pi*n/L
    freqs = np.array([2*np.pi*n/L for n in range(-N, N+1)])

    # The Weil form contributions from primes
    # W_p contribution: involves log(p)/p^{1/2} * sinc-like terms
    primes = [p for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] if p <= lam_sq]

    # Build the Toeplitz-like matrix from the explicit formula
    Q = np.zeros((dim, dim))

    # Pole contributions (W_{0,2}): positive, from s=0 and s=1 of zeta
    for i in range(dim):
        for j in range(dim):
            n = i - N
            m = j - N
            # The pole terms contribute ~delta_{n,m} * (positive constant)
            if n == m:
                Q[i, j] += 2.0  # Simplified W_{0,2} contribution

    # Prime contributions (negative for Weil positivity to be non-trivial)
    for p in primes:
        log_p = np.log(p)
        for k in range(1, 5):  # prime powers
            coeff = log_p * p**(-k/2)
            # Each prime contributes a rank-one-like term
            # Evaluated at the Fourier modes
            v = np.zeros(dim)
            for i in range(dim):
                n = i - N
                # The test function evaluated at p^k
                # For the Fourier mode V_n on [-L/2, L/2]:
                # V_n(log(p^k)) = exp(2*pi*i*n*k*log(p)/L) / sqrt(L)
                # if k*log(p) <= L/2, else 0
                if k * np.log(p) <= L/2:
                    v[i] = np.cos(2*np.pi*n*k*np.log(p)/L) / np.sqrt(L)

            # Subtract the prime contribution (negative in Weil form)
            Q -= coeff * np.outer(v, v)

    # Archimedean contribution (W_R): involves digamma function
    # Simplified: a negative diagonal contribution that grows with |n|
    for i in range(dim):
        n = i - N
        if n != 0:
            Q[i, i] -= np.log(abs(n) + 1) / (2 * np.pi)

    return Q

# Test with small parameters
for lam_sq in [7, 13]:
    for N in [5, 10, 20]:
        Q = weil_form_matrix(N, lam_sq)
        eigenvalues = np.sort(linalg.eigvalsh(Q))
        print(f"lambda^2={lam_sq}, N={N}: dim={2*N+1}")
        print(f"  Min eigenvalue: {eigenvalues[0]:.6f}")
        print(f"  Max eigenvalue: {eigenvalues[-1]:.6f}")
        print(f"  Eigenvalue 2nd: {eigenvalues[1]:.6f}")
        print(f"  Gap (2nd - 1st): {eigenvalues[1] - eigenvalues[0]:.6f}")

        # Check if minimal eigenvector is even
        min_vec = np.zeros(2*N+1)
        # Get actual eigenvector
        evals, evecs = linalg.eigh(Q)
        min_vec = evecs[:, 0]

        # Check evenness: V_{-n} component should equal V_n component
        is_even = True
        for i in range(1, N+1):
            # Index N-i corresponds to mode -i, index N+i corresponds to mode +i
            if abs(min_vec[N-i] - min_vec[N+i]) > 1e-10:
                is_even = False
                break
        print(f"  Minimal eigenvector is even: {is_even}")
        print()

# ============================================================
# Part 4: Exponential map verification
# ============================================================
print("\n--- Part 4: Exponential Map Verification ---\n")

# Verify: -i d/dphi on S^1 maps to -i x d/dx on R_+* under phi = log(x)
# If psi(phi) = f(e^phi), then:
# -i d/dphi psi = -i d/dphi f(e^phi) = -i e^phi f'(e^phi) = -i x f'(x) = -i x d/dx f

print("Under phi = log(x):")
print("  -i d/dphi psi(phi) = -i d/dphi f(e^phi)")
print("                     = -i e^phi f'(e^phi)")
print("                     = -i x f'(x)")
print("                     = (-i x d/dx) f(x)")
print()
print("So: D_{S^1} = -i d/dphi  <-->  D_log = -i x d/dx")
print("These are EXACTLY the same operator under the exponential map.")
print("This confirms Identification 1 with mathematical precision.")

# The eigenfunction e^{in*phi} maps to x^{in}
print("\nEigenfunctions:")
print("  e^{in*phi} on S^1  <-->  x^{in} = e^{in*log(x)} on R_+*")
print("  eigenvalue n/R (Dirac on S^1)  <-->  eigenvalue n/R (scaling on R_+*)")

# ============================================================
# Part 5: Local spectral zeta comparison
# ============================================================
print("\n--- Part 5: Local Spectral Zeta at Primes ---\n")

# From R30: the p-adic Vladimirov spectral zeta gives the WRONG local factor
# Euler factor: (1 - p^{-s})^{-1}
# Vladimirov (Dirac): (1 - p^{-s}) / (1 - p^{1-s})

print("Comparison of local factors at s = 2:")
print(f"{'Prime p':>8} {'Euler':>12} {'Vladimirov':>12} {'Ratio':>12}")
for p in [2, 3, 5, 7, 11, 13]:
    euler = 1 / (1 - p**(-2))
    vlad = (1 - p**(-2)) / (1 - p**(1-2))
    ratio = vlad / euler
    print(f"{p:>8} {euler:>12.6f} {vlad:>12.6f} {ratio:>12.6f}")

print("\nProduct comparison (first 6 primes, s=2):")
euler_prod = 1.0
vlad_prod = 1.0
for p in [2, 3, 5, 7, 11, 13]:
    euler_prod *= 1 / (1 - p**(-2))
    vlad_prod *= (1 - p**(-2)) / (1 - p**(1-2))

print(f"  Euler product: {euler_prod:.10f}")
print(f"  Vladimirov product: {vlad_prod:.10f}")
print(f"  zeta(2) = {np.pi**2/6:.10f}")
print(f"  zeta(3)/zeta(2) = {float(mpmath.zeta(3)/mpmath.zeta(2)):.10f}")

# ============================================================
# Part 6: The mu_lambda convergence question
# ============================================================
print("\n--- Part 6: Weil Form Minimum vs Lambda ---\n")

print("Minimum eigenvalue of simplified Weil form as lambda^2 increases:")
print(f"{'lambda^2':>10} {'N':>5} {'mu_lambda':>15} {'Num primes':>12}")
for lam_sq in [3, 5, 7, 11, 13, 17, 23, 29, 37, 47]:
    N = min(30, max(10, int(np.sqrt(lam_sq) * 5)))
    Q = weil_form_matrix(N, lam_sq)
    evals = np.sort(linalg.eigvalsh(Q))
    mu = evals[0]
    n_primes = sum(1 for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47] if p <= lam_sq)
    print(f"{lam_sq:>10} {N:>5} {mu:>15.8f} {n_primes:>12}")

print("\nNote: This is a SIMPLIFIED model. The actual Connes-Consani")
print("computation uses the exact explicit formula coefficients and")
print("achieves 10^{-55} accuracy for the first zero.\n")

# ============================================================
# Part 7: The rank-one perturbation structure
# ============================================================
print("\n--- Part 7: Rank-One Perturbation Analysis ---\n")

# Each prime p contributes a rank-one term to the Weil form
# The Connes-Consani perturbation is: H = D_free - |D xi><delta_N|
# where xi is the minimal eigenvector of Q_W

# The rank of the prime contribution
print("Rank of prime contributions in the Weil form:")
print("Each prime p contributes through the term:")
print("  W_p(f,g) = sum_{m>=1} log(p) p^{-m/2} [f(p^m)g(p^{-m}) + ...]")
print()
print("For test functions on [-L/2, L/2], p^m must satisfy m*log(p) <= L/2.")
print("So each prime contributes a FINITE-rank perturbation (rank = number of")
print("valid m values).\n")

for lam_sq in [7, 13, 29]:
    lam = np.sqrt(lam_sq)
    L = 2 * np.log(lam)
    primes = [p for p in [2,3,5,7,11,13,17,19,23,29] if p <= lam_sq]
    print(f"lambda^2 = {lam_sq} (L = {L:.4f}):")
    for p in primes:
        max_m = int(L / (2 * np.log(p))) if np.log(p) > 0 else 0
        print(f"  p = {p:>2}: rank contribution = {max(1, max_m)}")
    print()

print("Total perturbation rank = sum of contributions from each prime.")
print("The FINAL operator perturbation is rank-ONE (projected onto the")
print("minimal eigenvector direction), but the Weil form itself has rank")
print("determined by the number of prime contributions.\n")

# ============================================================
# Summary
# ============================================================
print("=" * 70)
print("COMPUTATIONAL SUMMARY")
print("=" * 70)
print("""
1. KK eigenvalues on S^1 are {n/R : n in Z} (Dirac) or {n^2/R^2} (Laplacian).
   These are NOT the zeta zeros. The zeta zeros emerge from the SPECTRAL ZETA
   (the sum over KK eigenvalues), not as individual eigenvalues.

2. The exponential map phi -> x = e^phi establishes exact unitary equivalence:
   D_{S^1} = -i d/dphi <--> D_log = -i x d/dx (Connes's scaling operator).
   This is Identification 1: mathematically precise.

3. The local p-adic spectral zeta (Vladimirov) gives the WRONG Euler factor:
   (1-p^{-s})/(1-p^{1-s}) instead of (1-p^{-s})^{-1}.
   The adelic product gives zeta(s-1)/zeta(s), NOT zeta(s).

4. The Weil form in our simplified model has a smallest eigenvalue that
   depends on lambda. The trend and convergence to 0 (which would prove RH)
   cannot be established from this simplified model.

5. Each prime contributes a finite-rank perturbation to the Weil form.
   The final operator perturbation is rank-one (D_log^{(lambda,N)} - D_log
   has rank one), constructed from the minimal eigenvector of Q_W.

6. The QG5D KK operator is NOT the same as the Connes-Consani operator
   (five critical differences from R30). The UV completion question is
   therefore about structural compatibility, not operator identity.
""")
