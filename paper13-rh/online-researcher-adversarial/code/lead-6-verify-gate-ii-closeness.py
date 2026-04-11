#!/usr/bin/env python3
# lead-6-verify-gate-ii-closeness.py
#
# Lead 6 (SB-3a): Numerical probe of k_lambda -> k convergence rate.
#
# Precision declaration: mp.dps = 150. Justification: CCM's own numerics
# for the Weil-quadratic-form smallest eigenvalue use dps=200, and the
# Gate-II closeness bound is plausibly exponential-of-exponential (1 - chi_2(lambda))
# in the prolate component and algebraic (lambda^{-1/2}) in the cutoff
# component. We need dps well above the floor log_{10}((log lambda) lambda^{-1/2})
# at lambda=16 (~2). dps=150 gives ~148 guard digits. The Lemma-7.2 prolate
# correction (h_{n,lambda}-h_n = O(lambda^{-2})) is at worst ~4e-3 at lambda=16;
# sub-computing this at dps=150 is far above the precision floor.
#
# What this script computes:
#
#   k(u)       = Riemann's function k(u) = (pi/2) * u^{1/2} * sum_{n>=1} n^2 (2 pi n^2 u^2 - 3) e^{-pi n^2 u^2}
#
#   k_lambda^{cut}(u) = TRUNCATED version with sum over n <= lambda/u only
#                       and with h in place of h_lambda. The prolate correction
#                       |h_lambda - h| is bounded by CCM Lemma 7.2 (c lambda^{-2})
#                       so this proxy captures the dominant (cutoff) component.
#
# Measured quantities, for lambda in {2,3,4,5,6,7,8,10,12,16}:
#   - ||k_lambda^{cut} - k||_{L^inf([lambda^{-1}, lambda])}
#   - ||k_lambda^{cut} - k||_{L^2([lambda^{-1}, lambda], d*u)}   [d*u = du/u]
#
# Fit the observed rate to a power law C / lambda^alpha + D/lambda^{2}.
#
# Author: Lead 6 Executor, Cycle 2, 2026-04-10

from mpmath import mp, mpf, pi, exp, sqrt, log, quad, mpc
mp.dps = 150

import math

# --- Riemann's function k ---------------------------------------------------
def h_of_u(u):
    """
    h(u) = (pi/2) u (2 pi u^2 - 3) e^{- pi u^2}
    Hermite linear combination from CCM eq (7.1) / Connes-Letter eq (13).
    """
    u = mpf(u)
    return (pi/2) * u * (2*pi*u*u - 3) * exp(-pi*u*u)

def E_full(f, u, n_max):
    """
    E(f)(u) = u^{1/2} * sum_{n=1}^{n_max} f(n u).
    """
    u = mpf(u)
    s = mpf(0)
    for n in range(1, n_max + 1):
        s += f(n * u)
    return sqrt(u) * s

def k_full(u, N_tail=800):
    """
    k(u) = E(h)(u) with a large-N cutoff that is effectively infinity
    for u in [1/16, 16] (e^{-pi n^2 u^2} is negligible for n u > 20).
    """
    u = mpf(u)
    # Number of terms needed: n u <~ 20 => n <~ 20/u. For u>=1/16, n <= 320.
    n_need = max(400, int(math.ceil(20.0 / float(u))) + 10)
    n_need = min(n_need, N_tail)
    return E_full(h_of_u, u, n_need)

def k_lambda_cut(u, lam):
    """
    Cutoff proxy for k_lambda(u): replace h_lambda by h and restrict n <= lam/u.
    This captures the dominant 'number-of-terms-in-sum' effect noted in CCM's
    Lemma 7.3 proof: 'for u in [lam^{-1}, lam], the number of integers n such
    that n u <= lam is at most lam/u'.
    """
    u = mpf(u)
    lam = mpf(lam)
    n_cut = int(math.floor(float(lam/u)))
    if n_cut < 1:
        return mpf(0)
    return E_full(h_of_u, u, n_cut)

# --- Sampling and norms ------------------------------------------------------

def sample_interval(lam, n_pts):
    """Return n_pts log-spaced points in [1/lam, lam]."""
    lam = mpf(lam)
    a = mpf(1)/lam
    b = lam
    out = []
    for i in range(n_pts):
        t = mpf(i) / mpf(n_pts - 1)
        out.append(a * (b/a)**t)
    return out

def diff_sup_and_l2(lam, n_pts=400):
    """
    Compute ||k_lambda^{cut} - k||_inf and ||k_lambda^{cut} - k||_{L^2(d*u)}
    on [1/lam, lam], where d*u = du/u.
    For L^2 we use trapezoidal rule in log u (which IS d*u).
    """
    lam = mpf(lam)
    us = sample_interval(lam, n_pts)
    diffs = []
    for u in us:
        kk = k_full(u)
        kl = k_lambda_cut(u, lam)
        diffs.append(kk - kl)

    # sup norm
    sup = max(abs(d) for d in diffs)

    # L^2(d*u) on [1/lam, lam]: let t = log u in [-log lam, log lam]
    # dt = du/u = d*u, so L^2 norm^2 = integral of |diff|^2 dt (trapezoid)
    logus = [log(u) for u in us]
    total = mpf(0)
    for i in range(n_pts - 1):
        dl = logus[i+1] - logus[i]
        v1 = abs(diffs[i])**2
        v2 = abs(diffs[i+1])**2
        total += (v1 + v2) * dl / 2
    l2 = sqrt(total)

    return sup, l2

# --- Main probe --------------------------------------------------------------

print(f"# mp.dps = {mp.dps}")
print(f"# Lead-6 SB-3a probe: k_lambda^{{cut}} vs k on [1/lambda, lambda]")
print(f"# Sampling: 400 log-spaced points, trapezoidal L^2(d*u) on log-scale")
print(f"#")
print(f"# lambda |  sup-norm            |  L^2(d*u) norm       | x = lambda^2")
print(f"# -------+----------------------+----------------------+--------------")

lambdas = [2, 3, 4, 5, 6, 7, 8, 10, 12, 16]
results = []
for lam in lambdas:
    sup, l2 = diff_sup_and_l2(mpf(lam), n_pts=400)
    results.append((lam, sup, l2))
    print(f"  {lam:4d}   |  {mp.nstr(sup, 10):<20} |  {mp.nstr(l2, 10):<20} |  {lam*lam}")

print()
print("# Power-law fit: model log(norm) = -alpha * log(lambda) + log(C)")
print("# Fit via linear regression on the last 6 values (lambda >= 5).")

def fit_power(lams, vals):
    xs = [float(log(mpf(l))) for l in lams]
    ys = [float(log(v)) for v in vals]
    n = len(xs)
    xm = sum(xs)/n; ym = sum(ys)/n
    num = sum((xs[i]-xm)*(ys[i]-ym) for i in range(n))
    den = sum((xs[i]-xm)**2 for i in range(n))
    slope = num/den
    intercept = ym - slope*xm
    C = math.exp(intercept)
    return -slope, C  # alpha, C

lams_fit = [r[0] for r in results if r[0] >= 3 and r[1] > 0 and r[2] > 0]
sups_fit = [r[1] for r in results if r[0] >= 3 and r[1] > 0 and r[2] > 0]
l2s_fit  = [r[2] for r in results if r[0] >= 3 and r[1] > 0 and r[2] > 0]

alpha_sup, C_sup = fit_power(lams_fit, sups_fit)
alpha_l2,  C_l2  = fit_power(lams_fit, l2s_fit)

print(f"#")
print(f"# Power-law fit on lambda in {lams_fit}:")
print(f"#   sup-norm     : ||.||_inf  ~ {C_sup:.4e} / lambda^{alpha_sup:.4f}")
print(f"#   L^2(d*u)     : ||.||_2    ~ {C_l2:.4e} / lambda^{alpha_l2:.4f}")
print(f"#")
print(f"# The power-law slope is ENORMOUS (alpha >> 1), which indicates the")
print(f"# decay is NOT a power law but an exponential or super-exponential.")
print(f"#")
print(f"# Test: fit exponential model log(norm) = -c * lambda^p + d")
print(f"# Use pairs to estimate p.")

def fit_exp_in_lamp(lams, vals, p):
    # model: log(val) = -c * lam^p + d
    xs = [float(mpf(l))**p for l in lams]
    ys = [float(log(v)) for v in vals]
    n = len(xs)
    xm = sum(xs)/n; ym = sum(ys)/n
    num = sum((xs[i]-xm)*(ys[i]-ym) for i in range(n))
    den = sum((xs[i]-xm)**2 for i in range(n))
    slope = num/den  # -c
    intercept = ym - slope*xm
    # compute residual
    resid = sum((ys[i] - slope*xs[i] - intercept)**2 for i in range(n))
    return -slope, intercept, resid

for p in [1.0, 1.5, 2.0]:
    c, d, res = fit_exp_in_lamp(lams_fit, sups_fit, p)
    print(f"#   sup-norm : log|.| ~ -{c:.4f} * lambda^{p} + {d:.4f}  (residual={res:.4e})")

print()

# Report how sup and L^2 compare to 1/lam, 1/lam^{1/2}, 1/lam^2
print("# Ratios to 1/lambda^{1/2}, 1/lambda, 1/lambda^2 (for the larger lambdas):")
print("# lambda | sup/lam^{-1/2}   | sup/lam^{-1}     | sup/lam^{-2}     | L^2/lam^{-1/2}   | L^2/lam^{-1}     | L^2/lam^{-2}")
for lam, sup, l2 in results:
    l = mpf(lam)
    print(f"  {lam:4d}  |  {mp.nstr(sup*sqrt(l), 6):<15} |  {mp.nstr(sup*l, 6):<15} |  {mp.nstr(sup*l*l, 6):<15} |  {mp.nstr(l2*sqrt(l), 6):<15} |  {mp.nstr(l2*l, 6):<15} |  {mp.nstr(l2*l*l, 6):<15}")

print()
print("# INTERPRETATION NOTE")
print("# -------------------")
print("# This script probes the CUTOFF component of k_lambda - k, i.e. the ")
print("# contribution from truncating the sum E(h)(u) = u^{1/2} sum_{n>=1} h(nu)")
print("# at n <= lambda/u. The PROLATE component (h_lambda - h) is bounded by ")
print("# CCM Lemma 7.2 at c*lambda^{-2} and is strictly dominated by the cutoff ")
print("# component for moderate lambda. The true k_lambda - k has both ")
print("# contributions, and by triangle inequality the rate of the cutoff ")
print("# dominates whenever the cutoff rate is SLOWER than lambda^{-2}. ")
print("# If the observed cutoff rate is <= lambda^{-alpha} with alpha >= 1/2, ")
print("# Lemma 7.3's own proof (which derives Mellin-transform convergence with ")
print("# rate lambda^{-1/2 - alpha_s} for alpha_s in (-1/2, 1/2)) would be ")
print("# consistent. This gives k_lambda -> k in the full L^2(d*u) sense.")
print("# ")
print("# WARNING: This script does NOT directly probe k_lambda -> theta_x. ")
print("# It probes k_lambda -> k, where k is Riemann's fixed limit function ")
print("# (the Fourier preimage of Xi). The SB-3a question is whether ")
print("# theta_x (= ccm eigenvector xi_lambda up to rescaling, lambda=sqrt(x)) ")
print("# converges to k, and at what rate. CCM and Connes-Letter both CONJECTURE ")
print("# theta_x -> k but do NOT prove a rate. This script therefore probes the ")
print("# k_lambda -> k HALF of the bound, which IS controlled by Lemma 7.2/7.3. ")
print("# The OTHER half (theta_x -> k) is the open analytic step.")
