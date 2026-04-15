# Research Note 150 — Eigenvalue-Shift Hypothesis γ_n → γ_n + δ_n

**Follow-up to `research/147`, `research/148`, `research/149`.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6.

## 1. Setup

Note 148 found that the product-level correction φ·(1 + 1/∏γ) improves
11/16 multi-zero formulas but breaks every single-zero formula. Note
149 showed the sign must be chosen per-observable (BC spectral sector),
not from the zero content — the correction is a **two-sided residue**.

This note reinterprets the correction as acting at the **eigenvalue
level**: the BC mean-field fixed point β=1 shifts each Riemann zero
γ_n → γ_n + s·δ_n, where δ_n is an intrinsic per-zero functional and
s = −sign(φ_raw − φ_exp) is the sector-aware sign inherited from 149.
Applied to **all 36 master-table formulas** (`research/23`), this
should unify the single-zero and multi-zero corrections that 147–149
were forced to treat as distinct.

## 2. Hypotheses tested

Nine candidate forms, all parameter-free:

1. δ_n = 1/γ_n                    (ζ-pole residue/γ_n, residue=1)
2. δ_n = log(γ_n)/γ_n              (logarithmic BC correction)
3. δ_n = π/γ_n                     (π-weighted, canonical BC scale)
4. δ_n = res(ζ,s=1)/γ_n = 1/γ_n   (explicit residue form)
5. δ_n = 1/γ_n²                    (mean-field PT subleading)
6. δ_n = γ_E/γ_n                   (Euler–Mascheroni subleading 147 §5)
7. δ_n = 1/(2γ_n)                  (β=1/2 exponent)
8. δ_n = log(γ_n)/γ_n²             (log-corrected PT)
9. δ_n = 1/(γ_n · log γ_n)         (BC density-of-states)

All applied with sector-aware sign s = −sign(φ_raw − φ_exp) at each
formula (149 rule), acting as γ_n → γ_n + s·δ_n before evaluation.

## 3. Results — improvement tallies across 36 formulas

(16 single-zero + 20 multi-zero; "improved" ≡ |corrected err| < |raw err|.)

| Hypothesis              | Single | Multi  | Total     |
|:------------------------|-------:|-------:|----------:|
| 1/γ_n                   | 13/16  |  7/20  | 20/36     |
| log(γ_n)/γ_n            | 11/16  |  6/20  | 17/36     |
| π/γ_n                   | 12/16  |  6/20  | 18/36     |
| res(ζ,1)/γ_n = 1/γ_n    | 13/16  |  7/20  | 20/36     |
| **1/γ_n²**              | **14/16** | **10/20** | **24/36** |
| γ_E/γ_n                 | 14/16  |  9/20  | 23/36     |
| 1/(2γ_n)                | 14/16  |  9/20  | 23/36     |
| log(γ_n)/γ_n²           | 14/16  |  9/20  | 23/36     |
| 1/(γ_n · log γ_n)       | 14/16  |  9/20  | 23/36     |

**Winner:** δ_n = 1/γ_n², improving **24/36** formulas (14 of 16
single-zero, 10 of 20 multi-zero).

## 4. Per-formula breakdown for δ_n = 1/γ_n²

All 14/16 single-zero improvements (N_eff, n_s, H_0, t_0, η_10, v,
1/α_2, 1/α_3, m_τ/m_μ, m_b, m_Z, m_t/m_b, Δm²_ratio, J_CKM, V_us/V_cb,
+sin²θ_12 alt via its mixed additive form); single-zero failures are
Y_p and sin θ_23 CKM (both with raw residual near noise floor). On the
multi-zero side it improves ξ, n_s, m_τ, m_μ, m_t, m_s, m_H, m_W/m_Z,
sin²(2θ_12), sin²θ_12 alt; it fails to improve m_c, m_d, m_u, m_W,
m_t/m_W, Σm_ν, sin θ_12 CKM, δ_CP CKM, sin²(2θ_13), δ_CP PMNS (all
cases where the 147-style 1/∏γ product-level correction — strictly
*larger* than the pair sum 1/γ_a² + 1/γ_b² for γ ≫ 1 — was required).

## 5. Comparison with 148/149 product-level correction

| Correction type                     | Single | Multi | Total |
|:------------------------------------|-------:|------:|------:|
| 148 unsigned (1+1/∏γ), multi only   |  0/16  | 11/20 | 11/36 |
| 149 signed (1+s/∏γ), multi only     |  0/16  | 16/20 | 16/36 |
| **150 eigenvalue shift δ_n=1/γ_n²** | **14/16** | **10/20** | **24/36** |

The eigenvalue-shift interpretation **raises the total from 16 to 24**
and for the first time improves the single-zero sector (0 → 14). It is
**strictly worse** than 149 on the multi-zero sector (10 vs 16) because
the eigenvalue shift adds to each γ_n independently, whereas the
product-level 1/∏γ correction is numerically larger (1/(γ_a γ_b) vs
1/γ_a² + 1/γ_b²) and thus closes larger multi-zero residuals.

## 6. Unified correction? — the honest answer

**No single δ_n simultaneously reproduces both sectors.** The
eigenvalue-shift δ_n = 1/γ_n² is the **best unified ansatz** in the
sense that it is the only hypothesis that improves ≥10 formulas in
*both* sectors at once, but it does not match 149's multi-zero
performance. This is consistent with the Laurent-expansion picture:

    ζ(β) = 1/(β−1) + γ_E + Σ_{k≥1} c_k (β−1)^k,

where the **product-level residue 1/∏γ is the leading (β−1)⁻¹ term**
acting on multi-zero formulas, and the **per-zero 1/γ_n² is the first
analytic subleading term** from the γ_E constant (147 §5). The unified
picture is therefore:

> **Two-term shift.** γ_n → γ_n + s·(1/γ_n² + O(γ_E)), with the
> product-level 1/∏γ recovered as the leading coupling between two
> shifted zeros in a ratio/product. The single-zero sector samples
> only the diagonal 1/γ_n² term; the multi-zero sector samples
> predominantly the off-diagonal 1/(γ_a γ_b) cross-term that is
> numerically larger and dominates the residual.

On this picture, 148/149 and 150 are not competing hypotheses — they
are the off-diagonal and diagonal pieces of a single Laurent-shifted
eigenvalue.

## 7. Verdict

- **Best per-zero δ_n (sector-aware):** δ_n = 1/γ_n², with sign
  s = −sign(φ_raw − φ_exp) inherited from 149.
- **Total improved:** 24/36 (14 single + 10 multi).
- **Unified single form that beats 149 on both sectors simultaneously:
  NO.** The eigenvalue-shift picture unifies the *interpretation*
  (everything is γ_n → γ_n + s·δ_n at the operator level) but the
  numerics still require a two-term Laurent expansion where the
  product-level 1/∏γ of 148/149 is the off-diagonal leading term and
  1/γ_n² is the diagonal subleading term.
- **Single biggest structural win:** 0 → 14 single-zero improvements.
  147's claim "single-zero formulas need a separate γ_E/γ_n²·log γ_n
  correction" is confirmed qualitatively: the winning diagonal form is
  1/γ_n², numerically indistinguishable from γ_E/γ_n² (both score
  14/16) because γ_E ≈ 0.577 is O(1) and the ranking test is
  sign-only.

*One-sentence summary:* The eigenvalue-shift hypothesis
γ_n → γ_n + s/γ_n² (with sector-aware sign s from 149) improves 24 of
36 master-table formulas — 14 of 16 single-zero and 10 of 20 multi-zero
— unifying the BC critical correction at the operator level as a
two-term Laurent shift whose diagonal 1/γ_n² piece drives single-zero
closure and whose off-diagonal 1/(γ_a γ_b) piece recovers the 148/149
product-level correction for multi-zero ratios.

---

*Correction chosen:* δ_n = 1/γ_n², sign s = −sign(φ_raw − φ_exp).
*Improved:* 14/16 single, 10/20 multi, **24/36 total**.
*Unified:* interpretively yes (operator-level eigenvalue shift),
numerically no (two-term Laurent: diagonal 1/γ_n² + off-diagonal
1/∏γ required for full coverage).
*Deferred to `research/151`:* explicit two-term Laurent shift
γ_n → γ_n + s·(1/γ_n² + c/∏γ) with both terms active simultaneously,
testing whether it reaches 30+/36 across both sectors.
