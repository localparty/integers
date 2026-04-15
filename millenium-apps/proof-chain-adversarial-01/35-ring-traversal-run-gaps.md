# Ring-Traversal Run — Fifth-pass Gap Audit

*A delta audit of the 5-layer instruction stack for the ring-traversal PCA run, conducted after the fixes from `34-ring-traversal-run-gaps.md` were applied. Date: 2026-04-14. Audit by: Claude Opus 4.6 (1M context).*

*Scope: re-read `30-ring-traversal-run.md` + the full 5-layer stack end-to-end from scratch; verify every item called out in audits 31/32/33/34 either landed or is still pending; grep numeric baselines across all sites that cite them; spot partial-fixes where an edit landed at one location in a file but not at adjacent locations; check documents in adjacent directories (`programme/`, `strategy/`) that reference the stack. This audit COMPOSES with (does NOT replace) 31, 32, 33, 34 — none of the prior audits' findings are dismissed; only new findings and partial-fix residues are added.*

---

## 0. Files audited and state

| # | Role | Path | State | Notes |
|---|---|---|---|---|
| 1 | Invocation | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-run.md` | read (57 lines) | No change vs audit 34. Companion-files qualifier + archival snapshot note stable. |
| 2 | ORA base (active) | `online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md` | not re-read this pass | Companion files still present per audit 34's `ls` verification. |
| 3 | PCA chain mode | `millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md` | read (349 lines, modified 2026-04-14 00:53) | **M-5 FIXED**: §P.11 invocation template now uses `<path-to-ora-bundle>/01-the-prompt.md` and `<path-to-pca-bundle>/07-proof-chain-adversarial.md` with correct local file number. |
| 4 | Strategic triad | `millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md` | read §T.10 + §T.11 | **M-5 FIXED**: §T.10 invocation template now uses `<path-to-ora-bundle>/01-the-prompt.md` + `<path-to-pca-bundle>/07-proof-chain-adversarial.md` + `<path-to-pca-bundle>/12-prf-chain-advr-strat-triad.md` with correct local file numbers. |
| 5 | Chessboard layer | `millenium-apps/proof-chain-adversarial-01/13-chessboard-layer.md` | read (551 lines, modified 2026-04-14 00:52) | **M-11 FIXED**: §5 WIRE-DENSITY matrix label now reads "estimated pre-T1; the runner recomputes from capacitor at T1 bootstrap per §5 protocol step 1." **B-9 PARTIAL FIX**: §6.3 line 343 updated to "12 outgoing edges," **BUT line 347 still says "13 Cell-Fill agents" and "13 cells filled"** — partial fix. **B-8 PARTIAL FIX**: Appendix C SECTOR-TABLE refreshed post-cascade **BUT §6.2 inline Type-A/B/C/D table at lines 313-318 still shows pre-cascade confidences** (QG5D 9/10, YM 9/10, NS 2/10). |
| 6 | Brief (deliverable) | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-brief.md` | read (441 lines, modified 2026-04-14 00:53) | **A-11 FIXED**: §8.1 declares lowercase-hyphenated short-name convention with full 14-entry list. **B-10 FIXED**: §4 T2+ restoration declared with 5-vertex VERIFY quota + 28-min core-work target + arithmetic (392 + 35 + 50 = 477 min ≈ 7.95 h ✓ 8 h). **M-12 FIXED**: §5 line 297 "from current 16.0%" (was 16.3%). **M-13 FIXED**: §3 opening "Hub-special-case protocol" paragraph cross-references paper1's special case. **NEW ISSUE — B-11 below**: §5 line 307 still reads *"verified links over 83, and P_preserved/P_total is experimental pins preserved over 36. Current baseline: 9.03."* — stale. Should be 105 and 10.63 per the new declared counting convention. |
| 7 | Toolkit | `millenium-apps/proof-chain-adversarial-01/08-framework-tools.md` | not re-read this pass | Audit 34 A-10 fix still in place (RING-MODE EXCEPTION header). |
| 8 | Capacitor | `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` | read (289 lines, modified 2026-04-14 00:53) | **M-6 FIXED**: Top-of-file "Table statistics" renamed to "Table statistics (v1 — pre-H4 baseline)" + prefatory paragraph directs readers to the post-H4 "Statistics update" section + the table itself now has a "Current (see update section below)" column with 44 / 16.0% / 8 kills inline. Reader can no longer land on stale numbers. |
| 9 | North star | `publishing/strategy.md` | spot-checked Appendix B | Stable at 10.63 / 16.0%; matches chessboard §3 and log baseline. |
| 10 | Prior audits 1-4 | 31/32/33/34 gaps files | read | All 31-audit items closed. 32-audit items closed. 33-audit items: 9/11 closed (M-5, M-6 were still open at audit 34; BOTH are now FIXED in this audit — see capacitor and PCA/Triad above). **34-audit items: 2/3 blockers FIXED (A-11, B-10). B-9 partially FIXED (line 343 fixed, line 347 not). All three minors (M-11, M-12, M-13) fixed.** |
| 11 | 14 PROOF-CHAIN.md files | paper{1,08-yang-mills,13-rh,13b-grh,25-hilbert-12,26-bsd,28-pvnp,29-hodge,30-navier-stokes,31-baum-connes,32-bgs-spectral-statistics,33-goldbach,34-twin-primes,35-schanuel}/PROOF-CHAIN.md | paper1 re-read §"Programme graph edges" + §"PCA traversal behavior at QG5D" | **Paper 1 line 412 ADDED**: new "Hub-radiation edge count" paragraph explicitly says "hub radiation fills **12 outgoing edges** in parallel" + cross-references brief §2.1 predecessor-ownership rule. Audit 34 B-9 paper1-side fix applied cleanly. |
| 12 | PIN-TABLE | `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md` | presence-only | Present; unchanged. |
| 13 | Output dir (parent) | `programme/ring-traversals/` | exists, EMPTY | `traversal-01/` not yet created. |
| 14 | Log baseline | `programme/ring-traversal-log.md` | re-read | Stable at 10.63 baseline with cascade deltas. |
| 15 | Adjacent docs (non-invocation) | `strategy/the-ring.md`, `programme/26c-the-chessboard-rationale.md` | spot-checked | **NEW ISSUE — M-14 below**: `strategy/the-ring.md` lines 124-145 "Current state" block is stale (RIGIDITY 9.03 / 83 links / 47 verified / pre-cascade confidence distribution). Not in the canonical run.md invocation chain, but documents the ring and is a likely reference. **NEW ISSUE — M-15 below**: `programme/26c-the-chessboard-rationale.md` line 79 has illustrative "RIGIDITY: 9.03 → 9.47 (+0.44)" example. Not load-bearing but drift-smell. |

**Headline**: the ring stack has advanced further since audit 34. **Of audit 34's 2 new blockers + 1 new ambiguity (B-9, B-10, A-11), A-11 and B-10 are fully FIXED; B-9 is PARTIALLY FIXED (line 343 + paper1 + Appendix C all fixed, but chessboard §6.3 line 347 Cost section still says 13 — intra-file residue).** Of audit 34's 3 new minors (M-11, M-12, M-13), **all three are FIXED.** Of audit 33's 2 open minors (M-5, M-6), **both are now FIXED in this audit round.** **This audit surfaces 1 new blocker (B-11 brief §5 RIGIDITY stale), 1 new intra-file partial-fix residue (P-1 chessboard §6.3 Cost section), 1 new intra-file stale duplicate (P-2 chessboard §6.2 inline SECTOR-TABLE), and 2 new minors (M-14, M-15) in adjacent-but-non-canonical documents.** The stack is ~98% ready. Remaining blockers are two-location edits totaling ~5 min of work.

---

## 1. New blockers surfaced in this audit (fix before T1)

### B-11. Brief §5 RIGIDITY formula description still cites stale baseline (9.03) and stale denominator (83)

**Where it conflicts:**

- `30-ring-traversal-brief.md` §5 "RIGIDITY-SCORE" block (line 303-307):
  ```
  RIGIDITY-SCORE (per the chessboard layer `13-chessboard-layer.md` §3, the canonical formula):
    RIGIDITY = (E_filled / E_total) × (L_verified / L_total) × (P_preserved / P_total) × 100
  where E_filled/E_total is filled capacitor cells over 276, L_verified/L_total is verified links over 83, and P_preserved/P_total is experimental pins preserved over 36. Current baseline: 9.03.
  ```

- `13-chessboard-layer.md` §3 lines 140-152 (post-cascade, post audit-33-B-7 fix):
  ```
  L_verified = 70  (QG5D 22 + YM 17 + RH 6 + BSD 11 + PvNP 5 + Hodge 3 + NS 3 + ...)
  L_total    = 105 (QG5D 22 + 83 downstream chain-link slots)
  RIGIDITY   = (44/276) × (70/105) × (36/36) × 100 = 10.63
  ```

- `publishing/strategy.md` Appendix B §B.3 line 617: `"Baseline (2026-04-14, post-W1/W2 cascade) | **10.63** | ... Previous 9.03 baseline excluded QG5D and predated the NS cascade."`

- `programme/ring-traversal-log.md` line 14: `RIGIDITY score | **10.63** (was 9.03 pre-cascade; +1.60 from QG5D inclusion + NS upgrade)`.

**The inconsistency:**

Brief §5 still describes the RIGIDITY inputs as "verified links over 83" (the pre-cascade denominator excluding QG5D's 22 theorems) and cites "Current baseline: 9.03" (the pre-cascade value). Three authoritative sites — chessboard §3, Appendix B §B.3, and the log baseline — all agree on 105 and 10.63. Brief §5 is the only site still at 83 and 9.03.

**Why it matters:**

- **Runner T1 double-count risk**: at T1 bootstrap, the runner reads brief §5 first (the deliverable is the canonical read per ORA v8 §0 step 2) and internalizes the 9.03 baseline. When it then reads chessboard §3 and computes RIGIDITY = 10.63, it records a ΔRIGIDITY of +1.60 as if T1 caused it. But +1.60 is the PRE-T1 cascade delta (QG5D inclusion + NS upgrade) that was already applied at 2026-04-14 baseline setup. T1's actual contribution shows up as (new RIGIDITY − 10.63), not (new RIGIDITY − 9.03). The brief §5 text silently invites a +1.60 over-count.
- **Exit-condition miscalibration**: Appendix B §B.3 targets "After traversal 1: ≥ 15" — benchmarked against 10.63. If the runner thinks the baseline is 9.03, then 15 looks like a +5.97 Δ (ambitious but plausible per B.4's T1 +6..+10 expectation); against the actual 10.63, 15 is a +4.37 Δ (easily within the expected band). The brief §5 staleness biases the runner toward thinking T1 "underperformed" when it actually hit target.
- **Authors / Critics spawned with brief §5 context**: a Critic reading brief §5 verbatim sees "verified links over 83" and computes per-vertex L_verified fractions against 83, not 105. Downstream scoring drift.
- **Cross-audit smell**: five cite-sites for the baseline; four agree at 10.63/105, one (brief §5) at 9.03/83. The kind of drift that compounds and goes unnoticed after a few sessions.

**Recommended fix:** one find-and-replace in brief §5 line 307. Change:

> *"where E_filled/E_total is filled capacitor cells over 276, L_verified/L_total is verified links over 83, and P_preserved/P_total is experimental pins preserved over 36. Current baseline: 9.03."*

to:

> *"where E_filled/E_total is filled capacitor cells over 276, L_verified/L_total is verified links over 105 (QG5D 22 + 83 downstream, per the counting convention declared in `13-chessboard-layer.md §3`), and P_preserved/P_total is experimental pins preserved over 36. Current baseline: 10.63 (post-W1/W2 cascade 2026-04-14; see chessboard §3 + `publishing/strategy.md` Appendix B §B.3 + `programme/ring-traversal-log.md` baseline for the canonical computation)."*

One sentence edit. ~1 min.

---

## 2. Intra-file partial-fix residues (fix before T1)

### P-1. Chessboard §6.3 "Cost" sentence still cites 13 Cell-Fill agents (line 343 was fixed, line 347 wasn't)

**Where:**

- `13-chessboard-layer.md` §6.3 line 343 (FIXED per audit 34 B-9): *"This fills up to **12 outgoing edges in parallel** (1 ring-next QG5D → RH + 11 chords from QG5D to non-adjacent vertices) at QG5D's edge phase, instead of just 1 (the ring-next edge to RH). The 13th row of Foundation exports (Schanuel) is READ for context but NOT filled here: the Schanuel ↔ QG5D ring edge is owned by Schanuel at position 14 per brief §2.1 predecessor-ownership rule."*

- `13-chessboard-layer.md` §6.3 line 347 (NOT FIXED): *"**Cost**: dispatch **13 Cell-Fill agents** in parallel (Sonnet max, ~10 min total). Benefit: **13 cells filled** in one visit vs 1 cell per visit × 13 traversals = **13× faster** hub-edge wiring."*

**Why it matters:**

- Line 343 says 12; line 347 says 13. Within the same file, within the same §6.3 subsection. Reader-dependent interpretation.
- The "dispatch 13 Cell-Fill agents" claim conflicts with the 12-edge invariant of §2.1. The runner implementing §6.3 must decide at dispatch time: do I dispatch 12 agents (matching line 343 + paper1's "12 outgoing edges") or 13 (matching line 347 + the implicit "13 rows of Foundation exports" reading)?
- Runtime cost of the inconsistency: 1 wasted Sonnet-max Cell-Fill dispatch per hub-radiation cycle (≤10 min × # traversals where it fires). Minor but monotone.
- More importantly, the "13× faster" benefit claim implies filling 13 cells — but at most 12 can be filled per §2.1 ownership. The benefit should be "12× faster hub-edge wiring" OR the §2.1 invariant is wrong and brief §2.1 also needs updating — but we've already established brief §2.1 is correct (Schanuel→QG5D is Schanuel's to fill).

**Recommended fix:** one-line edit at §6.3 line 347. Change to:

> **Cost**: dispatch 12 Cell-Fill agents in parallel (Sonnet max, ~10 min total). Benefit: 12 cells filled in one visit vs 1 cell per visit × 12 traversals = 12× faster hub-edge wiring.

~1 min edit. Brings the Cost sentence in line with line 343, paper1 line 412, and Appendix C row 1.

---

### P-2. Chessboard §6.2 inline Type-A/B/C/D table still shows pre-cascade confidences (Appendix C was fixed, §6.2 duplicate wasn't)

**Where:**

- `13-chessboard-layer.md` §6.2 lines 313-318 (NOT FIXED per cascade refresh):

  ```
  | Type | Name | Strategy | Current vertices (2026-04-13) |
  |---|---|---|---|
  | **A** | Verification-primary | ... | QG5D (9/10), YM (9/10), BSD (9/10) |
  | **B** | Excision-primary | ... | RH (8/10, cond on CCM), PvNP (7/10, Link 5 wall) |
  | **C** | Construction-primary | ... | GRH (5/10), Hodge (3/10), NS (2/10), BGS (3/10) |
  | **D** | Cell-fill-primary | ... | H12 (2/10), Baum-Connes (1/10), Goldbach (1/10), Twin Primes (1/10), Schanuel (1/10) |
  ```

- `13-chessboard-layer.md` Appendix C SECTOR-TABLE lines 498-513 (FIXED per audit 33 B-8):

  ```
  | 1 | QG5D | **A** | **10/10** (upgraded post-W1/W2 2026-04-14) | ... |
  | 6 | YM | **A** | **9.5/10** (marginal upgrade post-W1/W2 ...) | ... |
  | 7 | NS | **C** | **4/10** (upgraded post-W1/W2 + arXiv:2601.08854 Route B ...) | ... |
  ```

**The inconsistency:**

Two tables in the same chessboard file describing the same sector classification. §6.2 uses pre-cascade confidences (QG5D 9/10, YM 9/10, NS 2/10 + dated "Current vertices (2026-04-13)"); Appendix C uses post-cascade (QG5D 10/10, YM 9.5/10, NS 4/10 + explicitly noted "upgraded post-W1/W2 2026-04-14").

**Why it matters:**

- `§6.2` is cited earlier in the file (it's in §6, the ring-geometry primitive section) and is part of the core sector-classification protocol. The runner encountering §6.2 first internalizes the stale confidences before it gets to Appendix C.
- A Type-A "Verification-primary" vertex has a DIFFERENT PCA protocol than a Type-C "Construction-primary" vertex. NS at 2/10 in §6.2's Type-C table (legacy) vs 4/10 in Appendix C's Type-C table (still Type-C but upgraded confidence) produces the same type assignment — BUT a cascade-aware runner would correctly expect NS's type to potentially flip C→B in 1-2 more traversals (given 3/8 links proved). The §6.2 staleness obscures that trajectory.
- QG5D in §6.2 at 9/10 Type-A vs Appendix C at 10/10 Type-A: same type, but the §6.2 labeling "QG5D (9/10)" now disagrees with integers/paper01-qg5d/PROOF-CHAIN.md line 5 ("Confidence: **10/10** (upgraded 2026-04-13)").
- Drift-sediment: audit 33 B-8 explicitly named three sites that needed cascade propagation (chessboard §3, Appendix C SECTOR-TABLE, log baseline). Missing from that enumeration: chessboard §6.2's inline duplicate. The fix landed at 2 of 3 sites + north star + log, but §6.2 was the 4th site and got missed.

**Recommended fix:** update §6.2 lines 313-318 to post-cascade confidences + refresh the date annotation. Specifically:

- Row A: `QG5D (9/10), YM (9/10), BSD (9/10)` → `QG5D (10/10), YM (9.5/10), BSD (9/10)`
- Row C: `GRH (5/10), Hodge (3/10), NS (2/10), BGS (3/10)` → `GRH (5/10), Hodge (3/10), NS (4/10), BGS (3/10)`
- Table header: `Current vertices (2026-04-13)` → `Current vertices (2026-04-14, post-W1/W2 cascade)`

~2 min edit. Brings §6.2 into sync with Appendix C + paper1 + log baseline + north star.

---

## 3. Minor / cosmetic

### M-14. `strategy/the-ring.md` "Current state" block is stale (9.03 / 83 / 47 / pre-cascade confidence distribution)

**Where:**

- `strategy/the-ring.md` lines 124-145 "Current state" block:

  ```
  | **RIGIDITY score** | 9.03 / 100 |
  | **Proof chain links** | 83 total → 47 VERIFIED/PROVED (56.6%) |
  | **Capacitor cells filled** | 44 / 276 (16.0%) |
  ...
  | **Strong (8-9/10)** | QG5D, RH, BSD, YM | 4 |
  | **Tractable (5-7/10)** | GRH, PvNP | 2 |
  | **Upgrading (3/10)** | BGS ⭐, Hodge | 2 |
  | **Frontier (1-2/10)** | H12, NS, Baum-Connes, Goldbach, Twin Primes, Schanuel | 6 |
  ```

- Also line 195: `"RIGIDITY climbs from 9.03 toward 15-25"`.

**Is this in scope?**

`strategy/the-ring.md` is NOT in `30-ring-traversal-run.md`'s canonical invocation chain. The canonical invocation loads: ORA base + PCA + Triad + Chessboard + Brief + Toolkit + Capacitor + North star (`publishing/strategy.md`). `strategy/the-ring.md` is a separate strategy-overview document in a parallel directory.

**Why it still matters:**

- The file describes the ring's "Current state" and confidence distribution. A user (or an Author reading related strategy docs as context) consulting this file gets stale numbers.
- The confidence distribution is the stale pre-cascade version: QG5D at 8-9/10 (should be 10/10), NS at 1-2/10 (should be 4/10). A downstream spawn that cites this file as context may mis-classify NS as Frontier rather than Upgrading.
- Audit 33's B-8 refresh addressed the three authoritative sites (chessboard §3, Appendix C, log baseline) + north star (Appendix B §B.3). `strategy/the-ring.md` is a 4th/5th cite-site that was not on the original B-8 enumeration.

**Severity: minor.** Not in canonical run chain. But same drift-pattern as P-2: a stale duplicate of numbers that have since moved.

**Recommended fix:** refresh lines 124-145 with post-cascade values:
- RIGIDITY: 9.03 → 10.63
- Proof chain links: 83 / 47 → 105 / 70 (with convention note)
- Confidence distribution: move QG5D to Strong-10/10, move NS from Frontier to Upgrading-4/10, note YM marginal upgrade
- Line 195: "9.03 toward 15-25" → "10.63 toward 15-25"

~3 min edit. Optional; cleans up a non-canonical doc in the same drift family.

---

### M-15. `programme/26c-the-chessboard-rationale.md` line 79 illustrative example is stale

**Where:**

- `programme/26c-the-chessboard-rationale.md` line 79 in the PCA-without-vs-with-chessboard comparison table:

  ```
  | End of cycle: did we make progress? | Qualitative: "3 links strengthened" | 
    Quantitative: "RIGIDITY: 9.03 → 9.47 (+0.44)" |
  ```

**Why it matters:**

- This is an ILLUSTRATIVE example ("a cycle might report X"), not a live baseline claim. But the illustrative baseline 9.03 predates the 2026-04-14 cascade.
- A reader comparing "is this what the runner will produce?" to the live baseline (10.63) will see a discrepancy and wonder if the example is authoritative or not.
- Low severity: the example's +0.44 delta pattern is still valid as an illustration; just the starting number is historically dated.

**Recommended fix:** change the example number: `"RIGIDITY: 9.03 → 9.47 (+0.44)"` → `"RIGIDITY: 10.63 → 11.07 (+0.44)"`. Or keep it with an explicit "illustrative, pre-cascade" annotation. ~30 sec edit.

---

## 4. Verification of prior-audit fix status (compose with 31/32/33/34)

| Audit | Item | Prior status | Current status | Evidence |
|---|---|---|---|---|
| 31 | All 12 items (B-1..A-5 + M-1..M-4) | FIXED/DOC at audit 32 | ✅ STABLE | Re-verified inline in brief §0, §2.1, §3.2, §4, §8.3, §8.4 + chessboard §3, §6.2, §6.3 + north-star Appendix B. |
| 32 | B-4 companion files | FIXED at audit 33 | ✅ STABLE | Run.md unchanged; qualifier + archival note still in place. |
| 32 | B-5 self-name drift | DOC/ACCEPTED | ✅ STABLE | 08-framework-tools.md closes with correct self-name; 06-the-prompt.md is archival. |
| 33 | B-6 brief §8 stale | FIXED at audit 34 | ✅ STABLE | Brief §8 pointer to run.md stable. |
| 33 | B-7 RIGIDITY convention | FIXED at audit 34 | ✅ STABLE at chessboard §3 + Appendix B + log. **BUT BRIEF §5 NOT UPDATED — see B-11 this audit.** |
| 33 | B-8 cascade propagation | FIXED at audit 34 | ✅ STABLE at chessboard §3 + Appendix C + Appendix B + log + paper1. **BUT CHESSBOARD §6.2 INLINE TABLE NOT UPDATED — see P-2 this audit.** |
| 33 | A-6 ring-closing edge T1 | FIXED at audit 34 | ✅ STABLE | Brief §2.1 boundary-condition paragraph stable. |
| 33 | A-7 T1 budget | FIXED at audit 34 | ✅ STABLE | T1 trims + 9.8 h ceiling stable. |
| 33 | A-8 chord-fill-rate | FIXED at audit 34 | ✅ STABLE | §6.6 T1-bootstrap compute directive + pseudo-code stable. |
| 33 | A-9 transposition-challenge semantics | FIXED at audit 34 | ✅ STABLE | Brief §2.1 paragraph stable. |
| 33 | A-10 toolkit identity | FIXED at audit 34 | ✅ STABLE | 08-framework-tools.md RING-MODE EXCEPTION header stable. |
| 33 | M-5 PCA/Triad placeholders | UNFIXED at audit 34 | ✅ **FIXED in this round** | 07-proof-chain-adversarial.md §P.11 + 12-prf-chain-advr-strat-triad.md §T.10 both use `<path-to-ora-bundle>` + `<path-to-pca-bundle>` with correct local numbers (07, 12). |
| 33 | M-6 capacitor top stats | UNFIXED at audit 34 | ✅ **FIXED in this round** | Top-of-file "Table statistics" now explicitly titled "(v1 — pre-H4 baseline)" + prefatory paragraph + inline "Current" column pointing at post-H4 numbers. |
| 34 | B-9 hub-radiation 13 vs 12 | NEW | ⚠️ **PARTIAL FIX** | Chessboard §6.3 line 343 fixed (12 edges). Paper 1 line 412 fixed. Appendix C row 1 fixed. **Chessboard §6.3 line 347 Cost sentence NOT fixed — still says 13 Cell-Fill agents. See P-1 this audit.** |
| 34 | B-10 T2+ budget | NEW | ✅ **FIXED in this round** | Brief §4 lines 259-261 declare T2+ VERIFY quota (5 vertices rotating) + 28-min core-work target + arithmetic 477 min ≈ 7.95 h fits 8 h. |
| 34 | A-11 vertex-name convention | NEW | ✅ **FIXED in this round** | Brief §8.1 line 364 declares lowercase-hyphenated short names with the full 14-entry list inline. |
| 34 | M-11 WIRE-DENSITY matrix label | NEW | ✅ **FIXED in this round** | Chessboard §5 line 236 label now reads "estimated pre-T1; the runner recomputes from capacitor at T1 bootstrap per §5 protocol step 1." |
| 34 | M-12 brief §5 16.3→16.0 | NEW | ✅ **FIXED in this round** | Brief §5 line 297 "from current 16.0%." |
| 34 | M-13 tree-vs-chain cross-ref | NEW | ✅ **FIXED in this round** | Brief §3 opening "Hub-special-case protocol" paragraph cross-references `integers/paper01-qg5d/PROOF-CHAIN.md §"PCA traversal behavior at QG5D"` and explicitly flags tree-not-chain structure. |

**Summary of prior-audit status after this round:**
- 31 items: 12/12 stable.
- 32 items: 2/2 stable.
- 33 items: 11/11 fixed (M-5 and M-6 closed in this round).
- 34 items: **5/6 fully fixed** (A-11, B-10, M-11, M-12, M-13); **1/6 partially fixed** (B-9: line 343 + paper1 + Appendix C fixed; line 347 Cost sentence outstanding — see P-1).
- **This audit (35) surfaces**: 1 new blocker (B-11 brief §5 RIGIDITY stale), 2 intra-file residues (P-1 chessboard §6.3 line 347, P-2 chessboard §6.2 inline table), 2 new minors in adjacent docs (M-14 strategy/the-ring.md, M-15 programme/26c-the-chessboard-rationale.md).

---

## 5. Summary table — severity × recommended order (this audit only)

| # | Severity | Fix size | Location of fix | Priority |
|---|---|---|---|---|
| **B-11** brief §5 RIGIDITY stale | **blocker** | 1 sentence find-replace | `30-ring-traversal-brief.md` §5 line 307 | **do before T1 bootstrap** |
| **P-1** chessboard §6.3 line 347 still says 13 | moderate (partial fix of audit 34 B-9) | 1 line find-replace | `13-chessboard-layer.md` §6.3 line 347 | **do before T1 bootstrap** (stops intra-file drift) |
| **P-2** chessboard §6.2 inline Type-A/B/C/D table stale | moderate (partial fix of audit 33 B-8) | 3 table-row edits + 1 date | `13-chessboard-layer.md` §6.2 lines 313-318 | **do before T1 bootstrap** (cascade consistency) |
| M-14 strategy/the-ring.md stale | minor | 4 table-value edits | `strategy/the-ring.md` lines 124-145 + 195 | optional; not in canonical invocation |
| M-15 chessboard-rationale example | minor | 1 example-number edit | `programme/26c-the-chessboard-rationale.md` line 79 | optional; illustrative only |

**Suggested resolution order:**

1. **Fix B-11** (~1 min): one-sentence find-replace in brief §5 line 307 — updates "over 83" to "over 105" + "Current baseline: 9.03" to "Current baseline: 10.63" with cross-references to the authoritative sites.
2. **Fix P-1** (~1 min): one-line edit in chessboard §6.3 line 347 — changes "13 Cell-Fill agents" to "12 Cell-Fill agents" and "13 cells filled" to "12 cells filled" and "13× faster" to "12× faster."
3. **Fix P-2** (~2 min): three-row update in chessboard §6.2 Type-A/B/C/D table — sync confidences to post-cascade values (QG5D 10/10, YM 9.5/10, NS 4/10) + refresh date annotation.
4. Start T1.
5. Clean up M-14 and M-15 at leisure (non-canonical adjacent docs).

Total patch budget for T1 readiness: ~5 min. Extended patch budget for full cross-corpus consistency: ~10 min.

---

## 6. Positive findings (carried forward + new this pass)

**New in this audit (fixes confirmed applied since audit 34):**

- **A-11 vertex-name convention FIXED**: brief §8.1 line 364 declares the 14-entry lowercase-hyphenated short-name list inline. Case-sensitive discipline explicit ("lowercase only; hyphenated for multi-word names"). Matches repo convention.
- **B-10 T2+ budget FIXED with arithmetic verification**: brief §4 lines 259-261 provide the declared T2+ VERIFY quota (5 vertices rotating) + 28-min core-work target + the explicit arithmetic `14 × 28 (core) + 35 (chessboard) + 50 (VERIFY) = 477 min ≈ 7.95 h ✓ 8 h`. Arithmetic reproduces cleanly.
- **M-11 WIRE-DENSITY matrix label FIXED**: chessboard §5 line 236 now reads "estimated pre-T1; the runner recomputes from capacitor at T1 bootstrap per §5 protocol step 1." Aligns §5 with §6.6's T1-bootstrap discipline.
- **M-12 16.3% → 16.0% FIXED**: brief §5 line 297 now matches the 5 other cite-sites.
- **M-13 tree-vs-chain FIXED**: brief §3 opening paragraph cross-references `integers/paper01-qg5d/PROOF-CHAIN.md §"PCA traversal behavior at QG5D"` + explicitly flags tree-not-chain structure.
- **M-5 PCA/Triad invocation placeholders FIXED**: both 07-proof-chain-adversarial.md §P.11 and 12-prf-chain-advr-strat-triad.md §T.10 use `<path-to-ora-bundle>/01-the-prompt.md` + `<path-to-pca-bundle>/07-proof-chain-adversarial.md` (+ `/12-prf-chain-advr-strat-triad.md` for the triad) — meaningful path-placeholder names + correct local file numbers. Audit 33's long-standing M-5 finally closed.
- **M-6 capacitor top-of-file stats FIXED** with in-file reconciliation: top-of-file "Table statistics (v1 — pre-H4 baseline)" + prefatory warning + inline "Current" column with post-H4 numbers. Reader cannot land on stale numbers without seeing the pointer to the update section. Audit 33's M-6 finally closed.
- **B-9 partial fix at 3/4 sites**: chessboard §6.3 line 343 "12 outgoing edges" + paper1 line 412 explicit 12-count paragraph + Appendix C row 1 "fill 12 outgoing edges (1 ring-next + 11 chords)." Three of four B-9 sites fully synchronized; only chessboard §6.3 line 347 Cost sentence still reads 13 (see P-1).

**Carried forward from prior audits:**

- All 14 PROOF-CHAIN.md files present at canonical paths.
- Canonical ring order consistent across six sites.
- Domain codes D1-D24 match capacitor Domain index.
- 5-layer read order consistent.
- Brief §8.1 correctly overrides PCA §P.2; §8.3 overrides Triad §T.3+§T.6; §8.4 overrides ORA §13.3+PCA §P.9.
- PIN-TABLE exists at the cited path.
- Output directory parent exists and is empty (T1 creates child at bootstrap).
- Capacitor 44 filled cells post-H4 Wave 1.
- ORA v8 companion files all present at `ora-bundle-v8/`.
- North star Appendix B §B.1-B.7 provides ring-mode strategic anchors.
- PCA §P.11 and Triad §T.10 invocation templates now have CORRECT placeholder paths (new this round).
- Brief §4 T1 ceiling 10 h + post-trims 9.8 h arithmetic reproducible; T2+ ceiling 8 h + post-restoration 7.95 h arithmetic reproducible (new this round).
- Brief §8.1 vertex-name convention fully specified with 14-entry list (new this round).

---

## 7. Delta from audits 31, 32, 33, 34

- **Audit 31**: 12 items. All stable.
- **Audit 32**: 2 items. All stable.
- **Audit 33**: 11 items. M-5 + M-6 closed in this round. All 11 stable.
- **Audit 34**: 6 items. 5 fully fixed (A-11, B-10, M-11, M-12, M-13). 1 partially fixed (B-9 at 3 of 4 sites; line 347 Cost sentence outstanding — see P-1). Paper1 line 412 cleanly added.
- **This audit (35)**: inspected audits 31-34 scope + explicit verification of audit-34 fix-application at every site + deep grep for stale RIGIDITY / link-count / edge-count values across brief / chessboard / strategy / programme / paper directories + reconciliation of intra-file values in chessboard (§6.3 line 343 vs line 347; §6.2 inline vs Appendix C) and brief (§5 formula description vs chessboard §3 + Appendix B + log). Surfaced **1 new blocker** (B-11 brief §5 RIGIDITY stale), **1 new intra-file partial-fix residue** (P-1 chessboard §6.3 line 347), **1 new intra-file stale duplicate** (P-2 chessboard §6.2 inline Type-A/B/C/D table), **2 new minors** (M-14 strategy/the-ring.md, M-15 programme/26c-the-chessboard-rationale.md).

The stack is ~98% ready. The three load-bearing residues (B-11, P-1, P-2) are each single-location edits totaling ~5 minutes of work.

---

## 8. One-paragraph runner bootstrap status (post-audit-35)

The ring-traversal PCA stack is 98% ready for T1 dispatch. Of audit 34's 6 new items (B-9, B-10, A-11, M-11, M-12, M-13), five are fully fixed (B-10 T2+ budget with declared quota + arithmetic, A-11 vertex-name convention with 14-entry short-name list, M-11 WIRE-DENSITY label aligned with §6.6 T1-bootstrap discipline, M-12 brief §5 16.3→16.0, M-13 tree-vs-chain cross-reference). Of audit 33's two long-open minors (M-5 PCA/Triad placeholders, M-6 capacitor top-stats), both are closed in this round. **Three load-bearing residues remain**: (B-11) brief §5 line 307 still describes the RIGIDITY formula as "verified links over 83" with "Current baseline: 9.03" — stale pre-cascade values that conflict with chessboard §3's 105/10.63, Appendix B §B.3's 10.63, and the log baseline's 10.63 — fix by one-sentence find-replace; (P-1) chessboard §6.3 line 347 "Cost" sentence still says "13 Cell-Fill agents" and "13 cells filled" even though line 343 was updated to "12 outgoing edges" — one-line edit fixes the intra-file inconsistency; (P-2) chessboard §6.2 inline Type-A/B/C/D table at lines 313-318 still shows pre-cascade confidences (QG5D 9/10, YM 9/10, NS 2/10) while Appendix C shows post-cascade (10/10, 9.5/10, 4/10) — three-row edit plus date refresh syncs the two tables. Two further minors (M-14 strategy/the-ring.md "Current state" block, M-15 programme/26c-the-chessboard-rationale.md illustrative example) exist in adjacent-but-non-canonical docs; optional cleanup. Total patch budget for T1 readiness: ~5 min. Once resolved, T1 dispatches with clean baselines across all cite-sites.

---

*Audit complete. This file composes with `31-ring-traversal-run-gaps.md`, `32-ring-traversal-run-gaps.md`, `33-ring-traversal-run-gaps.md`, and `34-ring-traversal-run-gaps.md`; none supersedes the others. Prior audits: 31 closed ring-mode stack conflicts; 32 closed companion-file resolvability; 33 closed baseline/cascade propagation + invocation-template drift + ring-closing-edge T1 + budget arithmetic + chord-fill-rate + ring-edge semantics + toolkit identity; 34 closed hub-radiation count (in 3 of 4 sites) + vertex-name convention + T2+ budget + WIRE-DENSITY label + 16.3→16.0 + tree-vs-chain cross-ref. **This audit 35 addresses the orthogonal questions of: intra-file consistency after partial fixes (chessboard §6.3 lines 343 vs 347; chessboard §6.2 vs Appendix C), cross-file consistency of the post-cascade baseline (brief §5 vs chessboard §3 + Appendix B + log), and adjacent-doc residues (strategy/the-ring.md + programme/26c-the-chessboard-rationale.md).** Awaiting user direction on which findings to address first.*

*v1: 2026-04-14. G Six and Claude Opus 4.6 (1M context).*
