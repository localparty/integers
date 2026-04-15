# 1. Introduction: One Field, One History

Papers 1–4 of this series derive the laws of physics from the
geometry of an 11-dimensional spacetime `M⁴ × CP² × S² × S¹/Z₂`.
Paper 1 establishes quantum mechanics, gravity, and electromagnetism
from the e-circle `S¹`. Paper 2 derives the cosmological observables
from the orbifold dark sector. Paper 3 resolves the black hole
information paradox and the problem of time. Paper 4 derives the
Standard Model gauge group, the Higgs mechanism, and twenty-one
quantitative predictions — including the cosmological constant.

What no single paper provides is the **temporal narrative**: how
the universe evolves, epoch by epoch, from the initial quantum
fluctuation to the distant future, all driven by one geometric
object.

This paper fills that gap.

---

## 1.M Methodology: The Framework's Reasoning Patterns

This paper is one of seven in a series. Each paper applies the same
small set of reasoning patterns to a different domain of physics.
The patterns are documented in full in `readme.md`; the relevant ones
for this paper are identified below. Understanding which pattern a
derivation uses lets you see *why* the result works, not just *that*
it works — and lets you apply the same move to new problems.

The six patterns of the framework:

| # | Name | Core move |
|---|------|-----------|
| 1 | **Geometric Reinterpretation** | A 4D mystery is a shadow of simpler 5D geometry |
| 2 | **Holonomy Correspondence** | Wilson line VEV around a compact dimension → gauge phase |
| 3 | **Casimir as Scale-Setter** | Quantum vacuum energy on a compact space → a fundamental scale |
| 4 | **Topological Rigidity** | Discrete invariant (winding number, χ, homotopy) → exact quantized result |
| 5 | **Zeta Regularization of KK Towers** | Compact → discrete KK sum → analytic continuation → finite result |
| 6 | **Projection Produces Apparent Pathology** | 4D looks broken because 4D is a partial trace over the geometry |

**Primary patterns in this paper:**

- **Pattern 3** drives the entire thermal history: the dilaton
  potential V(φ) = V₀/φ⁴ is the Casimir energy of bulk fields on S¹.
  This one function — one compact dimension, one mechanism — produces
  inflation (from the G₄ axion hilltop), reheating, matter domination,
  and dark energy, in a single unbroken narrative.

- **Pattern 4** gives w₀ = −1 exactly: Theorem K.1 (Epstein zeros)
  forces all perturbative corrections to V(φ) to vanish. The dilaton
  potential is exact, and the equation of state is locked. No slow
  roll, no reconstruction — the equation of state is topologically
  rigid.

- **Pattern 1** frames the inflaton identification: the G₄ axion
  looked like a separate degree of freedom in 4D effective field
  theory. In 5D it is the phase of the GVW superpotential — a
  geometric object whose hilltop potential follows from the
  sub-Planckian decay constant f = M_Pl/√3.


---

## 1.1 The Central Object

The dilaton `φ(t)` measures the e-circle radius at cosmic time `t`:

    R(t) = R₀ × φ(t)

where `R₀ ≈ 10 μm` is the stabilized radius (Paper 1, Appendix W;
Paper 4, §7.21). The dilaton evolves in the potential:

    V(φ) = V₀/φ⁴

derived from the Casimir energy of bulk fields. This potential is
exact to all perturbative orders (the 2-loop and higher corrections
vanish from the Epstein zeta zeros — the same mechanism that gives
UV finiteness; see Paper 4 §7.21.10 and `etc/09`). No Goldberger-
Wise term exists at the perturbative level.

The dilaton is frozen at its post-inflationary value by Hubble friction.
The dimensionless fractional drift per Hubble time is ΔR/R₀ ~ H₀R₀ ~
3 × 10⁻³⁰ (Appendix A, Proposition A.1), giving w = −1 to precision
(ΔR/R₀)² ~ 10⁻⁵⁹. The dilaton is not the inflaton (ε = 32/3 ≫ 1;
§3.1). The G₄ flux axion drives inflation (Paper 7). The dilaton's
current value sets the cosmological constant: ρ_Λ = c/R₀⁴.

## 1.2 The Two Dynamical Regimes

The dilaton potential V(R) = +c/R⁴ has no minimum. The relevant
epochs map onto two regimes:

| Regime | Dilaton state | Epoch |
|---|---|---|
| Frozen by Hubble friction | R ≈ R₀, ΔR/R₀ ~ 3×10⁻³⁰/Hubble time | All epochs from inflation to today and beyond |
| Inflaton oscillation | G₄ axion oscillates around its own minimum | Reheating → leptogenesis |

Every epoch of cosmic history maps onto a segment of this picture.
The dilaton itself does not oscillate or roll in the revised framework
— it is frozen. The inflaton (G₄ axion) oscillates during reheating;
the dilaton is a bystander that happens to set the cosmological
constant through its frozen Casimir energy.

## 1.3 What Is New in This Paper

This paper presents no new formalism. It presents the complete
timeline — assembling results from Papers 1–4 into a single
chronological narrative, and computing four quantities that require
the temporal context:

1. The reheating temperature (§4)
2. The non-thermal leptogenesis pathway (§5)
3. The origin of the brane temperature asymmetry ξ (§6)
4. The far future of the dilaton (§11)
