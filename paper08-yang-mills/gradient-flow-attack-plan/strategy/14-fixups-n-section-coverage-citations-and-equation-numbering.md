# Fixup Strategy: N-Section Coverage, Citations, and Equation Numbering

*Three mechanical fixups identified by the Wave 10 audit. Total*
*effort: ~90 minutes, executable in parallel.*

*Date: 2026-04-08*

---

## 0. Context

The Wave 10 final audit found **9/10 PASS, 1 ISSUE, 0 content errors**.
The single ISSUE decomposes into 3 mechanical fixups, none of which
touches the mathematical content of the proof:

| # | Severity | What | Effort |
|:--|:---------|:-----|:-------|
| 1 | Medium | 21 raw "Paper X" citations missing Appendix N pointers | 30 min |
| 2 | Low | L.1 equation numbering inconsistent with L.2–L.4 | 15 min |
| 3 | High | L.0 / L.5 reference §§N.6–N.10 that don't exist | 15 or 45 min |

These are find-and-replace operations on 4 files. No new mathematics,
no new prose, no new citations to look up.


---


## 1. Fixup 3 First (Blocks the Other Two)

Fixup 3 is the highest priority because it determines whether
Appendix N grows from 6 sections to 11. That decision affects
Fixup 1 (the target sections for the citation pointers).

### 1.1 Decision: Option (a) or Option (b)?

**Option (a)** — Expand Appendix N with §§N.6–N.10 as a master
index pointing to L.1–L.4 for proofs.

- **Pros:** Cleaner cross-reference structure. Future readers can
  navigate from QG5D citations to gradient-flow lemmas via Appendix
  N alone. The §§N.6–N.10 act as "where this result is used in
  Appendix L."
- **Cons:** ~45 minutes of writing. Requires reading L.0 and L.5 to
  understand what §§N.6–N.10 should contain.

**Option (b)** — Update L.0 and L.5 to reference L sections directly
instead of non-existent N sections.

- **Pros:** 15 minutes. No new content. Minimal risk.
- **Cons:** Loses the symmetric "L cites N, N cites L" structure.
  L.0 and L.5 will mix N references (for QG5D inputs) with L
  references (for internal cross-links).

**Recommendation: Option (b).**

The reason: Appendix N's purpose is **inputs**, not **outputs**.
N.1–N.5 catalog QG5D theorems used as black-box inputs to Appendix L.
Adding §§N.6–N.10 as pointers from L.x lemmas back into the
gradient-flow programme would conflate the two directions and make
Appendix N harder to understand. The cleaner structure is:

- **Appendix N**: "Here are the QG5D theorems we cite. Here is where
  in Papers 1, 6, 10 they live."
- **Appendix L**: "Here are our 19 lemmas. They cite Appendix N for
  external inputs and other L lemmas for internal dependencies."

L.5 is the sub-clause resolution map — it should reference L lemmas
directly (e.g., "L.1(i) → Lemma L.3.8"), not route through Appendix N.
L.0 is the scope statement — same.

### 1.2 Execution

**Step 1.** Read `appendix-L/L0-L5-L6-L7.md` and find every reference
to "Appendix N, §N.6", "§N.7", ..., "§N.10".

**Step 2.** For each occurrence, identify the intended target:

- If the reference is to a QG5D input → change to the correct
  existing N section (§§N.1–N.5).
- If the reference is to a gradient-flow lemma → change to the
  L.x.y lemma reference.
- If the reference is to a sub-clause map entry → change to "L.5"
  (self-reference).

**Step 3.** Save and verify no §§N.6–N.10 references remain.

### 1.3 Dependency

Fixup 3 must complete before Fixup 1 because Fixup 1 needs to know
which N sections exist before adding pointers to them.


---


## 2. Fixup 1: Citation Cross-References

### 2.1 What needs to change

The audit found 21 instances of raw "Paper 1" or "Paper 10"
citations in Appendix L without parallel Appendix N pointers.
Files affected:

| File | Instances | Likely sections |
|:-----|:----------|:----------------|
| `appendix-L/L1-phase1.md` | 3 | Lemmas L.1.2 (action bound), L.1.5 (Casimir) |
| `appendix-L/L3-phase3.md` | 17 | Lemmas L.3.1 (heat kernel), L.3.4 (Theorem K.1), L.3.5 (Z₂), L.3.6 (GS = 0) |
| `appendix-L/L4-phase4.md` | 1 | Lemma L.4.1 (Suzuki + Paper 6 dilaton?) |

### 2.2 Find-and-replace pattern

For each occurrence of `Paper X (Section Y)` or `Paper X, Theorem Z`
without an Appendix N pointer, append `; Appendix N, §N.k`.

**The mapping:**

| QG5D result | Appendix N section |
|:------------|:-------------------|
| Theorem K.1 (Epstein vanishing) | §N.1.5 (or wherever in N.1) |
| Theorem S.1 (perturbative finiteness) | §N.1.x |
| $S_0 = 1 + 2\zeta(0) = 0$ | §N.1.x |
| Heat kernel factorization (Paper 1, App. S) | §N.1.x |
| Eisenstein lattice zeta (Paper 1, App. G) | §N.1.x |
| Orbifold structure (Paper 1, App. W) | §N.1.x |
| KK mass spectrum | §N.1.x |
| Theorem 1, $C_{\mathrm{GS}} = 0$ (Paper 10) | §N.2.1 |
| Theorem U.2a, $a_2 = a_4 = 0$ (Paper 10) | §N.2.2 |
| Proposition 3.1, $\mathbb{Z}_2$ cancellation (Paper 10) | §N.2.3 |
| Theorem 4.3, Wess–Zumino (Paper 10) | §N.2.4 |
| Lemmas A1–A3 (Paper 10) | §N.2.5 |
| Poisson bridge (Paper 10) | §N.2.6 |
| Theorem F.1, frozen dilaton (Paper 6) | §N.3 |
| CP² × S² × S¹ geometry (Paper 4) | §N.4 |

### 2.3 Execution

**Step 1.** Read the actual N-qg5d-infrastructure.md file to confirm
the precise section numbering (the table above is from memory; the
actual numbers may differ).

**Step 2.** For each of the 3 affected L files, do a regex search for
`Paper [0-9]` and inspect each match.

**Step 3.** For each match, check whether an "Appendix N" pointer
already follows. If not, append the appropriate `; Appendix N, §N.k`.

**Step 4.** Re-run the audit check (count raw "Paper X" without
following "Appendix N"). Should be 0.

### 2.4 What NOT to do

- **Don't remove the raw "Paper X" citation.** The Appendix N pointer
  is *additional*, not a replacement. Readers should be able to find
  the theorem in the original paper as well as in Appendix N.
- **Don't reformat surrounding text.** This is a pure-addition fixup;
  any sentence rewriting risks introducing new issues.


---


## 3. Fixup 2: Equation Numbering

### 3.1 What needs to change

`L1-phase1.md` uses flat numbering: equations labeled (L.1), (L.2),
..., (L.24). The other files (`L2-phase2.md`, `L3-phase3.md`,
`L4-phase4.md`) use hierarchical numbering: (L.2.1), (L.2.2),
(L.3.1), etc.

No collisions exist (L.1's flat numbers happen not to overlap with
L.2.1, L.3.1, L.4.1), but the inconsistency is visually jarring and
could confuse a reader who expects every equation to be prefixed by
its section number.

### 3.2 Execution

Mechanical renumbering: rename every (L.k) in `L1-phase1.md` to
(L.1.k), for k = 1, ..., 24.

**Step 1.** Find all `\tag{L.[0-9]+}` (or equivalent) in
`L1-phase1.md`.

**Step 2.** For each, replace `L.k` with `L.1.k`.

**Step 3.** Find all `(L.k)` references in the body text (e.g.,
"by equation (L.7)") and replace with `(L.1.k)`.

**Step 4.** Verify no other file references the old flat numbers.
Search the other L files and the preprint for `(L.1)` through
`(L.24)` and check whether any of those references are intended to
point to L.1's equations (in which case they need updating too).

### 3.3 What NOT to do

- **Don't renumber L.2, L.3, L.4.** They are already correct.
- **Don't change the section-level numbering** (Lemma L.1.1, Lemma
  L.1.2, etc.). Only the equation numbers change.


---


## 4. Execution Plan

### 4.1 Sequential or parallel?

Fixup 3 must complete first (it determines which N sections exist).
Fixups 1 and 2 are independent of each other and can run in parallel
after Fixup 3 is done.

```
Fixup 3 (15 min)
   │
   ├─→ Fixup 1 (30 min) ─┐
   │                      ├─→ Re-audit (15 min)
   └─→ Fixup 2 (15 min) ─┘
```

**Total wall-clock:** ~60 minutes if Fixups 1 and 2 run in parallel,
~75 minutes sequential.

### 4.2 Single-agent or multi-agent?

The fixups are small enough that one agent can do all three
sequentially. Multi-agent parallelism saves only ~15 minutes but
introduces coordination overhead (the agents need to read the same
files and avoid edit conflicts).

**Recommendation: single agent, sequential.** The savings from
parallelism don't justify the coordination cost for tasks this small.

### 4.3 The agent prompt

Give the agent this context:

1. The Wave 10 audit report (W10-25)
2. This strategy document
3. Permission to read and edit `appendix-L/*.md` and
   `appendix-N/N-qg5d-infrastructure.md`
4. Instruction to do Fixup 3, then Fixup 1 and Fixup 2, in that
   order
5. Instruction to re-run the audit checks (count §§N.6–N.10
   references, count raw "Paper X" without "Appendix N", check
   equation numbering pattern) and report PASS/FAIL

### 4.4 Quality gate

After all three fixups, verify:

| Check | Expected result |
|:------|:----------------|
| Search for `§N\.[6-9]` or `§N\.10` in `appendix-L/` | 0 matches |
| Search for `Paper [0-9]` not followed by `Appendix N` in `appendix-L/` | 0 matches |
| Search for `\tag{L\.[0-9]+}` (flat) in `L1-phase1.md` | 0 matches |
| Search for `\tag{L\.1\.[0-9]+}` in `L1-phase1.md` | 24 matches |
| The 9 PASS checks from Wave 10 | Still PASS |
| Total content lines changed | ~30 lines max |

If all gates pass, the appendix is ready for assembly into the
preprint.


---


## 5. After the Fixups

The integration addendum (`12-integration-addendum.md`, Section 6
"What Remains for Publication") lists the remaining mechanical work:

| Task | Effort | Status |
|:-----|:-------|:-------|
| Fixup 1 | 30 min | **This document** |
| Fixup 2 | 15 min | **This document** |
| Fixup 3 | 15 min | **This document** |
| Paste preprint update fragments | 15 min | After fixups |
| Assemble Appendix L from sections | 30 min | After fixups |
| Insert Appendix N | 15 min | After Fixup 3 |
| Final visual inspection | 30 min | After all above |
| **Total post-fixup** | **~1.5 hours** | |

After the 60–75 minutes of fixups + 1.5 hours of assembly = **~3
hours total** to a complete Clay submission.


---


## 6. Risk Assessment

| Risk | Severity | Mitigation |
|:-----|:---------|:-----------|
| Fixup 3 missing references | Low | Step 1 enumerates them via regex search |
| Fixup 1 wrong N section pointer | Low | Mapping table in §2.2; verifiable against Appendix N TOC |
| Fixup 2 missed equation reference | Medium | Step 4 audits the body text for references |
| Re-audit reveals new issue | Low | The 9 PASS checks from Wave 10 are independent of these fixups |
| Fixup introduces typo | Low | Mechanical edits, no new prose |

The only meaningful risk is Fixup 2 missing an equation reference
elsewhere in the preprint (e.g., a citation from Appendix M to L.1
equations). This is mitigated by the Step 4 audit but worth a
careful look.


---


## 7. What This Does NOT Address

These fixups are cosmetic and structural. They do NOT:

1. **Add new mathematics.** No new lemmas, no new proofs.
2. **Change the H4 conditional structure.** L.2 and the AF form of
   L.4 remain conditional.
3. **Touch the Wave 1–8 research memos.** Those stay frozen as the
   audit trail.
4. **Modify the preprint sections outside Appendix L/N.** Sections
   1–5, Appendices A–K, M are untouched.
5. **Affect the PROOF-CHAIN steps 1–14.** Only Steps 15–18 (the new
   ones) are involved, and they don't reference the changed
   equation numbers.

The fixups bring the publication text up to consistent style. The
mathematical content is unchanged and remains 9/10 PASS on the audit.


---


## 8. One Sentence

Three mechanical edits, one quality gate, ninety minutes — and the
appendix is consistent, citable, and ready for assembly into the
final preprint.
