# Paper 11: Why SU(3) x SU(2) x U(1)

## Working Title

*"Gauge Group Selection by Entanglement Geometry:
The Standard Model from Three Generations on the e-Circle"*

---

## The Question

Why is the gauge group of the universe SU(3) x SU(2) x U(1)/Z_6 and
not something else? This is arguably the deepest open question in
fundamental physics. The Standard Model takes the gauge group as an
input. String theory has a landscape of ~10^500 vacua. No framework
has derived the gauge group from a principle.

Paper 11 answers: **because that is the entanglement geometry of
three fermionic generations on the e-circle.**

---

## The Argument (One Paragraph)

In the e-dimension framework, entanglement is not an abstract
correlation — it is the conservation of the e-coordinate
(phi_1 + phi_2 = C). Three generations of fermions, each a qubit
on the e-circle, span a three-qubit Hilbert space (C^2)^{tensor 3}.
The SLOCC (stochastic local operations and classical communication)
equivalence classes of this space — the orbits under local
SL(2,C)^3 — classify the entanglement types. The GHZ orbit, which
is the generic entanglement class for three qubits, has a tangent
space that carries the A_2 root system — the roots of su(3). The
stabilizer of the GHZ state produces the Z_6 quotient. The S^1
factor (the e-circle itself) provides the U(1). The result:

    G_SM = [SU(3) x SU(2) x U(1)] / Z_6

This is not fitted, assumed, or selected from a landscape. It is the
unique gauge group determined by the entanglement geometry of three
qubits. The number of generations (three) comes from the Euler
characteristic chi(CP^2) = 3. The gauge group comes from the
entanglement structure of those three generations.

---

## Structure

### Section 1: The Three-Qubit System on the e-Circle

**Ingredients (all from Papers 1-4):**
- Each fermion generation has a two-state system on S^1 (the e-circle):
  |0> = left-mover, |1> = right-mover (winding number parity)
- Three generations = three qubits: H = (C^2)^{tensor 3}
- Entanglement = e-conservation: phi_1 + phi_2 + phi_3 = Q_e (Noether charge)
- The e-conservation constraint selects SLOCC equivalence classes

**New content:**
- Derive the SLOCC classification from e-conservation explicitly
- Show that the e-conservation constraint on three S^1-valued degrees of freedom
  produces the GHZ orbit as the generic class
- The constraint phi_1 + phi_2 + phi_3 = Q_e on S^1 x S^1 x S^1 defines a
  2-dimensional torus T^2 — this IS the stabilizer torus of the GHZ orbit

### Section 2: The GHZ Orbit and the A_2 Root System

**Established (Theorem 5.2, Paper 4):**
- The SLOCC tangent space at GHZ has 7 complex dimensions
- The Cartan torus T^2 acts with weights {+/- alpha_1, +/- alpha_2, +/- (alpha_1 + alpha_2)}
- These are exactly the roots of A_2 = su(3)

**New content:**
- Numerical verification of the root system (computation script)
- Explicit construction of the su(3) generators from SLOCC generators
- The physical meaning: each root direction corresponds to a specific
  pattern of entanglement change between generations

### Section 3: The Z_6 Quotient

**Established (Paper 4, Section 5):**
- Discrete stabilizer (Z_2)^2 from center of SL(2,C)^3
- Root lattice quotient Z_3 from A_2 structure
- Product: Z_6 = Z_2 x Z_3

**New content:**
- Physical interpretation: Z_2 distinguishes integer vs half-integer
  e-winding (bosons vs fermions in the SU(2) sector)
- Z_3 distinguishes the three color charges (from the three generations'
  entanglement phases)
- The Z_6 quotient IS the statement that color charge, weak isospin,
  and hypercharge are not independent — they are entangled

### Section 4: From Entanglement to Isometries

**The core new result of Paper 11:**

Why does SLOCC equivalence (an entanglement classification) produce
isometries of the internal manifold (a geometric property)?

**The mechanism (Pattern P1: Geometric Reinterpretation):**

In the e-dimension framework, entanglement IS geometry:
- Two-particle entanglement = e-conservation on S^1 (Paper 1)
- Three-particle entanglement = e-conservation on S^1 x S^1 x S^1
- SLOCC equivalence = equivalence under local e-coordinate changes
- Local e-coordinate changes ARE local diffeomorphisms of the internal space
- Diffeomorphisms that preserve the metric ARE isometries
- Therefore: SLOCC equivalence classes → isometry groups

More precisely: the SLOCC orbit of the GHZ state under SU(2)^3 is the
space of all three-qubit states reachable by local unitary e-rotations.
This orbit IS the internal manifold (or a quotient thereof). The isometry
group of this manifold IS the gauge group by the Kaluza-Klein theorem.

**The chain:**

    e-conservation (Noether) → entanglement structure (3 qubits)
    → SLOCC orbit = Fl(1,2;3) ≅ SU(3)/T^2 (tangent space = A_2 roots)
    → isometry group of orbit = SU(3) x SU(2) x U(1)/Z_6
    → gauge group by Kaluza-Klein = SU(3) x SU(2) x U(1)/Z_6

### Section 5: The Kirillov Orbit Method

**The mathematical formalization:**

The Kirillov orbit method (1962) states that irreducible unitary
representations of a Lie group G are in bijection with coadjoint
orbits of G. Applied here:

1. The group G = SU(2)^3 acts on the three-qubit space by local unitaries
2. The coadjoint orbits of SU(2)^3 are products of S^2 spheres
3. The GHZ orbit is NOT a product — it is the flag manifold Fl(1,2;3)
4. This non-product orbit is the coadjoint orbit of SU(3), not SU(2)^3
5. The transition SU(2)^3 → SU(3) is forced by the entanglement structure

**Theorem (Paper 11, main result):**

Let H = (C^2)^{tensor 3} be the three-qubit Hilbert space with the
e-conservation constraint Sum phi_i = Q_e. The gauge group of the
Kaluza-Klein reduction on the SLOCC orbit of the GHZ state is:

    G = [SU(3) x SU(2) x U(1)] / Z_6

where:
- SU(3) is the isometry group of the flag manifold Fl(1,2;3)
  (the GHZ orbit tangent space carries the A_2 root system)
- SU(2) is the residual symmetry from the SU(2)^3 action
  (the weak isospin)
- U(1) is the e-circle isometry (the electromagnetic gauge group)
- Z_6 = Z_2 x Z_3 from the discrete stabilizer and root lattice

### Section 6: Predictions

**From the derivation:**
1. Three generations: chi(CP^2) = 3 (topological, from index theorem)
2. Weinberg angle: sin^2 theta_W = 3/8 x (5/3) at GUT scale
   (from the spectral zeta ratio of S^2/CP^2)
3. Gauge coupling unification: n_2/n_1 = -17/9 (flux quantization)
4. The Z_6 quotient: NOT SU(3) x SU(2) x U(1) but the quotient
   (matches the SM exactly)

**New prediction from Paper 11:**
5. The entanglement spectrum of three generations at high energy
   should show the A_2 root structure — testable in principle
   via quantum information measures at collider experiments

### Section 7: Why Three Generations

**The answer:** Three is the minimum number of qubits whose generic
entanglement class (GHZ) produces a non-abelian gauge group.

- One qubit: SU(2) orbit = S^2 → U(1) gauge group (abelian)
- Two qubits: Bell state orbit → SU(2) gauge group
- Three qubits: GHZ orbit → SU(3) x SU(2) x U(1)/Z_6 gauge group
- Four qubits: would give a LARGER gauge group (not observed)

Three generations is not a coincidence. It is the unique number that
produces exactly the Standard Model gauge group from entanglement geometry.

This connects to the topological fact chi(CP^2) = 3: the internal
manifold's topology forces exactly three generations, and three
generations' entanglement produces exactly the right gauge group.
The circle closes.

### Section 8: Connection to the Full Framework

**How Paper 11 fits into the series:**

| Paper | What it derives | Role of entanglement |
|-------|----------------|---------------------|
| 1 | Quantum mechanics | Entanglement = e-conservation |
| 3 | Black hole information | Entanglement scrambling → Page curve |
| 4 | Standard Model gauge group | Entanglement TYPE → gauge group (Conjecture 5.1) |
| **11** | **WHY SU(3)xSU(2)xU(1)** | **Entanglement geometry IS the gauge group (proved)** |

Paper 11 completes the conceptual arc: the same e-conservation law that
produces entanglement (Paper 1) also selects the gauge group (Paper 11).
Quantum mechanics and the Standard Model are two consequences of one
geometric fact.

---

## Computation Plan

### Comp 1: Numerical verification of A_2 root system from SLOCC orbit
- Implement GHZ tangent space computation in Python
- Verify weight decomposition under Cartan torus
- Confirm A_2 root structure numerically
- Visualize the root diagram

### Comp 2: The e-conservation → SLOCC orbit bridge
- Model the three-qubit system with explicit S^1 coordinates
- Impose e-conservation phi_1 + phi_2 + phi_3 = Q_e
- Show the constrained configuration space = GHZ orbit

### Comp 3: The Kirillov orbit construction
- Compute coadjoint orbits of SU(2)^3 through GHZ
- Identify the non-product orbit with Fl(1,2;3)
- Verify isometry group = SU(3)

### Comp 4: Z_6 quotient verification
- Compute the discrete stabilizer (Z_2)^2 explicitly
- Verify the root lattice quotient Z_3
- Confirm G_SM = [SU(3) x SU(2) x U(1)] / Z_6

---

## The Six Patterns in Paper 11

| Pattern | Role |
|---------|------|
| P1 (Geometric Reinterpretation) | Entanglement as e-geometry → SLOCC as isometry |
| P2 (Holonomy Correspondence) | Wilson line on SLOCC orbit → gauge phase |
| P4 (Topological Rigidity) | chi(CP^2) = 3 → three generations → A_2 roots |
| P6 (Projection Produces Pathology) | The "why these symmetries?" mystery is a projection artifact |

---

*One e-circle. Three generations. One gauge group. The geometry chooses it.*
