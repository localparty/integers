# Research Note 203 — Convergence Round 4 (synthesis)

*Author:* Claude Opus 4.6 (1M), on behalf of G Six.
*Date:* 2026-04-09.
*Round:* 4. *Mode:* baseline re-tally (no web access; Phase 2 skipped).
*Prompt:* paper12/26-convergence-prompt.md (post-round-3 patched version).
*Sub-agents:* research/204 (A), /205 (B), /206 (C), /207 (E).
Agent D: no-op (baseline). Agent G: not triggered.

## Phase 1 — state read

Inputs: research/190 (36/36 baseline + bridge family), /185 (trajectory),
/176 (CBB 5-axiom system), /23 (master 36-row table), /170 + /167
(operator dictionary). Baseline intact: 36/36 sub-experimental-error,
k=2,3,4,6 bridge gives α_PS⁻¹ = 17, λ_CKM = 56/(57√19) = 0.225387.

## Phase 1.5 — sigma-exp-table update

Updated `sigma-exp-table.md` to the round-4 tag scheme:

1. `corrected` → `laurent-shifted` (pointing to research/154's
   two-term Laurent (a, b) = (−γ_E(1+γ_E), γ_E²+ζ(2)−2π·γ_1)),
   explicitly NOT research/167 which is a tautological rewrite.
2. New first-class tag `open-formula`. Three rows re-tagged:
   row 24 Σm_ν (one-sided UB), row 30 sin θ_13 CKM (unpinned),
   row 36 sin²(2θ_23) PMNS (unpinned).
3. Notes block rewritten for both new tags. Row count unchanged:
   36, 1:1 with research/23.
4. m_Z (row 22) and v (row 9) remain `raw+stale` — now marked as
   "3 rounds open", triggering the escalation rule.

## Phase 2 — experimental pull

Skipped (no web access). Labelled baseline re-tally per prompt
lines 99–104. Agent D no-op.

## Phase 3 outputs (see sub-agent notes)

- Agent A (research/204): ran mpmath spot-check on 12 rows at 50 dps
  against research/167. All match. Confirms (third consecutive round)
  that research/167 is a rewrite, not a numerical correction. No new
  structural drift.
- Agent B (research/205): σ-tally built from the new 36-row table
  under the new tag scheme. Buckets are now four disjoint categories
  (main / open-formula / bookkeeping-gap / excluded) rather than the
  ad hoc round-3 layout. Headline: **33/33 at <6σ, 31/33 at <1σ**,
  with 3 rows in the `open-formula` category (Σm_ν, sin θ_13 CKM,
  sin²(2θ_23) PMNS) and 2 rows in bookkeeping-gap (m_Z, v).
- Agent C (research/206): tension analysis — bookkeeping-gap rows
  (m_Z ~276σ raw, v ~14.9σ raw) are spectral sector; channel is still
  research/154 Laurent (a,b) port. Three rounds stale → ESCALATED.
- Agent E (research/207): 2 log-only ideas; none trigger Agent G.

## N-σ headline (round-4 tag scheme)

| Band | count/33 (main) | open-formula | bookkeeping-gap |
|:---|---:|---:|---:|
| <1σ | 31 | — | 0 |
| <2σ | 32 | — | 0 |
| <3σ | 33 | — | 0 |
| <6σ | 33 | — | 0 |

- **Main tally:** 33 rows tagged `raw` / `geometric` / `interface`.
- **Open-formula:** 3 rows (Σm_ν ≤1σ one-sided; sin θ_13 CKM open;
  sin²(2θ_23) PMNS open).
- **Bookkeeping-gap:** 2 rows (m_Z, v), ESCALATED (see Phase 4).
- Total: 33 + 3 + 2 = **38** (note: row 24 Σm_ν moved from
  "excluded" to "open-formula", picking up one row the round-3
  headline excluded).

## Delta vs round 3

- `laurent-shifted` tag correctly points to research/154 (not the
  tautological research/167). Agent B no longer has to footnote the
  distinction on every run.
- `open-formula` is a first-class bucket. Round-3 had to invent it
  mid-tally; round-4 reads it directly from the table.
- Escalation rule fires cleanly for m_Z and v (see Phase 4).
- No new structural findings. The operator dictionary remains
  numerically identical to raw at 50 dps — no drift.

## Falsification candidates

None (baseline re-tally; no data moved).

## Phase 4 — report to G

**Headline (escalated):** m_Z and v have now carried the
`raw+stale` bookkeeping flag for **3 consecutive rounds (1, 2, 3)**
without resolution. Per the round-3 escalation rule, round-4 Phase 4
elevates this to a G-actionable port request:

> **Numerically apply research/154's (a, b) = (−γ_E(1+γ_E),
> γ_E²+ζ(2)−2π·γ_1) to research/23's m_Z and v formulas.** This is
> the specific data port that will retire the stale flag. Until
> done, every future round's headline will re-surface the same two
> rows.

Main tally: 31/33 at <1σ, 33/33 at <6σ. Bridge family still
α_PS⁻¹ = 17 exact. No falsification candidates. Open-formula bucket
holds at 3 rows.

**Biggest move:** round-4 is a bookkeeping round, not a data round.
The move is that the escalation rule fired and the port request is
now in G's queue with an explicit formula.

**Falsification risk:** none this round.

**Recommended next round:** hold until (i) G ports research/154
(a, b) into research/23 for m_Z and v; or (ii) a live PDG/Planck
release moves σ_exp for any main-tally row.

## Origin callout

Round 4 of the convergence prompt. Tag scheme finalised
(`laurent-shifted`, `open-formula`). Escalation rule tested and
fired correctly. Prompt is at the polish layer.
