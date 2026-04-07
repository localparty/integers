# Update and Run Cosmological Computations — QG5D Framework

This prompt updates the numerical computation scripts at
`/Users/gsix/quantum-geometry-in-5d/etc/age/` to match the latest parameter
values from the QG5D paper series, then runs the calculations and regenerates
all plots.

Run this whenever the papers have been revised (e.g. after a full review cycle).

---

## Step 1 — Extract current parameter values from the papers

Read the following source files and extract the current definitive values for
each parameter listed below. Do not use memory or prior knowledge — read the
files now.

**ξ (mirror sector temperature ratio):**
- Read `paper2/02-sections-2-to-7.md` §2.2 ("The status of ξ")
- Read `paper2/appendices/09-appendix-e-mirror-baryogenesis.md` §E.4
- Extract: the determined value of ξ, the ΔN_eff formula, the N_eff^{recomb} range, the N_eff^{BBN} range

**w₀, wa (dark energy equation of state):**
- Read `paper6/appendix-A-dilaton-freezing.md`
- Read `paper6/00-abstract.md`
- Extract: w₀, wa, and the ΔR/R₀ per Hubble time (dilaton slow-roll)

**ns, r (inflationary spectral index and tensor ratio):**
- Read `paper7/05-inflaton.md`
- Read `paper7/00-abstract.md`
- Extract: n_s, r, and H_inf

**T_reh (reheating temperature):**
- Read `paper6/04-reheating.md` §4.0
- Extract: T_reh value and uncertainty

**N_eff:**
- Read `paper2/02-sections-2-to-7.md`
- Extract: N_eff^{recomb} (CMB epoch), N_eff^{BBN}; note these differ due to
  mirror e± annihilation after BBN

**Ω_DM/Ω_b scaling law:**
- Read `paper2/appendices/09-appendix-e-mirror-baryogenesis.md`
- Extract: the leptogenesis formula and the washout factor K

**Casimir potential / dark energy:**
- Read `paper6/02-dilaton-potential.md` §2.1
- Read `paper4/07-predictions.md` (the §7.21 dark energy section)
- Extract: V(R) = +c/R⁴ sign, ε_eff value, V(R₀) = ρ_Λ consistency

**KK / GUT scales:**
- Read `paper4/07-predictions.md`
- Extract: M_KK, sin²θ_W, m_H range, τ_p range

---

## Step 2 — Identify what has changed

Compare extracted values against what is currently in the scripts:

- `compute_age.py` — check the `scenarios` dict: H0, nnu, w, wa, ns values
- `compute_mirror_matter.py` — check the final CAMB run parameters
- `neff_extended_analysis.py` — check any hardcoded w₀, wa, N_eff values
- `plot_results.py` — check any hardcoded w₀, wa, ns values in CAMB calls

List every parameter that differs between current scripts and current paper
values before making any changes.

---

## Step 3 — Update the scripts

Edit the following files at `/Users/gsix/quantum-geometry-in-5d/etc/age/`:

### `compute_age.py`

Ensure the scenario set reflects the current framework state:

1. **`Planck_LCDM`** — keep as baseline; do not change.

2. **`5D_primary`** — the main framework prediction. Parameters derived from
   current ξ (Paper 2 determined value):
   - `nnu` = 3.044 + 0.05 + 6.14 × ξ⁴   (KK tower + mirror sector)
   - `omch2` = ombh2 / ξ²                  (1/ξ² scaling law)
   - `H0` = 67.4 + 6.3 × ΔN_eff           (N_eff→H₀ calibration)
   - `w` = current w₀ from Paper 6
   - `wa` = current wa from Paper 6
   - `ns` = current ns from Paper 7

3. **`5D_xi_low`** — lower end of ξ range (ξ = 0.432, the pure Ω_DM/Ω_b = 5.36 value):
   - Derive nnu, omch2, H0 from ξ = 0.432
   - Same w, wa, ns as primary

4. **`5D_xi_high`** — upper end of ξ range:
   - Use the theta*-matched omch2 ~ 0.117 (from Paper 2 Scenario A)
   - Same w, wa, ns as primary

5. **`5D_minimal`** — tower only (no mirror sector): nnu = 3.09, w=-1, wa=0.
   Keep as a diagnostic.

6. Remove or mark `[SUPERSEDED]` any scenario that uses the old thawing
   dilaton values (w₀ = −0.85, wa = −0.23).

Update `pars.InitPower.set_params(As=2.1e-9, ns=...)` to use the current ns
from Paper 7 in ALL scenario runs (inside `run_scenario()`).

### `compute_mirror_matter.py`

Update `run_final_camb()`:
- `w` and `wa` to current Paper 6 values
- `ns` to current Paper 7 value
- Update any printed summary blocks to show current w₀, wa

### `neff_extended_analysis.py`

Update any hardcoded w₀, wa in docstrings and comments to current values.
The core Boltzmann calculation does not depend on w — only the CAMB degeneracy
comparison uses w, so update those parameter sets.

### `plot_results.py`

- Update `ns` in any CAMB calls within `plot_Hz()` to current Paper 7 value
- In `plot_wz()`: add the current framework w(z) curve with correct label;
  mark any superseded curves as "[superseded]" with dashed gray style
- Keep the Planck LCDM and observational reference curves unchanged

Do not touch `.png`, `.json`, or `.venv` files in this step.

---

## Step 4 — Run the calculations

Run the scripts in this order using the `.venv` Python at
`/Users/gsix/quantum-geometry-in-5d/etc/age/.venv/bin/python`:

```bash
cd /Users/gsix/quantum-geometry-in-5d/etc/age

# Main CAMB computation (writes results.json)
.venv/bin/python compute_age.py

# Mirror matter relic abundance
.venv/bin/python compute_mirror_matter.py

# N_eff extended analysis (writes neff_analysis_results.json)
.venv/bin/python neff_extended_analysis.py

# Regenerate all plots (reads results.json, writes *.png)
.venv/bin/python plot_results.py
```

Capture stdout from each script. If any script fails, read the traceback,
diagnose the cause (likely a changed parameter name or a scenario key that no
longer exists in results.json), fix it, and re-run.

---

## Step 5 — Report the key numbers

After all scripts complete successfully, report:

| Observable | 5D Primary | 5D ξ-low | 5D ξ-high | Planck LCDM | Data |
|-----------|-----------|---------|---------|------------|------|
| Age (Gyr) | | | | 13.797 | |
| r_d (Mpc) | | | | 147.10 | |
| theta_* (deg) | | | | 0.59655 | |
| sigma_8 | | | | 0.811 | |
| S8 | | | | 0.832 | 0.776 (DES) |
| Omega_m | | | | 0.315 | |
| H_0 | | | | 67.4 | 69.8 (TRGB) |
| N_eff | | | | 3.044 | 2.86 (ACT) |
| t(z=14) Myr | | | | 295 | JWST |

Fill in all values from `results.json`. Flag any observable that is more than
2σ from its observational constraint.

---

## Notes

- The `.venv` has CAMB 1.6.6, numpy, matplotlib, sympy installed.
- CAMB accuracy is set to `AccuracyBoost=1.5` — this is sufficient.
- The computation scripts are at `/Users/gsix/quantum-geometry-in-5d/etc/age/`
  (note: NOT the `-latex` directory — this is the original repo).
- The paper source files are at `/Users/gsix/quantum-geometry-in-5d-latex/`.
- Do not modify paper source files in this workflow — only read them for
  parameter extraction.
- If `plot_results.py` fails because a scenario key is missing from
  `results.json`, either add the scenario to `compute_age.py` or update the
  scenario list in `plot_results.py` to match what was actually computed.
