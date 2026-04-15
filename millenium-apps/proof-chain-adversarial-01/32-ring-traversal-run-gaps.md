# Ring-Traversal Run — Second-pass Gap Audit

*A delta audit of the 5-layer instruction stack for the ring-traversal PCA run, conducted after the fixes from `31-ring-traversal-run-gaps.md` were applied. Date: 2026-04-13. Audit by: Claude Opus 4.6.*

*Scope: re-read every file listed in `30-ring-traversal-run.md` end-to-end, verify prior-audit fixes landed, check companion-file resolvability for `06-the-prompt.md`'s internal references, confirm the 14 target PROOF-CHAIN.md files exist, check the output directory. This audit composes with (does NOT replace) `31-ring-traversal-run-gaps.md`.*

---

## 0. Files audited and state

| # | Role | Path | State |
|---|---|---|---|
| 1 | Invocation | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-run.md` | read |
| 2 | ORA base | `millenium-apps/proof-chain-adversarial-01/06-the-prompt.md` | read (1318 lines) |
| 3 | PCA chain mode | `millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md` | read (348 lines) |
| 4 | Strategic triad | `millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md` | read (444 lines) |
| 5 | Chessboard layer | `millenium-apps/proof-chain-adversarial-01/13-chessboard-layer.md` | read (531 lines) |
| 6 | Brief (deliverable) | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-brief.md` | read (454 lines) |
| 7 | Toolkit | `millenium-apps/proof-chain-adversarial-01/08-framework-tools.md` | read (553 lines) |
| 8 | Capacitor | `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` | read (283 lines) |
| 9 | North star | `publishing/strategy.md` | read (671 lines) |
| 10 | Prior audit | `millenium-apps/proof-chain-adversarial-01/31-ring-traversal-run-gaps.md` | read (257 lines) |
| 11 | 14 PROOF-CHAIN.md files | paper{1,08-yang-mills,13-rh,13b-grh,25-hilbert-12,26-bsd,28-pvnp,29-hodge,30-navier-stokes,31-baum-connes,32-bgs-spectral-statistics,33-goldbach,34-twin-primes,35-schanuel}/PROOF-CHAIN.md | all 14 present ✓ |
| 12 | Output dir | `programme/ring-traversals/` | exists, EMPTY (fresh start) |

**Headline**: the prior audit's ten fixes (B-1, B-2, B-3, A-1 through A-5, M-1, M-2/M-3/M-4 notes) landed in the brief and `publishing/strategy.md` Appendix B. **One new blocker surfaces in this pass that the prior audit did not check: the base prompt `06-the-prompt.md` has twenty-two unresolved internal references to companion files that do not live in this bundle.**

---

## 1. New blocker surfaced in this audit

### B-4. `06-the-prompt.md` references five companion files that are not in the bundle directory

**What `06-the-prompt.md` actually is:** it is a byte-for-byte copy of `online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md`. The file refers to itself throughout as `01-the-prompt.md` (e.g., §10.7 "This file (`01-the-prompt.md`) is intended to be placed in the `system` field", §5.3 "Before writing the Author's spawn prompt…", §6 "If the toolkit/capacitor and the spawn templates below ever diverge, the toolkit/capacitor is canonical"). The rename to `06-the-prompt.md` was done to fit this bundle's numbering scheme, but the internal self-references were not updated.

**The unresolved references (count: 22 across 5 files):**

| Referenced file | Purpose inside the prompt | Where it is cited | Present in `proof-chain-adversarial-01/`? | Present in `ora-bundle-v8/`? |
|---|---|---|---|---|
| `08-changelog.md` | MANDATORY bootstrap read (§0 step 7); self-healing log target (§14.10); bootstrap input for next runner (§14.10 closing) | §0.7, §2 Signature 14.10, §14.10 (7 refs), §16 | **no** | yes |
| `02-rationale.md` | Design reasoning; cited from §0 ("See `02-rationale.md` in this bundle"), §2 (Layer L mining provenance, §13), §15 (empirical grounding), §16 (minimal instruction step 2) | §0, §2 (3 refs), §15, §16 | **no** | yes |
| `03-synthesis-spawn.md` | Synthesis agent prompt template (§5.7, §6.5) | §0, §5.7, §6.5, §11.5 | **no** | yes |
| `04-closure-templates.md` | 5-file closure ritual templates (§9, §13.1, §13.3) | §0, §9, §13.3, §14.1 | **no** | yes |
| `06-anti-overfit-discipline.md` | Anti-predictions A-1…A-4 (self-heal gate §14.10 step 4); Signature 16 provenance; Signature 18 provenance; the bundle's immune-system file | §2 (multiple), §14.10 step 4 | **no** | yes |

**Also cross-referenced but outside the per-prompt-bundle scope:**
- `15-v5-predictions.md` (cited at §2 Signature 17 as "refutes the prediction in `15-v5-predictions.md` P5-2") — not in either directory; a v5-era file.
- `07-changelog-v5-to-v6.md` (cited at §14.10) — not in either directory; a v5→v6 migration artifact.
- `solutions-with-prize/paper08-yang-mills/research/36-the-method.md` + `integers/paper12-cbb-system/research/214-the-method-six-patterns.md` (§7) — these EXIST and are load-bearing (they ARE the 6-step inner loop). Not part of this blocker.

**Why the missing five matter**:

1. **§0 bootstrap step 7 is mandatory, not optional**: *"Read `08-changelog.md` end-to-end as part of bootstrap. Every `I-v6-N` entry is a failure mode the bundle has learned to prevent from a prior run — internalize them before your first cycle dispatches."* If the runner resolves this literally against the CWD or the bundle dir, it fails. If the runner falls back to Glob, it may pick up `ora-bundle-v6/08-changelog-v6.md` or `ora-bundle-v8/08-changelog.md` — the latter is correct; the former is stale.

2. **§14.10 self-healing is unusable without `08-changelog.md` + `06-anti-overfit-discipline.md`**: the protocol says the runner MUST append a new `I-v6-N` entry to `08-changelog.md` BEFORE applying an in-run patch, AND re-audit the patch against anti-predictions A-1 through A-4 per `06-anti-overfit-discipline.md §3`. Without both files resolved, the self-healing immune system is dormant.

3. **§13.3 item-close requires `04-closure-templates.md`**: *"Write 5 closure files (using templates from `04-closure-templates.md`): moment, reflection, corrections, resume, digest."* Without the templates, the RING CLOSED outcome's full ritual (brief §8.4) has no source for the 5-file shapes.

4. **Every Synthesis spawn (brief mandates these at wave-boundaries) needs `03-synthesis-spawn.md`**: §5.7 and §6.5 both say *"spawn a Synthesis agent using `03-synthesis-spawn.md` as the prompt template"*. Without it, the Synthesis primitive has no spawn shape.

5. **§2 Signature 17 (resume re-anchor) cites `15-v5-predictions.md` P5-2 for the polarity discrimination discipline**: this is the empirical provenance for not re-anchoring on a leaving-marker. If a runner tries to read it to understand "why P5-2" for edge-case calibration, it fails. Low severity (the discipline is fully stated inline) but worth flagging.

**Concrete impact on traversal-01 bootstrap**:

Reading the `06-the-prompt.md` file literally, the runner's bootstrap sequence at §0 is:
1. Read deliverable end-to-end (`30-ring-traversal-brief.md`). ✓ resolvable.
2. Classify it (multi-item, the ring is 14 items). ✓ resolvable.
3. Write deliverable path to §A. ✓ resolvable.
4. Read companion files in priority order. ✓ resolvable (brief's citations all exist).
5. Locate voice canon seed. ✓ resolvable (multiple candidates in the corpus).
6. Invoke session-open ritual (§11). ✓ resolvable (§11 is inline in the prompt).
7. **Read `08-changelog.md` end-to-end.** ✗ file not co-located.

Step 7 is the first hard failure. Everything downstream that references self-healing / synthesis / closure templates / anti-overfit is downstream of that.

**Three fix options (same as summarized in oral audit):**

- **Option 1 — add a companion-path line to the invocation.** Lowest-effort. Change `30-ring-traversal-run.md` to include:

  > *companion files for the base prompt (`02-rationale.md`, `03-synthesis-spawn.md`, `04-closure-templates.md`, `06-anti-overfit-discipline.md`, `08-changelog.md`) live at `online-researcher-adversarial/ora-bundle-v8/` — resolve unqualified references there.*

  Zero file moves, one sentence in the invocation, all internal references resolvable with a path qualifier. Risk: the runner must know to apply the qualifier to every unqualified companion reference it encounters during a run, not just at bootstrap.

- **Option 2 — symlink or copy the five files into this bundle.**
  ```
  ln -s ../../online-researcher-adversarial/ora-bundle-v8/02-rationale.md          millenium-apps/proof-chain-adversarial-01/02-rationale.md
  ln -s ../../online-researcher-adversarial/ora-bundle-v8/03-synthesis-spawn.md    millenium-apps/proof-chain-adversarial-01/03-synthesis-spawn.md
  ln -s ../../online-researcher-adversarial/ora-bundle-v8/04-closure-templates.md  millenium-apps/proof-chain-adversarial-01/04-closure-templates.md
  ln -s ../../online-researcher-adversarial/ora-bundle-v8/06-anti-overfit-discipline.md millenium-apps/proof-chain-adversarial-01/06-anti-overfit-discipline.md
  ln -s ../../online-researcher-adversarial/ora-bundle-v8/08-changelog.md          millenium-apps/proof-chain-adversarial-01/08-changelog.md
  ```
  Pro: every self-reference in `06-the-prompt.md` resolves by unqualified name without the runner having to know about the qualifier. Con: introduces a numbering collision — this bundle already has `08-framework-tools.md` at slot 08; the symlink `08-changelog.md` would sit next to it. And this bundle's `06-the-prompt.md` would live next to an unrelated `06-anti-overfit-discipline.md` (both starting with 06). Resolvable by renaming the symlinks (e.g., `v8-08-changelog.md`) but that re-introduces the qualification problem.

- **Option 3 — repoint the invocation at `ora-bundle-v8/` for the base prompt.** Change `30-ring-traversal-run.md` line 2 to `ora-bundle-v8/01-the-prompt.md`, and keep the PCA/Triad/Chessboard extensions where they are at `proof-chain-adversarial-01/`. The base prompt then resolves all its unqualified references inside its native bundle (where all five companions live), and the extensions sit alongside.

  Pro: cleanest separation — the base prompt stays in its own bundle with its companions; the extensions (which are ring/chain/triad-specific) live in the ring-mode bundle. Con: requires the caller to remember the split; someone reading `30-ring-traversal-run.md` sees two bundle dirs referenced instead of one.

**Recommendation: Option 1.** It is the smallest change (one sentence), it preserves the current directory layout, and it matches the invocation's existing discipline of being explicit about paths. Options 2 and 3 are acceptable alternatives if the caller prefers either file-colocation or bundle-purity over a one-line qualifier.

---

### B-5. Self-name drift in `06-the-prompt.md` and `08-framework-tools.md`

**What I found:**

- `06-the-prompt.md` refers to itself as `01-the-prompt.md` throughout (§10.7, §6, §5.3, …). The content matches `ora-bundle-v8/01-the-prompt.md` byte-for-byte.
- `08-framework-tools.md` closes with *"End of `05-framework-tools.md`. This file is the inventory; selective inclusion of these tools in Author / Critic / Synthesis / Referee spawn contexts is implemented in `01-the-prompt.md` §6.1 / §6.2 / §6.5 / §6.6."* The content matches `ora-bundle-v8/05-framework-tools.md` (verified by comparing the v8 directory listing).

**Why it matters:**

The invocation (`30-ring-traversal-run.md`) specifies the files by their *actual* paths (`06-the-prompt.md`, `08-framework-tools.md`), so the bootstrap read succeeds. But once the runner is inside either file, every self-reference *inside the prompt* uses the old name. If the runner ever tries to re-read or grep for its own instruction file by its internal name, it fails. A future agent that writes a §K note citing "see `01-the-prompt.md` §6.1 for the Author spawn context" will be pointing to a path that does not exist in this bundle.

**Severity:** minor for traversal-01 (invocation paths are explicit), but it accumulates risk across cycles and is a correctness-smell.

**Fix options:**

- **(a) Textual rename inside the files.** `s/01-the-prompt.md/06-the-prompt.md/g` in `06-the-prompt.md`; `s/01-the-prompt.md/06-the-prompt.md/g` and `s/05-framework-tools.md/08-framework-tools.md/g` in `08-framework-tools.md`. Preserves the copies, fixes all self-references.
- **(b) Declare a rename map in the invocation.** A single block in `30-ring-traversal-run.md` stating "within this bundle, `01-the-prompt.md` → `06-the-prompt.md`, `05-framework-tools.md` → `08-framework-tools.md`." Simpler but the runner has to remember to translate on every read.

Recommendation: **(a)** — the rename is a one-shot find-replace and it eliminates the drift permanently.

---

## 2. Prior-audit fixes: verification status

All of the following were flagged in `31-ring-traversal-run-gaps.md` and claimed fixed. I re-verified by reading the relevant sections:

| Prior # | Prior-audit severity | Fix verified at | Verdict |
|---|---|---|---|
| B-1 EXCISE semantics | blocker | Brief §0.1 — explicit three-step ladder EXCISE → CONSTRUCT → BYPASS; notes the chessboard §6.2 Type B and architecture box usage; states "EXCISE is NOT a rename of PCA's BYPASS; EXCISE precedes it" | **FIXED** |
| B-2 time-budget overflow | blocker | Brief §4 — traversal-1 widened to 10 h, traversal-2+ stays at 8 h; explicit accounting for chessboard overhead | **FIXED** |
| B-3 status vocabulary | blocker | Brief §0.2 — three cross-layer mapping tables (link-level, edge-level, cell-level) | **FIXED** |
| A-1 missing VERIFY | blocker-adjacent | Brief §3.2 — traversal-1 spot-check policy (1 Sonnet Critic per vertex, 2-3 PROVED links) + traversal-2+ trust-or-trigger policy; explicit PCA §P.3.1 override | **FIXED** |
| A-2 Triad wave semantics | important | Brief §8.3 — per-traversal firing, non-blocking, NN-numbered output dirs; explicit override of Triad §T.3 and §T.6 | **FIXED** |
| A-3 approval gate | important | Brief §0.4 + §8.3 — ring mode declared CONTINUOUS-RUN; Triad proposals non-blocking | **FIXED** |
| A-4 north star mismatch | important | `publishing/strategy.md` gains Appendix B (B.1 meta-goal, B.2 capacitor-fill target, B.3 rigidity target, B.4 per-traversal deltas, B.5 closure ladder, B.6 walk-back contract, B.7 alignment check questions) | **FIXED** |
| A-5 closure ritual on exits | important | Brief §8.4 — ABBREVIATED / FULL / MEDIUM ritual by exit condition; explicit override of ORA §13.3 and PCA §P.9 | **FIXED** |
| M-1 "13 vertices" typo | minor | Chessboard §3 now says "14 vertices" at both call sites (lines 131, 143) | **FIXED** |
| M-2 duplicate paper dirs | minor | Brief §0.3 adds a paragraph noting `paper27-hodge/` and `paper27-navier/` are archive-only (canonical are `solutions-with-prize/paper29-hodge/` and `solutions-with-prize/paper30-navier-stokes/`); the old directories remain on disk | **DOCUMENTED, NOT DELETED** |
| M-3 hardcoded traversal-01 | minor | Brief §8.2 documents the NN-swap for subsequent traversals + resume semantics | **DOCUMENTED** |
| M-4 edge ownership vs hub | minor | Brief §2.1 adds an "Edge ownership (disambiguation)" subsection with the ring-edges vs chord-edges split | **FIXED** |

All twelve items from the prior audit are either fixed or adequately documented. **No regressions.**

---

## 3. Positive findings (carried forward + new)

- **All 14 PROOF-CHAIN.md files exist** at the canonical paths. Ring-traversal target is reachable.
- **Canonical ring order is consistent** across four places: invocation (`30-ring-traversal-run.md` lines 35-49), brief §2 table (lines 103-118), chessboard Appendix C SECTOR-TABLE (lines 481-494), chessboard §6.4 antipodal pairs (lines 350-356).
- **Domain codes (D1-D24)** in brief §2.2 match the capacitor's Domain index exactly.
- **Vertex-to-domain mapping** (brief §2.2) uses only the capacitor's actual codes.
- **RIGIDITY formula** matches between brief §5 and chessboard §3. Numeric baseline 9.03 = (44/276) × (47/83) × (36/36) × 100 is reproducible from the stated inputs.
- **The 5-layer read order** (ORA → PCA → Triad → Chessboard → Brief) is consistent: each layer declares which prior layers it extends.
- **Brief §8.1 explicitly overrides PCA §P.2** (`chain/chain-state.md` mandate) with ring-mode state-management architecture. The override is the *right* way — ring-mode tracks state across 14 in-situ PROOF-CHAIN.md files rather than one unified chain-state file.
- **Brief §8.2 handles output-directory resume semantics** — no data loss on interruption.
- **Capacitor has 44 filled cells** across Tier 1 + Tier 2, including the ring-edge SPEC ↔ ANT, OA ↔ AG, and SPEC ↔ OA cells. Traversal-1 has real material to work with.
- **The PIN-TABLE** referenced by chessboard Appendix A exists at `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md`.
- **Brief § status dictionary (§0.2)** covers all five partially-overlapping taxonomies identified in the prior audit. A runner who reads §0 internalizes the canonical mapping before hitting any section that uses a status code.
- **Brief § EXCISE glossary (§0.1)** defines the capacitor-aware triad EXCISE / CONSTRUCT / BYPASS and explicitly states the relationship to PCA's underlying verify / construct / bypass. The definition survives grep against the chessboard file (§6.2 Type B is consistent with "try EXCISE first at this vertex").
- **Appendix B of `publishing/strategy.md`** supplies the ring-mode north star content the Triad Strategist (§T.4.2) needs: capacitor-fill target (40% of 276), rigidity target (≥50 after T5), per-traversal deltas, walk-back contract, and three explicit alignment-check questions. The Triad can now fire without falling through to vacuous ALIGNED verdicts.
- **`08-framework-tools.md` is invoked as the toolkit** per `30-ring-traversal-run.md`. The file's own header says it is a *reference index* not a runtime file; but the invocation treats it as the toolkit/capacitor-alongside per ORA v8 §0 step (b). Semantically consistent even though the file's self-description says otherwise — the invocation elevates it to runtime status for this run. The toolkit's §A (Six Patterns method) and §E (anchor document) always-includes are actionable as spawn-context injections.

---

## 4. Open items from prior audit not blocking but worth noting

- **M-2 still has physical duplicate directories on disk.** The brief handles this via a documentation note, but an Author running `Glob` for Hodge- or Navier-related files will surface both `paper27-*/` and `paper29-*/` / `paper30-*/`. The runner's instruction *"do not update `paper27-*/`"* (brief §0.3) depends on the Author reading the brief first. Cheap follow-up: delete or archive the `paper27-hodge/` and `paper27-navier/` directories outside a live run.
- **M-3 hardcoded `traversal-01`**: the brief documents the NN-swap procedure and resume semantics, so this is not a data-safety issue — but it is an unforced manual step the caller repeats per traversal. Cheap follow-up: auto-detect the next free `traversal-NN/` at bootstrap. Not load-bearing.

---

## 5. Summary table — severity × recommended order

| # | Severity | Fix size | Location of fix | Priority |
|---|---|---|---|---|
| **B-4** companion files for base prompt | **blocker** | 1 sentence (Option 1) OR 5 symlinks (Option 2) OR 1 path change (Option 3) | `30-ring-traversal-run.md` OR bundle dir OR invocation | **do before traversal-1 bootstrap** |
| **B-5** self-name drift inside copies | minor-to-moderate | find-replace in `06-the-prompt.md` + `08-framework-tools.md` | in-place | optional; do before cycle 2 if not before traversal-1 |
| M-2 residual paper27 dirs on disk | minor | delete / archive | repo | convenient follow-up |
| M-3 hardcoded traversal-01 | minor | auto-detection logic | invocation + brief §8.2 | convenient follow-up |

**Suggested resolution order:**

1. **Fix B-4** (~5 min): add the one-sentence companion-path qualifier to `30-ring-traversal-run.md`. This unblocks §0 bootstrap step 7 and every downstream reference to self-healing / synthesis / closure / anti-overfit.
2. **Fix B-5** (~2 min): find-replace the self-references in `06-the-prompt.md` and `08-framework-tools.md`.
3. Start traversal-1.
4. Clean up M-2 and M-3 at leisure between traversals.

---

## 6. What changed between this audit and `31-ring-traversal-run-gaps.md`

- Prior audit inspected: invocation + all 8 stack files + 14 PROOF-CHAIN.md + PIN-TABLE + output directory.
- This audit inspected: **everything the prior audit inspected + a diff between `06-the-prompt.md` and `ora-bundle-v8/01-the-prompt.md` + a filesystem check on every file `06-the-prompt.md` internally references + a grep verification that the prior-audit fixes landed in the brief and strategy.md Appendix B.**
- The prior audit's 12 items are closed. **One new blocker (B-4) and one new minor item (B-5) surfaced by widening the audit scope to companion-file resolvability.** These were not in scope for the prior audit.

---

## 7. One-paragraph runner bootstrap status

The ring-traversal PCA stack is 98% ready. All 14 target vertices exist, the ring order is consistent, the domain codes match, the status taxonomies have a cross-layer dictionary, the RIGIDITY baseline is reproducible, the north star has a ring-mode section, the chessboard's experimental pins are on disk, the closure ritual has three exit forms, and the Triad fires per-traversal non-blocking. The one remaining blocker is that `06-the-prompt.md` internally cites five companion files (`02-rationale.md`, `03-synthesis-spawn.md`, `04-closure-templates.md`, `06-anti-overfit-discipline.md`, `08-changelog.md`) that live in `online-researcher-adversarial/ora-bundle-v8/` rather than in this bundle. A one-sentence qualifier in the invocation, a symlink sweep, or a repoint of the base-prompt path — any of the three resolves the blocker. Once resolved, traversal-1 can dispatch.

---

*Audit complete. This file composes with `31-ring-traversal-run-gaps.md`; neither supersedes the other. The prior audit addressed ring-mode-specific conflicts in the stack layers (B-1 through A-5, M-1 through M-4). This audit addresses the orthogonal question of whether the base prompt's companion files are reachable from this bundle (B-4, B-5). Awaiting user direction on which findings to address first.*
