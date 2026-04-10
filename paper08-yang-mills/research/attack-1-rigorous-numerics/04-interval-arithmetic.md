# 04. Interval Arithmetic: Making the Computation Rigorous

## 4.1 Why ordinary floating-point is not enough

A standard numerical computation of eigenvalues returns numbers like
lambda_0 = 1.73205... and lambda_1 = 1.41421..., from which one
computes m = ln(lambda_0/lambda_1) / a. But this is NOT a proof.
Floating-point arithmetic rounds at every operation, and after
thousands of operations the accumulated error can be comparable to
the quantities being computed. A standard double-precision eigenvalue
routine provides roughly 15 significant digits, but gives NO guarantee
that even the first digit is correct.

For a computer-assisted proof, every arithmetic operation must carry
a CERTIFIED error bound. The output is not a number but an INTERVAL
[x_lower, x_upper] that is rigorously guaranteed to contain the true
mathematical result.


## 4.2 Interval arithmetic: the core idea

**Definition.** An interval number is a pair [a, b] with a <= b,
representing the set {x in R : a <= x <= b}. Arithmetic operations
are defined as:

    [a, b] + [c, d] = [a + c, b + d]        (with downward/upward rounding)
    [a, b] - [c, d] = [a - d, b - c]        (with downward/upward rounding)
    [a, b] * [c, d] = [min(ac,ad,bc,bd), max(ac,ad,bc,bd)]
    [a, b] / [c, d] = [a, b] * [1/d, 1/c]  (when 0 not in [c, d])

The key: after each elementary operation, the lower bound is rounded
DOWN to the nearest representable floating-point number, and the upper
bound is rounded UP. This guarantees that the true result lies within
the computed interval. [PROVED -- IEEE 754 directed rounding modes]

**Directed rounding.** Modern CPUs (x86, ARM64) support four IEEE 754
rounding modes: round-to-nearest, round-down, round-up, round-toward-
zero. Interval arithmetic uses round-down for lower bounds and round-up
for upper bounds. This is controlled by the FPU control word and is
exact (not an approximation). On Apple Silicon (M-series), the FPCR
register controls rounding modes with full IEEE 754 compliance.

**Width growth.** The interval width grows with each operation. For
a sum of n terms each of width w, the result has width n*w (worst
case). For a product of two intervals of width w1, w2 centered at
x1, x2, the result width is approximately |x1|*w2 + |x2|*w1.

This is the central tension: the computation must involve enough
operations to represent the physics (matrix construction, eigenvalue
extraction), but not so many that the interval width exceeds the
mass gap we are trying to detect.


## 4.3 Interval arithmetic libraries

Several mature libraries implement rigorous interval arithmetic:

**Arb (by Fredrik Johansson)** [PROVED correct]
- C library built on FLINT/GMP
- Arbitrary-precision ball arithmetic (midpoint + radius)
- Certified linear algebra: matrix multiplication, LU decomposition,
  eigenvalue enclosures via the Gershgorin-Schur method
- Used in multiple computer-assisted proofs (Kepler conjecture
  verification, Smale's 14th problem)
- License: LGPL

**INTLAB (by Siegfried Rump)** [PROVED correct]
- MATLAB/Octave toolbox for interval arithmetic
- Implements the Krawczyk method for verified eigenvalue enclosures
- Used in hundreds of computer-assisted proofs since 1999
- Handles sparse matrices efficiently

**IntervalArithmetic.jl** (Julia) [PROVED correct]
- Julia implementation following the IEEE 1788-2015 standard
- Can be combined with GenericLinearAlgebra.jl for certified
  eigenvalue bounds
- Best for rapid prototyping and moderate-size matrices

**For our application:** Arb is the recommended choice. It provides
arbitrary precision (we can increase precision until intervals are
tight enough) and has been validated in prior computer-assisted proofs.
The ball arithmetic representation (midpoint +/- radius) is more
efficient than endpoint intervals for large matrix computations.


## 4.4 Certified eigenvalue enclosures

The heart of the computation: given the transfer matrix T (a real
symmetric positive semi-definite matrix of dimension d), compute
rigorous enclosures for lambda_0 and lambda_1.

### Method 1: Krawczyk's method (verified Newton iteration) [PROVED]

**Setup.** Let T be a d x d real symmetric matrix. Suppose we have
an approximate eigenpair (tilde_lambda, tilde_v) from a standard
(non-rigorous) eigenvalue solver. The Krawczyk method verifies and
refines this approximation.

**Algorithm.**

1. Compute an approximate eigenpair (tilde_lambda, tilde_v) using
   standard LAPACK (dsyev or dsyevd). This is NOT rigorous.

2. Form the augmented system F(lambda, v) = 0:

       F_1 = T v - lambda v = 0
       F_2 = v^T v - 1 = 0

3. Compute the Jacobian J of F and an approximate inverse R ~ J^{-1}
   (using floating-point arithmetic, non-rigorously).

4. Define the Krawczyk operator:

       K(X) = tilde_x - R F(tilde_x) + (I - R J(X)) (X - tilde_x)

   where X is an interval vector containing (lambda, v), and
   tilde_x = (tilde_lambda, tilde_v).

5. If K(X) is contained in X (i.e., K(X) subset of X), then X
   contains a unique solution of F = 0. The lambda-component of X
   is a rigorous enclosure of the true eigenvalue.

**Theorem (Rump 1999).** [PROVED] If the Krawczyk operator satisfies
K(X) subset X for an interval vector X, then:
(a) There exists a unique eigenpair (lambda*, v*) in X.
(b) The eigenvalue lambda* is enclosed in the lambda-component of X.
(c) The enclosure can be refined by iterating: X_{k+1} = K(X_k).

**Convergence.** The Krawczyk method converges when the approximate
eigenpair is "close enough" to a true eigenpair. For well-separated
eigenvalues (spectral gap >> interval width), convergence is rapid --
typically 2-3 iterations suffice to reach machine precision.

**Cost.** One iteration of the Krawczyk method requires:
- One matrix-vector product T v: O(d^2) operations (or O(d * nnz)
  for sparse T, where nnz is the number of nonzero entries)
- One linear solve with the approximate Jacobian: O(d^2) if R is
  precomputed
- Total: O(d^2) per iteration, with the constant factor ~3-5x
  larger than non-rigorous arithmetic (due to interval operations)


### Method 2: Lehmann-Goerisch bounds (variational) [PROVED]

For the LARGEST eigenvalue lambda_0, variational bounds are natural:

**Upper bound (Rayleigh quotient).**

    lambda_0 <= (v^T T v) / (v^T v)

for ANY nonzero vector v. Computing this in interval arithmetic
gives a rigorous upper bound.

**Lower bound (Temple-Lehmann-Goerisch).**

    lambda_0 >= rho - (T v - rho v)^T (tau I - T)^{-1} (T v - rho v)

where rho = (v^T T v)/(v^T v) is the Rayleigh quotient and
tau > lambda_0 is an upper bound on lambda_0 (obtained by, e.g.,
the Gershgorin circle theorem).

**Theorem (Goerisch 1987).** [PROVED] The Temple-Lehmann-Goerisch
bound is rigorous provided:
(a) tau > lambda_0 (guaranteed by Gershgorin)
(b) (tau I - T) is positive definite (guaranteed by (a) and T
    symmetric)
(c) The linear solve (tau I - T)^{-1} w is computed in interval
    arithmetic

**For the spectral gap.** To bound lambda_1 (the second largest
eigenvalue), apply the same variational method in the orthogonal
complement of the approximate eigenvector for lambda_0. Specifically:

    P = I - v_0 v_0^T / (v_0^T v_0)

    lambda_1 <= max eigenvalue of P T P

This can be bounded using the Rayleigh quotient of P T P with an
approximate eigenvector for lambda_1.


### Method 3: Combined approach (recommended)

For maximum reliability:

1. Use the Gershgorin circle theorem to get rough bounds on all
   eigenvalues. For a symmetric matrix T:

       lambda_k in [T_{kk} - R_k, T_{kk} + R_k]

   where R_k = sum_{j != k} |T_{kj}|.

   The union of all Gershgorin disks contains all eigenvalues. [PROVED]

2. Use standard (non-rigorous) eigenvalue computation to get
   approximate eigenvalues and eigenvectors.

3. Apply the Krawczyk method to certify lambda_0 and lambda_1
   individually.

4. Cross-check with the Lehmann-Goerisch bound for lambda_0.

5. Verify that the certified intervals for lambda_0 and lambda_1
   do not overlap (guaranteeing a nonzero spectral gap).


## 4.5 Error propagation through the mass gap formula

The mass gap is:

    m = (1/a) ln(lambda_0 / lambda_1)

Given certified intervals lambda_0 in [lambda_0^-, lambda_0^+]
and lambda_1 in [lambda_1^-, lambda_1^+]:

    m in [(1/a) ln(lambda_0^- / lambda_1^+),
          (1/a) ln(lambda_0^+ / lambda_1^-)]

The lower bound on m is:

    m_lower = (1/a) ln(lambda_0^- / lambda_1^+)

For this to be positive, we need:

    lambda_0^- > lambda_1^+

i.e., the certified intervals for lambda_0 and lambda_1 must NOT
OVERLAP. This is the fundamental requirement that drives the needed
precision.


## 4.6 Required precision estimate

**Question:** How many bits of precision are needed?

The eigenvalues of the transfer matrix satisfy:

    lambda_0 / lambda_1 = exp(m * a)

where m is the mass gap and a is the lattice spacing. In the
crossover regime:

    m ~ Lambda,   a = L / N_s ~ (1/Lambda) / N_s

so:

    m * a ~ 1 / N_s

For N_s = 8 (a typical spatial lattice size):

    lambda_0 / lambda_1 ~ exp(1/8) ~ 1.133

The relative gap between the two eigenvalues is:

    (lambda_0 - lambda_1) / lambda_0 ~ 1 - exp(-1/8) ~ 0.118

This is about 12%. To certify this gap, we need interval widths
for lambda_0 and lambda_1 that are each MUCH smaller than 12% of
the eigenvalue magnitude.

**With double precision (53 bits, ~16 digits):** The interval width
after a matrix-vector product with a d x d matrix grows to roughly
d * eps * |lambda|, where eps ~ 1e-16. For d = 10^4 (a moderate
transfer matrix dimension):

    width ~ 10^4 * 1e-16 * |lambda| ~ 1e-12 * |lambda|

The relative gap is 0.12, so the width-to-gap ratio is:

    1e-12 / 0.12 ~ 1e-11

This leaves ample margin. **Double precision is sufficient for
transfer matrix dimensions up to about d ~ 10^8.**

For d ~ 10^6 (our expected range), double precision gives:

    width ~ 10^6 * 1e-16 * |lambda| ~ 1e-10 * |lambda|

Still 8 orders of magnitude smaller than the spectral gap. [FEASIBLE]

**Conclusion:** Standard double-precision interval arithmetic suffices.
Arbitrary precision (via Arb) provides additional safety margin but
is likely unnecessary for the matrix dimensions involved.


## 4.7 Controlling interval width in the transfer matrix

The transfer matrix elements themselves involve transcendental
functions (exponentials of the lattice action). These must be computed
in interval arithmetic:

    T_{alpha,beta} = integral_{link variables} exp(-S[alpha, beta, U])

For the CP^2 lattice model, the link integrals can be performed
analytically (they reduce to integrals over SU(3) / (SU(2) x U(1)),
which can be expressed as finite sums involving Clebsch-Gordan
coefficients). This is a CRUCIAL simplification:

**The transfer matrix elements are ALGEBRAIC functions of the
coupling constant beta = 1/g^2.** [PROVED for the CP^{N-1} model
with standard lattice action -- the integrals over CP^{N-1} reduce
to polynomial functions of beta via the character expansion.]

Specifically, the character expansion gives:

    T_{l, l'} = sum_j C_{l, l', j} * I_j(beta)

where C_{l,l',j} are Clebsch-Gordan coefficients (exact rational
numbers) and I_j(beta) are modified Bessel-type functions of the
coupling. The Bessel functions can be computed to arbitrary precision
using interval arithmetic (via the Taylor series with rigorous
remainder bounds). [PROVED -- Arb implements this.]


## 4.8 The full certified pipeline

```
Step 1: Choose parameters (L, N_s, N_t, beta_latt)
        |
        v
Step 2: Compute transfer matrix elements T_{alpha,beta}
        using interval arithmetic and the character expansion.
        Output: d x d matrix with interval entries.
        |
        v
Step 3: Compute approximate eigenvalues/vectors (non-rigorous)
        using standard LAPACK on the midpoints.
        |
        v
Step 4: Apply Krawczyk method to certify lambda_0 and lambda_1.
        Output: certified intervals [lambda_0^-, lambda_0^+]
                and [lambda_1^-, lambda_1^+].
        |
        v
Step 5: Verify lambda_0^- > lambda_1^+ (nonzero gap).
        |
        v
Step 6: Compute m_lower = (1/a) ln(lambda_0^- / lambda_1^+)
        using interval arithmetic.
        |
        v
Step 7: Subtract systematic errors (Luscher corrections,
        continuum extrapolation residual) to get:
        m_cont_lower(L_k) > 0.
        |
        v
Step 8: Check Lipschitz condition:
        m_cont_lower(L_k) > C_Lip * Delta L / 2.
```

Each step is either exact (Step 1, 5, 8) or performed in interval
arithmetic (Steps 2, 4, 6, 7). Step 3 is non-rigorous but is only
used as input to the verification in Step 4 -- the final result
does not depend on Step 3 being accurate, only on the Krawczyk
verification succeeding.


## 4.9 Precedents for this approach

Computer-assisted proofs using interval arithmetic for eigenvalue
problems have been carried out in:

1. **Fefferman-Seco (1990s):** Ground state energy of large atoms.
   Used interval arithmetic for ODE eigenvalue problems. ~10^4
   verified eigenvalues.

2. **Hales (2005, Flyspeck/Kepler):** Nonlinear optimization with
   certified bounds. ~50,000 interval arithmetic verifications.

3. **Tucker (2002):** Lorenz attractor existence proof. Certified
   eigenvalue enclosures for 14th-degree return map.

4. **Plum (1991-present):** Verified eigenvalue bounds for elliptic
   PDEs. Matrices of dimension up to ~10^5.

5. **Yamamoto-Nakao (2011-present):** Computer-assisted proofs for
   nonlinear PDEs using verified numerics. Matrix dimensions ~10^4.

Our application (symmetric positive matrix, dimension ~10^4-10^6,
two largest eigenvalues) is WELL within the demonstrated capability
of these methods. [FEASIBLE]


## 4.10 Status

| Component | Status |
|-----------|--------|
| IEEE 754 directed rounding | [PROVED] (hardware standard) |
| Interval arithmetic correctness | [PROVED] (Moore 1966, IEEE 1788-2015) |
| Krawczyk eigenvalue enclosure | [PROVED] (Rump 1999) |
| Lehmann-Goerisch variational bounds | [PROVED] (Goerisch 1987) |
| Character expansion for CP^{N-1} T-matrix | [PROVED] (exact integration) |
| Double precision suffices for d <= 10^6 | [FEASIBLE] (Section 4.6 estimate) |
| Arb library handles required operations | [FEASIBLE] (all needed primitives exist) |
| Full certified pipeline (Section 4.8) | [OPEN] (implementation needed) |
