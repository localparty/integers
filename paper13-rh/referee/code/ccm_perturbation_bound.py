"""
CCM Perturbation Bound Computation
====================================
Compute the norm of the perturbation when adding prime p_{N+1}
to the CCM zeta spectral triple, and fit the decay exponent alpha.

Key quantity: ||D(lambda,N+1) - D(lambda,N)|| ~ 1/p^alpha

If alpha > 1/2: sum of ||perturbation||^2 converges -> Kato applies -> RH.
"""

from mpmath import mp, mpf, mpc, log, sqrt, pi, zeta, fabs, re, im, power
from mpmath import zetazero, nstr
import json

mp.dps = 60  # 60 decimal digits

# First 20 primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# First Riemann zero
gamma1 = zetazero(1)
gamma1_im = im(gamma1)  # ~ 14.134725...
s_crit = mpc(mpf('0.5'), gamma1_im)  # s = 1/2 + i*gamma_1

print("=" * 72)
print("CCM PERTURBATION BOUND COMPUTATION")
print("=" * 72)
print()
print(f"gamma_1 = {nstr(gamma1_im, 30)}")
print(f"s = 1/2 + i*gamma_1")
print()

# =====================================================================
# PART (a): |log(1 - p^{-s})| for each prime at s = 1/2 + i*gamma_1
# This is the log-perturbation from adding prime p to the Euler product.
# =====================================================================
print("=" * 72)
print("PART (a): Log-perturbation |log(1 - p^{-s})| at s = 1/2 + i*gamma_1")
print("=" * 72)
print()
print(f"{'p':>5s}  {'|log(1-p^{-s})|':>30s}  {'1/p^{1/2}':>20s}  {'1/p':>20s}  {'ratio to 1/sqrt(p)':>20s}")
print("-" * 100)

log_pert = []
for p in primes:
    p_mp = mpf(p)
    val = -log(1 - power(p_mp, -s_crit))
    absval = fabs(val)
    inv_sqrt_p = 1 / sqrt(p_mp)
    inv_p = 1 / p_mp
    ratio = absval / inv_sqrt_p
    log_pert.append(float(absval))
    print(f"{p:5d}  {nstr(absval, 20):>30s}  {nstr(inv_sqrt_p, 12):>20s}  {nstr(inv_p, 12):>20s}  {nstr(ratio, 12):>20s}")

print()

# =====================================================================
# PART (b): Cumulative Euler product convergence
# zeta_N(s) = prod_{p<=P_N} 1/(1-p^{-s})
# Compare |zeta_N(s)| vs |zeta(s)| at s = 1/2 + i*gamma_1
# (Note: zeta(1/2+i*gamma_1) = 0 by definition)
# =====================================================================
print("=" * 72)
print("PART (b): Cumulative Euler product at s = 1/2 + i*gamma_1")
print("=" * 72)
print()
print(f"{'N':>3s}  {'p_N':>5s}  {'|zeta_N(s)|':>30s}  {'|log zeta_N(s)|':>30s}")
print("-" * 75)

partial_prod = mpc(1, 0)
for i, p in enumerate(primes):
    p_mp = mpf(p)
    factor = 1 / (1 - power(p_mp, -s_crit))
    partial_prod *= factor
    abs_prod = fabs(partial_prod)
    log_abs = log(abs_prod) if abs_prod > 0 else mpf('-inf')
    print(f"{i+1:3d}  {p:5d}  {nstr(abs_prod, 20):>30s}  {nstr(re(log_abs), 15):>30s}")

print()

# Now compare with zeta(s) for s slightly off the critical line
# to check convergence rate
print("=" * 72)
print("PART (b'): Euler product convergence OFF critical line")
print("s = 0.6 + i*gamma_1 (off critical line)")
print("=" * 72)
print()

s_off = mpc(mpf('0.6'), gamma1_im)
zeta_exact = zeta(s_off)
print(f"zeta(0.6 + i*gamma_1) = {nstr(zeta_exact, 25)}")
print(f"|zeta(0.6 + i*gamma_1)| = {nstr(fabs(zeta_exact), 25)}")
print()
print(f"{'N':>3s}  {'p_N':>5s}  {'|zeta_N(s)|':>25s}  {'|zeta_N - zeta|':>25s}  {'rel error':>20s}")
print("-" * 105)

partial_prod = mpc(1, 0)
errors_off = []
for i, p in enumerate(primes):
    p_mp = mpf(p)
    factor = 1 / (1 - power(p_mp, -s_off))
    partial_prod *= factor
    abs_prod = fabs(partial_prod)
    err = fabs(partial_prod - zeta_exact)
    rel = err / fabs(zeta_exact) if fabs(zeta_exact) > 0 else mpf('inf')
    errors_off.append((p, float(err)))
    print(f"{i+1:3d}  {p:5d}  {nstr(abs_prod, 18):>25s}  {nstr(err, 12):>25s}  {nstr(rel, 8):>20s}")

print()

# =====================================================================
# PART (c): Fit the decay exponent alpha
# ||perturbation from p|| ~ c/p^alpha
# Use |log(1-p^{-s})| as the perturbation norm.
# Fit log|pert| = log(c) - alpha * log(p)
# =====================================================================
print("=" * 72)
print("PART (c): Fit perturbation decay exponent alpha")
print("=" * 72)
print()

from mpmath import log as mplog

# Method 1: Consecutive ratios
print("Method 1: Consecutive ratios alpha_ij = log(pert_i/pert_j) / log(p_j/p_i)")
print()
for i in range(len(primes)-1):
    p_i = mpf(primes[i])
    p_j = mpf(primes[i+1])
    pert_i = mpf(log_pert[i])
    pert_j = mpf(log_pert[i+1])
    if pert_j > 0 and pert_i > 0:
        alpha_ij = mplog(pert_i / pert_j) / mplog(p_j / p_i)
        print(f"  p={primes[i]:2d}->p={primes[i+1]:2d}: alpha = {nstr(alpha_ij, 10)}")

print()

# Method 2: Linear regression in log-log space
print("Method 2: Linear regression log|pert| = A - alpha * log(p)")
print()

log_p_vals = [float(mplog(mpf(p))) for p in primes]
log_pert_vals = [float(mplog(mpf(v))) for v in log_pert]

# Manual linear regression
n = len(primes)
sum_x = sum(log_p_vals)
sum_y = sum(log_pert_vals)
sum_xx = sum(x*x for x in log_p_vals)
sum_xy = sum(x*y for x, y in zip(log_p_vals, log_pert_vals))

alpha_fit = -(n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x**2)
log_c_fit = (sum_y + alpha_fit * sum_x) / n
c_fit = float(mp.exp(mpf(log_c_fit)))

print(f"  alpha (all 20 primes) = {alpha_fit:.8f}")
print(f"  c = {c_fit:.8f}")
print()

# Also fit on last 10 primes (large-p behavior)
log_p_vals_tail = log_p_vals[10:]
log_pert_vals_tail = log_pert_vals[10:]
n2 = len(log_p_vals_tail)
sum_x2 = sum(log_p_vals_tail)
sum_y2 = sum(log_pert_vals_tail)
sum_xx2 = sum(x*x for x in log_p_vals_tail)
sum_xy2 = sum(x*y for x, y in zip(log_p_vals_tail, log_pert_vals_tail))

alpha_fit_tail = -(n2 * sum_xy2 - sum_x2 * sum_y2) / (n2 * sum_xx2 - sum_x2**2)
log_c_fit_tail = (sum_y2 + alpha_fit_tail * sum_x2) / n2
c_fit_tail = float(mp.exp(mpf(log_c_fit_tail)))

print(f"  alpha (primes 31-71) = {alpha_fit_tail:.8f}")
print(f"  c = {c_fit_tail:.8f}")
print()

# =====================================================================
# PART (d): The three critical regimes
# =====================================================================
print("=" * 72)
print("PART (d): Convergence analysis for fitted alpha")
print("=" * 72)
print()

alpha = alpha_fit
print(f"Fitted alpha = {alpha:.8f}")
print()

# Sum of 1/p^alpha over primes
print("Partial sums: S_N = sum_{p<=p_N} 1/p^alpha")
partial_sum = mpf(0)
for p in primes:
    partial_sum += 1 / power(mpf(p), mpf(alpha))
    print(f"  p <= {p:3d}: S = {nstr(partial_sum, 15)}")
print()

# Sum of 1/p^{2*alpha} over primes (L^2 condition for Kato)
print(f"Partial sums: S_N = sum_{{p<=p_N}} 1/p^{{2*alpha}} (L^2 / Kato condition)")
partial_sum_sq = mpf(0)
for p in primes:
    partial_sum_sq += 1 / power(mpf(p), 2 * mpf(alpha))
    print(f"  p <= {p:3d}: S = {nstr(partial_sum_sq, 15)}")
print()

# Theoretical analysis
if alpha > 1:
    print(f"REGIME: alpha = {alpha:.4f} > 1")
    print("  => sum 1/p^alpha CONVERGES absolutely (prime zeta converges for Re(s)>1)")
    print("  => sum 1/p^{2alpha} also converges")
    print("  => Kato-Rellich applies DIRECTLY")
    print("  => Strong resolvent convergence GUARANTEED")
elif alpha > 0.5:
    print(f"REGIME: 1/2 < alpha = {alpha:.4f} <= 1")
    print("  => sum 1/p^alpha may diverge (like sum 1/p ~ log log P)")
    print("  => BUT sum 1/p^{2alpha} CONVERGES (2alpha > 1)")
    print("  => L^2 condition for Kato SATISFIED")
    print("  => Strong resolvent convergence via Kato")
else:
    print(f"REGIME: alpha = {alpha:.4f} <= 1/2")
    print("  => BOTH sums diverge")
    print("  => Kato does NOT directly apply")
    print("  => Need cancellation arguments")
print()

# =====================================================================
# PART (e): Rank-one perturbation structure
# =====================================================================
print("=" * 72)
print("PART (e): Rank-one perturbation norms")
print("=" * 72)
print()
print("For rank-one perturbation D(N+1) = D(N) + alpha_p |v_p><w_p|:")
print("  ||perturbation|| = |alpha_p| * ||v_p|| * ||w_p||")
print()
print("In CCM's construction, the Euler factor at prime p gives:")
print("  1/(1-p^{-s}) = 1 + p^{-s} + p^{-2s} + ...")
print()
print("The MULTIPLICATIVE perturbation from adding p is:")
print("  zeta_{N+1}(s) / zeta_N(s) = 1/(1-p^{-s})")
print()
print("The ADDITIVE log-perturbation is:")
print("  log zeta_{N+1} - log zeta_N = -log(1-p^{-s})")
print()
print("At |s| = 1/2: |p^{-s}| = p^{-1/2}, so:")
print("  |-log(1-p^{-s})| ~ p^{-1/2} + O(p^{-1})")
print()
print("BUT the CCM operator perturbation is NOT the log-perturbation.")
print("It is a RANK-ONE perturbation on L^2([lambda^{-1}, lambda]).")
print()
print("The actual operator norm depends on HOW CCM embed the Euler factor")
print("into their spectral triple. Two scenarios:")
print()
print("Scenario A: ||D(N+1)-D(N)|| ~ |log(1-p^{-1/2})| ~ 1/sqrt(p)")
print("  -> alpha = 1/2: BORDERLINE. Kato may not apply directly.")
print()
print("Scenario B: ||D(N+1)-D(N)|| ~ |1-1/(1-p^{-1})| ~ 1/p")
print("  -> alpha = 1: sum 1/p^2 converges. Kato applies cleanly.")
print()

# =====================================================================
# PART (f): The numerical evidence from CCM
# =====================================================================
print("=" * 72)
print("PART (f): What CCM's 10^{-55} precision implies")
print("=" * 72)
print()

# CCM match 50 zeros to 10^-55 with 6 primes (p <= 13)
# If each prime beyond 13 contributes perturbation ~ 1/p^alpha:
# Total tail error ~ sum_{p>13} 1/p^alpha

print("CCM achieve 10^{-55} precision for gamma_1 using primes {2,3,5,7,11,13}.")
print()
print("If the tail error is sum_{p>13} 1/p^alpha, then we need:")
print("  sum_{p>13} 1/p^alpha ~ 10^{-55}")
print()

# For various alpha, compute tail sum over next 100 primes
from sympy import primerange
big_primes = list(primerange(17, 10000))

for alpha_test in [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]:
    tail = sum(1.0 / p**alpha_test for p in big_primes)
    from math import log10
    log_tail = log10(tail) if tail > 0 else float('-inf')
    print(f"  alpha = {alpha_test:5.1f}: sum_{{p>13, p<10000}} 1/p^alpha = {tail:.6e} (log10 = {log_tail:.1f})")

print()
print("To reach 10^{-55} from 6 primes, need alpha >> 10.")
print("BUT: this assumes no cancellations in the operator construction.")
print("The 10^{-55} likely arises from STRUCTURAL reasons (Caratheodory-Fejer")
print("optimization), not from individual perturbation smallness.")
print()

# =====================================================================
# PART (g): The honest decomposition
# =====================================================================
print("=" * 72)
print("PART (g): Honest decomposition of the scaling")
print("=" * 72)
print()

print("The perturbation |log(1-p^{-s})| has TWO components at s=1/2+it:")
print()
print("1. MODULUS: |p^{-s}| = p^{-1/2} (independent of t)")
print("2. PHASE: arg(p^{-s}) = -t*log(p) (depends on t)")
print()
print("Decomposition for each prime:")
print()
print(f"{'p':>5s}  {'|p^{-s}| = p^{-1/2}':>20s}  {'phase = -gamma1*log(p)':>25s}  {'|1-p^{-s}|':>20s}")
print("-" * 75)

for p in primes[:10]:
    p_mp = mpf(p)
    modulus = power(p_mp, mpf('-0.5'))
    phase = -gamma1_im * mplog(p_mp)
    # phase mod 2*pi
    phase_mod = phase - 2 * pi * mp.floor(phase / (2 * pi) + mpf('0.5'))
    one_minus = fabs(1 - power(p_mp, -s_crit))
    print(f"{p:5d}  {nstr(modulus, 12):>20s}  {nstr(phase_mod, 12):>25s}  {nstr(one_minus, 12):>20s}")

print()

# =====================================================================
# PART (h): The DEFINITIVE test: alpha from operator norm vs log norm
# =====================================================================
print("=" * 72)
print("PART (h): Compare operator-norm decay at multiple zeros")
print("=" * 72)
print()

# Check at first 5 zeros
for k in range(1, 6):
    gamma_k = im(zetazero(k))
    s_k = mpc(mpf('0.5'), gamma_k)
    print(f"Zero #{k}: gamma_{k} = {nstr(gamma_k, 20)}")

    log_pert_k = []
    for p in primes:
        p_mp = mpf(p)
        val = -log(1 - power(p_mp, -s_k))
        log_pert_k.append(float(fabs(val)))

    # Fit alpha at this zero
    log_p_v = [float(mplog(mpf(p))) for p in primes]
    log_prt_v = [float(mplog(mpf(v))) for v in log_pert_k]

    n3 = len(primes)
    sx = sum(log_p_v)
    sy = sum(log_prt_v)
    sxx = sum(x*x for x in log_p_v)
    sxy = sum(x*y for x, y in zip(log_p_v, log_prt_v))

    alpha_k = -(n3 * sxy - sx * sy) / (n3 * sxx - sx**2)
    print(f"  Fitted alpha = {alpha_k:.8f}")
    print()

# =====================================================================
# SUMMARY
# =====================================================================
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()
print(f"Fitted alpha (all 20 primes, zero #1): {alpha_fit:.8f}")
print(f"Fitted alpha (primes 31-71, zero #1):  {alpha_fit_tail:.8f}")
print()
print("VERDICT:")
print()
if alpha_fit > 0.5:
    print(f"alpha = {alpha_fit:.4f} > 1/2")
    print("=> The LOG-PERTURBATION satisfies the L^2 condition: sum 1/p^{2alpha} < infty")
    print("=> IF the CCM operator perturbation has the SAME scaling,")
    print("   then Kato-Rellich gives strong resolvent convergence.")
else:
    print(f"alpha = {alpha_fit:.4f}")

print()
print("CRITICAL CAVEAT:")
print("The log-perturbation |log(1-p^{-s})| is NOT the same as the")
print("CCM operator perturbation ||D(N+1) - D(N)||.")
print()
print("The THEORETICAL lower bound on the leading term is:")
print("  |log(1-p^{-s})| >= |p^{-s}| - |p^{-2s}|/2 = p^{-1/2} - p^{-1}/2")
print("  => alpha >= 1/2 (with equality in the leading term)")
print()
print("The UPPER bound is:")
print("  |log(1-p^{-s})| <= |p^{-s}|/(1-|p^{-s}|) = p^{-1/2}/(1-p^{-1/2})")
print("  => alpha <= 1/2 (same leading term)")
print()
print("CONCLUSION: The log-perturbation scales as EXACTLY p^{-1/2} * (1 + O(1/sqrt(p)))")
print("This gives alpha = 1/2 EXACTLY in the leading term.")
print()
print("For the Kato L^2 condition: sum 1/p^{2*1/2} = sum 1/p ~ log log P -> DIVERGES")
print("=> The naive log-perturbation does NOT satisfy Kato's condition.")
print()
print("HOWEVER: The CCM operator perturbation could have DIFFERENT scaling")
print("if the rank-one structure introduces additional p-dependent suppression.")
print("This is the key open question.")
