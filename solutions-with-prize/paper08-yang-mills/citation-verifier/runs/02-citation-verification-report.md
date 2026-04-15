# Citation Verification Report

**Session:** r12, 2026-04-06
**Scope:** Full audit — Phase 1 (inventory), Phase 2 (LOCAL verification), Phase 4 (error detection), Phase 5 (updates)

---

## Phase 1: Inventory and Completeness

### 1a. Bibliography entries in `references.md` (after corrections)

22 sections, ~65 entries. See `references.md` for full list.

### 1b. In-text citation sources scanned

All 24 body files checked:
- `sections/00-abstract.md` through `sections/08-conclusion.md`
- `sections/A-laplacian-spectrum.md` through `sections/K-balaban-general-groups.md`
- `PROOF-CHAIN.md`

### 1c. Missing and orphan analysis

**MISSING references found and added (10):**

| # | Paper | Where cited | Action |
|:--|:------|:------------|:-------|
| M1 | Dubovsky, Gorbenko (2016), JHEP 02:022 | I-luscher-test.md | Added to references.md |
| M2 | Gaikwad, Gorbenko, Guerrieri (2024), JHEP 01:090 | I-luscher-test.md | Added to references.md |
| M3 | Athenodorou, Dubovsky, Luo, Teper (2024), arXiv:2411.03435 | I-luscher-test.md | Added to references.md |
| M4 | Athenodorou, Caristo, Caselle (2024), arXiv:2411.16507 | I-luscher-test.md | Added to references.md |
| M5 | Weisz, Wohlert (1984), Nucl. Phys. B 236, 397–422 | J-lattice-symanzik-basis.md | Added to references.md |
| M6 | Nachtergaele, Sims (2006), CMP 265, 119–130 | 05-continuum-limit.md:1136 | Added to references.md |
| M7 | Helgason (1978), Academic Press | I-gap-closures.md:412; I4-other-gauge-groups.md:412 | Added to references.md |
| M8 | Besse (1987), Springer | I4-other-gauge-groups.md:53 | Added to references.md |
| M9 | Borel (1953), Ann. Math. 57, 115–207 | I4-other-gauge-groups.md:225,248 | Added to references.md |
| M10 | Dimock (2013b), J. Math. Phys. 54, 092301 | H-balaban-analyticity.md:100 | Added to references.md |

**ORPHAN references (in `references.md`, not cited in body):**

- Chatterjee, arXiv:2104.05268 — tracked in ledger (entry #12), confirmed present in journals/. Not cited in any body section. Kept for context.
- Several entries in the Kaluza-Klein, instantons, holography, and e-dimension framework sections may be cited only in later papers of the series. Not removed.

---

## Phase 2: LOCAL paper verifications

### #1: Balaban, CMP 95, 17–40 (1984)

**Status:** LOCAL
**PDF:** `journals/balaban-CMP95-1984.pdf`
**Title page:** CMP 95, 17–40 (1984) — CONFIRMED
**Numbering:** Part-based propositions (Prop. 1.1, Prop. 1.2); lettered sections (A-F)
**Results verified:**
- Prop. 1.1 (p. 33): boundedness of propagator G with γ₀ independent of k
- Prop. 1.2 (p. 35): exponential decay |G(x,y)| ≤ O(1)e^{−δ₀|x−y|}
- No Prop. 3.2 exists in this paper

**Preprint references this paper at:**
- Multiple files — cites "Prop. 1.2 (p. 35)" — CORRECT (was Prop. 3.2, fixed in r09)

**Corrections applied:** Prop. 3.2 → Prop. 1.2 (fixed r09)

---

### #2: Balaban, CMP 109, 249–301 (1987)

**Status:** LOCAL
**PDF:** `journals/balaban-CMP109-1987.pdf`
**Title page:** CMP 109, 249–301 (1987) — CONFIRMED
**Numbering:** Plain theorem numbering (Thm 1, 2, 3); numbered sections (0–5)
**Results verified:**
- Thm 1 (p. 259): UV stability — polymer weights satisfy |E^(j)(X)| ≤ E₀ exp(−κ d_j(X))
- Thm 2 (p. 259): running coupling trajectory for SU(2)
- Thm 3 (p. 264): detailed version of Thm 1

**Preprint references this paper at:**
- `sections/I-gap-closures.md:55` — cites "CMP 109, Thm 1" — CORRECT
- `sections/05-continuum-limit.md:1352` — cites "CMP 109, Thm 1 (detailed: Thm 3)" — CORRECT
- `sections/H-balaban-analyticity.md:113` — cites "CMP 109, Theorem 1 (detailed: Theorem 3)" — CORRECT
- `PROOF-CHAIN.md:54,99` — cites "CMP 109, Sections 2–4" — sections are numbered, CORRECT

**Corrections applied:** Thm 2.1 → Thm 1 (fixed r09/r10)

---

### #3: Balaban, CMP 119, 243–285 (1988)

**Status:** LOCAL
**PDF:** `journals/balaban-CMP119-1988.pdf`
**Title page:** CMP 119, 243–285 (1988) — CONFIRMED (re-verified r12)
**Numbering:** Single UNNUMBERED theorem on p. 245
**Results verified:**
- "Theorem." (p. 245, unnumbered): "If ρ_k satisfies the assumptions described in detail in Sect. 2, then Tρ_k satisfies also the corresponding assumptions."

**Preprint references this paper at:**
- `sections/I-gap-closures.md:55` — "Theorem (unnumbered, p. 245)" — CORRECT
- `sections/05-continuum-limit.md:1352` — "Theorem (unnumbered, p. 245)" — CORRECT
- `sections/H-balaban-analyticity.md:113,335` — "Theorem (unnumbered, p. 245)" — CORRECT

**Corrections applied:** "Thm 1" → "Theorem (unnumbered, p. 245)" (4 occurrences, fixed r10)

---

### #4: Balaban, CMP 98, 17–51 (1985)

**Status:** LOCAL
**PDF:** `journals/balaban-CMP98-1985.pdf`
**Title page:** CMP 98, 17–51 (1985) — CONFIRMED
**Numbering:** Lettered sections A–F; no formally numbered theorems
**Results verified:**
- Sections A–F confirmed; "Sec. E" citation is correct

**Corrections applied:** Sec. 2 → Sec. E (fixed prior session); correct PDF URL identified (cmp/1103942283 not cmp/1103942535)

---

### #5: Dimock, arXiv:1108.1335 / Rev. Math. Phys. 25 (2013)

**Status:** LOCAL
**PDF:** `journals/dimock-arXiv1108.1335-2011.pdf`
**Title page:** arXiv:1108.1335 (2011); published Rev. Math. Phys. 25, 1330010 (2013) — CONFIRMED
**Numbering:** Plain theorem numbering
**Results verified:**
- Thm 14 (p. 23): main RG flow theorem for small-field contribution — CONFIRMED

**Preprint references this paper at:**
- `PROOF-CHAIN.md:62` — "arXiv:1108.1335, 2011, Thm 14" — CORRECT
- `sections/05-continuum-limit.md:1429,1716` — "Thm 14" — CORRECT
- `sections/H-balaban-analyticity.md:100,342` — "Thm 14" — CORRECT

**Corrections applied:** Thm 3.1 → Thm 14 (fixed prior session)

---

### #6: Fredenhagen-Marcu, CMP 92, 81–119 (1983)

**Status:** LOCAL
**PDF:** `journals/fredenhagen-marcu-CMP92-1983.pdf`
**Title page:** CMP 92, 81–119 (1983), "Charged States in Z₂ Gauge Theories" — CONFIRMED (re-verified r12)
**Numbering:** Numbered sections (1–7 + appendices); Proposition 2.1 (p. 85)
**Results verified:**
- Prop. 2.1 (p. 85): confinement/deconfinement criterion
- Paper is about Z₂ (discrete) gauge theory, NOT continuous SU(N)

**Preprint references this paper at:**
- `sections/04-lattice-proof-part1.md:746,1193` — cites "Fredenhagen-Marcu (1983)" — CORRECT
- `sections/F-area-law-mass-gap.md:127` — cites "Fredenhagen and Marcu (1983)" — CORRECT

**Corrections applied:** CMP 104 → CMP 92; year 1986 → 1983 (3 in-text occurrences, fixed r10)

---

### #7: Kotecky-Preiss, CMP 103, 491–498 (1986)

**Status:** LOCAL
**PDF:** `journals/kotecky-preiss-CMP103-1986.pdf`
**Title page:** CMP 103, 491–498 (1986) — CONFIRMED
**Numbering:** UNNUMBERED Theorem (p. 492) and Proposition (p. 494); paper is 8 pages
**Results verified:**
- "Theorem." (p. 492, unnumbered): convergence criterion for abstract polymer models
- "Proposition." (p. 494, unnumbered)

**Preprint references this paper at:**
- `sections/05-continuum-limit.md` — cites "Kotecky-Preiss (CMP 103, 1986)" — CORRECT
- All other mentions use abbreviated "Kotecky–Preiss cluster expansion" — acceptable

**Corrections applied:** Garbled duplicate "CMP 83, 1982" removed; residual "CMP 83, 1982" at 05-continuum-limit.md:1368 fixed to CMP 103, 1986 (r10)

---

### #8: Osterwalder-Schrader, CMP 31, 83–112 (1973)

**Status:** LOCAL
**PDF:** `journals/osterwalder-schrader-CMP31-1973.pdf`
**Title page:** CMP 31, 83–112 (1973) — CONFIRMED
**Numbering:** Axioms labeled (E0)–(E4)
**Results verified:**
- (E0) Temperedness, (E1) Covariance, (E2) Positivity, (E3) Symmetry, (E4) Cluster
- Modern relabeling OS1–OS5 in preprint is standard convention — CORRECT

**Corrections applied:** None

---

### #9: Osterwalder-Schrader, CMP 42, 281–305 (1975)

**Status:** LOCAL
**PDF:** `journals/osterwalder-schrader-CMP42-1975.pdf`
**Title page:** CMP 42, 281–305 (1975) — CONFIRMED
**Numbering:** Chapter-based; condition (E0') introduced in Chapter IV
**Results verified:**
- (E0') = "linear growth condition" (Chapter IV, p. 285) — this is the OS0' cited in preprint
- Theorem E↔R: (Ẽ0), E1–E4 ↔ Wightman axioms R0–R5 — CONFIRMED

**Corrections applied:** None; OS0' = (E0') in Ch. IV confirmed correct

---

### #10: Osterwalder-Seiler, Ann. Phys. 110, 440–471 (1978)

**Status:** WEB (ScienceDirect paywalled, no free PDF)
**Title confirmed:** "Gauge field theories on a lattice" — CONFIRMED via web
**Volume/pages/year:** 110, 440–471 (1978) — CONFIRMED

**Corrections applied:** None needed

---

### #11: Luscher, CMP 85, 39–48 (1982)

**Status:** LOCAL
**PDF:** `journals/luscher-CMP85-1982.pdf`
**Title page:** CMP 85, 39–48 (1982), "Topology of Lattice Gauge Fields" — CONFIRMED
**Numbering:** NO formally numbered theorems; results stated as properties (i)–(v) on p. 40; one unnumbered Lemma (p. 44)
**Results verified:**
- Properties (i)–(v) (p. 40): define topological charge Q_L on configurations with |1 − U(p̂)| < ε
- Smallness threshold: ε ≤ 0.03 for SU(2)

**Preprint references this paper at:**
- `sections/04-lattice-proof-part1.md:781` — "CMP 85, 1982, properties (i)--(v)" — CORRECT

**Corrections applied:** "Theorem 1" → "properties (i)--(v)" (r09/r10)

---

### #12: Chatterjee, arXiv:2104.05268 (2021)

**Status:** LOCAL (PDF on disk)
**PDF:** `journals/chatterjee-arXiv2104.05268-2021.pdf`
**Note:** NOT cited in preprint body. Orphan entry in ledger. Kept for context.

**Corrections applied:** None

---

## Phase 4: Error Detection Summary

### Author errors (NEW — found in r12)

**Error 13 — Wrong authors for arXiv:1511.01908:**
- Preprint claimed: "Dubovsky, Gorbenko, Mirbabayi (2016)"
- Actual authors: Dubovsky, S. and Gorbenko, V. (2-author paper)
- Published: JHEP 02 (2016) 022
- Locations: I-luscher-test.md:17, :19, :210
- **Fixed:** All three occurrences corrected

**Error 14 — Wrong authors for arXiv:2310.20698:**
- Preprint claimed: "Dubovsky, Gorbenko (2024)"
- Actual authors: Gaikwad, A., Gorbenko, V., Guerrieri, A.L. (3-author paper)
- Published: JHEP 01 (2024) 090
- Location: I-luscher-test.md:20
- **Fixed:** Corrected to "Gaikwad, Gorbenko, Guerrieri (2024)"

**Error 15 — Abbreviated authors for arXiv:2411.03435:**
- Preprint used shorthand "Athenodorou-Teper 2024" for a 4-author paper
- Actual authors: Athenodorou, A., Dubovsky, S., Luo, C., Teper, M.
- Location: I-luscher-test.md:211 (updated); other occurrences use shorthand which is tolerable in informal references
- **Fixed:** Line 211 (formal attribution) expanded to full 4 authors

### Previously fixed errors (confirmed still correct)

- CMP 95: No regression on Prop. 3.2 — CLEAN
- CMP 109: No regression on Thm 2.1 — CLEAN
- CMP 98: No regression on "Sec. 2" — CLEAN
- CMP 119: No regression on "Thm 1" — all cite "Theorem (unnumbered, p. 245)" — CLEAN
- Fredenhagen-Marcu: No regression on 1986/CMP 104 — CLEAN
- Kotecky-Preiss: No regression on "CMP 83, 1982" — CLEAN
- Lüscher CMP 85: No "Theorem 1" citation remains — CLEAN

---

## Summary

| # | Citation | Status | Errors found | Errors fixed |
|:--|:---------|:-------|:-------------|:-------------|
| 1 | Balaban, CMP 95 (1984) | LOCAL | 0 (was fixed r09) | 0 |
| 2 | Balaban, CMP 109 (1987) | LOCAL | 0 (was fixed r09) | 0 |
| 3 | Balaban, CMP 119 (1988) | LOCAL | 0 (was fixed r10) | 0 |
| 4 | Balaban, CMP 98 (1985) | LOCAL | 0 (was fixed) | 0 |
| 5 | Dimock, arXiv:1108.1335 (2013a) | LOCAL | 0 (was fixed) | 0 |
| 6 | Fredenhagen-Marcu, CMP 92 (1983) | LOCAL | 0 (was fixed r10) | 0 |
| 7 | Kotecky-Preiss, CMP 103 (1986) | LOCAL | 0 (was fixed r10) | 0 |
| 8 | Osterwalder-Schrader, CMP 31 (1973) | LOCAL | 0 | 0 |
| 9 | Osterwalder-Schrader, CMP 42 (1975) | LOCAL | 0 | 0 |
| 10 | Osterwalder-Seiler, Ann. Phys. 110 (1978) | WEB | 0 | 0 |
| 11 | Luscher, CMP 85 (1982) | LOCAL | 0 (was fixed r10) | 0 |
| 12 | Chatterjee, arXiv:2104.05268 (2021) | LOCAL | — (orphan) | — |
| 13 | Dubovsky, Gorbenko (2016) | WEB | 1 (wrong authors — Mirbabayi added) | 1 |
| 14 | Gaikwad, Gorbenko, Guerrieri (2024) | WEB | 1 (wrong authors — Dubovsky instead of Gaikwad+Guerrieri) | 1 |
| 15 | Athenodorou, Dubovsky, Luo, Teper (2024) | WEB | 1 (abbreviated to 2 authors) | 1 |
| 16 | Athenodorou, Caristo, Caselle (2024) | WEB | 0 (added) | — |
| 17 | Weisz, Wohlert (1984) | WEB | 0 (added) | — |
| 18 | Nachtergaele, Sims (2006) | WEB | 0 (added) | — |
| 19 | Helgason (1978) | WEB | 0 (added) | — |
| 20 | Besse (1987) | WEB | 0 (added) | — |
| 21 | Borel (1953) | WEB | 0 (added) | — |
| 22 | Dimock (2013b) | WEB | 0 (added) | — |

**Total citations tracked:** 22 (12 prior + 10 new)
**Total LOCAL:** 11
**Total WEB:** 11 (includes 1 paywalled, 10 confirmed via web)
**Total errors found this session:** 3 (author attribution errors in I-luscher-test.md)
**Total errors fixed this session:** 3
**Missing references added this session:** 10
**Remaining WEB papers to download if desired:** arXiv:2411.03435, arXiv:2411.16507, arXiv:1511.01908, arXiv:2310.20698 (all freely available on arXiv); Weisz-Wohlert (paywalled); Nachtergaele-Sims (paywalled); Helgason, Besse, Borel (books)

**No proof-critical citation errors remain unfixed.**
