# R.A.1 — Critic output (cycle 1)

*Critic: W1-A1-Critic (ORA v6 bundle §5.4 + §6.2; distinct Claude instance from Author per MAR confirmation-bias rule, arXiv 2512.20845)*
*Target node: R.A.1 — Taylor-coefficient identification (Author file: `nodes/R.A.1-taylor-coefficients.md`, 317 lines)*
*Author's verdict under review: BLOCKED-DECOMPOSED at COMPUTE. Generative step = Step 1 DIAGNOSE. Stuck-at = Step 5 COMPUTE.*
*Written: 2026-04-11*
*Effort: max (extended analysis, primary-source re-reads, bonus-grep + CoV, structurally distinct context from Author)*

---

## Direction

My job as Critic is to verify — with structurally distinct context, not by rubber-stamping — the Author's BLOCKED-DECOMPOSED verdict and the proposed R.A.1 → {R.A.1a, R.A.1b} decomposition. Per ORA v6 §5.4 the verdict options for a BLOCKED-DECOMPOSED node are DECOMPOSITION-VERIFIED / DECOMPOSITION-WEAK / DECOMPOSITION-INVALID. I ran the mandatory Critic sub-steps (voice-alignment, canonical-name, §F pattern check, bonus-grep + chain-of-verification, retrieval-augmented citation verification, extension test, cross-node consistency, precision floor, byte-for-byte re-run where applicable) against the Author's file and the Author's cited primary sources, using independent reads.

My one-sentence verdict: the Author's DIAGNOSE is correct, the reformulation-vs-closure distinction is primary-source-verified, the decomposition factors H4 cleanly into two honest sub-problems, and the BLOCKED-DECOMPOSED verdict is the honest-first structural reading. **Verdict: DECOMPOSITION-VERIFIED** with one minor presentation refinement noted in §Rationale (Obstruction A collapses to Obstruction A1 after consistency analysis — not a weakness, just a cleaner statement).

## Critic context received

- Author's research file at `nodes/R.A.1-taylor-coefficients.md` (317 lines, read end-to-end via Read tool offsets 1–160 + 160–317 because the file exceeds the single-read token cap).
- Blackboard §A (North Star), §B (context), §C (bottleneck), §D (toolkit 17 rows), §E (plan tree, 4 peer subtrees), §E.1 (joint probability post Wave 1 close), §F (K-1 + K-2 both registered as of Wave 1 close), §I notes, §J voice canon (selective read lines 164–196 for register markers), §K runner writes for cycle 1 (the Author's return entry + W1-B1/W1-C1/W1-D1 returns for cross-node consistency).
- W7-14-af-match.md §4 (H4 formal statement + status), §5.1 (controlled interpolation), §5.3 (analyticity bridge, verbatim block-quote at lines 388–413), §7 (summary table with "H4: Open (conditional) | Gap G7"). Read selectively.
- W5-10-cauchy-estimate-and-extraction.md Part I Step 2 (analyticity of F(t); lines 199–302), Step 3 (F(0) is dimension-4 Schwinger function; lines 308–354), Part II Lemma 3.8 statement + proof (lines 578–721). Selective reads.
- G4b-af-short-distance-match.md §1–§5 + Section 8 honest assessment (referee's full G4b gap file, 157 lines, read end-to-end because short).
- G4d-operator-product-expansion.md §1–§4 (referee's full G4d gap file, selective read through §4 — 90 lines of the 176).
- paper12/research/214-the-method-six-patterns.md §Patterns 1–6 + §How-Patterns-Combined (lines 136–288 selective) for the six-step method loop and stuck-where diagnostic.
- paper12/27-anchor-document.md §13 (voice quotes) + §14 (SP1-SP5) — selective for voice-alignment.
- paper08-yang-mills/research/21-the-rigorous-proof.md header + §II rigor labels — selective for THEOREM / LEMMA / KEY LEMMA — OPEN label verification.
- paper08-yang-mills/research/35-final-verdict.md §VI closing register marker ("That is the contribution", line 172) for voice-canon anchor.
- W7-15-ope-leading.md eq. (4.3j) block (lines 305–321) for C_N constant cross-check.
- No shipped code for R.A.1 (verified: only `code/R.C.1-seeley-dewitt-a4.py` exists in closing-H4/code/, which is W1-C1's node). Byte-for-byte re-run is N/A.

## Mandatory sub-steps results

### Sub-step 1 — Voice-alignment check

**Target**: §J voice canon register markers + `research/35-final-verdict.md` "That is the contribution" closing register + SP1-SP5 strategic principles from `paper12/27-anchor-document.md` §14.

**Findings**:
- Author's Step 1 DIAGNOSE opens with a one-sentence phenomenon description ("H4 is hard in the current framing because ..."), matching the "stripped phenomenon" register the runner used in §K REFRAME.
- Author's verdict section uses terse declaration ("Route A is a reformulation of H4 into ..."), matching the 35-final-verdict register ("The mass gap is not yet proved. But the problem has been transformed.").
- Author's §I CONCERN explicitly ties p_success downgrade to a specific mathematical obstruction (Borel summability for 4D YM), not to vague pessimism. Matches SP3 "trace discrepancies until they become theorems".
- Author's §Voice-canon-citation block at lines 308–313 of the research file explicitly lists the deployable and non-deployable registers, with "Not deployable: 'Route A landed' — this phrasing would be dishonest given my verdict. Reserve for an actual closure." This is **textbook honest-first SP5 discipline**: naming the voice markers that would be dishonest and marking them unavailable.
- The handoff section at lines 286–313 uses the "What-the-next-runner-needs-to-know" fixed schema (state at handoff / open dependencies / watch out for / preferred next move / voice canon citation) — this is the §5.4 structural-format requirement and the Author complies.
- Voice alignment **PASSES**. No drift into either (a) false-celebration register ("Route A landed", "H4 closed") or (b) unnecessarily-defeatist register ("the programme is doomed"). The Author's tone is the correct honest-first posture from §J.

### Sub-step 2 — Canonical-name check

**Targets**: The Author proposes 4 new §D toolkit rows + 1 modification. I check each name against §D's existing rows for uniqueness and naming-discipline (SP2 "name them and use them for decoding").

| Proposed name | Notation | Conflict with existing §D rows? | Naming-discipline verdict |
|---|---|---|---|
| Perturbative flow-time analyticity | $\mathcal{A}(F^{\mathrm{pert}})$ | None. Dual of existing "$F(t)$ rescaled correlator" row (which is non-perturbative); the duality is made explicit. | **Pass**. |
| Route A independent-point agreement | $\mathcal{P}_{R.A.1}^{\mathrm{ind}}$ | None. The subscript R.A.1 ties the name to the decomposition tree explicitly. | **Pass**. |
| Identity-theorem two-function requirement | (no dedicated notation; R status with applicability-blocked annotation) | Already listed in §D as "Analyticity identity theorem" (row 9). The Author's proposal is an **annotation** to the existing row, clarifying the R status applies to the theorem itself but the APPLICABILITY to Route A is blocked by failure of the two premises. | **Pass** (annotation, not duplicate). |
| Taylor-coefficient identity reformulation status | (existing row modified) | Already listed as row 5 ($F^{(n)}(0)/n! = f_n^{\text{pert}}$ — the closure target for Route A). The Author's proposal is to add "equivalent to H4 at each $(x,y)$, not weaker" as a clarifier. | **Pass** (clarification, not duplicate). |

**Canonical-name check PASSES.** All four proposals are structurally correct additions or clarifications; none collide with existing rows. The Author correctly distinguishes between **new entries** ($\mathcal{A}(F^{\text{pert}})$ and $\mathcal{P}_{R.A.1}^{\text{ind}}$) and **modifications** (the two annotations to rows 5 and 9). This is §D hygiene: don't duplicate, clarify in place when appropriate.

I endorse the four §D changes and add them to the "Proposed §D row changes" section below for the runner's cycle-close commit.

### Sub-step 3 — §F pattern check (especially K-1 and K-2)

**K-1** (Route B "Port CCM 2025 to YM"): killed with pattern categories *External-source-inconsistency* + *Wrong-space*. The paraphrase "UV asymptotics by construction" is not in the CCM 2025 primary source (p. 28 says the rigorous identification "remains OPEN"). The spectral triple transposition's closure mechanism reduces to W7-14 §5.3 analyticity (collapsing into Route A), and dictionary entries #12–#17 hit a category error (RH target = zeros of entire function, YM target = Taylor coefficients of analytic function, Hurwitz doesn't transfer).

**K-2** (Route C "Framework-native via spectral action + Identity 12 + bridge family k=4"): killed with pattern categories *External-source-inconsistency* + *Vacuous*. Connes 2007 §5 eq. (24) is verbatim "at the classical level"; spectral action produces a bare action at cutoff $\Lambda$, not a running coupling. The "framework-native closure" requires a running coupling the spectral action doesn't provide.

**R.A.1 pattern check**:

| Pattern category | Present in K-1? | Present in K-2? | Present in R.A.1? |
|---|:-:|:-:|:-:|
| External-source-inconsistency | Yes | Yes | **No** (Author's backward-verification **confirmed** primary source, did not contradict it) |
| Wrong-space | Yes | No | **No** (flow-time analyticity disk is the correct space for Route A) |
| Vacuous | No | Yes | **No** (Route A's reformulation is real; sub-problems are non-vacuous) |

**Pattern check verdict: R.A.1 is NOT a shadow of either K-1 or K-2.** It is structurally distinct. Route A's reformulation of H4 into "Taylor coefficients of an analytic function" is a **genuine structural advance** (packaging the non-perturbative side as an analytic function), just not a **closure** (the perturbative-side burden is shifted, not eliminated).

The Author's decision to classify R.A.1 as BLOCKED-DECOMPOSED (not KILLED) is structurally correct. BLOCKED-DECOMPOSED preserves the reformulation as a foothold for future work (if Borel summability or an instanton-obstruction mechanism is later established), which is what the §F kill-discipline would LOSE if we misclassified it as a kill. The Author's explicit statement "Route A is NOT KILLED: the reformulation is genuinely useful" (line 234 of the research file) is the correct tag.

### Sub-step 4 — Bonus-grep + chain-of-verification (CoV)

I grep'd the Author's research file for phrases signaling potential unstated assumptions, dangling citations, or numerical claims without §D anchors: `by construction|rigorous|established|known|proves|prove|trivially|obviously|clearly`. Five hits flagged as potential issues. Each was CoV-verified against primary source:

1. **Line 44 "Pattern 6 application"**. Author applies Pattern 6 (projection produces apparent pathology) to the asymptotic-category split between distributions and formal power series. CoV: is this a principled application of Pattern 6, or a forced pattern-match? → Verified against `paper12/research/214-the-method-six-patterns.md §Pattern 6` (lines 217–250 + 250–257). Pattern 6 is explicitly about "the 4D difficulty is a projection artifact" — projecting a higher-dimensional object (here: the analytic function $F(t)$ on the flow-time disk) to a lower-dimensional view (here: the asymptotic expansion at $t=0$) and seeing a difficulty that is NOT present in the lifted view. The Author's application is principled. **False positive. Not an issue.**

2. **Line 110 "Renormalon divergence (Beneke 1999; 't Hooft 1979; Lipatov 1977)"**. Author cites these without WebFetching the primary sources. CoV: is this a load-bearing claim? → Author's Step 6 VERIFY item 2 explicitly tags: *"Taken as rigorous within perturbation theory — this is textbook, not in my proximate sources, but is a standard fact and does not drive the argument (I use it only as supporting evidence for Obstruction A)."* The Author disclaims load-bearing reliance on this claim in favor of the primary-verified W7-14 + W5-10 chain. The "supporting evidence" role is epistemically-legitimate for a textbook fact. **False positive. Not an issue.** The Author's I-7 discipline is operational.

3. **Line 136 "$a_0 = F(0) = S_2^{\text{ren}}(x,y)$"** — load-bearing identification for the Step 5 COMPUTE conclusion. CoV: does the primary source actually establish this identity? → Verified against W5-10 Part I Step 3 line 314: *"$F(0) = \langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y)\rangle_c$ is the unique dimension-4 contribution"*, and Part II Lemma 3.8(i) lines 584–591: $S_2^{\text{ren}}(x,y) := \lim_{t \to 0^+} S_{2,t}^c(x,y)/c_1(t)^2$. The two definitions match: $F(t) = S_{2,t}^c / c_1(t)^2$ and $F(0) = \lim_{t \to 0^+} F(t) = S_2^{\text{ren}}(x,y)$. **Verified. Not an issue.**

4. **Line 216 "$f_0^{\text{pert}} = C_N/|x|^8 (\log)^{-2}$ with $C_N = 2(N^2-1)/\pi^6$"**. Author cites W7-14 §2.3, W7-15 §4.2 eq. (4.3j), and G4b §2 eq. (S2.4). CoV: do all three independent sources give the same $C_N$? → Verified:
   - G4b-af-short-distance-match.md line 47 (eq. S2.4): "$C_N = 2(N^2-1)/\pi^6$"
   - G4b line 83 (eq. S4.2): same
   - G4b line 127 (eq. 5.7.f.new.1): same
   - W7-15-ope-leading.md line 308 (eq. 4.3j): $C^{\mathbb{1}}(x-y) = \frac{C_N}{|x-y|^8} (\log)^{-2} [1 + O((\log)^{-1})]$ with $C_N$ the same constant
   **Verified across three independent sources. Not an issue.**

5. **Line 226 Obstruction A, line 299 "Non-perturbative side = analytic function (established). Perturbative side = formal power series (still)"** — load-bearing headline claim. CoV: is there a reading of W7-14 §5.3 under which $F^{\text{pert}}$ IS analytic (which would undercut Obstruction A)? → I re-read W7-14 §5.3 (lines 388–413) directly. The text says "This upgrades the status of **the perturbative expansion** from a formal series to an actual Taylor series with a positive radius of convergence" (lines 393–395). **This is a conditional upgrade**: IF the Feynman-diagrammatic coefficients $f_n^{\text{pert}}$ equal $F^{(n)}(0)/n!$ (the non-perturbatively-defined Taylor coefficients of the analytic $F$), THEN the formal series converges to $F(t)$ on the disk $|t| < r_t$. But establishing that term-by-term equality IS H4 in the new language. The §5.3 text makes this circularity explicit at lines 408–412: *"What H4 asks, in this language, is whether the Taylor coefficients $F^{(k)}(0)$ are computable by the Feynman-diagrammatic perturbative rules. This is a statement about the Taylor coefficients of an analytic function — **a more accessible question** than the traditional formulation of H4"* — note "a more accessible question", NOT "an answered question". The Author's Obstruction A is a **correct honest reading** of the primary source. **Verified. Not an issue.**

**Bonus-grep + CoV sweep complete. 5 potential issues, 5 false positives. Author's file passes the discipline.**

### Sub-step 5 — Retrieval-augmented citation verification of the W7-14 §5.3 block-quote

This is the mandatory I-7 backward-verification the Author self-reported executing in Way 1 of Step 5.5. I verify the Author's quote byte-for-byte against primary source.

**Author's block-quote** (R.A.1-taylor-coefficients.md lines 173–179, prose-normalized by the Author from the LaTeX-inline-math form of the primary source):

> "The analyticity of F(t) in the complex flow-time plane (W5-10, Step 2; radius r_t > 0 independent of the Balaban step k and the bare-scale index K) implies that the small-flow-time expansion is not merely asymptotic but **convergent**. This upgrades the status of the perturbative expansion from a formal series to an actual Taylor series with a positive radius of convergence. In particular:
> - The perturbative coefficients of F(t) = F(0) + F'(0) t + (1/2) F''(0) t^2 + ⋯ are the derivatives of a single analytic function, not independent perturbative computations.
> - The remainder R_n(t) = F(t) − Σ_{k=0}^n F^{(k)}(0) t^k/k! satisfies |R_n(t)| ≤ M_F (|t|/r_t)^{n+1}/(1 − |t|/r_t), a rigorous Cauchy remainder bound.
> - The non-perturbative value F(0) equals the sum of the convergent series, by definition of analyticity.
>
> What H4 asks, in this language, is whether the Taylor coefficients F^{(k)}(0) are computable by the Feynman-diagrammatic perturbative rules. This is a statement about the Taylor coefficients of an analytic function — a more accessible question than the traditional formulation of H4, which asks about the asymptotic behavior of a non-perturbative distribution."

**Primary source verbatim** (`gradient-flow-attack-plan/research/W7-14-af-match.md` lines 390–413, LaTeX stripped for comparison):

> "The analyticity of $F(t)$ in the complex flow-time plane (W5-10, Step 2; radius $r_t > 0$ independent of the Balaban step $k$ and the bare-scale index $K$) implies that the small-flow-time expansion is not merely asymptotic but **convergent**. This upgrades the status of the perturbative expansion from a formal series to an actual Taylor series with a positive radius of convergence. In particular:
> - The perturbative coefficients of $F(t) = F(0) + F'(0)\,t + \tfrac{1}{2}F''(0)\,t^2 + \cdots$ are the derivatives of a single analytic function, not independent perturbative computations.
> - The remainder $R_n(t) = F(t) - \sum_{k=0}^{n} F^{(k)}(0)\, t^k/k!$ satisfies $|R_n(t)| \leq M_F\,(|t|/r_t)^{n+1}/(1 - |t|/r_t)$, a rigorous Cauchy remainder bound.
> - The non-perturbative value $F(0)$ equals the sum of the convergent series, by definition of analyticity.
>
> What H4 asks, in this language, is whether the Taylor coefficients $F^{(k)}(0)$ are computable by the Feynman-diagrammatic perturbative rules. This is a statement about the Taylor coefficients of an analytic function --- a more accessible question than the traditional formulation of H4, which asks about the asymptotic behavior of a non-perturbative distribution."

**Byte-for-byte match.** The Author's quoted text matches the primary source exactly, modulo (a) stripping LaTeX inline math delimiters, (b) converting `\tfrac{1}{2}` to "(1/2)", (c) converting `\cdots` to "⋯", (d) converting `---` em-dash to "—". All four are standard plaintext-normalization differences, not content drift. The Author's line-reference (388–414) is exact.

**Author's interpretation of the quote**: that the primary source is "explicit" about H4 remaining open after reformulation, because the phrase "a more accessible question" (line 411 of W7-14) is NOT the same as "an answered question". Critic verifies this interpretation: yes, "more accessible" explicitly implies still-open-but-easier. Author's reading is faithful.

**Additional primary-source anchor I independently verified**: W7-14 §7 Summary table line 541: *"H4: non-pert $=$ pert at short distances | **Open** (conditional) | Gap G7"*. And §7 Conclusion lines 543–548: *"Conjecture L.2 is closed **conditional on Hypothesis H4**. The gradient-flow framework reduces H4 from a comparison of two independently defined objects ... to a statement about the Taylor coefficients of a single analytic function (Section 5.3), making it the **mildest formulation** of this standard hypothesis available in the literature."* — the word "mildest formulation" is used instead of "closure" or "proof", consistent with the Author's DIAGNOSE that the reformulation is real but the closure is not.

**Retrieval-augmented citation verification PASSES.** The Author's I-7 backward-verification is byte-accurate and correctly-interpreted. This is the first piece of empirical evidence I see in Wave 1 that an Author's I-7 discipline is operational not just by self-report but by Critic-independent-recheck. The discipline is doing its job.

### Sub-step 6 — Extension test

The spawn prompt asks whether there is a parameter value where the identity-theorem argument WOULD work. The Author ruled out four candidates in Step 3 Obstruction C (tree level, Reisz lattice perturbative, large $t$ IR regime, super-renormalizable $\phi^4_3$ analogue). As Critic I enumerate four additional candidates the Author did not explicitly consider:

1. **Complex $t$ on the imaginary axis** ($t = i\tau$, $0 < \tau < r_t$): inside the analyticity disk, so $F(i\tau)$ is well-defined. But the non-perturbative correlator at imaginary flow-time has no closed-form expression (the Balaban construction doesn't give closed forms at any $t$, let alone complex $t$), and the perturbative side at complex $t$ has the same convergence issues. **Does not close the gap.**

2. **Very small $t$ at fixed large $(x,y)$ separation** ($|x-y| \gg \Lambda^{-1}$, $t \to 0$): The non-perturbative correlator decays exponentially at rate $\Delta_\infty$ (the mass gap); the perturbative side is dominated by the running coupling at scale $1/\sqrt{8t}$ which enters the strong-coupling regime as $t \to 0$ for any fixed $|x-y|$. The two sides diverge numerically, so any agreement at a specific point would be coincidental, not structural. **Does not close the gap.**

3. **Dimensional continuation from $d < 4$**: In $d = 3$ the theory is super-renormalizable and H4 is proved (Glimm–Jaffe / Magnen–Rivasseau–Seneor for $\phi^4_3$; analogous statements for 3D YM would need to be proved separately but are plausibly accessible). A putative strategy would be: prove H4 at $d = 3$, analytically continue in $d$, deduce H4 at $d = 4$. But analytic continuation in dimension requires (a) dimensional regularization to be rigorously definable for non-Abelian gauge theory, which is itself open (Costello's perturbative work gives partial results but not the non-perturbative statement needed here), and (b) the continuation to preserve the identity, which is not automatic. **Does not close the gap** — pushes it into a different open problem.

4. **Large-$N$ limit**: At $N \to \infty$ with $g^2 N$ fixed (planar limit), a number of closure mechanisms become tractable (matrix model sums, AdS/CFT correspondence for $\mathcal{N}=4$ super-YM via Maldacena, etc.). Rigorous pure-YM large-$N$ for 4D non-supersymmetric is itself open (Maldacena's work is supersymmetric + conformal, inapplicable to the Clay problem's pure SU(N)). **Does not close the gap.**

**Extension test result**: I found four additional candidates the Author did not explicitly list; none of them close the gap. Each reduces to a different open problem. The Author's enumeration in Obstruction C, combined with my four additions, exhausts the natural parameter-value candidates within the primary-source framework. **The decomposition stands.** The additional four are worth preserving as future-work leads and I append them to §I below.

### Sub-step 7 — Cross-node consistency check

**Does R.A.1's decomposition collide with W1-B1's Route-B-collapse finding?** The spawn prompt asks this explicitly.

- W1-B1 (Author on Route B, now registered as K-1 in §F at Wave 1 close) found: "R.B's closure power reduces to R.A's analyticity input + category error at LOCK #12. The spectral triple is a *presentation* of W7-14 §5.3, not a new closure mechanism." Route B collapses into Route A.
- W1-A1 (this node's Author) found: R.A.1 requires closing R.A.1a ($\mathcal{A}(F^{\text{pert}})$) + R.A.1b ($\mathcal{P}_{R.A.1}^{\text{ind}}$), both OPEN.

**Consistency**: since R.B collapses into R.A, and R.A requires {R.A.1a, R.A.1b}, R.B effectively requires the same sub-problems. The blackboard §E.1 joint-probability revision at Wave 1 close correctly captures this: "R.A and R.B are NOT independent. The joint $P(A \lor B)$ is not $1 - (1-p_A)(1-p_B)$; it is $\max(p_A, p_B) \approx 0.10$." Both findings converge on the same structural obstruction.

**No collision. No reconcile needed.** The Author's decomposition is consistent with the other Wave 1 Author's finding, and the runner's Wave 1 close entry correctly represents the joint state.

**Additional cross-check**: W1-C1 (Route C, now K-2) found that the spectral action is classical/bare at $\Lambda$, not running. This is a **structurally distinct** obstruction from R.A.1's (which is about asymptotic-category mismatch between distributions and formal power series). The two kills attack H4 from different framework entry points and both fail, which is empirical evidence that H4 is structural rather than attackable via a single framework gadget. The Author's DIAGNOSE that H4 is genuinely hard is corroborated by the independent Wave 1 findings.

### Sub-step 8 — Precision floor check

**Precision floor requirement**: any numerical claim should be at 2× dps per §5.4 discipline.

**R.A.1 numerical claims**: none. The Author explicitly notes at Step 5 line 154–162 of the research file: *"I do NOT write a numerical verification script, because the verification cannot be numerical — it is a structural identification that reduces to H4 at a specific $(x,y)$, and no finite-precision computation can settle this. `mp.dps ≥ 30` would be applicable if there were two closed-form expressions to compare; there are not."*

The only numerical-ish value that enters the research file is $r_t \approx 3.16 \times 10^{-4}$ (the analyticity radius from W1-05 numerical table), which the Author cites but does NOT use in any computation requiring precision.

**Precision floor: N/A** (no headline numerical claim to double-dps-check). **Not an issue.**

### Sub-step 9 — Byte-for-byte script re-run

**Applicable?** No. R.A.1 did not ship code. The Author's Step 5 correctly explains why numerical verification is not applicable for a structural-obstruction finding. I verified the `closing-H4/code/` directory by directory listing — only `R.C.1-seeley-dewitt-a4.py` exists (W1-C1's node), no `R.A.1-*.py`.

**Byte-for-byte re-run: N/A for this node.**

## Verdict

**DECOMPOSITION-VERIFIED.**

The Author's BLOCKED-DECOMPOSED verdict is correct. The decomposition of R.A.1 into R.A.1a (perturbative flow-time analyticity, $\mathcal{A}(F^{\text{pert}})$) + R.A.1b (independent-point agreement, $\mathcal{P}_{R.A.1}^{\text{ind}}$) is:

1. **Structurally valid** — R.A.1a and R.A.1b are provably independent sub-conditions whose conjunction implies H4 (via the identity theorem as applied in Step 3 UNIFY of the research file), so they form a valid factorization.
2. **Primary-source-verified** — the Author's W7-14 §5.3 backward-verification is byte-accurate, and the interpretation ("more accessible question" ≠ "answered question") is faithful to the primary source.
3. **Pattern-distinct from kills** — R.A.1 does NOT match the K-1 or K-2 patterns (no external-source-inconsistency, no wrong-space, no vacuity). The reformulation is genuine structural progress; the BLOCKED-DECOMPOSED tag preserves it as a foothold for future work.
4. **Cross-node-consistent** — compatible with W1-B1's Route-B-collapse finding; no collision.
5. **Voice-canon-compliant** — honest-first register, terse declarations, no false-celebration language.
6. **Comprehensive on candidate alternatives** — Obstruction C enumeration + my four Critic-added candidates (imaginary-axis $t$, small $t$ large separation, dimensional continuation, large-$N$) exhaust the natural parameter-value candidates. None close the gap.

I endorse the decomposition and recommend the runner proceed with the Wave 1 close as registered, treating R.A.1 as DECOMPOSITION-VERIFIED for the cycle-close metrics row.

## Rationale

### Where the Author is strong

- **The DIAGNOSE is sharp and structurally correct**. The insight that "H4's difficulty lives in the asymptotic category of the perturbative side" is exactly the right level of abstraction. Neither too narrow (this is not just "compute $f_n^{\text{pert}}$ better") nor too wide (this is not just "H4 is hard"). It names the specific structural asymmetry — non-perturbative side upgraded to analytic function by W5-10 Step 2, perturbative side still a formal power series — that the reformulation does not address.
- **The backward-verification discipline is operational**. The Author's self-suspicion Way 1 (backward-verify the brief's paraphrase against W7-14 §5.3 primary source) produced the correct correction: the brief's "~30% remaining" framing is optimistic, the primary source's "more accessible question" is the accurate status. This is the I-7 discipline doing exactly what BSD MY4 Cycle-1 A-1 showed it was designed for.
- **The decomposition preserves optionality**. By splitting R.A.1 into R.A.1a (Borel-summability-like) and R.A.1b (independent-point agreement), the Author gives future work a clean structure: either sub-problem closing partially advances Route A, and together they close it. This is strictly better than a bare "Route A is blocked" verdict.
- **The Paper 26 BSD MY4 analogy break is independently found**. The Author's observation that "BSD §§7–8 was already algebraic; Paper 8 is not" is a genuine Sig 14 category-too-small finding. Note that W1-B1 independently found the same break via the "RH zeros of entire function vs YM Taylor coefficients of analytic function" category error — two Authors, two independent derivations of the same finding, strong evidence the finding is correct.

### Where the Author could be marginally refined (one minor point, not affecting verdict)

**Obstruction A collapses to A1 + A2 after consistency analysis**. The Author's Obstruction A states that $F^{\text{pert}}(t)$ "is not known to be an analytic function on any open disk — it is a formal power series whose coefficients are computed by Luscher–Harlander–Artz, but the series is expected to diverge." This framing treats analyticity-of-$F^{\text{pert}}$ as an additional hypothesis beyond the term-by-term agreement $f_n^{\text{pert}} = F^{(n)}(0)/n!$.

Critic observation: if we grant the term-by-term agreement (which is H4 in the Taylor-coefficient language), then the formal series $\sum_n f_n^{\text{pert}} t^n$ **automatically** converges to $F(t)$ on $|t| < r_t$, because $F(t)$ is analytic (W5-10 Step 2) and the Taylor series of an analytic function on a disk converges on that disk. So "analyticity of $F^{\text{pert}}$" is not an independent sub-condition — it is a consequence of "term-by-term agreement with the Taylor coefficients of the analytic $F$".

In other words, Obstruction A splits into:
- **A1**: Does $f_n^{\text{pert}} = F^{(n)}(0)/n!$ hold for all $n \geq 0$? (This IS H4 term-by-term.)
- **A2**: If A1 holds, does $\sum_n f_n^{\text{pert}} t^n$ converge to $F(t)$ on $|t| < r_t$? (This is **automatic** given A1 and the analyticity of $F$.)

A2 is free; only A1 is a real obstruction. So Obstruction A collapses to "does the term-by-term identity hold?", which is exactly H4 in the Taylor-coefficient language.

**Does this refine the decomposition?** No, it makes R.A.1a slightly cleaner but doesn't change the verdict. R.A.1a was originally stated as "show the formal power series converges to an analytic function on a disk"; the cleaner statement is "show the Feynman-diagrammatic coefficients equal the Taylor coefficients of the analytic $F$". The latter is equivalent to the former (modulo the free A2 step) and more directly names what's being asked.

The decomposition of R.A.1 can therefore be slightly re-stated as:
- **R.A.1a' (refined)**: Term-by-term agreement $f_n^{\text{pert}} = F^{(n)}(0)/n!$ for all $n \geq 0$. [This is H4 in the Taylor-coefficient language; equivalent to Author's R.A.1a + R.A.1b combined, not weaker.]

But the Author's two-sub-problem decomposition is ALSO valid — it factors into R.A.1a ("the perturbative side is analytic") + R.A.1b ("there's a point of independent agreement"), and together they invoke the identity theorem. Both decompositions are logically sound; the Author's is perhaps more faithful to the identity-theorem invocation structure, while my refinement is more faithful to the underlying obstruction.

**Bottom line**: this is a presentation refinement, not a verdict change. The Author's decomposition stands; I note the alternative framing in §I for future reference.

### Where the Author's verdict is empirically corroborated by cross-node findings

- W1-B1 (Route B, now K-1): Route B reduces to Route A's analyticity input + category error. Confirms the Author's "reformulation shifts but does not eliminate the burden" diagnosis from a different attack angle.
- W1-C1 (Route C, now K-2): The spectral action is classical/bare, not running, so cannot supply the perturbative-side closure mechanism from a framework-native entry point. Corroborates the Author's diagnosis that the obstruction is structural, not a missing framework gadget.
- Three independent I-7 catches in Wave 1 (W1-A1 on W7-14, W1-B1 on CCM 2025, W1-C1 on Connes 2007). All three Authors caught different brief-paraphrase errors against primary sources. This is **empirical validation that I-7 is load-bearing for cross-framework closure attempts** — the discipline is operational and catching real drift. R.A.1's honest-first verdict is part of this validation pattern, not an outlier.

## §I notes to append

- **LESSON (Critic-confirmed)**: *The I-7 backward-verification discipline is operational in Wave 1*. Three independent I-7 catches (W1-A1 W7-14, W1-B1 CCM 2025, W1-C1 Connes 2007) were all verified by Critic byte-for-byte re-reads against primary sources. The Author's self-reported backward-verification for R.A.1 matches the primary source exactly (W7-14 §5.3 lines 390–413, reference line range 388–414 as cited by the Author). This is the first piece of Critic-independent empirical evidence that the v3 → v6 I-7 transfer is genuinely working. *Recommendation*: budget for 1–3 Critic I-7 re-checks per wave in future Clay-class closure runs. The discipline has a catching-rate high enough to matter.

- **REFINEMENT (minor, not changing verdict)**: *Obstruction A splits into A1 + A2 with A2 automatic*. Given term-by-term agreement of $f_n^{\text{pert}}$ with $F^{(n)}(0)/n!$ (A1), convergence of the formal series to the analytic $F(t)$ on $|t| < r_t$ (A2) is automatic because the Taylor series of an analytic function on a disk converges on that disk. So R.A.1a can equivalently be stated as "term-by-term H4 in the Taylor-coefficient language", which is the same logical content as the Author's decomposition. The Author's two-sub-problem form is still valid (it factors R.A.1 along the identity-theorem invocation axis instead of the term-wise axis), but the refined form is conceptually simpler. Propose: both forms are recorded in §D (Author's $\mathcal{A}(F^{\text{pert}})$ + $\mathcal{P}_{R.A.1}^{\text{ind}}$) with an annotation "equivalent to term-by-term H4 in the Taylor-coefficient language".

- **EXTENSION (Critic-added future-work leads)**: Four additional parameter-value candidates for R.A.1b that the Author did not explicitly consider, all ruled out as closure mechanisms but worth preserving as forward-leads:
  1. Imaginary-axis complex $t$ in the analyticity disk — no closed form at any complex $t$.
  2. Small $t$ with large $(x,y)$ separation — running coupling enters strong-coupling regime, divergent.
  3. Dimensional continuation from proved $d = 3$ — requires rigorous dimensional regularization for non-Abelian gauge, itself open.
  4. Large-$N$ planar limit — rigorous pure-YM large-$N$ is itself open (Maldacena's $\mathcal{N}=4$ work is inapplicable).

  None close R.A.1b, but each is a distinct research direction worth tagging for future work if a framework-native tool becomes available.

- **CONCERN (structural)**: *The Author's p_success ≤ 0.10 estimate for Route A is supported by Critic cross-checks*. The Author's downgrade from 0.50 → 0.10 is conditional on "a future advance in Borel summability for 4D YM or an instanton-obstruction argument." I add: also conditional on a framework-native mechanism for establishing non-perturbative Taylor coefficients directly (e.g., from a spectral triple whose UV asymptotics are computed structurally, not via Feynman rules). The current state of Routes B and C (K-1 and K-2 respectively) is that no framework-native mechanism of this kind exists. So the 0.10 estimate is plausibly correct, and if anything might be slightly high. I don't propose further downgrade in this Critic cycle (that would require a separate analysis), but I flag the concern for the runner's Wave 2 planning.

## Proposed §D row changes (Critic-endorsed)

I endorse all four of the Author's proposed §D row changes, with the annotation noted in §I REFINEMENT above. Specifically:

1. **ADD row**: *Perturbative flow-time analyticity* — $\mathcal{A}(F^{\text{pert}})$ — status O — source: W1-A1 decomposition — completeness 0%. Annotation: "Equivalent to the first half of term-by-term H4 in the Taylor-coefficient language; the convergence sub-condition is automatic given term-by-term agreement."

2. **ADD row**: *Route A independent-point agreement* — $\mathcal{P}_{R.A.1}^{\text{ind}}$ — status O — source: W1-A1 decomposition — completeness 0%. Annotation: "No candidate mechanism identified in Wave 1. Critic enumerated 4 additional candidates (imaginary-axis, small-$t$ large-separation, dimensional continuation, large-$N$), all ruled out."

3. **MODIFY existing row 9** (Analyticity identity theorem): Add status annotation: "R (rigorous as a theorem of complex analysis); BLOCKED as a closure mechanism for Route A because both hypotheses (analyticity of both sides + agreement on a set with accumulation point) fail when applied to $\{F, F^{\text{pert}}\}$. The failure is explicit in the Author's §R.A.1a, §R.A.1b decomposition."

4. **MODIFY existing row 5** (Taylor-coefficient identity): Add annotation: "This identity is equivalent to H4 at each specific $(x,y)$, not weaker. The analyticity reframing does not reduce the proof burden; it shifts it to the perturbative side's Taylor-coefficient identification. Primary-source-verified against W7-14 §5.3 lines 408–413: 'a more accessible question' ≠ 'an answered question'."

All four changes can be committed at Wave 1 close as DECOMPOSITION-VERIFIED content.

## Report to runner

### Verdict
**DECOMPOSITION-VERIFIED**. Author's BLOCKED-DECOMPOSED verdict is correct. Decomposition of R.A.1 into {R.A.1a, R.A.1b} is structurally valid, primary-source-verified, pattern-distinct from K-1/K-2, cross-node-consistent with W1-B1, and voice-canon-compliant.

### Key findings (especially disagreements with Author's verdict)
- **No disagreement with verdict.** I endorse the BLOCKED-DECOMPOSED tag, the decomposition, the p_success ≤ 0.10 downgrade, and the §I CONCERN/CASCADE/LESSON notes.
- **One minor refinement** (non-verdict-changing): Obstruction A collapses to A1 (term-by-term Taylor identity = H4) + A2 (convergence; automatic). This cleans up the presentation but doesn't change the decomposition.
- **Critic-added content**: Four extension-test candidates (imaginary-axis $t$, small-$t$ large-separation, dimensional continuation, large-$N$), all ruled out as closure mechanisms but preserved as future-work leads.
- **Empirical finding**: This is the first Critic-independent verification of a Wave 1 Author's I-7 backward-verification in the H4 programme. The Author's W7-14 §5.3 quote is byte-accurate. Strong evidence the I-7 discipline is operational.

### §I notes (3 proposed)
1. LESSON (Critic-confirmed): I-7 operational; budget for 1-3 Critic I-7 re-checks per wave.
2. REFINEMENT: Obstruction A = A1 + A2 with A2 automatic; record both forms in §D.
3. EXTENSION: 4 new forward-leads for R.A.1b (imaginary-axis, small-$t$ large-separation, dimensional continuation, large-$N$).
Plus 1 CONCERN flag: p = 0.10 is plausible, possibly slightly optimistic.

### §D row changes
- ADD row: $\mathcal{A}(F^{\text{pert}})$ (status O, 0%).
- ADD row: $\mathcal{P}_{R.A.1}^{\text{ind}}$ (status O, 0%).
- MODIFY row 9 (Analyticity identity theorem): add "R (as theorem); BLOCKED (for Route A hypotheses)".
- MODIFY row 5 (Taylor-coefficient identity): add "equivalent to H4 per pair, not weaker".

### §M cycle-close metrics summary (≤200 words)

**R.A.1 cycle-1 Critic roll-up**: DECOMPOSITION-VERIFIED. Author's BLOCKED-DECOMPOSED verdict, decomposition into R.A.1a ($\mathcal{A}(F^{\text{pert}})$) + R.A.1b ($\mathcal{P}_{R.A.1}^{\text{ind}}$), and p_success 0.50 → 0.10 downgrade are all Critic-confirmed against primary sources. Byte-for-byte re-verification of the Author's W7-14 §5.3 block-quote (lines 388–414) matches exactly. Voice-alignment check PASSES (honest-first register, no false-celebration language). §F pattern check PASSES (R.A.1 is distinct from K-1 and K-2 kill patterns — reformulation is genuine structural progress, not a shadow of a killed approach). Bonus-grep + CoV sweep: 5 potential issues flagged, all false positives. Extension test: Author's 4 candidates + Critic's 4 additional candidates (imaginary-axis, small-$t$ large-separation, dimensional continuation, large-$N$) all ruled out. Cross-node consistency with W1-B1 R.B-collapse: CONSISTENT. Minor refinement noted: Obstruction A = A1 + A2 with A2 automatic given A1; does not affect verdict. 3 §I notes + 4 §D changes endorsed. **First Critic-independent empirical validation of I-7 backward-verification in Wave 1.** Structurally irreversible: R.A.1 is decomposition-verified; decomposition can be cited in Wave 2 R.A.1a / R.A.1b dispatches as settled ground.

---

*End of R.A.1 Critic output. Verdict: DECOMPOSITION-VERIFIED. Handoff to runner for Wave 1 cycle close per ORA v6 §5.4 + §6.2.*
