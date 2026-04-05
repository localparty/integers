#!/usr/bin/env python3
"""
Final numerical solution: self-consistent stabilization with cross-coupled
two-loop corrections.

Physical setup: S1 radius R is fixed first (by Scherk-Schwarz / Casimir).
Then r_2 and r_3 stabilize via one-loop (log) + two-loop (1/r^8) balance,
where the two-loop coefficient for each modulus depends on the OTHER radius
through the complementary volume.

For S2 sector (at fixed r_3):
  V_S(r_2) = -(N_S/2)/r_2^4 * [2*B_S*ln(r_2) + A_S] + c2_S(r_3)/r_2^8

For CP2 sector (at fixed r_2):
  V_C(r_3) = -(N_C/2)/r_3^4 * [2*B_C*ln(r_3) + A_C] + c2_C(r_2)/r_3^8

where:
  c2_S(r_3) = K * Z_S(0)^2 / r_3^8
  c2_C(r_2) = K * Z_C(0)^2 * beta / r_2^4

K absorbs alpha_GS, G_10, and volume normalization.
beta = ratio of volume prefactors.
"""

import numpy as np
from scipy.optimize import brentq, fsolve

# =============================================================================
# SPECTRAL DATA
# =============================================================================
B_S = 8.0/315.0          # Z_S2(-2) = 8/315
B_C = 313.0/5040.0       # Z_CP2(-2) = 313/5040
A_S = 0.0407366640        # Z'_S2(-2)
A_C = 0.1488836780        # Z'_CP2(-2)
Z_S0 = -2.0/3.0          # Z_S2(0)
Z_C0 = -119.0/120.0      # Z_CP2(0)
N_S = 52
N_C = 53
alpha_GS = 209.0/2880.0

# Volume prefactors
# Vol(S2) = 4*pi*r_2^2, Vol(CP2) = (8*pi^2/3)*r_3^4
# G_eff for S2 sector = G_10/Vol(CP2) where G_10 = G_11/(2*pi*R) is fixed
# G_eff for CP2 sector = G_10/Vol(S2)
#
# c2_S = alpha_GS * [G_10/Vol(CP2)]^2 * Z_S(0)^2 / (16*pi^2)^2
#       = alpha_GS * G_10^2 * Z_S(0)^2 / [(8*pi^2/3)^2 * r_3^8 * (16*pi^2)^2]
#       = [alpha_GS * G_10^2 / (16*pi^2)^2] * Z_S(0)^2 / [(8*pi^2/3)^2 * r_3^8]
#
# c2_C = [alpha_GS * G_10^2 / (16*pi^2)^2] * Z_C(0)^2 / [(4*pi)^2 * r_2^4]
#
# Define kappa = alpha_GS * G_10^2 / (16*pi^2)^2 (free parameter)
# c2_S = kappa * Z_S(0)^2 / [(8*pi^2/3)^2 * r_3^8]
# c2_C = kappa * Z_C(0)^2 / [(4*pi)^2 * r_2^4]

VCP2_norm = (8.0*np.pi**2/3.0)**2  # = (8*pi^2/3)^2
VS2_norm = (4.0*np.pi)**2           # = 16*pi^2

def compute_lambda(u, B, A):
    """Two-loop fraction at the minimum."""
    P = 2.0*B*u + A
    Q = 4.0*P - 2.0*B
    if P <= 0 or Q <= 0:
        return float('nan')
    return Q / (4.0*P + 2.0*B)

def solve_coupled(kappa):
    """
    Solve the coupled system:
    r_2^4 * Q_S(r_2) = 16 * kappa * Z_S(0)^2 / (N_S * VCP2_norm * r_3^8)
    r_3^4 * Q_C(r_3) = 16 * kappa * Z_C(0)^2 / (N_C * VS2_norm * r_2^4)

    Use log variables u2 = ln(r_2), u3 = ln(r_3).
    """
    def equations(uv):
        u2, u3 = uv
        Q_S = 8.0*B_S*u2 + 4.0*A_S - 2.0*B_S
        Q_C = 8.0*B_C*u3 + 4.0*A_C - 2.0*B_C
        if Q_S <= 0 or Q_C <= 0:
            return [1e20, 1e20]

        # Use log form to avoid overflow:
        # ln(r_2^4 * Q_S) = ln(16*kappa*Z_S^2) - ln(N_S*VCP2) - 8*u3
        # 4*u2 + ln(Q_S) = ln(16*kappa*Z_S^2/(N_S*VCP2)) - 8*u3
        lnRHS_S = np.log(16.0*kappa*Z_S0**2 / (N_S * VCP2_norm))
        lnRHS_C = np.log(16.0*kappa*Z_C0**2 / (N_C * VS2_norm))

        eq1 = 4.0*u2 + np.log(Q_S) - lnRHS_S + 8.0*u3
        eq2 = 4.0*u3 + np.log(Q_C) - lnRHS_C + 4.0*u2
        return [eq1, eq2]

    # Minimum u values (Q > 0 condition)
    u2_min = 0.25 - A_S/(2.0*B_S)  # = -0.552
    u3_min = 0.25 - A_C/(2.0*B_C)  # = -0.949

    best_sol = None
    best_res = 1e20

    for u2_init in np.linspace(u2_min + 0.01, 2.0, 10):
        for u3_init in np.linspace(u3_min + 0.01, 2.0, 10):
            try:
                sol = fsolve(equations, [u2_init, u3_init], full_output=True)
                x, info, ier, msg = sol
                if ier == 1:
                    u2, u3 = x
                    Q_S = 8.0*B_S*u2 + 4.0*A_S - 2.0*B_S
                    Q_C = 8.0*B_C*u3 + 4.0*A_C - 2.0*B_C
                    if Q_S > 0 and Q_C > 0 and u2 > u2_min and u3 > u3_min:
                        residual = np.max(np.abs(info['fvec']))
                        if residual < best_res:
                            best_res = residual
                            best_sol = (u2, u3)
            except:
                pass

    return best_sol, best_res

# =============================================================================
# SCAN OVER kappa
# =============================================================================
print("=" * 80)
print("COUPLED STABILIZATION: SCAN OVER TWO-LOOP STRENGTH kappa")
print("=" * 80)
print(f"\n{'kappa':>12s} | {'r_2':>8s} | {'r_3':>8s} | {'rho':>8s} | "
      f"{'(4/3)rho^2':>10s} | {'3r2^2/(2pi*r3^4)':>16s} | {'lam_S':>6s} | {'lam_C':>6s}")
print("-" * 100)

scan_results = []
for log_k in np.linspace(-4, 16, 400):
    kappa = np.exp(log_k)
    sol, res = solve_coupled(kappa)
    if sol is not None and res < 1e-8:
        u2, u3 = sol
        r2, r3 = np.exp(u2), np.exp(u3)
        rho = r2/r3
        alpha_approx = (4.0/3.0)*rho**2
        alpha_exact = (3.0/(2.0*np.pi))*r2**2/r3**4
        lam_S = compute_lambda(u2, B_S, A_S)
        lam_C = compute_lambda(u3, B_C, A_C)
        scan_results.append((kappa, r2, r3, rho, alpha_approx, alpha_exact, lam_S, lam_C, u2, u3))

# Print every 40th result
for row in scan_results[::40]:
    k, r2, r3, rho, aa, ae, ls, lc, u2, u3 = row
    print(f"{k:12.4e} | {r2:8.4f} | {r3:8.4f} | {rho:8.5f} | {aa:10.6f} | {ae:16.6f} | {ls:6.4f} | {lc:6.4f}")

# =============================================================================
# FIND alpha_3/alpha_2 = 1.0 (using BOTH formulas)
# =============================================================================
print("\n" + "=" * 80)
print("SEARCHING FOR alpha_3/alpha_2 = 1.0")
print("=" * 80)

# Using (4/3)*rho^2 formula
alphas_approx = [r[4] for r in scan_results]
print(f"\n(4/3)*rho^2 formula: range [{min(alphas_approx):.4f}, {max(alphas_approx):.4f}]")

for i in range(len(scan_results)-1):
    if (scan_results[i][4]-1.0)*(scan_results[i+1][4]-1.0) < 0:
        print("  Crossing found!")
        # Bisect on kappa
        k1, k2 = scan_results[i][0], scan_results[i+1][0]
        for _ in range(80):
            km = np.sqrt(k1*k2)  # geometric mean
            sol, res = solve_coupled(km)
            if sol is None or res > 1e-8:
                km = (k1+k2)/2
                sol, res = solve_coupled(km)
            if sol is None:
                break
            u2, u3 = sol
            rho_m = np.exp(u2-u3)
            alpha_m = (4.0/3.0)*rho_m**2
            if alpha_m > 1.0:
                k1 = km
            else:
                k2 = km
        sol, res = solve_coupled(km)
        if sol:
            u2, u3 = sol
            r2, r3 = np.exp(u2), np.exp(u3)
            rho = r2/r3
            lam_S = compute_lambda(u2, B_S, A_S)
            lam_C = compute_lambda(u3, B_C, A_C)
            alpha_exact = (3.0/(2.0*np.pi))*r2**2/r3**4
            print(f"\n  SOLUTION (approx formula):")
            print(f"    kappa = {km:.6e}")
            print(f"    r_2 = {r2:.10f},  r_3 = {r3:.10f}")
            print(f"    rho = {rho:.10f}")
            print(f"    (4/3)*rho^2 = {(4.0/3.0)*rho**2:.10f}")
            print(f"    (3/(2pi))*r2^2/r3^4 = {alpha_exact:.10f}")
            print(f"    lambda_S2 = {lam_S:.10f}")
            print(f"    lambda_CP2 = {lam_C:.10f}")
        break
else:
    print(f"  No crossing for (4/3)*rho^2 in scanned range.")

# Using (3/(2pi))*r2^2/r3^4 formula
alphas_exact = [r[5] for r in scan_results]
print(f"\n(3/(2pi))*r2^2/r3^4 formula: range [{min(alphas_exact):.4f}, {max(alphas_exact):.4f}]")

for i in range(len(scan_results)-1):
    if (scan_results[i][5]-1.0)*(scan_results[i+1][5]-1.0) < 0:
        print("  Crossing found!")
        k1, k2 = scan_results[i][0], scan_results[i+1][0]
        for _ in range(80):
            km = np.sqrt(k1*k2)
            sol, res = solve_coupled(km)
            if sol is None or res > 1e-8:
                km = (k1+k2)/2
                sol, res = solve_coupled(km)
            if sol is None:
                break
            u2, u3 = sol
            r2, r3 = np.exp(u2), np.exp(u3)
            alpha_m = (3.0/(2.0*np.pi))*r2**2/r3**4
            if alpha_m > 1.0:
                k1 = km
            else:
                k2 = km
        sol, res = solve_coupled(km)
        if sol:
            u2, u3 = sol
            r2, r3 = np.exp(u2), np.exp(u3)
            rho = r2/r3
            lam_S = compute_lambda(u2, B_S, A_S)
            lam_C = compute_lambda(u3, B_C, A_C)
            print(f"\n  SOLUTION (exact formula):")
            print(f"    kappa = {km:.6e}")
            print(f"    r_2 = {r2:.10f},  r_3 = {r3:.10f}")
            print(f"    rho = {rho:.10f}")
            print(f"    (4/3)*rho^2 = {(4.0/3.0)*rho**2:.10f}")
            print(f"    (3/(2pi))*r2^2/r3^4 = {(3.0/(2.0*np.pi))*r2**2/r3**4:.10f}")
            print(f"    lambda_S2 = {lam_S:.10f}")
            print(f"    lambda_CP2 = {lam_C:.10f}")
        break
else:
    print(f"  No crossing for exact formula in scanned range.")

# =============================================================================
# COMPREHENSIVE RESULTS TABLE
# =============================================================================
print("\n" + "=" * 80)
print("COMPREHENSIVE RESULTS")
print("=" * 80)

# Model B: pure log stabilization (kappa -> 0)
u2_log = 0.25 - A_S/(2.0*B_S)
u3_log = 0.25 - A_C/(2.0*B_C)
r2_log, r3_log = np.exp(u2_log), np.exp(u3_log)
rho_log = r2_log/r3_log

print(f"\nModel B (pure one-loop log stabilization, no two-loop):")
print(f"  r_2 = {r2_log:.6f},  r_3 = {r3_log:.6f}")
print(f"  rho = {rho_log:.6f}")
print(f"  (4/3)*rho^2 = {(4.0/3.0)*rho_log**2:.6f}")
print(f"  (3/(2pi))*r2^2/r3^4 = {(3.0/(2.0*np.pi))*r2_log**2/r3_log**4:.6f}")

# Baseline: Z(-2) ratio only
rho4_base = 128.0/313.0
rho_base = rho4_base**0.25
print(f"\nBaseline (Z(-2) ratio only, etc/14c):")
print(f"  (r_2/r_3)^4 = 128/313 = {rho4_base:.6f}")
print(f"  rho = {rho_base:.6f}")
print(f"  (4/3)*rho^2 = {(4.0/3.0)*rho_base**2:.6f}")

# Model A from etc/15
R0 = Z_S0**2 * N_C * B_C / (Z_C0**2 * N_S * B_S)
rho_A = R0**0.25
print(f"\nModel A (full self-consistent, etc/15 Section 3.7):")
print(f"  R0 = {R0:.6f}")
print(f"  rho = {R0**0.25:.6f}")
print(f"  (4/3)*rho^2 = {(4.0/3.0)*R0**0.5:.6f}")

# The physical prediction from the coupled system
if scan_results:
    # The prediction depends on kappa (the two-loop coupling strength).
    # The THEORY predicts kappa, but we don't know it a priori.
    # Report the prediction AS A FUNCTION of lambda.
    print(f"\n{'='*80}")
    print(f"PREDICTION AS A FUNCTION OF TWO-LOOP FRACTION lambda")
    print(f"{'='*80}")
    print(f"\n{'lambda_S':>8s} | {'lambda_C':>8s} | {'rho':>10s} | {'(4/3)rho^2':>12s} | {'(3/2pi)r2^2/r3^4':>16s}")
    print("-" * 70)
    for row in scan_results[::20]:
        k, r2, r3, rho, aa, ae, ls, lc, u2, u3 = row
        print(f"{ls:8.4f} | {lc:8.4f} | {rho:10.6f} | {aa:12.6f} | {ae:16.6f}")

    # Summary
    print(f"\n{'='*80}")
    print(f"FINAL SUMMARY")
    print(f"{'='*80}")
    print(f"""
The coupling ratio alpha_3/alpha_2 depends on the two-loop coupling strength kappa.

Using the approximate formula (4/3)*rho^2:
  Range: {min(alphas_approx):.4f} to {max(alphas_approx):.4f}

Using the exact formula (3/(2*pi))*r_2^2/r_3^4:
  Range: {min(alphas_exact):.4f} to {max(alphas_exact):.4f}

Key finding: The two formulas give DIFFERENT results because they
correspond to different normalizations. The (4/3)*rho^2 formula is
the correct one for the gauge coupling ratio in the KK framework
(see etc/13). The (3/(2*pi))*r_2^2/r_3^4 formula requires knowing
the absolute scale.

For the (4/3)*rho^2 formula, the baseline prediction is:
  Baseline (no log, Z(-2) only):  alpha_3/alpha_2 = 0.853
  Pure log (Model B):              alpha_3/alpha_2 = {(4.0/3.0)*rho_log**2:.3f}
  Full Model A:                    alpha_3/alpha_2 = {(4.0/3.0)*R0**0.5:.3f}

The models where rho is determined by the coupled V_1/V_2 balance give
alpha_3/alpha_2 in the range [{min(alphas_approx):.3f}, {max(alphas_approx):.3f}].

For alpha_3/alpha_2 = 1.0, we need rho^2 = 3/4 = 0.75, i.e., rho = {np.sqrt(0.75):.6f}.
This requires r_2 < r_3, which occurs when the one-loop log dominates
(since the log stabilization gives r_2 < r_3 for the spectral data of S^2 vs CP^2).

HOWEVER: The baseline formula (4/3)*sqrt(128/313) = 0.853 actually gives
rho = (128/313)^{{1/4}} = {(128.0/313.0)**0.25:.6f} < 1, meaning r_2 < r_3.
The coupled system consistently gives rho > 1 (r_2 > r_3).

The discrepancy is because the baseline uses a DIFFERENT stabilization model
(r^4 ~ c_1 from one-loop, without the log) while the coupled system
uses the full log + two-loop balance.
""")

# Determine what lambda gives alpha = 1.0 in the interpolation scheme of etc/15
print("=" * 80)
print("INTERPOLATION (etc/15 Section 4.2)")
print("=" * 80)
print("""
From etc/15, the interpolation between baseline and Model A:
  rho^4 = (128/313)^(1-lambda) * R0^lambda

For alpha_3/alpha_2 = (4/3)*rho^2 = 1, need rho^2 = 3/4, rho^4 = 9/16.
""")

# Solve: (128/313)^(1-lam) * R0^lam = 9/16
# ln(128/313)*(1-lam) + ln(R0)*lam = ln(9/16)
# ln(128/313) + [ln(R0) - ln(128/313)]*lam = ln(9/16)
# lam = [ln(9/16) - ln(128/313)] / [ln(R0) - ln(128/313)]

ln_base = np.log(128.0/313.0)
ln_R0 = np.log(R0)
ln_target = np.log(9.0/16.0)

lam_interp = (ln_target - ln_base) / (ln_R0 - ln_base)
rho4_check = (128.0/313.0)**(1-lam_interp) * R0**lam_interp
alpha_check = (4.0/3.0) * rho4_check**0.5

print(f"lambda_interp = {lam_interp:.10f}")
print(f"Check: rho^4 = {rho4_check:.10f} (should be 0.5625)")
print(f"Check: alpha = {alpha_check:.10f} (should be 1.0)")
print(f"\nThis corresponds to: lambda = {lam_interp:.4f} ({100*lam_interp:.1f}% two-loop contribution)")
print(f"i.e., {100*(1-lam_interp):.1f}% one-loop dominated, {100*lam_interp:.1f}% two-loop dominated")

# What rho values from the coupled scan give alpha = 1?
print(f"\nFrom the coupled system scan, rho ranges [{min([r[3] for r in scan_results]):.4f}, {max([r[3] for r in scan_results]):.4f}]")
print(f"For alpha = 1, need rho = {np.sqrt(0.75):.6f}")
print(f"The coupled system ALWAYS gives rho > 1, so alpha > 4/3 = {4.0/3.0:.4f}")
print(f"The coupled system CANNOT reach alpha = 1.0 in the (4/3)*rho^2 formula.")
print(f"\nThe alpha = 1.0 solution from etc/15 requires lambda = {lam_interp:.4f}")
print(f"which is an interpolation between the baseline (rho < 1) and Model A (rho > 1).")
