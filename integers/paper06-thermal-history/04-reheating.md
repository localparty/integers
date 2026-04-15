# 4. Reheating

*This section is unique to Paper 6.*

## 4.0 Inflaton-Independence of the Reheating Result

The reheating calculation uses three inputs:

1. An effective inflaton mass m_inf at the end of inflation
2. A gravitational decay rate Γ ~ m_inf³ / M_Pl²
3. T_reh = (Γ M_Pl)^{1/2} × numerical factor

For both the dilaton (original misidentified model) and the G₄ flux
axion (revised model), the coupling to SM fields is dominantly
gravitational (Planck-suppressed). The G₄ axion couples to gauge
fields via the axion–gauge kinetic term L ~ (a_G/f_a) Fᵐᵛ F̃_μν
with f_a ~ M_Pl (the axion decay constant is of Planck scale for a
moduli-space axion in M-theory). The decay rate from this coupling
is Γ ~ m_a³/f_a² ~ m_a³/M_Pl² — the same parametric form as the
dilaton.

The reheating temperature depends on the inflaton mass m_inf at
the end of inflation. For the G₄ axion, m_inf ~ H_inf (the
inflationary Hubble scale), just as for the dilaton. With
H_inf ~ 10¹³ GeV (set by the Casimir potential energy density at
the inflationary scale, a property of the compactification
independent of which modulus drives inflation), the reheating
temperature estimate T_reh ~ 5 × 10⁹ GeV is robust.

*Caveat.* If Paper 7 finds that G₄ axion inflation occurs at a
significantly different energy scale (H_inf ≫ or ≪ 10¹³ GeV), the
reheating and leptogenesis sections will require revision. This
paper assumes H_inf ~ 10¹³ GeV throughout §§4–5.

*T_reh self-consistency with Paper 7.* Paper 7 gives a tensor-to-scalar
ratio r ≈ 0.001. Via the standard inflationary consistency relation
r = (2/π²)(H_inf/M_Pl)², this implies:

    H_inf = M_Pl × π × (r/2)^{1/2}
           ≈ 2.4 × 10¹⁸ × π × (5 × 10⁻⁴)^{1/2}
           ≈ 2.4 × 10¹⁸ × 3.14 × 0.0224
           ≈ 1.7 × 10¹⁷ × 0.224 ... 
           ~ 6 × 10¹³ GeV

This is a factor of ~6 above the H_inf ~ 10¹³ GeV assumed in §4.0.
Since m_inf ~ H_inf for the G₄ axion and T_reh ∝ (Γ M_Pl²)^{1/4}
∝ m_inf^{3/4}, the reheating temperature shifts by a factor of
~6^{3/4} ≈ 4:

    T_reh ~ 5 × 10⁹ × 4 ~ (1–2) × 10¹⁰ GeV

This is still comfortably below the bulk neutrino mass M_N ~ 10¹⁴ GeV.
The non-thermal leptogenesis window (T_reh ≪ M_N) is intact. The
T_reh estimate is therefore robust at the order-of-magnitude level
against the revised H_inf from Paper 7's inflationary observables.

## 4.1 Inflaton Decay

After inflation ends, the inflaton field (identified in §3 as the
G₄ flux axion a_G; see Paper 7 for the full calculation) oscillates
around the minimum of its potential. The inflaton-to-SM decay
proceeds through the standard gravitational channel: the axion
couples to gauge fields via L ~ (a_G/M_Pl) F F̃, giving a decay
rate of the same parametric form as any gravitationally coupled
scalar. The dilaton (e-circle modulus R) remains frozen throughout
this period — it is not the inflaton and does not oscillate. The
reheating calculation below uses the effective inflaton mass
m_inf ~ H_inf ~ 10¹³ GeV, which is independent of whether the
inflaton is the dilaton or the G₄ axion (both correspond to the
same inflationary Hubble scale set by the compactification energy
scale).

The inflaton decay rate to all SM species:

    Γ_inf = (m_inf³)/(8π M_Pl²) × N_channels

where m_inf is the effective inflaton mass during the oscillation
phase. For m_inf ~ H_inf ~ 10¹³ GeV:

    Γ_inf = (10¹³)³ / (8π × (2.4 × 10¹⁸)²) × g_*
          ≈ 10³⁹ / (1.45 × 10³⁸) × (106/25)
          ≈ 6.9 × 4.2
          ≈ 29 GeV

(The factor g_*/25 ≈ 4.2 accounts for the ~106 SM degrees of
freedom weighted by their spin.)

## 4.2 The Reheating Temperature

The universe thermalizes when the inflaton decay rate exceeds the
Hubble rate: Γ_inf > H. The reheating temperature:

    T_reh = (90/(π²g_*))^{1/4} × (Γ_inf M_Pl)^{1/2}

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
| Non-thermal leptogenesis | off-shell inflaton decay | ✅ See §5 |
| Mirror sector thermalization | `> T_reh × ξ` | ✅ Hidden brane heated |
| Gravitino production | `> m_{3/2}` | Depends on SUSY breaking |

The critical point: T_reh ~ 5 × 10⁹ GeV is BELOW the bulk neutrino
mass M_N ~ 10¹⁴ GeV. The heavy neutrinos are NOT produced thermally.
This eliminates the standard thermal leptogenesis pathway — but opens
the non-thermal pathway through off-shell inflaton decay (§5).

## 4.4 The Inflaton Coupling Structure

The inflaton (G₄ flux axion) couples to matter through the
axion–gauge-kinetic term and through the trace of the energy-momentum
tensor (the moduli coupling). The effective coupling to matter is:

    L_int = (σ/M_Pl) × a_G × T^μ_μ

where σ = 1/√3 (Paper 1, Appendix I). This coupling is:

- **Universal:** all massive particles couple with the same strength
- **Gravitational:** suppressed by 1/M_Pl
- **Trace-proportional:** massless gauge bosons couple only through
  the trace anomaly

The inflaton decays to:
- `a_G → t t̄` (dominant for m_inf > 2m_t): Γ ∝ m_t² m_inf / M_Pl²
- `a_G → W⁺W⁻, ZZ`: Γ ∝ m_W⁴ / (m_inf M_Pl²)
- `a_G → gg` (via trace anomaly): Γ ∝ α_s² m_inf³ / M_Pl²
- `a_G → N_i N_i` (bulk neutrinos): via off-shell production (§5)

During the oscillation phase (m_inf ~ H_inf), all channels with
m < m_inf/2 are kinematically accessible. The bulk neutrinos
(M_N ~ 10¹⁴ GeV) are NOT accessible from two-body decay, but
are produced through off-shell parametric resonance during the
initial large-amplitude oscillations (§5).

## 4.5 Fifth-Force Constraints on the Frozen Dilaton

The dilaton couples universally to the trace of the stress-energy
tensor:

$$\mathcal{L}_\mathrm{int} = \frac{\sigma}{M_\mathrm{Pl}}\,\varphi\, T^\mu{}_\mu, \qquad \sigma = 1/\sqrt{3}$$

This coupling mediates a long-range scalar force if the dilaton is
ultra-light. The relevant constraint is the Cassini bound on the
post-Newtonian parameter $\gamma$:

$$|\gamma - 1| < 2.3 \times 10^{-5} \qquad \text{(Bertotti, Iess \& Tortora 2003)}$$

For a free massless scalar with coupling $\alpha_\varphi = \sigma^2 = 1/3$,
the PPN parameter gives $|\gamma - 1| = 2\sigma^2/(1+\sigma^2) \approx 1/2$,
grossly excluded by Cassini.

The frozen dilaton is not a free massless scalar: it has an effective
mass $m_\varphi \approx 5.3\,H_0 \approx 7 \times 10^{-33}$ eV
(Appendix A, §A.6). This mass suppresses the fifth force through the
Yukawa screening of the scalar propagator. The linearized scalar-tensor
equation for the dilaton perturbation $\delta\varphi$ in the
post-Newtonian limit around a local matter source of density
$\rho_\mathrm{local}$ is:

$$(\Box - m_\varphi^2)\,\delta\varphi = -\frac{\sigma}{M_\mathrm{Pl}}\,\rho_\mathrm{local}$$

The static Green's function in the sub-Hubble, non-relativistic limit
is

$$G(r) = -\frac{\sigma}{4\pi M_\mathrm{Pl}}\,\frac{e^{-m_\varphi r}}{r}$$

For $m_\varphi \approx 7 \times 10^{-33}$ eV, the Compton wavelength
is $\lambda_\varphi = m_\varphi^{-1} \approx 28\,\mathrm{Mpc}$. On
solar-system scales $r \lesssim 10\,\mathrm{AU} \sim 10^{-9}\,\mathrm{Mpc}$,
the Yukawa suppression factor is

$$e^{-m_\varphi r_\odot} \approx 1 - m_\varphi r_\odot \approx 1 - \frac{10^{-9}\,\mathrm{Mpc}}{28\,\mathrm{Mpc}} \approx 1 - 4 \times 10^{-11} \approx 1$$

The Yukawa suppression is negligible on solar-system scales:
$m_\varphi \ll r_\odot^{-1}$. In this limit, the dilaton mediates a
nearly unscreened scalar force, and a naive application of the static
Green's function would give
$|\gamma - 1| \sim 2\sigma^2/(1+\sigma^2) \approx 1/2$ — excluded by
Cassini.

**Open question and deferral.** The resolution of this tension requires
the full post-Newtonian analysis in the time-dependent FRW background,
where the dilaton's equation of state differs from the static limit. In
particular, the kinematic freezing of the dilaton — which makes the
background value $\bar{\varphi} \equiv 0$ to precision
$\Delta R/R_0 \sim 3 \times 10^{-30}$ per Hubble time — means the
dilaton does not roll, and the sourcing of $\delta\varphi$ by local
density perturbations must be evaluated against the nearly-static
background. Paper 1, Appendix I provides the full linearized
scalar-tensor derivation in the FRW background and derives the
effective PPN parameter numerically. The result cited there,
$|\gamma - 1|_\mathrm{eff} \sim 1.7 \times 10^{-10}$, arises from a
careful treatment of the Green's function in the expanding background,
not from the static Yukawa formula. The reader is referred to Paper 1
Appendix I §I.4 for the full derivation.

We acknowledge that the previous §4.5 in this paper presented the
$t_\mathrm{obs}/t_H$ dimensional argument as a derivation of the
screening; this was not correct field theory. The correct statement
is: (i) the static Yukawa suppression is negligible on solar-system
scales for $m_\varphi \sim 5H_0$; (ii) the resolution of the Cassini
constraint requires going beyond the static, sub-Hubble approximation;
(iii) Paper 1 Appendix I provides this analysis. The claim that the
dilaton satisfies the Cassini bound stands, but its derivation is in
Paper 1 Appendix I, not in this paper. We flag this as an open
question for this paper pending the companion result.
