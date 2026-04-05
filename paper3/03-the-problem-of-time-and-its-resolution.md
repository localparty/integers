## 3. The Problem of Time and Its Resolution


### 3.1 The Problem

The information paradox is fundamentally a question about time
evolution: does a pure initial state evolve unitarily to a pure
final state? But quantum gravity has a prior, deeper problem: the
*problem of time*.

In canonical quantum gravity, the Hamiltonian constraint requires:

    H|Ψ⟩ = 0

This is the Wheeler-DeWitt (WDW) equation (DeWitt 1967). It says
the wave function of the universe is *static* — it does not evolve.
There is no Schrödinger equation, no time derivative, no dynamics.
Time has disappeared from the fundamental description.

The problem has multiple facets (Isham 1992, Kuchař 1992):

1. **The frozen formalism:** `H|Ψ⟩ = 0` admits no time evolution.
   How do we extract the manifest dynamics we observe?

2. **The Hilbert space problem:** In standard QM, the Hilbert space
   is defined at a moment of time. In quantum gravity, "a moment of
   time" is gauge-dependent. What is the arena for quantum states?

3. **The multiple choice problem:** There are many inequivalent ways
   to define "time" in GR (proper time, coordinate time, York time,
   conformal time). They can disagree at the quantum level. Which
   is correct?

Any resolution of the information paradox must first answer: what
does "unitary time evolution" mean in a theory where time is absent
from the fundamental equations?

### 3.2 The e-Dimension as Internal Clock

In the 5D framework, the resolution is immediate.

The quantum phase evolves as:

    ∂φ/∂τ = −E/ℏ

where `τ` is proper time along a worldline and `E` is the particle's
energy (Paper 1, Section 3.3). The e-coordinate `φ` records the
passage of time geometrically — it is an internal clock, ticking
at a rate proportional to the energy, embedded in the geometry of
the compact dimension.

This clock is:

- **Gauge-invariant:** The e-coordinate is a scalar on the
  e-bundle. It does not depend on the choice of spacetime
  coordinates, time slicing, or gauge fixing.

- **Metric-independent:** The e-evolution `∂φ/∂τ = −E/ℏ` holds
  regardless of the background spacetime metric. Near a black hole,
  in an expanding universe, or in flat space — the e-clock ticks.

- **Universal:** Every quantum system has an e-coordinate. Every
  particle carries this clock. The clock is not an external
  apparatus — it is a geometric property of the particle itself.

### 3.3 The Wheeler-DeWitt Equation as a 4D Projection

The WDW equation `H|Ψ⟩ = 0` is a constraint on the 4D wave
function. In the 5D framework, the full wave function is:

    Ψ₅D(x, t, φ) = Σₙ ψₙ(x, t) · e^{inφ/R}

where `ψₙ(x, t)` are the KK mode wave functions and `n` indexes
the e-momentum (charge) quantum number. The 5D Hamiltonian is:

    Ĥ₅D = Ĥ₄D + Ĥ_e

where `Ĥ_e` is the e-circle Hamiltonian, whose eigenvalues are
`E_n = n²ℏ²/(2mR²)` — the KK tower.

The WDW constraint `Ĥ₅D|Ψ₅D⟩ = 0` does NOT say the 5D state is
static. It constrains the *total* energy (4D + e-circle) to vanish:

    Ĥ₄D|ψₙ⟩ = −E_n|ψₙ⟩

Each KK sector evolves with energy `E_n`. The 4D wave function `ψₙ`
has non-trivial dynamics — it satisfies a Schrödinger equation with
energy sourced by the e-circle. The apparent timelessness of the
WDW equation is an artifact of looking at the total (4D + e) system.
When we separate the e-sector, the 4D sector has dynamics because
the e-clock provides the reference.

This is precisely the **Page-Wootters mechanism** (Page & Wootters
1983): time emerges from entanglement between a "clock" subsystem
and the rest of the universe. In their framework, one defines:

    |ψ(t)⟩ = ⟨t_clock|Ψ_total⟩

— the conditional state of the universe given that the clock reads
time `t`. This conditional state evolves unitarily even though the
total state is static.

In the e-dimension framework: **the clock is the e-circle.** The
conditional state:

    |ψ(φ)⟩ = ⟨φ|Ψ₅D⟩

is the 4D state conditioned on the e-coordinate value `φ`. As `φ`
varies (tracing around the e-circle), the 4D state evolves —
unitarily, because the underlying 5D evolution is unitary. The WDW
equation `H|Ψ₅D⟩ = 0` simply states that the total (4D + e-clock)
energy vanishes — a constraint, not the absence of dynamics.

### 3.4 Euclidean Time and the e-Circle

The connection between time and the e-dimension has a second,
independent manifestation in the Euclidean (thermal) formulation.
We derive it from the near-horizon metric.

**The near-horizon 5D geometry.** The Schwarzschild metric in the
5D KK framework (Paper 1, Appendix O, Section O.2.1) is:

    ds² = f(r) c²dt² − f(r)⁻¹ dr² − r² dΩ² + R₀² dφ²

where `f(r) = 1 − r_s/r`, `r_s = 2GM/c²`, and `φ ∈ [0, 2π)` is
the e-circle coordinate. Near the horizon (`r → r_s`), define the
proper distance `ρ` from the horizon:

    ρ = ∫_{r_s}^{r} f(r')^{-1/2} dr' ≈ 2√(r_s(r − r_s))

so `f ≈ ρ²/(4r_s²)`. The near-horizon metric becomes:

    ds² ≈ (ρ²κ²) c²dt² − dρ² − r_s² dΩ² + R₀² dφ²

where `κ = 1/(2r_s) = c⁴/(4GM)` is the surface gravity.

**The Euclidean section.** Wick-rotating `t → −it_E`:

    ds²_E ≈ ρ²κ² c²dt_E² + dρ² + r_s² dΩ² + R₀² dφ²

The `(ρ, t_E)` sector is a flat plane in polar coordinates
`(ρ, κct_E)`. Regularity at `ρ = 0` (the horizon) requires that
`κct_E` be periodic with period `2π`:

    κct_E ∼ κct_E + 2π

This fixes the Euclidean time period:

    β_H = 2π/(κc) = 8πGM/(c⁴) × c = 8πGM/c³

giving `T_H = ℏc³/(8πGMk_B)` — the Hawking temperature, derived
purely from regularity of the Euclidean metric.

**The identification.** The Euclidean section of the 5D metric near
the horizon has the topology `R² × S² × S¹`, where the `R²` is the
`(ρ, κct_E)` plane. The `κct_E` direction is an angular coordinate
with period `2π`. The e-circle coordinate `φ` is also an angular
coordinate with period `2π`. Both have identical periodicity and
identical spin structure:

    Bosons:   Ψ(t_E + β_H) = +Ψ(t_E)  and  Ψ(φ + 2π) = +Ψ(φ)
    Fermions: Ψ(t_E + β_H) = −Ψ(t_E)  and  Ψ(φ + 2π) = −Ψ(φ)

The bosonic periodicity is the KMS condition. The fermionic
anti-periodicity is the spin structure of Paper 1, Appendix B. The
two circles — the thermal circle of Euclidean time and the geometric
e-circle — are isomorphic as spin manifolds:

    (S¹_thermal, period β_H, spin structure) ≅ (S¹_e, period 2π, spin structure)

The identification map is:

    φ = 2π t_E / β_H = κ c t_E

**What this means.** The Hawking temperature is not imposed from
outside — it is the statement that the thermal circle and the
e-circle are the same geometric object near the horizon. The
e-circle, which produces the spin-statistics theorem (Paper 1,
Appendix B), the Born rule (Appendix C), and quantum phase (Section
2.3), is also the object whose periodicity gives the black hole its
temperature.

The thermal nature of Hawking radiation is a geometric consequence
of the e-circle's periodicity. The same compact dimension that makes
particles fermions or bosons also makes black holes hot.

### 3.5 Why This Matters for the Information Paradox

The problem of time is the prerequisite obstacle. If time evolution
is meaningless in quantum gravity, then "unitary evolution" is
meaningless, and the information paradox dissolves into incoherence
rather than being resolved.

The e-dimension framework restores dynamics:

1. **Time exists.** The e-clock provides a gauge-invariant notion
   of temporal progression that survives quantization of the metric.

2. **Evolution is unitary.** The 5D evolution operator preserves
   inner products because the 5D action has no anomalies (the
   perturbative finiteness of Paper 1 ensures this).

3. **The question is well-posed.** We can meaningfully ask whether
   the S-matrix for black hole formation and evaporation is unitary
   in the full 5D theory.

With time and unitarity restored, the information paradox becomes
a precise question with a precise answer — developed in the
remaining sections.

---

