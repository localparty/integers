# R.A.1 — Taylor-coefficient identification (W1-A1 Author output)

*Author: W1-A1 (Author spawn under ORA v6 bundle)*
*Node: R.A.1 — Taylor coefficients of F(t) at t=0 vs Luscher / Harlander-Neumann / Artz perturbative coefficients, then analyticity-uniqueness via the identity theorem*
*Route: A (W7-14 §5.3 analyticity reformulation)*
*Written: 2026-04-11*
*Effort: max (interleaved extended thinking throughout)*

---

## Direction

R.A.1 asks me to (a) extract the Taylor coefficients `{F^{(n)}(0)/n!}` of the analytic rescaled correlator `F(t) := S_{2,t}^c(x,y)/c_1(t)^2` at `t = 0` from the W5-10 Step 2 analytic continuation; (b) compare to the Feynman-diagrammatic perturbative coefficients `{f_n^pert}` from Luscher 2010 + Harlander–Neumann 2016 + Artz et al. 2019 (3-loop); (c) assemble the analyticity-uniqueness argument via the identity theorem of complex analysis, by constructing an open neighborhood `U ∋ 0` where the non-perturbative and perturbative expansions demonstrably agree, so that the identity theorem closes the rest. The runner's REFRAME is that this is an **analytic continuation uniqueness theorem**, not a matching theorem; my job is to see whether this reframing actually closes H4 or merely shifts it.

My honest reading after executing the 6-step loop: Route A is a **reformulation of H4, not a closure**. The obstruction is structural, not a local technical gap; I recommend BLOCKED-DECOMPOSED rather than a dishonest ADVANCE.

## Framework tools used

**Always-read (full end-to-end)**:
- `paper12/research/214-the-method-six-patterns.md` (Six Patterns method loop — 339 lines)
- `paper12/27-anchor-document.md` (CBB anchor + SP1–SP5 + voice canon — 426 lines)
- `paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md` (seven-anchor strategy — selective read §1–§6)

**Load-bearing for R.A.1 (selective-read per I-9)**:
- `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md` §§1–5 (full, plus §5.3 verbatim block-quote for backward-verification)
- `paper08-yang-mills/gradient-flow-attack-plan/research/W7-15-ope-leading.md` §§1–7 (full)
- `paper08-yang-mills/gradient-flow-attack-plan/research/W5-10-cauchy-estimate-and-extraction.md` Part I Steps 1–6 + Part II Lemma 3.8 (backward-verification of analyticity claim)
- `paper08-yang-mills/gradient-flow-attack-plan/research/W1-05-analyticity-in-t.md` §§1–5 (composition theorem for `F(t)` analyticity, Lemma 3.1 + removable singularity extension)
- `paper08-yang-mills/preprint/sections/L-clay-conjectures.md` §L.6.1–L.7.2 (Conjecture L.2 + H4 statement)
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4b-af-short-distance-match.md` (full — formal G4(b) statement)
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4d-operator-product-expansion.md` (full — formal G4(d) statement)
- `paper08-yang-mills/preprint/PROOF-CHAIN.md` (full — 18-step chain context)
- `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` §§1–5 (canonical ORA-produced structural bypass — the shape Route A is trying to mirror)
- `paper08-yang-mills/closing-H4/blackboard.md` §§A–§J (runner context, toolkit, voice canon)

**External papers NOT WebFetched** (reason: primary-source numerical values for `f_n^pert` are not load-bearing at the bottleneck I identify — see §Verdict; backward-verification of W5-10 §5.3 is the I-7-mandated verification and was done against the W5-10 and W1-05 framework files directly):
- Luscher JHEP 08 (2010) 071 — cited through W7-14 §1.2, §2.2
- Harlander–Neumann JHEP 06 (2016) 161 — cited through W7-14 §1.2, §2.2
- Artz et al. JHEP 06 (2019) 121 — cited through W7-14 §1.2
- Zoller–Chetyrkin JHEP 12 (2012) 119; JHEP 10 (2014) 169 — cited through W7-15 §4.2

## Research

### Step 1 — DIAGNOSE (Pattern 6: projection produces apparent pathology)

**In one sentence**: H4 is hard in the current framing because it compares two objects — a non-perturbative Schwinger function `S_2^ren(x,y)` constructed by the Balaban polymer integral and a perturbative OPE prediction `C_N |x|^{-8}(log)^{-2}` built from finite-order Feynman diagrams — that live in different mathematical categories (tempered distributions vs formal power series); the phenomenon in a fuller description is that **both are the `t → 0` limit of the single analytic function `F(t) = S_{2,t}^c/c_1(t)^2` but accessed via different mechanisms, so the apparent H4 gap is a projection artifact of the standard framing**.

**Engaging the runner's REFRAME**: The runner says Route A is "not a matching theorem; it is an analytic continuation uniqueness theorem applied to a specific pair of analytic functions, and the remaining work is constructing the open set of agreement where the identity theorem of complex analysis closes the rest." I accept the first half (H4 is not a matching theorem); I interrogate the second half (the open set of agreement) in Steps 4–5 below. The interrogation is load-bearing, because the identity theorem requires *two analytic functions*, and whether `F^pert(t)` is actually an analytic function (rather than a formal power series) is exactly the question.

**Pattern 6 application**: The "apparent pathology" is that H4 appears intractable (the referee writes "comparable in difficulty to constructing the theory itself"). The projection artifact is the CHOICE of asymptotic category — treating `S_2^ren` as a distribution and the perturbative series as a formal power series makes the comparison look like a construction problem. Lifting to the flow-time variable `t ∈ ℂ` with `F(t)` analytic on `|t| < r_t` makes BOTH objects into candidate-analytic-functions on a common disk — but only if we can also make `F^pert(t)` actually analytic, which is the crux.

**The DIAGNOSE output**: The H4 obstruction lives in the **asymptotic category of the perturbative side**, not in the non-perturbative side. The non-perturbative side `F(t)` has been upgraded to an analytic function by W5-10 Step 2 (this is rigorous). The perturbative side `F^pert(t)` has NOT been upgraded — it remains a formal power series whose coefficients are computed by Luscher–Harlander–Artz. For the identity theorem to apply, we need `F^pert` to be an analytic function on some open disk, not merely a formal power series. **This is where Route A's "construct the open set of agreement" step is actually doing work, and it is the step that breaks.**

### Step 2 — REINTERPRET (Pattern 1: geometric reinterpretation)

The space in which the difficulty dissolves (partially) is the **complex flow-time disk** `D_{r_t} = {t ∈ ℂ : |t| < r_t}` with `r_t > 0` the `(k,K)`-independent analyticity radius established in W5-10 Step 2 + W1-05 Lemma 3.1.

In this space, three things become true:

1. `F(t)` is a holomorphic function on `D_{r_t}` with `F(0) < ∞`. It has a convergent Taylor series `F(t) = Σ_{n≥0} a_n t^n` with `|a_n| ≤ M_F / r_t^n` (Cauchy coefficient bound, W1-05 Corollary 5.1).
2. The `(k,K)`-uniformity of `r_t` means the statement is stable under the Balaban RG and the continuum limit `a → 0`. The statement is not a finite-lattice artefact.
3. The Cauchy estimate `|F(t) - F(t')| ≤ L|t - t'|` on `[0, r_t)` gives Lipschitz regularity (stronger than Hölder), which allows the Moore–Osgood interchange for the double limit `(a, t) → (0, 0)` (W5-10 Step 5).

**The geometric reinterpretation succeeds at the level of `F(t)`**, moving us from "a tempered distribution at coincident points" to "an analytic function with convergent Taylor series". This is Pattern 1 landing.

**The reinterpretation DOES NOT succeed at the level of `F^pert(t)`**. The perturbative coefficients `f_n^pert` are computed order-by-order using Luscher–Weisz 2011 Feynman rules at fixed `t > 0`, and each individual `f_n^pert` is a finite number. But the formal series `Σ_n f_n^pert t^n` is **not known to converge** as an analytic function on any open disk, and in fact the known asymptotic behavior of perturbative series in 4D Yang–Mills (`n! b_0^n` growth from instantons/renormalons; see Beneke, *Phys. Rep.* 317 (1999) 1, for the review) suggests it is **divergent as a power series in the coupling `g^2`**.

There is a subtlety: the perturbative expansion in `t` is different from the perturbative expansion in `g^2`, because the running coupling `ḡ^2(q) = 1/(2b_0 log(q/Λ))` at `q = 1/√(8t)` ties the two expansions together non-trivially (logs of `t` enter). The small-`t` asymptotic form of `c_1(t)` in W7-14 eq. (2.2) is `c_1(t) ~ t^{-2}(log(1/tΛ^2))^{-1}`, which has a BRANCH CUT along the negative real axis of `t` from the logarithm. This branch cut is **incompatible with `c_1(t)` being analytic at `t = 0`**.

But `F(t) = S_{2,t}^c / c_1(t)^2` is claimed analytic by W5-10 Step 2. This apparent tension is resolved by observing that the analyticity claim is about the *composition* `t → V_t → S_k^eff[V_t] → correlator`, and the logarithmic structure of `c_1(t)` is an artifact of the PERTURBATIVE expansion, not the non-perturbative definition. In the non-perturbative construction, `c_1(t)` is a specific scalar function built from free-field heat-kernel Wick contractions at `t > 0`, and the log structure arises only when the result is re-expressed in terms of the running coupling at scale `1/√(8t)`. The Balaban composition argument (W1-05 Lemma 3.1) bypasses this re-expression.

**Net**: The geometric reinterpretation gives us an analytic `F(t)` but leaves `F^pert(t)` as a formal object. The identity theorem's first hypothesis — that both sides are analytic — is not met.

### Step 3 — UNIFY (Pattern 2: holonomy correspondence → template identification)

**Canonical template (from §D of the blackboard)**: *Analyticity identity theorem*, Ahlfors Ch. 6 / Rudin *Real and Complex Analysis* Ch. 10 — "two analytic functions agreeing on an open subset of their common connected domain of analyticity are equal everywhere on that domain."

**Precise statement** (for the R.A.1 context): Let `U ⊂ ℂ` be a connected open set containing `0`. Let `f, g : U → ℂ` be holomorphic on `U`. If there exists `S ⊂ U` with an accumulation point in `U` such that `f = g` on `S`, then `f = g` on all of `U`.

**Application template for Route A**: Set `U = D_{r_t}` (the analyticity disk), `f = F` (non-perturbative, analytic by W5-10 Step 2), `g = F^pert` (perturbative), and `S = {t_0}` or a neighborhood where agreement can be demonstrated. Then `F ≡ F^pert` on `U`.

**Obstruction A (the one I flagged in Step 2)**: The template requires `g = F^pert` to be analytic on `U`. The existence of `F^pert` as an analytic function on a disk containing `0` is not established by the Feynman-diagrammatic computation — each `f_n^pert` is a finite number but the formal series may not converge, and the complex-analytic extension is not automatic.

**Obstruction B (the agreement set)**: Even granting `F^pert` is analytic on `U`, the template requires `S ⊂ U` with an accumulation point where `F = F^pert`. The NATURAL candidate is `S = {0}` (agreement at `t = 0`), but `{0}` has no accumulation point in itself — a single point is a discrete set, not a set with a limit point — so this case of the identity theorem does not apply. The stronger form of the theorem (equality of Taylor coefficients at a single point → equality on the connected component) requires the additional input that **all** Taylor coefficients agree, which is exactly the problem we're trying to solve.

**Obstruction C (independent-computation requirement)**: For a true application of the identity theorem, we need `F(t_0) = F^pert(t_0)` for some specific `t_0 ∈ U`, **demonstrated by an independent computation that does NOT itself invoke H4**. The candidates for such an independent computation:

- **Tree level (`g = 0`)**: Both sides reduce to the free-field Wick contraction of `Tr(F^2)(x) Tr(F^2)(0)`, giving `C_N/|x|^8`. But tree level is `O(g^0)`, a single point in the coupling expansion, and the tree-level expression is *not* a value of `F(t_0)` at a specific `t_0 > 0` — it's a value at `g = 0`. The identity theorem requires equality of the full theory at a specific `t_0`, not equality of a truncation.
- **Lattice perturbative at small `t`**: Reisz power counting guarantees lattice PT = continuum PT at each finite order in the loop expansion. But this is a purely perturbative identity; it does not relate the non-perturbative `F(t_0)` to the perturbative `F^pert(t_0)`.
- **Large `t` / IR regime**: At `t » Λ^{-2}`, the non-perturbative correlator decays exponentially at rate `Δ_∞` (mass gap) while the perturbative prediction diverges or misbehaves (the running coupling enters the strong-coupling regime). They disagree, but `|t| > r_t` is outside the analyticity disk anyway.
- **Super-renormalizable analogue (`φ^4_3`)**: Proved by Glimm–Jaffe / Magnen–Rivasseau–Seneor. But 4D Yang–Mills is not super-renormalizable; the analogous theorem for 4D YM is exactly H4.

None of these gives an independent `t_0` where `F(t_0) = F^pert(t_0)` can be demonstrated without circularity.

**Unification verdict**: The template IS the identity theorem, and the invocation structure is correct, but TWO out of THREE premises (analyticity of `F^pert`; independent agreement at a specific point) are not met. Route A's closure mechanism candidate is structurally incomplete.

### Step 4 — LOCK (Pattern 4: topological rigidity) + DECOMPOSITION

**The invariant that protects the result** (if it were achievable): "Uniqueness of analytic continuation." Formally: the Taylor series of an analytic function on a connected domain uniquely determines the function throughout the domain. Equivalently: the sheaf of holomorphic functions on a connected open set `U ⊂ ℂ` is a principal sheaf, so `H^0(U, 𝒪_U)` is one-dimensional for any connected `U ⊂ ℂ` (it's just `ℂ` as a vector space of constants, modulo the identity-theorem equivalence).

**The LOCK fails directly** because the invariant protects a result that *would* follow from the identity theorem *if its hypotheses were met*. The hypotheses are not met (Obstructions A–C in Step 3). No invariant protects a non-existent closure.

**DECOMPOSITION attempt** (per §5 of the spawn prompt, when LOCK fails):

Route A can be decomposed into two sub-problems, each weaker than the full H4 but each requiring independent closure:

**R.A.1.a — Analyticity of `F^pert(t)` on a complex disk**: Show that the formal power series `F^pert(t) := Σ_n f_n^pert t^n`, with coefficients computed by Luscher 2010 / Harlander–Neumann 2016 / Artz 2019, converges as an analytic function on some disk `|t| < r_t^pert > 0`. This would require:

- Computing the Luscher–Harlander–Artz coefficients `f_n^pert` up to order 3 (known) and showing that the known terms satisfy a uniform bound `|f_n^pert| ≤ M (r_t^pert)^{-n}`.
- Extending the bound to all orders — which is a statement about the asymptotics of 4D gauge-theory perturbation series, currently an open problem equivalent to Borel summability of the flow-time expansion. Renormalon analysis (Beneke 1999; 't Hooft 1979) suggests the perturbative series in `g^2` is factorially divergent; in the flow-time variable `t` the structure is different but is not known to be convergent.

**Status of R.A.1.a**: OPEN. Not closable within the current framework without either a Borel summation theorem for 4D YM or a direct constructive proof of convergence. **Estimated difficulty**: comparable to Borel summability of 4D non-Abelian gauge theory, which is an independent long-standing open problem.

**R.A.1.b — Existence of an independent point `t_0` where `F(t_0) = F^pert(t_0)`**: Find a specific `t_0 ∈ D_{r_t}` where the equality can be demonstrated without invoking H4. The NATURAL candidates (tree level, Reisz lattice perturbative agreement, large `t`, super-renormalizable analogue) are ruled out in Step 3. **Status**: OPEN, with no obvious candidate.

**Decomposition verdict**: Both sub-problems are OPEN and independent. Closing R.A.1.a does not close R.A.1.b, and vice versa. Route A is not "a few pages of new text from W7-14 §5.3"; it is two independent open problems each comparable to or harder than H4 itself.

### Step 5 — COMPUTE (Pattern 3: Casimir / scale-setter)

Per the spawn prompt, I execute the concrete computation attempt:

**(a) Extract Taylor coefficients `a_n = F^{(n)}(0)/n!` from W5-10 Step 2**:

By W1-05 Corollary 5.1 (convergence of the small-flow-time expansion):

```
F(t) = Σ_{n≥0} a_n t^n,   |a_n| ≤ M_F / r_t^n,   M_F := sup_{|s|=r_t/2}|F(s)| < ∞
```

The Taylor coefficients `a_n` are **abstractly defined** as
```
a_n = F^{(n)}(0)/n! = (1/2πi) ∮_{|s|=r} F(s) s^{-n-1} ds
```
for any `0 < r < r_t`. They are **not** computed explicitly in W5-10 — only their existence and the Cauchy-type bound are established. In particular:

- `a_0 = F(0) = S_2^ren(x,y)`, the renormalized two-point function at the specific non-coincident pair `(x,y)`. This is a **non-perturbative quantity of unknown closed-form value**. W5-10 Lemma 3.8 establishes that `a_0` exists and is finite, satisfies OS positivity and exponential clustering at rate `Δ_∞`, but does **not** compute its numerical value.
- `a_1 = F'(0) = lim_{t→0} (F(t) - F(0))/t`, an abstract derivative of the rescaled correlator. Not computed explicitly.
- Higher `a_n` similarly.

**The extraction of Taylor coefficients from W5-10 Step 2 is abstract, not concrete**. The Cauchy integral formula gives the coefficients in principle but requires evaluating `F(s)` on the boundary circle `|s| = r`, which is itself a non-perturbative computation.

**(b) Compute `f_n^pert` from the Feynman-diagrammatic rules**:

From W7-14 §1.2 (eq. 1.3) and W7-15 §4.2, the perturbative coefficients are:

- **Leading form** (by RG + trace-anomaly identity):
```
f_0^pert(x,y) = (C_N / |x-y|^8) · (log(1/|x-y|Λ))^{-2} · [1 + O((log)^{-1})]
```
with `C_N = 2(N^2 - 1)/π^6`, the tree-level Wick contraction constant.

- **Higher `f_n^pert`** are given by the Luscher–Weisz 2011 Feynman rules in the (4+1)-dimensional formulation. The rules produce finite integrals at each order in `g^2`, then are re-expanded in `t` via the running coupling `ḡ^2(q) = 1/(2b_0 log(q/Λ))` at `q = 1/√(8t)`. Explicit numerical values at 1-loop (Luscher 2010), 2-loop (Harlander–Neumann 2016), 3-loop (Artz et al. 2019) are available in the cited papers; I do not retrieve them here because the bottleneck below is structural, not coefficient-numerical.

**(c) Verify agreement at `n = 0` with `mp.dps ≥ 30`**:

The comparison `a_0 = f_0^pert` reduces to:
```
S_2^ren(x,y) = (C_N / |x-y|^8) · (log(1/|x-y|Λ))^{-2} · [1 + O((log)^{-1})]
```
for all non-coincident `(x,y)`. **This IS H4 at the pair `(x,y)`** (compare to L.7.1 in the preprint L-clay-conjectures.md and Conjecture L.2). The left-hand side is a non-perturbative quantity of unknown value; the right-hand side is a perturbatively-computed prediction. Equating them is not a verification step; it is the hypothesis we are trying to verify.

**I do NOT write a numerical verification script**, because the verification cannot be numerical — it is a structural identification that reduces to H4 at a specific `(x,y)`, and no finite-precision computation can settle this. `mp.dps ≥ 30` would be applicable if there were two closed-form expressions to compare; there are not.

**Compute verdict**: Step 5 does not produce a closing computation. What it produces is the recognition that the TAYLOR-COEFFICIENT IDENTIFICATION is itself H4 at the specific `(x,y)`, not a closure of H4. Route A is a **reformulation**, not a **closure**.

### Step 5.5 — Self-suspicion (3 ways this could be wrong, including backward-verification)

I list three ways my conclusion (Route A = reformulation, not closure) could be wrong. Per the spawn prompt's hard requirement, one of the three is a backward-verification of the brief's paraphrase of W7-14 §5.3 against the primary source.

**Way 1 (BACKWARD-VERIFICATION — mandatory)**: The brief claims that W7-14 §5.3 "already provides analyticity of `F(t)`" and that the remaining work is constructing the open set of agreement. Is this paraphrase faithful to the primary source?

**Verification**: I read W7-14 §5.3 directly (lines 388–414 of `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md`). The verbatim key passage is:

> "The analyticity of F(t) in the complex flow-time plane (W5-10, Step 2; radius r_t > 0 independent of the Balaban step k and the bare-scale index K) implies that the small-flow-time expansion is not merely asymptotic but **convergent**. This upgrades the status of the perturbative expansion from a formal series to an actual Taylor series with a positive radius of convergence. In particular:
> - The perturbative coefficients of F(t) = F(0) + F'(0) t + (1/2) F''(0) t^2 + ⋯ are the derivatives of a single analytic function, not independent perturbative computations.
> - The remainder R_n(t) = F(t) − Σ_{k=0}^n F^{(k)}(0) t^k/k! satisfies |R_n(t)| ≤ M_F (|t|/r_t)^{n+1}/(1 − |t|/r_t), a rigorous Cauchy remainder bound.
> - The non-perturbative value F(0) equals the sum of the convergent series, by definition of analyticity.
>
> What H4 asks, in this language, is whether the Taylor coefficients F^{(k)}(0) are computable by the Feynman-diagrammatic perturbative rules. This is a statement about the Taylor coefficients of an analytic function — a more accessible question than the traditional formulation of H4, which asks about the asymptotic behavior of a non-perturbative distribution."

**Observation**: The W7-14 §5.3 primary source is **explicit** that H4 "in this language ... [is] whether the Taylor coefficients `F^{(k)}(0)` are computable by the Feynman-diagrammatic perturbative rules" and describes this as "a more accessible question" — NOT as an already-closed question. The primary source does NOT claim Route A has closed H4; it claims Route A has **reformulated** H4 into "the mildest form in the literature".

**Backward-verification result**: The brief's paraphrase ("the remaining ~30% is the Taylor-coefficient identification", blackboard.md line 44) is CONSISTENT with the primary source. The primary source treats H4 as OPEN after the reformulation. **The blackboard is honest about this**: it describes the Taylor-coefficient identification as the **target** for Route A (line 52, "prove that the Taylor coefficients ... can be computed by the Feynman-diagrammatic perturbative rules"), not as an achieved result. My reading is consistent with both the primary source and the blackboard; the brief does not drift from the source.

**However**, the brief's language in some places describes Route A's p_success = 0.50 and calls it "the highest-probability route", which could be read as implying a plausible closure path. My §5 DIAGNOSIS is that this p_success estimate is **too optimistic** — the obstructions I identified in Steps 2–4 are structural, not "remaining engineering work", and the actual p_success is lower (possibly much lower).

**Way 2 (missing mechanism)**: I might be missing a non-standard mechanism that identifies `a_0` with `f_0^pert` without invoking H4. Candidates:

- A gradient-flow-specific selection rule that says non-perturbative contributions to `a_0` are absent (e.g., via a sum rule or an anomaly cancellation). I have searched W5-10, W7-14, W7-15, and the L-clay-conjectures appendix for such a mechanism; none is stated. The Wilson-coefficient decomposition `c_1(t) = (1/(8π^2 t^2)) · [1 + c̄_1 ḡ^2(q) + ⋯]` in W7-14 §1.2 is PERTURBATIVELY defined; using it as a denominator in `F(t) = S_{2,t}^c/c_1(t)^2` treats `c_1` perturbatively while treating the numerator non-perturbatively, and this mismatch is the source of my Obstruction A in Step 2.
- An anomaly-based argument (like the Wess–Zumino cohomological protection used for the KK tower in W7-14 §6.3). The trace-anomaly identity `γ_{TrF^2} = -2β(g)/g` is **perturbative** in origin (Spiridonov 1984; it is exact within continuum perturbation theory to all orders but not a non-perturbative theorem); it does not give `a_0 = f_0^pert` by itself.

**Assessment**: I don't see a missing mechanism, but I acknowledge the possibility. If Critic W1-A1-Critic can identify one, this Author would advance. Until then, I stand on BLOCKED-DECOMPOSED.

**Way 3 (identity-theorem-weaker form)**: Maybe the identity theorem can be applied in a weaker sense I missed. Candidates:

- **Identity of Taylor series as formal power series**: This doesn't require analyticity of `F^pert`; it just requires equality of all coefficients `a_n = f_n^pert`. But this is exactly the target, not a tool.
- **Identity modulo flat functions**: Two smooth functions with identical Taylor series at a point agree modulo flat (all-derivatives-zero) functions. `F` is analytic, so flat functions in the `F`-class are zero, and identity of Taylor coefficients would give `F ≡ F^pert` in the analytic category IF `F^pert` were also analytic. But analyticity of `F^pert` is Obstruction A.
- **Borel resummation**: If `F^pert` is Borel-summable (an open problem for 4D YM), the Borel sum is an analytic function in a sector, and the identity theorem can be applied in that sector. This would close Route A but requires a separate theorem (Borel summability of 4D YM) that is an independent open problem of comparable difficulty to H4 itself.

**Assessment**: All weaker forms of the identity theorem that I can identify either reduce to the original form, or require Borel summability, which is independently open. I don't see a weaker form that rescues Route A.

### Step 6 — VERIFY (Pattern 5: precision diagnostic)

**Finiteness**: Not applicable in the numerical sense — R.A.1's verdict is structural, not numerical.

**Precision floor**: Not applicable — I am not making a headline quantitative claim.

**Formal check**: The structural argument in Steps 2–5 depends on the following verifiable claims. I verify each against the primary sources:

1. **`F(t)` analytic on `|t| < r_t` with `r_t > 0`, `(k,K)`-independent**. Source: W5-10 Part I Step 2 + W1-05 Lemma 3.1. **Verified** against the primary source text in §5.5 Way 1.

2. **The perturbative series in `g^2` for 4D Yang–Mills is divergent (factorial growth)**. Source: Beneke, "Renormalons", Phys. Rep. 317 (1999) 1; 't Hooft 1979 "Can we make sense of quantum chromodynamics"; Lipatov 1977. **Taken as rigorous within perturbation theory** — this is textbook, not in my proximate sources, but is a standard fact and does not drive the argument (I use it only as supporting evidence for Obstruction A).

3. **Borel summability for 4D Yang–Mills is an open problem**. Source: Beneke 1999; 't Hooft 1979. **Open, textbook**.

4. **`f_0^pert = C_N/|x|^8 (log)^{-2}[1 + O((log)^{-1})]` with `C_N = 2(N^2-1)/π^6`**. Source: W7-14 §2.3 (eq. 2.5, 2.6); W7-15 §4.2 (eq. 4.3j); G4b-af-short-distance-match.md §2 (eq. S2.4, S2.5). **Verified** — three independent sources agree on the form; `C_N` is from the tree-level Wick contraction and is rigorous within perturbation theory.

5. **The perturbative identification `a_0 = f_0^pert` IS H4 at the specific pair `(x,y)`**. Source: L-clay-conjectures.md §L.7.1 (H4 statement, eq. L.7.1); compare to W7-14 §4.1 (eq. 4.1). **Verified by direct comparison** — the statements are identical modulo notation.

**All structural claims verified against primary sources. No paraphrase trust invoked.**

## Verdict: **BLOCKED-DECOMPOSED**

Route A is a **reformulation** of H4 into "identify the Taylor coefficients of `F(t)` at `t=0` with the Feynman-diagrammatic coefficients", not a **closure**. The identity theorem of complex analysis is the correct template, but its hypotheses are not met:

- (A) `F^pert(t)` is not known to be an analytic function on any open disk — it is a formal power series whose coefficients are computed by Luscher–Harlander–Artz, but the series is expected to diverge (renormalons / Borel summability open).
- (B) No independent `t_0 ∈ D_{r_t}` is known where `F(t_0) = F^pert(t_0)` can be demonstrated without invoking H4.
- (C) The `n = 0` Taylor coefficient identification `a_0 = f_0^pert` IS H4 at the specific `(x,y)`, not a closure of H4.

The decomposition yields **two independent open sub-problems** (R.A.1.a and R.A.1.b in Step 4), each of difficulty comparable to or greater than H4 itself. Neither is closable within the gradient-flow framework alone.

**My recommendation to the runner**: Downgrade Route A's `p_success` from 0.50 to a much smaller value (my estimate: ≤ 0.10, conditional on a future closure of R.A.1.a via a Borel-summation theorem or on a framework-native closure of R.A.1.b via a mechanism I'm not seeing). The runner may want to re-weight the joint probability calculation in blackboard §E.1 accordingly.

Route A is **NOT KILLED**: the reformulation is genuinely useful (it packages H4 into a cleaner form, it motivates the gradient-flow extraction, it provides a foothold for future work if Borel summability or an instanton-obstruction argument can be developed). But it is not the closure mechanism the brief suggests.

The analogy to Paper 26 Route 3 (G's projector) **breaks down at a specific point**: in Paper 26, the §§7–8 core was "already algebraic" (Remark 7.2: "The derivation is pure algebra on the local Euler factor"), and G's projector was a single algebraic object that replaced the one rhetorical dependency on eigenstates. In Paper 8, the W7-14 §5.3 reformulation is analytic, not algebraic, and the analogous "single object" — a function `F` that is already analytic — does not package the full closure because the identity-theorem hypotheses require a second analytic function to compare against, which doesn't exist canonically. The geometric pattern is structurally different: in BSD the rewrite eliminated a dependency; in YM the rewrite shifts a dependency.

## Generative step / Stuck-at step

**Generative step (produced the closing insight)**: Step 1 — DIAGNOSE. The insight that H4's difficulty lives in the **asymptotic category of the perturbative side** (formal power series vs analytic function), and that the non-perturbative side has already been upgraded to an analytic function by W5-10 Step 2, is the key. It re-centers the question from "compute Taylor coefficients" to "is `F^pert` analytic".

**Stuck-at step**: Step 5 — COMPUTE. The Taylor-coefficient identification `a_0 = f_0^pert` IS H4 at the specific `(x,y)`; there is no `t_0` where an independent computation gives equality without invoking H4; and the identity theorem's hypotheses are not met because `F^pert` is not analytic.

## §I notes to append

- **CONCERN**: The runner's `p_success = 0.50` estimate for Route A is likely too high. Based on my Steps 2–5, the route is structurally blocked rather than technically almost-there. I estimate `p_success ≤ 0.10` conditional on a future advance in Borel summability for 4D YM or an instanton-obstruction argument. The runner may want to reallocate Wave 2+ effort accordingly — R.B (CCM 2025 port) and R.C (spectral action) are both more structurally promising than R.A if my DIAGNOSIS is correct, because they attempt to construct the non-perturbative object from a DIFFERENT framework entirely (CCM spectral triple or Connes spectral action), which would provide the missing "second analytic function" that the identity theorem needs. Route D (editorial HONEST-STALL) remains the safety net at `p ≈ 0.99`.

- **CONCERN**: The blackboard §D entry for "Taylor-coefficient identity" (row labeled "`F^{(n)}(0)/n! = f_n^pert` — the closure target for Route A") is correctly listed as status = O (open). My recommendation is to add a second row for "Analyticity of `F^pert(t)` on an open disk" as a separate open sub-problem, which is actually the bottleneck I identify. This clarifies the decomposition of R.A.

- **CASCADE**: If Route A is reclassified from "p=0.5 technical" to "p≤0.1 structural", the blackboard §E.1 joint probability calculation changes: `P(A∨B∨C∨D) = 1 − (1−0.10)(1−0.30)(1−0.25)(1−0.99) = 1 − 0.90·0.70·0.75·0.01 ≈ 0.9953`. The joint probability is still dominated by R.D at ~0.99, so the PROGRAMME robustness is unaffected — Paper 8 still ships 18/18 conditional on CBB axioms via R.D. But the TECHNICAL closure ambition (closing H4 via mathematical bypass rather than editorial HONEST-STALL) drops from ~0.80 (if Routes A/B/C each had p ≈ 0.30–0.50) to ~0.55 if R.A is downgraded. The runner should consider whether to (a) accept the downgrade, (b) re-examine Routes B and C for structural obstructions of similar type, or (c) restructure Wave 2 to prioritize R.D editorial work while B/C proceed on a longer timescale.

- **LESSON**: The key meta-learning is that **"reformulation into the mildest form"** is not the same as **"closure"**. The W7-14 §5.3 reformulation was a real advance (it moved H4 from a comparison of two differently-defined objects to a question about Taylor coefficients of one analytic function), but the Taylor coefficients themselves are still non-perturbative objects, and the perturbative side is still only a formal power series. The analogous pattern in the BSD closure (Paper 26 Route 3) WAS a closure because Paper 26 §§7–8 was ALREADY algebraic and the projector eliminated the last rhetorical dependency. For a "structural bypass" to actually close a gap, the remaining core must itself be rigorous in the new framing — in Paper 26 this was true; in Paper 8 the new framing shifts the rigor burden from one side to the other without eliminating it. **The lesson**: before celebrating a reformulation, verify that the new form is CLOSABLE, not just CLEANER.

- **LESSON**: The I-7 backward-verification discipline saved me here. If I had trusted the brief's paraphrase — which says the remaining work is ~30% and Route A is ~50% likely to close — I would have written a different output that claimed a closure via invoking the identity theorem with hand-waved hypotheses. Reading the primary source (W7-14 §5.3, W5-10 Step 2, W1-05 Lemma 3.1, G4b/G4d gap statements) revealed that the primary sources are EXPLICITLY HONEST about the open-ness of the Taylor-coefficient identification and the partial nature of the reformulation. The honest-first cognitive stance combined with the mandatory backward-verification produced the correct (disappointing but truthful) verdict.

## Proposed §D toolkit additions

Four new entries, plus modifications to existing entries:

1. **Analyticity of `F^pert(t)` on an open disk** [OPEN sub-problem, comparable difficulty to Borel summability of 4D YM].
   - *Canonical name*: Perturbative flow-time analyticity.
   - *Statement*: The formal power series `F^pert(t) := Σ_n f_n^pert t^n`, with coefficients `f_n^pert` from Luscher 2010 / Harlander–Neumann 2016 / Artz 2019, converges as an analytic function on some open disk `|t| < r_t^pert > 0`.
   - *Source*: Logical reformulation of H4; dual to the W5-10 Step 2 non-perturbative analyticity.
   - *Status*: O (open; comparable to Borel summability).
   - *Notation*: `𝒜(F^pert)`.

2. **Independent-point agreement for R.A.1** [OPEN sub-problem, no obvious candidate].
   - *Canonical name*: Route A independent-point agreement.
   - *Statement*: There exists `t_0 ∈ D_{r_t}` such that `F(t_0) = F^pert(t_0)` can be demonstrated without invoking H4.
   - *Source*: Hypothesis premise of the identity-theorem closure for Route A.
   - *Status*: O (open; no candidate in sight).
   - *Notation*: `𝒫_{R.A.1}^{ind}`.

3. **Analyticity identity theorem applicability criterion** [R template, with new status marker].
   - *Canonical name*: Identity-theorem two-function requirement.
   - *Statement*: The identity theorem (Ahlfors Ch. 6) closes a gap of the form "`F = G` on `U`" iff BOTH `F` and `G` are analytic on a connected open set `U` AND they agree on a set with an accumulation point in `U`.
   - *Source*: Standard complex analysis (Ahlfors).
   - *Status*: R (rigorous); but the APPLICABILITY to Route A is BLOCKED by failure of the two premises (see §R.A.1.a, §R.A.1.b above).
   - *Notation*: (no change).

4. **Taylor-coefficient identity reformulation status** [modify existing row].
   - The existing §D row (`Taylor-coefficient identity | F^{(n)}(0)/n! = f_n^pert (the closure target for Route A) | Route A target | O`) should be annotated: this is equivalent to H4 at each specific `(x,y)`, not a closure of H4. The status stays O but the description should clarify "equivalent to H4, not weaker".

## What the next runner needs to know (fixed schema)

**State at handoff**:
- Route A's analyticity-uniqueness mechanism is a reformulation of H4, not a closure.
- The W7-14 §5.3 reformulation is real and useful (it packages the non-perturbative side as an analytic function), but does NOT reduce H4 to "a few pages of new text". It reformulates H4 into an equally hard open problem about Taylor-coefficient identification, which in turn decomposes into two sub-problems (R.A.1.a Borel-summability-like + R.A.1.b independent-point-agreement), both OPEN and not obviously closable.
- My backward-verification of W7-14 §5.3 against the primary source confirms the reformulation is genuine and NOT a closure; the primary source itself says "a more accessible question" (not "an answered question").
- **Route A is BLOCKED-DECOMPOSED**, not KILLED. The decomposition gives a clear structure for future work if a tool becomes available (Borel summability for 4D YM; instanton-obstruction argument; direct proof that non-perturbative contributions to `a_0` vanish).

**Open dependencies**:
- R.A.1.a — Analyticity of `F^pert(t)` on an open disk (equivalent to Borel summability of the flow-time expansion; currently OPEN).
- R.A.1.b — Independent `t_0` with `F(t_0) = F^pert(t_0)` (no candidate in sight).
- Both are independent of the W5-10 Step 2 non-perturbative analyticity, which is established.

**Watch out for**:
- **Don't conflate "reformulation" with "closure"**. The W7-14 §5.3 claim is an advance in framing, not a partial proof. Reading it as partial progress toward a closure overestimates the route.
- **The asymmetry in asymptotic category**. Non-perturbative side = analytic function (established). Perturbative side = formal power series (still). The identity theorem needs both sides analytic.
- **The analogy to Paper 26 Route 3 breaks at "core is already algebraic"**. In BSD, §§7–8 was already pure algebra and G's projector was the last rhetorical fix. In YM, the reformulation shifts the rigor burden but doesn't eliminate it.
- **The runner's `p_success = 0.50` may be optimistic**. Consider downgrading per my §I CONCERN.

**Preferred next move**:
- Accept the BLOCKED-DECOMPOSED verdict and prioritize Routes B (CCM 2025 port) and C (spectral action) for Wave 2+. These routes attempt to construct the non-perturbative side from a DIFFERENT framework (not gradient flow), which would provide the "second analytic function" that the identity theorem needs. This is structurally more promising than Route A within the existing framework.
- In parallel, R.D (editorial HONEST-STALL) proceeds per §E plan — it remains the safety net at p ≈ 0.99.
- Consider spawning a Wave 2 node R.A.2a specifically targeting the instanton-contribution analysis: prove that at `n = 0`, non-perturbative contributions (instantons, renormalons) to the Taylor coefficient `a_0` are ABSENT or structurally forbidden, perhaps via a framework-native mechanism (Identity 12 + bridge family). If this can be shown, `a_0 = f_0^pert` would follow rigorously without the full H4, which would partially close H4 (specifically, close the LEADING short-distance identification which is what L.2 needs).

**Voice canon citation** (§J register marker):
- "Route A is a reformulation, not a closure" — terse declaration, honest-first posture.
- "The wall is named; the wall is not yet crossed" — aligning with the §J register from `35-final-verdict.md`.
- "H4 remains the wall. W7-14 §5.3 moved the wall; it did not cross it" — extended variant.
- "W7-14 reformulated; W11-A did not close; the bottleneck is elsewhere" — structural event language for the closure-voice target in §J of the blackboard.
- **Not deployable**: "Route A landed" — this phrasing would be dishonest given my verdict. Reserve for an actual closure.

---

*End of R.A.1 Author output. Verdict: BLOCKED-DECOMPOSED. Handoff to Critic W1-A1-Critic and to runner for Wave 2 re-planning per §I CONCERN / CASCADE / LESSON above.*
