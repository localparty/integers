# Approach C: Prolate Wave Operator Limit

*Date: 2026-04-09*
*Status: PARTIAL -- Slepian transfer works for large N at each fixed lambda, but the convergence QW^{N,+} -> PW is NOT in the correct direction. The approach yields a conditional result, not a full proof.*

---

## 1. Slepian's theorem (precise statement)

**Theorem (Slepian 1961, Landau-Pollak 1961-62).** Let
P_T : L^2(R) -> L^2(R) be the time-limiting operator
(multiplication by 1_{[-T,T]}) and P_Omega the band-limiting
operator (Fourier multiplier by 1_{[-Omega, Omega]}). The
time-frequency concentration operator

    B_{T,Omega} = P_T P_Omega P_T

is a compact self-adjoint operator on L^2([-T,T]) with
eigenvalues 1 > chi_0 > chi_1 > chi_2 > ... > 0.

**All eigenvalues are simple.**

*Proof mechanism:* The operator B_{T,Omega} commutes with the
prolate spheroidal differential operator

    F_c y = d/dx [(1-x^2) dy/dx] + c^2(1-x^2) y

where c = pi*T*Omega (after scaling to [-1,1]). This is a
Sturm-Liouville operator on (-1,1). The Sturm-Liouville
oscillation theorem guarantees that:
- The n-th eigenfunction ps_n has exactly n zeros in (-1,1)
- All eigenvalues are simple
- The eigenfunctions ps_n have parity (-1)^n

Since B and F commute and share eigenfunctions, simplicity of
F's spectrum implies simplicity of B's spectrum. In particular,
the ground state ps_0 is even and nodeless.

**References:**
- Slepian & Pollak, Bell Syst. Tech. J. 40 (1961), 43-63 [CCM ref 15]
- Landau & Pollak, Bell Syst. Tech. J. 40 (1961), 65-84
- Fuchs, J. Math. Anal. Appl. 9 (1964), 317-330 [CCM ref 8]

---

## 2. CCM's prolate wave operator and its connection to QW

### 2.1 The operator

CCM define (eq 7.5):

    PW_lambda := -d_x( (lambda^2 - x^2) d_x ) + (2*pi*lambda*x)^2

acting on L^2([-lambda, lambda]). After the substitution z = x/lambda,
this becomes a rescaled prolate spheroidal operator with parameter
gamma = 2*pi*lambda^2 (eq 7.9).

The eigenfunctions h_{n,lambda} of PW_lambda:
- Have the same labeling as Hermite functions h_n
- Are even for n even, odd for n odd
- Satisfy h_{n,lambda}(x) -> h_n(x) as lambda -> infinity
  with error O(lambda^{-2}) uniformly on [-lambda, lambda]
  (Lemma 7.2(i))

### 2.2 What Lemma 7.2 says

**Lemma 7.2 (CCM).** The eigenfunctions h_{n,lambda} of PW_lambda,
suitably normalized, satisfy for n = 0, 4:

    max_{x in [-lambda, lambda]} |h_{n,lambda}(x) - h_n(x)| <= c * lambda^{-2}

The proof uses the asymptotic expansion of prolate spheroidal
functions ps_n(z; gamma^2) from Meixner-Schafke (1954) [CCM ref 9],
Satz 9, which gives:

    ps_n(x/lambda; gamma^2) = (4gamma/pi)^{1/4} * [(2n+1)n!]^{-1/2}
                               * D_n((2gamma)^{1/2} x/lambda) + O(gamma^{-3/4})

where D_n are Hermite functions.

### 2.3 What Lemma 7.3 says

**Lemma 7.3 (CCM).** The Fourier transform of k_lambda converges,
when lambda -> infinity, towards the Xi-function of Riemann
uniformly on closed substrips of |Im(z)| < 1/2.

Here k_lambda(u) := E(h_lambda)(u) for u in [lambda^{-1}, lambda],
where h_lambda is the linear combination of h_{0,lambda}, h_{4,lambda}
with vanishing integral, and E(f)(u) = u^{1/2} sum_{n>=1} f(nu).

### 2.4 Critical observation: the direction of convergence

CCM's convergence results are:

    h_{n,lambda} -> h_n     as lambda -> infinity  (Lemma 7.2)
    k_lambda -> Xi          as lambda -> infinity  (Lemma 7.3)

These are convergences **in the lambda -> infinity direction at
fixed mode number n**. They say nothing directly about
QW_lambda^{N,+} converging to PW_lambda as N -> infinity.

**The N -> infinity limit and the lambda -> infinity limit are
different limits that involve different mechanisms.**

---

## 3. Does QW_lambda^{N,+} -> PW_lambda as N -> infinity?

### 3.1 What is known

The connection between QW_lambda and PW_lambda is established
through the trace formula (CCM ref [3], Connes 1999):

    QW_lambda = sum of W_{0,2}, W_R, W_p terms

The QW matrix is built from the Weil explicit formula using a
finite number of primes p <= lambda. The PW operator arises from
the "archimedean" contribution alone (the W_{0,2} and W_R terms
in a certain limit).

CCM Section 8 and the Outlook (Section 7) describe the relationship
as follows:

> "the eigenfunction associated with the lowest eigenvalue of
> QW_lambda is well approximated by prolate spheroidal wave
> functions" (p. 27)

This is a statement about the **eigenvector** of QW being close
to PW eigenvectors, not about the **operators** being close in norm.

### 3.2 The truncation limit N -> infinity

The space E_N = span{V_n : |n| <= N}. As N -> infinity, E_N
exhausts L^2([lambda^{-1}, lambda], d*u). The even sector
E_N^+ = span{C_0, C_1, ..., C_N} exhausts L^2_even.

The QW matrix restricted to E_N^+ is an (N+1) x (N+1) matrix
QW_lambda^{N,+}. As N -> infinity, does this converge to an
operator on L^2_even?

**Yes, but with caveats.** The quadratic form QW_lambda defines
a bounded operator on L^2([lambda^{-1}, lambda], d*u) (by the
Weil explicit formula, the entries tau_{n,m} are bounded). The
truncation QW^{N,+} is the compression of this operator to E_N^+.
By the Dirichlet kernel convergence (CCM Lemma 5.5, eq 5.10),
for f in Dom(D_log^(lambda)):

    <delta_N | f> -> f(lambda) as N -> infinity

This gives strong operator convergence of the truncation, but
**not norm convergence** in general.

### 3.3 The limiting operator

The infinite-dimensional limit (N -> infinity) of QW_lambda^{N,+}
at fixed lambda is the even-sector compression of QW_lambda acting
on L^2_even([lambda^{-1}, lambda]). This is NOT the same as
PW_lambda. The operators QW_lambda and PW_lambda are different
objects:

- QW_lambda: built from the Weil explicit formula (involves primes)
- PW_lambda: the prolate spheroidal differential operator (no primes)

Their relationship is that PW_lambda **approximates** QW_lambda
as lambda -> infinity (more primes contribute, their effect
averages out, and the archimedean term dominates). But at fixed
lambda, they are genuinely different.

### 3.4 Conclusion on the N-limit

**The limit QW_lambda^{N,+} -> PW_lambda as N -> infinity does
NOT hold.** The N -> infinity limit gives QW_lambda^{infty,+}
(the full even-sector Weil form at parameter lambda), not PW.
The PW approximation arises in the lambda -> infinity limit.

---

## 4. Revised approach: double limit

### 4.1 The correct convergence path

The correct statement is a **double limit**:

    QW_lambda^{N,+}  --[N->inf]-->  QW_lambda^{inf,+}
                                         |
                                    [lambda->inf]
                                         |
                                         v
                                    PW  (prolate)

Step 1 (N -> infinity): compression converges to full operator.
Step 2 (lambda -> infinity): Weil form approaches prolate form.

Slepian simplicity lives in PW. To transfer it to QW_lambda^{N,+},
we need both limits to preserve simplicity.

### 4.2 Step 2: lambda -> infinity preserves simplicity?

By Lemma 7.2, the eigenfunctions of PW_lambda converge to Hermite
functions with error O(lambda^{-2}). The eigenvalues of PW_lambda
are simple for all lambda (Slepian). The spectral gap between
chi_0(lambda) and chi_1(lambda) is bounded below by a positive
function of lambda.

For the Weil form QW_lambda, CCM's numerical evidence (Section 7,
Table on p. 27) shows that the smallest eigenvalue epsilon_lambda
decreases super-exponentially:

    epsilon_lambda ~ exp(-4*pi*lambda^2)

The *gap* between the two smallest even-sector eigenvalues also
decreases (research/22: from 10^{-4} at N=2 to 10^{-49} at N=40).

**Key problem:** The eigenvalues of QW_lambda^{N,+} are NOT the
same as the eigenvalues of PW_lambda. The QW eigenvalues are much
smaller (they track epsilon_lambda ~ e^{-c*lambda^2}), while PW
eigenvalues chi_n(lambda) lie in (0,1). The gap structure is
completely different.

### 4.3 What Kato IV.3.5 requires

**Theorem (Kato, Perturbation Theory IV.3.5).** Let A_n -> A
in norm resolvent sense. If A has an isolated eigenvalue mu with
finite multiplicity m and spectral gap delta > 0, then for n
sufficiently large, A_n has exactly m eigenvalues (counting
multiplicity) in (mu - delta/2, mu + delta/2).

**Corollary:** If m = 1 (simple eigenvalue) and the convergence
is in operator norm with ||A_n - A|| < delta/2, then A_n has
a simple eigenvalue near mu.

**Application to our problem:** We would need:
- (a) ||QW^{N,+} - PW^+|| -> 0 as SOME parameter -> infinity
- (b) Gap(PW^+) > 0 (YES, by Slepian)
- (c) The norm difference is eventually < Gap(PW^+)/2

Condition (a) FAILS because QW and PW are fundamentally different
operators with different spectral scales. There is no parameter
regime where ||QW - PW|| -> 0 in operator norm.

---

## 5. What CAN be extracted from the prolate connection

### 5.1 Eigenvector approximation (valid)

CCM's actual claim is weaker but still useful: the minimal
eigenvector xi_lambda of QW_lambda is well approximated by
k_lambda (the prolate-derived function):

    ||xi_lambda - c * k_lambda|| = O(lambda^{-2})    (Lemma 7.2 + 7.3)

This is an **eigenvector** approximation, not an operator
approximation. It says the *shape* of the ground state of QW
is prolate-like, not that QW itself is close to PW.

### 5.2 Simplicity from non-degeneracy of the approximation (heuristic)

If xi_lambda is well-approximated by k_lambda, and k_lambda
is a simple eigenvector of PW_lambda (with definite even parity
and no near-crossings), then a perturbative argument suggests
xi_lambda is also simple.

But making this rigorous requires bounding the perturbation
QW - PW in a norm compatible with the spectral gap, which
brings us back to the problem of condition (a) above.

### 5.3 The Sturm-Liouville structure (partial transfer)

The prolate operator PW_lambda is Sturm-Liouville, and simplicity
follows from the oscillation theorem. The even-sector restriction
of QW_lambda^{N,+} is NOT Sturm-Liouville (it's a matrix, not
a second-order ODE). However:

The Cauchy structure of the matrix (Lemma 5.1) provides a
discrete analog of the oscillation property. Generalized Cauchy
matrices tau_{i,j} = (b_i - b_j)/(i-j) with strictly ordered
b_i have interlacing eigenvalues, which is the discrete version
of Sturm-Liouville oscillation.

**This suggests the simplicity mechanism may be Cauchy structure
(Approach A) rather than prolate convergence (Approach C).**

---

## 6. The computer-assisted proof attempt

### 6.1 Structure of the argument

Despite the failure of direct operator convergence, a hybrid
argument can be attempted:

**Claim.** For each fixed lambda > 1, there exists N_0(lambda)
such that QW_lambda^{N,+} has a simple minimum eigenvalue for
all N >= 1.

**Proposed proof (computer-assisted):**

*Part 1 (large N):* For N >= N_0(lambda), the eigenvector
xi_lambda^{N,+} converges to xi_lambda^{inf,+} (the ground state
of QW_lambda^{inf,+}). If QW_lambda^{inf,+} has a simple ground
state with gap delta_inf > 0, then for N large enough,
||QW^{N,+} - QW^{inf,+}|| < delta_inf / 2, and simplicity
transfers by Kato IV.3.5.

*Part 2 (small N):* For 1 <= N < N_0(lambda), verify simplicity
numerically at 120-digit precision.

### 6.2 Problems with this argument

**Problem 1: Does QW_lambda^{inf,+} have a simple ground state?**

This is the infinite-dimensional version of the conjecture. It is
NOT the prolate operator (Section 3.4). We would need to prove
simplicity for QW_lambda^{inf,+} independently. This is circular
-- we're trying to prove simplicity of the truncation by assuming
simplicity of the limit.

**Problem 2: What is N_0(lambda)?**

Even if the infinite-dimensional simplicity holds, the threshold
N_0 depends on the gap delta_inf of QW_lambda^{inf,+}. From the
numerical data (research/22):

    delta^ev(N=2, lambda=sqrt(10))  = 1.06 x 10^{-4}
    delta^ev(N=40, lambda=sqrt(14)) = 1.40 x 10^{-49}

The gap decreases exponentially: delta^ev ~ C * exp(-alpha * N).
If it converges to delta_inf > 0, the convergence is extremely
slow, and N_0 could be astronomically large. The numerical data
cannot distinguish delta_inf > 0 from delta_inf = 0.

**Problem 3: Is the computer-assisted verification rigorous?**

For the finite verification (Part 2) to be rigorous, one needs:
- Interval arithmetic (not just multiprecision floating-point)
- Certified eigenvalue bounds (e.g., Lehmann-Maehly or
  verified Krawczyk methods)
- A proof that the matrix entries are computed exactly (they
  involve integrals of log|zeta|, which require rigorous bounds)

The current 120-digit mpmath computation is strong numerical
evidence but not a computer-assisted proof in the sense of
Hales (Flyspeck) or Tucker (Lorenz attractor). Converting it
to a rigorous verification is feasible but non-trivial.

### 6.3 Assessment of the computer-assisted approach

| Requirement | Status |
|:------------|:-------|
| Simplicity of QW^{inf,+} | UNPROVED (not equivalent to PW) |
| Gap delta_inf > 0 | UNKNOWN (numerical: gap -> 0 exponentially?) |
| N_0(lambda) computable | NO (depends on unknown delta_inf) |
| Finite verification rigorous | NO (mpmath, not interval arithmetic) |
| **Overall** | **NOT A PROOF** |

---

## 7. The honest assessment

### 7.1 Does Slepian transfer?

**Partially.** Slepian proves simplicity for PW_lambda (the prolate
operator) for all lambda. The prolate eigenfunctions approximate
the QW eigenfunctions (Lemma 7.2). But the approximation is in
the lambda -> infinity direction, not the N -> infinity direction.
The operators QW and PW are fundamentally different (QW involves
primes; PW does not), and no norm convergence QW -> PW holds.

The Slepian structure provides strong *heuristic* support for
even-sector simplicity of QW, and it correctly predicts the
qualitative behavior (even ground state, exponentially small
eigenvalue). But it does not yield a proof.

### 7.2 What is N_0?

**Undefined.** The threshold N_0(lambda) requires knowledge of
delta_inf (the gap of QW_lambda^{inf,+}), which is unknown.
Numerically, the gap decreases as exp(-alpha*N), and whether it
has a positive limit is precisely the content of the conjecture.

### 7.3 Is the computer-assisted proof valid?

**No.** It has three gaps:
1. The infinite-dimensional simplicity (Part 1 hypothesis) is
   unproved and not implied by Slepian.
2. The finite verification (Part 2) uses multiprecision
   floating-point, not certified interval arithmetic.
3. The threshold N_0 is not computable from current data.

A rigorous computer-assisted proof would require resolving all
three issues. Issue 1 is the hardest -- it requires a proof of
simplicity for the full (non-truncated) even-sector Weil operator,
which is harder than the finite-dimensional version.

### 7.4 Is the conjecture proved?

**No.** Approach C does not close the conjecture. It provides:

- Structural motivation (the prolate analog IS simple)
- Eigenvector approximation (the shape is prolate-like)
- The correct qualitative picture (even ground state, simple)

But it does not provide a rigorous proof, because:
- QW != PW (different operators)
- The convergence QW -> PW is in lambda, not in N
- No norm convergence holds between QW and PW
- The computer-assisted strategy has unfilled prerequisites

---

## 8. What Approach C actually establishes

**Theorem (Partial).** For each lambda > 1, the minimal
eigenvector of QW_lambda (in the full space, as N -> infinity)
is approximated by the prolate function k_lambda with error
O(lambda^{-2}) in sup-norm. The prolate function k_lambda is
even. Therefore, for lambda sufficiently large, the minimal
eigenvector of QW_lambda is even.

*Proof.* Lemma 7.2 gives ||h_{n,lambda} - h_n|| = O(lambda^{-2}).
Lemma 7.1 identifies h = linear combination of h_0, h_4 as the
function whose Fourier transform gives Xi. The map E (eq 7.2)
produces k_lambda = E(h_lambda) which approximates E(h) = k.
Since h_0 and h_4 are even Hermite functions, h is even, hence
k is even. For lambda large enough that the O(lambda^{-2}) error
is smaller than the even/odd gap, the minimal eigenvector must
be even.

**But this only gives evenness, not simplicity within the even
sector.** And it only works for large lambda, not for all lambda > 1.

---

## 9. Comparison of approaches

| Approach | What it gives | What it lacks |
|:---------|:--------------|:--------------|
| A (Cauchy) | Simplicity from matrix structure | Proof that b-values are strictly ordered |
| B (Analytic perturbation) | No crossings generically | Proof that no crossings occur for lambda > 1 |
| **C (Prolate limit)** | **Evenness for large lambda** | **Simplicity; covers only lambda >> 1** |
| D (Monotonicity) | Gap positive if monotone | Gap not proved monotone |
| E (Functional equation) | Parity of eigenvectors | Does not force simplicity |

**Approach C is the weakest of the five for proving simplicity.**
Its strength is establishing evenness of the ground state; its
weakness is that the operator approximation is too loose to
transfer the simplicity property.

### 9.1 The most promising combination

**C + A:** Use Approach C to establish evenness (for large lambda),
then Approach A (Cauchy structure) to establish simplicity within
the even sector. The Cauchy structure is a finite-dimensional
matrix property that does not require an infinite-dimensional
limit.

---

## 10. Rating

| Component | Rating | Notes |
|:----------|:-------|:------|
| Slepian simplicity of PW | 10/10 | Classical theorem, rigorously proved |
| PW approximates QW eigenvectors | 8/10 | CCM Lemma 7.2, O(lambda^{-2}) error |
| Operator norm QW -> PW | 2/10 | FALSE: different operators |
| Kato spectral transfer | 2/10 | Inapplicable: no norm convergence |
| Computer-assisted proof | 3/10 | Multiple unfilled prerequisites |
| **Approach C overall** | **3/10** | Provides intuition, not proof |

**The conjecture remains OPEN after Approach C.**
