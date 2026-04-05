# 3. Inflation

## 3.1 The Inflaton Is Not the Radion

**⚠ Revised (see `etc/09-creative-routes-to-R.md`, Idea 6).**

The original version of this section identified the dilaton (the
e-circle radius `R`) as the inflaton, with the Casimir potential
`V = V₀/φ⁴` providing a slow-roll plateau. This identification
is incorrect.

The canonical kinetic term for the radion `R` from the 5D KK
reduction is:

    L_kin = (3M_Pl²)/(4R²) (∂R)²

Defining the canonical field `σ = (√3 M_Pl/2) ln(R/R₀)`:

    V(σ) = C R₀⁻⁴ exp(−8σ/(√3 M_Pl))

This is an EXPONENTIAL potential in the canonical field. The
slow-roll parameter:

    ε = (M_Pl²/2)(V'/V)² = (M_Pl²/2)(8/(√3 M_Pl))² = 32/3 ≈ 10.7

**ε = 10.7 ≫ 1.** The Casimir potential `V = C/R⁴` is far too
steep in the canonical field for slow-roll inflation. The dilaton
cannot be the inflaton.

The confusion arose because `V ∝ 1/φ⁴` LOOKS like a power-law
potential in the non-canonical field `φ`. A `1/φ⁴` potential with
canonical kinetic term gives `ε = 8/φ² ≈ 1/60` for `φ ~ 20 M_Pl`,
which supports inflation. But the radion's kinetic term is
non-canonical — and the canonical field transformation converts
the power law into an exponential, destroying the flatness.

## 3.2 The Candidate Inflatons

If the radion does not drive inflation, what does? The framework
has two other moduli with their own potentials:

**The S² radius `r₂`:** The Casimir potential on `S²` has a
different structure than on `S¹` — the eigenvalues `l(l+1)` are
shifted squares, and the spectral zeta values `Z_{S²}(−j)` are
nonzero (§2.3; Paper 4, Appendix C). The canonical field and
slow-roll parameters for `r₂` depend on the kinetic term from the
6D (M⁴ × S²) KK reduction, which differs from the 5D radion case.

**The CP² Kähler modulus `r₃`:** Similarly, the Casimir potential
on `CP²` involves the spectral zeta `Z_{CP²}(−j)` and a kinetic
term from the 8D (M⁴ × CP²) reduction.

The key question: do either of these moduli have a canonical
potential flat enough for slow-roll? This requires computing the
canonical kinetic terms from the full 11D → 4D reduction on
`CP² × S² × S¹` — a specific calculation that has not yet been
performed.

## 3.3 What the Inflationary Predictions Depend On

**⚠ The predictions `n_s ≈ 0.965` and `r ≈ 0.03` from Paper 4
§7.15 assumed the radion was the inflaton.** These predictions are
suspended pending identification of the correct inflaton field.

If the inflaton turns out to be the `CP²` or `S²` modulus, the
predictions will change — the slow-roll parameters depend on the
shape of the Casimir potential in the canonical field for that
modulus, which involves the spectral zeta values computed in
Paper 4, Appendix C.

The qualitative features may survive:
- The Casimir energy of bulk fields on a compact space generically
  provides a potential
- The potential is calculable (no free parameters beyond the field
  content and geometry)
- The prediction for `n_s` and `r` will be specific numbers from
  the spectral data

But the specific values `n_s = 0.965` and `r = 0.03` should not
be cited until the inflaton is identified and the canonical
potential is computed.

## 3.4 What Remains Established

Despite the inflaton identification being open, the following are
unaffected:

- **The Casimir potential `V = −c/R⁴` is exact** to all
  perturbative orders (Epstein zeta zeros, Paper 1 Appendix G)
- **`w₀ = −1`** to `10⁻⁵²` precision (frozen dilaton)
- **`R` is set by initial conditions** from the inflationary/
  compactification era, not by dynamical stabilization
- **The dark energy density `ρ_Λ = ΔN × 3ζ(5)/(64π⁶R⁴)`** is
  a true cosmological constant
- **The S² and CP² moduli are dynamically stabilized** by their
  nonvanishing spectral zeta values (Paper 4, §9.1, Appendix C)

The open question is: which modulus drove inflation, and what are
its slow-roll parameters? This is identified as the primary open
problem for the inflationary sector.
