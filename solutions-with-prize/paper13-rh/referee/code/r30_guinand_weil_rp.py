"""
R30: Does RP Supply ALL Test Functions for Guinand-Weil Positivity?

Five investigations:
  A: What EXACTLY are the test functions h for which Weil positivity must hold?
  B: Can these h be constructed from the QG5D RP inner product?
  C: Nyman-Beurling criterion and the QG5D Hilbert space
  D: Li's criterion as Weil positivity — lambda_n >= 0 for ALL n simultaneously
  E: Multiplicative reformulation of RP

Computational checks to accompany research/74-r30-guinand-weil-rp.md
"""

import numpy as np
from mpmath import (mp, zetazero, zeta, gamma, log, pi, mpf, mpc,
                    fsum, exp, cos, sin, sqrt, quad, inf, loggamma,
                    digamma, diff, floor, re, im, conj, power, fac,
                    binomial)

mp.dps = 30

# ======================================================================
# PART A: The exact class of test functions for Weil positivity
# ======================================================================
print("=" * 72)
print("PART A: Test Function Classes for Guinand-Weil Positivity")
print("=" * 72)

# Get 50 zeros for high-precision sums
N_zeros = 50
zeros_rho = []
zeros_gamma = []
for k in range(1, N_zeros + 1):
    rho = zetazero(k)
    zeros_rho.append(rho)
    zeros_gamma.append(float(rho.imag))

print(f"\nUsing {N_zeros} zeros (gamma_1 = {zeros_gamma[0]:.6f} ... gamma_{N_zeros} = {zeros_gamma[-1]:.6f})")

# Class 1: h = f * f~ (autocorrelation) — the Weil criterion class
# For f in C_c^infty(R), h(t) = int f(u) conj(f(u-t)) du
# Then h_hat(x) = |f_hat(x)|^2 >= 0 automatically
# Weil positivity: W(h) = sum_rho h(gamma_rho) >= 0 for ALL such h

print("\n--- Class 1: Autocorrelation functions h = f * f~ ---")
print("   These are EXACTLY the positive-definite functions.")
print("   h_hat >= 0 is automatic. W(h) >= 0 is RH.")

# Subclass 1a: f = Gaussian => h = Gaussian
print("\n  1a) Gaussian: h(t) = exp(-a*t^2)")
for a in [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]:
    W = 2 * sum(np.exp(-a * g**2) for g in zeros_gamma)
    print(f"    a = {a:6.3f}: W = {W:12.6f}  {'OK' if W >= 0 else 'FAIL'}")

# Subclass 1b: f = indicator of [0, T] => h = triangle function
print("\n  1b) Triangle: h(t) = max(0, T - |t|)")
for T in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    W = 2 * sum(max(0, T - abs(g)) for g in zeros_gamma)
    # All zeros have gamma > 14.13, so for T < 14.13, h(gamma) = 0
    # This means W = 0 trivially for small T
    print(f"    T = {T:5.1f}: W = {W:12.6f}  {'OK (trivial)' if W == 0 else ('OK' if W >= 0 else 'FAIL')}")

# Subclass 1c: f = characteristic function of [0,T] in Fourier space
# Then h_hat(x) = 1 for |x| <= T, so h is a sinc-like function
print("\n  1c) Fejer kernel: h(t) = (sin(Tt/2)/(t/2))^2 / (2*pi)")
for T in [1.0, 5.0, 10.0, 20.0, 50.0, 100.0]:
    W = 0.0
    for g in zeros_gamma:
        if abs(g) > 1e-10:
            h_val = (np.sin(T * g / 2) / (g / 2))**2 / (2 * np.pi)
        else:
            h_val = T**2 / (2 * np.pi)
        W += 2 * h_val
    print(f"    T = {T:6.1f}: W = {W:12.6f}  {'OK' if W >= 0 else 'FAIL'}")

# Class 2: Even Schwartz functions with h_hat in C_c^infty
# (a larger class — not necessarily positive-definite)
# For these, W(h) is SIGNED — it can be negative if RH fails.
# The condition sum_rho h(gamma_rho) >= 0 for ALL h in this class
# is STRONGER than just for autocorrelations.

print("\n--- Class 2: Even Schwartz functions (not necessarily h = f*f~) ---")
print("   W(h) >= 0 for ALL such h is EQUIVALENT to RH")
print("   But only for h = f*f~ (positive-definite) is it the standard criterion")

# A non-positive-definite test: h(t) = cos(b*t) * exp(-a*t^2)
# h_hat(x) = sqrt(pi/a)/2 * [exp(-(x-b)^2/(4a)) + exp(-(x+b)^2/(4a))]
# h_hat CAN be negative for some x (it's a sum of two shifted Gaussians)
# But h is NOT of the form f*f~ unless b=0

print("\n  Non-positive-definite test: h(t) = cos(b*t)*exp(-a*t^2)")
a = 0.01
for b in [0.0, 14.13, 21.02, 25.01, 30.42, 32.93]:
    W = 2 * sum(np.cos(b * g) * np.exp(-a * g**2) for g in zeros_gamma)
    is_pd = (b == 0.0)  # only positive-definite when b=0
    label = "pos-def" if is_pd else "NOT p-d"
    sign = "OK" if W >= -1e-8 else "NEGATIVE"
    print(f"    b = {b:6.2f} ({label}): W = {W:12.6f}  {sign}")

print("\n  Key: W CAN be negative for non-positive-definite h.")
print("  This does NOT contradict RH; Weil positivity only requires")
print("  W(h) >= 0 for h = f*f~ (positive-definite functions).")


# ======================================================================
# PART B: Can RP construct the Weil test functions?
# ======================================================================
print("\n" + "=" * 72)
print("PART B: RP Inner Product vs Weil Test Functions")
print("=" * 72)

# The QG5D RP inner product on S^1:
#   <f, Theta f>_{S^1} = int_{S^1} f(phi) * f(-phi) dphi
# Under exp map phi -> x = e^{phi/R}:
#   <f, Theta f> = int_{R+*} f(x) * conj(f(1/x)) dx/x
# This is the Weil pairing at the archimedean place.

# Question: what test functions on the spectral side does this generate?

# The RP inner product involves:
#   f in L^2(S^1, dphi) supported on [0, pi*R] (positive half-circle)
# Under Fourier transform on S^1:
#   f(phi) = sum_n a_n e^{in*phi/R}
# The RP condition is:
#   <f, Theta f> = sum_n |a_n|^2 * <e_n, Theta e_n> >= 0
# For the KK modes e_n(phi) = e^{in*phi/R}:
#   <e_n, Theta e_n> = int_0^{2piR} e^{in*phi/R} * e^{in*phi/R} dphi
#                    = int_0^{2piR} e^{2in*phi/R} dphi = 0 for n != 0, 2piR for n=0
# WAIT — this is the wrong computation. RP reflects phi -> -phi:
#   Theta e_n(phi) = e_n(-phi) = e^{-in*phi/R}
#   <e_n, Theta e_n> = int e^{in*phi/R} * e^{-in*phi/R} dphi = 2piR (for all n)
# So <f, Theta f> = 2piR * sum_n |a_n|^2 >= 0 trivially!

# But this is on the FULL circle. RP requires f supported on HALF the circle.
# For f supported on phi in [0, pi*R]:
#   <f, Theta f> = int_0^{piR} f(phi) * conj(f(-phi)) dphi
# Since f is supported on [0, piR], f(-phi) = 0 for phi in [0, piR].
# So <f, Theta f> = 0 trivially? No — Theta f is supported on [-piR, 0],
# so the inner product is <f, Theta f> = int_{-piR}^{piR} f(phi) (Theta f)(phi) dphi
# where (Theta f)(phi) = f(-phi) is supported on [-piR, 0].
# But f is supported on [0, piR], so the supports don't overlap!
# Unless we're computing int f(phi) * overline{(Theta f)(phi)} dphi over ALL of S^1.

# Standard OS RP: <f, Theta f> = int f(phi) * overline{Theta f(phi)} dphi
# where Theta f(phi) = overline{f(-phi)} (for scalar fields).
# Actually, for REAL scalar fields: Theta f(phi) = f(-phi).
# For complex fields: Theta f(phi) = overline{f(-phi)}.

# The proper formulation: f is a function on [0, piR] (positive half).
# Extend f to [0, 2piR] by f(phi) = 0 for phi in [piR, 2piR].
# Theta extends to [-piR, 0] by (Theta f)(phi) = overline{f(-phi)} for phi in [-piR, 0].
# The RP inner product is the overlap of the PROPAGATED f with Theta f:
#   <f, Theta f> = integral over S^1 of (e^{-tau*H} f)(phi) * overline{(Theta f)(phi)} dphi
# where H is the Hamiltonian and tau is the Euclidean time separation.

# For the SPECTRAL formulation:
# h_RP(n) = |f_hat(n)|^2 * e^{-tau*lambda_n}
# where lambda_n = n^2/R^2 are the S^1 eigenvalues.

# Under the map to the Weil pairing (via exponential map),
# the spectral parameter n/R maps to the imaginary part of s.
# The test function on the spectral side is:
#   h(t) = sum_n |a_n|^2 * e^{-tau * (t - n/R)^2 / (something)}

# Let's compute what RP generates as a Weil test function

print("\n--- The RP-to-Weil map ---")
print("  RP on S^1:  <f, Theta f> = sum_n |c_n|^2 * e^{-tau*n^2/R^2}")
print("  (for f = sum c_n e_n with e_n = KK modes)")
print()
print("  Under exp map phi -> x = e^{phi/R}:")
print("  This becomes the Weil pairing at the archimedean place:")
print("    int_{R+*} f(x) conj(f(1/x)) dx/x")
print()
print("  The spectral test function generated by RP is:")
print("    h_RP(t) = |f_hat(1/2 + it)|^2 * kernel(t)")
print("  where f_hat is the Mellin transform of f.")
print()
print("  KEY CONSTRAINT: h_RP is of the form |g|^2 >= 0,")
print("  so it IS a positive-definite function.")
print("  Therefore RP generates exactly the CLASS of test functions")
print("  needed for Weil positivity (autocorrelations = pos-def functions).")

print("\n  But WHICH positive-definite functions can RP generate?")
print("  The answer depends on the Hilbert space L^2(S^1).")
print("  If f ranges over ALL of L^2(S^1, half-circle), then |f_hat|^2")
print("  ranges over ALL positive-definite functions with compact support")
print("  in Mellin space. These are a PROPER SUBSET of all positive-definite")
print("  functions.")

# Numerical test: can we approximate arbitrary positive-definite h
# using RP-generated test functions?
print("\n--- Can RP approximate arbitrary positive-definite functions? ---")

# An RP-generated test function from N modes on S^1 with R=1:
# h_N(t) = |sum_{n=0}^{N} c_n / (1/2 + it - in)|^2
# This has poles at t = i(n - 1/2) and is entire on the real line.

# Weil positivity needs h(gamma_rho) values. Let's check if RP
# functions can be tuned to match arbitrary positive-definite h.

# Take h(t) = exp(-a*t^2) (Gaussian, positive-definite)
# Can we write exp(-a*t^2) = |g(t)|^2 for some g in the RP Hilbert space?
# g(t) = exp(-a*t^2/2) works, and g is entire, so YES.

# Take h(t) = (sin(Tt)/(pi*t))^2 (Fejer, positive-definite, compact Fourier support)
# Can we write this as |g(t)|^2?
# g(t) = sin(Tt)/(pi*t) works (sinc function).
# Is g in the RP Hilbert space? g has Fourier support on [-T, T].
# On S^1 with R finite, g can be approximated by modes up to n ~ TR.
# So YES, for any T, choosing R large enough gives the approximation.

print("  Gaussian h(t) = exp(-a*t^2): YES (g = exp(-a*t^2/2) is in L^2)")
print("  Fejer h(t) = sinc^2: YES (g = sinc, needs R ~ T)")
print("  Arbitrary pos-def h: YES if L^2(S^1) is dense in the right topology")
print()
print("  CONCLUSION: The RP Hilbert space CAN generate all positive-definite")
print("  test functions in the ARCHIMEDEAN variable, because L^2(R+*, dx/x)")
print("  under the exponential map contains all Mellin-square-integrable functions,")
print("  and |g|^2 for g in this space gives all positive-definite functions.")


# ======================================================================
# PART C: Nyman-Beurling Criterion
# ======================================================================
print("\n" + "=" * 72)
print("PART C: Nyman-Beurling Criterion and QG5D Hilbert Space")
print("=" * 72)

# Nyman-Beurling: RH <=> the constant function 1 is in the L^2(0,1)
# closure of the span of {rho_alpha : 0 < alpha <= 1}, where
# rho_alpha(x) = {alpha/x} - alpha*{1/x} (fractional parts).
# Equivalently: rho_alpha(x) = alpha/x - floor(alpha/x) - alpha*(1/x - floor(1/x))
# Simpler: rho_alpha(x) = frac(alpha/x) for the Nyman version.

# Baez-Duarte (2003) simplified: RH <=> the indicator function
# chi_{(0,1)} is in the L^2(0, infty) closure of the span of
# {d_k(x) = sum_{j=0}^{k} (-1)^j C(k,j) rho_{1/(j+1)}(x)}.

# The key space: L^2(0, 1) or L^2(0, infty) with Lebesgue measure.

# Question: does the QG5D Hilbert space = L^2(S^1) under the
# exponential map contain the Nyman-Beurling functions?

print("\n--- Nyman-Beurling Criterion ---")
print("  RH <=> chi_{(0,1)} in closure of span{rho_{1/k} : k >= 1}")
print("  in L^2(0, infty)")
print()
print("  rho_alpha(x) = {alpha/x}  (fractional part)")
print()
print("  QG5D connection: under exp map phi -> x = e^{phi/R},")
print("  L^2(0,infty, dx) maps to L^2(R, e^{phi/R} dphi).")
print("  This is NOT the same as L^2(S^1, dphi) — the measure differs!")
print()
print("  The RP Hilbert space is L^2(S^1, dphi) = L^2(R+*, dx/x)")
print("  The NB Hilbert space is L^2(0,infty, dx)")
print("  These are DIFFERENT spaces with DIFFERENT measures.")

# Compute: the Nyman-Beurling functions and their Mellin transforms
print("\n--- Mellin transforms of NB functions ---")
print("  rho_alpha(x) = {alpha/x} has Mellin transform:")
print("  M[rho_alpha](s) = -zeta(s) * alpha^s / s  for Re(s) > 1")
print()
print("  The Mellin transform connects NB to the Weil explicit formula!")
print("  If zeta(1/2+it) = 0, then M[rho_alpha](1/2+it) = 0 for all alpha.")
print("  The NB functions 'feel' the zeros through their Mellin transforms.")

# Can the RP Hilbert space supply the NB functions?
# L^2(R+*, dx/x) vs L^2(0,1, dx):
# A function f in L^2(R+*, dx/x) satisfies int |f(x)|^2 dx/x < infty.
# A function g in L^2(0,1, dx) satisfies int_0^1 |g(x)|^2 dx < infty.
# If f(x) = g(x) * sqrt(x) then int |f|^2 dx/x = int |g|^2 dx. So:
# L^2(0,1, dx) embeds into L^2(R+*, dx/x) via multiplication by sqrt(x).

print("\n  Embedding: L^2(0,1, dx) -> L^2(R+*, dx/x) via f(x) = g(x)*sqrt(x)")
print("  So NB functions CAN be embedded into the RP Hilbert space.")
print("  But: the NB density condition is about approximation in L^2(0,1, dx),")
print("  not in L^2(R+*, dx/x). The topologies are DIFFERENT.")
print()
print("  CONCLUSION: The RP Hilbert space CONTAINS the NB functions")
print("  (after a change of measure), but the NB density condition is")
print("  formulated in a DIFFERENT norm. RP positivity does not directly")
print("  imply NB density.")


# ======================================================================
# PART D: Li's Criterion — lambda_n >= 0 for ALL n
# ======================================================================
print("\n" + "=" * 72)
print("PART D: Li's Criterion as Weil Positivity")
print("=" * 72)

# Li (1997): RH <=> lambda_n >= 0 for all n >= 1, where
# lambda_n = sum_rho [1 - (1 - 1/rho)^n]
# = (1/((n-1)!)) * d^n/ds^n [s^{n-1} log xi(s)]|_{s=1}

# Coffey (2005): lambda_n = n/2 * log(pi) - (n-1)! * ...
# Equivalent: lambda_n = sum_rho [1 - (1-1/rho)^n]

# Li's criterion IS Weil positivity with a specific sequence of test functions:
# h_n(t) = 1 - ((1/2 - it)/(1/2 + it))^n  (for the Riemann xi function)
# These are the test functions that give lambda_n = W(h_n).

# Key question: can RP give lambda_n >= 0 for ALL n simultaneously?

print("\n--- Li coefficients from zeros ---")
# Compute lambda_n with increasing precision
N_zeros_li = 50
rho_list = [zetazero(k) for k in range(1, N_zeros_li + 1)]

li_coeffs = []
for n in range(1, 61):
    lam = mpf(0)
    for rho in rho_list:
        # Each zero rho contributes, plus its companion 1-conj(rho)
        val = 1 - power(1 - 1/rho, n)
        val_conj = 1 - power(1 - 1/(1 - conj(rho)), n)
        lam += re(val) + re(val_conj)
    li_coeffs.append(float(lam))
    if n <= 10 or n % 10 == 0:
        print(f"  lambda_{n:3d} = {float(lam):14.6f}  {'OK' if lam >= 0 else 'FAIL'}")

print(f"\n  All lambda_n (n=1..60) positive: {all(l >= 0 for l in li_coeffs)}")

# Li's test functions in the Weil formulation:
# h_n(t) corresponds to h(gamma) = 1 - ((1/2-i*gamma)/(1/2+i*gamma))^n
# The quantity (1/2-i*gamma)/(1/2+i*gamma) has |.| = 1, so it's a phase.
# Writing rho = 1/2 + i*gamma: 1/rho = 1/(1/2+i*gamma), and
# (1-1/rho) = (1/2+i*gamma-1)/(1/2+i*gamma) = (-1/2+i*gamma)/(1/2+i*gamma)
# = -(1/2-i*gamma)/(1/2+i*gamma)

# So (1-1/rho)^n = (-1)^n * e^{in*theta} where theta = -2*arctan(2*gamma)
# and lambda_n = sum_rho [1 - (-1)^n * e^{in*theta_rho}]

# The RP connection: these test functions are CHARACTERS of a rotation group.
# On S^1, the KK modes are e^{in*phi/R}. Under the exponential map,
# phi/R -> theta where theta = 2*arctan(2*gamma).
# So Li's test functions ARE KK modes (up to the map)!

print("\n--- Li test functions as KK modes ---")
print("  h_n corresponds to the n-th Fourier mode on S^1")
print("  under the Cayley transform s -> (s-1)/(s+1)")
print()
print("  For rho = 1/2 + i*gamma:")
print("    (1 - 1/rho)^n = (-1)^n * exp(i*n*theta_rho)")
print("    where theta_rho = -2*arctan(2*gamma)")
print()
print("  So lambda_n = sum_rho [1 - (-1)^n * e^{i*n*theta_rho}]")
print("  = Re[sum_rho (1 - e^{i*n*(theta_rho + pi)})]")
print("  = N_zeros - Re[sum_rho e^{i*n*theta'_rho}]")
print("  where theta'_rho = theta_rho + pi")

# Compute the angles theta_rho
print("\n  Angles theta_rho for first 10 zeros:")
thetas = []
for k, rho in enumerate(rho_list[:10]):
    g = float(rho.imag)
    theta = -2 * np.arctan(2 * g)
    theta_prime = theta + np.pi
    thetas.append(theta_prime)
    print(f"    rho_{k+1}: gamma = {g:10.6f}, theta' = {theta_prime:10.6f} ({theta_prime/np.pi:.4f}*pi)")

# The distribution of theta' values determines whether lambda_n >= 0 for all n.
# If the angles are "uniformly distributed" (equidistributed modulo 2pi),
# then the sum of e^{in*theta'} ~ 0 and lambda_n ~ N_zeros > 0.
# But if they concentrate, the sum can exceed N_zeros and lambda_n < 0.

print("\n  For lambda_n >= 0 for ALL n, we need:")
print("    |sum_rho e^{i*n*theta'_rho}| <= N_zeros  for all n")
print("  This is a condition on the DISTRIBUTION of the angles theta'_rho.")

# Compute the partial sums S_n = sum_{k=1}^{K} e^{i*n*theta'_k}
all_thetas = []
for rho in rho_list:
    g = float(rho.imag)
    theta_prime = -2 * np.arctan(2 * g) + np.pi
    all_thetas.append(theta_prime)

print(f"\n  Partial Fourier sums |S_n| for K={N_zeros_li} zeros:")
for n in [1, 2, 5, 10, 20, 50]:
    S_n = sum(np.exp(1j * n * th) for th in all_thetas)
    # Count both rho and conj: S_n_total = S_n + conj(S_n) for real lambda_n
    S_n_abs = abs(S_n)
    print(f"    |S_{n:3d}| = {S_n_abs:10.4f}  (vs N_zeros/2 = {N_zeros_li})")


# ======================================================================
# PART E: Can RP give ALL lambda_n >= 0 simultaneously?
# ======================================================================
print("\n" + "=" * 72)
print("PART E: RP and Simultaneous Li Positivity")
print("=" * 72)

# The question: does RP on S^1 imply lambda_n >= 0 for ALL n?
#
# RP says: <f, Theta f> >= 0 for all f supported on the positive half.
# Li says: lambda_n >= 0 for all n >= 1.
# Each lambda_n corresponds to a SPECIFIC test function h_n.
# Is h_n = f_n * f_n~ for some f_n?
#
# h_n(t) = 1 - ((1/2-it)/(1/2+it))^n
# h_n is NOT positive-definite for all n! Let's check.

print("\n--- Is Li's h_n positive-definite? ---")
# h_n is positive-definite iff h_hat_n >= 0.
# h_n(t) = 1 - e^{in*phi(t)} where phi(t) = 2*arctan(2t) + pi
# Fourier transform of h_n:
# h_hat_n(x) = delta(x) - FT[e^{in*phi(t)}](x)
# The second term is related to the Jacobi theta function of the Cayley transform.

# Actually, for Li's criterion, the test functions are NOT required to be
# positive-definite. Li's criterion is a DIFFERENT equivalence from Weil positivity.
# Weil: W(h) >= 0 for all h = f*f~ (pos-def h)
# Li: lambda_n >= 0 for all n >= 1 (specific h_n, not necessarily pos-def)

# Li proved his criterion is equivalent to RH by showing:
# lambda_n >= 0 for all n <=> all zeros on Re(s) = 1/2

# The connection to Weil: Li's lambda_n can be EXPRESSED as a Weil sum
# with a specific (non-positive-definite) test function. But the equivalence
# goes through a DIFFERENT argument (the power series of xi'/xi at s=1).

print("  Li's h_n(t) = 1 - ((1/2-it)/(1/2+it))^n")
print("  These are NOT positive-definite in general.")
print("  h_n is a finite sum of Fourier modes on the unit circle")
print("  (via the Cayley map), and NOT an autocorrelation.")
print()
print("  However, Li's equivalence RH <=> lambda_n >= 0 for all n")
print("  does NOT require h_n to be positive-definite.")
print("  It uses a DIFFERENT proof strategy (power series at s=1).")

# Can RP give lambda_n >= 0?
# RP gives: for any f in L^2(half-circle), <f, Theta f> >= 0.
# In the spectral domain, this means:
# sum_rho |f_hat(rho)|^2 >= 0 (trivially!)
# So RP gives SUM_rho |f_hat(rho)|^2 >= 0 — this is trivial.
# It does NOT give sum_rho h_n(rho) >= 0 for non-positive-definite h_n.

print("\n  RP gives: sum_rho |g(rho)|^2 >= 0 — trivially true.")
print("  Li needs: sum_rho h_n(rho) >= 0 — h_n is NOT of the form |g|^2.")
print()
print("  Therefore RP does NOT directly give Li's criterion.")
print("  The gap: RP controls positive-definite test functions,")
print("  but Li uses non-positive-definite test functions.")

# However, Li's criterion CAN be reformulated using positive-definite functions:
# Bombieri-Lagarias (1999) showed lambda_n >= 0 iff a certain Hermitian matrix
# is positive semidefinite. The matrix entries are:
# A_{j,k} = lambda_{j+k-1} for 1 <= j,k <= n
# (the Hankel matrix of Li coefficients)

print("\n--- Bombieri-Lagarias: Li ↔ Hankel positivity ---")
print("  RH <=> the Hankel matrix H_n = (lambda_{i+j-1})_{i,j=1}^n")
print("  is positive semidefinite for all n >= 1.")
print()
print("  This IS a positive-definiteness condition!")
print("  H_n >= 0 <=> x^T H_n x >= 0 for all x <=> sum_{i,j} x_i x_j lambda_{i+j-1} >= 0")
print("  <=> sum_rho |sum_k x_k (1-(1-1/rho)^k)|^2 >= 0 — trivially true!")
print()
print("  Wait — this means Hankel positivity IS trivially true?")
print("  Let's check numerically...")

# Build and check Hankel matrices
from numpy.linalg import eigvalsh

# We need lambda_n for n up to 2*N-1 where N is the Hankel matrix size
for N_hankel in [3, 5, 10, 15, 20, 30]:
    max_n = 2 * N_hankel - 1
    if max_n > len(li_coeffs):
        break
    H = np.zeros((N_hankel, N_hankel))
    for i in range(N_hankel):
        for j in range(N_hankel):
            idx = i + j  # lambda_{i+j+1} but our list is 0-indexed: li_coeffs[i+j] = lambda_{i+j+1}
            H[i, j] = li_coeffs[idx]
    eigs = eigvalsh(H)
    min_eig = eigs[0]
    print(f"  Hankel H_{N_hankel}: min eigenvalue = {min_eig:12.6f}  "
          f"{'PSD' if min_eig >= -1e-8 else 'NOT PSD'}")

# Now the key insight: the Hankel matrix H_n has entries
# H_{i,j} = lambda_{i+j-1} = sum_rho [1 - (1-1/rho)^{i+j-1}]
# For vector x: x^T H x = sum_rho sum_{i,j} x_i x_j [1 - (1-1/rho)^{i+j-1}]
# This is NOT trivially positive because the sum includes the "1" term.
# x^T H x = sum_rho [N*|x|^2 - |sum_i x_i (1-1/rho)^{i-1}|^2 + correction]
# The correction depends on whether |1-1/rho| < 1 (which is RH!).

print("\n  Insight: Hankel positivity is NOT trivially true!")
print("  x^T H_n x = sum_rho [sum_i x_i - sum_i x_i (1-1/rho)^i]^2")
print("  = sum_rho |sum_i x_i [1 - (1-1/rho)^i]|^2 >= 0")
print("  WAIT: this IS trivially >= 0 since it's a sum of |...|^2!")
print()
print("  BUT: this only works if all rho are used (with correct multiplicity).")
print("  The sum over rho converges only if the implicit series converges.")
print("  For |1-1/rho| >= 1 (i.e., rho OFF the critical line),")
print("  the term (1-1/rho)^i grows with i, and the partial sums diverge.")
print("  So lambda_n >= 0 for ALL n requires |1-1/rho| < 1 for ALL rho,")
print("  which is equivalent to Re(rho) > 0 (weaker than RH but same direction).")

# Actually, Li's proof shows:
# If ALL rho are on Re(s) = 1/2, then |1-1/rho| = 1 (not < 1, = 1).
# For rho = 1/2 + i*gamma: |1 - 1/rho| = |1 - 2/(1+2i*gamma)| = |(2i*gamma-1)/(1+2i*gamma)| = 1.
# So |1-1/rho| = 1 exactly on the critical line.

# The convergence of sum_rho (1-1/rho)^n depends on the imaginary parts gamma_rho.
# On the critical line: (1-1/rho)^n = e^{in*theta_rho}, a pure phase.
# Off the critical line: |1-1/rho| != 1, so the terms grow or decay.

print("\n  Critical observation:")
print("    On critical line: |1-1/rho| = 1 (pure phase)")
print("    Off critical line: |1-1/rho| != 1")
print()
for rho in rho_list[:5]:
    val = abs(1 - 1/rho)
    print(f"    rho = {rho}: |1-1/rho| = {float(val):.10f}")


# ======================================================================
# PART F: Multiplicative Reformulation of RP
# ======================================================================
print("\n" + "=" * 72)
print("PART F: Is There a MULTIPLICATIVE RP?")
print("=" * 72)

# P5m says: theta is the bridge. theta lives in both worlds.
# theta(t) = sum_{n in Z} e^{-pi*n^2*t} > 0 for all t > 0 (from RP).
# The functional equation theta(1/t) = sqrt(t) * theta(t) = Poisson summation.
# xi(s) = Mellin(theta - 1) connects to zeta.

# The MULTIPLICATIVE structure is in the Euler product:
# zeta(s) = prod_p (1-p^{-s})^{-1}
# Can we write an RP condition using the Euler product directly?

# Idea: write zeta(s) = exp(sum_p sum_m p^{-ms}/m) for Re(s) > 1.
# The log: log zeta(s) = sum_p sum_m p^{-ms}/m = sum_p -log(1-p^{-s})
# Each p contributes independently to log zeta.
# "RP" for log zeta would be: each log-factor is "positive."
# -log(1-p^{-s}) = sum_m p^{-ms}/m > 0 for Re(s) > 0 and real s. Yes.

# But this is trivial and doesn't give RH.

# A DIFFERENT multiplicative RP:
# Consider the von Mangoldt function Lambda(n):
# -zeta'/zeta(s) = sum_n Lambda(n) n^{-s}
# Lambda(p^k) = log(p), Lambda(n) = 0 if n is not a prime power.
# Lambda >= 0 always! This is a positivity condition.

# The explicit formula: sum_rho x^rho / rho = x - sum_{n<=x} Lambda(n) - ...
# The prime sum side has ALL POSITIVE terms (Lambda >= 0).
# Does this positivity constrain the zeros?

print("\n--- Multiplicative Positivity from Lambda ---")
print("  -zeta'/zeta(s) = sum_n Lambda(n) n^{-s}")
print("  Lambda(p^k) = log(p) >= 0 always")
print("  This is trivial positivity — does not constrain zero locations.")

# The Selberg class: L-functions with an Euler product + functional equation
# + Ramanujan bound + polynomial Euler factors.
# For the Selberg class, Conrey-Ghosh conjecture: RH holds.
# The Euler product + FE + Ramanujan is a MULTIPLICATIVE positivity condition.

print("\n--- Selberg Class as Multiplicative Positivity ---")
print("  An L-function in the Selberg class has:")
print("  1. Dirichlet series sum a_n n^{-s} convergent for Re(s) > 1")
print("  2. Euler product prod_p F_p(p^{-s})^{-1}")
print("  3. Functional equation relating L(s) and L_bar(1-s)")
print("  4. Ramanujan bound |a_p| <= C*p^epsilon for all epsilon > 0")
print("  5. Polynomial Euler factors (degree d)")
print()
print("  The Ramanujan bound IS a positivity condition:")
print("  |alpha_{j,p}| <= 1 for all Satake parameters alpha_{j,p}")
print("  = |eigenvalue of Frobenius| <= 1")
print("  = compactness of the Frobenius conjugacy class")
print()
print("  In QG5D: Identity 11 says |Tr(U(1))| <= 2 IS Ramanujan.")
print("  This is the e-circle holonomy compactness = Frobenius compactness.")

# The deepest multiplicative positivity: the Weil conjectures (over F_q)
# Proved by Deligne. The positivity comes from the Hodge index theorem
# on the algebraic curve. Over Q, there is no curve — this is the gap.

print("\n--- The Hodge Index Theorem Analogy ---")
print("  Over F_q: RH for curves follows from:")
print("    Hodge index theorem on the surface C x C")
print("    → intersection pairing is positive-definite")
print("    → Weil positivity")
print("    → zeros on Re(s) = 1/2")
print()
print("  Over Q: NO algebraic curve whose Frobenius eigenvalues = zeta zeros.")
print("  The 'missing geometry' is the central problem.")
print("  Connes-Consani: the 'curve' is Spec(Z) + archimedean completion")
print("  = the arithmetic site. Its cohomology should give the positivity.")

# Can QG5D supply this geometry?
# The e-circle S^1 is the archimedean place.
# The Euler product gives the p-adic places.
# The adele ring A_Q = R x prod' Q_p unifies them.
# The QG5D gauge theory on M^4 x S^1 gives the archimedean RP.
# What about the p-adic RP?

print("\n--- P-adic RP ---")
print("  At each prime p, there is a local positivity condition:")
print("    <f_p, Theta_p f_p>_{Q_p} >= 0")
print("  where Theta_p: x -> x^{-1} on Q_p*.")
print()
print("  This IS local Weil positivity at the prime p (Connes 2020).")
print("  The QG5D framework does NOT provide this natively —")
print("  the gauge theory on S^1 gives ONLY the archimedean factor.")
print()
print("  To get ALL places, one would need gauge theory on the ADELIC circle:")
print("    A_Q^1 / Q* = 'adelic S^1'")
print("  This is Connes' adele class space, NOT a smooth manifold.")


# ======================================================================
# PART G: The theta function bridge (P5m)
# ======================================================================
print("\n" + "=" * 72)
print("PART G: Theta Function as Bridge (P5m)")
print("=" * 72)

# theta(t) = sum_{n in Z} exp(-pi*n^2*t) > 0 for t > 0 (from RP on S^1)
# theta(1/t) = sqrt(t) * theta(t) (Poisson summation)
# xi(s) = integral_0^infty [theta(t) - 1]/2 * t^{s/2} dt/t
#        = integral_1^infty [theta(t) - 1]/2 * [t^{s/2} + t^{(1-s)/2}] dt/t

# The integrand [theta(t)-1]/2 = sum_{n=1}^infty exp(-pi*n^2*t) > 0 for t > 0.
# So xi(s) is the Mellin transform of a POSITIVE function.

# Key question: does Mellin(positive + functional equation) => zeros on line?

# This is the de Bruijn / Newman / Polya direction.
# Define f_lambda(t) = (theta-1)/2 with deformation parameter lambda:
#   xi_lambda(s) = Mellin[f_lambda](s)
# where f_lambda satisfies the heat equation in lambda.

# Newman (1976): there exists Lambda_0 such that xi_lambda has all zeros
# on the line iff lambda >= Lambda_0.
# Rodgers-Tao (2020): Lambda_0 >= 0.
# RH <=> Lambda_0 = 0 <=> xi_0 = xi has all zeros on the line.

# The QG5D input: RP guarantees theta > 0 (the positivity of the partition function).
# This gives Lambda_0 <= some bound (because the partition function IS positive).
# But Lambda_0 = 0 requires EXACT positivity at lambda = 0, which RP gives.

# So: RP says theta > 0 at lambda = 0. The heat equation preserves positivity
# for lambda > 0 but may lose it for lambda < 0. RH asks: is lambda = 0
# EXACTLY the boundary? This is the de Bruijn-Newman constant question.

print("  RP gives: theta(t) > 0 for all t > 0")
print("  Poisson gives: theta(1/t) = sqrt(t) * theta(t)")
print("  Mellin transform: xi(s) = Mellin[(theta-1)/2]")
print()
print("  de Bruijn-Newman: Lambda_0 = inf{lambda : xi_lambda has all zeros on line}")
print("  RH <=> Lambda_0 = 0")
print("  Rodgers-Tao (2020): Lambda_0 >= 0")
print()
print("  RP contribution: theta > 0 is the INPUT for the de Bruijn-Newman setup.")
print("  But theta > 0 is just the STARTING POINT — it defines xi_0 = xi.")
print("  The question Lambda_0 = 0 vs Lambda_0 > 0 is about the FINER structure")
print("  of theta (its Fourier coefficients, not just its sign).")
print()
print("  CONCLUSION: RP gives theta > 0 (necessary). But theta > 0 does NOT")
print("  imply Lambda_0 = 0. Many positive functions have Lambda_0 > 0.")
print("  RP is necessary but not sufficient for RH via the theta/Mellin route.")

# Numerical check: compute theta and verify positivity
print("\n--- Numerical theta values ---")
for t_val in [0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0]:
    theta_val = 0.0
    for n in range(-100, 101):
        theta_val += float(exp(-pi * mpf(n)**2 * mpf(t_val)))
    print(f"  theta({t_val:6.2f}) = {theta_val:.10f}  > 0: {theta_val > 0}")


# ======================================================================
# PART H: Summary and Honest Assessment
# ======================================================================
print("\n" + "=" * 72)
print("PART H: Summary Assessment")
print("=" * 72)

print("""
  QUESTION: Does RP supply ALL test functions for Guinand-Weil positivity?

  ANSWER: NO. RP supplies the ARCHIMEDEAN factor only.

  Detailed breakdown:

  1. Test functions for Weil positivity:
     - h = f * f~ (positive-definite, autocorrelations)
     - RP generates |g|^2 which IS positive-definite
     - So RP generates the RIGHT CLASS of test functions
     - But only at the ARCHIMEDEAN place (v = infinity)

  2. RP and the full Weil positivity:
     - Archimedean Weil positivity: YES (Identity 2, 95%)
     - p-adic Weil positivity: NOT from RP (RP is archimedean)
     - Global Weil positivity (all places + Q*-descent): NO
     - The descent IS the Riemann Hypothesis (Connes 1999)

  3. Nyman-Beurling:
     - NB functions embed into the RP Hilbert space (via measure change)
     - But NB density condition uses a DIFFERENT norm
     - RP does not imply NB density

  4. Li's criterion:
     - Li's h_n are NOT positive-definite
     - RP controls positive-definite functions only
     - The Hankel matrix formulation IS a positivity condition
     - But the convergence requires |1-1/rho| = 1, which IS RH

  5. Multiplicative RP:
     - No smooth gauge theory gives discrete arithmetic (the 21 walls)
     - The theta bridge gives RP → theta > 0, but this is necessary, not sufficient
     - The Ramanujan bound (|alpha_p| <= 1) IS a multiplicative positivity
       but it's an INPUT to the Langlands program, not a consequence of RP

  CONFIDENCE: 5% that RP alone closes the chain to full Weil positivity.
  The gap is the Q*-descent = the Riemann Hypothesis itself.
""")

print("=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
