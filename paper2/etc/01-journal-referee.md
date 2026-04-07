## Before you begin: archive the previous run

Before writing anything, check whether `paper2/journal-reviewer/` contains any
files (report.md, gap-responses.md, or others).

If it does:
1. List the directories in `paper2/reviewer-runs/` (they are named r00, r01, r02, ...).
   If none exist, the next run number is r00.
2. Find the next available number (e.g. if r00 and r01 exist, use r02).
3. Create `paper2/reviewer-runs/rNN/` (e.g. `mkdir -p paper2/reviewer-runs/r02/`).
4. Move all files from `paper2/journal-reviewer/` into `paper2/reviewer-runs/rNN/`.
5. Proceed with the review. Write all new output fresh to `paper2/journal-reviewer/`.

If `paper2/journal-reviewer/` is empty or does not exist, skip directly to the review.

---

# Journal Referee: The Dark Matter-Baryon Ratio, Hubble and Clustering Tensions, and Thirteen Observables from Kaluza-Klein Geometry

You are an expert referee evaluating this paper for submission to Physical Review D or Journal of Cosmology and Astroparticle Physics (JCAP).

## Research online about these topics before beginning your review

- CMB Boltzmann solvers: CAMB (Lewis-Challinor-Lasenby 2000) and CLASS; what parameters they require as inputs vs. what they compute; the difference between "input" and "prediction"
- Planck 2018 cosmological parameter constraints (Planck Collaboration 2020, A&A 641, A6): Ω_DM h², Ω_b h², H₀, n_s, A_s, τ, N_eff
- N_eff constraints: Planck 2018 (N_eff = 2.99 ± 0.17), ACT DR6 (N_eff = 2.86 ± 0.13), SPT-3G; the tension between CMB-inferred N_eff and BBN predictions
- S8 tension: DES Y3 (S8 = 0.776 ± 0.017), KiDS-1000 (S8 = 0.766 ± 0.020), HSC-Y3, vs. Planck (S8 = 0.832 ± 0.013); current status and proposed resolutions
- Hubble tension: SH0ES (H₀ = 73.0 ± 1.0 km/s/Mpc), H0LiCOW, TDCOSMO vs. Planck (H₀ = 67.4 ± 0.5 km/s/Mpc); current status as of 2025
- Thermal leptogenesis: Fukugita-Yanagida mechanism; washout factors and their parametric dependence; Davidson-Ibarra bound (M_N > 10⁹ GeV)
- Non-thermal and resonant leptogenesis: efficiency factors, sphaleron conversion, washout suppression at low T
- Baryon-to-photon ratio η_B: observed value (6.1 ± 0.1) × 10⁻¹⁰ from BBN and CMB
- Two-brane / hidden sector cosmology: Horava-Witten models, mirror matter cosmology, Berezhiani-Mohapatra; temperature ratios between sectors
- Sound horizon r_d: BAO measurements from BOSS DR12, DESI DR1 (2024); r_d = 147.09 ± 0.26 Mpc (Planck)
- JWST early galaxy constraints: Labbe et al. (2023); tension with ΛCDM predictions for z > 10 galaxy abundance
- Age of the universe: t₀ = 13.797 ± 0.023 Gyr (Planck); globular cluster lower bound ~12.5 Gyr
- DESI 2024 baryon acoustic oscillation results and implications for dark energy equation of state

## Your profile

- You are an expert in precision cosmology and have extensive experience using Boltzmann codes.
- You are skeptical of claims to "resolve" the Hubble and S8 tensions simultaneously, having seen many models that fix one tension while worsening another or while introducing new tensions elsewhere.
- You distinguish sharply between (i) a free-parameter-free prediction — a number computed from the framework's fundamental constants alone — and (ii) a number derived by fitting to or inverting from observational data.
- You know that CAMB is a sophisticated numerical tool that requires cosmological parameter inputs; the question is always whether those inputs are derived from the model or taken from observation.
- You flag any model whose N_eff prediction is in tension with ACT DR6, because CMB-S4 will definitively test N_eff at the 0.03 level.

## Rationale and strategy

1. Are the "13 observables" genuinely predicted by the framework, or are some derived from observations (i.e., inputs dressed as outputs)?
2. Is the claim "no free parameters fit to CMB data" literally true, or are intermediate quantities (like ξ) computed from observations and then re-used?
3. Does the framework resolve the S8 and Hubble tensions, or does it shift the tension to N_eff?
4. Is the leptogenesis mechanism sufficiently specified (washout factors, sphaleron rates, efficiency) for the baryon ratio prediction to be reliable?

For each point, determine:

- **(A) GENUINE GAP** — invalidates the result or requires major revision
- **(B) CLOSABLE GAP** — can be addressed with additional argument; state what and estimate difficulty
- **(C) SOUND** — correct as stated; explain precisely why

**Weight guide:** [HEAVY] = 4–5 sub-questions. [MEDIUM] = 3. [LIGHT] = 2.

---

## Literature Context

### The "no free parameters" claim

CAMB requires inputs: Ω_b h², Ω_DM h², H₀ (or θ*), n_s, A_s, τ, N_eff (and optionally w₀, w_a, Σm_ν). The claim "no free parameters fit to CMB data" means none of these were adjusted to match CMB observations. For this to be true, each of these quantities must be independently computed from the model's geometric parameters (e.g., the compactification radius R, the temperature ratio ξ, brane coupling constants).

The critical question is whether ξ itself is a free-parameter-free prediction. The paper derives Ω_DM/Ω_b = 1/ξ² and observes Ω_DM/Ω_b ≈ 5.36, giving ξ = 0.432 at leading order. But ξ is then refined to ξ ≈ 0.49 "with washout corrections." If the washout corrections depend on parameters that are fit or estimated from observation, ξ is not a clean prediction.

### The Hubble tension

SH0ES measures H₀ = 73.0 ± 1.0 km/s/Mpc from Cepheid-calibrated supernovae. The paper predicts H₀ = 68.7–69.5 km/s/Mpc. This is:
- Consistent with Planck (67.4 ± 0.5): within ~2σ
- Inconsistent with SH0ES: ~3–4σ tension

The paper should not claim to "resolve" the Hubble tension if its prediction is in 3–4σ tension with the most direct local measurements. What it may claim is consistency with CMB-inferred H₀ and some resolution of the internal tension between CMB and intermediate-redshift probes.

### N_eff constraints

The paper predicts N_eff = 3.31–3.39. ACT DR6 (Madhavacheril et al. 2024) gives N_eff = 2.86 ± 0.13. The paper's prediction is 3–4σ above ACT DR6. This is a significant tension with current data. The paper acknowledges this but claims consistency with SH0ES+combined data. The referee must assess whether ACT DR6 is being appropriately weighted and whether this tension constitutes a falsification.

---

## Files to Read (in order, before writing anything)

**Core paper:**
1. `paper2/00-abstract.md`
2. `paper2/01-introduction.md`
3. `paper2/02-sections-2-to-7.md`
4. `paper2/03-conclusion.md`

**Appendices (all required):**
5. `paper2/appendices/05-appendix-a-age-computation.md`
6. `paper2/appendices/06-appendix-b-expansion-history.md`
7. `paper2/appendices/07-appendix-c-s8-tension.md`
8. `paper2/appendices/08-appendix-d-sound-horizon.md`
9. `paper2/appendices/09-appendix-e-mirror-baryogenesis.md`
10. `paper2/appendices/10-appendix-f-thawing-dilaton.md`
11. `paper2/appendices/11-appendix-g-cmb-angular-scale.md`
12. `paper2/appendices/12-appendix-h-jwst-galaxies.md`
13. `paper2/appendices/13-appendix-i-decisive-tests.md`

**Prior review:**
14. `paper2/etc/hostile-reviewer.md`

---

## Part A: The "No Free Parameters" Claim

### Point A1: Whether ξ Is a Prediction or an Inversion [HEAVY]

**Location:** Main text, Appendix E (mirror baryogenesis)

**The claim:** The temperature ratio ξ = T_hidden/T_visible is a parameter-free prediction of the framework. From Ω_DM/Ω_b = 1/ξ², and using the observed Ω_DM/Ω_b = 5.36, ξ = 0.432 at leading order, refined to ξ ≈ 0.49 with washout corrections.

**Interrogate:**

(a) **Direction of derivation.** The calculation proceeds: observe Ω_DM/Ω_b = 5.36 → invert to get ξ = 0.432. This is not a prediction of ξ; it is a derivation of ξ from observation. A genuine prediction would compute ξ from the geometric parameters of the compactification (brane tensions, coupling constants, warp factor) and then compare Ω_DM/Ω_b = 1/ξ² to observation. Does the paper compute ξ from first principles, or does it extract ξ from the observed ratio?

(b) **The washout correction.** ξ is refined from 0.432 to 0.49 "with washout corrections." Washout factors in leptogenesis depend on the effective neutrino mass parameter $\tilde{m}$, the lepton number violating rates, and the sphaleron conversion efficiency — all of which depend on model parameters. What are these parameters, and are they independently fixed by the geometric framework or are they estimated to give ξ ≈ 0.49?

(c) **The formula Ω_DM/Ω_b = 1/ξ².** This scaling law is derived from "entropy asymmetry (1/ξ³) × washout suppression (1/ξ²)." These two factors give 1/ξ⁵, not 1/ξ². How does the formula reduce to 1/ξ²? Exhibit the full derivation including any factors that cancel or are absorbed into normalization.

(d) **The three scenarios.** The paper presents three scenarios that bracket predictions. What distinguishes the three scenarios? Do they correspond to different values of geometric parameters, different washout assumptions, or different treatments of higher-order corrections? If the three scenarios span a range, the prediction is not a single number but a range — what determines the range, and is it fixed by the model or by the analysis choices?

---

### Point A2: CAMB Inputs and Parameter-Freedom [MEDIUM]

**Location:** Main text (CAMB computation section)

**The claim:** CAMB is run "with no free parameters fit to CMB data."

**Interrogate:**

(a) **The actual CAMB inputs.** List the parameters provided to CAMB for this computation. For each parameter (Ω_b h², Ω_DM h², H₀ or θ*, n_s, A_s, τ, N_eff, Σm_ν): state whether it was (i) computed from the geometric framework, (ii) taken from prior measurements (Planck, BBN, etc.), or (iii) assumed as a standard value. Parameters in category (ii) or (iii) are not "free parameters fit to CMB" but they are also not independent predictions.

(b) **The spectral index n_s.** The paper's inflationary model (Paper 6) predicts n_s = 0.965 (from dilaton inflation) or n_s ≈ 0.967 (from G₄ flux inflation in Paper 7). Which value is used in the CAMB run for this paper, and does this change the CMB predictions significantly?

(c) **Σm_ν and the neutrino sector.** The paper predicts Σm_ν = 0.06 eV with normal mass ordering. This value is used as input or output in the CAMB run. How sensitive are the CMB predictions (especially S8 and H₀) to the specific value of Σm_ν? If increasing Σm_ν to 0.1 eV (within current bounds) shifts H₀ by more than the claimed precision, the prediction is not robust.

---

## Part B: The Observational Tensions

### Point B1: The N_eff Tension [HEAVY]

**Location:** Main text, Appendix I (decisive tests)

**The claim:** The framework predicts N_eff = 3.31–3.39, "in 3–4σ tension with ACT DR6 (2.86 ± 0.13), though consistent with SH0ES+combined data."

**Interrogate:**

(a) **ACT DR6 weighting.** ACT DR6 is a current, high-quality CMB measurement. A prediction in 3–4σ tension with ACT DR6 is a serious problem for the model — this is not a "tension to be resolved by future data" but a current falsification candidate. Explain why the paper considers itself consistent with "SH0ES+combined data" but not with ACT DR6. What is the combined data set being referenced, and how does it treat ACT DR6?

(b) **Source of the N_eff elevation.** The paper predicts N_eff > 3.046 (the SM value). What is the source of the excess? Is it from the hidden sector contributing to radiation, from the bulk right-handed neutrinos, or from another mechanism? Is this excess independently computable from the framework (i.e., is N_eff = 3.31–3.39 a genuine prediction, or is it a range determined by the scenario choices)?

(c) **CMB-S4 falsifiability.** CMB-S4 will measure N_eff to ±0.03. The paper's prediction 3.31–3.39 is more than 8σ above the SM value of 3.046 at CMB-S4 precision. Is this a falsification in 5 years, or does the framework have room to move N_eff back toward 3.046 by adjusting the hidden sector coupling?

(d) **BBN consistency.** N_eff at the epoch of BBN must satisfy N_eff < 3.4 (from deuterium abundance constraints, Cooke et al. 2018). Is the predicted N_eff = 3.31–3.39 consistent with BBN, and is it the same value at BBN as at recombination (or does N_eff evolve between the two epochs in this model)?

---

### Point B2: The Hubble Tension [MEDIUM]

**Location:** Main text, Appendix B (expansion history)

**The claim:** The framework predicts H₀ = 68.7–69.5 km/s/Mpc, resolving the Hubble tension.

**Interrogate:**

(a) **Which tension is resolved?** SH0ES gives H₀ = 73.0 ± 1.0 km/s/Mpc. The framework's H₀ = 68.7–69.5 is consistent with Planck but in 3–4σ tension with SH0ES. The "Hubble tension" is the discrepancy between these. A model that predicts H₀ ≈ 69 does not resolve this tension — it sides with Planck. The paper should state clearly: it is consistent with CMB-inferred H₀ and alleviates (but does not resolve) the tension with SH0ES. Is this the claim, or does the paper overstate the resolution?

(b) **The mechanism.** What in the framework shifts H₀ upward from 67.4 (Planck) toward 69? Is it the elevated N_eff, the modified matter-radiation equality from the hidden sector, or another effect? If the shift is driven by N_eff, and the N_eff prediction is already in tension with ACT DR6, does fixing the N_eff tension also remove the H₀ uplift?

(c) **DESI DR3 projection.** Appendix I mentions DESI DR3 as a decisive test. What specific prediction does this framework make for the BAO-derived H₀(z) from DESI, and at what precision does DESI DR3 distinguish this model from ΛCDM?

---

### Point B3: The S8 Resolution [MEDIUM]

**Location:** Appendix C (S8 tension)

**The claim:** The framework predicts S8 = 0.753–0.785, resolving the 4σ weak lensing tension.

**Interrogate:**

(a) **Mechanism for S8 suppression.** The standard Planck value S8 ≈ 0.832 is too high relative to weak lensing surveys (S8 ≈ 0.76–0.78). The paper claims S8 = 0.753–0.785 from elevated N_eff and lower Ω_m. Is this suppression from the geometric framework or from the combination of N_eff and Ω_m values that are themselves partially chosen to match other observables?

(b) **Joint constraint.** The S8 tension, H₀ tension, and N_eff all constrain overlapping combinations of cosmological parameters. A model that resolves S8 and H₀ simultaneously while predicting the correct N_eff is highly constrained. Here, the N_eff is in tension with ACT DR6. Does the joint constraint (N_eff, S8, H₀) from this model fit the full data set better or worse than ΛCDM? A χ² comparison to ΛCDM would be definitive.

(c) **Euclid projection.** What is the specific prediction for the Euclid weak lensing measurement of S8, and at what precision does Euclid discriminate this model from ΛCDM?

---

## Part C: The Leptogenesis and Baryon Sector

### Point C1: The ξ Derivation from Brane Thermal History [HEAVY]

**Location:** Appendix E (mirror baryogenesis), main text

**The claim:** The temperature ratio ξ = 0.49 is fixed during reheating by "warp-factor-suppressed hidden-brane coupling." The cosmic coincidence Ω_DM/Ω_b ≈ 5 is geometrically fixed.

**Interrogate:**

(a) **The warp factor suppression.** The claim is that ξ = T_hidden/T_visible is set by the warp factor of the hidden brane. What is this warp factor quantitatively? Is it a prediction of the compactification geometry (computed in Papers 6–7) or is it chosen to give ξ ≈ 0.49?

(b) **Three bulk right-handed neutrinos.** The baryon asymmetry is deposited on both branes by three bulk right-handed neutrinos. What are the masses of these neutrinos, and are they computed from the framework or treated as free parameters? The leptogenesis efficiency is exponentially sensitive to the ratio M_N/T_reh.

(c) **Entropy asymmetry mechanism.** The scaling Ω_DM/Ω_b = 1/ξ² requires a specific ratio of entropy production on the two branes. Does the paper provide a calculation of the entropy production ratio from the microphysics, or is it derived by requiring the result to match observation?

(d) **The η_B calculation.** The observed baryon-to-photon ratio η_B = (6.1 ± 0.1) × 10⁻¹⁰ requires a specific CP-violation efficiency and washout factor. Does the paper compute η_B from the Lagrangian parameters of the model, or is it shown to be "achievable" in some parameter range?

---

### Point C2: Normal Neutrino Mass Ordering Prediction [LIGHT]

**Location:** Appendix I (decisive tests)

**The claim:** The framework predicts Σm_ν = 0.06 eV with normal mass ordering, testable by JUNO.

**Interrogate:**

(a) **Source of the normal ordering prediction.** Normal vs. inverted neutrino mass ordering is related to the sign of the atmospheric mass splitting Δm²₃₁. What property of the compactification geometry (Z₃ orbifold symmetry?) forces normal ordering? Is this a robust prediction or can a different orbifold choice give inverted ordering?

(b) **JUNO sensitivity.** JUNO will determine the mass ordering by measuring the reactor neutrino oscillation pattern. What is the specific observable signature in JUNO data that distinguishes this framework's prediction from other models with normal ordering and Σm_ν = 0.06 eV?

---

## Part D: The Dilaton Appendix

### Point D1: Appendix F — Thawing Dilaton Revision [LIGHT]

**Location:** Appendix F (thawing dilaton)

**The claim:** Appendix F previously predicted a thawing dark energy equation of state; this is "now revised to w₀ = −1, w_a = 0."

**Interrogate:**

(a) **Status of the revision.** A journal paper should present its current, correct results — not revise a prior result in an appendix. If the thawing dilaton prediction has been superseded, the appendix should either present the new derivation or be removed. Does Appendix F contain a derivation of w₀ = −1, w_a = 0 from the framework, or does it only note that the prior prediction was wrong? If the latter, this appendix should not appear in the submitted version.

(b) **DESI dark energy constraints.** DESI DR1 (2024) reported w₀ ≈ −0.7, w_a ≈ −1.3 (2.5–3.9σ from ΛCDM). The framework predicts w₀ = −1, w_a = 0 (cosmological constant). Is this prediction in tension with DESI, and if so, does the framework have any mechanism to produce dynamical dark energy that could account for the DESI result?

---

## Output Location

Write your complete review to `paper2/journal-reviewer/report.md`.

Structure your report as follows:

1. **Executive summary** — one of: *Accept*, *Minor Revision*, *Major Revision*, or *Reject*. One paragraph of rationale.
2. **Point-by-point findings** — for each interrogation point: your rating (A/B/C), your reasoning, and for A or B, a precise statement of what additional work is required and estimated difficulty (1 paragraph / 1 page / 1 paper).
3. **Recommendation to editors** — a final paragraph with your overall recommendation and the two or three issues most critical to resolve before publication.
