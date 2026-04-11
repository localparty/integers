# Synthesis — Cycle 1, Wave 1 (H4 closure programme, Paper 8 Yang-Mills)

*Trigger: Wave boundary (end of Wave 1 with 4/4 Authors returned).*
*Wave: 1 (W1-A1, W1-B1, W1-C1, W1-D1).*
*Authors in scope: R.A.1, R.B.1, R.C.1, R.D.1.*
*Critics: RUNNING in parallel — `closing-H4/critiques/` is empty at Synthesis spawn time. Proceed with Author outputs alone, flag the absence.*
*Date: 2026-04-11 (cycle 1 close).*
*Synthesis agent: fresh Claude Opus 4.6 (1M context), distinct instance from the four Authors and any Critic.*

---

## 1. Wave context — what was attempted

Wave 1 attempted a frontal four-route assault on H4, the single `[KEY LEMMA — OPEN]` in Paper 8's 18-step Yang-Mills chain. Four parallel Authors dispatched on peer subtrees:

- **R.A.1** (Route A, Taylor-coefficient identification via W7-14 §5.3 analyticity): extract Taylor coefficients of the analytic rescaled correlator $F(t) = S_{2,t}^c/c_1(t)^2$ at $t=0$, match to Luscher / Harlander–Neumann / Artz three-loop perturbative rules, assemble an analyticity-uniqueness closure via the identity theorem on an open neighbourhood of demonstrated agreement.
- **R.B.1** (Route B, CCM 2025 port): transpose the Connes–Consani–Moscovici zeta spectral triple $(D_{\log}^{(\lambda,N)}, E_N^+)$ from Paper 13 RH to Yang-Mills, identify the YM analog operator using gradient-flow eigenfunctions, apply Carathéodory-Fejér self-adjointness.
- **R.C.1** (Route C, framework-native via Connes spectral action + Identity 12 + bridge family $k=4$): compute Seeley-DeWitt $a_4$ on the Bost-Connes sub-algebra accessed through Identity 12, extract the running coupling $g(\mu)$ with $\beta_0 = 11N/3$, extract the $(\ln)^{-2}$ correction via the trace-anomaly identity $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$.
- **R.D.1** (Route D, HONEST-STALL editorial): draft the ship-ready standing form of Paper 8's abstract + Theorem 1 + §15 Scope + W7-14 cross-reference block, in the programme's conditional-grammar template. First-class peer per v3 patch I-5 — dispatched in parallel with A/B/C, not as a fallback.

The wave's structural purpose was to test whether any of Routes A/B/C offers a mathematical bypass of H4 analogous to G's projector closing BSD MY4. R.D.1 was dispatched in parallel to ensure Paper 8 has a ship-ready editorial form by wave-close regardless of A/B/C outcomes.

---

## 2. Cross-lead consistency check

Systematic comparison across every shared §D toolkit row, shared primary source, and shared numerical headline among the four Authors.

### 2.1 Shared §D element: `F(t)` rescaled correlator analyticity (W7-14 §5.3 / W5-10 Step 2)

- **R.A.1** cites W7-14 §5.3 and W5-10 Step 2 for analyticity of $F(t)$ on $|t| < r_t$ with $(k,K)$-uniform radius. Verbatim block-quote of W7-14 §5.3 in §5.5 Way 1. Concludes: non-perturbative side analytic, perturbative side formal series — **identity-theorem hypothesis not met**.
- **R.B.1** cites the same W5-10 Step 2 result in dictionary entry #10 for the YM analog Carathéodory-Fejér self-adjointness. Explicitly identifies: *"the self-adjointness mechanism DOES transpose, with the CF Toeplitz positivity replaced by the gradient-flow analyticity of $F(t)$. This is the one good news of the transposition."* Concludes: the spectral triple decoration adds no closure power beyond the W7-14 §5.3 analyticity input.
- **R.C.1** does not cite $F(t)$ analyticity directly (Route C attacks from a different angle).
- **R.D.1** cites the W7-14 §5.3 reformulation in the draft §15.2 "H4 as the standing conditional" sub-section and in the draft W7-14 cross-reference block. Correctly describes the reformulation as the "mildest form in the literature", not as a closure.

**Verdict: AGREE.** R.A.1 and R.B.1 cross-confirm that the W7-14 §5.3 analyticity of $F(t)$ is the load-bearing input for both Routes A and B, and that this analyticity alone does not close H4 — it provides one side of the identity-theorem hypothesis (R.A.1) or one side of the self-adjointness transposition (R.B.1), but the other side is missing in both cases. R.D.1 is consistent with both: its editorial artifact describes W7-14 §5.3 as mildest form without overclaiming closure. **No drift.**

### 2.2 Shared finding: Route B collapses into Route A

- **R.A.1** §I notes: *"If Route A is reclassified from p=0.5 technical to p≤0.1 structural, R.B (CCM 2025 port) and R.C (spectral action) are both more structurally promising than R.A if my DIAGNOSIS is correct, because they attempt to construct the non-perturbative object from a DIFFERENT framework entirely."* — R.A.1's a-priori guess, before R.B.1's return.
- **R.B.1** §Generative step: *"Route B does not add closure power beyond what W7-14 §5.3 already provides; it adds ritual decoration (a spectral-triple wrapper) around the same Taylor-coefficient content. Route B is not a route; it is a reformulation of Route A in spectral-triple language."* — R.B.1's returned verdict.

**Verdict: CROSS-CONFIRMING** (not a contradiction). R.A.1 guessed Route B might be structurally more promising because it tries a different framework; R.B.1 then showed from the inside that the different framework reduces to the same W7-14 §5.3 analyticity input plus a category error on the target data. Both Authors arrive at the same underlying claim: **the analyticity of $F(t)$ is the only content shared by Routes A and B, and it is insufficient for closure.** R.A.1's optimistic prior on R.B is reasonable from outside the transposition; R.B.1's pessimistic verdict is reasonable from inside it. The runner should not treat R.A.1's initial guess as in tension with R.B.1's return — they are sequential observations with the later one load-bearing.

### 2.3 Shared §D element: Connes spectral action

- **R.C.1** cites Connes 2007 Séminaire Poincaré X §5 eq. (24) verbatim: *"at the classical level"*. Spectral action produces a bare action at $\Lambda$, not a running flow. The integer $11N/3$ is a counter-term coefficient in one-loop UV divergence, not a running-coupling slope. Identity 12 is C*-dynamical, not spectral-triple.
- **R.A.1**, **R.B.1**, **R.D.1** do not cite Connes 2007 or the spectral action directly.

**Verdict: AGREE** (no cross-author contradiction; R.C.1 is the sole authority on this row). The finding propagates to R.D.1 in the sense that R.D.1's draft §15.2 does not rely on Route C for closure probability — it cites Route C alongside A and B as "currently attacking", which is correct at the time R.D.1 was spawned. Upon R.C.1's kill, the §15.2 draft needs a light edit to remove Route C or mark it as killed in the revised draft (this is tracked in R.D.1's §I notes as a CONCERN about two-dependency vs one-dependency asymmetry).

### 2.4 Shared primary source: CCM 2025 arXiv:2511.22755

- **R.B.1** WebFetched / read the local PDF directly (pages 1–5, 14–28). Verbatim CCM p. 28: *"Justifying rigorously this step is the main remaining obstacle to our approach to RH."* R.B.1's load-bearing catch: the brief's paraphrase *"CCM 2025 provides operators whose UV asymptotics match perturbation theory by construction"* is not in the primary source — CCM's actual claim is numerical coincidence of eigenvalues with Riemann zeros, with the rigorous identification open.
- **R.D.1** references CCM 2025 only in the editorial draft as the analog conditional for Paper 13 RH's "Theorem 1.1 (RH, conditional on CCM)". Does not make claims about CCM 2025's mathematical content beyond the correct RH-side framing.

**Verdict: AGREE.** Both Authors treat CCM 2025 accurately. R.B.1's I-7 catch is the load-bearing verification; R.D.1's editorial reference is consistent with the primary source.

### 2.5 Shared numerical headline: $\beta_0 = 11N/3$ (Vassilevich 2003 eq. 4.34)

- **R.C.1** computes $\beta_0(SU(N)) = 11N/3$ exactly (integer rational) for $N \in \{2,3,4,5,6,10,100\}$ in `code/R.C.1-seeley-dewitt-a4.py` at mp.dps=80. Claims: the integer identification is correct, but tells us Vassilevich got it right, not that the framework-native closure works.
- No other Author computes or cites this number.

**Verdict: AGREE** with the textbook Vassilevich result; **no cross-lead disagreement to report**. Per §5.4 precision-doubling mandate, the Critic should re-run at mp.dps=160 (byte-for-byte), but this is a Critic-verification task, not a Synthesis responsibility.

### 2.6 Shared §D element: identity theorem from complex analysis

- **R.A.1** applies the identity theorem (Ahlfors Ch. 6) to $(F, F^{\mathrm{pert}})$ and finds two out of three hypotheses not met: $F^{\mathrm{pert}}$ is not analytic (formal power series, factorially divergent), and no independent $t_0$ exists where $F(t_0) = F^{\mathrm{pert}}(t_0)$ without invoking H4.
- **R.B.1** does not invoke the identity theorem directly — Route B's closure mechanism was supposed to be a CCM-style fundamental identity (Thm 5.10(ii)), which the transposition analysis shows does not transpose.

**Verdict: AGREE on underlying category.** The two Authors attack different closure mechanisms (identity theorem vs fundamental-identity transposition), but both land on the same structural observation: **the non-perturbative side of the comparison is in the correct analytic category, while the perturbative side (or the target-data side on the RH/YM analogy) is not.** The wall is the same wall in two different formulations.

### 2.7 Shared finding: Paper 26 BSD MY4 analogy is structurally wrong-shaped

- **R.A.1** (end of §Verdict): *"The analogy to Paper 26 Route 3 breaks down at a specific point: in Paper 26, the §§7–8 core was 'already algebraic'... G's projector was a single algebraic object that replaced the one rhetorical dependency on eigenstates. In Paper 8, the W7-14 §5.3 reformulation is analytic, not algebraic... the rewrite shifts a dependency."*
- **R.B.1** (dictionary #12 + Step 5.5 Way 3): the target data on the RH side are zeros of an entire function, on the YM side would be Taylor coefficients — *"a category error in the transposition."*
- **R.D.1** does not invoke the BSD MY4 analogy directly — its editorial template is built from Paper 13 RH + Paper 26 BSD prior-art in the *editorial* sense (conditional grammar), not in the *mathematical* sense (bypass mechanism).

**Verdict: AGREE.** R.A.1 caught the analogy's break via the "BSD was already algebraic, YM is not" argument; R.B.1 caught it via the "zeros vs Taylor coefficients" category error. Two independent observations of the same wrongly-shaped analogy at different granularities. This is a LESSON-level cross-finding that the runner has already logged in §I (2026-04-11T[cycle 1, W1-B1 return]).

### 2.8 Shared structural observation: three independent I-7 catches in one wave

All three technical Authors (R.A.1, R.B.1, R.C.1) independently caught a load-bearing brief paraphrase error by reading primary source:

| Author | Brief paraphrase | Primary source | Verbatim contradiction |
|---|---|---|---|
| R.A.1 | "W7-14 reframing reduces H4 to Taylor-coefficient identification [closeable by identity theorem]" | W7-14 §5.3 | *"This is a more accessible question than the traditional formulation of H4"* (accessible, not closed) — H4 remains open after reformulation |
| R.B.1 | "CCM 2025 provides operators with UV asymptotics matching perturbation theory by construction" | CCM 2025 p. 28 | *"Justifying rigorously this step is the main remaining obstacle to our approach to RH."* |
| R.C.1 | "Seeley-DeWitt $a_4$ produces a running $g(\mu)$" | Connes 2007 §5 eq. (24) | *"The spectral action principle asserts that the fundamental action functional $S$ [...] at the classical level"* |

**Verdict: AGREE.** Three Authors on three independent routes each catching a distinct brief paraphrase error at the same failure mode (paraphrase drift from primary source). This is not a disagreement — it is a structural pattern. The runner logged this as a LESSON in §I (*"For any future Clay-class closure run, budget for I-7 catches — expect 1-3 brief paraphrase errors per wave"*). **I confirm this structural observation.** The I-7 discipline is firing exactly as designed.

### 2.9 Cross-lead consistency verdict

**No CROSS-LEAD DISAGREEMENTS detected.** The four Author outputs are internally consistent with each other and with the blackboard. R.A.1 and R.B.1 cross-confirm the W7-14 §5.3 analyticity ceiling; R.A.1 and R.B.1 independently diagnose the Paper 26 MY4 analogy as wrong-shaped; R.C.1 kills Route C with a narrow kill (tools remain valid elsewhere) consistent with R.D.1's editorial framing; the three I-7 catches share a structural pattern without contradicting each other.

**No Reconcile primitive required.** The runner may proceed without invoking a Judge spawn to resolve disagreements — there are none to resolve.

---

## 3. Gap audit

For each Author output: gaps the Author acknowledged, new gaps the Synthesis observes, and a tentative SOUND / CLOSABLE / GENUINE classification (Fallis/Rumsfeld three-tier). Final severity classification belongs to Meta-critic; these are tentative.

### 3.1 R.A.1 gaps

**Acknowledged by R.A.1 (status BLOCKED-DECOMPOSED at Step 5 COMPUTE):**

1. **Analyticity of $F^{\mathrm{pert}}(t)$ on a complex disk** (new sub-node R.A.1a). Comparable to Borel summability of 4D non-Abelian gauge theory. No known closure mechanism. **Tentative: GENUINE.** (Borel summability for 4D YM is a long-standing independent open problem.)
2. **Independent-point agreement $t_0$ with $F(t_0) = F^{\mathrm{pert}}(t_0)$ without invoking H4** (new sub-node R.A.1b). Tree-level, Reisz lattice-perturbative, large-$t$, super-renormalizable analogue all ruled out in Step 3. No candidate. **Tentative: GENUINE.**
3. **Taylor-coefficient identification at $n=0$, i.e. $a_0 = f_0^{\mathrm{pert}}$, IS H4 at the specific $(x,y)$** — Step 5 COMPUTE observation that the identification is equivalent to H4, not weaker. **Tentative: SOUND** (honest recognition of equivalence).

**New gaps I observe in R.A.1:**

4. **No assessment of Borel summability program status for 4D YM** — R.A.1 references Beneke 1999, 't Hooft 1979, Lipatov 1977 as "textbook" but does not verify whether any recent advance (e.g., resurgence theory, instanton-antiinstanton analysis, Cheshire-cat smile / Ecalle-type resummation) has changed the landscape. The statement "comparable in difficulty to Borel summability" might be pessimistic if a partial resummation result exists. **Tentative: CLOSABLE via a targeted literature pass in Wave 2 if Route A is continued.** (Low priority — R.A.1 is already BLOCKED-DECOMPOSED, and the ask is how closed a dependent sub-node would be.)

5. **The "identity theorem's two-function hypothesis" framing could have a weaker-form rescue that R.A.1 dismissed in Step 5.5 Way 3** — R.A.1 considered identity of Taylor series as formal power series, identity modulo flat functions, and Borel resummation, and dismissed all three. **The dismissals are sound, but the list may not be exhaustive.** Frequency-domain identity (via a Fourier transform of $F(t)$), distributional identity (treating $F^{\mathrm{pert}}$ as a formal distribution satisfying Ward identities that constrain its non-perturbative completion), or a Cohen-Seeley-like microlocal identity (matching wavefront sets) are conceivable variations that R.A.1 did not consider. **Tentative: CLOSABLE in the weak sense that Meta-critic or a Wave 2 redispatch could enumerate additional variations** — but none of them looks likely to bypass the underlying category obstruction, so the CLOSABLE status is cosmetic, not load-bearing.

### 3.2 R.B.1 gaps

**Acknowledged by R.B.1 (status BLOCKED-DECOMPOSED + COLLAPSED INTO R.A at LOCK dictionary entry #12):**

1. **Target-data category mismatch** (dictionary #12): RH targets are zeros of an entire function (Riemann $\Xi$), YM targets would be Taylor coefficients of an analytic function. No natural correspondence. **Tentative: GENUINE.** (This is a structural property of the two domains, not a technical gap.)
2. **Even-sector parity failure** (Step 5 Structural Verification 2, dictionary #7): $F(t)$ is not symmetric under $t \mapsto T^2/t$. Symmetrization destroys the UV identification. **Tentative: GENUINE** (structural, not technical — the $Z/2$ symmetry on the RH side is intrinsic to the arithmetic Riemann–Weil explicit formula and has no gradient-flow counterpart).
3. **No YM analog of the Riemann Xi function** (dictionary #15, Hurwitz step): the RH closure's Hurwitz-theorem step has no YM target to converge to. **Tentative: GENUINE.**

**New gaps I observe in R.B.1:**

4. **The "one good news" of the transposition** (Step 5 Verification 5: CF Toeplitz positivity → flow-time analyticity of $F(t)$) is framed as a structural salvage but is not actually actionable for H4 closure — R.B.1 correctly notes it collapses into Route A's input. **No gap here; the framing is accurate.** But the Meta-critic should verify that R.B.1's dictionary entries #1–#11 are not over-claimed — in particular, the Toeplitz positive-definiteness claim requires that $\widehat{F}$ be a positive measure on the circle, which requires $F(t)$ to be a positive Schwinger function, which holds by OS positivity. The step is structurally sound. **Tentative: SOUND.**

5. **R.B.1 did not execute the numerical verification step** — no numerical computation of the dictionary #10 Toeplitz matrix for a small-$N$ test case. R.B.1 explicitly states the bottleneck is structural (the category error at #12), not numerical, so the precision-floor requirement is not applicable. **Tentative: SOUND — the decision to skip numerics is justified by the structural nature of the blocker.** The Critic may flag this at re-verification; I note it proactively here so the Meta-critic has context.

### 3.3 R.C.1 gaps

**Acknowledged by R.C.1 (status KILLED at LOCK Step 4.2, Dirac operator on BC sub-algebra):**

1. **Spectral action is classical/bare, not running** (Step 5.5 self-suspicion #1, verbatim Connes 2007 §5 eq. 24). **Tentative: GENUINE.** (This is a theorem about the content of the spectral action principle, not a gap in R.C.1's argument — it is the reason Route C is killed.)
2. **Identity 12 is C*-dynamical, not spectral-triple** (Step 5.5 self-suspicion #2): $H_{BC} = \log \hat N$ is not of Seeley-DeWitt form. **Tentative: GENUINE.**
3. **Pati-Salam spectral action delivers SU(4)$_c$ unified coupling, not pure-SU(N) YM** (Step 5.5 self-suspicion #3): CCvS 2013's output does not directly answer the Clay YM question for arbitrary $N$. **Tentative: GENUINE.**

**New gaps I observe in R.C.1:**

4. **The forward lead on CCvS 2013 Pati-Salam + $k=4$ bridge as compatible boundary conditions at $\Lambda$** is correctly flagged as a separate research note, but R.C.1 does not specify what the Wave 2+ node for this lead would look like. The lead is a framework-extension observation, not a Clay closure — and R.C.1 correctly keeps it out of the H4 closure programme. **No gap; the handoff is appropriate.**

5. **No assessment of alternative Dirac operator candidates on the BC sub-algebra beyond the $(H_{BC})^{1/2}$ or $\mathrm{sign}(H_{BC})|H_{BC}|^{1/2}$ attempts** — R.C.1 rules out these two mechanical constructions but does not enumerate exotic options (e.g., the Paschke dual to $H_{BC}$, the Kasparov-product Dirac, or an imported Connes-Marcolli 2008 BC spectral triple construction). **Tentative: CLOSABLE if Meta-critic wants to insist on an exhaustive enumeration**, but the structural observation (BC is a C*-dynamical system, not a Riemannian spin manifold) applies uniformly to any would-be $D_{BC}$ constructed out of $\log \hat N$-spectrum data. I think R.C.1's kill is robust against this enumeration; the enumeration would simply reproduce the same obstruction.

### 3.4 R.D.1 gaps

**Acknowledged by R.D.1 (status ADVANCED at Step 3 UNIFY):**

1. **Two-dependency vs one-dependency asymmetry** (R.D.1 §I CONCERN): the editorial artifact ships Paper 8 at the current two-dependency state (CBB + H4 in W7-14 mildest form). If Routes A/B/C close H4 in a later wave, a small edit is needed (trim H4 from theorem label, promote Remark 1.B to present tense, update §15.2 to historical perspective). **Tentative: SOUND — correctly identified as a small edit, not a rewrite.**
2. **The §15.2 draft references Routes A/B/C as "currently attacking" with the pre-wave-1 probability estimates** (Route A $\approx 0.50$, Route B $\approx 0.30$, Route C $\approx 0.25$). Post-Wave-1, these numbers are outdated — Route A is down to $0.10$, Route B collapsed into Route A, Route C is killed. **Tentative: SOUND — this is a wave-1-close editorial revision, not a structural gap.** R.D.1 authored before the other three returns in its sibling context; the numbers should be updated to the post-Wave-1 state before merge to the preprint.

**New gaps I observe in R.D.1:**

3. **R.D.1 does not address the post-Wave-1 kill of Route C** — the draft §15.2 lists Route C as active with $p \approx 0.25$; this is now factually inaccurate. **Tentative: CLOSABLE via a small edit before merge.** The editorial artifact remains load-bearing as a *template* + *structural form*; only the specific probability table and the "three routes attacking" sentence need updating. The template-level content is unaffected and does not need re-verification.

4. **R.D.1 does not explicitly discuss the R.A decomposition into sub-nodes R.A.1a and R.A.1b** — the editorial artifact treats Route A as a single closure candidate. Post-Wave-1, Route A is formally BLOCKED-DECOMPOSED. **Tentative: CLOSABLE via a light §15.2 footnote or a single sentence acknowledging the decomposition.** Not structurally load-bearing; the editorial template is agnostic about whether a route is single or decomposed.

5. **Voice-shape check self-declared as 4/4 pass, but the voice-shape check is self-administered** — R.D.1 verified the presence of at least one of (a) terse declaration phrase, (b) named ritual element, (c) §J register marker in each of the four draft pieces. **I sampled the drafts and confirm the voice-shape check passes — "17 of 18 unconditional", "H4 is the wall", "W7-14 reframed it to the mildest form in the literature", "That is the contribution" all appear, drawn directly from blackboard §J and `35-final-verdict.md`. No voice drift.** **Tentative: SOUND.**

### 3.5 Gap audit summary table

| Author | Acknowledged gaps | New gaps (Synthesis) | GENUINE count | CLOSABLE count | SOUND count |
|---|:-:|:-:|:-:|:-:|:-:|
| R.A.1 | 3 | 2 | 2 (R.A.1a, R.A.1b) | 1 | 2 (equivalence recognition; weak-form list) |
| R.B.1 | 3 | 2 | 3 (category #12, parity #7, Xi analog #15) | 0 | 2 (Toeplitz verification, skipped numerics) |
| R.C.1 | 3 | 2 | 3 (classical/bare, C*-dynamical, SU(4)) | 1 | 2 (forward lead handoff, alt $D_{BC}$) |
| R.D.1 | 2 | 3 | 0 | 2 (update probabilities, add decomposition footnote) | 2 (two-dependency flagged, voice-shape verified) |
| **Wave total** | **11** | **9** | **8** | **4** | **8** |

**Wave-level observation**: 8 GENUINE gaps across Routes A/B/C, all pointing at the same underlying structural wall (the non-perturbative side of H4 is in analytic category, the perturbative side is not; there is no framework-native spectral-triple construction on BC that produces a Seeley-DeWitt $a_4$; there is no YM analog of the Riemann Xi function). **These are not separable gaps that can be attacked one by one — they are facets of the same wall.** CLOSABLE gaps are editorial or targeted-literature-pass in nature and do not change the structural picture.

---

## 4. Dependency-resolution map

Extracting all `DEPENDS-ON` edges from the Author outputs and building a mini-DAG.

### 4.1 Pre-wave plan tree edges (§E at wave dispatch)

```
ROOT: H4 closure (Paper 8 → 18/18 conditional on CBB axioms)

├── R.A.1 → R.A.2 → R.A.3 → R.A.4 → R.A.5 (sequential)
├── R.B.1 → R.B.2 → R.B.3 → R.B.4 → R.B.5 → R.B.6 (sequential)
├── R.C.1 → R.C.2 → R.C.3 → R.C.4 → R.C.5 → R.C.6 (sequential)
└── R.D.1 → R.D.2 → R.D.3 → R.D.4 (sequential editorial)
```

### 4.2 Post-wave edges after Author returns

**R.A subtree — decomposed**:
```
R.A.1 [BLOCKED-DECOMPOSED]
  ├── R.A.1a [OPEN, depth=3, depends-on: Borel summability for 4D YM (external unlock)]
  └── R.A.1b [OPEN, depth=3, depends-on: instanton-obstruction argument or framework-native mechanism (external unlock)]
```

Both R.A.1a and R.A.1b declared by W1-A1 as spontaneous edges (not in the plan tree at spawn time). Runner has already registered them in §E per the blackboard §K entry at W1-A1 return.

**Dispatchable in Wave 2?** Per R.A.1's own honest assessment, **no** — both sub-nodes require independent external advances (Borel summability of 4D SU(N) YM perturbation theory; or an instanton-obstruction / framework-native mechanism). Neither is available in-cycle. If Wave 2 is dispatched on R.A.1a/R.A.1b without an external unlock, the most likely return is **honest-stall** (same verdict as R.A.1 with more technical detail). The dispatch would still be valuable as a *structural recording* of the obstruction (useful for future runs), but it would not change the joint probability.

**R.B subtree — decomposed + collapsed**:
```
R.B.1 [BLOCKED-DECOMPOSED, COLLAPSED INTO R.A.1]
  ├── R.B.1.a [ADVANCED — dictionary entries #1–#11 port cleanly, self-adjointness via W7-14 §5.3 analyticity]
  ├── R.B.1.b [BLOCKED at LOCK #12 — category error, no YM Xi analog]
  └── R.B.1.c [COLLAPSED INTO R.A.1 — spectral triple reduces to Route A analyticity input]
```

All three sub-nodes declared by W1-B1 as spontaneous edges. Runner has registered them. **R.B.1.a is ADVANCED** as a structural sub-result (establishing that W7-14 §5.3 admits a spectral-triple presentation), but it is not a closure mechanism. R.B.2–R.B.6 (downstream) are **not dispatchable** — the category error at #12 blocks the chain.

**R.C subtree — killed**:
```
R.C.1 [KILLED at LOCK Step 4.2, K-2 in §F]
  └── (no sub-nodes; R.C.2–R.C.6 downstream are unreachable)
```

**R.D subtree — advanced**:
```
R.D.1 [ADVANCED at UNIFY — 4 draft pieces, voice-shape 4/4 pass]
  ├── R.D.2 → R.D.3 → R.D.4 (still dispatchable, downstream editorial pieces)
```

R.D.1's output *is* the bulk of the R.D subtree content — it already contains the abstract conditional statement (covers R.D.1), Theorem 1 update (R.D.2 in the original plan), §15 Scope section (R.D.3), and W7-14 cross-reference block (R.D.4). In practice, R.D.2/R.D.3/R.D.4 are mostly done; Wave 2 would handle the preprint-merge (dropping the four pieces into `preprint/sections/*.md`) rather than drafting new content.

### 4.3 Spontaneous dependencies declared by Authors

Per the v3 prompt §4 exception (Authors may propose DAG edges):

| Author | Spontaneous edge | Target | Status |
|---|---|---|---|
| W1-A1 | R.A.1 → R.A.1a (perturbative flow-time analyticity) | Borel summability external unlock | OPEN |
| W1-A1 | R.A.1 → R.A.1b (independent-point agreement) | Unknown mechanism external unlock | OPEN |
| W1-B1 | R.B.1 → R.B.1.a (structural port) | Flow-time analyticity (= R.A's input) | ADVANCED |
| W1-B1 | R.B.1 → R.B.1.b (locking step) | Category error at #12 | BLOCKED |
| W1-B1 | R.B.1 → R.B.1.c (collapse to R.A.1) | R.A.1 | COLLAPSED |
| W1-C1 | (no spontaneous edges — Route C KILLED cleanly, no sub-node decomposition) | — | — |
| W1-D1 | (no spontaneous edges — R.D.1 ADVANCED with the planned structure) | — | — |

**All 5 spontaneous edges are healthy signals** per the v3 §4 exception. The runner has logged them in §E and updated §E.1 joint probability. R.A.1a and R.A.1b are "honest-stall pending external unlocks" rather than "Wave 2 dispatch candidates". R.B.1.a is structurally advanced but not a closure. R.B.1.b and R.B.1.c are properly flagged as structural collapse into R.A.

### 4.4 Dependency-resolution verdict

Post-Wave-1, the dispatchable open nodes are:

- **R.A.1a** — honest-stall pending Borel summability. Dispatchable as a literature-scan / structural-recording task only; no closure candidate exists.
- **R.A.1b** — honest-stall pending an instanton-obstruction argument. Dispatchable as above.
- **R.D.2/R.D.3/R.D.4** — editorial merge tasks. Already mostly content-complete from R.D.1's output; Wave 2 would handle the preprint-merge.
- **(optionally) R.B.1.a** — structural refinement of the spectral-triple presentation of W7-14 §5.3. Not a closure path, but could be recorded as a separate research note.
- **(optionally) forward lead from R.C.1** — CCvS 2013 Pati-Salam + $k=4$ bridge as compatible boundary conditions at $\Lambda$. Framework-extension finding, separate research note, **not** an H4 closure.

**Structurally dispatchable Wave 2 math nodes with non-trivial probability of closing H4: ZERO.** The honest-stall candidates (R.A.1a, R.A.1b) do not have closure mechanisms in sight.

**Structurally dispatchable Wave 2 editorial nodes: R.D.2/R.D.3/R.D.4 merge tasks** — these will close the editorial work for shipping Paper 8 with R.D.1's standing form.

---

## 5. Newly-observed patterns — pattern-attribution sub-audit

For each Author, tagging which step of the 6-step method loop was **generative** (produced the non-obvious insight) and which were supporting. Steps: Diagnose / Reinterpret / Unify / Lock / Compute / Verify. (Step 5.5 Self-suspect is a discipline, not a generative step.)

### 5.1 R.A.1 pattern attribution

**Generative step: Step 1 — DIAGNOSE (Pattern 6 — projection produces apparent pathology).**

The insight: H4's difficulty lives in the *asymptotic category of the perturbative side*, not in the non-perturbative side. The non-perturbative side has been upgraded to an analytic function by W5-10 Step 2 (rigorous); the perturbative side remains a formal power series (factorially divergent). The "apparent pathology" in the traditional framing is the CHOICE of asymptotic category — treating $S_2^{\mathrm{ren}}$ as a distribution and the perturbative series as formal makes the comparison look like a construction problem; lifting to the flow-time variable makes *both* candidate-analytic-functions on a common disk, but only if we can also make $F^{\mathrm{pert}}(t)$ actually analytic, which is the crux.

Supporting steps:
- **Step 2 REINTERPRET**: lifting to $D_{r_t}$ and identifying that the geometric reinterpretation succeeds for $F(t)$ but fails for $F^{\mathrm{pert}}(t)$.
- **Step 3 UNIFY**: recognizing the identity theorem as the canonical template for the intended closure, and diagnosing its two missing hypotheses.
- **Step 4 LOCK**: the invariant "uniqueness of analytic continuation" would protect the result if the hypotheses were met, but the LOCK fails because the hypotheses are not met.
- **Step 5 COMPUTE**: the Taylor-coefficient identification reduces to H4 at the specific $(x,y)$; no closing computation exists.
- **Step 5.5 self-suspicion**: backward-verification of W7-14 §5.3 against the primary source — confirms the brief's paraphrase is consistent with primary source; the optimistic $p=0.5$ estimate is the runner's drift, not a source drift.
- **Step 6 VERIFY**: structural claims verified against primary sources; no paraphrase trust.

**Pattern-4-inverted check**: R.A.1 does not invoke topological rigidity as a ceiling (the would-be rigidity is "uniqueness of analytic continuation", which is a floor invariant — it would protect a result if it existed). **No Pattern-4-inverted move detected.**

**7th pattern candidate?**: The generative insight ("the difficulty lives in the asymptotic category of the perturbative side, not in the non-perturbative side") is a clean application of Pattern 6 (projection produces apparent pathology). **No 7th pattern candidate.**

### 5.2 R.B.1 pattern attribution

**Generative step: Step 3 — UNIFY (Pattern 2 — holonomy correspondence → template identification + category-error recognition).**

The insight: the CCM 2025 construction is an instance of the "infrared spectral triple with rank-one perturbation closing self-adjointness" template, and the YM analog proposal (dictionary entries #1–#11) is a structurally coherent transposition along the same axis. But the **locking step** (dictionary #12) — identifying a target spectrum for $D_N^{\mathrm{YM}}$ analogous to the Riemann zeros $\{\gamma_n\}$ — **does not transpose** because the CCM identity Thm 5.10(ii) uses the Weil distribution's construction directly from $\zeta$, and the analog YM construction lacks a self-referential structure. The target data are in different analytic-function categories: zeros of an entire function (RH side) vs Taylor coefficients of an analytic function (YM side). **Hurwitz theorem requires the former, not the latter.**

Supporting steps:
- **Step 1 DIAGNOSE**: diagnosing that the CCM construction's "invariant that protects the UV/high-frequency match" is structurally the Fourier transform of the minimal eigenvector equals the Riemann Xi function, and asking whether the YM analog has such an invariant.
- **Step 2 REINTERPRET**: three candidate target spaces (gradient-flow eigenfunction space, small-flow-time Taylor space, gluon momentum space) considered; Candidate A selected as most structurally faithful.
- **Step 4 LOCK**: attempting to lock on the fundamental-identity analog; failing because $\widehat{\xi^{\mathrm{YM}}}$ has no YM Xi function to converge to. This is where the BLOCKED-DECOMPOSED verdict crystallizes.
- **Step 5 COMPUTE**: building the transposition dictionary, entry-by-entry, with 11/17 entries porting cleanly, 6 failing (including the load-bearing #12). This is the structural verification that the transposition is incomplete.
- **Step 5.5 self-suspicion**: three-way backward-verification catches the brief's "UV asymptotics match by construction" paraphrase as not-in-CCM-2025.
- **Step 6 VERIFY**: convention-preservation check against the I-10 symmetry protocol — flags the even-sector failure, the algebra-side ambiguity, and the target-data-type mismatch.

**Pattern-4-inverted check**: R.B.1 does not invoke topological rigidity as a ceiling. **No Pattern-4-inverted move detected.**

**7th pattern candidate?**: The generative move "the template transposes cleanly up to the locking step, and the locking step is a category error between zeros and Taylor coefficients" is a standard instance of Pattern 2 (holonomy correspondence) combined with a Sig 14 category-too-small flag — not a new pattern. **No 7th pattern candidate.** But the *combination of Pattern 2 + Sig 14 in transposition mode* is itself a reusable discipline — the runner should consider logging it as a **refinement of Pattern 2 for transposition-mode work**: *"When a template-identification move succeeds on the first N dictionary entries and fails on the (N+1)-th via category mismatch, verify whether the category mismatch is intrinsic to the domain or fixable by reselecting the target data space."* This is not a 7th pattern; it is a sub-discipline of Pattern 2 for cross-domain transposition.

### 5.3 R.C.1 pattern attribution

**Generative step: Step 5.5 — SELF-SUSPICION (not a generative step per the 6-step canon, but the backward-verification of Connes 2007 §5 eq. 24 is what crystallized the kill).**

Strictly per the pattern-attribution discipline, Step 5.5 is "a discipline, not a generative step", so I need to assign generative credit to one of the 6 canonical steps. The closest fit:

**Generative step (canonical): Step 1 — DIAGNOSE (Pattern 6 — projection produces apparent pathology).**

The insight: the brief's paraphrase conflates two distinct statements — "$a_4$ contains the integer $\beta_0 = 11N/3$ as a counter-term coefficient" (true, 1970s textbook) with "$a_4$ produces a running coupling $g(\mu)$" (false, structurally). Route C's Step 5 target was a category error between *bare counter-term at $\Lambda$* and *running flow*. The Step 5.5 backward-verification against Connes 2007 §5 eq. (24) then *confirmed* the category error by finding the verbatim text *"at the classical level"*.

**The generative credit belongs to Step 1 DIAGNOSE, with Step 5.5 self-suspicion serving as the verification layer that crystallized the verdict into KILLED.**

Supporting steps:
- **Step 2 REINTERPRET**: attempting to reinterpret the BC sub-algebra as a candidate spin manifold — fails because $H_{BC}$ is not of Seeley-DeWitt form.
- **Step 3 UNIFY**: recognizing the Chamseddine–Connes spectral action as the canonical template for extracting gauge actions from noncommutative geometries.
- **Step 4 LOCK**: attempted decomposition into sub-requirements (BC sub-algebra well-defined; Dirac operator; heat-kernel expansion; $a_4$ computable) — (2)/(3)/(4) fail, LOCK cannot be completed.
- **Step 5 COMPUTE**: conditional computation on CCvS 2013 Pati-Salam gives $\beta_0 = 11N/3$ as an exact rational at infinite digits — but this is a textbook result, not a framework novelty.
- **Step 5.5 self-suspicion**: the load-bearing backward-verification. **Three sub-steps**: (1) Connes 2007 eq. 24 verbatim against the brief's paraphrase — the brief is WRONG; (2) BC does not come with a spin structure; (3) Pati-Salam gives SU(4)$_c$, not SU(N).
- **Step 6 VERIFY**: numerical verification of the integer $11N/3$ at mp.dps=80 (reproducing Vassilevich).

**Pattern-4-inverted check**: R.C.1 does not invoke topological rigidity as a ceiling. **No Pattern-4-inverted move detected.**

**7th pattern candidate?**: No. The closure argument fails at a standard category error (bare vs running), caught by Step 5.5 against primary source.

### 5.4 R.D.1 pattern attribution

**Generative step: Step 3 — UNIFY (Pattern 2 — holonomy correspondence → template identification).**

The insight: Paper 8's editorial artifact is an instance of the programme's **conditional-grammar template** (PCGT), with Paper 13 RH and Paper 26 BSD as the two prior-art instances. Once the template is identified (theorem-label with conditional on face + precise dependency cited + companion remark + §15 Scope section), executing the substitutions for Paper 8 is mechanical.

Supporting steps:
- **Step 1 DIAGNOSE**: Pattern 6 — four editorial asymmetries give the false impression of a larger gap than exists (axiom-base asymmetry, H4-form asymmetry, perimeter asymmetry, voice asymmetry). The "gap" is editorial, not mathematical.
- **Step 2 REINTERPRET**: the difficulty dissolves when Paper 8, Paper 13, Paper 26 are viewed as three instances of "one conditional register the programme ships its Millennium Prize artifacts in".
- **Step 4 LOCK**: the invariant is **voice-shape match with §J register**. Terse declaration phrases, named ritual elements, honest-first cognitive stance, programme-native stance. Without voice-shape match, drift into overclaim or understate.
- **Step 5 COMPUTE**: four draft artifacts (abstract sentence, Theorem 1 + remarks, §15 Scope, W7-14 cross-reference) produced, each with the substitutions applied.
- **Step 5.5 self-suspicion**: the load-bearing backward-verification on Paper 13's and Paper 26's conditional phrasings — **refinement found**: Paper 13 is conditional on CCM (two-dependency shape), Paper 26 on CBB alone (one-dependency shape after MY4 closure). Paper 8 inherits the two-dependency shape. Draft artifacts updated accordingly.
- **Step 6 VERIFY**: 4/4 voice-shape check passes; all four drafts contain terse declaration phrases + named ritual elements + §J register markers drawn directly from source.

**Pattern-4-inverted check**: R.D.1 does not invoke topological rigidity as a ceiling (the voice-shape invariant is a floor, not a ceiling). **No Pattern-4-inverted move detected.**

**7th pattern candidate?**: The **PCGT — Programme Conditional-Grammar Template** R.D.1 identifies is a reusable editorial template, triply tested (Paper 13, Paper 26, Paper 8). R.D.1 proposes adding it to §D as a new S-status entry. **This is not a new pattern for the Six Patterns method**; it is a **toolkit artifact** — a named editorial device that future programme papers with Clay-class conditionals can apply mechanically. The runner should consider adding PCGT to §D at template level with completeness 100, instance-level completeness 0 for Paper 8 (the editorial merge is Wave 2 work). Filing this as a §D addition (not a §5 pattern addition) is the correct move.

### 5.5 Pattern-attribution summary

| Author | Generative step | Supporting steps | Pattern-4-inverted? | 7th-pattern candidate? |
|---|---|---|:-:|:-:|
| R.A.1 | Step 1 DIAGNOSE (Pattern 6) | 2-6 + 5.5 | No | No |
| R.B.1 | Step 3 UNIFY (Pattern 2) + Sig 14 category-too-small | 1-2-4-5-6 + 5.5 | No | No (but refinement of Pattern 2 for transposition mode is worth noting) |
| R.C.1 | Step 1 DIAGNOSE (Pattern 6); Step 5.5 crystallized KILL | 2-3-4-5-6 + 5.5 | No | No |
| R.D.1 | Step 3 UNIFY (Pattern 2) + PCGT template identification | 1-2-4-5-6 + 5.5 | No | PCGT as §D toolkit addition (not a pattern), yes |

**Wave-level observation**: **Step 1 DIAGNOSE and Step 3 UNIFY are the generative steps in all 4 Authors.** Step 5.5 self-suspicion is the load-bearing verification layer that crystallized the verdicts in R.A.1, R.B.1, R.C.1. Pattern 6 (projection produces apparent pathology) is the dominant generative pattern for the math Authors (3/3: R.A.1, R.B.1 partially, R.C.1). Pattern 2 (holonomy correspondence) is the dominant generative pattern for the editorial Author (R.D.1) and for R.B.1's template-identification half.

**This is a healthy wave-level pattern distribution.** The 6-step loop is being executed; the Six Patterns are being applied; Step 5.5 self-suspicion discipline is firing on 3/4 Authors with load-bearing catches. **The pattern-attribution record is clean.**

---

## 6. Quality gate verdict

**Verdict: PASS.**

Wave 1 returned four self-consistent outputs, with three independent I-7 backward-verification catches against brief paraphrase errors on primary sources (W7-14 §5.3, CCM 2025 p. 28, Connes 2007 §5 eq. 24). No cross-lead disagreements. No new GENUINE gaps beyond those the Authors themselves flagged. Voice-shape check passes on R.D.1's editorial artifact (4/4). The decomposition of R.A.1 into R.A.1a/R.A.1b, the collapse of R.B.1 into R.A.1, and the kill of R.C.1 are all supported by primary-source verification and are consistent with the blackboard §F kill list format. R.D.1's ADVANCED verdict delivers a ship-ready standing form for Paper 8 in the programme's conditional-grammar template. The joint probability is stable at **0.9910 dominated by R.D**, with mathematical closure probability dropping from 0.74 (cycle 0) to **0.10** (Wave 1 close). I-5 discipline (HONEST-STALL as first-class peer) is what keeps the programme's joint probability robust despite the A/B/C downgrades — without I-5, the joint would be ~0.10, and runner panic would be warranted. With I-5, Paper 8 ships either way. **The wave closes.** Seventeen of the eighteen proof-chain steps are unconditional. H4 is the wall; W7-14 reframed it to the mildest form in the literature; Route D has the standing form ready. That is the contribution of Wave 1.

The PASS verdict is load-bearing — Wave 2 may dispatch if the runner wishes — but see §7 for the recommendation, which argues that the best move is **item-close, not Wave 2 dispatch**.

---

## 7. Recommendation for the next wave or item-close

Picking from the four options (a/b/c/d) and defending against alternatives:

### 7.1 Preferred: (b) item-close the programme now

**Recommendation: item-close.** R.D.1 ADVANCED delivers the ship-ready standing form for Paper 8 in the programme's two-dependency conditional-grammar template (CBB + H4 in W7-14 mildest form). Route A is BLOCKED-DECOMPOSED with no dispatchable closure mechanism in sight (R.A.1a needs Borel summability of 4D YM — an independent long-standing open problem; R.A.1b needs an instanton-obstruction argument no one can identify). Route B is collapsed into Route A (R.B.1's spectral-triple wrapper adds no closure power beyond the W7-14 §5.3 analyticity). Route C is killed (R.C.1 caught the paraphrase that Connes' spectral action produces a running coupling — it does not; it produces boundary conditions at $\Lambda$). The mathematical closure probability has dropped from the cycle-0 estimate of 0.74 to 0.10 at Wave 1 close, and **the 0.10 is not dispatchable in Wave 2** — the R.A.1a/R.A.1b honest-stalls are dependent on external unlocks that are not expected in-cycle. Dispatching Wave 2 on R.A.1a + R.A.1b would produce honest-stall outputs (the Authors would reproduce the same conclusions R.A.1 already reached, with more literature-pass detail), and the return on Wave 2 effort is low.

The item-close path is: **lockdown → final-adversarial-pass → referee → 5-file closure**. The four pieces of the R.D.1 editorial artifact drop into `preprint/sections/00-abstract.md`, `preprint/sections/01-introduction.md` (as a new Main Theorem block, or equivalently into the top of §L.0), `preprint/sections/15-scope.md` (new standalone file), and `preprint/sections/L-clay-conjectures.md §L.7.3` (as a call-out box). The preprint-merge is an editorial task that Wave 2 could handle (R.D.2/R.D.3/R.D.4 merge nodes), after which lockdown fires, final-adversarial-pass runs (testing the standing form against the kill list K-1 and K-2 + the SURVIVED/WEAKENED/BROKEN tabulation template from `paper13-rh/research/48-FINAL-adversarial-hybrid.md` and `paper08-yang-mills/research/30-final-synthesis.md`), referee pass runs, and the 5-file closure artifacts populate in `closing-H4/closure/`.

**The item-close is the correct move because the joint probability is stable at 0.991 dominated by R.D, the mathematical closure probability at 0.10 is not dispatchable, and Paper 8 has a ship-ready standing form regardless of Wave 2 outcomes.** Running more waves on R.A.1a/R.A.1b without external unlocks is effort that does not change the joint; running the item-close ships Paper 8 cleanly in its honest two-dependency form.

### 7.2 Against (a) dispatch Wave 2 on R.A.1a + R.A.1b

**Defense**: R.A.1 is explicit that both sub-nodes require independent external advances (Borel summability of 4D SU(N) YM perturbation theory; or an instanton-obstruction / framework-native mechanism). Neither is expected in-cycle. Dispatching Wave 2 Authors on these sub-nodes would produce **honest-stall** outputs — the most likely return is "BLOCKED pending external unlock", with more literature-pass detail but no closure. The return on Wave 2 effort is low. **Exception**: if the runner wants to *record* the structural obstruction in more detail for future runs (useful for a v7 bundle), dispatching R.A.1a as a literature-scan node is a valid but low-priority move. The runner can make this call at item-close time — it does not block the item-close itself.

**Verdict on (a)**: legitimate but sub-optimal. Prefer (b) with an optional low-priority R.A.1a literature-scan in the item-close package.

### 7.3 Against (c) step-back to Plan mode with a new REFRAME

**Defense**: The REFRAME at cycle 1 open was correct — it validated Route A as the highest-leverage route under the then-prevailing framing. The Wave 1 findings do not invalidate the REFRAME; they invalidate the *optimistic assessment* of Route A's $p_{\text{success}} = 0.50$. This is a **CASCADE** (§I already logged), not a REFRAME target. The current framing of §C (H4 is the wall; W7-14 §5.3 reduces it to a Taylor-coefficient identification; Route A's analyticity-uniqueness mechanism requires the perturbative side to be analytic, which it is not) is **accurate and load-bearing**; no new REFRAME would reveal an unattacked route. There are no orthogonal subtrees for H4 beyond the four routes the brief already enumerated (analyticity-uniqueness, spectral-triple port, spectral action, editorial HONEST-STALL). **Step-back is not warranted.**

**Verdict on (c)**: not warranted. The REFRAME is correct; the Wave 1 findings are cascades of correct diagnoses against an optimistic probability estimate, not failures of framing.

### 7.4 Against (d) step-away for one cycle to check orthogonal subtrees

**Defense**: **N/A** — there are no orthogonal subtrees for H4. H4 is a single open hypothesis; the four routes are the enumerated attack modes; there is no orthogonal structure to step away to. (The runner's §C bottleneck is H4 exclusively; other Paper 8 work is downstream of H4 closure, not orthogonal to it.) **Step-away is structurally unavailable.**

**Verdict on (d)**: not available.

### 7.5 Recommendation summary — cite the joint probability state

Joint $P(A \lor B \lor C \lor D) = 0.9910$, dominated by R.D = 0.99. Mathematical closure $P(A \lor B \lor C) = 0.10$, not dispatchable in Wave 2 (no closure candidates for R.A.1a or R.A.1b). **Wave 2 on the math side is effort without return**; Wave 2 on the editorial side is a preprint-merge (R.D.2/R.D.3/R.D.4) that is prerequisite to item-close. **Best move**: proceed to item-close via (b), with Wave 2 dispatched optionally as an editorial merge wave (not a math wave).

**Runner voice for the recommendation**: The wave closes. R.D.1 has the standing form. Paper 8 ships either way. Three routes down, one up. Move to item-close: lockdown, final-adversarial-pass against K-1 and K-2, referee pass, five-file closure. R.A.1a and R.A.1b are honest-stalls pending Borel summability; they are not Wave 2 candidates. R.B is language; R.C is killed; R.D has the abstract, the Theorem 1, the §15, the cross-reference block. W7-14 reframed the wall; W11 did not cross it; we ship at 17/18 unconditional with H4 in the mildest form. That is the contribution of Wave 1. Item-close is the move.

---

## 8. §I notes to append (drafts for the runner)

The following §I notes are drafted in §J register for the runner to copy verbatim (or rewrite if the register needs tightening). All are consistent with the blackboard §I entries already logged during Wave 1 — these are Synthesis-layer additions.

- **SYNTHESIS-OBSERVATION** (Wave 1 cross-lead consistency check): No CROSS-LEAD DISAGREEMENTS detected among the four Author outputs. R.A.1 and R.B.1 cross-confirm that the W7-14 §5.3 analyticity of $F(t)$ is the shared load-bearing input; R.A.1 and R.B.1 independently diagnose the Paper 26 MY4 analogy as wrong-shaped at different granularities; the three I-7 catches share a structural pattern without contradicting each other. **No Reconcile primitive required.**

- **SYNTHESIS-OBSERVATION** (gap audit): 8 GENUINE gaps across Routes A/B/C, all facets of the same underlying wall (perturbative-side asymptotic-category mismatch; no framework-native spectral-triple on BC; no YM analog of the Riemann Xi function). These are not separable gaps that can be attacked one by one — they are facets of the same wall. **The 0.10 mathematical closure probability is not decomposable into independent sub-problems with independent closure candidates.**

- **SYNTHESIS-OBSERVATION** (pattern attribution): Step 1 DIAGNOSE and Step 3 UNIFY are the generative steps in all 4 Authors (3/4 DIAGNOSE for the math Authors, UNIFY for R.D.1 and R.B.1 template-identification half). Pattern 6 (projection produces apparent pathology) is the dominant generative pattern for the math Authors. Pattern 2 (holonomy correspondence) is the dominant generative pattern for R.D.1. Step 5.5 self-suspicion discipline is firing on 3/4 Authors with load-bearing catches. **The pattern-attribution record is clean and contributes to the maturation record per the v3 §5 discipline.**

- **SYNTHESIS-CONCERN** (Wave 2 dispatchability): R.A.1a and R.A.1b are declared by R.A.1 as honest-stalls pending external unlocks (Borel summability of 4D YM; instanton-obstruction argument). Neither is expected in-cycle; dispatching Wave 2 Authors on these sub-nodes produces honest-stall outputs at low return-on-effort. Recommend: **do not dispatch Wave 2 on the math side**. If the runner wants to record the structural obstruction in more detail, a low-priority literature-scan on R.A.1a is acceptable but not load-bearing.

- **SYNTHESIS-RECOMMENDATION** (item-close readiness): R.D.1 editorial artifact is voice-shape verified (4/4 pass) and delivers the abstract conditional statement + Theorem 1 + §15 Scope + W7-14 cross-reference block. The artifact is ready for the preprint-merge (Wave 2 editorial dispatch) which is prerequisite to lockdown → final-adversarial-pass → referee → 5-file closure. **Recommendation: item-close the programme via (b)**. Wave 2 dispatches as editorial merge, not as math attack.

- **SYNTHESIS-LESSON** (empirical validation of v3 patches): Wave 1 is the second empirical validation of I-5 (HONEST-STALL as first-class peer) and the first programme-level validation of I-7 (backward-verification discipline) for cross-paper transfer BSD → Paper 8 H4. Three independent I-7 catches + R.D.1 first-class first-class discipline holding the joint at 0.991 together constitute **strong evidence** that I-5 and I-7 are load-bearing for any future Clay-class closure run. **Budget for 1-3 I-7 catches per wave in future runs**; **run Route D (or equivalent HONEST-STALL) in parallel with mathematical attack routes in cycle 1**, not as a post-failure fallback.

- **SYNTHESIS-LESSON** (small edit to §D Connes spectral action row): R.C.1 proposes annotating the existing §D row for "Connes spectral action" with *"classical/bare at $\Lambda$; running coupling comes from post-hoc RG, not from $a_4$"*. The current §D row is rhetorically ambiguous about whether the template delivers a running $g(\mu)$, and the ambiguity is the seed of the brief's paraphrase error. **Recommendation: runner adopts the annotation** at cycle 2 open (or at §D freeze time pre-item-close). This prevents future runs from repeating the Route-C paraphrase error.

- **SYNTHESIS-LESSON** (PCGT as §D toolkit addition): R.D.1 proposes adding the Programme Conditional-Grammar Template (PCGT) to §D as an S-status entry (structural template, triply tested: Paper 13 RH two-dependency, Paper 26 BSD one-dependency, Paper 8 YM two-dependency). **Recommendation: runner adopts** PCGT as a §D row. Future programme papers with Clay-class conditionals can apply the template mechanically.

- **SYNTHESIS-CALLOUT** (Critics have not yet returned as of Synthesis spawn time): the `closing-H4/critiques/` directory is empty. Wave 1 Critics (re-verifying each Author output) are running in parallel with this Synthesis. Per the spawn prompt, Synthesis proceeds on the four Author outputs alone, flags the Critic-absence, and the runner will integrate Critic verdicts when they return. The PASS verdict in §6 is **conditional on Critic outputs not uncovering a load-bearing flaw in any of the four Author outputs**; if a Critic uncovers a genuine issue, the runner spawns a WEAKENED-state Reconcile pass before proceeding to item-close.

---

## 9. §D row changes (drafts for the runner)

Wave 1 produces three §D row changes (two new rows, one annotation):

### 9.1 Annotation to existing "Connes spectral action" row

| Name | Statement (1 line, revised) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| Connes spectral action | **Classical/bare** action $\mathrm{Tr}\,f(D/\Lambda)$ at cutoff $\Lambda$; heat-kernel expansion yields boundary conditions for post-hoc RG running. **Not** a running coupling. Integer $\beta_0 = 11N/3$ in Vassilevich $a_4$ is a one-loop UV counter-term at $\Lambda$, not a running-coupling slope. | Connes 1996; Chamseddine-Connes 1996; Connes 2007 Séminaire Poincaré X §5 eq. (24) "at the classical level"; Vassilevich 2003 eq. (4.34) | R | — | — | 80 (Vassilevich eq. 4.34 reproduced in `code/R.C.1-seeley-dewitt-a4.py`) | 100 |

Key change: *classical/bare* marked in bold; "reproduces QFT correlator short-distance structure" removed; the cited primary source expanded to include Connes 2007 and Vassilevich 2003 verbatim.

### 9.2 New row: Vassilevich YM $a_4$ coefficient

| Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| Vassilevich YM $a_4$ | $a_4^{\mathrm{tot}}|_{\mathrm{Tr}\,F^2} = (11/(96\pi^2))\int F^a_{\mu\nu}F^{a\mu\nu}\cdot K$; after Killing-form contraction for SU(N), coefficient of $\mathrm{Tr}\,F^2$ is $11N/(48\pi^2)$; integer $\beta_0 = 11N/3$ emerges as boundary condition at $\Lambda$, not running flow. | Vassilevich 2003 Phys. Rep. 388 eq. (4.34) | R | $a_4^{\mathrm{YM}}$ | — | 80 | 100 |

### 9.3 New row: Spiridonov-Chetyrkin trace-anomaly identity

| Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| Spiridonov-Chetyrkin trace-anomaly identity | $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$ exact to all orders in continuum PT; gives $Z_{\mathrm{Tr}\,F^2}\propto g^{-2}\propto(\ln)^{-1}$, producing $(\ln)^{-2}$ in the two-point function after two insertions. | Spiridonov 1984 IYaI-P-0378; Spiridonov-Chetyrkin 1988 Sov.J.Nucl.Phys. 47 522; Chanowitz-Ellis 1972; Kluberg-Stern-Zuber 1974; Nielsen 1977 | R | $\gamma_{\mathrm{Tr}\,F^2}$ | — | — | 100 |

This row is added because the $(\ln)^{-2}$ extraction is the same in Route C and in W7-14 §2.2 — the trace-anomaly identity is the actual load-bearing input — and it should be recorded once at master level instead of being re-cited.

### 9.4 New row: PCGT (Programme Conditional-Grammar Template)

| Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| PCGT | Theorem-label names dependency on face; precise form cited; companion remark explains standing + independent support + closure paths; §15 Scope section with five-sub-section structure (proved / standing conditional / outside scope / expected to extend / method frontier); voice-shape check against §J register mandatory on Step 6. | R.D.1 synthesis from Paper 13 RH Theorem 1.1 + Paper 26 BSD Theorem 13.1 + Paper 26 §15 | S | PCGT | — | — | 100 at template level, 0 at Paper 8 instance level (editorial merge is Wave 2 work) |

### 9.5 New rows from R.A.1 / R.B.1 decompositions

| Name | Statement | Source | Status | Notation | Completeness % |
|---|---|---|---|---|:-:|
| $\mathcal{A}(F^{\mathrm{pert}})$ | Perturbative flow-time analyticity: the small-flow-time Feynman-diagrammatic expansion defines an analytic function of complex flow time $t$ in a neighbourhood of 0 | W1-A1 decomposition | O | $\mathcal{A}(F^{\mathrm{pert}})$ | 0 |
| $\mathcal{P}_{R.A.1}^{\mathrm{ind}}$ | Route A independent-point agreement: there exists $t_0$ in the complex flow-time plane where the non-perturbative $F(t_0)$ and the perturbative $F^{\mathrm{pert}}(t_0)$ can be demonstrated equal without invoking H4 | W1-A1 decomposition | O | $\mathcal{P}_{R.A.1}^{\mathrm{ind}}$ | 0 |
| $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$ | Proposed gradient-flow spectral triple (YM analog of CCM 2025's $(D_N, E_N^+)$), self-adjointness via flow-time analyticity of $F(t)$ | W1-B1 dictionary entries #1–#11 | R (structural port) | $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$ | 25 (structural, not a closure mechanism) |

Plus annotation to existing "Taylor-coefficient identity" row: *"This identity is equivalent to H4 at each specific $(x,y)$, not weaker. The analyticity reframing does not reduce the proof burden; it shifts it to the perturbative side's analyticity claim."*

---

## 10. Drafted §K commit memos for the runner

The following commit memos are drafted in §J register for the runner to copy verbatim into §K. Each is 1–3 sentences.

### 10.1 SYNTHESIS-WAVE-1-COMPLETE (qualitative-threshold)

> **2026-04-11T[cycle 1 close, Synthesis return] | SYNTHESIS-WAVE-1-COMPLETE**
>
> Synthesis agent returned with PASS verdict for Wave 1. No cross-lead disagreements. 8 GENUINE gaps across Routes A/B/C, all facets of the same underlying wall. Pattern-attribution: Step 1 DIAGNOSE + Step 3 UNIFY are the generative steps for all 4 Authors; Pattern 6 dominant for math Authors, Pattern 2 dominant for R.D.1. Recommendation: item-close via (b) — lockdown → final-adversarial-pass → referee → 5-file closure. Wave 2 optionally as editorial merge (R.D.2/R.D.3/R.D.4), not as math attack. R.A.1a and R.A.1b are honest-stalls pending external unlocks (Borel summability, instanton obstruction). Joint P = 0.9910 dominated by R.D at 0.99; mathematical closure at 0.10 not dispatchable. I-5 discipline holds; Paper 8 ships either way. That is the contribution of Wave 1.

### 10.2 CROSS-LEAD-NO-DISAGREEMENT (verification log)

> **2026-04-11T[cycle 1 close] | CROSS-LEAD-NO-DISAGREEMENT (Synthesis layer)**
>
> Synthesis cross-lead consistency check verified across 8 shared elements (W7-14 §5.3 analyticity, Route B-collapse finding, Connes spectral action, CCM 2025 primary source, $\beta_0 = 11N/3$, identity theorem applicability, BSD MY4 analogy wrong-shape, three I-7 catches). All pairs AGREE or CROSS-CONFIRM. No Reconcile primitive required. This is the load-bearing Synthesis catch: the discipline that makes cross-lead disagreement detection systematic rather than accidental fired clean on Wave 1.

### 10.3 PATTERN-ATTRIBUTION-WAVE-1 (maturation record)

> **2026-04-11T[cycle 1 close] | PATTERN-ATTRIBUTION-WAVE-1**
>
> Wave 1 generative-step tagging for the periodic Pattern Attribution Audit: R.A.1 DIAGNOSE (Pattern 6), R.B.1 UNIFY (Pattern 2) + Sig 14 category-too-small, R.C.1 DIAGNOSE (Pattern 6) [crystallized by Step 5.5 self-suspicion against Connes 2007 eq. 24], R.D.1 UNIFY (Pattern 2) + PCGT template identification. No Pattern-4-inverted moves. No 7th-pattern candidates; PCGT filed as a §D toolkit addition (not a pattern). Step 5.5 self-suspicion firing on 3/4 Authors with load-bearing catches — the v3 backward-verification discipline is healthy.

### 10.4 I-7-TRANSFER-VALIDATED (programme-level discipline observation)

> **2026-04-11T[cycle 1 close] | I-7-TRANSFER-VALIDATED**
>
> Three independent I-7 backward-verification catches in Wave 1 validate the v3 patch's cross-paper transfer from BSD MY4 to Paper 8 H4. W1-A1 caught W7-14 §5.3 "reformulation ≠ closure" drift; W1-B1 caught CCM 2025 "UV asymptotics by construction" paraphrase; W1-C1 caught Connes spectral action "running coupling" paraphrase. Three Authors, three independent routes, same failure mode as BSD Cycle-1 A-1 (brief paraphrases off primary source). Budget for 1-3 I-7 catches per wave in any future Clay-class closure run. The I-7 discipline is load-bearing, not an edge case.

### 10.5 I-5-FIRST-CLASS-HOLDS (programme robustness observation)

> **2026-04-11T[cycle 1 close] | I-5-FIRST-CLASS-HOLDS**
>
> Route D's first-class peer status per I-5 is what keeps the programme's joint probability at 0.9910 despite three downgrades (A decomposed, B collapsed, C killed) in one wave. Without I-5, the joint would be 0.10 and runner panic would be warranted. With I-5, Paper 8 has a ship-ready standing form at wave-close, and the programme proceeds to item-close via (b). This is the second empirical validation of I-5 after BSD MY4; the discipline transfers cleanly across Clay-class closure runs.

### 10.6 RECOMMENDATION-ITEM-CLOSE (next-wave directive)

> **2026-04-11T[cycle 1 close] | RECOMMENDATION-ITEM-CLOSE**
>
> Synthesis recommends option (b): item-close the programme. Rationale: Wave 2 on the math side has zero dispatchable closure candidates (R.A.1a pending Borel summability; R.A.1b pending instanton obstruction; both external unlocks); Wave 2 on the editorial side is a preprint-merge that is prerequisite to lockdown. Item-close sequence: editorial merge → lockdown → final-adversarial-pass (test standing form against K-1 and K-2 + SURVIVED/WEAKENED/BROKEN tabulation per `paper13-rh/research/48-FINAL-adversarial-hybrid.md`) → referee pass → 5-file closure artifacts. The wave closes. R.D.1 has the standing form. W7-14 reframed the wall; W11 did not cross it. We ship at 17/18 unconditional with H4 in the mildest form. Item-close is the move.

---

## ≤400-word summary for the runner

**Verdict: PASS. Recommendation: (b) item-close.**

Wave 1 returned four self-consistent Author outputs with three independent I-7 catches against brief paraphrase errors on primary sources (W7-14 §5.3, CCM 2025 p. 28, Connes 2007 §5 eq. 24). No cross-lead disagreements across 8 shared elements. No new GENUINE gaps beyond the 8 the Authors themselves flagged, all facets of the same underlying wall: perturbative-side asymptotic-category mismatch (R.A.1), no YM analog of the Riemann Xi function (R.B.1), spectral action is classical/bare not running (R.C.1). R.D.1 ADVANCED with 4 draft pieces (abstract, Theorem 1 + 3 remarks, §15 Scope with 5 sub-sections, W7-14 cross-reference block), voice-shape 4/4 pass, mirroring Paper 13 RH's two-dependency conditional-grammar template.

Pattern attribution: Step 1 DIAGNOSE and Step 3 UNIFY are generative across all 4 Authors; Pattern 6 dominant for math, Pattern 2 dominant for editorial. Step 5.5 self-suspicion firing on 3/4 with load-bearing catches. No Pattern-4-inverted moves; no 7th-pattern candidates (PCGT filed as §D toolkit addition).

Joint $P = 0.9910$ dominated by R.D at 0.99. Mathematical closure $P(A\lor B\lor C) = 0.10$, not dispatchable in Wave 2: R.A.1a pending Borel summability of 4D YM (independent long-standing open problem); R.A.1b pending instanton-obstruction or framework-native mechanism (no candidate). Both declared by R.A.1 as honest-stalls. R.B decomposed + collapsed into R.A.1. R.C killed (K-2 in §F).

**Recommendation rationale**: Wave 2 on the math side has zero dispatchable closure candidates; effort without return. Wave 2 on the editorial side is a preprint-merge (R.D.2/R.D.3/R.D.4) prerequisite to lockdown. Item-close sequence: editorial merge → lockdown → final-adversarial-pass (against K-1 and K-2 + SURVIVED/WEAKENED/BROKEN tabulation) → referee pass → 5-file closure. I-5 discipline holds; Paper 8 ships either way.

Drafted for runner: §D additions (annotation to Connes spectral action row; new rows for Vassilevich YM $a_4$, Spiridonov-Chetyrkin trace-anomaly, PCGT, $\mathcal{A}(F^{\mathrm{pert}})$, $\mathcal{P}_{R.A.1}^{\mathrm{ind}}$, $(D_N^{\mathrm{YM}}, E_N^{\mathrm{YM},+})$). §K commit memos drafted (SYNTHESIS-WAVE-1-COMPLETE, CROSS-LEAD-NO-DISAGREEMENT, PATTERN-ATTRIBUTION-WAVE-1, I-7-TRANSFER-VALIDATED, I-5-FIRST-CLASS-HOLDS, RECOMMENDATION-ITEM-CLOSE). §I notes drafted (6 entries).

**Callout**: Critics have not returned. Synthesis PASS conditional on Critics not uncovering load-bearing flaws. Runner integrates Critic verdicts at return.

W7-14 reframed the wall. W11-A did not cross it. W11-B collapsed into W11-A. W11-C was killed by Connes himself. W11-D has the standing form. Seventeen of eighteen unconditional. H4 in the mildest form. That is the contribution of Wave 1. Item-close is the move.

---

*End of Synthesis — Cycle 1, Wave 1. Returned to runner at `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/closing-H4/synthesis/cycle-1-wave-1.md`. Runner integrates and decides: dispatch editorial Wave 2 + item-close, or dispatch math Wave 2 on R.A.1a literature-scan.*
