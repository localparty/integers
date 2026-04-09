## 4. The Horizon as S² × S¹ — Information Lives on the Surface


### 4.1 The Standard Picture vs the 5D Picture

In standard 4D general relativity, the event horizon is a 2-sphere
`S²` — a two-dimensional surface enclosing the black hole interior.
The Bekenstein-Hawking entropy `S = A/4` counts the information
capacity of this surface in Planck units.

In the 5D framework, the horizon is `S² × S¹` — the 2-sphere crossed
with the e-circle. At every point on the horizon, the e-circle is
attached as a fiber. The information content of the horizon includes
not just the area but the e-coordinate state at each point.

### 4.2 The Horizon Does Not Transmit — It Grows

The standard picture imagines infalling matter crossing the horizon
and entering the black hole interior. This is the assumption that
makes information loss seem inevitable: once inside, the information
is inaccessible.

The 5D framework suggests a different geometric picture. The horizon
is a dynamical surface. When matter approaches the horizon, the
horizon expands — by exactly one Planck area unit per infalling bit,
consistent with the Bekenstein entropy bound. The information does
not cross the horizon. The horizon grows to incorporate it.

This is consistent with the membrane paradigm (Thorne, Price &
Macdonald 1986), which treats the horizon as a physical membrane
with well-defined properties. It is also consistent with black hole
complementarity (Susskind, Thorlacius & Uglum 1993), which holds
that infalling information is both transmitted to the interior (for
the infalling observer) and encoded on the horizon (for the exterior
observer). The 5D framework provides the geometric mechanism for
the exterior encoding.

**The classical limit.** The discrete Planck-area growth events
occur at a rate set by the infalling flux. For a black hole of mass
`M >> M_Pl`, the flux of infalling matter corresponds to
`~10^(2S_BH)` growth events over the evaporation time — an
astronomically large number of discrete steps. In the classical
limit `M >> M_Pl`, the discrete area increments `ΔA = l_P² ≪ A`
are invisible at any classical or semiclassical resolution. The
smooth, continuously-shrinking horizon of the standard Hawking
calculation is recovered as the coarse-grained average of these
Planck-scale growth events, with corrections suppressed by
`M_Pl/M << 1`. This is the same limit in which any discrete quantum
spectrum (atomic energy levels, angular momentum eigenvalues)
reproduces the Bohr correspondence principle for large quantum
numbers. The discreteness is real at the Planck scale and invisible
above it.

Quantitatively: an isolated black hole satisfies T_H ≪ T_Hawking^{equilibrium},
so the Hawking emission rate exceeds any astrophysical accretion rate, and the net
mass evolution dM/dt = −(dM/dt)_{Hawking} + (dM/dt)_{accretion} ≈ −σ T_H⁴ A to
leading order in M_Pl/M; the discrete area-growth events from infalling matter
(each increasing A by l_P²) contribute at order (infalling flux) × l_P² ≪ (Hawking
flux) for an isolated black hole, so the standard semiclassical mass loss formula
dM/dt ~ −1/M² is reproduced to leading order with corrections suppressed by M_Pl/M,
confirming that the smooth classical dynamics emerge correctly from the discrete
Planck-scale picture.

### 4.3 The e-Coordinate of the Horizon — Derivation

When the horizon grows by one Planck pixel to incorporate a bit of
infalling information, the growth manifests as a change in the
e-coordinate of the horizon surface at that location. We derive
this from the e-conservation law explicitly.

**Geometric definition.** The event horizon of a Schwarzschild black
hole in the 5D framework is a null hypersurface in the 4D base M⁴.
The e-bundle restricts to this null hypersurface: at each point of
the 2-sphere S² of the horizon, an e-circle S¹ is attached as the
fiber of the principal U(1) bundle. The "e-coordinate of the horizon"
`φ_{horizon}` is the section of this restricted bundle — the
assignment of an e-circle position to each point of the horizon
2-sphere. As established in Section 9.3.2 (Gap 3), the e-Killing
vector `∂/∂φ` is spacelike everywhere, including at the horizon,
and `Q_e` is well-defined on the horizon hypersurface. The
"e-coordinate" is the eigenvalue of the e-charge operator `Q̂_e`
restricted to the horizon.

The e-conservation law (Paper 1, §2.2.3) states that for any
interaction vertex in the 5D theory, the sum of incoming
e-coordinates equals the sum of outgoing e-coordinates:

    Σ φ_in = Σ φ_out    (Noether charge of U(1) e-translation)

At the horizon interaction vertex, the infalling quantum (with
e-coordinate `φ_infalling`) is absorbed into the horizon surface
(with current e-coordinate `φ_horizon`). The outgoing state is the
modified horizon surface. By e-conservation:

    φ_infalling + φ_horizon = φ_horizon_new

    φ_horizon_new = φ_horizon + δφ    where δφ = φ_infalling

This is not an assumption — it is the direct application of the
Noether conservation law from Paper 1, Theorem 2.1. The infalling
quantum's e-coordinate is transferred to the horizon surface
because e-charge is conserved at every interaction vertex, just
as electric charge is conserved at every QED vertex.

**What is derived:** The mapping δφ = φ_infalling follows from
e-conservation alone. No additional assumption is required.

**What is argued:** That the e-conservation law applies at the
horizon vertex in the same way it applies in flat space. This
requires the 5D theory to remain well-defined near the horizon —
established by the UV finiteness result (Paper 1, Appendix S).

**The area quantization.** The derivation above establishes that each
infalling quantum deposits one unit of e-charge (`δφ = φ_{infalling}`)
on the horizon. What is the corresponding area increase?

This is not independently derived from the e-conservation law alone.
It follows from combining two results: (1) the e-conservation law at
the absorption vertex, which establishes the e-charge transfer;
(2) the Bekenstein-Hawking entropy formula `S_BH = A/(4l_P²)`, derived
in Section 8 from the entanglement entropy of KK modes across the
horizon after G-renormalization.

From Section 8.3: the entropy counts independent e-circle
configurations on the horizon, with each Planck-area cell supporting
one independent e-degree of freedom. `S_BH = N_{pixels}` where
`N_{pixels} = A/(4l_P²)`. Therefore one unit of entropy (one bit,
in natural units with `s₀ = 1` after G-renormalization, as derived
in Section 7 and established in Section 8.2) corresponds to one
Planck area and one e-charge unit. The "one Planck area per bit"
claim is the statement that these two units are the same — which is
forced by requiring consistency between the e-charge counting and the
entropy formula. It is derived from the conjunction of e-conservation
and `S_BH = A/4`, not from e-conservation alone.

The precise relationship between e-charge units and area eigenvalues
in the 5D quantum gravity theory — the analog of the LQG area
spectrum derivation — is not computed here. The claim is that the
semiclassical counting is consistent: one absorbed quantum increases
the entropy by one unit (one bit in Bekenstein units), and the entropy
formula assigns one Planck area per entropy unit. The derivation of
the exact area eigenvalue spectrum from the 5D operator algebra is
deferred to future work.

We therefore state explicitly: "Planck pixel creation" is an effective description
valid in the semiclassical limit M >> M_Pl, where discrete area-eigenvalue growth
events coarse-grain to the smooth Bekenstein area law. The underlying quantum gravity
process — the precise eigenvalue spectrum and creation operator algebra for Planck
area quanta in the 5D theory — is deferred to future work, consistent with the
acknowledgement throughout Section 4 that the semiclassical counting is confirmed to
be self-consistent while the full quantum gravity spectrum is an open problem.

### 4.4 Operator-Algebraic Identification: M_int and M_ext

*[Addendum: Tomita--Takesaki identification, April 2026.]*

The two-region structure of the horizon — interior and exterior —
that appears throughout this section is not merely a presentational
choice. Paper 12 (research/73, research/04) established that the
e-circle Hilbert space H_e is unitarily equivalent to the GNS space
of the Bost--Connes C*-algebra A_BC at the unique KMS_1 state omega_1
(Identity 12). The von Neumann closure pi_1(A_BC)'' is a type III_1
factor, and Tomita--Takesaki modular theory at beta = 1 provides:

- A modular conjugation J with J^2 = 1,
- Interior and exterior algebras M_int and M_ext satisfying
  J M_int J = M_ext,
- A modular flow sigma_t generated by the modular Hamiltonian
  H_BC = log Delta_{omega_1}.

The interior algebra M_int = pi_1(A_BC)''(P_F) consists of
observables inside the horizon's modular spectral window (where P_F
is the finite-rank spectral projector of H_BC on the Riemann
subspace H_R). The exterior algebra M_ext = pi_1(A_BC)''(1 - P_F)
consists of observables outside the horizon. The e-conservation
constraint Sum phi_i = C of Section 4.3 is the modular flow sigma_t
preserving the KMS_1 state omega_1.

In Tomita--Takesaki theory, any faithful normal state on a type III
factor *necessarily* produces the factorization M = M_int v M_ext
via the modular conjugation J. Paper 3's geometric intuition — that
the black hole must be understood as two regions connected by the
e-circle mechanism — was correct at the structural level. The
correction is that "connected by the e-circle mechanism" is now
identified as "connected by the Tomita--Takesaki modular conjugation
J at beta = 1."

> **Origin (G, ChatGPT conversation, 28 January 2026).**
>
> *"...in my mind when an object is added to the mass of a bh,
> it is added via spaghettification, so in my mind i see a 1-dimension
> strip... every bit added to the surface, changes the overall shape
> of the sphere... imagine that every plank pixel on the surface of
> the bh is sending a laser signal to a receiver in the outside of
> the event horizon, constantly, to send its position... those beams
> they are actually the hawking radiation intrinsic to every bh"*
>
> *"the realization that adding a single bit would have to change
> the shape of the whole object and that perpendiculars to the event
> horizon would all change with one bit, it's like the information
> of the bit is distributed but not erased"*
>
> *"because the amount of gravity slows time progression, change
> within a bh could not happen inside, cause it's frozen in time,
> relatively to observers outside, like us, so the only piece of the
> bh that could change relative to us, is the horizon"*

These statements contain, in compressed intuitive form, the core of
the Tomita--Takesaki identification: (1) "a receiver in the outside"
is the exterior algebra M_ext receiving the J-image of every interior
observable; (2) "distributed but not erased" is the modular
conjugation J as a bijection; (3) "the only piece that could change
is the horizon" is the modular flow sigma_t acting on the horizon
projector P_F while the interior is frozen under modular time (KMS
condition).

> **Origin (G, ChatGPT conversation, 12 September 2025).**
>
> *"maybe one of those 'hidden' dimensions could be interpreted
> functionally as the 'entanglement dimension' -- the axis along
> which two correlated states remain adjacent."*
>
> This is the e-circle. In the BC language, the "entanglement
> dimension" is the modular bimodule structure of J on H_R: the
> interior and exterior are "adjacent" in the modular conjugation
> sense — J maps one to the other without any propagation.

---

