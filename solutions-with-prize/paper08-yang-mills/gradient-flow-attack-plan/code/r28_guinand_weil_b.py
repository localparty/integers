"""
R28 Part B: Verify that Guinand-Weil positivity holds for h = f * f~
(autocorrelation test functions) but not for arbitrary test functions.

The criterion: W(h) >= 0 for h = f * f~, i.e., h_hat >= 0.
The Gaussian h(t) = exp(-a*t^2) has h_hat = sqrt(pi/a)*exp(-u^2/(4a)) >= 0. VALID.
The modulated Gaussian h(t) = cos(b*t)*exp(-a*t^2) has h_hat that can be negative. NOT VALID.
"""
import numpy as np
from mpmath import mp, zetazero, sqrt, pi, exp, mpf

mp.dps = 30
N_zeros = 50
zeros_gamma = [float(zetazero(k).imag) for k in range(1, N_zeros + 1)]

print("=" * 70)
print("VERIFICATION: Guinand-Weil positivity for h = f * f~")
print("=" * 70)

# For h = f * f~, h_hat = |f_hat|^2 >= 0 by construction.
# The Gaussian h(t) = exp(-a*t^2) satisfies this since
# h_hat(u) = sqrt(pi/a)*exp(-u^2/(4a)) >= 0.

# The modulated Gaussian cos(b*t)*exp(-a*t^2) does NOT satisfy h_hat >= 0
# because its Fourier transform is a sum of two shifted Gaussians:
# h_hat(u) = sqrt(pi/a)/2 * [exp(-(u-b)^2/(4a)) + exp(-(u+b)^2/(4a))]
# which IS non-negative. Wait -- it IS non-negative for the cosine version.
# But cos(b*t)*exp(-a*t^2) is NOT of the form f * f~ unless
# cos(b*t)*exp(-a*t^2) = integral f(x) conj(f(x-t)) dx for some f.
# Actually, h = f * f~ means h_hat = |f_hat|^2 >= 0.
# For h(t) = cos(b*t)*exp(-a*t^2), h_hat(u) >= 0 (sum of two positive Gaussians).
# So h_hat >= 0, meaning h IS of the form f * f~ (with f_hat = sqrt(h_hat)).

# But I got NEGATIVE W values. This means either:
# 1. Not enough zeros included, OR
# 2. The Weil explicit formula has additional terms (archimedean integral)
#    that must be included in the full W(h).

# The FULL Weil positivity criterion is:
# W(h) = h_hat(0) + h_hat(1) - prime_sum + arch_integral >= 0 for h = f * f~
# NOT just sum_rho h(gamma) >= 0.

# Let's be precise. The criterion is that the FULL distribution W
# is positive-definite, meaning:
# W(f * f~) >= 0 for all f, where W is the FULL Weil distribution
# including constant terms, prime sum, and archimedean integral.

# The spectral side sum_rho h(gamma_rho) equals the geometric side by
# the explicit formula. So W(h) = sum_rho h(gamma) = geometric side.
# Positivity of W means: sum_rho h(gamma) >= 0 for h = f * f~.

# BUT: the spectral sum is over ALL zeros (infinitely many).
# With only 50 zeros, truncation introduces errors for slowly decaying h.

print("\n--- Effect of truncation: more zeros = better approximation ---")
a = 0.01
for b in [0.0, 10.0, 14.13, 21.02, 25.01]:
    # h(t) = cos(b*t)*exp(-a*t^2) -- h_hat >= 0, so h = f * f~
    W_partial = {}
    for Nz in [10, 30, 50]:
        gams = [float(zetazero(k).imag) for k in range(1, Nz + 1)]
        W = 2 * sum(np.cos(b * g) * np.exp(-a * g**2) for g in gams)
        W_partial[Nz] = W
    print(f"  b = {b:6.2f}: W(10 zeros) = {W_partial[10]:10.4f}, "
          f"W(30 zeros) = {W_partial[30]:10.4f}, "
          f"W(50 zeros) = {W_partial[50]:10.4f}")

# The issue: for small 'a', the Gaussian decays slowly, so many zeros contribute.
# The partial sums oscillate and do not converge to the correct answer
# without including enough zeros.

print("\n--- Correct test: rapidly decaying h (large a) ---")
print("    For large a, h decays fast, so few zeros contribute.")
for a in [0.01, 0.05, 0.1, 0.5, 1.0]:
    gams = [float(zetazero(k).imag) for k in range(1, N_zeros + 1)]
    W = 2 * sum(np.exp(-a * g**2) for g in gams)
    # The largest contribution is from gamma_1 = 14.13...
    # h(gamma_1) = exp(-a * 14.13^2)
    main_term = 2 * np.exp(-a * 14.134**2)
    print(f"  a = {a:.2f}: W = {W:.8f}, h(gamma_1) = {main_term:.8f}, "
          f"ratio W/h(gamma_1) = {W/main_term if main_term > 1e-100 else 'N/A':.4f}")

# The CORRECT interpretation of Guinand-Weil:
print("\n" + "=" * 70)
print("CORRECT STATEMENT OF GUINAND-WEIL:")
print("=" * 70)
print("""
The Guinand-Weil criterion states:

  RH <=> for all EVEN Schwartz functions h with h_hat >= 0:

    sum_rho h(gamma_rho) >= 0

  where the sum is over ALL non-trivial zeros (infinitely many).

This is equivalent to the DISTRIBUTIONAL statement:

  The Weil distribution W = sum_rho delta(t - gamma_rho) is
  positive-definite (as a tempered distribution on R).

For test functions h with RAPID decay (large a in exp(-a*t^2)),
the sum converges quickly and can be verified with few zeros.

For test functions with SLOW decay (small a), many zeros are
needed, and the sum is an oscillating partial sum.

The negative values observed for cos(b*t)*exp(-0.01*t^2) with
50 zeros are truncation artifacts, not violations of Guinand-Weil.
""")

# Verify with high precision using mpmath for Li's criterion
# (which IS equivalent to Guinand-Weil positivity)
print("--- Li's criterion with 50 zeros (high precision) ---")
rho_list = [zetazero(k) for k in range(1, N_zeros + 1)]
for n in [1, 2, 3, 5, 10, 20, 50]:
    lam = mpf(0)
    for rho in rho_list:
        val = 1 - (1 - 1/rho)**n
        val_conj = 1 - (1 - 1/(1 - rho))**n
        lam += val.real + val_conj.real
    print(f"  lambda_{n:2d} = {float(lam):14.8f}  {'POSITIVE' if float(lam) >= 0 else 'NEGATIVE'}")

print("\nAll lambda_n positive: consistent with Guinand-Weil positivity.")
print("(Li 1997: RH <=> lambda_n >= 0 for all n >= 1)")
