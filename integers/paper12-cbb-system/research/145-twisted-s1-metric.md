# Research 145: Twisted S¹ Relaxation — Z_n Galois Twist of the 5D Metric

*Postulate under test: "The 5D metric is the trivial product M⁴ × S¹."*
*Relaxation: M⁴ × (S¹ twisted by a Z_n Galois automorphism).*

*Authors: G Six, with Claude Opus 4.6 (postulate-relaxation agent)*
*Date: 2026-04-09*

---

## 1. Setup

The CC formula (research/05, eq. 1.1) has leading term

    log(π R_obs / ℓ_P) = γ_1 · π²/2 + corrections,

derived as the ground-state eigenvalue of H_0 = T_BC · π²/2 on the
Riemann subspace H_R. The derivation assumes the e-circle is a
**trivial** S¹: the KK momentum spectrum is p_k = k/R, k ∈ Z, and
T_BC acts through the Mellin-dual scaling generator with *no*
boundary phase.

Under a Z_n Galois twist, the circle is identified by
φ ∼ φ + 2π/n with a phase e^{2πi/n} = ω_n acting on the fiber.
Equivalently, KK momenta become p_k → (k + 1/n)/R. This is a
standard twisted-boundary-condition deformation.

## 2. Shift of the CC formula

The Mellin dual of a twist by 1/n replaces T_BC by T_BC + τ_n·1
where τ_n is a real shift determined by the character sum

    τ_n = (1/n) Σ_{j=1}^{n-1} log|1 − ω_n^j| / (π²/2).

Explicit values (computed by the Kronecker limit / product formula
Σ log|1 − ω_n^j| = log n):

| n | Σ_j log\|1−ω_n^j\| | τ_n        | τ_n · π²/2 |
|:--|:------------------|:-----------|:-----------|
| 2 | log 2 = 0.69315   | +0.14047   | +0.69315   |
| 3 | log 3 = 1.09861   | +0.07423   | +0.36620   |
| 6 | log 6 = 1.79176   | +0.06051   | +0.29863   |

The leading term of the CC formula shifts as

    γ_1 · π²/2  →  γ_1 · π²/2 + τ_n · π²/2,

*adding* a positive amount to the already-too-large leading term.
The empirical residual Δ = measured − leading = −0.00990 is
**negative**; the twist pushes the leading term **further above**
the measurement, *worsening* the match.

## 3. Residual comparison

| n | New leading | Distance from measured (69.74217094) | Worse / better |
|:--|:------------|:--------------------------------------|:---------------|
| 1 (trivial) | 69.7521 | −0.00990 (absorbed by 1/γ_m corrections at 5 ppb) | **reference** |
| 2 | 70.4452  | −0.70305 | worse by 7 × 10⁴ |
| 3 | 70.1182  | −0.37607 | worse by 4 × 10⁴ |
| 6 | 70.0507  | −0.30850 | worse by 3 × 10⁴ |

Even allowing the 1/γ_m corrections to readjust (|V_{12}|² at most
order 1), no second-order PT shift can absorb a ~0.3–0.7 upward
push: the energy gap (γ_2 − γ_1)·π²/2 ≈ 27 would require
|V_{12}|² ≈ 8–19, i.e., strongly-coupled and outside the O(1)
regime. The 5 ppb residual does **not** shrink; it blows up by
four orders of magnitude.

## 4. Graviton mass prediction

A Z_n twist of the S¹ gives the graviton zero-mode a nonzero KK
mass

    m_grav(n) = (1/n) · (1/R_obs) = (1/n) · ℏ/(c R_obs).

With R_obs ≈ 1.36 × 10²⁶ m (horizon scale), 1/R_obs ≈ 1.45 × 10⁻³³ eV.

| n | m_grav                |
|:--|:----------------------|
| 2 | 7.3 × 10⁻³⁴ eV        |
| 3 | 4.8 × 10⁻³⁴ eV        |
| 6 | 2.4 × 10⁻³⁴ eV        |

These are all well **below** the LIGO bound m_grav < 1.76 × 10⁻²³ eV
(so not excluded by graviton-dispersion tests), but also far below
any foreseeable detection threshold. The prediction is therefore
empirically unfalsifiable in the near term.

## 5. Verdict

**The twist is excluded by the CC formula**, not by graviton-mass
bounds. The trivial-S¹ postulate is *required* by the 5 ppb match:
any Z_n twist with n ∈ {2, 3, 6} adds τ_n·π²/2 ≥ 0.30 to the
leading term, pushing the prediction ~10⁴× away from the measured
log(π R_obs/ℓ_P). The best twist is n = 6 (smallest shift), but
even it fails catastrophically. No value of n shrinks the residual.

| Twist n | τ_n · π²/2 | CC residual | m_grav (eV) | Verdict |
|:--------|:-----------|:------------|:------------|:--------|
| 1 (triv)| 0          | 5 ppb       | 0           | **kept** |
| 2       | +0.693     | 0.70        | 7.3e−34     | ruled out |
| 3       | +0.366     | 0.38        | 4.8e−34     | ruled out |
| 6       | +0.299     | 0.31        | 2.4e−34     | ruled out |

**One-sentence verdict.** The trivial-product 5D metric M⁴ × S¹
survives: every Z_n Galois twist (n = 2, 3, 6) inflates the CC
residual from 5 ppb to ~10⁻¹, so the postulate is *not* relaxable
by a Galois twist of the e-circle.
