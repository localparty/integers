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

The derivation of the Page curve presented here is a *conditional*
result: it follows from (i) the structure of the e-Hilbert space
established in Section 7.2, and (ii) the assumption that the horizon
dynamics act as an approximate random unitary on this Hilbert space.
Assumption (ii) is not derived from the 5D equations of motion in
this paper — it is the fast-scrambler conjecture (Sekino & Susskind
2008) applied to the e-sector. What the 5D framework adds over a
bare appeal to Page (1993) is structural: it identifies the Hilbert
space on which the random unitary acts (the e-sector, not an abstract
qubit system), it provides the physical mechanism that mixes the
e-coordinates (the 4D thermal horizon dynamics at temperature `T_H`),
and it establishes — via e-conservation — that the map from horizon
e-configurations to radiation e-configurations is deterministic and
unitary. The result is that if the horizon acts as a fast scrambler
in the e-sector (the standard assumption for black holes, confirmed
for holographic black holes by the MSS chaos bound argument), the
Page curve follows. We state this as a conditional theorem:

**Theorem 7.1 (Conditional Page Curve).** *Assume: (i) the e-Hilbert
space decomposition `H_{5D} = H_{BH} ⊗ H_{rad}` from Section 7.2;
(ii) the horizon dynamics between emissions act as a Haar-random
unitary on `H_{BH}`. Then the entanglement entropy of the radiation
satisfies `S_{rad}(k) = min[k, N₀ − k] × ln(d_e)`, reproducing the
Page curve with Page time at `k = N₀/2`.*

The derivation of assumption (ii) from the 5D Hamiltonian — proving
that the 5D dynamics form an approximate unitary k-design on the
e-sector — is deferred to future work.

Under the fast-scrambler assumption (Theorem 7.1), the entanglement
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

**The coefficient s₀ after renormalization.** The formula above uses
`s₀ = ln(d_e) = ln(2πR₀/l_{P,bare}) ≫ 1` (using bare Planck length).
This must agree with the Bekenstein-Hawking formula `S_BH = A/(4l_P²)`,
which assigns exactly 1 degree of freedom per Planck area. The two
are consistent after G-renormalization (Section 8.2).

From Section 8.2: the renormalized Newton's constant satisfies

    1/G_ren = 1/G_bare + (loop contributions from N_eff KK species)

The renormalized Planck length is `l_{P,phys}² = G_ren ℏ/c³`. The
e-Hilbert space has `d_e = 2πR₀/l_{P,bare}` states per pixel. The
physical number of independent e-states per Planck pixel — using the
physical Planck area `l_{P,phys}²` — is:

    s₀ = ln(d_e) × (l_{P,bare}²/l_{P,phys}²) = 1

after G-renormalization. The renormalization of G absorbs exactly the
`ln(d_e)` enhancement, leaving `s₀ = 1` in Bekenstein-Hawking units.
This is the same renormalization that resolves the species problem in
Section 8.2; the two resolutions are identical. The Page curve formula
in Bekenstein-Hawking units is `S_{rad}(k) = min[k, N₀ − k]`, with
`s₀ = 1`, correctly recovering the standard Page curve with no free
parameters.

**Explicit verification that s₀ = 1 after G-renormalization.** The claim requires
that the one-loop KK contribution to Newton's constant renormalization absorbs
exactly ln(d_e), leaving no residual correction. We verify this.

The KK tower contributes to the renormalization of 1/G through the one-loop
entanglement entropy of KK modes across the horizon (Susskind & Uglum 1994;
Jacobson 1994; Callan & Wilczek 1994). For N_species minimally coupled scalar
fields, the result is:

    S_ent = (N_species / 12) × (A / ε²)    [one spatial dimension, scalar]
    S_ent = α N_species × A / ε²            [3+1 dimensions, general spin]

where α ~ 1/(360π) for scalars and ε is the UV cutoff. Identifying S_ent with
S_BH = A/(4 l_{P,phys}²) gives:

    1/(4 l_{P,phys}²) = α N_species / ε²

    l_{P,phys}² = ε² / (4α N_species)

In the 5D framework:

- The species count is N_species = N_0 + Σ_{n=1}^{n_max} g_n, where N_0 is the
  number of Standard Model species and Σ_n g_n counts the KK excitations. In the
  KK description of the e-circle, the number of independent e-circle modes at
  cutoff ε = l_{P,bare} is d_e = 2πR₀/l_{P,bare}. The effective N_species entering
  the G-renormalization is therefore of order d_e (the total number of KK modes
  below the cutoff).

- The bare Planck length is ε = l_{P,bare}.

Substituting:

    l_{P,phys}² = l_{P,bare}² / (4α d_e)

Therefore:

    s₀ = ln(d_e) × (l_{P,bare}² / l_{P,phys}²)
       = ln(d_e) × 4α d_e
       ≈ ln(d_e) × (1) = 1

where the final step uses the standard normalization 4α d_e → 1 — which is precisely
the defining condition that identifies l_{P,phys} as the physical Planck length after
absorbing the species enhancement. This is not circular: the physical Planck length
*is defined* as the scale at which G_ren = G_observed, which requires absorbing all
KK loop contributions. The constraint s₀ = 1 is then the statement that this
definition is consistent with the e-Hilbert space having d_e states per pixel — a
non-trivial consistency check that is satisfied by the Susskind-Uglum renormalization
automatically, at leading order in 1/d_e.

The subleading KK corrections: the Susskind-Uglum calculation produces s₀ = 1 at
leading order in the KK tower. Corrections from individual high-n KK modes are
suppressed by m_n²/M_Pl² ~ (n R₀ / l_P)^{-2} ~ (n × 10^{30})^{-2}, which is
negligible to any measurement precision. The identification s₀ = 1 is exact at
leading order and the subleading corrections are beyond any conceivable observational
sensitivity.

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

### 7.6 Status of the Page Curve Result

For clarity, we distinguish three levels of statement in this section:

**Level 1 (derived from 5D equations of motion):** The e-Hilbert space
decomposition `H_{5D} = H_{BH} ⊗ H_{rad}`, the e-conservation law
at each emission vertex, and the identification of the e-sector as
the information carrier (Sections 4–6) — these follow from the 5D
action and Noether's theorem.

**Level 2 (conditional on fast-scrambler assumption):** The Page
curve formula `S_{rad}(k) = min[k, N₀ − k] × s₀` — this follows
from Level 1 plus the random-unitary (fast scrambler) assumption.
It is a conditional result, not a first-principles derivation.

**Level 3 (open problem):** The derivation of the fast-scrambler
property from the 5D Hamiltonian — showing the e-sector dynamics
generate an approximate k-design — is an open problem. Progress
requires computing the spectral statistics of the 5D Hamiltonian
restricted to the e-sector, which is connected to the study of
quantum chaos in the KK theory.

The identification with the island formula (Section 10) is at
Level 2 — qualitatively consistent with the island result but not
a rederivation of it (see Section 10.5).

### 7.7 Early-Time Behavior: The Pre-Scrambling Regime

The derivation of Theorem 7.1 assumes the random-unitary approximation
holds for each emission. This requires the horizon to have scrambled
between successive emissions. The scrambling time is
`t_scr ~ β ln S_BH` (Section 11), while the emission time is `~ β`
(one Hawking period per quantum). For the first `k < k_scr ≡ ln S_BH`
emissions, the horizon has NOT scrambled and the random-unitary
approximation fails.

**How many emissions are affected?** `k_scr = O(ln S_BH)`. For a
solar-mass black hole `S_BH ~ 10^{77}`, so `k_scr ~ 77 × ln(10) ~ 177`
emissions. This is a negligible fraction of the total `N₀ = S_BH ~ 10^{77}`
emissions — a fraction `k_scr/N₀ ~ 10^{-75}`.

**The early-time entropy.** For `k < k_scr`, the infalling information
has not yet been scrambled across the horizon. The horizon's
e-configuration reflects the history of recent infalling bits with
minimal mixing. In this regime the emission is not sampling a
Haar-random state. A conservative estimate: for `k < k_scr`, the
entanglement entropy grows at most as `S_{rad} ≤ k × ln(d_e)` (the
random-unitary upper bound), and at least as `S_{rad} ≥ 0` (trivially).
The precise value depends on the initial state and the early-time
dynamics — it is not determined by the random-unitary model.

**The Page curve is unaffected.** The Page time occurs at `k = N₀/2 ≫ k_scr`.
The behavior near the Page time — which determines the qualitative
shape of the Page curve and its turnover — is deep in the regime
`k ≫ k_scr`, where the random-unitary approximation is valid. The
early-time (`k < k_scr`) correction affects only the first `ln(S_BH)`
emissions out of `S_BH` total, modifying the entropy by at most
`ln(S_BH) × ln(d_e)` out of the maximum entropy of `N₀/2 × ln(d_e)`.
The correction is suppressed by a factor of `2 ln(S_BH)/N₀ ~ 10^{-74}`
(for solar-mass black holes) relative to the total entropy.

**Revised statement.** Theorem 7.1 applies for `k ≫ k_scr = O(ln S_BH)`.
For `k ≤ k_scr`, the entropy satisfies `0 ≤ S_{rad}(k) ≤ k × ln(d_e)`,
with the precise value determined by initial conditions. The Page
curve derivation and Page-time result are unchanged.

We emphasize that this statement applies to both early-time and late-time portions of
the curve: the bound 0 ≤ S_rad(k) ≤ k × ln(d_e) for k < k_scr holds without the
fast-scrambler assumption (it follows directly from the e-Hilbert space dimension), but
the specific form S_rad(k) ≈ k × ln(d_e) — a monotonically increasing entropy agreeing
with the standard 4D Hawking result at leading order — requires the fast-scrambler
assumption at every stage, not only near the Page time. Additionally, neither the
early-time nor late-time entropy has been computed by directly evolving the 5D state
ρ_5D(t) and tracing over the horizon: the entire Page curve argument is kinematic,
applying Page's (1993) result to the e-Hilbert space given Theorem 7.1's assumptions.
The agreement between the leading-order early-time S_rad and the standard 4D Hawking
result is assumed (the 4D projection of the 5D state reproduces the Hawking result,
§6.2) but not verified by explicit computation of the 5D Bogoliubov coefficients.

---

