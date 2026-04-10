# 06. Feasibility: Matrix Sizes, Memory, Computation Time

## 6.1 The computational task, restated

From Sections 03 and 05, the full computer-assisted proof requires:

- 33 transfer matrix eigenvalue computations (13 grid points x 2-3
  lattice spacings each)
- Each computation: find the two largest eigenvalues of a symmetric
  positive matrix with certified error bounds
- Matrix dimensions range from ~30 (easiest case) to ~10^{12}
  (hardest case)

The computation breaks into three tiers by difficulty.


## 6.2 Tier 1: Small lattices (N_s = 4-8 at strong coupling)

These are the deep crossover grid points at the coarsest lattice
spacing (the "a_1" column in Section 03.6).

| Grid point | L Lambda | N_s | beta | d_sector | Method |
|-----------|----------|-----|------|----------|--------|
| 1 | 0.50 | 4 | 1.0 | ~30 | Direct |
| 2 | 0.75 | 6 | 1.3 | ~500 | Direct |
| 3 | 1.00 | 8 | 1.6 | ~8,000 | Direct |
| 4 | 1.25 | 8 | 1.8 | ~12,000 | Direct |
| 5 | 1.50 | 8 | 2.0 | ~8,000 | Direct |
| 6-7 | 1.75-2.00 | 8 | 2.2-2.5 | ~5,000 | Direct |
| 8-13 | 2.5-8.0 | 10-12 | 2.8-4.3 | ~10^5-10^6 | Lanczos |

**"Direct" means:** Construct the full matrix in memory, compute
ALL eigenvalues using symmetric eigenvalue routines (LAPACK dsyev
or equivalent), then apply Krawczyk verification for the top two.

**Resources for Tier 1 (direct diagonalization):**

Matrix dimension d = 10,000 (largest Tier 1 case):
- Matrix storage: d^2 * 8 bytes = 800 MB (double precision)
  With interval arithmetic (2x for endpoints): 1.6 GB
- LAPACK dsyev time: O(d^3) ~ 10^{12} flops ~ 100 seconds
  on a modern CPU (10 GFLOPS sustained for eigenvalue computation)
- With interval arithmetic overhead (3-5x): ~500 seconds ~ 8 min
- Krawczyk verification: ~10 matrix-vector products ~ seconds

**Total Tier 1 time: ~13 direct diagonalizations x 10 min average
= ~2 hours.** [FEASIBLE]

**Memory: peak ~2 GB.** Easily fits on any modern workstation.


## 6.3 Tier 2: Medium lattices (N_s = 8-16, moderate coupling)

These are the Richardson extrapolation points at the second lattice
spacing (a_2 = a_1/2, meaning N_s is doubled).

| Grid point | L Lambda | N_s | beta | d_sector | Method |
|-----------|----------|-----|------|----------|--------|
| 1' | 0.50 | 8 | 1.0 | ~8,000 | Direct |
| 2' | 0.75 | 12 | 1.3 | ~3e6 | Lanczos |
| 3' | 1.00 | 16 | 1.6 | ~6e8 | Lanczos |
| 4' | 1.25 | 16 | 1.8 | ~2e9 | Lanczos |
| 5' | 1.50 | 16 | 2.0 | ~6e8 | Lanczos |
| 6'-7' | 1.75-2.00 | 16 | 2.2-2.5 | ~2e8 | Lanczos |

**"Lanczos" means:** Do NOT store the full matrix. Use iterative
eigenvalue computation (Lanczos algorithm) with matrix-vector
products computed on the fly via the factored transfer matrix
(Section 05.6).

**Resources for Tier 2 (Lanczos iteration):**

Matrix dimension d = 10^8 (representative Tier 2 case):
- Vector storage: 100 Lanczos vectors x 10^8 x 16 bytes = 160 GB
  This exceeds typical RAM. **Must use out-of-core or reduced
  Lanczos with restart (implicitly restarted Lanczos, ARPACK-style).**
- With thick-restart Lanczos (store only 20 vectors): 32 GB.
  Fits in a high-end workstation (64-128 GB RAM).

Matrix-vector product cost (factored form, N_s links):
- Each link: sparse matrix-vector product on d_site^2 ~ 10^4
  nonzero entries, applied to a d_rest-dimensional vector.
- Total cost per T|v>: O(N_s * d_site^2 * d_sector) ~ 16 * 10^4 * 10^8
  = 1.6 x 10^{13} flops.
- Time per matrix-vector product: 1.6e13 / 10^{10} (10 GFLOPS)
  ~ 1600 seconds ~ 27 min.
- With interval arithmetic (5x): ~2.2 hours per matrix-vector product.

Lanczos convergence: ~50-100 iterations for the two largest
eigenvalues (the spectral gap is O(0.1) relative to the largest
eigenvalue, so convergence is rapid).

**Total per grid point: 100 iterations x 2.2 hours = 220 hours
~ 9 days (single core).**

With parallelization (the matrix-vector product is trivially
parallelizable across the site factorization):
- 8 cores: ~1.1 days per grid point
- 64 cores (cluster node): ~3.4 hours per grid point

**Total Tier 2: ~12 grid points x 1 day (8-core) = 12 days.**
[FEASIBLE on a workstation]

Krawczyk verification adds ~10 matrix-vector products = ~1 day
per grid point. **Total with verification: ~24 days on 8 cores.**


## 6.4 Tier 3: Large lattices (N_s = 32, for Richardson at L Lambda = 1)

This is the single hardest computation: the finest lattice spacing
at the most critical grid point.

| Grid point | L Lambda | N_s | beta | d_sector | Method |
|-----------|----------|-----|------|----------|--------|
| 3'' | 1.00 | 32 | 1.6 | ~10^{12} | Special |

d_sector ~ 10^{12} is BEYOND standard Lanczos capability:
- Vector storage: 10^{12} x 16 bytes = 16 TB (one vector!)
- Matrix-vector product: prohibitively expensive by direct methods

**Strategies to handle the N_s = 32 case:**

### Strategy A: Avoid N_s = 32 entirely

Use only two lattice spacings (N_s = 8 and N_s = 16) for the
Richardson extrapolation at L Lambda = 1. The continuum extrapolation
error is then O(a^4) rather than O(a^6):

    |m_Richardson - m_cont| <= C_4 a^4 Lambda^5

For a = L / 16 = 1/(16 Lambda):

    error ~ C_4 / 16^4 * Lambda ~ C_4 * 1.5e-5 * Lambda

If C_4 ~ 10 (a pessimistic estimate), the error is ~1.5e-4 Lambda.
This is well below the mass gap (~0.3-0.7 Lambda). **Two lattice
spacings likely suffice.** [FEASIBLE]

The risk: C_4 is not known rigorously. To make this a proof, we
need a RIGOROUS BOUND on C_4. This can be obtained from:

(a) Perturbative computation of the Symanzik coefficients for the
    CP^2 lattice action (the coefficients are known to 2-loop order
    in perturbation theory, and the non-perturbative corrections are
    exponentially small in 1/g^2 for the standard action).

(b) Comparison of the m_latt(a) values at a and a/2: if they agree
    to within delta, then the continuum value is within delta of the
    Richardson extrapolant (up to higher-order terms bounded by the
    ratio of successive corrections).

### Strategy B: Tensor network / DMRG

The transfer matrix T is a MATRIX PRODUCT OPERATOR (MPO) with bond
dimension d_site. The two largest eigenvalues of an MPO can be
computed using DMRG (Density Matrix Renormalization Group) in a time
that scales as:

    O(N_s * d_site^2 * chi^3)

where chi is the bond dimension of the matrix product state (MPS)
approximation to the eigenvector. For gapped systems (which this
is -- the mass gap is O(Lambda)), the required chi scales as:

    chi ~ exp(c * xi / a) ~ exp(c / (m * a))

For m a ~ 1/32 (the ratio m * a at N_s = 32), we get:

    chi ~ exp(c * 32) for some c > 0

This is exponentially large in N_s, suggesting DMRG does NOT help
for large N_s with small correlation length in lattice units.

**However:** DMRG can provide APPROXIMATE eigenvalues that serve as
starting points for a verification step. If the DMRG eigenvalues
are accurate enough, a local Krawczyk-type verification (using the
MPS structure to define a projected space) could certify them.

**Status:** This is a research-level idea. [OPEN]

### Strategy C: Multi-level Monte Carlo with variance reduction

Use stochastic methods (Monte Carlo evaluation of the trace of T^n)
with interval arithmetic to get probabilistic bounds that can be
promoted to rigorous bounds via concentration inequalities. This
approach was used by Hales in the Kepler conjecture proof.

**Status:** Applicable in principle, but the variance reduction
needed for O(1) relative precision on the spectral gap would require
O(1/gap^2) samples. For gap ~ 0.1, this is ~100 samples, each
involving the action of T^{N_t} -- equivalent to a full Lanczos
computation. No advantage over Lanczos. [NOT USEFUL]

### Strategy D: Accept two lattice spacings

The most practical approach: for the single point L Lambda = 1.0,
use only N_s = 8 and N_s = 16 for the Richardson extrapolation.
Bound the continuum extrapolation error using the rigorous Symanzik
bound (Section 02.6) with the COMPUTED lattice data:

    |m_cont - m_R| <= |m_latt(a) - m_latt(a/2)| * (a/L)^2 / (1 - (a/L)^2)

This is a POSTERIORI bound that uses the actual computed mass gap
values to estimate the continuum extrapolation error. It does not
require knowing C_4 a priori.

**Status:** [FEASIBLE] -- this is the recommended approach.


## 6.5 Total resource estimate

### Computation time (8-core workstation)

| Tier | Grid points | Time per point | Total |
|------|------------|---------------|-------|
| Tier 1 (direct) | 13 | 10 min | 2 hours |
| Tier 2 (Lanczos) | 12 | 2 days | 24 days |
| Krawczyk verif. | 12 | 1 day | 12 days |
| **Total** | | | **~38 days** |

### Computation time (64-core cluster node)

| Tier | Grid points | Time per point | Total |
|------|------------|---------------|-------|
| Tier 1 (direct) | 13 | 2 min | 30 min |
| Tier 2 (Lanczos) | 12 | 4 hours | 2 days |
| Krawczyk verif. | 12 | 2 hours | 1 day |
| **Total** | | | **~3 days** |

### Memory

| Tier | Peak memory |
|------|-------------|
| Tier 1 | 2 GB |
| Tier 2 | 32 GB (thick-restart Lanczos, 20 vectors) |

### Storage

- Lanczos vectors (checkpointing): ~500 GB for Tier 2
- Transfer matrix elements (precomputed): ~10 GB
- Total: ~500 GB (fits on one SSD)


## 6.6 Software development estimate

The computation requires custom software (no existing package
implements the CP^2 lattice transfer matrix with Z_3 twist in
interval arithmetic). The components:

| Component | Estimated effort | Dependencies |
|-----------|-----------------|-------------|
| CP^2 angular momentum basis | 2 weeks | Representation theory |
| Transfer matrix elements (character expansion) | 3 weeks | Arb library |
| Symmetry reduction (Z_3, translation, C, P) | 2 weeks | Group theory |
| Lanczos algorithm (interval arithmetic) | 2 weeks | Arb library |
| Krawczyk eigenvalue verification | 2 weeks | INTLAB or custom |
| Error budget computation | 1 week | Sections 02, 04 |
| Grid management and automation | 1 week | Scripting |
| Testing and validation | 3 weeks | Comparison with MC |
| **Total** | **~16 weeks (4 months)** | |

**Recommended language:** C with Arb library for the core computation,
Julia or Python for the driver scripts and error budget.


## 6.7 Comparison with existing computer-assisted proofs

| Proof | Matrix dimension | Precision | Time | Year |
|-------|-----------------|-----------|------|------|
| Hales (Kepler conjecture) | ~10^4 | double | months | 1998-2005 |
| Tucker (Lorenz attractor) | ~10^2 | extended | days | 2002 |
| Fefferman-Seco (atoms) | ~10^4 | arbitrary | weeks | 1990s |
| Plum (elliptic eigenvalues) | ~10^5 | double | days | 2005 |
| **This project** | **~10^8** | **double** | **weeks** | **2026?** |

Our project is at the upper end of existing computer-assisted proofs
in terms of matrix dimension but not qualitatively beyond what has
been done. The Kepler conjecture proof involved ~50,000 separate
linear programming verifications, comparable in total computation
to our ~33 eigenvalue certifications. [FEASIBLE]


## 6.8 Risk factors

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Interval widths blow up | Low | High | Increase precision (Arb) |
| Krawczyk fails to converge | Low | Medium | Use Lehmann-Goerisch instead |
| d_sector larger than estimated | Medium | High | Tighter importance truncation |
| Continuum extrap. error too large | Medium | Medium | Strategy D (Section 6.4) |
| Software bugs | Medium | High | Independent verification |
| Symmetry reduction error | Low | Fatal | Automated group theory checks |

The most serious risk is that the effective matrix dimension at
Tier 2 is larger than estimated in Section 05.9. The estimates
there used the Bessel-function decay to truncate insignificant
basis states, but the precise threshold depends on how the
truncation error propagates through the eigenvalue computation.
A factor-of-10 underestimate in d_sector would increase Tier 2
computation time from 24 days to 240 days (8-core), or from 3 days
to 30 days (64-core). Still feasible, but pushing the boundaries.


## 6.9 The minimal viable computation

If resources are limited, the MINIMUM computation that constitutes
a proof is:

1. **Single lattice spacing** at each of 13 grid points (no
   Richardson extrapolation). This gives a mass gap bound with
   O(a^2) systematic error.

2. Choose the lattice spacing small enough that a^2 Lambda^2 << 1.
   With N_s = 8 and L Lambda = 1, a Lambda = 1/8, so
   a^2 Lambda^2 = 1/64 ~ 0.016. The systematic error is ~2% of
   the mass gap.

3. The continuum extrapolation error is bounded by the Symanzik
   formula:
       |m_latt - m_cont| <= D a^2 / xi^3 = D a^2 m^3
   For m ~ Lambda and a = 1/(8 Lambda):
       error <= D / (512 Lambda^2) * Lambda^3 = D Lambda / 512
   With D ~ 10: error ~ 0.02 Lambda.

4. Since m ~ 0.3-1.0 Lambda, a 2% systematic error still allows
   proving m > 0 (we need m_lower > 0, not m_lower > 0.9 Lambda).

**Minimal computation: 13 Tier 1 diagonalizations. Time: 2 hours.**

This would prove the mass gap with ~2% relative precision on the
lower bound -- more than sufficient for a qualitative "m > 0"
statement. The continuum limit extrapolation is needed only if
the systematic error term is not rigorously bounded.

**Issue with the minimal approach:** We need a RIGOROUS bound on
the Symanzik coefficient D, not just a perturbative estimate.
This is available in the literature for the CP^1 model (O(3) sigma
model) but may need to be derived for CP^2. [OPEN]


## 6.10 Summary

| Question | Answer |
|----------|--------|
| Is the computation feasible? | **Yes**, for Tiers 1-2. |
| Total computation time (8-core)? | ~38 days |
| Total computation time (64-core)? | ~3 days |
| Peak memory? | ~32 GB |
| Software development time? | ~4 months |
| Is N_s = 32 feasible? | No, but not needed (Strategy D) |
| Minimal viable computation? | 2 hours (single lattice spacing) |
| Overall feasibility | [FEASIBLE] |
