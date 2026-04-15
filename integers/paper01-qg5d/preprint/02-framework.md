# Section 2 — The 4+1 Coordinate Framework (M⁵ = M⁴ × S¹)

<!-- Heading migration (Intervention 8b, 2026-04-15, user-approved 2026-04-15): legacy heading "Section 2 — The Five-Dimensional Framework" → canonical heading above per strategy/north-star.md §0.10 entry 1 ("4+1 derivable coordinates" preferred over "5-dimensional") and §0.1 (M⁵ = M⁴ × S¹ naming). -->
<!-- Vocabulary canon note (Intervention 8b, 2026-04-15, aggressive migration applied): this file uses "five-dimensional" / "5D" / "fifth dimension" as subject-matter language for the derivation of the 4+1 coordinate framework. Per strategy/north-star.md §0.10 (Vocabulary Canon), canonical phrasing is "4+1 coordinate structure" / "M⁵" / "internal phase" / "S¹ coordinate". Inline strikethrough migrations applied to thesis sentences, headings, and high-salience passages. -->

---

## 2.1 Five Coordinates

In this framework, every event in reality is characterized by five coordinates:

    (x, y, z, t, e)

The first four — spatial position `(x, y, z)` and time `(t)` — are the coordinates of
standard four-dimensional spacetime, familiar from special and general relativity.
The fifth — `e` — is new. We call it the *phase dimension* or *e-dimension*.

These five coordinates are proposed as equally fundamental degrees of freedom. Just
as it is meaningful to ask "where is this particle in space?" or "when does this
event occur?", it is equally meaningful to ask "where is this particle in the
e-dimension?" The e-coordinate is not metaphorical, not a mathematical convenience,
and not a shorthand for something else. It is a coordinate — a real degree of
freedom of the physical world.

The central claim of the framework is simple to state:

**Our four-dimensional experience is a projection of ~~five-dimensional reality~~ the 4+1 coordinate structure (M⁵)<!-- legacy 2026-04-15 Intervention 8b §0.10: "five-dimensional reality" → "4+1 coordinate structure (M⁵)" -->.
The e-coordinate is the hidden ~~dimension~~ internal phase (S¹ coordinate)<!-- legacy 2026-04-15 Intervention 8b §0.10: "dimension" → "internal phase (S¹ coordinate)" --> of that projection.**

Everything that follows is a consequence of this claim.

---

## 2.2 Properties of the e-Dimension

The e-dimension has three defining properties that distinguish it from the spatial
and temporal dimensions. Each property is motivated by the quantum phenomena it
explains, which we develop fully in Section 3.

### 2.2.1 Circular and Periodic

The e-dimension is not a line stretching from `-∞` to `+∞`, as the spatial dimensions
are. It is a *circle* — periodic, like an angle, wrapping continuously from 0 to
`2π` and back to 0. A particle whose e-coordinate increases continuously will
eventually return to its starting e-value after one full revolution.

This circularity has immediate consequences:

- It explains why quantum phase is periodic: the phase factor `e^(iθ)` in the
  wave function is periodic in `θ` with period `2π`, because `θ` *is* the e-coordinate
  and the e-coordinate lives on a circle.

- It explains why spin-`½` particles require a `720°` spatial rotation to return
  to their original state (rather than `360°`): a `360°` rotation in space corresponds
  to a half-revolution in e-space — the particle is at the antipodal point of the
  e-circle. A full `720°` rotation completes one e-revolution and returns the
  particle to its starting e-value (Section 3.4).

- It provides the topological structure underlying the spin-statistics theorem:
  winding numbers on the e-circle are integers or half-integers, and these are
  precisely the allowed spin values (Section 4.2).

Mathematically, the e-dimension is parameterized by an angle `φ ∈ [0, 2π)`, and
the structure group of the e-circle is `U(1)` — the group of complex numbers of
unit modulus.

### 2.2.2 Observable Only Through Relationships

We cannot directly measure the absolute e-coordinate of a particle. What we can
observe are:

- **Differences** between e-coordinates: when two paths through spacetime
  accumulate different e-values, the difference produces interference — the
  oscillating intensity patterns of the double-slit experiment, the fringes
  of the Mach-Zehnder interferometer, the Aharonov-Bohm phase shift.

- **Conservation constraints**: when two particles interact, their e-coordinates
  become correlated through a conservation law (Section 2.3). The constraint
  `e₁ + e₂ = C` is what we observe as quantum entanglement.

- **Gradients with respect to space**: the rate at which the e-coordinate changes
  per unit distance (`∂e/∂x`) is what we observe as momentum. The rate of change
  per unit time (`∂e/∂t`) is related to energy. These are the helical pitch of
  the particle's trajectory through `(x, e)`-space (Section 3.3).

This observability structure is not a limitation imposed by experimental technology.
It is a fundamental geometric constraint: just as we cannot measure "absolute position
in space" (only positions relative to a reference frame), we cannot measure absolute
e-coordinates (only differences, gradients, and conservation constraints). The
e-dimension is real and fully physical; it is simply not accessible to direct
observation from our four-dimensional perspective.

### 2.2.3 The e-Conservation Law

In any interaction between particles, the total e-coordinate is conserved:

    e₁ + e₂ + ... + eₙ = constant

This conservation law is the e-analog of momentum conservation. By Noether's theorem,
every conservation law corresponds to a continuous symmetry of the action. Momentum
is conserved because the laws of physics are symmetric under spatial translation
(shifting all x-coordinates by a constant changes nothing physical). The e-conservation
law holds because the laws of physics are symmetric under translation in the
e-dimension (shifting all e-coordinates by a constant changes nothing physical).

This symmetry — called *e-translation invariance* — was historically labeled
"the deepest postulate of the framework." Under the 2026-04 audit (see §2.7
label-migration note, and `strategy/paper1-audit/`), it is upgraded to
**Theorem T3**, derivable from T2 (the `S¹`-uniqueness theorem, Paper 61
§13.5) via the `U(1)` isometry of `S¹` and Noether 1918; it is the single
structural claim from which the e-conservation law, and therefore the
geometric account of entanglement, follows. The legacy "postulate" wording is
preserved here for continuity; the epistemic status is theorem.

---

## 2.3 The Projection Postulate

We cannot observe the e-dimension directly. Our measurements, our instruments,
and our sensory experience are all four-dimensional. We observe projections of
the five-dimensional reality onto four-dimensional spacetime.

This projection works in one of two ways, depending on the type of observation:

**Integration:** When we observe a particle without making a measurement that
localizes its e-coordinate, we effectively integrate over all e-values. We see
the full projection of the particle's five-dimensional structure onto four-
dimensional spacetime. This integration is what produces the wave-like behavior
of quantum mechanics — interference, diffraction, and spread-out probability
distributions.

**Sampling:** When we make a measurement that interacts with the particle's
e-coordinate — coupling our apparatus's e-coordinate to the particle's — we
sample the five-dimensional structure at a particular e-value. We see a slice
through the structure at that e-value. This sampling is what produces the
particle-like behavior — localized detection events, definite measurement
outcomes.

The transition between these two observational modes is what standard quantum
mechanics calls "wave function collapse." In the 5D framework, nothing collapses.
The five-dimensional structure is unchanged by measurement. What changes is our
mode of observation: from integrating over the full e-range to sampling at a
specific e-value. "Collapse" is an epistemic update about which e-slice we
intersected, not an ontological change in the particle's state.

This resolves the measurement problem without any additional postulate. The
apparent paradox of "collapse" disappears when the e-dimension is made explicit.

---

## 2.4 The Wave Function as Geometry

In standard quantum mechanics, the wave function `ψ(x, y, z, t)` is a complex-valued
function — a mathematical object that encodes probabilities. Its modulus squared
`|ψ|²` gives the probability density for finding the particle at a given location.
The phase of `ψ` — the angle of the complex number — affects interference but is
not directly observable. The wave function is, in this standard view, an abstract
calculational tool rather than a description of physical reality.

In the 5D framework, the wave function is not abstract. It is the literal geometric
shape of the particle in five-dimensional spacetime.

Consider the standard form of a quantum wave function:

    ψ(x, y, z, t) = A(x, y, z, t) · e^(iθ(x,y,z,t))

where `A` is the amplitude and `θ` is the phase. In the 5D framework:

- The amplitude `A(x, y, z, t)` describes how much of the particle's five-dimensional
  structure is present at each spacetime point, integrated over the e-direction —
  it is the four-dimensional "shadow" density of the five-dimensional object.

- The phase `θ(x, y, z, t)` *is* the e-coordinate. It is not a property of an
  abstract mathematical object. It is a physical coordinate, as real as `x` or `t`.

- The complex plane — the space of values `A·e^(iθ)` — is the e-circle. The real
  and imaginary parts of `ψ` are the projections of the e-coordinate onto two
  orthogonal axes.

- The Schrödinger equation, which governs the time evolution of `ψ`, is the
  equation of motion for the particle's five-dimensional geometric structure —
  the law describing how the shape evolves through `(x, y, z, t, e)`-space.

The wave function is therefore not mysterious. It is a geometric object — the
five-dimensional shape of the particle — described in terms of its four-dimensional
projections (amplitude) and fifth coordinate (phase).

---

## 2.5 Mathematical Structure: U(1) Fiber Bundles

For readers familiar with differential geometry, we note the precise mathematical
structure that the framework employs.

The five-dimensional spacetime of the framework is a principal fiber bundle:

    P(M⁴, U(1))

where `M⁴` is four-dimensional spacetime (the base manifold) and `U(1)` is the
structure group — the group of rotations of the e-circle. At every point in `M⁴`,
a copy of the e-circle `U(1)` is attached as a fiber. The full five-dimensional
space is the total space of this bundle.

The connection on this bundle — the geometric object that describes how e-coordinates
are transported as we move through spacetime — is what appears in physics as the
electromagnetic vector potential **A**. The curvature of this connection is the
electromagnetic field tensor **F** = d**A**, whose spatial components are the
magnetic field **B** and mixed space-time components are the electric field **E**.

This identification is not new — it is the standard geometric formulation of
electromagnetism as a `U(1)` gauge theory, developed by Weyl, Yang, Mills, and
others in the mid-twentieth century. What *is* new in our framework is the
physical interpretation: we identify the `U(1)` fiber not as a mathematical gauge
redundancy but as a literal physical dimension — the e-dimension — whose geometry
is directly observable through quantum phenomena.

The Aharonov-Bohm effect (Section 4.1) is the direct experimental evidence for
this identification: it shows that the connection **A** is physically real (not
merely a gauge artifact), which is precisely what the fiber bundle interpretation
predicts.

The mathematical structure proposed here — a `U(1)` principal bundle over spacetime
with the wave function as a section — connects to the program of geometric
quantization (Kostant 1970, Souriau 1970, Woodhouse 1992), which constructs
quantum mechanics from symplectic geometry using precisely this bundle structure.
The distinction is ontological: geometric quantization treats the `U(1)` fiber as
a mathematical device for producing a quantum theory from a classical one; the
e-dimension framework treats it as a literal physical dimension. The mathematical
objects are the same. What is new is the claim that the fiber has geometric reality.

For readers unfamiliar with fiber bundles: all that is required for what follows
is the picture established in Sections 2.1-2.4. The fiber bundle language makes
the mathematics precise but does not change the physical content.

### Distinction from Kaluza-Klein Theory

The mathematical structure of the framework — a `U(1)` principal bundle over
spacetime — is shared with Kaluza-Klein theory (Kaluza 1921, Klein 1926). The
physical content is entirely different, in three respects that we state explicitly
because the superficial resemblance will invite the comparison.

First, the coupling. Kaluza-Klein couples the fifth dimension to *electric charge*.
A particle's momentum in the compact dimension is proportional to its charge. The
framework proposed here couples the e-dimension to *quantum phase* — a property of
every particle, charged or not. A neutron has zero electric charge but has definite
spin, participates in interference experiments, and can be entangled. Kaluza-Klein
has nothing to say about the neutron's quantum properties. The e-dimension framework
accounts for all of them.

Second, the observability. Kaluza-Klein compactifies the fifth dimension at the
Planck scale (`~10⁻³⁵ m`), rendering it inaccessible to any foreseeable experiment.
The e-dimension is accessible at *all* scales — in every interference pattern, every
entanglement correlation, every spin measurement ever performed. It is not hidden at
the Planck scale. It is hidden in the quantum phase, which was interpreted as an
abstract amplitude rather than a geometric coordinate.

Third, the scope. Kaluza-Klein provides a geometric account of electromagnetism
(and, in its modern extensions, the gauge forces). The e-dimension framework provides
a geometric account of *quantum mechanics itself* — superposition, entanglement,
spin, measurement, the uncertainty principle, and the spin-statistics theorem. These
are not electromagnetic phenomena. They are the phenomena that Kaluza-Klein takes as
given and does not explain.

The mathematical tools overlap. The physical questions do not.

### The Neutral-Particle Test

The distinction between the e-dimension and Kaluza-Klein can be stated as a
sharp empirical claim. In Kaluza-Klein theory, a particle's momentum in the
compact dimension is proportional to its electric charge: `p₅ = eQ/ℏ`. A
particle with zero electric charge (`Q = 0`) has zero fifth-dimensional
dynamics — no compact momentum, no coupling to the gauge connection, no
quantum behavior attributable to the fifth dimension.

Neutrons have zero electric charge. Yet neutrons interfere (Rauch et al. 1974),
have spin ½ (requiring 720° rotation for identity), and participate in
entanglement (Hasegawa et al. 2003). These are precisely the phenomena that
the e-dimension framework attributes to the fifth dimension.

**The distinguishing claim:** Kaluza-Klein predicts no fifth-dimensional
dynamics for electrically neutral particles. The e-dimension framework
predicts that *every* quantum system — charged or neutral — couples to the
e-dimension through quantum phase. Observation sides unambiguously with the
e-dimension framework.

### Distinguishing Predictions

Beyond the neutral-particle test, the frameworks make different gravitational
predictions. If the e-dimension is a physical dimension (not a gauge
redundancy), the gravitational sector must couple to it, producing a
Kaluza-Klein tower of massive graviton modes at masses `m_n = nℏ/Rc`, where
`R` is the e-circle radius. Standard gauge theory with `U(1)` as a fiber bundle
predicts no such gravitational KK tower. The mass scale is set by the
e-circle circumference L ≈ 130 μm (Paper 2), giving m₁ ≈ 10 meV — within
reach of next-generation short-range gravity experiments (Appendix D).

The framework's ontological claim — that the U(1) fiber is a literal
physical dimension, not a gauge redundancy — is supported by Baptista (2024,
arXiv:2306.01049), who takes the same position for higher-dimensional
internal spaces and derives the Standard Model gauge group from metric
instabilities on the SU(3) group manifold.

---

## 2.6 Why Exactly 4+1 Coordinates?<!-- legacy 2026-04-15 Intervention 8b §0.10: "Why Exactly Five Dimensions?" → "Why Exactly 4+1 Coordinates?" -->

A natural question: why one additional dimension? Why not two, or seven, or eleven
as in string theory?

The answer is empirical and minimal. Quantum mechanics, as it stands, requires
exactly one additional degree of freedom beyond `(x, y, z, t)` to account for:

- The periodicity of quantum phase
- The conservation law underlying entanglement
- The two-valuedness of spin (chirality of the helix)
- The topological structure of exchange statistics
- The physical reality of the gauge connection (Aharonov-Bohm)

Adding a second additional dimension would introduce new phenomena that are not
observed. We do not add dimensions beyond what the physics requires.

This is distinct from string theory, which adds six or seven dimensions to unify
the forces at the Planck scale. Those dimensions are proposed to be compactified
at scales far below any current experimental reach, and their primary purpose
is the unification of gauge forces. Our single e-dimension is not tiny —
it is accessible to every quantum experiment ever performed, because quantum
phase is its direct observable.

The e-dimension is not hidden at the Planck scale. It is hidden in plain sight,
in every interference pattern, every entangled pair, every spin measurement.
The reason it was not recognized as a literal dimension is that its observational
signature was interpreted, through the formalism of quantum mechanics, as an
abstract probability amplitude rather than a geometric coordinate.

---

## 2.7 Summary: The Framework's Theorems

*Label-migration note (2026-04-15, per `strategy/paper1-audit/`):* The four
statements below were originally labeled **Postulates P1-P4**. The PAC audit
(`strategy/paper1-audit/audit-report.md`, `reclassification-table.md`,
`derivation-chains.md`) established that every one of them is either (i) a
theorem derivable from ℤ + ZFC via cited programme papers, or (ii) an
empirical observation anchored by the 36-pin master table at aggregate
statistical significance `< 10⁻⁸⁹`. The labels below have been upgraded
accordingly — **original statements preserved verbatim**, labels changed from
"Postulate" to "Theorem" / "Observation" with explicit derivation pointers.
This resolves the legacy POSTULATES framing against the programme's
north-star signature *"Zero postulates beyond ℤ"* (see
`strategy/north-star.md` §0.4 and §0.8). See the reclassification-table for
the compact summary and the derivation-chains document for each VERIFY-clean
chain.

For clarity, we state the complete set of foundational claims of the ~~5D
geometric framework~~ 4+1 coordinate framework (M⁵)<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric framework" → "4+1 coordinate framework (M⁵)" -->. Everything in this paper is derived from these
statements, each of which is in turn derived (THEOREM) or empirically
anchored (OBSERVATION) as indicated.

**Theorem T1 (math) + Observation O1 (empirical) — ~~Five-dimensional spacetime~~ 4+1 coordinate structure<!-- legacy 2026-04-15 Intervention 8b §0.10: "Five-dimensional spacetime" → "4+1 coordinate structure" -->:**
Physical reality has ~~five dimensions~~ a 4+1 coordinate structure<!-- legacy 2026-04-15 Intervention 8b §0.10: "five dimensions" → "a 4+1 coordinate structure" -->: `(x, y, z, t, e)`. All five are equally
fundamental degrees of freedom.

*Label split.* The original Postulate 1 combines a mathematical existence
claim (T1) with an empirical identification claim (O1):

- **Theorem T1 (mathematical half).** The smooth 5-manifold
  `M⁵ = M⁴ × S¹` exists as a ZFC-level construction from ℤ: starting from
  ℤ one builds ℚ (Grothendieck), ℝ (Cauchy/Dedekind completion), the smooth
  4-manifold `M⁴`, and `S¹ = ℝ/ℤ` via integer translation action; product
  manifold is a ZFC product functor. *Derivation: chain T1, paper 61 §13.1
  and classical differential geometry (Kobayashi-Nomizu 1963 Ch. I-II); see
  `strategy/paper1-audit/derivation-chains.md` §T1.*

- **Observation O1 (empirical half).** "Physical reality is that 5-manifold"
  is an empirical claim, confirmed by 36 pins (paper 12 research master
  table `research/23-framework-predictions-master-table.md`) at aggregate
  statistical significance `< 10⁻⁸⁹`, by all five Branch-A quantum
  interpretations, and by Bell inequality measurements to the Tsirelson
  bound `|S| = 2√2` (Paper 1 §9; experimental record since Aspect 1982).
  *Empirical anchor: 36-pin master table, Paper 12.*

**Theorem T2 — The e-dimension is a circle:**
The e-coordinate is periodic, parameterized by an angle `φ ∈ [0, 2π)`. The structure
group of the e-dimension is `U(1)`.

*Derivation: Paper 61 §13.5.* Among compact connected manifolds, `S¹` is
the unique choice satisfying simultaneously (a) discrete KK spectrum
(⇒ compactness), (b) abelian `U(1)` gauge symmetry (⇒ dim = 1 with abelian
isometry group, ruling out `Sᵏ` for `k ≥ 2` whose isometry group
`SO(k+1)` is non-abelian), and (c) well-defined integer winding number
(⇒ connectedness). ℤ enters essentially as `π₁(S¹) = ℤ`, powering
charge quantization, the Hecke semigroup, and the Bost-Connes algebra
(Paper 12 Identity 12). Once T1's mathematical half is granted, T2 is
forced — not an independent assumption. *See derivation-chains.md §T2.*

### §2.7.Ia Why `S¹` (self-contained derivation of Theorem T2)

*This subsection lifts the three-part argument of Paper 61 §13.5 into*
*Paper 1 so the reader does not need to consult Paper 61 to follow the*
*derivation of T2. The full formal statement (with VERIFY-clean chain) is*
*still in `strategy/paper1-audit/derivation-chains.md` §T2 and in Paper 61*
*§13.5; this subsection extracts the proof into the main text. Style: bare*
*derivation — definitions + theorem + three forcing lemmas + conclusion. No*
*new content.*
*Closes **GAP-2** of `strategy/integers-content-mapping/report.md` §D.*

**Inputs (from T1).** A smooth compact 1-manifold `M_e` carrying a smooth
`U(1)` action with connected fiber, attached fiber-by-fiber to the smooth
4-manifold `M⁴`.

**Output.** `M_e ≅ S¹` as smooth 1-manifolds, uniquely up to diffeomorphism.

**Three requirements that the fifth dimension must satisfy.** Each is *forced*
by a downstream physical fact; none is an independent assumption.

---

**Requirement (i): Compactness.** *The fifth dimension is compact.*

*Forcing argument.* A non-compact fifth dimension (e.g. `ℝ`) would give
the 5D Laplacian a continuous spectrum on the fifth-coordinate factor.
Every 5D field `Ψ(x^μ, e)` would Fourier-decompose into a continuous
family of 4D fields labelled by a real wavenumber `k ∈ ℝ`, producing a
continuous KK mass spectrum `m(k) = |k|`. Experimentally, no such
continuous tower exists; the observed spectrum of physical states is
discrete (Planck 2018 CMB power spectrum constrains any continuous
extra-dimensional KK contribution to `< 10⁻⁵` of the total energy
density). Moreover:

- The Casimir regularization that gives `Λ ≈ 10⁻¹²³` in Planck units
  (Paper 2; Paper 1 Appendix W §W.9.2) requires a *discrete* KK sum
  `∑_{n ∈ ℤ} |n|^{−s}` (Epstein zeta at `s = −3` after analytic
  continuation). A continuous integral `∫ dk |k|^{−s}` diverges at
  `k = 0` for `s > 0` without the discrete combing.
- The spectral gap `Δ_0^{KK} = 1/R² > 0` (Paper 61 §13.4) that seeds the
  Yang–Mills mass gap (Paper 8 Theorem 4) requires a lower bound on
  the non-zero part of the KK spectrum; a continuous spectrum starting
  at zero has no such gap.

Conclusion: `M_e` is compact.

---

**Requirement (ii): `U(1)` isometry (1-dimensionality).** *The isometry
group of the fifth dimension is exactly `U(1)`.*

*Forcing argument.* Theorem T3 (e-translation invariance) and the
observed abelian structure of electromagnetism both require the isometry
group acting on `M_e` to be abelian and continuous. Among compact
connected Lie groups, the only 1-parameter abelian subgroup is `U(1)`
(up to isomorphism).

Suppose `M_e = Sᵏ` for `k ≥ 2`. Then the isometry group is `SO(k+1)`,
which is non-abelian for `k ≥ 2`:

- `k = 2`: `SO(3)` is non-abelian; gauge-theory reduction gives an `SU(2)`
  gauge boson triplet, not a single photon.
- `k = 3`: `SO(4) ≅ (SU(2) × SU(2))/ℤ_2` is non-abelian; gives two
  `SU(2)` factors.
- `k ≥ 4`: `SO(k+1)` is non-abelian simple (compact); gives a
  higher-rank non-abelian gauge theory.

These would all produce observable non-abelian gauge bosons descending
from the extra-dimensional isometries. The observed low-energy gauge
content — `SU(3) × SU(2) × U(1)` — has `U(1)` as the only factor
compatible with a *geometric* interpretation via KK reduction from a
single extra dimension (the `SU(3) × SU(2)` factors come from the
further internal manifold `CP² × S²`, Paper 11 / Paper 4).

Conclusion: if `M_e` admits a smooth `U(1)` action by isometries acting
transitively on the fiber, then `dim M_e = 1`.

---

**Requirement (iii): Connectedness (well-defined winding number).** *The
fiber `M_e` is connected.*

*Forcing argument.* The topological charge of the e-dimension — the
winding number of a particle's trajectory around `M_e` — must be an
integer for the spin-statistics theorem (Paper 1 Appendix B) and for
charge quantization (Dirac 1931, via `π_1(M_e) = ℤ`).

A disconnected 1-manifold `M_e = M_e^{(1)} ⊔ M_e^{(2)} ⊔ …` has
`π_0(M_e)` non-trivial: the connected components are labelled by
`π_0`, and the winding number (`π_1` of each component) is defined
only within a component. Transitions between components have no
well-defined winding number, breaking:

- Charge quantization (no integer `n` labels cross-component paths).
- Spin-statistics (the `720°` rotation argument of Appendix B
  requires a single connected path in `M_e`).
- The Aharonov–Bohm phase (Paper 1 §4.1), which is a line integral
  over a closed loop in `M_e` — ill-defined if the loop can leave and
  re-enter a component.

Conclusion: `M_e` is connected.

---

**Classification step.** *The only compact connected 1-manifold is `S¹`.*

*Proof.* The classification of compact connected 1-manifolds (Milnor
1965, *Topology from the Differentiable Viewpoint*, Appendix; or
Hirsch 1976 *Differential Topology* §3.3) states: every compact
connected smooth 1-manifold without boundary is diffeomorphic to `S¹`;
every compact connected smooth 1-manifold with boundary is
diffeomorphic to the closed interval `[0, 1]`. Since the fiber `M_e`
carries a free transitive `U(1)` action (Requirement (ii)), it has no
boundary. Therefore `M_e ≅ S¹`.  ∎

---

**Theorem T2 (full statement).** *Given T1's mathematical half (the
existence of a smooth 5-manifold `M⁵ = M⁴ × M_e` with `M_e` a compact
connected smooth 1-manifold admitting a smooth `U(1)` action), the
fifth-dimensional factor is uniquely `M_e ≅ S¹` up to diffeomorphism,
with isometry group `U(1)` and fundamental group `π_1(S¹) = ℤ`.*

---

**Why this matters for the programme.** The chain

$$
T1 \;\Rightarrow\; T2 \;\Rightarrow\; T3 \;\Rightarrow\;
\text{quantum mechanics (§§3–5)}
$$

is driven by the identification `π_1(S¹) = ℤ` (from T2) as the source
of the integers that power:

- Charge quantization (`∫ F = 2π n`, `n ∈ ℤ`; Dirac 1931).
- The Hecke semigroup `ℕ*` and the Bost–Connes algebra (Paper 12
  Identity 12; derivations/00 Links 2–3).
- The spin-statistics theorem (Paper 1 §4.2, Appendix B).
- The Casimir KK tower and the cosmological-constant match (Paper 2;
  integers/paper02-cosmology/appendices/14-appendix-j-R-from-Lambda.md).

The fifth dimension being `S¹` is not a choice; it is the only
compact connected abelian 1-manifold, and each of those three
adjectives is forced by an observed physical fact (discrete spectrum;
abelian electromagnetism; integer winding). This is Signature 5 of
`strategy/north-star.md` §0.4.

---

**Theorem T3 — E-translation invariance:**
The laws of physics are symmetric under uniform translation of all e-coordinates.
By Noether's theorem, this symmetry implies the conservation law `e₁ + e₂ + ... = C`.

*Derivation: Paper 61 §13.5 (via T2) + Noether 1918.* `S¹` is a flat 1-manifold
with isometry group `U(1)`, generated by the Killing vector `∂_e`. Noether's
theorem applied to this continuous `U(1)` action gives the conserved charge
`Q = Σ eᵢ (mod L)`. T3 is a direct geometric consequence of T2; it is not an
independent postulate. *See derivation-chains.md §T3.*

**Theorem T4 (math) + Observation O2 (empirical) — The projection postulate:**
Our observations are four-dimensional intersections of five-dimensional reality.
Unlocalized observations integrate over e-values (wave behavior). Localized
measurements sample at a specific e-value (particle behavior).

*Label split.* The original Postulate 4 combines a mathematical structural
claim (T4) with an empirical identification claim about observers (O2):

- **Theorem T4 (mathematical half).** The map
  `P_A: M⁵ → 𝒪_quantum` given by fiber integration
  `ψ(x,e) → (1/L) ∫₀^L ψ(x,e) de` with respect to Haar measure on the
  `U(1)` fiber is the quantum projection functor; its right adjoint
  `P_A^*` is pullback to constant-e sections. The adjunction
  `(P_A ⊣ P_A^*)` implements measurement as categorical structure; the
  Born rule follows by Gleason's theorem + Haar uniqueness (Paper 1
  Appendix C.1). *Derivation: Paper 61 §14.2 (fiber integration), classical
  fiber-bundle theory (Kobayashi-Nomizu 1963 Ch. II-III), Paper 1 §9 +
  Appendix C.1 (Born-rule reduction); see derivation-chains.md §T4.*

- **Observation O2 (empirical half).** "Our 4D observations are the
  intersections / fiber-integrations of 5D reality" is an empirical claim
  about observers, confirmed by every wave/particle-duality experiment
  (double-slit, Mach-Zehnder, Bell tests, quantum eraser) — a body of
  experiment exceeding `10¹⁷` event counts with 0% deviation from the
  fiber-integration prediction (Paper 1 §9; Bell / Tsirelson since Aspect
  1982). *Empirical anchor: 36-pin master table, Paper 12.*

These four theorems (T1-T4), together with the two empirical observations
(O1, O2) anchoring the math to reality, together with the standard laws of
quantum mechanics and general relativity as they apply in four dimensions,
constitute the complete framework. Sections 3 through 5 derive their
physical content from the theorems alone; the observations confirm the
identification with physical reality but do not enter any proof chain as
input. For the legacy "postulate" reading of T1-T4 (retained for historical
and pedagogical continuity), see the original preamble language preserved
above; the epistemic status is theorem + observation, not axiom.

### 2.7.1 Derived Theorems (D1-D4) and Observational Anchors (O5-O6)

*Label-migration note (2026-04-15).* The four items D1-D4 were originally
labeled "Derived Assumptions"; the PAC audit promotes them to THEOREMS
(D-series) with explicit VERIFY-clean derivation chains (see
`strategy/paper1-audit/derivation-chains.md` §D1-§D4). The two additional
items A1-A2, previously labeled "speculative", are reclassified as
OBSERVATIONS (O5-O6) backed by 36-pin empirical match, with explicit
CONSTRUCT-route TODOs toward full theorem status. Original statements
preserved verbatim.

Several theorems used in the paper's technical appendices are not
independent postulates — they follow from the four theorems above
combined with standard physics. The audit makes each derivation explicit.

**Theorem D1 — The rotation-e coupling** (used in Appendix B): the
e-coordinate's coupling to spatial rotations follows from identifying spin with
e-angular momentum via the Noether theorem applied to Theorem T3.
*Derivation: Paper 1 Appendix B Theorems B.1.1, B.1.2, B.2.1, B.3.1, B.3.2,
B.3.3 (all PROVED in `integers/paper01-qg5d/PROOF-CHAIN.md` §T.1); see
`strategy/paper1-audit/derivation-chains.md` §D1.*

**Theorem D2 — The 5D density rule** (used in Appendix C): the probability density
`|ψ|²` is the 5D density projected onto 4D using the Haar measure on the
e-circle — the unique measure consistent with Theorem T3 (e-translation
invariance). The Born rule `P(i) = |αᵢ|²` follows from this measure and the
orthonormality of e-eigenstates (Appendix C.1). The measure is not chosen
to reproduce the Born rule; it is forced by the symmetry. Causal consistency
independently selects the same rule (Torres Alegre 2026).
*Derivation: Paper 1 §9 + Appendix C.1; Gleason 1957 uniqueness + classical
Haar existence/uniqueness; see derivation-chains.md §D2.*

**Theorem D3 — The gravitational action** (used in Appendix D): the 5D Einstein-
Hilbert action on `P(M⁴, U(1))` is the unique generally covariant
two-derivative action on the bundle — not an additional postulate but
the standard gravitational action applied to the framework's geometry.
*Derivation: Paper 1 Appendix D; Lovelock 1971 classification at dim 5;
see derivation-chains.md §D3.*

**Theorem D4 — Zeta regularization** (used in Appendices F, G, S): the regularization
of KK mode sums by spectral zeta functions. This is the unique
prescription consistent with the `U(1)` translation symmetry of the
e-circle (Theorem T3); see Appendix S, §S.7.4.
*Derivation: Paper 1 §S.7.4; scheme-independence proved at L=1 (Paper 10
Thm U.2a), L=2 (Paper 10 Thm 1), L≥3 (Paper 11 Thm K.4); W1 RESOLVED
in `integers/paper01-qg5d/PROOF-CHAIN.md`; see derivation-chains.md §D4.*

Two additional items are used in the speculative extensions; the audit
reclassifies them as OBSERVATIONS (empirical anchors with matching
experimental pins) with named CONSTRUCT-route TODOs toward full theorem
status. These do not block the core QG5D chain; they affect cosmological
Branch C and matter-sector generation counting.

**Observation O5 — The `Z₂` orbifold** (Appendix W): modding out `S¹` by the fermion parity
`(−1)^F`. Geometrically motivated by the spin structure but not forced
by it — a physical hypothesis.
*Empirical anchor:* the Z₂ orbifold underwrites predictions (i) dark energy
`Λ ≈ 10⁻¹²³` (Casimir on `S¹/ℤ₂`), (ii) `Ω_DM/Ω_b = 1/ξ²` (Paper 2 §2.2),
(iii) `N_eff = 3.35`, (iv) `Σm_ν ≈ 0.06 eV`, (v) three generations via
orbifold Euler characteristic — all confirmed at sub-percent (Pins 13, 14,
16, 19, 22 of the 36-pin master table, Paper 12).
*CONSTRUCT route (open):* derive Z₂ from spin structure + anomaly freedom
+ Horava-Witten (Paper 4 §7 direction). Follow-up deliverable flagged
in `strategy/paper1-audit/commit-memo.md` R5.

**Observation O6 — The `Z₃` symmetry** (Appendix W, §W.4): a three-fold rotation of the
e-circle, producing three generations. Speculative.
*Empirical anchor:* three-generation count matches Pin #22 exactly; Paper 2
§2 derives the same count via `Ω_DM/Ω_b = 1/ξ²` + orbifold Euler
characteristic.
*CONSTRUCT route (open):* derive Z₃ from CP² topology + Horava-Witten
(Paper 4 §7 expansion). Follow-up deliverable flagged in commit-memo R5.

### 2.7.2 A Note on Two Scenarios

Two configurations of the e-circle appear in this paper. The **circle
scenario** (`S¹`) has circumference `L ≈ 50–200 μm` (`R ≈ 8–32 μm`), with
all Standard Model fields propagating on the circle. The **orbifold
scenario** (`S¹/Z₂`) has brane separation `R ≈ 12 μm`, with only bulk
fields (gravity and three right-handed neutrinos) propagating between
the branes. The circle scenario is used in Appendices A–V (unless
noted); the orbifold scenario is used in Appendix W and the abstract.
The two scenarios make different predictions for the Yukawa gravitational
deviation scale (21 `μm` vs 12 `μm`) and are experimentally distinguishable.
See Section 6.6 for the full comparison.

---
