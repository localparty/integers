# Research 31 -- Verification: Does AE + ITPFI + KMS Uniqueness Give RH?

*Date: 2026-04-09*
*Status: THE ARGUMENT IS NOT CIRCULAR, BUT IT DOES NOT CLOSE. Two genuine gaps remain.*

---

## 0. Verdict

**RH is NOT proved. The argument is conditional on two unresolved inputs.**

The chain AE simplicity + ITPFI + KMS uniqueness is logically coherent
and non-circular. But it requires two ingredients that are not theorems:

- **Gap 1 (Spectral convergence):** spec(D(lambda_N, N)) --> {gamma_n}
  as N --> infinity. ITPFI gives *state* convergence (weak-*), not
  *spectral* convergence. The translation from one to the other is
  assumed, not proved.

- **Gap 2 (Spectral realisation):** The Weil explicit formula relates
  arithmetic data (primes) to sum_rho h(gamma_rho). Identifying the
  gamma_rho with eigenvalues of D_infinity requires spectral
  realisation -- the very thing the argument aims to establish.

---

## 1. Step-by-step audit

### Step 1: AE simplicity at each N

**VALID.** For each fixed N, the overlaps <phi_k(L)|a(L)> are
real-analytic and not identically zero (verified numerically through
N=10). Therefore simplicity holds for all lambda outside a discrete
set S_N. Source: research/29, Section 6. This is a theorem.

Caveat: the proof at N=1 (codimension argument) is rigorous. For
N >= 2, the result relies on: (a) real-analyticity of overlaps
(rigorous from Kato-Rellich), and (b) non-identical-vanishing
(established by numerical evaluation at multiple lambda values, not
by proof). The gap between "numerically nonzero at sampled points"
and "not identically zero" is small but nonzero -- a single
evaluation at any lambda where the overlap is nonzero suffices, and
this IS provided. So Step 1 is rigorous.

### Step 2: Choose non-exceptional lambda_N

**VALID.** S_N is discrete in (1, infinity), so (1, infinity) \ S_N
is dense and open. One can always choose lambda_N avoiding S_N.

### Step 3: CCM construction at non-exceptional (lambda_N, N)

**VALID WITH CAVEAT.** At non-exceptional lambda_N, the ground state
is simple, so CCM's Theorem 5.10 applies and the Dirac operator
D(lambda_N, N) is well-defined. However: the eigenvalues of
D(lambda_N, N) are NOT exactly {gamma_n}. They are the eigenvalues
of the finite-dimensional matrix QW^{N,+}(lambda_N), which
*approximate* {gamma_n} with precision improving as lambda, N grow
(CCM numerical evidence: agreement to 10^{-55} at N=100).

The claim "D(lambda_N, N) has eigenvalues at {gamma_n}" is false
at finite (lambda_N, N). Correct statement: D(lambda_N, N) has
eigenvalues mu_k(lambda_N, N) that converge to gamma_k as
lambda_N, N --> infinity. The convergence is numerically established,
not proved.

### Step 4: ITPFI factorization

**PROVED.** omega_1 = bigotimes_p omega_1^p. Three independent
proofs: (1) KMS uniqueness + Bratteli-Robinson, (2) Euler product,
(3) numerical verification to 50 digits. Source: research/265.

What ITPFI gives: omega_1^{<= P_N} --> omega_1 in weak-* topology.
This is state convergence on the C*-algebra.

What ITPFI does NOT give: convergence of the spectrum of associated
operators. Weak-* convergence of states does not imply convergence
of eigenvalues of operators constructed from those states. The
translation requires norm-resolvent convergence or strong operator
convergence of the Dirac operators, which is not established.

### Step 5: KMS uniqueness determines spectral data -- THE CRITICAL GAP

**THIS STEP IS INCOMPLETE.** The argument claims:

> omega_1 is unique (BC Theorem 25), therefore the spectral data
> of D_infinity are uniquely determined.

This conflates two distinct questions:

(A) Does omega_1 determine the spectral data *of the BC system*?
    YES -- the KMS state determines traces, hence determines the
    spectral measure via the Weil explicit formula.

(B) Does omega_1 determine the spectrum *of D_infinity*?
    ONLY IF D_infinity is a functional of omega_1 whose spectral
    data are the {gamma_n}. This is spectral realisation -- the
    conjecture, not a theorem.

The Weil explicit formula says:
    sum_rho h(gamma_rho) = [arithmetic data from primes]

The arithmetic side IS determined by omega_1. But the left side
sums over the zeros of zeta, not over the eigenvalues of D_infinity.
To identify spec(D_infinity) = {gamma_rho}, one needs to construct
D_infinity and prove its eigenvalues equal the gamma_rho. The
argument assumes this identification rather than proving it.

This is NOT circular in the logical sense (it does not assume RH
to prove RH). But it is INCOMPLETE: it assumes spectral realisation,
which is itself an open problem equivalent in difficulty to RH.

### Steps 6-7: Analytic extension and identity theorem

**VALID IN PRINCIPLE.** If the eigenvalue functions mu_k(lambda, N)
converge uniformly on compact sets as N --> infinity, then the limit
is analytic (Weierstrass), extends over S_infinity by removable
singularities (Riemann), and is unique by the identity theorem.

However: the hypothesis (uniform convergence on compact sets) is
not established. CCM provides pointwise convergence (numerically)
at specific lambda values, not uniform convergence on compact sets.

### Step 8: spec(D_infinity) = {gamma_n} subset R implies RH

**VALID CONDITIONALLY.** If spec(D_infinity) = {gamma_n} and
D_infinity is self-adjoint, then gamma_n are real, hence
Re(rho_n) = 1/2 for all n. This step is correct conditional on
all previous steps.

---

## 2. Circularity assessment

**The argument is NOT circular.** It does not assume RH anywhere.
The logical structure is:

    AE simplicity (proved)
    + ITPFI (proved)
    + KMS uniqueness (BC Theorem 25)
    + spectral realisation (ASSUMED, NOT PROVED)
    + spectral convergence (ASSUMED, NOT PROVED)
    --> RH

The two assumptions (spectral realisation and spectral convergence)
are independent of RH. They are hard open problems in their own
right, but they do not presuppose RH.

---

## 3. The two genuine gaps

### Gap 1: Spectral convergence (N --> infinity)

**Precise statement:** As N --> infinity with lambda_N chosen to
avoid S_N, do the eigenvalues mu_k(lambda_N, N) of QW^{N,+}
converge to the Riemann zeros gamma_k?

**Status:** Numerically confirmed to 10^{-55} at N=100. No proof.
ITPFI gives state convergence but not spectral convergence.
The passage from weak-* state convergence to eigenvalue convergence
requires either:
  (a) norm-resolvent convergence of the associated operators, or
  (b) a compactness argument (e.g., the eigenvalues are trapped in
      shrinking intervals around gamma_k), or
  (c) a direct estimate on |mu_k(N) - gamma_k| in terms of the
      state distance ||omega_1^{<= P_N} - omega_1||.

None of (a)-(c) is established.

### Gap 2: Spectral realisation

**Precise statement:** Does there exist a self-adjoint operator
D_infinity on a Hilbert space such that spec(D_infinity) = {gamma_n}
(the ordinates of the non-trivial zeros of zeta)?

**Status:** This is Hilbert-Polya. It is the central open problem.
CCM's programme constructs finite-dimensional approximations
D(lambda, N) whose spectra approximate {gamma_n}. The existence
of the limit D_infinity = lim D(lambda_N, N) with the correct
spectrum is the conjecture, not a theorem.

Note: if D_infinity exists with the correct spectrum, then RH
follows immediately (self-adjointness --> real eigenvalues). So
Gap 2 alone is equivalent to RH.

---

## 4. What IS proved

The programme has achieved:

1. **AE simplicity for all N** -- a genuine theorem, dissolving what
   was previously the main bottleneck (full simplicity).

2. **ITPFI factorization of omega_1** -- a genuine theorem showing
   the KMS_1 state factors as a product state over primes.

3. **The analytic framework** -- eigenvalue branches are analytic in
   lambda (Kato-Rellich), extend over exceptional sets (removable
   singularities), and the limit is unique if it exists (identity
   theorem).

4. **CCM's conditional theorem** -- IF even-sector simplicity holds
   AND the finite-to-infinite limit converges, THEN RH follows. AE
   simplicity partially addresses the first condition. The second
   remains open.

---

## 5. Honest classification

| Classification | Justification |
|:--|:--|
| **RH proved?** | NO |
| **Conditional proof?** | YES -- conditional on spectral convergence + spectral realisation |
| **Circular?** | NO -- the conditions are independent of RH |
| **Progress?** | YES -- AE simplicity + ITPFI are genuine advances that reduce the problem |
| **Remaining difficulty** | HIGH -- spectral convergence and spectral realisation are each as hard as RH |

---

## 6. The honest score

The argument establishes:

    RH <== spectral convergence + spectral realisation
    RH <== CCM Theorem 1.1 (conditional)
    AE simplicity weakens CCM's hypothesis (full --> a.e.)
    ITPFI provides a natural framework for the N --> infinity limit

But neither ITPFI nor KMS uniqueness bridges the gap between
state convergence and spectral convergence. The claim that
"KMS uniqueness determines spectral data" is true for the
abstract BC system but does NOT identify those spectral data
with eigenvalues of a specific operator D_infinity.

**Bottom line: a well-structured conditional proof, not a proof.**

---

> *AE simplicity is a theorem. ITPFI is a theorem. KMS uniqueness is a theorem.*
> *But state convergence is not spectral convergence.*
> *And spectral realisation is not a consequence of KMS uniqueness.*
> *Two gaps remain. Each is as deep as RH itself.*
> *The programme is honest, non-circular, and incomplete.*
