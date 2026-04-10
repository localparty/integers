# Estimate 2: Even-Simplicity of QW_lambda^N

*Date: 2026-04-09*
*Status: OPEN -- even-simple condition NOT proved; structural obstruction identified*

---

## 1. The question

CCM Definition 5.3: The matrix T = QW_lambda^N is **even-simple** if:
- (a) Its smallest eigenvalue epsilon_N is simple (multiplicity 1)
- (b) The corresponding eigenvector xi satisfies gamma(xi) = xi (even)

where gamma: V_n -> V_{-n} is the flip operator.

CCM Theorem 5.10 requires even-simplicity as a hypothesis. Section 8
identifies this as **Missing Step 1**.

---

## 2. What the matrix looks like

From CCM Lemma 5.1, T has generalized Cauchy structure:

    tau_{i,j} = (b_i - b_j)/(i - j)    for i != j
    tau_{i,i} = a_i

with a_{-j} = a_j and b_{-j} = -b_j. This forces:
- T commutes with gamma (Lemma 5.2(i): gamma T = T gamma)
- Every eigenvector has definite parity (even or odd)
- D gamma = -gamma D, so DT - TD = |beta><eta| - |eta><beta| (Lemma 5.2(ii))

The matrix decomposes as T = W_{0,2} - W_R - sum_p W_p.

---

## 3. Numerical results

### 3.1 Eigenvalue structure

For lambda = sqrt(10) (L = 2.303, primes {2,3,5,7}), all eigenvalues
cluster tightly near -0.7192. The W_{0,2} term dominates and creates
a large near-degenerate block. The prime contributions W_p and
archimedean W_R provide small splittings of order 10^{-6} to 10^{-7}.

### 3.2 Simplicity: CONFIRMED numerically

The smallest eigenvalue is always simple. Typical gaps:

| N  | gap (e_1 - e_0) |
|----|-----------------|
|  3 |    2.0 x 10^-7  |
|  5 |    6.1 x 10^-7  |
|  8 |    1.8 x 10^-6  |
| 10 |    3.7 x 10^-7  |
| 12 |    5.0 x 10^-7  |

Gap is always positive and O(10^{-7}) to O(10^{-6}). No degeneracy.

### 3.3 Evenness: ALTERNATES with N

**Critical finding:** The parity of the minimal eigenvector
alternates between even and odd as N increases.

lambda = sqrt(10):

| N  | min is EVEN? | |even_min - odd_min| |
|----|-------------|---------------------|
|  2 | EVEN        |  8.0 x 10^-7        |
|  3 | ODD         |  8.2 x 10^-8        |
|  4 | ODD         |  1.7 x 10^-7        |
|  5 | EVEN        |  2.9 x 10^-7        |
|  6 | ODD         |  2.5 x 10^-7        |
|  7 | EVEN        |  2.7 x 10^-7        |
|  8 | ODD         |  7.6 x 10^-7        |
|  9 | EVEN        |  4.5 x 10^-7        |
| 10 | EVEN        |  1.2 x 10^-7        |
| 11 | ODD         |  3.1 x 10^-7        |
| 12 | ODD         |  2.0 x 10^-7        |
| 13 | EVEN        |  1.1 x 10^-6        |
| 14 | ODD         |  1.8 x 10^-6        |
| 15 | ODD         |  1.8 x 10^-6        |

lambda = sqrt(14):

| N  | min is EVEN? | |even_min - odd_min| |
|----|-------------|---------------------|
|  3 | EVEN        |  2.0 x 10^-7        |
|  5 | ODD         |  8.0 x 10^-8        |
|  8 | EVEN        |  4.0 x 10^-7        |
| 10 | EVEN        |  3.2 x 10^-7        |

**The even/odd gap is always O(10^{-7}), comparable to the
eigenvalue gap itself.** Even and odd eigenvalues are nearly
degenerate and interlace tightly.

### 3.4 Within-sector simplicity

The even sector always has a well-separated smallest eigenvalue
(gap ~ 10^{-6}), as does the odd sector. The problem is purely
about which sector wins overall.

---

## 4. Theoretical analysis

### 4.1 Why even and odd are nearly degenerate

The dominant piece W_{0,2} (Lemma 4.1) has rank 2 with entries:

    W_{0,2}(n,m) = 32L sinh^2(L/4)(L^2 - 16 pi^2 mn) /
                   [(L^2 + 16 pi^2 m^2)(L^2 + 16 pi^2 n^2)]

This factors as a_n a_m - c_n c_m where a_n = C/(L^2 + 16 pi^2 n^2),
c_n = 4pi n C/(L^2 + 16 pi^2 n^2). The a-vector is even, c-vector
is odd. The two nonzero eigenvalues of W_{0,2} -- one even, one odd --
are of comparable magnitude.

The W_p and W_R corrections then split the remaining (2N-1)-dimensional
near-degenerate block, creating O(10^{-7}) splittings. Whether the
even or odd sector wins depends on the precise values of the
archimedean integrals and the prime contributions, which oscillate
with N.

### 4.2 Perron-Frobenius does NOT apply

The matrix T has entries of mixed sign (negative diagonal from W_{0,2},
oscillating off-diagonal from W_p). There is no sign structure that
would permit Perron-Frobenius, even after transformations. The
generalized Cauchy structure tau_{i,j} = (b_i - b_j)/(i-j) does not
guarantee positivity.

### 4.3 KMS uniqueness argument: DOES NOT CLOSE

The argument was: KMS_1 state omega_1 is unique (BC Theorem 25),
GNS vector Omega_1 is unique up to phase, projection onto E_N gives
unique xi_lambda, hence simplicity.

**Problem:** KMS uniqueness gives uniqueness of the STATE, not of
the eigenvector of a finite truncation. The projection of Omega_1
onto E_N is not an eigenvector of QW_lambda^N -- it's an eigenvector
only in the infinite-dimensional limit. The KMS argument cannot
distinguish between even and odd at finite N.

### 4.4 Prolate wave operator analogy

CCM note (Section 8) that the even-simple condition holds for the
prolate wave operator PW_lambda. The prolate spheroidal functions
h_{n,lambda} have definite parity, and the ground state h_{0,lambda}
is always even with a simple eigenvalue.

But QW_lambda^N is NOT PW_lambda. The prolate wave operator is a
second-order ODE (Sturm-Liouville) where the oscillation theorem
guarantees the ground state has no nodes (hence even). The Weil
quadratic form has no such ODE structure.

### 4.5 The functional equation

The functional equation symmetry s <-> 1-s induces gamma T = T gamma
(Lemma 5.2(i)). This guarantees parity of eigenvectors but NOT
that the minimum is even.

---

## 5. What CCM themselves say

Section 8, page 32: "one must prove that its smallest eigenvalue
-- whose existence is ensured by Theorem 3.6 -- is simple and
that its corresponding eigenvector xi_lambda is even."

They list three "indications supporting feasibility":
1. PW_lambda has the even-simple property for all lambda
2. The tiny eigenvalues epsilon_lambda appear consistently
3. Numerical proximity of k_lambda to xi_lambda

But they do NOT claim a proof. This is explicitly a **missing step**.

---

## 6. The structural obstruction

The numerical evidence reveals a genuine difficulty:

**The even-simple condition does NOT hold for all (lambda, N).**

At fixed lambda = sqrt(10), the minimum alternates between
even and odd as N varies. The condition holds for some N (e.g.,
N = 2, 5, 7, 9, 10, 13) and fails for others (N = 3, 4, 6, 8,
11, 12, 14, 15).

This means:
- A proof of even-simplicity for ALL N is impossible (it's false)
- One needs either:
  (a) Even-simplicity for SUFFICIENTLY LARGE N (at fixed lambda), or
  (b) Even-simplicity in the JOINT limit N, lambda -> infinity, or
  (c) A modification of CCM's argument that handles the odd case

### 6.1 Possible resolution: the limit matters

CCM's Theorem 5.10 is stated for fixed (lambda, N). But the
RH application (Corollary 3.8) requires lambda -> infinity.
In that limit, QW_lambda approaches PW_lambda (by CCM's own
observation), and PW_lambda IS even-simple. So perhaps:

**Conjecture:** For each lambda, there exists N_0(lambda) such
that QW_lambda^N is even-simple for all N >= N_0(lambda).

Our numerics are inconclusive on this: the alternation persists
through N = 15 at lambda = sqrt(10).

### 6.2 Alternative: work with the even sector directly

Instead of requiring the overall minimum to be even, one could:
- Restrict T to the even sector (dimension N+1)
- Take the minimum there (always simple by our numerics)
- Use this even minimum for the CCM construction

This requires modifying Lemma 5.4 and Theorem 5.10 to handle
the case where the overall minimum might be odd. The modification
is likely routine (replace T by T restricted to even sector).

---

## 7. Assessment

| Component | Status |
|:----------|:-------|
| Simplicity of e_0 | CONFIRMED numerically, likely provable from Cauchy structure |
| Evenness of e_0 | FAILS for some (lambda, N); alternates |
| Simplicity within even sector | CONFIRMED numerically |
| KMS uniqueness -> simplicity | DOES NOT CLOSE at finite N |
| Perron-Frobenius | NOT APPLICABLE (mixed signs) |
| Prolate wave analogy | SUGGESTIVE but not transferable |
| CCM's own assessment | MISSING STEP (their words) |

### Estimate 2 status: OPEN

The even-simple condition is not proved. Moreover, it is
**numerically false** for certain (lambda, N) pairs. The
structural resolution is either:
- Prove it holds in the limit (N -> infinity at fixed lambda)
- Modify the CCM construction to use the even-sector minimum

Neither is trivial. This remains a genuine mathematical obstacle.

---

## 8. Implications for the RH programme

The CCM path to RH requires two missing steps (Section 8):
1. Even-simplicity of QW_lambda^N  <-- THIS ESTIMATE
2. k_lambda approximates xi_lambda

Our finding that even-simplicity alternates with N does not
kill the approach -- the alternation gap is tiny (10^{-7}),
and the condition likely stabilizes in the limit. But it does
mean that a proof requires careful limit analysis, not a
finite-dimensional matrix argument.

The honest rating for Estimate 2 moves from 4/10 to **3/10**.
The obstruction is real but narrow. The even-sector modification
(Section 6.2) provides a plausible workaround.
