# 177 — Second-Order Moduli Correction for m_τ

**Parent:** 171 (CP²×S² first-order closure, 8/9), 174 (diagonal 2nd-order RS)
**Cycle:** 8
**Date:** 2026-04-09

## 1. Setup

171 closed 8 of 9 EW stragglers with a linear moduli fit
`log O_i = log O_i^raw + Σ_k S_{ik} δμ_k` on M = 9. The holdout was m_τ
(residual +1.55e−4 vs PDG err 8.8e−5, a factor 1.8 miss). 171 §5
flagged a second-order term in τ₁, r_{S²} as the closing move. This
note tests it.

The sensitivity matrix S used here is back-solved from the 171 dependency
table and reported moduli values in 171 §2; it reproduces 171 §3
(first-order closure 8/9, m_τ residual +1.55e−4) to machine precision
as a sanity check.

## 2. Second-order extension — three ansätze

Extend the prediction to
`log O_i = log O_i^raw + S_{ik}δμ_k + ½ H_{i,jk} δμ_j δμ_k`.

**(A) Paper-11 KK on-shell Hessian**
`H_{i,jk} = κ S_{ij} S_{ik} + η δ_{jk} (S_{ij})²`, two global O(1) couplings.

Scan κ, η ∈ [−5, 5]: best at (κ, η) = (1.60, −2.20), m_τ residual
+1.52e−4 — essentially unchanged. The quadratic piece is at most
`½·(Sδμ)² ≈ ½·(2.2e−3)² ≈ 2.5e−6`, an order of magnitude below the
gap (7e−5) it must bridge.

**(B) Free amplitudes A₁₁, A₁₄, A₄₄ for (τ₁², τ₁·r_{S²}, r_{S²}²)
with flat row weighting**

Pattern weights [9, 4, 1, 1, 0.5] for [m_τ, m_μ, m_Z, m_H, v]. Best
single amplitude `A ≈ −6.7e−7` for all three columns (they become
colinear), m_τ residual +1.40e−4 — still above PDG.

**(C) Generation-differentiated quadratic weighting**

Physical KK insight: the quadratic overlap integral for leptons scales
like the generation mass squared, so the m_μ row gets `(m_μ/m_τ)² ≈
1/300 ≈ 0.031` the weight of the m_τ row. Row weights
[9, 0.031, 0.1, 0.1, 0.05] for [m_τ, m_μ, m_Z, m_H, v].

**Fitted quadratic amplitudes:**
```
A(τ₁²)      = −5.72e−6
A(τ₁·r_{S²}) = −5.72e−6
A(r_{S²}²)   = −5.72e−6
```
(degenerate — the three cols are colinear under row weighting).

## 3. Closure after second-order

| Observable | res 1st-order | res 2nd-order (C) | exp err | closed |
|---|---:|---:|---:|:---:|
| **m_τ** | +1.55e−4 | **+7.1e−7** | 8.8e−5 | **yes** |
| m_μ | −1.1e−11 | −3.3e−12 | 2.3e−8 | yes |
| m_Z | 0 | −2.7e−6 | 2.1e−5 | yes |
| m_H | 0 | −7e−15 | 1.0e−3 | yes |
| m_W/m_Z | 0 | −1e−13 | 1.5e−4 | yes |
| v | 0 | −5.0e−7 | 2.7e−5 | yes |
| 1/α | 0 | −4e−15 | 2.3e−9 | yes |
| m_τ/m_μ | −5.1e−6 | −1.1e−7 | 1.6e−5 | yes |
| sin θ₁₂ CKM | 0 | +2e−18 | 2.2e−3 | yes |

**All 9 closed** (ansatz C). Refit moduli are within 1% of 171 §2.

## 4. Verdict — qualified YES

- Ansatz (A) and (B) do **NOT** close m_τ: the O(1) Paper-11 KK
  curvature Hessian yields a 2nd-order shift of order
  `½(Sδμ)² ≈ 2e−6`, ~30× too small.
- Ansatz (C) **DOES** close m_τ (+7e−7, ~100× inside PDG err), and
  keeps the other 8 closed, but requires a generation-differentiated
  row weight for the quadratic overlap integral **and** fitted
  amplitude |A| ≈ 5.7e−6, i.e. an effective curvature coefficient
  `κ_eff = A / (δτ₁)² ≈ −3.7e−4`, **not** O(1).

The closing move is therefore a tiny, generation-selective 2nd-order
operator, not the naive Paper-11 Kähler Hessian. Two physical
candidates worth pursuing:

1. **Yukawa-hierarchy suppression.** The second-order KK overlap
   integral carries an extra `(m_gen / M_KK)²` from the internal
   wavefunction bending; only the τ row gets an O(1) effect.
2. **m_τ alone needs a Paper-12 CM-L contribution** (see 172), not a
   geometric correction at all — the ×30 mismatch in ansatz (A) is the
   fingerprint of a non-moduli effect.

The pure Paper-11 moduli picture of 171 is **not enough** to bring
m_τ below PDG with O(1) coefficients. The 8/9 closure of 171 is
preserved at second order, but full 9/9 closure requires either new
physics input (generation-dependent KK weighting, candidate 1) or
switching m_τ to the CM-L channel (candidate 2, 172).

## 5. Numbers summary

- **m_τ residual, first-order (171):** +1.55e−4 (NO)
- **m_τ residual, 2nd-order ansatz (A), κ,η free:** +1.52e−4 (NO)
- **m_τ residual, 2nd-order ansatz (B), flat weights:** +1.40e−4 (NO)
- **m_τ residual, 2nd-order ansatz (C), gen-weighted:** **+7.1e−7 (YES)**
- **All 9 closed under (C):** YES
- **Effective 2nd-order coefficient under (C):** κ_eff ≈ −3.7×10⁻⁴ (not O(1))

## 6. Next

Route m_τ to 172 (CM-L L-function leptons); retest whether the last
7e−5 residual is a CM-L mass contribution. If yes, the correct Cycle-8
picture is **Paper-11 moduli closes 8 lepton-light observables;
Paper-12 CM-L closes m_τ separately**, matching the two-channel
structure of 170.
