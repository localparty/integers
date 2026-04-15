# Final Numerical Results: The Lüscher Test

All numbers computed with the validated integral formula for the massive
Casimir energy. Massless limit verified to 0.2% accuracy.


---

## I. The Five Scenarios at the Sweet Spot (R√σ = 0.7, R ≈ 0.31 fm)

| Scenario | Modes | Masses (×√σ) | c_eff | δc | % effect |
|:---------|:-----:|:-------------|:-----:|:--:|:--------:|
| Nambu-Goto | 0 | — | 2.000 | 0.000 | 0% |
| Single axion (DGM) | 1 | [1.85] | 2.107 | 0.107 | 5.3% |
| **CP² with mass hierarchy** | **4** | **[1.85, 2.3, 2.3, 2.8]** | **2.262** | **0.262** | **13.1%** |
| CP² all degenerate | 4 | [1.85, 1.85, 1.85, 1.85] | 2.427 | 0.427 | 21.4% |
| 1 light + 3 very heavy | 4 | [1.85, 4.0, 4.0, 5.0] | 2.123 | 0.123 | 6.1% |

**The realistic scenario** is "4 hierarchy" (bold): the axion at 1.85√σ
(measured), the scalars at ~2.3√σ (estimated from 1/N), the
pseudo-partner at ~2.8√σ. This gives **δc = 0.26, a 13% effect** —
between the single-axion (5%) and all-degenerate (21%) predictions.


---

## II. Full Table: c_eff(R) for All Scenarios

| R√σ | R (fm) | NG | 1 axion | 4 hierarchy | 4 degenerate |
|:---:|:------:|:--:|:-------:|:-----------:|:------------:|
| 0.3 | 0.13 | 2.000 | 2.382 | 3.223 | 3.527 |
| 0.5 | 0.22 | 2.000 | 2.203 | 2.567 | 2.811 |
| 0.7 | 0.31 | 2.000 | 2.107 | 2.262 | 2.427 |
| 1.0 | 0.45 | 2.000 | 2.040 | 2.083 | 2.160 |
| 1.5 | 0.67 | 2.000 | 2.007 | 2.012 | 2.030 |
| 2.0 | 0.90 | 2.000 | 2.001 | 2.002 | 2.005 |
| 3.0 | 1.34 | 2.000 | 2.000 | 2.000 | 2.000 |


---

## III. SU(N) Scaling (all modes at m = 1.85√σ)

| N | Gauge group | n_modes = 2(N-1) | c_eff(0.7) | δc | δc ratio |
|:-:|:-----------|:----------------:|:----------:|:--:|:--------:|
| 2 | SU(2) | 2 | 2.214 | 0.214 | 0.50 |
| 3 | SU(3) | 4 | 2.427 | 0.427 | 1.00 |
| 4 | SU(4) | 6 | 2.641 | 0.641 | 1.50 |
| 5 | SU(5) | 8 | 2.854 | 0.854 | 2.00 |
| 6 | SU(6) | 10 | 3.068 | 1.068 | 2.50 |

**δc grows linearly with (N-1).** The single-axion model predicts
δc = 0.107 (constant) for all N.

**At SU(6):** δc = 1.068 (53% effect) vs 0.107 (5.3%) — a factor of
10× difference. This is unmistakable.


---

## IV. What Distinguishes Each Scenario

### NG vs any massive modes:
The NG prediction is c_eff = 2.000 flat. Any deviation above 2.0 at
intermediate R signals massive worldsheet modes. **The lattice already
sees this** (Caselle et al., Dubovsky-Gorbenko).

### 1 mode vs 4 modes:
At R√σ = 0.7:
- 1 axion: δc = 0.107 (5.3%)
- 4 CP² (hierarchy): δc = 0.262 (13.1%)
- Ratio: **2.4×**

This is distinguishable at ~10% precision on c_eff. Current lattice
precision on the string spectrum is ~2-5% for the ground state.

### The SU(N) scaling:
Our prediction: δc ∝ (N-1) (linear).
Single-axion: δc = constant.
**This is the cleanest test** — it's a counting argument, not a
precision measurement.


---

## V. Precision Requirements for Each Test

| Test | Quantity | Our prediction | Competing prediction | Required precision |
|:-----|:---------|:--------------|:--------------------|:-------------------|
| c_eff at R√σ = 0.7 | δc | 0.26 | 0.11 (1 axion) | ~10% on c_eff |
| c_eff at R√σ = 0.5 | δc | 0.57 | 0.20 (1 axion) | ~15% on c_eff |
| SU(5) vs SU(3) δc ratio | δc(5)/δc(3) | 2.0 | 1.0 | ~30% on ratio |
| SU(6) vs SU(3) δc ratio | δc(6)/δc(3) | 2.5 | 1.0 | ~40% on ratio |

**The SU(N) ratio test needs only 30-40% precision** — the easiest
measurement. The δc values themselves need ~10-15% precision — harder
but feasible.


---

## VI. The Bottom Line

The computation reveals a clear, testable prediction:

1. **A massive mode on the worldsheet EXISTS.** (Already confirmed:
   the axion at $m_a = 1.85\sqrt{\sigma}$.)

2. **Our framework predicts 4 modes, not 1.** The extra 3 modes have
   specific quantum numbers ($0^{+-}$, $0^{++}$, $0^{--}$) and are
   ~30-60% heavier than the axion.

3. **The most decisive test is SU(N) scaling.** The mode count should
   grow as $2(N-1)$, giving $\delta c$ linear in $N$. At SU(6), the
   signal is 10× larger than the single-axion prediction. This can be
   tested with existing lattice technology.

4. **At R√σ = 0.7 (R ≈ 0.3 fm):** our realistic prediction is
   $c_{\text{eff}} = 2.26$ ($\delta c = 0.26$, 13% effect). The
   single-axion prediction is $c_{\text{eff}} = 2.11$ ($\delta c = 0.11$,
   5% effect). Distinguishable at ~10% precision.
