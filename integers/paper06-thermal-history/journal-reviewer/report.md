# Referee Report — Paper 6: "The Complete Thermal History from Inflation to Dark Energy"

**Journal:** Physical Review D / JCAP (as submitted)
**Reviewer run:** r01

---

## 1. Executive Summary

**Recommendation: Major Revision**

This paper presents the temporal narrative of a novel 11-dimensional cosmological framework, assembling results from Papers 1–4 and deriving four new results: the reheating temperature, non-thermal leptogenesis pathway, the origin of the brane temperature asymmetry ξ, and the far future of the dilaton. The paper has substantially improved its internal housekeeping since the previous draft: it explicitly retracts the earlier dilaton-as-inflaton identification, self-corrects the ε_eff ~ 10⁻⁵² dimensional error, retracts the w₀ ≠ −1 Goldberger-Wise prediction, and acknowledges the LHC tension on M_KK. These are substantive corrections.

However, several issues sufficient to block publication remain. Most critically: (1) the dilaton fifth-force argument relies on a Hubble-friction screening mechanism that is not a standard field-theoretic result and is not derived; (2) the leptogenesis calculation achieves agreement with η_B only by parameter-tuning (Br ~ 10⁻² at the upper end) without independent determination of the resonant mass splitting; (3) the Z₂ Conservation Theorem carries an unresolved circularity in the c_ν/ξ derivation; (4) the paper uses inconsistent values of ξ (ξ = 0.49 in the abstract and Section 6.1, ξ = 0.432 in Section 6.5) derived from the same observational input, with no reconciliation.

---

## 2. Point-by-Point Findings

---

### PART A: THE DILATON

---

#### A1(a): Canonical Field Normalization — ε_eff Dimensional Error

**Rating: (C) SOUND** (correction already made)

The previous draft claimed ε_eff = 8/M_5³ ~ 10⁻⁵², interpreting a dimensionful quantity as a dimensionless number. The current Appendix A §§A.2–A.3 corrects this explicitly. Starting from the 5D KK reduction kinetic term L_kin = (3M_Pl²/4R²)(∂R)², the canonical field σ = (√3 M_Pl/2) ln(R/R₀) is correctly defined. The potential in canonical field space is V(σ) = (c/R₀⁴) exp(−4√(2/3) σ/M_Pl), giving ε = 32/3. This computation is standard and correct.

The physical drift rate ΔR/R₀ ~ H₀R₀ ~ 3 × 10⁻³⁰ is correctly derived in §A.3.2 via the slow-drift balance between Hubble friction and the potential gradient. The key suppression is the ratio H₀R₀ ~ (10⁻³³ eV)(0.1 eV⁻¹) ~ 10⁻³⁴. The ε = 32/3 and ΔR/R₀ ~ 3 × 10⁻³⁰ results are not contradictory: ε measures slope in canonical σ-space; ΔR/R₀ measures physical drift of R. The large kinetic prefactor (3M_Pl²/4R²) absorbs the steep canonical gradient, leaving R nearly stationary. Section A.4 explains this clearly.

No further action required.

---

#### A1(b): Quantum Corrections to the Dilaton Mass

**Rating: (B) CLOSABLE GAP**

Section A.6 derives the dilaton effective mass from V''(R₀): |m| = √27.6 H₀ ≈ 5.3 H₀ ~ 5 × 10⁻³³ eV. This uses only the classical Casimir potential curvature.

The paper does not address one-loop quantum corrections from SM matter fields coupling to the dilaton through L_int = (σ/M_Pl) φ T^μ_μ. These generate a Coleman-Weinberg contribution to m_φ² of order (g_SM/4π)² × M_KK² ~ 10⁻² × (0.1 eV)² ~ 10⁻⁴ eV² — roughly (10⁻² eV)², which is ~10⁶⁰ times larger than m_φ² ~ H₀² ~ (10⁻³³ eV)². If such corrections are unsuppressed, the frozen-dilaton picture collapses. The paper invokes the Epstein zeta zero theorem (Theorem K.1) to kill higher-loop corrections to the KK Casimir sum, but this theorem governs the spectral zeta of bulk kinetic operators, not the Coleman-Weinberg corrections from SM matter running in dilaton-coupled loops.

What is needed: A one-paragraph argument showing SM matter loops are either killed by the Epstein mechanism (with explicit extension of Theorem K.1 to this case), further suppressed by (M_KK/M_Pl)², or screened by another mechanism. Difficulty: 1 paragraph of argument or 1 page of calculation.

---

#### A1(c): Fifth-Force Constraints — Hubble-Friction Screening

**Rating: (A) GENUINE GAP**

Section 4.5 argues that Hubble friction suppresses the dilaton's response to local perturbations on sub-Hubble timescales, giving an effective PPN suppression factor t_obs/t_H ~ 2.5 × 10⁻¹⁰ and |γ − 1|_eff ~ 1.7 × 10⁻¹⁰, safely within the Cassini bound.

This argument is not physically correct as field theory. The dilaton equation of motion is:

    R̈ + 3H Ṙ + (2R³/3M_Pl²) V'(R) + (σ/M_Pl) ρ_local = 0

The Hubble term 3H Ṙ represents cosmological damping of the homogeneous background field — it governs the global drift rate. A local matter density ρ_local sources the dilaton locally via the Green's function of the scalar wave equation. For an ultra-light scalar with m_φ ≪ (solar-system scale)⁻¹, the local Green's function is essentially that of a massless scalar, and the local response is NOT suppressed by H₀ × t_obs. The Cassini experiment probes the local gradient of the dilaton in the solar system, not its cosmological drift rate. These are decoupled in linear perturbation theory at sub-Hubble scales.

Standard screening mechanisms (chameleon, Vainshtein, symmetron) suppress fifth forces through environment-dependent effective masses or derivative self-couplings — neither of which is the mechanism claimed here. The paper cites Paper 1 Appendix I as providing the full PPN derivation, but Paper 1 is unpublished and the specific result is not summarized here.

What is needed: Either (a) a derivation of the local Green's function in the post-Newtonian limit showing the coupling is suppressed by H₀t_obs (which would require explicitly solving the linearized scalar-tensor perturbation equation), or (b) an explicit citation of where Paper 1 Appendix I provides this with the numerical bound, or (c) invocation of a standard screening mechanism that applies to this dilaton and is shown to satisfy the Cassini bound. The current t_obs/t_H dimensional argument does not constitute a derivation.

Difficulty: If Paper 1 Appendix I already has the PPN calculation: 1 page summary. If the mechanism requires new development: 1 paper.

---

#### A1(d): Duration of Freezing — Self-Consistency of m_φ and H_∞

**Rating: (C) SOUND**

Section A.6 finds |m| ~ 5.3 H₀ > H_∞ ~ 0.83 H₀, so the dilaton is not in the overdamped regime in the de Sitter future — it oscillates. The ODE analysis shows Δ = (3H_∞/2)² − 19.0 H_∞² = −16.75 H_∞² < 0, giving damped oscillations with decay constant e^{−3H_∞t/2}. The amplitude decays exponentially. A damped oscillator (underdamped) is stable — perturbations decay to zero. The earlier (incorrect) draft used V = −c/R⁴ giving V'' < 0 and a growing mode. With the correct sign V = +c/R⁴ and V'' > 0, the stability analysis is sound.

Self-consistency is satisfied: the dilaton mass (~5H₀) is derived from the same Casimir potential that determines H_∞ via ρ_Λ = c/R₀⁴ = 3H₀²M_Pl²Ω_Λ. The circular check closes: |m|² = 40H₀²Ω_Λ = 40 × 0.69 × H₀² ~ 27.6 H₀², and H_∞² = Ω_Λ H₀² ~ 0.69 H₀², giving |m|² ~ 40 H_∞². Hubble damping rate 3H_∞ < |m|, so the system is underdamped but stable.

No action required.

---

#### A2(a): "Exact to All Perturbative Orders" — Scope of Theorem K.1

**Rating: (B) CLOSABLE GAP**

The Epstein zeta zero theorem kills corrections to the spectral zeta function of the bulk kinetic operator. Section 2.1 correctly extends this to the FRW background by noting curvature corrections are of order (H₀R₀)² ~ 10⁻⁶⁸, negligible. However, the claim "exact to all perturbative orders" should be qualified to note it covers corrections from the KK spectral sum (bulk field loops) and does not automatically cover: (i) Coleman-Weinberg corrections from dilaton-matter couplings (see A1(b) above), (ii) corrections to the dilaton kinetic term from off-diagonal KK metric components. These are distinct classes of corrections not obviously governed by the same spectral zeta.

What is needed: A two-sentence qualification distinguishing corrections to the Casimir vacuum energy (killed by Theorem K.1) from corrections to the dilaton kinetic term and matter coupling (which require separate treatment, deferred to Paper 1). Difficulty: 1 paragraph.

---

#### A2(b): Sign of the Casimir Energy

**Rating: (C) SOUND**

Section 2.1a correctly determines the sign. With n_b = 5 (graviton KK DOF) and n_f = 12 (three bulk Weyl neutrinos × 4 DOF per Dirac fermion), the Casimir density ρ ∝ −(n_b − 7/8 × n_f) = −(5 − 10.5) = +5.5 > 0. The 7/8 ratio from anti-periodic (fermionic) vs. periodic (bosonic) boundary conditions is standard. The sign V = +c/R⁴ is correct, and the retraction of the earlier V = −c/R⁴ error is appropriate.

No action required.

---

#### A2(c): The Dine-Seiberg Runaway Problem

**Rating: (B) CLOSABLE GAP**

The potential V = +c/R⁴ has no minimum; V'(R) = −4c/R⁵ < 0 (decreasing function). Section 2.4 correctly acknowledges R₀ is "kinematically frozen at initial conditions," not dynamically stabilized. However, the paper does not clarify a subtle but important point: for V = +c/R⁴ with c > 0, the gradient force on R is −∂V/∂R = +4c/R⁵ > 0, which pushes R toward SMALLER values (R → 0, the 10D collapse direction), not toward decompactification (R → ∞). This is opposite to the usual Dine-Seiberg runaway (where the dilaton runs to infinite coupling, corresponding to R → ∞ in some parametrizations). With V decreasing as R increases, the force on R is restoring (toward smaller R) — Hubble friction prevents this collapse just as effectively as it prevents decompactification.

Section A.6 shows V''(R₀) = +20c/R₀⁶ > 0, confirming the frozen point is stable under small perturbations — consistent with this interpretation.

What is needed: One paragraph clarifying the direction of the gradient force (toward R → 0, not R → ∞) and noting that Hubble friction stabilizes R₀ against collapse, not against decompactification. This removes potential confusion with the standard Dine-Seiberg problem. Difficulty: 1 paragraph.

---

### PART B: INFLATION AND THE ξ PARAMETER

---

#### B1(a): Journal Submission Standard — Superseded Inflation Model

**Rating: (C) SOUND** (issue resolved)

Section 3 now explicitly states "The dilaton is NOT the inflaton" (ε = 32/3, §3.1). Section 3.3 states "No inflationary predictions (n_s, r values) are made in this paper." The abstract does not cite the old n_s = 0.965, r = 0.03 values as predictions. The one-page timeline (§12) defers all inflationary predictions to Paper 7.

The journal submission concern is resolved. A residual issue: Paper 7 remains "in preparation," meaning the inflationary scale H_inf ~ 10¹³ GeV assumed in §§4–5 is unverified. Section 4.0 notes a factor-of-6 uncertainty in T_reh if Paper 7's H_inf differs. The paper should state the inflaton scale assumption as an explicit caveat rather than a fixed input.

No action required on the submission standard issue itself; see B1(c) for the H_inf uncertainty propagation.

---

#### B1(b): r = 0.03 Prediction vs. Current Data

**Rating: (C) SOUND** (not applicable)

The revised Paper 6 makes no r = 0.03 prediction. The old dilaton slow-roll value is discarded. No tensor-to-scalar ratio comparison is required.

No action required.

---

#### B1(c): Independence of Leptogenesis from Inflation Model

**Rating: (B) CLOSABLE GAP**

Section 4.0 correctly argues inflaton-independence at the parametric level: both dilaton and G₄ axion decay gravitationally with Γ ~ m_inf³/M_Pl². However, §4.0 derives H_inf ~ 6 × 10¹³ GeV from Paper 7's r ≈ 0.001, shifting T_reh by a factor ~4 to (1–2) × 10¹⁰ GeV. The leptogenesis calculation in §5 uses T_reh = 5 × 10⁹ GeV specifically. Since n_N/s ~ Br × T_reh/M_N is directly proportional to T_reh, a factor-of-4 increase propagates directly to η_B. The paper already shows η_B is delicately balanced between Br ~ 2.8 × 10⁻³ (giving η_B ~ 1.7 × 10⁻¹⁰) and Br ~ 10⁻² (giving η_B ~ 6 × 10⁻¹⁰). A factor-of-4 larger T_reh would ease this tension — but this should be stated explicitly.

What is needed: Redo the leptogenesis summary table at T_reh = 1 × 10¹⁰ GeV (from Paper 7's H_inf ~ 6 × 10¹³ GeV) to show η_B is still consistent. Alternatively, carry T_reh as an explicit uncertainty. Difficulty: 1 paragraph of scaling argument.

---

#### B2(a): Z₂ Conservation Theorem — Mirror QCD Confinement

**Rating: (B) CLOSABLE GAP**

The theorem in §6.4 is logically sound: under exact Z₂ symmetry, both sectors undergo the same g_* steps at their respective threshold temperatures, so ξ_after/ξ_before = 1 at every transition. However, the argument assumes each sector has the same number of active quark flavors at its QCD transition temperature.

For the visible sector, QCD confinement occurs at T_QCD ~ 155 MeV. All three light quarks (m_u ~ 2 MeV, m_d ~ 5 MeV, m_s ~ 95 MeV) satisfy m < T_QCD, so three flavors are active.

For the hidden sector at ξ = 0.432, the hidden-sector QCD transition occurs at T_QCD' = ξ × 155 MeV ~ 67 MeV. The mirror strange quark has mass m_s' = 95 MeV (by Z₂ symmetry) > T_QCD' ~ 67 MeV. The mirror strange quark is therefore NOT active at the hidden-sector QCD transition — it has already been integrated out. The hidden sector has only two active quark flavors at its transition, versus three in the visible sector. This gives a different g_* step and breaks the conservation.

The paper does not address this. The statement "same particle content, same g_* values at corresponding thresholds" is not self-evidently true when the quark masses are close to the threshold temperature.

What is needed: A quantitative check of the N_f = 3 vs. N_f = 2 g_* step difference at T_QCD' ~ 67 MeV. The difference in g_* drops (10.5 for N_f=3 QCD vs. 9.0 for N_f=2 QCD at the lattice-corrected values) would shift ξ by ~ (10.5/9.0)^{1/3} × (9.0/10.5)^{1/3} ≈ 1 (first order, the effect partly cancels), but the precise value must be computed. Difficulty: 1 page.

---

#### B2(b): g_* Steps — Proof vs. Assumption

**Rating: (B) CLOSABLE GAP**

The logical structure of the theorem is correct but not fully spelled out. The key point — that the Z₂ theorem holds for any initial ξ₀ ≠ 1 because non-simultaneity of the two sectors' transitions is irrelevant — should be stated explicitly. What matters is that each sector's own g_* step at its own threshold is the same function of its own particle content, which is Z₂-identical to the other sector's. The ratio ξ = T'/T evolves as ξ_after = ξ_before × (drop_hidden/drop_vis)^{1/3} = ξ_before × 1 = ξ_before.

What is needed: One sentence: "The theorem holds for any ξ₀ because the Z₂ symmetry acts on the particle content independently of the temperature ratio; the g_* evolution of each sector depends only on its own particle content, not on the other sector's current temperature." Difficulty: 1 sentence.

---

#### B2(c): Old Chain vs. Theorem — Formal Retraction

**Rating: (B) CLOSABLE GAP**

Section 6.4 correctly identifies the error in the old thermal-history chain. However, it does not formally retract the numerical values (0.14 → 0.84 → 0.79 → 0.49) that may have been used in companion papers. The old chain gives ξ = 0.49 after all corrections; the theorem gives ξ = const at the leptogenesis value. These are numerically inconsistent.

What is needed: A formal one-sentence retraction: "The thermal-history chain (ξ_0 → 0.84 → 0.79 → 0.49) presented in earlier drafts of this paper is formally retracted. The correct result, established by the Z₂ Conservation Theorem, is ξ = const throughout thermal history at its leptogenesis value." Difficulty: 1 sentence.

---

#### B2(d): Theorem Hypotheses — Derivation of Z₂ Mirror Symmetry

**Rating: (B) CLOSABLE GAP**

The Z₂ mirror symmetry of the hidden and visible sectors is invoked as a hypothesis of the theorem but is not derived from the brane construction. It should be derived: the S¹/Z₂ orbifold Z₂ action maps y → −y, interchanging the two fixed-point branes. Since the 5D gauge fields and matter are placed in the same 5D multiplets, both branes obtain the same gauge group and particle content from the Kaluza-Klein reduction. This is a geometric consequence of the orbifold, not an independent assumption.

What is needed: One paragraph citing the S¹/Z₂ geometry and Papers 1 and 4 as the source of the mirror symmetry, noting it is a consequence of the orbifold action on the 5D spectrum. Difficulty: 1 paragraph.

---

#### B2(e): Paper 2 CAMB Runs at ξ = 0.49 vs. ξ = 0.432

**Rating: (A) GENUINE GAP**

This is the most significant internal consistency problem in the paper series. The abstract of this paper states: "The precise value ξ = 0.49 is determined in Paper 2 from the Ω_DM/Ω_b observational ratio." Section 6.1 also quotes ξ = 0.49 from Paper 2. But Section 6.5 of this paper derives ξ = 0.432 from the same observational ratio Ω_DM/Ω_b = 5.36 via ξ = 1/√5.36 = 0.432.

These cannot both be correct. The discrepancy is 12%, which propagates to ~25% in ξ² and ~50% in ξ⁴, affecting N_eff, dark matter density, and all CMB predictions from Paper 2. Paper 2's CAMB runs used ξ = 0.49; if the correct value is ξ = 0.432, those runs must be redone.

The paper provides no formula reconciling the two values, no statement of which is correct, and no assessment of the impact on Paper 2's predictions. The Z₂ Conservation Theorem would actually make this WORSE: if ξ is conserved (constant throughout thermal history), then whatever value Paper 2 used should be the leptogenesis-epoch value from §6.5. But §6.5 gives 0.432, not 0.49.

What is needed: An explicit resolution. Either: (a) The 1/ξ² law is ξ = 1/√(Ω_DM/Ω_b) exactly, giving ξ = 0.432, and Paper 2's value of 0.49 incorporated a washout correction that is now removed (in which case Paper 2 must be updated); or (b) The 1/ξ² law is approximate, and ξ is determined by a more complex formula that gives 0.49, in which case §6.5 should not use 0.432 as the exact value. Until this is resolved, the cross-paper consistency claim of the series is not supported.

Difficulty: Requires identifying the exact formula for ξ vs. Ω_DM/Ω_b and potentially updating Paper 2.

---

#### B3(a): Bulk Neutrino Wavefunction — Z₂ Orbifold Boundary Conditions

**Rating: (B) CLOSABLE GAP**

The wavefunction f_L(y) ∝ e^{(2−c_ν)k|y|} is the standard Grossman-Neubert result for bulk fermion zero modes on S¹/Z₂. The |y| makes the profile Z₂-even, consistent with even boundary conditions. For c_ν > 1/2 without brane-localized mass terms, the standard Neumann-type condition ∂_y f_L|_{y=0,πR} = 0 is automatically satisfied. This is a known result but should be cited explicitly.

What is needed: One sentence: "The even profile e^{(2−c_ν)k|y|} automatically satisfies the Neumann boundary conditions at y = 0 and y = πR on the S¹/Z₂ orbifold in the absence of brane-localized mass terms (Grossman & Neubert 2000), consistently with the fermion spectrum of Paper 4." Difficulty: 1 sentence.

---

#### B3(b): Circularity of c_ν and ξ — Logic Runs Backwards

**Rating: (A) GENUINE GAP**

Section 6.5 states: "What this section claims. (1) A derivation, not an estimate. The value ξ = 0.432 is derived from a single fundamental parameter of the 5D theory: the bulk neutrino mass c_ν = 0.634."

This description reverses the logical order of the derivation. The paper's own computation (equations in §6.5) takes ξ = 0.432 as input (from Ω_DM/Ω_b = 5.36) and solves for c_ν:

    c_ν = 1/2 + ln(1/ξ⁴) / (4kπ) = 0.634

This is c_ν derived FROM ξ. The claim "ξ is derived from c_ν" would require c_ν to be determined independently — but it is not. The 5/2 topological identity is invoked as a potential independent handle on c_ν, but the paper itself notes that exact closure of 5/2 requires either m_ν = 48.8 meV (4.7σ below current central value) or R₀ = 9.84 μm — neither of which is confirmed. The 5/2 identity gives m_ν^{5D}/M_KK = 5/2 ~ 2.5, which at the Z-pole gives 2.57 (3% discrepancy from running). This is a consistency check, not an independent determination of c_ν.

The result is physically interesting: c_ν = 0.634 is a natural O(1) parameter that consistently explains the observed dark matter abundance AND is approximately consistent with a topological mass ratio. But the paper overstates the logical status of this result. "A derivation" implies an independent prediction; what has been done is a consistency analysis.

What is needed: Reframe §6.5 item (1) as: "A consistency result: the observed Ω_DM/Ω_b = 5.36 constrains c_ν = 0.634. This parameter is natural (within (0,1) for bulk fermion localization) and is approximately consistent with the topological mass ratio m_ν^{5D}/M_KK = 5/2 from CP² topology, confirmed to ~3% at the Z-pole. The consistency between two a priori independent quantities (the dark matter abundance and the neutrino mass ratio) is a non-trivial self-consistency check, but not yet an independent prediction until c_ν is derived from first principles." Difficulty: 1 paragraph of reframing.

---

#### B3(c): The 5/2 Identity — Paper 6's Claim vs. Papers 4 and 7

**Rating: (B) CLOSABLE GAP**

Section 6.5 presents the topological identity m_ν/m_KK = 5/2 = χ(CP²) − c₂_eff/2 as a "connection claim" citing Papers 4 and 7. The attribution is appropriate. The concern is that the conditions for exact closure (m_ν = 48.8 meV at 4.7σ tension, or R₀ = 9.84 μm) are stated but not flagged prominently as significant observational tensions.

At the Z-pole the ratio is 2.57, departing from 5/2 by ~3%. This is framed as a "running effect" recoverable at M_GUT, but the Yukawa running from M_GUT to M_Z is itself a significant calculation (involving the full MSSM RGE structure) that is not presented here. The 4.7σ tension with the current neutrino mass central value (if m_ν = 48.8 meV vs. the Planck-preferred value ~60 meV) is a testable tension that should be highlighted, not buried in a closing paragraph.

What is needed: Promote the 4.7σ neutrino mass tension to a prominent observational prediction/tension, and frame it as "if the 5/2 identity holds exactly, CMB-S4 + DESI will either confirm it (if m_ν ~ 49 meV) or falsify it (if m_ν ~ 60 meV)." This makes the 5/2 claim falsifiable and therefore scientifically meaningful. Difficulty: 1 paragraph.

---

#### B3(d): m_ν^{5D} = 1.27 M_KK vs. 5/2 = 2.5 — Notation Confusion

**Rating: (B) CLOSABLE GAP**

The text states "m_ν^{5D} = c_ν × k = 0.634 × 2 = 1.268 M_KK" while also citing the 5/2 identity m_ν/m_KK = 2.5. These are numerically different (1.268 ≠ 2.5) and the paper does not explain the relationship.

The likely resolution: c_ν × k = 1.268 is the 5D bulk mass parameter M_ν = c_ν k (in units where M_KK = 1), while the 5/2 identity refers to the ratio of the 4D Majorana mass M_R (obtained from integrating out the KK tower after seesaw) to M_KK. These are different physical quantities — c_ν parameterizes bulk localization, while M_R is the 4D right-handed neutrino mass. The near-equality "1.268 ≈ 5/2" alluded to in the text (implying 1.268 ~ 1.27 ~ 5/2 ≈ 2.5) conflates a factor-of-2 discrepancy with a "numerical coincidence."

What is needed: Explicit separation of notation: c_ν = 0.634 (dimensionless localization parameter), M_ν^{5D} = c_ν k = 1.268 M_KK (5D bulk mass parameter), M_R (4D Majorana mass from seesaw, predicted to be 5/2 × M_KK from Paper 4 topology). Remove the implication that 1.268 ≈ 5/2. Difficulty: 1 paragraph of clarification.

---

#### B4(a): Three Constraints on R — Over-Determination

**Rating: (B) CLOSABLE GAP**

Section 6.5 claims ξ⁴ is "one of the three simultaneous constraints that determine R," deferred to Paper 9 §4d. The three constraints (dark energy ρ_Λ = c/R₀⁴, dark matter ξ⁴ correction, 5/2 neutrino mass identity) are asserted to be mutually consistent but the consistency is not shown.

The 0.86% shift from ξ⁴ is straightforward: the mirror sector adds ξ⁴ to the Casimir constant (c_eff = c_vis × (1 + ξ⁴)), shifting R_A by (1 + ξ⁴)^{1/4} ≈ 1 + ξ⁴/4 = 1 + (0.432)⁴/4 ≈ 1 + 0.0087, approximately 0.87% — consistent with the stated 0.86%. This is a perturbative correction to R, not a fixing mechanism, and does not conflict with Paper 7's Theorem U (which presumably states perturbative geometry alone cannot fix R to the observed value from first principles, not that no perturbative corrections exist).

What is needed: Display the two-line derivation of the 0.86% shift (ξ⁴/4) explicitly. Clarify that the three "constraints" are one primary determination (ρ_Λ observational constraint) plus two consistency checks (ξ⁴ correction and 5/2 identity), not three independent fixing mechanisms. Paper 9 §4d can develop the full argument. Difficulty: 2 lines of algebra plus 1 clarifying sentence.

---

### PART C: REHEATING AND LEPTOGENESIS

---

#### C1(a): Decay Width — Dilaton Mass vs. T_reh Tension

**Rating: (C) SOUND**

The apparent tension from the referee prompt does not exist in the revised paper. The inflaton is the G₄ flux axion with m_inf ~ H_inf ~ 10¹³ GeV. The dilaton does not reheat the universe — it is frozen and does not oscillate. The reheating calculation uses m_inf ~ 10¹³ GeV (the axion mass at the end of inflation), not the dilaton mass m_φ ~ 5H₀ ~ 5 × 10⁻³³ eV. The two masses refer to entirely different fields. The derivation in §§4.1–4.2 is correct given this inflaton identification.

No action required.

---

#### C1(b): Leptogenesis Efficiency — Branching Ratio Determination

**Rating: (B) CLOSABLE GAP**

The central GNRRS estimate in §5.2a gives Br ~ 2.8 × 10⁻³, yielding η_B ~ 1.7 × 10⁻¹⁰ — a factor of 3.5 below observed. Agreement with η_B = 6 × 10⁻¹⁰ requires Br ~ 10⁻² (upper end of estimate) AND resonant factor ~80. Both are adjusted upward from their computed central values to achieve the observed η_B. The paper acknowledges this explicitly.

The resonant enhancement factor of ~80 requires mass splitting |M₂ − M₁|/M₁ ~ a few × 10⁻³, which "should be confirmed from the Z₃ geometry calculation in Paper 4, §7.5.4." Without this confirmation, the leptogenesis calculation is consistent with observations only by parameter adjustment, not by first-principles prediction.

What is needed: Either (a) derive the mass splitting from Z₃ geometry (Paper 4 §7.5.4) and show it gives the required resonant factor, or (b) reframe the leptogenesis result as an order-of-magnitude estimate consistent with observations at natural parameter values, not a precise prediction. Difficulty: Depends on the complexity of the Z₃ mass-splitting calculation in Paper 4.

---

#### C1(c): Washout Factor

**Rating: (C) SOUND**

The derivation K = m̃/(10⁻³ eV) = 50 and η_L = 0.26 from the strong-washout formula are correct standard results. The seesaw identity m̃ = m_ν = 0.05 eV for a democratic Yukawa matrix, giving K = 50, is straightforward. The Buchmuller-Di Bari-Plumacher formula for the efficiency in strong washout is applied correctly.

No action required.

---

#### C1(d): Three Routes to ξ — Mutual Consistency

**Rating: (A) GENUINE GAP**

This duplicates and reinforces B2(e) as a separate finding from the leptogenesis section. The abstract and §6.1 give ξ = 0.49 (from Paper 2). Section 6.5 derives ξ = 0.432 (from the same Ω_DM/Ω_b = 5.36). Section 6.6 gives ξ ~ O(0.3–0.9) from the warp-factor mechanism. Three different claimed routes to ξ give different numbers, and no reconciliation is provided.

The Z₂ Conservation Theorem adds urgency: if ξ is conserved through thermal history (the theorem's conclusion), then the reheating-epoch value from §6.6 (order-of-magnitude, mechanistic) should equal the leptogenesis value from §6.5 (ξ = 0.432) should equal the CMB-epoch value from Paper 2 (ξ = 0.49). The 12% discrepancy between 0.432 and 0.49 is not within the "O(0.3–0.9)" range claimed for the mechanical uncertainty — it is a specific numerical discrepancy between two apparently exact calculations.

What is needed: Identical resolution as B2(e) — an explicit formula for ξ vs. Ω_DM/Ω_b that reconciles the two values, and a statement of whether Paper 2's CMB predictions need revision.

---

### PART D: THE ELECTROWEAK PHASE TRANSITION

---

#### D1(a): Why First-Order — The KK Gauge Boson Mechanism

**Rating: (C) SOUND**

Section 8.1a correctly identifies the BSM mechanism: the Higgs is the GHU Wilson-line angle θ_H, coupled to KK gauge bosons with M_KK ~ 1 TeV. These contribute a cubic thermal correction −c₃ T |m³(θ_H)| to the thermal effective potential, absent in the SM for m_H > 72 GeV but present in GHU due to the KK tower contributions. The cubic term creates a potential barrier between θ_H = 0 and θ_H = θ₀, making the transition first-order. This is the standard GHU first-order EWPT mechanism in the Hosotani framework. The derivation is attributed to Paper 4 §7.12 with a correct qualitative summary.

No action required.

---

#### D1(b): GW Signal Amplitude

**Rating: (C) SOUND**

Section 8.3a applies the standard Espinosa-Konstandin-No-Servant (2010) formulae correctly. With α = 0.12, β/H_* = 32, v_w = 0.92, T_* = 900 GeV, the peak frequency f_sw ~ 6 mHz and amplitude h²Ω_GW ~ 5 × 10⁻¹³ are correctly computed. The comparison to LISA sensitivity ~ 3 × 10⁻¹² at 6 mHz is honest: the central prediction is ~6 times below the LISA threshold, with the uncertainty range straddling detectability. The binary test is correctly formulated as a falsifiable prediction.

No action required.

---

#### D1(c): T_c ~ 1 TeV vs. the EW Scale

**Rating: (C) SOUND**

Section 8.2a correctly explains the factor-of-10 enhancement: T_c ~ M_KK/g ~ 1 TeV/0.65 ~ 1.5 TeV (consistent with T_c ~ 1 TeV) because the transition is driven by KK gauge bosons entering the thermal sum at T ~ M_KK, not by the Higgs VEV v = 246 GeV. This is a direct consequence of M_KK ~ 1 TeV ≫ v.

No action required.

---

#### D1(d): LHC Constraints on M_KK ~ 1 TeV

**Rating: (B) CLOSABLE GAP** (acknowledged and partially addressed)

Section 8.5 honestly acknowledges M_KK ~ 1 TeV is excluded by LHC at the quoted bounds (KK W± → ℓν below ~3 TeV; KK Z → ℓ⁺ℓ⁻ below ~4 TeV). The paper proposes two resolutions: (a) M_KK ~ 3–4 TeV with T_c ~ 3–4 TeV and GW peak at ~20–40 mHz; (b) fermion localization suppression. The GW parameters in §8.3 assume M_KK ~ 1 TeV and should be explicitly labeled as preliminary estimates.

What is needed: The GW spectrum table should carry a footnote: "Parameters computed for M_KK = 1 TeV; LHC constraints require M_KK ≳ 3 TeV, shifting T_c → 3 TeV, f_peak → 20 mHz, with α and β/H_* to be recomputed at this mass scale." A brief two-line rescaling of h²Ω_GW for M_KK = 3 TeV would help. Difficulty: 1 paragraph.

---

### PART E: THE FUTURE AND DARK ENERGY

---

#### E1(a): de Sitter Stability — Swampland Conjecture

**Rating: (C) SOUND**

Section 11.5 correctly shows V'(R₀) ≠ 0 (the dilaton is on a slope, not a minimum), and in canonical field space |∇_σ V| = 4√(2/3) V/M_Pl with c = 4√(2/3) ≈ 3.3, satisfying the first de Sitter swampland condition with an O(1) constant. The de Sitter-like expansion is not a vacuum state but a kinematically frozen field configuration on a slope, which is precisely what the swampland conjecture is designed NOT to exclude (it forbids metastable V' = 0 minima, not slow-drift states with V' ≠ 0).

This is an elegant feature of the framework and the analysis is correct.

No action required.

---

#### E1(b): H_∞ < H₀ and the de Sitter Equation of State

**Rating: (C) SOUND**

H_∞ = H₀√Ω_Λ ≈ 0.83 H₀ < H₀ is the standard ΛCDM asymptotic Hubble rate. In ΛCDM with w = −1, H decreases from H₀ as matter dilutes and asymptotically approaches H_Λ = H₀√Ω_Λ from above. The usage H_∞ in §A.6 for the de Sitter approximation during dark energy domination (H ≈ H_∞ = const) is correct and standard. The claim H_∞ < H₀ is consistent with ΛCDM behavior.

No action required.

---

## 3. Recommendation to Editors

**Recommendation: Major Revision Required**

The paper is conceptually original, internally well-organized, and honest about its limitations. The authors have corrected multiple errors from earlier drafts, which is commendable. However, three issues must be resolved before publication:

**Issue 1 (Critical — ξ inconsistency):** The paper simultaneously reports ξ = 0.49 (abstract, §6.1, from Paper 2) and ξ = 0.432 (§6.5, derived here from the same Ω_DM/Ω_b ratio). These two values differ by 12% and lead to ~50% differences in ξ⁴, which affects N_eff, the dark matter abundance calculation, and all CMB predictions from Paper 2. The Z₂ Conservation Theorem requires ξ to be constant throughout history — which value is it? The paper cannot claim internal consistency across the series without resolving this discrepancy. (Points B2(e), C1(d))

**Issue 2 (Critical — fifth-force mechanism):** The claim that Hubble friction suppresses the dilaton's fifth-force coupling by the ratio t_obs/t_H does not follow from the linearized scalar-tensor field equations. The Cassini constraint is one of the strongest precision tests of scalar-tensor gravity. Without a proper PPN Green's function derivation or invocation of a standard screening mechanism, the fifth-force claim is unsubstantiated. (Point A1(c))

**Issue 3 (Significant — circular derivation framing):** The claim that "ξ is derived from c_ν" is logically backwards. The paper derives c_ν = 0.634 from the observed ξ = 0.432, not the reverse. The physical result — that a natural bulk fermion localization parameter is consistent with both the dark matter abundance and a topological neutrino mass ratio — is interesting and worth publishing. But it should be framed as a consistency result, not an independent derivation. (Point B3(b))

A paper that resolves these three issues, addresses the leptogenesis parameter uncertainty (C1(b)), and clarifies the m_ν^{5D}/M_KK notation (B3(d)) would be suitable for publication in PRD or JCAP with minor additional revision.

---

*Report prepared for reviewer run r01. Previous run archived at integers/paper06-thermal-history/reviewer-runs/r00/.*
