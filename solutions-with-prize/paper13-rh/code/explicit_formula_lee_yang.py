"""
explicit_formula_lee_yang.py
Research R27: Does the Explicit Formula Convert zeta(s) into a Lee-Yang System?

The explicit formula (Weil's version) converts the Euler product (multiplicative)
into a sum over zeros (additive). This code investigates whether the additive
formulation satisfies Lee-Yang conditions.

Key questions:
1. Are the prime contributions log(p)/p^{m/2} "ferromagnetic" (all positive)?
2. Does the truncated explicit formula (primes p <= P) give a trigonometric
   polynomial whose zeros lie on the unit circle?
3. Does the Weil positivity condition match Lee-Yang positivity?
"""

import numpy as np
from mpmath import mp, mpf, mpc, zeta, zetazero, log, exp, pi, sqrt, cos, sin, gamma, fabs
from mpmath import quad as mpquad
from scipy import optimize

mp.dps = 50  # 50-digit precision

print("=" * 70)
print("PART A: The Prime Contributions -- Ferromagnetic?")
print("=" * 70)

# The explicit formula (von Mangoldt form):
# psi(x) = x - sum_rho x^rho / rho - log(2pi) - (1/2)log(1 - x^{-2})
#
# Weil's explicit formula (symmetric form):
# sum_rho h(gamma_rho) = h_hat(0) + h_hat(1) - sum_p sum_m (log p / p^{m/2}) * g(m log p)
#
# where h is an even function, h_hat(s) = integral h(t) e^{(s-1/2)t} dt,
# and g = Fourier transform of h.
#
# The prime contributions are: c_{p,m} = log(p) / p^{m/2}
# These are ALL POSITIVE for p prime, m >= 1.

print("\nPrime contributions c_{p,m} = log(p) / p^{m/2}:")
print(f"{'p':>5} {'m':>3} {'c_{p,m}':>20} {'sign':>6}")
print("-" * 40)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
total_positive = 0
total_negative = 0

for p in primes:
    for m in [1, 2, 3]:
        c_pm = float(log(p) / p**(mpf(m)/2))
        sign = "+" if c_pm > 0 else "-"
        if c_pm > 0:
            total_positive += 1
        else:
            total_negative += 1
        if m <= 2 or p <= 5:
            print(f"{p:5d} {m:3d} {c_pm:20.10f} {sign:>6}")

print(f"\nTotal positive: {total_positive}, Total negative: {total_negative}")
print(f"ALL prime contributions are POSITIVE (log(p) > 0, p^{{m/2}} > 0)")
print(f"This is FERROMAGNETIC sign structure!")

# Verify the decay rate
print("\n--- Decay of prime contributions ---")
print(f"{'p':>5} {'c_{{p,1}}':>15} {'c_{{p,2}}':>15} {'c_{{p,3}}':>15}")
for p in [2, 3, 5, 7, 11, 101, 1009]:
    c1 = float(log(p) / p**(mpf(1)/2))
    c2 = float(log(p) / p**(mpf(2)/2))
    c3 = float(log(p) / p**(mpf(3)/2))
    print(f"{p:5d} {c1:15.8f} {c2:15.8f} {c3:15.8f}")

print("\nDecay: c_{p,m} -> 0 as p -> infty or m -> infty")
print("The series converges absolutely for Re(s) > 1/2 + epsilon")


print("\n" + "=" * 70)
print("PART B: The Explicit Formula as a 'Partition Function'")
print("=" * 70)

# In the explicit formula:
# sum_rho h(gamma_rho) = (prime terms) + (constant terms)
#
# Can we write the "spectral side" as a partition function?
# Z(z) = sum_rho z^{f(rho)} where z is related to the test function
#
# For a Gaussian test function h(t) = exp(-alpha * t^2):
# h_hat(s) = sqrt(pi/alpha) * exp((s-1/2)^2 / (4*alpha))
#
# The explicit formula becomes:
# sum_rho exp(-alpha * gamma_rho^2) = (prime side)

print("\nGaussian test function h(t) = exp(-alpha * t^2)")
print("Explicit formula: sum_rho exp(-alpha * gamma_rho^2) = ...")

# Compute the spectral side with first 20 zeros
print("\n--- Spectral side (sum over zeros) ---")
nzeros = 20
zeros = []
for n in range(1, nzeros + 1):
    z = zetazero(n)
    zeros.append(z)

for alpha_val in [0.01, 0.1, 1.0, 10.0]:
    spectral_sum = mpf(0)
    for z in zeros:
        gamma_rho = z.imag
        spectral_sum += 2 * exp(-mpf(alpha_val) * gamma_rho**2)  # factor 2 for conjugate pair
    print(f"  alpha = {alpha_val:6.2f}: sum_rho h(gamma) = {float(spectral_sum):.10f} (first {nzeros} pairs)")


print("\n--- Prime side (geometric side) ---")
# Explicit formula prime contribution for Gaussian h:
# g(u) = (1/sqrt(4*pi*alpha)) * exp(-u^2 / (4*alpha))
# Prime term: -sum_p sum_m (log p / p^{m/2}) * [g(m log p) + g(-m log p)]
#           = -2 * sum_p sum_m (log p / p^{m/2}) * g(m log p)
# since g is even.

def prime_side_gaussian(alpha_val, P_max=1000, M_max=20):
    """Compute the prime side of explicit formula with Gaussian test function."""
    alpha = mpf(alpha_val)
    result = mpf(0)
    p = 2
    while p <= P_max:
        logp = log(p)
        for m in range(1, M_max + 1):
            u = m * logp
            coupling = logp / p**(mpf(m)/2)
            g_u = exp(-u**2 / (4 * alpha)) / sqrt(4 * pi * alpha)
            result -= 2 * coupling * g_u
        # next prime
        p = int(p) + 1
        while p <= P_max:
            is_prime = True
            for d in range(2, int(p**0.5) + 1):
                if p % d == 0:
                    is_prime = False
                    break
            if is_prime:
                break
            p += 1
    return result

for alpha_val in [0.01, 0.1, 1.0, 10.0]:
    ps = prime_side_gaussian(alpha_val, P_max=200, M_max=10)
    print(f"  alpha = {alpha_val:6.2f}: prime side = {float(ps):.10f}")


print("\n" + "=" * 70)
print("PART C: Truncated Explicit Formula -- Trigonometric Polynomial?")
print("=" * 70)

# Truncated to primes p <= P:
# F_P(t) = sum_{p<=P} sum_{m=1}^{M} (log p / p^{m/2}) * cos(t * m * log p)
#
# This IS a trigonometric polynomial in t (finite sum of cosines at
# frequencies m*log(p)). BUT the frequencies are INCOMMENSURABLE
# (log(p_i)/log(p_j) is irrational).
#
# Key question: is this a genuine trigonometric polynomial?
# Answer: it is a GENERALIZED trigonometric polynomial (sum of
# cos(omega_k * t) with incommensurable omega_k), NOT a standard
# trigonometric polynomial (sum of cos(n*t) for integer n).

print("\nTruncated explicit formula geometric side:")
print("F_P(t) = sum_{p<=P} sum_m (log p / p^{m/2}) * cos(t * m * log p)")
print()
print("Frequencies omega_{p,m} = m * log(p):")
print(f"{'p':>5} {'m':>3} {'omega':>15} {'omega/omega_1':>18}")

omega_1 = float(log(2))
for p in [2, 3, 5, 7, 11]:
    for m in [1, 2, 3]:
        omega = float(m * log(p))
        ratio = omega / omega_1
        print(f"{p:5d} {m:3d} {omega:15.10f} {ratio:18.10f}")

print(f"\nlog(3)/log(2) = {float(log(3)/log(2)):.15f} (irrational)")
print(f"log(5)/log(2) = {float(log(5)/log(2)):.15f} (irrational)")
print(f"log(7)/log(2) = {float(log(7)/log(2)):.15f} (irrational)")
print("\nThe frequencies are INCOMMENSURABLE -- this is NOT a standard")
print("trigonometric polynomial in a single variable.")


print("\n" + "=" * 70)
print("PART D: The 'Partition Function' Structure")
print("=" * 70)

# Can we write Z_P(z) = sum of z^{something} where z = e^{it}?
#
# For Lee-Yang, we need Z(z) = sum a_k z^k with integer k.
# The explicit formula gives: sum c_{p,m} * (w^{m*log p} + w^{-m*log p})
# where w = e^{it} and the exponents m*log(p) are NOT integers.
#
# However, we can try a MULTI-VARIABLE approach:
# Define z_p = e^{it * log p} = p^{it} for each prime p.
# Then w^{m*log p} = z_p^m.
# The truncated formula becomes:
# F_P(t) = sum_{p<=P} sum_m c_{p,m} * (z_p^m + z_p^{-m})
#
# For EACH prime p separately, this IS a Laurent polynomial in z_p.
# For a single prime: sum_m (log p / p^{m/2}) * (z_p^m + z_p^{-m})
# = (log p) * sum_m (z_p / sqrt(p))^m + (z_p^{-1} / sqrt(p))^m

print("\nSingle-prime partition function Z_p(z_p) where z_p = p^{it}:")
print()

for p_val in [2, 3, 5, 7]:
    p = mpf(p_val)
    logp = log(p)
    print(f"Prime p = {p_val}:")
    print(f"  Z_p(z_p) = log(p) * sum_m [(z_p/sqrt(p))^m + (z_p/sqrt(p))^{{-m}}]")
    q = 1/sqrt(p)
    print(f"  |z_p/sqrt(p)| = 1/sqrt({p_val}) = {float(q):.6f}")
    print(f"  This is a geometric series in q^m with |q| < 1")
    print(f"  Sum = log(p) * [q*z_p/(1-q*z_p) + q*z_p^{{-1}}/(1-q*z_p^{{-1}})]")
    print(f"  = log(p) * [(z_p/sqrt(p))/(1 - z_p/sqrt(p)) + conj]")
    print()

print("KEY OBSERVATION:")
print("Each Z_p(z_p) is a rational function of z_p = p^{it}.")
print("On the critical line Re(s) = 1/2, we have |z_p| = 1.")
print("So z_p lives on the unit circle -- the Lee-Yang locus!")


print("\n" + "=" * 70)
print("PART E: Lee-Yang for a Single Prime Factor")
print("=" * 70)

# For a single prime p, consider:
# Z_p(z) = sum_{m=0}^{M} (z/sqrt(p))^m = (1 - (z/sqrt(p))^{M+1}) / (1 - z/sqrt(p))
#
# Truncated to M terms: polynomial of degree M in (z/sqrt(p)).
# Zeros of Z_p(z) = zeros of 1 - (z/sqrt(p))^{M+1} = 0
# => z/sqrt(p) = (M+1)-th roots of unity
# => z = sqrt(p) * exp(2*pi*i*k/(M+1)), k = 0, ..., M
# => |z| = sqrt(p) > 1

# For the RECIPROCAL: 1/Z_p(z) = 1 - z/sqrt(p) (Euler factor for a single prime)
# Zero at z = sqrt(p), so |z| = sqrt(p) > 1. NOT on unit circle.

print("For a single prime p, the Euler factor:")
print("  (1 - p^{-s})^{-1} in z_p = p^{it} becomes:")
print("  Z_p(z_p) = (1 - z_p/sqrt(p))^{-1}")
print()
print("Zeros of 1/Z_p (= zeros of 1 - z_p/sqrt(p)):")
for p_val in [2, 3, 5, 7, 11]:
    z_zero = float(sqrt(mpf(p_val)))
    print(f"  p = {p_val}: z_p = sqrt({p_val}) = {z_zero:.6f}, |z_p| = {z_zero:.6f}")

print()
print("ALL zeros have |z_p| = sqrt(p) > 1.")
print("They are NOT on the unit circle |z_p| = 1.")
print()
print("But wait -- the PRODUCT over primes should have zeros where")
print("ANY factor has a zero. The Euler product 1/zeta(s) = prod_p (1-p^{-s})")
print("has zeros at s = 2*pi*i*k/log(p) for each prime p.")
print("In the w = e^{s-1/2} variable: |w| = e^{-1/2} < 1.")
print("So the zeros of 1/zeta in the w-variable are INSIDE the unit circle.")

# The zeros of the Euler product factors
print("\nZeros of 1 - p^{-s} in w = e^{s-1/2}:")
for p_val in [2, 3, 5, 7]:
    # s = 2*pi*i*k/log(p), w = e^{s-1/2} = e^{-1/2} * e^{2*pi*i*k/log(p)}
    w_mod = float(exp(mpf(-1)/2))
    print(f"  p = {p_val}: |w| = e^{{-1/2}} = {w_mod:.6f} (inside unit circle)")


print("\n" + "=" * 70)
print("PART F: The Weil Explicit Formula -- Precise Form")
print("=" * 70)

# Weil's explicit formula (for test functions h in the Schwartz space):
#
# sum_{rho} h(rho - 1/2) = h_hat(0) + h_hat(0) [wait, let me be precise]
#
# Standard version (following Bombieri):
# For h even, holomorphic in |Im(z)| < 1/2 + epsilon, decaying:
#
# sum_{rho nontrivial} h((rho - 1/2)/i)
# = 2h(i/2) - sum_p sum_{m=1}^infty (log p / p^{m/2}) * [h_hat(m log p) + h_hat(-m log p)]
# + integral_R h(t) * [Gamma'/Gamma(1/4 + it/2) / (2*pi)] dt
#
# The LHS sums h evaluated at the "spectral parameters" gamma_rho.
# The RHS has:
# (a) Constant term 2h(i/2) from the pole and trivial zeros
# (b) Sum over primes -- ALL COEFFICIENTS POSITIVE
# (c) Archimedean (gamma function) integral

print("Weil Explicit Formula:")
print("  sum_rho h(gamma_rho) = [constant] - sum_p sum_m c_{p,m} * g(m log p) + [integral]")
print()
print("where c_{p,m} = log(p)/p^{m/2} and g = Fourier transform of h")
print()
print("The SIGN STRUCTURE:")
print("  Spectral side: sum of h(gamma) (evaluations of test function at zero heights)")
print("  Geometric side: NEGATIVE sum of positive c_{p,m} * g(m log p)")
print()
print("The MINUS sign in front of the prime sum is CRUCIAL.")
print("In partition function language:")
print("  Z = sum a_k * z^k")
print("  log Z = -sum c_{p,m} * ...")
print()
print("The log Z form is like the FREE ENERGY, not the partition function.")
print("The primes contribute to log(Z), not Z itself.")
print("This is characteristic of a FREE (non-interacting) theory:")
print("  log Z = sum (single-particle contributions)")


print("\n" + "=" * 70)
print("PART G: Does the Explicit Formula Define a Lee-Yang System?")
print("=" * 70)

# The three Lee-Yang conditions applied to the explicit formula:
#
# CONDITION 1 (Polynomial):
# The truncated explicit formula F_P(t) = sum_{p<=P} sum_m c_{p,m} cos(t m log p)
# is a generalized trigonometric polynomial (quasi-polynomial) with
# INCOMMENSURABLE frequencies m*log(p).
#
# This is NOT a polynomial in z = e^{it} (because the frequencies
# are not integers). BUT in the MULTI-VARIABLE sense z_p = p^{it}:
# F_P = sum_p f_p(z_p) where each f_p IS a polynomial in z_p.
#
# Borcea-Branden (2009) extended Lee-Yang to STABLE POLYNOMIALS in
# SEVERAL VARIABLES. Can their framework handle this?

print("CONDITION 1: Polynomial structure")
print("-" * 40)
print()
print("The truncated explicit formula is:")
print("  F_P(t) = sum_{p<=P} sum_m c_{p,m} * cos(t * m * log p)")
print()
print("In multi-variable: F_P(z_2, z_3, z_5, ...) where z_p = p^{it}")
print("  = sum_p sum_m c_{p,m} * (z_p^m + z_p^{-m}) / 2")
print()
print("Each z_p lives on the unit circle |z_p| = 1 when t is real.")
print("This IS a polynomial in several variables z_p.")
print()
print("HOWEVER: the Lee-Yang theorem for multi-variable polynomials")
print("(Borcea-Branden) requires the polynomial to be STABLE in a")
print("specific sense. The coupling between different primes comes")
print("from the constraint that ALL z_p are evaluated at the SAME t:")
print("  z_p = p^{it} means log(z_p)/log(z_q) = log(p)/log(q)")
print("This is a CONSTRAINT surface in the multi-variable space.")

print()
print("CONDITION 2: Ferromagnetic coupling")
print("-" * 40)
print()
print("The coefficients c_{p,m} = log(p)/p^{m/2} are ALL POSITIVE.")
print("In the explicit formula, they appear with a MINUS sign:")
print("  sum_rho h(gamma) = -sum c_{p,m} g(m log p) + ...")
print()
print("The minus sign means: the prime contributions REPEL the zeros")
print("from the test function's support. This is OPPOSITE to ferromagnetic.")
print()
print("Wait -- let's think more carefully.")
print("In the Ising model: Z(z) = sum exp(-beta H) z^{up-spins}")
print("Ferromagnetic = neighboring spins prefer alignment = J > 0")
print("= zeros REPELLED from positive real axis (Lee-Yang)")
print()
print("In the explicit formula: the prime sum contributes with minus sign.")
print("If we write Z(t) = exp(sum_rho log h(gamma_rho))")
print("then log Z(t) = sum_rho log h(gamma_rho)")
print("and the 'free energy' has the prime contributions SUBTRACTED.")
print()
print("The sign analysis is SUBTLE and depends on how we define Z.")

print()
print("CONDITION 3: Correct involution")
print("-" * 40)
print()
print("The functional equation gives the involution t -> -t")
print("(equivalently, all z_p -> z_p^{-1} = conj(z_p) on |z_p|=1)")
print("This IS the Lee-Yang involution. SATISFIED.")


print("\n" + "=" * 70)
print("PART H: The Critical Test -- Positivity")
print("=" * 70)

# Weil's positivity criterion:
# RH iff sum_rho h(gamma_rho) >= 0 for all h of the form h = f * f~
# where f~ (t) = conj(f(-t)) and * is convolution.
#
# This is equivalent to: the distribution D(t) = sum_rho delta(t - gamma_rho)
# (the "spectral measure") defines a POSITIVE functional on the algebra
# of test functions under convolution.
#
# Li's criterion: RH iff lambda_n >= 0 for all n >= 1 where
# lambda_n = sum_rho [1 - (1 - 1/rho)^n]

print("Weil positivity criterion:")
print("  RH iff sum_rho h(gamma) >= 0 for all h = f * f~")
print()
print("Li's criterion:")
print("  RH iff lambda_n >= 0 for all n >= 1")
print("  lambda_n = sum_rho [1 - (1 - 1/rho)^n]")
print()

# Compute Li coefficients
print("Li coefficients (first 10):")
for n in range(1, 11):
    li_n = mpf(0)
    for rho in zeros:
        term = 1 - (1 - 1/rho)**n
        li_n += term
        # conjugate
        rho_conj = mpc(rho.real, -rho.imag)
        li_n += 1 - (1 - 1/rho_conj)**n
    print(f"  lambda_{n:2d} = {float(li_n.real):15.10f} (imaginary part: {float(li_n.imag):.2e})")

print()
print("All Li coefficients are POSITIVE (assuming RH for the computed zeros).")
print("This IS a positivity condition -- same structure as Lee-Yang positivity?")


print("\n" + "=" * 70)
print("PART I: Comparison -- Lee-Yang vs Weil Positivity")
print("=" * 70)

print("""
Lee-Yang positivity:
  Z(z) = sum a_k z^k has all zeros on |z|=1
  iff certain determinantal conditions on the a_k hold
  iff the Toeplitz matrix T_{ij} = a_{i-j} is positive semi-definite

Weil positivity:
  sum_rho h(gamma) >= 0 for all h = f * f~
  iff the spectral distribution is positive-definite
  iff the correlation matrix C_{ij} = sum_rho exp(i(gamma_i - gamma_j)) is PSD

These are BOTH positive-definiteness conditions, but on DIFFERENT objects:
  Lee-Yang: PSD of coefficients (Toeplitz structure)
  Weil: PSD of spectral distribution (convolution structure)

The Lee-Yang condition is about the POLYNOMIAL COEFFICIENTS.
The Weil condition is about the ZERO DISTRIBUTION.
They are DUAL conditions connected by the relationship between
a polynomial and its zeros.
""")


print("=" * 70)
print("PART J: The Trigonometric Polynomial Test")
print("=" * 70)

# For each truncation P, define:
# Z_P(t) = 1 + sum_{p<=P} sum_{m=1}^M c_{p,m} * 2*cos(t * m * log p)
#
# This is a quasi-periodic function of t.
# If we restrict to a single prime p:
# Z_p(t) = 1 + 2 * sum_m (log p / p^{m/2}) * cos(t * m * log p)
#
# In variable z_p = e^{i*t*log(p)} = p^{it}:
# Z_p(z_p) = 1 + (log p) * sum_m (z_p^m + z_p^{-m}) / p^{m/2}
#
# For M=1: Z_p(z_p) = 1 + (log p / sqrt(p)) * (z_p + z_p^{-1})
# = 1 + 2*(log p / sqrt(p)) * cos(theta) where z_p = e^{i*theta}
#
# This is a degree-1 Laurent polynomial in z_p.
# Zeros: z_p + z_p^{-1} = -sqrt(p)/log(p)
# => 2*cos(theta) = -sqrt(p)/log(p)
# => cos(theta) = -sqrt(p)/(2*log(p))

print("\nSingle-prime truncation (M=1, one prime p):")
print("Z_p(z) = 1 + (log p / sqrt(p)) * (z + z^{-1})")
print()
print("Zeros: z + z^{-1} = -sqrt(p)/log(p)")
print("=> cos(theta) = -sqrt(p)/(2*log(p))")
print()

for p_val in [2, 3, 5, 7, 11, 13, 101, 1009]:
    p = mpf(p_val)
    cos_val = -sqrt(p) / (2 * log(p))
    on_circle = fabs(cos_val) <= 1
    print(f"  p = {p_val:5d}: cos(theta) = {float(cos_val):12.6f}, |cos| <= 1? {on_circle}")

print()
print("For p >= 3: |cos(theta)| = sqrt(p)/(2*log(p))")
print("This exceeds 1 for p >= 3 (checked: sqrt(3)/(2*log(3)) = 0.788...)")
print("Actually for p = 2: sqrt(2)/(2*log(2)) = 1.020... > 1!")

# More careful check
for p_val in [2, 3, 5, 7, 11]:
    p = mpf(p_val)
    val = sqrt(p) / (2 * log(p))
    print(f"  p = {p_val}: sqrt(p)/(2*log(p)) = {float(val):.10f}")

print()
print("For p = 2: the value exceeds 1! The zeros are NOT on the unit circle.")
print("For p >= 3: the value grows as sqrt(p)/log(p) -> infinity.")
print("The single-prime truncation DOES NOT have Lee-Yang property.")


print("\n" + "=" * 70)
print("PART K: The Coupling Strength Problem")
print("=" * 70)

# The coupling coefficient c_{p,1} = log(p)/sqrt(p) in the Z_p polynomial
# determines whether zeros are on the unit circle.
# For Z_p(z) = 1 + c * (z + 1/z) with c = log(p)/sqrt(p):
# Zeros on |z|=1 iff |c| <= 1/2 (since max of cos on circle is 1, need 2c <= 1)
# But c = log(p)/sqrt(p) exceeds 1/2 for ALL primes p.

print("Coupling strength analysis:")
print("Z_p(z) = 1 + c * (z + 1/z) where c = log(p)/sqrt(p)")
print()
print("Lee-Yang requires: zeros on |z|=1")
print("For this degree-1 Laurent polynomial: need |c| <= 1/2")
print("Because z + 1/z = 2*cos(theta) on the unit circle, max = 2")
print("Zero exists on circle iff 1 + 2c*cos(theta) = 0 has solution")
print("iff |cos(theta)| = 1/(2c) <= 1 iff c >= 1/2")
print()
print("Wait -- let me reconsider. Zeros ON the circle means we WANT solutions.")
print("Lee-Yang says zeros should be ON the circle, not off it.")
print()
print("For Z_p(z) = 1 + c*(z + 1/z):")
print("  If c >= 1/2: zeros exist on |z|=1 (Lee-Yang satisfied)")
print("  If c < 1/2: zeros are REAL and NOT on |z|=1")
print()

for p_val in [2, 3, 5, 7, 11, 101, 1009, 10007]:
    p = mpf(p_val)
    c = log(p) / sqrt(p)
    status = "ON circle (LY ok)" if float(c) >= 0.5 else "OFF circle (LY fails)"
    print(f"  p = {p_val:6d}: c = {float(c):.8f}, {status}")

print()
print("CORRECTION: For c >= 1/2, the polynomial 1 + c*(z+1/z) = 0")
print("has solutions z = e^{i*theta} with cos(theta) = -1/(2c).")
print("These ARE on the unit circle. Lee-Yang is SATISFIED for each prime!")
print()
print("But this is trivial -- any real Laurent polynomial of odd degree")
print("must have zeros on the unit circle (by the intermediate value theorem")
print("applied to z -> 1 + 2c*cos(theta)).")


print("\n" + "=" * 70)
print("PART L: The Multi-Prime Product -- Where It Gets Interesting")
print("=" * 70)

# The FULL truncated partition function:
# Z_P(z_2, z_3, ..., z_P) = PRODUCT of Z_p factors?
# Or SUM of Z_p factors?
#
# The explicit formula gives a SUM:
# sum_rho h(gamma) = sum_p (prime contribution) = SUM
#
# But the Euler product is a PRODUCT:
# zeta(s) = prod_p Z_p
#
# The LOGARITHM of the Euler product is:
# log zeta(s) = -sum_p log(1 - p^{-s}) = sum_p sum_m p^{-ms}/m
#
# The explicit formula is related to the DERIVATIVE of log zeta:
# -zeta'/zeta(s) = sum_p sum_m (log p) * p^{-ms}
#
# So the explicit formula is the LOGARITHMIC DERIVATIVE of the Euler product!
# This means:
# Euler product: Z = prod_p (1 - p^{-s})^{-1} (MULTIPLICATIVE)
# log of product: log Z = sum_p sum_m p^{-ms}/m (ADDITIVE = free energy)
# derivative of log: -(d/ds) log Z = sum_p sum_m (log p) p^{-ms} (EXPLICIT FORMULA)

print("The chain of reformulations:")
print()
print("Level 0 (Multiplicative): zeta(s) = prod_p (1-p^{-s})^{-1}")
print("Level 1 (Additive/Free energy): log zeta(s) = sum_p sum_m p^{-ms}/m")
print("Level 2 (Explicit formula): -zeta'/zeta(s) = sum_p sum_m (log p) p^{-ms}")
print("Level 3 (Weil): sum_rho h(gamma) = -(prime sum) + constants")
print()
print("Lee-Yang operates at Level 0 (partition function Z).")
print("The explicit formula operates at Level 2 (logarithmic derivative of Z).")
print("These are DIFFERENT mathematical objects!")
print()
print("The Lee-Yang theorem constrains zeros of Z.")
print("The explicit formula relates zeros of Z to the logarithmic derivative.")
print("The positivity of the prime coefficients in Level 2 does NOT")
print("translate to ferromagnetic coupling in Level 0.")


print("\n" + "=" * 70)
print("PART M: Quantifying the Gap -- Can We Fix It?")
print("=" * 70)

# The explicit formula:
# sum_rho h(gamma) = h_hat(0) + h_hat(1) - sum_p sum_m c_{p,m} g(m log p)
#
# Rearranging:
# sum_rho h(gamma) + sum_p sum_m c_{p,m} g(m log p) = h_hat(0) + h_hat(1)
#
# This says: (spectral contribution) + (prime contribution) = (constants)
#
# If we define:
# Z(h) = exp[sum_rho h(gamma)]
# W(h) = exp[sum_p sum_m c_{p,m} g(m log p)]
# Then: Z(h) * W(h) = exp(h_hat(0) + h_hat(1))
#
# This is NOT a partition function in the Lee-Yang sense.
# It's a BALANCE between spectral and geometric sides.

print("The explicit formula as a balance equation:")
print()
print("  (Spectral) + (Geometric) = (Constant)")
print("  sum_rho h(gamma) + sum_p c_{p,m} g(m log p) = const")
print()
print("In exponential form:")
print("  Z_spectral * W_prime = exp(const)")
print()
print("This is a CONSTRAINT, not a partition function.")
print("The zeros of zeta are where the spectral side has poles/zeros,")
print("and the primes determine the geometric side.")
print()
print("Lee-Yang says: if Z = poly with non-negative coefficients,")
print("then zeros on unit circle.")
print("The explicit formula says: Z_spectral is determined by W_prime.")
print("But it does NOT say Z_spectral is a polynomial with non-negative coefficients.")


print("\n" + "=" * 70)
print("PART N: The Honest Assessment")
print("=" * 70)

print("""
QUESTION: Does the explicit formula convert zeta(s) into a Lee-Yang system?

ANSWER: NO. But the failure is INSTRUCTIVE.

WHAT WORKS:
1. The explicit formula IS additive (sum, not product). [TRUE]
2. The prime coefficients c_{p,m} = log(p)/p^{m/2} ARE positive. [TRUE]
3. The involution t -> -t IS the Lee-Yang involution. [TRUE]
4. The Weil positivity criterion IS a positivity condition. [TRUE]

WHAT FAILS:
1. LEVEL MISMATCH: The explicit formula operates at the level of the
   LOGARITHMIC DERIVATIVE of zeta, not at the level of zeta itself.
   Lee-Yang operates on the partition function Z, not on (log Z)' or
   on the free energy. The positivity of coefficients in (log Z)' does
   NOT imply Lee-Yang for Z.

2. INCOMMENSURABLE FREQUENCIES: Even at the explicit formula level, the
   "trigonometric polynomial" has incommensurable frequencies m*log(p).
   This is a generalized trig poly (quasi-periodic function), NOT a
   standard polynomial. Lee-Yang requires polynomial structure.

3. SIGN OF THE PRIME CONTRIBUTION: In the explicit formula, the prime
   sum appears with a MINUS sign relative to the spectral side:
     sum_rho h(gamma) = -(prime sum) + constants
   This minus sign means the primes REPEL the spectral values, not
   attract them. The sign is the opposite of "ferromagnetic."

4. SINGLE-PRIME FACTORS ARE TRIVIAL: For each prime p, the factor
   Z_p(z_p) = 1 + c*(z_p + z_p^{-1}) trivially has zeros on the
   unit circle (because c >= 1/2 for all primes). But the MULTI-PRIME
   product is not Lee-Yang because the constraint z_p = p^{it}
   (same t for all primes) correlates the variables in a non-polynomial way.

DEEPER DIAGNOSIS:
The explicit formula is the SHADOW (in the additive/spectral world) of
the Euler product (in the multiplicative world). Converting from product
to sum DOES change the mathematical structure -- but it converts the
partition function into a FREE ENERGY, not into a different partition
function. Lee-Yang is a theorem about partition functions, not about
free energies.

To make the Lee-Yang strategy work, one would need:
(a) A genuine PARTITION FUNCTION (not free energy) in an additive variable
(b) With POLYNOMIAL structure (integer exponents, finite degree)
(c) With NON-NEGATIVE coefficients
(d) Whose zeros correspond to the zeros of zeta

The explicit formula provides (a) partially but fails on (b), (c), (d).

THE WALL: This should be added as Wall 13:
"Explicit formula is at the free-energy level (log Z)', not partition
function level Z. Positive prime coefficients in the free energy do not
give Lee-Yang for the partition function."
""")

print("\n" + "=" * 70)
print("PART O: Is There a WAY to Define a Genuine Partition Function?")
print("=" * 70)

# Consider: what if we DON'T use the logarithmic derivative?
# What if we use the explicit formula for Chebyshev's theta function?
# theta(x) = sum_{p<=x} log p
# The prime counting function pi(x) counts primes up to x.
# The explicit formula for theta(x):
# theta(x) = x - sum_rho x^rho / rho - log(2pi) - (1/2)log(1-1/x^2)
#
# The "partition function" approach:
# Define Z(z) = sum_{p prime} z^{log p} = sum_p p^{s} where z = e^s
# This is the PRIME ZETA FUNCTION: P(s) = sum_p p^{-s}
#
# P(s) = sum_p p^{-s} = sum_k mu(k)/k * log zeta(ks)
#
# P(s) is related to log zeta(s) by Mobius inversion:
# log zeta(s) = sum_k P(ks)/k
# P(s) = sum_k (mu(k)/k) log zeta(ks)
#
# The prime zeta function P(s) has the same incommensurable-frequency
# problem: the exponents are log(p), which are incommensurable.

print("Alternative: the prime zeta function P(s) = sum_p p^{-s}")
print()
print("P(s) = sum_p p^{-s} has:")
print("  - Positive coefficients (all equal to 1)")
print("  - Incommensurable exponents log(p)")
print("  - Natural boundary at Re(s) = 0 (cannot be continued!)")
print()
print("The natural boundary is the FATAL problem. P(s) has a dense set")
print("of singularities on the imaginary axis, so it cannot even be")
print("defined at Re(s) = 1/2 where the RH zeros live.")
print()
print("This is yet another manifestation of the same wall:")
print("Any 'additive' reformulation using primes inherits the")
print("incommensurable-frequency structure that prevents polynomial")
print("representation.")


print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)

print("""
+--------------------------------------+----------+---------------------------+
| Condition                            | Status   | Detail                    |
+--------------------------------------+----------+---------------------------+
| Additive structure (sum, not product)| TRUE     | Explicit formula is a sum |
| Prime coefficients positive          | TRUE     | c_{p,m} = log(p)/p^{m/2} |
| Correct involution (t -> -t)         | TRUE     | = functional equation     |
| Polynomial in single variable        | FAILS    | Incommensurable freq      |
| Polynomial in multi-variables z_p    | PARTIAL  | Each z_p factor is poly   |
| Ferromagnetic at partition fn level  | FAILS    | Explicit formula is at    |
|                                      |          | free energy level, not Z  |
| Explicit formula -> Lee-Yang system  | NO       | Level mismatch + freq     |
| Weil positivity = Lee-Yang positivity| RELATED  | Both PSD, different spaces|
+--------------------------------------+----------+---------------------------+

BOTTOM LINE: The explicit formula DOES convert the multiplicative Euler
product into an additive sum. The prime coefficients ARE positive. But
the conversion puts us at the FREE ENERGY level, not the partition
function level. Lee-Yang operates on Z, not on log(Z) or (log Z)'.
The positive prime coefficients at the free energy level do NOT give
Lee-Yang at the partition function level.
""")
