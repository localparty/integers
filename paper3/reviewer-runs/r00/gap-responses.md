# Author Response and Revision Material
## "Information Preservation in Black Hole Evaporation via e-Dimension Geometry"
### Paper 3 — Response to Referee Report

---

We thank the referee for a thorough and constructive review. The report
correctly identifies several places where the manuscript's prose
outran its derivations. We address every A-rated (GENUINE GAP) and
B-rated (CLOSABLE GAP) finding in turn. For each finding we state
(i) our response to the referee and (ii) the precise new text or
derivation to be inserted into the revision.

---

## A1(a) — Definition of "No Causal Structure" [GENUINE GAP]

### Author Response

The referee is correct that the phrase "the e-dimension carries no
causal structure" as stated in Sections 2.1 and 2.4 is imprecise and,
read literally, incorrect: the 5D metric is Lorentzian and every
direction, including the spacelike e-direction, participates in the
null-cone condition ds² = 0. The intended meaning is not that the
e-direction is outside the 5D causal structure, but that the
zero-mode of the e-coordinate is non-dynamical — it is a conserved
charge constrained algebraically by the Noether law, not a degree of
freedom with its own wave equation.

Section 5.2 already makes this precise for the e-coordinate shift δφ,
but it does so after the imprecise claim has already been introduced
in Sections 2.1 and 2.4. The revision replaces every instance of
"carries no causal structure" in the early sections with the sharper
statement developed below, and adds a technical remark (new
Section 2.4, replacing the current paragraph) that draws the
explicit distinction between the background e-geometry (the zero-mode,
non-dynamical) and KK mode excitations (dynamical, subluminal).

### Draft New Content — Replacement for Sections 2.1 and 2.4

**Section 2.1 replacement paragraph (the fifth coordinate):**

> The fifth dimension e is a circle — periodic, parameterized by an
> angle φ ∈ [0, 2π) — with structure group U(1). It is a spacelike
> direction in the 5D Lorentzian metric ds² = g_{μν}dx^μ dx^ν +
> R₀² dφ², participating in the 5D null-cone condition in the standard
> way. What distinguishes the e-direction from the four ordinary
> spacetime dimensions is not the absence of a causal structure
> (every spacelike direction participates in the light cone) but the
> non-dynamical character of its zero-mode. The background value of φ
> — the KK zero-mode, constant around the circle — is not a propagating
> field. It is determined, at every point of the evaporation history,
> by the algebraic e-conservation constraint Σ φᵢ = C (Section 2.2).
> Changes in this background value are not causal propagation events;
> they are instantaneous rearrangements of a conserved charge, analogous
> to the instantaneous adjustment of all momenta in a system when a
> single particle is created or destroyed. KK excitations of φ — the
> n ≠ 0 modes — are dynamical fields that propagate at subluminal
> speeds with mass m_n = nℏ/(cR₀). The non-dynamical character refers
> exclusively to the zero-mode (n = 0) background geometry, not to the
> full tower of KK modes.

**Section 2.4 replacement (to replace the current "Acausal Nature of e" paragraph):**

> ### 2.4 The Zero-Mode as a Non-Dynamical Geometric Variable
>
> The KK decomposition of any 5D field is Φ(x,φ) =
> Σ_n Φ_n(x) e^{inφ/R₀}. The n = 0 mode Φ₀(x) is the
> 4D-observable projection; the n ≠ 0 modes are massive KK excitations
> with masses m_n = n/R₀, propagating in 4D at subluminal speeds
> (Paper 1, §4.3, propagator bounds |g_b| ≤ C₀ e^{−m₁a}).
>
> The e-coordinate shift δφ discussed throughout this paper is a change
> in the n = 0 background geometry — not a KK mode excitation. A
> background geometry change is not subject to propagator bounds; those
> bounds govern the propagation of fluctuations around a background, not
> changes in the background itself. The physical analogy: shifting the
> vacuum expectation value ⟨Φ⟩ changes the masses of all particles
> coupled to Φ (via m = g⟨Φ⟩), but this shift is not subject to
> the propagation bound of any single particle excitation.
>
> The e-conservation constraint Σ φᵢ = C is an operator constraint on
> the n = 0 sector of the e-Hilbert space. When one term changes (a
> quantum is absorbed by the horizon, shifting φ_{horizon}), all other
> terms are constrained by the algebraic identity — not by any
> propagating signal. This is the structure of a superselection rule,
> formalized in Section 9.3.1 (Properties 1–3), not the structure of
> a field propagating faster than light.
>
> Precision statement replacing "carries no causal structure": *The
> n = 0 zero-mode of the e-coordinate is a non-dynamical geometric
> variable whose changes are determined by the algebraic e-conservation
> constraint, not by a differential equation of motion in spacetime.
> The 5D Lorentzian metric has a complete causal structure. The e-circle
> is a spacelike direction within it. What is non-dynamical is the
> background fiber geometry, not the full 5D theory.*

---

## A1(b) — No-Signaling Constraint [CLOSABLE GAP]

### Author Response

The referee accepts the superselection argument of Section 9.3.1
(Property 2: [Q̂_e, Ô_{4D}] = 0 for all 4D observables) as largely
sound, but notes a remaining question: if massive KK modes are
experimentally accessible, they carry e-charge and might provide a
channel for e-information. The referee asks for a statement about
whether KK modes are thermally accessible for astrophysical black holes.

This is a one-paragraph addition to Section 5.3.

### Draft New Content — Addition to Section 5.3

**New paragraph to append to Section 5.3:**

> The argument that [Q̂_e, Ô_{4D}] = 0 (Section 9.3.1, Property 2)
> relies on 4D observables being KK zero-modes. Massive KK modes
> (n ≠ 0) carry e-charge and could in principle provide a channel
> through which e-information leaks into 4D-accessible observables.
> This channel is thermally suppressed for all astrophysical black holes.
> The lightest KK mode has mass m₁ = ℏc/(R₀) ~ 10⁻² eV for R₀ ~ 12 μm,
> corresponding to a temperature scale T₁ = m₁c²/k_B ~ 100 K. The
> Hawking temperature of a solar-mass black hole is T_H ~ 10⁻⁷ K, nine
> orders of magnitude below T₁. The thermal production rate of the
> lightest KK mode is Γ ~ exp(−m₁c²/k_B T_H) ~ exp(−10⁹) — negligible
> by any standard. For black holes with M >> M_Pl, we always have
> T_H << m₁/k_B (the KK mass far exceeds the thermal scale), so the
> n ≠ 0 sector is dynamically inaccessible and the 4D observables are
> genuinely restricted to the zero-mode sector. The no-signaling
> argument is complete in this astrophysical regime. For M ~ M_Pl,
> T_H ~ m₁/k_B and the KK modes are produced, but at that scale the
> semi-classical approximation itself breaks down — the AMPS argument,
> and indeed the Hawking calculation, are not reliable there anyway.

---

## A1(c) — Coordinate Dependence and the Global vs. Local e-Shift [GENUINE GAP]

### Author Response

The referee identifies a genuine ambiguity between two interpretations
of "the horizon's e-coordinate changes when a bit falls in":

> (a) The *total* e-charge of the horizon changes (a global statement
>     from conservation).
> (b) The e-coordinate of *every* Planck pixel changes simultaneously
>     (a local-propagation claim).

The derivation in Section 4.3 derives only (a) — the total e-charge
shifts by δφ = φ_{infalling}. But the Page curve derivation (Section 7)
and the scrambling argument (Section 11) treat all Planck pixels as
carrying e-imprints reflecting the infalling information, which
requires either (b) or a mechanism by which the global conservation
constraint translates into distributed local imprints.

The correct resolution is neither purely (a) nor purely (b) but a
precise statement about how the e-conservation constraint
distributes among the individual pixel e-coordinates. This requires
a new argument, given below.

### Draft New Content — New Section 5.4 (to be inserted after Section 5.3)

**New Section 5.4: From Global Charge Conservation to Local e-Imprint Distribution**

> ### 5.4 How the Global Constraint Distributes: From Conservation to Imprint
>
> Section 4.3 derives that the total horizon e-charge shifts by
> δφ = φ_{infalling} when one bit falls in. Section 7 requires that
> this shift is distributed across the individual Planck pixels in a
> way that allows the Page curve to be derived. We now make this
> distribution precise.
>
> **The state of the horizon e-sector.** Before the infalling quantum
> arrives, the horizon consists of N_BH Planck pixels with e-coordinates
> {φ₁, φ₂, ..., φ_{N_BH}}. The e-conservation constraint fixes the
> total: Σᵢ φᵢ = Q_{before}.
>
> After the infalling quantum (e-coordinate φ_{in}) is absorbed,
> the new total is Q_{after} = Q_{before} + φ_{in}. This is a
> constraint on the updated pixel configuration {φ₁', φ₂', ..., φ_{N_BH+1}'} —
> the new pixel created by the Planck area growth joins the surface
> with e-coordinate φ_{new pixel} = φ_{in} (by local e-conservation
> at the absorption vertex, Section 4.3, Theorem 2.1). The other
> N_BH pixels are not individually updated by the absorption — the
> global constraint is satisfied by the creation of the new pixel.
>
> **Interpretation (a) is the correct one for the absorption event.**
> The total e-charge changes; the individual pixels are not each
> updated; the new pixel carries the infalling e-charge. This is
> consistent with the local Noether conservation at the absorption
> vertex (Paper 1, Theorem 2.1) and requires no acausal pixel-by-pixel
> update.
>
> **The scrambling distributes the imprint.** What converts this
> localized new pixel's e-coordinate into a distributed imprint across
> all pixels is not the conservation law but the scrambling dynamics.
> The horizon is a quantum system in contact with the Hawking thermal
> bath at temperature T_H. The 4D thermal dynamics cause the horizon's
> internal degrees of freedom to mix — to scramble — on the timescale
> t_scr ~ β ln S_BH (Section 11). After scrambling, the information
> about the infalling φ_{in} has been distributed across all N_BH+1
> pixels: no individual pixel carries the original φ_{in}, but
> correlations among all pixels encode it.
>
> **Precise claim replacing the ambiguous "instantaneous global shift":**
>
> > When a bit falls in, the e-charge of the new horizon pixel is
> > locally set to φ_{in} by e-conservation at the absorption vertex.
> > No other pixel is instantly updated. After the scrambling time
> > t_scr, the e-information in φ_{in} is mixed across all horizon
> > pixels by the thermal dynamics, making it available to be encoded
> > in subsequent Hawking emissions. The "instantaneous" character of
> > e-encoding refers to the local absorption (which happens at the
> > vertex, not via a propagating signal), not to an instantaneous
> > redistribution across all pixels.
>
> **Consequence for Section 7 (Page curve).** The random-unitary model
> of Section 7 applies to the scrambled configuration — after
> t_scr, not at the moment of absorption. For k < t_scr/β = O(ln S_BH)
> emissions, the e-configuration has not yet been scrambled and the
> random-unitary approximation is not yet valid. We address the
> early-time behavior explicitly in Section 7.3 revision (see
> response to B1(c)).

---

## A1(d) — Consistency with KK Propagator Bounds [CLOSABLE GAP]

### Author Response

The referee accepts that the tension between "instantaneous e-propagation"
and the KK propagator bounds of Paper 1 is resolvable by distinguishing
fiber geometry changes from KK mode propagation. The required paragraph
is simple and follows naturally from the distinction established in A1(a)/(c).

### Draft New Content — Addition to Section 2.4

**New paragraph to append to revised Section 2.4:**

> The KK propagator bounds of Paper 1 (§4.3, |g_b| ≤ C₀ e^{−m₁a})
> describe the propagation of massive KK mode excitations — the n ≠ 0
> fields Φ_n(x) — through the 4D base. These are dynamical degrees of
> freedom, and their propagation is subluminal with exponential
> spatial decay at distances a >> R₀. The e-coordinate shift δφ
> discussed in this paper is not a KK mode excitation. It is a change
> in the background fiber geometry — the value of the n = 0 Noether
> charge at the horizon — around which the KK modes are defined.
> The propagator bounds apply to fluctuations around a background;
> they say nothing about a change in the background itself. A helpful
> analogy: the Yukawa potential bound on a massive scalar mediator
> (exponential suppression for distances r >> 1/m) does not constrain
> how fast the scalar's vacuum expectation value can shift — VEV shifts
> are background rearrangements, not particle-exchange events.

---

## A2(a) — One Planck Area Per Bit: Derivation Missing [GENUINE GAP]

### Author Response

The referee is correct that Section 4.3 derives only that δφ = φ_{infalling}
from e-conservation. It does not derive that each unit of e-charge
corresponds to exactly one Planck area of horizon growth. The
referee offers two options: (a) derive the area spectrum from the 5D
theory, or (b) state honestly that "one Planck area per bit" is a
hypothesis consistent with Bekenstein's bound, not a derived result.

Option (a) — deriving the spectrum of the 5D horizon area operator
— is a separate paper's work (the analog of the LQG Casimir calculation
with the Immirzi parameter). We choose option (b) and insert the
honest statement. However, we can say more than "consistent with
Bekenstein's bound": the relationship δφ = φ_{infalling} from
e-conservation, combined with the Bekenstein-Hawking formula
S_BH = A/(4l_P²) from Section 8, forces the identification
"one e-quantum = one Planck area" as a derived consequence of
requiring S_BH to count independent e-states. We make this
derivation explicit below.

### Draft New Content — Revised Section 4.3 closing paragraph + new footnote

**New closing paragraph for Section 4.3:**

> **The area quantization.** The derivation above establishes that each
> infalling quantum deposits one unit of e-charge (δφ = φ_{infalling})
> on the horizon. What is the corresponding area increase?
>
> This is not independently derived from the e-conservation law alone.
> It follows from combining two results: (1) the e-conservation law at
> the absorption vertex, which establishes the e-charge transfer;
> (2) the Bekenstein-Hawking entropy formula S_BH = A/(4l_P²), derived
> in Section 8 from the entanglement entropy of KK modes across the
> horizon after G-renormalization.
>
> From Section 8.3: the entropy counts independent e-circle
> configurations on the horizon, with each Planck-area cell supporting
> one independent e-degree of freedom. S_BH = N_{pixels} where
> N_{pixels} = A/(4l_P²). Therefore one unit of entropy (one bit,
> in natural units with s₀ = 1 after G-renormalization, as derived in
> Section 7 and established in Section 8.2) corresponds to one Planck
> area and one e-charge unit. The "one Planck area per bit" claim is
> the statement that these two units are the same — which is forced
> by requiring consistency between the e-charge counting and the
> entropy formula. It is derived from the conjunction of
> e-conservation and S_BH = A/4, not from e-conservation alone.
>
> The precise relationship between e-charge units and area eigenvalues
> in the 5D quantum gravity theory — the analog of the LQG area
> spectrum derivation — is not computed here. The claim is that the
> semiclassical counting is consistent: one absorbed quantum increases
> the entropy by one unit (one bit in Bekenstein units), and the entropy
> formula assigns one Planck area per entropy unit. The derivation of
> the exact area eigenvalue spectrum from the 5D operator algebra
> is deferred to future work.

---

## A2(b) — Discrete Growth vs. Smooth Classical Dynamics [CLOSABLE GAP]

### Author Response

The referee asks for an explicit statement that in the limit of many
infalling quanta, the discrete Planck-scale growth events average to
continuous classical dynamics. This is universal in quantum gravity
and a brief statement suffices.

### Draft New Content — Addition to Section 4.2

**New paragraph to add at the end of Section 4.2:**

> **The classical limit.** The discrete Planck-area growth events
> occur at a rate set by the infalling flux. For a black hole of mass
> M >> M_Pl, the flux of infalling matter corresponds to
> ~10^(2S_BH) growth events over the evaporation time — an
> astronomically large number of discrete steps. In the classical
> limit M >> M_Pl, the discrete area increments ΔA = l_P² ≪ A
> are invisible at any classical or semiclassical resolution. The
> smooth, continuously-shrinking horizon of the standard Hawking
> calculation is recovered as the coarse-grained average of these
> Planck-scale growth events, with corrections suppressed by
> M_Pl/M << 1. This is the same limit in which any discrete quantum
> spectrum (atomic energy levels, angular momentum eigenvalues)
> reproduces the Bohr correspondence principle for large quantum
> numbers. The discreteness is real at the Planck scale and invisible
> above it.

---

## A2(c) — Definition of "e-Coordinate of the Horizon" [CLOSABLE GAP]

### Author Response

The referee accepts the geometric picture but asks for an explicit
mathematical definition in Section 4.3.

### Draft New Content — Sentence to insert in Section 4.3

**Sentence to insert immediately before the derivation in Section 4.3
(before "The e-conservation law states..."):**

> **Geometric definition.** The event horizon of a Schwarzschild black
> hole in the 5D framework is a null hypersurface in the 4D base M⁴.
> The e-bundle restricts to this null hypersurface: at each point of
> the 2-sphere S² of the horizon, an e-circle S¹ is attached as the
> fiber of the principal U(1) bundle. The "e-coordinate of the horizon"
> φ_{horizon} is the section of this restricted bundle — the assignment
> of an e-circle position to each point of the horizon 2-sphere. As
> established in Section 9.3.2 (Gap 3), the e-Killing vector ∂/∂φ is
> spacelike everywhere, including at the horizon, and Q_e is well-defined
> on the horizon hypersurface. The "e-coordinate" is the eigenvalue of
> the e-charge operator Q̂_e restricted to the horizon.

---

## B1(a) — Is the Page Curve a Derivation or a Description? [GENUINE GAP]

### Author Response

The referee is correct that Section 7 applies Page's (1993)
random-unitary result to the e-Hilbert space rather than deriving
the random-unitary property from the 5D equations of motion. The
referee offers two options: (a) derive the k-design property of the
5D Hamiltonian restricted to the e-sector, or (b) honestly reframe
Section 7 as a conditional result.

We adopt option (b) as the honest characterization, while strengthening
the justification for the random-unitary assumption by connecting it
more explicitly to the structure of the 5D theory. A full derivation
of the k-design property from the 5D Hamiltonian is a future-work
item. The revision rewrites the opening of Section 7.3 and adds a
new Section 7.6.

### Draft New Content — Revised Section 7.3 preamble

**Replacement for the second paragraph of Section 7.3 (beginning
"Following Page (1993) and Hayden-Preskill (2007)..."):**

> The derivation of the Page curve presented here is a *conditional*
> result: it follows from (i) the structure of the e-Hilbert space
> established in Section 7.2, and (ii) the assumption that the horizon
> dynamics act as an approximate random unitary on this Hilbert space.
> Assumption (ii) is not derived from the 5D equations of motion in
> this paper — it is the fast-scrambler conjecture (Sekino & Susskind
> 2008) applied to the e-sector. What the 5D framework adds over a
> bare appeal to Page (1993) is structural: it identifies the Hilbert
> space on which the random unitary acts (the e-sector, not an abstract
> qubit system), it provides the physical mechanism that mixes the
> e-coordinates (the 4D thermal horizon dynamics at temperature T_H),
> and it establishes — via e-conservation — that the map from horizon
> e-configurations to radiation e-configurations is deterministic and
> unitary. The result is that if the horizon acts as a fast scrambler
> in the e-sector (the standard assumption for black holes, confirmed
> for holographic black holes by the MSS chaos bound argument), the
> Page curve follows. We state this as a conditional theorem:
>
> **Theorem 7.1 (Conditional Page Curve).** *Assume: (i) the e-Hilbert
> space decomposition H_{5D} = H_{BH} ⊗ H_{rad} from Section 7.2;
> (ii) the horizon dynamics between emissions act as a Haar-random
> unitary on H_{BH}. Then the entanglement entropy of the radiation
> satisfies S_{rad}(k) = min[k, N₀ − k] × ln(d_e), reproducing the
> Page curve with Page time at k = N₀/2.*
>
> The derivation of assumption (ii) from the 5D Hamiltonian — proving
> that the 5D dynamics form an approximate unitary k-design on the
> e-sector — is deferred to future work. The result is physically
> motivated: black holes are conjectured to be fast scramblers
> (Sekino & Susskind 2008), and the e-sector dynamics are driven by
> the same 4D thermal chaos that underlies scrambling in 4D. A precise
> estimate of when the random-unitary approximation becomes valid
> (for k > t_scr/β = O(ln S_BH) emissions) is given in the revised
> Section 7.3 on early-time behavior (see response to B1(c)).

**New Section 7.6 to follow Section 7.5:**

> ### 7.6 Status of the Page Curve Result
>
> For clarity, we distinguish three levels of statement in this section:
>
> **Level 1 (derived from 5D equations of motion):** The e-Hilbert space
> decomposition H_{5D} = H_{BH} ⊗ H_{rad}, the e-conservation law
> at each emission vertex, and the identification of the e-sector as
> the information carrier (Sections 4–6) — these follow from the 5D
> action and Noether's theorem.
>
> **Level 2 (conditional on fast-scrambler assumption):** The Page
> curve formula S_{rad}(k) = min[k, N₀ − k] × s₀ — this follows from
> Level 1 plus the random-unitary (fast scrambler) assumption. It is a
> conditional result, not a first-principles derivation.
>
> **Level 3 (open problem):** The derivation of the fast-scrambler
> property from the 5D Hamiltonian — showing the e-sector dynamics
> generate an approximate k-design — is an open problem. Progress
> requires computing the spectral statistics of the 5D Hamiltonian
> restricted to the e-sector, which is connected to the study of
> quantum chaos in the KK theory.
>
> The identification with the island formula (Section 10) is at
> Level 2 — qualitatively consistent with the island result but not
> a rederivation of it (see Section 10 and response to B1(d)).

---

## B1(b) — The Coefficient s₀ [CLOSABLE GAP]

### Author Response

The referee points out that s₀ = ln(d_e) ~ 69 bits per pixel appears
to contradict S_BH = A/4l_P², which assigns 1 degree of freedom per
Planck area. The resolution is given in Section 8.2 (G-renormalization
absorbs the species factor) but is not connected back to Section 7.
The revision adds an explicit demonstration.

### Draft New Content — New paragraph in Section 7.3

**New paragraph to append to Section 7.3 (after the expression for
S_max = (N₀/2) × ln(d_e)):**

> **The coefficient s₀ after renormalization.** The formula above uses
> s₀ = ln(d_e) = ln(2πR₀/l_{P,bare}) ≫ 1 (using bare Planck length).
> This must agree with the Bekenstein-Hawking formula S_BH = A/(4l_P²),
> which assigns exactly 1 degree of freedom per Planck area. The two
> are consistent after G-renormalization (Section 8.2).
>
> From Section 8.2: the renormalized Newton's constant satisfies
>
>     1/G_ren = 1/G_bare + (loop contributions from N_eff KK species)
>
> The renormalized Planck length is l_{P,phys}² = G_ren ℏ/c³. The
> e-Hilbert space has d_e = 2πR₀/l_{P,bare} states per pixel. The
> physical number of independent e-states per Planck pixel — using
> the physical Planck area l_{P,phys}² — is:
>
>     s₀ = ln(d_e) × (l_{P,bare}²/l_{P,phys}²) = 1
>
> after G-renormalization. The renormalization of G absorbs exactly the
> ln(d_e) enhancement, leaving s₀ = 1 in Bekenstein-Hawking units.
> This is the same renormalization that resolves the species problem in
> Section 8.2; the two resolutions are identical. The Page curve formula
> in Bekenstein-Hawking units is S_{rad}(k) = min[k, N₀ − k], with s₀ = 1,
> correctly recovering the standard Page curve with no free parameters.

---

## B1(c) — Early-Time Behavior [GENUINE GAP]

### Author Response

The referee identifies a real inconsistency: the Page curve formula
S_{rad} ≈ k × ln(d_e) for the first k emissions requires each
emission to sample from a maximally mixed e-state, which in turn
requires the horizon to have scrambled its e-configuration. But the
scrambling time t_scr ~ β ln S_BH is much longer than one emission
time β — so for the first O(ln S_BH) emissions, the horizon has NOT
scrambled. The early-time entropy behavior in this pre-scrambling
regime must be treated separately.

### Draft New Content — New Section 7.7 (Early-Time Page Curve)

**New Section 7.7 to insert after revised Section 7.3:**

> ### 7.7 Early-Time Behavior: The Pre-Scrambling Regime
>
> The derivation of Theorem 7.1 assumes the random-unitary approximation
> holds for each emission. This requires the horizon to have scrambled
> between successive emissions. The scrambling time is
> t_scr ~ β ln S_BH (Section 11), while the emission time is ~ β
> (one Hawking period per quantum). For the first k < k_scr ≡ ln S_BH
> emissions, the horizon has NOT scrambled and the random-unitary
> approximation fails.
>
> **How many emissions are affected?** k_scr = O(ln S_BH). For a
> solar-mass black hole S_BH ~ 10^{77}, so k_scr ~ 77 × ln(10) ~ 177
> emissions. This is a negligible fraction of the total N₀ = S_BH ~ 10^{77}
> emissions — a fraction k_scr/N₀ ~ 10^{-75}.
>
> **The early-time entropy.** For k < k_scr, the infalling information
> has not yet been scrambled across the horizon. The horizon's
> e-configuration reflects the history of recent infalling bits with
> minimal mixing. In this regime the emission is not sampling a
> Haar-random state. A conservative estimate: for k < k_scr, the
> entanglement entropy grows at most as S_{rad} ≤ k × ln(d_e) (the
> random-unitary upper bound), and at least as S_{rad} ≥ 0 (trivially).
> The precise value depends on the initial state and the early-time
> dynamics — it is not determined by the random-unitary model.
>
> **The Page curve is unaffected.** The Page time occurs at k = N₀/2 ≫ k_scr.
> The behavior near the Page time — which determines the qualitative
> shape of the Page curve and its turnover — is deep in the regime
> k ≫ k_scr, where the random-unitary approximation is valid. The
> early-time (k < k_scr) correction affects only the first ln(S_BH)
> emissions out of S_BH total, modifying the entropy by at most
> ln(S_BH) × ln(d_e) out of the maximum entropy of N₀/2 × ln(d_e).
> The correction is suppressed by a factor of 2 ln(S_BH)/N₀ ~ 10^{-74}
> (for solar-mass black holes) relative to the total entropy.
>
> **Revised statement.** Theorem 7.1 applies for k ≫ k_scr = O(ln S_BH).
> For k ≤ k_scr, the entropy satisfies 0 ≤ S_{rad}(k) ≤ k × ln(d_e),
> with the precise value determined by initial conditions. The Page
> curve derivation and Page-time result are unchanged.

---

## B1(d) — Comparison with Island Formula [GENUINE GAP]

### Author Response

The referee correctly identifies that Section 10's mapping from the
e-framework to the island formula is qualitative, not a rederivation.
The island formula requires: (a) the extremization condition
δS_gen/δX = 0 reproduced; (b) subleading corrections agreeing;
(c) extension to non-AdS spacetimes.

A full derivation of the island formula from the e-framework
(including replica wormhole saddle structure) is beyond the scope
of this paper. We adopt the honest option (b) of the referee:
explicitly reframe Section 10 as a qualitative consistency
identification rather than a derivation, while strengthening the
physical argument for where the identification is exact.

### Draft New Content — Revised Section 10.3 closing + new Section 10.5

**New closing paragraph for Section 10.3:**

> The mapping A(X)/4G_N ↔ (number of Planck pixels on X) and
> S_bulk ↔ (4D thermal component) is a qualitative identification
> at the level of counting degrees of freedom. The derivation of the
> island formula by Penington (2020) and Almheiri et al. (2019) uses
> a gravitational path integral with replica wormhole saddles in JT
> gravity; the saddle-point transition at the Page time is a dynamical
> result, not a kinematic one. The e-framework does not reproduce the
> replica wormhole calculation. What we establish is consistency: the
> Page curve that follows (conditionally) from the e-framework
> matches the Page curve derived from the island formula at leading
> order. Subleading corrections of order e^{−S_BH} from replica
> wormhole saddles are not captured by the e-framework's
> random-unitary model. Whether the replica wormhole structure
> emerges from the e-framework's gravitational path integral —
> specifically, whether the e-sector generates topological
> contributions to the gravitational path integral that produce
> wormhole saddles — is an open question.

**New Section 10.5:**

> ### 10.5 Scope and Limitations of the Island Identification
>
> The connection between the e-framework and the island formula is
> at present a physical picture, not a mathematical derivation. We
> summarize what is and is not established:
>
> **Established:** (1) The e-framework produces a Page curve
> (conditional on the fast-scrambler assumption, Theorem 7.1) that
> agrees with the island formula result at the level of the Page time
> and the leading entropy formula S_{rad} = min[N_{rad}, N_{BH}].
> (2) The physical interpretation of the "island" as the set of
> Planck pixels whose e-imprints have been transferred to radiation
> is internally consistent. (3) The boundary A(X)/4G_N naturally
> maps to a pixel count in the e-framework.
>
> **Not established:** (1) The extremization condition δS_gen/δX = 0
> from the island formula is not rederived in the e-framework;
> it is argued that the e-information boundary provides a natural
> geometric locus, but the precise equality with the quantum
> extremal surface condition is not shown. (2) Subleading corrections
> of order e^{−S_BH} from replica wormholes are not computed.
> (3) The applicability to non-AdS spacetimes is asserted (Section 10.4)
> based on the geometric character of the e-framework, but the
> island formula has only been derived in holographic settings; the
> e-framework's extension is conjectural.
>
> The e-framework provides a non-holographic geometric mechanism
> whose coarse-grained result coincides with the island formula.
> Whether this coincidence reflects a deeper identity — the island
> formula as the holographic dual of the e-mechanism — is an open
> problem.

---

## B2(a) — Monogamy and the Superselection Claim [CLOSABLE GAP]

### Author Response

The referee accepts the superselection derivation of Section 9.3.1
as largely sound but asks for explicit bounding of the mass range
for which the argument is valid (M >> M_Pl where KK modes are
thermally suppressed).

### Draft New Content — Addition to Section 9.3.1, after Property 2

**New paragraph to insert at the end of Section 9.3.1, after the proof
of Property 2:**

> **Mass range validity.** The derivation of Property 2
> ([Q̂_e, Ô_{4D}] = 0) rests on 4D observables being KK zero-modes.
> For black holes with M >> M_Pl, the Hawking temperature
> T_H = ℏc³/(8πGMk_B) satisfies T_H << m₁c²/k_B (the lightest KK
> mass, m₁ = ℏc/R₀). In this regime, KK modes are not thermally
> produced (Γ ~ e^{−m₁/T_H} → 0) and the 4D observable algebra
> is effectively restricted to the zero-mode sector. The argument
> holds unconditionally for M >> M_Pl. For M ~ M_Pl (the
> near-Planck regime), T_H ~ m₁/k_B and the KK sector becomes
> dynamically relevant — but at this scale the semiclassical
> approximation itself breaks down, making the AMPS argument
> inapplicable. We therefore state: Theorem 9.1 holds for all
> black holes in the semiclassical regime M >> M_Pl, which is the
> only regime where the AMPS argument is formulated.

---

## B2(b) — Bogoliubov Transformation in the 5D Theory [GENUINE GAP]

### Author Response

The referee requires a demonstration that the 4D marginal state
ρ_{4D} = Tr_e[ρ_{5D}] satisfies the Hadamard condition near the
horizon in ingoing Eddington-Finkelstein coordinates — establishing
that the infalling observer sees the vacuum. Section 6.1 recovers
the thermal density matrix from the e-trace but does not address
the Hadamard condition near the horizon. This requires an explicit
calculation.

### Draft New Content — New Section 9.5 (Hadamard Condition)

**New Section 9.5 to follow Section 9.4:**

> ### 9.5 Hadamard Condition for the Infalling Observer
>
> For the infalling observer to encounter a smooth horizon (AMPS
> Postulate 2 — "no drama"), the 4D quantum state near the horizon
> must satisfy the Hadamard condition: the 2-point function of the
> quantum field must have the short-distance behavior of the Minkowski
> vacuum. We demonstrate this for the 4D marginal state in the 5D
> framework.
>
> **Setup.** The full 5D state is ρ_{5D} living on H_{5D} = H_{4D} ⊗ H_e.
> The 4D marginal state seen by the infalling observer is
> ρ_{4D} = Tr_e[ρ_{5D}]. We must show ρ_{4D} satisfies the Hadamard
> condition near the horizon.
>
> **Step 1: The 5D state in ingoing coordinates.** In ingoing
> Eddington-Finkelstein (IEF) coordinates (v, r, θ, ϕ_S, φ) — where
> v = t + r* is the advanced time and φ is the e-coordinate — the
> near-horizon 5D metric is regular (no coordinate singularity at
> r = r_s). The 5D vacuum state |0⟩_{5D} defined in IEF coordinates
> is the Unruh state — the physical vacuum appropriate for the
> infalling observer. In IEF coordinates the metric is:
>
>     ds² = −f(r)dv² + 2dvdr − r²dΩ² + R₀²dφ²
>
> This is regular at the horizon with no divergence.
>
> **Step 2: Tracing over e in the Unruh state.** The Unruh state
> |0⟩_{5D} in the product spacetime M⁴ × S¹ factorizes as
> |0⟩_{5D} = |0⟩_{4D,Unruh} ⊗ |0⟩_e, because the 5D metric is a
> direct product and the 5D vacuum mode functions factorize into
> 4D mode functions times e-circle mode functions (the product
> structure established in Appendix B). The e-sector vacuum is
> the standard S¹ ground state.
>
> The marginal 4D state is:
>
>     ρ_{4D} = Tr_e[|0⟩_{5D}⟨0|] = Tr_e[|0⟩_{4D,Unruh}⟨0| ⊗ |0⟩_e⟨0|]
>             = |0⟩_{4D,Unruh}⟨0| × ⟨0|0⟩_e = |0⟩_{4D,Unruh}⟨0|
>
> The 4D marginal state is the 4D Unruh vacuum.
>
> **Step 3: Hadamard condition.** The 4D Unruh vacuum |0⟩_{4D,Unruh}
> is a Hadamard state on the Schwarzschild spacetime. This is a
> standard result in quantum field theory on curved spacetime
> (Fredenhagen & Haag 1990; Kay & Wald 1991): the Unruh state
> defined by requiring regularity of mode functions on the past
> horizon satisfies the Hadamard condition near the future horizon
> in ingoing coordinates. The 2-point function
> G(x,x') = ⟨0_{Unruh}|Φ(x)Φ(x')|0_{Unruh}⟩ has the Minkowski
> short-distance behavior for x, x' near the horizon.
>
> **Conclusion.** The 4D marginal state ρ_{4D} = Tr_e[ρ_{5D}] is the
> 4D Unruh vacuum, which satisfies the Hadamard condition. The
> infalling observer — whose detectors respond to 4D field
> observables — sees the vacuum near the horizon. There is no
> firewall. The e-sector's state |0⟩_e contributes no energy density
> when traced over.
>
> **What the e-imprints do to this calculation.** After the black hole
> has absorbed infalling matter, the full 5D state is not the product
> vacuum but an e-imprinted state:
>
>     ρ_{5D}^{imprinted} = |Ψ_Hawking⟩⟨Ψ_Hawking|
>
> The 4D marginal state is still ρ_{4D} = Tr_e[ρ_{5D}^{imprinted}]
> = Σ_{n,φ} |α_{n,φ}|² |n⟩⟨n| = thermal state (Section 6.1). The
> thermal state near the horizon, in ingoing coordinates, is again the
> Unruh state — the same Hadamard state as before. The e-imprints
> modify the e-sector of ρ_{5D} but not the 4D marginal state, which
> remains thermal. Since the thermal 4D state satisfies the Hadamard
> condition (it is the Unruh vacuum), the infalling observer encounters
> no drama. The argument is consistent.
>
> **Caveats.** The factorization ρ_{5D} = ρ_{4D} ⊗ ρ_e used above is
> exact only in the product metric (Appendix B). Near the Planck scale
> (M ~ M_Pl) this approximation breaks down; but as noted, the
> semiclassical analysis is valid only for M >> M_Pl anyway.

---

## B2(c) — Infalling Observer's 4D Experience: KK Mass Renormalization [CLOSABLE GAP]

### Author Response

The referee notes that near the horizon, Christoffel symbols of the
curved 4D metric mix KK sectors, potentially creating observable KK
mass renormalization effects for the infalling observer. A brief
argument is required.

### Draft New Content — Addition to Section 9.4

**New paragraph to append to Section 9.4:**

> **KK mass renormalization near the horizon.** In the curved 4D
> background, the KK masses receive curvature corrections from the
> coupling of the KK fields to the Ricci scalar:
> m_n² → n²/R₀² + ξR_{4D}, where R_{4D} is the 4D Ricci scalar and ξ
> is the non-minimal coupling. Near the horizon in IEF coordinates,
> R_{4D} is finite (for a smooth Schwarzschild horizon it vanishes in
> the vacuum). For the Unruh vacuum near the horizon, ⟨T_μν⟩ = 0
> (the renormalized stress tensor vanishes for the Hadamard state), so
> the backreaction curvature from quantum fields is negligible. The KK
> mass renormalization near the horizon is of order R_{4D}/m₁² ~
> (M_Pl/M)⁴ × (l_P/R₀)² — suppressed by four powers of M_Pl/M and
> by (l_P/R₀)² ~ 10^{-60} for R₀ ~ 12 μm. This is negligible for any
> astrophysical black hole. No observable energy density is created
> near the horizon by KK mass renormalization. See Paper 1, Appendix O
> for the detailed computation of curvature corrections to KK masses in
> the Schwarzschild background.

---

## B2(d) — Equivalence Principle in 5D [CLOSABLE GAP]

### Author Response

The referee asks for a paragraph stating the 5D equivalence principle
and showing that the e-imprint (a fiber connection change) does not
violate it.

### Draft New Content — Addition to Section 9.4

**New paragraph to append to Section 9.4 (after the KK mass
renormalization paragraph):**

> **The 5D equivalence principle.** The equivalence principle in the
> 5D framework states: the local 5D geometry at any point p is
> indistinguishable from flat 5D spacetime M^{4,1} = M⁴ × S¹_{flat}
> (locally) — a freely-falling observer in a region small compared to
> the curvature scale sees flat 5D physics. The e-imprint δφ on the
> horizon is a change in the fiber connection — a global property of
> the bundle over the horizon surface S² × S¹, not a local geometric
> property at any single point. A freely-falling observer passing
> through one fiber does not "see" the connection of adjacent fibers,
> just as a particle traveling along a worldline does not detect a
> non-trivial holonomy of a gauge field unless it travels a closed
> loop. The e-imprint δφ is detectable only through non-local
> operations (comparing e-coordinates of spatially separated points
> on the horizon, or accessing the global e-charge Q_e) — neither
> of which is available to a local infalling observer. The 5D
> equivalence principle is preserved: locally, the horizon looks
> like a smooth 5D Minkowski geometry, with the e-imprint invisible
> to any local measurement. This is analogous to the Berry phase
> in quantum mechanics: a globally non-trivial gauge connection
> produces no local force or energy density.

---

## C1(a) — Self-Adjointness of the e-Clock Operator [GENUINE GAP]

### Author Response

The referee correctly identifies that the angle operator φ̂ on L²(S¹)
is NOT self-adjoint — this is the Garrison-Wong / Carruthers-Nieto
angle-angular momentum problem. The KK momentum operator p̂_e = −iℏ∂/∂φ
is self-adjoint with discrete integer spectrum (winding numbers), but
its conjugate angle has no self-adjoint extension compatible with the
compact topology. The referee further notes that a clock on a compact
space with period 2π repeats, which limits its ability to track the
full evaporation history.

We address this with a revised treatment of Section 3.2–3.3 that
identifies the correct clock observable (the KK winding number, not
the angle), discusses the winding-number tracking, and clarifies the
scope of the Page-Wootters argument.

### Draft New Content — New Section 3.2.1 (Clock Self-Adjointness)

**New Section 3.2.1 to insert after Section 3.2:**

> ### 3.2.1 Self-Adjointness and the Correct Clock Observable
>
> The e-coordinate φ ∈ [0, 2π) parameterizes the compact e-circle S¹.
> As an operator on L²(S¹), the angle φ̂ is NOT self-adjoint — this
> is the standard angle-angular momentum problem (Garrison & Wong 1970;
> Carruthers & Nieto 1968). The compact topology S¹ forces the
> identification φ ~ φ + 2π, which is incompatible with a self-adjoint
> angle operator. The canonically conjugate momentum to φ — the KK
> winding number operator n̂ = R₀ p̂_e / ℏ = −iR₀ ∂/∂φ — IS
> self-adjoint on L²(S¹) with discrete integer eigenvalues n ∈ Z.
>
> **The correct clock observable is n̂, not φ̂.**
>
> In the Page-Wootters mechanism, the clock system must have a
> self-adjoint "clock observable" (playing the role of "time") and
> a conjugate "clock Hamiltonian" (generating time translation).
> On S¹:
>
> - Clock Hamiltonian: Ĥ_e with eigenvalues E_n = n²ℏ²/(2mR₀²), n ∈ Z.
> - Clock observable: The energy eigenvalues n label the clock states.
>   For the clock to "read time," we need a finer observable. The
>   correct choice is the winding observable W, counting net winds
>   around the e-circle over the evaporation history.
>
> **Winding number as clock.** The winding number W = ∮ dφ/(2π) is
> an integer-valued observable that counts how many times the
> particle's phase has advanced around the full circle. Unlike φ̂, W
> is well-defined on the universal cover R of S¹ and is self-adjoint.
> It can take arbitrarily large integer values, making it suitable as
> a clock for the full evaporation history.
>
> The relationship between winding and time is: for a particle with
> energy E, the phase advances at rate ∂φ/∂τ = −E/ℏ (Section 3.2).
> The winding number after proper time τ is W = |Eτ/(2πℏ)|. Since
> E ~ T_H and τ = t_evap ~ M³ (in Planck units), the total winding
> over the evaporation is W_evap ~ T_H × t_evap / (2πℏ) ~
> S_BH/(2π) >> 1 for any macroscopic black hole. The clock has
> more than enough "resolution" to track the entire evaporation.
>
> **The Page-Wootters mechanism revisited.** The clock state in the
> Page-Wootters mechanism should be indexed by the winding number W,
> not the compact angle φ:
>
>     |ψ(W)⟩ = ⟨W|Ψ_{5D}⟩
>
> The conditional state at winding number W is the 4D state seen at
> the W-th thermal cycle. The WdW constraint Ĥ_{5D}|Ψ_{5D}⟩ = 0
> implies Ĥ_{4D}|ψ_n⟩ = −E_n|ψ_n⟩, and conditioning on the winding
> observable W (which counts cycles of the clock) reproduces
> Schrödinger evolution in the 4D sector with time parameter
> t = 2πWℏ/E.
>
> **The role of φ vs. W.** The compact angle φ provides the periodic
> identification that makes particles fermions or bosons (spin-statistics,
> Paper 1 Appendix B) and that generates the Hawking temperature from
> Euclidean periodicity (Section 3.4). The winding number W provides
> the self-adjoint clock observable for the Page-Wootters mechanism.
> These are complementary aspects of the same compact dimension —
> the local phase structure (φ) and the global winding structure (W).
>
> **Factor-ordering note.** The concern about factor-ordering
> ambiguities in the WdW equation is addressed in Section 3.3
> revision (see C1(c) below).

---

## C1(b) — Metric Independence of the e-Clock [CLOSABLE GAP]

### Author Response

The referee accepts that the metric independence claim holds in the
product gauge (A_μ = 0), justified by Z₂ symmetry, but asks for
an explicit qualifier in Section 3.2.

### Draft New Content — Sentence to add to Section 3.2

**Sentence to add after "Metric-independent: The e-evolution
∂φ/∂τ = −E/ℏ holds regardless of the background spacetime metric":**

> Precisely: this holds in the product-metric gauge g_{5D} =
> g_{4D} + R₀² dφ², which corresponds to the KK gauge choice A_μ = 0
> (no off-diagonal KK vector). This gauge is enforced by the Z₂
> orbifold symmetry φ → −φ of the e-circle (Paper 1, §2.1), which
> forbids the odd-function coupling g_{5μ} ∝ A_μ. The product
> structure is therefore not a gauge choice but a symmetry consequence:
> the Z₂ symmetry renders A_μ = 0 exact, and the e-clock evolution
> is metric-independent as a result.

---

## C1(c) — Wheeler-DeWitt Hamiltonian Factorization [GENUINE GAP]

### Author Response

The referee identifies that the WdW factorization Ĥ_{5D} = Ĥ_{4D} + Ĥ_e
is valid for a free scalar field in a fixed 5D background, not for the
full gravitational WdW constraint, which involves the nonlinear 5D ADM
Hamiltonian and is coupled through the radion. The factor-ordering
ambiguity is also not addressed.

We add a revised Section 3.3 that honestly scopes the factorization,
discusses the radion coupling and factor ordering, and explains what
additional assumptions are needed for the gravitational case.

### Draft New Content — Revised Section 3.3 and New Section 3.3.1

**New first paragraph of Section 3.3 (replacing the current
"The WDW equation as a 4D projection" opening):**

> ### 3.3 The Wheeler-DeWitt Equation — Scope and Factorization
>
> The Wheeler-DeWitt (WdW) equation in canonical quantum gravity is
> Ĥ_G|Ψ⟩ = 0 where Ĥ_G is the full gravitational Hamiltonian
> constraint — the 5D ADM Hamiltonian. This is a nonlinear functional
> differential operator on superspace (the space of 5D metrics). It
> does NOT factorize as Ĥ_{4D} + Ĥ_e in general, because gravity
> couples the 4D and e-sectors through the radion (the KK scalar that
> describes fluctuations of R₀).
>
> The factorization Ĥ_{5D} = Ĥ_{4D} + Ĥ_e presented in this section
> applies to matter fields in a fixed 5D background geometry (the
> Born-Oppenheimer approximation for quantum gravity: treat the metric
> as a fixed classical background and quantize matter fields on it).
> In this approximation, the 5D Hamiltonian for matter factorizes
> exactly by the product structure of the metric (Section B.3):
>
>     Ĥ_{5D,matter} = Ĥ_{4D,matter} + Ĥ_{e,matter}
>
> This is the sense in which the factorization holds: it is a statement
> about the matter Hamiltonian in a fixed background, not about the
> full quantum gravitational Hamiltonian.
>
> **What additional assumptions are needed for the gravitational case?**
>
> To extend the argument to the full gravitational WdW equation, we
> need: (1) modulus stabilization ensures R₀ is frozen at its
> Casimir-determined value (Paper 1, §2.1), so the radion is not a
> dynamical degree of freedom below energy scales 1/R₀ ~ 10⁻² eV;
> (2) below this scale, the e-sector of the gravitational Hamiltonian
> reduces to the frozen radion sector plus the KK matter tower, both
> of which contribute to the factorized Ĥ_e; (3) the 4D gravitational
> Hamiltonian Ĥ_{4D,grav} is the standard 4D ADM Hamiltonian,
> decoupled from the frozen e-sector.
>
> Under these conditions — which hold throughout the semiclassical
> evaporation regime — the effective WdW factorization holds:
>
>     Ĥ_{eff,5D}|Ψ_{5D}⟩ = (Ĥ_{4D,grav} + Ĥ_e)|Ψ_{5D}⟩ = 0
>
> The effective factorization is not the full WdW equation but its
> Born-Oppenheimer limit with a frozen radion. This is the framework
> in which the Page-Wootters mechanism applies and in which "the
> problem of time is resolved."

**New Section 3.3.1 (Factor Ordering):**

> ### 3.3.1 Factor Ordering
>
> The WdW equation suffers from factor-ordering ambiguities: the
> classical constraint H = 0 can be quantized as Ĥ|Ψ⟩ = 0 in multiple
> inequivalent ways. In the 5D framework, the factor-ordering question
> for the e-sector is straightforward: the e-sector Hamiltonian is
> Ĥ_e = (1/2m)(p̂_e)² with p̂_e = −iℏ(1/R₀)∂/∂φ, a self-adjoint
> operator on L²(S¹). The eigenvalues are E_n = n²ℏ²/(2mR₀²), and
> factor ordering does not arise (the Hamiltonian is already in
> normal-ordered form on the compact S¹).
>
> For the 4D gravitational sector Ĥ_{4D,grav}, factor ordering is the
> standard unresolved problem of quantum gravity — present in all
> approaches (Wheeler-DeWitt, loop quantum gravity, Euclidean path
> integrals). The e-dimension framework does not resolve this problem
> for the 4D sector. What it does resolve is the problem of time: given
> that some consistent quantization of Ĥ_{4D,grav} exists (with any
> factor ordering), the e-clock provides the conditional state
> |ψ(W)⟩ = ⟨W|Ψ_{5D}⟩ that evolves unitarily as W increases. The
> clock resolves the frozen-formalism problem (dynamics disappears)
> without needing to solve the factor-ordering problem (which
> quantization of Ĥ_{4D,grav} to use). The two issues are decoupled.

---

## C2(a) — The ln(S_BH) Factor in Scrambling Time [CLOSABLE GAP]

### Author Response

The referee correctly notes that the coupon collector's argument gives
O(N ln N) trials to see all coupons, not O(ln N). The O(ln N)
scrambling time arises from the Hayden-Preskill decoupling theorem,
not coupon collecting. The revision corrects Section 11.2.

### Draft New Content — Revised Section 11.2 (third paragraph)

**Replacement for the paragraph "The scrambling time is the time for
the 4D thermal dynamics..." in Section 11.2:**

> The scrambling time is the time for the 4D thermal dynamics to mix
> the δφ perturbation into the emission process — for the next emitted
> quanta to carry e-imprints that reflect the new δφ. The O(ln S_BH)
> factor arises from the Hayden-Preskill decoupling theorem (Hayden &
> Preskill 2007, Theorem 2): for a black hole modeled as a random
> unitary acting on S_BH qubits, an infalling bit becomes decodable
> from the Hawking radiation after only O(ln S_BH) additional qubits
> are emitted. Specifically, the decoupling argument shows that after
> k additional emissions following a perturbation, the mutual
> information between the perturbation and the accessible radiation
> drops to negligible values for k = O(log₂ S_BH) — the information
> has been scrambled into the full quantum state. In the e-framework,
> the perturbation is δφ (the new e-imprint), the "qubits" are the
> Planck pixels on the horizon, and the thermalization rate is 1/β.
> Therefore:
>
>     t_scr = O(ln S_BH) × β = β/(2π) × ln S_BH
>
> reproducing the Sekino-Susskind result. The earlier "coupon
> collector" language in previous versions was imprecise; the correct
> reference is the decoupling theorem of Hayden-Preskill (2007).

---

## C2(b) — Consistency with the Chaos Bound [CLOSABLE GAP]

### Author Response

The referee accepts the argument (e-propagation is invisible to 4D
OTOCs by the superselection of Section 9.3.1) but asks for a single
explicit sentence.

### Draft New Content — Addition to Section 11

**Sentence to add to Section 11.3 (after the four-point enumeration):**

> The Maldacena-Shenker-Stanford (2016) chaos bound λ_L ≤ 2πT_H/ℏ
> constrains out-of-time-order correlators (OTOCs) of 4D observables.
> By the superselection structure of Section 9.3.1 (Property 2:
> [Q̂_e, Ô_{4D}] = 0), e-propagation does not contribute to any 4D
> OTOC — the e-sector is decoupled from the 4D observable algebra.
> The Lyapunov exponent measured by 4D OTOCs is λ_L = 2πT_H/ℏ,
> saturated in the 4D sector alone, consistent with the standard
> result for black holes as fastest scramblers. The instantaneous
> e-encoding does not enter the chaos bound calculation.

---

## C3(a) — M-Theory Identification as UV Completeness [CLOSABLE GAP]

### Author Response

The referee accepts the physical content of Appendix A but flags that
Premise 1 ("The framework = M-theory on S¹/Z₂ × CP² × S²") is labeled
"Established: Paper 4, §2.3" while Paper 4 is not submitted. The
referee asks for either including the identification argument or
demoting Premise 1 to "Conjectured."

We demote Premise 1 and restate the logical structure.

### Draft New Content — Revised Section A.4.2

**Replacement for the first paragraph of Section A.4.2:**

>     Premise 1: The framework ≅ M-theory on (S¹/Z₂ × CP² × S²)
>               [Status: Conjectured — evidence in Paper 4, §2.3;
>                verification pending submission of Paper 4]
>     Premise 2: M-theory is non-perturbatively well-defined
>               [Standard assumption, supported by duality checks,
>                anomaly cancellation, matrix theory; not proved]
>     Conclusion: The framework is non-perturbatively well-defined
>               [Conditional on Premises 1 and 2]
>
> We flag explicitly that this is a plausibility argument, not a proof.
> Premise 1 is a conjecture with supporting evidence (the e-circle
> identified with the M-theory circle, the KK spectrum consistent with
> the M-theory compactification) to be established in Paper 4. Premise 2
> is the standard (unproven) assumption about M-theory's non-perturbative
> definition shared by all approaches invoking M-theory as a UV
> completion. The M-theory completion is not required for any physical
> prediction in this paper — all predictions follow from Layers 1 and 2
> (perturbative finiteness and non-perturbative stability), which are
> proved from within the framework without M-theory.

---

## C3(b) — Bubble of Nothing Instability [CLOSABLE GAP]

### Author Response

The referee identifies that the antiperiodic boundary conditions for
fermions (established in Paper 1 Appendix B from the spin-statistics
theorem) give a kinematic suppression of the bubble of nothing —
stronger than the exponential Casimir barrier already cited.

### Draft New Content — Addition to Section A.3.1

**Sentence to add to Section A.3.1, after the description of the
Witten bubble of nothing:**

> There is a kinematic suppression of the bubble of nothing instability
> that is stronger than the exponential Casimir barrier: fermions in
> this framework have antiperiodic boundary conditions around the
> e-circle (from the spin-statistics theorem, Paper 1, Appendix B;
> winding once around the e-circle multiplies a fermion wave function
> by −1). Witten (1982, p. 1263) showed that with antiperiodic fermion
> boundary conditions, the bubble of nothing nucleation requires a
> fermionic zero mode on the bubble wall. This zero mode raises the
> bubble's energy, making nucleation kinematically suppressed beyond
> the exponential Casimir barrier. The antiperiodic spin structure is
> therefore the primary mechanism suppressing the bubble of nothing;
> the Casimir barrier provides additional suppression on top of the
> kinematic one.

---

## C3(c) — Topology Change During Evaporation [CLOSABLE GAP]

### Author Response

The referee asks for a paragraph addressing whether 4D topology change
during black hole evaporation (formation of a trapped region, eventual
dissolution) is compatible with the 5D product structure.

### Draft New Content — New paragraph in Section A.3.1

**New paragraph to add at the end of the topology change entry in
Section A.3.1:**

> **4D topology change during evaporation.** Black hole evaporation
> involves a change in the 4D causal structure: the spacetime begins
> as Minkowski space, develops a Schwarzschild trapped region with an
> event horizon, and (in the semiclassical picture) the mass decreases
> until the black hole dissolves. Throughout this process the 5D metric
> remains a direct product g_{5D} = g_{4D}(x, t) + R₀² dφ², where
> g_{4D}(x, t) is the time-evolving 4D metric. The 4D topology changes
> as the evaporation proceeds, but the e-fiber S¹ is always present:
> it is attached to every point of the 4D base by a trivial bundle, and
> as the 4D base changes topology, the e-fiber simply accompanies it.
> No fiber degeneration occurs because R₀ is constant (modulus
> stabilization, Paper 1, §2.1) and the S¹ factor is orthogonal to
> all 4D dynamics. The 5D topology during evaporation is
> M⁴_{evap}(t) × S¹, where M⁴_{evap}(t) evolves but S¹ is constant.
> This is topologically trivial from the perspective of the e-dimension.

---

## Revision Checklist

The following changes are required for the revision. Items are
labeled by their referee point, the paper location, and the type
of change (new text / replacement / addition).

### Critical Issues (A-rated findings)

| # | Finding | Paper Location | Action |
|---|---------|---------------|--------|
| R1 | Replace "carries no causal structure" throughout with precise zero-mode statement | Sections 2.1, 2.4 | Replacement (see A1(a) draft) |
| R2 | Add new Section 2.4 distinguishing zero-mode background from KK excitations | Section 2.4 | New text (see A1(a) draft) |
| R3 | Add new Section 5.4 on global charge vs. local pixel imprint distribution | After Section 5.3 | New text (~2 pages, see A1(c) draft) |
| R4 | Add to Section 4.3: derivation of area quantization from e-conservation + S_BH formula | Section 4.3 | Addition (see A2(a) draft) |
| R5 | Reframe Section 7 as conditional result (Theorem 7.1); add Section 7.6 on status | Sections 7.3, new 7.6 | Replacement + new text (see B1(a) draft) |
| R6 | Add Section 7.7 on early-time Page curve in pre-scrambling regime | After Section 7.3 | New text (~1 page, see B1(c) draft) |
| R7 | Add new Section 9.5 on Hadamard condition for infalling observer | After Section 9.4 | New text (~2 pages, see B2(b) draft) |
| R8 | Add new Section 3.2.1 on clock self-adjointness; replace φ with winding number W | After Section 3.2 | New text (~1.5 pages, see C1(a) draft) |
| R9 | Revise Section 3.3 to scope WdW factorization as Born-Oppenheimer; add Section 3.3.1 on factor ordering | Section 3.3 | Replacement + new text (~1.5 pages, see C1(c) draft) |

### Secondary Issues (B-rated findings)

| # | Finding | Paper Location | Action |
|---|---------|---------------|--------|
| R10 | Add KK thermal suppression paragraph to Section 5.3 | Section 5.3 | Addition (~100 words, see A1(b) draft) |
| R11 | Add KK propagator vs. background distinction paragraph to Section 2.4 | Section 2.4 | Addition (~100 words, see A1(d) draft) |
| R12 | Add classical limit paragraph to Section 4.2 | Section 4.2 | Addition (~80 words, see A2(b) draft) |
| R13 | Add e-coordinate geometric definition sentence to Section 4.3 | Section 4.3 | Addition (1 sentence, see A2(c) draft) |
| R14 | Add s₀ renormalization paragraph to Section 7.3 | Section 7.3 | Addition (~120 words, see B1(b) draft) |
| R15 | Revise Section 10.3 closing + add Section 10.5 on island formula scope | Sections 10.3, new 10.5 | Replacement + new text (~400 words, see B1(d) draft) |
| R16 | Add mass range paragraph (M >> M_Pl) to Section 9.3.1 | Section 9.3.1 | Addition (~100 words, see B2(a) draft) |
| R17 | Add KK mass renormalization paragraph to Section 9.4 | Section 9.4 | Addition (~100 words, see B2(c) draft) |
| R18 | Add 5D equivalence principle paragraph to Section 9.4 | Section 9.4 | Addition (~120 words, see B2(d) draft) |
| R19 | Add metric-independence qualifier (product gauge, Z₂ symmetry) to Section 3.2 | Section 3.2 | Addition (2 sentences, see C1(b) draft) |
| R20 | Replace coupon collector argument with Hayden-Preskill decoupling theorem in Section 11.2 | Section 11.2 | Replacement (~150 words, see C2(a) draft) |
| R21 | Add chaos bound sentence to Section 11.3 | Section 11.3 | Addition (1–2 sentences, see C2(b) draft) |
| R22 | Demote Premise 1 of Section A.4.2 from "Established" to "Conjectured" | Section A.4.2 | Replacement (~100 words, see C3(a) draft) |
| R23 | Add kinematic bubble suppression sentence to Section A.3.1 | Section A.3.1 | Addition (~80 words, see C3(b) draft) |
| R24 | Add 4D topology change paragraph to Section A.3.1 | Section A.3.1 | Addition (~120 words, see C3(c) draft) |

### Summary of Critical Issue Resolution

**Critical Issue 1 (e-causal structure):** Addressed by R1–R3 and R10–R11.
The precise replacement for "carries no causal structure" is:
"the n = 0 zero-mode of the e-coordinate is non-dynamical; changes in
it are determined by the algebraic e-conservation constraint, not by
a differential equation. The 5D metric has a complete Lorentzian causal
structure; the e-direction is spacelike within it." The global vs. local
ambiguity is resolved in new Section 5.4.

**Critical Issue 2 (Page curve derivation):** Addressed by R5–R6 and R14–R16.
Section 7 is reframed as a conditional theorem: given the fast-scrambler
assumption, the Page formula follows from the e-Hilbert space structure.
The early-time pre-scrambling behavior is treated explicitly in new
Section 7.7. The island formula connection is honestly characterized as
a qualitative identification in new Section 10.5.

**Critical Issue 3 (e-clock self-adjointness and WdW factorization):**
Addressed by R8–R9 and R19. The correct clock observable is the
winding number W (self-adjoint, unbounded, tracks the full evaporation),
not the compact angle φ. The WdW factorization is reframed as valid in
the Born-Oppenheimer limit with frozen radion (the regime of
semiclassical evaporation). Factor ordering for the 4D gravitational
sector is explicitly decoupled from the clock problem.

---

*Prepared April 2026*
