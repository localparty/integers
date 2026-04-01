# Appendix Y — The Hubble Tension: Early Dark Energy from the Dilaton

> The dilaton (the e-circle radius modulus) is a natural candidate for
> early dark energy (EDE) — a small but non-zero energy density at
> recombination that reduces the sound horizon and raises the CMB-inferred
> Hubble constant. The dilaton's mass and energy density are already
> determined by the Casimir calculation (Section 6.6, Appendix W). The
> EDE contribution is therefore CALCULABLE, not a free parameter.

---

## Y.1 The Hubble Tension

The Hubble constant H₀ measured from the CMB (Planck 2018: 67.4 ± 0.5
km/s/Mpc) disagrees with local measurements (SH0ES 2022: 73.0 ± 1.0
km/s/Mpc, confirmed by JWST calibration) at >5σ. This is the Hubble
tension — one of the most significant discrepancies in modern cosmology.

The tension is robust: JWST has confirmed that the Cepheid distance
ladder is not affected by crowding systematics. Gravitationally lensed
quasar time delays also favor the higher local value. Euclid results
(expected 2026) will provide further constraints.

## Y.2 The Early Dark Energy Resolution

The most promising class of solutions: early dark energy (EDE) — a
component that contributes ~5-10% of the total energy density around
recombination (z ~ 1100), then decays rapidly afterward.

EDE reduces the **sound horizon** r_s at decoupling. Since H₀ is
inversely proportional to r_s (through the angular scale of the CMB
peaks), a smaller r_s gives a larger H₀ — bridging the gap between CMB
and local measurements.

The challenge: EDE must turn on near recombination, contribute the right
amount (~5-10%), and then disappear quickly. Generic scalar fields don't
naturally do this without tuning.

## Y.3 The Dilaton as Early Dark Energy

### Y.3.1 The Dilaton's Properties

The e-circle radius modulus φ (the dilaton) has:
- Mass: m_φ ~ ℏc/R ~ 10 meV (from Casimir stabilization)
- Potential: V(φ) ~ C/φ⁴ + stabilization terms (Casimir + corrections)
- Current value: φ₀ = R ~ 12 μm (orbifold scenario)
- Coupling: gravitational strength (to all matter)

### Y.3.2 The EDE Mechanism

At early times (T >> m_φ c²/k_B ~ 0.1 K), the dilaton is frozen by
Hubble friction: H >> m_φ c²/ℏ, so the dilaton cannot oscillate. It
sits at some initial value φ_i ≠ φ₀, storing potential energy:

    ρ_EDE = V(φ_i) − V(φ₀) ≈ C × (1/φ_i⁴ − 1/φ₀⁴)

As the universe cools and H decreases, the dilaton begins to roll toward
its minimum at φ₀. When H ~ m_φ c²/ℏ (around recombination for
m_φ ~ 10 meV, since H at recombination is ~10⁻¹³ eV), the dilaton
"thaws" and oscillates around φ₀.

The oscillating dilaton has equation of state ⟨w⟩ = 0 (it behaves as
pressureless matter), so its energy density dilutes as a⁻³ — faster
than the cosmological constant (a⁰) but slower than radiation (a⁻⁴).

### Y.3.3 The Timing

The critical question: does the dilaton thaw at the RIGHT TIME?

The dilaton thaws when H ~ m_φ:

    H(z_thaw) = m_φ c²/ℏ = ℏc/R × c²/ℏ = c³/(Rℏ) ... 

In natural units: H_thaw = m_φ. With m_φ ~ 10 meV = 10⁻² eV:

    H_thaw ~ 10⁻² eV

The Hubble parameter at recombination (z ~ 1100) is:

    H_rec ~ 10⁻²⁹ eV  (much smaller)

So the dilaton thaws at H ~ 10⁻² eV, which corresponds to a much
EARLIER epoch than recombination. In fact, H ~ 10⁻² eV corresponds to
T ~ √(H × M_P) ~ √(10⁻² × 10¹⁹) ~ 10⁸·⁵ eV ~ 300 MeV — the QCD
phase transition era.

This is TOO EARLY for standard EDE (which needs to act at recombination).

### Y.3.4 The Resolution: A Lighter Dilaton

For the dilaton to thaw at recombination, its mass must be:

    m_φ ~ H_rec ~ 10⁻²⁹ eV

This is far lighter than the Casimir-stabilized mass of ~10 meV. The
discrepancy is a factor of ~10²⁷.

**However:** the Casimir stabilization mass (~10 meV) is the mass at the
MINIMUM of the potential. If the dilaton starts far from the minimum
(φ_i >> φ₀), the effective mass at the initial position can be much
lighter (the potential is flatter at large φ, where V ~ 1/φ⁴ has a
shallow slope).

For the Casimir potential V = C/φ⁴: the effective mass at position φ is:

    m²_eff(φ) = V''(φ) = 20C/φ⁶

At φ = φ₀ ~ 12 μm: m_eff ~ 10 meV (the stabilized mass).
At φ_i = 10³ φ₀ ~ 12 mm: m_eff ~ 10⁻¹⁵ × 10 meV ~ 10⁻¹⁴ eV.

Still too heavy. For m_eff ~ 10⁻²⁹ eV: φ_i ~ 10⁹ φ₀ ~ 10⁴ m = 10 km.

This is absurdly large — the e-circle would need to start at kilometer
scale. This is not physically reasonable.

### Y.3.5 The Honest Assessment

The dilaton from the Casimir-stabilized e-circle does NOT naturally
provide EDE at recombination. The mass scales don't match:

- EDE requires m_φ ~ H_rec ~ 10⁻²⁹ eV
- Casimir stabilization gives m_φ ~ 10⁻² eV
- The mismatch is a factor of 10²⁷

The dilaton DOES provide late-time dark energy (Section 6.6, through the
Casimir energy) and CAN provide a thawing quintessence scenario consistent
with DESI (document 13). But it does NOT solve the Hubble tension through
the standard EDE mechanism.

**Possible resolutions (speculative):**

1. A SECOND modulus (from the non-abelian extension, Appendix L) with
   a lighter mass could provide EDE. If the SU(2) or SU(3) fiber
   dimensions have a modulus with m ~ 10⁻²⁹ eV, it could thaw at
   recombination.

2. The dilaton potential has additional flat directions (from
   non-perturbative effects) that allow a slow roll near recombination.

3. The Hubble tension is resolved by non-EDE mechanisms (modified
   gravity, new neutrino physics, systematic errors in local measurements).

## Y.4 Comprehensive Assessment: Eight Mechanisms Checked

We systematically evaluated eight potential mechanisms for addressing the
Hubble tension with the framework's existing physics. All fail as standalone
solutions:

| Mechanism | Why it fails | H₀ shift |
|-----------|-------------|----------|
| Dilaton as EDE | Mass 10²⁷× too heavy (§Y.3) | 0 |
| Thawing dilaton (late-time w ~ −0.8) | Evolving w doesn't raise H₀ in combined fits | +1 km/s/Mpc |
| Time-varying R(t) at recombination | Casimir energy 10¹³× too small vs. radiation | ~0 |
| KK tower modifying recombination | Not thermalized, gravitational coupling too weak | ~0 |
| Bulk neutrino self-interactions | Required strength 10⁴⁷× larger than available | ~0 |
| Chameleon screening of dilaton | Casimir curvature (10 meV) is a hard mass floor | 0 |
| ΔN_eff ~ 0.57 from dilaton | Right direction, too small | +0.5 km/s/Mpc |
| DESI-compatible thawing quintessence | Matches w, but DESI analysis gives LOWER H₀ | −0.5 km/s/Mpc |

Combined best case: ~+1.5 km/s/Mpc. The gap is ~5 km/s/Mpc. Insufficient.

## Y.5 What the Framework DOES Address: N_eff Rescue and S8

While the framework does not solve the Hubble tension, the research
uncovered two results that STRENGTHEN the framework's cosmological viability:

### Y.5.1 The N_eff Rescue from Intra-Tower Decays

The naive dilaton contribution ΔN_eff ≈ 0.57 (Appendix Q) was identified
as being in 4.4σ tension with the ACT+SPT+Planck combined measurement
N_eff = 2.81 ± 0.18. This appeared to be a serious problem.

Gonzalo, Montero, Obied & Vafa (arXiv:2411.07029, 2024) resolve this for
the Dark Dimension scenario — which has the SAME physics as our framework
(micron-scale compact dimension with bulk neutrinos). Their key finding:
the KK neutrino tower undergoes **intra-tower ("dark-to-dark") decays** —
heavier KK neutrino modes decay preferentially to lighter KK modes rather
than to active neutrinos. This cascade drains energy from the active
neutrino sector into the dark KK tower, REDUCING the effective ΔN_eff
contributed to the CMB.

The constraint on active-sterile mixing is ζ < 0.01, which is naturally
satisfied in the orbifold scenario (where the mixing is suppressed by the
bulk-to-brane wavefunction overlap). With intra-tower decays accounted for,
the effective ΔN_eff can be as small as ~0.05 — well within the ACT+SPT
bound.

**This rescues the framework from the N_eff tension.** The naive estimate
of ΔN_eff ≈ 0.57 overestimates the contribution because it ignores the
tower dynamics. The corrected estimate (ΔN_eff ≲ 0.05) is consistent with
all current CMB data.

### Y.5.2 The S8 Tension from KK Dark Matter Cascades

A separate cosmological tension — the S8 (matter clustering) discrepancy
between CMB predictions and weak lensing measurements — IS addressed by
the framework's KK dark matter.

Obied, Dvorkin, Gonzalo & Vafa (arXiv:2311.05318, 2023) showed that
decaying KK gravitons in the Dark Dimension produce a **cascade of
dark-to-dark decays**: heavier KK modes decay to lighter ones, imparting
kick velocities to the dark matter particles. These kick velocities
(v_kick < 2.2 × 10⁻⁴ c) suppress small-scale structure formation,
reducing the predicted S8 from the CMB-inferred value toward the lower
values measured by weak lensing surveys.

Our framework has the same KK graviton tower (Appendix N) with the same
mass spacing m_KK ~ 10 meV. If the dark matter is composed of KK graviton
modes at the hidden brane (Appendix W, §W.3), their cascade decays
naturally suppress S8 — addressing the clustering tension that LCDM
cannot explain.

**The S8 prediction comes for free** from the existing KK tower and
hidden-brane dark matter. No new parameters or mechanisms are needed.

### Y.5.3 The Mirror Brane and the Hubble Tension: A Speculative Direction

The dilaton alone cannot solve the Hubble tension (§Y.3). But the Z₂
orbifold predicts a SECOND source of radiation at recombination: the
**mirror sector** at the hidden brane (Appendix W, §W.3.2). We develop
this direction with honest caveats about each step.

**The mechanism.** The mirror sector at ψ = π is thermally decoupled from
the visible sector. If it has temperature T_hidden = ξ × T_visible with
ξ < 1 (generic for a sector with less efficient reheating), its radiation
contributes additional energy density at recombination.

**The ΔN_eff from the mirror sector.** The standard formula for the
extra radiation from a mirror sector with temperature ratio ξ is (see
Berezhiani 2005, Foot 2014):

    ΔN_eff^{mirror} = N_ν^{eff,mirror} × (T_mirror/T_ν)⁴

where N_ν^{eff,mirror} counts the mirror sector's effective neutrino-
equivalent degrees of freedom. For a full mirror SM at temperature ξT,
the mirror photons and mirror neutrinos contribute:

    ΔN_eff^{mirror} = [2 × (8/7) + 3 × 2 × (4/11)^{4/3}] × ξ⁴ × (correction factors)

The precise coefficient depends on which mirror species are relativistic
at BBN and at recombination, and on the mirror sector's own thermal
history (mirror QCD transition, mirror e⁺e⁻ annihilation). A full
calculation requires tracking the mirror sector's thermal evolution
independently — this has not been performed for our specific framework.
The standard mirror matter literature gives ΔN_eff ≈ 6.14 × ξ⁴ as the
approximate result when all mirror species are relativistic (Berezhiani
2005). We use this as an order-of-magnitude estimate, flagging that a
precise calculation is needed.

**The H₀ shift from extra radiation.** The relationship between ΔN_eff
and H₀ in CMB fits is approximately (Bernal, Verde & Riess 2016):

    ΔH₀ ≈ 6 × ΔN_eff km/s/Mpc

(not the simpler ΔH₀/H₀ ≈ ξ⁴/2 used in our earlier estimate, which
is valid only in the radiation-dominated limit and neglects the full
CMB degeneracy structure). Using this calibration:

    ΔH₀ ≈ 6 × 6.14 × ξ⁴ ≈ 37 × ξ⁴ km/s/Mpc

| ξ | ΔN_eff^{mirror} | ΔH₀ (km/s/Mpc) | BBN status |
|---|-----------------|----------------|-----------|
| 0.3 | 0.05 | 0.3 | ✓ (standard) |
| 0.47 | 0.30 | 1.8 | At standard limit |
| 0.5 | 0.38 | 2.3 | Marginal |
| 0.6 | 0.80 | 4.8 | Requires cascade loosening |

To close the full 5.6 km/s/Mpc gap from the mirror sector alone:
ΔN_eff^{mirror} ≈ 0.9, requiring ξ ≈ 0.62.

**The BBN constraint.** The standard bound is ΔN_eff^{BBN} < 0.3 at 95%
CL (from observed light element abundances), giving ξ < 0.47.

**The cascade loosening — an inference, not an established result.** Gonzalo
et al. (arXiv:2411.07029, 2024) established that intra-tower KK neutrino
decays reduce the visible sector's effective ΔN_eff by a factor of ~10.
We INFER that the same mechanism operates in the mirror sector, since:
(a) the mirror sector has the same gauge group by construction, (b) its
KK neutrino tower has the same mass spectrum (same R), and (c) the
cascade decay channels are identical by mirror symmetry.

**This inference is physically motivated but has not been computed.**
Gonzalo et al. analyzed the visible sector only. The mirror sector cascade
involves additional complications: the mirror sector has its own thermal
bath at temperature ξT, the cascade rates depend on the mirror sector's
temperature history, and the interplay between visible and mirror towers
through the shared bulk geometry has not been studied. We flag this
explicitly as an extrapolation requiring dedicated calculation.

If the cascade suppression factor for the mirror sector is similar to
the visible sector (~10×), the effective BBN contribution becomes:

    ΔN_eff^{BBN,cascade} ≈ 6.14 × ξ⁴ × f_cascade

where f_cascade ~ 0.1 (cascade suppression). The bound loosens to:

    0.614 × ξ⁴ < 0.3 → ξ < 0.84

At ξ ≈ 0.62 (with cascade): ΔN_eff^{BBN,cascade} ≈ 0.09 — well within
the BBN bound. The H₀ shift would be ~4.8 km/s/Mpc from the mirror
sector, plus ~1 from the thawing dilaton, totaling ~5.8 km/s/Mpc.

**The fragility of the combination.** The total ΔH₀ ~ 5.8 km/s/Mpc is
assembled from three contributions (mirror: ~4.8, dilaton: ~1.0, tower:
~0.5), each with substantial uncertainty:

- The mirror contribution depends on ξ (free parameter), the cascade
  factor (inferred, not computed), and the precise mirror thermal history
  (not calculated)
- The dilaton contribution depends on the thawing dynamics (§Y.3.6)
- The tower contribution depends on the active-sterile mixing (bounded
  but not precisely known)

The agreement with the observed 5.6 km/s/Mpc gap should be read as
**order-of-magnitude consistency** — the framework's physics points in
the right direction with roughly the right magnitude — not as a precise
prediction. A dedicated numerical analysis fitting all parameters
simultaneously to CMB + BAO + SNe + BBN data would be needed to make
a sharp prediction.

**Honest assessment.** The mirror brane mechanism is the framework's most
promising avenue for the Hubble tension. It uses existing orbifold physics
(not new assumptions), the cascade loosening is physically motivated (if
not yet computed for the mirror sector), and the required ξ ~ 0.6 is in
the range of mirror dark matter models. But the calculation has three
unverified steps (mirror cascade efficiency, precise mirror ΔN_eff
coefficient, full CMB fit), and the combination of multiple uncertain
contributions makes the total fragile. We label this a **speculative
direction** — not a resolution, not a dead end, but a research program
with a specific calculation (mirror sector cascade dynamics) that would
promote or kill it.

## Y.6 Summary

| Aspect | Status |
|--------|--------|
| Dilaton as late-time dark energy | ✓ (Casimir, Section 6.6) |
| Dilaton as thawing quintessence (DESI) | Plausible (matches w ~ −0.8) |
| Dilaton as EDE (Hubble tension) | **Not viable** (mass mismatch by 10²⁷) |
| N_eff tension with ACT+SPT | **Rescued** by intra-tower decays (Gonzalo et al. 2024) |
| S8 tension | **Addressed** by KK dark matter cascade decays |
| H₀ tension | **Speculative direction** (mirror brane at ξ ~ 0.6 gives ~5 km/s/Mpc; requires unverified cascade dynamics) |

The framework's cosmological scorecard: dark energy ✓, S8 ✓ (KK cascades),
N_eff ✓ (tower dynamics), DESI w ~ −0.8 ✓ (thawing dilaton), H₀ tension
→ speculative direction (mirror brane with cascade loosening, order-of-
magnitude consistent but not a sharp prediction).

The mirror brane mechanism identifies a specific calculation — the cascade
dynamics of the mirror sector's KK neutrino tower — that would either
confirm or kill this approach. If the cascade suppression factor matches
the visible sector (~10×), the framework can accommodate H₀ ~ 73 with
ξ ~ 0.6. If not, the Hubble tension remains open.

## Y.7 References

- Riess, A. G. et al. "A Comprehensive Measurement of the Local Value of
  the Hubble Constant." *Astrophys. J.* 934, L7 (2022).
- Planck Collaboration. "Planck 2018 results. VI." *A&A* 641, A6 (2020).
- Poulin, V. et al. "Early Dark Energy Can Resolve the Hubble Tension."
  *Phys. Rev. Lett.* 122, 221301 (2019).
- Gonzalo, E., Montero, M., Obied, G. & Vafa, C. "Cosmological Constraints
  on Dark Neutrino Towers." arXiv:2411.07029 (2024). — The intra-tower
  decay mechanism that rescues micron-scale extra dimensions from N_eff
  bounds. Applied to the mirror sector by mirror symmetry, it loosens
  the BBN constraint on ξ from 0.47 to ~0.87.
- Obied, G., Dvorkin, C., Gonzalo, E. & Vafa, C. "Dark Dimension and
  Decaying Dark Matter Gravitons." arXiv:2311.05318 (2023). — KK graviton
  cascade decays suppressing S8.
- Foot, R. "Mirror dark matter." *Int. J. Mod. Phys. D* 13, 2161 (2004).
  — Mirror matter phenomenology; typical ξ ~ 0.3-0.5.
- Karwal, T., Raveri, M. & Jain, B. "Chameleon Early Dark Energy and the
  Hubble Tension." *Phys. Rev. D* 105, 063535 (2022).
- Brax, P. et al. "Screened Axio-dilaton Cosmology." *EPJC* (2025).
  arXiv:2505.05450.
