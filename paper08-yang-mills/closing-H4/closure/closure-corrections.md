# Corrections and addenda: H4 closure for Paper 8 Yang-Mills mass gap

*Every honest finding caught and how it was applied. The kill list and the corrections together form the credibility of the programme.*

*Runner: Claude Opus 4.6 (1M context). Bundle: ora-bundle-v6. Date: 2026-04-11.*

---

## Findings summary

| Finding | Caught at | Severity | Status |
|---|---|---|---|
| W7-14 §5.3 "reformulation = closure" brief paraphrase error | Cycle 1 W1-A1 Step 1 DIAGNOSE | MAJOR | APPLIED — R.A $p$ 0.50 → 0.10, decomposed into R.A.1a + R.A.1b, §I LESSON logged |
| CCM 2025 "UV asymptotics by construction" brief paraphrase error | Cycle 1 W1-B1 Step 3 UNIFY + Step 4 LOCK + Step 5.5 backward-verification | MAJOR | APPLIED — R.B collapsed into R.A, §F kill K-1 registered, §I LESSON logged |
| Connes 2007 "running coupling from $a_4$" brief paraphrase error | Cycle 1 W1-C1 Step 5.5 Self-suspicion | MAJOR | APPLIED — R.C KILLED, §F kill K-2 registered, §D Connes spectral action row annotated |
| Paper 26 MY4 analogy wrong-shaped for H4 | Cycle 1 W1-A1 + W1-B1 cross-finding | MAJOR | APPLIED — §I LESSON logged, brief's "canonical example" framing retired |
| R.D.1 v1 "two-dependency template" inference error | Cycle 1 R.D.1 Critic (→ Wave 1.5 sub-cycle) | MAJOR | APPLIED — Option 1 revision in R.D.1-v2 per critique §7, Paper 8 now mirrors Paper 13 RH actual one-dependency grammar |
| Cross-node structural LOCK at 9/10 on attack-surface identification | R.B.1 Critic cross-confirmation → Delta-Critic upgrade | HONEST NEGATIVE (structural finding) | APPLIED — §H bottleneck history updated, future attack-route variations on the Taylor-coefficient surface discouraged |
| Blackboard §C/§D/§E/§F/§I body content stale vs §K commit memos | Epsilon-Critic final-adversarial-pass | MEDIUM | PARTIALLY APPLIED — §C, §F, §I body content fixed during cycle-close; §D/§E/§G/§H/§N body updates deferred to final-pass cleanup (non-ship-blocking) |
| Precision-doubling stress test: 25/25 PASS at mp.dps=200, N up to 10000 | Beta-Critic final-adversarial-pass | POSITIVE CONFIRMATION | APPLIED — K-2 kill strength upgraded to maximally-verified, §F K-2 scope note extended |
| 11 new variant candidates for K-1 / K-2 escape tested, all fail | Beta-Critic final-adversarial-pass | POSITIVE CONFIRMATION | APPLIED — K-1 and K-2 scope notes extended with variant list (7 for K-1 + 4 for K-2) |
| `paper12/research/53-transposition-asymptotic-freedom.md` also foreclosed (framework-internal mechanism distinct from Chamseddine-Connes spectral action) | Beta-Critic final-adversarial-pass | HONEST NEGATIVE | APPLIED — K-2 scope note extended to cover the research/53 "QCD asymptotic freedom IS simple pole of $\zeta$ at $\beta=1$" mechanism as also failing to close H4 (structural, not rigorous; doesn't address non-perturbative Schwinger function asymptotics) |
| RH and H4 require incompatible NCG machinery ($\theta$-summable vs finitely-summable) | Beta-Critic cross-paper insight I.β.6 | POSITIVE CONFIRMATION (meta-level architectural finding) | APPLIED — §I LESSON logged for future programme architecture; meta-level finding that the framework's NCG toolkit is multiple incompatible tools, not a single unified machine |
| Paper 12 `relaxation/04` stale "Paper 10 = Yang-Mills" numbering | Gamma-Critic cross-paper consistency check | NON-SHIP-BLOCKING HOUSEKEEPING | FLAGGED — does not affect H4 closure artifacts; separate cleanup task recommended (Paper 12 `relaxation/04` lines 171, 507 call "Paper 10" the YM paper; Paper 10 is actually *"Scheme-Independence of UV Finiteness in 5D KK Gravity"*; Paper 8 is the YM paper; obsolete numbering from before YM content was split out) |
| I-7 catches paraphrase errors but NOT inference errors | R.D.1 Critic discovery | MAJOR v6 BUNDLE FINDING | APPLIED — v6 patch I-v6-1 (inference-from-source check) added to `ora-bundle-v6/01-the-prompt.md §7 Step 5.5 Way 1`; first entry in `ora-bundle-v6/08-changelog-v6.md`; anti-predictions A-1 through A-4 re-audited and all still pass |
| CCM 2025's "perturbation" means "rank-one perturbation" (operator-theoretic), NOT QFT perturbation theory — lexical category error | Delta-Critic via applying I-v6-1 logical-entailment check | HONEST NEGATIVE (refinement to the K-1 kill) | APPLIED — K-1 scope note updated to note this lexical category error as additional evidence supporting the pattern category assignment; empirical validation that I-v6-1 adds value beyond I-7 |

## Findings by round / cycle

### Cycle 1 Wave 1 (4 parallel Authors + 4 parallel Critics)

**W1-A1 (R.A.1 Taylor-coefficients) BLOCKED-DECOMPOSED**

Findings:
1. *"Reformulation into the mildest form" ≠ "closure".* The W7-14 §5.3 analyticity reframing moves the rigor burden from the non-perturbative side to the perturbative side but does NOT eliminate the burden. The Author's DIAGNOSE: *"What H4 asks in this language is whether the Taylor coefficients are computable by the Feynman-diagrammatic perturbative rules — a more accessible question, not an answered one."*
2. $F^{\mathrm{pert}}(t)$ is a formal power series (divergent, expected from renormalons for 4D YM), not an analytic function. The identity theorem's two-function hypothesis fails at the perturbative side.
3. Route A decomposes into two sub-problems, both harder than the ancestor: R.A.1a (perturbative flow-time analyticity — comparable to Borel summability) + R.A.1b (independent-point agreement — no candidate mechanism).

Applied: R.A $p$ 0.50 → 0.10; §E updated with R.A.1a, R.A.1b sub-nodes marked OPEN and deferred pending external unlocks; §E.1 joint probability cascaded from 0.9974 to 0.9953; §I CONCERN + CASCADE + 2× LESSON entries logged.

**W1-B1 (R.B.1 CCM 2025 port) BLOCKED-DECOMPOSED + COLLAPSED INTO R.A**

Findings:
1. CCM 2025 does NOT provide "UV asymptotics by construction" — the primary source (arXiv:2511.22755 p.1 Abstract + §7 Outlook p.28) states the rigorous identification of operators' spectra with Riemann zeros remains "the main remaining obstacle to our approach to RH". The brief's paraphrase was confused with CCM 2025's "rank-one perturbation of the spectral triple" (operator-theoretic), not QFT perturbation theory — a lexical category error.
2. The CCM 2025 → YM transposition's self-adjointness mechanism reduces to W7-14 §5.3 analyticity — the same input Route A depends on. Route B is not a distinct closure mechanism; it is Route A in spectral-triple language.
3. Dictionary entries #12-17 hit a category error: RH targets are zeros of an entire function (Hurwitz requires the former); YM targets would be Taylor coefficients of an analytic function.
4. Even-sector parity (CCM Lemma 5.2(i)) fails because $F(t)$ is not symmetric under $t \mapsto T^2/t$.

Applied: §F K-1 registered with pattern External-source-inconsistency + Wrong-space; scope note clarifies K-1 is CCM-2025-specific (not NCG-level); joint probability updated to use $\max(p_A, p_B)$ instead of $(1 - p_A)(1 - p_B)$; §I 2× LESSON entries on transposition collapse risk and I-7 transfer validation.

**W1-C1 (R.C.1 Spectral action + Identity 12 + bridge family) KILLED**

Findings:
1. Connes 2007 Séminaire Poincaré X §5 eq. (24) verbatim: *"The spectral action principle asserts that the fundamental action functional $S$ that allows to compare different geometric spaces at the classical level..."* — the spectral action is defined at the classical level, producing bare actions at cutoff $\Lambda$, NOT running flow.
2. Vassilevich 2003 hep-th/0306138 eq. (4.34) verbatim + interpretation: *"We calculate the heat kernel coefficient $a_4^{\mathrm{tot}}$ which defines the one-loop divergences in the zeta function regularization. We also recover the coefficient 11/3 which is familiar from computations of the Yang-Mills beta functions."* The integer $11N/3$ emerges as a counter-term coefficient, not a running-coupling slope.
3. Identity 12 is a C*-dynamical equivalence ($T_e \leftrightarrow H_{BC} = \log\hat{N}$), not a spectral-triple equivalence. `paper12/research/04-identity-12-rigorous.md` contains ZERO occurrences of "Dirac operator", "spectral triple", "Seeley-DeWitt", or "heat kernel". $H_{BC}$ is a positive multiplication operator with discrete log spectrum — not of Seeley-DeWitt form.
4. k=4 bridge at (3,13) is a Brauer cocycle in $H^2(\mathbb{Z}/4\mathbb{Z}, U(1))$, not an NCG construction.
5. Four variant mappings of $H_{BC}$ tested: direct (heat trace exponentially divergent), half-power $\sqrt{H_{BC}}$ (dimension 1 not 4), tensor product $A_{BC} \otimes C^\infty(M^4)$ (inherits BC divergence), CCvS 2013 Pati-Salam graft (bypasses Identity 12 + still classical at $\Lambda$). All fail.
6. Forward lead preserved: CCvS 2013 Pati-Salam spectral triple + k=4 bridge at (3,13) + $\alpha_{PS}^{-1} = 17$ match as compatible boundary conditions at $\Lambda$ — separate research note, not an H4 closure.

Applied: §F K-2 registered with pattern External-source-inconsistency + Vacuous; narrow kill — spectral action + Identity 12 + bridge family remain valid framework tools for their actual purposes (Paper 10 Route 05 KK decoupling via mass-independence uses them correctly); §D Connes spectral action row annotated with "classical/bare at $\Lambda$; running comes from post-hoc Callan-Symanzik RG flow, not from $a_4$"; §D row added for Vassilevich YM $a_4$; §D row added for Spiridonov-Chetyrkin trace-anomaly identity; byte-for-byte verification script `code/R.C.1-seeley-dewitt-a4.py` at mp.dps=80 → 7/7 PASS exact rational.

**W1-D1 (R.D.1 Editorial HONEST-STALL) ADVANCED → WEAKENED → revised → SHIP-READY**

Findings:
1. v1 mis-characterized Paper 13 RH as "two-dependency (CCM + CBB)". Paper 13 §1.5 lines 237-240 explicitly disavow CBB as a logical dependency: *"For the reader interested only in the proof of RH, Sections 3–11 are self-contained and do not depend on the CBB axioms. The proof uses CCM's operators, our ITPFI factorization, Boegli's theorem, and Hurwitz's theorem — all independent of the broader Integers programme."*
2. The Author correctly block-quoted this passage but drew the opposite structural inference. This was the discovery of a new failure mode: *reading-vs-inference mismatch*. I-7 backward-verification catches paraphrase errors (quote ≠ claim at text level) but not inference errors (quote ≠ logical entailment of claim).
3. The correct one-dependency grammar mirrors Paper 13 RH: H4 alone on the theorem-label face, CBB noted as framework embedding via Paper 10 / Appendix N in Remark 1.A, not as a logical co-dependency.

Applied: Wave 1.5 sub-cycle revision Agent produced R.D.1-v2 (565 lines, +43 net from v1); Theorem 1 body + Remark 1.A + Remark 1.B + §M summary + §I CONCERN all corrected; voice-shape 4/4 passes with 50 markers (cycle-1 Critic recount) / 123 markers (Alpha-Critic independent recount); v6 bundle patch I-v6-1 (inference-from-source check) added to `ora-bundle-v6/01-the-prompt.md §7 Step 5.5 Way 1`; first entry in `ora-bundle-v6/08-changelog-v6.md`.

### Cycle 1 Wave 1 Critic pass (4 parallel Critics)

**R.A.1 Critic: DECOMPOSITION-VERIFIED.** No disagreement with Author. Byte-for-byte re-verification of the Author's W7-14 §5.3 block-quote matches primary source at lines 388-414. First Critic-independent empirical validation of a Wave 1 Author's I-7 backward-verification. 4 additional extension-test candidates ruled out (imaginary-axis, small-$t$ large-separation, dimensional continuation from $d<4$, large-$N$ planar limit).

**R.B.1 Critic: DECOMPOSITION-VERIFIED.** Triple-confirmed I-7 catch against CCM 2025 PDF. K-1 scope refined to CCM-2025-specific (not NCG-level). Cross-node structural LOCK at 9/10 identified (R.A.1 + R.B.1 cross-confirm attack surface). One genuine structural gain: flow-time CF analog is a lemma-level refinement of W7-14 §5.3.

**R.C.1 Critic: VERIFIED (kill stands at maximum strength).** Byte-for-byte script re-run at mp.dps=160 with extended N grid → 12/12 PASS with zero residual. Connes 2007 + Vassilevich 2003 primary sources re-verified via pdftotext. Extension test exhausted (4 variant mappings fail). Cross-node consistency with Paper 10 Route 05 verified.

**R.D.1 Critic: WEAKENED.** Identified the Paper 13 two-dependency mis-characterization. Option 1 revision instructions provided (~60 line diff). Voice-shape check passes independently at 50 markers. Proposed the v6 bundle patch I-v6-1 (inference-from-source check).

### Cycle 1 Wave 1.5 sub-cycle (R.D.1 revision)

**R.D.1 revision Agent: ADVANCED.** 565-line v2 artifact produced. Paper 8 now mirrors Paper 13 RH's actual one-dependency grammar. Applied the inference-from-source-check discipline INLINE before I-v6-1 was formally committed to v6 — first empirical validation of the patch. Primary-source verification performed: Paper 13 §1.5 disavowal (byte-accurate), Paper 13 proof skeleton (line 6 header), Paper 26 Theorem 13.1 ("Under the CBB axioms"), Paper 8 Theorem L.0 (H4 alone on face).

### Cycle 1 final-adversarial-pass (5 parallel Critics)

**Alpha-Critic (R.D.1-v2 ship-safety) SURVIVED.** 4/4 voice-shape pass with 123 markers independently counted. Paper 13 `00-proof-skeleton.md` grep for "CBB" returned ZERO matches across 234 lines — independent structural confirmation of one-dependency claim. All prior-art verbatim quotes verified. 6 low-priority W2 editorial-merge notes carried forward.

**Beta-Critic (K-1 + K-2 kill re-verification) VERIFIED at maximum strength.** 11 new variant candidates tested and all fail (7 for K-1 + 4 for K-2). Byte-for-byte re-run at mp.dps=200 with $N \in \{2, \ldots, 10000\}$ → 25/25 PASS zero residual. K-2 scope extended to cover `paper12/research/53` mechanism. Cross-paper insight: RH and H4 require structurally distinct NCG machinery.

**Gamma-Critic (cross-paper consistency) SURVIVED.** 17/18 chain state verified against PROOF-CHAIN.md §IV.1. Paper 13 + Paper 26 + Paper 10 Route 05 + Paper 12 relaxation/04 all cross-consistent. Unrelated housekeeping issue flagged: Paper 12 `relaxation/04` stale numbering (Paper 10 vs Paper 8 for YM).

**Delta-Critic (LOCK + 3× I-7 + joint P + I-5) VERIFIED all 6 attack vectors.** LOCK at 9/10 confirmed via 6 variant third-Route-A mechanisms (5 fail, 1 residual). 3× I-7 catches re-verified independently. I-v6-1 logical-entailment check caught additional refinement on CCM 2025 catch (rank-one vs QFT perturbation lexical category error). Joint P = 0.9910 verified symbolically + numerically. I-5 operational.

**Epsilon-Critic (blackboard integrity + bootstrap preview) WEAKENED → in-repair.** Blackboard §C/§D/§E/§F/§I body content was cycle-0 stale while §K commit memos documented Wave 1 events. Non-ship-blocking. §C, §F, §I body content fixed during cycle-close. §D/§E/§G/§H/§N body updates partially deferred.

## Findings by pattern category

- **Brief paraphrase errors (3)**: W7-14 §5.3 optimism (W1-A1), CCM 2025 "UV by construction" (W1-B1), Connes 2007 "running from $a_4$" (W1-C1). All caught by I-7 backward-verification. All cross-confirmed by Wave 1 Critics and re-verified by Delta-Critic final-adversarial-pass.
- **Structural inference errors (1)**: R.D.1 v1 "two-dependency template" claim drawn from Paper 13 §1.5 quote. Caught by R.D.1 Critic. Applied via Wave 1.5 sub-cycle revision + v6 bundle patch I-v6-1.
- **Lexical category errors (1)**: CCM 2025 "perturbation" means "rank-one perturbation of the spectral triple" (operator-theoretic), not QFT perturbation theory. Caught by Delta-Critic applying I-v6-1 logical-entailment check.
- **Analogy transfer errors (1)**: Paper 26 MY4 → Paper 8 H4 analogy breaks because BSD §§7-8 was algebraic and Paper 8's H4 core is not. Cross-finding W1-A1 + W1-B1.
- **Cross-paper architectural findings (1)**: RH and H4 require structurally distinct and incompatible NCG machinery. Meta-level observation from Beta-Critic.
- **Blackboard book-keeping gaps (1)**: cycle-0 section bodies not updated to reflect cycle-1 §K commit memos. Caught by Epsilon-Critic; partially repaired during cycle-close.
- **Paper 12 housekeeping issue (1, unrelated)**: `relaxation/04` stale Paper 10/Paper 8 numbering. Caught by Gamma-Critic; not propagated to H4 artifacts.

## Cascades propagated backward

- **R.A → R.B collapse**: the finding that Route B is a reformulation of Route A cascades backward — R.B's $p$ is not independent of R.A's. Joint probability computation updated to use $\max(p_A, p_B)$ instead of $(1-p_A)(1-p_B)$.
- **R.D.1 v1 → v2 template correction**: the inference error in v1 cascades through Theorem 1 body, Remark 1.A, Remark 1.B, §M summary, §I CONCERN. v2 revision corrects all 5 propagation points.
- **K-2 scope extension**: Beta-Critic's research/53 finding cascades backward to K-2's original scope note, adding a foreclosure clause for the framework-internal "QCD asymptotic freedom IS simple pole of $\zeta$ at $\beta=1$" mechanism.
- **v6 patch I-v6-1 application**: the R.D.1 Critic's finding cascades forward to all future v6 runs — Authors must now perform the inference-from-source check as part of Step 5.5 Way 1.

## Summary

Wave 1 produced 7 structurally irreversible events. The programme's joint $P$ cascaded from 0.9974 → 0.9910 through honest downgrades of Routes A/B/C, held stable by I-5's first-class HONEST-STALL discipline. The kill list grew by 2 (K-1 CCM port, K-2 spectral action). The §D toolkit grew by 7 new rows + 2 annotations. The v6 bundle grew by 1 patch (I-v6-1). R.D.1 revision was the one ship-critical correction; all others are §K commit memos + §D/§F book-keeping.

## What this discipline earned us

- **A ship-ready Paper 8 with an honest conditional.** Paper 8 was going to ship either way (Route D was first-class from cycle 0 per I-5). The discipline earned us the specific form: H4 in the W7-14 §5.3 mildest form, CBB as framework embedding via Paper 10/Appendix N, one-dependency grammar mirroring Paper 13 RH.
- **Two maximally-verified route-level kills.** K-1 and K-2 were attacked by 11 new variant candidates beyond the original kill cases, tested at mp.dps=200 with N up to 10000, and survived. Future runs won't need to re-test these — the kills are at maximum strength.
- **A cross-node structural LOCK at 9/10.** Taylor-coefficient identification is the attack surface and it is stuck. Future attack-route variations on this surface are unlikely to succeed without external unlocks (Borel summability, instanton obstruction).
- **A v6 bundle patch born from the run**: I-v6-1 (inference-from-source check). The next Clay-class closure run will have this discipline available, catching inference errors that I-7 alone would miss.
- **Empirical validation of I-5 + I-7 composition for cross-paper transfer**: BSD MY4 → Paper 8 H4. The two patches held the programme through three route downgrades and three paraphrase-error catches. Strong evidence both are load-bearing for any Clay-class run.
- **A cross-paper architectural finding**: the framework's NCG toolkit is not "one tool for all Clay problems" — RH and H4 require structurally distinct and incompatible NCG machinery. Useful for future programme architecture decisions.
- **A precision-verified kill**: the K-2 kill at mp.dps=200 across N = 2 to N = 10000 is the most thoroughly verified kill in the programme's history. SU(17) = 187/3 (the framework's $\alpha_{PS}^{-1}$), SU(1729) = 19019/3 (Hardy-Ramanujan), SU(10000) = 110000/3 (large-N stress). Exact rational, precision-invariant.
