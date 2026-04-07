# Cross-Paper Consistency Review: The QG5D Framework (Papers 1–7)

**Reviewer role:** Senior theoretical physicist, cross-series consistency referee
**Date:** 2026-04-07
**Status of series:** All seven papers revised following individual referee reports; gap-responses filed; source files updated.
**Scope:** This review assesses cross-paper consistency of the revised versions.

---

## 1. Executive Summary

The seven-paper QG5D series has been substantially improved by the individual revision rounds. Several per-paper genuine gaps (the 0.7% string-tension overclaim in Paper 5, the dilaton inflation misidentification in Paper 6, the "GUT condition as derived output" overclaim in Paper 7) have been corrected honestly and with appropriate hedging. The series, viewed as a whole, is more internally honest than most multi-paper theoretical programs of comparable ambition.

However, four cross-paper tensions survive the individual revisions. Two are genuine inconsistencies (A-rated) requiring coordinated revision before any submission. Two are resolvable tensions (B-rated) requiring explicit clarifying text.

**The three most critical issues before any paper in the series is submitted, in priority order:**

**Priority 1 — The ξ origin story is mechanically unresolved (B1c, Parts B and C).** Paper 6 Section 6 attempts to derive ξ ≈ 0.49 from reheating dynamics but reaches ξ ~ 0.84 at its last quantitative step, with the final value appealing to "full thermal history" without a completed calculation. Paper 2's ξ is determined by inverting the Ω_DM/Ω_b observational ratio. These approaches have not been shown quantitatively consistent. Paper 6 §6.5 already contains the honest statement that only ξ ~ 0.3–0.9 is established; the abstract must match it.

**Priority 2 — The Casimir scale assignment in Paper 4 vs. Paper 6 is contradictory as stated (A1c, Part A).** Paper 4 assigns the S¹ Casimir energy to the cosmological constant (a constant). Paper 6 identifies the same S¹ Casimir energy as V(R) = +c/R⁴, a runaway scalar field potential. These are physically distinct. The reconciliation — that V(R₀) at the frozen value equals ρ_Λ — is available but requires Paper 6 Appendix A's dilaton-freezing argument to be imported into Paper 4 §7.21.

**Priority 3 — The R-dependence of Papers 4 and 5's numerical predictions is not acknowledged (D1b, Part D).** Paper 7 establishes r₃² = n₁/(2c_R) ∝ R⁻¹, so M_GUT ∝ R^{1/2}, m_H ∝ R^{1/2}, and τ_p ∝ R². Papers 4 and 5 give numerical predictions (m_H ~ 125 GeV, √σ ≈ 440 MeV) without stating this R-dependence. Paper 7's gap-response acknowledges it but the source files do not yet reflect this.

**Overall recommendation:** The series is submittable after addressing Priorities 1–3. The papers should not be submitted independently until the cross-paper fixes described below are implemented.

---

## 2. Point-by-Point Findings

---

### PART A: The Finiteness Result and Its Scope

---

**A1(a): Geometry mismatch — single S¹ vs. CP² × S² × S¹**

**Rating: (B) RESOLVABLE TENSION**

Paper 1's Theorem S.1 is for M⁴ × S¹. Paper 4 Appendix C correctly explains the mechanism — the S¹ spectral zeta evaluates to 2ζ(−2j) = 0 (trivial zeros), while the CP² and S² spectral zetas are nonzero because shifted-square eigenvalues mix ζ values at different arguments. Paper 4 does not claim finiteness of the full CP² × S² sector; it claims the S¹ sector is UV-finite (Paper 1) and the CP² × S² sector generates a nonzero stabilization potential.

**What is needed:** Paper 4 Appendix C needs one paragraph explicitly stating: (i) finiteness of the S¹ Casimir uses Theorem K.1 of Paper 1 directly; (ii) the CP² and S² contributions are finite by the Epstein-Terras theorem (their pole at s = L/2 > 0 is never reached at the needed s ≤ 0); (iii) both sectors are UV-finite but only the S¹ sector evaluates to zero — the CP² and S² sectors generate nonzero potentials. Papers requiring revision: Paper 4 Appendix C (one paragraph); Paper 5 §3 (citation of Paper 1 Appendix L).

---

**A1(b): Non-abelian finiteness — gauge-gravity mixing diagrams**

**Rating: (B) RESOLVABLE TENSION**

Paper 1 Appendix L correctly establishes that SU(N) KK towers on S¹ have the same spectral structure as U(1), so Theorem K.1 applies. Gauge-gravity mixing diagrams are not explicitly addressed. The argument that polynomial vertex mass-dependence (which drives the Epstein structure) extends to mixed loops is plausible but unstated.

**What is needed:** One paragraph in Paper 1 Appendix L or Paper 4 §8 explicitly extending the Epstein structure argument to gauge-gravity mixing diagrams, with the honest note that this has not been separately computed (same status as the L ≥ 3 factorization gap). Papers requiring revision: Paper 1 Appendix L (one paragraph); Paper 5 §3 (one citation).

---

**A1(c): The S¹ Casimir energy — cosmological constant or dilaton potential?**

**Rating: (A) GENUINE INCONSISTENCY**

This is the most precisely identifiable cross-paper inconsistency in the series.

Paper 4 §7.21: "The Scherk-Schwarz SUSY breaking on S¹/Z₂ derives ρ_Λ = (2.25 meV)⁴ with zero free parameters." Paper 4's three-scale Casimir hierarchy explicitly identifies S¹ → dark energy Λ (a constant).

Paper 6 §2.1: "The dilaton potential V(R) = +c/R⁴ — the Casimir energy of bulk fields on the e-circle, exact to all perturbative orders." Paper 6 Appendix A shows this is a runaway function: V'(R) = −4c/R⁵ ≠ 0, no minimum.

The reconciliation is available: the "cosmological constant" of Paper 4 is V(R₀) = c/R₀⁴ evaluated at the kinematically frozen value R = R₀, where the freezing is established by Paper 6 Appendix A (ΔR/R₀ ~ 3 × 10⁻³⁰ per Hubble time). But Paper 4 presents ρ_Λ as directly derived from the Casimir energy without invoking this argument. A reader of Paper 4 alone sees a constant cosmological constant derived from the S¹ Casimir. A reader of Paper 6 alone sees a runaway potential. Neither paper's self-contained presentation explains how both are simultaneously true.

Additionally, Paper 4's claim w₀ = −1 now depends on the Paper 6 Appendix A corrected calculation (ΔR/R₀ ~ 3 × 10⁻³⁰, replacing the earlier erroneous 10⁻⁵²). This dependency is not stated.

**What is needed:** Paper 4 §7.21 must be revised to state: (i) the S¹ Casimir energy produces V(R) = c/R⁴, not a constant; (ii) the observed cosmological constant is V(R₀) at the frozen value R₀ ~ 10 μm; (iii) the frozen-dilaton argument justifying w₀ = −1 is established in Paper 6 Appendix A (forward reference). Paper 6 §2.1 should add a backward cross-reference noting that Paper 4's "S¹ Casimir → Λ" is V(R₀) at frozen R₀. Papers requiring revision: Paper 4 §7.21 (one to two paragraphs); Paper 6 §2.1 (one sentence). Estimated difficulty: Moderate — careful wording required.

---

**A1(d): The R³ counterterm in 11D vs. 5D**

**Rating: (B) RESOLVABLE TENSION**

Paper 1's two-loop finiteness is for 5D gravity. The 11D counterterm structure (R⁴ at one loop in 11D SUGRA) is different. Paper 1 is not claiming to eliminate all UV divergences in 11D SUGRA — it claims the 4D effective theory from integrating out KK modes is UV-finite. These are different claims that should be stated explicitly.

**What is needed:** Paper 4 §8 should add one sentence clarifying that finiteness claims apply to the 4D effective theory from KK integration, not to the full 11D SUGRA counterterm structure.

---

**A1(e): "Exact to all orders" for the Coleman-Weinberg effective potential vs. S-matrix**

**Rating: (B) RESOLVABLE TENSION**

The background field method guarantees that the effective action (including the effective potential) has the same UV structure as the S-matrix amplitudes, because both are governed by the spectral representation of the heat kernel. The Epstein-vanishing mechanism applies to both.

**What is needed:** Paper 6 §2.1 should add one sentence: "The Epstein-vanishing mechanism applies to the spectral zeta function of the kinetic operator, which governs both the S-matrix amplitudes (Paper 1) and the Coleman-Weinberg effective potential via the same heat kernel representation."

---

**A2(a): Paper 3 UV completion cites Paper 4's geometry**

**Rating: (B) RESOLVABLE TENSION**

Paper 3 Appendix A's "M-theory identification" commits to M-theory on M⁴ × CP² × S² × S¹/Z₂, whose SM field content is established in Paper 4. This is a real dependency. Paper 3's information-loss resolution operates at the 5D e-circle level (Papers 1–2) and does not require Paper 4 for its core argument, but the UV completion claim does.

**What is needed:** Paper 3 Appendix A §A.3 should explicitly state: "The M-theory identification is fully established only when Paper 4 (SM field content) and Paper 7 (tadpole cancellation) are accepted. Papers 3 and 4 are companion submissions establishing the same 11D geometry from two different directions."

---

**A2(b): Bubble-of-nothing instability**

**Rating: (C) CONSISTENT**

Correctly distributed across Papers 1 (Appendix J: antiperiodic fermion suppression + Casimir barrier, S_CDL ≫ 10³⁰), 3 (cites Paper 1), and 7 (CP² × S² moduli stabilized by flux, not subject to the same S¹ instability). No cross-paper inconsistency.

---

**A2(c): M-theory UV completion requires Papers 4 and 7**

**Rating: (B) RESOLVABLE TENSION**

Same as A2(a), but emphasizing the Paper 7 dependency (tadpole cancellation, Freed-Witten anomaly). Paper 3 Appendix A should state the conditional nature of the UV-complete claim.

---

### PART B: The ξ Parameter Across Papers

---

**B1(a): Are Paper 2 and Paper 6 computing the same quantity?**

**Rating: (B) RESOLVABLE TENSION**

The two derivations operate in different logical directions and are consistent in principle: Paper 2 determines ξ from Ω_DM/Ω_b via the leptogenesis scaling law; Paper 6 explains the physical mechanism placing ξ in the range 0.3–0.9. The problem is presentation — Paper 2 §2.2 cites Paper 6 as providing "the origin of ξ," overstating Paper 6's result.

**What is needed:** Paper 2 §2.2 should revise its citation of Paper 6 to read: "Paper 6 §6 identifies the physical mechanism that places ξ in the range 0.3–0.9; the precise value ξ = 0.49 is determined in this paper from the Ω_DM/Ω_b scaling law."

---

**B1(b): Washout corrections**

**Rating: (C) CONSISTENT**

Paper 2's washout (K ≈ 5 from m_ν = 50 meV; BDP efficiency function) corrects the leptogenesis scaling law at the epoch of leptogenesis. Paper 6's entropy correction from differential QCD confinement is a different physical effect at a later epoch. These are additive, non-competing corrections. The gap-response for Paper 2 (A1(b)) provides the correct, corrected K ≈ 5 calculation with the M_N-cancellation demonstrated explicitly.

---

**B1(c): Direction of logical flow of ξ**

**Rating: (A) GENUINE INCONSISTENCY**

Paper 2 abstract: "fits zero free parameters to CMB data... Ω_DM/Ω_b (which fixes ξ through the scaling law)."

Paper 6 abstract: "the precise value ξ = 0.49 (Paper 2) emerges from the full numerical thermal history."

These statements create a circular presentation. Paper 6's §6.4 final paragraph gives ξ = 0.79 after bulk neutrino decays, then appeals to unquantified "entropy from phase transitions" to reach 0.49 — this calculation is incomplete. The abstract's claim that ξ = 0.49 "emerges" from the thermal history is therefore premature.

The honest statement is: Paper 2 determines ξ = 0.49 from the Ω_DM/Ω_b ratio; Paper 6 explains the physical mechanism producing ξ ~ 0.3–0.9. Paper 6 §6.5 already contains this honest assessment; the abstract must be brought into alignment.

**What is needed:** Paper 6 abstract must be revised to remove the implication that ξ = 0.49 precisely is derived from the mechanism. The 0.79 → 0.49 step is an unresolved calculation gap that should be labeled as such, with the full two-sector Boltzmann simulation identified as needed future work. Papers requiring revision: Paper 6 abstract (one sentence); Paper 6 §6.2–6.5 (remove overstatement that ξ = 0.49 is derived). Estimated difficulty: Light editing.

---

**B1(d): N_eff consistency**

**Rating: (C) CONSISTENT**

Paper 2 computes N_eff = 3.31–3.39 from ΔN_eff = 6.14 × ξ⁴. Paper 6 defers N_eff calculation to Paper 2. Both use the same ξ and the same formula. The tension with ACT DR6 (N_eff = 2.86 ± 0.13) is an experimental tension acknowledged by both papers, not a cross-paper inconsistency.

---

### PART C: The Inflation Model Conflict

---

**C1(a): T_reh robustness to inflaton identity**

**Rating: (C) CONSISTENT — with important caveat requiring a calculation**

Paper 6 §4.0 correctly argues that both the dilaton and G₄ axion couple gravitationally with Γ ~ m_inf³/M_Pl². Paper 7's r ≈ 0.001 constrains H_inf ~ 6 × 10¹³ GeV (from r = (2/π²)(H_inf/M_Pl)²), within a factor of 6 of the assumed 10¹³ GeV. T_reh scales as H_inf^{3/2}/M_Pl, so T_reh would shift by ~15, remaining below M_N ~ 10¹⁴ GeV (non-thermal leptogenesis path intact).

**What is needed:** Paper 6 §4.0 should add three equations computing T_reh self-consistently using Paper 7's r ≈ 0.001 to fix H_inf ~ 6 × 10¹³ GeV, and confirm T_reh ~ (1–2) × 10¹⁰ GeV remains below M_N.

---

**C1(b): Leptogenesis efficiency with G₄ inflaton**

**Rating: (C) CONSISTENT**

The leptogenesis CP asymmetry ε ~ 10⁻⁶ comes from Paper 4's Z₃ Yukawa phases, independent of the inflaton. The inflaton-to-neutrino coupling changes parametrically (gravitational vs. axion-gauge kinetic) but at the same Planck-suppressed order. No inconsistency.

---

**C1(c): ξ origin story with G₄ inflaton profile**

**Rating: (B) RESOLVABLE TENSION**

Paper 6 §6.2 computes initial brane energy deposition from the dilaton wavefunction f(y) = e^{−αk|y|}, giving ρ_hid/ρ_vis = e^{−4kπ} ~ 10⁻¹¹ (warp-factor suppressed). With the G₄ axion as inflaton, the axion is the zero-mode of A₃ along compact 4-cycles — it has a flat bulk profile, not a warped one. The §6.2 initial energy ratio becomes ρ_hid/ρ_vis ≈ 1 (equal energy deposition on both branes). This changes the starting point of the §6.4 gravitational thermalization calculation, which then dominates the determination of ξ anyway. The final ξ ~ 0.3–0.9 range is not invalidated; the intermediate steps need updating.

**What is needed:** Paper 6 §6.2 should note: "With the G₄ flux axion as inflaton (Paper 7), the axion has a flat bulk profile and the warp-factor suppression in §6.2 does not apply. For the G₄ axion, ρ_hid/ρ_vis ≈ 1 at the end of reheating, and gravitational thermalization (§6.4) dominates the determination of ξ." This revision strengthens the §6.4 argument.

---

**C1(d): Predictions belonging to Paper 6**

**Rating: (C) CONSISTENT after revision**

Paper 6 correctly eliminates dilaton inflation (ε = 32/3 ≫ 1), defers G₄ axion inflation to Paper 7, and makes no quantitative n_s/r claims. The four headline results (T_reh, ξ mechanism, EWPT, dilaton future) are all inflaton-model-independent as presented. No revision needed on this point.

---

### PART D: Moduli Stabilization and the Ordering Problem

---

**D1(a): What Papers 1–6 assume about R**

**Rating: (C) CONSISTENT**

Paper 7 Theorem U claims all observables are R-independent. Checking against Papers 1–6: the core high-precision observables (α₃/α₂, sin²θ_W, n_s, r, Ω_DM/Ω_b, N_eff) are genuinely R-independent. Dimensionful observables with absolute-scale predictions (m_H, KK resonance masses) depend on R through r₃(R), but Paper 4 explicitly acknowledges this via Open Problem OC-2. Paper 7's abstract claim "all observables are R-independent" should be revised to distinguish dimensionless from dimensionful observables (see D1(b)).

---

**D1(b): m_H, M_GUT, and √σ depend on R through r₃(R)**

**Rating: (B) RESOLVABLE TENSION — critical for submission**

Paper 7 establishes r₃² = n₁/(2c_R) ∝ R⁻¹ (since c_R ∝ R). Therefore:
- M_GUT = r₃⁻¹ ∝ R^{1/2}
- r₂ = ρ r₃ ∝ R^{−1/2} (since ρ = √3/2 is R-independent)
- M_KK = r₂⁻¹ ∝ R^{1/2}
- m_H ∝ M_KK ∝ R^{1/2} (gauge-Higgs unification)
- τ_p ∝ M_X⁴ ∝ R²

Paper 7's gap-response explicitly acknowledges this, but the Paper 4 and Paper 5 source files do not state the R-dependence of their predictions. A referee of Papers 4 or 5 reading Paper 7 will notice this immediately.

The important physics consequence: m_H ~ 125 GeV and dark energy scale (2.3 meV)⁴ are related through R — both are determined by R_obs, whose value is the CC problem. Paper 4 §7.21's "zero free parameters" claim for dark energy is accurate given R = R_obs, but the coincidence that m_H ~ 125 GeV at the same R_obs as dark energy is a genuine structural observation that deserves to be stated explicitly.

**What is needed:** Paper 4 §6.7 should state: "Since r₂ ∝ R^{−1/2} (Paper 7, §3.2), M_KK ∝ R^{1/2}, and the Higgs mass depends on R. The prediction m_H ~ 125 GeV is consistent with the observed R_obs ≈ 10.1 μm (determined by dark energy matching), whose underivability is established in Paper 7 Theorem U." Paper 5 §3.2.2 should add an analogous two-sentence note. Paper 7 §3.6.3 should revise "all observables are R-independent" to "all dimensionless observables are R-independent; dimensionful observables (M_GUT, m_H, KK resonance masses) depend on R through r₃(R)." Papers requiring revision: Papers 4, 5, 7 (one paragraph each or less).

---

**D1(c): Logical ordering of Papers 4, 5, and 7**

**Rating: (B) RESOLVABLE TENSION**

Papers 4 and 5 use r₃ by fixing it from α_s(M_Z) (observational input). Paper 7 derives r₃ from flux stabilization. Both give the same r₃ — this consistency should be stated explicitly with cross-references in both directions.

**What is needed:** Papers 4 §3.3 and 5 §3.2 should add forward references to Paper 7 §3.2 noting that r₃ is independently confirmed by flux stabilization. Paper 7 §3.5 should note consistency with Papers 4 and 5.

---

**D1(d): The cosmological constant — environmental selection in Paper 4?**

**Rating: (B) RESOLVABLE TENSION**

Paper 4 §7.21 presents the dark energy prediction without noting that R_obs — on which it depends — is declared underivable by Paper 7 Theorem U. The prediction is a consistency relation at R = R_obs, not a derivation of R_obs.

**What is needed:** Paper 4 §7.21 should add: "The zero-parameter nature of the dark energy derivation should be understood as a consistency relation: given the observed R_obs (whose value is the CC problem, Paper 7 Theorem U), the Casimir energy c/R_obs⁴ precisely reproduces ρ_Λ^obs with no further free parameters."

---

### PART E: Gauge Structure Consistency

---

**E1(a): sin²θ_W ≈ 0.232 and α₃ = α₂ — consistent?**

**Rating: (C) CONSISTENT**

Paper 4 §7.1 correctly derives sin²θ_W = 3/8 at GUT scale → 0.231 at M_Z, under GUT normalization assumption. Paper 7's α₃ = α₂ from n₂/n₁ = −17/9 is consistent. Both papers acknowledge that GUT normalization is assumed. No inconsistency in the numerics. The "geometric" content is that α₃ = α₂ is derived from CP² × S² geometry; sin²θ_W then follows from standard SU(5) running under GUT normalization.

---

**E1(b): α₁ is not fixed by flux — sin²θ_W requires α₁ = α₂ = α₃**

**Rating: (B) RESOLVABLE TENSION**

Paper 7 establishes α₃ = α₂ from flux. But α₁ = 1/(2πM_Pl² R²) depends on R (Theorem U). The "complete GUT unification" α₃ = α₂ = α₁ is not derived from the framework's flux physics — only two of the three couplings are equalized by the flux. The sin²θ_W prediction assumes α₁ = α₂ at the GUT scale (GUT normalization), which is equivalent to three-coupling unification, which is not derived.

**What is needed:** Papers 4 §7.1 and 7 §6 should both note: "Only α₃ = α₂ follows from flux quantization. α₁ depends on R (Theorem U). The sin²θ_W prediction assumes GUT normalization for α₁, equivalent to asserting three-coupling unification — a standard SU(5) assumption that the framework motivates but does not derive."

---

**E1(c): M_X and proton lifetime consistency**

**Rating: (B) RESOLVABLE TENSION**

M_X ∝ R^{1/2} (from D1(b)), so τ_p ∝ R². Paper 4's prediction τ_p ~ 10³⁴–10³⁶ years at M_X ~ 10¹⁵ GeV is consistent with observation for R = R_obs. Paper 4 §7.3 should note this R-dependence explicitly.

---

### PART F: The Confinement–GUT Scale Connection

---

**F1(a): Scale consistency — r₃ in Papers 4 and 5**

**Rating: (C) CONSISTENT**

The apparent dimensional catastrophe (σ at GUT scale ≪ 440 MeV) is explicitly resolved by Paper 5 §3.2.2 through the QCD beta function running over 13 orders of magnitude. The CP² geometry sets the GUT-scale boundary condition α_s(M₃) = 1/25; dimensional transmutation then gives Λ_QCD = 190 MeV; the string tension at confinement scale is √σ ~ Λ_QCD × 2.3 ~ 437 MeV. Both Papers 4 and 5 use the same r₃, consistently defined. No inconsistency.

---

**F1(b): QCD running explicitly performed**

**Rating: (C) CONSISTENT**

Paper 5 §3.2.2 explicitly performs the RG running with b₀ = 7 (two-loop MS-bar, N_f = 3), three-loop running factor 2.3, and quotes Λ_QCD = 190 MeV (12% below PDG central value 210 MeV — noted as a 1.4σ discrepancy within expected one-loop accuracy over 13 orders of magnitude). The revised paper correctly characterizes the result as a leading-order formula with ~25% systematic uncertainty, not a precision prediction.

---

### PART G: The Mirror Sector Across Papers

---

**G1(a): Mirror BBN and N_eff^{BBN} vs. N_eff^{recomb}**

**Rating: (B) RESOLVABLE TENSION**

Paper 2's time-varying N_eff is correctly computed: N_eff^{BBN} ≈ 3.55–3.65, falling to N_eff^{recomb} = 3.31–3.39 after mirror e± annihilation. Paper 6 §7's mirror BBN discussion should reference this distinction — the mirror helium yield Y_p^{mirror} is governed by N_eff^{BBN}, not N_eff^{recomb}.

**What is needed:** Paper 6 §7 should add one paragraph: "Mirror BBN proceeds at T_mirror ≈ ξ × T ≈ 0.43–0.47 MeV (Paper 2), when N_eff^{BBN} ≈ 3.55–3.65. The mirror helium yield uses this BBN-epoch value; the lower N_eff^{recomb} = 3.31–3.39 quoted in Paper 2's CMB predictions reflects mirror e± annihilation occurring after BBN."

---

**G1(b): Mirror baryons = dark matter**

**Rating: (C) CONSISTENT**

Paper 2 §2.2 and Appendix E are explicit: Ω_DM = Ω_{mirror baryons}. The scaling law Ω_DM/Ω_b = 1/ξ² is a ratio of mirror baryons to visible baryons. No confusion between mirror baryons and non-baryonic dark matter. Paper 6 §7 is consistent.

---

## 3. Parameter Audit Table

| Parameter | Paper 1 | Paper 2 | Paper 3 | Paper 4 | Paper 5 | Paper 6 | Paper 7 | Consistent? |
|-----------|---------|---------|---------|---------|---------|---------|---------|-------------|
| **ξ** | — | 0.432–0.49 (from Ω_DM/Ω_b) | — | — | — | ~0.3–0.9 mechanism; "0.49 (Paper 2)" in abstract | — | **INCONSISTENCY A (B1c):** Paper 6 abstract implies ξ = 0.49 derived from mechanism; §6.5 limits claim to ξ ~ 0.3–0.9 |
| **r₃ (CP² radius)** | — | — | — | r₃⁻¹ ~ 10¹⁵ GeV (from α_s(M_Z)) | same r₃ | — | r₃² = n₁/(2c_R) ∝ R⁻¹; r₃/l₁₁ ≈ 0.003 | **TENSION (D1b):** Papers 4, 5 use r₃ without stating R-dependence |
| **M_X (GUT scale)** | — | — | — | M_X ~ 10¹⁵ GeV | M₃ ~ 10¹⁵ GeV | — | M_GUT = r₃⁻¹ ∝ R^{1/2} | **TENSION (D1b):** M_X is R-dependent; not stated in Papers 4, 5 |
| **T_reh** | — | — | — | — | — | 5 × 10⁹ GeV | — | Internally consistent; needs Paper 7 H_inf check (C1a) |
| **R (S¹ radius)** | 12–21 μm (dark energy matching) | — | 12 μm | uses α_s to fix r₃ | — | R₀ ~ 21 μm | R_bare ~ l_Pl (Theorem U); R_obs ≈ 10.1 μm | **CONSISTENT:** all use R_obs from dark energy; Paper 7 characterizes R_bare vs. R_obs as CC problem |
| **N_eff** | 3.31–3.39 (Paper 2) | 3.31–3.39 (CAMB) | — | — | — | deferred to Paper 2 | — | **CONSISTENT** |
| **n_s, r** | — | — | — | — | — | no claim (deferred to Paper 7) | n_s ≈ 0.967, r ≈ 0.001 | **CONSISTENT** |
| **ρ = r₂/r₃** | — | — | — | √3/2 (from α₃/α₂ = 1, Appendix C) | — | — | √3/2 (from n₂/n₁ = −17/9 F-flat) | **CONSISTENT:** same value from two independent arguments |
| **m_H** | — | — | — | ~125 GeV for M_KK ~ 1–2.5 TeV (Open Problem OC-2) | — | — | r₂ = ρ r₃ ∝ R^{−1/2}; m_H ∝ R^{1/2} | **TENSION (D1b):** m_H is R-dependent; labeled OC-2 but R-dependence not stated |
| **√σ** | — | — | — | — | [410, 510] MeV (25% uncertainty) | — | — | **CONSISTENT within Paper 5**; depends on r₃ via α_s running (F1a sound) |
| **sin²θ_W** | — | — | — | 0.232 (GUT normalization assumed) | — | — | α₃ = α₂ from flux → 0.231 at M_Z | **CONSISTENT numerically; TENSION (E1b):** α₁ R-dependent, three-coupling unification not derived |
| **S¹ Casimir (c/R⁴)** | c = ρ_Λ R₀⁴ | — | — | "S¹ Casimir = dark energy (constant)" | — | V(R) = +c/R⁴ (runaway) | — | **INCONSISTENCY A (A1c):** Paper 4 presents V(R₀) as constant; Paper 6 presents V(R) as scalar field; reconciliation requires Paper 6 App. A to be imported into Paper 4 |
| **Σm_ν** | 0.06 eV | 0.06 eV | — | — | — | — | — | **CONSISTENT** |
| **K (washout)** | — | K ≈ 5 (m_ν = 50 meV; M_N cancels) | — | — | — | entropy correction from QCD confinement (different epoch) | — | **CONSISTENT:** different physical corrections at different epochs |

**Summary count: 2 genuine inconsistencies (A), 12 resolvable tensions (B), 11 consistent (C).**

---

## 4. Recommended Submission Order

**Phase 1 — Revise first, before any submission:**
- Paper 7: revise §3.6.3 to distinguish dimensionless from dimensionful R-independence; add explicit R-dependence of M_GUT.
- Paper 6: revise §6.2 for G₄ axion flat profile; revise abstract to remove premature ξ = 0.49 claim from mechanism.
- Paper 4: revise §7.21 (A1(c) fix); revise §6.7 (D1(b) fix); revise §7.1 (E1(b) note on α₁).

**Phase 2 — Submit together:** Papers 1 and 2. These establish the M⁴ × S¹ sector and the cosmological predictions. Paper 2's ξ determination is from Ω_DM/Ω_b — the dependency chain is clean.

**Phase 3 — Submit together, after Phase 2:** Papers 3 and 4. Paper 3 UV completion depends on Paper 4 geometry. Paper 4 depends on Papers 1 (finiteness) and 7 (flux stabilization).

**Phase 4 — Submit after Phase 3:** Papers 5, 6, and 7. Paper 5 depends on Paper 4's r₃. Paper 6 depends on Paper 7 for inflaton identification. Paper 7 depends on Paper 4 for GUT condition.

**Papers that cannot be submitted before others are revised:**
- Paper 3 cannot be submitted before Paper 4 is revised.
- Papers 4 and 5 should not claim specific numerical predictions without the Paper 7 R-dependence caveat.
- Paper 6 cannot be submitted with its current abstract claiming ξ = 0.49 emerges from the mechanism.

---

*Report prepared following complete reading of all seven abstracts, referee reports, gap-responses, and all source sections specified in the referee prompt: Paper 1 Appendices S and K; Paper 2 §§2–7 and Appendix E; Paper 3 Appendix A; Paper 4 §6, Appendix C; Paper 5 §3; Paper 6 §§3, 4, 6, Appendix A; Paper 7 §§3, 5, Appendix A. All cross-references are to section numbers as found in the revised source files.*
