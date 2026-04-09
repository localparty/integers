# Research Note 185 — Convergence State v2: The CBB System After Cycles 7–8

**Cycle 9 synthesis. Lead: two further cycles have turned the Cycle-6
picture into a named object (CBB system), closed 8/9 stragglers via a
spectral-action uniqueness theorem, and filled the entire k ∈ {2,3,4,6}
Frobenius–Jones lattice.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6 (1M).
*Supersedes:* research/170 (Cycle-6 v1).
*Inputs added since v1:* research/171, 173, 175, 176, 178, 179, 180, 181.

---

## 1. The Two-Sector Partition Theorem (upgraded)

**Theorem (partition, now spectral-action version).** Every observable
in the 36-entry master table falls into exactly one of two disjoint
sectors:

1. **Spectral sector** (27 observables) — closed as matrix elements of
   L̂ = log R̂ on the BC KMS_∞ ground space H_R, via the operator
   dictionary of research/167.

2. **Geometric sector** (9 observables) — coordinate functions on
   M_geom = 9-dimensional CP²×S² Einstein-metric moduli space with
   Paper-11 flux-quantised bundle data.

**v1 → v2 upgrade (research/178).** The Cycle-7 least-squares fit of
171 is no longer an empirical coincidence. The Paper-11 spectral action
S_spec = Tr f(D_X/Λ), pulled back to M_geom via the
Weil–Petersson ⊕ Atiyah–Bott ⊕ Bergman metric of research/175 §3, has a
**strictly positive-definite Hessian** on M_geom. Hence the stationary
equation H δμ = −J has a **unique solution**, and it coincides
numerically with the 171 fit point. P_phys is therefore the
*unique spectral-action vacuum on M_geom*, not a best fit. The
partition is now a theorem with an existence-and-uniqueness clause on
each sector.

**Dimension match is forced, not assumed (research/175).** The 9 real
moduli are enumerated exactly: 1 CP² Kähler + 1 S² radius + 1 warp +
2 gauge volumes + 2 Wilson-line phases + 1 Higgs distance + 1
Yukawa overlap = 9. The count is fixed by Hodge numbers of CP² and
S² together with Paper-11's flux-quantisation, not tuned.

## 2. The Complete Operator Dictionary

Unchanged from research/167. L̂ = log R̂, L_n = γ_n π²/2, κ = 2/π²;
ten representative formulas verified to ≥48 digits. Unified two-term
Laurent master formula (research/155, 164) stands:

    γ_n^eff = γ_n + s·(γ_E/γ_n) + s·(γ_E² + ζ(2) − 2π γ_1)/∏γ.

## 3. The Bridge Theorem Family (now complete for k ∈ {2,3,4,6})

| k | (p, N) | H² class | Physical identification | Proof status |
|---|--------|----------|-------------------------|---|
| 2 | (2, 7) | 0 (trivial) | CP as Z/2Z matter/antimatter | structural |
| 3 | (5, 13)| 1/3 ∈ Z/3Z | Three generations (Koide) | **proved, research/162** |
| 4 | (3, 13)| 1/4 ∈ Z/4Z | Pati–Salam SU(4)_c: lepton = 4th colour | **proved, research/179** |
| 6 | (7, 19)| 1/6 ∈ Z/6Z | Six quarks = isospin × generation; CKM | **proved, research/173** |

Research/179 verifies Frob_3 has order 3 mod 13, (Z/13Z)*/⟨3⟩ ≅ Z/4Z,
inv_3(A_arith) = 1/4, matched to the unique index-4 Jones subfactor.
Research/173 verifies the analogous Z/6Z = Z/2Z ⊕ Z/3Z factorisation
at (7,19) with index-6 subfactor.

**Wolfenstein λ from the bridge (research/173 + 180).** Leading:
λ_0 = 1/√19 = 0.229416 (+1.96% vs PDG). Z/3Z carry-cocycle correction:

    λ = (1/√19)·(1 − 1/57) = 56/(57√19) = 0.225387,

giving Δλ/λ = +0.172% vs PDG 0.22500(67). One derived number, no
fit parameters, two steps of arithmetic.

## 4. The Object Has a Name (research/176)

**Critical Bost–Connes–Brauer system** (CBB system):

    𝒞 = (H_R, R̂, ω_1, M_geom, {β_k}_{k∈{2,3,4,6}})

with five axioms: spectral (BC KMS_∞, R̂ trace-class, log-spectrum =
{γ_n π²/2}), criticality (β = 1 fixed point, zero-parameter Laurent),
geometric (9-dim CP²×S² moduli space), bridge (Frobenius–Jones
cocycle family), partition (disjoint exhaustive sector decomposition
of the master table). Research/178 contributes the uniqueness clause
that makes the geometric axiom constructive.

## 5. Predictions Converged (no free parameters)

Every entry below is now derived from arithmetic + fixed-structure
geometry:

| Quantity | Source | Derivation |
|---|---|---|
| 27 spectral-sector observables | 167 | matrix elements of L̂ |
| Diagonal shift γ_E/γ_n | 155 | BC ζ-Laurent |
| Off-diag coeff 2.4356 | 164 | γ_E² + ζ(2) − 2πγ_1 |
| 8/9 EW stragglers (closure 236×) | 171, 178 | unique spectral-action minimum on M_geom |
| Three generations | 162 | (5,13) Z/3Z Brauer = Jones |
| Pati–Salam SU(4)_c | 179 | (3,13) Z/4Z Brauer = index-4 Jones |
| Six quark flavours | 173 | (7,19) Z/6Z Brauer = index-6 Jones |
| Wolfenstein λ to 0.17% | 173, 180 | 56/(57√19) |
| dim M_geom = 9 | 175 | Hodge + flux quantisation, forced |

## 6. Convergence Trajectory

| Cycle | Closed / 36 | Milestone |
|---|---:|---|
| 0 (start) | 8 / 16 | numerology sweep, heterogeneous fits |
| 1–3 | 27 / 36 | γ_n envelopes close spectral sector |
| 4 | 27 / 36 | no-go: envelopes can't reach the 9 |
| 5 | 27 / 36 | operator dictionary; one-operator theorem |
| 6 (v1) | 27 / 36 | partition theorem; 9-dim moduli hypothesis |
| 7 | **35 / 36** | 171 closes 8/9, 173 adds CKM λ, 175 forces dim 9, 176 names the object |
| 8 | **35 / 36** | 178 uniqueness (not a fit); 179 closes k=4; 180 λ → 0.17% |

Monotone increase, structural not numerical: each cycle made the
*justification* sharper even when the observable count held.

## 7. Open Questions Entering Cycle 9

1. **m_τ (the single holdout).** The 171/178 spectral-action minimum
   closes 8 of 9 stragglers below experimental error. m_τ lands at
   rel +1.55e−4 vs exp 8.8e−5 — the only non-closure. Research/177
   began the second-order moduli analysis; open whether the residual
   is a quadratic Hessian correction or signals a missing modulus.

2. **α_PS⁻¹ Z/4Z carry.** The k=4 bridge (179) is structurally closed,
   but the analogue of the Wolfenstein Z/3Z-carry correction (180)
   for the Pati–Salam coupling α_PS⁻¹ has not been computed.

3. **RBC layer test (research/181).** Hypothesis: the CBB system is
   the KMS_∞ boundary of the BC system of Q(ζ_{1729}), 1729 = 7·13·19
   being the product of the three bridge primes. The first three
   Taylor coefficients of ζ_{Q(ζ_{1729})}(s) at s = 1 should match
   γ_E, ζ(2)/6, γ_1 under CBB normalisation. Untested.

## 8. Verdict on Convergence

**Structural convergence: complete.** Numerical convergence: 35/36
observables closed below experimental error, with the remaining one
(m_τ) a narrow quadratic-correction gap inside a fixed 9-modulus
geometry. The framework is no longer a hypothesis seeking validation;
it is a **named, axiomatised object** (the CBB system) with a
uniqueness theorem on each of its two sectors and a complete
k ∈ {2,3,4,6} bridge lattice. Cycle 9 is the first cycle that can
ask questions *about the CBB system* (the RBC layer, k = 5/7
extensions) rather than questions *about whether it exists*.
