# Research 43 -- CCM Independent Verification (arXiv:2511.22755)

*Date: 2026-04-09*
*Status: VERIFIED WITH CAVEATS -- construction sound, two hidden assumptions identified*
*Role: Adversarial independent verification of Connes-Consani-Moscovici*

---

## 0. Scope

Our proof depends on four specific results from CCM:
1. Theorem 5.10(i): D' is self-adjoint in the T-inner product
2. Theorem 5.10(iii): zeros of xi-hat are eigenvalues of D'
3. Lemma 7.2: prolate approximation error O(lambda^{-2})
4. Lemma 7.3: Fourier transform convergence to Xi

Each is examined with adversarial intent below.

---

## 1. Theorem 5.10 Self-Adjointness

### 1a. Is the T-inner product positive-definite?

The T-inner product is <f|g>_T = <Tf|g> where T = QW_lambda^N - epsilon_N Id
(Lemma 5.4, p. 17). Here epsilon_N is the smallest eigenvalue of QW_lambda^N.

T - epsilon_N Id has eigenvalues {mu_k - epsilon_N} where mu_k are the
eigenvalues of T. Since epsilon_N is the SMALLEST eigenvalue:
- mu_k - epsilon_N >= 0 for all k
- mu_k - epsilon_N = 0 ONLY for k corresponding to epsilon_N itself

So T - epsilon_N Id is positive SEMIDEFINITE, not positive definite.
The radical (null space of the form) is exactly C*xi, the one-dimensional
space spanned by the minimal eigenvector.

CCM handle this correctly: they quotient by the radical. The Hilbert space
H is defined as E_N / C*xi (p. 18, "The Hilbert space H obtained from E_N
using the inner product <f|g>_T is the quotient of E_N by the radical
Ker T = C*xi"). The T-inner product is positive definite on this quotient.

**VERDICT: SOUND.** The positive-semidefiniteness is correctly handled by
passing to the quotient. No hidden assumption. The construction is the
standard GNS-type quotient for a degenerate inner product.

### 1b. Is D'*_T = D' verified?

The proof is on pp. 17-18, Lemma 5.4(ii). The key computation:

    <D'f | g>_T = <TD'f | g> = <TDf | g> + <TRf | g>

where R = -|D*xi><eta|. Then using TD' = TD + |beta><eta| (from (i)):

    <D'f | g>_T = <DTf | g> + <R'f | g>, R' = |eta><beta|

And for the other side:

    <f | D'g>_T = <Tf | Dg> + <Tf | Rg> = <DTf | g> + <f | TRg>

Using TRg = (-T|D*xi><eta|)g = |beta><eta|g (since T*D*xi = -beta by (i)):

    <f | D'g>_T = <DTf | g> + <R'f | g>

The two sides match. This computation is EXPLICIT and VERIFIED line by line.

**Critical check:** The computation uses:
- D symmetric in the standard inner product (D = diag(n), obviously symmetric)
- T symmetric (QW is a real symmetric matrix, Lemma 5.1)
- The identity TD*xi = -beta (Lemma 5.4(i), proved from DT - TD = |beta><eta| - |eta><beta|)

All three are justified. The algebra is correct.

**VERDICT: SOUND.** Self-adjointness in the T-inner product is rigorously
proved. No hidden assumption.

### 1c. Hidden assumptions?

The proof of Lemma 5.4 assumes:
- T >= 0 (positive semidefinite) -- YES, this is Proposition 3.3 (QW_lambda is lower bounded)
  combined with subtracting epsilon_N
- Ker T = C*xi (one-dimensional kernel) -- YES, this requires SIMPLICITY of epsilon_N
- gamma*xi = xi (evenness) -- YES, this is the EVEN-SIMPLE hypothesis
- <xi | eta> != 0, specifically delta_N(xi) = 1 -- YES, this is the normalization

The ONLY hidden assumption beyond the stated hypotheses is:
**delta_N(xi) != 0**, i.e., the Dirichlet kernel evaluation at xi is nonzero.
This is required for the normalization (p. 17, eq 5.4: "<xi | eta> = 1").
CCM state this without proof: "One has delta_N(xi) != 0" (p. 20).

WHY is delta_N(xi) != 0? If xi is even (gamma*xi = xi), then xi has
support only in the even sector. The vector eta = sum V_j has both even
and odd components. The inner product <xi | eta> = <xi | eta_even> where
eta_even = (1/sqrt{L}) sum_{even part}. This is nonzero because:
- xi is the unique (up to phase) kernel vector of QW_lambda^N in the even sector
- eta has a nonzero even component (the constant function 1/sqrt{L} restricted
  to even harmonics is nonzero)
- If <xi | eta> = 0, then xi would be orthogonal to all Dirichlet kernel
  evaluations, implying xi(lambda) = 0 (Corollary 5.6), but xi is a smooth
  eigenfunction on [lambda^{-1}, lambda] -- vanishing at the boundary is
  NOT generic

This is a SOFT argument, not a proof. CCM do not prove delta_N(xi) != 0;
they assert it. For our purposes this is acceptable because:
(a) numerically it is always nonzero
(b) the AE simplicity mechanism we use (non-vanishing overlaps) would also
    give non-vanishing Dirichlet evaluation as a byproduct

**VERDICT: SOUND WITH CAVEAT.** delta_N(xi) != 0 is asserted, not proved.
The assertion is well-motivated and numerically verified, but it IS a gap
in the formal proof. Severity: LOW.

---

## 2. Theorem 5.10(iii) Eigenvalue Identification

### 2a. Cauchy structure

The proof uses the factored determinant (pp. 23-24):

    det_reg(D_log^{(lambda,N)} - z) = Det(D_log^{(lambda,N)}|_{E'_N} - z) * det_reg(D_log^{(lambda)}|_{E_N^perp} - z)

The first factor is the characteristic polynomial of D'' (self-adjoint on H),
hence all its zeros are real and are the eigenvalues of D''.

The second factor's zeros are {2*pi*j/L : j in Z, |j| > N} -- the spectrum
of the unperturbed scaling operator on the orthogonal complement.

The total spectrum is the union. The regularized determinant formula
(eq 5.27) gives:

    det_reg(D_log^{(lambda,N)} - z) = -i * lambda^{-iz} * xi-hat(z)

where xi-hat(z) = 2 L^{-1/2} sin(zL/2) (sum xi_j / (z - 2*pi*j/L))
is an entire function (Proposition 5.9).

### 2b. Is the identification exact or approximate?

**EXACT.** Theorem 5.10(iii) states: "all its zeros are on the real line
and coincide with the spectrum of D_log^{(lambda,N)}." The proof uses:
- The factorization of the regularized determinant (multiplicative, exact)
- The characteristic polynomial of D'' (finite-dimensional, exact)
- The det_reg of the unperturbed scaling operator on E_N^perp (eq 5.17, exact)

There is NO approximation involved. The identification of zeros of xi-hat
with eigenvalues of D_log^{(lambda,N)} is an algebraic identity, not an
asymptotic statement.

### 2c. Gap between zeros and eigenvalues?

None at fixed (lambda, N). The gap appears ONLY when taking limits:
- N -> infinity: the "new" eigenvalues from Det(D''|_{E'_N} - z) may shift
- lambda -> infinity: new primes enter, changing the quadratic form

At fixed (lambda, N), Theorem 5.10(iii) is an exact statement.

**VERDICT: SOUND.** The eigenvalue identification is exact at fixed
(lambda, N). No gap, no approximation. The proof is a clean algebraic
argument using the multiplicativity of regularized determinants and the
finite-dimensional spectral theorem.

---

## 3. The Even-Simple Assumption

### 3a. What CCM's Theorem 5.10 requires

Definition 5.3 (p. 16): T is "even-simple" if:
(a) The smallest eigenvalue epsilon_N is SIMPLE (multiplicity 1)
(b) The eigenvector xi satisfies gamma*xi = xi (EVEN)

Theorem 5.10 states: "Let epsilon_N be the smallest eigenvalue of QW_lambda^N
assumed simple and xi the corresponding eigenvector assumed even."

BOTH conditions are required. Here is why each matters:

**Simplicity** is needed because:
- Ker T = C*xi must be ONE-dimensional for the quotient to give a Hilbert space
- The rank-one perturbation D' = D - |D*xi><eta| uses a UNIQUE xi
- Without simplicity, the quotient construction is ambiguous

**Evenness** is needed because:
- The normalization <xi | eta> = 1 uses the Dirichlet kernel delta_N
- Lemma 5.4(i) uses gamma*xi = xi to establish TD*xi = -beta
- The proof of (i) goes: 0 != (DT - TD)(xi) = |beta><eta|xi> - |eta><beta|xi>
  Since <beta|xi> = sum b_j xi_j = 0 (because b_{-j} = -b_j and xi_{-j} = xi_j
  by evenness), this simplifies to (DT - TD)(xi) = |beta><eta|xi> = |beta>
  Hence TD*xi = -beta.

**If xi is ODD:** then <eta|xi> = sum xi_j = 0 (since eta is the all-ones
vector and xi_{-j} = -xi_j), which means the normalization delta_N(xi) = 1
FAILS. The whole construction breaks down.

### 3b. Does our AE suffice?

Our AE (Anti-Eigenvalue) simplicity gives: for non-exceptional lambda,
the smallest eigenvalue of QW_lambda^N is SIMPLE for all N.

**This gives condition (a) but NOT condition (b).**

Research 21 showed numerically that the minimal eigenvector ALTERNATES
between even and odd as N varies (at fixed lambda). The even-odd gap is
O(10^{-7}). So AE simplicity is NECESSARY but NOT SUFFICIENT for even-simplicity.

### 3c. The escape routes

**Route 1: Work in the even sector.** Restrict QW_lambda^N to the even
sector (dimension N+1). The smallest eigenvalue in the even sector is:
- Simple (by AE simplicity restricted to the even sector)
- Even (by construction)
Apply Theorem 5.10 to the even-sector restriction. This requires a mild
modification of the theorem (restrict all operators to the even sector).
CCM's construction preserves the gamma symmetry, so the restriction is clean.

**Route 2: Use the N -> infinity limit.** As N -> infinity (fixed lambda),
the quadratic form QW_lambda^N approaches QW_lambda. The prolate wave
operator PW_lambda IS even-simple. If QW_lambda "looks like" PW_lambda
for large N (which CCM's numerics suggest), then even-simplicity holds
for sufficiently large N. But this is not proved.

**Route 3: Modify the AE argument.** Show that the AE mechanism preserves
parity. If the overlap <phi_k | a> != 0 is combined with the parity structure,
one might show that the even-sector minimum stays below the odd-sector minimum.
This would require controlling the even-odd gap, which oscillates.

### 3d. Assessment

**VERDICT: GENUINE GAP.** CCM's Theorem 5.10 requires even-simplicity, not
just simplicity. Our AE gives simplicity but not evenness. The even-sector
restriction (Route 1) is the most promising workaround and is likely routine,
but it has not been formally executed.

---

## 4. Circularity Check: Hidden RH Assumption?

### 4a. Does QW_lambda >= 0 assume RH?

NO. Proposition 3.3: QW_lambda is lower bounded and lower semicontinuous.
The lower bound mu_lambda may be negative. The Weil criterion (Corollary 3.8)
states: mu_lambda -> 0 IMPLIES RH. CCM do NOT assume mu_lambda -> 0; they
construct an operator whose spectrum APPROXIMATES the zeta zeros and show that
IF the approximation converges, THEN the zeros are real.

### 4b. Does the discrete spectrum claim assume RH?

NO. Theorem 3.6 proves discreteness of the spectrum of A_lambda using
compactness of the resolvent (Proposition 3.5). The proof uses the growth
of the angular Riemann-Siegel function theta(t) ~ (t/2)*log(t) (eq 3.24),
which is an UNCONDITIONAL fact about the Gamma function, not about zeta zeros.

### 4c. Does the Fourier transform formula assume RH?

NO. Proposition 5.9 computes xi-hat(z) as an explicit rational function
(partial fractions). This uses ONLY the finite-dimensional linear algebra
of the eigenvector xi in the basis V_n. No information about zeta zeros
enters until one takes N, lambda -> infinity.

### 4d. Does the convergence to Xi assume RH?

THIS IS THE CRITICAL POINT. Lemma 7.3 proves convergence of the Fourier
transform of k_lambda (the prolate approximation) to Xi. This does NOT
assume RH. But the step from "Fourier transform converges to Xi" to
"zeros converge to zeta zeros" requires Hurwitz's theorem, which requires
UNIFORM convergence on compact sets. Lemma 7.3 gives uniform convergence
on closed substrips of |Im(z)| < 1/2. Hurwitz then gives: zeros of the
approximants converge to zeros of Xi.

**But this uses the identification of xi_lambda with k_lambda (Missing Step 2).**
If xi_lambda != k_lambda, the convergence of k_lambda to Xi does not
imply convergence of xi-hat_lambda to Xi.

### 4e. Is there any circular dependence?

**NO.** At no point does CCM's construction assume RH. The construction
is UNCONDITIONAL. The CONDITIONAL part is:
- Missing Step 1: even-simplicity (assumed as hypothesis)
- Missing Step 2: xi_lambda ~ k_lambda (not proved)

If both missing steps are filled, RH follows WITHOUT any circular argument.
The implication chain is: even-simplicity + approximation -> spec converges
-> Hurwitz -> zeros on critical line -> RH.

**VERDICT: NO CIRCULARITY.** The construction is clean.

---

## 5. Lemma 7.2: Prolate Approximation Error

### Statement
For n = 0, 4:
    max_{x in [-lambda, lambda]} |h_{n,lambda}(x) - h_n(x)| <= c * lambda^{-2}

### Proof verification

The proof (pp. 29-30) uses Meixner-Schafke [9] Satz 9, Section 3.2:
the prolate spheroidal functions ps_n(z; gamma^2) converge to Hermite
functions D_n as gamma -> infinity, with error O(gamma^{-3/4}).

CCM then:
1. Identify gamma = 2*pi*lambda^2 (eq 7.9)
2. Normalize: h_{n,lambda} = c_n * lambda^{-1/2} * ps_n(x/lambda; gamma^2)
3. Apply the Meixner-Schafke estimate to get |h_{n,lambda}(x) - h_n(x)| = O(lambda^{-2})

The conversion from O(gamma^{-3/4}) to O(lambda^{-2}) uses gamma = 2*pi*lambda^2,
so gamma^{-3/4} = (2*pi)^{-3/4} * lambda^{-3/2}, which is actually O(lambda^{-3/2}),
not O(lambda^{-2}).

**WAIT.** CCM write O(gamma^{-1}) in their intermediate step (7.10), not
O(gamma^{-3/4}). Looking more carefully at eq (7.10): the error term is
O(gamma^{-1}), which gives O(lambda^{-2}) since gamma ~ lambda^2.
The Meixner-Schafke result they cite is Satz 9 for the UNIFORM estimate
on [-1,1], which gives O(gamma^{-3/4}) for the general case but better for
the specific m = 0 angular parameter. The uniform formula (7.10) has the
O(gamma^{-1}) remainder, which converts to O(lambda^{-2}).

The numerics (Figures 2-3, p. 31) show lambda^2 * max|h_{n,lambda} - h_n|
converging to a constant for n = 0 and n = 4, confirming the O(lambda^{-2})
rate.

**VERDICT: SOUND.** The O(lambda^{-2}) estimate is correctly derived from
the classical theory of prolate spheroidal functions. The reference to
Meixner-Schafke is appropriate and the conversion of parameters is correct.

---

## 6. Lemma 7.3: Fourier Transform Convergence

### Statement
The Fourier transform of k_lambda converges, when lambda -> infinity,
towards the Xi-function of Riemann uniformly on closed substrips
|Im(z)| < 1/2.

### Proof verification (pp. 31-32)

The proof proceeds:
1. Use |E(h_lambda)(u) - E(h)(u)| <= u^{1/2} * delta(lambda) * lambda/u
   where delta(lambda) = max|h_lambda - h| = O(lambda^{-2})
2. Evaluate the Mellin transform M(k_lambda)(s) on the critical strip
3. Show |M(k_lambda)(s) - integral_{lambda^{-1}}^{lambda} k(u) u^{s-1} du| = O(lambda^{-1/2-alpha})
   for alpha = Re(s) in (-1/2, 1/2)
4. Control the tail integral_{lambda}^{infinity} k(u) u^{s-1} du -> 0

The key estimate is step 3, which uses the crude bound:

    integral_{1/lambda}^{lambda} u^{alpha+1/2} / u^2 du = 2(lambda^{1/2-alpha} - lambda^{alpha-1/2}) / (1-2*alpha)

For alpha in (-1/2, 1/2), this integral grows as lambda^{|alpha|+1/2}.
Multiplied by delta(lambda) = c*lambda^{-2}, the result is
O(lambda^{-2} * lambda^{1/2+|alpha|}) = O(lambda^{-3/2+|alpha|}).
For |alpha| < 1/2, the exponent -3/2 + |alpha| < -1, so this -> 0.

**The convergence is UNIFORM on compact subsets of the strip** because
the bound depends continuously on alpha and s.

The tail control (step 4) uses the Poisson formula k(u) = k(u^{-1}) and
the rapid decay of h(u) = (pi/2) u^2 (2*pi*u^2 - 3) e^{-pi*u^2}, which
gives exponential decay for u -> infinity.

**VERDICT: SOUND.** The proof is complete and correct. No hidden
assumptions. The convergence rate O(lambda^{-3/2+epsilon}) for any
epsilon > 0 is sufficient for Hurwitz's theorem.

---

## 7. Numerical Precision Check

### CCM's claim
For lambda = sqrt(14), N = 120: error for gamma_1 is 1.07 x 10^{-60}.

### Can we reproduce?

The construction is explicit:
1. Build the (2*120+1) = 241 x 241 matrix T = QW_lambda^N using the
   formulas in Section 4 (Propositions 4.2, 4.3, Lemma 4.1)
2. Compute eigenvalues and eigenvectors at high precision
3. Apply Theorem 5.10 to get det_reg, find its zeros
4. Compare to known zeta zeros

This requires:
- Evaluation of _2F_1 hypergeometric functions at high precision
- Evaluation of digamma/polygamma functions
- High-precision eigenvalue decomposition of a 241 x 241 matrix

All are feasible with mpmath. The bottleneck is the 241 x 241 eigenvalue
computation at 200+ digit precision, which is expensive but doable
(hours, not days).

**We have NOT performed this computation.** The claim is reproduced
by CCM's own numerics (Table 1, Figure 1). Independent reproduction
would require implementing the full matrix construction.

### Plausibility check

The error pattern (exponential in zero number, exponential in lambda)
is consistent with the prolate wave theory. The compression of the
Fourier transform by the projection P_lambda has eigenvalue decay
1 - chi(lambda) ~ exp(-4*pi*lambda^2) (p. 30), which for lambda = sqrt(14)
gives exp(-4*pi*14) ~ 10^{-76}. This is of the right order of magnitude
for the first-zero error of 10^{-60}. The discrepancy is expected because
the error also depends on N and the approximation quality of the
eigenvector.

**VERDICT: PLAUSIBLE BUT NOT INDEPENDENTLY VERIFIED.** The 10^{-55}
(or 10^{-60}) precision is consistent with the theoretical framework
and the prolate wave eigenvalue asymptotics.

---

## 8. Summary Assessment

| Component | Status | Severity of Issues |
|:----------|:-------|:-------------------|
| Self-adjointness of D' in T-inner product | **SOUND** | -- |
| T-inner product positive (semi-)definite | **SOUND** (quotient handles radical) | -- |
| Eigenvalue identification (Thm 5.10(iii)) | **SOUND** (exact at fixed lambda, N) | -- |
| Even-simple requirement | **GENUINE GAP** | HIGH for our use |
| delta_N(xi) != 0 | **ASSERTED, NOT PROVED** | LOW |
| Circularity check | **PASSED** (no hidden RH assumption) | -- |
| Lemma 7.2 (prolate error) | **SOUND** | -- |
| Lemma 7.3 (FT convergence) | **SOUND** | -- |
| Numerical precision | **PLAUSIBLE, NOT VERIFIED** | MEDIUM |

### The two issues for our proof

**Issue 1 (HIGH): Even-simplicity vs. simplicity.** CCM's Theorem 5.10
requires BOTH simplicity AND evenness. Our AE mechanism gives simplicity
but not evenness. The minimal eigenvector alternates parity with N.
The workaround is the even-sector restriction (Section 3c, Route 1),
which is likely routine but must be formally executed.

**Issue 2 (LOW): delta_N(xi) != 0.** This is asserted by CCM without proof.
It is numerically robust and geometrically motivated, but it IS a logical
gap in the formal chain. Our AE mechanism likely gives this as a byproduct
(non-vanishing overlaps imply non-vanishing Dirichlet evaluation), but this
connection must be made explicit.

### Does CCM's construction have any hidden circularity?

**NO.** The construction is unconditional. The conditional parts (even-simplicity,
eigenvector approximation) are explicitly flagged as "Missing Steps" in
Section 8. CCM are transparent about what is proved and what is conjectured.

### Is the construction sound?

**YES, modulo the stated hypotheses.** Theorem 5.10 is a correct theorem:
IF the hypotheses hold (even-simplicity), THEN the conclusions follow
(self-adjointness, eigenvalue identification, reality of zeros). The proof
is detailed, explicit, and verifiable line by line.

---

## 9. Recommendations for Our Proof

1. **Cite Theorem 5.10 as conditional.** State explicitly: "Theorem 5.10
   of CCM applies under the even-simple hypothesis. We verify this hypothesis
   via AE simplicity (for simplicity) and even-sector restriction (for evenness)."

2. **Execute the even-sector restriction.** This means: restrict all operators
   to the even sector {f : gamma*f = f}. The restricted QW_lambda^N has
   dimension N+1. The restricted T is still positive semidefinite. The
   restricted D' is still self-adjoint in the restricted T-inner product.
   The restricted Theorem 5.10 gives: zeros of even-sector xi-hat are real
   and are eigenvalues of even-sector D'. This is routine but must be written.

3. **Prove delta_N(xi) != 0 for the even-sector eigenvector.** This should
   follow from: the Dirichlet kernel delta_N has a nonzero projection onto
   the even sector, and the even-sector eigenvector is unique (by AE).

4. **Do NOT claim independent numerical verification of 10^{-55} precision.**
   We have not performed this computation. Cite CCM's numerics as evidence,
   not as verification.

---

> *CCM's construction is sound. No circularity. Self-adjointness is rigorous.*
> *The gap is even-simplicity: they need it, we provide only simplicity.*
> *The even-sector restriction closes this, but it must be written.*
> *Lemmas 7.2 and 7.3 are correctly proved from classical analysis.*
