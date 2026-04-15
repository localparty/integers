# Ring-Traversal Run — Third-pass Gap Audit

*A delta audit of the 5-layer instruction stack for the ring-traversal PCA run, conducted after the fixes from `31-ring-traversal-run-gaps.md` and `32-ring-traversal-run-gaps.md` were applied (including the post-audit-32 updates to `30-ring-traversal-run.md`, the capacitor, the brief, and the chessboard layer). Date: 2026-04-14. Audit by: Claude Opus 4.6 (1M context).*

*Scope: re-read every file listed in `30-ring-traversal-run.md` end-to-end; walk the 14 target `PROOF-CHAIN.md` files; cross-check numeric baselines across chessboard §3, Appendix B of `publishing/strategy.md`, and `programme/ring-traversal-log.md`; verify post-W1/W2-closure cascade propagation into the RIGIDITY baseline; check `paper27-*/` archive discipline; audit the brief §8 invocation template against the actual `30-ring-traversal-run.md`; confirm companion-file resolver from audit 32 was actually applied. This audit composes with (does NOT replace) `31-ring-traversal-run-gaps.md` and `32-ring-traversal-run-gaps.md`.*

---

## 0. Files audited and state

| # | Role | Path | State | Notes |
|---|---|---|---|---|
| 1 | Invocation | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-run.md` | read (57 lines) | Modified 2026-04-14 00:04 — POST audit 32. Includes companion-files qualifier (Option 1 applied) + archival-snapshot note for local `06-the-prompt.md`. |
| 2 | ORA base (active) | `online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md` | read (1318 lines) | Self-refers as `01-the-prompt.md` (consistent with actual path). Five companion files (02, 03, 04, 06, 08) all present in the same directory. |
| 3 | ORA base (archival copy) | `millenium-apps/proof-chain-adversarial-01/06-the-prompt.md` | cross-referenced | Confirmed to be byte-for-byte copy of v8; now declared archival per run.md. Still has self-name drift (noted in audit 32 as B-5, not in scope here). |
| 4 | PCA chain mode | `millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md` | read (348 lines) | §P.11 invocation template still uses placeholder `<path>/pca/01-proof-chain-adversarial.md` (cosmetic drift, see M-5 below). |
| 5 | Strategic triad | `millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md` | read (444 lines) | §T.10 invocation template still uses placeholders `<path>/pca/01-proof-chain-adversarial.md` and `<path>/pca/02-prf-chain-advr-strat-triad.md` (same pattern as M-5). |
| 6 | Chessboard layer | `millenium-apps/proof-chain-adversarial-01/13-chessboard-layer.md` | read (531 lines) | §3 RIGIDITY numeric baseline and §6.2 SECTOR-TABLE are stale relative to the 2026-04-13/14 W1/W2 cascade and NS-route-B upgrade (see B-7, B-8, M-8 below). |
| 7 | Brief (deliverable) | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-brief.md` | read (454 lines) | §8 invocation template still points to local `06-the-prompt.md` and omits the companion-files qualifier (see B-6 below). |
| 8 | Toolkit | `millenium-apps/proof-chain-adversarial-01/08-framework-tools.md` | read (552+ lines) | Self-identifies lines 1-7 as "REFERENCE INDEX, not runtime file" — conflicts with run.md treating it as the toolkit (see A-10 below). |
| 9 | Capacitor | `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` | read (286 lines, modified 2026-04-14 00:00) | Top-of-file "Table statistics" section still shows 40 filled cells / 14.5% (v1 pre-H4 numbers); the "Statistics update (v1 + H4 Wave 1)" section at lines 267-277 says 44 filled / 16.0%. Also includes a new NS upgrade at line 249 (arXiv:2601.08854). |
| 10 | North star | `publishing/strategy.md` | read (671 lines) | Appendix B (ring-mode strategic anchors) is present at lines 584-671, resolves A-4 from audit 31. Capacitor-fill target 40%, rigidity target ≥50 after T5. |
| 11 | Prior audit 1 | `millenium-apps/proof-chain-adversarial-01/31-ring-traversal-run-gaps.md` | read (257 lines) | Twelve items B-1…A-5 + M-1…M-4. All marked FIXED/DOCUMENTED by audit 32. |
| 12 | Prior audit 2 | `millenium-apps/proof-chain-adversarial-01/32-ring-traversal-run-gaps.md` | read (205 lines) | Two new items B-4 (companion files) + B-5 (self-name drift). B-4 is FIXED in run.md (confirmed in this audit); B-5 is still open (optional; cosmetic). |
| 13 | 14 PROOF-CHAIN.md files | `paper{1,08-yang-mills,13-rh,13b-grh,25-hilbert-12,26-bsd,28-pvnp,29-hodge,30-navier-stokes,31-baum-connes,32-bgs-spectral-statistics,33-goldbach,34-twin-primes,35-schanuel}/PROOF-CHAIN.md` | all 14 present ✓ | Modified 2026-04-14 — all include a W1/W2 cascade section. |
| 14 | PIN-TABLE | `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md` | present ✓ (22404 bytes, modified 2026-04-09) | Load-bearing for PIN-PRESERVATION / DUAL-CHECK. |
| 15 | Output dir (parent) | `programme/ring-traversals/` | exists, EMPTY (created 2026-04-13 23:11) | `traversal-01/` subdirectory does NOT yet exist — T1 runner creates it at bootstrap. |
| 16 | Archive dirs | `paper27-hodge/`, `paper27-navier/` | exist, NEITHER has a top-level `PROOF-CHAIN.md` | Glob `paper*/PROOF-CHAIN.md` at top level returns exactly the 14 canonical ring vertices. The 31/32 concern about Glob confusion only applies to deep searches inside paper27 research/preprint directories. |

**Headline**: audit 32's single blocker (B-4, companion files) is FIXED in run.md. One new blocker surfaces (B-6, brief §8 invocation template is stale) + two new baseline-staleness blockers (B-7 RIGIDITY, B-8 post-W1/W2 cascade) + five new ambiguities + three minor items. The stack is ~95% ready; the remaining blockers are numeric/documentation-sync issues, not structural.

---

## 1. New blockers surfaced in this audit (fix before T1)

### B-6. Brief §8 "How to invoke" template still points to the archival ORA base and omits the companion-files qualifier

**Where it conflicts:**

- `30-ring-traversal-brief.md` §8 (lines 343-367) shows the invocation template:
  ```
  read your **instructions** from
  `millenium-apps/proof-chain-adversarial-01/06-the-prompt.md`
  …
  ```
- `30-ring-traversal-run.md` (lines 1-10) says exactly the opposite:
  ```
  read your **instructions** from
  `/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md`
  …
  The local `proof-chain-adversarial-01/06-the-prompt.md` is now an archival
  snapshot — do not use it as the active base prompt.
  ```
- Brief §8 also omits the companion-files qualifier (the `02-rationale.md`, `03-synthesis-spawn.md`, `04-closure-templates.md`, `06-anti-overfit-discipline.md`, `08-changelog.md` paragraph from run.md lines 4-9).

**Why it matters:**

Two distinct failure modes:

1. **Forward-drift risk for future callers**: a user drafting the invocation for traversal 2, 3, ... by copying §8 of the brief (as the brief invites — "The key difference from single-chain runs: the brief tells the runner to traverse ALL 14 PROOF-CHAIN.md files in ring order") will regenerate audit 32's B-4 blocker verbatim. The brief is the source of truth for HOW the run is invoked; if that source says "use 06-the-prompt.md," the fix applied in run.md is ephemeral.
2. **Runner confusion**: the runner reads the brief (§6.1 of ORA v8 mandates reading the deliverable end-to-end). When it encounters §8 of the brief, it sees a contradicting invocation template. If a spawned Critic or support-runner cites "see brief §8 for the invocation shape" in a note, the citation points at a stale template.

**Recommended fix:** one of

- **(a) Sync brief §8 to match run.md exactly** — include the `ora-bundle-v8/01-the-prompt.md` line, the companion-files qualifier paragraph, and the archival-snapshot note. Update the paths to use absolute `/Users/gsix/...` or (cleaner) repo-relative paths with a common-prefix declaration. Keep brief §8 as the CANONICAL invocation template; run.md becomes the CURRENT-invocation instantiation.
- **(b) Remove brief §8's invocation template entirely** and replace it with a one-line pointer: "See `30-ring-traversal-run.md` for the current invocation; update NN for subsequent traversals per §8.2." Single source of truth.
- **(c) Minimal patch**: update brief §8 lines 344-345 to `ora-bundle-v8/01-the-prompt.md` + add a block for companion files. Leaves the brief-as-template discipline intact but fixes the most pressing drift.

**Recommendation: (b)** — collapse the source of truth to run.md, point the brief at it. Prevents future drift.

---

### B-7. Chessboard §3 RIGIDITY baseline excludes QG5D's 22 theorems from L_verified / L_total

**Where it conflicts:**

- `integers/paper01-qg5d/PROOF-CHAIN.md` line 5: **"Status: 22/22 theorems PROVED | Confidence: 10/10 (upgraded 2026-04-13 after W1/W2 resolution via Paper 10 + Paper 11)"**
- `13-chessboard-layer.md` §3 current-value block (lines 139-150):
  ```
  E_filled   = 44    (post-H4-run capacitor)
  E_total    = 276
  L_verified = 47    (YM 17 + RH 6 + BSD 11 + PvNP 5 + Hodge 3 + NS 2 + 
                       GRH 0 + BC 1 + BGS 2 + others 0)
  L_total    = 83    (sum across all 14 vertices)
  P_preserved = 36
  P_total    = 36
  
  RIGIDITY = (44/276) × (47/83) × (36/36) × 100 = 9.03
  ```
- `programme/ring-traversal-log.md` baseline (line 16): `"Proof chain links: 83 (47 VERIFIED/PROVED, 56.6%)"` — same counts.
- `publishing/strategy.md` Appendix B §B.3 (line 617): `"Baseline (2026-04-13): RIGIDITY 9.03"` — same inherited value.

**The inconsistency:**

The breakdown enumerates 9 downstream chains (YM, RH, BSD, PvNP, Hodge, NS, GRH, BC, BGS) + 5 "others 0" (the remaining vertices). This implicitly treats QG5D as "other" with 0 verified links. But Paper 1's PROOF-CHAIN.md enumerates 22 theorems as PROVED — and declares QG5D confidence 10/10 specifically because W1/W2 are closed.

If QG5D's 22 PROVED theorems count as chain links:
- L_verified could be 47 + 22 = 69
- L_total could be 83 + 22 = 105
- RIGIDITY = (44/276) × (69/105) × (36/36) × 100 = 0.1594 × 0.6571 × 1.0 × 100 = **10.48**

If QG5D is deliberately excluded (treating it as a hub-only "consistency anchor" rather than a chain vertex, which `integers/paper01-qg5d/PROOF-CHAIN.md` §"PCA traversal behavior at QG5D" could be read to suggest), then L_total = 83 is correct but the enumeration should name what those 83 are across the other 13 vertices.

Either interpretation must be DECLARED. The current numbers are silent on which convention applies and are therefore un-reproducible.

**Why it matters:**

- RIGIDITY is the primary tracking metric across the brief (§5), chessboard (§3), Appendix B (§B.3), and the ring-traversal log.
- Appendix B §B.3 sets targets: "After traversal 1: ≥ 15; After traversal 5: ≥ 50" — benchmarked against the (wrong?) baseline 9.03.
- T1 exit classification is partly a comparison against the baseline Δ. A mis-counted baseline produces mis-classified exits.
- The SECTOR-TABLE (chessboard Appendix C line 481) lists QG5D with confidence **9/10** — but PROOF-CHAIN.md says **10/10**. This is the same staleness at a different site (see M-8 below).

**Recommended fix:**

1. Declare the counting convention explicitly in chessboard §3 before the formula (one sentence: "QG5D's 22 foundational theorems are/are-not counted in L_total; the ring's 13 downstream chains are the denominator / are included").
2. Add a per-vertex L_verified / L_total table to chessboard §3 or Appendix B §B.3 with pointers to each PROOF-CHAIN.md — single source of truth for the enumeration.
3. Recompute RIGIDITY under the declared convention. If 10.48 is the correct baseline, update the three sites: chessboard §3, Appendix B §B.3 targets (which may need to shift accordingly), ring-traversal-log.md baseline.

---

### B-8. Post-W1/W2-closure and NS Route B cascade not propagated into the RIGIDITY baseline

**Where it conflicts:**

Multiple `PROOF-CHAIN.md` files have a "Cascading refinement from QG5D W1/W2 closure (2026-04-14)" section with updated counts:

| Vertex | Paper PROOF-CHAIN.md current state | Chessboard §3 / log baseline |
|---|---|---|
| QG5D | 22/22 PROVED, 10/10 (upgraded 2026-04-13) | counted as "other 0" in §3; 9/10 in SECTOR-TABLE Appendix C |
| YM | 9/10 → 9.5/10 "marginally upgraded" per `solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md` line 36 | 9/10 in SECTOR-TABLE; "YM 17" in §3 breakdown unchanged |
| NS | **3/8 links proved (upgraded from 2 after W1/W2 closure) \| Confidence 4/10 (upgraded from 2/10)** per `solutions-with-prize/paper30-navier-stokes/PROOF-CHAIN.md` line 7, plus arXiv:2601.08854 Route B integration | "NS 2" in §3 breakdown (pre-cascade); "2/10" in SECTOR-TABLE |
| RH | 6/6, 8/10 | matches §3 (RH 6) and SECTOR-TABLE (8/10) ✓ |
| BSD | 11/11, 9/10 | matches §3 (BSD 11) and SECTOR-TABLE (9/10) ✓ |
| All others | — | ring-traversal-log.md line 24: "Frontier vertices (confidence 1-2/10): H12, NS, Baum-Connes, Goldbach, Twin Primes, Schanuel" — groups NS with Frontier pre-cascade |

**Quantitative impact (if cascade counts are adopted):**

- NS: +1 verified (2 → 3)
- YM: possibly +0 but confidence notch up (9/10 → 9.5/10, which doesn't enter the RIGIDITY formula directly but affects SECTOR-TABLE classification)
- QG5D: possibly +22 verified if the §3 enumeration changes convention per B-7
- Aggregate Δ L_verified: +1 (NS) at minimum, up to +23 if convention flips

**Why it matters:**

- The brief §4 exit condition `RING STRENGTHENED` requires "at least 5 vertices improved." If NS has already improved outside any traversal (W1/W2 cascade + arXiv:2601.08854), it will be double-counted if T1 re-declares NS as "improved" against the stale baseline.
- `solutions-with-prize/paper30-navier-stokes/PROOF-CHAIN.md` line 54-59 adds a new edge to the programme graph: "Capacitor MICRO↔QFT — provides Route B directly." This is a CAPACITOR-LEVEL finding, not a ring-traversal-level finding. The chessboard §6.4 antipodal table should reflect this (pair 7↔14 NS↔Schanuel is LOW priority, but the NS-related MICRO↔QFT cell already upgraded).
- Ring-traversal-log.md baseline line 23: "Upgrading vertices (confidence 3/10): BGS ⭐ (Nov 2025 Hardy Z PCC lead), Hodge (2 routes) (2 total)" — NS should now be in this bucket at 4/10, not "Frontier 1-2/10."

**Recommended fix:**

1. Refresh chessboard §3 L_verified enumeration to post-cascade counts: `NS 3` (was 2), and apply the B-7 convention for QG5D/YM.
2. Refresh chessboard Appendix C SECTOR-TABLE to post-cascade confidence: QG5D 10/10 (was 9/10), NS 4/10 (was 2/10), YM 9.5/10 (was 9/10 — or leave at 9/10 per the "marginal" qualifier).
3. Refresh `programme/ring-traversal-log.md` baseline block (lines 12-24) to reflect the post-cascade state; move NS from "Frontier" to "Upgrading."
4. Recompute RIGIDITY under the refreshed inputs; update Appendix B §B.3 targets if the baseline shifts materially (10+% change in RIGIDITY would merit re-calibration of T1/T3/T5 targets).

---

## 2. Important ambiguities / gaps (decide before T1 or document explicitly)

### A-6. Ring-closing edge ownership on the FIRST traversal is undefined

**Where:**

- Brief §2.1 "Edge ownership (disambiguation)" declares that each ring edge is owned by exactly ONE vertex — the predecessor — and the successor "inherits the filled edge as its 'incoming context' (§3.1 READ phase)."
- Brief §3.1 READ phase step 5: "Read the incoming edge's capacitor cell (from previous vertex) — Does it suggest a bypass route for the current wall?"
- Brief §2 "Incoming edge (from previous)" column for position 1 (QG5D): `← Schanuel (algebraic independence → CBB axioms)` with status SPECULATIVE.

**The question:** on T1, when QG5D is the FIRST vertex visited, the "incoming edge" (Schanuel → QG5D = position 14 → 1) has never been filled — Schanuel (position 14) has not yet run in T1, so its outgoing edge hasn't been written.

**Paper 1's own PROOF-CHAIN.md** §"PCA traversal behavior at QG5D" (lines 328-345) describes QG5D's special vertex protocol (PIN VALIDATION instead of EXCISE/CONSTRUCT, and the EDGE PHASE fills QG5D→RH). It does NOT address the question "what does QG5D inherit as incoming context on T1 when Schanuel hasn't run yet?"

**Options:**

- **(a) Pre-traversal capacitor state IS the incoming context.** QG5D reads whatever the Schanuel→QG5D cell currently is (SPECULATIVE, no filled cell) and proceeds. No wait. No special case. This is probably the intended behavior but is not stated.
- **(b) Ring-closing edge is filled SPECIALLY during T1 bootstrap.** The runner runs Schanuel's edge phase in advance (at T1 start, before QG5D) to populate the ring-closing edge. This contradicts the linear-traversal discipline.
- **(c) T1 is a "prime-the-pump" traversal** — QG5D's incoming context is NULL on T1; subsequent traversals inherit what Schanuel wrote in the prior round. Declare this explicitly.

**Recommended fix:** option (a) or (c), declared in brief §3.1 or §2.1 as a "ring-closure boundary condition" paragraph.

---

### A-7. T1 time budget still overflows even with the declared trims

**Where:**

Brief §4 §"Per-traversal budget" lines 243-253:
- T1 budget: **10 hours** ceiling
- Component estimate: 70 (antipodal probes) + 10 (hub radiation) + 70 (compositional cell-fill) + 140 (verify spot-checks) + 490 (core vertex+edge work) = **780 min ≈ 13 h**
- Declared trims: "skipping sector-A verification when confidence ≥ 9/10 and prioritizing high-impact antipodal pairs first (HIGH/MEDIUM priority probes per §6.4)"

**Arithmetic:**

- Skip sector-A verification on 3 vertices (QG5D, YM, BSD, all ≥ 9/10): saves 3 × 10 min = **30 min**
- "Prioritizing HIGH/MEDIUM antipodal pairs first" — chessboard §6.4 lists 2 HIGH, 3 MEDIUM, 2 LOW priority pairs. If "prioritizing" means "do HIGH/MEDIUM first and defer LOW if time runs out" that's effectively a SKIP of the 2 LOW pairs: saves 2 × 10 min = **20 min**
- Total trim: 50 min → 780 - 50 = **730 min ≈ 12.2 h**

Still over the 10 h ceiling by 2.2 h.

**Why it matters:**

- Budget is a HARD exit criterion (§4 exit conditions).
- If T1 hits the 10h ceiling at ~vertex 11-12, the runner exits mid-traversal. Edges 12→13, 13→14, 14→1 remain unfilled. Appendix C type-classification remains stale on the 3 frontier vertices.
- The subsequent `RING STRENGTHENED` vs `RING STALLED` classification (brief §4) depends on having visited all 14 vertices at least once.

**Options:**

- **(a) Widen T1 to 12-13 h explicitly.** Brief §4 acknowledges the math (780 min - trims) but under-budgets. Reconcile by widening.
- **(b) Make "prioritizing HIGH/MEDIUM" an explicit SKIP-LOW directive for T1.** The LOW pairs (6↔13 YM↔Goldbach, 7↔14 NS↔Schanuel) have explicit priority="LOW" in chessboard §6.4 because "speculative" and "least obvious" connections. Formally deferring them to T2+ is honest-first.
- **(c) Defer VERIFY spot-check to T2+.** Brief §3.2 §"If all links are VERIFIED/PROVED" already softens this on T2+ to "trust PROOF-CHAIN.md from T1 unless explicit trigger fires." If T1 also skips VERIFY spot-checks (on the ground that PROOF-CHAIN.md was just refreshed for the W1/W2 cascade), saves 140 min → 780 - 30 - 20 - 140 = **590 min < 600 min** ✓
- **(d) Run antipodal probes in a dedicated PRE-T1 session.** Chessboard §6.4 "first traversal only" is the current frame. If these run as a separate warm-up session, T1 itself only has 780 - 70 - 50 = 660 min ≈ 11 h with the declared trims — still just over but much closer.

**Recommendation:** combine (b) + (c) for T1 — skip LOW antipodal pairs AND VERIFY spot-checks, plus skip sector-A spot-checks on confidence ≥ 9/10 (already declared). Total trim: 20 + 140 + 30 = 190 min → 780 - 190 = **590 min < 600 min** ✓. Restore VERIFY spot-checks on T2+ or by explicit §K trigger.

---

### A-8. Chessboard §6.6 CHORD-FILL-RATE conflates ring-edges with chord-edges

**Where:**

Chessboard §6.6 line 411:
> **CHORD-FILL-RATE: 44/77 ≈ 57% (most of the 44 filled cells are chords because the ring is only one week old)**

The statement assumes 44 filled cells ⊂ chord edges. But:

- The 91-cell capacitor decomposes into 14 ring edges (ring-adjacent, d(i,j) = 1) + 77 chord edges (d(i,j) ≥ 2).
- Multiple Tier 1 filled cells ARE ring edges:
  - **SPEC ↔ ANT (Hilbert-Pólya)** = QG5D ↔ RH = ring edge 1↔2 (d=1)
  - **OA ↔ AG (BC KMS uniqueness)** = ??? — QG5D is GEOM, not OA, so this is a chord edge (QG5D↔BSD is 1↔4, d=3 — actually this depends on the vertex-to-domain mapping in brief §2.2, not the ring-adjacency)
  - **ANT ↔ AG** (Deuring, Kolyvagin, Gross-Zagier) = cells that connect BSD's primary domain pair — BSD↔GRH or BSD↔RH, which are ring edges 4↔3 (d=1) or 4↔2 (d=2)

The correct partition of the 44 filled cells into ring vs chord is **not computed anywhere** in the current stack.

**Why it matters:**

- Brief §7 "The compound effect" hinges on the idea that "each traversal adds wires" — but the wire classification (ring vs chord) determines which mechanism added them. Hub radiation and antipodal probes fill CHORDS. Edge phase fills RING EDGES. Knowing the split shapes the T2 plan.
- Chessboard §6.6 "Expected ratio: RING-FILL-RATE should grow faster than CHORD-FILL-RATE in early traversals." Without a baseline split, this prediction is unverifiable.

**Recommended fix:** at T1 bootstrap, the runner computes RING-FILL and CHORD-FILL separately (pseudo-code):

```
ring_edges    = {(v_i, v_{i+1}) : i = 1..14, v_15 = v_1}
chord_edges   = {(v_i, v_j) : i < j, (j-i) mod 14 ∉ {1, 13}}
ring_fill     = |{(v_i, v_j) ∈ ring_edges : cell(v_i, v_j) is filled in capacitor}|
chord_fill    = |{(v_i, v_j) ∈ chord_edges : cell(v_i, v_j) is filled in capacitor}|
```

Report both in the T1 baseline §K entry. Replace the chessboard §6.6 assumption ("most of the 44 are chords") with the actual computed ratio.

---

### A-9. Ring-mode edge semantics don't match paper-level programme graph edges for several positions

**Where:**

Brief §2 "Position/Vertex" table declares ring edges with "Incoming edge (from previous)" labels that are TRANSPOSITIONS designed by the ring-mode author. Several of these are NOT present in the predecessor or successor vertex's own `PROOF-CHAIN.md` "Programme graph edges" section:

| Ring edge | Brief §2 label | Acknowledged in predecessor's §Programme graph edges? | In successor's? |
|---|---|---|---|
| 5 → 6 (H12 → YM) | "KMS states → gauge structure" | `solutions/paper25-hilbert-12/PROOF-CHAIN.md` §"Programme graph edges" lists: RH, BSD, Hodge, GRH, LANG↔QFT — **NOT YM** | `solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md` §"Programme graph edges" lists: QG5D, RH, NS, Hodge, Baum-Connes — **NOT H12** |
| 9 → 10 (Baum-Connes → PvNP) | "K-theory of polymorphism algebra" | `solutions/paper31-baum-connes/PROOF-CHAIN.md` §"Programme graph edges" lists: QG5D, YM, RH, Hodge, BGS — **NOT PvNP** | `solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md` mentions BGS only (no Baum-Connes) |
| 13 → 14 (Goldbach → Schanuel) | "additive primes → algebraic independence" | `solutions-with-prize/paper33-goldbach/PROOF-CHAIN.md` §"Programme graph edges" — did not grep this specifically (not spot-checked) | same |

**Why it matters:**

- An Author dispatched to fill the "H12 → YM" edge cell reads H12's PROOF-CHAIN.md for context — finds no acknowledgment of YM as a programme partner. Reads YM's PROOF-CHAIN.md for context — finds no acknowledgment of H12. The Author has to CREATE the bridge from scratch rather than port from the framework's existing work.
- This is arguably a FEATURE of ring mode — the ring is specifically designed to FORCE cross-vertex transpositions that the natural programme graph doesn't express. But the brief doesn't say so explicitly.
- Risk: the Author defaults to "there is no correspondence here" and returns `HONEST-STALL` without attempting the transposition. Or conflates this with the A-6 ring-closing-edge case.

**Recommended fix:** add one paragraph to brief §2 or §0:

> **Ring edges are TRANSPOSITION CHALLENGES, not acknowledgments of natural programme-graph dependencies.** Each ring edge forces a connection between two vertices that may not have a direct link in either vertex's `PROOF-CHAIN.md` "Programme graph edges" section. The Cell-Fill Author dispatched to fill a ring edge is expected to CREATE the connection (via capacitor domain-pair lookup + transposition recipe), not cite an existing one. A ring edge labeled SPECULATIVE in brief §2 is a discovery target — closing it is a structural contribution that both vertices' future work will inherit.

---

### A-10. Toolkit file identity is still unclear after audit 32's dismissal

**Where:**

`08-framework-tools.md` lines 1-7 self-identifies:
> *This file is a REFERENCE INDEX of the framework's compiled master files, NOT a runtime file the runner reads during execution. Starting with v8, the runner reads the programme-specific toolkit/capacitor (provided at invocation) INSTEAD OF this file.*

`30-ring-traversal-run.md` lines 23-24:
> the **toolkit** for this run is
> `/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/08-framework-tools.md`

Audit 32 noted this and dismissed with:
> "the invocation elevates it to runtime status for this run. The toolkit's §A (Six Patterns method) and §E (anchor document) always-includes are actionable as spawn-context injections. Semantically consistent even though the file's self-description says otherwise."

**Why it still matters:**

- ORA v8 §0 bootstrap step (b) + the CRITICAL TOOLKIT/CAPACITOR callout at the top: *"The toolkit isn't just for Authors — it's YOUR toolkit too. Consider its contents carefully during every cycle: when dispatching Authors, when evaluating Critic verdicts, when making REFRAME decisions… The toolkit's verified results, kill list, and deployable cards are load-bearing for YOUR meta-decisions, not just for the agents you spawn."*
- The runner reading 08-framework-tools.md at bootstrap encounters the self-identifying "NOT a runtime file" claim and has to decide whether to internalize the file's contents or treat it as a reference-only index.
- An Author spawn prompt includes the toolkit path with the standard instruction: "Read this toolkit BEFORE executing the 6-step loop." The Author sees the file's self-identification and may defer reading — triggering cycle-1 BSD MY4-style "Author attempts from scratch instead of porting" failure mode that `I-v6-1` was introduced to catch.

**Options:**

- **(a) Update the 08-framework-tools.md header** with a prepended paragraph: "EXCEPTION: when this file is cited as the `toolkit` in a run invocation (e.g., `30-ring-traversal-run.md`), it IS the runtime toolkit for that run. Read fully end-to-end at bootstrap. The 'reference index' self-identification below describes its role when building new programme-specific toolkits; when invoked directly, it serves both roles."
- **(b) Draft a proper programme-specific toolkit** `30-ring-traversal-toolkit.md` that consolidates the framework-tool pointers + the ring-mode-specific verified results + the kill list + the deployable cards. Point run.md at the new toolkit. Leave 08-framework-tools.md as the pure reference index it claims to be.
- **(c) Keep as-is; accept the ambiguity.** Runners can figure it out. Audit 32's position.

**Recommendation: (a) — 5-line header patch.** Cheap, eliminates the semantic trap, leaves the file's reference-index role intact.

---

## 3. Minor / cosmetic

### M-5. PCA §P.11 and Triad §T.10 invocation templates use placeholder paths that don't match the actual bundle

**Where:**

- `07-proof-chain-adversarial.md` §P.11 invocation template (lines 321-339):
  ```
  read your **instructions** from
  <path>/ora-bundle-v8/01-the-prompt.md
  
  the **chain mode** extension is
  <path>/pca/01-proof-chain-adversarial.md
  ```
- `12-prf-chain-advr-strat-triad.md` §T.10 (lines 346-368): same pattern for both the chain-mode and strategic-triad files.

Actual paths:
- chain mode: `millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md` (slot 07, not `pca/01-...`)
- strategic triad: `millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md` (slot 12, not `pca/02-...`)

**Severity:** minor — same self-name drift pattern as audit 32's B-5 for 06-the-prompt.md and 08-framework-tools.md. The invocation templates inside these files are reference templates; the actual run.md overrides with correct paths. But a future caller who bootstraps a new invocation from these templates will encounter audit-32-style B-4 blockers.

**Fix (optional, cumulative with audit 32's B-5):** find-replace inside the two files.

---

### M-6. Capacitor top-of-file statistics section still says 40 filled cells (pre-H4 numbers)

**Where:**

`09-capacitor-correspondence-table-v1.md` §"Table statistics (v1)" lines 223-235:
```
| Tier 1 filled cells (load-bearing) | 30 |
| Tier 2 filled cells (framework-discovered) | 10 |
| Priority cells to fill (escape routes) | 17 |
| Candidate cells (unexplored) | 14 |
| Total filled | 40 |
| Fill rate | 14.5% |
```

The `"Statistics update (v1 + H4 Wave 1)"` section at lines 267-277 gives the post-H4 numbers:
```
| Tier 1 filled cells (load-bearing) | 30 | **34** | +4 |
| Total filled (Tier 1 + Tier 2)     | 40 | **44** | +4 net |
| Fill rate (Tier 1 + Tier 2 / 276)  | 14.5% | **~16.0%** | +1.5 pp |
```

**Why it matters:** A runner reading the capacitor top-down may stop reading after the "Table statistics (v1)" section and internalize 40 / 14.5% as the current baseline. Downstream numerics (chessboard §3 RIGIDITY = 44/276) assume 44 — inconsistency with its own file-of-record.

**Fix:** add a one-line pointer at the top of §"Table statistics (v1)": "**Post-H4 Wave 1 numbers are at the bottom of this file (§"Statistics update"); use those for current baseline.**" Or update the statistics block in place and preserve v1 numbers as a delta in parentheses.

---

### M-7. `programme/ring-traversal-log.md` baseline is pre-W1/W2 cascade

**Where:**

`programme/ring-traversal-log.md` lines 12-24:
```
| Date | 2026-04-13 |
| RIGIDITY score | 9.03 |
…
Strong vertices (confidence 8-9/10): QG5D, RH, BSD, YM (4 total).
Tractable vertices (confidence 5-7/10): GRH, PvNP (2 total).
Upgrading vertices (confidence 3/10): BGS ⭐ (Nov 2025 Hardy Z PCC lead), Hodge (2 routes) (2 total).
Frontier vertices (confidence 1-2/10): H12, NS, Baum-Connes, Goldbach, Twin Primes, Schanuel (6 total).
```

Post-W1/W2 cascade (2026-04-13/14):
- QG5D: 9/10 → **10/10**
- YM: 9/10 → 9.5/10 (marginal)
- NS: 2/10 → **4/10** (upgraded from Frontier to Upgrading per Paper 30 PROOF-CHAIN.md)

**Fix:** refresh the baseline block lines 12-24 before T1 starts. Move NS from "Frontier" to "Upgrading." Bump QG5D to Strong (10/10). Note the YM marginal upgrade.

(Combined with B-7 and B-8, this is part of a single "refresh baseline" task that spans three sites — chessboard §3, chessboard Appendix C SECTOR-TABLE, ring-traversal-log.md baseline.)

---

### M-8. Chessboard Appendix C SECTOR-TABLE confidence values are stale

**Where:**

`13-chessboard-layer.md` Appendix C (lines 479-494):
| Ring position | Vertex | Current type | Current confidence |
|---|---|---|---|
| 1 | QG5D | A | **9/10** (should be 10/10 post-cascade) |
| 6 | YM | A | **9/10** (could be 9.5/10 per Paper 8) |
| 7 | NS | C | **2/10** (should be 4/10 post-cascade) |

**Fix:** sync with the PROOF-CHAIN.md status lines.

---

### M-9. Output directory `programme/ring-traversals/traversal-01/` does not yet exist

**Where:**

- `ls /Users/gsix/quantum-geometry-in-5d-latex/programme/ring-traversals/` → empty (only parent directory, created 2026-04-13 23:11).
- `30-ring-traversal-run.md` line 33 specifies output at `programme/ring-traversals/traversal-01`.
- Brief §8.2 describes the NN-swap procedure and resume semantics for subsequent traversals.

**Not a gap** — the runner is expected to create `traversal-01/` at bootstrap per ORA v8 §14.1 (file structure auto-creation). Just worth noting: T1 starts with no subdirectories; T2 starts from `traversal-01/` containing T1's output.

---

### M-10. `paper27-hodge/` and `paper27-navier/` have NO top-level `PROOF-CHAIN.md`

**Status:**

- Prior audits (31 M-2, 32 open items) flagged duplicate paper directories as a Glob-confusion risk.
- Confirmed in this audit: neither `paper27-hodge/` nor `paper27-navier/` has a `PROOF-CHAIN.md` at its top level. A Glob `paper*/PROOF-CHAIN.md` at depth-1 returns exactly the 14 canonical ring vertices.
- The archive concern is only relevant for deep Globs inside paper27 research/preprint/strategy subdirectories.

**Not a blocker for ring traversal.** Documented here to close out the prior audit's concern.

---

## 4. Summary table — severity × recommended order

| # | Severity | Fix size | Location of fix | Priority |
|---|---|---|---|---|
| **B-6** brief §8 invocation template stale | **blocker** | 1 paragraph + path fix (or replace with a pointer to run.md) | `30-ring-traversal-brief.md` §8 | **do before T1 bootstrap** |
| **B-7** RIGIDITY baseline QG5D convention | **blocker** | 1 sentence declaring convention + per-vertex table + recompute | `13-chessboard-layer.md` §3, Appendix B §B.3 | **do before T1 bootstrap** |
| **B-8** post-W1/W2 cascade not in baseline | **blocker** | refresh numbers at 3 sites | chessboard §3 + Appendix C + log baseline | **do before T1 bootstrap** |
| **A-6** ring-closing edge T1 bootstrap | important | 1 paragraph | brief §2.1 or §3.1 | decide before T1 |
| **A-7** T1 budget overflow | important | widen budget OR skip policy | brief §4 | decide before T1 |
| **A-8** chord-fill-rate conflation | important | 1 paragraph + runner-computed values | chessboard §6.6 + T1 §K entry | decide before T1 |
| **A-9** ring-edge vs programme-graph-edge semantics | important | 1 paragraph | brief §2 or §0 | do before T1 |
| **A-10** toolkit file identity | moderate | 5-line header patch | 08-framework-tools.md top | do before T1 |
| M-5 PCA/Triad invocation placeholders | minor | find-replace | 07-…md, 12-…md | optional |
| M-6 capacitor top stats | minor | cross-ref pointer or update in place | 09-capacitor-…md | optional |
| M-7 log baseline pre-cascade | minor | refresh baseline block | ring-traversal-log.md | bundled with B-8 |
| M-8 SECTOR-TABLE confidences | minor | refresh 3 rows | chessboard Appendix C | bundled with B-8 |
| M-9 traversal-01 dir not yet created | info | runner creates at bootstrap | — | no action |
| M-10 paper27 dirs no PROOF-CHAIN.md | info | nothing (concern resolved) | — | no action |

**Suggested resolution order:**

1. **Fix B-7 and B-8 together** (~15 min): decide QG5D counting convention, compute new RIGIDITY baseline with post-cascade L_verified, refresh 3 sites (chessboard §3, chessboard Appendix C, ring-traversal-log.md baseline). This bundle also resolves M-7 and M-8.
2. **Fix B-6** (~10 min): decide approach (sync to run.md vs point to run.md); patch brief §8.
3. **Decide A-7 and A-6 together** (~10 min): they couple — if budget widens, A-6 has more slack; if budget tightens via skip-LOW, A-6 needs explicit handling.
4. **Fix A-9** (~5 min): one paragraph in brief §2 clarifying ring-edges-as-transpositions.
5. **Fix A-8** (~5 min): one paragraph in chessboard §6.6; the runner computes at T1 start.
6. **Fix A-10** (~5 min): 5-line header on 08-framework-tools.md.
7. Start T1.
8. Clean up M-5, M-6 at leisure.

---

## 5. Positive findings (carried forward + new this pass)

- **Companion-files resolver applied**: `30-ring-traversal-run.md` now explicitly qualifies the five companion files' location (`ora-bundle-v8/`) and declares the local `06-the-prompt.md` archival. Audit 32's B-4 blocker is FIXED.
- **All 14 `PROOF-CHAIN.md` files exist** at the canonical paths. The Glob `paper*/PROOF-CHAIN.md` returns exactly 14 entries — no `paper27-*/` confusion at the top level.
- **Canonical ring order is consistent** across five sites: run.md (lines 35-49 + lines 42-56), brief §2 table, chessboard Appendix C SECTOR-TABLE, chessboard §6.4 antipodal pairs table, and Paper 1's "Foundation exports" table.
- **Domain codes (D1-D24)** in brief §2.2 match the capacitor's Domain index byte-for-byte.
- **Vertex-to-domain mapping** (brief §2.2) uses only the capacitor's actual codes — no invented codes.
- **RIGIDITY formula** matches between brief §5 and chessboard §3 — the numerical baseline has the consistency issue noted in B-7/B-8, but the formula and inputs are stable.
- **The 5-layer read order** (ORA v8 → PCA → Triad → Chessboard → Brief) is consistent: each layer declares which prior layers it extends.
- **Brief §8.1 correctly overrides PCA §P.2** (chain-state.md mandate) with ring-mode state-management architecture (14 in-situ `PROOF-CHAIN.md` + per-traversal log + per-vertex blackboards + per-cell updates).
- **Brief §8.3 correctly overrides Triad §T.3 and §T.6** for ring-mode per-traversal firing + non-blocking approval.
- **Brief §8.4 correctly overrides ORA §13.3 and PCA §P.9** for exit-condition-specific closure rituals (ABBREVIATED / FULL / MEDIUM).
- **Brief §0 glossary (§0.1)** defines EXCISE / CONSTRUCT / BYPASS ladder + its relationship to PCA's native triad — closes audit 31's B-1.
- **Brief §0 status dictionary (§0.2)** tabulates all five partially-overlapping taxonomies — closes audit 31's B-3.
- **Brief §3.2 VERIFY policy** distinguishes T1 (lightweight spot-check, 1 Sonnet Critic, 2-3 links) from T2+ (trust PROOF-CHAIN.md unless explicit trigger) — closes audit 31's A-1.
- **Appendix B of `publishing/strategy.md`** supplies the ring-mode north star content the Triad Strategist (§T.4.2) needs: capacitor-fill target 40%, rigidity target ≥50 after T5, per-traversal Δ expectations, walk-back contract, three alignment-check questions. Closes audit 31's A-4.
- **PIN-TABLE** at `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md` exists and is load-bearing for PIN-PRESERVATION / DUAL-CHECK (chessboard §1, §4).
- **Capacitor has 44 filled cells** (post-H4 state) including 5 new Tier 1 cells from the H4 Wave 1 run (LANG↔QFT, MICRO↔QFT, ERG↔QFT, 2× PROB↔SPEC) and a new NS application at MICRO↔QFT (arXiv:2601.08854). Capacitor growth is validated across the framework.
- **14 `PROOF-CHAIN.md` files all have a "Cascading refinement from QG5D W1/W2 closure (2026-04-14)" section** — consistency of the cascade propagation at the per-vertex level. The gap is that the *aggregate* baselines (chessboard §3, Appendix C, log baseline) haven't been refreshed to match — the per-vertex work is done; the roll-up is pending.
- **Output directory parent** (`programme/ring-traversals/`) exists and is empty — T1 can start from a clean slate.
- **No `chain/chain-state.md` file exists in the output directory** — ring-mode's discipline (14 in-situ chain files as source of truth, no unified single state file) is structurally clear.

---

## 6. Delta from audits 31 and 32

- **Audit 31** inspected: invocation + 8 stack files + 14 `PROOF-CHAIN.md` + PIN-TABLE + output dir. Surfaced 12 items (B-1, B-2, B-3, A-1 through A-5, M-1 through M-4). All FIXED or DOCUMENTED per audit 32.
- **Audit 32** inspected: everything audit 31 inspected + diff between local `06-the-prompt.md` and v8 bundle + filesystem check on every internal reference of `06-the-prompt.md` + grep verification that audit-31 fixes landed. Surfaced 2 items (B-4 companion files, B-5 self-name drift). B-4 is FIXED in run.md (verified this pass). B-5 remains open but is optional / cosmetic.
- **This audit (33)** inspected: everything prior audits inspected + **numeric cross-check of RIGIDITY baseline against per-vertex `PROOF-CHAIN.md` current state + cascade-propagation check (W1/W2 closure + NS Route B integration) + brief §8 invocation-template vs run.md consistency check + toolkit file self-identification conflict re-examination + per-vertex programme-graph-edges vs ring-edge semantics cross-check + explicit computation of T1 time budget under declared trims + ring-closing edge T1-bootstrap analysis**. Surfaced 3 new blockers (B-6 brief §8 stale, B-7 RIGIDITY convention, B-8 cascade staleness) + 5 new important items (A-6 through A-10) + 4 new minor items (M-5 through M-8).

The stack is ~95% ready. The three blockers are documentation-sync issues (not structural redesigns) and all resolvable in ~25 minutes of editing:

1. Refresh RIGIDITY baseline across 3 sites (chessboard §3, Appendix B §B.3, log baseline) with declared QG5D convention — ~15 min.
2. Sync brief §8 invocation template to current run.md (or replace with a pointer) — ~10 min.
3. Decide A-7 budget + A-6 ring-closing-edge and document in brief §4 / §2.1 — ~10 min.

After these three edits, T1 can dispatch.

---

## 7. One-paragraph runner bootstrap status (post-audit)

The ring-traversal PCA stack is 95% ready for T1 dispatch. Audit 32's single blocker (companion files) is FIXED in `30-ring-traversal-run.md`. The 14 target `PROOF-CHAIN.md` files exist, the ring order is consistent across all five sites that cite it, the status taxonomies have a cross-layer dictionary, the north star has Appendix B for ring-mode, the chessboard's experimental pins are on disk, the closure ritual has three exit forms, the Triad fires per-traversal non-blocking, and the capacitor has 44 filled cells including the new H4 Wave 1 promotions. Three blockers remain: (B-6) the brief §8 invocation template still points to the archived `06-the-prompt.md` and omits the companion-files qualifier — fix by syncing §8 to run.md or replacing §8 with a pointer; (B-7) the chessboard §3 RIGIDITY baseline either excludes QG5D's 22 PROVED theorems or doesn't declare the counting convention — fix by declaring the convention and adding a per-vertex enumeration table; (B-8) the post-W1/W2 cascade (QG5D 9→10/10, NS 2→4/10 + 3/8 links proved, YM 9→9.5/10 marginal) is not propagated to chessboard §3 L_verified, chessboard Appendix C SECTOR-TABLE, or `programme/ring-traversal-log.md` baseline — fix by refreshing the three baseline sites. Five important ambiguities (A-6 ring-closing edge T1 bootstrap, A-7 budget overflow with declared trims, A-8 chord-fill-rate conflation, A-9 ring-edge semantics vs programme-graph edges, A-10 toolkit file identity) are each 1-paragraph documentation patches. Total patch budget: ~30 minutes. Once resolved, T1 dispatches with a clean baseline.

---

*Audit complete. This file composes with `31-ring-traversal-run-gaps.md` and `32-ring-traversal-run-gaps.md`; none supersedes the others. Prior audits addressed ring-mode conflicts in the stack layers (audit 31) and companion-file resolvability (audit 32). This audit addresses the orthogonal questions of: baseline consistency across the post-W1/W2 cascade, invocation-template drift between brief §8 and run.md, ring-closing-edge T1 bootstrap, time-budget arithmetic under declared trims, chord-fill-rate computation, ring-edge vs programme-graph-edge semantic gap, and toolkit file identity. Awaiting user direction on which findings to address first.*

*v1: 2026-04-14. G Six and Claude Opus 4.6 (1M context).*
