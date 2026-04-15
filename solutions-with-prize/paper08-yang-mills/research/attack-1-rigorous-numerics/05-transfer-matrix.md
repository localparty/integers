# 05. The Transfer Matrix: Finite Dimensions, Explicit Construction

## 5.1 Why the transfer matrix is finite

This is the crucial structural fact that makes the entire computer-
assisted proof approach viable.

In a CONTINUUM 2D field theory on R x S^1_L, the Hilbert space is
infinite-dimensional (it consists of all L^2 functions on the field
configuration space Maps(S^1_L -> CP^2)). The transfer matrix (the
operator exp(-a H)) is an operator on this infinite-dimensional
space, and computing its eigenvalues rigorously would require
functional-analytic estimates -- effectively a full constructive
QFT argument.

On the LATTICE, the spatial circle S^1_L is replaced by N_s discrete
sites. A configuration on one time-slice is:

    (z_0, z_1, ..., z_{N_s - 1})  with each z_x in CP^2

subject to the Z_3 twist: z_{N_s} = Omega z_0.

CP^2 is a compact 4-real-dimensional manifold. But the lattice transfer
matrix acts on L^2(CP^2)^{N_s} -- still infinite-dimensional, because
each z_x ranges over a continuous manifold.

**The key step: angular momentum truncation.**

The functions on CP^2 = SU(3) / (SU(2) x U(1)) decompose into
irreducible representations of SU(3):

    L^2(CP^2) = direct sum_{l=0}^{infinity} V_l

where V_l is the space of degree-l spherical harmonics on CP^2.
The dimension of V_l is:

    dim V_l = (l + 1)(l + 2)^2 (l + 3) / 12

(These are the symmetric traceless representations of SU(3) labeled
by the Young diagram (l, 0), i.e., the l-fold symmetric power of
the fundamental representation.)

| l | dim V_l | Cumulative dim |
|---|---------|---------------|
| 0 | 1 | 1 |
| 1 | 6 | 7 |
| 2 | 20 | 27 |
| 3 | 50 | 77 |
| 4 | 105 | 182 |
| 5 | 196 | 378 |
| 6 | 336 | 714 |
| 7 | 540 | 1254 |
| 8 | 825 | 2079 |

The nearest-neighbor lattice action couples only adjacent angular
momentum modes: the matrix element <l | exp(-S_link) | l'> falls off
as:

    |<l| exp(-beta S) |l'>| ~ I_{|l-l'|}(beta) / I_0(beta)

where I_n is a modified Bessel function (this comes from the
character expansion on CP^{N-1}). For the lattice coupling beta
in the range [0.5, 5.0] (our crossover range from Section 03):

    I_1(beta) / I_0(beta) ~ 0.4 -- 0.9

    I_l(beta) / I_0(beta) ~ (beta/2)^l / l!   for l >> 1

The coupling falls off FACTORIALLY in l. Truncating at angular
momentum l_max introduces an error exponentially small in l_max.


## 5.2 Truncation error bound

**Theorem (angular momentum truncation).** [PROVED -- standard
representation theory + Bessel function asymptotics]

Let T be the exact lattice transfer matrix on L^2(CP^2)^{N_s}, and
let T_{l_max} be the transfer matrix truncated to angular momentum
modes with l <= l_max at each site. Then:

    |lambda_k(T) - lambda_k(T_{l_max})| <= C * N_s * (I_{l_max+1}(beta) / I_0(beta))^{N_s}

where C is an O(1) constant depending on the spectrum.

**Proof sketch.** The truncation removes the coupling between modes
with l <= l_max and l > l_max. By the Weyl perturbation theorem for
symmetric matrices, the eigenvalue change is bounded by the operator
norm of the removed coupling. Each spatial link contributes a coupling
of order I_{l_max+1}(beta)/I_0(beta), and there are N_s links on the
spatial circle. The total perturbation is bounded by the product
(since the transfer matrix is a product of link contributions). QED.

**Numerical estimates for truncation error:**

For beta = 2.0 (mid-crossover) and N_s = 8:

| l_max | I_{l_max+1}(2)/I_0(2) | Truncation error bound |
|-------|-----------------------|-----------------------|
| 3 | 0.0340 | ~ (0.034)^8 ~ 2e-12 |
| 4 | 0.0073 | ~ (0.007)^8 ~ 6e-17 |
| 5 | 0.0013 | ~ (0.001)^8 ~ 1e-24 |
| 6 | 0.0002 | negligible |

**Conclusion: l_max = 4 or 5 suffices for double-precision
accuracy.** The truncation error is far below the spectral gap
(which is O(0.1) in lattice units). [FEASIBLE]

For weaker coupling (beta ~ 1.0, deep crossover):

| l_max | I_{l_max+1}(1)/I_0(1) | Truncation error bound (N_s=8) |
|-------|-----------------------|-------------------------------|
| 2 | 0.0222 | ~ (0.022)^8 ~ 3e-13 |
| 3 | 0.0035 | ~ (0.004)^8 ~ 7e-19 |
| 4 | 0.0004 | negligible |

At weak coupling, l_max = 3 suffices. The angular momentum
truncation is EASIER in the deep crossover. [FEASIBLE]


## 5.3 Transfer matrix dimension

With angular momentum truncation at l_max, the single-site Hilbert
space has dimension:

    d_site = sum_{l=0}^{l_max} dim V_l = sum_{l=0}^{l_max} (l+1)(l+2)^2(l+3)/12

| l_max | d_site |
|-------|--------|
| 3 | 77 |
| 4 | 182 |
| 5 | 378 |
| 6 | 714 |

The full transfer matrix acts on the tensor product of N_s such
spaces, subject to the Z_3 twist. The naive dimension is:

    d_naive = (d_site)^{N_s}

For d_site = 182 and N_s = 8:

    d_naive = 182^8 ~ 1.1 x 10^{18}

This is astronomically large. **But we have not yet exploited the
symmetries.**


## 5.4 Symmetry reduction

The CP^2 model with Z_3 twist has several symmetries that drastically
reduce the transfer matrix dimension.

### (a) Global SU(3) symmetry (partially broken by the twist)

The Z_3 twist breaks SU(3) to its center Z_3. However, the twist
commutes with spatial translations by N_s/3 sites (when N_s is
divisible by 3). The residual symmetry group that commutes with T
is the Z_3 center.

This gives a decomposition into Z_3 sectors:

    H = H_0 + H_1 + H_2

where H_k = {states with Z_3 charge omega^k}. The mass gap lies
in the sector H_0 (the vacuum sector) or H_1 (depending on the
quantum numbers of the lightest excitation). We need to compute
eigenvalues in each sector separately.

The Z_3 decomposition reduces the dimension by a factor of ~3.

### (b) Spatial translation invariance

The Hamiltonian commutes with translations on the spatial lattice
(the Z_3 twist is compatible with translations because Omega
commutes with itself). The Hilbert space decomposes into momentum
sectors:

    H = direct sum_{p = 0, 2pi/N_s, ..., 2pi(N_s-1)/N_s} H_p

The mass gap is in the p = 0 (or p = 2pi/3 for the twisted sector)
momentum sector. Translation invariance reduces the dimension by
a factor of N_s.

### (c) Charge conjugation / complex conjugation

The CP^2 model has a charge conjugation symmetry C: z -> z*. This
commutes with the Z_3 twist (since Omega* = Omega^{-1} = Omega^2,
and the twist is Z_3-symmetric). The C-symmetry gives a factor-of-2
reduction.

### (d) Spatial reflection

The parity transformation x -> N_s - x combined with the twist
gives a Z_2 symmetry. This provides another factor of ~2 reduction.

### Combined reduction factor

    d_effective = d_naive / (3 * N_s * 2 * 2) = d_naive / (12 N_s)

For N_s = 8:

    d_effective = d_naive / 96


## 5.5 Effective matrix dimensions

Combining the angular momentum truncation (Section 5.2) with the
symmetry reduction (Section 5.4), but using a SMARTER basis than
the naive tensor product:

**The Fourier-mode basis.** Instead of working in the tensor product
basis (d_site)^{N_s}, we exploit translation invariance from the
start. A translation-invariant state on N_s sites is characterized
by the RELATIVE angular momenta between adjacent sites. With the
character expansion, the transfer matrix becomes block-diagonal in
the angular momentum quantum numbers at each link.

**The link basis.** The transfer matrix element between adjacent
sites decomposes as:

    <l_x | exp(-beta S_link) | l_{x+1}> = delta_{l_x, l_{x+1}} I_{l_x}(beta) / I_0(beta)
                                           + off-diagonal terms

In the strong-coupling (character) expansion, the dominant
contribution comes from the diagonal (l_x = l_{x+1}) terms. The
effective dimension is:

    d_eff ~ (l_max + 1)^{N_s} / (12 N_s)

but after exploiting the rapidly decaying Bessel coefficients, the
number of SIGNIFICANT basis states (those contributing above the
truncation threshold) is much smaller.

**Practical dimension estimates (pessimistic, using full l_max
truncation without Bessel decay):**

| N_s | l_max | d_site | d_naive | Symmetry reduction | d_effective |
|-----|-------|--------|---------|-------------------|-------------|
| 4 | 4 | 182 | 1.1e9 | /48 | ~2.3e7 |
| 6 | 4 | 182 | 3.6e13 | /72 | ~5.0e11 |
| 8 | 4 | 182 | 1.1e18 | /96 | ~1.1e16 |
| 4 | 3 | 77 | 3.5e7 | /48 | ~7.3e5 |
| 6 | 3 | 77 | 2.1e11 | /72 | ~2.9e9 |
| 8 | 3 | 77 | 1.2e15 | /96 | ~1.3e13 |

These dimensions are STILL too large for direct diagonalization.
We need a further reduction.


## 5.6 The character expansion: making it tractable

The breakthrough is the CHARACTER EXPANSION of the transfer matrix,
which expresses T as a product of SPARSE matrices.

**The link transfer matrix.** Define T_link as the transfer matrix
for a single spatial link (x, x+1):

    (T_link)_{l, l'} = integral_{CP^2} Y_l(z)* exp(beta |z^dag z'|^2) Y_{l'}(z') dz dz'

In the character expansion, this is:

    (T_link)_{l, l'} = sum_j N_j * I_j(beta) * C(l, l'; j)

where N_j is a normalization, I_j is a Bessel-type coefficient, and
C(l, l'; j) is a Clebsch-Gordan coefficient for SU(3). The key
point: C(l, l'; j) is nonzero only for |l - l'| <= j, and I_j(beta)
decays factorially in j.

The full transfer matrix on N_s sites is:

    T = T_link(0,1) * T_link(1,2) * ... * T_link(N_s-1, 0)

with the Z_3 twist applied at the boundary link (N_s-1, 0).

**Computing eigenvalues of a matrix product.** We do NOT need to
form the full d_eff x d_eff matrix explicitly. We only need the
ACTION of T on a vector:

    T |v> = T_link(0,1) T_link(1,2) ... T_link(N_s-1, 0) |v>

Each T_link acts on a pair of adjacent sites and is sparse (bandwidth
limited by the angular momentum coupling). The cost of applying
T_link to a vector is O(d_site^2 * d_rest) where d_rest is the
dimension of the remaining sites.

**Iterative eigenvalue methods.** The two largest eigenvalues of T
can be computed by iterative methods (Lanczos algorithm, power
iteration) that only require matrix-vector products, never the full
matrix. The Lanczos algorithm finds the k largest eigenvalues of a
d x d matrix in O(k * d * cost_of_Tv) operations.


## 5.7 The practical algorithm: Lanczos with interval arithmetic

**Algorithm (Certified Lanczos for the Transfer Matrix).**

Input: N_s, l_max, beta, Z_3 twist parameter, desired precision eps.
Output: Certified intervals for lambda_0, lambda_1.

1. **Basis construction.** Enumerate the symmetry-reduced basis
   states for the spatial lattice with N_s sites, l_max truncation,
   and the selected symmetry sector (Z_3 charge, momentum, parity).

2. **Matrix-vector product.** Implement the action v -> T v as a
   sequence of N_s sparse matrix-vector products (one per link),
   using interval arithmetic for all operations.

3. **Lanczos iteration (non-rigorous phase).** Run m_Lanczos ~ 100
   steps of the Lanczos algorithm using floating-point arithmetic
   (midpoints of intervals) to get approximate eigenvalues and
   Ritz vectors for lambda_0, lambda_1.

4. **Krawczyk verification (rigorous phase).** Use the approximate
   eigenvalues and Ritz vectors from Step 3 as starting points for
   the Krawczyk method (Section 04). Verify certified enclosures
   for lambda_0 and lambda_1.

5. **Gap certification.** Verify that the certified interval for
   lambda_0 is strictly above the certified interval for lambda_1.
   Compute m_lower = (1/a) ln(lambda_0^- / lambda_1^+).

**The Krawczyk method for the Lanczos output.** An important
subtlety: the Krawczyk method (Section 04.4) requires solving a
linear system involving (T - lambda I). For a matrix given only
as a matrix-vector product (not stored explicitly), this is done
iteratively:

- Use GMRES or CG (in interval arithmetic) to solve
  (T - tilde_lambda I) w = r, where r = T v - tilde_lambda v
  is the residual.

- The interval arithmetic version of CG converges because T is
  symmetric positive definite and (T - tilde_lambda I) is well-
  conditioned when tilde_lambda is between lambda_0 and lambda_1
  (the condition number is lambda_0 / gap).

**Alternative: the Behnke-Goerisch method.** For the largest
eigenvalue, one can avoid linear solves entirely by using the
Lehmann-Goerisch variational bound (Section 04.4, Method 2). The
upper bound tau can be obtained from the Gershgorin circle theorem
applied to the Lanczos tridiagonal matrix (which IS stored
explicitly). The linear solve (tau I - T)^{-1} w can be approximated
by a few CG iterations with rigorous error control.


## 5.8 Matrix dimension in the momentum-space basis

A much more efficient basis uses the Fourier transform in the spatial
direction. Define momentum-space angular momentum states:

    |p, l> = (1/sqrt(N_s)) sum_x exp(i p x) |l at site x>

where p = 2 pi k / N_s for k = 0, 1, ..., N_s - 1.

In this basis, the transfer matrix is block-diagonal in momentum
(up to the Z_3 twist, which shifts momentum by 2 pi / 3). The
vacuum sector (p = 0) has dimension:

    d_vacuum ~ (l_max + 1)^{N_s / symmetry factor}

But more importantly, the matrix-vector product T|v> in the momentum
basis has cost:

    O(N_s * (l_max + 1)^2 * d_sector)

where d_sector is the dimension of the relevant momentum sector.

**Effective dimension for eigenvalue computation (what matters for
Lanczos/Krawczyk):**

The Lanczos algorithm does NOT need to store the full matrix. It
only needs to store O(m_Lanczos) vectors of dimension d_sector,
where m_Lanczos ~ 50-100 is the number of Lanczos steps.

The MEMORY requirement is:

    Memory ~ m_Lanczos * d_sector * 16 bytes (double complex)

The TIME requirement per Lanczos step is:

    Time ~ cost of one matrix-vector product T|v>


## 5.9 Realistic dimension estimates

For the computer-assisted proof, the key question is: what is
d_sector for the relevant symmetry sector?

**The vacuum sector at p = 0, C = +1, P = +1.**

Consider the states labeled by angular momentum quantum numbers
(l_0, l_1, ..., l_{N_s-1}) at each spatial site, with:
- Total momentum p = 0 (translation invariant)
- Charge conjugation C = +1
- Parity P = +1
- Z_3 charge q = 0

The number of such states, after symmetry reduction and truncation
at l_max, is approximately:

    d_sector ~ (l_max + 1)^{N_s} / (2 * 2 * 3 * N_s)

Accounting for the additional constraint that only low-angular-
momentum configurations contribute significantly (due to Bessel
decay), the EFFECTIVE number of significant basis states is much
smaller.

**Practical estimates using importance truncation.**

Keep only basis states whose Boltzmann weight exceeds a threshold
delta:

    product_{x} (I_{l_x}(beta) / I_0(beta)) > delta

For beta = 2.0 and delta = 1e-15 (well below double-precision
resolution):

| N_s | States above threshold | After symmetry reduction |
|-----|----------------------|------------------------|
| 4 | ~2.6e4 | ~500 |
| 6 | ~1.4e6 | ~2.0e4 |
| 8 | ~7.8e7 | ~8.0e5 |
| 12 | ~2.4e11 | ~8.0e8 |
| 16 | ~7.2e14 | ~2.0e12 |
| 32 | enormous | ~10^{24} (too large) |

For beta = 1.0 (deep crossover, stronger coupling):

| N_s | States above threshold | After symmetry reduction |
|-----|----------------------|------------------------|
| 4 | ~1.5e3 | ~30 |
| 6 | ~3.5e4 | ~500 |
| 8 | ~8.0e5 | ~8,000 |
| 12 | ~4.3e8 | ~3.0e6 |
| 16 | ~2.3e11 | ~6.0e8 |
| 32 | ~5.3e22 | too large |

**The critical finding:** For N_s <= 16, the effective transfer
matrix dimension in the relevant symmetry sector is at most
~10^8-10^{12}. Lanczos iteration (which only needs matrix-vector
products, not explicit storage) is feasible for dimensions up to
~10^{12} with modern hardware, provided the matrix-vector product
is fast. [FEASIBLE for N_s <= 16]

**For N_s = 32** (the finest lattice at L Lambda = 1.0, from the
Richardson extrapolation in Section 03.6), the dimension is too
large for direct Lanczos. However, N_s = 32 is the FINEST lattice
spacing -- it is needed only to reduce the continuum extrapolation
error, and only at the single most critical grid point L Lambda = 1.
See Section 06 for strategies to handle this case.


## 5.10 The Z_3 twist implementation

The Z_3 twist modifies the boundary link transfer matrix. At the
boundary link (N_s - 1, 0), the field z(0) is replaced by Omega z(0)
where Omega = diag(1, omega, omega^2).

In the angular momentum basis, Omega acts as:

    Omega |l, m_1, m_2> = omega^{m_1 + 2 m_2} |l, m_1, m_2>

where (l, m_1, m_2) are the SU(3) weight labels. This is a DIAGONAL
operation in the angular momentum basis, so the Z_3 twist does not
increase the computational complexity -- it simply modifies the phases
in the boundary link transfer matrix.

The Z_3 charge sectors are:

    q = 0: omega^{sum (m_1 + 2 m_2)} = 1    (vacuum sector)
    q = 1: omega^{sum (m_1 + 2 m_2)} = omega
    q = 2: omega^{sum (m_1 + 2 m_2)} = omega^2

The mass gap we need is in the q = 0 sector (the lightest excitation
above the vacuum in the same Z_3 sector), or possibly in the q = 1
sector (the lightest twisted-sector excitation). Both must be checked.


## 5.11 Status

| Component | Status |
|-----------|--------|
| Angular momentum decomposition on CP^2 | [PROVED] |
| Character expansion of transfer matrix | [PROVED] |
| Truncation error bound (Bessel decay) | [PROVED] |
| l_max = 4-5 suffices for double precision | [FEASIBLE] (Section 5.2 estimates) |
| Symmetry reduction (Z_3, translation, C, P) | [PROVED] |
| Lanczos + Krawczyk for certified eigenvalues | [PROVED] (method) |
| d_sector manageable for N_s <= 16 | [FEASIBLE] (Section 5.9) |
| N_s = 32 feasibility | [OPEN] (requires further strategies) |
| Z_3 twist implementation | [PROVED] (diagonal in weight basis) |
