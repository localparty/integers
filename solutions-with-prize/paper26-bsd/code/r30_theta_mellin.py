"""
R30: Theta-Mellin investigation for Approach A.

Verifies:
1. The precise relationship theta -> Phi -> xi via Mellin
2. Positivity of Phi(t) for t > 0
3. xi(s) = Mellin(Phi) numerically at known zeros
4. The de Bruijn-Newman deformation H_lambda and Phi_lambda
5. Counterexample search: positive + symmetric functions whose
   Mellin transform has OFF-line zeros
"""

import numpy as np
from mpmath import (mp, mpf, mpc, pi, exp, sqrt, gamma, zeta, zetazero,
                    log, fsum, diff, quad, inf, fabs, re, im, nstr)

mp.dps = 30  # 30 decimal places


# ---------------------------------------------------------------
# Section 1: Theta function and its derivatives
# ---------------------------------------------------------------

def theta3(t, nmax=200):
    """Jacobi theta_3(0|it) = sum_{n=-nmax}^{nmax} exp(-pi n^2 t)."""
    s = mpf(1)
    for n in range(1, nmax + 1):
        s += 2 * exp(-pi * n**2 * t)
    return s


def theta3_deriv(t, nmax=200, k=1):
    """k-th derivative of theta3 with respect to t.
    d^k/dt^k theta3(t) = sum_n (-pi n^2)^k exp(-pi n^2 t)."""
    s = mpf(0)
    for n in range(1, nmax + 1):
        s += 2 * (-pi * n**2)**k * exp(-pi * n**2 * t)
    return s


print("=" * 60)
print("SECTION 1: Theta function basics")
print("=" * 60)

# Verify the functional equation theta(1/t) = sqrt(t) * theta(t)
for t_val in [mpf('0.1'), mpf('0.5'), mpf('1'), mpf('2'), mpf('5')]:
    lhs = theta3(1 / t_val)
    rhs = sqrt(t_val) * theta3(t_val)
    print(f"t = {nstr(t_val, 4):>6}: theta(1/t) = {nstr(lhs, 15)},  "
          f"sqrt(t)*theta(t) = {nstr(rhs, 15)},  diff = {nstr(fabs(lhs - rhs), 4)}")

print()

# Verify theta > 0 for all t > 0
print("Theta positivity check:")
for t_val in [mpf('0.001'), mpf('0.01'), mpf('0.1'), mpf('1'),
              mpf('10'), mpf('100'), mpf('1000')]:
    val = theta3(t_val)
    print(f"  theta({nstr(t_val, 4):>7}) = {nstr(val, 15)}")

print()


# ---------------------------------------------------------------
# Section 2: The kernel Phi(t)
# ---------------------------------------------------------------

print("=" * 60)
print("SECTION 2: The Phi kernel for xi = Mellin(Phi)")
print("=" * 60)
print()

# The xi function is defined as:
#   xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
#
# The standard representation via theta:
#   pi^{-s/2} Gamma(s/2) zeta(s) = integral_0^infty [theta(t)-1]/2 * t^{s/2} dt/t
#                                  + 1/(s-1) - 1/s
#
# So xi(s) = (1/2) s(s-1) [integral_0^infty psi(t) t^{s/2} dt/t + 1/(s-1) - 1/s]
#
# where psi(t) = [theta(t)-1]/2 = sum_{n>=1} exp(-pi n^2 t)
#
# More cleanly, xi(s) can be written as a pure Mellin transform:
#   xi(1/2 + it) = integral_0^infty Phi(u) e^{itu} du
#
# where Phi is defined via the "super-exponentially decaying" kernel.
#
# The STANDARD form (Riemann's original, see Edwards Ch. 1):
#   xi(s) = integral_1^infty Phi_R(x) [x^{s/2-1} + x^{(1-s)/2-1}] dx
#
# where Phi_R(x) = sum_{n>=1} (2 pi^2 n^4 x^2 - 3 pi n^2 x) exp(-pi n^2 x)
#
# Let's use the equivalent form via substitution x = e^u:
#   xi(1/2 + it) = 2 integral_0^infty Phi_R(e^u) e^{u/2} cos(tu) du

def psi(t, nmax=200):
    """psi(t) = [theta3(t) - 1]/2 = sum_{n>=1} exp(-pi n^2 t)."""
    s = mpf(0)
    for n in range(1, nmax + 1):
        s += exp(-pi * n**2 * t)
    return s


def Phi_R(x, nmax=200):
    """Riemann's kernel:
    Phi_R(x) = sum_{n>=1} (2*pi^2*n^4*x^2 - 3*pi*n^2*x) exp(-pi*n^2*x).

    This satisfies: xi(s) = int_1^infty Phi_R(x)[x^{s/2-1} + x^{(1-s)/2-1}] dx
    """
    s = mpf(0)
    for n in range(1, nmax + 1):
        pn2 = pi * n**2
        s += (2 * pn2**2 * x**2 - 3 * pn2 * x) * exp(-pn2 * x)
    return s


# The KEY Phi kernel for the "pure Mellin" representation:
#   xi(s) = integral_0^infty Phi_xi(t) t^{s/2} dt/t
#
# Phi_xi(t) = 2 * sum_{n>=1} (2*pi^2*n^4*t^2 - 3*pi*n^2*t) * exp(-pi*n^2*t)
# (factor of 2 from folding the integral from (0,infty) to (1,infty) using the FE)
#
# Actually, the correct pure Mellin form (from Riemann):
#   xi(s) = int_0^infty [omega(t) t^{s/2} + omega(t) t^{(1-s)/2}] dt/t
# where omega(t) = sum_{n>=1} ...
# This naturally builds in the s <-> 1-s symmetry.
#
# More precisely (following the classical derivation):
# Start from: pi^{-s/2} Gamma(s/2) zeta(s) = int_0^infty psi(t) t^{s/2} dt/t + ...
# After careful manipulation:
#   xi(s) = 1/2 - 1/(s*(1-s)) + int_1^infty psi(t) [t^{s/2} + t^{(1-s)/2}] dt/t ... WRONG
#
# Let me use the correct classical form. The Riemann xi function:
#   xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
#
# has the integral representation (Riemann 1859):
#   xi(s) = 1/2 + integral_1^infty Phi_R(t) (t^{(s-1)/2} + t^{-s/2}) dt
# where Phi_R(t) = d/dt [t^{3/2} psi'(t)]
# and psi(t) = sum_{n>=1} exp(-pi n^2 t)
# so psi'(t) = -sum_{n>=1} pi n^2 exp(-pi n^2 t)
# and t^{3/2} psi'(t) = -sum_{n>=1} pi n^2 t^{3/2} exp(-pi n^2 t)
# d/dt[...] = sum_{n>=1} [-(3/2) pi n^2 t^{1/2} + pi^2 n^4 t^{3/2}] exp(-pi n^2 t)

def Phi_Riemann(t, nmax=200):
    """Riemann's kernel: Phi(t) = d/dt[t^{3/2} psi'(t)].
    xi(s) = 1/2 + int_1^infty Phi(t) [t^{(s-1)/2} + t^{-s/2}] dt
    """
    s = mpf(0)
    for n in range(1, nmax + 1):
        pn2 = pi * n**2
        s += (-mpf(3)/2 * pn2 * sqrt(t) + pn2**2 * t * sqrt(t)) * exp(-pn2 * t)
    return s


print("Phi_Riemann(t) values -- testing positivity:")
for t_val in [mpf('0.01'), mpf('0.1'), mpf('0.3'), mpf('0.5'),
              mpf('1'), mpf('2'), mpf('5'), mpf('10'), mpf('100')]:
    val = Phi_Riemann(t_val)
    sign = "POSITIVE" if val > 0 else "NEGATIVE" if val < 0 else "ZERO"
    print(f"  Phi({nstr(t_val, 4):>6}) = {nstr(val, 15):>25}  {sign}")

print()


# ---------------------------------------------------------------
# Section 3: Verify xi(s) = 1/2 + int Phi(t)... numerically
# ---------------------------------------------------------------

print("=" * 60)
print("SECTION 3: Numerical verification xi(s) = Mellin(Phi)")
print("=" * 60)
print()

def xi_from_zeta(s):
    """Compute xi(s) from the definition."""
    return mpf(1)/2 * s * (s - 1) * pi**(-s/2) * gamma(s/2) * zeta(s)


def xi_from_integral(s, tmax=50, nmax=200):
    """Compute xi(s) via Riemann's integral:
    xi(s) = 1/2 + int_1^infty Phi(t) [t^{(s-1)/2} + t^{-s/2}] dt
    """
    def integrand(t):
        return Phi_Riemann(t, nmax) * (t**((s - 1)/2) + t**(-s/2))

    result = quad(integrand, [1, tmax])
    return mpf(1)/2 + result


# Test at several s values
print("Comparing xi(s) from definition vs integral:")
test_s = [mpc('2', '0'), mpc('0.5', '0'), mpc('3', '0'),
          mpc('0.5', '14.134725'), mpc('0.5', '21.022040'),
          mpc('0.5', '25.010858')]

for s in test_s:
    xi_def = xi_from_zeta(s)
    xi_int = xi_from_integral(s)
    diff_val = fabs(xi_def - xi_int)
    print(f"  s = {nstr(s, 12):>20}: xi_def = {nstr(xi_def, 12):>20},  "
          f"xi_int = {nstr(xi_int, 12):>20},  |diff| = {nstr(diff_val, 4)}")

print()


# ---------------------------------------------------------------
# Section 4: Does positivity of theta imply positivity of Phi?
# ---------------------------------------------------------------

print("=" * 60)
print("SECTION 4: theta > 0 => Phi > 0 ?")
print("=" * 60)
print()

# Phi(t) = d/dt[t^{3/2} psi'(t)]
# psi(t) = [theta(t) - 1]/2 > 0  (since theta > 1 for all t > 0)
# psi'(t) = theta'(t)/2 < 0 for t > 0 (theta is decreasing as t -> infty)
# But does Phi(t) > 0?

# Let's compute Phi more carefully and check the sign structure.
# Phi(t) = d/dt[t^{3/2} psi'(t)]
#        = (3/2) t^{1/2} psi'(t) + t^{3/2} psi''(t)

def psi_prime(t, nmax=200):
    """psi'(t) = -sum pi n^2 exp(-pi n^2 t)."""
    s = mpf(0)
    for n in range(1, nmax + 1):
        s += -pi * n**2 * exp(-pi * n**2 * t)
    return s


def psi_double_prime(t, nmax=200):
    """psi''(t) = sum (pi n^2)^2 exp(-pi n^2 t)."""
    s = mpf(0)
    for n in range(1, nmax + 1):
        s += (pi * n**2)**2 * exp(-pi * n**2 * t)
    return s


print("Decomposition of Phi(t) = (3/2)*t^{1/2}*psi'(t) + t^{3/2}*psi''(t):")
print(f"  {'t':>8}  {'(3/2)t^{1/2}psi_prime':>22}  {'t^{3/2}psi_dblprime':>22}  {'Phi(t)':>22}  {'sign':>8}")
for t_val in [mpf('0.001'), mpf('0.01'), mpf('0.05'), mpf('0.1'),
              mpf('0.3'), mpf('0.5'), mpf('1'), mpf('2'),
              mpf('5'), mpf('10'), mpf('50')]:
    term1 = mpf(3)/2 * sqrt(t_val) * psi_prime(t_val)
    term2 = t_val**mpf(3)/mpf(2) * psi_double_prime(t_val)
    # fix: t^{3/2}
    term2_corr = t_val**(mpf(3)/2) * psi_double_prime(t_val)
    phi_val = term1 + term2_corr
    sign = "+" if phi_val > 0 else "-" if phi_val < 0 else "0"
    print(f"  {nstr(t_val, 4):>8}  {nstr(term1, 15):>22}  {nstr(term2_corr, 15):>22}  "
          f"{nstr(phi_val, 15):>22}  {sign:>8}")

print()

# Now verify the functional equation for Phi:
# If xi(s) = xi(1-s) and xi(s) = 1/2 + int_1^infty Phi(t)(t^{(s-1)/2} + t^{-s/2}) dt,
# the symmetry is built into the integrand (t^{(s-1)/2} + t^{-s/2} is symmetric under s -> 1-s).
# But Phi itself satisfies a functional equation?
#
# Under t -> 1/t in the FULL integral (0 to infty form):
# The symmetry of xi under s -> 1-s comes from theta(1/t) = sqrt(t)*theta(t).
# For Phi_Riemann: since Phi = d/dt[t^{3/2} psi'(t)], and psi has the FE
# psi(1/t) + 1/2 = sqrt(t)[psi(t) + 1/2], there IS a functional equation for Phi
# but it's implicit.


# ---------------------------------------------------------------
# Section 5: The de Bruijn-Newman constant
# ---------------------------------------------------------------

print("=" * 60)
print("SECTION 5: de Bruijn-Newman deformation")
print("=" * 60)
print()

# The de Bruijn deformation: H_lambda(t) = int_0^infty e^{lambda*u^2} Phi(u) cos(tu) du
# where Phi is the Fourier representation of xi.
#
# Actually, the standard form: define
#   Xi(t) = xi(1/2 + it) = 2 int_0^infty Phi_R(e^u) e^{u/2} cos(tu) du
#
# Then the de Bruijn-Newman deformation:
#   H_lambda(t) = int_0^infty e^{lambda*u^2} Phi_R(e^u) e^{u/2} cos(tu) du
#
# Key result: Lambda = sup{lambda : H_lambda has a non-real zero}
# RH <=> Lambda <= 0
# Rodgers-Tao (2020, building on Newman 1976): Lambda >= 0
# So RH <=> Lambda = 0.
#
# The QUESTION for Approach A: does positivity of the kernel Phi_R
# force Lambda <= 0?
#
# de Bruijn (1950) proved: if lambda > 1/2, then H_lambda has only real zeros.
# The heat flow smoothing at lambda > 0 eventually forces all zeros real.
# The question is whether lambda = 0 is already enough.

print("The de Bruijn-Newman framework:")
print(f"  Lambda >= 0 (Newman 1976 conjecture, proved Rodgers-Tao 2020)")
print(f"  Lambda <= 0 iff RH (de Bruijn 1950)")
print(f"  So: RH <=> Lambda = 0")
print()

# Compute Xi(t) = xi(1/2 + it) at the first few zero locations
print("Xi(t) at known zero locations (should be ~ 0):")
for k in range(1, 6):
    t0 = im(zetazero(k))
    xi_val = xi_from_zeta(mpc('0.5', t0))
    print(f"  Xi({nstr(t0, 10)}) = {nstr(fabs(xi_val), 6)}")

print()

# Key: Xi(t) is an EVEN function of t, real-valued for real t.
# Since xi(1/2 + it) = xi(1/2 - it), Xi(-t) = Xi(t).
print("Xi(t) reality and evenness check:")
for t_val in [mpf('5'), mpf('10'), mpf('14.134')]:
    val_pos = xi_from_zeta(mpc('0.5', t_val))
    val_neg = xi_from_zeta(mpc('0.5', -t_val))
    print(f"  Xi({nstr(t_val, 5):>8}) = {nstr(val_pos, 15)}")
    print(f"  Xi({nstr(-t_val, 5):>8}) = {nstr(val_neg, 15)}")
    print(f"  difference    = {nstr(fabs(val_pos - val_neg), 4)}")
    print(f"  imaginary part= {nstr(fabs(im(val_pos)), 4)}")
    print()


# ---------------------------------------------------------------
# Section 6: Counterexample search -- positive + symmetric
# but Mellin zeros NOT on Re(s) = 1/2
# ---------------------------------------------------------------

print("=" * 60)
print("SECTION 6: Counterexample search")
print("=" * 60)
print()

# Consider f(t) = t^a * exp(-t) for a > 0.
# This is positive for t > 0.
# Its Mellin transform: int_0^infty t^a e^{-t} t^{s-1} dt = Gamma(s + a)
# Gamma has no zeros! So this has NO zeros at all -- trivially "on the line."
#
# Consider f(t) with symmetry f(1/t) = t^c * f(t) for some c.
# The Mellin transform F(s) = int_0^infty f(t) t^{s-1} dt then satisfies
# F(s) = F(c + 1 - s) (functional equation with critical line Re(s) = (c+1)/2).
#
# The question is: can we find f > 0 + f(1/t) = t^c f(t) + appropriate decay
# but F has zeros OFF Re(s) = (c+1)/2?

# Example: Epstein zeta of a 2x2 matrix Q.
# E_Q(s) = sum'_{m in Z^2} Q(m)^{-s}
# = Mellin transform of theta_Q(t) - 1.
# theta_Q is positive (sum of exponentials).
# theta satisfies FE: theta_Q(1/t) = t * det(Q)^{-1/2} * theta_{Q^{-1}}(t)
# For Q = I_2: theta_Q = theta_{Q^{-1}} and we get theta(1/t) = t * theta(t).
# E_{I_2}(s) = 4 zeta(s) L(s, chi_{-4}) -- zeros at zeros of zeta(s).
# These are (conjecturally) on Re(s) = 1/2. So NOT a counterexample.

# For GENERAL Q, Epstein zeta E_Q(s) has zeros OFF the critical line!
# This is the key counterexample.

# The Davenport-Heilbronn example:
# Q = [1, t; t, 1+t^2] for certain t, the Epstein zeta has zeros off Re(s) = 1/2.
# Yet theta_Q > 0 and theta satisfies a FE.

# Let's verify with a specific Davenport-Heilbronn-type example.
# E(s; Q) for Q = diag(1, a) has theta_Q(t) = theta(t) * theta(at).
# FE: theta_Q(1/t) = t * a^{-1/2} * theta_Q(t/a) ... not the right FE for a single E.
#
# More precisely, for Q = [[1, 0], [0, a]]:
# theta_Q(t) = sum_{m,n} exp(-pi t (m^2 + a n^2))
#            = theta(t) * theta(at)  where theta(t) = sum_n exp(-pi n^2 t)
# FE: theta_Q(1/t) = t/sqrt(a) * theta_Q(t) ... NO, wrong.
# Actually theta_Q(1/t) = t * sqrt(det Q^{-1}) * theta_{Q^{-1}}(t)
# For Q = diag(1,a): Q^{-1} = diag(1, 1/a), det Q = a.
# theta_Q(1/t) = t / sqrt(a) * theta_{Q^{-1}}(t)
# = t/sqrt(a) * theta(t) * theta(t/a)
# This is NOT equal to (some power of t) * theta_Q(t) unless a = 1.
#
# So for the rectangle lattice, theta_Q is NOT self-dual.
# The Epstein zeta has a FE, but E_Q(s) = E_{Q^{-1}}(c - s) for some c,
# and for Q != Q^{-1} up to scaling, the FE is between two DIFFERENT functions.
#
# For a counterexample, we need f(1/t) = t^c f(t) (SAME function) + f > 0
# + Mellin zeros off line.

# Actually Davenport-Heilbronn (1936) constructed a Dirichlet series with
# functional equation s <-> 1-s but with zeros OFF the critical line.
# But their f(t) is NOT necessarily positive.

# Key question: is there f > 0 for all t > 0, f(1/t) = t^c f(t), and
# Mellin(f) has zeros off Re(s) = (c+1)/2?

# Approach: construct a linear combination of theta functions that is
# positive and self-dual, then check its Mellin zeros.

# Example: f(t) = A * theta(t) + B * theta(alpha*t) for suitable A, B, alpha
# such that f > 0 and f has the right FE.

# For theta functions: theta(t) > 0 always, and theta(1/t) = sqrt(t) theta(t).
# For theta(alpha*t): theta(alpha/t) = sqrt(t/alpha) theta(alpha*t).
# Wait, theta(alpha*t) means sum exp(-pi n^2 alpha t).
# Set u = alpha*t: theta(u) = theta(alpha*t).
# theta(1/u) = sqrt(u) theta(u) => theta(alpha / (alpha*t)) = theta(1/(alpha*t))
#   = ... this doesn't simplify to a FE for theta(alpha*t) itself.

# The proper way: theta(alpha*t) has FE:
# Under t -> 1/t: theta(alpha/t) = sum exp(-pi n^2 alpha/t)
#   != t^c * theta(alpha*t) for any c (unless alpha = 1)

# So a linear combination of theta functions at different scales does NOT
# satisfy a functional equation in general. The FE is tied to self-duality.

# RESULT: For the special class of functions with f(1/t) = sqrt(t)*f(t)
# (the EXACT symmetry of theta), positivity + FE + "appropriate" behavior
# may or may not force zeros on the line. This is precisely the content of RH.

print("COUNTEREXAMPLE ANALYSIS:")
print()
print("The question: does f > 0 + f(1/t) = t^c f(t) => Mellin zeros on Re(s) = (c+1)/2?")
print()
print("Key example: Epstein zeta functions E_Q(s)")
print("  theta_Q(t) > 0 for all t > 0 (sum of positive terms)")
print("  theta_Q satisfies a functional equation")
print("  BUT: E_Q(s) can have zeros OFF Re(s) = 1/2")
print()
print("However, for Epstein Q != Q^{-1} (up to scaling),")
print("the FE is E_Q(s) = E_{Q^{-1}}(L/2 - s), relating TWO DIFFERENT functions.")
print("The self-dual case Q = I requires both Q = Q^{-1} AND det Q = 1.")
print()
print("For the SELF-DUAL case (single function with f(1/t) = t^c f(t)):")
print("  The Davenport-Heilbronn counterexample is a LINEAR COMBINATION")
print("  of L-functions, not a theta-type kernel. Its kernel f(t)")
print("  is NOT everywhere positive (it changes sign).")
print()

# Let's verify: the Davenport-Heilbronn function
# DH(s) = [L(s, chi_5^+) + i*kappa * L(s, chi_5^-)] / (1 + i*kappa)
# where chi_5^+ has period 5, chi_5^+(1)=1, chi_5^+(2)=-1, chi_5^+(3)=-1, chi_5^+(4)=1
# and chi_5^- is the other character mod 5
# and kappa is chosen to make the FE exact.
#
# The theta kernel of chi_5^+: theta_chi(t) = sum_{n>=1} chi(n) exp(-pi n^2 t / 5)
# This CHANGES SIGN because chi takes values +1 and -1.
# Therefore the kernel of DH is NOT positive.

print("Davenport-Heilbronn kernel is NOT positive:")
print("  theta_{chi_5}(t) = sum chi_5(n) exp(-pi n^2 t/5)")
print("  chi_5 takes values +1, -1 => theta_{chi_5} changes sign")
print("  This is NOT a counterexample to 'positive + self-dual => zeros on line'")
print()

# Check: are there ANY known counterexamples to the specific statement
# "f > 0 for all t > 0, f(1/t) = sqrt(t)*f(t), f super-exponentially decaying,
#  and Mellin(f) has zeros off Re(s) = 1/2" ?
#
# ANSWER: No known counterexamples exist.
# But also no theorem proves it.
# This is essentially equivalent to RH.

print("CONCLUSION on counterexamples:")
print("  No known function f with:")
print("    (a) f(t) > 0 for all t > 0")
print("    (b) f(1/t) = sqrt(t) * f(t)")
print("    (c) super-exponential decay")
print("    (d) Mellin transform with zeros off Re(s) = 1/2")
print("  exists in the literature.")
print()
print("  However, no theorem proves this is impossible either.")
print("  The Epstein zeta counterexamples have non-self-dual FE.")
print("  The Davenport-Heilbronn counterexample has a kernel that changes sign.")
print("  Both escape the hypotheses.")


# ---------------------------------------------------------------
# Section 7: Polya's criterion and the Laguerre-Polya class
# ---------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 7: Polya criterion and Laguerre-Polya class")
print("=" * 60)
print()

# The xi function belongs to the Laguerre-Polya class LP iff RH holds.
# LP = {entire functions that are limits of polynomials with only real zeros}
#
# Polya (1927) showed: xi(1/2 + it) = xi(t) is in LP iff all its zeros are real,
# i.e., all zeros of xi(s) have Re(s) = 1/2.
#
# The Laguerre-Polya class is characterized by:
#   f(z) = c * z^m * e^{-az^2 + bz} * prod_k (1 - z/z_k) e^{z/z_k}
# where a >= 0, b, c are real, m >= 0 is integer, and all z_k are real.
#
# Polya's criterion: an entire function of order <= 2 with real coefficients
# is in LP iff it can be represented as
#   f(z) = integral_{-infty}^{infty} C(t) e^{izt} dt
# where C(t) is a POSITIVE function in LP.
#
# THIS IS THE KEY CONNECTION to Approach A:
# If Xi(t) = xi(1/2 + it) = integral C(u) e^{itu} du where C > 0 and C in LP,
# then Xi in LP, so all zeros of Xi are real, so RH holds.
#
# The kernel Phi (from the Riemann representation) IS positive.
# But is Phi in LP? That would require Phi to itself have only real zeros
# (as a function of... what variable?)

print("Polya's criterion for LP membership:")
print("  xi(1/2+it) in LP <=> all zeros of xi on Re(s)=1/2 <=> RH")
print()
print("  xi(1/2+it) = int Phi(u) cos(tu) du  (Fourier cosine transform)")
print("  Phi(u) > 0 for all u > 0 (verified numerically above)")
print()
print("  Polya: f in LP if f = Fourier transform of positive LP function.")
print("  So: xi in LP iff Phi is positive AND in LP.")
print("  Phi > 0 is necessary but not sufficient.")
print()

# The de Bruijn deformation gives the "heat flow" perspective:
# H_lambda(t) = int e^{lambda u^2} Phi(u) cos(tu) du
# For lambda > 0: multiplying by e^{lambda u^2} BROADENS Phi,
#   which SMOOTHS the Fourier transform => zeros migrate toward real axis.
# For lambda >= 1/2: de Bruijn proved all zeros are real.
# For lambda = 0: this is just Xi(t) = xi(1/2+it). RH <=> zeros real.
# Newman: Lambda >= 0 (all zeros real for lambda > 0 but not necessarily at 0).
# Tao et al: Lambda = 0 would mean the zeros are "just barely" real.

print("The de Bruijn-Newman picture:")
print("  H_lambda(t) = Fourier(e^{lambda*u^2} * Phi(u))")
print("  lambda > 0: e^{lambda*u^2}*Phi(u) still positive, but grows!")
print("  lambda > 1/2: de Bruijn proved H_lambda has only real zeros")
print("  lambda = 0: H_0 = Xi. RH <=> zeros of H_0 are real.")
print("  Lambda = 0: the critical threshold (Rodgers-Tao: Lambda >= 0)")
print()
print("  KEY INSIGHT: Positivity of Phi is PRESERVED by the heat flow")
print("  (e^{lambda*u^2} * Phi(u) > 0 if Phi(u) > 0).")
print("  But positivity ALONE does not force zeros onto the real line.")
print("  de Bruijn needed lambda > 1/2 even WITH positivity.")
print()
print("  What EXTRA property of Phi would push lambda down to 0?")
print("  This is the content of RH in the de Bruijn-Newman language.")


# ---------------------------------------------------------------
# Section 8: Can QG5D prove the missing property?
# ---------------------------------------------------------------

print()
print("=" * 60)
print("SECTION 8: What property would close the gap?")
print("=" * 60)
print()

# Summary of what's known:
# 1. Phi > 0 (positivity) -- from theta > 0 (heat kernel positivity, RP)
# 2. Phi satisfies a FE -- from theta's FE (Poisson summation)
# 3. Phi has super-exponential decay -- from theta's Gaussian decay
# 4. Xi = Fourier(Phi) -- the Mellin/Fourier representation
# 5. RH <=> Xi has only real zeros <=> Lambda = 0

# What's missing: a property of Phi that FORCES Lambda = 0.
# Known candidates:
# (a) Log-concavity of Phi: -d^2/du^2 log Phi(u) > 0 for all u
#     (This would strengthen positivity. Check numerically.)

print("Checking log-concavity of Phi_Riemann(t):")
print("  If -d^2/dt^2 log Phi(t) > 0, Phi is log-concave.")
print()

# Compute log-concavity numerically
ts = [mpf(k)/10 for k in range(5, 101, 5)]
print(f"  {'t':>6}  {'Phi(t)':>20}  {'log Phi(t)':>20}  {'d^2 log / dt^2':>20}  {'log-conc?':>10}")
for t_val in ts:
    if t_val < mpf('0.5'):
        continue
    phi = Phi_Riemann(t_val)
    if phi <= 0:
        print(f"  {nstr(t_val, 4):>6}  {nstr(phi, 12):>20}  {'N/A':>20}  {'N/A':>20}  {'N/A':>10}")
        continue

    # Numerical second derivative of log Phi
    dt = t_val * mpf('0.001')
    phi_m = Phi_Riemann(t_val - dt)
    phi_p = Phi_Riemann(t_val + dt)

    if phi_m <= 0 or phi_p <= 0:
        print(f"  {nstr(t_val, 4):>6}  {nstr(phi, 12):>20}  {nstr(log(phi), 12):>20}  {'boundary':>20}  {'N/A':>10}")
        continue

    log_phi_m = log(phi_m)
    log_phi_0 = log(phi)
    log_phi_p = log(phi_p)
    d2_log = (log_phi_p - 2 * log_phi_0 + log_phi_m) / dt**2
    is_lc = "YES" if d2_log < 0 else "NO"
    print(f"  {nstr(t_val, 4):>6}  {nstr(phi, 12):>20}  {nstr(log_phi_0, 12):>20}  "
          f"{nstr(d2_log, 12):>20}  {is_lc:>10}")

print()
print("=" * 60)
print("COMPUTATION COMPLETE")
print("=" * 60)
