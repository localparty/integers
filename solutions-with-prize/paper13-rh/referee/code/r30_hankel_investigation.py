"""
R30 supplementary: Investigate the Hankel matrix issue from Li's criterion.

The main computation found Hankel matrices H_n are NOT PSD using 50 zeros.
Is this a truncation artifact? What does it mean for the RP connection?
"""

import numpy as np
from mpmath import mp, zetazero, re, power, conj, mpf, log, pi, exp, sqrt
from numpy.linalg import eigvalsh

mp.dps = 30

# The issue: lambda_n = sum_{ALL rho} [1 - (1-1/rho)^n]
# With only K zeros, we get lambda_n^{(K)} = partial sum.
# For small n, the sum converges fast. For large n, it converges slowly.
# The Hankel matrix H_n = (lambda_{i+j-1})_{i,j=1}^n needs lambda up to 2n-1.

# Question 1: How many zeros are needed for the Li coefficients to stabilize?
print("=" * 72)
print("How many zeros needed for Li coefficient lambda_n?")
print("=" * 72)

# Compute lambda_n for various K (number of zeros)
for n in [1, 5, 10, 20, 30]:
    print(f"\n  lambda_{n} with increasing number of zeros:")
    prev = None
    for K in [10, 20, 50, 100, 200]:
        lam = mpf(0)
        for k in range(1, K + 1):
            rho = zetazero(k)
            val = 1 - power(1 - 1/rho, n)
            val_conj = 1 - power(1 - 1/(1 - conj(rho)), n)
            lam += re(val) + re(val_conj)
        delta = ""
        if prev is not None:
            delta = f"  (delta = {float(lam - prev):+.2e})"
        prev = lam
        print(f"    K = {K:4d}: lambda_{n} = {float(lam):14.8f}{delta}")

# Question 2: The Hankel matrix — is the negative eigenvalue from truncation?
print("\n" + "=" * 72)
print("Hankel matrix eigenvalues with increasing zeros")
print("=" * 72)

for K in [20, 50, 100, 200]:
    rho_list = [zetazero(k) for k in range(1, K + 1)]
    li_coeffs = []
    for n in range(1, 61):
        lam = mpf(0)
        for rho in rho_list:
            val = 1 - power(1 - 1/rho, n)
            val_conj = 1 - power(1 - 1/(1 - conj(rho)), n)
            lam += re(val) + re(val_conj)
        li_coeffs.append(float(lam))

    print(f"\n  K = {K} zeros:")
    for N_hankel in [3, 5, 10]:
        max_n = 2 * N_hankel - 1
        if max_n > len(li_coeffs):
            break
        H = np.zeros((N_hankel, N_hankel))
        for i in range(N_hankel):
            for j in range(N_hankel):
                H[i, j] = li_coeffs[i + j]
        eigs = eigvalsh(H)
        min_eig = eigs[0]
        max_eig = eigs[-1]
        print(f"    H_{N_hankel}: min eig = {min_eig:12.4f}, max eig = {max_eig:12.4f}"
              f"  {'PSD' if min_eig >= -1e-6 else 'NOT PSD'}")

# Question 3: What are the EXACT Li coefficients (from the known formula)?
# Li (1997) / Coffey (2005):
# lambda_n = sum_{k=0}^{n} C(n,k) * c_k
# where c_k involve derivatives of xi at s=1.
# Equivalently: lambda_n = (1/(n-1)!) * [d^n/ds^n s^{n-1} log xi(s)]_{s=1}

# There is also the formula:
# lambda_n = n/2 * [gamma_E + log(4*pi) - 2] + 1 - (1/2)*sum_{k=2}^{n} C(n,k)*(-1)^k * eta(k)
# where eta(k) = (1 - 2^{1-k})*zeta(k) for k >= 2

# Simpler: Maslanka's formula gives lambda_n in terms of the Stieltjes constants.
# But the most reliable is direct computation from zeros.

print("\n" + "=" * 72)
print("The gap between Li's criterion and Weil positivity")
print("=" * 72)

# Li's criterion: lambda_n >= 0 for all n >= 1 <=> RH
# Weil positivity: sum_rho h(gamma_rho) >= 0 for all h = f*f~ <=> RH
#
# Li's test function h_n is NOT an autocorrelation (not positive-definite).
# But Li proved the two conditions are EQUIVALENT (both equivalent to RH).
# The question: does RP give EITHER of these?

# RP gives: for any f in L^2(half-circle, S^1),
#   <f, Theta f> = int f(phi) * conj(f(-phi)) dphi >= 0
# Under Mellin transform (exp map phi -> x):
#   <f, Theta f> = int |f_hat(1/2+it)|^2 * (kernel) dt >= 0

# This is a SINGLE positivity condition (for each f).
# It says the Weil distribution, tested against |g|^2, is non-negative.

# Weil positivity says this for ALL autocorrelations.
# RP gives it for ALL f in L^2(half-circle), which generates ALL
# autocorrelations in the archimedean variable.

# But the Weil distribution involves zeros of zeta, which involve ALL places.
# The archimedean RP only controls the archimedean contribution to the
# explicit formula.

print("""
  The precise chain:

  1. RP on S^1 => <f, Theta f>_{S^1} >= 0 for all f in L^2(half-circle)
     This is PROVED. (OS axioms for the free field on S^1.)

  2. Under exp map: this becomes int f(x) conj(f(1/x)) dx/x >= 0
     on R_+*. This is the archimedean Weil pairing.
     PROVED (Identity 2, 95% confidence).

  3. The archimedean Weil pairing IS one factor of the full Weil pairing
     on the idele class group C_Q = A_Q*/Q*.
     PROVED (Tate's thesis, decomposition of C_Q by places).

  4. The full Weil pairing Tr(f * f#) >= 0 on C_Q requires:
     - Archimedean factor >= 0 (from step 2, RP)
     - p-adic factors >= 0 at each p (expected but NOT from RP)
     - Compatibility under Q*-quotient (THIS IS RH)

  5. The Q*-quotient correlates all places through the arithmetic
     of prime factorization. This correlation IS the content of RH.

  CONCLUSION: RP provides step 1-2 (archimedean Weil positivity).
  Steps 4-5 are BEYOND RP's reach because RP is an archimedean tool
  and the descent through Q* is arithmetic.
""")

# Question 4: What ADDITIONAL structure could close the gap?
print("=" * 72)
print("What additional structure would close the gap?")
print("=" * 72)

print("""
  Three theoretical options:

  A. ADELIC RP: Extend RP from S^1 to the adelic circle A_Q^1/Q*.
     This would give global Weil positivity directly.
     OBSTACLE: A_Q^1/Q* is not a smooth manifold. RP requires
     a Riemannian structure (or at least a measure + reflection).
     Connes' framework provides the measure and reflection on the
     adele class space, but the positivity is EXACTLY RH.

  B. THETA FACTORIZATION: Use theta as bridge (P5m).
     theta(t) = product over places of local theta functions?
     theta_infty(t) = sum_n exp(-pi*n^2*t) (the Jacobi theta)
     theta_p(t) = ??? (p-adic theta functions exist but don't multiply)
     OBSTACLE: theta does NOT factor as a product of local thetas.
     The additive structure (sum over n) prevents multiplicative
     factorization. This is the A/M theorem again.

  C. RAMANUJAN + FUNCTIONAL EQUATION:
     If all Satake parameters satisfy |alpha_p| <= 1 (Ramanujan)
     AND the functional equation holds
     AND the Euler product converges in Re(s) > 1/2,
     THEN RH follows (under GRH for the symmetric power L-functions).
     This is the automorphic approach (Langlands program).
     OBSTACLE: Proving Ramanujan for GL(n) is itself a major open problem
     (proved only for GL(1) and GL(2) over Q).
     QG5D: Identity 11 gives Ramanujan as holonomy compactness.
     But this is the archimedean Ramanujan (holonomy of e-circle),
     not the arithmetic Ramanujan (eigenvalues of Frobenius at each p).
""")

# Question 5: Is there a genuinely MULTIPLICATIVE RP?
print("=" * 72)
print("Can one formulate RP multiplicatively?")
print("=" * 72)

# The Euler product: zeta(s) = prod_p (1 - p^{-s})^{-1}
# Each factor is > 0 for real s > 0. The product of positive factors is positive.
# So zeta(s) > 0 for real s > 0 (except the trivial zeros at s = -2n).
# This is NOT RH — RH is about COMPLEX s.

# For complex s, each factor (1-p^{-s})^{-1} is a nonzero complex number
# (has nonzero modulus). The product of nonzero complex numbers converges
# to a nonzero number for Re(s) > 1. This gives the zero-free half-plane.

# For 0 < Re(s) < 1 (critical strip), the Euler product DIVERGES.
# The zeros appear as limits of the divergent partial products.
# The zeros are COLLECTIVE phenomena — no single factor contributes them.

# A "multiplicative RP" would need to express positivity of the PRODUCT
# (not the sum) in a way that constrains the collective zeros.

# The CLOSEST thing: the Selberg class axioms.
# These are MULTIPLICATIVE conditions (Euler product, polynomial local factors)
# plus POSITIVITY conditions (Ramanujan bound |alpha_p| <= 1)
# plus SYMMETRY (functional equation).

# Conjecture (strong): Selberg class axioms => GRH.
# This would mean the multiplicative structure (Euler product + Ramanujan + FE)
# IS sufficient for RH. But this conjecture is unproven.

print("""
  A multiplicative RP would need:

  1. Express zeta(s) = prod_p (1-p^{-s})^{-1} (for Re(s) > 1)
  2. Continue to the critical strip (where the product diverges)
  3. Show the continuation has zeros ONLY on Re(s) = 1/2

  The difficulty: step 2 is where the multiplicative structure fails.
  The Euler product diverges in the critical strip. The zeros are
  NOT features of individual Euler factors — they are COLLECTIVE
  phenomena arising from the interference of infinitely many factors.

  This is P6m: the zeros are PROJECTED phenomena. They appear only
  in the additive sum (Dirichlet series), not in the multiplicative
  product (Euler factors). Each factor alone is nonvanishing.

  No known formulation of "multiplicative RP" can constrain the
  collective zeros because the collective behavior only emerges
  AFTER the projection from multiplicative to additive.

  BOTTOM LINE: RP is inherently additive (inner products, Hilbert spaces,
  spectral theory). The zeros are multiplicative-then-projected-to-additive.
  RP controls the additive side (archimedean Weil positivity).
  The multiplicative side (Euler product, prime factorization, Q*-descent)
  is beyond RP's reach.
""")

print("=" * 72)
print("SUPPLEMENTARY COMPUTATION COMPLETE")
print("=" * 72)
