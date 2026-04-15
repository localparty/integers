"""
Adelic Lee-Yang Analysis (Round 27)

Computational checks for the adelic Tate zeta integral and Lee-Yang conditions.

Sections:
A. Local zeta integrals as polynomials in z_p = p^{-s}
B. Asano contraction: product of local Lee-Yang factors
C. Archimedean local factor: NOT polynomial
D. Adelic Fourier transform and functional equation
E. Positivity check on Schwartz-Bruhat test functions
F. The convergence obstruction: infinite product of polynomials
"""

import mpmath
import numpy as np

mpmath.mp.dps = 50  # 50-digit precision

print("=" * 70)
print("PART A: Local zeta integrals at finite primes")
print("=" * 70)
print()

# At each prime p, the local zeta integral for Phi_p = char(Z_p) is:
#   Z_p(s) = integral_{Q_p*} char(Z_p)(x) |x|_p^s d*x
#          = sum_{k=0}^{infty} p^{-ks} * (1 - 1/p)
#          = (1 - 1/p) / (1 - p^{-s})
# But the EULER FACTOR in zeta(s) is (1 - p^{-s})^{-1}.
# The local zeta integral differs by the volume factor (1-1/p).
#
# Key question: Is (1 - p^{-s})^{-1} a polynomial in z_p = p^{-s}?
# Answer: NO. It is 1/(1-z_p), a RATIONAL function, not a polynomial.
#
# But 1/Z_p(s) = (1 - z_p) IS a polynomial of degree 1 in z_p.
# Its zero is at z_p = 1, i.e., p^{-s} = 1, i.e., s = 2*pi*i*k/log(p).

print("For each prime p, the local factor:")
print("  Z_p(s) = (1 - p^{-s})^{-1}")
print("  1/Z_p(s) = 1 - p^{-s} = 1 - z_p  [degree 1 polynomial in z_p]")
print()

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print("Prime p | Zero of 1/Z_p at z_p = | |z_p| on critical line (s=1/2+it)")
print("-" * 70)
for p in primes:
    # Zero of 1-z_p is at z_p = 1
    # On the critical line s = 1/2 + it:
    #   z_p = p^{-1/2-it} => |z_p| = p^{-1/2}
    z_p_modulus = float(p ** (-0.5))
    print(f"  p={p:2d}   | z_p = 1 (i.e. s=0)    | |z_p| = p^{{-1/2}} = {z_p_modulus:.6f}")

print()
print("KEY: On the critical line, |z_p| = p^{-1/2} < 1 for all primes.")
print("The zero of each local factor 1-z_p is at |z_p| = 1 (the unit circle")
print("in the LOCAL variable z_p). So each local factor IS Lee-Yang!")
print()

# Check: does 1-z_p have its zero on |z_p| = 1?
# Yes: the zero is at z_p = 1, and |1| = 1.
print("Verification: zero of (1 - z_p) is at z_p = 1, |z_p| = 1. CHECK.")
print()

print("=" * 70)
print("PART B: The Asano contraction question")
print("=" * 70)
print()

# Each local factor 1/zeta_p(s) = (1 - z_p) is a degree-1 polynomial
# with zero on |z_p| = 1. The Lee-Yang property holds for each factor.
#
# The global product is:
#   1/zeta(s) = prod_p (1 - z_p) where z_p = p^{-s}
#
# Asano contraction: if we have polynomials P_1(z_1), P_2(z_2) each
# with zeros on |z| = 1, and we COUPLE them with J >= 0, the
# contracted polynomial retains zeros on |z| = 1.
#
# BUT: the Euler product is NOT an Asano contraction!
# The variables z_p = p^{-s} for different primes p are ALL functions
# of the SAME parameter s. The "coupling" between primes is the
# CONSTRAINT that z_p = p^{-s} for a common s.
#
# In an Asano contraction, you SUM over one variable while keeping
# the other fixed. In the Euler product, all variables are linked.

print("The Asano contraction question:")
print()
print("Each local 1/Z_p(s) = (1 - p^{-s}) has zero at p^{-s} = 1.")
print("This zero is on |z_p| = 1 in the LOCAL variable z_p = p^{-s}.")
print()
print("BUT the Euler product is NOT an Asano contraction because:")
print("  - Asano contracts INDEPENDENT variables with ferromagnetic coupling")
print("  - The Euler product constrains ALL z_p via z_p = p^{-s}")
print("  - The z_p are NOT independent: z_6 = z_2 * z_3, etc.")
print("  - The 'coupling' is the shared parameter s, not a J >= 0 weight")
print()

# Demonstrate the coupling constraint:
print("Coupling constraint demonstration:")
print("If z_2 = 2^{-s} and z_3 = 3^{-s}, then z_6 = z_2 * z_3.")
print("This multiplicative constraint has no ferromagnetic interpretation.")
print()

# What WOULD Asano contraction give?
# If the z_p were truly independent, and we coupled them ferromagnetically,
# the resulting polynomial would have zeros on a multi-dimensional
# unit torus |z_p| = 1 for all p.
# But the zeros of zeta(s) correspond to a ONE-DIMENSIONAL curve
# in the infinite-dimensional z-space: {(p^{-s})_p : s in C}.
# The constraint to this curve is what makes the problem hard.

print("If z_p were independent with ferromagnetic coupling:")
print("  Asano would give zeros on |z_p| = 1 for ALL p simultaneously")
print("  This is the multi-dimensional unit torus T^infty")
print()
print("But zeros of zeta(s) lie on the 1D curve (p^{-s})_p in C^infty.")
print("The intersection of this curve with T^infty is:")
print("  |p^{-s}| = 1 for all p")
print("  p^{-Re(s)} = 1 for all p")
print("  Re(s) = 0 (NOT 1/2!)")
print()
print("CRITICAL: In the z_p variables, Re(s) = 0 maps to the unit torus,")
print("not Re(s) = 1/2. The Lee-Yang locus is WRONG by 1/2.")
print()

# Verify: on Re(s) = 0: |p^{-s}| = |p^{-it}| = 1. Yes.
# On Re(s) = 1/2: |p^{-s}| = p^{-1/2} < 1. Not on unit circle.
for p in [2, 3, 5]:
    val_half = float(p ** (-0.5))
    val_zero = 1.0
    print(f"  p={p}: |z_p| at Re(s)=1/2: {val_half:.4f}, at Re(s)=0: {val_zero:.4f}")

print()

print("=" * 70)
print("PART C: Archimedean local factor")
print("=" * 70)
print()

# The archimedean (real) local factor is:
#   Z_infty(s) = pi^{-s/2} Gamma(s/2)
# This is NOT a polynomial in any variable. It is a meromorphic function
# with poles at s = 0, -2, -4, ... (the trivial zeros of zeta).
#
# In the Tate integral framework:
#   Z_infty(s, Phi_infty) = integral_{R*} Phi_infty(x) |x|^s d*x
# For Phi_infty(x) = e^{-pi x^2} (Gaussian):
#   = 2 integral_0^infty e^{-pi x^2} x^s dx/x = pi^{-s/2} Gamma(s/2)

print("Archimedean local factor:")
print("  Z_infty(s) = pi^{-s/2} Gamma(s/2)")
print("  This is NOT a polynomial in any variable.")
print("  It has poles at s = 0, -2, -4, -6, ...")
print("  These correspond to the trivial zeros of the completed zeta.")
print()
print("The archimedean factor breaks the polynomial structure.")
print("Even if all p-adic local factors are polynomials (they are, degree 1),")
print("the archimedean factor is transcendental.")
print()

# Show the Gamma values at key points
print("Z_infty(s) values at key points:")
for s_val in [0.5, 1.0, 2.0, 0.5 + 14.134725j]:
    if isinstance(s_val, complex):
        val = mpmath.power(mpmath.pi, -s_val/2) * mpmath.gamma(s_val/2)
        print(f"  s = 1/2 + i*14.13... : |Z_infty| = {float(abs(val)):.6f}")
    else:
        val = mpmath.power(mpmath.pi, -s_val/2) * mpmath.gamma(s_val/2)
        print(f"  s = {s_val}: Z_infty = {float(val):.6f}")

print()

print("=" * 70)
print("PART D: The variable mismatch - w vs z_p")
print("=" * 70)
print()

# The R25 analysis uses w = e^{s-1/2} so critical line -> |w| = 1.
# The local analysis uses z_p = p^{-s} so |z_p| = 1 at Re(s) = 0.
#
# These give DIFFERENT unit circles!
# - In the w-variable: critical line Re(s)=1/2 -> |w| = 1
# - In the z_p-variable: imaginary axis Re(s)=0 -> |z_p| = 1
#
# The adelic Lee-Yang approach needs the LOCAL zeros on |z_p| = 1
# to combine into GLOBAL zeros on Re(s) = 1/2.
# But |z_p| = 1 at Re(s) = 0 and |z_p| = p^{-1/2} at Re(s) = 1/2.
#
# For the Lee-Yang self-dual locus to match the critical line,
# we need a CHANGE OF VARIABLE at each prime.

print("Variable mismatch between local and global Lee-Yang:")
print()
print("Global (R25): w = e^{s-1/2}")
print("  Critical line Re(s)=1/2 -> |w| = 1")
print("  Functional equation: w -> 1/w")
print()
print("Local at p:   z_p = p^{-s}")
print("  Unit circle |z_p| = 1 at Re(s) = 0 (NOT 1/2)")
print("  To get |z_p| = 1 at Re(s) = 1/2, need z_p = p^{-(s-1/2)} = p^{1/2} * p^{-s}")
print()

# If we define w_p = p^{-(s-1/2)} = p^{1/2-s}, then:
# |w_p| = p^{1/2-Re(s)} = 1 iff Re(s) = 1/2. Good!
# The local Euler factor becomes:
# 1 - z_p = 1 - p^{-s} = 1 - p^{-1/2} * w_p
# In terms of w_p: 1 - p^{-1/2} * w_p. Zero at w_p = p^{1/2}.
# |w_p| = p^{1/2} > 1. NOT on the unit circle!

print("Attempt: define w_p = p^{1/2-s} so |w_p| = 1 at Re(s) = 1/2.")
print()
for p in [2, 3, 5, 7]:
    zero_loc = float(p ** 0.5)
    print(f"  p={p}: 1/Z_p = 1 - p^{{-1/2}} w_p, zero at w_p = p^{{1/2}} = {zero_loc:.4f}")
    print(f"         |w_p| = {zero_loc:.4f} > 1. NOT on unit circle.")
print()
print("The zero of each local factor is at |w_p| = p^{1/2} > 1,")
print("which is OUTSIDE the unit circle in the w_p variable.")
print("Lee-Yang requires zeros ON |w_p| = 1. FAILS.")
print()

print("=" * 70)
print("PART E: Does the Schwartz-Bruhat polynomial structure help?")
print("=" * 70)
print()

# At each prime p, Schwartz-Bruhat functions on Q_p are locally constant
# with compact support. The STANDARD choice is Phi_p = char(Z_p).
# But we can also choose Phi_p = char(p^{-N} Z_p) for some N >= 0.
#
# For Phi_p = char(p^{-N} Z_p):
#   Z_p(s, Phi_p) = integral_{Q_p*} char(p^{-N} Z_p)(x) |x|_p^s d*x
#                 = sum_{k=-N}^{infty} integral_{p^k Z_p*} |x|^s d*x
#                 = sum_{k=-N}^{infty} p^{-ks} (1 - 1/p)
#                 = (1-1/p) * p^{Ns} * sum_{k=0}^{infty} p^{-ks}
#                 = p^{Ns} (1 - 1/p) / (1 - p^{-s})
#
# This is still (1 - p^{-s})^{-1} times a constant, NOT a polynomial.
#
# For a GENERAL Schwartz-Bruhat function:
# Phi_p = sum_{j} a_j char(x_j + p^{n_j} Z_p)
# (finite sum of translates of characteristic functions)
# The local zeta integral becomes a FINITE sum of terms p^{-ks}
# for finitely many k values. THIS IS a polynomial in z_p = p^{-s}!

print("General Schwartz-Bruhat function on Q_p:")
print("  Phi_p = sum_j a_j * char(x_j + p^{n_j} Z_p)")
print("  (finite sum of translates of characteristic functions)")
print()
print("Local zeta integral:")
print("  Z_p(s, Phi_p) = integral Phi_p(x) |x|_p^s d*x")
print("  = finite sum of terms c_k * p^{-ks}")
print("  = POLYNOMIAL in z_p = p^{-s}!")
print()
print("YES: for a general Schwartz-Bruhat function, the local zeta")
print("integral IS a polynomial in z_p = p^{-s}.")
print()
print("BUT: for the STANDARD choice Phi_p = char(Z_p), the integral")
print("gives (1-p^{-s})^{-1}, which is NOT a polynomial (infinite series).")
print()
print("The polynomial structure requires NON-STANDARD Schwartz-Bruhat")
print("functions. But then the global zeta integral is NOT zeta(s).")
print("It is a different function zeta_A(s, Phi) for a different Phi.")
print()

# For the standard Phi_0 = prod_v Phi_v that gives zeta(s):
# At almost all primes: Phi_p = char(Z_p) -> Z_p = (1-p^{-s})^{-1}
# If we modify finitely many Phi_p, we get zeta(s) * (finite correction)
# But the infinite product over remaining primes is still not a polynomial.

print("Even modifying finitely many local functions:")
print("  zeta_A(s, Phi') = [finite polynomial] * prod_{p not in S} (1-p^{-s})^{-1}")
print("  The infinite tail product is still NOT a polynomial.")
print("  So the GLOBAL function is never a polynomial in z_p.")
print()

print("=" * 70)
print("PART F: The infinite product convergence problem")
print("=" * 70)
print()

# Even if each local factor WERE a Lee-Yang polynomial (zeros on |z_p|=1),
# the INFINITE product of polynomials is NOT a polynomial.
# The Asano contraction theorem applies to FINITE products.
# For infinite products, additional conditions are needed.
#
# Specifically: the Asano contraction of n factors gives a polynomial
# of degree <= sum of individual degrees. As n -> infty, this degree
# goes to infinity. The limiting function need not have all zeros on
# the unit circle even if each finite truncation does.
#
# Classical example: e^z = lim_{n->infty} (1 + z/n)^n
# Each factor (1+z/n) has zero at z = -n (on the real line).
# The product (1+z/n)^n has all n zeros at z = -n.
# The limit e^z has NO zeros at all.
# The zero location property is NOT preserved in the limit.

print("Infinite product of Lee-Yang polynomials:")
print()
print("Classical example: e^z = lim (1 + z/n)^n")
print("Each (1+z/n) has zero at z = -n.")
print("The limit e^z has NO zeros.")
print("Lee-Yang property is NOT preserved under infinite products.")
print()

# For the Euler product: prod_p (1 - z_p) with z_p = p^{-s}
# At Re(s) > 1: this converges to 1/zeta(s), which has zeros at
# the nontrivial zeros of zeta (i.e., at the Riemann zeros).
# These are on Re(s) = 1/2 (if RH holds).
# In the z_p variables: Re(s) = 1/2 gives |z_p| = p^{-1/2},
# NOT on the unit circle.

# Compute: for each known zero of zeta, what is |z_p|?
print("At the first nontrivial zero rho_1 = 1/2 + i*14.134725...:")
gamma1 = mpmath.mpf('14.134725141734693790')
s1 = mpmath.mpf('0.5') + 1j * gamma1

for p in [2, 3, 5, 7]:
    z_p = mpmath.power(p, -s1)
    mod_z_p = abs(z_p)
    print(f"  p={p}: |z_p| = |p^{{-rho_1}}| = p^{{-1/2}} = {float(mod_z_p):.10f}")

print()
print(f"  All have |z_p| = p^{{-1/2}} < 1. INSIDE unit disk, not on boundary.")
print()

print("=" * 70)
print("PART G: The functional equation in adelic language")
print("=" * 70)
print()

# Tate's thesis: the global functional equation is
#   zeta_A(s, Phi) = zeta_A(1-s, Phi_hat)
# where Phi_hat is the adelic Fourier transform of Phi.
#
# In the Lee-Yang framework, the involution s -> 1-s maps w -> 1/w
# (from R25). The functional equation says:
#   Z(w) = Z(1/w) * [correction from Phi -> Phi_hat]
#
# For the Lee-Yang theorem, we need Z(z) and Z(1/z) to be related
# by conjugation (for real partition functions: Z(1/z) = Z(z) up to
# a monomial factor). The adelic FE gives:
#   zeta_A(s, Phi) = zeta_A(1-s, Phi_hat)
# which relates Z at s to Z at 1-s with a DIFFERENT test function.
#
# This is NOT the Lee-Yang involution unless Phi_hat = Phi
# (self-dual Schwartz-Bruhat function).

print("Adelic functional equation (Tate's thesis):")
print("  zeta_A(s, Phi) = zeta_A(1-s, Phi_hat)")
print()
print("For Lee-Yang involution z -> 1/z, we need:")
print("  Z(z) related to Z(1/z) with the SAME coefficients.")
print()
print("The adelic FE changes Phi to Phi_hat. This is NOT a pure involution")
print("unless Phi is self-dual (Phi_hat = Phi).")
print()

# The standard Gaussian Phi_infty = e^{-pi x^2} IS self-dual:
# hat{Phi}_infty = Phi_infty (Fourier transform of Gaussian is Gaussian).
# At each prime p: char(Z_p) is also self-dual:
# hat{char(Z_p)} = char(Z_p) (under the standard normalization).
# So the standard Phi_0 = prod_v Phi_v IS self-dual!

print("However: the STANDARD Schwartz-Bruhat function IS self-dual:")
print("  Phi_infty = e^{-pi x^2}: Fourier self-dual (Gaussian)")
print("  Phi_p = char(Z_p): Fourier self-dual (standard p-adic character)")
print("  So Phi_0 = prod_v Phi_v is self-dual: Phi_hat_0 = Phi_0")
print()
print("For the standard choice, the FE IS a pure involution:")
print("  zeta_A(s, Phi_0) = zeta_A(1-s, Phi_0)")
print("  i.e., xi(s) = xi(1-s)")
print()
print("This confirms: the functional equation = Lee-Yang involution.")
print("Condition (3) SATISFIED (same conclusion as R25).")
print()

print("=" * 70)
print("PART H: Summary of adelic Lee-Yang conditions")
print("=" * 70)
print()

print("| Condition | Archimedean (R25) | p-adic local | Adelic global |")
print("|-----------|-------------------|--------------|---------------|")
print("| (1) Polynomial | FAILS (Gamma)  | PARTIAL*     | FAILS         |")
print("| (2) Ferromagnetic | FAILS (Mobius) | N/A**       | FAILS         |")
print("| (3) Involution | SATISFIED       | SATISFIED    | SATISFIED     |")
print()
print("* Each local p-adic factor (1-z_p) IS a polynomial with zero on")
print("  |z_p|=1, but in the WRONG variable. In the variable w_p that puts")
print("  the critical line on |w_p|=1, the zero is at |w_p| = p^{1/2} > 1.")
print()
print("** The local factors individually have non-negative structure,")
print("  but the Mobius function signs emerge from the PRODUCT structure")
print("  (inclusion-exclusion over primes). Ferromagnetism is not well-")
print("  defined for a single degree-1 polynomial.")
print()

print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print()
print("The adelic formulation does NOT change the Lee-Yang analysis.")
print("The same two obstructions from R25 persist:")
print()
print("1. POLYNOMIAL OBSTRUCTION: The archimedean factor pi^{-s/2}Gamma(s/2)")
print("   is transcendental. Even if every p-adic local factor is a degree-1")
print("   polynomial, the infinite product + archimedean factor is not.")
print()
print("2. VARIABLE MISMATCH: The local Lee-Yang locus |z_p|=1 corresponds")
print("   to Re(s)=0, not Re(s)=1/2. In the variable where Re(s)=1/2 maps")
print("   to the unit circle, local zeros are at |w_p|=p^{1/2}>1.")
print()
print("3. INFINITE PRODUCT: Even ignoring (1) and (2), the Asano contraction")
print("   theorem is for FINITE products. Infinite products can lose the")
print("   Lee-Yang property (e.g., e^z = lim (1+z/n)^n).")
print()
print("The adelic language is more natural (local-global structure,")
print("self-dual Fourier transform), but the Lee-Yang obstructions")
print("are STRUCTURAL, not notational. Changing notation does not")
print("change the mathematics.")
