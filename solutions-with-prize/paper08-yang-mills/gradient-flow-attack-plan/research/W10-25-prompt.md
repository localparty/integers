# W10-25: Final Read-Through and Cross-Reference Audit

## Task
Read the complete Appendix L (all sections), Appendix N, and the preprint update fragments. Verify the assembled publication text is internally consistent, complete, and ready for integration into the preprint.

## What to check (from Task 8 of the integration addendum)

### 1. Dependency chain walk
Walk the chain 1.1 → 1.2 → 1.3 → 2.2 → 3.7 → 3.8 → 3.9 → 4.1/4.2/4.3 through the L.1-L.4 sections. For each arrow, verify there is an explicit "By Lemma L.x.y" citation. Flag any lemma that uses a result without citing it.

### 2. QG5D citation consistency
Every QG5D result cited in Appendix L must point to a specific section in Appendix N. Search for: "Theorem K.1", "Theorem S.1", "Theorem 1", "Theorem U.2a", "Proposition 3.1", "Theorem 4.3", "Lemma A1/A2/A3". Each must reference "Appendix N, §N.x" — flag any that use raw Paper 1/10 references or file paths.

### 3. H4-conditional flagging
Search all L sections for mentions of: L.2, L.1(iii), Lemma 4.2, Lemma 4.3, AF match, AF form, short-distance. Verify each H4-dependent result is flagged with "Conditional on Hypothesis H4" or equivalent. Flag any unflagged conditional result.

### 4. PROOF-CHAIN consistency
Read the Steps 15-18 fragment (preprint-updates/all-updates.md Fragment 1) and verify each step's "Proved" or "Conditional" status matches what's actually proved in L.1-L.4.

### 5. Abstract/conclusion/IV.5 mutual consistency
Read Fragments 2-5 from preprint-updates/all-updates.md. Verify all three (abstract, conclusion 12.7, IV.5 update) say the same thing about what's proved unconditionally vs conditionally.

### 6. Stale language check
Search all L and N sections for: "open conjecture", "open problem", "deferred", "future work", "remains to be", "not yet". Flag any that should have been updated. (Note: "full OPE at all orders remains open" in L.4.3 is correct and should NOT be flagged.)

### 7. Notation consistency
Verify that L.1-L.4 use the same notation as the preprint: g_k, Δ̂_k, C_K, Ω_s, κ_B, m_W, ε_k. Flag any notation conflicts.

### 8. Equation numbering
Verify equation numbers within each L section are sequential and non-overlapping (L.1.1, L.1.2, ...; L.2.1, L.2.2, ...; etc.). Flag any duplicates or gaps.

### 9. Completeness check
Verify all 19 lemmas from the lemma catalog appear in L.1-L.4. Cross-check against the catalog in `strategy/01-lemmas-and-gap-strategy.md` or `W8-16-synthesis.md` Section 1.

### 10. Sub-clause coverage
Verify L.5's sub-clause resolution table matches what's actually proved in L.1-L.4. Every sub-clause (L.1(i)-(iii), L.2, L.3(i)-(v), L.4) must point to a specific lemma in a specific section.

## What to read (ALL of these)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L0-L5-L6-L7.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L1-phase1.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L2-phase2.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L3-phase3.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-L/L4-phase4.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/appendix-N/N-qg5d-infrastructure.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/preprint-updates/all-updates.md`
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W8-16-synthesis.md` (for cross-checking)

## What to write
Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W10-25-final-audit.md`

## Output format
For each of the 10 checks: PASS or ISSUE, with details for any ISSUE. Then:
- Summary table: 10 checks, PASS/ISSUE count
- List of any fixups needed (with exact file, line, and correction)
- **FINAL VERDICT: READY FOR INTEGRATION / NEEDS FIXUPS**
