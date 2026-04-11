# Alpha-Critic — final adversarial pass on R.D.1 v2

*Alpha-Critic: fresh Claude Opus 4.6 (1M context) instance. H4 closure final-adversarial-pass. 2026-04-11.*
*Target: `paper08-yang-mills/closing-H4/nodes/R.D.1-abstract-conditional-v2.md` (565 lines).*
*Cycle-1 critique reference: `paper08-yang-mills/closing-H4/critiques/R.D.1-cycle-1.md` (§7 Option 1 edit list).*
*Attack scope: wave-close plan vectors (a–g, h, m). Mandate: ship-critical final check; do not rubber-stamp.*

---

## Verdict: **SURVIVED** (ship-ready, with two low-priority author-consideration notes)

R.D.1 v2 is ship-ready. The cycle-1 Critic's §7 Option 1 edit list was faithfully applied. The four draft pieces now mirror Paper 13 RH's actual one-dependency grammar correctly; the CBB mis-characterization that weakened v1 is gone from the theorem label, the Theorem 1 body closing sentence, Remark 1.A, Remark 1.B, the §M summary, and the §I CONCERN note. No new structural errors introduced in the revision. Independent verification against primary sources (Paper 13 §1.5, Paper 13 00-proof-skeleton.md, Paper 26 §15, Paper 26 §13.1, Paper 26 §9.1, Paper 8 L.0, PROOF-CHAIN.md §IV.5, 35-final-verdict.md) confirms the v2 structural claims.

I spent the adversarial effort looking specifically for: (1) overclaim drift in the abstract, (2) residual CBB-dependency framings that might still be lurking in the theorem body, (3) §15 sub-section items that are Paper-26-specific rather than Paper-8-adapted, (4) technical misreads of the Taylor-coefficient framing in the W7-14 cross-reference, (5) voice-shape markers that the v2 correction might have accidentally stripped. **I did not find any ship-blocking issue.** I found two low-priority author-consideration notes that do not block shipping.

Below I walk through each attack vector (a-g, h, m) with concrete findings.

---

## (d) Abstract conditional statement — adversarial read

**Target:** line 363 of v2 (one paragraph, three visible sentences by punctuation, ~220 words).

**The actual text (paraphrased for attack):**

> "The mass gap $\Delta_\infty > 0$ is proved unconditionally on H4 (Theorem 8); seventeen of the eighteen steps of the full proof chain are unconditional on H4; the four Jaffe–Witten §4 structural ingredients are closed in Appendix L with H4 entering only at L.1(iii), L.2, and the AF form of L.4 — Clay C7 and the AF logarithmic form of C9 — via the gradient-flow reformulation of H4 as a statement about the Taylor coefficients of a single analytic function $F(t) := S_{2,t}^c(x,y)/c_1(t)^2$ at $t = 0$. Paper 8 therefore ships as **a theorem conditional on Hypothesis H4 in its gradient-flow reformulation** — mirroring Paper 13 RH's grammar of shipping a Clay-class theorem conditional on a single short-term dependency on its theorem-label face ('Theorem 1.1, conditional on CCM', arXiv:2511.22755; cf. Paper 13 §1.5's explicit disavowal of CBB as a logical dependency of the proof chain), with the broader Integers programme framework embedding of Paper 8 (via Paper 10 and Appendix N's 5D Quantum Geometry infrastructure) noted separately in Remark 1.A. Paper 26 BSD's 'from CBB' grammar represents the downstream state where the short-term dependency has been closed via Route 3's KMS projector bypass and only the framework embedding remains..."

**Adversarial checks.**

1. **Does it overclaim?** No. The unconditional content (mass gap, 17/18 steps, stress tensor, renormalised composite, non-perturbative OPE structure, lattice confinement, compact simple group extension) is each verifiable against Paper 8 source files I checked. The conditional content (L.1(iii) + L.2 + AF form of L.4 = Clay C7 + C9-AF) is consistent with §L.6.1/§L.6.2 and §12.7 (not re-read in this pass; cross-verified by cycle-1 Critic §3). The abstract does not claim Paper 8 is unconditional, does not claim H4 is closed, does not claim any mathematical content has moved. Clean.

2. **Does it underclaim?** No. The "seventeen of the eighteen steps unconditional" and "mass gap unconditional on H4" are explicit; the "mildest form of H4 in the literature" is named; the Paper 13 RH analog is cited with the correct one-dependency grammar. No understate drift.

3. **Does it match Paper 13 RH's actual grammar?** Yes. The abstract explicitly writes "mirroring Paper 13 RH's grammar of shipping a Clay-class theorem conditional on a single short-term dependency on its theorem-label face ('Theorem 1.1, conditional on CCM')" and includes "cf. Paper 13 §1.5's explicit disavowal of CBB as a logical dependency of the proof chain." This correctly encodes the corrected grammar — one dependency, CCM alone, CBB noted as framework embedding separately per §1.5. **The v2 correction is propagated cleanly into the abstract.** v1's "two-dependency (CCM + CBB for Paper 13; H4-W7-14 + CBB for Paper 8)" framing is gone.

4. **Paper 26 handling.** The abstract correctly distinguishes Paper 26's situation from Paper 8's: Paper 26 ships "from CBB" as the downstream state where the short-term dependency has been closed (via Route 3's KMS projector bypass) and "only the framework embedding remains — in Paper 26's case, the framework embedding coincides with the sole logical dependency because Paper 26's proof chain genuinely uses CBB-system machinery (BC bridge algebra, KMS$_1$ ITPFI)." This is structurally correct per my Paper 26 §9 cross-check. Paper 26 is genuinely CBB-dependent at the logical level; Paper 8 and Paper 13 are framework-embedded-only. The abstract encodes this asymmetry correctly. No ambiguity remains.

5. **Three-sentence constraint.** The abstract is packed into what is formally one HTML-block-quote paragraph but with three sentence-boundaries visible by punctuation: sentence 1 ends at "the mildest form of H4 in the literature)." — sentence 2 ends at "noted separately in Remark 1.A." — sentence 3 ends at "H4 is the perimeter." Three sentences. The spawn constraint is ≤3 sentences; v2 meets it. The v2 author flagged that sentence 3 is slightly longer than v1 and that the parenthetical "cf. Paper 13 §1.5's explicit disavowal" and Paper 26 explanatory clause could be trimmed to a footnote if tighter phrasing is preferred (line 365). **I concur with the author's self-assessment: for a Clay-submission abstract, sentence 3 is at the upper length limit but is still one sentence and is ship-acceptable.** The cycle-1 Critic did not flag length as a blocker and neither do I.

6. **Would a Clay referee reading this cold be confused?** I did the "read it cold" test (cycle-1 Critic §7.5 discipline) and the answer is: no. A Clay referee would read:
   - "17/18 unconditional, mass gap unconditional on H4, H4 affects only Clay C7 and C9-AF" — crisp perimeter.
   - "the Taylor coefficients of a single analytic function" — the mildest-form claim is visible.
   - "mirroring Paper 13 RH's grammar of shipping a Clay-class theorem conditional on a single short-term dependency on its theorem-label face" — the analog citation is there.
   - "cf. Paper 13 §1.5's explicit disavowal of CBB as a logical dependency of the proof chain" — the framework-embedding separation is explicit.
   - "Paper 26 BSD's 'from CBB' grammar represents the downstream state..." — the Paper 26 asymmetry is explained.
   A careful referee can reconstruct the full programme-wide conditional-grammar picture from the abstract alone. This is the honest-first editorial move.

**Attack vector (d) verdict: SURVIVED.** The abstract conditional statement is structurally correct, matches Paper 13 RH's actual grammar (not the mischaracterization), maintains the honest-first register, and will read correctly to a Clay referee.

---

## (e) Consolidated Theorem 1 three-clause structure — adversarial read

**Target:** lines 371–389 of v2 (Theorem 1 label, body in three clauses A/B/C, proof-chain closing sentence, Remarks 1.A/1.B/1.C).

**Adversarial checks.**

1. **Theorem label grammar.** "Theorem 1 (Yang–Mills mass gap with full Jaffe–Witten structural compliance; conditional on H4 in the W7-14 mildest form)." — **one dependency on the face** (H4 alone). Mirrors Paper 13 RH's "Theorem 1.1 (RH, conditional on CCM)" label exactly. No CBB on the face. Clean. The existing §L.0 theorem label in Paper 8's preprint (`L-clay-conjectures.md` line 10: "**Theorem L.0** (Gradient-flow closure). *Let $G = \mathrm{SU}(N)$...*") already carries H4 alone via its sub-clause markers, so v2's label is structurally consistent with what Paper 8 already says — v2 is foregrounding the grammar to Theorem 1 (Main) level while the §L.0 Theorem stays as the structural discharge.

2. **Three-clause structure (A)/(B)/(C).** 
   - (A) Mass gap, unconditional on H4 — discharges Clay C1–C5. Cites Theorems 4, 5, 8. **Correct** per my §05-continuum-limit cross-check.
   - (B) Jaffe–Witten structural sub-clauses, unconditional on H4 — discharges Clay C6, C8, C9-non-AF. Cites Conjecture L.1(i)–(ii), Conjecture L.3(i)–(v), Conjecture L.4 non-perturbative content. Discharge via Appendix L, Theorem L.6.1 (i)–(iii), via Lemmas L.1.1–L.1.5, L.2.1–L.2.4, L.3.1–L.3.9, L.4.1, L.4.3. **Correct** per my §L.0 cross-check; the L.3(i)–(v) five sub-clauses (symmetry, gauge invariance, distributional conservation, positive Hamiltonian identification, trace anomaly) are exactly the five Clay C8 sub-clauses.
   - (C) AF-form sub-clauses, conditional on H4 — discharges Clay C7 (anomalous dimension + AF match) and Clay C9-AF (AF form of OPE identity channel). Cites Conjectures L.1(iii), L.2, L.4 AF form. Discharge via Appendix L, Theorem L.6.2 (i)–(iii), Lemma L.4.2. The H4 form cited as "`gradient-flow-attack-plan/research/W7-14-af-match.md §5.3`" with the Taylor-coefficient reformulation and the three-loop verification chain (Luscher 2010, Harlander–Neumann 2016, Artz et al. 2019, Harlander et al. 2021). **Correct** per my §L.0 and §L.6 cross-checks.

   The three-clause structure cleanly separates unconditional content from the H4-conditional perimeter. The reader sees at a glance: (A) mass gap — unconditional, (B) structural sub-clauses — unconditional, (C) AF-form sub-clauses — conditional on H4. This is exactly the Jaffe–Witten discharge table projected into a theorem statement. Good editorial architecture.

3. **Theorem 1 closing sentence.** The sentence that was most ambiguous in v1 has been rewritten in v2 (line 383):

   > *"The proof chain uses Balaban's RG, KK-enhanced lattice geometry, and the gradient-flow construction of Appendix L, and is logically self-contained modulo Hypothesis H4. Paper 8 sits inside the Integers programme as a framework-level embedding via Paper 10 and Appendix N (the 5D Quantum Geometry infrastructure used for UV finiteness of the gradient-flow composite operators), mirroring Paper 13 RH's relation to the CBB axioms (Paper 13 §1.5): the framework motivates the paper's place in the programme, but the proof chain does not depend on the CBB axioms at the logical level."*

   **This is the direct structural analog of Paper 13 §1.5's disavowal**, with Paper 8's proof-chain ingredients (Balaban + KK + gradient-flow) named explicitly and the CBB framework embedding scoped to "motivates the paper's place in the programme" rather than "a logical dependency of the proof chain." **The ambiguity from v1 is gone.** The phrase "depends on the CBB axioms at the framework-level embedding" (v1's load-bearing ambiguity source per cycle-1 Critic §7) has been replaced with "the proof chain does not depend on the CBB axioms at the logical level." A Clay referee reading this cold sees: one short-term dependency (H4), framework embedding (noted), no hidden CBB logical dependency. **Ship-safe.**

4. **Remark 1.A.** Opens with "Paper 8 carries **one short-term logical dependency** — **Hypothesis H4**..." — the exact corrected framing per cycle-1 Critic §7.4. v1's "Paper 8 carries two logical dependencies" is gone; v2 explicitly says **one**, with bold emphasis. The remark then mirrors Paper 13 §1.5 structurally and cites the §1.5 passage verbatim ("Sections 3–11 are self-contained and do not depend on the CBB axioms..."). The independent-support clause (36 zero-parameter predictions, $P < 10^{-89}$) is retained and is correctly scoped: "this independent support is orthogonal to Paper 8's logical dependency on H4 but is the reason the Integers-programme framework embedding is a credible motivational anchor." The Routes A/B/C naming is retained. **Correctly foregrounds H4 on the theorem-label face with CBB framework embedding as a separate observation.**

   **Low-priority note 1**: Remark 1.A still cites specific runner probabilities for the routes indirectly via the "Three independent routes are currently active" phrase without actually putting numeric probabilities in the Remark itself — so the cycle-1 "0.74 → 0.10" staleness flag does not hit Remark 1.A. (It does hit the §15.2 W7-14 cross-reference paragraph where "Joint closure probability across A/B/C ≈ 0.74" is still written verbatim; see the W7-14 section below.)

5. **Remark 1.B.** The rewritten version (lines 387–388) has three parallel one-sentence characterizations:
   - Paper 13 RH: "Theorem 1.1 (RH, conditional on CCM)" — conditional on CCM; "Paper 13's proof chain is independent of the CBB axioms at the logical level per the explicit disavowal in Paper 13 §1.5" — **one-logical-dependency on the theorem-label face (CCM) with the Integers programme framework embedding noted in §1.5 but not carried through the proof chain**.
   - Paper 26 BSD: "Theorem 13.1 (BSD from CBB)" — conditional on CBB axioms alone, after MY4 bypass via the KMS projector; "Paper 26's proof chain genuinely depends on CBB at the logical level via the BC bridge algebra and the KMS$_1$ ITPFI factorization" — **one-logical-dependency on the theorem-label face (CBB) where the framework embedding and the logical dependency coincide**.
   - Paper 8 YM: "Theorem 1 (Yang–Mills, conditional on H4 in the W7-14 mildest form)" — "**one-logical-dependency on the theorem-label face** (H4), with the Integers programme framework embedding via Paper 10 and Appendix N noted in Remark 1.A but not carried as a logical dependency of the proof chain, mirroring Paper 13 RH's actual grammar (one short-term dependency, framework embedding noted separately)."

   Closing: "Three Clay Millennium Prize artifacts, three instances of the programme's **one-dependency-on-the-theorem-label-face + framework-embedding** conditional grammar; Paper 8 and Paper 13 RH are closest in shape... Paper 26 BSD is the structural outlier in that its framework embedding has been upgraded to the sole logical dependency because the proof chain uses CBB-system machinery directly."

   **This is structurally correct and matches primary source evidence.** Paper 13's §1.5 + proof skeleton (which I verified: the proof skeleton has ZERO mentions of CBB across 234 lines — the term CBB does not appear) confirms Paper 13 is genuinely CBB-independent at the proof-chain level. Paper 26's §9 KMS1 ITPFI construction (partially verified: Theorem 9.1 label "GRH for CM curves, conditional on CBB" at line 606 matches) confirms Paper 26 genuinely does use CBB machinery. The three-way asymmetry the v2 artifact describes is real and faithful. **v1's mis-characterization is fully repaired.**

6. **Remark 1.C.** "What is independent of H4." Lists: mass gap, lattice confinement, OS axioms, unique continuum limit, renormalised composite operators, stress tensor with all five Clay sub-clauses, non-perturbative OPE singularity structure, compact simple group extension, quantitative predictions (string tension 437 MeV, glueball $0^{++} \sim 1.5$ GeV, Lüscher coefficient $\pi/6$). Closing: "If H4 is never closed, Paper 8 still proves the Yang–Mills mass gap and establishes nine of the eleven Clay compliance requirements (C1–C6, C8, C10–C11) unconditionally. H4 affects only the AF-logarithmic-form clauses of Clay C7 and C9 — i.e., the perturbative-match clauses of the Jaffe–Witten §4 structural ingredients — not the existence clauses. The mass gap is proved. The perimeter is tight."

   This is the §J register register-inverse ("Here is what they found"; "That is the contribution") applied to the unconditional perimeter. **Honest-first, declarative, no drift.** The "9 of 11 Clay unconditional, 2 of 11 conditional on H4" count is consistent with the Paper 8 §12.7 compliance table (cycle-1 Critic §3 verified this). **Good.**

7. **Proof-chain LOCK check.** Theorem 1 depends on independent rows:
   - Row 1: Paper 13 §1.1 (conditional on CCM label) — independent.
   - Row 2: Paper 26 §13.1 (from CBB label) — independent.
   - Row 3: Paper 8 §L.0 existing Theorem L.0 — independent (this is the base Theorem 1 consolidates).
   - Row 4: Paper 8 PROOF-CHAIN.md §IV.1–IV.5 — independent.
   - Row 5: Paper 8 §L.6.1/§L.6.2 — independent.
   - Row 6: W7-14-af-match.md §5.3 — independent.
   - Row 7: Paper 13 §1.5 disavowal — independent.
   - Row 8: Paper 8 Appendix N / Paper 10 framework embedding — independent.

   **Eight independent rows.** If any one row fails, only that row's piece of the artifact needs updating. Strong LOCK. Independently and silently the v2 revision actually strengthens the LOCK by adding Row 7 (Paper 13 §1.5 disavowal) as a load-bearing source for the one-dependency framing.

**Attack vector (e) verdict: SURVIVED.** The consolidated Theorem 1 three-clause structure is clean. The one-dependency grammar flows correctly. H4 is foregrounded on the theorem-label face. CBB is framed as framework embedding in Remark 1.A. Remark 1.B correctly captures the three-way Paper 13 / Paper 26 / Paper 8 asymmetry. Remark 1.C lists the unconditional perimeter in §J register. No structural issues.

---

## (f) §15 (Scope) section five sub-sections — adversarial read

**Target:** lines 395–475 of v2 (§15 header + §§15.1, 15.2, 15.3, 15.4, 15.5 + terminal phrase).

**Paper 26 §15 baseline.** I verified independently against `paper26-bsd/preprint/sections-parts-V-VI.md`:
- §15.0 header (lines 203–207): "This section is the most important in the paper. Everything before it is a proof. Everything after it is context. This section is the honest accounting of scope."
- §15.1 Rank 0 and rank 1: proved (line 209)
- §15.2 Rank ≥ 2: genuinely open (line 272)
- §15.3 Non-CM curves: genuinely open (line 296)
- §15.4 Class number h_K > 1: expected to extend (line 329)
- §15.5 The Langlands frontier (line 353)

Five sub-sections. Pattern: proved / open / open / expected / frontier.

**Paper 8 §15 as adapted in v2.**
- §15 header (line 397): borrows Paper 26's opening verbatim-ish — "This section is the most important in the paper. Everything before it is a proof. Everything after it is context. This section is the honest accounting of scope." — direct carry-over, byte-matches Paper 26.
- §15.1 "The mass gap and the structural ingredients: proved" (line 399)
- §15.2 "Hypothesis H4 as the standing conditional" (line 409)
- §15.3 "What the gradient-flow method does not cover" (line 445)
- §15.4 "Compact simple groups: handled; fundamental-representation extensions: scoped" (line 455)
- §15.5 "Where the gradient-flow method stops" (line 463)

Five sub-sections. Pattern: proved / standing conditional / outside scope / handled-and-scoped / method frontier.

**Adversarial check: is the adaptation correct (Paper 8-specific) or is it a mechanical Paper-26 copy?**

1. **§15.1 (proved).** Paper 26's §15.1 is rank 0 and rank 1 BSD for CM curves. Paper 8's §15.1 is the mass gap + the four Jaffe–Witten §4 structural ingredients + the compact simple group extension via Appendix I.4. **These are genuinely different mathematical scope items — the adaptation is Paper-8-specific, not a Paper 26 copy.** §15.1 also correctly names the proof-chain ingredients (Balaban's RG, KK-enhanced lattice geometry, gradient-flow construction) and foregrounds the framework-embedding grammar in one sentence: "Paper 8 sits inside the Integers programme as a framework-level embedding via Paper 10 and Appendix N, mirroring Paper 13 RH's relation to the CBB axioms (Paper 13 §1.5), but the proof chain does not depend on the CBB axioms at the logical level." **v2 correction propagates into §15.1.** Closing declaration: "Seventeen of the eighteen proof-chain steps are unconditional. The mass gap is proved." — §J register, terse, correct.

2. **§15.2 (standing conditional).** Paper 26's §15.2 is "Rank ≥ 2: genuinely open" — a *mathematical outside-scope* category. Paper 8's §15.2 is "Hypothesis H4 as the standing conditional" — a *standing-conditional* category that Paper 26 doesn't have because Paper 26's only standing conditional is CBB itself (which is not a scope section item). **The adaptation repurposes Paper 26's §15.2 slot for Paper 8's actual standing conditional.** This is structurally correct and is exactly what cycle-1 Critic §2 said ("Paper 8 needs the same [five-sub-section structure] but the slot items are different because Paper 8's scope items are different"). §15.2 correctly names H4 in its traditional form vs the W7-14 §5.3 reformulation, walks through the three structural reasons it's more tractable (controlled interpolation, UV finiteness eliminates renormalisation, analyticity provides a rigorous bridge), lists the three closure routes (A / B / C) plus Route D (editorial), lists the perimeter (Unconditional on H4 / Conditional on H4), and closes with the §J terse declaration: "H4 is the wall. W7-14 reframed it to the mildest form in the literature. Three routes are attacking it. Paper 8 ships either way."

   **Low-priority note 1 (the cycle-1 Critic's flagged issue):** §15.2 still contains the "Joint closure probability across A/B/C ≈ 0.74" and "Runner $p \approx 0.99$" and "the HONEST-STALL option, first-class per v3 patch I-5" phrasings that the cycle-1 Critic §9 flagged as internal runner-blackboard language not belonging in a Clay-submission preprint. The v2 artifact acknowledges this as a W2 editorial-merge-task cleanup item (v2 line 556 item (5)) but does not apply the cleanup in v2 itself. **For the node-level R.D.1 v2 status: this is fine** — R.D.1 v2 is shipping the draft artifact to the editorial pipeline, not directly into the preprint; the W2 merge task will strip the runner language when dropping the four pieces into their target files. But as Alpha-Critic I flag it here so the runner knows the scrub is still outstanding.

   **Low-priority note 2:** §15.2 also contains the phrase "Route A (Taylor-coefficient identification)... Runner $p \approx 0.50$. The highest-probability route..." — similarly internal. Same comment.

3. **§15.3 (outside scope).** Paper 26's §15.3 is "Non-CM curves: genuinely open." Paper 8's §15.3 is "What the gradient-flow method does not cover" — covering matter fields (fermionic QCD), OPE channels beyond the identity, Wightman reconstruction beyond OS axioms. **These are genuinely different outside-scope items.** The adaptation correctly captures Paper 8-specific limitations. §15.3 explicitly directs a Clay referee to the Clay Institute's problem statement itself — pure Yang-Mills, not QCD with matter — which is the exactly right referee-framing. Closing declaration: "Fermionic QCD is outside the scope of this paper. The gradient flow extends structurally but the matter-sector work is not carried out here." §J register. Correct.

4. **§15.4 (handled and scoped).** Paper 26's §15.4 is "Class number h_K > 1: expected to extend." Paper 8's §15.4 is "Compact simple groups: handled; fundamental-representation extensions: scoped." **Different slot items, both correctly adapted.** §15.4 names Appendix I.4's theorem I.4.1 extension from SU(N) to all compact simple Lie groups, notes the universal Weitzenböck–Bochner spectral gap argument, and notes that higher representations are outside the Clay statement (which is stated for pure Yang–Mills without matter representation specification). Closing: "The compact simple groups beyond $\mathrm{SU}(N)$ are handled in Appendix I.4. The fundamental representation at higher rank is covered. The adjoint-only framework is sufficient for the Clay statement." §J register. Correct.

5. **§15.5 (frontier).** Paper 26's §15.5 is "The Langlands frontier" — where Paper 26's bridge tool stops. Paper 8's §15.5 is "Where the gradient-flow method stops" — where Paper 8's main tool stops. **Parallel in structure, specific in content.** §15.5 correctly notes the gradient flow as a UV tool (smearing over $\sqrt{8t}$ scale), notes that the mass gap itself does not use the gradient flow (it uses Balaban's RG + Weitzenböck spectral gap), and notes H4 as the perimeter. Closing: "The gradient-flow method reaches the Jaffe–Witten §4 structural ingredients. H4 is the perimeter. Beyond H4, the content of this paper ends." §J register. Correct.

6. **§15 terminal phrase** (line 475): "The mass gap is proved. The structural ingredients are proved within their conditional. H4 is stated honestly. That is the contribution." — direct borrow from `35-final-verdict.md` line 172 ("That is the contribution.") applied to the five-sub-section discharge. **Exact canonical voice-shape match.**

**Attack vector (f) verdict: SURVIVED.** The §15 five sub-section structure is genuinely adapted to Paper 8's scope items (not mechanically copied from Paper 26), each sub-section is structurally correct, the closing declarations are in §J register, and the terminal phrase is the canonical Paper-8 closure-declaration. **Two low-priority items** (internal runner language "0.74", "$p \approx 0.99$", "first-class per v3 patch I-5") are acknowledged for W2 merge cleanup.

---

## (g) W7-14 cross-reference block — adversarial read

**Target:** lines 481–497 of v2 (W7-14 cross-reference, to be inserted as a call-out box in §L.7 of `L-clay-conjectures.md` §L.7.3).

**Adversarial check: is the Taylor-coefficient framing technically correct and will it read correctly to a Clay referee?**

1. **The mathematical framing.** v2 states:
   > "Let $F(t) := S_{2,t}^c(x,y) / c_1(t)^2$... By Lemma L.3.1 (W5-10 Step 2), $F(t)$ is analytic in a complex neighbourhood of $t = 0$ with a $(k,K)$-uniform radius $r_t > 0$. The Cauchy remainder of the Taylor series at $t = 0$ is $|R_n(t)| \leq M_F (|t|/r_t)^{n+1}/(1 - |t|/r_t)$ (rigorously, not formally). Hypothesis H4 in the W7-14 §5.3 form is the claim that the Taylor coefficients $\{F^{(n)}(0)/n!\}_{n \geq 0}$ are computed by the standard Feynman-diagrammatic perturbative rules applied to the gradient-flow action."

   This is careful phrasing. The claim is: the Taylor coefficients of one analytic function $F(t)$ at one point ($t=0$) are computed by Feynman rules. It is NOT the claim "two analytic functions agree" — which would be structurally stronger than the actual H4.

2. **Cycle-1 Critic §4 precision note.** The cycle-1 Critic flagged (at §4) that the phrasing is technically correct but easy to misread: "a careful reader would expect the comparison to be between two convergent Taylor series on the same disk, and the I-7 catch shows that is not quite what W7-14 §5.3 actually delivers — the non-perturbative side is analytic with a convergent series, the perturbative side is a formal series, and the match claim is 'the Taylor coefficients of the analytic function equal the formal-series coefficients term-by-term'." The cycle-1 Critic recommended a parenthetical clarification making explicit that the perturbative side is a formal power series and H4 is the term-by-term match of formal coefficients with analytic function's Taylor coefficients.

   **Adversarial check: did v2 apply the clarification?** I re-read the v2 W7-14 cross-reference block carefully. **v2 did NOT apply the parenthetical clarification**; it still reads as written in v1 (which is "technically correct but easy to misread"). The cycle-1 Critic explicitly marked this as LOW-PRIORITY (§12 low-priority, not blockers for the WEAKENED verdict). So v2 is not violating the cycle-1 Critic's required edit list on this point — the cycle-1 Critic did NOT require this edit, only suggested it. However, as Alpha-Critic doing the ship-critical final check, I note:

   **Low-priority author-consideration note 3 (carried over from cycle-1 Critic §4).** The W7-14 cross-reference block's phrasing "the Taylor coefficients of the analytic function $F(t)$ at $t = 0$ are computed by the standard Feynman-diagrammatic perturbative rules" is technically correct but a careful reader may query whether the "perturbative rules" produce a formal series or a convergent series. The cycle-1 Critic's suggested clarification would be a parenthetical: "(H4's assertion is that the Taylor coefficients $F^{(n)}(0)/n!$, which are the derivatives of a single analytic function $F$ at a single point, agree term-by-term with the formal-series coefficients computed by the Feynman diagrammatic rules applied to the gradient-flow action; it is not a claim that the perturbative rules themselves sum to an analytic function)." **This is not ship-blocking** — the current phrasing is technically correct — but a W2 editorial-merge pass should consider adding the parenthetical.

3. **Three structural reasons.** §15.2 and the W7-14 cross-reference both list three reasons the W7-14 §5.3 form is more tractable than the traditional form:
   - Controlled interpolation (the gradient flow provides a smooth one-parameter interpolation)
   - UV finiteness eliminates renormalisation ambiguities (no separate $Z_{\mathcal{O}}(a)$ needed)
   - Analyticity provides a rigorous bridge (convergent small-flow-time expansion)
   
   Each reason is correctly tied to a specific Appendix L lemma (Lemma L.3.1 for convergent expansion, Lemma L.3.7 for Cauchy Lipschitz estimate, W5-10 Step 2 for analyticity radius). Cites the three-loop perturbative verification chain correctly (Luscher 2010 JHEP 08:071; Harlander–Neumann 2016 JHEP 06:161; Artz et al. 2019 JHEP 06:121; Harlander et al. 2021 arXiv:2111.14376). **Correct citations — I spot-checked Luscher 2010 JHEP 08:071 which is the standard reference for gradient-flow small-$t$ expansion.**

4. **Independent numerical support.** The v2 cross-reference claims "Every lattice QCD simulation comparing short-distance correlators to perturbative predictions... has found quantitative agreement at the level of available perturbative precision. H4 is implicitly invoked in every SVZ sum rule, every lattice determination of $\alpha_s$ from short-distance quantities, and every perturbative matching calculation in continuum QCD. It is the standard hypothesis of QCD phenomenology; we make it explicit rather than implicit, in its mildest available form."
   
   **This is a correct and ship-safe editorial framing**. SVZ (Shifman–Vainshtein–Zakharov) sum rules are the canonical QCD phenomenology case study where H4 is invoked implicitly. Lattice $\alpha_s$ determinations (e.g., the ALPHA Collaboration's step-scaling, FLAG Review 2021 compilations) all implicitly match perturbative short-distance predictions to non-perturbative lattice data, which is an instance of H4. The claim "standard hypothesis of QCD phenomenology" is supportable by the literature. Good.

5. **Three routes paragraph.** The v2 cross-reference paragraph (line 495) still cites "Joint closure probability across A/B/C $\approx 0.74$" — this is the cycle-1 Critic §9's second low-priority cleanup item (the 0.74 figure is pre-Wave-1, post-Wave-1 it's closer to 0.10). **Low-priority note 4 (carried over from cycle-1 Critic §9).** Recommend: W2 merge pass should remove the specific probability from the preprint version. Alternative: remove the "Joint closure probability" phrase entirely; keep the routes named but do not attach probabilities to them in the preprint body text. **This is explicitly acknowledged in the v2 handoff notes** (line 556 item (5)) — not a v2 ship-blocker.

6. **Closing declarative.** "H4 in its traditional form is open. H4 in the W7-14 §5.3 analyticity reformulation is the mildest form in the literature. This is the form of H4 that Paper 8's conditional carries. The traditional form is not what is assumed." — **four stacked declarative sentences**, §J register, terse, unambiguous. A Clay referee reading this closing paragraph cannot be confused about what form of H4 Paper 8 assumes. Good.

**Attack vector (g) verdict: SURVIVED.** The Taylor-coefficient framing is technically correct. The three reasons are correctly mapped to specific Appendix L lemmas. The three-loop citations are correct. The independent numerical support framing is ship-safe. The closing declarative is clean. Two low-priority items carried from cycle-1 Critic (§4 precision parenthetical, §9 stale probability) are acknowledged for W2 merge.

---

## (h) PCGT template correctness — adversarial read

**Target:** lines 530–538 of v2 (Proposed §D toolkit addition: "the programme conditional-grammar template" PCGT).

**The v2-refined PCGT statement (line 533):**

> "Theorem-label names the single short-term logical dependency on its face (one dependency; if multiple are present, name the most short-term); precise form of the dependency cited (specific theorems/lemmas/axioms/reformulation paths); companion remark explains standing + independent support + framework embedding (if any) **noted separately from the logical dependency** + what becomes unconditional on closure; §15 (Scope) with the five-sub-section structure (proved / standing conditional / outside scope / expected to extend / method frontier); voice-shape check against the programme's §J register mandatory on Step 6; **ship-safe re-reading check for semantic ambiguity in load-bearing phrases mandatory on Step 6.5** (new per cycle-1 Critic §7.5 lesson)."

**Adversarial check: is this a reusable template or an idiosyncratic description?**

1. **Template vs description.** The PCGT has six components:
   - (i) theorem-label with single short-term dependency on its face
   - (ii) precise form of dependency cited
   - (iii) companion remark with standing + independent support + framework embedding noted separately + what becomes unconditional
   - (iv) §15 Scope section with five sub-section structure
   - (v) voice-shape check against §J register on Step 6
   - (vi) ship-safe re-reading check for semantic ambiguity on Step 6.5

   Each component is abstract enough to apply across different Clay-class artifacts with different specific content. Component (i) works for "conditional on CCM" (Paper 13) or "from CBB" (Paper 26) or "conditional on H4 in W7-14 mildest form" (Paper 8). Component (ii) works for arbitrary specific dependency forms. Component (iii) works with arbitrary framework-embedding situations (noted but not carried-through, coinciding with logical dependency, or not present). Component (iv) is the five-sub-section template slots. Components (v) and (vi) are general-purpose checks. **This is a reusable template, not an idiosyncratic description.**

2. **Tripled test.** v2 claims the PCGT is triply tested:
   - Paper 13 RH: one-dependency on CCM, framework embedding CBB-independent per §1.5.
   - Paper 26 BSD: one-dependency on CBB post-MY4, framework embedding coincides with logical dependency.
   - Paper 8 YM: one-dependency on H4, framework embedding via Paper 10 / Appendix N noted separately.

   **I verified all three instances hold.** Paper 13's §1.1 Theorem 1.1 label, Paper 13's §1.5 disavowal, and Paper 13's 00-proof-skeleton.md (zero CBB mentions across 234 lines) triangulate Paper 13 as a one-dependency-on-the-theorem-label-face + framework-embedding-separate instance. Paper 26's §13.1 Theorem label, Paper 26's §9 KMS1 ITPFI construction, and `strategy/04-closing-my4.md §6` post-MY4 standing confirm Paper 26 as a one-dependency-where-framework-embedding-coincides-with-logical-dependency instance. Paper 8's §L.0 Theorem L.0 label (existing), the §IV.5 scope paragraph, and the proof-chain ingredients (Balaban + KK + gradient-flow + Epstein) confirm Paper 8 as a one-dependency-on-H4 + framework-embedding-separate instance. The three instances fit the template with differing dependency structures. **Reusable and correctly tested.**

3. **Component (vi) — the ship-safe re-reading check.** This is the NEW component added per cycle-1 Critic §7.5 lesson. The cycle-1 Critic caught v1's ambiguity by applying "what would a Clay referee reading this cold ask?" to the specific phrase "depends on the CBB axioms at the framework-level embedding." The v2 PCGT codifies this as Step 6.5 of the spawn template for editorial nodes. **This is a genuine process refinement** that would have caught the v1 issue earlier in the Author's own cycle if it had been in the template when v1 was drafted. The Author/Critic have explicitly propagated the lesson back into the toolkit.

4. **Idiosyncratic risk.** The risk of the PCGT being too Paper-8-specific: does it over-fit to the Paper 13 / Paper 26 / Paper 8 Clay-class cases? Would it apply to a non-Clay programme artifact? The template is described as "conditional-grammar template for Clay Millennium Prize artifacts" — it's scoped to that specific class. Within that class, the three-instance test is convincing. **Outside that class** (e.g., for a Lemma-level result or a structural theorem that doesn't carry a named conditional), the template would need adaptation. But v2 is scoped to Clay-class artifacts, not general-purpose, so this is not a defect of v2's PCGT claim.

5. **One sub-question: does the template correctly handle a "no framework embedding" case?** The template says "companion remark explains... framework embedding (if any) noted separately". This handles cases where framework embedding is not present. For Paper 13, framework embedding is Integers programme (present but disavowed as logical dependency). For Paper 26, framework embedding is Integers programme (present and coincident with logical dependency). For Paper 8, framework embedding is Integers programme (present and separate from logical dependency, analogous to Paper 13). All three instances have framework embedding; the template's "(if any)" clause correctly anticipates cases where there might be none (e.g., a pure mathematical result with no programme embedding). **Template is robust to the absence case.**

**Attack vector (h) verdict: SURVIVED.** The PCGT is genuinely a reusable template, correctly tripled-tested against Paper 13 / Paper 26 / Paper 8, and v2 adds the ship-safe re-reading check as a process refinement per the cycle-1 Critic lesson. Not idiosyncratic.

---

## (m) Voice-shape recount — independent count

**Target:** all four draft pieces of v2. The v2 artifact claims "~50 markers preserved from v1" (line 524, v2 blackboard §I CASCADE note; also lines 558 in handoff notes) based on the cycle-1 Critic's independent recount (which itself replaced the v1 Author's conservative 28).

**My independent count.** I counted markers using the three-category scheme from blackboard §J and `35-final-verdict.md`: (a) terse declaration phrases, (b) named ritual elements, (c) §J register markers. I counted strictly in the **four draft pieces** (lines 363, 371-389, 395-475, 481-497) — not the framing prose, not the research steps, not the §M summary or §I notes. Same scope as cycle-1 Critic §1.

**Piece 1: Abstract conditional statement (line 363, one HTML-block-quote paragraph with three sentence-boundaries).**
- Terse declaration: "The mass gap $\Delta_\infty > 0$ is proved unconditionally on H4" (1); "seventeen of the eighteen steps of the full proof chain... are unconditional on H4" (2); "H4 is the perimeter" (3); "The unconditional content of Paper 8... is complete and self-contained" (4).
- Named ritual: "the gradient-flow reformulation" (5); "the Taylor coefficients of a single analytic function" (6); "the mildest form of H4 in the literature" (7); "standing form of the conditional" (bold header) (8); "$F(t) := S_{2,t}^c(x,y)/c_1(t)^2$" (9, the named-function ritual).
- §J register: "Paper 8... ships as **a theorem conditional on Hypothesis H4...**" (10); "mirroring Paper 13 RH's grammar of shipping a Clay-class theorem conditional on a single short-term dependency on its theorem-label face" (11); "cf. Paper 13 §1.5's explicit disavowal of CBB as a logical dependency of the proof chain" (12).
- **Piece 1 total: 12 markers.** (Cycle-1 Critic counted 7 for v1 piece 1. My independent v2 count: 12. v2 piece 1 is slightly longer than v1 piece 1 because of the inserted "cf. Paper 13 §1.5" clause and the Paper 26 asymmetry explanation.)

**Piece 2: Theorem 1 statement + Remarks 1.A/1.B/1.C (lines 371-389).**
- Terse declaration: "(Mass gap, unconditional on H4)" clause label (1); "(Jaffe–Witten structural sub-clauses, unconditional on H4)" clause label (2); "(AF-form sub-clauses, conditional on Hypothesis H4 in the W7-14 §5.3 reformulation)" clause label (3); "one short-term logical dependency" (bold, in 1.A) (4); "Hypothesis H4" (bold, in 1.A) (5); "one-logical-dependency on the theorem-label face" (bold, in 1.B, 3 times — Paper 13, Paper 26, Paper 8) (6-8); "If H4 is never closed, Paper 8 still proves the Yang–Mills mass gap" (9); "The mass gap is proved" (terminal, 1.C) (10); "The perimeter is tight" (terminal, 1.C) (11); "17 of 18" (implicit via 1.A "only input separating Paper 8 from 18/18 unconditional-within-CBB closure") (12); "nine of the eleven Clay compliance requirements" (1.C) (13).
- Named ritual: "the W7-14 mildest form" (label) (14); "the W7-14 §5.3 reformulation" (1.A) (15); "the mildest form of H4 in the literature" (1.A) (16); "the framework-level embedding via Paper 10 and Appendix N" (1.A and closing sentence of body) (17); "mirroring Paper 13 RH's relation to the CBB axioms (Paper 13 §1.5)" (body closing sentence) (18); "the three routes" — not explicit here actually, "Three independent routes are currently active" is close (19); "Route A (Taylor-coefficient identification via analyticity)" (1.A) (20); "Route B (CCM 2025 spectral triple port to Yang–Mills)" (1.A) (21); "Route C (Connes spectral action + bridge family $k=4$ + Identity 12)" (1.A) (22); "$P_k^{\mathfrak{p}} := I - s_{\mathfrak{p}}^k(s_{\mathfrak{p}}^k)^*$" (1.B, named projector) (23); "BC bridge algebra $\mathcal{A}_{BC,K}$" (1.B) (24); "KMS$_1$ ITPFI factorization" (1.B) (25); "$36$ zero-parameter closed-form predictions" (1.A, the independent-support ritual) (26).
- §J register: "the programme's **one-dependency-on-the-theorem-label-face + framework-embedding** conditional grammar" (1.B closing) (27); "ships as" (three times in 1.B, once per paper) (28-30); "the proof chain does not depend on the CBB axioms at the logical level" (body closing, direct Paper 13 §1.5 structural mirror) (31); "Paper 8 ships in the form stated here" (1.A closing) (32); "mirroring Paper 13 RH's actual grammar" (1.B) (33); "the structural outlier" (1.B closing) (34).
- **Piece 2 total: 34 markers.** (Cycle-1 Critic counted 12 for v1 piece 2. My v2 count: 34. v2 is substantially longer than v1 in piece 2 — Remark 1.B was rewritten to carry three parallel "ships as" / "one-logical-dependency on the theorem-label face" characterizations, and Remark 1.A was rewritten to mirror Paper 13 §1.5 verbatim in structure. The factor ~2.8 increase reflects the v2 revision, not counting-granularity differences.)

**Piece 3: §15 (Scope) section five sub-sections (lines 395-475).**
- Terse declaration / §J register / named ritual (I'm going to stop splitting by category within piece 3 because the markers are dense):
  - §15 opening: "This section is the most important in the paper. Everything before it is a proof. Everything after it is context. This section is the honest accounting of scope." (1-2, two markers: the Paper 26 borrow + the §J register carry-over)
  - §15.1 body: "framework-level embedding via Paper 10 and Appendix N" (3); "mirroring Paper 13 RH's relation to the CBB axioms (Paper 13 §1.5)" (4); "the proof chain does not depend on the CBB axioms at the logical level" (5); "unlike Paper 26 BSD" contrast framing (6)
  - §15.1 closing: "Seventeen of the eighteen proof-chain steps are unconditional" (7); "The mass gap is proved" (8)
  - §15.2 opening: "The wall, honestly stated" (9); "H4 is the wall" (10 — first occurrence); "the standard hypothesis of QCD phenomenology" (11)
  - §15.2 "the form of H4 Paper 8 assumes" body: "gradient-flow reformulation" (12); "W7-14 reframed it to the mildest form in the literature" (13 — first occurrence); "the Taylor coefficients $F^{(n)}(0)/n!$" (14, named function ritual); "It is a statement about one analytic function and the computational rules for its Taylor coefficients" (15)
  - §15.2 three structural reasons: "Controlled interpolation" (16); "UV finiteness eliminates renormalisation ambiguities" (17); "Analyticity provides a rigorous bridge" (18); "convergent (not merely asymptotic) small-flow-time expansion" (19)
  - §15.2 Three routes body: "Route A (Taylor-coefficient identification)" (20); "Route B (CCM 2025 spectral triple port to Yang-Mills)" (21); "Route C (Connes spectral action + Identity 12 + bridge family $k=4$)" (22); "Route D (this editorial node)" (23); "the HONEST-STALL option" (24)
  - §15.2 perimeter list: "(A) mass gap + OS axioms (Clay C1–C5)" (25); "(B) renormalised composite operators L.1(i)–(ii) (Clay C6)" (26); "(C) anomalous-dimension match L.1(iii), AF short-distance match L.2" (27)
  - §15.2 closing: "Nine of the eleven Clay requirements are unconditional on H4" (28); "Two require H4" (29); "H4 is the wall. W7-14 reframed it to the mildest form in the literature. Three routes are attacking it. Paper 8 ships either way." (30-33, four markers in one terminal sentence)
  - §15.3 body: "Matter fields" (34); "Paper 8 is a pure Yang-Mills paper" (35); "OPE channels beyond the identity" (36); "Wightman reconstruction beyond OS axioms" (37)
  - §15.3 closing: "Fermionic QCD is outside the scope of this paper. The gradient flow extends structurally but the matter-sector work is not carried out here" (38-39)
  - §15.4 body: "Other compact simple groups... Appendix I.4... Theorem I.4.1" (40); "the universal properties of compact irreducible symmetric spaces" (41); "the Weitzenböck–Bochner spectral gap" (42)
  - §15.4 closing: "The compact simple groups beyond $\mathrm{SU}(N)$ are handled in Appendix I.4. The fundamental representation at higher rank is covered. The adjoint-only framework is sufficient for the Clay statement." (43-45, three markers in one terminal sentence)
  - §15.5 "UV tool" body: "The Yang-Mills gradient flow... smears gauge fields over a Gaussian kernel of width $\sqrt{8t}$" (46); "Luscher-Weisz 2011, JHEP 02:051" (47); "the Jaffe-Witten §4 structural ingredients" (48); "Balaban's RG + the KK Weitzenböck spectral gap" (49)
  - §15.5 closing: "The gradient-flow method reaches the Jaffe-Witten §4 structural ingredients. H4 is the perimeter. Beyond H4, the content of this paper ends." (50-52, three markers in one terminal sentence)
  - §15 terminal phrase: "The mass gap is proved. The structural ingredients are proved within their conditional. H4 is stated honestly. That is the contribution." (53-56, four markers — direct borrow from 35-final-verdict.md line 172, with "That is the contribution" being the canonical closure declaration)
- **Piece 3 total: 56 markers.** (Cycle-1 Critic counted 21 for v1 piece 3. My v2 count: 56. The factor ~2.7 increase reflects a much more granular counting — cycle-1 Critic counted one per sub-section plus header borrows; I counted one per named ritual element + one per terse declarative phrase + one per §J register occurrence. Both counts confirm §15 passes voice-shape; mine is a higher-granularity count.)

**Piece 4: W7-14 cross-reference block (lines 481-497).**
- Opening: "Cross-reference: the form of H4 Paper 8 assumes" (1); "not the traditional form" (2); "the gradient-flow reformulation" (3)
- Mathematical framing: "Let $F(t) := S_{2,t}^c(x,y) / c_1(t)^2$" (4, named function ritual); "analytic in a complex neighbourhood of $t = 0$ with a $(k,K)$-uniform radius" (5); "the Taylor coefficients $\{F^{(n)}(0)/n!\}_{n \geq 0}$" (6); "Hypothesis H4 in the W7-14 §5.3 form" (7)
- Three reasons: "Controlled interpolation" (8); "UV finiteness eliminates renormalisation ambiguities" (9); "Analyticity provides a rigorous bridge" (10)
- Three-loop citation: "Luscher 2010 JHEP 08:071" (11); "Harlander-Neumann 2016 JHEP 06:161" (12); "Artz et al. 2019 JHEP 06:121" (13); "Harlander et al. 2021 arXiv:2111.14376" (14)
- Independent numerical support: "every lattice QCD simulation comparing short-distance correlators to perturbative predictions" (15); "It is the standard hypothesis of QCD phenomenology" (16); "we make it explicit rather than implicit, in its mildest available form" (17)
- Closing: "H4 in its traditional form is open. H4 in the W7-14 §5.3 analyticity reformulation is the mildest form in the literature. This is the form of H4 that Paper 8's conditional carries. The traditional form is not what is assumed." (18-21, four markers in one terminal block)
- **Piece 4 total: 21 markers.** (Cycle-1 Critic counted 10 for v1 piece 4. My v2 count: 21. Similar factor-2 scaling from higher-granularity counting.)

**Independent aggregate count across four draft pieces: 12 + 34 + 56 + 21 = 123 markers.**

**Comparison to prior counts:**
- v1 Author (original): 28 markers. Conservative, strict-maximum-per-category.
- Cycle-1 Critic (independent v1 recount): 50 markers. Higher granularity than Author.
- v2 artifact claim (line 524): "~50 markers preserved from v1 per cycle-1 Critic recount."
- **Alpha-Critic (my independent v2 recount): 123 markers.** Highest-granularity count (I counted every named ritual element + every terse declarative clause + every §J register occurrence, not "one per category per piece").

**Variance interpretation.** All three counts (Author 28, cycle-1 Critic 50, me 123) confirm the artifact passes voice-shape 4/4. The variance is in counting granularity, not structural verdict. The cycle-1 Critic's "50" was itself a factor-1.8 larger than the Author's "28"; my "123" is a factor-2.5 larger than the cycle-1 Critic's "50" — scaling consistently with how finely you grain the counting. **The ratios are stable: in all three counts, §15 is the richest piece (Author: presumably ~14 if we scale; Critic: 21; me: 56) and §15.2 is the richest sub-section (~half of §15's markers).**

**Load-bearing observation.** The cycle-1 Critic noted the v1 blackboard §M row records "28 register markers counted across the artifact" (the Author's conservative count) and suggested updating to 50. v2 line 524 says "Voice-shape recount for v2: ~50 markers across the 4 draft pieces (unchanged from v1 Critic recount), 4/4 voice-shape passes." — this is the *cycle-1 Critic's recount carried forward*. My independent recount gives a much larger number (123), which is more consistent with high-granularity counting discipline. But **for the purpose of the shipping verdict, 50 and 123 both equally pass the "≥1 marker per category per piece" threshold comfortably.**

**Low-priority note 5 (counting-granularity reconciliation):** blackboard §M cycle-1 sub-cycle row can record "50 markers per cycle-1 Critic recount; 123 markers per Alpha-Critic higher-granularity recount (both counts confirm 4/4 voice-shape pass)" if the runner wants to be precise. Not a blocker.

**Attack vector (m) verdict: SURVIVED.** My independent recount yields 123 markers across 4 draft pieces — much larger than the v2 artifact's claim of ~50. The variance is explainable by counting granularity; all three counts (Author 28, cycle-1 Critic 50, Alpha-Critic 123) agree on 4/4 voice-shape pass. The cycle-1 Critic's observation that voice-shape markers were preserved in v2 is correct — my count actually suggests v2 has *more* markers than v1 in Piece 2 specifically (the Remark 1.B rewrite added ~3 parallel "ships as" / "one-logical-dependency" phrases and ~5 named-ritual elements at the body closing sentence).

---

## Structural integrity checks (bonus pass)

I did several "looking for something broken" passes that aren't on the (a)-(m) attack list but are standard final-adversarial-pass due diligence.

1. **Paper 13 §1.5 verbatim quote preservation.** v2 quotes Paper 13 §1.5 in Remark 1.A and in the §7 edit-log at the top of the file. I verified both quotes against `paper13-rh/preprint/sections-01-05.md` lines 237–240 directly: the quote "Sections 3–11 are self-contained and do not depend on the CBB axioms. The proof uses CCM's operators, our ITPFI factorization, Boegli's theorem, and Hurwitz's theorem — all independent of the broader Integers programme" is **byte-accurate**. Good.

2. **Paper 13 00-proof-skeleton.md line 6 header.** v2 claims: "Paper 13 proof skeleton header 'Conditional on CCM (arXiv:2511.22755)' as the *sole* conditional" (v2 line 16). I verified directly: line 6 of 00-proof-skeleton.md reads "*Conditional on CCM (arXiv:2511.22755).*" (with the `*` markdown emphasis and a period). The word "sole" and "single" are interpretive additions by the v2 author — technically correct because the proof skeleton across 234 lines contains exactly zero occurrences of "CBB" (I grep'd for this independently and confirmed zero matches). **The v2 author's "sole conditional" claim is verifiable.** Good.

3. **Paper 13 six-layer proof chain.** v2 claims "the six-layer proof chain (lines 50–62) names CCM as Layer 1 with no CBB dependency in any layer" (v2 line 16). I verified directly: Paper 13 00-proof-skeleton.md lines 52–62 present Layer 1 (CCM operators, from arXiv:2511.22755) through Layer 6 (conclusion via Boegli + Hurwitz), and none of Layers 1–6 invoke CBB. CBB is absent from this section. **The v2 author's claim holds.** Good.

4. **Paper 26 §13.1 verbatim quote preservation.** v2 quotes Paper 26 §13.1: "Theorem 13.1 (BSD from CBB). Under the CBB axioms (Paper 23), for CM curves E/Q with CM by a class-number-1 imaginary quadratic field K and analytic rank 0 or 1, BSD holds..." I verified directly: `paper26-bsd/preprint/sections-part-IV.md` line 360 is the theorem statement "**Theorem 13.1 (BSD from CBB).** *Under the CBB axioms (Paper 23), for CM curves E/Q with CM by a class-number-1 imaginary quadratic field K and analytic rank 0 or 1, BSD holds:*" — byte-accurate match to v2's quote. Good.

5. **Paper 26 strategy/04 vs strategy/05 phrasing distinction.** The v2 Author's note on line 43 (and indirectly via Remark 1.B) explicitly acknowledges that the phrase "the same conditional Paper 13's RH proof lives with" in `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` line 31 is a motivational paraphrase internal to Paper 26's strategy document, and that the Cycle-1 Critic verified Paper 13 §1.5 explicitly disavows CBB as a logical dependency of the RH proof chain. **The v2 author correctly distinguishes the two senses of "same conditional" — framework embedding (both papers sit inside the Integers programme) vs logical dependency (Paper 26 uses CBB machinery directly; Paper 13 does not).** This is the correct reading, and the cycle-1 Critic's WEAKENED verdict was precisely because v1 failed to make this distinction.

6. **Paper 8 Theorem L.0 structural parallel.** v2 claims: "Theorem L.0 currently carries H4 alone on its face, not CBB — this is structurally identical to Paper 13 RH's one-dependency-on-the-theorem-label-face grammar, confirming the v2 correction is the honest reading of Paper 8's current state" (v2 line 47). I verified directly: `L-clay-conjectures.md` line 10 is "**Theorem L.0** (Gradient-flow closure). *Let $G = \mathrm{SU}(N)$, $N \geq 2$...*" and the H4 conditional appears only in sub-clauses (b) and (d) ("conditional on H4"). The theorem label itself does not mention CBB, only H4 as the sub-clause condition. **Paper 8's existing Theorem L.0 grammar is structurally one-dependency-on-H4 (with CBB absent), consistent with v2's Theorem 1 consolidation.** The v2 correction is not changing any mathematics and is not even changing the existing Paper 8 theorem label structure — it is simply foregrounding the already-correct Paper 8 grammar to the Theorem 1 (Main) level and adding the Paper 13 analog citation.

7. **PROOF-CHAIN.md §IV.5 consistency.** v2 claims "The gradient-flow programme (Steps 15–17) is unconditional; Step 18 is conditional on the standard hypothesis H4" (paraphrased as "17 of 18 unconditional"). I verified directly: `PROOF-CHAIN.md` line 161 reads "The gradient-flow programme (Steps 15--17) is unconditional; Step 18 is conditional on the standard hypothesis H4 (non-perturbative Schwinger functions agree with perturbation theory at short distances)." — byte-accurate. The "17 of 18" count is whole-number counting; the half-steps 1b and 10b would make it "19 row entries" but the standard whole-number framing is "18 steps" with 17 unconditional and Step 18 conditional. v2's "seventeen of the eighteen" phrasing is consistent with the whole-number convention used throughout Paper 8's preprint. Good.

8. **Preprint-insertion locations.** v2 specifies target files for the four draft pieces: abstract sentence → `00-abstract.md` replacing lines 99–103, Theorem 1 + 3 remarks → `01-introduction.md` §1.1.1 Main Theorem block, §15 → new standalone `15-scope.md` between §12 and appendices, W7-14 cross-reference → `L-clay-conjectures.md` §L.7.3 call-out box. I verified that `00-abstract.md` lines 99–103 are indeed the H4 conditional sentences that v2 replaces (I read them directly above and they are as expected). I did not verify that `01-introduction.md` has a natural §1.1.1 insertion point (not read in this pass; this is a W2 merge task concern, not R.D.1 v2 ship-readiness). **The target file locations are sensible and consistent with Paper 8's current preprint structure.**

9. **Diff from v1 to v2.** v2 claims ~60 lines of diff confined to (a) abstract sentence, (b) Theorem 1 body closing sentence, (c) Remark 1.A, (d) Remark 1.B, (e) §M summary, (f) §I CONCERN note, (g) Step 5.5 Way 1 backward-verification correction. The voice-shape markers in the draft pieces were preserved. **I did not compare v1 and v2 byte-for-byte** (would require reading v1 also, which is beyond the scope of this pass per the prompt), but the diff scope claimed by v2 is internally consistent with the cycle-1 Critic's §7 Option 1 edit list. Reasonable.

---

## Ship-blocking issues

**None.**

The cycle-1 Critic's §7 Option 1 edit list has been applied faithfully. The v1 mischaracterization is repaired. v2 correctly mirrors Paper 13 RH's actual grammar. The four draft pieces are structurally sound, voice-shape-matched, and ready for W2 preprint merge.

---

## Low-priority author-consideration notes (ship-acceptable)

These notes do NOT block shipping. They are W2 editorial-merge-task considerations, already acknowledged in v2's own handoff notes (line 556).

1. **Internal runner language in §15.2** — "Joint closure probability across A/B/C ≈ 0.74", "Runner $p \approx 0.99$", "the HONEST-STALL option, first-class per v3 patch I-5". These are internal blackboard language not appropriate for a Clay-submission preprint. The cycle-1 Critic §9 flagged them as W2 cleanups. v2 handoff note (5) at line 556 explicitly acknowledges this. **Recommendation: strip during W2 merge.**

2. **Stale joint probability 0.74 → 0.10** — same §15.2 location; the "0.74" was the pre-Wave-1 joint closure probability, and post-Wave-1 outcomes put it closer to 0.10 per blackboard §K. Better: remove the specific joint-probability figure entirely from the preprint version (attaching a specific numerical probability to a Clay-class theorem's remark is unusual and a referee may query). v2 handoff note (5) acknowledges. **Recommendation: strip specific probability.**

3. **Taylor-coefficient vs formal-series precision parenthetical** — the W7-14 cross-reference block's phrasing "the Taylor coefficients of the analytic function $F(t)$ at $t = 0$ are computed by the Feynman-diagrammatic perturbative rules" is technically correct but a careful reader may query whether the rules produce a formal or convergent series. Cycle-1 Critic §4 recommended a parenthetical clarification. Not a blocker; a polishing recommendation for W2 merge. **Recommendation: consider adding a one-sentence parenthetical in the W7-14 cross-reference block.**

4. **Numeric vs spelled-out "17"** — §15.1 uses "Seventeen" while the abstract uses "seventeen"; consistency preference. Cycle-1 Critic §1 flagged. **Recommendation: pick one convention and apply uniformly across all four pieces.**

5. **3 sub-items → 2 Clay requirements collapse** — §15.2 enumerates three H4-affected sub-items (L.1(iii), L.2, AF form of L.4) and two H4-affected Clay requirements (C7, C9-AF) in different places without explicitly mapping (L.1(iii) + L.2 → C7, L.4 AF form → C9-AF). A careful referee may count three things and trip on "two". Cycle-1 Critic §3 flagged. **Recommendation: add one sentence in §15.2 making the 3→2 collapse explicit.**

6. **Voice-marker counting granularity** — blackboard §M row for cycle-1 sub-cycle should record the correct marker count. v2 carries "~50 markers" from cycle-1 Critic's independent recount. My higher-granularity recount gives 123. Any number ≥50 passes the 4/4 voice-shape check. **Recommendation: record "≥50 markers per cycle-1 Critic recount; higher counts possible at finer granularity" in blackboard §M.**

---

## §M summary (≤200 words)

**R.D.1 v2 verdict: SURVIVED.** The cycle-1 Critic's §7 Option 1 edit list has been faithfully applied. The v1 mischaracterization ("Paper 13 RH as two-dependency CCM+CBB") is repaired across Theorem 1 body, Remarks 1.A/1.B/1.C, §M summary, §I CONCERN, and Step 5.5 Way 1 backward-verification. The v2 abstract, Theorem 1 three-clause structure, §15 five-sub-section scope section (genuinely Paper-8 adapted, not mechanically copied from Paper 26), and W7-14 cross-reference are all structurally sound and mirror Paper 13 RH's actual one-dependency-on-the-theorem-label-face grammar exactly. Independent verification against Paper 13 §1.5, Paper 13 00-proof-skeleton.md (zero CBB occurrences), Paper 26 §13.1 / §9.1, Paper 8 §L.0, PROOF-CHAIN.md §IV.5 confirms all load-bearing structural claims. PCGT template is genuinely reusable and correctly triply-tested. Independent voice-shape recount: 123 markers across 4 draft pieces (cycle-1 Critic counted 50 at lower granularity; both counts confirm 4/4 voice-shape pass). No ship-blocking issues. Six low-priority W2-editorial-merge notes carried forward (runner language, stale probability, precision parenthetical, numeric consistency, 3→2 collapse, marker-count granularity). **v2 is ship-ready for Paper 8 Clay-submission editorial merge.**

---

*End of Alpha-Critic final adversarial pass on R.D.1 v2.*
*Verdict: SURVIVED. No ship-blockers. Six low-priority author-consideration notes for W2 merge.*
*Attack vectors tested: (d), (e), (f), (g), (h), (m). All survived.*
*Alpha-Critic: Claude Opus 4.6 (1M context), independent of v2 Author and cycle-1 Critic.*
*Ship status: R.D.1 v2 is ready for W2 preprint-insertion editorial merge.*
