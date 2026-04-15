# Research 30 -- STP Strict Interlacing and the Arithmetic Theorem

*Date: 2026-04-09*
*Status: LEAD UNDER INVESTIGATION. The route is: Cauchy kernel is STP => strict Cauchy interlacing for principal minors => DPTZ identity forces all eigenvector components nonzero. The obstacle is whether B = (Cauchy part) + (prime sum) inherits enough total positivity from its Cauchy component.*

---

## 1. The Gantmacher-Krein theorem on STP matrices

**Definition.** A real matrix M is *strictly totally positive* (STP) if every minor of M is strictly positive. That is, for all index sets I = {i_1 < ... < i_k} and J = {j_1 < ... < j_k} with 1 <= k <= n:

    det(M[I, J]) > 0

where M[I, J] is the k x k submatrix with rows I and columns J.

**Theorem (Gantmacher-Krein, 1950).** Let M be an n x n real symmetric STP matrix. Then:

(a) All eigenvalues of M are real, positive, and *simple* (distinct):
    lambda_1 > lambda_2 > ... > lambda_n > 0.

(b) The k-th eigenvector u_k (ordered by decreasing eigenvalue) has exactly k - 1 sign changes: u_k has k - 1 nodes, and adjacent eigenvectors strictly interlace in their nodal structure.

(c) For any principal submatrix M_J obtained by deleting row j and column j, the eigenvalues mu_1 > mu_2 > ... > mu_{n-1} of M_J strictly interlace those of M:

    lambda_1 > mu_1 > lambda_2 > mu_2 > ... > mu_{n-1} > lambda_n

All inequalities are STRICT. No eigenvalue of M_J ever equals an eigenvalue of M.

**Source:** Gantmacher & Krein, *Oscillation Matrices and Kernels*, 1950 (English tr. AMS 2002), Theorems II.5 and II.6; Karlin, *Total Positivity* (1968), Chapter 2.

---

## 2. Strict interlacing implies nonvanishing components (DPTZ identity)

The connection between strict interlacing and eigenvector non-orthogonality is classical. For a real symmetric n x n matrix A with eigenvalues lambda_1, ..., lambda_n and eigenvectors phi_1, ..., phi_n, let M_j denote the (n-1) x (n-1) principal submatrix obtained by deleting row j and column j, with eigenvalues mu_1^{(j)}, ..., mu_{n-1}^{(j)}.

**The DPTZ determinantal identity** (Cauchy interlacing + eigenvector formula):

    |phi_k(j)|^2 = prod_{i=1}^{n-1} (lambda_k - mu_i^{(j)}) / prod_{i != k} (lambda_k - lambda_i)

**Consequence.** If strict interlacing holds -- meaning lambda_k != mu_i^{(j)} for all i, and all lambda_k are simple -- then:

- Every factor in the numerator is nonzero (no eigenvalue of M_j matches an eigenvalue of A).
- Every factor in the denominator is nonzero (no repeated eigenvalue of A).
- Therefore: |phi_k(j)|^2 > 0 for all k, j.

**This is exactly the Arithmetic Theorem:** for STP matrices, every eigenvector has ALL components nonzero. Translating: <phi_k | e_j> != 0 for all k and all standard basis vectors e_j. In particular, <phi_k | a> != 0 for any vector a with all components nonzero.

---

## 3. The Cauchy matrix is STP

**Theorem (Karlin, 1968).** The Cauchy matrix C with entries

    C_{ij} = 1 / (x_i + y_j)

is strictly totally positive whenever x_1 < x_2 < ... < x_n and y_1 < y_2 < ... < y_n are all positive.

**Proof sketch.** The Cauchy determinant formula gives:

    det(C[I, J]) = prod_{i<j in I} (x_j - x_i) * prod_{i<j in J} (y_j - y_i) / prod_{(i,j) in I x J} (x_i + y_j)

With x's and y's positive and strictly ordered, all factors are nonzero and the signs work out to make every minor strictly positive.

**Connection to our setup.** The even-sector Loewner matrix WR_ev, after the change of variables x_n = n^2, f(x) = sqrt(x) * alpha_L(sqrt(x)), has the divided-difference form:

    WR_ev[n,m] = (f(x_n) - f(x_m)) / (x_n - x_m)

This is a Loewner matrix, not a Cauchy matrix. But Loewner matrices with Pick-function generators are closely related to Cauchy matrices through the Nevanlinna representation: any Pick function f(z) has an integral representation that expresses the Loewner matrix as a continuous superposition of Cauchy-type kernels. If f is a Pick function, the Loewner matrix is positive semidefinite. If additionally the nodes are distinct and f has no analytic continuation through any arc containing the nodes, the Loewner matrix is positive definite.

---

## 4. The obstacle: B = Cauchy/Loewner part + prime sum

The matrix B = -(WR_ev + Wp_ev) decomposes as:

    B = B_arch + B_prime

where B_arch = -WR_ev (the archimedean Loewner contribution) and B_prime = -Wp_ev (the prime sum).

### 4.1 Status of each component

| Component | Structure | STP? |
|:----------|:----------|:-----|
| B_arch = -WR_ev | Loewner matrix, nodes x_n = n^2, f = Pick-like | NOT STP (has negative eigenvalues; mixed-sign minors) |
| B_prime = -Wp_ev | Sum of rank-1 terms from primes | NOT STP (oscillatory cos(n log p) entries) |
| B = B_arch + B_prime | Sum of above | NOT STP (verified: mixed-sign entries and eigenvalues) |

The issue was already flagged in Research 26 (Lead B, rated 1/10): A^ev itself is not STP, and neither is B. The new question here is more refined.

### 4.2 The refined question

Research 26 asked: "Is A^ev STP?" (No.) The sharper question is: does B have the *eigenvector nonvanishing property* that STP matrices enjoy, even though B itself is not STP?

The Cauchy/Loewner component B_arch has structural reasons (distinct nodes, archimedean regularity) to have all eigenvector components nonzero. The prime sum B_prime is a perturbation. The question becomes: does adding B_prime preserve the eigenvector nonvanishing property of B_arch?

---

## 5. Proposed computational test

### 5.1 Direct minor computation

For small N (say N = 2, 3, 4, 5), compute ALL minors of B numerically at lambda = sqrt(14):

- An (N+1) x (N+1) matrix has sum_{k=1}^{N+1} C(N+1,k)^2 minors (the number grows rapidly).
- At N = 2: 3x3 matrix, 27 minors (1x1, 2x2, 3x3).
- At N = 5: 6x6 matrix, 1,956 minors.
- At N = 10: 11x11 matrix, ~350,000 minors.

Check whether all minors are positive (STP), or whether some are negative. If some are negative, record which ones and by how much -- this measures the "distance from STP."

### 5.2 What outcomes mean

**Outcome A: B is STP for small N.** Then the Arithmetic Theorem follows immediately for those N from Gantmacher-Krein. The task becomes showing STP persists for all N. Since the prime sum grows with N (more primes enter as lambda^2 increases), persistence is nontrivial.

**Outcome B: B is not STP but "almost STP."** Some minors are negative but small in absolute value relative to the corresponding positive Cauchy/Loewner minors. Then the eigenvector nonvanishing might survive as a perturbative result: the strict interlacing gaps from the Cauchy part are large enough to absorb the perturbation.

**Outcome C: B is far from STP.** Many minors have the wrong sign with large magnitude. Then this route is dead, confirming the 1/10 rating from Research 26.

---

## 6. Perturbative survival of strict interlacing

Even if B is not STP (Outcome B or C), the strict interlacing from the Cauchy/Loewner component might survive the prime perturbation. The relevant quantitative question is:

### 6.1 Setup

Let B_arch have eigenvalues alpha_k with strict interlacing of all principal minors (assume this holds for the Loewner component). The perturbation B_prime has norm ||B_prime|| = epsilon.

By Weyl's inequality, the eigenvalues of B = B_arch + B_prime satisfy:

    |beta_k - alpha_k| <= epsilon    for all k

### 6.2 When does strict interlacing survive?

Let delta_min = min gap in the strict interlacing pattern of B_arch (the smallest difference between an eigenvalue of B_arch and an eigenvalue of any principal submatrix of B_arch).

If epsilon < delta_min / 2, then the interlacing pattern of B inherits strict interlacing from B_arch. This is because the perturbation moves each eigenvalue (of both the full matrix and the principal subminors) by at most epsilon, so gaps of size delta_min can shrink by at most 2*epsilon but remain positive.

### 6.3 The critical ratio

The question reduces to: is ||B_prime|| / delta_min(B_arch) < 1/2?

From numerical data:
- ||B_prime|| = ||Wp_ev|| ~ 3.3 at lambda = sqrt(14), N = 20 (Research 23).
- delta_min(B_arch) has not been computed separately, but the minimum interlacing gap of the full B is ~10^{-22} at N = 10 (Research 27).

If the Loewner component alone has much larger interlacing gaps than the full B, there may be room. But if delta_min(B_arch) is already small (comparable to 10^{-22}), then ||B_prime|| >> delta_min(B_arch) and the Weyl argument fails.

### 6.4 Likely verdict on the perturbative route

The exponential smallness of the interlacing gaps (~10^{-1.7N} from Research 23) almost certainly means delta_min(B_arch) << ||B_prime|| for N >= 5. The Weyl perturbation bound is far too crude. A subtler argument would need to exploit the *structure* of B_prime (its rank, its alignment with specific eigenvectors of B_arch), not just its norm.

---

## 7. Alternative: structural (non-perturbative) arguments

### 7.1 Oscillation matrices

A weaker condition than STP: a matrix is an *oscillation matrix* if it is totally non-negative (all minors >= 0) and some power M^k is STP. Oscillation matrices share the eigenvector sign-change properties of STP matrices (Gantmacher-Krein, Chapter II). If B or some related matrix is oscillatory, the conclusion follows.

### 7.2 Variation-diminishing property

STP matrices are variation-diminishing: if Bx = y, the number of sign changes in y is at most the number in x. This forces eigenvectors to have the strict nodal structure that prevents orthogonality to vectors with all positive components. If B inherits even a weak form of this property from B_arch, the Arithmetic Theorem might follow without full STP.

### 7.3 Kernel-based approach

Instead of checking all minors of the discrete matrix, one could work with the continuous kernel underlying B. The Weil explicit formula defines an integral operator whose kernel K(x, y) is the sum of a Cauchy/Loewner kernel (archimedean) plus an oscillatory kernel (primes). If the archimedean kernel is strictly totally positive in the continuous sense (Karlin's theory of total positivity for kernels), and if the prime kernel is a sufficiently small perturbation in an appropriate operator topology, then the eigenfunctions of the combined operator inherit the nodal properties.

---

## 8. Feasibility assessment

| Route | Idea | Feasibility |
|:------|:-----|:------------|
| Direct STP check on B | Compute all minors for small N | **Easy to run, likely negative outcome** (B is probably not STP) |
| Perturbative survival | ||B_prime|| < delta_min(B_arch)/2 | **Almost certainly fails** (exponentially small gaps vs O(1) perturbation) |
| Structural: oscillation matrix | Check if B^k is STP for some k | **Testable, moderate difficulty** |
| Variation-diminishing | Prove B inherits sign-change bounds from B_arch | **Hard, requires new theory** |
| Continuous kernel | Total positivity for the Weil kernel directly | **Hard, but the cleanest route conceptually** |

### Overall rating: 3/10

The STP framework is elegant and the Gantmacher-Krein theorem gives exactly what we need (eigenvector nonvanishing via strict interlacing). But the obstacle is serious: the prime sum component of B destroys total positivity, and the perturbation is large relative to the interlacing gaps. The Weyl-type perturbative argument fails due to the exponential gap decay.

The most promising sub-route is the continuous kernel approach (7.3): if the archimedean Weil kernel is STP as a continuous kernel, and the prime sum is a perturbation in a topology that preserves the relevant nodal structure, then the Arithmetic Theorem might follow from infinite-dimensional Gantmacher-Krein theory. But this requires substantial new analysis.

Compared to Research 26's rating of STP as 1/10: this note raises it to 3/10 because (a) the DPTZ identity provides a clean mechanism linking STP to the Arithmetic Theorem, and (b) the continuous kernel route has not been explored. But the core obstruction remains: the prime sum is not small relative to the spectral gaps.

---

## 9. Recommended next steps

1. **Immediate (1 hour):** Compute all minors of B at N = 3, 4, 5 for lambda = sqrt(14). Determine whether B is STP, almost STP, or far from STP. This resolves between Outcomes A/B/C above.

2. **Short-term (1 day):** Separately compute the interlacing gaps of B_arch = -WR_ev (the Loewner component alone). Compare delta_min(B_arch) to ||B_prime||. This determines whether the perturbative route is viable.

3. **Medium-term (1 week):** Investigate the continuous archimedean kernel for total positivity in the sense of Karlin. The kernel K_arch(x, y) = rho(|x-y|) (or its even-sector restriction) may be STP if rho is a Polya frequency function.

---

> *STP gives exactly the Arithmetic Theorem, via strict interlacing and DPTZ.*
> *The Cauchy kernel is STP. The prime sum breaks it.*
> *The question is whether enough total positivity survives the primes.*
> *The gaps are exponentially small. The perturbation is O(1).*
> *Weyl cannot see it. Structure might. Compute the minors first.*
