# Phase 1 — Assessment of the Current Appendix Y

Date: 2026-04-01

## What the rewrite does well

The current appendix is a major improvement over the original version. It:

1. **Correctly abandons dilaton-as-EDE** (mass mismatch by 10^27) and pivots
   to the mirror brane mechanism — a fundamentally different approach.

2. **Has a clear logical chain**: spin structure → Z2 → orbifold → hidden
   brane → dark radiation → H0 shift. The H0 prediction is traced back
   to the same topology that gives spin-statistics.

3. **Makes a specific, falsifiable prediction**: H0 = 69–70 km/s/Mpc,
   with ΔN_eff = 0.25–0.38 testable by CMB-S4.

4. **Is honest** about what it cannot do (the 3–4 km/s/Mpc Cepheid residual).

5. **Good structure**: the table comparing with TRGB, Cepheids, lensing
   is effective. The falsifiability section is clear.


## What needs updating — two critical problems

### Problem 1: ACT DR6 kills the current prediction

The paper uses the constraint N_eff = 2.81 ± 0.18 (earlier ACT+SPT+Planck).
**ACT DR6 (March 2025, arXiv:2503.14452) — the final ACT release — gives:**

    N_eff = 2.86 ± 0.13  (ACT alone)
    N_eff = 2.89 ± 0.11  (ACT + He + D abundances combined)

The framework predicts N_eff = 3.094 + 6.14 × ξ^4 (tower + mirror).
For ξ = 0.47 (the conservative BBN limit used in the paper):

    N_eff = 3.094 + 0.30 = 3.39

Tension with ACT DR6 alone: (3.39 − 2.86) / 0.13 = **4.1σ**
Tension with combined:      (3.39 − 2.89) / 0.11 = **4.5σ**

**The mirror sector at ξ = 0.45–0.50 is essentially ruled out by ACT DR6.**

At the 2σ boundary of ACT DR6 (N_eff < 3.12):
- Allowed mirror ΔN_eff < 3.12 − 3.094 = 0.026
- ξ < 0.255
- ΔH0 < 0.16 km/s/Mpc
- H0 < 67.9

This is devastating for the current prediction. The framework can barely
shift H0 at all under the tightest current constraint.


### Problem 2: BBN has also tightened

The paper uses Fields et al. 2020 (N_eff = 2.88 ± 0.27). A 2025 joint
BBN analysis gives:

    N_eff^BBN = 2.898 ± 0.141
    Upper limit: N_eff < 3.180 at 2σ

This means ΔN_eff < 0.136 at 2σ from BBN (vs. the paper's 0.37).
BBN alone now constrains ξ < 0.384 (vs. the paper's 0.50).


## The good news: the reframing helps

Pantos & Perivolaropoulos (arXiv:2601.00650, 2026) analyzed 88
sound-horizon-free H0 measurements and found:

    Distance Ladder:                    H0 = 72.73 ± 0.39
    Sound-horizon-free, non-DL methods: H0 = 69.37 ± 0.34
    Tension between these:              6.5σ

**The framework's prediction of H0 = 69–70 sits right on top of the
non-DL sound-horizon-free average (69.37 ± 0.34).**

This reframes the Hubble tension as "distance ladder vs. everything else"
— not "early vs. late universe." The framework would be predicting the
"everything else" value.

BUT: to actually reach 69.37, the framework needs ΔH0 ≈ 2 from the
Planck baseline, which requires ΔN_eff ≈ 0.3, which is in 4σ tension
with ACT DR6.


## Bottom line

The appendix makes the right physical argument (mirror brane dark radiation)
but the **quantitative prediction (H0 = 69–70) is now in tension with the
latest CMB data (ACT DR6)**. The allowed H0 shift is much smaller than
claimed. Either:

1. The prediction must be revised downward (to H0 ≈ 68–68.5)
2. A mechanism must be found that reduces the CMB sensitivity to the
   mirror radiation (without reducing its gravitational effect)
3. The paper must frame the prediction as a future test (ACT DR6 vs.
   CMB-S4), acknowledging the current tension

See `03-key-tension.md` for deeper analysis and `04-opportunities.md`
for creative ideas within the framework.
