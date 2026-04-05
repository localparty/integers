## 6. Hawking Radiation Structured in e


### 6.1 The Modified Hawking State

Standard Hawking radiation is described by a density matrix:

    ρ_Hawking = Σ_n e^{-nω/T_H} |n⟩⟨n| / Z

This is a thermal state — maximum entropy, no information.

In the 5D framework, the full state of the Hawking radiation is:

    |Ψ_Hawking⟩ = Σ_{n,φ} α_{n,φ} |n, φ⟩

where `φ` is the e-coordinate of each emitted quantum and `α_{n,φ}`
encodes the e-imprint from the horizon. The 4D projection is:

    ρ_4D = Tr_e [|Ψ_Hawking⟩⟨Ψ_Hawking|]
          = Σ_n e^{-nω/T_H} |n⟩⟨n| / Z

The thermal density matrix is recovered exactly by tracing over `e`.
Hawking's result is the 4D shadow of the full 5D state.

### 6.2 Why Hawking Computed the Shadow

Hawking's Bogoliubov transformation was performed entirely in 4D.
It did not include the e-dimension. In the language of the 5D
framework, his calculation computed:

    ρ_rad = Tr_e [ρ_5D]

— the partial trace over the e-dimension of the full 5D state.
This is mathematically identical to what he computed: tracing over
the "interior" states of the black hole is, in the 5D framework,
tracing over `e`. The result is necessarily thermal.

Hawking's calculation is not wrong. It is a 4D projection of a 5D
reality, and projections lose information by construction.

### 6.3 The Information in e-Correlations

The full 5D state `|Ψ_Hawking⟩` contains correlations between the
e-coordinates of successive Hawking quanta:

    φ_n = f(φ_1, φ_2, ..., φ_{n-1}, {φ_infalling bits})

where the function `f` encodes the accumulated e-imprints from all
infalling bits via e-conservation. These correlations are:

- **Invisible in 4D:** Any 4D measurement on individual quanta or
  on the 4D correlations of the radiation will see a thermal state.
  The e-correlations do not appear in any `(x,y,z,t)` measurement.

- **Complete in 5D:** A 5D observer with access to the e-coordinates
  of all emitted Hawking quanta could reconstruct the e-coordinates
  of all infalling bits from the e-conservation constraints. The
  information is completely encoded.

- **Unitary:** The map from infalling e-coordinates to outgoing
  e-coordinates is a unitary transformation — it is e-conservation
  applied iteratively. No information is destroyed. The evolution
  is unitary in 5D even though it appears non-unitary in 4D.

### 6.4 Unitarity from e-Conservation

We prove that the map from infalling to outgoing e-coordinates is
unitary.

**Theorem 6.1** *(Unitarity of the e-scattering matrix).*
*The S-matrix for black hole formation and complete evaporation,
in the full 5D theory, is unitary.*

**Proof sketch.** The e-conservation law `Σ φ_i = C` is the Noether
charge of the `U(1)` translation symmetry of the e-circle (Paper 1,
Section 2.2.3). By Noether's theorem, this symmetry generates a
one-parameter family of unitary operators `U(α) = e^{iαQ_e}`, where
`Q_e` is the conserved e-charge. The time evolution operator of the
full 5D theory commutes with `Q_e`:

    [Ĥ₅D, Q̂_e] = 0

This implies that the S-matrix `S₅D = T exp(-i∫Ĥ₅D dt)` preserves
the e-charge at every step:

    S₅D† S₅D = I

The proof requires that the 5D path integral is well-defined — that
no perturbative divergences destroy unitarity. This is established
by the perturbative finiteness theorem (Paper 1, Appendix S, Theorem
S.1): the L-loop effective action is finite at every order, with
counterterm coefficients uniquely determined by Epstein zeta values.
No uncontrolled divergences arise to break unitarity.

The S-matrix maps the space of infalling e-configurations `{φ_in}`
to the space of outgoing Hawking e-configurations `{φ_out}` via the
iterative application of e-conservation at each horizon interaction
vertex. Since each vertex preserves e-charge, and the composition of
unitary maps is unitary, `S₅D` is unitary. `∎`

**What the 4D observer sees:** The 4D S-matrix is obtained by
tracing over the e-coordinates:

    S_4D = Tr_e [S_5D]

This trace produces a non-unitary map (a thermal channel) — exactly
Hawking's result. The apparent non-unitarity is an artifact of the
partial trace, not of the underlying evolution.

---

