"""
R21: Computations for the Ramanujan Delta function test case.
Verify Satake parameters, Ramanujan bound, and inner product data.
"""
import mpmath
import numpy as np
from mpmath import mp, mpf, sqrt, pi, cos, acos, gamma, zeta, log

mp.dps = 30  # 30 decimal places

print("=" * 70)
print("PART 1: Ramanujan Delta Function — Known Fourier Coefficients")
print("=" * 70)

# Ramanujan tau function values (first few primes)
# tau(n) = a_n for Delta = sum tau(n) q^n
tau = {
    2: -24,
    3: 252,
    5: 4830,
    7: -16744,
    11: 534612,
    13: -577738,
    17: -6905934,
    19: 10661420,
    23: 18643272,
    29: -128406630,
    31: 52843168,
    37: -182213314,
    41: -308120442,
    43: 534257568,
}

print("\nFourier coefficients tau(p) for first primes:")
print(f"{'p':>5} {'tau(p)':>15} {'tau(p)/p^(11/2)':>20} {'|normalized|':>15}")
print("-" * 60)

for p in sorted(tau.keys()):
    a_p = tau[p]
    norm = mpf(a_p) / mpf(p) ** (mpf(11) / 2)
    print(f"{p:5d} {a_p:15d} {float(norm):20.10f} {float(abs(norm)):15.10f}")

print("\nRamanujan bound: |tau(p)/p^(11/2)| <= 2 for all primes")
print("(Deligne 1974: proved via Weil conjectures on etale cohomology)")

print("\n" + "=" * 70)
print("PART 2: Satake Parameters for Delta at Each Prime")
print("=" * 70)

print("\nFor weight k=12, the Satake parameters alpha_p, beta_p satisfy:")
print("  alpha_p + beta_p = tau(p)")
print("  alpha_p * beta_p = p^(k-1) = p^11")
print("  |alpha_p| = |beta_p| = p^(11/2)  (Ramanujan)")
print()

for p in [2, 3, 5, 7, 11]:
    a_p = mpf(tau[p])
    pk = mpf(p) ** 11
    phalf = mpf(p) ** (mpf(11) / 2)

    # alpha_p and beta_p are roots of x^2 - a_p*x + p^11 = 0
    disc = a_p ** 2 - 4 * pk
    print(f"p = {p}:")
    print(f"  tau(p) = {int(a_p)}")
    print(f"  p^11 = {int(pk)}")
    print(f"  p^(11/2) = {float(phalf):.6f}")
    print(f"  discriminant = tau(p)^2 - 4*p^11 = {float(disc):.2f}")

    if disc < 0:
        # Complex conjugate pair: alpha = p^(11/2) * e^(i*theta)
        sqrt_neg_disc = sqrt(-disc)
        theta = acos(a_p / (2 * phalf))
        cos_theta = a_p / (2 * phalf)

        alpha_abs = phalf
        alpha_re = a_p / 2
        alpha_im = sqrt_neg_disc / 2

        print(f"  disc < 0 => alpha_p, beta_p are complex conjugates")
        print(f"  |alpha_p| = |beta_p| = p^(11/2) = {float(alpha_abs):.6f}")
        print(f"  alpha_p = {float(alpha_re):.4f} + {float(alpha_im):.4f}i")
        print(f"  beta_p  = {float(alpha_re):.4f} - {float(alpha_im):.4f}i")
        print(f"  cos(theta_p) = tau(p)/(2*p^(11/2)) = {float(cos_theta):.10f}")
        print(f"  theta_p = {float(theta):.10f} rad = {float(theta * 180 / pi):.6f} deg")

        # Verify |alpha|^2
        abs_sq = alpha_re ** 2 + alpha_im ** 2
        print(f"  Verify: |alpha|^2 = {float(abs_sq):.4f}, p^11 = {float(pk):.4f}, match = {abs(abs_sq - pk) < 1}")
    else:
        # Real roots (shouldn't happen for Ramanujan)
        print(f"  disc >= 0 => REAL roots (violates Ramanujan!)")
    print()

print("=" * 70)
print("PART 3: Petersson Inner Product of Delta")
print("=" * 70)

print("\nThe Petersson inner product:")
print("  <Delta, Delta>_Pet = integral_{SL(2,Z)\\H} |Delta(z)|^2 y^12 dmu(z)")
print("\nBy the Rankin-Selberg method:")
print("  <Delta, Delta>_Pet = (4pi)^(-11) * Gamma(11) * zeta*(2) * L(1, Sym^2 Delta) / (something)")
print()

# Compute known values
gamma_11 = gamma(11)
print(f"  Gamma(11) = 10! = {int(gamma_11)}")

four_pi_11 = (4 * pi) ** 11
print(f"  (4pi)^11 = {float(four_pi_11):.6f}")

# The exact Petersson norm of Delta is known
# <Delta, Delta>_Pet = (2pi)^(-12) * Gamma(12) * L(1, Sym^2 Delta) * ... 
# Actually the standard normalization gives:
# <Delta, Delta> = (4pi)^(-12) * Gamma(12) * (completed L-function value)

# The completed L-function of Sym^2(Delta) at s=1:
# L(s, Sym^2 Delta) = prod_p [(1 - alpha_p^2/p^s)(1 - alpha_p*beta_p/p^s)(1 - beta_p^2/p^s)]^(-1)
# For Delta, alpha_p*beta_p = p^11, so the middle factor is (1 - p^(11-s))^(-1) = zeta(s-11)

print(f"\nThe Petersson norm is known numerically (Zagier):")
print(f"  <Delta, Delta>_Pet = 1.03536... x 10^(-6)")
print(f"  (normalized with y^k dxdy/y^2 measure on SL(2,Z)\\H)")

print("\n\nRankin-Selberg connection to L-values:")
print("  <Delta, Delta>_Pet * (4pi)^12 / Gamma(12) = L(12, Delta x Delta_bar)")
print("  = L(1, Sym^2 Delta) * zeta(2)")
print("  L(1, Sym^2 Delta) > 0  (Gelbart-Jacquet 1978 + Shahidi 1981)")

print("\n" + "=" * 70)
print("PART 4: The Satake/Plancherel Inner Product at Each Prime")
print("=" * 70)

for p in [2, 3, 5]:
    a_p = mpf(tau[p])
    phalf = mpf(p) ** (mpf(11) / 2)
    cos_theta = a_p / (2 * phalf)
    theta = acos(cos_theta)

    print(f"\nPrime p = {p}:")
    print(f"  Satake parameter: (alpha_p, beta_p) with |alpha|=|beta|=p^(11/2)={float(phalf):.4f}")
    print(f"  cos(theta_p) = {float(cos_theta):.10f}")
    print(f"  theta_p = {float(theta):.10f}")

    # The Harish-Chandra c-function for PGL(2, Q_p)
    # c(s) = (1 - p^(-2s)) / (1 - p^(-1))
    # At s = 1/2 + it/log(p) with theta_p = t:
    s_val = mpf(1) / 2 + 1j * theta / log(p)
    c_val = (1 - mpf(p) ** (-2 * s_val)) / (1 - mpf(p) ** (-1))

    print(f"  c(1/2 + i*theta/log p) = {float(abs(c_val)):.8f} (absolute value)")

    # Plancherel density at theta_p
    # |c(1/2+it)|^(-2) gives the Plancherel weight
    plancherel_weight = abs(c_val) ** (-2)
    print(f"  Plancherel weight |c|^(-2) = {float(plancherel_weight):.8f}")

    # Tamagawa factor
    tam = 1 - mpf(p) ** (-2)
    print(f"  Tamagawa factor (1 - p^(-2)) = {float(tam):.10f}")

    # Local L-factor
    # L_p(s, Delta) = (1 - alpha_p * p^(-s))^(-1) * (1 - beta_p * p^(-s))^(-1)
    # At s = 11/2 (center of critical strip for Delta):
    # L_p(11/2, Delta) = (1 - alpha_p/p^(11/2))^(-1) * (1 - beta_p/p^(11/2))^(-1)
    # = (1 - e^(i*theta))^(-1) * (1 - e^(-i*theta))^(-1)
    # = 1/(2 - 2*cos(theta)) = 1/(4*sin^2(theta/2))
    sin_half = mpmath.sin(theta / 2)
    L_local = 1 / (4 * sin_half ** 2) if sin_half != 0 else float('inf')
    print(f"  Local L-factor at s=11/2: {float(abs(L_local)):.8f}")

print("\n" + "=" * 70)
print("PART 5: Tamagawa Product and Global Normalization")
print("=" * 70)

# The product of Tamagawa factors
# prod_p (1 - p^(-2)) = 1/zeta(2) = 6/pi^2
tam_product = 6 / pi ** 2
print(f"\nProduct of all Tamagawa factors:")
print(f"  prod_p (1 - p^(-2)) = 1/zeta(2) = 6/pi^2 = {float(tam_product):.10f}")
print(f"  zeta(2) = pi^2/6 = {float(pi**2/6):.10f}")

print("\nThis product appears in the ratio of adelic vs classical normalizations.")
print("If the adelic KK inner product = C * Petersson inner product,")
print("then C involves zeta(2) through the Tamagawa number formula.")
print(f"\nTamagawa number tau(GL(2)) = 2")
print(f"Tamagawa number tau(PGL(2)) = 2")

print("\n" + "=" * 70)
print("PART 6: Verification That Frobenius Is Unitary")
print("=" * 70)

print("\nFor each prime p, the Galois representation rho_{Delta,l} gives:")
print("  rho(Frob_p) has eigenvalues alpha_p, beta_p")
print("  |alpha_p| = |beta_p| = p^(11/2)  (Ramanujan = Deligne)")
print()
print("In the NORMALIZED representation (divide by p^(11/2)):")
print("  rho_norm(Frob_p) has eigenvalues alpha_p/p^(11/2), beta_p/p^(11/2)")
print("  These lie on the UNIT CIRCLE (since alpha_p = p^(11/2) e^(i theta))")
print("  => rho_norm(Frob_p) is UNITARY")
print()

for p in [2, 3, 5, 7, 11]:
    a_p = mpf(tau[p])
    phalf = mpf(p) ** (mpf(11) / 2)
    cos_theta = a_p / (2 * phalf)
    
    # The normalized eigenvalues
    e1 = cos_theta + 1j * sqrt(1 - cos_theta**2)
    e2 = cos_theta - 1j * sqrt(1 - cos_theta**2)
    
    print(f"  p={p:2d}: cos(theta) = {float(cos_theta):+.10f}, |e^(i theta)| = {float(abs(e1)):.10f} (should be 1.0)")

print("\n" + "=" * 70)
print("PART 7: The Weil Pairing vs RP Inner Product")
print("=" * 70)

print("""
For the Eichler-Shimura Galois representation of Delta:

  rho_{Delta,l}: Gal(Qbar/Q) -> GL(2, Q_l)

constructed from H^1_et(E, Q_l) of the universal elliptic curve E -> X(1),
specifically from Sym^10(H^1_et).

The Weil pairing on H^1_et(E, Q_l) is:
  <x, y>_Weil = x cup y  (cup product in etale cohomology)

Properties:
  - Alternating: <x,y> = -<y,x>
  - Galois-equivariant: <sigma x, sigma y> = chi(sigma) <x,y>
    where chi is the cyclotomic character
  - Non-degenerate

After twisting by Tate(11/2), Frobenius preserves the pairing:
  <Frob_p x, Frob_p y> = chi(Frob_p)^11 / p^11 * <x,y> = <x,y>
  (since chi(Frob_p) = p)

The RP inner product (from Lemma D.1):
  <F, Theta F>_RP = integral |G[phi_0]|^2 >= 0

Properties:
  - Positive-definite (not just non-degenerate)
  - Gauge-invariant: gauge transformations preserve it
  - Factorizes over places

COMPARISON:
  Weil pairing: alternating, non-degenerate, Galois-equivariant
  RP inner product: symmetric, positive-definite, gauge-invariant

These are NOT the same pairing. But they serve the same PURPOSE:
  Weil pairing => Frobenius has prescribed determinant
  RP inner product => gauge holonomy is unitary

For Deligne's proof:
  Weil pairing + Hodge-Riemann => |alpha_p| = p^(11/2)

For the adelic KK proof (if it works):
  RP inner product + gauge invariance => |alpha_p| = p^(11/2)

The key difference: Deligne uses the ALTERNATING Weil pairing
combined with the POSITIVE-DEFINITE Hodge-Riemann bilinear form.
The QG5D framework uses the POSITIVE-DEFINITE RP inner product directly.
""")

print("=" * 70)
print("PART 8: Numerical Sanity Check — First 20 tau(p)")
print("=" * 70)

# Compute tau(n) using the product formula
# Delta(q) = q * prod_{n>=1} (1 - q^n)^24
# We compute tau(n) for n = 1,...,50 using q-expansion

N = 100  # compute enough terms
coeffs = [0] * (N + 1)
coeffs[0] = 1

# (1 - q^n)^24 by repeated multiplication
for n in range(1, N + 1):
    new_coeffs = coeffs[:]
    for k in range(24):
        temp = [0] * (N + 1)
        for i in range(N + 1):
            if new_coeffs[i] == 0:
                continue
            # subtract contribution of q^n
            j = i + n
            if j <= N:
                temp[i] = temp[i] + new_coeffs[i]
                temp[j] = temp[j] - new_coeffs[i]
            else:
                temp[i] = temp[i] + new_coeffs[i]
        new_coeffs = temp
    coeffs = new_coeffs

# Actually, let's use a cleaner approach: compute prod (1-q^n)^24
# Initialize power series coefficients
tau_computed = [0] * (N + 1)
# Start with 1
prod_coeffs = [0] * (N + 1)
prod_coeffs[0] = 1

for n in range(1, N + 1):
    # Multiply by (1 - q^n)^24
    # First compute (1 - q^n)^24 using binomial theorem
    # But that's complex. Instead, multiply by (1 - q^n) twenty-four times
    for _ in range(24):
        new_prod = prod_coeffs[:]
        for i in range(N + 1):
            j = i + n
            if j <= N:
                new_prod[j] -= prod_coeffs[i]
        prod_coeffs = new_prod

# Delta(q) = q * prod (1-q^n)^24, so tau(n) = prod_coeffs[n-1]
print(f"\nComputed tau(n) from q-expansion of Delta = q * prod (1-q^n)^24:")
print(f"{'n':>5} {'tau(n) computed':>20} {'tau(n) known':>15} {'match':>8}")
print("-" * 52)

known_tau = {1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830, 6: -6048, 7: -16744,
             8: 84480, 9: -113643, 10: -115920, 11: 534612, 12: -370944,
             13: -577738, 14: 401856, 15: 1217160}

for n in sorted(known_tau.keys()):
    computed = prod_coeffs[n - 1]  # tau(n) = coeff of q^n in Delta = coeff of q^(n-1) in prod
    known = known_tau[n]
    match = "YES" if computed == known else "NO"
    print(f"{n:5d} {computed:20d} {known:15d} {match:>8}")

# Now verify Ramanujan bound for all computed prime tau values
print(f"\nRamanujan bound verification |tau(p)/p^(11/2)| <= 2:")
print(f"{'p':>5} {'tau(p)':>15} {'normalized':>15} {'|norm| <= 2':>12}")
print("-" * 50)

primes_to_check = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for p in primes_to_check:
    if p - 1 < len(prod_coeffs):
        t = prod_coeffs[p - 1]
        norm_val = float(mpf(t) / mpf(p) ** (mpf(11) / 2))
        bound_ok = abs(norm_val) <= 2.0
        print(f"{p:5d} {t:15d} {norm_val:15.8f} {'YES' if bound_ok else 'NO':>12}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
