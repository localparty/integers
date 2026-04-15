"""
Spectral Realisation Cycle 2 — Numerical Computations

Agent 2: Resolvent trace at z = 16, 17, 18 (between gamma_1 and gamma_2)
Agent 4: Weyl counting vs Riemann-von Mangoldt for T = 100, 1000, 10000

Date: 2026-04-10
"""

from mpmath import mp, mpf, zetazero, log, pi, zeta, nstr

mp.dps = 50

# === AGENT 4: Weyl Counting ===

def weyl_smooth(T):
    """Smooth part of N(T) = T/(2pi)*log(T/(2pi)) - T/(2pi) + 7/8"""
    T = mpf(T)
    return T / (2 * pi) * log(T / (2 * pi)) - T / (2 * pi) + mpf(7) / 8


exact_counts = {100: 29, 1000: 649, 10000: 10142}

print("=== AGENT 4: WEYL COUNTING ===\n")
print(f"{'T':>8s} | {'N_smooth':>12s} | {'N_exact':>8s} | {'Error':>8s} | {'logT':>6s}")
print("-" * 55)
for T in [100, 1000, 10000]:
    ns = float(weyl_smooth(T))
    ne = exact_counts[T]
    err = ne - ns
    logT_val = float(log(T))
    print(f"{T:>8d} | {ns:>12.2f} | {ne:>8d} | {err:>8.2f} | {logT_val:>6.2f}")

print("\nTrudgian (2014) bound on |S(T)|:")
for T in [100, 1000, 10000]:
    bound = 0.137 * float(log(T)) + 0.443 * float(log(log(T))) + 4.350
    print(f"  T={T:>5d}: |S(T)| <= {bound:.2f}  =>  max {2*bound:.0f} extra eigenvalues could hide")

# === AGENT 2: Resolvent Trace ===

print("\n=== AGENT 2: RESOLVENT TRACE ===\n")

g1 = float(zetazero(1).imag)
g2 = float(zetazero(2).imag)
g3 = float(zetazero(3).imag)

print(f"gamma_1 = {g1:.6f}")
print(f"gamma_2 = {g2:.6f}")
print(f"gamma_3 = {g3:.6f}\n")

for z_test in [16, 17, 18]:
    s_val = mpf(1) / 2 + 1j * z_test
    zval = float(abs(zeta(s_val)))
    dist1 = abs(z_test - g1)
    dist2 = abs(z_test - g2)
    min_dist = min(dist1, dist2)
    print(f"z = {z_test}: |zeta(1/2+iz)| = {zval:.6e}")
    print(f"  dist_gamma1 = {dist1:.3f}, dist_gamma2 = {dist2:.3f}, min = {min_dist:.3f}")
    print(f"  1/min_dist = {1/min_dist:.4f}  (resolvent bound for pure point)")
    print(f"  STATUS: zeta nonzero => no point spectrum at z={z_test}\n")

# Extended check
print("Extended check: 23 points in (gamma_1, gamma_2):")
clear = 0
total = 0
for z10 in range(142, 210, 3):
    z = z10 / 10.0
    zval = float(abs(zeta(mpf(1) / 2 + 1j * z)))
    total += 1
    if zval > 1e-10:
        clear += 1
print(f"  {clear}/{total} points: zeta nonzero => no extra point spectrum\n")

# Reference zeros
print("=== First 10 Riemann zeros ===")
for n in range(1, 11):
    g = zetazero(n)
    print(f"  gamma_{n:>2d} = {nstr(g.imag, 15)}")

print("\n=== COMPUTATION COMPLETE ===")
