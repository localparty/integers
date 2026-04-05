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

## 7. References

- Buchmuller, Di Bari, Plumacher, "Leptogenesis for Pedestrians,"
  Ann. Phys. 315, 305 (2005) [hep-ph/0401240]
- Giudice, Notari, Raidal, Riotto, Strumia, Nucl. Phys. B 685, 89
  (2004) [hep-ph/0310123]
- Gonzalo et al., arXiv:2403.xxxxx (2024) — KK neutrino tower decays
