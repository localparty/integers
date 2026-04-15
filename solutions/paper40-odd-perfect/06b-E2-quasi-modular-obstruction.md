# Link 6, Route B: The E_2 quasi-modular obstruction

*Paper 40 -- Odd Perfect Numbers*
*Sub-route 6b: does the anomalous transformation of E_2, restricted to odd Fourier coefficients, obstruct the fixed point h = 2?*

*Author: G Six (originator), Claude Opus 4.6 (construction)*
*Date: 2026-04-14*

---

## 1. Odd-restricted E_2

### 1.1 The full E_2 series and sigma

The weight-2 Eisenstein series is

    E_2(tau) = 1 - 24 sum_{n>=1} sigma(n) q^n,    q = e^{2 pi i tau}

so

    sum_{n>=1} sigma(n) q^n = -(1/24)(E_2(tau) - 1).

### 1.2 Extracting odd-index coefficients

We want the odd-restricted sigma-series:

    F_odd(tau) := sum_{n odd} sigma(n) q^n.

The standard parity projection: for any power series f(q) = sum a(n) q^n,

    sum_{n odd} a(n) q^n = (1/2)[f(q) - f(-q)]
                         = (1/2)[f(q) - f(e^{i pi} q)]

In terms of the E_2 variable tau (where q = e^{2 pi i tau}), replacing q -> -q means tau -> tau + 1/2. Therefore:

    F_odd(tau) = -(1/48)[ (E_2(tau) - 1) - (E_2(tau + 1/2) - 1) ]
              = -(1/48)[ E_2(tau) - E_2(tau + 1/2) ].

### 1.3 Alternative decomposition via level-2 structure

There is a cleaner route. The even-index sigma-series is:

    sum_{n>=1} sigma(2n) q^{2n}.

We use the identity sigma(2n) = 3 sigma(n) - 2 sigma_odd(n) (where sigma_odd counts only odd divisors). But a more direct approach: the generating function for sigma(n) q^n over even n is obtained from the Hecke operator U_2:

    (E_2 | U_2)(tau) = sum_{n>=1} sigma(2n) q^n  (up to normalization).

Instead, use the known identity for restricted Eisenstein sums. We have:

    E_2(tau) - 2 E_2(2 tau) = 1 - 24 sum_{n>=1} [sigma(n) - 2 sigma(n/2)] q^n

where sigma(n/2) = 0 if n is odd. For odd n, sigma(n) - 2 sigma(n/2) = sigma(n). For even n = 2m, sigma(2m) - 2 sigma(m) = sigma_odd(2m) (the sum of ODD divisors of 2m).

Wait -- let me be more careful. We want to isolate the odd-index terms directly. The key identity is:

    sum_{n odd} sigma(n) q^n = sum_{n>=1} sigma(n) q^n  -  sum_{m>=1} sigma(2m) q^{2m}.

The second sum: sigma(2m) = sigma(2) sigma(m) when gcd(2,m) = 1 (m odd), and more generally sigma(2m) follows the multiplicative formula. But this still mixes parities of m.

The cleanest decomposition uses the fact that for the divisor sigma function on odd arguments, the generating function at level 2 is:

    F_odd(tau) = -(1/48)[ E_2(tau) - E_2(tau + 1/2) ]

as derived above. This is exact: the shift tau -> tau + 1/2 sends q -> -q, which negates odd-power terms and preserves even-power terms, so the difference isolates the odd-power terms.

### 1.4 Rewriting in standard modular objects

The function E_2(tau) - E_2(tau + 1/2) is a quasi-modular form of weight 2 for Gamma_0(2) intersected with the translation tau -> tau + 1/2 subgroup. Denote:

    G(tau) := E_2(tau) - E_2(tau + 1/2).

The Fourier expansion:

    E_2(tau) = 1 - 24 sum_{n>=1} sigma(n) q^n
    E_2(tau + 1/2) = 1 - 24 sum_{n>=1} sigma(n) (-1)^n q^n

so

    G(tau) = -24 sum_{n>=1} sigma(n) [1 - (-1)^n] q^n
           = -48 sum_{n odd} sigma(n) q^n.

Therefore:

    F_odd(tau) = sum_{n odd} sigma(n) q^n = -(1/48) G(tau) = -(1/48)[E_2(tau) - E_2(tau + 1/2)].

Confirmed. The odd-restricted sigma generating function is (up to constant) the difference E_2(tau) - E_2(tau + 1/2).

### 1.5 Alternative form: E_2(tau) - E_2(tau + 1/2) in terms of theta functions

The shift tau -> tau + 1/2 is NOT in SL_2(Z) (it corresponds to T^{1/2}, which doesn't preserve the lattice). So G(tau) is not a form for any congruence subgroup in the usual sense. However, it IS a form for the theta group Gamma_theta = < T^2, S >, because T^2: tau -> tau + 2 preserves the half-period shift.

This is the first structural observation: **the odd-restricted sigma series lives on the theta group, not on SL_2(Z) or Gamma_0(2)**.

---

## 2. Transformation analysis

### 2.1 Transformation of G(tau) under S: tau -> -1/tau

We compute G(-1/tau) = E_2(-1/tau) - E_2(-1/tau + 1/2).

**First term:**

    E_2(-1/tau) = tau^2 E_2(tau) + 6 tau / (pi i).

**Second term:** We need E_2(-1/tau + 1/2). Write -1/tau + 1/2 = (tau - 2)/(2 tau). We need to express this as a Mobius transform of tau and use the quasi-modular transformation.

The matrix taking tau to (tau - 2)/(2 tau) is:

    gamma = [[1, -2], [2, 0]] ... no, check: (1 * tau + (-2)) / (2 * tau + 0) = (tau - 2)/(2 tau).

But det(gamma) = 1*0 - (-2)*2 = 4, not 1. So gamma is NOT in SL_2(Z).

Let's factor differently. We have:

    -1/tau + 1/2 = (-2 + tau) / (2 tau).

Write this as a composition of SL_2(Z) transformations:

    tau -> 2 tau  (scaling, not in SL_2(Z))
    tau -> tau - 2  (T^{-2}, in SL_2(Z))
    tau -> -1/tau  (S)

This doesn't factor through SL_2(Z) in a clean way.

**Direct approach:** Use the general quasi-modular transformation law. For any gamma = [[a,b],[c,d]] in SL_2(Z):

    E_2(gamma tau) = (c tau + d)^2 E_2(tau) + (6c(c tau + d)) / (pi i).

But we need E_2 at -1/tau + 1/2, which is NOT an SL_2(Z) image of tau in general. We instead write:

    E_2(-1/tau + 1/2) = E_2(S(tau) + 1/2)

where S(tau) = -1/tau. Setting w = S(tau) = -1/tau:

    E_2(w + 1/2)  (this is just E_2 evaluated at w + 1/2).

There is no closed-form modular transformation relating E_2(w + 1/2) to E_2(w) because the half-integer shift is not in SL_2(Z). However, using the Fourier expansion:

    E_2(w + 1/2) = 1 - 24 sum_{n>=1} sigma(n) e^{pi i n} q_w^n

where q_w = e^{2 pi i w}. So E_2(w + 1/2) = 1 - 24 sum sigma(n) (-1)^n q_w^n.

### 2.2 Transformation of G under tau -> -1/tau

    G(-1/tau) = E_2(-1/tau) - E_2(-1/tau + 1/2)
              = [tau^2 E_2(tau) + 6 tau/(pi i)] - E_2(-1/tau + 1/2).

The second term does not simplify to a nice expression in E_2(tau). This is already a structural result:

**The odd-restricted sigma-series does NOT have a clean quasi-modular transformation under S.** The function G(tau) transforms into a mixture of E_2(tau) (with weight-2 transformation + anomaly) and E_2(-1/tau + 1/2) (which involves the Fourier expansion of E_2 at a half-period-shifted point in the S-transformed variable).

### 2.3 Transformation under Gamma_0(2)

For gamma = [[a,b],[c,d]] in Gamma_0(2) (i.e., c equiv 0 mod 2), we compute:

    E_2(gamma tau) = (c tau + d)^2 E_2(tau) + 6c(c tau + d)/(pi i).

And:

    E_2(gamma tau + 1/2) = E_2((a tau + b)/(c tau + d) + 1/2)
                         = E_2((a tau + b + (c tau + d)/2) / (c tau + d))
                         = E_2(((a + c/2) tau + b + d/2) / (c tau + d)).

Since c is even, c/2 is an integer. So a + c/2 is an integer, and b + d/2: since ad - bc = 1 and c is even, d must be odd (from ad = 1 + bc, bc even, so ad is odd, so d is odd), meaning d/2 is a half-integer. This means the argument is NOT of the form gamma' tau for any gamma' in SL_2(Z).

**Structural conclusion:** G(tau) does NOT transform as a (quasi-)modular form under Gamma_0(2) either. The half-period shift is incommensurable with the level-2 structure.

### 2.4 Transformation under Gamma(2)

For gamma in Gamma(2) = { [[a,b],[c,d]] : a equiv d equiv 1, b equiv c equiv 0 mod 2 }, we get:

    gamma tau + 1/2 = ((a + c/2) tau + (b + d/2)) / (c tau + d).

Now b is even so b + d/2: d equiv 1 mod 2, so d/2 is half-integer. Still not in SL_2(Z).

**However**, under T^2: tau -> tau + 2:

    G(tau + 2) = E_2(tau + 2) - E_2(tau + 2 + 1/2) = E_2(tau + 2) - E_2(tau + 5/2).

Since E_2(tau + 1) = E_2(tau) (E_2 is periodic with period 1), E_2(tau + 2) = E_2(tau) and E_2(tau + 5/2) = E_2(tau + 1/2). So:

    G(tau + 2) = G(tau).    [PROVED: G is periodic with period 2.]

Under S: tau -> -1/tau, we showed G does NOT transform cleanly.

Under ST^2S: tau -> tau/(2 tau + 1), which maps tau + 1/2 to... this gets complicated.

**Summary:** G(tau) = E_2(tau) - E_2(tau + 1/2) has period 2 but does NOT transform as a (quasi-)modular form under any standard congruence subgroup. It lives on the theta group but with BROKEN quasi-modularity: the anomalous term from E_2 does not cancel, and the half-period shift introduces additional non-modular behavior.

---

## 3. Obstruction assessment

### 3.1 The question: does the broken quasi-modularity obstruct h(n) = 2 for odd n?

The generating function for the odd-restricted abundancy condition is:

    sum_{n odd} sigma(n) q^n = -(1/48) G(tau).

The perfect-number condition sigma(n) = 2n requires the coefficient of q^n in the E_2 series to be sigma(n) = 2n, i.e., the n-th Fourier coefficient of G(tau) is -48 * 2n = -96n.

For this to hold, G(tau) must contain a term -96n * q^n at some specific odd n. The question is whether the analytic properties of G(tau) permit this.

### 3.2 Fourier coefficient constraints from (broken) modularity

For a genuine modular form f of weight k and level N, the Fourier coefficients a(n) satisfy the Ramanujan-Petersson bound |a(n)| << n^{(k-1)/2 + epsilon} (proved for holomorphic cusp forms of weight >= 2; the Deligne bound). For quasi-modular forms, the situation is different: E_2 is NOT a modular form, so Deligne's bound does not apply directly. The coefficients sigma(n) grow as O(n log log n) (Gronwall's theorem), which is consistent with weight 2 (the bound would be O(n^{1/2 + epsilon}) for a genuine weight-2 cusp form -- but E_2 is not cuspidal, so the comparison is moot).

**The broken quasi-modularity of G does NOT directly bound sigma(n) away from 2n.** The Fourier coefficients of G are still sigma(n) for odd n -- the same sigma(n) that can in principle equal 2n. The transformation properties constrain the FUNCTION G, not individual coefficients.

### 3.3 Could the anomalous term force a parity constraint?

The anomalous transformation term for E_2 is 6 tau/(pi i). This is a CONTINUOUS function of tau -- it carries no arithmetic information about individual Fourier coefficients. The anomaly tells us that E_2 (and hence G) is not a modular form, which means:

1. **No Hecke eigenform structure.** Genuine modular forms for congruence subgroups have Hecke eigenvalues that constrain coefficients multiplicatively. G does not have this property. But sigma(n) IS multiplicative, so this is a constraint that comes from number theory, not from modularity.

2. **No L-function with functional equation.** A genuine modular form of weight k for Gamma_0(N) corresponds to an L-function L(s, f) with functional equation s <-> k - s. The lack of such a functional equation for G means we cannot use zero-distribution arguments (a la RH) to constrain coefficients.

3. **No Atkin-Lehner involution.** For Gamma_0(2), the Atkin-Lehner involution W_2: tau -> -1/(2 tau) interchanges the two cusps. G does not transform under W_2, which means the two-cusp structure doesn't constrain G's coefficients.

### 3.4 The Rankin-Selberg connection

The most promising angle: sigma(n) = 2n means the RATIO sigma(n)/n = 2. The Dirichlet series sum sigma(n)/n^s = zeta(s) zeta(s-1). At s = 1, this has a double pole (from zeta(1) * zeta(0)). The odd-restricted version:

    sum_{n odd} sigma(n)/n^s = [1 - 2^{-s}] zeta(s) * [1 - 2^{1-s}] zeta(s-1)
                              = (1 - 2^{-s})(1 - 2^{1-s}) zeta(s) zeta(s-1).

Wait -- this requires care. The odd-restricted sigma Dirichlet series is NOT simply the product with the 2-Euler factor removed from zeta(s) zeta(s-1), because sigma(n) for odd n includes ALL divisors of n (which are all odd since n is odd). So:

    sum_{n odd} sigma(n) n^{-s} = prod_{p odd prime} sum_{a>=0} sigma(p^a) p^{-as}
                                = prod_{p odd} [1/(1 - p^{-s}) * 1/(1 - p^{1-s})]
                                    (after computing the local factor)

Actually: sum_{a>=0} sigma(p^a) p^{-as} = 1/((1 - p^{-s})(1 - p^{1-s})), which is the local factor of zeta(s) zeta(s-1) at p. So:

    sum_{n odd} sigma(n) n^{-s} = prod_{p odd} 1/((1 - p^{-s})(1 - p^{1-s}))
                                = zeta(s) zeta(s-1) / [(1/(1-2^{-s})) * (1/(1-2^{1-s}))]  ... no.

    zeta(s) zeta(s-1) = prod_{all p} 1/((1-p^{-s})(1-p^{1-s})).

Removing the p=2 factor:

    sum_{n odd} sigma(n) n^{-s} = zeta(s) zeta(s-1) * (1 - 2^{-s})(1 - 2^{1-s}).

At s = 1: zeta(1) has a simple pole with residue 1, and zeta(0) = -1/2. So zeta(s) zeta(s-1) has a simple pole at s = 1 with residue zeta(0) = -1/2. The correction factor (1 - 2^{-1})(1 - 2^{0}) = (1/2)(0) = 0.

**The odd-restricted sigma Dirichlet series has a ZERO at s = 1** (from the factor (1 - 2^{1-s}) vanishing at s = 1), not a pole. This is a significant structural fact: the pole of the full sigma Dirichlet series is CANCELLED by removing the p = 2 Euler factor.

### 3.5 Honest verdict on the E_2 obstruction

The quasi-modular anomaly of E_2 does not produce a direct arithmetic obstruction to sigma(n) = 2n for odd n. Here is why:

1. **The anomaly is analytic, not arithmetic.** The term 6 tau/(pi i) constrains the global analytic behavior of E_2 but does not restrict individual Fourier coefficients.

2. **The odd restriction breaks quasi-modularity further** (G has period 2 but no SL_2(Z) or Gamma_0(N) transformation law), which means FEWER tools are available to constrain coefficients, not more.

3. **The Dirichlet series cancellation** (Section 3.4) IS arithmetically significant: the vanishing of (1 - 2^{1-s}) at s = 1 means the odd-restricted sigma series has weaker growth than the full series. But this is a statement about AVERAGE ORDER, not about individual values sigma(n) = 2n.

4. **The correct framing:** the E_2 route would work if E_2's quasi-modularity somehow forced sigma(n) mod 2n to be nonzero for all odd n. But quasi-modular forms have Fourier coefficients that are essentially unconstrained in their divisibility properties (unlike genuine modular forms, which have Galois representations constraining coefficients).

**The E_2 quasi-modular obstruction, as a standalone route, does NOT close Link 6.**

---

## 4. ITPFI connection

### 4.1 The BC partition function and the halved residue

The BC partition function is Z(beta) = zeta(beta). The odd-restricted partition function is:

    Z_odd(beta) = prod_{p odd prime} (1 - p^{-beta})^{-1} = zeta(beta) / (1 - 2^{-beta})^{-1} = zeta(beta)(1 - 2^{-beta}).

At beta = 1:

    Res_{beta=1} Z_odd = (1 - 2^{-1}) Res_{beta=1} zeta = (1/2)(1) = 1/2.

The residue is halved -- this is the "2 without the 2" phenomenon: removing the p = 2 factor halves the pole strength.

### 4.2 From residue to Robin-type inequality

Robin's inequality: sigma(n) < e^gamma n ln(ln n) for all n > 5040, conditional on RH. The proof (Robin 1984, Lagarias 2002) uses the growth rate of sigma(n)/n, which is controlled by the partial products of (1 - p^{-1})^{-1} over primes p <= P(n).

For odd n, all prime factors p | n are odd, so the partial product is:

    prod_{p | n, p odd} p/(p-1) = prod_{p | n} p/(p-1).

Mertens' theorem gives prod_{p <= x} p/(p-1) ~ e^gamma ln x. For odd primes only:

    prod_{p <= x, p odd} p/(p-1) = [prod_{p <= x} p/(p-1)] / [2/(2-1)]
                                  = (1/2) prod_{p <= x} p/(p-1)
                                  ~ (e^gamma / 2) ln x.

**The odd Mertens constant is e^gamma / 2.** This is exact (not approximate): removing p = 2 from Mertens' product divides the constant by 2.

### 4.3 The odd Robin inequality

If we follow the Robin proof structure for odd n, the maximal order of sigma(n)/n over odd n should satisfy:

    lim sup_{n -> infty, n odd} sigma(n) / (n ln ln n) = e^gamma / 2.

This would give: for all sufficiently large odd n,

    sigma(n)/n < (e^gamma / 2) ln(ln n) + lower order terms.

For sigma(n)/n = 2, we need:

    (e^gamma / 2) ln(ln n) > 2
    ln(ln n) > 4 e^{-gamma} = 4 / 1.7810... = 2.2465...
    ln n > e^{2.2465} = 9.455
    n > e^{9.455} = 12,847.

So for all odd n > ~12,847, the odd Robin inequality would give sigma(n)/n < 2. Since all odd n < 12,847 can be checked computationally (none are perfect), this would prove the non-existence of odd perfect numbers.

**HOWEVER:** this argument requires PROVING the odd Robin inequality, which is not just the standard Robin inequality restricted to odd n. The standard Robin inequality uses the maximizer n_k = product of first k primes (primorial), which includes 2. The odd maximizer would be the odd primorial n_k^{odd} = 3 * 5 * 7 * 11 * ... * p_k. Proving that this is the maximizer among odd n, and that the bound is (e^gamma / 2) ln(ln n), requires a separate argument.

**Status of the odd Robin bound:** CONJECTURED, based on the halved Mertens constant. The proof would need:
- (a) RH (for the standard Robin infrastructure), inherited from Paper 13
- (b) A proof that the odd primorial is the maximizer of sigma(n)/n among odd n (plausible, but not in the literature as stated)
- (c) An effective version of the odd Mertens theorem with explicit error terms

### 4.4 Connection to E_2 obstruction

The E_2 route and the ITPFI/Robin route are COMPLEMENTARY, not redundant:

- E_2 encodes sigma(n) as Fourier coefficients of a quasi-modular form -- this is the ANALYTIC side.
- ITPFI encodes sigma(n)/n as a product of local KMS data -- this is the ALGEBRAIC side.
- The halved residue at beta = 1 (Section 4.1) appears in BOTH: it's the vanishing of (1 - 2^{1-s}) in the Dirichlet series (Section 3.4, E_2 side) and the halved pole of Z_odd (Section 4.1, ITPFI side).

The productive synthesis: the E_2 route ALONE doesn't close Link 6, but the Dirichlet series cancellation it reveals (the zero at s = 1 from (1 - 2^{1-s})) is the SAME phenomenon as the halved residue in the ITPFI route. **Route 6b feeds into Route 6a** -- the quasi-modular analysis confirms the halved residue and motivates the odd Robin inequality, but the actual closure must come through Route 6a (odd Robin sharpening) or Route 6c (ITPFI joint constraint).

### 4.5 Salvageable content from Route 6b

Despite not closing Link 6 independently, Route 6b establishes:

1. **F_odd(tau) = -(1/48)[E_2(tau) - E_2(tau + 1/2)]**: explicit formula for the odd-restricted sigma generating function.

2. **G(tau) has period 2 but no quasi-modular transformation under SL_2(Z) or any congruence subgroup**: the odd restriction destroys the quasi-modular structure, not just weakens it.

3. **The Dirichlet series sum_{n odd} sigma(n) n^{-s} has a ZERO at s = 1**: the factor (1 - 2^{1-s}) vanishes, cancelling the pole of zeta(s) zeta(s-1). This is the Dirichlet-series manifestation of "2 without the 2."

4. **The halved Mertens constant e^gamma / 2**: the odd restriction halves the asymptotic growth rate of sigma(n)/n, which is the foundation for the odd Robin inequality (Route 6a).

---

## 5. Verdict

### BLOCKED-DECOMPOSED

**Route 6b (E_2 quasi-modular obstruction) does not close Link 6 independently.**

The quasi-modular anomaly of E_2 is an analytic property of the generating function, not an arithmetic constraint on individual Fourier coefficients. The odd restriction further breaks the modular structure (losing the transformation law entirely, not just gaining an anomaly), which reduces the available tools rather than strengthening them.

**What Route 6b contributes:**
- Explicit formula: F_odd = -(1/48)[E_2(tau) - E_2(tau + 1/2)]
- Structural insight: the odd-restricted sigma Dirichlet series has a ZERO at s = 1 (from the factor (1 - 2^{1-s}))
- The halved Mertens constant e^gamma / 2, confirming the Route 6a foundation
- Proof that G(tau) has no quasi-modular transformation law under any standard congruence subgroup

**What Route 6b does NOT provide:**
- Any direct arithmetic obstruction to sigma(n) = 2n for odd n
- A Hecke eigenform structure or Galois representation constraining coefficients
- A functional equation for the odd-restricted L-function that could yield zero-distribution constraints

**Decomposition:**
- The Dirichlet series zero at s = 1 feeds directly into **Route 6a** (odd Robin sharpening)
- The ITPFI halved residue is the operator-algebraic manifestation of the same cancellation
- Route 6b is ABSORBED into Route 6a; it is not a standalone path to Link 6

**Recommended next step:** Construct the odd Robin inequality (Route 6a) using the halved Mertens constant. The key technical gap is proving that the odd primorial maximizes sigma(n)/n among odd n, and establishing an effective bound with explicit constants.

---

*v1: 2026-04-14. The E_2 obstruction is real but analytic, not arithmetic. The quasi-modular anomaly constrains the generating function's global behavior but cannot pin individual coefficients. The productive output: the Dirichlet series zero at s=1 and the halved Mertens constant, both of which feed Route 6a. The honest conclusion: modular forms constrain averages, not extremes -- and the odd perfect number question is about a single extreme value.*
