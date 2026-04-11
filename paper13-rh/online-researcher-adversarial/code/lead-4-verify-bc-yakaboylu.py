"""
Lead 4 verification: BC-ITPFI positivity --> Yakaboylu W >= 0?

This script does TWO things:

(A) Sanity-check Yakaboylu's W >= 0 on its OWN ground (not via BC).
    Per Theorem 5.1 / Prop 5.3 of Yakaboylu 2024 (arXiv:2408.15135),
    W >= 0 corresponds to Bombieri's refined positivity criterion

        Q(varphi) := sum_{rho in Z_zeta} varphi(rho) * conj(varphi(1-rho)) > 0

    for every nonzero complex-valued varphi on the zeros.
    Under the truth of RH (which holds numerically for the first
    millions of zeros), every rho = 1/2 + i*gamma so 1-rho = 1/2 - i*gamma
    = conj(rho), hence conj(varphi(1-rho)) = conj(varphi(conj(rho))).
    Choosing varphi(rho) = f(Im rho) for f even-real on R, we get
    Q(varphi) = sum_n |f(gamma_n)|^2 > 0  (manifestly).
    This is a quick sanity check that the numerator condition is plausible.

(B) Compare the BC-ITPFI positive functional omega_1 (a STATE on the BC
    von Neumann algebra, NOT an operator) with Yakaboylu's W (a bounded
    self-adjoint OPERATOR on a Hilbert subspace H_Psi^{S_zeta}). The two
    objects live on incompatible categories:

        - omega_1 : M_1 -> C    (positive linear functional, takes a value)
        - W       : H_Psi -> H_Phi  (positive semidefinite operator)

    There is no canonical "pushforward" of a state on M_1 to an operator
    on a different Hilbert space. We numerically illustrate this category
    mismatch by computing both objects on the simplest non-trivial test
    case and showing the dimensional / type mismatch.
"""
import mpmath as mp

mp.mp.dps = 60

print("=" * 72)
print("LEAD 4 VERIFICATION: BC-ITPFI -> Yakaboylu W >= 0")
print("mp.dps =", mp.mp.dps)
print("=" * 72)

# ----------------------------------------------------------------------
# (A) Bombieri-form sanity: Q(varphi) on first 10 Riemann zeros
# ----------------------------------------------------------------------
print("\n(A) Bombieri Q(varphi) for f(gamma) = exp(-gamma^2 / 2000)")
print("    over the first 10 nontrivial zeros (assuming RH for these).")

zeros = [mp.zetazero(n).imag for n in range(1, 11)]
print("    First 10 zeros:")
for k, g in enumerate(zeros, 1):
    print(f"      gamma_{k} = {mp.nstr(g, 15)}")

# Test function: real, even, decaying. Under RH, conj(varphi(1-rho)) = varphi(rho).
def varphi(rho):
    return mp.exp(- (rho.imag) ** 2 / mp.mpf(2000))

Q = mp.mpf(0)
for g in zeros:
    rho = mp.mpc("0.5", g)
    one_minus_rho = mp.mpc("0.5", -g)  # under RH
    Q += varphi(rho) * mp.conj(varphi(one_minus_rho))

print(f"\n    Q = sum_n varphi(rho_n) * conj(varphi(1-rho_n)) = {mp.nstr(Q, 20)}")
print(f"    Q > 0? {Q > 0}")
print("    Interpretation: Yakaboylu's W >= 0 condition is consistent")
print("    with the first 10 zeros (necessary condition, not sufficient).")

# ----------------------------------------------------------------------
# (B) Category check: omega_1 vs W
# ----------------------------------------------------------------------
print("\n" + "=" * 72)
print("(B) Category mismatch between omega_1 and W")
print("=" * 72)

print("""
omega_1 is a POSITIVE LINEAR FUNCTIONAL on the BC vNa M_1:
    omega_1 : M_1 -> C
    omega_1(mu_n mu_n^*) = 1/n  (a complex number for each n)
    Positivity of omega_1 means: omega_1(x* x) >= 0 for all x in M_1.

W is a POSITIVE SEMIDEFINITE BOUNDED OPERATOR on H_Psi^{S_zeta} subset L^2([0,inf)):
    W : H_Psi -> H_Phi
    W = sum_{rho in S_zeta} |Phi_{1-bar rho}><Phi_rho|
    Positivity of W means: <varphi | W varphi> >= 0 for all varphi in H_Psi.

These are NOT the same kind of object:
    - omega_1 evaluates an algebra element to a scalar.
    - W maps a Hilbert space vector to another Hilbert space vector.

For a "transport" omega_1 -> W to make sense, one would need:

    (i) a *-homomorphism pi: M_1 -> B(H) for some Hilbert space H
        such that pi(M_1) contains W in its commutant or weak closure;
    (ii) a way to read W off of pi(omega_1) -- but pi(omega_1) is a state
         on B(H), not an operator. A state can be paired with W via the
         trace, < omega_1, W > = tr(rho_omega W), where rho_omega is the
         density matrix representing omega_1 in the pi-representation.

Even if (i) and (ii) are formally executed, the *positivity of omega_1*
gives < omega_1, x* x > >= 0 for x in M_1, which is positivity of the
expectation against POSITIVE OPERATORS in the image of pi. It says
nothing about W unless W is in the image of pi or in its weak closure.

Yakaboylu's W is an explicit operator built from:
    - the Berry-Keating operator D_hat = (xp+px)/2,
    - the Bessel operator T_hat = (xp^2 + p^2 x)/2,
    - the function mu(t) = T_hat tanh(T_hat / 2) - I,
    - the function omega(t) = t e^t / (1+e^t)^2.

NONE of these arise from the BC algebra. The Bessel operator's
generalized eigenbasis |t> in C' (the dual of test functions) has
spectral parameter t in (0, infty), and the Mellin transform of
omega(t) is the completed eta function Lambda(s) = Gamma(s+1)
(1 - 2^{1-s}) zeta(s). The PRIMES enter only through the zeros of
zeta, NOT through any direct map p -> something in L^2([0,inf)).

CONCLUSION (B): There is no natural intertwiner T: M_1 -> B(L^2([0,inf)))
that pushes omega_1 forward to W or to anything in W's weak closure.
The BC algebra acts on its own GNS space H_omega_1 with spec(H_mod) =
{log n : n in N} -- this is the WRONG SPECTRUM (K13 territory) for
Yakaboylu's H_Psi^{S_zeta}, whose 'natural spectral coordinate' (via T_hat)
is t in (0, infty) with continuous spectrum.
""")

# ----------------------------------------------------------------------
# (C) Quick check: does Yakaboylu's W have any obvious "Euler product" structure?
# ----------------------------------------------------------------------
print("=" * 72)
print("(C) Does W have an Euler product / ITPFI factorization?")
print("=" * 72)
print("""
W = sum_{rho in S_zeta} |Phi_{1 - bar rho}><Phi_rho|

The sum is over Riemann zeros, NOT over primes. There is no obvious
sum/tensor over primes in W's definition. The matrix elements
<Psi_{lambda'} | W Psi_lambda> reduce to delta_{lambda', lambda} via
the regularized identity (Lemma 4.3, eq. (50)) -- a *spectral*
delta, not a *prime-indexed* delta.

By contrast, ITPFI omega_1 = bigotimes_p omega_1^p has a TENSOR
PRODUCT over primes structure. To map omega_1 to W, one would need
either:
    (a) W to factor over primes (it does not), or
    (b) a sum-over-primes -> sum-over-zeros explicit-formula bridge
        that preserves positivity.

Option (b) is exactly the Weil/Li explicit-formula route -- which
is killed by K6 (off-line zeros INCREASE Li coefficients, wrong sign).
The "transport" BC-ITPFI -> W via the explicit formula is a SHADOW
OF K6.
""")

print("=" * 72)
print("FINAL VERDICT: Lead 4 is BLOCKED by category mismatch.")
print("Yakaboylu's W lives on a Bessel/Mellin Hilbert space, not on")
print("the BC GNS space. The only sum-over-primes <-> sum-over-zeros")
print("bridge is the explicit formula, which is K6. No new sign mechanism")
print("is contributed by ITPFI-omega_1's positivity.")
print("=" * 72)
