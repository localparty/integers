# PCA Run Details — reference notes

*Companion notes for the Proof-Chain Adversarial runs. Documents what the invocation does, what the runner does at bootstrap, what happens during a run, and how memory persists (or doesn't) across runs.*

*Read this if you want to understand what's happening under the hood when you launch a run. Not required for launching — the runner reads its own instructions from `06-the-prompt.md`.*

---

## 1. Files in play at invocation

The run invocation (e.g., `10-ym-proof-chain-verifying-run.md`) specifies six paths. The runner reads them in this order at bootstrap:

| # | File | Role |
|---|---|---|
| 1 | `06-the-prompt.md` | **Instructions** — the ORA runner prompt, 19 signatures, blackboard, primitives, autonomous parallel operation, self-healing discipline |
| 2 | `07-proof-chain-adversarial.md` | **Chain mode extension** — verify/construct/bypass modes, bidirectional traversal, junction detection, cell-filling primitive |
| 3 | `08-framework-tools.md` | **Toolkit** — compiled framework knowledge (Six Patterns method, theorem catalogues, programme-specific sections) |
| 4 | `09-capacitor-correspondence-table-v1.md` | **Capacitor** — the cross-domain correspondence table (24 domains, 40 filled cells, 17 priority escape routes) |
| 5 | `paper08-yang-mills/strategy/05-chain-verification-brief.md` | **Brief (deliverable)** — the specific task for THIS run (verify all 17 proved YM links adversarially) |
| 6 | `paper08-yang-mills/chain-verification/` | **Output directory** — where blackboard, nodes, critiques, chain-state files are written. Created fresh by the PCA. |

Files 1-4 are framework-level (shared across all PCA runs, live in `millenium-apps/proof-chain-adversarial-01/`). Files 5-6 are programme-specific (live in the paper's own directory).

---

## 2. What the brief tells the PCA for the YM run

- **Verify all 17 proved YM links adversarially** (Links 1-17 from `preprint/PROOF-CHAIN.md`)
- **Attack from both ends in parallel**: forward agents on Links 1-9, backward agents on Links 17-10
- **Do NOT re-attempt H4 closure** — the H4 closure programme (2026-04-11) already adjudicated this. Just verify Link 18 is correctly labeled CONDITIONAL on H4 in W7-14 §5.3 mildest form.
- **Use the capacitor for bypasses** if any link WEAKENS during verification
- **Success criteria**: CHAIN CLOSED (all 17 SURVIVED + Link 18 correctly CONDITIONAL) / CHAIN STRENGTHENED (some WEAKENED and repaired) / CHAIN AT RISK (any BROKEN without successful construct or bypass) — all three are honest outcomes

---

## 3. What the runner does at bootstrap

1. Read `06-the-prompt.md` end-to-end → internalize 19 signatures, blackboard structure, primitives, 9-layer drift defense, self-healing discipline (§14.10), autonomous parallel operation (§0 CRITICAL blocks)
2. Read `07-proof-chain-adversarial.md` → activate chain-mode extensions (verify/construct/bypass, bidirectional, junction detection)
3. Read `09-capacitor-correspondence-table-v1.md` → internalize 40 filled cells, especially Tier 1 (load-bearing for YM) and priority cells for H4 (PROB↔SPEC, THERMO↔QFT, MICRO↔QFT)
4. Read `08-framework-tools.md` → framework catalogues, YM programme-specific sections (H.2 + I.2 YM proof chain)
5. Read `05-chain-verification-brief.md` → the specific task
6. Map the 18-link chain to `chain/chain-state.md` in the output directory
7. Create the blackboard at `paper08-yang-mills/chain-verification/blackboard.md` with §A-§O
8. REFRAME on §C + capacitor scan
9. Plan: identify forward and backward frontiers
10. Dispatch: 17 Critics in parallel (one per proved link) in Wave 1

---

## 4. What happens during a run

| Step | Action | Note |
|---|---|---|
| Wave 1 | Dispatch 17 Critics in parallel | One per proved link. Forward: Links 1-9. Backward: Links 17-10. |
| Return | Collect SURVIVED / WEAKENED / BROKEN verdicts | Each Critic writes to `critiques/<link-id>-cycle-1.md` |
| Update | Chain state updated per verdict | `chain/chain-state.md` gets per-link status changes |
| Junction check | Test if forward + backward fronts meet | Run at every cycle-close |
| Handle weakenings | For each WEAKENED link, dispatch Construct Author | Wave 2: repair agents |
| Handle breaks | For each BROKEN link, enter Bypass mode | Scan capacitor row for the link's domain; find escape route via transposition |
| Cycle autonomously | REFRAME → Plan → dispatch → collect → update → repeat | No pausing. No asking. Until CLOSED / STRENGTHENED / STALLED. |

**One caveat**: the PCA has not been run before on a real chain verification. Expect self-healing events — the runner will catch bundle-level failure modes during its first real run and patch them in place, logging to `08-changelog.md` as new `I-v6-N` entries. That's by design; the changelog grows.

---

## 5. Memory persistence across runs

### What DOES persist (built into the architecture)

| Memory layer | Persistence | What it remembers |
|---|---|---|
| **Capacitor** (`09-capacitor-correspondence-table-v1.md`) | Cross-run (shared file) | Filled cells = correspondences discovered in any prior run. Every cell fill becomes a permanent escape route for all future runs. |
| **Bundle changelog** (`08-changelog.md` in ORA v8) | Cross-run (shared file) | Every `I-v6-N` patch = a failure mode the bundle has learned to prevent. Each future runner reads this at bootstrap. |
| **Toolkit** (`08-framework-tools.md`) | Cross-run within a programme | Verified results, deployable cards, kill list summaries that get folded back at programme-close. |
| **Trajectory library** (`experience/reframes/`, `experience/heuristics/`) | Cross-run (shared) | Successful REFRAMEs and heuristics, cited by future REFRAME invocations per Sig 5. |

### What does NOT persist by default

| Memory layer | Scope | Why |
|---|---|---|
| **§F kill list** | Per-programme (in the run's blackboard) | Each new output directory gets a fresh blackboard with a fresh §F. |
| **§K commit memos** | Per-programme | Same — fresh blackboard. |
| **§I notes** (CONCERN / CASCADE / LESSON / CALLOUT) | Per-programme | Same. |
| **Chain state** | Per-run | Each run tracks its own chain in `chain/chain-state.md`. |

### How to make kills persist across runs

Two practical options:

1. **Reuse the same output directory** across sessions. The PCA will continue the existing programme (same blackboard, same accumulating §F) rather than starting fresh.
2. **Fold kills into the toolkit or capacitor at programme-close.** Each kill becomes either a toolkit entry (with re-entry gate) or a negative-status capacitor cell ("this transposition does NOT work because [reason]"). The capacitor grows with both successful escape routes AND known dead ends.

For this YM run specifically: the H4 closure programme already produced K-1 (CCM port) and K-2 (spectral action) kills, documented in `paper08-yang-mills/closing-H4/closure/closure-corrections.md`. The brief references that file (load-bearing files table, priority 6) so the PCA reads it at bootstrap and treats those kills as known starting context.

---

*End of run details. The runner does not need to read this file — it reads `06-the-prompt.md` and follows that. This file exists for human-facing documentation of what the system does.*
