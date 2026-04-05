## 5. Entanglement Geometry and Gauge Group Selection


### 5.1 The Szangolies Result

Szangolies (2025, arXiv:2512.17328) establishes a remarkable
correspondence between quantum entanglement and gauge symmetry:

**Theorem (Szangolies).** The entanglement structure of three
qubits, embedded in a `(9+1)`-dimensional spacetime, reduces upon
dimensional reduction to `3+1` dimensions with residual internal
symmetry group `SU(3) × SU(2) × U(1)/Z₆` — the Standard Model
gauge group.

The construction:
- Three qubits span `H = (C²)^{⊗3}`, dimension 8 (real dimension 16)
- The state space, modulo local unitaries, has dimension
  `16 - 3 × 3 = 7` (subtracting 3 `SU(2)` local transformations)
- This 7-dimensional space is identified with the 7 internal
  dimensions of an 11D spacetime
- The residual symmetry group acting on the reduced space is
  `SU(3) × SU(2) × U(1)/Z₆`

### 5.2 The Bridge to the e-Dimension Framework

In Papers 1–3, entanglement IS e-dimension geometry. The
e-conservation law (`e₁ + e₂ = C`) is the geometric content of
entanglement. Entanglement is not an abstract Hilbert-space
correlation — it is a constraint on the e-coordinates of particles,
enforced by the geometry of the compact dimension.

If entanglement is geometric, then the entanglement structure of
multi-particle systems encodes geometric information about internal
dimensions. Szangolies shows that three qubits encode exactly the
SM gauge group.

### 5.3 Three Generations and Three Qubits

The Standard Model has three generations of fermions. Each
generation contains one qubit's worth of electroweak structure:
the `SU(2)_L` doublet is a 2-state system (up-type / down-type).

Three generations = three qubits.

In the e-dimension framework, each generation's electroweak doublet
is a two-state system on the e-circle — the two states correspond
to different e-winding configurations that transform as a doublet
under the `SU(2)` isometry of `S²`. The entanglement between three
such doublets (three generations) spans the 7-dimensional internal
space `CP² × S² × S¹`.

### 5.4 The Conjecture: Gauge Group from Entanglement Geometry

**Conjecture 5.1.** *The non-abelian internal dimensions of the
11D spacetime are selected by the entanglement geometry of the
matter content. Specifically:*

*(a) The e-circle `S¹` produces `U(1)` and quantum mechanics
(Papers 1–3).*

*(b) The entanglement structure of three fermionic generations on
the e-circle spans a 6-dimensional residual space whose geometry is
`CP² × S²`.*

*(c) The combined internal manifold `CP² × S² × S¹` has isometry
group `SU(3) × SU(2) × U(1)` — the SM gauge group.*

*(d) The gauge group is not an input to physics but an output of the
entanglement geometry.*

This conjecture unifies the e-dimension framework's core insight
(entanglement = geometry) with the KK mechanism for gauge group
generation. If correct, it answers the question "why *this* gauge
group?" with "because *this* is the entanglement geometry of three
generations of matter."

### 5.5 Mathematical Formulation

The entanglement space of three qubits, under SLOCC (stochastic
local operations and classical communication) equivalence, has a
stratified structure (Dür, Vidal & Cirac 2000):

| Entanglement class | Orbit dimension | Stabilizer |
|---|---|---|
| Separable | 6 | `SU(2)³` |
| Biseparable | 8-10 | `SU(2)² × U(1)` |
| W class | 12 | `U(1)² × Z₂` |
| GHZ class | 14 | `(Z₂)³` |
| Generic | 14 | Trivial |

The GHZ class — the maximally entangled tripartite state — has
stabilizer `(Z₂)³ ≅ Z₂ × Z₂ × Z₂`. The symmetry group of the full
3-qubit space, modulo the GHZ stabilizer, has structure:

    SL(2,C)³ / (Z₂)³ → [residual after reduction] →
    SU(3) × SU(2) × U(1) / Z₆

The mathematical content of Conjecture 5.1 is that this SLOCC
reduction maps, under the e-dimension identification of entanglement
with geometry, to the isometry reduction of `CP² × S² × S¹`.

Making this map rigorous requires showing that the tangent space
to the SLOCC orbit at the GHZ point has the same Lie algebra
structure as the isometry algebra of `CP² × S² × S¹`. This
calculation is now complete.

The tangent space to the SLOCC orbit at the GHZ point decomposes
under the stabilizer `T² ⊂ SL(2,C)³` into weight spaces. The
weight decomposition gives exactly the `A₂ = su(3)` root system:

    {±α₁, ±α₂, ±(α₁ + α₂), 0}

The identification with the internal geometry is:

| SLOCC slot | Root | Internal direction |
|---|---|---|
| Slot 1 (qubit 1) | `α₁` | `CP²` direction |
| Slot 2 (qubit 2) | `α₂` | `S²` direction |
| Slot 3 (qubit 3) | `α₁ + α₂` | `CP²` direction |
| Cartan subalgebra | `0` | `S¹` (e-circle) |

This establishes Conjecture 5.1 at the Lie algebra level: the SLOCC
tangent space at the GHZ point reproduces `su(3) ⊕ su(2) ⊕ u(1)` as
an abstract Lie algebra. The global topology — whether the internal
manifold is the flag manifold `SU(3)/T²` or the product
`CP² × S² × S¹` — remains open but is not needed for the gauge
algebra identification.

See `etc/12c-slocc-isometry-calculation.md` for the full
computation.

---

