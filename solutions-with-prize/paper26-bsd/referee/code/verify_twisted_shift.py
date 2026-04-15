"""Verify |Δc^ψ(δ, θ)| < 1/k on all four rows of the corrected bridge table.

For each row (k, N), sweep δ ∈ (0, 1/2) and θ ∈ [0, 2π), and check that
|Δc^ψ(δ, θ)| = |1 − e^{iθ} N^{−2δ}| / |N − e^{iθ} N^{−2δ}| < 1/k.
"""

from mpmath import mpf, mpc, exp, log, pi, fabs, mp

mp.dps = 30


def delta_c_twisted(N, delta, theta):
    x = exp(-2 * delta * log(N))
    psi = exp(mpc(0, theta))
    num = 1 - psi * x
    den = N - psi * x
    return fabs(num / den)


rows = [(2, 13), (3, 13), (4, 41), (6, 29)]
n_theta = 360
n_delta = 50

print(f"{'k':>3} {'N':>4} {'max |Δc^ψ|':>16} {'1/k':>14} {'ok':>5}")
print("-" * 50)
for k, N in rows:
    bound = mpf(1) / k
    max_val = mpf(0)
    argmax = None
    for i in range(1, n_delta):
        delta = mpf(i) / (2 * (n_delta + 1))  # δ ∈ (0, ~0.5)
        for j in range(n_theta):
            theta = 2 * pi * j / n_theta
            v = delta_c_twisted(N, delta, theta)
            if v > max_val:
                max_val = v
                argmax = (float(delta), float(theta))
    ok = max_val < bound
    print(
        f"{k:>3} {N:>4} {float(max_val):>16.10f} "
        f"{float(bound):>14.10f} {'✓' if ok else '✗'}"
    )
    if not ok:
        print(f"    argmax at δ ≈ {argmax[0]:.4f}, θ ≈ {argmax[1]:.4f}")

print()
print("If all four rows show ✓, the twisted integrality argument holds.")
