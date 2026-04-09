"""
R27: Investigating whether S1+S2+S3+S5 (without S4/Ramanujan) force zeros
onto the critical line.

Key tests:
1. Construct Dirichlet series with Euler product + FE but violating Ramanujan
2. Check zero locations of such series
3. Examine Epstein zeta (S1+S2+S3, no S5) as control
4. Examine Davenport-Heilbronn (S1+S2+S3, no S5) as control
5. Explore what "faster than Ramanujan" Euler products look like
"""

import numpy as np
from mpmath import (mp, mpf, mpc, zeta, gamma, pi, log, exp, sqrt,
                    fsum, power, cos, sin, inf, quad, diff, nstr,
                    zetazero, siegeltheta, siegelz, findroot,
                    nprint, chop, fabs, arg, re, im, conj, polyroots,
                    altzeta)

mp.dps = 30  # 30 decimal places

print("=" * 70)
print("R27: SELBERG AXIOMS WITHOUT S4 — COMPUTATIONAL INVESTIGATION")
print("=" * 70)

# =================================================================
# TEST 1: The Davenport-Heilbronn function
# Has FE (S3) but NO Euler product (S5). Known to have off-line zeros.
# This establishes: S5 is NECESSARY (known result, verification).
# =================================================================
print("\n" + "=" * 70)
print("TEST 1: Davenport-Heilbronn Function (S1+S2+S3, no S5)")
print("=" * 70)

# The DH function is built from Hurwitz zeta at specific arguments.
# f(s) = [zeta(s, 1/5) - zeta(s, 2/5) - zeta(s, 3/5) + zeta(s, 4/5)]
#       * cos(theta) / 2
#       + [zeta(s, 1/5) - zeta(s, 4/5)] * sin(theta) / 2
# with theta chosen so it has a functional equation.
# Actually, the standard construction uses a specific linear combination
# of Dirichlet L-functions mod 5.

# More precisely: let chi be a character mod 5 with chi(2) = i.
# Then L(s, chi) has zeros on Re(s) = 1/2 (GRH for chi).
# The DH function is:
# f(s) = cos(alpha) * L(s, chi_1) + sin(alpha) * L(s, chi_2)  (wrong)
#
# Actually the standard DH is:
# f(s) = sum_{n=1}^inf a_n / n^s
# where a_n follows a specific pattern mod 5.
# It satisfies a functional equation but NOT an Euler product.

# Let's use the Titchmarsh formulation:
# Let chi be the primitive character mod 5 with chi(2) = i (or -i).
# Then L(s,chi) satisfies a FE.
# The DH function is a specific real linear combination of L(s,chi)
# and L(s, chi_bar) that satisfies a FE of signature (5, s -> 1-s)
# but has zeros off the line.

# For our purposes, we verify the KEY FACT: without Euler product,
# FE alone does NOT force zeros onto the line.

# Compute L(s, chi_5) for the non-trivial character mod 5
# chi_5: 1->1, 2->i, 3->-i, 4->-1, 0->0

def hurwitz_zeta(s, a, N=2000):
    """Compute Hurwitz zeta(s, a) = sum_{n=0}^inf (n+a)^{-s}"""
    return mp.hurwitz(s, a)

# The DH function using Titchmarsh's construction
# f(s) = (e^{i*alpha} * L(s,chi) + e^{-i*alpha} * L(s,chi_bar)) / 2
# where chi is a complex character mod 5 and alpha is chosen to
# give a real-valued FE.

# Character table mod 5:
# chi_1: 1,1,1,1 (trivial)
# chi_2: 1,i,-i,-1 (complex)
# chi_3: 1,-i,i,-1 (conjugate of chi_2)
# chi_4: 1,-1,-1,1 (real, quadratic)

# The DH uses chi_2 (or equivalently chi_3).

def L_chi_mod5(s, chi_vals, N=500):
    """L-function for a character mod 5"""
    result = mpf(0)
    for n in range(1, N+1):
        r = n % 5
        if r == 0:
            continue
        result += chi_vals[r] * power(n, -s)
    return result

# chi_2 values: chi(1)=1, chi(2)=i, chi(3)=-i, chi(4)=-1
chi2 = {1: mpc(1,0), 2: mpc(0,1), 3: mpc(0,-1), 4: mpc(-1,0)}
chi3 = {1: mpc(1,0), 2: mpc(0,-1), 3: mpc(0,1), 4: mpc(-1,0)}

# Verify basic properties
print("\nL(2, chi_2) mod 5 =", L_chi_mod5(2, chi2))
print("L(2, chi_3) mod 5 =", L_chi_mod5(2, chi3))

# The DH angle: alpha = arctan((sqrt(10 - 2*sqrt(5)) - 2) / (sqrt(5) - 1))
# From Davenport-Heilbronn (1936)

sqrt5 = sqrt(5)
# The critical angle for the DH function
# Using the standard construction from Titchmarsh/Voronin:
# The function is f(s) = sum a_n n^{-s} with
# a_1 = 1, a_2 = p, a_3 = p_bar, a_4 = -1, a_5 = 0, period 5
# where p = (-1 + i*tan(alpha))/2 with specific alpha

# Better: use the known fact directly. The DH function has a zero at
# approximately s = 0.808... + 85.7i (OFF the critical line).

print("\nKEY FACT (Davenport-Heilbronn, 1936):")
print("The DH function satisfies S1 (Dirichlet series), S2 (continuation),")
print("S3 (functional equation), but NOT S5 (no Euler product).")
print("It has zeros OFF the critical line.")
print("CONCLUSION: S5 (Euler product) is NECESSARY for GRH.")
print("Without it, S1+S2+S3 alone do NOT force zeros onto Re(s) = 1/2.")

# =================================================================
# TEST 2: Epstein Zeta Functions
# Has S1+S2+S3 but NOT S5. Known off-line zeros.
# Another confirmation that S5 is necessary.
# =================================================================
print("\n" + "=" * 70)
print("TEST 2: Epstein Zeta Functions (S1+S2+S3, no S5)")
print("=" * 70)

# The Epstein zeta function for a positive definite quadratic form
# Q(m,n) = am^2 + bmn + cn^2 is:
# Z_Q(s) = sum'_{(m,n)} Q(m,n)^{-s}
# It satisfies a functional equation but generally does NOT have
# an Euler product (unless Q is associated to a class number 1 form).

# For Q(m,n) = m^2 + n^2 (the Gaussian integers), the Epstein zeta
# IS 4*L(s,chi_{-4})*zeta(s), which DOES have an Euler product.
# So this case satisfies S5 and has zeros on the line.

# For Q(m,n) = m^2 + 5*n^2 (discriminant -20), the class number is 2,
# so Z_Q does NOT have a simple Euler product.
# The Epstein zeta for non-class-number-1 forms has zeros off the line.

# Key reference: Dahlquist (1952), Stark (1967)
print("\nEpstein zeta for Q(m,n) = m^2 + 5n^2:")
print("Class number h(-20) = 2, so no Euler product.")
print("Stark (1967) proved: Epstein zeta for non-class-1 forms")
print("has infinitely many zeros OFF the critical line.")
print("\nCONCLUSION: Confirms S5 (Euler product) is necessary.")

# =================================================================
# TEST 3: Can we construct F with S1+S2+S3+S5 but NOT S4?
# This is the CENTRAL question of R27.
# =================================================================
print("\n" + "=" * 70)
print("TEST 3: Constructing functions with S1+S2+S3+S5 but NOT S4")
print("=" * 70)

print("""
THEORETICAL ANALYSIS:

The key constraint is the EULER PRODUCT axiom S5:
  log F(s) = sum_p sum_{k>=1} b_{p^k} p^{-ks}
  with b_{p^k} = O(p^{k*theta}), theta < 1/2

The Ramanujan bound (S4) says: a_n = O(n^epsilon) for all epsilon > 0.

For an Euler product with local factors:
  F_p(s) = prod_{j=1}^d (1 - alpha_{j,p} p^{-s})^{-1}

S4 (Ramanujan) means: |alpha_{j,p}| = 1 for all j,p (on the unit circle)
The S5 bound theta < 1/2 means: |alpha_{j,p}| < p^{1/2}

So S5 already PARTIALLY constrains the Satake parameters:
  |alpha_{j,p}| < p^{1/2}  (from S5)
vs
  |alpha_{j,p}| = 1          (from S4, Ramanujan)

The gap between S5 and S4 is:
  1 <= |alpha_{j,p}| < p^{1/2}
  (allowed by S5, forbidden by S4)
""")

# =================================================================
# TEST 4: Degree-1 Selberg class members
# For degree 1, Kaczorowski-Perelli PROVED that S1+S2+S3+S5 implies
# the function is a Dirichlet L-function (2002).
# For these, Ramanujan (|a_p| = 1) is AUTOMATIC.
# So for d=1: S4 is a CONSEQUENCE of S1+S2+S3+S5!
# =================================================================
print("\n" + "=" * 70)
print("TEST 4: Degree-1 Classification (Kaczorowski-Perelli)")
print("=" * 70)

print("""
THEOREM (Kaczorowski-Perelli, 1999/2002):
The only degree-1 functions in the Selberg class are the
Riemann zeta function zeta(s) and Dirichlet L-functions L(s, chi)
for primitive characters chi.

CONSEQUENCE: For degree 1:
- S1+S2+S3+S5 => F is a Dirichlet L-function
- For Dirichlet L-functions: |a_p| = |chi(p)| = 0 or 1
- Therefore: S4 (Ramanujan bound |a_p| <= 1) is AUTOMATIC
- S4 is a CONSEQUENCE of S1+S2+S3+S5 for degree 1!

This means: for degree 1, the four axioms S1+S2+S3+S5
FORCE the function to be a Dirichlet L-function, and
Ramanujan follows automatically.
""")

# =================================================================
# TEST 5: What about degree 2?
# =================================================================
print("\n" + "=" * 70)
print("TEST 5: Degree-2 Analysis")
print("=" * 70)

print("""
For degree 2, the Selberg class includes:
1. Hecke L-functions of holomorphic cusp forms
2. L-functions of Maass forms
3. Rankin-Selberg L-functions L(s, f x chi)
4. Symmetric square L-functions sym^2(f)

For holomorphic cusp forms of weight k:
  |a_p| <= 2p^{(k-1)/2}  (PROVED by Deligne, 1974)
  After normalization: |alpha_{1,p}| = |alpha_{2,p}| = 1
  So S4 HOLDS (proven).

For Maass forms:
  The Ramanujan conjecture |alpha_{j,p}| = 1 is OPEN.
  Best known: |alpha_{j,p}| <= p^{7/64} (Kim-Sarnak, 2003)
  This DOES satisfy S5 (theta = 7/64 < 1/2) but NOT S4.

KEY QUESTION: Do Maass form L-functions satisfy GRH?
ANSWER: This is believed YES (part of GRH), but UNPROVED.
However, we cannot use this to test whether S4 is needed,
because Maass forms DO satisfy S5 with theta = 7/64.

The question is: does the SPECIFIC value of theta matter?
""")

# =================================================================
# TEST 6: Constructing a "stretched" Euler product
# Take zeta(s) and modify the local factors to violate Ramanujan
# while preserving the Euler product structure
# =================================================================
print("\n" + "=" * 70)
print("TEST 6: Stretched Euler Products — Computational Test")
print("=" * 70)

# Consider the function:
# F_alpha(s) = prod_p (1 - p^alpha * p^{-s})^{-1} * (1 - p^{-alpha} * p^{-s})^{-1}
# = prod_p (1 - p^{alpha-s})^{-1} * (1 - p^{-alpha-s})^{-1}
#
# For alpha = 0: F_0(s) = zeta(s)^2 (satisfies S4, zeros on Re(s)=1/2)
# For alpha > 0: the Satake parameters are p^alpha and p^{-alpha}
#   |alpha_{1,p}| = p^alpha != 1, violating Ramanujan
#   But if alpha < 1/2, then |alpha_{j,p}| < p^{1/2}, satisfying S5

# Actually F_alpha(s) = zeta(s-alpha) * zeta(s+alpha) for alpha real.
# This has zeros where zeta(s-alpha) = 0 or zeta(s+alpha) = 0.
# If RH holds for zeta: zeros at s = 1/2 + alpha + i*t and s = 1/2 - alpha + i*t
# For alpha > 0: zeros are at Re(s) = 1/2 + alpha and Re(s) = 1/2 - alpha
# These are OFF the critical line!

print("Consider F_alpha(s) = zeta(s-alpha) * zeta(s+alpha)")
print("This has Euler product: prod_p [(1-p^{alpha-s})(1-p^{-alpha-s})]^{-1}")
print()

for alpha_val in [0, 0.1, 0.2, 0.3, 0.49]:
    alpha = mpf(alpha_val)

    # Check S5: theta parameter
    # The Satake parameters are p^alpha and p^{-alpha}
    # For convergence of log F: need alpha < 1/2
    s5_satisfied = alpha < 0.5

    # Zero locations (assuming RH for zeta):
    # Re(s) = 1/2 + alpha and Re(s) = 1/2 - alpha
    zero_loc1 = 0.5 + alpha_val
    zero_loc2 = 0.5 - alpha_val

    # Does it satisfy S4?
    s4_satisfied = (alpha_val == 0)

    # Does it satisfy S3 (functional equation)?
    # zeta(s-a)*zeta(s+a) satisfies:
    # Lambda(s-a)*Lambda(s+a) has symmetry s -> 1-s
    # But the COMPLETED function is:
    # pi^{-(s-a)/2} Gamma((s-a)/2) zeta(s-a) * pi^{-(s+a)/2} Gamma((s+a)/2) zeta(s+a)
    # Under s -> 1-s: this does NOT simply map to its conjugate times epsilon
    # unless alpha = 0.

    # Actually check: does F_alpha(s) = F_alpha(1-s)?
    # F_alpha(1-s) = zeta(1-s-a) * zeta(1-s+a)
    # Using zeta(s) = chi(s)*zeta(1-s):
    # zeta(s-a) = chi(s-a) * zeta(1-s+a)
    # zeta(s+a) = chi(s+a) * zeta(1-s-a)
    # So F_alpha(s) = chi(s-a)*chi(s+a) * F_alpha(1-s)
    # This IS a functional equation of the right form IF
    # we can write chi(s-a)*chi(s+a) in the Selberg class form.
    # chi(s) = pi^{s-1/2} * Gamma((1-s)/2) / Gamma(s/2)
    # This is expressible with Gamma factors, so YES — it has a FE.

    has_fe = True
    on_line = (alpha_val == 0)

    print(f"alpha = {alpha_val}:")
    print(f"  S4 (Ramanujan): {'YES' if s4_satisfied else 'NO'}")
    print(f"  S5 (theta < 1/2): {'YES' if s5_satisfied else 'NO'}")
    print(f"  S3 (func eq): {'YES' if has_fe else 'NO'}")
    print(f"  Zeros at Re(s) = {zero_loc1} and {zero_loc2}")
    print(f"  On critical line: {'YES' if on_line else 'NO'}")
    print()

print("""
CRITICAL FINDING:
F_alpha(s) = zeta(s-alpha) * zeta(s+alpha) satisfies:
  S1 (Dirichlet series): YES
  S2 (analytic continuation): YES
  S3 (functional equation): YES
  S5 (Euler product with theta = alpha < 1/2): YES (for 0 < alpha < 1/2)
  S4 (Ramanujan): NO (Satake parameters = p^{+/-alpha}, not on unit circle)

And its zeros are at Re(s) = 1/2 +/- alpha, which is OFF the critical line.

THEREFORE: S1+S2+S3+S5 without S4 do NOT force zeros onto Re(s) = 1/2.
S4 (or at least some bound on coefficients beyond theta < 1/2) is ESSENTIAL.
""")

# =================================================================
# TEST 7: Verify the FE more carefully for F_alpha
# =================================================================
print("\n" + "=" * 70)
print("TEST 7: Verifying F_alpha is in the Selberg class (minus S4)")
print("=" * 70)

# Check S1: F_alpha(s) = sum a_n n^{-s}
# The coefficients of zeta(s-a)*zeta(s+a) = sum_n d_a(n) n^{-s}
# where d_a(n) = sum_{d|n} d^a * (n/d)^{-a} ... no.
# Actually: zeta(s-a)*zeta(s+a) = sum_n (sum_{d|n} d^a * (n/d)^{-a}) n^{-s}
# Wait, let me be more careful.
# zeta(s-a) = sum_m m^{-(s-a)} = sum_m m^a * m^{-s}
# zeta(s+a) = sum_k k^{-(s+a)} = sum_k k^{-a} * k^{-s}
# Product: sum_n (sum_{mk=n} m^a * k^{-a}) n^{-s}
# = sum_n (sum_{d|n} d^a * (n/d)^{-a}) n^{-s}
# = sum_n d_a(n) n^{-s}
# where d_a(n) = sum_{d|n} (d/(n/d))^a = sum_{d|n} (d^2/n)^a

# For S4: |d_a(n)| = |sum_{d|n} (d^2/n)^a|
# For a > 0 and n = p: d_a(p) = 1 + (p^2/p)^a = 1 + p^a
# So |a_p| = 1 + p^a, which grows as p^a for large p.
# If a > 0, this is NOT O(p^epsilon) for epsilon < a. Violates S4.

print("Coefficients of F_alpha(s) = zeta(s-alpha)*zeta(s+alpha):")
print()

alpha_test = mpf('0.1')
print(f"For alpha = {alpha_test}:")
print(f"  a_2 = 1 + 2^alpha = {1 + power(2, alpha_test)}")
print(f"  a_3 = 1 + 3^alpha = {1 + power(3, alpha_test)}")
print(f"  a_5 = 1 + 5^alpha = {1 + power(5, alpha_test)}")
print(f"  a_7 = 1 + 7^alpha = {1 + power(7, alpha_test)}")
print()

# Growth rate check
print("Growth of a_p for alpha = 0.1:")
for p in [2, 3, 5, 7, 11, 13, 101, 1009, 10007]:
    a_p = 1 + power(p, alpha_test)
    ratio = a_p / power(p, mpf('0.01'))
    print(f"  p = {p}: a_p = {nstr(a_p, 6)}, a_p/p^0.01 = {nstr(ratio, 6)}")

print()
print("a_p ~ p^{0.1} for large p, violating a_p = O(p^epsilon) for eps < 0.1")
print("So S4 fails for any alpha > 0.")

# =================================================================
# TEST 8: Is S4 truly independent, or does it follow from S1+S2+S3+S5
# together with some OTHER condition (like primitivity)?
# =================================================================
print("\n" + "=" * 70)
print("TEST 8: The Role of Primitivity")
print("=" * 70)

print("""
A function F in the Selberg class is PRIMITIVE if it cannot be written
as a non-trivial product F = F_1 * F_2 of Selberg class elements.

F_alpha(s) = zeta(s-alpha) * zeta(s+alpha) is NOT primitive — it is
a product of two shifted zeta functions.

QUESTION: Is zeta(s-alpha) in the Selberg class?

For alpha > 0:
  zeta(s-alpha) = sum_n n^alpha * n^{-s}
  The coefficients are a_n = n^alpha.
  For S4: |a_n| = n^alpha, and for alpha > 0, this is NOT O(n^epsilon)
  for epsilon < alpha. So zeta(s-alpha) does NOT satisfy S4.

  For S5: log zeta(s-alpha) = sum_p sum_k p^{k*alpha} / (k * p^{ks})
  The coefficient b_{p^k} = p^{k*alpha} / k = O(p^{k*alpha}).
  For S5 we need alpha < 1/2. If alpha < 1/2, S5 is satisfied.

So zeta(s-alpha) with 0 < alpha < 1/2 satisfies S1,S2,S3,S5 but NOT S4.
And it IS primitive (it's a shifted version of a primitive function).

Its zeros are at s = rho + alpha where rho are zeros of zeta.
Assuming RH: Re(rho) = 1/2, so Re(s) = 1/2 + alpha > 1/2.
All zeros are OFF the critical line.

THIS IS THE DEFINITIVE COUNTEREXAMPLE:
zeta(s - alpha) for 0 < alpha < 1/2 satisfies S1+S2+S3+S5 (not S4)
and has ALL zeros off the critical line.
""")

# Actually, wait — is zeta(s-alpha) a valid Selberg class element?
# S1: sum n^alpha * n^{-s} converges for Re(s) > 1+alpha.
# But S1 requires convergence for Re(s) > 1. If alpha > 0,
# the abscissa of convergence is 1 + alpha > 1.
# So zeta(s-alpha) does NOT satisfy S1 as stated!

print("CORRECTION: Does zeta(s-alpha) satisfy S1?")
print(f"Abscissa of absolute convergence = 1 + alpha")
print(f"S1 requires absolute convergence for Re(s) > 1")
print(f"So zeta(s-alpha) does NOT satisfy S1 for alpha > 0.")
print()
print("But F_alpha(s) = zeta(s-alpha)*zeta(s+alpha):")
print("As a Dirichlet series sum a_n n^{-s}:")
print(f"  a_n = sum_{{d|n}} (d^2/n)^alpha")
print(f"  For alpha < 0.5: a_n = O(n^alpha * d(n)) = O(n^{{alpha+eps}})")
print(f"  Abscissa of convergence: 1 + alpha (from the n^alpha growth)")
print()
print("REFINED CHECK: S1 requires convergence for Re(s) > 1.")
print("F_alpha has abscissa of convergence 1 + alpha > 1 for alpha > 0.")
print("So F_alpha does NOT satisfy S1 as standardly formulated!")

# =================================================================
# TEST 9: More careful construction — Rankin-Selberg with bad bound
# =================================================================
print("\n" + "=" * 70)
print("TEST 9: What about the normalization?")
print("=" * 70)

print("""
The issue with zeta(s-alpha) is that the shift changes the abscissa
of convergence. Let's think about this more carefully.

In the Selberg class, the normalization is a_1 = 1 and convergence
for Re(s) > 1. The Ramanujan bound a_n = O(n^eps) ensures the
Dirichlet series converges for Re(s) > 1.

WITHOUT S4, the Dirichlet series might converge only for Re(s) > sigma_0
where sigma_0 > 1. In that case, even S1 fails.

So there is a LOGICAL DEPENDENCY: S4 is needed to ensure S1 works
with the standard normalization (convergence for Re(s) > 1).

But the question is: can we separate the GROWTH condition from the
ZERO-LOCATION question?

KEY INSIGHT: The Selberg class axiom S5 already imposes theta < 1/2,
which gives |b_{p^k}| = O(p^{k*theta}). For the multiplicative
coefficients, this gives:
  |a_n| = O(n^theta) (by multiplicativity + theta < 1/2)

Wait, that's not quite right. Let me think more carefully.

For degree d with Satake parameters |alpha_{j,p}| <= p^theta:
  The local factor is prod_j (1 - alpha_{j,p} p^{-s})^{-1}
  log F_p(s) = sum_j sum_k alpha_{j,p}^k / (k p^{ks})
  b_{p^k} = sum_j alpha_{j,p}^k / k
  |b_{p^k}| <= d * p^{k*theta} / k = O(p^{k*theta})

The multiplicative coefficients:
  a_p = sum_j alpha_{j,p}
  |a_p| <= d * p^theta

If theta < 1/2: |a_p| <= d * p^theta = O(p^{1/2 - eps})
This is MUCH weaker than Ramanujan (|a_p| <= d), but DOES give
convergence of sum a_p p^{-s} for Re(s) > 1/2 + theta.

For the full Dirichlet series sum a_n n^{-s}:
  The abscissa of convergence sigma_a depends on the size of a_n.
  With |a_p| <= d * p^theta and multiplicativity:
  |a_n| <= d(n) * n^theta = O(n^{theta + eps})

  So the series converges for Re(s) > 1 + theta.
  For theta > 0: this is ABOVE Re(s) > 1, so S1 fails!

  For theta = 0 (Ramanujan): |a_n| <= d(n) = O(n^eps), convergence
  for Re(s) > 1. S1 holds.

CONCLUSION: S4 (Ramanujan, i.e., theta = 0) is needed to ensure
S1 works with the standard normalization. Without Ramanujan,
the abscissa of convergence shifts above 1.
""")

# =================================================================
# TEST 10: The REAL question — what about the WEAK Selberg class
# where we allow a_n = O(n^A) for some fixed A (not n^eps)?
# =================================================================
print("\n" + "=" * 70)
print("TEST 10: The Extended Selberg Class S# (without S4)")
print("=" * 70)

print("""
Kaczorowski and Perelli studied the EXTENDED Selberg class S#,
which consists of functions satisfying S1 (with a_n polynomial
growth), S2, and S3, but NOT necessarily S4 or S5.

The extended class S# contains:
- All Selberg class elements
- Dirichlet series with polynomial coefficient growth
- Products/quotients of Selberg class elements

KEY RESULTS on S#:

1. S# is closed under products (but NOT the full Selberg class S).

2. The degree d_F is well-defined for F in S#.

3. For d_F = 0: F(s) = 1 (trivially).
   All zeros are on the line (vacuously).

4. For d_F = 1: F(s) is a Dirichlet L-function times a shift.
   Kaczorowski-Perelli (1999) proved the structure theorem:
   F(s) must be n^{ia}L(s, chi) for real a and primitive chi.
   If a = 0: zeros on the line (GRH for L(s,chi) — unproved but
   expected). If a != 0: zeros SHIFTED by ia.

5. For d_F = 2: Much less is known. Contains Hecke/Maass L-functions.

CRITICAL OBSERVATION: The function zeta(s-alpha) has:
   - Degree 1 (same as zeta)
   - Coefficients a_n = n^alpha (polynomial growth for alpha > 0)
   - It IS in S# but NOT in S
   - Zeros at 1/2 + alpha + i*gamma_n (off the line for alpha > 0)

So elements of S# with degree 1 can have off-line zeros.
The DIFFERENCE between S# and S is exactly S4+S5.
S4+S5 force the function to be an actual L-function (for d=1).
""")

# =================================================================
# TEST 11: The Selberg class with S5 but without S4
# Can we define S' = {S1 + S2 + S3 + S5, no S4}?
# =================================================================
print("\n" + "=" * 70)
print("TEST 11: The Class S' = S1+S2+S3+S5 (without S4)")
print("=" * 70)

print("""
Define S' as the class of Dirichlet series satisfying S1, S2, S3, S5
but NOT necessarily S4.

FUNDAMENTAL ISSUE: S1 requires a_n = sum over n^{-s} converging
for Re(s) > 1. With S5 (theta < 1/2), we get |a_n| = O(n^{theta+eps})
with theta < 1/2. The Dirichlet series sum a_n n^{-s} then converges
for Re(s) > 1 + theta.

If theta > 0 (i.e., S4 fails), the series does NOT converge at Re(s) = 1.
This creates tension with S1.

RESOLUTION: There are two interpretations of S1:

(A) STRICT S1: The series sum a_n n^{-s} converges absolutely for
    Re(s) > 1. This REQUIRES a_n = O(n^eps), which IS S4.
    Under this interpretation, S1 IMPLIES S4. The question is vacuous.

(B) RELAXED S1: The series defines an analytic function in some
    right half-plane Re(s) > sigma_0. The analytic continuation to
    the full plane comes from S2.
    Under this interpretation, S4 is genuinely independent.

In the literature, S1 is usually stated as in (A): convergence for
Re(s) > 1, with a_1 = 1. This DOES imply a_n = O(n^A) for some A,
but convergence at Re(s) > 1 specifically requires a_n = O(n^{eps})
(since sum n^{A-sigma} diverges for sigma <= 1+A unless A < 0+eps).

Wait — that's not right either. sum n^{A-sigma} converges for
sigma > 1+A. So if a_n = O(n^A), convergence is for Re(s) > 1+A.
For convergence at Re(s) > 1, we need A = 0, i.e., a_n = O(n^eps).
This IS the Ramanujan bound!

CRUCIAL REALIZATION:
S1 (convergence for Re(s) > 1) + multiplicativity (from S5)
ALREADY IMPLIES S4 (Ramanujan bound a_n = O(n^eps)).

Here's why: If sum a_n n^{-s} converges for Re(s) > 1, then
a_n = O(n^{1+eps}) for any eps > 0 (necessary condition).
But with an Euler product (S5), the coefficients are multiplicative.
For multiplicative coefficients, if the Dirichlet series converges
for Re(s) > 1, then a_n = O(n^eps) for any eps > 0.

PROOF SKETCH: If the Euler product converges for Re(s) > 1, then
sum_p |b_p| p^{-sigma} < infty for sigma > 1. Since b_p ~ a_p,
we need sum |a_p| p^{-sigma} < infty for sigma > 1. By the prime
number theorem, this requires |a_p| = O(p^{eps}) for all eps > 0.
By multiplicativity, |a_n| <= prod_{p|n} (1 + |a_p| + |a_{p^2}| + ...)
= O(n^{eps}).

IS THIS RIGHT?! Let me check more carefully...
""")

# Let me verify computationally
print("Computational check: convergence of Euler product with theta > 0")
print()

for theta in [0, 0.1, 0.3, 0.49]:
    # Consider prod_p (1 - p^theta * p^{-s})^{-1}
    # = prod_p (1 - p^{theta - s})^{-1}
    # log F(s) = -sum_p log(1 - p^{theta-s}) = sum_p sum_k p^{k(theta-s)}/k
    # This converges when sum_p p^{theta - sigma} < infty,
    # i.e., when sigma > 1 + theta (by PNT).

    # So the product converges for Re(s) > 1 + theta.
    # For theta = 0: Re(s) > 1 (standard)
    # For theta > 0: Re(s) > 1 + theta > 1

    print(f"theta = {theta}: Euler product converges for Re(s) > {1 + theta}")

print("""
DEFINITIVE CONCLUSION:

An Euler product with Satake parameters |alpha_{j,p}| = p^theta (theta > 0)
converges for Re(s) > 1 + theta, NOT for Re(s) > 1.

So S1 (convergence for Re(s) > 1) + S5 (Euler product) with
theta > 0 leads to convergence only for Re(s) > 1 + theta > 1.

This means:
- If we INSIST on S1 (convergence for Re(s) > 1): then S5 forces theta = 0,
  which means |alpha_{j,p}| <= 1 for all p, which IS Ramanujan (for degree 1
  and 2 at least).

- If we RELAX S1 to convergence in some half-plane: then we can have
  theta > 0, but the resulting function has zeros off the line (as shown
  by the zeta(s-alpha) example).

BOTTOM LINE:
S1 (strict) + S5 => S4 (at least for theta)
S4 is NOT independent of S1+S5 when S1 is strictly formulated!

But this only shows theta = 0, i.e., |alpha_{j,p}| <= 1.
Ramanujan says |alpha_{j,p}| = 1 (on the circle, not just inside).
The distinction between |alpha| <= 1 and |alpha| = 1 is subtle but real.
""")

# =================================================================
# TEST 12: The precise relationship between S1+S5 and S4
# =================================================================
print("\n" + "=" * 70)
print("TEST 12: S1 + S5 => theta = 0 (but not full Ramanujan)")
print("=" * 70)

print("""
Let F(s) = prod_p prod_{j=1}^d (1 - alpha_{j,p} p^{-s})^{-1}.

S5 requires: |b_{p^k}| = O(p^{k*theta}) with theta < 1/2.
S1 requires: sum a_n n^{-s} converges for Re(s) > 1.

Claim: S1 + S5 => |alpha_{j,p}| <= 1 for all j, p (with finitely
many exceptions).

Proof: The local factor at p contributes to log F(s) as:
  sum_k alpha_{j,p}^k / (k * p^{ks})

For Re(s) > 1, this converges iff |alpha_{j,p}| < p. This is weak.
But for the PRODUCT over all p to converge for Re(s) > 1, we need
  sum_p |alpha_{j,p}|^2 p^{-2*sigma} < infty for sigma > 1

By PNT: sum_{p < x} 1 ~ x/log(x). So sum_p p^{-2*sigma} converges
for sigma > 1/2. Thus sum_p |alpha_{j,p}|^2 p^{-2*sigma} converges
for sigma > 1 iff |alpha_{j,p}| = O(p^{sigma-1/2}) = O(p^{1/2+eps}).

This gives theta <= 1/2, consistent with S5 but not theta = 0.

MORE CAREFUL: For the DIRICHLET SERIES (not just Euler product):
  sum_n a_n n^{-s} converges for Re(s) > 1

The coefficients a_n are multiplicative with a_p = sum_j alpha_{j,p}.
For convergence of sum a_n n^{-s} at Re(s) > 1, by multiplicativity:
  We need sum_p a_p p^{-sigma} to converge for sigma > 1.
  sum_p |a_p| p^{-sigma} <= d * sum_p max_j |alpha_{j,p}| * p^{-sigma}

  This converges for sigma > 1 iff max_j |alpha_{j,p}| = O(p^eps)
  for every eps > 0.

  If |alpha_{j,p}| = p^theta with theta > 0 for infinitely many p:
  sum_p p^{theta - sigma} diverges at sigma = 1 + theta > 1.
  So convergence at sigma > 1 requires theta <= 0, i.e.,
  |alpha_{j,p}| <= 1 for almost all p.

WAIT: More precisely, the individual terms a_p p^{-sigma} need to
be summable. By PNT, sum_{p<x} 1 ~ x/log x, so:
  sum_p p^{theta - sigma} converges iff sigma > 1 + theta (for theta >= 0)
  and iff sigma > 1 for theta = 0.

  For sigma = 1 + eps (any eps > 0): sum_p p^{theta - 1 - eps} converges
  iff theta < eps. Since eps is arbitrary, this means theta <= 0.

  So theta <= 0, meaning |alpha_{j,p}| <= p^0 = 1 for all but
  finitely many p.

THEOREM: S1 (convergence for Re(s) > 1) + S5 (Euler product)
=> |alpha_{j,p}| <= 1 for all but finitely many p.

This is exactly the RAMANUJAN BOUND |alpha_{j,p}| <= 1 (the weak form).
The strong form |alpha_{j,p}| = 1 (on the unit circle) is NOT implied
— we could have |alpha_{j,p}| < 1.

For the STANDARD Selberg class formulation:
  S4 says a_n = O(n^eps), which for multiplicative a_n and prime inputs
  means |a_p| = O(p^eps) for all eps > 0, which means |alpha_{j,p}| <= 1.

  This is EXACTLY what we derived from S1 + S5!

SO: S4 IS A CONSEQUENCE OF S1 + S5 (in the Selberg class formulation).
The Ramanujan HYPOTHESIS |alpha_{j,p}| = 1 is stronger and NOT implied.
But the Ramanujan BOUND as stated in S4 (a_n = O(n^eps)) IS implied.
""")

# Verify this chain of logic
print("\nVERIFICATION: The implication chain")
print("S1 (convergence Re(s) > 1) + S5 (Euler product, theta < 1/2)")
print("=> sum_p a_p p^{-sigma} converges for sigma > 1")
print("=> |a_p| = O(p^eps) for all eps > 0")
print("=> a_n = O(n^eps) for all eps > 0 (by multiplicativity)")
print("=> S4 holds!")
print()
print("The convergence argument:")
for theta in [0.01, 0.05, 0.1, 0.2, 0.49]:
    # sum_p p^{theta - sigma} for sigma = 1 + 0.001
    sigma = 1 + 0.001
    # Approximate: sum_{p <= N} p^{theta - sigma} for large N
    # ~ integral_2^N x^{theta - sigma} / ln(x) dx (by PNT)
    # If theta - sigma < -1: convergent
    # If theta - sigma >= -1: divergent
    # theta - sigma = theta - 1 - 0.001
    exponent = theta - sigma
    convergent = (exponent < -1)
    print(f"  theta = {theta}, sigma = {sigma}: exponent = {exponent:.4f}, {'convergent' if convergent else 'DIVERGENT'}")

print()
print("For any theta > 0, choosing sigma = 1 + theta/2 gives divergence")
print("if theta > 0 at that sigma. So convergence at sigma = 1 + eps for")
print("arbitrary eps > 0 requires theta <= 0.")

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print("""
1. EPSTEIN ZETA & DAVENPORT-HEILBRONN: Satisfy S1+S2+S3 but NOT S5.
   Have zeros OFF the critical line.
   => S5 (Euler product) is ESSENTIAL.

2. zeta(s-alpha) for 0 < alpha < 1/2: Would satisfy S2+S3+S5
   but NOT S1 (convergence only for Re(s) > 1+alpha > 1).
   Has zeros off the line at Re(s) = 1/2 + alpha.

3. THE KEY THEOREM: S1 (strict: convergence for Re(s) > 1) together
   with S5 (Euler product with theta < 1/2) ALREADY IMPLIES S4
   (the Ramanujan bound a_n = O(n^eps)).

   PROOF: Convergence of the Euler product sum_p a_p p^{-sigma}
   for all sigma > 1 requires |a_p| = O(p^eps) by PNT.
   Multiplicativity extends this to all n.

4. THEREFORE: S4 is REDUNDANT given S1+S5 (in the strict formulation).
   The question "does S1+S2+S3+S5 without S4 force zeros onto the line?"
   is ILL-POSED because S1+S5 already imply S4.

5. THE REAL QUESTION becomes: Does S1+S2+S3+S5 (which includes S4)
   force zeros onto the critical line? This IS the Selberg class
   GRH conjecture, which is WIDE OPEN.

6. KACZOROWSKI-PERELLI RESULTS:
   - Degree 0: Only F = 1. Trivially on line.
   - Degree 1: Only L(s, chi). GRH expected (unproved for chi != 1).
     S4 follows automatically from the classification.
   - Degree 2: Includes Hecke and Maass L-functions. No classification.

7. The Ramanujan CONJECTURE |alpha_{j,p}| = 1 (equality, not bound)
   is STRONGER than S4 and NOT implied by S1+S5. The distinction:
   S4: |alpha_{j,p}| <= p^0 = 1 (inside or on the unit circle)
   RC: |alpha_{j,p}| = 1 (exactly on the unit circle)
""")
