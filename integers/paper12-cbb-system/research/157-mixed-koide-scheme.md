# Research 157: Mixed Koide Scheme — γ-Magnitudes with Z/3Z Orbit Characters

*Cycle 3. Author: G Six, with Claude Opus 4.6. Date: 2026-04-09.*
*Builds on research/47 (three-category γ-template), research/140
(Jones index [M:N]=3 fixes Koide and generation count structurally),
research/141 (Frobenius p=5, N=13 gives three Z/3Z orbits),
research/151 (direct orbit periods give Q=0.5088, wrong by 23.7%).*

---

## 1. Motivation

Research/151 closed in the negative the naive idea of using
Frobenius-orbit Gaussian periods as lepton mass magnitudes: the
period spread |η|² ≈ 370 is far too compressed for the observed
hierarchy m_τ/m_e ≈ 3477. Research/141 §6.1 left open a *mixed*
scheme: magnitudes from γ-zeros, labels from orbit characters.
This note executes that scheme and tests whether the 0.08 %
residual of research/47 §6.4 closes.

## 2. The mixed construction

The Z/3Z of Frobenius orbits at (p, N) = (5, 13) has three
characters χ_0, χ_1, χ_2 with χ_k(j) = ω^{kj}, ω = e^{2πi/3}.
The γ-template of research/47 provides three category amplitudes:

    A_PRODUCT    = √(γ_7 · γ_8)        = 42.106   (tau class)
    A_RATIO      = √(γ_7 · γ_8^{1/4})  = 10.246   (mu class)
    A_DIFFERENCE = √|γ_4 − γ_1|        =  4.036   (e class, trial)

The mixed masses are defined as Z/3Z Fourier components:

    m_i := (1/3) |Σ_j χ_i(j) A_j|²,    i = 0, 1, 2.

By Parseval, Σ_i m_i = Σ_j A_j² ≈ 1877 MeV.

## 3. Numerical results

### 3.1 Fourier mixing (characters as phases on category amplitudes)

| scheme                         | m_1 [MeV] | m_2 [MeV] | m_3 [MeV] | Q        | residual |
|:-------------------------------|:---------:|:---------:|:---------:|:--------:|:--------:|
| Fourier, a₃ = 0 (empty diff)   | 913.57    | 482.15    | 482.15    | 0.34162  | −48.8 %  |
| Fourier, a₃ = √\|γ₄−γ₁\|        | 1059.86   | 417.15    | 417.15    | 0.35154  | −47.3 %  |
| direct γ-template (research/47)| 1772.89   | 104.98    | 0.5106    | 0.66613  | **0.08 %** |
| orbit periods (research/151)   | —         | —         | —         | 0.5088   | −23.7 %  |

The Fourier mixing **destroys the hierarchy**: when one amplitude
dominates (A_PRODUCT ≫ A_RATIO ≫ A_DIFFERENCE), the three Z/3Z
Fourier components fall within a factor of 2–3 of each other, and
the Koide ratio collapses toward 1/3 (the Q-value of three equal
masses). This is the opposite of what the lepton hierarchy needs.

### 3.2 Power-progression mixing (characters as exponents)

A second reading: the three Z/3Z characters select three powers of
γ_8 in a geometric progression {γ_8^1, γ_8^{1/4}, γ_8^p}. The first
two reproduce research/47's m_τ and m_μ. Taking p = 1/16 (the
natural next term in the Z/3Z-compatible progression 4^{−k}):

    m_τ = γ_7·γ_8           = 1772.89 MeV
    m_μ = γ_7·γ_8^{1/4}     =  104.98 MeV
    m_e = γ_7·γ_8^{1/16}    =   51.79 MeV    (PDG 0.511 — 100× high)
    Q   = 0.5442,    residual vs 2/3 = **−18.4 %**

Solving Koide Q = 2/3 for p gives p = −1.152, m_e = 0.5320 MeV,
which is **4.1 %** off PDG — *worse* than research/47's
Koide-solved 0.5106 MeV at 0.08 %. The power-progression mixing
does not help either.

## 4. Why the mixed scheme fails

The Koide combination is extremely sensitive to the smallest mass:
Q = 2/3 requires a specific quartic structure in the √m_i that
both research/47 (empirical γ_7·γ_8 products) and the Jones-index
argument of research/140 produce *directly*, without needing an
orbit-character dressing. Any non-trivial Z/3Z mixing redistributes
the √m_i weights and pushes Q either toward 1/3 (equal masses) or
toward 1 (dominant-single-mass limit), *away* from 2/3.

The orbit characters supply the right **labels** (three
generations, Z/3Z grading consistent with N_eff = γ_6^{1/3}) but
carry no metric information. The γ-template supplies the right
magnitudes and **already** satisfies Koide at 0.08 %. Dressing one
with the other cannot improve either.

## 5. Verdict

| Scheme                              | Q       | residual |
|:------------------------------------|:-------:|:--------:|
| γ-template (research/47 §6.4)       | 0.66613 | **0.08 %** |
| Mixed Fourier (this note §3.1)      | 0.3515  | −47.3 %  |
| Mixed power-progression (§3.2)      | 0.5442  | −18.4 %  |
| Direct orbit periods (research/151) | 0.5088  | −23.7 %  |

**The mixed scheme does not close the 0.08 % residual.** It is
worse in every variant tested. The 0.08 % residual of research/47
is the **floor** of all γ-zero + orbit-character constructions
currently available; further shrinkage would require a genuinely
new matrix-element principle (e.g. a direct Tomita–Takesaki
derivation of m_τ, m_μ from the subfactor N ⊂ M of index 3).

**Structural takeaway.** Research/140's Jones-index result
(Q = 2/[M:N] = 2/3 **structurally**, to 9×10⁻⁴ %) already explains
why Koide holds; it does not touch the 0.08 % numerical residual
because that residual lives in the γ-zero formulas for m_τ, m_μ,
not in the Koide identity itself. The orbits supply labels, the
subfactor supplies the identity, the γ-zeros supply the magnitudes,
and the 0.08 % is where γ_7·γ_8 and γ_7·γ_8^{1/4} meet PDG — a
statement about Riemann zeros, not about Z/3Z.

### 5.1 Recommendation

Close this route. The path to a sub-0.08 % Koide residual is a
**direct subfactor-theoretic derivation** of m_τ and m_μ (not a
relabelling of the existing γ-template), following research/140 §5
rather than research/141's orbit programme.

## 6. References

- research/47 §6.4 — Koide-solved m_e = 0.5106 MeV, 0.08 %
- research/140 — Jones index 3 ⇒ Q = 2/3 structurally
- research/141 — Frobenius orbits at (p, N) = (5, 13)
- research/151 — direct orbit periods Koide Q = 0.5088, 23.7 %
- Koide, *Lett. Nuovo Cim.* **34** (1982) 201
- Jones, *Invent. Math.* **72** (1983) 1

---

*Mixed Koide scheme tested in two variants (Fourier, power
progression); both fail to improve on research/47's 0.08 %
residual. The 0.08 % is a statement about γ_7·γ_8 matching PDG
m_τ, not a statement about Z/3Z orbit structure. Route closed.*
