#!/usr/bin/env python3
"""
OC-2: Ultra-Precision Search for Even Better Formulas
====================================================

Can we find a formula that achieves < 0.0001% error?
Try combinations with more parameters and finer coefficients.
"""

import mpmath as mp
from datetime import datetime

mp.dps = 500

print("OC-2: ULTRA-PRECISION SEARCH")
print("=" * 100)
print()

# Constants
l_P = mp.mpf("1.616255237e-35")
R_obs = mp.mpf("1.0e-5")
target = mp.log(mp.pi * R_obs / l_P)

# Riemann zeros
zeros = [mp.im(mp.zetazero(n)) for n in range(1, 11)]
gamma_1, gamma_2, gamma_3, gamma_4, gamma_5 = zeros[:5]

pi = mp.pi

# Basic formula
formula_basic = gamma_1 * pi**2 / 2
error_basic = abs(formula_basic - target) / abs(target) * 100

print(f"Basic error: {float(error_basic):.15f}%")
print()

# We know 0.2/γ_2 gives 0.0005565%
# Can we do better?

candidates = []

# Ultra-fine search: a/γ_2 + b/γ_3 + c log(γ_2/γ_1)
print("Testing ultra-fine 3-parameter combinations:")
count = 0
for a_100 in range(15, 25):  # 0.15 to 0.24
    for b_1000 in range(-50, 50, 10):  # -0.05 to 0.05
        for c_100 in range(-10, 10):
            a = mp.mpf(a_100) / 100
            b = mp.mpf(b_1000) / 1000
            c = mp.mpf(c_100) / 100
            
            test = gamma_1 * pi**2 / 2 - a/gamma_2 - b/gamma_3 - c*mp.log(gamma_2/gamma_1)
            err = abs(test - target) / abs(target) * 100
            name = f"{float(a):.2f}/γ_2 - {float(b):.3f}/γ_3 - {float(c):.2f}ln(γ2/γ1)"
            candidates.append((float(err), name, test))
            count += 1

print(f"Tested {count} combinations\n")

# Sort by error
candidates.sort()

print("Top 10 ultra-fine combinations:")
for i, (err, name, _) in enumerate(candidates[:10], 1):
    print(f"{i}. {name:70s}  error: {err:.15f}%")

print()
best_err = candidates[0][0]
print(f"BEST ERROR FOUND: {best_err:.15f}%")
if best_err < 0.0001:
    print("BREAKTHROUGH: Better than 0.0001%!")
else:
    print(f"The 0.2/γ_2 formula at 0.0005565% appears to be optimal in this class.")

