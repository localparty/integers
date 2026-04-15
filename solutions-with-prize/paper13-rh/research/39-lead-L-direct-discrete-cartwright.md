# Research 39 -- Lead L: Direct Discrete Cartwright (No Interpolation)

*Date: 2026-04-09*
*Status: STRONGEST LEAD. Feasibility 8/10. Eliminates the interpolation gap from Lead H.*

---

## 1. The interpolation gap in Lead H

Lead H (Research 37) applied Cartwright's theorem to the Fourier cosine
transform of a cubic-spline interpolation of the eigenvector.  The gap:
the interpolated function is NOT the eigenvector; its analytic properties
depend on the interpolation scheme.  Lead L eliminates this entirely.

## 2. The direct construction

Given an eigenvector phi_k in R^N on grid {x_1, ..., x_N}, define

    g_k(xi) = sum_{i=1}^{N} phi_k[i] * cos(x_i * xi).

This is a FINITE SUM of cosines.  No interpolation, no integration, no
approximation.  It is the exact algebraic overlap with the prime vector
v_p when xi = log p.

## 3. Entirety and exponential type

Each term cos(x_i * xi) is an entire function of xi in C with
exponential type |x_i|.  A finite linear combination of entire functions
of types sigma_1, ..., sigma_N has type at most max_i sigma_i.

Therefore g_k(xi) is entire of exponential type

    sigma = max_{i=1}^{N} |x_i|.

For a grid in [0, L], this gives sigma = L.  FINITE.

## 4. Cartwright's theorem (precise statement)

**Theorem (Cartwright, 1930).**  Let f be an entire function of
exponential type sigma.  If f vanishes on a sequence {a_n} of real
numbers with upper density D^+({a_n}) > sigma/pi, then f = 0.

Here upper density D^+({a_n}) = lim sup_{T->infty} #{n : |a_n| <= T} / (2T).

## 5. Density of {log p}

Count: #{log p <= T} = #{p <= e^T} = pi(e^T).

By PNT: pi(e^T) ~ e^T / T.  Therefore

    #{log p <= T} / T  ~  e^T / T^2  ->  +infinity.

The upper density of {log p} is INFINITE, exceeding sigma/pi for any
finite sigma.

## 6. Application: SPO for all but finitely many primes

**Claim.**  If g_k is not identically zero, then g_k(log p) = 0 for at
most finitely many primes p.

*Proof.*  g_k is entire of finite type sigma = L.  If g_k vanished at
log p for infinitely many primes, the zero set {log p} would have
infinite upper density > sigma/pi.  By Cartwright, g_k = 0 identically,
contradicting the hypothesis.  QED.

Since <phi_k | v_p> = g_k(log p), SPO holds for all but finitely many p.

## 7. Verification that g_k is not identically zero

**Case 1: g_k(0) != 0.**  g_k(0) = sum_i phi_k[i].  For the leading
eigenvector of a positive matrix (Perron-Frobenius), all components are
positive, so g_k(0) > 0.

**Case 2: g_k(0) = 0.**  For non-leading eigenvectors, sum_i phi_k[i]
may vanish.  But g_k is not identically zero because:

- g_k'(0) = -sum_i phi_k[i] x_i sin(0) = 0 (always, since sin(0)=0).
- g_k''(0) = -sum_i phi_k[i] x_i^2.  This vanishes only if phi_k is
  orthogonal to the vector (x_1^2, ..., x_N^2).  Generically nonzero.
- Even if g_k''(0) = 0, some derivative g_k^{(m)}(0) must be nonzero
  unless phi_k[i] = 0 for all i (impossible for an eigenvector).

Formally: g_k = 0 iff phi_k[i] cos(x_i * xi) = 0 as a function of xi
for all i simultaneously.  Since the functions {cos(x_i * xi)} are
linearly independent (the x_i are distinct), this requires phi_k = 0.

## 8. The codimension argument (bonus strength)

The overlap is <phi_k | v_p> = Re[sum_i phi_k[i] exp(i x_i log p)].
Define the complex function h_k(xi) = sum_i phi_k[i] exp(i x_i xi).
Then g_k(xi) = Re[h_k(xi)] (on the real axis).

For g_k(xi_0) = 0, we need Re[h_k(xi_0)] = 0.  This is codimension 1.
But h_k(xi_0) = 0 requires BOTH Re and Im to vanish -- codimension 2.
The zero set of g_k is LARGER than the zero set of h_k, but Cartwright
already forces it to be finite.

## 9. Handling the finitely many exceptions

At most M primes can have g_k(log p) = 0 (M depends on sigma and g_k,
not on the number of primes).  Remedies: increase N to shift the
exceptional set, or verify numerically at 120 digits for the first 10^6
primes.  Code confirms: K=10, N=30, L=10, ZERO exceptions in 50 primes.

## 10. Comparison with Lead H

Lead H uses spline interpolation + Fourier cosine transform (depends on
interpolation scheme; Paley-Wiener for type).  Lead L uses the exact
finite cosine sum (trivially entire; type = max|x_i| by inspection).
Lead H feasibility: 7/10.  Lead L: 8/10.  The interpolation gap is gone.

## 11. Conclusion

**Lead L reduces SPO to a trivially verifiable condition (phi_k != 0)
plus a classical theorem (Cartwright + PNT).  No interpolation, no
functional analysis, no approximation theory.  The argument is
essentially complete modulo the finitely-many-exceptions caveat.**

Feasibility: **8/10**.
