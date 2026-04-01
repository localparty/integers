# Phase 5 — Recommended Strategy for the Rewrite

## The core problem

The current appendix predicts H₀ = 69–70 based on mirror dark radiation
with ΔN_eff = 0.25–0.38. ACT DR6 (March 2025, final release) constrains
N_eff = 2.86 ± 0.13, putting the framework's predicted N_eff ≈ 3.35–3.48
in 4–5σ tension with the latest CMB data.

The prediction H₀ = 69–70 is no longer compatible with the current
N_eff constraint at the 2σ level.


## The proposed approach: "geometric prediction, not tension resolution"

Instead of claiming to resolve the Hubble tension (which would require
~5.6 km/s/Mpc shift), the paper should:

1. **Predict H₀ from the framework's geometry** (the mirror brane is
   a consequence of spin-statistics, not an ad hoc addition)
2. **Present the prediction in tiers** based on the constraining dataset
3. **Position the prediction relative to the observational landscape**
   using the Pantos & Perivolaropoulos reframing


## The two-tier prediction

### Tier 1: Current CMB-constrained (ACT DR6)

Using ACT DR6 alone: N_eff = 2.86 ± 0.13

At the 2σ boundary (N_eff < 3.12):
- ΔN_eff^mirror < 0.03 → ξ < 0.26 → ΔH₀ < 0.2
- **H₀ < 67.9** (indistinguishable from ΛCDM)

At the 3σ boundary (N_eff < 3.25):
- ΔN_eff^mirror < 0.16 → ξ < 0.40 → ΔH₀ < 1.0
- **H₀ < 68.7**

**Assessment:** With current CMB data, the mirror sector's contribution
is modest. The framework predicts H₀ ≈ 68.0–68.7 at the 2–3σ level.
This is above ΛCDM (67.4) and consistent with ACT DR6 + DESI values
(68.2–68.4), but not a dramatic shift.


### Tier 2: BBN-constrained (agnostic to CMB N_eff)

Using updated BBN: N_eff < 3.18 at 2σ (2025 analysis)

- ΔN_eff^mirror < 0.09 → ξ < 0.35 → ΔH₀ < 0.6
- **H₀ ≈ 68.0–68.3**

Or using the older BBN (Fields et al. 2020): N_eff < 3.42 at 2σ

- ΔN_eff^mirror < 0.38 → ξ < 0.50 → ΔH₀ < 2.4
- **H₀ ≈ 69.7–70.1**

**Assessment:** The BBN constraint has tightened. The older BBN limit
(ξ < 0.50) allowed H₀ up to 70. The updated BBN limit (ξ < 0.35)
allows only H₀ ≈ 68.3. The paper MUST use the updated BBN constraint.


## The Pantos & Perivolaropoulos reframing

P&P (arXiv:2601.00650, 2026) analyzed 88 sound-horizon-free H₀
measurements:
- Distance ladder methods: H₀ = 72.73 ± 0.39
- Non-DL, sound-horizon-free: H₀ = 69.37 ± 0.34
- Internal tension: 6.5σ

The tension is "distance ladder vs. everything else," not "early vs.
late universe."

The framework's contribution (ΔH₀ ~ 0.5–1.0) moves the CMB-inferred
value (67.4) toward the "everything else" consensus (69.4). The gap
between the framework prediction (~68.0–68.7) and the non-DL consensus
(69.4) is 1–3σ — suggesting the framework captures PART of the physics
but not all.


## Key fixes needed

### 1. Inconsistency in reference annotations

The reference to Gonzalo et al. (line ~360) says:
"Applied to the mirror sector by mirror symmetry, it loosens the BBN
constraint on ξ from 0.47 to ~0.87."

But the BODY (§Y.4.2) correctly argues the cascade does NOT loosen
the BBN constraint on ξ (the cascade redistributes energy within the
dark sector but doesn't change the total gravitational effect).

**The reference annotation is wrong.** It contradicts the body's
analysis. The cascade does NOT help the mirror sector because:
- BBN constrains TOTAL extra radiation (expansion rate)
- The cascade is an internal redistribution (brane → bulk)
- The total energy is conserved → H is unchanged → BBN bound unchanged

Fix: remove the incorrect annotation from the reference.


### 2. Update observational values

- ACT DR6: N_eff = 2.86 ± 0.13 (replaces 2.81 ± 0.18)
- BBN 2025: N_eff = 2.898 ± 0.141 (tighter than Fields et al. 2020)
- CCHP JWST: the paper cites "69.8 ± 0.6" but the full CCHP JWST
  results show a spread (70.39 for HST+JWST, 68.81 for JWST-only TRGB,
  67.80 for JWST-only JAGB). Present the full picture.
- Add Pantos & Perivolaropoulos meta-analysis
- Add DESI DR2 results
- Add Bedroya, Obied, Vafa & Wu (2507.03090) Dark Dimension support


### 3. Revise the prediction

Current: H₀ = 69–70 (ξ = 0.45–0.50)
Updated: H₀ ≈ 68.0–68.7 (ξ < 0.35–0.40, CMB + updated BBN constrained)

The prediction is weaker but more honest.


### 4. Add the extended parameter space caveat

Note that the ACT DR6 constraint N_eff = 2.86 ± 0.13 is from ΛCDM +
N_eff. In extended models (ΛCDM + N_eff + w₀ + wₐ, which is what the
framework predicts), the N_eff constraint typically loosens by 30–50%.
A dedicated MCMC analysis with the framework's specific model (mirror
radiation + thawing dilaton) has not been performed. Flag this as
important future work.


## Outline of the revised appendix

Y.1 — The Hubble tension (updated numbers, P&P reframing)
Y.2 — Geometric origin of dark radiation (unchanged — this is strong)
Y.3 — The dark radiation contribution (unchanged math, updated constraints)
Y.4 — The BBN constraint (updated to 2025 analysis, ξ < 0.35)
Y.5 — The CMB constraint (NEW section: ACT DR6, the binding constraint)
Y.6 — The framework's H₀ prediction (revised: H₀ ≈ 68.0–68.7)
Y.7 — Comparison with the observational landscape (updated, P&P reframing)
Y.8 — Why the dilaton does not provide EDE (keep, it's good)
Y.9 — Complementary cosmological results (N_eff rescue, S8, scorecard)
Y.10 — Falsifiability and future tests (CMB-S4 is KEY)
Y.11 — Summary


## The paper's message, revised

"The 5D orbifold geometry predicts dark radiation from the hidden brane.
Current data (ACT DR6, updated BBN) constrains the contribution to
ΔN_eff < 0.1–0.2, giving H₀ ≈ 68–69. This is above the pure ΛCDM
value and in the direction of the non-distance-ladder consensus, but
does not resolve the full tension. CMB-S4 (σ(N_eff) ~ 0.03) will
definitively determine whether the mirror sector contributes at the
level predicted."

This is honest, falsifiable, and positions the framework correctly.
