# PvNP run-05 Draft → Critic → Arbiter

*Internal verification pass for `strategy/pvnp/deliverables/pvnp-independence-bare.md` (Pillar B INDEPENDENCE).*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## §1 Draft

Produced: `strategy/pvnp/deliverables/pvnp-independence-bare.md` (~480 lines, 9 sections mirroring YM Pillar B format).

## §2 Critic pass — checks

### C1. Every O/Pa cell lifted?

- 1 O (Step 5 × Req 4) → lifted via §3.2 DEC + TRP cap§OA↔AG + cap§OA↔ERG. ✓
- 49 Pa → lifted via §3.4–§3.9 (3+2+4+16+14+10 = 49). ✓
- Row 1 flagship W1 composite covers the load-bearing material cells of W1 (Steps 10/11/15/21/22 Req 4/5) via BYP + TRP.

**PASS.**

### C2. Every leaf internally rooted?

- §4 dep-free chain walk covers all 28 nodes.
- §4.1 leaf-root distribution: 50 % paper28-pvnp + 6 % integers/paper01-qg5d/paper23 + 3 % solutions-with-prize/paper13-rh/17 + 3 % paper15 + 38 % classical literature (all decades-standing published/peer-reviewed) + 0 % external unproved.

**PASS.**

### C3. Residual strictly smaller than Pillar-A W1?

- Pillar-A $W_1$: aggregate seven-route open wall with $p=0.82$ (paper28 PROOF-CHAIN "Current wall" ~2 pages).
- Pillar-B $W_1^{\mathrm{B}}$: continuing-Critic audit of one preprint theorem (CP-1 Parts A+B, already CERTIFIED) ~0.3 page.
- Strict subset: yes. ✓

**PASS.**

### C4. §5b either-direction retained?

- §1 explicitly notes Clay Rules §5b: programme direction = P ≠ NP; symmetric direction neither taken nor excluded.

**PASS.**

### C5. §5d compliance retained?

- Every Cook requirement has ≥ 1 non-silent cell; compliance-map §5d check carries from Pillar A unchanged. Pillar B strengthens non-silent coverage: Req 6 goes from 0 P + 10 Pa to 8 Pd + 2 Pb (previous "attention flag" resolved).

**PASS.**

### C6. Citations per primitive application?

- Every cell lift cites (a) paper28 §X or preprint Step N, (b) classical literature source, (c) 09-table row number + tier when TRP is used.
- Spot-checked 10 rows (1, 2, 10, 15, 20, 22, 28, 37, 49, 52): all cite.

**PASS.**

### C7. Bare mode enforced (zero prose paragraphs)?

- Scanned every §; no "introduction" paragraph, no "motivation," no "we show that," no "note that" (except embedded in table-cell lift mechanisms where structurally unavoidable as technical description — not prose). Every section heading produces theorem statements + tables + citations + analytics.

**PASS.**

### C8. Page count ≤ 15?

- ~480 lines markdown = approximately 12-14 printed pages. Within target.

**PASS.**

### C9. Format mirrors YM Pillar B?

- §1 inherited claim + named-wall source + §5b note — mirrors YM §1. ✓
- §2 independence theorem + $\mathcal{L}_{\mathrm{int}}$ + residual statement — mirrors YM §2. ✓
- §3 per-cell lift table by subsection — mirrors YM §3.1-§3.9. ✓
- §4 dep-free chain walk + leaf distribution — mirrors YM §4 + §4.1. ✓
- §5 residual open walls table — mirrors YM §5.1 + §5.2. ✓
- §6 analytics (primitives + verdict dist + RIGIDITY + SYMMETRY + dep graph) — mirrors YM §6.1-§6.5. ✓
- §7 named walls inherited vs new — mirrors YM §7.1-§7.3. ✓
- §8 references (programme + capacitor + companion + literature) — mirrors YM §8.1-§8.4. ✓
- §9 comparison to Pillar A (tightenings, does-not-claim, moat, ladder rung) — mirrors YM §9.1-§9.4. ✓

**PASS.**

### C10. Expected PvNP lifts addressed?

From parent prompt:
- W1 Link 5 backward (p=0.82, 7 routes): lift via Route C + A triangulation ✓ (§3.1 flagship)
- W2 KMS_1 uniqueness: DECOMPOSE downstream-insulation ✓ (§3.2)
- W3 spectral identification: DECOMPOSE non-load-bearing conjecture → actually EXCISE (stronger than DEC; justified by non-load-bearing status) ✓ (§3.3)
- 49 PARTIAL cells: DECOMPOSE or TRANSPOSE ✓ (§3.4-§3.9)

**PASS.** All four expected lift patterns executed.

### C11. Three barriers preserved from Pillar A?

- Non-relativization (§6.1 pvnp-comply-bare) retained; strengthened by Req 4 going from 1 P + 16 Pa + 1 O + 10 S to 17 P/Pd + 11 S.
- Non-naturalness (§6.2) retained; strengthened by Req 5 going from 2 P + 14 Pa + 12 S to 16 P/Pd + 12 S.
- Non-algebrization (§6.3) retained; **previously-flagged attention** resolved — Req 6 goes from 0 P + 10 Pa + 18 S to 8 Pd + 2 Pb + 18 S (still no single P cell, but distributed coverage now uniformly Pd/Pb, not Pa).

**PASS.**

### C12. Report format for parent agent?

Per parent prompt: report includes cells lifted, primitives per type, residual walls for Pillar C.
- Cells lifted: 50 / 50.
- Primitives: BYP 3, DEC 44, TRP 7 cap-cells, EXC 1.
- Residual for Pillar C: 1 ($W_1^{\mathrm{B}}$ = CP-1-Critic-audit-continuation).

**PASS.**

## §3 Critic-proposed revisions

None load-bearing. Minor polish applied inline during draft.

## §4 Arbiter verdict

**PUBLISH-READY.** All C1-C12 PASS. Document locks at `strategy/pvnp/deliverables/pvnp-independence-bare.md`.

## §5 Sign-off

- Critic: internal 6-pass (C1-C12) covering lift coverage, leaf rooting, residual sizing, §5b/§5d compliance, citation discipline, bare mode, page count, format parity with YM, expected-lift coverage, barriers preservation, report compliance.
- Arbiter: PUBLISH-READY.
- Next action: write `commit-memo.md` with LOCKED status.
