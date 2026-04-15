# Research 45 -- FINAL ADVERSARIAL REVIEW

*Date: 2026-04-09*
*Role: FINAL ADVERSARIAL REVIEWER. Last line of defense.*
*Mission: Kill this proof or confirm it stands.*

---

## Preamble

I have read the complete chain (Strategy 24), the first adversarial
review (Research 41), all three wound closures (Research 42, 43, 44),
the Cartwright argument (Research 39), the secular induction
(Research 33), the CCM+ITPFI programme (Strategy 11), the kill list
(Strategy 15), and the Arithmetic Theorem (Strategy 16). I have also
read the source code for both numerical verifications
(uniform_levin_bound.py and mpmath_rate_comparison.py) and the
earlier Lead H (Research 37) for context.

I will now attack every wound closure as hard as I can.

---

## WOUND 1: The Levin Constant Argument

### The claim

C(g_k) <= C(N), independent of K, because ||phi_k|| = 1 and
|g_k(xi)| <= sqrt(N) by Cauchy-Schwarz, regardless of K.

### Attack 1: The Levin constant is NOT just about the sup bound

Research 42 bounds three quantities:
  (i)   |g_k(0)| <= sqrt(N)
  (ii)  sup_{R} |g_k| <= sqrt(N)
  (iii) Jensen integral <= (1/2) log N + L*R

But the LEVIN ZERO-COUNTING FORMULA (Levin, Ch. V, Thm 1) is:

    n(r) = (1/2pi) integral_0^{2pi} log|f(r e^{i theta})| d theta
           - log|f(0)| + O(1)

The "+C" in n(T) <= (sigma/pi)*T + C comes from Jensen's formula,
and C contains the term **-log|f(0)|** (with a MINUS sign). When
|f(0)| is small, -log|f(0)| is LARGE AND POSITIVE, inflating C.

Research 42 bounds |g_k(0)| from ABOVE: |g_k(0)| <= sqrt(N). This
gives the trivial bound -log|g_k(0)| >= -log(sqrt(N)) = -(1/2)log N.
But this is a LOWER bound on -log|g_k(0)|, not an UPPER bound.

**The critical question:** Can |g_k(0)| be very SMALL, making
-log|g_k(0)| very LARGE?

g_k(0) = sum_i phi_k[i]. For non-leading eigenvectors of a real
symmetric matrix, the components sum to values near zero -- this is
the generic situation. If phi_k is orthogonal to the all-ones vector,
then g_k(0) = 0 EXACTLY, and -log|g_k(0)| = +infinity.

**Research 42 does NOT address this.** The upper bound
|g_k(0)| <= sqrt(N) does not prevent |g_k(0)| from being zero or
exponentially small.

### Attack 2: What happens when g_k(0) = 0?

If g_k(0) = 0, the standard Levin formula requires modification:
one uses g_k(z)/z^m where m is the order of the zero at z = 0.
The modified counting formula is:

    n(T) <= (sigma/pi)*T + C'   where C' involves log|g_k^{(m)}(0)/m!|

For g_k(0) = 0 but g_k not identically zero, m >= 1, and
g_k^{(m)}(0) involves sum_i phi_k[i] * x_i^m. This sum CAN be
bounded: |g_k''(0)| = |sum_i phi_k[i] x_i^2| <= sqrt(N) * ||x^2||
= sqrt(N) * (sum x_i^4)^{1/2} <= sqrt(N) * L^2 * sqrt(N) = N * L^2.

So the modified constant C' <= m*log(1) + log(N*L^2) or similar.
This IS bounded by a function of N alone.

**Verdict on Attack 1-2:** The SPECIFIC argument in Research 42 has a
gap: it does not account for the -log|g_k(0)| term when g_k(0) is
small or zero. HOWEVER, the gap is FILLABLE: the modified Jensen
formula handles zeros at the origin by dividing out z^m, and the
resulting constant still depends only on N and L, not on K. The fix
requires slightly more work than Research 42 provides, but the claim
C <= C(N) is CORRECT in substance.

**STATUS: The argument has a presentational gap but the conclusion
is correct. WOUND 1 IS CLOSED, but the write-up needs the
g_k(0) = 0 case handled explicitly.**

### Attack 3: Could g_k(0) be nonzero but exponentially small?

For a "typical" non-leading eigenvector of B_K, the component sum
sum_i phi_k[i] is not exactly zero but could be exponentially small
in N (if phi_k is "nearly orthogonal" to the all-ones vector). Then
-log|g_k(0)| ~ alpha*N, and C grows linearly in N, which is
ALREADY captured by C <= C(N). The claim is C is uniform in K, not
in N. Growing with N is fine -- the induction is for fixed N.

**This attack fails.** C growing with N is permitted. Only growth
with K would be fatal.

### Attack 4: The counting argument for "bad primes" fraction

Research 42 argues that the fraction of bad primes tends to zero:

    N * (sigma * log K / pi + C(N)) / (K + 1) -> 0 as K -> infinity

This is correct for fixed N. But the argument requires that the
Levin bound counts ALL zeros of g_k in [-T, T], not just zeros at
{log p}. The zeros at {log p} are a SUBSET of all zeros, so the
bound is valid (it overcounts, which is fine for an upper bound).

The argument that K_0(N) exists is correct: for K sufficiently large
(depending on N), more primes are available than the Levin bound
allows for bad ones. The induction becomes self-sustaining.

**This attack fails.** The counting argument is correct.

### Attack 5: What about K < K_0(N)?

For the finitely many steps K = 0, 1, ..., K_0(N)-1, the chain
requires EXPLICIT VERIFICATION that no bad primes occur. This is
delegated to numerical computation at 120 digits.

**This is an engineering gap, not a mathematical one.** The number
of steps to verify is finite and computable. Interval arithmetic
would make this rigorous. The chain acknowledges this (Strategy 24,
"What remains," item 1).

### WOUND 1 FINAL VERDICT: **CLOSED (with minor presentational gap)**

The core claim -- C is uniform in K for fixed N -- is correct.
The g_k(0) = 0 case needs to be handled in the write-up via the
modified Jensen formula, but this is routine. The counting argument
for K_0(N) is valid. The finite verification for K < K_0(N) is
engineering, not mathematics.

---

## WOUND 2: The Rate Comparison / Bridge

### The claim

The discretization error (Chebyshev spectral method) decays as
exp(-alpha*N) with alpha ~ 3.5, while the eigenvalue gap decays as
exp(-beta*N) with beta ~ 0.3-0.5 (saturating), giving alpha/beta ~ 10.
Crossover at N ~ 54.

### Attack 1: The computation uses a MODEL, not the actual CCM operator

The matrix B in mpmath_rate_comparison.py is:

    B = Cauchy(x_i, x_j) + sum_{p <= 29} (log p / sqrt p) * v_p v_p^T

with a shift of 0.01 in the Cauchy kernel. The actual CCM operator
QW_lambda on L^2([lambda^{-1}, lambda]) involves:
  - The digamma function (not 1/(x+y))
  - The Riemann-Siegel theta function
  - The explicit formula with exact Weil coefficients

**The model is an APPROXIMATION to the actual CCM quadratic form.**
The Cauchy kernel 1/(x_i + x_j) is the LEADING TERM of the
archimedean part, but the digamma function has additional structure.
The shift 0.01 is ad hoc regularization.

**Question:** Does the saturation of the gap at 10^{-51} persist for
the ACTUAL CCM operator? The saturation could be an artifact of the
simplified model. The actual operator might have a gap that closes
to zero.

**Severity: MEDIUM.** The model captures the qualitative structure
(Cauchy + rank-one prime perturbations), and the saturation phenomenon
has a clear mechanism (the archimedean and prime data are "independent"
in a transcendence-theoretic sense). But the specific numerical value
10^{-51} and the specific rates alpha, beta apply to the model, not
necessarily to the actual CCM construction.

### Attack 2: 10^{-51} is the precision floor, not a physical floor

The computation uses mp.dps = 50 (50 decimal digits). The reported
gap saturation is at ~ 10^{-51}. This is ONE DIGIT below the
precision setting. The gap "saturation" could be the point where
the eigenvalue computation loses all significant digits, not a
genuine mathematical floor.

**This is a SERIOUS concern.** To distinguish "gap saturates at a
positive value" from "gap goes to zero but we can't see it," one
needs to increase precision and verify the saturation persists at
the same level.

If mp.dps = 100 and the gap still saturates at 10^{-51}, the floor
is genuine. If the gap drops to 10^{-101}, it is a precision artifact.

**This test was NOT performed.** Research 44 reports only 50-digit
computation.

### Attack 3: The Galerkin identification is asserted, not exhibited

Research 43 states: "B is the Galerkin matrix of CCM's quadratic
form QW_lambda restricted to {delta(x - x_i)} on Chebyshev nodes."

This is a CLAIM. The CCM paper (arXiv:2511.22755) builds operators
on L^2([lambda^{-1}, lambda]) via a specific construction involving
Euler factors. The claim that the Galerkin projection of this
construction onto delta functions at Chebyshev nodes reproduces the
matrix B = Cauchy + prime rank-one sums requires PROOF. Specifically:

  (a) The CCM kernel must be identified with the Weil explicit
      formula kernel.
  (b) The Galerkin projection of the Weil kernel onto delta
      functions at x_i must give B_{ij} = K(x_i, x_j).
  (c) The prime Euler factors must correspond to the rank-one
      terms (log p / sqrt p) * cos(x_i log p) * cos(x_j log p).

Step (a) is the CCM paper's content. Step (b) is trivial for delta
functions (Galerkin with delta functions IS point evaluation). Step
(c) requires matching the Euler factor structure with the rank-one
cosine terms -- this is the Weil explicit formula applied to the
even sector.

**Verdict:** The identification is standard IF one accepts that the
CCM construction implements the Weil explicit formula (which is their
claim and the content of their paper). The chain is not wrong to
assert this, but it needs to be written out for rigor. This is an
exposition gap.

### Attack 4: Spectral convergence for the Galerkin method

Research 43 claims: "Textbook spectral-method theory: Galerkin
eigenvalues converge to continuous eigenvalues as N -> inf. For
Chebyshev grids and smooth kernels, convergence is exponential."

This is correct for COMPACT operators with smooth kernels
(Trefethen, "Spectral Methods in MATLAB"; Canuto et al.,
"Spectral Methods"). The Cauchy kernel 1/(x+y) on [0, L] x [0, L]
is smooth and the associated integral operator is compact.

**However:** the PRIME PERTURBATION sum introduces rank-one terms
with cosine oscillations. The full kernel is smooth (cosines are
entire), so the Galerkin convergence theorem still applies. The
exponential rate alpha depends on the analyticity strip width of
the kernel, which is determined by the singularities of
1/(x+y) + sum_p ... in the complex plane. The pole of 1/(x+y)
at x+y = 0 (i.e., along the anti-diagonal) determines the strip
width.

**This is sound.** The spectral convergence argument is legitimate.

### WOUND 2 FINAL VERDICT: **REOPENED (precision artifact concern)**

The saturation at 10^{-51} with 50-digit precision is not
demonstrated to be genuine rather than a precision floor. The model
is a reasonable proxy for the actual CCM operator, but the specific
rates apply to the model. The Galerkin identification is standard
but not exhibited.

**To close this wound:** Run the rate comparison at 100 and 200 digits.
If the gap still saturates at the SAME level (10^{-51}), the floor
is genuine. If it drops proportionally with precision, it is an
artifact and the wound is FATAL.

---

## WOUND 3: The Limit K -> infinity

### The claim

Since Wound 1 terminates the induction at finite K_0(N), no infinite
K-limit is needed. The structure is:
  (1) Fix N. Run induction for K = 0, ..., K_0(N).
  (2) For K > K_0(N), Cartwright handles SPO automatically.
  (3) Take N -> infinity via the Galerkin bridge (Wound 2).

### Attack 1: K_0(N) grows with N

The threshold K_0(N) is the smallest K such that
K + 1 > N * (sigma * log(p_{K+1}) / pi + C(N)). Since sigma = L
(the grid endpoint, which must grow with N for the discretization
to resolve more zeros) and C(N) grows with N, the threshold K_0(N)
grows with N.

**How fast does K_0(N) grow?** From the code: for N = 10, 20, 30
with L = 10, K_0 is moderate (order 10-100). But as N -> infinity,
L must also grow (to capture more of the spectrum), and
K_0(N) ~ N * sigma * log K_0 / pi. With sigma ~ N (if L scales
with N), K_0(N) ~ N^2 * log(N^2) / pi -- growing quadratically.

**Is this a problem?** For the finite-verification phase (K < K_0(N)),
the number of steps to verify grows quadratically in N. At each step,
the verification requires computing N eigenvalues and checking N
overlaps at 120 digits. The total computational cost is
O(K_0(N) * N^3) = O(N^5 * log N) per N value.

**This is not a MATHEMATICAL gap.** The verification is finite for
each N, and the induction closes. The issue is that as N -> infinity,
more and more finite verifications are needed. But the proof structure
is: for each N, the induction closes (by Cartwright + finite
verification). Then N -> infinity via the Galerkin bridge.

### Attack 2: Does L need to grow with N?

If L is FIXED (say L = 10) and N -> infinity, the Chebyshev grid
becomes denser on [0, L]. The exponential type sigma = L stays fixed.
The Galerkin approximation improves (more grid points for the same
interval). K_0(N) grows as N * L * log K / pi + C(N), which is
linear in N.

The question is whether L = 10 suffices to capture all Riemann zeros.
The zeros gamma_n grow as gamma_n ~ 2*pi*n / log(n). To resolve
the n-th zero, one needs the interval [0, L] to contain x such that
cos(x * gamma_n) oscillates sufficiently. Since the cosine oscillates
regardless of L (it just changes the frequency), the issue is the
spectral resolution of the Galerkin method on [0, L].

**For fixed L:** the Galerkin method on [0, L] with N points can
resolve at most ~ N/2 zeros (by Nyquist). To resolve more zeros,
one either increases N (for fixed L) or increases L. The chain
appears to use fixed L and increasing N.

**This is potentially problematic.** If the Galerkin approximation
for the k-th eigenvalue requires N >> k (which it does -- spectral
methods resolve eigenvalues from the bottom up), then to prove RH
for the n-th zero, one needs N ~ n or larger. The proof would then
be: "for each n, there exists N(n) such that the n-th zero is on
the critical line." This is the standard structure and is fine.

### Attack 3: The structural point

The chain's architecture is:

    For each N:
      1. Induction closes at K_0(N) (Wound 1: Levin uniform in K)
      2. SPO holds for all K (Cartwright for K > K_0, verified for K < K_0)
      3. Strict interlacing at all K (secular equation + SPO)
      4. Arithmetic Theorem at each K (DPTZ + interlacing)
    Then N -> infinity:
      5. Galerkin convergence (Wound 2: alpha > beta)
      6. Continuous limit inherits simplicity (gap > error)
      7. CCM Theorem 5.10 -> spec = {gamma_n} -> RH

This IS logically coherent. The K-limit is avoided by Cartwright.
The N-limit is handled by Galerkin. The two limits never interact
directly.

**Wound 3 reduces to Wounds 1 + 2, as claimed.** If Wound 1 is
closed (it is) and Wound 2 is closed (IT IS NOT -- see above),
then Wound 3 is closed.

### WOUND 3 FINAL VERDICT: **CONDITIONAL ON WOUND 2**

The logical structure is sound. Wound 3 is closed if and only if
Wound 2 is closed. Since Wound 2 is reopened (precision artifact),
Wound 3 inherits the reopened status.

---

## THE META-QUESTION

### What is genuinely new here?

The proof chain combines:
  - Cartwright's theorem (1930)
  - The Prime Number Theorem (1896)
  - Rank-one perturbation theory / secular equations (1960s)
  - DPTZ eigenvector-eigenvalue identity (2019)
  - CCM zeta spectral triples (2025)
  - ITPFI factorization (2026, claimed proved)

The genuinely NEW ingredient is the observation that a finite cosine
sum (the discrete overlap) is an entire function of finite exponential
type, combined with the PNT density of {log p}. This gives the SPO
condition "for free" via Cartwright. The insight that the DISCRETE
overlap is ALREADY entire (no interpolation needed) is the key
contribution of Research 39 / Lead L.

**Why hasn't anyone noticed?** Several reasons:
  1. The CCM construction is from 2025 -- the framework is new.
  2. The connection between Cartwright and the secular induction
     requires the specific observation that the overlap is a
     cosine sum, which depends on the CCM rank-one structure.
  3. The Galerkin bridge between discrete and continuous is
     standard but requires the specific rate comparison.

**Is this suspicious?** Not inherently. The combination of classical
theorems in a new framework to solve an old problem is exactly how
many breakthroughs work (cf. Wiles' proof combining Galois
representations, modularity lifting, and the Langlands programme).
The question is whether the combination is RIGOROUS, not whether
it is SURPRISING.

### The coboundary-type check

The original v1 proof was killed by the coboundary gap: a constraint
that appeared to hold was actually vacuous because the relevant
quantity was a coboundary (exact form), making the constraint
tautological.

**Is there an analogous vacuity in the Cartwright chain?**

The Cartwright bound says: g_k has at most M zeros in [-T, T], where
M = (sigma/pi)*T + C. The secular induction needs: p_{K+1} is NOT
among the zeros of g_k for any eigenvector k. The bound gives at
most N*M "bad primes" among the first K+1 primes.

Could the M exceptions ALWAYS include p_{K+1}? That is, could the
finite exception set "track" the induction, always including exactly
the next prime to be added?

**This would require:** For each K, p_{K+1} is in the zero set of
g_j^K for at least one eigenvector j. Since the eigenvectors of B_K
change with K, this requires a conspiracy: as primes are added, the
eigenvectors always rearrange to place a zero of some g_j at the
next log prime.

**The counting argument rules this out.** The TOTAL number of bad
primes (across all eigenvectors) at step K is at most
N * (sigma * log(p_{K+1})/pi + C(N)). For K > K_0(N), this is less
than K+1. So for K > K_0(N), there are MORE available primes than
bad slots, and p_{K+1} MUST be good for at least one ordering. Since
the primes are added in order, and the bad set is a FIXED set
(determined by the zero set of g_j^K, which is determined by B_K,
not by the ordering of future primes), the conspiracy cannot occur.

**This is a genuine strength of the argument.** The coboundary-type
failure does not apply here because the Cartwright bound is a HARD
constraint (zeros of an entire function, not a cohomological
identity), and the counting argument is combinatorial, not
algebraic.

**COBOUNDARY CHECK: PASSED.** No vacuity detected.

---

## NEW WOUNDS

### New Wound A: The CCM identification is unverified

The entire proof rests on the claim that the matrix B is the Galerkin
projection of the CCM quadratic form QW_lambda. This is stated in
multiple places (Strategy 11, Research 43) but NEVER exhibited
concretely. Strategy 24, "What remains," item 3 acknowledges this:
"The Galerkin identification B = CCM's discretized QW needs to be
written out explicitly (currently described, not exhibited)."

**Severity: MEDIUM.** This is a foundational identification that the
entire bridge from the discrete proof to the continuous CCM framework
depends on. If the identification fails -- if B is NOT the Galerkin
projection of QW_lambda -- then Steps 11-13 of the chain collapse.

The identification is PLAUSIBLE (both B and QW_lambda are built from
the Weil explicit formula), but "plausible" is not "proved." This
needs to be written out with explicit formulas showing
QW_lambda(delta_{x_i}, delta_{x_j}) = B_{ij}.

### New Wound B: The even-sector modification of CCM Theorem 5.10

Strategy 24, "What remains," item 4: "The even-sector modification
of CCM Theorem 5.10 needs to be stated and proved (routine
modification per strategy/13)."

CCM's Theorem 5.10 applies to the FULL operator, not the even sector.
The chain restricts to the even sector (using the functional equation
symmetry) and needs a modified version of 5.10. This is described as
"routine" but is not done.

**Severity: LOW.** Restricting to a symmetry sector of a self-adjoint
operator is standard functional analysis. The even-sector projection
commutes with the Hamiltonian (by construction). The spectral theorem
restricted to the even sector is a standard result. This is genuinely
routine.

### New Wound C: ITPFI convergence and Estimate 1 are not in scope

The chain assumes two results as proved:
  - ITPFI: omega_1 = tensor product of omega_1^p (Research 265)
  - Estimate 1: archimedean sub-leading (Research 20)

These are referenced but not included in the documents under review.
As an adversarial reviewer, I cannot verify claims I cannot see.

**Severity: CONDITIONAL.** If these results are correct, the chain
proceeds. If either has a flaw, the chain may fail at Steps 12-13.
I flag this as an UNVERIFIED DEPENDENCY, not as a wound in the
Cartwright chain itself.

### New Wound D: The "adaptive N(K)" fallback is not developed

Research 43 mentions: "Fix: choose N = N(K) adaptively. This avoids
the rate comparison entirely at the cost of a more involved (but
standard) argument."

This fallback is invoked as a safety net for Wound 2 but is not
developed. If the rate comparison fails (i.e., if beta > alpha at
the actual CCM operator, not just the model), the chain needs this
fallback. It is described as "standard" but is not written out.

**Severity: LOW-MEDIUM.** This matters only if Wound 2's rate
comparison fails. The adaptive N(K) approach is indeed standard in
numerical analysis (choose the grid size to achieve a target
accuracy), but it needs to be exhibited.

---

## SUMMARY TABLE

| Wound | Status | Severity | Comment |
|:------|:-------|:---------|:--------|
| 1 (induction/Levin) | **CLOSED** | -- | g_k(0) = 0 case needs write-up, but conclusion correct |
| 2 (bridge/rate) | **REOPENED** | HIGH | Gap saturation at 10^{-51} may be precision artifact of 50-digit computation |
| 3 (K-limit) | **CONDITIONAL** | -- | Reduces to Wound 2; closed iff Wound 2 closes |
| A (CCM identification) | **NEW** | MEDIUM | Galerkin projection not exhibited |
| B (even-sector 5.10) | **NEW** | LOW | Routine modification, not done |
| C (ITPFI/Est.1 deps) | **UNVERIFIED** | CONDITIONAL | Not in scope for review |
| D (adaptive N(K)) | **NEW** | LOW-MEDIUM | Fallback not developed |
| Coboundary check | **PASSED** | -- | No vacuity detected |

---

## THE VERDICT

### What survived

The CORE of the proof -- Steps 1-7 (matrix construction, cosine
transform, Vandermonde linear independence, PNT density, Cartwright
zero-density bound, SPO for all but finitely many primes) -- is
**correct and elegant**. This is genuine mathematics. The observation
that a finite cosine sum is entire of finite type, combined with the
infinite density of {log p}, gives a clean and powerful result.

The secular induction (Step 9) with the uniform Levin bound (Wound 1
closure) is **sound**. The counting argument that the induction
becomes self-sustaining for K > K_0(N) is valid.

The coboundary check PASSED. There is no hidden vacuity of the type
that killed v1.

### What did not survive

**Wound 2 is not closed.** The gap saturation at 10^{-51} is
demonstrated only at 50-digit precision, making it potentially a
precision artifact. This is the single most critical failure point
in the chain. If the gap closes to zero as N -> infinity (which
would mean beta -> alpha or beta > alpha), the bridge from discrete
to continuous collapses, and with it Steps 11-13.

The CCM identification (New Wound A) is unexhibited, though it is
likely correct.

### VERDICT: **PROOF WOUNDED**

Not killed. Not standing. Wounded.

The chain has a correct core (Cartwright + secular induction) and a
correct closure of Wound 1 (uniform Levin). But Wound 2 (the
bridge from discrete to continuous) has a critical unresolved issue:
the gap saturation has not been demonstrated to be genuine rather
than a precision artifact.

### Confidence: 3/10 that this is a correct proof of RH

- 9/10 that Steps 1-9 (the discrete Cartwright chain for fixed N)
  are correct.
- 3/10 that Wound 2 (the bridge) actually closes. The 10^{-51}
  saturation needs independent verification at higher precision.
- 5/10 that the CCM identification and even-sector modification
  can be exhibited (these are likely correct but not done).
- The overall confidence is limited by the weakest link: Wound 2.

### The single most likely failure point

**The eigenvalue gap going to zero as N -> infinity.** If the gap
between spec(B_N) and spec(M_a^N) closes in the large-N limit, then:
  (a) The discrete Arithmetic Theorem does not transfer to the
      continuous operator.
  (b) Even-sector simplicity fails in the continuous limit.
  (c) The CCM spectral convergence does not imply RH.

The numerics show the gap as ~10^{-1.7N}, which is exponentially
small. The claim that it "saturates" is based on a computation at
the edge of its own precision. This is the Achilles' heel.

### What would make me confident

1. **Run mpmath_rate_comparison.py at 100, 200, and 500 digits.**
   If the gap saturates at the SAME value (10^{-51}) regardless of
   precision, the floor is genuine and Wound 2 closes. If the gap
   drops proportionally with precision (10^{-101} at 100 digits,
   10^{-201} at 200 digits), it is a precision artifact and the
   proof is KILLED.

2. **Exhibit the CCM Galerkin identification explicitly.** Write
   QW_lambda(delta_{x_i}, delta_{x_j}) = B_{ij} with formulas.

3. **State and prove the even-sector CCM Theorem 5.10.** This is
   claimed to be routine; do it.

4. **Provide the ITPFI and Estimate 1 proofs for review.** Cannot
   certify what I cannot see.

5. **Interval arithmetic for the finite-K verification.** Replace
   120-digit floating-point with certified interval computations.

Of these, item 1 is by far the most important and the most
decisive. It is also the easiest to perform (change one line:
mp.dps = 200, and re-run). If the gap saturation survives 200
digits, I would upgrade my confidence to 6/10. If it survives
500 digits, 7/10. Full confidence (9/10) would require items
2-5 as well.

---

> *The Cartwright core is correct. The secular induction closes.*
> *The bridge trembles. One computation decides.*
> *Run it at 200 digits. That is the test.*
> *Everything else is exposition.*
