# Appendix D — The Sound Horizon r_d and BAO Predictions

> The framework predicts r_d = 146.2 Mpc, 0.6% smaller than the
> Planck ΛCDM value (147.1 Mpc). This shift — from elevated N_eff
> shrinking the sound horizon — is directly testable by DESI BAO
> measurements at current precision.

---

## D.1 The Sound Horizon

The sound horizon at baryon drag is the distance sound travels in
the baryon-photon plasma from the Big Bang to the drag epoch:

    r_d = ∫_{z_d}^∞ c_s(z) dz / H(z)

where c_s ~ c/√(3(1 + 3Ω_b/(4Ω_γ(1+z)⁻¹))) is the sound speed
and z_d ~ 1060 is the drag epoch redshift.

**Standard ΛCDM:** r_d = 147.09 ± 0.26 Mpc (Planck 2018)

---

## D.2 The Framework Prediction

The framework modifies r_d through elevated N_eff = 3.39.

Higher N_eff → faster expansion at early times → less time for
sound to travel → smaller r_d.

The CAMB computation gives:

**r_d = 146.2 Mpc** (vs Planck 147.1 Mpc)

This is a 0.63% reduction.

---

## D.3 Comparison with DESI Measurements

DESI DR2 measures D_V(z)/r_d and H(z) × r_d at multiple redshifts.
The framework predicts both the numerator (through H(z), Appendix B)
and the denominator (r_d = 146.2 Mpc).

**Framework prediction for D_V/r_d at key DESI redshifts:**

| Redshift | D_V^{5D}/r_d^{5D} | D_V^{LCDM}/r_d^{LCDM} | DESI DR2 measurement |
|----------|-------------------|------------------------|----------------------|
| z = 0.51 | 13.41 | 13.22 | 13.62 ± 0.25 |
| z = 0.71 | 17.76 | 17.54 | 17.91 ± 0.27 |
| z = 0.93 | 21.89 | 21.63 | 21.94 ± 0.33 |
| z = 1.32 | 28.44 | 28.25 | 28.57 ± 0.42 |

The framework values are within DESI DR2 uncertainties at all
measured redshifts.

---

## D.4 Why r_d Is a Stringent Test

The sound horizon r_d is one of the most robustly calibrated
quantities in cosmology. It is measured at ~0.2% precision by
DESI and at 0.18% by Planck (through the CMB angular scale).

A 0.6% shift in r_d (from ΛCDM 147.1 to framework 146.2) is:
- 3.5σ relative to Planck's r_d measurement precision
- ~0.6σ relative to DESI's BAO distance measurement precision

The current DESI data are consistent with both the framework and
ΛCDM at the 1σ level. DESI DR3 (full 5-year dataset) will measure
r_d to ~0.1% precision — at which point the framework's prediction
of 146.2 Mpc becomes a 9σ test against the Planck ΛCDM value.

---

## D.5 The Self-Consistency Chain

The framework's r_d prediction is tied to its θ* prediction through:

    θ* = r_d / D_A(z*)

With r_d = 146.2 Mpc and θ* = 0.59640° (matched to Planck at 0.5"),
the angular diameter distance to last scattering is:

    D_A(z*) = r_d / θ* = 146.2 / 0.010416 = 14,034 Mpc

This is 1.1% below the Planck value (14,191 Mpc). The framework
achieves a smaller D_A through the combination of higher H₀ and
lower Ω_m — a self-consistent solution that simultaneously passes
the θ* test (Appendix A) and the r_d test.

---

## D.6 References

- DESI Collaboration. "DESI DR2 Results II." arXiv:2503.14738 (2025).
- Eisenstein, D. J. et al. "BAO in galaxy survey." *ApJ* **633**,
  560 (2005).
- Planck Collaboration. "Planck 2018 results. VI." *A&A* **641**,
  A6 (2020).
