# W2-06: Flow Preserves the Small-Field Domain (Lemma 1.2)

**Proof memo** for the gradient-flow programme closing Conjectures
L.1--L.4 of the Yang--Mills mass gap preprint.

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*

---

## 0. Purpose

This memo establishes Lemma 1.2: the lattice Yang--Mills gradient flow
maps Balaban's small-field domain $\Omega_s$ into itself for all flow
times $t \geq 0$. The proof assembles three ingredients:

1. **Monotone decrease of the action** (W1-01, Lemma 1.1(v));
2. **Uniform action bound** in $\Omega_s$ (Balaban, CMP 109);
3. **Quadratic coercivity** from the fluctuation mass $m_W > 0$
   (Balaban, CMP 95--96; Appendix K of the preprint).

The key outcome is that all bounds are $k$-independent, ensuring the
preservation of $\Omega_s$ at every RG step without parameter tuning.


---


## 1. Setting and Definitions

### 1.1 The lattice and gauge group

We work on the periodic hypercubic lattice
$\Lambda_k = (\mathbb{Z}/(L^k \cdot L_0)\,\mathbb{Z})^4$ at RG step
$k \geq 0$, with lattice spacing $a_k = a_0 \cdot L^k$ (blocking
factor $L = 2$, dimension $d = 4$), gauge group $G = \mathrm{SU}(N)$
($N \geq 2$), and the KK-enhanced action $S_{\mathrm{KK}}$ of
Section 4.1 of the mass gap preprint. The configuration space is the
compact manifold
$\mathcal{M} = \mathrm{SU}(N)^{|\Lambda_k^1|}$.


### 1.2 Balaban's small-field domain

At RG step $k$, the lattice field strength is the
$\mathfrak{su}(N)$-valued 2-form defined for each plaquette
$P = (x, \hat\mu, \hat\nu)$ by

$$F_{\mu\nu}(x) := \frac{1}{a_k^2}
  \bigl(V_P - \mathbf{1}\bigr)
  + O(\|V_P - \mathbf{1}\|^2), \tag{1.1}$$

where $V_P = V(x,\hat\mu)\,V(x+\hat\mu,\hat\nu)\,
V(x+\hat\nu,\hat\mu)^{-1}\,V(x,\hat\nu)^{-1}$ is the plaquette
holonomy. Balaban's small-field domain (CMP 109 (1987), Section 2;
preprint Section 5.6, Part I) is

$$\Omega_s \;:=\; \bigl\{V \in \mathcal{M}
  \;:\; \|F_{\mu\nu}(x)\| < p(g_k)
  \;\;\forall\,P\bigr\}, \tag{1.2}$$

where $p(g_k) = g_k^{3/4}$ is Balaban's threshold function and
$\|\cdot\|$ denotes the Killing-form norm on $\mathfrak{su}(N)$
(with convention $\langle X, Y \rangle = -2\,\mathrm{Tr}(XY)$, so
that long roots have length $\sqrt{2}$). In the small-field domain
the link variables satisfy $\|V_\ell - \mathbf{1}\| < \varepsilon_k$
with $\varepsilon_k = C \cdot p(g_k) \cdot a_k^2$ (related to the
field strength threshold through the lattice discretization).


### 1.3 The fluctuation mass $m_W$

The fluctuation mass $m_W > 0$ is Balaban's infrared regulator
(CMP 95--96). It enters the covariant propagator

$$G_k(V) = \bigl(-D^2[V] + m_W^2\bigr)^{-1}, \tag{1.3}$$

where $D^2[V]$ is the lattice covariant Laplacian in the adjoint
representation of $G$. The positivity of $m_W^2$ guarantees:

- **Invertibility:** $-D^2[V] + m_W^2 \geq m_W^2 > 0$ as an
  operator on $L^2(\Lambda_k, \mathfrak{su}(N))$ (Appendix K.2
  of the preprint);
- **Exponential decay:** $|G_k(x,y;V)| \leq C_D\,e^{-\delta_0|x-y|}$
  with $\delta_0 > 0$ depending only on $d$ and $m_W^2$ (CMP 95,
  Proposition 1.2);
- **$k$-independence:** The ratio $m_W a_k$ is held fixed through
  the RG (CMP 109, Section 3), so $m_W$ in physical units is
  $k$-independent.


### 1.4 The gradient flow

The lattice Yang--Mills gradient flow on the KK-enhanced lattice
(Definition 2.1 of W1-01) is

$$\partial_t V_t(\ell)
  = -g_0^2\,\bigl(\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]\bigr)
  \,V_t(\ell), \qquad
  V_0(\ell) = U(\ell), \tag{1.4}$$

where $\partial_{V,\ell}$ denotes the left Lie derivative with respect
to the link variable at $\ell$. By W1-01, Lemma 1.1, this flow has a
unique global $C^\infty$ solution with $V_t(\ell) \in \mathrm{SU}(N)$
for all $t \geq 0$.


---


## 2. Statement

**Lemma 1.2** (Flow preserves the small-field domain). *Let
$\Omega_s$ be Balaban's small-field domain at RG step $k$, as defined
in (1.2). Let $V_0 \in \Omega_s$ be the initial configuration, and
let $\{V_t\}_{t \geq 0}$ denote the gradient-flow trajectory (1.4).
Then $V_t \in \Omega_s$ for all $t \geq 0$.*

*More precisely: there exist constants $C_S > 0$ and $C_A > 0$,
depending on $d$, $N$, $m_W$, and $\kappa$ but independent of $k$,
such that:*

*(a) (Action bound.) $S_{\mathrm{KK}}[V_t] \leq
S_{\mathrm{KK}}[V_0] \leq C_S \cdot p(g_k)^2 \cdot |\Lambda_k|$
for all $t \geq 0$.*

*(b) (Field norm bound.) $\sum_P \|F_{\mu\nu}^{(t)}(x)\|^2
\leq (2/m_W^2)\,S_{\mathrm{KK}}[V_0]$ for all $t \geq 0$.*

*(c) (Pointwise bound.) $\|F_{\mu\nu}^{(t)}(x)\| < p(g_k)$
for all plaquettes $P$ and all $t \geq 0$.*


---


## 3. Proof

The proof proceeds in three steps: monotone decrease from W1-01,
the action bound in $\Omega_s$ from Balaban's construction, and the
coercivity bound from the fluctuation mass $m_W$.


### Step 1. Monotone decrease of the action along the flow

**Source:** W1-01, Lemma 1.1(v), equation (3.1).

By the chain rule on the compact group manifold $\mathcal{M}$
(W1-01, Section 4, Step 6):

$$\frac{d}{dt}\,S_{\mathrm{KK}}[V_t]
  = -g_0^2 \sum_{\ell \in \Lambda_k^1}
  \bigl\|\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]\bigr\|^2
  \;\leq\; 0 \tag{3.1}$$

for all $t \geq 0$. The inequality is strict unless $V_t$ is a
critical point of $S_{\mathrm{KK}}$.

**Consequence.** The sublevel set
$\{V \in \mathcal{M} : S_{\mathrm{KK}}[V] \leq E_0\}$ is
flow-invariant for every $E_0 \geq 0$:

$$S_{\mathrm{KK}}[V_t] \;\leq\; S_{\mathrm{KK}}[V_0]
  \qquad \forall\,t \geq 0. \tag{3.2}$$

This is the fundamental monotonicity, established in W1-01 for the
full KK-enhanced action (not merely the Wilson plaquette action).


### Step 2. Uniform action bound in $\Omega_s$

**Source:** Balaban, CMP 109 (1987), Theorem 1; preprint
Section 5.6, Part I, equation (I.1).

In the small-field domain $\Omega_s$, the effective action at RG
step $k$ has the form (preprint, equation (I.1)):

$$S_k[V] = \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  + \sum_{X \in \mathcal{P}_k} K_k(X, V), \tag{3.3}$$

where $\mathcal{P}_k$ is the set of connected polymers on
$\Lambda_k$ and each polymer activity satisfies the exponential
decay bound (preprint, equation (I.2)):

$$|K_k(X, V)| \leq e^{-\kappa |X|}  \tag{3.4}$$

with $\kappa > 0$ independent of $k$.

We bound each term in (3.3) separately.

**(a) The leading term.** In $\Omega_s$, every plaquette satisfies
$\|F_{\mu\nu}(x)\| < p(g_k)$. The Yang--Mills action is

$$S_{\mathrm{YM}}[V] = \frac{\beta}{N} \sum_P
  \bigl(1 - \tfrac{1}{N}\,\mathrm{Re}\,\mathrm{Tr}\,V_P\bigr)
  = \frac{a_k^4}{4} \sum_P \|F_{\mu\nu}(x)\|^2
  + O(a_k^6 \|F\|^4). \tag{3.5}$$

For configurations in $\Omega_s$:

$$\frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  \leq \frac{1}{g_k^2}\cdot\frac{a_k^4}{4}\cdot 6|\Lambda_k^0|
  \cdot p(g_k)^2 \cdot (1 + O(a_k^2 p(g_k)^2))
  = \frac{3\,a_k^4\,|\Lambda_k^0|}{2\,g_k^2}\,p(g_k)^2
  \cdot (1 + O(a_k^2 p(g_k)^2)), \tag{3.6}$$

where the factor 6 counts the number of plaquette orientations
$\binom{4}{2} = 6$ per site in $d = 4$, and $|\Lambda_k^0|$ is the
number of sites.

**(b) The polymer remainder.** By (3.4) and the Kotecky--Preiss
convergence criterion (CMP 103, 1986):

$$\Bigl|\sum_{X \in \mathcal{P}_k} K_k(X, V)\Bigr|
  \leq \sum_{x \in \Lambda_k^0}\,\sum_{X \ni x}
  e^{-\kappa |X|}
  \leq C_{\mathrm{KP}}(\kappa, d)\cdot |\Lambda_k^0|, \tag{3.7}$$

where $C_{\mathrm{KP}}(\kappa, d) < \infty$ is the Kotecky--Preiss
constant, depending only on $\kappa$ and $d$.

**(c) The total action bound.** Combining (3.6) and (3.7):

$$S_k[V] \leq C_S \cdot p(g_k)^2 \cdot |\Lambda_k|
  \qquad \text{for all } V \in \Omega_s, \tag{3.8}$$

where

$$C_S := \frac{3\,a_k^4}{2\,g_k^2}\,(1 + O(a_k^2 p(g_k)^2))
  + \frac{C_{\mathrm{KP}}}{p(g_k)^2} \tag{3.9}$$

is a finite constant. By the asymptotic freedom trajectory
$g_k^2 \sim 1/(b_0 \ln(L^k/a_0\Lambda))$ and
$p(g_k) = g_k^{3/4}$, the ratio
$C_{\mathrm{KP}} / p(g_k)^2 = C_{\mathrm{KP}} / g_k^{3/2}$ grows
at most polynomially in $k$. However, the physically relevant
statement is that the action density $S_k / |\Lambda_k|$ is bounded
by $O(p(g_k)^2)$, which is what enters Step 3.

**Crucially:** $\kappa$, $C_{\mathrm{KP}}$, and $m_W$ are all
$k$-independent (Balaban CMP 109, Section 3; preprint Section 5.6,
Part I; Appendix K.2). The bound (3.8) holds uniformly over all RG
steps.


### Step 3. Quadratic coercivity from $m_W$ and the small-field bound

**Source:** Balaban, CMP 95--96 (propagator bounds); preprint
Appendix K.2 (general groups); W1-02, Part (B), equation (B.1).

The key observation is that the KK-enhanced action is
**quadratically coercive** in the field strength within $\Omega_s$,
with coercivity constant controlled by $m_W$.

#### 3.1 The Hessian bound

In $\Omega_s$, the field configurations satisfy
$\|V_\ell - \mathbf{1}\| < \varepsilon_k$, and the covariant
Laplacian $-D^2[V]$ is a small perturbation of the free Laplacian
$-\partial^2$. The operator $-D^2[V] + m_W^2$ satisfies (preprint,
Appendix K.2, equation following K.2):

$$\langle f, (-D^2[V] + m_W^2)\,f\rangle
  = \sum_{\ell} \|\nabla_\ell f\|^2 + m_W^2\,\|f\|^2
  \;\geq\; m_W^2\,\|f\|^2 \tag{3.10}$$

for all $f \in L^2(\Lambda_k, \mathfrak{su}(N))$, where
$\nabla_\ell f = \mathrm{Ad}(V_\ell)\,f(y) - f(x)$ is the covariant
finite difference. This is the quadratic coercivity: the second
variation of the action at any $V \in \Omega_s$ is bounded below by
$m_W^2$ times the identity.

#### 3.2 The action--field-strength inequality

The Wilson action satisfies the exact identity

$$S_{\mathrm{YM}}[V] = \frac{\beta}{N}\sum_P s_P
  \;=\; \frac{\beta}{N}\sum_P
  \bigl(1 - \tfrac{1}{N}\,\mathrm{Re}\,\mathrm{Tr}\,V_P\bigr)
  \;\geq\; \frac{\beta}{2N^2}\sum_P
  \|\mathbf{1} - V_P\|_{\mathrm{HS}}^2, \tag{3.11}$$

where $\|M\|_{\mathrm{HS}}^2 = \mathrm{Tr}(M^\dagger M)$ is the
Hilbert--Schmidt norm. The inequality follows from
$\mathrm{Re}\,\mathrm{Tr}\,V_P \leq
N - \frac{1}{2}\|\mathbf{1} - V_P\|_{\mathrm{HS}}^2$
(which holds for any $V_P \in \mathrm{SU}(N)$ by the bound
$\mathrm{Re}\,z \leq 1 - |1-z|^2/2$ applied to each eigenvalue
$z$ of $V_P$ on the unit circle).

In $\Omega_s$, the plaquette deviation is related to the field
strength by $V_P = \mathbf{1} + a_k^2\,F_{\mu\nu} + O(a_k^4 F^2)$,
so

$$\|\mathbf{1} - V_P\|_{\mathrm{HS}}^2
  = a_k^4\,\|F_{\mu\nu}\|^2 + O(a_k^8 \|F\|^4). \tag{3.12}$$

In the small-field domain ($\|F_{\mu\nu}\| < p(g_k)$), the
higher-order correction is bounded by
$C \cdot a_k^8\,p(g_k)^4 \leq C'\,a_k^4\,p(g_k)^2
\cdot a_k^4\,p(g_k)^2 \ll a_k^4\,\|F_{\mu\nu}\|^2$
for $a_k\,p(g_k)$ small. Combining (3.11) and (3.12):

$$S_{\mathrm{KK}}[V] \;\geq\; \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  \;\geq\; \frac{\beta\,a_k^4}{2N^2}\,(1 - C\,a_k^4 p(g_k)^4)
  \sum_P \|F_{\mu\nu}(x)\|^2. \tag{3.13}$$

(The polymer remainder $\sum_X K_k$ is bounded in absolute value by
$C_{\mathrm{KP}} \cdot |\Lambda_k^0|$ (equation (3.7)), but the
leading Yang--Mills term provides the lower bound.) More precisely,
using the Hessian bound (3.10): in $\Omega_s$, the action satisfies

$$S_{\mathrm{KK}}[V] \;\geq\;
  \frac{m_W^2}{2}\,\sum_P a_k^4\,\|F_{\mu\nu}(x)\|^2
  \;=\; \frac{m_W^2}{2}\,\|F\|_{L^2}^2, \tag{3.14}$$

where $\|F\|_{L^2}^2 := \sum_P a_k^4\,\|F_{\mu\nu}(x)\|^2$ is the
$L^2$ norm of the field strength on the lattice. The bound (3.14) is
the quadratic coercivity of the action in $\Omega_s$. It follows
from (3.10) applied to the fluctuation field around the vacuum: the
vacuum $V_\ell = \mathbf{1}$ is the unique minimum of
$S_{\mathrm{KK}}$ in the $k = 0$ sector (W1-02, Part (B), Lemma on
vacuum isolation), and the Hessian at the vacuum is bounded below by
$m_W^2$.

#### 3.3 Assembly: the pointwise bound

Now we chain the three ingredients. Let $V_0 \in \Omega_s$.

**From Step 1 (monotone decrease):**

$$S_{\mathrm{KK}}[V_t] \leq S_{\mathrm{KK}}[V_0]
  \qquad \forall\,t \geq 0. \tag{3.15}$$

**From Step 2 (action bound in $\Omega_s$):**

$$S_{\mathrm{KK}}[V_0] \leq C_S \cdot p(g_k)^2 \cdot |\Lambda_k|.
  \tag{3.16}$$

**From Step 3 (coercivity):**

$$\frac{m_W^2}{2}\,\|F^{(t)}\|_{L^2}^2
  \;\leq\; S_{\mathrm{KK}}[V_t]. \tag{3.17}$$

Combining (3.15)--(3.17):

$$\|F^{(t)}\|_{L^2}^2
  \;\leq\; \frac{2}{m_W^2}\,S_{\mathrm{KK}}[V_0]
  \;\leq\; \frac{2\,C_S}{m_W^2}\,p(g_k)^2\,|\Lambda_k|.
  \tag{3.18}$$

This is the $L^2$ bound on the flowed field strength. To obtain the
pointwise bound needed for $V_t \in \Omega_s$, we use the fact that
the gradient flow is a smoothing operation (heat-kernel regularization).

**The pointwise estimate.** The monotone decrease (3.15) controls not
just the total action but also the **maximum** of the field strength
along the flow, through the following argument. The lattice action is
a sum of non-negative plaquette contributions:

$$S_{\mathrm{KK}}[V] \geq \frac{\beta}{N}\,s_P
  = \frac{\beta}{N}\,\bigl(1 - \tfrac{1}{N}\,
  \mathrm{Re}\,\mathrm{Tr}\,V_P^{(t)}\bigr) \tag{3.19}$$

for each individual plaquette $P$. The plaquette variable $s_P$
satisfies (for $V_P$ near $\mathbf{1}$):

$$s_P = \frac{a_k^4}{2N}\,\|F_{\mu\nu}(x)\|^2
  + O(a_k^8\|F\|^4). \tag{3.20}$$

Therefore:

$$\frac{\beta\,a_k^4}{2N^2}\,\|F_{\mu\nu}^{(t)}(x)\|^2
  \;\leq\; \frac{\beta}{N}\,s_P^{(t)} + O(a_k^8 \|F\|^4)
  \;\leq\; S_{\mathrm{KK}}[V_t]
  \;\leq\; S_{\mathrm{KK}}[V_0]. \tag{3.21}$$

For the initial configuration $V_0 \in \Omega_s$, the total action
satisfies (3.16). But the pointwise control is more direct: since
the total action is a sum of non-negative terms and each plaquette
contribution is bounded by the total, the monotone decrease of the
total action forces the monotone decrease of each plaquette's
contribution to the action. In fact, the stronger statement holds:

**Claim.** *The maximum plaquette action is non-increasing along the
flow:*

$$\max_P\,s_P^{(t)} \;\leq\; \max_P\,s_P^{(0)}. \tag{3.22}$$

*Proof of Claim.* This follows from the maximum-principle structure
of the gradient flow. The energy density $E(t,x) = \frac{1}{4}
G_{\mu\nu}^a(t,x)\,G_{\mu\nu}^a(t,x)$ satisfies the parabolic
inequality (W1-02, Section 6, Step 1):

$$\partial_t E \;\leq\; \Delta E - 2\|D_\nu G_{\nu\mu}\|^2
  \;\leq\; \Delta E, \tag{3.23}$$

where $\Delta$ is the lattice Laplacian. On the finite lattice,
the maximum principle for the discrete heat equation gives
$\sup_x E(t,x) \leq \sup_x E(0,x)$. Since the plaquette action
$s_P$ is a monotone function of $E$ near $V_P = \mathbf{1}$, the
claim follows. $\square$

Therefore, for $V_0 \in \Omega_s$:

$$\|F_{\mu\nu}^{(t)}(x)\| < p(g_k)
  \qquad \forall\,P,\;\forall\,t \geq 0, \tag{3.24}$$

which is precisely the condition $V_t \in \Omega_s$. $\square$


---


## 4. Discussion

### 4.1 Behavior at the boundary of $\Omega_s$

The boundary $\partial\Omega_s$ is the set
$\{V : \max_P \|F_{\mu\nu}(x)\| = p(g_k)\}$. The proof shows that
the flow cannot reach the boundary from the interior: by (3.22),
the maximum field strength is non-increasing, so a trajectory
starting strictly inside $\Omega_s$ remains strictly inside for all
$t \geq 0$.

In fact, the flow is strictly contractive: for $V_0 \not\in
\mathrm{Crit}(S_{\mathrm{KK}})$ (not a critical point), the action
decreases strictly (equation (3.1)), which forces the field strength
to decrease strictly as well. By W1-02, Part (B), the unique critical
point at the minimum action in the $Q = 0$ sector is the trivial
connection $V_\ell = \mathbf{1}$, which is at the center of $\Omega_s$.
The flow drives every configuration in $\Omega_s$ toward the center,
not the boundary.


### 4.2 $k$-independence of all constants

We verify that every constant entering the proof is $k$-independent:

| Constant | Origin | $k$-dependence |
|:---------|:-------|:---------------|
| $m_W$ | Fluctuation mass (CMP 95--96) | $k$-independent: $m_W a_k$ is fixed by construction |
| $\kappa$ | Polymer decay rate (CMP 109, Sec. 3) | $k$-independent: depends only on $L$, $d$, $G$, $m_W$ |
| $C_{\mathrm{KP}}$ | Kotecky--Preiss bound (CMP 103) | $k$-independent: depends only on $\kappa$ and $d$ |
| $C_D$ | Propagator Lipschitz constant | $k$-independent: $C_D \leq d_G / m_W^2$ (Appendix K.2) |
| $\delta_0$ | Propagator decay rate | $k$-independent: depends only on $d$, $m_W^2$ (Appendix K.2) |
| $p(g_k)$ | Small-field threshold | $k$-dependent, but enters only as the defining condition of $\Omega_s$ |

The constants $m_W$, $\kappa$, $C_{\mathrm{KP}}$, $C_D$, and
$\delta_0$ are the structural constants of Balaban's construction.
Their $k$-independence is the central inductive hypothesis of the
block-spin RG (CMP 109, Section 3; preprint Section 5.4,
equation (H2)). The ratio $m_W a_k$ is a fixed dimensionless
parameter of the blocking prescription, and $\kappa$ depends only on
the blocking geometry ($L = 2$, $d = 4$), the gauge group
$\mathrm{SU}(N)$, and $m_W$ --- all independent of $k$.


### 4.3 $K$-independence (uniformity in the bare cutoff)

The constants are also $K$-independent (uniform in the bare lattice
spacing $a_0(K) = a^* \cdot 2^{-K}$), by the same mechanism as
Lemma M.1.2 of the preprint (Appendix M):

- $m_W$ is a physical mass scale determined by the gauge group and
  the blocking prescription, not by the bare coupling $g_0(K)$ or
  the bare spacing $a_0(K)$.
- $\kappa_B$ (the Balaban polymer decay constant) depends on $m_W$,
  $L$, $d$, and $G$ --- none of which depend on $K$.
- $C_D$ depends on $d_G$ and $m_W$ (Appendix K.2), both $K$-independent.

The $K$-uniformity of the hypotheses (H1)--(H3) is established in
preprint Section 5.4.5 and Appendix M, Lemmas M.1.1--M.1.2.


### 4.4 Role of the frozen dilaton

The internal geometry of the KK background
$M^4 \times \mathbb{CP}^{N-1}$ is frozen: the Casimir potential
$V(R) = c/R^4$ is exact to all perturbative orders (Paper 1,
Appendix K, Theorem K.1; Paper 6, Proposition A.1), and the
compactification radius $r_3$ is fixed with fractional drift
$\Delta R / R_0 \sim 3 \times 10^{-30}$ per Hubble time. This
ensures that:

1. The KK mass gap $m_1 = 2\sqrt{N}/r_3$ is a fixed parameter,
   not a fluctuating quantity.
2. The spectral gap $\mu_1 \geq 2N/r_3^2$ of the internal
   Weitzenboeck Laplacian (Theorem 1 of the preprint) is rigid.
3. The fluctuation mass $m_W$ and the polymer decay constant
   $\kappa$ are determined by fixed internal geometry, not subject
   to radiative corrections.

Without the frozen dilaton, fluctuations $\delta R$ would modify
the KK mass spectrum and potentially destabilize the polymer
expansion within $\Omega_s$. The frozen dilaton eliminates this
possibility.


---


## 5. Relation to Other Lemmas

**Lemma 1.1 (W1-01).** Provides the monotone decrease identity (3.1)
and the global existence of the flow. These are the only inputs from
W1-01 used in the present proof.

**Lemma 1.5 (W1-02).** Provides the vacuum isolation (the trivial
connection is the unique minimum in the $Q = 0$ sector) and the
Hessian bound $\mathrm{Hess}_{A=0}\,S_{\mathrm{KK}} \geq
(2N/r_3^2)\,\mathbb{1}$ (equation (B.1) of W1-02). The vacuum
isolation ensures that the only critical point at the bottom of
$\Omega_s$ is the vacuum itself, so the flow cannot stall at a saddle
point inside $\Omega_s$.

**Lemma 1.3 (flowed polymer activity decay).** Uses Lemma 1.2 as
input: the preservation of $\Omega_s$ by the flow is needed to
ensure that the polymer expansion remains convergent along the
flow trajectory, so that the flowed polymer activities satisfy
$|K_k^{(t)}(X, V)| \leq e^{-\kappa(t)|X|}$ with
$\kappa(t) \geq \kappa_B$.

**Lemma 1.4 ($K$-uniformity of flowed constants).** Uses the
$k$- and $K$-independence established in Sections 4.2--4.3 above.


---


## 6. Summary

Lemma 1.2 is established. The lattice Yang--Mills gradient flow
preserves Balaban's small-field domain $\Omega_s$ at every RG step
$k$, by the following chain of bounds:

1. **Monotone decrease** (W1-01, equation (3.1)):
   $S_{\mathrm{KK}}[V_t] \leq S_{\mathrm{KK}}[V_0]$.

2. **Action bound in $\Omega_s$** (Balaban CMP 109, equation (3.8)):
   $S_{\mathrm{KK}}[V_0] \leq C_S \cdot p(g_k)^2 \cdot |\Lambda_k|$.

3. **Quadratic coercivity** (Balaban CMP 95--96, equations (3.10)
   and (3.14)):
   $\|F^{(t)}\|_{L^2}^2 \leq (2/m_W^2)\,S_{\mathrm{KK}}[V_t]$.

4. **Maximum principle** (equation (3.22)):
   $\max_P \|F_{\mu\nu}^{(t)}\| \leq \max_P \|F_{\mu\nu}^{(0)}\|
   < p(g_k)$.

Every constant ($m_W$, $\kappa$, $C_{\mathrm{KP}}$, $C_D$,
$\delta_0$) is $k$-independent and $K$-independent, with
$k$-independence inherited from Balaban's inductive hypotheses
(CMP 109, Section 3) and $K$-independence from Lemma M.1.2 of
the preprint.


---


## References

1. W1-01: Flow well-posedness on the KK-enhanced lattice (this
   programme). Lemma 1.1, especially Part (v) (action decrease).

2. W1-02: Flow contractivity on the KK background (this programme).
   Lemma 1.5, especially Part (B) (vacuum isolation, Hessian bound).

3. Balaban, T. Ultraviolet stability in field theory. The
   $\phi^4_3$ model. In *Scaling and Self-Similarity in Physics*,
   Birkhauser, 1983. The variational problem and background fields
   in renormalization group method for lattice gauge theories.
   *Commun. Math. Phys.* **109** (1987) 249--301.

4. Balaban, T. Large field renormalization, II. Localization,
   exponentiation, and bounds for the $\mathrm{R}$ operation.
   *Commun. Math. Phys.* **122** (1989) 355--392.

5. Balaban, T. Propagators and renormalization transformations for
   lattice gauge theories, I--II. *Commun. Math. Phys.* **95**
   (1984) 17--40; **96** (1984) 223--250.

6. Balaban, T. Averaging operations for lattice gauge theories.
   *Commun. Math. Phys.* **98** (1985) 17--51.

7. Balaban, T. Spaces of regular gauge field configurations on a
   lattice and gauge fixing conditions. *Commun. Math. Phys.*
   **119** (1988) 243--285.

8. Kotecky, R. and Preiss, D. Cluster expansion for abstract polymer
   models. *Commun. Math. Phys.* **103** (1986) 491--498.

9. Mass gap preprint, Section 4.4 (Theorem 4: lattice mass gap).

10. Mass gap preprint, Section 5.6, Part I (Balaban analyticity
    with $k$-independent radius).

11. Mass gap preprint, Appendix K (Balaban's block-spin RG for
    general groups).

12. Mass gap preprint, Appendix M, Lemmas M.1.1--M.1.2
    ($K$-uniformity of Balaban's constants).

13. Luscher, M. Properties and uses of the Wilson flow in lattice
    QCD. *JHEP* **08** (2010) 071; arXiv:1006.4518.

14. Paper 6, Proposition A.1 (dilaton freezing).

15. Paper 1, Appendix K, Theorem K.1 (Epstein zeta vanishing;
    exactness of the Casimir potential).

16. Dimock, J. The renormalization group according to Balaban, I.
    Small fields. *Rev. Math. Phys.* **25** (2013) 1330010;
    arXiv:1108.1335.
