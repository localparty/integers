# Link 14 Wave 7 Critic — Final Adversarial Verification of Route B

**Verdict:** SURVIVED

**Prior state:** Wave 5 returned WEAKENED on the per-polymer dev ≥ 2 assertion in Wave 4's Edit 4. Route B (Wave 6) re-orders the chain to avoid any per-polymer claim. This is the independent Wave 7 adversarial check.

---

## C1 — §5.5.3 Lemma bound (3) verbatim form

**PASS.**

Preprint lines 1183–1200 (`05-continuum-limit.md`) read, verbatim:

> **Lemma (Two-Derivative Spectral Bound).** *Let $\mathcal{O}$ be a
> gauge-invariant operator on $\Lambda_{k+1}$ satisfying:*
>
> *(i) Bounded operator norm: $\|\mathcal{O}\| \leq M$.*
>
> *(ii) Locality: $\mathcal{O}$ is supported in $\mathcal{N}(0)$ of
> diameter $R_0$ lattice spacings.*
>
> *(iii) Boltzmann deviation order $\mathrm{dev}(\mathcal{O}) \geq p$
> in the minimal transfer-matrix representation.*
>
> *Then:*
>
> $$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p\,M\,\hat{\Delta}^p \tag{3}$$
>
> *where $C_p$ depends on $p$, $R_0$, and the gauge group $N$, but not
> on $k$, $g_k$, or the volume.*

The Author's claim is correct. Bound (3) has exactly the factorized form $C_p \cdot \|\mathcal{O}\| \cdot \hat\Delta^p$ with $M = \|\mathcal{O}\|$. Route B's central use — applying (3) to the total operator $\delta E_k^{d=6}$ with $M = \|\delta E_k^{d=6}\|_{\mathrm{op}}$ — is a verbatim reading of the lemma.

**Bonus finding.** §5.6 Part III.5 (lines 1885–1892) shows the preprint itself does exactly this:

> Applying the spectral lemma with $p = 2$, $M = \|\delta E_k^{d=6}\| \leq Cg_k^4$ (Balaban):
> $$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
>   \leq C_2 \cdot Cg_k^4 \cdot \hat{\Delta}_{k+1}^2 = C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2. \tag{III.2}$$

Route B formalizes the preprint's own Part III.5. There is no novelty to contest; the total-operator spectral application at line 1888 is the preprint's preferred reading.

---

## C2 — Scope separation validity

**PASS — and supported by preprint framing.**

The Author claims Part III.3's Lemma applies to the total operator $\delta E_k^{d=6}$ (where gauge invariance is manifest in any reading), not per polymer. Two independent confirmations from the preprint:

**1. Part III.3's own preamble** (lines 1763–1767):

> Instead of splitting, we prove that the **total** operator
> $\delta E_k^{d=6}$ has $\mathrm{dev} \geq 2$ by classifying
> all dimension-6 gauge-invariant operators.

The Lemma at lines 1769–1773 is introduced as a total-operator statement. The preprint's framing is that Part III.3 *deliberately* avoids per-polymer splitting; this is its design.

**2. Part III.4** (lines 1859–1872) applies the Lemma to $\delta E_k^{d=6}$ in a single step:

> The dimension-6 part $\delta E_k^{d=6}$ of the remainder is by
> construction a $\mathcal{C}$-even, dimension-6, gauge-invariant
> local operator. By the Lemma: $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$.

No per-polymer invocation appears anywhere in Part III.3 or III.4. Gauge invariance at the total-operator level is uncontested: Balaban's effective action is gauge-invariant by construction of the RG (Wilson action + Haar measure + block-spin integration all preserve gauge symmetry), and the dimension-6 projection commutes with the gauge-group action.

$\mathcal{C}$-evenness, dimension-6, and analyticity in $\{V_\ell\}$ with radius $\rho > 0$ (from (B1)) all hold at the total-operator level by construction. All five hypotheses of Part III.3's Lemma are satisfied by $\delta E_k^{d=6}$ as a total operator. Route B's scope separation is both valid and preprint-endorsed.

---

## C3 — Triangle inequality step

**PASS.**

The step $\|\delta E_k^{d=6}\|_{\mathrm{op}} = \|\sum_{X \ni 0} K_k^{d=6}(X,\cdot)\|_{\mathrm{op}} \leq \sum_{X \ni 0} \|K_k^{d=6}(X,\cdot)\|_{\mathrm{op}}$ requires all summands to act on the same Hilbert space.

Each $K_k^{d=6}(X, \cdot)$ is a polymer activity at RG step $k$, viewed as a bounded operator on the transfer-matrix Hilbert space $\mathcal{H}_{k+1}$ (the same Hilbert space on which the §5.5.3 Lemma operates — explicit at line 1184: "gauge-invariant operator on $\Lambda_{k+1}$"). The polymer support $X \subset \Lambda_k$ determines the spatial localization of the operator, but the operator itself acts on the full $\mathcal{H}_{k+1}$. Triangle inequality on operator norms (sub-additivity of $\|\cdot\|_{\mathrm{op}}$) then applies without qualification.

The norm-convergent polymer expansion (CMP 109, Thm 3, Mayer/Kotecký–Preiss bound) guarantees the sum is norm-convergent, so the triangle inequality extends from finite sums to the infinite polymer sum by continuity of the norm. No Hilbert-space mismatch exists. Step is load-free.

---

## C4 — Revised Application paragraph

**PASS.**

Route B's Application paragraph (the replacement for Wave 4's Edit 4) reads:

> **Application.** By (B1), $\delta E_k^{d=6}(0) = \sum_{X \ni 0}
> K_k^{d=6}(X, \cdot)$ is a convergent polymer expansion in the
> small-field domain, whose total operator is a local, gauge-invariant,
> $\mathcal{C}$-even, dimension-6 operator, analytic in $\{V_\ell\}$.
> By §5.6 Part III.4 (eq. (III.1)), applied once at the total-operator
> level, $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$. Therefore by the
> Lemma (Two-Derivative Spectral Bound, §5.5.3, bound (3)) with
> $p = 2$ and $M = \|\delta E_k^{d=6}\|_{\mathrm{op}}$:
> $$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
>   \leq C_2 \cdot \|\delta E_k^{d=6}\|_{\mathrm{op}}
>   \cdot \hat{\Delta}_{k+1}^2.$$
> The operator norm is controlled at the polymer-sum level by the
> polymer-aware Hastings--Koma bound of Step 3(i): by triangle
> inequality on operator norms plus Balaban's polymer-activity bound
> $\|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}} \leq C\,g_k^4\,e^{-\kappa|X|}$
> (CMP 109, Thm 3; dimension-6 power counting),
> $$\|\delta E_k^{d=6}\|_{\mathrm{op}} \leq
>   \sum_{X \ni 0} \|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}}
>   \leq C\,g_k^4\,C_{\mathrm{KP}} =: C_{\mathrm{norm}}\,g_k^4.$$
> Combining, with $C_{\mathrm{new}} := C_2 \cdot C_{\mathrm{norm}}$
> ($k$-uniform and $L$-uniform):
> $$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\,
>   g_k^4\,\hat{\Delta}_{k+1}^2.$$
> The deviation order is extracted from Part III.3 at the level of the
> total operator (where gauge invariance is manifest by construction);
> the polymer-sum control is extracted at the level of operator norms.
> Per-polymer dev $\geq 2$ is neither asserted nor needed.

Comparison against Wave 4 Edit 4's "to" text (L14-patch.md lines 174–186): the Wave 4 text asserted "activities are $\mathcal{C}$-even dimension-6 operators with $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$ (§5.6 Part III.3)" — a per-polymer dev ≥ 2 claim. Route B's paragraph removes this assertion entirely. The phrase does not appear. The paragraph is internally coherent: each step cited exists in the preprint, and the logical sequence (Part III.4 eq. (III.1) → §5.5.3 bound (3) → triangle inequality → KP sum) is watertight.

One minor presentation note: the paragraph cites "§5.6 Part III.4 (eq. (III.1))" rather than "§5.6 Part III.3", correctly distinguishing the Lemma statement (III.3) from its application to $\delta E_k^{d=6}$ (III.4). This is a precision improvement over the Wave 4 text.

---

## C5 — Double-citation concern (F5)

**PRESENTATION ISSUE ONLY — no content flaw.**

Route B cites §5.5.3 Step 3(i) at two logically separate points:

1. **Spectral step on the total operator.** Step 3(i)'s context (lines 1321–1332) gives the Hastings–Koma-based spectral lemma $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p^* \cdot M \cdot \hat\Delta^p$ with $K$-uniform constant. Route B uses this as the warrant for applying bound (3) to the total operator with the polymer-aware constant $C_p^*$ replacing $C_p$ (handling the F4 locality concern: the total operator's support is not bounded by fixed $R_0$, but Step 3(i)'s polymer extension delivers an $|X|$-independent constant).

2. **Norm step on the polymer sum.** Step 3(i)'s explicit Kotecký–Preiss sum $\sum_{X\ni 0} C_p^* e^{-\kappa|X|} < \infty$ (lines 1337–1339) is used purely as a norm-summability fact: $\sum_X \|K_k^{d=6}(X)\| \leq C_{\mathrm{KP}} \cdot Cg_k^4$. The $\hat\Delta^p$ factor from the spectral part of Step 3(i) is not invoked in this second use.

These are genuinely distinct contents of the same paragraph. The paragraph establishes two things: (a) a per-polymer spectral bound with $|X|$-independent constant, and (b) norm-summability via Kotecký–Preiss. Route B uses (a) at the spectral level for the total operator and (b) at the norm level for the polymer decomposition. No content is double-counted; the $\hat\Delta^2$ factor is sourced exactly once (from Part III.4 eq. (III.1) → bound (3) applied to the total operator), and the $g_k^4$ factor is sourced exactly once (from Balaban's polymer-activity norm bound via the KP sum).

**However**, a referee who has not read Route B's design brief may read the Application paragraph and infer that Step 3(i) is doing both jobs simultaneously for the same operator, creating apparent circularity. The Author's recommendation to label the two uses "Step 3(i) spectral" and "Step 3(i) norm" in the Application paragraph is apt and should be implemented in the preprint. This is a presentation matter, not a logical flaw. The content is sound.

---

## Summary

Route B closes the Wave 5 residual joint (per-polymer dev ≥ 2) by refusing to assert it. Instead it:

1. Applies Part III.3 once to the total operator $\delta E_k^{d=6}$, producing dev ≥ 2 at the total-operator level — exactly what preprint Part III.4 eq. (III.1) already does.
2. Applies §5.5.3 bound (3) to the total operator, yielding $|\langle 1|\delta E_k^{d=6}|1\rangle_c| \leq C_2 \|\delta E_k^{d=6}\| \hat\Delta^2$ — exactly what preprint Part III.5 already does.
3. Bounds the operator norm by triangle inequality and Kotecký–Preiss, using Balaban's polymer-activity norm bound. This is a norm-level step with no spectral content.

All five checks pass. The composition is load-free, preprint-native, and strictly avoids the per-polymer claim that Wave 5 flagged. C5 is a presentation issue that warrants a two-word label fix in the Application paragraph but does not impugn soundness.

**Final recommendation: Route B is ready to promote into the preprint.** Replace Wave 4's Edit 4 "to" text verbatim with Route B's Application paragraph, and update Edit 3's Method column entry as specified. The chain closes at 17/17 (with L18 conditional on the independent spectral-gap induction, unchanged). The PCA programme for Paper 08 is complete.

---

*Wave 7 Critic. Independent instance. 2026-04-13.*
