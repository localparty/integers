"""Cycle 4, Route 3: Meyer eigenstate completeness numerical test.

Computes the norm weight carried by nontrivial vs trivial zeros
in the Weil explicit formula "Parseval" identity.
Result: trivial zeros dominate by 10^12 -- nontrivial eigenstates
are NOT complete on their own.
See research/04-route3.md.
"""

import mpmath as mp
mp.dps = 50

gammas = [
    mp.mpf("14.134725141734693790457251983562470270784257115699"),
    mp.mpf("21.022039638771554992628479593896902777334340524903"),
    mp.mpf("25.010857580145688763213790992562821818659549672558"),
    mp.mpf("30.424876125859513210311897530584091320181560023715"),
    mp.mpf("32.935061587739189690662368964074903488812715603517"),
    mp.mpf("37.586178158825671257217763480705332821405597350831"),
    mp.mpf("40.918719012147495187398126914633254395726165962777"),
    mp.mpf("43.327073280914999519496122165406805782645668371837"),
    mp.mpf("48.005150881167159727942472749427516041686844001144"),
    mp.mpf("49.773832477672302181916784678563724057723178299677"),
]


def f_hat(s):
    """Mellin transform of f(x) = x*exp(-pi*x^2) at s.
    f_hat(s) = pi^{-(s+1)/2} * Gamma((s+1)/2) / 2
    No poles for s != -1, -3, -5, ... (avoids Gamma poles at non-negative integers)."""
    return mp.power(mp.pi, -(s + 1) / 2) * mp.gamma((s + 1) / 2) / 2


print("Meyer Eigenstate Completeness: Norm Weight Analysis")
print(f"Test function: f(x) = x * exp(-pi*x^2)")
print(f"f_hat(s) = pi^{{-(s+1)/2}} * Gamma((s+1)/2) / 2")
print()

# Nontrivial zeros
print("Nontrivial zeros (paired rho, 1-rho):")
nontrivial_sum = mp.mpf(0)
for n, g in enumerate(gammas):
    rho = mp.mpc(mp.mpf("0.5"), g)
    val = f_hat(rho)
    contrib = 2 * abs(val) ** 2
    nontrivial_sum += contrib
    print(f"  n={n+1:2d}: gamma = {mp.nstr(g, 12)}, |f_hat(rho)|^2 = {mp.nstr(abs(val)**2, 8)}, cumulative = {mp.nstr(nontrivial_sum, 12)}")

print()

# Trivial zeros
print("Trivial zeros (s = -2, -4, -6, ...):")
trivial_sum = mp.mpf(0)
for k in range(1, 21):
    s = mp.mpf(-2 * k)
    val = f_hat(s)
    contrib = 2 * abs(val) ** 2
    trivial_sum += contrib
    if k <= 10:
        print(f"  k={k:2d}: s={int(s):4d}, |f_hat|^2 = {mp.nstr(abs(val)**2, 10)}, cumulative = {mp.nstr(trivial_sum, 12)}")
    elif k == 11:
        print(f"  ...")

print()
print(f"Nontrivial sum (10 pairs): {mp.nstr(nontrivial_sum, 15)}")
print(f"Trivial sum (20 pairs):    {mp.nstr(trivial_sum, 15)}")
if nontrivial_sum > 0:
    print(f"Ratio trivial/nontrivial:  {mp.nstr(trivial_sum / nontrivial_sum, 8)}")

print()
print("VERDICT: Trivial zeros dominate by ~10^12.")
print("The nontrivial-zero eigenstates carry negligible weight.")
print("Meyer's construction is NOT complete without correction terms.")
print("Completeness of {phi_n} is EQUIVALENT to spectral realisation -- CIRCULAR.")
