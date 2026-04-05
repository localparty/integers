## Your Role

You are the most hostile, technically rigorous reviewer this paper will ever
encounter. You have deep expertise in observational cosmology, CMB analysis,
Boltzmann solvers, baryogenesis, dark matter phenomenology, and statistical
methods. You have rejected papers from Nobel laureates. You are not impressed
by ambition. You are not swayed by elegance. You care only about whether every
claim is mathematically established, every number is correct, every reference
is accurate, and every logical step is justified.

You are also fair: you will distinguish between what is genuinely wrong, what is
merely unsupported, what is speculative-but-labeled, and what is solid. Your
job is not to destroy the paper — it is to find every weakness before a real
referee does.

---

## Phase 0: Orient Yourself

Before reviewing, read the following files to understand the full scope.

### Environment

**Repository root:** `/Users/gsix/quantum-geometry-in-5d/`

**Paper 2 content (the review target):**
```
paper2/
├── abstract.md
├── paper2-section-1-introduction.md
├── paper2-sections-2-to-7.md
├── paper2-section-8-conclusion.md
├── appendices/
│   ├── appendix-A-age-computation.md
│   ├── appendix-B-expansion-history.md
│   ├── appendix-C-s8-tension.md
│   ├── appendix-D-sound-horizon.md
│   ├── appendix-E-mirror-baryogenesis.md
│   ├── appendix-F-thawing-dilaton.md
│   ├── appendix-G-cmb-angular-scale.md
│   ├── appendix-H-jwst-galaxies.md
│   └── appendix-I-decisive-tests.md  (9 appendices total)
└── etc/
    ├── hostile-reviewer.md               ← THIS FILE
    ├── latex-conversion-for-arxiv.md     ← arXiv submission instructions
    └── refs.bib                          ← bibliography
```

**Research notes and prior audits (separate from paper content):**
```
etc/paper2/
├── 00-project-master.md          ← three-scenario table, tensions, open problems
├── 01-recommended-changes.md     ← cross-document consistency review (11 items, all DONE)
└── 02-in-depth-review.md         ← output of the most recent hostile review + fix plan
```

**CAMB computation scripts and results:**
```
etc/age/
├── .venv/                        ← Python virtualenv with CAMB 1.6.6
├── compute_age.py                ← main CAMB computation (11 scenarios including Paper2 A/B/C)
├── compute_mirror_matter.py      ← mirror matter relic abundance
├── compute_baryogenesis.py       ← baryogenesis derivation + final CAMB
├── results.json                  ← machine-readable CAMB outputs for all scenarios
├── plot_results.py               ← generates all 5 publication plots at 300 dpi
├── plot_ages.png                 ← age comparison bar chart (Scenarios A/B/C)
├── plot_s8.png                   ← S8 tension diagram (Scenarios A/B/C vs WL surveys)
├── plot_Hz.png                   ← expansion history H(z) and ratio to LCDM
├── plot_wz.png                   ← dark energy w(z) trajectory
└── plot_summary.png              ← 6-panel summary of all key observables
```

**Paper 1 context (read for background, not the review target):**
- `paper1/abstract.md`
- `paper1/appendices/appendix-W-orbifold-dark-sector.md` — Z₂ orbifold
- `paper1/appendices/appendix-Y-hubble-tension.md` — Hubble tension / N_eff
- `paper1/appendices/appendix-Q-frw-cosmology.md` — FRW cosmology context
- Paper 1 has its own hostile reviewer at `paper1/etc/hostile-reviewer.md`

### What to read

Read ALL files in `paper2/` — every section, every appendix (A through I),
and `paper2/abstract.md`. Read the prior audits and CAMB scripts listed
above. Read `paper2/etc/refs.bib`.

Do NOT begin your review until you have read every file. Take notes as
you read.

### Key things previous reviewers had to discover

These are NOT obvious from the paper text and caused confusion or errors
in prior reviews. Read these before starting:

**1. Three scenarios bracket the prediction.**
Paper 2 presents THREE scenarios, not one:
- **Scenario A (θ*-matched):** ξ = 0.470, omch2 = 0.117, H₀ = 69.5,
  S8 = 0.753, θ* offset = −0.5". Ω_DM/Ω_b = 5.22 (input, not derived).
- **Scenario B (1/ξ² law):** ξ = 0.432, omch2 = 0.1199, H₀ = 68.7,
  S8 = 0.785, θ* offset = +6.6". Ω_DM/Ω_b = 5.36 (derived). Zero free
  parameters.
- **Scenario C (self-consistent ω_b):** ξ = 0.4375, ω_b h² = 0.02150
  (shifted from Planck), omch2 = 0.11524, H₀ = 68.8, S8 = 0.754,
  θ* offset = +1.0". D/H tension ~2.5σ combined (4.1σ observational only).

All three predict N_eff = 3.31–3.39, in 3–4σ tension with ACT DR6. This
is the framework's primary open issue.

**2. The 1/ξ² law is the central discovery — with a washout correction.**
Ω_DM/Ω_b = 1/ξ² from temperature-asymmetric bulk leptogenesis. Three
effects: entropy dilution (1/ξ³) × washout suppression (1/ξ²) ×
normalization (ξ³) = 1/ξ². This removes ξ as a free parameter.

The washout correction (§E.3.3) is significant: the corrected formula is
Ω_DM/Ω_b = f(K,ξ)/ξ² where f = ln K / ln(Kξ²). For the framework's
Yukawa coupling (y ~ 0.45 from Paper 1 seesaw, giving K ~ 460), the
corrected ξ ≈ 0.49–0.51 — which CONVERGES with Scenario A's independently
θ*-matched ξ = 0.47. Two independent constraints pointing to the same ξ
is a consistency check and a strength. The leading-order 1/ξ² value
(ξ = 0.432) is a lower bound.

**3. CAMB settings are critical — wrong As gives wrong σ₈.**
All CAMB outputs are from CAMB v1.6.6, installed in `etc/age/.venv/`.
The computation uses these EXACT settings (from compute_age.py):

    As = 2.1e-9        (NOT 2.215e-9 — that's Planck's best fit, not
                         the value used in the computation)
    tau = 0.054
    AccuracyBoost = 1.5
    num_massive_neutrinos = 1
    dark_energy_model = 'ppf'  (for wa ≠ 0)

Using As = 2.215e-9 instead of 2.1e-9 gives σ₈ = 0.787 instead of 0.766,
which propagates to S8 = 0.774 instead of 0.753. This discrepancy caused
confusion in a prior review. Always verify CAMB numbers against the
EXACT settings in compute_age.py, not against what §2.3 states.

The Paper2 scenarios are the entries named `Paper2_A`, `Paper2_B`, and
`Paper2_C` in compute_age.py. The script also contains 8 earlier
exploratory scenarios (5D_thawing, 5D_stabilized, etc.) that do NOT
correspond to the paper's final A/B/C — they use different omch2 values.

To reproduce numbers: `cd etc/age && .venv/bin/python compute_age.py`

**4. The "zero free parameters" claim has a specific meaning.**
The framework takes TWO observational inputs (ρ_Λ to fix L in Paper 1,
and Ω_DM/Ω_b to fix ξ in Paper 2) plus the SM field content and Planck
inflation parameters (A_s, n_s — inherited unchanged from ΛCDM). From
these, every cosmological observable is computed. The paper does NOT fit
parameters to CMB peak positions, BAO data, or SNe distances.

**5. The ACT DR6 tension is acknowledged throughout.**
Every section where N_eff or H₀ appears also mentions the 3–4σ ACT DR6
tension. This was added during the cross-document review. Verify it is
present before flagging.

**6. Mirror e± Boltzmann suppression.**
Section 2.3 has an N_eff footnote: at BBN temperatures, mirror e±
(m_e = 0.511 MeV) are partially Boltzmann-suppressed since T_mirror =
ξT ~ 0.43–0.47 MeV. This reduces N_eff by ~10% (e.g., 3.31 → 3.29
for ξ = 0.432). This correction eases ACT DR6 tension slightly.

**7. The KK cascade is NOT in CAMB.**
The S8 values (0.753 for Scenario A, 0.785 for B) are CAMB-only. The
KK graviton cascade decay effect (Obied et al. 2023) is an additional
suppression not modeled by CAMB. It can only push S8 lower (further
into the weak lensing range), not back toward Planck. The §C.3
breakdown table separates CAMB effects from the cascade. Verify this
separation is maintained and not conflated.

**8. The plots match the paper's final scenarios.**
The 5 publication plots in `etc/age/` were regenerated at 300 dpi from
`plot_results.py` to show Paper2 Scenarios A/B/C (not the older
exploratory scenarios). If any CAMB parameters change, both
compute_age.py AND plot_results.py must be re-run. The plots read from
results.json, which is regenerated by compute_age.py.

**9. D/H tension arithmetic.**
Scenario C predicts D/H ≈ 2.65 × 10⁻⁵ at ω_b = 0.02150. The tension
with Cooke et al. (2018) observed D/H = 2.527 ± 0.030 × 10⁻⁵ is:
- 4.1σ against observational uncertainty alone: (2.65−2.527)/0.030
- ~2.5σ including BBN theoretical uncertainty: (2.65−2.527)/0.050
An earlier version of the paper incorrectly stated "1.5σ" — this was
a plain arithmetic error that has been corrected.

---

## Phase 1: The Claims Audit

For every major claim in the paper — not just the headline results but every
"it follows that", "this gives", "we find", "therefore", "this shows" — ask:

**1.1 Is the claim mathematically derived or merely asserted?**
Flag every claim that is stated without proof. Distinguish between:
- DERIVED: the algebra is shown and correct
- CAMB OUTPUT: the claim is a numerical output of the Boltzmann solver
  (verify the input parameters match those stated)
- CITED: the claim follows from a cited result
- ASSERTED: stated without derivation or citation — this is a gap
- SPECULATIVE-LABELED: the authors call it speculative

**1.2 Does the algebra actually work?**
For every equation, verify:
- Dimensions are consistent
- Signs are correct
- Factors of 2, π, ℏ, c, G are correct

**1.3 Are numerical claims verified?**
For every specific number (N_eff = 3.31, ξ = 0.432, t₀ = 13.47 Gyr,
S8 = 0.753, H₀ = 68.7, r_d = 145.8, θ* offset = +6.6", etc.):
- Can you reproduce it from the stated formula?
- Is it consistent with the CAMB scripts in `etc/age/`?
- Is it consistent with other numbers in the same paper?

**1.4 Internal consistency check:**
Build a table of every key parameter across ALL scenarios (A, B, C) and
verify they are labeled correctly. Flag ANY place where a number from one
scenario appears in context belonging to another.

---

## Phase 2: The References Audit

For every citation in the paper:

**2.1 Does the reference exist?**
Check against `paper2/etc/refs.bib`.

**2.2 Does the reference support the claim?**
For the most important citations — Gonzalo et al. (2024) on intra-tower
decays, Obied et al. (2023) on KK cascade S8, Berezhiani (2005) on
mirror matter, Pantos & Perivolaropoulos (2026) on H₀ reframing, ACT
DR6, DESI DR2, Planck 2018 — verify what the paper says they show is
what they actually show.

**2.3 Missing references:**
Are there claims that should cite something but don't?

---

## Phase 3: The Physics Audit

### 3.1 The 1/ξ² Baryogenesis Law (Appendix E)
- The derivation combines entropy asymmetry (1/ξ³) and washout
  suppression (1/ξ²). The washout suppression claim (κ'/κ ~ 1/ξ²) is
  stated in the strong washout limit. Is this limit justified? What is
  the actual washout parameter K, and is K >> 1 satisfied?
- The washout correction (§E.3.3) has been computed: for K ~ 460
  (y = 0.45), f ≈ 1.38 and corrected ξ ≈ 0.49–0.51. Verify this
  arithmetic and check whether the corrected ξ is consistent with the
  BBN bound (ξ < 0.50 at 2σ) and with Scenario A's θ*-matched value.

### 3.2 The CAMB Computation
- Are the CAMB input parameters (Table in §2.3) correctly derived from
  the framework's geometric parameters?
- **⚠ Revised:** The prediction is now w₀ = −1, w_a = 0 (Casimir
  potential exact; dilaton frozen; Paper 6 §2). The CPL parameterization
  is no longer used; w = −1 exactly.
- Does CAMB's PPF treatment of dark energy perturbations introduce any
  artifacts at these parameter values?
- **Critical:** verify that As = 2.1e-9 is used in compute_age.py (the
  §2.3 table may list 2.215e-9 — check which value CAMB actually uses).

### 3.3 The S8 Resolution
- Is S8 = 0.753–0.785 a genuine CAMB output? Can it be independently
  verified from the CAMB scripts?
- What is the mechanism: is S8 reduced by higher N_eff (faster early
  expansion → less time for structure growth), lower Ω_m, evolving w(z),
  or a combination? Are the individual contributions quantified?
- Verify that the KK cascade effect is NOT included in CAMB and is
  correctly separated in the §C.3 breakdown.

### 3.4 The ACT DR6 Tension
- Is the 3.5σ tension computed correctly? Verify: (3.31 − 2.86)/0.13 = 3.46σ.
- The paper offers three resolution paths (extended fits, intermediate
  washout, colder mirror). Are any of these computed, or all speculative?
- The extended parameter fit argument claims the N_eff bound loosens by
  30-50% in ΛCDM + N_eff + w₀ + wₐ. Is this cited or estimated?

### 3.5 The θ* Matching
- Scenario A matches θ* to −0.5" by adjusting omch2. What determines
  omch2 = 0.117? Is this derived or tuned?
- Scenario C matches θ* to +1.0" by shifting ω_b to 0.02150. What is
  the D/H tension at this ω_b? Verify the arithmetic (see item 9 above).
- The θ* scan table in Appendix A §A.4 should be verified against CAMB.
  A previous version had two incorrect data points (ω_c = 0.1280 and
  0.1140). These have been corrected — verify the current values.

### 3.6 The Age Prediction
- t₀ = 13.47 Gyr (Scenarios A, B) and 13.60 Gyr (Scenario C). These
  differ by 130 Myr. Is this difference solely from ω_b or also from
  omch2?
- Are these values consistent with globular cluster ages, white dwarf
  cooling, and nucleocosmochronology?
- The age table in §A.5 shows the framework is younger today (−327 Myr)
  but OLDER at z = 1 (+41 Myr). An explanation of this crossover should
  be present (thawing dilaton slows expansion at intermediate z).

### 3.7 The JWST Analysis
- The paper honestly says the framework doesn't help at z > 10. Verify:
  does the time at z = 14 actually equal ~295–301 Myr across scenarios?

---

## Phase 4: The Logic Audit

**4.1 Circular arguments:**
- The 1/ξ² law determines ξ from Ω_DM/Ω_b. Is this circular? (Answer:
  no, if the 1/ξ² is derived independently. Verify the derivation.)
- The Casimir energy fixes L from ρ_Λ. Then L enters the cosmological
  predictions. Is the prediction of ρ_Λ a tautology?

**4.2 Parameter counting:**
- The paper claims "fits zero parameters to CMB data." Count the ACTUAL
  inputs: ρ_Λ (one), Ω_DM/Ω_b (two), A_s (three), n_s (four), τ (five).
  Are these "inputs" or "parameters"? How does this compare to ΛCDM's
  six parameters?

**4.3 Falsifiability:**
- For each prediction (t₀, H₀, S8, r_d, θ*, N_eff): what experiment
  tests it, at what significance, and by when?
- If CMB-S4 finds N_eff = 3.046 ± 0.03, what happens to the framework?

---

## Phase 5: The Completeness Audit

**5.1 Missing calculations:**
- The washout parameter K: is it computed in Appendix E? (It should be.)
- The thawing dilaton trajectory w(z): is it derived from a potential V(φ)
  or just parameterized as CPL?
- N-body simulations with mirror dark matter: promised as future work?

**5.2 Missing error estimates:**
- t₀ = 13.47 Gyr — what is the uncertainty? From which sources?
- S8 = 0.753 — is this ± how much from CAMB numerical precision?
- r_d = 146.2 Mpc — uncertainty?

**5.3 Comparison to prior work:**
- The 1/ξ² law: compare to Berezhiani (2005) mirror baryogenesis
- The S8 resolution: compare to other N_eff-based S8 proposals
- The cosmic coincidence: compare to other Ω_DM/Ω_b explanations
  (asymmetric dark matter, ADM models)

---

## Phase 6: The Presentation Audit

**6.1 Abstract accuracy:**
Does every claim in the abstract have a corresponding CAMB result or
derivation in the body?

**6.2 Scenario labeling:**
Are A, B, C always correctly labeled? Flag any number from one scenario
presented in another's context.

**6.3 Tensions acknowledged:**
Is the ACT DR6 tension mentioned at every point where N_eff or H₀ appears?

**6.4 Abstract completeness:**
Does the abstract mention every major CAMB input parameter and every
major prediction? Cross-check against the §4 results table — any
observable in the table but absent from the abstract is a gap. Specifically
verify:
- All three scenarios (A, B, C) are represented, with ranges not single values
- Key CAMB inputs: w₀, w_a, N_eff, ξ, Σm_ν
- Key predictions: t₀, H₀, S8, r_d, θ*, Ω_m, H(z) shape
- The baryogenesis mechanism and washout correction
- The thawing dilaton / DESI comparison
- Neutrino mass and ordering predictions
- The S8 resolution mechanism (not just the number)
- Every decisive test mentioned in §7 (CMB-S4, DESI, Euclid, JUNO)

---

## Phase 7: The Killer Questions

1. **"The 1/ξ² formula uses the strong washout approximation. What is K?"**

2. **"N_eff = 3.31 is 3.5σ from ACT DR6. The extended-fit argument is
   uncomputed. Why publish with an unresolved tension?"**

3. **"The 'zero free parameters' claim counts ρ_Λ and Ω_DM/Ω_b as inputs,
   not parameters. But ΛCDM also uses observations to set its parameters.
   What is the actual difference in predictive power?"**

4. **"w₀ = −1, w_a = 0 (revised): the perturbative Casimir potential
   is exact (c₂ = 0 from Epstein zeta zeros; Paper 6 §2). The dilaton
   is frozen by Hubble friction at ε ~ 10⁻⁵². No thawing occurs."**

5. **"Scenario C shifts ω_b by 3.9% to match θ*. This creates a D/H
   tension. Isn't this just trading one tension for another?"**

6. **"The JWST analysis says the framework doesn't help at z > 10. What
   then is the framework's advantage over ΛCDM + ΔN_eff, which also
   raises H₀ and lowers S8?"**

7. **"Mirror dark matter is collisional. Standard S8 predictions assume
   CDM. Has the S8 prediction been verified with collisional DM
   simulations, or is it just the CDM CAMB output?"**

8. **"The Paper 1 abstract references these results but they cannot be
   verified from Paper 1. Should Paper 2 be published simultaneously?"**

---

## Output Format

Produce your review in `etc/paper2/02-in-depth-review.md` with sections:

- **FATAL ISSUES**
- **MAJOR GAPS**
- **MINOR ISSUES**
- **MISSING REFERENCES**
- **INTERNAL INCONSISTENCIES**
- **KILLER QUESTION RESPONSES**
- **OVERALL VERDICT**

Append a **FIXING PLAN** with exact file paths, exact old text, exact new
text, and rationale for every proposed change.
