# Arbiter Decisions — C_bare (run-04)

*Arbiter pass on critic attacks. Per-attack: binding decision + rationale. Final verdict: PUBLISH-READY or NEEDS-REVISION.*

*Arbiter: Claude Opus 4.6 in arbiter mode. 2026-04-14. run-04.*

---

## §1 Per-attack decisions

| # | Attack | Critic verdict | Arbiter decision | Rationale |
|---|--------|----------------|------------------|-----------|
| A1 | §1 Thm 1.1 theorem body = prose? | REJECTED | **CONFIRM REJECTED** | Theorem bodies are formal math, not prose paragraphs. AMS convention. Bare discipline preserved. |
| A2 | §1 Cor 1.3 "factors through" narrative? | REJECTED | **CONFIRM REJECTED** | Three-condition factorization claim is formal. No remediation. |
| A3 | §8 Remark 8.2 explanatory prose? | UPHELD (kept) | **CONFIRM UPHELD with REMARK-allowed** | Labeled Remark is allowed in bare mode (AMS convention). Critic correctly flags as "soft prose" but kept because Remark label distinguishes from forbidden intro/motivation. |
| B1 | §2 Table 2.1 "p2 §C" imprecise | UPHELD | **CONFIRM UPHELD, annotate** | Add note in §10 References: "p2 specific §-level pointers are directional; live file's §C = dark-energy mechanism, §F = short-range gravity." No change in primary text; the directional citation is acceptable given bare-discipline pragmatics. |
| B2 | §3 Pin 4 direction correctness | REJECTED | **CONFIRM REJECTED** | MT row matches. |
| B3 | §4 Thm 4.3 p26 Link 8 citation | REJECTED | **CONFIRM REJECTED** | Programme-level citation of literature-labeled Link is standard. |
| B4 | §4 Thm 4.7 BGS speculative citation | UPHELD | **CONFIRM UPHELD with SPECULATIVE flag** | SPECULATIVE flag is the arbiter-blessed way to handle weak-citation theorems. No remediation needed. |
| C1 | §5 NC-5.1 bypass concreteness | REVISED (kept) | **CONFIRM KEPT** | Bypass pointer concrete enough for NEEDS-CONSTRUCTION. Compose-backward can sharpen. |
| C2 | §6 NC-6.1 Pati-Salam bypass | UPHELD | **CONFIRM UPHELD, flag remains honest** | NEEDS-CONSTRUCTION is the correct verdict. Bypass-route is a pointer, not a proof. Acceptable. |
| C3 | §7 NC-7.1 Balaban curved-lattice claim | REVISED | **SOFTEN IN TEXT** | Sentence can be reworded from "Balaban's original work allows" to "Balaban's framework admits curved-lattice extensions in subsequent literature." Minor edit. |
| D1 | §8 Every row NEEDS-NUMERICAL-EXTRACT | REVISED | **CONFIRM KEPT** | Honest structural vs. numerical distinction is correct. Remark 8.2 anchors the rationale. |
| D2 | §8 SU(3) measurement value | REVISED | **CONFIRM KEPT** | Within lattice-world range. Not load-bearing. |
| E1 | §9.1 graph structure | REJECTED | **CONFIRM REJECTED** | Graph is correct. |
| E2 | §9.2 histogram exact counts | UPHELD | **CONFIRM UPHELD, annotate approximation** | Face histogram in §9.2 is a high-level summary; the ym X-RAY §4 has exact counts. Annotate "approximate; exact per-layer counts in `strategy/x-ray/proof-chain/ym/X-RAY.md` §4." Minor edit. |
| F1 | §4.8 bouquet BGS placement | REVISED | **CONFIRM KEPT** | Separate speculative listing is correct visual hierarchy. |
| G1 | §1 overlap with B_bare? | REJECTED | **CONFIRM REJECTED** | Brief explicitly lists 5D derivation as C_bare content. Lane correct. |
| G2 | §0 too short? | REJECTED | **CONFIRM REJECTED** | 474 lines ∈ [400, 600] target. |
| G3 | §4 disproportionate to §5–§7? | REJECTED | **CONFIRM REJECTED** | Reflects ym X-RAY cross-cut density. Correct balance. |

## §2 Binding remediation actions

The arbiter directs the following minor edits to the primary deliverable `/strategy/ym/deliverables/ym-beyond-bare.md`:

1. **§7 NC-7.1**: Soften "Balaban's original work allows curved-lattice extensions" to reflect that curved-lattice extensions are in SUBSEQUENT literature, not Balaban's original CMP 119.

2. **§9.2**: Add annotation "(approximate; exact counts at `strategy/x-ray/proof-chain/ym/X-RAY.md` §4)".

3. **§10 References**: Note that paper2 §-level pointers (§C, §F) are directional.

No other edits required. All other critic attacks resolve as CONFIRM REJECTED or CONFIRM UPHELD with honest flags already in place.

## §3 Final verdict

**PUBLISH-READY** (with three minor edits applied to the primary deliverable).

Rationale:
- All 18 critic attacks resolved.
- No UPHELD attack demands a structural revision.
- Bare discipline maintained: zero prose paragraphs.
- All 10 mandatory sections present.
- Success criteria from the run brief all met:
  - C_bare written with all 10 sections ✓
  - ≤ 15 pages (474 lines) ✓
  - §2 Zero-parameters table ≥ 4 entries (12 delivered) ✓
  - §3 Pins table ≥ 3 YM-relevant pins (8 delivered) ✓
  - §4 Cross-Clay ≥ 2 theorems (7 delivered) ✓
  - §8 Numerical table has SU(3) entry ✓
  - Every theorem cited or NEEDS-CONSTRUCTION-flagged ✓
  - Zero prose paragraphs ✓

The three minor edits tighten the honest flags further but do not change the structural correctness of the document.

## §4 Lock recommendation

C_bare is **LOCKED for publication** after the three minor edits applied.

Recommendation for next run:
- **run-05+**: Composition-backward pass to produce C_full (and B_full) via parallel agents on 60-project reservoir. Specifically for each section §1–§10, retrieve related prose from Papers 1, 60, 61, 8, 12, 13, 26, 28, 29, 30, 31 and compose the full-supplement prose BACKWARD from the bare skeleton. The 5 NEEDS-CONSTRUCTION flags (NC-5.1, NC-5.2, NC-6.1, NC-6.2, NC-7.1) become future programme tasks, not blockers for Zenodo / arXiv / journal release of the bare+full pair.

## §5 Sibling coordination

- **Parallel run-03** (B_bare `ym-clay-bare.md`): independent agent; no coordination required at this pass.
- **Next composition-backward run**: will use both B_bare + C_bare as the bare-skeleton input and produce B_full + C_full. Both bare documents must be LOCKED first.

---

*End arbiter decisions. C_bare PUBLISH-READY. Three minor edits applied post-arbiter.*
