# Appendix B — The Expansion History H(z) and DESI Predictions

> **⚠ Revised:** With the perturbative Casimir potential exact
> (`w₀ = −1`, `w_a = 0`; dilaton frozen; Paper 6 §2), the H(z) peak
> from evolving `w` is absent. The remaining deviations from `ΛCDM`
> come from elevated `N_eff` and lower `Ω_m`, not from evolving `w`.
> The fingerprint described below assumed the earlier `w₀ = −0.85`
> prediction and should be recomputed with `w = −1`.

---

## B.1 The Modified Hubble Parameter

The framework's `H(z)` differs from `ΛCDM` through three channels:

**1. Higher `H₀` (dominant at `z ~ 0`):**
    H(z=0) = 69.5 vs 67.4 → ratio 1.031

**2. Evolving w(z) (dominant at z ~ 0.3–0.7):**
The thawing dilaton (Appendix F) gives less dark energy at
intermediate z than a cosmological constant. This RAISES H(z)
relative to what higher `H₀` alone would give, because more matter
is needed to close the flat universe.

**3. Convergence at high z (radiation domination):**
At z > 2, H(z) → `H₀` × √(`Ω_r`) × (1+z)², and since `Ω_r` = `ρ_r/ρ_crit`
∝ `1/H₀²`, the `H₀` dependence cancels. The physical radiation density
(fixed by `T_CMB` = 2.725 K) is `H₀-independent`.

---

## B.2 CAMB-Computed H(z) Values

| Redshift | `H_5D` (km/s/Mpc) | `H_LCDM` (km/s/Mpc) | Ratio | DESI precision |
|----------|-----------------|-------------------|-------|----------------|
| 0.0 | 69.50 | 67.36 | 1.032 | — |
| 0.3 | 82.1 | 79.1 | 1.038 | ~1% (DR2) |
| 0.5 | 95.6 | 91.9 | 1.040 | ~1% (DR2) |
| 0.7 | 111.5 | 107.4 | 1.038 | ~1% (DR2) |
| 1.0 | 140.3 | 136.6 | 1.027 | ~2% (DR2) |
| 1.5 | 196.2 | 195.4 | 1.004 | ~2% (DR2) |
| 2.0 | 262.0 | 263.3 | 0.995 | ~2% (DR2) |
| 2.5 | 340.8 | 342.5 | 0.995 | ~3% (DR2) |

**The maximum deviation (4.0%) occurs at z ~ 0.5**, right in DESI's
highest-precision measurement bin. The crossing point (`H_5D` = `H_LCDM`)
occurs at z ~ 1.5.

---

## B.3 The Characteristic Shape

The H(z)/`H_LCDM`(z) ratio has a specific shape:

    z ~ 0: ratio = 1.032 (from H₀ shift alone)
    z ~ 0.5: ratio = 1.040 (peak — evolving DE adds)
    z ~ 1.5: ratio = 1.000 (crossing point)
    z > 2: ratio → 1.005 (small residual from N_eff)

This shape is a SIGNATURE of the specific combination of:
- Higher `H₀` (sets the z=0 value)
- Thawing dark energy (creates the peak above z=0 value)
- Same physical radiation density (forces convergence at high z)

No `ΛCDM` model can produce this shape. A model with only higher `H₀`
would give a monotonically decreasing ratio. The peak above 1.032
at z ~ 0.5 is the imprint of the thawing dilaton.

---

## B.4 DESI BAO Predictions

DESI measures the BAO angular scale `θ_BAO(z`) = `r_d` / `D_A`(z)
and the radial BAO scale H(z) × `r_d` at each redshift bin.

The framework predicts `r_d` = 146.2 Mpc (vs Planck's 147.1 Mpc),
a 0.6% reduction from the elevated `N_eff`.

**Predicted H(z) × `r_d` values:**

| Redshift | `H_5D` × `r_d` | `H_LCDM` × `r_d` | Difference |
|----------|-----------|--------------|------------|
| z = 0.51 | 14,050 km/s | 13,610 km/s | +3.2% |
| z = 0.71 | 16,290 km/s | 15,760 km/s | +3.4% |
| z = 0.93 | 19,540 km/s | 18,910 km/s | +3.3% |
| z = 1.32 | 26,530 km/s | 25,950 km/s | +2.2% |
| z = 2.33 | 56,110 km/s | 56,440 km/s | −0.6% |

The framework predicts H(z) × `r_d` systematically 2–3% above `ΛCDM`
at z < 1.5, falling slightly below at z > 2. DESI DR2 measures
these to ~1% precision. DESI DR3 (full 5-year dataset, expected
2027) will measure them to ~0.5% precision — sufficient to detect
a 3% deviation at `6σ`.

**This is the most decisive near-term test of the framework.**

---

## B.5 Comparison with Current DESI Data

DESI DR2 (arXiv:2503.14738) reports H(z) × `r_d` values consistent
with `ΛCDM` at z > 0.5, but with `2–4σ` hints of evolving dark energy.
The framework's prediction of H(z) peaking at z ~ 0.5 and the
thawing w(z) trajectory are in the same direction as the DESI hints
but milder in amplitude (DESI's best-fit `w₀` ≈ −0.75, `w_a` ≈ −0.75).
**⚠ Revised:** The framework now predicts `w₀ = −1`, `w_a = 0` (Casimir
potential exact; Paper 6 §2). If DESI DR3 confirms `w ≠ −1`,
non-perturbative modifications to the dilaton potential are required.

The current DESI DR2 data neither confirms nor excludes the
framework. DESI DR3 will be decisive.

---

## B.6 References

- DESI Collaboration. "DESI DR2 Results II." arXiv:2503.14738 (2025).
- Eisenstein, D. J. et al. "BAO in the galaxy correlation function."
  *Astrophys. J.* **633**, 560 (2005).
- Bedroya, A., Obied, G., Vafa, C. & Wu, H. "Evolving Dark Sector
  and the Dark Dimension Scenario." arXiv:2507.03090 (2025).
