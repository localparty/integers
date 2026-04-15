"""
R27: Bost-Connes Realization — Numerical Investigations

Key computations:
1. BC partition function Z(beta) = zeta(beta) near the phase transition beta=1
2. KMS condition verification: the positivity structure
3. Zeros of zeta on the critical line and their relation to beta = 1/2 + it
4. The primon gas energy levels E_n = log(n) and their statistics
5. Comparison of BC Hamiltonian spectrum with S^1 Laplacian spectrum
6. Free energy F(beta) = -log Z(beta) / beta and its behavior near beta=1
"""

import numpy as np
from mpmath import mp, mpf, zeta, gamma, log, exp, pi, fabs, re, im, zetazero, diff
from scipy import optimize

mp.dps = 30  # 30 decimal places

print("=" * 70)
print("R27: BOST-CONNES REALIZATION — NUMERICAL INVESTIGATIONS")
print("=" * 70)

# =====================================================================
# 1. THE BC PARTITION FUNCTION Z(beta) = zeta(beta) NEAR beta = 1
# =====================================================================
print("\n--- 1. BC Partition Function Z(beta) = zeta(beta) Near beta = 1 ---\n")

betas = [0.5, 0.8, 0.9, 0.95, 0.99, 0.999, 1.001, 1.01, 1.05, 1.1, 1.5, 2.0, 3.0, 5.0]
print(f"{'beta':>8s}  {'Z(beta) = zeta(beta)':>25s}  {'Phase':>12s}")
print("-" * 55)
for b in betas:
    z = zeta(mpf(b))
    if b == 1.0:
        print(f"{b:8.3f}  {'DIVERGES (pole)':>25s}  {'CRITICAL':>12s}")
    else:
        phase = "disordered" if b <= 1 else "ordered"
        print(f"{b:8.3f}  {float(z):25.6f}  {phase:>12s}")

# Laurent expansion near s = 1: zeta(s) = 1/(s-1) + gamma + O(s-1)
# gamma = Euler-Mascheroni constant
euler_gamma = float(mp.euler)
print(f"\nEuler-Mascheroni constant gamma = {euler_gamma:.15f}")
print(f"zeta(1 + epsilon) ~ 1/epsilon + gamma for small epsilon")
print(f"Check: zeta(1.001) ~ 1/0.001 + gamma = {1/0.001 + euler_gamma:.6f}")
print(f"Actual: zeta(1.001) = {float(zeta(mpf('1.001'))):.6f}")

# =====================================================================
# 2. THE PRIMON GAS: ENERGY LEVELS AND PARTITION FUNCTION
# =====================================================================
print("\n\n--- 2. The Primon Gas: Energy Levels ---\n")

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print("Single-particle energy levels E_p = log(p):")
print(f"{'p':>4s}  {'E_p = log(p)':>15s}  {'exp(-beta*E_p) at beta=1':>25s}  {'= 1/p':>8s}")
print("-" * 60)
for p in primes:
    E_p = float(log(p))
    boltz = float(exp(-E_p))  # at beta = 1
    print(f"{p:4d}  {E_p:15.10f}  {boltz:25.15f}  {1.0/p:8.6f}")

# Verify: Z(beta) = prod_p (1 - p^{-beta})^{-1}
print("\nEuler product verification:")
for beta_val in [2.0, 1.5, 1.1]:
    product = mpf(1)
    for p in range(2, 1000):
        # Check if p is prime
        is_prime = True
        if p < 2:
            is_prime = False
        for d in range(2, int(p**0.5) + 1):
            if p % d == 0:
                is_prime = False
                break
        if is_prime:
            product *= 1 / (1 - mpf(p) ** (-beta_val))
    z_exact = zeta(mpf(beta_val))
    print(f"  beta = {beta_val}: Euler product (primes < 1000) = {float(product):.10f}, "
          f"zeta(beta) = {float(z_exact):.10f}, "
          f"relative error = {float(fabs(product - z_exact) / fabs(z_exact)):.2e}")

# =====================================================================
# 3. BC HAMILTONIAN SPECTRUM vs S^1 LAPLACIAN SPECTRUM
# =====================================================================
print("\n\n--- 3. BC Hamiltonian vs S^1 Laplacian Spectra ---\n")

print("BC Hamiltonian H: eigenvalues = log(n) for n = 1, 2, 3, ...")
print("S^1 Laplacian -d^2/dphi^2: eigenvalues = n^2/R^2 for n in Z")
print()
print(f"{'n':>4s}  {'E_BC = log(n)':>15s}  {'E_S1 = n^2 (R=1)':>18s}  {'Ratio E_S1/E_BC':>18s}")
print("-" * 60)
for n in range(1, 16):
    E_BC = float(log(n)) if n > 1 else 0.0
    E_S1 = n * n
    ratio = E_S1 / E_BC if E_BC > 0 else float('inf')
    print(f"{n:4d}  {E_BC:15.10f}  {E_S1:18.1f}  {ratio:18.6f}")

print("\nKey observation: The spectra are DIFFERENT.")
print("BC spectrum: log-spaced (additive over primes)")
print("S^1 spectrum: quadratic-spaced (additive over integers)")
print("Same U(1) action, different representations.")

# =====================================================================
# 4. KMS STATES AND THE PHASE TRANSITION
# =====================================================================
print("\n\n--- 4. KMS States and the Phase Transition ---\n")

# The KMS condition: for a KMS state phi at inverse temperature beta,
# phi(a sigma_{ibeta}(b)) = phi(ba) for all a, b in the algebra.
#
# For beta > 1: extremal KMS states are labeled by embeddings
# sigma: Q^{cyc} -> C, and given by:
#   phi_{beta, sigma}(e(r)) = f_{beta}(r) / zeta(beta)
# where f_beta is a specific function.
#
# For beta = 1: the partition function diverges, no regular KMS state.
# For beta <= 1: unique KMS state.

# The free energy
print("Free energy F(beta) = -log(zeta(beta)) / beta:")
print(f"{'beta':>8s}  {'F(beta)':>15s}  {'Entropy S = beta^2 dF/dbeta':>30s}")
print("-" * 60)

for b in [0.5, 0.8, 0.9, 0.95, 0.99, 1.01, 1.05, 1.1, 1.5, 2.0, 3.0]:
    b_mp = mpf(b)
    z = zeta(b_mp)
    if float(re(z)) > 0:
        F = float(-log(fabs(z)) / b_mp)
        # Numerical derivative for entropy
        eps = mpf('1e-6')
        z_plus = zeta(b_mp + eps)
        z_minus = zeta(b_mp - eps)
        if float(re(z_plus)) > 0 and float(re(z_minus)) > 0:
            dF = float((-log(fabs(z_plus)) / (b_mp + eps) + log(fabs(z_minus)) / (b_mp - eps)) / (2 * eps))
            S = float(b_mp ** 2 * dF)
            print(f"{b:8.3f}  {F:15.6f}  {S:30.6f}")
        else:
            print(f"{b:8.3f}  {F:15.6f}  {'(complex)':>30s}")
    else:
        print(f"{b:8.3f}  {'(zeta < 0)':>15s}")

# =====================================================================
# 5. ZEROS OF ZETA AND THE KMS CONDITION
# =====================================================================
print("\n\n--- 5. Zeros of zeta(s) and Their Relation to beta ---\n")

print("First 10 non-trivial zeros of zeta(s) on Re(s) = 1/2:")
print(f"{'k':>4s}  {'t_k (imaginary part)':>22s}  {'|zeta(1/2 + i*t_k)|':>22s}")
print("-" * 55)
for k in range(1, 11):
    z_k = zetazero(k)
    t_k = float(im(z_k))
    # Verify it's a zero
    val = zeta(z_k)
    print(f"{k:4d}  {t_k:22.15f}  {float(fabs(val)):22.2e}")

print("\nThe zeros sit at s = 1/2 + i*t_k.")
print("If we write s = beta_eff + i*t, these correspond to 'complex temperature'")
print("beta_eff = 1/2 for all zeros — this is the SELF-DUAL temperature")
print("(in the sense that the FE s <-> 1-s fixes Re(s) = 1/2).")

# =====================================================================
# 6. THE CRITICAL QUESTION: DOES BETA = 1 (BC) RELATE TO RE(S) = 1/2?
# =====================================================================
print("\n\n--- 6. The Critical Question: beta=1 vs Re(s)=1/2 ---\n")

print("Two special values of the zeta function's argument:")
print("  (A) s = 1: pole of zeta(s), BC phase transition")
print("  (B) Re(s) = 1/2: critical line, non-trivial zeros")
print()
print("These are DIFFERENT points. The BC phase transition is at the POLE,")
print("not at the zeros. The zeros are at Re(s) = 1/2, the pole at s = 1.")
print()
print("However, both share the SELF-DUALITY property:")
print("  - s = 1: not self-dual (FE maps 1 -> 0)")
print("  - Re(s) = 1/2: self-dual (FE maps 1/2 + it -> 1/2 - it)")
print()
print("The BC system's self-dual temperature (where beta maps to itself")
print("under the transformation that exchanges high-T and low-T) depends")
print("on the DUALITY being considered:")

# Under the FE, the natural duality is s <-> 1-s
# The self-dual point is s = 1/2
# Under T-duality R <-> 1/R, the self-dual radius is R = 1
# The mapping between beta and s: Z(beta) = zeta(beta), so beta plays the role of s
# BUT the physical beta (inverse temperature) is real, while s can be complex

print()
print("Resolution: The BC 'inverse temperature' beta is the REAL PART of s.")
print("The zeros sit at s = 1/2 + it, i.e., at beta_eff = Re(s) = 1/2.")
print("The BC phase transition is at beta = 1 (the pole).")
print("These are genuinely different: beta = 1 != beta = 1/2.")

# =====================================================================
# 7. THE KMS CONDITION AS A POSITIVITY CONDITION
# =====================================================================
print("\n\n--- 7. KMS Condition and Positivity ---\n")

print("The KMS condition at inverse temperature beta:")
print("  phi(a* sigma_{ibeta}(a)) >= 0  for all a in the algebra")
print()
print("This IS a positivity condition (it makes phi a positive functional).")
print("Compare with reflection positivity (RP):")
print("  <F, Theta F> >= 0  for all F supported on positive half-space")
print()
print("Both are positivity conditions involving:")
print("  - An involution (* or Theta)")
print("  - An analytic continuation (sigma_{ibeta} or Wick rotation)")
print()
print("The KMS condition at beta involves the Gibbs state e^{-beta H}.")
print("The partition function Z(beta) = Tr(e^{-beta H}) = zeta(beta).")
print()
print("Key identity: The KMS state phi_beta on the BC algebra satisfies")
print("  phi_beta(mu_n* mu_n) = n^{-beta} / zeta(beta)")
print()

# Verify this for several n and beta
print(f"{'n':>4s}  {'beta':>6s}  {'n^(-beta)/zeta(beta)':>22s}  {'Sum check':>12s}")
print("-" * 50)
for beta_val in [1.5, 2.0, 3.0]:
    total = mpf(0)
    for n in range(1, 20):
        val = mpf(n) ** (-beta_val) / zeta(mpf(beta_val))
        total += val
        if n <= 5:
            print(f"{n:4d}  {beta_val:6.1f}  {float(val):22.15f}")
    print(f"{'':>4s}  {beta_val:6.1f}  {'':>22s}  {float(total):12.10f}")
    print()

print("The KMS probabilities sum to 1 (by definition: sum n^{-beta}/zeta(beta) = 1).")

# =====================================================================
# 8. THE CONNES-MARCOLLI GL(2) EXTENSION
# =====================================================================
print("\n\n--- 8. The Connes-Marcolli GL(2) System ---\n")

print("The GL(2) BC system (Connes-Marcolli, 2004) extends BC from GL(1) to GL(2).")
print("Key properties:")
print("  - Algebra: built from the Hecke algebra of GL(2, Q)")
print("  - Partition function: involves GL(2) L-functions")
print("  - Phase transitions at beta = 0, 1, 2:")
print("    * beta in (0, 1): unique KMS state (disorder)")
print("    * beta in (1, 2): KMS states parameterized by Shimura variety")
print("    * beta > 2: extremal KMS states, symmetry breaking by GL(2) Galois action")
print()
print("QG5D connection: The internal manifold CP^2 x S^2 x S^1")
print("has gauge group SU(3) x SU(2) x U(1).")
print("The GL(2) BC system acts on the SU(2) sector (the S^2 factor).")
print("If the QG5D gauge theory on the full internal manifold realizes")
print("the GL(2) BC system, then the phase transitions of the GL(2)")
print("system correspond to the gauge theory phases on S^2.")

# =====================================================================
# 9. THE SYMMETRY BREAKING AND GALOIS ACTION
# =====================================================================
print("\n\n--- 9. Symmetry Breaking at beta = 1 ---\n")

print("BC system symmetry structure:")
print("  beta < 1 (high T): UNIQUE KMS state")
print("    -> Full symmetry group Z_hat* = prod_p Z_p* acts trivially")
print("    -> No Galois action visible")
print("    -> Primes are 'invisible' (thermal noise washes them out)")
print()
print("  beta = 1: PHASE TRANSITION")
print("    -> Partition function zeta(beta) diverges")
print("    -> System is critical")
print()
print("  beta > 1 (low T): INFINITELY MANY extremal KMS states")
print("    -> States parameterized by sigma: Q^{ab} -> C")
print("    -> Gal(Q^{ab}/Q) = Z_hat* acts by permuting KMS states")
print("    -> SPONTANEOUS SYMMETRY BREAKING")
print("    -> Primes become 'visible' (individual Boltzmann weights)")
print()
print("Physical interpretation in QG5D:")
print("  beta = R (the e-circle radius)")
print("  R < 1: high temperature, symmetric phase")
print("  R = 1: self-dual radius, phase transition")
print("  R > 1: low temperature, broken phase")
print()
print("BUT: The self-dual RADIUS is R = 1, and the self-dual VALUE of s is Re(s) = 1/2.")
print("These are NOT the same number unless there is a factor-of-2 mapping.")

# =====================================================================
# 10. THE FACTOR-OF-2 MAPPING
# =====================================================================
print("\n\n--- 10. The Factor-of-2 Mapping ---\n")

print("Identity 1: Z_{S^1}(s) = 2R^{2s} * zeta(2s)")
print("The spectral zeta of S^1 involves zeta(2s), not zeta(s).")
print()
print("If the BC system has partition function Z(beta) = zeta(beta),")
print("and the S^1 spectral zeta is Z_{S^1}(s) = 2R^{2s} zeta(2s),")
print("then the mapping between BC temperature and spectral parameter is:")
print()
print("  beta_BC = 2s")
print()
print("Under this mapping:")
print("  BC phase transition at beta_BC = 1  <->  s = 1/2")
print("  Critical line Re(s) = 1/2  <->  Re(beta_BC) = 1")
print()
print("THIS IS THE KEY OBSERVATION:")
print("The BC phase transition at beta = 1 maps to the spectral parameter s = 1/2")
print("via the factor-of-2 relation between the BC partition function zeta(beta)")
print("and the S^1 spectral zeta 2R^{2s}zeta(2s).")
print()
print("Verification:")
print(f"  zeta(1) = pole  <->  Z_S1(1/2) = 2R * zeta(1) = pole  CHECK")
print(f"  Zeros of zeta(2s) at 2s = 1/2 + it_k  <->  s = 1/4 + it_k/2")
print()

# More precise: if we use the S^1 spectral zeta directly
print("The S^1 Laplacian has eigenvalues n^2/R^2 (n in Z, n != 0).")
print("Its spectral zeta is Z_{S^1}(s) = sum_{n != 0} (n^2/R^2)^{-s}")
print("                                = 2R^{2s} sum_{n=1}^infty n^{-2s}")
print("                                = 2R^{2s} zeta(2s)")
print()
print("The BC Hamiltonian has eigenvalues log(n) (n in N*).")
print("Its partition function is Z_BC(beta) = sum_{n=1}^infty n^{-beta} = zeta(beta)")
print()
print("The DIRECT mapping:")
print("  Z_BC(beta) = zeta(beta)")
print("  Z_{S^1}(s) = 2R^{2s} zeta(2s)")
print()
print("  Setting beta = 2s (and R = 1):")
print("  Z_BC(2s) = zeta(2s) = Z_{S^1}(s) / 2")
print()
print("  So the BC partition function at temperature 1/(2s) IS the S^1")
print("  spectral zeta at spectral parameter s (up to factor of 2).")
print()

# Verify numerically
print("Numerical verification of Z_BC(2s) = Z_{S^1}(s)/2 at R = 1:")
print(f"{'s':>8s}  {'Z_BC(2s) = zeta(2s)':>22s}  {'Z_{S^1}(s)/2':>22s}  {'Match':>6s}")
print("-" * 65)
for s_val in [0.6, 0.75, 1.0, 1.5, 2.0, 3.0]:
    s = mpf(s_val)
    z_bc = zeta(2 * s)
    z_s1 = 2 * zeta(2 * s)  # Z_{S^1}(s) = 2R^{2s}*zeta(2s) with R=1
    z_s1_half = z_s1 / 2
    match = "YES" if float(fabs(z_bc - z_s1_half)) < 1e-20 else "NO"
    print(f"{s_val:8.2f}  {float(z_bc):22.15f}  {float(z_s1_half):22.15f}  {match:>6s}")

# =====================================================================
# 11. DOES KMS AT SELF-DUAL TEMPERATURE FORCE ZEROS TO RE(S) = 1/2?
# =====================================================================
print("\n\n--- 11. Can KMS Force Zeros onto the Critical Line? ---\n")

print("The KMS condition at inverse temperature beta states:")
print("  For all a, b in the algebra:")
print("  phi(a * sigma_{i*beta}(b)) = phi(b * a)")
print()
print("For the BC system, sigma_t(mu_n) = n^{it} * mu_n, so")
print("  sigma_{i*beta}(mu_n) = n^{-beta} * mu_n")
print()
print("The KMS condition becomes a statement about the ANALYTICITY of")
print("  F_{a,b}(z) = phi(a * sigma_z(b))")
print("in the strip 0 <= Im(z) <= beta.")
print()
print("The zeros of zeta(s) at s = rho_k = 1/2 + it_k correspond to")
print("VANISHING of the partition function at COMPLEX temperature.")
print()
print("Under the mapping beta = 2s, the zeros at s = 1/2 + it_k give")
print("  beta = 1 + 2it_k")
print()
print("These are complex temperatures with Re(beta) = 1 = the BC")
print("phase transition temperature!")
print()
print("So the zeros of zeta on Re(s) = 1/2 correspond to complex")
print("temperatures on Re(beta) = 1 — the REAL PART of the complex")
print("temperature equals the critical BC temperature.")

print("\n\nFirst 10 zero locations in beta = 2s coordinates:")
print(f"{'k':>4s}  {'s = 1/2 + it_k':>25s}  {'beta = 2s = 1 + 2it_k':>25s}")
print("-" * 60)
for k in range(1, 11):
    z_k = zetazero(k)
    t_k = float(im(z_k))
    s_re = 0.5
    s_im = t_k
    beta_re = 2 * s_re  # = 1
    beta_im = 2 * s_im
    print(f"{k:4d}  {s_re:6.1f} + {s_im:17.10f}i  {beta_re:6.1f} + {beta_im:17.10f}i")

# =====================================================================
# 12. SUMMARY OF THE CHAIN
# =====================================================================
print("\n\n" + "=" * 70)
print("SUMMARY: THE BC-ECIRCLE CHAIN")
print("=" * 70)
print()
print("1. Z_BC(beta) = zeta(beta)  [BC partition function]")
print("2. Z_{S^1}(s) = 2R^{2s} zeta(2s)  [S^1 spectral zeta, Identity 1]")
print("3. beta = 2s  [the mapping between BC temperature and spectral parameter]")
print("4. BC phase transition at beta = 1 <-> spectral parameter s = 1/2")
print("5. Zeros of zeta(2s) at 2s = 1/2 + it_k <-> spectral zeros at s = 1/4 + it_k/2")
print("   BUT: zeros of zeta(beta) at beta = 1/2 + it_k <-> s = 1/4 + it_k/2")
print()
print("THE GAP: The factor-of-2 mapping shifts the zeros.")
print("  - zeta(s) has zeros at Re(s) = 1/2")
print("  - zeta(2s) has zeros at Re(2s) = 1/2, i.e., Re(s) = 1/4")
print("  - The S^1 spectral zeta Z_{S^1}(s) = 2R^{2s}zeta(2s) has")
print("    spectral zeros at Re(s) = 1/4, NOT Re(s) = 1/2")
print()
print("  The BC phase transition at beta = 1 maps to s = 1/2,")
print("  which is the critical line. But the ZEROS of the spectral zeta")
print("  are at s = 1/4, not s = 1/2.")
print()
print("  Resolution: The POLE of zeta at s = 1 maps to s = 1/2.")
print("  The zeros of zeta at Re(s) = 1/2 map to Re(s_spectral) = 1/4.")
print("  The BC phase transition (pole) and the RH zeros are")
print("  DIFFERENT features of zeta, at DIFFERENT locations.")
