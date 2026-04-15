# Research 86: Log-Periodic CMB Prediction — Numerical Assessment

*Does the BC framework's most distinctive inflation prediction —*
*log-periodic oscillations in P_R(k) — produce a detectable signal*
*in the CMB angular power spectrum?*

*Authors: G Six, with Claude Opus 4.6*
*Date: 2026-04-09*
*Builds on: research/71 (inflation in detail), research/43*
*(inflation initial conditions), research/30 (n_s = gamma_9/gamma_10).*

---

## 1. The Question

Research/71 (Section 4.3) identifies a distinctive, falsifiable
prediction of the BC framework: the primordial curvature spectrum
carries a log-periodic modulation at period Delta_ln_k = 2pi/gamma_1
with amplitude A_log ~ few x 10^{-3}. This modulation arises because
the BC spectrum is a discrete set {gamma_n pi^2/2}, and the
correlator at horizon crossing picks up a Mellin-transform oscillation
locked to the first non-trivial Riemann zero gamma_1 = 14.1347.

The question is quantitative: does this 0.3% modulation in P_R(k)
survive the k-to-ell projection (via Bessel functions) and remain
above Planck's noise floor? If yes, we have an actionable near-term
test. If no, we need to quantify what *would* be needed.

This note answers that question via numerical computation.

---

## 2. The Predicted Primordial Power Spectrum

### 2.1 The modulated P_R(k)

From research/71 equation (4.5), the BC framework predicts:

$$
P_R(k) = A_s \left(\frac{k}{k_*}\right)^{n_s - 1}
\left[1 + A_{\mathrm{log}} \cos\!\left(\gamma_1 \ln\frac{k}{k_*}
+ \phi_0\right)\right]
$$

with parameters fixed by BC structure:

| Parameter | Value | BC source |
|:----------|:------|:----------|
| A_s | 2.1 x 10^{-9} | standard (input) |
| k_* | 0.05 Mpc^{-1} | pivot (convention) |
| n_s | gamma_9/gamma_10 = 0.96425 | BC eigenvalue ratio |
| gamma_1 | 14.1347 | first Riemann zero |
| Delta_ln_k | 2pi/gamma_1 = 0.4445 | log-periodic period |
| A_log | 3 x 10^{-3} | subleading Mellin expansion |
| phi_0 | unknown (0 to 2pi) | phase; framework does not fix |

The spectral index n_s = 0.96425 sits within the Planck 2018
1-sigma band (0.9649 +/- 0.0042).

### 2.2 Key features of the modulation

The log-periodic cosine oscillates with *constant period in ln k*:
every Delta_ln_k = 0.4445 e-folds in wavenumber, the modulation
completes one full cycle. This means:
- In linear k-space, the oscillation frequency increases with k.
- In ell-space (via k ~ ell/eta_0), the angular spacing scales as
  Delta_ell ~ 0.44 * ell — i.e., geometric (multiplicative) rather
  than arithmetic (additive) spacing.

This geometric spacing is the distinctive signature: standard BAO
features have *additive* Delta_ell ~ 300, while the BC prediction
has *multiplicative* Delta_ell/ell ~ 0.44.

---

## 3. The Angular Power Spectrum C_ell

### 3.1 Sachs-Wolfe approximation

We compute C_ell via the Sachs-Wolfe approximation:

$$
C_\ell = \frac{4\pi}{9} \int \frac{dk}{k}\, P_R(k)\,
j_\ell^2(k\,\eta_0)
$$

where eta_0 = 14,000 Mpc is the comoving conformal distance to the
last scattering surface and j_ell is the spherical Bessel function.

This approximation captures the correct physics for large scales
(ell < 100) and gives the right order of magnitude at smaller scales.
A full Boltzmann code (CAMB/CLASS) would add acoustic oscillations
that reshape C_ell but would preserve the *fractional modulation*
Delta_C_ell/C_ell at approximately the same amplitude, since the
log-periodic modulation is multiplicative in P_R(k).

### 3.2 Integration details

The script (log_periodic_cmb_prediction.py) computes C_ell at 269
ell values from 2 to 2500, using scipy.integrate.quad with
scipy.special.spherical_jn. For each ell, the integration range is
centered on k ~ ell/eta_0 and extends +/- 1.5 decades. Relative
tolerance is 10^{-6}.

Two spectra are computed:
- C_ell^{smooth}: from P_R(k) without modulation (A_log = 0).
- C_ell^{mod}: from the full modulated P_R(k).

The fractional residual is:

$$
\frac{\Delta C_\ell}{C_\ell} = \frac{C_\ell^{\mathrm{mod}} -
C_\ell^{\mathrm{smooth}}}{C_\ell^{\mathrm{smooth}}}
$$

---

## 4. Results: The Modulation Signature

### 4.1 Amplitude of Delta_C_ell / C_ell

| Statistic | Value |
|:----------|:------|
| Mean |Delta_C/C| | 1.3 x 10^{-3} |
| Max Delta_C/C | +2.93 x 10^{-3} |
| Min Delta_C/C | -2.96 x 10^{-3} |
| RMS | 1.6 x 10^{-3} |

The fractional residual in C_ell is approximately half the input
A_log = 3 x 10^{-3}. This factor-of-two reduction is expected: the
Bessel function projection j_ell^2(k eta_0) is a broad kernel in
k-space that partially averages out the log-periodic oscillation.

The surviving amplitude |Delta_C/C| ~ 1-3 x 10^{-3} is the actual
observable signal in the CMB.

### 4.2 Peak and trough locations

The log-periodic oscillation produces a characteristic pattern of
peaks and troughs with geometrically spaced ell values:

**Peaks** (Delta_C/C > 0):
  ell = 5, 12, 19, 30, 46, 72, 115, 175, 270, 430

**Troughs** (Delta_C/C < 0):
  ell = 4, 10, 15, 24, 38, 58, 90, 140, 220, 345

Consecutive peak ratios confirm the expected geometric spacing:

| Pair | Ratio | Expected (e^{0.4445}) |
|:-----|:------|:----------------------|
| 12/5 | 2.40 | 1.56 (2 cycles) |
| 19/12 | 1.58 | 1.56 |
| 30/19 | 1.58 | 1.56 |
| 46/30 | 1.53 | 1.56 |
| 72/46 | 1.57 | 1.56 |
| 115/72 | 1.60 | 1.56 |
| 175/115 | 1.52 | 1.56 |
| 270/175 | 1.54 | 1.56 |
| 430/270 | 1.59 | 1.56 |

The ratios cluster around exp(0.4445) = 1.56 as predicted, with
scatter of order +/- 0.05 from the finite width of the Bessel
projection kernel. This is the distinctive geometric-spacing
fingerprint.

### 4.3 Characteristic angular spacing

The angular spacing of the modulation depends on ell:

| ell | Delta_ell |
|:----|:----------|
| 50 | ~22 |
| 100 | ~44 |
| 200 | ~89 |
| 500 | ~222 |
| 1000 | ~445 |
| 2000 | ~889 |

At high ell, the oscillation period becomes very broad — wider than
acoustic peaks — making it difficult to separate from smooth
spectral tilts or calibration uncertainties.

---

## 5. Planck Sensitivity Comparison

### 5.1 Noise model

The fractional uncertainty per ell mode has three contributions:

1. **Cosmic variance**: sigma_CV / C_ell = sqrt(2/(2ell+1)),
   irreducible.

2. **Instrumental noise**: N_ell = sigma_T^2 exp(ell(ell+1) sigma_b^2)
   with sigma_T = 5 muK-arcmin and FWHM = 5 arcmin (Planck 143 GHz).

3. **Sky fraction**: f_sky = 0.70 (Planck common mask), which
   inflates variance by 1/f_sky.

The total fractional uncertainty per mode is:

$$
\frac{\sigma(C_\ell)}{C_\ell} = \frac{1}{\sqrt{f_{\mathrm{sky}}}}
\sqrt{\frac{2}{2\ell+1}} \left(1 + \frac{N_\ell}{C_\ell}\right)
$$

### 5.2 Per-ell signal-to-noise

| ell | |Delta_C/C| | sigma_total | SNR |
|:----|:-----------|:------------|:----|
| 2 | 2.2 x 10^{-3} | 0.76 | 0.003 |
| 10 | 2.7 x 10^{-3} | 0.37 | 0.007 |
| 30 | 2.9 x 10^{-3} | 0.22 | 0.013 |
| 100 | 5.3 x 10^{-4} | 0.12 | 0.004 |
| 500 | 1.2 x 10^{-3} | 0.053 | 0.022 |
| 1000 | 1.6 x 10^{-4} | 0.038 | 0.004 |
| 2000 | 3.0 x 10^{-4} | 0.027 | 0.011 |
| 2500 | 2.1 x 10^{-3} | 0.024 | 0.089 |

The per-ell SNR is everywhere << 1. At low ell, the signal is
largest (~3 x 10^{-3}) but cosmic variance dominates (sigma ~ 0.2-0.8).
At high ell, noise is smaller but the Bessel averaging reduces the
signal.

### 5.3 Cumulative signal-to-noise

Summing in quadrature over all ell values:

| ell range | Cumulative SNR |
|:----------|:---------------|
| [2, 30] | 0.037 |
| [30, 100] | 0.084 |
| [100, 500] | 0.240 |
| [500, 1000] | 0.172 |
| [1000, 2500] | 0.318 |
| **[2, 2500]** | **0.443** |

**Total cumulative SNR = 0.44**, far below the 3-sigma detection
threshold.

### 5.4 Binned analysis

A more realistic binned analysis (Delta_ell = 30 bins, averaging the
signal and reducing noise by sqrt(N_modes)) gives a total binned
SNR = 0.34, consistent with the per-mode estimate.

---

## 6. Detectability Assessment

### 6.1 The verdict

**The log-periodic modulation at A_log = 3 x 10^{-3} is
UNDETECTABLE in current Planck data.**

The total cumulative SNR of 0.44 means the signal is buried ~7x
below the noise floor. Even optimizing the ell range, the best
achievable SNR is 0.43 (essentially the full range contributes).

### 6.2 What amplitude would be needed?

For 3-sigma detection in Planck data: **A_log >= 0.020** (a factor
of 6.8 above the BC prediction).

For 2-sigma marginal evidence: A_log >= 0.014.

The BC framework predicts A_log ~ "few x 10^{-3}" from the
subleading Mellin expansion. This is an order-of-magnitude estimate;
the actual coefficient depends on the precise Mellin residue at the
first zero. If the amplitude were at the upper end of "few" (say
A_log = 0.01), the cumulative SNR would scale to ~1.5, still below
detection threshold but entering the "marginally interesting" regime.

### 6.3 Why detection is hard

Three effects conspire:

1. **Cosmic variance dominates at low ell** (ell < 500), where the
   Bessel averaging preserves the most signal. At ell = 30, the
   signal is 2.9 x 10^{-3} but cosmic variance is 22%.

2. **Bessel averaging at high ell**: the spherical Bessel function
   j_ell(k eta_0) has width Delta_k/k ~ 1/ell in k-space. For
   ell > 500, this width exceeds the log-periodic half-period, and
   the oscillation is partially washed out.

3. **Geometric (not arithmetic) spacing**: unlike BAO features that
   add coherently across many ell modes with fixed Delta_ell ~ 300,
   the log-periodic signal has Delta_ell proportional to ell.
   At high ell, each "cycle" spans hundreds of ell values, providing
   no more statistical leverage than a smooth tilt.

### 6.4 Phase dependence

The unknown phase phi_0 shifts the pattern but does not change the
amplitude. The script scans phi_0 = 0, pi/4, pi/2, 3pi/4, pi and
confirms the RMS of Delta_C/C is phase-independent (as expected for
a stationary oscillation projected through a symmetric kernel).

---

## 7. Paths to Detection

### 7.1 Optimal matched-filter analysis

A dedicated matched-filter search for the log-periodic template in
the Planck power spectrum would be the most sensitive test. The
template has only two free parameters: A_log and phi_0. The
wavenumber gamma_1 = 14.1347 is fixed by the framework.

Even with optimal filtering, the SNR gain over the naive quadrature
sum is modest (of order sqrt(2) from the matched-filter theorem),
bringing the expected SNR to ~0.6 — still undetectable.

### 7.2 Combined Planck + ACT + SPT

Adding ground-based experiments (ACT, SPT-3G) to Planck extends the
usable ell range to ~4000 with lower noise at high ell. However, the
Bessel averaging effect worsens at higher ell. The gain from
ell > 2500 is marginal.

Estimated combined SNR: ~0.6-0.8. Still insufficient.

### 7.3 Next-generation experiments

CMB-S4 (sigma_T ~ 1 muK-arcmin, ell_max ~ 5000) and LiteBIRD
(cosmic-variance-limited to ell ~ 200) would improve the picture:

- **LiteBIRD** (ell < 200, near-CV-limited): the main gain is
  slightly reduced noise at ell = 30-200, but cosmic variance still
  dominates. Marginal improvement.

- **CMB-S4** (ell < 5000, low noise): reduces sigma_total by ~5x at
  ell > 1000, but Bessel averaging limits the signal. Estimated
  cumulative SNR ~ 1.5-2.0 for A_log = 3 x 10^{-3}.

- **Combined LiteBIRD + CMB-S4**: possibly SNR ~ 2-2.5.
  Marginal detection only.

### 7.4 The real lever: primordial spectrum reconstruction

The most promising approach bypasses C_ell entirely and directly
reconstructs P_R(k) from data, e.g. via:

- **Free-form P_R(k) reconstruction** (cubic spline nodes in ln k).
- **Fourier analysis of residuals** in ln k after removing smooth
  power-law.

In reconstructed P_R(k), the log-periodic modulation appears at
full amplitude A_log = 3 x 10^{-3} without Bessel dilution. The
relevant "noise" is the reconstruction uncertainty, which at
Planck precision is delta P_R / P_R ~ 0.02-0.05 depending on k.

At A_log = 3 x 10^{-3}, the modulation is still a factor of ~10
below reconstruction noise. But a Fourier search at the specific
frequency gamma_1 = 14.13 in ln k could, in principle, accumulate
signal over many cycles.

Number of cycles in the Planck k-range [10^{-4}, 0.2] Mpc^{-1}:
  N_cycles = ln(0.2/10^{-4}) / Delta_ln_k = 7.6 / 0.4445 ~ 17
  cycles.

SNR from Fourier analysis ~ A_log * sqrt(N_cycles) / delta_P_R
  ~ 3e-3 * 4.1 / 0.03 ~ 0.4.

Still insufficient. However, this analysis deserves a dedicated
study with actual Planck likelihood data.

### 7.5 The honest assessment

The BC framework's log-periodic prediction at A_log = 3 x 10^{-3}
is not accessible to any current or near-future CMB experiment as
a standalone detection. It becomes **marginally accessible** (SNR
~ 2) only with CMB-S4 + optimal matched-filter analysis.

However, the prediction remains extremely valuable as a
**consistency check**: if an unrelated analysis of Planck data
were to find evidence for log-periodic features in P_R(k) at the
specific frequency gamma_1 = 14.13, the coincidence with the first
Riemann zero would be powerful evidence for the BC framework.
Existing searches for "resonant non-Gaussianity" and "oscillatory
features" in Planck data (Planck 2018 Paper X, Section 7) do
constrain related models, though they have not targeted this
specific frequency.

---

## 8. Comparison to Existing Searches

Planck 2018 Paper X (Akrami et al. 2020) searched for oscillatory
features in the primordial power spectrum with templates:

$$
P_R(k) = A_s (k/k_*)^{n_s - 1}
\left[1 + A_{\mathrm{feat}} \cos(\omega \ln(k/k_*) + \phi)\right]
$$

They scanned omega in [1, 1000] and found no significant detection
above the 3-sigma threshold. For omega = gamma_1 = 14.13, which
falls in the low-frequency range of their scan, they place an upper
bound of roughly A_feat < 0.03-0.05 (depending on the analysis
method).

The BC prediction A_log = 3 x 10^{-3} is well below this bound,
consistent with non-detection.

---

## 9. Summary Table

| Quantity | Value |
|:---------|:------|
| Primordial modulation amplitude A_log | 3 x 10^{-3} |
| Log-periodic period Delta_ln_k | 0.4445 |
| Frequency in ln(k) space: gamma_1 | 14.1347 |
| Angular spacing: Delta_ell/ell | ~0.44 (geometric) |
| Mean |Delta_C_ell/C_ell| | 1.3 x 10^{-3} |
| Peak |Delta_C_ell/C_ell| | 3.0 x 10^{-3} |
| Total cumulative SNR (Planck) | 0.44 |
| Required A_log for 3-sigma | >= 0.020 |
| Assessment | **UNDETECTABLE** |
| Best future prospect | CMB-S4 matched-filter: SNR ~ 2 |

---

## 10. Precise Prediction Statement

> **The BC framework predicts log-periodic oscillations in the CMB TT
> power spectrum at fractional angular spacing Delta_ell/ell = 0.44,
> corresponding to the first non-trivial Riemann zero gamma_1 =
> 14.1347, with amplitude |Delta_C_ell/C_ell| ~ 1.3 x 10^{-3}.
> The oscillation peaks appear at geometrically spaced multipoles
> ell ~ 5, 12, 19, 30, 46, 72, 115, 175, 270, 430, ..., with
> consecutive ratios clustering around exp(2pi/gamma_1) = 1.56.
> The total cumulative signal-to-noise in Planck data is 0.44,
> making this signal undetectable in current CMB data. Detection
> would require either an amplitude 7x larger than predicted, or
> a next-generation experiment (CMB-S4) combined with optimal
> matched-filter analysis targeting the known frequency gamma_1.**

---

## 11. Implications for the BC Framework

### 11.1 Non-falsification

The non-detectability at A_log = 3 x 10^{-3} is *not* a problem for
the framework. The prediction is consistent with Planck's null result
for oscillatory features. The framework is not falsified; it simply
makes a prediction below current sensitivity.

### 11.2 The amplitude estimate

The value A_log ~ 3 x 10^{-3} comes from the "subleading Mellin
expansion" of the BC partition function (research/71, Section 4.3).
This is an order-of-magnitude estimate, not a rigorous computation.
A more careful calculation of the Mellin residue at gamma_1 could
raise or lower this estimate by a factor of a few.

If a rigorous computation gave A_log ~ 0.01, the CMB-S4 cumulative
SNR would reach ~5, making this a firm prediction testable in the
2030s.

### 11.3 More promising near-term tests

The BC framework's more actionable near-term predictions are:

1. **r = (3-8) x 10^{-3}**: detectable by LiteBIRD (launch ~2032,
   sigma(r) ~ 10^{-3}).

2. **n_s = gamma_9/gamma_10 = 0.96425**: already consistent with
   Planck, will be sharpened by CMB-S4 to sigma(n_s) ~ 0.002.

3. **alpha_s = -5.1 x 10^{-3}**: marginal for CMB-S4
   (sigma(alpha_s) ~ 3 x 10^{-3}).

The log-periodic modulation is the *most distinctive* prediction
(no other framework predicts oscillations at gamma_1) but also the
*hardest to detect*. The tensor-to-scalar ratio r is the most
actionable.

---

## 12. Code Reference

Script: `integers/paper12-cbb-system/code/log_periodic_cmb_prediction.py`
Results: `integers/paper12-cbb-system/code/log_periodic_cmb_results.json`

The script computes C_ell via Sachs-Wolfe approximation using
scipy.special.spherical_jn and scipy.integrate.quad, then compares
to a simplified Planck noise model. Runtime: ~3 minutes on a
standard laptop. All results are reproducible.

---

## 13. Status

**CLOSED.** The log-periodic CMB prediction has been quantified.
The answer is clear: A_log = 3 x 10^{-3} is undetectable in
Planck data (SNR = 0.44). The prediction stands as a future test
for CMB-S4, and serves as a consistency check against existing
oscillatory-feature searches.

The most actionable near-term prediction of the BC inflation model
remains the tensor-to-scalar ratio r ~ 5 x 10^{-3}, testable by
LiteBIRD.
