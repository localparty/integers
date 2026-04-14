
# Arbiter Decisions — B_bare review (run-03)

*Arbiter's rulings on the 11 critic attacks. Each decision cites bare discipline DELTA 3, citation discipline DELTA 8, H4 disclosure DELTA 10, or compliance-map ground truth.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Global finding

Author's draft is **PUBLISH-READY** with 6 small edits applied. No SILENT J-W requirement, no missing DELTA-10 fields, every claim cited, page count 367 lines (well under 600-line WARN threshold).

---

## Decisions

### Attack 1 — §1 "Clay Rules §5d" sentence

**Ruling**: **DELETE** (critic wins).

**Reason**: Interpretive commentary. DELTA 3 disallows "note that" / explanatory text. §5d compliance is captured in §3 Requirements Map caption and §15. Not needed in §1.

**Edit**: Remove the sentence "Clay Rules §5d: ..." from §1.

**Rejected alternative**: Author's phrasing was a useful signal to Clay referee — but the signal is redundant with §3 and §10 H4 disclosure.

### Attack 2 — §2 proof paragraph

**Ruling**: **COMPRESS** (critic wins).

**Reason**: Brief §3 template shows brief proof-line format. Author's line is 3 sentences; compress to 1.

**Edit**: Replace the Theorem 2.1 proof line with one-liner: `*Proof.* §§5-13; paper08-yang-mills Theorem I.4.1 (universal mass gap) + chain L1-L18 of PROOF-CHAIN.md; Step 18' bypass per h4-capacitor-bypass/closure/closure-digest.md (2026-04-13). $\square$`

**Rejected alternative**: Author's fuller phrasing provided narrative context — but bare discipline drops narrative.

### Attack 3 — §7 Remark 7.2

**Ruling**: **KEEP** (author wins).

**Reason**: Remark 7.2 is a single-sentence factual note about WHERE the Wightman theory lives (gauge-invariant observable algebra); this is definitional, not explanatory. The citation "Strocchi 2013 Ch.7" is inherited via paper08 §05 (author cites p8§05 pp.2696-2712). Bare discipline permits Remarks that state fact with citation; forbids "we note that" narrative.

**Edit**: No change.

**Rejected alternative**: Critic wanted to delete for brevity. But factual content is load-bearing (indefinite-metric avoidance matters for gauge-theory Wightman).

### Attack 4 — §10 Status line

**Ruling**: **KEEP** (author wins).

**Reason**: Single-line verdict indicator, not prose. Format acceptable.

**Edit**: No change.

**Rejected alternative**: Critic's tightening would remove "audit pending" signal. That signal is part of DELTA 10 disclosure discipline and belongs here.

### Attack 5 — §3 Row 1 phrasing

**Ruling**: **KEEP** (concurrent — no dispute).

**Edit**: No change.

### Attack 6 — §3 table "— centralized" labels

**Ruling**: **DROP** (critic wins).

**Reason**: Data-only tables per bare discipline. Interpretive labels belong in §14 Analytics or the compliance-map.md itself.

**Edit**: Remove "— centralized" from Req 4, Req 6, Req 7 rows.

### Attack 7 — §13 signature (i) area-law citation

**Ruling**: **ADD Appendix F citation** (critic wins).

**Reason**: Area-law proof is in paper08 Appendix F (preprint/sections/F-area-law-mass-gap.md). Theorem 4 of §04 is the cluster-expansion lattice mass gap; area law (implying $\sigma>0$) flows through Appendix F and feeds the non-triviality proposition.

**Edit**: Change "(p8§04 Theorem 4, area-law bound from cluster expansion)" to "(p8§04 Theorem 4 lattice mass gap; p8 Appendix F area-law proof)".

### Attack 8 — §16 entry 3 convergence sum

**Ruling**: **SPLIT** (critic wins).

**Reason**: Two distinct bounds ($s=2$ vs $s=4$) at different programme locations. Accuracy matters.

**Edit**: Replace entry 3 with two sub-rows: "3a: $\sum g_k^4(a_k\Lambda)^4 \leq 10^{-3}$ (p8R§51 III eq.)" and "3b: $\sum g_k^4(a_k\Lambda)^2 \leq 10^{-2}$ dominated at $k=0$; doubly exponential convergence (p8§05 Thm 8(b) numerical)".

### Attack 9 — §14.1 ASCII tree

**Ruling**: **CORRECT** (critic wins).

**Reason**: PROOF-CHAIN.md is authoritative: L3 depends on nothing (literature); L4 depends on L2, L3; L5 depends on L4. Author's tree is structurally inaccurate.

**Edit**: Rewrite the L2-L5 block to show dependency correctly:
```
L2 ── UV stability (Balaban; p11 K.4)   [literature]
L3 ── κ k-indep                         [literature; independent of L2]
L4 ── (B1) analyticity ◄── L2 + L3
L5 ── (B2) SL(N,C) ext ◄── L4
```

### Attack 10 — Remark 12.2 vs Numbers Table

**Ruling**: **DELETE Remark 12.2** (critic wins).

**Reason**: Numbers Table rows 8, 9, 10 are the canonical locus. Remark repeats data.

**Edit**: Delete "**Remark 12.2**" block at end of §12.

### Attack 11 — Histograms in §14

**Ruling**: **KEEP** (author wins).

**Reason**: Brief §14 template explicitly asks for RIGIDITY / SYMMETRY metrics and compliance matrix. Histograms ARE the analytics. Not prose.

**Edit**: No change.

---

## Summary of edits to apply

1. §1: DELETE "Clay Rules §5d: ..." sentence.
2. §2: COMPRESS Theorem 2.1 proof line to one-liner.
3. §3: DROP "— centralized" labels from Req 4/6/7 rows.
4. §13: ADD Appendix F citation to signature (i).
5. §16: SPLIT entry 3 into 3a and 3b.
6. §14.1: CORRECT L2-L5 dependency structure in ASCII tree.
7. §12: DELETE Remark 12.2.

## Verdict

**PUBLISH-READY** after 7 edits applied. No SILENT J-W requirement; H4 fully disclosed with 9 DELTA-10 fields; page count well under 15-page target; every claim cited.

---

*End of arbiter decisions.*
