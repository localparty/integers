"""
R31: Can the Euler product improve Lambda <= 1/2 to Lambda <= 0?

Investigation:
1. The de Bruijn-Newman constant Lambda and what determines it
2. How the zero-free region from the Euler product constrains Lambda
3. Ki-Kim-Lee (2009) and subsequent improvements
4. Whether the QG5D theta function gives better bounds
5. Multiplicative de Bruijn-Newman theory

Uses mpmath for high-precision arithmetic.
"""

from mpmath import (mp, mpf, mpc, pi, exp, sqrt, gamma, zeta, zetazero,
                    log, quad, fabs, re, im, nstr, cos, sin, inf, diff,
                    power, loggamma, cosh, sinh)
import numpy as np

mp.dps = 30

# ===================================================================
# Part 1: The de Bruijn-Newman kernel F(u) and Lambda
# ===================================================================

print("=" * 70)
print("PART 1: The de Bruijn-Newman kernel F(u)")
print("=" * 70)
print()

# The kernel F(u) is defined so that:
# Xi(t) = xi(1/2 + it) = integral_{-inf}^{inf} F(u) e^{itu} du
#        = 2 integral_0^{inf} F(u) cos(tu) du    [F is even]
#
# Explicitly (Edwards p.16, de Bruijn 1950):
# F(u) = sum_{n=1}^{inf} [2*pi^2*n^4*exp(9u/2) - 3*pi*n^2*exp(5u/2)] * exp(-pi*n^2*exp(2u))
#
# The heat-flow family:
# H_lambda(t) = integral F(u) e^{lambda*u^2} e^{itu} du
# Lambda = inf{lambda : H_lambda has all real zeros}
# RH <=> Lambda <= 0
# de Bruijn (1950): Lambda <= 1/2 (from F > 0)
# Rodgers-Tao (2020): Lambda >= 0

def F_kernel(u, nmax=200):
    """The de Bruijn-Newman kernel F(u) (even function, u >= 0)."""
    u = mpf(u)
    s = mpf(0)
    for n in range(1, nmax + 1):
        pn2 = pi * n**2
        eu = exp(2*u)
        s += (2*pn2**2*exp(mpf(9)*u/2) - 3*pn2*exp(mpf(5)*u/2)) * exp(-pn2*eu)
    return s

print("F(u) values (the de Bruijn-Newman kernel):")
print(f"  {'u':>6}  {'F(u)':>25}  {'sign':>6}")
for u_val in [0, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]:
    Fval = F_kernel(u_val)
    sign = "+" if Fval > 0 else "-" if Fval < 0 else "0"
    print(f"  {u_val:>6.1f}  {nstr(Fval, 15):>25}  {sign:>6}")

print()

# ===================================================================
# Part 2: Verify Xi(t) = Fourier transform of F
# ===================================================================

print("=" * 70)
print("PART 2: Verify Xi(t) = 2 int_0^inf F(u) cos(tu) du")
print("=" * 70)
print()

def xi_def(s):
    """xi(s) from definition."""
    return mpf(1)/2 * s * (s - 1) * pi**(-s/2) * gamma(s/2) * zeta(s)

def Xi_from_fourier(t_val, umax=20):
    """Xi(t) = xi(1/2+it) via Fourier transform of F."""
    t_val = mpf(t_val)
    def integrand(u):
        return F_kernel(u) * cos(t_val * u)
    return 2 * quad(integrand, [0, umax], maxdegree=8)

print("Verification at first 5 zeros of zeta:")
for k in range(1, 6):
    t_k = im(zetazero(k))
    Xi_direct = xi_def(mpc(mpf('0.5'), t_k))
    Xi_fourier = Xi_from_fourier(float(t_k))
    print(f"  t_{k} = {nstr(t_k, 10):>14}: |Xi_direct| = {nstr(fabs(Xi_direct), 4):>10}, "
          f"|Xi_fourier| = {nstr(fabs(Xi_fourier), 4):>10}")

# Also verify at non-zero points
print()
print("Verification at non-zero points:")
for t_val in [0, 5.0, 10.0]:
    Xi_direct = xi_def(mpc(mpf('0.5'), mpf(t_val)))
    Xi_fourier = Xi_from_fourier(t_val)
    print(f"  t = {t_val:>6.1f}: Xi_direct = {nstr(re(Xi_direct), 12):>16}, "
          f"Xi_fourier = {nstr(re(Xi_fourier), 12):>16}, "
          f"ratio = {nstr(re(Xi_fourier)/re(Xi_direct), 8)}")

print()

# ===================================================================
# Part 3: What the zero-free region gives in Lambda language
# ===================================================================

print("=" * 70)
print("PART 3: Zero-free region -> Lambda constraint")
print("=" * 70)
print()

# The classical zero-free region: zeta(s) != 0 for Re(s) >= 1 - c/log(|t|+2)
# In the s = sigma + it plane, this means:
# No zeros in {sigma > 1 - c/log(|t|+2)}
#
# In the de Bruijn-Newman framework:
# H_lambda(z) has zeros z_k(lambda) that move as lambda varies.
# At lambda = 0, the zeros of H_0 = Xi are the imaginary parts of
# zeta zeros on Re(s) = 1/2 (assuming RH), or complex numbers
# z_k = gamma_k + i*delta_k where rho_k = 1/2 + delta_k + i*gamma_k.
#
# The zero-free region tells us: no zeros of zeta in the region
# |Re(s) - 1/2| > 1/2 - c/log|t|. This means the "off-line distance"
# of any zero is at most 1/2 - c/log|t|.
#
# Translation to Lambda:
# A zero at s = 1/2 + delta + i*gamma with |delta| > 0 means the
# corresponding H_0 zero is at z = gamma + i*delta (complex).
# As lambda increases from 0, this complex zero moves toward the
# real axis and hits it at some lambda_k > 0.
# Lambda = sup_k lambda_k.
#
# For a zero at distance delta from the line, the lambda value at
# which it becomes real is approximately delta^2/(2 log |gamma|)
# (from the heat equation analysis).
#
# The zero-free region gives delta < 1/2 - c/log|gamma|.
# So lambda_k < (1/2 - c/log|gamma|)^2 / (2 log|gamma|)
#            ~ 1/(8 log|gamma|) for large |gamma|.
#
# This goes to 0 as |gamma| -> infinity! The zero-free region
# already implies that LARGE zeros contribute very little to Lambda.
# But it says nothing about SMALL zeros (|gamma| < some T_0).

print("Zero-free region in Lambda language:")
print()
print("The classical zero-free region: no zeta zeros for")
print("  Re(s) > 1 - c/log|Im(s)|  (Korobov-Vinogradov, c ~ 1/57)")
print()
print("For a hypothetical zero at s = 1/2 + delta + i*gamma:")
print("  The zero contributes to Lambda approximately delta^2/(2*log|gamma|)")
print("  The zero-free region gives delta < 1/2 - c/log|gamma|")
print()
print("Translation table (c = 1/57 ~ 0.0175):")
print(f"  {'|gamma|':>10}  {'max delta':>12}  {'max lambda_k':>14}  {'improvement':>14}")
for gamma_val in [14.13, 21.02, 100, 1000, 10000, 1e6, 1e10]:
    c_val = 1.0/57
    log_g = np.log(max(gamma_val, 3))
    max_delta = 0.5 - c_val / log_g
    max_lambda_k = max_delta**2 / (2 * log_g)
    improvement = 0.5 - max_lambda_k  # how much better than 1/2
    print(f"  {gamma_val:>10.2f}  {max_delta:>12.6f}  {max_lambda_k:>14.8f}  {improvement:>14.8f}")

print()
print("KEY OBSERVATION: The zero-free region gives lambda_k -> 0 as gamma -> infty.")
print("But Lambda = SUP of all lambda_k. The dangerous zeros are the SMALL ones")
print("(near the real axis in the s-plane, i.e., near gamma ~ 14).")
print("For these, the zero-free region gives delta < 0.493, lambda_k < 0.046.")
print("This is better than Lambda <= 1/2 but NOWHERE NEAR Lambda <= 0.")
print()

# ===================================================================
# Part 4: Ki-Kim-Lee and subsequent improvements
# ===================================================================

print("=" * 70)
print("PART 4: Known upper bounds on Lambda")
print("=" * 70)
print()

# History of Lambda upper bounds:
# de Bruijn (1950): Lambda <= 1/2 (from F > 0)
# Ki-Kim-Lee (2009): Lambda < 1/2 (strict inequality)
# Polymath 15 (2019): Lambda <= 0.22
# Current best: Lambda <= 0.22 (as of early 2026)
#
# The Ki-Kim-Lee argument:
# They proved Lambda < 1/2 by showing that for lambda slightly less
# than 1/2, the zeros of H_lambda are still all real. Their argument
# used the STRUCTURE of F, not just its positivity. Specifically,
# they showed that F has enough "Gaussian-like" properties near its
# peak to prevent zero-creation at lambda = 1/2 - epsilon.
#
# The Polymath 15 argument (Tao et al. 2019):
# Used barrier methods: showed that if Lambda > 0.22, then the zeros
# of H_lambda at lambda = 0.22 would have to satisfy certain
# constraints that are violated by numerical computation of actual
# zeta zeros. The argument combined:
# - The explicit formula (Euler product structure -> zero distribution)
# - Numerical computation of zeta zeros (the first ~10^6 zeros)
# - Barrier arguments for zero dynamics under heat flow

print("History of Lambda upper bounds:")
print(f"  {'Year':>6}  {'Author(s)':>25}  {'Bound':>15}  {'Method':>30}")
print(f"  {'1950':>6}  {'de Bruijn':>25}  {'<= 1/2':>15}  {'F > 0 (positivity)':>30}")
print(f"  {'2009':>6}  {'Ki-Kim-Lee':>25}  {'< 1/2':>15}  {'Structure of F near peak':>30}")
print(f"  {'2019':>6}  {'Polymath 15':>25}  {'<= 0.22':>15}  {'Barrier + explicit formula':>30}")
print()

# ===================================================================
# Part 5: What properties of F go beyond positivity?
# ===================================================================

print("=" * 70)
print("PART 5: Properties of F beyond positivity")
print("=" * 70)
print()

# The kernel F has many properties beyond mere F > 0:
# 1. F is EVEN: F(-u) = F(u)
# 2. F is REAL: F(u) in R for all u
# 3. F has a unique maximum at u = 0
# 4. F is super-exponentially decaying: F(u) ~ exp(-pi*exp(2u)) as u -> inf
# 5. F is log-concave
# 6. F satisfies the functional equation: related to F by s <-> 1-s
# 7. F has a MULTIPLICATIVE DECOMPOSITION coming from the Euler product:
#    since zeta = product_p (1-p^{-s})^{-1}, the Fourier kernel F
#    is related to a convolution of local kernels F_p.
#
# Property 7 is the KEY multiplicative structure.

# Check log-concavity: d^2/du^2 [log F(u)] < 0
print("Log-concavity of F(u):")
print(f"  {'u':>6}  {'F(u)':>18}  {'d^2 log F/du^2':>18}  {'log-concave?':>14}")
for u_val in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
    u = mpf(u_val)
    F_val = F_kernel(u_val)
    if F_val > 0:
        # Numerical second derivative of log F
        h = mpf('0.001')
        F_plus = F_kernel(u_val + float(h))
        F_minus = F_kernel(max(0, u_val - float(h)))
        if u_val == 0:
            F_minus = F_kernel(float(h))  # F is even
        logF_pp = (log(F_plus) - 2*log(F_val) + log(F_minus)) / h**2
        is_lc = "YES" if logF_pp < 0 else "NO"
        print(f"  {u_val:>6.1f}  {nstr(F_val, 10):>18}  {nstr(logF_pp, 8):>18}  {is_lc:>14}")

print()

# ===================================================================
# Part 6: The Euler product as convolution
# ===================================================================

print("=" * 70)
print("PART 6: Euler product -> convolution structure of F")
print("=" * 70)
print()

# log zeta(s) = sum_p sum_{k>=1} p^{-ks}/k  for Re(s) > 1
#
# In the Fourier representation:
# Xi(t) = xi(1/2+it) = exp(log xi(1/2+it))
#
# The Euler product gives:
# log zeta(1/2+it) = sum_p sum_k p^{-k(1/2+it)}/k
#                  = sum_p sum_k p^{-k/2} e^{-ikt log p} / k
#
# So log(Euler product part) = sum of oscillating terms with
# frequencies {log p, 2 log p, 3 log p, ...}.
#
# In the Fourier domain, this means the Euler product DECOMPOSES
# the function into a product, which in the Fourier domain becomes
# a CONVOLUTION:
#
# If H(t) = exp(sum_p f_p(t)), and f_p(t) involves e^{it log p},
# then in the Fourier domain:
# F(u) = F_Gamma(u) * conv_{p} F_p(u)
#
# where * denotes convolution and F_p is the local Fourier kernel
# for the p-th Euler factor.
#
# This is the MULTIPLICATIVE de Bruijn-Newman structure:
# The kernel F is a CONVOLUTION of local kernels F_p,
# one for each prime.

# Let's compute the contribution of a single Euler factor
# (1 - p^{-s})^{-1} to the kernel.
#
# For a single factor: zeta_p(s) = (1 - p^{-s})^{-1}
# log zeta_p(s) = -log(1 - p^{-s}) = sum_{k>=1} p^{-ks}/k
#
# At s = 1/2 + it:
# log zeta_p(1/2+it) = sum_{k>=1} p^{-k/2} e^{-ikt log p} / k

print("Local Euler factor contributions at s = 1/2 + it:")
print()
for p in [2, 3, 5, 7, 11]:
    # |log zeta_p(1/2+it)| <= sum_{k>=1} p^{-k/2}/k = -log(1 - p^{-1/2})
    bound = -float(log(1 - p**(-0.5)))
    # The contribution oscillates with period 2*pi/log(p)
    period = 2 * np.pi / np.log(p)
    print(f"  p = {p:>3}: |log zeta_p| <= {bound:.6f}, "
          f"oscillation period in t = {period:.4f}")

print()
print("The Euler product decomposes F into a convolution:")
print("  F(u) = F_Gamma(u) * F_2(u) * F_3(u) * F_5(u) * ...")
print("  where * is convolution and F_p is the local kernel for prime p.")
print()
print("Each F_p encodes the p-th Euler factor (1-p^{-s})^{-1}.")
print("The convolution structure is the MULTIPLICATIVE analog of")
print("the additive theta function sum.")
print()

# ===================================================================
# Part 7: Can convolution structure improve Lambda?
# ===================================================================

print("=" * 70)
print("PART 7: Does convolution structure improve Lambda?")
print("=" * 70)
print()

# The key question: does the decomposition F = conv_p F_p give
# a better Lambda bound than treating F as a monolithic positive function?
#
# Fact 1: If g = f1 * f2 (convolution), and both f1, f2 have only
# real Fourier zeros, then g = f1*f2 in the time domain, and
# g-hat = f1-hat * f2-hat. The zeros of g-hat are the union of zeros
# of f1-hat and f2-hat, all on the real line. So:
#
# "Convolution of functions with real Fourier zeros
#  = product of functions with real Fourier zeros
#  = function with real Fourier zeros."
#
# This is the Lee-Yang property: the class of functions with all real
# zeros is closed under multiplication (in the transform domain, i.e.,
# closed under convolution in the kernel domain).
#
# But wait -- the individual Euler factors DO NOT have all zeros on the
# critical line. Each (1 - p^{-s})^{-1} has NO zeros at all (it's the
# reciprocal of a function with zeros at s = 2*pi*i*k/log p for k in Z).
# So the convolution argument goes the wrong way: we're convolving
# functions that are zero-free, not functions with real zeros.

print("Analysis: Does the convolution decomposition help?")
print()
print("Fact: Each local factor zeta_p(s) = (1-p^{-s})^{-1} is NONVANISHING.")
print("      Its zeros (the zeros of 1-p^{-s}) are at s = 2*pi*i*k/log(p),")
print("      which lie on Re(s) = 0, NOT on Re(s) = 1/2.")
print()
print("So the individual factors don't have zeros on Re(s) = 1/2.")
print("The zeros of zeta on Re(s) = 1/2 are a COLLECTIVE phenomenon:")
print("they arise from the INFINITE PRODUCT of all Euler factors.")
print()
print("The convolution structure tells us:")
print("  F(u) = F_Gamma(u) * (conv_p F_p(u))")
print("  where each F_p > 0 (since zeta_p has no zeros)")
print("  and F_Gamma > 0 (from the Gamma factor)")
print()
print("Convolution of positive functions is positive: F > 0.")
print("This gives Lambda <= 1/2 (de Bruijn) -- same as before.")
print("The convolution structure REPRODUCES the positivity but")
print("does not IMPROVE on it.")
print()

# ===================================================================
# Part 8: The Polymath 15 approach and why it works
# ===================================================================

print("=" * 70)
print("PART 8: How Polymath 15 got Lambda <= 0.22")
print("=" * 70)
print()

# Polymath 15 (Tao et al. 2019) proved Lambda <= 0.22.
# Their method:
#
# 1. BARRIER ARGUMENT: If Lambda > lambda_0, then at heat time lambda_0,
#    there must be a complex zero of H_{lambda_0}. This complex zero
#    must be near a pair of real zeros that are about to collide and
#    split into the complex plane.
#
# 2. EXPLICIT FORMULA: The zeros of H_{lambda_0} are related to zeta
#    zeros by the heat flow. The explicit formula connects zeta zeros
#    to prime sums. This gives CONSTRAINTS on where complex zeros can form.
#
# 3. NUMERICAL VERIFICATION: Compute the first ~10^6 zeta zeros and
#    verify that none of them, under heat flow backward from lambda = 0.22,
#    would produce a complex zero.
#
# The key insight: the Euler product enters through the EXPLICIT FORMULA.
# The explicit formula is:
#   sum_{rho} h(rho) = h-hat(0) + h-hat(1) - sum_p sum_k (log p) h-hat(log p^k) / p^{k/2}
#
# The prime sum on the right constrains the zero distribution on the left.
# The constraint is: zeros can't be "too clustered" or "too spread out"
# because the prime sum has a specific structure.
#
# This is how the Euler product improves Lambda:
# NOT by making F "more positive" (it's already positive),
# BUT by constraining the ZERO DISTRIBUTION of Xi = H_0.

print("Polymath 15 method (Tao, Trudgian, Platt et al. 2019):")
print()
print("1. BARRIER: If Lambda > 0.22, a complex zero of H_{0.22} must exist.")
print("2. EXPLICIT FORMULA: Constrains where complex zeros can form,")
print("   using the Euler product via the Weil explicit formula.")
print("3. NUMERICAL: Verify no zero collision occurs for first ~10^6 zeros")
print("   under heat flow backward from lambda = 0.22.")
print()
print("The Euler product enters through the EXPLICIT FORMULA,")
print("which constrains the zero distribution. This is an INDIRECT")
print("use of multiplicative structure -- the Euler product constrains")
print("the zero distribution, which constrains Lambda.")
print()
print("This is fundamentally different from trying to use the Euler")
print("product to improve POSITIVITY of F. The improvement comes from")
print("constraining the ZEROS, not from strengthening the KERNEL.")
print()

# ===================================================================
# Part 9: Does the QG5D R = R* theta give better bounds?
# ===================================================================

print("=" * 70)
print("PART 9: QG5D theta function vs generic theta")
print("=" * 70)
print()

# The QG5D framework identifies the e-circle radius R with a specific
# value related to the self-dual radius R* = 1/(2*sqrt(pi)).
# At this radius, the spectral zeta is:
#   Z_{S^1}(s) = 2*R^{2s} * zeta(2s)
#
# The theta function is:
#   theta_R(t) = sum_{n in Z} exp(-pi*n^2*t/R^2)    [for generic R]
#   theta_1(t) = sum_{n in Z} exp(-pi*n^2*t)          [for R = 1]
#
# The de Bruijn-Newman constant Lambda does NOT depend on R:
# different R values give a rescaling of the kernel F(u) that
# doesn't change the zero locations.
#
# More precisely: theta_R(t) = theta_1(t/R^2), so the kernel becomes
# F_R(u) = F_1(u - log R), which shifts the argument but doesn't
# change the zeros of the Fourier transform.
#
# So the QG5D specific radius does NOT give a better Lambda bound.

print("Does the QG5D e-circle radius R give a better Lambda?")
print()
print("  theta_R(t) = theta_1(t/R^2)")
print("  F_R(u) = F_1(u - log R)")
print()
print("  A shift in u does not change the zeros of the Fourier transform.")
print("  Lambda is invariant under rescaling of the theta function.")
print()
print("  CONCLUSION: The specific radius R of the QG5D e-circle does NOT")
print("  give a better Lambda bound. Lambda depends on the ARITHMETIC")
print("  structure of Z (unique factorization), not on the geometric")
print("  parameter R.")
print()

# ===================================================================
# Part 10: The Mellin bridge (P5m) and log zeta constraint
# ===================================================================

print("=" * 70)
print("PART 10: Can P5m translate the Euler product to a heat constraint?")
print("=" * 70)
print()

# The Euler product gives: log zeta(s) = sum_p sum_k p^{-ks}/k
# for Re(s) > 1.
#
# The Mellin transform connects theta to zeta:
#   pi^{-s/2} Gamma(s/2) zeta(s) = Mellin[psi](s/2)
#   where psi(t) = (theta(t) - 1)/2
#
# So: log[pi^{-s/2} Gamma(s/2)] + log zeta(s) = log Mellin[psi](s/2)
#
# The Euler product constrains log zeta. Can this be translated to a
# constraint on psi (and hence on theta)?
#
# The constraint: log zeta(s) = sum_p sum_k p^{-ks}/k is a SPECIFIC
# Dirichlet series with positive coefficients (for Re(s) > 1).
# This means: Re(log zeta(sigma+it)) has a specific Fourier structure
# in t, with frequencies {log p, 2 log p, ...}.
#
# In the Mellin domain: psi(t) = Mellin^{-1}[pi^{-s/2} Gamma(s/2) zeta(s)](s/2)
# The Euler product constraint on zeta becomes:
# psi(t) = Mellin^{-1}[pi^{-s/2} Gamma(s/2) exp(sum_p sum_k p^{-ks}/k)](s/2)
#
# This is a constraint on psi, but it's TAUTOLOGICAL: it just says
# psi is what it is. The Euler product doesn't add NEW information
# about psi that wasn't already encoded in psi being the theta function
# of Z.

print("P5m translation attempt:")
print()
print("  log zeta(s) = sum_p sum_k p^{-ks}/k    [Euler product]")
print("  zeta(s) = Mellin[theta-1](s/2) / [2*pi^{-s/2}*Gamma(s/2)]")
print()
print("  The Euler product constrains log(Mellin[theta-1](s/2)).")
print("  But this is EQUIVALENT to saying that theta is the Jacobi")
print("  theta function of the integer lattice Z.")
print()
print("  The Euler product does NOT give a NEW constraint on theta.")
print("  It is a RESTATEMENT of the fact that theta encodes the")
print("  multiplicative structure of Z via the Mellin transform.")
print()
print("  This is the fundamental circularity:")
print("  theta encodes Z (additive structure)")
print("  Euler product encodes Z (multiplicative structure)")
print("  P5m (Mellin) translates between them")
print("  But the information content is the SAME -- it's Z.")
print()

# ===================================================================
# Part 11: What WOULD close the gap?
# ===================================================================

print("=" * 70)
print("PART 11: What would close the gap Lambda in [0, 1/2] to Lambda = 0?")
print("=" * 70)
print()

# Three approaches have improved the upper bound on Lambda:
#
# A. POSITIVITY (de Bruijn 1950): F > 0 => Lambda <= 1/2.
#    This is the WEAKEST bound, using only additive structure.
#
# B. STRUCTURE OF F (Ki-Kim-Lee 2009): F has specific shape =>
#    Lambda < 1/2 (strict). Uses more than positivity.
#
# C. EXPLICIT FORMULA + NUMERICS (Polymath 15, 2019):
#    Euler product + numerical zero data => Lambda <= 0.22.
#    Uses the MULTIPLICATIVE structure via the explicit formula.
#
# The progression: A uses additive tools only.
#                  B uses slightly more than additive.
#                  C uses multiplicative tools + numerics.
#
# To reach Lambda = 0, one would need either:
# (i) A NON-NUMERICAL proof from the Euler product alone, or
# (ii) A new structural property of F that implies Lambda <= 0.
#
# Option (i) is essentially the Riemann Hypothesis (any proof of RH
# gives Lambda = 0 as a corollary).
#
# Option (ii) would require finding a property P of F such that:
# - P is provable from the definition of F (i.e., from properties of theta)
# - P implies Lambda <= 0
# - P is stronger than positivity but weaker than "all Fourier zeros are real"

print("Three levels of upper bounds on Lambda:")
print()
print("Level A (Additive): F > 0 => Lambda <= 1/2")
print("  Uses: positivity of theta function (RP on S^1)")
print("  Gap to RH: 1/2")
print()
print("Level B (Structural): Ki-Kim-Lee => Lambda < 1/2 (strict)")
print("  Uses: shape of F near its maximum, not just sign")
print("  Gap to RH: slightly less than 1/2")
print()
print("Level C (Multiplicative): Polymath 15 => Lambda <= 0.22")
print("  Uses: Euler product (via explicit formula) + numerical zeros")
print("  Gap to RH: 0.22")
print()
print("Level D (RH): Lambda = 0")
print("  Requires: full arithmetic structure of zeta")
print()
print("The gap from Level A to Level D is the full arithmetic content.")
print("The gap from Level C to Level D is 0.22 -- still requires a")
print("conceptual breakthrough, not just better numerics.")
print()

# ===================================================================
# Part 12: Is there a MULTIPLICATIVE de Bruijn-Newman theory?
# ===================================================================

print("=" * 70)
print("PART 12: Multiplicative de Bruijn-Newman theory?")
print("=" * 70)
print()

# The de Bruijn-Newman framework is ADDITIVE: it deforms xi via the
# heat equation (backward heat flow). The kernel e^{lambda*u^2} is
# Gaussian -- the most basic additive kernel.
#
# Is there a MULTIPLICATIVE version? That is, a deformation of xi
# that respects the Euler product structure?
#
# Candidate: MULTIPLICATIVE HEAT FLOW.
# Instead of deforming xi(s) = exp(lambda * d^2/ds^2) xi_0(s),
# deform each Euler factor independently:
#   zeta_lambda(s) = prod_p (1 - p^{-(s+lambda*f(p))})^{-1}
# for some function f(p) of the prime.
#
# If f(p) = 1: this shifts s -> s + lambda, which shifts all zeros
# by lambda to the left. This makes Lambda trivially 0 for lambda >= 1/2
# (since all zeros satisfy Re(rho) > 0, shifting by 1/2 puts them on
# Re(s) > 1/2). But this is just the classical result Re(rho) > 0.
#
# If f(p) = log log p / log p or similar: this could give a nontrivial
# deformation that respects the Euler product. But no such theory exists.
#
# The fundamental problem: the Euler product is defined for Re(s) > 1.
# The zeros are at Re(s) = 1/2. The Euler product DIVERGES at the zeros.
# Any multiplicative deformation must grapple with this divergence.

print("Is there a multiplicative de Bruijn-Newman theory?")
print()
print("The additive DN framework: H_lambda(t) = Fourier[e^{lambda*u^2}*F(u)]")
print("  - Lambda >= 0 from ARITHMETIC (Rodgers-Tao)")
print("  - Lambda <= 1/2 from POSITIVITY (de Bruijn)")
print()
print("A multiplicative version would deform the Euler product directly:")
print("  zeta_lambda(s) = prod_p (1 - p^{-s-lambda*f(p)})^{-1}")
print()
print("Problem: the Euler product DIVERGES for Re(s) <= 1.")
print("The zeros live in the region where the Euler product doesn't converge.")
print("Any multiplicative deformation must work with the ANALYTIC CONTINUATION")
print("of the product, not the product itself.")
print()
print("ASSESSMENT: No multiplicative de Bruijn-Newman theory exists.")
print("The DN framework is intrinsically ADDITIVE (heat equation).")
print("The Euler product enters only INDIRECTLY, through the")
print("explicit formula and the constraint on zero distribution.")
print()

# ===================================================================
# SUMMARY
# ===================================================================

print("=" * 70)
print("SUMMARY: Can Lambda <= 1/2 be improved to Lambda <= 0")
print("         using the Euler product?")
print("=" * 70)
print()
print("SHORT ANSWER: Not directly. The Euler product has already been")
print("used (by Polymath 15) to get Lambda <= 0.22, but this uses the")
print("Euler product INDIRECTLY (via the explicit formula + numerics).")
print("A direct improvement to Lambda <= 0 would constitute a proof of RH.")
print()
print("DETAILED FINDINGS:")
print()
print("1. de Bruijn (1950): F > 0 => Lambda <= 1/2. This is the pure")
print("   positivity bound. RP on S^1 gives exactly this.")
print()
print("2. The zero-free region from the Euler product gives:")
print("   lambda_k ~ delta^2/(2*log|gamma|) < 1/(8*log|gamma|)")
print("   This goes to 0 for LARGE zeros but says nothing about SMALL ones.")
print("   It does NOT give Lambda <= 0.")
print()
print("3. The Euler product decomposes F into a convolution of local")
print("   kernels F_p. Each F_p > 0. Convolution of positive functions")
print("   is positive. This REPRODUCES Lambda <= 1/2, doesn't improve it.")
print()
print("4. Polymath 15 used the Euler product (via explicit formula) +")
print("   numerical zero data to get Lambda <= 0.22. This is the best")
print("   known bound (as of 2026). The method is inherently numerical.")
print()
print("5. No multiplicative de Bruijn-Newman theory exists. The DN")
print("   framework is additive (heat equation). The Euler product")
print("   enters only indirectly.")
print()
print("6. The QG5D radius R does not improve Lambda. Lambda depends on")
print("   the arithmetic of Z, not the geometric parameter R.")
print()
print("7. The P5m bridge (Mellin transform) translates between additive")
print("   and multiplicative descriptions but does not create NEW")
print("   information. The Euler product constraint on theta is")
print("   tautological -- it just says theta is the theta function of Z.")
print()
print("HONEST ASSESSMENT: The gap Lambda in [0, 1/2] cannot be closed")
print("from above by combining positivity with the Euler product in any")
print("known way. The Polymath 15 approach (explicit formula + numerics)")
print("is the only method that has improved the upper bound, and it")
print("appears to be inherently limited by computational resources.")
print("Closing the gap to Lambda = 0 requires a conceptual breakthrough")
print("that goes beyond both positivity and the explicit formula.")
