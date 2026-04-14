# Ring-Traversal Run — Fourth-pass Gap Audit

*A delta audit of the 5-layer instruction stack for the ring-traversal PCA run, conducted after the fixes from `31-ring-traversal-run-gaps.md`, `32-ring-traversal-run-gaps.md`, and `33-ring-traversal-run-gaps.md` were at least partly applied (the W1/W2 cascade propagation is now visible in chessboard §3, `publishing/strategy.md` Appendix B §B.3, and `programme/ring-traversal-log.md` baseline; brief §8 has been rewritten to point at run.md as canonical; §2.1 has the ring-closure boundary condition and ring-edges-as-transposition-challenges paragraphs; §3.2 T1 VERIFY-skip policy is in place; §4 budget accounting is now explicit). Date: 2026-04-14. Audit by: Claude Opus 4.6 (1M context).*

*Scope: re-read `30-ring-traversal-run.md` + the full 5-layer stack end-to-end; verify every blocker called out in audits 31/32/33 either landed or is still pending; numerically cross-check RIGIDITY, fill rate, and link counts across all sites that cite them; walk paper1's `Foundation exports` table against chessboard §6.3 hub-radiation protocol; verify the companion-files qualifier resolves at the filesystem level; check §8.1 output-directory naming conventions for load-bearing ambiguity; confirm the output dir parent state; verify the 14 PROOF-CHAIN.md files still all present. This audit COMPOSES with (does NOT replace) 31, 32, 33 — none of the prior audits' findings are dismissed; only new findings are added, and prior findings are tracked for verification of fix-application.*

---

## 0. Files audited and state

| # | Role | Path | State | Notes |
|---|---|---|---|---|
| 1 | Invocation | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-run.md` | read (57 lines) | Includes companion-files qualifier (Option 1 applied from audit 32 B-4) + archival-snapshot note for local `06-the-prompt.md`. No further change vs audit 33 state. |
| 2 | ORA base (active) | `online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md` | too-large-to-read-inline; companions verified via `ls` | All five required companions present: `02-rationale.md`, `03-synthesis-spawn.md`, `04-closure-templates.md`, `06-anti-overfit-discipline.md`, `08-changelog.md`. Also: `05-framework-tools.md`, `AUDIT.md`, `README.md`, `p-v-np-toolkit/` subdir. |
| 3 | ORA base (archival copy) | `millenium-apps/proof-chain-adversarial-01/06-the-prompt.md` | not re-read this pass | Audit 32's B-5 self-name drift (file self-refers as `01-the-prompt.md`) is documented as "optional cosmetic." Still accurate since run.md declares the file archival and redirects the runner to the v8 active copy. |
| 4 | PCA chain mode | `millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md` | read (348 lines) | §P.11 invocation template STILL uses placeholder `<path>/pca/01-proof-chain-adversarial.md` — audit 33's M-5 is UNFIXED. |
| 5 | Strategic triad | `millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md` | read (444 lines) | §T.10 invocation template STILL uses placeholders `<path>/pca/01-proof-chain-adversarial.md` and `<path>/pca/02-prf-chain-advr-strat-triad.md` — audit 33's M-5 is UNFIXED. |
| 6 | Chessboard layer | `millenium-apps/proof-chain-adversarial-01/13-chessboard-layer.md` | read (551 lines) | §3 RIGIDITY now 10.63 with QG5D-inclusion convention declared (audit 33 B-7 FIXED). §6.2 SECTOR-TABLE (Appendix C) refreshed to post-cascade confidences (QG5D 10/10, YM 9.5/10, NS 4/10) (audit 33 B-8 FIXED at SECTOR-TABLE site). §6.6 chord/ring fill rate now declared "to be computed at T1 bootstrap" (audit 33 A-8 FIXED). **§6.3 hub-radiation "13 outgoing edges" vs brief §2.1 predecessor-ownership is newly surfaced — see B-9 below.** §5 WIRE-DENSITY matrix label still "2026-04-13, estimated" — newly surfaced (see M-11). |
| 7 | Brief (deliverable) | `millenium-apps/proof-chain-adversarial-01/30-ring-traversal-brief.md` | read (454 lines) | §8 invocation template collapsed into a pointer to run.md (audit 33 B-6 FIXED). §0.2 status dictionary, §0.1 EXCISE glossary, §2.1 Ring-closure boundary condition T1, §2.1 ring-edges-as-transposition-challenges, §3.2 T1 VERIFY-skip, §4 10h ceiling + post-trims 9.8h, §8.3 non-blocking triad all present. **§5 "from current 16.3%" disagrees with the 16.0% baseline used in the five other sites that cite capacitor fill rate — see M-12 below.** §8.1 `<vertex-name>.md` naming convention is unspecified — see A-11 below. |
| 8 | Toolkit | `millenium-apps/proof-chain-adversarial-01/08-framework-tools.md` | read (header + close) | Audit 33 A-10 FIXED — new line 3 "RING-MODE EXCEPTION" paragraph resolves the "NOT a runtime file" self-identification trap. Closing line 555 now correctly self-refers as `08-framework-tools.md`. Internal references to `01-the-prompt.md` inside §F-§I resolve correctly via run.md's companion-file qualifier (they point at the active v8 base prompt's sections, which do exist). |
| 9 | Capacitor | `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` | read (header + statistics + update sections) | **Top-of-file "Table statistics (v1)" section at lines 223-235 STILL shows "Total filled: 40 \| Fill rate: 14.5%" — audit 33's M-6 is UNFIXED.** The later "Statistics update (v1 + H4 Wave 1)" section (lines 267-277) and the closing attribution (lines 283-285) both show 44 / 16.0%. Two-state file; reader-dependent. |
| 10 | North star | `publishing/strategy.md` | read Appendix B | Appendix B §B.2 baseline 44/276 = 16.0% ✓. Appendix B §B.3 baseline RIGIDITY 10.63 ✓ (matches chessboard §3 + log baseline). Internal consistency within Appendix B preserved. |
| 11 | Prior audit 1 | `millenium-apps/proof-chain-adversarial-01/31-ring-traversal-run-gaps.md` | re-read selectively | 12 items B-1..A-5 + M-1..M-4. All FIXED / DOCUMENTED per audits 32/33. |
| 12 | Prior audit 2 | `millenium-apps/proof-chain-adversarial-01/32-ring-traversal-run-gaps.md` | re-read selectively | 2 items B-4 (companion files) + B-5 (self-name drift). B-4 is FIXED. B-5 remains open (cosmetic). |
| 13 | Prior audit 3 | `millenium-apps/proof-chain-adversarial-01/33-ring-traversal-run-gaps.md` | read end-to-end | 3 blockers (B-6, B-7, B-8) + 5 important items (A-6..A-10) + 4 minor items (M-5..M-8) + 2 info items (M-9, M-10). Of the three BLOCKERS: B-6 ✅ FIXED (brief §8 now a pointer to run.md). B-7 ✅ FIXED (chessboard §3 now declares convention + 10.63 computed). B-8 ✅ FIXED (log baseline refreshed, Appendix B §B.3 refreshed, SECTOR-TABLE refreshed). Of the A-items: A-6 ✅ FIXED (§2.1 ring-closure boundary), A-7 ✅ PARTIAL (trims documented — budget now 9.8h after trims; see verification in B-10 below), A-8 ✅ FIXED (§6.6 T1-compute), A-9 ✅ FIXED (§2.1 transposition-challenges paragraph), A-10 ✅ FIXED (08-framework-tools.md RING-MODE EXCEPTION paragraph). Of the M-items: M-5 ❌ UNFIXED, M-6 ❌ UNFIXED, M-7 ✅ FIXED (log baseline refreshed), M-8 ✅ FIXED (SECTOR-TABLE refreshed). |
| 14 | 14 PROOF-CHAIN.md files | paper{1,08-yang-mills,13-rh,13b-grh,25-hilbert-12,26-bsd,28-pvnp,29-hodge,30-navier-stokes,31-baum-connes,32-bgs-spectral-statistics,33-goldbach,34-twin-primes,35-schanuel}/PROOF-CHAIN.md | `Glob paper*/PROOF-CHAIN.md` returns exactly 14 entries | Confirmed via glob. No `paper27-*/PROOF-CHAIN.md` at top level (concern from audits 31/32 stays resolved). |
| 15 | PIN-TABLE | `paper12/research/23-framework-predictions-master-table.md` | presence-only check | Present. Load-bearing for PIN-PRESERVATION / DUAL-CHECK per chessboard Appendix A. |
| 16 | Output dir (parent) | `programme/ring-traversals/` | exists, EMPTY | `traversal-01/` not yet created — runner creates at bootstrap per ORA v8 §14.1. |
| 17 | Archive dirs | `paper27-hodge/`, `paper27-navier/` | exist on disk; no top-level PROOF-CHAIN.md | The ring Glob is clean. Only deep Globs inside their subdirs would surface paper27 content. Discipline from brief §0.3 still adequate. |

**Headline**: the ring stack has advanced materially since audit 33. Of the 3 blockers named in audit 33, **all 3 are fixed.** Of the 5 important items (A-6..A-10), **all 5 are fixed or adequately mitigated.** Of the 4 minor items (M-5..M-8), **2 are fixed** (M-7 log, M-8 SECTOR-TABLE) **and 2 are still open** (M-5 PCA/Triad placeholder invocation templates, M-6 capacitor top-stats staleness). **This audit surfaces 1 new blocker (B-9 hub-radiation edge-count mismatch), 1 new ambiguity (A-11 vertex-name file-naming convention), and 3 new minors (M-11 WIRE-DENSITY matrix staleness label, M-12 brief §5 16.3% vs 16.0% cosmetic arithmetic, M-13 paper1 tree-vs-chain structural note).** Plus an explicit verification-pass observation: **budget arithmetic from audit 33 A-7 is now reconcilable at 9.8 h but the VERIFY spot-check skip is declared for T1 only — T2+ budget of 8 h does not re-accommodate VERIFY unless further trims are declared (see B-10 below).** The stack is ~97% ready. The remaining blocker B-9 is a one-sentence clarification in chessboard §6.3; B-10 is a decision on T2+ budget.

---

## 1. New blockers surfaced in this audit (fix before T1)

### B-9. Chessboard §6.3 "13 outgoing edges" from QG5D conflicts with brief §2.1 predecessor-ownership rule

**Where it conflicts:**

- `13-chessboard-layer.md` §6.3 "Hub radiation" (line 343): *"This fills up to **13 outgoing edges in parallel** at QG5D's edge phase, instead of just 1 (the ring-next edge to RH)."*
- `13-chessboard-layer.md` §6.3 (line 339): *"Read `paper1/PROOF-CHAIN.md §"Foundation exports"` — the 13-row table."* (The 13 rows enumerate all 13 downstream vertices: RH, YM, BSD, PvNP, Hodge, NS, H12, GRH, Baum-Connes, BGS, Goldbach, Twin Primes, Schanuel.)
- Brief §2.1 "Edge ownership (disambiguation)" (lines 124-145): *"Ring edges (14 total) are owned by exactly ONE vertex — the **predecessor** (the vertex you're leaving). That vertex fills the ring edge during its EDGE PHASE … The successor vertex does NOT re-fill the edge — it inherits the filled edge as its 'incoming context'."* Schanuel (position 14, last in the ring) OWNS the ring-closing edge Schanuel → QG5D.
- `paper1/PROOF-CHAIN.md` §"Programme graph edges (outgoing from QG5D)" (line 377-379): *"The ring-PCA fills one outgoing edge per traversal (position 1 → position 2 = QG5D → RH). **The other 12 edges from QG5D are filled incidentally** as the capacitor grows."* Paper 1 itself says 12, not 13.

**The arithmetic:**

QG5D is at position 1. It has 13 OTHER vertices (positions 2-14). Among those 13:
- Position 2 (RH): ring-NEXT edge, owned by QG5D per §2.1.
- Position 14 (Schanuel): ring-PREV edge, owned by Schanuel per §2.1.
- Positions 3-13 (11 vertices): chord edges, no single owner; filled via hub radiation / antipodal probe / composition (per brief §2.1's no-single-owner chord rule).

So QG5D's hub radiation can SANELY fill:
- 1 ring-next edge (QG5D → RH) — owned by QG5D ✓
- 11 chord edges (QG5D ↔ {GRH, BSD, H12, YM, NS, Hodge, BC, PvNP, BGS, Twin Primes, Goldbach}) — unowned ✓
- **Total: 12 edges, matching paper1's own self-description.**

Chessboard §6.3's "13 outgoing edges" includes the Schanuel ↔ QG5D cell. That cell is Schanuel's-to-fill per brief §2.1. Either:

- **(i) Chessboard §6.3 is off-by-one** — the 13th row of Foundation exports is Schanuel, but that specific row corresponds to an edge QG5D does NOT own. Hub radiation should fill 12, not 13. Paper 1's own §"Programme graph edges" agrees ("the other 12").

- **(ii) Hub radiation "fills early" on T1** — QG5D pre-fills the Schanuel → QG5D cell on T1's position-1 visit, and when Schanuel reaches position 14 it finds the cell FILLED and executes §3.3 step 5 ("verify it's still current; append a 'traversal-T confirmation note' rather than re-filling"). Under this reading, hub radiation legitimately touches 13 cells. But the race is never stated — §2.1 claims Schanuel OWNS the edge, §6.3 claims hub radiation fills it first, and the T1 boundary condition paragraph in §2.1 addresses the read-side of the inheritance but not the write-side.

- **(iii) Dual-ownership is intended** — hub radiation is a DIFFERENT protocol than ring edge-phase, and the Schanuel ↔ QG5D cell can be filled TWICE (once by QG5D hub radiation on T1, then confirmed by Schanuel at T1 position 14; on T2+, Schanuel's §3.3 step 5 "verify current / confirmation note" applies because the cell is already FILLED). Under this reading, §6.3 is correct at 13 edges. But the brief should DECLARE this dual-path as intentional rather than leaving it ambiguous.

**Why it matters:**

- Hub radiation dispatches 13 Cell-Fill Authors (Sonnet max) in parallel per chessboard §6.3. If the 13th Author is redundant with Schanuel's position-14 action, that's an off-by-one wasted dispatch per traversal (minor cost). If the 13th Author races Schanuel and they produce different cell content, that's a merge conflict at T1's position-14 edge phase (higher cost).
- Runner-level behavior is undefined: on T1, when Schanuel reaches position 14, does it (a) skip the edge fill because QG5D already filled it, (b) upgrade QG5D's content with Schanuel-specific transposition recipe, or (c) overwrite with its own content? The §3.3 protocol step 5 ("FILLED: verify it's still current … append a 'traversal-T confirmation note' rather than re-filling") reads as (a)+(b). But the chessboard §6.3 protocol doesn't cross-reference §3.3, and the brief's §2.1 doesn't name hub radiation as a path that touches QG5D ↔ Schanuel.
- A silent off-by-one (interpretation (i)) is the simplest repair. A declared dual-path (interpretation (iii)) is more complete but adds coordination cost.

**Recommended fix:** one of

- **(a) Change chessboard §6.3 line 343 from "13 outgoing edges" to "12 outgoing edges (1 ring-next + 11 chords)."** Keep §6.3's Foundation-exports read (all 13 rows read for context), but only DISPATCH fills on the 12 QG5D-outgoing cells. The Schanuel → QG5D cell remains Schanuel's at position 14. This matches paper1's own count and preserves brief §2.1's predecessor-ownership rule. Simplest. One line in chessboard §6.3.

- **(b) Add an explicit dual-path declaration.** Brief §2.1 gets a new sub-paragraph: "Hub radiation (§6.3 chessboard) fills the 1 QG5D-outgoing ring edge + 11 chord edges + the ring-incoming edge Schanuel → QG5D AS AN EARLY-FILL on T1. On T1 position 14, Schanuel's edge phase sees the cell FILLED and executes §3.3 step 5 (verify + confirmation note). On T2+, Schanuel's standard edge-phase fill is the authoritative write; hub radiation verifies." Fuller but adds coordination burden. Add ~5 lines in brief §2.1.

- **(c) Keep §6.3 as-is and add a cross-reference**: leave "13 outgoing edges" in §6.3 but append a parenthetical: "(the 13th edge, QG5D ↔ Schanuel, races with Schanuel's position-14 edge phase — see brief §2.1 dual-path resolution above)." Requires adding the dual-path content per (b) in brief §2.1. Two-location edit.

**Recommendation: (a) — one-line change in chessboard §6.3 plus a one-line note in paper1's §"PCA traversal behavior at QG5D" clarifying that hub radiation fills 12 (not 13) edges.** Matches paper1's self-description, preserves brief §2.1's invariant, no coordination burden. Dual-path (b) is over-engineering for a cell that's already flagged SPECULATIVE (per brief §2 table) and gets filled once per ring close regardless of ownership.

---

### B-10. T2+ budget unfunded if VERIFY spot-checks are restored

**Where it conflicts:**

- `30-ring-traversal-brief.md` §4 lines 247-256: T1 budget widened to **10 h** with the following trims:
  - LOW antipodal probes SKIPPED on T1 (saves 20 min)
  - VERIFY spot-checks SKIPPED ENTIRELY on T1 (saves 140 min) — rationale: "the 14 PROOF-CHAIN.md files were just refreshed for the W1/W2 cascade (2026-04-14) and are authoritative at T1 start"
  - Skip sector-A on confidence ≥ 9/10 (saves 30 min)
  - Total trim: 190 min → 780 - 190 = **590 min ≈ 9.8 h** ✓ under 10 h ceiling
  - **Restore policy (brief §4 line 255): "VERIFY spot-checks on T2+ (at baseline, the refresh is stale). LOW antipodal probes on T2+ if HIGH/MEDIUM closed or fully probed."**

- `30-ring-traversal-brief.md` §4 lines 257-258: T2+ budget: **8 h**.

**The arithmetic:**

T2+ budget starts at 8 h = 480 min. Restoring T1-skipped work on T2+:
- VERIFY spot-checks: +140 min (per audit 33 A-7 budget estimate: 10 min × 14 vertices = 140 min)
- LOW antipodal probes (if HIGH/MEDIUM fully closed): +20 min (2 pairs × 10 min)
- Sector-A skip still applies (confidence ≥ 9/10 vertices don't need sector-A spot-check): saves 30 min
- Net adjustment: +140 + 20 - 30 = **+130 min**
- T2+ realistic: 480 + 130 (restorations vs T1) - 490 (core) - 70 (antipodal T1-only minus re-probe cost) - 70 (compositional cell-fill, T1-only savings) = ?

Actually the brief §4 line 258 claims T2+ is trimmed BY the T1-only items (antipodal probes done once, hub radiation done, sector classification cached). Let's recompute T2 from scratch:

- Core vertex+edge work: 14 × ~35 min = 490 min (same as T1)
- Chessboard overhead T2+ (per §Summary lines 539): "~30-40 min per subsequent cycle" — so ~35 min for chessboard
- VERIFY spot-checks (restored per §4 line 255): +140 min
- LOW antipodal re-probes (conditional on HIGH/MEDIUM closed): +20 min (optional)
- **T2 total: 490 + 35 + 140 + 0 = 665 min ≈ 11.1 h** — over the 8 h ceiling by 3.1 h.

Even without the LOW re-probes, T2+ budget overflows unless VERIFY spot-checks are ALSO skipped on T2+.

**Why it matters:**

- Budget is a hard exit criterion. T2+ overflows predict premature RING-STRENGTHENED classification (runner exits mid-traversal with unvisited vertices, biasing the outcome) or repeated budget-widening via trims.
- The brief's T2+ restoration policy contradicts its 8 h ceiling: 
  - line 255 says "VERIFY spot-checks on T2+" (restore)
  - line 257-258 says "Traversals 2+: 8 hours maximum"
  - these two statements can't both be true under the accounting in line 253.
- The W1/W2 cascade refresh argument that justifies T1 VERIFY-skip does NOT justify T2+ skip: by T2, PROOF-CHAIN.md files may have been EDITED IN PLACE by T1 Authors (§8.1's canonical-state discipline). T2's incoming state is not the refreshed 2026-04-14 baseline; it's the post-T1 state. The staleness argument for T2 is valid.

**Options:**

- **(a) Relax T2+ to 10 h** (mirror T1). Brief §4 updates the T2+ ceiling. Pro: consistent with the actual work T2+ does. Con: makes ring convergence slower (5 traversals × 10 h = 50 h total, vs 10 + 4 × 8 = 42 h under current prescription).

- **(b) Make VERIFY spot-checks lazy / sampled on T2+**: instead of 14 × 10 min = 140 min, sample 5 vertices per traversal on a rotating schedule (5 × 10 = 50 min). Over 3 traversals, each vertex gets verified at least once. Saves 90 min per traversal. T2+ at 490 + 35 + 50 + 0 = **575 min ≈ 9.6 h** — still over 8 h but closer.

- **(c) Keep T2+ at 8 h + declare VERIFY a per-traversal QUOTA of 5 vertices** (not 14). Brief §4 restoration line 255 becomes: "T2+ VERIFY spot-checks cover 5 vertices per traversal, rotating by position; every vertex gets at least one spot-check per 3 traversals." T2+ budget: 490 + 35 + 50 + 0 = 575 min. Still over 8 h by ~95 min.

- **(d) Drop core vertex+edge work estimate from 35 min avg to 28 min avg**: brief §4 line 245 already admits "some vertices are CLOSED (skip in ~5 min), some are hard (spend ~60 min). The budget is per-traversal, not per-vertex — the runner balances across vertices." If the AVERAGE is 28 min (instead of 35), 14 × 28 = 392 min core + 35 overhead + 50 VERIFY-quota = **477 min ≈ 7.95 h** ✓ fits 8 h. Pro: makes the arithmetic work. Con: relies on the runner's ability to skim-mode hard vertices that DON'T close under budget.

- **(e) Accept the overrun and rename the ceiling to a "soft target"**: brief §4 reclassifies both T1 and T2+ budgets as SOFT targets; the hard exit condition stays the exit-condition count (5 improvements etc.) rather than clock. Pro: honest-first. Con: removes the self-imposed clock discipline.

**Recommendation: (c) + (d) combined.** Brief §4 declares:
1. T2+ VERIFY spot-checks: 5 vertices per traversal, rotating schedule — not all 14.
2. T2+ core work: target 28-min average (not 35), with the explicit recognition that this requires runner skim-mode on CLOSED-AND-VERIFIED vertices (≤15 min) to balance against hard-wall vertices (60+ min).
3. T2+ budget stays at 8 h; arithmetic: 392 + 35 + 50 = **477 min ≈ 7.95 h** ✓.

Document both clarifications in brief §4 alongside the existing T1 trim list. Single edit, ~6 lines added.

---

## 2. Important ambiguities / gaps (decide before T1 or document explicitly)

### A-11. Per-vertex blackboard file-naming convention is unspecified

**Where:**

- `30-ring-traversal-brief.md` §8.1 line 359: *"Per-vertex blackboards at `${output-directory}/vertices/<vertex-name>.md` — the runner creates these for each vertex visit, capturing the blackboard §A-§O state DURING the visit."*

The placeholder `<vertex-name>` is undefined.

**The question:** when the T1 runner creates the first blackboard for QG5D, what filename does it use?

Candidate conventions (all plausible from context):

- `QG5D.md` — the ring vertex short name (used in §2, §6.3, brief prose)
- `paper1.md` — the paper directory name (used in the ring table §2, in §2.1)
- `01-QG5D.md` — position-prefixed + short name (matches ring order)
- `qg5d-paper1.md` — short name + directory name composite
- `p01-qg5d.md` — lowercase-prefixed variant

**Why it matters:**

- The runner's bootstrap §0 protocol (brief §0 plus ORA v8 §0) is deterministic. If the naming convention is ambiguous, two different runs (or a resume) may produce conflicting filenames for the same vertex, breaking `vertices/` subdirectory consistency.
- §8.2 resume semantics depend on the runner recognizing prior-traversal state in `vertices/`. An inconsistent naming convention can cause a resume to miss prior work and treat the vertex as unvisited.
- Referencing across traversals: T2's §K entries cite T1's `vertices/<vertex-name>.md` to trace prior-visit actions. If T2 uses a different convention than T1, cross-references break.
- Referencing from Authors: a T1 Cell-Fill Author returning from the edge phase may cite "see vertices/QG5D.md §D" in its output. If the actual file is `paper1.md`, the Author's citation is stale.

**Recommendation:** declare the convention in brief §8.1. Option: `<vertex-name> := <short-name>.md` where short-name is the 1-2 word camel/compact name used in §2 (QG5D, RH, GRH, BSD, H12, YM, NS, Hodge, BaumConnes, PvNP, BGS, TwinPrimes, Goldbach, Schanuel). Lowercase variant: `qg5d.md`, `rh.md`, `grh.md`, `bsd.md`, `h12.md`, `ym.md`, `ns.md`, `hodge.md`, `baum-connes.md`, `pvnp.md`, `bgs.md`, `twin-primes.md`, `goldbach.md`, `schanuel.md`. The lowercase hyphenated form is the canonical filesystem convention for the repo (`paper08-yang-mills`, `paper13-rh`, etc.) and avoids case-sensitivity pitfalls.

One-line patch in brief §8.1: change `${output-directory}/vertices/<vertex-name>.md` to `${output-directory}/vertices/<short-name>.md` with short-names defined in the §2 table.

---

## 3. Minor / cosmetic

### M-11. Chessboard §5 WIRE-DENSITY matrix is labeled "2026-04-13, estimated" and inconsistent with §6.6 T1-bootstrap computation

**Where:**

- `13-chessboard-layer.md` §5 line 236: *"Current density map (2026-04-13, estimated)"* followed by a 14×14 integer matrix (line 239-253).
- `13-chessboard-layer.md` §6.6 lines 413-429 (post-audit-33 fix): the RING-FILL-RATE and CHORD-FILL-RATE are "to be computed at T1 bootstrap" per explicit pseudo-code.

**The inconsistency:**

- §5's matrix is PRE-COMPUTED (dated 2026-04-13) and labeled "estimated" — it's used at every cycle-close (per §5 "How the ring-PCA uses it" protocol step 1: "At the start of each traversal, compute WIRE-DENSITY for all 91 edges (14 choose 2)").
- §6.6's RING/CHORD fill rates are deferred to T1 bootstrap, with explicit pseudo-code.
- These are the same quantity (wire count per vertex-pair) aggregated two ways: §5 is per-pair, §6.6 is by ring vs chord category.

If §5's "estimated" matrix is used at T1 cycle-close, it may contradict the T1-computed rates from §6.6 (which are computed from the CURRENT capacitor state). The result: two differently-computed densities in the same cycle.

**Recommendation:** change §5 label from "Current density map (2026-04-13, estimated)" to "**Current density map (estimated pre-T1; the runner recomputes from capacitor at T1 bootstrap per §5 protocol step 1)**". Aligns §5 with §6.6's "compute at T1 bootstrap" discipline. One-line label change.

---

### M-12. Brief §5 "from current 16.3%" contradicts the 16.0% baseline in 5 other sites

**Where:**

- `30-ring-traversal-brief.md` §5 line 292: *"After 3 traversals: capacitor target fill rate 20%+ (from current 16.3%)"*
- Capacitor §"Statistics update" line 276: *"Fill rate (Tier 1 + Tier 2 / 276) | 14.5% | ~16.0% | +1.5 pp"*
- `publishing/strategy.md` Appendix B §B.2 line 603: *"Baseline (2026-04-13) | 44 / 276 = 16.0%"*
- `programme/ring-traversal-log.md` line 17: *"Capacitor cells filled | 44 / 276 (16.0%)"*
- Chessboard §3 (current-value block, line 142): *"E_filled = 44 (post-H4-run capacitor) / E_total = 276"* — 44/276 = 15.94% rounding to 16.0%.

**The arithmetic:**

- 44 / 276 = 0.15942... which rounds to 16.0% or 15.9% (either is defensible).
- 45 / 276 = 0.16304... which rounds to 16.3%.
- 44 / 270 = 0.16296... which rounds to 16.3% (a possible alternative denominator if diagonal cells were counted — but 270 isn't used anywhere else).

So the brief §5 "16.3%" is either a typo (off-by-0.3 percentage-points) or implies a different numerator/denominator that isn't used anywhere else in the stack.

**Why it matters:**

- Low-severity: the target is "20%+" so a 16.0 vs 16.3 baseline affects the gap to target by 0.3 pp out of 4 pp. Not decisive.
- High-audit-smell: five sites consistent at 16.0%; one site at 16.3%. The drift is surface-level but the kind of inconsistency that compounds in later audits.

**Recommendation:** fix brief §5 line 292 to `16.0%`. One find-replace edit.

---

### M-13. `paper1/PROOF-CHAIN.md` structure is a TREE (22 theorems + 13 downstream chains), not a linear chain — brief §3 "the chain" language mildly misfits

**Where:**

- `paper1/PROOF-CHAIN.md` line 3: *"The programme's root. Four postulates on M⁴ × S¹ generate 22 theorems plus the CBB system plus 36 sub-percent predictions plus 13 downstream proof chains. **Not a linear chain — a tree whose root is axiomatic and whose leaves touch every Millennium problem.**"*
- Brief §3 "What happens at each vertex (the vertex protocol)" (lines 182-241): the protocol is explicitly CHAIN-centric ("identify the weakest link," "target the NEXT weakest link," "construct via capacitor").
- Paper 1's own §"PCA traversal behavior at QG5D (the hub special case)" (lines 389-404) modifies the vertex protocol for QG5D: *"The ring-PCA's vertex protocol is MODIFIED at QG5D because there are no 'weak links' — the 22 theorems are all PROVED. … At QG5D, the PCA does: 1. READ phase (~5 min): verify all 22 theorems are still valid. Check Branch E's 36 pins. … 2. ACT phase (~20 min): PIN VALIDATION instead of EXCISE/CONSTRUCT."*

**The semantic gap:**

- Brief §3 describes the vertex protocol in link-centric terms. Paper 1's PROOF-CHAIN.md describes QG5D's visit in pin-centric terms (PIN VALIDATION, not link excision).
- An Author dispatched to "target the weakest link at QG5D" would be confused — QG5D has no weak links; it has 22 proved theorems and 36 experimental pins.
- The existing §3.2 "If all links are VERIFIED/PROVED" branch (line 210) partially covers this: T1 runs "a lightweight re-verification pass" via a Sonnet Critic on 2-3 highest-confidence PROVED links. BUT T1 SKIPS VERIFY spot-checks entirely per §4 line 252. So QG5D's T1 visit has NO spot-check AND NO link excision — it falls through to the edge phase.
- Paper 1's §"PCA traversal behavior at QG5D" is the correct behavior — PIN VALIDATION + hub radiation — but the brief §3 protocol doesn't cross-reference it.

**Why it matters:**

- The runner reading brief §3 in isolation may not know to consult paper1/PROOF-CHAIN.md §"PCA traversal behavior at QG5D" for the special-case protocol.
- An Author spawned with "execute the vertex protocol at QG5D" context has the wrong mental model unless the spawn context includes paper1's §"PCA traversal behavior at QG5D" verbatim.
- The chessboard §6.3 hub-radiation protocol is ADDITIONAL to (not a replacement for) the standard §3 vertex protocol. All three (brief §3, chessboard §6.3, paper1's special case) must compose coherently at position 1.

**Recommendation:** add one cross-reference paragraph to brief §3 (before §3.1 "Read phase"):

> **Hub-special-case protocol**: position 1 (QG5D) has a MODIFIED vertex protocol per `paper1/PROOF-CHAIN.md §"PCA traversal behavior at QG5D"` — PIN VALIDATION instead of EXCISE/CONSTRUCT, and hub radiation (chessboard §6.3) in the edge phase. The generic §3.1-§3.4 protocol applies to vertices 2-14; QG5D's visit uses paper1's special-case procedure. The runner reads paper1's §"PCA traversal behavior at QG5D" at QG5D's read phase as context.

One-paragraph cross-reference in brief §3. No structural change.

---

## 4. Verification of prior-audit fix status (composing with audits 31/32/33)

| Audit | Item | Severity (at time of audit) | Fix status as of this audit | Evidence |
|---|---|---|---|---|
| 31 | B-1 EXCISE semantics | blocker | ✅ FIXED | Brief §0.1 three-step ladder present; chessboard §6.2 Type B consistent. |
| 31 | B-2 T1 budget overflow | blocker | ✅ PARTIAL FIX | Brief §4 T1 widened to 10 h with 190-min trims → 9.8 h. **T2+ budget not re-verified — see B-10 this audit.** |
| 31 | B-3 status vocabulary | blocker | ✅ FIXED | Brief §0.2 three cross-layer mapping tables present. |
| 31 | A-1 missing VERIFY | blocker-adjacent | ✅ FIXED | Brief §3.2 T1 skip + T2+ spot-check-or-trigger policy declared. |
| 31 | A-2 Triad wave semantics | important | ✅ FIXED | Brief §8.3 per-traversal firing. |
| 31 | A-3 approval gate | important | ✅ FIXED | Brief §0.4 + §8.3 continuous-run + non-blocking. |
| 31 | A-4 north-star mismatch | important | ✅ FIXED | `publishing/strategy.md` Appendix B §B.1-B.7 present. |
| 31 | A-5 closure ritual on exits | important | ✅ FIXED | Brief §8.4 ABBREVIATED / FULL / MEDIUM rituals declared per exit condition. |
| 31 | M-1 "13 vertices" typo | minor | ✅ FIXED | Chessboard §3 now 14. |
| 31 | M-2 paper27 duplicates | minor | ✅ DOCUMENTED (not deleted) | Brief §0.3 paragraph present; directories remain on disk but have no top-level PROOF-CHAIN.md. |
| 31 | M-3 hardcoded traversal-01 | minor | ✅ DOCUMENTED | Brief §8.2 NN-swap + resume semantics. |
| 31 | M-4 edge-ownership vs hub | minor | ✅ FIXED | Brief §2.1 disambiguation paragraph; **BUT see B-9 this audit — the 13-edge count in §6.3 still conflicts.** |
| 32 | B-4 companion files | blocker | ✅ FIXED | `30-ring-traversal-run.md` includes qualifier sentence + archival note. |
| 32 | B-5 self-name drift | minor-moderate | ✅ DOCUMENTED / ACCEPTED | Run.md's archival-snapshot note makes the `06-the-prompt.md` self-reference harmless. `08-framework-tools.md` line 555 self-refers CORRECTLY to `08-framework-tools.md` now. |
| 33 | B-6 brief §8 invocation stale | blocker | ✅ FIXED | Brief §8 now a pointer to run.md ("The canonical invocation is `30-ring-traversal-run.md`"). |
| 33 | B-7 RIGIDITY baseline convention | blocker | ✅ FIXED | Chessboard §3 declares convention, 10.63 computed, per-vertex enumeration provided. |
| 33 | B-8 post-W1/W2 cascade propagation | blocker | ✅ FIXED | Chessboard §3 refreshed, Appendix C SECTOR-TABLE refreshed (QG5D 10/10, YM 9.5/10, NS 4/10), log baseline refreshed, Appendix B §B.3 refreshed. All three sites consistent. |
| 33 | A-6 ring-closing edge T1 bootstrap | important | ✅ FIXED | Brief §2.1 "Ring-closure boundary condition (T1)" paragraph declares option (a)+(c) hybrid. |
| 33 | A-7 T1 budget overflow | important | ✅ PARTIAL FIX | T1 trimmed to 9.8 h via the three declared trims. **T2+ restoration not costed — see B-10 this audit.** |
| 33 | A-8 chord-fill-rate conflation | important | ✅ FIXED | Chessboard §6.6 T1-compute declaration + pseudo-code. |
| 33 | A-9 ring-edge vs programme-graph-edge semantics | important | ✅ FIXED | Brief §2.1 "Ring edges are TRANSPOSITION CHALLENGES" paragraph. |
| 33 | A-10 toolkit file identity | moderate | ✅ FIXED | `08-framework-tools.md` new line 3 "RING-MODE EXCEPTION" paragraph. |
| 33 | M-5 PCA/Triad invocation placeholders | minor | ❌ UNFIXED | `07-proof-chain-adversarial.md` §P.11 and `12-prf-chain-advr-strat-triad.md` §T.10 still use `<path>/pca/...` placeholders. |
| 33 | M-6 capacitor top-of-file stats | minor | ❌ UNFIXED | Capacitor lines 223-235 still show 40 / 14.5% pre-H4 numbers. Lines 267-277 show 44 / 16.0% post-H4. Two-state file. |
| 33 | M-7 log baseline pre-cascade | minor | ✅ FIXED | Log baseline is post-W1/W2. |
| 33 | M-8 SECTOR-TABLE staleness | minor | ✅ FIXED | SECTOR-TABLE rows 1 (QG5D 10/10), 6 (YM 9.5/10), 7 (NS 4/10) refreshed. |
| 33 | M-9 traversal-01 dir not yet created | info | ✅ CLEAN | Parent dir exists and empty. Runner creates child at bootstrap. |
| 33 | M-10 paper27 no top-level PROOF-CHAIN.md | info | ✅ CLEAN | Glob returns exactly 14 canonical entries. |

**Summary of prior-audit status:**
- 31: 12/12 items addressed (11 fixed, 1 documented).
- 32: 2/2 items addressed (1 fixed, 1 accepted).
- 33: 9/11 items fixed, 2 unfixed (M-5, M-6) — all three B-items fixed; all five A-items fixed; M-5 and M-6 still open as cumulative cleanup.

---

## 5. Summary table — severity × recommended order (this audit only)

| # | Severity | Fix size | Location of fix | Priority |
|---|---|---|---|---|
| **B-9** hub-radiation 13 vs 12 edges | **blocker** | 1 line in chessboard §6.3 + 1 line in paper1 special case | `13-chessboard-layer.md` §6.3 + `paper1/PROOF-CHAIN.md` §"PCA traversal behavior at QG5D" | **do before T1 bootstrap** |
| **B-10** T2+ budget under-funded | **blocker** | ~6 lines in brief §4 declaring T2+ VERIFY quota + core-work average | `30-ring-traversal-brief.md` §4 | decide before T2 (can defer past T1) |
| **A-11** vertex-name naming convention | important | 1 line in brief §8.1 + supplementary short-name list in §2 or §8.1 | `30-ring-traversal-brief.md` §8.1 | **do before T1 bootstrap** (otherwise the runner invents its own convention silently) |
| M-11 WIRE-DENSITY matrix label | minor | 1-word label change | `13-chessboard-layer.md` §5 | optional; do anytime before cycle 2 |
| M-12 brief §5 16.3% → 16.0% | minor | 1 find-replace | `30-ring-traversal-brief.md` §5 | optional; cosmetic |
| M-13 paper1 tree-vs-chain cross-ref | minor | 1 paragraph in brief §3 | `30-ring-traversal-brief.md` §3 | optional; the runner may figure it out, but load-bearing for QG5D's T1 visit context |
| M-5 (carry-forward) PCA/Triad placeholders | minor | find-replace in 2 files | `07-…md` §P.11 + `12-…md` §T.10 | optional cumulative cleanup |
| M-6 (carry-forward) capacitor top-stats | minor | cross-ref pointer OR update in-place | `09-capacitor-…md` §"Table statistics (v1)" | optional cumulative cleanup |

**Suggested resolution order:**

1. **Fix B-9** (~5 min): one-line edit in chessboard §6.3 changing "13 outgoing edges" → "12 outgoing edges (1 ring-next + 11 chords)," plus a one-line cross-note in paper1's PCA-traversal-behavior section clarifying the 12-count matches the brief §2.1 invariant.
2. **Fix A-11** (~5 min): declare vertex-name convention in brief §8.1 (suggested: lowercase hyphenated: `qg5d.md`, `rh.md`, `grh.md`, `bsd.md`, `h12.md`, `ym.md`, `ns.md`, `hodge.md`, `baum-connes.md`, `pvnp.md`, `bgs.md`, `twin-primes.md`, `goldbach.md`, `schanuel.md`).
3. **Decide B-10** (~10 min): pick option (c)+(d) or explicitly widen T2+ to 10 h. Document in brief §4 alongside T1 trim list.
4. **Fix M-13** (~5 min): one paragraph in brief §3 cross-referencing paper1's §"PCA traversal behavior at QG5D" special case.
5. **Fix M-11, M-12** (~5 min total): label change in chessboard §5, find-replace in brief §5.
6. Start T1.
7. Clean up M-5, M-6 (carry-forward from audit 33) at leisure between traversals.

Total patch budget: ~30 min (same as audit 33's conclusion — the ring is now at ~97% ready).

---

## 6. Positive findings (new + carried-forward)

**New positive findings in this audit:**

- **All three blockers from audit 33 (B-6, B-7, B-8) are FIXED.** The brief §8 is a pointer, chessboard §3 has the declared convention + 10.63, and the cascade is propagated across chessboard §3, Appendix C SECTOR-TABLE, Appendix B §B.3, and the log baseline.
- **All five important items from audit 33 (A-6 through A-10) are FIXED or adequately mitigated.** Brief §2.1 has both the ring-closure boundary condition (T1) and the ring-edges-as-transposition-challenges paragraphs. Brief §3.2 declares the T1 VERIFY-skip with rationale. Chessboard §6.6 defers fill-rate to T1 bootstrap with pseudo-code. 08-framework-tools.md has the RING-MODE EXCEPTION header.
- **Internal consistency within `publishing/strategy.md` Appendix B is preserved** across §B.2 (fill-rate baseline 16.0%) and §B.3 (RIGIDITY baseline 10.63). No drift between north-star sections.
- **The canonical ring order is consistent** across all six sites that cite it: run.md (lines 42-56), brief §2 table, chessboard Appendix C SECTOR-TABLE, chessboard §6.4 antipodal pairs, paper1 §"Foundation exports" table, and the `programme/ring-traversal-log.md` baseline.
- **The 14 PROOF-CHAIN.md glob is clean**: `Glob paper*/PROOF-CHAIN.md` returns exactly 14 canonical entries. No `paper27-*/` noise at the top level.
- **The ORA v8 companion files all exist** at `online-researcher-adversarial/ora-bundle-v8/`: `02-rationale.md`, `03-synthesis-spawn.md`, `04-closure-templates.md`, `06-anti-overfit-discipline.md`, `08-changelog.md`. Audit 32's B-4 resolver is live.
- **The output directory parent** (`programme/ring-traversals/`) exists and is empty — T1 creates `traversal-01/` at bootstrap. Clean slate.
- **Paper 1's `Foundation exports` 13-row table exists** and the 13 rows are exactly the 13 downstream ring vertices in ring order — consistent with chessboard §6.3 hub-radiation's read of it (modulo the B-9 count issue).
- **Paper 1's §"PCA traversal behavior at QG5D"** explicitly describes the hub special-case protocol — it's on-disk, just not cross-referenced from brief §3.

**Carried-forward from prior audits:**

- Domain codes (D1-D24) in brief §2.2 match the capacitor's Domain index exactly (audit 31-33).
- Vertex-to-domain mapping uses only the capacitor's actual codes (audit 31-33).
- RIGIDITY formula matches brief §5 / chessboard §3 / Appendix B §B.3; numeric baseline 10.63 now reproducible per the declared convention (audit 33 verified the convention; this audit verifies the cross-site consistency).
- The 5-layer read order (ORA v8 → PCA → Triad → Chessboard → Brief) is consistent: each layer declares which prior layers it extends, and all extensions preserve prior-layer invariants.
- Brief §8.1 correctly overrides PCA §P.2 (chain-state.md mandate); §8.3 correctly overrides Triad §T.3 + §T.6; §8.4 correctly overrides ORA §13.3 + PCA §P.9.
- PIN-TABLE exists at `paper12/research/23-framework-predictions-master-table.md` (load-bearing for PIN-PRESERVATION / DUAL-CHECK per chessboard Appendix A).

---

## 7. Delta from audits 31, 32, 33

- **Audit 31** inspected: invocation + 8 stack files + 14 PROOF-CHAIN.md + PIN-TABLE + output dir. Surfaced 12 items. All addressed.
- **Audit 32** inspected: audit-31 scope + companion-file resolvability for `06-the-prompt.md`. Surfaced 2 items. Both addressed.
- **Audit 33** inspected: audit-32 scope + numeric cross-check of RIGIDITY + cascade propagation + brief §8 vs run.md consistency + toolkit identity + ring-closing edge T1 bootstrap + T1 budget arithmetic + chord-fill-rate computation + per-vertex programme-graph-edges semantics. Surfaced 11 items. Of which: 3 blockers (ALL FIXED in this audit), 5 important (ALL FIXED or mitigated), 2 minor (UNFIXED: M-5, M-6), 1 info (CLEAN: M-9, M-10).
- **This audit (34)** inspected: audit-33 scope + **verification of audit 33's fix-application at every site** + paper1 Foundation exports vs chessboard §6.3 hub-radiation arithmetic + T2+ budget re-cost under VERIFY restoration + per-vertex blackboard file-naming ambiguity + paper1 tree-vs-chain structural cross-ref gap + capacitor-fill-rate arithmetic inconsistency between brief §5 (16.3%) and 5 other sites (16.0%) + WIRE-DENSITY matrix staleness label. Surfaced **2 new blockers** (B-9 hub-radiation count, B-10 T2+ budget) + **1 new important ambiguity** (A-11 vertex-name convention) + **3 new minors** (M-11 WIRE-DENSITY label, M-12 16.3→16.0, M-13 tree-vs-chain cross-ref) + **2 carry-forwards** (M-5, M-6 from audit 33).

The stack is ~97% ready. B-9 and A-11 are load-bearing for T1 bootstrap (fix before T1). B-10 is deferred to T2 decision. Three minors are cosmetic cleanups. Two carry-forwards are cumulative audit sediment.

Total patch budget for T1 readiness: ~15 min (B-9 + A-11 only). Extended patch budget for full readiness: ~30 min.

---

## 8. One-paragraph runner bootstrap status (post-audit-34)

The ring-traversal PCA stack is 97% ready for T1 dispatch. Audit 33's three blockers (B-6 brief §8 stale, B-7 RIGIDITY baseline convention, B-8 cascade propagation) are ALL FIXED and verified at every cite-site. Audit 33's five important items (A-6 through A-10) are all FIXED or adequately mitigated. Of audit 33's four minor items, two are fixed (M-7, M-8) and two remain as cumulative cleanup (M-5 PCA/Triad invocation placeholders, M-6 capacitor top-of-file stats). This audit surfaces three new items relevant to T1 bootstrap: (B-9) chessboard §6.3 says "13 outgoing edges" from QG5D during hub radiation, but paper1's own §"Programme graph edges" says 12 and brief §2.1's predecessor-ownership rule constrains QG5D to 1 ring-next + 11 chords = 12 — one-line fix changes "13 outgoing edges" to "12 outgoing edges (1 ring-next + 11 chords)"; (A-11) brief §8.1 specifies per-vertex blackboards at `vertices/<vertex-name>.md` without defining the convention — suggested fix is to declare lowercase-hyphenated short names in §8.1; and (B-10) the brief §4 T2+ 8 h ceiling does not absorb the VERIFY spot-check restoration (140 min) that §4 itself mandates for T2+ — fix by declaring a 5-vertex rotating VERIFY quota on T2+ (not all 14) plus a 28-min core-work average. Three other minor items (M-11 WIRE-DENSITY matrix label, M-12 brief §5 16.3% vs 16.0% arithmetic, M-13 paper1-tree-vs-chain cross-ref) are cosmetic. Total patch budget for T1 readiness: ~15 min (B-9 + A-11). Once resolved, T1 dispatches.

---

*Audit complete. This file composes with `31-ring-traversal-run-gaps.md`, `32-ring-traversal-run-gaps.md`, and `33-ring-traversal-run-gaps.md`; none supersedes the others. Audit 31 addressed ring-mode conflicts in the stack layers (EXCISE semantics, budget, status vocabulary, VERIFY policy, Triad/approval/north-star, closure ritual, + 4 minors). Audit 32 addressed companion-file resolvability (B-4) and self-name drift (B-5). Audit 33 addressed baseline consistency across the post-W1/W2 cascade (B-7, B-8), invocation-template drift between brief §8 and run.md (B-6), ring-closing-edge T1 bootstrap (A-6), time-budget arithmetic under declared trims (A-7), chord-fill-rate computation (A-8), ring-edge semantics (A-9), toolkit file identity (A-10), + 4 minors. **This audit 34 addresses the orthogonal questions of: verification of audit-33 fix-application at every site, hub-radiation edge-count arithmetic against brief §2.1 invariants, T2+ budget re-cost under VERIFY-restoration policy, per-vertex blackboard file-naming convention, and capacitor-fill-rate cosmetic consistency across sites.** Awaiting user direction on which findings to address first.*

*v1: 2026-04-14. G Six and Claude Opus 4.6 (1M context).*
