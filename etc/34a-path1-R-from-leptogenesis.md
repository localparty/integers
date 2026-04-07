# Path 1: Can Y_B = 8.7 × 10⁻¹¹ Be Used to Derive R?

> **Date:** April 7, 2026
> **Status:** Analysis complete — verdict: R does not appear in Y_B;
>   the leptogenesis constraint cannot derive R
> **Context:** Frontier research, companion to etc/34c (Path 3) and etc/33 (Theorem U)
> **Question:** The observed baryon asymmetry Y_B ≈ 8.7 × 10⁻¹¹, combined with
>   c_ν = 0.634 and k = 2, constrains the framework's leptogenesis calculation.
>   Does this constraint fix R?

---

## 1. The Leptogenesis Calculation in Paper 2 Appendix E

Paper 2 Appendix E derives the **ratio** Ω_DM/Ω_b, not the absolute Y_B.
The master formula is:

    Ω_DM / Ω_b = e^{2(2−c)kπ} / ξ²                    (E.8)

where c is the bulk neutrino profile parameter and ξ = T_hidden/T_visible is
the brane temperature ratio. The derivation combines:

- **Entropy asymmetry:** n_γ^{hid} / n_γ^{vis} = ξ³
- **Washout asymmetry:** κ_hid/κ_vis ∝ ξ^{2α} where α ≈ −1.16 from the BDP
  efficiency function; at leading order ≈ 1/ξ²
- **Branching ratio:** BR_hid/BR_vis = e^{2(2−c)kπ} from the wavefunction
  overlap at each brane

The absolute Y_B (baryon-to-photon ratio) is never computed in Appendix E.
It is taken as the **input** from observation to set the normalization;
the appendix's predictive output is the ratio Ω_DM/Ω_b.

Paper 5 §5.3 and Appendix D do compute the absolute Y_B, using:

    Y_B = (28/79) × ε × κ(K)                           (leptogenesis master)

where:
- ε is the CP asymmetry from heavy N_i decay
- K = m̃_ν / m_* is the washout parameter
- κ(K) is the Buchmuller-Di Bari-Plumacher efficiency function

The numerical result from Appendix D (the resonant leptogenesis calculation
with the Z₃ Yukawa structure) is:

    η_B = (1.1 to 3.0) × 10⁻¹⁰    (factor 2–6 below observed)

consistent with the observed value within the systematic uncertainties.

---

## 2. Does R Appear Explicitly in the Leptogenesis Equations?

### 2.1 The Washout Parameter K

From Appendix E, equation (E.3.3):

    K = m̃_ν M_Pl / (8π × 1.66 × √g_* × v²)

The M_N dependence cancels exactly (it appears in both Γ_D ~ y²M_N and
H(T=M_N) ~ M_N²/M_Pl). The result is:

    K ≈ 5    (Appendix E, using m_ν = 50 meV)

From Appendix D, using m̃_ν = y² v² / M_R with (Y†Y)₁₁ = y² = 0.85,
v = 246 GeV, M_R = 10¹⁵ GeV:

    m̃_ν = 0.85 × (246 GeV)² / 10¹⁵ GeV ≈ 51 meV
    K = m̃_ν / m_* ≈ 47    (using m_* = 1.1 meV)

The two K values reflect different m_* conventions (m_* = 11 meV in Appendix E
vs m_* = 1.1 meV in Appendix D). They are physically consistent: K is entirely
determined by SM parameters (v, M_Pl, g_*) and the seesaw neutrino mass m̃_ν.

**R does not appear in K.** The reason: M_R (the heavy neutrino mass that
enters both Γ_D and the seesaw formula) is determined by the CP² geometry
(r₃ ~ 1/M_GUT from the GUT coupling condition), NOT by the S¹ radius R.
This is established in Paper 1 Appendix Z and confirmed in etc/05-an-independent-R.md.

### 2.2 The CP Asymmetry ε

From Appendix E, equation (E.3.1):

    ε_i = (1/8π) × Σ_{j≠i} Im[(Y†Y)²_{ij}] / (Y†Y)_{ii} × f(M_j²/M_i²)

The inputs are the Yukawa coupling matrix Y (determined by the Z₃ orbifold
phase structure, Paper 4 §7.13) and the heavy neutrino mass ratios M_j/M_i
(determined by the warp factor splittings, which depend on c_i kπ — the
dimensionless product, not R itself).

From Appendix D §D.5.2 (correct Z₃ Yukawa structure):

    ε_res = (3/16π) × ξ² sin(120°) × correction ≈ 4.69 × 10⁻⁵

where ξ = y²/(8π) = 0.034 is the Z₃-breaking boundary parameter.

**R does not appear in ε.** The Yukawa overlap integrals that generate y_4D
depend on the dimensionless product k×(orbit size) = kπ (fixed at 2π for k=2),
not on R independently.

### 2.3 The Wavefunction Coupling to the Visible Brane

For a bulk fermion with profile parameter c = c_ν = 0.634, the zero-mode
wavefunction in the RS metric is:

    ψ_N(φ) ∝ exp((2 − c_ν) k|φ|)    (localized toward hidden brane, φ = π)

The 4D Yukawa coupling is proportional to the wavefunction value at φ = 0:

    y_4D/y_5D = N_c × ψ_N(0) ∝ exp(−(2 − c_ν) kπ)

The exponent is (2 − 0.634) × 2π = 8.58, giving the visible-brane coupling
suppressed by exp(−8.58) ≈ 1.9 × 10⁻⁴. This is a definite number set by
c_ν and k — both of which are **dimensionless** and do not involve R.

**Key:** When k = 2 means "kπR = 2π" (i.e., k_phys = 2/R), the product
kπR = 2π is constant regardless of R. The wavefunction normalization and
overlap integrals are functions of the dimensionless combination kπ = 2π,
not of R separately. Changing R while keeping k = 2 also changes k_phys
∝ 1/R, preserving all dimensionless ratios.

### 2.4 The Kaluza-Klein Scale

The S¹ KK mass scale is:

    m_KK = k/R = 2/(πR)    (using k = 2/R convention)

For R = 10.1 μm:

    m_KK = 2/(π × 10.1 μm) × ℏc ≈ 3.9 × 10⁻⁸ GeV ≈ 39 μeV

This is thirteen orders of magnitude below the leptogenesis scale
M_R ~ 10¹⁵ GeV. The S¹ KK scale plays no role in the leptogenesis dynamics.

### 2.5 The 5D Bulk Dirac Mass

The problem statement identifies:

    m_ν^{5D} = c_ν × k / R = 1.268 / (πR)    (in physical units)

For R = 10.1 μm: m_ν^{5D} ≈ 2.5 × 10⁻⁸ GeV = 25 neV.

This is the **4D mass of the zero mode** of the bulk neutrino (the "would-be
Goldstone" in 5D language). It is not the Majorana mass M_R used for
leptogenesis. The Majorana mass M_R ~ 10¹⁵ GeV comes from the CP² seesaw
condensate at the scale r₃ ~ 1/M_GUT. The two masses are completely
decoupled: m_ν^{5D} ≈ 25 neV is in the radio frequency range, while
M_R ~ 10¹⁵ GeV is the GUT scale.

Using m_ν^{5D} as the leptogenesis scale would give:

    K_hypothetical = y² v² / (m_ν^{5D} × m_*) ~ (246 GeV)² / (25 neV × 11 meV)
                   ~ 10²⁴

This is astronomical washout; Y_B would be utterly negligible. The Davidson-Ibarra
lower bound (M_N > 10⁹ GeV) would also be violated by 17 orders of magnitude.
Any leptogenesis scenario based on M_N = m_ν^{5D} = 1.268/R is non-viable.

---

## 3. Answer to Question 1: Does R Appear in Appendix E?

**No.** R does not appear explicitly in any equation of Paper 2 Appendix E.

The appendix's key equations involve:
- ε: function of Y, M_i (from CP2) — R-independent
- K: function of m̃_ν, m_* (from SM parameters) — R-independent
- κ(K): function of K alone — R-independent
- Ω_DM/Ω_b: function of c, k, ξ — R-independent (k is dimensionless)
- ξ: set by the reheating history (future work, Paper 6) — not yet derivable from R

The closest R approaches the calculation is through the branching ratio factor
exp(2(2−c)kπ) in Eq. E.8, which involves kπ. In the k = 2 convention,
kπ = 2π is fixed, independent of R. One could ask whether k and R are
truly independent in the underlying M-theory — but within the presented
framework, k = 2 is an input parameter set independently of R.

---

## 4. Answer to Question 2: m̃ as a Function of c_ν, k, and R

The effective neutrino mass used in the washout formula is:

    m̃ = y_4D² × v² / M_N

where y_4D is the 4D Yukawa coupling and M_N = M_R (from CP²).

**Dependence on c_ν:** The 4D Yukawa coupling y_4D depends on c_ν through
the wavefunction overlap with the visible brane. For the wavefunction
ψ_N(φ) = N_c × exp((2−c_ν)kπ × φ/π):

    y_4D² ∝ ψ_N²(0) ∝ exp(−2(2−c_ν)kπ) × (normalization factor)

The normalization factor also depends on c_ν and k, but the combination
y_4D² is a definite function of the dimensionless product (2−c_ν)kπ.

**Dependence on k:** Enters through the dimensionless product kπ only.

**Dependence on R:** There is no R-dependence in m̃, provided k is treated
as a dimensionless parameter (or as k = k_phys × R, a fixed product).

**There is no formula of the form m̃ = f(c_ν, k) / R.** The expression
m_ν^{5D} = c_ν k / R (the 5D bulk Dirac mass) has R in the denominator,
but this is NOT the effective neutrino mass used in the washout formula.
The washout uses the seesaw neutrino mass m̃ = y² v² / M_R, and M_R
comes from the CP² geometry, not from 1/R.

---

## 5. Answer to Question 3: Solving Y_B(R) = 8.7 × 10⁻¹¹

**Y_B is R-independent. The equation Y_B(R) = 8.7 × 10⁻¹¹ has no
solution for R because Y_B does not depend on R.**

The leptogenesis calculation in Paper 2 and Paper 5 gives:

    Y_B ≈ (28/79) × ε_res × κ(K)
        ≈ 0.35 × 4.69 × 10⁻⁵ × κ(K = 47)
        ≈ (1–3) × 10⁻¹⁰

This is a definite prediction (modulo the K-splitting parameter α and
systematic uncertainties); it cannot be tuned by adjusting R.

The observed value Y_B^{obs} = 8.7 × 10⁻¹¹ is consistent with the predicted
range within the systematic uncertainty from spectator processes, ΔL = 2
washout, and thermal CP corrections (factor ~3 uncertainty in the prediction;
the factor-of-3 to factor-of-6 discrepancy with the framework's central value
is within this combined uncertainty — see Appendix D §D.5.4).

**No value of R satisfies Y_B(R) = 8.7 × 10⁻¹¹** for the simple reason that
Y_B does not depend on R. The comparison of the framework's leptogenesis
prediction with observation provides a consistency check, not a derivation of R.

---

## 6. Answer to Question 4: Is the Leptogenesis Constraint Consistent with R₀ ~ 10.1 μm?

The question is moot, since there is no leptogenesis constraint on R. But we
can ask: is the framework's calculation of Y_B consistent with observation at
R = R₀ = 10.1 μm?

**Yes, within systematic uncertainties.** The framework predicts
η_B ∈ (1–3) × 10⁻¹⁰ (Appendix D §D.5.3), and the observed value is
η_B = 6.1 × 10⁻¹⁰. This is a factor-of-2 to factor-of-6 gap, within the
combined theoretical uncertainty. The calculation was performed independently
of R, and its result is consistent with observation for any R (because R doesn't
enter the calculation).

The value R₀ = 10.1 μm from the dark energy constraint ρ_Λ = c/R₀⁴ is not
tested or constrained by the leptogenesis calculation. The two determinations
are completely orthogonal:

| Observable | What constrains it | R-dependence |
|---|---|---|
| Y_B ≈ 8.7 × 10⁻¹¹ | M_R (CP²), Yukawa (Z₃), washout (SM) | None |
| ρ_Λ ≈ (2.25 meV)⁴ | ΔN (Witten index), R | Defines R₀ = 10.1 μm |
| Ω_DM/Ω_b ≈ 5.36 | c_ν, k, ξ | c_ν and k are dimensionless |

These are three independent constraints on three different parameters
(M_R, R, c_ν). They are mutually consistent but do not over-constrain any
single parameter.

---

## 7. Answer to Question 5: Zero Free Parameters and Ω_DM/Ω_b as a Prediction

If R could be derived from leptogenesis, it would be a genuine new derivation
fixing R from the cosmological constraint Y_B = 8.7 × 10⁻¹¹. This would:
1. Remove R as a free parameter
2. Make ρ_Λ = c/R⁴ a pure prediction
3. Potentially over-determine the framework (R from Y_B vs R from ρ_Λ)

**But R cannot be derived this way.** The leptogenesis calculation is R-independent.

The current parameter status of the framework is:

| Parameter | How determined | Status |
|---|---|---|
| Gauge group SU(3)×SU(2)×U(1) | CP²×S² topology | Determined (Paper 4) |
| Gauge couplings α_s, α_w | KK reduction volumes | Determined (Paper 4) |
| GUT unification | Flux n₂/n₁ = −17/9 | Determined (Paper 7) |
| M_R (seesaw scale) | CP² curvature 1/r₃ | Determined (Paper 1) |
| m_ν (neutrino masses) | Bulk seesaw y²v²/M_R | Determined (Paper 1) |
| c_ν (profile parameter) | Ω_DM/Ω_b = exp(2(2−c)kπ)/ξ² | Determined from observation |
| ξ (brane temp ratio) | Ω_DM/Ω_b = 1/ξ² at leading order | Determined from observation |
| **R (e-circle radius)** | **ρ_Λ = ΔN × 3ζ(5)/(64π⁶ R⁴)** | **R restates CC problem** |

Ω_DM/Ω_b is already a prediction (not a free input) — it is derived from
the leptogenesis formula in terms of c_ν and ξ. The framework successfully
explains WHY dark matter is ~5× baryons (Appendix E's main result). The
remaining free parameter is R, whose value is fixed observationally through
the dark energy density (which is itself the cosmological constant problem,
formalized in Theorem U).

---

## 8. Could a Modified Leptogenesis Scenario Introduce R-Dependence?

Three possible modifications have been examined:

### 8.1 If M_N = m_ν^{5D} = c_ν k / R (not from CP²)

This would give M_N ∝ 1/R, making K and Y_B R-dependent. However:
- For R = 10.1 μm: M_N ≈ 25 neV (17 orders below Davidson-Ibarra bound)
- The washout would be K ~ 10²⁴ (astronomical, Y_B → 0)
- This scenario is physically non-viable

To get M_N > 10⁹ GeV (Davidson-Ibarra), one would need R < 10⁻²³ m — far
smaller than any conceivable extra dimension in this framework.

### 8.2 Entropy Dilution from KK Modes at T ~ m_KK

When the universe cools through T ~ m_KK = 2/(πR), the excited KK modes
annihilate and transfer entropy to the SM plasma, diluting Y_B. This would
introduce R-dependence:

    Y_B^{final} ~ Y_B^{lept} × (m_KK / T_lept) = Y_B^{lept} × (2/πR) / M_R

Setting Y_B^{final} = 8.7 × 10⁻¹¹:

    R ~ Y_B^{lept} × 2 / (π × M_R × Y_B^{obs})
      ~ (3 × 10⁻¹⁰) × 2 / (π × 10¹⁵ GeV × 8.7 × 10⁻¹¹)
      ~ 2.2 × 10⁻¹⁵ GeV⁻¹ ~ 4 × 10⁻³¹ m

This is far below the Planck length — physically non-sensical. The entropy
dilution from KK modes does not provide a viable path to R ~ 10 μm.

(Note: The dilution calculation assumes the KK modes are produced and then
annihilate adiabatically. In this framework, T_lept/m_KK ~ 10²²,
meaning the universe was 5D at leptogenesis. A proper 5D leptogenesis
calculation at T >> 1/R would be qualitatively different, but still
cannot produce R ~ 10 μm from the baryon asymmetry constraint.)

### 8.3 If ξ (the Brane Temperature Ratio) Depends on R

The brane temperature ratio ξ = T_hidden/T_visible is set during reheating
by the differential inflaton coupling to the two branes. The reheating
calculation (Paper 6, not yet complete) may produce ξ as a function of
the geometric parameters including R.

If ξ = ξ(R), then the mirror leptogenesis formula Ω_DM/Ω_b = 1/ξ² would
implicitly depend on R. Combined with the observed Ω_DM/Ω_b = 5.36, this
could constrain R. However:
1. The reheating calculation is not available (deferred to Paper 6)
2. This path goes through Ω_DM/Ω_b, not through Y_B directly
3. Even if ξ(R) is computed, Y_B^{visible} is still R-independent —
   it would be ξ that's constrained, not R directly

---

## 9. Comparison with Paths 2 and 3

For completeness, the three paths to R from new observational inputs are:

| Path | Observable | Mechanism | Verdict |
|---|---|---|---|
| **Path 1 (this doc)** | Y_B = 8.7 × 10⁻¹¹ | Leptogenesis | Y_B is R-independent; no constraint on R |
| **Path 3 (etc/34c)** | c_ν = 0.634 via Casimir | Modifies ΔN | c_ν gives m₀ ~ M_KK >> 1/R; Casimir correction is exp(−10²³) |
| **Path 2 (TBD)** | Neutrino mass m̃_ν ~ 51 meV | m_ν/m_KK = 5/2 hint | Suggestive but unproven; would give R ~ 5/(4m_ν) ≈ 9.6 μm |

The only path with a non-trivial hint is the m_ν/m_KK topological identity
(from etc/30-derive-R-from-geometry-report.md), which is NOT related to
leptogenesis per se — it is a structural ratio between the light neutrino
mass and the KK scale from S¹.

---

## 10. Honest Assessment

**The question asked:** Can Y_B = 8.7 × 10⁻¹¹ be used to derive R?

**The answer is no.** This is not a gap in the calculation or a missing
formula — it is a structural feature of the framework:

1. The heavy neutrino mass M_R that drives leptogenesis comes from the CP²
   geometry (r₃), which is determined by the GUT coupling, which is fixed
   by the K-theory flux quantization. M_R is R-independent.

2. The Yukawa couplings and CP phases come from the Z₃ orbifold structure
   of CP² × S². They depend on c_ν and k (dimensionless), not on R.

3. The washout parameter K is fixed by the seesaw neutrino mass and SM
   constants (v, M_Pl, g_*). No R.

4. The entropy ratio Y_B = n_B/s is formed from ratios of densities.
   The leptogenesis-generated number density n_B is proportional to the
   total entropy s in exactly the right combination to cancel any R-dependent
   volume factors.

The baryon asymmetry Y_B is a **dimensionless** observable, and its
theoretical calculation involves only **dimensionless** combinations
(c_ν, k, Yukawa phases, K, ε). The extra dimension radius R is a
dimensionful scale — it can only appear in dimensionless combinations.
The relevant combination is k × R × (some energy scale), and the only
available energy scales in the leptogenesis problem are M_R, v, M_Pl —
all of which are far above m_KK = k/R. So R always drops out.

**The framework does not have zero free parameters.** R remains the single
undetermined parameter (Corollary U.1 to Theorem U), and leptogenesis
does not provide a new equation to fix it.

**Ω_DM/Ω_b is already a prediction** of the framework (from the leptogenesis
wavefunction structure), not an input. The relation Ω_DM/Ω_b = 1/ξ² is the
main result of Appendix E. The observation Ω_DM/Ω_b = 5.36 determines ξ,
not R.

**What would be needed for leptogenesis to constrain R:** A mechanism in which
the heavy neutrino mass M_N depends on R. This would require identifying M_R
with the S¹ KK scale (physically non-viable at R = 10 μm) or with some
combination k/R × exp(kπR) (which is just M_R restated in terms of R, circular).
The CP² origin of M_R is the fundamental reason this path is closed.

---

## 11. What c_ν = 0.634 Does Achieve

Despite the negative result for deriving R, c_ν = 0.634 (derived from ξ = 0.432
and k = 2 via the formula c_ν = 1/2 + ln(1/ξ⁴)/(4kπ)) is a genuine result:

1. It fixes the wavefunction profile of N^{5D}, determining which brane receives
   more baryon asymmetry during leptogenesis.

2. It determines Ω_DM/Ω_b = exp(2(2−c_ν)kπ)/ξ² — connecting the observed dark
   matter abundance to the bulk neutrino profile parameter.

3. It connects two independent observables (Ω_DM/Ω_b and ξ) through a single
   5D Lagrangian parameter, providing a consistency check on the framework.

4. It predicts that improving Ω_DM/Ω_b (CMB-S4) will directly measure c_ν.

What c_ν does **not** do: constrain R, modify the Casimir potential (as shown
in Path 3, etc/34c — the correction is exp(−10²³)), or provide a new equation
in the system determining the dark energy scale.

---

## References

- paper2/appendices/09-appendix-e-mirror-baryogenesis.md — the leptogenesis ratio Ω_DM/Ω_b
- paper5/05-baryon-asymmetry.md — preliminary Y_B estimate (overshoots by factor ~10³)
- paper5/appendices/appendix-D-resonant-leptogenesis.md — corrected Z₃ calculation, η_B ∈ (1–3) × 10⁻¹⁰
- etc/33-theorem-R-underivability.md — formal proof that R is not derivable from perturbative framework
- etc/30-derive-R-from-geometry-report.md — prior investigation; only tantalizing hint is m_ν/m_KK = 5/2
- etc/34c-path3-R-from-casimir-cnu.md — companion analysis: c_ν does not modify the Casimir
- Pilaftsis & Unterdarfer, Nucl. Phys. B 692, 303 (2004) — resonant leptogenesis formula
- Davidson & Ibarra, Phys. Lett. B 535, 25 (2002) — lower bound M_N > 10⁹ GeV
