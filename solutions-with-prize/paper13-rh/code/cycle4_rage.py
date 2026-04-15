"""Cycle 4, Route 1: RAGE theorem return probability computation.

Computes the return probability under BC modular dynamics sigma_t.
Result: |n^{it}|^2 = 1 for all t (trivially pure point for H_mod).
This is IRRELEVANT to T_BC -- see research/04-route1.md.
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

print("RAGE return probability under modular dynamics")
print("sigma_t(mu_n) = n^{it} mu_n")
print()

# Return probability for Hecke vector mu_2
print("Return probability |<sigma_t(mu_2)Omega, mu_2 Omega>|^2 / |<mu_2 Omega>|^4:")
for t in [1, 10, 100, 1000, 10000]:
    amp = mp.power(2, mp.mpc(0, t))
    prob = abs(amp)**2
    print(f"  t = {t:6d}: 2^{{it}} = {mp.nstr(amp, 15)},  |2^{{it}}|^2 = {mp.nstr(prob, 20)}")

print()
print("RAGE integral (1/T) int_0^T |<...|K|...>| dt:")
for T_val in [1, 10, 100, 1000]:
    # K = |mu_2 Omega><mu_2 Omega|, psi = mu_2 Omega
    # <e^{itH}psi, K e^{itH}psi> = |<e^{itH}psi, psi>|^2 * ||psi||^{-2}
    # = |n^{it}|^2 * (phi(n)/n)^2 / (phi(n)/n) = phi(n)/n = 1/2
    # But with K as rank-1 projector onto normalized psi:
    # = |<e^{itH}psi, psi/||psi||>|^2 = (phi(2)/2)^2 * |2^{it}|^2 / (phi(2)/2)
    # = phi(2)/2 = 1/2
    # Actually: <psi, K psi> with K = |hat{psi}><hat{psi}|:
    # = |<psi, hat{psi}>|^2 = ||psi||^2 = phi(2)/2 = 1/2
    # Time-averaged: same constant.
    rage_val = mp.mpf(1)/2
    print(f"  T = {T_val:5d}: (1/T)*integral = {mp.nstr(rage_val, 15)}")

print()
print("VERDICT: Return probability = 1 for all t.")
print("Pure point for H_mod. Trivial and expected.")
print("Does NOT constrain T_BC on H_R. IRRELEVANT to spectral realisation.")
