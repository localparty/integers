# Paper 5 — Section 2: The Topology of CP² and Color Flux Tubes

## 2.1 The Topology of CP²

The complex projective plane CP² is the coset space `SU(3)/(SU(2)×U(1))`.
Its cohomology groups are:

    H⁰(CP², Z) = Z
    H²(CP², Z) = Z       ← the key: a non-trivial 2-cycle
    H⁴(CP², Z) = Z
    H^{odd}(CP², Z) = 0

The generator of `H²(CP², Z)` is the Fubini-Study 2-form `ω_FS`,
normalized so that `∫_{CP¹} ω_FS = 1`. The CP¹ ⊂ CP² is the
non-contractible 2-cycle — topologically a 2-sphere embedded in CP².

This is the crucial topological fact: **CP² contains a non-contractible
2-sphere**. A Wilson loop traced around this 2-cycle cannot be
continuously deformed to a point. It carries a topological invariant.

## 2.2 The SU(3) Wilson Loop on the Non-Contractible Cycle

Consider the SU(3) gauge field `A_a(y)` on CP² (where `y^a` are the
CP² coordinates, `a = 1,...,4`). The Wilson loop around the generator
of `H²(CP², Z)` is:

    W_{CP¹} = Tr P exp(i ∮_{CP¹} A_a dy^a)

where P denotes path ordering around the non-contractible CP¹ ⊂ CP².

In the confining vacuum, this Wilson loop has a vacuum expectation
value:

    ⟨W_{CP¹}⟩ = 0

This is the statement of confinement in the CP² language: the vacuum
average of the Wilson loop around the non-contractible cycle vanishes.
In contrast, in the deconfined (quark-gluon plasma) phase:

    ⟨W_{CP¹}⟩ ≠ 0   (deconfined)

The Polyakov loop — the order parameter for the deconfinement phase
transition — maps directly to this CP² Wilson loop. The deconfinement
temperature `T_c ≈ 155 MeV` is the temperature at which `⟨W_{CP¹}⟩`
becomes non-zero. In the framework, this transition temperature is set
by the CP² Casimir energy at finite temperature — calculable.

## 2.3 Projection to 4D: Color Flux Tubes

In the 11D framework, quarks are localized on the visible brane at
`φ = 0`. Their color charges are endpoints of SU(3) gauge field
configurations on CP².

A quark-antiquark pair at 4D positions `x` and `y` sources a chromoelectric
field configuration on CP². By the non-trivial topology of CP², this
field configuration cannot spread out in all directions — it is
topologically forced to form a flux tube along the shortest path
connecting the two sources.

The 4D projection of this CP² flux tube is the **color string** between
quark and antiquark. Its properties:

**Orientation:** Along the geodesic in `M⁴` between the quark positions.

**Width:** Set by the CP² radius `r₃ ~ 10⁻³¹ m` projected onto 4D
through the KK reduction. The physical string width is:

    d_string ~ r₃ / (g₃ r₃ M_Pl) = 1/(g₃ M_Pl) ~ Λ_QCD^{-1} ~ 1 fm

consistent with the measured proton radius.

**Tension:** The energy per unit length of the flux tube (§3).

## 2.4 Why the Flux Tube Cannot Break (At Low Energy)

In 4D QCD, a sufficiently energetic string can break by producing a
quark-antiquark pair from the vacuum. The string tension `σ` sets the
energy scale for string breaking: a string of length `L > 2m_q/σ` will
break.

In the geometric picture: string breaking corresponds to a CP² gauge
field configuration developing a node — a zero of the flux tube field
— at some intermediate point. The cost of this node is set by the
CP² curvature energy, which is of order `m_q × Λ_QCD`.

For light quarks (`m_q < Λ_QCD`): the node is energetically accessible.
Strings break, producing hadrons — consistent with observation.

For heavy quarks (`m_q > Λ_QCD`): the energy cost of string breaking
exceeds the string energy at short distances. The charmonium and
bottomonium spectra exhibit long-lived bound states — the confining
potential dominates before string breaking. The geometric picture is:
the CP² flux tube is stable when the quark mass exceeds the Casimir
energy scale.

## 2.5 The Deconfinement Phase Transition

At temperature `T > T_c ≈ 155 MeV`, quarks are deconfined in a
quark-gluon plasma. In the geometric picture:

At low T: the CP² gauge field configuration has `⟨W_{CP¹}⟩ = 0`.
The non-contractible 2-cycle carries non-trivial flux. Flux tubes form.

At high T: thermal fluctuations excite the CP² gauge field, restoring
the Z₃ center symmetry of SU(3). The Wilson loop acquires a non-zero
VEV. Flux tubes dissolve. Quarks move freely.

The transition temperature is set by the CP² Casimir energy at finite
temperature:

    T_c ~ (CP² Casimir energy)^{1/4} ~ Λ_QCD ~ 200 MeV

This is the same dimensional analysis that gives `Λ_QCD` from the CP²
compactification scale — the deconfinement temperature and the
confinement scale are the same geometric quantity, as expected from
the QCD phase diagram.
