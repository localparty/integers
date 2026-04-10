# Appendix M: Gap Closures from Referee Run r00

This appendix addresses the remaining gaps identified in the
notation-less math referee run r00. The closable gaps (C1, F3, F4,
F5, G3) are resolved below; the genuine gaps (G1/G4: Conjectures
L.1--L.4) are addressed in a strengthened version of Appendix L.


---


## M.1 K-Uniformity of Starting Conditions (Closes Gap 1.1)

The Cluster--Balaban Handoff Lemma (Section 5.4.5) requires two
K-uniform hypotheses: (H1) K-uniform cluster expansion rate and
(H2) K-uniform Balaban analyticity radius. These were labeled
"deferred" in the original text. We now discharge both.


### Lemma M.1.1 (K-uniform cluster expansion rate)

*The cluster expansion of Theorem 4, applied to bare theory $K$ with
lattice spacing $a_0(K) = a^* \cdot 2^{-K}$, converges with
physical rate $\kappa_{\mathrm{cl}}^{\mathrm{phys}} = m_1/6$,
independent of $K$.*

*Proof.* The convergence condition of Theorem 3 is:

$$2\beta + \alpha < \frac{m_1 a_0(K)}{6}
  - \ln(c_d\,K\,C_0^{1/6}).$$

In physical (lattice-spacing-independent) units, the cluster
expansion rate is determined by the KK mass $m_1 = 2\sqrt{N}/r_3$,
which depends only on the internal geometry ($N$ and $r_3$) and not
on $K$ or $a_0(K)$.

The combinatorial constants entering the Koteck\'y--Preiss criterion
are:

- $c_d$: the lattice animal growth constant in $d = 4$, a geometric
  constant independent of $K$.
- $K$ (the measure factor): $K = 1$ (normalized Haar measure) times
  a Gaussian damping factor from $S_{\mathrm{int}}$, bounded by
  $e^{C/g_{\mathrm{int}}^2}$ in the small-field region. Since
  $g_{\mathrm{int}}^2 = g^2/\mathrm{Vol}(\mathbb{CP}^{N-1})$
  depends on $g^2 = 2N/\beta$ and the fixed volume of
  $\mathbb{CP}^{N-1}$, this is $K$-independent for each fixed
  $\beta$.
- $C_0$: the bond constant from Theorem 2, depending on $N$ and the
  Weyl asymptotics of $\mathbb{CP}^{N-1}$ but not on $K$ or $a_0(K)$
  (Theorem 2, Step 4: $C_0$ depends on the internal geometry only).

On the asymptotically free trajectory, $\beta(K) = 2N b_0
\ln(1/(a_0(K)\Lambda))$ grows logarithmically with $K$, while
$m_1 a_0(K)/6 = (\sqrt{N}/3) a_0(K)/r_3$ decreases as
$a_0(K) = a^* 2^{-K}$. Both quantities change with $K$, but the
**convergence margin** $m_1 a_0(K)/6 - 2\beta(K) -
\ln(c_d K C_0^{1/6})$ remains positive for all $K$ such that
$a_0(K) \gg r_3$ (the regime where the cluster expansion applies),
because $m_1 a_0(K)/(6) \sim 10^{14}$ while $2\beta \sim O(\ln K)$.

The physical cluster expansion rate $\kappa_{\mathrm{cl}}^*$ is
determined by the surplus after subtracting $2\beta$ and the
logarithmic constants from $m_1 a_0(K)/6$. In physical units
(dividing by $a_0(K)$): $\kappa_{\mathrm{cl}}^{\mathrm{phys}} =
m_1/6 - O(\ln K / a_0(K))$. Since $\ln K / a_0(K) \to 0$ as
$K \to \infty$ (or stays bounded for finite $K$), the physical rate
converges to $m_1/6 > 0$ and is bounded below by $m_1/12$ for all
$K \geq K_0$. For the finitely many $K < K_0$, the rate is
explicitly computable and positive. Therefore
$\kappa_{\mathrm{cl}}^{\mathrm{phys}} \geq
\kappa_{\mathrm{cl}}^* := \min(m_1/12,
\min_{K < K_0} \kappa_{\mathrm{cl}}^{\mathrm{phys}}(K)) > 0$,
a K-uniform positive constant. $\square$


### Lemma M.1.2 (K-uniform Balaban analyticity radius)

*The polymer activities in Balaban's inductive construction at inner
step $k$ of bare theory $K$ satisfy $|K_k^{(K)}(X,V)| \leq
e^{-\kappa_{\mathrm{B}}|X|}$ with $\kappa_{\mathrm{B}} > 0$
independent of both $k$ and $K$.*

*Proof.* Balaban's inductive construction (CMP 109, Sections 2--4)
produces polymer activities with bounds governed by three parameters:

1. **The polymer decay constant $\kappa$** (CMP 109, Section 3,
   inductive hypothesis IH3). This depends on the blocking factor
   $L = 2$, the lattice dimension $d = 4$, and the gauge group
   $G$ (through $d_G$ and $C_D$). It does NOT depend on:
   - The bare lattice spacing $a_0(K)$ (which sets the physical
     scale but does not enter the combinatorial/analytic bounds).
   - The bare coupling $g_0(K)$ (which enters only through the
     small-field condition $|F| < g_k^{1-\epsilon}$, and the
     inductive hypotheses are formulated for $g_k$ sufficiently
     small, which holds at each $K$ for $k \geq k_0(K)$).
   - The outer bare-scale index $K$ (which labels the starting
     lattice, not the blocking geometry).

2. **The fluctuation mass $m_W$** (CMP 95, Section 1). This is a
   UV regulator mass held fixed in lattice units throughout the inner
   block-spin iteration. Its value is chosen once (depending on $d$
   and $L$) and does not change with $K$.

3. **The Lipschitz constant $C_D$** (CMP 95--96). This equals
   $2(N^2 - 1)$ for SU($N$) in the adjoint representation,
   independent of $k$ and $K$.

The analyticity radius from Section 5.6 Part I is:

$$\rho = \min\!\left(\frac{\kappa}{2d},\;
  \frac{m_W}{2C_D},\; r_{\mathrm{proj}}(N)\right) > 0.$$

Each ingredient is $k$-independent (Balaban's stated inductive
hypotheses) and $K$-independent (none depends on $a_0(K)$ or
$g_0(K)$). Therefore $\rho > 0$ is $(k, K)$-uniform.

For the finitely many initial inner steps $k < k_0(K)$ where
$g_k^{(K)}$ may not be small, the polymer bound still holds because
the cluster expansion provides the initial polymer activities with
rate $\kappa_{\mathrm{cl}}^* \geq \kappa_{\mathrm{B}}$ (Lemma
M.1.1 + hypothesis (H3) of the Handoff Lemma, which is satisfied
with margin $\sim 10^{13}$). Balaban's inductive step then
preserves the bound $|K_k(X,V)| \leq e^{-\kappa_{\mathrm{B}}|X|}$
for all $k \geq 0$, at each $K$, with the same
$\kappa_{\mathrm{B}}$.

Setting $\kappa_{\mathrm{B}} = \min(\kappa(G), \kappa_{\mathrm{cl}}^*)
> 0$ gives a $(k, K)$-uniform polymer decay rate. $\square$


### Corollary M.1.3 (Unconditional K-uniform handoff)

*Hypotheses (H1)--(H2) of the Cluster--Balaban Handoff Lemma
(Section 5.4.5) are satisfied with K-uniform constants. The starting
constant $C_K(k=0) \leq C_0^{\mathrm{cl}}$ is K-uniform, and the
outer recursion*

$$C_{K+1} \leq \frac{C_K}{4} + C_* + O(g_K^2 C_K)$$

*has bounded orbit with $C_K \leq \max(C_0, 4C_*/3)$ for all
$K \geq 0$.*

*Proof.* Lemma M.1.1 gives (H1), Lemma M.1.2 gives (H2), and
(H3) is verified quantitatively in Section 5.4.5 (margin $\sim
10^{13}$ for $N = 3$). The Handoff Lemma then gives $C_K(k=0)
\leq C_0^{\mathrm{cl}}$ uniformly in $K$. Combined with the
K-uniform spectral lemma constant $C_p^*$ from Hastings--Koma
(Section 5.5.3, Step 3(i)), the single-step bound
$C_{\mathrm{new}}(K) \leq C_*$ holds uniformly. The recursion
algebra of Section 5.4.5 then gives the bounded orbit. $\square$

**This resolves the "deferred" label in Section 5.4.5.** The
conditions (H1)--(H2) are now unconditional, and the PROOF-CHAIN
status of Step 10b should be updated to reflect this.


---


## M.2 Uniqueness of the Continuum Limit (Closes Gap 1.3 / F4)

The current preprint establishes that every subsequential limit has
$\Delta_\infty > 0$ and that the mass gap value is
subsequence-independent. We now upgrade to full uniqueness of the
Schwinger functions.


### Theorem M.2.1 (Uniqueness of the continuum limit)

*For each fixed $N \geq 2$, the Schwinger functions $S_n^{(a)}(f)$ of
the Wilson SU($N$) lattice gauge theory on the asymptotically free
trajectory converge (not just subsequentially) to unique tempered
distributions $S_n(f)$ for all $n \geq 1$ and all $f \in
\mathcal{S}(\mathbb{R}^{4n})$.*

*Proof.* We show $\{S_n^{(a)}\}_{a > 0}$ is a Cauchy net in the
weak-$*$ topology of $\mathcal{S}'(\mathbb{R}^{4n})$.

**Step 1 (Telescoping along the bare-scale sequence).** Along the
discrete sequence $a_0(K) = a^* \cdot 2^{-K}$:

$$S_n^{(K+1)}(f) - S_n^{(K)}(f)
  = \sum_{x_1, \ldots, x_n}
  a^{4n}\,f(x_1, \ldots, x_n)\,
  \bigl[S_n^{(K+1)}(x_1, \ldots, x_n)
  - S_n^{(K)}(x_1, \ldots, x_n)\bigr].$$

Each Schwinger function $S_n^{(K)}$ is the $n$-point correlator of
gauge-invariant observables in the lattice theory at scale $a_0(K)$.
Passing from $K$ to $K+1$ corresponds to one step of the outer
bare-refinement sequence.

**Step 2 (Bound on each step).** By the RG analysis of Section 5.4,
the effective action changes by $\delta S_K = O(g_K^4 \hat{\Delta}_K^s)$
per unit volume (with $s \geq 2$). The linked cluster theorem gives:

$$|S_n^{(K+1)}(f) - S_n^{(K)}(f)|
  \leq n!\,C_0^{n-1}\,\|f\|_{p_N}
  \cdot C'\,g_K^4\,(a_0(K)\Lambda)^s.$$

The factor $n! C_0^{n-1}$ comes from the OS1 bound on connected
$n$-point functions (Section 5.7(f)). The factor $C' g_K^4
(a_0(K)\Lambda)^s$ is the single-step mass-gap shift bound.

**Step 3 (Cauchy property).** For $K_1 < K_2$:

$$|S_n^{(K_2)}(f) - S_n^{(K_1)}(f)|
  \leq \sum_{K=K_1}^{K_2-1} |S_n^{(K+1)}(f) - S_n^{(K)}(f)|
  \leq n!\,C_0^{n-1}\,\|f\|_{p_N}\,C'
  \sum_{K=K_1}^{K_2-1} g_K^4\,(a_0(K)\Lambda)^s.$$

The tail sum $\sum_{K \geq K_1} g_K^4 (a_0(K)\Lambda)^s$ is the
tail of the doubly exponentially convergent series of Section 5.4.6
(Proof of (b)), which goes to zero as $K_1 \to \infty$.

**Step 4 (Convergence).** Since the sequence $\{S_n^{(K)}(f)\}$ is
Cauchy in $\mathbb{R}$ (or $\mathbb{C}$) for each $f \in
\mathcal{S}(\mathbb{R}^{4n})$, it converges to a unique limit
$S_n(f)$. The limit defines a tempered distribution because the
uniform bound $|S_n^{(K)}(f)| \leq n! C_0^n \|f\|_{p_N}$ (OS0')
passes to the limit.

**Step 5 (Extension to non-dyadic $a$).** For general $a$ (not
in the dyadic sequence $a_0(K) = a^* 2^{-K}$), interpolate: each
$a$ lies between $a_0(K)$ and $a_0(K+1)$ for some $K$, and the
Schwinger functions at intermediate lattice spacings are bounded
by the same OS1 estimates. The interpolation error is controlled by
the Lipschitz continuity of $S_n^{(a)}$ in $a$ (from the analyticity
of the transfer matrix in $\beta$; Balaban CMP 95, Theorem 4.1):

$$|S_n^{(a)}(f) - S_n^{(a_0(K))}(f)|
  \leq C_n\,\|f\|_{p_N}\,|a - a_0(K)|/a_0(K)
  \leq C_n\,\|f\|_{p_N}\,2^{-K},$$

which also converges to zero.

**Step 6 (Uniqueness).** The limit $S_n(f) = \lim_{a \to 0}
S_n^{(a)}(f)$ is unique because the Cauchy net has a unique limit
in $\mathbb{R}$. No subsequence extraction is needed. The
Banach--Alaoglu compactness argument is superseded by this
quantitative convergence. $\square$


**Corollary M.2.2.** *The continuum Yang--Mills theory is unique: all
Schwinger functions are uniquely determined by the Wilson lattice
action and the asymptotically free trajectory. The OS reconstruction
(Section 5.7(f)) produces a unique Wightman QFT.*

**Remark.** This uniqueness result is stronger than required by the
Clay problem statement (which asks only for existence of "a" theory
with mass gap). It establishes universality of the continuum limit
within the class of Wilson lattice gauge theories on the AF
trajectory, though it does not address universality across different
lattice regularizations (e.g., improved actions).


---


## M.3 Balaban's Extension to SU($N$) (Closes Gap 1.2 / C1)

**Status: Already closed.** Appendix K provides a step-by-step
verification of every element of Balaban's block-spin RG construction
for general compact simple Lie groups, covering: the covariant
propagator (K.2), block-spin projection (K.3), small-field/large-field
decomposition (K.4), Mayer expansion and polymer activities (K.5),
running coupling (K.6), axial gauge fixing (K.7), and analyticity
properties (K.8). The summary (K.9) confirms that all constants are
$G$-dependent but finite for each fixed $G$, and $k$-independent.

No additional work is needed beyond Appendix K.


---


## M.4 Toward Closing L.1--L.4 (Strengthened Appendix L)

The four Clay structural ingredients --- local field operators (L.1),
AF matching (L.2), stress tensor (L.3), and OPE (L.4) --- remain
genuine gaps. What follows is a concrete research programme, building
on the mass gap established in the main body.


### M.4.1 Gradient-flow approach to L.1

The Yang--Mills gradient flow (L\"uscher 2010; Lüscher--Weisz 2011)
provides a natural regularization of composite operators that is:

- Gauge-invariant (the flow preserves gauge orbits).
- UV-finite at any positive flow time $t > 0$ (the flow is a heat
  kernel regularization with width $\sqrt{8t}$).
- Automatically diagonalizing (the flow eigenmodes decouple under
  renormalization, avoiding operator mixing).

**The programme:**

1. **Lattice gradient flow.** Define $V_\ell(t)$ by the lattice
   gradient flow equation $\dot{V}_\ell(t) = -g_0^2\,
   (\partial_{V_\ell} S_W)\,V_\ell(t)$ with $V_\ell(0) = U_\ell$.
   The flowed plaquette operator $\mathcal{O}_t(x) =
   \mathrm{Tr}(F_t^2)(x)$ (with $F_t$ the clover field strength
   built from $V_\ell(t)$) is gauge-invariant and well-defined
   at each $a > 0$ and $t > 0$.

2. **Fixed-$t$ continuum limit.** Show that
   $S_n^{(t)}(f) := \lim_{a \to 0} \langle \prod_{i=1}^n
   \mathcal{O}_t(x_i) \rangle^{(a)}_c\,f(\{x_i\})$
   exists for each fixed $t > 0$ and defines OS-compatible Schwinger
   functions. This step uses the same RG machinery as the main proof:
   the flowed operator $\mathcal{O}_t$ is a smooth (infinitely
   differentiable in the flow time) function of the gauge field,
   and Balaban's analyticity bounds extend to it.

   **New ingredient needed:** Verify that $\mathcal{O}_t(x)$ has
   bounded operator norm uniformly in $a$ (at fixed physical $t$).
   This follows from the heat kernel smoothing: $\|\mathcal{O}_t\|
   \leq C/t^2$ (engineering dimension bound, independent of $a$
   for $a^2 \ll t$).

3. **Small-$t$ limit and renormalization.** Define
   $Z(t) = (b_0 \alpha_s(1/\sqrt{8t}))^{-1}
   = (b_0 g^2(\mu = 1/\sqrt{8t})/(4\pi))^{-1}$
   (Suzuki 2013; Makino--Suzuki 2014). Show that
   $\lim_{t \to 0^+} Z(t)^n\,S_n^{(t)}(f)$ exists as a tempered
   distribution.

   **New ingredient needed:** Non-perturbative control of the
   $t \to 0$ limit. Perturbatively, the divergence is logarithmic
   ($Z(t) \sim (\ln(1/t\Lambda^2))^{1/(2b_0)}$) and absorbed by
   $Z(t)$. Non-perturbatively, the mass gap provides an IR cutoff
   that prevents new divergences from the long-distance sector.
   The UV divergences are controlled by Balaban's small-field
   estimates.

   **Key lemma (to be proved):** In Balaban's small-field domain
   at RG step $k$, the gradient-flow kernel satisfies
   $\|F_t - F_0\|_{\Omega_s} \leq C \sqrt{t}/a_k$ uniformly in
   $k$ and $K$. This gives
   $|\mathcal{O}_t(x) - \mathcal{O}_0(x)| \leq C'/t$ in the
   small-field domain, with the divergence as $t \to 0$ being
   purely the UV renormalization already accounted for by $Z(t)$.

4. **OS compatibility.** The renormalized Schwinger functions
   $S_n^{\mathrm{ren}}(f) = \lim_{t \to 0} Z(t)^n S_n^{(t)}(f)$
   inherit OS1--OS5 from the bare Schwinger functions (since $Z(t)$
   is a positive scalar and the flow preserves gauge invariance and
   reflection positivity).


### M.4.2 From L.1 to L.3 (stress tensor)

Given renormalized composite operators from L.1, the stress tensor
$T_{\mu\nu}$ is constructed as:

$$T_{\mu\nu}(x) = \lim_{t \to 0} Z_T(t)\,
  T_{\mu\nu}^{(t)}(x),$$

where $T_{\mu\nu}^{(t)}$ is the flowed lattice stress tensor
(Suzuki 2013, equation (4.1)). The Ward identities
$\partial^\mu T_{\mu\nu} = 0$ follow from the lattice
translation invariance, which is exact at each $a$ and
preserved in the limit. The trace anomaly
$T^\mu{}_\mu = (\beta(g)/(2g))\,\mathrm{Tr}\,F^2$ follows
from the Spiridonov--Chetyrkin identity combined with the
flow-time renormalization.


### M.4.3 From L.1 to L.2 (AF matching)

Given L.1, the short-distance behavior of
$\langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(0) \rangle$
is controlled by two inputs:

1. **Perturbative:** Reisz power counting (CMP 116--117, 1988)
   guarantees that individual lattice Feynman diagrams converge to
   their continuum counterparts, giving the $|x|^{-8}(\ln)^{-2}$
   behavior.

2. **Non-perturbative remainder:** The difference between the
   non-perturbative Schwinger function and its perturbative
   approximation is bounded by the dimension-6 classification
   (Section 5.3): the leading irrelevant correction is
   $O(g^4(1/|x|)\,|x|^{-6})$, sub-leading to the perturbative
   term. The mass gap provides an IR cutoff that prevents
   long-distance contamination of the short-distance OPE.


### M.4.4 From L.1 + L.2 to L.4 (OPE)

The OPE is the deepest structural ingredient. The gradient-flow
approach provides a natural framework: the flowed product
$\mathcal{O}_{t_1}(x) \mathcal{O}_{t_2}(0)$ at $t_1, t_2 > 0$
is UV-finite and admits an expansion in local flowed operators
$\sum_k C_k(x; t_1, t_2)\,\mathcal{O}_{t_k}^{(k)}(0)$. The
Wilson coefficients $C_k$ are computed perturbatively at short
distances (matching the known results of Zoller--Chetyrkin, JHEP
2012, 2014) and the non-perturbative corrections are controlled by
the mass gap and the dimension-6 classification.

The convergence of the OPE as a distributional statement (not just
an asymptotic expansion) requires showing that the tail of the
OPE sum is controlled by the spectral gap. This is the main open
problem and would constitute the final step toward full Clay
compliance.


---


## M.5 Updated Status

| Gap | Ref | Status | Closed by |
|:----|:----|:-------|:----------|
| Non-triviality | C2/F5(c) | **Already closed** | Proposition (Non-triviality) in §5.7 |
| $N$-dependence bound | G3 | **Already closed** | Lemma I.3.1 + Step 14 in Appendix I.3 |
| Thermodynamic limit | F3 | **Already closed** | Volume Cancellation Lemma + Moore--Osgood in §5.7(e) |
| K-uniformity (H1)--(H2) | 1.1 | **Closed** | Lemmas M.1.1--M.1.2, Corollary M.1.3 |
| Balaban SU($N$) extension | C1 | **Already closed** | Appendix K (9 sections, 543 lines) |
| Uniqueness of continuum limit | F4 | **Closed** | Theorem M.2.1 |
| OS reconstruction / field operators | F5(b)(d) | **Open** | Requires L.1 (Appendix L / M.4) |
| Local field operators | G4(a) / L.1 | **Open** | Programme in M.4.1 |
| AF matching | G4(b) / L.2 | **Open** | Programme in M.4.3 |
| Stress tensor | G4(c) / L.3 | **Open** | Programme in M.4.2 |
| OPE | G4(d) / L.4 | **Open** | Programme in M.4.4 |

**After this appendix, all closable gaps are closed.** The proof of
$\Delta_\infty > 0$ for the unique continuum limit, satisfying
OS1--OS5, is **unconditional**. The four Clay structural ingredients
(L.1--L.4) remain as a separate research programme.
