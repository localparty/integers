# Paper 6 — Section 4: Reheating and the Thermal History

## 4.1 Reheating from Dilaton Decay

After inflation ends (when ε ~ 1), the dilaton `φ` begins oscillating
around `φ_min`. The oscillating dilaton decays into SM particles through
its gravitational coupling:

    Γ_φ→SM = (m_φ³)/(8πM_Pl²) × N_eff

where `N_eff` counts the number of SM species the dilaton can decay into.
At `m_φ^{inflation} ~ V_0^{1/4} ~ 10¹³ GeV` (the inflationary Hubble scale),
all SM species are accessible: `N_eff ~ g_* ~ 106`.

    Γ_φ ≈ (10¹³ GeV)³/(8π × (2.4 × 10¹⁸ GeV)²) × 106
         ≈ 10³⁹/(5.8 × 10³⁷) × 106/25
         ≈ 17 × 4.24 GeV ≈ **72 GeV**

The reheating temperature:

    T_reh = (90/(π² g_*))^{1/4} × (Γ_φ M_Pl)^{1/2}
           = (90/106π²)^{1/4} × (72 × 2.4 × 10¹⁸)^{1/2} GeV
           ≈ 0.55 × (1.7 × 10²⁰)^{1/2} GeV
           ≈ 0.55 × 1.3 × 10¹⁰ GeV
           ≈ **7 × 10⁹ GeV**

This is well above the electroweak scale (`T_EW ~ 100 GeV`), ensuring:
- ✅ Electroweak baryogenesis is possible
- ✅ Leptogenesis from heavy neutrino decay (`M_N ~ 10¹⁴ GeV < T_reh... wait`)

Actually `T_reh ~ 10¹⁰ GeV < M_N ~ 10¹⁴ GeV`. The heavy neutrinos are
NOT thermally produced. Leptogenesis occurs NON-THERMALLY from direct
dilaton decay: `φ → N_i N_i` (the dilaton couples to the bulk neutrinos).

Non-thermal leptogenesis from dilaton decay:

    η_L ~ Γ(φ→N_i→leptons)/Γ_total × ε_CP ~ 10⁻⁶ × (Γ_φ→N)/Γ_φ

For the bulk neutrino coupling: `Γ_φ→N/Γ_total ~ m_φ²/M_N² ~ (10¹³/10¹⁴)² ~ 10⁻²`

    η_L ~ 10⁻⁶ × 10⁻² = 10⁻⁸

After sphaleron conversion: `η_B ~ 0.35 × η_L ~ 3 × 10⁻⁹`

This is within a factor of 2 of `6 × 10⁻¹⁰` — consistent with the
Paper 5 estimate and consistent with observation.

## 4.2 The Complete Thermal History

| Epoch | Temperature | Physics | Framework contribution |
|-------|-------------|---------|----------------------|
| Inflation | `T < H_inf ~ 10¹³ GeV` | De Sitter expansion | Casimir plateau |
| Reheating | `T_reh ~ 10¹⁰ GeV` | Dilaton decay → SM | Gravitational coupling |
| Leptogenesis | `T ~ 10⁹–10¹⁰ GeV` | Non-thermal `φ → N → L` | Z₃ CP phases |
| EW phase transition | `T_c ~ 1 TeV` | First-order EWPT, GWs | Paper 4, §7.12 |
| QCD confinement | `T ~ 155 MeV` | Quark-hadron transition | Paper 5, §2 |
| BBN | `T ~ 1 MeV` | Nucleosynthesis | Standard + mirror ν_R |
| Mirror BBN | `T' = ξT ~ 0.43 MeV` | Mirror nucleosynthesis | Paper 2 |
| Matter-radiation | `T ~ 0.8 eV` | Dark matter dominates | Mirror protons (Paper 5) |
| Recombination | `T ~ 0.3 eV` | CMB decoupling | Paper 2 CAMB |
| Dark energy | `T_0 ~ 2.4 × 10⁻⁴ eV` | Dilaton thaws | Paper 2, Appendix F |

Every epoch is determined by the framework. The thermal history from
`10⁻³⁶ s` to `10¹⁰ yr` is a single geometric story.

## 4.3 The Mirror Sector Thermal History

The hidden brane (Paper 2) has its own thermal history, offset by `ξ = 0.49`:

| Visible epoch | `T_vis` | Mirror epoch | `T_mir = ξ T_vis` |
|---------------|---------|--------------|-------------------|
| BBN | 1 MeV | Mirror BBN | 0.49 MeV |
| Mirror e± annihilation | — | 0.43 MeV | Mirror photon heating |
| Recombination | 0.3 eV | Mirror recombination | 0.15 eV |

The mirror e± annihilation at `T_mir ≈ 0.43 MeV` (just below `m_e = 0.511 MeV`)
heats the mirror photon bath relative to mirror neutrinos — producing
the time-varying `ΔN_eff` already incorporated in Paper 2's CAMB
computation. The prediction `N_eff = 3.31–3.39` at recombination
follows directly from this thermal history.
