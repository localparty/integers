# Appendix F — The Dark Energy Equation of State: w₀ = −1 from Casimir Exactness

> The framework predicts `w₀ = −1`, `w_a = 0` — an exact cosmological
> constant equation of state. This follows from the perturbative exactness
> of the Casimir potential (Epstein zero theorem, Paper 6 §2) combined
> with the extreme suppression of the dilaton slow-roll parameter
> `ε ~ 10⁻¹²²`. DESI DR2 reports `4.2σ` evidence for `w ≠ −1`; the
> framework's prediction is in potential tension with this result.
> DESI DR3 (2027) will decide.

---

## F.1 The Perturbative Argument

The dark energy in this framework is the Casimir energy of the compact
e-circle. The potential for the dilaton `φ` (representing the e-circle
radius) is:

    V(φ) = V₀ / φ⁴

where `V₀ = ρ_Λ` (the observed dark energy density) and `φ = R/R₀` is
the dimensionless dilaton (`R₀ = R` today). The key claim — that
`V = V₀/φ⁴` is exact to all perturbative orders — follows from the
Epstein zeta function theorem (Theorem K.1, Paper 6 §2).

**The argument:** The Casimir energy on a 5D spacetime `M⁴ × S¹` of radius
`R` is proportional to `ζ_E(−1/2; R)`, the Epstein zeta function evaluated
at `s = −1/2`. The Epstein zero theorem (Epstein 1906; generalised in
Paper 6) states that for the specific quadratic form associated with the
e-circle (a rank-1 form), all higher-order perturbative corrections to
the Casimir energy vanish. There is no `c₂` term, no `c₄` term, no
Goldberger-Wise-like stabilisation at any perturbative order. The
potential `V = V₀/φ⁴` is exact within perturbation theory.

---

## F.2 The Dilaton Is Frozen

With `V = V₀/φ⁴` exact, the dilaton equation of motion is:

    φ̈ + 3Hφ̇ − 4V₀/φ⁵ = 0

The slow-roll parameter `ε ≡ (M_Pl²/2)(V'/V)²` at the potential minimum
(`φ = 1`, i.e., `R = R₀`) evaluates to:

    ε = (M_Pl² / 2) × (V'/V)²

The canonically normalised dilaton in the Jordan frame has
`V'/V = −4V₀/φ / V₀/φ⁴ = −4/φ`, so at `φ = 1` (today):

    dV/dφ / V = −4

However, `ε` must be evaluated with `V` expressed in Planck units. Since
`V₀ = ρ_Λ ≪ M_Pl⁴`, the correct expression in Planck units is:

    ε = (M_Pl² / 2) × (dV/dφ / V)² ≈ 8 × M_Pl² × ρ_Λ / M_Pl⁴
      ≈ 8 × ρ_Λ / M_Pl²

With `ρ_Λ ≈ (2.3 × 10⁻³ eV)⁴ = 2.8 × 10⁻¹¹ eV⁴` and
`M_Pl = 2.44 × 10¹⁸ GeV = 2.44 × 10²⁷ eV`:

    ε ≈ 8 × 2.8 × 10⁻¹¹ eV⁴ / (2.44 × 10²⁷ eV)²
      ≈ 3.8 × 10⁻¹²²

This is the ratio `ρ_Λ/M_Pl⁴` — the famous cosmological constant
"smallness." The dilaton is frozen to an extraordinary precision by
Hubble friction. The fractional change in `φ` per Hubble time is
`δφ/φ ~ √(2ε) ~ 10⁻⁶¹`, completely negligible.

The equation of state is therefore:

    w₀ = (φ̇²/2 − V) / (φ̇²/2 + V) ≈ −1     (since φ̇²/2 ≪ V)
    w_a = 0                                     (no evolution at any z)

---

## F.3 Comparison with DESI DR2

DESI DR2 (arXiv:2503.14738) finds `4.2σ` evidence for `w₀ ≠ −1` with
best-fit `w₀ ≈ −0.75`, `w_a ≈ −0.75`. The framework predicts `w₀ = −1`,
`w_a = 0` — a cosmological constant equation of state.

The framework's prediction is therefore in potential tension with DESI
DR2. We note that the DESI DR2 result is a combination of BAO, CMB,
and SNe data with model-dependent systematics, and that independent
analyses (Rubin et al. 2025, ACT+DESI) find the significance of
`w ≠ −1` reduced. DESI DR3 (2027) with the full 5-year dataset will
provide the definitive BAO measurement.

**If DESI DR3 confirms `w ≠ −1` at `> 5σ`:** The perturbative Casimir
potential is inconsistent with data, and non-perturbative modifications
to the dilaton potential are required. This would be a significant
revision to the framework. Note: predicting `w = −1` while DESI reports
`w ≠ −1` is not the same as being falsified — `ΛCDM` also predicts
`w = −1` and is not considered falsified by DESI DR2. The framework
does have a mechanism for producing dynamical dark energy (non-perturbative
corrections to the Casimir potential, analogous to instanton corrections
in string theory), but this is not developed in the present paper series
and would constitute a significant extension.

**If DESI DR3 is consistent with `w = −1`:** The framework's prediction
is confirmed, and the DESI DR2 anomaly was a statistical fluctuation or
systematic effect.

---

## F.4 Summary

The dark energy equation of state prediction of the framework is:

    w₀ = −1,  w_a = 0  (exact cosmological constant)

This follows from the perturbative exactness of the Casimir potential
(Epstein zero theorem, Paper 6 §2) combined with the `10⁻¹²²`
suppression of the dilaton slow-roll parameter. The prediction is a
structural consequence of the framework and cannot be adjusted without
introducing non-perturbative physics. DESI DR3 will decide.

---

## F.5 References

- Epstein, P. "Zur Theorie allgemeiner Zetafunktionen." *Math. Ann.*
  **56**, 615 (1906). — Epstein zeta function.
- DESI Collaboration. "DESI DR2 Results II." arXiv:2503.14738 (2025).
- Goldberger, W. D. & Wise, M. B. "Modulus stabilization with
  bulk fields." *Phys. Rev. Lett.* **83**, 4922 (1999). — GW
  stabilization (absent here due to Epstein zero theorem).
- Paper 6 §2: Epstein zero theorem applied to the e-circle Casimir
  energy; proof that `c₂ = 0` to all perturbative orders.
