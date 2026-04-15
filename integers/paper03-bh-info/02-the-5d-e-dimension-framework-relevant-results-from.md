## 2. The 5D e-Dimension Framework — Relevant Results from Paper 1


We summarize the elements of Paper 1 required for the information
paradox argument. Full derivations are given in Paper 1.

### 2.1 The Five Coordinates

Physical reality has five dimensions: `(x, y, z, t, e)`. The fifth
dimension `e` is a circle — periodic, parameterized by an angle
`φ ∈ [0, 2π)` — with structure group `U(1)`. It is a spacelike
direction in the 5D Lorentzian metric `ds² = g_{μν}dx^μ dx^ν +
R₀² dφ²`, participating in the 5D null-cone condition in the standard
way. What distinguishes the e-direction from the four ordinary
spacetime dimensions is not the absence of a causal structure
(every spacelike direction participates in the light cone) but the
non-dynamical character of its zero-mode. The background value of φ
— the KK zero-mode, constant around the circle — is not a propagating
field. It is determined, at every point of the evaporation history,
by the algebraic e-conservation constraint `Σ φᵢ = C` (Section 2.2).
Changes in this background value are not causal propagation events;
they are instantaneous rearrangements of a conserved charge, analogous
to the instantaneous adjustment of all momenta in a system when a
single particle is created or destroyed. KK excitations of φ — the
`n ≠ 0` modes — are dynamical fields that propagate at subluminal
speeds with mass `m_n = nℏ/(cR₀)`. The non-dynamical character
refers exclusively to the zero-mode (`n = 0`) background geometry,
not to the full tower of KK modes.

### 2.2 The e-Conservation Law

In any interaction, the total e-coordinate is conserved:

    φ₁ + φ₂ + ... + φₙ = C  (constant)

This follows from e-translation invariance by Noether's theorem
(Paper 1, Section 2.2.3). It is the geometric basis of quantum
entanglement.

### 2.3 The Wave Function as 5D Geometry

The quantum wave function `ψ(x, y, z, t) = A · e^{iφ}` is not an
abstract probability amplitude. The phase `φ` is the e-coordinate.
The amplitude `A` is the 4D projection of the 5D density. Information
about a quantum state lives in the 5D structure — including, and
especially, in the e-coordinate.

### 2.4 The Zero-Mode as a Non-Dynamical Geometric Variable

The KK decomposition of any 5D field is `Φ(x,φ) = Σ_n Φ_n(x) e^{inφ/R₀}`.
The `n = 0` mode `Φ₀(x)` is the 4D-observable projection; the `n ≠ 0`
modes are massive KK excitations with masses `m_n = n/R₀`, propagating
in 4D at subluminal speeds (Paper 1, §4.3, propagator bounds
`|g_b| ≤ C₀ e^{−m₁a}`).

The e-coordinate shift `δφ` discussed throughout this paper is a change
in the `n = 0` background geometry — not a KK mode excitation. A
background geometry change is not subject to propagator bounds; those
bounds govern the propagation of fluctuations around a background, not
changes in the background itself. The physical analogy: shifting the
vacuum expectation value `⟨Φ⟩` changes the masses of all particles
coupled to Φ (via `m = g⟨Φ⟩`), but this shift is not subject to
the propagation bound of any single particle excitation.

The e-conservation constraint `Σ φᵢ = C` is an operator constraint on
the `n = 0` sector of the e-Hilbert space. When one term changes (a
quantum is absorbed by the horizon, shifting `φ_{horizon}`), all other
terms are constrained by the algebraic identity — not by any
propagating signal. This is the structure of a superselection rule,
formalized in Section 9.3.1 (Properties 1–3), not the structure of
a field propagating faster than light.

Precision statement replacing the earlier informal language: *The
`n = 0` zero-mode of the e-coordinate is a non-dynamical geometric
variable whose changes are determined by the algebraic e-conservation
constraint, not by a differential equation of motion in spacetime.
The 5D Lorentzian metric has a complete causal structure. The e-circle
is a spacelike direction within it. What is non-dynamical is the
background fiber geometry, not the full 5D theory.*

The KK propagator bounds of Paper 1 (§4.3, `|g_b| ≤ C₀ e^{−m₁a}`)
describe the propagation of massive KK mode excitations — the `n ≠ 0`
fields `Φ_n(x)` — through the 4D base. These are dynamical degrees of
freedom, and their propagation is subluminal with exponential
spatial decay at distances `a >> R₀`. The e-coordinate shift `δφ`
discussed in this paper is not a KK mode excitation. It is a change
in the background fiber geometry — the value of the `n = 0` Noether
charge at the horizon — around which the KK modes are defined.
The propagator bounds apply to fluctuations around a background;
they say nothing about a change in the background itself. A helpful
analogy: the Yukawa potential bound on a massive scalar mediator
(exponential suppression for distances `r >> 1/m`) does not constrain
how fast the scalar's vacuum expectation value can shift — VEV shifts
are background rearrangements, not particle-exchange events.

**Precision: quantum-operator status of the zero-mode.** The zero-mode φ₀ is a
quantum operator — the zero-mode projection of the e-coordinate field operator
Φ(x,φ) onto the n = 0 KK sector. Its canonical conjugate is the zero-mode momentum
operator p̂₀ = ℏ Q̂_e / R₀, where Q̂_e is the conserved e-charge (§9.3.1). The
Hilbert space is the KK Fock space H₅D = ⊕_Q H_Q — the direct sum over
superselection sectors, each labeled by total e-charge eigenvalue Q (§9.3.1,
Property 3). The "algebraic e-conservation constraint" Σ φᵢ = C is the operator
statement that Q̂_e is conserved: [Q̂_e, Ĥ₅D] = 0 (Property 1). It is an operator
equation in H₅D, not a classical background condition. Within each sector H_Q, the
e-charge eigenvalue Q is fixed. Absorbing an infalling quantum with e-coordinate
φ_in does not propagate any excitation through H₅D — it places the post-absorption
state in the sector H_{Q + φ_in}. This transition is determined by the conservation
law (which sector is correct), not by a differential equation in spacetime (how the
transition propagates). The non-dynamical character of the zero-mode refers precisely
to this: the zero-mode label Q is updated by sector selection, not by a field
equation. The KK propagator bounds of §4.3 govern excitations *within* a sector H_Q —
fluctuations around a background with fixed Q. They say nothing about which sector
the system is in.

### 2.5 Perturbative Finiteness

The 5D Einstein-Hilbert action on `M⁴ × S¹`, under zeta
regularization of the KK mode sums, is perturbatively finite at
every loop order (Paper 1, Appendices F, G, K, S). The compactness
of the e-circle converts continuous UV momentum integrals into
discrete sums that admit zeta regularization, with the leading
divergence vanishing identically: `S₀^{(L)} = [1 + 2ζ(0)]^L = 0`.
This establishes the 5D framework as a perturbatively consistent
quantum theory of gravity — the prerequisite for any meaningful
statement about unitarity in black hole evaporation.

### 2.6 ER = EPR as e-Dimension Tubes

Paper 1 Section 6.1 established that entangled particles are
connected through the e-dimension. The Einstein-Rosen bridge is the
e-space tube along which the conservation constraint `e₁ + e₂ = C`
propagates. This gives the ER=EPR conjecture (Maldacena & Susskind
2013) a specific geometric mechanism in the 5D framework.

---

