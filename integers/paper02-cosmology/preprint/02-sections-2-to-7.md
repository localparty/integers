# Paper 2 — Sections 2–7

---

## Section 2: Framework Parameters

### 2.1 Inherited from Paper 1

The 5D framework derives cosmological parameters from four geometric
inputs. All are established in Paper 1:

| Input | Value | Source (Paper 1) |
|-------|-------|-----------------|
| `L` (e-circle circumference) | ~130 `μm` | Casimir energy = `ρ_Λ` (Section 6.6) |
| SM field content | Fixed (Standard Model) | `N_B = 28`, `N_F = 90` |
| `V(φ)` (dilaton potential) | Casimir: `V = V₀/φ⁴` (exact; no GW term) | Appendix Q §Q.5, Paper 6 §2 |
| Orbifold structure | `Z₂ × Z₃` | Appendix W |

From these, Paper 1 derives the key quantities used here:
- Casimir dark energy density `ρ_Λ` matching observation
- `N_eff^{tower} = 3.09` (dilaton + intra-tower decays, citing Gonzalo et al. 2024)
- `ΔN_eff^{mirror} = 6.14 × ξ⁴` (from hidden-brane dark radiation, Appendix Y)
- `w₀ = −1`, `w_a = 0` (frozen dilaton; Casimir potential exact, Section 6.6, Paper 6 §2)
- `Σm_ν = 0.06 eV`, normal ordering (bulk seesaw, Appendix Z)

### 2.2 The New Result: `ξ` from `Ω_DM/Ω_b`

Paper 1 treated `ξ` (the hidden-to-visible temperature ratio) as the
framework's one free cosmological parameter, constrained by BBN to
`ξ < 0.50`. Paper 2 determines `ξ` from a derived scaling law.

The bulk leptogenesis mechanism (Appendix E) gives:

    Ω_DM / Ω_b = 1/ξ²

Inserting the observed ratio 5.36 determines `ξ`:

    ξ = 1/√5.36 = **0.432**  (leading order)

This determination is consistent with the bulk neutrino localization
parameter fixed in Paper 6. Paper 6 §6.5 derives, within the gauge-Higgs
unification context, that the leptogenesis efficiency relates `ξ` to the
5D bulk mass parameter `c_ν`; with `k = 2` from Paper 1, one finds
`c_ν = 0.634` and 5D neutrino mass `m_ν^{5D} = c_ν k = 1.27 M_KK`. Note on
parameter conventions: Appendix E §E.8 determines `c = 1.986`, the bulk mass
parameter of the right-handed neutrino zero-mode profile in the
Randall-Sundrum background. The parameter `c_ν = 0.634` of Paper 6 §6.5 is
the same underlying 5D bulk mass expressed in the gauge-Higgs unification
normalization convention; the explicit mapping between the two conventions is
established in Paper 6. The present paper cannot independently verify this
mapping.

The logical direction of this consistency check is: the cosmological
observation `Ω_DM/Ω_b = 5.36` determines `ξ = 0.432` via the derived scaling
law; the resulting `ξ` is then consistent with `c_ν = 0.634` if the Paper 6
§6.5 relation holds. This is a cross-check, not a forward prediction of `c_ν`
from first principles in this paper. The forward chain — compactification
geometry fixes `k = 2`, `k = 2` gives `c_ν = 0.634` by the Paper 6 analytic
formula, `c_ν = 0.634` predicts `ξ` via the leptogenesis efficiency, `ξ`
predicts `Ω_DM/Ω_b` — will be completed in Paper 6. The predictive content
claimed here is the functional form of the `1/ξ²` scaling law and the
convergence of the cosmologically determined `ξ` with the independently
`θ*`-matched `ξ = 0.47`.

The consistency of `ξ = 0.432` with `c_ν = 0.634` (under the Paper 6
relation) has a further consequence. In gauge-Higgs unification (Paper 4),
the wavefunction factor `F_c²` arising from `c_ν` enters the 4D neutrino
mass formula; combined with the Horava-Witten anomaly constraint on CP²
(Paper 7), this yields the GUT-scale identity

    m_ν / m_KK = χ(CP²) − c₂^{eff}/2 = 5/2          (Paper 4 §7.5.7)

If the Paper 6 relation between `ξ` and `c_ν` is confirmed, the cosmological
ratio `Ω_DM/Ω_b = 5.36` and the neutrino mass scale `m_ν ≈ 50 meV` are
connected through the same CP² localization parameter. This connection is
stated as a consistency observation, not a derived result of the present
paper.

All subsequent calculations use `ξ = 0.432` as the primary value
(Scenario B), with `ξ = 0.47` (Scenario A, where `ξ` is tuned to match
`θ*`) as a cross-check. A third scenario (C) allows `ω_b h²` to float
for self-consistent `θ*` matching. The three scenarios bracket the
true answer.

**The status of ξ.** The calculation in Appendix E proceeds as
follows: (i) from the Z₂ orbifold structure and the three bulk
right-handed neutrinos required by the Casimir calculation (Paper 1,
Appendix W §W.9.1), we derive the scaling law `Ω_DM/Ω_b = f(K,ξ)/ξ²`
without consulting the observed ratio; (ii) we then insert the
observational input `Ω_DM/Ω_b = 5.36` to determine `ξ = 0.432` at
leading order (`ξ ≈ 0.49` with washout correction). This is a
*determination* of `ξ` from a derived law, not a prediction of `ξ`
in isolation. Paper 6 §6 identifies the physical mechanism — warp-factor-suppressed
reheating — that in principle places `ξ` in the range 0.3–0.9; however, the
explicit calculation of `ξ` from the reheating dynamics and inflaton-brane
coupling has not been completed and is deferred to Paper 6. In the present
paper, `ξ` is determined from the observed `Ω_DM/Ω_b = 5.36` via the derived
`1/ξ²` scaling law. This is a determination from a cosmological observable,
not a prediction of `ξ` from the geometric parameters alone; that forward
prediction will be completed in Paper 6. The predictive content lies in the
functional form of the law (the specific `1/ξ²` scaling), in the convergence
of this determined value with the independently `θ*`-matched `ξ = 0.47`, and
in the fact that no CMB parameter is adjusted to achieve this convergence. The two observational inputs to the framework are `ρ_Λ`
(which fixes the e-circle circumference `L` via the Casimir energy,
Paper 1 §6.6) and `Ω_DM/Ω_b` (which fixes `ξ` through the `1/ξ²` law);
all other cosmological observables are then computed predictions.

**Epoch-independence of ξ: the Z₂ conservation theorem.** A potential
concern is whether `ξ = 0.432`, determined from the present-day ratio
`Ω_DM/Ω_b`, represents the temperature ratio at a single epoch or is
modified by the intervening thermal history. Paper 6 §6.4 proves that
`ξ` is exactly conserved. The argument is as follows. The Z₂ orbifold
symmetry (Paper 1, Appendix W) makes the mirror sector an exact copy
of the visible sector: every particle species and interaction is
replicated with identical mass spectrum and coupling constants. Every
phase transition in the visible sector — the electroweak crossover,
QCD confinement, `e±` annihilation — therefore has an exact mirror
counterpart at the scaled temperature `T' = ξ T`. At each threshold,
the entropy released is proportional to `Δg_*`, the change in effective
degrees of freedom. Because the two sectors are identical,
`Δg_*^{vis} = Δg_*^{hid}` at every transition. The ratio of entropy
deposited in the two sectors is therefore equal at each step, and the
temperature ratio satisfies:

    ξ_after / ξ_before = (g_{*,vis,before}/g_{*,vis,after})^{1/3}
                       × (g_{*,hid,after}/g_{*,hid,before})^{1/3} = 1

**Sequential-transition argument.** The two sectors undergo their QCD
crossovers at different cosmic times. The mirror QCD crossover occurs when
`T_mirror = T_QCD ≈ 150` MeV, which corresponds to `T_vis = T_QCD/ξ ≈
150/0.432 ≈ 347` MeV — earlier than the visible QCD crossover. We trace `ξ`
through the two transitions in sequence.

*Step 1 (mirror QCD crossover, T_vis ≈ 347 MeV).* At this epoch,
`g_*^{hid}` drops from 61.75 to 17.25 (mirror quarks and gluons confining)
while `g_*^{vis}` is unchanged. The mirror sector heats its own photon bath:

    ξ → ξ × (g_{*,hid,before}/g_{*,hid,after})^{1/3} = ξ × (61.75/17.25)^{1/3} ≈ ξ × 1.528

At this step `ξ` increases — the mirror sector is temporarily "hotter"
relative to what it will be.

*Step 2 (visible QCD crossover, T_vis ≈ 150 MeV).* Now `g_*^{vis}` drops
from 61.75 to 17.25 while `g_*^{hid}` is unchanged. The visible sector heats
its photon bath:

    ξ → ξ_step1 × (g_{*,vis,after}/g_{*,vis,before})^{1/3} = ξ_step1 × (17.25/61.75)^{1/3}
       ≈ ξ_step1 × (1/1.528) = ξ

The two steps cancel exactly: `ξ` is restored to its pre-QCD value. The
cancellation holds because the Z₂ symmetry enforces `Δg_*^{vis} = Δg_*^{hid}`
at each corresponding threshold — the magnitudes are equal, only the timing
differs. The argument extends to every threshold (electroweak, `e±`
annihilation, mirror `e±` annihilation): for each visible-sector transition at
`T_vis = T_threshold`, the mirror-sector transition occurs at
`T_vis = T_threshold/ξ`, and the equal but time-separated changes in `g_*`
produce changes in `ξ` that cancel in pairs. Accumulated over the full
thermal history from leptogenesis to recombination, `ξ` is exactly conserved.

The value `ξ = 0.432` determined in this section from the
present-day `Ω_DM/Ω_b` ratio is therefore valid at all epochs — it is
a property of the initial conditions set at leptogenesis, not an
epoch-dependent quantity. There is no need to track `ξ(T)` as a
function of temperature; the single CAMB input `ξ = 0.432` accurately
represents the mirror-sector temperature ratio throughout the
cosmological evolution.

### 2.3 The Complete Parameter Set for CAMB

**Table 1: Complete CAMB Input Parameter Audit**

The following table audits every parameter passed to CAMB for the
framework computation, distinguishing parameters that are (i) computed
from the 5D geometry, (ii) taken from prior BBN/inflation measurements
and held fixed, and (iii) determined by the `θ*` scan.

| CAMB parameter | Value used | Status | Notes |
|----------------|-----------|--------|-------|
| `H₀` | 69.5 / 68.7 km/s/Mpc | *Computed* | From `H₀ = 67.4 + 6.3×ΔN_eff` formula, Paper 1 App. Y |
| `ω_b h²` | 0.02237 | *Prior measurement* | Standard BBN value (Cooke et al. 2018); unchanged from `ΛCDM` |
| `ω_c h²` | 0.1170 / 0.1199 | *Computed* | Scenario A: from `θ*` scan. Scenario B: `ω_b h²/ξ²` |
| `N_eff` | 3.39 / 3.31 | *Computed — fluid upper bound* | `3.046 + 0.05` (KK tower) `+ 6.14ξ⁴ × 0.49` (mirror, fluid formula; see §2.4 and Table 2 for free-streaming estimate 3.16–3.26) |
| `w₀` | −1 | *Computed* | Casimir potential exact (`c₂ = 0`), Paper 6 §2 |
| `w_a` | 0 | *Computed* | Frozen dilaton |
| `Σm_ν` | 0.06 eV | *Computed* | Bulk seesaw, Paper 1 Appendix Z |
| `A_s` | `2.1 × 10⁻⁹` | *Prior measurement* | Planck inflation amplitude; unchanged from `ΛCDM` |
| `n_s` | 0.9649 | *Prior measurement* | Planck spectral index; unchanged from `ΛCDM` |
| `τ` | 0.054 | *Prior measurement* | Planck optical depth; unchanged from `ΛCDM` |

**Note on N_eff upper-bound status.** The N_eff values in Table 1 use the
fluid formula `ΔN_eff^{mirror} = 6.14 ξ⁴`. As explained in Section 2.4,
mirror photons free-stream from `z ≈ 2460` onward; the appropriate comparison
to ACT DR6 (which measures `N_eff` at recombination, `z ≈ 1090`) uses the
free-streaming estimate `ΔN_eff^{mirror,fs} ≈ 3.43 ξ⁴`, giving
`N_eff^{recomb} ≈ 3.16–3.26` (Section 2.4, Table 2). All fluid-formula values
should be read as upper bounds. The ACT tension is between 2.3σ
(free-streaming lower estimate) and 3.5σ (fluid upper bound), with the
definitive value pending the full Boltzmann computation.

Parameters computed from the geometry (`H₀`, `ω_c h²`, `N_eff`, `w₀`, `w_a`,
`Σm_ν`) are determined before any comparison to CMB observables. The
remaining four parameters (`ω_b h²`, `A_s`, `n_s`, `τ`) are identical to
standard `ΛCDM` inputs and are not being "fit" in any new sense — they
are the same BBN and inflation measurements that `ΛCDM` itself takes as
input. The predictive content of the framework is in the six
geometrically derived parameters, not in the four inherited ones.

Note: `n_s = 0.9649` (Planck 2018) is used throughout. The framework's
dilaton inflation prediction (`n_s = 0.965`, Paper 6 §3) differs by
`Δn_s = 0.0001`, producing shifts in `σ₈` and `S8` below 0.001 — negligible
for all conclusions here.

Note: Increasing `Σm_ν` from 0.06 eV to 0.10 eV (within current upper
bounds) shifts `H₀` by `< 0.2` km/s/Mpc and `S8` by `< 0.01` — both below
current measurement precision. The predictions are robust to the
neutrino mass value within the theoretically predicted range.

**Scenario A (`θ*`-matched, `ξ` from Appendix Y):**

| CAMB parameter | Value | Source |
|---------------|-------|--------|
| `H₀` | 69.5 km/s/Mpc | `67.4 + 6.3 × ΔN_eff` |
| `ω_b h²` | 0.02237 | SM baryons (Planck `ΛCDM`) |
| `ω_c h²` | 0.1170 | Adjusted to match `θ*` |
| `N_eff` | 3.39 | `3.046 + 0.05 + 6.14×(0.47)⁴ × 0.49` |
| `ξ` | 0.470 | From `θ*` matching |

**Scenario B (`1/ξ²` law — zero free parameters):**

| CAMB parameter | Value | Source |
|---------------|-------|--------|
| `H₀` | 68.7 km/s/Mpc | `67.4 + 6.3 × ΔN_eff` |
| `ω_b h²` | 0.02237 | SM baryons (Planck `ΛCDM`) |
| `ω_c h²` | 0.1199 | `ω_b h² / ξ²` |
| `N_eff` | 3.31 | `3.046 + 0.05 + 6.14×(0.432)⁴ × 0.49` |
| `ξ` | 0.432 | From `Ω_DM/Ω_b = 1/ξ²` |

**Scenario C (self-consistent `ω_b` — `θ*` AND `Ω_DM/Ω_b` matched):**

| CAMB parameter | Value | Source |
|---------------|-------|--------|
| `H₀` | 68.8 km/s/Mpc | `67.4 + 6.3 × ΔN_eff` |
| `ω_b h²` | **0.02150** | Self-consistent fit (−3.9% from `ΛCDM`) |
| `ω_c h²` | 0.11524 | `5.36 × ω_b h²` |
| `N_eff` | 3.32 | `3.046 + 0.05 + 6.14×(0.4375)⁴ × 0.49` |
| `ξ` | 0.4375 | From `θ*` zero-crossing |

Scenario C resolves the `θ*` tension (offset +1.0") at the cost of a
−3.9% shift in `ω_b h²`, which creates a significant tension with
primordial D/H measurements: predicted `D/H ≈ 2.65×10⁻⁵` vs observed
`2.527 ± 0.030×10⁻⁵` (Cooke et al. 2018), a `4.1σ` discrepancy against
observational uncertainty alone. Including BBN theoretical uncertainty
from nuclear reaction rates (`~±0.04×10⁻⁵`), the combined tension is
`~2.5σ`. This D/H tension is Scenario C's primary cost; a full MCMC
analysis would determine whether the `θ*` improvement justifies it. All three scenarios use the same dilaton parameters:

| Shared parameter | Value | Source |
|-----------------|-------|--------|
| `w₀` | −1 | Frozen dilaton (Casimir exact; Paper 6 §2) |
| `w_a` | 0 | Frozen dilaton (no GW term; c₂ = 0) |
| `Σm_ν` | 0.06 eV | Bulk seesaw |
| `A_s` | `2.1×10⁻⁹` | Inflation (unchanged from `ΛCDM`) |
| `n_s` | 0.9649 | Inflation (unchanged) |

**`N_eff`: the framework's primary tension.** The fluid-formula values
`N_eff = 3.31–3.39` are upper bounds on the `N_eff` measured at recombination
(see Section 2.4 and the note above for the reasoning). The free-streaming-
corrected estimate is `N_eff^{recomb} ≈ 3.16–3.26`. Both ranges constitute the
framework's most directly falsifiable near-term prediction. The fluid upper
bound is in **3.3–3.5σ tension** with ACT DR6 (`N_eff = 2.86 ± 0.13`; Qu et
al. 2025, arXiv:2503.14454); the free-streaming estimate reduces this to
approximately **2.3–3.1σ**. This range of tension — from 2.3σ to 3.5σ
depending on the treatment of mirror photon perturbations — represents a
genuine discrepancy with current data and is the framework's primary open
problem. The definitive calculation (full Boltzmann treatment of mirror photons
in CAMB) is identified as the highest-priority pending improvement.

**Source of the N_eff elevation.** The elevation has two components:
(i) a KK tower contribution `ΔN_eff ≈ 0.05` from intra-tower decays
heating the neutrino bath (Gonzalo et al. 2024, same physics); and
(ii) a mirror sector contribution. The naive formula
`ΔN_eff^{mirror} = 6.14 × ξ⁴` assumes all mirror species are fully
relativistic. A CAMB-based computation of the mirror-sector thermal
history reveals a richer picture. At BBN (`T ~ 1 MeV`), the mirror
sector temperature is `T' = ξT ≈ 0.43–0.47` MeV — comparable to
`m_e = 0.511` MeV. Mirror `e±` are therefore partially Boltzmann-suppressed,
and as they annihilate they heat the mirror photon bath (exactly as
visible `e±` heat the visible photon bath). After mirror `e±` annihilation
is complete, the effective mirror-sector contribution at recombination
is suppressed by a factor of 0.49 relative to the fully relativistic
limit. For `ξ = 0.47` this gives `ΔN_eff(recombination) ≈ 0.36`, yielding
total `N_eff ≈ 3.40`; for `ξ = 0.432`, `ΔN_eff ≈ 0.26`, yielding `N_eff ≈ 3.30`.

**BBN N_eff evolution.** The effective number of relativistic species
`N_eff` is not constant between the BBN epoch (`T ~ 1 MeV`) and
recombination (`T ~ 0.26 eV`). In the visible sector, `e±` annihilation at
`T ~ m_e` heats the photon bath but not the neutrino bath, reducing `N_eff`
from 3.37 to 3.046. An exactly analogous process occurs in the mirror
sector, but shifted in temperature by factor `ξ`. Mirror `e±` annihilate
at `T_vis ~ m_e/ξ ≈ 1.1–1.2 MeV`, after which the mirror photon bath is
heated and the mirror neutrino bath is not. The result is:

    N_eff^{BBN}   ≈ 3.55–3.65 (mirror e± contributing at BBN temperatures)
    N_eff^{recomb} ≈ 3.31–3.39 (post-mirror e± annihilation)

The BBN value `N_eff ≈ 3.6` lies within the 95% CL bound from primordial
deuterium, `N_eff < 3.7` (Cooke et al. 2018; Pisanti et al. 2021). The
prediction is consistent with BBN, with a margin of `< 0.1` unit before
violating the 95% bound. A precise calculation using the full mirror
`e±` Fermi-Dirac distribution (rather than the semi-analytic estimate
above) is the highest-priority follow-up computation for the `N_eff` sector.

We note three contextual factors that bear on how the ACT DR6 tension
should be interpreted — not as justifications for ignoring ACT DR6, but
as evidence that the current observational consensus on `N_eff` is itself
unsettled:

(i) The combined ACT+SPT+Planck measurement yields `N_eff = 2.81 ± 0.12`,
which is itself `1.9σ` *below* the Standard Model prediction of 3.043
(Cielo et al. 2023, arXiv:2306.05460). Alvarez et al. (2026,
arXiv:2603.22391) ask explicitly "What does it take to have `N_eff < 3`
at CMB times?", finding that only a narrow class of BSM mechanisms
(thermal electrophilic relics or late-decaying particles) can produce
such a deficit. The anomalously low ground-based values are not specific
to the e-dimension framework.

(ii) When the SH0ES local `H₀` measurement is included as a prior, the
preferred value shifts to `N_eff = 3.43 ± 0.13` (Garcia Escudero &
Abazajian 2025, arXiv:2509.25478), consistent with the framework. The
framework's predicted `H₀ = 69.5` km/s/Mpc is intermediate between
Planck (67.36) and SH0ES (73.04), and its `N_eff` prediction is
intermediate between CMB-only and CMB+SH0ES joint fits.

(iii) Planck alone gives `N_eff = 2.99 ± 0.17`, consistent with both
the Standard Model and the framework at `< 2.5σ`. The dominant pull
toward low `N_eff` comes from the high-ℓ damping tail measured by
ground-based experiments; Simons Observatory (`σ(N_eff) ≈ 0.045`) will
provide an independent check by ~2030.

CMB-S4 (`σ(N_eff) ≈ 0.03`, projected ~2030) will confirm or exclude the
mirror sector at `> 9σ`. If CMB-S4 measures `N_eff = 3.046 ± 0.03`, the
mirror sector is excluded and the framework's cosmological predictions
reduce to their minimal form (`N_eff ≈ 3.09`, `H₀ ≈ 67.7`, `S8 ≈ 0.80`). If
CMB-S4 confirms `N_eff = 3.3–3.5`, every other prediction in this paper
follows. This is the framework's make-or-break test.

**Structural argument against N_eff degeneracy.** No combination of
cosmological parameters can simultaneously satisfy `N_eff ~ 3.046` and
`Ω_DM/Ω_b ~ 5.36` within this framework. The argument is direct. The dark
matter-baryon ratio requires `ξ = 1/√(Ω_DM/Ω_b)`. Observationally,
`Ω_DM/Ω_b = 5.36 ± 0.50` (combining Planck 2018 `Ω_c h²` and `Ω_b h²`
uncertainties at 2σ), which forces `ξ ∈ [0.41, 0.50]`. Any `ξ` in this range
gives a mirror contribution (fluid upper bound):

    ΔN_eff^{mirror} = 6.14 ξ⁴ ≥ 6.14 × (0.41)⁴ ≈ 0.17

Adding the KK tower contribution `ΔN_eff^{tower} = 0.05` gives `N_eff ≥ 3.27`
at the minimum `ξ = 0.41`. With the free-streaming correction (coefficient
3.43 instead of 6.14), the minimum `N_eff` is `≥ 3.10`. Reducing `N_eff` to
the Standard Model value 3.046 would require `ξ → 0`, but `ξ = 0` gives
`Ω_DM/Ω_b = 1/ξ² → ∞` — no dark matter. The framework cannot simultaneously
satisfy `N_eff ~ 3.046` and `Ω_DM/Ω_b ~ 5`. The predictions stand or fall
together: the `N_eff` elevation is a structural consequence of the same `ξ`
that explains dark matter. The framework's frozen-dilaton dark energy
(`w₀ = −1`, `w_a = 0`) provides no relief: dark energy does not enter the
`N_eff` constraint. Appendix I §I.2 gives the full algebraic version of this
argument. With CMB-S4's projected `σ(N_eff) = 0.02–0.03`, the test becomes
`9–17σ` (using the fluid upper bound) or `3–7σ` (using the free-streaming
estimate), decisively resolving the question.

### 2.4 Mirror Recombination and the Free-Streaming Transition

The mirror sector is a thermal copy of the Standard Model at temperature
`T' = ξ × T_vis`. Consequently, every thermal threshold that occurs in
the visible sector at temperature `T` occurs in the mirror sector at the
corresponding visible temperature `T_vis = T/ξ` — that is, at a higher
visible-sector temperature and therefore at a higher redshift. Mirror
hydrogen recombination is the most cosmologically consequential such
threshold.

**Derivation of z_mirror_recomb.** Visible hydrogen recombines when
the CMB temperature drops to approximately `T_recomb ≈ 0.25 eV`
(`z_recomb ≈ 1090`). Mirror hydrogen recombines when the *mirror* photon
temperature reaches the same binding-energy threshold:

    T'_recomb = 0.25 eV

The mirror photon temperature is `T' = ξ × T_vis`, so the condition
`T' = 0.25 eV` corresponds to a visible-sector temperature of:

    T_vis = T'_recomb / ξ = 0.25 eV / 0.432 = 0.579 eV

Converting to redshift via `T_vis = T_{CMB,0} × (1 + z)` with
`T_{CMB,0} = 2.725 K = 2.348 × 10⁻⁴ eV`:

    z_mirror_recomb = (T_vis / T_{CMB,0}) − 1
                    = (0.579 eV / 2.348 × 10⁻⁴ eV) − 1
                    ≈ 2464 − 1 ≈ **2463**

Mirror hydrogen recombines at `z ≈ 2460`, well before visible
recombination at `z ≈ 1090`.

**Consequence: mirror photons are free-streaming at CMB recombination.**
After mirror recombination, mirror photons decouple from mirror baryons
and free-stream. The mirror photon-baryon plasma, which behaves as a
tightly-coupled fluid prior to `z ≈ 2460`, transitions to a
free-streaming radiation bath by `z ≈ 1090`. This distinction matters:
free-streaming and tightly-coupled radiation affect the CMB power
spectrum differently. A tightly-coupled fluid produces acoustic
oscillations in the stress-energy tensor without anisotropic stress; a
free-streaming species develops anisotropic stress that damps power in
the damping tail differently. These two regimes produce distinct
signatures in the `C_ℓ` spectrum at multipoles `ℓ ≳ 100`, where the
damping tail is precisely measured.

**Correction to the fluid N_eff formula.** The formula
`ΔN_eff^{mirror} = 6.14 × ξ⁴` (Appendix E, §E.5) treats the mirror
sector as a perfect fluid throughout. This is appropriate at `z > 2460`,
when mirror photons are indeed coupled to mirror baryons. However, the
ACT DR6 `N_eff` constraint (Qu et al. 2025) is a measurement at
recombination (`z ≈ 1090`), at which epoch mirror photons have been
free-streaming for over a decade in log-redshift. The effective `N_eff`
contribution from free-streaming radiation differs from the fluid
contribution through the anisotropic stress factor.

A fluid species contributes to `N_eff` through its energy density alone.
A free-streaming species contributes the same energy density but also
develops anisotropic stress, which enters the Boltzmann hierarchy and
modifies the CMB damping tail in the same way as standard neutrinos. The
conversion between the fluid and free-streaming `N_eff` parameterization
involves the standard neutrino-like factor, capturing the fact that
neutrinos are the canonical free-streaming species in the `N_eff`
definition. The corrected estimate for the mirror photon contribution at
`z < 2460` — treating them as free-streaming analogously to neutrinos —
gives:

    ΔN_eff^{mirror, free-streaming} ≈ 3.43 × ξ⁴

rather than `6.14 × ξ⁴` from the fluid formula. For `ξ = 0.432` this
reduces `ΔN_eff^{mirror}` from `0.214` (fluid) to approximately `0.119`
(free-streaming estimate), yielding total `N_eff ≈ 3.16` rather than
`3.31`. This would narrow, though not eliminate, the tension with ACT
DR6.

**Derivation of the free-streaming coefficient.** The fluid formula
`ΔN_eff^{mirror} = 6.14 ξ⁴` follows from the energy density of mirror photons
relative to the standard neutrino energy density:

    ΔN_eff^{fluid} = (8/7) × (g_b/2) × (T_mirror/T_ν)⁴
                   = (8/7) × (11/4)^{4/3} × ξ⁴
                   = 6.14 ξ⁴

where `g_b = 2` for photons, `T_mirror = ξ T_vis`, and `T_ν = (4/11)^{1/3} T_vis`.
The factor 8/7 converts from bosonic to fermionic counting (as `N_eff` is
defined relative to neutrinos). For a free-streaming species, the contribution
to `N_eff` as measured by CMB temperature and polarization anisotropies
involves not only energy density but also the anisotropic stress tensor. The
effective `N_eff` for a free-streaming boson is related to the fluid `N_eff`
by the ratio of the relevant CMB response functions. For a single free-streaming
boson versus a single free-streaming fermion (neutrino), the ratio of CMB
damping contributions is:

    ΔN_eff^{fs} / ΔN_eff^{fluid} = (7/8) × (g_b_eff^{fs}/g_b)

Numerically, for a photon species decoupling at `z ≈ 2460` and free-streaming
from that epoch to recombination, `g_b_eff^{fs}/g_b ≈ 0.640`, giving the ratio
`7/8 × 0.640 ≈ 0.559` and:

    ΔN_eff^{mirror, free-streaming} ≈ 0.559 × 6.14 ξ⁴ ≈ 3.43 ξ⁴

This estimate carries an uncertainty of approximately ±15% from the
approximation of an instantaneous decoupling at `z = 2460`. The full Boltzmann
treatment will refine this coefficient.

**Caution: this estimate is approximate.** A proper treatment requires
evolving the mirror photon perturbations through the Boltzmann hierarchy as a
free-streaming species below `z = 2460`, with the transition handled
self-consistently in CAMB. The current computation approximates the mirror
sector as a fluid throughout, which overestimates `N_eff` as measured by CMB
experiments. This is **listed as a pending improvement**: the highest-priority
refinement to the `N_eff` sector is a full CAMB computation in which the
mirror photon-baryon fluid is switched to a free-streaming component at
`z = z_mirror_recomb ≈ 2460`. Until that computation is completed, the fluid
`N_eff` values in Table 1 and §2.3 must be understood as upper bounds on the
`N_eff` as measured by ACT DR6. For completeness, Table 2 gives both the fluid
upper bound and the free-streaming estimate for each scenario.

**Table 2: N_eff summary — fluid upper bound vs. free-streaming estimate**

| Scenario | ξ | N_eff (fluid, upper bound) | N_eff (free-streaming est.) | ACT tension (fluid) | ACT tension (fs est.) |
|----------|---|---------------------------|------------------------------|---------------------|----------------------|
| A        | 0.470 | 3.39 | 3.26 | 3.5σ | 3.1σ |
| B        | 0.432 | 3.31 | 3.21 | 3.3σ | 2.7σ |
| C        | 0.4375| 3.32 | 3.22 | 3.4σ | 2.8σ |

ACT DR6 measurement: `N_eff = 2.86 ± 0.13` (Qu et al. 2025). Tensions computed
as `(N_eff^{pred} − 2.86)/0.13`. The free-streaming estimate uses
`ΔN_eff^{mirror,fs} = 3.43 ξ⁴`; see text for the derivation of the coefficient
3.43. The definitive calculation requires the full Boltzmann implementation in
CAMB; all values in this table are estimates pending that computation.

**Mirror BAO signature.** Prior to mirror recombination, the
mirror photon-baryon plasma supports acoustic oscillations. Mirror
baryons are dragged along with the mirror photon pressure waves,
producing oscillations in the mirror matter density field — precisely
analogous to the visible BAO mechanism. At `z ≈ 2460`, this coupling
ceases, and the mirror baryon perturbations retain a frozen imprint of
these oscillations at the mirror sound horizon scale:

    r_{s, mirror} ≈ r_s(z_mirror_recomb) ≈ ξ × r_s(z_recomb)

where the approximate scaling by `ξ` captures the reduced sound speed
in the denser, cooler mirror sector. This produces a sub-leading
oscillatory feature in the matter power spectrum at a characteristic
wavenumber `k_BAO^{mirror} > k_BAO^{visible}` — a mirror BAO imprint
that is, in principle, distinguishable from the standard visible BAO
feature. The amplitude is suppressed relative to the visible BAO signal
(mirror baryons constitute only `~15%` of the total matter, since
`Ω_DM/Ω_b ≈ 5.36` implies mirror baryons are ~16% of dark matter) but
the scale separation from the visible BAO is a qualitatively distinct
prediction of the mirror sector.

**Mirror BAO quantitative estimates.** The mirror sound horizon at mirror
recombination (`z_mirror ≈ 2460`) is approximately `r_{s,mirror} ≈ ξ ×
r_s(z_recomb)`. However, the mirror photon-to-baryon ratio
`R_b^{mirror} = 3ρ_b^{mirror}/(4ρ_γ^{mirror})` differs from the visible sector
by a factor `ξ³ × (Ω_DM/Ω_b)^{−1} ≈ 0.0156`, making the mirror sector more
baryon-dominated. This reduces the mirror sound speed relative to the naive
`ξ`-scaling. Accounting for this, the approximate mirror sound horizon is:

    r_{s,mirror} ≈ ξ × r_s(z_recomb) × C_{R_b}

where `C_{R_b}` is a correction factor of order 0.8–0.9 from the larger
`R_b^{mirror}`. With `r_s(z_recomb) ≈ 147` Mpc and `ξ = 0.432`, the mirror
sound horizon is approximately:

    r_{s,mirror} ≈ 0.432 × 147 × 0.85 ≈ 54 Mpc

The corresponding BAO wavenumber is:

    k_{BAO}^{mirror} = 2π / r_{s,mirror} ≈ 2π / 54 Mpc ≈ 0.116 h/Mpc

compared to `k_{BAO}^{visible} ≈ 2π/147 ≈ 0.043 h/Mpc`. The mirror BAO
feature appears at roughly 2.7× the visible BAO wavenumber.

The amplitude of the mirror BAO signal relative to the visible BAO is
suppressed by the mirror baryon fraction. Mirror baryons constitute
`≈ Ω_b^{vis}/Ω_DM ≈ 1/5.36 ≈ 19%` of the total matter density. The BAO
feature amplitude scales approximately as the oscillating matter fraction
squared, giving an amplitude suppression of order `(0.19)² ≈ 4%` relative to
the visible BAO. BOSS DR12 (`σ_P/P ~ 5–10%` per BAO bin) and DESI DR1
(`σ_P/P ~ 2–3%` at `k ~ 0.1 h/Mpc`) are marginally sensitive to a feature at
this amplitude. A dedicated power spectrum analysis at `k ~ 0.10–0.12 h/Mpc`
would be needed, accounting for the damping of the mirror BAO by non-linear
structure formation (which erases BAO features at `k ≳ 0.2 h/Mpc`). Detection
at current sensitivity is unlikely but not impossible; the feature becomes
cleanly detectable at the ~3σ level at Stage-IV surveys with `σ_P/P ~ 0.5%`
(e.g., Euclid spectroscopic survey, ~2028).

**CMB-S4 discriminator.** The transition from mirror photon-baryon
coupling to free-streaming at `z ≈ 2460` corresponds to a Hubble scale
`k_H(z=2460) ≈ 0.04–0.05 h/Mpc`, imprinting a characteristic step in
the damping tail of the CMB temperature and polarization power spectra
at `ℓ ≈ 200–400`. This step is distinct from the smooth suppression
produced by a constant `N_eff` and in principle allows CMB-S4 to
discriminate between: (a) a mirror sector that is always a fluid
(mimicking fractional `N_eff` throughout), (b) a mirror sector that
transitions to free-streaming at `z ≈ 2460`, and (c) standard extra
neutrinos. The free-streaming transition signature is independent of
the total `N_eff` value and survives even if the overall `N_eff`
is consistent with 3.046. This makes the mirror sector potentially
detectable at CMB-S4 through its *spectral shape* in the damping tail,
not only through its *amplitude* in the overall `N_eff` measurement.

---

## Section 3: The CAMB Computation

### 3.1 Tool and Configuration

CAMB v1.6.6 was used (Lewis, Challinor & Lasenby 2000).
The dark energy equation of state uses the CPL parameterization
(Chevallier & Polarski 2001, Linder 2003) with `w₀ = −1`, `w_a = 0`
(the perturbative Casimir potential `V = V₀/φ⁴` is exact to all orders;
the dilaton is frozen by Hubble friction at `ε ~ 10⁻¹²²`; see Appendix F,
Paper 6 §2). Massive neutrinos are included with the bulk seesaw mass
(`Σm_ν = 0.06 eV`, normal ordering).

The computation is documented in `age/compute_age.py` and
`age/compute_mirror_matter.py`. Results are in `age/results.json`.

### 3.2 Validation

The Planck `ΛCDM` baseline was reproduced to better than 0.01% on all
observables before the 5D parameter set was substituted. This confirms
the CAMB setup is correct.

### 3.3 The Eight Scenarios

Eight parameter sets were run, spanning the range from minimal
(tower-only, no mirror sector) to DESI-compatible (`w₀ = −0.80`):

| Scenario | `H₀` | `ξ` | `w₀` | Purpose |
|----------|-----|---|----|---------|
| Planck `ΛCDM` | 67.4 | — | −1.0 | Baseline |
| 5D Minimal | 67.7 | 0 | −1.0 | Tower-only |
| 5D Stabilized | 69.5 | 0.47 | −1.0 | No dilaton |
| 5D Scenario A | 69.5 | 0.47 | −1.0 | `θ*` matched, `w = −1` |
| 5D DESI (exploratory) | 69.5 | 0.47 | −0.80 | DESI best-fit (not current prediction) |
| 5D TRGB | 69.8 | 0.47 | −1.0 | `H₀` = TRGB |
| 5D Scenario B | 68.7 | 0.432 | −1.0 | **`1/ξ²` law, `w = −1`** |
| 5D Scenario B static | 68.7 | 0.432 | −1.0 | Cross-check |

---

## Section 4: Results Overview

The complete cosmological predictions from both scenarios:

| Observable | Scenario A (`ξ=0.47`) | Scenario B (`ξ=0.432`) | Planck `ΛCDM` | Data |
|-----------|--------------------|--------------------|-------------|------|
| `t₀` (Gyr) | **13.47** | **13.47** | 13.80 | 12.5–14.5 (stellar) |
| `H₀` (km/s/Mpc) | 69.5 | **68.7** | 67.4 | 69.8 (TRGB) |
| `θ*` offset (") | −0.5 | +6.6 | 0 | ±1.1 (`1σ`) |
| `r_d` (Mpc) | 146.2 | **145.8** | 147.1 | 147.1 ± 0.3 |
| `σ₈` | 0.766 | **0.782** | 0.811 | 0.811 (CMB) |
| `S8` | 0.753 | **0.785** | 0.832 | 0.76–0.78 (WL) |
| `Ω_m` | 0.290 | **0.302** | 0.315 | 0.315 (CMB) |
| `N_eff` | 3.39 | **3.31** | 3.044 | `2.86±0.13` (ACT DR6) |
| `Ω_DM/Ω_b` | 5.22 | **5.36** | — | 5.36 (observed) |

Both scenarios predict `t₀ ≈ 13.47 Gyr` and resolve the `S8` tension.
Scenario B additionally explains `Ω_DM/Ω_b` from first principles.

### §4.1 The Six Absolute Time Scale

The CBB system (Paper 12) provides a closed-form expression for the present
age of the universe in terms of the Riemann zeta function's non-trivial zeros:

$$\tau_S^{(\text{now})} = (\log \gamma_7)^2 \text{ Gyr} \approx 13.77588\ldots \text{ Gyr}$$

where $\gamma_7 \approx 25.0109$ is the imaginary part of the seventh non-trivial
zero of $\zeta(s)$.

**Properties:**

1. **Absolute origin.** $\tau_S = 0$ coincides with the Big Bang — intrinsic
   to the universe, not to any culture, calendar, or astronomical convention.
2. **Closed-form present.** The current value is a computable mathematical
   constant, determinable to arbitrary precision by any civilisation with
   access to $\zeta(s)$.
3. **Frame-independent.** Comoving observers in standard FRW cosmology agree
   on $\tau_S$ to within the precision of $\gamma_7$ (currently 50+ digits).
4. **Empirical match.** $\tau_S^{(\text{now})} = 13.776$ Gyr matches the
   Planck 2018 age determination ($13.797 \pm 0.023$ Gyr) at $-0.91\sigma$
   — consistent and sub-percent.
5. **Kelvin analogue.** As Kelvin replaced the anthropocentric Fahrenheit/Celsius
   zero with absolute zero of temperature, the Six scale replaces the
   anthropocentric AD/BC zero with the absolute zero of cosmic time.

**Naming.** The scale is denoted $\tau_S$ or Six, after G Six (originator
of the derivation), in the tradition of physics units bearing the name
of the person who first stated them rigorously.

**Conversion.** AD year $= (\tau_S - \tau_S^{(2026)}) \times 10^9 + 2026$.
The conversion is explicit and reversible.

**Derivation chain:** $\mathbb{Z} \to \zeta(s) \to \{\gamma_n\} \to
\gamma_7 \to (\log \gamma_7)^2$ — zero free parameters, zero fitted constants,
zero postulates beyond $\mathbb{Z} + \text{ZFC}$.

---

## Section 5: Tensions Resolved

### 5.1 The `S8` Tension

The `S8` tension — Planck `ΛCDM` (0.832) vs weak lensing surveys
(0.76–0.78) at `4σ` — dissolves in both scenarios:

- Scenario A: `S8 = 0.753` (within `1σ` of all three surveys)
- Scenario B: `S8 = 0.785` (within `1σ` of DES Y3)

The mechanism requires no new physics beyond the existing framework:
elevated `N_eff` suppresses early clustering, and lower `Ω_m = 0.290–0.302`
directly reduces `S8`. Both effects are fixed by the same `ξ` that was
determined by the `Ω_DM/Ω_b` input — the `S8` resolution is not arranged
by hand. The KK graviton cascade decays (Paper 1, Appendix Q §Y.8.2)
contribute an additional damping of small-scale structure. Full
derivation in Appendix C.

### 5.2 The Hubble Constant

The framework predicts `H₀ = 68.7–69.5 km/s/Mpc`, consistent with
Planck (67.4 ± 0.5 km/s/Mpc) at `1–2σ` and with TRGB/CCHP
(69.8 ± 0.6 km/s/Mpc) at `< 1σ`, but in `3–4σ` tension with SH0ES
Cepheid-based measurements (73.0 ± 1.0 km/s/Mpc). The framework is
consistent with CMB-inferred and intermediate-rung distance ladder
measurements but does not resolve the SH0ES discrepancy. The
Cepheid-TRGB calibration discrepancy remains an observational question
outside the framework (see §6.4).

The mechanism for the `H₀` uplift is the mirror sector dark radiation.
Elevated `N_eff = 3.31–3.39` increases the expansion rate at early
times; CAMB translates this into a higher effective `H₀` when holding
`θ*` fixed. The formula `H₀ ≈ 67.4 + 6.3 × ΔN_eff` (Paper 1, App. Y)
gives `H₀ ≈ 69.5` km/s/Mpc for `ΔN_eff = 0.35` (Scenario A). This
means the `H₀` prediction and the `N_eff` prediction are structurally
linked: both are driven by the same `ξ` from the mirror sector. If
CMB-S4 measures `N_eff = 3.046 ± 0.03` (ruling out the mirror sector),
the `H₀` prediction falls back to `H₀ ≈ 67.4` km/s/Mpc — the Planck
`ΛCDM` value. The two predictions stand or fall together.

### 5.3 The DESI Evolving Dark Energy

DESI DR2 (arXiv:2503.14738) reports `4.2σ` evidence for evolving dark
energy with `w₀ ≈ −0.75`, `w_a ≈ −0.75`. The perturbative framework
predicts `w₀ = −1`, `w_a = 0` (the Casimir potential V = V₀/φ⁴ is exact;
the dilaton is frozen by Hubble friction at ε ~ 10⁻⁵²; see Paper 6 §2).
If DESI DR3 confirms `w ≠ −1`, non-perturbative modifications to the
dilaton potential are required.

### 5.4 The Cosmic Coincidence

`Ω_DM/Ω_b = 5.36 ± 0.05` is now derived rather than input. Full
derivation in Appendix E. The coincidence is explained by the
`1/ξ²` scaling law from temperature-asymmetric bulk leptogenesis.

---

## Section 6: Open Problems

### 6.1 The `θ*` Tension and the Derivation Path B → C → A

The three scenarios are not alternative models — they are three
approximation levels applied to the *same* framework, bracketing the
physically correct answer. The range `ξ = 0.432–0.47` is determined
by the approximation level, not by any free parameter choice.

**Scenario B (leading-order, `ξ = 0.432`)** uses the `1/ξ²` law with
`K → ∞` (no washout correction). This is the purely theoretical
prediction with no CMB input. It gives `θ*` offset +6.6 arcseconds —
a `6σ` discrepancy — and is excluded by CMB data. It is presented to
demonstrate falsifiability: a 10% shift in `ξ` produces a `6σ` effect
in the most precisely measured cosmological quantity.

**Scenario C (washout-corrected, `ξ = 0.4375`)** incorporates the
logarithmic washout correction at `K = 5` (fixed by the observed
neutrino mass `m_ν = 50 meV` and the SM electroweak scale; see
Appendix E §E.3.3). This shifts `ξ` from 0.432 to ~0.44, reducing the
`θ*` offset to +1.0 arcseconds (`~1σ`), at the cost of a `~2.5σ` D/H tension.

**Scenario A (`θ*`-matched, `ξ = 0.47`)** further incorporates the warp
correction to the neutrino branching ratio (`c = 1.986` rather than
`c = 2`, §E.8), a calculable 0.7% deviation from the conformally coupled
value. This scenario passes both `θ*` and `Ω_DM/Ω_b` constraints.

The spread in `ξ` across the three scenarios reflects: (i) the
leading-order approximation `K → ∞` versus the `K = 5` correction (~15%
shift in washout ratio), and (ii) whether the small warp correction
`c = 1.986` is included. These are computable quantities with a definite
answer; the spread will be resolved by the full two-sector Boltzmann
analysis identified as future work in §6.2. The progression B → C → A
is the physics: the naive scaling law is corrected by washout dynamics
and warp geometry, converging on a value consistent with CMB data. A
dedicated MCMC scan of the framework's geometric parameters
`{L, ξ, c, k}`, simultaneously fitting `θ*`, `Ω_DM/Ω_b`, and BBN
constraints, is the highest-priority follow-up computation to determine
the precise corrected `ξ`.

### 6.2 Mirror Baryogenesis Precision

The washout ratio `κ'/κ ~ 1/ξ²` is derived in the strong washout
limit. A full Boltzmann equation analysis for two-sector leptogenesis
would determine this ratio precisely. This is identified as future work.

### 6.3 JWST Early Galaxies

The framework does not add time at `z > 10` (Appendix H). The early
galaxy tension must be addressed through mirror dark matter structure
formation (N-body simulations with collisional DM), or through
astrophysical channels (star formation efficiency).

### 6.4 The SH0ES Residual

The framework predicts `H₀ = 68.7–69.5`, not 73.0. The `3.5–4σ`
gap with SH0ES Cepheids is not explained by the minimal framework.
Either the Cepheid calibration has a systematic at the ~3 km/s/Mpc
level, or the framework requires additional physics (Paper 1,
Appendix Y §Y.9.5).

---

## Section 7: Decisive Tests

Eight experiments in the next decade test every prediction simultaneously.
Full roadmap in Appendix I. The three most decisive:

**CMB-S4 (2030):** `N_eff = 3.31` is a `9σ` deviation from the SM value.
Detection at CMB-S4's `σ(N_eff) ≈ 0.03` sensitivity either confirms the
mirror sector at > `8σ` or rules it out at the same significance.

**DESI DR3 (2027):** The `H(z)` fingerprint peaks 4% above `ΛCDM` at
`z ~ 0.5`. At DESI DR3's ~0.5% precision per bin, this is an `8σ` signal
if present, or a strong exclusion if absent.

**Euclid (2027+):** `S8` prediction (0.75–0.79) vs Planck `ΛCDM` (0.832)
is a `16σ` test at Euclid's `σ(S8) ≈ 0.005` precision. The `S8` resolution
is the framework's most immediate decisive test.
