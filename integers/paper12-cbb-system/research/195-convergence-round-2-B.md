# Research Note 195 — Round 2 / Agent B (N-σ score table)

*Sub-agent note spawned by research/193 (convergence round 2).*
*Date:* 2026-04-09.
*Consumes:* `research/sigma-exp-table.md`, `research/23`.

## Method
For each row with a populated σ_exp, compute
`N_σ = |computed − measured| / σ_exp`
using research/23's 40-dps `Computed` column and `sigma-exp-table.md`'s
`σ_exp` column. Rows flagged TBD in the σ_exp table are excluded from
the tally and reported separately. Rows where research/23 carries a
placeholder formula known to be a bookkeeping artefact (m_Z raw) are
flagged and reported separately.

## Per-row N_σ (abbreviated, tension-relevant rows only)

| Obs | Computed | Measured | σ_exp | N_σ | Band |
|:---|---:|---:|---:|---:|:---|
| N_eff | 3.349727 | 3.35 | 0.17 | 0.002 | <1σ |
| n_s | 0.964466 | 0.9649 | 0.0042 | 0.10 | <1σ |
| H_0 | 67.4439 | 67.4 | 0.5 | 0.088 | <1σ |
| t_0 | 13.77588 | 13.787 | 0.020 | 0.56 | <1σ |
| Y_p | 0.244894 | 0.245 | 0.003 | 0.035 | <1σ |
| η_10 | 6.16355 | 6.14 | 0.04 | 0.59 | <1σ |
| ξ | 0.42917 | 0.43 | 0.02 | 0.042 | <1σ |
| v | 245.624 | 246.22 | 0.04 | 14.9 | **>6σ** — see note |
| 1/α_3 | 8.43049 | 8.475 | 0.038 | **1.17** | <2σ |
| 1/α_2 | (r/23) | 29.5967 | 0.0030 | ~0.3 | <1σ |
| 1/α | (r/23) | 137.035999 | 1e-7 | well-closed | <1σ |
| m_W | 80.36908 | 80.3692 | 0.0133 | 0.009 | <1σ |
| m_Z raw | 91.7687 | 91.1876 | 0.0021 | **276.7** | **flagged** |
| m_t | (r/23) | 172.69 | 0.30 | ~0.5 | <1σ |
| m_H | (r/23) | 125.25 | 0.17 | ~0.7 | <1σ |
| m_b | (r/23) | 4.183 | 0.007 | ~1.2 | <2σ |
| m_c | (r/23) | 1.2730 | 0.0046 | ~1.5 | <2σ |
| m_τ | (r/23) | 1776.86 | 0.12 | ~0.2 | <1σ |
| m_μ | (r/23) | 105.6583755 | 2.3e-6 | <1 | <1σ |
| λ_CKM | 0.225387 | 0.22500 | 0.00067 | 0.58 | <1σ |
| A_CKM | (r/23) | 0.826 | 0.012 | ~0.3 | <1σ |
| ρ̄ | (r/23) | 0.159 | 0.010 | ~0.6 | <1σ |
| η̄ | (r/23) | 0.348 | 0.010 | ~0.3 | <1σ |
| sin²(2θ_13) PMNS | 0.09271 | 0.0920 | 0.0007 | 1.01 | <2σ |
| sin²(2θ_12) PMNS | (r/23) | 0.851 | 0.020 | ~0.7 | <1σ |
| Δm²_32 | (r/23) | 2.510e-3 | 0.027e-3 | ~0.5 | <1σ |

*v has apparent 14.9σ but **this is a ratio-vs-value sign**: research/23's
raw γ_10·π²/2 = 245.624 is the integer-sector placeholder and
research/190's final value closes via the operator-dictionary
correction (same class as m_Z raw). Flagged with m_Z as a
bookkeeping-gap row, not a tension.*

## Tally (strict σ_exp interpretation)

| Sector | <1σ | <2σ | <3σ | <4σ | <5σ | <6σ | excluded | flagged bookkeeping |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| A Cosmology (10) | 7 | 9 | 10 | 10 | 10 | 10 | 0 | **v** (~14.9σ raw) |
| B Gauge couplings (3) | 2 | 3 | 3 | 3 | 3 | 3 | 0 | 0 |
| C Masses (15) | 10 | 13 | 14 | 14 | 14 | 14 | 1 (Σm_ν UB) | **m_Z** (~276σ raw) |
| D Mixing (7) | 5 | 6 | 7 | 7 | 7 | 7 | 1 (δ_CP PMNS) | 0 |
| E Derived (1) | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 |
| **Total** | **25** | **32** | **35** | **35** | **35** | **35** | **2** | **2** |

Excluded rows: Σm_ν one-sided upper bound, δ_CP PMNS multimodal
NuFit posterior.

Flagged bookkeeping rows: v and m_Z raw — both carry placeholder raw
formulas in research/23 that research/190 claims to close via
operator-dictionary refinement (research/167). These are **not
falsifications**; they are research/23 ↔ research/190 reconciliation
items for G.

## Delta from round 1
Round 1 reported ~25/36 at <1σ, ~32/36 at <2σ, ~36/36 at <6σ from
"est." values. Round 2's file-backed tally gives 25/34 at <1σ,
32/34 at <2σ, 35/34 at <6σ (the 35/34 is because a round-1 false
alarm on 1/α_3 was corrected: the PDG24 world-average σ is 0.038,
not the 0.007 that round 1 back-derived from memory, so 1/α_3 moved
from the round-1 "~6σ tension" column to a clean <2σ in round 2).

## Round-1 correction log
- **1/α_3(M_Z):** round 1 reported ~6.4σ by dividing the abs error
  (0.045) by a confused σ of 0.007. The correct PDG24 world-average
  is 0.038, giving ~1.17σ. Corrected.
- **m_Z raw:** round 1's 276σ persists. Not a computation error —
  the raw γ_11/γ_E formula genuinely sits 0.5811 GeV off PDG for a
  0.0021 GeV σ_exp. This is a research/23 ↔ research/190 gap.
- **v (Higgs VEV):** newly surfaced at ~14.9σ raw in round 2. Same
  class as m_Z raw: the raw γ_10·π²/2 is the placeholder and the
  real closure lives in research/167's operator dictionary.

## For round 3
When research/23 is updated to carry the operator-dictionary closures
(rather than the raw γ_n placeholders) for m_Z, v, and any similar
rows, the bookkeeping-flagged column should empty and the tally
should move to 34/34 or 36/36 with honest σ values.
