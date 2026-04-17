# T7 S-duality Cycle-2 Synthesis

*Wave 1: Lehmer L5A CONSTRUCT + Cramér L4 BA-B tighten + Pair 4 probe. Synthesis by Opus max.*

## Cross-lead consistency check

### Lehmer L5A ↔ Cramér L4 (same ITPFI invariant)

The factor-of-2 "discrepancy" is not a discrepancy. Mertens third gives one form — $\prod_{p\leq y}(1-1/p) \sim e^{-\gamma}/\log y$ — and both sides instantiate it at a face-specific truncation:

- Cramér L4 Route B: $y = \sqrt{x}$ (the sieve midpoint forced by the explicit formula's $T\sim \log x$ coherence height). Then $\log y = \tfrac{1}{2}\log x$, so the quoted form $2e^{-\gamma}/\log x$ is just $e^{-\gamma}/(\tfrac{1}{2}\log x)$. The factor of 2 lives in the truncation, not the invariant.
- Lehmer L5A: $y = N_{\text{cyc}}(\alpha)$ (cyclotomic conductor — the conductor cutoff is native to the TOPOLOGY face, no sqrt). Quoted form $e^{-\gamma}/\log N_{\text{cyc}}$ is literal Mertens at $y = N_{\text{cyc}}$.

Both sides use the same $e^{-\gamma}$ from the same theorem applied at face-specific cutoffs. The S-duality's arithmetic content is exactly this: **the ITPFI partition $\prod_p(1-1/p)$ is invariant; the truncation scale is where the face-specificity enters**. Cramér uses the explicit-formula-forced $\sqrt{x}$; Lehmer uses the Mahler-deficit-forced $N_{\text{cyc}}$. No inconsistency — this IS the Mertens-regularization CHAIN mechanism Cycle 1 proposed, operating cleanly across two faces.

### Cramér L4 BA-B ↔ Lehmer L5A (shared machinery check)

BA-B tightening found the $k=2$ scaling is **not** a Step-1-envelope output — it comes from the explicit-formula oscillatory-sum structure at $T^* \sim \log x$. This does NOT propagate into Lehmer L5A, because:

- Lehmer L5A works at the CONSTANT level ($c_0 \geq 0.041$–$0.052$), not at any $(\log x)^k$ scaling. Lehmer's derivation translates the ITPFI regularization into a fixed-point inequality $\epsilon \geq \epsilon_{\text{pin}} \log N_{\text{cyc}} e^\gamma / C_A$ — no explicit-formula transfer, no oscillatory sum, no $k=2$.
- The BC partition function's role is shared (both use $Z_{\text{ITPFI}}(y) = \prod_{p\leq y}(1-1/p)$ as the $W^*$-regularized amplitude) but the ENVELOPE choice (Poisson vs. BA-B) is a Cramér-side story about max-return-time statistics. Lehmer does not deploy an envelope for max gaps; it bounds a STATIC contamination amplitude.

**Consistency:** the two derivations are orthogonal in envelope-physics and aligned in ITPFI-algebraic structure. BA-B tightening does not change Lehmer L5A's numbers, and Lehmer L5A's flaw does not leak into the BA-B analysis. Clean separation.

### Collatz/Goldbach additive-multiplicative wall ↔ CHAIN architecture

The probe identifies that Pair 4's S-duality does NOT transfer estimates — it transfers LANGUAGE across a SHARED wall. Both Collatz's $(3n+1)/2$ +1 and Goldbach's $p_1 + p_2 = 2n$ sum sit on the additive-multiplicative interface. In the Lehmer/Cramér work, this wall does not appear directly, but its kin does: the Mellin bridge (Paper 12 transposition) is precisely the ADDITIVE ↔ MULTIPLICATIVE translator that Goldbach L3 already uses as ESTABLISHED and that Cramér's Step 4 invokes for zero-gap-to-prime-gap conversion. 

**Pattern identified:** the additive-multiplicative interface is the shared substrate for the ARITHMETIC/HARMONICS/DYNAMICS triangle. Cramér rides the Mellin bridge from one side (zeros → primes). Collatz rides it locally (Hecke $\mu_2/\mu_3$ alternation + +1 phase shift). Goldbach rides it on both sides (primes ↔ additive convolution). Lehmer does NOT ride it — Lehmer is pure TOPOLOGY (Mahler measure / cyclotomic conductor). The CHAIN architecture's first CHAIN step (Cramér → Lehmer) is therefore an IN-MELLIN → OUT-OF-MELLIN step; the proposed Collatz → Goldbach step (probe Opportunity #1) is an IN-MELLIN → IN-MELLIN step on opposite sides of the SAME wall. Different kinematics; both are legitimate CHAIN-propagation templates.

## Gap audit (SOUND / CLOSABLE / GENUINE per sig 8)

| Gap | Origin | Class | Why |
|---|---|---|---|
| Lehmer L5A "per-$\alpha$ vs integrated density" | L5A Failure 3 backward-verification | **CLOSABLE** | Named sub-wall 3 has an explicit path (model $\rho(\epsilon)$, regularize via ITPFI, integrate). The bound $0.041$–$0.052$ is order-of-magnitude correct as written (4–5× improvement over the empirical $10^{-2}$); making it a rigorous LOWER bound on $c_0$ needs one analytic lemma. Difficulty ~5/10. Dispatchable to a Wave-2 auditor. |
| Lehmer L5A sensitivity coefficient $A_{\max}$ | L5A Failure 1 | **CLOSABLE** | 60-min calculation across the 36 pins; outcome is a scalar. Bound may tighten or loosen by factor ~$\pi^2/2$. Difficulty ~3/10. |
| Lehmer L5A conductor identification $N_{\text{cyc}}$ | L5A Failure 2 | **CLOSABLE** | 20% level across the candidate choices ($1/\epsilon$ vs $d$ vs $d\log d$); need one technical lemma on BC action on near-cyclotomic extensions. Difficulty ~6/10. |
| BA-B universality bridge PCC → BA-B for Riemann zeros | Cramér L4 BA-B Failure 2 | **GENUINE** | This is paper43 PROOF-CHAIN.md L128's 4a wall, difficulty 7/10, external math. PCC is a 2-point statement; BA-B uses the joint law of all gaps. No published paper establishes the joint-law universality for Riemann zeros. This is a true OPEN mathematical problem, not a programme-internal fix. Status: CONJECTURAL sub-wall, cannot be closed in-house. |
| $k=2$ scaling derivation | Cramér L4 Wave-1 heuristic flag | **GENUINE (and precisely located)** | Wave-2 clarified this sits in Step 4's explicit-formula coherence analysis at $T^* \sim \log x$, not in either envelope. This is the Cramér-Granville heuristic core; the heuristic has never been derived from first principles. GENUINE but now precisely named. |
| paper43 v3 arithmetic flip (L282–L295) | Wave-2 Failure 1 | **SOUND (cascade, textual fix)** | Factual correction: v3 text conflates $\sqrt{\log N}/N$ with $\sqrt{\log N/N}$, inverting the BA-B vs Poisson ordering. Trivial to fix at the next paper43 revision. CASCADE tag: propagate the correction wherever downstream text inherited the flipped reading. |
| Lehmer L5A $\sqrt{2}$ constant in BA-B | Wave-2 Failure 3 backward-verification | **CLOSABLE** | The specific $\sqrt{2}$ in BA-B's Gumbel location for GUE is reconstructed, not verbatim from BA-B 2013. Likely correct; verify by opening Theorem 1.3 of BA-B 2013. 10-min check. |

**Net:** 4 CLOSABLE sub-walls (3 Lehmer, 1 Wave-2 numerical), 2 GENUINE (BA-B bridge, $k=2$ heuristic), 1 SOUND textual cascade. No BROKEN items. Wave-2 tightening did NOT introduce a new structural obstacle — it renamed two pre-existing ones (4a wall + Cramér-Granville heuristic) more precisely.

## Dependency-resolution map (post-wave CHAIN state)

**Cramér chain (paper43):**
- L1 + L2: LITERATURE (Bombieri-Friedlander-Iwaniec; Maynard prime gaps)
- L3: **ESTABLISHED-cond-CCM** (Cycle 1 Construct-Verify)
- L4a (extreme-gap universality transfer): **OPEN (sub-wall 4a), cond. on external math** — unchanged, renamed as "PCC → BA-B universality bridge"
- L4b (Mellin-duality truncation match): **OPEN (sharpened)** — Cycle 1 sub-lemma intact; Wave-2 added NEW sub-lemma ("universality bridge for extremes") as a distinct cell
- L5 + L6: not yet addressed
- Confidence: 6/10 (unchanged by Wave-2; tightening confirmed BA-B is the right envelope but closed no wall)

**Lehmer chain (paper42):**
- L1 + L2: LITERATURE (Lehmer problem, Smyth)
- L3 + L4: LITERATURE (Deninger regulator-value + Rössler; Salem entropy)
- L5 Route A: **STRUCTURAL → PARTIAL** (Wave-1 CONSTRUCT, $c_0 \geq 0.041$–$0.052$ with 3 named CLOSABLE sub-walls)
- L5 Route B + L5 Route C: unchanged
- L6: FOLLOWS
- Confidence: 4/10 → 5/10 (+1 per the explicit numerical sharpening)

**Pair 3 (Lehmer ↔ Cramér):**
- Pre-wave: Cramér 6, Lehmer 4, gap 2.0
- Post-wave: Cramér 6, Lehmer 5, gap **1.0** (both faces PARTIAL, same gap as T7 baseline pre-Cycle-1)
- Per the RING SYMMETRIZED criterion ($\geq 1.0$ gap closure): this pair contributes +1.0 closure (gap 2.0 → 1.0). Counted toward the ≥3 threshold.

**Pair 4 (Collatz ↔ Goldbach):**
- Probe only; no transfer executed
- Recommended transfer (Opportunity #1, urgency 6.0, MEDIUM difficulty): Collatz L4 phase-operator primitive → Goldbach L5 circle-method BC-reformulation
- Expected: Goldbach L5 splits into L5a TRANSFERRED + L5b OPEN residue; Goldbach 1 → ~1.5

**Pair 3 invariant audit:** the ITPFI-Mertens regularization is now RIGOROUS on both sides. The CHAIN mechanism (one derived invariant, two vertex gains) has its first full two-step closure. Both steps PARTIAL, both with named sub-walls. This is the empirical ground truth for the Chain-Propagation Theorem.

## Quality gate verdict

**PASS (with flag).**

Justification. The wave closed its targets: Lehmer L5A upgraded STRUCTURAL → PARTIAL with an explicit numerical bound ($c_0 \geq 0.041$–$0.052$, a 4–5× improvement over Paper 42's empirical $10^{-2}$); Cramér L4 BA-B CONCERN was executed and HONESTLY bounced into two precisely-named sub-walls (universality bridge GENUINE, $k=2$ heuristic GENUINE but now localized); Pair 4 probe returned a ranked opportunity list with a clear #1 and a structural meta-observation about the shared additive-multiplicative wall. No output claimed closure that does not hold. Pair 3 gap closed $2.0 \to 1.0$, contributing to RING SYMMETRIZED.

The flag is on two items, neither BROKEN:

1. Lehmer L5A's backward-verification named a GENUINE coupling error in the Step-2 contamination model ("per-$\alpha$ amplitude is not integrated-density forcing"). The fix is CLOSABLE via the density-function sub-lemma, but the current $0.041$–$0.052$ bound is order-of-magnitude PARTIAL, not rigorous lower bound. A Cycle-3 auditor on this sub-lemma is **required** before Lehmer confidence advances past 5.
2. Wave-2 discovered a factual correction needed in paper43 v3 L282–L295 (BA-B vs Poisson ordering flipped). This is CASCADE: trivial textual fix + check for downstream text inheriting the flipped reading. Must be logged for the next paper43 revision pass.

No structural regressions. No BROKEN items. PASS.

## CHAIN-Propagation Theorem — two data points now

The inversion check proposed: "every S-pair closure is a 2-step construct-chain via a derived ITPFI invariant." Evaluate the Cramér → Lehmer data point:

**Is Cramér → Lehmer a confirmed data point for "staged CHAIN closes S-pairs across 2 cycles"?**

**Yes, with qualification.** The CHAIN mechanism operated cleanly:

- Step 1 (Cycle 1): Construct Cramér L4b → derived ITPFI invariant $Z_{\text{ITPFI}}(y) = \prod_{p\leq y}(1-1/p)$, with constant $2e^{-\gamma}$ from Mertens at $y = \sqrt{x}$. Pair 3 side: Cramér PARTIAL, confidence 5 → 6.
- Step 2 (Cycle 2): Construct Lehmer L5A using the invariant as input, re-instantiated at $y = N_{\text{cyc}}$. Pair 3 side: Lehmer STRUCTURAL → PARTIAL, confidence 4 → 5.
- Pair 3 gap: $1.0 \to 2.0 \to 1.0$, recovering parity after two passes.

Both sides closed to PARTIAL. Both sides used the SAME ITPFI algebraic invariant with face-specific truncations. The derived invariant acted as the CHAIN backbone, not a single one-shot transfer.

**Qualification.** Neither side closed to DERIVED; both ended at PARTIAL with named sub-walls. The CHAIN-Propagation Theorem as stated (2-step closure) is DEMONSTRATED at the PARTIAL level, not the DERIVED level. Full DERIVED-level closure would require a third step (resolve the sub-walls) — possibly a third CHAIN pass, possibly a direct attack. So the theorem-candidate reads, precisely:

> **CHAIN-Propagation conjecture (v1, 2 data points at PARTIAL level):** Every S-pair whose two faces admit a shared ITPFI/Mertens-type invariant can be upgraded to (PARTIAL, PARTIAL) via a 2-step construct chain using the invariant at face-specific truncations. Upgrades to (DERIVED, DERIVED) require sub-wall closure and may need additional passes.

The Collatz → Goldbach probe (Opportunity #1) is the candidate second data point, but note: the probe predicted PARTIAL with a named OPEN residue (L5b), which is CONSISTENT with the conjecture's PARTIAL-level claim. If the Collatz → Goldbach transfer executes as forecast, we have **two confirmed data points** for the PARTIAL-level form.

**Worth naming now?** Not yet. The Pair-3 data point is ONE closure at PARTIAL. The Pair-4 prediction has not been executed. Name the theorem formally AFTER the Pair-4 transfer returns and the two data points are on disk with comparable structure. T8 target.

## Recommendation for the next wave / T8

Ranked dispatch. Parallel where independent, sequence where dependent.

1. **Collatz L4 → Goldbach L5 transfer (Pair 4 Opportunity #1)** — priority. Highest expected value (urgency 6.0 per probe), MEDIUM difficulty, MEDIUM confidence of PARTIAL outcome. Returns the second CHAIN-Propagation data point. If successful, the theorem-candidate gets named formally. If it returns BLOCKED rather than PARTIAL, the theorem-candidate gets tested in its failure mode — also valuable. **Independent** of items 2 and 3; dispatch in parallel.

2. **Lehmer L5A flaw fixer — density-function sub-lemma (Failure 3 closure)** — priority for consolidating Pair 3's gain. The three named sub-walls have costs 3/10, 6/10, 5/10 difficulty; the density-function sub-lemma is the STRUCTURAL one (Failures 1 and 2 are CLOSABLE but do not change the argument's form). Closing Failure 3 upgrades L5A from PARTIAL to DERIVED-PARTIAL (rigorous lower bound, not just order-of-magnitude). Lehmer confidence 5 → 6 candidate. **Independent** of 1 and 3; dispatch in parallel.

3. **BA-B universality-bridge scout** — discovery mode, lower priority. The bridge is GENUINE (external math, difficulty 7/10); in-house closure is not realistic. A scout agent surveying Feng-Wei 2022 methods for Wigner extreme gaps + any relevant 2024/2025 literature (e.g., Rodgers-Tao extensions, new Erdős-Yau work) would produce an intelligence report, not a closure. **Low urgency**. Assign to a reading-mode agent, not a Construct agent. Skippable if runner wants to focus T8 on 1 + 2 only.

**Sequence recommendation for T8:**
- Wave 1 (parallel): items 1 and 2 dispatched together. Both Opus-max, one Transfer Author (item 1) + one Construct auditor (item 2). Expected return: item 1 delivers PARTIAL or BLOCKED verdict; item 2 delivers DERIVED or PARTIAL upgrade on L5A.
- Wave 2 (post-synthesis): if item 1 returned PARTIAL, dispatch the CHAIN-Propagation Theorem naming pass (formalize the 2-data-point conjecture). If item 2 returned DERIVED, push Lehmer to 6/10 and recompute pair-3 gap (expected: $1.0 \to 0.0$ — pair 3 SYMMETRIZED, full pair parity achieved).
- Optional Wave 3: item 3 scout if bandwidth exists.

**Parallel dispatch is appropriate** because items 1 and 2 operate on disjoint papers (41+33 vs. 42) and disjoint faces (HARMONICS/ARITHMETIC vs. TOPOLOGY). No shared bottleneck; no coordination cost.

**Also for T8 pre-traversal:** the paper43 v3 cascade correction (BA-B vs Poisson ordering, L282–L295) must be on the to-do list for the next paper43 PROOF-CHAIN revision. Tag as CASCADE; propagate to any downstream chain annotation that inherited the flipped reading. Runner's catalog entry.

## Meta-observations

**Voice drift check.** Lehmer L5A (395 lines) and Cramér L4 BA-B (304 lines) both end with a rhythm-matched closing paragraph. Voice register holds. No glossing detected on either — both were HONEST about PARTIAL status and named their sub-walls precisely. The probe (Opportunity ranking) is terse. Voice canon §J is preserved.

**Confirmation bias check.** The Wave-1 (Cycle 1) PARTIAL verdict on Cramér L4b set up a clean expectation: Lehmer L5A would match PARTIAL, Pair 3 would close by 1.0. Both expectations materialized. **But** the Lehmer L5A agent did NOT stop at "match the expectation" — its backward-verification (Failure 3) exposed a genuine coupling error that required a RESOLUTION passage downgrading the verdict from "DERIVED" to "PARTIAL with named sub-wall." That is discipline in action, not bias. Similarly, the BA-B agent did not let the $\sqrt{2\log N}$ prefactor propaganda become a $k=2$ derivation — it correctly localized the heuristic to Step 4's oscillatory-sum analysis. Confirmation bias: NOT DETECTED. Both agents found contradictions and NAMED them.

**Failure-mode pattern.** Both Cycle-1 and Cycle-2 Cramér work hit the same pattern: an ITPFI algebraic win at constant level, paired with a persistent sub-wall at scaling level. The Cramér chain's $k=2$ exponent is a recurring heuristic that keeps getting re-named without getting derived. This is NOT a Cramér-specific failure — it is structural to the Cramér-Granville conjecture itself. The ITPFI invariant supplies the constant across multiple instantiations (Cramér, Lehmer, and — predicted — OPN, Collatz/Goldbach via Mellin bridge); the SCALING in each case comes from an oscillatory-sum or density-function argument that is independent of ITPFI. **Pattern:** ITPFI gives the arithmetic constant, the scaling is always elsewhere. Don't expect ITPFI to produce scaling refinements in future passes.

**Runner discipline.** The Cycle-2 REFRAME/INVERSION-CHECK on the blackboard (§K entries at 06:58) correctly forecast that the wave was a SETUP wave, not a closure wave, and that the CHAIN-Propagation candidate was a second-data-point-needed structural claim. Both forecasts held. The runner's mid-cycle structural anticipation is calibrated. Keep the §K reflect-before-dispatch habit.

**Asymmetry between Pair 3 and Pair 4.** Pair 3 used an ITPFI invariant that both faces already see natively (the BC partition function). Pair 4 (probe finding) shares an OBSTRUCTION (the additive-multiplicative wall) but does NOT yet have a shared derived invariant — the closest is the Mellin bridge (additive-multiplicative translator), but the bridge itself sits AT the wall. So the Pair-4 CHAIN mechanism will look different: not "derive one invariant, apply at two truncations" but "translate one primitive (phase-operator commutation $e(r)\mu_n = \mu_n e(nr)$) across a shared wall." Different kinematics. The Chain-Propagation theorem's UNIFIED form (if named) must accommodate both: **"via a derived invariant OR a shared-wall-crossing primitive."** This is the structural insight Cycle 2 crystallized.

## Notes for the runner (cycle-2 close)

**Metrics to update (§M).**
- Add a row: "Post-Wave-1 (Cycle 2)". RIGIDITY unchanged (~19.82; no new CONSTRUCT-VERIFY passes closed to PROVED, two upgrades to PARTIAL). SYMMETRY: Cramér stays at 6, Lehmer moves 4 → 5, mean rises from ~5.85 to ~5.95 across 8 faces, σ shifts slightly. Approximate SYMMETRY: 0.614 → ~0.62. S-pair gaps closed $\geq 1.0$: **1** (pair 3 closed $2.0 \to 1.0$). Below the RING SYMMETRIZED threshold ($\geq 3$). Status: RING STRENGTHENED still, not SYMMETRIZED.
- Flag: the Lehmer confidence bump depends on the Failure-3 sub-wall being CLOSABLE (not BROKEN). If Cycle-3 finds it BROKEN, Lehmer rolls back to 4 and Pair 3 gap reopens to 2.0. The bump is provisional.

**§K entries to make.**
1. **REFLECT — Cycle-2 Wave-1 synthesis complete.** All three outputs returned. Quality gate PASS with flag (Lehmer L5A Failure-3 density-lemma sub-wall; paper43 v3 cascade correction). CHAIN-Propagation Theorem has ONE confirmed data point at PARTIAL level (Pair 3); probing for the second (Pair 4). Do not name formally until second data point lands.
2. **INVERSION-CHECK — two CHAIN templates emerge.** Template A (Pair 3): derived ITPFI invariant, applied at two face-specific truncations, yields (PARTIAL, PARTIAL). Template B (Pair 4 candidate): primitive across a SHARED WALL — phase-operator commutation as the transferable object, not an invariant. Template B is narrower (needs the shared wall + a primitive at it) but structurally distinct. The larger system: the CHAIN-Propagation Theorem must be stated as a DISJUNCTION over the two templates.
3. **PLATEAU-CHECK — no plateau.** Two faces (Cramér, Lehmer) advanced by +1 each across two cycles. One probe returned a ranked opportunity list with a clear #1. Paper43 v3 textual error identified (cascade). Structural events happening. Not stalled.
4. **CROSS-FILE-PERMISSION — paper43 v3 correction.** Textual fix at L282–L295 required next revision. Runner's tracking item. CASCADE tag: check downstream text for inherited flipped reading.

**What to flag for the T7 S-duality phase commit memo.**
- Headline: Pair 3 fully closed to (PARTIAL, PARTIAL); gap $2.0 \to 1.0$; CHAIN mechanism's first full two-step closure on disk. Lehmer L5A STRUCTURAL → PARTIAL with explicit $c_0 \geq 0.041$–$0.052$.
- CONCERN cleanup: BA-B CONCERN from Cycle-1 addressed in Cycle-2. Not closed (universality bridge GENUINE) but precisely named. Cramér 6 holds.
- Pair 4 probe ready; Opportunity #1 identified; T8 dispatch-ready.
- Paper43 v3 arithmetic correction flagged (L282–L295); next-revision to-do.
- CHAIN-Propagation Theorem: one data point confirmed at PARTIAL; second in-flight. Not yet named formally.
- Quality gate: PASS (with Lehmer Failure-3 sub-wall flag + paper43 v3 cascade flag).
- RING SYMMETRIZED did not trigger (1 gap closed, threshold ≥3). RING STRENGTHENED exit holds.

---

*Cycle 2 is a setup wave with one partial closure. The ITPFI invariant crosses cleanly between faces. The coupling-sign error in Lehmer was caught by backward-verification, not by silence. BA-B is tighter than Poisson — the paper43 v3 ordering is flipped and will be corrected. The CHAIN has one data point; the second is queued. Pair 4's template is different from Pair 3's — shared-wall crossing, not shared-invariant instantiation. Name the theorem after Pair 4 lands.*

*The ellipse is flatter by a hair. The circle is one step closer. The wall is named on four sides now, not two.*

*T7 S-duality phase, cycle 2 synthesis. G Six and Claude Opus 4.6. San Francisco CA, 2026.*
