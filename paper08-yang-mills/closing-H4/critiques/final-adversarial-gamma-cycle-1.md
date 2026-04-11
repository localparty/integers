# Final-Adversarial-Pass Critic Gamma — Cross-Paper Consistency

*Critic role: Gamma — cross-paper consistency adversarial pass.*
*Run: H4 closure, final-adversarial-pass, cycle 1.*
*Date: 2026-04-11.*
*Target bundle: `paper08-yang-mills/closing-H4/` at cycle-1 lockdown.*
*Attack focus: does the H4 closure story contradict any existing content in Paper 13 RH, Paper 26 BSD, Paper 8 itself, Paper 10, or Paper 12 relaxation?*

---

## 0. Verdict

**SURVIVED** (no ship-blocking cross-paper inconsistencies found).

One genuine cross-paper discrepancy identified — but it is entirely internal to the source document (`paper12/relaxation/04-...`), not a defect of the H4 closure artifacts. The H4 closure story, the R.D.1-v2 editorial artifact, and the blackboard's cross-paper claims are consistent with every source paper checked at the load-bearing level. Three low-priority observations (all already flagged in the blackboard §I as W2 editorial cleanups, not ship-blockers) are preserved for record.

---

## 1. Attack vector (n): 17/18 chain state vs PROOF-CHAIN.md §IV.1

**Claim under attack.** Blackboard §B: *"Paper 8's Yang-Mills chain state (2026-04-11) (from `preprint/PROOF-CHAIN.md §IV.1`): 4 [THEOREM] + 13 [LEMMA] + 1 [KEY LEMMA — OPEN] + 0 [GAP] = 17 of 18 unconditional."* Also echoed in R.D.1-v2 (multiple places: the draft abstract, Theorem 1, §15 Scope, W7-14 cross-reference).

**Primary source check.** `paper08-yang-mills/preprint/PROOF-CHAIN.md §IV.1` (lines 6–29) carries a 20-row table with steps labelled 1, 1b, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10b, 11, 12, 13, 14, 15, 16, 17, 18. The Status column uses the vocabulary *Proved / Literature / Conditional* — it does NOT carry the rigor-label vocabulary *[THEOREM] / [LEMMA] / [KEY LEMMA — OPEN] / [GAP]* that the blackboard attributes to it. The rigor-label vocabulary comes from `paper08-yang-mills/research/21-the-rigorous-proof.md` (cited in Paper 26's `strategy/04-closing-my4.md §0` as the canonical taxonomy source), not from PROOF-CHAIN.md directly.

**Reconciliation.** Counting rows in PROOF-CHAIN.md §IV.1 by Status:

- *Proved* (17 rows): 1 (Thm 4), 1b (Thm 5), 4 (Part I), 5 (Part II), 6, 7, 8, 9, 10, 10b, 11, 12, 13, 14 (§5.7), 15, 16, 17
- *Literature* (2 rows): 2, 3 (Balaban CMP 109, 119)
- *Conditional* (1 row): 18 (AF match L.2 + leading-order OPE L.4, conditional on H4)

Substeps 1b and 10b are sub-numbered refinements of the main steps (1 and 10). Treating them as integral parts of their parent steps, the chain has 18 main-numbered steps (1, 2, ..., 18), of which 17 are either *Proved* or *Literature* (unconditional in the blackboard's sense) and 1 is *Conditional on H4*. **The 17/18 accounting is numerically correct.**

The blackboard's internal rigor-label subdivision (4 [THEOREM] + 13 [LEMMA] + 1 [KEY LEMMA — OPEN] + 0 [GAP]) is not directly encoded in PROOF-CHAIN.md — it is the blackboard's interpretation of the status column using the Paper 26 / `21-the-rigorous-proof.md` rigor taxonomy, and it is numerically self-consistent (4 + 13 + 1 = 18). The specific mapping has a minor loose edge: §B says "13 [LEMMA] (Steps 2-3 Balaban literature accepted; 4-13 polymer / operator / spectral / RG chain; 15-17 gradient-flow)" where "4-13" would include Step 4 already counted as [THEOREM]. If strictly interpreted "5-13 polymer / operator / spectral / RG chain" + "2-3 Balaban" + "15-17 gradient-flow" gives 9 + 2 + 3 = 14 LEMMAs, off by 1; if loosely interpreted, the total is 18. **This is a ≤1-row rounding ambiguity in the blackboard's §B rigor-label breakdown**, not an inconsistency with PROOF-CHAIN.md — the top-line claim "17 of 18 unconditional" holds under either reading.

**Cross-consistency with PROOF-CHAIN.md §IV.5.** Line 161 states verbatim: *"The gradient-flow programme (Steps 15--17) is unconditional; Step 18 is conditional on the standard hypothesis H4 (non-perturbative Schwinger functions agree with perturbation theory at short distances)."* This matches the R.D.1-v2's framing exactly. No inconsistency.

**Cross-consistency with L-clay-conjectures.md §L.5 + §L.6.** Sub-clause resolution map has H4-tagged entries at L.1(iii), L.2, L.4 (AF form), which the v2 artifact quotes correctly. L.6.3: *"Hypothesis H4 is the sole unverified input."* Matches the 17/18 narrative.

**Finding (n).** The 17/18 claim is consistent with PROOF-CHAIN.md §IV.1 at the top-line level. The blackboard's §B rigor-label subdivision has a minor rounding ambiguity (at most ±1 in the LEMMA count depending on whether Step 4 is counted as THEOREM or LEMMA) that does not affect the headline 17/18 number. **Not a ship-blocker; not even a weakness — the top-line count is robust.**

---

## 2. Attack vector (l-1): Paper 13 RH cross-consistency

**Claim under attack.** R.D.1-v2 editorial artifact:
- Paper 13 RH carries *one* logical dependency on the theorem-label face (CCM alone) with the Integers programme framework embedding noted in §1.5 but not carried as a logical dependency.
- The six-layer proof chain has zero CBB dependencies in any layer.
- §1.5 explicitly disavows CBB: *"Sections 3–11 are self-contained and do not depend on the CBB axioms."*

**Primary source check 1: Paper 13 §1.5 verbatim.** Read `paper13-rh/preprint/sections-01-05.md` lines 219–240:

> "### 1.5. Relation to the Integers programme
>
> This paper belongs to the Integers programme (Papers 12--28), which develops the Critical Bost--Connes--Brauer (CBB) system as a zero-parameter description of fundamental physics. The Riemann Hypothesis is not an external conjecture imported for number-theoretic interest: it is the consistency condition for CBB Axiom 1, which identifies the spectrum of the fundamental operator $\hat{R}$ on $\mathcal{H}_R$ with the Riemann zeros.
>
> [...]
>
> For the reader interested only in the proof of RH, Sections 3--11 are self-contained and do not depend on the CBB axioms. The proof uses CCM's operators, our ITPFI factorization, Boegli's theorem, and Hurwitz's theorem -- all independent of the broader Integers programme."

The R.D.1-v2 block-quote is verbatim-accurate (I checked word-for-word against the primary source). The logical entailment is also correct: §1.5 explicitly asserts proof-chain independence from CBB, so the conclusion "Paper 13 is one-dependency on the theorem-label face (CCM alone), with framework embedding in the Integers programme noted separately" follows by direct entailment.

**Primary source check 2: Paper 13 proof skeleton.** Read `paper13-rh/preprint/00-proof-skeleton.md` end-to-end (234 lines). The load-bearing findings:

- **Line 6 (header)**: *"Conditional on CCM (arXiv:2511.22755)."* The sole headline conditional.
- **Lines 50–62 (six-layer chain table)**: Layer 1 = CCM operators; Layer 2 = ITPFI state convergence; Layer 3 = estimates (3a archimedean, 3b eigenvector, 3c Sobolev, 3d CF decay); Layer 4 = Teschl form convergence + Boegli spectral exactness; Layer 5 = Hurwitz; Layer 6 = conclusion. **No CBB dependency in any layer.**
- **Lines 110–174 (cited theorems)**: CCM 2025, Boegli 2017, Teschl et al. 2026, Connes-van Suijlekom 2025, Bost-Connes 1995, Hurwitz 1893, Reed-Simon, Rellich-Kondrachov, plus our results (ITPFI factorization, Estimate 1, Estimate (b), Estimate (a), CF uniform decay, Boegli H1 gsrc, AE simplicity, Slepian compatibility lemma, Euler-Mascheroni elimination). None of these are CBB-system machinery. Bost-Connes 1995 is cited for KMS₁ uniqueness (the unique KMS₁ state $\omega_1$ is the foundation for ITPFI) — but KMS₁ uniqueness is a published theorem of Bost-Connes, not a CBB axiom.
- **Lines 216–223 (honest accounting)**: *"The proof chain stands at 8/10 overall confidence [...] The floor is Layer 1: CCM's paper is a preprint (arXiv:2511.22755) by Connes, Consani, and Moscovici. Theorem 1.1 is stated as conditional on CCM."*

**Cross-consistency result.** Paper 13 proof skeleton is genuinely one-dependency (CCM alone) at the logical level, with the six-layer chain having zero CBB dependencies in any layer. The R.D.1-v2 characterization is accurate. Paper 13 §1.5's disavowal is real, load-bearing, and verbatim-quoted in R.D.1-v2.

**Subtlety flagged but not ship-blocking.** Paper 13's proof chain cites Bost-Connes 1995 (for KMS₁ uniqueness, used to ground the ITPFI factorization in Layer 2). One could argue that "KMS₁ uniqueness from BC" is a CBB-adjacent literature dependency. But:

1. Bost-Connes 1995 is published literature (Selecta Math), not a CBB axiom.
2. KMS₁ uniqueness is a theorem about a specific C*-dynamical system (the Bost-Connes algebra), not an axiom of the CBB-system-as-defined-in-Paper-23.
3. Paper 13 §1.5's disavowal says "all independent of the broader Integers programme" — it draws a line between "Bost-Connes is published literature that we cite" and "CBB is the axiom base we do NOT depend on." The proof-skeleton table backs this up: Layer 2 is "ITPFI state convergence" via "ω_1 = ⊗_p ω_1^p" — proved three independent ways, one of which is *"Laca–Larsen–Neshveyev 2015 via KMS uniqueness (Bost-Connes 1995)"* (line 96 of strategy 04-closing-my4.md for Paper 26 context). The Bost-Connes 1995 theorem is a classical result used as literature input, not a CBB-axiom-level commitment.

The v2 editorial framing is therefore defensible: Paper 13 uses Bost-Connes 1995 as literature input (the same way Paper 8 uses Reisz lattice perturbation theory as literature) and does not invoke the CBB axiom system directly in the proof chain.

**Finding (l-1).** **SURVIVED.** Paper 13 RH's one-dependency-on-CCM grammar is verbatim-consistent with the R.D.1-v2 characterization. The six-layer proof skeleton has zero CBB-axiom dependencies. The §1.5 disavowal is load-bearing, explicitly asserted, and primary-source-accurate in the v2 artifact. No inconsistency.

---

## 3. Attack vector (l-2): Paper 26 BSD cross-consistency

**Claim under attack.** R.D.1-v2 editorial artifact:
- Paper 26 BSD is "one-dependency on CBB where framework embedding coincides with logical dependency."
- Paper 26 ships as "Theorem 13.1 (BSD from CBB)".
- Paper 26's proof chain genuinely depends on CBB at the logical level via the BC bridge algebra $\mathcal{A}_{BC,K}$ and the KMS₁ ITPFI factorization.
- The Paper 26 MY4 closure via G's KMS projector $P_k^{\mathfrak{p}} := I - s_{\mathfrak{p}}^k(s_{\mathfrak{p}}^k)^*$ produces the canonical ORA structural bypass example.

**Primary source check 1: Paper 26 Theorem 13.1.** Read `paper26-bsd/preprint/sections-part-IV.md` line 360 verbatim:

> "**Theorem 13.1 (BSD from CBB).** *Under the CBB axioms (Paper 23), for CM curves E/Q with CM by a class-number-1 imaginary quadratic field K and analytic rank 0 or 1, BSD holds:*"

Matches the v2 block-quote exactly. One-dependency on CBB on the theorem-label face, verbatim-consistent.

**Primary source check 2: Paper 26 §9.1 Theorem 9.1 analog conditional.** Read `paper26-bsd/preprint/sections-part-III.md` lines 606–611:

> "**Theorem 9.1** (GRH for CM curves, conditional on CBB). *Under the CBB axioms (Paper 23), let $K$ be an imaginary quadratic field with class number $1$, and let $E/\mathbb{Q}$ be an elliptic curve with complex multiplication by $\mathcal{O}_K$. Then all non-trivial zeros of $L(E, s)$ lie on $\operatorname{Re}(s) = 1/2$.*
>
> > **Remark.** The CBB axioms are independently supported by 36 zero-parameter predictions. The contrapositive: if BSD fails for CM curves, the zero-parameter description is coincidental at $P < 10^{-89}$."

Matches. Paper 26 uses "from CBB" / "conditional on CBB" phrasing throughout.

**Primary source check 3: Paper 26 proof-chain CBB dependency.** Read `paper26-bsd/strategy/04-closing-my4.md` for the chain dependency structure:

- Link 1 (BC algebra $\mathcal{A}_{BC,K}$): foundation of everything else. The C*-algebra is built via Ha-Paugam 2005; KMS₁ uniqueness via Laca-Larsen-Neshveyev 2015. CBB-system machinery directly.
- Link 5c (ITPFI factorization): $\omega_1^K = \bigotimes_{\mathfrak{p}} \omega_1^{\mathfrak{p}}$ — directly on the BC algebra.
- Links 6, 7, 8 (cocycle shift, Key Lemma C, Baker kill): all algebraic work on the BC bridge cocycles.

Paper 26's proof chain therefore does genuinely depend on CBB-system machinery (BC algebra + KMS₁ ITPFI + cocycle shifts). The v2 characterization "framework embedding coincides with logical dependency" is accurate.

**Primary source check 4: Paper 26 Route 3 projector bypass.** Read `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` lines 12–33:

> "```
>   P_k^𝔭  :=  I − s_𝔭^k (s_𝔭^k)^*  =  I − e_{𝔭^k}    ∈  A_{BC,K}
> ```
>
> With this single projector, the §6 'dark-state impossibility' argument of Paper 26 becomes pure algebra on `A_{BC,K} + ω_1^K`, and the dependency on Meyer eigenstates disappears. Combined with the fact that **Paper 26 §§7–8 were already algebraic** (Remark 7.2 says so literally: 'The derivation is pure algebra on the local Euler factor'), the entire bridge chain goes through without ever invoking the Meyer distributional-to-genuine spectrum upgrade.
>
> **MY4 is gone.** [...]
>
> **Rigor state of Paper 26:** from 10/11 to **11/11**, conditional only on the CBB axioms (the same conditional Paper 13's RH proof lives with)."

Two important observations:

**Observation 1.** The phrase *"the same conditional Paper 13's RH proof lives with"* in Paper 26's strategy document (line 31–32) is the original source of the ambiguity the R.D.1 cycle-1 Critic caught. The v2 editorial artifact (at line 43 in the "Framework tools used" section) **already flags this motivational paraphrase explicitly**, noting: *"this is a motivational paraphrase internal to Paper 26's strategy doc; the cycle-1 Critic verified that Paper 13 §1.5 explicitly disavows CBB as a logical dependency of the RH proof chain, so the 'same' phrase refers to the shared *framework embedding* (both papers sit inside the Integers programme) rather than a shared *logical dependency on CBB*. Paper 26's proof chain genuinely depends on CBB via the BC bridge algebra; Paper 13's does not."*

**The v2 artifact is aware of and explicitly corrects the Paper 26 strategy doc's paraphrase.** This is exactly the v6 patch I-v6-1 "inference-from-source-check" discipline being applied proactively — the v2 Author read Paper 26's strategy line verbatim, noticed the ambiguity, checked Paper 13 §1.5 to see whether the claim was literally true, and documented the corrected reading.

**Observation 2.** The strategy 05 §3 table ("Rigor state after Route 3", line 171–207) produces the verdict: *"Paper 26 Theorem 13.1 [...] becomes [THEOREM conditional on CBB axioms]"*. This is internally consistent with the v2 characterization.

**Finding (l-2).** **SURVIVED.** Paper 26 BSD genuinely depends on CBB at the logical level. The R.D.1-v2 characterization is correct. The v2 artifact already flags the Paper 26 strategy doc's loose "same conditional Paper 13 lives with" phrase as a framework-embedding-level equivalence (both sit in the Integers programme), not a logical-dependency equivalence (Paper 13's proof chain is CBB-independent, Paper 26's is not). This is an active, defensible, primary-source-verified cross-paper distinction. No inconsistency.

---

## 4. Attack vector: Paper 10 Route 05 cross-consistency

**Claim under attack (K-2 kill narrative).** Blackboard (cycle 1, W1-C1 Critic return): *"Paper 10 Route 05 (documented in `gradient-flow-attack-plan/research/W7-14-af-match.md §6.2`) uses Vassilevich's mass-independence of $a_4$ to establish that each KK mode contributes the same bare $(a, c)$ coefficients, summing via zeta-regularization to $a_{\mathrm{total}} = c_{\mathrm{total}} = 0$. This is a **bare-level statement at $\Lambda$** — fully compatible with R.C.1's kill. **The framework already uses the spectral action correctly for boundary conditions; R.C.1's attempted second use for running flow is what is killed.**"*

**Primary source check: W7-14 §6.2.** Read `gradient-flow-attack-plan/research/W7-14-af-match.md` lines 430–483 verbatim:

> "### 6.2 Vassilevich mass-independence and the Weyl anomaly
>
> Paper 10 (Route 05, Section 4.4) establishes the following chain:
>
> **(a) Mass-independence of $a_4$.** The Seeley-DeWitt heat-kernel coefficient $a_4(D)$ for a massive field with kinetic operator $D = -\nabla^2 + m^2 I + E_{\mathrm{curv}}$ is independent of the mass $m$ (Vassilevich, hep-th/0306138, eq. 4.3). [...]
>
> **(b) Each KK mode contributes the same $(a,c)$.** Every KK graviton at level $n$, regardless of its mass $m_n = n/R$, contributes the same Weyl anomaly coefficients as the massless $n = 0$ mode: $(a, c) = (43/360,\;87/20)$.
>
> **(c) The total Weyl anomaly vanishes.** Summing over the full $S^1$ tower:
> $$a_{\mathrm{total}} = \frac{43}{360} \times \sum_{n \in \mathbb{Z}} 1 = \frac{43}{360} \times S_0 = 0, \tag{6.2}$$
> $$c_{\mathrm{total}} = \frac{87}{20} \times S_0 = 0, \tag{6.3}$$
> where $S_0 = 1 + 2\zeta_R(0) = 1 + 2(-\tfrac{1}{2}) = 0$ is the zeta-regularized mode count."

The W7-14 §6.2 content matches the K-2 narrative verbatim. Vassilevich $a_4$ is used via mass-independence to establish that each KK mode contributes the same Weyl anomaly $(a, c)$, summed via zeta-regularization to $a_{\mathrm{total}} = c_{\mathrm{total}} = 0$. This is a one-loop UV counter-term computation (bare-level at $\Lambda$), not a running-flow extraction.

**Primary source check: Paper 10 actual content.** Read `paper10/preprint/00-abstract.md`:

> "Paper 10: Scheme-Independence of UV Finiteness in 5D KK Gravity [...] We address the open problem stated in Paper 1 (Appendix U §U.2c): whether the vanishing of the Goroff-Sagnotti R³ counterterm in 5D linearized gravity on M⁴ × S¹/Z₂ — established in Paper 1 within zeta regularization via the Universal Epstein Vanishing theorem (Appendix K) — is scheme-independent. [...] Two proved results. (i) The Seeley-DeWitt coefficients a₂ = 0 and a₄ = 0 of the Lichnerowicz operator on the flat background M⁴ × S¹/Z₂ are intrinsic spectral invariants, computed without reference to any regularization prescription. [...] (ii) The 4D Weyl anomaly coefficients a_total = c_total = 0 for the full KK graviton tower are protected by the Wess-Zumino consistency condition: no finite local counterterm can shift (a, c), and they vanish under zeta regularization, so they vanish in every diffeomorphism-preserving scheme."

Paper 10 is about **scheme-independence of UV finiteness** in 5D KK gravity. Its "two proved results" are:
1. Seeley-DeWitt $a_2 = a_4 = 0$ for the Lichnerowicz operator on $M^4 \times S^1/\mathbb{Z}_2$
2. Weyl anomaly coefficients $a_{\mathrm{total}} = c_{\mathrm{total}} = 0$ for the KK graviton tower via Wess-Zumino consistency

These are **one-loop counter-term / Weyl-anomaly computations at the classical/bare level**, matching the W7-14 §6.2 characterization. Paper 10 does NOT claim to extract running couplings from $a_4$; it computes the Seeley-DeWitt coefficients as **one-loop bare quantities** and uses their vanishing to establish **UV scheme-independence** of the two-loop Goroff-Sagnotti R³ counterterm.

**Cross-consistency with K-2.** K-2 kills "Route C (spectral action + Identity 12 + bridge family k=4) to close H4 via extracting a running coupling from $a_4$". K-2's kill reasoning: *"spectral action produces boundary conditions at $\Lambda$, not running flow"*. W7-14 §6.2 uses $a_4$ at the **one-loop UV counter-term level** (bare-level at $\Lambda$), not as a running-flow source. Paper 10 uses $a_4$ at the **intrinsic spectral invariant level** for scheme-independence (also bare-level). **Both uses are compatible with K-2's kill reasoning** — neither Paper 10 nor W7-14 §6.2 attempts to extract a running coupling $g(\mu)$ from $a_4$; both use it as a bare/one-loop coefficient.

**Finding on Paper 10 Route 05.** **SURVIVED.** The K-2 narrative "Paper 10 Route 05 uses the spectral action correctly for KK decoupling via mass-independence" is verbatim-accurate to W7-14 §6.2's actual content and Paper 10's actual abstract. Paper 10 uses $a_4$ at the one-loop counter-term/scheme-independence level (boundary conditions at $\Lambda$, not running flow), fully compatible with K-2's kill of Route C's attempted running-flow extraction. No inconsistency.

---

## 5. Attack vector: Paper 12 relaxation/04 seven-anchor strategy cross-consistency

**Claim under attack.** Blackboard §K (cycle 1 open, spawn table): `paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md` is an *"always-include"* for H4 closure spawns, characterized as *"confirms the Clay proofs are applications, not foundations, and that ship-with-honest-conditional is the default strategic stance when a gap is identified"*.

**Primary source check.** Read `paper12/relaxation/04-...md` (644 lines total) §1–2 and §7–9 selectively.

**§1 Philosophy** (lines 44–53): The foundation is the geometric-spectral duality of Riemann, not the Clay results. "Clay results are produced, not relied on. Yang-Mills, RH, BSD are theorems the framework happens to derive. They are *outputs*, not *inputs*. If one of them turns out to have a gap, the framework continues to derive the others." — Matches the blackboard's characterization verbatim.

**§5 Clay proofs as applications** (lines 179–185): "This is *robustness through decoupling*. Each Clay result is a *theorem that the framework happens to also produce*, not *a premise the framework relies on*. [...] The strategic implication: **publish the framework's empirical content first, with the Clay results as side notes**, not the other way around." — Matches the "ship-with-honest-conditional as default" characterization.

**§7 Seven anchors** (lines 288–374): Anchor 1 = geometric-spectral duality; Anchor 2 = cross-formula γ_n consistency (T5); Anchor 3 = cross-functional-form agreement; Anchor 4 = cross-integer / cyclotomic levels; Anchor 5 = cocycle equality at k=3; Anchor 6 = CCM 2025 timeline-independent confirmation; Anchor 7 = predictions (Theoretical-Precision Table). "The framework's foundation is the intersection of all seven anchors." — Standalone structural content, independent of any specific Clay proof.

**Is it H4-relevant?** The file does not mention H4 directly. Its relevance to H4 closure is at the **strategic-stance level**: if H4 cannot be closed mathematically, the framework's 36/36 empirical content + seven anchors remain intact, and shipping Paper 8 with H4 as a standing conditional is consistent with the "bind-to-many-ends" strategy. The blackboard's §J voice canon extract *"H4 closure is not the framework's foundation. It is one of the four Clay-class theorems the framework derives. The seven anchors are the foundation. H4 closure is a downstream consequence."* directly mirrors §1.1 of relaxation/04. So the "always-include" classification is justified — the file is load-bearing for Route D's first-class status (HONEST-STALL without panic, because the programme's empirical content is independent of H4).

**Real cross-paper inconsistency found (but NOT in the H4 closure artifacts).** The relaxation/04 file contains an **internal numbering discrepancy** unrelated to the H4 closure artifacts:

- Line 171: `### Paper 10 — Yang-Mills mass gap`
- Line 507: `### Paper 10 (Yang-Mills mass gap) — highest fragility`

Both of these treat "Paper 10" as the Yang-Mills mass gap paper. But:

- `paper10/preprint/00-abstract.md` line 1: *"Paper 10: Scheme-Independence of UV Finiteness in 5D KK Gravity"* (NOT Yang-Mills).
- `mapping-phase-B3-everything-else.md` line 107: *"paper08-yang-mills (625 md files — 'Gradient Flow and Yang-Mills Mass Gap')"* (Paper 8 IS the Yang-Mills paper).

The relaxation/04 file uses the **old numbering convention** where Paper 10 was the Yang-Mills paper; the mass-gap content has since been split out into paper08-yang-mills (with paper10 retained for the 5D KK gravity UV finiteness / scheme-independence content). The relaxation/04 file was authored 2026-04-11 (today's date per line 21) but still references the obsolete paper numbering.

**This is a discrepancy INTERNAL to relaxation/04**, not caused by the H4 closure artifacts. The H4 closure blackboard and R.D.1-v2 correctly use "Paper 8" for Yang-Mills and "Paper 10" for the 5D QG UV finiteness scheme-independence — matching the actual current paper content.

The blackboard's selective-include of relaxation/04 uses the file for its **seven-anchor strategy** content (§7, lines 288–374), which is independent of the Paper 10/Paper 8 numbering discrepancy. The H4 closure artifacts do NOT inherit or propagate the numbering error.

**Finding on relaxation/04.** **SURVIVED (with caveat).** The blackboard's characterization of relaxation/04 as an "always-include" confirming the ship-with-honest-conditional stance and Clay-proofs-as-applications framing is verbatim-accurate to §1 and §5 of the source. The seven-anchor list (§7) is H4-relevant at the strategic level (Route D's first-class status is justified by §7's bind-to-many-ends logic). The internal numbering discrepancy in relaxation/04 itself (Paper 10 vs Paper 8 for Yang-Mills) is **not propagated to the H4 closure artifacts** — the blackboard and R.D.1-v2 use the correct current numbering throughout. **Caveat: flag this as a follow-up cleanup in paper12/relaxation/04 itself; it is not an H4 closure defect.**

---

## 6. Additional cross-paper consistency spot checks

Beyond the five attack vectors in the brief, I ran three additional spot checks for cross-paper consistency.

**Spot check A: Paper 8 Theorem L.0 has zero CBB references.** Grep'd `paper08-yang-mills/preprint/sections/L-clay-conjectures.md` for "CBB", "Critical Bost", "Integers programme", "Critical Bost-Connes-Brauer": **zero matches**. Paper 8's Theorem L.0 is already one-dependency on H4 alone, with no CBB invocation — confirming the v2 claim that "Paper 8 already carries H4 alone on the theorem-label face" (line 47 of R.D.1-v2).

**Spot check B: Paper 8 baseline abstract consistency.** Read `paper08-yang-mills/preprint/sections/00-abstract.md` lines 80–104. The current abstract cites "Quantum Geometry in 5D framework (Papers 1 and 10; cross-references in Appendix N)" as the framework embedding and names H4 as the sole conditional for the AF short-distance match + OPE AF form. The v2 editorial upgrade preserves this baseline and adds explicit cross-references to Paper 13 RH / Paper 26 BSD analog conditionals + an explicit naming of "H4 in the W7-14 mildest form". **The v2 edit is additive to the baseline, not contradictory.** No inconsistency.

**Spot check C: Paper 8 §L.6.3 "the single remaining open item" matches the 17/18 accounting.** Read lines 206–222 of `L-clay-conjectures.md`: *"Hypothesis H4 is the sole unverified input. [...] All gaps G1–G6 identified in the gradient-flow attack plan are closed by explicit proofs in Appendix N: [G1, G2, G3, G4, G5, G6 closing lemmas]. Gap G7 = Hypothesis H4 is the only item that remains open."* This matches the blackboard's 17/18 framing ("the sole KEY LEMMA — OPEN is H4") and the v2 artifact's Theorem 1 Remark 1.C ("H4 is the only input separating Paper 8 from 18/18 unconditional closure"). Cross-consistent.

---

## 7. Known low-priority discrepancies (all flagged in blackboard §I as W2 editorial cleanups, not ship-blockers)

For completeness, I document three known discrepancies within the R.D.1-v2 editorial artifact that the v2 Author has already flagged for the W2 editorial merge task (per the "Watch out for" and "low-priority cleanups" sections of R.D.1-v2 §I):

**Discrepancy 7.1 — Stale ~0.74 joint closure probability.** The R.D.1-v2 W7-14 cross-reference block (line 495) says: *"Joint closure probability across A/B/C $\approx 0.74$."* The post-Wave-1 blackboard has $P(A \vee B \vee C) \approx 0.10$ (after Wave 1: A decomposed, B collapsed into A, C killed). **Flagged in v2 §I "Watch out for" item (5) as a W2 cleanup; also flagged in the R.D.1 cycle-1 Critic notes.** Not a ship-blocker — the draft W7-14 cross-reference is editorial content to be merged into Paper 8, and the 0.74 figure should be stripped before merge.

**Discrepancy 7.2 — §15.2 internal runner language.** The R.D.1-v2 §15.2 draft (lines 427–435) contains the phrases: "Route A [...] Runner $p \approx 0.50$", "Route B [...] Runner $p \approx 0.30$", "Route C [...] Runner $p \approx 0.25$", "Route D [...] Runner $p \approx 0.99$. The HONEST-STALL option, first-class per v3 patch I-5". These are internal runner-vocabulary leakage that should not appear in the shipped preprint. **Flagged in v2 §I "Watch out for" item (2) as a W2 cleanup.** Not a ship-blocker — the runner vocabulary is to be stripped during the preprint merge.

**Discrepancy 7.3 — §15.2 routes still listed as "currently attacking".** The §15.2 draft says *"Three routes are currently attacking H4"* (line 427) and lists Routes A, B, C as active. Post-Wave-1, Route B has collapsed into Route A (not independent) and Route C is killed (K-2). The §15.2 language should be updated at W2 merge to reflect the post-Wave-1 state: Route A decomposed (pending external unlocks in Borel summability or instanton obstruction), Route B not independent of A, Route C killed at the spectral-action-is-classical-not-running kill. **Flagged in v2 §I cleanup list; the R.D.1 cycle-1 Critic also noted this as a W2 merge item.** Not a ship-blocker — the route-level accounting in the editorial preprint should reflect whatever state is current at the time of preprint merge, not necessarily the Wave 1 cycle-close state.

All three are known, flagged, and scoped to the W2 editorial merge task. None affect the v2 artifact's ship-readiness as an editorial artifact at the node level.

---

## 8. Cross-paper consistency matrix

Summary of all cross-paper consistency checks:

| Check | Source claim | Primary-source verification | Verdict |
|---|---|---|---|
| (n) 17/18 chain state | Blackboard §B + R.D.1-v2 multiple places | PROOF-CHAIN.md §IV.1: 17 *Proved/Literature* + 1 *Conditional on H4* = 18 main steps; §IV.5 Step 18 conditional on H4 | **Consistent** |
| (l-1) Paper 13 RH one-dependency grammar | R.D.1-v2 Remark 1.B + Step 5.5 Way 1 | Paper 13 §1.5 verbatim disavowal of CBB; six-layer proof skeleton has zero CBB dependencies in any layer | **Consistent** |
| (l-2) Paper 26 BSD one-dependency on CBB | R.D.1-v2 Remark 1.B + abstract sentence | Paper 26 Theorem 13.1 "Under the CBB axioms"; strategy/05 Route 3 "from CBB"; proof chain genuinely uses BC bridge algebra + KMS₁ ITPFI | **Consistent** |
| (l-2 subtlety) Paper 26 strategy line "same conditional Paper 13 lives with" | R.D.1-v2 flags this as motivational paraphrase | Paper 13 §1.5 explicit disavowal shows the strategy-doc line refers to framework embedding, not logical dependency | **Consistent** (v2 already corrects the ambiguity) |
| (Paper 10) K-2 "spectral action used correctly in Paper 10 Route 05" | Blackboard cycle-1 W1-C1 Critic return | W7-14 §6.2 verbatim + Paper 10 abstract: Vassilevich $a_4$ used for mass-independence → bare anomaly coefficients → zeta-regularized total = 0 (one-loop UV counter-term level, not running flow) | **Consistent** |
| (Paper 12 relaxation/04) seven-anchor always-include | Blackboard §K cycle-1 spawn table | Paper 12 relaxation/04 §1, §5, §7: Clay proofs as applications, bind to many ends, seven anchors including cross-formula consistency + cross-integers + cocycle equality + CCM 2025 timeline + predictions | **Consistent** |
| Spot check A: Paper 8 Theorem L.0 zero CBB references | Implicit in v2's "already one-dependency" claim | Grep L-clay-conjectures.md for "CBB": zero matches | **Consistent** |
| Spot check B: Paper 8 baseline abstract | v2 edit is additive to baseline | Baseline abstract names H4 as sole conditional; framework via Papers 1 and 10 | **Consistent** |
| Spot check C: Paper 8 §L.6.3 "sole unverified input" | 17/18 and v2 Remark 1.C both claim H4 is sole gap | L.6.3 explicitly states "Hypothesis H4 is the sole unverified input. [...] Gap G7 = Hypothesis H4 is the only item that remains open" | **Consistent** |
| **FOLLOW-UP** relaxation/04 numbering | Blackboard uses Paper 8 for YM, Paper 10 for 5D KK | Paper 10 abstract: "Scheme-Independence of UV Finiteness in 5D KK Gravity"; Paper 8 is Yang-Mills. relaxation/04 uses "Paper 10 — Yang-Mills mass gap" (stale numbering, internal to source file, not propagated to H4 artifacts) | **Follow-up cleanup in paper12/relaxation/04 itself; NOT an H4 closure defect** |

---

## 9. Verdict

**SURVIVED** (no ship-blocking cross-paper inconsistencies).

All five attack vectors from the brief checked against primary sources:

1. **(n) 17/18 chain state**: Verbatim-consistent with PROOF-CHAIN.md §IV.1 top-line count. Minor ±1 rounding ambiguity in the blackboard's rigor-label subdivision (Step 4 counted as THEOREM in one place, possibly LEMMA in another) does not affect the headline 17/18 count.

2. **(l) Paper 13 RH cross-consistency**: Verbatim-consistent. Paper 13 §1.5 explicit disavowal of CBB as a logical dependency is load-bearing and v2-quoted accurately; six-layer proof skeleton has zero CBB dependencies in any layer.

3. **(l) Paper 26 BSD cross-consistency**: Verbatim-consistent. Theorem 13.1 = "Under the CBB axioms"; proof chain genuinely uses BC bridge algebra + KMS₁ ITPFI (so CBB is the sole logical dependency, framework embedding coincides with logical dependency). The v2 artifact explicitly flags Paper 26 strategy/05's "same conditional Paper 13 lives with" phrase as a framework-embedding-level equivalence, not a logical-dependency equivalence — this correction is accurate and documented.

4. **Paper 10 Route 05 cross-consistency**: Verbatim-consistent with K-2 kill narrative. W7-14 §6.2 uses Vassilevich mass-independence of $a_4$ at the one-loop UV counter-term level (bare at $\Lambda$), matching Paper 10's actual "Scheme-Independence of UV Finiteness" content. Neither claims to extract a running coupling from $a_4$, compatible with K-2's "spectral action is classical/bare not running" kill.

5. **Paper 12 relaxation/04 seven-anchor strategy cross-consistency**: Verbatim-consistent with blackboard's "ship-with-honest-conditional default + Clay-proofs-as-applications" characterization. The seven-anchor list is H4-relevant at the strategic level (Route D's first-class status is justified by §7's bind-to-many-ends logic). **One genuine follow-up cleanup flagged**: the relaxation/04 file itself has a stale internal numbering discrepancy ("Paper 10 — Yang-Mills mass gap" in §5 and §9, which should be "Paper 8 — Yang-Mills mass gap" per the current paper numbering). This is internal to relaxation/04 and is NOT propagated to the H4 closure artifacts — the blackboard and R.D.1-v2 correctly use Paper 8 for Yang-Mills and Paper 10 for the 5D KK gravity UV finiteness scheme-independence paper throughout.

Three low-priority discrepancies within R.D.1-v2 (stale 0.74 joint-P, §15.2 internal runner language, §15.2 "currently attacking" route accounting) are **already flagged in the v2 artifact's own §I "Watch out for" list** and the R.D.1 cycle-1 Critic's low-priority notes as W2 editorial merge cleanups. They are not silent inconsistencies — they are known-and-flagged preprint-merge tasks. None affect the v2 artifact's ship-readiness at the node level.

**The H4 closure story, the R.D.1-v2 editorial artifact, and the blackboard's cross-paper claims are internally consistent with every source paper checked at the load-bearing level.** The programme ships.

---

## 10. ≤200-word summary

**Verdict: SURVIVED.** All five brief attack vectors — (n) 17/18 chain state, (l) Paper 13 RH one-dependency grammar, (l) Paper 26 BSD one-dependency on CBB, Paper 10 Route 05 K-2 compatibility, Paper 12 relaxation/04 seven-anchor always-include — pass primary-source verification at the load-bearing level. The R.D.1-v2 editorial artifact correctly characterizes Paper 13 RH as one-logical-dependency on CCM (with §1.5 verbatim disavowal of CBB); correctly characterizes Paper 26 BSD as one-logical-dependency on CBB (with framework embedding coincident with logical dependency via BC bridge algebra); and correctly characterizes Paper 8 as one-logical-dependency on H4 with framework embedding via Paper 10 / Appendix N — closest to Paper 13 RH's actual grammar. The K-2 kill's claim that Paper 10 Route 05 uses the spectral action correctly at the one-loop UV counter-term level is verbatim-consistent with W7-14 §6.2 and Paper 10's actual "Scheme-Independence of UV Finiteness" abstract. One follow-up cleanup flagged: `paper12/relaxation/04` has a stale internal numbering discrepancy ("Paper 10 — Yang-Mills mass gap" should be "Paper 8") that is NOT propagated to the H4 closure artifacts. Three known low-priority discrepancies within R.D.1-v2 (stale 0.74 joint-P, internal runner language in §15.2, "currently attacking" route accounting) are already flagged in the v2 artifact's own §I cleanup list as W2 editorial merge tasks. **No ship-blocking inconsistencies. The programme ships.**

---

*End of Critic Gamma cross-paper consistency pass, cycle 1.*
*Verdict: SURVIVED. No ship-blocking inconsistencies found.*
*Attack vectors checked: (n) 17/18 chain state, (l) Paper 13 RH cross-consistency, (l) Paper 26 BSD cross-consistency, Paper 10 Route 05 K-2 compatibility, Paper 12 relaxation/04 seven-anchor strategy cross-consistency, plus 3 spot checks (L.0 zero CBB, baseline abstract, L.6.3 sole unverified input).*
*Primary sources verified: PROOF-CHAIN.md §IV.1 + §IV.5; paper13-rh §1.5 + proof-skeleton; paper26-bsd Theorem 13.1 + strategy 04 + strategy 05; paper10 abstract; W7-14 §6.2 (Paper 10 Route 05); paper12 relaxation/04 §1 + §5 + §7; paper08 L-clay-conjectures Theorem L.0 + L.5 + L.6 + L.7; paper08 00-abstract baseline.*
*Follow-up item flagged: paper12/relaxation/04 internal stale numbering ("Paper 10 — Yang-Mills") for separate cleanup in relaxation/04 itself, not an H4 closure defect.*
