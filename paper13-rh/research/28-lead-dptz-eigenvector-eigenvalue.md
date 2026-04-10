# Research 28 -- Lead: DPTZ Eigenvector-Eigenvalue Identity

*Date: 2026-04-09*
*Status: NEW LEAD. Reformulates the Arithmetic Theorem as an eigenvalue non-coincidence condition via Denton-Parke-Tao-Zhang. Strict interlacing of minors would close the theorem if B has sufficient positivity structure.*

---

## 1. The DPTZ identity

**Theorem (Denton-Parke-Tao-Zhang, 2019).** Let A be an n x n Hermitian matrix with eigenvalues lambda_1(A), ..., lambda_n(A) and unit eigenvectors v_1, ..., v_n. Let M_j be the (n-1) x (n-1) principal minor obtained by deleting row j and column j. Then for each eigenvector component:

    |v_{i,j}|^2 * prod_{k != i} [lambda_i(A) - lambda_k(A)] = prod_{k=1}^{n-1} [lambda_i(A) - lambda_k(M_j)]

This relates the squared magnitude of the j-th component of the i-th eigenvector to the eigenvalues of A and the eigenvalues of the minor M_j. The identity is exact, not asymptotic.

**Source:** Denton, Parke, Tao, Zhang, "Eigenvectors from Eigenvalues: A Survey of a Basic Identity in Linear Algebra," Bull. AMS 59 (2022), 31--58. Originally arXiv:1908.03795.

---

## 2. Application to the Arithmetic Theorem

### 2.1 Setup

The Arithmetic Theorem requires: for all k, the overlap <phi_k | a> != 0, where:

- B = -(WR_ev + Wp_ev) is the (N+1) x (N+1) even-sector matrix (Loewner + prime sum)
- phi_k are the eigenvectors of B with eigenvalues beta_k
- a is the archimedean vector, a_n = 1/(L^2 + 16*pi^2*n^2), normalized to unit length: a_hat = a / ||a||

### 2.2 Expressing the overlap via DPTZ

The overlap <phi_k | a_hat> is not directly a component v_{k,j} in the standard basis, because a_hat is not a standard basis vector e_j. However, we can rotate to a basis where a_hat IS a basis vector.

Let U be any unitary with U*e_1 = a_hat (i.e., the first column of U is a_hat). Define:

    B_rot = U^T * B * U

Then B_rot has the same eigenvalues beta_k as B, and its eigenvectors w_k = U^T * phi_k satisfy:

    w_{k,1} = (U^T * phi_k)_1 = <e_1, U^T * phi_k> = <U*e_1, phi_k> = <a_hat, phi_k>

So the overlap equals the first component of the eigenvector of B_rot. The DPTZ identity gives:

    |<phi_k | a_hat>|^2 * prod_{j != k} [beta_k - beta_j] = prod_{j=1}^{N} [beta_k - mu_j(M_a)]

where M_a is the N x N principal minor of B_rot obtained by deleting row 1 and column 1.

### 2.3 The reformulation

**The overlap <phi_k | a_hat> = 0 if and only if beta_k is an eigenvalue of M_a.**

This is immediate from the DPTZ identity (assuming B has simple eigenvalues, so the LHS product is nonzero). The condition becomes:

    spec(B) cap spec(M_a) = empty set   <==>   <phi_k | a> != 0 for all k

**The Arithmetic Theorem is equivalent to: no eigenvalue of B coincides with any eigenvalue of M_a.**

### 2.4 What is M_a geometrically?

M_a = P_a^perp * B * P_a^perp restricted to a^perp, where P_a^perp = I - |a_hat><a_hat| is the projector onto the orthogonal complement of a_hat. Equivalently, M_a is the compression of B to the N-dimensional subspace orthogonal to a.

This is the "B with the a-direction projected out."

---

## 3. Eigenvalue interlacing and the non-coincidence condition

### 3.1 Cauchy interlacing for principal minors

For any Hermitian A with eigenvalues lambda_1 <= ... <= lambda_n and any principal minor M (delete row j, col j) with eigenvalues mu_1 <= ... <= mu_{n-1}:

    lambda_1 <= mu_1 <= lambda_2 <= mu_2 <= ... <= mu_{n-1} <= lambda_n

This is the Cauchy interlacing theorem. The inequalities are non-strict in general.

### 3.2 When is interlacing strict?

Strict interlacing (all inequalities strict) holds iff:

    lambda_k != mu_j for all k, j

By DPTZ, this is equivalent to: |v_{k,j}|^2 != 0 for all k. In our context, strict interlacing between spec(B) and spec(M_a) is EXACTLY the Arithmetic Theorem.

So we have a perfect circle: strict interlacing <=> all overlaps nonzero <=> Arithmetic Theorem. The DPTZ identity does not break the circle, but it REFORMULATES the problem in eigenvalue language, which opens different tools.

### 3.3 Known conditions for strict interlacing

**(a) Irreducibility.** If A is a tridiagonal matrix with all off-diagonal entries nonzero (irreducible Jacobi matrix), then interlacing is always strict. B is NOT tridiagonal -- it is a dense matrix.

**(b) Strict total positivity.** If A is strictly totally positive (STP), then ALL principal minors interlace strictly with A. This was explored in Research 26, Lead B: B is NOT STP (mixed signs from prime contributions). Dead end confirmed.

**(c) Oscillatory matrices.** A matrix is oscillatory if it is totally nonnegative (TN) and some power A^k is STP. Oscillatory matrices have strict interlacing. B is not TN either -- the prime sum creates negative entries.

**(d) Perron complement structure.** For M-matrices (positive off-diagonal, positive inverse), principal minors inherit M-matrix structure and interlacing is strict. B is not an M-matrix.

### 3.4 The structural gap

None of the classical sufficient conditions for strict interlacing apply to B. The matrix B = -(WR_ev + Wp_ev) has:
- Dense structure (not tridiagonal)
- Mixed-sign entries (from cos(n*log p) in the prime sum)
- Eigenvalues spanning from ~ -6 to ~ +3 (not positive definite)

The Loewner component WR_ev alone DOES have nice structure (Pick matrix, related to Cauchy matrices), but adding Wp_ev destroys any total positivity or sign-regularity.

---

## 4. A different angle: analytic dependence of spec(M_a)

### 4.1 Both B and a depend on lambda

As lambda varies, both B(lambda) and a(lambda) change analytically. The eigenvalues beta_k(lambda) of B and mu_j(lambda) of M_a are all analytic functions of lambda (by Kato-Rellich). A coincidence beta_k(lambda_0) = mu_j(lambda_0) is the intersection of two analytic curves.

### 4.2 Codimension argument

In the (k, j, lambda) parameter space, each equation beta_k(lambda) = mu_j(lambda) is one equation in one unknown (lambda). Generically this has isolated solutions (if any). There are N*(N+1) such equations (N+1 choices of k, N choices of j), but each pair of curves generically crosses transversally.

The VNW-type argument from Research 26: the coincidence set {lambda : beta_k(lambda) = mu_j(lambda) for some k, j} is generically discrete (codimension 1 in lambda-space). This does NOT exclude coincidences -- it says they are isolated if they occur.

### 4.3 What would exclude them

If we could show that d/d(lambda)[beta_k - mu_j] has a DEFINITE SIGN whenever beta_k = mu_j, then the curves could never touch (they approach from one side and would have to bounce, contradicting analyticity). This is a monotonicity/repulsion argument.

For the Weil matrix, the lambda-derivatives of beta_k and mu_j involve the prime sum structure. Monotonicity would require showing that "adding more primes" (as lambda increases) pushes the eigenvalues of B and M_a apart. This is plausible but unproved.

---

## 5. Proposed computational test

### 5.1 Direct eigenvalue comparison

For each tested (lambda, N):

1. Build B = -(WR_ev + Wp_ev), dimension (N+1) x (N+1)
2. Build a_hat = a / ||a||
3. Rotate: B_rot = U^T * B * U where U has a_hat as first column (Householder)
4. Extract M_a = B_rot[1:, 1:], dimension N x N
5. Compute spec(B) = {beta_0, ..., beta_N} and spec(M_a) = {mu_1, ..., mu_N}
6. Compute all pairwise distances |beta_k - mu_j|
7. Report min distance and verify DPTZ identity against known overlaps

### 5.2 Verification via DPTZ

For each k, check:

    |<phi_k | a_hat>|^2 = prod_{j=1}^{N} [beta_k - mu_j(M_a)] / prod_{j != k} [beta_k - beta_j]

This is a nontrivial consistency check. Both sides should agree to machine precision.

### 5.3 Scaling of minimum distance

Track min_{k,j} |beta_k - mu_j| as a function of N and lambda. Compare to the known overlap scaling |<phi_k|a>|^2 ~ 10^{-1.7*N} (from Research 23). By DPTZ, these are related:

    min |<phi_k|a>|^2 ~ min_j |beta_k - mu_j| / (eigenvalue spread)

If the minimum pairwise distance also decays exponentially in N, this quantifies how close the system gets to a coincidence without reaching it.

---

## 6. What this lead buys

### 6.1 Advantages over the direct overlap approach

- **Spectral language:** The condition spec(B) cap spec(M_a) = empty is a statement about eigenvalue repulsion between a matrix and its compression. This connects to random matrix theory (eigenvalue rigidity, level repulsion) and perturbation theory.
- **Minor structure:** M_a is a rank-1 perturbation of B restricted to a subspace. The relationship between spec(B) and spec(M_a) is constrained by more than just Cauchy interlacing -- the specific structure of the perturbation (projection onto a_hat) may give additional constraints.
- **Induction on N:** If the theorem holds at dimension N, the passage to N+1 adds one new eigenvalue of B and one new eigenvalue of M_a. Tracking how the new eigenvalues interleave with existing ones could support an inductive argument.

### 6.2 Limitations

- The reformulation is EQUIVALENT to the original problem, not weaker. No free lunch.
- Classical sufficient conditions for strict interlacing (STP, oscillatory, Jacobi) all fail for B.
- The eigenvalue non-coincidence condition is itself an arithmetic statement -- just phrased differently.

---

## 7. Feasibility rating

| Aspect | Assessment |
|:-------|:-----------|
| Reformulation via DPTZ | CLEAN. Exact, no approximation. |
| Computational test | EASY. Standard eigenvalue computation, can be done in mpmath. |
| Connection to strict interlacing | EXACT equivalence, verified by DPTZ. |
| Classical sufficient conditions (STP, etc.) | ALL FAIL for B. |
| New angle: eigenvalue repulsion / rigidity | PROMISING but speculative. Would need RMT-type arguments adapted to structured (non-random) matrices. |
| Induction on N | POSSIBLE angle. The N -> N+1 step adds one eigenvalue to each spectrum. |
| Path to proof | NOT CLEAR. Reformulation is clean but does not obviously simplify the core difficulty. |
| Overall rating | **4/10** -- valuable reformulation, easy to test, but does not by itself break the impasse. Worth pursuing computationally to build intuition. |

---

## 8. Next steps

1. **Implement the computational test** (Section 5). Verify DPTZ identity numerically. Measure min |beta_k - mu_j| across the standard (lambda, N) grid.

2. **Track the interlacing pattern.** For each (lambda, N), record the full interlacing sequence beta_1, mu_1, beta_2, mu_2, ... and check whether the pattern is always strict. Look for near-coincidences and their arithmetic content.

3. **Explore the N -> N+1 transition.** When the matrix dimension increases by 1, how do the new eigenvalue and new minor eigenvalue relate? Is there a recursive structure exploitable for induction?

4. **Connect to eigenvalue rigidity.** In random matrix theory, eigenvalue rigidity (Erdos-Yau-Yin 2012) says eigenvalues of Wigner matrices are close to their classical locations with high probability. For structured matrices like B, analogous rigidity results might constrain how close spec(B) and spec(M_a) can get.

---

> *DPTZ turns the overlap question into a spectral question:*
> *do B and its a-compression ever share an eigenvalue?*
> *The reformulation is exact and opens eigenvalue-repulsion tools.*
> *But the arithmetic core remains: primes vs. archimedean, now*
> *refracted through the lens of minor eigenvalues.*
> *Test it. Measure the gaps. See if the interlacing speaks.*
