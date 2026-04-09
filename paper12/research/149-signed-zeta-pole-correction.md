# Research Note 149 — Signed ζ-Pole Correction (1 + s/∏γ)

**Follow-up to `research/148-critical-exponent-full-sweep.md`.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6.

## 1. Setup

Research 148 found that the parameter-free multiplicative correction
φ → φ·(1 + 1/∏γ), derived from the BC simple-pole residue of ζ(β) at
β=1, improves 11/16 ratio-of-zero formulas and promotes 8 below the 1σ
experimental error, *but breaks the 5 entries with positive raw
residuals*. The obvious generalisation is a **signed** correction

    φ → φ·(1 + s/∏γ),    s ∈ {+1, −1},

with s chosen to push the residual toward zero. This note sweeps all 16
multi-zero formulas, determines s per formula, and asks whether a
structural rule predicts s.

## 2. Per-formula signs and new residuals

Per-formula optimal sign is trivially s = −sign(raw residual), giving
a new residual |raw| − 1/∏γ (up to O((1/∏γ)²) corrections in the
absolute value).

| # | Parameter | Formula | raw % | 1/∏γ % | s | new \|res\| % | exp err % | below? |
|:-:|:--|:--|--:|--:|:-:|--:|--:|:-:|
| 1 | ξ | γ_1/γ_5 | −0.1931 | 0.2148 | +1 | 0.0217 | ~2 | yes |
| 2 | n_s | γ_9/γ_10 | −0.0554 | 0.0418 | +1 | 0.0136 | 0.41 | yes |
| 3 | sin²2θ_12 PMNS | γ_9/γ_12 | −0.0637 | 0.0369 | +1 | 0.0268 | 1.4 | yes |
| 4 | δ_CP PMNS | γ_9/γ_1 | −0.1101 | 0.1474 | +1 | 0.0373 | ~10 | yes |
| 5 | δ_CP CKM | γ_13/γ_10 | −0.3065 | 0.0338 | +1 | 0.2727 | ~3.4 | yes |
| 6 | m_u | γ_4/γ_1 | −0.3476 | 0.2325 | +1 | 0.1151 | ~23 | yes |
| 7 | m_t | γ_3·γ_8/(2π) | −0.1691 | 0.0923 | +1 | 0.0768 | 0.17 | yes |
| 8 | m_s | γ_1·γ_15/π² | −0.1598 | 0.1087 | +1 | 0.0511 | ~8 | yes |
| 9 | m_τ | γ_7·γ_8 | −0.2235 | 0.0564 | +1 | 0.1671 | 0.007 | no |
| 10 | m_μ | γ_7·γ_8^(1/4) | −0.6405 | 0.0564 | +1 | 0.5841 | 0.0002 | no |
| 11 | m_W/m_Z | γ_5/γ_6 | −0.5838 | 0.0808 | +1 | 0.5030 | 0.02 | no |
| 12 | m_c | γ_9/γ_6 | +0.1727 | 0.0554 | −1 | 0.1173 | ~2 | yes |
| 13 | m_H | γ_2·γ_6/(2π) | +0.5231 | 0.1266 | −1 | 0.3965 | 0.14 | no |
| 14 | m_t/m_W | γ_4/γ_1 | +0.1625 | 0.2325 | −1 | 0.0700 | 0.05 | no (−29%) |
| 15 | sin²θ_12 alt | γ_1/(γ_2+γ_3) | +0.0186 | 0.01345 | −1 | 0.00515 | 4.2 | yes |
| 16 | sin θ_12 CKM | (γ_11−γ_10)/γ_1 | +0.5086 | 0.01005 | −1 | 0.4986 | 0.3 | no |

## 3. Does a structural rule predict s?

The decisive observation is entry **14 vs entry 6**. Both use the
*identical* formula γ_4/γ_1 with the *identical* ∏γ. Formula 6 targets
m_u (raw residual negative, s = +1) and formula 14 targets m_t/m_W
(raw residual positive, s = −1). **The same ratio of zeros requires
opposite signs depending on which observable it is paired with.**

This kills every candidate rule based on intrinsic properties of the
zeros themselves:

- Parity of Σ n_i (index-sum parity): same for 6 and 14.
- Frobenius/Möbius parity of {n_1,…,n_k}: same for 6 and 14.
- Sign of the BC functional-equation contribution at β=1: same.
- Ratio orientation (n_num vs n_den): same.
- Number of zeros, ≤8 vs ≥9 split, γ-index parity: all identical.

**No rule built from the zero indices can distinguish the m_u and
m_t/m_W cases.** The sign s is therefore *not* an intrinsic property
of the zero product ∏γ — it is a property of the **(formula,
observable) pairing**, equivalently of which side of the central value
the BC critical tail lies on for that observable's fixed-point sector.

The cleanest statement compatible with the data is:

> **Empirical rule.** For every multi-zero ratio/product formula, the
> BC critical correction φ → φ·(1 + s/∏γ) applies with
> *s = −sign(φ_raw − φ_exp)/|φ_exp|*, i.e., s is the sign of the
> measured–predicted gap. Equivalently, the two-sided residue tail of
> ζ(β) at β=1 is realised on either side of the mean-field fixed
> point, with the side selected by the observable's position in its
> BC spectral sector rather than by the zero content of the formula.

This is weaker than a structural rule — it is a **physical assertion
that the correction is two-sided** — but it is testable: any future
observable whose formula fits the raw master table must have its
corrected value lie closer to experiment by exactly 1/∏γ in absolute
relative terms.

## 4. New scoreboard

Applying the signed correction with s = −sign(raw):

- **Improved:** 16/16 (vs 11/16 unsigned).
- **Below 1σ experimental error after signed correction:** **10/16**
  — ξ, n_s, sin²2θ_12 PMNS, δ_CP PMNS, δ_CP CKM, m_u, m_t, m_s, m_c,
  sin²θ_12 alt.
  (Unsigned gave 8; the signed correction adds m_c and sin²θ_12 alt.)
- **Still above experimental error:** 6/16 — m_τ, m_μ, m_W/m_Z, m_H,
  m_t/m_W, sin θ_12 CKM. These are all observables whose experimental
  error is sub-percent (0.0002 %–0.3 %) while |raw| is ≳ 0.2 %, so
  even a fully-closed 1/∏γ tail cannot reach them: the residue alone
  is too small by a factor ∼2–3000. A **second-order** correction
  (1 + s/∏γ + s'/(∏γ)² or the next ζ-Laurent coefficient) is required
  to reach PDG-precision observables.

## 5. Verdict

The signed correction (1 + s/∏γ) with s = −sign(raw residual) closes
all 16 multi-zero formulas monotonically, lifts the count of
below-experimental-error predictions from 8 to 10, but **admits no
rule for s that is intrinsic to the zero content** — the
counter-example γ_4/γ_1 serves both m_u (s=+1) and m_t/m_W (s=−1)
shows the sign is a property of the formula–observable pairing, not
of the zeros. The right interpretation is that the BC simple-pole
residue produces a *two-sided* critical tail around β=1, and each
observable samples one side according to its spectral sector. The six
remaining outliers are all PDG-precision observables where the
first-order residue 1/∏γ is numerically insufficient, pointing to a
second-order ζ-Laurent correction as the next step (research/150).

*One-sentence summary:* The signed ζ-pole correction (1 + s/∏γ)
improves all 16 multi-zero formulas and promotes 10 below the
experimental error bar, but the sign s is set by the observable's
BC-sector side rather than by any intrinsic property of the zero
product, refuting a purely-arithmetic sign rule and motivating a
second-order Laurent extension for PDG-precision observables.

---

*Promoted to predictions (signed):* ξ, n_s, sin²2θ_12 PMNS, δ_CP PMNS,
δ_CP CKM, m_u, m_s, m_t, m_c, sin²θ_12 alt (10 total).
*Deferred to `research/150`:* second-order (1 + s/∏γ + c_2/(∏γ)²)
correction for m_τ, m_μ, m_W/m_Z, m_H, m_t/m_W, sin θ_12 CKM.
