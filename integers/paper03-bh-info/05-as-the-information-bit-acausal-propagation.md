## 5. δφ as the Information Bit — Non-Dynamical Propagation in e


### 5.1 The Global Effect of a Local Change

A sphere has a specific geometric property: the normals to its
surface at every point all pass through the center. The sphere is
a unified geometric object — a global structure, not a collection
of independent local pieces.

When the e-coordinate of one Planck pixel on the horizon shifts by
`δφ`, this is a change in the geometry of `S² × S¹`. The e-bundle
over the horizon is a geometric structure — a connection on a
principal U(1) bundle over S². A shift in the e-coordinate at one
fiber affects the holonomy around every loop on S² that passes
through that fiber. The full e-bundle structure is modified.

This is the geometric statement underlying the disco ball intuition:
adding one mirror tile to a disco ball changes the entire light field
in the room, not just the patch directly illuminated by the new tile.

### 5.2 Non-Dynamical Propagation in e

The e-coordinate shift `δφ` modifies the e-bundle geometry of the
entire horizon surface simultaneously. This is not propagation of
a signal — it is a change in a boundary condition.

Precisely: the e-circle is a fiber in a principal bundle over
spacetime M⁴. The e-coordinate `φ(x)` at each point `x ∈ M⁴` is
a section of this bundle. When a section changes, it changes as
a geometric fact about the bundle — not as a dynamical process
propagating from one spacetime point to another.

The correct framing is not "instantaneous propagation" — that
language implies a signal traveling faster than light, which is
misleading. The correct framing is: **the e-coordinate is a
non-dynamical geometric variable.** It has no equation of motion
of its own — it is constrained by the e-conservation law, which
is an algebraic constraint, not a differential equation in
spacetime.

The analogy is not to a signal propagating, but to a gauge choice:
when you fix a gauge in electromagnetism, the gauge field changes
everywhere simultaneously — not because information traveled, but
because gauge fixing is a constraint on the configuration space,
not a dynamical process.

The gauge-fixing analogy captures the *acausal* character of δφ
propagation accurately — it is a constraint on the configuration
space, not a dynamical process in spacetime. But the analogy has a
limit that must be stated. In gauge theory, the gauge degree of
freedom is unphysical — pure redundancy with no observable
consequences. The e-coordinate is not redundant. It is physically
meaningful: it determines the quantum phase of a particle (Paper 1,
§2.3), its statistics under exchange (Paper 1, Appendix B), and
through e-conservation, its entire interaction history. What is
acausal is not a gauge artifact but a genuine Noether charge.

The correct framing is this: δφ is a Noether charge evaluated on a
compact dimension, and Noether charges are global quantities. When the
total momentum of a system changes — because a particle is created or
absorbed — the momentum of every other particle in the system is
immediately constrained by conservation. There is no signal. There is
no propagation. There is only the algebraic fact that a conserved
quantity has a definite total value, and a change in one term
constrains all others simultaneously. The acausality of δφ is exactly
this — not the FTL transfer of information, but the global character
of Noether conservation. The locality is in the *encoding*: one Planck
pixel absorbs one infalling quantum and acquires one unit of e-imprint.
The *constraint* that follows is global, just as conservation of
energy is global — it holds everywhere, not because a signal traveled,
but because it is an algebraic identity on the state space.

**What is claimed:** The e-conservation constraint `Σ φ_i = C`
implies that a change in one e-coordinate immediately constrains
all others. This is algebraic, not causal.

**What this does NOT claim:** That any physical signal travels
faster than light. The e-coordinate shift is invisible to 4D
observers (Section 5.3) and cannot be used to transmit information.

**What requires further development:** A precise statement of the
Hilbert space structure in which e-conservation is an operator
constraint, analogous to the Gauss law constraint in gauge theories.
This is identified as an open problem (see §9.3).

### 5.3 No Violation of Causality

It is essential to note that this non-dynamical e-geometry does
not permit faster-than-light communication. The shift `δφ` is in
the e-dimension, invisible to 4D observers. An external observer
cannot use the δφ change to send a signal — they cannot
detect `δφ` directly. The 4D projected Hawking radiation remains
thermal, causally consistent, and indistinguishable from Hawking's
original prediction to any 4D measurement.

The e-information is present. It is not accessible to 4D detectors.
This is the same structure as entanglement: the e-conservation
constraint is real, but measuring it requires access to the
e-dimension, which 4D observers do not have directly.

The argument that `[Q̂_e, Ô_{4D}] = 0` (Section 9.3.1, Property 2)
relies on 4D observables being KK zero-modes. Massive KK modes
(`n ≠ 0`) carry e-charge and could in principle provide a channel
through which e-information leaks into 4D-accessible observables.
This channel is thermally suppressed for all astrophysical black holes.
The lightest KK mode has mass `m₁ = ℏc/(R₀) ~ 10⁻² eV` for
`R₀ ~ 12 μm`, corresponding to a temperature scale `T₁ = m₁c²/k_B ~ 100 K`.
The Hawking temperature of a solar-mass black hole is `T_H ~ 10⁻⁷ K`,
nine orders of magnitude below T₁. The thermal production rate of
the lightest KK mode is `Γ ~ exp(−m₁c²/k_B T_H) ~ exp(−10⁹)` —
negligible by any standard. For black holes with `M >> M_Pl`, we
always have `T_H << m₁/k_B` (the KK mass far exceeds the thermal
scale), so the `n ≠ 0` sector is dynamically inaccessible and the
4D observables are genuinely restricted to the zero-mode sector.
The no-signaling argument is complete in this astrophysical regime.
For `M ~ M_Pl`, `T_H ~ m₁/k_B` and the KK modes are produced, but
at that scale the semi-classical approximation itself breaks down
— the AMPS argument, and indeed the Hawking calculation, are not
reliable there anyway.

**Explicit no-signaling theorem.** Consider two spacelike-separated observers A and
B who share an e-entangled state ρ_5D (a state in a definite superselection sector
H_Q with e-correlations between their respective subsystems). Observer B performs an
arbitrary e-sector operation E_B on their subsystem. The claim is that A's 4D
measurement statistics are unaffected.

*Proof.* A's 4D measurement statistics are determined entirely by A's 4D marginal
state ρ_A^{4D} = Tr_{e,B-sys}[ρ_5D], where the trace is over the e-sector and B's
entire subsystem. After B's operation E_B, the global state becomes
ρ'_5D = (id_A ⊗ E_B)[ρ_5D]. Then

    ρ_A^{4D,after} = Tr_{e,B-sys}[(id_A ⊗ E_B)[ρ_5D]].

By Property 2 (§9.3.1), all 4D observables Ô₄D on A's system commute with Q̂_e:
[Q̂_e, Ô₄D] = 0. This means Ô₄D acts only on the zero-mode sector of A's Hilbert
space — it is e-sector blind. Therefore Ô₄D is insensitive to any operation E_B
that acts only on the e-sector of B's subsystem. Explicitly:

    Tr[ρ_A^{4D,after} Ô₄D] = Tr[ρ_5D (Ô₄D ⊗ E_B†)]
                              = Tr[ρ_5D (Ô₄D ⊗ id_e)] × Tr_e[E_B† / dim(H_e)]
                              = Tr[ρ_A^{4D} Ô₄D]

since Ô₄D ⊗ E_B† = Ô₄D ⊗ id_e when the observable Ô₄D commutes with all e-sector
operators. No 4D measurement by A can detect B's e-sector operation. No e-sector
information transfer is observable through 4D measurements. No signaling. ∎

This argument holds for arbitrary e-sector operations E_B, including non-unitary ones
(e.g., B measuring and post-selecting on the e-sector). The no-signaling conclusion
is unconditional within the semiclassical regime M >> M_Pl where Property 2 holds.

### 5.4 How the Global Constraint Distributes: From Conservation to Imprint

Section 4.3 derives that the total horizon e-charge shifts by
`δφ = φ_{infalling}` when one bit falls in. Section 7 requires that
this shift is distributed across the individual Planck pixels in a
way that allows the Page curve to be derived. We now make this
distribution precise.

**The state of the horizon e-sector.** Before the infalling quantum
arrives, the horizon consists of `N_BH` Planck pixels with e-coordinates
`{φ₁, φ₂, ..., φ_{N_BH}}`. The e-conservation constraint fixes the
total: `Σᵢ φᵢ = Q_{before}`.

After the infalling quantum (e-coordinate `φ_{in}`) is absorbed,
the new total is `Q_{after} = Q_{before} + φ_{in}`. This is a
constraint on the updated pixel configuration `{φ₁', φ₂', ..., φ_{N_BH+1}'}` —
the new pixel created by the Planck area growth joins the surface
with e-coordinate `φ_{new pixel} = φ_{in}` (by local e-conservation
at the absorption vertex, Section 4.3, Theorem 2.1). The other
`N_BH` pixels are not individually updated by the absorption — the
global constraint is satisfied by the creation of the new pixel.

**Interpretation (a) is the correct one for the absorption event.**
The total e-charge changes; the individual pixels are not each
updated; the new pixel carries the infalling e-charge. This is
consistent with the local Noether conservation at the absorption
vertex (Paper 1, Theorem 2.1) and requires no acausal pixel-by-pixel
update.

**The scrambling distributes the imprint.** What converts this
localized new pixel's e-coordinate into a distributed imprint across
all pixels is not the conservation law but the scrambling dynamics.
The horizon is a quantum system in contact with the Hawking thermal
bath at temperature `T_H`. The 4D thermal dynamics cause the horizon's
internal degrees of freedom to mix — to scramble — on the timescale
`t_scr ~ β ln S_BH` (Section 11). After scrambling, the information
about the infalling `φ_{in}` has been distributed across all `N_BH+1`
pixels: no individual pixel carries the original `φ_{in}`, but
correlations among all pixels encode it.

**Precise claim replacing the ambiguous "instantaneous global shift":**

> When a bit falls in, the e-charge of the new horizon pixel is
> locally set to `φ_{in}` by e-conservation at the absorption vertex.
> No other pixel is instantly updated. After the scrambling time
> `t_scr`, the e-information in `φ_{in}` is mixed across all horizon
> pixels by the thermal dynamics, making it available to be encoded
> in subsequent Hawking emissions. The "instantaneous" character of
> e-encoding refers to the local absorption (which happens at the
> vertex, not via a propagating signal), not to an instantaneous
> redistribution across all pixels.

**Consequence for Section 7 (Page curve).** The random-unitary model
of Section 7 applies to the scrambled configuration — after `t_scr`,
not at the moment of absorption. For `k < t_scr/β = O(ln S_BH)`
emissions, the e-configuration has not yet been scrambled and the
random-unitary approximation is not yet valid. The early-time behavior
is treated explicitly in Section 7.7.

---

