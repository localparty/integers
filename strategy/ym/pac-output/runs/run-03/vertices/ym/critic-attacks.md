
# Critic Attacks — B_bare review (run-03)

*Critic pass on the author's ym-clay-bare.md draft. Attack surface: bare-discipline violations (prose paragraphs), uncited claims, SILENT J-W requirements, missing DELTA-10 fields, page-count overruns, factual errors against compliance-map.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Summary

- **Total attacks raised**: 9
- **Bare-discipline violations suspected**: 3 (all minor)
- **Factual/citation dissent**: 4
- **Structural framing**: 2
- **Uncited claims**: 0
- **SILENT J-W requirements**: 0
- **DELTA-10 field gaps**: 0
- **Page count**: 367 lines — well under 600-line cap (WARN threshold); PASS

---

## Attack 1 — §1 "Clay Rules §5d" sentence (BARE-DISCIPLINE)

**Location**: §1, final paragraph of Implicit requirements.

**Author text**: "Clay Rules §5d: a submission must ADDRESS each specific mathematical question. Silence fails §5d; transparent named wall with attempted bypass satisfies §5d."

**Attack**: This is explanatory commentary, not a theorem/definition/number. Belongs in the internal brief, not B_bare. Proposed action: DELETE the sentence. §5d compliance is a meta-statement about submission strategy, not a math theorem.

**Alternative framing**: Keep but minimize — fold into §3 Requirements Map caption as "(§5d compliance: PASS per run-02 commit-memo.md)".

## Attack 2 — §2 proof paragraph "Assemble Theorems ..." (BARE-DISCIPLINE)

**Location**: §2 Theorem 2.1 proof line.

**Author text**: "Assemble Theorems 5.1, 6.1, 7.1, 8.1, 9.1, 10.1, 11.1, 11.2, 12.1, 13.1 below. Combined chain: ..."

**Attack**: Bare discipline requires *Proof:* lines that cite programme papers with §-level precision. "Assemble Theorems X, Y, Z below" is internal cross-reference, not a citation. The brief §3 template shows: `*Proof:* See §§5-13 below. Combined via [programme paper reference].` — author's line is compliant but verbose.

**Alternative framing**: Compress to: `*Proof.* §§5-13; paper08-yang-mills Theorem I.4.1 + chain L1-L18; Step 18' bypass per h4-capacitor-bypass/closure/closure-digest.md 2026-04-13.  $\square$`

## Attack 3 — §7 Remark 7.2 (BARE-DISCIPLINE)

**Location**: §7, after Theorem 7.1 proof.

**Author text**: "**Remark 7.2.** *The reconstructed Wightman theory is formulated on the gauge-invariant observable algebra ... Strocchi 2013 Ch.7).*"

**Attack**: A Remark explaining WHY the construction avoids indefinite-metric issues is prose-in-italics. Bare discipline per DELTA 3 says "prose proof details in prose" are disallowed. A remark is soft prose.

**Alternative framing**: Either delete the Remark entirely (it is explanatory) or convert to a numbered Definition-style statement. Arbiter must decide.

## Attack 4 — §10 "Status" line (BARE-DISCIPLINE)

**Location**: §10 Theorem 10.1 status indicator.

**Author text**: "*Status.* **OPEN-BUT-ADDRESSED** (conditional on H4; addressed unconditionally via Step 18' bypass, audit pending)."

**Attack**: Borderline — it IS a declaration, not prose. But "audit pending" is slightly narrative. Could be tightened to just: "Status: OPEN-BUT-ADDRESSED (H4; see §10 NAMED WALL W1 table)."

**Alternative framing**: Tighten as above. Arbiter decides.

## Attack 5 — §3 Requirements Map Req 1 cell "L2-L7, L14" (FACTUAL)

**Location**: §3 table Row 1.

**Author text**: "Req 1: Addressing layers L2-L7, L14 (7 P-cells / 13 Pa-cells; 0 SILENT; 100 % non-SILENT)"

**Attack**: Per compliance-map.md §2 re-count (exact), Req 1 P-cells are L2, L3, L4, L5, L6, L7, L14 = 7 (correct), and the remaining 13 are Pa-cells. 100 % non-SILENT is correct. But the hyphen-range "L2-L7" miswrites — L1, L1b are Pa not P in Req 1. The phrasing "L2-L7" looks like P cells are L2,L3,L4,L5,L6,L7 which is correct; +L14 = 7 total P-cells. Phrasing is technically accurate.

**Arbiter decision needed**: Keep. No error.

## Attack 6 — §3 Requirements Map Req 4 "centralized" comment (BARE-DISCIPLINE)

**Location**: §3 table cell, Req 4.

**Author text**: "L16, L17 (2 P / 2 Pa / 16 S — centralized)"

**Attack**: The word "centralized" is an interpretive comment, not a data field. Tables in bare mode should be data-only.

**Alternative framing**: Drop "— centralized" across Req 4, Req 6, Req 7 rows. Numbers speak for themselves.

## Attack 7 — §13 non-triviality signatures (FACTUAL)

**Location**: §13 Theorem 13.1 proof.

**Author text**: "*(i) String tension $\sigma > 0$* (p8§04 Theorem 4, area-law bound from cluster expansion)."

**Attack**: Theorem 4 of §04 is "Lattice mass gap" (p8§04 line 749). The area-law theorem is in Appendix F (§17 Appendix F-area-law-mass-gap.md) — the run-02 compliance map cites p8F for area law. Verify the correct citation.

**Alternative framing**: Change citation to "p8§04 Theorem 4 (lattice mass gap); p8F (area-law derivation)" or "paper08 Appendix F area-law mass gap". Arbiter should verify.

## Attack 8 — §16 Numbers Table entry 3 (FACTUAL)

**Location**: §16 Numbers Table row 3.

**Author text**: "Convergence sum: $\sum_k g_k^4(a_k\Lambda)^s \leq 10^{-3}$"

**Attack**: Per p8R§51 III and §05 Theorem 8 numerical table at row $k=0$: first-term bound is $1.0\times 10^{-2}$ (per §05 Theorem 8 proof (b)), and the cumulative sum bound from p8R§51 III eq. is $\sum g^4(a\Lambda)^4 \leq 10^{-3}$ (given in research/51 line 96). So $10^{-3}$ is the cumulative bound for $s=4$, and $10^{-2}$ is the first-term bound for $s=2$ (Corollary 8.2). Author mixes these.

**Alternative framing**: Entry 3: "Convergence sum: $\sum g_k^4(a_k\Lambda)^4 \leq 10^{-3}$ (research/51 §III eq.); $\sum g_k^4(a_k\Lambda)^2 \leq 10^{-2}$ dominated at $k=0$ (§05 Thm 8(b) numerical)". Both citations needed.

## Attack 9 — §14.1 ASCII dependency graph (FACTUAL)

**Location**: §14.1 dependency graph.

**Author text**: shows `L2 ── UV stability (Balaban; p11 K.4)` with L3, L4, L5 as sub-nodes.

**Attack**: Per PROOF-CHAIN.md, L3 has `Depends on: --` (literature, not L2); L4 depends on L2, L3; L5 depends on L4. The author's tree shows L3, L4, L5 all as direct children of L2. Structurally inaccurate.

**Alternative framing**: Correct the graph to show L3 as sibling of L2 (both literature), L4 depends on L2+L3, L5 depends on L4. OR accept the current simplification as a "block" view — but annotate.

---

## Structural attacks

### Attack 10 (STRUCTURAL) — §11 Remark 12.2 misplaced

**Location**: §12 Remark 12.2 (group data from p8K.1).

**Author text**: "**Remark 12.2** (group data, from p8K.1). *SU(N): $h^\vee=N$, ...*"

**Attack**: The data belongs in §16 Numbers Table, not as a Remark in §12 (which repeats the content of Numbers Table rows 8, 9, 10 — redundancy). Either delete Remark 12.2 or delete Numbers Table entries 8-10.

**Alternative framing**: Delete Remark 12.2; keep Numbers Table entries as the canonical locus.

### Attack 11 (STRUCTURAL) — §14.2-§14.4 histograms repeat X-RAY.md content

**Location**: §14 Proof-Chain Analytics subsections.

**Author text**: Three histograms (face, projection, pattern) reproduced from X-RAY.md.

**Attack**: These are reproduced verbatim; are they needed in B_bare or should B_bare point to X-RAY.md as the authoritative source? Brief §14 template says "RIGIDITY contribution / SYMMETRY contribution / Compliance matrix [reference]" — the histograms are a reasonable inclusion, but could be compressed.

**Arbiter decision needed**: Keep (they are analytics; bare includes analytics). No action.

---

## Verdict counts proposed

| Attack | Class | Critic proposes | Probable arbiter |
|--------|-------|-----------------|------------------|
| 1 | BARE | DELETE §5d sentence | DELETE |
| 2 | BARE | Compress proof line | COMPRESS |
| 3 | BARE | DELETE/convert Remark 7.2 | KEEP (single-sentence definitional) |
| 4 | BARE | Tighten Status line | KEEP (one-liner ok) |
| 5 | FACT | Keep (no error) | KEEP |
| 6 | BARE | Drop "— centralized" | DROP |
| 7 | FACT | Add Appendix F citation | ADD |
| 8 | FACT | Split $s=2$ vs $s=4$ in entry 3 | SPLIT |
| 9 | FACT | Correct tree structure | CORRECT |
| 10 | STRUCT | Delete Remark 12.2 OR Numbers entries 8-10 | DELETE Remark 12.2 |
| 11 | STRUCT | Keep histograms | KEEP |

---

*End of critic attacks.*
