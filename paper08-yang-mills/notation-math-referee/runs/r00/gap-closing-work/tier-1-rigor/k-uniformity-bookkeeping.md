# K-Uniformity Bookkeeping: Cluster-Expansion Starting Condition and Balaban's Analyticity Radius

**Tier 1 / Steps 1.1 + 1.2.** **Date:** 2026-04-08. **Scope:** bookkeeping audit, under the Tier 0 K/k separation, of whether the constants that enter (i) the cluster-expansion bound at bare scale $a_0(K)$ and (ii) Balaban's analyticity radius are bounded uniformly in the outer bare-refinement index $K$. No new mathematics; no preprint edits.

**Notation recap.** Outer index $K$: $a_0(K) = a^* 2^{-K}$, $a^* \gg r_3$ fixed. Inner index $k$ (within bare theory $K$): $a_k^{(K)} = 2^k a_0(K) = 2^{k-K} a^*$. Physical gap $\Delta_{\mathrm{phys}}$ is $K$-independent; $\hat\Delta_K = a_0(K)\Delta_{\mathrm{phys}}$, $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$. The continuum limit is $K\to\infty$. The spectral-lemma constant $C_p$ is explicitly deferred to Tier 1 Step 1.3 / Tier 2 D3.

---

## Section 1 — K-uniformity of the cluster-expansion starting condition (Step 1.1)

The starting condition at $k = 0$ of bare theory $K$ is the cluster-expansion bound from §§4.3–4.4 applied at lattice spacing $a_0(K)$. Theorem 4(c) asserts exponential clustering with rate $m \geq \alpha/a_0(K) > 0$; the form-factor constant $C_K(k=0)$ is extracted from Theorem 2's bond bound $|g_b| \leq C_0 e^{-m_1 a_0(K)}$ and Theorem 3's Kotecký–Preiss condition $2\beta + \alpha < m_1 a_0(K)/6 - \ln(c_d K C_0^{1/6})$.

### 1.1 Bond constant $C_0$ (Theorem 2)

$C_0 = C_4$ (preprint `04-lattice-proof-part1.md` lines 556–563) is the prefactor in the integrated KK-propagator sum $\sum_{n\geq 1} d_n G_n(a)/(m_n a) \leq C_3 e^{-m_1 a}$ on $\mathbb{CP}^{N-1}$, via Weyl's law $d_n \sim n^{N-2}$ and $m_n \sim n^{1/(2(N-1))}/r_3$. The proof runs at generic lattice spacing $a$; nothing distinguishes $a_0(K)$ from $a^*$. $C_0$ is dimensionless and depends on $K$ only through the ratio $a_0(K)/r_3$. In the preprint's regime of validity $a_0(K)/r_3 \gg 1$ (i.e. $K \leq K_{\max}(a^*/r_3)$), $C_0$ is a smooth, monotone, bounded function of $K$, with $C_0(K) \leq C_0^* = C_0(a^*/r_3, N)$ achieved at $K = 0$. **Verdict: K-uniform in the regime of validity.**

### 1.2 KP convergence threshold $\beta_{\max}(a_0(K))$

From Theorem 3: $\beta_{\max}(a) = m_1 a/6 - \ln(c_d K_{\mathrm{meas}} C_0^{1/6}) - \alpha/2$. With $m_1 = 2\sqrt{N}/r_3$:
$$\beta_{\max}(a_0(K)) = \frac{\sqrt{N}\,a^*}{3 r_3}\cdot 2^{-K} + O(\ln K).$$
The leading term *shrinks* geometrically like $2^{-K}$. **As $K \to \infty$, $\beta_{\max}(K) \to 0$: the bare convergence window in $\beta$ narrows monotonically.** This is the central concern flagged in the task prompt, and it is real: asymptotic freedom requires $\beta_0(K) \to \infty$, but the cluster-expansion window requires $\beta_0(K) < \beta_{\max}(K) \to 0$. These pull in opposite directions. **Consequence: the Section 4 cluster expansion is a strong-coupling tool, valid only in the coarse regime, and cannot provide the starting condition $C_K(k=0)$ at every $K$.** The resolution (§1.5 below) is that the cluster expansion supplies the starting condition at the *coarse* reference bare scale only, and Balaban's inner RG supplies it at fine bare scales via a handoff at a fixed reference inner slice.

### 1.3 Exponential clustering rate $\alpha/a_0(K)$ in Theorem 4(c)

Dimensionless $\alpha$ is $K$-independent (a KP weight of order unity). The *physical* rate is $\alpha/a_0(K) = (\alpha/a^*)\cdot 2^K$, which *grows* unboundedly. As a multiple of any fixed physical scale (e.g. $r_3^{-1}$ or $\Lambda_{\mathrm{phys}}$), the rate grows by a factor $2^K$. This is the *favourable* direction: the CE bound remains comfortably above every physical mass as the lattice refines. **The physical clustering rate is K-uniform from below** (bounded from below by a fixed $r_3^{-1}$, in fact growing unboundedly). This is not a problem — the form-factor bound needs the rate to exceed the physical gap, which is trivially satisfied.

### 1.4 Measure factor $K_{\mathrm{meas}}$ and lattice-animal constant $c_d$

Both $K$-independent: $K_{\mathrm{meas}}$ depends on $N$ only (Haar + Gaussian on internal fields); $c_d$ is the $d=4$ lattice-animal growth constant. **Verdict: K-uniform.**

### 1.5 Precise statement for Step 1.1

Let $C_{\mathrm{CE}}(K) := C_K(k=0)$.

**Conditional K-uniformity.** *In the strong-coupling regime $K \leq K_{\max}(a^*/r_3)$, $C_{\mathrm{CE}}(K) \leq C_0^*(N, r_3, \Lambda_{\mathrm{phys}})$ $K$-uniformly, with $C_0^*$ depending only on $N$, $r_3$, and the physical scale $\Lambda_{\mathrm{phys}}$.*

For $K > K_{\max}$, the bare cluster expansion fails to converge at $a_0(K)$ and the starting condition must be supplied by Balaban's inner RG, evaluated at the coarse inner slice $k = K$ where $a_K^{(K)} = a^*$ *coincides with the reference bare scale* at which Section 4 does converge. The handoff is Tier 1 Step 1.5 (the C3 lemma) and is outside the scope of this bookkeeping.

The apparent non-uniformity of the bare convergence window is therefore not a failure but a regime-of-validity statement: cluster expansion and Balaban's inner RG control complementary regions, joined at the fixed reference inner slice $a^*$.

---

## Section 2 — K-uniformity of Balaban's analyticity radius (Step 1.2)

From `05-continuum-limit.md` §5.6 Part I (I.3 at line 1502) and `H-balaban-analyticity.md` §3:
$$\rho \;=\; \min\!\left(\frac{\kappa}{2d},\; \frac{m_W a}{2 C_D},\; r_{\mathrm{proj}}(N)\right).$$
We audit each factor with $a$ interpreted as $a_k^{(K)} = 2^k a_0(K)$.

### 2.1 $\kappa$ — polymer decay rate (Balaban CMP 109 §3)

Per `H-balaban-analyticity.md` §3 Step (c) and the inductive proof in `K-balaban-general-groups.md` lines 272–275:
$$\kappa(G) = \kappa_0 - C_1 d_G \ln(\max(4 d\, d_G/m_W^2,\, 2)),$$
with $\kappa_0 \sim m_W a_k$ the "bare Boltzmann suppression per polymer element". Balaban's convention (CMP 95–119, confirmed by `K-balaban-general-groups.md` line 64: "the ratio $m_W a_k$ is held fixed through the RG") treats $m_W$ as a $K$-indexed regulator with $m_W(K) \cdot a_0(K) = \mu_W$ fixed dimensionless. Then $m_W(K)$ *in physical units* scales as $\mu_W \cdot 2^K/a^*$: it is a cutoff-scale UV regulator, not a physical mass. With $\mu_W$ fixed, $\kappa_0 = \mu_W$, $d_G = N^2 - 1$, and $d = 4$ are all $K$-independent, so $\kappa$ is literally $K$-independent. **Verdict: K-uniform**, $\kappa \geq \kappa_*(N, \mu_W, d) > 0$.

### 2.2 $m_W a_k^{(K)}$ — fluctuation mass × inner scale

**Claim.** $m_W a_k^{(K)} = \mu_W \cdot 2^k$, $K$-independent at fixed inner $k$.

**Proof.** $m_W(K) a_k^{(K)} = m_W(K) \cdot 2^k a_0(K) = \mu_W \cdot 2^k$. $\square$

Hence $m_W a_k^{(K)}/(2 C_D) = \mu_W 2^k/(2 C_D)$, $K$-independent at each inner $k$; at the bare slice $k = 0$ it equals $\mu_W/(2 C_D)$. This is exactly what `05-continuum-limit.md` line 1489 asserts, once "$k$" there is read as inner index. **Verdict: K-uniform at each $k$**, in particular at $k = 0$.

### 2.3 $C_D$ — Lipschitz constant of $D^2[V]$

From `K-balaban-general-groups.md` K.2(b) lines 105–112: $C_D \leq 2 d\, d_G = 2\cdot 4 \cdot (N^2-1)$, depending only on $d$ and the adjoint dimension. **Verdict: K-uniform.**

### 2.4 $r_{\mathrm{proj}}(N)$ — block-spin projection radius

From `K-balaban-general-groups.md` K.3 line 161: $r_{\mathrm{proj}}(N) \geq 1/2$, a purely linear-algebraic bound on the polar decomposition near $\mathbf{1}$. **Verdict: K-uniform**, depending only on $N$.

### 2.5 Precise statement for Step 1.2

Combining 2.1–2.4:
$$\rho(K) \;\geq\; \rho_* \;=\; \min\!\left(\frac{\kappa_*}{8},\; \frac{\mu_W}{8(N^2-1)},\; \tfrac{1}{2}\right) > 0,$$
depending only on $N$, $\mu_W$, and $d = 4$, with *no* explicit dependence on the outer index $K$. **$\rho(K) \geq \rho_* > 0$ uniformly in $K$.**

This verdict is *conditional* on the interpretation that $m_W a_k$-fixed in Balaban CMP 95/96/109/119 is the inner-$k$ convention (confirmed at the level of the preprint's secondary text but requiring explicit verification against the primary source — see §5 below).

---

## Section 3 — Verification table

Legend: K-uniform ✓ (yes), ✗ (no), ? (unclear without further reading).

| # | Constant | Defined in (paper/eqn) | $K$-dep. (physical units) | K-unif.? | Notes |
|:--|:---------|:----------------------|:--------------------------|:--------:|:------|
| 1 | $C_0$ (bond constant) | Preprint §4.3 Thm 2; `04-lattice-proof-part1.md` lines 556–563 | Monotone in $a_0(K)/r_3$; bounded above by $C_0^* = C_0(a^*/r_3, N)$ in strong-coupling regime | ✓ | Only in the regime $K \leq K_{\max}(a^*/r_3)$ |
| 2 | $m_1$ (lightest KK mass) | Preprint §4.3 Thm 2, Appendix E (Weitzenböck) | $m_1 = 2\sqrt{N}/r_3$, depends only on $N, r_3$ | ✓ | Physical mass, $K$-independent |
| 3 | $\beta_{\max}(a_0(K))$ | Preprint §4.3 Thm 3; `04-lattice-proof-part1.md` line 747 | $\sim m_1 a_0(K)/6 \sim 2^{-K}$; shrinks geometrically | ✗ | Narrows as $K\to\infty$; CE regime of validity is $K \leq K_{\max}$ |
| 4 | $\alpha$ (KP weight, dim.less) | Preprint §4.3 Thm 3 proof | $O(1)$, chosen once | ✓ | Pure number |
| 5 | $\alpha/a_0(K)$ (cluster rate, physical units) | Preprint §4.4 Thm 4(c) | $(\alpha/a^*)\cdot 2^K$, grows | ✓ (trivially from below) | Is *above* any physical scale, favourable |
| 6 | $K_{\mathrm{meas}}$ (measure factor) | Preprint §4.3 Thm 3 | $N$-dep. only; $K$-independent | ✓ | From Haar + Gaussian on internal fields |
| 7 | $c_d$ (lattice animal constant, $d=4$) | Preprint §4.3 Thm 3 proof | Pure combinatorial number | ✓ | Dimension-only |
| 8 | $\kappa$ (polymer decay, Balaban) | CMP 109 Thm 1/3; `05-continuum-limit.md` I.2 line 1445 | Depends on $d, N, \mu_W$; $K$-independent | ✓ | Conditional on $m_W a_k$-fixed convention (§2.1) |
| 9 | $m_W a_k^{(K)}$ (fluct. mass × inner scale) | Balaban CMP 95 Prop 1.2; `05-continuum-limit.md` line 1489 | $\mu_W \cdot 2^k$; $K$-indep. at each inner $k$ | ✓ | The key inner-$k$ identity |
| 10 | $C_D$ (Lipschitz const of $D^2[V]$) | `K-balaban-general-groups.md` K.2(b) line 106 | $\leq 2 d (N^2-1)$; $K$-independent | ✓ | Group- and dim-only |
| 11 | $r_{\mathrm{proj}}(N)$ | CMP 98 §E; `K-balaban-general-groups.md` K.3 | $\geq 1/2$; $N$-dep., $K$-indep. | ✓ | Polar decomposition radius |
| 12 | $\rho = \min(\kappa/2d, m_W a/(2C_D), r_{\mathrm{proj}})$ | `05-continuum-limit.md` eq. (I.3) line 1502 | Combination of 8–11 above | ✓ | Conditional on 8–9 |
| 13 | $\|E_k\| \leq C g_k^4$ operator norm $C$ | `05-continuum-limit.md` line 103; `I3-N-dependence-tracking.md` item 11 | Polynomial in $N$, $K$-indep. | ✓ | From polymer sum with $K$-unif. constants |
| 14 | $C_{\mathrm{new}}(K)$ (from §5.6 III.5) | `05-continuum-limit.md` eq. (III.2) line 1740 | Product $C_2(N) \cdot C(N)$ — factors $K$-indep. *except* spectral lemma $C_p$ | ? | Depends on $C_p$; deferred to Tier 1 Step 1.3 |

---

## Section 4 — Open issues

### 4.1 Narrowing cluster-expansion window $\beta_{\max}(K) \to 0$

Not a failure of $K$-uniformity but a regime-of-validity restriction: the bare CE converges at $a_0(K)$ only for $K \leq K_{\max}(a^*/r_3)$. **Needed:** the Tier 1 Step 1.5 / C3 handoff lemma, which derives the starting condition at large $K$ from Balaban's inner RG evaluated at the coarse inner slice $k = K$ (where $a_K^{(K)} = a^*$ coincides with the reference scale). **Alternative:** declare Section 4's bare CE applicable only at $K = 0$, and inherit all $C_K$ ($K \geq 1$) from the recursion without re-establishing the starting condition at each $K$.

### 4.2 The fluctuation-mass convention under K/k separation

§2's verdict is conditional on $m_W(K) a_0(K) = \mu_W$ fixed. The preprint's "$m_W a_k$ held fixed" is single-indexed and must be re-parsed. **Needed:**
1. Explicit verification against Balaban CMP 95 §3, CMP 96 §2, CMP 109 §3 that $m_W$ is a regulator parameter chosen at the start of each bare theory (outer $K$), not a physical mass.
2. Ruling out any hidden $a_0$-dependence in $\kappa$ beyond $m_W a_k$.
3. A one-sentence clarification in the §5.1 preamble: "*$m_W$ is a regulator mass chosen with $m_W(K)\cdot a_0(K) = \mu_W$ fixed.*"

### 4.3 Operator-norm bound $C$ in $\|E_k\| \leq C g_k^4$

`I3-N-dependence-tracking.md` item 11 asserts $C$ is polynomial in $N$ and $K$-independent via the operator-extraction lemma. Under K/k separation, $C$ inherits $K$-uniformity from $\kappa$ and $\rho$ (both verified in §2). **Needed:** a single-sentence cross-reference in §5.1.3 making this inheritance explicit.

### 4.4 The spectral-lemma constant $C_p$

**Deferred** per task instructions. Tier 1 Step 1.3 (Combes-Thomas / Lieb-Robinson reformulation).

---

## Section 5 — Recommended next steps for the authors

1. **Verify the $m_W a_k$-fixed convention in Balaban CMP 95/96/109.** Read CMP 109 §3 (inductive hypotheses) and CMP 95 Proposition 1.2 with the goal of confirming that $m_W$ is a dimensionless regulator indexed by the bare scale $a_0$ (our $K$) and that all bounds are expressed in terms of dimensionless products $m_W \cdot a_k$. ~1 week.

2. **Add an explicit "regulator mass" sentence to the §5.1 notation preamble** (after Tier 0 patch 2.1): "*For each bare theory $K$, the fluctuation regulator mass is $m_W(K) = \mu_W/a_0(K)$ for a fixed dimensionless $\mu_W > 0$; hence $m_W(K)\cdot a_k^{(K)} = \mu_W\cdot 2^k$ is $K$-independent at each inner step $k$.*" One sentence, no re-derivation.

3. **Tabulate $\kappa, \delta_0, \rho_{\mathrm{prop}}, r_{\mathrm{proj}}$ as explicit functions of $(\mu_W, N, d)$** with no $K$ or $k$ dependence, in Appendix H, with precise CMP citations.

4. **Add a "regime of validity" remark to §4.4 (Theorem 4).** State that Section 4's cluster expansion converges at bare scale $a_0(K)$ only for $K \leq K_{\max}(a^*/r_3)$; at larger $K$ the starting condition is supplied by Balaban's inner RG (Tier 1 Step 1.5), not by Section 4. This resolves the tension between "K-uniform CE starting condition" and "$\beta_{\max}(K) \sim 2^{-K}$".

5. **Cite CMP 109 p. 251 and Dimock arXiv:1108.1335 p. 2 at the point of the $m_W a_k$-fixed convention**, not only at the notation preamble.

6. **Defer $C_p$ to Tier 1 Step 1.3** and add a forward-reference in §5.5.3 flagging the Lieb-Robinson / Combes-Thomas reformulation in physical units.

---

## Conclusion of the audit

Under the Tier 0 K/k separation and conditional on the $m_W(K)\cdot a_0(K) = \mu_W$ convention (recommendation 2 above):

- **Balaban's analyticity radius $\rho(K) \geq \rho_* > 0$ is K-uniform** (§2.5). All four ingredients ($\kappa, m_W a_k, C_D, r_{\mathrm{proj}}$) are $K$-independent or built from ratios whose $K$-dependence cancels by the fixed-regulator convention.

- **The CE starting condition $C_K(k=0)$ is K-uniform only in the strong-coupling regime $K \leq K_{\max}(a^*/r_3)$** (§1.5). At large $K$, $\beta_{\max}(K) \sim 2^{-K}$ closes the convergence window and Section 4 no longer applies directly; the Tier 1 Step 1.5 handoff lemma is the resolution.

- **The one constant not directly K-uniform is $\beta_{\max}(a_0(K))$** (Table row 3), which shrinks like $2^{-K}$. Mitigated by the regime-of-validity restriction (§4.1); not a failure, but a regime restriction the preprint must acknowledge.

- **$C_p$ is explicitly deferred** to Tier 1 Step 1.3.

All other constants in §3 are $K$-uniform directly or conditional on the (recommended) explicit $m_W a_k$-fixed convention. No constant outside the deferred $C_p$ and the regime-restricted $\beta_{\max}$ was found to violate $K$-uniformity.

— End of Tier 1 / Steps 1.1 + 1.2 bookkeeping.
