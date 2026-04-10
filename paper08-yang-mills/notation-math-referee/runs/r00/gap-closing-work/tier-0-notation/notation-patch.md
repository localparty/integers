# Notation Cleanup Patch: K vs k separation in §§5.1, 5.4, 5.7

**Gap ID:** Tier 0 / C1 + E1 + E2 (single gap, three manifestations).
**Date:** 2026-04-08.
**Scope:** Notation-only rewrite of `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`; no new mathematics.

**Problem (one sentence).** The preprint uses a single letter $k$ for two contradictory conventions — Balaban's inner coarsening ($a_k = 2^k a_0$, $\hat\Delta_k$ grows) in §§5.1.2, 5.4.1, 5.4.3 and bare refinement ($a_k = a_0/2^k$, $\hat\Delta_k^2 \sim 4^{-k}$) in §§5.4.6, 5.7(b), 5.7(f); under the first convention the §5.4.6 convergence sum is literally divergent, so the two must be split into an outer index $K$ (bare refinement) and an inner index $k$ (Balaban RG within a fixed bare theory), following Balaban CMP **109** (1987) p. 251 and Dimock arXiv:1108.1335 (2011) p. 2.

---

## 1. New "Notation and Strategy" preamble (insert at start of §5.1, before §5.1.1)

> **Notation and strategy (two-index convention).**
> This section uses two distinct integer indices; the reader is asked to keep them separate.
>
> * **Outer index $K \in \mathbb{N}$ (bare refinement).** The continuum limit is built from a refining sequence of bare lattices $\Lambda_0(K)$ with spacing
>   $$a_0(K) \;=\; a^* \cdot 2^{-K},$$
>   where $a^* \gg r_3$ is a fixed reference scale chosen so that the cluster expansion of Section 4 converges at $K = 0$. As $K \to \infty$, $a_0(K) \to 0$, and the dimensionless mass gap at the bare scale *shrinks*:
>   $$\hat\Delta_K := a_0(K)\,\Delta_{\mathrm{phys}} = a^*\Delta_{\mathrm{phys}}\cdot 2^{-K}, \qquad \hat\Delta_{K+1}^2 = \hat\Delta_K^2/4.$$
> * **Inner index $k \in \mathbb{N}$ (Balaban block-spin RG within a fixed bare theory).** Within each bare theory at scale $a_0(K)$, Balaban's block-spin RG generates a sequence of effective actions on progressively coarser lattices
>   $$a_k^{(K)} \;=\; 2^k\,a_0(K), \qquad k = 0, 1, 2, \ldots,$$
>   with the dimensionless gap $\hat\Delta_k^{(K)} = a_k^{(K)}\Delta_{\mathrm{phys}} = 2^{k-K}\,a^*\Delta_{\mathrm{phys}}$ *growing* in $k$ (at fixed $K$) and *shrinking* in $K$ (at fixed $k$).
>
> The two indices play different roles. **Balaban's UV stability theorem** (§5.1.3 below) is applied *within* each bare theory $K$ separately, controlling the inner flow $k = 0 \to \infty$ at fixed $K$. **The §5.4 form-factor recursion** is a *comparison between two bare theories* at consecutive outer scales $K$ and $K+1$; it is **not** a single Wilsonian block-spin step. The factor $1/4$ in the recursion is the kinematic identity $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$, coming from the bare refinement $a_0(K+1) = a_0(K)/2$, not from physical contraction under flow. **The convergence sum** $\sum_K C_K g_K^4 \hat\Delta_K^2$ is indexed by the *outer* $K$; its doubly-exponential decay $4^{-K}$ comes from the bare shrinking.
>
> Convention follows Balaban, *Renormalization group approach to lattice gauge field theories, I*, CMP **109** (1987), 249–301, p. 251 (inner block-spin index); and Dimock, *The renormalization group according to Balaban, I. Small fields*, arXiv:1108.1335 (2011), p. 2 (outer bare-scale indexing for the continuum-limit sequence). Throughout §§5.1–5.7, $k$ always refers to the inner Balaban step within a fixed bare theory, and $K$ always refers to the outer bare-refinement step.

---

## 2. Before/after patches

All "before" blocks quote `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` verbatim with line numbers.

### Patch 2.1 — §5.1.2, lines 20–23

**Before:**
> Start from a fine lattice $\Lambda_0$ with spacing $a_0$ and bare coupling $g_0$. At RG step $k$, define a coarser lattice $\Lambda_k$ with spacing $a_k = 2^k a_0$ by block-spinning the link variables over $2^4$ blocks.

**After:**
> *Fix a bare scale $K \in \mathbb{N}$.* Start from the bare lattice $\Lambda_0(K)$ with spacing $a_0(K) = a^* \cdot 2^{-K}$ and bare coupling $g_0(K)$. At Balaban inner step $k$ within bare theory $K$, define a coarser effective lattice $\Lambda_k^{(K)}$ with spacing $a_k^{(K)} = 2^k\,a_0(K)$ by block-spinning the link variables over $2^4$ blocks. Within §§5.1–5.2 the outer scale $K$ is held fixed and the superscript $(K)$ is suppressed; §5.4 then compares different bare theories indexed by $K$.

**Justification.** Restores Balaban's inner-coarsening convention as an *inner* statement at fixed outer $K$, and names the outer index explicitly, so all subsequent "$k$" in §§5.1–5.2 is unambiguously inner.

---

### Patch 2.2 — §5.4.1, lines 678–683

**Before:**
> **Geometry and field decomposition.** At step $k$: lattice $\Lambda_k$, spacing $a_k = 2^k a_0$, dimensionless gap $\hat{\Delta}_k = a_k \Delta_k$. One block-spin step coarsens to $\Lambda_{k+1}$ with $a_{k+1} = 2a_k$ and $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k(1 + O(g_k^4))$.

**After:**
> **Geometry: outer recursion between bare theories.** Let $K$ denote the bare-scale index. Bare theory $K$ has lattice $\Lambda_0(K)$ with spacing $a_0(K) = a^*\cdot 2^{-K}$ and dimensionless gap $\hat\Delta_K = a_0(K)\,\Delta_{\mathrm{phys}}$. Bare theory $K+1$ is obtained by refining: $a_0(K+1) = a_0(K)/2$, so
> $$\hat\Delta_{K+1} = \hat\Delta_K/2, \qquad \hat\Delta_{K+1}^2 = \hat\Delta_K^2/4. \tag{5.4.1a}$$
> This identity is purely kinematic. *Within a fixed bare theory $K$*, Balaban's block-spin step $k \to k+1$ splits the field $U = V\cdot u$ into slow $V$ on $\Lambda_{k+1}^{(K)}$ and fast $u$ (momenta $\pi/a_{k+1}^{(K)} < |p| < \pi/a_k^{(K)}$), with effective action $e^{-S_{k+1}^{(K)}[V]} = \int\!\mathcal{D}u\;e^{-S_k^{(K)}[V\cdot u]}\,\delta(\text{gauge fixing})$. All subsequent saddle-point, one-loop, and remainder bounds in this subsection are inner statements at fixed $K$; the outer identity (5.4.1a) is reserved for the outer recursion in §5.4.3 and §5.4.5.

**Justification.** The original "$\hat\Delta_{k+1} = 2\hat\Delta_k$ growing" statement is Balaban inner (correct) but does *not* drive the §5.4 recursion. The recursion is an outer comparison whose kinematic content is $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$. We separate the two explicitly: outer identity (5.4.1a), plus inner field decomposition at fixed $K$.

---

### Patch 2.3 — §5.4.3, lines 754–775

**Before:**
> Assume the inductive hypothesis at step $k$: $|{}_k\langle 1|E_k(0)|1\rangle_k^c| \leq C_k\,g_k^4\,\hat{\Delta}_k^2$. […] Converting to step-$k+1$ variables via $\hat{\Delta}_k = \hat{\Delta}_{k+1}/2 + O(g_k^4\hat{\Delta}_{k+1})$: $|\text{(A1)}| \leq (C_k/4)\,g_k^4\,\hat{\Delta}_{k+1}^2\,(1+O(g_k^2))$.
>
> **The factor $1/4$ is the contraction mechanism.** The old form factor, expressed in the new dimensionless units, shrinks by $1/4$ because $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$. The physics has not changed; only the bookkeeping units have coarsened.

**After:**
> *Inductive hypothesis at bare scale $K$.* Let $C_K$ be the form-factor constant of the IR effective theory of bare theory $K$ (the output of Balaban's inner flow at fixed $K$; K-uniformity is the Tier 1 follow-up). The inductive hypothesis reads
> $$|\langle 1|E^{(K)}(0)|1\rangle_c^{(K)}| \;\leq\; C_K\,g_K^4\,\hat\Delta_K^2, \tag{5.4.3a}$$
> where $E^{(K)}$ is the IR effective remainder of bare theory $K$ and $g_K := g_0(K)$ (up to $O(g_K^6)$ under inner running).
>
> *Passage to bare scale $K+1$.* The old operator $E^{(K)}$, pulled forward to theory $K+1$, contributes $E^{(K)\downarrow}$ with $|c_{d_O}^{\downarrow}| \leq |c_{d_O}^{(K)}|(1 + O(g_K^2))$. Its *physical* matrix element is unchanged. When we express the bound against the *new* reference scale $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$, the dimensionless coefficient of $\hat\Delta_{K+1}^2$ in the $K+1$ bookkeeping is one-quarter of the coefficient of $\hat\Delta_K^2$ in the $K$ bookkeeping, because the inductive bound at $K+1$ uses $\hat\Delta_{K+1}^2$ on the reference scale side:
> $$|\text{(A1)}_{K\to K+1}| \;\leq\; \tfrac{C_K}{4}\,g_K^4\,\hat\Delta_{K+1}^2\,(1 + O(g_K^2)). \tag{5.4.3b}$$
>
> **The factor $1/4$ is the kinematic contraction between bare theories.** It is the change of dimensionless units when the bare lattice is refined ($\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$), not a physical decay under Wilsonian flow.

**Justification.** The $1/4$ is now unambiguously an *outer* bookkeeping identity (refinement between bare theories), not an *inner* decay. The original "$\hat\Delta_k = \hat\Delta_{k+1}/2$" was already the refining direction under its charitable interpretation; we simply make the direction explicit by promoting $k$ to $K$.

---

### Patch 2.4 — §5.4.5, lines 832–858 (the recursion box)

**Before:**
> **Combining (A) and (B):** $|\langle 1|E_{k+1}(0)|1\rangle_c^{(k+1)}| \leq ((C_k/4) + C_{\mathrm{new}})\,g_k^4\,\hat{\Delta}_{k+1}^2\,(1+O(g_k^2))$. Converting $g_k^4 = g_{k+1}^4(1+O(g_k^2))$: $|\langle 1|E_{k+1}(0)|1\rangle_c^{(k+1)}| \leq C_{k+1}\,g_{k+1}^4\,\hat{\Delta}_{k+1}^2$, where the constant recursion is $\boxed{C_{k+1} = C_k/4 + C_{\mathrm{new}} + O(g_k^2 C_k)}$.
>
> Ignoring the $O(g_k^2)$ correction, $C_{k+1} = C_k/4 + C_{\mathrm{new}}$ has stable fixed point $C_* = 4C_{\mathrm{new}}/3$ with geometric convergence $C_k = C_* + (C_0 - C_*)\cdot 4^{-k}$.

**After:**
> **Combining (A) and (B) between bare theories $K$ and $K+1$:**
> $$|\langle 1|E^{(K+1)}(0)|1\rangle_c^{(K+1)}| \;\leq\; \left(\tfrac{C_K}{4} + C_{\mathrm{new}}(K)\right) g_K^4\,\hat\Delta_{K+1}^2\,(1 + O(g_K^2)),$$
> where $C_{\mathrm{new}}(K)$ is the new-contribution constant from the fluctuation integral along the *inner* Balaban flow of bare theory $K$ (§5.4.4, interpreted with $K$ fixed and inner $k$). Converting $g_K^4 = g_{K+1}^4(1 + O(g_K^2))$ via bare-scale running:
> $$|\langle 1|E^{(K+1)}(0)|1\rangle_c^{(K+1)}| \;\leq\; C_{K+1}\,g_{K+1}^4\,\hat\Delta_{K+1}^2,$$
> with outer recursion
> $$\boxed{\;C_{K+1} \;=\; \tfrac{C_K}{4} \;+\; C_{\mathrm{new}}(K) \;+\; O(g_K^2\,C_K)\;}$$
>
> *Fixed point (conditional on K-uniform inner bound).* If $C_{\mathrm{new}}(K) \leq C_*$ uniformly in $K$ (Tier 1, pending), the recursion has bounded orbit $C_K \leq \max(C_0,\,4C_*/3)$, with geometric convergence $C_K \to 4\,C_\infty^{\mathrm{new}}/3$ at rate $4^{-K}$ if $C_{\mathrm{new}}(K) \to C_\infty^{\mathrm{new}}$.

**Justification.** The recursion is now unambiguously an *outer* comparison between bare theories. $C_{\mathrm{new}}(K)$ depends on $K$ because it is extracted from the full inner Balaban flow of a $K$-dependent bare theory; K-uniformity is the Tier 1 step, explicitly flagged.

---

### Patch 2.5 — §5.4.6, lines 874–887

**Before:**
> **Why this does not matter:** The mass gap shift sum involves $C_k g_k^4 \hat{\Delta}_k^2$. With $C_k \sim k^\gamma$, $g_k^4 \sim 1/k^2$, $\hat{\Delta}_k^2 \sim 4^{-k}$: $\sum_k C_k\,g_k^4\,\hat{\Delta}_k^2 \sim \sum_k k^{\gamma-2}\cdot 4^{-k} < \infty$.

**After:**
> **Why this does not matter (outer sum over bare scales).** The mass-gap shift sum runs over the *outer* bare-refinement index $K$, not over Balaban inner steps. With $C_K \lesssim K^\gamma$ (power-law accumulation of $O(g_K^2)$ corrections in the outer recursion), $g_K^4 \sim 1/(b_0 K \log 2)^2 \sim 1/K^2$ (bare running), and $\hat\Delta_K^2 = (a^*\Delta_{\mathrm{phys}})^2\cdot 4^{-K}$ (outer shrinking from $a_0(K) = a^*/2^K$):
> $$\sum_{K\geq K_0} C_K\,g_K^4\,\hat\Delta_K^2 \;\lesssim\; \sum_{K\geq K_0} K^{\gamma-2}\cdot 4^{-K} \;<\; \infty.$$
> The doubly exponential factor $4^{-K}$ comes from *bare refinement*, not from any inner block-spin step, and overwhelms any polynomial $K^\gamma$.

**Justification.** Every index in the convergence sum is now outer. The $4^{-K}$ decay is tied explicitly to $a_0(K) = a^*/2^K$, resolving the contradiction with §§5.4.1, 5.4.3 (now inner statements, no longer claiming the $4^{-k}$ decay).

---

### Patch 2.6 — §5.7(b), lines 1880–1885

**Before:**
> Along the RG trajectory with $L^k$ blocking ($L = 2$): $a_k = a_0/2^k$, and $g_k^2 \sim 1/(b_0 k \log 2)$ for large $k$ with $b_0 = 11N/(48\pi^2)$. The general term is $g_k^4(a_k\Lambda)^s \sim (a_0\Lambda)^s/[(b_0 k\log 2)^2 \cdot 2^{ks}]$.

**After:**
> Along the *outer* refinement sequence of bare scales $K = 0, 1, 2, \ldots$ with $a_0(K) = a^*\cdot 2^{-K}$ and bare-coupling running $g_K^2 \sim 1/(b_0 K \log 2)$ for large $K$ ($b_0 = 11N/(48\pi^2)$), the general term of the convergence sum is
> $$g_K^4\,(a_0(K)\,\Lambda)^s \;\sim\; \frac{(a^*\Lambda)^s}{(b_0 K \log 2)^2 \cdot 2^{Ks}}.$$
> The exponential $2^{-Ks}$ dominates $1/K^2$; the sum converges doubly exponentially in the outer index $K$ for any $s \geq 1$.

**Justification.** Notation-only flip $k \to K$; the formula is content-preserving. The numerical tables that follow (lines 1893–1913) are unchanged in value; relabel the column header "$k$" as "$K$".

---

### Patch 2.7 — §5.7(f) OS2, lines 2139–2160

**Before:**
> **Rate of O(4) restoration.** The O(4)-breaking corrections to the $n$-point Schwinger functions at lattice spacing $a_k = a_0/2^k$ are bounded by […] $|S_n^{\mathrm{lat}} - S_n^{\mathrm{O}(4)}| \leq C_n\,g_k^4 \cdot (a_k\Lambda)^2$. […] $g_k^4 \cdot (a_k\Lambda)^2 = (a_0\Lambda)^2/[(b_0 k\ln 2)^2 \cdot 4^k] \to 0$ as $k \to \infty$.

**After:**
> **Rate of O(4) restoration.** At bare scale $K$, with lattice spacing $a_0(K) = a^*\cdot 2^{-K}$, the O(4)-breaking corrections to the $n$-point Schwinger functions satisfy
> $$|S_n^{\mathrm{lat},(K)}(x_1,\ldots,x_n) - S_n^{\mathrm{O}(4)}(x_1,\ldots,x_n)| \;\leq\; C_n\,g_K^4\cdot (a_0(K)\,\Lambda)^2. \tag{OS2.3}$$
> Along the outer refinement, $g_K^4 \to 0$ and $a_0(K) \to 0$, so
> $$g_K^4\cdot (a_0(K)\,\Lambda)^2 \;=\; \frac{(a^*\Lambda)^2}{(b_0 K \ln 2)^2 \cdot 4^K} \;\to\; 0 \quad\text{as }K\to\infty. \tag{OS2.4}$$

**Justification.** Notation-only flip $k \to K$. The coefficient bound (OS2.2) on $|c_i^{(6)}(k)| \leq C g_k^4$ is itself an *inner* Balaban statement (the inner running coupling at inner step $k$ of bare theory $K$); at the IR end of the inner flow it reduces to $g_K^4$, which is what enters (OS2.3) at the outer level.

---

## 3. Consistency check

**Recursion under corrected notation.** At bare scale $K$:
$$|\langle 1|E^{(K)}(0)|1\rangle_c^{(K)}| \leq C_K\,g_K^4\,\hat\Delta_K^2.$$
Passing to $K+1$, the kinematic identity (5.4.1a) $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$ lets us rewrite the old contribution relative to the $K+1$ reference scale as $(C_K/4)\,g_K^4\,\hat\Delta_{K+1}^2$, and the new contribution is $C_{\mathrm{new}}(K)\,g_K^4\,\hat\Delta_{K+1}^2$. Absorbing $g_K^4 = g_{K+1}^4(1 + O(g_K^2))$:
$$\boxed{\;C_{K+1} \;=\; \tfrac{C_K}{4} \;+\; C_{\mathrm{new}}(K) \;+\; O(g_K^2\,C_K)\;.}$$
The $1/4$ is a *comparison between bare theories* (kinematic units change under refinement), **not** a Balaban inner step.

**Convergence sum (ratio test).** Assuming K-uniform $C_{\mathrm{new}}(K) \leq C_*$ (Tier 1), the recursion gives $C_K$ bounded and at worst polynomial in $K$, say $C_K \lesssim K^\gamma$. With $g_K^4 \sim 1/K^2$ and $\hat\Delta_K^2 \sim (a^*\Delta_{\mathrm{phys}})^2\cdot 4^{-K}$:
$$\sum_K C_K\,g_K^4\,\hat\Delta_K^2 \;\lesssim\; \sum_K K^{\gamma-2}\cdot 4^{-K}.$$
Ratio test:
$$\lim_{K\to\infty}\frac{(K+1)^{\gamma-2}\,4^{-(K+1)}}{K^{\gamma-2}\,4^{-K}} \;=\; \tfrac{1}{4}\cdot\lim_{K\to\infty}\!\left(\tfrac{K+1}{K}\right)^{\gamma-2} \;=\; \tfrac{1}{4} \;<\; 1.$$
The sum converges geometrically at rate $4^{-K}$, for any $\gamma \in \mathbb{R}$. The $4^{-K}$ comes from the outer bare refinement ($\hat\Delta_K^2 \sim 4^{-K}$, matching §5.4.6 claim) and **not** from any growing $4^{+k}$ under inner Balaban flow. The contradiction identified in the referee report is resolved.

---

## 4. Open follow-up (Tier 1, NOT closed here)

This patch is a notation-only rewrite. The following substantive claims are *exposed* but **not** established:

1. **K-uniform inner-RG bound on $C_{\mathrm{new}}(K)$.** The outer recursion has a bounded fixed point only if $C_{\mathrm{new}}(K) \leq C_*$ uniformly in $K$. Since $C_{\mathrm{new}}(K)$ is derived from Balaban's full inner flow of bare theory $K$ (integrating UV shells from $a_0(K) = a^*/2^K$ up through coarser inner scales $a_k^{(K)} = 2^k a_0(K)$) and Balaban's published theorems are stated *for fixed bare scale*, K-uniformity does not follow from Balaban directly. See `gap-closing-strategy.md` Steps 1.1–1.4.

2. **K-uniform analyticity radius $\rho(K) \geq \rho_* > 0$.** Balaban's CMP 95 §3 / CMP 98 §E / CMP 109 §3 express the polymer-expansion radius in terms of $\kappa$, $m_W a_k^{(K)}$, and $r_{\mathrm{proj}}$. Under the corrected notation $m_W a_k^{(K)}$ is $K$-independent (physical constants × inner ratio $2^k$), so verification reduces to bookkeeping, but must be carried out explicitly under the $K$-indexed family.

3. **K-uniform spectral-lemma constant $C_p$.** The Combes-Thomas / $\zeta$ argument of §5.5.3 currently uses lattice-unit local Hilbert-space dimensions that grow like $\exp(R_0^4/a_0(K)^4)$. A K-uniform bound requires reformulation in *physical* units (e.g., via a lattice Lieb-Robinson bound). Tier 1 Step 1.3; this is the hardest item.

4. **Cluster/Balaban handoff at $k = 0$ of bare theory $K$.** The starting condition $C_K(k=0)$ at the bare scale of theory $K$ comes from the Section 4 cluster expansion. Kotecký–Preiss / Balaban-polymer compatibility at $k=0$ must hold uniformly in $K$. Tier 1 Steps 1.6–1.7 (the "C3" follow-up).

None of 1–4 is affected in *substance* by the Tier 0 rewrite; what changes is that they become *statable* without notational contradiction, which is the precondition for proving them.

---

**End of patch.** After applying 2.1–2.7, §§5.1–5.7 of `05-continuum-limit.md` read coherently: $K$ is bare refinement throughout, $k$ is Balaban inner coarsening within a fixed bare theory throughout, the §5.4.5 recursion is an outer comparison, and the §5.4.6 / §5.7(b) convergence sum is an outer sum whose $4^{-K}$ decay comes from bare refinement. No mathematics has been added or removed.
