# Research 33 -- Lead D: Secular Equation + Induction on Primes

*Date: 2026-04-09*
*Status: VIABLE STRUCTURAL APPROACH. Reduces the full Arithmetic Theorem to single-prime overlap conditions. Baker's theorem is the natural tool for the overlap step, but a nontrivial gap remains.*

---

## 1. The secular equation for rank-one perturbations

**Theorem (rank-one secular equation).** Let A be a real symmetric n x n matrix with eigenvalues lambda_1 < lambda_2 < ... < lambda_n and orthonormal eigenvectors e_1, ..., e_n. Let v be a vector and alpha a real scalar. The eigenvalues mu of the rank-one update

    A' = A + alpha * v v^T

are the roots of the secular equation:

    f(mu) = 1 + alpha * sum_{k=1}^{n} |<e_k | v>|^2 / (lambda_k - mu) = 0

Equivalently, mu is an eigenvalue of A' iff det(A' - mu I) = 0, which by the matrix determinant lemma reduces to:

    1 + alpha * v^T (A - mu I)^{-1} v = 0

Expanding in the eigenbasis of A gives the stated form. Each pole at mu = lambda_k contributes a term that diverges, producing strict sign alternation of f between consecutive eigenvalues.

**Source:** Golub (1973), "Some modified matrix eigenvalue problems"; Bunch, Nielsen, & Sorensen (1978).

---

## 2. Strict interlacing criterion

**Theorem.** Let A have simple eigenvalues lambda_1 < ... < lambda_n, let v in R^n, and let A' = A + alpha * v v^T with alpha > 0. Then:

(a) **Cauchy interlacing always holds:** lambda_k <= mu_k <= lambda_{k+1} (with the convention mu_n >= lambda_n).

(b) **Strict interlacing (all inequalities strict) holds if and only if**

    <e_k | v> != 0    for every k = 1, ..., n.

*Proof sketch.* The secular function f(mu) has poles at each lambda_k with residue -alpha |<e_k|v>|^2. Between consecutive poles lambda_k and lambda_{k+1}, f goes from +infinity to -infinity (or vice versa) **only if** both residues are nonzero. If <e_k|v> = 0, the pole at lambda_k vanishes: f has no singularity there, so f passes smoothly through lambda_k, and mu_k = lambda_k is unchanged. Strict interlacing fails.

**Converse.** If every overlap is nonzero, every pole is active, f alternates sign between every consecutive pair of eigenvalues, and by the intermediate value theorem there is exactly one root mu_k in each interval (lambda_k, lambda_{k+1}), giving strict interlacing.

---

## 3. Inductive argument: adding primes one by one

### 3.1 Setup

The even-sector Weil quadratic form, truncated to primes p_1 < p_2 < ... < p_K, has matrix:

    B_K = B_0 + sum_{k=1}^{K} alpha_k * v_{p_k} v_{p_k}^T

where B_0 is the archimedean (Cauchy/Loewner) component, alpha_k = log(p_k) / sqrt(p_k), and v_{p_k}[i] = cos(x_i * log p_k).

Each prime contributes a rank-one symmetric perturbation to the previous matrix.

### 3.2 The induction

**Base case (K = 0).** B_0 is the Cauchy matrix 1/(x_i + x_j). By Karlin (1968), this is STP on ordered positive nodes. By Gantmacher-Krein, all eigenvalues are simple and all eigenvector components are nonzero. The Arithmetic Theorem holds for B_0.

More precisely: the compression M_a^0 of B_0 onto {a}^perp has eigenvalues that strictly interlace those of B_0 (STP property). Hence spec(B_0) and spec(M_a^0) are disjoint.

**Inductive step (K -> K+1).** Suppose B_K has simple eigenvalues with strict interlacing against M_a^K (the Arithmetic Theorem holds at step K). Adding prime p_{K+1}:

    B_{K+1} = B_K + alpha_{K+1} * v_{p_{K+1}} v_{p_{K+1}}^T

By the secular equation theorem (Section 2), eigenvalues of B_{K+1} strictly interlace those of B_K **if and only if** v_{p_{K+1}} has nonzero overlap with every eigenvector of B_K:

    <phi_j^K | v_{p_{K+1}}> != 0    for all j = 1, ..., n

If this holds, B_{K+1} has simple eigenvalues. One must then also verify that the compression M_a^{K+1} inherits strict interlacing. The compression changes by a projected rank-one update, so a similar secular argument applies.

### 3.3 What the induction achieves

**The full Arithmetic Theorem (for all K) reduces to the single-prime overlap condition at each step:**

    (SPO_K):  <phi_j^K | v_{p_{K+1}}> != 0   for all j, for each K = 0, 1, 2, ...

This is a vast simplification: instead of proving a global spectral property of the infinite-prime matrix, we need only verify that each newly added prime vector is "generic" with respect to the current eigenbasis.

---

## 4. Reducing to single-prime overlaps

The condition (SPO_K) asks: does the vector v_p, with entries cos(x_i * log p), have nonzero projection onto every eigenvector of the matrix B_K?

### 4.1 Structure of the overlap

    <phi_j^K | v_p> = sum_{i=1}^{n} phi_j^K(x_i) * cos(x_i * log p)

This is a discrete cosine transform of the eigenvector phi_j^K evaluated at frequency log p. It vanishes iff phi_j^K is orthogonal to the specific oscillatory pattern cos(x * log p).

### 4.2 Why genericity is expected

The eigenvectors phi_j^K depend on ALL primes up to p_K through the matrix B_K. The new prime p_{K+1} is independent: it introduces a new frequency log p_{K+1} that is (by the prime number theorem) generically incommensurate with the frequencies log p_1, ..., log p_K already present.

For the overlap to vanish, the eigenvector would need to be exactly orthogonal to a specific trigonometric vector -- a codimension-1 condition. Generically, this does not happen.

### 4.3 The gap: generic is not proven

"Generically nonzero" is not a proof. We need either:
- An algebraic/transcendence argument that the overlap is provably nonzero, or
- A quantitative lower bound on |<phi_j^K | v_p>|.

---

## 5. Baker's theorem and the single-prime overlap

### 5.1 Statement of Baker's theorem

**Theorem (Baker, 1966).** If alpha_1, ..., alpha_m are algebraic numbers (not 0 or 1) and beta_1, ..., beta_m are algebraic numbers not all zero, then

    beta_1 * log(alpha_1) + ... + beta_m * log(alpha_m) != 0

More precisely, |beta_1 log alpha_1 + ... + beta_m log alpha_m| > C^{-1} where C depends explicitly on the heights and degrees of the alpha_i and beta_j.

### 5.2 Could Baker's theorem apply?

The overlap <phi_j^K | v_p> = sum_i phi_j^K(x_i) cos(x_i log p) involves:

- **log p**: logarithm of a prime, transcendental by Lindemann-Weierstrass.
- **x_i**: the grid nodes (e.g., Chebyshev nodes, algebraic numbers).
- **phi_j^K(x_i)**: eigenvector components of B_K, which are algebraic functions of the matrix entries. The matrix entries involve log p_1, ..., log p_K (transcendental) and x_i (algebraic).

The obstruction: eigenvector components phi_j^K(x_i) are **not** algebraic numbers -- they depend on transcendental quantities (the logs of primes already in B_K). Baker's theorem in its standard form requires algebraic coefficients.

### 5.3 Possible extensions

- **Nesterenko-type results** on algebraic independence of values of analytic functions might handle the transcendental eigenvector components.
- **Hermite-Lindemann for the archimedean part**: the Cauchy kernel 1/(x_i + x_j) with algebraic nodes gives a matrix with algebraic entries, so its eigenvectors involve algebraic numbers over Q(x_1, ..., x_n). At step K = 0, Baker's theorem could apply directly.
- **Inductive algebraic structure**: if the eigenvector components at step K lie in a known transcendence class (e.g., the field generated by log p_1, ..., log p_K over the algebraics), Baker-type bounds for linear forms in logarithms might extend.

This is the key technical gap. Bridging it would complete the proof.

---

## 6. Feasibility assessment

| Component | Status | Difficulty |
|:----------|:-------|:-----------|
| Secular equation framework | Classical, rigorous | Done |
| Inductive structure K -> K+1 | Clean, reduces to (SPO_K) | Done |
| Base case K = 0 (Cauchy matrix) | STP, Gantmacher-Krein | Done |
| Single-prime overlap nonvanishing | Needs transcendence theory | **Hard** |
| Baker's theorem at K = 0 | Plausible (algebraic eigenvectors) | Moderate |
| Baker's theorem at K >= 1 | Eigenvectors transcendental | **Open** |
| Compression M_a inherits interlacing | Projected rank-one update | Moderate |

### Overall rating: 5/10

This is the highest-rated lead so far. The inductive structure is clean and the reduction to single-prime overlaps is a genuine simplification. The base case is rigorous (Cauchy = STP). The obstacle is proving (SPO_K) for K >= 1, where eigenvector components are transcendental.

The computational test (secular_induction_test.py) will determine whether the overlaps stay bounded away from zero or decay dangerously. If they remain O(1/n), the programme is alive. If they decay exponentially, the inductive route faces the same gap-decay problem as the direct approach.

---

> *Each prime enters as a rank-one update. Strict interlacing propagates if the prime vector overlaps all eigenvectors.*
> *The Arithmetic Theorem reduces to single-prime overlaps: n conditions per step, not n^2.*
> *Baker's theorem is the natural tool. It works at K = 0. The K >= 1 case needs transcendental eigenvector control.*
> *Compute the overlaps. If they stay nonzero, the structure is right.*
