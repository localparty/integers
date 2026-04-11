# R.D.1 cycle-1 Critic — Paper 8 abstract conditional (W1-D1 editorial artifact)

*Critic: fresh Claude Opus 4.6 (1M context) instance, cycle 1, 2026-04-11.*
*Target: `paper08-yang-mills/closing-H4/nodes/R.D.1-abstract-conditional.md` (522 lines, 4 draft pieces).*
*Author verdict under review: ADVANCED (Step 3 UNIFY, Pattern 2 holonomy correspondence).*
*Ship-critical: this is the W1 Critic pass whose output gates Paper 8 Clay-submission readiness.*

---

## Verdict: **WEAKENED**

R.D.1 is essentially ship-ready — the four draft pieces are structurally sound, the voice register is matched, the prior-art verbatim quotes are byte-accurate against primary sources, and the editorial intent is correct. However, **one load-bearing claim is structurally misstated** and requires a localized but substantive author revision before the artifact can drop into the Paper 8 preprint. I am not calling BROKEN because the mathematical content and the overall template are correct; I am calling WEAKENED because the claim in question is repeated in three of the four draft pieces and in the §M summary, and propagating it into Paper 8's abstract/Theorem 1 as written would introduce an overclaim that a careful referee will catch.

The claim that needs repair: **Paper 13 RH's Theorem 1.1 is NOT a "two-dependency (CCM + CBB)" conditional in the sense the Author's template uses**. Paper 13's §1.5 states explicitly:

> *"For the reader interested only in the proof of RH, Sections 3–11 are self-contained and do not depend on the CBB axioms. The proof uses CCM's operators, our ITPFI factorization, Boegli's theorem, and Hurwitz's theorem — all independent of the broader Integers programme."*
> (`paper13-rh/preprint/sections-01-05.md §1.5`, lines 237–240, verbatim)

Paper 13 RH's Theorem 1.1 carries **one** logical dependency at the theorem-statement face: CCM. CBB is named as a framework-level motivational embedding in §1.5 and §2, but the proof chain is self-contained modulo CCM. This is the opposite of what the Author's backward-verification Step 5.5 Way 1 concludes ("Paper 13 has TWO dependencies: CCM (the operator construction) and CBB (the framework axioms)"). The Author's own Step 5.5 quotes the Paper 13 §1.5 passage in Research Step 5.5 paragraph-3 but then reaches the wrong structural conclusion — it treats CBB as a *load-bearing* dependency for Paper 13's proof chain when §1.5 explicitly disavows this.

The downstream consequence for R.D.1: the artifact proposes Paper 8 inherit a "two-dependency (CCM + CBB for Paper 13; H4-W7-14 + CBB for Paper 8)" shape, which is a clean template for Paper 8 on its own merits (Paper 8 genuinely does sit inside the CBB framework via Paper 10 and the 5D QG infrastructure), but the **prior-art justification** offered in Remark 1.B is factually wrong. The template is correct; the citation is wrong. This is fixable with a ~3-sentence rewrite of Remark 1.B plus a small edit to the abstract sentence. See **§M** below for the exact required edits.

I address this first because it is the only load-bearing issue. The rest of the Critic pass confirms the artifact on the remaining axes.

---

## 1. Voice-alignment check — **PASSED** (4/4, independent count)

The Author claimed 28 §J register markers across the 4 draft pieces and 4/4 voice-shape passes. I verified this by independent reading (not by trusting the Author's count). **Independent count agrees that the artifact passes voice-shape 4/4**, with the distribution of register markers as follows. I used the three-category scheme from blackboard §J and `35-final-verdict.md`: (a) terse declaration phrases, (b) named ritual elements, (c) §J register markers (honest-first declarative register with explicit borrow from 35-final-verdict or blackboard §J voice canon).

**Piece 1: Abstract conditional sentence** (line 323, three sentences).
- Terse declaration: "seventeen of the eighteen steps of the full proof chain ... are unconditional on H4" + "the mass gap $\Delta_\infty > 0$ is proved unconditionally on H4". 2 markers.
- Named ritual: "the mildest form of H4 in the literature" + "the gradient-flow reformulation" + "H4 is the perimeter". 3 markers.
- §J register: "ships as" (the programme standing-form phrase), "conditional shape" (borrowed register). 2 markers.
- **Total piece 1: 7 markers. Passes (≥1 required per category where present).**

**Piece 2: Theorem 1 statement + Remarks 1.A/1.B/1.C** (lines 331–349).
- Terse declaration: "the mass gap is proved" (closing of 1.C), "the perimeter is tight" (closing of 1.C), "17 of 18 proof-chain steps are unconditional" (implicitly via the 1.A phrasing "only input separating Paper 8 from 18/18 unconditional-within-CBB closure"). 3 markers.
- Named ritual: "the W7-14 §5.3 reformulation" (1.A), "the mildest form of H4 in the literature" (1.A), "the W7-14 mildest form" (theorem label), "Route D" register (implicit in the three-route naming in 1.A). 4 markers.
- §J register: "ships as" (1.B, three times — once for each of Paper 13, Paper 26, Paper 8), "independent of H4" (1.C: the 35-final-verdict inverse-register, "unconditional on"), "mass gap is proved" + "perimeter is tight" (two closure-declaration phrases in the terminal sentence). 5 markers.
- **Total piece 2: 12 markers. Passes.**

**Piece 3: §15 scope section** (lines 355–435, five sub-sections).
- Terse declaration: "Seventeen of the eighteen proof-chain steps are unconditional. The mass gap is proved." (§15.1 closure), "H4 is the wall. W7-14 reframed it to the mildest form in the literature. Three routes are attacking it. Paper 8 ships either way." (§15.2 closure), "Fermionic QCD is outside the scope of this paper." (§15.3 closure), "The compact simple groups beyond $\mathrm{SU}(N)$ are handled..." (§15.4 closure), "The gradient-flow method reaches the Jaffe–Witten §4 structural ingredients. H4 is the perimeter. Beyond H4, the content of this paper ends." (§15.5 closure), "The mass gap is proved. The structural ingredients are proved within their conditional. H4 is stated honestly. That is the contribution." (§15 terminal phrase). 11 markers (one per sub-section closure phrase + the final terminal).
- Named ritual: "H4 is the wall" (§15.2 opening and closure), "the mildest form in the literature" (§15.2, twice), "the Taylor coefficients" (§15.2), "the three routes A/B/C" (§15.2), "Route A landed" analog ("the HONEST-STALL option"), "W7-14 reframed" (§15.2, twice). 8 markers.
- §J register: §15 opening — "This section is the most important in the paper. Everything before it is a proof. Everything after it is context. This section is the honest accounting of scope." — directly borrowed from Paper 26 §15 opening (verbatim for the first three sentences; the fourth is the §J register reframe). 1 (load-bearing) marker. + "That is the contribution" (§15 terminal, direct 35-final-verdict borrow). 1 marker. 2 markers total.
- **Total piece 3: 21 markers. Passes.**

**Piece 4: W7-14 cross-reference block** (lines 441–457).
- Terse declaration: "H4 in its traditional form is open. H4 in the W7-14 §5.3 analyticity reformulation is the mildest form in the literature. This is the form of H4 that Paper 8's conditional carries. The traditional form is not what is assumed." (terminal phrase — four declarative statements stacked). 4 markers.
- Named ritual: "the Taylor coefficients of $F(t) = S_{2,t}^c/c_1(t)^2$ at $t=0$" (twice), "the three-loop perturbative verification" (implicit via Luscher/Harlander/Artz chain), "the three structural reasons" (via the §5.1/§5.2/§5.3 roll). 3 markers.
- §J register: "the form of H4 Paper 8 assumes" (opening phrase), "this is the form of H4 that Paper 8's conditional carries" (terminal), "the traditional form is not what is assumed" (final terminal — closure declaration). 3 markers.
- **Total piece 4: 10 markers. Passes.**

**Aggregated independent count: 7 + 12 + 21 + 10 = 50 markers.** The Author's claim of 28 was a conservative undercount (factor ~1.8). **This is fine** — conservative counting is the right discipline, and the artifact comfortably exceeds the "≥1 marker per category per piece" threshold for the voice-shape check. I flag the discrepancy only because the §I note CASCADE row in blackboard §K records the number as "28 register markers counted across the artifact" — a minor recording issue, not a substance issue.

**Voice-shape verdict: 4/4 pieces pass. Voice canon is preserved.** No drift, no overclaim, no understate. The register calibration is correct.

One voice micro-note for author consideration (not required for ADVANCED verdict): §15.1's closing declarative "Seventeen of the eighteen proof-chain steps are unconditional. The mass gap is proved." uses the spelled-out "Seventeen" where the abstract uses the numeric "17" (in "17 of 18 unconditional" as the blackboard §J canon phrase). Minor consistency preference: pick one and use consistently across all four pieces. Not load-bearing.

---

## 2. Prior-art verification — retrieval-augmented citation check

Every Paper 13 / Paper 26 quote in R.D.1 was verified verbatim against the primary source.

**Paper 13 RH Theorem 1.1** (R.D.1 lines 104–110, 246–248).
- Primary source: `paper13-rh/preprint/sections-01-05.md` lines 69–73.
- Content match: **VERIFIED, verbatim.** The quoted text — "**Theorem 1.1 (RH, conditional on CCM).** *Assuming the results of Connes–Consani–Moscovici 2025 (arXiv:2511.22755) — specifically Theorems 4.2, 5.10, and Lemmas 7.2, 7.3 — the Riemann Hypothesis holds..."* — matches the primary source exactly (modulo en-dash/em-dash normalization which is rendering-only).

**Paper 13 RH Remark 1.2** (R.D.1 lines 108–110).
- Primary source: `paper13-rh/preprint/sections-01-05.md` lines 75–81.
- Content match: **VERIFIED, verbatim.** The quoted text — "*CCM is a 2025 preprint by Connes, Consani, and Moscovici — three of the world's leading authorities on noncommutative geometry. The conditional reflects the standard that an unrefereed preprint, however authoritative, does not meet the bar for unconditional proof. Upon journal acceptance of CCM, Theorem 1.1 becomes unconditional. Our contribution (Layers 2–6 of the proof chain) is independent of CCM's status and is proved here.*" — matches the primary source.

**Paper 13 RH §1.5** (R.D.1 lines 256–258).
- Primary source: `paper13-rh/preprint/sections-01-05.md` lines 219–240.
- Content match: **VERIFIED, verbatim** for the specific passage the Author quotes ("For the reader interested only in the proof of RH, Sections 3–11 are self-contained and do not depend on the CBB axioms"). The Author's own Step 5.5 paragraph 3 correctly cites and block-quotes this passage. *However*, the Author's *structural interpretation* of this passage is the problem — see §5 below.

**Paper 26 BSD Theorem 13.1** (R.D.1 lines 118–127).
- Primary source: `paper26-bsd/preprint/sections-part-IV.md` line 360.
- Content match: **VERIFIED, verbatim.**

**Paper 26 BSD Theorem 9.1** (R.D.1 lines 128–132).
- Primary source: `paper26-bsd/preprint/sections-part-III.md` lines 606–611.
- Content match: **VERIFIED, verbatim** for the theorem statement; the remark on "36 zero-parameter predictions" and "$P < 10^{-89}$" is the right text from the source §13.1 Remark, not §9.1 Remark (which is a different remark about independent support). Minor: R.D.1 cites §9.1 for the remark but the actual quoted text is from the §13.1 Remark (line 373). Not a substance issue — both remarks exist in Paper 26, and the Author's citation pattern attributes the contrapositive-probability phrasing to Paper 26 which is correct, but the specific theorem-level location is §13.1, not §9.1. **Low-priority note: the Author's Remark 1.B currently cites Paper 26 §13.1 for the CBB contrapositive phrasing, which is correct.**

**Paper 26 §15 header + sub-structure** (R.D.1 lines 140–148).
- Primary source: `paper26-bsd/preprint/sections-parts-V-VI.md` lines 203–209 (header) and lines 209, 272, 296, 329, 353 (sub-section headers).
- Content match: **VERIFIED, verbatim** for the header opening phrase ("This section is the most important in the paper. Everything before it is a proof. Everything after it is context. This section is the honest accounting of scope.") and the five sub-section titles (15.1 Rank 0 and rank 1: proved / 15.2 Rank ≥ 2: genuinely open / 15.3 Non-CM curves: genuinely open / 15.4 Class number h_K > 1: expected to extend / 15.5 The Langlands frontier).
- **Substructure interpretation: VERIFIED.** The Author correctly describes Paper 26 §15 as a five-row pattern (15.1 proved / 15.2–15.3 outside scope / 15.4 expected to extend / 15.5 frontier). The Author correctly notes that Paper 8 needs a substantively different sub-structure because Paper 8's scope items are different, and adapts the template accordingly (15.1 proved / 15.2 H4 standing conditional / 15.3 outside scope / 15.4 compact simple groups / 15.5 frontier). **The adaptation is sound.** Paper 26 §15 does not have a dedicated "standing conditional" row because Paper 26 has no standing conditional beyond CBB; Paper 8's §15.2 is the correct Paper-8-specific slot.

**Paper 26 Route 3 KMS projector** (R.D.1 lines 346–347, Remark 1.B).
- Primary source: `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` lines 14–16 (projector definition) and §§3.2, 3.3 (the post-MY4 standing).
- Content match: **VERIFIED.** The projector formula `$P_k^{\mathfrak{p}} := I - s_{\mathfrak{p}}^k(s_{\mathfrak{p}}^k)^*$` in Remark 1.B matches the primary source `P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^* = I − e_{𝔭^k}`. The characterization of Paper 26 post-MY4 as "conditional on CBB alone" is also verified against `05-route3-kms-projector-bypass.md §3` lines 195–208 ("Paper 26 Theorem 13.1 ... becomes [THEOREM conditional on CBB axioms] — inheriting only the CBB axiomatic framework from Paper 13").

**Citation verification verdict: all direct quotes are verbatim-accurate.** The author has not introduced any fabricated content or misattribution. The structural-interpretation issue is a logical-inference problem, not a citation problem (see §5 below).

---

## 3. Cross-node consistency: "17/18 unconditional on H4"

The Author's abstract and §15.1 both claim "seventeen of the eighteen proof-chain steps are unconditional on H4". I cross-checked this against `paper08-yang-mills/preprint/PROOF-CHAIN.md §IV.1`.

**PROOF-CHAIN.md §IV.1 table** (lines 8–29): 18 numbered steps (1, 1b, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10b, 11, 12, 13, 14, 15, 16, 17, 18). Steps labeled "Proved" or "Literature": 1, 1b, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10b, 11, 12, 13, 14, 15, 16, 17. Step labeled "Conditional on H4": 18.

**Discrepancy at the row level:** the table actually has **19** row entries (there are two step-1 rows, 1 and 1b, plus a step-10b row, so the numbering goes 1, 1b, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10b, 11–18 = 19 table rows, labeled via 16 whole numbers plus two half-steps). The Author's phrasing "eighteen steps" is *consistent with the whole-number numbering* (1–18, with 1b and 10b treated as sub-steps not counted separately), which is also how §IV.5 and §12.7 are framed.

**Confirming the "17/18" claim:**
- §IV.5 (Scope paragraph, PROOF-CHAIN.md lines 142–165) says: "The gradient-flow programme (Steps 15–17) is unconditional; Step 18 is conditional on the standard hypothesis H4". So Steps 1–17 unconditional; Step 18 conditional. **17/18 is correct at the whole-number row level.**
- `paper08-yang-mills/preprint/sections/L-clay-conjectures.md §L.6.1 / §L.6.2` confirms H4 affects three sub-items inside Step 18: Conjecture L.1(iii), Conjecture L.2, and the AF form of Conjecture L.4. The Author's Step 5.5 Way 2 self-suspicion correctly identifies this refinement and the artifact correctly enumerates the three sub-items in Theorem 1 clause (C).
- `paper08-yang-mills/preprint/sections/08-conclusion.md §12.7` (referenced but not read in this critique pass; the Author cites it as the 11-row C1–C11 compliance table with 9 unconditional / 2 H4-conditional). This is consistent with the Author's mapping of H4 to Clay C7 + C9-AF.

**Cross-node consistency verdict: 17/18 is consistent with PROOF-CHAIN.md §IV.1 + §IV.5 and L-clay-conjectures.md §L.6.** No contradiction.

**One minor precision note for author consideration (not load-bearing).** The Author's §15.2 "The perimeter of what H4 affects" block (lines 397–401) correctly enumerates the three sub-items of H4's perimeter: L.1(iii), L.2, and AF form of L.4. The same block then says "Nine of the eleven Clay requirements are unconditional on H4. Two require H4." The mapping of "three sub-items" → "two Clay requirements" is: L.1(iii) + L.2 both fall under Clay C7 (the AF match + anomalous-dimension match clause), and AF form of L.4 falls under Clay C9-AF. **This is correct.** But the Author should consider making the 3→2 collapse explicit in §15.2 so the referee does not count three different things and trip on the arithmetic.

---

## 4. Extension test: could the two-dependency template be wrong for Paper 8?

I checked whether the artifact's template would fail for Paper 8 in any cases the Author did not consider. Two specific worries:

**(a) Could CBB axioms themselves be conditional on a deeper axiom?** No. Paper 23 (read indirectly via the Author's citation to `paper13-rh/preprint/sections-01-05.md §2` — which I confirmed describes Definition 2.1 and the five axioms with no upstream dependencies in the text) presents the CBB system as a zero-parameter axiom base, not as a derived structure. The CBB axioms are the floor, not a mezzanine, of the Integers programme. Extending the artifact to carry a third dependency is not needed.

**(b) Could H4 actually require MORE than just the W7-14 reformulation?** This is the interesting test. The Author's Theorem 1 clause (C) cites H4 "in the form stated in `gradient-flow-attack-plan/research/W7-14-af-match.md §5.3`, where H4 is reduced to the claim that the Taylor coefficients $F^{(n)}(0)/n!$ of the analytic function $F(t)$ are computed by the standard Feynman-diagrammatic perturbative rules". This is mildest-form H4. The blackboard §J notes from the W1-A1 run (lines 478, 485) report an I-7 catch: the W7-14 §5.3 reformulation still leaves H4 open because "the perturbative side is a formal power series, not an analytic function". **This is a structural subtlety the Critic should flag**: the Author's artifact describes the W7-14 form as "a statement about one analytic function" (Theorem 1 clause C, §15.2, W7-14 cross-ref), but the I-7 catch from W1-A1 says the perturbative side of the comparison is a formal power series, not an analytic function. If the artifact's phrasing is taken at face value, a careful reader would expect the comparison to be between two convergent Taylor series on the same disk, and the I-7 catch shows that is not quite what W7-14 §5.3 actually delivers — the non-perturbative side is analytic with a convergent series, the perturbative side is a formal series, and the match claim is "the Taylor coefficients of the analytic function equal the formal-series coefficients term-by-term".

**Assessment of this subtlety.** The Author's phrasing in the artifact *is* compatible with the I-7 catch if read carefully: "the Taylor coefficients $F^{(n)}(0)/n!$ of the analytic function $F(t)$ at $t = 0$ are computed by the standard Feynman-diagrammatic perturbative rules". This says the coefficients of the analytic function are computed by the perturbative rules, not that the perturbative rules sum to an analytic function. **The phrasing is technically correct but is easy to misread as "two analytic functions agree".** For a Clay-submission-grade preprint, a small clarification would help: add a parenthetical in Theorem 1 clause (C) and in the W7-14 cross-reference block making explicit that the perturbative side is a formal power series and H4 is the term-by-term match of the formal coefficients with the analytic function's Taylor coefficients. This is not a BROKEN issue; it is a PRECISION issue that a referee might query. I note it here for author consideration.

**Extension test verdict: the two-dependency template is sound for Paper 8; no deeper axiom needed; the H4 form-precision subtlety is a low-priority author-consideration note, not a blocker.**

---

## 5. Pattern-check against §F (killed approaches)

The editorial artifact is not re-entering any killed approach. Routes A, B, C are named and catalogued in the artifact correctly as the closure programme; Route D (the editorial node itself) is the HONEST-STALL option. The artifact does not propose any new *mathematical* closure mechanism, so the §F kill register (K-1 for R.B.1 — CCM port, and K-2 for R.C.1 — spectral action) does not apply to this artifact.

**§F-check verdict: no pattern re-entry. Clean.**

---

## 6. LOCK verification (editorial version)

For an editorial node, the LOCK check is: **does the conditional statement compose consistently with Paper 13 RH and Paper 26 BSD without introducing contradictions?** I checked this by tracing the Author's proposed Theorem 1 statement back to the load-bearing source rows:

- **Row 1** (theorem-label dependency form): Paper 13 RH's "conditional on CCM" grammar (`paper13-rh/preprint/sections-01-05.md §1.1`). **Independent.** The grammar is Paper 13's choice and is documented in Paper 13's own referee fix #6 ("Theorem 1.1 reframed as conditional on CCM"; see `paper13-rh/preprint/00-proof-skeleton.md` line 231).
- **Row 2** (axiom-base "from CBB" formulation): Paper 26 BSD's Theorem 13.1 (`paper26-bsd/preprint/sections-part-IV.md §13.1`). **Independent.**
- **Row 3** (the five-sub-section §15 template): Paper 26 BSD §15 (`paper26-bsd/preprint/sections-parts-V-VI.md §15`). **Independent.**
- **Row 4** (H4 W7-14 mildest form): `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md §5.3`. **Independent.**
- **Row 5** (CBB framework embedding of Paper 8 via Paper 10): `paper08-yang-mills/preprint/sections/N-qg5d-inputs.md` (cited in the artifact as Appendix N) + `paper12/27-anchor-document.md §1–2`. **Independent** (different file, different axiom system, orthogonal content).

**The artifact's load-bearing claim does NOT depend on a single source row; it depends on an independent set of at least four rows that do not derive from one another.** This is strong LOCK: if any single row were wrong, only that row's piece of the artifact would need updating, not the whole artifact.

**LOCK verdict: PASSED.** The editorial artifact is robustly composable.

---

## 7. The load-bearing issue: "two-dependency" template justification in Remark 1.B

This is the WEAKENED finding. I will be precise about what is wrong and what needs to change.

**What the Author claims** (Remark 1.B, lines 346–347, and §M summary lines 469–470):

1. Paper 13 RH ships with a two-dependency conditional (CCM headline + CBB framework).
2. Paper 26 BSD post-MY4 ships with a one-dependency conditional (CBB alone).
3. Paper 8 YM therefore inherits Paper 13's two-dependency *grammar* (H4 headline + CBB framework).

**What the primary sources actually say:**

- Paper 13 RH's Theorem 1.1 is stated conditional on CCM *alone*. Paper 13's §1.5 explicitly says: "For the reader interested only in the proof of RH, Sections 3–11 are self-contained and do not depend on the CBB axioms. The proof uses CCM's operators, our ITPFI factorization, Boegli's theorem, and Hurwitz's theorem — all independent of the broader Integers programme." Paper 13 RH's *proof chain* has **one** dependency at the logical level: CCM. CBB is named in §1.5 and §2 as the *motivational embedding* of Paper 13 into the Integers programme, not as a logical dependency of the Theorem 1.1 proof.
- Paper 26 BSD post-MY4 (Route 3) is stated conditional on CBB alone, with the CBB axioms being the *sole* logical dependency. Paper 26's §15 notes explicitly that "The proof is conditional on CBB, the same axiomatic foundation as the RH proof (Paper 13)" (`sections-part-III.md` line 857) — *but this phrasing "same axiomatic foundation" is a motivational claim, not a claim that Paper 13 RH's proof chain depends on CBB*. The shared axiomatic foundation is the Integers programme context, which both papers sit inside; Paper 13's proof chain is CBB-independent per §1.5, Paper 26's proof chain is CBB-dependent because the BC bridge algebra $\mathcal{A}_{BC,K}$ and the KMS$_1$ ITPFI factorization directly use CBB-system machinery (`paper26-bsd/preprint/sections-part-III.md §9`).
- Paper 8 YM's situation is its own: the proof chain uses Balaban + KK geometry + gradient flow, and CBB enters only at the framework-level embedding via Paper 10 / Appendix N. Whether Paper 8's proof chain is CBB-*dependent* or CBB-*embedded-but-independent* (like Paper 13 RH) is a structural question about Paper 8 itself that R.D.1 does not verify.

**The structural fact the Author missed.** Paper 13 RH's two "dependencies" (CCM and CBB) are not the same *kind* of dependency: CCM is a logical dependency of the proof chain (Sections 3–11 use CCM's operators directly), while CBB is a motivational embedding (§1.5 says the proof chain is independent of CBB). So Paper 13 is NOT a two-dependency grammar in the sense "two logical dependencies on the theorem-statement face"; it is a one-logical-dependency grammar (CCM) with a framework embedding (CBB) noted in §1.5 but not on the theorem-label face. The theorem label is "Theorem 1.1 (RH, **conditional on CCM**)" — one dependency, not two.

**Why this matters for Paper 8.** If Paper 8 genuinely has *both* a logical dependency on H4 (which it does — Step 18) *and* a logical dependency on CBB (which is an open structural question — does Paper 8's Appendix L actually use CBB axioms, or does it only sit inside the Integers programme as context?), then Paper 8 is a genuinely-two-dependency paper and the Author's template is correct *for Paper 8 on its own merits*. If Paper 8 is CBB-framework-embedded-but-not-dependent (analogous to Paper 13 RH), then Paper 8 is a one-logical-dependency paper (H4 alone) with a CBB framework embedding, and the Author's template is overclaiming a CBB logical dependency where there is only a framework embedding.

**This is a real question the artifact does not answer.** The Author's Step 5.5 Way 1 correctly flags it (paragraph 3: "YM uses Balaban + KK geometry + gradient-flow + Epstein vanishing, none of which are CBB-framework tools directly — but Paper 8's *framework-level* embedding into the Integers programme (via Paper 10's relation to the e-dimension and the 5D QG infrastructure) provides the CBB anchor") — but then the artifact proceeds to *treat* the CBB anchor as a logical dependency in Theorem 1 clause (C) final sentence: "*The proof is carried out within the CBB axiomatic framework of the Integers programme (Papers 23–24) and depends on the CBB axioms at the framework-level embedding of Paper 8 via Paper 10's 5D Quantum Geometry infrastructure (Appendix N).*"

**The phrase "depends on the CBB axioms at the framework-level embedding" is semantically ambiguous**: it could mean "Paper 8 depends on CBB for framework embedding" (embedding-dependence — like Paper 13) or "Paper 8 depends on CBB axioms whose embedding goes through Paper 10" (logical dependence via Paper 10). These are structurally different. A Clay referee will notice the ambiguity and ask "which?"

**Required author revision (the WEAKENED ask).** The Author should do one of the following:

**Option 1 (minimal, preferred).** Mirror Paper 13 RH exactly: state Theorem 1 conditional on H4 *alone* on the theorem-label face, with CBB as a *framework embedding* noted in Remark 1.A, not as a logical dependency of the proof chain. The theorem label becomes: "Theorem 1 (Yang–Mills mass gap with full Jaffe–Witten structural compliance, conditional on H4 in the W7-14 mildest form)". Remark 1.A gets a new paragraph stating that Paper 8 sits inside the Integers programme (framework embedding via Paper 10 / Appendix N) but Paper 8's proof chain is independent of the CBB axioms at the logical level (analogous to Paper 13 RH §1.5). This makes Paper 8 a **one-dependency** conditional at the theorem-label face, *matching Paper 13 RH's actual grammar rather than the mis-characterized "two-dependency" version*. The §M summary and §15.2 update accordingly.

**Option 2 (if the Author can verify that Paper 8's Appendix L genuinely uses CBB axioms as logical dependencies of the gradient-flow construction).** Keep the two-dependency theorem label but rewrite Remark 1.B to correctly state the structural asymmetry: "Paper 13 RH ships conditional on CCM alone (Paper 13's proof chain is independent of CBB per Paper 13 §1.5). Paper 26 BSD ships conditional on CBB alone (Paper 26's proof chain depends on CBB via the BC bridge algebra). Paper 8 YM ships conditional on both CBB (via Appendix N / Paper 10 / 5D QG framework-logical embedding) and H4 (via Appendix L / W7-14 §5.3)." This requires the Author or the runner to positively verify that Paper 8's Appendix L genuinely uses CBB logical content (not just framework motivation) via Paper 10. I did not verify this in this Critic pass because (a) it requires reading Paper 10 and Appendix N end-to-end, which is beyond the scope of this R.D.1 Critic, and (b) the question is properly a Paper-8-internal question that the R.D.1 author should confirm before shipping the two-dependency theorem label.

**My recommendation: Option 1.** The one-dependency theorem label is the honest, conservative choice and mirrors Paper 13 RH's actual grammar. If the Paper 8 / Paper 10 logical dependency on CBB turns out to be genuine (Option 2), the theorem label can always be strengthened later; going the other direction (downgrading from two to one) would be an embarrassment once the preprint is out. Option 1 is ship-safe. Option 2 requires additional load-bearing verification that R.D.1 did not do.

**Concrete edits required (minimal diff, under the Option 1 recommendation):**

1. **Theorem 1 label** (line 331): change "conditional on H4 in the W7-14 mildest form" to — unchanged if Option 1 is adopted. (The current label already names H4 alone. The issue is in the *body*, not the *label*.) Wait — I re-read the label. The current label reads: "**Theorem 1 (Yang–Mills mass gap with full Jaffe–Witten structural compliance; conditional on H4 in the W7-14 mildest form).**" This is *already* a one-dependency label on H4 alone. Good. The label is fine. The issue is in the body, specifically line 343 ("*The proof is carried out within the CBB axiomatic framework of the Integers programme (Papers 23–24) and depends on the CBB axioms at the framework-level embedding of Paper 8 via Paper 10's 5D Quantum Geometry infrastructure (Appendix N).*") — this sentence is the ambiguity source.

2. **Theorem 1 body closing sentence** (line 343): **REMOVE** the ambiguous "depends on the CBB axioms at the framework-level embedding" phrasing. **REPLACE** with: "*The proof chain uses Balaban's RG, KK-enhanced lattice geometry, and the gradient-flow construction of Appendix L, and is logically self-contained modulo Hypothesis H4. Paper 8 sits inside the Integers programme as a framework-level embedding via Paper 10 and Appendix N, mirroring Paper 13 RH's relation to the CBB axioms (Paper 13 §1.5): the framework motivates the paper's place in the programme, but the proof chain does not depend on the CBB axioms at the logical level.*" This is honest, mirrors Paper 13's grammar exactly, and removes the ambiguity.

3. **Abstract conditional sentence** (line 323): **REMOVE** the phrase "a theorem conditional on the Critical Bost–Connes–Brauer axioms (Paper 23) and on Hypothesis H4 in its gradient-flow reformulation". **REPLACE** with "a theorem conditional on Hypothesis H4 in its gradient-flow reformulation". Keep the "same conditional shape that Paper 13 RH ships with ('conditional on CCM', arXiv:2511.22755)" phrasing; **REMOVE or REWORD** the parallel phrase "that Paper 26 BSD ships with ('from CBB', Paper 23)". The parallel is inexact because Paper 26 has a CBB logical dependency where Paper 8 has only a framework embedding. Suggested replacement: "a theorem conditional on Hypothesis H4 in its gradient-flow reformulation — mirroring Paper 13 RH's grammar of shipping a Clay-class theorem conditional on a single short-term dependency (Paper 13: CCM; Paper 8: H4 in the W7-14 mildest form), with the broader CBB framework embedding of the Integers programme noted separately in Remark 1.A. Paper 26 BSD's 'from CBB' grammar (`paper26-bsd/preprint/sections-part-IV.md §13.1`) represents the downstream state where the short-term dependency has been closed and only the framework embedding remains."

4. **Remark 1.A** (line 345): **REWRITE** the opening sentences to state that Paper 8 carries **one logical dependency** (H4), with the CBB axioms noted as the framework embedding. The current opening "Paper 8 carries two logical dependencies" is the exact sentence that needs to change. Suggested replacement: "Paper 8 carries one short-term logical dependency — **Hypothesis H4** — stated in the W7-14 §5.3 reformulation, the mildest form of H4 in the literature. Paper 8 sits inside the Integers programme as a framework-level embedding via Paper 10 and Appendix N, mirroring Paper 13 RH's relation to the CBB axioms (Paper 13 §1.5): the framework motivates the paper's place in the programme, but the proof chain does not depend on the CBB axioms at the logical level. The CBB system is independently supported by 36 zero-parameter closed-form predictions ($P < 10^{-89}$; see `paper12/27-anchor-document.md §4`)." The "If any of the three routes closes" sentence can stay (it's about Routes A/B/C).

5. **Remark 1.B** (line 347): **REWRITE** to reflect the actual structural pattern. Suggested replacement: "Paper 13 RH ships as 'Theorem 1.1 (RH, conditional on CCM)' — conditional on the Connes–Consani–Moscovici 2025 preprint (arXiv:2511.22755; expected to become unconditional on journal acceptance); Paper 13's proof chain is independent of the CBB axioms at the logical level (Paper 13 §1.5). Paper 26 BSD ships as 'Theorem 13.1 (BSD from CBB)' — conditional on the CBB axioms alone, after the Bost–Connes 'Meyer wall' MY4 was bypassed via G Six's KMS projector $P_k^{\mathfrak{p}} := I - s_{\mathfrak{p}}^k(s_{\mathfrak{p}}^k)^*$ (`paper26-bsd/strategy/05-route3-kms-projector-bypass.md`); Paper 26's proof chain genuinely depends on CBB via the BC bridge algebra $\mathcal{A}_{BC,K}$ and the KMS$_1$ ITPFI factorization. Paper 8 Yang–Mills, by the present theorem, ships as 'Theorem 1 (Yang–Mills, conditional on H4 in the W7-14 mildest form)' — conditional on a single short-term hypothesis H4, mirroring Paper 13's one-dependency theorem-label grammar, with the CBB framework embedding noted in Remark 1.A but not carried as a logical dependency of the proof chain. Three Clay Millennium Prize artifacts, three instances of the programme's conditional-grammar template with differing dependency structures; Paper 8 and Paper 13 are closest in shape (one short-term dependency, framework embedding noted separately)."

6. **§M summary** (R.D.1 lines 469–471): adjust the "Paper 8 is therefore structurally closer to Paper 13's two-dependency form (CCM + CBB for Paper 13; H4-W7-14 + CBB for Paper 8)" sentence to "Paper 8 is therefore structurally closer to Paper 13's **one-dependency-on-the-theorem-label-face + framework-embedding** form (Paper 13: CCM + Integers-programme embedding; Paper 8: H4 + Integers-programme embedding) than to Paper 26's one-dependency-*from-CBB* form (where the framework embedding has been upgraded to a logical dependency via the BC bridge algebra)."

7. **§15.2** (line 371 onwards): one small edit. The current §15.2 opening says "The wall, honestly stated" and proceeds to enumerate H4 — no changes needed in this sub-section. It correctly foregrounds H4 as the single standing conditional and does not overclaim a CBB logical dependency. Fine as is.

8. **§I note CONCERN** (line 482 of R.D.1): adjust to reflect the corrected understanding. Current: "Paper 13 RH carries *two* distinct conditional dependencies (CCM as the headline preprint-dependency and CBB as the framework axiom-base)". Replace: "Paper 13 RH carries *one* logical dependency on the theorem-label face (CCM) with a separate framework embedding into the Integers programme (CBB, noted in §1.5 but not carried through the proof chain). Paper 26 BSD carries *one* logical dependency (CBB alone, after MY4 bypass) where the framework embedding has been upgraded to a logical dependency via the BC bridge algebra. Paper 8 YM, by the present editorial artifact, ships as one-logical-dependency (H4) with the CBB framework embedding noted in Remark 1.A."

These edits are confined to ~8 lines in the actual theorem body + ~3 lines in the §I notes, plus Remark 1.A / 1.B rewrites (~15 lines each). **Total diff ~60 lines in a 522-line file.** The edits do not change the structure of Theorem 1 (three clauses A/B/C unchanged), the §15 scope section (five sub-sections unchanged), or the W7-14 cross-reference block (unchanged). The voice register is preserved — the terse declaration phrases, the named ritual elements, and the §J register markers are all kept. **The edits are strictly a correction of the prior-art structural claim that propagates into the Paper-8 characterization; they do not change the ship-ready status of the artifact once applied.**

---

## 8. Pattern check — generative step verification

The Author credits Step 3 UNIFY (Pattern 2: holonomy correspondence) as the generative step. I verified against `paper12/research/214-the-method-six-patterns.md §Pattern 2` (line 79) and the 6-step loop (§Step 3, line 269–270): "**Step 3 (Pattern 2 — unify):** Recognize the phenomenon as an instance of the holonomy correspondence."

**The Author's generative claim is correct.** Paper 2's holonomy correspondence says "recognize a phenomenon as an instance of a known template"; the Author recognized Paper 8's editorial artifact as an instance of "the programme's conditional-grammar template" with Paper 13 and Paper 26 as prior-art instances. This is Step 3 UNIFY / Pattern 2 exactly.

**Generative-step verdict: correct.**

---

## 9. Bonus-grep: unstated assumptions, dangling citations, overclaims

I grep'd the artifact for common failure modes.

**Dangling citations.** All cross-references I spot-checked resolve:
- `paper08-yang-mills/preprint/sections/00-abstract.md` — exists (I read it, 110 lines).
- `paper08-yang-mills/preprint/sections/L-clay-conjectures.md` — exists (I grep'd it, Theorem L.0 lines 10–48 matches the Author's verbatim quote).
- `paper08-yang-mills/preprint/PROOF-CHAIN.md §IV.1` — exists (I read it, 18-step table).
- `paper08-yang-mills/research/35-final-verdict.md §I–VI` — exists (I read it, 172 lines; the Author's register quotes match).
- `paper13-rh/preprint/sections-01-05.md §1.1` — exists (I read it, Theorem 1.1 at lines 69–73).
- `paper26-bsd/preprint/sections-part-IV.md §13.1` — exists (I read it, Theorem 13.1 at line 360).
- `paper26-bsd/preprint/sections-parts-V-VI.md §15` — exists (I read it, §15 header at line 203).
- `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` — exists (I read it, projector at lines 14–16).
- `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md §5.3` — referenced but not read in this Critic pass (the mildest-form reformulation exists; the Author's Step 5.5 Way 1 self-suspicion checks it).
- `paper12/27-anchor-document.md §1, §2, §4` — referenced but not read; not load-bearing for the Critic verdict.

**Overclaims I looked for:**

- *"Paper 8 ships as a theorem conditional on..."* — the abstract sentence phrasing. **Flagged** under §7 above (the CBB portion of the dependency is ambiguous).
- *"The three closure routes A/B/C may retire H4 entirely"* — the §15.2 phrasing. Factually correct (the Author notes "joint closure probability ≈ 0.74" which matches blackboard §E); **also notes** from the blackboard W1 outcome that A/B/C closure probabilities have collapsed to ~0.10 (A/B collapsed + C killed). R.D.1 was written at the start of W1-D1, so the 0.74 number represents *pre-W1-outcome* probabilities. **The 0.74 figure in Remark 1.A will be out of date by the time R.D.1 is inserted into Paper 8's preprint**, since by the end of Wave 1 the actual joint probability of closing H4 via Routes A/B/C is ~0.10 (blackboard §K line 495). **Author revision recommended**: update the joint closure probability in Remark 1.A and §15.2 from "0.74" to "0.10" (post-W1 state) — or, better, do not cite a specific joint probability at all in the preprint since probabilities will continue to move and a referee may bridle at a speculative joint probability in a Clay-class theorem's remark. Alternative: remove "joint closure probability is ≈ 0.74 across routes A–C" from Remark 1.A entirely; keep the routes named but do not attach probabilities. This is a low-priority edit but I flag it because it's a *factual correctness* issue post-Wave-1.
- *"The HONEST-STALL option, first-class per v3 patch I-5"* — §15.2 closing sentence on Route D. **Remove for preprint**: the "first-class per v3 patch I-5" phrasing is internal runner-blackboard language and does not belong in a Clay-submission preprint. Replace with: "Route D (this editorial node). Retire the 'open' label on H4 by stating it explicitly as a conditional in its mildest form and shipping Paper 8 in the standing form of Theorem 1." This is strictly an in-preprint language cleanup; the runner/author knows the phrase "first-class per v3 patch I-5" has internal meaning but a Clay referee does not and should not see it.
- *"Runner $p \approx 0.99$"* — §15.2 on Route D. **Remove for preprint**: probabilities attached to editorial-closure options do not belong in a Clay-class preprint. Replace: remove the $p \approx 0.99$ phrase. Keep the descriptive sentence ("HONEST-STALL option") without the probability.

**Bonus-grep verdict: found two low-priority preprint-insertion cleanups** (the "0.74" probability becoming stale post-W1; the internal runner language in §15.2). Both are **not blockers for the Critic verdict**; they are author-revision items for the W2 editorial merge task, not for the R.D.1 node-level advancement. I flag them here so the author has a complete list.

---

## 10. CoV on grep findings

**CoV = corroboration of verification.** For each non-trivial grep finding I made above, I independently sanity-checked by re-reading the surrounding context.

- **Paper 13 §1.5 passage** — I read lines 219–240 of `sections-01-05.md` directly and the sentence "For the reader interested only in the proof of RH, Sections 3–11 are self-contained and do not depend on the CBB axioms" appears verbatim. CoV confirmed.
- **PROOF-CHAIN.md §IV.1** — I read lines 1–165 of PROOF-CHAIN.md directly and the 18-step table (Steps 1, 1b, 2, 3, ..., 17, 18 with Step 18 the only "Conditional on H4" row) is intact. §IV.5 confirms 17/18 accounting. CoV confirmed.
- **Paper 26 §15 five-sub-section structure** — I read lines 203–383 of `sections-parts-V-VI.md` directly and the five sub-sections (15.1 proved / 15.2 rank ≥ 2 open / 15.3 non-CM open / 15.4 h_K > 1 expected / 15.5 Langlands frontier) are intact. CoV confirmed.
- **Paper 13 Theorem 1.1 verbatim** — I read lines 63–82 directly and the text matches the Author's quote verbatim. CoV confirmed.
- **Paper 26 Theorem 13.1 verbatim** — I read line 360 directly and the text matches the Author's quote verbatim. CoV confirmed.
- **Paper 26 Route 3 projector formula** — I read lines 14–16 of `05-route3-kms-projector-bypass.md` directly and the formula matches the Author's Remark 1.B quote. CoV confirmed.
- **The "28 register markers" claim** — I independently counted 50 markers across the 4 pieces (~1.8× the Author's count), confirming the direction of the Author's claim (voice-shape passes comfortably) while flagging the quantitative discrepancy as a recording issue only. CoV confirmed (in the direction of the Author's structural claim, with a minor count adjustment).

**CoV verdict: all non-trivial grep findings corroborated by direct reading.** No phantom citations, no fabricated content.

---

## 11. Byte-for-byte — N/A

No code in this node. No numerical computations. Byte-for-byte check inapplicable.

---

## 12. Summary of findings by severity

**BLOCKER (must-fix before merge into Paper 8 preprint):**
- None.

**WEAKENED (must-fix before the R.D.1 artifact is considered ship-ready as editorial output):**
- **Two-dependency template mis-characterization** (§7 above): Paper 13 RH's Theorem 1.1 is one-dependency on the theorem-label face (CCM) with CBB as framework embedding per §1.5, not two-dependency. The Author's Theorem 1 body, Remark 1.A, Remark 1.B, §M summary, and §I note CONCERN all carry the incorrect two-dependency characterization. **Required revision: ~60 lines of edits per §7 recommendation (Option 1: mirror Paper 13's one-dependency grammar for Paper 8).**

**LOW-PRIORITY (author-consideration, not blockers):**
- **Stale joint probability** in Remark 1.A / §15.2 (the "≈ 0.74 across routes A–C" figure becomes "≈ 0.10" after Wave 1 outcomes; recommend removing the specific probability from the preprint version).
- **Internal runner language in §15.2** ("Runner $p \approx 0.99$", "the HONEST-STALL option, first-class per v3 patch I-5") should be stripped from the preprint-insertion version.
- **Numeric vs spelled-out "17"/"Seventeen"** — consistency preference, pick one across all four pieces.
- **"3 sub-items → 2 Clay requirements"** collapse in §15.2 should be made explicit.
- **Precision on "analytic function" vs "formal power series"** in Theorem 1 clause (C) and the W7-14 cross-reference block — the phrasing is technically correct but easy to misread; a parenthetical clarification would help a careful referee.

**VERIFIED (no issues):**
- Voice-shape check: 4/4 pieces pass, independent count 50 markers (Author's 28 was a conservative undercount).
- Prior-art verbatim quotes: all direct quotes verify byte-accurate against primary sources.
- Cross-node consistency with PROOF-CHAIN.md: "17/18 unconditional" is correct.
- §F kill register: no pattern re-entry.
- LOCK check: the artifact's load-bearing claim depends on ≥4 independent source rows, strong LOCK.
- Generative step: Step 3 UNIFY (Pattern 2 holonomy correspondence) is correctly identified.
- §15 five-sub-section adaptation: sound (Paper 8's scope items are different from Paper 26's, and the Author correctly re-mapped the template slots).
- The H4 W7-14 mildest-form description is structurally compatible with the W1-A1 I-7 catch (the artifact's phrasing is technically correct; precision note in §4 above is a recommendation, not a correction).

---

## §I notes to append to blackboard

- **CONCERN — R.D.1 Critic cycle 1**: The R.D.1 artifact characterizes Paper 13 RH as two-dependency (CCM + CBB), but Paper 13 §1.5 states explicitly that the proof chain is CBB-independent at the logical level. Paper 13's Theorem 1.1 label is one-dependency (CCM alone). Required revision: apply Option 1 per critique §7 (mirror Paper 13's one-dependency grammar; move CBB to a framework-embedding note in Remark 1.A). ~60 line diff. Not a blocker for R.D.1's node-level ADVANCED status, but a blocker for the preprint-insertion W2 editorial task.

- **CASCADE — voice-canon check transfer**: Independent Critic recount of §J register markers in R.D.1 yielded 50 markers across the 4 pieces (vs Author's 28). Voice-shape check passes 4/4 per both counts; the discrepancy is in the counting granularity, not the structural verdict. Update blackboard §M cycle-1 row recording to "50 register markers" (or reconcile via a specific counting rule — the Author likely counted only the strongest markers per category per piece; the Critic counted all markers). Structural verdict unchanged.

- **LESSON — prior-art structural claims need primary-source verification, not brief-paraphrase trust**: The Author's Step 5.5 Way 1 performed the backward-verification check by reading Paper 13 §1.5 directly and quoting the correct passage — but then drew the wrong structural conclusion from the correct quote. This is a subtler failure mode than the W1-A1/B1/C1 brief-paraphrase catches: the source was read correctly, but the *inference* from the source was wrong. The I-7 discipline needs augmentation: "backward-verify the source quote *and* the structural conclusion drawn from the quote". For the R.D.1 case, the correct inference from Paper 13 §1.5 is that Paper 13 is *one-dependency-on-the-theorem-label-face* (CCM) with *framework embedding in Integers programme* (CBB), not two logical dependencies. Propose patch I-9: "inference-from-source-check" added to the Step 5.5 Way-1 backward-verification discipline.

- **LESSON — editorial artifacts benefit from a "ship-safe reading" test**: The Critic found the R.D.1 issue by applying a "what would a Clay referee reading this cold ask?" test to Theorem 1 clause (C)'s final sentence ("depends on the CBB axioms at the framework-level embedding"). The ambiguity there would provoke a referee question. **Recommended discipline for future editorial nodes**: after Step 6 voice-shape check, add a Step 6.5 "ship-safe reading" step: re-read each artifact with a referee's eye, flagging any semantic ambiguities in load-bearing phrases. This is a low-cost discipline that catches a specific failure mode (ambiguity-propagation) that voice-shape check does not catch.

---

## §D toolkit changes

- **PCGT (Programme Conditional-Grammar Template)** — the Author proposes adding this as a new §D row with status S, completeness 100% at template level. **Critic concurs with the proposal** but with a **refinement to the template itself**:
  - **Revised template (1 line)**: Theorem-label names the short-term logical dependency on its face (one dependency; if multiple, name the most short-term); precise form of the dependency cited (specific theorems/lemmas/axioms/reformulation paths); companion remark explains standing + independent support + what becomes unconditional on closure + framework embedding (if any) noted separately from the logical dependency; §15 (Scope) with the five-sub-section structure (proved / standing conditional / outside scope / expected to extend / method frontier); voice-shape check against the programme's §J register mandatory on Step 6; **NEW**: ship-safe re-reading check for semantic ambiguity in load-bearing phrases mandatory on Step 6.5.
  - **Status**: S (structural). Triply tested (Paper 13 RH one-dependency, Paper 26 BSD one-dependency post-MY4, Paper 8 YM one-dependency per corrected R.D.1).
  - **Notation**: PCGT.
  - **Completeness %**: 100 at template level; R.D.1 instance for Paper 8 is *conditionally* ready pending the Option 1 revision per critique §7.

- **The "W7-14 mildest-form reduction of H4"** row (the Author's second §D proposal): **Critic concurs as stated**. Status S, completeness 70%, notation H4^(W7-14). No changes.

---

## §M summary (≤200 words)

**R.D.1 verdict: WEAKENED.** The editorial artifact is structurally sound on most axes: four draft pieces (abstract, Theorem 1+3 remarks, §15 five-sub-section scope, W7-14 cross-reference) with 50 independently-counted §J register markers (Author's 28 was a conservative undercount, factor 1.8), all four pieces passing voice-shape, all direct prior-art quotes byte-verbatim against primary sources, LOCK robust (≥4 independent source rows), no §F kill re-entry, cross-node "17/18 unconditional" consistent with PROOF-CHAIN.md §IV.1. However, **the backward-verification Step 5.5 Way 1 misinterprets Paper 13 §1.5**: Paper 13 RH is one-dependency on the theorem-label face (CCM alone; CBB is framework embedding per §1.5's explicit disavowal), not two-dependency (CCM + CBB) as the Author claims. The Theorem 1 body, Remark 1.A, Remark 1.B, §M summary, and §I note CONCERN all propagate this mis-characterization. **Fix**: apply Option 1 (critique §7) — mirror Paper 13's one-dependency grammar for Paper 8 (H4 alone on theorem-label face; CBB as framework embedding in Remark 1.A). ~60 line diff. Once applied, R.D.1 advances to ship-ready for Paper 8 preprint insertion. Low-priority cleanups also noted (stale probability, internal runner language, numeric consistency) for the W2 editorial-merge task.

---

*End of R.D.1 cycle-1 Critic pass.*
*Critic: Claude Opus 4.6 (1M context), independent instance from Author.*
*Verdict: WEAKENED. Required author revision: ~60 lines per §7 Option 1. Voice-shape check 4/4 pass. Prior-art quotes verbatim. LOCK robust. No §F re-entry. The editorial artifact is close to ship-ready and becomes ship-ready after the Option 1 edits.*
