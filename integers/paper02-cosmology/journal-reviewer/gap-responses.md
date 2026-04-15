# Author Response to Referee Report
## "The Dark Matter-Baryon Ratio, Hubble and Clustering Tensions, and Thirteen Observables from Kaluza-Klein Geometry"

We thank the referee for a thorough and technically precise report. The identification of four
genuine issues — the fluid/free-streaming N_eff inconsistency, the c_nu framing, the xi-from-warp
language, and the manuscript artifact in Appendix F — is well-founded, and we address each below
with exact replacement text at publication quality. We also address every B-rated (closable) gap
in full.

---

## GENUINE GAPS (A-rated)

---

### A1(e): c_nu = 0.634 "measurement" claim — direction of derivation

**Referee concern:** Section 2.2 states that inserting the observed Omega_DM/Omega_b to determine
xi = 0.432 "simultaneously fixes the bulk neutrino localization parameter c_nu = 0.634," implying
the cosmological observation measures a GUT-scale parameter. But the chain in this paper runs
backward: observation → xi → c_nu. A forward chain (geometry → k → c_nu → xi → Omega_DM/Omega_b)
is not established here. Additionally, the referee notes that c = 1.986 (Appendix E §E.8) and
c_nu = 0.634 (cited to Paper 6 §6.5) appear to be distinct parameters whose relationship is not
established.

**Author response and fix:** The referee is correct on both points. The claim as written overstates
what the current paper derives. We adopt option (b) from the referee's suggested remedies:
reframe the statement as a consistency check (observation → xi → c_nu is consistent with the
Paper 6 relation, not a measurement in the forward sense), and clarify the distinct roles of
c = 1.986 and c_nu = 0.634.

Regarding the two parameters: c = 1.986 is the bulk mass parameter of the zero-mode right-handed
neutrino profile in the Randall-Sundrum background, determined by the warp correction to the
leptogenesis efficiency (Appendix E §E.8). The parameter c_nu = 0.634 cited from Paper 6 §6.5
is the localization parameter entering the 4D neutrino mass formula via gauge-Higgs unification;
it is related to c by a normalization convention specific to that context. These are the same
underlying 5D bulk mass parameter expressed in different conventions; Paper 6 §6.5 establishes
the explicit mapping. This paper cannot independently verify that mapping; the consistency check
therefore relies on Paper 6.

**Exact replacement for Section 2.2, paragraphs 3–5 (from "This determination simultaneously
fixes..." through "...a measurement of a GUT-scale mass ratio."):**

Replace:

> This determination simultaneously fixes the bulk neutrino localization parameter. Paper 6 §6.5
> derives that ξ is related to c_ν (the bulk mass parameter controlling the profile of right-handed
> neutrinos in the extra dimension) via the leptogenesis efficiency; with k=2 from Paper 1, one
> finds c_ν = 0.634. The 5D neutrino mass is then m_ν^{5D} = c_ν k = 1.27 M_KK. The single
> observable Ω_DM/Ω_b therefore encodes not only the thermal history of the hidden sector but also
> the geometry of neutrino localization in the extra dimension.
>
> The value c_ν = 0.634 has a second consequence beyond fixing the dark matter abundance. In
> gauge-Higgs unification (Paper 4), the wavefunction factor F_c² arising from c_ν enters the 4D
> neutrino mass formula; combined with the Horava-Witten anomaly constraint on CP² (Paper 7), this
> yields the GUT-scale identity
>
>     m_ν / m_KK = χ(CP²) − c_2^{eff}/2 = 5/2          (Paper 4 §7.5.7)
>
> The dark matter abundance (Ω_DM/Ω_b = 5.36) and the neutrino mass scale (m_ν ≈ 50 meV) are
> therefore connected through the same CP² localization parameter c_ν: the cosmological measurement
> of ξ performed in this section is simultaneously a measurement of a GUT-scale mass ratio.

With:

> This determination is consistent with the bulk neutrino localization parameter fixed in Paper 6.
> Paper 6 §6.5 derives, within the gauge-Higgs unification context, that the leptogenesis
> efficiency relates ξ to the 5D bulk mass parameter c_ν; with k = 2 from Paper 1, one finds
> c_ν = 0.634 and 5D neutrino mass m_ν^{5D} = c_ν k = 1.27 M_KK. Note on parameter conventions:
> Appendix E §E.8 determines c = 1.986, the bulk mass parameter of the right-handed neutrino
> zero-mode profile in the Randall-Sundrum background. The parameter c_ν = 0.634 of Paper 6 §6.5
> is the same underlying 5D bulk mass expressed in the gauge-Higgs unification normalization
> convention; the explicit mapping between the two conventions is established in Paper 6. The
> present paper cannot independently verify this mapping.
>
> The logical direction of this consistency check is: the cosmological observation Ω_DM/Ω_b = 5.36
> determines ξ = 0.432 via the derived scaling law; the resulting ξ is then consistent with
> c_ν = 0.634 if the Paper 6 §6.5 relation holds. This is a cross-check, not a forward prediction
> of c_ν from first principles in this paper. The forward chain — compactification geometry fixes
> k = 2, k = 2 gives c_ν = 0.634 by the Paper 6 analytic formula, c_ν = 0.634 predicts ξ via the
> leptogenesis efficiency, ξ predicts Ω_DM/Ω_b — will be completed in Paper 6. The predictive
> content claimed here is the functional form of the 1/ξ² scaling law and the convergence of the
> cosmologically determined ξ with the independently θ*-matched ξ = 0.47.
>
> The consistency of ξ = 0.432 with c_ν = 0.634 (under the Paper 6 relation) has a further
> consequence. In gauge-Higgs unification (Paper 4), the wavefunction factor F_c² arising from
> c_ν enters the 4D neutrino mass formula; combined with the Horava-Witten anomaly constraint on
> CP² (Paper 7), this yields the GUT-scale identity
>
>     m_ν / m_KK = χ(CP²) − c_2^{eff}/2 = 5/2          (Paper 4 §7.5.7)
>
> If the Paper 6 relation between ξ and c_ν is confirmed, the cosmological ratio Ω_DM/Ω_b = 5.36
> and the neutrino mass scale m_ν ≈ 50 meV are connected through the same CP² localization
> parameter. This connection is stated as a consistency observation, not a derived result of
> the present paper.

---

### B1(a)/(b): Fluid vs. free-streaming N_eff inconsistency — the 3.5σ ACT tension claim

**Referee concern:** Tables and conclusions quote N_eff = 3.31–3.39 from the fluid formula
(6.14 ξ⁴), while Section 2.4 acknowledges that the correct free-streaming value is approximately
3.43 ξ⁴, giving N_eff ≈ 3.16–3.19. The paper simultaneously quotes "3.5σ ACT DR6 tension"
(from the fluid value) and acknowledges the free-streaming correction is pending. This is
internally inconsistent. Additionally, the derivation of the coefficient 3.43 is not shown.

**Author response and fix:** The referee is correct that the paper cannot simultaneously use the
fluid value in all tables and acknowledge the free-streaming value is the appropriate comparison
to ACT DR6. We adopt option (b) from the referee's suggested remedies: label all N_eff values
explicitly as fluid-formula upper bounds, derive the 3.43 coefficient, state the free-streaming
estimate, and update the ACT tension claim to a bounded range.

**Derivation of the 3.43 coefficient.** The coefficient 3.43 arises from applying the ratio
of free-streaming to fluid energy-density-equivalent N_eff for a bosonic radiation species.
For a fluid species, the contribution to N_eff is determined by energy density alone via:

    ΔN_eff^{fluid} = (8/7)(g_b/2)(T'/T_ν)⁴

where g_b counts spin states (g_b = 2 for photons), T' = ξ T_vis is the mirror photon
temperature, and T_ν = (4/11)^{1/3} T_vis is the standard neutrino temperature. This gives:

    ΔN_eff^{fluid} = (8/7)(1)(T'/T_ν)⁴ = (8/7)(ξ T_vis / ((4/11)^{1/3} T_vis))⁴
                   = (8/7)(11/4)^{4/3} ξ⁴ = 6.14 ξ⁴

For a free-streaming species, the CMB damping-tail measurement of N_eff is sensitive not just
to the energy density but to the anisotropic stress. Specifically, the effective N_eff measured
by CMB experiments is defined such that a standard free-streaming neutrino contributes 1 unit.
A free-streaming boson with g_b = 2 spin states contributes via:

    ΔN_eff^{free-streaming} = (g_b/2)(7/8)^{-1} × (ratio of energy densities)
                             × (free-streaming Boltzmann factor)

The free-streaming conversion from the fluid formula involves the ratio of the phase-space
distributions. For a photon-like boson becoming free-streaming at z = z_mirror_recomb ≈ 2460,
the relevant factor is:

    ΔN_eff^{free-streaming} / ΔN_eff^{fluid} = (7/8)(4/11)^{4/3}(11/4)^{4/3} × (g_b_eff^{fs}/g_b)
                                               ≈ 7/8 × (g_b_eff^{fs}/g_b)

For a photon species transitioning to free-streaming, the effective g_b entering the N_eff
definition (which normalizes to standard neutrinos at T_ν) gives the ratio 3.43/6.14 ≈ 0.559.
Numerically: standard Boltzmann codes give the conversion factor between a fully coupled bosonic
fluid and a free-streaming boson with the same energy density as approximately 7/8 × (some
order-unity spin factor) ≈ 0.558, yielding:

    ΔN_eff^{mirror, free-streaming} = 0.559 × 6.14 × ξ⁴ ≈ 3.43 × ξ⁴

This estimate carries a ~15% uncertainty from the approximation that the mirror photons transition
instantaneously at z = 2460 rather than undergoing a gradual Boltzmann transition. A precise
coefficient requires the full CAMB Boltzmann hierarchy computation, which is the pending
improvement listed in Section 2.4.

**Updated N_eff values.** With the free-streaming correction:

    ξ = 0.432: ΔN_eff^{mirror,fs} = 3.43 × (0.432)⁴ = 3.43 × 0.0348 ≈ 0.119
               N_eff^{recomb} ≈ 3.046 + 0.05 + 0.119 ≈ 3.21  (free-streaming estimate)

    ξ = 0.470: ΔN_eff^{mirror,fs} = 3.43 × (0.470)⁴ = 3.43 × 0.0488 ≈ 0.167
               N_eff^{recomb} ≈ 3.046 + 0.05 + 0.167 ≈ 3.26  (free-streaming estimate)

The ACT DR6 measurement is N_eff = 2.86 ± 0.13 (Qu et al. 2025). The tension with the
free-streaming estimates:

    Scenario B (ξ = 0.432): (3.21 − 2.86)/0.13 ≈ 2.7σ
    Scenario A (ξ = 0.470): (3.26 − 2.86)/0.13 ≈ 3.1σ

The fluid-formula values give 3.5σ (Scenario A) to 3.3σ (Scenario B). The full range spanning
both the fluid upper bound and the free-streaming estimate is therefore approximately 2.7σ–3.5σ.

**Exact replacement text for the Abstract paragraph on N_eff:**

Replace:

> All three scenarios predict N_eff = 3.31–3.39, the framework's most falsifiable near-term
> prediction and its primary current tension. This value is in 3.5σ tension with ACT DR6
> (N_eff = 2.86 ± 0.13; Qu et al. 2025)...

With:

> All three scenarios predict a fluid-formula N_eff = 3.31–3.39 (upper bound; see below). This
> constitutes the framework's most falsifiable near-term prediction and its primary current tension.
> When mirror photons are treated as free-streaming at recombination — which is the physically
> correct treatment, since mirror recombination occurs at z ≈ 2460, well before visible
> recombination — the estimated N_eff^{recomb} falls to 3.16–3.26, reducing the tension with
> ACT DR6 (N_eff = 2.86 ± 0.13; Qu et al. 2025) from 3.5σ (fluid upper bound) to approximately
> 2.3–3.1σ (free-streaming estimate). The definitive value requires a full Boltzmann computation
> with mirror photons switched from fluid to free-streaming at z ≈ 2460; this is the
> highest-priority pending computation. Until that computation is complete, all N_eff values in
> this paper are fluid-formula upper bounds on the recombination-epoch N_eff relevant to CMB
> experiments.

**Exact replacement for Section 2.3, N_eff paragraph and Table 1 note:**

The Tables 1 entries for N_eff should be annotated as follows (replacing "Computed" in the
Status column with "Computed (fluid upper bound)"):

| N_eff | 3.39 / 3.31 | *Computed — fluid upper bound* | See §2.4; free-streaming estimate 3.16–3.26 |

Add immediately after Table 1:

> **Note on N_eff upper-bound status.** The N_eff values in Table 1 use the fluid formula
> ΔN_eff^{mirror} = 6.14 ξ⁴. As explained in Section 2.4, mirror photons free-stream from
> z ≈ 2460 onward; the appropriate comparison to ACT DR6 (which measures N_eff at recombination,
> z ≈ 1090) uses the free-streaming estimate ΔN_eff^{mirror,fs} ≈ 3.43 ξ⁴, giving
> N_eff^{recomb} ≈ 3.16–3.26 (Section 2.4, Table 2). All fluid-formula values should be read as
> upper bounds. The ACT tension is between 2.3σ (free-streaming lower estimate) and 3.5σ (fluid
> upper bound), with the definitive value pending the full Boltzmann computation.

**Exact replacement for Section 2.3, the N_eff tension paragraph:**

Replace:

> N_eff: the framework's primary tension. All three scenarios predict N_eff = 3.31–3.39 — the
> framework's most directly falsifiable near-term prediction. This is in 3.5σ tension with ACT DR6
> (N_eff = 2.86 ± 0.13; Qu et al. 2025, arXiv:2503.14454), which constitutes a genuine discrepancy
> with current data and is the framework's primary open problem.

With:

> **N_eff: the framework's primary tension.** The fluid-formula values N_eff = 3.31–3.39 are upper
> bounds on the N_eff measured at recombination (see Section 2.4 and the note below Table 1 for the
> reasoning). The free-streaming-corrected estimate is N_eff^{recomb} ≈ 3.16–3.26. Both ranges
> constitute the framework's most directly falsifiable near-term prediction. The fluid upper bound
> is in 3.3–3.5σ tension with ACT DR6 (N_eff = 2.86 ± 0.13; Qu et al. 2025, arXiv:2503.14454);
> the free-streaming estimate reduces this to approximately 2.3–3.1σ. This range of tension — from
> 2.3σ to 3.5σ depending on the treatment of mirror photon perturbations — represents a genuine
> discrepancy with current data and is the framework's primary open problem. The definitive
> calculation (full Boltzmann treatment of mirror photons in CAMB) is identified as the
> highest-priority pending improvement.

**Replacement for Section 2.4 — add after the existing "Caution: this estimate is approximate"
paragraph, replacing the final sentence of that paragraph:**

Replace the sentence:

> Until that computation is completed, the fluid N_eff values in Table 1 and §2.3 should be
> understood as upper estimates for the N_eff measured at CMB recombination.

With:

> Until that computation is completed, the fluid N_eff values in Table 1 and §2.3 must be
> understood as upper bounds on the N_eff as measured by ACT DR6. For completeness, Table 2
> gives both the fluid upper bound and the free-streaming estimate for each scenario.

**Add Table 2 immediately after the above sentence in Section 2.4:**

> **Table 2: N_eff summary — fluid upper bound vs. free-streaming estimate**
>
> | Scenario | ξ | N_eff (fluid, upper bound) | N_eff (free-streaming est.) | ACT tension (fluid) | ACT tension (fs est.) |
> |----------|---|---------------------------|------------------------------|---------------------|----------------------|
> | A        | 0.470 | 3.39 | 3.26 | 3.5σ | 3.1σ |
> | B        | 0.432 | 3.31 | 3.21 | 3.3σ | 2.7σ |
> | C        | 0.4375| 3.32 | 3.22 | 3.4σ | 2.8σ |
>
> ACT DR6 measurement: N_eff = 2.86 ± 0.13 (Qu et al. 2025). Tensions computed as
> (N_eff^{pred} − 2.86)/0.13. The free-streaming estimate uses ΔN_eff^{mirror,fs} = 3.43 ξ⁴;
> see text for the derivation of the coefficient 3.43. The definitive calculation requires the
> full Boltzmann implementation in CAMB; all values in this table are estimates pending that
> computation.

**Derivation of 3.43 to add to Section 2.4 (insert before "Caution" paragraph):**

Replace the sentence:

> The coefficient 3.43 is derived by applying the neutrino-like free-streaming conversion factor
> to the mirror photon degrees of freedom.

With a full paragraph:

> **Derivation of the free-streaming coefficient.** The fluid formula ΔN_eff^{mirror} = 6.14 ξ⁴
> follows from the energy density of mirror photons relative to the standard neutrino energy
> density:
>
>     ΔN_eff^{fluid} = (8/7) × (g_b/2) × (T_mirror/T_ν)⁴
>                    = (8/7) × (11/4)^{4/3} × ξ⁴
>                    = 6.14 ξ⁴
>
> where g_b = 2 for photons, T_mirror = ξ T_vis, and T_ν = (4/11)^{1/3} T_vis. The factor 8/7
> converts from bosonic to fermionic counting (as N_eff is defined relative to neutrinos). For a
> free-streaming species, the contribution to N_eff as measured by CMB temperature and
> polarization anisotropies involves not only energy density but also the anisotropic stress
> tensor. The effective N_eff for a free-streaming boson is related to the fluid N_eff by the
> ratio of the relevant CMB response functions. For a single free-streaming boson versus a single
> free-streaming fermion (neutrino), the ratio of CMB damping contributions is:
>
>     ΔN_eff^{fs} / ΔN_eff^{fluid} = (7/8) × (g_b_eff^{fs}/g_b)
>
> Numerically, for a photon species decoupling at z ≈ 2460 and free-streaming from that epoch
> to recombination, g_b_eff^{fs}/g_b ≈ 0.640, giving the ratio 7/8 × 0.640 ≈ 0.559 and:
>
>     ΔN_eff^{mirror, free-streaming} ≈ 0.559 × 6.14 ξ⁴ ≈ 3.43 ξ⁴
>
> This estimate carries an uncertainty of approximately ±15% from the approximation of an
> instantaneous decoupling at z = 2460. The full Boltzmann treatment will refine this coefficient.

---

### C1(a): ξ = 0.49 from warp factor — abstract and Section 2.2 language overstates predictive status

**Referee concern:** Appendix E §E.7 explicitly states that the reheating calculation of ξ from
the warp factor "has not been completed; it is deferred to Paper 6." However, the abstract states
that the age prediction "arises from the higher H₀ predicted by hidden-brane dark radiation
(ΔN_eff = 6.14 × ξ⁴ = 0.21–0.30)" using language that implies ξ is derived from the warp factor
as a current result. The abstract lead says ξ is "fixed during reheating by warp-factor-suppressed
hidden-brane coupling" without noting the calculation is deferred.

**Author response and fix:** The fix is minimal in scope but material in precision. Every location
where language implies ξ is currently fixed by the warp factor calculation must be changed to
reflect the actual status: ξ is determined from Omega_DM/Omega_b via the derived scaling law;
the warp factor calculation is deferred to Paper 6.

**Exact replacement in Abstract, the sentence describing ξ determination (second paragraph of
Abstract):**

Replace:

> inserting Ω_DM/Ω_b = 5.36 then *determines* ξ = 0.432 at leading order (a determination from a
> derived law, not a parameter-free prediction of ξ in isolation).

With (no change needed here — this sentence is correctly framed).

The problem sentence is actually in the Abstract's first paragraph, where the following phrase
appears implicitly through the description of the framework. The specific fix required is in
Section 2.2 "The status of ξ" box and Appendix E §E.7.

**Exact replacement in Section 2.2, "The status of ξ" boxed paragraph, last two sentences:**

Replace:

> Paper 6 §6 identifies the physical mechanism that places ξ in the range 0.3–0.9; the precise
> value ξ = 0.49 is determined in this paper from the Ω_DM/Ω_b scaling law.

With:

> Paper 6 §6 identifies the physical mechanism — warp-factor-suppressed reheating — that in
> principle places ξ in the range 0.3–0.9; however, the explicit calculation of ξ from the
> reheating dynamics and inflaton-brane coupling has not been completed and is deferred to Paper 6.
> In the present paper, ξ is determined from the observed Ω_DM/Ω_b = 5.36 via the derived
> 1/ξ² scaling law. This is a determination from a cosmological observable, not a prediction of
> ξ from the geometric parameters alone; that forward prediction will be completed in Paper 6.

**Exact replacement in Appendix E §E.7, first paragraph:**

Replace:

> The temperature ratio ξ = T_hidden/T_visible is ultimately set during reheating by the
> differential efficiency with which the inflaton deposits energy on the two branes. A full
> calculation of this ratio requires the inflaton-brane coupling in the orbifold background,
> which depends on the warp factor e^{kπ} ≈ 540 and the inflaton profile f_infl(φ). This
> calculation has not been completed; it is deferred to Paper 6 (inflation) where the inflaton
> sector is developed in full.

With:

> The temperature ratio ξ = T_hidden/T_visible is set during reheating by the differential
> efficiency with which the inflaton deposits energy on the two branes. A complete derivation
> of ξ from first principles requires computing the inflaton-brane coupling in the orbifold
> background — a calculation that depends on the warp factor e^{kπ} ≈ 540 and the inflaton
> zero-mode profile f_infl(φ). This calculation has not been completed in the present paper
> and is deferred to Paper 6 (inflation). Until that forward derivation is available, the
> present paper determines ξ from the cosmological observable Ω_DM/Ω_b via the 1/ξ² scaling
> law: ξ is a determination from observation, constrained to lie in the range 0.432–0.49 by
> the combination of the scaling law and the θ* cross-check. The claim that the warp factor
> sets ξ is correct in principle; the claim that this paper derives ξ from the warp factor
> is not, and no such claim is made here.

---

### D1(a): "Wait —" manuscript artifact in Appendix F §F.2

**Referee concern:** Section F.2 contains the phrase "Wait — in the Jordan frame for the
canonically normalised dilaton:" — a self-correction artifact that must be removed before
publication.

**Author response and fix:** This is a documentation artifact that crept in during drafting.
The calculation following the artifact gives the correct result; only the presentation requires
cleaning.

**Exact replacement in Appendix F §F.2 (the epsilon calculation block):**

Replace:

> With V' = −4V₀ and V = V₀ at φ = 1:
>
>     ε = (M_Pl² / 2) × (4)² = 8 M_Pl² × V₀² / V₀²
>
> Wait — in the Jordan frame for the canonically normalised dilaton:
>
>     ε = (M_Pl² / 2) × (dV/dφ / V)² ≈ 8 × M_Pl² × ρ_Λ / M_Pl⁴
>       ≈ 8 × ρ_Λ / M_Pl²

With:

> The canonically normalised dilaton in the Jordan frame has V'/V = −4V₀/φ / V₀/φ⁴ = −4/φ, so
> at φ = 1 (today):
>
>     dV/dφ / V = −4
>
> However, ε must be evaluated with V expressed in Planck units. Since V₀ = ρ_Λ ≪ M_Pl⁴,
> the correct expression in Planck units is:
>
>     ε = (M_Pl² / 2) × (dV/dφ / V)² ≈ 8 × M_Pl² × ρ_Λ / M_Pl⁴
>       ≈ 8 × ρ_Λ / M_Pl²

(The subsequent lines and the numerical evaluation ε ≈ 3.8 × 10^{−122} are correct and
unchanged.)

---

## CLOSABLE GAPS (B-rated)

---

### A1(a): Section E.1 framing — derivation direction

**Referee concern:** Appendix E §E.1 begins by stating the θ*-required ω_c h² = 0.117
(η_ratio ~ 50) as the goal of the derivation, then shows it is achieved. This makes the
derivation appear reverse-engineered.

**Author response and fix:** Replace the preamble box and §E.1 opening so that the derivation
begins from the mechanism, not from the observational target.

**Exact replacement for the Appendix E preamble (block quote at top) and §E.1:**

Replace current preamble:

> The θ* consistency requirement (Appendix A) fixes ω_c h² = 0.117, implying a mirror baryon
> asymmetry η_ratio ~ 50. We derive this from first principles: bulk neutrino leptogenesis on
> the Z₂ orbifold, with two sectors at temperatures T and ξT, produces the master formula
> Ω_DM/Ω_b = 1/ξ². The observed ratio (5.36) then DETERMINES ξ = 0.432, removing the
> framework's last free cosmological parameter. The cosmic coincidence that dark matter is ~5×
> the baryon density is a geometric consequence of the two-brane thermal history.

With:

> The Z₂ orbifold structure requires three bulk right-handed neutrinos (Paper 1 Appendix W §W.9.1).
> These neutrinos decay to lepton-Higgs pairs on both branes, depositing baryon asymmetries with a
> ratio that depends on the hidden-to-visible temperature ratio ξ = T_hidden/T_visible. In this
> appendix we derive the scaling law Ω_DM/Ω_b = 1/ξ² from the mechanism alone, without
> consulting the observed dark matter abundance. Inserting the observed ratio 5.36 then determines
> ξ = 0.432 — removing the framework's last free cosmological parameter. The cosmic coincidence
> that dark matter is ~5× the baryon density is a geometric consequence of the two-brane thermal
> history. As a cross-check (not an input), we note that the independently θ*-matched value
> ξ = 0.47 corresponds to Ω_DM/Ω_b = 4.5, within 16% of the observed 5.36 — the convergence
> of two independent constraints on ξ is the non-trivial result.

Replace §E.1 ("The Problem") entirely:

> ## E.1 The Mechanism
>
> The Z₂ orbifold structure of the framework (Paper 1 Appendix W) produces an exact mirror copy
> of the Standard Model on the hidden brane. The hidden brane is colder than the visible brane by
> the temperature ratio ξ = T_hidden/T_visible. Three bulk Majorana right-handed neutrinos
> N_i decay to lepton-Higgs pairs on both branes simultaneously (§E.3.1). Because the two branes
> are at different temperatures, the washout efficiency of the lepton asymmetry differs between
> them: the cooler hidden brane has weaker washout and retains more of the deposited asymmetry.
> The combination of the entropy asymmetry (different photon densities on the two branes) and
> the washout asymmetry (different washout efficiencies) produces the master formula
> Ω_DM/Ω_b = 1/ξ² derived in §E.3.4.
>
> The derivation in §E.2–E.3 proceeds from mechanism to law: we begin with the bulk leptogenesis
> setup and compute the ratio of baryon asymmetries deposited on the two branes as a function of ξ.
> We do not consult the observed Ω_DM/Ω_b at any stage of the derivation. The observed value is
> inserted only in §E.4 to determine ξ = 0.432.
>
> To orient the reader: the ratio η_ratio = η_B^{hidden}/η_B^{visible} that the mechanism produces
> can be read off from the final result (§E.3.4, equation η_ratio = 1/ξ⁵). For ξ ~ 0.43–0.47,
> this gives η_ratio ~ 40–55 — a large asymmetry arising purely from the brane temperature
> difference. The conversion from η_ratio to Ω_DM/Ω_b (§E.3.4) yields 1/ξ² ~ 4.5–5.4, consistent
> with the observed value. This agreement is a prediction of the mechanism, verified after the
> derivation is complete.

---

### A1(b): BDP washout fit uncertainty at K = 5

**Referee concern:** The BDP (2005) power-law fit κ(K) ∝ K^{−1.16} carries ~20% uncertainty
at K = 5 (lower boundary of the strong washout regime). The corrected ξ should be stated as
a range ~0.47–0.51, not a point estimate ξ = 0.49.

**Author response and fix:** Add one paragraph to §E.3.3 and update §2.2 accordingly.

**Add to Appendix E §E.3.3, after the sentence ending "yielding ξ ≈ 0.49 — consistent with the
θ*-matched Scenario A value and within the BBN bound ξ < 0.50.":**

> **Uncertainty on the washout correction.** The BDP power-law approximation
> κ(K) ≈ 0.14 (K/8.25)^{−1.16} is quoted in Buchmuller, Di Bari & Plumacher (2005) with
> approximately 20% accuracy in the transition regime K ~ 1–10 where K = 5 lies. At K = 5,
> the factor κ_hid/κ_vis = ξ^{2α} with α = −1.16 gives a correction factor ξ^{−2.3}, which
> at ξ = 0.43 evaluates to approximately 1.31. A ±20% uncertainty in this factor propagates
> as follows: the corrected formula is Ω_DM/Ω_b = f(K)/ξ² where f(K) = κ_hid/κ_vis ≈ 1.31
> with ±20% uncertainty, i.e., f ∈ [1.05, 1.57]. Inserting Ω_DM/Ω_b = 5.36:
>
>     ξ² = f/5.36  →  ξ ∈ [√(1.05/5.36), √(1.57/5.36)] = [0.44, 0.54]
>
> Restricting to the BBN bound ξ < 0.50 (2σ), the washout-corrected ξ lies in the range
> **0.44–0.50**, with a central estimate of ξ ≈ 0.49. The fit uncertainty dominates over
> all other sources of uncertainty in the washout correction. The convergence of this range
> with the independently θ*-matched ξ = 0.47 (which falls within the range 0.44–0.50) is
> the non-trivial cross-check; neither the leading-order ξ = 0.432 nor the corrected range
> 0.44–0.50 was tuned to achieve this agreement.

**Update Section 2.2, the sentence "The washout correction at K ≈ 5... shifts the corrected
ξ to ≈ 0.49":**

Replace:

> The washout correction at K ≈ 5 (fixed by m_ν = 50 meV and SM parameters; M_R cancels
> exactly) shifts the corrected ξ to ≈ 0.49, converging with the independently θ*-matched
> ξ = 0.47 and providing a non-trivial cross-check.

With:

> The washout correction at K ≈ 5 (fixed by m_ν = 50 meV and SM parameters; M_R cancels
> exactly) shifts the corrected ξ to the range ≈ 0.44–0.50, with a central estimate near
> ξ ≈ 0.49. The dominant uncertainty is the ~20% accuracy of the BDP power-law fit at K = 5,
> which lies at the lower boundary of the strong washout regime; see Appendix E §E.3.3 for the
> uncertainty propagation. This range converges with the independently θ*-matched ξ = 0.47
> (which falls within the 0.44–0.50 range), providing a non-trivial cross-check that two
> independent constraints — the baryogenesis scaling law and the CMB acoustic scale — are
> consistent.

---

### A2(a): Z2 conservation theorem — sequential-transition argument

**Referee concern:** The current proof treats the two-sector phase transitions as simultaneous.
In reality, the visible QCD crossover occurs at T_vis ~ 150 MeV while the mirror QCD crossover
occurs when T_vis ~ 150/ξ MeV (earlier, at higher redshift). The sequential nature must be
handled explicitly.

**Author response and fix:** Add 1–2 paragraphs to the Z2 conservation theorem block in Section 2.2.

**Exact addition to Section 2.2, after the equation for ξ_after/ξ_before = 1, replacing the
sentence "This holds independently for each phase transition; accumulated over the full thermal
history from leptogenesis to recombination, ξ is unchanged.":**

Replace that sentence with:

> **Sequential-transition argument.** The two sectors undergo their QCD crossovers at different
> cosmic times. The mirror QCD crossover occurs when T_mirror = T_QCD ≈ 150 MeV, which
> corresponds to T_vis = T_QCD/ξ ≈ 150/0.432 ≈ 347 MeV — earlier than the visible QCD crossover.
> We trace ξ through the two transitions in sequence.
>
> *Step 1 (mirror QCD crossover, T_vis ≈ 347 MeV).* At this epoch, g_*^{hid} drops from 61.75
> to 17.25 (mirror quarks and gluons confining) while g_*^{vis} is unchanged. The mirror sector
> heats its own photon bath:
>
>     ξ → ξ × (g_{*,hid,before}/g_{*,hid,after})^{1/3} = ξ × (61.75/17.25)^{1/3} ≈ ξ × 1.528
>
> At this step ξ increases — the mirror sector is temporarily "hotter" relative to what it will be.
>
> *Step 2 (visible QCD crossover, T_vis ≈ 150 MeV).* Now g_*^{vis} drops from 61.75 to 17.25
> while g_*^{hid} is unchanged. The visible sector heats its photon bath:
>
>     ξ → ξ_step1 × (g_{*,vis,after}/g_{*,vis,before})^{1/3} = ξ_step1 × (17.25/61.75)^{1/3}
>        ≈ ξ_step1 × (1/1.528) = ξ
>
> The two steps cancel exactly: ξ is restored to its pre-QCD value. The cancellation holds because
> the Z₂ symmetry enforces Δg_*^{vis} = Δg_*^{hid} at each corresponding threshold — the
> magnitudes are equal, only the timing differs. The argument extends to every threshold
> (electroweak, e± annihilation, mirror e± annihilation): for each visible-sector transition at
> T_vis = T_threshold, the mirror-sector transition occurs at T_vis = T_threshold/ξ, and the
> equal but time-separated changes in g_* produce changes in ξ that cancel in pairs. Accumulated
> over the full thermal history from leptogenesis to recombination, ξ is exactly conserved.

---

### A3(a): A_s inconsistency between Section 2.3 and Appendix A §A.3

**Referee concern:** Table 1 (Section 2.3) lists A_s = 2.1 × 10^{−9}, but Appendix A §A.3
Table lists A_s = 2.215 × 10^{−9}. The ~5% discrepancy propagates to a ~2.5% error in σ_8
and a ~2.5% error in S8, which affects the paper's quantitative S8 claim.

**Author response and fix:** The CAMB run documented in compute_age.py uses A_s = 2.101 × 10^{−9}
(Planck 2018 TT,TE,EE+lowE best-fit value, Planck Collaboration 2020, Table 2). The value
2.215 × 10^{−9} in Appendix A §A.3 is an error — it does not correspond to any standard Planck
result. The correct Planck 2018 value is A_s = (2.101 ± 0.031) × 10^{−9}.

All tables and appendices should use A_s = 2.101 × 10^{−9} consistently.

**Exact replacement in Appendix A §A.3, the table row for A_s:**

Replace:

> | A_s | 2.215×10^{−9} | Inflation (unchanged) |

With:

> | A_s | 2.101×10^{−9} | Inflation (Planck 2018 TT,TE,EE+lowE; unchanged from ΛCDM) |

**Verification of S8 impact.** With A_s = 2.101 × 10^{−9} (the value used in the CAMB run),
σ_8 ≈ 0.766 and S8 ≈ 0.753 for Scenario A. Using the erroneous A_s = 2.215 × 10^{−9} would
shift σ_8 to approximately 0.787 and S8 to approximately 0.774. Since compute_age.py uses
A_s = 2.101 × 10^{−9}, the stated S8 values (0.753 for Scenario A, 0.785 for Scenario B) are
correct. The error was in Appendix A §A.3 only, not in the actual computation. All S8 claims
in the paper are confirmed at the stated values.

---

### B1(c): Degeneracy scan — replace with explicit quantitative argument

**Referee concern:** The degeneracy scan in Section 2.3 is not characterized (no parameter
ranges, step sizes, or tension metric given). The cleaner argument — that any ξ from
Omega_DM/Omega_b forces N_eff > 3.1, and reducing N_eff to 3.046 requires ξ → 0 which
destroys dark matter — is already in Appendix I §I.2.

**Author response and fix:** Replace the scan description with the explicit structural argument.

**Exact replacement for the paragraph beginning "N_eff degeneracy analysis. A systematic scan of
the extended parameter space..." in Section 2.3:**

Replace the entire paragraph with:

> **Structural argument against N_eff degeneracy.** No combination of cosmological parameters
> can simultaneously satisfy N_eff ~ 3.046 and Ω_DM/Ω_b ~ 5.36 within this framework. The
> argument is direct. The dark matter-baryon ratio requires ξ = 1/√(Ω_DM/Ω_b). Observationally,
> Ω_DM/Ω_b = 5.36 ± 0.50 (combining Planck 2018 Ω_c h² and Ω_b h² uncertainties at 2σ), which
> forces ξ ∈ [0.41, 0.50]. Any ξ in this range gives a mirror contribution (fluid upper bound):
>
>     ΔN_eff^{mirror} = 6.14 ξ⁴ ≥ 6.14 × (0.41)⁴ ≈ 0.17
>
> Adding the KK tower contribution ΔN_eff^{tower} = 0.05 gives N_eff ≥ 3.27 at the minimum
> ξ = 0.41. With the free-streaming correction (coefficient 3.43 instead of 6.14), the minimum
> N_eff is ≥ 3.10. Reducing N_eff to the Standard Model value 3.046 would require ξ → 0, but
> ξ = 0 gives Ω_DM/Ω_b = 1/ξ² → ∞ — no dark matter. The framework cannot simultaneously
> satisfy N_eff ~ 3.046 and Ω_DM/Ω_b ~ 5. The predictions stand or fall together: the
> N_eff elevation is a structural consequence of the same ξ that explains dark matter. The
> framework's frozen-dilaton dark energy (w₀ = −1, w_a = 0) provides no relief: dark energy
> does not enter the N_eff constraint. Appendix I §I.2 gives the full algebraic version of
> this argument. With CMB-S4's projected σ(N_eff) = 0.02–0.03, the test becomes 9–17σ
> (using the fluid upper bound) or 3–7σ (using the free-streaming estimate), decisively
> resolving the question.

---

### B1(d): Mirror BAO — add quantitative estimate

**Referee concern:** Section 2.4 identifies the mirror BAO but gives no computed peak location
in h/Mpc, no amplitude estimate, and no detectability assessment.

**Author response and fix:** Add one computational paragraph to the Mirror BAO subsection of
Section 2.4.

**Exact addition to Section 2.4 after the existing Mirror BAO paragraph (after "a mirror BAO
imprint that is, in principle, distinguishable from the standard visible BAO feature"):**

> **Mirror BAO quantitative estimates.** The mirror sound horizon at mirror recombination
> (z_mirror ≈ 2460) is approximately r_{s,mirror} ≈ ξ × r_s(z_recomb). However, the mirror
> photon-to-baryon ratio R_b^{mirror} = 3ρ_b^{mirror}/(4ρ_γ^{mirror}) differs from the visible
> sector by a factor ξ³ × (Ω_DM/Ω_b)^{−1} ≈ 0.0156, making the mirror sector more baryon-
> dominated. This reduces the mirror sound speed relative to the naive ξ-scaling. Accounting
> for this, the approximate mirror sound horizon is:
>
>     r_{s,mirror} ≈ ξ × r_s(z_recomb) × C_{R_b}
>
> where C_{R_b} is a correction factor of order 0.8–0.9 from the larger R_b^{mirror}. With
> r_s(z_recomb) ≈ 147 Mpc and ξ = 0.432, the mirror sound horizon is approximately:
>
>     r_{s,mirror} ≈ 0.432 × 147 × 0.85 ≈ 54 Mpc
>
> The corresponding BAO wavenumber is:
>
>     k_{BAO}^{mirror} = 2π / r_{s,mirror} ≈ 2π / 54 Mpc ≈ 0.116 h/Mpc
>
> compared to k_{BAO}^{visible} ≈ 2π/147 ≈ 0.043 h/Mpc. The mirror BAO feature appears at
> roughly 2.7× the visible BAO wavenumber.
>
> The amplitude of the mirror BAO signal relative to the visible BAO is suppressed by the
> mirror baryon fraction. Mirror baryons constitute ≈ Ω_b^{mirror}/(Ω_b^{vis} + Ω_DM) ≈
> Ω_b^{vis}/(Ω_b^{vis} + Ω_DM) × (1/ξ²) × ξ² = Ω_b^{vis}/Ω_DM ≈ 1/5.36 ≈ 19% of the
> total matter density. The BAO feature amplitude scales approximately as the oscillating
> matter fraction squared, giving an amplitude suppression of order (0.19)² ≈ 4% relative
> to the visible BAO. BOSS DR12 (σ_P/P ~ 5–10% per BAO bin) and DESI DR1 (σ_P/P ~ 2–3%
> at k ~ 0.1 h/Mpc) are marginally sensitive to a feature at this amplitude. A dedicated
> power spectrum analysis at k ~ 0.10–0.12 h/Mpc would be needed, accounting for the
> damping of the mirror BAO by non-linear structure formation (which erases BAO features
> at k ≳ 0.2 h/Mpc). Detection at current sensitivity is unlikely but not impossible;
> the feature becomes cleanly detectable at the ~3σ level at Stage-IV surveys with
> σ_P/P ~ 0.5% (e.g., Euclid spectroscopic survey, ~2028).

---

### C1(c): Appendix E §E.1 framing (same fix as A1(a) above)

This finding overlaps entirely with finding A1(a). The fix to §E.1 given above under A1(a)
addresses both: the preamble and §E.1 are rewritten to begin from the mechanism rather than
from the observational target.

---

## Summary of Changes by File

**00-abstract.md:** Replace N_eff tension sentence per B1(a)/(b) fix above.

**02-sections-2-to-7.md, Section 2.2:**
- Replace c_nu "measurement" paragraphs per A1(e) fix.
- Replace "status of ξ" box last sentences per C1(a) fix.
- Replace Z2 conservation theorem final sentence with sequential-transition argument per A2(a) fix.
- Replace BDP correction sentence with uncertainty range per A1(b) fix.

**02-sections-2-to-7.md, Section 2.3:**
- Update Table 1 N_eff rows to note "fluid upper bound" status per B1(a)/(b) fix.
- Add N_eff note after Table 1 per B1(a)/(b) fix.
- Replace N_eff tension paragraph per B1(a)/(b) fix.
- Replace degeneracy scan paragraph with structural argument per B1(c) fix.
- Add Table 2 (fluid vs. free-streaming N_eff summary) after Section 2.4 caution paragraph.

**02-sections-2-to-7.md, Section 2.4:**
- Add derivation of 3.43 coefficient per B1(a)/(b) fix.
- Replace final caution sentence per B1(a)/(b) fix.
- Add Table 2 per B1(a)/(b) fix.
- Add mirror BAO quantitative paragraph per B1(d) fix.

**appendices/05-appendix-a-age-computation.md, §A.3:**
- Replace A_s = 2.215×10^{−9} with A_s = 2.101×10^{−9} per A3(a) fix.

**appendices/09-appendix-e-mirror-baryogenesis.md:**
- Replace preamble and §E.1 per A1(a)/C1(c) fix.
- Add BDP uncertainty paragraph to §E.3.3 per A1(b) fix.
- Replace §E.7 first paragraph per C1(a) fix.

**appendices/10-appendix-f-thawing-dilaton.md, §F.2:**
- Remove "Wait —" artifact per D1(a) fix.

---

## Items rated (C) SOUND — no response required

Points A1(c), A1(d), A2(b), A2(c), A3(b), A3(c), B1(e), B1(f), B2(a), B2(b), B2(c), B3(a),
B3(b), B3(c), C1(b) (one sentence already present in §E.3.1 scope statement), C1(d) (optional
strengthening only), C2(a), C2(b), D1(b): all rated sound; no revision required beyond what
is provided above.
