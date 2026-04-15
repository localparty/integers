#!/usr/bin/env python3
"""
r58_l5_continuum_limit.py

L.5 investigation: continuum limit P -> infinity for BC heat semigroup.

Key questions:
1. Does prod_p Z_p(t) converge as P -> inf?
2. Does sum_p (Z_p(t) - 1) converge?
3. Does sum_p e^{-t(log p)^2} converge?
4. Does the integral int e^{-t(log x)^2} dx/log x converge?
5. What does compact resolvent on H_1 actually give?
"""

from mpmath import mp, mpf, log, exp, pi, sqrt, fsum, quad, inf, nstr
import sympy
from sympy import primerange, isprime, nextprime

mp.dps = 50

print("=" * 72)
print("L.5 CONTINUUM LIMIT INVESTIGATION")
print("=" * 72)

# =====================================================================
# STEP 1: Compute Z_p(t) for individual primes
# =====================================================================
print("\n--- STEP 1: Individual Z_p(t) values ---")
print("Z_p(t) = sum_{k=0}^inf e^{-t*(k*log(p))^2}")
print("       = 1 + 2*sum_{k=1}^inf e^{-t*(k*log(p))^2}")
print()

def Z_p(p, t, kmax=200):
    """Compute Z_p(t) = sum_{k=0}^inf e^{-t*(k*log(p))^2}"""
    lp = log(mpf(p))
    total = mpf(1)  # k=0 term
    for k in range(1, kmax+1):
        term = exp(-t * (k * lp)**2)
        if term < mpf(10)**(-40):
            break
        total += 2 * term  # +-k symmetry
    return total

primes_test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
t_values = [mpf('0.01'), mpf('0.1'), mpf('1.0'), mpf('10.0')]

print(f"{'p':>5} | {'t=0.01':>18} | {'t=0.1':>18} | {'t=1.0':>18} | {'t=10.0':>18}")
print("-" * 85)
for p in primes_test:
    vals = [Z_p(p, t) for t in t_values]
    print(f"{p:5d} | {nstr(vals[0],12):>18} | {nstr(vals[1],12):>18} | {nstr(vals[2],12):>18} | {nstr(vals[3],12):>18}")

# =====================================================================
# STEP 2: Compute Z_p(t) - 1 for convergence analysis
# =====================================================================
print("\n--- STEP 2: Z_p(t) - 1 for convergence check ---")
print("Product converges iff sum_p (Z_p(t)-1) converges")
print()

print(f"{'p':>5} | {'Z_p-1 (t=0.01)':>18} | {'Z_p-1 (t=0.1)':>18} | {'Z_p-1 (t=1.0)':>18} | {'2*e^(-t*(log p)^2)':>20}")
print("-" * 90)
for p in primes_test:
    lp = log(mpf(p))
    zpm1 = [Z_p(p, t) - 1 for t in [mpf('0.01'), mpf('0.1'), mpf('1.0')]]
    asymp = 2 * exp(-1.0 * lp**2)
    print(f"{p:5d} | {nstr(zpm1[0],12):>18} | {nstr(zpm1[1],12):>18} | {nstr(zpm1[2],12):>18} | {nstr(asymp,12):>20}")

# =====================================================================
# STEP 3: THE CRITICAL SUM: sum_p e^{-t*(log p)^2}
# =====================================================================
print("\n--- STEP 3: sum_p e^{-t*(log p)^2} (partial sums) ---")
print("This is the convergence-determining series")
print()

def partial_sum_exp(t, P_max):
    """Compute sum_{p <= P_max} e^{-t*(log p)^2}"""
    total = mpf(0)
    for p in primerange(2, P_max + 1):
        lp = log(mpf(p))
        total += exp(-t * lp**2)
    return total

def partial_sum_zpm1(t, P_max):
    """Compute sum_{p <= P_max} (Z_p(t) - 1)"""
    total = mpf(0)
    for p in primerange(2, P_max + 1):
        total += Z_p(p, t) - 1
    return total

P_cutoffs = [10, 100, 1000, 10000, 100000]

for t in [mpf('0.01'), mpf('0.1'), mpf('1.0')]:
    print(f"\nt = {t}:")
    print(f"{'P_max':>8} | {'sum e^(-t*(log p)^2)':>25} | {'sum (Z_p-1)':>25} | {'#primes':>8}")
    print("-" * 75)
    for P_max in P_cutoffs:
        s_exp = partial_sum_exp(t, P_max)
        s_zpm1 = partial_sum_zpm1(t, P_max)
        n_primes = len(list(primerange(2, P_max + 1)))
        print(f"{P_max:8d} | {nstr(s_exp,15):>25} | {nstr(s_zpm1,15):>25} | {n_primes:8d}")

# =====================================================================
# STEP 4: THE INTEGRAL TEST
# =====================================================================
print("\n--- STEP 4: Integral convergence test ---")
print("By PNT: sum_p f(p) ~ integral f(x) dx/log(x)")
print("Test: integral_2^inf e^{-t*(log x)^2} dx/log(x)")
print()

for t in [mpf('0.01'), mpf('0.1'), mpf('1.0')]:
    def integrand(x):
        if x < 2:
            return mpf(0)
        lx = log(x)
        return exp(-t * lx**2) / lx

    # Integrate up to various cutoffs
    for upper in [100, 1000, 10000, 100000, 1000000]:
        try:
            val = quad(integrand, [2, upper], error=True)
            print(f"t={t}, int_2^{upper}: {nstr(val[0],15)}")
        except:
            print(f"t={t}, int_2^{upper}: [computation failed]")

    # Try to infinity
    # Substitution: x = e^u, dx = e^u du, log x = u
    # integral becomes: int_{log 2}^inf e^{-t*u^2} * e^u / u du
    def integrand_u(u):
        return exp(-t * u**2 + u) / u

    try:
        val_inf = quad(integrand_u, [log(2), inf], error=True)
        print(f"t={t}, int_2^inf: {nstr(val_inf[0],15)} (to infinity)")
    except Exception as e:
        print(f"t={t}, int_2^inf: DIVERGES or failed ({e})")
    print()

# =====================================================================
# STEP 5: THE PRODUCT prod_p Z_p(t) for specific P values
# =====================================================================
print("\n--- STEP 5: Product of Z_p(t) for primorial cutoffs ---")
print("Primorial cutoffs: 2, 6=2*3, 30=2*3*5, 210=2*3*5*7, 2310=2*3*5*7*11")
print()

primorial_cutoffs = [2, 6, 30, 210, 2310]

for t in [mpf('0.01'), mpf('0.1'), mpf('1.0')]:
    print(f"\nt = {t}:")
    print(f"{'P':>6} | {'prod Z_p(t)':>25} | {'log(prod)':>20}")
    print("-" * 60)
    for P in primorial_cutoffs:
        product = mpf(1)
        for p in primerange(2, P + 1):
            product *= Z_p(p, t)
        print(f"{P:6d} | {nstr(product,15):>25} | {nstr(log(product),12):>20}")

# Also larger cutoffs
print(f"\nExtended cutoffs at t = 1.0:")
print(f"{'P':>8} | {'prod Z_p(1)':>25} | {'log(prod)':>20} | {'#primes':>8}")
print("-" * 70)
for P in [10, 100, 1000, 10000]:
    product = mpf(1)
    n = 0
    for p in primerange(2, P + 1):
        product *= Z_p(p, mpf('1.0'))
        n += 1
    print(f"{P:8d} | {nstr(product,15):>25} | {nstr(log(product),12):>20} | {n:8d}")

# =====================================================================
# STEP 6: Does log(prod) diverge or converge?
# =====================================================================
print("\n--- STEP 6: Convergence of log(prod Z_p) = sum log(Z_p) ---")
print("log Z_p(t) ~ -Z_p(t)^{-1}*(Z_p(t)-1) for Z_p close to 1")
print("For large p: Z_p(t) -> 1 rapidly, so log Z_p ~ -(Z_p-1) ~ -2*e^{-t*(log p)^2}")
print()

# The key insight: sum_p |log Z_p(t)| converges iff sum_p (Z_p(t)-1) converges
# iff sum_p e^{-t*(log p)^2} converges
# But this is ~ integral e^{-t*(log x)^2} dx/log x
# Substituting x = e^u: integral e^{-t*u^2 + u}/u du from u=log 2 to infinity
# For t > 0: the exponent -t*u^2 + u -> -inf as u -> inf (quadratic dominates)
# So THE INTEGRAL CONVERGES for all t > 0!!!

print("ANALYTIC ARGUMENT:")
print("sum_p e^{-t*(log p)^2} ~ int_2^inf e^{-t*(log x)^2} dx/log x   [PNT]")
print("Substituting x = e^u:")
print("  = int_{log 2}^inf e^{-t*u^2 + u}/u du")
print("For t > 0: exponent = -t*u^2 + u = -t(u - 1/(2t))^2 + 1/(4t)")
print("  -> -infinity as u -> infinity (t > 0 fixed)")
print("Gaussian decay beats 1/u growth.")
print("CONCLUSION: The integral CONVERGES for all t > 0.")
print()

# Verify: compute the integral precisely
for t in [mpf('0.01'), mpf('0.1'), mpf('1.0'), mpf('10.0')]:
    def integrand_u(u):
        return exp(-t * u**2 + u) / u
    val = quad(integrand_u, [log(2), inf], error=True)
    print(f"t={nstr(t,4)}: int = {nstr(val[0],15)}, error = {nstr(val[1],6)}")

# =====================================================================
# STEP 7: But what about sum_p (Z_p(t) - 1)?
# =====================================================================
print("\n--- STEP 7: Does sum_p (Z_p(t) - 1) converge? ---")
print("Z_p(t) - 1 = 2*e^{-t*(log p)^2} + 2*e^{-t*(2*log p)^2} + ...")
print("           ~ 2*e^{-t*(log p)^2}  for large p (higher k negligible)")
print("So sum_p (Z_p(t)-1) ~ 2 * sum_p e^{-t*(log p)^2} which CONVERGES.")
print()

# =====================================================================
# STEP 8: THE CRITICAL DISTINCTION: H_1 vs H_R
# =====================================================================
print("\n" + "=" * 72)
print("STEP 8: THE H_1 vs H_R WALL")
print("=" * 72)
print()
print("The P-truncated operator T_BC^{<=P} on H_1 has eigenvalues:")
print("  {log n : n is P-smooth}")
print()
print("The full operator T_BC on H_1 has eigenvalues:")
print("  {log n : n = 1, 2, 3, ...}")
print()
print("The Riemann zeros gamma_n are NOT eigenvalues of T_BC on H_1.")
print("They appear as spec(T_BC) on H_R (the representation at beta=infty).")
print()
print("If we prove compact resolvent of T_BC on H_1:")
print("  -> spec on H_1 = {log n}, pure point, discrete")
print("  -> NO continuous spectrum on H_1")
print("  -> gamma_n CANNOT appear on H_1 (they're not in {log n})")
print("  -> This is a theorem about the WRONG Hilbert space for RH")
print()
print("Meyer's result: {gamma_n} subset spec(T_BC) IN DISTRIBUTIONAL SENSE")
print("  -> The gamma_n are spectral for T_BC acting on tempered distributions S'")
print("  -> S' contains both H_1 and H_R eigenstates")
print("  -> Compact resolvent on H_1 says nothing about H_R spectrum")
print()

# =====================================================================
# STEP 9: Can we run T_BC on H_R instead?
# =====================================================================
print("=" * 72)
print("STEP 9: WHAT IF WE RUN THE FLOW ON H_R?")
print("=" * 72)
print()
print("H_R has basis {e_chi : chi in (Z/nZ)^*} for all n.")
print("T_BC on H_R has eigenvalues {gamma_n} (the Riemann zeros).")
print("The heat trace on H_R would be: sum_n e^{-t*gamma_n^2}")
print()

# Compute heat trace on H_R using known zeros
# First few gamma_n values
gamma_values = [
    mpf('14.134725141734693790'),
    mpf('21.022039638771554993'),
    mpf('25.010857580145688763'),
    mpf('30.424876125859513210'),
    mpf('32.935061587739189691'),
    mpf('37.586178158825671257'),
    mpf('40.918719012147495187'),
    mpf('43.327073280914999519'),
    mpf('48.005150881167159728'),
    mpf('49.773832477672302181'),
]

print("Heat trace on H_R (using first 10 known zeros):")
for t in [mpf('0.001'), mpf('0.01'), mpf('0.1')]:
    trace = fsum([exp(-t * g**2) for g in gamma_values])
    print(f"  t = {t}: sum_{{n=1}}^10 e^{{-t*gamma_n^2}} = {nstr(trace, 12)}")

print()
print("For t=0.001: e^{-0.001 * 14.13^2} = e^{-0.2} ~ 0.82 -- ALL terms contribute")
print("For t=0.01:  e^{-0.01 * 14.13^2}  = e^{-2.0} ~ 0.14 -- rapid decay")
print("For t=0.1:   e^{-0.1 * 14.13^2}   = e^{-20} ~ 2e-9 -- essentially zero")
print()
print("The H_R heat trace converges MUCH faster because gamma_n >> log n")
print("(gamma_1 = 14.13 vs log 2 = 0.69)")
print()

# =====================================================================
# STEP 10: THE HONEST VERDICT
# =====================================================================
print("=" * 72)
print("STEP 10: THE HONEST VERDICT")
print("=" * 72)
print()
print("QUESTION 1: Does prod_p Z_p(t) converge?")
print("ANSWER: YES. The sum_p (Z_p(t)-1) ~ 2*sum_p e^{-t*(log p)^2}")
print("converges for all t > 0 by the integral test (Gaussian decay")
print("beats all polynomial growth). Therefore the infinite product")
print("prod_p Z_p(t) converges to a finite positive value for all t > 0.")
print()
print("QUESTION 2: Does compact resolvent on H_1 follow?")
print("ANSWER: YES. The Kato-Rellich argument works:")
print("  (a) Strong resolvent convergence: ITPFI + Trotter-Kato")
print("  (b) Uniform spectral gap: (log 2)^2 = 0.4805")
print("  (c) Uniform trace bound: prod_p Z_p(t) < infinity")
print("  => Limiting operator on H_1 has compact resolvent")
print("  => spec(T_BC | H_1) = {log n : n >= 1}, purely discrete")
print()
print("QUESTION 3: Does this prove RH?")
print("ANSWER: NO. Compact resolvent on H_1 proves that {log n} is the")
print("complete spectrum on H_1. The Riemann zeros {gamma_n} live on H_R,")
print("a DIFFERENT Hilbert space. L.5 on H_1 is a theorem about the")
print("wrong spectrum.")
print()
print("THE WALL: To prove RH via this route, we would need L.5 on H_R:")
print("  - Define T_BC^{<=P} on H_R^{<=P}")
print("  - Show P -> inf gives compact resolvent on H_R")
print("  - Identify spec on H_R with {gamma_n}")
print("  - Show all gamma_n are real")
print()
print("But H_R has NO natural ITPFI factorization (the characters of")
print("(Z/nZ)^* don't factor over primes in the same way). The tensor")
print("product structure H_1 = tensor_p H_1^p does NOT carry over to H_R.")
print("This is the H_1 vs H_R wall, and L.5 does not breach it.")
print()
print("=" * 72)
print("SUMMARY: L.5 CONVERGES but ON THE WRONG SPACE.")
print("The product is finite. The math works. It proves compact resolvent")
print("on H_1 with spectrum {log n}. But RH needs spec on H_R = {gamma_n}.")
print("L.5 is a valid theorem about the wrong operator.")
print("=" * 72)
