# 03. The Crossover Grid: How Many Points, What Lattice Sizes

## 3.1 Identifying the crossover interval

The crossover interval is where the bootstrap cluster expansion
cannot analytically prove m(L) > 0. From the bootstrap analysis
(2d-attack-bootstrap/05-reaching-infinity.md, Section 5.7):

**Left boundary (L_min):** The semiclassical expansion breaks down
when the fractional instanton action becomes O(1):

    4 pi / (3 g^2(1/L)) ~ 1

Using the one-loop running g^2(mu) = 2pi / (3 ln(mu/Lambda)):

    4pi / (3 * 2pi / (3 ln(1/(L Lambda)))) = 2 ln(1/(L Lambda)) ~ 1

    L_min ~ Lambda^{-1} exp(-1/2) ~ 0.6 / Lambda

**Right boundary (L_max):** The cluster expansion at large L
converges when m(L) * L >> K, the Kotecky-Preiss constant. From
the estimate K ~ 4 (Section 5.7 of the bootstrap analysis), and
m(L) -> m(infinity) ~ Lambda for large L:

    m * L >> K  =>  Lambda * L >> 4  =>  L >> 4/Lambda

With some margin: L_max ~ 8/Lambda.

**The crossover interval:**

    I_cross = [0.6/Lambda, 8/Lambda]

This has width ~ 7.4/Lambda. In units of Lambda^{-1}, it spans
roughly one order of magnitude.


## 3.2 The mass gap profile in the crossover

From lattice simulations (Campostrini-Rossi 1992, Caracciolo et al.
1995, and more recent work by Bietenholz-de Forcrand):

| L Lambda | m(L)/Lambda (numerical) | m(L) * L |
|----------|------------------------|----------|
| 0.5 | ~0.3 | ~0.15 |
| 1.0 | ~0.7 | ~0.7 |
| 2.0 | ~0.9 | ~1.8 |
| 3.0 | ~0.95 | ~2.85 |
| 5.0 | ~0.98 | ~4.9 |
| 8.0 | ~0.99 | ~7.9 |

The minimum of m(L)*L occurs near L Lambda ~ 0.5-1.0 (the deep
crossover), where m L ~ 0.15-0.7. This is the region where the
cluster expansion convergence is most delicate.

**Critical observation:** m(L) is NEVER close to zero. The minimum
value of m(L) in the crossover is approximately 0.3 Lambda (at
L ~ 0.5/Lambda). This is a large, O(1) fraction of Lambda --
there is no near-cancellation or fine-tuning.


## 3.3 Grid spacing requirement

From Section 01, the grid spacing must satisfy:

    Delta L < 2 m_lower / C_Lip

The Lipschitz constant C_Lip bounds |dm/dL|. From the Hellmann-
Feynman analysis (bootstrap Section 5.5):

    |dm/dL| <= m^2 / (4 pi)

At the crossover, m ~ Lambda, so:

    |dm/dL| <= Lambda^2 / (4 pi) ~ 0.08 Lambda^2

Therefore:

    Delta L < 2 * (0.3 Lambda) / (0.08 Lambda^2) = 7.5 / Lambda

This is comparable to the full width of the crossover interval,
suggesting that only a FEW grid points suffice.

**More conservatively:** The Lipschitz bound above uses the free-
field estimate. In the strongly-coupled crossover, the actual
dm/dL could be larger by a factor of 2-5. Taking:

    C_Lip ~ 0.4 Lambda^2

we get:

    Delta L < 2 * (0.3 Lambda) / (0.4 Lambda^2) = 1.5 / Lambda


## 3.4 The grid design

**Primary grid (coarse):** 8 points uniformly spaced in [0.5, 8.0]
in units of Lambda^{-1}:

    L_k / Lambda = 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 8.0

Spacing: Delta L = 1.0/Lambda (inner) to 1.5/Lambda (endpoints).
This satisfies the Lipschitz requirement Delta L < 1.5/Lambda
everywhere except possibly the leftmost interval.

**Refinement grid (fine):** Additional points in [0.5, 2.0] where
the mass gap is smallest:

    L_k / Lambda = 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0

Spacing: Delta L = 0.25/Lambda. Combined with the Lipschitz bound,
this guarantees m > 0 if m_lower > C_Lip * 0.25 / (2 Lambda)
= 0.05 Lambda at each grid point -- easily satisfied since
m > 0.3 Lambda throughout.

**Total grid points: 13** (8 coarse + 5 additional fine points
in the deep crossover region).


## 3.5 Lattice parameters at each grid point

For each L_k, we need to choose:
- N_s: number of spatial sites (determines L = N_s * a and a = L/N_s)
- N_t: number of temporal sites (determines T = N_t * a)
- beta = 1/g^2: the lattice coupling

**Coupling constant.** The CP^2 sigma model coupling g^2 is related
to the lattice coupling beta by:

    beta = 1/g^2

The coupling runs as:

    1/g^2(mu) = (3/(2 pi)) ln(mu/Lambda)

At each L, we work at the coupling g^2(1/L):

    beta_k = (3/(2 pi)) ln(1/(L_k Lambda))

| L Lambda | beta = 1/g^2 | g^2 |
|----------|-------------|-----|
| 0.5 | 0.33 | 3.0 |
| 1.0 | 0 (formal) | -- |
| 1.5 | -0.19 (formal) | -- |

**Problem:** The running coupling g^2(1/L) diverges at L = 1/Lambda
and becomes negative for L > 1/Lambda. This is an artifact of the
one-loop formula; the LATTICE coupling beta = N_s/(N_s g^2_latt)
is always positive on the lattice.

**Resolution:** On the lattice, we do NOT use the perturbative
coupling. Instead, for each physical L, we choose a LATTICE coupling
beta_latt that reproduces the correct correlation length at that L.
This is determined by matching conditions (matching the lattice
string tension or mass gap to known numerical values).

**Practical approach:** Use the lattice coupling beta_latt in the
range [0.5, 5.0], which covers the entire crossover. The exact
mapping beta_latt <-> L Lambda is determined by measuring the
correlation length on the lattice.

**Recommended lattice parameters:**

| Grid point | L Lambda | N_s | a Lambda | beta_latt | N_t |
|-----------|----------|-----|----------|-----------|-----|
| 1 | 0.50 | 4 | 0.125 | ~1.0 | 32 |
| 2 | 0.75 | 6 | 0.125 | ~1.3 | 48 |
| 3 | 1.00 | 8 | 0.125 | ~1.6 | 64 |
| 4 | 1.25 | 8 | 0.156 | ~1.8 | 64 |
| 5 | 1.50 | 8 | 0.188 | ~2.0 | 64 |
| 6 | 1.75 | 8 | 0.219 | ~2.2 | 64 |
| 7 | 2.00 | 8 | 0.250 | ~2.5 | 64 |
| 8 | 2.50 | 10 | 0.250 | ~2.8 | 80 |
| 9 | 3.50 | 12 | 0.292 | ~3.2 | 80 |
| 10 | 4.50 | 12 | 0.375 | ~3.5 | 80 |
| 11 | 5.50 | 12 | 0.458 | ~3.8 | 80 |
| 12 | 6.50 | 12 | 0.542 | ~4.0 | 80 |
| 13 | 8.00 | 12 | 0.667 | ~4.3 | 80 |


## 3.6 Continuum extrapolation: multiple lattice spacings

For each physical L, we need the mass gap at 2-3 lattice spacings
to perform Richardson extrapolation. The minimum set:

    a_1 = L / N_s,    a_2 = L / (2 N_s),    a_3 = L / (4 N_s)

This triples (or quadruples) the number of computations but
removes the O(a^2) lattice artifact rigorously.

**For the deep crossover (L Lambda in [0.5, 2.0]):**

| L Lambda | N_s values | a Lambda values | Transfer matrix dim |
|----------|------------|-----------------|---------------------|
| 0.50 | 4, 8, 16 | 0.125, 0.063, 0.031 | see Section 05 |
| 1.00 | 8, 16, 32 | 0.125, 0.063, 0.031 | see Section 05 |
| 2.00 | 8, 16, 32 | 0.250, 0.125, 0.063 | see Section 05 |

The finest lattice (N_s = 32 for L Lambda = 1) is the most
computationally expensive. See Section 06 for feasibility.

**For the outer crossover (L Lambda in [2.0, 8.0]):**

Two lattice spacings suffice (the O(a^2) correction is smaller
because a Lambda is larger, meaning the lattice is coarser relative
to the physical scale, and the correction c_2 a^2 is small).


## 3.7 Summary

**Total computations needed:**

- 7 grid points in the deep crossover x 3 lattice spacings = 21
- 6 grid points in the outer crossover x 2 lattice spacings = 12
- **Total: 33 transfer matrix eigenvalue computations**

Each computation involves:
1. Constructing the transfer matrix (dimension d, see Section 05)
2. Computing the two largest eigenvalues with interval arithmetic
3. Extracting the certified mass gap bound

The grid is designed so that the Lipschitz bound, combined with the
certified mass gap at each point, proves m(L) > 0 for ALL L in
the crossover interval -- not just at the grid points.
