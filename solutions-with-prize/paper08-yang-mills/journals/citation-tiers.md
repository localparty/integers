# Citation Verification Ledger

Status key:
- **LOCAL** — full text saved in `journals/`, theorem numbers verified against source
- **WEB** — verified via web search (title, volume, year confirmed), no local copy
- **UNVERIFIED** — cited but not yet checked against source

## Core proof-chain citations

| # | Citation | Status | Local file | Corrections applied |
|:--|:---------|:-------|:-----------|:--------------------|
| 13 | Dubovsky, Gorbenko, JHEP 02 (2016) 022 | **WEB** | — | Authors corrected (was Mirbabayi 3rd author) |
| 14 | Gaikwad, Gorbenko, Guerrieri, JHEP 01 (2024) 090 | **WEB** | — | Authors corrected (was Dubovsky, Gorbenko) |
| 15 | Athenodorou, Dubovsky, Luo, Teper, arXiv:2411.03435 (2024) | **WEB** | — | Added (was "Athenodorou-Teper") |
| 16 | Athenodorou, Caristo, Caselle, PoS(LATTICE2024)393 | **WEB** | — | Added |
| 17 | Weisz, Wohlert, Nucl. Phys. B 236 (1984) 397-422 | **WEB** | — | Added |
| 18 | Nachtergaele, Sims, CMP 265 (2006) 119-130 | **LOCAL** | `nachtergaele-sims-CMP265-2006.pdf` | Thm 2.1 → Theorem 2 (plain numbering) |
| 19 | Helgason (1978), Academic Press | **WEB** | — | Added |
| 20 | Besse (1987), Springer | **WEB** | — | Added |
| 21 | Borel, Ann. Math. 57 (1953) 115-207 | **WEB** | — | Added |
| 22 | Dimock (2013b), J. Math. Phys. 54, 092301 | **WEB** | — | Added |
| 23 | Friedli, Velenik, Cambridge (2017) | **WEB** | — | Added; Thm 5.4 confirmed (cluster expansion convergence) |
| 24 | Krantz, Parks, Birkhäuser (2002) | **WEB** | — | Added; Thm 1.1.5 cited (identity theorem for analytic functions) |
| 25 | Billingsley, Wiley (1999) | **WEB** | — | Added; Thm 2.1 cited (Portmanteau theorem) |
| 26 | Kallenberg, Springer (2002) | **WEB** | — | Added; Lemma 4.3 cited (weak convergence) |
| 1 | Balaban, CMP 95, 17-40 (1984) | **LOCAL** | `balaban-CMP95-1984.pdf` | Prop. 3.2 -> Prop. 1.2 (p. 35) |
| 2 | Balaban, CMP 109, 249-301 (1987) | **LOCAL** | `balaban-CMP109-1987.pdf` | Thm 2.1 -> Thm 1 (detailed: Thm 3) |
| 3 | Balaban, CMP 119, 243-285 (1988) | **LOCAL** | `balaban-CMP119-1988.pdf` | Thm (unnumbered, p. 245) confirmed |
| 4 | Balaban, CMP 98, 17-51 (1985) | **LOCAL** | `balaban-CMP98-1985.pdf` | Sec. 2 -> Sec. E; correct URL: cmp/1103942283 (Issue 1, pp. 17-51) |
| 5 | Dimock, arXiv:1108.1335 / RMP 25 (2013) | **LOCAL** | `dimock-arXiv1108.1335-2011.pdf` | Thm 3.1 -> Thm 14 |
| 6 | Fredenhagen-Marcu, CMP 92, 81-119 (1983) | **LOCAL** | `fredenhagen-marcu-CMP92-1983.pdf` | CMP 104 -> CMP 92; 1986 -> 1983 |
| 7 | Kotecky-Preiss, CMP 103, 491-498 (1986) | **LOCAL** | `kotecky-preiss-CMP103-1986.pdf` | Removed garbled duplicate (was "CMP 83, 1982") |
| 8 | Osterwalder-Schrader, CMP 31, 83-112 (1973) | **LOCAL** | `osterwalder-schrader-CMP31-1973.pdf` | (none needed) |
| 9 | Osterwalder-Schrader, CMP 42, 281-305 (1975) | **LOCAL** | `osterwalder-schrader-CMP42-1975.pdf` | OS0' = (E0') in Ch. IV confirmed |
| 10 | Osterwalder-Seiler, Ann. Phys. 110, 440-471 (1978) | **WEB** | — | (none needed); ScienceDirect paywalled |
| 11 | Luscher, CMP 85, 39-48 (1982) | **LOCAL** | `luscher-CMP85-1982.pdf` | "Theorem 1" -> "properties (i)--(v)"; paper has NO numbered theorems |
| 12 | Chatterjee, arXiv:2104.05268 / CMP (2021) | **LOCAL** | `chatterjee-arXiv2104.05268-2021.pdf` | (none needed; not in references.md) |

## Download URLs

### Already LOCAL (6 papers)

These are saved in `journals/`. No action needed.

### Pending download (6 papers)

Project Euclid (free access, bot detection may require browser):

```
# 3. Balaban CMP 119 (1988)
curl -o journals/balaban-CMP119-1988.pdf \
  "https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-119/issue-2/Convergent-renormalization-expansions-for-lattice-gauge-theories/cmp/1104162401.pdf"

# 4. Balaban CMP 98 (1985)
curl -o journals/balaban-CMP98-1985.pdf \
  "https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-98/issue-1/Averaging-operations-for-lattice-gauge-theories/cmp/1103942535.pdf"

# 6. Fredenhagen-Marcu CMP 92 (1983)
curl -o journals/fredenhagen-marcu-CMP92-1983.pdf \
  "https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-92/issue-1/Charged-states-in-Z_2-gauge-theories/cmp/1103940736.pdf"

# 9. Osterwalder-Schrader CMP 42 (1975)
curl -o journals/osterwalder-schrader-CMP42-1975.pdf \
  "https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf"

# 11. Luscher CMP 85 (1982)
curl -o journals/luscher-CMP85-1982.pdf \
  "https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-85/issue-1/Topology-of-lattice-gauge-fields/cmp/1103921338.pdf"
```

ScienceDirect (requires institutional access):

```
# 10. Osterwalder-Seiler, Ann. Phys. 110 (1978)
# DOI: https://doi.org/10.1016/0003-4916(78)90039-8
# Direct: https://www.sciencedirect.com/science/article/pii/0003491678900398
# No free PDF available — requires institutional login or purchase
```

### Springer DOI links (paywalled, for institutional access)

| # | DOI link |
|:--|:---------|
| 3 | https://doi.org/10.1007/BF01217741 |
| 4 | https://doi.org/10.1007/BF01211042 |
| 6 | https://doi.org/10.1007/BF01206315 |
| 9 | https://doi.org/10.1007/BF01608978 |
| 10 | https://doi.org/10.1016/0003-4916(78)90039-8 |
| 11 | https://doi.org/10.1007/BF02029132 |

## Key findings from verified papers

**CMP 95 (Balaban 1984):**
- Paper uses lettered sections (A-F) and part-based numbering (Prop. 1.1, 1.2)
- Prop. 1.1 (p. 33): boundedness of G with gamma_0 independent of k
- Prop. 1.2 (p. 35): exponential decay |G(x,y)| <= O(1)e^{-delta_0|x-y|}
- Only 2 propositions in entire paper; no "Prop. 3.2" exists

**CMP 109 (Balaban 1987):**
- Paper uses numbered sections (0-5) and plain theorem numbering
- Thm 1 (p. 259): UV stability — polymer weights satisfy |E^(j)(X)| <= E_0 exp(-kappa d_j(X))
- Thm 2 (p. 259): running coupling trajectory for SU(2)
- Thm 3 (p. 264): detailed version of Thm 1 with all inductive constants
- Key bound (1.18): kappa independent of k — CONFIRMED

**Kotecky-Preiss (1986):**
- Main result labeled "Theorem." (UNNUMBERED, p. 492)
- Also has "Proposition." (unnumbered, p. 494)
- Convergence criterion: sum_{gamma': gamma' incompatible gamma} e^{a(gamma')+d(gamma')} |Phi(gamma')| <= a(gamma)
- Paper is only 8 pages

**Osterwalder-Schrader (1973):**
- OS axioms labeled (E0)-(E4): Temperedness, Covariance, Positivity, Symmetry, Cluster
- Modern convention OS1-OS5 used in the preprint is standard relabeling
- Paper structure: 8 sections, main theorems in Section 3 ("E -> R" and "R -> E")
- 1975 Part II corrects regularity condition (E0) to (E0') — this is the OS0' referenced in the preprint

**Fredenhagen-Marcu:**
- Actual paper: CMP 92, 81-119 (1983), NOT CMP 104 (1986)
- The 1986 date likely confused with their PRL 56, 223 (1986) paper

**CMP 119 (Balaban 1988):**
- Title: "Convergent Renormalization Expansions for Lattice Gauge Theories"
- Main result on p. 245: single UNNUMBERED "Theorem." — "If ρ_k satisfies the assumptions described in Sect. 2, then Tρ_k satisfies also the corresponding assumptions."
- Extends CMP 109 to include large-field domains
- References CMP 109 as "[I]" and CMP 116 as "[II]" internally

**Fredenhagen-Marcu (1983):**
- Title: "Charged States in Z₂ Gauge Theories" — CMP 92, 81-119 (1983) CONFIRMED
- Uses section-based numbering: Proposition 2.1 (p. 85)
- Paper is about Z₂ (discrete) gauge theory, not continuous SU(N)
- The confinement/deconfinement criterion is developed here

**Osterwalder-Schrader (1975):**
- Title: "Axioms for Euclidean Green's Functions II" — CMP 42, 281-305 (1975) CONFIRMED
- Corrects Lemma 8.8 from OS I (p. 282, Remark 2 — "the lemma is wrong")
- New condition (E0') = "linear growth condition" introduced in Chapter IV
- Theorem E↔R (revisited, p. 285): (Ẽ0), E1-E4 ↔ Wightman axioms R0-R5
- This is exactly the OS0' condition the preprint uses — CONFIRMED


**Nachtergaele-Sims (2006):**
- Title: "Lieb-Robinson Bounds and the Exponential Clustering Theorem" — CMP 265, 119-130 CONFIRMED
- Plain numbering: Theorem 1 (Lieb-Robinson bound), Theorem 2 (exponential clustering / decay of correlations)
- No section-based numbering; "Thm 2.1" in preprint was WRONG — corrected to "Theorem 2"
- Theorem 2 = exponential clustering: for gapped lattice Hamiltonian, spatial correlations decay exponentially
- Revision history confirms: "corrected proof of Theorem 2" (v2), "slightly better bound in Theorem 2" (v3)

**Friedli-Velenik (2017):**
- Title: "Statistical Mechanics of Lattice Systems" — Cambridge University Press 2017 CONFIRMED
- Chapter 5 = Cluster Expansion; Theorem 5.4 = Kotecky-Preiss abstract polymer convergence criterion
- Statement (p. 224): given ∑_γ |w(γ)|e^{a(γ)}|ζ(γ,γ*)| ≤ a(γ*), the cluster expansion converges
- This is exactly the abstract form of the criterion used in the preprint — CONFIRMED CORRECT

**CMP 98 (Balaban 1985):**
- Title: "Averaging Operations for Lattice Gauge Theories" — CMP 98, 17-51 (1985) CONFIRMED
- Downloaded from: https://projecteuclid.org/.../cmp/1103942283.pdf (correct URL; prior URL cmp/1103942535 gave wrong issue)
- Sections: Lettered A-F (confirms Sec. E citation is correct)
- Main result: averaging operations are analytic on regular gauge field configurations
- No formally numbered theorems; results stated as properties and lemmas in lettered sections
- Osterwalder-Seiler cited in its references (confirmed connection)

**Lüscher (1982):**
- Title: "Topology of Lattice Gauge Fields" — CMP 85, 39-48 (1982) CONFIRMED
- Paper has NO formally numbered theorems
- Main result stated as properties (i)-(v) on p. 40
- One unnumbered Lemma (p. 44: cocycle condition)
- Smallness condition: Tr{1 - U(p̂)} < ε with ε ≤ 0.03 for SU(2) (footnote: "not optimal")
- Preprint cited "Theorem 1" — CORRECTED to "properties (i)--(v)"

## Corrections applied (total: 22)

1. CMP 95: Prop. 3.2 -> Prop. 1.2 (in 05-continuum-limit.md, PROOF-CHAIN.md)
2. CMP 109: Thm 2.1 -> Thm 1 (in multiple files; applied in prior session)
3. CMP 98: Sec. 2 -> Sec. E (applied in prior session)
4. Dimock: Thm 3.1 -> Thm 14 (applied in prior session)
5. Fredenhagen-Marcu: CMP 104 (1986) -> CMP 92 (1983) (in 04-lattice-proof-part1.md, references.md)
6. Fredenhagen-Marcu: year 1986 -> 1983 (in references.md)
7. Duplicate Kotecky-Preiss entry: removed "CMP 83 (1982), 493-515" (garbled duplicate of CMP 103, 1986)
8. Lüscher CMP 85: "Theorem 1" -> "properties (i)--(v)" (paper has no numbered theorems)
9. Kotecky-Preiss: "CMP 83, 1982" -> "CMP 103, 1986" (in 05-continuum-limit.md:1368; garbled ref survived prior fix)
10. Fredenhagen-Marcu: year 1986 -> 1983 in three in-text citations (04-lattice-proof-part1.md:746, :1193; F-area-law-mass-gap.md:127)
11. CMP 119: "Thm 1" -> "Theorem (unnumbered, p. 245)" in four places (05-continuum-limit.md:1352; H-balaban-analyticity.md:113, :335; I-gap-closures.md:55)
12. references.md: removed duplicate Kotecky-Preiss correction note; fleshed out Balaban series and Dimock entries; added missing refs (Symanzik 1983, Lüscher-Weisz 1985, Lüscher 1977, Necco-Sommer 2002, Prasad-Sommerfield 1975)
13. I-luscher-test.md:17,19,210: "Dubovsky-Gorbenko-Mirbabayi (2016)" → "Dubovsky-Gorbenko (2016)"; arXiv:1511.01908 is 2-author (Dubovsky, Gorbenko), no Mirbabayi
14. I-luscher-test.md:20: "Dubovsky, Gorbenko 2024" → "Gaikwad, Gorbenko, Guerrieri 2024" for arXiv:2310.20698
15. I-luscher-test.md:211: "Athenodorou and Teper (2024)" expanded to "Athenodorou, Dubovsky, Luo, and Teper (2024)" (arXiv:2411.03435 is 4-author)
16. references.md: added 10 missing entries (Dubovsky-Gorbenko 2016; Gaikwad-Gorbenko-Guerrieri 2024; Athenodorou-Dubovsky-Luo-Teper 2024; Athenodorou-Caristo-Caselle 2024; Weisz-Wohlert 1984; Nachtergaele-Sims 2006; Helgason 1978; Besse 1987; Borel 1953; Dimock 2013b)
17. references.md: Lüscher-Weisz 1985 entry updated to include Erratum (CMP 98, 433); Weisz-Wohlert entry includes its erratum (Nucl. Phys. B 247, 544)
18. 05-continuum-limit.md:1152: "Nachtergaele-Sims 2006, Thm 2.1" → "Theorem 2" (paper uses plain numbering: Theorem 1=Lieb-Robinson, Theorem 2=exponential clustering; no section-based "2.1" exists)
19. I4-other-gauge-groups.md:53: "Besse 1987, Theorem 7.73" → "Theorem 7.73 and Corollary 7.74" (Thm 7.73 = Ricci formula r=−B|p; Corollary 7.74 = Einstein property; both needed for the claim)
20. references.md: Added Friedli-Velenik 2017 (missing entry; cited at 04:1001 as Thm 5.4, confirmed correct)
21. references.md: Added Krantz-Parks 2002 (missing entry; cited at 05:1536 and H:349 as Thm 1.1.5)
22. references.md: Added Billingsley 1999 and Kallenberg 2002 (missing entries; cited at 05:2145 as Thm 2.1 and Lemma 4.3)

## Verification log

**2026-04-06, r09 session:**
- Fetched CMP 95 via Project Euclid PDF. Prop. 1.1/1.2 verified. No Prop. 3.2. Fixed.
- Fetched CMP 109 via Project Euclid PDF. Thm 1, 2, 3 confirmed (plain numbering).
- Fetched Kotecky-Preiss CMP 103 via Project Euclid PDF. Unnumbered Theorem verified.
- Fetched Osterwalder-Schrader CMP 31 via Project Euclid PDF. Axioms (E0)-(E4) confirmed.
- Fetched Dimock via arXiv PDF. Thm 14 confirmed.
- Fetched Chatterjee via arXiv PDF.
- Fredenhagen-Marcu verified via web: CMP 92 (1983), not CMP 104 (1986). Fixed.
- CMP 119 confirmed via INSPIRE (record #270214) and Project Euclid search.
- CMP 98, Dimock corrections from prior sessions confirmed.
- Osterwalder-Schrader CMP 42 (1975) confirmed via Springer.
- Osterwalder-Seiler Ann. Phys. 110 (1978) confirmed via ScienceDirect.
- Luscher CMP 85, 39-48 (1982) confirmed via Project Euclid and Springer.
- Chatterjee (2021) confirmed via web search (probabilistic mechanism for quark confinement).
- Garbled duplicate reference (Kotecky-Preiss "CMP 83, 1982") identified and removed.
- Remaining 6 papers: Project Euclid bot detection triggered; curl commands and DOIs recorded for manual download.

**2026-04-06, r10 session (citation-verifier run):**
- Full inventory of all in-text citations vs references.md completed.
- Found residual garbled ref: "Kotecky--Preiss (CMP 83, 1982)" in 05-continuum-limit.md:1368. Fixed to CMP 103, 1986.
- Found 3 residual Fredenhagen-Marcu "(1986)" in body (04-lattice-proof-part1.md:746, :1193; F-area-law-mass-gap.md:127). Fixed to (1983).
- Found 4 instances of "CMP 119, Thm 1" — paper has UNNUMBERED theorem (p. 245). Fixed in 05-continuum-limit.md, H-balaban-analyticity.md, I-gap-closures.md.
- Verified Dimock Thm 14 (p. 23): main RG flow theorem, correctly cited.
- Verified CMP 95 Prop. 1.1 (p. 33) and Prop. 1.2 (p. 35): exponential decay confirmed.
- Verified Fredenhagen-Marcu Prop. 2.1 (p. 85): section-based numbering, Z₂ gauge theory.
- Verified Kotecky-Preiss: unnumbered Theorem (p. 492), unnumbered Proposition (p. 494).
- CMP 119 unnumbered Theorem (p. 245): re-confirmed from PDF.
- Added 5 missing references to references.md: Symanzik (1983), Lüscher-Weisz (1985), Lüscher (1977), Necco-Sommer (2002), Prasad-Sommerfield (1975).
- Fleshed out Balaban series entries (individual papers CMP 95, 96, 98, 102, 109, 119) and Dimock entry in references.md.
- Removed duplicate Kotecky-Preiss correction note from references.md.
- Attempted CMP 98 download: Project Euclid returned HTML (bot detection). Metadata confirmed via INSPIRE API.
- Osterwalder-Seiler remains paywalled (ScienceDirect). Metadata confirmed in prior session.
- Chatterjee (2021): LOCAL in ledger but NOT cited in preprint body. Orphan in ledger — kept for context.

**2026-04-06, r12 session (full audit):**
- Fredenhagen-Marcu CMP 92 (1983) PDF re-confirmed: "Charged States in Z₂ Gauge Theories," pp. 81-119, Klaus Fredenhagen and Mihail Marcu. Uses numbered sections. ✓
- Balaban CMP 119 (1988) PDF re-confirmed: "Convergent Renormalization Expansions for Lattice Gauge Theories," pp. 243-285, T. Balaban. Unnumbered Theorem on p. 245 confirmed. ✓
- Complete cross-reference of all body files vs references.md completed.
- Found 4 new author errors in I-luscher-test.md: Mirbabayi incorrectly added to arXiv:1511.01908 (2-author paper); arXiv:2310.20698 wrongly attributed to Dubovsky-Gorbenko (actually Gaikwad-Gorbenko-Guerrieri). Fixed.
- Athenodorou-Teper 2024 identified as arXiv:2411.03435 (4 authors: Athenodorou, Dubovsky, Luo, Teper). Citation in body expanded from 2-author shorthand to full 4 authors.
- Found 10 missing references and added all to references.md.
- New section "Flux-Tube Spectrum and Effective String Theory" added to references.md.
- Orphan in ledger: Chatterjee (2021) still not cited in body — kept for context.

**2026-04-07, r13 session (full audit of new appendices):**
- Full inventory of all body files completed, including new appendices I3, I4, K, J not audited in prior sessions.
- Nachtergaele-Sims CMP 265 (2006) PDF downloaded via arXiv (math-ph/0506030). Confirmed plain numbering: Theorem 1 (Lieb-Robinson bound), Theorem 2 (exponential clustering). No Theorem 2.1 exists. Fixed "Thm 2.1" → "Theorem 2" in 05-continuum-limit.md:1152.
- Besse 1987, Theorem 7.73 citation (I4:53) corrected: Thm 7.73 = Ricci formula only; Einstein property is Corollary 7.74. Citation updated to "Theorem 7.73 and Corollary 7.74."
- Found 4 missing references not in references.md: Friedli-Velenik 2017, Krantz-Parks 2002, Billingsley 1999, Kallenberg 2002. All added.
- Friedli-Velenik Theorem 5.4 verified from PDF: confirmed as the Kotecky-Preiss abstract polymer convergence theorem (Section 5.4, page 224 of chapter). Citation correct.
- K-balaban-general-groups.md: all citations verified (CMP 119 Section 2 confirmed; CMP 109 Thm 1/3 correct; Kotecky-Preiss unnumbered).
- J-lattice-symanzik-basis.md: inline references [1]–[3] match references.md metadata for Symanzik, Lüscher-Weisz, Weisz-Wohlert ✓.
- Glimm-Jaffe Theorems 18.2.1, 19.1.1 and Seiler 1982 Theorem 6.1: plausible but unverifiable without book access. Flagged WEB.
- Krantz-Parks Thm 1.1.5 and Billingsley Thm 2.1 and Kallenberg Lemma 4.3: plausible, unverifiable without book access. Flagged WEB.
- PROOF-CHAIN.md: all citations verified in prior sessions; no new issues.

**2026-04-06, r11 session (manual download):**
- CMP 98 successfully downloaded from Project Euclid using correct URL (cmp/1103942283, not cmp/1103942535).
- Verified: Volume 98, Issue 1, pp. 17-51, "Averaging Operations for Lattice Gauge Theories," T. Balaban.
- Lettered sections A-F confirmed. No formally numbered theorems.
- Status updated from WEB to LOCAL.
- Osterwalder-Seiler Ann. Phys. 110 (1978): definitively paywalled (ScienceDirect only). Metadata confirmed from multiple secondary sources. No free PDF found. Remains WEB.
