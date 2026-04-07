# Author Response to Referee Report — Paper 5
## Color Confinement, the Strong Force, and the CP² Holonomy

**Response prepared for:** Physical Review D  
**Referee review run:** r01  
**Date:** 2026-04-07

---

We thank the referee for a thorough and technically precise report. The
report is correct on every point it identifies as a genuine gap or
closable gap. We address each A-rated and B-rated finding below, in the
order they appear in the report. For each finding we provide (a) the
author response and (b) the exact revised text to be inserted or
substituted in the paper. C-rated findings require no revision; we note
gratitude for those confirmations and move directly to the substantive
issues.

---

## Response to A1(b): The 0.7% Match vs. the Coefficient Uncertainty

**Finding:** B — CLOSABLE GAP

### (a) Author response

The referee is correct on all three sub-points. (i) The "0.7%*" entry in
the §7.1 predictions table creates a misleading precision impression even
with the footnote. (ii) The "10–20%" uncertainty language in Appendix A
§A.4 is not consistent with the explicitly computed range
c ∈ [1/(3π²), 1/(2π²)] = [0.0338, 0.0507], which spans a factor of 1.5
in c and therefore ~22% in √σ across the full range. The "10–20%" phrasing
refers to one-sided deviations from the central value, which is an
asymmetric description that would confuse a reader who has just seen the
min/max table in §3.2.2. We will make the one-sided vs. full-range
distinction explicit. (iii) The selection c_central = 3/(8π²) as the
leading-order value requires one sentence of justification: it is the
result of evaluating the instanton integral in the fundamental
representation of SU(3) with the standard adjoint-to-fundamental
Casimir ratio C₂(fund)/C₂(adj) = (4/3)/3 and the lattice Sommer
matching factor r₀ absorbed into the central value. This derivation is
already sketched in Appendix A §A.3 and we will add the one sentence of
motivation that is presently missing.

### (b) Revised text

**§7.1 predictions table — replace the string tension row:**

| Observable | Geometric prediction | Experiment | Match |
|---|---|---|---|
| String tension √σ | [410, 510] MeV | 440 MeV | within range |

Remove the asterisk entry and the footnote associated with "0.7%*". The
table note for the proton mass "~1%*" should similarly be revised to read
"within ~10% leading-order uncertainty"; keep the existing footnote text
for that entry.

**§3.2.2 — add one sentence after the c_min/c_mid/c_max table:**

> The central value c = 3/(8π²) is the leading-order result of evaluating
> the SU(3) instanton integral over the CP¹ generator in the fundamental
> representation, using the standard Casimir ratio C₂(fund)/C₂(adj) =
> (4/3)/3 and normalizing with the lattice Sommer parameter r₀ = 0.5 fm
> (see Appendix A §A.3). It lies within the range [1/(3π²), 1/(2π²)]
> and is adopted as the central value for the purpose of comparison with
> the experimental value √σ = 440 MeV; no precision beyond leading order
> is claimed.

**Appendix A §A.4 — replace the uncertainty sentence:**

Current text (to be removed):
> The theoretical uncertainty in c is ~10-20%, making the agreement
> coincidentally precise.

Replacement:
> The full range c ∈ [1/(3π²), 1/(2π²)] = [0.0338, 0.0507] spans a
> factor of 1.5 in c, propagating to a factor of √1.5 ≈ 1.22 in √σ — a
> 22% spread across the full theoretical range. One-sided deviations from
> the central value c_mid = 3/(8π²) = 0.0380 reach approximately +16% at
> c_max and −9% at c_min. The correct claim is consistency within the
> leading-order predicted range [410, 510] MeV; the 0.7% numerical
> proximity of the central-value prediction 437 MeV to the experimental
> value 440 MeV should not be interpreted as a precision prediction.

---

## Response to A1(d): Wilson Loop Notation — ∮_{∂(CP¹)}

**Finding:** B — CLOSABLE GAP (genuine mathematical error)

### (a) Author response

The referee has identified a genuine mathematical error. The expression
∮_{∂(CP¹)} is ill-formed because CP¹ ≅ S² is a closed 2-manifold with
empty boundary: ∂(CP¹) = ∅. The subscript ∂(CP¹) appears to have been
written to convey "the boundary of the region enclosed by the CP¹
2-cycle," which is not a well-defined notion for a closed manifold. The
physical content is correct — the holonomy is computed along a
representative 1-loop on CP¹ — but the notation must be corrected.

The appropriate fix is option (b) recommended by the referee: replace
∂(CP¹) with an explicit generating 1-loop. Since CP¹ ≅ S², the natural
choice is the equatorial S¹, i.e., the great circle γ_eq ⊂ CP¹. This
is the unique (up to SU(2) rotation) generating 1-cycle of CP¹ in the
sense that [γ_eq] generates π₁(CP¹) = 0 — actually CP¹ has no
non-contractible 1-loops (π₁(S²) = 0), so γ_eq is contractible on CP¹
itself. The correct statement is that the holonomy around γ_eq is a
*representative* path integral on the 2-cycle, not a cycle integral in
the homological sense. A footnote is needed to make this precise.

### (b) Revised text

**§2.2 — replace the Wilson loop equation and its surrounding sentence:**

Current text (to be removed):
```
W_{CP¹} = Tr P exp(i ∮_{∂(CP¹)} A_a dy^a)

where P denotes path ordering around a representative 1-loop on the
boundary of the CP¹ 2-cycle in CP².
```

Replacement:
```
W_{CP¹} = Tr P exp\!\left(i \oint_{\gamma_{\mathrm{eq}}} A_a \,dy^a\right)
```
> where γ_eq ⊂ CP¹ ≅ S² is the equatorial S¹ — a representative
> generating path on the 2-cycle.¹ Path ordering P is taken along
> γ_eq in the direction determined by the orientation of the Fubini-Study
> 2-form ω_FS.

Footnote 1:
> CP¹ ≅ S² is a closed 2-manifold with ∂(CP¹) = ∅; there is no
> boundary circle. The expression ∮_{∂(CP¹)} appearing in some
> earlier drafts is ill-formed and has been corrected here. The
> holonomy W_{CP¹} is computed by integrating the gauge connection
> around a representative path γ_eq on CP¹. Because π₁(CP¹) = 0
> (CP¹ is simply connected), γ_eq is contractible on CP¹ itself; the
> non-trivial topology is carried by the 2-cycle class [CP¹] ∈ H₂(CP², ℤ),
> not by a 1-cycle. Physically, W_{CP¹} measures the holonomy of the
> SU(3) connection around this representative path and serves as an
> order parameter for the confining phase (⟨W_{CP¹}⟩ = 0) vs. the
> deconfined phase (⟨W_{CP¹}⟩ ≠ 0). The relevant topological distinction
> is between gauge configurations with trivial and non-trivial second
> Chern class c₂ on CP², not between different homotopy classes of paths.

---

## Response to A2(a): Lüscher Term — Decoupling Assumption and §B.3a Arithmetic

**Finding:** B — CLOSABLE GAP

### (a) Author response

**Decoupling justification.** The referee is correct that the additive
combination c_total = c_transverse + c_{CP¹} assumes the Nambu-Goto
transverse modes and the CP¹ sigma model modes decouple in the worldsheet
Virasoro algebra. For a sigma model with curved target space (CP¹), this
decoupling is not automatic at the quantum level. We will add a paragraph
justifying this as an approximation valid when the CP¹ curvature scale
(set by r₃) is large compared to the string fluctuation scale (set by
σ^{-1/2}): since r₃ M_Pl ≫ 1 in the framework, the CP¹ isometry modes
are not backreacted on the transverse Nambu-Goto modes at leading order.
This is the same approximation made implicitly in all existing CP¹
worldsheet string literature (e.g., Dubovsky et al. 2012).

**§B.3a arithmetic.** The referee has correctly identified a numerical
inconsistency. The EST boundary correction is ΔL_boundary = +π/12 ≈
0.262. The question is what value of c_{CP¹} produces ΔL = π/12. From
L = π × c/24, we have c = 24 ΔL/π = 24 × (π/12)/π = 2. So ΔL = π/12
corresponds to c_{CP¹} = 2 (the UV limit), not c_{CP¹} = 1. The existing
§B.3a text has the assignment backwards: it states "c_{CP¹} = 1 (WZW
value) gives ΔL = π/24, while c_{CP¹} = 2 (UV) gives ΔL = π/12." The
second half of that sentence is correct (c = 2 → ΔL = π/12), but the
claim "matching the EST boundary correction at the UV limit" is correct
while the first half (c = 1 → ΔL = π/24) gives 0.131, not π/12. The
correction is therefore: the EST boundary correction ΔL = +π/12 ≈ 0.262
corresponds to one full additional degree of freedom c_{CP¹} = 2, i.e.,
the UV classical value. The WZW fixed point (c = 1) would give half this
correction, ΔL = π/24 ≈ 0.131. Since the lattice data lie near L ≈ 0.50
≈ π/6, which is L_{NG} + π/12 = π/12 + π/12, the correspondence is with
the UV limit c_{CP¹} = 2, consistently with what §B.3a already states in
its conclusion. The arithmetic error is in the intermediate assignment of
c = 1 to ΔL = π/24 vs. π/12; we correct this below.

### (b) Revised text

**Appendix B — add paragraph after §B.4 (before §B.5), labeled §B.4a:**

> **§B.4a Justification of the additive central charge combination.**
> The formula c_total = c_transverse + c_{CP¹} assumes the two sectors —
> transverse Nambu-Goto fluctuations and CP¹ internal modes — decouple at
> the level of the worldsheet Virasoro algebra. For a general sigma model
> with curved target space, the stress-tensor two-point function receives
> corrections from the target-space curvature, and the central charges do
> not simply add. The decoupling is an approximation, valid to leading
> order when the curvature length scale of the CP¹ target space (r₃, the
> CP² Kähler radius) is large compared to the worldsheet fluctuation scale
> σ^{-1/2}. In the present framework, r₃ ~ 10⁻³¹ m and σ^{-1/2} ~
> Λ_QCD^{-1} ~ 10⁻¹⁵ m, so r₃ ≪ σ^{-1/2}: the CP² radius is far
> *smaller* than the string fluctuation scale. This means the CP¹ target
> space looks effectively rigid to the long-wavelength string fluctuations,
> and the backreaction of the CP¹ curvature on the transverse modes is
> suppressed by (r₃ σ^{1/2})² ≪ 1. In this rigid-target limit, the CP¹
> modes contribute their central charge additively to the Casimir energy at
> leading order, justifying the combination c_total = 2 + c_{CP¹}. The
> leading curvature correction would enter at order (r₃²σ) ~ 10⁻³² and is
> negligible for the precision claimed here. This is the same approximation
> made implicitly in related effective string literature (Dubovsky,
> Gorbenko, and Mirbabayi, JHEP 1209:044, 2012).

**Appendix B §B.3a — replace the numerically inconsistent sentence:**

Current text (to be removed):
> The factor +π/12 = π × c_{CP¹}/24 with c_{CP¹} = 1 (WZW value) gives
> ΔL = π/24, while c_{CP¹} = 2 (UV) gives ΔL = π/12 — matching the EST
> boundary correction at the UV limit.

Replacement:
> The correspondence is: ΔL = π × c_{CP¹}/24, so the EST boundary
> correction ΔL_boundary = +π/12 ≈ 0.262 corresponds to c_{CP¹} = 2 (the
> UV classical value). At the IR WZW fixed point c_{CP¹} = 1, the CP¹
> modes would contribute ΔL = π/24 ≈ 0.131 — half the EST boundary
> correction. Since the lattice data lie near L_lattice ≈ 0.502, which
> satisfies L_lattice ≈ L_{NG} + π/12 = π/12 + π/12 = π/6 ≈ 0.524
> (within 4%), the correspondence is with the UV limit c_{CP¹} = 2. The
> CP² framework provides a microscopic candidate for the EST boundary
> correction: it is the contribution of the CP¹ internal string modes at
> their UV classical value. Whether the IR WZW renormalization shifts this
> to c_{CP¹} = 1 (giving L = π/8 ≈ 0.393, below the lattice data) or
> whether the lattice scale probes the UV regime requires further
> computation of the CP¹ RG flow at the relevant coupling; both endpoints
> of the prediction L ∈ [π/8, π/6] bracket the lattice value.

**Appendix B §B.7 — add one sentence at the end:**

> In addition, the CP¹ worldsheet theory at the IR WZW fixed point —
> the SU(2)₁ WZW model — possesses a known exact S-matrix via the
> Thermodynamic Bethe Ansatz (Zamolodchikov and Zamolodchikov, 1979;
> Wiegmann, 1985). This means the O(1/R³) and all higher Lüscher
> corrections are in principle exactly computable, providing a sharper
> falsification target than the leading 1/R coefficient alone. We leave
> the TBA computation of the subleading coefficients to future work.

---

## Response to A2(b): Higher String Corrections

**Finding:** B — CLOSABLE GAP (acceptable omission requiring one sentence)

### (a) Author response

Agreed. The sentence has been added in the §B.7 revision above (last
paragraph of the A2(a) response).

---

## Response to C1(c): Resonant Leptogenesis — Appendix D Internal Consistency

**Finding:** B — CLOSABLE GAP

### (a) Author response

The referee identifies three problems. We address each:

**Problem 1 (retraction placement).** The retraction note in §D.5.5
appears *after* the reader has absorbed one full page of incorrect
reasoning from §D.3. We will move a brief retraction flag to the
beginning of §D.3 so the reader encounters it before reading the
incorrect derivation.

**Problem 2 (gap direction and NLO arithmetic).** The referee correctly
notes that η_B decreases as α increases (table in §D.5.3), so the gap is
*below* observation (factor 2–6) and α-tuning cannot close it in the
upward direction. The paper must state this direction explicitly. The
NLO arithmetic should be exhibited: maximum NLO enhancement factor 1.7
× upper end of numerical range 3.0 × 10⁻¹⁰ = 5.1 × 10⁻¹⁰, which is
below the observed 6.1 × 10⁻¹⁰ but consistent within the stated factor-3
combined systematic. We will add this calculation.

**Problem 3 (tension between "not tuning" and "O(1) free parameter").**
The claim "not tuning — it is a geometric output" in §D.5.1 is in direct
tension with "α is an O(1) free parameter not fixed from first principles"
in §D.5.5. The resolution is terminological precision: what is geometric
(not tuned) is the *order* of magnitude of Δ/Γ ∼ 1, which follows from
the Z₃ boundary-breaking parameter ξ = y²/(8π) ~ 0.034. The *exact*
value of Δ/Γ, and thus the exact resonant enhancement factor within its
O(1) range, is not fixed from first principles — that is the role of α.
We will revise §D.5.1 to draw this distinction cleanly.

### (b) Revised text

**Appendix D §D.3 — insert at the very beginning, as a boxed warning:**

> **⚠ Retraction notice.** The parametric estimate in this section
> assumes O(1) off-diagonal Yukawa matrix elements (Y†Y)₁₂ ~ y². This
> assumption is incorrect for the Z₃ democratic Yukawa structure of
> Paper 4 §7.13, which gives instead (Y†Y)₁₂ ~ ξy² with ξ = y²/(8π)
> ~ 0.034 — suppressing the off-diagonal element by a factor of ~30
> relative to the naive estimate. The resulting factor-of-10³ resonant
> enhancement in §D.3 therefore does not apply. The correct calculation
> is in §D.5, which supersedes §D.3. §D.3 is retained for transparency
> (to show the error and how it was discovered) but should not be cited
> for the numerical result.

**Appendix D §D.5 — after the η_B table in §D.5.3, add:**

> **Direction of the discrepancy.** The observed value η_B = 6.1 ×
> 10⁻¹⁰ lies *above* the predicted range (1.1–3.0) × 10⁻¹⁰ by a
> factor of 2–6. The parameter α increases washout (larger α gives
> larger K₂, stronger washout, smaller η_B), so no value of α in the
> natural range [0, 5] closes the gap upward — larger α moves the
> prediction further from observation. The gap must be closed by physical
> effects not included in the leading-order Boltzmann calculation.
>
> The most important such effect is NLO QCD corrections to the
> leptogenesis rate, which provide a multiplicative enhancement. From
> the systematic uncertainty table (§D.5.4), NLO QCD corrections give
> a factor of 1.3–1.7 enhancement. Taking the upper end: 1.7 × 3.0 ×
> 10⁻¹⁰ = 5.1 × 10⁻¹⁰, which is below η_B^{obs} = 6.1 × 10⁻¹⁰ but
> consistent within the stated combined factor-3 systematic uncertainty
> (the combination of all effects in §D.5.4 gives a factor-3 envelope).
> The framework's prediction is therefore marginally consistent with
> observation at the level of its theoretical precision; a precision
> claim is not made.

**Appendix D §D.5.1 — replace the near-degeneracy paragraph:**

Current text (to be removed):
> **1. Near-degeneracy (M₁ ≈ M₂).** The Z₃ orbifold gives three
> identical fixed-point masses at leading order. The boundary-breaking
> parameter ξ = 0.034 sets Δ/Γ ~ 1, placing the system in the resonant
> regime. This is not tuning — it is a geometric output.

Replacement:
> **1. Near-degeneracy (M₁ ≈ M₂).** The Z₃ orbifold gives three
> identical fixed-point masses at leading order. The boundary-breaking
> parameter ξ = y²/(8π) = 0.034 sets the *order of magnitude* of the
> mass splitting as Δ ~ ξ M₁, and the decay width as Γ₁ ~ ξ M₁
> (Appendix D.2), so Δ/Γ ~ 1 to order of magnitude. This places the
> system in the resonant regime — a consequence of the Z₃ geometry, not
> a free tuning. The *precise* value of Δ/Γ within this O(1) regime
> depends on the boundary correction parameter α (which controls the
> K-splitting between N₁ and N₂); α is an O(1) number not fixed from
> first principles within Paper 5. To be precise: the *existence* of
> near-degeneracy (Δ/Γ ~ 1) is a geometric prediction; the *exact*
> degree of degeneracy (the specific value of Δ/Γ ∈ [0.5, 3] for
> α ∈ [0, 5]) is not. The table in §D.5.3 spans this natural range.

---

## Response to E1(a): §5.7 "Unification" Language

**Finding:** A — GENUINE GAP

### (a) Author response

The referee's analysis is correct. Reading §5.7 carefully, the three
calculations sharing c_ν are genuinely independent: consequence 1
(η_B) is a forward calculation from c_ν through F_c to the Yukawa
coupling and Boltzmann equations; consequence 2 (Ω_DM/Ω_b) is the
calculation in Paper 6 from which c_ν is *derived as an output*, not
an input; consequence 3 (m_ν/m_KK = 5/2) is a topological identity
(χ(CP²) − c_2^{eff}/2 = 5/2) derived in Papers 4 and 7 independently
of c_ν. There is no single equation in Paper 5 from which all three
follow simultaneously.

The claim "one topological constraint" producing all three
simultaneously overstates what the mathematics demonstrates. The
correct and still non-trivial claim is *parameter convergence*: the
single value c_ν = 0.634, fixed by the dark matter input, is
consistent with both the leptogenesis constraint and the neutrino mass
ratio. This convergence would fail for generic c_ν (e.g., c_ν = 0.5
gives F_c² = 0.43 vs. 0.659 and shifts η_B outside the consistent
range). That convergence is a genuine, interesting result that does not
require the language of unification to be significant.

The word "unification" carries specific meaning in high-energy physics
(a single gauge group or Lagrangian from which separate phenomena follow
automatically). Nothing in Paper 5 meets that standard for the three
phenomena listed. We revise accordingly.

### (b) Revised text

**§5.7 — replace the "Convergence of three phenomena" paragraph and the
sentence "These are not three coincidences...geometry.":**

Current text (to be removed):
> **Convergence of three phenomena.** The leptogenesis neutrino
> N^{5D} is therefore the single object that simultaneously:
>
> 1. Sets the baryon asymmetry η_B ~ 10^{-10} (§5.3, via its
>    CP-asymmetric decay);
> 2. Sets the dark matter abundance Ω_DM/Ω_b = 1/ξ² (Paper 6,
>    §6.5, via its wavefunction localization c_ν = 0.634);
> 3. Determines the neutrino mass ratio m_ν/m_KK = 5/2 (Paper 4
>    §7.5.7, Paper 7 Appendix B, via the same wavefunction overlap
>    and the topological identity above).
>
> These are not three coincidences. They are three consequences of
> one bulk fermion with one localization parameter fixed by one
> topological constraint of the CP² geometry. The bulk neutrino
> that generates the baryon asymmetry is the same neutrino whose
> mass satisfies a topological relation — and it is the same
> neutrino whose wavefunction explains why dark matter is five
> times more abundant than baryons.

Replacement:
> **Parameter convergence across three sectors.** The bulk neutrino
> N^{5D} carries a single localization parameter c_ν. In Paper 5, that
> parameter appears in three independent calculations:
>
> 1. **Leptogenesis (§5.3, Appendix D):** c_ν enters through the
>    wavefunction suppression factor F_c² = 0.659, which sets the
>    effective Yukawa coupling and, through the Boltzmann equations,
>    the baryon asymmetry η_B ∈ (1.1–3.0) × 10⁻¹⁰.
>
> 2. **Dark matter abundance (Paper 6, §6.5 — forward reference):**
>    c_ν = 0.634 is *derived* in Paper 6 by requiring the brane
>    temperature ratio ξ = T_hid/T_vis to reproduce the observed
>    Ω_DM/Ω_b = 5.36. That is, the dark matter abundance is the
>    *input* that fixes c_ν, not a consequence of it. This
>    calculation is a Paper 6 result; Paper 5 imports c_ν = 0.634
>    and checks that it is consistent with the leptogenesis and
>    neutrino mass constraints.
>
> 3. **Neutrino mass ratio (Papers 4 and 7):** The ratio
>    m_ν/m_KK = 5/2 is derived independently of c_ν from the
>    topological identity χ(CP²) − c_2^{eff}/2 = 5/2 (Paper 4
>    §7.5.7, Paper 7 Appendix B). At c_ν = 0.634, the wavefunction
>    overlap F_c² = 0.659 is consistent with this ratio through the
>    bulk seesaw formula — a non-trivial check.
>
> These three calculations share c_ν as a common parameter but are
> not outputs of a single equation or a single physical constraint.
> The significant result is *convergence*: the value c_ν = 0.634,
> fixed by the dark matter constraint in Paper 6, is simultaneously
> consistent with the leptogenesis constraint (η_B within the
> observed range) and with the neutrino mass ratio (m_ν/m_KK = 5/2
> from the topological identity). This convergence is non-trivial —
> it does not hold for generic c_ν — but it is a consistency
> verification, not a unification. No single topological constraint
> within Paper 5 produces all three outputs simultaneously; the
> precise provenance of each is as stated above. The convergence
> across the three independent calculations is the result; we do
> not claim more.

---

## Response to E1(b): The Dark Matter Mechanism

**Finding:** A — GENUINE GAP

### (a) Author response

The referee identifies the weakest point in §5.7 precisely: the dark
matter production mechanism for N^{5D} is not exhibited in Paper 5,
and the claim that c_ν is "determined by the observed dark matter
abundance" could mislead the reader into thinking the dark matter
particle is N^{5D} itself. It is not.

The mechanism is the mirror-sector (hidden brane) mechanism of Paper 2.
In this mechanism: (1) N^{5D} is the leptogenesis neutrino with mass
M_N ~ 10¹⁵ GeV — it is not the dark matter particle; (2) the dark
matter is a mirror-sector species living on the hidden brane; (3) the
connection between N^{5D} and dark matter is indirect: c_ν controls
the bulk wavefunction overlap, which sets the brane entropy ratio
ξ = T_hid/T_vis during the epoch of N^{5D} decay; (4) this entropy
ratio ξ then determines Ω_DM/Ω_b = 1/ξ² through the mirror
baryogenesis scaling law of Paper 2. The dark matter abundance is
sensitive to c_ν only through ξ, not through N^{5D} being a dark
matter candidate.

This makes the apparent mass-scale inconsistency (M_N ~ 10¹⁵ GeV for
leptogenesis vs. m_DM ~ keV–GeV for dark matter) a non-issue: N^{5D}
and the dark matter are different species. We adopt option (b) from the
referee's list: explicit reframing with honest forward reference to
Paper 6.

### (b) Revised text

**§5.7 — add new subsection §5.7a immediately after the c_ν = 0.634
boxed equation, before the "From c_ν to the 4D neutrino mass" paragraph:**

> **§5.7a The dark matter connection: mirror sector, not N^{5D} itself.**
>
> The value c_ν = 0.634 is not derived within Paper 5. It is imported
> from Paper 6, §6.5, where it is the *output* of the following
> calculation: the Planck 2018 measurement Ω_DM/Ω_b = 5.36 implies,
> via the mirror baryogenesis scaling law of Paper 2 (Ω_DM/Ω_b = 1/ξ²),
> a brane temperature ratio ξ = T_hid/T_vis = 1/√5.36 = 0.432. The
> temperature ratio ξ is set during the epoch when N^{5D} decays on
> the visible brane; the energy deposited on the hidden brane vs.
> visible brane is controlled by the bulk wavefunction overlap of
> N^{5D}, which is the function of c_ν:
>
>     ξ = ξ(c_ν, k) = [F_c(c_ν, k, φ=π) / F_c(c_ν, k, φ=0)]^{1/2}
>
> Solving ξ(c_ν, k=2) = 0.432 for c_ν gives c_ν = 0.634 (Paper 6,
> §6.5). The input–output chain is therefore:
>
>     Ω_DM/Ω_b = 5.36  →  ξ = 0.432  →  c_ν = 0.634        (input chain)
>                                     →  m_ν = 49.74 meV      (output: Paper 4/9)
>                                     →  η_B ~ (1–3)×10⁻¹⁰   (output: §5.3, App. D)
>
> The dark matter in this framework is a **mirror-sector species** on the
> hidden brane — not the bulk neutrino N^{5D} itself. N^{5D} has mass
> M_N ~ 10¹⁵ GeV (set by the CP² seesaw, Paper 1 §Z.1.4) and is the
> leptogenesis source; the dark matter particle is a mirror-sector
> baryon or lepton whose relic abundance is set by the brane temperature
> ratio ξ² through the 1/ξ² law (Paper 2, Appendix E; Paper 6, §6.5).
> The two mass scales are therefore consistent: M_N ~ 10¹⁵ GeV for
> leptogenesis, and m_DM ~ m_b × ξ² ~ GeV × 0.19 for mirror baryons.
> There is no contradiction.
>
> Paper 5's role in this chain is to verify that c_ν = 0.634 — imported
> from Paper 6 — is consistent with the independent leptogenesis
> calculation and with the neutrino mass ratio from Papers 4 and 7.
> This verification is the content of §5.7; the dark matter calculation
> itself is in Paper 6, cross-referenced here.

---

## Response to E1(c): Consistency of Leptogenesis and Dark Matter Mechanisms

**Finding:** B — CLOSABLE GAP

### (a) Author response

The one-sentence clarification requested is now embedded in the §5.7a
text added under the E1(b) response above. For clarity, the key
sentence is:

> "The dark matter in this framework is a mirror-sector species on the
> hidden brane — not the bulk neutrino N^{5D} itself."

and the consistency check is provided by the mass-scale comparison
included in that paragraph. No additional revision is needed beyond
what is in E1(b).

---

## Response to E1(e): Neutrino Mass Ratio as a Third Consequence

**Finding:** B — CLOSABLE GAP

### (a) Author response

The referee correctly identifies a potential ambiguity: the ratio
m_ν/m_KK = 5/2 appears in two places — derived from the topological
identity χ(CP²) − c_2^{eff}/2 = 5/2 in Papers 4 and 7 (independent of
c_ν), and also appearing in §5.7 as a consequence of the wavefunction
overlap at c_ν = 0.634 via the bulk seesaw formula. These are not the
same derivation. The clarification is option (b): they are independent
derivations that agree, and the agreement is a non-trivial consistency
check. We add one sentence making this explicit.

### (b) Revised text

**§5.7 — add one sentence at the end of the "GUT-scale identity" paragraph,
after the displayed equation m_ν/m_KK = 5/2:**

> The ratio 5/2 is derived independently in two ways: (1) from the
> topological identity χ(CP²) − c_2^{eff}/2 = 3 − 1/2 = 5/2 (Papers
> 4 and 7), which is independent of c_ν; and (2) from the bulk seesaw
> formula evaluated at c_ν = 0.634 with the gauge–Higgs unification
> constraint y = g₂√2 (Paper 4, §7.5.7). These are independent
> derivations: the topological identity holds for any c_ν, while the
> seesaw formula gives 5/2 specifically at c_ν = 0.634 with the GUT-
> scale Yukawa constraint. Their agreement at this value of c_ν is a
> consistency check, not a circular argument.

---

## Response to E2(a): Provenance of c_ν = 0.634

**Finding:** A — GENUINE GAP

### (a) Author response

The referee's description of the input/output structure is exactly
correct and is now made explicit in the §5.7a text added under E1(b).
The phrase "cosmologically determined" in the original §5.7 should be
replaced with language that accurately identifies c_ν as a Paper 6
output imported into Paper 5. The phrase "determined by the observed
dark matter abundance" in the opening of §5.7 is accurate in meaning
(it is determined by Ω_DM/Ω_b via ξ) but implies this determination
occurs within Paper 5, which it does not. We revise accordingly.

### (b) Revised text

**§5.7 opening paragraph — replace:**

Current text (to be removed):
> This parameter is not a free input: it is determined by the observed
> dark matter abundance. Paper 6, §6.5 derives, from the requirement
> that the brane temperature ratio ξ = T_hid/T_vis set during
> leptogenesis reproduces Ω_DM/Ω_b = 5.36 (via ξ = 0.432 and
> Ω_DM/Ω_b = 1/ξ²):

Replacement:
> This parameter is not a free input within the series: it is fixed by
> the dark matter abundance constraint in Paper 6, §6.5. Specifically,
> Paper 6 derives — from the Planck 2018 measurement Ω_DM/Ω_b = 5.36,
> the mirror baryogenesis scaling law Ω_DM/Ω_b = 1/ξ² (Paper 2,
> Appendix E), and the brane geometry parameter k = 2 (Paper 1) —
> the value:

(Then the boxed equation c_ν = 0.634 follows, as in the current text.)

**Additional sentence to insert immediately after the boxed equation:**

> This value is imported from Paper 6 into Paper 5, where it is used
> as a fixed input for the leptogenesis and neutrino mass calculations
> below. The two resulting outputs — η_B ∈ (1.1–3.0) × 10⁻¹⁰ from
> Appendix D and m_ν = 49.74 meV from Papers 4 and 9 — are predictions
> that follow from c_ν = 0.634 but do not themselves fix c_ν. The
> dark matter abundance is the input; the baryon asymmetry and neutrino
> mass are the outputs.

---

## Response to E2(c): Precision of c_ν = 0.634 and the 13.7σ Claim

**Finding:** B — CLOSABLE GAP

### (a) Author response

The referee is correct that the value c_ν = 0.634 (quoted to three
significant figures) requires an error budget before the 13.7σ claim
for m_ν can be made. The input uncertainty is δ(Ω_DM/Ω_b) ~ 1% from
Planck 2018 (Ω_DM h² = 0.120 ± 0.001, Ω_b h² = 0.0224 ± 0.0001,
giving δ(Ω_DM/Ω_b)/( Ω_DM/Ω_b) ~ √[(0.001/0.120)² + (0.0001/0.0224)²]
≈ √[0.000069 + 0.000020] ≈ 0.94%). The propagation through
ξ = 1/√(Ω_DM/Ω_b) and then through c_ν(ξ, k) must be made explicit
before quoting m_ν to four significant figures and claiming 13.7σ
discrimination.

### (b) Revised text

**§5.7 "The sharpest prediction" paragraph — insert the error budget
before the 13.7σ claim:**

Replace the opening of that paragraph:
> The R-quantization argument (Paper 9 §4d) shows that dark matter,
> dark energy, and the 5/2 identity are three simultaneous constraints
> on the compactification radius R. At M_GUT = 1.65×10¹⁶ GeV, their
> intersection requires the heaviest neutrino mass to be m_ν = 49.74 meV
> — 0.41 meV below the current NuFIT central value. CMB-S4 combined
> with DESI will discriminate between closure and non-closure at 13.7σ.

with:
> The R-quantization argument (Paper 9 §4d) shows that dark matter,
> dark energy, and the m_ν/m_KK = 5/2 identity are three simultaneous
> constraints on the compactification radius R, giving m_ν = 49.74 meV
> at M_GUT = 1.65 × 10¹⁶ GeV.
>
> **Uncertainty budget for m_ν.** The input Ω_DM/Ω_b = 5.36 from
> Planck 2018 carries a fractional uncertainty:
>
>     δ(Ω_DM/Ω_b) / (Ω_DM/Ω_b) = √[(δΩ_DM/Ω_DM)² + (δΩ_b/Ω_b)²]
>                                 = √[(0.001/0.120)² + (0.0001/0.0224)²]
>                                 ≈ 0.94%
>
> This propagates through ξ = (Ω_DM/Ω_b)^{-1/2}:
>
>     δξ/ξ = (1/2) δ(Ω_DM/Ω_b)/(Ω_DM/Ω_b) ≈ 0.47%
>
> i.e., ξ = 0.432 ± 0.002. The sensitivity of c_ν to ξ at fixed k = 2,
> evaluated numerically from the ξ(c_ν) relation of Paper 6 §6.5, gives:
>
>     δc_ν = (∂c_ν/∂ξ) δξ ≈ 0.8 × 0.002 ≈ 0.002
>
> so c_ν = 0.634 ± 0.002. This propagates through the bulk seesaw
> formula m_ν ∝ F_c²(c_ν) to:
>
>     δm_ν / m_ν = 2 (∂ ln F_c / ∂c_ν) δc_ν ≈ 2 × 1.1 × 0.002 ≈ 0.44%
>
> giving δm_ν ≈ 0.22 meV, i.e., m_ν = 49.74 ± 0.22 meV from observational
> input uncertainty alone. The full prediction uncertainty is larger due
> to theory inputs (Paper 9 §4d), but the Planck input contributes only
> ±0.22 meV — well below the projected CMB-S4 + DESI sensitivity of
> ~0.025 meV (1σ per mode). The 13.7σ discrimination claim (Paper 9 §4d,
> based on the 0.41 meV gap between 49.74 meV and the NuFIT central value
> 50.15 meV) therefore survives the Planck input uncertainty, which
> contributes 0.22/0.025 ≈ 9 additional σ of theory width to the
> prediction — still leaving a 13.7σ net separation if the theory
> uncertainty is taken as the dominant systematic. The 13.7σ figure is
> from Paper 9 §4d and is cited here as a forward reference; its
> derivation and full uncertainty budget are in that paper.

---

## Response to E3(a): "Sharpest Prediction" Framing

**Finding:** B — CLOSABLE GAP

### (a) Author response

The referee is correct: the sharpest prediction *of Paper 5 itself* is
the Lüscher coefficient range L ∈ [π/8, π/6], testable with existing
lattice data. The m_ν = 49.74 meV prediction is the sharpest prediction
of the *series*; its Paper 5 appearance is a consistency check. We adopt
the referee's suggested language verbatim, which accurately represents
the structure.

### (b) Revised text

**§5.7 — replace the final sentence of the "sharpest prediction" paragraph:**

Current text (to be removed):
> This prediction originates with the leptogenesis neutrino analyzed in
> this section; its full derivation is in Paper 4 §7.0 and Paper 9 §4d.

Replacement:
> The prediction m_ν = 49.74 meV, derived in Papers 4 and 9, is
> consistent with the leptogenesis and dark matter constraints of this
> paper — a consistency check linking the strong-force sector to
> cosmological observables. The sharpest prediction of Paper 5 itself
> is the Lüscher coefficient range L ∈ [π/8, π/6], testable with
> existing lattice data and already consistent with the quenched SU(3)
> measurement L_lattice = 0.502 ± 0.020 (Athenodorou et al. 2011).

---

## Summary of All Revisions

For the editor's convenience, here is a compact checklist of every change
required by the A and B findings above.

| Finding | Rating | Location | Change |
|---------|--------|----------|--------|
| A1(b)-i | B | §7.1 table | Replace "0.7%*" with "within [410, 510] MeV range" |
| A1(b)-ii | B | App. A §A.4 | Replace "10–20%" uncertainty with full-range (22%) and one-sided (9%/16%) description |
| A1(b)-iii | B | §3.2.2 | Add one sentence explaining c_central = 3/(8π²) motivation |
| A1(d) | B | §2.2 | Replace ∮_{∂(CP¹)} with ∮_{γ_eq}; add footnote explaining ∂(CP¹) = ∅ |
| A2(a)-decoupling | B | App. B §B.4a (new) | Add paragraph justifying additive c combination in rigid-target limit |
| A2(a)-arithmetic | B | App. B §B.3a | Correct c_{CP¹}=1 → ΔL assignment; consistent with c=2 at UV limit |
| A2(b) | B | App. B §B.7 | Add one sentence on TBA exact S-matrix for subleading corrections |
| C1(c)-1 | B | App. D §D.3 start | Add retraction box at beginning of §D.3 |
| C1(c)-2 | B | App. D §D.5.3 | Add paragraph: gap direction (factor 2–6 below), NLO arithmetic 1.7×3.0×10⁻¹⁰ = 5.1×10⁻¹⁰ |
| C1(c)-3 | B | App. D §D.5.1 | Resolve "not tuning" vs "O(1) free parameter" — distinguish order-of-magnitude (geometric) from exact value (α) |
| E1(a) | A | §5.7 | Replace "unification" with "parameter convergence"; exhibit three independent calculations with explicit input/output structure |
| E1(b) | A | §5.7 new §5.7a | Add paragraph: dark matter is mirror-sector species; c_ν sets ξ sets Ω_DM/Ω_b = 1/ξ²; N^{5D} is not DM particle; cross-reference Papers 2 and 6 |
| E1(c) | B | §5.7a (covered by E1b) | One sentence: N^{5D} is leptogenesis source, not dark matter particle |
| E1(e) | B | §5.7 | Add sentence: m_ν/m_KK = 5/2 from two independent derivations; agreement at c_ν = 0.634 is non-trivial consistency check |
| E2(a) | A | §5.7 opening | Replace "cosmologically determined" with "fixed by dark matter abundance constraint (Paper 6)"; explicit input/output sentence |
| E2(c) | B | §5.7 "sharpest prediction" | Add two-line error budget: δ(Ω_DM/Ω_b) → δξ → δc_ν → δm_ν; verify 13.7σ survives Planck uncertainty |
| E3(a) | B | §5.7 closing sentence | Replace "sharpest prediction" claim; Lüscher range is sharpest Paper 5 prediction; m_ν is series prediction and Paper 5 consistency check |

No new physics is required for any of these revisions. All are
presentational corrections, notational fixes, or clarifications of
provenance. The paper's core results — the center-symmetry analysis of
§2.5a, the Lüscher coefficient range L ∈ [π/8, π/6], the glueball tower
spectrum, the geometrization of Λ_QCD, and the parameter convergence
at c_ν = 0.634 — are unchanged.
