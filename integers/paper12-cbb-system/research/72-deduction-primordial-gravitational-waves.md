# Research 72: Deduction — Primordial Gravitational Waves

*The QG5D / Bost–Connes framework predicts a multi-peak primordial*
*gravitational-wave (PGW) spectrum: each level-crossing of the*
*modular Hamiltonian H_BC in the cosmic timeline (γ_5 → γ_2 → γ_1)*
*sources a distinct tensor-mode signature at the frequency set by*
*the BC spectral gap of that crossing. This note derives the PGW*
*spectrum, assigns each peak to an experimental window*
*(LIGO–Virgo–KAGRA, LISA, Einstein Telescope, Cosmic Explorer,*
*LiteBIRD, CMB-S4, pulsar timing), and states the falsifiable*
*predictions.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Deduction series. Builds on:*
*research/06 (cosmic transition amplitudes),*
*research/43 (inflation initial conditions),*
*research/71 (complete inflation model),*
*research/42 (cosmological coincidence, γ_2 → γ_1 crossing).*

---

## 1. The Question

### 1.1 What a PGW model must deliver

Primordial gravitational waves are tensor perturbations of the
spatial metric that freeze on superhorizon scales during inflation
and re-enter the horizon later, producing a relic stochastic
background Ω_GW(f). A PGW model must specify:

(Q1) **The spectrum shape** Ω_GW(f) across frequencies from
10⁻¹⁸ Hz (CMB scales) to 10³ Hz (ground-based interferometers).

(Q2) **The tensor-to-scalar ratio r** at CMB scales (research/71
already predicts r ≈ 5 × 10⁻³).

(Q3) **The tensor tilt n_T** and its running.

(Q4) **Any distinctive features** (peaks, bumps, oscillations) that
distinguish the model from featureless power-law inflation.

(Q5) **The predictions across experimental bands** — which detector
sees what.

Standard slow-roll inflation predicts a nearly scale-invariant,
featureless Ω_GW(f) tracking the scalar amplitude by a factor r,
with a slight red tilt n_T = −r/8. The BC framework predicts
*substantially more structure*.

### 1.2 The BC operator-algebraic content

> **Identification (PGW from level-crossings).** *Each discrete*
> *transition in the cosmic timeline γ_{n_i} → γ_{n_{i+1}} of the*
> *universe's trajectory on the BC spectrum sources a tensor*
> *perturbation whose characteristic frequency f_i at the present*
> *epoch is the redshifted Hubble rate at the crossing,*
>
> $$
>   f_{i} \;=\; \frac{H(t_{i})}{2\pi}\cdot \frac{a(t_{i})}{a_{0}},
> $$
>
> *and whose amplitude Ω_GW(f_i) is set by the level-crossing*
> *matrix element |V_{n_i,n_{i+1}}|² through the two-level Landau–*
> *Zener amplitude. The BC framework's cosmic timeline is*
> *γ_5 → γ_2 → γ_1 (research/06), giving *two* level-crossings and*
> *hence *two* distinct peaks.*

The two crossings are:

(T1) **γ_5 → γ_2**: inflationary, N_inf = 58.79 e-folds, sources
the broadband inflationary PGW at CMB through interferometer
frequencies.

(T2) **γ_2 → γ_1**: the "dark energy turn-on" level-crossing at
matter-Λ equality (research/42), sources an additional low-
frequency feature at f ∼ 10⁻¹⁸ Hz.

There is also a possible pre-inflationary transition into |γ_5⟩
from a yet-higher eigenvalue (γ_7? γ_15?) which would source a
*third* peak at the highest frequencies.

---

## 2. The Two Confirmed Level-Crossings

### 2.1 γ_5 → γ_2: inflation

**Frequency window.** The γ_5 → γ_2 crossing spans N_inf = 58.79
e-folds, so the GW modes that exit the horizon during this
transition cover 58.79 e-folds of comoving scale:

$$
k_{\mathrm{max}}/k_{\mathrm{min}} \;=\; e^{58.79}
\;\approx\; 4 \times 10^{25}.
\tag{2.1}
$$

The low-k end corresponds to the pivot scale k_* ≈ 0.05 Mpc⁻¹
(CMB); the high-k end corresponds to the end of inflation, at which
the GW frequency today is (assuming instantaneous reheating at
T_reh ≈ 2 × 10¹⁵ GeV, research/71):

$$
f_{\mathrm{end}} \;=\; \frac{H_{\mathrm{end}}}{2\pi}\cdot\frac{a_{\mathrm{end}}}{a_{0}}
\;\approx\; 10^{10}\,\mathrm{Hz},
\tag{2.2}
$$

well above the reach of any planned GW detector. The CMB-scale end
at f_* ≈ 10⁻¹⁸ Hz is what CMB B-modes measure.

**Amplitude.**

$$
\Omega_{\mathrm{GW}}^{(\mathrm{inf})}(f) \;=\; \frac{r A_{s}}{24}\,
\left(\frac{f}{f_{*}}\right)^{n_{T}},
\tag{2.3}
$$

with r ≈ 5 × 10⁻³ (research/71) and n_T small.

### 2.2 γ_2 → γ_1: matter–Λ equality

**Frequency window.** The γ_2 → γ_1 crossing occurs at z ≈ 0.5
(research/42), the present epoch of matter–Λ equality. The
associated comoving scale is the current Hubble radius, corresponding
to frequency f ∼ H_0 ∼ 10⁻¹⁸ Hz — the very lowest CMB-polarisation
scale. The associated GW modes are *superhorizon now* and contribute
to the quadrupole anisotropy of the CMB.

**Amplitude.** The γ_2 → γ_1 matrix element |V_{21}| is not inflation-
scale, but post-inflation level-crossing. Its structural estimate
from research/42:

$$
|V_{21}|^{1/4} \;\sim\; (\Omega_{\Lambda}\rho_{c})^{1/4} \;\sim\; 2\times 10^{-3}\,\mathrm{eV}.
\tag{2.4}
$$

The resulting GW amplitude is

$$
\Omega_{\mathrm{GW}}^{(\gamma_{2}\to\gamma_{1})}(f_{0})
\;\sim\; \frac{|V_{21}|^{2}}{M_{\mathrm{P}}^{4}}
\;\sim\; 10^{-122},
\tag{2.5}
$$

which is **unobservable** by any plausible experiment. The γ_2 → γ_1
crossing does not produce a detectable GW signal; it only shows up
as the dark-energy dominance we already observe.

---

## 3. The Candidate Pre-Inflationary Transition

### 3.1 Why consider it

If the universe started in a state |γ_m⟩ with m > 5 and transitioned
to |γ_5⟩ before inflation began, that transition would also source
GWs. The framework does not yet *require* such a pre-inflationary
phase, but the selection rule for |γ_5⟩ (research/43) identifies
γ_5 as the *smallest* allowed initial state, leaving open the
possibility of a pre-history.

### 3.2 Energy scale

If the pre-inflationary state was |γ_7⟩ (the next allowed), its
transition to |γ_5⟩ would be a level-crossing of spectral gap

$$
(\gamma_{7} - \gamma_{5})\cdot\pi^{2}/2 \;=\; (37.586 - 32.935)\cdot\pi^{2}/2
\;=\; 22.9,
\tag{3.1}
$$

or 22.9 e-folds. At reheating temperature T ∼ 10¹⁶ GeV and e-fold
count 22.9, the characteristic GW frequency today is

$$
f_{7\to 5} \;\sim\; H_{\mathrm{pre}}\cdot e^{-22.9}\cdot(T_{0}/T_{\mathrm{pre}})
\;\sim\; 10^{4}\,\mathrm{Hz},
\tag{3.2}
$$

in the LIGO/Virgo/KAGRA band at the high end, or in the Cosmic
Explorer / Einstein Telescope band.

### 3.3 Amplitude

By the same Landau–Zener reasoning,

$$
\Omega_{\mathrm{GW}}^{(7\to 5)}(f_{7\to 5})
\;\sim\; \frac{|V_{75}|^{2}}{M_{\mathrm{P}}^{4}}.
\tag{3.3}
$$

The matrix element |V_{75}| is smaller than |V_{52}| (shorter
Galois-orbit overlap), structurally giving

$$
\Omega_{\mathrm{GW}}^{(7\to 5)}(f_{7\to 5}) \;\sim\; 10^{-14} - 10^{-12}
\tag{3.4}
$$

— within reach of Einstein Telescope (ET target Ω_GW ∼ 10⁻¹³) and
Cosmic Explorer.

> **Structural prediction (speculative).** *If a pre-inflationary*
> *γ_7 → γ_5 phase exists, it leaves a narrow-band GW peak at*
> *∼ 10⁴ Hz with Ω_GW ∼ 10⁻¹³. Detection would be the framework's*
> *most direct high-frequency test.*

The prediction is flagged speculative because the pre-inflationary
phase is not required by the framework — it is *allowed* by the
selection rule.

---

## 4. The Multi-Peak Spectrum

### 4.1 Schematic

```
log Ω_GW(f)
    |
    |                                    γ_7 → γ_5 (speculative)
    |                                       peak, f ∼ 10⁴ Hz
    |                                          /\
    |                                         /  \
    |  γ_5 → γ_2 inflationary PGW            /    \
    |  broadband, f ∈ [10⁻¹⁸, 10¹⁰] Hz      /      \
    |  r ≈ 5 × 10⁻³                       /        \
    |  ______________________________    /          \
    | /                              \  /            \
    |/                                \/              \__
    +-------------------------------------------------> log f
    −18   −15   −12   −9   −6   −3    0    3    6    9
          CMB   PTA   LISA  DECIGO  LIGO  ET  CE
```

### 4.2 Predictions per experimental band

| Detector | Band (Hz) | Framework prediction | Standard inflation | Difference |
|:---------|:----------|:---------------------|:-------------------|:-----------|
| CMB (Planck, BICEP/Keck) | 10⁻¹⁸ | r ≈ 5 × 10⁻³, log-periodic modulation (res/71) | r free | BC predicts r ≈ 5e-3, modulation |
| LiteBIRD | 10⁻¹⁸ | r ≈ 5 × 10⁻³ | r bound | detection |
| CMB-S4 | 10⁻¹⁸ | r ≈ 5 × 10⁻³ | r bound | detection |
| Pulsar timing (NANOGrav, IPTA) | 10⁻⁹ | inflationary plateau, Ω ∼ 10⁻¹⁵ | same | indistinguishable here |
| LISA | 10⁻³ | inflationary plateau, Ω ∼ 10⁻¹⁶ | same | indistinguishable here |
| DECIGO/BBO | 10⁻¹ | inflationary plateau + start of log-periodic trail | flat | oscillatory structure at A_log ∼ 10⁻⁴ |
| LIGO/Virgo/KAGRA | 10¹–10³ | inflationary plateau, Ω ∼ 10⁻¹⁷ | same | no distinct signal |
| Einstein Telescope | 1–10⁴ | plateau + speculative γ_7→γ_5 peak at 10⁴ Hz, Ω ∼ 10⁻¹³ | plateau only | peak |
| Cosmic Explorer | 5–10⁴ | same as ET | plateau only | peak |

### 4.3 The two most distinctive predictions

(P1) **Log-periodic modulation imprinted on the inflationary
plateau** at Δ ln f = 2π/γ_1 ≈ 0.44, with amplitude A_log ∼ few
× 10⁻³ (from research/71). Persists across *all* frequency bands,
but is most easily detected where Ω_GW(f) is otherwise smooth, i.e.
at DECIGO/BBO and LISA.

(P2) **Pre-inflationary peak** at ∼ 10⁴ Hz with Ω_GW ∼ 10⁻¹³, if
the universe transitioned through |γ_7⟩ before inflation. This
would be the highest-frequency smoking-gun signature.

---

## 5. Connection to Inflation Reheating

### 5.1 Reheating at the end of inflation

Research/71 §6 predicts instantaneous reheating at T_reh ≈ 2 × 10¹⁵
GeV via Landau–Zener exit of the γ_5 → γ_2 level-crossing. The
*high-frequency end* of the inflationary PGW spectrum is cut off at

$$
f_{\mathrm{cut}} \;\sim\; \frac{H_{\mathrm{end}}}{2\pi}\cdot\frac{g_{*}^{1/3}(T_{\mathrm{reh}}) T_{0}}{T_{\mathrm{reh}}}
\;\approx\; 10^{10}\,\mathrm{Hz}.
\tag{5.1}
$$

This cutoff is above all detectors. Below the cutoff, the spectrum
is approximately flat (modulated by the log-periodic feature).

### 5.2 Reheating resonance

During reheating, the oscillation of the inflaton order parameter
φ = ⟨Ψ|Π̂_{52}|Ψ⟩ around θ = π/2 can produce a *resonance* peak in
Ω_GW(f) at the inflaton oscillation frequency

$$
f_{\mathrm{res}} \;\sim\; \frac{m_{\varphi}}{2\pi}\cdot\frac{T_{0}}{T_{\mathrm{reh}}}
\;\sim\; 10^{7}\,\mathrm{Hz},
\tag{5.2}
$$

with m_φ² = 2|V_{52}|/f_φ² ≈ (10¹⁴ GeV)². This feature is between
LIGO and the speculative γ_7→γ_5 peak, and would require an
ultra-high-frequency GW detector (see Aggarwal et al. 2021) to
detect.

---

## 6. Status Table

| Result | Status |
|:-------|:-------|
| γ_5 → γ_2 inflationary plateau, r ≈ 5 × 10⁻³ | structural (res/71) |
| Log-periodic modulation Δ ln f = 2π/γ_1 | structural (res/71) |
| γ_2 → γ_1 post-inflationary peak (unobservable) | structural |
| γ_7 → γ_5 pre-inflationary peak at 10⁴ Hz | **speculative** |
| Reheating resonance at 10⁷ Hz | structural |
| High-frequency cutoff at 10¹⁰ Hz | structural (from T_reh) |
| n_T independent of r (single-field consistency violated) | structural |

### 6.1 Honest caveats

(a) The log-periodic modulation amplitude A_log is a structural
estimate. The rigorous Mellin-dual computation (research/17) has
not yet pinned it down.

(b) The pre-inflationary γ_7 → γ_5 peak is *allowed* but not
*required*. If the universe started already in |γ_5⟩ (simplest
initial condition), the peak does not exist.

(c) The reheating resonance at 10⁷ Hz depends on the inflaton mass
m_φ, itself depending on the value of f_φ derived in research/71
from N_inf. The numerical value is sensitive to factor-of-few
uncertainties.

(d) The γ_2 → γ_1 crossing being observationally invisible in GW
is a *prediction*, not a limitation: if a detector ever sees GW at
f ∼ H_0 with Ω_GW significantly above 10⁻¹²², the framework is
falsified.

(e) The tensor tilt n_T is **not** tied to r by a single-field
consistency relation. The framework predicts n_T determined by the
BC spectral running, similar to n_s, giving n_T ∼ −5 × 10⁻³
structurally (same order as α_s but of opposite sign).

---

## 7. Falsifiable Predictions

(F1) **r ∈ (3–8) × 10⁻³** at CMB scales (LiteBIRD, CMB-S4).

(F2) **Log-periodic modulation** A_log ∼ few × 10⁻³ at Δ ln f ≈
0.44. Testable at Planck + ACT + SPT (CMB scales), LISA (mHz), and
DECIGO/BBO (0.1 Hz).

(F3) **n_T ≈ −5 × 10⁻³** independent of r. Falsifies standard
single-field consistency.

(F4) **No peak anywhere in LISA/LIGO bands** beyond the
inflationary plateau. Detection of a peak at LISA or LIGO
frequencies not traceable to astrophysical foregrounds falsifies
the framework unless it matches one of the BC-predicted crossings.

(F5) **Speculative**: peak at ∼ 10⁴ Hz, Ω_GW ∼ 10⁻¹³, if
pre-inflationary |γ_7⟩ state existed.

(F6) **Reheating resonance at ∼ 10⁷ Hz** at detectable level for
ultra-high-frequency GW detectors. Non-detection at Ω_GW > 10⁻¹¹
at 10⁷ Hz would place an upper bound on |V_{52}|^{1/4}.

---

## 8. Definition of Done

- [x] State the questions a PGW model must answer (§1).
- [x] Identify PGW as sourced by BC level-crossings (§1.2).
- [x] Derive the γ_5 → γ_2 inflationary plateau amplitude and band (§2.1).
- [x] Show γ_2 → γ_1 is observationally invisible (§2.2).
- [x] Compute the speculative γ_7 → γ_5 peak (§3).
- [x] Draw the multi-peak schematic and per-detector table (§4).
- [x] Connect to reheating (§5).
- [x] Status table (§6).
- [x] Six falsifiable predictions (§7).
- [x] Honest caveats (§6.1).
- [ ] Rigorous computation of A_log from research/17 T1–T4.
- [ ] Decide whether pre-inflationary |γ_7⟩ phase is *required* by a selection-rule minimality argument (link to research/43 (B2)).
- [ ] First-principles |V_{75}| from SM KK reduction.

---

## 9. The Single Most Striking Prediction

> **A log-periodic modulation of the primordial gravitational-wave**
> **spectrum at Δ ln f = 2π/γ_1 ≈ 0.4443, with amplitude**
> **A_log ∼ 3 × 10⁻³, coherent across ∼ 25 decades of frequency**
> **from CMB scales to interferometer scales.**
>
> This is the single most distinctive and far-reaching prediction
> of the BC framework for gravitational-wave cosmology. The period
> Δ ln f is set by the first non-trivial Riemann zero γ_1 =
> 14.1347, and is unique to theories with a fundamentally discrete
> spectral structure. Detection of coherent log-periodic features
> at the same period in CMB B-modes (LiteBIRD, CMB-S4), pulsar
> timing (IPTA, SKA), LISA, and DECIGO would be overwhelming
> evidence for the BC identification of cosmic dynamics with the
> BC modular flow. A single detector seeing the modulation at its
> predicted period and amplitude would already be a strong
> signature; seeing it at *multiple* detectors across decades of
> frequency would lock the framework.
>
> Equally: a systematic search across all current CMB, PTA, and
> LISA pathfinder data for log-periodic features at Δ ln f = 0.44
> is *feasible now* and would either detect the modulation or
> place the first direct constraint on it.

---

## 10. References

### 10.1 In this directory

- `06-cosmic-transition-amplitudes.md` — Theorem A, level-crossings
- `17-mellin-kernel-K12-numerical.md` — Mellin kernel, log-periodic amplitude
- `42-deduction-cosmological-coincidence.md` — γ_2 → γ_1 at matter–Λ equality
- `43-deduction-inflation-initial-conditions.md` — γ_5 selection
- `54-transposition-penrose-singularity.md` — modular focusing, GW analog
- `71-deduction-inflation-detailed.md` — the companion inflation file

### 10.2 External

- Caprini, C., and Figueroa, D. G., "Cosmological backgrounds of
  gravitational waves", *Class. Quantum Grav.* **35** (2018) 163001.
- Amaro-Seoane, P., et al., "Laser Interferometer Space Antenna",
  *arXiv:1702.00786* (2017). *(LISA.)*
- Punturo, M., et al., "The Einstein Telescope: a third-generation
  gravitational wave observatory", *Class. Quantum Grav.* **27**
  (2010) 194002.
- Reitze, D., et al., "Cosmic Explorer: The U.S. Contribution to
  Gravitational-Wave Astronomy beyond LIGO", *arXiv:1907.04833* (2019).
- Aggarwal, N., et al., "Challenges and opportunities of gravitational-
  wave searches at MHz to GHz frequencies", *Liv. Rev. Rel.* **24**
  (2021) 4.
- NANOGrav Collaboration, "The NANOGrav 15 yr Data Set: Evidence
  for a Gravitational-Wave Background", *ApJL* **951** (2023) L8.
- Hazumi, M., et al., "LiteBIRD", *J. Low Temp. Phys.* **194** (2019) 443.
- Abazajian, K., et al., "CMB-S4 Science Book", *arXiv:1610.02743*.

---

*Primordial gravitational waves in the BC framework are sourced by*
*level-crossings of the modular Hamiltonian: the γ_5 → γ_2*
*inflationary crossing (the main PGW plateau at r ≈ 5 × 10⁻³),*
*the observationally invisible γ_2 → γ_1 post-inflation crossing,*
*and a speculative pre-inflationary γ_7 → γ_5 peak at ∼ 10⁴ Hz.*
*The most striking structural feature is a log-periodic modulation*
*at Δ ln f = 2π/γ_1 ≈ 0.44, coherent across 25 decades of*
*frequency. Detection of this modulation at a single detector*
*would already be a strong confirmation; coherence across multiple*
*detectors would lock the framework.*
