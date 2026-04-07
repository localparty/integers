# Appendix B — The Expansion History H(z) and DESI Predictions

> The framework predicts `w₀ = −1`, `w_a = 0` (Casimir potential exact;
> Paper 6 §2; Appendix F). The deviations from `ΛCDM` in `H(z)` come
> from elevated `N_eff` and lower `Ω_m`, not from evolving `w`. The
> `H(z) × r_d` predictions in this appendix are computed with `w = −1`
> and reflect the current framework prediction. DESI DR3 (2027) will
> test these at 0.5% precision per bin.

---

## B.1 The Modified Hubble Parameter

The framework's `H(z)` differs from `ΛCDM` through two physical channels:

**1. Higher `H₀` (dominant at `z ~ 0`):**

    H(z=0) = 69.5 vs 67.4 → ratio 1.031

The `H₀` uplift comes from elevated `N_eff` via the formula
`H₀ ≈ 67.4 + 6.3 × ΔN_eff` (Paper 1, App. Y). This is the dominant
effect at low z.

**2. Convergence at high z (radiation domination):**

At `z > 2`, `H(z) → H₀ × √(Ω_r) × (1+z)²`, and since
`Ω_r = ρ_r/ρ_crit ∝ 1/H₀²`, the `H₀` dependence cancels. The
physical radiation density (fixed by `T_CMB = 2.725` K) is
`H₀`-independent. This forces `H(z)` to converge to `ΛCDM` at
`z > 2`, so the signature of elevated `N_eff` is a peak in the
`H(z)/H_ΛCDM(z)` ratio at `z ~ 0.3–0.7`, followed by convergence.

The dark energy is `w = −1` (frozen dilaton); there is no evolving-`w`
contribution to `H(z)` at any redshift.

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

With `w = −1`, the `H(z)/H_ΛCDM(z)` ratio has the following shape:

    z ~ 0: ratio = 1.032 (from H₀ shift alone)
    z ~ 0.5: ratio = 1.038 (peak — from elevated N_eff, lower Ω_m)
    z ~ 1.5: ratio = 1.000 (crossing point)
    z > 2: ratio → 0.995 (small residual from elevated N_eff)

The peak above 1.032 at `z ~ 0.5` is driven by elevated `N_eff` and
lower `Ω_m` (not by evolving dark energy). No `ΛCDM` model can produce
this specific combination: a model with only higher `H₀` would give a
monotonically decreasing ratio; the peak is the imprint of the mirror
sector's effect on the energy budget. The shape at `w = −1` is
qualitatively the same as previously described but with a slightly
lower peak (1.038 vs 1.040 for the former `w₀ = −0.85` scenario)
because the evolving-`w` channel is absent.

---

## B.4 DESI BAO Predictions

DESI measures the BAO angular scale `θ_BAO(z) = r_d / D_A(z)`
and the radial BAO scale `H(z) × r_d` at each redshift bin.

The framework predicts `r_d = 146.2` Mpc (vs Planck's 147.1 Mpc),
a 0.6% reduction from the elevated `N_eff`.

**Table B4: Predicted H(z) × r_d values for DESI DR3 (w = −1)**

| Redshift | `H_5D` × `r_d` | `H_ΛCDM` × `r_d` | Deviation | DESI DR3 precision | Detection |
|----------|-----------|--------------|------------|-------------------|-----------|
| z = 0.51 | 14,050 km/s | 13,610 km/s | +3.2% | ~0.5% | ~6σ |
| z = 0.71 | 16,290 km/s | 15,760 km/s | +3.4% | ~0.5% | ~7σ |
| z = 0.93 | 19,540 km/s | 18,910 km/s | +3.3% | ~0.5% | ~7σ |
| z = 1.32 | 26,530 km/s | 25,950 km/s | +2.2% | ~0.5% | ~4σ |
| z = 2.33 | 56,110 km/s | 56,440 km/s | −0.6% | ~0.5% | ~1σ |

The framework predicts `H(z) × r_d` systematically 3–3.4% above `ΛCDM`
at `z = 0.5–0.9`, driven by the higher `H₀` from elevated `N_eff`. The
deviation falls off at higher `z` as the radiation-dominated regime is
approached. Note that the excess is now driven by the `N_eff` effect
rather than by evolving `w`; the 3.2–3.4% signal at `z ~ 0.5–0.7` is
nearly identical in magnitude (though slightly smaller than the
superseded thawing-dilaton prediction).

DESI DR2 measures these to ~1% precision. DESI DR3 (full 5-year dataset,
expected 2027) will measure them to ~0.5% precision — sufficient to
detect the 3% deviation at `6–7σ` in individual bins. If DESI DR3
measures `H(z) × r_d` consistent with `ΛCDM` at these redshifts, the
elevated-`N_eff` prediction is excluded (correlated with the CMB-S4 test).

**This is the most decisive near-term test of the framework.**

---

## B.5 Comparison with Current DESI Data

DESI DR2 (arXiv:2503.14738) reports `H(z) × r_d` values consistent
with `ΛCDM` at `z > 0.5`, but with `2–4σ` hints of evolving dark energy
(`w₀ ≈ −0.75`, `w_a ≈ −0.75`). The framework predicts `w₀ = −1`, `w_a = 0`
(Casimir potential exact; Paper 6 §2; Appendix F) — in potential tension
with DESI DR2. The `H(z) × r_d` excess predicted by the framework at
`z ~ 0.5–0.7` has a different origin than the DESI DR2 hints (it is from
elevated `N_eff`, not from evolving `w`), so the two are physically
distinguishable by their redshift dependence: the framework's excess
peaks at `z ~ 0.7` while evolving-`w` models produce a different
`H(z)` shape at `z > 1`.

If DESI DR3 confirms `w ≠ −1` at `> 5σ`, non-perturbative modifications
to the dilaton potential are required. The current DESI DR2 data neither
confirms nor excludes the framework. DESI DR3 will be decisive.

---

## B.6 References

- DESI Collaboration. "DESI DR2 Results II." arXiv:2503.14738 (2025).
- Eisenstein, D. J. et al. "BAO in the galaxy correlation function."
  *Astrophys. J.* **633**, 560 (2005).
- Bedroya, A., Obied, G., Vafa, C. & Wu, H. "Evolving Dark Sector
  and the Dark Dimension Scenario." arXiv:2507.03090 (2025).
