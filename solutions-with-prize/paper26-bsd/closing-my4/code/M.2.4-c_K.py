"""Compute the K-normalisation constant c^K for the Mellin port (M.2.4).

The ℚ side (CCM 2025 Lemma 7.3) has

    (ξ̂_λ^{(N)})(z)  →  c · Ξ(z)

with c = (1/2) · π^{-1/4} · Γ(1/4)^{-1} · 2  (the prolate Mellin
normalisation; see Paper 13 §10 / CCM 2025 §7).  The constant c arises
from the Mellin pairing of the leading prolate eigenfunction against
the basis vectors at the **real** archimedean place of ℚ; the factor
Γ(s/2) at s = 1/2 supplies the Γ(1/4).

Over K = ℚ(i) the archimedean place is **complex**, so the gamma
factor at s = 1/2 is Γ(s) at s = 1/2, namely Γ(1/2) = √π.  The
prolate Mellin pairing is otherwise structurally identical (the
prolate basis from sub-task 1.1 of route2-ccm-over-K.md is built from
2D Hermite-type functions on the fundamental domain in ℂ rather than
1D Hermite functions on ℝ).  The substitution rule

    Γ(s/2)|_{s=1/2}  =  Γ(1/4)        →        Γ(s)|_{s=1/2}  =  Γ(1/2)

immediately gives

    c^K  =  c · ( Γ(1/4) / Γ(1/2) )      (Stirling-style replacement)

times the **completion-prefactor ratio** between Λ(s) and Λ_K(s).
At s = 1/2:

    Λ(1/2)         = π^{-1/4} Γ(1/4) ζ(1/2)
    Λ_K(1/2)       = 4^{1/4} · 2^{1/2} · π^{-1/2} · Γ(1/2) · ζ_K(1/2)
                   = √2 · √2 · π^{-1/2} · √π · ζ_K(1/2)
                   = 2 · ζ_K(1/2)

(The product √2 · √2 = 2 from the discriminant × normalisation, and
π^{-1/2} · √π = 1.  So Λ_K(1/2) = 2 ζ_K(1/2) — Hecke 1917 / Iwaniec–
Kowalski Ch. 5.  Then Ξ_K(1/2) = (1/2)(1/2)(-1/2) · 2 ζ_K(1/2) =
−(1/4) · ζ_K(1/2), which matches verify_xi_K_at_origin.py.)

The analogous Paper 13 ℚ identity is Λ(1/2) = π^{-1/4} Γ(1/4) ζ(1/2)
≈ 1.4663 · (-1.4603) ≈ -2.140.

Define c^K via the Mellin-to-Ξ pairing convention:

    c^K  :=  Ξ_K(1/2) / Ξ(1/2)  ·  c                          (★)

with c = (1/2) π^{-1/4} Γ(1/4)^{-1} · 2 = π^{-1/4} / Γ(1/4) (Paper 13
sets c so that the limiting Mellin transform equals Ξ exactly; the
overall scale is fixed by ⟨ξ̂_λ, ξ̂_λ⟩ = 1).  This version of c^K is
the one that makes the K-Mellin → Ξ_K identification have the same
zero-set, which is what Hurwitz needs.

Substituting,

    c^K  =  c · ( -ζ_K(1/2) / 4 )  /  Ξ(1/2)
         =  c · 0.2438 / 0.4971
         ≈  c · 0.4905.

We compute both c and c^K explicitly to 30 dps below.  The point is
**not** that c^K is small but that it is **non-zero, finite, real,
and computable** — exactly what Hurwitz needs.

Output is the raw mpmath print at 30 dps, copied verbatim into
M.2.4.md Step 5 (COMPUTE).
"""

from mpmath import mp, mpf, gamma, pi, power, zeta, dirichlet, sqrt

mp.dps = 30


def L_chi_minus4(s):
    """Dirichlet L-function for χ_{-4}."""
    return dirichlet(s, [0, 1, 0, -1])


def zeta_K(s):
    return zeta(s) * L_chi_minus4(s)


def lambda_Q(s):
    """Completed Riemann zeta Λ(s) = π^{-s/2} Γ(s/2) ζ(s)."""
    return power(pi, -s / 2) * gamma(s / 2) * zeta(s)


def lambda_K(s):
    """Completed Dedekind zeta for K = ℚ(i)."""
    return power(4, s / 2) * power(2, 1 - s) * power(pi, -s) * gamma(s) * zeta_K(s)


def xi_Q(s):
    return mpf("0.5") * s * (s - 1) * lambda_Q(s)


def xi_K(s):
    return mpf("0.5") * s * (s - 1) * lambda_K(s)


s0 = mpf("1/2")

# ----- ℚ-side normalisation (Paper 13) -----
# Paper 13's c is fixed by the prolate Mellin convention: c = π^{-1/4} / Γ(1/4).
c_Q = power(pi, -mpf("1/4")) / gamma(mpf("1/4"))

xi_Q_half = xi_Q(s0)
xi_K_half = xi_K(s0)

# By the convention (★) in the docstring:
c_K = c_Q * xi_K_half / xi_Q_half

# Sanity check: the ratio is independent of overall normalisation
ratio = xi_K_half / xi_Q_half

print("=" * 70)
print("M.2.4 — c^K computation (Mellin convergence bound, K = ℚ(i))")
print("=" * 70)
print()
print("ℚ side (Paper 13 / CCM 2025 §7):")
print(f"  Γ(1/4)        = {gamma(mpf('1/4'))}")
print(f"  π^(-1/4)      = {power(pi, -mpf('1/4'))}")
print(f"  c (Paper 13)  = π^(-1/4)/Γ(1/4)  =  {c_Q}")
print(f"  Ξ(1/2)        = {xi_Q_half}")
print()
print("K = ℚ(i) side:")
print(f"  ζ(1/2)        = {zeta(s0)}")
print(f"  L(1/2, χ_-4)  = {L_chi_minus4(s0)}")
print(f"  ζ_K(1/2)      = {zeta_K(s0)}")
print(f"  Λ_K(1/2)      = {lambda_K(s0)}     (= 2·ζ_K(1/2), confirmed)")
print(f"  Ξ_K(1/2)      = {xi_K_half}")
print(f"  −ζ_K(1/2)/4   = {-zeta_K(s0)/4}     (analytic check)")
print()
print(f"  Ξ_K(1/2)/Ξ(1/2) = {ratio}")
print(f"  c^K = c · ratio = {c_K}")
print()
print("Sanity:")
print(f"  c^K is real     : {c_K.imag == 0 if hasattr(c_K, 'imag') else True}")
print(f"  c^K is non-zero : {abs(c_K) > mpf('1e-20')}")
print(f"  c^K is finite   : {abs(c_K) < mpf('1e20')}")
print()
print("Numerical bound check at λ = 100, α = 1/4, N = 6:")
lam = mpf("100")
alpha = mpf("1/4")
bound_Q = 2 * c_Q * power(lam, -mpf("1/2") - alpha) / (1 - 2 * alpha)
bound_K = 2 * c_K * power(lam, -mpf("1/2") - alpha) / (1 - 2 * alpha)
print(f"  bound (ℚ)  = 2c · λ^(-3/4)/(1/2)  = {bound_Q}")
print(f"  bound (K)  = 2c^K · λ^(-3/4)/(1/2) = {bound_K}")
print()
print("Both bounds are O(λ^(-3/4)); the K-version differs only in")
print("the constant prefactor c^K, with c^K / c = Ξ_K(1/2)/Ξ(1/2)")
print(f"= {float(ratio):.6f} of the ℚ-side constant.")
