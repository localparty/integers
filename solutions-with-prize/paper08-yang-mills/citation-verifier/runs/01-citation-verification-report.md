# Citation Verification Report

**Date:** 2026-04-06
**Session:** r10 (citation-verifier run)
**Scope:** All proof-critical citations in the Yang--Mills preprint

---

## #1: Balaban, CMP 95 (1984)

**Status:** LOCAL
**PDF:** `journals/balaban-CMP95-1984.pdf`
**Title page:** Commun. Math. Phys. 95, 17--40 (1984) -- CONFIRMED
**Numbering:** Lettered sections (A--F), part-based proposition numbering (Prop. 1.1, 1.2)
**Results verified:**
- Prop. 1.1 (p. 33): boundedness of G with $\gamma_0$ independent of $k$
- Prop. 1.2 (p. 35): exponential decay $|G(x,y)| \leq O(1)e^{-\delta_0|x-y|}$, $\delta_0$ depending on $d$ only

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1386` -- cites "CMP 95, Sec. 3" -- CORRECT
- `sections/05-continuum-limit.md:1389` -- cites "CMP 95, Prop. 1.2" -- CORRECT
- `PROOF-CHAIN.md:52--68` -- cites "CMP 95 Prop. 1.2" -- CORRECT

**Corrections applied:** Prop. 3.2 -> Prop. 1.2 (prior session)

---

## #2: Balaban, CMP 109 (1987)

**Status:** LOCAL
**PDF:** `journals/balaban-CMP109-1987.pdf`
**Title page:** Commun. Math. Phys. 109, 249--301 (1987) -- CONFIRMED
**Numbering:** Numbered sections (0--5), plain theorem numbering (Thm 1, 2, 3)
**Results verified:**
- Thm 1 (p. 259): UV stability -- polymer weights satisfy $|E^{(j)}(X)| \leq E_0 \exp(-\kappa d_j(X))$
- Thm 2 (p. 259): running coupling trajectory for SU(2)
- Thm 3 (p. 264): detailed version of Thm 1 with all inductive constants
- Key bound (1.18): $\kappa$ independent of $k$ -- CONFIRMED

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1352` -- cites "CMP 109 (1987), Thm 1 (detailed: Thm 3)" -- CORRECT
- `sections/H-balaban-analyticity.md:52` -- cites "CMP 109, Theorem 1 (detailed: Theorem 3)" -- CORRECT
- `PROOF-CHAIN.md:13` -- cites "CMP 109, Thm 1 (detailed: Thm 3)" -- CORRECT
- `sections/I3-N-dependence-tracking.md:129` -- cites "Balaban (CMP 109, Theorem 1; detailed: Theorem 3)" -- CORRECT

**Corrections applied:** Thm 2.1 -> Thm 1 (prior session)

---

## #3: Balaban, CMP 119 (1988)

**Status:** LOCAL
**PDF:** `journals/balaban-CMP119-1988.pdf`
**Title page:** Commun. Math. Phys. 119, 243--285 (1988) -- CONFIRMED
**Numbering:** Single UNNUMBERED "Theorem." on p. 245
**Results verified:**
- Theorem (p. 245, unnumbered): "If $\rho_k$ satisfies the assumptions described in Sect. 2, then $T\rho_k$ satisfies also the corresponding assumptions."

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1352` -- was "CMP 119 (1988), Thm 1" -- **FIXED** to "Theorem (unnumbered, p. 245)"
- `sections/H-balaban-analyticity.md:113` -- was "CMP 119, Theorem 1" -- **FIXED**
- `sections/H-balaban-analyticity.md:335` -- was "CMP 119 (1988), Thm 1" -- **FIXED**
- `sections/I-gap-closures.md:55` -- was "CMP 119, Thm 1" -- **FIXED**

**Corrections applied:** "Thm 1" -> "Theorem (unnumbered, p. 245)" in 4 places (this session)

---

## #4: Balaban, CMP 98 (1985)

**Status:** WEB
**PDF:** not available (Project Euclid bot detection; ScienceDirect paywalled)
**Title:** "Averaging operations for lattice gauge theories" -- CONFIRMED via INSPIRE API
**Metadata:** Commun. Math. Phys. 98, 17--51 (1985) -- CONFIRMED
**Numbering:** Lettered sections (A--F) per ledger note from prior session

**Preprint references this paper at:**
- `sections/H-balaban-analyticity.md:88` -- cites "CMP 98 (1985)" -- CORRECT
- `sections/H-balaban-analyticity.md:338` -- cites "CMP 98 (1985), Sec. E" -- CORRECT (lettered sections)
- `PROOF-CHAIN.md:60` -- cites "CMP 98 Sec. E" -- CORRECT

**Corrections applied:** Sec. 2 -> Sec. E (prior session)

---

## #5: Dimock, arXiv:1108.1335 / Rev. Math. Phys. 25 (2013)

**Status:** LOCAL
**PDF:** `journals/dimock-arXiv1108.1335-2011.pdf`
**Title page:** "The Renormalization Group According to Balaban, I. Small Fields" -- CONFIRMED
**Numbering:** Sequential across all result types (Thm 1, Lemma 2, ..., Thm 14, Lemma 15, ...)
**Results verified:**
- Thm 1 (p. 2): stability bound for partition function
- Thm 14 (p. 23): main RG flow theorem -- density representation preserved under RG step with explicit bounds

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1716` -- cites "Dimock (arXiv:1108.1335, 2011; published Rev. Math. Phys. 25, 2013, Thm 14)" -- CORRECT
- `sections/H-balaban-analyticity.md:100` -- cites "Dimock, arXiv:1108.1335, Thm 14" -- CORRECT
- `PROOF-CHAIN.md:62` -- cites "Dimock (arXiv:1108.1335, 2011, Thm 14)" -- CORRECT

**Corrections applied:** Thm 3.1 -> Thm 14 (prior session)

---

## #6: Fredenhagen--Marcu, CMP 92 (1983)

**Status:** LOCAL
**PDF:** `journals/fredenhagen-marcu-CMP92-1983.pdf`
**Title page:** "Charged States in Z_2 Gauge Theories" -- Commun. Math. Phys. 92, 81--119 (1983) -- CONFIRMED
**Numbering:** Section-based (Prop. 2.1 on p. 85)
**Results verified:**
- Prop. 2.1 (p. 85): algebraic characterization of disjoint representations of observable algebra B
- Confinement/deconfinement criterion developed throughout

**Content note:** Paper is specifically about $\mathbb{Z}_2$ gauge theories with matter fields. The preprint correctly states "We state the continuum analogue" (F-area-law-mass-gap.md:128) when applying the criterion to SU(N). The generalization is standard in the literature.

**Preprint references this paper at:**
- `sections/04-lattice-proof-part1.md:662` -- cites "Fredenhagen--Marcu, CMP 92, 1983" -- CORRECT
- `sections/04-lattice-proof-part1.md:746` -- was "Fredenhagen--Marcu theorem (1986)" -- **FIXED** to (1983)
- `sections/04-lattice-proof-part1.md:1193` -- was "Fredenhagen--Marcu (1986)" -- **FIXED** to (1983)
- `sections/F-area-law-mass-gap.md:127` -- was "Fredenhagen and Marcu (1986)" -- **FIXED** to (1983)

**Corrections applied:**
- CMP 104 (1986) -> CMP 92 (1983) (prior session)
- Year 1986 -> 1983 in 3 residual in-text citations (this session)

---

## #7: Kotecky--Preiss, CMP 103 (1986)

**Status:** LOCAL
**PDF:** `journals/kotecky-preiss-CMP103-1986.pdf`
**Title page:** "Cluster Expansion for Abstract Polymer Models" -- Commun. Math. Phys. 103, 491--498 (1986) -- CONFIRMED
**Numbering:** UNNUMBERED results (single "Theorem." p. 492, single "Proposition." p. 494)
**Results verified:**
- Theorem (p. 492, unnumbered): convergence criterion $\sum_{\gamma': \gamma' \text{ incomp. } \gamma} e^{a(\gamma')+d(\gamma')} |\Phi(\gamma')| \leq a(\gamma)$
- Proposition (p. 494, unnumbered): decay of correlations

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1368` -- was "Kotecky--Preiss (CMP 83, 1982)" -- **FIXED** to (CMP 103, 1986)
- `sections/04-lattice-proof-part1.md:562` -- cites "Koteck\'y--Preiss criterion" -- CORRECT (no volume cited)
- `sections/04-lattice-proof-part1.md:727` -- cites "Koteck\'y--Preiss" -- CORRECT

**Corrections applied:**
- Garbled duplicate entry "CMP 83 (1982)" removed from references.md (prior session)
- Residual "CMP 83, 1982" in body fixed to "CMP 103, 1986" (this session)

---

## #8: Osterwalder--Schrader, CMP 31 (1973)

**Status:** LOCAL
**PDF:** `journals/osterwalder-schrader-CMP31-1973.pdf`
**Title page:** "Axioms for Euclidean Green's Functions" -- Commun. Math. Phys. 31, 83--112 (1973) -- CONFIRMED
**Numbering:** 8 numbered sections; OS axioms labeled (E0)--(E4)
**Results verified:**
- Axioms (E0)--(E4): Temperedness, Covariance, Positivity, Symmetry, Cluster
- Main theorems in Section 3: "E -> R" and "R -> E" reconstruction

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:2237` -- cites "Osterwalder--Schrader 1973, 1975" -- CORRECT
- `sections/05-continuum-limit.md:2403--2404` -- full citation -- CORRECT
- `sections/references.md:69--70` -- full entry -- CORRECT

**Corrections applied:** none needed

---

## #9: Osterwalder--Schrader, CMP 42 (1975)

**Status:** LOCAL
**PDF:** `journals/osterwalder-schrader-CMP42-1975.pdf`
**Title page:** "Axioms for Euclidean Green's Functions II" -- Commun. Math. Phys. 42, 281--305 (1975) -- CONFIRMED
**Numbering:** Chapters I--IV
**Results verified:**
- Corrects Lemma 8.8 from OS I (p. 282, Remark 2)
- New condition (E0') = "linear growth condition" introduced in Chapter IV
- Theorem E<->R revisited (p. 285)

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:1961` -- cites "corrected OS0' growth condition (Osterwalder--Schrader 1975)" -- CORRECT
- `sections/05-continuum-limit.md:2186` -- cites "growth condition of Osterwalder--Schrader (1975)" -- CORRECT

**Corrections applied:** none needed

---

## #10: Osterwalder--Seiler, Ann. Phys. 110 (1978)

**Status:** WEB (paywalled, ScienceDirect)
**Metadata:** "Gauge field theories on a lattice" -- Ann. Phys. 110, 440--471 (1978) -- CONFIRMED via prior session
**DOI:** 10.1016/0003-4916(78)90039-8

**Preprint references this paper at:**
- `sections/05-continuum-limit.md:2062--2063` -- cites "Osterwalder--Seiler theorem (Osterwalder--Seiler 1978)" -- CORRECT
- `sections/D-reflection-positivity.md:1` -- cites "Osterwalder-Seiler theorem (1978)" -- CORRECT
- `sections/07-previous-approaches.md:43` -- cites "Osterwalder--Seiler 1978" -- CORRECT
- `sections/references.md:78--79` -- full entry -- CORRECT

**Corrections applied:** none needed

---

## #11: Luscher, CMP 85 (1982)

**Status:** LOCAL
**PDF:** `journals/luscher-CMP85-1982.pdf`
**Title page:** "Topology of Lattice Gauge Fields" -- Commun. Math. Phys. 85, 39--48 (1982) -- CONFIRMED
**Numbering:** NO formally numbered theorems. Main result: properties (i)--(v) on p. 40. One unnumbered Lemma (p. 44).
**Results verified:**
- Properties (i)--(v) (p. 40): topological charge assignment
- Smallness condition: $\mathrm{Tr}\{1 - U(\hat{p})\} < \epsilon$ with $\epsilon \leq 0.03$ for SU(2)

**Preprint references this paper at:**
- `sections/04-lattice-proof-part1.md:764` -- cites "L\"uscher, CMP 85, 1982" -- CORRECT
- `sections/04-lattice-proof-part1.md:776` -- cites "CMP 85, 1982, properties (i)--(v)" -- CORRECT

**Corrections applied:** "Theorem 1" -> "properties (i)--(v)" (prior session)

---

## #12: Chatterjee, arXiv:2104.05268 (2021)

**Status:** LOCAL
**PDF:** `journals/chatterjee-arXiv2104.05268-2021.pdf`
**Title:** "A probabilistic mechanism for quark confinement"
**Note:** Paper is LOCAL in ledger but **NOT cited anywhere in the preprint body**. Orphan in ledger -- kept for background context only.

**Corrections applied:** none needed

---

## Missing References Added to `references.md`

| Reference | Section where cited | Status |
|:----------|:-------------------|:-------|
| Symanzik (1983), Nucl. Phys. B 226, 187--204 | 05-continuum-limit.md, I-gap-closures.md, J-lattice-symanzik-basis.md | Added |
| Luscher, Weisz (1985), CMP 97, 59--77 | 05-continuum-limit.md:2043 | Added |
| Luscher (1977), CMP 54, 283--292 | 04-lattice-proof-part1.md:480 | Added |
| Necco, Sommer (2002), Nucl. Phys. B 622, 328--346 | I-luscher-test.md:151 | Added |
| Prasad, Sommerfield (1975), PRL 35, 760--762 | 01-introduction.md:168 | Added |

## Cleanup Applied to `references.md`

- Removed duplicate Kotecky-Preiss entry with correction note (was lines 215--218)
- Replaced sparse Balaban series entry with individual paper entries (CMP 95, 96, 98, 102, 109, 119)
- Replaced sparse Dimock entry with full metadata (Rev. Math. Phys. 25, 2013, arXiv:1108.1335)

---

## Summary

| # | Citation | Status | Errors found | Errors fixed |
|:--|:---------|:-------|:-------------|:-------------|
| 1 | Balaban, CMP 95 (1984) | LOCAL | 0 (this session) | 0 |
| 2 | Balaban, CMP 109 (1987) | LOCAL | 0 (this session) | 0 |
| 3 | Balaban, CMP 119 (1988) | LOCAL | 4 ("Thm 1" for unnumbered thm) | 4 |
| 4 | Balaban, CMP 98 (1985) | WEB | 0 (this session) | 0 |
| 5 | Dimock, arXiv:1108.1335 (2013) | LOCAL | 0 (this session) | 0 |
| 6 | Fredenhagen--Marcu, CMP 92 (1983) | LOCAL | 3 (residual year 1986) | 3 |
| 7 | Kotecky--Preiss, CMP 103 (1986) | LOCAL | 1 (residual "CMP 83, 1982") | 1 |
| 8 | Osterwalder--Schrader, CMP 31 (1973) | LOCAL | 0 | 0 |
| 9 | Osterwalder--Schrader, CMP 42 (1975) | LOCAL | 0 | 0 |
| 10 | Osterwalder--Seiler, Ann. Phys. 110 (1978) | WEB | 0 | 0 |
| 11 | Luscher, CMP 85 (1982) | LOCAL | 0 (this session) | 0 |
| 12 | Chatterjee, arXiv:2104.05268 (2021) | LOCAL | 0 (orphan in ledger) | 0 |

**Total proof-critical citations:** 12
**Total LOCAL:** 10
**Total WEB:** 2 (CMP 98, Osterwalder-Seiler)
**Errors found this session:** 8 in-text + 5 missing refs + cleanup
**Errors fixed this session:** 8 in-text + 5 refs added + bibliography cleanup
**Remaining WEB (need download):** Balaban CMP 98 (1985), Osterwalder-Seiler Ann. Phys. 110 (1978)

**Cumulative corrections (all sessions):** 12

---

## Consistency Check (Phase 5c)

- Every proof-critical entry in `citation-tiers.md` has a matching entry in `references.md`: **PASS**
- Metadata (volume, pages, year) matches between the two files: **PASS**
- All in-text correction applied are reflected in `references.md`: **PASS**
- No orphan proof-critical refs in `references.md` without ledger entry: **PASS**
- Chatterjee: LOCAL in ledger, not in `references.md`, not cited in body: **CONSISTENT** (orphan in ledger only)
