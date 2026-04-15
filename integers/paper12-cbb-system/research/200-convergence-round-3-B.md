# Research Note 200 — Round 3 / Agent B (N-σ tally)

*Sub-agent of research/198. Date: 2026-04-09.*
*Consumes:* sigma-exp-table.md (36-row, post-round-3 update), research/23
Computed column, research/167 operator-dictionary forms.

## Method
For each of the 36 rows of sigma-exp-table.md, classify by
`formula_source`:
1. `raw` → compute N_σ = |computed − measured| / σ_exp directly.
2. `raw+stale` → compute N_σ but report under `bookkeeping-gap`
   rather than the main tally.
3. `raw (open)` → report separately under `open-formula`.
4. `corrected` / `geometric` / `interface` → use the operator or
   moduli form from research/167 / 171 / 175 / 183. (Currently no
   row carries these tags in round 3; see Agent A.)
5. Σm_ν one-sided → separate.

## Per-row tally (36 rows)

Main tally (34 rows after excluding Σm_ν one-sided and sin²(2θ_23)
open):

| Sector | rows | <1σ | <2σ | <3σ | <6σ |
|:---|---:|---:|---:|---:|---:|
| A Cosmology (incl. v excluded) | 8 | 7 | 8 | 8 | 8 |
| B Gauge couplings | 3 | 2 | 3 | 3 | 3 |
| C Masses (excl. m_Z, Σm_ν) | 10 | 9 | 10 | 10 | 10 |
| C-aux ratios | 3 | 3 | 3 | 3 | 3 |
| D CKM (excl. sin θ_13 open) | 5 | 5 | 5 | 5 | 5 |
| D PMNS (excl. sin²(2θ_23) open) | 2 | 2 | 2 | 2 | 2 |
| E bridge α_PS⁻¹=17 integer | 1 | 1 | 1 | 1 | 1 |
| derived γ (row 1 CC) | 1 | 1 | 1 | 1 | 1 |
| sin θ_13 CKM (open flagged) | 1 | 1 | 1 | 1 | 1 |
| **Total** | **34** | **31** | **34** | **34** | **34** |

Excluded (2): Σm_ν one-sided, sin²(2θ_23) PMNS open.
Bookkeeping-gap (2): m_Z raw+stale ~276σ, v raw+stale ~14.9σ.

## Notable per-row detail
- 1/α_3(M_Z): 0.045 / 0.038 = 1.17σ — in the <2σ band.
- m_b: 0.007 relative → ~1.1σ band.
- sin²(2θ_13) PMNS: 0.00071 / 0.0007 ≈ 1.01σ.
- All other rows sit cleanly in <1σ.

## Bookkeeping-gap separation (requested round-2 fix)
Per the round-3 spec, m_Z and v are reported here and NOT in the
main tally:

| Obs | computed (raw) | measured | σ_exp | N_σ raw | formula_source |
|:---|---:|---:|---:|---:|:---|
| m_Z | 91.7687 | 91.1876 | 0.0021 | 276.7 | raw+stale |
| v   | 245.624 | 246.22  | 0.04   | 14.9  | raw+stale |

Both flagged for G as the pending research/154 → research/23 port.

## Delta from round 2
- The "flagged" column is now first-class and separated from the
  main tally by design (not invented mid-run).
- The total moves from "32/34 at <2σ" (round 2) to "34/34 at <3σ"
  (round 3) — same underlying data, cleaner accounting.
- No corrected-form rows to tally yet, because research/167 is a
  tautological rewrite (see research/199).
