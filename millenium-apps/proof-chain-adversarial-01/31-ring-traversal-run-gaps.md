# Ring-Traversal Run — Instruction Gaps, Ambiguities, and Conflicts

*A recursive audit of the 5-layer instruction stack for the ring-traversal PCA run, before first invocation. Date: 2026-04-13. Audit by: Claude Opus 4.6.*

*Scope: every file listed in `30-ring-traversal-run.md`, read end-to-end, plus the 14 target PROOF-CHAIN.md files verified to exist and the referenced PIN-TABLE at `paper12/research/23-framework-predictions-master-table.md` verified to exist. The output directory `programme/ring-traversals/` does **not** exist yet — traversal-01 will be a fresh start.*

---

## 0. Files audited

| # | Role | Path | Status |
|---|---|---|---|
| 1 | Invocation | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-run.md` | read |
| 2 | ORA base | `millenium-apps/proof-chain-adversarial-01/06-the-prompt.md` | read |
| 3 | PCA chain mode | `millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md` | read |
| 4 | Strategic triad | `millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md` | read |
| 5 | Chessboard layer | `millenium-apps/proof-chain-adversarial-01/13-chessboard-layer.md` | read |
| 6 | Brief (deliverable) | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-brief.md` | read |
| 7 | Toolkit | `millenium-apps/proof-chain-adversarial-01/08-framework-tools.md` | read |
| 8 | Capacitor | `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` | read (domain index + Tier 1 + priority cells) |
| 9 | North star | `publishing/strategy.md` | read |
| 10 | 14 PROOF-CHAIN.md files | `paper{1,08-yang-mills,13-rh,13b-grh,25-hilbert-12,26-bsd,28-pvnp,29-hodge,30-navier-stokes,31-baum-connes,32-bgs-spectral-statistics,33-goldbach,34-twin-primes,35-schanuel}/PROOF-CHAIN.md` | all 14 present ✓ |
| 11 | PIN-TABLE | `paper12/research/23-framework-predictions-master-table.md` | present ✓ |
| 12 | Output dir | `programme/ring-traversals/` | does NOT exist (fresh start) |

---

## 1. Blockers (must resolve before first traversal)

### B-1. "EXCISE" is multi-defined across the stack

**Where it conflicts:**

- PCA §P.3 (file `07-proof-chain-adversarial.md`) defines the primitive triad as **verify / construct / bypass**. EXCISE is not a PCA primitive.
- Brief §3.2 (file `30-ring-traversal-brief.md`) uses EXCISE to mean *"find an independent proof or construction"* — the literature / independent-route move. `CONSTRUCT/BYPASS via capacitor` is the explicit fallback if EXCISE fails.
- Chessboard §6.2 Type B (`13-chessboard-layer.md`) defines Type B as "Excision-primary. Focus: **eliminate the conditional via bypass or alternative proof**" — here EXCISE ⊇ BYPASS.
- Chessboard architecture box (top of `13-chessboard-layer.md`): "Strategic triad (**VERIFY/EXCISE/CONSTRUCT** escalation + capacitor-first)" — this reads as a rename of PCA's triad, with EXCISE substituted for BYPASS.

**Why it matters:** The runner's first Plan step dispatches Authors by primitive name. If a vertex's weakest link is CONDITIONAL and the brief says "try EXCISE first," the Author needs to know whether that means *hunt for external literature*, *transpose via the capacitor*, or *both as one composite move*.

**Recommended fix:** add a one-paragraph glossary at the top of the brief:

> **EXCISE** = attempt to replace the conditional with an independent, already-published result. Literature search + direct proof. If no independent result exists, fall through to **CONSTRUCT** (build via capacitor toolkit) or **BYPASS** (transpose to a different domain via the capacitor). These are the three capacitor-aware moves. PCA's underlying triad (verify / construct / bypass) still applies; EXCISE is the ring-mode's name for the literature-first escalation that sits *above* construct/bypass.

Then audit `13-chessboard-layer.md` §6.2 and the architecture box to either adopt the same definition or explicitly re-scope.

---

### B-2. First-traversal time budget overflows by ~25%

**Where it conflicts:**

- Brief §4 (`30-ring-traversal-brief.md`): "14 vertices × ~35 min average = ~7.5 hours per full traversal … Budget per traversal: **8 hours maximum**."
- Chessboard summary (`13-chessboard-layer.md` §Summary): "Total overhead per cycle (first traversal): **~100-110 min**. After traversal 1, … overhead drops to ~30-40 min per subsequent cycle."

The chessboard overhead decomposes (per §6):
- §6.4 antipodal probes: 7 probes × ~10 min = ~70 min (first traversal only)
- §6.3 hub radiation: ~10 min when at QG5D (~once per traversal)
- §6.5 compositional cell-fill: ~5 min per vertex × 14 = ~70 min
- §1 DUAL-CHECK: ~5 min per status-changing node return × N
- §4 PIN-PRESERVATION: ~5 min per bypass/construct proposal
- §6.1 + §6.2 geometry/sector classification: ~5 min at traversal start

**Net estimate for traversal 1:** 14 × 35 min (brief) + ~100 min chessboard overhead = **~590 min ≈ 9.8 h**.

**Why it matters:** The budget is a hard exit criterion. At 8 h the runner would exit at ~vertex 10-11 with chessboard overhead unaccounted for.

**Recommended fix:** one of
- (a) Widen traversal-1 budget to 10 h explicitly (brief §4), with traversal-2+ staying at 8 h (antipodal probes done, hub radiated).
- (b) Make the chessboard primitives *lazy* in ring mode — e.g., DUAL-CHECK only on BYPASSED/CONSTRUCTED links (already status-changing), not on EXCISE-via-literature.
- (c) Move antipodal probes out of the per-traversal hot path — run them once in a dedicated pre-traversal setup session.

---

### B-3. Status vocabulary is fragmented — five partially-overlapping taxonomies

**Where they conflict:**

| Where | Codes used |
|---|---|
| PCA §P.2 (`07-proof-chain-adversarial.md`) | `OPEN / IN_PROGRESS / VERIFIED / WEAKENED / BROKEN / BYPASSED / CONDITIONAL / HONEST-STALL` |
| Brief §2 edge statuses | `STRONG / PARTIAL / CANDIDATE / SPECULATIVE` |
| Brief §3.2 link statuses | `OPEN / CONJECTURED / PROVED / LITERATURE / VERIFIED / CLOSED / HONEST-STALL` |
| Brief §3.3 cell statuses | `EMPTY / PARTIAL / FILLED` |
| Capacitor (`09-capacitor-correspondence-table-v1.md`) cells | `VERIFIED / ESTABLISHED / CONJECTURED / CANDIDATE` |
| Chessboard §3.1 (inherits PCA) | `VERIFIED / WEAKENED / OPEN / BYPASSED` |

The brief §2.2 example makes an explicit translation ("SPEC ↔ ANT … already FILLED at Tier 1 status") where FILLED (brief) = ESTABLISHED (capacitor) — but the mapping is never tabulated.

**Why it matters:** Authors read the brief + capacitor + PCA; Critics read all three. Every spawn context has to *decide* which taxonomy a given status label belongs to before it can act. This causes ambiguous critic verdicts and mis-classified node statuses.

**Recommended fix:** add a status-dictionary table to the brief (or `13-chessboard-layer.md`) with rows `Ring-mode name | PCA equivalent | Capacitor equivalent | Meaning`. Minimum rows needed:

- Link-level: PROVED/LITERATURE/CLOSED → map to PCA's VERIFIED; CONJECTURED → OPEN; CONDITIONAL stays.
- Edge-level: STRONG/PARTIAL/CANDIDATE/SPECULATIVE → map to capacitor's VERIFIED/PARTIAL/CANDIDATE/(no-cell).
- Cell-level: FILLED (brief) → VERIFIED or ESTABLISHED (capacitor); PARTIAL → PARTIAL; EMPTY → no-entry.

---

## 2. Important ambiguities (decide before traversal 1, document in brief)

### A-1. VERIFY mode is absent from the vertex protocol

**Where:**
- PCA §P.3.1 mandates: "verify ALL links that have proofs simultaneously. If the chain has 8 links with proofs, dispatch 8 Critics in the first wave. **Do not serialize.**"
- Brief §3.2: "If the weakest link is OPEN or CONJECTURED: … If the weakest link is CONDITIONAL: … **If all links are VERIFIED/PROVED: This vertex is CLOSED. Skip to edge phase.**"

The brief trusts the prior PROOF-CHAIN.md's PROVED status rather than re-verifying. This is an *override* of PCA §P.3.1 but is not declared as such (unlike §8.1's explicit override of §P.2's chain-state.md mandate).

**Why it matters:** The whole point of a ring traversal compounding over multiple passes is that past verifications can drift (new literature, refactored cells, updated dependencies). Skipping VERIFY on PROVED links means traversal-2 inherits traversal-1's trust decisions silently.

**Options:**
- (a) Declare the override: "Ring mode assumes each vertex's PROOF-CHAIN.md status is the source of truth at traversal start; VERIFY is only re-run by explicit trigger (§2.2 in the capacitor-lookup lineage, or a user §K note)." — fast but trust-heavy.
- (b) Run a lightweight verification pass: at each vertex, spawn ONE Sonnet Critic to spot-check the 2-3 highest-confidence PROVED links. If any WEAKEN → downgrade and EXCISE. Cost: ~10 min per vertex = ~140 min per traversal. Pushes budget further but preserves PCA semantics.
- (c) Run the full VERIFY wave on traversal-1 only (baseline) and skip on subsequent traversals. Amortizes cost.

### A-2. Triad wave semantics in ring mode are undefined

**Where:**
- Triad §T.3 (`12-prf-chain-advr-strat-triad.md`) triggers reference "Wave N findings" / "Wave N results."
- Triad §T.6 paces approvals as "Wave N+1 awaiting approval."
- Ring mode (brief §8.1) overrides PCA §P.2 but says nothing about Triad wave semantics.

**Options:**
- (a) **Triad fires per-traversal, not per-vertex**: at traversal-close, check the 6 triggers against the traversal's aggregate findings; propose brief upgrades between traversals. Approval gate blocks the *next* traversal, not the current vertex dispatch.
- (b) **Triad fires per-vertex**: at every vertex-close, check triggers. This will spam the user with approval requests (14× per traversal).
- (c) **Disable Triad for ring mode** (invoke backward-compat clause §T.10: "if the invocation omits the strategic triad line, the run proceeds as pure PCA"). Re-enable once ring-mode brief is stable.

Recommended: (a) — per-traversal. Add to brief §8 or §3.4 (Move phase).

### A-3. User approval gate can consume half the traversal budget

**Where:**
- Triad §T.6: user unavailable default = 30 min (interactive) / **4 h** (continuous).
- Brief §4: 8-hour traversal budget.
- Brief §8 / §8.2 does not declare whether ring mode is interactive or continuous-run.

**Consequence:** if Triad fires once per traversal (option A-2.a), and the user is structurally async, a single approval wait consumes 50% of the budget.

**Options:**
- Declare ring mode as continuous-run (matches the "structurally async caller" test in ORA §11.5 since traversals take hours).
- Shorten the ring-mode Triad wait window to ~60 min (half of vertex budget).
- Have Triad propose edits but **not block** — the proposal lands in `triad/traversal-N/mediator-proposal.md` and the runner continues; user applies edits before traversal-N+1.

### A-4. North star file doesn't contain the strategic anchors the Triad expects

**Where:**
- Triad §T.2 expects the north star to contain: Millennium Strategy, capacitor-first framing ("capacitor IS the deliverable"), publishing channel architecture, programme-level goals ("fill capacitor to 40%+ of 276 cells"), walk-back contracts.
- `publishing/strategy.md` is a *release-order* document: Wave 1 (Papers 23, 24) → Wave 2 (Paper 25 + retraction) → Wave 3 (Papers 8, 13, 26). It contains the PCGT conditional-grammar template and a dependency-verification status table. It does **not** contain the "capacitor IS the deliverable" framing or a 40% cell-fill target.

**Why it matters:** the Triad Strategist role (§T.4.2) must answer three alignment questions against the north star. If the north star is framed around publishing sequencing and the brief is framed around capacitor growth, the Strategist may either (a) return vacuous ALIGNED verdicts for lack of applicable anchors, or (b) FLAG systematic misalignment that's really just file-mismatch.

**Options:**
- (a) **Add a "Ring-mode north star section"** to `publishing/strategy.md` with: capacitor-fill target, cross-chain rigidity target, per-traversal deltas expected, closure ladder.
- (b) **Point the invocation at a different north star file** — e.g., a new `publishing/ring-mode-strategy.md` — and keep `publishing/strategy.md` as the publishing-sequence doc.
- (c) **Remove the north-star / Triad layer from this run** (backward-compat) and add it once a proper north star for ring-mode exists.

### A-5. Closure ritual triggering on ring exit is undefined

**Where:**
- ORA §13.3 + PCA §P.9 define a 5-file closure ritual (lockdown, final-adversarial-pass, referee, closure files, backup, commit memo) at item-close.
- Brief §4 defines three exit conditions: RING CLOSED / RING STRENGTHENED / RING STALLED.
- Brief §3.4 "Move phase" just writes a §K entry and advances.
- Brief §5 "What the ring-PCA produces" lists per-traversal deliverables but doesn't say whether they are produced via the ORA closure ritual or ad-hoc.

**Options:**
- **RING STRENGTHENED (typical)**: abbreviated ritual — write `programme/ring-traversal-log.md` entry + commit memo, do NOT spawn final-adversarial-pass or referee.
- **RING STALLED / RING CLOSED**: full 5-file closure ritual per ORA §13.3.

Declare this in brief §4 or §5.

---

## 3. Minor / cosmetic

### M-1. Chessboard §3 says "13 vertices" but means 14

**Where:** `13-chessboard-layer.md` §3, the RIGIDITY current-value block:

```
L_total     = 83    (sum across all 13 vertices)
```

But the ring has 14 vertices (QG5D through Schanuel). The arithmetic (83 = YM 17 + RH 6 + BSD 11 + PvNP 5 + Hodge 3 + NS 2 + GRH 0 + BC 1 + BGS 2 + 5 "others 0") is consistent with 14 vertices. Just a text typo.

**Fix:** `s/13 vertices/14 vertices/` in chessboard §3.

### M-2. Duplicate paper directories in the repo

`/Users/gsix/quantum-geometry-in-5d-latex/` contains both:
- `paper27-hodge/` AND `paper29-hodge/` (invocation uses paper29)
- `paper27-navier/` AND `paper30-navier-stokes/` (invocation uses paper30)

The invocation is unambiguous, but an Author doing a Glob for Hodge-related files could surface both. Low-priority: either delete the old `paper27-*/` directories or add a note to the brief that paper29/paper30 are canonical.

### M-3. Output directory is hardcoded to `traversal-01`

Brief §8.2 already documents: "the invocation file hardcodes `traversal-01` — for traversal 2, change to `traversal-02`; for traversal 3, `traversal-03`; and so on." and provides resume semantics. Not a conflict, just a manual step the caller must remember.

**Optional improvement:** have the runner auto-detect the next free `traversal-NN/` at bootstrap and update its output path accordingly, warning if `traversal-01/` exists without a resume marker.

### M-4. Edge-ownership vs hub-radiation interaction is under-specified

- Brief §2.1: "each edge in the ring is owned by exactly ONE vertex — the predecessor … fills the edge during its EDGE PHASE … as its LAST action."
- Chessboard §6.3: at QG5D (the hub), fill up to **13 outgoing edges in parallel**. This includes 1 ring edge (QG5D → RH) and 12 chord edges.
- Chessboard §6.5: compositional cell-fill for triangles (A, B, C) = (previous, current, next) with chord A↔C.

No direct conflict — §2.1's ownership rule is scoped to the 14 ring edges; chord edges have no single-owner rule. But the interaction is worth one explicit sentence: "Ring edges are predecessor-owned (§2.1). Chord edges have no owner — hub radiation (§6.3), compositional cell-fill (§6.5), and antipodal probes (§6.4) all fill chords and must check WIRE-DENSITY before dispatching to avoid duplicate work."

---

## 4. Summary table — severity × recommended order

| # | Severity | Fix size | Location of fix |
|---|---|---|---|
| B-1 EXCISE semantics | blocker | 1 paragraph | brief §0 glossary + chessboard §6.2 |
| B-3 status vocabulary | blocker | 1 small table | brief §0 dictionary |
| A-1 missing VERIFY | blocker-adjacent | 1 sentence + decision | brief §3.2 |
| B-2 time-budget overflow | blocker | 1 sentence + decision | brief §4 |
| A-2 Triad wave semantics | important | 1 paragraph | brief §8 |
| A-3 approval gate | important | 1 sentence | brief §8.2 (continuous-run flag) |
| A-4 north star mismatch | important | add section to `publishing/strategy.md` OR new file | north star |
| A-5 closure ritual on exits | important | 1 sentence | brief §4 or §5 |
| M-1 "13 vertices" typo | minor | `s/13/14/` | chessboard §3 |
| M-2 duplicate paper dirs | minor | optional delete or note | brief §1 or repo |
| M-3 hardcoded traversal-01 | minor | optional automation | invocation + brief §8.2 |
| M-4 edge ownership vs hub | minor | 1 sentence | brief §2.1 |

**Suggested resolution order:**
1. Fix B-1 (EXCISE glossary) + B-3 (status dictionary) — writing prep, ~15 min.
2. Decide A-1 (VERIFY policy) and B-2 (budget) together — they couple.
3. Decide A-2 + A-3 + A-4 as a Triad-integration bundle. Easiest interim: disable Triad on traversal-1 (backward-compat per §T.10), revisit once ring-mode north star exists.
4. Add A-5 closure-ritual sentence.
5. Minor cleanup M-1 through M-4 as convenient.

---

## 5. What is NOT broken (audit positive findings)

Worth recording:

- **The 14 PROOF-CHAIN.md files all exist** at the canonical paths. Ring-traversal target is reachable.
- **The canonical ring order is consistent** between the invocation (`30-ring-traversal-run.md` lines 35-49) and brief §2 table.
- **Domain codes (D1-D24)** in brief §2.2 match the capacitor's Domain index exactly.
- **Vertex-to-domain mapping** (brief §2.2) uses only the capacitor's actual codes — no invented codes.
- **RIGIDITY formula** matches between brief §5 and chessboard §3. Numeric baseline 9.03 is reproducible from the stated inputs.
- **The 5-layer read order** (ORA → PCA → Triad → Chessboard → Brief) is consistent: each layer declares which prior layers it extends, and `13-chessboard-layer.md` correctly names all three predecessors in its opening paragraph.
- **Brief §8.1 explicitly overrides PCA §P.2** (`chain/chain-state.md` mandate) with ring-mode state-management architecture. This is the *right* way to override; other overrides in the stack (e.g., A-1) should follow this pattern.
- **Brief §8.2 already handles output-directory resume semantics** — no data loss on interruption.
- **Capacitor has 44+ filled cells** across Tier 1 + Tier 2, including the critical ring-edge SPEC ↔ ANT, OA ↔ AG, and SPEC ↔ OA cells. Traversal-1 has real material to work with.
- **The PIN-TABLE referenced by chessboard Appendix A exists** at `paper12/research/23-framework-predictions-master-table.md`.

The stack is *close* to ready. The blockers above are surface-level fixes (1 paragraph + 1 table + 3 decisions), not structural redesigns.

---

*Audit complete. Awaiting user direction on which findings to address first.*
