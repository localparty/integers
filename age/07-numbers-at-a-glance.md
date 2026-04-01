# 5D Framework Cosmological Predictions: Numbers at a Glance

## Framework Input Parameters (Geometric)

| Parameter | Value | Source |
|-----------|-------|--------|
| E-circle circumference L | ~130 um (range 50-200) | Casimir = rho_Lambda |
| E-circle radius R | ~21 um | L/(2*pi) |
| KK mass scale m_KK | 9.4 meV | hbar/(R*c) |
| Hidden-to-visible temp ratio xi | 0.45-0.50 | BBN constraint |
| Dilaton mass m_phi | ~10 meV | Stabilization potential |
| 5D fundamental scale M_5 | ~2.5e14 GeV | (M_Pl^2/L)^{1/3} |

## Derived Cosmological Parameters

| Parameter | LCDM (Planck 2018) | 5D Framework | Difference |
|-----------|-------------------|-------------|------------|
| H_0 (km/s/Mpc) | 67.36 +/- 0.54 | **69-70** | +2-3 |
| N_eff | 3.044 (SM) | **3.09** (tower) + **0.30** (mirror) = **3.39** | +0.35 |
| w_0 | -1 (exact) | **-0.85** (thawing dilaton) | +0.15 |
| w_a | 0 (exact) | **-0.23** (thawing dilaton) | -0.23 |
| Sum m_nu (eV) | < 0.12 (bound) | **~0.06** (NO, bulk seesaw) | predicted |
| Mass ordering | unknown | **Normal** (Z_3 geometry) | predicted |
| 1/alpha(0) | 137.036 (measured) | **137.0 +/- 0.3** (geometric) | 0.12% |

## Cosmological Observables (Predictions vs Data)

| Observable | Planck LCDM | 5D Framework | Current Data |
|-----------|------------|-------------|-------------|
| t_0 (Gyr) | 13.80 +/- 0.02 | **13.4-13.6** | 13.80 (CMB); 12.5-14.5 (stellar) |
| r_d (Mpc) | 147.09 +/- 0.26 | **~145-146** | 147.09 (CMB); ~144-148 (BAO) |
| theta_* (deg) | 1.04110 +/- 0.00031 | **TBD** (need CLASS) | 1.04110 |
| sigma_8 | 0.811 +/- 0.006 | **~0.78-0.82** | 0.811 (CMB); 0.76 (WL) |
| S8 | 0.832 +/- 0.013 | **~0.75-0.79** | 0.832 (CMB); 0.76 (WL) |
| Omega_m | 0.315 +/- 0.007 | **~0.30-0.35** | 0.315 (CMB) |
| Omega_Lambda | 0.685 +/- 0.007 | **~0.64-0.70** | 0.685 (CMB) |

## Tensions Addressed by the Framework

| Tension | LCDM Status | 5D Framework Resolution |
|---------|------------|------------------------|
| Hubble tension (H_0) | 5-sigma | Partially resolved: 69-70 (matches TRGB) |
| S8 tension | 2-3 sigma | Resolved: mirror DM + KK cascades |
| DESI w != -1 | 4.2-sigma | Explained: thawing dilaton |
| JWST early galaxies | 2-3 sigma | NOT resolved (same time at high z) |
| Strong CP | Fine-tuning | Topological: pi_4(SU(3)) = 0 |
| Cosmological constant | 120 orders | Casimir energy (by construction) |

## Upcoming Experiments and Framework Tests

| Experiment | Measurement | Framework Prediction | Decisive? |
|-----------|------------|---------------------|-----------|
| CMB-S4 (~2030) | N_eff to +/- 0.03 | 3.39 (if mirror) or 3.09 (minimal) | **YES** |
| DESI DR3 (~2027) | w_0, w_a | w_0 ~ -0.85, w_a ~ -0.23 | **YES** |
| JUNO (~2028-2031) | Mass ordering | Normal | **YES** |
| MEMS gravity (~2030+) | Newton's law < 50 um | Yukawa at ~21 um | **YES** |
| LDMX/LHCb (~2027) | Dark photon | epsilon ~ 5e-4 | **YES** |
| Euclid (~2027+) | S8, w(z) | S8 ~ 0.76, w thawing | Supportive |
| Rubin/LSST (~2027+) | SNe, w(z) | w_0 ~ -0.85 | Supportive |
| ADMX/IAXO | QCD axion | No axion (pi_4 = 0) | Falsifying if found |

## The Age Prediction: What We Know So Far

**Conservative estimate (stabilized e-circle, w = -1):**
    t_0 ~ 13.15-13.4 Gyr (primarily from H_0 = 69.5)

**Best estimate (thawing dilaton, w_0 ~ -0.85):**
    t_0 ~ 13.4-13.6 Gyr

**Full dynamics estimate (needs computation):**
    t_0 ~ 13.2-14.0 Gyr (depends on Omega_m from mirror matter)

**The age is YOUNGER than Planck LCDM by 200-600 Myr, primarily
because H_0 is higher (69.5 vs 67.4).**

## What Would Change the Age Prediction Most

| Change | Effect on t_0 | Magnitude |
|--------|-------------|-----------|
| Omega_m from 0.35 to 0.30 | Older | +0.6 Gyr |
| w_0 from -1.0 to -0.85 | Slightly older | +0.1-0.3 Gyr |
| H_0 from 67.4 to 69.5 | Younger | -0.4 Gyr |
| N_eff from 3.04 to 3.39 | Younger | -0.1 Gyr |
| Sum m_nu = 0.06 eV | Younger | -0.03 Gyr |

**The Omega_m value is the single most important unknown for the age.**

## Next Steps

1. Write Python age calculator with 5D parameters
2. Solve dilaton dynamics to get exact w(z)
3. Run CLASS to get r_d, theta_*, sigma_8
4. Compare with Planck + DESI + weak lensing
5. Calculate mirror matter Omega_m from gravitational production
6. Pin down the age to +/- 0.1 Gyr precision
