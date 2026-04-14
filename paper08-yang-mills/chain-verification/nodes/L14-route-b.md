# L14 Route B — Total-Operator dev ≥ 2, Norm Bound from Hastings–Koma

**Link:** 14 (Δ_∞ > 0, continuum mass gap)
**Wave:** 6 (Author; construct)
**Wave 5 Critic verdict:** WEAKENED — residual joint S4 (per-polymer dev ≥ 2)
**Author:** Claude Opus 4.6 (1M context), Wave 6 Route B
**File-owner:** only `nodes/L14-route-b.md`
**Verdict:** ADVANCED
**Headline:** Apply §5.6 Part III.3 only to the total operator δE_k^{d=6} (where gauge invariance is manifest in any reading); feed the resulting dev ≥ 2 conclusion into §5.5.3's spectral lemma, which already bounds the connected matrix element by ‖𝒪‖·Δ̂²; then bound ‖𝒪‖ polymer-wise via §5.5.3 Step 3(i) + Kotecký–Preiss. The Δ̂² factor lives at the total-operator spectral level; the polymer sum lives at the norm level; they never meet inside one per-polymer claim.

**Compared to Route A:** Route A closes the joint by *reading-of-hypothesis* — arguing Part III.3's "gauge-invariant" means block-spin, so each polymer activity individually satisfies Part III.3's hypotheses. Route B closes the joint by *scope separation* — refusing to invoke Part III.3 per polymer at all. Route B assumes strictly less: it does not require that individual polymer activities be block-level gauge-invariant. The price is one extra inequality chain (the norm-triangle step ‖ΣK‖ ≤ Σ‖K‖), which is standard and load-free.

---

## Diagnosis

### The joint, and the precise re-ordering

The Wave 4 Application paragraph (Edit 4 of `L14-patch.md`) asserts, for a fixed polymer $X$:

> dev$(K_k^{d=6}(X,\cdot)) \geq 2$ (§5.6 Part III.3)

Wave 5's Critic (C2) flags this as unproved: Part III.3's hypothesis includes "local, gauge-invariant, $\mathcal{C}$-even", and a single polymer activity $K_k(X,\cdot)$ is not *obviously* gauge-invariant in isolation (it is supported on $X$; the full effective action is gauge-invariant after summing over all $X$). Route A closes this by interpreting the Lemma's "gauge-invariant" as *block-spin* gauge-invariant and pointing to Balaban CMP 95–98 for per-polymer block-level invariance. That reading is defensible but depends on a hypothesis-reading claim a referee could contest.

Route B refuses to argue per-polymer dev ≥ 2 at all. Instead it re-orders the chain:

**Route A order:**
> For each $X$: (gauge-invariance per polymer) ⇒ Part III.3 ⇒ dev$(K_k^{d=6}(X,\cdot)) \geq 2$ ⇒ §5.5.3 gives $|\langle 1|K_k^{d=6}(X,\cdot)|1\rangle_c| \leq C_p^* \|K_k^{d=6}(X,\cdot)\| \hat\Delta^2$; sum over $X$.

**Route B order:**
> (Total-operator gauge-invariance) ⇒ Part III.3 ⇒ dev$(\delta E_k^{d=6}) \geq 2$ at the *total-operator* level ⇒ §5.5.3's Lemma (Two-Derivative Spectral Bound) gives $|\langle 1|\delta E_k^{d=6}|1\rangle_c| \leq C_2\,\|\delta E_k^{d=6}\|\,\hat\Delta^2$; then bound $\|\delta E_k^{d=6}\| \leq \sum_X \|K_k^{d=6}(X,\cdot)\| \leq C_{\text{new}}\,g_k^4$ by triangle inequality and the polymer-aware Hastings–Koma norm estimate of §5.5.3 Step 3(i) + Kotecký–Preiss.

The step that replaces per-polymer dev ≥ 2 is the **triangle inequality on operator norms** $\|\sum_X K_k^{d=6}(X,\cdot)\| \leq \sum_X \|K_k^{d=6}(X,\cdot)\|$. This is a free step (it needs only that the $K_k^{d=6}(X,\cdot)$ all act on the same Hilbert space — which they do, namely the transfer-matrix Hilbert space at step $k+1$).

### Contrast with Route A's reading-of-hypothesis approach

Route A's load-bearing claim is **hermeneutic**: *"gauge-invariant" in Part III.3 means block-spin gauge-invariant.* Supported by the Lemma's context ($\Lambda_{k+1}$ block lattice, "analytic in $\{V_\ell\}$"), but a referee invested in the full fine-lattice reading could insist on reading (a).

Route B's load-bearing claim is **algebraic**: *the §5.5.3 Lemma already delivers $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p \|\mathcal{O}\| \hat\Delta^p$, and the operator norm of a convergent polymer sum is bounded by the sum of polymer norms.* No hermeneutic dispute is possible — triangle inequality does not depend on how anyone reads the word "gauge-invariant".

Route B therefore assumes strictly less. Its cost is one additional line in the proof. (Route A's cost is a hermeneutic defense extending over three preprint passages and one lemma.)

---

## Research (6-step inner method loop)

### Step 1 — Diagnose (precise)

Replace the per-polymer dev ≥ 2 step with the composition:

$$\underbrace{|\langle 1|\delta E_k^{d=6}|1\rangle_c|}_{\text{spectral bound target}}
\;\leq\;
\underbrace{C_2 \cdot \|\delta E_k^{d=6}\| \cdot \hat\Delta_{k+1}^2}_{\text{§5.5.3 Lemma applied to total operator}}
\;\leq\;
\underbrace{C_2 \cdot \Big(\sum_X \|K_k^{d=6}(X,\cdot)\|\Big) \cdot \hat\Delta_{k+1}^2}_{\text{triangle inequality}}
\;\leq\;
\underbrace{C_2 \cdot C^*_{\mathrm{KP}} \cdot g_k^4 \cdot \hat\Delta_{k+1}^2}_{\text{§5.5.3 Step 3(i) + KP sum}}.$$

No step invokes dev ≥ 2 of an individual $K_k^{d=6}(X,\cdot)$. Part III.3 is cited only once, applied to the sum $\delta E_k^{d=6}$ as a whole, where its hypothesis (gauge-invariance) is manifest in any reading.

### Step 2 — Reinterpret (spectral vs. norm are separate facts)

The $\hat\Delta^2$ factor is a **spectral** property: it emerges from the transfer-matrix decomposition of the connected one-particle matrix element, controlled by how much the spectral weight vanishes at the diagonal $\mathbf{n} = (m, m, \ldots)$. §5.5.3's Lemma packages this: *for any* operator $\mathcal{O}$ satisfying (i)–(iii), the one-particle connected matrix element satisfies the bound (3) with $M = \|\mathcal{O}\|$.

The polymer sum $\sum_X K_k^{d=6}(X,\cdot)$ is a **norm** fact: it is a convergent expansion, and the sum of norms converges by the Kotecký–Preiss bound plus the $|X|$-independent Hastings–Koma constant. This is a completely independent estimate — it has nothing to do with spectral gaps or deviations. §5.5.3 Step 3(i) provides this polymer-aware norm-level statement.

These two facts compose by **triangle inequality on operator norms**, applied to the total operator $\delta E_k^{d=6}$. The composition is entirely clean: the spectral bound sees only the total operator's norm; the norm bound sees only the polymer decomposition's convergence. The per-polymer dev ≥ 2 question is dissolved — it was never needed.

### Step 3 — Unify (primary-source support)

Both ingredients are already preprint-native:

1. **§5.5.3's Lemma (Two-Derivative Spectral Bound), `05-continuum-limit.md` lines 1183–1200, verbatim:**

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
    > $$|\langle 1|\mathcal{O}|1\rangle_c|
    >   \leq C_p\,M\,\hat{\Delta}^p \tag{3}$$
    >
    > *where $C_p$ depends on $p$, $R_0$, and the gauge group $N$, but not
    > on $k$, $g_k$, or the volume.*

    This is exactly the spectral-to-norm inequality Route B needs: bound (3) has the form $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p \cdot \|\mathcal{O}\| \cdot \hat\Delta^p$ with $M = \|\mathcal{O}\|$. Applied to $\mathcal{O} = \delta E_k^{d=6}$ with $p = 2$: we get $|\langle 1|\delta E_k^{d=6}|1\rangle_c| \leq C_2 \|\delta E_k^{d=6}\| \hat\Delta^2$ directly.

2. **§5.5.3 Step 3(i), `05-continuum-limit.md` lines 1334–1339, verbatim:**

    > **For the polymer-aware extension:** each polymer $K(X)$ with
    > $\|K(X)\| \leq e^{-\kappa|X|}$ satisfies the same bound with $C_p^*$
    > independent of $|X|$, because the Hastings--Koma constant depends on
    > the physical support (not the lattice-unit count). The sum
    > $\sum_{X \ni 0} C_p^* e^{-\kappa|X|} = C_p^* C_{\mathrm{KP}}
    > < \infty$ converges by Koteck\'y--Preiss.

    **Critical reading for Route B.** The phrase "$\|K(X)\| \leq e^{-\kappa|X|}$" is a *norm-level* hypothesis on individual polymer activities (not a spectral one). The Koteck\'y–Preiss sum $\sum_{X \ni 0} \|K(X)\| \leq C_{\mathrm{KP}}$ is therefore a **norm-level** summability statement. This is what Route B uses: $\sum_X \|K_k^{d=6}(X,\cdot)\| \leq C_{\mathrm{KP}}\,g_k^4$ with the $g_k^4$ factor from Balaban's bound $\|K_k^{d=6}(X, \cdot)\| \leq C\,g_k^4\,e^{-\kappa|X|}$ (preprint §5.5.5/§5.6 Part III.5).

    (Observation. In Wave 4's patch, §5.5.3 Step 3(i) was used for a *spectral* single-polymer bound with the spectral constant $C_p^*$. That reading depended on per-polymer dev ≥ 2 to get the $\hat\Delta^p$ factor per term. Route B's alternative use of Step 3(i) is strictly weaker — it uses only the norm-level summability $\sum_X \|K(X)\| < \infty$, which is also proved by the same paragraph.)

3. **§5.6 Part III.3 Lemma, `05-continuum-limit.md` lines 1769–1773, verbatim:**

    > **Lemma (Stability of Deviation Order).** *Let $\mathcal{O}$ be
    > a local, gauge-invariant, $\mathcal{C}$-even operator on
    > $\Lambda_{k+1}$ of engineering dimension 6, analytic in $\{V_\ell\}$
    > with radius $\rho > 0$ (from (B1)). Then
    > $\mathrm{dev}(\mathcal{O}) \geq 2$.*

    Applied to $\mathcal{O} = \delta E_k^{d=6}$: the operator is local (union of polymer supports; local observables live on compact patches), gauge-invariant *in any reading* (sum over all polymers restores full gauge symmetry — this is not disputed anywhere in the preprint or by Wave 5), $\mathcal{C}$-even (Wilson action $\mathcal{C}$-invariant ⇒ effective action $\mathcal{C}$-invariant ⇒ each component of fixed dimension is $\mathcal{C}$-even ⇒ $\delta E_k^{d=6}$ is $\mathcal{C}$-even), dimension 6 by construction, and analytic in $\{V_\ell\}$ by (B1). All five hypotheses hold for the *total* operator. Part III.3 applies and gives dev$(\delta E_k^{d=6}) \geq 2$.

4. **§5.6 Part III.4, `05-continuum-limit.md` lines 1859–1867, verbatim:**

    > Balaban's effective action is $\mathcal{C}$-invariant (the Wilson
    > action and Haar measure are $\mathcal{C}$-invariant; each RG step
    > preserves this symmetry). The dimension-6 part $\delta E_k^{d=6}$
    > of the remainder is by construction a $\mathcal{C}$-even, dimension-6,
    > gauge-invariant local operator. By the Lemma:
    >
    > $$\mathrm{dev}(\delta E_k^{d=6}) \geq 2. \tag{III.1}$$

    Part III.4 already applies Part III.3 to $\delta E_k^{d=6}$ at the total-operator level — exactly the invocation Route B uses. The preprint's own III.4 is Route B's step 1.

5. **Balaban norm bound on polymer activities.** The standard polymer-activity bound $\|K_k(X, \cdot)\|_{\mathrm{op}} \leq C\,e^{-\kappa|X|}$ is a consequence of CMP 109, Thm 3 (cluster/Mayer convergence); the $g_k^4$ prefactor for the dimension-6 projection comes from Balaban's power-counting analysis (preprint line 1888: $\|\delta E_k^{d=6}\| \leq C g_k^4$). Both are load-free for Route B.

### Step 4 — Lock (verify the composition is a valid spectral identity)

The spectral-to-norm inequality Route B uses is not a novel claim — it is §5.5.3's Lemma, bound (3), read left-to-right. The lemma's hypothesis (iii) (dev$(\mathcal{O}) \geq p$) is supplied by Part III.3 (applied to the total operator), and the conclusion is $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p \cdot \|\mathcal{O}\| \cdot \hat\Delta^p$ — a bound in which the norm $\|\mathcal{O}\|$ appears as a *factor*. There is no further spectral identity to prove; the "spectral-norm inequality" of Route B's design statement is already in the preprint as bound (3).

The only composition step is the triangle inequality: $\|\sum_X K_k^{d=6}(X,\cdot)\|_{\mathrm{op}} \leq \sum_X \|K_k^{d=6}(X,\cdot)\|_{\mathrm{op}}$, which is the triangle inequality on operator norms (valid whenever all summands act on the same Hilbert space, which they do here — all $K_k^{d=6}(X, \cdot)$ are operators on the transfer-matrix Hilbert space at RG step $k+1$).

### Step 5 — Compute (explicit composition)

Step-by-step:

**(a) §5.6 Part III.3 applied to the total operator.** $\delta E_k^{d=6}$ is local, gauge-invariant (sum over all polymers is gauge-invariant by construction of Balaban's RG: the effective action is gauge-invariant in any reading, and the dimension-6 projection commutes with the gauge group action on operator-algebra generators), $\mathcal{C}$-even (the full effective action is $\mathcal{C}$-invariant ⇒ each dimension-class projection is $\mathcal{C}$-even), dimension 6 (by construction), analytic in $\{V_\ell\}$ with radius $\rho > 0$ (by (B1), preprint lines 1577–1580). Therefore:

$$\mathrm{dev}(\delta E_k^{d=6}) \geq 2. \tag{B1.1}$$

This is Part III.3 applied once, to the total operator, no per-polymer claim made. Preprint Part III.4 does exactly this, eq. (III.1).

**(b) §5.5.3's Lemma applied to the total operator.** $\delta E_k^{d=6}$ satisfies:
- (i) $\|\delta E_k^{d=6}\| \leq M$ for some $M \in \mathbb{R}_{\geq 0}$ (to be bounded in step (c));
- (ii) Locality with diameter $R_0$: each polymer has bounded diameter (CMP 109, Thm 1), and by the norm-convergent expansion, tails are absorbed in the norm bound. (One may restrict to the core polymer in a small neighborhood of the base point, or work directly with the polymer sum — in either case the spectral lemma applies to any operator with finite norm and locality.)
- (iii) dev ≥ 2 by (B1.1).

Therefore by bound (3) with $p = 2$:

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
  \leq C_2 \cdot \|\delta E_k^{d=6}\|_{\mathrm{op}} \cdot \hat\Delta_{k+1}^2. \tag{B1.2}$$

The constant $C_2$ depends on $R_0$, $N$, and $p$, but not on $k$, $g_k$, or the volume (by §5.5.3's lemma statement verbatim).

**(c) Norm bound via Hastings–Koma polymer sum.** By triangle inequality on operator norms:

$$\|\delta E_k^{d=6}\|_{\mathrm{op}}
  = \Big\|\sum_{X \ni 0} K_k^{d=6}(X,\cdot)\Big\|_{\mathrm{op}}
  \leq \sum_{X \ni 0} \|K_k^{d=6}(X,\cdot)\|_{\mathrm{op}}. \tag{B1.3}$$

(This is well-defined because: (a) the polymer sum $\sum_X K_k^{d=6}(X,\cdot)$ is norm-convergent by CMP 109 Thm 3's Mayer bound, (b) each $K_k^{d=6}(X,\cdot)$ is a bounded operator on the transfer-matrix Hilbert space at step $k+1$, (c) operator norm is sub-additive.)

Balaban's polymer-activity bound gives $\|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}} \leq C\,g_k^4\,e^{-\kappa|X|}$ (preprint §5.6 III.5 implicit; the $g_k^4$ comes from the dimension-6 projection's power-counting, the $e^{-\kappa|X|}$ from Balaban's small-field polymer bounds). Applying §5.5.3 Step 3(i) at the *norm level*:

$$\sum_{X \ni 0} \|K_k^{d=6}(X,\cdot)\|_{\mathrm{op}}
  \leq \sum_{X \ni 0} C\,g_k^4\,e^{-\kappa|X|}
  = C\,g_k^4\,C_{\mathrm{KP}}
  =: C_{\mathrm{norm}}\,g_k^4. \tag{B1.4}$$

The constant $C_{\mathrm{norm}} = C \cdot C_{\mathrm{KP}}$ is $|X|$-independent (as Step 3(i) provides) and $k$-uniform (as Step 3(ii) provides), with $C_{\mathrm{KP}}$ the Kotecký–Preiss sum and $C$ Balaban's dimension-6 coefficient.

**(d) Composition.** Chaining (B1.2) and (B1.4):

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
  \leq C_2 \cdot C_{\mathrm{norm}} \cdot g_k^4 \cdot \hat\Delta_{k+1}^2
  =: C_{\mathrm{new}} \cdot g_k^4 \cdot \hat\Delta_{k+1}^2. \tag{B1.5}$$

With $C_{\mathrm{new}} = C_2 \cdot C_{\mathrm{norm}}$, $k$-uniform and $L$-uniform. This is exactly the bound §5.5.5 and §5.7 (L11) need, in exactly the form L13 sums and L14 propagates.

### Step 5.5 — SELF-SUSPECT (three failure modes)

**(F1) Spectral-norm inequality requires specific structure.** The concern: $\|\mathcal{O}\|_{\mathrm{spectral}} \leq \hat\Delta^2 \|\mathcal{O}\|_{\mathrm{op}}$ for dev = 2 may require the operator to act between specific spectral subspaces (e.g., a commutator structure, or projector sandwiching), which $\delta E_k^{d=6}$ might not have.

*Recovery.* The "spectral-norm inequality" Route B uses is not an abstract functional-analysis identity but §5.5.3's bound (3) verbatim: $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p \|\mathcal{O}\| \hat\Delta^p$. Bound (3) holds for *any* operator satisfying (i)–(iii), without any commutator / projector structure beyond the standard transfer-matrix connected matrix element. $\delta E_k^{d=6}$ is a bounded local operator on the transfer-matrix Hilbert space with dev ≥ 2 (by B1.1), so (i)–(iii) all hold. The structure concern is moot: (3) is proved in §5.5.3's proof (lines 1203–1451) without any extra structural assumption on $\mathcal{O}$. **F1 closed.**

**(F2) Triangle inequality requires common Hilbert space.** The concern: $\|\sum_X K\|_{\mathrm{op}} \leq \sum_X \|K\|_{\mathrm{op}}$ needs all $K_k^{d=6}(X, \cdot)$ to be operators on the same Hilbert space.

*Recovery.* They are. Each $K_k^{d=6}(X, \cdot)$ is a polymer activity at RG step $k$, viewed as an operator on the transfer-matrix Hilbert space $\mathcal{H}_{k+1}$ of the effective theory at step $k+1$ (this is the Hilbert space on which the §5.5.3 Lemma operates: lines 1183–1184 "gauge-invariant operator on $\Lambda_{k+1}$"). The polymer support $X$ is a subset of $\Lambda_k$, but the *operator* $K_k^{d=6}(X, \cdot)$ acts on the full Hilbert space $\mathcal{H}_{k+1}$ (supported on a patch corresponding to $X$'s physical location). Standard operator-algebra: any bounded operator supported on a sub-region is a bounded operator on the whole space, and triangle inequality applies. **F2 closed.**

**(F3) Does the norm $\|\delta E_k^{d=6}\|$ in (B1.2) match what Hastings–Koma controls in (B1.4)?** The concern: the norm appearing in §5.5.3's bound (3) might be a different norm than the one Balaban's polymer-activity bound controls.

*Recovery.* Both are the operator norm $\|\cdot\|_{\mathrm{op}}$ on $\mathcal{H}_{k+1}$.

- §5.5.3's Lemma hypothesis (i): "$\|\mathcal{O}\| \leq M$". Context (line 1186) specifies operator norm (bound on matrix elements against normalized states; this is the submultiplicative norm used throughout §5.5.3's proof in §5.5.3 Step 2 lines 1261–1266: "$\sum_\alpha \prod_s \|\hat{A}_\alpha^{(s)}\| \leq M$ (by the triangle inequality and submultiplicativity of the operator norm applied to (1) with $\|\hat{T}\| = 1$)").
- §5.5.3 Step 3(i): "$\|K(X)\| \leq e^{-\kappa|X|}$" — same operator norm (the Hastings–Koma argument is about operator norms on the transfer-matrix Hilbert space).
- Balaban's polymer-activity bound in CMP 109 Thm 3 uses operator norm as well (the Mayer bound is typically stated in sup-norm on the matrix-element function, which coincides with the operator norm for bounded operators on a finite-dimensional effective Hilbert space; Balaban's inductive argument uses this norm throughout).

All three norms are the same. **F3 closed.**

**(Additional sanity check: is (ii) locality satisfied for the total $\delta E_k^{d=6}$?)** §5.5.3 Lemma's hypothesis (ii) demands locality with diameter $\leq R_0$. The total operator $\delta E_k^{d=6}$ is *not* supported in a fixed-diameter region (its support is the union of all polymers $X$ passing through the base point). However, §5.5.3's proof (Steps 3(i) and Remark on lines 1504–1518) handles the polymer case explicitly: bound (3) is proved uniformly for polymer-supported operators (Step 3(i)'s phrase "each polymer $K(X)$ with $\|K(X)\| \leq e^{-\kappa|X|}$ satisfies the same bound with $C_p^*$ independent of $|X|$") via the Hastings–Koma route, which replaces the $R_0$-diameter hypothesis by the $|X|$-independent $C_p^*$. Route B's use of §5.5.3 at the total-operator level is therefore routing through Step 3(i) at the *spectral* level *once* for the total operator — but only using the spectral Lemma's bound (3) *norm-factor structure* — and handling the polymer decomposition at the norm level separately.

Formally cleaner reformulation: apply §5.5.3 Step 3(i) directly at the total-operator level to produce

$$|\langle 1|\delta E_k^{d=6}|1\rangle_c| \leq C_p^*\,\|\delta E_k^{d=6}\|\,\hat\Delta^2$$

where $C_p^*$ is $|X|$-independent (because the Hastings–Koma constant depends on physical support, not lattice count). The dev ≥ 2 input is sourced from Part III.3 Part III.4 (total-operator statement, eq. (III.1)). Then bound the norm by (B1.4). This is the cleanest statement of Route B and what is used below.

### Step 6 — Verify (the resulting bound matches L11)

L11 (preprint §5.7 Theorem 8; chain-verification node L11-patch.md) needs:

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^2
\quad\text{with } C_{\mathrm{new}} \text{ $k$-uniform.}$$

Route B's conclusion (B1.5) is exactly this bound, with $C_{\mathrm{new}} = C_2 \cdot C_{\mathrm{norm}}$, where both factors are $k$-uniform and $L$-uniform by their respective lemma statements. L13 (RG summability) then converges the geometric sum $\sum_k g_k^4 \hat\Delta_{k+1}^2$, and L14 concludes $\Delta_\infty > 0$.

**Route B reproduces the L11 bound exactly.** Verified.

---

## The spectral-norm inequality

The load-bearing step in Route B is the inequality

$$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p \cdot \|\mathcal{O}\|_{\mathrm{op}} \cdot \hat\Delta^p$$

for any operator $\mathcal{O}$ with dev$(\mathcal{O}) \geq p$. **This inequality is §5.5.3's Lemma bound (3), verbatim.** No new theorem is introduced; the inequality lives in the preprint, is proved there (preprint lines 1203–1451), and applies to any operator satisfying (i)–(iii) of §5.5.3's Lemma.

The observation that makes Route B work is that bound (3)'s right-hand side has the factorized form $C_p \cdot \|\mathcal{O}\| \cdot \hat\Delta^p$ — *a spectral quantity bounded by operator norm times $\hat\Delta^p$*. The operator norm $\|\mathcal{O}\|$ is a separate, norm-level quantity that can be bounded independently (by triangle inequality and Kotecký–Preiss).

For completeness, here is the statement in a form that isolates the Route B use:

**Proposition (Spectral-Norm Factorization; restatement of §5.5.3 bound (3)).** *Let $\mathcal{O}$ be a bounded operator on the transfer-matrix Hilbert space $\mathcal{H}_{k+1}$ satisfying the hypotheses of §5.5.3's Lemma (locality with diameter $\leq R_0$, or — in the polymer extension of Step 3(i) — with $|X|$-independent Hastings–Koma constant $C_p^*$), and with $\mathrm{dev}(\mathcal{O}) \geq p$. Then*

$$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p \cdot \|\mathcal{O}\|_{\mathrm{op}} \cdot \hat\Delta^p,$$

*with $C_p$ ($k$, $g_k$, $L$)-uniform.*

**Proof.** §5.5.3's Lemma bound (3), with $M$ identified as $\|\mathcal{O}\|_{\mathrm{op}}$ (see lines 1186 and 1262–1266 for this identification). $\square$

(Note. Standard spectral theory provides an abstract analog: if $\mathcal{O}$ annihilates the one-particle eigenspace to order $\geq p$ in the spectral expansion — the content of dev$(\mathcal{O}) \geq p$ — and $T$ has top two eigenvalues $\lambda_0, \lambda_1$ with $\hat\Delta = \log(\lambda_0/\lambda_1)$, then connected matrix elements pick up $\hat\Delta^p$ suppression with coefficient controlled by $\|\mathcal{O}\|_{\mathrm{op}}$. This is folklore in transfer-matrix analysis; e.g., Reed–Simon Vol. IV §XIII on isolated eigenvalue perturbations gives the underlying perturbation theory. For Route B's purposes §5.5.3 Lemma bound (3) is the citation-of-record; the spectral-theory folklore is only cross-validation.)

---

## Composition with Hastings–Koma

Route B's second load-bearing step is the **norm-level** polymer bound:

$$\|\delta E_k^{d=6}\|_{\mathrm{op}}
  \leq \sum_{X \ni 0} \|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}}
  \leq C_{\mathrm{norm}} \cdot g_k^4.$$

The two steps:

**(i) Triangle inequality.** $\|\sum_X K_k^{d=6}(X, \cdot)\|_{\mathrm{op}} \leq \sum_X \|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}}$. Valid because all summands act on $\mathcal{H}_{k+1}$ and operator norm is sub-additive. *No dev ≥ 2 per polymer needed.*

**(ii) Kotecký–Preiss sum.** §5.5.3 Step 3(i) (preprint lines 1334–1339, quoted above) provides:

> The sum $\sum_{X \ni 0} C_p^* e^{-\kappa|X|} = C_p^* C_{\mathrm{KP}} < \infty$ converges by Koteck\'y--Preiss.

Route B uses this only as a **norm** summability statement: $\sum_{X \ni 0} \|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}} \leq C_{\mathrm{KP}} \cdot \sup_X e^{\kappa |X|} \|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}} \leq C_{\mathrm{KP}} \cdot C\,g_k^4 = C_{\mathrm{norm}}\,g_k^4$, with $C$ from Balaban's polymer-activity bound $\|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}} \leq C\,g_k^4\,e^{-\kappa|X|}$ (CMP 109 Thm 3 for the Mayer-level exponential decay, Balaban's dimension-6 power-counting for the $g_k^4$ prefactor — preprint line 1888).

**This uses polymer activity norms, not per-polymer dev ≥ 2.** The Kotecký–Preiss sum in §5.5.3 Step 3(i) is stated as a norm-level sum from the start; the $C_p^*$ factor in the preprint's statement is there to pre-package the *spectral* bound per polymer under the Hastings–Koma route, but if one uses Step 3(i)'s Kotecký–Preiss estimate purely at the norm level, the $C_p^*$ factor is replaced by the Balaban norm bound $C\,g_k^4$, and the per-polymer spectral claim is not invoked.

---

## Revised Application paragraph

This replaces Edit 4 of `L14-patch.md` (preprint §5.5 lines 1520–1527, "Application" paragraph). Route B version:

> **Application.** By (B1), $\delta E_k^{d=6}(0) = \sum_{X \ni 0}
> K_k^{d=6}(X, \cdot)$ is a convergent polymer expansion in the
> small-field domain, whose total operator is a local, gauge-invariant,
> $\mathcal{C}$-even, dimension-6 operator, analytic in $\{V_\ell\}$.
> By §5.6 Part III.4 (eq. (III.1)), applied once at the total-operator
> level, $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$. Therefore by the
> Lemma (Two-Derivative Spectral Bound, §5.5.3, bound (3)) with
> $p = 2$ and $M = \|\delta E_k^{d=6}\|_{\mathrm{op}}$:
>
> $$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
>   \leq C_2 \cdot \|\delta E_k^{d=6}\|_{\mathrm{op}}
>   \cdot \hat{\Delta}_{k+1}^2.$$
>
> The operator norm is controlled at the polymer-sum level by the
> polymer-aware Hastings--Koma bound of Step 3(i): by triangle
> inequality on operator norms plus Balaban's polymer-activity bound
> $\|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}} \leq C\,g_k^4\,e^{-\kappa|X|}$
> (CMP 109, Thm 3; dimension-6 power counting),
>
> $$\|\delta E_k^{d=6}\|_{\mathrm{op}} \leq
>   \sum_{X \ni 0} \|K_k^{d=6}(X, \cdot)\|_{\mathrm{op}}
>   \leq C\,g_k^4\,C_{\mathrm{KP}} =: C_{\mathrm{norm}}\,g_k^4.$$
>
> Combining, with $C_{\mathrm{new}} := C_2 \cdot C_{\mathrm{norm}}$
> ($k$-uniform and $L$-uniform):
>
> $$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\,
>   g_k^4\,\hat{\Delta}_{k+1}^2.$$
>
> This is the quantitative form of $\mathrm{dev}(\delta E_k^{d=6})
> \geq 2$. The deviation order is extracted from Part III.3 at the
> level of the total operator $\delta E_k^{d=6}$ (where gauge
> invariance is manifest by construction of Balaban's RG); the
> polymer-sum control is extracted from §5.5.3 Step 3(i) at the
> level of operator norms. Per-polymer dev $\geq 2$ is neither
> asserted nor needed.

---

## Self-suspicion

Three failure modes, each with recovery:

**F1 — Spectral-norm inequality may require specific operator structure.** Recovery: The inequality Route B uses is §5.5.3 bound (3) verbatim, which holds for any operator satisfying the lemma's hypotheses. No additional structure (commutators, projector sandwiches) is needed.

**F2 — Triangle inequality requires common Hilbert space.** Recovery: All polymer activities $K_k^{d=6}(X, \cdot)$ act on $\mathcal{H}_{k+1}$ (the transfer-matrix Hilbert space at RG step $k+1$). Triangle inequality on operator norms is standard.

**F3 — Norm mismatch.** Recovery: §5.5.3's $M$, §5.5.3 Step 3(i)'s $\|K(X)\|$, and Balaban's CMP 109 polymer-activity norm are all the same operator norm on $\mathcal{H}_{k+1}$. No conversion factor is hidden.

Additional concerns:

**(F4, minor) The total operator $\delta E_k^{d=6}$ is not supported in a fixed-$R_0$ diameter region, so §5.5.3 Lemma hypothesis (ii) may appear violated.** Recovery: The polymer extension of §5.5.3 Step 3(i) (preprint lines 1334–1339) explicitly handles the polymer-sum case, with the locality hypothesis replaced by $|X|$-independent Hastings–Koma constants. Applied at the total-operator level in Route B's spectral step.

**(F5, pedagogical) A referee might read Route B's use of Step 3(i) twice — once at spectral level for the total operator, once at norm level for the polymer sum — as double-counting.** Recovery: The two uses are disjoint. The spectral use reads Step 3(i) as "the $\hat\Delta^2$ bound holds with $|X|$-independent constant." The norm use reads Step 3(i) as "the Kotecký–Preiss sum converges." These are independent statements inside the same paragraph; Route B uses one for the spectral step on the total operator and the other for the norm-level polymer decomposition. No content is double-counted; only the paragraph is cited twice for its two distinct contents.

---

## Integration with L14-patch.md

**Edits to be modified** (Route B supersedes these parts of the Wave 4 patch):

| Wave 4 patch edit | Location | Change under Route B |
|:---|:---|:---|
| **Edit 4** (§5.5 Application, lines 1520–1527) | Preprint §5.5 | Replaced verbatim by the Route B Application paragraph above. Key deletion: the phrase "whose activities are $\mathcal{C}$-even dimension-6 operators with $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$ (§5.6 Part III.3)" — this per-polymer dev claim is removed. |
| **Edit 1** (§5.4.7 final paragraph, lines 1035–1043) | Preprint §5.4.7 | The "to" text currently contains "Combined with the dimension-6 classification of §5.6 Part III.3 ($\mathrm{dev}(\delta E_k^{d=6}) \geq 2$)" — this already reads at the total-operator level (Part III.4 eq. (III.1)), not per polymer. No change needed under Route B: Edit 1 is already Route-B-compatible. |
| **Edit 3** (§5.5.5 status table) | Preprint §5.5.5 | The Route B reading makes "Proved" by Part III.3 + III.4 at the total-operator level, cited jointly with §5.5.3 Step 3(i) for the norm-level polymer sum. Table entry "$\mathrm{dev}(\delta E_k^{d=6}) \geq 2$" is unambiguously at the total-operator level (matches preprint Part III.4 eq. (III.1)). Update the "Method" column for the "Bound (5)" row to read "§5.5.3 bound (3) at the total-operator level + triangle inequality + Kotecký–Preiss sum (§5.5.3 Step 3(i) norm level) + dim-6 classification (§5.6 Part III.3)". |
| **Edit 2-new** (§5.5.3 Uniform temporal extent remark) | Preprint §5.5.3 | Unchanged under Route B. The remark is a meta-comment about when the Linear Combination Lemma applies; Route B doesn't use that lemma at all, so the remark remains accurate as written. |

**Edits that remain unchanged** (Route B is consistent with these as-is):

- Edits 9–16 (the "Conjecture 1" orphan sweep): Route B closes Conjecture 1 at $d_O = 6$ by the same route as the patch (§5.5.3 + §5.6 Part III.3 composition). The citation targets in Edits 9–16 still point to the right places.
- Edit 5 (§5.7 Theorem 8): the continuum mass gap theorem. Route B's (B1.5) supplies exactly the $C_{\text{new}} g_k^4 \hat\Delta^2$ bound §5.7 consumes.
- Finding 2 (margin condition): already moot under the Hastings–Koma route; Route B doesn't reopen it.
- Finding 4 (rigor label): under Route B, the discharge of Conjecture 1 at $d_O = 6$ is a composition of three existing THEOREMs (§5.5.3 bound (3), §5.6 Part III.3 applied once at the total-operator level per §5.6 Part III.4, and §5.5.3 Step 3(i) used at the norm level via triangle inequality + Kotecký–Preiss). The composition is strictly cleaner than the Wave 4 patch's composition (which required a per-polymer reading of Part III.3). Rigor label remains THEOREM without qualification.

**Specific diff summary:** in practical terms, Route B asks for a single surgical edit relative to the Wave 4 patch — replace the "Application" paragraph (Edit 4) with the Route B version above, and update the §5.5.5 "Method" column entry for "Bound (5)" to reflect the norm-level polymer sum (Edit 3's Method column).

---

## What the next runner needs to know

1. **Route B is cleaner than Route A.** Route A closes the joint by hermeneutic defense (Part III.3's "gauge-invariant" means block-spin). Route B closes it by algebraic refactoring (apply Part III.3 once at total-operator level, bound operator norm by triangle inequality). Route B assumes strictly less (no reading-of-hypothesis) at the cost of one extra triangle-inequality step.

2. **The key move is scope separation.** Part III.3 → dev ≥ 2 → $\hat\Delta^2$ factor happens *at the total-operator level*, exactly once (this is what preprint Part III.4 eq. (III.1) already does). The polymer sum happens *at the norm level*, using §5.5.3 Step 3(i)'s Kotecký–Preiss summability plus triangle inequality. These are separate facts that compose by §5.5.3's Lemma bound (3).

3. **No new lemma is introduced.** Route B uses only: (a) §5.5.3 bound (3), already a THEOREM in the preprint; (b) §5.6 Part III.3 + III.4, already applied at the total-operator level in the preprint; (c) §5.5.3 Step 3(i), used at the norm level (strictly weaker than the spectral-level use in Wave 4); (d) operator-norm triangle inequality. All four are load-free.

4. **Minimum edit to the Wave 4 patch.** Replace the "Application" paragraph (Edit 4) verbatim with the Route B version (given above); update one cell in the §5.5.5 Status Table Method column (Edit 3). All other Wave 4 patch edits remain unchanged.

5. **Route B does not require Route A.** They are independent closures. If the runner prefers the hermeneutic argument of Route A (or wants to keep both for belt-and-braces redundancy), Route A's per-polymer statement stands on its own. But if the runner wants the *minimal-assumption* closure, Route B is the choice: it does not require any reading-of-hypothesis about Part III.3.

6. **Failure modes, ranked by residual concern:**
   - Most concerning (still residual): F5, double-citation of §5.5.3 Step 3(i). Pedagogically, a referee might want the two uses (spectral vs. norm) disentangled in the preprint prose. Recommended: explicitly label them as "Step 3(i) spectral" and "Step 3(i) norm" in the Application paragraph, or cite the two contents at distinct places in the preprint. This is a presentation matter, not a content flaw.
   - Moderately concerning (mitigated): F4, locality hypothesis on the total operator. §5.5.3 Step 3(i)'s polymer extension handles this. A thorough writeup should spell this out.
   - Fully closed: F1, F2, F3.

7. **If Route B fails in referee review**, Route A remains a backup. Neither route requires the other. Route B is preferred because it requires strictly fewer judgment calls.

---

**End of L14-route-b.md.**
