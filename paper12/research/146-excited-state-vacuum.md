# Research 146: Relaxing "Vacuum = ω_1": Can an Excited-State Admixture Absorb the 5 ppb CC Residual?

*Postulate under test: the physical vacuum is the critical KMS state ω_1,
equivalently the ground state |γ_1⟩ of H_0 = T_BC·π²/2 on H_R.*
*Relaxation: |Ω⟩ = √(1−Σ|c_k|²)|γ_1⟩ + Σ_k c_k |γ_{k+1}⟩, a small
excited-state admixture. We test the minimal k=1 case (single
admixture of |γ_2⟩) against the 5 ppb CC residual and check
whether the same amplitude tightens the Higgs VEV formula
v = γ_10·π²/2 (which uses the same operator H_0).*

*Author: Claude Opus 4.6 (postulate-relaxation agent), commissioned by G Six*
*Date: 2026-04-09*

*Builds on:*
- *research/05-derive-cc-formula.md — CC formula, Rayleigh–Schrödinger setup*
- *research/81-third-order-PT-CC-formula.md — third-order PT closure*
- *preprint/12-high-precision-formulas.md — CC (5 ppb) and VEV (0.15%) numerics*

---

## 1. Setup

The unperturbed Hamiltonian on H_R is H_0 = T_BC·π²/2 with
eigenvalues E_n^{(0)} = γ_n·π²/2. Both observables of interest
are matrix elements of H_0 in some reference state:

| Observable | Operator | Reference state (postulate) |
|:-----------|:---------|:----------------------------|
| log(πR_obs/ℓ_P) (CC) | H_0 | |γ_1⟩ (ground / ω_1) |
| v (Higgs VEV, GeV)   | H_0 | |γ_10⟩ (selection rule, research/09) |

The postulate to relax is the first: instead of |Ω⟩ = |γ_1⟩ exactly,
take

$$
|\Omega\rangle \;=\; \sqrt{1-|c_1|^2}\,|\gamma_1\rangle + c_1\,|\gamma_2\rangle,
\qquad |c_1| \ll 1.
$$

## 2. First-Order Correction to the CC Formula

$$
\langle\Omega|H_0|\Omega\rangle \;=\; \gamma_1\,\frac{\pi^2}{2}
 \;+\; |c_1|^2\,(\gamma_2-\gamma_1)\,\frac{\pi^2}{2}.
$$

The admixture **raises** the expectation value (required, since the
measured log(πR/ℓ_P) = 69.74217094 exceeds the full PT formula
prediction 69.74216747 by a residual Δ_res ≈ +3.46×10⁻⁶ ≈ 5 ppb —
positive, in the right direction for an admixture to absorb).

## 3. Fitting c_1 to the CC Residual

Numerical inputs (mpmath / LMFDB):
- γ_1 = 14.134725141…,  γ_2 = 21.022039639…
- (γ_2 − γ_1)·π²/2 = 6.8873 × 4.93480 = 33.9834
- Δ_res(CC) ≈ 3.46 × 10⁻⁶ (measured minus formula, see research/05 §1 table)

Solving |c_1|²·33.9834 = 3.46×10⁻⁶:

$$
\boxed{|c_1|^2 \;=\; 1.02\times 10^{-7}, \qquad |c_1| \;=\; 3.19\times 10^{-4}.}
$$

Post-correction CC residual: **0 by construction** (this is a one-parameter
absorption of one residual). The post-fit log(πR/ℓ_P) matches to the
floor of the γ_1..γ_3 truncation.

## 4. Induced Correction to the Higgs VEV Formula

"Same operator" means H_0 acts identically on the VEV sector. The
minimal-universality ansatz: the VEV vacuum has a **c_1 admixture
of the neighbouring eigenstate** with the **same amplitude**, i.e.
|Ω_v⟩ = √(1−|c_1|²)|γ_{10}⟩ + c_1|γ_{11}⟩. Then

$$
\Delta v \;=\; |c_1|^2\,(\gamma_{11}-\gamma_{10})\,\frac{\pi^2}{2}
 \;\approx\; 1.02\times 10^{-7} \times 3.197 \times 4.9348
 \;\approx\; 1.6\times 10^{-6}\ \text{GeV}.
$$

Relative shift: Δv/v ≈ **6.5 × 10⁻⁹**.

Empirical VEV residual: v_meas − v_formula = 246 − 245.62 = **0.38 GeV
(1.5 × 10⁻³ relative)**.

The induced shift is **5–6 orders of magnitude too small** to touch
the Higgs VEV residual. Even saturating with the largest accessible
eigenvalue gap |γ_∞ − γ_10|·π²/2 / v ≈ 10⁻¹ per unit c₁², one still
needs |c_1|² ~ 10⁻² to absorb 0.15%, which is 10⁵× the CC-fitted
value and would overshoot the CC residual by the same factor.

## 5. Verdict

| Check | Result |
|:------|:-------|
| c_1 absorbs CC residual?        | YES (|c_1| = 3.19×10⁻⁴) |
| CC residual after fit           | 0 (one-parameter absorption) |
| Induced Higgs VEV shift         | +1.6×10⁻⁶ GeV (6.5×10⁻⁹ relative) |
| Closes Higgs VEV 0.15% residual?| NO (5 orders of magnitude too small) |
| Joint closure of both residuals?| **NO** |

**Verdict — POSTULATE RELAXATION REJECTED AS A UNIFIED EXPLANATION.**
A single |γ_2⟩-admixture in the Riemann-subspace vacuum can numerically
absorb the 5 ppb CC residual, but the implied |c_1|² ≈ 10⁻⁷ is far
too small (by ~10⁵) to account for the 0.15% Higgs VEV residual —
despite both observables being eigenvalues of the **same** operator
H_0 = T_BC·π²/2. The two residuals therefore have **different
physical origins**: the CC 5 ppb residual may well live in a small
vacuum excitation (or equivalently in the truncation of the PT series
at third order per research/81), but the Higgs VEV 0.15% residual is
dominated by a separate mechanism — most plausibly SM radiative
corrections to v from the KK threshold at the S¹ scale (paper 4), not
by vacuum-state impurity. The postulate "vacuum = ω_1" survives as
the leading description; if it is relaxed, the excited-state weight
is ≲ 10⁻⁷ and is effectively invisible to every other framework
formula.

## 6. Caveats

- The identification of the "CC residual" with Δ_res ≈ 3.46×10⁻⁶
  uses the three-term truncated formula of research/05 §1. Research/81
  closes that formula through third-order PT at the structural level;
  the leftover 5 ppb is already assigned there to fourth-order PT
  and/or prime-phase interference, both of which are orthogonal to a
  vacuum admixture. The calculation above is therefore *not* an
  independent new mechanism — it is an alternative (degenerate)
  parametrisation of one residual that fails the cross-check on
  the VEV.
- The VEV cross-check assumes the admixture amplitude c_1 is
  "universal" across H_R sectors. If the admixture is sector-local
  (e.g., excited only in the Riemann-subspace ground sector, not in
  the |γ_10⟩ neighbourhood), the VEV is unchanged and the postulate
  relaxation becomes vacuous (it absorbs one residual with one
  free parameter, making no prediction elsewhere). Either way the
  relaxation does **not** tighten the Higgs VEV.

---

*One free parameter closes the CC residual; the same parameter is
invisible to the Higgs VEV residual. The two residuals do not share
a common origin in a single vacuum excitation.*
