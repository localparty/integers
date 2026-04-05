## 7. The Page Curve — Quantitative Recovery


### 7.1 Setup

Consider a black hole of initial mass `M_0` formed from collapse of
a pure state. The initial state has `N_0 = S_{BH} = A_0/(4l_P²)`
Planck pixels on the horizon, each carrying an e-coordinate `φ_i`
encoding the infalling information.

The black hole evaporates by emitting Hawking quanta one at a time
(in the semiclassical approximation). Each emitted quantum carries:

- A 4D state `|n_k⟩` (energy, momentum, spin) drawn from the
  thermal distribution at temperature `T_H`
- An e-coordinate `φ_k` determined by e-conservation from the
  horizon's e-configuration

After `k` emissions, the system has:

- `N_rad = k` Hawking quanta in the radiation
- `N_BH = N_0 - k` Planck pixels remaining on the horizon

### 7.2 The e-Hilbert Space

The e-coordinate of each Planck pixel takes values on the circle
`S¹` of circumference `L = 2πR`. The number of distinguishable
e-states per pixel is:

    d_e = L / l_P = 2πR / l_P

For the framework's Casimir-derived e-circle (`R ≈ 12 μm`,
`l_P ≈ 1.6 × 10⁻³⁵ m`): `d_e ~ 10³⁰`. In practice, `d_e ≫ 1`
and we work in the limit `d_e → ∞` (continuous e-circle), where the
results are independent of `d_e`.

The total e-Hilbert space of the horizon is:

    H_BH = (C^{d_e})^{⊗N_BH}

The total e-Hilbert space of the radiation is:

    H_rad = (C^{d_e})^{⊗N_rad}

The e-conservation constraint entangles these two spaces.

### 7.3 The Entanglement Entropy

At each emission event, the e-conservation law transfers one unit of
e-information from the horizon to the radiation. The emitted quantum's
e-coordinate `φ_k` is determined by the horizon's e-configuration:

    φ_k = g_k(φ_1^{hor}, φ_2^{hor}, ..., φ_{N_BH}^{hor})

where `g_k` is the function encoding how the `k`-th emission samples
the horizon's e-structure (determined by the Bogoliubov coefficients
of the 5D field theory).

Following Page (1993) and Hayden-Preskill (2007), we model the
horizon dynamics as a random unitary acting on the e-Hilbert space
— the assumption that the black hole is a fast scrambler
(Sekino & Susskind 2008). Under this assumption, the entanglement
entropy of the radiation after `k` emissions is:

    S_rad(k) = min[k, N_0 - k] × ln(d_e)

This is the Page result applied to the e-Hilbert space. The
derivation:

**Before the Page time** (`k < N_0/2`): The radiation subsystem
has dimension `d_e^k` and the horizon has dimension `d_e^{N_0-k}`.
For a random state in the combined Hilbert space, the reduced density
matrix of the smaller subsystem is approximately maximally mixed
(Lubkin 1978, Page 1993):

    S_rad ≈ k × ln(d_e) - d_e^{2k} / (2 × d_e^{2(N_0-k)})

For `k ≪ N_0/2`, the correction term is negligible:
`S_rad ≈ k × ln(d_e)`. The entropy rises linearly.

**At the Page time** (`k = N_0/2`): The entropy reaches its maximum:

    S_max = (N_0/2) × ln(d_e) = S_BH/2

This is half the initial Bekenstein-Hawking entropy — the Page
maximum.

**After the Page time** (`k > N_0/2`): The radiation is now the
larger subsystem. The horizon is the smaller subsystem with
`N_0 - k` pixels. By the symmetry of entanglement entropy:

    S_rad = (N_0 - k) × ln(d_e)

The entropy decreases linearly.

**At complete evaporation** (`k = N_0`): `N_BH = 0`, and:

    S_rad = 0

The radiation is in a pure state. All information has been
transferred from the horizon to the radiation via e-correlations.

### 7.4 The Page Time

The Page time — the moment when `S_rad` reaches its maximum —
occurs at `k = N_0/2`, when half the Planck pixels have been
emitted. Since the black hole emits at the Hawking rate:

    dM/dt = −σ T_H⁴ A ∝ −1/M²

the evaporation time is `t_evap ~ M_0³` in Planck units, and the
Page time is:

    t_Page ~ M_0³/2 ~ M_0² × (M_0/2)

For a solar-mass black hole: `t_Page ~ 10⁶⁶` years.

In terms of the initial entropy:
`t_Page ~ S_BH^{3/2} × t_Planck`, matching the standard result.

### 7.5 What the e-Conservation Adds Beyond Page's Argument

Page's 1993 result is a *kinematic* argument — it assumes unitarity
and derives consequences. The e-dimension framework provides the
*dynamical* mechanism that implements unitarity:

1. **The information carrier:** Each Hawking quantum carries a
   specific e-coordinate, not just a random bit. The e-coordinate
   is determined by e-conservation, not by assumption.

2. **The encoding mechanism:** The map from horizon e-coordinates to
   radiation e-coordinates is the iterative application of
   e-conservation at each emission vertex — a deterministic,
   unitary process.

3. **The scrambling mechanism:** The horizon dynamics scrambles the
   e-coordinates between emission events. This is the 4D thermal
   dynamics of the horizon surface, governed by the Hawking
   temperature. The scrambling is what makes the random-unitary
   approximation valid.

4. **The 4D invisibility:** The e-correlations are in the e-dimension
   and invisible to any 4D measurement. This is why Hawking's 4D
   calculation correctly gives a thermal result — the information is
   present but encoded in a dimension the 4D calculation doesn't see.

---

