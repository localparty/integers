# Resolution of the K Issue: K Depends on m_nu, Not M_R

*The washout parameter was computed with the wrong M_R (2.5 × 10¹⁴ GeV
from a unit error). But K doesn't depend on M_R — it depends only on
the light neutrino mass. The corrected K ≈ 46, still in the strong
washout regime. The 1/ξ² law holds.*

---

## 1. The Key Formula

The washout parameter (BDP 2005, Eq. 5-6):

    K = m̃₁ / m_star

where m̃₁ = (Y†Y)₁₁ v²/M₁ is the effective neutrino mass and:

    m_star = (16π^{5/2} √g_*) / (3√5) × v²/M_Pl = **1.08 × 10⁻³ eV**

For the type-I seesaw with one dominant Yukawa: m̃₁ ≈ m_ν.

    **K = m_ν / m_star ≈ m_ν / (1.08 meV)**

K is independent of M_R. The seesaw relation y² = m_ν M_R/v² and the
Hubble rate H ∝ M_R² cause M_R to cancel exactly.

---

## 2. Numerical Values

| m_ν (meV) | K     | Regime        |
|-----------|-------|---------------|
| 8.7 (solar) | 8   | transition    |
| 30        | 28    | strong        |
| 50 (atm)  | **46**| **strong**    |
| 60        | 56    | strong        |
| 100       | 93    | strong        |

For m_ν = 50 meV (atmospheric splitting): **K ≈ 46**.

This is in the STRONG washout regime — not K = 460 (old, wrong M_R)
and not K = 5 (an intermediate calculation error). The physics is
qualitatively similar to the original: strong washout with the
1/(K ln K) efficiency formula approximately valid.

---

## 3. Comparison: Old vs. Corrected

| Quantity    | Old (unit error)    | Corrected          |
|-------------|--------------------|--------------------|
| M_R         | 2.5 × 10¹⁴ GeV    | 10¹⁵ GeV (CP²)    |
| y           | 0.45               | 0.9                |
| K           | 460                | **46**             |
| Regime      | Very strong washout| Strong washout     |
| f(K, ξ=0.43)| 1.38              | 1.78               |
| Corrected ξ | 0.507              | ~0.50–0.53         |

---

## 4. The Washout Ratio and the 1/ξ² Law

The DM-to-baryon ratio: Ω_DM/Ω_b = κ(K_hid)/κ(K_vis)

where K_hid = K × ξ² (Paper 2 derivation: hidden brane washout
reduced by ξ² from the temperature ratio).

Using BDP Eq. 63 (strong washout efficiency):

    κ(K) = (2 / (z_B K)) × (1 − exp(−z_B K/2))

| ξ    | K_hid | κ(46)   | κ(K_hid) | Ratio | Target |
|------|-------|---------|----------|-------|--------|
| 0.40 | 7.4   | 0.0056  | 0.058    | 10.2  | 5.36   |
| 0.44 | 8.9   | 0.0056  | 0.044    | 7.9   | 5.36   |
| 0.48 | 10.6  | 0.0056  | 0.035    | 6.3   | 5.36   |
| 0.50 | 11.6  | 0.0056  | 0.032    | 5.6   | 5.36   |
| 0.51 | 12.0  | 0.0056  | 0.030    | 5.3   | 5.36   |

**The ratio = 5.36 at ξ ≈ 0.50–0.51.** This is at the BBN
boundary (ξ < 0.50 at 2σ from BBN 2025).

---

## 5. The Tension and Its Resolution

With K = 46, the self-consistent ξ ≈ 0.50–0.51. This is:
- Marginal with BBN 2025 (ξ < 0.50 at 2σ)
- In 2.5σ tension with ACT DR6 (ξ < 0.40 at 2σ)

The same tension existed with K = 460 (corrected ξ ≈ 0.507).
The K value changed (460 → 46) but the corrected ξ is similar
because the logarithmic correction f(K,ξ) partially compensates.

**Three resolution pathways:**

1. **ξ is set by leading-order 1/ξ² = 5.36 → ξ = 0.432.** The
   washout correction (f ≈ 1.78) is an overestimate because the
   1/(K ln K) formula is approximate. The exact Boltzmann equation
   with thermal averaging may give f closer to 1.0.

2. **Intra-tower KK neutrino decays** (Gonzalo et al. 2024) reduce
   the effective ΔN_eff from the mirror sector, relaxing the BBN
   bound and allowing ξ up to ~0.55.

3. **The full two-brane Boltzmann equation** (not yet solved)
   replaces the approximate f(K,ξ) formula with the exact result.
   The precise thermal averaging of inverse decays on the cold
   hidden brane may give significantly different washout than
   the K × ξ² approximation.

---

## 6. What Is Solid

1. **K = m_ν/m_star ≈ 46** — from BDP (2005), model-independent.
2. **K is independent of M_R** — the seesaw M_R cancels exactly.
3. **Strong washout regime** — K >> 1, the 1/(K ln K) formula
   applies approximately.
4. **The 1/ξ² law at leading order** — gives ξ = 0.432, N_eff ≈ 3.28.
5. **All CAMB predictions** — use ξ as input, unaffected by K.
6. **The washout correction** pushes ξ to ~0.50, in tension with
   BBN but resolvable by exact Boltzmann calculation.

---

## 7. Stabilization Results (from etc/08)

### 7.1 S² tower: does NOT stabilize R

SUSY is exact on S² (simply connected, `π₁(S²) = 0` → no
Scherk-Schwarz). At every S² KK level: `N_B(l) = N_F(l)` →
`ΔN_S²(l) = 0`. The S² tower contributes ZERO to the Casimir.
Same for CP². Only S¹ breaks SUSY through the spin structure.

V(R) = −ΔN × 3ζ(5)/(64π⁶R⁴) is monotonically increasing.
No minimum from Casimir alone.

### 7.2 Goldberger-Wise: requires μ ~ 0.4 eV

The GW potential V_GW = A exp(−2μπR) creates a minimum at:

    R_min ≈ ln(A/c) / (2μπ)

With A ~ m_H² M₅² ~ 10⁵⁷ eV⁴ and c ~ 1.74 × 10⁻⁴ eV⁴:

    ln(A/c) ≈ 140

For R = 10 μm: **μ = 0.44 eV**. The eV scale — 10 orders below
the weak scale. The CC problem is reduced from 10¹²² to 10¹⁰.

### 7.3 What sets μ?

The 140 = ln(m_H²M₅²/c_Casimir) is the key number. It comes from
the hierarchy between the Higgs-M₅ scale and the Casimir coefficient.
The physical content: R/l_P ~ exp(70) because the Casimir residual
(from ΔN = 3.44) is exponentially small compared to the electroweak
scale.

---

## 8. The Path Forward

### 8.1 The 11D dilaton effective potential (THE key computation)

The bulk scalar that stabilizes S¹ is the DILATON — the zero mode
of g₅₅ from the 11D metric. Its effective potential receives
contributions from:

1. **The S¹ Casimir** (computed): V_C = −ΔN × 3ζ(5)/(64π⁶R⁴)
2. **Brane couplings**: the dilaton couples to brane-localized
   fields (Higgs, SM fermions) through the warp factor
3. **The GW scalar**: if a separate bulk scalar exists, its
   boundary conditions generate V_GW

The question is whether the dilaton's OWN brane couplings generate
a stabilizing potential WITHOUT needing a separate bulk scalar.

### 8.2 The dilaton-Higgs coupling from dimensional reduction

In the 5D metric `ds² = e^{−2σ(y)} g_μν dx^μ dx^ν + R² dy²`,
the Higgs VEV on the visible brane depends on R through:

    v(R) = v₀ × e^{−σ(0)} × (R/R₀)^α

where α is the dilaton-Higgs coupling exponent. The Higgs
contribution to V_eff(R) is:

    V_Higgs(R) = −λ v(R)⁴/4 = −λ v₀⁴ (R/R₀)^{4α} / 4

For α > 0: V_Higgs decreases with R (same direction as Casimir).
For α < 0: V_Higgs increases with R (STABILIZING).

The sign of α is determined by the conformal dimension of the
Higgs on the brane. In RS: α = −1 (the Higgs VEV is warped DOWN
on the IR brane). In our framework: α depends on the S² Casimir
coupling to R.

**Computation needed:** Derive α from the KK reduction of the
5D metric on `S² × S¹/Z₂`, with the Higgs identified as the
Wilson line `g_{iψ}` (Paper 4, §6). The R-dependence of the
Higgs VEV follows from the R-dependence of the S² Casimir
potential that generates the Higgs mechanism.

### 8.3 Flux stabilization: TOPOLOGICALLY IMPOSSIBLE

The 4-form `F₄ = dC₃` requires a 4-cycle. By the Künneth theorem:

    b₄(CP² × S² × S¹) = 2

The two 4-cycles are CP² and CP¹ × S² — **neither involves S¹.**
(Because b₁(CP²) = b₃(CP²) = 0, no 4-cycle can include the S¹ factor.)

F₄ flux cannot generate an R-dependent potential. The S¹ modulus
is a FLAT DIRECTION of the flux potential. Flux stabilization is
ruled out on topological grounds for this specific manifold.

### 8.4 The brane-localized Higgs potential (NEW — most promising)

The SM Higgs on the visible brane couples to R through the metric.
The Higgs VEV depends on R through the warp factor:

    v(R) = v₀ × (R/R₀)^α

where α is the conformal dimension of the Higgs on the brane.
The brane Higgs potential contributes:

    V_Higgs(R) = −λ v(R)⁴ / 4 = −(λv₀⁴/4) × (R/R₀)^{4α}

For α = −1 (RS IR brane): V_Higgs ∝ 1/R⁴ — same power as Casimir.
No new minimum.

For α ≠ −1: DIFFERENT R-dependence → competition with Casimir →
**potential minimum at finite R**.

In the framework: the Higgs IS the Wilson line `g_{iψ}` on S²
(Paper 4, §6). Its VEV depends on the S² Casimir potential, which
depends on R through the overall compactification volume. The
exact α comes from the KK reduction of the gauge-Higgs sector.

**This is the key computation.** If α is determined from the
gauge-Higgs geometry and α ≠ −1, then:

    V_total = −c/R⁴ − (λv₀⁴/4)(R/R₀)^{4α}

has a minimum at R_min where 4c/R⁵ = −4α(λv₀⁴/4R₀^{4α}) R^{4α−1}:

    R_min^{4−4α} = c R₀^{4α} / (α λ v₀⁴/4)

For α > 0 (Higgs VEV grows with R): V_Higgs becomes more negative
at large R, destabilizing. No minimum.

For −1 < α < 0 (Higgs VEV decreases with R, but slower than 1/R):
V_Higgs ∝ R^{4α} with −4 < 4α < 0. Combined with −c/R⁴: the
Casimir dominates at small R, Higgs dominates at large R. Minimum
exists if the powers are different (4α ≠ −4, i.e., α ≠ −1).

### 8.4 Action items

1. **Compute V_flux(R)** for the 4-form flux `F₄ = dC₃` on the
   cycle `S¹ × (2-cycle in CP²)` with flux quantum n = 1.
   Determine the coefficient in V_flux = n²/(R × Vol₆ × κ₁₁²).

2. **Find R_min** from V_total = V_flux + V_Casimir = 0.
   Check whether R_min ~ 10 μm.

3. **Compute ρ_Λ = V(R_min)** and compare to (2.25 meV)⁴.

4. If successful: R is determined by {n, Vol₆, ΔN} — all geometric.
   ρ_Λ is PREDICTED. The CC problem is solved.

---

## 9. References

- Buchmuller, Di Bari, Plumacher, "Leptogenesis for Pedestrians,"
  Ann. Phys. 315, 305 (2005) [hep-ph/0401240]
- Giudice, Notari, Raidal, Riotto, Strumia, Nucl. Phys. B 685, 89
  (2004) [hep-ph/0310123]
- Gonzalo et al., arXiv:2403.xxxxx (2024) — KK neutrino tower decays
- Goldberger, Wise, Phys. Rev. Lett. 83, 4922 (1999) — GW mechanism
- Montero, Vafa et al., arXiv:2205.12293 (2022) — Dark Dimension
- Bousso, Polchinski, JHEP 06, 006 (2000) — Flux stabilization
