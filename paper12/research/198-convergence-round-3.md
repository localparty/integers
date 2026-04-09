# Research Note 198 — Convergence Round 3 (synthesis)

*Author:* Claude Opus 4.6 (1M), on behalf of G Six.
*Date:* 2026-04-09.
*Round:* 3. *Mode:* baseline re-tally (no web access; Phase 2 skipped).
*Prompt:* paper12/26-convergence-prompt.md (round-2 patched version).
*Sub-agents:* research/199 (A), /200 (B), /201 (C), /202 (E).
Agent D: no-op (baseline). Agent G: not triggered.

## Phase 1 — state read
Inputs read: research/190, /185, /176, /23, /170, /167. Baseline is
36/36 sub-experimental-error; bridge family k=2,3,4,6 gives α_PS⁻¹=17
exact and λ_CKM = 56/(57√19).

## Phase 1.5 — sigma-exp-table update
`sigma-exp-table.md` existed from round 2 with 40 rows and no
`formula_source` column. Updated to the round-3 spec: exactly 36
rows 1:1 with research/23, `formula_source` column added with values
{raw, raw+stale, raw (open), corrected, geometric, interface}. The
auxiliary rows (Σm_ν companion, Δm² ratio, E sector, CC hierarchy,
α_PS⁻¹=17 integer) moved to a companion file slot.

## Phase 2 — experimental pull
Skipped (no web). Labelled baseline re-tally per prompt lines 99–104.

## Phase 3 outputs (see sub-agent notes)
- Agent A (research/199): ran per the round-2 trigger rule. Spot-
  checked 10 rows against research/167's 50-dps values; all match
  to full precision. Confirms operator-dictionary is numerically
  identical to raw γ_n placeholders for every row tested.
- Agent B (research/200): σ-tally built from the new 36-row
  sigma-exp-table.md, strictly separating `raw+stale`, `open`, and
  `corrected`/`raw` rows. Headline: **32/34 at <1σ, 34/34 at <6σ**,
  with 2 rows excluded (Σm_ν one-sided, sin²(2θ_23) open) and 2
  rows bookkeeping-flagged (m_Z raw+stale ~276σ, v raw+stale ~14.9σ).
- Agent C (research/201): the two bookkeeping-flagged rows (m_Z, v)
  belong to the spectral sector (γ_n operator matrix elements).
  Recommended channel: research/154 two-term Laurent V-shift
  substitution — but Agent A's check shows research/167 as currently
  written does NOT yet carry the numerical correction. This is the
  substantive finding of round 3.
- Agent E (research/202): 3 log-only ideas; none trigger Agent G.

## N-σ headline (baseline re-tally, corrected-form tally)

| Band | count/34 |
|:---|---:|
| <1σ | 32 |
| <2σ | 33 |
| <3σ | 34 |
| <6σ | 34 |

Excluded: Σm_ν (one-sided), sin²(2θ_23) PMNS (open formula).
Bookkeeping-flagged (not in tally): m_Z (~276σ raw), v (~14.9σ raw).

## Delta vs round 2
- Phase 1.5 row alignment: 40→36 rows, 1:1 with research/23. Clean.
- `formula_source` column: present and populated.
- Agent B tally is now **strictly** separated — corrected vs raw+stale
  vs open vs excluded — no more on-the-fly "flagged" column invention.
- One new substantive finding: research/167 as written is NOT a
  numerical correction. Its operator dictionary is a tautological
  rewrite of research/23 (see research/167 §3 Table, "Rel err" column
  is all 0 or 10⁻⁵¹). The m_Z and v "raw+stale" rows cannot be
  resolved by "use research/167" — they need the research/154 Laurent
  (a,b) shift ported as numerical values. This is a research/167 ↔
  research/190 gap, not a prompt bug.

## Falsification candidates
None (baseline re-tally; no data moved).

## Next round
Hold until one of: (i) G ports research/154 Laurent (a,b) into
research/23 for the stale rows; (ii) a live experimental release
moves PDG/Planck values; (iii) research/167 is extended with the
V-shift closed form.
