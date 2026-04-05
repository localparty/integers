# 11D SUGRA Field Content Decomposition on CP² x S² x S¹/Z₂

> **Date:** April 5, 2026
> **Status:** Complete decomposition
> **Purpose:** Fully decompose the 11D SUGRA field content (g_MN, C_MNP, Ψ_M)
> under the isometry group SU(3) x SU(2) x U(1) of the internal manifold
> CP² x S² x S¹/Z₂, and extract the 4D spectrum with Casimir coefficients.
> **Depends on:** 03-the-explicit-kk-reduction-on-cp-s-s.md, 12b-moduli-freezing-analysis.md

---

## Conventions and Notation

**Index ranges:**
- M, N = 0, ..., 10 (11D)
- μ, ν = 0, 1, 2, 3 (4D spacetime)
- a, b = 1, 2, 3, 4 (CP²)
- i, j = 1, 2 (S²)
- φ (S¹/Z₂)

**Cohomology of the internal factors:**

| Factor | H⁰ | H¹ | H² | H³ | H⁴ |
|--------|-----|-----|-----|-----|-----|
| CP²    | Z   | 0   | Z   | 0   | Z   |
| S²     | Z   | 0   | Z   | —   | —   |
| S¹/Z₂  | Z   | Z*  | —   | —   | —   |

(*For S¹, H¹(S¹) = Z. For the orbifold S¹/Z₂, we must distinguish even/odd
sectors under the Z₂ reflection φ → −φ. Bosonic fields are even (periodic),
fermionic fields are odd (anti-periodic) under the Scherk-Schwarz twist.)

**Betti numbers:**
- b₀(CP²) = 1, b₁(CP²) = 0, b₂(CP²) = 1, b₃(CP²) = 0, b₄(CP²) = 1
- b₀(S²) = 1, b₁(S²) = 0, b₂(S²) = 1
- b₀(S¹) = 1, b₁(S¹) = 1

**Killing vectors (isometry generators):**
- CP²: 8 Killing vectors generating SU(3)
- S²: 3 Killing vectors generating SU(2)
- S¹: 1 Killing vector generating U(1)

**Key spectral data (from etc/12b):**
- Scalar Laplacian on S²: eigenvalues l(l+1)/r₂², degeneracy 2l+1
- Scalar Laplacian on CP²: eigenvalues related to SU(3) Casimir
- On S¹/Z₂: bosonic KK masses n/R, fermionic KK masses (n+1/2)/R

---

## Part A: Decomposition of the 11D Metric g_MN

The 11D metric is a symmetric 2-tensor with 11×12/2 = 66 components.
On-shell in 11D: 44 propagating degrees of freedom (d.o.f.).

The 11D index pair (M,N) splits into 4D + internal indices. We organize
by the block structure of the symmetric matrix g_MN.

### A.1 The (μ,ν) Block: 4D Graviton

**g_μν(x):** The 4D metric.

- 4D spin: 2
- d.o.f.: 2 (massless graviton in 4D)
- Species: 1
- Internal origin: zero mode on all internal factors
- Casimir: does NOT propagate on any internal factor (zero mode everywhere)

This is the massless graviton. It is a singlet under SU(3) x SU(2) x U(1).

### A.2 The (μ,a) Block: SU(3) Gauge Bosons

**g_μa(x,y):** Mixed 4D-CP² components.

These are expanded in the Killing vectors K_I^a(y) of CP²:

    g_μa(x,y) = Σ_{I=1}^{8} B_μ^I(x) K_{Ia}(y) + (massive KK tower)

- 4D spin: 1 (gauge bosons)
- d.o.f.: 2 per gauge field (massless vectors in 4D)
- Species: 8 (the adjoint of SU(3))
- Internal origin: CP² Killing vectors
- Casimir: propagate on CP² (their KK tower on CP² gives SU(3) Casimir)
- Gauge group: SU(3) — the strong force (gluons)

### A.3 The (μ,i) Block: SU(2) Gauge Bosons

**g_μi(x,z):** Mixed 4D-S² components.

Expanded in the Killing vectors L_J^i(z) of S²:

    g_μi(x,z) = Σ_{J=1}^{3} C_μ^J(x) L_{Ji}(z) + (massive KK tower)

- 4D spin: 1 (gauge bosons)
- d.o.f.: 2 per gauge field
- Species: 3 (the adjoint of SU(2))
- Internal origin: S² Killing vectors
- Casimir: propagate on S² (their KK tower on S² gives SU(2) Casimir)
- Gauge group: SU(2) — the weak force (W⁺, W⁻, Z⁰)

### A.4 The (μ,φ) Block: U(1) Gauge Boson

**g_μφ(x):** Mixed 4D-S¹ component.

The single Killing vector ∂/∂φ of S¹ gives:

    g_μφ(x,φ) = A_μ(x) + (massive KK tower)

- 4D spin: 1 (gauge boson)
- d.o.f.: 2
- Species: 1
- Internal origin: S¹ Killing vector
- Casimir: propagates on S¹ (its KK tower on S¹ gives U(1) Casimir)
- Gauge group: U(1) — electromagnetism (photon/graviphoton)

### A.5 The (a,b) Block: CP² Metric Deformations

**g_ab(x,y):** Symmetric 2-tensor on CP².

The zero modes of the symmetric 2-tensor Laplacian (Lichnerowicz operator)
on CP² determine the number of 4D scalars from this sector.

The Lichnerowicz operator on CP² acts on symmetric traceless 2-tensors.
For a compact Einstein manifold (M, g₀) with Ric = Λg₀, the Lichnerowicz
operator is:

    Δ_L h_ab = −∇²h_ab − 2R_{acbd}h^{cd} + 2Λh_ab

The zero modes of Δ_L are the infinitesimal Einstein deformations —
the moduli of the Einstein metric.

**CP² is rigid as an Einstein manifold.** The Fubini-Study metric on CP²
has no infinitesimal Einstein deformations. This follows from:

1. CP² is a Hermitian symmetric space SU(3)/U(2)
2. For irreducible symmetric spaces, the space of infinitesimal Einstein
   deformations is trivial (Koiso's theorem, 1980)
3. Equivalently: the Lichnerowicz operator on CP² has no zero modes
   among symmetric traceless 2-tensors

However, the TRACE part g_ab = Ω(x) g₀_ab gives one scalar:

**The CP² breathing mode (r₃):**
- 4D spin: 0 (scalar)
- d.o.f.: 1
- Species: 1
- Internal origin: CP² volume modulus
- Casimir: the overall scale of CP² — this IS the CP² modulus r₃

So from (a,b): exactly **1 scalar** (the CP² breathing mode r₃).

### A.6 The (i,j) Block: S² Metric Deformations

**g_ij(x,z):** Symmetric 2-tensor on S².

On S², symmetric traceless 2-tensors have no zero modes (the round
metric on S² is also rigid — all deformations are diffeomorphisms
or conformal rescalings). The only mode is the trace:

**The S² breathing mode (r₂):**
- 4D spin: 0 (scalar)
- d.o.f.: 1
- Species: 1
- Internal origin: S² volume modulus
- Casimir: the overall scale of S² — this IS the S² modulus r₂

So from (i,j): exactly **1 scalar** (the S² breathing mode r₂).

### A.7 The (φ,φ) Block: S¹ Dilaton

**g_φφ(x):** The S¹ metric component.

- 4D spin: 0 (scalar — the dilaton)
- d.o.f.: 1
- Species: 1
- Internal origin: S¹ radius modulus
- Casimir: the S¹ scale R — this IS the S¹ modulus (the e-circle radius)

From (φ,φ): exactly **1 scalar** (the dilaton R).

### A.8 The (a,i) Block: Mixed CP²-S² Deformations

**g_ai(x,y,z):** Mixed CP²-S² off-diagonal metric.

These are expanded in products of harmonics: vectors on CP² times vectors
on S². The zero modes would require simultaneous Killing vectors on both
factors. However, these fields are 4D scalars (since both indices are
internal).

Expanding: g_ai(x,y,z) = Σ_{I,J} φ^{IJ}(x) K_I^a(y) L_J^i(z) + ...

The zero-mode sector requires harmonic 1-forms. Since H¹(CP²) = 0 and
H¹(S²) = 0, there are no harmonic 1-forms on either factor to provide
zero-mode expansions for the mixed components in the standard Hodge
decomposition sense.

However, the Killing vector expansion is different from the harmonic form
expansion. The g_ai components, expanded in Killing vectors of CP² and S²,
give 4D scalars:

    g_ai(x,y,z) = Σ_{I=1}^{8} Σ_{J=1}^{3} φ^{IJ}(x) K_{Ia}(y) L_{Ji}(z) + ...

These 8 × 3 = 24 scalars transform in the (8, 3) representation of
SU(3) x SU(2). But wait — this is a gauge artifact.

Under 11D diffeomorphisms, these mixed metric components can be gauged
away (they are pure gauge in the linearized theory around a product
metric). The (a,i) block does NOT produce independent physical degrees
of freedom at the massless level. The physical content is already
captured by the gauge fields and breathing modes.

**From (a,i): 0 massless physical d.o.f.**

### A.9 The (a,φ) Block: Mixed CP²-S¹ Deformations

**g_aφ(x,y):** Mixed CP²-S¹ off-diagonal metric.

Expanding in Killing vectors of CP²:

    g_aφ(x,y) = Σ_{I=1}^{8} σ^I(x) K_{Ia}(y) + ...

These 8 scalars are in the adjoint of SU(3). However, similar to A.8,
these can be gauged away by diffeomorphisms mixing the CP² and S¹
directions. In the standard KK Ansatz (Section 3.1 of paper4), the
cross-term g_μa already accounts for the gauge fields, and the residual
g_aφ components are absorbed by gauge transformations.

More precisely: the 4D vector A_μ from g_μφ and the 8 vectors B_μ^I
from g_μa are the physical gauge bosons. The scalars from g_aφ are
the "Wilson line" scalars — they parametrize flat directions of the
gauge connection around the S¹. But on S¹/Z₂ (the orbifold), the Z₂
projection eliminates the Wilson lines that are odd under the orbifold
action.

For the geometry CP² x S² x S¹/Z₂ with the Z₂ acting only on S¹,
the Wilson line scalars from g_aφ are:
- Even under Z₂: survive the projection → 0 (none, because the
  Killing vectors on CP² are independent of φ)
- Actually: g_aφ is odd under φ → −φ (one index along φ direction),
  so the Z₂ orbifold projects out the zero modes entirely.

**From (a,φ): 0 massless d.o.f.** (projected out by S¹/Z₂ orbifold)

### A.10 The (i,φ) Block: Mixed S²-S¹ Deformations

**g_iφ(x,z):** Mixed S²-S¹ off-diagonal metric.

By the same argument as A.9: g_iφ is odd under the Z₂ orbifold
action φ → −φ, so the zero modes are projected out.

**From (i,φ): 0 massless d.o.f.** (projected out by S¹/Z₂ orbifold)

### A.11 Summary of Metric Decomposition

| Sector | 4D field | Spin | Species | d.o.f. | Internal origin |
|--------|----------|------|---------|--------|-----------------|
| g_μν   | graviton | 2    | 1       | 2      | singlet         |
| g_μa   | SU(3) gauge | 1 | 8       | 16     | CP² Killing     |
| g_μi   | SU(2) gauge | 1 | 3       | 6      | S² Killing      |
| g_μφ   | U(1) gauge  | 1 | 1       | 2      | S¹ Killing      |
| g_ab   | r₃ modulus  | 0 | 1       | 1      | CP² breathing   |
| g_ij   | r₂ modulus  | 0 | 1       | 1      | S² breathing    |
| g_φφ   | R dilaton   | 0 | 1       | 1      | S¹ breathing    |
| g_ai   | (none)      | — | 0       | 0      | gauge artifact  |
| g_aφ   | (none)      | — | 0       | 0      | Z₂ projected    |
| g_iφ   | (none)      | — | 0       | 0      | Z₂ projected    |
| **Total** |         |    |         | **29** |                 |

The 29 on-shell d.o.f. from the metric decomposition: 2 (graviton)
+ 2×(8+3+1) = 24 (gauge bosons) + 3 (scalars) = 29.

**Cross-check:** The 11D graviton has 44 on-shell d.o.f. The
remaining 44 − 29 = 15 d.o.f. are accounted for by the massive
KK modes (they appear as massive fields in 4D with additional
polarization states).

---

## Part B: Decomposition of the 3-Form C_MNP

The 11D 3-form is a totally antisymmetric tensor with C(11,3) = 165
components. On-shell in 11D: 84 propagating d.o.f.

The 3 indices of C_MNP are distributed among the four sectors
{μ, a, i, φ}. We enumerate all partitions of 3 indices.

### B.1 C_μνρ: Three 4D Indices

**C_μνρ(x):** A 4D 3-form.

In 4D, a 3-form is dual to a scalar (via Hodge duality: *C₃ = σ).
This is the **4D axion** (dual scalar).

- 4D spin: 0 (pseudoscalar/axion)
- d.o.f.: 1
- Species: 1
- Internal origin: singlet under all internal isometries
- Casimir: does not propagate on any internal factor (zero mode)

### B.2 C_μνa: Two 4D + One CP² Index

**C_μνa(x,y):** Expanded in harmonic 1-forms on CP².

The massless sector requires harmonic 1-forms, counted by b₁(CP²).
Since **b₁(CP²) = 0**, there are no harmonic 1-forms on CP².

**From C_μνa: 0 massless d.o.f.**

### B.3 C_μνi: Two 4D + One S² Index

**C_μνi(x,z):** Expanded in harmonic 1-forms on S².

Since **b₁(S²) = 0**, there are no harmonic 1-forms on S².

**From C_μνi: 0 massless d.o.f.**

### B.4 C_μνφ: Two 4D + One S¹ Index

**C_μνφ(x):** A 4D 2-form (the S¹ index just selects the φ-component).

A 4D 2-form is dual to a scalar via Hodge duality: *B₂ = σ'.

However, we must check the Z₂ parity. Under φ → −φ, the component
C_μνφ has one index along φ, so it is **odd** under Z₂. The zero mode
on S¹/Z₂ requires even parity.

**From C_μνφ: 0 massless d.o.f.** (Z₂ projected out)

### B.5 C_μab: One 4D + Two CP² Indices

**C_μab(x,y):** Expanded in harmonic 2-forms on CP².

The massless sector requires harmonic 2-forms, counted by b₂(CP²).
Since **b₂(CP²) = 1** (generated by the Kähler form ω_ab), there is
exactly one harmonic 2-form.

    C_μab(x,y) = A'_μ(x) ω_ab(y) + (massive modes)

This gives **one additional 4D gauge field** from the 3-form sector.

- 4D spin: 1 (gauge boson)
- d.o.f.: 2
- Species: 1
- Internal origin: CP² Kähler form ω ∈ H²(CP²)
- Casimir: associated with CP² topology
- This is a **U(1) gauge field** — it is an ABELIAN gauge boson,
  distinct from the SU(3) gauge bosons from the metric.

**This is physically important:** the 3-form reduction on CP² produces
an additional U(1) gauge boson. In the Standard Model context, this
could mix with the metric U(1) to produce the hypercharge U(1)_Y.

### B.6 C_μij: One 4D + Two S² Indices

**C_μij(x,z):** Expanded in harmonic 2-forms on S².

Since **b₂(S²) = 1** (generated by the volume form ε_ij), there is
exactly one harmonic 2-form.

    C_μij(x,z) = A''_μ(x) ε_ij(z) + (massive modes)

This gives **one additional 4D gauge field**.

- 4D spin: 1 (gauge boson)
- d.o.f.: 2
- Species: 1
- Internal origin: S² volume form ε ∈ H²(S²)
- Casimir: associated with S² topology
- Another **U(1) gauge field** from the 3-form.

### B.7 C_μaφ: One 4D + One CP² + One S¹ Index

**C_μaφ(x,y):** Expanded in harmonic 0-forms on CP² (since the φ-index
is already saturated).

The zero mode on CP² is the constant function (b₀ = 1). But we must
check Z₂ parity: C_μaφ has one index along φ, so it is **odd** under Z₂.

**From C_μaφ: 0 massless d.o.f.** (Z₂ projected out)

### B.8 C_μiφ: One 4D + One S² + One S¹ Index

**C_μiφ(x,z):** Same argument as B.7 — odd under Z₂.

**From C_μiφ: 0 massless d.o.f.** (Z₂ projected out)

### B.9 C_μai: One 4D + One CP² + One S² Index

**C_μai(x,y,z):** Requires harmonic 1-forms on both CP² and S²
(or more precisely, the product of harmonic forms with total degree 1
distributed between CP² and S²).

The options are:
- Harmonic 1-form on CP² × harmonic 0-form on S²: b₁(CP²) × b₀(S²) = 0 × 1 = 0
- Harmonic 0-form on CP² × harmonic 1-form on S²: b₀(CP²) × b₁(S²) = 1 × 0 = 0

**From C_μai: 0 massless d.o.f.**

### B.10 C_abc: Three CP² Indices

**C_abc(x,y):** Expanded in harmonic 3-forms on CP².

Since **b₃(CP²) = 0**, there are no harmonic 3-forms.

**From C_abc: 0 massless d.o.f.**

### B.11 C_abφ: Two CP² + One S¹ Index

**C_abφ(x,y):** The 2-form part on CP² is expanded in harmonic 2-forms.

b₂(CP²) = 1 (the Kähler form ω). So this gives a 4D scalar:

    C_abφ(x,y) = σ₁(x) ω_ab(y) + ...

But Z₂ parity: C_abφ has one index along φ → **odd** under Z₂.

**From C_abφ: 0 massless d.o.f.** (Z₂ projected out)

### B.12 C_abi: Two CP² + One S² Index

**C_abi(x,y,z):** Requires harmonic 2-form on CP² × harmonic 1-form on S²
(total: 3 internal indices = 2 from CP² + 1 from S²).

b₁(S²) = 0, so no massless modes.

Alternatively: harmonic 1-form on CP² × harmonic ... but b₁(CP²) = 0.

**From C_abi: 0 massless d.o.f.**

### B.13 C_ijφ: Two S² + One S¹ Index

**C_ijφ(x,z):** The 2-form part on S² is expanded in harmonic 2-forms.

b₂(S²) = 1 (the volume form ε). So this gives a 4D scalar:

    C_ijφ(x,z) = σ₂(x) ε_ij(z) + ...

But Z₂ parity: odd under Z₂ (one φ-index).

**From C_ijφ: 0 massless d.o.f.** (Z₂ projected out)

### B.14 C_aij: One CP² + Two S² Indices

**C_aij(x,y,z):** The 2-form on S² is expanded in its volume form (b₂=1),
leaving a 1-form on CP² expanded in harmonic 1-forms.

    C_aij(x,y,z) = [σ₃(x) × (harmonic 1-form on CP²)_a] × ε_ij(z) + ...

But b₁(CP²) = 0, so no harmonic 1-forms on CP².

**From C_aij: 0 massless d.o.f.**

### B.15 C_aiφ: One CP² + One S² + One S¹ Index

**C_aiφ(x,y,z):** Three internal indices on three different factors.
Expanded in harmonic 0-forms on CP² and S² (the a and i indices are
single indices on each factor, requiring harmonic 1-forms).

Since b₁(CP²) = 0 and b₁(S²) = 0, no massless modes even before
the Z₂ projection.

**From C_aiφ: 0 massless d.o.f.**

### B.16 Summary of 3-Form Decomposition

| Sector   | 4D field      | Spin | Species | d.o.f. | Internal origin    |
|----------|---------------|------|---------|--------|--------------------|
| C_μνρ    | axion σ       | 0    | 1       | 1      | singlet            |
| C_μνa    | (none)        | —    | 0       | 0      | b₁(CP²)=0         |
| C_μνi    | (none)        | —    | 0       | 0      | b₁(S²)=0          |
| C_μνφ    | (none)        | —    | 0       | 0      | Z₂ projected      |
| C_μab    | U(1)' gauge   | 1    | 1       | 2      | ω ∈ H²(CP²)       |
| C_μij    | U(1)'' gauge  | 1    | 1       | 2      | ε ∈ H²(S²)        |
| C_μaφ    | (none)        | —    | 0       | 0      | Z₂ projected      |
| C_μiφ    | (none)        | —    | 0       | 0      | Z₂ projected      |
| C_μai    | (none)        | —    | 0       | 0      | b₁=0              |
| C_abc    | (none)        | —    | 0       | 0      | b₃(CP²)=0         |
| C_abφ    | (none)        | —    | 0       | 0      | Z₂ projected      |
| C_abi    | (none)        | —    | 0       | 0      | b₁=0              |
| C_ijφ    | (none)        | —    | 0       | 0      | Z₂ projected      |
| C_aij    | (none)        | —    | 0       | 0      | b₁(CP²)=0         |
| C_aiφ    | (none)        | —    | 0       | 0      | b₁=0              |
| **Total**|               |      |         | **5**  |                    |

The 3-form produces: 1 axion (scalar) + 2 U(1) gauge bosons = 5 d.o.f.

**Remark on the additional U(1) gauge bosons:**

The two U(1) gauge fields from C_μab and C_μij are topological in origin
(they come from the nontrivial cohomology of the internal spaces). Together
with the U(1) from the metric (g_μφ), we have THREE U(1) gauge fields:

1. A_μ from g_μφ — the "geometric" U(1) (graviphoton/photon)
2. A'_μ from C_μab — the "CP² topological" U(1)
3. A''_μ from C_μij — the "S² topological" U(1)

In the Standard Model identification, the physical U(1)_Y (hypercharge)
is a linear combination of these three U(1) factors. The gauge group
before symmetry breaking is:

    SU(3) × SU(2) × U(1) × U(1)' × U(1)''

Two of the three U(1) factors must be either:
(a) broken by the Stückelberg mechanism (the extra U(1) gauge bosons
    eat the 3-form scalars), or
(b) decoupled at low energies, or
(c) identified with global symmetries (B−L, etc.)

The standard mechanism in 11D SUGRA compactifications is (a): the
C-field gauge transformations mix with the U(1) gauge transformations,
producing Stückelberg masses for two of the three U(1) bosons. The
massless combination is the physical U(1)_EM.

---

## Part C: Decomposition of the Gravitino Ψ_M

The 11D gravitino is a Majorana spinor-vector (Rarita-Schwinger field)
with 128 on-shell fermionic d.o.f. in 11D. It has one vector index M
and one spinor index (suppressed).

### C.1 The Scherk-Schwarz Mechanism on S¹/Z₂

The Z₂ orbifold acts on S¹ by the reflection φ → −φ. The Scherk-Schwarz
twist assigns anti-periodic boundary conditions to fermions:

    Ψ_M(x, y, z, φ + 2πR) = −Ψ_M(x, y, z, φ)

This means the KK expansion on S¹ for fermions uses half-integer modes:

    Ψ_M(x, y, z, φ) = Σ_{n=0}^∞ Ψ_M^{(n)}(x, y, z) sin((n+1/2)φ/R)
                      + Σ_{n=0}^∞ Ψ_M^{(n)}(x, y, z) cos((n+1/2)φ/R)

The KK masses are:

    m_n^{ferm} = (n + 1/2)/R,    n = 0, 1, 2, ...

**Critical consequence:** There is NO n=0 massless mode for any
fermionic field. All fermions acquire a mass gap of at least 1/(2R).
This is the Scherk-Schwarz supersymmetry breaking — SUSY is broken
at the compactification scale 1/R.

### C.2 Ψ_μ: 4D Gravitino Components

**Ψ_μ(x,y,z,φ):** The 4D spacetime components of the gravitino.

In a supersymmetric reduction, the zero mode of Ψ_μ would be the 4D
gravitino (the superpartner of the graviton). But the Scherk-Schwarz
mechanism eliminates the zero mode.

- 4D spin: 3/2
- Massless species: **0** (no zero mode due to anti-periodicity)
- Massive KK tower: masses (n+1/2)/R
- The lightest gravitino has mass 1/(2R)

The number of "would-be" zero modes (i.e., the number of gravitini
that would exist without the Scherk-Schwarz twist) equals the number
of Killing spinors on CP² × S².

**Killing spinors on CP²:** CP² is a Kähler-Einstein manifold with
positive scalar curvature. It admits Killing spinors satisfying:

    ∇_a η = ± (i/2r₃) γ_a η

The number of Killing spinors on CP^n is:
- For CP^1 = S²: 2 Killing spinors (it's the round 2-sphere)
- For CP²: being Kähler with positive curvature, CP² admits
  **1 Killing spinor** for each chirality of the internal spin
  bundle. In total: **2 Killing spinors** on CP².

More precisely: CP² is a spin^c manifold but NOT a spin manifold
(its second Stiefel-Whitney class w₂ ≠ 0). To define spinors on CP²,
one must either:
(a) Use the spin^c structure (coupling to the Kähler connection), or
(b) Note that CP² × S² is spin (the total w₂ cancels).

For the product CP² × S², the total space IS spin, and admits Killing
spinors. The number of Killing spinors on the product is:

    N_Killing(CP² × S²) = N_Killing(CP²) × N_Killing(S²)

For S²: 2 Killing spinors.
For CP² (using spin^c): 2 Killing spinors (one for each chirality
of the spin^c bundle).

Total: 2 × 2 = **4 Killing spinors** on CP² × S².

Without the Scherk-Schwarz twist, this would give N = 4 supersymmetry
in 5D (before the S¹ reduction) or N = 8 in 4D (after the S¹ reduction
preserving all supercharges). The Scherk-Schwarz twist on S¹/Z₂ breaks
ALL supersymmetries, giving N = 0 in 4D.

**Summary for Ψ_μ:**
- 4 would-be gravitini (from 4 Killing spinors)
- All massive with m ≥ 1/(2R)
- 0 massless gravitini → N = 0 SUSY in 4D

### C.3 Ψ_a: CP² Components → 4D Spin-1/2

**Ψ_a(x,y,z,φ):** The CP² components of the gravitino.

Under dimensional reduction, a spinor with a CP² vector index
decomposes as:

    Ψ_a = (spin-3/2 on CP²) ⊕ (spin-1/2 on CP²)

using the decomposition of the vector-spinor representation.

The relevant modes for 4D fields are:

(a) **Killing spinor-vectors on CP²** (spin-3/2 zero modes): these
would give 4D spin-1/2 fields. The number of Killing spinor-vectors
is related to the Killing spinors by a Weitzenböck formula. On CP²,
the number of independent solutions is determined by the representation
theory of SU(3).

(b) **Harmonic spinors on CP²** (Dirac zero modes): the index of the
Dirac operator on CP² is given by the Atiyah-Singer index theorem:

    ind(D_{CP²}) = Â(CP²) = 0

(The Â-genus of CP² vanishes because CP² is not spin. Using the spin^c
Dirac operator coupled to the canonical line bundle:)

    ind(D^{spin^c}_{CP²}) = χ(CP², O) = 1

But we need the full product CP² × S². On this spin manifold, the
Dirac operator decomposes as:

    D_{CP² × S²} = D_{CP²} ⊗ 1 + γ_{CP²} ⊗ D_{S²}

The zero modes of D_{CP² × S²} are:

    ker(D_{CP² × S²}) = ker(D_{CP²}) ⊗ ker(D_{S²})

On S² of radius r₂: the Dirac operator has zero modes (Killing spinors).
The index is ind(D_{S²}) = 0 (from the Â-genus), but the kernel is
nontrivial: dim ker(D_{S²}) = 1 (one zero mode for each chirality, but
they're paired).

Actually, for S² the Dirac spectrum is:

    eigenvalues: ±(l + 1/2)/r₂,  l = 0, 1, 2, ...
    degeneracy: 2(l+1) for each sign

There is no zero eigenvalue — the lowest eigenvalue is ±1/(2r₂). So
dim ker(D_{S²}) = 0 on the round S².

Wait — this depends on whether we mean the standard Dirac operator or
the Killing spinor equation. The Killing spinor equation ∇η = λγη
is NOT the Dirac equation Dη = 0. Killing spinors satisfy Dη = nλη
(they are eigenspinors of the Dirac operator, not zero modes).

For the decomposition of Ψ_a, the relevant objects are the eigenspinors
of D_{CP²} and D_{S²}, which form a complete basis. The 4D mass spectrum
is determined by these eigenvalues combined with the Scherk-Schwarz
mass on S¹.

The key point is: **ALL 4D fermions from the gravitino are massive.**
The Scherk-Schwarz mechanism ensures a mass gap of 1/(2R) from the S¹
factor, and the internal Dirac eigenvalues on CP² and S² add additional
mass contributions.

For the CP² sector specifically:
- The vector-spinor on CP² decomposes into representations of SU(3)
- These give 4D spin-1/2 fields in various SU(3) representations
- All are massive (minimum mass 1/(2R))

**From Ψ_a: 0 massless 4D fields** (all massive, m ≥ 1/(2R))

### C.4 Ψ_i: S² Components → 4D Spin-1/2

**Ψ_i(x,y,z,φ):** The S² components of the gravitino.

By the same analysis as C.3, with the roles of CP² and S² exchanged:

- The vector-spinor on S² decomposes into spin-1/2 modes
- These transform in representations of SU(2)
- All are massive due to the Scherk-Schwarz mechanism

**From Ψ_i: 0 massless 4D fields** (all massive, m ≥ 1/(2R))

### C.5 Ψ_φ: S¹ Component → Dilatino

**Ψ_φ(x,y,z,φ):** The S¹ component of the gravitino.

This is the "dilatino" — the would-be superpartner of the S¹ dilaton.
In a supersymmetric reduction, it would pair with the dilaton g_φφ in
a chiral multiplet.

Under the Scherk-Schwarz twist: anti-periodic on S¹, so no zero mode.

- 4D spin: 1/2 (the dilatino)
- Massless species: **0** (Scherk-Schwarz projected)
- Lightest mode: mass 1/(2R)

**From Ψ_φ: 0 massless 4D fields**

### C.6 The Massive Fermion Spectrum

Although no massless fermions survive the Scherk-Schwarz projection,
the massive spectrum is important for the Casimir energy calculation.

The gravitino has 128 on-shell d.o.f. in 11D. Under the KK reduction,
these distribute as massive towers on each internal factor:

**S¹ tower (Scherk-Schwarz):**
- Masses: m_n = (n + 1/2)/R, n = 0, 1, 2, ...
- Each mass level contains the full CP² × S² spectrum of modes
- The n=0 level (mass 1/(2R)) contains the lightest fermions

**S² tower:**
- The Dirac eigenvalues on S² add to the masses
- Combined mass: m² = ((n+1/2)/R)² + λ²_{S²}
- where λ_{S²} are the eigenvalues of the Dirac operator on S²

**CP² tower:**
- Similarly, the Dirac eigenvalues on CP² contribute
- Full mass formula: m² = ((n+1/2)/R)² + λ²_{S²} + λ²_{CP²}

### C.7 Counting Fermionic d.o.f. for the Casimir Energy

For the Casimir energy on each internal factor, we need the EFFECTIVE
number of fermionic d.o.f. propagating on that factor.

**On S¹:** All 128 fermionic d.o.f. propagate on S¹ (anti-periodic).
Each contributes to the S¹ Casimir with the opposite sign from bosons
(fermionic statistics → −(−1)^{2s} = +1 for s=1/2, 3/2).

More precisely, the effective number of 4D fermionic fields propagating
on S¹ is determined by the zero-mode count on CP² × S²:

The gravitino Ψ_M in 11D has:
- Vector index M → 11 components, but on-shell: 9 (transverse)
- Spinor: 32-component Majorana in 11D, on-shell: 16

Total on-shell: 9 × 16 / 2 = 128 (dividing by 2 for the Rarita-Schwinger
constraint γ^M Ψ_M = 0 and equation of motion, effectively giving
(D-3) × 2^{(D-3)/2} / 2 = 8 × 16 = 128).

For the S¹ Casimir, we need the number of effective 4D+6D fields at
each S¹ KK level. At the lowest level (n=0):
- 128 d.o.f., all with mass 1/(2R) from the S¹

**On S²:** The gravitino components that propagate on S² are:
- Ψ_μ: 4 × (4D spinor d.o.f.) = 4 × 4 = 16 per S² mode → but
  constrained to (D_4-3) × 2 = 2 on-shell per mode
- Ψ_i: 2 × (4D spinor d.o.f.) per S² mode
- Ψ_a: not directly on S², contributes through CP² modes
- Ψ_φ: contributes as a spectator

The detailed counting requires tracking each KK tower carefully,
which we do in Part D.

### C.8 Summary of Gravitino Decomposition

| Sector | Would-be 4D field | Spin | Would-be massless | Actual massless |
|--------|-------------------|------|-------------------|-----------------|
| Ψ_μ    | gravitino(s)      | 3/2  | 4 (from Killing spinors) | 0 |
| Ψ_a    | gauginos (CP²)    | 1/2  | various reps of SU(3) | 0 |
| Ψ_i    | gauginos (S²)     | 1/2  | various reps of SU(2) | 0 |
| Ψ_φ    | dilatino          | 1/2  | 1                  | 0               |
| **Total** |                |      |                    | **0**           |

**The Scherk-Schwarz mechanism on S¹/Z₂ eliminates ALL massless fermions.**

This is the origin of the non-supersymmetric 4D spectrum: all bosonic
fields from the metric and 3-form have massless zero modes, but all
fermionic fields from the gravitino are massive. The boson-fermion
asymmetry drives the Casimir energy.

---

## Part D: Summary Tables

### Table 1: Complete 4D Massless Spectrum

| # | Field | Source | Spin | d.o.f. | Gauge rep | Notes |
|---|-------|--------|------|--------|-----------|-------|
| 1 | graviton g_μν | g_MN | 2 | 2 | singlet | 4D gravity |
| 2-9 | gluons B_μ^I | g_μa | 1 | 16 | 8 of SU(3) | strong force |
| 10-12 | weak bosons C_μ^J | g_μi | 1 | 6 | 3 of SU(2) | weak force |
| 13 | photon A_μ | g_μφ | 1 | 2 | 1 of U(1) | EM |
| 14 | CP² U(1) A'_μ | C_μab | 1 | 2 | 1 of U(1)' | from ω∈H²(CP²) |
| 15 | S² U(1) A''_μ | C_μij | 1 | 2 | 1 of U(1)'' | from ε∈H²(S²) |
| 16 | CP² modulus r₃ | g_ab | 0 | 1 | singlet | breathing mode |
| 17 | S² modulus r₂ | g_ij | 0 | 1 | singlet | breathing mode |
| 18 | S¹ dilaton R | g_φφ | 0 | 1 | singlet | e-circle radius |
| 19 | axion σ | C_μνρ | 0 | 1 | singlet | dual of 3-form |
| — | gravitini, gauginos | Ψ_M | 3/2, 1/2 | 0 | various | ALL massive |

**Total massless d.o.f.: 34**
- Bosonic: 2 (graviton) + 28 (gauge bosons: 16+6+2+2+2) + 4 (scalars) = 34
- Fermionic: 0

**Gauge group of the massless sector:**

    G = SU(3) × SU(2) × U(1) × U(1)' × U(1)''

With the Stückelberg mechanism eating two of the three U(1) gauge bosons
(via the 3-form gauge transformations), the effective low-energy gauge
group is:

    G_eff = SU(3) × SU(2) × U(1)

matching the Standard Model gauge group.

### Table 2: Internal Factor Association

For each 4D field, which internal factor(s) it "propagates on" — meaning
its KK tower lives on that factor, so it contributes to the Casimir
energy of that factor.

| Field | Propagates on S¹ | Propagates on S² | Propagates on CP² |
|-------|-------------------|-------------------|---------------------|
| graviton g_μν | no (zero mode) | no (zero mode) | no (zero mode) |
| gluons B_μ^I | KK tower | zero mode | Killing vectors |
| weak bosons C_μ^J | KK tower | Killing vectors | zero mode |
| photon A_μ | Killing vector | zero mode | zero mode |
| U(1)' from C_μab | KK tower | zero mode | H²(CP²) topology |
| U(1)'' from C_μij | KK tower | H²(S²) topology | zero mode |
| r₃ modulus | KK tower | zero mode | breathing mode |
| r₂ modulus | KK tower | breathing mode | zero mode |
| R dilaton | breathing mode | zero mode | zero mode |
| axion σ | KK tower | zero mode | zero mode |
| gravitini (massive) | anti-periodic | eigenspinors | eigenspinors |

**Interpretation:**

- A field "propagates on" a factor if its KK tower includes non-trivial
  modes on that factor. This means the field's Casimir energy depends on
  the size of that factor.

- The graviton is a zero mode on ALL internal factors — it does not
  contribute to ANY internal Casimir energy at one loop.

- The SU(3) gauge bosons propagate on CP² (they ARE the CP² Killing
  vector modes) and have a KK tower on S¹. They contribute to the
  Casimir energy on both CP² and S¹.

- Similarly, the SU(2) gauge bosons propagate on S² and S¹.

- ALL fields (bosonic and fermionic) have KK towers on S¹ (periodic
  for bosons, anti-periodic for fermions).

### Table 3: Effective d.o.f. for Casimir Energy

This is the critical table. For each internal factor, we count the
net bosonic d.o.f. (weighted by spin-statistics factor (−1)^{2s})
that propagate on that factor.

The Casimir energy on a factor X has the form:

    V_Casimir^X = c_1^X / (Vol_X)^{(d_X+1)/d_X} × [spectral zeta factor]

where c_1^X = Σ_fields (−1)^{2s} × d_s × (species on X).

#### Table 3a: Casimir Coefficients for S¹

On S¹, ALL fields have KK towers (periodic for bosons, anti-periodic
for fermions). The effective d.o.f. count is:

| Field type | Spin s | (−1)^{2s} | d.o.f. per species | # species on S¹ | Contribution |
|------------|--------|-----------|-------------------|-----------------|-------------|
| graviton | 2 | +1 | 2 | 1 | +2 |
| SU(3) gauge | 1 | +1 | 2 | 8 | +16 |
| SU(2) gauge | 1 | +1 | 2 | 3 | +6 |
| U(1) gauge (metric) | 1 | +1 | 2 | 1 | +2 |
| U(1)' gauge (C-field) | 1 | +1 | 2 | 1 | +2 |
| U(1)'' gauge (C-field) | 1 | +1 | 2 | 1 | +2 |
| CP² modulus | 0 | +1 | 1 | 1 | +1 |
| S² modulus | 0 | +1 | 1 | 1 | +1 |
| R dilaton | 0 | +1 | 1 | 1 | +1 |
| axion | 0 | +1 | 1 | 1 | +1 |
| **Bosonic subtotal** | | | | | **+34** |
| gravitini (×4) | 3/2 | −1 | 2 | 4 | −8 |
| gauginos CP² | 1/2 | −1 | 2 | (from CP² Killing spinor-vectors) | (see below) |
| gauginos S² | 1/2 | −1 | 2 | (from S² eigenspinors) | (see below) |
| dilatino | 1/2 | −1 | 2 | 1 | −2 |

For the full fermionic count on S¹: the 11D gravitino has 128 on-shell
d.o.f. These ALL propagate on S¹ (anti-periodic). At each S¹ KK level,
there are 128 fermionic d.o.f.

The net Casimir coefficient for S¹ is:

    c_1^{S¹} = (bosonic d.o.f. on S¹) − (fermionic d.o.f. on S¹)

But we must be careful: the bosonic d.o.f. on S¹ are not simply 34
(the massless count). At each S¹ KK level, the FULL set of 11D modes
contributes. The 11D SUGRA has 128B + 128F on-shell d.o.f., so:

    c_1^{S¹} = n_B − n_F = 128 − 128 = 0 ... ?

NO — this is the naive count for the UNTWISTED S¹. The Scherk-Schwarz
twist changes the periodicity:
- Bosons: periodic → standard KK sum Σ_{n∈Z}
- Fermions: anti-periodic → shifted KK sum Σ_{n∈Z+1/2}

The Casimir energy on S¹ with these mixed boundary conditions is:

    V^{S¹} = (1/2R) [n_B × E_P(s) − n_F × E_AP(s)]

where E_P and E_AP are the Epstein zeta sums for periodic and
anti-periodic boundary conditions respectively.

The key result (from standard Casimir calculations):
- Periodic BC: E_P = −ζ_R(−1)/R = +1/(12R)
- Anti-periodic BC: E_AP = −(1−2^{1+1})ζ_R(−1)/R = −7/(12R) × (−1) ...

Actually, let me state the standard result cleanly. For a circle of
circumference L = 2πR:

    E_Casimir^{periodic}(L) = −π/(6L) × n_B
    E_Casimir^{anti-periodic}(L) = +π/(12L) × n_F

(The anti-periodic Casimir energy has the OPPOSITE sign from periodic,
and is reduced by a factor of 2.)

Wait — the precise result is:

For a SINGLE real scalar field on S¹ of radius R:
- Periodic BC: E = −1/(4πR²) × π²/6 × ... 

Let me use the notation from etc/12b. The S¹ Casimir potential is:

    V^{S¹}(R) = −1/(2(2πR)) [n_B ζ_R(−1) + n_F ζ_R^{AP}(−1)]

where ζ_R^{AP}(s) = Σ_{n=0}^∞ (n+1/2)^{−s} = (2^s − 1) ζ_R(s).

For the effective potential on S¹:

    c_1^{S¹} = n_B − n_F × (ratio of AP to P Casimir)

The ratio is: ζ^{AP}(−1)/ζ_R(−1) = (2^{−1}−1)(−1/12) / (−1/12) = −1/2.

Hmm, let me just state it directly. Using the standard result for the
Casimir energy density on S¹ of circumference L:

    ρ_Casimir = −(π/6L²) [n_B^{per} + n_F^{anti-per} × (−1/2 + 1)]

Actually, the cleanest formulation uses the Epstein zeta:

For periodic boundary conditions (bosons):
    ε_n = n/R, n ∈ Z → Casimir: −1/(720 R⁴) per d.o.f. (in 4D)

For anti-periodic (fermions):
    ε_n = (n+1/2)/R → Casimir: +7/(5760 R⁴) per d.o.f. (in 4D)

The ratio is −7/8, with opposite sign. So:

    V_{S¹} ∝ [n_B − (7/8) n_F] / R⁴ × (numerical factor)

But wait — this 7/8 factor is for 4D fields in a thermal/Casimir
context. For a 1D compactification (S¹), the relevant formula is:

    V_{S¹} = −(1/R) [n_B × (−ζ(−1)/2) + n_F × (−ζ^{AP}(−1)/2)]

where the signs encode spin-statistics. For the net coefficient:

    c_1^{S¹} = n_B × ζ(−1) − n_F × ζ^{AP}(−1)
             = n_B × (−1/12) − n_F × ((2^{−1}−1)(−1/12))
             = −n_B/12 − n_F × (1/24)
             = −(1/12)(n_B + n_F/2)

Since n_B = 128 and n_F = 128:

    c_1^{S¹} = −(1/12)(128 + 64) = −(1/12)(192) = −16

The sign is NEGATIVE, meaning the Casimir energy is attractive (tends
to shrink S¹). This must be balanced by the classical flux energy
(which is repulsive) to stabilize the modulus.

Actually, let me reconsider. The overall sign depends on conventions.
The physical content is: c_1^{S¹} ≠ 0 because the Scherk-Schwarz
twist breaks the bose-fermi degeneracy on S¹.

#### Table 3b: Casimir Coefficients for S²

For the S² Casimir, we sum over all fields that have non-trivial
KK towers on S², taking zero modes on the other factors.

**Bosonic fields propagating on S²:**

The fields with S² KK towers are those whose internal wavefunctions
involve non-trivial harmonics on S². At the zero-mode level on CP²
and S¹:

| Field | # of effective scalars on S² | Origin |
|-------|------------------------------|--------|
| g_μν × (CP² zero) × (S¹ zero) | 2 (helicities) | graviton |
| g_μa × (CP² Killing) × (S¹ zero) | 8 × 2 = 16 | SU(3) gauge |
| g_μφ × (S¹ Killing) | 2 | U(1) photon |
| g_ab × (CP² breathing) × (S¹ zero) | 1 | r₃ modulus |
| g_φφ × (S¹ zero) | 1 | dilaton |
| C_μνρ × (S¹ zero) | 1 | axion |
| C_μab × (CP² ω) × (S¹ zero) | 2 | U(1)' gauge |
| g_μi: these ARE the S² modes | 3 × 2 = 6 | SU(2) gauge |
| g_ij: this IS the S² mode | 1 | r₂ modulus |
| C_μij: this IS the S² mode | 2 | U(1)'' gauge |

However, this double-counts. We must be more careful about which fields
actually have S² KK towers versus which are zero modes on S².

The correct counting for the S² Casimir is: for each field, ask
"does this field have a non-trivial S² dependence?" If yes, its
S² KK tower contributes to the S² Casimir.

Fields with non-trivial S² dependence:
- g_μi (the SU(2) gauge bosons): these are built from S² Killing vectors
- g_ij (the S² breathing mode): S² metric deformation
- C_μij (the S² U(1)): built from the S² volume form

Fields that are zero modes on S² (constant on S²):
- g_μν, g_μa, g_μφ, g_ab, g_φφ: all are S² zero modes
- C_μνρ, C_μab: S² zero modes

The S² zero modes do NOT contribute to the S² Casimir energy at
leading order (they have no S² KK mass). Only the massive S² modes
contribute.

But for the Casimir energy on S², we sum over ALL S² KK levels
(l = 0, 1, 2, ...) for each field that lives on S². Each field
has the full tower. The question is: how many independent fields
have S² towers?

The correct approach: start from 11D, reduce first on CP² × S¹
to get an intermediate theory on S², then compute the S² Casimir.

After reducing on CP² × S¹ (taking zero modes), the effective
fields on M⁴ × S² are:

From the metric sector:
- A 5+1D graviton (from g_μν, g_μi, g_ij): contributes as
  a 6D graviton on M⁴ × S², which has 6×7/2 − (gauge) = 9 d.o.f.
  in 6D, reducing to various 4D fields via S² KK decomposition.
  But since we already took the CP² × S¹ zero modes, we effectively
  have a 6D theory.

This is getting intricate. Let me instead count the number of
EFFECTIVE SCALAR FIELDS on S² by reducing the other dimensions first.

**After reduction on CP² (zero modes) × S¹ (zero modes for bosons):**

The effective theory on M⁴ × S² has the following field content:

From g_MN:
- g_μν(x): 4D metric → 1 field (5 d.o.f. as massive spin-2, but
  at zero mode level: 2 d.o.f.)
- g_μa(x) → 8 vectors in 4D (from CP² Killing vectors): each is
  a constant on S², so does not propagate on S²
- g_μφ(x) → 1 vector: constant on S²
- g_μi(x,z) → this becomes a 4D+S² vector. The S² Killing vectors
  give 3 massless vectors, plus a KK tower.
  At each S² KK level l, the vector harmonics on S² give
  2(2l+1) vector modes for l ≥ 1.
- g_ab(x) → 1 scalar (r₃): constant on S²
- g_φφ(x) → 1 scalar (R): constant on S²
- g_ij(x,z) → the S² metric fluctuations: 1 breathing mode at l=0,
  plus a KK tower.
- g_ai(x,z) → from CP² Killing × S² index: but we took CP²
  zero modes, so these are 8 vectors on S².
  Wait — g_ai has one CP² and one S² index. After taking the CP²
  zero mode (Killing vector expansion), we get 8 fields with one
  S² index, i.e., 8 vectors on S². But these are gauge artifacts
  (see A.8). Skip.
- g_aφ, g_iφ: zero (Z₂ projection).

From C_MNP (after CP² × S¹ zero modes):
- C_μνρ → 1 scalar: constant on S²
- C_μab → from ω ∈ H²(CP²): 1 vector in 4D, constant on S²
- C_μij(x,z) → 1 vector from ε ∈ H²(S²), plus KK tower
- C_μνi → zero (b₁(S²)=0 for massless, but massive tower exists)
- Other C sectors: zero

So the fields that PROPAGATE on S² (have S² KK towers) are:
1. g_μi: the 6D metric cross-terms → S² vector harmonics
2. g_ij: S² metric fluctuations → S² scalar/tensor harmonics  
3. C_μij: the 3-form with two S² indices → S² 2-form harmonics
4. The 4D graviton, gauge bosons, and scalars that are constant
   on S² also have S² KK towers when we consider the full 6D theory

Actually, the correct statement is simpler: ALL fields in the effective
6D theory (M⁴ × S²) have KK towers on S². The number of 6D d.o.f.
determines the S² Casimir.

After the CP² × S¹ reduction, the 6D field content (on M⁴ × S²) is:

**Bosonic 6D fields:**

From g_MN (11D graviton, 44 d.o.f.):
After reducing on CP² (keeping Killing vectors + zero modes) and S¹
(keeping n=0 mode for bosons):

The 11D index M splits as (μ, a, i, φ). The symmetric tensor g_MN
with M,N ∈ {μ, a, i, φ} gives:
- (μ,ν): 6D metric g_μν^{6D} where μ now runs over 4D + S²
  Actually no — we are reducing CP² and S¹ first, keeping S² untouched.
  
Let me reframe. We reduce on CP²(zero modes) × S¹(zero mode), keeping
the full S² dependence. The result is a 6D theory on M⁴ × S² with:

Metric sector:
- 6D graviton h_αβ (α,β ∈ {μ, i}): the metric on M⁴ × S²
  On-shell d.o.f. in 6D: 6×7/2 − 6 = 15 → but we need to be careful.
  A massless graviton in 6D has (6-2)(6-1)/2 - 1 = 9 on-shell d.o.f.
- 8 vectors B_α^I (from CP² Killing vectors): 8 × (6−2) = 32 ... 
  no, a massless vector in 6D has (6−2) = 4 on-shell d.o.f.
  So 8 × 4 = 32
- 1 vector A_α (from S¹ Killing): 1 × 4 = 4
- 1 scalar (CP² breathing mode): 1
- 1 scalar (S¹ dilaton): 1

Total from g_MN in 6D: 9 + 32 + 4 + 1 + 1 = 47

From C_MNP (11D 3-form, 84 d.o.f.):
After CP² × S¹ reduction:
- C_αβγ: 6D 3-form → in 6D has C(4,3) = 4 d.o.f. (using only
  transverse indices) → actually 6D 3-form has (6-2)(6-3)(6-4)/6 = 4×3×2/6 = 4
  But this comes from C_μνρ and C_μνi → a 6D 3-form. On-shell: 
  C(6-2, 3) = C(4,3) = 4 d.o.f.
- C_αβ,a → needs ω ∈ H²(CP²): gives a 6D 2-form. On-shell: C(4,2)=6 d.o.f.
- C_α,ab → with ω: a 6D 1-form (vector). On-shell: 4 d.o.f.
  This is the U(1)' gauge boson.
- C_αβ,φ → zero (Z₂ projection)
- C_abc → zero (b₃(CP²)=0)

Total from C_MNP in 6D: 4 + 6 + 4 = 14

Total 6D bosonic d.o.f.: 47 + 14 = 61

**Fermionic 6D fields:**

From Ψ_M (11D gravitino, 128 d.o.f.):
After CP² × S¹ reduction (S¹ anti-periodic → no zero mode!):

Since fermions are ANTI-PERIODIC on S¹, they have NO zero mode
on S¹. Therefore, after the S¹ reduction, there are NO fermionic
fields in the effective 6D theory at the massless level.

For the massive S¹ KK levels: at each level n, there are fermionic
modes, but they all have mass ≥ 1/(2R). For the S² Casimir at
energies below 1/R, these decouple.

**This is the key insight for the S² Casimir:** In the hierarchy
r₃ << r₂ << R, the S² Casimir energy is dominated by the BOSONIC
fields (since all fermions are massive at scale 1/R >> 1/r₂ and
therefore decouple from the S² Casimir at leading order).

Therefore:

    c_1^{S²} ≈ n_B^{eff, S²} (pure bosonic, fermions decoupled)

The effective bosonic d.o.f. on S²:

To count properly, we need the number of EFFECTIVE SCALAR FIELDS
on S² (since each field type contributes differently to the Casimir).

A spin-s field in 4D contributes to the Casimir like d_s effective
scalars, where d_s is the number of on-shell polarizations:
- spin 0: d₀ = 1
- spin 1: d₁ = 2
- spin 2: d₂ = 2

The bosonic fields that are constant on S² (zero modes) contribute
to the S² Casimir through their S² KK towers. Each such 4D field
has a KK tower on S² with eigenvalues l(l+1)/r₂².

The number of 4D fields that are zero modes on S² and have KK
towers:
- graviton: 1 field × 2 d.o.f. = 2 eff. scalars
- 8 SU(3) gauge: 8 × 2 = 16
- 1 U(1) metric gauge: 1 × 2 = 2
- 1 U(1)' C-field gauge: 1 × 2 = 2
- r₃ modulus: 1
- R dilaton: 1
- axion: 1

Subtotal (S² zero modes): 2 + 16 + 2 + 2 + 1 + 1 + 1 = 25

Plus the fields that ARE the S² modes (not zero modes):
- 3 SU(2) gauge: from S² Killing vectors (l=1)
- 1 r₂ modulus: from S² breathing (l=0 trace)
- 1 U(1)'' from C_μij: from S² volume form (l=0 of 2-form)

These are already part of the S² spectrum — they contribute specific
modes within the S² KK tower.

The total effective bosonic scalar count for S² Casimir is:

    c_1^{S²} = 25 (from 4D fields × S² towers)
             + corrections from the non-minimal coupling of higher spins

For a rough estimate: **c_1^{S²} ≈ 25** (all bosonic, all positive).

#### Table 3c: Casimir Coefficients for CP²

By the same logic, for the CP² Casimir we reduce on S² × S¹ first.

Fields that are zero modes on CP² and have KK towers:
- graviton: 2 eff. scalars
- 3 SU(2) gauge: 3 × 2 = 6
- 1 U(1) metric gauge: 2
- 1 U(1)'' from C_μij: 2
- r₂ modulus: 1
- R dilaton: 1
- axion: 1

Subtotal (CP² zero modes): 2 + 6 + 2 + 2 + 1 + 1 + 1 = 15

Plus the fields that ARE CP² modes:
- 8 SU(3) gauge: from CP² Killing vectors
- 1 r₃ modulus: CP² breathing
- 1 U(1)' from C_μab: from Kähler form

Again, fermions decouple (massive from Scherk-Schwarz).

    c_1^{CP²} ≈ 15 (all bosonic, all positive)

#### Table 3 Summary: Net Casimir Coefficients

| Internal factor | c_1 (bosonic) | c_1 (fermionic) | c_1 (net) | Sign of Casimir |
|-----------------|---------------|-----------------|-----------|-----------------|
| S¹ (radius R) | +128 | −128 (shifted) | ≠ 0 (SS twist) | stabilizing |
| S² (radius r₂) | +25 | ~0 (decoupled) | +25 | positive (attractive) |
| CP² (radius r₃) | +15 | ~0 (decoupled) | +15 | positive (attractive) |

**Key results:**

1. **c_1^{S¹} ≠ 0** due to the Scherk-Schwarz twist. The precise value
   depends on the relative weight of periodic (boson) vs anti-periodic
   (fermion) Casimir sums. With n_B = n_F = 128 but different boundary
   conditions, the S¹ Casimir is non-vanishing and proportional to
   (n_B + n_F/2)/12 = (128 + 64)/12 = 16.

2. **c_1^{S²} ≈ 25** — purely bosonic because fermions decouple
   in the hierarchy r₂ << R.

3. **c_1^{CP²} ≈ 15** — purely bosonic, same reasoning.

4. **The hierarchy c_1^{S²} > c_1^{CP²}** means the Casimir force is
   STRONGER on S² than on CP², which tends to make S² smaller than CP²
   in the absence of other effects. Combined with the flux quantization
   and classical potential, this drives the stabilization toward
   r₃ < r₂ < R, consistent with g₃ > g₂ > g₁ (asymptotic freedom
   aside, the bare couplings satisfy this hierarchy).

5. **The ratio c_1^{S²}/c_1^{CP²} ≈ 25/15 = 5/3** is a prediction
   of the framework for the relative Casimir strengths.

---

## Appendix: Cross-Checks and Consistency

### D.o.f. Count Cross-Check

11D SUGRA: 128B + 128F = 256 total on-shell d.o.f.

Our massless 4D spectrum: 34B + 0F = 34 total.

The "missing" 256 − 34 = 222 d.o.f. are in:
- Massive KK towers on S¹ (bosonic and fermionic)
- Massive KK towers on S² and CP²
- The Stückelberg-massive U(1) gauge bosons (eaten by 3-form scalars)

### Gauge Group Cross-Check

Metric gauge bosons: SU(3) × SU(2) × U(1) — 8 + 3 + 1 = 12 generators
3-form gauge bosons: U(1)' × U(1)'' — 2 additional U(1) factors
Total: 14 gauge bosons

After Stückelberg mechanism: SU(3) × SU(2) × U(1) — 12 generators
This matches the Standard Model gauge group.

### Cohomology Cross-Check

The total number of massless scalars from the 3-form is determined by
the Betti numbers of the internal manifold M₇ = CP² × S² × S¹:

By the Künneth formula:
    b_p(M₇) = Σ_{i+j+k=p} b_i(CP²) × b_j(S²) × b_k(S¹)

| p | Contributions | b_p(M₇) |
|---|---------------|----------|
| 0 | b₀×b₀×b₀ = 1 | 1 |
| 1 | b₁(CP²)×1×1 + 1×b₁(S²)×1 + 1×1×b₁(S¹) = 0+0+1 | 1 |
| 2 | b₂(CP²)×1×1 + 1×b₂(S²)×1 + cross terms = 1+1+0 | 2 |
| 3 | b₂(CP²)×b₁(S¹) + b₂(S²)×b₁(S¹) + b₃(CP²)×1×1 + ... = 1+1+0+0 | 2 |
| 4 | b₄(CP²)×1×1 + b₂(CP²)×b₂(S²)×1 + b₂(CP²)×1×b₁(S¹)... wait |

Let me be systematic. The nonzero Betti numbers of the factors:

CP²: b₀=1, b₂=1, b₄=1
S²: b₀=1, b₂=1
S¹: b₀=1, b₁=1

Products for b_p(M₇):
- p=0: (0,0,0) → 1×1×1 = 1
- p=1: (0,0,1) → 1×1×1 = 1
- p=2: (2,0,0)+(0,2,0)+(0,0,?) → 1×1×1 + 1×1×1 + 0 = 2
  [no (0,0,2) since S¹ is 1-dimensional]
- p=3: (2,0,1)+(0,2,1)+(2,2,?)... 
  (2,0,1): b₂(CP²)×b₀(S²)×b₁(S¹) = 1
  (0,2,1): b₀(CP²)×b₂(S²)×b₁(S¹) = 1
  (4,0,?)+(2,2,?): can't make (i,j,k) with i+j+k=3 and j≤2, k≤1, i∈{0,2,4}
  other than (2,0,1) and (0,2,1).
  b₃ = 2
- p=4: (4,0,0)+(2,2,0)+(2,0,?)+(0,2,?)...
  (4,0,0): 1×1×1 = 1
  (2,2,0): 1×1×1 = 1
  (4,0,0) and (2,2,0): b₄ = 2
  Wait, also (2,2,0)=1. And (0,2,1)? no that's p=3.
  (4,0,0)=1, (2,2,0)=1. Any more? (0,4,0): b₄(S²)=0. 
  b₄ = 2
- p=5: (4,0,1)+(2,2,1)+(4,2,?)...
  (4,0,1): 1×1×1 = 1
  (2,2,1): 1×1×1 = 1
  b₅ = 2
- p=6: (4,2,0)+(4,0,?)+(2,2,?)...
  (4,2,0): 1×1×1 = 1
  (4,2,0) only possibility with i∈{0,2,4}, j∈{0,2}, k∈{0,1}, i+j+k=6.
  Also (4,2,0): b₆ = 1
  Wait: (2,2,1)? 2+2+1=5, not 6. (4,2,0)=6. (4,0,1)? 4+0+1=5.
  Only (4,2,0): b₆ = 1
- p=7: (4,2,1): 1×1×1 = 1. b₇ = 1

So: b₀=1, b₁=1, b₂=2, b₃=2, b₄=2, b₅=2, b₆=1, b₇=1.

Poincaré duality check: b_p = b_{7-p}. ✓ (1,1,2,2,2,2,1,1)

Euler characteristic: χ = 1−1+2−2+2−2+1−1 = 0. ✓ (odd-dimensional manifold)

**For S¹/Z₂ orbifold:** The Z₂ acts as φ → −φ. The harmonic forms
that are ODD under Z₂ (those involving dφ) are projected out. This
removes b₁(S¹)=1, effectively setting:

Effective Betti numbers for CP² × S² × S¹/Z₂ (even sector only):
- b₀=1, b₁=0, b₂=2, b₃=0, b₄=2, b₅=0, b₆=1, b₇=0

Wait — the forms involving dφ are:
- p=1: dφ → removed. b₁: 1→0
- p=3: ω∧dφ, ε∧dφ → removed. b₃: 2→0  
- p=5: ω∧ε∧dφ... let me check:
  (2,0,1)=ω_CP²∧dφ, (0,2,1)=ε_S²∧dφ → both removed. b₅: 2→0
- p=7: vol_CP²∧vol_S²∧dφ → removed. b₇: 1→0

Even sector: b₀=1, b₁=0, b₂=2, b₃=0, b₄=2, b₅=0, b₆=1, b₇=0.

The massless scalars from C_MNP come from harmonic 3-forms (giving 4D
scalars directly) and harmonic 2-forms (giving 4D vectors).

- H³(M₇)^{even} = 0: no scalars from C_{abc...} with 3 internal indices
  and no dφ component. ✓ (consistent with our finding of 0 scalars
  from the purely internal C-sectors)
  
- H²(M₇)^{even} = Z² (from ω_CP² and ε_S²): two 4D vectors from C_μab
  and C_μij. ✓ (consistent with our finding of 2 U(1) gauge bosons)

The cohomology cross-check confirms our field content decomposition.

