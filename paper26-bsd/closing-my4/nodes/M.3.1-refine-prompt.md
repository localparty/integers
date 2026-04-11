# Author spawn prompt — M.3.1-refine (slot W2-C)

**EFFORT: MAX.** You are an Author in the ORA, dispatched to refine the Cycle 1 M.3.1 Option C anchor draft. Cycle 1 produced a WEAKENED verdict with 6-8 mechanical fixes pending. Your task is to apply every fix, verify each against its primary source, and ship a clean M.3.1-v2 draft that is ready to incorporate into Paper 26's LaTeX preprint.

**Important context**: G has **already fixed** the upstream deliverable errors on the runner's flagging:
- `paper26-bsd/strategy/04-closing-my4.md` lines 694 and 921 — the referee misquotes are now GONE. Every time/effort/scope estimate in the deliverable has been removed (per G's directive "we don't need the estimates"). You cannot inherit the misquotes from the deliverable anymore because they don't exist there.
- `paper26-bsd/research/route2-ccm-over-K.md` — Phase IV sub-task 4.1 is corrected.

Your refinement applies to **the Cycle 1 Author output `nodes/M.3.1.md`**, which still has the misquotes in the draft text (the deliverable is fixed but the Cycle 1 draft predates the fix). You fix them in the new M.3.1-refine output.

This is an **editorial node** (`node-kind = editorial`, per I-5 v3 patch). Not math. Not transposition.

Slot: W2-C. Wave: 2. Effort: **MAX**.

---

## Framework tools to read (per I-8 patch, editorial-mode minimal set)

**Always include** (editorial nodes get the baseline):
- `/Users/gsix/quantum-geometry-in-5d-latex/paper12/research/214-the-method-six-patterns.md` (~339 lines) — the 6-step loop (adapted for editorial)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper12/27-anchor-document.md` (~426 lines) — operational anchor + voice register

**Editorial-mode conditional** (not a transposition, but voice calibration matters):
- `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/research/35-final-verdict.md` — per the new `04-closure-templates.md` Template 5 canonical example pointer. This is the YM closure-digest in §J register — match its rhythm for the §3.6.2 draft and §15.6 paragraph.

**Load-bearing input files for the refinement**:
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4/nodes/M.3.1.md` — the Cycle 1 draft you are refining. **READ THIS END-TO-END.** It contains the 7 artifacts you need to update.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4/critiques/M.3.1-cycle-1.md` — the Cycle 1 Critic's full critique with every fix identified. **READ THIS END-TO-END.** It contains the fix list (G17-G24) you need to apply.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/runs/r00/points/A3-meyer-spectral/verdict.md` — the **actual** referee A3 verdict. Read this before fixing any quote attribution. Per the Critic's discovery, the verdict says "Overall verdict: CLOSABLE GAP" + "Difficulty: 2-3 pages of explicit computation" — NOT "multiple months of focused work." Every "CLOSABLE GAP — substantial work required" quote in the Cycle 1 draft must be verified against this file.
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/04-closing-my4.md` — the **now-corrected** deliverable. G removed all the time/effort/scope estimates. Verify that your refinement does not re-introduce any (no "pages" estimates, no "months," no "few days").
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-I.md` — for §2.3 line 168 (the first silent-inference site Critic identified).
- `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/preprint/sections-part-III.md` (or wherever §9.1 Step 4 lives) — for the second silent-inference site at lines 518-521.

---

## Target — apply all fixes from the Cycle 1 Critic

The Cycle 1 Critic's fix list (from the status report, full details in `critiques/M.3.1-cycle-1.md`):

**G17 — 5 referee misquotes**. The Cycle 1 draft has "CLOSABLE GAP — substantial work required" / "multiple months of focused work" at M.3.1.md lines 189, 240, 394, 594–595, 671. Correct each to match the actual r00 verdict ("CLOSABLE GAP" + "Difficulty: 2-3 pages of explicit computation"). If a sentence needs to paraphrase rather than direct-quote, make the paraphrase accurate and drop the direct-quote attribution. **All 5 instances must be fixed.**

**G18 — MY4 vs A3 sub-point mismatch**. Cycle 1 draft frames MY4 as "the wall the referee flagged on A3." The referee's headline A3 concern was sub-point (c) — the character twist cocycle integrality — NOT sub-point (b) — the distributional construction verification. Rewrite §3.6.2 and §15.6 to **distinguish**:
- "*MY4 (distributional → genuine spectral upgrade for `T̄_{BC,K}`)*" — the Author's naming of the open gap.
- "*The referee's A3 headline concern (character twist cocycle integrality)*" — the referee's phrasing of a different aspect of the same area.

Do NOT conflate them. Be explicit that MY4 is the sub-decomposition *within* the A3-cluster that r01 (the later run) identified, while r00 (the authoritative A3 verdict) treated the distributional-to-genuine question as SOUND and flagged the character twist as the main gap. Refer to `strategy/04-closing-my4.md` for the now-clarified framing (G noted: "r00 marked sub-question (d) SOUND, r01 flagged it as MY4 [KEY LEMMA — OPEN]").

**G19 — Theorem 13.1 trailing parenthetical**. The Cycle 1 draft added a trailing rank-1 vacuity parenthetical inside the Theorem 13.1 block that is new text, not in the original. Drop the parenthetical (the rank-1 vacuity is already covered in Remark 12.6, which should be the sole anchor). Restore Theorem 13.1's conclusion to byte-for-byte identical with the current preprint except for the added conditional clause at the start of the hypothesis.

**G20 — Change-log incomplete: 2 missed silent-inference sites**. Add to the change-log's adjacent-edits list:
- `sections-part-I.md` line 168 — §2.3 RH proof summary has "Nelson's analytic vector theorem upgrades these to genuine eigenstates" which silently assumes MY4.
- `sections-part-III.md` lines 518–521 — §9.1 Step 4 has "Nelson self-adjointness promotes these to genuine eigenstates" which silently assumes MY4.
Both sites need the same citation update to §3.6.2 as §9.2 Step B(5) (which was already in the Cycle 1 change-log).

**G21 — Reed–Simon volume**. The Cycle 1 draft cites "Reed-Simon II §VIII.3" for the spectral theorem. The spectral theorem is in Reed-Simon **Vol. I** §VIII.3; Nelson's X.39 is in Vol. II. Fix "II" to "I" in the §3.6.2 citation.

**G22 — Unsourced "5-15 pages" Route 1 estimate**. G removed all estimates from the deliverable; the Cycle 1 draft's references to "5–15 pages" at §3.6.2 line 369 and §15.6 line 587 are now unsourced *and* inconsistent with the corrected deliverable. **Remove the page estimates entirely.** Do not replace with other numbers — the deliverable's new stance is "no estimates."

**G23 — §9.2 Step B sub-item numbers**. The Cycle 1 draft says the silent upgrade is "Step B(5)"; the Critic found it's actually in sub-items 4 AND 5 jointly (sub-item 4 silently assumes distributional eigenstates are genuine; sub-item 5 says "since self-adjoint, spectrum real"). Fix the sub-item numbering to cite "Step B(4-5)" or "Step B sub-items 4 and 5."

**G24 — Honest-framing audit procedural extension**. The Cycle 1 audit walked the draft against banned *weasel phrases* only. Add a second audit pass: **"quoted-attribution fidelity"** — for every direct quote in the draft that cites a source, verify the quoted text appears in the cited source. This is the procedural gap that let G17 slip through in Cycle 1. Write the extended audit as a new sub-section in Artifact 7 (Honest-framing audit). Apply it to the refined draft and list every quote you verified.

---

## Verification discipline (per I-7)

Every fix you apply must be verified against its primary source. Specifically:
- The referee verdict quotes: verify against the actual verdict file.
- The Reed-Simon citation: verify Vol. I §VIII.3 contains the spectral theorem (classical fact, but verify explicitly).
- The §2.3 and §9.1 silent-inference sites: verify the line numbers and the actual inference language.
- The §9.2 Step B sub-item numbering: verify sub-items 4 and 5 both contain the silent inference.

**If any verification step fails** (e.g., line numbers have shifted, the referee verdict text has been updated since Critic M.3.1 read it, the Reed-Simon volume is different): flag as CONCERN and use the actual verified content, not the Cycle 1 Critic's reading.

---

## Output

Write to: `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4/nodes/M.3.1-refine.md`

Produce the full refined 7-artifact draft:
- **Artifact 1**: New §3.6.2 of Paper 26 (refined — MY4/A3 distinction applied, misquotes removed, page estimates removed)
- **Artifact 2**: Updated Theorem 9.1 (unchanged from Cycle 1, verify byte-for-byte preservation)
- **Artifact 3**: Updated Theorem 13.1 (trailing parenthetical dropped per G19)
- **Artifact 4**: New §15.6 paragraph (refined — MY4/A3 distinction applied, page estimates removed)
- **Artifact 5**: Companion-notes pointer (unchanged from Cycle 1)
- **Artifact 6**: Change-log entry (extended with §2.3 and §9.1 Step 4 adjacent-edit sites)
- **Artifact 7**: Honest-framing audit (extended with the new quoted-attribution-fidelity sub-audit — list every direct quote you verified)

Plus the standard 6-step loop structure for editorial nodes, the Sig 11 "what the next runner needs to know" section, and a fix-list cross-reference table showing which G-number each fix resolved.

---

## Status report (return to runner, ≤300 words)

1. Status verdict (typically ADVANCED for editorial refinement)
2. How many of the 8 fixes (G17-G24) were applied (target: all 8)
3. Whether the quoted-attribution-fidelity audit found any additional misquotes beyond G17's 5
4. Whether the referee verdict file is byte-for-byte the same as the Cycle 1 Critic's reading (sanity check)
5. Whether any fix surfaced a new CONCERN (e.g., if line numbers have shifted since Cycle 1)
6. Length of the refined draft in pages
7. Whether the refined draft is ready to incorporate into Paper 26's LaTeX preprint (YES/NO + rationale)
8. p_success self-estimate

---

## Constraints

- **Effort: MAX**. Editorial does not mean low-effort — it means high-precision.
- **Verify every quote** against its primary source. The Cycle 1 misquotes were inherited from the deliverable's now-corrected prose; don't inherit them from the Cycle 1 draft either.
- **Do NOT use weasel words.** Same ban as Cycle 1 (no "we believe," no "it should follow," etc.).
- **Do NOT reintroduce time/effort/scope estimates.** G removed them from the deliverable deliberately.
- **Do NOT change mathematical content of any existing theorem.** Theorem 9.1 and 13.1 conclusions stay byte-for-byte identical; only the conditional clause at the start of the hypothesis changes.
- **Do NOT modify Paper 26 itself.** Write only to `nodes/M.3.1-refine.md`. The runner decides whether to apply artifacts to the LaTeX preprint in a later cycle.
- **Compute first, prove second** applies to editorial nodes too: before declaring ADVANCED, run your own quoted-attribution-fidelity audit (grep + primary-source check) and list the hits.
