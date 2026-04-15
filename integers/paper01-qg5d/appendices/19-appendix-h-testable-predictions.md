# Appendix H — Testable Predictions of the 4+1 Framework (M⁵)<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Framework" → "4+1 Framework (M⁵)" -->

<!-- Vocabulary canon note (Intervention 8b, 2026-04-15, aggressive migration applied): this file uses "5D" / "five-dimensional" as subject-matter language. Per strategy/north-star.md §0.10 (Vocabulary Canon), canonical phrasing is "4+1 coordinate structure" / "M⁵" / "internal phase". Inline strikethrough migrations applied per Intervention 8b to thesis sentences, H1 heading, and high-salience passages. -->

> This appendix consolidates every testable prediction that distinguishes the
> 5D e-dimension framework from a pure interpretation of quantum mechanics.
> Each prediction is stated with its numerical value, its theoretical origin
> within the framework, the experiment that could test it, and the current
> experimental status.

---

## H.1 Why This Appendix Matters

An interpretation of quantum mechanics that makes the same predictions as
standard QM is metaphysics, not physics. The 5D framework began as an
interpretation (Sections 2-3 of the paper), but the development of the
gravity program (Section 5, Appendices D-G) and the Casimir calculation
(Section 6.6) has produced concrete predictions that go beyond standard QM.

This appendix collects them in one place, organized by experimental
accessibility. The predictions range from "within reach of current
experiments" to "requires Planck-scale physics." We state each one honestly,
with its assumptions and caveats.

---

## H.2 Prediction 1: Modified Gravity Below ~100 `μm`

### Statement

Newton's inverse-square law receives a Yukawa correction at short distances:

    F(r) = −GMm/r² × [1 + α_G e^{−r/λ}]

with characteristic length scale:

    **λ ≈ 8–32 μm**    (best estimate: ~21 μm)

and coupling strength `α_G` of order unity.

### Origin

The e-circle of circumference `L ~ 50–200 μm` (determined by the Casimir dark
energy calculation, Section 6.6) produces Kaluza-Klein graviton modes with
mass `m_n = nℏ/(Rc)`. The `n = 1` mode mediates a Yukawa force with range
`λ = R = L/(2π)`. Higher KK modes (`n > 1`) produce shorter-range corrections.

### Experimental Test

Torsion balance and MEMS cantilever experiments measuring gravitational
force at separations below 50 `μm`.

### Current Status

| Experiment | Scale reached | Result | Our prediction |
|-----------|--------------|--------|---------------|
| Lee et al. (2020) | 52 `μm` | No deviation | `λ ~ 21 μm`: not yet probed |
| Kapner et al. (2007) | 56 `μm` | No deviation | Consistent |
| Westphal et al. (2021) | ~100 `μm` | No deviation | Consistent |
| Near-future MEMS | 1–10 `μm` target | In development | **Will test** |

**Assessment:** Not yet tested. Within reach of next-generation experiments
(5–10 year timescale).

---

## H.3 Prediction 2: The Dark Energy Density from Field Content

### Statement

The cosmological constant is determined by the Standard Model field content
and the e-circle circumference:

    ρ_Λ = (π²/90) × (ℏc/L⁴) × |N_B − (7/8)N_F|

With the Standard Model (`N_B = 28`, `N_F = 90`):

    ρ_Λ = (50.75 π²/90) × ℏc/L⁴

### Origin

The Casimir energy of the Standard Model fields on the compact e-circle,
with boundary conditions determined by spin (Appendix B.1: bosons periodic,
fermions anti-periodic).

### Experimental Test

This is a CONSISTENCY prediction rather than a new measurement. If the
e-circle circumference `L` is measured independently (through short-range
gravity, Prediction 1), the predicted `ρ_Λ` can be compared to the observed
value. A match would be striking. A mismatch constrains the framework.

The equation of state is predicted to be `w = −1` exactly (a true cosmological
constant, not dynamical dark energy). Current measurement: `w = −1.03 ± 0.03`
(Planck 2018).

### Current Status

**Consistent** with observations. Not independently testable until `L` is
measured. The `w = −1` prediction is testable by future cosmological surveys
(DESI, Euclid, Roman Space Telescope).

---

## H.4 Prediction 3: A Scalar Field at the meV Scale

### Statement

The e-circle radius `φ(x)` is a dynamical scalar field (the dilaton) with
mass:

    **m_φ ~ ℏ/(Rc) ~ 1–10 meV**

It couples to matter with gravitational strength (`~G_N × mass`).

### Origin

The Kaluza-Klein reduction of the 5D metric produces a scalar field — the
local e-circle radius (Appendix D, Section D.4.3). Its mass is set by the
stabilization potential, which is of order the inverse e-circle radius.

### Experimental Test

A meV-scale scalar field coupled gravitationally is an "ultralight" particle.
It could manifest as:
- A fifth force with range `λ_φ = ℏ/(m_φ c) ~ 20 μm` (same as Prediction 1)
- A contribution to the Casimir effect at `μm` separations
- An ultralight dark matter component
- Anomalous neutron scattering at meV energy transfers

### Current Status

Partially constrained by fifth-force experiments (see Prediction 1). A
dedicated search for a meV-scale scalar coupled to mass has not been
performed but is feasible with current neutron scattering or Casimir
force measurement technology.

---

## H.5 Prediction 4: KK Graviton Spectrum

### Statement

The graviton has a tower of massive excitations with masses:

    m_n = nℏ/(Rc) ≈ n × (1–10 meV)    for n = 1, 2, 3, ...

Each massive graviton has spin-2 and couples to the stress-energy tensor
with strength `G_N` (same as the massless graviton).

### Origin

The Kaluza-Klein decomposition of the 5D graviton on `S¹` (Appendix F,
Section F.1.2). The massive modes are the Fourier modes of the graviton
field on the e-circle.

### Experimental Test

Massive spin-2 particles coupled gravitationally at the meV scale are
extremely difficult to detect directly. Indirect signatures:
- Modifications to the gravitational wave spectrum at frequencies
  `f ~ m₁c²/h ~ 2.4 THz` (far above LIGO/LISA sensitivity)
- Threshold effects in high-energy collisions (if `L` is at the larger end
  of the range)
- Contributions to the Casimir force (spin-2 Casimir effect)

### Current Status

**Not yet testable** with current technology. The THz frequency range is
accessible to table-top optics experiments but the gravitational coupling
is extremely weak. This prediction may become testable with future
gravitational wave detectors at higher frequencies.

---

## H.6 Prediction 5: Perturbatively Finite Graviton Scattering

### Statement

Graviton-graviton scattering amplitudes are FINITE at every order in
perturbation theory, regulated by the compact e-circle.

The specific prediction: the 2-to-2 graviton scattering amplitude at
center-of-mass energy `√s` does NOT diverge as `√s → E_Planck`. Instead, it
saturates at a finite value determined by the number of KK modes:

    A(s) → A_max ~ G₄ × s × n_max² ~ G₄ × s × (L/l_P)²

### Origin

The perturbative finiteness established in Appendices F (one-loop) and G
(two-loop, all-orders conjecture). The compact e-circle provides a natural
UV regulator through the discreteness of the KK spectrum and the zeta
regularization of mode sums.

### Experimental Test

Graviton scattering at Planck energies is not experimentally accessible.
However, the finiteness of the theory has INDIRECT consequences:
- The quantum corrections to Newton's constant (running of `G` with energy)
  are calculable and finite — they predict specific modifications to
  gravitational physics at energies approaching the Planck scale
- Black hole entropy should be finite and calculable in the 5D framework
- The gravitational contribution to vacuum energy is finite (related to
  Prediction 2)

### Current Status

**Not directly testable.** Indirect tests through cosmological observations
(primordial gravitational waves, black hole thermodynamics) are the most
promising avenue.

---

## H.7 Prediction 6: Anyon Statistics from Topology

### Statement

In any physical system where the effective spatial dimension is reduced to
two, fractional exchange statistics (anyons) MUST appear — as a geometric
consequence of the winding number classification.

Specifically: for the fractional quantum Hall state at filling `ν = 1/m`,
the quasiparticle exchange phase is:

    e^{iθ} = e^{iπ/m}

### Origin

The winding number argument (Appendix B.1, Theorem B1.3): in `d = 2`,
`π₁(SO(2)) = Z` allows any winding number, giving continuous exchange phases.
This prediction was first made by Leinaas & Myrheim (1977) using the same
topological logic.

### Experimental Test

Fractional quantum Hall interferometry.

### Current Status

**Confirmed.** Bartolomei et al. (Science, 2020) and Nakamura et al.
(Nature Physics, 2020) directly measured anyon braiding statistics in
FQH systems. The measured exchange phases match the topological prediction.

This is the framework's strongest experimental consistency check: the
geometric reasoning that produces the boson-fermion dichotomy in 3D also
reproduces anyon statistics in 2D, and both are experimentally confirmed.
The anyon prediction itself was made by Leinaas & Myrheim (1977) using the
same topological logic; the framework reproduces their result within the
e-dimension picture rather than predicting it independently.

---

## H.8 Prediction 7: No Variation of the Fine Structure Constant

### Statement

If the e-circle radius is stabilized (as required for Prediction 2), the
fine structure constant `α` does NOT vary with cosmic time:

    dα/dt = 0

### Origin

In the Kaluza-Klein framework, the electromagnetic coupling depends on the
e-circle radius. A stable e-circle gives a stable `α`. An expanding e-circle
(the alternative dark energy scenario) would give `|Δα/α| ~ 2|ΔR/R|`, which
is constrained by quasar absorption spectra to `< 10⁻⁵` over cosmological
time.

### Experimental Test

Quasar absorption spectra, atomic clock comparisons, the Oklo natural
reactor constraint.

### Current Status

**Consistent.** Current bounds (Webb et al. 2011, Rosenband et al. 2008)
show `|Δα/α| < 10⁻⁵` cosmologically and `< 10⁻¹⁷/year` locally. The stable
e-circle scenario predicts exactly zero variation.

---

## H.9 Summary Table

| # | Prediction | Value | Test | Status | Timescale |
|---|-----------|-------|------|--------|-----------|
| 1 | Modified gravity at short range | `λ ~ 21 μm` | Torsion balance, MEMS | Not yet tested | 5–10 years |
| 2 | Dark energy from Casimir energy | `ρ_Λ` from SM field content + `L` | Cosmological surveys | **DESI tension** (`4.2σ` vs `w=−1`) | Ongoing |
| 2b | `N_eff` from dilaton | `ΔN_eff ≈ 0.05` (after intra-tower decays) | CMB-S4 | **Consistent** (ACT+SPT: `2.81±0.18`; tower dynamics reduce naive `0.57` to `~0.05`) | 5–10 years |
| 3 | meV-scale scalar field (dilaton) | `m_φ ~ 1–10 meV` | Neutron scattering, Casimir | Partially constrained | 5–10 years |
| 4 | KK graviton tower | `m_n = n × (1–10 meV)` | High-frequency GW, Casimir | Not testable (current) | 10+ years |
| 5 | Finite graviton scattering | No UV divergences | Indirect (cosmology, BH) | Not testable (current) | Far future |
| 6 | Anyon statistics in 2D | `θ = π/m` for `ν = 1/m` FQH | FQH interferometry | **Confirmed** | Done |
| 7 | Constant `α` | `dα/dt = 0` | Quasar spectra, atomic clocks | **Consistent** | Ongoing |
| 8 | Normal neutrino mass ordering | `m₃ > m₂ > m₁` from `Z₃` geometry | JUNO (data taking since Aug 2025) | Hinted at `2–3σ` (NOvA, T2K, SK) | 3–6 years |
| 9 | No QCD axion (strong CP topological) | `θ̄ = 0` (conjecture pending; see Appendix X §X.3.3 for open requirements: π₃(SU(3)) instanton analysis, quark mass phase, 4D effective theory) | ADMX, ABRACADABRA, IAXO | Not yet excluded | Ongoing |
| 10 | `H₀ ≈ 68.0–68.7 km/s/Mpc` (hidden-brane dark radiation) | `ΔN_eff = 0.02–0.14`, `ξ < 0.384` (BBN); `ξ < 0.397` (ACT DR6 `3σ`) | CMB-S4, TRGB/JWST, GW sirens | Tier 1 **consistent** with ACT DR6+DESI (`68.2–68.4`); Tier 2 in `2.5–2.8σ` tension with ACT DR6 | 5–10 years |

---

## H.10 The Hierarchy of Evidence

The predictions form a hierarchy from established to speculative:

**Confirmed experimentally:**
- Anyon statistics (Prediction 6) — the framework's topological reasoning
  is validated by FQH experiments

**Consistent with all current data:**
- Constant `α` (Prediction 7)
- Dark energy equation of state `w = −1` (Prediction 2)
- No gravitational deviations above 52 `μm` (Prediction 1)

**Testable within 5–10 years:**
- Modified gravity at `~21 μm` (Prediction 1) — this is the framework's
  make-or-break experimental test
- meV-scale scalar field (Prediction 3)

**Requires future technology:**
- KK graviton tower (Prediction 4)
- Perturbatively finite scattering (Prediction 5)

---

## H.11 What Would Falsify the Framework

The framework makes specific claims that are falsifiable:

**If short-range gravity experiments find NO deviation down to 1 `μm`:**
The Casimir dark energy scenario (`L ~ 50–200 μm`) is ruled out. The framework
as an interpretation survives (it can accommodate any `R`), but the specific
testable prediction is falsified.

**If `w ≠ −1` is measured definitively:**
The Casimir cosmological constant scenario is ruled out. The expanding
e-circle scenario might survive.

**If anyon statistics were NOT observed in 2D systems:**
The winding number classification would be falsified. (This has not happened
— anyons ARE observed.)

**If the two-loop divergence of 5D KK gravity is shown to persist despite
zeta regularization:**
The perturbative finiteness conjecture is falsified. The framework survives
as an interpretation but the quantum gravity program fails.

**If Bell inequalities were NOT violated:**
The entire framework would be falsified — the e-conservation constraint
requires the quantum correlations. (This has not happened — Bell violations
are thoroughly confirmed.)

**If JUNO finds inverted neutrino mass ordering (`m₁ > m₃`):**
The simple `Z₃` bulk seesaw geometry is falsified. (More complex bulk profiles
could accommodate inverted ordering, so this would constrain but not
decisively rule out the `Z₃` scenario.)

**If axion searches (ADMX, ABRACADABRA, IAXO) discover the QCD axion:**
The topological strong CP conjecture (Appendix X) is falsified. Since this
is a conjecture (not a derived result — see Appendix X §X.3.3 for the three
open requirements), this would rule out that particular resolution but
would not falsify the core e-circle framework.

**If CMB-S4 finds `N_eff` consistent with `3.046 ± 0.03`**: the mirror sector
is absent at the needed level. The framework is left with `H₀ ≈ 67.7` (tower
only). This would also constrain `ξ < 0.14`, essentially ruling out any
thermally populated hidden brane.

**If multiple independent `H₀` methods converge above `71 km/s/Mpc`**: both
Tier 1 and Tier 2 of the framework's prediction are insufficient. Physics
beyond the minimal orbifold is required (lighter modulus from Appendix L,
or additional bulk species not present in the minimal model).

**If ACT DR6 extended-parameter fits (`ΛCDM + N_eff + w₀ + wₐ`) tighten
further**: the window for Tier 2 could close entirely, leaving only
Tier 1 (`H₀ ≈ 68.0–68.3`) as the allowed prediction.

The framework is falsifiable at multiple levels. The most immediate tests are
Prediction 1 (modified gravity at `~21 μm`), Prediction 8 (neutrino mass
ordering from JUNO), Prediction 9 (no QCD axion), and Prediction 10 (`H₀ ≈ 68.0–68.7` from CMB-S4 `N_eff` detection and JWST-calibrated distance measurements).

---

## H.12 Referee-Requested Summary: Seven Predictions with Full Metadata

The following table provides, for each of the seven primary quantitative
predictions, the four items requested by journal referees: (i) current
experimental status, (ii) quantitative prediction with uncertainty,
(iii) what falsifies it, (iv) whether it is unique to this framework or
generic to extra-dimension models.

| # | Prediction | Quantitative value | Framework-unique? | Falsification | Current status | Timeline |
|---|------------|-------------------|-------------------|--------------|----------------|---------|
| 1 | Gravitational deviation at short range | Yukawa deviation at λ ~ R ≈ 12 μm (Scenario 1) to 21 μm (Scenario 3); α ~ O(1) | Specific scale from dark energy matching — generic extra-dim models have free R | Any experiment ruling out Yukawa forces at 12-21 μm scale with O(1) coupling | Not yet excluded; current limits from Eöt-Wash reach ~50 μm; Stanford torsion pendulum extends to ~10 μm | 3-5 years |
| 2 | Dark photon kinetic mixing | ε = α_EM × π²/6 × exp(-π) ≈ 5.0 × 10⁻⁴ (within ~20% from subleading corrections) | Specific formula from two-brane KK tower mediation; generic models have ε as free parameter | ε outside range 2-8 × 10⁻⁴ at A' mass m_{A'} = n₁/R ~ 16 meV | Not yet probed at this (ε, mass) point; below current FASER sensitivity | 3-7 years (LDMX, LHCb Run 3-4) |
| 3 | Neutrino masses | m_ν ~ meV scale from bulk seesaw with M_R ~ 1/R²M_Pl; normal ordering from Z₃ geometry | Scale tied to R; ordering from geometry | Inverted hierarchy measured by JUNO or KamLAND-Zen | Normal ordering preferred by current oscillation fits; mass scale consistent | 5-8 years (JUNO) |
| 4 | N_eff from KK neutrino contribution | N_eff = 3.31-3.39 (three scenarios; see Paper 2) | Specific prediction from three bulk RHN; generic models have this as free parameter | N_eff < 3.1 at 2σ from CMB-S4 | 3-4σ tension with ACT DR6 N_eff = 2.86 ± 0.13; consistent with Planck+BAO | 5-8 years (CMB-S4) |
| 5 | H₀ from hidden brane dark radiation | H₀ = 68.7-69.5 km/s/Mpc | Dark radiation contribution from ξ = T_hidden/T_visible fixed by Ω_DM/Ω_b ratio | H₀ < 67 or > 71 km/s/Mpc from multiple independent probes | Consistent with Planck+BAO (67.4 ± 0.5); below SH0ES (73.0 ± 1.0); helps but does not resolve H₀ tension | Currently testable |
| 6 | Dark energy equation of state | w = -1 exactly (perturbative Casimir V = c/R⁴ is exact to all orders; dilaton frozen) | The w = -1 prediction comes from dilaton being frozen to ε ~ 10⁻⁵²; differs from quintessence | w ≠ -1 at > 2σ from DESI DR3 or Euclid | Current DESI DR2 shows 4.2σ tension with static w = -1; if the quintessence interpretation holds, framework w = -1 is in tension | 2-3 years (DESI DR3) |
| 7 | Mirror dark matter signal | Hidden-brane baryons with same spectrum as SM but no electromagnetic coupling | Generic dark matter models have no visible mirror baryons | Direct detection of mirror baryon with SM nuclear interactions at low cross section | Not probed; distinctive phenomenology (dark atoms, mirror neutrinos) | 10+ years |

**Notes on uniqueness (column 4).** Predictions 1-4 are quantitatively specific
to the framework because their numerical values are fixed by the single parameter
R = 12 μm, which is itself fixed by the dark energy matching. Generic extra-
dimension models with a free compactification radius would have these as free
parameters. The framework's predictions are therefore falsifiable at the specific
numerical values listed, not merely "consistent with extra dimensions."
