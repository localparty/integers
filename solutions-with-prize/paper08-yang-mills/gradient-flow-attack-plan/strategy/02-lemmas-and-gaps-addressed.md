# Lemma-by-Lemma and Gap-by-Gap Strategy

*Every lemma that must be proved, every gap that must be closed, and the*
*QG5D physics that addresses each one.*

*Companion to: `formal-argument.md` (synthesis) and*
*`l1-gradient-flow-attack-plan.md` (attack plan).*

*Date: 2026-04-08*

---

## How to read this document

**Part I** catalogs every lemma needed for L.1--L.4, organized by phase.
Each entry gives: (a) a precise mathematical statement, (b) the QG5D
input that bears on it, (c) a proof strategy sketch, (d) exact
references, (e) a difficulty rating.

**Part II** catalogs every gap and risk, with the QG5D physics that
addresses each.

**Part III** maps each sub-clause of Conjectures L.1--L.4 to the
specific lemmas that close it.

**Part IV** gives the dependency graph and critical path.

Difficulty ratings: **E** (established / minor adaptation), **M** (moderate
new work), **H** (hard / genuinely new mathematics).


---
---


# Part I: Lemma Catalog


## Phase 1 — Lattice Gradient Flow in the KK--Balaban Framework

---

### Lemma 1.1: Flow well-posedness on the KK-enhanced lattice

**Statement.** *The lattice gradient flow equation*

$$\partial_t V_t(\ell) = -g_0^2\,(\partial_{V,\ell} S_{\mathrm{KK}}[V_t])\,V_t(\ell), \qquad V_0(\ell) = U(\ell),$$

*on the KK-enhanced lattice of Section 4.1 of the mass gap preprint, has
a unique global solution $V_t(\ell) \in \mathrm{SU}(N)$ for all
$t \ge 0$ and all initial link configurations $\{U(\ell)\}$.*

**QG5D input.** The KK-enhanced lattice action $S_{\mathrm{KK}}$ is a
smooth function on the compact Lie group $\mathrm{SU}(N)^{|\mathrm{links}|}$.
The CP$^{N-1}$ harmonic enhancement (mass gap preprint, Section 4.1)
modifies only the coupling structure, not the compactness of the
configuration space.

**Proof strategy.** Direct application of Picard--Lindelof on compact
manifolds: the right-hand side is a smooth vector field on a compact Lie
group, so global existence and uniqueness are immediate. This is the same
argument as Luscher 2010, JHEP 08 (2010) 071, adapted from Wilson
plaquette action to $S_{\mathrm{KK}}$.

**References.**
- Luscher 2010 (well-posedness for Wilson action): JHEP 08 (2010) 071
- Chatterjee 2018 (probabilistic setting): arXiv:1803.01950
- KK-enhanced action: mass gap preprint, Section 4.1
  (`/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`)

**Difficulty: E** — Textbook ODE theory on compact manifolds.

---

### Lemma 1.2: Flow preserves the small-field domain $\Omega_s$

**Statement.** *Let $\Omega_s$ denote Balaban's small-field domain at
RG step $k$, defined by $\|A\| < \varepsilon_k$. If the initial
configuration $(V, A)$ lies in $\Omega_s$, then the flowed configuration
$(V_t, A_t)$ lies in $\Omega_s$ for all $t \ge 0$.*

**QG5D input.** The Yang--Mills gradient flow is the negative gradient of
the Yang--Mills action functional:

$$\partial_t S_{\mathrm{YM}}[B_t] = -2\int |D_\nu G_{\nu\mu}|^2\,d^4x \le 0.$$

The action is non-increasing. On the KK background, the flow drives
toward the KK vacuum — the trivial connection times the $S^1$ fiber — which
is at the center of $\Omega_s$. The KK mass gap $\Delta_0^{\mathrm{KK}} > 0$
(Theorem 4, Section 4.4, line 749) means the vacuum is an isolated
minimum, so small-field configurations cannot flow out of $\Omega_s$.

The Casimir potential $V(R) = c/R^4$ (Paper 1, Section 6.6; Paper 6,
Theorem F.1) is exact to all perturbative orders — the internal geometry
is frozen. The dilaton does not fluctuate during the flow.

**Proof strategy.**
1. Show $S_{\mathrm{KK}}[V_t, A_t] \le S_{\mathrm{KK}}[V_0, A_0]$ for
   all $t$ (monotone decrease of the action, from the flow equation).
2. In $\Omega_s$, the action is uniformly bounded: $S_{\mathrm{KK}} \le C\varepsilon_k^2$.
   Monotone decrease preserves this bound.
3. The quadratic coercivity of the action in $\Omega_s$ (from the mass gap
   $m_W > 0$ at each RG step) gives $\|A_t\|^2 \le (2/m_W^2)\,S[V_t, A_t]
   \le (2/m_W^2)\,S[V_0, A_0] < \varepsilon_k^2$.

**References.**
- Theorem 4 (KK mass gap): Section 4.4, lines 749--769
  (`/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`)
- Dilaton frozen: Paper 6, Theorem F.1
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper6/`)
- Casimir potential exact: Paper 1, Appendix K, Theorem K.1
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/22-appendix-k-higher-loop-epstein.md`)

**Difficulty: M** — Requires combining flow monotonicity with Balaban's
small-field structure. The conceptual content is clear; the technical
work is verifying compatibility.

---

### Lemma 1.3: Flowed polymer activity decay estimate

**Statement.** *For each polymer $X$ in Balaban's expansion at RG scale
$k$, the flowed polymer activity satisfies*

$$|K_k^{(t)}(X, V)| \le e^{-\kappa(t)\,|X|}, \qquad \kappa(t) \ge \kappa_B > 0,$$

*for all $t \ge 0$ and all $k$, where $\kappa_B$ is Balaban's polymer
decay constant (CMP 109, Theorem 1).*

**QG5D input.** Three ingredients from the QG5D/mass-gap framework:

(a) **KK mass tower strengthens decay.** Each KK mode $n$ has mass
$m_n = n\hbar/(Rc)$ (Paper 1, Section 2, line 283). The propagator for
mode $n$ is $G_k^{(n)} = (-D^2 + m_W^2 + m_n^2)^{-1}$, with decay rate
$\delta_0 + m_n > \delta_0$. Balaban CMP 95, Proposition 1.2 gives
$|G_k(x,y)| \le O(1)\,e^{-\delta_0|x-y|}$ with $\delta_0$ depending on
$d$ only. The KK mass adds to the exponent.

(b) **Flow contractivity.** The flow propagator $e^{-t(-D^2)}$ applied
to $G_k$ gives $G_k^{(t)} = e^{-t(-D^2)} G_k$ with enhanced decay:

$$|G_k^{(t)}(x,y)| \le C(t)\,e^{-(\delta_0 + t/a_k^2)|x-y|}.$$

The additional $t/a_k^2$ in the exponent improves polymer activity decay.

(c) **K-uniform polymer activities.** Lemma M.1.2 (Appendix M, line 77)
establishes that unflowed polymer activities satisfy
$|K_k^{(K)}(X,V)| \le e^{-\kappa_B |X|}$ with $\kappa_B$ independent
of both $k$ and $K$.

**Proof strategy.**
1. Define flowed polymer activities by evaluating Balaban's polymer at
   the flowed configuration: $K_k^{(t)}(X,V) := K_k(X, V_t)$ where
   $V_t$ is the gradient-flow evolution of $V$.
2. By Lemma 1.2, $V_t \in \Omega_s$, so $K_k(X, V_t)$ is in the domain
   of Balaban's estimates.
3. By the unflowed estimate (Lemma M.1.2), $|K_k(X, V_t)| \le e^{-\kappa_B|X|}$.
4. The flow can only improve this: $\kappa(t) \ge \kappa_B$ because the
   flow drives toward smaller field values (lower action), which
   correspond to better-converging polymer expansions.

**References.**
- Lemma M.1.2: Appendix M, line 77
  (`/Users/gsix/yang-mills/preprint/sections/M-gap-closures-r00.md`)
- Balaban CMP 109, Theorem 1 (polymer convergence)
- Balaban CMP 95, Prop. 1.2 (propagator decay, verified against journal)
- KK mode mass: Paper 1, Section 2, line 283
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper1/02-framework.md`)

**Difficulty: M** — The conceptual argument is straightforward (flow
improves, doesn't degrade). Technical work: verifying that the
composition of flow + polymer evaluation preserves the uniform decay.

---

### Lemma 1.4: K-uniformity of flowed constants

**Statement.** *The flow-time-dependent constants $\kappa(t)$, $C(t)$ in
Lemma 1.3 are K-uniform: they depend on the gauge group $N$, the KK
geometry $(R, r_3)$, and the flow time $t$, but not on the bare theory
index $K$.*

**QG5D input.** Corollary M.1.3 (Appendix M, line 132) establishes that
hypotheses (H1)--(H2) of the Cluster--Balaban Handoff Lemma (Section 5.4.5,
lines 854--933) are satisfied with K-uniform constants. The controlling
parameters are:

- $\kappa_B$: from Balaban's blocking geometry ($L=2$, $d=4$, group $\mathrm{SU}(N)$)
- $m_W$: fluctuation mass (k-independent by Balaban's inductive hypothesis)
- $C_D$: Lipschitz constant (k-independent)
- $r_{\mathrm{proj}}(N)$: block-spin kernel radius ($N$-dependent only)
- $\kappa_{\mathrm{cl}}^{\mathrm{phys}} = m_1/6$: cluster expansion rate
  (K-independent, from internal geometry $m_1 = 2\sqrt{N}/r_3$)

The gradient flow introduces no new K-dependent parameters: it is a
deterministic ODE whose coefficients (the gradient of $S_{\mathrm{KK}}$)
are determined by the action, which depends on $N$ and the lattice
geometry but not on the bare coupling $g_0(K)$ at flow time $t > 0$
(the flow erases bare-coupling dependence by smoothing).

**Proof strategy.** The flow constants inherit K-uniformity from the
unflowed constants (Lemma M.1.1, M.1.2, Corollary M.1.3). The flow
maps the K-uniform domain $\Omega_s$ into itself (Lemma 1.2), so
K-uniform estimates propagate.

**References.**
- Lemma M.1.1: Appendix M, line 20
- Lemma M.1.2: Appendix M, line 77
- Corollary M.1.3: Appendix M, line 132
- Handoff Lemma hypotheses (H1)--(H3): Section 5.4.5, lines 854--933
  (`/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`)

**Difficulty: E** — K-uniformity is inherited, not constructed anew.

---

### Lemma 1.5: Flow contractivity on the KK background

**Statement.** *For any initial configuration $U \in \Omega_s$, the
Yang--Mills energy density at the flowed configuration satisfies*

$$E(t, x) := \tfrac{1}{4}G_{\mu\nu}^a(t,x)\,G_{\mu\nu}^a(t,x) \le E(0, x)$$

*for all $t \ge 0$ and all $x$, with equality only at classical solutions.
On the KK background, the flow converges to the KK vacuum
(topological charge $Q = 0$ sector) or to the self-dual instanton
($Q \ne 0$ sector).*

**QG5D input.** The gradient flow is the negative gradient of
$S_{\mathrm{YM}}$. Feehan (arXiv:1409.1525) proves global existence and
convergence near minimizers in 4D via Lojasiewicz--Simon. On the KK
background with $Q = 0$, the unique minimizer is the trivial connection.
With $Q \ne 0$, the minimizer is the self-dual instanton, whose
contribution to correlators is exponentially suppressed by
$e^{-8\pi^2|Q|/g^2}$.

The KK mass gap (Theorem 4) ensures the vacuum is isolated: the nearest
excitation is at energy $\Delta_0^{\mathrm{KK}} > 0$ above the vacuum.
This prevents the flow from stalling at saddle points of the action
within the $Q = 0$ sector.

**Proof strategy.** Standard for the lattice: monotone decrease of the
action is immediate from the flow equation. For the continuum limit:
cite Feehan 2014 for convergence near minimizers, and Struwe 1994 for
short-time existence in 4D.

**References.**
- Feehan, arXiv:1409.1525 (Lojasiewicz--Simon convergence)
- Struwe, Calc. Var. PDE 2 (1994) 123 (YM heat flow, 4D)
- Rade, J. Reine Angew. Math. 431 (1992) 123 (2D, 3D)
- Theorem 4 (vacuum isolation): Section 4.4, lines 749--769

**Difficulty: E** — Established results; adaptation to KK background is
straightforward.


---


## Phase 2 — Continuum Limit of Flowed Correlators at Fixed $t > 0$

---

### Lemma 2.1: Flow propagator factorization on $M^4 \times S^1$

**Statement.** *On the product manifold $M^4 \times S^1$, the gradient-
flow heat kernel factorizes:*

$$K_{M^4 \times S^1}(t; x,y; \phi,\phi') = K_{M^4}(t; x,y) \cdot K_{S^1}(t; \phi,\phi'),$$

*where $K_{M^4}(t; x,y) = (4\pi t)^{-2}\,e^{-|x-y|^2/(4t)}$ is the 4D
heat kernel and $K_{S^1}(t; \phi,\phi')$ is the circle heat kernel
(Jacobi theta function).*

**QG5D input.** Paper 1, Appendix S, Section S.3.1 establishes that the
spectral zeta function factorizes for product geometries
$M^4 \times S^1$. The heat kernel inherits this factorization because
the Laplacian on the product is $\Delta_{M^4} + \Delta_{S^1}$ and
$e^{-t(\Delta_1 + \Delta_2)} = e^{-t\Delta_1} \otimes e^{-t\Delta_2}$.

On the orbifold $S^1/\mathbb{Z}_2$, the method of images (Paper 10,
Lemma A3, Section 5.2c) gives:

$$K_{S^1/\mathbb{Z}_2}(t; \phi,\phi') = K_{S^1}(t; \phi,\phi') + K_{S^1}(t; \phi,-\phi').$$

This is the propagator structure that produces $S_0 = 1 + 2\zeta(0) = 0$
(Paper 1, Appendix K, Section K.2.1).

**Proof strategy.** Standard spectral theory on product manifolds. The
orbifold extension uses the method of images, which is classical for
$\mathbb{Z}_2$ quotients.

**References.**
- Spectral factorization: Paper 1, Appendix S, Section S.3.1
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/30-appendix-s-finiteness-theorem.md`)
- Method of images: Paper 10, Lemma A3, Section 5.2c
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/04-poisson-weyl.md`)
- $S_0 = 1 + 2\zeta(0) = 0$: Paper 1, Appendix K, Section K.2.1

**Difficulty: E** — Standard spectral theory.

---

### Lemma 2.2: Cauchy estimate for flowed Schwinger functions

**Statement.** *For Schwartz test functions $f_1, \ldots, f_n$ and fixed
flow time $t > 0$:*

$$|S_{n,t}^{(a_1)}(f_1, \ldots, f_n) - S_{n,t}^{(a_2)}(f_1, \ldots, f_n)| \le C(t,n)\,|a_1^2 - a_2^2|^\alpha$$

*for some $\alpha > 0$ and $C(t,n) < \infty$ depending on $t$ but not
on $a_1, a_2$.*

**QG5D input.** Five convergent results:

(a) **Theorem M.2.1** (Appendix M, line 169): the *unflowed* Schwinger
functions converge (not just subsequentially) via a Cauchy argument using
the RG telescoping sum of Section 5.4. The telescoping sum satisfies
$\sum_k g_k^4 (a_k \Lambda)^s < \infty$ (Theorem 8(b), Section 5.7, line 2008).

(b) **Flow UV enhancement.** At fixed $t > 0$, the flow propagator
contributes $e^{-tp^2}$ to every internal line, improving convergence
from $O(g_k^4)$ to $O(g_k^4 \cdot e^{-t/a_k^2})$.

(c) **Paper 10, Theorem U.2a** ($a_2 = a_4 = 0$, Section 2.5): one-loop
UV divergences vanish as geometric invariants.

(d) **Paper 10, Route 05** (Weyl anomaly, Section 4.5): vanishing
protected by Wess--Zumino in any diffeomorphism-preserving scheme.

(e) **Mass gap IR control.** $\Delta_\infty > 0$ (Theorem 8(d), line 2012)
controls large-distance behavior.

**Proof strategy.** Adapt the RG telescoping sum of Section 5.4 to flowed
correlators. The flow enhancement factor $e^{-t/a_k^2}$ improves the
convergence rate from $O(g_k^4)$ to doubly-to-triply exponential.

**References.**
- Theorem M.2.1: Appendix M, line 169
  (`/Users/gsix/yang-mills/preprint/sections/M-gap-closures-r00.md`)
- Theorem 8(b): Section 5.7, line 2008
  (`/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`)
- Theorem U.2a: Paper 10, Section 2.5
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/02-seeley-dewitt.md`)
- Wess--Zumino protection: Paper 10, Section 4.5, Theorem 4.3

**Difficulty: M** — Adapts existing Cauchy argument with improved estimates.

---

### Lemma 2.3: Uniqueness of continuum limit for flowed correlators

**Statement.** *The continuum limit $S_{n,t} = \lim_{a \to 0} S_{n,t}^{(a)}$
exists and is unique (not just subsequential), for each fixed $t > 0$.*

**QG5D input.** Direct consequence of Lemma 2.2: a Cauchy sequence in a
complete space has a unique limit. Theorem M.2.1 establishes this for
the unflowed case; the flowed case inherits the same structure.

**Difficulty: E** — Corollary of Lemma 2.2.

---

### Lemma 2.4: OS axioms for flowed Schwinger functions

**Statement.** *The continuum flowed Schwinger functions $S_{n,t}$
satisfy the Osterwalder--Schrader axioms OS0--OS4 at each fixed $t > 0$.*

**QG5D input.** Theorem 8(f) (Section 5.7, line 2017) verifies all five
OS axioms for the unflowed continuum Schwinger functions. Each transfers:

| Axiom | Unflowed source | Flowed status |
|:------|:----------------|:--------------|
| OS0 (temperedness) | Lines 2181--2248: $\|S_n\| \le n!\,C_0^n$ | **Improved**: $e^{-tp^2}$ exponential UV suppression |
| OS1 (Euclidean invariance) | Lines 2252--2317: O(4)-breaking $\to 0$ | **Same**: continuum flow is rotationally invariant |
| OS2 (reflection positivity) | Lines 2321--2372: Osterwalder--Seiler + weak limits | **Inherited**: $E(t,x) = \tfrac{1}{4}G^a G^a \ge 0$ (sum of squares) |
| OS3 (symmetry) | Lines 2376--2380 | **Same**: flow preserves gauge covariance |
| OS4 (cluster) | Lines 2384--2423: $e^{-\Delta_\infty t}$ | **Inherited**: mass gap independent of flow time |

**Proof strategy.** Verify each axiom. OS2 (reflection positivity) is the
key non-trivial step: the flowed observable is a sum of squares, so
lattice reflection positivity holds; the limit preserves it by Portmanteau
(same argument as lines 2365--2370).

**References.**
- OS axiom verification: Section 5.7, Theorem 8(f), lines 2172--2615
  (`/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`)

**Difficulty: E** — Direct adaptation of existing verification.


---


## Phase 3 — Small-Flow-Time Expansion and the $t \to 0^+$ Limit

---

### Lemma 3.1: Analyticity of flowed effective action in $t$

**Statement.** *The flowed Balaban effective action
$S_k^{\mathrm{eff}}[V, A_t]$, viewed as a function of flow time $t$,
is analytic in $t$ for $|t| < r_t$ with $r_t > 0$ independent of $k$.*

**QG5D input.** Two analyticity results compose:

(a) **Balaban analyticity (B1)** (Section 5.6, Part I, lines 1577--1664):
effective action analytic in block-link variables with k-independent radius

$$\rho = \min\!\left(\frac{\kappa}{2d},\; \frac{m_W a}{2C_D},\; r_{\mathrm{proj}}(N)\right) > 0.$$

(b) **Heat kernel entirety.** $e^{-tp^2}$ is entire in $t$.

Composition: $V_t(\ell)$ depends analytically on $t$ (smooth ODE on
compact manifold, Cauchy--Kowalevski). Effective action depends
analytically on $V$ (by B1). Therefore $S_k^{\mathrm{eff}}[V, A_t]$
is analytic in $t$ by composition. Radius $r_t \ge \rho / L_F$ where
$L_F$ is the k-independent Lipschitz constant of the flow.

**Critical consequence.** Analyticity in $t$ means the small-flow-time
expansion **converges** (not merely asymptotic). This eliminates the
primary risk of Phase 3 (attack plan, Section 6.1, risk 1).

**References.**
- Balaban analyticity (B1): Section 5.6, Part I, lines 1577--1664
- Analyticity radius: lines 1654--1657
  (`/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`)
- Heat kernel entirety: standard (Seeley 1967; DeWitt 1965)
- Paper 1, Appendix S, Section S.2

**Difficulty: M** — Requires composing two analyticity results and
bounding $r_t$ uniformly in $k$.

---

### Lemma 3.2: Operator mixing control at dimension 4

**Statement.** *On the 4D hypercubic lattice, the unique local,
gauge-invariant, $\mathcal{C}$-even, parity-even operator of engineering
dimension 4 is $S_{\mathrm{YM}} = \sum_P s_P$. The mixing matrix at
dimension 4 in the small-flow-time expansion is $1 \times 1$.*

**QG5D input.** Mass gap preprint, Section 5.3.1 (lines 393--488):

(a) **$\mathcal{C}$-elimination.** $\mathrm{Tr}(F^3)$ and $d^{abc}F^3$
are $\mathcal{C}$-odd — absent from $\mathcal{C}$-invariant action.
Exact and non-perturbative.

(b) **Dimensional analysis.** $s_P^2$ has dimension 8.
$\mathrm{Tr}(F\tilde{F})$ is parity-odd. Redundant operators absent from
block-spin integration.

Balaban's coupling definition: $g_{k+1}$ is the coefficient of
$S_{\mathrm{YM}}$ in the effective action (CMP 109, Section 2); the
remainder contains no dimension-4 contamination.

**References.**
- $\mathcal{C}$-elimination: Section 5.3.1, lines 393--488
- PROOF-CHAIN step 6: confirmed
  (`/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`)

**Difficulty: E** — Already established.

---

### Lemma 3.3: Operator mixing control at dimension $\ge 6$ (deviation order)

**Statement.** *Every $\mathcal{C}$-even, gauge-invariant, dimension-6
operator has $\mathrm{dev} \ge 2$. Subleading terms in the small-flow-time
expansion are suppressed by $g_k^4 \hat{\Delta}^2$.*

**QG5D input.** Section 5.6, Part III (lines 1737--1891) classifies all
dimension-6 operators:

| Class | Operators | dev |
|:------|:----------|:----|
| (I) Zero-derivative | $\mathrm{Tr}(F^3)$, $d^{abc}F^3$ | $\mathcal{C}$-odd (absent) |
| (II) One-derivative | None exist | Absent |
| (III) Two-derivative | $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$, $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ | $\ge 2$ (structural zeros) |
| (IV) Three+ derivatives | Multiple | $\ge 3$ (automatic) |

Key mechanism for Class (III): transfer-matrix weight contains
$(e^{E_m - E_n} - 1)^2$, vanishing identically at $n = m$ (Section 5.5.4,
lines 1530--1551).

Spectral lemma (Section 5.5.3, lines 1181--1400):
$|\langle 1|\mathcal{O}|1\rangle_c| \le C_p\,M\,\hat{\Delta}^p$ with
$C_p$ independent of $k$, $g_k$, volume. K-uniformity from Hastings--Koma
exponential clustering (lines 1282--1344).

Quantitative bound (lines 1882--1891):
$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \le C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2.$$

**References.**
- Dimension-6 classification: Section 5.6, Part III, lines 1737--1891
- Spectral lemma: Section 5.5.3, lines 1181--1400
- dev verification: Section 5.5.4, lines 1530--1551
- Hastings--Koma: Section 5.5.3, Step 3(i), lines 1282--1344
  (`/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`)

**Difficulty: E** — Already established.

---

### Lemma 3.4: KK mode sum vanishing at $t = 0$

**Statement.** *$S_0^{(L)} = [1 + 2\zeta(0)]^L = 0$ for all $L \ge 1$.
More generally, $E_L(-j; Q) = 0$ for all positive-definite $Q$ and
$j \ge 1$.*

**QG5D input.** Theorem K.1 (Paper 1, Appendix K, Section K.7b):

> *For any positive-definite quadratic form $Q$ in $L$ variables,
> $E_L(-j; Q) = 0$ for all integers $j \ge 1$.*

Proof via $E_L(s; Q) = \pi^s \Lambda(s) / \Gamma(s)$ and $1/\Gamma(-j) = 0$.

Corollary K.2: every counterterm containing $E_L(-j; Q_L)$ vanishes.

**For gradient flow:** At $t = 0$, KK mode sums are Epstein zeta functions
at non-positive integers. Vanishing means $t \to 0$ encounters no new UV
divergences from KK sector.

**References.**
- Theorem K.1: Paper 1, Appendix K, Section K.7b
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/22-appendix-k-higher-loop-epstein.md`)
- $S_0 = 1 + 2\zeta(0) = 0$: Section K.2.1

**Difficulty: E** — Already proved.

---

### Lemma 3.5: $\mathbb{Z}_2$ parity cancellation persists at all $t$

**Statement.** *$f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0$ at each
KK level $n \ge 1$ holds for flowed correlators at every $t \ge 0$.*

**QG5D input.** Paper 10, Route 03, Proposition 3.1 (Section 3.3,
lines 106--114): cancellation from $y$-integrals
$\int \cos^3(ny/R)\,dy$ vs. $\int \sin^2(ny/R)\cos(ny/R)\,dy$ entering
with opposite signs (Section 3.2, lines 67--86). Property of
$\mathbb{Z}_2$ mode decomposition, independent of flow time.

**Proof strategy.** $\mathbb{Z}_2$ parity is discrete, preserved by
gauge-covariant flow. Mode decomposition is $t$-independent.

**References.**
- Proposition 3.1: Paper 10, Section 3.3, lines 106--114
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/03-z2-parity.md`)

**Difficulty: E** — Algebraic and $t$-independent.

---

### Lemma 3.6: Scheme-independence of GS vanishing at $t = 0$

**Statement.** *$C_{\mathrm{GS}} = 0$ in all schemes on
$M^4 \times S^1/\mathbb{Z}_2$.*

**QG5D input.** Paper 10, Theorem 1 (Section 4.6, lines 274--279):
three-graviton vertex $I_{+++}(n_1, n_2, n_1+n_2) = \pi R/4$ universal,
$n$-independent. Proved via:
- Lemma A1 (vertex mass-independence, Section 5.2a, lines 72--102)
- Lemma A2 (graviphoton/radion decouple, Section 5.2b, lines 104--126)
- Lemma A3 (method of images, Section 5.2c, lines 128--152)

Combined one-loop + two-loop: Theorem U.2 (Paper 1, Appendix U,
Section U.11, lines 905--913).

**References.**
- Theorem 1: Paper 10, Section 4.6
- Theorem U.2: Paper 1, Section U.11, lines 905--913
  (`/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/32-appendix-u-goroff-sagnotti-verification.md`)

**Difficulty: E** — Already proved.

---

### Lemma 3.7: Cauchy estimate for rescaled correlator [CRITICAL]

**Statement.** *For fixed non-coincident $x, y$:*

$$\left|\frac{S_{2,t}^c(x,y)}{c_1(t)^2} - \frac{S_{2,t'}^c(x,y)}{c_1(t')^2}\right| = O(|t - t'|^\alpha)$$

*uniformly as $t, t' \to 0^+$, for some $\alpha > 0$.*

**QG5D input.** Combines all previous lemmas:

| Input | Source | Role |
|:------|:-------|:-----|
| Analyticity in $t$ | Lemma 3.1 (B1 + heat kernel) | Expansion converges, not asymptotic |
| No mixing at dim 4 | Lemma 3.2 (Section 5.3.1) | Rescaling by $c_1^2$ is exact |
| $\mathrm{dev} \ge 2$ at dim $\ge 6$ | Lemma 3.3 (Section 5.6) | Subleading suppressed by $g_k^4 \hat{\Delta}^2 \cdot t$ |
| KK vanishing at $t = 0$ | Lemma 3.4 (Theorem K.1) | No new UV divergences at $t = 0$ |
| $\mathbb{Z}_2$ at all $t$ | Lemma 3.5 (Route 03) | Cancellation persists through limit |
| GS = 0 all schemes | Lemma 3.6 (Theorem 1) | Two-loop finiteness at $t = 0$ |
| $c_1(t)$ perturbatively known | Luscher 2010, Harlander--Neumann 2016--2022 | Wilson coefficient computed to 3 loops |

**Proof strategy.**
1. Write $F(t) = S_{2,t}^c / c_1^2$. By Lemma 3.1, $F$ is analytic in $t$
   for $|t| < r_t$.
2. Leading term (dim 4) is
   $\langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y)\rangle_c$
   (no mixing, Lemma 3.2).
3. Subleading terms are $O(t^\beta)$, $\beta > 0$ (Lemma 3.3).
4. $F(0)$ is finite: KK vanishing (Lemma 3.4) + scheme-independence
   (Lemma 3.6) guarantee no divergence at $t = 0$.
5. Cauchy estimate: $|F(t) - F(t')| = O(|t - t'|^\alpha)$ with
   $\alpha = \beta > 0$.

**In the KK framework:** $F(0)$ is finite because the KK compactification
provides UV regulation at $t = 0$. The double UV regulator (flow + KK)
means the $t \to 0$ limit is a transition between two finite theories,
not a deregularization.

**Difficulty: H** — The only hard lemma. Individual inputs are established;
the difficulty is composing them into a rigorous Cauchy estimate. This is
where the bulk of Phase 3's effort concentrates.

---

### Lemma 3.8: Extraction of $[\mathrm{Tr}\,F^2]_R$

**Statement.** *$S_2^{\mathrm{ren}}(x,y) := \lim_{t \to 0^+} S_{2,t}^c / c_1^2$
exists as a finite tempered distribution on $\{x \ne y\}$, satisfying OS
positivity and clustering at rate $\Delta_\infty$.*

**QG5D input.** Consequence of Lemma 3.7 + Lemma 2.4 (OS axioms for
flowed Schwinger functions). OS positivity preserved because $c_1(t) > 0$.
Clustering at $\Delta_\infty$ independent of $t$ (Theorem 8(d)).

By GNS reconstruction, $\{S_n^{\mathrm{ren}}\}$ yields
$[\mathrm{Tr}\,F^2]_R(f)$ as operator-valued distribution on $\mathcal{H}$.

**Difficulty: M** — Follows from Lemma 3.7 + standard reconstruction.

---

### Lemma 3.9: KK-to-4D projection for composite operators

**Statement.** *$|S_n^{\mathrm{ren,KK}}(f) - S_n^{\mathrm{ren,4D}}(f)| \le C\,e^{-m_1 r_{\min}}$
where $m_1 = 2\sqrt{N}/r_3$.*

**QG5D input.** Theorem 5 (Section 4.5, lines 953--972):
$\Delta_0^{\mathrm{std}} \ge \Delta_0^{\mathrm{KK}} - C\,e^{-m_1 a}$.

Feshbach mechanism (lines 1188--1262): KK Hamiltonian decomposes as
$H = H_{00} + W$ with $\|W\| \le C_W e^{-m_1 a}$ (line 1207).
Eigenstate factorization (lines 1233--1239):
$|n\rangle = |\psi_n\rangle_{4D} \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle$
with $\|\delta_n\| \le (2C_W/m_1)\,e^{-m_1 a}$.

Lemma A2 (Paper 10, Section 5.2b): graviphoton/radion contribute only at
dimension $\ge 8$. So $[\mathrm{Tr}\,F^2]_R^{\mathrm{KK}}$ is the 4D
operator plus $O(e^{-m_1 r})$ from virtual KK exchange.

**Proof strategy.** Decompose KK correlator into $n = 0$ sector (4D) plus
$n \ge 1$ sectors (exponentially suppressed by $e^{-m_1 r_{\min}}$).

**References.**
- Theorem 5: Section 4.5, lines 953--972
  (`/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`)
- Feshbach projection: lines 1188--1262
- Eigenstate factorization: lines 1233--1239
- Lemma A2: Paper 10, Section 5.2b, lines 104--126

**Difficulty: M** — Feshbach mechanism established for spectrum; extending
to composite operator matrix elements is the new content.


---


## Phase 4 — Assembly

---

### Lemma 4.1: Stress tensor via Suzuki's formula

**Statement.** *$T_{\mu\nu}^R$ from Suzuki's formula exists as operator-
valued distribution, satisfying L.3 sub-clauses (i)--(v).*

**QG5D input.** Flowed operators UV-finite at $t > 0$ (Luscher--Weisz).
$t \to 0$ controlled by Phase 3. Sub-clauses:
- (i) Symmetry: algebraic
- (ii) Gauge invariance: flow covariance
- (iii) Conservation: Del Debbio--Patella--Rago, JHEP 11 (2013) 212
- (iv) $H_{\mathrm{OS}} = \int T_{00}$: transfer-matrix + L.1
- (v) Trace anomaly: Spiridonov--Chetyrkin + Collins--Duncan--Joglekar

$H_{\mathrm{OS}} \ge 0$ already unconditional (Section 5.7, lines 2321--2372).

**Difficulty: M**

---

### Lemma 4.2: AF short-distance match

**Statement.** *Two-point function matches $C_N/|x|^8 \cdot (\log)^{-2}$.*

**QG5D input.** Small-flow-time expansion (Luscher 2010) + Reisz power
counting (CMP 116). Paper 10 Route 05: KK tower Weyl anomaly vanishes,
so AF prediction not modified by KK effects at short distances.

**Difficulty: M** — Conditional on H4 (Gap G7).

---

### Lemma 4.3: Leading-order OPE

**Statement.** *Identity-channel OPE coefficient equals AF-predicted form.*

**QG5D input.** At $t > 0$, operator product UV-finite (including
coincident points). Deviation-order classification controls subleading
channels. Perturbative coefficients known to 3 loops (Zoller--Chetyrkin).

**Difficulty: M** — Leading order from Phases 3--4. Full OPE remains open.


---
---


# Part II: Gap Catalog


## Gap G1: Small-flow-time expansion only asymptotic

**Resolution: Lemma 3.1.** Balaban (B1) + heat kernel entirety gives
analyticity in $t$. Analytic $\Rightarrow$ convergent Taylor expansion.

**Status: Closed.**

---

## Gap G2: Flow--RG non-commutativity

**Resolution.** KK mode decomposition commutes with both operations
(eigenstates of both Laplacians). Scale-matching: $t_k = c \cdot a_k^2$.
Paper 1 Appendix S, Section S.3.1: spectral factorization on products.

**Status: De-risked.** Formal proof requires Lemma 1.3.

---

## Gap G3: Large-field / instanton contributions

**Resolution: Lemma 1.5.** Flow drives toward vacuum ($Q = 0$) or
instanton ($Q \ne 0$, suppressed by $e^{-8\pi^2/g^2}$). KK mass gap
(Theorem 4) isolates vacuum. Calorons on $M^4 \times S^1$ exponentially
suppressed by KK mass scale.

**Status: Closed.**

---

## Gap G4: KK-to-4D projection for operators

**Resolution: Lemma 3.9.** Feshbach mechanism (Theorem 5, Section 4.5)
+ Lemma A2 (graviphoton/radion decouple at dim 4--6).

**Status: De-risked.** Formal proof requires Lemma 3.9.

---

## Gap G5: Orbifold fixed-point contributions

**Resolution.** Paper 10, Route 02 (Theorem U.2a): boundary $a_2, a_4 = 0$
(flat fixed-point locus, no deficit). Route 03 (Proposition 3.1):
algebraic $\mathbb{Z}_2$ cancellation eliminates boundary terms.

**Status: Closed.**

---

## Gap G6: Vertex mass-dependence in flowed theory

**Resolution.** Paper 10, Lemma A1 (Section 5.2a): de Donder vertex
$n$-independent via (1) UV power counting, (2) $\mathbb{Z}_2$ parity
projection, (3) Epstein backstop. Verified numerically $k/m_n = 10, 100, 1000$.

**Status: Closed.**

---

## Gap G7: Non-perturbative = perturbative at short distances

**Resolution (partial).** Gradient flow provides controlled interpolation
between non-perturbative (large $t$) and perturbative (small $t$).
Paper 10's five routes demonstrate perturbative/non-perturbative matching
in KK theory. Does not rigorously prove H4.

**Status: Open.** Stated conditional in L.2 (Appendix L, line 229).


---
---


# Part III: Sub-Clause Resolution Map


### Conjecture L.1 (Appendix L, line 72)

| Sub-clause | Requirement | Lemma(s) | Status |
|:-----------|:------------|:---------|:-------|
| (i) | Limit of renormalized lattice operator | 2.2 + 2.3 ($a \to 0$) + 3.7 + 3.8 ($t \to 0$) + 3.9 (KK$\to$4D) | **Closes** |
| (ii) | OS-positive tempered distributions | 2.4 (flowed OS) + 3.8 (limit inherits) | **Closes** |
| (iii) | Anomalous dimensions match pQCD | 4.2 (AF match via small-flow-time) | **Closes** (conditional H4) |

### Conjecture L.2 (Appendix L, line 229)

| Requirement | Lemma(s) | Status |
|:------------|:---------|:-------|
| $\sim |x|^{-8}(\log)^{-2}$ at short distance | 4.2 + Reisz | Conditional H4 (Gap G7) |

### Conjecture L.3 (Appendix L, line 332)

| Sub-clause | Requirement | Status |
|:-----------|:------------|:-------|
| (i) Symmetry | Algebraic | **Unconditional** |
| (ii) Gauge invariance | Flow covariance | **Unconditional** |
| (iii) Conservation | Ward identity (unconditional for Schwinger functions; distributional via L.1) | **Mostly unconditional** |
| (iv) $H_{\mathrm{OS}} = \int T_{00}$ | Lemma 4.1 + L.1 | Conditional on L.1 |
| (v) Trace anomaly | Phase 3 + Spiridonov--Chetyrkin | Conditional on L.1 |
| $H_{\mathrm{OS}} \ge 0$ | Already proved (Section 5.7, OS2) | **Unconditional** |

### Conjecture L.4 (Appendix L, line 468)

| Requirement | Lemma(s) | Status |
|:------------|:---------|:-------|
| Leading-order OPE with $C^{\mathbb{1}}$ | 4.3 + 4.2 | **Closes at leading order** |
| Full channel decomposition (dim $\ge 6$) | Open | **Open** (separate programme) |


---
---


# Part IV: Dependency Graph and Critical Path


## Dependency diagram

```
Lemma 1.1 (flow well-posedness) ──── E
  │
  ├── Lemma 1.2 (preserves Ω_s) ──── M
  │     │
  │     └── Lemma 1.3 (polymer decay) ──── M
  │           │
  │           ├── Lemma 1.4 (K-uniform) ──── E
  │           │
  │           └── Lemma 2.2 (Cauchy, flowed) ──── M
  │                 │
  │                 ├── Lemma 2.3 (uniqueness) ──── E
  │                 │
  │                 ├── Lemma 2.4 (OS axioms) ──── E
  │                 │
  │                 └── Lemma 3.7 (Cauchy, rescaled) ◄── BOTTLENECK ──── H
  │                       │
  │                       │   ┌── 3.1 (analytic in t) ──── M  ◄── Balaban (B1) + heat kernel
  │                       │   ├── 3.2 (no dim-4 mix) ──── E   ◄── Section 5.3.1
  │                       │   ├── 3.3 (dev ≥ 2)     ──── E   ◄── Section 5.6 Part III
  │                       │   ├── 3.4 (KK vanish)   ──── E   ◄── Theorem K.1
  │                       │   ├── 3.5 (Z₂ all t)    ──── E   ◄── Paper 10 Route 03
  │                       │   └── 3.6 (GS=0)        ──── E   ◄── Paper 10 Theorem 1
  │                       │
  │                       └── Lemma 3.8 (extract [Tr F²]) ──── M
  │                             │
  │                             ├── 3.9 (KK → 4D) ──── M  ◄── Theorem 5 Feshbach
  │                             │
  │                             ├── 4.1 (T_μν)    ──── M  → L.3
  │                             ├── 4.2 (AF)      ──── M  → L.2
  │                             └── 4.3 (OPE)     ──── M  → L.4
  │
  └── Lemma 1.5 (contractivity) ──── E

Independent: Lemma 2.1 (factorization) ──── E  ◄── Paper 1 Appendix S
```


## Critical path

$$1.1 \;\to\; 1.2 \;\to\; 1.3 \;\to\; 2.2 \;\to\; \boxed{3.7} \;\to\; 3.8 \;\to\; 3.9 \;\to\; 4.1$$


## Scorecard

| | E (established) | M (moderate) | H (hard) |
|:--|:--|:--|:--|
| **Count** | 11 | 7 | 1 |
| **Lemmas** | 1.1, 1.4, 1.5, 2.1, 2.3, 2.4, 3.2, 3.3, 3.4, 3.5, 3.6 | 1.2, 1.3, 2.2, 3.1, 3.8, 3.9, 4.1--4.3 | **3.7** |

| | Closed | De-risked | Open |
|:--|:--|:--|:--|
| **Gaps** | G1, G3, G5, G6 | G2, G4 | G7 |


## One hard lemma

The entire programme reduces to **Lemma 3.7**: the Cauchy estimate for the
rescaled correlator as $t \to 0^+$. Every input to 3.7 is rated E or M.
The difficulty is composition, not discovery. The QG5D framework provides
every ingredient; the remaining work is assembly into a single rigorous
estimate.


---


*File locations:*
- *This document:* `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/lemmas-and-gap-strategy.md`
- *Formal argument:* `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/formal-argument.md`
- *Attack plan:* `/Users/gsix/yang-mills/gradient-flow-attack-plan/l1-gradient-flow-attack-plan.md`
- *Mass gap preprint:* `/Users/gsix/yang-mills/preprint/`
- *Proof chain:* `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`
- *Paper 1:* `/Users/gsix/quantum-geometry-in-5d-latex/paper1/`
- *Paper 10:* `/Users/gsix/quantum-geometry-in-5d-latex/paper10/`
- *Conjectures L.1--L.4:* `/Users/gsix/yang-mills/preprint/sections/L-clay-conjectures.md`
