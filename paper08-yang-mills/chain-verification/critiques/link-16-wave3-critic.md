# Link 16 Wave 3 Critic — OS-Axiom Convention Harmonization

**Target:** Continuum flowed Schwinger functions: unique (not subsequential), OS0--OS4 at fixed $t > 0$  
**Repair under review:** L16-repair.md (Wave 2 Author)  
**Wave 1 verdict:** WEAKENED (A6: OS labeling inconsistency)  
**Wave:** 3, adversarial  
**Runner:** Claude Sonnet 4.6, 2026-04-13  

---

## Verdict: WEAKENED

The repair correctly identifies all five problem sites and proposes an appropriate structural fix (declaration + five line edits). However, the convention-declaration paragraph (edit (a)) contains an algebraically inverted crosswalk sentence that would actively mislead a reader. This is not a phantom concern — the sentence is wrong in every coherent reading. The line edits (b)–(f) are independently correct and survive scrutiny. The repair is therefore WEAKENED, not SURVIVED: the declaration paragraph must be corrected before the inconsistency is genuinely resolved.

---

## Vector A — Numbering conventions: CONFIRMED WITH ONE CRITICAL ERROR

**§5.7 convention verified directly:**

`preprint/sections/05-continuum-limit.md` line 2174:
> "We verify the five Osterwalder--Schrader axioms (OS1--OS5) for the continuum Schwinger functions..."

Line 2181: **(OS1) Temperedness.** Line 2252: **(OS2) Euclidean covariance.** Line 2321: **(OS3) Reflection positivity.** Line 2376: **(OS4) Symmetry.** Line 2384: **(OS5) Cluster decomposition.**

Author's claim confirmed: §5.7 uses OS1–OS5 with OS3 = RP.

**§L.2 convention verified directly:**

`preprint/sections/L-clay-conjectures.md` lines 1177–1179:
> "(OS0) Temperedness; (OS1) Euclidean covariance; (OS2) Reflection positivity; (OS3) Symmetry; (OS4) Cluster decomposition."

Author's claim confirmed: §L.2 uses OS0–OS4 with OS2 = RP.

**The conflict table is correct.** The conventions differ by exactly one throughout.

**Critical error in edit (a) — the convention-declaration paragraph:**

The proposed paragraph (L16-repair.md lines 131–133) states:

> "Cross-references of the form `\S5.7, OS$k$' should be read as `\S5.7, OS$(k+1)$' in the \S5.7 numbering."

This sentence is internally incoherent. It says a §5.7 cross-reference "OS$k$" (already in §5.7 notation) should be re-read as "OS$(k+1)$" in §5.7 notation — transforming a §5.7 label into a larger §5.7 label, which is meaningless.

The Author's own repair goal is to tell a reader in §L.2 context that a citation "§5.7, OS3" refers to §L.2's OS2 (reflection positivity). The correct crosswalk reads:

> "A cross-reference of the form §5.7, OS$k$ refers to the same axiom as OS$(k-1)$ in the present Appendix L convention."

Under the Author's stated mapping (§5.7 OS3 = RP = §L.2 OS2), we have: §5.7 OS$k$ ↔ §L.2 OS$(k-1)$. The sign in the declaration is wrong: "$k+1$" appears instead of "$k-1$". A reader following the declaration literally would look up "§5.7, OS3" and conclude it refers to §5.7 OS4 (= Symmetry in §5.7, = OS3 in §L.2) — the exact wrong axiom.

The line edits (b)–(f) are self-sufficient disambiguations (they add explicit axiom names at each site) and are correct independently. But the declaration paragraph is supposed to be the primary resolution tool covering all present and future cross-references; its arithmetic is backwards.

**Canonical convention check:** The Author's choice of OS0–OS4 as the §L.2 canonical form (using OS0 = OS0' of the 1975 paper) is historically sound. Osterwalder–Schrader 1975, CMP 42, Theorem 3.3, replaces the 1973 regularity condition (their OS0) with the corrected linear-growth condition (their OS0'). The §5.7 convention (which absorbs OS0' into OS1's "Step 3" note at line 2238) differs from the 1975 numbering. §L.2's OS0–OS4 is the more faithful rendering. This aspect of the Author's reasoning is correct.

---

## Vector B — Site enumeration: CONFIRMED, ONE ADDITIONAL SITE MISSED

**Author's enumeration (lines 164, 1218, 1239, 2486, 2535):** All five sites verified directly. Each uses OS3 in a context where the §L.2 convention assigns OS3 = Symmetry, yet the intended referent is reflection positivity.

**Full grep of `OS3` in L-clay-conjectures.md** (all occurrences):

| Line | Text (verbatim) | Assessment |
|-----:|:----------------|:-----------|
| 164 | `from OS3 (reflection positivity) as established in Section 5.6.` | Wrong under §L.2: OS3 = Symmetry. **Problem site.** Author flags this. |
| 979 | `\S5.7, OS1 bound) yields...` | OS1 — no conflict (OS1 = Euclidean covariance in both sections). |
| 1143 | OS0' growth condition | Correct §L.2 usage. |
| 1218 | `(Osterwalder--Seiler 1978; \S5.7, OS3).` | Cross-ref using §5.7 label inside OS2 block. **Problem site.** Author flags. |
| 1239 | `argument of \S5.7, OS3 then transfers RP...` | Same. **Problem site.** Author flags. |
| 1261 | `*OS3 (Symmetry).*` | Correct §L.2 usage. |
| 2006 | `**OS2** (reflection positivity): Part (iii) above.` | Correct §L.2 usage. |
| 2008 | `**OS3** (symmetry): the Schwinger functions...` | Correct §L.2 usage. |
| 2065 | `OS3 symmetry` | Correct. |
| 2079 | `OS3 symmetry` | Correct. |
| 2486 | `OS3 (reflection positivity) implies` | Wrong under §L.2. **Problem site.** Author flags. |
| 2535 | `unconditional (OS3 + Seiler).` | Wrong under §L.2. **Problem site.** Author flags. |

**Additional site not in Author's list:** `preprint/sections/04-lattice-proof-part1.md` line 1774 uses **OS3 = Reflection positivity** in §H.8 (the SU(2) KK warmup), inside a block labeled OS1–OS5 (line 1767 uses OS1 = Regularity, not Temperedness, a third and distinct convention). This third convention (OS1 = Regularity, OS3 = RP) is outside Appendix L, so it is not covered by the Appendix-L-scoped declaration. The Author restricts the declaration to "Throughout Appendix L" — this is correct scoping, but a reader cross-referencing §H.8 will encounter yet a third OS labeling without any harmonization note. The Author does not flag §H.8. This is a residual inconsistency.

**Missed site verdict:** The §H.8 locus is not strictly within the Author's repair scope (Appendix L), and the §H.8 OS convention (OS1=Regularity, OS3=RP) is a further complication that neither the Wave 1 Critic nor the Author addressed. It weakens the completeness of the repair.

**OS2 cross-contamination check (bonus):** Are there uses of "OS2" in §5.7 context (= Euclidean covariance in §5.7) that might be confused with §L.2's OS2 (= RP) inside Appendix L? Grep on L-clay-conjectures.md for "OS2":

| Line | Text | Context |
|-----:|:-----|:--------|
| 1178 | `(OS2) Reflection positivity` | §L.2 Lemma L.2.3 header — correct local. |
| 1214 | `*OS2 (Reflection positivity).*` | §L.2 body — correct local. |
| 2006 | `**OS2** (reflection positivity)` | §L.2/L.3 — correct local. |

No bare "OS2" in Appendix L is used with §5.7's meaning (Euclidean covariance). No additional conflict introduced. Vector B sub-question answered: no.

---

## Vector C — Proposed edits vs. preprint verbatim text: FOUR OF FIVE EXACT, ONE MISMATCH

### Edit (b) — line 1218

Preprint verbatim (lines 1216–1218):
> "The lattice measure $\mu_K$ is reflection-positive for all $K$ (Osterwalder--Seiler 1978; \S5.7,  
> OS3). The gradient flow is a deterministic function of the gauge"

Author's FROM:
```
reflection-positive for all $K$ (Osterwalder--Seiler 1978; \S5.7,
OS3).
```

**Match confirmed.** Proposed TO reads `OS3 $=$ OS2 here` — adequate disambiguation.

### Edit (c) — line 1239

Preprint verbatim (line 1239):
> "argument of \S5.7, OS3 then transfers RP to the continuum limit:"

Author's FROM:
```
argument of \S5.7, OS3 then transfers RP to the continuum limit:
```

**Match confirmed.** Proposed TO is verbose but correct.

### Edit (d) — line 164

Preprint verbatim (line 164):
> "from OS3 (reflection positivity) as established in Section 5.6."

Author's FROM:
```
from OS3 (reflection positivity) as established in Section 5.6.
```

**Match confirmed.**

### Edit (e) — line 2486

Preprint verbatim (lines 2485–2486):
> "reconstructed transfer matrix. OS3 (reflection positivity) implies"

Author's FROM:
```
OS3 (reflection positivity) implies
```

**Match confirmed.** (Partial-line match; surrounding context is consistent.)

### Edit (f) — line 2535

Preprint verbatim (line 2535):
> "unconditional (OS3 + Seiler). Sub-clauses (iv-b) and (v) are"

Author's FROM:
```
unconditional (OS3 + Seiler).
```

**Match confirmed.** However, the Author's proposed TO:
```
unconditional (OS2 + Seiler; OS2 = reflection positivity in the Appendix L convention).
```

creates a redundant parenthetical. If the convention-declaration paragraph is placed at the top of §L.2, the reader at line 2535 (§L.4) is over 1300 lines later; the repetition is helpful and not an error. But the declaration paragraph's arithmetic error (Vector A) would have already confused the reader by line 2535. The parenthetical in edit (f) is self-correcting (it directly names RP), so the error in the declaration does not propagate into this edit — the edit reads correctly in isolation.

**Convention-declaration flow check (secondary concern):** The Author proposes inserting the declaration as the first paragraph of §L.2, before Lemma L.2.1. Read the top of §L.2:

Lines 1171–1180 show Lemma L.2.3 opens immediately after the §L.2 section heading. The declaration insertion is structurally sound. No section-flow disruption is created. Confirmed.

---

## Vector D — Cross-node effects (L15, L17): NONE

**L15 (gradient flow §L.1):** L15 uses no OS axiom labels. The critic (link-15-critic.md) identifies five attacks; none concerns axiom numbering. OS labels appear in §L.2 and §L.4, not in the gradient-flow well-posedness section (§L.1). The Author's edits do not touch §L.1. No cross-node contamination.

**L17 (composite operators §L.3–L.4):** L17 uses OS labels at lines 1999–2013 (§L.3 body) and line 2486 and 2535 (§L.4). Lines 1999–2013 use OS0'–OS4 in the correct §L.2 convention throughout (OS2=RP, OS3=symmetry) — no repair needed there. Lines 2486 and 2535 are exactly the Author's edit sites (e) and (f). Edits (e) and (f) do not alter the mathematical content of L17; they add only parenthetical disambiguation. L17's verdict (SURVIVED) is unaffected.

**L17 cross-reference note:** L17 (link-17-critic.md) does not cite any OS axiom numbering in its attack or defense. The OS reconstruction theorem is invoked by name at lines 2015–2016 in §L.3, using "Osterwalder–Schrader" without a numbered label at that point — no conflict exists there.

---

## Vector E — Full grep for "reflection positivity": THIRD CONVENTION EXPOSED

All hits in `preprint/sections/`:

- `05-continuum-limit.md` (§5.7): OS3=RP throughout. (Author's §5.7 source; not touched by repair.)
- `L-clay-conjectures.md`: OS3-as-RP at lines 164, 2486, 2535 (Author corrects); OS2=RP at lines 1178, 1214, 2006 (correct under §L.2).
- `04-lattice-proof-part1.md` line 1774: **OS3 = Reflection positivity** under a **third convention** (OS1=Regularity, OS2=Euclidean covariance, OS3=RP, OS4=Symmetry, OS5=Cluster). This is §H.8.
- `D-reflection-positivity.md`: All occurrences are descriptive (no axiom number label used). No conflict.
- `C-transfer-matrix.md`, `F-area-law-mass-gap.md`, `A-laplacian-spectrum.md`, `01-introduction.md`, `08-conclusion.md`, `02-geometric-framework.md`, `00-abstract.md`, `M-gap-closures-r00.md`: All use "reflection positivity" without OS numbering. No conflict.

**Net:** The §H.8 locus (04-lattice-proof-part1.md:1774) uses a third OS convention (OS1–OS5 with OS1=Regularity rather than Temperedness). This convention is internally inconsistent with both §5.7 and §L.2, and the Author's declaration ("Throughout Appendix L...") does not scope to §H.8. This is a residual gap.

---

## Summary (≤150 words)

The repair is **WEAKENED** on two grounds. First and most seriously, the convention-declaration paragraph (edit (a)) contains an algebraically inverted crosswalk: it states "§5.7, OS$k$ should be read as §5.7, OS$(k+1)$" when the correct translation is §5.7, OS$k$ ↔ Appendix L, OS$(k-1)$. A reader following the declaration literally would misdirect from OS3=RP to OS4=Symmetry. The five line edits (b)–(f) are individually correct and self-rescue by naming the axioms explicitly, but the governing declaration is wrong. Second, a third OS convention in §H.8 (04-lattice-proof-part1.md line 1774: OS1=Regularity, OS3=RP) is outside the Author's repair scope but creates a further cross-reference hazard not acknowledged. Required fix: invert the crosswalk sign in edit (a) and note the §H.8 third convention.

---

## Required repair (minimal)

**Edit (a) correction:** Replace the final sentence of the declaration paragraph:

FROM:
```
Cross-references of the form ``\S5.7, OS$k$'' should be read as ``\S5.7, OS$(k+1)$'' in the \S5.7 numbering.
```

TO:
```
A cross-reference of the form ``\S5.7, OS$k$'' refers to the same axiom as OS$(k-1)$ in the present Appendix L convention (e.g., \S5.7's OS3 = reflection positivity = OS2 here).
```

**§H.8 acknowledgment (non-blocking):** Add a brief note in §H.8 (04-lattice-proof-part1.md near line 1764) that the OS1–OS5 labeling in that section's heuristic step matches §5.7 (OS3=RP), not the §L.2 convention.
