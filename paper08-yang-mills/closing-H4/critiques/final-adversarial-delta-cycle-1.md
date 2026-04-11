# Delta-Critic — Final Adversarial Pass, Cycle 1

*Final-adversarial-pass attack on Wave 1's cross-node structural LOCK (9/10), the three I-7 catches, the joint probability calculation, and the I-5 first-class discipline application. Written by Delta-Critic under the H4-closure maximum-effort adversarial brief.*

*Context: This is the wave-close adversarial pass, run against R.B.1 Critic's cross-confirmation LOCK identification. If the LOCK weakens, the Wave 1 close recommendation weakens with it.*

---

## Headline verdicts

| Attack vector | Verdict | Confidence |
|---|---|---:|
| (a) Taylor-coefficient identification LOCK at 9/10 | **VERIFIED at 9/10** (unchanged) | high |
| (k.1) W1-A1 I-7 catch (W7-14 §5.3) | **VERIFIED** | high |
| (k.2) W1-B1 I-7 catch (CCM 2025 p. 28) | **VERIFIED** | high |
| (k.3) W1-C1 I-7 catch (Connes 2007 §5 eq. 24) | **VERIFIED** | high |
| (i) Joint probability $P(A \vee B \vee C \vee D) = 0.9910$ | **VERIFIED** (both symbolic and numeric) | high |
| (j) I-5 first-class discipline application | **VERIFIED** (R.D is a peer, not a safety net) | high |

**Bottom line**: the LOCK holds, the three I-7 catches each hold, the joint P is correct, and I-5 is correctly operational. The Wave-1-close recommendation does not weaken under this adversarial pass.

---

## (a) Taylor-coefficient LOCK at 9/10 — attack and verdict

### Toolkit rows used by R.A.1's block (the failure row, not the input)

From R.A.1-taylor-coefficients.md §§2, 4, 5, and the verification at §6, the load-bearing §D rows for R.A.1's **failure** (not mere input) are:

1. **Formal-power-series divergence** (renormalons; factorial growth of $f_n^{\text{pert}}$): cited as Beneke 1999, 't Hooft 1979, Lipatov 1977. R.A.1 §6 item 2 lists this as textbook. It is **not a §D row** in the master dictionary; it enters as an unstated but textbook-rigorous input that disables the analyticity hypothesis for $F^{\text{pert}}$.
2. **Analyticity identity theorem** (§D row "Analyticity identity theorem", status R, 100%): R.A.1 Step 3 UNIFY tries to apply this theorem; the two-function hypothesis fails because only one side is analytic.
3. **Taylor-coefficient identity** (§D row: status O, 0%): R.A.1 Step 5 COMPUTE concludes this identity IS H4 at the specific $(x,y)$, i.e., it is the target, not a tool.
4. **$F(t)$ rescaled correlator** (§D row: status S, 70%, W7-14 §5.3): enters as an INPUT. R.A.1 uses it but does not fail on it — the analyticity of $F(t)$ is not where the block lives.
5. **Reisz power-counting theorem** (§D row: status R, 100%): enters as a supporting tool for lattice-continuum perturbative agreement; R.A.1 §5.5 Way 2 notes this does not provide non-perturbative to perturbative agreement, so it cannot close Route A.

**Load-bearing failure row for R.A.1**: **formal-power-series divergence of $F^{\text{pert}}$**. This disables the two-function hypothesis of the identity theorem on the PERTURBATIVE side. The failure is a *missing analytic category* on the perturbative side.

### Toolkit rows used by R.B.1's block (the failure row, not the input)

From R.B.1-ccm-ym-analog.md entries #12–#17 + the category-error diagnosis, the load-bearing §D rows for R.B.1's **failure** are:

1. **CCM 2025 spectral triple** (§D row: status R per the original blackboard entry, but the R.B.1 Critic correctly notes this should be downgraded — the "UV asymptotics by construction" statement was brief paraphrase, not primary source): enters as the structural template for the port. R.B.1 uses it for entries #1–#11 which port cleanly; it fails at #12 where the category of target data is wrong.
2. **Carathéodory–Fejér extension** (§D row: status R, 100%): self-adjointness mechanism ports cleanly (this is the "good news") — it is NOT where the block lives; it becomes the Flow-time CF analog at entries #10–#11, and THIS is identical to R.A.1's $F(t)$ analyticity input (shared INPUT, not a failure row).
3. **Hurwitz zero convergence** (mentioned in dictionary #15, not a separate §D row): R.B.1 fails here because YM has no target entire function whose zeros to converge to.
4. **Toeplitz self-adjointness** (absorbed into the CF extension row, §D row: R, 100%): not a failure — it is the part that ports cleanly.
5. **$F(t)$ analyticity** (§D row: status S, 70%): SHARED INPUT with R.A.1. Not a failure row for R.B.1 either.

**Load-bearing failure row for R.B.1**: **category error at dictionary entry #12** — YM target data are Taylor coefficients of an analytic function, but CCM 2025 provides operators whose spectra are zeros of an entire function. This is a *wrong-space category error* on the target-data side.

### Intersection check (load-bearing failure rows)

- **R.A.1 fails on**: formal-series pathology of $F^{\text{pert}}$ (missing analytic category on the perturbative side).
- **R.B.1 fails on**: target-data category error at entry #12 (YM Taylor coefficients ≠ RH zeros).
- **Shared input (not failure)**: $F(t)$ analyticity (W7-14 §5.3, §D row "F(t) rescaled correlator").

**The intersection of load-bearing failure rows is EMPTY.** $F(t)$ analyticity is the shared INPUT but not where either route breaks — both routes USE it correctly (R.A.1 for the non-perturbative side, R.B.1 for the entry #10 CF-analog substitution). The failures are downstream and in non-overlapping objects.

**Routes are genuinely independent at the failure level.** The LOCK claim's "non-overlapping failure rows" condition is satisfied.

### Failure-mode pattern check (§F categories)

- **R.A.1's failure mode**: the Author's R.A.1 research node does not explicitly assign pattern categories (BLOCKED-DECOMPOSED, not KILLED), but the implicit pattern is **"Distributional / Wrong-space / Wrong-category"** — a formal power series is in the wrong category to satisfy the identity theorem's analytic-function hypothesis. The decomposition leaves R.A.1a (Borel-summability-like analyticity) and R.A.1b (independent-point agreement) as open sub-problems.
- **R.B.1's failure mode**: registered as K-1 in §F with pattern categories *"External-source-inconsistency"* + *"Wrong-space"* (RH and YM target data live in different analytic-function categories — entire-function zeros vs Taylor coefficients).

**Pattern-category intersection**:
- R.A.1 has category "Distributional / Wrong-space".
- R.B.1 has category "External-source-inconsistency + Wrong-space".
- **Shared pattern: "Wrong-space"**, but the *specific wrong-space* differs: R.A.1's wrong-space is "formal series vs analytic function" (on the perturbative side of the identity theorem); R.B.1's wrong-space is "Taylor coefficients vs entire function zeros" (on the target-data side of the transposition dictionary).
- These are the SAME ABSTRACT PATTERN ("Wrong-space") applied to DIFFERENT specific objects at different layers of the attack chain. This is a genuine cross-confirmation: both routes found that the target attack surface was in a category that is incompatible with the tool being applied, but for *different* compatibility reasons.

**Verdict on pattern check**: the abstract pattern ("wrong category") is shared, but the specific category-error instances are independent. This is weak evidence the routes are not independent (same abstract failure mode) and strong evidence that the shared abstract pattern is pointing at a real structural feature of the underlying problem. The R.B.1 Critic's "different pattern categories" assertion is slightly overstated — the correct framing is *"different category-error instances that both instantiate the abstract wrong-space pattern"*.

**Net effect on LOCK confidence**: the pattern-category independence is slightly weaker than the R.B.1 Critic claimed, but the failure-row independence is still strong. Net LOCK confidence: **9/10, unchanged**. The 1/10 remaining accounts for the abstract-pattern-sharing concern plus the residual possibility of a novel mechanism (see independent-attempt section below).

### Independent attempt — can I find a third Route A-style closure?

Delta-Critic attempts to construct a third Route A-style closure mechanism that does not hit either failure row.

- **Candidate 1 — Lattice-to-continuum direct match at $t_0 > 0$ (Reisz route)**. Use Reisz power-counting for lattice-perturbative ↔ continuum-perturbative agreement at $t_0$, then interpolate back to $t = 0$ via $F(t)$ analyticity.
  - **Failure**: At $t_0 > 0$, the non-perturbative $F(t_0)$ is lattice-measurable but the perturbative $F^{\text{pert}}(t_0)$ still requires an unresummed perturbative evaluation, which has the same divergence problem. Hits **R.A.1a** (perturbative analyticity). Not escaped.
- **Candidate 2 — Borel transform + Borel summability**. If $F^{\text{pert}}$ is Borel-summable, the Borel sum is analytic in a sector and can be compared with $F$ via the identity theorem applied within that sector.
  - **Failure**: Borel summability of 4D SU(N) pure Yang–Mills is an open problem comparable to H4 itself — explicitly flagged in R.A.1 §5.5 Way 3. Hits **R.A.1a**. Not escaped.
- **Candidate 3 — Hamburger moment problem**. Treat $\{f_n^{\text{pert}}\}$ as a moment sequence and use Stieltjes inversion to reconstruct $F^{\text{pert}}$ as an analytic function.
  - **Failure**: The moment problem requires Hankel positivity of the coefficients; for factorially-growing renormalon series this fails. Even if determinate, Stieltjes inversion gives analyticity in a sector at $\infty$, not at $t = 0$. Hits **R.A.1a**. Not escaped.
- **Candidate 4 — SVZ condensate / instanton-obstruction**. Invoke the Shifman–Vainshtein–Zakharov OPE + instanton condensate framework to bypass the Taylor-coefficient identification.
  - **Failure**: This IS the standard SVZ route, which *assumes* H4 as its starting point. Circular.
- **Candidate 5 — Gradient-flow spectral action** (a second NCG attempt distinct from CCM 2025). Build $(A, H, D)$ with $D^2$ = gradient-flow Laplacian + compute Seeley–DeWitt $a_4$.
  - **Failure**: This is R.C (KILLED at K-2). The spectral action is classical/bare at $\Lambda$, not running. Hits **R.C kill basis**. Not escaped.
- **Candidate 6 — Transpose from a different NCG source** (Yakaboylu 2024, Connes–Marcolli 2008, or other).
  - **Status**: The K-1 scope note explicitly leaves this open: *"A future NCG-based closure attempt from a different primary source would need to pass its own I-7 backward-verification and would not be auto-killed by K-1."* A new NCG source would still need to provide a mechanism that identifies the Taylor coefficients of $F$ at $t = 0$, which is the attack surface the LOCK is on. Any such mechanism would need to provide analyticity (or a stand-in) for the perturbative side, or identify a new target-data category. Both are hard.
  - **Verdict**: Not STRICTLY foreclosed by the LOCK, but structurally routed back through the same attack surface. Counts as residual 1/10 uncertainty, not as a broken LOCK.

**Independent-attempt verdict**: Delta-Critic cannot construct a Route A-style closure mechanism that escapes both failure rows. Candidates 1–5 all hit one of R.A.1a, R.A.1b, or K-2. Candidate 6 is not foreclosed but is routed through the same attack surface the LOCK is on.

### LOCK verdict (attack vector a)

**VERIFIED at 9/10 (unchanged from R.B.1 Critic's original assessment).**

- Load-bearing failure rows: **non-overlapping** (R.A.1 fails on perturbative-side analyticity category; R.B.1 fails on target-data entire-function-vs-Taylor-coefficient category). The shared $F(t)$ analyticity is an INPUT, not a failure point.
- Pattern categories: **same abstract pattern (wrong-space) applied to different specific objects at different layers.** This is slight evidence of dependence but strong evidence the routes cross-confirm a real structural feature of the underlying problem.
- Independent attempt: **no third Route A-style mechanism escapes both failure rows** (within my search budget). Candidate 6 (different NCG source) remains as residual 1/10 uncertainty.

The LOCK holds. The statement "Taylor-coefficient identification is the attack surface, and it is genuinely stuck for any Route A-style closure mechanism" is at **9/10 confidence**. The 1/10 uncertainty is dominated by the possibility of a new NCG source that provides a closure mechanism not hit by the current failure rows — this is the same "K-1 scope note" uncertainty the R.B.1 Critic flagged.

---

## (k.1) W1-A1 I-7 catch on W7-14 §5.3 — re-verification

### Independent primary-source read

Delta-Critic read `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md` lines 388–414 directly (via Read tool, independent of the Author's block-quote).

**Primary source verbatim** (W7-14 §5.3 lines 388–413):

> ### 5.3 Analyticity provides a rigorous bridge
>
> The analyticity of $F(t)$ in the complex flow-time plane (W5-10, Step 2; radius $r_t > 0$ independent of the Balaban step $k$ and the bare-scale index $K$) implies that the small-flow-time expansion is not merely asymptotic but **convergent**. This upgrades the status of the perturbative expansion from a formal series to an actual Taylor series with a positive radius of convergence. In particular:
>
> - The perturbative coefficients of $F(t) = F(0) + F'(0)\,t + \tfrac{1}{2}F''(0)\,t^2 + \cdots$ are the derivatives of a single analytic function, not independent perturbative computations.
> - The remainder $R_n(t) = F(t) - \sum_{k=0}^{n} F^{(k)}(0)\,t^k/k!$ satisfies $|R_n(t)| \leq M_F\,(|t|/r_t)^{n+1}/(1 - |t|/r_t)$, a rigorous Cauchy remainder bound.
> - The non-perturbative value $F(0)$ equals the sum of the convergent series, by definition of analyticity.
>
> What H4 asks, in this language, is whether the Taylor coefficients $F^{(k)}(0)$ are computable by the Feynman-diagrammatic perturbative rules. This is a statement about the Taylor coefficients of an analytic function — a more accessible question than the traditional formulation of H4, which asks about the asymptotic behavior of a non-perturbative distribution.

**Author's block-quote** (R.A.1-taylor-coefficients.md lines 173–179, prose-normalized from the LaTeX-inline-math):

> "The analyticity of F(t) in the complex flow-time plane (W5-10, Step 2; radius r_t > 0 independent of the Balaban step k and the bare-scale index K) implies that the small-flow-time expansion is not merely asymptotic but **convergent**. This upgrades the status of the perturbative expansion from a formal series to an actual Taylor series with a positive radius of convergence. In particular:
> - The perturbative coefficients of F(t) = F(0) + F'(0) t + (1/2) F''(0) t^2 + ⋯ are the derivatives of a single analytic function, not independent perturbative computations.
> - The remainder R_n(t) = F(t) − Σ_{k=0}^n F^{(k)}(0) t^k/k! satisfies |R_n(t)| ≤ M_F (|t|/r_t)^{n+1}/(1 − |t|/r_t), a rigorous Cauchy remainder bound.
> - The non-perturbative value F(0) equals the sum of the convergent series, by definition of analyticity.
>
> What H4 asks, in this language, is whether the Taylor coefficients F^{(k)}(0) are computable by the Feynman-diagrammatic perturbative rules. This is a statement about the Taylor coefficients of an analytic function — a more accessible question than the traditional formulation of H4, which asks about the asymptotic behavior of a non-perturbative distribution."

**Byte-for-byte comparison**: Author's quote matches primary source modulo standard plaintext-normalization: LaTeX inline-math stripping, `\tfrac{1}{2}` → "(1/2)", `\cdots` → "⋯", em-dash `---` → "—". No content drift.

### Logical entailment check (I-v6-1 discipline)

Under the v6 patch I-v6-1 (inference-from-source-check), the quote must logically entail the claim: *"§5.3 explicitly says H4 remains open after the reformulation."*

- The primary source says H4 is reformulated as *"whether the Taylor coefficients $F^{(k)}(0)$ are computable by the Feynman-diagrammatic perturbative rules"*.
- This is phrased as a QUESTION ("is whether ... are computable"), which logically entails "not yet answered".
- The primary source calls it *"a more accessible question than the traditional formulation of H4"*.
- "More accessible question" logically entails "still a question, not a resolved answer". The comparative "more accessible" is with respect to the original H4 question, not with respect to "closure".
- The primary source frames this as a **reformulation** (from "asymptotic behavior of a non-perturbative distribution" to "Taylor coefficients of an analytic function"), not as a **resolution**.

**Entailment valid**: "More accessible question" + "What H4 asks, in this language, is whether..." ⇒ "§5.3 is a reformulation, not a resolution of H4". The Author's conclusion that "H4 remains open after the reformulation" is **logically entailed by the verbatim quote**. The I-v6-1 check passes.

**Minor nuance**: The primary source does not literally use the phrase "H4 remains open" — it says "a more accessible question". The Author's conclusion drops one level of logical inference (from "more accessible question" to "still a question" to "H4 still open"). This is a valid inference chain, but not a direct quotation. In the v6 I-v6-1 framing, this is an **inference**, not a **paraphrase** — and the inference is valid.

### I-7 catch verdict (k.1)

**VERIFIED**. The Author's block-quote is byte-accurate against the primary source (lines 388–413), and the logical entailment from the quoted text to the conclusion ("H4 remains open after the reformulation") is valid under the I-v6-1 discipline. The R.A.1 Critic's independent verification agrees (Critic's sub-step 5 in `R.A.1-cycle-1.md` lines 100–128).

---

## (k.2) W1-B1 I-7 catch on CCM 2025 — re-verification

### Independent primary-source read

Delta-Critic used `pdftotext -layout` on `/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/sources/ccm-zeta-spectral-triples-2025.pdf` and grepped for "remaining obstacle | Justifying rigorously | main remaining".

**Primary source verbatim** (CCM 2025, PDF page 28, §7 Outlook, lines 1566–1567 of extracted text):

> "We refer to [4], Section 3, for the motivation behind the formula for $k_\lambda$ and the numerical evidence showing that it gives an approximation of a scalar multiple of $\xi_\lambda$. **Justifying rigorously this step is the main remaining obstacle to our approach to RH.**"

**Page verification**: PDF page 28 contains the "§7. Outlook" section header in the PDF footer at line 1570 of extracted text (immediately below the verbatim quote). The quote appears on PDF page 28 at the top of §7 Outlook — the blackboard's "CCM 2025 p. 28 verbatim" citation is accurate.

**R.B.1 Author's quote** (R.B.1-ccm-ym-analog.md line 184): *"CCM state verbatim (p. 28): 'Justifying rigorously this step is the main remaining obstacle to our approach to RH.'"*

**Byte-for-byte match**: Author's quote matches primary source exactly. No content drift.

### Logical entailment check (I-v6-1 discipline)

Does the verbatim quote entail the claim: *"CCM 2025 does NOT provide UV asymptotics by construction"* (the key Wave 1 finding)?

- The quote identifies "Justifying rigorously this step" as the "main remaining obstacle".
- Context: "this step" is the convergence $k_\lambda \to$ approximation of $\xi_\lambda$, which is the step that identifies the operator's eigenvalues with Riemann zeros (via the conjectured convergence of $\widehat{k}_\lambda$ to $\Xi$ plus Hurwitz).
- If the rigorous justification is the "main remaining obstacle", then the operator-to-zeros identification is **open inside CCM 2025** — the paper does not provide a proof, only numerical evidence plus an educated-guess formula.
- An operator whose rigorous spectral identification with Riemann zeros is still open cannot be an operator whose "UV asymptotics match perturbation theory by construction" — because the "match by construction" claim would require the identification to be rigorous, not numerically conjectural.
- **Furthermore**, the word "perturbation" in CCM 2025 refers to **"rank-one perturbation"** of the spectral triple (an operator-theoretic move, CCM 2025 §5.4 and Lemma 5.4), NOT to QFT "perturbation theory" in the Feynman-diagrammatic sense. The brief's phrase "UV asymptotics match perturbation theory" conflates these two meanings of "perturbation".

**Entailment valid**: "Justifying rigorously this step is the main remaining obstacle" ⇒ "rigorous operator-to-zeros identification is OPEN" ⇒ "CCM 2025 does NOT provide 'UV asymptotics match perturbation theory by construction' for ANY target data". The I-v6-1 check passes.

**Strong additional evidence**: The "rank-one perturbation" vs "QFT perturbation theory" distinction is a lexical category error, catchable on any careful read of CCM 2025 §5.4 and Lemma 5.4 — this is a second independent reason the brief's paraphrase cannot be in the primary source.

### I-7 catch verdict (k.2)

**VERIFIED**. The Author's quote is byte-accurate against the primary source (CCM 2025 PDF p. 28, §7 Outlook). The quote is on the correct page. The logical entailment from the quote to the conclusion (CCM 2025 does NOT provide UV asymptotics by construction) is valid under I-v6-1. The R.B.1 Critic's independent verification triple-confirms (Critic's §1 verbatim check in `R.B.1-cycle-1.md` lines 51–83).

---

## (k.3) W1-C1 I-7 catch on Connes 2007 — re-verification

### Independent primary-source read

Delta-Critic WebFetched `https://seminaire-poincare.pages.math.cnrs.fr/connes2.pdf` (WebFetch returned binary, but the framework's cache saved the PDF to a local temp path, which Delta-Critic then extracted via `pdftotext -layout`).

**Primary source verbatim** (Connes 2007, Séminaire Poincaré X, §5 "The spectral action principle", eq. (24) at lines 426–434 of extracted text; page header at line 400 shows *"Vol. X, 2007 Noncommutative geometry and the spectral model of space-time 185"* — so eq. (24) is on p. 185):

> "data are available in localized form anywhere, and are (asymptotically) of the form (23) when they are of the additive form
>
> $\text{Trace}(f(D/\Lambda))$, (24)
>
> where $D$ is the Dirac operator and $f$ is a positive even function of the real variable while the parameter $\Lambda$ fixes the mass scale. **The spectral action principle asserts that the fundamental action functional $S$ that allows to compare different geometric spaces at the classical level and is used in the functional integration to go to the quantum level**, is itself of the form (24). The detailed form of the function $f$ is largely irrelevant since the spectral action (24) can be expanded in decreasing powers of the scale $\Lambda$..."

**R.C.1 Author's quote** (R.C.1-spectral-action.md line 73, reproduced via §5.5 Way 1 backward-verification):

> "The spectral action principle asserts that the fundamental action functional $S$ that allows to compare different geometric spaces **at the classical level** and is used in the functional integration **to go to the quantum level**, is itself of the form ..."

**Byte-for-byte match**: Author's quote matches primary source exactly. The Author's ALL-CAPS-then-bolded emphasis on "at the classical level" is transparent editorial marking, flagged as such by the Author. No content drift.

### Logical entailment check (I-v6-1 discipline)

Does the verbatim quote entail the claim: *"spectral action is bare/classical, not running"*?

- The quote explicitly places the fundamental action functional "**at the classical level**".
- The quote then states the functional is "used in the functional integration **to go to the quantum level**" — i.e., the spectral action is the STARTING POINT for the quantization process, not the result.
- Action functionals used as integrands of functional integrals are *by definition* "bare" / "classical" — they are actions at a reference scale $\Lambda$ (mentioned explicitly: "the parameter $\Lambda$ fixes the mass scale"), before the functional integration has been performed.
- "Running" (in the renormalization-group sense) is a quantum-level phenomenon that emerges from the functional integration, not from the action functional itself.
- **Therefore**: "at the classical level" + "used to go to the quantum level" + "$\Lambda$ fixes the mass scale" ⇒ "spectral action is a classical/bare action at $\Lambda$" ⇒ "spectral action is NOT a running coupling".

**Entailment valid**: The I-v6-1 check passes cleanly. The Author's conclusion that Route C's "running $g(\mu)$ from $a_4$" is a category error between *bare counter-term* and *running flow* is a direct logical consequence of the verbatim quote plus one textbook fact (running is a quantum RG phenomenon, not a classical-action phenomenon).

**Cross-evidence**: Vassilevich 2003 eq. (4.34) independently confirms the same thing from the computational side — $a_4$ is the coefficient of the one-loop UV divergence in zeta regularization, which is a counter-term coefficient at the bare level. The R.C.1 Critic's independent WebFetch + pdftotext of Vassilevich confirmed this at byte-for-byte level (Critic's §1.2 in `R.C.1-cycle-1.md`).

### I-7 catch verdict (k.3)

**VERIFIED**. The Author's quote is byte-accurate against Connes 2007 §5 eq. (24) (p. 185, Séminaire Poincaré X). The logical entailment from the quote ("at the classical level" + "used to go to the quantum level" + $\Lambda$ fixes the mass scale) to the conclusion (spectral action is bare/classical, not running) is valid under I-v6-1. The R.C.1 Critic's independent verification at byte-for-byte level triple-confirms (Critic's §1.1 in `R.C.1-cycle-1.md` lines 18–46).

---

## (i) Joint probability recomputation

### Symbolic recomputation

Given:
- R.A = 0.10
- R.B = collapsed into R.A (not independent; effective contribution is $\max(p_A, p_B) = p_A = 0.10$)
- R.C = 0 (KILLED)
- R.D = 0.99 (first-class peer per I-5)

**Interpretation 1 — collapse as fusion**: Routes A and B share a closure chain (both require the same Taylor-coefficient identification of $F^{(k)}(0) = f_k^{\text{pert}}$), so the joint event "A OR B closes" collapses to the single event "the Taylor-coefficient identification closes", with probability $p_{A \lor B} = 0.10$.

Then:
$$P(A \lor B \lor C \lor D) = 1 - P(\text{all fail})$$

Since A, B, and D are the remaining routes (C has p = 0, so $1 - p_C = 1$ and C contributes 0 to the failure product), and A-B are treated as one collapsed route with probability 0.10:

$$P(\text{all fail}) = (1 - p_{A \lor B})(1 - p_C)(1 - p_D) = (1 - 0.10)(1 - 0)(1 - 0.99)$$
$$= 0.90 \times 1 \times 0.01 = 0.009$$

$$P(A \lor B \lor C \lor D) = 1 - 0.009 = \mathbf{0.9910}$$

**Interpretation 2 — treating B's independent contribution as 0**: if instead we treat R.B as having $p_B = 0$ independently (because the route does not close on its own), with R.A at 0.10:

$$P(A \lor B \lor C \lor D) = 1 - (1 - 0.10)(1 - 0)(1 - 0)(1 - 0.99) = 1 - 0.90 \times 1 \times 1 \times 0.01 = 1 - 0.009 = \mathbf{0.9910}$$

**Both interpretations give $P = 0.9910$.** The collapse is handled consistently.

### Numerical recomputation

```
p_A = 0.10
p_B = collapsed (= 0 independent)
p_C = 0.00
p_D = 0.99

(1 - p_A) = 0.90
(1 - p_B) = 1.00
(1 - p_C) = 1.00
(1 - p_D) = 0.01

product = 0.90 * 1.00 * 1.00 * 0.01 = 0.0090

P(at least one closes) = 1 - 0.0090 = 0.9910
```

Numerical result: $P = 0.9910$. **Blackboard claim is correct.**

### Sanity checks

1. **Mathematical closure** $P(A \vee B \vee C) = 1 - (1 - 0.10)(1 - 0)(1 - 0) = 1 - 0.90 = \mathbf{0.10}$. Blackboard states this as 0.10 — correct.
2. **Without I-5 (R.D as safety net with reduced weight)**: if R.D's contribution were reduced, say to 0.50 as a "fallback", the joint would be $1 - (0.90)(1)(1)(0.50) = 1 - 0.45 = 0.55$ — a catastrophic drop. The full 0.99 contribution of R.D is what produces the 0.991 joint; this is the operational meaning of I-5 first-class discipline.
3. **Collapse arithmetic sanity**: the choice to collapse R.A and R.B (vs treating them as independent with $p_B$ at some non-zero value) can only DECREASE the joint probability. The current choice (collapse → $p_{A \lor B} = 0.10$) is the conservative / honest choice.

### Joint P verdict (i)

**VERIFIED** both symbolically and numerically. $P(A \vee B \vee C \vee D) = 0.9910$ is correct given the stated R.A = 0.10, R.B collapsed, R.C = 0, R.D = 0.99 inputs.

---

## (j) I-5 first-class discipline application

### Check 1 — Parallel dispatch of R.D in cycle 1

From blackboard §K lines 240 and 145: *"R.D.1 dispatches **in parallel** with R.A.1 / R.B.1 / R.C.1 — not waiting for A/B/C to fail. This is I-5 first-class discipline operational: the HONEST-STALL subtree has its own p ≈ 0.99 in §E.1 and is a peer option from cycle 1, not a post-failure fallback."*

**Verified**: R.D.1 was dispatched in Wave 1 as slot W1-D1 in parallel with W1-A1, W1-B1, W1-C1 (blackboard §K Plan-primitive dispatch table, line 234 onwards). This is the operational signature of I-5 first-class discipline.

### Check 2 — R.D's joint probability contribution is 0.99, not reduced

From §E.1 final Wave 1 state (line 539): *"R.D (editorial HONEST-STALL, first-class) | 0.99 | 0.99 | 0.99 | **0.99** | ADVANCED"*.

From the joint calculation: R.D enters the joint with the full $0.99$ peer weight, not a reduced "fallback" weight. $1 - p_D = 0.01$ is the term that dominates the product.

**Verified**: R.D's joint contribution is 0.99, treated as a peer.

### Check 3 — R.D.1 has its own node file, its own Critic, its own §D proposal

- Node file: `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/closing-H4/nodes/R.D.1-abstract-conditional.md`
- Critic file: `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/closing-H4/critiques/R.D.1-cycle-1.md`
- Wave 1 roll-up (blackboard line 481): R.D.1 appears with its own verdict **ADVANCED**, its own generative step (Step 3 UNIFY), and its own I-7 catch (Paper 13 RH/BSD MY4 conditional grammars verified).

**Verified**: R.D is treated as a first-class peer throughout Wave 1. It has a full node/critic pipeline, a full Wave 1 return, a full §D proposal (PCGT template), and its verdict (ADVANCED) is a genuine closure output.

### Check 4 — R.D.1 outputs are load-bearing for Paper 8 ship decision

From blackboard §K line 448: *"Paper 8 now has a ship-ready standing form regardless of whether Wave 2 closes H4 mathematically."*

The R.D.1 editorial artifact (4 draft pieces: abstract conditional, consolidated Theorem 1, §15 Scope section, §L.7.3 cross-reference block) is directly insertable into the preprint. This is a *completed* closure output, not a "if all else fails, we'll fall back to this".

**Verified**: R.D.1's Wave 1 output is a shipping deliverable, not a safety net.

### I-5 verdict (j)

**VERIFIED**. R.D is treated as a first-class peer throughout cycle 1:
- Parallel dispatch in Wave 1 (not post-failure).
- Full 0.99 weight in joint probability (not reduced fallback weight).
- Full node/critic/§D pipeline.
- ADVANCED verdict with shipping-ready artifact.
- Joint probability robustness (0.991) is structurally dependent on I-5 — if R.D were reduced to "fallback" treatment, the joint would drop from 0.991 to somewhere between 0.10 and 0.55 depending on weighting.

**I-5 is operationally load-bearing and operationally correct.** The R.D.1 Critic verdict was WEAKENED (for a one-dependency-vs-two-dependency template claim that requires a ~60-line revision), but this is a within-node refinement, not a demotion of R.D to fallback status. The Wave 1 roll-up correctly keeps R.D's Wave-1 outcome as ADVANCED (pending the ~60-line revision).

---

## Summary (≤200 words)

**LOCK at 9/10 VERIFIED.** R.A.1 and R.B.1 fail on non-overlapping load-bearing rows (perturbative-side analyticity category vs target-data entire-function-vs-Taylor-coefficient category). Shared $F(t)$ analyticity is INPUT, not failure point. Pattern categories share the abstract "wrong-space" pattern at different layers — slight evidence of dependence but strong cross-confirmation of the underlying structural obstruction. Delta-Critic's independent attempt to construct a third Route A-style closure fails on all six candidates (Reisz, Borel, moments, SVZ, gradient-flow spectral action, alternative NCG source). The residual 1/10 is the K-1 scope-note uncertainty on a new NCG source.

**Three I-7 catches VERIFIED.** Byte-for-byte primary-source check confirms all three: W7-14 §5.3 at lines 388–413 (W1-A1); CCM 2025 PDF p. 28 §7 Outlook (W1-B1); Connes 2007 §5 eq. (24) at p. 185 (W1-C1). Logical entailment from quoted text to conclusion is valid under the v6 I-v6-1 inference-from-source discipline in all three cases.

**Joint $P = 0.9910$ VERIFIED** symbolically and numerically.

**I-5 first-class discipline VERIFIED operational**: parallel dispatch, full 0.99 weight, full pipeline, shipping-ready artifact, structurally load-bearing for the 0.991 joint.

**Wave-1-close recommendation does not weaken under this adversarial pass.**
