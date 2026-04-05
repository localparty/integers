# Appendix N — Gravitational Wave Signatures of the E-Dimension

> The KK decomposition of the 5D graviton produces a tower of massive spin-2
> modes in addition to the standard massless graviton. This appendix computes
> their masses, polarizations, and observational consequences for gravitational
> wave detectors.

---

## N.1 The KK Graviton Tower

The 5D graviton field `ĥ_{AB}(x, ψ)` decomposes on the e-circle into a
Kaluza-Klein tower (Appendix F, Section F.1.2):

    ĥ_{AB}(x, ψ) = Σ_{n=-∞}^{∞} h_{AB}^{(n)}(x) e^{inψ/R}

Each mode `n` is a 4D field with mass:

    m_n = |n| ℏ / (Rc) = |n| × m_KK

where `m_KK = ℏ/(Rc)` is the fundamental KK mass.

For `R = 21 μm` (the Casimir prediction):

    m_KK = (1.055 × 10⁻³⁴ × 2.998 × 10⁸) / (2.1 × 10⁻⁵)
         = 1.51 × 10⁻²¹ J = 9.4 meV

    f_KK = m_KK c² / h = 9.4 × 10⁻³ × 1.602 × 10⁻¹⁹ / (6.626 × 10⁻³⁴)
         = 2.27 × 10¹² Hz = 2.27 THz

The first KK graviton mode oscillates at `~2.3 THz` — in the far-infrared.

---

## N.2 Polarizations

### N.2.1 The Massless Graviton (`n = 0`)

The `n = 0` mode is the standard 4D massless graviton:
- **2 tensor polarizations** (+ and ×) — the standard GR gravitational waves
- These propagate at the speed of light
- Detected by LIGO, Virgo, KAGRA, LISA

The 5D framework makes NO modification to the massless graviton. Standard
gravitational waves are identical in the framework and in GR.

### N.2.2 The Massive KK Gravitons (`n ≥ 1`)

Each massive KK mode has additional polarizations compared to the massless
graviton. A massive spin-2 particle in 4D has **5 polarization states**
(compared to 2 for massless):

| Polarization | Helicity | Present in GR? | Present in KK? |
|-------------|---------|---------------|---------------|
| Tensor + | ±2 | Yes | Yes |
| Tensor × | ±2 | Yes | Yes |
| Vector x | ±1 | No | **Yes** |
| Vector y | ±1 | No | **Yes** |
| Scalar (breathing) | 0 | No | **Yes** |

The 3 additional polarizations (two vector + one scalar) are the signature
of massive gravitons. They arise because the massive spin-2 field has more
degrees of freedom than the massless one (5 vs 2).

Additionally, the KK decomposition produces:
- A massive vector field (from `ĥ_{μ5}`) with **3 polarizations** per mode
- A massive scalar field (from `ĥ_{55}`) with **1 polarization** per mode

Total degrees of freedom per KK level: `5 + 3 + 1 = 9`.

---

## N.3 Detection Prospects

### N.3.1 Frequency Comparison

| Detector | Frequency band | KK frequency | Detectable? |
|---------|---------------|-------------|-------------|
| LIGO/Virgo | `10 – 10⁴ Hz` | `2.3 × 10¹² Hz` | **No** (`10⁸×` too high) |
| LISA | `10⁻⁴ – 1 Hz` | `2.3 × 10¹² Hz` | **No** (`10¹²×` too high) |
| Pulsar timing | `10⁻⁹ – 10⁻⁷ Hz` | `2.3 × 10¹² Hz` | **No** |
| CMB B-modes | `~10⁻¹⁸ Hz` | `2.3 × 10¹² Hz` | **No** |
| **THz spectroscopy** | **`10¹¹ – 10¹³ Hz`** | **`2.3 × 10¹² Hz`** | **In band** |

The KK graviton frequency falls in the THz (far-infrared) band. No current
gravitational wave detector operates at this frequency. However, THz
spectroscopy and photonics are active experimental fields — the frequency
is accessible to table-top experiments, even if the gravitational coupling
is extremely weak.

### N.3.2 The Coupling Problem

The massive KK gravitons couple to matter with the same strength as the
massless graviton — gravitational strength `G_N`. The cross-section for
producing a KK graviton is:

    σ ~ G_N E²/c⁴ ~ (l_P/λ)² × λ²

where `λ` is the wavelength and `l_P` is the Planck length. For THz radiation
(`λ ~ 100 μm`):

    σ ~ (10⁻³⁵/10⁻⁴)² × (10⁻⁴)² ~ 10⁻⁶² × 10⁻⁸ ~ 10⁻⁷⁰ m²

This is absurdly small — about `10³⁰` times smaller than the weak interaction
cross-section. **Direct production of KK gravitons is not feasible with any
foreseeable technology.**

### N.3.3 Indirect Signatures

Although direct production is impossible, the KK modes contribute virtually
to gravitational processes:

**Modified Newton's law at short range.** The virtual exchange of massive KK
gravitons produces the Yukawa correction to gravity at distances `r ~ R ~ 21 μm`
(Appendix H, Prediction 1). This is the most promising experimental signature
— it detects the KK tower indirectly through its effect on the static force
law.

**Casimir force modifications.** The KK graviton modes contribute to the
Casimir effect between conducting plates at separations `d ~ R`. The graviton
Casimir force is negligible compared to the electromagnetic Casimir force
(by a factor of `G_N/α ~ 10⁻⁴⁰`), but it represents a calculable quantum
gravity effect.

**Graviton emission in high-energy collisions.** At collider energies
`E >> m_KK c²`, the KK tower appears as a quasi-continuum of massive gravitons.
The total cross-section for graviton emission sums over all accessible KK
modes. For the e-circle with `R ~ 21 μm` (`m_KK ~ 10 meV`), essentially ALL
KK modes up to `n ~ E/(m_KK c²)` contribute. At LHC energies (`E ~ 10⁴ GeV`):
`n_max ~ 10⁴/(10⁻² eV) ~ 10⁶` modes. The summed cross-section is enhanced by
`n_max` but still gravitationally suppressed.

---

## N.4 What LIGO Does NOT See

An important null prediction: **LIGO sees exactly the standard GR gravitational
waves.** The massless graviton (`n = 0`) is identical to the GR graviton. The
massive modes (`n ≥ 1`) are at THz frequencies, far above LIGO's band. The KK
tower does not produce any signal in LIGO, Virgo, KAGRA, or LISA.

This is consistent with all current observations: LIGO's detections of binary
black hole and neutron star mergers match GR predictions with no excess
polarizations or anomalous frequency components.

**If LIGO were to detect anomalous gravitational wave polarizations (vector
or scalar modes), it would be evidence against the framework** — because the
only massive gravitons in the KK tower are at THz frequencies, not in LIGO's
Hz-kHz band.

---

## N.5 The Graviton Mass Bound

Gravitational wave observations constrain the graviton mass. LIGO's
observation of GW150914 gives:

    m_{graviton} < 1.2 × 10⁻²² eV

(Abbott et al. 2016)

This bounds the mass of the **massless graviton** (the `n = 0` mode). In the
KK framework, the `n = 0` mode IS massless — the bound is satisfied trivially.
The massive KK modes (`m_n ≥ 9.4 meV`) are not constrained by this bound
because they are not the graviton that produces the observed GW signal.

---

## N.6 Gravitational Wave Speed

In GR and in the KK framework, the massless graviton travels at exactly
the speed of light: `v_g = c`. The joint detection of GW170817 (gravitational
waves) and GRB170817A (gamma-ray burst) from a neutron star merger confirmed:

    |v_g/c − 1| < 10⁻¹⁵

(Abbott et al. 2017)

The KK framework satisfies this trivially: the massless graviton propagates
on the null cone of the 4D base metric `gμν`, which is exactly the speed of
light. The massive KK modes propagate SLOWER than light (`v < c` for massive
particles), but they are not the modes detected by LIGO.

---

## N.7 Summary of Gravitational Wave Predictions

| Observable | GR prediction | 5D framework prediction | Status |
|-----------|-------------|------------------------|--------|
| GW polarizations (LIGO band) | 2 (tensor +, ×) | 2 (tensor +, ×) — identical | Consistent |
| GW speed | `c` exactly | `c` exactly (`n=0` mode) | Consistent |
| Graviton mass | 0 | 0 (`n=0`); `9.4n` meV (`n≥1`) | Consistent |
| Additional polarizations | None | 5 per KK mode, at THz | Not yet testable |
| Yukawa gravity correction | None | `α_G e^{−r/21μm}` at `r < 100 μm` | Testable (Prediction 1) |

**The framework is fully consistent with all gravitational wave
observations.** It predicts no deviations from GR in the LIGO/LISA frequency
band. The KK graviton signatures are at THz frequencies — currently
inaccessible to GW detectors but in principle within reach of far-infrared
technology.

---

## N.8 References

- Abbott, B. P. et al. (LIGO/Virgo). "Tests of General Relativity with
  GW150914." *Phys. Rev. Lett.* 116, 221101 (2016).
- Abbott, B. P. et al. "Gravitational Waves and Gamma-Rays from a Binary
  Neutron Star Merger: GW170817 and GRB 170817A." *Astrophys. J. Lett.*
  848, L13 (2017).
- de Rham, C. "Massive Gravity." *Living Rev. Rel.* 17, 7 (2014). —
  Comprehensive review of massive graviton physics.
- Han, T., Lykken, J. D. & Zhang, R.-J. "Kaluza-Klein States from Large
  Extra Dimensions in Relation to the Tevatron, LHC, and NLC."
  *Phys. Rev. D* 59, 105006 (1999).
