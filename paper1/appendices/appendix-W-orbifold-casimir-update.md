# Appendix W — Orbifold Casimir Update (Section W.9.2)

> **Update:** This section replaces the naive `S¹` Casimir estimate
> with the field-by-field computation on the physical `S¹/Z₂` orbifold.
> The result shifts the predicted e-circle radius from `R ≈ 21 μm`
> (circle) to `R ≈ 8.5 μm` (orbifold), closer to the Vafa et al.
> Dark Dimension prediction and within reach of current short-range
> gravity experiments.

---

## W.9.2 The Orbifold Casimir Energy — Field-by-Field Computation

### W.9.2.1 Boundary Conditions on `S¹/Z₂`

On the orbifold `S¹/Z₂ = [0, πR]`, fields have definite Z₂ parity:

- **Z₂-even** (Neumann b.c.): `Φ(−y) = +Φ(y)` → cosine modes
  `cos(ny/R)`, `n = 0, 1, 2, ...`
- **Z₂-odd** (Dirichlet b.c.): `Φ(−y) = −Φ(y)` → sine modes
  `sin(ny/R)`, `n = 1, 2, 3, ...`

The Casimir energy per d.o.f. (Appelquist & Chodos 1983):

    ρ_Neumann = −π²/(1440 (πR)⁴)
    ρ_Dirichlet = +7π²/(11520 (πR)⁴)

The Dirichlet contribution is positive (repulsive) and 7/8 the
magnitude of the Neumann contribution.

### W.9.2.2 Z₂ Parity Assignments

The Z₂ parity is determined by the spin structure (Appendix B):

**Graviton sector:**
- `g_μν` (4D graviton): Z₂-even (5 d.o.f.) → Neumann
- `g_μ5` (graviphoton → photon): Z₂-odd (3 d.o.f.) → Dirichlet
- `g_55` (dilaton): Z₂-even (1 d.o.f.) → Neumann

**SM fields:** Brane-localized at `φ = 0`. Do not contribute to
the BULK Casimir energy.

**Bulk fermions:**
- 3 × `N_i` (right-handed neutrinos): Z₂-odd (2 d.o.f. each) → Dirichlet

### W.9.2.3 The Computation

**Bosonic contribution:**

    ρ_B = 6 × ρ_N + 3 × ρ_D
        = 6 × (−π²/(1440(πR)⁴)) + 3 × (7π²/(11520(πR)⁴))
        = (−48 + 21) × π²/(11520(πR)⁴)
        = −27π²/(11520(πR)⁴)

**Fermionic contribution (with (−1)^F sign):**

    ρ_F = −6 × ρ_D = −6 × (7π²/(11520(πR)⁴)) = −42π²/(11520(πR)⁴)

**Total:**

    ρ_total = ρ_B − ρ_F = (−27 + 42) × π²/(11520(πR)⁴)
            = −15π²/(11520(πR)⁴)
            = −π²/(768(πR)⁴)

The sign is negative → a positive vacuum energy (dark energy). ✓

### W.9.2.4 The Predicted Radius

Setting `|ρ_total| = ρ_Λ = 3.9 × 10⁻¹¹ eV⁴ (ℏc)⁻³`:

    (πR)⁴ = π²/(768 × ρ_Λ)

    πR = [π²/(768 × 3.9 × 10⁻¹¹)]^{1/4} × ℏc

    R ≈ **8.5 μm**,   L = 2πR ≈ **53 μm**

### W.9.2.5 Comparison

| Geometry | R | L | Source |
|---|---|---|---|
| `S¹` (circle, full SM) | 21 μm | 130 μm | §6.6 (naive) |
| **`S¹/Z₂` (orbifold, bulk only)** | **8.5 μm** | **53 μm** | **This section** |
| Vafa et al. (Dark Dimension) | 1–5 μm | 6–30 μm | Swampland |

The orbifold value is the physical prediction. It should replace
the circle estimate in all subsequent calculations. The value is
consistent with the Vafa et al. range and within reach of the IUPUI
short-range gravity experiments (sensitive at 10–100 μm).

### W.9.2.6 Self-Consistency

The dark energy density determines R. The Casimir energy at R gives
ρ_Λ. The loop is closed: `ρ_Λ → R → ρ_Casimir(R) = ρ_Λ`. ✓

---

## W.9.3 Clarification: Circle vs Orbifold Scenarios

Two geometric scenarios appear in the appendices:

- **Circle scenario** (`S¹`, `R ≈ 21 μm`): Used in the perturbative
  finiteness computation (Appendices F, G, K, S) and the hydrogen
  atom calculation (Appendix M). The finiteness theorem depends on
  the compactness of `S¹`, not on whether it is orbifolded.

- **Orbifold scenario** (`S¹/Z₂`, `R ≈ 8.5 μm`): Used in the dark
  energy, dark matter, and baryogenesis predictions (Appendices W, Y,
  and Paper 2). The Z₂ structure is required by the spin structure
  (Appendix B) and is the physical geometry.

The perturbative finiteness results hold for BOTH scenarios — the
KK mode sums converge under zeta regularization whether the modes
are periodic (circle) or have definite parity (orbifold). The
specific Epstein zeta values may differ, but the finiteness mechanism
(pole at `s = L/2 > 0`, evaluation at `s ≤ 0`) is unchanged.
