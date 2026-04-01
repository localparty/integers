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

## Y.4 What the Framework DOES Address

While the dilaton doesn't solve the Hubble tension through EDE, the
framework does make specific predictions for cosmological parameters
that bear on the tension:

- **N_eff:** The dilaton contributes ΔN_eff ~ 0.57 (Appendix Q), which
  would INCREASE H₀ from the CMB by ~0.5 km/s/Mpc — in the right
  direction but far too small to close the 6 km/s/Mpc gap. (Note: this
  prediction is in tension with ACT+SPT data.)

- **Dark energy equation of state:** The thawing dilaton gives w ≈ −0.8
  at late times (consistent with DESI), which modifies the late-time
  expansion history and shifts H₀ by ~1 km/s/Mpc — again in the right
  direction but insufficient.

- **Casimir dark energy:** The predicted Casimir energy density matches
  the observed ρ_Λ by construction. The framework does not produce a
  DIFFERENT ρ_Λ that would resolve the tension.

## Y.5 Summary

| Aspect | Status |
|--------|--------|
| Dilaton as late-time dark energy | ✓ (Casimir, Section 6.6) |
| Dilaton as thawing quintessence (DESI) | Plausible (document 13) |
| Dilaton as early dark energy (Hubble tension) | **Not viable** (mass mismatch by 10²⁷) |
| ΔN_eff contribution | Right direction, too small |
| Second modulus as EDE | Speculative (requires Appendix L extension) |

The Hubble tension remains an open problem for the framework. The e-circle
dilaton is the wrong mass for EDE. A resolution may require the non-abelian
extension (additional compact dimensions with lighter moduli) or a
non-cosmological explanation of the tension.

## Y.6 References

- Riess, A. G. et al. "A Comprehensive Measurement of the Local Value of
  the Hubble Constant." *Astrophys. J.* 934, L7 (2022).
- Planck Collaboration. "Planck 2018 results. VI." *A&A* 641, A6 (2020).
- Poulin, V. et al. "Early Dark Energy Can Resolve the Hubble Tension."
  *Phys. Rev. Lett.* 122, 221301 (2019).
- Agrawal, P., Obied, G. & Vafa, C. "H₀ Tension, Swampland Conjectures,
  and the Epoch of Fading Dark Matter." arXiv:1906.08261 (2019).
