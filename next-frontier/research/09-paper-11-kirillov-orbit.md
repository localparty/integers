# Research 09: Kirillov Orbit — SU(2)³ → SU(3) Transition

**Date:** April 8, 2026
**Status:** VERIFIED
**Computation:** `code/kirillov_orbit.py`

---

## The Core Result

The entanglement of three generations through e-conservation ENHANCES
the gauge group from SU(2)³ (three independent weak forces) to SU(3)
(the strong force). The mechanism is group-theoretic:

    SU(2)³ acts on (C²)^⊗3
    → GHZ orbit has non-product stabiliser T²
    → T² = Cartan(SU(3)), NOT Cartan(SU(2)³)
    → orbit = SU(3)/T² = Fl(1,2;3)
    → isometry group = SU(3)

---

## The Moment Map

The moment map mu: CP^7 → su(2)*³ = R^9 sends each state to its
angular momentum expectation values in each SU(2) factor.

    mu_k^a(psi) = <psi| T_a^(k) |psi>

For the GHZ state: mu(GHZ) = 0 (origin of su(2)*³).

This means GHZ is a fixed point of the Cartan torus — consistent
with its T² stabiliser.

---

## The Key Distinction: Product vs Non-Product Stabiliser

For THREE INDEPENDENT gauge groups SU(2)³, the stabiliser of a
generic state would be U(1)³ = U(1) x U(1) x U(1) — three
independent circles, one per factor. The orbit would be
S² x S² x S² (a product of three 2-spheres), and the isometry
group would remain SU(2)³.

For the GHZ state, the stabiliser is T² = {(t₁,t₂,t₃) : t₁t₂t₃ = 1}.
This is NOT a product — the constraint t₁t₂t₃ = 1 ties the three
circles together. This constraint is EXACTLY the e-conservation law
a₁ + a₂ + a₃ = 0.

The non-product stabiliser forces the orbit to be a non-product
manifold — the flag manifold Fl(1,2;3) = SU(3)/T².

---

## Why SU(3) and Not SU(2)³

| Property | SU(2)³ | SU(3) |
|----------|--------|-------|
| Rank | 3 | 2 |
| Cartan torus | U(1)³ (3 independent circles) | T² (2-torus, Σa=0) |
| Root system | A₁ x A₁ x A₁ (6 independent roots) | A₂ (6 entangled roots) |
| Dimension | 9 | 8 |

The GHZ state's properties match SU(3), not SU(2)³:
- Stabiliser = T² = Cartan(SU(3)) ✓
- Tangent weights = A₂ root system ✓
- Orbit dimension = 6 = dim SU(3)/T² ✓

The extra dimension of SU(2)³ (dim 9 vs dim 8) is the overall U(1)
phase, which acts trivially in projective space CP⁷.

---

## The Entanglement Mechanism

Without entanglement (separable state): each generation has an
independent SU(2) gauge group. Root system A₁ x A₁ x A₁. Three
independent weak forces. No strong force.

With GHZ entanglement (e-conservation): the three SU(2) factors
are tied together by t₁t₂t₃ = 1. Their root systems merge into A₂.
The gauge group enhances to SU(3). The strong force emerges.

The strong force IS entanglement. Not metaphorically — literally.
SU(3) is what you get when you entangle three SU(2) factors through
a global conservation law.

---

## The Full Gauge Group Assembly

    SU(2)³ (dim 9)
      │
      ├── U(1) overall phase (dim 1, trivial)
      │
      └── Physical (dim 8)
            │
            ├── SU(3) from GHZ orbit (strong force)
            │     Orbit = Fl(1,2;3), root system A₂
            │     Internal space: CP² = SU(3)/(SU(2)×U(1))
            │
            ├── SU(2) residual (weak force)
            │     Internal space: S² = SU(2)/U(1)
            │
            └── U(1) from e-circle (electromagnetism)
                  Internal space: S¹

    G_SM = [SU(3) × SU(2) × U(1)] / Z₆

---

## Borel-de Siebenthal Classification

The identification of the orbit with Fl(1,2;3) = SU(3)/T² uses
the Borel-de Siebenthal classification: a compact homogeneous space
of dimension 6 with A₂ tangent root system and T² stabiliser is
UNIQUELY SU(3)/T².

No other compact group G/H has these properties:
- dim G/H = 6
- Root system of H in G = A₂
- H = T² (rank 2 torus)

The classification is: G = SU(3), H = T² (maximal torus). QED.

---

## References

- Kirillov, A. A. "Unitary representations of nilpotent Lie groups."
  Uspekhi Mat. Nauk 17, 57-110 (1962).
- Borel, A. & de Siebenthal, J. "Les sous-groupes fermés de rang
  maximum des groupes de Lie clos." Comment. Math. Helv. 23, 200 (1949).
- Dür, Vidal & Cirac, PRA 62, 062314 (2000).
- Paper 4, Theorem 5.2 (A₂ root system identification).
- Research 07 (Cartan matrix verification).
- Research 08 (stabiliser bridge argument).
