# Research Note 152 — Second-Order ζ-Laurent Correction: Negative Result

**Follow-up to `research/149-signed-zeta-pole-correction.md`.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6.

## 1. Ansatz

Research 149 left six PDG-precision stragglers uncovered by the
first-order BC pole correction `(1 + s/∏γ)`: m_τ, m_μ, m_W/m_Z, m_H,
m_t/m_W, sin θ_12 CKM. Motivated by the Laurent expansion of ζ(β) at
β=1,

    ζ(β) = 1/(β−1) + γ_E − γ_1·(β−1) + γ_2/2·(β−1)² − …,    γ_1 ≈ −0.0728

we extend the correction to

    φ → φ·(1 + s/∏γ + c/(∏γ)²)

and ask whether a **single universal c**, ideally derivable from the
Stieltjes constants, closes all six stragglers.

## 2. Per-formula fit of c

Setting the second-order-corrected residual to zero gives
`c = −(r_frac + s/∏γ)·(∏γ)²`, where `r_frac` is the raw fractional
residual. Using the `∏γ` and residuals from table §2 of research/149:

| Observable   | ∏γ      | res. after 1st-ord % | fitted c   |
|:---          |--:      |--:                   |--:         |
| m_τ          | 1773.05 | −0.16710             | +5 253     |
| m_μ          | 1773.05 | −0.58410             | +18 362    |
| m_W/m_Z      | 1237.62 | −0.50300             | +7 705     |
| m_H          |  789.89 | +0.39650             | −2 474     |
| m_t/m_W      |  430.11 | −0.07000             | +129       |
| sin θ_12 CKM | 9950.25 | +0.49855             | −493 602   |

**c is neither universal nor formula-local.** It spans four decades
(`10²`–`10⁵`), carries both signs (three + and three −), and shares no
algebraic pattern across the six entries. m_τ and m_μ even use the
*same* ∏γ=1773.05 but require c values differing by 3.5×.

## 3. Why no Laurent coefficient can close these

The ζ-Laurent coefficients at β=1 are all O(1):
`γ_E ≈ 0.5772`, `−γ_1 ≈ 0.0728`, `γ_2/2 ≈ −0.0048`, …  
Substituting any O(1) candidate c ∈ {γ_E, γ_E², −γ_1, ½, 1} into
`(1 + s/∏γ + c/(∏γ)²)` moves the residual only in the 5th–6th decimal
place, because `1/(∏γ)² ∈ [10⁻⁸, 10⁻⁵]`. The required c's are
`10²`–`10⁵` times larger than any Laurent coefficient of ζ. A
second-order Laurent correction is **numerically incapable** of
reaching PDG precision on these observables: the (∏γ)² suppression
kills it before any coefficient has a chance.

## 4. Closure check under universal c

For every candidate c ∈ {γ_E, γ_E², −γ_1, ½, 1}, **zero of six**
stragglers fall below the experimental error bar. The new residuals
are indistinguishable from the first-order residuals to four
significant figures.

## 5. Verdict

The second-order ζ-Laurent ansatz `(1 + s/∏γ + c/(∏γ)²)` **fails
decisively** as a closure mechanism for the six PDG-precision
stragglers:

1. **Not universal.** Fitted c ranges over `−5×10⁵` to `+2×10⁴`.
2. **Not Laurent-scale.** Required |c| ≫ any Stieltjes constant.
3. **Not closing.** No O(1) universal c promotes any straggler below
   experimental error.

The six stragglers are therefore **not** reachable by any polynomial
refinement of the BC pole residue in powers of `1/∏γ`. They signal
that the ζ-pole mechanism itself saturates at first order for these
observables — the residual gap must come from a *different* structure
(candidate mechanisms: KK mode mixing corrections on S¹, Frobenius
orbit-averaging at higher twist sector, or a genuinely non-ζ
contribution from the M⁴×CP²×S²×S¹ geometry).

The research 149 rule stands as stated: the BC critical tail
`(1 + s/∏γ)` is a **first-order, two-sided** correction, and six
PDG-precision observables simply lie beyond its reach. Research 153
should pivot away from Laurent refinement toward the KK / Frobenius
correction channel identified in research 142–143.

*One-sentence summary:* A second-order ζ-Laurent term cannot close
the six PDG-precision stragglers — fitted c is non-universal, spans
four decades with both signs, and any Laurent-scale universal c is
suppressed by `(∏γ)² ≳ 10⁵` to numerical irrelevance, so the closure
mechanism must come from outside the BC pole expansion.

---

*Deferred to `research/153`:* KK/Frobenius correction channel for
m_τ, m_μ, m_W/m_Z, m_H, m_t/m_W, sin θ_12 CKM.
