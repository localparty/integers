# 4. Reheating (φ Oscillates around φ_min)

*This section is unique to Paper 6.*

## 4.1 Dilaton Decay

After inflation ends, the dilaton `φ` oscillates around `φ_min`.
Each oscillation is a coherent excitation of the e-circle radius —
the fifth dimension pulsing around its equilibrium size. These
oscillations decay into Standard Model particles through the
dilaton's gravitational coupling to the energy-momentum tensor.

The dilaton decay rate to all SM species:

    Γ_φ = (m_φ,inf³)/(8π M_Pl²) × N_channels

where `m_φ,inf` is the effective dilaton mass during the oscillation
phase. Near the minimum, `m_φ,inf ~ V₀^{1/4} ~ H_inf` (the
inflationary Hubble scale). For `H_inf ~ 10¹³ GeV`:

    Γ_φ = (10¹³)³ / (8π × (2.4 × 10¹⁸)²) × g_*
        ≈ 10³⁹ / (1.45 × 10³⁸) × (106/25)
        ≈ 6.9 × 4.2
        ≈ 29 GeV

(The factor `g_*/25 ≈ 4.2` accounts for the ~106 SM degrees of
freedom weighted by their spin.)

## 4.2 The Reheating Temperature

The universe thermalizes when the dilaton decay rate exceeds the
Hubble rate: `Γ_φ > H`. The reheating temperature:

    T_reh = (90/(π²g_*))^{1/4} × (Γ_φ M_Pl)^{1/2}

    = (90/(106π²))^{1/4} × (29 × 2.4 × 10¹⁸)^{1/2} GeV

    = 0.55 × (7.0 × 10¹⁹)^{1/2} GeV

    = 0.55 × 8.4 × 10⁹ GeV

    **T_reh ≈ 5 × 10⁹ GeV**

## 4.3 Consequences of T_reh ~ 5 × 10⁹ GeV

The reheating temperature determines which processes occur in the
thermal bath:

| Process | Required temperature | Status |
|---|---|---|
| Electroweak baryogenesis | `> 100 GeV` | ✅ Above threshold |
| Thermal leptogenesis | `> M_N ~ 10¹⁴ GeV` | ❌ Below threshold |
| Non-thermal leptogenesis | `> m_φ/2` (dilaton can produce N_i) | ✅ See §5 |
| Mirror sector thermalization | `> T_reh × ξ` | ✅ Hidden brane heated |
| Gravitino production | `> m_{3/2}` | Depends on SUSY breaking |

The critical point: `T_reh ~ 5 × 10⁹ GeV` is BELOW the bulk
neutrino mass `M_N ~ 10¹⁴ GeV`. The heavy neutrinos are NOT
produced thermally. This eliminates the standard thermal
leptogenesis pathway — but opens the non-thermal pathway through
direct dilaton decay (§5).

## 4.4 The Dilaton Coupling Structure

The dilaton couples to matter through the trace of the energy-
momentum tensor:

    L_int = (σ/M_Pl) × φ × T^μ_μ

where `σ = 1/√3` (Paper 1, Appendix I). This coupling is:

- **Universal:** all massive particles couple with the same strength
- **Gravitational:** suppressed by `1/M_Pl`
- **Trace-proportional:** massless gauge bosons couple only through
  the trace anomaly

The dilaton decays to:
- `φ → t t̄` (dominant for `m_φ > 2m_t`): Γ ∝ m_t² m_φ / M_Pl²
- `φ → W⁺W⁻, ZZ`: Γ ∝ m_W⁴ / (m_φ M_Pl²)
- `φ → gg` (via trace anomaly): Γ ∝ α_s² m_φ³ / M_Pl²
- `φ → N_i N_i` (bulk neutrinos): Γ ∝ M_N² m_φ / M_Pl² (§5)

During the oscillation phase (`m_φ ~ H_inf`), all channels with
`m < m_φ/2` are kinematically accessible, including the bulk
neutrinos if `M_N < m_φ/2 ~ H_inf/2 ~ 5 × 10¹² GeV`. For
`M_N ~ 10¹⁴ GeV`: the bulk neutrinos are NOT kinematically
accessible from the oscillating dilaton either.

However, the dilaton can still produce bulk neutrinos through
off-shell decay during the initial large-amplitude oscillations
(when the effective dilaton energy exceeds `2M_N`). This is the
non-thermal production mechanism of §5.
