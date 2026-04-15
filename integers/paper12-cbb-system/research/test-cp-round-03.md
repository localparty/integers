# Meta-report: Convergence Prompt Round 3 Test

*Test of `integers/paper12-cbb-system/26-convergence-prompt.md` (post-round-2 patch), round 3.*
*Tester:* Claude Opus 4.6 (1M), 2026-04-09.
*Round 3 output:* research/198 (+ sub-agents 199/200/201/202), updated
`sigma-exp-table.md`.

## 1. Did the prompt run end-to-end?
**Yes.** Phase 1 (read state), 1.5 (update table), 2 (fallback), 3
(A/B/C/E; D no-op; F synthesis), 4 (G report) all cleanly. No
tester-invented steps. Numbering rule unambiguous: max=197, so
synthesis = 198, sub-agents 199–202.

## 2. Was the sigma-exp-table.md update clean? formula_source column?
**Yes, clean.** The round-2 table had 40 rows with no
`formula_source`. Rewrote to exactly 36 rows, 1:1 with research/23's
master sector tally (A9+B3+C12+C-aux3+D-CKM6+D-PMNS3). Added
`formula_source` column with {raw, raw+stale, raw (open), corrected,
geometric, interface}. Auxiliary rows (Σm_ν companion, Δm², E sector,
α_PS⁻¹=17) moved to a companion slot. Column worked: Agent B
consumed it directly and the bookkeeping-gap separation fell out
without on-the-fly invention.

## 3. Did Agent A use research/167 corrected forms?
**Yes — and the check surfaced a substantive finding.** research/167
§3 is a tautological rewrite: every "Op value" matches the raw γ_n
value to 50 dps by construction. So "corrected" = "raw" numerically
for every row currently in research/167. The m_Z and v stale rows
are *not* fixed by "use research/167"; they need research/154's
Laurent (a, b) numerically ported. See research/199.

## 4. Did the σ-tally cleanly separate corrected/raw rows?
**Yes.** Agent B (research/200) reports four disjoint buckets:
main tally (34 rows, 31<1σ, 34<3σ, 34<6σ), excluded (2: Σm_ν
one-sided, sin²(2θ_23) open), bookkeeping-gap (2: m_Z, v
raw+stale), and open-formula (sin θ_13 CKM). Headline readable in
one line.

## 5. Output quality vs round 2
**8/10, up from 7/10. Delta +1.**
Improvements: 1:1 row alignment enforced; formula_source in place;
bookkeeping-gap no longer invented mid-run; Agent A sanity-check
ran and surfaced a real structural finding (research/167 is a
rewrite, not a correction). Held back: still no live mpmath run;
research/154 port still pending; no web data.

## 6. NEW issues surfaced (top 3)
1. **"corrected" category is empty by construction.** The prompt
   defines `corrected = operator-dictionary form in research/167`,
   but research/167 is a tautological rewrite at 50 dps. The
   category only becomes live after research/154 (a, b) Laurent
   values are ported. Fix: prompt should either redefine
   `corrected` to mean `research/154-shifted`, or add a fifth tag
   `laurent-shifted`.
2. **open-formula rows have no formal column.** sin θ_13 CKM and
   sin²(2θ_23) PMNS are marked `open` in research/23 but the
   Phase 3 Agent B spec lists only <N-σ bands and exclusion.
   Round 3 had to invent `open-formula` as a bucket.
3. **Bookkeeping-gap stagnation has no escalation rule.** Two
   rounds in a row, m_Z and v sit in the gap column without
   escalation. Prompt should add: "if a row stays bookkeeping-
   gap for ≥2 rounds, elevate to Phase 4 headline G-attention."

## 7. Single biggest remaining weakness
**research/154 Laurent (a, b) values have never been numerically
ported into research/23 or research/167.** This is the only thing
standing between the prompt and a clean "36/36 <Nσ" headline. It's
a ~half-day data job for G, not a prompt fix. Until done, every
future round will re-flag m_Z and v and the convergence prompt
cannot ship a one-line clean tally.

---

## Summary line
Round 2 → Round 3: row alignment and formula_source column locked;
σ-tally cleanly segmented; Agent A sanity check surfaced the real
gap (research/167 is rewrite not correction). 7→8/10.
