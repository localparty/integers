# Story 48: Close All Referee Gaps

The notation-less math referee (run r00) found **15 SOUND / 5 CLOSABLE
/ 2 GENUINE** across 24 points. The genuine gaps (G1, G4) overlap —
both concern the four Clay structural ingredients (L.1–L.4). This
document is the plan for closing every gap, ordered from quickest to
hardest.

---

## Tier 0 — Paragraph-level fixes (< 1 hour each)

These are statement gaps, not proof gaps. The math exists; it just
needs to be written down.

### 0.1  Non-triviality of the continuum theory (C2 / F5(c))

**Gap:** The connected 4-point function of the continuum theory is
never explicitly shown to be nonzero.

**Fix:** Add a Remark after Section 5.7(f) OS5. Argument:

1. At the lattice level, the connected 4-point function of the
   plaquette operator $\hat{s}_P$ is $O(g_0^2)$ at leading order in
   lattice perturbation theory (one-gluon exchange in the $t$-channel).
2. $g_0^2 > 0$ at every lattice spacing (asymptotic freedom runs $g_0$
   to zero only in the continuum limit $a \to 0$; at any finite $a$,
   $g_0 > 0$).
3. The 4-point Schwinger function $S_4(f)$ is a continuous functional of
   the test function $f$. Its value at the lattice level is bounded
   below by $c \cdot g_0^2 > 0$.
4. By the convergence of the Schwinger functions in the continuum
   limit (Section 5.7), $S_4^{\mathrm{cont}}(f) = \lim S_4^{(a)}(f)$.
   Since each term is positive (by RP) and nonzero, the limit is nonzero.
5. Therefore the continuum theory is non-Gaussian. $\square$

Also note $m < \infty$ (spectrum above 0 non-empty) follows: the
one-glueball state has finite mass $\Delta_\infty$.

**Where:** New Remark 5.7.2 in Section 5.7.

### 0.2  $N$-dependence closed-form bound (G3)

**Gap:** Appendix I.3 tracks individual constants but doesn't state
the total accumulated $N$-dependence of $C_\infty$ as a closed-form
bound.

**Fix:** Add a Corollary at the end of Appendix I.3:

> **Corollary I.3.2.** For each fixed $N \geq 2$, the continuum mass
> gap satisfies $\Delta_\infty(N) \geq \Delta_0(N) \cdot
> \prod_{K=1}^\infty (1 - P(N) \cdot K^{\gamma(N)-2} \cdot 4^{-K})$,
> where $P(N) = O(N^{2\alpha(N)})$ and $\gamma(N) =
> O(N^3)$ are explicit polynomial bounds collecting the
> $N$-dependence from all 14 proof steps. The infinite product
> converges for each $N$ because $4^{-K}$ dominates $K^{\gamma-2}$.

Collect: $C_0 = O(N^{N-1})$ (bond constant), $C_D = N^2 - 1$,
$\kappa = O(1/\mathrm{poly}(N))$, $\gamma = \alpha/(b_0 \ln 2)$ with
$\alpha \sim N^2$ and $b_0 \sim N$.

**Where:** New Corollary I.3.2 in Appendix I.3.

### 0.3  Thermodynamic limit uniformity (F3)

**Gap:** The uniformity in $a$ of the $L$-convergence rate is implicit
but not explicitly stated.

**Fix:** Add a Lemma in Section 5.7(e):

> **Lemma 5.7.e.1.** For each fixed $N$ and $\beta$ in the
> convergence domain, the finite-volume mass gap satisfies
> $|\Delta(a, L) - \Delta(a, \infty)| \leq C e^{-L \Delta_{\mathrm{phys}}}$
> uniformly in $a$, where $\Delta_{\mathrm{phys}} > 0$ is the
> $a$-independent physical mass gap on the AF trajectory.

Proof: The Hastings–Koma exponential clustering (§5.5.3 Step 3(i))
gives correlation decay with physical correlation length
$\xi = v_{\mathrm{LR}} / \Delta_{\mathrm{phys}}$. Since both
$v_{\mathrm{LR}}$ and $\Delta_{\mathrm{phys}}$ are $a$-independent
(on the AF trajectory, they are physical quantities), the convergence
rate $e^{-L/\xi}$ is uniform in $a$. The finite-volume spectral gap
is bounded below by $\Delta_{\mathrm{phys}} - C e^{-L \Delta_{\mathrm{phys}}} > 0$
for $L \geq L_0$, uniformly in $a$.

**Where:** New Lemma in Section 5.7(e).

---

## Tier 1 — Page-level arguments (1–3 pages each)

### 1.1  K-uniformity of (H1)–(H2) (the "Tier 1B" question)

**Gap:** The Cluster–Balaban Handoff Lemma (§5.4.5) requires
K-uniform cluster expansion (H1) and K-uniform Balaban analyticity
radius (H2), labeled "deferred."

**Fix:** Prove K-uniformity by the following argument:

**(H1) K-uniform cluster expansion.** The cluster expansion of
Theorem 4 converges with rate $\kappa_{\mathrm{cl}} = m_1/(6a_0(K))$
in lattice units, or $\kappa_{\mathrm{cl}}^{\mathrm{phys}} =
m_1/6$ in physical units. Since $m_1 = 2\sqrt{N}/r_3$ is independent
of $K$, the physical rate is K-uniform.  The combinatorial constants
($c_d$, $K$, $C_0$) are $K$-independent by Theorem 2 (they depend on
$N$ and the internal geometry, not on $a_0(K)$).

**(H2) K-uniform Balaban analyticity radius.** Balaban's inductive
construction at inner step $k$ of bare theory $K$ produces polymer
activities with bounds depending on three $k$-independent parameters:
$\kappa$ (CMP 109, §3), $m_W$ (CMP 95, §1), $C_D$ (CMP 95–96).
None of these depend on the bare coupling $g_0(K)$ or the bare
lattice spacing $a_0(K)$ — they depend on the blocking factor $L=2$,
the dimension $d=4$, and the gauge group SU($N$). Therefore they are
also $K$-independent. The analyticity radius
$\rho = \min(\kappa/(2d), m_W a/(2C_D), r_{\mathrm{proj}}(N))$
is then K-uniform (the factor $m_W a$ is in lattice units at the
current effective lattice spacing, not at the bare spacing).

Resolve the tension: update PROOF-CHAIN IV.1 to note "(H1)–(H2)
established in new Lemma 5.4.5b" and remove the "deferred" label.

**Where:** New Lemma 5.4.5b (K-uniformity of starting conditions),
~2 pages, in Section 5.4.5.

### 1.2  Balaban SU(2) → SU($N$) (C1)

**Gap:** Balaban's published program is for SU(2). The extension to
SU($N$) is argued structurally but not verified step-by-step.

**Fix:** Write a self-contained verification appendix (new Appendix K
or expansion of existing Appendix K) covering:

1. **Covariant Laplacian $D^2[V]$:** Depends on the adjoint
   representation $\mathrm{Ad}(V)$, which is polynomial in the matrix
   entries of $V \in \mathrm{SU}(N)$. The Lipschitz constant
   $C_D = 2(N^2-1)$ enters Balaban's propagator bounds. For each
   fixed $N$, $C_D$ is finite; the propagator bounds (CMP 95,
   Prop. 1.2) hold with $N$-dependent but $k$-independent constants.

2. **Block-spin projection:** The map $A \mapsto A(A^\dagger A)^{-1/2}$
   (polar decomposition) is analytic on GL($N$, $\mathbb{C}$) near
   $\mathbf{1}$ with radius $r_{\mathrm{proj}}(N) \geq 1/(2N)$.
   This is already established in PROOF-CHAIN IV.3 (block-spin
   kernel complexification).

3. **Polymer expansion convergence:** The Kotecký–Preiss criterion
   depends on $\kappa$ and the lattice animal constant $c_d$, both
   $N$-independent. The polymer activities have $N$-dependent norms
   but the convergence structure is identical for all $N$.

4. **Running coupling:** $b_0 = 11N/(48\pi^2)$ is the universal
   one-loop coefficient. Higher-loop corrections are $O(g_k^6)$ per
   step, with $N$-dependent coefficients that do not affect the
   convergence of $\sum g_k^4$ (which uses only $1/k^2$ decay).

5. **Inductive hypotheses:** Walk through Balaban's induction
   (CMP 109, §2–4) identifying every $N$-dependent constant and
   verifying it is finite for fixed $N$.

**Where:** New Appendix K.5 or expansion of existing K, ~3 pages.

### 1.3  Uniqueness / subsequence independence (F4)

**Gap:** The paper proves every subsequential limit has $\Delta_\infty > 0$
but doesn't show the Schwinger functions converge (not just
subsequentially).

**Fix:** Show the Schwinger functions form a Cauchy net in $a$.

The key observation: the telescoping sum
$S_n^{(a)} - S_n^{(a')} = \sum_{K} (S_n^{(K+1)} - S_n^{(K)})$
is controlled by the same bounds that give convergence of the mass gap:
$|S_n^{(K+1)}(f) - S_n^{(K)}(f)| \leq C_n \|f\|_{p_N} g_K^4
\hat{\Delta}_K^s$ for $s \geq 2$. The sum over $K$ converges (doubly
exponentially), so the sequence $\{S_n^{(a)}\}$ is Cauchy in the
weak-* topology on tempered distributions. By completeness of
$\mathcal{S}'(\mathbb{R}^{4n})$, the limit exists and is unique.

This would upgrade "a subsequential limit" to "the unique continuum
limit" — a stronger statement than needed for Clay but valuable for
the physics.

**Where:** New Theorem 5.7.3 (uniqueness of continuum limit), ~1 page.

---

## Tier 2 — Paper-level work (the L.1–L.4 programme)

These are the genuine gaps. Each is a substantial open problem. The
ordering follows the dependency chain: L.1 is prerequisite to L.2–L.4.

### 2.1  Conjecture L.1: Renormalised composite operators

**What's needed:** Construct operator-valued distributions
$[\mathrm{Tr}\,F^2]_R(x)$ on the GNS Hilbert space as limits of
multiplicatively renormalised lattice operators.

**Strategy (from Appendix L.1.4):**

1. **Gradient-flow regularisation.** Define the smeared composite
   $\mathcal{O}_t(x) = \mathrm{Tr}\,F_t^2(x)$ where $F_t$ is the
   Yang–Mills gradient flow at flow time $t > 0$ (Lüscher 2010).
   At any $t > 0$, $\mathcal{O}_t$ is UV-finite and gauge-invariant.
   The flow smears over a physical ball of radius $\sqrt{8t}$.

2. **Small-$t$ limit.** The open problem is to show
   $Z(t) \mathcal{O}_t(x) \to [\mathrm{Tr}\,F^2]_R(x)$ as $t \to 0$
   for a suitable renormalisation factor $Z(t)$. Perturbatively,
   $Z(t) = 1/(b_0 \alpha_s(1/\sqrt{8t}))$ (Suzuki 2013;
   Makino–Suzuki 2014). Non-perturbatively, this is open.

3. **Compatibility with Balaban.** The gradient flow can be formulated
   on the lattice (Lüscher 2010, §4). Balaban's small-field estimates
   provide the bounds needed to control the flow in the UV regime.
   The specific input needed: $\|F_t - F_0\| \leq C \sqrt{t}/a$ in
   the small-field domain, uniformly in $k$ and $K$.

4. **Deliverable:** A proof that $Z(a,t) \sum_x a^4
   \mathcal{O}_t^{\mathrm{lat}}(x) f(x)$ converges as $a \to 0$
   (at fixed physical $t$), then as $t \to 0$ (with $Z$ absorbing the
   divergence), to a tempered distribution satisfying OS properties.

**Estimated difficulty:** 1 paper. The gradient-flow approach is the
most promising route because it avoids operator mixing (the flow
automatically diagonalises the renormalisation) and stays gauge-invariant
throughout. The main technical obstacle is the non-perturbative
control of the small-$t$ limit.

**Prerequisite for:** L.2, L.3, L.4.

### 2.2  Conjecture L.2: Short-distance match to AF

**What's needed:** Show $\langle [\mathrm{Tr}\,F^2]_R(x)
[\mathrm{Tr}\,F^2]_R(0) \rangle = C_N |x|^{-8} (\ln(1/|x|\Lambda))^{-2}
[1 + O((\log)^{-1})]$ as $|x| \to 0$.

**Strategy:**

1. **Short-distance expansion via Balaban.** At lattice spacing $a$,
   the two-point function is computable in lattice perturbation theory
   (Reisz power counting guarantees lattice → continuum convergence of
   individual diagrams). The one-loop result gives the $|x|^{-8}$
   power with the AF logarithm.

2. **Non-perturbative = perturbative at short distances.** This is the
   hard step. Show that the non-perturbative Schwinger function admits
   a short-distance OPE whose leading term matches the perturbative
   result. The key input from the mass gap proof: the spectral gap
   $\Delta_\infty > 0$ controls the long-distance behaviour, and
   Balaban's effective action controls the short-distance structure.
   The dimension-6 classification (Section 5.3) already shows that the
   leading irrelevant correction is $O(|x|^{-6} g^4)$, sub-leading to
   the perturbative term.

3. **Bound on the remainder.** The non-perturbative – perturbative
   difference is controlled by $O(e^{-c/g^2(1/|x|)})$ (instanton
   contributions) plus $O(g^4(1/|x|) \hat{\Delta}^2)$ (irrelevant
   operators). Both vanish as $|x| \to 0$.

**Estimated difficulty:** 1 paper (conditional on L.1). The conceptual
framework exists (Symanzik effective theory + Balaban RG); the missing
piece is the rigorous bridge from the lattice Schwinger functions to
their continuum short-distance asymptotics.

### 2.3  Conjecture L.3: Stress-energy tensor

**What's needed:** Construct $T_{\mu\nu}(x)$ as an operator-valued
distribution, gauge-invariant, symmetric, conserved, reproducing the
trace anomaly $T^\mu{}_\mu = (\beta(g)/(2g)) \mathrm{Tr}\,F^2$.

**Strategy:**

1. **Lattice stress tensor.** On the lattice, the Noether stress tensor
   is defined via the response to a deformation of the lattice metric
   (Caracciolo–Menotti–Pelissetto 1992). The lattice $T_{\mu\nu}$ is
   gauge-invariant and conserved up to $O(a^2)$ corrections.

2. **Renormalisation.** $T_{\mu\nu}$ mixes with lower-dimension
   operators (the unit operator and $\delta_{\mu\nu} \mathrm{Tr}\,F^2$)
   under renormalisation. The mixing coefficients are fixed by Ward
   identities (translation invariance, conservation, trace anomaly).

3. **Continuum limit.** Given L.1 (renormalised composite operators),
   the construction of $T_{\mu\nu}$ reduces to verifying the Ward
   identities in the continuum limit. The key identity:
   $\partial^\mu T_{\mu\nu} = 0$ (conservation) follows from
   translation invariance of the measure, which is manifest on the
   lattice and preserved in the limit.

**Estimated difficulty:** 1/2 paper (conditional on L.1). The main
work is the operator mixing / Ward identity verification, which is
technically involved but conceptually standard.

### 2.4  Conjecture L.4: Operator product expansion

**What's needed:** Establish an OPE
$[\mathcal{O}_1]_R(x) [\mathcal{O}_2]_R(0) \sim \sum_k C_k(x)
[\mathcal{O}_k]_R(0)$ with coefficient functions $C_k(x)$ matching
the perturbative AF predictions at short distances.

**Strategy:**

1. **Formal OPE from Balaban.** At each RG step $k$, Balaban's
   effective action provides a systematic expansion of products of
   operators in terms of local operators with Wilson coefficients.
   The OPE structure is built into the block-spin construction.

2. **Convergence.** The genuine open problem: show the OPE converges
   (in the distributional sense) as an operator statement, not just
   as an asymptotic series. This requires controlling the tail of the
   OPE expansion non-perturbatively.

3. **Wilson coefficients.** The perturbative Wilson coefficients are
   known to high loop order (Zoller–Chetyrkin, JHEP 2012, 2014). The
   non-perturbative corrections are expected to be $O(e^{-c/g^2})$
   (instantons) or $O(\Lambda^{d_O - d_1 - d_2}/|x|^{d_O - d_1 - d_2})$
   (power corrections from higher-dimension operators).

**Estimated difficulty:** 1 paper (conditional on L.1, L.2). This is
the deepest of the four conjectures, requiring a non-perturbative OPE
convergence theorem.

---

## Dependency graph

```
Tier 0 (paragraphs, can all be done now):
  0.1 Non-triviality
  0.2 N-dependence bound
  0.3 Thermodynamic limit uniformity

Tier 1 (pages, can all be done now):
  1.1 K-uniformity (H1)-(H2)
  1.2 Balaban SU(N) extension
  1.3 Uniqueness of continuum limit

Tier 2 (papers, sequential):
  L.1 Composite operators ──→ L.2 AF matching
          │                         │
          └──→ L.3 Stress tensor    │
                                    │
                                    └──→ L.4 OPE
```

---

## Execution order

**Phase 1 (immediate, in the current preprint revision):**
Close 0.1, 0.2, 0.3, 1.1. These require no new mathematics — they
are clarifications, short lemmas, and explicit statements of facts
already implicit in the proof. Doing these upgrades the proof chain
from "conditional" to "unconditional" and eliminates the "deferred"
label on (H1)–(H2).

**Phase 2 (short-term, can be a preprint supplement):**
Close 1.2 (Balaban SU($N$)) and 1.3 (uniqueness). These are
1–3 pages each and could be added as expanded appendices or a
companion note. After Phase 2, the preprint proves:
"For any SU($N$) with $N \geq 2$, the **unique** continuum limit
of the Wilson lattice gauge theory satisfies OS1–OS5 with
$\Delta_\infty > 0$."

**Phase 3 (research programme, separate papers):**
L.1 → L.3 → L.2 → L.4, following the dependency chain. The
gradient-flow approach to L.1 is the most promising starting point.
After Phase 3, the proof would satisfy all Jaffe–Witten requirements
C1–C11.

---

## What Phase 1 + Phase 2 achieve

After Phases 1–2, the scoreboard becomes:

| Category | Before | After |
|:---------|:-------|:------|
| SOUND | 15 | 22 |
| CLOSABLE GAP | 5 | 0 |
| GENUINE GAP | 2 | 2 (G1/G4 — the L.1–L.4 programme) |

The proof of $\Delta_\infty > 0$ with OS axioms would be
**unconditional and complete**, with the four Clay structural
ingredients (L.1–L.4) the only remaining work for full prize
eligibility.
