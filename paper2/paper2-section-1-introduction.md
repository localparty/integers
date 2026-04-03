# Paper 2 — Section 1: Introduction

## 1.1 Context

Paper 1 established the 5D e-dimension framework: a single compact
`U(1)` circle in which quantum mechanics, electromagnetism, gravity,
UV finiteness, and twenty-two additional phenomena are geometric
consequences of the projection from five to four dimensions.

The cosmological predictions of Paper 1 were stated qualitatively:
- `H₀ ≈ 68–70 km/s/Mpc` from hidden-brane dark radiation
- `w(z)` evolving from `−1` toward `−0.8` from the thawing dilaton
- `S8` suppressed by elevated `N_eff` and evolving dark energy
- `t₀` younger than Planck `ΛCDM` by up to 500 Myr

Paper 2 makes these quantitative. Using the CAMB Boltzmann solver
with parameters derived entirely from the e-circle geometry — no
free fits to cosmological data — we compute the complete expansion
history `H(z)`, the CMB power spectrum, and all derived cosmological
observables.

## 1.2 The Central Claim

**The framework fits zero parameters to the CMB.** Two observational
inputs — `ρ_Λ` (which fixes `L ~ 130 μm` via the Casimir energy, Paper 1
§6.6) and `Ω_DM/Ω_b = 5.36` (which fixes `ξ = 0.432` via the `1/ξ²` law,
Appendix E) — together with quantities derived from the e-circle
geometry in Paper 1:

| Quantity | Value | Derivation chain (Paper 1) |
|----------|-------|---------------------------|
| `L` | ~130 `μm` | Casimir energy = `ρ_Λ` (§6.6) |
| `w₀`, `w_a` | −0.85, −0.23 | Dilaton potential from `L` (Appendix Q/F) |
| `Σm_ν` | 0.06 eV | Bulk seesaw from `M₅ = (M_P²/L)^{1/3}` (Appendix Z) |
| `N_eff^{tower}` | 0.05 | Intra-tower decays (Appendix Y, Gonzalo et al.) |
| `ΔN_eff^{mirror}` | `6.14 × ξ⁴` | Hidden-brane dark radiation (Appendix Y) |

and inherited SM/Planck parameters (`ω_b h²`, `A_s`, `n_s` — unchanged from
`ΛCDM`) determine every cosmological observable computed here.

In `ΛCDM`, six parameters are fitted to the CMB. In this framework,
zero CMB parameters are fitted; `H₀`, `ω_c h²`, `t₀`, `S8`, `θ*`, `r_d`, `N_eff`,
and `H(z)` are all predictions. The framework either works or it
doesn't.

## 1.3 The Key Results (Preview)

The five headline results, derived in the appendices:

1. **`t₀ = 13.470 Gyr`** — 327 Myr younger than Planck `ΛCDM`, from
   the higher `H₀` predicted by the mirror sector (Appendix A).

2. **`θ*` matched to 0.5 arcseconds** — the CMB first peak angular
   scale is reproduced within Planck's measurement uncertainty,
   despite using a completely different {`H₀`, `N_eff`, `w(z)`, `Ω_m`}
   (Appendix A).

3. **`S8 = 0.753`** — the matter clustering tension dissolves. The
   framework lands within `1σ` of all three major weak lensing surveys
   without tuning (Appendix C).

4. **`H(z)` fingerprint** — the expansion history peaks 4–6% above
   `ΛCDM` at `z ~ 0.3–0.7`, a specific prediction testable by DESI DR3
   (Appendix B).

5. **`Ω_DM/Ω_b ≈ 5.2`** — the cosmic coincidence is explained by
   `η_ratio × ξ³`, where `η_ratio ~ 50` arises from warp-factor-enhanced
   dilaton baryogenesis on the hidden brane (Appendix E).

## 1.4 Organization

| Appendix | Content |
|----------|---------|
| A | The age computation: modified Friedmann equation and CAMB results |
| B | The expansion history `H(z)` and DESI predictions |
| C | `S8` resolution: `N_eff` + evolving `w(z)` mechanism |
| D | The sound horizon `r_d` and BAO predictions |
| E | Mirror baryogenesis and the cosmic coincidence `Ω_DM/Ω_b` |
| F | The thawing dilaton: `w(z)` trajectory and DESI DR2 comparison |
| G | CMB angular scale `θ*` consistency check |
| H | JWST early galaxies: what the framework addresses and what it doesn't |
| I | Decisive tests: CMB-S4, DESI DR3, GW sirens, Euclid |

## 1.5 Relationship to Paper 1

Paper 2 is self-contained but references Paper 1 throughout. The
key results inherited from Paper 1:

- The 5D Friedmann equation (Paper 1, Appendix Q)
- The hidden-brane dark radiation `ΔN_eff = 6.14ξ⁴` (Paper 1, Appendix Y)
- The dilaton potential `V(φ) ~ C/φ⁴ + V_GW(φ)` (Paper 1, Section 6.6)
- The KK tower intra-tower decays reducing `ΔN_eff^{tower}` to ~0.05
  (Paper 1, Appendix Q, citing Gonzalo et al. 2024)
- The warp factor `e^{kπ} ~ 540` on the hidden brane (Paper 1, Appendix W)
- The bulk seesaw giving `Σm_ν ~ 0.06 eV` with normal ordering
  (Paper 1, Appendix Z)
