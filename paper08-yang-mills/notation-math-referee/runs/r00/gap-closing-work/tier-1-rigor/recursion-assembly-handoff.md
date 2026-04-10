# Recursion Assembly and Cluster / Balaban Handoff

**Gap ID:** Tier 1 / Steps 1.4, 1.5, 1.6, 1.7 + Gap C3 (outer recursion assembly and the cluster-expansion / Balaban-RG handoff at $k=0$ within each bare theory).
**Date:** 2026-04-08.
**Scope:** Assemble the K-uniform inputs of Tier 1 Steps 1.1–1.3 into the outer recursion $C_{K+1} = C_K/4 + C_{\mathrm{new}}(K) + O(g_K^2 C_K)$ under the corrected K/k notation, state the cluster / Balaban handoff as a lemma, and derive continuum mass gap positivity from the resulting convergence sum.
**Status:** **Conditional-assembly.** The assembly itself is rigorous modulo its three explicit inputs. Two of those inputs (K-uniform cluster expansion; K-uniform Balaban analyticity radius) are produced by the parallel bookkeeping agent; the third (K-uniform spectral lemma via Lieb-Robinson, Step 1.3) is hard and may be only partial.
**Dependencies:** Tier 0 notation cleanup (`../tier-0-notation/notation-patch.md`); Tier 1 bookkeeping (`k-uniform-cluster-expansion.md`, `k-uniform-balaban-radius.md`); Tier 1 spectral reformulation (`k-uniform-spectral-lemma.md`).

Notation throughout: $K \in \mathbb{N}$ = outer bare-refinement index ($a_0(K) = a^* \cdot 2^{-K}$); $k \in \mathbb{N}$ = inner Balaban block-spin index within a fixed bare theory ($a_k^{(K)} = 2^k a_0(K)$); $\hat\Delta_K := a_0(K)\,\Delta_{\mathrm{phys}}$; $\hat\Delta_k^{(K)} := a_k^{(K)}\,\Delta_{\mathrm{phys}} = 2^{k-K}\,a^*\,\Delta_{\mathrm{phys}}$. Convention as in Tier 0 patch §1.

---

## Section 1 — The outer recursion (Steps 1.4 / 1.5)

### 1.1 Kinematic identity between bare theories

Bare theories $K$ and $K+1$ are related by refinement $a_0(K+1) = a_0(K)/2$. The physical mass gap $\Delta_{\mathrm{phys}}$ is the same in both theories (it is the continuum target that the sequence approaches). Therefore
$$\hat\Delta_{K+1} = a_0(K+1)\,\Delta_{\mathrm{phys}} = \tfrac{1}{2}\,a_0(K)\,\Delta_{\mathrm{phys}} = \tfrac{1}{2}\,\hat\Delta_K,$$
and squaring,
$$\boxed{\;\hat\Delta_{K+1}^{\,2} \;=\; \tfrac{1}{4}\,\hat\Delta_K^{\,2}\;} \tag{1.1}$$
This is a **kinematic** identity: it contains no dynamics, only a unit change. It is **not** a Balaban inner step, which runs the *opposite* direction ($\hat\Delta_{k+1}^{(K)} = 2\,\hat\Delta_k^{(K)}$) and comes with dynamical corrections of order $g_k^4$.

### 1.2 Inductive hypothesis at bare scale $K$

Let $E^{(K)}$ denote the IR effective remainder of bare theory $K$, i.e., the $k \to \infty$ output of Balaban's inner flow (Section 5.1.3 of the preprint) started at bare scale $a_0(K)$. Let $|1\rangle^{(K)}$ be the one-particle state of the IR-limit transfer matrix of bare theory $K$. The inductive hypothesis is
$$|\langle 1|E^{(K)}(0)|1\rangle_c^{(K)}|\;\leq\;C_K\,g_K^4\,\hat\Delta_K^{\,2}, \tag{1.2}$$
where $g_K := g_0(K)$ is the bare coupling of theory $K$ (up to $O(g_K^6)$ corrections from the inner flow, which are absorbed into $C_K$).

### 1.3 Passage to bare scale $K+1$

Refining the bare theory does not change the *physics*; it only changes the bookkeeping. The old remainder $E^{(K)}$, pulled forward to theory $K+1$ via the bare-refinement map, becomes an operator $E^{(K)\downarrow}$ whose *physical* matrix elements differ from those of $E^{(K)}$ by $O(g_K^2)$ (coefficient drift under bare-coupling running; see preprint §5.4.3). Write
$$|\langle 1|E^{(K)\downarrow}(0)|1\rangle_c^{(K+1)}|\;\leq\;C_K\,g_K^4\,\hat\Delta_K^{\,2}\,(1 + O(g_K^2)).$$
Substitute the kinematic identity (1.1):
$$|\langle 1|E^{(K)\downarrow}(0)|1\rangle_c^{(K+1)}|\;\leq\;\tfrac{C_K}{4}\,g_K^4\,\hat\Delta_{K+1}^{\,2}\,(1 + O(g_K^2)). \tag{1.3}$$
This is the "$1/4$ contraction." It is pure unit conversion: the same physical quantity, expressed relative to the smaller reference scale $\hat\Delta_{K+1}^2$, has a four-times-smaller dimensionless coefficient.

Passing from bare theory $K$ to bare theory $K+1$ also generates new operators. These are operators that exist in the Balaban inner flow of theory $K+1$ but not in that of $K$ — schematically, they are the modes whose momenta lie between $\pi/a_0(K)$ and $\pi/a_0(K+1) = 2\pi/a_0(K)$. Their one-particle form factor, bounded under Tier 1 Step 1.3 (spectral lemma reformulated in physical units), gives
$$|\langle 1|\delta E(0)|1\rangle_c^{(K+1)}|\;\leq\;C_{\mathrm{new}}(K)\,g_K^4\,\hat\Delta_{K+1}^{\,2}. \tag{1.4}$$
The $K$-dependence of $C_{\mathrm{new}}(K)$ sits in the spectral-lemma constant $C_p(K)$, the Balaban analyticity radius $\rho(K)$, and the cluster-expansion starting constant.

### 1.4 The recursion

Adding (1.3) and (1.4),
$$|\langle 1|E^{(K+1)}(0)|1\rangle_c^{(K+1)}|\;\leq\;\left(\tfrac{C_K}{4} + C_{\mathrm{new}}(K)\right)\,g_K^4\,\hat\Delta_{K+1}^{\,2}\,(1 + O(g_K^2)).$$
Convert bare couplings via $g_K^4 = g_{K+1}^4\,(1 + O(g_K^2))$ (bare-scale running under $g_{K+1}^2 = g_K^2 - b_0\,g_K^4\,\ln 2 + O(g_K^6)$):
$$|\langle 1|E^{(K+1)}(0)|1\rangle_c^{(K+1)}|\;\leq\;C_{K+1}\,g_{K+1}^4\,\hat\Delta_{K+1}^{\,2},$$
with
$$\boxed{\;C_{K+1}\;=\;\tfrac{C_K}{4}\;+\;C_{\mathrm{new}}(K)\;+\;O(g_K^2\,C_K)\;} \tag{1.5}$$
This matches the Tier 0 notation patch (Patch 2.4) and the §5.4.5 recursion box *read under corrected indices*. The $O(g_K^2\,C_K)$ term encodes both the Kato cross-term $A_2$ and the coupling-running conversion.

### 1.5 Inputs to the recursion

The recursion (1.5) is a numeric statement once three inputs are supplied:

1. **$C_K$.** Starting value: $C_0$, from the cluster expansion at bare scale $K = 0$ (Theorem 4 of §4.4; K-uniformity at $K = 0$ is automatic because there is no limit to take). Subsequent values: by recursion (1.5).
2. **$C_{\mathrm{new}}(K)$.** From the K-uniform single-step bound on new operators generated at bare scale $K$. By Tier 1 Step 1.3 (Lieb-Robinson reformulation of the spectral lemma), $C_{\mathrm{new}}(K) \leq C_*$ uniformly in $K$, where $C_*$ is a physical constant depending on $N$, $r_3$, and $\Lambda_{\mathrm{QCD}}$ but not on $K$.
3. **$g_K$.** From bare-scale running $g_K^2 \sim 1/(b_0 K \ln 2)$ for large $K$, $b_0 = 11N/(48\pi^2)$.

The K-uniformity of input (2) is the core Tier 1 requirement. It is proved (modulo its own conditionality) in the sister document `k-uniform-spectral-lemma.md`.

---

## Section 2 — Cluster expansion / Balaban handoff at $k=0$ (Steps 1.5 / 1.6)

### 2.1 Setup

Fix a bare theory $K$. Inside this theory, the inner index $k$ runs from $k=0$ (the bare lattice at spacing $a_0(K)$) to $k = \infty$ (the IR effective theory). The construction of $C_K$ — the output of the inner flow used in (1.2) — requires a **starting condition** $C_K(k=0)$ at the bare scale, followed by a **propagation rule** that gives $C_K$ from $C_K(k=0)$. The two are furnished by different tools:

- **Starting condition $C_K(k=0)$:** cluster expansion of Section 4 at bare scale $a_0(K)$.
- **Propagation $k = 0 \to \infty$:** Balaban's block-spin RG with polymer activities $K_k^{(K)}(X, V)$, bounded by $e^{-\kappa|X|}$ uniformly in the inner step $k$ and (by Tier 1 Step 1.2) in the outer bare scale $K$.

The handoff is the statement that the cluster-expansion output is a *valid input* for Balaban's polymer expansion at $k=0$.

### 2.2 Cluster-Balaban Handoff Lemma

**Lemma (Cluster–Balaban Handoff).** *Fix a bare theory $K$ with $a_0(K) \gg r_3$ (automatic for any $K$ with $K \leq K_*$, where $K_*$ is the "bare cluster-convergent" threshold of Tier 1 Step 1.1; see Remark 2.3 below for $K > K_*$). Assume:*

*(H1) K-uniform cluster expansion. The cluster expansion of Theorem 2 / Theorem 4 of Section 4 converges for bare theory $K$ at a rate $\kappa_{\mathrm{cl}}(K) \geq \kappa_{\mathrm{cl}}^* > 0$, with $\kappa_{\mathrm{cl}}^*$ a physical (K-uniform) constant. This is the output of Tier 1 Step 1.1 (`k-uniform-cluster-expansion.md`).*

*(H2) K-uniform Balaban analyticity radius. Balaban's polymer activities at inner step $k$ of bare theory $K$ satisfy $|K_k^{(K)}(X, V)|\leq e^{-\kappa_{\mathrm{B}}\,|X|}$ with $\kappa_{\mathrm{B}} > 0$ independent of both $k$ and $K$. This is the output of Tier 1 Step 1.2 (`k-uniform-balaban-radius.md`).*

*(H3) Rate compatibility. $\kappa_{\mathrm{cl}}^* \geq \kappa_{\mathrm{B}}$.*

*Then the cluster-expansion bound at bare scale $a_0(K)$,*
$$|K_{\mathrm{cluster}}^{(K)}(X)|\;\leq\;e^{-\kappa_{\mathrm{cl}}^*\,|X|}, \tag{2.1}$$
*is a valid initial condition for Balaban's polymer expansion at $k=0$: the bound $|K_0^{(K)}(X, V)|\leq e^{-\kappa_{\mathrm{B}}\,|X|}$ holds with the same $\kappa_{\mathrm{B}}$ used in Balaban's inner flow. In particular, $C_K(k=0) \leq C_0^{\mathrm{cl}}$ uniformly in $K$, where $C_0^{\mathrm{cl}}$ is a physical constant depending on $N$ and the initial cluster constants of Theorem 4.*

*Proof sketch.* The cluster expansion produces activities satisfying the Kotecký–Preiss criterion (Theorem 3, preprint §4.3): $\sum_{\mathcal{C} \ni x}|\phi(\mathcal{C})|\,e^{\alpha|\mathcal{C}|} \leq \alpha$ with $\alpha \geq \kappa_{\mathrm{cl}}^*$. The exponential weight $e^{-\alpha|\mathcal{C}|}$ in the cluster convergence is equivalent, after grouping clusters by their support $X$, to a bound $|K_{\mathrm{cluster}}^{(K)}(X)| \leq e^{-\alpha|X|}$ on the support-indexed polymer activities (Salmhofer 1998 §2.2 for the polymer / cluster dictionary, Balaban CMP 109 §3 for the analogous form on the Balaban side).

By (H3), $\alpha \geq \kappa_{\mathrm{cl}}^* \geq \kappa_{\mathrm{B}}$, so the cluster bound majorises Balaban's requirement. Moreover, the "block field $V$" dependence of Balaban's polymer activity factorises in the form $K_0^{(K)}(X, V) = K_{\mathrm{cluster}}^{(K)}(X)\cdot Q(X, V)$, where $Q(X, V)$ is bounded by $1$ on Balaban's small-field domain $\Omega_s$ (by the definition of Balaban's polymer activities, CMP 109 §3; small-field control from §5.6 Part I). Therefore
$$|K_0^{(K)}(X, V)|\;\leq\;|K_{\mathrm{cluster}}^{(K)}(X)|\;\leq\;e^{-\kappa_{\mathrm{cl}}^*|X|}\;\leq\;e^{-\kappa_{\mathrm{B}}|X|}.$$
The activity bound is in the form required by Balaban's inductive convergence theorem, so the inner RG can be started at $k = 0$. The resulting starting constant $C_K(k=0)$ is bounded by the cluster-expansion output, which is a finite physical constant by (H1).

$\square$

### 2.3 On hypotheses

(H1) and (H2) are the main substantive inputs; they are *not* proved here. (H3) is a quantitative compatibility check between the two rates. Numerically, Balaban's $\kappa_{\mathrm{B}}$ is determined by the block-spin construction and is $O(1)$ in physical units (see Balaban CMP 109 §3, Dimock 2011 Thm 3.1); the cluster-expansion rate $\kappa_{\mathrm{cl}}^*$ is determined by Theorem 4, $\kappa_{\mathrm{cl}}(K) \sim m_1 a_0(K)/6$ in lattice units $\to$ $\kappa_{\mathrm{cl}}^* = m_1/(6\Lambda_{\mathrm{UV}})$ in physical units after the Step 1.1 reformulation, where $m_1 = 2\sqrt{N}/r_3$. For $N = 3$ at $a_0(K) \sim 10^{-16}$ m, this is a wide margin, and (H3) is automatic.

**Remark (bare cluster-convergent range).** The cluster expansion of Theorem 4 requires $a_0(K) \gg r_3$ to converge (Section 4.4, "Scope and Limitations"). As $K \to \infty$, $a_0(K) \to 0$, and eventually $a_0(K) < r_3$; at that point the cluster expansion "fails" in the naive sense. However, for the recursion assembly we do not need cluster convergence at *every* $K$: we only need a finite $C_K(k=0)$ that is K-uniform. Tier 1 Step 1.1 reformulates the cluster expansion in physical units using the Lieb-Robinson radius instead of lattice-unit balls; under that reformulation the starting constant $C_K(k=0)$ is defined and bounded for *all* $K$, including $K \to \infty$. This is the content of Step 1.1 and is assumed in (H1).

---

## Section 3 — The "first few inner steps" non-perturbatively (Step 1.7)

The §5.7 Remark 1 informally says: "at $k = 0, 1, 2$ where $g_k^4 = O(1)$, first-order perturbation is not a priori justified. These finitely many steps are handled non-perturbatively via the cluster expansion." Under the corrected K/k separation, this statement is about the *inner* index $k$ at *fixed* bare theory $K$. Here is the rigorous version.

### 3.1 The crossover inner step $k_0(K)$

Fix a bare theory $K$. Balaban's inner flow produces $g_k^{(K)}$ via the running
$$(g_{k+1}^{(K)})^2 = (g_k^{(K)})^2 - b_0 (g_k^{(K)})^4 \ln 2 + O((g_k^{(K)})^6),\qquad g_0^{(K)} = g_K.$$
For the one-loop form-factor bound of Theorem 7 to be justified (§5.1.6), we need $(g_k^{(K)})^4 \ll 1$. Define
$$k_0(K)\;:=\;\min\left\{k \geq 0 \;\big|\; (g_k^{(K)})^4 \leq \epsilon_*\right\},$$
where $\epsilon_*$ is a small universal constant (e.g., $\epsilon_* = 10^{-2}$). Solving the one-loop running $g_k^2 = g_K^2 / (1 + b_0 g_K^2 k \ln 2)$ gives
$$k_0(K)\;=\;\max\!\left(0,\; \left\lceil \frac{1}{b_0 \ln 2}\left(\frac{1}{\epsilon_*^{1/2}} - \frac{1}{g_K^2}\right)\right\rceil\right). \tag{3.1}$$
For $g_K = O(1)$ (e.g., $g_K = 1$), $k_0(K) = O(10^2)$ with the constants for $N = 3$. For $g_K \ll 1$ (e.g., $K$ large on the AF trajectory), $k_0(K) = 0$: the perturbative regime starts immediately.

### 3.2 Non-perturbative bound on the first $k_0$ inner steps

On $k \in \{0, 1, \ldots, k_0(K) - 1\}$, the one-loop Theorem 7 estimate is not a priori justified because $(g_k^{(K)})^4$ is not small. Replace it by the cluster-expansion / polymer bound of the Handoff Lemma (§2.2):

**Claim.** For $k < k_0(K)$, the polymer activities $K_k^{(K)}(X, V)$ satisfy $|K_k^{(K)}(X, V)| \leq e^{-\kappa_{\mathrm{B}}|X|}$ and the form-factor contribution at inner step $k$ is bounded by a K-uniform constant:
$$|\langle 1|E_k^{(K)}(0)|1\rangle_c^{(K)}| \leq C_{\mathrm{np}}\,\hat\Delta_{k+1}^{(K)2}, \tag{3.2}$$
where $C_{\mathrm{np}}$ is a physical constant (depending on $N$, $r_3$) arising from the cluster-expansion / polymer bound of the Handoff Lemma, and *not* containing an explicit $g_k^4$ factor (because the perturbative identity is not used).

*Proof sketch.* On the Balaban polymer side, the form-factor bound reduces, via the polymer expansion of §5.5.3, to the sum $\sum_X |K_k^{(K)}(X, V)|\,|X|^2$. By (H2), $|K_k^{(K)}(X, V)| \leq e^{-\kappa_{\mathrm{B}}|X|}$, so $\sum_X |K_k^{(K)}(X, V)|\,|X|^2 \leq c(\kappa_{\mathrm{B}}) < \infty$. This gives (3.2) with $C_{\mathrm{np}} = c(\kappa_{\mathrm{B}})$. The key point is that the activity bound $e^{-\kappa_{\mathrm{B}}|X|}$ holds for *all* $k$, including the first few where $g_k$ is large, because it comes from Balaban's polymer convergence criterion (which does not use the smallness of $g_k$ beyond the initial analyticity radius, which is K-uniform by Tier 1 Step 1.2). $\square$

### 3.3 Bounded total contribution of the first $k_0$ inner steps

The form-factor contributions over $k = 0, \ldots, k_0(K) - 1$ sum to
$$\sum_{k=0}^{k_0(K) - 1}|\langle 1|E_k^{(K)}(0)|1\rangle_c^{(K)}|\;\leq\;C_{\mathrm{np}}\,\sum_{k=0}^{k_0(K)-1}\hat\Delta_{k+1}^{(K)2}.$$
With $\hat\Delta_k^{(K)2} = 4^{k-K}\,(a^*\Delta_{\mathrm{phys}})^2$,
$$\sum_{k=0}^{k_0(K)-1}\hat\Delta_{k+1}^{(K)2}\;=\;(a^*\Delta_{\mathrm{phys}})^2\,4^{-K}\,\sum_{k=1}^{k_0(K)}4^{k}\;\leq\;(a^*\Delta_{\mathrm{phys}})^2\,4^{-K}\cdot\tfrac{4}{3}\cdot 4^{k_0(K)}.$$
This is bounded by
$$C_{\mathrm{np}}\cdot(a^*\Delta_{\mathrm{phys}})^2\cdot\tfrac{4}{3}\cdot 4^{\,k_0(K)-K}. \tag{3.3}$$
For this contribution to be bounded — i.e., absorbable into $C_K(k=0) = C_0^{\mathrm{cl}}$ — we need $k_0(K) - K$ to not grow. By (3.1), $k_0(K)$ depends *only on $g_K$*, and $g_K^2$ decreases with $K$, so $k_0(K)$ *decreases* with $K$. In particular, for $K$ large enough that $g_K^4 < \epsilon_*$, $k_0(K) = 0$ and the contribution (3.3) is empty. For small $K$ where $k_0(K)$ is $O(1)$ in $K$, the contribution is bounded by a fixed constant.

The conclusion: the "first few inner steps" of the inner flow of each bare theory contribute a bounded total, absorbable into $C_K(k=0)$, with no $K$-dependence that could blow up. This is what §5.7 Remark 1 said informally.

---

## Section 4 — Convergence and continuum mass gap (Step 1.4 final)

### 4.1 Fixed point of the outer recursion

Assume Tier 1 Step 1.3 delivers $C_{\mathrm{new}}(K) \leq C_*$ uniformly in $K$. Then (1.5) gives
$$C_{K+1}\;\leq\;\tfrac{C_K}{4}\;+\;C_*\;+\;\text{(sub-leading)}. \tag{4.1}$$
The recursion $C_{K+1} = C_K/4 + C_*$ has fixed point $C_{**} = 4 C_*/3$, approached geometrically:
$$C_K = C_{**}\;+\;(C_0 - C_{**})\cdot 4^{-K}.$$
So $C_K \leq \max(C_0, C_{**})$ for all $K \geq 0$. Including the sub-leading $O(g_K^2 C_K)$ term gives at most polynomial growth $C_K \lesssim K^\gamma$ on top of the fixed point (as in §5.4.6), which does not affect the conclusion of §4.2 below.

### 4.2 Convergence of the outer sum

The continuum mass gap shift is
$$\sum_K C_K\,g_K^4\,\hat\Delta_K^{\,2}.$$
With $C_K \leq \max(C_0, C_{**})\cdot(1 + O(K^\gamma))$, $g_K^4 \sim 1/(b_0 K \ln 2)^2$, and $\hat\Delta_K^2 = (a^*\Delta_{\mathrm{phys}})^2 \cdot 4^{-K}$,
$$\sum_{K \geq K_0}C_K\,g_K^4\,\hat\Delta_K^{\,2}\;\lesssim\;\sum_{K \geq K_0}K^{\gamma-2}\cdot 4^{-K}\;<\;\infty.$$
Ratio test: the ratio is $\tfrac{1}{4}(1 + O(1/K))^{\gamma-2} \to 1/4 < 1$. So the sum converges absolutely, and its value is $\leq$ a constant depending only on $N$, $r_3$, $a^*$, $\Delta_{\mathrm{phys}}$.

### 4.3 Positivity of the continuum mass gap

From the sum bound, the mass-gap shifts are summable:
$$\Delta_\infty\;=\;\Delta_0\;-\;\sum_K \delta\Delta_K,\qquad |\delta\Delta_K|\leq C\,C_K\,g_K^4\,\hat\Delta_K^{\,2}\,\Delta_{\mathrm{phys}}.$$
By §5.7(c), with the convergent sum above, $|\Delta_0 - \Delta_\infty| \leq \epsilon \cdot \Delta_0$ for $\epsilon$ small (numerically $\sim$ 1.2% at $s = 2$, $\sim$ 0.01% at $s = 4$; see preprint §5.7 tables). Therefore $\Delta_\infty > 0$: the continuum mass gap is positive.

### 4.4 Which Tier 1 results were used

- **Step 1.1 (K-uniform cluster expansion):** used for (H1) in the Handoff Lemma, which gives a K-uniform starting constant $C_0^{\mathrm{cl}}$ for the inner flow of each bare theory. **Used.**
- **Step 1.2 (K-uniform Balaban analyticity radius):** used for (H2) in the Handoff Lemma, for the inner-flow activity bound $e^{-\kappa_{\mathrm{B}}|X|}$ in (3.2), and for the K-uniformity of the inner flow's output constants. **Used.**
- **Step 1.3 (K-uniform spectral lemma via Lieb-Robinson):** used to bound $C_{\mathrm{new}}(K) \leq C_*$, which is what feeds into the recursion as the "$+\,C_*$" in (4.1). **Used.**
- **Tier 0 notation patch:** used throughout to separate $K$ from $k$ and distinguish the kinematic refinement identity (1.1) from any Balaban inner step. **Used.**

---

## Section 5 — What the assembly does and does not establish

The assembly is **conditional** on four explicit inputs:

1. **Tier 1 Step 1.1 (K-uniform cluster expansion).** If this fails — i.e., if the cluster-expansion starting constant grows with $K$, or the cluster expansion cannot be reformulated in physical units — then (H1) fails, the Handoff Lemma breaks, and the inner flows of different bare theories cannot be assembled into a single convergent outer sum. The contribution from §3 ("first few inner steps") would potentially grow with $K$. Outcome: continuum mass gap claim unsupported.
2. **Tier 1 Step 1.2 (K-uniform Balaban analyticity radius).** If this fails — i.e., if $\kappa_{\mathrm{B}}$ depends on $K$ and degrades as $K \to \infty$ — then (H2) fails, and the activity bound $|K_k^{(K)}(X, V)| \leq e^{-\kappa_{\mathrm{B}}|X|}$ is no longer K-uniform. The inner flow's output $C_K$ may grow with $K$, and the fixed-point argument in §4.1 loses its meaning. Outcome: convergence sum of §4.2 would require separate control.
3. **Tier 1 Step 1.3 (K-uniform spectral lemma via Lieb-Robinson).** *This is the hard step.* If the Combes-Thomas / $\zeta$ argument of §5.5.3 cannot be reformulated K-uniformly in physical units, then $C_{\mathrm{new}}(K)$ may grow as $\exp(R_0^4/a_0(K)^4)$ or worse, and the recursion $C_{K+1} = C_K/4 + C_{\mathrm{new}}(K)$ has no K-uniform fixed point. The whole assembly collapses. *Partial* Step 1.3 (e.g., a K-uniform bound for $N = 2$ but not $N = 3$; or K-uniform up to a polynomial factor) yields a partial assembly: the continuum mass gap claim holds for the restricted regime but not in full generality.
4. **(H3) rate compatibility in the Handoff Lemma.** This is a quantitative check that $\kappa_{\mathrm{cl}}^* \geq \kappa_{\mathrm{B}}$. It is *very likely to hold* at the physical regime $a_0(K) \gg r_3$, because $\kappa_{\mathrm{cl}}$ has a $10^{13}$-plus margin (Section 4.4). Failure is unlikely but must be verified numerically for $N = 3$, which is Step 1.7 in the gap-closing strategy.

**What the assembly positively establishes (conditionally).** Given inputs 1–4, the assembly furnishes:
- A rigorous outer recursion $C_{K+1} = C_K/4 + C_*$ with fixed point $C_{**} = 4 C_*/3$.
- A K-uniform bound $C_K \leq \max(C_0^{\mathrm{cl}}, C_{**})\cdot (1 + O(K^\gamma))$.
- An absolutely convergent outer sum $\sum_K C_K g_K^4 \hat\Delta_K^2 < \infty$.
- Positivity of the continuum mass gap, $\Delta_\infty > 0$.

**What the assembly does *not* establish.**
- It does not establish any of inputs 1–3. Those are the Tier 1 bookkeeping / spectral-lemma substance.
- It does not establish OS axioms or Euclidean covariance; those are §5.7(f).
- It does not address the renormalized composite operators (Tier 3) that are needed for Clay eligibility.
- It does not extend beyond SU(N) to general compact simple $G$.

**If Tier 1 Step 1.3 is only partial.** Most plausibly: a K-uniform spectral lemma holds for $N = 2$, and for $N \geq 3$ modulo a Lieb-Robinson bound for non-Abelian lattice gauge theory (conjecturally true but not proven). Then §1–§4 applies unconditionally for $N = 2$ and conditionally for $N = 3$. Honest progress, but not gap-closure.

---

**End of document.** This assembly completes the Tier 1 "core rigor" phase at the level of the recursion algebra and the handoff lemma; the three K-uniformity inputs are deferred to parallel Tier 1 sister documents.
