## Part B, Point 1: Cluster Expansion Convergence

**Weight:** MEDIUM
**Verdict:** SOUND (with the standing N-dependence drift from A1/A2)

**Finding:**

(a) **Kotecký–Preiss criterion.** Section 04.3, Theorem 3 verifies the KP criterion via the standard route: cluster weight $\leq (K \cdot |f_P|_{\max} \cdot C_0^{1/6} \cdot e^{-m_1 a/6})^{|\mathcal{C}|}$, with each connected cluster on $\mathbb{Z}^4$ satisfying $|B| \geq |S|/6$. The geometric series converges when $c_d \cdot K \cdot C_0^{1/6} \cdot e^{2\beta - m_1 a/6 + \alpha} < 1$, giving $2\beta + \alpha < m_1 a/6 - \ln(c_d K C_0^{1/6})$.

The lattice-animal constant $c_d$ in $d=4$ is bounded above by approximately $e^7 \sim 1097$ (Klarner–Rivest 1973; tighter bounds exist but are immaterial since $\ln c_d$ is much smaller than $m_1 a/6 \sim 10^{14}$). Verified.

The polymer activity bound is $|K(X)| \leq e^{-\kappa|X|}$ with $\kappa = m_1 a / 6 - \ln(\text{const})$, satisfying the standard KP convergence radius. The combinatorial mode count $d_n \sim n^{N-2}$ on $\mathbb{CP}^{N-1}$ enters $C_0$ but is suppressed exponentially.

(b) **Physical regime coverage and the Balaban handoff.** The convergence regime is $\beta < \beta_{\max}(a) \sim a/(2\sqrt{N} r_3)$ (with the corrected N-dependent constant from A1/A2). In the physical regime $a/r_3 \sim 10^{15}$, this gives $\beta_{\max} \sim 10^{14}$, more than enough to cover all couplings used in lattice QCD simulations.

But the preprint conflates two distinct regimes:
- **Cluster expansion regime:** $a$ large, $\beta < \beta_{\max}(a)$ — used for Theorem 4.
- **Balaban regime:** $g_0$ small (large $\beta$), Balaban's RG applies — used for the continuum limit.

The cluster expansion gives $\Delta_0(\beta) > 0$ for *every* $\beta$ in its window. Balaban's RG gives a controlled flow *starting* from a small bare coupling $g_0$. The handoff between the two is not addressed quantitatively: at what scale does the cluster expansion "hand off" to the Balaban RG, and is the *same* mass gap (i.e., the same $\Delta_0$) being tracked? Section 5.7 Remark 1 acknowledges this informally:

> "At $k = 0, 1, 2$ where $g_k^4 = O(1)$, first-order perturbation is not a priori justified. These finitely many steps are handled non-perturbatively via the cluster expansion, with bounded total contribution $K_0$ absorbed into $C_0$."

This is reasonable in spirit but circular in detail. The cluster expansion regime requires *coarse* lattice spacings ($a \gg r_3$, hence $a \gg$ continuum scale), where Balaban's RG would need many *coarsening* steps to reach. But Balaban's RG flows toward the IR (coarser scales), not toward the UV (finer scales) — see Point C1 and the K-vs-k notation problem.

**This is the same K-vs-k confusion that breaks §5.4: the cluster expansion lives at a coarse $a_0$ ("bare" in the script's $K = 0$ sense), and Balaban's RG runs forward in the inner index $k$ from there. To establish the *continuum limit* one needs a *refining* sequence of bare lattices indexed by an outer $K$, with each bare theory's mass gap controlled separately. The preprint never separates these, and the result is that "Balaban's RG" and "cluster expansion" are described as living in the same coupling regime when in fact they correspond to different conceptual axes.**

(c) **Connected function bounds.** Theorem 2 in Section 04.3 gives exponential clustering with rate $\alpha/a > 0$. The constant $C$ in $|S_n^c| \leq C^n e^{-\Delta \cdot \mathrm{diam}}$ is $a$-independent because the cluster expansion bound is uniform in $a$ within its convergence window. The OS1 temperedness in Section 5.7(f) inherits this, giving $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$.

The bound *is* $a$-independent within the cluster-expansion regime, but the cluster-expansion regime itself has an $a$-dependent threshold $\beta < \beta_{\max}(a) \sim a/r_3$, which goes to *infinity* as $a$ increases (coarser lattice = wider window). For the $a \to 0$ continuum limit, the cluster-expansion regime *shrinks* to nothing and the proof must rely entirely on the Balaban handoff. This is internally consistent only if the K-vs-k issue is fixed.

**Impact on the claimed result:** Sound at the level of "lattice mass gap $\Delta_0 > 0$ at any fixed $a$ within the cluster-expansion window." The continuum-limit propagation depends on Point C1 and on the K-vs-k notation issue.
