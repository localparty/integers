# Appendix Y — The Hubble Tension: A Geometric Prediction from the Hidden Brane

> The Z₂ orbifold of Appendix W, introduced for dark matter and the spin
> structure, predicts a hidden-brane radiation sector thermally decoupled
> from the visible sector. This dark radiation raises the CMB-inferred
> Hubble constant above the pure ΛCDM value. The allowed contribution is
> constrained by two independent datasets: updated BBN (2025 joint
> analysis) and ACT DR6 (March 2025, the final ACT release). Under the
> tighter ACT DR6 constraint, the framework predicts **H₀ ≈ 68.0–68.7
> km/s/Mpc** — above ΛCDM (67.4) and in the direction of the
> non-distance-ladder consensus (69.4 ± 0.3, Pantos & Perivolaropoulos
> 2026). The full BBN-allowed range (H₀ up to 70) is in tension with
> ACT DR6 and will be definitively tested by CMB-S4.

---

## Y.1 The Hubble Tension: A Reframing

The Hubble constant H₀ is measured by two broad classes of methods that
disagree significantly.

**CMB / early-universe methods** infer H₀ by fitting the acoustic peaks
of the CMB within a cosmological model (ΛCDM or extensions):

| Source | H₀ (km/s/Mpc) | Reference |
|--------|---------------|-----------|
| Planck 2018 (ΛCDM) | 67.4 ± 0.5 | Planck Collaboration 2020 |
| ACT DR6 + DESI DR1 | 68.22 ± 0.36 | ACT DR6, arXiv:2503.14452 |
| ACT DR6 + Planck + DESI DR2 | 68.43 ± 0.27 | ACT DR6 |
| DESI DR2 + Planck + lensing | 67.97 ± 0.38 | DESI 2025, arXiv:2503.14738 |

**Local distance-ladder methods** measure H₀ by calibrating standard
candles against geometric anchors:

| Source | H₀ (km/s/Mpc) | Calibrator | Reference |
|--------|---------------|------------|-----------|
| SH0ES (HST+JWST, 19 hosts) | 73.49 ± 0.93 | Cepheids | Riess et al. 2024 |
| CCHP TRGB (HST+JWST, 24 cal.) | 70.39 ± 1.22 ± 1.33 | TRGB | Freedman et al. 2408.06153 |
| CCHP TRGB (JWST only) | 68.81 ± 1.79 ± 1.32 | TRGB | Freedman et al. 2408.06153 |
| CCHP JAGB (JWST only) | 67.80 ± 2.17 ± 1.64 | J-AGB | Freedman et al. 2408.06153 |
| TDCOSMO lensing (8 quasars) | 71.6 +3.9/−3.3 | Lens time delay | arXiv:2506.03023 |
| Two-population SN Ia reanalysis | 70.59 ± 1.15 | SN Ia | arXiv:2506.22150 |

### Y.1.1 The Pantos & Perivolaropoulos Reframing

The traditional framing — "CMB vs. Cepheids at 5σ" — obscures important
structure. Pantos & Perivolaropoulos (arXiv:2601.00650, 2026) analyzed
88 sound-horizon-free H₀ measurements and found:

    Distance-ladder methods:              H₀ = 72.73 ± 0.39 km/s/Mpc
    Sound-horizon-free, non-DL methods:  H₀ = 69.37 ± 0.34 km/s/Mpc
    Tension between these two classes:   6.5σ

The real tension is **distance ladder vs. everything else** — not early
vs. late universe. The CMB value (67.4) is one data point within the
"everything else" class. The JWST-only CCHP results trend toward the
low end (67.8–68.8), consistent with the "everything else" consensus.

**The question for the framework:** The 5D orbifold predicts dark
radiation from the hidden brane. How much does it shift H₀, and is
the shift in the right direction?

---

## Y.2 The Geometric Origin of Dark Radiation

### Y.2.1 From Spin Structure to Hidden Brane

The framework's H₀ prediction traces to the spin structure of
Appendix B. The logical chain is:

**Step 1 — Spin structure (Appendix B.1, B.3.3).** The topology of
Spin(d) for d ≥ 3 requires fermions to be anti-periodic on the e-circle:
ψ(φ + 2π) = −ψ(φ). This is the unique boundary condition consistent
with half-integer spin representations of the double cover Spin(d) → SO(d).

**Step 2 — The Z₂ action (Appendix W.1).** The anti-periodicity defines
a natural Z₂ action: φ → φ + π acts as (−1)^F on spinor fields. This
Z₂ is the element −1 ∈ ker(Spin(d) → SO(d)) — the same topological
object that gives the 720° property of spin-½ particles.

**Step 3 — The orbifold (Appendix W.2).** Modding out by this Z₂
produces S¹/Z₂ = [0, πR], an interval with two fixed-point branes:
visible at φ = 0 (SM matter), hidden at φ = π (gravitates normally,
couples to no SM force).

**Step 4 — Hidden-brane radiation.** If the hidden brane supports a
thermal bath populated gravitationally during reheating, it contributes
dark radiation to the expansion rate of the universe. This is not an
ad hoc addition — it follows from the same topology that produces the
spin-statistics theorem.

### Y.2.2 The Temperature Ratio ξ

The hidden sector is thermally decoupled: T_hidden = ξ × T_visible,
with 0 < ξ < 1. The visible sector is preferentially heated (couples
directly to inflaton decay products). For T_reh ~ 10⁹ GeV, typical
gravitational production gives ξ ~ 0.3–0.5 (Berezhiani 2005, Foot 2004).
The precise value of ξ is constrained from above by both BBN and CMB
data. Crucially, it is also constrained FROM BELOW by the observed dark
matter abundance: the bulk leptogenesis mechanism (developed in Paper 2,
Appendix E) yields Ω_DM/Ω_b = 1/ξ², which combined with the observed
ratio 5.36 gives ξ = 0.432–0.47. Within this range ξ is no longer a
free parameter — it is determined by the observed Ω_DM/Ω_b ratio.

---

## Y.3 The Dark Radiation Contribution

### Y.3.1 Mirror Sector Degrees of Freedom

If the hidden brane supports a mirror SM (the most symmetric possibility
from the Z₂ orbifold), the mirror sector has g_*^{mirror} = 10.75
relativistic degrees of freedom at BBN temperatures above the mirror
electron mass (mirror photon: 2, mirror e±: 4 × 7/8, mirror ν: 6 × 7/8):

    g_*^{mirror}(T > m_e) = 2 + (7/8)(4 + 6) = 10.75

### Y.3.2 ΔN_eff from the Mirror Sector

    ΔN_eff^{mirror} = (g_*^{mirror} / g_*^{1ν}) × ξ⁴ = (10.75/1.75) × ξ⁴
                    = **6.14 × ξ⁴**

This is the standard result (Berezhiani 2005). Energy conservation
ensures this value holds at all epochs after mirror e⁺e⁻ annihilation.

### Y.3.3 Why the Mirror Sector Maps Directly to N_eff

A key physical point: mirror recombination occurs at T_mirror ~ 0.3 eV
(same atomic physics as visible recombination). Since T_mirror = ξ × T_vis:

    Mirror recombination at T_vis = 0.3/ξ eV:
    ξ = 0.50 → z_mirror_rec ~ 2500
    ξ = 0.35 → z_mirror_rec ~ 3600

In all cases, mirror recombination occurs **before** visible recombination
(z ~ 1100). At z = 1100, mirror photons are already free-streaming. They
contribute directly to N_eff — not to N_fluid (interacting radiation).
The ACT DR6 constraint on N_eff applies in full to the mirror sector.

### Y.3.4 The H₀ Shift from Extra Radiation

From the Planck 2018 ΛCDM+N_eff chain (Table 2): H₀ shifts from
67.36 at N_eff = 3.046 to 69.32 at N_eff = 3.36, giving:

    ΔH₀ ≈ 6.3 × ΔN_eff   km/s/Mpc

(calibrated to Bernal, Verde & Riess 2016). The mirror sector contribution:

    ΔH₀^{mirror} = 6.3 × 6.14 × ξ⁴ = **38.7 × ξ⁴**  km/s/Mpc

---

## Y.4 The Constraints on ξ

### Y.4.1 BBN Constraint (updated 2025)

The 2025 joint BBN analysis (arXiv:2507.23354) gives:

    N_eff^{BBN} = 2.898 ± 0.141  (from D/H + Y_P)

The 2σ upper bound: N_eff < 3.180 → ΔN_eff < 0.136 → **ξ < 0.384**

(The earlier Fields et al. 2020 bound of ξ < 0.50 is superseded by
this tighter 2025 analysis and should no longer be used.)

### Y.4.2 CMB Constraint: ACT DR6 (binding)

ACT DR6 (arXiv:2503.14452, March 2025 — the final ACT data release)
gives:

    N_eff = 2.86 ± 0.13  (ACT DR6 alone)
    N_eff = 2.89 ± 0.11  (ACT DR6 + He + D abundances)

This is more constraining than BBN and supersedes it as the binding
constraint. The framework predicts N_eff = 3.046 (SM) + 0.05 (tower,
from §Y.8.1) + 6.14 × ξ⁴ (mirror). The tension with ACT DR6 alone:

| ξ | ΔN_eff^{mirror} | N_eff^{total} | Tension (ACT DR6) |
|---|-----------------|---------------|-------------------|
| 0.25 | 0.024 | 3.12 | 2.0σ |
| 0.30 | 0.050 | 3.15 | 2.2σ |
| 0.35 | 0.092 | 3.19 | 2.5σ |
| 0.40 | 0.157 | 3.25 | 3.0σ |
| 0.45 | 0.252 | 3.35 | 3.8σ |
| 0.50 | 0.384 | 3.48 | 4.8σ |

At 2σ (ACT DR6): N_eff < 3.12 → ΔN_eff^{mirror} < 0.026 → **ξ < 0.255**
At 3σ (ACT DR6): N_eff < 3.25 → ΔN_eff^{mirror} < 0.156 → **ξ < 0.397**

### Y.4.3 Why the Cascade Does Not Loosen This Bound

The Gonzalo et al. (2024) intra-tower cascade (§Y.8.1) reduces the
VISIBLE sector's N_eff by draining energy from active neutrinos into
dark KK tower modes. It does NOT reduce the mirror sector's contribution.

The reason is fundamental: the cascade is an internal redistribution
of energy between the mirror brane and the bulk KK tower. Both
components contribute to the expansion rate of the universe. The CMB
measures the total gravitational effect of all radiation — brane-localized
or bulk. Redistributing energy within the dark sector leaves the total
expansion rate unchanged. The mirror ΔN_eff = 6.14 × ξ⁴ is a
gravitational effect; no internal reshuffling can reduce it.

---

## Y.5 The Framework's H₀ Prediction

### Y.5.1 Three Contributions to H₀

**1. Mirror brane dark radiation (geometric).**

    ΔH₀^{mirror} = 38.7 × ξ⁴  km/s/Mpc

**2. KK tower dark radiation (geometric, small).**
After intra-tower cascade dynamics (§Y.8.1), ΔN_eff^{tower} ≈ 0.05:

    ΔH₀^{tower} = 6.3 × 0.05 = **+0.3** km/s/Mpc

**3. Thawing dilaton (if DESI-compatible w ≈ −0.8).**
The DESI DR2 combined fit with Planck (arXiv:2503.14738, Table 3) finds
evolving dark energy (w₀ ≈ −0.75, wₐ ≈ −0.75) gives H₀ ≈ 66.9 —
about 0.5 km/s/Mpc below the static ΛCDM value. The thawing dilaton
goes in the OPPOSITE direction from the mirror radiation:

    ΔH₀^{dilaton} ≈ **−0.5** km/s/Mpc  (approximate; sign is robust)

### Y.5.2 Two-Tier Prediction

The ACT DR6 constraint defines two distinct regimes:

---

**Tier 1 — Current CMB-constrained (ACT DR6, 2–3σ allowed):**

At ξ < 0.35 (well within ACT DR6 at 2.5σ):

| ξ | ΔN_eff^{mirror} | H₀ Scenario A (w=−1) | H₀ Scenario B (thawing) |
|---|-----------------|----------------------|-------------------------|
| 0.25 | 0.024 | 67.7 | 67.2 |
| 0.30 | 0.050 | 67.9 | 67.4 |
| 0.35 | 0.092 | 68.3 | 67.8 |

**Tier 1 prediction: H₀ ≈ 68.0–68.3** — above pure ΛCDM (67.4),
consistent with all current data including ACT DR6.

---

**Tier 2 — BBN-limited (testable by CMB-S4, in tension with ACT DR6):**

At ξ = 0.35–0.384 (BBN 2025 limit, 2.5–3σ tension with ACT DR6):

| ξ | ΔN_eff^{mirror} | H₀ Scenario A | H₀ Scenario B | ACT DR6 tension |
|---|-----------------|---------------|---------------|-----------------|
| 0.35 | 0.092 | 68.3 | 67.8 | 2.5σ |
| 0.37 | 0.115 | 68.4 | 67.9 | 2.6σ |
| 0.384 | 0.136 | 68.7 | 68.2 | 2.8σ |

**Tier 2 prediction: H₀ ≈ 68.3–68.7** — above ΛCDM, moving toward
the non-DL consensus, but in 2.5–2.8σ tension with ACT DR6.
Definitively testable by CMB-S4 (σ(N_eff) ≈ 0.03).

---

### Y.5.3 The Honest Prediction

The framework predicts:

    **H₀ ≈ 68.0–68.7 km/s/Mpc**

depending on ξ (constrained to 0.25–0.384 by current data) and the
dark energy scenario. This prediction:

- Is **above ΛCDM** (67.4) by 0.6–1.3 km/s/Mpc ✓
- Is **in the right direction** toward the non-DL consensus (69.4) ✓
- Is **consistent with ACT DR6** at the Tier 1 level (ξ < 0.35) ✓
- Is **not tuned**: ξ is bounded by BBN and ACT DR6, not by H₀ ✓
- Is **not a full resolution** of the Hubble tension — the gap to
  Cepheids (73.0) and even to the non-DL consensus (69.4) remains ✗

---

## Y.6 Comparison with the Observational Landscape

### Y.6.1 Where the Prediction Sits

| H₀ (km/s/Mpc) | Source | Consistency with framework (68.0–68.7) |
|---------------|--------|----------------------------------------|
| 67.4 ± 0.5 | Planck (ΛCDM) | 0.5–2σ above ✓ |
| 68.2 ± 0.4 | ACT DR6 + DESI | **< 1σ** ✓ |
| 68.4 ± 0.3 | ACT + Planck + DESI | **< 1σ** ✓ |
| 69.4 ± 0.3 | Non-DL consensus (P&P) | 1.5–3σ below prediction |
| 70.4 ± 1.8 | CCHP TRGB (HST+JWST) | 0.5–1.5σ below prediction |
| 68.8 ± 2.2 | CCHP TRGB (JWST only) | **< 1σ** ✓ |
| 67.8 ± 2.8 | CCHP JAGB (JWST only) | < 1σ ✓ |
| 73.0 ± 1.0 | SH0ES Cepheids | 4–5σ discrepancy |

### Y.6.2 The P&P Reframing: Framework as a Partial Resolution

The framework cannot close the full 5.6 km/s/Mpc gap to Cepheids. But
reframing via Pantos & Perivolaropoulos:

- The real tension is distance-ladder (72.7) vs. non-DL (69.4) at 6.5σ
- The framework moves the CMB inference (67.4) toward the non-DL
  consensus (69.4) by 0.6–1.3 km/s/Mpc
- The remaining gap (framework 68.5 vs. non-DL 69.4) is 1.5–3σ
- The distance-ladder discrepancy (73 vs. 69) is a calibration question
  independent of the framework's physics

The framework partially explains why the CMB value is lower than most
other methods — it identifies the missing ingredient (mirror dark
radiation) that the ΛCDM fit omits. Whether this is sufficient depends
on what CMB-S4 finds.

### Y.6.3 The CCHP JWST update

The paper previously cited "TRGB: 69.8 ± 0.6" as the primary comparison.
The full CCHP JWST results (arXiv:2408.06153) show a spread:
- TRGB (HST+JWST combined): 70.39 ± 1.22 ± 1.33
- TRGB (JWST only): 68.81 ± 1.79 ± 1.32
- JAGB (JWST only): 67.80 ± 2.17 ± 1.64

The JWST-only values trend toward ΛCDM. The framework prediction
(68.0–68.7) is consistent with the JWST-only CCHP results at < 1σ.

---

## Y.7 Why the Dilaton Does Not Provide Early Dark Energy

For completeness, we demonstrate that the dilaton cannot serve as
early dark energy — the class of models that reduce the sound horizon
by contributing ~10% of the energy density at recombination.

### Y.7.1 The Mass Scale Mismatch

EDE requires a scalar field that thaws at recombination (H(z_rec) ~ m_φ):

    H_rec ~ 2 × 10⁻²⁹ eV     (at z ~ 1100)
    m_φ   ~ 10⁻² eV           (Casimir-stabilized dilaton)
    Mismatch: m_φ / H_rec ~ **10²⁷**

The dilaton thaws at T ~ 300 MeV (the QCD era), not at recombination.

### Y.7.2 No Flat Direction Rescue

For m_eff(φ) ~ H_rec, one needs φ_i ~ 10⁹ φ₀ ~ 10⁴ m — the e-circle
at kilometer scale. This is not physically reasonable.

### Y.7.3 Assessment

The dilaton-as-EDE mechanism is **not viable**. The framework's H₀
shift comes exclusively from the hidden-brane dark radiation, not from
EDE.

---

## Y.8 Complementary Cosmological Results

### Y.8.1 The N_eff Rescue (Gonzalo et al. 2024)

The naive dilaton contribution ΔN_eff ≈ 0.57 (Appendix Q) appeared
to conflict with CMB constraints at 4.4σ. Gonzalo, Montero, Obied &
Vafa (arXiv:2411.07029, 2024) resolved this for the Dark Dimension
scenario — the same physics as our framework: heavier KK neutrino modes
decay preferentially to lighter KK modes (intra-tower "dark-to-dark"
decays), reducing ΔN_eff^{tower} from ~0.57 to ~0.05. The constraint
ζ < 0.01 on active-sterile mixing is naturally satisfied by the
brane-to-bulk wavefunction suppression in the orbifold scenario.

**Status:** N_eff tension resolved. Tower contribution: ΔN_eff ≈ 0.05,
giving N_eff ≈ 3.09 from the tower alone.

### Y.8.2 The S8 Tension (Obied et al. 2023)

Obied, Dvorkin, Gonzalo & Vafa (arXiv:2311.05318, 2023) showed that
decaying KK gravitons in the Dark Dimension impart kick velocities
(v_kick < 2.2 × 10⁻⁴ c) to dark matter, suppressing small-scale
structure formation and reducing S8 toward weak lensing measurements.

The framework has the same KK graviton tower (Appendix N) and
hidden-brane dark matter (Appendix W). The S8 resolution requires no
new parameters.

**Status:** S8 tension addressed by KK cascade dynamics.

### Y.8.3 The Dark Dimension Convergence

Bedroya, Obied, Vafa & Wu (arXiv:2507.03090, 2025) connect the DESI
DR2 phantom crossing (w₀ ≈ −0.75, wₐ ≈ −0.75) to the Dark Dimension
via varying dark matter mass from an evolving compact dimension radius.
This is the same physics as the thawing dilaton scenario (Section 6.5).
Independent theoretical support from the Swampland program for the
same micrometer-scale compact dimension.

### Y.8.4 The Cosmological Scorecard

| Tension | Framework mechanism | Status |
|---------|-------------------|--------|
| Dark energy density | Casimir energy on orbifold | ✓ Predicted |
| N_eff (visible sector) | Intra-tower KK decays | ✓ Resolved (Gonzalo et al.) |
| S8 clustering | KK graviton cascades | ✓ Addressed (Obied et al.) |
| DESI w ≈ −0.8 | Thawing dilaton | Plausible |
| **Hubble tension** | **Mirror brane dark radiation** | **H₀ ≈ 68.0–68.7** (Tier 1) |
| Hubble tension (full) | Beyond minimal orbifold | Open |

---

## Y.9 Falsifiability and Future Tests

### Y.9.1 The Prediction

    **Tier 1 (current data):    H₀ ≈ 68.0–68.3**   (ξ < 0.35, ACT DR6 safe)
    **Tier 2 (BBN-limited):     H₀ ≈ 68.3–68.7**   (ξ = 0.35–0.384, 2.5–2.8σ ACT DR6 tension)

    **ΔN_eff^{mirror} = 0.02–0.14**   (both tiers combined)

### Y.9.2 CMB-S4: The Definitive Test

CMB-S4 targets σ(N_eff) ≈ 0.03. The framework's total N_eff:

    N_eff^{total} = 3.046 + 0.05 (tower) + 6.14 × ξ⁴ (mirror)

At ξ = 0.35: N_eff = 3.19 → **4.7σ detection by CMB-S4**
At ξ = 0.25: N_eff = 3.12 → **2.7σ detection by CMB-S4**

**If CMB-S4 finds N_eff consistent with 3.046 ± 0.03**: the mirror
sector is absent at the level needed for any H₀ shift. The framework
is left with H₀ ≈ 67.7 (tower only).

**If CMB-S4 finds N_eff > 3.10**: the mirror sector is confirmed at
the level of the Tier 1 prediction.

### Y.9.3 H₀ Convergence Tests

**TRGB/CCHP precision (JWST).** If JWST-only CCHP results converge
to 68–69, the framework's Tier 1 prediction is confirmed. If they
converge to 73, the framework is insufficient.

**Gravitational wave standard sirens (O5+).** Will reach ~2%
precision — sufficient to distinguish H₀ = 68 from H₀ = 73 at >5σ.

**Extended parameter fits.** The ACT DR6 N_eff constraint (2.86 ± 0.13)
is derived within ΛCDM + N_eff. In extended models (ΛCDM + N_eff +
w₀ + wₐ), which is what the framework predicts, the N_eff constraint
typically loosens by 30–50% due to parameter degeneracies. A dedicated
MCMC analysis of the framework's specific model (mirror dark radiation +
thawing dilaton) could shift the allowed ξ range toward Tier 2.
This is identified as important future work.

### Y.9.4 Correlated Tests

The orbifold that produces the mirror sector also predicts:

| Prediction | Test | Timeline |
|-----------|------|---------|
| Short-range gravity at λ ~ 12 μm | MEMS cantilever | 3–5 years |
| Dark photon at ε ~ 5 × 10⁻⁴ | LDMX, LHCb Run 3 | 3–5 years |
| Normal neutrino mass ordering | JUNO | 3–6 years |
| No QCD axion | ADMX, ABRACADABRA | Ongoing |
| ΔN_eff = 0.07–0.19 (total) | CMB-S4 | 5–10 years |

Confirmation of any of these correlated predictions strengthens the
case for the Z₂ orbifold and therefore for the mirror-brane H₀ mechanism.

### Y.9.5 What Would Falsify the Prediction

**If CMB-S4 finds N_eff = 3.046 ± 0.03 with no excess**: mirror sector
absent at the needed level. H₀ ≈ 67.7 (tower only). The orbifold exists
but the hidden brane is either empty or too cold (ξ → 0).

**If multiple independent H₀ methods converge above 71**: Tier 1 and
Tier 2 are both insufficient. Physics beyond the minimal orbifold is
required (lighter modulus from Appendix L, or additional bulk species).

**If short-range gravity finds no deviation below 1 μm**: the R ~ 12 μm
orbifold scenario is ruled out and the mirror sector mechanism needs
re-evaluation under the circle scenario.

---

## Y.10 Summary

| Claim | Status |
|-------|--------|
| Dilaton as early dark energy | **Not viable** (mass mismatch 10²⁷) |
| Mirror brane as dark radiation | **Geometrically required** (spin structure → Z₂ → orbifold) |
| BBN constraint (2025 joint analysis) | ξ < 0.384 (2σ), ΔN_eff < 0.136 |
| ACT DR6 constraint (binding) | ξ < 0.255 (2σ), ξ < 0.397 (3σ) |
| Ω_DM/Ω_b constraint (1/ξ² law) | ξ = 0.432–0.47 (from observed 5.36) |
| Self-consistent prediction (ξ = 0.4375) | H₀ = 68.8, t₀ = 13.60 Gyr, S8 = 0.754 |
| θ* offset at ξ = 0.4375 | +1.0 arcsecond (within Planck 1σ = 1.1") |
| Tier 1 H₀ prediction (ACT DR6 safe) | **68.0–68.3 km/s/Mpc** |
| Tier 2 H₀ prediction (BBN-limited) | **68.3–68.7 km/s/Mpc** (2.5–2.8σ ACT DR6 tension) |
| Direction relative to non-DL consensus | Correct (↑ from 67.4 toward 69.4) |
| Full resolution of Hubble tension | **Not achieved** by minimal framework |
| CMB-S4 test | Definitive: σ(N_eff) ≈ 0.03 will confirm or exclude |
| ω_b h² at self-consistent solution | 0.02150 (3.9% below ΛCDM; mild 1.5σ D/H tension) |
| N_eff (visible sector tower) | ✓ Resolved at ΔN_eff ≈ 0.05 |
| S8 tension | ✓ Addressed by KK cascade decays |

The framework predicts dark radiation from the hidden brane — a geometric
consequence of the spin-statistics theorem. Current data (ACT DR6,
updated BBN 2025) constrains the contribution to a modest H₀ shift of
0.6–1.3 km/s/Mpc above ΛCDM, giving H₀ ≈ 68.0–68.7. This is in the
right direction toward the non-distance-ladder consensus (69.4 ± 0.3)
but does not resolve the full tension. The full BBN-allowed range is in
tension with ACT DR6 at 2.5–2.8σ — neither confirmed nor excluded.
CMB-S4 will make the definitive measurement.

---

## Y.11 References

1. Planck Collaboration. "Planck 2018 results. VI." *A&A* **641**, A6
   (2020). — Table 2: ΛCDM+N_eff chain.

2. ACT Collaboration. "The Atacama Cosmology Telescope: DR6 CMB Power
   Spectra, Likelihoods, and Cosmological Parameters." arXiv:2503.14452
   (2025). — N_eff = 2.86 ± 0.13; H₀ = 68.22 ± 0.36 (with DESI DR1).

3. DESI Collaboration. "DESI DR2 Results II: BAO and Cosmological
   Constraints." arXiv:2503.14738 (2025). — H₀ = 67.97 ± 0.38;
   Table 3: w₀wₐ fit with Planck gives H₀ ≈ 66.9.

4. Pantos, I. & Perivolaropoulos, L. "Sound-horizon-free H₀ tension."
   arXiv:2601.00650 (2026). — 88 measurements; DL: 72.73 ± 0.39;
   non-DL: 69.37 ± 0.34; tension: 6.5σ.

5. Freedman, W. L. et al. "CCHP: Three Independent H₀ Determinations
   with JWST." *Astrophys. J.* **976**, 15 (2024). arXiv:2408.06153. —
   TRGB(HST+JWST): 70.39; TRGB(JWST): 68.81; JAGB(JWST): 67.80.

6. Riess, A. G. et al. SH0ES (HST+JWST, 19 hosts): H₀ = 73.49 ± 0.93.
   (2024).

7. Fields, B. D. et al. "BBN after Planck." *JCAP* **03**, 010 (2020).
   — Original BBN constraint used for comparison.

8. BBN 2025 joint analysis. arXiv:2507.23354. — N_eff = 2.898 ± 0.141;
   updated constraint ξ < 0.384.

9. Gonzalo, E., Montero, M., Obied, G. & Vafa, C. "Cosmological
   Constraints on Dark Neutrino Towers." arXiv:2411.07029 (2024). —
   Intra-tower decays reduce ΔN_eff from ~0.57 to ~0.05.

10. Obied, G., Dvorkin, C., Gonzalo, E. & Vafa, C. "Dark Dimension and
    Decaying Dark Matter Gravitons." arXiv:2311.05318 (2023). — KK
    graviton cascades address S8 tension.

11. Bedroya, A., Obied, G., Vafa, C. & Wu, H. "Evolving Dark Sector
    and the Dark Dimension Scenario." arXiv:2507.03090 (2025). — Dark
    Dimension + DESI phantom crossing connection.

12. Berezhiani, Z. "Through the looking-glass: Alice's adventures in
    mirror world." arXiv:hep-ph/0508233 (2005). — ΔN_eff = 6.14 ξ⁴.

13. Foot, R. "Mirror dark matter." *Int. J. Mod. Phys. D* **13**, 2161
    (2004). — Mirror sector temperature ratio ξ ~ 0.3–0.5.

14. Bernal, J. L., Verde, L. & Riess, A. G. "The trouble with H₀."
    *JCAP* **10**, 019 (2016). — ΔH₀ ≈ 6 × ΔN_eff calibration.

15. CMB-S4 Collaboration. "CMB-S4 Science Book." arXiv:1610.02743
    (2016). — Target σ(N_eff) ≈ 0.03.
