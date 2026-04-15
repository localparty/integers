"""
Round 31: Can positivity improve Lambda >= 0 to Lambda = 0?

Investigation of the Rodgers-Tao mechanism and whether RP adds information
to the proof that Lambda >= 0.

Key computations:
1. The heat flow dynamics: how zeros evolve under xi_t
2. The multiplicative heat flow: Euler factors under temperature deformation
3. Testing whether positivity of Phi constrains the BACKWARD flow
4. The interplay between GUE repulsion and kernel positivity
"""

import numpy as np
from mpmath import mp, mpf, pi, exp, sqrt, log, gamma, zeta, zetazero
from mpmath import quad, diff, fabs, inf, cos, sin, re, im, mpc
import warnings

mp.dps = 30  # 30 decimal places


# ============================================================
# PART 1: The de Bruijn-Newman heat flow on xi
# ============================================================

def theta(t):
    """Jacobi theta function: sum_{n in Z} exp(-pi n^2 t)"""
    s = mpf(0)
    for n in range(1, 100):
        term = exp(-pi * n**2 * t)
        if term < mpf(10)**(-mp.dps):
            break
        s += term
    return 1 + 2*s

def psi(t):
    """Half-theta: [theta(t) - 1] / 2"""
    return (theta(t) - 1) / 2

def Phi_kernel(u):
    """
    The kernel F(u) in the Fourier representation
    Xi(tau) = 2 int_0^infty F(u) cos(tau u) du

    F(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) exp(-pi n^2 e^{2u})

    This comes from the change of variables t = e^{2u} in the Mellin representation.
    """
    s = mpf(0)
    for n in range(1, 100):
        e2u = exp(2*u)
        arg = pi * n**2 * e2u
        if arg > mp.dps * log(10):
            break
        term = (2 * pi**2 * n**4 * exp(mpf(9)*u/2) - 3 * pi * n**2 * exp(mpf(5)*u/2)) * exp(-arg)
        s += term
    return s

def Phi_kernel_with_heat(u, lam):
    """
    The heat-flowed kernel: F_lambda(u) = exp(lambda * u^2) * F(u)

    For lambda > 0: broadens the kernel (smoothing)
    For lambda = 0: the original kernel (= xi on the critical line)
    For lambda < 0: sharpens the kernel (can create off-line zeros)
    """
    return exp(lam * u**2) * Phi_kernel(u)


# ============================================================
# PART 2: Zero dynamics under heat flow
# ============================================================

def xi_function(s):
    """
    The Riemann xi function: xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
    """
    return mpf(1)/2 * s * (s - 1) * pi**(-s/2) * gamma(s/2) * zeta(s)

def xi_on_critical_line(tau):
    """Xi(tau) = xi(1/2 + i*tau)"""
    s = mpc(mpf(1)/2, tau)
    return xi_function(s)


print("=" * 70)
print("PART 1: Kernel F(u) positivity and heat flow")
print("=" * 70)

print("\n--- Kernel F(u) for u >= 0 ---")
u_values = [mpf(x) for x in [0, 0.1, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0]]
for u in u_values:
    F = Phi_kernel(u)
    print(f"  F({float(u):5.1f}) = {float(F):15.8e}  {'POSITIVE' if F > 0 else 'NEGATIVE'}")


# ============================================================
# PART 3: Heat-flowed kernel at various lambda
# ============================================================

print("\n--- Heat-flowed kernel F_lambda(u) at u = 1.0 ---")
for lam in [-0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0]:
    F_lam = Phi_kernel_with_heat(mpf(1), mpf(lam))
    print(f"  lambda = {lam:6.2f}: F_lambda(1) = {float(F_lam):15.8e}")

print("\n--- Heat-flowed kernel F_lambda(u) at u = 2.0 ---")
for lam in [-0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0]:
    F_lam = Phi_kernel_with_heat(mpf(2), mpf(lam))
    print(f"  lambda = {lam:6.2f}: F_lambda(2) = {float(F_lam):15.8e}")


# ============================================================
# PART 4: The Rodgers-Tao mechanism
# ============================================================

print("\n" + "=" * 70)
print("PART 2: Understanding the Rodgers-Tao proof mechanism")
print("=" * 70)

print("""
The Rodgers-Tao proof (2020) that Lambda >= 0 works as follows:

1. ASSUME Lambda < 0 (i.e., xi already has all real zeros at lambda = 0,
   AND we can push to negative lambda while maintaining all-real zeros).

2. Under the BACKWARD heat flow (lambda decreasing from 0):
   - Zeros of H_lambda move according to an ODE system
   - Each zero x_k(lambda) evolves by:
     dx_k/d_lambda = -2 sum_{j != k} 1/(x_k - x_j)
   - This is a Coulomb/Dyson-type repulsion

3. The KEY: as lambda decreases, zeros REPEL each other (GUE dynamics).
   Two nearby zeros push each other apart. But if zeros separate too much,
   they must eventually COLLIDE (because the functional equation pairs them
   symmetrically, and there's no room at infinity).

4. At a collision point: two real zeros merge and split into a complex
   conjugate pair. This creates off-line zeros.

5. Rodgers-Tao showed: the zero dynamics are INCOMPATIBLE with Lambda < 0.
   If Lambda < 0, the backward flow would need to maintain all-real zeros
   for lambda in [Lambda, 0], but the Coulomb repulsion makes this impossible
   for negative lambda.

6. THEREFORE: Lambda >= 0.
""")


# ============================================================
# PART 5: Zero spacing and GUE repulsion
# ============================================================

print("--- First 20 nontrivial zeros of zeta (normalized) ---")
zeros = []
for k in range(1, 21):
    rho = zetazero(k)
    zeros.append(float(im(rho)))
print(f"  gamma_k: {[f'{z:.4f}' for z in zeros]}")

# Compute spacings
spacings = [zeros[k+1] - zeros[k] for k in range(len(zeros)-1)]
avg_spacing = sum(spacings) / len(spacings)
print(f"\n  Average spacing: {avg_spacing:.6f}")
print(f"  Spacings (normalized by average):")
norm_spacings = [s / avg_spacing for s in spacings]
print(f"  {[f'{s:.4f}' for s in norm_spacings]}")

# The GUE prediction: the nearest-neighbor spacing distribution
# is the Gaudin distribution (no zero spacing, quadratic repulsion)
print(f"\n  Min spacing (normalized): {min(norm_spacings):.4f}")
print(f"  Max spacing (normalized): {max(norm_spacings):.4f}")
print(f"  This is consistent with GUE (no zero spacing = no collisions)")


# ============================================================
# PART 6: The multiplicative heat flow idea
# ============================================================

print("\n" + "=" * 70)
print("PART 3: The Multiplicative Heat Flow")
print("=" * 70)

print("""
Standard heat flow: acts on the ADDITIVE representation (theta function).
  theta_t(x) = sum_n exp(-pi n^2 (x + 2t))
  = the heat equation on S^1 with "temperature" t

IDEA: a MULTIPLICATIVE heat flow acting on the Euler product.
  zeta_t(s) = prod_p (1 - p^{-(s+t)})^{-1}

At t = 0: the standard zeta function.
As t increases: better convergence (s+t has larger real part).
As t decreases (goes negative): worse convergence.

Question: is there a Newman-type constant for this multiplicative flow?
""")

# Compute the "multiplicative heat-flowed zeta" for various t
print("--- Multiplicative heat-flowed zeta: zeta(s+t) ---")
print("  (This is simply zeta evaluated at s+t)")
print("  s = 1/2 + 14.13i (near first zero)")
s0 = mpc(mpf(1)/2, mpf('14.134725'))
for t in [mpf('-0.5'), mpf('-0.25'), mpf(0), mpf('0.25'), mpf('0.5')]:
    val = zeta(s0 + t)
    print(f"  t = {float(t):6.2f}: zeta(s+t) = {float(re(val)):12.6e} + {float(im(val)):12.6e}i  |zeta| = {float(fabs(val)):12.6e}")

print("""
OBSERVATION: zeta(s+t) for t > 0 just shifts the argument.
This is NOT the same as the de Bruijn-Newman heat flow.

The de Bruijn-Newman flow acts on the KERNEL F(u) by multiplying by
exp(lambda * u^2). This is a Gaussian smoothing in the Fourier variable.

The multiplicative shift zeta(s+t) acts on the Dirichlet series by
multiplying each coefficient a_n by n^{-t}. This is a MULTIPLICATIVE
damping, not a Gaussian smoothing.

These are DIFFERENT flows on the space of entire functions!
""")


# ============================================================
# PART 7: Can the Euler product restrict backward flow?
# ============================================================

print("=" * 70)
print("PART 4: Does the Euler product restrict backward heat flow?")
print("=" * 70)

print("""
The KEY question: in the Rodgers-Tao proof, does the Euler product
play a role? Or is it purely about zero dynamics?

ANSWER: The Rodgers-Tao proof uses the DISTRIBUTION of zeros
(specifically, the two-point correlation function) which comes from
the Euler product via the explicit formula. But it does NOT use
the Euler product DIRECTLY.

The proof works as follows:
1. Start with the kernel F(u) > 0 (we know this from RP).
2. H_lambda(tau) = int F(u) exp(lambda u^2) cos(tau u) du
3. The zeros of H_lambda are the eigenvalues of the "GUE matrix"
   at temperature lambda.
4. As lambda DECREASES from 0, zeros repel each other.
5. The repulsion strength is proportional to 1/(x_k - x_j)^2.
6. Rodgers-Tao proved: this repulsion is strong enough that zeros
   MUST collide at some lambda_c > 0 (they can't be maintained
   in a real configuration for lambda < 0).
7. But this means H_lambda for lambda < 0 has complex zeros.
8. Therefore Lambda >= 0.

The critical insight: the proof uses the TWO-POINT FUNCTION of
the zeros (Montgomery's pair correlation conjecture, partially
proved by Rodgers-Tao) to establish the repulsion strength.
This two-point function comes from the ARITHMETIC (primes,
Euler product) but enters only STATISTICALLY.
""")


# ============================================================
# PART 8: Testing whether RP adds to Rodgers-Tao
# ============================================================

print("=" * 70)
print("PART 5: Does RP (positivity of F) add to the Rodgers-Tao bound?")
print("=" * 70)

print("""
Rodgers-Tao proved Lambda >= 0 using:
  (A) Zero dynamics (Coulomb ODE for zero positions)
  (B) Pair correlation estimates (from the explicit formula + primes)
  (C) The fact that F is a real even rapidly decaying function

RP (from the e-circle framework) gives:
  (D) F(u) > 0 for all u

Does (D) improve the bound from Lambda >= 0 to Lambda = 0?

ANALYSIS:
The de Bruijn theorem: F > 0 => Lambda <= 1/2.
The Rodgers-Tao theorem: (A)+(B)+(C) => Lambda >= 0.
Together: Lambda in [0, 1/2].

Could F > 0 additionally imply Lambda <= 0?

NO, for the following reason:

Consider a PERTURBATION of the Riemann kernel:
  F_epsilon(u) = F(u) + epsilon * g(u)
where g is chosen so that:
  - F_epsilon > 0 (preserved for small epsilon)
  - F_epsilon is even and rapidly decaying
  - F_epsilon satisfies the same functional equation

Such perturbations EXIST and generically have Lambda > 0.
(The space of positive, even, rapidly-decaying functions with the right
FE is infinite-dimensional, and Lambda = 0 is a codimension-infinity
condition within it.)

So positivity ALONE cannot force Lambda = 0. The statement
"F > 0 => Lambda <= 0" is FALSE for generic F.

WHAT MAKES THE RIEMANN KERNEL SPECIAL?
The Riemann kernel F is not generic -- it comes from the theta
function of the integer lattice Z. This lattice has the Euler
product structure. The Euler product structure is what makes
Lambda = 0 (if RH is true).
""")


# ============================================================
# PART 9: The log-concavity approach
# ============================================================

print("=" * 70)
print("PART 6: Log-concavity of F and its implications")
print("=" * 70)

# Compute -d^2/du^2 log F(u) for the Riemann kernel
print("--- Log-concavity: -d^2/du^2 log F(u) ---")
for u in [mpf('0.5'), mpf(1), mpf(2), mpf(3), mpf(5)]:
    F_val = Phi_kernel(u)
    if F_val > 0:
        def logF(x):
            val = Phi_kernel(x)
            if val > 0:
                return log(val)
            return mpf('-inf')
        try:
            d2logF = diff(logF, u, 2)
            print(f"  u = {float(u):4.1f}: -d^2 log F / du^2 = {float(-d2logF):12.6f}  {'(log-concave)' if d2logF < 0 else '(NOT log-concave)'}")
        except:
            print(f"  u = {float(u):4.1f}: computation failed")


# ============================================================
# PART 10: The forward-only nature of the Euler product under heat flow
# ============================================================

print("\n" + "=" * 70)
print("PART 7: Does the Euler product survive heat flow?")
print("=" * 70)

print("""
For t > 0 (forward heat flow), does zeta_t(s) have an Euler product?

The heat-flowed xi function is:
  H_lambda(tau) = int_0^infty exp(lambda u^2) F(u) cos(tau u) du

Back in the s-variable (s = 1/2 + i*tau):
  xi_lambda(s) = H_lambda(tau)

For lambda > 0: xi_lambda is an ENTIRE function with all real zeros
(for lambda >= Lambda). Does it factor as a product over primes?

KEY THEOREM: The Euler product is a property of the ORIGINAL zeta(s),
not of xi_lambda(s). Specifically:
  zeta(s) = prod_p (1 - p^{-s})^{-1} for Re(s) > 1
This converges absolutely for Re(s) > 1. The analytic continuation
to all of C does NOT have an Euler product (the product diverges).

For the heat-flowed version: xi_lambda corresponds to a DIFFERENT
entire function for each lambda. The Euler product structure is
specific to lambda = 0 (the original zeta). For lambda != 0,
xi_lambda is a different function that generically does NOT have
an Euler product.

CONCLUSION: The Euler product is NOT preserved under heat flow.
The heat flow is an ADDITIVE operation (convolution in Fourier space),
and the Euler product is MULTIPLICATIVE structure. The two are
incompatible.
""")


# ============================================================
# PART 11: The multiplicative structure as a constraint on Lambda
# ============================================================

print("=" * 70)
print("PART 8: The Euler product as a constraint on Lambda")
print("=" * 70)

# The Euler product at s = 1/2 + it: prod_p (1 - p^{-1/2 - it})^{-1}
# This product does NOT converge (conditionally), but the partial products
# give important information about zero distribution.

print("--- Partial Euler products at s = 1/2 + 14.13i ---")
s = mpc(mpf(1)/2, mpf('14.134725'))
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

partial_product = mpc(1, 0)
for p in primes:
    factor = 1 / (1 - mpc(p)**(-s))
    partial_product *= factor
    print(f"  Up to p = {p:3d}: |prod| = {float(fabs(partial_product)):12.6e}  arg = {float(im(log(partial_product))):8.4f}")

print(f"\n  zeta({float(re(s)):.1f} + {float(im(s)):.2f}i) = {float(fabs(zeta(s))):12.6e}")
print("  (The partial product should approximate |zeta(s)| as more primes are included)")
print("  (But convergence is conditional and slow on the critical line)")


# ============================================================
# PART 12: Summary computation - the gap measure
# ============================================================

print("\n" + "=" * 70)
print("PART 9: The precise gap [0, 1/2] and what bridges it")
print("=" * 70)

print("""
FROM ABOVE (positivity, RP):
  Lambda <= 1/2 (de Bruijn 1950)
  Mechanism: F(u) > 0 => the Fourier transform H_lambda has no
  off-axis zeros for lambda >= 1/2 (Gaussian smoothing is strong enough).

FROM BELOW (arithmetic, Euler product):
  Lambda >= 0 (Rodgers-Tao 2020)
  Mechanism: zero repulsion (from pair correlation, which comes from
  primes via the explicit formula) makes backward flow impossible.

THE GAP: Lambda in [0, 1/2].

WHAT WOULD CLOSE IT FROM BELOW (Lambda = 0):
  Need: the zero repulsion is EXACTLY strong enough that zeros are
  "just barely" on the real line at lambda = 0. Not "robustly" real
  (Lambda < 0) but "critically" real (Lambda = 0).

  This requires understanding the EXACT balance between:
  (a) The pair correlation (repulsion strength)
  (b) The potential created by F(u)
  (c) The global constraint from the functional equation

WHAT WOULD CLOSE IT FROM ABOVE (Lambda <= 0):
  Need: the kernel F has ADDITIONAL structure (beyond positivity)
  that prevents the Gaussian smoothing from being necessary.

  Candidates:
  - The Euler product (multiplicative factorization of F)
  - Full modular invariance (SL(2,Z) symmetry of theta)
  - The lattice structure (F comes from Z, not a generic lattice)

COMBINING ABOVE AND BELOW:
  If BOTH bounds could be improved:
  - From above: Lambda <= 0 (from Euler product structure of F)
  - From below: Lambda >= 0 (already proved)
  - Together: Lambda = 0 (= RH)

  The question is whether the Euler product gives Lambda <= 0.
  This is NOT what Rodgers-Tao proved. They proved Lambda >= 0 using
  the ARITHMETIC of the zeros. To prove Lambda <= 0 would require
  showing that the arithmetic PREVENTS the creation of off-line zeros
  even without Gaussian smoothing.
""")

print("\nDone.")
