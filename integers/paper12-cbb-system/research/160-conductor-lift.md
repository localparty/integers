# Research 160 — Conductor Lift on the Nine PDG-Precision Stragglers

*Follow-up to research/154 (9 stragglers isolated), research/156 (KK
and Frobenius averaging both falsified), research/19 thread 3g/§4
(conductor-lifting map from bare BC eigenstates to gauge-decorated
eigenstates).*

*Date:* 2026-04-09
*Author:* Claude Opus 4.6 (1M ctx), with G Six.

---

## 1. Hypothesis

Research/19 §4.1 notes that the bare Riemann zeros γ_n carry conductor
N = 1 — the Galois action is trivial on them. A non-trivial correction
appears only after tensoring with a gauge-decoration whose Dirichlet
character has a larger conductor N(γ_n). The natural leading-order
conductor-lift correction to a formula is multiplicative:

    F_lift(γ_n) = F(γ_n) · (1 + ε · log N(γ_n) / γ_n)

with ε an O(1) global coefficient and N(γ_n) the conductor of the
Dirichlet L-function attached to the dominant gauge orbit of |γ_n⟩ in
the formula.

## 2. Conductor assignments

Using the research/19 §5 matching table and the gauge decoration of
each observable:

| # | Observable   | Dominant γ_n | N(γ_n) | Origin of conductor       |
|:-:|:---          |:---          |:-:     |:---                       |
| 1 | m_τ          | γ_8 = 43.327 | 8      | SU(3) adjoint orbit       |
| 2 | m_μ          | γ_6 = 37.586 | 6      | Z_6 center orbit          |
| 3 | m_Z          | γ_11 = 52.970| 11     | non-gauge / mass sector   |
| 4 | m_H          | γ_6 = 37.586 | 6      | Z_6 EW sector             |
| 5 | m_W/m_Z      | γ_6 = 37.586 | 6      | Z_6 EW sector             |
| 6 | v (Higgs VEV)| γ_10 = 49.774| 10     | excited EW sector         |
| 7 | 1/α          | γ_4 = 30.425 | 4      | EW-unbroken orbit (1+3)   |
| 8 | m_τ/m_μ      | γ_8 = 43.327 | 8      | lepton hierarchy / SU(3)  |
| 9 | sin θ_12 CKM | γ_12 = 56.446| 12     | PMNS/CKM flavour orbit    |

## 3. Global fit

Residuals (%) from research/154 Table 3 and research/156 §1. Global ε
minimising Σ|residual after correction| over the 9 stragglers:

    ε* ≈ −0.05

The log N / γ ratios span only 0.037–0.048 (a factor 1.3), so the
correction is effectively flat at −0.22% to −0.24% across *all* 9
entries. This:

- moves every straggler by roughly the same amount,
- cannot split same-γ formulas (m_μ / m_H / m_W-m_Z all ride γ_6),
- cannot split same-N same-γ formulas (m_τ vs m_τ/m_μ, both γ_8),
- cannot reach tight PDG errors (1/α at 2·10⁻⁸, m_μ at 2·10⁻⁶,
  m_Z at 2·10⁻³) because the correction itself is ~10⁻³.

| Observable   | Residual % | Lift shift % | New resid % | Exp err % | Closed? |
|:---          |---:        |---:          |---:         |---:       |:-:      |
| m_τ          | −0.167     | −0.240       | −0.407      | 6.9·10⁻³  | no      |
| m_μ          | −0.584     | −0.238       | −0.822      | 2.2·10⁻⁶  | no      |
| m_Z          | −0.220     | −0.226       | −0.446      | 2.3·10⁻³  | no      |
| m_H          | +0.397     | −0.238       | +0.159      | 1.1·10⁻¹  | no      |
| m_W/m_Z      | −0.503     | −0.238       | −0.741      | 1.5·10⁻²  | no      |
| v            | +0.300     | −0.231       | +0.069      | 4.0·10⁻³  | no      |
| 1/α          | +0.220     | −0.228       | −0.008      | 2.3·10⁻⁸  | no      |
| m_τ/m_μ      | +0.420     | −0.240       | +0.180      | 6.0·10⁻³  | no      |
| sin θ_12 CKM | +0.499     | −0.220       | +0.279      | 1.8·10⁻¹  | no      |

Closed: **0 / 9**.

Even the most generous per-observable fit of ε (separate ε per entry)
would only close the loose-tolerance cases (m_H, sin θ_12) trivially;
the tight-PDG entries (1/α, m_μ, m_Z) are unreachable.

## 4. Why the mechanism fails

1. **log N(γ_n) / γ_n is almost constant.** For the relevant γ ∈
   [30, 60] and N ∈ [4, 12], the ratio sits in [0.037, 0.048]. No
   linear combination with a single ε can discriminate between
   observables whose residuals have mixed signs and span two orders
   of magnitude.

2. **Same γ, same N, different residual.** m_μ, m_H, m_W/m_Z all live
   on γ_6 with N = 6 yet have residuals (−0.584, +0.397, −0.503). A
   conductor lift must give them the *same* fractional shift, so it
   cannot close even two of them.

3. **PDG precision dwarfs the shift.** 1/α is known to 2·10⁻⁸; the
   smallest dimensionally-natural conductor-lift correction, ε · log 4
   / γ_4 ≈ 0.045·ε, is already O(10⁻²·ε) — five orders too coarse for
   ε of order unity, and a fine-tuned ε kills the other eight.

4. **The conductor lift is a global, slowly-varying envelope**, not a
   formula-specific correction. It cannot be the PDG-precision closure
   mechanism for the same reason KK resummation failed in research/156:
   insufficient formula-specificity.

## 5. Verdict

**The conductor lift of research/19 thread 3g does not close any of the
nine PDG-precision stragglers.**

The three a-priori candidate corrections flagged by the 147–156 arc
(two-term Laurent, KK tower / threshold, conductor lift) are now all
tested and all falsified on the nine-straggler set. The survival of
these nine observables at residuals of 10⁻³–10⁻² against experimental
errors of 10⁻⁸–10⁻¹ is a robust finding: the closure mechanism must be
something that **acts at the formula-template level** rather than as a
multiplicative envelope on γ_n.

The remaining structural candidates from research/156 §6 — (ii)
higher-KK-mode *mixing* between γ-indices, and (iii) genuine Paper-11
M⁴ × CP² × S² geometric corrections that do not factor through the BC
pole at all — are now the only surviving leads.

### One-sentence summary

The conductor lift produces an almost-flat ~−0.23% envelope across all
nine stragglers, cannot discriminate same-γ formulas, cannot reach PDG
precision for 1/α or m_μ, and closes zero of nine — eliminating the
third and last of the 147–156 arc's correction candidates and leaving
only genuine Paper-11 geometric corrections as the remaining closure
channel.

---

*Deferred to research/161:* Paper-11 M⁴ × CP² × S² geometric correction
sweep (option (iii) of research/156 §6).
