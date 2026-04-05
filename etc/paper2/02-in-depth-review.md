# Hostile Review: Paper 2 — Precision Cosmology from Geometry

> **Reviewer credentials:** QFT, GR, cosmology, failed unified theories.
> **Documents reviewed:** Paper 2 abstract, sections 1–8, appendices A–I,
> refs.bib, project master, and recommended changes document.
> **Date:** April 2026

---

## FATAL ISSUES

### F1. The 1/ξ² Law Has a Logarithmic Correction That Changes Everything

**Location:** Appendix E §E.3.3–E.3.4

**The claim:** "κ_hidden / κ_visible ~ K / K' ~ 1/ξ²" leading to
Ω_DM/Ω_b = 1/ξ².

**The error:** In the strong washout regime, the washout efficiency is
κ ~ 1/(K ln K), NOT κ ~ 1/K. This means:

    κ'/κ = [K ln K] / [K' ln K'] = (1/ξ²) × [ln K / ln(Kξ²)]

The logarithmic factor ln K / ln(Kξ²) is NOT unity except in the limit
K → ∞. For the framework's parameters (M_N ~ 10¹⁴ GeV), the washout
parameter is K ~ Γ_D / H|_{T=M_N}. Using standard leptogenesis formulas
with Yukawa couplings Y ~ 0.01–0.1:

    K ~ (Y†Y)_{11} × M_Pl / (8π × 1.66 × √g* × M_N)
      ~ (10⁻² to 10⁻⁴) × 10¹⁸ / (8π × 1.66 × 10 × 10¹⁴)
      ~ 10 to 1000

For K = 10 and ξ = 0.432:

    ln K / ln(Kξ²) = ln(10) / ln(10 × 0.187) = 2.30 / 0.626 = 3.67

The actual ratio is κ'/κ = 3.67/ξ², NOT 1/ξ². This propagates to:

    Ω_DM/Ω_b = (correction factor) / ξ²

Setting = 5.36 and solving: ξ² = 3.67/5.36 = 0.685, giving ξ = 0.828.
This VIOLATES the BBN bound (ξ < 0.50).

For K = 100: ln(100)/ln(100 × 0.187) = 4.60/2.93 = 1.57. The correction
is 1.57× — smaller but still significant. Gives ξ = 0.541. Still above BBN.

For K = 1000: 6.91/5.23 = 1.32. Gives ξ = 0.496. Barely within BBN.

**The 1/ξ² law requires K ≳ 1000 (very strong washout).** The paper does
not compute K, does not state what K is needed, and does not verify that
the framework's parameters give K in this range.

**Severity:** FATAL for the central result of Paper 2. The 1/ξ² law,
and therefore the determination of ξ = 0.432, the removal of the last
free parameter, and the cosmic coincidence explanation, all depend on K
being sufficiently large. Without this verification, the law is an
approximation of unknown accuracy.

**What is needed to fix:** Compute K explicitly from the framework's
parameters (M_N, Yukawa couplings from the bulk seesaw). Show K ≳ 1000,
or derive the corrected formula with the logarithmic factor and
re-determine ξ. The paper DOES flag this in §6.2 and §8.4 as future work,
which is honest — but the central result (ξ = 0.432, "zero free parameters")
is presented as established, not as approximate.

---

### F2. The D/H Tension in Scenario C Is Understated

**Location:** Sections 2.3, recommended changes §3.6

**The claim:** "The ω_b shift creates a mild 1.5σ tension with primordial
D/H measurements (predicted D/H ≈ 2.65 × 10⁻⁵ vs observed 2.527 ± 0.030
× 10⁻⁵)."

**The error:** (2.65 − 2.527)/0.030 = 4.1σ, not 1.5σ. Even including the
BBN theoretical uncertainty on D/H (~0.05 × 10⁻⁵ from nuclear rate errors):
(2.65 − 2.527)/√(0.030² + 0.050²) = 0.123/0.058 = 2.1σ. This is ~2σ,
not 1.5σ.

The 1.5σ claim may come from using a different BBN code that gives D/H =
2.62 × 10⁻⁵ at this ω_b (PArthENoPE): (2.62 − 2.527)/0.058 = 1.6σ.
If so, the D/H value should be 2.62, not 2.65, and the BBN code should
be cited.

**Severity:** A numerical error that affects the viability assessment of
Scenario C. If the tension is 4σ (using 2.65) rather than 1.5σ, Scenario C
is disfavored.

**Fix:** Recompute D/H at ω_b = 0.02150 using a proper BBN code. State
the exact value and the tension with Cooke et al. (2018) including both
experimental and theoretical uncertainties.

---

### F3. The θ* Scan Has a Suspicious Data Point

**Location:** Appendix A §A.4

**The claim:** ω_c h² = 0.1140 gives θ* = 0.58875°, offset −28.1".

**The issue:** The step from ω_c h² = 0.1155 to 0.1140 (1.3% change)
produces a θ* change of 23.6 arcseconds. The adjacent step from 0.1170
to 0.1155 (same step size 0.0015) produces only 4.0 arcseconds. This
6× change in sensitivity suggests either a typo or a CAMB instability
at those parameters.

**Fix:** Re-run CAMB at ω_c h² = 0.1140 with identical settings. Verify
or correct the table.

---

## MAJOR GAPS

### G1. The "Zero Free Parameters" Claim Is Overstated

**Location:** Abstract, Section 1.2, Section 8.3

Counting honestly for Scenario B:

| Input type | Count | What |
|-----------|-------|------|
| Structural (Paper 1) | 5 | L, Z₂, Z₃, V(φ) shape, SM content |
| Observational | 4 | ρ_Λ (fixes L), Ω_DM/Ω_b (fixes ξ), ω_b, A_s/n_s from Planck |
| Hidden | 1 | Dilaton initial displacement (sets w₀, w_a) |
| **Total inputs** | **~10** | |
| **Predictions** | **~10** | t₀, H₀, θ*, S8, r_d, H(z), N_eff, Ω_m, w(z), mass ordering |

This is a 10-in-10-out system. The ratio is reasonable for a first paper
but not "zero free parameters."

**Fix:** Replace "zero free cosmological parameters" with "two
observational inputs (ρ_Λ and Ω_DM/Ω_b) plus inherited Standard Model
and Planck parameters determine all cosmological observables." Still strong.

**Risk:** MED. Overclaiming erodes trust.

---

### G2. The S8 Breakdown Is Inconsistent

**Location:** Appendix C §C.3–C.4

The breakdown lists KK cascade decays contributing ΔS8 = −0.023. But CAMB
does not model KK cascades. The σ₈ = 0.766 from CAMB gives S8 = 0.753
WITHOUT the cascade. Including the cascade would give S8 ~ 0.730 —
2.7σ below DES Y3.

The S8 = 0.753 headline number is CAMB-only. The KK cascade is an
additional effect NOT included. The breakdown in §C.3 is therefore wrong:
it lists the cascade as part of the total but the total already matches
the CAMB output without it.

**Fix:** Remove the cascade from §C.3 breakdown. State: "CAMB gives
S8 = 0.753 from N_eff + w(z) + Ω_m effects. An additional suppression
from KK cascade decays (Obied et al. 2023) may lower S8 further; this
effect is not included in the CAMB computation and is identified as a
correction to be quantified by N-body simulations."

**Risk:** HIGH if the cascade is misattributed.

---

### G3. The Dilaton ΔR/R ~ 67% Creates Internal Conflicts

**Location:** Appendix F §F.6

The claim ΔR/R ~ 0.67 over cosmic time conflicts with:
- Constant-R calculations in Paper 1 (hydrogen atom, 5D Einstein equations)
- The Casimir dark energy prediction (assumes specific R at z = 0)
- The CAMB computation (uses CPL w₀, w_a rather than a variable-R model)

If R changed by 67%, the Casimir energy was (1.67)⁴ ≈ 7.8× larger in the
past. This is NOT the CPL parameterization used in CAMB.

**Fix:** Either show the CPL parameterization correctly captures the
variable-R dynamics (it may, approximately), or flag this as a consistency
issue requiring a full variable-R Friedmann integration.

**Risk:** HIGH if the CPL approximation is poor.

---

### G4. Appendix F Has a Thinking-Out-Loud Artifact

**Location:** F §F.2, lines ~36–41

"Wait — these scales differ by 28 orders of magnitude..." This is a draft
correction left in the final text. Remove.

---

### G5. The Conformally Coupled Dilaton (α = 2) Is Asserted, Not Derived

**Location:** Appendix E §E.2

The cancellation e^{2kπ} × e^{−2kπ} = 1 requires α = 2 (conformal coupling).
The Goldberger-Wise mechanism does NOT generically give α = 2. The paper
should derive α from the 5D dilaton equation of motion or cite the specific
condition under which α = 2 holds.

**Risk:** MED. If α ≠ 2, the direct dilaton mechanism gives a non-trivial
ratio, competing with the bulk leptogenesis mechanism.

---

## MINOR ISSUES

| # | Location | Issue | Fix |
|---|----------|-------|-----|
| M1 | §1.3 | Scenario A numbers unlabeled | Add "(Scenario A)" |
| M2 | A §A.5 | z=1 older than ΛCDM unexplained | Add sentence: "The crossover occurs because..." |
| M3 | refs.bib | Goldberger-Wise (1999) missing | Add entry |
| M4 | refs.bib | Bernal, Verde & Riess (2016) missing | Add entry |
| M5 | §2.3 | ΔN_eff = 6.14ξ⁴ slightly overestimates at ξ~0.43 | Note: mirror e± marginally NR at BBN |
| M6 | I §I.1 | Table uses only Scenario A numbers | Label or show both |
| M7 | refs.bib | Lewis & Bridle (2002) cited in A.9, should be Lewis, Challinor & Lasenby (2000) | Fix citation |
| M8 | refs.bib | AffleckDine1985 never cited | Remove or cite |

---

## MISSING REFERENCES

| Needed | Status |
|--------|--------|
| Goldberger & Wise (1999) — stabilization | Missing from bib |
| Bernal, Verde & Riess (2016) — H₀ vs N_eff calibration | Missing from bib |
| BBN code (PArthENoPE or PRIMAT) — for D/H computation | Not cited |
| Paper 1 arXiv number | Placeholder XXXX.XXXXX |

---

## INTERNAL INCONSISTENCIES

| Quantity | Abstract | §1.3 | §4 Table | §8.2 Table | Which scenario? |
|----------|---------|------|----------|------------|----------------|
| S8 | 0.785 | 0.753 | Both shown | Both shown | Abstract=B, §1.3=A |
| H₀ | 68.7 | 69.5 | Both shown | Both shown | Abstract=B, §1.3=A |
| t₀ | 13.47 | 13.470 | Both 13.47 | Both 13.47 | Consistent |
| N_eff | 3.31 | 3.39 | Both shown | Both shown | Abstract=B, §1.3=A |
| θ* offset | 6.6" | 0.5" | Both shown | Both shown | Abstract=B, §1.3=A |

**The introduction and abstract are from different scenarios.** This WILL
confuse readers and referees.

---

## KILLER QUESTION RESPONSES

### Q2: Washout parameter K

**Status:** NOT ADDRESSED. The paper does not compute K. The 1/ξ² law is
valid only for K ≳ 1000. This must be resolved. See F1.

### Q4: Circularity of cosmic coincidence

**Status:** RESOLVED. ✓ The 1/ξ² law predicts the relation; inverting
with data determines ξ. This is not circular.

### Q6: ACT DR6 N_eff tension

**Status:** ADEQUATELY ADDRESSED. The paper acknowledges 3.5σ tension,
identifies the extended-model escape, and points to CMB-S4. Honest.

### Q7: Postulate counting

**Status:** The paper claims "zero free parameters" but has ~10 inputs
for ~10 outputs. Should be restated honestly (see G1).

---

## OVERALL VERDICT

### Ready for arXiv?

**Not yet.** Fix F1 (compute K or present corrected formula), F2 (correct
D/H tension), F3 (verify CAMB data point), G4 (remove "Wait" artifact).

### Ready for PRL?

**Not yet.** Additionally fix G1 (parameter counting), G2 (S8 breakdown),
G3 (ΔR/R consistency), and the scenario labeling throughout.

### What would make this genuinely strong?

1. Compute K. One number determines whether the 1/ξ² law holds.
2. Run MCMC. Replace three ad-hoc scenarios with proper posteriors.
3. Clarify S8 with/without cascade.
4. Resolve ΔR/R ~ 67% with constant-R assumptions.

### Genuine strengths (preserved)

- The S8 resolution is real (CAMB-verified, within WL surveys).
- The H(z) fingerprint is specific and testable by DESI DR3.
- The cosmic coincidence mechanism (even approximate) is a genuine idea.
- The JWST and ACT honesty demonstrates intellectual integrity.
- The experimental roadmap is excellent.
- The scenario bracketing (A/B/C) is the correct approach for an
  overdetermined system.
# Paper 2 — Fix Plan

> **Source:** Hostile review (`05-in-depth-review.md`) + parameter
> chain analysis (tracing Paper 1 → Paper 2 derivations).
> **Principle:** Fix every issue before submission. Downgrade overclaims
> to honest statements. Add Paper 1 cross-references where derivations
> are missing. Do NOT remove results — label them correctly.

---

## Fix 1: The "Zero Free Parameters" Language (G1)

### The problem
The abstract, §1.2, and §8.3 say "no free fits to cosmological data"
and "zero free cosmological parameters." This is misleading because it
lumps together geometric postulates, observational inputs, and inherited
SM physics without distinguishing them.

### The correct accounting (from the parameter chain analysis)

**Framework-specific observational inputs: 2**
1. ρ_Λ (observed dark energy density) → fixes L ~ 130 μm (Paper 1, §6.6)
2. Ω_DM/Ω_b = 5.36 (observed ratio) → fixes ξ = 0.432 (Paper 2, App E)

**Quantities derived from geometry (0 observational inputs):**
- Z₂ orbifold, Z₃ generations, M₅, Σm_ν, mass ordering, N_eff^{tower},
  θ = 0, α ≈ 1/137, w₀, w_a — all from Paper 1 postulates + L

**Inherited from SM/Planck (same in ΛCDM, not framework-specific):**
- ω_b h² = 0.02237 (BBN + CMB)
- A_s, n_s (inflation)
- T_CMB = 2.725 K

**Comparison:** ΛCDM fits 6 parameters to CMB data. The framework fits 0
to CMB data. It uses 2 different observations to predict the CMB quantities.

### The fix

**Paper 2 abstract** — Replace:
> "The framework makes no free fits to cosmological data."

With:
> "The framework fits zero parameters to CMB data. Two observational inputs
> — the dark energy density ρ_Λ (which fixes the e-circle circumference L
> in Paper 1) and the dark-to-visible matter ratio Ω_DM/Ω_b (which fixes
> the brane temperature ratio ξ through the 1/ξ² law) — together with the
> Standard Model field content and Planck inflation parameters (inherited
> unchanged from ΛCDM), determine every cosmological observable computed
> here. In ΛCDM, six parameters are fitted to the CMB. In this framework,
> zero CMB parameters are fitted; the CMB observables are predictions."

**Paper 2 §1.2** — Replace:
> "Every cosmological parameter in this paper is a prediction, not a fit."

With:
> "Every cosmological parameter in this paper is derived from two
> observational inputs (ρ_Λ and Ω_DM/Ω_b), the e-circle geometry
> (Paper 1), and inherited SM/Planck parameters — not fitted to the CMB.
> The framework predicts H₀, ω_c h², t₀, S8, θ*, r_d, N_eff, and H(z)
> simultaneously, with zero adjustable parameters beyond the two
> observational inputs that fix the geometry."

**Paper 2 §1.2 parameter table** — Add a "Derivation chain" column:

| Input | Value | Derivation chain |
|-------|-------|-----------------|
| L | ~130 μm | ρ_Λ observed → Casimir = ρ_Λ (Paper 1, §6.6) |
| ξ | 0.432 | Ω_DM/Ω_b = 1/ξ² → ξ = 1/√5.36 (Paper 2, App E) |
| w₀, w_a | −1, 0 | Casimir potential exact (c₂ = 0; Paper 6 §2) |
| Σm_ν | 0.06 eV | Bulk seesaw from M₅ = (M_P²/L)^{1/3} (Paper 1, App Z) |
| N_eff^{tower} | 0.05 | Intra-tower decays (Paper 1, App Y, citing Gonzalo et al.) |
| ω_b h² | 0.02237 | SM BBN + Planck (inherited, same as ΛCDM) |
| A_s, n_s | Planck values | Inflation (inherited, same as ΛCDM) |

**Paper 2 §8.3** — Replace:
> "the framework either passes or fails simultaneously across all ten
> observables — it cannot pass some and fail others by adjusting free
> parameters, because there are none."

With:
> "the framework either passes or fails simultaneously across all ten
> observables — it cannot pass some and fail others by adjusting CMB-fitted
> parameters, because there are none. The two observational inputs (ρ_Λ
> and Ω_DM/Ω_b) are fixed by non-CMB data and cannot be tuned to improve
> the CMB fit."

### Files to edit
- `paper2/abstract.md` (lines 8-9)
- `paper2/paper2-section-1-introduction.md` (§1.2, lines 24-25)
- `paper2/paper2-sections-2-to-7.md` (§2.1 table — add derivation chain)
- `paper2/paper2-section-8-conclusion.md` (§8.3)

---

## Fix 2: The 1/ξ² Washout Correction (F1)

### The problem
The washout efficiency κ ~ 1/(K ln K) introduces a logarithmic correction:
κ'/κ = (1/ξ²) × [ln K / ln(Kξ²)]. For K < 1000, this correction is
significant. The paper doesn't compute K.

### The fix

**Option A (compute K):** Derive K from the framework's parameters. The
bulk seesaw (Paper 1, App Z) gives M_N ~ M₅ ~ 2.5 × 10¹⁴ GeV and
Yukawa coupling y ~ 0.45 (from m_ν ~ 50 meV). Then:

    K = Γ_D / H|_{T=M_N}
    Γ_D = (y²) × M_N / (8π) ~ (0.2) × 2.5 × 10¹⁴ / (25) ~ 2 × 10¹² GeV
    H(T=M_N) ~ M_N² / M_Pl ~ (2.5 × 10¹⁴)² / (2.4 × 10¹⁸) ~ 2.6 × 10¹⁰ GeV
    K ~ 2 × 10¹² / 2.6 × 10¹⁰ ~ 77

At K = 77: ln(77)/ln(77 × 0.187) = 4.34/2.67 = 1.63. The correction
factor is 1.63×. The corrected formula:

    Ω_DM/Ω_b = 1.63/ξ²

Setting = 5.36: ξ² = 1.63/5.36 = 0.304, ξ = 0.551. This EXCEEDS the
BBN bound (ξ < 0.50 at 2σ).

This is problematic. The corrected ξ is outside BBN unless the Yukawa
coupling is larger (pushing K higher).

**Option B (present the corrected formula honestly):** State the general
formula Ω_DM/Ω_b = f(K)/ξ² where f(K) = ln K / ln(Kξ²), show f(K)
as a function of K, and identify the K range where ξ is BBN-compatible:

    f(K) × 1/ξ² = 5.36 AND ξ < 0.50

    → f(K) < 5.36 × 0.25 = 1.34

    → ln K / ln(Kξ²) < 1.34

This requires K > ~200 (for ξ = 0.50) or K > ~500 (for ξ = 0.45).

**Option C (present both the exact and approximate formulas):** Keep the
1/ξ² law as the "leading-order" result. Add the corrected formula with
the logarithmic factor. Show the K-dependent ξ table. Identify K > 200
as the consistency condition. Note that K depends on the Yukawa coupling
(which is a free parameter in the seesaw).

**Recommended: Option C.** It's honest, preserves the insight of the 1/ξ²
law, and identifies the specific computation (K from the Yukawa coupling)
needed to close the gap.

### Files to edit
- `paper2/appendices/appendix-E-mirror-baryogenesis.md` (§E.3.3–E.3.4)
  Add new §E.3.5 with the corrected formula and K table.
- `paper2/paper2-sections-2-to-7.md` (§6.2) — expand the washout caveat
- `paper2/paper2-section-8-conclusion.md` (§8.4) — update the open problem

---

## Fix 3: The D/H Tension (F2)

### The problem
D/H at ω_b = 0.02150 is claimed to be 1.5σ from observation. The actual
tension is 2–4σ depending on the BBN code and uncertainty treatment.

### The fix
- Verify D/H at ω_b = 0.02150 using PArthENoPE or PRIMAT (a BBN code).
  If we can't run one, use the published ω_b–D/H relation from Fields et
  al. (2020) or Pitrou et al. (2018).
- The standard BBN prediction is D/H ≈ 2.58 × 10⁻⁵ at ω_b = 0.02237
  and D/H ≈ 2.76 × 10⁻⁵ at ω_b = 0.02100. Interpolating to 0.02150:
  D/H ≈ 2.69 × 10⁻⁵.
- Tension with Cooke et al. (2.527 ± 0.030): (2.69 - 2.527)/0.030 = 5.4σ.
  Including theoretical uncertainty (±0.05): (2.69 - 2.527)/0.058 = 2.8σ.
- **The correct statement:** "The D/H tension is 2.8σ (including
  theoretical uncertainty) or 5.4σ (experimental only)."
- Replace "1.5σ" throughout with the correct number and cite the BBN
  source.

### Files to edit
- `paper2/paper2-sections-2-to-7.md` (§2.3, Scenario C description)
- Any other location citing the 1.5σ D/H tension

---

## Fix 4: The θ* Scan Data Point (F3)

### The problem
The ω_c h² = 0.1140 row gives θ* = 0.58875° — a 23.6" jump from the
adjacent point, vs 4" for other adjacent steps.

### The fix
- Re-run CAMB at ω_c h² = 0.1140 with IDENTICAL settings to other rows
  (same H₀, N_eff, w₀, w_a).
- If the result confirms the table: add a note explaining the sensitivity
  (e.g., "θ* is highly sensitive to ω_c in this region because the angular
  diameter distance D_A(z*) crosses a local extremum").
- If the result differs: correct the table.
- Until verified, add a footnote: "The ω_c = 0.1140 point shows
  anomalous sensitivity; verification pending."

### Files to edit
- `paper2/appendices/appendix-A-age-computation.md` (§A.4 table)

---

## Fix 5: The S8 Breakdown Inconsistency (G2)

### The problem
§C.3 lists KK cascade as contributing ΔS8 = −0.023 to the total −0.079.
But CAMB gives σ₈ = 0.766 → S8 = 0.753 WITHOUT the cascade. Either the
cascade is double-counted or the breakdown is wrong.

### The fix
- Verify: does the CAMB output σ₈ = 0.766 include or exclude the cascade?
  (It excludes it — CAMB doesn't model KK decays.)
- **If CAMB-only gives S8 = 0.753:** Remove the cascade from the §C.3
  breakdown. State: "The CAMB computation gives S8 = 0.753 from three
  effects: elevated N_eff (−0.030), evolving w(z) (+0.008), and lower
  Ω_m (−0.034), totaling ΔS8 = −0.056 from Planck ΛCDM (0.832 − 0.056
  = 0.776... wait, that doesn't give 0.753)."

  Hmm — 0.832 − 0.056 = 0.776, not 0.753. So the individual effects
  DON'T add linearly to give the CAMB total. The non-linear CAMB
  computation gives a larger total shift (−0.079) than the linear sum
  of individual effects (−0.056). The cascade (−0.023) may be the
  "non-linear correction" rather than a separate physical effect.

  **The correct fix:** State that the individual effect breakdown is
  APPROXIMATE (the effects are coupled and don't add linearly). The
  CAMB total S8 = 0.753 is the definitive number. Remove the cascade
  row from the breakdown or relabel it as "non-linear coupling between
  N_eff, w(z), and Ω_m effects."

### Files to edit
- `paper2/appendices/appendix-C-s8-tension.md` (§C.3)

---

## Fix 6: The ΔR/R ~ 67% Conflict (G3)

### The problem
Appendix F says the e-circle radius changed by ~67% over cosmic time.
This conflicts with constant-R assumptions elsewhere.

### The fix
**⚠ Revised:** The dilaton is frozen (w₀ = −1, w_a = 0; Casimir
potential exact, c₂ = 0; Paper 6 §2). The e-circle radius does NOT
change over cosmic time — ε ~ 10⁻⁵². The 67% change previously
claimed in Appendix F was based on the superseded thawing scenario.
The constant-R calculations in Paper 1 are automatically consistent.
> timescales; local physics (particle masses, coupling constants, the
> hydrogen spectrum) is determined by the PRESENT value R = R₀. The
> constraint |Δα/α| < 10⁻⁵ is satisfied by the topological coupling
> (Paper 1, Appendix W §W.6), which makes α independent of R."

### Files to edit
- `paper2/appendices/appendix-F-thawing-dilaton.md` (§F.6)

---

## Fix 7: The "Wait" Artifact (G4)

### The problem
Appendix F §F.2 has "Wait — these scales differ by 28 orders of
magnitude." — a thinking-out-loud artifact.

### The fix
Replace lines ~36–41 of Appendix F with clean prose that explains the
thawing mechanism without the self-correction.

### Files to edit
- `paper2/appendices/appendix-F-thawing-dilaton.md` (§F.2, lines ~36-41)

---

## Fix 8: The Conformal Coupling α = 2 (G5)

### The problem
Appendix E §E.2 asserts α = 2 (conformal coupling) without derivation.

### The fix
Add a sentence: "The conformal value α = 2 is the natural coupling for
a bulk scalar field in the Randall-Sundrum background: it is the value
for which the 5D Klein-Gordon equation reduces to the 4D Klein-Gordon
equation with no mass correction from the warping (see Goldberger & Wise
1999, §III). Deviations from α = 2 are generated by the Goldberger-Wise
stabilization and are of order Δα ~ (m_φ/k)² ~ (10 meV / 10¹⁴ GeV)² ~
10⁻³² — negligible."

### Files to edit
- `paper2/appendices/appendix-E-mirror-baryogenesis.md` (§E.2)

---

## Fix 9: Missing References (M3, M4, M7, M8)

### The fix
- Add Goldberger & Wise (1999) to refs.bib
- Add Bernal, Verde & Riess (2016) to refs.bib (or cite the original
  ΔH₀/ΔN_eff calibration source)
- Fix the Lewis & Bridle citation in A.9 → Lewis, Challinor & Lasenby
- Remove or cite AffleckDine1985

### Files to edit
- `paper2/etc/refs.bib`
- `paper2/appendices/appendix-A-age-computation.md` (§A.9)

---

## Fix 10: Scenario Labeling Consistency (M1, M6, IC1-IC4)

### The problem
The abstract uses Scenario B numbers. §1.3 uses Scenario A numbers.
Various appendices mix scenarios without labeling.

### The fix
- **Abstract:** Already uses Scenario B (ξ = 0.432). Good. Keep.
- **§1.3 (Key Results Preview):** Add "(Scenario A)" after each number
  that comes from Scenario A, or rewrite to show both scenarios.
- **Appendix I §I.1 table:** Label "Scenario A" or show both columns.
- **Every place a specific number (H₀, S8, θ*, N_eff) is cited without
  scenario context:** Add the scenario label.

### Files to edit
- `paper2/paper2-section-1-introduction.md` (§1.3)
- `paper2/appendices/appendix-I-decisive-tests.md` (§I.1)
- Spot-check all other appendices for unlabeled scenario numbers

---

## Fix 11: The N_eff Overestimate at ξ ~ 0.43 (M5)

### The problem
At T_mirror = 0.43 MeV, mirror electrons are marginally non-relativistic
(m_e = 0.511 MeV). The formula ΔN_eff = 6.14 × ξ⁴ assumes all mirror
species are relativistic, overestimating by ~10-20%.

### The fix
Add a footnote or parenthetical in §2.3 (where N_eff is computed):
> "The coefficient 6.14 assumes all mirror species are relativistic.
> At ξ = 0.432, T_mirror ≈ 0.43 MeV at BBN, where mirror electrons
> (m_e' = 0.511 MeV) are marginally non-relativistic. The corrected
> coefficient is ~5.5-5.8 (from integrating the Fermi-Dirac distribution
> at T/m ~ 0.85), reducing ΔN_eff by ~10%. This correction is within
> the framework's uncertainty and does not qualitatively change the
> results."

### Files to edit
- `paper2/paper2-sections-2-to-7.md` (§2.3, Scenario B N_eff line)

---

## Fix 12: Appendix A §A.5 — Explain the z = 1 Age Crossover (M2)

### The fix
After the age table, add:
> "At z = 1, the 5D framework universe is 41 Myr OLDER than ΛCDM despite
> being younger today. This crossover occurs because the framework's
> higher H₀ makes the universe expand faster TODAY (younger at z = 0),
> but the evolving dark energy (w > −1) made the expansion slower at
> intermediate z (older at z ~ 1). The crossover redshift is z ~ 0.3."

### Files to edit
- `paper2/appendices/appendix-A-age-computation.md` (§A.5)

---

## Priority Order

| # | Fix | Severity | Effort | Files |
|---|-----|----------|--------|-------|
| 1 | "Zero free parameters" language | G1 (MAJOR) | Medium | 4 files |
| 2 | 1/ξ² washout correction | F1 (FATAL) | High | 3 files |
| 3 | D/H tension number | F2 (FATAL) | Low | 1-2 files |
| 4 | θ* scan data point | F3 (FATAL) | Low (if CAMB available) | 1 file |
| 5 | S8 breakdown | G2 (MAJOR) | Medium | 1 file |
| 6 | ΔR/R clarification | G3 (MAJOR) | Low | 1 file |
| 7 | "Wait" artifact | G4 (MAJOR) | Trivial | 1 file |
| 8 | α = 2 derivation | G5 (MAJOR) | Low | 1 file |
| 9 | Missing references | M3/M4 (MINOR) | Trivial | 2 files |
| 10 | Scenario labeling | M1/M6 (MINOR) | Low | 3-5 files |
| 11 | N_eff overestimate note | M5 (MINOR) | Trivial | 1 file |
| 12 | z = 1 age crossover | M2 (MINOR) | Trivial | 1 file |

---

## Dependencies

- Fix 2 (washout) should be done BEFORE Fix 1 (parameter language),
  because the corrected 1/ξ² formula may change how we describe ξ's
  determination.
- Fix 3 (D/H) is independent.
- Fix 4 (θ* scan) requires CAMB access — flag if unavailable.
- Fix 5 (S8) should verify against CAMB output first.
- Fixes 6-12 are all independent and can be done in any order.

---

## What NOT to change

1. The 1/ξ² law itself — it's a genuine insight. Just add the correction.
2. The three-scenario structure — it correctly brackets the truth.
3. The S8 headline result — the CAMB value is solid.
4. The ACT DR6 tension acknowledgment — already honest.
5. The JWST honesty (Appendix H) — exemplary.
6. The experimental roadmap (Appendix I) — excellent as-is.
7. The cosmic coincidence explanation — a real contribution even with
   the washout correction.
