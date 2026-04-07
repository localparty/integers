# The Dark Matter-Baryon Ratio, Hubble and Clustering Tensions, and Thirteen Observables from Kaluza-Klein Geometry

## Abstract

We present the complete cosmological predictions of the 5D e-dimension
framework introduced in Paper 1, computed using the CAMB Boltzmann solver
(v1.6.6). Papers 1 and 2 develop the `M⁴ × S¹` sector — a 5D truncation
capturing quantum mechanics, electromagnetism, and cosmology — which embeds
naturally into a full 11-dimensional framework developed in companion papers.
The framework fits no free parameters to CMB data. Two observational
inputs — the dark energy density `ρ_Λ` (which fixes the e-circle circumference
`L` in Paper 1) and the dark-to-visible matter ratio `Ω_DM/Ω_b` (which fixes
the brane temperature ratio `ξ` through the scaling law below) — together
with the Standard Model field content and Planck inflation parameters
(inherited unchanged from `ΛCDM`) determine every cosmological observable.
The dark energy equation of state is `w₀ = −1`, `w_a = 0`: the perturbative
Casimir potential `V = V₀/R⁴` is exact to all orders (Epstein zero theorem,
Paper 6 §2), and the dilaton is frozen by Hubble friction at `ε ~ 10⁻¹²²`
(see Appendix F).

The central discovery of this paper is the scaling law — derived from
temperature-asymmetric bulk leptogenesis on the `Z₂` orbifold — that
*determines* `ξ`:

    Ω_DM / Ω_b = 1/ξ²

where `ξ = T_hidden/T_visible` is the hidden-to-visible brane temperature
ratio. The three bulk right-handed neutrinos (required by the orbifold
Casimir calculation) deposit baryon asymmetries on both branes; the entropy
asymmetry (`1/ξ³`) and washout suppression (`1/ξ²`) combine to give
`η_ratio = 1/ξ⁵`, which reduces to `Ω_DM/Ω_b = 1/ξ²` after multiplying by `ξ³`
(the photon-number dilution between branes). The scaling law `Ω_DM/Ω_b = 1/ξ²`
is derived without consulting the observed ratio; inserting `Ω_DM/Ω_b = 5.36`
then *determines* `ξ = 0.432` at leading order (a determination from a derived
law, not a parameter-free prediction of `ξ` in isolation). The washout
correction at `K ≈ 5` (fixed by `m_ν = 50` meV and SM parameters; `M_R`
cancels exactly) shifts the corrected `ξ` to `≈ 0.49`, converging with the
independently `θ*`-matched `ξ = 0.47` and providing a non-trivial cross-check.

Three scenarios bracket the prediction:

- **Scenario A** (`θ*`-matched, `ξ = 0.47`): `H₀ = 69.5` km/s/Mpc, `S8 = 0.753`,
  `θ*` offset = −0.5" from Planck.
- **Scenario B** (leading-order `1/ξ²` law, `ξ = 0.432`): `H₀ = 68.7` km/s/Mpc,
  `S8 = 0.785`, `θ*` offset = +6.6".
- **Scenario C** (self-consistent `ω_b`, `ξ = 0.4375`): `H₀ = 68.8` km/s/Mpc,
  `S8 = 0.754`, `θ*` offset = +1.0", at the cost of a `~2.5σ` D/H tension.

The complete prediction set, computed by CAMB across all three scenarios:

**Age of the universe:** `t₀ = 13.47–13.60` Gyr — 200–330 Myr younger than
Planck `ΛCDM`, arising from the higher `H₀` predicted by hidden-brane dark
radiation (`ΔN_eff = 6.14 × ξ⁴ = 0.21–0.30`).

**S8 tension resolved:** `S8 = 0.753–0.785`, matching all major weak lensing
surveys (DES Y3: `0.776 ± 0.017`, KiDS-1000: `0.759 ± 0.024`, HSC Y3:
`0.763 ± 0.020`) within `1σ`, resolving the `4σ` discrepancy with Planck `ΛCDM`
(`0.832`). The mechanism: elevated `N_eff` suppresses early clustering, and
lower `Ω_m = 0.290–0.302` directly reduces `S8`. Both effects are determined
by `ξ`, fixed by `Ω_DM/Ω_b` before `S8` is computed.

**Expansion history:** With `w = −1` (frozen dilaton; Appendix F),
the expansion history at the dark energy level matches `ΛCDM`. Deviations
from `ΛCDM` come from elevated `N_eff` and lower `Ω_m`, producing a
3.2–3.4% excess in `H(z) × r_d` at `z = 0.5–0.9` detectable by DESI DR3
at `6–7σ`. If DESI DR3 confirms `w ≠ −1` at `> 5σ`, non-perturbative
modifications to the dilaton potential are required.

**Sound horizon:** `r_d = 145.8–146.2` Mpc (0.6–0.9% below Planck).

**Neutrino sector:** The bulk seesaw mechanism (Paper 1) predicts
`Σm_ν = 0.06` eV with normal mass ordering from the `Z₃` orbifold geometry,
testable by JUNO within 6 years.

**The cosmic coincidence explained:** `Ω_DM/Ω_b ≈ 5` is no longer a
coincidence — it is a geometric consequence of the two-brane thermal
history. The ratio is `1/ξ²`, where `ξ` is fixed by bulk leptogenesis.

All three scenarios predict `N_eff = 3.31–3.39`, the framework's most
falsifiable near-term prediction and its primary current tension. This
value is in **3.5σ tension with ACT DR6** (`N_eff = 2.86 ± 0.13`; Qu et al.
2025), which is the framework's principal open problem. A CAMB computation
of the mirror-sector thermal history shows that mirror `e±` undergo
Boltzmann suppression at BBN (`T_mirror ≈ 0.43–0.47` MeV vs `m_e = 0.511` MeV),
producing a time-varying `ΔN_eff`: `N_eff^{BBN} ≈ 3.55–3.65` (within the
95% CL D/H bound `N_eff < 3.7`; Cooke et al. 2018), falling to
`N_eff^{recomb} = 3.31–3.39` after mirror `e±` annihilation. The `N_eff`
elevation and the `H₀` prediction are structurally linked through the
same `ξ`: the framework cannot simultaneously satisfy `N_eff ≈ 3.046` and
`Ω_DM/Ω_b ≈ 5` — the predictions stand or fall together. CMB-S4
(`σ(N_eff) ≈ 0.03`) will confirm or exclude the mirror sector at `> 9σ`.

CMB-S4 will confirm or exclude the mirror sector at `> 9σ`. DESI DR3 will
test `H(z)` at `8σ`. Euclid will test `S8` at `16σ` relative to Planck `ΛCDM`.
JUNO will test the neutrino mass ordering. The decade 2025–2035 will
decide.
