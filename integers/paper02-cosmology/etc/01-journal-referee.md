## Before you begin: archive the previous run

Before writing anything, check whether `integers/paper02-cosmology/journal-reviewer/` contains any
files (report.md, gap-responses.md, or others).

If it does:
1. List the directories in `integers/paper02-cosmology/reviewer-runs/` (they are named r00, r01, r02, ...).
   If none exist, the next run number is r00.
2. Find the next available number (e.g. if r00 and r01 exist, use r02).
3. Create `integers/paper02-cosmology/reviewer-runs/rNN/` (e.g. `mkdir -p integers/paper02-cosmology/reviewer-runs/r02/`).
4. Move all files from `integers/paper02-cosmology/journal-reviewer/` into `integers/paper02-cosmology/reviewer-runs/rNN/`.
5. Proceed with the review. Write all new output fresh to `integers/paper02-cosmology/journal-reviewer/`.

If `integers/paper02-cosmology/journal-reviewer/` is empty or does not exist, skip directly to the review.

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
1. `integers/paper02-cosmology/00-abstract.md`
2. `integers/paper02-cosmology/01-introduction.md`
3. `integers/paper02-cosmology/02-sections-2-to-7.md`
4. `integers/paper02-cosmology/03-conclusion.md`

**Appendices (all required):**
5. `integers/paper02-cosmology/appendices/05-appendix-a-age-computation.md`
6. `integers/paper02-cosmology/appendices/06-appendix-b-expansion-history.md`
7. `integers/paper02-cosmology/appendices/07-appendix-c-s8-tension.md`
8. `integers/paper02-cosmology/appendices/08-appendix-d-sound-horizon.md`
9. `integers/paper02-cosmology/appendices/09-appendix-e-mirror-baryogenesis.md`
10. `integers/paper02-cosmology/appendices/10-appendix-f-thawing-dilaton.md`
11. `integers/paper02-cosmology/appendices/11-appendix-g-cmb-angular-scale.md`
12. `integers/paper02-cosmology/appendices/12-appendix-h-jwst-galaxies.md`
13. `integers/paper02-cosmology/appendices/13-appendix-i-decisive-tests.md`

**Prior review:**
14. `integers/paper02-cosmology/etc/hostile-reviewer.md`

---

## Part A: The "No Free Parameters" Claim

### Point A1: Whether ξ Is a Prediction or an Inversion [HEAVY]

**Location:** Main text §2.2, Appendix E (mirror baryogenesis)

**The claim:** The temperature ratio ξ = T_hidden/T_visible is a parameter-free prediction of the framework. From Ω_DM/Ω_b = 1/ξ², and using the observed Ω_DM/Ω_b = 5.36, ξ = 0.432 at leading order, refined to ξ ≈ 0.49 with washout corrections. The paper further asserts that ξ = 0.432 constitutes a measurement of the 5D warp parameter $c_\nu = 0.634$.

**Interrogate:**

(a) **Direction of derivation.** The calculation proceeds: observe Ω_DM/Ω_b = 5.36 → invert to get ξ = 0.432. This is not a prediction of ξ; it is a derivation of ξ from observation. A genuine prediction would compute ξ from the geometric parameters of the compactification (brane tensions, coupling constants, warp factor) and then compare Ω_DM/Ω_b = 1/ξ² to observation. Does the paper compute ξ from first principles, or does it extract ξ from the observed ratio?

(b) **The washout correction.** ξ is refined from 0.432 to 0.49 "with washout corrections." Washout factors in leptogenesis depend on the effective neutrino mass parameter $\tilde{m}$, the lepton number violating rates, and the sphaleron conversion efficiency — all of which depend on model parameters. What are these parameters, and are they independently fixed by the geometric framework or are they estimated to give ξ ≈ 0.49?

(c) **The formula Ω_DM/Ω_b = 1/ξ².** This scaling law is derived from "entropy asymmetry (1/ξ³) × washout suppression (1/ξ²)." These two factors give 1/ξ⁵, not 1/ξ². How does the formula reduce to 1/ξ²? Exhibit the full derivation including any factors that cancel or are absorbed into normalization.

(d) **The three scenarios.** The paper presents three scenarios that bracket predictions. What distinguishes the three scenarios? Do they correspond to different values of geometric parameters, different washout assumptions, or different treatments of higher-order corrections? If the three scenarios span a range, the prediction is not a single number but a range — what determines the range, and is it fixed by the model or by the analysis choices?

(e) **ξ as a measurement of $c_\nu$.** The paper claims that ξ = 0.432 from $\Omega_{DM}/\Omega_b$ constitutes a measurement of the 5D parameter $c_\nu = 0.634$ (from Paper 1, Appendix W §W.5, via $k = 2$). For this to be a measurement of a 5D parameter — rather than circular reasoning — the chain must run: (i) compactification geometry fixes $k = 2$ independently; (ii) $k = 2$ gives $c_\nu = 0.634$ by an analytic formula; (iii) $c_\nu$ predicts ξ via the leptogenesis calculation; (iv) the predicted ξ is compared to the observed $\Omega_{DM}/\Omega_b$. Does §2.2 execute all four steps, or does it run the chain backward — inferring $c_\nu$ from the observed ratio and calling the inversion a "measurement"? If the latter, the language is misleading and must be corrected.

---

### Point A2: The Z₂ Conservation Theorem [MEDIUM]

**Location:** Main text §2.2

**The claim:** ξ is conserved through all thermal history — it does not evolve between reheating and recombination — because the $Z_2$ symmetry of the orbifold makes $\Delta g_*$ identical in both sectors at every phase transition.

**Interrogate:**

(a) **Rigor of the proof.** The claim that $Z_2$ symmetry forces $\Delta g_*^{\text{hidden}} = \Delta g_*^{\text{visible}}$ at every phase transition is a non-trivial assertion. The standard model has QCD and electroweak phase transitions; the mirror sector has mirror-QCD and mirror-electroweak transitions at temperatures scaled by ξ. Even under exact $Z_2$ symmetry, the transitions occur at different times (since $T_{\text{hidden}} = \xi T_{\text{visible}}$ with $\xi < 1$), meaning they never overlap in cosmic time. How then can $\Delta g_*$ be "identical" at the same time? State the precise theorem: is the claim that the entropy injection into each sector is individually zero at every transition (no entropy production — i.e., the transitions are all second-order), or is the claim that the ratio of entropy injections from the two sectors is unity?

(b) **Phase transition order.** QCD confinement in the visible sector is a crossover (not a true phase transition) at $T_{\text{QCD}} \approx 150$ MeV. If mirror QCD is also a crossover, no entropy is injected by either sector at $T_{\text{mirror-QCD}} \approx 65$ MeV (for ξ = 0.432), and the $Z_2$ argument is unnecessary — ξ is conserved trivially. If the transitions are first-order (as in some BSM scenarios), they produce latent heat and inject entropy differently depending on the bubble nucleation dynamics, which the $Z_2$ symmetry does not control. Which case does the paper assume, and is the assumption justified by the mirror sector spectrum?

(c) **Consequence for the "no free parameters" claim.** If the Z₂ conservation theorem is sound, ξ is genuinely set at reheating and does not drift — the cosmological prediction uses a single ξ throughout. If the theorem has a gap (for example, if one sector undergoes a first-order transition the other does not, breaking $Z_2$ thermally), ξ is time-varying and the CAMB run with a fixed ξ is internally inconsistent. Assess whether this theorem, if it fails, qualitatively invalidates the cosmological predictions of §2.4 and onward.

---

### Point A3: CAMB Inputs and Parameter-Freedom [MEDIUM]

**Location:** Main text (CAMB computation section)

**The claim:** CAMB is run "with no free parameters fit to CMB data."

**Interrogate:**

(a) **The actual CAMB inputs.** List the parameters provided to CAMB for this computation. For each parameter (Ω_b h², Ω_DM h², H₀ or θ*, n_s, A_s, τ, N_eff, Σm_ν): state whether it was (i) computed from the geometric framework, (ii) taken from prior measurements (Planck, BBN, etc.), or (iii) assumed as a standard value. Parameters in category (ii) or (iii) are not "free parameters fit to CMB" but they are also not independent predictions.

(b) **The spectral index n_s.** The paper's inflationary model (Paper 6) predicts n_s = 0.965 (from dilaton inflation) or n_s ≈ 0.967 (from G₄ flux inflation in Paper 7). Which value is used in the CAMB run for this paper, and does this change the CMB predictions significantly?

(c) **Σm_ν and the neutrino sector.** The paper predicts Σm_ν = 0.06 eV with normal mass ordering. This value is used as input or output in the CAMB run. How sensitive are the CMB predictions (especially S8 and H₀) to the specific value of Σm_ν? If increasing Σm_ν to 0.1 eV (within current bounds) shifts H₀ by more than the claimed precision, the prediction is not robust.

---

## Part B: The Observational Tensions

### Point B1: The N_eff Tension and Mirror Recombination [HEAVY]

**Location:** Main text §2.3–§2.4, Appendix I (decisive tests)

**The claim:** The framework predicts a corrected $\Delta N_{\text{eff}} = 3.43\,\xi^4$ (superseding the earlier formula $6.14\,\xi^4$), giving N_eff in the range 3.31–3.39. The tension with ACT DR6 (N_eff = 2.86 ± 0.13) is stated as precisely 3.5σ. A degeneracy scan over the available parameter space finds no combination of parameters that closes this gap. Mirror recombination occurs at $z \approx 2463$ (before visible recombination at $z \approx 1090$), after which mirror photons free-stream and contribute to $\Delta N_{\text{eff}}$.

**Interrogate:**

(a) **Derivation of the corrected formula $3.43\,\xi^4$ vs. $6.14\,\xi^4$.** The factor of 2 discrepancy between the old and new $\Delta N_{\text{eff}}$ prefactors is significant — it shifts the prediction by roughly 0.12 in N_eff for ξ = 0.432. Exhibit the calculation that gives 3.43: where does the factor 3.43 come from (is it $2 \times (4/11)^{4/3} \times f$ for some $f$?), and what was wrong in the prior derivation that gave 6.14? A corrected formula of this specificity requires a derivation that can be checked line-by-line, not just a quoted number.

(b) **Mirror recombination at z ≈ 2463.** If mirror hydrogen recombines at $z_{\text{mirror}} \approx 2463$ and mirror photons subsequently free-stream, they contribute to $N_{\text{eff}}$ as if they were additional neutrino species from the visible sector's perspective. The free-streaming mirror photons must be accounted for in the CAMB run as a modified radiation component, not as standard neutrinos. Does the CAMB run implement the mirror photon free-streaming correctly — specifically, does it treat the mirror photons as a relativistic fluid before $z_{\text{mirror}}$ and as free-streaming radiation after? If not, the CMB power spectrum predictions are wrong at multipoles $\ell$ sensitive to the damping tail at $z \sim 2000$.

(c) **The 3.5σ ACT tension and the degeneracy scan.** The paper states a 3.5σ tension with ACT DR6 and asserts that no parameter space closes this gap. Describe the degeneracy scan: which parameters were varied (ξ, $M_{KK}$, $\Sigma m_\nu$, $H_0$, etc.), over what ranges, and what statistic was used to measure the tension (χ² improvement, Δ ln $\mathcal{L}$, tension metric)? A statement that "no parameter space closes the tension" is extraordinary — it means the ACT DR6 constraint, if correct, falsifies the model at 3.5σ. Has the paper verified that the tension cannot be reduced by, for example, varying ξ below 0.432 (which would lower $\Delta N_{\text{eff}}$), even at the cost of worsening the $\Omega_{DM}/\Omega_b$ fit?

(d) **Mirror BAO signature.** Mirror recombination at $z \approx 2463$ imprints a mirror sound horizon $r_d^{\text{mirror}} = r_d^{\text{visible}} \times \xi^{\alpha}$ on the matter power spectrum. State the predicted mirror BAO peak location in units of $h/\text{Mpc}$ (or equivalently, the angular scale in the CMB), and whether this signature has been searched for in BOSS DR12 or DESI DR1 data. If the mirror BAO peak lies within the current survey window, its non-detection is a constraint on this model.

(e) **CMB-S4 falsifiability.** CMB-S4 will measure N_eff to ±0.03. The paper's prediction 3.31–3.39 is more than 8σ above the SM value of 3.046 at CMB-S4 precision. Is this a falsification in 5 years, or does the framework have room to move N_eff back toward 3.046 by adjusting the hidden sector coupling?

(f) **BBN consistency.** N_eff at the epoch of BBN must satisfy N_eff < 3.4 (from deuterium abundance constraints, Cooke et al. 2018). Is the predicted N_eff = 3.31–3.39 consistent with BBN, and is it the same value at BBN as at recombination (or does N_eff evolve between the two epochs in this model)? In particular, if mirror recombination at $z \approx 2463$ changes the effective radiation content between BBN and recombination, the N_eff inferred from deuterium abundance is not the same N_eff entering the CMB Boltzmann equations — this discrepancy must be tracked.

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

Write your complete review to `integers/paper02-cosmology/journal-reviewer/report.md`.

Structure your report as follows:

1. **Executive summary** — one of: *Accept*, *Minor Revision*, *Major Revision*, or *Reject*. One paragraph of rationale.
2. **Point-by-point findings** — for each interrogation point: your rating (A/B/C), your reasoning, and for A or B, a precise statement of what additional work is required and estimated difficulty (1 paragraph / 1 page / 1 paper).
3. **Recommendation to editors** — a final paragraph with your overall recommendation and the two or three issues most critical to resolve before publication.
