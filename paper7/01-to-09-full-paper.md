# Paper 7 — Sections 1-8: The Full Argument

## 1. The Problem

The naive QFT estimate of the vacuum energy is:

    ρ_QFT ~ ∫₀^{M_Pl} k³ dk ~ M_Pl⁴ ~ (2.4 × 10¹⁸ GeV)⁴

The observed value:

    ρ_Λ = (2.3 × 10⁻³ eV)⁴ = (2.3 meV)⁴

The ratio:

    ρ_Λ/ρ_QFT ~ (2.3 × 10⁻³ eV / 2.4 × 10²⁷ eV)⁴ ~ 10⁻¹²²

This is the cosmological constant problem. No known symmetry, no known
mechanism, no known anthropic argument fully explains it.

## 2. Why Previous Approaches Fail

**Supersymmetry:** Cancels boson-fermion contributions. Fails because
SUSY is broken at the TeV scale, leaving a residual `~ (TeV)⁴ ~ 10⁶⁰ ρ_Λ`.

**Anthropic selection:** Unverifiable. Not science.

**Sequestering:** Hides the cosmological constant in extra dimensions.
Requires fine-tuned boundary conditions.

**Self-tuning:** Scalar fields adjust to cancel Λ. Generically
requires fine-tuned potentials.

The framework's approach is different: the cosmological constant is
not cancelled — it is DETERMINED by the moduli stabilization conditions.

## 3. The Four Contributions to Vacuum Energy

In the 11D framework, the vacuum energy receives contributions from
all sectors:

| Source | Scale | Sign |
|--------|-------|------|
| 4D graviton + matter loops | `M_Pl⁴` | `+` (large, positive) |
| CP² Casimir (gluons) | `(10¹⁵ GeV)⁴` | `−` (attractive) |
| S² Casimir (W, Z, Higgs) | `(100 GeV)⁴` | `−` (attractive) |
| S¹ Casimir (visible sector) | `+(2 meV)⁴` | `+` (repulsive) |
| S¹ Casimir (3 bulk ν_R) | compensates | `−` (adjusts sign) |

The TOTAL vacuum energy is the sum. Without any constraint, this sum
would be dominated by the `M_Pl⁴` term — completely unrelated to the
observed `ρ_Λ`.

## 4. The Stabilization Conditions as Constraints

The three moduli are stabilized by setting:

    ∂V_total/∂R = 0     (1)
    ∂V_total/∂r₂ = 0    (2)
    ∂V_total/∂r₃ = 0    (3)

Each condition is a relationship between contributions at different
scales. Explicitly:

**Equation (1):** `∂V_{S¹}/∂R + ∂V_{GW}/∂R = 0`

    4π²ℏc/(768π⁴R⁵) = ∂V_{GW}/∂R|_{R_min}

This fixes `R = R_min ~ 8.5 μm` and determines the S¹ Casimir
contribution to `ρ_Λ`.

**Equation (2):** `∂V_{S²}/∂r₂ = 0`

The S² Casimir energy stabilizes `r₂ ~ 10⁻¹⁸ m`. This condition
relates the electroweak Casimir contribution to the GW stabilization
of the weak compact dimension.

**Equation (3):** `∂V_{CP²}/∂r₃ = 0`

The CP² Casimir energy stabilizes `r₃ ~ 10⁻³¹ m`. This condition
relates the GUT-scale Casimir contribution to the stabilization
of the strong compact dimension.

## 5. The Residual Vacuum Energy

After imposing conditions (1), (2), (3), three of the four large
contributions are determined by the stabilization requirements. The
residual vacuum energy:

    ρ_Λ = V_total|_{minimum of (R,r₂,r₃)}

is the value of the potential AT the simultaneous minimum. This is
a specific number — not zero, not `M_Pl⁴`, but something determined
by the geometry of `CP² × S² × S¹`.

**The dimensional argument:**

At the minimum, the Goldberger-Wise potential contributes:

    V_GW(R_min) ~ m_φ²(R_min) × φ_min² ~ H_0² × M_Pl² ~ H_0² M_Pl²

Since `H_0 ~ 10⁻³³ eV`:

    ρ_Λ ~ (10⁻³³ eV)² × (10²⁸ eV)² ~ 10⁻¹⁰ eV⁴ ~ (2 meV)⁴

**This dimensional argument gives the right answer!**

The cosmological constant is of order `H_0² M_Pl²` because:
- `H_0` is the Hubble rate today, set by when the dilaton thawed (Paper 6)
- `M_Pl` is the Planck scale, set by the 11D Newton's constant
- Their product appears naturally from the GW potential at the dilaton minimum

## 6. Why This Is Not Fine-Tuning

In the SM, the 122-order cancellation is REQUIRED but UNEXPLAINED —
why should the cosmological constant be so small?

In the framework, `ρ_Λ ~ H_0² M_Pl²` FOLLOWS from the stabilization
conditions. The question "why is `ρ_Λ` small?" becomes "why is `H_0`
small compared to `M_Pl`?" which becomes "why did the dilaton thaw
recently?" which becomes "why does the GW potential have a minimum
at `φ_min ~ M_Pl`?"

The last question has a geometric answer: `φ_min ~ M_Pl` because
the Casimir + GW potential minimum is at the Planck scale by
construction (the Goldberger-Wise mechanism requires `m_φ R_min ~ 1/k`
where `k ~ M_Pl`). The Planck scale IS the natural scale of the dilaton.

The hierarchy `ρ_Λ/M_Pl⁴ ~ (H_0/M_Pl)² ~ 10⁻¹²²` is the hierarchy
`H_0/M_Pl ~ 10⁻⁶¹` — which is just the statement that the universe
is very old (`t_0 ~ 1/H_0 ~ 4 × 10¹⁷ s`). **The cosmological constant
is small because the universe is old.** And the universe is old because
it took 13.8 billion years for the dilaton to reach its current
slowly-thawing state — a consequence of the Casimir + GW potential
shape fixed by Paper 1.

## 7. The Key Calculation

The full verification requires computing `V_total(R, r₂, r₃)` as a
function of all three moduli and finding the simultaneous minimum.
This is the Casimir energy of ALL bulk fields on `CP² × S² × S¹/Z₂`:

    V_total = V_{11D}(graviton) + V_{S¹}(SM fields projected) + V_{S²}(EW fields) + V_{CP²}(QCD fields) + V_{GW}(all three)

The computation requires:
1. The Casimir energy on CP² (the heat kernel of the SU(3) Laplacian)
2. The Casimir energy on S² (the heat kernel of the SU(2) Laplacian)
3. The heat kernel of the full product `CP² × S² × S¹/Z₂`
4. The simultaneous minimization

Steps 1-2 are known mathematically (from the spectral theory of
symmetric spaces). Step 3 factorizes on a product manifold. Step 4
is the numerical minimization.

**This calculation is identifiable as future work.** The framework
predicts it will give `ρ_Λ ~ (2 meV)⁴` — this is the key verifiable
claim of Paper 7.

## 8. Predictions and Falsifiability

**If the calculation gives `ρ_Λ = (2 meV)⁴` to within a factor of 10:**
→ Geometric resolution of the cosmological constant problem confirmed.

**If the calculation gives `ρ_Λ ≫ (2 meV)⁴`:**
→ Additional fine-tuning required; the geometric mechanism is incomplete.

**If the calculation gives `ρ_Λ = 0` exactly:**
→ A symmetry is operating (perhaps a remnant SUSY); dark energy is
  not from the Casimir mechanism but from a different origin.

The prediction is testable in principle — the computation is defined
and finite (the Casimir energies on compact symmetric spaces are
well-defined mathematical objects). No experiment can distinguish the
geometric mechanism from the SM cosmological constant — but the internal
consistency of the framework is verifiable by explicit calculation.

## 9. Conclusion

The cosmological constant problem is reframed:

**SM:** "Why is Λ so small?" (no answer — requires 122-order fine-tuning)

**Framework:** "What is the value of `V_total` at the simultaneous
Casimir minimum of `CP² × S² × S¹/Z₂`?" (a calculation, not a tuning)

The answer is `ρ_Λ ~ H_0² M_Pl² ~ (2 meV)⁴` from dimensional analysis
of the GW stabilization potential. The detailed calculation — showing
that the geometry of `CP² × S² × S¹` produces this specific value
from the Casimir energies of the known field content — is the central
open problem of the framework.

### References

- Weinberg, S. "The cosmological constant problem." *Rev. Mod. Phys.*
  61, 1 (1989). — The definitive statement of the problem.
- Bousso, R. "The cosmological constant." *Gen. Rel. Grav.* 40, 607 (2008).
- Goldberger, W. D. & Wise, M. B. *Phys. Rev. Lett.* 83, 4922 (1999).
- Arkani-Hamed, N., Hall, L. J., Nomura, Y. & Weiner, N.
  "The large hadron collider, dark matter, and cosmology." *Nucl. Phys. B*
  605, 81 (2001). — Sequestering approaches.
- Papers 1-6: [this framework series]
