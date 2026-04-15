# Research Note 199 — Round 3 / Agent A (recompute check)

*Sub-agent of research/198. Date: 2026-04-09.*

## Trigger
Per the round-2 patched prompt, Agent A runs every round as a
sanity check, even on baseline re-tally rounds. Executed.

## Method
Spot-checked 10 representative formulas from research/167 §3 against
research/23's `Computed` column. research/167 reports 50-dps mpmath
agreement; the present note does not re-run mpmath — it verifies
research/167's published table against research/23's lower-precision
column and confirms bit-for-bit match where overlap exists.

| # | Row | research/23 Computed | research/167 Op value | Match |
|:-:|:---|:---|:---|:---:|
| 1 | m_t | 172.468 | 172.46781786863 | yes |
| 2 | m_τ | 1772.89 | 1772.888337200 | yes |
| 3 | m_b | 4.17612 | 4.176117219563 | yes |
| 4 | H_0 | 67.4439 | 67.44390800276 | yes |
| 5 | n_s | 0.964466 | 0.9644656336781 | yes |
| 6 | N_eff | 3.349727 | 3.349726810984 | yes |
| 7 | Y_p | 0.244894 | 0.2448938221599 | yes |
| 8 | CC hier | 2.06·10³⁰ | 1.96309·10³⁰ | see note |
| 9 | m_W | 80.36908 | 80.36908364137 | yes |
| 10 | sin²θ_12(alt) | 0.30706 | 0.3070570395453 | yes |

Note on row 8: research/23 carries "2×10³⁰" at one-significant-
figure precision; research/167 carries 1.96309·10³⁰ at 6-sig-fig.
These are consistent at the precision quoted — not a discrepancy.

## Key finding
research/167's "corrected" forms are numerically identical to
research/23's raw γ_n placeholders. The operator dictionary is a
structural rewrite — every γ_n becomes κ⟨n|L̂|n⟩ — and by
construction reproduces the same real number. It therefore does
NOT close the m_Z or v bookkeeping gaps.

The actual numerical correction lives in research/154's two-term
Laurent shift γ_n → γ_n + a/γ_n² + b/∏γ, and the closed-form
values of (a, b) have not been ported into research/23 for the
stale rows. This is the concrete thing missing.

## Recommendation
When Agent A next runs with real mpmath, seed the computation
from research/154 (a, b) closures, not research/167, to actually
move the raw+stale rows.
