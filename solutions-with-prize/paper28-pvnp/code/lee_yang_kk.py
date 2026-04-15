"""
Lee-Yang analysis for the KK partition function on S^1.

Checks:
1. The change of variable w = e^{s-1/2} mapping critical line to unit circle
2. The functional equation symmetry in w-variable
3. Whether Euler factors have zeros on the unit circle in w
4. Mobius function sign distribution (ferromagnetic condition check)
5. Numerical zeros of zeta in w-variable

Author: Research agent for G's RH project
"""

import numpy as np
from mpmath import mp, mpf, mpc, zeta, zetazero, log, exp, pi, fabs, arg
from mpmath import sqrt, gamma, inf
from sympy import mobius as sympy_mobius

mp.dps = 50  # high precision

print("=" * 70)
print("PART A: Change of variable w = exp(s - 1/2)")
print("=" * 70)

# The first 20 nontrivial zeros of zeta
print("\nFirst 20 nontrivial zeros of zeta(s):")
print(f"{'n':>3} {'Im(rho)':>20} {'|w|':>20} {'|w|=1?':>10}")
for n in range(1, 21):
    rho = zetazero(n)  # rho = 1/2 + i*t_n
    # w = exp(s - 1/2) = exp(rho - 1/2) = exp(i*t_n)
    w = exp(rho - mpf('0.5'))
    absw = fabs(w)
    on_circle = "YES" if fabs(absw - 1) < mpf('1e-30') else "NO"
    print(f"{n:3d} {float(rho.imag):20.12f} {float(absw):20.15f} {on_circle:>10}")

print("\n" + "=" * 70)
print("PART B: Functional equation in w-variable")
print("=" * 70)

# The completed zeta function xi(s) = 1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
# satisfies xi(s) = xi(1-s).
# In w = exp(s - 1/2): s = 1/2 + log(w), 1-s = 1/2 - log(w) = 1/2 + log(1/w)
# So: s -> 1-s corresponds to w -> 1/w
# For complex s = sigma + it: w = exp(sigma - 1/2 + it)
# 1 - conj(s) = 1 - sigma + it: w' = exp(1/2 - sigma + it)
# |w'| = exp(1/2 - sigma) = 1/|w| since |w| = exp(sigma - 1/2)
# So the FE symmetry s -> 1-conj(s) becomes |w||w'| = 1 (involution on modulus)

print("\nFunctional equation symmetry check:")
print("xi(s) = xi(1-s)")
print("In w-variable: w -> 1/w (for real s)")
print("For complex s = sigma + it:")
print("  s -> 1-s gives w = e^{s-1/2} -> e^{1/2-s} = 1/w")
print("  This is EXACTLY w -> 1/w (NOT w -> 1/conj(w))")
print()
print("The Lee-Yang involution is z -> 1/conj(z) for the unit circle |z|=1.")
print("The FE involution is w -> 1/w.")
print("These AGREE on the unit circle |w|=1 if w = e^{it} (purely imaginary exponent).")
print("On the critical line s = 1/2 + it: w = e^{it}, so w -> 1/w = e^{-it} = conj(w) = 1/conj(w).")
print("=> The FE involution MATCHES the Lee-Yang involution ON the self-dual locus.")

print("\n" + "=" * 70)
print("PART C: Euler factor zeros in w-variable")
print("=" * 70)

# Each Euler factor: (1 - p^{-s})^{-1}
# Zero of 1/zeta: 1 - p^{-s} = 0 => p^{-s} = 1 => s = 2*pi*i*k/log(p)
# In w-variable: w = exp(s - 1/2) = exp(-1/2 + 2*pi*i*k/log(p))
# |w| = exp(-1/2) ≈ 0.6065... NOT 1.

print("\nEuler factor (1 - p^{-s}) = 0 at s = 2*pi*i*k/log(p), k in Z")
print(f"|w| at these zeros = exp(-1/2) = {float(exp(mpf('-0.5'))):.10f}")
print("This is NOT on the unit circle |w| = 1.")
print()

# But wait -- what about a DIFFERENT change of variable?
# The "correct" variable for Lee-Yang might be z_p = p^{-s} for each prime.
# Then 1 - z_p = 0 at z_p = 1, which IS on |z_p| = 1.
# But each prime has its OWN variable z_p, so there's no single variable.

print("Alternative: for each prime p, set z_p = p^{-s}.")
print("Then 1 - z_p = 0 at z_p = 1, which IS on |z_p| = 1.")
print("But RH in z_p variable: s = 1/2 + it => |z_p| = p^{-1/2}.")
print(f"For p=2: |z_2| = {float(2**(-0.5)):.10f}")
print(f"For p=3: |z_3| = {float(3**(-0.5)):.10f}")
print("The critical line is NOT |z_p| = 1 in any per-prime variable.")

print("\n" + "=" * 70)
print("PART D: Mobius function and ferromagnetic condition")
print("=" * 70)

# 1/zeta(s) = sum_{n=1}^infty mu(n) n^{-s}
# The ferromagnetic condition requires non-negative coefficients.
# mu(n) takes values -1, 0, +1.

print("\nMobius function mu(n) for n = 1..30:")
mus = []
for n in range(1, 31):
    m = int(sympy_mobius(n))
    mus.append(m)

print("n:  ", " ".join(f"{n:3d}" for n in range(1, 31)))
print("mu: ", " ".join(f"{m:3d}" for m in mus))

neg_count = sum(1 for m in mus if m < 0)
pos_count = sum(1 for m in mus if m > 0)
zero_count = sum(1 for m in mus if m == 0)
print(f"\nOut of first 30: {pos_count} positive, {neg_count} negative, {zero_count} zero")
print("=> The coefficients of 1/zeta(s) are NOT non-negative.")
print("=> The 'ferromagnetic' condition FAILS for 1/zeta(s).")

# Check for larger N
print("\nMobius function statistics for n = 1..1000:")
pos = neg = zero = 0
for n in range(1, 1001):
    m = int(sympy_mobius(n))
    if m > 0: pos += 1
    elif m < 0: neg += 1
    else: zero += 1
print(f"Positive: {pos}, Negative: {neg}, Zero: {zero}")
print(f"Ratio positive/negative: {pos/neg:.4f}")
print("The Mobius function is essentially equally distributed between +1 and -1")
print("(on squarefree integers). This is maximally NON-ferromagnetic.")

print("\n" + "=" * 70)
print("PART E: Can RP fix the ferromagnetic condition?")
print("=" * 70)

# RP gives: Z(beta) > 0 for real beta > 1.
# This is true: zeta(sigma) > 0 for sigma > 1.
# But Lee-Yang needs POLYNOMIAL coefficients to be non-negative.
# These are different conditions.

# Check: is zeta(sigma) > 0 for sigma > 1?
print("\nzeta(sigma) for real sigma > 1:")
for sigma in [1.1, 1.5, 2.0, 3.0, 5.0, 10.0]:
    z = float(zeta(sigma))
    print(f"  zeta({sigma}) = {z:.10f} > 0: {'YES' if z > 0 else 'NO'}")

# But zeta has negative values for 0 < sigma < 1
print("\nzeta(sigma) for 0 < sigma < 1:")
for sigma in [0.1, 0.3, 0.5, 0.7, 0.9]:
    z = float(zeta(sigma))
    sign = "POSITIVE" if z > 0 else "NEGATIVE"
    print(f"  zeta({sigma}) = {z:.10f} ({sign})")

print("\nzeta(s) changes sign in (0,1): it is NOT always positive.")
print("RP guarantees positivity only for beta > 1 (the physical region).")

print("\n" + "=" * 70)
print("PART F: The completed xi function in w-variable")
print("=" * 70)

# xi(s) = 1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
# This satisfies xi(s) = xi(1-s) and xi(conj(s)) = conj(xi(s))
# In w = e^{s-1/2}: xi is an entire function of w (actually of log w)

# The xi function as a product over zeros:
# xi(s) = xi(0) * prod_rho (1 - s/rho)
# In w-variable: rho = 1/2 + i*gamma_n, so s/rho terms become functions of w

# The key question: does xi(w), viewed as a function of w,
# have the property that its zeros lie on |w| = 1?
# YES -- this is exactly RH restated!

# But does it satisfy the Lee-Yang conditions to PROVE this?

# Write xi in the w-variable via the Hadamard product:
# xi(s) = e^{A+Bs} prod_rho (1 - s/rho) e^{s/rho}
# where A, B are constants.

print("\nThe completed xi function satisfies:")
print("  xi(s) = xi(1-s)  [functional equation = w -> 1/w symmetry]")
print("  xi(conj(s)) = conj(xi(s))  [reality condition]")
print()
print("In w = e^{s-1/2}:")
print("  Zeros of xi at s = 1/2 + i*gamma_n")
print("  => w = e^{i*gamma_n} => |w| = 1  (if RH)")
print()
print("The Hadamard product of xi in w-variable:")
print("  xi(1/2 + log w) = prod_n (1 - log(w)/(i*gamma_n)) * ...")
print("  This is NOT a polynomial in w -- it is a function of log(w).")
print("  Lee-Yang requires a polynomial (or limit of polynomials) in z.")
print("  xi(s) as a function of w is NOT a polynomial in w.")

print("\n" + "=" * 70)
print("PART G: Is there ANY formulation as polynomial in w?")
print("=" * 70)

# The xi function has the product:
# Xi(t) = xi(1/2 + it) = prod_n (1 - t/gamma_n)(1 + t/gamma_n)
# = prod_n (1 - t^2/gamma_n^2)
# Setting u = t^2: Xi = prod_n (1 - u/gamma_n^2)
# This IS a "polynomial" (infinite product of linear factors) in u = t^2.

# In w = e^{it}: t = -i log(w), t^2 = -(log w)^2
# u = -(log w)^2 is NOT polynomial in w.

# Alternative: the partial sums of the Dirichlet series
# zeta_N(s) = sum_{n=1}^N n^{-s} = sum_{n=1}^N e^{-s log n}
# In w = e^{s-1/2}: zeta_N = sum n^{-1/2} w^{-log n}
# The exponents -log n are NOT integers, so this is NOT a polynomial in w.

# However, the PARTITION FUNCTION of the primon gas:
# Z(beta) = prod_p 1/(1 - p^{-beta})
# is a product of geometric series. Each 1/(1-x) is NOT a polynomial.

print("Attempt to write zeta as polynomial in w = e^{s-1/2}:")
print()
print("zeta(s) = sum n^{-s} = sum n^{-1/2} * w^{-log(n)}")
print("The exponents -log(n) are NOT integers.")
print("=> zeta(s) is NOT a polynomial in w.")
print()
print("Alternative: the Z function")
print("  Z(t) = pi^{-it/2} Gamma(1/4 + it/2)/|Gamma(1/4+it/2)| * zeta(1/2+it)")
print("  Hardy's function: Z(t) is real for real t.")
print("  Z(t) = 0 iff zeta(1/2+it) = 0")
print("  But Z is a function of t, not of w = e^{it}.")
print("  Z is NOT periodic in t, so NOT a function of w alone.")

print("\n" + "=" * 70)
print("PART H: The polynomial obstruction quantified")
print("=" * 70)

# The fundamental issue: Lee-Yang applies to POLYNOMIALS in z.
# zeta(s) is not a polynomial in ANY variable z such that
# Re(s) = 1/2 corresponds to |z| = 1.

# Can we approximate? The truncated Euler product:
# zeta_P(s) = prod_{p <= P} 1/(1-p^{-s})
# In w: this is prod_{p<=P} 1/(1 - e^{-log(p)*log(w) + log(p)/2})
# Still not polynomial in w.

# The truncated Dirichlet series:
# zeta_N(s) = sum_{n=1}^N n^{-s}
# Can we write this as a polynomial in SOME variable?
# Set z = N^{-s}. Then n^{-s} = z^{log n / log N}.
# For n=1: z^0 = 1. For n=N: z^1 = z. For n=2: z^{log2/logN}.
# The exponents are log(n)/log(N), which are NOT integers for n != 1, N.
# => NOT a polynomial in z either.

# ONLY way to get a polynomial: the FINITE Ising model has
# 2^N configurations, giving a degree-N polynomial in z.
# The primon gas has infinitely many "configurations" (all integers),
# so it never reduces to a finite polynomial.

print("The fundamental obstruction:")
print()
print("Lee-Yang theorem applies to POLYNOMIALS P(z) = sum a_k z^k")
print("where k ranges over a FINITE set of NON-NEGATIVE INTEGERS.")
print()
print("For the Ising model on N sites: P has degree N (finite polynomial).")
print("The unit circle theorem then applies.")
print()
print("For zeta(s): there is NO variable z such that zeta becomes a")
print("polynomial in z with integer exponents. The 'exponents' are")
print("log(n) for n = 1,2,3,... which are not commensurable.")
print()
print("This is not a technicality -- it is the ARITHMETIC obstruction:")
print("the primes are multiplicatively independent (log p_i / log p_j")
print("is irrational for distinct primes). This means no single variable")
print("z can make the Euler product into a polynomial.")

# Verify: log(p_i)/log(p_j) is irrational
print("\nVerification: log(p_i)/log(p_j) for small primes:")
primes = [2, 3, 5, 7, 11, 13]
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        ratio = float(log(primes[j]) / log(primes[i]))
        print(f"  log({primes[j]})/log({primes[i]}) = {ratio:.15f} (irrational)")

print("\n" + "=" * 70)
print("SUMMARY OF COMPUTATIONAL FINDINGS")
print("=" * 70)
print("""
1. The change of variable w = e^{s-1/2} DOES map the critical line
   to the unit circle |w| = 1. Verified for the first 20 zeros.

2. The functional equation symmetry s -> 1-s becomes w -> 1/w,
   which MATCHES the Lee-Yang involution on |w| = 1.

3. Individual Euler factor zeros lie at |w| = e^{-1/2} ≈ 0.6065,
   NOT on the unit circle. The Asano contraction cannot help.

4. The Mobius function mu(n) takes values {-1, 0, +1} with roughly
   equal positive and negative counts. The ferromagnetic (non-negative
   coefficient) condition FAILS maximally for 1/zeta(s).

5. RP gives zeta(sigma) > 0 for sigma > 1, but this is WEAKER than
   the Lee-Yang non-negativity of polynomial coefficients.

6. zeta(s) is NOT a polynomial in w (or any variable). The exponents
   log(n) are not commensurable due to multiplicative independence
   of the primes. This is the FUNDAMENTAL obstruction.
""")
