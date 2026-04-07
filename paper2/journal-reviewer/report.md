# Referee Report
## "The Dark Matter-Baryon Ratio, Hubble and Clustering Tensions, and Thirteen Observables from Kaluza-Klein Geometry"

**Submitted to:** Physical Review D / JCAP
**Recommendation:** Major Revision

---

## 1. Executive Summary

**Recommendation: Major Revision**

This paper presents cosmological predictions from a 5D Kaluza-Klein framework with a mirror (Z2 orbifold) hidden sector, claiming that two observational inputs — the dark energy density rho_Lambda and the dark matter-baryon ratio Omega_DM/Omega_b — together with fixed Standard Model content, determine a complete set of cosmological observables with no free parameters fitted to CMB data. The central technical result is a scaling law Omega_DM/Omega_b = 1/xi^2 derived from temperature-asymmetric bulk leptogenesis, which determines the hidden-to-visible brane temperature ratio xi.

The paper has genuine intellectual content and several correct derivations. The CAMB parameter audit (Section 2.3, Table 1) is unusually transparent. The three-scenario bracketing strategy is scientifically honest. The acknowledgment that N_eff = 3.31-3.39 is in 3.5sigma tension with ACT DR6 — and that this tension cannot be closed by parameter adjustment — is admirable. The paper earns credit for predicting the correct S8 range and for a non-trivial theta* near-match.

However, there are issues that must be addressed before publication. The most critical are: (1) the fluid vs. free-streaming N_eff inconsistency — the paper uses the fluid formula (6.14 xi^4, giving N_eff = 3.31-3.39) in all tables while acknowledging in prose that the correct free-streaming formula gives approximately 3.43 xi^4 (N_eff ~ 3.16-3.19), materially changing the quoted 3.5sigma ACT tension; (2) the claim that xi = 0.432 "measures" the GUT-scale parameter c_nu = 0.634 appears to run the derivation chain backward; (3) the Z2 conservation theorem proof is stated without handling the case of non-simultaneous phase transitions; (4) the A_s value is inconsistent between Section 2.3 (2.1 x 10^{-9}) and Appendix A Section A.3 (2.215 x 10^{-9}), which propagates a ~3% error in sigma_8 and S8.

These are all closable gaps. None represents a fatal error in the core physics. I recommend major revision with the revisions described below.

---

## 2. Point-by-Point Findings

### Part A: The "No Free Parameters" Claim

#### Point A1(a): Direction of derivation — is xi a prediction or an inversion?
**Rating: (B) CLOSABLE GAP**

The paper correctly states the logical structure at Section 2.2: the 1/xi^2 law is derived from first principles in Appendix E, and only then is the observed Omega_DM/Omega_b inserted to determine xi = 0.432. The phrase "determination from a derived law, not a prediction of xi in isolation" is accurate and defensible.

However, the language is not uniformly maintained. In Appendix E Section E.1, the paper starts by saying "The theta* constraint requires omega_c h^2 = 0.117, corresponding to eta_ratio ~ 50. We need a mechanism that produces eta_ratio ~ 50." This inverts the derivation direction: the paper opens by stating the conclusion (theta*-required eta_ratio ~ 50) as the goal of the derivation, then shows it is achieved. This makes the derivation appear reverse-engineered, even if Section E.3 runs in the correct direction. Similarly, in Appendix A Section A.3 and G.2, omega_c h^2 = 0.117 in Scenario A is described as "from theta* consistency" — meaning Scenario A uses the CMB acoustic scale to fix one effective parameter, which should be explicitly distinguished from a "zero free parameter" prediction.

**Required work:** Revise Section E.1 so that it does not begin from the theta*-required eta_ratio ~ 50 as motivation. The derivation should start from the bulk leptogenesis mechanism and conclude with eta_ratio = 1/xi^5. Agreement with the theta*-required value is a cross-check, not the starting point. Additionally, clarify in Section 2.2 and Section 6.1 that in Scenario A, xi = 0.47 is constrained by theta* matching (a CMB observable, not a CMB parameter fit), and that the convergence of this theta*-constrained xi with the leptogenesis-derived xi = 0.49 is the non-trivial cross-check. Estimated difficulty: 2-3 paragraphs.

---

#### Point A1(b): The washout correction — are the parameters independently fixed?
**Rating: (B) CLOSABLE GAP**

The washout parameter K ~ 5 is derived in Section E.3.3 using m_nu = 50 meV and SM parameters. The M_R dependence cancels exactly in K = Gamma_D/H|_{T=M_N}. This derivation is shown explicitly and is correct.

However, the correction factor used is kappa(K) proportional to K^alpha with alpha ~ -1.16 from the BDP (2005) power-law fit. At K ~ 5, this fit is at the lower boundary of the "strong washout" regime (K > 3-5). The BDP power-law approximation carries ~20% uncertainty in this regime. The claimed 15% correction (xi^{-0.3} ~ 1.31 at xi ~ 0.43) is within the uncertainty of the fit itself. The paper derives a specific corrected xi ~ 0.49 from this, but the uncertainty on the correction factor means the corrected value should be xi ~ 0.47-0.51, not a point estimate.

**Required work:** Quantify the uncertainty in xi from the ~20% accuracy of the BDP washout fit at K = 5. State the corrected xi as approximately 0.47-0.51 with explicit uncertainty, noting that the fit uncertainty is the dominant source. The convergence of xi_{leptogenesis} ~ 0.49 with xi_{theta*} = 0.47 remains a valid cross-check within this uncertainty range. Estimated difficulty: 1 paragraph addition to Section E.3.3 and Section 2.2.

---

#### Point A1(c): The formula Omega_DM/Omega_b = 1/xi^2 — derivation correctness
**Rating: (C) SOUND**

The derivation in Section E.3.4 is clear and correct. Three factors combine: (1) entropy asymmetry 1/xi^3 from the local photon density difference; (2) washout suppression 1/xi^2 from kappa'/kappa ~ xi^{2alpha} ~ xi^{-2.3} ~ 1/xi^2 at leading order; (3) conversion from eta_ratio to Omega_DM/Omega_b multiplies by xi^3. Product: (1/xi^3) x (1/xi^2) x xi^3 = 1/xi^2. The algebra is shown, dimensionally consistent, and correctly described in the abstract. No revision required.

---

#### Point A1(d): Three scenarios — what distinguishes them?
**Rating: (C) SOUND**

Section 6.1 clearly explains that the three scenarios correspond to three approximation levels: Scenario B is K -> infinity (leading-order washout), Scenario C includes the K=5 BDP correction at fixed omega_b (D/H tension ~2.5sigma disclosed), and Scenario A additionally includes the c=1.986 warp correction (0.7% deviation from conformally coupled). The physical interpretation is given and transparent. No revision required.

---

#### Point A1(e): Is xi = 0.432 a measurement of c_nu = 0.634, or circular reasoning?
**Rating: (A) GENUINE GAP**

Section 2.2 states: "This determination simultaneously fixes the bulk neutrino localization parameter. Paper 6 Section 6.5 derives that xi is related to c_nu via the leptogenesis efficiency; with k=2 from Paper 1, one finds c_nu = 0.634. The single observable Omega_DM/Omega_b therefore encodes... the geometry of neutrino localization." This language implies that the cosmological observation "measures" c_nu = 0.634.

However, the direction of this chain is not established in this paper. For this to be a forward prediction, the chain must run: (i) compactification geometry fixes k = 2 independently; (ii) k = 2 gives c_nu = 0.634 by an analytic formula; (iii) c_nu = 0.634 predicts xi via the leptogenesis efficiency; (iv) xi predicts Omega_DM/Omega_b = 1/xi^2. The paper executes this chain in reverse: it uses the observed Omega_DM/Omega_b to determine xi = 0.432, and then infers c_nu = 0.634.

Furthermore, Appendix E Section E.8 derives c = 1.986 (the warp correction to the conformally coupled value c = 2), not c_nu = 0.634. These two quantities appear to be distinct: c = 1.986 is the bulk neutrino zero-mode parameter in the Randall-Sundrum leptogenesis context, while c_nu = 0.634 is described as coming from Paper 6 Section 6.5 via k = 2. Their relationship is not established in this paper.

**Required work:** Either (a) present the forward derivation (geometry gives k=2, k=2 gives c_nu=0.634 by a stated analytic formula from Paper 6, c_nu=0.634 predicts xi via the leptogenesis efficiency, xi predicts Omega_DM/Omega_b), or (b) remove the "measurement of c_nu" language and replace with a statement that xi = 0.432 is consistent with c_nu = 0.634 if the Paper 6 relation holds, but c_nu is not independently derived here. Additionally clarify whether c = 1.986 (from Section E.8) and c_nu = 0.634 (from Paper 6) are the same parameter. Estimated difficulty: 1-2 pages, requires Paper 6 context.

---

#### Point A2(a): The Z2 conservation theorem — rigor of the proof
**Rating: (B) CLOSABLE GAP**

The proof at Section 2.2 states: because the two sectors are identical under Z2, Delta g_*^{vis} = Delta g_*^{hid} at every transition, so xi_after/xi_before = 1. The equation shown is:

    xi_after / xi_before = (g_{*,vis,before}/g_{*,vis,after})^{1/3} x (g_{*,hid,after}/g_{*,hid,before})^{1/3} = 1

This is mathematically correct as stated, but it conflates two transitions that occur at different cosmic times. The visible QCD crossover occurs at T_vis ~ 150 MeV; the mirror QCD crossover occurs when the visible sector is at T_vis ~ 150/xi MeV (earlier). These are sequential, not simultaneous. The proof needs to handle them sequentially: when only the visible sector undergoes a crossover (Delta g_*^{vis} != 0, Delta g_*^{hid} = 0 at that moment), xi changes temporarily; when the mirror sector undergoes its (equal magnitude) crossover later, xi is restored. The cumulative effect is zero. This is the correct argument but it requires the sequential treatment.

**Required work:** Add 1-2 paragraphs showing the sequential-transition argument: at visible crossover (T_vis = T_QCD), xi -> xi x (g_*^{vis,before}/g_*^{vis,after})^{1/3}; at mirror crossover (T_vis = T_QCD/xi), xi -> xi x (g_*^{hid,after}/g_*^{hid,before})^{1/3} = xi x (g_*^{vis,after}/g_*^{vis,before})^{1/3}; these cancel exactly because Delta g_* is equal by Z2. Accumulated over all thresholds, xi is unchanged. Estimated difficulty: 1 page.

---

#### Point A2(b): Phase transition order — QCD crossover assumption
**Rating: (C) SOUND**

The visible-sector QCD and electroweak transitions are both crossovers in the SM. Under Z2 symmetry, the mirror sector is an exact copy with the same crossover behavior. For crossovers, g* changes smoothly and there is no discrete entropy injection, making the Z2 conservation argument trivially satisfied. The concern about first-order transitions causing differential entropy injection does not apply. Brief explicit statement recommended but not required.

---

#### Point A2(c): If Z2 theorem fails, does the CAMB computation collapse?
**Rating: (C) SOUND**

As argued in A2(b), the crossover nature of the SM phase transitions makes xi trivially conserved regardless of the exact Z2 proof structure. The CAMB computation using a single xi = 0.432 throughout is internally consistent. No revision required.

---

#### Point A3(a): CAMB inputs — the A_s discrepancy
**Rating: (B) CLOSABLE GAP**

Section 2.3 Table 1 lists A_s = 2.1 x 10^{-9}. Appendix A Section A.3 lists A_s = 2.215 x 10^{-9}. These are inconsistent. The hostile-reviewer notes (etc/hostile-reviewer.md item 3) confirm this is a known issue: using A_s = 2.215 x 10^{-9} gives sigma_8 = 0.787 instead of 0.766, propagating to S8 = 0.774 instead of 0.753. This is a 2.8% shift in S8, which affects the quantitative claims about S8 resolution (0.753 vs 0.774 vs observed ~0.77). The paper cannot simultaneously claim S8 = 0.753 matches observations "within 1sigma" if the correct A_s gives S8 = 0.774.

**Required work:** Identify the A_s value actually used in the CAMB run (from compute_age.py) and use it consistently throughout all tables and appendices. If A_s = 2.1 x 10^{-9} is the correct value (non-standard; Planck 2018 best-fit is 2.101 x 10^{-9}), this should be noted. If 2.215 x 10^{-9} was used (this is not a standard Planck value; Planck 2018 gives A_s = (2.101 +/- 0.031) x 10^{-9}), all S8 numbers must be revised. The value 2.215 x 10^{-9} in Appendix A does not correspond to any standard Planck result and appears to be an error. Estimated difficulty: 1 hour of cross-checking; potential revision of S8 numbers if wrong A_s was used.

---

#### Point A3(b): Spectral index n_s
**Rating: (C) SOUND**

n_s = 0.9649 (Planck 2018) is used throughout. Section 2.3 explicitly quantifies the difference from the framework's own prediction (n_s = 0.965 from Paper 6, Delta n_s = 0.0001) as producing shifts below 0.001 — negligible. Transparent and correct. No revision required.

---

#### Point A3(c): Sigma m_nu sensitivity
**Rating: (C) SOUND**

Section 2.3 explicitly states: increasing Sigma m_nu from 0.06 eV to 0.10 eV shifts H_0 by < 0.2 km/s/Mpc and S8 by < 0.01. These numbers are plausible given standard CAMB sensitivities. Correct and transparent. No revision required.

---

### Part B: The Observational Tensions

#### Point B1(a): Derivation of 3.43 xi^4 vs 6.14 xi^4
**Rating: (A) GENUINE GAP**

This is the most significant technical inconsistency in the paper. Section 2.4 states: "The corrected estimate for the mirror photon contribution at z < 2460 — treating them as free-streaming analogously to neutrinos — gives Delta N_eff^{mirror, free-streaming} ~ 3.43 xi^4 rather than 6.14 xi^4 from the fluid formula." Then: "Caution: this estimate is approximate... A proper treatment requires evolving the mirror photon perturbations through the Boltzmann hierarchy as a free-streaming species below z = 2460... This is listed as a pending improvement."

The consequences:
- With the fluid formula (6.14 xi^4): N_eff = 3.31-3.39 at recombination; ACT DR6 tension = 3.5sigma.
- With the free-streaming formula (3.43 xi^4): N_eff ~ 3.16-3.19 at recombination; ACT DR6 tension ~ 2.3sigma.

The paper uses the fluid values in ALL tables and the conclusion, while acknowledging the free-streaming correction is both (a) correct in principle and (b) pending computation. This is an internal inconsistency: the paper's headline tension statistic ("3.5sigma ACT DR6 tension") uses a value the paper itself identifies as an overestimate. The paper cannot simultaneously quote 3.5sigma and acknowledge the correct calculation gives ~2.3sigma without choosing one of them.

Furthermore, the derivation of the coefficient 3.43 is not shown. The paper says it is obtained by "applying the neutrino-like free-streaming conversion factor to the mirror photon degrees of freedom" but does not exhibit this conversion factor or derive the ratio 3.43/6.14 ~ 0.559.

**Required work:** Either (a) complete the full Boltzmann computation switching mirror photons from fluid to free-streaming at z ~ 2460 and report N_eff^{recomb} consistently throughout, or (b) explicitly label all N_eff values as "fluid-formula upper bounds," state the estimated free-streaming corrected range as N_eff ~ 3.16-3.19, and state the ACT tension as "between 2.3sigma (free-streaming estimate) and 3.5sigma (fluid upper bound), with the definitive calculation pending." Also show the derivation of the 3.43 coefficient. Estimated difficulty: (a) ~1 week of CAMB work; (b) ~1 page of revision.

---

#### Point B1(b): Mirror recombination at z ~ 2463 — CAMB implementation
**Rating: (A) GENUINE GAP**

Linked to B1(a). The paper states at Section 2.4: "The current computation approximates the mirror sector as a fluid throughout, which overestimates N_eff as measured by CMB experiments." The N_eff measurement by ACT DR6 is by definition sensitive to free-streaming species at recombination (z ~ 1090). A fluid species and a free-streaming species produce different C_ell signatures — specifically, free-streaming species generate anisotropic stress that damps the damping tail differently, exactly the observable that ACT DR6 uses to measure N_eff. The fluid approximation therefore makes the CAMB N_eff prediction not directly comparable to the ACT DR6 measurement.

**Required work:** Same as B1(a). The resolution is the same computation: implementing the mirror photon-baryon system as a fluid for z > 2460 and switching to a free-streaming Boltzmann hierarchy at z = 2460.

---

#### Point B1(c): The 3.5sigma ACT tension and the degeneracy scan
**Rating: (B) CLOSABLE GAP**

The degeneracy scan described in Section 2.3 ("a systematic scan of the extended parameter space (xi, omega_b h^2, H_0, Omega_m) was performed") does not specify the parameter ranges, step sizes, or tension metric. The paper's conclusion that "no viable degenerate region exists" is stated as a fact. The correct argument — that any xi consistent with Omega_DM/Omega_b = 5.36 gives xi ~ 0.41-0.50, forcing N_eff ~ 3.1-3.4, and that reducing N_eff to 3.046 requires xi -> 0, destroying the dark matter explanation — is actually presented in Appendix I Section I.2 with equations. This is more convincing than the uncharacterized scan.

**Required work:** Replace the degeneracy scan description with the explicit quantitative argument: any xi satisfying Omega_DM/Omega_b = 5.36 +/- 0.5 lies in xi ~ 0.41-0.50, giving N_eff (with free-streaming correction) ~ 3.10-3.40; reducing N_eff to 3.046 requires xi -> 0, giving Omega_DM/Omega_b -> infinity. The framework cannot simultaneously satisfy N_eff ~ 3.046 and Omega_DM/Omega_b ~ 5. This argument is clean, compelling, and eliminates the need for a scan. Estimated difficulty: 2 paragraphs.

---

#### Point B1(d): Mirror BAO signature
**Rating: (B) CLOSABLE GAP**

Section 2.4 identifies the mirror BAO but does not compute the predicted peak location in h/Mpc or the expected amplitude. The formula r_{s,mirror} ~ xi x r_s(z_recomb) is an approximation (the mirror sector sound speed differs from visible because the photon-to-baryon ratio differs by xi^3); a more careful estimate would account for the different R_b = 3 rho_b^{mirror}/(4 rho_gamma^{mirror}) in the mirror sector. The approximate location k_BAO^{mirror} ~ 2pi/(xi x 150 Mpc) ~ 0.10 h/Mpc is straightforward to compute. The amplitude relative to the visible BAO is suppressed by the mirror baryon fraction (~16% of total dark matter), making detection in current surveys unlikely.

**Required work:** Add one paragraph with: (1) the approximate mirror BAO peak location in h/Mpc (with a note on the approximation), (2) an order-of-magnitude amplitude estimate relative to the visible BAO, (3) a statement on whether this is detectable in BOSS DR12 or DESI DR1, and (4) at what future sensitivity it becomes detectable. Estimated difficulty: 1 calculation + 1 paragraph.

---

#### Point B1(e): CMB-S4 falsifiability
**Rating: (C) SOUND**

The paper correctly states that CMB-S4 will test N_eff to +/-0.03. The structural argument in Appendix I Section I.2 that N_eff cannot be dialled away without destroying the dark matter explanation is correct and well-stated. The falsification criterion is unambiguous. This rating is conditioned on resolving the fluid vs. free-streaming inconsistency (B1a/b) — the significance of the CMB-S4 test depends on which N_eff is the true prediction. No additional revision beyond B1(a) and B1(b).

---

#### Point B1(f): BBN consistency
**Rating: (C) SOUND**

The paper correctly tracks N_eff^{BBN} ~ 3.55-3.65 (mirror e+/- contributing at BBN temperatures, T_mirror ~ 0.43-0.47 MeV ~ m_e) vs. N_eff^{recomb} ~ 3.31-3.39 (post-mirror e+/- annihilation). The distinction is explicit and the BBN bound N_eff < 3.7 at 95% CL (Cooke et al. 2018) is correctly applied. The mechanism — mirror e+/- annihilation heating mirror photons, analogously to visible e+/- — is correctly identified. This time-varying N_eff between BBN and recombination is a distinctive signature of this model and is correctly noted. No revision required.

---

#### Point B2(a): Which Hubble tension is resolved?
**Rating: (C) SOUND**

Section 5.2 is appropriately calibrated: "consistent with Planck (67.4 +/- 0.5) at 1-2sigma and with TRGB/CCHP (69.8 +/- 0.6) at < 1sigma, but in 3-4sigma tension with SH0ES Cepheid-based measurements (73.0 +/- 1.0). The framework...does not resolve the SH0ES discrepancy." Section 6.4 explicitly acknowledges the 3.5-4sigma gap with SH0ES. The paper does not claim to "resolve" the Hubble tension in the SH0ES sense, only to be consistent with CMB and intermediate-rung measurements. No revision required.

---

#### Point B2(b): H_0 uplift mechanism and structural link to N_eff
**Rating: (C) SOUND**

Section 5.2 explicitly states the structural link: "both [H_0 and N_eff] are driven by the same xi from the mirror sector. If CMB-S4 measures N_eff = 3.046 +/- 0.03, the H_0 prediction falls back to 67.4 km/s/Mpc." The formula H_0 ~ 67.4 + 6.3 x Delta N_eff is cited. The mechanism (mirror dark radiation elevating the early expansion rate) is correctly described. No revision required.

---

#### Point B2(c): DESI DR3 projection
**Rating: (C) SOUND**

Appendix B Table B4 gives specific H(z) x r_d predictions at five redshifts with DESI DR3 precision estimates and sigma levels. The 3.2-3.4% excess at z = 0.5-0.9 is projected as a 6-7sigma signal at DESI DR3's ~0.5% precision per bin. The physical origin (elevated N_eff + lower Omega_m, not evolving w) and the distinctive redshift dependence are correctly described. No revision required.

---

#### Point B3(a): S8 suppression mechanism
**Rating: (C) SOUND**

The mechanism is double-barrel: elevated N_eff reduces sigma_8 (delays matter-radiation equality), and lower Omega_m reduces S8 = sigma_8 sqrt(Omega_m/0.3) directly. Both effects are fixed by xi before S8 is computed. Neither N_eff nor Omega_m was independently adjusted to hit S8 = 0.753. The chain of determination (Omega_DM/Omega_b -> xi -> N_eff, omega_c h^2 -> CAMB -> S8) is unambiguous and the S8 resolution is a genuine prediction. No revision required.

---

#### Point B3(b): Joint chi^2 comparison
**Rating: (C) SOUND**

Appendix C Section C.6 Table C1 provides a joint chi^2 comparison (H_0, S8, N_eff). The conclusion is honest: with ACT DR6 as N_eff constraint, ΛCDM wins by Delta Delta chi^2 ~ 5-10; with Planck 2018, the framework wins by ~35-40. The paper does not cherry-pick the favorable dataset. No revision required.

---

#### Point B3(c): Euclid S8 projection
**Rating: (C) SOUND**

Appendix C Section C.7 gives specific predictions: S8 = 0.753 (Scenario A) or 0.785 (Scenario B) vs ΛCDM 0.832, testable at 16sigma or 9sigma at Euclid's sigma(S8) ~ 0.005. The falsification criterion is stated clearly. No revision required.

---

### Part C: Leptogenesis and the Baryon Sector

#### Point C1(a): Warp factor suppression — is xi = 0.49 computed or chosen?
**Rating: (A) GENUINE GAP**

Appendix E Section E.7 states explicitly: "A full calculation of this ratio requires the inflaton-brane coupling in the orbifold background... This calculation has not been completed; it is deferred to Paper 6." The framework's introduction states that xi is "set during reheating by warp-factor-suppressed hidden-brane coupling" — but no calculation establishes this. The warp factor e^{k pi} ~ 540 is invoked qualitatively, but what value of xi it predicts has not been derived.

The paper instead determines xi from the cosmological observation Omega_DM/Omega_b = 1/xi^2. This is legitimate (it is a "determination" from a derived law), but the reheating calculation that would predict xi from first principles — completing the chain from geometry to xi — is absent. The language in the abstract and Section 2.2 overstates the current predictive status by suggesting xi is a consequence of the warp factor without a calculation to back this up.

**Required work:** In the abstract and Section 2.2, replace language suggesting xi is fixed by the warp factor (as a current result) with: "xi is determined from the observed Omega_DM/Omega_b via the derived scaling law; the calculation of xi from the reheating dynamics and warp factor is deferred to Paper 6." This is 3-4 sentences of revision but materially affects how the "zero free parameters" claim is evaluated. Estimated difficulty: minimal writing effort.

---

#### Point C1(b): Right-handed neutrino masses — free parameters or computed?
**Rating: (B) CLOSABLE GAP**

M_R ~ 10^15 GeV is cited as "from the CP^2 seesaw scale, Paper 1 Appendix Z." The Davidson-Ibarra bound is satisfied with margin 10^6. For the washout parameter K, M_R cancels exactly (shown explicitly in Section E.3.3). For the CP asymmetry epsilon_i ~ 10^{-6}, the paper cites "standard thermal leptogenesis" — an estimate, not a derivation from the bulk Yukawa matrix. The absolute eta_B calculation is appropriately deferred to Paper 5. However, a brief statement that the bulk Yukawa couplings of Paper 5 are consistent with epsilon ~ 10^{-6} would close the concern about whether the mechanism can in principle reproduce the observed eta_B.

**Required work:** One sentence noting that epsilon ~ 10^{-6} is an order-of-magnitude estimate consistent with the Davidson-Ibarra bound at M_R ~ 10^15 GeV, and that the precise calculation from bulk Yukawa couplings is in Paper 5. Estimated difficulty: 1 sentence.

---

#### Point C1(c): Entropy asymmetry — microphysics vs. observational constraint
**Rating: (B) CLOSABLE GAP**

Appendix E Section E.1 begins: "The theta* constraint requires omega_c h^2 = 0.117, corresponding to eta_ratio ~ 50. We need a mechanism that produces eta_ratio ~ 50." This framing derives the target first and then shows it is achieved. The actual derivation in Section E.3 runs correctly (mechanism -> eta_ratio = 1/xi^5 -> Omega_DM/Omega_b = 1/xi^2). The issue is purely one of presentation: a reader who reads only the opening of Appendix E will conclude the mechanism was reverse-engineered.

**Required work:** Revise Section E.1 to begin from the bulk leptogenesis mechanism. The theta*-required eta_ratio ~ 50 can be noted as a quantitative target that the derivation will be checked against, but it should not be the stated motivation. Estimated difficulty: 1 paragraph.

---

#### Point C1(d): The eta_B calculation
**Rating: (B) CLOSABLE GAP**

The paper's scope declaration (Section E.3.1) is appropriate: the present appendix derives only eta_ratio, not the absolute eta_B. This is stated clearly. However, no verification is offered that the framework's parameters can produce eta_B = 6.1 x 10^{-10} — the scope is limited to the ratio. This is acceptable for a "ratio paper," but a brief statement that eta_B will be computed in Paper 5 and that the expected Yukawa structure is consistent with the Davidson-Ibarra bound would preempt a referee concern.

**Required work:** Optional strengthening. One sentence confirming the mechanism is consistent in principle with the observed eta_B at the order-of-magnitude level. No blocking revision.

---

#### Point C2(a): Normal neutrino mass ordering prediction
**Rating: (C) SOUND**

Appendix I Section I.5 provides a clear derivation from Z_3 orbifold geometry: the Z_3 cyclic permutation symmetry generates a mass matrix with eigenvalue ordering m_1 < m_2 < m_3 (normal ordering). Inverted ordering would require breaking Z_3 or introducing bulk mass hierarchy, neither of which is present. The prediction is robust under the Z_3 symmetry assumption (enforced by the orbifold geometry, not chosen). No revision required.

---

#### Point C2(b): JUNO sensitivity and distinguishing signature
**Rating: (C) SOUND**

The three-experiment corroboration signature is well-defined: JUNO (normal ordering), KATRIN (m_1 -> 0 non-detection), CMB-S4 (Sigma m_nu ~ 0.06 eV). JUNO is already taking data (since August 2025). The joint prediction — normal hierarchy minimum — is unique among viable BSM scenarios. No revision required.

---

### Part D: The Dilaton Appendix

#### Point D1(a): Status of Appendix F — derivation of w_0 = -1
**Rating: (C) SOUND** (with a presentation defect)

Appendix F presents a complete derivation of w_0 = -1, w_a = 0 from the Epstein zero theorem and slow-roll parameter epsilon ~ 10^{-122}. There is no residual discussion of any prior thawing prediction. The derivation is physically correct.

However, Section F.2 contains a manuscript artifact: "Wait — in the Jordan frame for the canonically normalised dilaton:" This must be removed before publication. The calculation gives the correct final result; the self-correction mid-derivation is a documentation artifact that should be cleaned up.

**Required work:** Remove "Wait —" artifact from Section F.2 and present the epsilon calculation as a clean derivation. Estimated difficulty: 5 minutes.

---

#### Point D1(b): DESI dark energy constraints
**Rating: (C) SOUND**

Section F.3 correctly acknowledges the DESI DR2 4.2sigma evidence for w_0 != -1 (w_0 ~ -0.75, w_a ~ -0.75), states the framework predicts w_0 = -1 as "in potential tension with DESI DR2," and acknowledges non-perturbative modifications would be required if DESI DR3 confirms the result. The paper is appropriately candid that this is a potential problem and does not dismiss it. No revision required.

---

## 3. Summary of Issues by Severity

### Genuine Gaps (A) — Require Substantive Revision

1. **A1(e): c_nu = 0.634 "measurement" claim.** The chain ξ → c_nu runs backward (inference from observation, not geometric prediction). Either the forward chain must be shown (geometry → k → c_nu → ξ → Omega_DM/Omega_b) or the language corrected. Additionally, c = 1.986 from Section E.8 and c_nu = 0.634 from Paper 6 appear to be different parameters, and their relationship is not established. [1-2 pages; requires Paper 6]

2. **B1(a)/(b): Fluid vs. free-streaming N_eff inconsistency.** Tables quote N_eff = 3.31-3.39 (fluid, upper bound) but the correct free-streaming value is N_eff ~ 3.16-3.19. The "3.5sigma ACT tension" is overstated; the correct number is likely ~2.3sigma. These two numbers are used interchangeably in the paper without resolution. [Either 1 week of CAMB work to complete the computation, or 1 page of revision clearly labeling the fluid values as upper bounds]

3. **C1(a): ξ = 0.49 from warp factor — calculation absent.** The reheating derivation of ξ from the warp factor is deferred to Paper 6. Language in the abstract and Section 2.2 should reflect this. [3-4 sentences revision]

### Closable Gaps (B) — Addressable in Revision

4. **A1(a): Section E.1 framing** inverts the derivation direction by starting from the theta*-required eta_ratio ~ 50. [1-2 paragraphs revision]

5. **A1(b): BDP fit uncertainty** at K = 5 should be quantified; corrected ξ should be stated as ~0.47-0.51, not a point estimate. [1 paragraph in E.3.3]

6. **A2(a): Z2 conservation proof** needs sequential-transition argument for non-simultaneous phase transitions. [1 page in Section 2.2]

7. **A3(a): A_s value** is inconsistent between Section 2.3 (2.1 x 10^{-9}) and Appendix A Section A.3 (2.215 x 10^{-9}), propagating a ~3% error in S8. [Cross-check against compute_age.py; update all tables to consistent value]

8. **B1(c): Degeneracy scan** should be replaced with the explicit quantitative argument (any ξ from Omega_DM/Omega_b forces N_eff > 3.1, closing only at ξ -> 0 which destroys dark matter). [2 paragraphs]

9. **B1(d): Mirror BAO** location in h/Mpc and amplitude estimate needed. [1 calculation + 1 paragraph]

10. **C1(c): Appendix E Section E.1** should not begin from the theta*-required eta_ratio as motivation. [1 paragraph revision]

### Sound — No Revision Required

11. A1(c): The 1/xi^2 algebra — correct.
12. A1(d): Three-scenario structure — transparent and appropriate.
13. A2(b)/(c): Crossover phase transitions, CAMB consistency — sound.
14. A3(b)/(c): n_s and Sigma m_nu sensitivities — correct and quantified.
15. B1(e): CMB-S4 falsifiability structure — correct (subject to B1a/b resolution).
16. B1(f): BBN N_eff evolution tracking — well-handled.
17. B2(a)/(b)/(c): Hubble tension characterization — not overstated, mechanistically correct.
18. B3(a)/(b)/(c): S8 mechanism and projections — correct.
19. C1(b): K computation with M_R cancellation — shown explicitly, correct.
20. C2(a)/(b): Normal ordering prediction and JUNO signature — well-motivated.
21. D1(b): DESI w != -1 tension acknowledged — honest and appropriate.

---

## 4. Recommendation to Editors

**Recommendation: Major Revision**

The paper presents a technically substantive framework with genuine predictive content and an unusually transparent CAMB parameter audit. The 1/xi^2 scaling law is derived (not assumed), the three-scenario presentation is scientifically honest, and the paper appropriately acknowledges its primary tension with ACT DR6. The S8 resolution and θ* near-match are non-trivial quantitative results.

Three issues constitute the conditions for major revision:

**First and most urgent (gaps B1a/b):** The paper's headline tension statistic — "3.5sigma from ACT DR6" — uses a fluid-formula N_eff that the paper itself acknowledges is an overestimate at the recombination epoch measured by ACT DR6. The correct free-streaming calculation would give N_eff ~ 3.16-3.19 and a tension of approximately 2.3sigma with ACT DR6. The paper cannot simultaneously use 3.5sigma in its tables and acknowledge the free-streaming correction reduces this. Either complete the free-streaming CAMB computation (strongly preferred) or clearly label all N_eff values as upper bounds and state the 2.3sigma estimate. This affects the paper's central claim about its status relative to current CMB data.

**Second (gap A1e):** The claim that the cosmological measurement of xi = 0.432 "simultaneously measures" the GUT-scale parameter c_nu = 0.634 requires a forward derivation (geometry → c_nu → ξ) that is not present in this paper. As written, the chain runs backward (observation → ξ → c_nu). Additionally, c = 1.986 from Appendix E Section E.8 and c_nu = 0.634 from Paper 6 appear to be different parameters; their identification should be established. This must be resolved to avoid a misleading claim.

**Third (gap A3a):** The A_s value in Section 2.3 (2.1 x 10^{-9}) is inconsistent with Appendix A Section A.3 (2.215 x 10^{-9}). The wrong A_s propagates a ~3% error in S8, which matters for the paper's central claim of S8 = 0.753 matching weak lensing surveys within 1sigma. The actual value used in the CAMB computation (from compute_age.py) must be stated consistently throughout.

The manuscript presentation artifact ("Wait —" in Appendix F Section F.2) must also be removed.

All other gaps are closable with paragraph-level additions and do not require new calculations. If the three major issues and the closable gaps above are addressed, the paper would merit publication. The framework makes specific, falsifiable predictions at a precision level uncommon in BSM cosmology, and the experimental roadmap in Appendix I provides a clear decade-scale test program.
