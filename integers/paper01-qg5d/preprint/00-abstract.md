# Spin-Statistics, Aharonov-Bohm, and Perturbative Finiteness from M⁵ = M⁴ × S¹

<!-- Title migration (Intervention 8b, 2026-04-15, user-approved 2026-04-15): legacy title "Spin-Statistics, Aharonov-Bohm, Perturbative Finiteness, and Twenty-Two Derivations from Kaluza-Klein Geometry" → canonical title above per strategy/north-star.md §0.10 (Vocabulary Canon) §0.1 (naming hierarchy). Rationale: (1) "Kaluza-Klein Geometry" inherits Kaluza-Klein theory's postulational register; "M⁵ = M⁴ × S¹" states the derived object precisely. (2) The legacy "Twenty-Two Derivations" was the PROOF-CHAIN.md Branch A-D tree-position count (items #1-22) spanning Paper 1 + Paper 2; it is not a live tally. Post paper-1-audit (strategy/paper1-audit/) the clean Paper-1-only tally is 15 theorems + 6 observations; with Branch E pins the programme surfaces 36 pins separately. Dropping the count keeps the title robust to future expansion and matches the north-star "description of what's derivable" register. Structured counts live in strategy/proof-chain/qg5d/PROOF-CHAIN.md where they can evolve without title drift. -->

<!-- Vocabulary canon note (Intervention 8 + 8b, 2026-04-15): this paper (Paper 1 / QG5D) was drafted with "five-dimensional" / "5D" / "fifth dimension" as subject-matter terms throughout. Per strategy/north-star.md §0.10 (Vocabulary Canon), the canonical phrasing is "4+1 coordinate structure" (four spacetime coordinates + one internal U(1) phase fiber — the e-circle S¹) / "M⁵" / "internal phase". The terms refer to the same structure: M⁵ = M⁴ × S¹. Intervention 8b (user-approved 2026-04-15) applied aggressive inline strikethrough migration across all prose files; reviewer-runs / journal-reviewer / code / bibliography remain preserved as external correspondence / build artifacts. Programme-P1-P4 labels that appeared as "Postulates" in early drafts have been reclassified to Theorems T1-T4 per strategy/paper1-audit/; see the legacy-annotation comments inline throughout this paper's preprint files. -->

> **Editorial Note:** This paper presents results at three rigor levels, clearly
> labeled in §1.5 and Table 1.1. The central mathematical result — the Universal
> Epstein Vanishing theorem (Theorem K.1) and the BPHZ Factorization theorem
> (Theorem K.3), establishing perturbative UV finiteness of linearized 5D
> KK gravity under zeta regularization — is independent of the geometric
> interpretations of quantum mechanics (Sections 3–4). Referees whose primary
> competence is in the gravitational/finiteness direction are directed to
> Appendices F, G, K, S, U, and §G.9b. Referees whose primary competence is in
> foundations/geometric interpretations are directed to Sections 3–4 and
> Appendices B, C. The paper is designed to allow independent evaluation of each
> part, and the epistemic labels in Table 1.1 are intended to make this structure
> explicit.

## Abstract

<!-- legacy 2026-04-15 Intervention 8 §0.10: "We propose that spacetime is five-dimensional" — original postulational framing; canonical form per Vocabulary Canon reads "We derive that spacetime has a 4+1 coordinate structure (four spacetime coordinates fibered over a U(1) internal phase, the e-circle S¹)." The paper's technical content is unchanged; "five-dimensional" is retained throughout this paper as the subject-matter term for reader familiarity and historical continuity — see strategy/north-star.md §0.10 for the canon and strategy/paper1-audit/ for the T1-T4 reclassification that removes the postulational reading. -->
~~We propose that spacetime is five-dimensional~~ We derive that spacetime has a 4+1 coordinate structure — `(x, y, z, t, e)` — where the
~~fifth dimension~~ internal phase<!-- legacy 2026-04-15 Intervention 8b §0.10: "fifth dimension" → "internal phase" --> `e` is circular, periodic, and corresponds to the `U(1)` fiber in
a principal bundle over four-dimensional spacetime. Our four-dimensional
experience is a projection of this ~~five-dimensional reality~~ 4+1 coordinate structure (M⁵)<!-- legacy 2026-04-15 Intervention 8b §0.10: "five-dimensional reality" → "4+1 coordinate structure (M⁵)" -->, and every quantum
phenomenon is a geometric consequence of the projection. This paper develops
the `M⁴ × S¹` sector — a ~~5D truncation~~ 4+1 truncation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D truncation" → "4+1 truncation" --> capturing quantum mechanics and
electromagnetism — which embeds naturally into a full 11-dimensional framework
(`M⁴ × CP² × S² × S¹`) developed in companion papers.

Within this framework, superposition is extension in the `e`-dimension,
entanglement is conservation of the `e`-coordinate (`e₁ + e₂ = C`), momentum is
helical pitch (`∂e/∂x = p/ℏ`), spin is helical chirality, and measurement is
`e`-space sampling. The wave function is not an abstract probability amplitude —
it is the literal shape of the particle in ~~five-dimensional spacetime~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "five-dimensional spacetime" → "M⁵" -->.

We present three original results. First, the Aharonov-Bohm effect is derived
as the holonomy of the `e`-bundle around a topological defect, establishing the
physical reality of the vector potential from geometry. Second, the
spin-statistics theorem is derived from a single geometric fact: the winding
number of a particle's helix through the circular `e`-dimension determines both
its spin (via the Noether theorem) and its exchange statistics (via parallel
transport). Integer winding gives bosons; half-integer gives fermions; fractional
winding in two dimensions gives anyons — confirmed experimentally in the
fractional quantum Hall effect. Third, the Born rule `P(i) = |αᵢ|²` is reproduced within
the ~~five-dimensional~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "five-dimensional" → "M⁵" --> density interpretation and the projection functor (Theorem T4;
strategy/paper1-audit/derivation-chains.md §T4), and the
framework reproduces the quantum correlations that violate the CHSH Bell
inequality (`|S| = 2√2`), with the non-locality sourced by the `e`-conservation
constraint through the ~~fifth dimension~~ internal phase (S¹)<!-- legacy 2026-04-15 Intervention 8b §0.10: "fifth dimension" → "internal phase (S¹)" -->.
<!-- legacy 2024 framing, reclassified 2026-04-15 per strategy/paper1-audit/ -->
<!-- Original: "the Born rule P(i) = |αᵢ|² is reproduced within the five-dimensional density interpretation and the projection postulate" -->

The same compact `e`-circle also resolves the central obstacle to quantum
gravity. The ~~five-dimensional~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "five-dimensional" → "M⁵" --> Einstein-Hilbert action on the `e`-bundle reduces
via Kaluza-Klein decomposition to four-dimensional gravity coupled to
electromagnetism and a scalar field in a single metric. The compactness of
the `e`-circle converts the continuous UV momentum integrals of 4D quantum
gravity into discrete Kaluza-Klein mode sums that admit zeta regularization.
For linearized ~~5D gravity~~ M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" --> on `M⁴ × S¹`, under zeta regularization of the
KK mode sums, the leading UV divergence vanishes identically at every loop
order:
`S₀^{(L)} = [1 + 2ζ(0)]^L = 0`. The subleading terms are Epstein zeta
functions evaluated at non-positive integers. For the two-loop `R³` counterterm of linearized ~~5D gravity~~ M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10 --> on `M⁴ × S¹`
— corresponding to the Goroff-Sagnotti divergence that proved 4D Einstein
gravity non-renormalizable in 1986 — the result under zeta regularization
is stronger than expected: the `R³` coefficient is **identically zero at
every order in the mass expansion**, not just at leading order. The sunset
topology produces the Epstein zeta of the Eisenstein lattice,
`E₂(s; n²+nm+m²) = 6ζ(s)L(s,χ₋₃)`, which vanishes at every negative
integer through complementary trivial zeros of `ζ(s)` and `L(s,χ₋₃)` — a
result specific to the two-loop sunset topology on the A₂ (Eisenstein)
lattice, superseded at higher loops by the Universal Epstein Vanishing theorem
(Theorem K.1), which establishes `E_L(-j; Q) = 0` for all `j ≥ 1`, all loop
orders `L`, and any positive-definite quadratic form `Q` via the single
structural fact `1/Γ(-j) = 0`. The
figure-eight and vertex correction topologies vanish independently through
the trivial zeros of the Riemann zeta at even negative integers (forced
by the perfect-square structure of KK masses). Ghost contributions, carrying the same
Eisenstein quadratic form through KK number conservation, vanish by the
same mechanisms. Under spectral zeta regularization of the KK mode sums,
linearized ~~5D gravity~~ M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" --> on `M⁴ × S¹` is perturbatively UV finite: every
loop-order KK counterterm coefficient vanishes identically. This is established
through two loops by explicit computation (Appendices F and G), and at all
orders by two theorems working in tandem: the Universal Epstein Vanishing
theorem (Appendix K, Theorem K.1) proves that `E_L(-j; Q_L) = 0` for all
`j ≥ 1` and any positive-definite `Q`, and the BPHZ Factorization theorem
(Theorem K.3) establishes — via joint holomorphicity of the Epstein zeta
function in Schwinger parameters — that BPHZ-subtracted amplitudes preserve
the Epstein zeta structure at all loop orders. The factorization is verified
explicitly at `L = 1` and `L = 2`; at `L ≥ 3` it relies on Theorem K.3 and
Weinberg locality, and a Route-C explicit three-loop computation remains an
open task (§K.5.2). **Whether the zeta-regularized zero is
scheme-independent — i.e., whether it reflects a property of physical
on-shell observables rather than of the regularization scheme — is not
demonstrated in this paper and is identified as the critical open problem.**
The comparison with Goroff-Sagnotti (1986) is between different theories
(4D pure gravity vs. ~~5D KK gravity~~ M⁵ KK gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D KK gravity" → "M⁵ KK gravity" --> with full KK tower) and between different
regularization schemes; a same-theory, same-observable comparison is the
necessary next step. Counterterm coefficients are determined from two
parameters: `G₄` and the `e`-circle circumference `L`.

The compact e-circle, with fermions anti-periodic and bosons periodic, has a
natural Z₂ orbifold interpretation with two fixed-point branes. The visible
brane supports Standard Model matter; the hidden brane gravitates normally but
couples to no SM force. The Casimir energy of bulk fields on the orbifold,
with three right-handed neutrinos to ensure positivity, matches the observed
dark energy density for brane separation R ≈ 12 μm and predicts Yukawa-type
gravitational deviations at that scale — a unique signature testable by
short-range gravity experiments currently underway. The same construction
gives neutrino masses at the meV scale and kinetic mixing between brane U(1)
fields at ε ~ 5 × 10⁻⁴ (from α_EM × π²/6 × exp(-π)), testable by LDMX and
LHCb Run 3. These are quantitative predictions following from the single
parameter R fixed by dark energy matching. Further consequences at higher
rigor levels (including baryon asymmetry, fermion generations, and mass
hierarchies) are detailed in §1.5 and the companion papers.

What is established in this paper is a geometric framework in which the same
compact circle that provides a geometric account of quantum mechanics also
produces perturbative finiteness of linearized ~~5D gravity~~ M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" --> via the Universal
Epstein Vanishing theorem. The spin-statistics theorem, the Aharonov-Bohm
effect, and the Born rule each receive geometric interpretations that, while
using the same logical foundations as their standard derivations, provide
the geometric picture that those derivations cannot supply. A full accounting
of the twenty-two phenomena addressed at three levels of rigor, together with
the epistemic status of each result, appears in §1.5 and Table 1.1.

A companion computation (Paper 2) applies the CAMB Boltzmann solver to
the framework's cosmological sector (to appear separately) with parameters
derived entirely from the `e`-circle geometry — fitting zero parameters to
CMB data. The central result is a scaling law from bulk leptogenesis on
the `Z₂` orbifold: the three bulk right-handed neutrinos deposit baryon
asymmetries on both branes, but the hidden brane is colder
(`ξ = T_hidden/T_visible`). The entropy asymmetry (`1/ξ³`) and washout
suppression (`1/ξ²`) combine to give:

    Ω_DM / Ω_b = 1/ξ²

Inverting against the observed ratio 5.36 determines `ξ = 0.432` at leading
order; the washout correction shifts this to `ξ ≈ 0.49`, converging with
the independently `θ*`-matched value `ξ = 0.47`. Three scenarios bracket
the prediction. The CAMB-computed results: `t₀ = 13.47–13.60` Gyr, `H₀ = 68.7–69.5` km/s/Mpc, `S8 = 0.753–0.785` (resolving the `4σ` weak lensing
tension without tuning), `r_d = 145.8–148.0 Mpc`, and the CMB angular
scale `θ*` matched to within 0.5–6.6 arcseconds of Planck's measurement.
The dilaton dark energy equation of state — **revised to `w = −1`
exactly** (the perturbative Casimir V = c/R⁴ is exact to all orders;
the dilaton is frozen at ε ~ 10⁻⁵², stabilized by the Casimir minimum of the
orbifold potential: the Casimir energy of bulk fields on the Z₂ orbifold has a
minimum at R ~ 12 μm, and the flatness of this minimum suppresses dilaton
evolution to ε ~ 10⁻⁵² relative to the Planck time (detailed in the companion
Paper 6)) — makes the expansion history
consistent with `ΛCDM` at the w level. Remaining deviations from
`ΛCDM` come from elevated `N_eff` and lower `Ω_m`, testable by
DESI DR3 and CMB-S4. The cosmic coincidence
`Ω_DM/Ω_b ≈ 5` is not a coincidence: it is `1/ξ²`, where `ξ` is fixed by
geometry and baryogenesis. All three scenarios predict `N_eff = 3.31–3.39`,
in `3–4σ` tension with ACT DR6 (`N_eff = 2.86 ± 0.13`) — the framework's
primary open issue, definitively resolved by CMB-S4 (`σ(N_eff) ≈ 0.03`).
