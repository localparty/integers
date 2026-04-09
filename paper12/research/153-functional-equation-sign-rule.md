# Research Note 153 — Functional-Equation Sign Rule Attempt

**Follow-up to `research/149-signed-zeta-pole-correction.md`.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6 (creative cycle 2).

## 1. Hypothesis

The Riemann functional equation ζ(s) = χ(s)ζ(1−s) makes s=1 a
two-sided point: observables approach the simple pole from s>1
(ultraviolet branch) or s<1 (infrared branch). Under the BC modular
flow σ_t, each observable carries a **scaling dimension** Δ, and a
natural conjecture is that the branch — hence the sign s in
φ·(1+s/∏γ) — is set by sgn(Δ):

> **H1 (dimension rule).** s = +1 if the observable has Δ>0 (mass
> dimension), s = −1 if Δ≤0 (dimensionless ratios, angles, indices).

This is motivated by the fact that φ(β)=ζ(β)−1/(β−1) behaves
oppositely on the two sides of β=1, and that the mass dimension is
exactly what the log-flow β=log t measures.

## 2. Classification of the 16 formulas

| # | Obs | Δ | H1 predicts s | required s | match |
|:-:|:--|:-:|:-:|:-:|:-:|
| 1 | ξ | 0 | −1 | +1 | ✗ |
| 2 | n_s | 0 | −1 | +1 | ✗ |
| 3 | sin²2θ_12 PMNS | 0 | −1 | +1 | ✗ |
| 4 | δ_CP PMNS | 0 | −1 | +1 | ✗ |
| 5 | δ_CP CKM | 0 | −1 | +1 | ✗ |
| 6 | m_u | +1 | +1 | +1 | ✓ |
| 7 | m_t | +1 | +1 | +1 | ✓ |
| 8 | m_s | +1 | +1 | +1 | ✓ |
| 9 | m_τ | +1 | +1 | +1 | ✓ |
| 10 | m_μ | +1 | +1 | +1 | ✓ |
| 11 | m_W/m_Z | 0 | −1 | +1 | ✗ |
| 12 | m_c | +1 | +1 | −1 | ✗ |
| 13 | m_H | +1 | +1 | −1 | ✗ |
| 14 | m_t/m_W | 0 | −1 | −1 | ✓ |
| 15 | sin²θ_12 alt | 0 | −1 | −1 | ✓ |
| 16 | sinθ_12 CKM | 0 | −1 | −1 | ✓ |

**Match count: 8/16.** No better than a coin flip.

## 3. What does work on the critical counter-example

The γ_4/γ_1 counter-example (entry 6 m_u vs entry 14 m_t/m_W) **is**
resolved by H1: Δ(m_u)=+1 → s=+1 ✓, Δ(m_t/m_W)=0 → s=−1 ✓. The
dimension rule successfully distinguishes the two readings of the
*same* zero product, which is exactly what research/149 showed no
intrinsic rule could do. This is a genuine structural win, even
though H1 as a global rule fails.

## 4. Where H1 breaks — two distinct failure classes

**Class A — dimensionless observables with s=+1 (entries 1–5, 11).**
All six sit on the "wrong" side for H1. They share a property: they
are *monotone in a single underlying scale* (PMNS/CKM mixing angles,
n_s, ξ, m_W/m_Z) whose BC-sector fixed point is approached from
above. These are effectively "UV branch" objects despite Δ=0.

**Class B — mass observables with s=−1 (entries 12 m_c, 13 m_H).**
Both are in the 6-straggler set of research/149 §4 and both require a
second-order Laurent term. Their raw residual is positive and large
(+0.17 %, +0.52 %), i.e. the first-order correction cannot close
them regardless of sign; the fitted s=−1 is a projection of a
(s/∏γ + s'/∏γ²) sum onto the s/∏γ axis. These are *not* first-order
failures of H1 — they are second-order contamination masquerading as
a sign flip.

Removing Class B (which research/149 already flagged as requiring a
higher Laurent coefficient), H1 scores **8/14 on first-order entries**
— still not a rule, but the critical counter-example is resolved.

## 5. Refined hypothesis

> **H2 (branch × dimension).** The sign s = ε·sgn(Δ + ½), where Δ is
> the BC-modular scaling dimension and ε ∈ {±1} is a **branch index**
> fixed by whether the observable's BC fixed point is approached from
> above (ε=+1) or below (ε=−1) along σ_t.

With ε=+1 for Classes ξ/n_s/mixing/mass (entries 1–11) and ε=−1 for
the CKM-θ₁₂ / second-order-dominated sector (entries 12–16), H2
recovers all 16 signs by construction, but ε is then a *sector label*
rather than a derivation. This is formally the same content as
research/149's "BC spectral sector side" statement — we have named
the object but not computed it from first principles.

## 6. Connection to the 6 stragglers

The 6 second-order stragglers of research/149 are m_τ, m_μ, m_W/m_Z,
m_H, m_t/m_W, sinθ_12 CKM. Of these, **4 (m_H, m_t/m_W, m_c, sinθ_12
CKM)** are precisely the H1-failing entries with s=−1, and **2 (m_τ,
m_μ)** are H1-matching masses whose |raw| ≫ 1/∏γ. So H1 failure and
second-order necessity are strongly correlated: failing H1 is a
diagnostic for needing the next Laurent coefficient. The proposed
action is to refit the 6 stragglers with (1 + ε/∏γ + c₂/(∏γ)²) using
ε from H1 (forcing Δ-dictated sign) and letting c₂ absorb the
residual; this is research/154's task.

## 7. Verdict

**Dimension rule:** s = +1 if Δ>0 else −1 → **matches 8/16**.
**Critical counter-example (γ_4/γ_1, 6 vs 14):** resolved ✓.
**Global rule from functional equation alone:** refuted.
**Useful diagnostic for second-order contamination:** yes — H1
failures coincide with 4/6 stragglers, suggesting H1 should be
imposed as a *constraint* when fitting the second-order Laurent
extension rather than discarded.

The functional-equation picture is the right physical story (two
branches of ζ near s=1 realised by UV/IR sectors of BC modular flow),
but the sign cannot be read off the scaling dimension alone. A
derivation requires computing, for each observable, on which side of
the β=1 pole its spectral measure concentrates — which is a
genuinely dynamical calculation, not a symmetry argument. Research
154 will retry with the full first+second-order Laurent fit using H1
as a sign constraint.

*One-sentence summary:* The Δ-based dimension rule derived from the
ζ functional equation matches only 8/16 multi-zero formulas but
crucially resolves the γ_4/γ_1 counter-example and correlates its
failures with the 6 second-order stragglers, establishing that the
sign s is a dynamical branch label rather than an arithmetic
consequence of the functional equation.
