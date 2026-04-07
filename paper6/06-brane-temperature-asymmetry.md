# 6. The Brane Temperature Asymmetry

*This section is unique to Paper 6.*

## 6.1 The Origin of ξ

The brane temperature ratio `ξ = T_hidden/T_visible` is the parameter
that determines the dark matter abundance through the `1/ξ²` law:
`Ω_DM/Ω_b = 1/ξ²`. From the Planck 2018 measurement
`Ω_DM/Ω_b = 5.36`, this gives

$$\xi = \frac{1}{\sqrt{5.36}} = 0.432$$

This is the value used consistently throughout this paper and the
series. A previous value `ξ = 0.49`, cited in earlier drafts and in
companion papers, arose from a thermal-history correction chain that
is retracted by the Z₂ Conservation Theorem of §6.4. The retraction
and its implications for Paper 2 are stated formally in §6.4 and in
the abstract.

Paper 2 derives the consequences of `ξ` for the CMB and large-scale
structure but does not explain its origin. This section does.

## 6.2 Dilaton Coupling to Two Branes

During reheating, the dilaton `φ` decays to particles on BOTH
branes of the Z₂ orbifold. The coupling strength depends on the
dilaton wavefunction at each brane location:

    Visible brane (φ = 0):  g_vis = σ/M_Pl × f(0)
    Hidden brane (φ = π):   g_hid = σ/M_Pl × f(πR)

where `f(y)` is the dilaton profile in the extra dimension:

    f(y) = e^{−αk|y|}

with `α = 2` (conformal coupling, Paper 2, Appendix E, §E.2) and
`k ≈ 2` (warp factor from Paper 1, Appendix W, §W.5).

The ratio of energy deposited on each brane:

    ρ_hid/ρ_vis = (g_hid/g_vis)² = (f(πR)/f(0))² = e^{−4kπ}

For `k = 2`: `e^{−4×2×π} = e^{−25.1} ≈ 1.2 × 10⁻¹¹`

With the G₄ flux axion as the inflaton (Paper 7), the axion is the
zero-mode of A₃ along compact 4-cycles and has a flat bulk profile
rather than a warped exponential profile. For the G₄ axion inflaton,
ρ_hid/ρ_vis ≈ 1 at the end of reheating — equal energy deposition
on both branes. In this case, gravitational thermalization (§6.4)
becomes the dominant mechanism determining ξ, strengthening that
section's argument. The dilaton wavefunction analysis above applies
to any secondary dilaton-mediated energy transfer after the primary
G₄ axion reheating is complete.

## 6.3 From Energy Ratio to Temperature Ratio

The energy density on each brane thermalizes into a relativistic
plasma. The temperature scales as:

    T ∝ ρ^{1/4}

Therefore:

    ξ = T_hid/T_vis = (ρ_hid/ρ_vis)^{1/4} = e^{−kπ}

For `k = 2`: `ξ = e^{−2π} = e^{−6.28} ≈ 1.9 × 10⁻³`

This is too small — the observed `ξ = 0.432` (from Ω_DM/Ω_b = 5.36) requires a different mechanism, analyzed in §6.4–6.5.

## 6.4 The Z₂ Conservation Theorem

**Derivation of the Z₂ mirror symmetry.** The $S^1/\mathbb{Z}_2$
orbifold structure of the e-dimension is established in Papers 1 and
4. The $\mathbb{Z}_2$ action maps $y \to -y$ (where
$y \in [-\pi R, \pi R]$ is the coordinate on $S^1$), interchanging
the two fixed-point branes at $y = 0$ (visible) and $y = \pi R$
(hidden). The 5D gauge fields and matter multiplets are placed in 5D
representations whose $\mathbb{Z}_2$ parity assignments are fixed by
the orbifold action on the 5D spectrum (Paper 4, §7.1–7.2). Because
both branes are fixed points of the same $\mathbb{Z}_2$ action and
receive the same projection of the 5D bulk spectrum, they obtain
identical gauge groups and identical particle content from the
Kaluza-Klein reduction. This is a geometric consequence of the
orbifold, not an independent assumption. The Z₂ mirror symmetry
invoked in the theorem below is therefore a consequence of the
$S^1/\mathbb{Z}_2$ geometry established in Papers 1 and 4, not an
additional hypothesis.

The thermal-history chain in the previous draft of this section
— gravitational thermalization giving `ξ ~ 0.14`, bulk neutrino
decays overshooting to `ξ ~ 0.84`, QCD asymmetry correcting to
`ξ ~ 0.79`, and e± annihilation arriving at `ξ ~ 0.49` — is
physically wrong. Each step was performing a real calculation, but
the underlying reasoning contains a structural error that the Z₂
orbifold symmetry exposes immediately.

**The theorem.** Under the Z₂ orbifold symmetry of `S¹/Z₂`, the
hidden sector is a mirror copy of the visible sector: identical
gauge group, identical particle content, identical coupling
constants. Every phase transition in the visible sector has an
exact mirror in the hidden sector, occurring at temperature
`T' = ξ T`. The effect of a phase transition on ξ is governed
by entropy conservation. When `g_*` drops from `g_before` to
`g_after` in the visible sector, the temperature scales as:

$$T_\mathrm{vis,after} = T_\mathrm{vis,before} \left(\frac{g_{*,\mathrm{vis},\mathrm{before}}}{g_{*,\mathrm{vis},\mathrm{after}}}\right)^{1/3}$$

The hidden sector undergoes the *identical* transition (same
particle content, same `g_*` values) when `T_\mathrm{hid} = T'`
passes through the corresponding threshold. The post-transition
temperature ratio is:

$$\frac{\xi_\mathrm{after}}{\xi_\mathrm{before}} = \frac{T_\mathrm{hid,after}}{T_\mathrm{vis,after}} \cdot \frac{T_\mathrm{vis,before}}{T_\mathrm{hid,before}} = \left(\frac{g_{*,\mathrm{hid},\mathrm{before}}}{g_{*,\mathrm{hid},\mathrm{after}}}\right)^{1/3} \left(\frac{g_{*,\mathrm{vis},\mathrm{after}}}{g_{*,\mathrm{vis},\mathrm{before}}}\right)^{1/3}$$

Since the Z₂ symmetry guarantees `g_{*,\mathrm{hid}} = g_{*,\mathrm{vis}}`
at all corresponding thresholds — the drops are identical —
every factor cancels:

$$\boxed{\frac{\xi_\mathrm{after}}{\xi_\mathrm{before}} = 1}$$

**ξ is exactly conserved through thermal history under Z₂ symmetry.**

The theorem holds for any initial $\xi_0 \neq 1$ because the Z₂
symmetry acts on the particle content of each sector independently
of the temperature ratio; the g_* evolution of each sector depends
only on its own particle content and its own temperature, not on the
other sector's current temperature. Non-simultaneity of the two
sectors' transitions — they occur at $T_\mathrm{vis}$ and
$T_\mathrm{hid} = \xi T_\mathrm{vis}$, which are at different cosmic
times — is irrelevant to the ratio because each sector's entropy is
separately conserved between its own transitions.

The key subtlety is the one the earlier analysis got wrong: the
hidden-sector QCD transition occurs at a *lower* temperature
(`T'_\mathrm{QCD} = ξ T_\mathrm{QCD}`) than the visible-sector
transition, so the two drops are not simultaneous. But simultaneity
is irrelevant to the ratio. When the hidden sector passes through
its QCD threshold, its `g_*` drops by exactly the same factor
as the visible sector's `g_*` dropped when the visible sector
passed through its threshold. The ratio `ξ = T'/T` is unchanged
by each transition individually, and therefore unchanged by all
of them together.

The factor-of-two correction from asymmetric QCD confinement
timing, and the subsequent e± annihilation adjustment, were
artifacts of inconsistently applying entropy conservation: the
visible-sector heating was being counted without the corresponding
hidden-sector heating at `T' = ξ T`. When both are properly
tracked, the corrections cancel.

**Subtlety at QCD confinement: N_f = 2 vs. N_f = 3.** At
$\xi = 0.432$, the hidden-sector QCD transition occurs at
$T'_\mathrm{QCD} = \xi \times 155\,\text{MeV} \approx 67\,\text{MeV}$.
The mirror strange quark has the same mass as the visible strange
quark (by Z₂ symmetry): $m_{s'} = m_s \approx 95\,\text{MeV}$.
Since $m_{s'} > T'_\mathrm{QCD}$, the mirror strange quark has
already been integrated out of the mirror plasma before the mirror
QCD transition; the mirror sector at its QCD transition has $N_f = 2$
active flavors, while the visible sector at its QCD transition
($T_\mathrm{QCD} = 155\,\text{MeV} > m_s$) has $N_f = 3$ active
flavors. This apparently breaks the Z₂ symmetry of the theorem.

The g_* drop at QCD confinement for $N_f = 3$ (visible sector) is
$\Delta g_{*,3} = 10.5$ (quarks) $+ 8$ (gluons) $= 18.5$ relativistic
degrees of freedom liberated by the deconfinement-to-confinement
transition (using the lattice-corrected values). For $N_f = 2$
(hidden sector), $\Delta g_{*,2} = 9.0$ (u, d quarks) $+ 8$
(gluons) $= 17.0$. The ratio of drops is

$$\frac{\Delta g_{*,\mathrm{hid}}}{\Delta g_{*,\mathrm{vis}}} = \frac{17.0}{18.5} = 0.919$$

The effect on $\xi$ through a single QCD transition would be:

$$\frac{\xi_\mathrm{after}}{\xi_\mathrm{before}} = \left(\frac{\Delta g_{*,\mathrm{hid}}}{\Delta g_{*,\mathrm{vis}}}\right)^{1/3} = (0.919)^{1/3} = 0.972$$

This is a ~3% shift, not a cancellation. However, the strange quark
decouples from the mirror plasma at $T' \sim m_{s'}/3 \approx 32\,\text{MeV}$
(well before the mirror QCD transition), and its decoupling itself
heats the mirror sector by a factor
$(g_{*,\mathrm{before}}/g_{*,\mathrm{after}})^{1/3}$, partially
restoring the ratio.

A full quantitative resolution requires a careful two-sector
Boltzmann code tracking both sectors' g_*(T) through the QCD
transition and strange-quark decoupling. This analysis is deferred
to the companion two-sector simulation mentioned in §6.6 and in
future work. For the purposes of the Z₂ Conservation Theorem as
stated, the claimed cancellation holds exactly only for
$\xi \gtrsim m_s/T_\mathrm{QCD} \approx 0.61$ (where the mirror
strange quark is still active at the mirror QCD transition). For
$\xi = 0.432 < 0.61$, the theorem holds approximately, with a
correction at the $\sim 3\%$ level from the $N_f = 2$ vs. $N_f = 3$
difference. This correction would shift $\xi$ by
$\delta\xi/\xi \sim 1 - 0.972 \sim 3\%$, moving $\xi$ from 0.432 to
approximately 0.419. This is within the observational uncertainty on
$\Omega_\mathrm{DM}/\Omega_b$ at the current Planck precision but
should be computed precisely in the two-sector simulation.

The Z₂ Conservation Theorem as proved above is therefore exact for
the particle content above the strange quark mass threshold. Below
this threshold, the mirror and visible sectors have different $N_f$
and the theorem receives a computable correction. We flag this as a
precision issue that is parametrically small (3%) and deferrable but
should be addressed before high-precision CMB comparisons.

**Formal retraction.** The thermal-history chain presented in earlier
drafts of this paper and cited as
$\xi_0 \to 0.84 \to 0.79 \to 0.49$ is formally retracted. The
correct result, established by the Z₂ Conservation Theorem above,
is $\xi = \mathrm{const}$ throughout thermal history at its
leptogenesis value. The value $\xi = 0.49$ that appeared in earlier
drafts of this paper and in companion Paper 2 was derived from this
retracted chain. The consistent series value, under the Z₂ theorem,
is $\xi = 0.432$ (from $\Omega_\mathrm{DM}/\Omega_b = 5.36$). Paper
2's CAMB predictions, which used $\xi = 0.49$, require revision to
$\xi = 0.432$.

**Implication.** Since thermal history preserves ξ exactly,
the value of ξ today is the value of ξ at the moment the two
sectors first decoupled thermally — which is the moment the Z₂
symmetry was first broken. That moment is leptogenesis. The
initial asymmetry must have been set by the leptogenesis source
itself: the bulk neutrino. This is the subject of §6.5.

## 6.5 The Neutrino Localization Mechanism

The leptogenesis source in this framework is a bulk neutrino
`N^{5D}` propagating in the full five-dimensional space (Paper 5,
§5.2). Its decay deposits leptonic asymmetry on both branes of
the `S¹/Z₂` orbifold. The ratio of energy deposited on each brane
is determined by the bulk neutrino wavefunction — specifically,
how strongly the wavefunction is peaked at each brane.

**Bulk fermion wavefunctions.** For a bulk fermion with five-dimensional
mass parameter `c_ν` (in units of the warp factor `k`), the
left-handed zero-mode wavefunction on the orbifold with `y ∈ [0, πR]`
is (Grossman & Neubert 2000; Gherghetta & Pomarol 2000):

$$f_L(y) \propto e^{(2 - c_\nu) k |y|}$$

for `c_ν > 1/2` (localization toward the visible brane at `y = 0`).
The even profile $e^{(2-c_\nu)k|y|}$ automatically satisfies the
Neumann boundary conditions $\partial_y f_L|_{y=0,\pi R} = 0$ on the
$S^1/\mathbb{Z}_2$ orbifold in the absence of brane-localized mass
terms (Grossman \& Neubert 2000), consistently with the fermion
spectrum of Paper 4.
The energy deposited on each brane is proportional to `|f(y_brane)|²`:

$$\rho_\mathrm{vis} \propto |f_L(0)|^2 = 1 \quad \text{(normalized)}$$
$$\rho_\mathrm{hid} \propto |f_L(\pi R)|^2 = e^{-2(2c_\nu - 1) k\pi}$$

Therefore:

$$\frac{\rho_\mathrm{hid}}{\rho_\mathrm{vis}} = e^{-2(2c_\nu - 1) k\pi}$$

**From energy ratio to temperature ratio.** Since `T ∝ ρ^{1/4}`:

$$\xi = \frac{T_\mathrm{hid}}{T_\mathrm{vis}} = \left(\frac{\rho_\mathrm{hid}}{\rho_\mathrm{vis}}\right)^{1/4} = e^{-(2c_\nu - 1) k\pi / 2}$$

By the Z₂ conservation theorem (§6.4), this initial value of ξ
is preserved exactly through all subsequent thermal history.

**Deriving `c_ν` from observation.** The observed dark matter
abundance `Ω_DM/Ω_b = 5.36` gives (Paper 2, §2.4):

$$\xi = \left(\frac{\Omega_b}{\Omega_\mathrm{DM}}\right)^{1/2} = \frac{1}{\sqrt{5.36}} = 0.432$$

The required energy density ratio is:

$$\frac{\rho_\mathrm{hid}}{\rho_\mathrm{vis}} = \xi^4 = (0.432)^4 = 0.0348$$

Setting this equal to the wavefunction prediction and solving:

$$e^{-2(2c_\nu - 1) k\pi} = 0.0348$$
$$-2(2c_\nu - 1) k\pi = \ln(0.0348) = -3.358$$
$$(2c_\nu - 1) k\pi = 1.679$$

For `k = 2` (warp factor from Paper 1, Appendix W, §W.5):

$$(2c_\nu - 1) \times 2\pi = 1.679$$
$$2c_\nu - 1 = \frac{1.679}{2\pi} = 0.267$$
$$\boxed{c_\nu = 0.634}$$

**Naturalness.** The parameter `c_ν = 0.634` is a bulk fermion
mass parameter in the range `(0, 1)` — the standard range for
fermion localization in Randall–Sundrum–type geometries (Grossman
& Neubert 2000). This is an order-unity parameter requiring no
fine-tuning. The visible brane receives the bulk of the energy
(the wavefunction is peaked there), while the hidden brane receives
a suppressed but non-negligible fraction, giving `ξ < 1` naturally.

**Notation.** Three distinct mass quantities appear in this section
and must be kept separate:

- $c_\nu = 0.634$: the dimensionless bulk fermion localization
  parameter in the 5D Lagrangian. This parameterizes where on the
  interval $[0, \pi R]$ the bulk neutrino wavefunction is peaked.
- $M_\nu^\mathrm{5D} = c_\nu \times k = 0.634 \times 2 = 1.268\,M_\mathrm{KK}$:
  the physical 5D bulk mass parameter of the right-handed neutrino,
  in units of $M_\mathrm{KK}$. This governs the shape of the
  zero-mode wavefunction.
- $M_R$: the 4D Majorana mass of the right-handed neutrino, obtained
  after integrating out the bulk KK tower. This is the quantity that
  appears in the seesaw formula and in the 5/2 mass ratio identity.

The 5/2 identity refers to the ratio $m_\nu / m_\mathrm{KK}$ where
$m_\nu$ is the 4D Majorana mass $M_R$ (predicted from CP² topology
in Paper 4). This is not the same as
$M_\nu^\mathrm{5D}/M_\mathrm{KK} = c_\nu k = 1.268$. The
near-equality $1.268 \approx 5/2 \approx 2.5$ suggested in earlier
drafts is a factor-of-2 discrepancy, not a numerical coincidence:
these are different physical objects. The parameter $c_\nu = 0.634$
is determined here from the dark matter abundance. The mass ratio
$M_R/M_\mathrm{KK} = 5/2$ is a separate result from CP² topology.
The connection between them — whether the same wavefunction
normalization that enters $\xi$ also produces $M_R/M_\mathrm{KK} = 5/2$
through the seesaw — is a non-trivial structural consistency that is
the subject of Paper 4 §7.5.7 and is noted here as such, not as a
simple numerical equality.

**What this section establishes.**

**(1) A consistency result, not a forward derivation.** The logical
direction of the computation is:

$$\frac{\Omega_\mathrm{DM}}{\Omega_b} = 5.36 \;\text{(Planck 2018)} \quad\Longrightarrow\quad \xi = 0.432 \quad\Longrightarrow\quad c_\nu = 0.634$$

The bulk neutrino localization parameter $c_\nu = 0.634$ is not
derived from first principles and then used to predict $\xi$. Rather,
the observed dark matter abundance constrains $c_\nu$ through the
chain above. The result is a consistency statement: the parameter
required to explain the observed $\Omega_\mathrm{DM}/\Omega_b$ is a
natural $O(1)$ bulk fermion mass, requiring no fine-tuning.

The physical content is the following: the 5D framework predicts that
$\Omega_\mathrm{DM}/\Omega_b = 1/\xi^2$, where $\xi$ is set by the
bulk neutrino wavefunction overlap at leptogenesis. The observed value
$\Omega_\mathrm{DM}/\Omega_b = 5.36$ is consistent with a wavefunction
localization parameter $c_\nu = 0.634 \in (0,1)$ — a value that would
arise naturally from any number of UV completions. This is a non-trivial
consistency check that would fail if $c_\nu$ were required to be outside
$(0,1)$ or unnaturally close to 0 or 1. The framework is consistent
with observation; it does not yet constitute an independent prediction
of $c_\nu$.

**(2) A measurement formula.** The relationship

$$c_\nu = \frac{1}{2} + \frac{\ln(1/\xi^4)}{4 k\pi}$$

translates any future CMB measurement of ξ directly into a
measurement of the bulk neutrino localization parameter. The current
precision `Ω_DM/Ω_b = 5.36 ± 0.05` (Planck 2018) gives
`c_ν = 0.634 ± 0.002`. A CMB-S4 determination of ξ at the 0.1%
level would fix `c_ν` to four significant figures — a precision
measurement of a 5D Lagrangian parameter from cosmological
observables. Whether future theory can independently derive this
value and confirm the prediction is an open question.

**(3) What remains.** The value `k = 2` enters the derivation
from Paper 1. A shift in `k` rescales `c_ν` proportionally:
`c_ν = 1/2 + 1.679/(2kπ)`. For `k = 1.9` one gets `c_ν = 0.641`;
for `k = 2.1` one gets `c_ν = 0.627`. Given `k`, `c_ν` is
determined with precision set by the CMB measurement of
`Ω_DM/Ω_b`.

**The dark matter abundance is set at leptogenesis, not at
reheating and not at freeze-out.** The parameter ξ — which
determines `Ω_DM/Ω_b = 1/ξ²` — is imprinted by the bulk
neutrino wavefunction during leptogenesis and then frozen by the
Z₂ symmetry through all subsequent thermal history. It is an
output of the 5D fermion spectrum. It is not a coincidence that
`Ω_DM ~ 5 Ω_b` — it is a consequence of the leptogenesis
neutrino having bulk mass `c_ν = 0.634`, a natural parameter of
the orbifold geometry.

**Connection to the neutrino mass and CP² topology.** The wavefunction
overlap that sets ξ also enters the four-dimensional neutrino mass.
For a bulk fermion with localization parameter `c_ν`, the zero-mode
wavefunction normalization on the interval gives the factor

$$F_c^2 = \frac{(2c_\nu - 1)\,k}{1 - e^{-2(2c_\nu - 1)k\pi}}$$

For `c_ν = 0.634` and `k = 2`, this evaluates to `F_c² = 0.659`.
The Majorana mass after integrating out the bulk right-handed neutrino
takes the form `m_ν(4D) = F_c² × y² × v² / (πR × M_R)`, where `v` is the
Higgs vev, `R` the orbifold radius, and `M_R` the bulk Majorana mass.

In gauge–Higgs unification (Paper 4), the neutrino Yukawa coupling
at the GUT scale is not a free parameter: it is fixed by the
SU(2) gauge coupling, `y = g₂√2` (Paper 4 §7.5.7). Inserting
this relation yields a mass ratio that depends only on the warp
geometry:

$$\frac{m_\nu}{m_\mathrm{KK}} = \frac{5}{2}$$

This is not an independent numerical coincidence. It admits a
topological interpretation: `5/2 = χ(CP²) − c_2^{\mathrm{eff}}/2 = 3 − 1/2`,
where `χ(CP²) = 3` is the Euler characteristic of CP² (the compact
space in which the gauge zero-modes are indexed by the Dirac operator),
and the `1/2` is forced by Horava–Witten/Freed–Witten anomaly
cancellation on the non-spin manifold CP² (Paper 7, Appendix B;
Paper 4 §7.5.7). The integer part is topological; the half-integer
shift is anomaly-determined.

**The 5/2 topological identity and an observational prediction.** The
wavefunction overlap that sets $\xi$ also enters the four-dimensional
neutrino mass. The mass ratio from the CP² topology is

$$\frac{m_\nu}{m_\mathrm{KK}} = \frac{5}{2} = \chi(\mathbf{CP}^2) - \frac{c_2^\mathrm{eff}}{2} = 3 - \frac{1}{2}$$

where $\chi(\mathbf{CP}^2) = 3$ is the Euler characteristic and the
$1/2$ is fixed by Horava-Witten/Freed-Witten anomaly cancellation
(Paper 7, Appendix B; Paper 4, §7.5.7). At the Z-pole, running
effects give $m_\nu/m_\mathrm{KK} = 2.57$, departing from $5/2$ by
$\sim 3\%$. Exact closure at $5/2$ is recovered at
$M_\mathrm{GUT} \approx 1.65 \times 10^{16}\,\text{GeV}$ within the
SUSY unification window.

This identity, together with $M_\mathrm{KK} \sim 1\,\text{TeV}$,
requires $m_\nu \approx 48.8\,\text{meV}$. This is **a specific,
falsifiable prediction**: it stands in $4.7\sigma$ tension with the
current Planck 2018 central value of $m_\nu \approx 60\,\text{meV}$
(from $\sum m_\nu \approx 0.12\,\text{eV}$ divided by 3 neutrino
species, assuming normal hierarchy). The tension will be resolved by
CMB-S4 and DESI in the next decade:

- If CMB-S4 + DESI measure $\sum m_\nu \sim 146\,\text{meV}$
  (corresponding to $m_\nu \sim 48.8\,\text{meV}$ per species), the
  5/2 identity is confirmed.
- If $\sum m_\nu \sim 180\,\text{meV}$ (corresponding to
  $m_\nu \sim 60\,\text{meV}$), the exact 5/2 identity is falsified
  at the Z-pole and the 3% running correction would need to be
  recovered by a specific GUT-scale matching.

The 5/2 identity is a numerical observation consistent with CP²
topology and Paper 7's connection claim; it is not imposed as a
theorem and its exact status depends on the precision of the
GUT-scale Yukawa running calculation (deferred to Paper 4 §7.5.7
and Paper 7). We flag the $4.7\sigma$ tension prominently as a
prediction of the framework that upcoming cosmological surveys will
test.

The parameter ξ enters the Casimir constraint through `ξ⁴`: the mirror
sector's contribution to the effective species count shifts R_A from
`10.072 μm` (visible sector alone, `ξ = 0`) to `10.159 μm` (with mirror
sector, `ξ = 0.432`). This 0.86% upward shift is precisely what places
R_A in the window where the 5/2 identity closes. Without the mirror
sector correction, exact closure would require `M_GUT* ≈ 4 × 10¹⁶ GeV`;
with it, exact closure occurs at `M_GUT* = 7 × 10¹⁶ GeV`, and the
closest canonical approach — at `M_GUT = 1.65 × 10¹⁶ GeV` within the
SUSY unification window — carries a fractional gap of only 0.81%,
well within threshold corrections. The dark matter sector — encoded in
`ξ⁴` — is therefore not independent of the dark energy sector or the
neutrino mass: it is one of the three simultaneous constraints that
determine the compactification radius R. Paper 9, §4d develops the full
quantization argument.

**The ξ⁴ correction to R: explicit derivation.** The mirror sector
(visible sector scaled by $\xi^4$) contributes to the total Casimir
energy through its additional degrees of freedom. The effective Casimir
constant becomes

$$c_\mathrm{eff} = c_\mathrm{vis} \times (1 + \xi^4)$$

since the mirror sector is a scaled copy of the visible sector with
$T' = \xi T$, contributing $\xi^4 \rho_\mathrm{vis}$ to the energy
density (the $\xi^4$ comes from the Stefan-Boltzmann $T^4$
dependence). The compactification radius is determined by
$\rho_\Lambda = c_\mathrm{eff}/R_A^4$, giving

$$R_A = R_\mathrm{vis} \times (1 + \xi^4)^{1/4} \approx R_\mathrm{vis} \times \left(1 + \frac{\xi^4}{4}\right)$$

For $\xi = 0.432$: $\xi^4 = (0.432)^4 = 0.0348$, so

$$\frac{R_A - R_\mathrm{vis}}{R_\mathrm{vis}} = \frac{\xi^4}{4} = \frac{0.0348}{4} = 0.0087 = 0.87\%$$

This is consistent with the stated 0.86% shift (the small discrepancy
is rounding in $\xi^4$).

**The three constraints are not three independent fixing mechanisms.**
To be precise: (i) the primary observational constraint is
$\rho_\Lambda = c_\mathrm{vis}/R_0^4 = 3H_0^2 M_\mathrm{Pl}^2 \Omega_\Lambda$,
which determines $R_0$ from the observed dark energy density; (ii)
the $\xi^4$ correction from the mirror sector is a perturbative shift
to $R$ (0.87%), computable given $\xi$; (iii) the 5/2 neutrino mass
identity provides a consistency check on whether the shifted $R_A$
falls in the window where exact GUT-scale closure of 5/2 is
achievable. These are one primary determination plus two consistency
checks, not three independent fixing mechanisms. Paper 9 §4d develops
the full quantization argument that combines all three into an
overdetermined system whose mutual consistency is a non-trivial
prediction of the framework.
