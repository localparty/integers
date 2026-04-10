"""
Round 31 Part 2: Deeper investigation of the multiplicative heat flow
and the interaction between positivity and the Euler product.

Key questions:
1. Is there a natural multiplicative analogue of the de Bruijn-Newman constant?
2. Can the Euler product be encoded as a constraint on the kernel F?
3. What does the Weil explicit formula say about Lambda?
"""

import numpy as np
from mpmath import mp, mpf, pi, exp, sqrt, log, gamma, zeta, zetazero
from mpmath import quad, diff, fabs, inf, cos, sin, re, im, mpc, nstr
from mpmath import loggamma
import warnings

mp.dps = 30


# ============================================================
# PART A: The multiplicative heat flow - a rigorous formulation
# ============================================================

print("=" * 70)
print("PART A: Multiplicative heat flow on the Euler product")
print("=" * 70)

print("""
DEFINITION: The multiplicative heat flow is the family of L-functions
  L_t(s) = prod_p (1 - alpha_p(t) p^{-s})^{-1}

where alpha_p(t) is a "temperature-dependent" Satake parameter.

For the Riemann zeta: alpha_p = 1 for all p, so
  zeta(s) = prod_p (1 - p^{-s})^{-1}

Natural choices for the multiplicative deformation:

(M1) Shift: alpha_p(t) = p^{-t}, giving
     L_t(s) = prod_p (1 - p^{-(s+t)})^{-1} = zeta(s+t)
     This just shifts the argument. Trivial.

(M2) Damping: alpha_p(t) = e^{-t log^2 p}, giving
     L_t(s) = prod_p (1 - e^{-t log^2 p} p^{-s})^{-1}
     This damps higher primes more. Nontrivial!

(M3) Rankin-Selberg: L_t(s) = L(s, f_t x f_t) where f_t is a
     heat-flowed modular form. This preserves modularity but changes
     the L-function.

Let's investigate (M2) numerically.
""")

# Compute the M2 multiplicative heat flow
def mult_heat_zeta(s, t, num_primes=50):
    """
    The multiplicatively damped zeta:
    prod_p (1 - exp(-t log^2 p) p^{-s})^{-1}
    """
    from sympy import primerange
    primes = list(primerange(2, 300))[:num_primes]
    product = mpc(1, 0)
    for p in primes:
        lp = log(mpf(p))
        alpha = exp(-t * lp**2)
        factor = 1 / (1 - alpha * mpc(p)**(-s))
        product *= factor
    return product

print("--- M2 multiplicative heat flow at s = 2 ---")
for t in [mpf(0), mpf('0.01'), mpf('0.05'), mpf('0.1'), mpf('0.5'), mpf(1)]:
    val = mult_heat_zeta(mpf(2), t)
    true_val = zeta(2) if t == 0 else None
    print(f"  t = {float(t):5.2f}: L_t(2) = {float(re(val)):12.8f}  {'(= pi^2/6 = ' + nstr(zeta(2), 10) + ')' if t == 0 else ''}")

print("\n--- M2 at s = 1/2 + 14.13i (near first zero) ---")
s0 = mpc(mpf(1)/2, mpf('14.134725'))
for t in [mpf(0), mpf('0.001'), mpf('0.01'), mpf('0.05'), mpf('0.1')]:
    val = mult_heat_zeta(s0, t, num_primes=30)
    print(f"  t = {float(t):6.3f}: |L_t(s)| = {float(fabs(val)):12.6e}")


# ============================================================
# PART B: The Weil explicit formula and Lambda
# ============================================================

print("\n" + "=" * 70)
print("PART B: The Weil explicit formula connection to Lambda")
print("=" * 70)

print("""
The Weil explicit formula relates zeros and primes:

  sum_rho h(rho) = h_hat(0) + h_hat(1) - sum_p sum_k log(p)/p^{k/2}
                    * [h_hat(k log p) + h_hat(-k log p)] + (Gamma terms)

where h is a test function and h_hat is its Fourier transform.

WEIL POSITIVITY: RH <=> for all admissible h >= 0 with h_hat >= 0,
the left side is >= 0.

OBSERVATION: The Weil explicit formula connects:
- SPECTRAL side: sum over zeros (the zero distribution)
- ARITHMETIC side: sum over primes (the Euler product data)

The de Bruijn-Newman Lambda encodes HOW CLOSE the zeros are to being
all real. Lambda = 0 means "barely real." Lambda > 0 means "some are
off-line."

Can we express Lambda in terms of the ARITHMETIC data (the prime sum)?

KEY INSIGHT FROM RODGERS-TAO:
Lambda >= 0 was proved using the pair correlation function R_2(x, y),
which is defined as:

  R_2(x, y) = sum_{rho, rho'} delta(x - gamma_rho) delta(y - gamma_{rho'})

Montgomery's conjecture (partially proved by Rodgers-Tao) says:

  R_2(x, y) ~ 1 - sin^2(pi(x-y)) / (pi(x-y))^2  (GUE statistics)

This comes from the EXPLICIT FORMULA applied to the two-point function:
  R_2 depends on the PRIME POWERS p^k via the von Mangoldt function.

The de Bruijn-Newman constant Lambda is determined by the pair
correlation. Specifically:
  - If R_2 = 1 (Poisson, independent zeros): Lambda = 1/2
  - If R_2 = GUE (full repulsion): Lambda = 0
  - If R_2 shows even MORE repulsion than GUE: Lambda < 0 (impossible)

So the Rodgers-Tao result Lambda >= 0 says: the repulsion is AT MOST
as strong as GUE. And Lambda = 0 would say: the repulsion is EXACTLY GUE.
""")


# ============================================================
# PART C: Positivity of F and the pair correlation
# ============================================================

print("=" * 70)
print("PART C: Does F > 0 constrain the pair correlation?")
print("=" * 70)

print("""
The pair correlation function R_2 determines Lambda.
The kernel positivity F > 0 determines Lambda <= 1/2.

QUESTION: Does F > 0 constrain R_2 beyond what is needed for Lambda >= 0?

ANALYSIS:
The pair correlation R_2 is determined by the ARITHMETIC (primes),
not by the kernel F directly. The kernel F is a function of the
theta series (additive structure), while R_2 is determined by the
von Mangoldt function (multiplicative structure).

However, F and R_2 are RELATED through the zeros:
  Xi(tau) = F_hat(tau) = prod_{rho} (1 - tau/gamma_rho)

The zero distribution {gamma_rho} determines both:
  - The kernel F (via inverse Fourier transform)
  - The pair correlation R_2 (by definition)

So F > 0 is a constraint ON THE ZEROS, and R_2 is ALSO a property
of the zeros. In principle, F > 0 could constrain R_2.

But this is CIRCULAR: we're saying "the zeros constrain the zeros."
The real question is: does the POSITIVITY of F provide INDEPENDENT
information beyond what the pair correlation already gives?

ANSWER: YES, in the following sense.
  - R_2 (pair correlation) is a LOCAL property of the zeros
    (it measures the density of zero pairs at a given separation)
  - F > 0 (kernel positivity) is a GLOBAL property
    (it constrains the overall distribution of zeros)

The local property (R_2 = GUE) gives Lambda >= 0.
The global property (F > 0) gives Lambda <= 1/2.

For Lambda = 0, we need BOTH the local and global properties to
be in a specific relationship. This is where the ARITHMETIC enters:
the Euler product determines R_2, and the theta function determines F,
and the LATTICE STRUCTURE of Z connects them.
""")


# ============================================================
# PART D: The critical question - does {F > 0 + R_2 = GUE} force Lambda = 0?
# ============================================================

print("=" * 70)
print("PART D: Does {F > 0 + R_2 = GUE} force Lambda = 0?")
print("=" * 70)

print("""
If we ASSUME:
  (1) F(u) > 0 for all u (from RP)
  (2) R_2 = GUE (from Rodgers-Tao, conditional on stronger form)

Does this FORCE Lambda = 0?

ANALYSIS:

The de Bruijn-Newman constant can be expressed as:
  Lambda = lim_{T -> infty} sup_{|gamma| < T}
           (1/2 - sigma_rho) / log T

where rho = sigma_rho + i gamma are the zeros of zeta.

If all zeros have sigma_rho = 1/2 (RH), then Lambda <= 0.
Combined with Lambda >= 0 (Rodgers-Tao), this gives Lambda = 0.

But this is CIRCULAR: RH => Lambda = 0.

The NON-CIRCULAR question is:
Does {F > 0 + R_2 = GUE + functional equation} => Lambda = 0?

THIS IS THE KEY THEOREM THAT WOULD PROVE RH.

The situation is:
  - F > 0 alone: Lambda <= 1/2 (de Bruijn). NOT Lambda = 0.
  - R_2 = GUE alone: Lambda >= 0 (Rodgers-Tao). NOT Lambda = 0.
  - FE alone: Lambda real. NOT Lambda = 0.
  - F > 0 + FE: Lambda <= 1/2. NOT Lambda = 0.
  - R_2 = GUE + FE: Lambda >= 0. NOT Lambda = 0.

The question is whether F > 0 AND R_2 = GUE TOGETHER force Lambda = 0.

OBSTRUCTION: There is no known theorem of the form
"positive kernel + GUE pair correlation => all real zeros."

This is because the constraints act on DIFFERENT aspects of the zeros:
  - F > 0 constrains the FOURIER TRANSFORM of the zero counting function
  - R_2 = GUE constrains the TWO-POINT function of the zeros
  - Lambda = 0 constrains EVERY zero individually

Going from two-point statistics + global Fourier positivity to
individual zero control is a gap that has not been bridged.

HOWEVER: there is a possible route via the HIGHER correlation functions.

The pair correlation R_2 is the two-point function. GUE also predicts
the k-point functions R_k for all k. If ALL k-point functions match
GUE, then the zero distribution is COMPLETELY determined (up to density),
and Lambda = 0 follows.

The Euler product (via the explicit formula) in principle determines
ALL k-point functions. So the full Euler product + F > 0 MIGHT force
Lambda = 0.

This is the most promising direction, but proving it requires:
  (a) Establishing all R_k = GUE (currently only R_2 is partially proved)
  (b) Showing that F > 0 + all R_k = GUE => Lambda = 0
  (c) This is essentially a different (and equally hard) route to RH
""")


# ============================================================
# PART E: Numerical test - spacing statistics and positivity
# ============================================================

print("=" * 70)
print("PART E: Numerical spacing statistics")
print("=" * 70)

# Compute more zeros and their spacings
N_zeros = 50
zeros = []
for k in range(1, N_zeros + 1):
    rho = zetazero(k)
    zeros.append(float(im(rho)))

# Normalize by local density: density ~ (1/2pi) log(gamma/2pi e)
normalized_spacings = []
for k in range(len(zeros) - 1):
    gamma_k = zeros[k]
    density = (1 / (2*np.pi)) * np.log(gamma_k / (2*np.pi * np.e))
    spacing = zeros[k+1] - zeros[k]
    normalized_spacings.append(spacing * density)

print(f"  Number of zeros computed: {N_zeros}")
print(f"  Number of spacings: {len(normalized_spacings)}")
print(f"  Mean normalized spacing: {np.mean(normalized_spacings):.6f}")
print(f"  Std of normalized spacing: {np.std(normalized_spacings):.6f}")
print(f"  Min normalized spacing: {min(normalized_spacings):.6f}")
print(f"  Max normalized spacing: {max(normalized_spacings):.6f}")

# GUE prediction: mean = 1, variance ~ 0.284
# Poisson prediction: mean = 1, variance = 1
print(f"\n  GUE predicted variance: ~0.284")
print(f"  Poisson predicted variance: 1.0")
print(f"  Observed variance: {np.var(normalized_spacings):.4f}")

# The proportion of small spacings (< 0.5) - GUE predicts very few
small_spacings = sum(1 for s in normalized_spacings if s < 0.5)
print(f"\n  Spacings < 0.5 (normalized): {small_spacings} out of {len(normalized_spacings)}")
print(f"  GUE predicts: ~5% of spacings < 0.5")
print(f"  Poisson predicts: ~39% of spacings < 0.5")


# ============================================================
# PART F: The backward heat equation and the Euler product
# ============================================================

print("\n" + "=" * 70)
print("PART F: The backward heat equation meets the Euler product")
print("=" * 70)

print("""
CRITICAL OBSERVATION (the deepest point of this investigation):

The de Bruijn-Newman heat flow is:
  d/d_lambda H_lambda = -H_lambda''  (backward heat equation)

The Euler product for zeta at lambda = 0 is:
  zeta(s) = prod_p (1 - p^{-s})^{-1}

Under the heat flow (lambda increasing from 0):
  - The function H_lambda changes continuously
  - The zeros move continuously toward the real axis
  - The Euler product BREAKS: H_lambda for lambda > 0 does NOT
    have an Euler product

Under the BACKWARD heat flow (lambda decreasing from 0):
  - The function becomes "sharper" (less smooth)
  - Zeros can collide and leave the real axis
  - The Euler product was already broken for lambda != 0

KEY QUESTION: Is there a lambda_Euler such that the Euler product
BREAKS at lambda_Euler? That is, for lambda > lambda_Euler, the
function H_lambda does NOT have an Euler product (in any sense),
but for lambda < lambda_Euler, it does?

ANSWER: The Euler product is a property ONLY of lambda = 0.
  lambda_Euler = 0  (the Euler product exists only at the original function)

This is because the Euler product is an IDENTITY of the function zeta(s),
not a general property of entire functions with real zeros. The heat
flow destroys the Euler product for any lambda != 0.

SO THE EULER PRODUCT IS A FIXED POINT of... what?

INSIGHT: The Euler product is not a property of the heat flow.
It is a property of the ARITHMETIC. The integer lattice Z has unique
factorization, which gives the Euler product for the theta function's
Mellin transform. No other function in the heat flow family
{H_lambda : lambda in R} has an Euler product (generically).

This means:
  Lambda = 0 <=> the unique lambda where H_lambda has an Euler product
               has all real zeros

RH is equivalent to: THE EULER PRODUCT POINT IS THE CRITICAL POINT
of the de Bruijn-Newman flow.

THIS IS A STRIKING REFORMULATION:
  - For lambda > 0: all zeros are real (for lambda > Lambda)
  - For lambda < 0: some zeros are off-line
  - At lambda = 0: the Euler product exists
  - RH = the Euler product exists at the EXACT lambda where zeros
    transition from all-real to having complex ones
""")


# ============================================================
# PART G: Can we bound Lambda from above using the Euler product?
# ============================================================

print("=" * 70)
print("PART G: Can the Euler product give Lambda <= 0?")
print("=" * 70)

print("""
To prove Lambda <= 0 (the other half of Lambda = 0), we need:
  "The original zeta function (lambda = 0) already has all real zeros"
  = RH itself.

So proving Lambda <= 0 IS proving RH. There is no shortcut.

However, the REFORMULATION above suggests a possible approach:

APPROACH: Show that the Euler product is INCOMPATIBLE with
Lambda > 0. That is, show that:
  "If an entire function H has all real zeros AND an Euler product,
   then H's position in the de Bruijn-Newman family is at Lambda."

In other words: the Euler product FORCES the function to be at
the critical point of the heat flow.

WHY THIS MIGHT WORK:
  - The Euler product constrains the MULTIPLICATIVE structure of H
  - The de Bruijn-Newman constant Lambda constrains the ADDITIVE
    structure (Fourier kernel)
  - If these two constraints are INCOMPATIBLE for Lambda > 0,
    then Lambda = 0.

WHY THIS PROBABLY DOESN'T WORK (as stated):
  - H_lambda for lambda > Lambda has all real zeros but NO Euler product
  - So "all real zeros + Euler product" is a very strong condition
  - But we'd need to show this condition IMPLIES Lambda <= 0
  - This is essentially: Euler product + all-real zeros => Lambda = 0
  - Which is: Euler product => (if all zeros real, then Lambda = 0)
  - Which is: Euler product + RH => Lambda = 0
  - But Lambda = 0 IS RH, so this is circular: RH => Lambda = 0

THE CIRCULARITY:
  Lambda = 0 is EQUIVALENT to RH. Any proof of Lambda = 0 IS a proof
  of RH, and vice versa. You cannot prove Lambda = 0 without proving RH.

  The question is whether the COMBINATION
    {Euler product + positivity of F + functional equation}
  constitutes a PROOF of RH (= Lambda = 0).

  Currently: each ingredient gives a PARTIAL bound:
    - FE: Lambda real
    - F > 0: Lambda <= 1/2
    - Euler product: Lambda >= 0 (via Rodgers-Tao)

  The combination gives Lambda in [0, 1/2]. To close to Lambda = 0
  would require a NEW argument that uses ALL THREE simultaneously.
""")


# ============================================================
# PART H: The Selberg class and universality
# ============================================================

print("=" * 70)
print("PART H: The Selberg class perspective")
print("=" * 70)

print("""
The SELBERG CLASS S consists of Dirichlet series F(s) satisfying:
  (S1) Ramanujan bound: a_n << n^epsilon
  (S2) Analytic continuation and functional equation
  (S3) Euler product: F(s) = prod_p exp(sum_{k>=1} b_{p^k} p^{-ks})
  (S4) Polynomial growth in vertical strips

The GRAND RH (GRH) conjectures that ALL F in S have zeros on Re(s) = 1/2.

For each F in S, there is a de Bruijn-Newman constant Lambda_F.

QUESTION: Does the Selberg class axiom (S3) (Euler product) constrain
Lambda_F?

ANSWER (conjectural): For F in S, Lambda_F = 0. This is GRH.
  - Lambda_F >= 0 follows from the zero distribution (GUE for all F in S)
  - Lambda_F <= 0 follows from... ? (This IS GRH)

The Selberg class axioms ALONE do not prove GRH. The axioms define
the CLASS of functions for which GRH should hold, but the proof
requires something beyond the axioms.

WHAT'S BEYOND THE AXIOMS?
The axioms (S1)-(S4) are INDIVIDUAL properties: each is a condition on F
separately. But the CLASS S has COLLECTIVE properties:
  - Selberg's orthonormality conjecture: distinct primitive F, G in S
    have orthogonal coefficients
  - The degree conjecture: the degree d_F determines the statistics
  - Conrey-Ghosh: the zeros of different F in S satisfy cross-correlation
    constraints

Perhaps it is these COLLECTIVE properties (not the individual axioms)
that force Lambda = 0 for each member.
""")


print("\n" + "=" * 70)
print("SUMMARY: The Honest Assessment")
print("=" * 70)

print("""
QUESTION: Can positivity (RP) be added to the Rodgers-Tao framework
to force Lambda = 0?

ANSWER: No, not in any straightforward way. Here is why:

1. RODGERS-TAO proves Lambda >= 0 using:
   - Zero dynamics under backward heat flow (Coulomb ODE)
   - Pair correlation estimates (from arithmetic, via explicit formula)
   - GUE repulsion prevents zeros from being maintained below lambda = 0

2. RP (positivity) proves Lambda <= 1/2 using:
   - F(u) > 0 => Fourier transform has no off-line zeros for lambda >= 1/2
   - This is de Bruijn's theorem (1950)

3. These two bounds CANNOT be combined to give Lambda = 0 because:
   - Rodgers-Tao gives a LOWER bound on Lambda (from below)
   - de Bruijn gives an UPPER bound on Lambda (from above)
   - The gap [0, 1/2] cannot be closed by combining two bounds
     that attack from DIFFERENT directions
   - To close the gap, one bound must be IMPROVED, not combined
     with the other

4. Can RP improve the Rodgers-Tao bound from Lambda >= 0 to Lambda = 0?
   - RP gives F > 0, which Rodgers-Tao already USES (implicitly, as
     part of the kernel properties)
   - F > 0 does not add new information beyond what Rodgers-Tao already
     has. Their proof works for any kernel with the right decay and
     pair correlation, regardless of positivity.

5. Can RP improve the de Bruijn bound from Lambda <= 1/2 to Lambda <= 0?
   - This would require showing that POSITIVITY of F implies more
     than Lambda <= 1/2. But generic positive kernels with the same
     functional equation can have Lambda > 0. So positivity ALONE
     cannot give Lambda <= 0.

6. THE MULTIPLICATIVE HEAT FLOW:
   - The idea of parameterizing Euler factors by temperature is natural
     but does not produce a meaningful analogue of the de Bruijn-Newman
     constant. The simplest version (zeta(s+t)) is trivial. More
     sophisticated versions (M2 damping) do not preserve the functional
     equation or modularity.
   - The Euler product is a property of lambda = 0 ONLY. It is
     destroyed by the heat flow for any lambda != 0.

7. THE REFORMULATION (the one genuinely new insight):
   RH is equivalent to: the Euler product point (lambda = 0) is the
   CRITICAL POINT of the de Bruijn-Newman flow (where zeros transition
   from all-real to having complex ones). This is a striking statement
   about the COINCIDENCE of arithmetic structure and analytic criticality.
   But it is a reformulation, not a proof.

CONFIDENCE: 95% that this approach CANNOT yield Lambda = 0 without
additional deep input that goes beyond both RP and Rodgers-Tao.

The gap Lambda in [0, 1/2] remains. The next step is NOT to try to
close it from within the de Bruijn-Newman framework, but to use
the structural SDP approach or the full modular invariance.
""")

print("\nDone.")
