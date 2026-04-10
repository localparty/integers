# Gap-Closing Strategy: Yang-Mills Mass Gap Preprint

This document is a tactical companion to the referee report. For each gap (genuine or closable), it states the diagnosis, the proposed fix, the concrete steps, the dependencies on other fixes, and the estimated effort. The goal is to give the authors a phased program for moving the preprint toward Clay eligibility.

---

## Executive Summary

The gaps split into four severity tiers, with strict dependencies between tiers:

| Tier | Gaps | Effort | Blocks |
|:----|:-----|:-------|:-------|
| **0** (must do first) | K-vs-k notation cleanup (C1, E1, E2 — ONE gap) | 1 page | Everything else in §5 |
| **1** (core rigor) | Inner-RG K-uniformity, cluster/Balaban handoff (C3) | 1 paper | Continuum limit claim |
| **2** (technical fixes) | A1 (Weitzenböck notation), A3 (Lüscher Q on lattice), B2 (FM direction), C2 (large-field exponent), D3 (Combes-Thomas locality), F1 (coincident-point singularities), F2 (RP topology), F5 (non-triviality logic) | ~5–10 pages total | None — can run in parallel with Tier 1 |
| **3** (Clay structural) | G4(a) renormalized composite operators, G4(b) AF short-distance match, G4(c) stress tensor, G4(d) OPE | 3–5 papers | Needs Tier 0+1 done |
| **4** (scope) | G1(b)/I.4/K — extension to all compact simple G | 1–2 papers | Needs SU(N) case complete |

**Critical path: Tier 0 → Tier 1 → Tier 3.** Tier 2 fixes can run in parallel with Tier 1. Tier 4 should wait until SU(N) is airtight, otherwise the same bugs propagate.

**Total program: roughly 18–24 months of focused work** by a small team with deep constructive QFT expertise. This is not "minor revisions" — it is a substantive research program to convert a structurally interesting proof into a Clay-eligible submission.

---

## Dependency Graph

```
                    Tier 0
              [K/k notation cleanup]
                       |
                       v
           +-----------+-----------+
           |                       |
           v                       v
        Tier 1                  Tier 2 (parallel)
   [Inner-RG K-uniformity]    [A1, A3, B2, C2,
   [cluster/Balaban handoff]   D3, F1, F2, F5]
           |
           v
        Tier 3
   [Renormalized composite operators]
   [AF short-distance match]
   [Stress tensor]
   [OPE]
           |
           v
        Tier 4
   [Extension to all compact simple G]
           |
           v
   [Clay submission]
```

---

# Tier 0: Notation Cleanup (Foundation)

## Gap C1/E1/E2: The K-vs-k Notation Collision

### Diagnosis

The proof uses a single letter $k$ for two conceptually distinct indices:
- **(Balaban inner)** $k$ in §5.1.2 / §5.4.1: $a_k = 2^k a_0$ (coarsening), $\hat\Delta_{k+1} = 2\hat\Delta_k$ (growing).
- **(Bare refinement)** $k$ in §5.4.6 / §5.7(b): $a_k = a_0/2^k$ (refining), $\hat\Delta_k^2 \sim 4^{-k}$ (shrinking).

The §5.4.5 recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}}$ is *internally consistent* under the Balaban convention but its convergence sum diverges. It is *internally consistent* under the bare-refinement convention but the recursion becomes $C_{K+1} = 4 C_K + C_{\mathrm{new}}$ (a blow-up) and the sum converges only because $\hat\Delta_K^2$ shrinks faster than $C_K$ grows.

Neither single convention gives both "$1/4$ contraction" AND "$\sum 4^{-k}$ converges." The proof needs the script's *two-index* structure: an outer $K$ for bare refinement and an inner $k$ for Balaban's RG within each bare theory.

### Strategy

Adopt the script's two-index convention from the start of §5. Add a 1-paragraph "Notation and Strategy" preamble at §5.1 stating:

> *"This proof uses two distinct integer indices. The **outer index $K$** parameterizes a refining sequence of bare lattices: $\Lambda_0(K)$ has spacing $a_0(K) = a^* \cdot 2^{-K}$, where $a^* \gg r_3$ is a fixed reference scale chosen so that the cluster expansion of Section 4 converges. The continuum limit is $K \to \infty$, $a_0(K) \to 0$. The **inner index $k$** parameterizes Balaban's block-spin RG steps within a fixed bare theory: $a_k^{(K)} = 2^k a_0(K)$, coarsening from the bare scale to progressively coarser effective scales. The continuum mass gap $\Delta_\infty$ is the limit of $\Delta_0(K)$ as $K \to \infty$, with each $\Delta_0(K)$ controlled by the cluster expansion (Section 4) at the bare scale and Balaban's UV stability (Section 5.1) within the bare theory. The §5.4 recursion compares form-factor constants $C_K$ vs $C_{K+1}$ between consecutive bare theories. The factor $1/4$ is the kinematic identity $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$, which holds because refining the bare scale by 2 shrinks the dimensionless gap by 2. Convention follows Balaban CMP 109 (1987) p. 251 and Dimock arXiv:1108.1335 (2011) p. 2."*

Then mechanically rewrite §5.1, §5.4, §5.7:

### Concrete steps

**Step 0.1 — Add notation preamble.** Insert the paragraph above at the start of §5.1. Cite Balaban CMP 109 p. 251 and Dimock 2011 p. 2 for the convention.

**Step 0.2 — Rewrite §5.1.2.** Replace
> "At RG step $k$, define a coarser lattice $\Lambda_k$ with spacing $a_k = 2^k a_0$..."

with
> "*Within each fixed bare theory at scale $a_0(K)$, Balaban's block-spin RG generates a sequence of effective actions at progressively coarser scales $a_k^{(K)} = 2^k a_0(K)$, $k = 0, 1, 2, \ldots$. The dimensionless gap at inner step $k$ within bare theory $K$ is $\hat\Delta_k^{(K)} = a_k^{(K)} \cdot \Delta_{\mathrm{phys}} = 2^{k - K} a^* \Delta_{\mathrm{phys}}$, growing in $k$ and shrinking in $K$.*"

**Step 0.3 — Rewrite §5.4.1.** Replace the "step $k$" framing with:
> "*The §5.4 recursion is a comparison between two bare theories at consecutive bare scales $a_0(K)$ and $a_0(K+1) = a_0(K)/2$. It is NOT a single Balaban inner step within a fixed bare theory.*"

**Step 0.4 — Re-derive §5.4.5 under the corrected convention.** The recursion should now read $C_{K+1} = C_K/4 + C_{\mathrm{new}}(K)$, where $C_K$ is the form-factor constant of the IR effective theory of bare theory $K$, and the $1/4$ is the kinematic shrinking $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$. Re-verify the algebra with explicit subscripts.

**Step 0.5 — Re-verify the convergence sum.** Under the corrected convention, $\hat\Delta_K^2 \sim 4^{-(K - K_0)} \hat\Delta_{K_0}^2$, and the sum
$$\sum_K C_K g_K^4 \hat\Delta_K^2 \sim \sum_K K^{\gamma - 2} \cdot 4^{-K}$$
converges by ratio test = $1/4 < 1$. This is the same algebra as in §5.4.6, just with subscripts corrected.

**Step 0.6 — Cross-check §5.7(b) and OS2.** The "$a_k = a_0/2^k$" already appears in §5.7(b) and §5.7(f) OS2; relabel as "$a_0(K) = a^*/2^K$" for consistency.

### Effort

**1 page of notation rewriting**, no new mathematics required. The harder content is in Tier 1.

### Dependencies

None — this is the foundation.

### Risk

**Low.** Pure notation rewrite. The danger is that the rewrite *exposes* the Tier 1 issue (inner-RG K-uniformity) which is currently hidden by the conflation. That exposure is the point — it forces the next step.

---

# Tier 1: Core Rigor

## Gap C1 (continued): Inner-RG K-uniformity

### Diagnosis

After the Tier 0 notation cleanup, the proof structure becomes: for each bare theory $K$, Balaban's inner RG must deliver a form-factor constant whose magnitude is *bounded uniformly in $K$*. The outer recursion then compares these K-uniform constants. But Balaban's published work establishes UV stability *for fixed bare scale* — not the K-uniformity of derived constants like $C_p$, $C_{\mathrm{new}}$, $\zeta$.

Concretely: as $K \to \infty$ (refining), the bare lattice spacing $a_0(K) \to 0$, but the *physical* mass gap $\Delta_{\mathrm{phys}}$ stays fixed. So $\hat\Delta_0^{(K)} = a_0(K) \Delta_{\mathrm{phys}} \to 0$. The cluster-expansion convergence threshold $\beta < a_0(K)/(2\sqrt{N} r_3)$ also shrinks, so the cluster expansion at the bare scale of theory $K$ becomes *narrower* as $K$ grows. The "fine bare lattice" regime is exactly where Balaban's RG is supposed to take over.

But the form-factor constants $C_K$ require *both* the cluster expansion (to set the starting condition $C_K(k=0)$) AND Balaban's RG (to flow it). The K-uniformity question is: can $C_K(k=0)$, $C_{\mathrm{new}}(K)$, $\zeta(K)$, and the Combes-Thomas radius $R_0(K)$ all be bounded *uniformly in $K$* as $K \to \infty$?

### Strategy

Establish three separate K-uniformity statements:

**(i) K-uniform cluster-expansion starting condition.** For each $K$, the cluster expansion at bare scale $a_0(K)$ converges in some window $\beta_0(K) < \beta < \beta_{\max}(K)$ where $\beta_{\max}(K) \sim a_0(K)/r_3 \to 0$ as $K \to \infty$. The starting condition $C_K(k = 0)$ is bounded by the cluster-expansion estimate. We need $C_K(k = 0)$ bounded uniformly in $K$, i.e., the cluster-expansion constants do not blow up as the bare lattice refines.

**(ii) K-uniform Balaban analyticity radius.** The radius $\rho(K)$ of analyticity of polymer activities at bare theory $K$ must be bounded below uniformly in $K$. Balaban's published proofs make this radius depend on $\kappa$, $m_W a_k$, and $r_{\mathrm{proj}}$, where $a_k = 2^k a_0(K)$. The product $m_W a_k$ is *manifestly $K$-independent* (it's a combination of physical constants and the inner-step ratio), so this should be straightforward — but it needs explicit verification under the corrected notation.

**(iii) K-uniform spectral lemma constant $C_p$.** This is the harder one. $C_p$ depends on $\zeta(K)$ which depends on the local Hilbert space dimension on a ball of radius $R_0$. As $K$ grows and $a_0(K)$ shrinks, the *physical* radius $R_0 \cdot a_0(K)$ shrinks (good) but the *number of lattice sites* in the ball grows like $1/a_0(K)^4$ (bad). So $\zeta(K)$ may grow exponentially in $1/a_0(K)^4$ — which is *much worse* than the doubly-exponential decay $4^{-K}$ in the convergence sum.

The fix here is to parameterize the spectral lemma in *physical* units rather than lattice units: the spectral lemma's constant should depend on physical distances (e.g., $r_3$, $\Lambda_{\mathrm{QCD}}^{-1}$), not on $a_0(K)$. This requires reformulating the Combes-Thomas estimate in physical units.

### Concrete steps

**Step 1.1 — Verify that the cluster-expansion constants are K-uniform in physical units.** Re-derive the Theorem 4 bounds with explicit physical scales. The constant $\kappa$ in $|K(X)| \leq e^{-\kappa|X|}$ should be $|X|$ in *physical* units, not lattice units, so that $\kappa$ is K-uniform.

**Step 1.2 — Verify Balaban's analyticity radius is K-uniform.** Read Balaban CMP 95 §3 (propagator Lipschitz constant $C_D$), CMP 98 §E (block-spin projection $r_{\mathrm{proj}}$), CMP 109 §3 (Mayer convergence $\kappa$). For each, write down explicit dependence on $a_k$ and confirm K-independence in physical units. **Estimated effort: 1–2 weeks of careful reading.**

**Step 1.3 — Reformulate the spectral lemma in physical units.** Step 3 of §5.5.3 (the Combes-Thomas/$\zeta$ argument) should be re-derived with $R_0$ being a *physical* radius (in units of $r_3$ or $\Lambda_{\mathrm{QCD}}^{-1}$), not a number of lattice sites. This reformulation is non-trivial because the "local Hilbert space dimension" on a ball of physical radius $R_0$ scales as $\exp(R_0^4 \Lambda^4 \dim G)$ for some physical UV cutoff $\Lambda$, not as $\exp(R_0^4 (1/a)^4 \dim G)$.

The standard tool for this kind of K-uniform local-bound is the **lattice Lieb-Robinson bound** (Nachtergaele–Sims 2006 for the bosonic version; Hastings 2010 for review). Under a Lieb-Robinson bound, the influence of an operator at distance $r$ in physical units is bounded by $e^{-\mu r}$ for some K-uniform $\mu > 0$, regardless of how fine the lattice is.

**Step 1.4 — Prove K-uniformity of $C_{\mathrm{new}}$.** Combine 1.1, 1.2, 1.3 to show $C_{\mathrm{new}}(K) \leq C_*$ uniformly in $K$. This is the linchpin: with K-uniformity, the outer recursion $C_{K+1} = C_K/4 + C_{\mathrm{new}}(K) \leq C_K/4 + C_*$ has a K-uniform fixed point and the convergence sum runs.

**Step 1.5 — Cluster expansion / Balaban RG handoff.** At $k = 0$ in the inner index of bare theory $K$, the bare coupling $g_0(K)$ must be small enough for Balaban's RG to start. If $g_0(K) = O(1)$, the cluster expansion gives $C_K(k=0)$ but Balaban's RG needs $g_0(K)$ small. The handoff is: use the cluster expansion to bound $C_K(k=0)$, then run Balaban's RG forward from there. The Tier 0 notation cleanup makes this explicit, but the actual estimate that Balaban's "first few inner steps" can be controlled non-perturbatively requires §5.7 Remark 1 to be made rigorous.

### Effort

**~1 paper.** Steps 1.1–1.2 are bookkeeping (1–2 weeks). Step 1.3 (Lieb-Robinson reformulation) is the harder piece — possibly 1–2 months for someone fluent with constructive QFT and Lieb-Robinson bounds. Step 1.4 is assembly. Step 1.5 needs careful estimates of the "first few RG steps" non-perturbatively.

### Dependencies

Tier 0 must be done first.

### Risk

**Medium-high.** Step 1.3 (K-uniform spectral lemma) is genuinely hard. If the Combes-Thomas argument cannot be reformulated K-uniformly in physical units, the entire proof structure collapses — there is no other way to get a $K$-independent $C_p$. The hope is that **Lieb-Robinson bounds give exactly what's needed** for lattice gauge theory at fixed physical scale (this has been established for some lattice systems, e.g., quantum spin systems and bosonic field theories on lattices, though not specifically for SU(N) lattice gauge theory in the gapped phase).

**Mitigation:** if Lieb-Robinson is too aggressive, an alternative is the **Aizenman–Holroyd / Kennedy–King decay-of-correlations** approach for spin systems, which gives K-uniform estimates via different machinery. Either way, the existing Combes-Thomas formulation in §5.5.3 needs to be replaced or reformulated.

---

## Gap C3: Cluster expansion / Balaban regime overlap

### Diagnosis

§5.7 Remark 1 says "the first few RG steps $k = 0, 1, 2$ where $g_k^4 = O(1)$ are handled non-perturbatively via the cluster expansion." Under the corrected K/k notation, this means: at the bare scale of theory $K$ ($k = 0$ in the inner index), the bare coupling $g_0(K)$ may be $O(1)$, and the cluster expansion provides a non-perturbative starting condition. The inner Balaban RG then runs from $k = 1$ where $g_k$ is small.

But this hand-off is not made rigorous. Balaban's RG and the cluster expansion are *parallel* tools that control different things: cluster expansion controls *individual* bare lattice mass gaps via polymer convergence; Balaban's RG controls the *flow* of the effective action under coarsening. The hand-off claim is that "after the cluster expansion gives $C_K(k=0)$, Balaban takes over." But this requires the cluster expansion's *output* to be a valid *input* to Balaban's RG, and the precise condition for this is not stated.

### Strategy

Establish a quantitative hand-off lemma: at bare scale $a_0(K)$, the cluster-expansion provides a form-factor bound with constant $C_K(k=0)$, and this constant is a valid starting condition for Balaban's polymer expansion at bare scale $a_0(K)$ (i.e., the polymer activities at $k = 0$ are bounded by $e^{-\kappa|X|}$ with the same $\kappa$ used in Balaban's inner RG).

### Concrete steps

**Step 1.6 — Derive an explicit cluster-expansion bound on Balaban's polymer activities $K_0(X, V)$ at the bare scale.** This requires translating Theorem 4's exponential clustering (rate $\alpha/a$) into Balaban's polymer activity rate ($\kappa$). The translation involves matching the cluster-expansion's Kotecký-Preiss criterion to Balaban's polymer convergence criterion.

**Step 1.7 — Verify quantitative compatibility.** The cluster expansion's exponential rate should be at least Balaban's $\kappa$ at the bare scale. Under the assumption that Balaban's $\kappa$ is a *physical* constant (K-uniform), this becomes a requirement on the cluster expansion's rate at small $a_0(K)$. Verify computationally for $N = 3$ at typical scales.

### Effort

**1–2 pages**, but only meaningful after Tier 1 step 1.3 (K-uniform formulation).

### Dependencies

Tier 1, especially step 1.3.

### Risk

**Low.** Once the K-uniform formulation is in place, the hand-off is bookkeeping.

---

# Tier 2: Technical Fixes (Parallel Workstreams)

These can run in parallel with Tier 1 and don't block Tier 3.

## Gap A1: Weitzenböck spectral gap notation

### Diagnosis

The proof's "$\mu_1 = 6/r_3^2$" and "$m_1 = 2\sqrt{3}/r_3$" are N=3-specific (they correspond to the actual eigenvalue on $\mathbb{CP}^2$). For general $N$, the Weitzenböck lower bound is $2N/r_3^2$ and the actual eigenvalue (per Ikeda–Taniguchi) is $4N/r_3^2$ on $\mathbb{CP}^{N-1}$ — modulo a convention discrepancy with Appendix H (SU(2) on $S^2$ where the value $2/r_2^2$ is given).

### Strategy

Standardize on $\mu_1 \geq 2N/r_3^2$ (the Weitzenböck lower bound) throughout, and N-dependent expressions everywhere $2\sqrt{3}$ appears.

### Concrete steps

**Step 2.1 — Restate Theorem 1 (Section 02) as $\mu_1 \geq 2N/r_3^2$ for $\mathbb{CP}^{N-1}$**, removing the "$\mu_1 = 6/r_3^2$" universal claim. Note in the proof that for $N = 3$ this gives the often-cited value $6/r_3^2$.

**Step 2.2 — Replace "$m_1 = 2\sqrt{3}/r_3$" with "$m_1 = 2\sqrt{N}/r_3$" (or $\sqrt{2N}/r_3$ if using the Weitzenböck lower bound)** throughout the abstract, Section 4.3 (Theorem 2), Section 4.4 (Theorem 4), Section 4.5 (Theorem 5), and Section 5.

**Step 2.3 — Reconcile the "$r_3$" convention between Section 02 / Appendix E (FS metric, $r_3$ defined by holomorphic sectional curvature $4/r_3^2$) and Appendix H (SU(2), $r_2$ defined as the round-sphere radius).** The two conventions differ by a factor of $\sqrt{2}$. Make the convention switch explicit at the start of Appendix H, OR adopt a single convention throughout.

**Step 2.4 — Update §3 quantitative predictions** to use the corrected N-dependent values.

### Effort

**~1 page.**

### Risk

**Low.** Pure notation cleanup.

---

## Gap A3: Lüscher topological charge on coarse lattices

### Diagnosis

The Bogomolny-suppressed-instanton argument uses Lüscher's geometric topological charge $Q_L$, which is well-defined for configurations with $\|1 - U_P\| < \epsilon_L$. The preprint argues this holds for Balaban's small-field domain, but the argument for the *bare* cluster expansion at coarse $a_0$ (where $\beta$ is small and configurations may be rough) is weaker.

### Strategy

Provide an explicit Lüscher-charge applicability check at the bare cluster-expansion scale.

### Concrete steps

**Step 2.5 — At the bare scale of theory $K$, verify that the cluster-expansion-typical configurations (i.e., those dominating the path integral in the convergent regime) satisfy $\|1 - U_P\| < \epsilon_L$.** This is a *moment estimate* on $\|1 - U_P\|$ under the cluster-expansion measure. By Theorem 2 of Section 4.3, the bond activities are $O(e^{-m_1 a_0(K)})$, so deviations from identity are exponentially small.

**Step 2.6 — Quantify the contribution from "rough" configurations** (those with $\|1 - U_P\| > \epsilon_L$) via Markov's inequality + the cluster expansion bound. This contribution should be exponentially small in the convergence margin.

### Effort

**~1 page.**

### Risk

**Low.**

---

## Gap B2: Fredenhagen-Marcu direction of implication

### Diagnosis

The preprint cites FM as if it gives "$\sigma > 0 \Rightarrow \Delta > 0$", but FM actually gives the converse direction via the gauge-invariant order parameter. The "$\sigma > 0 \Rightarrow \Delta \geq c\sqrt{\sigma}$" part is a heuristic flux-tube argument (Appendix F), not a theorem.

### Strategy

State the rigorous chain explicitly: cluster expansion → exponential clustering → spectral gap via transfer matrix and reflection positivity. Drop the "area law implies mass gap" framing.

### Concrete steps

**Step 2.7 — Rewrite §4.3 "Consequences" item 4** to state: "*The connected correlator decay rate $\alpha/a$ from the cluster expansion (Theorem 2) equals the spectral gap of the transfer matrix via reflection positivity and the spectral decomposition. Therefore $\Delta_0 \geq \alpha/a > 0$.*" Drop the "$\Delta_0 \geq c\sqrt\sigma$" claim from the rigorous chain (move it to "consistency check").

**Step 2.8 — Rewrite §4.4 Theorem 4 part (e)** similarly, with the rigorous chain being cluster expansion → clustering → spectral gap.

**Step 2.9 — Move Appendix F's flux-tube derivation to a "physics check" remark.** Acknowledge it as a heuristic that gives the right order of magnitude but is not a step in the rigorous proof.

### Effort

**~1 page.**

### Risk

**Low.** This is a presentation cleanup; the rigorous chain (cluster expansion → spectral gap) is already implicit in the existing text.

---

## Gap C2: Large-field exponent optimization

### Diagnosis

Balaban's small-field condition $|F| < g_k^{1-\epsilon}$ with $\epsilon = 1/4$ gives a large-field bound $O(e^{-c/g_k^{1/2}})$, which is borderline at moderate $g_k$. For $g_k \sim 0.1$, $e^{-c/0.316} \sim e^{-3c}$, comparable to $g_k^4 \sim 10^{-4}$.

### Strategy

Choose $\epsilon$ to make the large-field bound *strongly* sub-leading to $g_k^4$ uniformly along the AF trajectory.

### Concrete steps

**Step 2.10 — Solve the optimization problem.** Find $\epsilon^* \in (0, 1/4]$ such that $e^{-c/g_k^{2\epsilon^*}}$ decays faster than any power of $g_k$ for the target range $g_k \in [0, g_0]$ AND the small-field domain still admits the polymer expansion. Take $\epsilon^* = 1/100$ as a candidate: large-field bound becomes $e^{-c/g_k^{50}}$, vastly smaller than any power. Verify the polymer expansion still converges in $|F| < g_k^{0.99}$.

**Step 2.11 — Update §5.5.3 "Non-perturbative contributions to $\epsilon_B$"** with the optimized $\epsilon^*$ and verify the bound is sub-leading along the AF trajectory.

### Effort

**~1 page** (the optimization is straightforward once formulated).

### Risk

**Low to medium.** The risk is that polymer expansion convergence requires $|F| < $ a specific function of $g_k$ that the literature pins to $g_k^{1-\epsilon}$ with $\epsilon \geq 1/4$, in which case smaller $\epsilon$ fails. Need to check Balaban CMP 119 §3 for the actual bound.

---

## Gap D3: Combes-Thomas locality vs. polymer expansion

### Diagnosis

The spectral lemma (§5.5.3 Step 3) applies Combes-Thomas to "an operator with support radius $R_0 = O(1)$", but Balaban's polymer expansion generates operators that are *sums* of polymer activities with *unbounded* support (the exponential decay $e^{-\kappa|X|}$ provides convergence, not a hard cutoff). The Combes-Thomas estimate, applied to a single local operator, doesn't directly handle this.

### Strategy

Re-derive the spectral lemma estimate as a sum over polymer activities, applying Combes-Thomas to *each* activity individually (with the activity's specific support radius) and summing with the polymer-expansion convergence factor.

### Concrete steps

**Step 2.12 — State the spectral lemma for individual polymer activities.** For each $K(X, V)$ with support $X$, the spectral lemma applies with $R_0 = |X|$. The bound is $|\langle 1|K(X, V)|1\rangle_c| \leq C_p(|X|) \cdot \|K(X)\| \cdot \hat\Delta^p$, where $C_p(|X|)$ depends on the polymer size.

**Step 2.13 — Sum over polymers.** The total bound is $\sum_X C_p(|X|) e^{-\kappa|X|} \hat\Delta^p$. The $C_p(|X|)$ growth is at most exponential in $|X|^d$ (from the local Hilbert space dimension), but the polymer convergence factor $e^{-\kappa|X|}$ is exponential in $|X|$. **This is potentially marginal** — if $C_p(|X|)$ grows faster than $e^{-\kappa|X|}$ shrinks, the sum diverges.

The fix here is the same as Tier 1 step 1.3: the local Hilbert space dimension should be measured in *physical* units, where the polymer of size $|X|$ has physical extent $|X| \cdot a_0(K)$, and the local dimension on a ball of physical radius $r$ is bounded by $\exp(C r^d \Lambda^d \dim G)$ for some physical UV cutoff $\Lambda$ — *NOT* by $\exp(C |X|^d \dim G)$ in lattice units.

This is again a Lieb-Robinson reformulation.

### Effort

**1–3 pages**, depending on whether Tier 1 step 1.3 is done in parallel.

### Dependencies

Best done together with Tier 1 step 1.3 (K-uniform spectral lemma).

### Risk

**Medium.** Same as Tier 1 step 1.3.

---

## Gap F1: Coincident-point singularities

### Diagnosis

The proof's bound $|S_n(x_1, \ldots, x_n)| \leq C^n n! \prod_{i<j} (1 + |x_i - x_j|^{-2}) e^{-\Delta \mathrm{diam}}$ asserts a $|x|^{-2}$ singularity at coincident points and uses dimension counting to argue local integrability. The bound is *asserted*, not *derived*, and it appeals to "the OPE" which has not been constructed (see G4(d)).

### Strategy

Provide a direct estimate of coincident-point behavior that does not rely on a constructed OPE.

### Concrete steps

**Step 2.14 — Use the spectral representation.** For the connected 2-point function in a massive gapped theory, the Källén-Lehmann representation gives
$$|S_2^c(x, y)| \leq \int \rho(m) \cdot \frac{e^{-m|x-y|}}{|x-y|^2} dm$$
where $\rho(m)$ is the spectral density. With $\rho$ supported on $[\Delta, \infty)$, this gives the bound $|S_2^c| \leq C |x-y|^{-2} e^{-\Delta|x-y|}$ — exactly what the proof claims, but via an explicit derivation.

**Step 2.15 — Higher-$n$ via clustering.** For $n \geq 3$, use the cluster decomposition to bound $S_n$ in terms of products of lower-$n$ functions. The "iterated coincident-point" estimate then follows from the 2-point bound applied at each level.

**Step 2.16 — Verify local integrability rigorously.** The lemma's claim "for $n \leq 4$ the integral converges" should be turned into an explicit calculation: dimension counting in $\mathbb{R}^{4n}$, integrate against the worst-case singularity, verify finiteness.

### Effort

**~2 pages.**

### Risk

**Low to medium.** The Källén-Lehmann approach gives the right answer for the 2-point function. For higher $n$, it may turn out that the worst-case singularity is *worse* than $|x|^{-2}$ near the simultaneous-collision diagonal, in which case the local integrability claim needs revisiting.

---

## Gap F2: Reflection positivity topology specification

### Diagnosis

§5.7(f) OS3 Step 2 uses Portmanteau on $F_f(\phi) = \overline{f[\phi|_+]} \cdot f[\theta^*\phi|_+]$, requiring $F_f$ to be a bounded continuous function on field space. The "topology on field space" is left unspecified, but it matters: Portmanteau requires the *same* topology under which the measures $\mu_a$ converge weakly.

### Strategy

Specify the topology explicitly and verify continuity of $F_f$.

### Concrete steps

**Step 2.17 — Use the weak-$*$ topology on $\mathcal{S}'(\mathbb{R}^4)$** (tempered distributions). The lattice measures $\mu_a$ are supported on configurations $\phi$ that are step functions; in the continuum limit, $\mu_a$ converges weak-$*$ on $\mathcal{S}'(\mathbb{R}^4)$ to a measure $\mu$ on the same space.

**Step 2.18 — Verify $F_f$ is weak-$*$ continuous.** For a Schwartz-class $f$, the pairing $\phi \mapsto \langle f, \phi\rangle$ is weak-$*$ continuous on $\mathcal{S}'(\mathbb{R}^4)$ by definition. The product $F_f(\phi) = \overline{\langle f|_+, \phi\rangle} \cdot \langle f|_+, \theta^*\phi\rangle$ is then continuous as a product of continuous functions.

**Step 2.19 — Verify $F_f$ is bounded.** Boundedness on the *full* space of distributions is *false* (a delta function gives unbounded values). The right statement is: $F_f$ is bounded on the *support* of $\mu_a$, which is a subset where field configurations are uniformly bounded (because the lattice gauge field is a compact-group-valued variable, so $|\phi|$ is uniformly bounded on lattice configurations). The continuum limit measure $\mu$ inherits this boundedness on its support.

### Effort

**~1 page.**

### Risk

**Low.** Standard functional analysis.

---

## Gap F5: Non-triviality logic hole

### Diagnosis

The §5.7(f) Proposition (Non-triviality) lists three signatures and says "Any one of (i) or (ii) alone suffices". Signature (ii) is a non-zero connected 2-point function — but a *free* massive scalar has a non-zero 2-point function, so (ii) does not exclude the Gaussian case. Only (i) (string tension) and (iii) (asymptotic freedom) genuinely distinguish the constructed theory from a free theory.

### Strategy

Drop the "(ii) alone suffices" claim. Use (i) (positive string tension is incompatible with a free gauge theory which has perimeter law) and (iii) (asymptotically free running with $b_0 > 0$ is incompatible with a free theory which has $b_0 = 0$).

### Concrete steps

**Step 2.20 — Rewrite the Proposition.** Replace "Any one of (i) or (ii) alone suffices" with "Any one of (i) or (iii) alone suffices. (ii) alone is not sufficient, since a free massive scalar field has a non-vanishing 2-point function. (ii) is included as a positive lower bound on the lightest glueball matrix element, which is auxiliary information needed for later steps (e.g., the OPE construction)."

**Step 2.21 — Strengthen (iii).** The "asymptotic freedom" signature is currently stated qualitatively. Strengthen by computing $b_0$ explicitly and showing that the 2-point function's short-distance behavior (which the proof should construct in Tier 3) has the AF logarithmic running characteristic of $b_0 > 0$ — distinct from any power-law behavior of a free theory.

### Effort

**~1 paragraph** for the immediate fix; the strengthening of (iii) ties into Tier 3 G4(b).

### Risk

**Low.**

---

# Tier 3: Clay Structural Ingredients

These are the heavy-lifts. Each is a substantive piece of constructive QFT.

## Gap G4(a): Renormalized composite operators

### Diagnosis

The preprint constructs Schwinger functions of *bare* lattice composites ($s_P(x) = 1 - (1/N) \mathrm{Re}\,\mathrm{Tr}\,U_P$, etc.). These are not the same as renormalized continuum operators $[\mathrm{Tr}\,F^2]_R(x)$ with multiplicative renormalization $Z_O(a)$ chosen to give finite continuum correlators with the correct AF anomalous dimension.

### Strategy

Construct the renormalized $\mathrm{Tr}\,F^2$ operator via point-splitting, computing its anomalous dimension perturbatively, and verifying that the renormalized 2-point function converges to a finite distribution as $a \to 0$.

### Concrete steps

**Step 3.1 — Define the bare lattice operator.** $\mathcal{O}^{\mathrm{bare}}(x) = (2N/(a^4 g^2)) s_P(x)$, where $s_P(x)$ is averaged over the four plaquettes touching site $x$ (to make it scalar under the hypercubic group).

**Step 3.2 — Compute the lattice 1-loop anomalous dimension.** Use the result from Caracciolo–Curci–Menotti–Pelissetto (1992) or similar for the lattice anomalous dimension of $\mathrm{Tr}\,F^2$. The result is $\gamma_O(g) = -2 b_0 g^2 + O(g^4)$ (or a similar coefficient).

**Step 3.3 — Define the renormalized operator.** $[\mathrm{Tr}\,F^2]_R(x) = Z_O(a) \cdot \mathcal{O}^{\mathrm{bare}}(x)$, where $Z_O(a) = (\log(1/(a\Lambda)))^{-\gamma_O/(2 b_0)}$ is chosen to absorb the leading log divergence.

**Step 3.4 — Verify the renormalized 2-point function has a finite continuum limit.** $\lim_{a \to 0} Z_O(a)^2 \cdot \langle \mathcal{O}^{\mathrm{bare}}(x) \mathcal{O}^{\mathrm{bare}}(y)\rangle$ should be finite for $x \neq y$. This is the classical Symanzik program for composite operator renormalization.

**Step 3.5 — Compute the leading short-distance behavior.** For $|x-y| \to 0$, the renormalized 2-point function should behave as $|x - y|^{-2(d_O + \gamma_O)}$ (with $d_O = 4$), modulo logarithmic corrections from the running coupling.

**Step 3.6 — Repeat for higher-spin / higher-dimension operators** (the full Lüscher-Weisz basis): $\mathrm{Tr}(F_{\mu\nu}^2)$, $\mathrm{Tr}(F_{\mu\nu}F_{\rho\sigma}F_{\sigma\nu})$ (after $\mathcal{C}$-reduction), $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$, etc. Each gets its own $Z_O(a)$.

### Effort

**~1 paper.** This is a known program (Symanzik improvement, Brandt 1971, Hill 1996) but has never been executed rigorously in the constructive QFT setting. The hard part is showing that the lattice $Z_O(a)$ defined perturbatively can be made non-perturbative via Balaban's RG.

### Dependencies

Tier 0, Tier 1.

### Risk

**Medium-high.** The Symanzik composite operator program has been completed for free fields (Hollands-Wald) and for super-renormalizable theories ($\phi^4_3$ — Glimm-Jaffe, others). For non-Abelian gauge theory in 4D, it has *never* been done rigorously. This is one of the open problems in mathematical physics. The preprint's authors are essentially asked to either solve it, or restrict their claim to "Schwinger functions of gauge-invariant lattice observables" (which is *not* a Wightman field theory).

**Mitigation:** A "soft" version is to construct the renormalized operator's *Schwinger function* (just the correlator, not the operator itself) via the lattice continuum limit + perturbative $Z_O(a)$, and verify the asymptotic behavior matches AF. This is *weaker* than constructing operator-valued distributions, but it might satisfy the J-W "correlation functions of the quantum field operators should agree at short distances with AF" requirement at the level of Schwinger functions.

---

## Gap G4(b): Short-distance AF match

### Diagnosis

Jaffe-Witten requires "*correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory*." The preprint's bound $|S_2| \leq C|x-y|^{-2} e^{-\Delta|x-y|}$ does NOT match this — it has the *free* short-distance singularity, not the AF-corrected one.

### Strategy

After Tier 3 (a) constructs the renormalized 2-point function, compute its short-distance asymptotics and compare with the perturbative one-loop result.

### Concrete steps

**Step 3.7 — Compute the perturbative AF prediction** for the 2-point function of $\mathrm{Tr}\,F^2$ at one loop. Standard textbook result: $\langle \mathrm{Tr}\,F^2(x) \mathrm{Tr}\,F^2(0)\rangle \sim |x|^{-8} \cdot (1 + \alpha_s(\mu)/(\pi) \cdot \mathrm{stuff})$ where $\alpha_s$ runs logarithmically.

**Step 3.8 — Show the renormalized lattice 2-point function reproduces this** as $a \to 0$ and $|x| \to 0$. This requires a *uniform* continuum limit + short-distance asymptotic analysis. The formal limit gives the right answer if the lattice perturbative expansion matches continuum perturbation theory at one loop, which is the standard Reisz-Weinberg power-counting result.

**Step 3.9 — Verify the higher-order matching** at two loops or beyond. Optional but recommended for a Clay submission.

### Effort

**~1/2 paper to 1 paper**, conditional on Tier 3 (a) being done.

### Dependencies

Tier 3 (a).

### Risk

**Medium.** The perturbative matching is standard, but rigorous (non-perturbative) verification that the constructed lattice limit *equals* the perturbative answer at short distances requires a "perturbative agreement theorem" that constructive QFT typically achieves only for super-renormalizable theories. For 4D YM, this is again open, but more accessible than the full operator construction.

---

## Gap G4(c): Stress tensor

### Diagnosis

Jaffe-Witten requires the existence of a stress-energy tensor $T_{\mu\nu}(x)$ on the reconstructed Hilbert space. The canonical YM stress tensor is gauge-non-invariant; the gauge-invariant version requires the Belinfante-Rosenfeld improvement. The preprint does not address this at all.

### Strategy

Construct the Belinfante-Rosenfeld improved stress tensor on the lattice, take the continuum limit, and verify conservation as a distributional Ward identity.

### Concrete steps

**Step 3.10 — Define the lattice stress tensor.** The lattice analogue of the BR improved stress tensor for YM is
$$T_{\mu\nu}^{\mathrm{lat}}(x) = -\frac{1}{g^2}\left[\mathrm{Tr}(F_{\mu\rho}F_{\nu}{}^\rho) - \frac{1}{4}\delta_{\mu\nu} \mathrm{Tr}(F_{\rho\sigma}F^{\rho\sigma})\right](x)$$
where the $F_{\mu\nu}$ are clover-improved lattice field strengths.

**Step 3.11 — Renormalize.** The lattice stress tensor needs its own multiplicative renormalization $Z_T(a)$. Standard result (Caracciolo-Pelissetto and others): $Z_T = 1 + O(g^2)$ at one loop, with explicit lattice computation.

**Step 3.12 — Verify conservation.** $\partial^\mu T_{\mu\nu} = 0$ should hold as a distributional Ward identity in the continuum limit. Use the Schwinger-Dyson equation already derived in §5.7(f), which gives the *equation of motion* of the field — the Ward identity for $T_{\mu\nu}$ then follows from the YM action's translation invariance.

**Step 3.13 — Verify positivity.** $T_{00}(x)$ should give $H \geq 0$ on the GNS Hilbert space, which is automatic from the OS reconstruction (the Hamiltonian from the transfer matrix is positive).

### Effort

**~1 paper.**

### Dependencies

Tier 3 (a) (renormalized composite operators, since $T_{\mu\nu}$ is a composite of $F$'s).

### Risk

**Medium.** The stress tensor construction has been done in 2D (Polyakov, Friedan) and in some toy models, but for 4D YM it requires the same composite operator machinery as G4(a). Once that machinery exists, $T_{\mu\nu}$ is a relatively direct application.

---

## Gap G4(d): Operator product expansion

### Diagnosis

Jaffe-Witten requires "*an operator product expansion, having prescribed local singularities predicted by asymptotic freedom*." The preprint asserts an OPE in the coincident-point lemma but does not construct one.

### Strategy

Establish the leading OPE for two stress-tensor or two field-strength operators, with coefficients computed at one loop.

### Concrete steps

**Step 3.14 — State the OPE structure.** For two gauge-invariant operators $\mathcal{O}_1, \mathcal{O}_2$ at points $x, y$ with $|x - y| \to 0$:
$$\mathcal{O}_1(x) \mathcal{O}_2(y) \sim \sum_k C_{12}^k(x - y) \cdot \mathcal{O}_k\left(\frac{x+y}{2}\right)$$
where $\mathcal{O}_k$ ranges over local operators of dimension $\geq d_1 + d_2$, and $C_{12}^k(x-y)$ has explicit short-distance behavior $|x-y|^{d_k - d_1 - d_2}$ modulo logarithms.

**Step 3.15 — Compute the leading OPE coefficient at one loop.** For $\mathcal{O}_1 = \mathcal{O}_2 = \mathrm{Tr}\,F^2$, the leading singular operator is the identity, with coefficient $C^I(x - y) \sim |x - y|^{-8}$ (modulo logs from the anomalous dimension). The next operator is $\mathrm{Tr}\,F^2$ itself, with coefficient $\sim |x-y|^{-4}$. Compute these coefficients perturbatively using lattice + continuum agreement.

**Step 3.16 — Verify the OPE as a distributional identity.** The OPE as a relation between Schwinger functions: for any test function $f$ supported in a small ball, $\int f(x) f(y) \langle \mathcal{O}_1(x) \mathcal{O}_2(y) X\rangle \sim \sum_k \int f \cdot C_{12}^k \cdot \langle \mathcal{O}_k X\rangle$ for any product of additional operators $X$ at distant points.

**Step 3.17 — Verify AF agreement of OPE coefficients.** The leading coefficient $C^I(x - y) \sim |x|^{-8}$ should have logarithmic corrections matching one-loop QCD. This is the same matching as G4(b) but at the level of OPE coefficients.

### Effort

**~1 paper, possibly 2.**

### Dependencies

Tier 3 (a), (b).

### Risk

**High.** A rigorous OPE for non-Abelian gauge theory in 4D is one of the major open problems in mathematical physics. Hollands-Wald have done it for free fields in curved spacetime; Bostelmann has worked on the lattice OPE for $\phi^4$; but the gauge case is open.

**Mitigation:** A *partial* OPE — the leading singular term in the coefficient functions, computed perturbatively — may suffice for Clay's "having prescribed local singularities predicted by asymptotic freedom" requirement. Full nonperturbative OPE is beyond current technology.

---

# Tier 4: Gauge Group Extension

## Gap G1(b)/I.4/K: All compact simple gauge groups

### Diagnosis

The body proof works only for SU(N). Appendix I.4 + K identify the relevant homogeneous spaces ($\mathbb{HP}^{N-1}$ for Sp(N), $G/H$ for the exceptionals) but do not execute the full proof for any group beyond SU(N).

### Strategy

For each compact simple group $G$, redo the proof with the appropriate homogeneous space.

### Concrete steps (per group)

**Step 4.1 (SO(N)) — Internal space $S^{N-1}$ or $\mathbb{R}P^{N-1}$.** Compute the Hodge Laplacian spectrum on 1-forms (standard, Ikeda-Taniguchi). Verify cluster expansion convergence with the SO(N) bond activity. Verify the dimension-6 operator classification (the cubic Casimir $d^{abc}$ exists for SO(N) with $N \geq 7$ and is $\mathcal{C}$-odd, so the same elimination works). Verify Balaban's analyticity and form-factor recursion for SO(N).

**Step 4.2 (Sp(N)) — Internal space $\mathbb{HP}^{N-1}$.** Compute the Hodge Laplacian spectrum (less standard but known: Berger-Gauduchon-Mazet 1971). Repeat the cluster expansion + dimension-6 + Balaban steps.

**Step 4.3 ($G_2, F_4, E_6, E_7, E_8$).** Each requires:
- The relevant homogeneous space $G/H$.
- The Hodge Laplacian spectrum on 1-forms (computed via the representation-theoretic decomposition; standard for symmetric spaces).
- The Lie algebra structure for the dimension-6 classification.
- Balaban's construction generalized to the structure constants of $G$.

For $G_2$ ($G/H = G_2/\mathrm{SU}(3)$, dim 6), this is computationally feasible. For $F_4$ ($G/H = F_4/\mathrm{Spin}(9)$, dim 16) and beyond, the computations grow but are still finite.

**Step 4.4 — Universal argument.** Once each group is checked, package the result as a single theorem: "For any compact simple gauge group $G$, choose the homogeneous space $G/H$ from the table; the proof of Sections 4-5 (with $G$-dependent constants) gives $\Delta_\infty(G) > 0$."

### Effort

**~1–2 papers**, depending on how much can be packaged universally vs. how much is group-by-group.

### Dependencies

SU(N) case must be airtight first. If Tier 0+1 are not done, the same notation/K-uniformity bugs propagate to every group and the work is wasted.

### Risk

**Medium.** The structural argument generalizes naturally — every compact simple group has a positively-curved symmetric space — but the *constants* (cluster-expansion threshold, Balaban radius, spectral lemma constant) need to be computed group-by-group. Some computations may turn out to be hard for the exceptional groups due to large adjoint representation dimensions.

**Alternative:** Restrict the Clay claim to SU(N) explicitly. Jaffe-Witten asks for "any compact simple gauge group $G$", so this *would not* satisfy the full Clay requirement, but it would still be a substantive contribution and a referee might accept it as "partial Clay solution" with the understanding that the extension is mechanical.

---

# Phasing Recommendation

## Phase 1: 3 months — Foundation cleanup

- **Tier 0** (notation cleanup): 2 weeks.
- **Tier 1 step 1.1, 1.2** (verify K-uniformity of cluster expansion + Balaban radius): 4–6 weeks.
- **Tier 2 fixes A1, A3, B2, F2, F5** (notation/clarity fixes): 4 weeks parallel.

**Output:** A clean v2 of §§5.1–5.4 with the K/k separation explicit and the easy notation issues fixed.

## Phase 2: 6 months — Inner-RG K-uniformity

- **Tier 1 step 1.3** (Lieb-Robinson reformulation of spectral lemma): 4–6 months. This is the hardest step in the entire program.
- **Tier 1 steps 1.4, 1.5, 1.6, 1.7** (K-uniformity assembly + cluster/Balaban handoff): 2 months.
- **Tier 2 fixes C2, D3, F1** (technical fixes that depend on the Lieb-Robinson reformulation): 2 months parallel.

**Output:** A clean §5 with K-uniformity established and the convergence sum proved rigorously under the corrected convention.

## Phase 3: 12 months — Clay structural ingredients

- **Tier 3 (a)** (renormalized composite operators): 4–6 months. The hardest individual piece. May fail or require restriction to "Schwinger functions only."
- **Tier 3 (b)** (AF short-distance match): 2 months, conditional on (a).
- **Tier 3 (c)** (stress tensor): 2–3 months, conditional on (a).
- **Tier 3 (d)** (OPE): 4–6 months, conditional on (a)+(b)+(c). May fail or require restriction to leading-order OPE.

**Output:** A constructive QFT framework satisfying the J-W structural requirements, at least for SU(N).

## Phase 4: 6 months — Gauge group extension

- **Tier 4** (other compact simple groups): 4–6 months, working group-by-group or building a universal framework.

**Output:** Clay submission for "any compact simple gauge group $G$".

**Total: 27 months.** The hard sub-problems are Phase 2 (Lieb-Robinson reformulation) and Phase 3 (composite operators and OPE), each of which could fail and would require either alternative approaches or restriction of the claimed result.

---

# Decision Points

At each phase, the authors should evaluate whether the next phase is feasible:

**After Phase 1:** Is the K/k separation clean? If yes, proceed to Phase 2. If no (e.g., the inner-RG K-uniformity is harder than expected), consider restricting the claim to "lattice mass gap at coarse $a$" without claiming the continuum limit.

**After Phase 2:** Does Tier 1's K-uniformity hold? If yes, the SU(N) lattice → continuum chain is rigorous. Decide whether to proceed to Phase 3 (full Clay submission) or to publish the result as "rigorous SU(N) continuum mass gap" without claiming the full Clay framework.

**After Phase 3:** Does Tier 3 succeed? If composite operators / OPE / stress tensor cannot be constructed, the result is "SU(N) continuum mass gap with Schwinger functions but not Wightman field operators". This is a substantive result but does NOT satisfy the full Clay statement. The authors should be candid about which Clay requirements are met vs. unmet.

**After Phase 4:** Extension to other groups. If any group fails (e.g., the exceptionals turn out to have technical obstructions), restrict the claim to the groups that work.

---

# Honest Assessment

The preprint as written is **not Clay-ready** but contains **substantial original mathematics**:

1. The dimension-6 operator classification + stability of deviation order argument (Sections 5.3, 5.5, 5.6) is a genuine technical innovation. **This work should be published independently** as a contribution to the Balaban RG program, even before the Clay claim is resolved.

2. The Theorem 5 IR equivalence via reduced transfer matrix + Feshbach is a clean rigorous result. **This too can be published independently**.

3. The cluster expansion at coarse lattices via the KK enhancement (Section 4) is a complete proof of $\Delta_0 > 0$ at the lattice level. **This is also publishable independently**.

What is *not* in the preprint is:
- A clean proof of the $a \to 0$ continuum limit (blocked by the K-vs-k issue).
- The Clay structural framework (renormalized operators, stress tensor, OPE).
- The extension to all compact simple groups.

**Recommendation:** Split the preprint into three independently publishable papers (lattice mass gap; IR equivalence; deviation order), and treat the Clay submission as a longer-term program addressing the outstanding gaps in tiered fashion.

Each of those three papers can be a strong *independent* contribution to constructive QFT, and the Clay submission (when ready) can cite them as building blocks. This is a more honest framing than claiming a complete Clay solution for an incomplete proof.
