# Research Note 204 — Convergence Round 4, Agent A

*Recompute at 50 dps via the research/167 operator dictionary.*
*Baseline re-tally; trigger rule applies (cheap sanity check).*

## Method

mpmath dps=50. For each of the 36 master-table rows, evaluated the
closed-form expression from research/167 §3 and compared to (a) the
raw γ_n placeholder in research/23 and (b) the sigma-exp-table.md
central value.

## Spot-check (12 rows)

| # | Observable | Op value (50 dps) | Raw | Match |
|---:|:---|:---|:---:|:---:|
| 1 | log(πR_obs/ℓ_P) | 69.7421708...canonical | = | ✓ |
| 2 | N_eff | 3.04399... | = | ✓ |
| 3 | n_s | 0.96544... | = | ✓ |
| 9 | v [GeV] | 246.2196... (raw) | = | ✓* |
| 10 | 1/α(0) | 137.035999... | = | ✓ |
| 13 | m_τ [MeV] | 1776.860... | = | ✓ |
| 22 | m_Z [GeV] | 91.1876... (raw) | = | ✓* |
| 23 | m_W [GeV] | 80.369... | = | ✓ |
| 28 | sin θ_12 CKM | 0.22500... | = | ✓ |
| 29 | sin θ_23 CKM | 0.04182... | = | ✓ |
| 32 | J_CKM | 3.18e-5 | = | ✓ |
| 34 | sin²(2θ_12) PMNS | 0.851... | = | ✓ |

Rows 9 and 22 (starred): these are the `raw+stale` rows. research/167
returns the raw placeholder at 50 dps — it does NOT carry the
research/154 Laurent (a, b) shift. Confirmed for a third round.

## Finding (unchanged from round 3)

research/167 is a tautological rewrite of research/23 at 50 dps. The
"Rel err" column is identically 0 or 10⁻⁵¹. The `laurent-shifted` tag
therefore still has zero rows — no numerical substitution of
(a, b) = (−γ_E(1+γ_E), γ_E²+ζ(2)−2π·γ_1) exists in the corpus yet.

## Output to Agent B

Use raw γ_n values for all 36 rows. Flag rows 9 (v) and 22 (m_Z) as
`raw+stale` with 3-round-open escalation.
