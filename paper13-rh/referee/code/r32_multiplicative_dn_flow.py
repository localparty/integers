"""
R32: Multiplicative de Bruijn-Newman Flow via Frobenius
Computations for research/81-r32-multiplicative-dn-flow.md

Explores:
1. The "naive" multiplicative flow: zeta(ns) and its zeros
2. Satake parameter deformation: Frobenius iteration on Euler factors
3. Zero trajectories under the multiplicative flow
4. Comparison with the standard (additive) DN flow
5. Function field analogue: Frobenius on a curve over F_q
"""

import numpy as np
from scipy.optimize import brentq
from mpmath import mp, zeta, zetazero, gamma as mpgamma, pi as mppi, sqrt as mpsqrt
from mpmath import log as mplog, exp as mpexp, im, re, mpc, mpf, fabs, j as mpj
import warnings

mp.dps = 30  # 30 decimal places

# ============================================================
# Part A: The naive multiplicative flow: zeta(ns)
# ============================================================

print("=" * 70)
print("PART A: The Naive Multiplicative Flow zeta(ns)")
print("=" * 70)

# Get first 10 zeta zeros
num_zeros = 10
zeros = []
for k in range(1, num_zeros + 1):
    rho = zetazero(k)
    zeros.append(rho)
    print(f"  rho_{k} = 1/2 + {float(im(rho)):.6f}i")

print()
print("Zeros of zeta(ns) are at s = rho_k / n:")
print()
for n in [1, 2, 3, 5, 10, 100]:
    print(f"  n = {n}:")
    for k in range(1, min(4, num_zeros + 1)):
        rho = zeros[k - 1]
        s_n = rho / n
        print(f"    rho_{k}/n = {float(re(s_n)):.6f} + {float(im(s_n)):.6f}i  "
              f"(Re = {float(re(s_n)):.6f}, dist from 1/2 = {float(fabs(re(s_n) - mpf('0.5'))):.6f})")
    print()

print("Key observation: Re(rho_k/n) = Re(rho_k)/n = 1/(2n)")
print("As n -> inf, ALL zeros collapse to Re(s) = 0 (not 1/2)")
print("This flow moves zeros AWAY from the critical line.")
print("The 'critical line' for zeta(ns) would be Re(s) = 1/(2n).")
print()

# ============================================================
# Part B: Satake parameter Frobenius iteration
# ============================================================

print("=" * 70)
print("PART B: Satake Parameter Frobenius Iteration")
print("=" * 70)
print()

# For each prime p, the local Euler factor is (1 - p^{-s})^{-1}
# Under "Frobenius iteration n times": the Satake parameter alpha_p = p^{-s}
# becomes alpha_p^n = p^{-ns}
# So the "Frobenius-iterated" Euler product is:
# prod_p (1 - p^{-ns})^{-1} = zeta(ns)
# This is the SAME as Part A. The naive Frobenius iteration on the
# standard zeta IS just argument scaling.

print("For zeta(s) = prod_p (1 - p^{-s})^{-1}:")
print("  Satake parameter at p: alpha_p = 1 (trivially, for the Riemann zeta)")
print("  Local factor: (1 - p^{-s})^{-1}")
print()
print("Frobenius^n on the local factor:")
print("  If Frob_p raises alpha_p -> alpha_p^n = 1^n = 1  (trivial!)")
print("  The Satake parameter for zeta is FIXED by Frobenius.")
print()
print("Alternative: Frob_p acts by p^{-s} -> p^{-ns}:")
print("  Then prod_p (1 - p^{-ns})^{-1} = zeta(ns)  [Part A]")
print()

# More interesting: consider a general Dirichlet L-function
# L(s, chi) = prod_p (1 - chi(p) p^{-s})^{-1}
# Under Frobenius^n: chi(p) -> chi(p)^n = chi(p^n mod m)

print("For L(s, chi) with chi a Dirichlet character mod m:")
print("  Frobenius^n on Satake: chi(p) -> chi(p)^n")
print()

# Compute for chi_4 (the nontrivial character mod 4)
print("Example: chi_4 (mod 4): chi(1)=1, chi(3)=-1")
print()

def chi4(n):
    n = n % 4
    if n == 1: return 1
    if n == 3: return -1
    return 0  # n even

primes_small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for n_iter in [1, 2, 3, 4, 5]:
    print(f"  Frobenius^{n_iter}: chi(p) -> chi(p)^{n_iter}")
    for p in primes_small[:6]:
        chi_val = chi4(p)
        chi_n = chi_val ** n_iter if chi_val != 0 else 0
        print(f"    p={p}: chi(p)={chi_val}, chi(p)^{n_iter}={chi_n}", end="")
        if chi_val != 0:
            print(f"  (Euler factor: (1 - {chi_n}*{p}^{{-s}})^{{-1}})")
        else:
            print(f"  (ramified)")
    print()

print("Observation: For chi_4, Frobenius^n gives:")
print("  n odd:  chi^n = chi  (same L-function)")
print("  n even: chi^n = chi_0 (principal character) -> related to zeta")
print("  The flow is PERIODIC with period 2 (= order of chi).")
print()

# ============================================================
# Part C: Function field analogue - curve over F_q
# ============================================================

print("=" * 70)
print("PART C: Function Field Analogue")
print("=" * 70)
print()

# For a curve X over F_q of genus g, the zeta function is:
# Z_X(u) = P(u) / ((1-u)(1-qu))
# where P(u) = prod_{i=1}^{2g} (1 - alpha_i u) and |alpha_i| = q^{1/2} (Weil/Deligne)

# Under Frobenius^n: alpha_i -> alpha_i^n
# Z_{X,n}(u) = P_n(u) / ((1-u)(1-q^n u))
# where P_n(u) = prod_{i=1}^{2g} (1 - alpha_i^n u)

# For the simplest example: elliptic curve over F_q (genus 1)
# P(u) = 1 - a_q u + q u^2 where a_q = q + 1 - |E(F_q)|
# Roots of P: alpha, beta with alpha*beta = q, alpha+beta = a_q

# Take q = 5, a_q = 2 (so |E(F_5)| = 5 + 1 - 2 = 4)
q = 5
a_q = 2
print(f"Elliptic curve over F_{q} with a_q = {a_q} (|E(F_q)| = {q+1-a_q})")
print()

# alpha, beta are roots of u^2 - a_q*u + q = 0
disc = a_q**2 - 4*q
print(f"Discriminant: a_q^2 - 4q = {disc}")
if disc < 0:
    alpha = complex(a_q/2, np.sqrt(-disc)/2)
    beta = complex(a_q/2, -np.sqrt(-disc)/2)
else:
    alpha = complex((a_q + np.sqrt(disc))/2, 0)
    beta = complex((a_q - np.sqrt(disc))/2, 0)

print(f"  alpha = {alpha}")
print(f"  beta  = {beta}")
print(f"  |alpha| = {abs(alpha):.6f} (should be sqrt(q) = {np.sqrt(q):.6f})")
print(f"  |beta|  = {abs(beta):.6f}")
print(f"  alpha*beta = {(alpha*beta).real:.6f} (should be q = {q})")
print()

print("Frobenius iteration: alpha^n, beta^n")
print()
for n in [1, 2, 3, 4, 5, 10, 50, 100]:
    an = alpha**n
    bn = beta**n
    # For the zeta function of X over F_{q^n}, the eigenvalues are alpha^n, beta^n
    # |alpha^n| should be q^{n/2}
    print(f"  n={n:3d}: |alpha^n| = {abs(an):.6e}, q^(n/2) = {q**(n/2):.6e}, "
          f"ratio = {abs(an)/q**(n/2):.10f}")

print()
print("Key: |alpha^n| = |alpha|^n = (sqrt(q))^n = q^{n/2} EXACTLY")
print("This is STABLE: the flow preserves the 'critical line' |alpha| = sqrt(q).")
print()

# Normalized picture: set w_i = alpha_i / q^{1/2}
# Then |w_i| = 1, and under Frobenius^n: w_i -> w_i^n (moves on the unit circle)
print("Normalized eigenvalues w = alpha/sqrt(q):")
w = alpha / np.sqrt(q)
print(f"  w = {w}")
print(f"  |w| = {abs(w):.10f}")
print()
for n in [1, 2, 3, 4, 5, 10, 100]:
    wn = w**n
    print(f"  n={n:3d}: w^n = {wn.real:.6f} + {wn.imag:.6f}i, |w^n| = {abs(wn):.10f}")

print()
print("The normalized eigenvalues stay on the unit circle under Frobenius iteration.")
print("This IS the function field analogue of 'zeros on the critical line'.")

# ============================================================
# Part D: What happens when |alpha| != q^{1/2}?
# ============================================================

print()
print("=" * 70)
print("PART D: Unstable Flow When |alpha| != q^{1/2}")
print("=" * 70)
print()

# Hypothetical: suppose alpha had |alpha| = q^{1/2 + delta} for some delta > 0
# Then |alpha^n| = q^{n(1/2 + delta)} = q^{n/2} * q^{n*delta}
# As n -> inf: |alpha^n| / q^{n/2} -> inf  (exponentially divergent)

# This is the "instability" that Deligne's theorem rules out

for delta in [0.01, 0.05, 0.1, 0.2]:
    print(f"delta = {delta}:")
    alpha_bad = q**(0.5 + delta) * np.exp(1j * np.pi / 4)
    for n in [1, 5, 10, 50, 100]:
        ratio = abs(alpha_bad**n) / q**(n/2)
        print(f"  n={n:3d}: |alpha^n|/q^(n/2) = {ratio:.6e}")
    print()

print("If |alpha| != q^{1/2}, the Frobenius flow is UNSTABLE:")
print("  |alpha| > q^{1/2}: |alpha^n|/q^{n/2} -> inf  (diverges)")
print("  |alpha| < q^{1/2}: |alpha^n|/q^{n/2} -> 0    (collapses)")
print("  |alpha| = q^{1/2}: |alpha^n|/q^{n/2} = 1     (STABLE)")
print()
print("The Weil conjectures (Deligne) = ALL eigenvalues are stable under Frobenius flow.")

# ============================================================
# Part E: Number field: where do zeros of zeta(ns) go?
# ============================================================

print()
print("=" * 70)
print("PART E: Zero Trajectories Under zeta(ns)")
print("=" * 70)
print()

# Zeros of zeta(ns) are at s = rho/n
# Track the first 5 zeros as n varies

print("Zero trajectories s_k(n) = rho_k / n:")
print()
print(f"{'n':>6s}", end="")
for k in range(1, 6):
    print(f"  {'Re(s_'+str(k)+')':>12s} {'Im(s_'+str(k)+')':>12s}", end="")
print()

for n_val in [1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 50.0, 100.0]:
    line = f"{n_val:6.1f}"
    for k in range(1, 6):
        rho = zeros[k - 1]
        s_n = rho / mpf(n_val)
        line += f"  {float(re(s_n)):12.6f} {float(im(s_n)):12.6f}"
    print(line)

print()
print("All zeros collapse to the origin as n -> inf.")
print("The 'critical line' Re(s) = 1/(2n) -> 0.")
print()

# ============================================================
# Part F: A more interesting flow - interpolating L-functions
# ============================================================

print("=" * 70)
print("PART F: Interpolating Satake Parameters")
print("=" * 70)
print()

# Consider the family: L_t(s) = prod_p (1 - alpha_p(t) p^{-s})^{-1}
# where alpha_p(t) smoothly deforms from some starting value to another.
#
# For the Ramanujan-tau function: alpha_p is the Satake parameter of
# the weight-12 cusp form Delta. |alpha_p| = p^{11/2} (Deligne).
# After normalization: alpha_p / p^{11/2} has |.| = 1.
#
# The "Frobenius flow" would be: alpha_p -> alpha_p^n / p^{(n-1)*11/2}
# (normalizing to keep |.| = 1)

# But let's compute something tractable: partial Euler products
# and their zero structure.

print("Partial Euler product up to prime P:")
print("  zeta_P(s) = prod_{p <= P} (1 - p^{-s})^{-1}")
print()

# Compute partial products at s = 1/2 + it for t near the first zero
t_first = float(im(zeros[0]))
print(f"First zero at t = {t_first:.6f}")
print()

ts = np.linspace(t_first - 2, t_first + 2, 201)

P_cutoffs = [2, 3, 5, 7, 11, 23, 47, 97, 197]

print("Partial product magnitudes near first zero:")
print(f"{'t':>10s}", end="")
for P in P_cutoffs:
    print(f"  {'P='+str(P):>8s}", end="")
print()

for t_val in [t_first - 1, t_first - 0.5, t_first, t_first + 0.5, t_first + 1]:
    s = mpc('0.5', str(t_val))
    line = f"{t_val:10.4f}"
    for P in P_cutoffs:
        prod_val = mpc(1, 0)
        for p in primes_small + [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                                   101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
                                   163, 167, 173, 179, 181, 191, 193, 197]:
            if p > P:
                break
            factor = 1 / (1 - mpexp(-s * mplog(p)))
            prod_val *= factor
        line += f"  {float(fabs(prod_val)):8.4f}"
    print(line)

print()

# ============================================================
# Part G: The functional equation under Frobenius
# ============================================================

print("=" * 70)
print("PART G: Functional Equation Under Frobenius Flow")
print("=" * 70)
print()

# The completed zeta: xi(s) = pi^{-s/2} Gamma(s/2) zeta(s) satisfies xi(s) = xi(1-s)
# For zeta(ns): xi_n(s) = pi^{-ns/2} Gamma(ns/2) zeta(ns) should satisfy
# xi_n(s) = xi_n(1/n - s + (n-1)/(2n))? Let's check.

print("The functional equation for zeta(ns):")
print("  zeta(ns) has a functional equation relating ns <-> 1-ns")
print("  i.e., s <-> (1-ns)/n = 1/n - s")
print()
print("  xi_n(s) := pi^{-ns/2} Gamma(ns/2) zeta(ns)")
print("  xi_n(s) = xi_n(1/n - s)  ??? Let's verify numerically.")
print()

for n_val in [1, 2, 3, 5]:
    print(f"  n = {n_val}:")
    for s_val in ['0.3+2j', '0.1+5j', '0.05+10j']:
        s = mpc(*[x.strip() for x in s_val.replace('j', '').split('+')])
        s_re = re(s)
        s_im = im(s)
        s_mp = mpc(s_re, s_im)

        ns = n_val * s_mp
        # xi(ns) = pi^{-ns/2} Gamma(ns/2) zeta(ns)
        xi_ns = mpexp(-ns/2 * mplog(mppi)) * mpgamma(ns/2) * zeta(ns)

        # The FE for zeta: xi(w) = xi(1-w), so xi(ns) = xi(1-ns)
        # 1-ns corresponds to s' where ns' = 1-ns, i.e. s' = (1-ns)/n = 1/n - s
        s_prime = mpf(1)/n_val - s_mp
        ns_prime = n_val * s_prime  # = 1 - ns
        xi_ns_prime = mpexp(-ns_prime/2 * mplog(mppi)) * mpgamma(ns_prime/2) * zeta(ns_prime)

        ratio = xi_ns / xi_ns_prime if fabs(xi_ns_prime) > mpf('1e-50') else mpc(0, 0)
        print(f"    s = {float(s_re):.2f}+{float(s_im):.1f}i: "
              f"xi(ns)/xi(1-ns) = {float(fabs(ratio)):.10f} "
              f"(should be 1 if FE holds)")
    print()

print("The functional equation xi(ns) = xi(1-ns) IS just the standard FE")
print("applied at the argument ns. It relates s <-> 1/n - s, which is")
print("the symmetry about Re(s) = 1/(2n), NOT about Re(s) = 1/2.")
print()
print("Conclusion: the naive flow zeta(ns) has its critical line at")
print("Re(s) = 1/(2n), not Re(s) = 1/2. The flow moves the critical")
print("line, not the zeros relative to the line.")

# ============================================================
# Part H: The DN constant under rescaling
# ============================================================

print()
print("=" * 70)
print("PART H: DN Constant Under Argument Rescaling")
print("=" * 70)
print()

print("If zeta(ns) has zeros rho_k/n, and the critical line is Re(s)=1/(2n),")
print("then the distance of zero k from the critical line is:")
print("  delta_k(n) = Re(rho_k/n) - 1/(2n) = (Re(rho_k) - 1/2)/n = delta_k(1)/n")
print()
print("So the relative distance delta_k(n)/delta_k(1) = 1/n for all zeros.")
print()
print("This means the 'DN constant' of zeta(ns) is:")
print("  Lambda_n = Lambda_1 / n^2  (heuristically, since Lambda ~ delta^2)")
print()
print("If Lambda_1 = 0 (RH), then Lambda_n = 0 for all n. Trivially.")
print("If Lambda_1 > 0, then Lambda_n > 0 for all finite n but Lambda_n -> 0.")
print()
print("The naive flow does NOT prove Lambda = 0. It is circular.")

# ============================================================
# Part I: Summary statistics
# ============================================================

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("1. The naive multiplicative flow zeta(ns) just rescales zeros to rho_k/n.")
print("   Its critical line is Re(s)=1/(2n). It is trivial and circular for RH.")
print()
print("2. Frobenius iteration on Satake parameters for zeta: alpha_p=1 -> 1^n=1.")
print("   The Satake parameter is FIXED. The flow is the identity.")
print()
print("3. For Dirichlet L-functions: chi(p)^n is periodic in n (period = ord(chi)).")
print("   The flow cycles through a finite set of L-functions.")
print()
print("4. Over function fields: |alpha|=q^{1/2} => |alpha^n|=q^{n/2} (STABLE).")
print("   Deligne's theorem = all eigenvalues are stable = Lambda_{F_q} = 0.")
print()
print("5. Over number fields: there is no single Frobenius. Each prime has its own.")
print("   The 'adelic Frobenius' would need to ACT on a SINGLE cohomological object")
print("   (like H^1 of a variety), not on the L-function directly.")
print()
print("6. The functional equation is NOT preserved by the naive multiplicative flow.")
print("   The flow zeta(ns) satisfies xi(ns)=xi(1-ns), not xi(s)=xi(1-s).")
print()
print("7. The DN constant Lambda is NOT improved by the naive flow.")
print("   Lambda_n = Lambda/n^2 -> 0, but this is circular (assumes Lambda finite).")
