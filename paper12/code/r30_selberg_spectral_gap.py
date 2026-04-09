#!/usr/bin/env python3
"""
Round 30: Selberg Spectral Gap Investigation

1. Verify the Kim-Sarnak bound and the gap to 1/4
2. Compute the scattering matrix phi(s) and verify its connection to zeta
3. Check whether T^2 spectral data can constrain Gamma\H eigenvalues
4. Explore the Selberg zeta / Riemann zeta relationship quantitatively
"""

import numpy as np
from scipy import special
from mpmath import mp, mpf, zeta, gamma, pi, log, sqrt, inf

mp.dps = 30  # 30 decimal places

print("=" * 70)
print("PART A: The Selberg Eigenvalue Conjecture — Known Bounds")
print("=" * 70)

# Known bounds on the first eigenvalue for congruence subgroups
bounds = [
    ("Selberg (1965)", "3/16", 3/16, "Original"),
    ("Gelbart-Jacquet (1978)", "~0.2", 0.2, "Sym^2 to GL(3)"),
    ("Luo-Rudnick-Sarnak (1995)", "171/784", 171/784, "Rankin-Selberg"),
    ("Kim-Shahidi (2002)", "66/289", 66/289, "Sym^3 to GL(4)"),
    ("Kim-Sarnak (2003)", "975/4096", 975/4096, "Sym^4 to GL(5)"),
]

print("\nProgression of lower bounds on lambda_1 for congruence subgroups:")
print(f"{'Author(s)':<30} {'Fraction':<12} {'Value':<10} {'Gap to 1/4':<12} {'Method'}")
print("-" * 90)
for author, frac, val, method in bounds:
    gap = 0.25 - val
    print(f"{author:<30} {frac:<12} {val:<10.6f} {gap:<12.6f} {method}")

target = mpf(1)/4
best = mpf(975)/4096
gap = target - best
print(f"\nThe gap: 1/4 - 975/4096 = {gap}")
print(f"As fraction: 49/4096 = {mpf(49)/4096}")
print(f"Percentage of target: {float(gap/target)*100:.2f}%")

# The theta exponent from each bound
print("\n\nCorresponding Ramanujan theta exponents:")
print(f"{'Sym power':<12} {'theta':<15} {'lambda_1 bound':<15} {'1/4 - lambda':<15}")
print("-" * 60)
for n in range(1, 6):
    if n == 1:
        theta = mpf(1)/4  # Trivial
        label = "Sym^1"
    elif n == 2:
        theta = mpf(1)/5  # Gelbart-Jacquet
        label = "Sym^2"
    elif n == 3:
        theta = mpf(5)/34  # Kim-Shahidi
        label = "Sym^3"
    elif n == 4:
        theta = mpf(7)/64  # Kim-Sarnak
        label = "Sym^4"
    elif n == 5:
        theta = mpf(9)/100  # Hypothetical Sym^5
        label = "Sym^5*"
    lam = mpf(1)/4 - theta**2
    print(f"{label:<12} {float(theta):<15.6f} {float(lam):<15.6f} {float(mpf(1)/4 - lam):<15.6f}")

print("\n* Sym^5 is hypothetical -- not yet established.")
print("  Pattern: theta = (2n-1)/(n^2 * const), decreasing toward 0.")

print("\n" + "=" * 70)
print("PART B: The Scattering Matrix phi(s) on SL(2,Z)\\H")
print("=" * 70)

print("\nThe scattering matrix for SL(2,Z)\\H is:")
print("  phi(s) = sqrt(pi) * Gamma(s - 1/2) / Gamma(s) * zeta(2s-1) / zeta(2s)")
print()
print("Key properties:")
print("  1. phi(s) * phi(1-s) = 1  (functional equation)")
print("  2. Poles of phi(s) at zeros of zeta(2s), i.e., s = rho/2")
print("  3. Zeros of phi(s) at zeros of zeta(2s-1), i.e., s = (1+rho)/2")

# Evaluate phi(s) at several points
print("\nEvaluating |phi(1/2 + it)| for small t:")
print(f"{'t':<10} {'|phi(1/2+it)|':<20} {'arg(phi)/pi':<15}")
print("-" * 50)
for t_val in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 14.13]:
    s = mpf(1)/2 + t_val * 1j
    try:
        gamma_ratio = gamma(s - mpf(1)/2) / gamma(s)
        zeta_ratio = zeta(2*s - 1) / zeta(2*s)
        phi_val = sqrt(pi) * gamma_ratio * zeta_ratio
        abs_phi = abs(phi_val)
        arg_phi = float(mp.arg(phi_val) / pi)
        print(f"{t_val:<10} {float(abs_phi):<20.6f} {arg_phi:<15.6f}")
    except Exception as e:
        print(f"{t_val:<10} error: {e}")

# Verify |phi(1/2+it)| = 1 (unitarity on the critical line)
print("\nUnitarity check: |phi(1/2 + it)| should be 1 for all real t")
print("(This follows from phi(s)*phi(1-s) = 1 and the functional equation)")

print("\n" + "=" * 70)
print("PART C: T^2 = S^1_e x S^1_beta and the Modular Group")
print("=" * 70)

print("""
The torus T^2 = S^1 x S^1 has modular group SL(2,Z) acting on its
complex structure parameter tau in the upper half-plane H.

The moduli space of flat tori = SL(2,Z)\\H = the modular surface.

This connection is TOPOLOGICAL/GEOMETRIC, not spectral:
- The SPECTRUM of T^2 at a fixed tau = eigenvalues of the flat Laplacian
  on T^2 = {|m + n*tau|^2 / Im(tau)^2 : (m,n) in Z^2 \\ (0,0)}
  = the Epstein zeta function E_2(s; Q_tau)
- The MODULI SPACE of all such T^2's = SL(2,Z)\\H
- The SPECTRUM of Delta on SL(2,Z)\\H = Maass eigenvalues + continuous
  spectrum = a completely different spectral problem

The two spectral problems are related through MODULAR FORMS:
- A Maass cusp form phi(z) on SL(2,Z)\\H, evaluated at z = tau,
  gives a function on the moduli space of tori
- The Hecke operators T_p on Maass forms correspond to averaging
  over degree-p coverings of the torus
""")

# Compute spectral gap of T^2 at the self-dual point tau = i
print("Spectrum of T^2 at tau = i (square torus):")
print("  Eigenvalues = (m^2 + n^2) * (2*pi)^2 / Area")
print("  (normalized so Area = 1)")
eigenvalues = sorted(set(m**2 + n**2 for m in range(-5, 6) for n in range(-5, 6) if m != 0 or n != 0))[:10]
print(f"  First 10 distinct eigenvalues (m^2+n^2): {eigenvalues}")
print(f"  Spectral gap: lambda_1 = {eigenvalues[0]} (from (m,n) = (1,0) or (0,1))")
print(f"  Degeneracies: {[sum(1 for m in range(-10,11) for n in range(-10,11) if m**2+n**2 == e) for e in eigenvalues]}")

# At the hexagonal point tau = e^{i*pi/3}
print("\nSpectrum of T^2 at tau = e^{i*pi/3} (hexagonal torus):")
print("  Eigenvalues = (m^2 + mn + n^2) * 4*pi^2 / (sqrt(3)/2)")
hex_eigenvalues = sorted(set(m**2 + m*n + n**2 for m in range(-5, 6) for n in range(-5, 6) if m != 0 or n != 0))[:10]
print(f"  First 10 distinct eigenvalues (m^2+mn+n^2): {hex_eigenvalues}")
print(f"  Spectral gap: lambda_1 = {hex_eigenvalues[0]}")

print("\n" + "=" * 70)
print("PART D: Selberg Zeta vs Riemann Zeta — The Connection")
print("=" * 70)

print("""
The Selberg zeta Z_Gamma(s) for Gamma = SL(2,Z) encodes:

1. Maass cusp form eigenvalues: zeros at s = 1/2 +/- i*r_j
   where lambda_j = 1/4 + r_j^2

2. Scattering resonances: related to phi(s) = zeta(2s-1)/zeta(2s) * ...
   Poles of phi(s) at zeros of zeta(2s), i.e., s = rho/2

3. The Riemann zeta appears through:
   - The scattering matrix: phi(s) involves zeta(2s)/zeta(2s-1)
   - The Eisenstein series E(z,s) has constant term y^s + phi(s)*y^{1-s}
   - The Rankin-Selberg method: <E(.,s), |phi_j|^2> involves L(s, phi_j x phi_j)

CONNECTION: If RH is true for zeta(s), then the scattering poles of
phi(s) all have Re(s) = 1/4 (from zeta(2s) = 0 at 2s = rho with
Re(rho) = 1/2). But conversely, the Selberg conjecture lambda >= 1/4
for the DISCRETE spectrum does NOT imply RH for the continuous spectrum.
""")

# Verify: first few zeros of zeta map to scattering poles
print("First zeros of zeta(s) -> scattering poles of phi(s):")
print(f"{'rho (zero of zeta)':<30} {'s = rho/2 (pole of phi)':<30} {'Re(s)':<10}")
print("-" * 70)
# Known zeros of zeta(s) on the critical line
zeros_of_zeta = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]
for gamma_n in zeros_of_zeta:
    rho = 0.5 + gamma_n * 1j
    s_pole = rho / 2
    print(f"1/2 + {gamma_n:.6f}i   {f'1/4 + {gamma_n/2:.6f}i':<30} {'1/4':<10}")

print("\nAll scattering poles have Re(s) = 1/4 (assuming RH).")
print("The Selberg eigenvalue conjecture says discrete eigenvalues")
print("satisfy Re(s_j) = 1/2 (for s_j = 1/2 + i*r_j with r_j real).")
print()
print("Gap between discrete (Re = 1/2) and continuous (Re = 1/4):")
print("  1/2 - 1/4 = 1/4 -- this is exactly the Selberg gap!")

print("\n" + "=" * 70)
print("PART E: Can the KK Decomposition on T^2 Relate to Gamma\\H?")
print("=" * 70)

print("""
The QG5D KK decomposition on T^2 = S^1_e x S^1_beta:
- 5D field Phi(x,phi,beta) = sum_{m,n} phi_{m,n}(x) * exp(i*m*phi/R_e) * exp(i*n*beta/R_beta)
- KK masses: M^2_{m,n} = m^2/R_e^2 + n^2/R_beta^2
- At the self-dual point R_e = R_beta = R: this is the flat torus spectrum

The modular group SL(2,Z) acts on the complex structure tau = R_beta/R_e:
- T: tau -> tau + 1 (shifts by one period of the beta-circle)
- S: tau -> -1/tau (T-duality, exchanges e and beta circles)

The KK spectrum at tau is the Epstein zeta E_2(s; Q_tau).

KEY QUESTION: Does the SL(2,Z) invariance of the KK spectrum
propagate to a spectral constraint on Gamma\\H?

ANSWER: NO, because:

1. The KK spectrum is the spectrum of the FLAT torus T^2 at a FIXED
   modular parameter tau. It is a collection of numbers {lambda_{m,n}(tau)}.

2. The spectrum of Gamma\\H is the set of eigenvalues of the HYPERBOLIC
   Laplacian on the MODULI SPACE of tori. This is a completely different
   operator on a completely different space.

3. The SL(2,Z) symmetry enters differently:
   - KK: SL(2,Z) is a GAUGE symmetry identifying equivalent tori
   - Gamma\\H: SL(2,Z) is the GROUP defining the quotient

4. The fact that the KK spectrum is SL(2,Z)-invariant is TRIVIAL --
   it just means equivalent tori have the same spectrum. This tells
   us nothing about the Maass eigenvalues on the moduli space.

The relationship between T^2 and Gamma\\H is that Gamma\\H is the
SPACE OF T^2's (moduli space), not a T^2 itself. The spectrum of the
space of objects is not determined by the spectra of the objects.
""")

# Quantitative check: spectral gap of T^2 vs spectral gap of Gamma\H
print("Spectral gaps compared:")
print(f"  T^2 (flat, at tau=i): lambda_1 = (2*pi)^2 * 1 = {(2*np.pi)**2:.4f}")
print(f"  Gamma\\H (hyperbolic): lambda_1 ~ 91.14")
print(f"  Selberg conjecture for Gamma_0(N): lambda_1 >= 1/4 = 0.25")
print()
print("The T^2 gap is about the flat Laplacian on a torus.")
print("The Gamma\\H gap is about the hyperbolic Laplacian on a quotient of H.")
print("These are mathematically unrelated spectral gaps.")

print("\n" + "=" * 70)
print("PART F: The Geometric Euler Product vs Arithmetic Euler Product")
print("=" * 70)

print("""
SELBERG ZETA (geometric Euler product):
  Z_Gamma(s) = prod_{gamma_0} prod_{k>=0} (1 - N(gamma_0)^{-(s+k)})

  "Primes" = primitive closed geodesics on Gamma\\H
  "Norms" = N(gamma_0) = exp(l(gamma_0)) where l is the geodesic length

RIEMANN ZETA (arithmetic Euler product):
  zeta(s) = prod_p (1 - p^{-s})^{-1}

  "Primes" = prime numbers p = 2, 3, 5, 7, ...

CONNECTION via Prime Geodesic Theorem:
  pi_geod(x) ~ x / log x   (same form as PNT: pi(x) ~ x / log x)

But the geodesic "primes" are NOT ordinary primes:
  Geodesic norms: N = epsilon_D^2 for fundamental units epsilon_D
  of real quadratic fields Q(sqrt(D))

  First few: D=5: N~2.618, D=8: N~5.828, D=12: N~13.93, D=13: N~13.93, ...
  Ordinary primes: 2, 3, 5, 7, 11, 13, ...

The two sets have the SAME DISTRIBUTION (prime counting functions
both grow as x/log x) but are DIFFERENT NUMBERS.
""")

# Compute first few geodesic norms
print("First geodesic norms vs primes:")
print(f"{'D':<5} {'epsilon_D':<15} {'N = epsilon_D^2':<20} {'Nearest prime':<15}")
print("-" * 55)
# Fundamental discriminants and their units
discriminants = [(5, (1+np.sqrt(5))/2), (8, 1+np.sqrt(2)), (12, 2+np.sqrt(3)),
                 (13, (3+np.sqrt(13))/2), (17, 4+np.sqrt(17)), (21, (5+np.sqrt(21))/2)]
for D, eps in discriminants:
    N = eps**2
    # Find nearest prime
    from sympy import nextprime, prevprime
    try:
        np_prime = int(round(N))
        print(f"{D:<5} {eps:<15.6f} {N:<20.6f} {np_prime:<15}")
    except:
        print(f"{D:<5} {eps:<15.6f} {N:<20.6f}")

print("\nThe geodesic norms and ordinary primes are different number sets,")
print("but with the same asymptotic distribution.")

print("\n" + "=" * 70)
print("PART G: Summary of Obstructions")
print("=" * 70)

print("""
OBSTRUCTION 1: Curvature mismatch
  QG5D spectral gap (Theorem E.1): Lichnerowicz on CP^2 (positive curvature)
  Modular surface: K = -1 (negative curvature)
  Lichnerowicz does NOT apply on negatively curved manifolds.
  STATUS: HARD WALL

OBSTRUCTION 2: Wrong category
  QG5D internal manifold M_7: compact, Riemannian, differential-geometric
  Modular surface Gamma\\H: arithmetic quotient, spectral theory of
  automorphic forms, Langlands program
  These are different mathematical universes.
  STATUS: HARD WALL

OBSTRUCTION 3: Product decomposition doesn't propagate
  Spectral gap on M_1 x M_2: shifts combined spectrum by gap of M_1,
  but does NOT constrain spectrum of M_2 alone.
  STATUS: HARD WALL (mathematical theorem)

OBSTRUCTION 4: T^2 moduli != Gamma\\H spectrum
  T^2 KK spectrum at fixed tau != Maass eigenvalues on the moduli space.
  The spectrum of the moduli space is not determined by spectra of the objects.
  STATUS: HARD WALL (category error)

OBSTRUCTION 5: Geometric vs arithmetic primes
  Selberg zeta "primes" = geodesic norms (units of quadratic fields)
  Riemann zeta "primes" = prime numbers
  Same distribution, different numbers. No known bridge.
  STATUS: HARD WALL
""")
