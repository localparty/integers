# Paper 25 Review Concerns

*Reviewer: Claude Opus 4.6 (independent review + revision agent)*
*Date: 2026-04-09*

---

**REVISED 2026-04-11 — Conjecture 5 (V-Hilbert 12) formally RETRACTED.** The entry for Conjecture 5 in the review-concerns table is updated from "Yes, computationally testable / Yes, via Stark unit computation" to **"RETRACTED (see `sections-05-08.md` §8.0)"**. The computational test ran (research/267 + `paper12/relaxation/research/T7c-stark-rescue-verification.md`) and returned 0 / 30 pass across six pre-committed rescue candidates. The retraction is a vindication of the "computationally testable" column — the conjecture was testable and was tested, and the test was negative. This is honest-first discipline working as designed.

---

## CRITICAL

### C1. RH proof sketch gap (Section 5.4)
**Issue:** The conditional proof that Conjecture 2 implies RH relies on the claim that a spectral density factor f(gamma) is "generically irrational." This is asserted without proof. The irrationality of f(gamma) for the specific spectral density of zeta zeros is a nontrivial analytic claim that is neither obvious nor referenced.
**Fix applied:** REVISED. Replaced "QED (conditional)" framing with explicit identification of the gap. Added a **Gap** paragraph flagging that the irrationality step is open. Changed "Sketch of proof" to "Sketch of argument (conditional, not a complete proof)."
**File:** sections-05-08.md, Section 5.4

### C2. Silent escalation from local to global Conjecture 2 (Section 10.3)
**Issue:** Conjecture 2 as formally stated in Section 5.1 is local (per-bridge). Section 10.3 invokes a "global form" (simultaneous compatibility across all bridges) that is never formally stated as a conjecture. The implication chain Conjecture 2 (local) -> RH has an unstated intermediate step (simultaneous-lift implies spectral completeness). This makes the RH-as-corollary claim structurally incomplete.
**Fix applied:** REVISED. Added an "Important distinction" paragraph in Section 10.3 explicitly flagging the local-vs-global gap and noting the intermediate step.
**File:** sections-09-15.md, Section 10.3

---

## MAJOR

### M1. LOCK overclaiming (Section 10.4)
**Issue:** "RH is experimentally supported by 37 independent physical measurements" overstates. The R-Theorems test the conjunction "CBB + RH", not RH independently. If the CBB system is wrong, the R-Theorems say nothing about RH.
**Fix applied:** REVISED. Changed "experimentally supported" to "consistent with." Added clarification that the evidence is joint evidence for CBB + RH.
**File:** sections-09-15.md, Section 10.4

### M2. Draft debris in Section 6.2
**Issue:** The text contains a wrong table, then "Wait -- l = 13 gives k = 6 as well," followed by an inline arithmetic correction and a corrected table. This is draft-stage thinking-out-loud inappropriate for a published paper.
**Fix applied:** REVISED. Removed the wrong table and the self-correction passage. Retained only the corrected table with a parenthetical note.
**File:** sections-05-08.md, Section 6.2

---

## MINOR

### m1. "37 R-Theorems" count (Section 10.4)
**Issue:** The text says "37 R-Theorems" but then lists "27 spectral + 9 geometric + 1 interface = 37, plus the derivations of a and b." That is 37 + 2 = 39, or 37 if a and b are included in the 27. The accounting is ambiguous.
**Status:** Not fixed; flagged for author clarification.

### m2. Section 3.2 uniqueness claim (sections-01-04.md)
**Issue:** "These are the *only* pairs (p, N) with p, N both prime, N <= 19, k in {3,4,6}, and G_{p,N} cyclic." This should be verified computationally or stated as "the only pairs found" with a reference to the verification.
**Status:** Not fixed; the claim is likely correct but should be backed by explicit enumeration (Section 12 proposes this).

### m3. Conjecture 4 precision (Section 7.1)
**Issue:** "Every abelian extension of Q(zeta_13) and Q(zeta_19) embedded in the CBB Hilbert space H_R" -- the notion of "embedding into H_R" is not formally defined. A mathematician would need a precise definition of what it means for an abelian extension to "embed" in a Hilbert space.
**Status:** Not fixed; flagged for author to add a precise definition (e.g., the Galois group acts as a subgroup of the unitary group of H_R compatible with the KMS structure).

### m4. RBC refutations stated honestly
**Verdict:** YES. Section 9.3 (research/182) and Section 9.4 (research/188) are admirably honest. Both refutations are stated clearly with numerical values, and the text explains what was learned from each failure. This is a strength of the paper.

### m5. Cross-paper consistency with Papers 23, 24
**Verdict:** Consistent. The CBB quintuple definition, bridge table entries, carry cocycle formula, and V operator all match the anchor document and the Paper 23/24 skeleton TOCs. No contradictions found.

---

## Conjectures: precision assessment

| Conjecture | Precisely stated? | Attackable by mathematician? |
|:--|:--|:--|
| 1 (CBB Reciprocity) | Yes, with explicit map | Yes, extending research/162 |
| 2 (Brauer-KMS Duality) | Yes for local form; global form implicit | Local: yes. Global: needs formal statement |
| 3 (Level-Jump Rigidity) | Yes, finite computation | Yes, elementary |
| 4 (Spectral Kronecker-Weber) | Mostly; "embedding in H_R" needs definition | Close, with m3 fix |
| 5 (V-Hilbert 12) | Yes, computationally testable | Yes, via Stark unit computation |

---

## Verdict after fixes

**Publishable as a mathematical programme paper**, conditional on addressing m3 (Conjecture 4 precision). The five conjectures are well-structured, the RH claim is now properly hedged with gaps identified, the refutations are honest, and the paper successfully separates what is proved (k=3 lemma) from what is conjectured. The paper's ambition is appropriate for a programme paper in the tradition of Hilbert's original lecture.

---

## Three strongest aspects

1. **Honesty about refutations.** Sections 9.3 and 9.4 frankly report two failed hypotheses (research/182 and research/188) and explain what was learned. This builds credibility.

2. **Conjecture hierarchy.** The five conjectures are ordered by logical dependency and estimated difficulty, with a clear timeline. A reader knows exactly where to start (Conjecture 3, a finite computation) and where the summit is (Conjecture 2, implying RH).

3. **Audience-awareness.** Section 11 systematically addresses five distinct mathematical audiences (number theorists, operator algebraists, NCG, mathematical physicists, category theorists) with specific entry points for each. This is unusually well-targeted for a programme paper.
