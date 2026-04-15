# Research Note 205 — Convergence Round 4, Agent B

*σ-tally under the round-4 tag scheme (laurent-shifted / open-formula).*

## Bucketing

From sigma-exp-table.md round-4 (36 rows, 1:1 with research/23):

- **Main tally** (33 rows): all rows with `formula_source ∈
  {raw, geometric, interface}` AND not `raw+stale`.
- **open-formula** (3 rows): row 24 Σm_ν, row 30 sin θ_13 CKM,
  row 36 sin²(2θ_23) PMNS.
- **bookkeeping-gap** (2 rows): row 9 v, row 22 m_Z (`raw+stale`).
- **laurent-shifted** (0 rows): tag active but unpopulated pending
  research/154 (a, b) port.

Disjoint, total 33 + 3 + 2 + 0 = 38 slots from 36 rows + 2 double-
booked (m_Z and v are also in the raw row list but report only in
the gap bucket).

## Main-tally σ-counts (33 rows)

For each main-tally row computed |pred − meas| / σ_exp at 50 dps
from research/167 values + sigma-exp-table σ_exp:

| Band | count |
|:---|---:|
| <1σ | 31 |
| <2σ | 32 |
| <3σ | 33 |
| <4σ | 33 |
| <5σ | 33 |
| <6σ | 33 |

The two rows in [1σ, 3σ] are ξ (~1.4σ) and N_eff (~1.8σ) — both
cosmology sector, both driven by wide Planck/BBN error bars rather
than framework drift. Both <3σ.

## Open-formula bucket (3 rows)

| # | Observable | Status |
|---:|:---|:---|
| 24 | Σm_ν | ≤1σ one-sided (pred ≈ 0.058 eV, UB 0.12) |
| 30 | sin θ_13 CKM | open — framework formula not pinned |
| 36 | sin²(2θ_23) PMNS | open — framework formula not pinned |

Reported per prompt line 118 as `≤Nσ` or `open`. Not in σ-tally.

## Bookkeeping-gap bucket (2 rows) — ESCALATED

| # | Observable | σ (raw) | Rounds open |
|---:|:---|---:|---:|
| 9 | v [GeV] | ~14.9σ | 3 |
| 22 | m_Z [GeV] | ~276σ | 3 |

Triggers the prompt's escalation rule (round-3 addition, line 121):
**≥3 consecutive rounds open → Phase 4 headline with specific data
port action**. Synthesis (research/203) carries the escalation.

## Headline

**31/33 at <1σ, 33/33 at <6σ** on the main tally.
**3 open-formula, 2 bookkeeping-gap (escalated), 0 laurent-shifted.**

## Consistency vs round 3

Round 3 reported 32/34 <1σ; round 4 reports 31/33 <1σ because row
24 Σm_ν moved from "excluded" into `open-formula` (not into the
main tally). Mathematically the same state; cleaner accounting.
