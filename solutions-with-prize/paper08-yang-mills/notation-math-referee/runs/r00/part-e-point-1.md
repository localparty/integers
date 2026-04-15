## Part E, Point 1: Inductive Stability

**Weight:** MEDIUM
**Verdict:** **GENUINE GAP** (the recursion algebra requires the K-vs-k separation; as written, the "$1/4$ contraction" is undefined because it relies on a kinematic identity that contradicts the §5.4.1 setup)

**Finding:**

(a) **The $1/4$ contraction.** The recursion (§5.4.5):
$$|\langle 1|E_{k+1}(0)|1\rangle_c^{(k+1)}| \leq (C_k/4 + C_{\mathrm{new}}) g_k^4 \hat\Delta_{k+1}^2 (1 + O(g_k^2))$$
relies on the identity $\hat\Delta_k^2 = \hat\Delta_{k+1}^2/4$, which the proof attributes to "doubling the lattice spacing doubles $\hat\Delta$" (line 1006).

This identity is *correct under the bare-refinement convention* ($a_0(K+1) = a_0(K)/2$, hence $\hat\Delta_{K+1} = \hat\Delta_K/2$, hence $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$, i.e., $\hat\Delta_K^2 = \hat\Delta_{K+1}^2 \cdot 4 \neq \hat\Delta_{K+1}^2/4$). Wait — let me re-check.

If $a_0(K+1) < a_0(K)$ (refining: smaller spacing), and $\Delta_{phys}$ is fixed, then $\hat\Delta_{K+1} = a_0(K+1) \Delta_{phys} < a_0(K) \Delta_{phys} = \hat\Delta_K$. So $\hat\Delta_{K+1} < \hat\Delta_K$, i.e., $\hat\Delta_{K+1}^2 = \hat\Delta_K^2 / 4$, i.e., $\hat\Delta_K^2 = 4 \hat\Delta_{K+1}^2$. Substituting:
$$C_K g_K^4 \hat\Delta_K^2 = 4 C_K g_K^4 \hat\Delta_{K+1}^2$$
But the recursion says the OLD term contributes $C_K/4 \cdot \hat\Delta_{K+1}^2$, *not* $4 C_K \cdot \hat\Delta_{K+1}^2$. So the "$1/4$" is the ratio $\hat\Delta_{K+1}^2/\hat\Delta_K^2$, *not* $\hat\Delta_K^2/\hat\Delta_{K+1}^2$.

Concretely: the old form factor at scale $K$ (in $\hat\Delta_K$ units) is $C_K g_K^4 \hat\Delta_K^2$. Re-expressed in $\hat\Delta_{K+1}$ units (the new scale), it becomes $C_K g_K^4 \cdot 4 \hat\Delta_{K+1}^2$. The ratio of "new constant" to "old constant" is therefore $4 C_K + C_{\mathrm{new}}$, not $C_K/4 + C_{\mathrm{new}}$.

**Wait** — let me re-read §5.4.3 line 769:
> "Converting to step-$k+1$ variables via $\hat\Delta_k = \hat\Delta_{k+1}/2 + O(g_k^4 \hat\Delta_{k+1})$"

So the proof asserts $\hat\Delta_k = \hat\Delta_{k+1}/2$, i.e., $\hat\Delta_{k+1} = 2 \hat\Delta_k$. This says $\hat\Delta$ *grows* with $k$. Combined with $\hat\Delta_{k+1}^2 = 4 \hat\Delta_k^2$:
$$\hat\Delta_k^2 = \hat\Delta_{k+1}^2 / 4$$
Substituting into the form-factor bound at step $k$:
$$|\langle 1|E_k|1\rangle_c| \leq C_k g_k^4 \hat\Delta_k^2 = C_k g_k^4 \cdot \hat\Delta_{k+1}^2/4 = (C_k/4) g_k^4 \hat\Delta_{k+1}^2$$
So the "$1/4$" *is* the conversion factor, **under the convention $\hat\Delta_{k+1} = 2 \hat\Delta_k$ (which is the Balaban inner-step coarsening convention).**

OK, so the recursion §5.4.5 *itself* is internally consistent under the Balaban convention: $\hat\Delta$ grows with $k$, and the $1/4$ comes from re-expressing the old (smaller) form factor in the new (larger) units. Fine.

**But then the convergence sum §5.4.6 contradicts this.** Under the Balaban convention $\hat\Delta_k = 2^k \hat\Delta_0$ (growing), we have $\hat\Delta_k^2 = 4^k \hat\Delta_0^2$. The sum is
$$\sum_k C_k g_k^4 \hat\Delta_k^2 = \hat\Delta_0^2 \sum_k C_k g_k^4 \cdot 4^k$$
which **diverges** because $4^k$ beats $g_k^4 \sim 1/k^2$ exponentially.

The §5.4.6 claim "$\hat\Delta_k^2 \sim 4^{-k}$, so the sum is $\sum k^{\gamma-2} \cdot 4^{-k} < \infty$" requires $\hat\Delta_k$ to *shrink* with $k$, which is **opposite** to §5.4.1 / §5.4.3.

So the recursion itself is OK *in either* convention, but the convergence sum requires the *opposite* convention from the recursion setup. The proof has a sign confusion: the recursion is set up in the Balaban inner-coarsening convention, but the "convergence" of the sum is computed in the bare-refining convention. **This is a fatal sign error**, not just a notation drift.

(b) **The wave-function correction (term A2).** §5.4.3 bounds $\|\delta 1\| \leq C g_k^4 / \hat\Delta_k$ via Kato perturbation with $\|E_k\| \leq C g_k^4$. The Kato bound requires $\|E_k\|$ to be small compared to the spectral gap of the unperturbed operator (here $\hat\Delta_k$). This needs $g_k^4 \ll \hat\Delta_k$, which is satisfied on the AF trajectory.

The cross term contribution $|\langle\delta 1|E_k|1\rangle| \leq C g_k^8/\hat\Delta_k$ is bounded against $g_k^4 \hat\Delta_{k+1}^2$ via "$\hat\Delta_k \gtrsim g_k^{4/3}$" (a claim about the AF trajectory). This is plausible but not obviously satisfied — if anything, $\hat\Delta_k \to 0$ as $k \to \infty$ in the refining convention, so $\hat\Delta_k$ shrinks faster than $g_k^{4/3}$ would shrink, making the bound *worse* not better.

Actually, in the Balaban inner convention $\hat\Delta_k = 2^k \hat\Delta_0$ grows, so $\hat\Delta_k \gg g_k^{4/3}$ is automatic. In the bare convention $\hat\Delta_K \to 0$, this fails. Yet another instance of the K-vs-k confusion making the algebra ambiguous.

(c) **The Gronwall bound and polynomial growth.** $C_k \sim k^\gamma$ from $\prod (1 + \alpha g_j^2) \leq \exp(\alpha \sum g_j^2) \sim \exp(\alpha \ln k) = k^{\alpha/(b_0 \ln 2)}$. The exponent $\gamma$ is N-dependent ($\gamma \sim N$ via I.3.2 item 9). For each fixed $N$, $\gamma$ is finite, so $k^\gamma \cdot 4^{-k}$ converges. *Provided* that $4^{-k}$ rather than $4^k$ is the correct factor — see (a).

**To close:**

1. Rewrite §5.4 with explicit K (bare-scale exponent) and $k$ (Balaban inner index) separation.
2. Show that the inner Balaban RG within a fixed bare theory $K$ delivers a $K$-uniform bound on the form factor.
3. Set up the *outer* recursion as a comparison of $C_K$ to $C_{K+1}$ with $a_0(K+1) = a_0(K)/2$, and verify $\hat\Delta_K^2 = 4^{-(K - K_0)} \hat\Delta_{K_0}^2$ in this convention.
4. Re-derive the convergence sum $\sum_K C_K g_K^4 \hat\Delta_K^2 \sim \sum_K k^{\gamma-2} 4^{-K}$ under the corrected convention.

**Difficulty:** As a notation cleanup, **1 page**. As a re-derivation that the inner RG's outputs feed correctly into the outer recursion, **1 paper or more**. The current presentation papers over the fact that *the inner RG and the outer recursion are different mathematical structures*, conflated by a single index $k$.

**Impact on the claimed result:** As written, the convergence claim of §5.4.6 is contradicted by the conventions of §5.4.1 / §5.4.3. The proof's central technical innovation (the form-factor recursion) cannot be evaluated until this is fixed. **This is the same gap as Point C1, restated at the level of the recursion algebra.**
