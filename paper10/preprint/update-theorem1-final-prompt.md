# Prompt — Update Paper 10: Theorem 1 is Now Unconditional

**Issued by:** G (principal investigator)  
**Date:** 2026-04-07

Read these three memos before editing anything:
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/03-a2-graviphoton-radion-sector.md` (Lemma A2)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/04-a3-kk-loop-momentum-range.md` (Lemma A3)

All three assumptions A1, A2, A3 are now proved. Theorem 1 is unconditional within
linearized 5D gravity on flat M⁴ × S¹/Z₂.

## Changes required across four files

### `04-poisson-weyl.md`
- Change Theorem 1 label from "conditional on A2–A3" to **"Theorem 1 (proved)"**
- Add Lemma A2 (before Theorem 1): index structure argument + Z₂ selection rules
  forbid A_μ and φ from contributing to leading GS operator at dimension 6.
  *Proof:* see research memo 03.
- Add Lemma A3 (before Theorem 1): method-of-images propagator on S¹/Z₂ gives
  loop sum = 1 + 2·Σ_{n≥1} = Σ_{n∈ℤ} = S₀ = 0. Zero-mode n=0 contributes "1";
  image-doubled n≥1 modes contribute "2ζ_R(0) = −1". Exact cancellation.
  *Proof:* see research memo 04.
- Update the assumptions list: all three now marked "Proved (Lemma A1/A2/A3)"
- Update closing sentence: remove "binding open items are A2 and A3"
  → "All three assumptions are proved; Theorem 1 is unconditional."

### `05-open-problems.md`
- Status table: "Conditional on A2–A3" → **"Proved (Theorem 1)"**
- §5.2b: update A2 from open → proved; summarize Lemma A2 (two mechanisms)
- §5.2c: update A3 from open → proved; summarize Lemma A3 (method of images)
- Add new §5.3 — **"Weyl Anomaly of the Full KK Tower (Open Observation)"**:
  The A2 computation found a_grand = 19/240 ≠ 0 for the combined (h_{μν} + A_μ + φ)
  KK tower Weyl anomaly. This is orthogonal to Theorem 1 (it is a curved-background
  effect, not the flat-background GS divergence), but it is a real non-cancellation
  from Z₂-asymmetric mode counts. State: the Weyl anomaly of the full orbifold KK
  tower is 19/240 at one loop; this is not in conflict with Theorem 1 but is an
  independent open question deserving further study.

### `00-abstract.md`
- Remove all "conditional on A2–A3" language
- Theorem 1 is now stated unconditionally
- Update forward paragraph: Paper 10 establishes Theorem 1 (proved), Lemmas A1–A3
  (proved), and identifies the Weyl anomaly 19/240 as a separate open observation

### `01-introduction.md`
- §1.3 status summary: update vertex mass-independence to "Proved (Theorem 1,
  Lemmas A1–A3)"
- Closing paragraph of §1.3: remove all "conditional" and "remaining open"
  language for A2/A3; Theorem 1 is complete

Use the Edit tool throughout. Read each file before editing. Be precise and minimal.
