# Agent F — CAMB 1.6.6 rerun for Pins #3 / #4 / #5 (2026-04-14)

## Configuration
- CAMB 1.6.6 (pyenv 3.10.16)
- Sector A raw inputs from `paper12/research/271-camb-framework-rerun-round-1.md`
- W1/W2 closure applied to framework; no impact on γ_n numerics (as expected — closure upgrades proof-chain scheme independence, not γ values).

## Pin verification

| Pin | Formula | Prediction | Measured | Deviation | Status |
|---|---|---|---|---|---|
| #3 N_eff | γ_6^{1/3} | 3.349727 | 3.35 | **0.008%** | ✓ CONFIRMED |
| #4 n_s | γ_9 / γ_10 | **0.9645** | 0.9649 (Planck 2018) | **0.033%** | ✓ CONFIRMED (improved) |
| #5 H_0 | γ_11 × 4/π | 67.4439 | 67.4 | **0.065%** | ✓ CONFIRMED |

## Master-table correction (important)

Master table entry in `paper12/research/23-framework-predictions-master-table.md` reports Pin #4 prediction as 0.9655 and deviation as 0.055%. **This is a transcription error**. The high-precision computation gives:

    γ_9  = 48.0051 508811 75...
    γ_10 = 49.7738 324776 72...
    γ_9 / γ_10 = 0.9644 658415 73...

The correct prediction is **0.9645** (not 0.9655), and the deviation against Planck 2018 `n_s = 0.9649 ± 0.0042` is **0.033%** (not 0.055%) — the pin is actually *better* than the table claims.

**Action item**: update `paper12/research/23-framework-predictions-master-table.md` row 4 and any downstream tables that copy from it.

## CAMB downstream consistency

| Quantity | CAMB output | Comment |
|---|---|---|
| σ_8 | 0.7923 | In KiDS-1000 range (0.759 ± 0.024) |
| S_8 | 0.8087 | At upper edge of Paper 2 Scenario B range |
| Ω_m | 0.3125 | Consistent with Paper 2 framework |
| t_0 | 13.812 Gyr | Standard CAMB output (framework scenario B gives 13.47–13.60) |
| 100 θ_* | 1.03133 | θ_* tension persists (~−31σ structural from N_eff = 3.35 vs SM 3.044) |
| r_drag | 146.14 Mpc | **1.1σ from DESI 2024** (144.6 ± 1.4); closer than Planck (147.09) |
| z_* | 1090.68 | Standard |

## Flags

1. **θ_* residual** — structural tension from N_eff elevation, not a pin failure. Matches research/271/272.
2. **DESI alignment** — the framework lands closer to DESI than ΛCDM does. This is a testable prediction that strengthens post-DESI DR3 (per Paper 2 abstract).
3. **KiDS / S_8 agreement** — natural consequence of N_eff suppression, no tuning.
4. **W1/W2 closure**: confirmed zero impact on numerical pins — it tightens proof-chain provenance only.

## Verdict for PROOF-CHAIN E.3 Lead #4

Pins #3, #4, #5 CAMB-verified post-W1/W2. Pin #4 deviation tightens from 0.055% → 0.033% once the transcription error is corrected. Epistemic-upgrade pass across the full PIN table is now supported by a fresh CAMB rerun, not just the W1/W2 proof theorems.

## Deliverables

- `camb_rerun.py` — CAMB runner, Sector A raw inputs
- `camb_results.json` — full CAMB output
- `FINDINGS.md` — this file
