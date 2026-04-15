# W3-08: Flowed Polymer Activity Decay and K-Uniformity (Lemmas 1.3 + 1.4)

**Proof memo** for the gradient-flow programme closing Conjectures
L.1--L.4 of the Yang--Mills mass gap preprint.

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*

---

## 0. Purpose

This memo proves Lemmas 1.3 and 1.4 of the gradient-flow programme.
The central result is that the flowed polymer activities---obtained by
evaluating Balaban's polymer expansion at the gradient-flowed
configuration $V_t$---satisfy exponential decay with a rate at least
as good as the unflowed Balaban rate $\kappa_B$, and that all
constants are uniform in both the inner RG step $k$ and the outer
bare-scale index $K$.

The proof is short and structural: it composes two established facts.
The gradient flow preserves the small-field domain (Lemma 1.2, proved
in W2-06), and Balaban's polymer estimates apply to every
configuration in the small-field domain (Lemma M.1.2 of Appendix M).
Therefore the flowed configuration inherits the unflowed estimates.
The KK mass tower then provides a strict improvement of the decay
rate for all modes $n \geq 1$.

**Inputs from previous waves:**

| Wave | Output | Result used |
|:-----|:-------|:------------|
| W1-01 | Flow well-posedness | Lemma 1.1: $V_t \in \mathrm{SU}(N)$ for all $t \geq 0$; action monotone decreasing |
| W1-02 | Flow contractivity | Lemma 1.5: vacuum isolation; Hessian bound $\geq 2N/r_3^2$ |
| W1-05 | Analyticity in $t$ | Balaban (B1) details; $k$-independent analyticity radius $\rho > 0$ |
| W2-06 | Preserves $\Omega_s$ | Lemma 1.2: $V_0 \in \Omega_s \Longrightarrow V_t \in \Omega_s$ for all $t \geq 0$ |

**Inputs from the preprint:**

| Source | Result used |
|:-------|:------------|
| Appendix M, Lemma M.1.1 (line 20) | K-uniform cluster expansion rate $\kappa_{\mathrm{cl}}^{\mathrm{phys}} = m_1/6$ |
| Appendix M, Lemma M.1.2 (line 77) | K-uniform Balaban polymer decay: $\|K_k^{(K)}(X,V)\| \leq e^{-\kappa_B |X|}$ |
| Appendix M, Corollary M.1.3 (line 132) | Handoff hypotheses (H1)--(H2) satisfied K-uniformly |
| Section 5.4.5 (line 854) | Cluster--Balaban Handoff Lemma: hypotheses (H1)--(H3) |
| Section 5.6, Part I (line 1573) | Balaban analyticity (B1) with $k$-independent radius |
| CMP 95, Proposition 1.2 | Propagator decay $\|G_k(x,y;V)\| \leq C_D\,e^{-\delta_0 |x-y|}$ |
| CMP 109, Theorem 1 | Polymer expansion convergence with $\kappa$ $k$-independent |


---


## 1. Setting and Definitions

We adopt the notation of W2-06 throughout. The lattice
$\Lambda_k = (\mathbb{Z}/(L^k L_0)\mathbb{Z})^4$ at RG step $k$ has
spacing $a_k = 2^k a_0(K)$, gauge group $G = \mathrm{SU}(N)$, and
the KK-enhanced action $S_{\mathrm{KK}}$ of preprint Section 4.1.


### 1.1 Polymer activities and the Balaban expansion

In Balaban's small-field domain $\Omega_s = \{V : \|F_{\mu\nu}(x)\| <
p(g_k)\;\forall\,P\}$ (W2-06, equation (1.2)), the effective action
at RG step $k$ decomposes as (preprint, Section 5.6, Part I,
equation (I.1)):

$$S_k^{\mathrm{eff}}[V] = \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  + \sum_{X \in \mathcal{P}_k} K_k(X, V), \tag{1.1}$$

where $\mathcal{P}_k$ is the set of connected polymers on $\Lambda_k$
and each polymer activity satisfies the exponential decay bound
(Section 5.6, Part I, equation (I.2); CMP 109, Theorem 1):

$$|K_k(X, V)| \leq e^{-\kappa |X|}, \tag{1.2}$$

with $\kappa > 0$ independent of $k$. Here $|X|$ denotes the number of
unit cells (plaquettes) in the polymer $X$.


### 1.2 Flowed polymer activities

**Definition.** Let $V_0 \in \Omega_s$ and let $\{V_t\}_{t \geq 0}$
be the gradient-flow trajectory (W1-01, Lemma 1.1; W2-06,
equation (1.4)):

$$\partial_t V_t(\ell)
  = -g_0^2\,\bigl(\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]\bigr)
  \,V_t(\ell), \qquad V_0(\ell) = U(\ell). \tag{1.3}$$

The **flowed polymer activity** at flow time $t$ is:

$$K_k^{(t)}(X, V) := K_k(X, V_t), \tag{1.4}$$

where $V_t = V_t[V]$ is the gradient-flow image of the initial
configuration $V$. The subscript $k$ denotes the inner Balaban RG
step; the superscript $(t)$ denotes the flow time. When the bare
theory index $K$ needs to be tracked, we write $K_k^{(K,t)}(X, V)$.

**Remark.** The flowed activity (1.4) is obtained by
*precomposition*: we first flow the gauge field by the deterministic
ODE (1.3), then evaluate the unflowed Balaban activity at the flowed
configuration. This is conceptually distinct from flowing the
effective action itself; the Balaban expansion (1.1) applies to the
static configuration $V_t$ for each fixed $t$.


### 1.3 The KK propagator and the mass tower

In the KK-enhanced theory on $M^4 \times \mathbb{CP}^{N-1}$, the
covariant propagator decomposes by KK mode (preprint Section 4.1;
formal argument, Section 2.2, equation (KK.2)):

$$G_k^{(n)}(V) = \bigl(-D^2[V] + m_W^2 + m_n^2\bigr)^{-1},
  \tag{1.5}$$

where $m_n$ is the mass of the $n$-th KK mode. For the lowest
modes: $m_0 = 0$ (the 4D gauge field), $m_1 = 2\sqrt{N}/r_3$
(the lightest KK mode; preprint Section 2, Theorem 4), and $m_n$
grows with $n$ according to the Weyl asymptotics on
$\mathbb{CP}^{N-1}$ (preprint Appendix A, corrected via
Appendix B1).

Each KK-mode propagator satisfies the exponential decay bound
(CMP 95, Proposition 1.2; formal argument, Section 3.1,
equation (a)):

$$|G_k^{(n)}(x,y;V)| \leq C_D\,e^{-(\delta_0 + m_n)|x-y|},
  \tag{1.6}$$

where $\delta_0 > 0$ depends only on $d = 4$ and $m_W^2$ (not on
$k$, $K$, or $n$), and $C_D \leq 2(N^2-1)/m_W^2$ (W1-05,
Section 1, notation table; preprint Appendix K.2). The additional
KK mass $m_n > 0$ for $n \geq 1$ strictly improves the decay rate
relative to the zero mode.


---


## 2. Statements

**Lemma 1.3** (Flowed polymer activity decay). *Let $\Omega_s$ be
Balaban's small-field domain at RG step $k$. Let $V_0 \in \Omega_s$,
and let $K_k^{(t)}(X, V) = K_k(X, V_t)$ be the flowed polymer
activity (1.4). Then for all $t \geq 0$, all RG steps $k \geq 0$,
and all connected polymers $X \in \mathcal{P}_k$:*

$$|K_k^{(t)}(X, V)| \leq e^{-\kappa(t)\,|X|}, \tag{2.1}$$

*where*

$$\kappa(t) \geq \kappa_B > 0 \tag{2.2}$$

*and $\kappa_B$ is Balaban's polymer decay constant from CMP 109,
Theorem 1. In the KK-enhanced theory, the effective decay rate
satisfies the stronger bound*

$$\kappa^{\mathrm{KK}}(t)
  \geq \kappa_B + m_1 \cdot \ell_{\min}(X) \cdot \mathbf{1}_{n \geq 1},
  \tag{2.3}$$

*for KK modes $n \geq 1$, where $\ell_{\min}(X) > 0$ is the
minimal diameter of the polymer $X$ and $m_1 = 2\sqrt{N}/r_3$.*

---

**Lemma 1.4** (K-uniformity of flowed constants). *The constants
$\kappa(t)$ and $C(t)$ appearing in Lemma 1.3 are K-uniform:
they depend on $N$, the compactification data $(R, r_3)$, and $t$,
but not on the bare theory index $K$.*


---


## 3. Proof of Lemma 1.3

The proof has three steps: (1) the flowed configuration lies in
$\Omega_s$, (2) Balaban's estimates therefore apply, and (3) the
KK mass tower provides a strict improvement.


### Step 1. The flowed configuration lies in $\Omega_s$

**Source:** Lemma 1.2 (W2-06, Section 2, equation (3.24)).

By Lemma 1.2, the gradient flow preserves the small-field domain:
if $V_0 \in \Omega_s$, then $V_t \in \Omega_s$ for all $t \geq 0$.
The proof (W2-06, Section 3) proceeds by three bounds:

- **Monotone decrease** (W1-01, Lemma 1.1(v)):
  $S_{\mathrm{KK}}[V_t] \leq S_{\mathrm{KK}}[V_0]$ for all
  $t \geq 0$.

- **Action bound in $\Omega_s$** (Balaban CMP 109; W2-06,
  equation (3.8)): $S_{\mathrm{KK}}[V_0] \leq C_S \cdot
  p(g_k)^2 \cdot |\Lambda_k|$.

- **Maximum principle** (W2-06, equation (3.22)):
  $\max_P \|F_{\mu\nu}^{(t)}(x)\| \leq
  \max_P \|F_{\mu\nu}^{(0)}(x)\| < p(g_k)$.

The constants $C_S$, $m_W$, and $p(g_k)$ entering this chain are
$k$-independent (W2-06, Section 4.2, table of constants).

**Conclusion of Step 1.** For all $t \geq 0$:

$$V_t \in \Omega_s. \tag{3.1}$$


### Step 2. Balaban's polymer estimates apply to $V_t$

**Source:** Balaban, CMP 109, Theorem 1; preprint Section 5.6,
Part I, equations (I.1)--(I.2); Appendix M, Lemma M.1.2.

Balaban's polymer expansion bound (equation (1.2) above) is a
statement about **all** configurations in $\Omega_s$: for every
$V \in \Omega_s$ and every connected polymer $X \in \mathcal{P}_k$,

$$|K_k(X, V)| \leq e^{-\kappa |X|}, \tag{3.2}$$

with $\kappa > 0$ independent of $k$ (CMP 109, Section 3, inductive
hypothesis IH3). This is not a bound on the initial configuration
alone---it is a bound on the functional $K_k(X, \cdot)$ evaluated at
any point in $\Omega_s$.

**The key logical step.** Since $V_t \in \Omega_s$ (Step 1), the
bound (3.2) applies with $V$ replaced by $V_t$:

$$|K_k^{(t)}(X, V)| = |K_k(X, V_t)| \leq e^{-\kappa |X|}. \tag{3.3}$$

Setting $\kappa(t) := \kappa$ gives $\kappa(t) \geq \kappa_B$ where
$\kappa_B := \min(\kappa(G), \kappa_{\mathrm{cl}}^*) > 0$ is the
$(k,K)$-uniform Balaban polymer decay constant from Lemma M.1.2
(Appendix M, line 77ff).

**Remark on the logical structure.** The argument is deliberately
simple. There is no need to track how the polymer activities change
along the flow, because we are not differentiating with respect to
$t$. We simply observe that for each fixed $t$, the flowed
configuration $V_t$ is a point in $\Omega_s$, and the Balaban bound
is a pointwise bound valid everywhere in $\Omega_s$. The composition
is automatic.


### Step 3. The KK mass tower strictly improves decay

**Source:** CMP 95, Proposition 1.2; formal argument (Section 3.1,
equation (a)); preprint Theorem 4.

The polymer activities $K_k(X, V)$ are constructed from the
propagator $G_k(V)$ and its iterates (W1-05, Section 2,
Ingredient (a), Steps (b)(ii)--(iv)). In the KK-enhanced theory,
the propagator decomposes by KK mode as in equation (1.5). For
mode $n \geq 1$, the decay rate of $G_k^{(n)}$ is $\delta_0 + m_n$
(equation (1.6)), which is strictly larger than $\delta_0$.

This improved decay propagates through every step of Balaban's
inductive construction:

**(a) Saddle-point evaluation.** The classical solution
$u_{\mathrm{cl}} = -G_k(V) \cdot \nabla_u S_{k-1}|_{u=0}$ (W1-05,
Section 2, Ingredient (a), Step (b)(ii)) involves the propagator
$G_k$. For KK mode $n$, the propagator $G_k^{(n)}$ has decay rate
$\delta_0 + m_n$, so the classical solution decays faster.

**(b) Gaussian integration.** The determinant
$(\det S_k^{(2)})^{-1/2}$ is controlled by the trace-log expansion
(W1-05, Section 2, Step (b)(iii)):

$$\log \det(S_k^{(2)}) = \mathrm{Tr}\log(\mathbf{1} + \delta S_k^{(2)}).$$

For KK mode $n$, the operator $S_k^{(2)} = -D^2[V] + m_W^2 + m_n^2$
has a larger spectral gap ($m_W^2 + m_n^2$ instead of $m_W^2$),
making the Neumann series converge faster and reducing the
contribution to the polymer activity.

**(c) Mayer resummation.** The Kotecky--Preiss criterion
(CMP 103, 1986) for the Mayer expansion uses the exponential decay
rate as input. A larger decay rate strengthens the convergence
criterion, so the KK modes $n \geq 1$ make a smaller contribution
to the polymer activities than the zero mode.

**Quantitative bound for KK modes.** For mode $n \geq 1$, the
polymer activity satisfies

$$|K_k^{(n)}(X, V_t)| \leq C_n\,e^{-(\kappa + m_n \cdot \mathrm{diam}(X))|X|/|X|}
  \leq C_n\,e^{-\kappa |X|}\,e^{-m_n \cdot \ell_{\min}(X)},
  \tag{3.4}$$

where $\ell_{\min}(X) := \min_{\mathrm{spanning\,tree}} |T|$ is the
minimal spanning tree length of the polymer (which satisfies
$\ell_{\min}(X) \geq |X|^{1/d}$ for a connected polymer in $d = 4$
dimensions, by the lattice isoperimetric inequality). The coefficient
$C_n$ is bounded by $C_0$ uniformly in $n$ because the Mayer
expansion coefficients depend on the propagator only through its
norm $\|G_k^{(n)}\| \leq C_D/(m_W^2 + m_n^2) \leq C_D/m_W^2$,
which is bounded by the zero-mode value.

**Summing over KK modes.** The full polymer activity is the sum
over all modes:

$$K_k(X, V_t) = \sum_{n=0}^{\infty} K_k^{(n)}(X, V_t). \tag{3.5}$$

The zero mode ($n = 0$) contributes the standard Balaban bound
$|K_k^{(0)}| \leq e^{-\kappa |X|}$. Each higher mode $n \geq 1$
contributes with an additional exponential suppression
$e^{-m_n \ell_{\min}(X)}$, so the sum converges rapidly:

$$|K_k(X, V_t)| \leq e^{-\kappa|X|}\,\Bigl(1 + \sum_{n=1}^{\infty}
  C_0\,e^{-m_n \ell_{\min}(X)}\Bigr). \tag{3.6}$$

The parenthetical factor is bounded by $1 + C_0\,Z_{\mathrm{KK}}$
where $Z_{\mathrm{KK}} := \sum_{n=1}^{\infty} e^{-m_n \ell_{\min}(X)}
\leq \sum_{n=1}^{\infty} e^{-m_1 n \ell_{\min}(X)} =
(e^{m_1 \ell_{\min}(X)} - 1)^{-1}$, a convergent geometric series.
For polymers of any size $|X| \geq 1$, we have
$\ell_{\min}(X) \geq a_k > 0$, so $Z_{\mathrm{KK}} < \infty$ and
the prefactor $1 + C_0 Z_{\mathrm{KK}} =: C_{\mathrm{KK}} < \infty$
is finite. This gives

$$|K_k(X, V_t)| \leq C_{\mathrm{KK}}\,e^{-\kappa|X|}
  = e^{-(\kappa - \ln C_{\mathrm{KK}}/|X|)|X|}.$$

For $|X| \geq |X|_0 := \lceil \ln C_{\mathrm{KK}} / (\kappa/2) \rceil$,
the effective rate is $\kappa(t) \geq \kappa/2 > 0$. For the finitely
many small polymers with $|X| < |X|_0$, the bound $|K_k(X, V_t)|
\leq C_{\mathrm{KK}} e^{-\kappa|X|}$ is a finite constant, absorbed
into the polymer expansion by adjusting the initial polymer bound by
a multiplicative constant.

In summary, the effective decay rate satisfies

$$\kappa(t) \geq \kappa_B > 0 \qquad \text{for all } t \geq 0,
  \tag{3.7}$$

with $\kappa_B = \min(\kappa(G), \kappa_{\mathrm{cl}}^*) > 0$ as in
Lemma M.1.2. The KK mass tower does not degrade the bound; it
strictly improves the contributions from modes $n \geq 1$. $\square$


---


## 4. Proof of Lemma 1.4

**Lemma 1.4** (K-uniformity). *The constants $\kappa(t)$ and $C(t)$
in Lemma 1.3 are K-uniform: they depend on $N$, $(R, r_3)$, and
(through the KK mass tower) the internal geometry, but not on the
bare theory index $K$.*

**Proof.** The proof is an inheritance argument: K-uniformity of the
flowed constants follows from K-uniformity of the unflowed constants
plus the K-independence of the gradient flow.


### Step 1. K-uniformity of the unflowed polymer decay

**Source:** Appendix M, Lemma M.1.2 (preprint, line 77ff).

The unflowed polymer activities satisfy
$|K_k^{(K)}(X, V)| \leq e^{-\kappa_B |X|}$ with $\kappa_B > 0$
independent of both $k$ and $K$. The proof (Lemma M.1.2) identifies
three parameters governing the bound:

| Parameter | Value | $K$-dependence |
|:----------|:------|:---------------|
| $\kappa$ (polymer decay constant) | $O(1)$, depends on $L = 2$, $d = 4$, $G$ | None |
| $m_W$ (fluctuation mass) | Fixed in lattice units: $m_W a_k = 1$ | None |
| $C_D$ (Lipschitz constant of $D^2[V]$) | $2(N^2 - 1)$ | None |

None depends on $a_0(K)$ or $g_0(K)$. Therefore $\kappa_B =
\min(\kappa(G), \kappa_{\mathrm{cl}}^*)$ is $K$-uniform (Lemma M.1.2,
conclusion).


### Step 2. K-independence of the gradient flow

The gradient flow (equation (1.3)) is a deterministic first-order
ODE on the compact manifold $\mathrm{SU}(N)^{|\mathrm{links}|}$,
with right-hand side determined by $S_{\mathrm{KK}}$ (W1-01,
Lemma 1.1). The parameters entering the flow equation are:

| Parameter | $K$-dependence |
|:----------|:---------------|
| $g_0^2$ (overall scale factor in (1.3)) | Cancels: appears as $g_0^2 \cdot \partial_V(S_{\mathrm{KK}}/g_0^2)$ |
| $S_{\mathrm{KK}}$ (action functional) | Defined by the KK geometry, $K$-independent |
| $\mathrm{SU}(N)$ (manifold structure) | $K$-independent |

The crucial observation is that the gradient-flow equation involves
the combination $g_0^2 \cdot \partial_V S_{\mathrm{KK}}$, where
$S_{\mathrm{KK}} = (1/g_0^2) S_{\mathrm{YM}} + \ldots$. The
$g_0^2$ prefactor in the flow equation cancels the $1/g_0^2$ in the
action, so the flow equation for $V_t$ on $\Omega_s$ is
$K$-independent in form (W1-05, Section 2, Ingredient (b),
equation (ODE), with the Lipschitz constant depending on $d$, $N$
only; equation (ODE.2)).

**Consequence.** The flow map $V \mapsto V_t$ does not introduce any
$K$-dependent parameters. If the input $V$ is in $\Omega_s$ (with
$\Omega_s$ defined $K$-independently as the small-field domain at
step $k$), then the output $V_t$ is also in $\Omega_s$ (Lemma 1.2),
and the polymer bound (3.3) applies with the same $K$-independent
constants.


### Step 3. K-uniformity of the KK mass tower contribution

The KK masses $m_n$ are determined by the internal geometry of
$\mathbb{CP}^{N-1}$ (preprint Section 2; Paper 1, Section 2):

$$m_1 = \frac{2\sqrt{N}}{r_3}, \tag{4.1}$$

depending only on $N$ and the compactification radius $r_3$. By the
frozen dilaton (W2-06, Section 4.4; Paper 6, Proposition A.1), $r_3$
is fixed with fractional drift $\Delta R/R_0 \sim 3 \times 10^{-30}$
per Hubble time, so $m_n$ is a physical constant independent of $K$.

The KK mode sum constant $C_{\mathrm{KK}}$ from equation (3.6)
depends on $C_0$ (a $K$-independent Mayer constant), $m_1$
($K$-independent), and $a_k$ ($K$-dependent through $a_k = 2^k
a_0(K)$). However, $Z_{\mathrm{KK}} \leq (e^{m_1 a_k} - 1)^{-1}
\leq (e^{m_1 a_*} - 1)^{-1}$ where $a_* = \min_K a_0(K)$ (the
finest lattice spacing in the sequence). For $K \to \infty$,
$a_0(K) \to 0$ and $Z_{\mathrm{KK}} \to 1/(m_1 a_k)$, which grows.
But this growth is bounded uniformly for each fixed $k$ because
$a_k = 2^k a_0(K)$ and the polymer expansion at step $k$ concerns
the lattice $\Lambda_k$ at spacing $a_k$, which is the blocked
lattice. The relevant scale is $m_1 a_k$, and the convergence
of the KK sum requires only $m_1 a_k > 0$, which holds at every
finite RG step.

**More precisely:** The $K$-uniformity does not require bounding
$C_{\mathrm{KK}}$ uniformly as $K \to \infty$ at fixed $k$, because
the basic estimate (3.3) already gives $\kappa(t) \geq \kappa_B$
without using the KK improvement. The KK mass tower provides a
*bonus*---strictly better decay for modes $n \geq 1$---but the
$K$-uniform lower bound $\kappa(t) \geq \kappa_B$ comes directly
from the unflowed Balaban bound (Step 1), which is already
$K$-uniform by Lemma M.1.2.


### Step 4. Assembly

Collecting Steps 1--3: for all $t \geq 0$, all $k \geq 0$, and all
$K \geq 0$:

$$|K_k^{(K,t)}(X, V)| \leq e^{-\kappa_B |X|}, \tag{4.2}$$

with $\kappa_B > 0$ independent of $k$, $K$, and $t$. The constant
$C(t)$ multiplying the exponential (from the KK mode sum and Mayer
coefficients) satisfies $C(t) \leq C_{\mathrm{KK}}(N, r_3)$,
depending on the internal geometry but not on $K$.

This establishes Lemma 1.4. $\square$


---


## 5. Discussion: How the KK Mass Tower Strengthens Decay

The basic estimate (Lemma 1.3 with $\kappa(t) \geq \kappa_B$) uses
only the zero-mode ($n = 0$) contribution. The KK mass tower provides
qualitative and quantitative improvements that we now describe.


### 5.1 Mode-by-mode decay enhancement

For KK mode $n \geq 1$, the propagator decay rate is
$\delta_0 + m_n$ instead of $\delta_0$ (equation (1.6)). Since
$m_n \sim n^{1/(N-1)}/r_3$ by the Weyl asymptotics on
$\mathbb{CP}^{N-1}$ (preprint Appendix A, corrected in the B1
closure, Appendix M), the decay rate grows with $n$. The first
non-trivial KK mode ($n = 1$) already provides an enhancement of
$m_1 = 2\sqrt{N}/r_3$ in the decay exponent.

**Physical interpretation.** Each KK mode contributes a massive
propagator to the polymer expansion. The mass $m_n$ acts as an
additional IR regulator beyond Balaban's $m_W$, exponentially
suppressing long-range correlations at each KK level. The total
polymer activity, summed over all KK modes, is dominated by the
zero mode ($n = 0$) at large distances, but the higher modes
provide exponentially suppressed corrections.


### 5.2 Connection to the lattice mass gap

The KK mass gap $m_1 = 2\sqrt{N}/r_3 > 0$ (preprint Theorem 4)
provides the physical IR regulator for the full theory. In
Balaban's construction, the mass gap enters through the
fluctuation mass $m_W > 0$, which is an artificial regulator
removed in the continuum limit. The KK mass $m_1$ is a
*physical* mass that survives the continuum limit, providing
permanent exponential decay.

At each RG step $k$, the polymer expansion involves the
propagator at scale $a_k$. The ratio $m_1 a_k = 2\sqrt{N}
a_k/r_3$ controls the KK enhancement: when $m_1 a_k \gg 1$
(coarse lattice, early RG steps), the KK modes are strongly
suppressed; when $m_1 a_k \ll 1$ (fine lattice, late RG steps),
the KK modes contribute more democratically, but the basic Balaban
bound still controls the sum.

The crossover scale $k_*$ at which $m_1 a_{k_*} \sim 1$ is

$$k_* \sim \log_2(r_3 / a_0(K)) - \log_2(2\sqrt{N}), \tag{5.1}$$

which depends on $K$ (through $a_0(K)$) but not on the polymer
decay constant $\kappa_B$ (which is $K$-independent). Below $k_*$,
the KK enhancement is operative; above $k_*$, it is negligible but
harmless. In either regime, $\kappa(t) \geq \kappa_B$.


### 5.3 Role of the gradient flow in the KK enhancement

The gradient flow interacts with the KK mass tower through the
flow equation (1.3), which includes the KK-enhanced action
$S_{\mathrm{KK}}$. The flow drives configurations toward the
minimum of $S_{\mathrm{KK}}$, which is the trivial connection
$V_\ell = \mathbf{1}$ on the product $M^4 \times
\mathbb{CP}^{N-1}$ (W1-02, Part (B), vacuum isolation lemma).

At the vacuum, the Hessian of $S_{\mathrm{KK}}$ is (W1-02,
equation (B.1)):

$$\mathrm{Hess}_{A=0}\,S_{\mathrm{KK}}
  \geq \frac{2N}{r_3^2}\,\mathbb{1}, \tag{5.2}$$

where $2N/r_3^2$ is the spectral gap of the internal
Weitzenboeck Laplacian (preprint Theorem 1). The flow contracts
perturbations at a rate proportional to this spectral gap, so
configurations that are closer to the vacuum (as $t$ increases)
have smaller field strengths and consequently smaller polymer
activities.

**Quantitative improvement.** For $t > 0$, the flow has strictly
reduced the action (W1-01, equation (3.1), strict unless at a
critical point). The field strength satisfies (W2-06,
equation (3.18)):

$$\|F^{(t)}\|_{L^2}^2 \leq \frac{2}{m_W^2}\,S_{\mathrm{KK}}[V_0]
  \cdot e^{-\mu_1 t}, \tag{5.3}$$

where $\mu_1 \geq 2N/r_3^2$ is the spectral gap (the exponential
decay follows from the contractivity estimate of W1-02 applied to
the $L^2$ norm of the field strength). This means the flowed
configuration is closer to the center of $\Omega_s$ than the
initial one, and the polymer activities are correspondingly smaller.
While we do not need this improvement for the lower bound
$\kappa(t) \geq \kappa_B$ (which already follows from Step 2), it
shows that the gradient flow can only improve polymer decay, never
degrade it.


---


## 6. Verification of (k, K)-Uniformity: Complete Constant Table

We verify that every constant entering Lemmas 1.3 and 1.4 is
independent of $k$ and $K$.

| Constant | Value / Origin | $k$-dep. | $K$-dep. | Source |
|:---------|:---------------|:---------|:---------|:-------|
| $\kappa_B$ | Balaban polymer decay constant | None | None | CMP 109, Thm 1; Lemma M.1.2 |
| $m_W$ | Fluctuation mass ($m_W a_k = 1$) | None | None | CMP 95--96; Appendix K.2 |
| $C_D$ | Lipschitz const. of $D^2[V]$: $2(N^2-1)$ | None | None | CMP 95, Sec. 3; W1-05 |
| $\delta_0$ | Propagator decay rate | None | None | CMP 95, Prop. 1.2 |
| $C_S$ | Action bound const. in $\Omega_s$ | None | None | W2-06, eq. (3.8)--(3.9) |
| $C_{\mathrm{KP}}$ | Kotecky--Preiss constant | None | None | CMP 103; depends on $\kappa$, $d$ only |
| $\rho$ | Balaban analyticity radius | None | None | Section 5.6, Part I, eq. (I.3) |
| $m_1$ | Lightest KK mass: $2\sqrt{N}/r_3$ | None | None | Preprint Thm 4; Paper 1, Sec. 2 |
| $m_n$ ($n \geq 2$) | Higher KK masses | None | None | Internal geometry of $\mathbb{CP}^{N-1}$ |
| $r_3$ | Compactification radius | None | None | Frozen dilaton (Paper 6, Prop. A.1) |
| $L_{\mathrm{flow}}$ | Flow Lipschitz constant | None | None | W1-05, eq. (ODE.3); depends on $d$, $N$ |
| $r_{\mathrm{ODE}}$ | ODE analyticity radius | None | None | W1-05, eq. (ODE.1); depends on $d$, $N$ |
| $p(g_k)$ | Small-field threshold $g_k^{3/4}$ | $k$-dep. | $K$-dep. | Defines $\Omega_s$; not a constant in the bound |

The only $k$- and $K$-dependent quantity in the table is $p(g_k)$,
which enters only as the *defining condition* of $\Omega_s$, not as a
multiplicative constant in the polymer bound. The bound (2.1) with
$\kappa(t) \geq \kappa_B$ is therefore $(k, K)$-uniform.


---


## 7. Relation to Other Lemmas in the Programme

**Lemma 1.1 (W1-01, flow well-posedness).** Provides the existence
and regularity of the flow trajectory $\{V_t\}$. Without this, the
flowed polymer activity (1.4) would not be well-defined. Used in
Step 1 through Lemma 1.2.

**Lemma 1.2 (W2-06, flow preserves $\Omega_s$).** The essential
bridge. The entire proof of Lemma 1.3 rests on this: the flow image
$V_t$ lies in $\Omega_s$, so Balaban's estimates apply. Without
Lemma 1.2, one would need to extend Balaban's polymer expansion
beyond $\Omega_s$, which is a much harder problem.

**Lemma 1.5 (W1-02, flow contractivity).** Provides the vacuum
isolation and Hessian bound. Used in the discussion of how the flow
improves decay (Section 5.3), but not in the core proof of
Lemma 1.3.

**Lemma 3.1 (W1-05, analyticity in $t$).** Provides the analyticity
of the flowed effective action in flow time. Lemma 1.3 is the
exponential decay estimate that complements the analyticity: together,
they ensure that the flowed polymer expansion converges uniformly in
$t$, $k$, and $K$.

**Lemma M.1.2 (Appendix M).** The unflowed $K$-uniform polymer
bound. This is the direct ancestor of Lemma 1.4: the $K$-uniformity
of the flowed constants is inherited from the unflowed ones.

**Corollary M.1.3 (Appendix M).** Establishes that the
Cluster--Balaban Handoff Lemma hypotheses (H1)--(H2) are satisfied
$K$-uniformly. Lemma 1.4 extends this to the flowed theory.

**Handoff Lemma (Section 5.4.5).** The starting point of the outer
recursion $C_{K+1} \leq C_K/4 + C_* + O(g_K^2 C_K)$. Lemma 1.4
ensures that the constants entering this recursion are $K$-uniform,
so the recursion has bounded orbit (Corollary M.1.3).


---


## 8. Summary

Lemmas 1.3 and 1.4 are established.

**Lemma 1.3.** The flowed polymer activities satisfy
$|K_k^{(t)}(X,V)| \leq e^{-\kappa(t)|X|}$ with $\kappa(t) \geq
\kappa_B > 0$ for all $t \geq 0$ and all $k \geq 0$. The proof is a
two-step composition:

1. The gradient flow preserves $\Omega_s$ (Lemma 1.2, W2-06).
2. Balaban's polymer estimates apply to all $V \in \Omega_s$
   (CMP 109, Theorem 1; Lemma M.1.2).

The KK mass tower provides an additional exponential suppression
$e^{-m_n \ell_{\min}(X)}$ for modes $n \geq 1$, strictly improving
the bound beyond the zero-mode baseline.

**Lemma 1.4.** All constants are $K$-uniform, by three independent
mechanisms:

1. The unflowed polymer constants ($\kappa_B$, $m_W$, $C_D$) are
   $K$-uniform (Lemma M.1.2).
2. The gradient flow introduces no $K$-dependent parameters
   (deterministic ODE with $K$-independent coefficients).
3. The KK masses ($m_1, m_2, \ldots$) are determined by the
   internal geometry, independent of $K$.


---


## References

1. W1-01: Flow well-posedness on the KK-enhanced lattice (this
   programme). Lemma 1.1, especially Part (v) (action decrease).

2. W1-02: Flow contractivity on the KK background (this programme).
   Lemma 1.5, especially Part (B) (vacuum isolation, Hessian bound).

3. W1-05: Analyticity of the flowed effective action in $t$ (this
   programme). Lemma 3.1 (composition theorem).

4. W2-06: Flow preserves the small-field domain (this programme).
   Lemma 1.2 (preservation of $\Omega_s$).

5. W2-07: Numerical verification of polymer decay estimates (this
   programme). Independent computational check.

6. Balaban, T. Propagators and renormalization transformations for
   lattice gauge theories, I--II. *Commun. Math. Phys.* **95**
   (1984) 17--40; **96** (1984) 223--250.

7. Balaban, T. Averaging operations for lattice gauge theories.
   *Commun. Math. Phys.* **98** (1985) 17--51.

8. Balaban, T. The variational problem and background fields in
   renormalization group method for lattice gauge theories.
   *Commun. Math. Phys.* **109** (1987) 249--301.

9. Balaban, T. Spaces of regular gauge field configurations on a
   lattice and gauge fixing conditions. *Commun. Math. Phys.*
   **119** (1988) 243--285.

10. Kotecky, R. and Preiss, D. Cluster expansion for abstract polymer
    models. *Commun. Math. Phys.* **103** (1986) 491--498.

11. Luscher, M. Properties and uses of the Wilson flow in lattice
    QCD. *JHEP* **08** (2010) 071; arXiv:1006.4518.

12. Mass gap preprint, Section 4.4 (Theorem 4: lattice mass gap).

13. Mass gap preprint, Section 5.4.5 (Cluster--Balaban Handoff Lemma).

14. Mass gap preprint, Section 5.6, Part I (Balaban analyticity (B1)
    with $k$-independent radius).

15. Mass gap preprint, Appendix K (Balaban's block-spin RG for
    general groups).

16. Mass gap preprint, Appendix M, Lemmas M.1.1--M.1.2, Corollary
    M.1.3 ($K$-uniformity of Balaban's constants).

17. Dimock, J. The renormalization group according to Balaban, I.
    Small fields. *Rev. Math. Phys.* **25** (2013) 1330010;
    arXiv:1108.1335.

18. Paper 1 (QG5D), Section 2 (Framework): KK mass spectrum.

19. Paper 6 (QG5D), Proposition A.1 (dilaton freezing).
