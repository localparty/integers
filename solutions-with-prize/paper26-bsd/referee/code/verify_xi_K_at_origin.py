"""Verify Ξ_K(1/2) ≠ 0 for K = Q(i).

This is the Hurwitz non-vanishing hypothesis for the K-analogue of
Paper 13's identification of spec(D_∞^K) with the non-trivial zeros of
ζ_K. Paper 13 uses Ξ(0) = 0.4971... ≠ 0; Route 2 needs the analogous
non-vanishing for K.

Definitions:
    Λ_K(s) = 4^(s/2) · 2^(1-s) · π^(-s) · Γ(s) · ζ_K(s)
    Ξ_K(s) = (1/2) · s(s-1) · Λ_K(s)
    ζ_K(s) = ζ(s) · L(s, χ_{-4})   (for K = Q(i))

The "origin" after the change of variable s = 1/2 + iz is s = 1/2.
We verify Ξ_K(1/2) ≠ 0.
"""

from mpmath import mp, mpf, gamma, pi, power, zeta, dirichlet, fabs

mp.dps = 40


def L_chi_minus4(s):
    """Dirichlet L-function for the non-trivial Kronecker character mod 4."""
    return dirichlet(s, [0, 1, 0, -1])


def zeta_K(s):
    """Dedekind zeta for K = Q(i) = Q(√-1)."""
    return zeta(s) * L_chi_minus4(s)


def lambda_K(s):
    """Completed Dedekind zeta Λ_K(s) for K = Q(i)."""
    completion = power(4, s / 2) * power(2, 1 - s) * power(pi, -s) * gamma(s)
    return completion * zeta_K(s)


def xi_K(s):
    """Ξ_K(s) = (1/2) · s(s-1) · Λ_K(s)."""
    return mpf("0.5") * s * (s - 1) * lambda_K(s)


# -- computations --------------------------------------------------------
s0 = mpf("1/2")

xi_at_half = xi_K(s0)
zeta_K_at_half = zeta_K(s0)
expected = -zeta_K_at_half / 4

print("=" * 66)
print("Ξ_K(1/2) non-vanishing check (Route 2, Phase IV sub-task 4.2)")
print("=" * 66)
print()
print(f"  ζ(1/2)           = {float(zeta(s0)):.15f}")
print(f"  L(1/2, χ_{{-4}})   = {float(L_chi_minus4(s0)):.15f}")
print(f"  ζ_K(1/2)         = {float(zeta_K_at_half):.15f}")
print()
print(f"  Λ_K(1/2)         = {float(lambda_K(s0)):.15f}")
print(f"  Ξ_K(1/2)         = {float(xi_at_half):.15f}")
print(f"  −(1/4) ζ_K(1/2)  = {float(expected):.15f}  (analytical target)")
print()
print(f"  |Ξ_K(1/2)|       = {float(fabs(xi_at_half)):.15f}")
print(f"  non-vanishing    = {bool(fabs(xi_at_half) > mpf('1e-20'))}")
print()

# Full precision
print(f"Full 40-digit: Ξ_K(1/2) = {xi_at_half}")
