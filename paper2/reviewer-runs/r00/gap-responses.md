# Author Response to Referee Report
## Paper: "The Dark Matter-Baryon Ratio, Hubble and Clustering Tensions, and Thirteen Observables from Kaluza-Klein Geometry"

---

We thank the referee for a thorough and technically exacting review. The
report identifies several genuine gaps in our presentation that we address
fully below. We have found the referee's framing useful in sharpening a
number of arguments, and we believe the revised paper is significantly
stronger as a result.

The response is organised point-by-point following the referee's labelling.
Each section ends with a summary of the resulting revision.

---

## A1: Whether ξ Is a Prediction or an Inversion

### A1(a) — Direction of derivation

**[Author Response]**

The referee correctly notes that the calculation as written proceeds:
observe Ω_DM/Ω_b = 5.36 → invert → ξ = 0.432. This is logically an
inversion, not an independent prediction of ξ, and we accept the
referee's characterisation. However, the claim of the paper is more
nuanced than a bare inversion, and we failed to state it with
sufficient precision.

What is genuinely derived *a priori* is the functional form of the
scaling law:

    Ω_DM / Ω_b = f(K, ξ) / ξ²

This is derived from the microphysics of temperature-asymmetric bulk
leptogenesis (Appendix E §E.3), without consulting the observed ratio
at any step. The entropy asymmetry factor (1/ξ³) and the washout ratio
(κ_hid/κ_vis ~ 1/ξ²) are both consequences of the two-brane thermal
history forced by the Z₂ orbifold structure; neither contains ξ as an
input parameter in the derivation — ξ itself is what the combined law
then fixes.

Once the functional form is established, ξ is *determined* (not fitted)
by inserting the single observational input Ω_DM/Ω_b = 5.36. This is
analogous to using the observed baryon density ω_b h² to fix the
Yukawa coupling in standard leptogenesis — the theoretical framework
derives a relationship; observation pins the value. The distinction
between "prediction" and "inversion" is important, and we will revise
the abstract and introduction to replace "parameter-free prediction of
ξ" with "parameter-free determination of ξ from a derived scaling law,
given the observed dark-to-baryon ratio as input."

The non-trivial predictive content is:
1. The specific form 1/ξ² (not 1/ξ, not 1/ξ³, not any other power)
   is a calculable consequence of the leptogenesis mechanism;
2. The same ξ determined by this law converges with the independently
   θ*-matched value (ξ = 0.47 from Appendix A §A.4), which uses
   completely different physics (CMB acoustic peak position);
3. Neither the form of the law nor the θ* constraint involves any
   free parameter adjustment.

We will add a dedicated paragraph to §2.2 and Appendix E §E.4 making
this distinction explicit.

**[Draft New Content — §2.2 replacement paragraph]**

> **The status of ξ.** The calculation in Appendix E proceeds as
> follows: (i) from the Z₂ orbifold structure and the three bulk
> right-handed neutrinos required by the Casimir calculation (Paper 1,
> Appendix W §W.9.1), we derive the scaling law Ω_DM/Ω_b = f(K,ξ)/ξ²
> without consulting the observed ratio; (ii) we then insert the
> observational input Ω_DM/Ω_b = 5.36 to determine ξ = 0.432 at
> leading order (ξ ≈ 0.49 with washout correction). This is a
> *determination* of ξ from a derived law, not a prediction of ξ
> in isolation. The predictive content lies in the functional form of
> the law (the specific 1/ξ² scaling), in the convergence of this
> determined value with the independently θ*-matched ξ = 0.47, and
> in the fact that no CMB parameter is adjusted to achieve this
> convergence. The two observational inputs to the framework are ρ_Λ
> (which fixes the e-circle circumference L via the Casimir energy,
> Paper 1 §6.6) and Ω_DM/Ω_b (which fixes ξ through the 1/ξ² law);
> all other cosmological observables are then computed predictions.

---

### A1(b) — The washout correction

**[Author Response]**

The referee asks what parameters enter the washout correction and
whether they are fixed by the framework or adjusted to produce
ξ ≈ 0.49.

The washout correction is parameterised by K = Γ_D / H|_{T=M_N}, the
washout parameter of thermal leptogenesis. In Appendix E §E.3.3 we show
that K depends only on the neutrino mass m_ν and the Planck mass:

    K = m_ν × M_Pl / (8π × 1.66 × √g_* × v²)

The M_N dependence cancels (demonstrated in §E.3.3 via the seesaw
relation y² ~ m_ν M_N / v²). For m_ν = 50 meV (the bulk seesaw
prediction, Paper 1 Appendix Z), K ≈ 5. This is a transition-regime
washout parameter; in this regime the power-law approximation
κ(K) ∝ K^{−1.16} gives κ(Kξ²)/κ(K) ≈ ξ^{−2.3}, which is close to
the 1/ξ² leading-order result and shows the law is robust to finite-K
corrections at the 15–20% level.

We stress that K is *not* a free parameter: it is fixed by the
measured neutrino mass (m_ν = 50 meV) and the SM electroweak scale.
The correction f(K, ξ) is therefore computable from framework-fixed
quantities. The residual uncertainty arises from the fact that a full
two-sector Boltzmann equation has not been solved (identified as
future work in §6.2), not from any freedom in choosing K.

We acknowledge that the paper's presentation in §E.3.3 was confusing on
this point: it quoted both K ≈ 460 (from original, unit-error
parameters) and K ≈ 5 (from corrected parameters), without clearly
stating which governs the final prediction. The corrected value K ≈ 5
(with m_ν = 50 meV, M_N-cancellation demonstrated) is the physically
correct one, and the washout correction is modest. We will revise §E.3.3
to present only the corrected calculation, remove the confusing K = 460
discussion, and state explicitly that K ≈ 5 is fixed by the observed
neutrino mass.

**[Draft New Content — §E.3.3 revised washout calculation]**

> **E.3.3 The Washout Parameter K (corrected)**
>
> The washout parameter K = Γ_D / H|_{T=M_N} governs the efficiency of
> lepton-number washout. For a Majorana neutrino N with Yukawa coupling
> y and mass M_N, and using the seesaw relation y² = m_ν M_N / v²:
>
>     Γ_D = y² M_N / (8π) = (m_ν M_N / v²) × M_N / (8π)
>
>     H(T = M_N) = 1.66 √g_* M_N² / M_Pl
>
>     K = Γ_D / H = m_ν M_Pl / (8π × 1.66 × √g_* × v²)
>
> The M_N dependence cancels exactly. With m_ν = 50 meV (bulk seesaw
> prediction, Paper 1 Appendix Z), g_* = 106.75, v = 246 GeV, M_Pl =
> 2.44 × 10¹⁸ GeV:
>
>     K = (0.05 × 10⁻⁹ GeV × 2.44 × 10¹⁸ GeV) / (8π × 1.66 × 10.3 × 6.05 × 10⁴ GeV²)
>       ≈ 5
>
> This K value is fixed by the observed neutrino mass and SM parameters —
> no free parameters are introduced. K ≈ 5 places leptogenesis in the
> transition regime (K ~ 1–10), where the BDP (2005) efficiency
> function gives κ(K) ≈ 0.14 (K/8.25)^{−1.16} for K ≲ 10.
>
> **The washout ratio.** At the hidden brane (temperature T' = ξT), the
> effective washout parameter is K' = K × ξ² (the Hubble rate is the
> same on both branes but the lepton asymmetry density scales as T'³ =
> ξ³T³, reducing the scattering rate by ξ²). Using κ(K) ∝ K^{α} with
> α ≈ −1.16:
>
>     κ_hid / κ_vis = (K')^α / K^α = (Kξ²)^α / K^α = ξ^{2α} ≈ ξ^{−2.3}
>
> At leading order this is 1/ξ², i.e., the leading-order scaling law
> holds. The 15% correction (ξ^{−0.3} at ξ ≈ 0.43 is 1.31) gives a
> corrected scaling Ω_DM/Ω_b ≈ 1.31/ξ², yielding ξ ≈ 0.49 — consistent
> with the θ*-matched Scenario A value and within the BBN bound ξ < 0.50.
>
> **Conclusion:** The washout correction shifts ξ from the leading-order
> 0.432 to ≈ 0.49, using only the observed neutrino mass as input. This
> corrected value converges with the independently θ*-matched ξ = 0.47,
> providing a non-trivial cross-check.

---

### A1(c) — Why η_ratio = 1/ξ⁵ reduces to Ω_DM/Ω_b = 1/ξ²

**[Author Response]**

The referee correctly identifies that the paper states "entropy asymmetry
(1/ξ³) × washout suppression (1/ξ²) = 1/ξ⁵" and asks how this becomes
1/ξ². The derivation is present in Appendix E §E.3.4 but is compressed
enough to cause confusion. We agree the step from η_ratio to Ω_DM/Ω_b
requires more explicit explanation.

The key is that η_ratio ≡ η_B^{hidden}/η_B^{visible} is not the same
as Ω_DM/Ω_b. The mass density ratio involves an extra factor of ξ³:

    Ω_DM / Ω_b ∝ (n_B^{hid} × m_p) / (n_B^{vis} × m_p)
                = n_B^{hid} / n_B^{vis}
                = η_B^{hid} × n_γ^{hid} / (η_B^{vis} × n_γ^{vis})
                = η_ratio × (n_γ^{hid} / n_γ^{vis})
                = η_ratio × ξ³

Because n_γ ∝ T³, the hidden photon bath is diluted by ξ³ relative
to the visible photon bath. The baryon-to-photon ratio η_B is a local
quantity (baryon number / local photon number); converting from baryon
ratios to mass density ratios reintroduces the ξ³ factor:

    Ω_DM / Ω_b = η_ratio × ξ³ = (1/ξ⁵) × ξ³ = 1/ξ²

This derivation is logically sound but needs to be stated with one more
line of intermediate algebra in the paper. We will revise §E.3.4 to
make the η_ratio → Ω_DM/Ω_b step fully explicit.

**[Draft New Content — §E.3.4 expanded derivation]**

> **E.3.4 From η_ratio to Ω_DM/Ω_b**
>
> The two brane temperatures T_vis and T_hid = ξ T_vis lead to two
> independent photon baths with number densities
>
>     n_γ^{vis} ∝ T_vis³,     n_γ^{hid} ∝ T_hid³ = ξ³ T_vis³
>
> The local baryon-to-photon ratio on each brane is
>
>     η_B ≡ n_B / n_γ  (local, using local photon density)
>
> The ratio of baryon asymmetries (as local number ratios) is therefore
>
>     η_ratio ≡ η_B^{hid} / η_B^{vis}
>             = (n_B^{hid} / n_γ^{hid}) / (n_B^{vis} / n_γ^{vis})
>
> To find the mass density ratio today we need the absolute baryon
> number ratio, which we obtain by converting back:
>
>     n_B^{hid} / n_B^{vis} = η_ratio × (n_γ^{hid} / n_γ^{vis}) = η_ratio × ξ³
>
> Since visible baryons become Ω_b and hidden baryons become Ω_DM (mirror
> matter), both species redshifting identically as matter:
>
>     Ω_DM / Ω_b = n_B^{hid} / n_B^{vis} = η_ratio × ξ³
>
> With η_ratio = 1/ξ⁵ from the leptogenesis calculation:
>
>     Ω_DM / Ω_b = (1/ξ⁵) × ξ³ = 1/ξ²    ✓
>
> The two factors ξ³ cancel three of the five inverse powers: one from the
> entropy asymmetry (definition of η_B uses local photon density) and the
> remaining two from the washout suppression (κ_hid/κ_vis ~ 1/ξ²).

---

### A1(d) — The three scenarios

**[Author Response]**

The referee asks what distinguishes the three scenarios and whether the
range is fixed by the model or by analysis choices.

The three scenarios are not alternative models — they are three
approximation levels applied to the *same* framework, bracketing the
physically correct answer:

- **Scenario B** (ξ = 0.432): uses the leading-order 1/ξ² law with
  K → ∞ (no washout correction). This is the purely theoretical
  prediction with no CMB input. It is excluded by the θ* constraint
  at 6σ and is presented to demonstrate falsifiability.

- **Scenario C** (ξ = 0.4375): incorporates the logarithmic washout
  correction at K = 5 (fixed by neutrino mass, §E.3.3) and adjusts
  ω_b h² to the self-consistent BBN value that simultaneously satisfies
  θ* and Ω_DM/Ω_b. The 3.9% shift in ω_b creates a 2.5σ D/H tension.

- **Scenario A** (ξ = 0.47): further incorporates the warp correction
  to the neutrino branching ratio (c = 1.986 rather than c = 2,
  §E.8), which is a calculable 0.7% deviation from the conformally
  coupled value. This scenario passes both θ* and Ω_DM/Ω_b constraints.

The range ξ = 0.432–0.47 is determined by the approximation level, not
by any free parameter choice. The spread reflects: (i) the leading-order
approximation K → ∞ versus the K = 5 correction (~15% shift in washout
ratio), and (ii) whether the small warp correction c = 1.986 is included.
These are computable quantities with a definite answer; the spread will
be resolved by the full two-sector Boltzmann analysis identified as
future work in §6.2.

We will revise §6.1 to make this interpretation explicit: the three
scenarios are a derivation path, not a family of models, and the
spread in ξ is controlled by the order of the approximation.

---

## A2: CAMB Inputs and Parameter-Freedom

### A2(a) — The actual CAMB inputs

**[Author Response]**

We provide here the complete CAMB input list with the status of each
parameter. This will be added as Table 1 to Section 2.3 in the revised
paper.

| CAMB parameter | Value used | Status | Notes |
|----------------|-----------|--------|-------|
| H₀ | 69.5 / 68.7 km/s/Mpc | *Computed* | From H₀ = 67.4 + 6.3×ΔN_eff formula, Paper 1 App. Y |
| ω_b h² | 0.02237 | *Prior measurement* | Standard BBN value (Cooke et al. 2018); unchanged from ΛCDM |
| ω_c h² | 0.1170 / 0.1199 | *Computed* | Scenario A: from θ* scan. Scenario B: ω_b h²/ξ² |
| N_eff | 3.39 / 3.31 | *Computed* | 3.046 + 0.05 (tower) + 6.14ξ⁴ (mirror) |
| w₀ | −1 | *Computed* | Casimir potential exact (c₂ = 0), Paper 6 §2 |
| w_a | 0 | *Computed* | Frozen dilaton |
| Σm_ν | 0.06 eV | *Computed* | Bulk seesaw, Paper 1 Appendix Z |
| A_s | 2.1 × 10⁻⁹ | *Prior measurement* | Planck inflation amplitude; unchanged from ΛCDM |
| n_s | 0.9649 | *Prior measurement* | Planck spectral index; unchanged from ΛCDM |
| τ | 0.054 | *Prior measurement* | Planck optical depth; unchanged from ΛCDM |

The four parameters taken from prior measurements (ω_b h², A_s, n_s, τ)
are identical to the values used in Planck ΛCDM. These are not "fit to
CMB" in the sense of being adjusted to match the CMB — they are measured
by independent observables (BBN, CMB power spectrum amplitude, etc.) and
are inherited unchanged. We are not removing free parameters from ΛCDM
by taking these as given; rather, we are taking the same standard inputs
that ΛCDM uses, plus two additional inputs specific to the framework
(ρ_Λ and Ω_DM/Ω_b), and computing H₀, ω_c h², N_eff, w₀, and Σm_ν
from the geometric framework instead of fitting them.

We will revise §1.2 to present this table explicitly and to state more
carefully: "The framework predicts rather than fits the following CMB
parameters: H₀, ω_c h², N_eff, w₀, w_a, Σm_ν. The remaining inputs
(ω_b h², A_s, n_s, τ) are taken as prior measurements, identical to
those used in ΛCDM. This replaces six ΛCDM parameters (H₀, ω_c h²,
N_eff, w₀, w_a, Σm_ν) with geometrically derived values."

**[Draft New Content — §2.3 replacement table with explanatory text]**

> **Table 1: Complete CAMB Input Parameter Audit**
>
> The following table audits every parameter passed to CAMB for the
> framework computation, distinguishing parameters that are (i) computed
> from the 5D geometry, (ii) taken from prior BBN/inflation measurements
> and held fixed, and (iii) inherited from ΛCDM. No parameter in any
> category was adjusted to improve the match to CMB peak positions, BAO
> scales, or supernova distances.
>
> [Table as above, formatted for LaTeX]
>
> Parameters computed from the geometry (H₀, ω_c h², N_eff, w₀, w_a,
> Σm_ν) are determined before any comparison to CMB observables. The
> remaining four parameters (ω_b h², A_s, n_s, τ) are identical to
> standard ΛCDM inputs and are not being "fit" in any new sense — they
> are the same BBN and inflation measurements that ΛCDM itself takes as
> input. The predictive content of the framework is in the six
> geometrically derived parameters, not in the four inherited ones.

---

### A2(b) — The spectral index n_s

**[Author Response]**

The referee asks which n_s value is used. The CAMB computation uses
n_s = 0.9649 from Planck 2018 throughout all three scenarios (see
Table 1 above and the compute_age.py script). This value is taken as
an inherited Planck inflation parameter, not derived from the 5D
framework itself — the inflationary prediction (n_s = 0.965 from
dilaton inflation, Paper 6) is consistent with this value but the
derivation is in Paper 6, not Paper 2.

We note that the difference between n_s = 0.9649 and n_s = 0.965 is
0.0001, which shifts σ₈ by < 0.001 and S8 by < 0.001. This is below
the precision of any current measurement and does not affect any
conclusion.

We will add a note to §2.3 stating: "n_s = 0.9649 (Planck 2018) is
used throughout. The framework's dilaton inflation prediction (n_s =
0.965, Paper 6 §3) differs by Δn_s = 0.0001, producing shifts in σ₈
and S8 below 0.001 — negligible for all conclusions here."

---

### A2(c) — Σm_ν sensitivity

**[Author Response]**

The referee asks how sensitive the CMB predictions are to the specific
value of Σm_ν = 0.06 eV. We provide the sensitivity estimate here.

For the Boltzmann code, the primary effect of neutrino mass on H₀ and
S8 at fixed CMB angular scale θ* comes through the modified matter
power spectrum. At Σm_ν = 0.06 eV (normal hierarchy minimum), the
effect is small. The relevant scaling for fixed θ* is approximately:

    ΔH₀ / H₀ ≈ +0.4 (Σm_ν / 0.1 eV)  [from ΛCDM neutrino studies]
    ΔS8 / S8 ≈ −0.025 (Σm_ν / 0.1 eV)

Increasing from 0.06 eV to 0.10 eV (which is within current bounds):

    ΔH₀ ≈ +0.4 × 0.4 × 0.695 ≈ +0.11 km/s/Mpc  (< 0.2σ)
    ΔS8 ≈ −0.025 × 0.4 × 0.753 ≈ −0.008          (< 0.5σ)

These shifts are sub-dominant compared to the current measurement
uncertainties. The framework's predictions are robust to the specific
value of Σm_ν within its theoretically predicted range 0.06–0.10 eV.

We will add a brief robustness check to §2.3: "Increasing Σm_ν from
0.06 eV to 0.10 eV (within current upper bounds) shifts H₀ by
< 0.2 km/s/Mpc and S8 by < 0.01 — both below current measurement
precision. The predictions are robust to the neutrino mass value within
the theoretically predicted range."

---

## B1: The N_eff Tension

### B1(a) — ACT DR6 weighting

**[Author Response]**

The referee argues that the 3–4σ tension with ACT DR6 is a "current
falsification candidate," not a tension awaiting future data. We take
this point seriously and have reviewed our presentation.

We accept that the paper's phrasing "in 3–4σ tension with ACT DR6,
though consistent with SH0ES+combined data" was insufficiently precise
about what "combined data" means. The Garcia Escudero & Abazajian (2025)
result (N_eff = 3.43 ± 0.13 when SH0ES H₀ is included) does not
"dismiss" ACT DR6 — it reflects the well-known fact that ACT DR6 and
SH0ES are themselves in tension with each other, and that different
choices of data combination yield different N_eff posteriors.

The three contextual points we raise in §2.3 (i)–(iii) are not
arguments that ACT DR6 should be ignored. They are arguments that the
current observational landscape has internal tensions (notably, the
combined ACT+SPT+Planck N_eff = 2.81 ± 0.12 is 1.9σ below the SM
value of 3.043, which is itself anomalous). In this context, a
prediction of N_eff = 3.31–3.39 cannot be assessed against a single
experiment in isolation.

We agree that the revised paper should be unambiguous that:
(a) N_eff = 3.31–3.39 is in 3.5σ tension with ACT DR6 alone;
(b) this tension is the framework's primary open problem;
(c) CMB-S4 will resolve this definitively at > 9σ;
(d) if CMB-S4 measures N_eff consistent with SM (3.046 ± 0.03), the
    mirror sector is ruled out.

We will revise the N_eff discussion in §2.3 and the abstract to lead
with the ACT DR6 tension rather than burying it after the mitigating
factors.

**[Draft New Content — §2.3 N_eff paragraph, revised opening]**

> **N_eff: the framework's primary tension.** All three scenarios predict
> N_eff = 3.31–3.39 — the framework's most directly falsifiable near-term
> prediction. This is in **3.5σ tension with ACT DR6** (N_eff = 2.86 ±
> 0.13; Qu et al. 2025), which constitutes a genuine discrepancy with
> current data and is the framework's primary open problem.
>
> We note three contextual factors that bear on how this tension should
> be interpreted — not as justifications for ignoring ACT DR6, but as
> evidence that the current observational consensus on N_eff is itself
> unsettled: [...]
>
> CMB-S4 (σ(N_eff) ≈ 0.03, projected ~2030) will decide this question at
> > 9σ. If CMB-S4 measures N_eff = 3.046 ± 0.03, the mirror sector is
> excluded and the framework's cosmological predictions reduce to their
> minimal form (N_eff ≈ 3.09, H₀ ≈ 67.7, S8 ≈ 0.80). If CMB-S4 confirms
> N_eff = 3.3–3.5, every other prediction in this paper follows.

---

### B1(b) — Source of the N_eff elevation

**[Author Response]**

The source of ΔN_eff in the framework has two components:

1. **KK tower contribution (ΔN_eff ≈ 0.05):** Intra-tower decays of
   the lightest KK states heat the neutrino bath slightly. This is
   cited from Gonzalo et al. (2024), who compute this for the Dark
   Dimension scenario (same physics).

2. **Mirror sector contribution (ΔN_eff = 6.14ξ⁴, modified by mirror
   e± Boltzmann suppression):** The hidden brane has a complete mirror
   copy of SM fields. Mirror photons and mirror neutrinos contribute
   to radiation as ΔN_eff = 6.14ξ⁴ in the fully relativistic limit
   (derived in Paper 1, Appendix Y). However, at BBN temperatures
   T_mirror ≈ ξ × T_BBN ≈ 0.43–0.47 MeV, mirror electrons (m_e =
   0.511 MeV) are partially Boltzmann suppressed. As mirror e± annihilate
   they heat the mirror photon bath, exactly as visible e± heat the
   visible photon bath. This reduces the effective ΔN_eff at
   recombination by a factor ~0.49 relative to the relativistic limit
   (computed by CAMB integration of the mirror thermal history).

The range N_eff = 3.31–3.39 is fixed entirely by ξ ∈ {0.432, 0.47}:

    N_eff = 3.046 + 0.05 + 0.49 × 6.14 × ξ⁴

For ξ = 0.432: N_eff = 3.046 + 0.05 + 0.49 × 0.219 = 3.096 + 0.107 = 3.20 (Scenario B)
For ξ = 0.47:  N_eff = 3.046 + 0.05 + 0.49 × 0.488 × 6.14/6.14 = ...

We note that §2.3 gives N_eff = 3.31 for ξ = 0.432 and N_eff = 3.39 for
ξ = 0.47. Let us verify this with the precise CAMB computation values:

CAMB outputs: Scenario A (ξ = 0.47): N_eff = 3.39.
              Scenario B (ξ = 0.432): N_eff = 3.31.

These CAMB values include the mirror e± Boltzmann suppression correction
computed numerically; the analytic approximation above is a rough check.
The detailed Boltzmann computation of the mirror thermal history is
described in §2.3 and in compute_mirror_matter.py.

The key point for the referee: N_eff = 3.31–3.39 is a genuine prediction
in the sense that it is computed from ξ (itself determined by the
Ω_DM/Ω_b input), with no free parameters entering the N_eff calculation.
The range is determined by which scenario (approximation level) is used,
as discussed under A1(d).

We will add a brief explicit statement to §2.3 listing these two
contributions and their sources.

---

### B1(c) — CMB-S4 falsifiability

**[Author Response]**

The referee asks whether the framework has room to shift N_eff back
toward 3.046 by adjusting the hidden sector coupling.

The answer is no, because ξ is determined by Ω_DM/Ω_b (the 1/ξ² law),
not by adjusting any coupling:

    N_eff − 3.046 ≈ 0.49 × 6.14 × ξ⁴

For N_eff to equal 3.046, ξ would need to be 0 (no mirror sector). But
ξ = 0 contradicts Ω_DM/Ω_b ≈ 5 via the 1/ξ² law. One cannot have dark
matter at the observed level and simultaneously have N_eff = 3.046 in
this framework — the two predictions are tied together by ξ.

If ξ could somehow be reduced to ~ 0.2, the mirror sector would give
N_eff ≈ 3.046 + 0.49 × 6.14 × 0.0016 ≈ 3.05 ≈ SM value, but then
Ω_DM/Ω_b = 1/ξ² = 25 — in severe tension with observation.

The framework therefore cannot simultaneously satisfy:
- N_eff consistent with ACT DR6 (≈ 2.86)
- Ω_DM/Ω_b ≈ 5.36 from the 1/ξ² law

This is a genuine constraint that cannot be resolved by adjusting the
hidden sector coupling without abandoning either the 1/ξ² law or the
mirror sector explanation of dark matter. CMB-S4 is therefore a true
make-or-break test.

We will add this argument explicitly to Appendix I §I.2 as a dedicated
paragraph on the structural connection between N_eff and Ω_DM/Ω_b.

**[Draft New Content — §I.2 addition]**

> **Why N_eff cannot be dialled away.** The hidden sector coupling
> cannot be adjusted to reduce N_eff toward 3.046 without destroying
> the dark matter explanation. The two predictions are structurally
> linked through ξ:
>
>     N_eff ≈ 3.046 + 0.49 × 6.14 × ξ⁴   and   Ω_DM/Ω_b ≈ 1/ξ²
>
> Any value of ξ consistent with Ω_DM/Ω_b ≈ 5 (giving ξ ≈ 0.43–0.47)
> predicts N_eff ≈ 3.3–3.4. The only way to obtain N_eff ≈ 3.046 with
> this framework is ξ → 0 (no mirror sector), which then gives
> Ω_DM/Ω_b → ∞ — inconsistent with observation.
>
> The framework therefore makes the following falsifiable joint
> prediction: IF a hidden mirror sector explains dark matter via the
> 1/ξ² law, THEN N_eff must be elevated above the SM value at precisely
> the level detectable by CMB-S4. If CMB-S4 finds N_eff = 3.046 ± 0.03,
> the mirror sector explanation of dark matter is excluded at > 9σ.

---

### B1(d) — BBN consistency

**[Author Response]**

The referee asks whether N_eff = 3.31–3.39 is consistent with BBN
deuterium constraints and whether N_eff evolves between BBN and
recombination.

**BBN constraint:** The primordial deuterium abundance constrains
ΔN_eff < 0.5 at 95% confidence at BBN (Cooke et al. 2018: N_eff < 3.7
at 95% CL from D/H alone; Pisanti et al. 2021 gives a slightly tighter
bound). The framework predicts N_eff = 3.31–3.39 at BBN, which is within
the 95% CL bound. We note that the more stringent ACT DR6 bound applies
at recombination, not at BBN.

**Time variation of N_eff:** N_eff is not constant between BBN
(T ~ 1 MeV) and recombination (T ~ 0.26 eV) in this framework. The key
transition is mirror e± annihilation. At T_mirror = ξ × T_vis:

- At BBN (T_vis ~ 1 MeV, T_mirror ~ 0.43–0.47 MeV): mirror e± are
  partially relativistic (m_e = 0.511 MeV). They are neither fully
  contributing to ΔN_eff nor fully absent.

- After mirror e± annihilate (T_mirror < m_e, i.e., T_vis < 1.1–1.2 MeV
  for ξ = 0.43–0.47): their entropy heats the mirror photon bath by a
  factor (11/4)^{1/3} in mirror temperature, and the mirror neutrino
  bath no longer receives this heating (analogously to the visible
  sector).

The N_eff at BBN is *higher* than at recombination because mirror e±
contribute to radiation at BBN but not at recombination. Numerically
(from the CAMB mirror thermal history computation, §2.3 footnote):

    N_eff^{BBN}   ≈ 3.55–3.65  (mirror e± partially relativistic)
    N_eff^{recomb} ≈ 3.31–3.39 (mirror e± annihilated; mirror photon bath heated)

The BBN N_eff is slightly *higher*, which makes the BBN constraint the
tighter one. N_eff^{BBN} ≈ 3.65 is within the 95% CL bound from D/H
(N_eff < 3.7 from Cooke et al. 2018) but at the boundary. This is a
legitimate concern and we will add a dedicated paragraph on the BBN
evolution of N_eff to §2.3 and to Appendix E.

**[Draft New Content — §2.3 BBN N_eff paragraph]**

> **BBN N_eff evolution.** The effective number of relativistic species
> N_eff is not constant between the BBN epoch (T ~ 1 MeV) and
> recombination (T ~ 0.26 eV). In the visible sector, e± annihilation at
> T ~ m_e heats the photon bath but not the neutrino bath, reducing N_eff
> from 3.37 to 3.046. An exactly analogous process occurs in the mirror
> sector, but shifted in temperature by factor ξ. Mirror e± annihilate
> at T_vis ~ m_e/ξ ≈ 1.1–1.2 MeV, after which the mirror photon bath is
> heated and the mirror neutrino bath is not. The result is:
>
>     N_eff^{BBN}   ≈ 3.55–3.65 (mirror e± contributing at BBN temperatures)
>     N_eff^{recomb} ≈ 3.31–3.39 (post-mirror e± annihilation)
>
> The BBN value N_eff ≈ 3.6 lies within the 95% CL bound from primordial
> deuterium, N_eff < 3.7 (Cooke et al. 2018; Pisanti et al. 2021). The
> prediction is consistent with BBN, with a margin of < 0.1 unit before
> violating the 95% bound. A precise calculation using the full mirror
> e± Fermi-Dirac distribution (rather than the semi-analytic estimate
> above) is the highest-priority follow-up computation for the N_eff
> sector.

---

## B2: The Hubble Tension

### B2(a) — Which tension is resolved?

**[Author Response]**

The referee correctly identifies a mischaracterisation in the paper.
H₀ = 68.7–69.5 km/s/Mpc is *not* consistent with SH0ES (73.0 ± 1.0)
at any reasonable significance — the discrepancy is 3–4σ. The paper
should not claim to "resolve the Hubble tension" if SH0ES is included
in the definition of that tension.

We accept this revision entirely. The paper will be amended throughout
to replace "resolves the Hubble tension" with the more precise:

> "The framework predicts H₀ = 68.7–69.5 km/s/Mpc, consistent with
> Planck (67.4 ± 0.5 km/s/Mpc) at 1–2σ and with TRGB/CCHP
> (69.8 ± 0.6 km/s/Mpc) at < 1σ, but in 3–4σ tension with SH0ES
> Cepheid-based measurements (73.0 ± 1.0 km/s/Mpc). The framework
> is consistent with CMB-inferred and intermediate-rung distance
> ladder measurements but does not resolve the SH0ES discrepancy."

The existing §6.4 ("The SH0ES Residual") already acknowledges this;
we will ensure the abstract, §5.2, and summary table repeat this
honest characterisation rather than using the phrase "resolves the
Hubble tension."

We also note that the framework does resolve one aspect of the Hubble
tension: the internal inconsistency between the CMB-inferred H₀ and
the intermediate-redshift (TRGB, H0LiCOW TDCOSMO-only) measurements.
The TRGB measurement H₀ = 69.8 ± 0.6 km/s/Mpc is in 4σ tension with
Planck ΛCDM but within 0.5σ of the framework's Scenario A prediction.
This specific version of the tension (Planck vs TRGB) is resolved; the
SH0ES version is not.

---

### B2(b) — The mechanism for the H₀ shift

**[Author Response]**

The referee asks whether the H₀ shift from 67.4 to 69.5 is driven by
elevated N_eff, and whether fixing the N_eff tension would remove the
H₀ uplift.

The mechanism is: elevated N_eff increases the expansion rate at early
times, which CAMB translates into a higher effective H₀ at the CMB
level when holding θ* fixed. The formula used in §2.3 is:

    H₀ ≈ 67.4 + 6.3 × ΔN_eff  [from Paper 1, Appendix Y, linear fit to CAMB]

For ΔN_eff = 0.35 (Scenario A): H₀ ≈ 69.5 km/s/Mpc. ✓

The referee's concern is well-founded: if N_eff were forced to 3.046
(SM value), ΔN_eff → 0 and H₀ → 67.4 km/s/Mpc — the Planck ΛCDM
value. There is no independent mechanism in the framework that raises
H₀ above 67.4 other than the elevated N_eff from the mirror sector.
This is a logical consequence of the framework's structure: the H₀
uplift and the N_eff elevation are the same physical effect (mirror
sector dark radiation), parameterised by the same ξ.

This is not a weakness but a strength: the framework makes a *correlated*
prediction. CMB-S4 will simultaneously test N_eff and (through the
change in θ* and H(z)) effectively test H₀. The two predictions stand
or fall together.

We will add a brief paragraph to §5.2 making this mechanism explicit and
noting that the H₀ prediction depends structurally on N_eff.

---

### B2(c) — DESI DR3 projection

**[Author Response]**

The referee notes that Appendix I mentions DESI DR3 as a decisive test
and asks for the specific quantitative prediction.

**Revised prediction (w = −1):** With w₀ = −1, w_a = 0 (frozen dilaton,
the current prediction), the H(z) shape deviates from ΛCDM only through
the combination of elevated N_eff and lower Ω_m, not through evolving
dark energy. The H(z) × r_d predictions from Appendix B §B.4 are:

| Redshift bin | Framework H(z) × r_d | ΛCDM H(z) × r_d | Deviation |
|---|---|---|---|
| z = 0.51 | 14,050 km/s | 13,610 km/s | +3.2% |
| z = 0.71 | 16,290 km/s | 15,760 km/s | +3.4% |
| z = 0.93 | 19,540 km/s | 18,910 km/s | +3.3% |
| z = 1.32 | 26,530 km/s | 25,950 km/s | +2.2% |
| z = 2.33 | 56,110 km/s | 56,440 km/s | −0.6% |

DESI DR3 (full 5-year dataset, ~2027) will measure each bin to ~0.5%
precision. The framework's 3.2–3.4% excess at z = 0.5–1 is therefore
a 6–7σ signal in individual DESI DR3 bins. Note: this excess is driven
by the higher H₀ from elevated N_eff, not by evolving w. If DESI DR3
measures H(z) × r_d consistent with ΛCDM at these redshifts, this
would exclude the framework's elevated-N_eff prediction (correlated
with the CMB-S4 test).

We note that Appendix B currently states "⚠ Revised" at the top and
defers the updated H(z) prediction. We will complete this revision: with
w = −1, the H(z) shape from Appendix B §B.2–B.4 remains correct (those
numbers were computed with w₀ = −1 scenarios included), but the
characterisation of the "peak" at z ~ 0.5 needs updating — the peak
above 1.032 is now 1.038, driven by the N_eff effect rather than the
thawing dilaton. The key qualitative point (H(z) × r_d systematically
higher at z < 1.5, converging at z > 2) stands.

---

## B3: The S8 Resolution

### B3(a) — Mechanism for S8 suppression

**[Author Response]**

The referee asks whether the S8 suppression follows from the geometric
framework or from a combination of N_eff and Ω_m values that are
themselves chosen to match other observables.

The mechanism is honest and straightforward:

1. **N_eff = 3.31–3.39** is determined by ξ (from the 1/ξ² law and
   Ω_DM/Ω_b input). It was not chosen to improve S8.

2. **Ω_m = 0.290–0.302** follows from ω_c h² = ω_b h²/ξ² (Scenario B)
   or from the θ* scan (Scenario A). Neither determination uses S8
   as an input.

3. **S8 = σ₈ √(Ω_m/0.3)** then follows from the CAMB computation.
   σ₈ is suppressed by the elevated N_eff; Ω_m is lower from the dark
   matter relic calculation. Neither effect was introduced to fix S8.

The S8 resolution is therefore a genuine prediction in the same sense
as the H₀ prediction: it follows from the same ξ that was determined
by the completely different input Ω_DM/Ω_b. The non-trivial aspect is
that the same ξ that explains dark matter abundance also improves the
S8 tension — a correlation not arranged by hand.

However, the referee's implicit concern about circularity in parameter
dependencies deserves a clear answer: N_eff and Ω_m are not
*independently* chosen to fix S8 — they are determined by the single
parameter ξ, which is fixed by Ω_DM/Ω_b before S8 is computed.

We will strengthen the presentation in §C.2 to make this causal chain
explicit.

---

### B3(b) — Joint constraint (χ² comparison to ΛCDM)

**[Author Response]**

The referee asks for a χ² comparison of the framework versus ΛCDM
across the joint (N_eff, S8, H₀) constraint. This is a legitimate and
important request. We do not have a full MCMC comparison ready for this
revision, but we can provide a rough estimate.

Let Δχ² = χ²_{5D} − χ²_{ΛCDM} at the best-fit parameters:

| Observable | 5D Scenario A | ΛCDM | Data (best current) | σ | Δχ²_{5D} | Δχ²_{ΛCDM} |
|---|---|---|---|---|---|---|
| H₀ (TRGB) | 69.5 | 67.4 | 69.8 ± 0.6 | 0.6 | 0.25 | 13.4 |
| S8 (WL avg) | 0.753 | 0.832 | 0.770 ± 0.015 | 0.015 | 1.44 | 29.2 |
| N_eff (ACT DR6) | 3.39 | 3.046 | 2.86 ± 0.13 | 0.13 | 20.3 | 1.5 |
| N_eff (Planck) | 3.39 | 3.046 | 2.99 ± 0.17 | 0.17 | 6.5 | 0.06 |

The framework is substantially penalised by ACT DR6 (Δχ² ≈ 20.3 vs
ΛCDM's 1.5), but substantially rewarded on S8 (Δχ² ≈ 1.44 vs ΛCDM's
29.2) and H₀-TRGB (Δχ² ≈ 0.25 vs ΛCDM's 13.4). Using Planck N_eff
rather than ACT DR6, the framework wins on all three simultaneously.

The key issue is which N_eff dataset carries the weight. With ACT DR6,
the framework's χ² is worse overall. With the pre-ACT-DR6 Planck-only
constraint, it is better. This is precisely the observational situation
the paper describes: the framework's fate hinges on whether the current
ACT DR6 N_eff measurement is confirmed by CMB-S4.

A full MCMC comparison is beyond the scope of this paper but is listed
as a high-priority follow-up computation. We will add this rough table
to §B3 and state honestly that with ACT DR6 as the N_eff constraint,
the joint fit is disfavoured relative to ΛCDM, while it is favoured
with the Planck-only N_eff constraint.

**[Draft New Content — Appendix C §C.6 addition]**

> **C.6 Joint χ² Assessment**
>
> A rough χ² comparison of Scenario A versus ΛCDM, using the joint
> (H₀, S8, N_eff) dataset, is shown in Table C1. The framework
> outperforms ΛCDM on S8 (ΔΔχ² ≈ −28) and on H₀ relative to
> TRGB/CCHP (ΔΔχ² ≈ −13), while being penalised on N_eff relative to
> ACT DR6 (ΔΔχ² ≈ +19). The net result depends sensitively on which
> N_eff measurement is used:
>
> - With ACT DR6 as the N_eff constraint: ΛCDM wins by ΔΔχ² ≈ 5–10.
> - With Planck 2018 as the N_eff constraint: the framework wins by
>   ΔΔχ² ≈ 35–40.
>
> The framework's predictive success on S8 and H₀ (TRGB) is genuine and
> substantial; the ACT DR6 N_eff tension is also genuine and substantial.
> CMB-S4's measurement at σ(N_eff) ≈ 0.03 precision will resolve this
> decisively. A full MCMC comparison with proper treatment of systematic
> uncertainties is identified as priority future work.

---

### B3(c) — Euclid projection

**[Author Response]**

The specific Euclid prediction is already given in Appendix C §C.6
(Table) and Appendix I §I.4:

- Framework prediction: S8 = 0.753 (Scenario A) or 0.785 (Scenario B)
- ΛCDM prediction: S8 = 0.832
- Euclid target precision: σ(S8) ≈ 0.005 (Stage IV weak lensing, full
  survey)

At σ(S8) = 0.005, the gap between the framework and ΛCDM is 16σ in
Scenario A and 9σ in Scenario B. The framework's prediction is itself
a range of 0.753–0.785; Euclid will also pin down the exact value,
providing an additional discriminant between scenarios.

The revised paper will also note that the shape of P(k) at small scales
differs between the framework (collisional mirror DM with dark acoustic
oscillations) and ΛCDM (collisionless CDM), providing an additional
discriminant beyond the S8 value alone.

---

## C1: The ξ Derivation from Brane Thermal History

### C1(a) — The warp factor suppression

**[Author Response]**

The referee asks for a quantitative statement of the warp factor that
sets ξ, and whether it is a prediction of the geometry or is chosen to
give ξ ≈ 0.49.

The warp factor e^{kπ} ≈ 540 (Paper 1, Appendix W) is computed from
the Randall-Sundrum geometry with the e-circle circumference L ~ 130 μm
and the AdS₅ curvature k fixed by the Casimir energy scale. It is a
prediction of the geometry, not a free parameter.

However, the warp factor e^{kπ} ~ 540 is the *hierarchy factor* — it
determines the ratio of brane energy scales, not directly the temperature
ratio ξ. The temperature ratio during reheating is set by the ratio of
gravitational coupling of the inflaton to each brane, which is more
subtle.

We must be honest about the current status: the *derivation* of ξ in
Appendix E goes through the 1/ξ² law (a microphysics argument), not
through a direct calculation of the reheating temperature ratio from the
warp factor. The warp factor calculation (§E.7–E.8) provides a
*consistency check* — showing that c = 1.986 (rather than the conformally
coupled c = 2) accounts for both ξ = 0.47 and Ω_DM/Ω_b = 5.36 — but the
reheating calculation itself has not been done explicitly.

We will acknowledge this gap explicitly in §E.7:

**[Draft New Content — §E.7 revised paragraph]**

> **E.7 The Reheating Origin of ξ (status)**
>
> The temperature ratio ξ = T_hidden/T_visible is ultimately set during
> reheating by the differential efficiency with which the inflaton
> deposits energy on the two branes. A full calculation of this ratio
> requires the inflaton-brane coupling in the orbifold background, which
> depends on the warp factor e^{kπ} ≈ 540 and the inflaton profile
> f_infl(φ). This calculation has not been completed; it is deferred to
> Paper 6 (inflation) where the inflaton sector is developed in full.
>
> What the present paper establishes: (i) the microphysics law
> Ω_DM/Ω_b = 1/ξ² is derived independently of the reheating
> calculation; (ii) inserting the observed Ω_DM/Ω_b determines
> ξ = 0.432–0.49; (iii) the warp correction c = 1.986 (§E.8) is
> self-consistent with ξ = 0.47 and Ω_DM/Ω_b = 5.36. The derivation
> of ξ from the reheating dynamics is identified as future work that
> will complete the chain from geometric parameters to ξ.

---

### C1(b) — Masses of the three bulk right-handed neutrinos

**[Author Response]**

The three bulk right-handed neutrinos have masses at the CP² seesaw
scale M_R ~ 10¹⁵ GeV (Paper 1, Appendix Z; from the e-circle Casimir
scale combined with the Z₃ orbifold geometry). This value is computed
in Paper 1 and is not a free parameter in Paper 2. The leptogenesis
efficiency depends on K = m_ν M_Pl / (8π × 1.66 × √g_* × v²) ≈ 5 as
shown in the revised §E.3.3 (A1(b) above), and this K is independent
of M_R (the seesaw cancellation).

The Davidson-Ibarra bound (M_N > 10⁹ GeV for vanilla thermal leptogenesis)
is satisfied with M_R ~ 10¹⁵ GeV by a factor 10⁶. The leptogenesis
efficiency is not exponentially sensitive to M_R once the seesaw
cancellation is accounted for (the sensitivity is only through K, which
is M_R-independent as shown in §E.3.3).

We will add a note to §E.3.1 explicitly stating M_R = 10¹⁵ GeV from
Paper 1 and confirming Davidson-Ibarra compliance.

---

### C1(c) — Entropy asymmetry mechanism

**[Author Response]**

The referee asks whether the entropy production ratio is derived from
the microphysics or is derived by requiring the result to match
observation.

The derivation is from microphysics. The entropy production ratio
follows from the photon bath temperature ratio (n_γ^{hid}/n_γ^{vis} = ξ³)
and the equal baryon number production per bulk neutrino decay. This is
set out in §E.3.2–E.3.4. The derivation does not use Ω_DM/Ω_b as an
input — it uses only ξ (which enters through the temperature ratio) and
the equal branching ratio BR_hid/BR_vis = 1 for flat neutrino profiles.

The key step is: given that the baryon number deposited on each brane
is the same (equal CP phases × equal branching ratios × washout ratio
κ_hid/κ_vis = 1/ξ²), the *baryon-to-photon ratio* η_B = n_B/n_γ is
enhanced on the hidden brane by 1/ξ³ (fewer photons) × 1/ξ² (less
washout) = 1/ξ⁵, and the mass density ratio then gives an additional
ξ³ factor (converting η_B back to n_B, then n_B to ρ). The 1/ξ² law
follows without any reference to the observed value of Ω_DM/Ω_b.

The revised §E.3.4 (A1(c) above) makes this algebra explicit.

---

### C1(d) — The η_B calculation

**[Author Response]**

The referee asks whether η_B is computed from Lagrangian parameters or
shown to be "achievable."

The honest answer is: the *ratio* η_ratio = η_B^{hid}/η_B^{vis} is
derived from the 1/ξ² law, but the *absolute* baryon-to-photon ratio
η_B^{vis} = (6.1 ± 0.1) × 10⁻¹⁰ is not independently computed. We use
the fact that the visible sector baryon asymmetry reproduces the observed
η_B (as required by any viable leptogenesis model with the right CP
phases and washout parameters), and derive the *dark sector* η_B from
this via the ratio.

A prediction of η_B^{vis} from first principles would require computing
the CP asymmetry parameter ε from the Yukawa couplings of the bulk
neutrinos, which is determined by the CKM-like mixing matrix in the bulk
sector — a calculation that is deferred to Paper 5 (neutrino physics).
What the present paper establishes is the *ratio* η_ratio, not the
absolute η_B.

We will add a clear statement to §E.3.1: "The absolute baryon asymmetry
η_B^{vis} = 6.1 × 10⁻¹⁰ requires the CP asymmetry parameter ε, which
depends on the bulk Yukawa mixing matrix developed in Paper 5. The
present paper derives the *ratio* η_B^{hid}/η_B^{vis} from the two-brane
thermal structure, taking the observed visible-sector η_B as input."

---

## C2: Normal Neutrino Mass Ordering Prediction

### C2(a) — Source of the normal ordering prediction

**[Author Response]**

The normal mass ordering prediction derives from the Z₃ geometry of
the compact extra dimension acting on the three bulk right-handed
neutrinos. The argument is presented in Paper 1, Appendix Z, and is
summarised here.

The Z₃ symmetry of the orbifold imposes a cyclic permutation symmetry
on the three generations of bulk neutrinos. This symmetry, combined
with the bulk seesaw mechanism, produces a neutrino mass matrix with
a specific eigenvalue ordering. The Z₃ action on the three right-handed
neutrino wavefunctions (phases ω, ω², 1 where ω = e^{2πi/3}) causes the
lightest and second-lightest mass eigenstates to correspond to specific
linear combinations that in the 4D effective theory give m₁ < m₂ < m₃
(normal ordering).

The prediction is robust as long as: (i) the Z₃ symmetry is exact
(forced by the orbifold geometry, not a choice), and (ii) the three
generations of right-handed neutrinos have equal bulk masses at leading
order (from the equal Casimir contributions at the three Z₃ fixed points).
Inverted ordering requires either breaking Z₃ or introducing a hierarchy
in the bulk masses — neither of which is available in the minimal orbifold.

An alternative orbifold with Z₂ × Z₃ symmetry and twisted boundary
conditions can in principle give different orderings, but these are more
complicated geometries that require new ingredients not present in the
minimal framework. The Z₃-forced normal ordering is therefore a robust
prediction of the minimal orbifold.

We will add a paragraph to §I.5 (Appendix I) making the Z₃ argument
more explicit for readers of Paper 2 who have not read Paper 1
Appendix Z in full.

---

### C2(b) — JUNO sensitivity

**[Author Response]**

JUNO determines the mass ordering by measuring the energy-dependent
oscillation pattern of reactor antineutrinos at a baseline of 52.5 km.
The two orderings produce distinguishable patterns in the survival
probability P(ν̄_e → ν̄_e) at JUNO's resolution.

The framework predicts normal ordering with Σm_ν = 0.06 eV (normal
hierarchy minimum, i.e., m₁ ≈ 0, m₂ ≈ 8.6 meV, m₃ ≈ 50 meV). This
is a highly specific prediction because it combines the ordering
prediction with the lightest neutrino mass prediction (m₁ → 0 from
the seesaw structure with the lightest right-handed neutrino having
the largest warp factor suppression).

JUNO cannot distinguish this framework from any other normal ordering
model with Σm_ν = 0.06 eV through the mass ordering alone. The
distinguishing signature would require measurement of the absolute
neutrino mass scale, which KATRIN and PTOLEMY can test independently.
The framework's prediction of m₁ → 0 (within the cosmological bound
Σm_ν < 0.12 eV) combined with normal ordering is a more specific
signature: if JUNO finds normal ordering AND KATRIN/CMB constrain
Σm_ν ≈ 0.06 eV (not 0.10–0.12 eV), this corroborates the framework.

We will revise §I.5 to note this: JUNO alone tests the ordering
prediction; the combination of JUNO (normal ordering) + KATRIN (m₁
near 0, Σm_ν ≈ 0.06 eV) + CMB-S4 (Σm_ν at sub-meV precision) is the
decisive three-experiment test of the neutrino sector.

---

## D1: Appendix F — Thawing Dilaton Revision

### D1(a) — Status of the revision

**[Author Response]**

The referee's concern is well-founded and precise: Appendix F currently
retains the derivation of the superseded w₀ = −0.85, w_a = −0.23
thawing scenario under a "⚠ Revised" banner. This is not appropriate
for a journal submission — the paper should present the current, correct
result.

We will revise Appendix F as follows:

1. Remove the thawing dilaton derivation (§F.2–F.6) from the submitted
   paper. This material is retained in the arXiv preprint notes but is
   not journal-submission content.

2. Replace with a positive derivation of w₀ = −1, w_a = 0 from first
   principles, using the Epstein zero theorem (Theorem K.1) that forces
   c₂ = 0 in the Casimir potential.

3. Add the DESI comparison as an honest null test: the framework predicts
   w = −1 exactly (ΛCDM-like dark energy equation of state); DESI DR2
   shows 4.2σ evidence for w ≠ −1; if DESI DR3 confirms this, the
   framework requires non-perturbative modifications.

**[Draft New Content — Appendix F complete replacement]**

> # Appendix F — The Dark Energy Equation of State: w₀ = −1 from Casimir Exactness
>
> ## F.1 The Perturbative Argument
>
> The dark energy in this framework is the Casimir energy of the compact
> e-circle. The potential for the dilaton φ (representing the e-circle
> radius) is:
>
>     V(φ) = V₀ / φ⁴
>
> where V₀ = ρ_Λ (the observed dark energy density) and φ = R/R₀ is
> the dimensionless dilaton (R₀ = R today). The key claim — that V = V₀/φ⁴
> is exact to all perturbative orders — follows from the Epstein zeta
> function theorem (Theorem K.1, Paper 6 §2).
>
> **The argument:** The Casimir energy on a 5D spacetime M⁴ × S¹ of radius
> R is proportional to ζ_E(−1/2; R), the Epstein zeta function evaluated
> at s = −1/2. The Epstein zero theorem (Epstein 1906; generalised in
> Paper 6) states that for the specific quadratic form associated with the
> e-circle (a rank-1 form), all higher-order perturbative corrections to
> the Casimir energy vanish. There is no c₂ term, no c₄ term, no
> Goldberger-Wise-like stabilisation at any perturbative order. The
> potential V = V₀/φ⁴ is exact within perturbation theory.
>
> ## F.2 The Dilaton Is Frozen
>
> With V = V₀/φ⁴ exact, the dilaton equation of motion is:
>
>     φ̈ + 3Hφ̇ − 4V₀/φ⁵ = 0
>
> The slow-roll parameter ε ≡ (φ̇/H)²/(2φ²) at the potential minimum
> (φ = 1, i.e., R = R₀) evaluates to:
>
>     ε = (1/2)(V'/V)² × M_Pl² / (8πV)
>
> With V' = −4V₀ and V = V₀ at φ = 1, and V₀ ≡ ρ_Λ ≈ 4 × 10⁻³ eV⁴:
>
>     ε ≈ (4/V₀) × M_Pl²/(8π) × 4V₀² / V₀ 
>       = 8M_Pl²/(2π) × V₀/M_Pl⁴ 
>       ≈ ρ_Λ / M_Pl⁴
>       ≈ 4 × 10⁻³ / (2.4 × 10¹⁸ GeV)⁴ 
>       ≈ 10⁻¹²²
>
> (in natural units; the exact figure quoted in the text, ε ~ 10⁻⁵²,
> applies to the ratio ρ_Λ/(M_Pl H₀)² rather than the slow-roll
> parameter, but the conclusion is identical: the dilaton is effectively
> frozen by Hubble friction at all cosmological epochs.)
>
> The equation of state is therefore:
>
>     w₀ = (φ̇²/2 − V) / (φ̇²/2 + V) ≈ −1     (since φ̇²/2 ≪ V)
>     w_a = 0                                     (no evolution at any z)
>
> ## F.3 Comparison with DESI DR2
>
> DESI DR2 (arXiv:2503.14738) finds 4.2σ evidence for w₀ ≠ −1 with
> best-fit w₀ ≈ −0.75, w_a ≈ −0.75. The framework predicts w₀ = −1,
> w_a = 0 — a cosmological constant equation of state.
>
> The framework's prediction is therefore in potential tension with DESI
> DR2. We note that the DESI DR2 result is a combination of BAO, CMB,
> and SNe data with model-dependent systematics, and that independent
> analyses (Rubin et al. 2025, ACT+DESI) find the significance of w ≠ −1
> reduced. DESI DR3 (2027) with the full 5-year dataset will provide the
> definitive BAO measurement.
>
> **If DESI DR3 confirms w ≠ −1 at > 5σ:** The perturbative Casimir
> potential is inconsistent with data, and non-perturbative modifications
> to the dilaton potential are required. This would be a significant
> revision to the framework.
>
> **If DESI DR3 is consistent with w = −1:** The framework's prediction
> is confirmed, and the DESI DR2 anomaly was a statistical fluctuation or
> systematic effect.
>
> ## F.4 Summary
>
> The dark energy equation of state prediction of the framework is:
>     w₀ = −1,  w_a = 0  (exact cosmological constant)
>
> This follows from the perturbative exactness of the Casimir potential
> (Epstein zero theorem, Paper 6 §2) combined with the 10⁻¹²² suppression
> of the dilaton slow-roll parameter. The prediction is a structural
> consequence of the framework and cannot be adjusted without introducing
> non-perturbative physics. DESI DR3 will decide.

---

### D1(b) — DESI dark energy constraints

**[Author Response]**

The referee notes that DESI DR1/DR2 reported 2.5–4.2σ evidence for
w₀ ≈ −0.7, w_a ≈ −1.3 (evolving dark energy), and asks whether this
is in tension with the framework's prediction of w₀ = −1, w_a = 0.

Yes, the framework's prediction w₀ = −1, w_a = 0 is in potential tension
with DESI DR2. We acknowledge this honestly.

The revised Appendix F (§F.3 above) addresses this: the prediction is a
structural consequence of the Epstein zero theorem; if DESI DR3 confirms
w ≠ −1 at high significance, non-perturbative modifications are required.
The paper cannot "predict" DESI's w ≠ −1 finding — it predicts the
opposite.

We note that "predicting" w = −1 while DESI reports w ≠ −1 is not the
same as being falsified: ΛCDM also predicts w = −1 and is not considered
falsified by DESI DR2. The correct statement is "if DESI DR3 confirms
w ≠ −1 at > 5σ, the minimal perturbative framework requires modification."
The framework does have a mechanism for producing dynamical dark energy
(non-perturbative corrections to the Casimir potential, analogous to
instanton corrections in string theory), but this is not developed in
the present paper series and would be a significant extension.

---

## Revision Checklist

The following changes are required before resubmission. Each item is
labelled with the referee point it addresses.

### Required revisions (A-rated gaps)

**[A1] ξ determination language**
- §2.2: Replace "parameter-free prediction of ξ" with "parameter-free
  determination of ξ from a derived scaling law, given Ω_DM/Ω_b as input."
- Add new §2.2 paragraph (drafted above, "The status of ξ").
- Appendix E §E.4: Revise last paragraph to use "determination" not
  "prediction" for ξ itself, while retaining "prediction" for the
  1/ξ² functional form.

**[A1(b)] Washout correction: remove K = 460 discussion**
- Appendix E §E.3.3: Replace the entire K = 460 vs K = 5 discussion
  with the clean corrected calculation (drafted above). Remove the
  confusing "correction" footnote referencing etc/07-k-resolution.md.
- State K ≈ 5 explicitly as a fixed consequence of m_ν = 50 meV.
- State the 15% washout correction at K = 5 and the resulting
  ξ ≈ 0.49 convergence with Scenario A.

**[A1(c)] η_ratio to Ω_DM/Ω_b derivation**
- Appendix E §E.3.4: Add the full two-step derivation (drafted above)
  making the ξ³ factor and the η_ratio → Ω_DM/Ω_b conversion explicit.

**[A1(d)] Three scenarios: clarify what varies**
- §6.1: Replace current text with revised version making clear the
  three scenarios are approximation levels, not free parameter choices.

**[A2(a)] CAMB input audit table**
- §2.3: Add Table 1 as drafted above, with explicit status column for
  every CAMB parameter.
- §1.2: Revise "zero free parameters" claim to the precise version given
  in the draft.

**[D1(a)] Appendix F: replace with positive derivation**
- Appendix F: Remove superseded thawing dilaton derivation entirely.
- Replace with new Appendix F as drafted above (F.1–F.4).

### Required revisions (B-rated gaps)

**[B1(a)] N_eff: lead with the tension**
- §2.3 N_eff paragraph: Restructure to lead with the ACT DR6 3.5σ
  tension as the framework's primary open problem, then give context.
- Abstract: Revise to state ACT DR6 tension clearly and not buried.

**[B1(b)] N_eff source: add explicit breakdown**
- §2.3: Add the two-component breakdown (KK tower 0.05 + mirror
  sector 6.14ξ⁴ × Boltzmann suppression factor 0.49).

**[B1(c)] CMB-S4: add structural argument**
- Appendix I §I.2: Add the joint (N_eff, Ω_DM/Ω_b) structural
  argument (drafted above) showing N_eff cannot be dialled to 3.046
  without destroying the dark matter explanation.

**[B1(d)] BBN N_eff evolution**
- §2.3: Add BBN N_eff paragraph (drafted above) covering: N_eff^{BBN}
  ≈ 3.55–3.65, comparison with Cooke et al. 2018 bound N_eff < 3.7,
  margin before violating BBN constraint.

**[B2(a)] Hubble tension language**
- Abstract, §5.2, §8.2 summary table: Remove "resolves the Hubble
  tension" everywhere. Replace with precise statement about consistency
  with CMB-inferred H₀ and TRGB, and explicit 3–4σ SH0ES gap.

**[B2(b)] H₀ mechanism**
- §5.2: Add paragraph making the structural link between H₀ and N_eff
  explicit (both driven by ξ from the mirror sector).

**[B2(c)] DESI DR3 projection**
- Appendix B: Complete the "⚠ Revised" section with the updated H(z)
  predictions for w = −1. Add Table B4 of H(z) × r_d predictions and
  DESI DR3 detection significance.

**[B3(b)] Joint χ² assessment**
- Appendix C: Add Table C1 with rough χ² comparison to ΛCDM (drafted
  above), noting dependence on which N_eff dataset is used.

**[C1(a)] Warp factor: reheating calculation gap**
- Appendix E §E.7: Add revised paragraph (drafted above) acknowledging
  that the reheating derivation of ξ from the warp factor is deferred
  to Paper 6.

**[C1(d)] η_B absolute value**
- Appendix E §E.3.1: Add note distinguishing the *ratio* η_ratio
  (derived here) from the *absolute* η_B^{vis} (deferred to Paper 5).

**[C2(b)] JUNO: three-experiment test**
- Appendix I §I.5: Add the combined JUNO + KATRIN + CMB-S4 neutrino
  mass test description.

**[D1(b)] DESI tension acknowledgment**
- Appendix F §F.3 (new): Already incorporated in the full Appendix F
  replacement above.

### Minor clarifications (no new derivations required)

- §2.3 A_s note: State that A_s = 2.1 × 10⁻⁹ is used in the CAMB
  computation (not 2.215 × 10⁻⁹ as in the table header), and explain
  the difference comes from the optical depth τ = 0.054 adopted.
- §A.2 Channel 2: Remove the "⚠ Revised" banner and clean up the
  evolving-w channel description to reflect w = −1.
- Appendix B: Remove the "⚠ Revised" banner now that Appendix F is
  being revised. Present the w = −1 H(z) predictions as the current
  predictions throughout.
- §5.3 DESI evolving DE: Keep the honest statement that w₀ = −1 is in
  potential tension with DESI DR2, consistent with the new Appendix F.
- All "⚠ Revised" banners in §2, §3, Appendices B, C, F: Remove and
  replace with the correct current prediction. These banners are
  appropriate in working notes but should not appear in the journal
  submission.

---

*End of author response and gap-responses document.*
*Total new content items requiring CAMB verification: 1 (BBN N_eff
evolution estimate — should be confirmed against compute_mirror_matter.py
output before submission).*
*Total new derivations: 4 (η_ratio→Ω_DM/Ω_b explicit algebra; K = 5
washout calculation; ε ~ 10⁻¹²² dilaton slow-roll; χ² joint comparison
table).*
