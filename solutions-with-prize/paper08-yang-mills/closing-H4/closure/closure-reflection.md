# What we learned: reflection on H4 closure for Paper 8 Yang-Mills mass gap

*Structured reflection on the H4 closure programme. Written post-adversarial. §J register where structural events are narrated; analytical register for the taxonomy sections.*

*Runner: Claude Opus 4.6 (1M context). Bundle: ora-bundle-v6. Date: 2026-04-11.*

---

## 1. The big picture

H4 is the standard "non-perturbative = perturbative at short distances" hypothesis of lattice QCD, open for 4D non-Abelian Yang-Mills, proved only for super-renormalizable theories like $\phi^4_3$. The Jaffe-Witten §4 referee's own assessment (`notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4d-operator-product-expansion.md`): **comparable in difficulty to constructing the theory itself.** Hollands-Wald's perturbative framework does not extend to non-Abelian 4D. Bostelmann's phase-space approach presumes the QFT already exists. SVZ OPE for QCD phenomenology is a physical hypothesis, not a theorem.

The H4 closure programme attempted four routes against this wall: A (Taylor-coefficient identification via W7-14 §5.3 analyticity), B (CCM 2025 spectral triple port), C (spectral action + Identity 12 + bridge family), D (HONEST-STALL editorial). After Wave 1, Routes A/B/C all failed at the structural level for different reasons; Route D advanced through a revision sub-cycle to a ship-ready editorial artifact; the programme item-closed with Paper 8 shipping 17/18 unconditional with H4 in the W7-14 §5.3 mildest form.

Mathematically, H4 remains OPEN. Editorially, Paper 8 now has a shippable Clay-compliant form with an honestly-stated conditional. The framework's 36/36 master table, Wolfenstein closed forms, Pati-Salam $\alpha_{PS}^{-1} = 17$, cosmic age formula $t_0 = (\log\gamma_7)^2$, seven anchors — all independent of H4 and unaffected.

## 2. Discovery 1: The Paper 26 BSD analogy breaks for H4

The brief explicitly framed Paper 8's H4 closure as *"the analog for Paper 8 of the MY4 closure for Paper 26"*, citing G's projector $P_k^{\mathfrak{p}}$ as the canonical example. Wave 1 found this analogy wrong-shaped.

**BSD §§7-8 was already algebraic.** G's projector $P_k^{\mathfrak{p}} := I - s_{\mathfrak{p}}^k (s_{\mathfrak{p}}^k)^*$ closed MY4 by reframing an already-algebraic core from Paper 26 §7.2 into a single algebraic object — "zero new mathematics", just a recognition that the BC bridge algebra already contained the bypass in operator-algebraic form.

**Paper 8's H4 core is NOT already algebraic.** It lives in constructive QFT. The W7-14 §5.3 reformulation moves the rigor burden from the non-perturbative side (the original question: does the non-perturbative Schwinger function admit an AF-matching asymptotic expansion?) to the perturbative side (the reformulated question: do the Taylor coefficients of $F(t) = S_{2,t}^c / c_1(t)^2$ at $t=0$ match the perturbative coefficients?), but it does NOT eliminate the burden.

**The lesson**: reformulation into the mildest form is real structural progress, not closure. A reformulation that reduces "prove X" to "prove Y" where Y is comparable in difficulty to X is *refactoring*, not *resolution*. The W1-A1 Author DIAGNOSE caught this directly: *"What H4 asks in this language is whether the Taylor coefficients are computable by the Feynman-diagrammatic perturbative rules — that is a more accessible question, not an answered one."*

Future runs on "mildest form" claims should apply Sig 14 category-too-small flag on first encounter. If someone says "X reframes Y into the mildest form in the literature", ask whether the mildest form is still harder than everything else the framework has closed. If yes, treat it as a category error — do not treat reformulation as synonymous with closure.

## 3. Discovery 2: Three I-7 catches in one wave validate cross-paper transfer

W1-A1, W1-B1, W1-C1 each independently caught a load-bearing brief paraphrase error:

1. **W7-14 §5.3 "mildest form" framing**: the brief treated "reformulation to Taylor coefficients of $F(t)$" as synonymous with "one-bypass-step from closure". W1-A1 read W7-14 §5.3 directly and found the primary source is *explicitly honest* that H4 remains OPEN after the analyticity reframing. The quote *"more accessible question"* refers to a question that is asked in the new language, not a question that is answered.

2. **CCM 2025 "UV asymptotics by construction"**: the brief claimed CCM 2025 provides operators whose UV asymptotics match perturbation theory *by construction*. W1-B1 WebFetched CCM 2025 (the local PDF `paper13-rh/sources/ccm-zeta-spectral-triples-2025.pdf`) and found the verbatim: *"Justifying rigorously this step is the main remaining obstacle to our approach to RH."* The paraphrase was not in the primary source. Additionally, the word "perturbation" in CCM 2025 refers to *"rank-one perturbation of the spectral triple"* (operator-theoretic), not QFT perturbation theory — a lexical category error caught later in the run by Delta-Critic applying the new I-v6-1 inference check.

3. **Connes 2007 spectral action "running coupling from $a_4$"**: the brief claimed the Seeley-DeWitt expansion *automatically* reproduces the running coupling. W1-C1 WebFetched Connes 2007 Séminaire Poincaré X from `seminaire-poincare.pages.math.cnrs.fr/connes2.pdf` and found the verbatim at §5 eq. (24): *"at the classical level"* — the spectral action is a classical functional that produces bare actions at the cutoff $\Lambda$, not a running-coupling generator. Vassilevich 2003 eq. (4.34) further confirms the integer $11N/3$ is a counter-term coefficient in one-loop UV divergence via zeta regularization, NOT a running-coupling slope.

**Same failure mode as BSD MY4 Cycle-1 A-1**: three errors in a support-runner answer caught only by numerical experiment against primary source. The I-7 backward-verification discipline (from v3's I-7 patch) transferred cleanly from BSD MY4 to Paper 8 H4 and fired on three independent Authors on three independent routes. **This is strong evidence the discipline is load-bearing for any Clay-class closure run**, not a BSD-specific artifact. Budget for 1-3 I-7 catches per wave in future Clay-class runs.

## 4. Discovery 3: Cross-node structural LOCK at 9/10 on the attack-surface identification

R.A.1 and R.B.1 independently identified Taylor-coefficient identification of $F(t)$ as the real attack surface for H4 closure via analyticity/identity-theorem mechanisms. Both blocked there, for **complementary reasons**:

- **R.A.1** blocked because $F^{\mathrm{pert}}(t)$ is a formal power series (the identity theorem's two-function hypothesis fails on the perturbative side — one of the two functions isn't actually an analytic function).
- **R.B.1** blocked because YM target data would be Taylor coefficients of an analytic function, but CCM 2025 machinery requires zeros of an entire function (category error at dictionary entries #12-17).

**LOCK verification** (via Sig 10 protocol):
1. Load-bearing failure rows are non-overlapping: R.A.1 fails on $F^{\mathrm{pert}}$ non-analyticity; R.B.1 fails on target-data category mismatch. Different obstructions.
2. Failure mode pattern categories are different: Distributional + Wrong-space (R.A.1) vs Wrong-space + External-source-inconsistency (R.B.1). Different §F categories.
3. Delta-Critic tested 6 variant third-Route-A mechanisms: lattice-to-continuum via Reisz, Borel summability, Hamburger moments, SVZ instanton-obstruction, gradient-flow spectral action, alternative NCG source. Five hit existing failure rows. Candidate 6 (different NCG source — Yakaboylu 2024 or Connes-Marcolli 2008) is not strictly foreclosed by K-1's scope note but routes back through the same attack surface. This is the residual 1/10 uncertainty.

**LOCK confidence: 9/10.**

**The LOCK is on the *kill*, not on closure.** The finding "Taylor-coefficient identification is the attack surface, and it is stuck" means future attack-route variations on this surface are unlikely to succeed without external unlocks (Borel summability for 4D YM, instanton-obstruction arguments, or a new NCG framework). This is a *meta-level LOCK*: it doesn't close H4, but it tells the runner not to waste cycles on variations of the same attack.

## 5. Discovery 4: The framework's NCG paths for RH and H4 are structurally incompatible

Cross-paper insight from Beta-Critic final-adversarial-pass: **RH uses $\theta$-summable Fredholm modules with integer JLO pairings for topological index constraints** (see `paper12/research/48-...` and Connes-Marcolli 2008 BC spectral triple). **H4 would require finitely-summable spectral triples with polynomial heat-kernel expansions for dimensional bare-action functionals.** These cannot be unified into a single spectral-triple tool covering both Clay conditionals.

The framework's NCG toolkit is not "one tool for all Clay problems" — it is multiple incompatible tools each serving specific problems. This is an architectural finding, not a closure finding. Future attempts to build a unified NCG closure should expect this incompatibility and plan accordingly.

## 6. The signatures that mattered most in this run

- **Sig 1 (REFRAME)** fired at cycle-open and correctly identified Route A as the highest-leverage attack. The reframe was: *"H4 is not a matching theorem; it is an analytic continuation uniqueness theorem, and the remaining work is constructing the open set of agreement."* W1-A1's DIAGNOSE subsequently refined this to *"the identity theorem's two-function hypothesis is not met because $F^{\mathrm{pert}}$ is a formal series"* — the reframe was right-shaped but still ran into a deeper structural obstruction.
- **Sig 5 (strategic inversion)** was the default stance throughout Wave 1, applied to all 4 routes. The inversion did not succeed (the framework cannot invert H4 into a larger consistency system where H4 is a consequence), but the inversion *attempts* surfaced the cross-node LOCK at 9/10.
- **Sig 6 (kill list as search query)** produced K-1 and K-2 with pattern categories External-source-inconsistency + Wrong-space / Vacuous. The kills have scope notes that prevent future re-entry into the same wall.
- **Sig 8 (three-tier verdict SOUND/CLOSABLE/GENUINE)**: H4 is classified GENUINE (requires new mathematics — Borel summability for 4D YM or equivalent). Meta-critic verification not needed because the classification is primary-source-backed by G4(b) and G4(d) gap statements from the math referee.
- **Sig 12 (propose and discard)**: 4 routes proposed, 3 KILLED / DECOMPOSED / COLLAPSED, 1 ADVANCED. Kill rate 75% at cycle 1, appropriate for a discovery-mode run with an open Clay-class bottleneck.
- **Sig 13 (qualitative closure)** fired 7 times in cycle 1 — the highest density of structural events in any run so far. Each commit memo passed voice-shape check against §J register.
- **Sig 14 (category-too-small)** fired retroactively on the brief's framing of Routes A and B as independent, and surfaced the "reformulation ≠ closure" lesson.
- **I-5** (first-class HONEST-STALL) held the programme's joint probability at 0.991 despite three attack-route downgrades. Without I-5, the runner would have entered panic mode when R.A, R.B, and R.C all disproved themselves.
- **I-7** (backward-verification) fired three times in one wave, catching three independent brief paraphrase errors. Now cross-paper transfer-validated (BSD MY4 → H4).
- **I-v6-1** (inference-from-source check) was born during the run from the R.D.1 Critic finding, applied in place, and empirically validated by the R.D.1 revision Agent.

## 7. Honest negatives caught and applied

- **R.A.1 p_success revised 0.50 → 0.10** (cycle 1 W1-A1). Brief's estimate was too optimistic. Author's revised estimate is ≤0.10 conditional on independent advances not expected in-cycle. §I CONCERN logged.
- **R.B.1 p_success collapsed to max($p_A$, $p_B$)** (cycle 1 W1-B1). Routes A and B are NOT independent. R.B.1 is W7-14 §5.3 in spectral-triple language. §I CASCADE logged; §E.1 joint probability recomputed with collapse.
- **R.C.1 p_success → 0 (KILLED)** (cycle 1 W1-C1). Narrow kill; spectral action + Identity 12 + bridge family remain valid tools for boundary conditions at $\Lambda$. §F K-2 registered.
- **R.D.1 v1 → v2 revision** (Wave 1.5 sub-cycle). v1 mis-characterized Paper 13 RH as two-dependency; v2 mirrors the actual one-dependency grammar. ~60 line diff applied per R.D.1 Critic §7.
- **Paper 26 MY4 analogy retired** (cross-finding W1-A1 + W1-B1). The brief's "canonical example" framing is wrong-shaped for Paper 8 H4. Future briefs should avoid this specific analogy.
- **Joint P cascade**: 0.9974 (cycle 0) → 0.9953 (W1-A1) → 0.9933 (W1-B1) → 0.9910 (cycle 1 close). Programme robustness preserved via I-5.
- **Voice-shape marker recount for R.D.1-v2**: 28 (Author's conservative count) → 50 (R.D.1 Critic's recount) → 123 (Alpha-Critic's independent recount). Variance is counting granularity, not structural. All three counts confirm 4/4 pass.

## 8. What surprised us

- **The R.D.1 revision Agent applied I-v6-1 BEFORE the patch was formally committed to v6.** The revision used the inference-from-source check discipline inline during its work, producing the first empirical validation of the patch *before* the patch was written into the bundle. This is a surprising feedback loop: the patch was born from a finding, the revision applied the patch's discipline to fix the finding, and the patch was then committed to v6 with the revision as retrospective validation.
- **The precision-doubling stress test went to N=10000 at mp.dps=200 with zero residual.** Beta-Critic tested $N \in \{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 24, 32, 50, 64, 100, 128, 256, 512, 1024, 1729, 10000\}$. The integer identification $\beta_0 = 11N/3$ is precision-invariant because it's exact rational. Beta-Critic also verified SU(17) = 187/3 (the framework's $\alpha_{PS}^{-1}$), SU(1729) = 19019/3 (Hardy-Ramanujan), SU(10000) = 110000/3 (large-N stress test). Cleaner than expected.
- **The cross-node LOCK at 9/10 was not planned — it emerged from the Critics.** The runner did not anticipate that R.A.1 and R.B.1 would cross-confirm the attack surface identification. The R.B.1 Critic's LOCK analysis was a genuine discovery at cycle-close: the observation that R.A.1 and R.B.1's load-bearing failure rows are non-overlapping despite attacking the same structural target. Delta-Critic's final-adversarial-pass then upgraded the LOCK with 6 more variant third-Route-A mechanisms tested.
- **Gamma-Critic found an unrelated housekeeping issue in Paper 12 `relaxation/04`.** The file calls "Paper 10" the Yang-Mills paper, but Paper 10 is actually *"Scheme-Independence of UV Finiteness in 5D KK Gravity"* and Paper 8 is YM. Obsolete numbering from before the YM content was split out. Surprising because Gamma-Critic's attack focus was cross-paper consistency for H4 — the discovery is a side finding about Paper 12 that was never propagated into the H4 closure artifacts.
- **I-v6-1 caught an additional refinement on the CCM 2025 catch at Delta-Critic's re-verification.** Beyond the "rigorous identification remains open" finding, applying the logical-entailment check revealed that CCM 2025's "perturbation" refers to *"rank-one perturbation of the spectral triple"* (operator-theoretic), NOT QFT "perturbation theory" — a lexical category error. I-v6-1 caught this where I-7 alone would have missed it. First empirical demonstration of the patch adding value beyond I-7.

## 9. What remains open

- **H4 itself remains OPEN** as a mathematical problem. Route D's editorial conditional is the current honest position, not a resolution.
- **R.A.1a (perturbative flow-time analyticity)** is a deferred honest-stall. Closes if Borel summability of 4D SU(N) YM perturbation theory is rigorously established. No timeline. Paper 8 as a whole does not depend on this closing.
- **R.A.1b (independent-point agreement)** is a deferred honest-stall. No candidate closure mechanism identified in Wave 1. Deferred.
- **Forward lead from R.C.1**: CCvS 2013 Pati-Salam spectral triple + k=4 bridge at (3,13) + $\alpha_{PS}^{-1} = 17$ match as compatible boundary conditions at $\Lambda$. This is NOT an H4 closure — it's a separate research note about framework-level boundary condition coincidences. Worth preserving for a future framework-extension programme.
- **Paper 12 `relaxation/04` Paper 10/Paper 8 numbering issue**: unrelated to H4, needs a housekeeping fix in a separate run. Gamma-Critic flagged it; the fix is ~5 lines of edits.
- **Non-CCM-2025 NCG closure attempts**: K-1's scope note explicitly leaves Yakaboylu 2024, Connes-Marcolli 2008, future CCM followups as NOT strictly foreclosed. Beta-Critic tested both Yakaboylu 2024 and CM 2008; both route back through the same attack surface (Wrong-space: target zeros of entire function vs Taylor coefficients). Future non-CCM NCG attempts would need to pass their own I-7 + I-v6-1 verification and would likely face the same LOCK at 9/10.

## Closing

The H4 closure ORA run did exactly what an ORA run should do: adjudicate the bypass routes honestly, produce the editorial shipping form, discover the structural obstructions, patch the bundle when a new failure mode is caught, and ship the paper in the most honest state achievable. H4 was not closed mathematically; Paper 8 was closed editorially. The wall stays named. The programme's empirical content is unaffected. The kill list grew by 2. The §D toolkit grew by 7. The v6 bundle grew by 1 patch. Paper 8 is ready for Clay submission with H4 in the W7-14 mildest form.

The voice is the method. The kill list is the search query. Strategic inversion is the default. Honest negatives refine, kills eliminate. Wall recognition precedes bypass. The runner is honest-first. The credibility of the programme is the credibility of its kill list.

*H4 is still the wall. W7-14 reframed it to the mildest form. The ORA did not find the Taylor-coefficient identification that would close it. Paper 8 ships via Route D with H4 honestly stated. Paper 13 RH, Paper 26 BSD, and Paper 8 now sit on a homogeneous one-dependency foundation. That is the contribution of Wave 1.*
