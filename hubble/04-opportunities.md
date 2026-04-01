# Phase 4 — Creative Opportunities Within the Framework

## Idea A: Reduced mirror degrees of freedom (the "lean hidden brane")

**Premise:** The Z2 orbifold doesn't require the hidden brane to host
a full mirror Standard Model. The orbifold projection can remove species.

If the hidden brane has a reduced particle content — say just a U(1)
dark photon and one neutrino-like fermion:

    g_*^{mirror} = 2 + (7/8)(2) = 3.75  (instead of 10.75)

Then:
    ΔN_eff = (3.75/1.75) × ξ^4 = 2.14 × ξ^4

**But this doesn't help.** The BBN/CMB constraint is on ΔN_eff itself,
not on ξ. A smaller g_* allows larger ξ for the same ΔN_eff, but the
maximum ΔN_eff (and therefore ΔH0) is capped by the N_eff constraint
regardless.

At the ACT DR6 2σ limit (ΔN_eff < 0.026):
- Full mirror: ξ < 0.255, ΔH0 < 0.16
- Lean hidden brane: ξ < 0.348, ΔH0 < 0.16

Same ΔH0. The bottleneck is the total radiation, not the temperature.

**Verdict: Does not resolve the tension.**


## Idea B: Extended parameter space loosens N_eff constraint

**Premise:** The ACT DR6 constraint N_eff = 2.86 ± 0.13 is from
ΛCDM + N_eff. In an extended model (ΛCDM + N_eff + w0 + wa), the
N_eff constraint loosens due to parameter degeneracies.

The framework predicts BOTH extra radiation AND evolving dark energy
(thawing dilaton, w ~ −0.8). In the joint fit, higher N_eff can be
compensated by different w values.

**This is plausible but unquantified.** Literature on extended models
typically shows the N_eff error inflating by 30–50% when additional
parameters are freed. If ACT DR6 in an extended model gives
σ(N_eff) ~ 0.20 (vs. 0.13 in ΛCDM+N_eff):

At 2σ: N_eff < 2.86 + 0.40 = 3.26
ΔN_eff_mirror < 3.26 − 3.094 = 0.166
ξ < 0.406
ΔH0 < 1.05
H0 < 69.1

**This helps!** But it requires an actual MCMC analysis to verify.

**Verdict: Promising, but needs computation. Flag as future work.**


## Idea C: The mirror sector recombines DIFFERENTLY

**Premise:** What if mirror sector physics modifies the CMB impact?

The mirror sector's effect on the visible CMB comes through two channels:
1. **Background effect:** Extra radiation → faster expansion → smaller
   sound horizon. This is what N_eff measures.
2. **Perturbation effect:** Free-streaming radiation causes phase shifts
   in the CMB peaks. Fluid-like radiation does not.

If the mirror sector is FLUID-LIKE (not free-streaming) at visible
recombination, it contributes to the background expansion (channel 1)
but not to the phase shifts (channel 2). The N_eff constraint from
the CMB primarily comes from the phase shifts. So fluid-like dark
radiation can have a larger ΔN_eff than free-streaming radiation.

**Problem:** As computed in 03-key-tension.md, mirror recombination
happens BEFORE visible recombination for all ξ < 1. After mirror
recombination, mirror photons free-stream.

**Possible exception:** If the mirror sector has additional interactions
that keep it coupled. In the framework, the mirror sector couples to
the bulk KK tower gravitationally. If the KK tower mediates effective
self-interactions in the mirror sector, the mirror photon mean free
path could remain short.

The KK-mediated scattering cross-section is σ ~ G_4^2 × T^2 (from
exchange of KK graviton modes). This is tiny. The mirror photon mean
free path is enormous. **Mirror photons free-stream.**

**Verdict: Does not work.**


## Idea D: Phase transition in the mirror sector near recombination

**Premise:** If a mirror phase transition occurs near visible
recombination (z ~ 1100), it could temporarily change the mirror
sector's equation of state, modifying its effect on the CMB in a
way that differs from constant N_eff.

Mirror QCD confinement: T_mirror ~ ξ × 200 MeV
At ξ = 0.5: T_mirror^QCD = 100 MeV, at visible T = 200 MeV, z ~ 10^9
Way too early.

Mirror recombination: z_mirror ~ 2500–4000 (as computed above)
This is before visible recombination but after it in temperature terms.

**No mirror phase transition occurs near z ~ 1100.**

**Verdict: Does not work.**


## Idea E: Reframe as concordance with ACT DR6 H0

**Premise:** ACT DR6 + DESI gives H0 = 68.22–68.43. The framework with
modest mirror radiation (ξ ~ 0.30–0.35) gives H0 ≈ 68.0–68.5.
These are CONSISTENT.

The argument becomes:
- The framework with ξ ~ 0.30 predicts H0 ≈ 68.0 and ΔN_eff ≈ 0.05
- This is consistent with ACT DR6 (N_eff = 2.86 ± 0.13 → 3.14 is ~2σ)
- The shift from 67.4 to 68.0 is modest but in the right direction
- The rest of the gap (68 → 69.4 or 73) is outside the framework

**Problem:** This is a much weaker claim. ΔH0 ≈ 0.6 is barely
distinguishable from noise. The prediction loses its punch.

**Verdict: Honest but weak.**


## Idea F: Two-tier prediction (STRONGEST OPTION)

**Premise:** Present two predictions — one conservative (using latest
constraints) and one forward-looking (what CMB-S4 will test).

**Tier 1 — Current data (ACT DR6 constrained):**
- ξ < 0.35 (2σ from ACT DR6)
- ΔN_eff < 0.10
- H0 = 67.7–68.3 (barely above ΛCDM)
- Status: CONSISTENT with all current data

**Tier 2 — Framework prediction (testable by CMB-S4):**
- ξ = 0.35–0.50 (BBN-limited, aggressive)
- ΔN_eff = 0.09–0.38
- H0 = 68.3–70.1
- Status: IN TENSION with ACT DR6 at 2.5–4.8σ

The paper would say: "Current data constrains the mirror contribution
to be modest (Tier 1). The full BBN-allowed range (Tier 2) is in
tension with ACT DR6 but will be definitively tested by CMB-S4.
If CMB-S4 finds N_eff > 3.15, the mirror sector is confirmed at
the level needed for a significant H0 shift."

**Verdict: Honest, structured, and gives a clear future test.**


## Idea G: The Pantos & Perivolaropoulos concordance (COMPLEMENTARY)

**Premise:** Use the P&P meta-analysis to reframe the comparison.

The framework doesn't need to reach H0 = 73. The P&P analysis shows
the REAL tension is distance ladder (72.7) vs. everything else (69.4).
The CMB-inferred value (67.4) is one data point within "everything
else." Even a modest ΔH0 ~ 0.6–1.0 from the mirror sector moves the
CMB inference toward the "everything else" consensus.

The paper could argue:
- The framework's H0 prediction (68–69) is consistent with the
  non-distance-ladder consensus (69.4 ± 0.3)
- The gap between 68.5 and 69.4 is < 2σ
- The distance ladder discrepancy (73 vs. 69) is a calibration
  question, not a fundamental physics question
- The framework addresses the physics question (why is the CMB H0
  lower than most other methods?) by predicting extra dark radiation


## Recommended strategy: F + G

Combine Ideas F and G:

1. Present the two-tier prediction (F)
2. Use the P&P reframing (G) to argue the framework's modest shift
   is in the right direction and consistent with the "everything else"
   consensus
3. Emphasize CMB-S4 as the definitive test
4. Honestly acknowledge the ACT DR6 tension for the larger ξ values
5. Note that extended parameter fits (Idea B) could loosen the
   constraint, but this requires future MCMC work

This approach is scientifically honest, makes falsifiable predictions,
and doesn't oversell the framework's current capability.
