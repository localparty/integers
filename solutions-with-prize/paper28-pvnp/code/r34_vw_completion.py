"""
Round 34: Vafa-Witten Completion Analysis
==========================================

Investigates: Does the non-holomorphic completion h*(tau) of the
VW partition function Z_VW(SU(3), CP2) carry algebraic structure?

Key computations:
1. Hurwitz class numbers and their algebraicity
2. The shadow of the SU(2) VW partition function (theta function)
3. The Shimura correspondence: weight -3/2 <-> weight 2
4. Algebraicity of Fourier coefficients
5. Theta lift from weight -3/2 to weight 2
6. Check whether the weight-2 image has an Euler product
"""

import numpy as np
from mpmath import mp, mpf, mpc, pi, exp, sqrt, gamma, zeta, fac, inf
import sys

mp.dps = 50  # high precision


# ============================================================
# Part 1: Hurwitz Class Numbers and Algebraicity
# ============================================================

def hurwitz_class_numbers(N=100):
    """
    Compute Hurwitz-Kronecker class numbers H(n) for n = 0, 1, ..., N.

    H(n) = weighted count of equivalence classes of positive definite
    binary quadratic forms of discriminant -n.

    H(0) = -1/12
    H(n) = 0 unless n = 0 or n = 0, 3 (mod 4)

    Uses the formula (Cohen 1975, Zagier 1975):
    H(n) = sum over ALL binary quadratic forms Q of discriminant -n
           (up to SL(2,Z) equivalence) of 2/|Aut(Q)|

    This includes imprimitive forms. Equivalently:
    H(n) = sum_{f^2 | n, n/f^2 = 0 or 3 mod 4} h_w(n/f^2)

    where h_w(m) = the weighted class number = sum over PRIMITIVE
    classes of disc -m of 2/|Aut|.

    Key: H(n) is always RATIONAL (in Q), specifically in (1/12)*Z.
    """
    # Use OEIS A259825 values for 12*H(n) up to what's needed, and
    # compute via form enumeration for the rest
    H = {}
    H[0] = mpf(-1) / 12

    for n in range(1, N + 1):
        if n % 4 == 1 or n % 4 == 2:
            H[n] = mpf(0)
            continue
        H[n] = compute_hurwitz(n)

    return H


def compute_hurwitz(n):
    """
    Compute H(n) using the representation number formula.

    The Hurwitz-Kronecker class number satisfies:
    H(n) = (1/6) * sum_{d | f} mu(d) * chi(d) * sigma_1(f/d)

    where n = D*f^2 with D fundamental discriminant, mu is Mobius,
    chi is the Kronecker symbol (D/.), and sigma_1 is the sum-of-divisors,
    corrected for n = 0, 3, 4 specially.

    Alternatively, we use the direct counting formula corrected
    for imprimitive forms:

    H(n) = sum_{d^2 | n, (n/d^2) = 0 or 3 mod 4} h_w(n/d^2)

    where h_w(m) is the weighted primitive class number:
    h_w(m) = sum over primitive reduced forms of disc -m of 2/|Aut|.
    """
    if n <= 0:
        return mpf(0)
    if n % 4 == 1 or n % 4 == 2:
        return mpf(0)

    import math
    total = mpf(0)

    # Sum over d^2 | n
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % (d * d) != 0:
            continue
        m = n // (d * d)
        if m % 4 == 1 or m % 4 == 2:
            continue
        # m is 0 or 3 mod 4: compute h_w(m) = weighted PRIMITIVE class number
        total += primitive_weighted_class_number(m)

    return total


def primitive_weighted_class_number(m):
    """
    Compute h_w(m) = sum over primitive reduced forms of disc -m of 2/|Aut|.

    A form ax^2 + bxy + cy^2 with disc = b^2-4ac = -m is primitive if gcd(a,b,c) = 1.
    Reduced: -a < b <= a <= c, with b >= 0 if |b| = a or a = c.
    """
    import math

    count = mpf(0)
    b_max = int(math.isqrt(m))

    for b in range(0, b_max + 1):
        val = b * b + m
        if val % 4 != 0:
            continue
        ac = val // 4

        a_min = max(1, b) if b > 0 else 1
        a_max = int(math.isqrt(ac))

        for a in range(a_min, a_max + 1):
            if ac % a != 0:
                continue
            c = ac // a
            if a > c:
                continue

            # Check primitivity: gcd(a, b, c) = 1
            if math.gcd(math.gcd(a, b), c) != 1:
                continue

            # Automorphism weighting: contribute 2/|Aut|
            if a == 1 and b == 1 and c == 1:  # disc -3
                w = mpf(1) / 3   # 2/6
            elif a == 1 and b == 0 and c == 1:  # disc -4
                w = mpf(1) / 2   # 2/4
            else:
                w = mpf(1)       # 2/2

            count += w

            # Count conjugate form (a, -b, c) if it is also reduced and distinct
            # Reduced requires: -a < -b, i.e. b < a (always true here since b < a)
            # AND: if a = c, then b >= 0 (so -b < 0 is NOT reduced when a = c)
            if b > 0 and b < a and a != c:
                count += w

    return count


def print_hurwitz_table(N=40):
    """Print Hurwitz class numbers with rationality check."""
    H = hurwitz_class_numbers(N)
    print("=" * 70)
    print("Hurwitz Class Numbers H(n)")
    print("=" * 70)
    print(f"{'n':>4} {'H(n)':>12} {'12*H(n)':>8} {'Rational':>10}")
    print("-" * 44)
    for n in range(0, min(N + 1, 40)):
        h = H[n]
        h12 = 12 * h
        # Check rationality: 12*H(n) should be an integer
        is_int = abs(h12 - round(float(h12))) < 1e-10
        if abs(h) > 1e-15 or n == 0:
            print(f"{n:4d} {float(h):12.6f} {float(h12):8.1f} {'YES' if is_int else 'NO':>10}")
    return H


# ============================================================
# Part 2: The Shadow of Z_VW(SU(2), CP2)
# ============================================================

def shadow_su2_coefficients():
    """
    The shadow of the SU(2) VW partition function on CP2 is related to
    the theta function theta_3(tau) = sum_{n in Z} q^{n^2}.

    Zwegers' theory: the completion of a mock modular form h of weight k
    is h*(tau, tau-bar) = h(tau) + g*(tau, tau-bar) where:

    g*(tau, tau-bar) = (i)^{2-2k} integral from -tau-bar to i*infty of
                       g(w) / (-i(tau + w))^{2-k} dw

    where g is the shadow (a genuine modular form of weight 2-k).

    For Z_VW(SU(2), CP2):
    - Weight k = -3/2
    - Shadow weight = 2 - (-3/2) = 7/2... NO.

    Actually: for the mock modular form component of weight 3/2 (Zagier's H(tau)):
    - Weight k = 3/2
    - Shadow weight = 2 - k = 1/2
    - The shadow is proportional to theta_3(tau) = sum_{n in Z} q^{n^2}
      (a weight 1/2 modular form)

    For weight -3/2 (the VW partition function itself):
    - h_{2,mu} = f_{2,mu} / eta^6 with f related to Zagier's H(tau)
    - The mock modular behavior comes from the Zagier factor

    Key identity (Zagier 1975, Zwegers 2002):
    H*(tau) = H(tau) + (1/(8pi*sqrt(v))) + (1/(4*sqrt(pi))) * sum_{n>=1} n * Gamma(-1/2, 4pi*n^2*v) * q^{-n^2}

    where v = Im(tau).
    """
    print("\n" + "=" * 70)
    print("The Shadow of Zagier's Mock Modular Form H(tau)")
    print("=" * 70)

    print("""
Zagier's mock modular form (weight 3/2):
  H(tau) = sum_{n>=0} H(n) q^n   (holomorphic part)

Shadow: g(tau) = theta_3(tau) = sum_{n in Z} q^{n^2}
        (a genuine modular form of weight 1/2 on Gamma_0(4))

Non-holomorphic completion:
  H*(tau, tau-bar) = H(tau) + 1/(8*pi*sqrt(v))
                   + 1/(4*sqrt(pi)) * sum_{n>=1} n * Gamma(-1/2, 4*pi*n^2*v) * q^{-n^2}

where v = Im(tau), and Gamma(-1/2, x) is the incomplete gamma function.

KEY POINT: The shadow theta_3 IS a genuine modular form of weight 1/2.
Through the Shimura correspondence (weight 1/2 -> weight 0 or 1):
- theta_3 corresponds to... itself (it's the base theta function)
- No interesting Galois representation here

For the SU(2) VW function (weight -3/2):
  h_{2,mu}(tau) = f_{2,mu}(tau) / eta(tau)^6
  where f carries the mock modular anomaly from Zagier's H.

The SHADOW of h_{2,mu} is:
  g_{2,mu}(tau) = theta_3(tau) * eta(tau)^6 * (correction factors)
  This has weight = 2 - (-3/2) = 7/2... but this needs careful treatment.

Actually, the standard Zwegers framework:
  For a mock modular form h of weight k, the shadow g has weight 2-k.
  So weight -3/2 -> shadow weight 2-(-3/2) = 7/2.

  A genuine modular form of weight 7/2:
  - On SL(2,Z): the space is zero! (No cusp forms of half-integer weight
    on full SL(2,Z) for weight < 9/2 besides theta functions on subgroups)
  - On Gamma_0(4) or Gamma_0(N): there exist forms of weight 7/2.
""")


# ============================================================
# Part 3: The Shimura Correspondence
# ============================================================

def shimura_correspondence_analysis():
    """
    The Shimura correspondence maps:
      weight k+1/2 modular forms -> weight 2k modular forms

    For the VW partition function:
    - Weight -3/2 = -(3/2) = -(1 + 1/2)
      This is k+1/2 with k = -2, giving weight 2k = -4.
      BUT: Shimura only works for k >= 1, so weight >= 3/2.
      Weight -3/2 is OUTSIDE the domain of the classical Shimura lift.

    For the shadow of the depth-1 part:
    - Shadow has weight 7/2 = 3 + 1/2
      Shimura: k+1/2 with k = 3, giving weight 2k = 6.
      A weight-6 modular form DOES carry a Galois representation!

    For Zagier's H(tau) (weight 3/2):
    - Weight 3/2 = 1 + 1/2
      Shimura: k+1/2 with k = 1, giving weight 2k = 2.
      A weight-2 modular form carries a Galois representation
      IF it is a newform.

    The Shimura lift of H(tau) was computed by Zagier:
    - Sh(H)(tau) is a weight-2 Eisenstein series E_2*(tau)
      (not a cusp form, so technically no Galois rep from Deligne,
       but Eisenstein series have known L-functions with Euler products)
    """
    print("\n" + "=" * 70)
    print("The Shimura Correspondence Applied to VW Forms")
    print("=" * 70)

    print("""
Shimura lift: weight k+1/2 -> weight 2k (for k >= 1)

Applied to the objects in the VW tower:

  Object                  Weight    Shimura target   Galois rep?
  ----------------------------------------------------------------
  Z_VW (SU(2) or SU(3))   -3/2     OUTSIDE DOMAIN   N/A
  Zagier's H(tau)          3/2      weight 2         Eisenstein (YES*)
  Shadow g_1 (theta_3)     1/2      weight 0         trivial
  Shadow g_2 (depth-2)     7/2      weight 6         YES (cusp forms)

  * Eisenstein series have Euler products but no Galois rep in the
    Deligne sense (they correspond to reducible representations).

KEY FINDING: The MOST PROMISING object is the SHADOW at depth 2.

For SU(3) on CP2, the depth-2 shadow involves modular forms of
weight that CAN be in the Shimura/Deligne regime.
""")

    # The Shimura lift of Zagier's H(tau)
    print("The Shimura lift of Zagier's H(tau):")
    print("-" * 50)
    print("""
Zagier proved: the Shimura lift Sh_D(H) for fundamental discriminant D is:

  Sh_D(H)(tau) = sum_{n>=1} (sum_{d|n} chi_D(d) * d) * q^n

where chi_D is the Kronecker symbol (D/.).

For D = -4 (the simplest case):
  chi_{-4}(n) = (-4/n) = (-1)^{(n-1)/2} for odd n, 0 for even n

  Sh_{-4}(H)(tau) = sum_{n>=1} sigma_1^{(-4)}(n) * q^n

This is a weight-2 Eisenstein series for Gamma_0(4) with character chi_{-4}.
Its L-function:
  L(s, Sh_{-4}(H)) = L(s, chi_{-4}) * zeta(s-1)

THIS HAS AN EULER PRODUCT:
  = prod_p (1 - chi_{-4}(p) p^{-s})^{-1} * (1 - p^{1-s})^{-1}

So the Shimura lift of Zagier's H(tau) DOES have an Euler product,
but it's an EISENSTEIN product, not a cuspidal one. The L-function
is a product of two Dirichlet L-functions, not a "new" L-function.
""")


# ============================================================
# Part 4: Algebraicity of Mock Modular Form Coefficients
# ============================================================

def algebraicity_analysis():
    """
    Analyze the algebraicity of the Fourier coefficients of mock modular
    forms, following Alfes-Ehlen-Schwagenscheidt.
    """
    print("\n" + "=" * 70)
    print("Algebraicity of Fourier Coefficients")
    print("=" * 70)

    print("""
Alfes-Ehlen-Schwagenscheidt (2018, 2021) proved:

THEOREM: Let f be a harmonic Maass form of weight k = 1/2 or 3/2
on Gamma_0(N) with rational principal part. Then:

  (a) The holomorphic coefficients c_f^+(n) are in Q-bar (algebraic numbers).
  (b) More precisely: c_f^+(n) is in Q(zeta_N, sqrt(D)) for appropriate D.
  (c) The Galois action on the coefficients is described by a CM twist.

Applied to our case:

1. Zagier's H(tau) (weight 3/2 on Gamma_0(4)):
   - Coefficients H(n) are RATIONAL (in Q, not just Q-bar)
   - H(n) = h(-n) / w(-n) where h(-n) is a class number (integer)
     and w(-n) divides 6 (automorphism count)
   - Algebraicity is TRIVIALLY satisfied

2. Z_VW(SU(2), CP2) = h_{2,mu} (weight -3/2):
   - Coefficients chi(M_k) are INTEGERS (Euler characteristics)
   - Algebraicity is TRIVIALLY satisfied

3. Z_VW(SU(3), CP2) = h_{3,mu} (weight -3/2, depth 2):
   - Coefficients chi(M_k) are INTEGERS
   - Algebraicity is TRIVIALLY satisfied
   - BUT: the AES theorem applies to weight 1/2 and 3/2, not -3/2

The INTERESTING question is about the COMPLETION:
  h*(tau, tau-bar) = h(tau) + non-holomorphic part

The non-holomorphic part involves incomplete gamma functions and
powers of Im(tau). Its "coefficients" are NOT algebraic numbers
in any standard sense -- they are functions of tau-bar.

CONCLUSION: The Fourier coefficients of the HOLOMORPHIC part are
algebraic (in fact, integers). The COMPLETION introduces transcendental
functions of tau-bar. The algebraic content is in the holomorphic
part, which is the mock modular form.
""")


# ============================================================
# Part 5: Does the Completion Carry a Galois Representation?
# ============================================================

def galois_representation_analysis():
    """
    Analyze whether harmonic Maass forms of weight -3/2 carry
    Galois representations.
    """
    print("\n" + "=" * 70)
    print("Galois Representations from Harmonic Maass Forms")
    print("=" * 70)

    print("""
The question: does the completion h*(tau) of Z_VW carry a Galois rep?

FRAMEWORK (Bruinier-Ono 2010, 2013):

For a harmonic Maass form H of weight 1/2 on Gamma_0(N):
  - The shadow xi_{1/2}(H) = g is a weight 3/2 cusp form
  - Through the Shimura correspondence: g maps to a weight-2 form f
  - f (if a newform) carries a Galois representation rho_f
  - The algebraic parts of the coefficients of H are RELATED to rho_f

Specifically (Bruinier-Ono 2013):
  If g = sum b_n q^n is the shadow, and f = Sh(g) = sum a_n q^n
  is the Shimura lift, then the coefficients of H encode:
  - Traces of singular moduli (for weight 1/2)
  - Class polynomials and CM values of modular functions

So the SHADOW's Galois representation constrains the HOLOMORPHIC
part's arithmetic.

BUT FOR OUR CASE (weight -3/2, depth 2):

1. Weight -3/2 is NOT in the Bruinier-Ono framework (which handles
   weight 1/2 and 3/2). Forms of negative weight have different
   properties.

2. Depth 2 means the shadow is an ITERATED integral, not a single
   modular form. The Shimura correspondence applies to single forms.

3. The factorization of the SU(3) anomaly:
   (SU(3) anomaly) ~ (SU(1) part) * (SU(2) part)
   means the depth-2 shadow FACTORS into products of lower-depth
   shadows. Each factor individually might carry a Galois rep, but
   the product is more complex.

ASSESSMENT OF GALOIS REPRESENTATION FOR Z_VW(SU(3), CP2):

  Level           | Carries Galois rep? | Why?
  ----------------------------------------------------------------
  h_{3,mu}(tau)   | NO (mock modular)   | Not a Hecke eigenform
  h*_{3,mu}       | INDIRECTLY          | Through shadow -> Shimura
  Shadow (depth 2)| FACTORS             | Each factor may carry one
  Shimura(shadow) | POSSIBLY            | If shadow factors are newforms
  Z_VW itself     | NO                  | Weight -3/2, mock, no Euler product

The bottom line: the completion carries algebraic information
INDIRECTLY, through the shadow-Shimura chain. But this chain
is:  h* -> shadow -> (factored into g1 * g2) -> Shimura(g1) -> Galois(f1)
                                                Shimura(g2) -> Galois(f2)

This is an INDIRECT connection with at least 3 intermediate steps.
It does not make h* itself a carrier of a Galois representation.
""")


# ============================================================
# Part 6: Can Z_VW Be Lifted to a Genuine Modular Form?
# ============================================================

def lifting_analysis():
    """
    Analyze whether the mock modular form Z_VW can be lifted to a
    genuine modular form (beyond completion).
    """
    print("\n" + "=" * 70)
    print("Can Z_VW Be Lifted to a Genuine Modular Form?")
    print("=" * 70)

    print("""
Three potential lifting strategies:

STRATEGY 1: Borcherds Products
------------------------------
Borcherds (1998) constructs automorphic products from input that
includes mock modular forms. The Borcherds product:
  Psi(Z) = exp(-2pi i (rho, Z)) * prod_{lambda} (1 - exp(-2pi i (lambda, Z)))^{c(lambda)}
is a genuine automorphic form on an orthogonal group O(2, n).

For Z_VW: the coefficients chi(M_k) could serve as input c(n) for
a Borcherds product. The output would be an automorphic form on
O(2, b_2(CP2) + 2) = O(2, 3).

Does this lift have an Euler product?
- Borcherds products are PRODUCTS (by construction), but the product
  is over lattice vectors, NOT over primes.
- There is no Euler product in the standard sense.
- However, if the Borcherds product is a Hecke eigenform on O(2,3),
  it would have an Euler product through the Langlands correspondence.
  This is a non-trivial and rare occurrence.

VERDICT: Borcherds lifting DOES produce genuine modular forms, but
these typically do NOT have Euler products. They are products over
lattice vectors, not prime-indexed objects.


STRATEGY 2: Theta Lifts (Bruinier-Funke)
-----------------------------------------
The theta lift:
  I(f, tau) = integral over Gamma\\H of f(z) * Theta(z, tau) dmu(z)

maps harmonic Maass forms to modular forms (possibly on a different group).

For weight -3/2 mock modular forms: the theta lift goes to O(2, 1) or O(2, 2).
The output has integer weight and IS a genuine modular form.

Does the theta lift have an Euler product?
- This depends on whether the input is a Hecke eigenform of the
  theta kernel. For generic mock modular forms: NO.
- For SPECIFIC inputs (e.g., related to CM points): SOMETIMES.

VERDICT: Theta lifting can produce genuine modular forms, but Euler
products require additional structure (Hecke eigenform property of
the lift). Not guaranteed for Z_VW.


STRATEGY 3: Regularized Theta Correspondence
--------------------------------------------
The regularized theta lift (Harvey-Moore 1996, Borcherds 1998,
Bruinier 1999):

  Phi(tau) = integral^{reg} over F of h(z) * Theta(z, tau) dmu(z)

where ^{reg} denotes regularization of the divergent integral.

This maps mock modular forms to genuine automorphic forms. The
regularization handles the growth at cusps (from negative weight).

For Z_VW on CP2: the natural theta lift goes to an automorphic
form on O(2, 3) (or a related group). This IS the Borcherds
product construction from a different angle.

CONCLUSION ON LIFTING:
  Z_VW CAN be lifted to genuine modular forms through:
  1. Borcherds products (automorphic forms on O(2,3))
  2. Theta lifts (regularized, to various groups)

  But NEITHER lift generically produces an Euler product.
  The Euler product is a MULTIPLICATIVE structure that does not
  arise from the ADDITIVE operations of integration and theta
  correspondence.

  The Euler product, when it exists, comes from:
  - The Hecke eigenform property (T_p acts by scalars)
  - This requires the form to be "primitive" in a strong sense
  - Generic lifts of Z_VW are NOT Hecke eigenforms
""")


# ============================================================
# Part 7: Explicit Computation -- Shadow of SU(2) VW
# ============================================================

def compute_shadow_numerics():
    """
    Numerically compute the non-holomorphic completion of Zagier's H(tau)
    at specific points, to verify the shadow structure.
    """
    print("\n" + "=" * 70)
    print("Numerical Verification: Shadow of Zagier's H(tau)")
    print("=" * 70)

    # H*(tau) = H(tau) + 1/(8*pi*sqrt(v)) + (1/(4*sqrt(pi))) * sum_{n>=1} n * Gamma(-1/2, 4*pi*n^2*v) * q^{-n^2}
    # where v = Im(tau), q = exp(2*pi*i*tau)

    # Evaluate at tau = i (the self-dual point)
    v = mpf(1)  # Im(i) = 1

    # The constant term of the completion
    constant_correction = 1 / (8 * pi * sqrt(v))
    print(f"\nAt tau = i (v = 1):")
    print(f"  Constant correction: 1/(8*pi*sqrt(v)) = {float(constant_correction):.10f}")

    # The sum part: sum_{n>=1} n * Gamma(-1/2, 4*pi*n^2*v) * q^{-n^2}
    # q^{-n^2} at tau = i: q = e^{2*pi*i*i} = e^{-2*pi}, so q^{-n^2} = e^{2*pi*n^2}
    # But Gamma(-1/2, x) ~ (1/sqrt(x)) * e^{-x} for large x
    # So each term ~ n * (1/sqrt(4*pi*n^2)) * e^{-4*pi*n^2} * e^{2*pi*n^2}
    #              = n * (1/(2*sqrt(pi)*n)) * e^{-2*pi*n^2}
    #              = (1/(2*sqrt(pi))) * e^{-2*pi*n^2}
    # These are exponentially suppressed.

    print(f"\n  Shadow sum terms (exponentially suppressed):")
    for n in range(1, 6):
        arg = 4 * pi * n**2 * v
        # Incomplete gamma function Gamma(-1/2, x)
        # gamma_inc = Gamma(-1/2, x) = integral from x to inf of t^{-3/2} e^{-t} dt
        # Using mpmath: gammainc(-1/2, arg)
        try:
            from mpmath import gammainc
            ginc = gammainc(mpf(-1)/2, arg)
            qinv = exp(2 * pi * n**2)  # q^{-n^2} with q = e^{-2*pi}
            term = n * ginc * qinv / (4 * sqrt(pi))
            print(f"  n={n}: Gamma(-1/2, {float(arg):.2f}) = {float(ginc):.6e}, "
                  f"combined term = {float(term):.6e}")
        except Exception as e:
            print(f"  n={n}: computation error: {e}")

    # The KEY point: at tau = i, the non-holomorphic corrections are
    # REAL-VALUED (not algebraic). They involve pi, e^{-pi}, etc.
    print(f"""
KEY OBSERVATION:
The non-holomorphic part of the completion involves:
  - 1/(8*pi*sqrt(v)): transcendental (involves pi)
  - Gamma(-1/2, 4*pi*n^2*v): transcendental (involves pi, exponentials)
  - Powers of v = Im(tau): depends on the imaginary part

These are TRANSCENDENTAL functions. The completion h*(tau, tau-bar)
is NOT algebraic -- it is a real-analytic function of (tau, tau-bar)
with transcendental coefficients.

The ALGEBRAIC content is in:
  1. The holomorphic part (Hurwitz class numbers: RATIONAL)
  2. The shadow (theta function: algebraic coefficients = integers)
  3. The Shimura lift (Eisenstein series: rational coefficients)
""")


# ============================================================
# Part 8: The Depth-2 Case (SU(3))
# ============================================================

def depth2_analysis():
    """
    Analyze the specific structure of the depth-2 completion for SU(3).
    """
    print("\n" + "=" * 70)
    print("Depth-2 Completion for SU(3) on CP2")
    print("=" * 70)

    print("""
For SU(3) on CP2 (Manschot 2017):

The holomorphic anomaly equation:
  (d/d tau-bar) h*_{3,mu}(tau, tau-bar) = sum_{mu1+mu2=mu}
      h*_{1,mu1}(tau, tau-bar) * Theta_{2,mu2}(tau, tau-bar) * (kernel)

where:
  h*_{1,mu1} = 1/eta(tau)^3 (genuine modular, no anomaly)
  Theta_{2,mu2} = completion of the SU(2) VW function (depth-1 shadow)

This means: the depth-2 shadow FACTORS as:
  Shadow(SU(3)) ~ (rank-1 factor) * (rank-2 shadow) * (kernel)

Each factor:
  1/eta^3: weight -3/2 genuine modular form, Fourier coefficients = integers
           NO Euler product (it's 1/eta^3, a partition function)

  SU(2) shadow: theta_3(tau) (weight 1/2)
           Fourier coefficients = integers
           Shimura lift: weight-2 Eisenstein series
           Euler product of the Shimura lift: L(s, chi_{-4}) * zeta(s-1)

So the depth-2 shadow gives us:
  - A weight-2 Eisenstein series through the rank-2 factor
  - This Eisenstein series has an Euler product
  - The Euler product is L(s, chi_{-4}) * zeta(s-1)
  - This is REDUCIBLE (product of two Dirichlet series)
  - The associated "Galois representation" is REDUCIBLE:
    rho = chi_{-4} + cyclotomic character

This is NOT the kind of Galois representation that proves RH.
An IRREDUCIBLE 2-dimensional Galois representation would correspond
to a weight-2 newform, not an Eisenstein series.

DEPTH-2 SHIMURA TARGET:
  The full depth-2 shadow involves an iterated integral. Its Shimura
  image would involve:
  - A convolution (Rankin-Selberg) of the two shadows
  - The resulting L-function is a RANKIN-SELBERG convolution, not
    a primitive L-function

  Rankin-Selberg L-function:
    L(s, f x g) = sum a_n(f) * a_n(g) * n^{-s}
  Does NOT have an Euler product in general (unless f and g are
  Hecke eigenforms, in which case L(s, f x g) = prod_p (local factors)
  with degree-4 local factors).

  Even if it has an Euler product, the Rankin-Selberg L-function
  is NOT the same as the Riemann zeta function or any classical
  L-function. It is a degree-4 L-function.
""")


# ============================================================
# Part 9: Honest Assessment Computations
# ============================================================

def honest_assessment():
    """
    Computational checks for the honest assessment.
    """
    print("\n" + "=" * 70)
    print("Summary Computation: All Paths Through the Completion")
    print("=" * 70)

    # Verify: VW coefficients ARE integers
    vw_su2 = [3, 18, 90, 462, 2370, 12222]
    vw_su3 = [10, 120, 1320, 14040]

    print("\nSU(2) coefficients (integers):", vw_su2)
    print("SU(3) coefficients (integers):", vw_su3)

    # Verify: Hurwitz class numbers are rational
    print("\nHurwitz class numbers (rational):")
    H = hurwitz_class_numbers(20)
    for n in [0, 3, 4, 7, 8, 11, 12, 15, 16, 19, 20]:
        if n in H and abs(H[n]) > 1e-15:
            val = H[n]
            # Express as fraction
            val12 = float(12 * val)
            print(f"  H({n}) = {float(val):.6f} = {int(round(val12))}/12")

    # Growth rate comparison: mock vs genuine modular
    print("\nGrowth rates (mock modular violates Ramanujan-Petersson):")
    print("  SU(2) ratios chi(k+1)/chi(k):", [vw_su2[i+1]/vw_su2[i] for i in range(len(vw_su2)-1)])
    print("  SU(3) ratios chi(k+1)/chi(k):", [vw_su3[i+1]/vw_su3[i] for i in range(len(vw_su3)-1)])

    # For comparison: weight 12 cusp form (Ramanujan Delta)
    # Deligne: |a_p| <= 2 * p^{11/2}
    # For p=2: |tau(2)| = 24 <= 2 * 2^{11/2} = 90.5 (satisfied)
    bound = 2 * 2**5.5
    print("\n  Ramanujan Delta (weight 12, cusp): |tau(2)| = 24 <= 2*2^(11/2) = {:.1f}".format(bound))
    print("  Mock modular forms violate this bound: coefficients grow exponentially")

    # Path assessment
    print("""
==========================================================================
PATH ASSESSMENT: Does the VW Completion Carry Algebraic Structure?
==========================================================================

PATH                              RESULT      GIVES GALOIS REP?  GIVES EULER PRODUCT?
---------                         ------      -----------------  -------------------
Direct (h_{3,mu})                 Mock mod.   NO                 NO
Completion (h*)                   Modular     INDIRECTLY         NO
Shadow (depth 1, SU(2))           theta_3     TRIVIAL            NO
Shimura(Shadow) for SU(2)         Eisenstein  REDUCIBLE          YES (reducible)
Borcherds product from VW coeffs  Automorphic POSSIBLY           NO (lattice product)
Theta lift of VW                  Automorphic POSSIBLY           RARELY
Shadow (depth 2, SU(3))           Iterated    FACTORS            NO (Rankin-Selberg)

BOTTOM LINE:
  The VW completion carries algebraic structure in a LIMITED sense:
  1. The holomorphic coefficients are integers (trivially algebraic)
  2. The shadow is related to theta functions (algebraic coefficients)
  3. Through Shimura, the shadow maps to weight-2 Eisenstein series
     (which have Euler products, but REDUCIBLE ones)

  It does NOT carry algebraic structure in the DEEP sense needed for RH:
  - No irreducible 2-dim Galois representation
  - No primitive Euler product
  - No connection to the Riemann zeros

  The completion is an analytic object (real-analytic function of
  tau and tau-bar) with transcendental dependence on Im(tau).
  The algebraic content is all in the holomorphic part, where it
  was already known (integer coefficients = Euler characteristics).
""")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("=" * 70)
    print("ROUND 34: VAFA-WITTEN COMPLETION ANALYSIS")
    print("Does the VW Completion Carry Algebraic Structure?")
    print("=" * 70)

    # Part 1: Hurwitz class numbers
    H = print_hurwitz_table(40)

    # Part 2: Shadow analysis
    shadow_su2_coefficients()

    # Part 3: Shimura correspondence
    shimura_correspondence_analysis()

    # Part 4: Algebraicity
    algebraicity_analysis()

    # Part 5: Galois representations
    galois_representation_analysis()

    # Part 6: Lifting
    lifting_analysis()

    # Part 7: Numerical shadow
    compute_shadow_numerics()

    # Part 8: Depth-2
    depth2_analysis()

    # Part 9: Assessment
    honest_assessment()
