# L.1 Phase 1: Lattice Gradient Flow in the KK-Balaban Framework

This section establishes the five foundational lemmas (Lemmas L.1.1
through L.1.5) for the lattice Yang--Mills gradient flow on the
KK-enhanced lattice. The flow is a finite-dimensional ODE on the
compact configuration manifold $\mathcal{M} =
\mathrm{SU}(N)^{|\Lambda_k^1|}$; the results below confirm that it
is globally well-posed, preserves Balaban's small-field domain
$\Omega_s$, and yields flowed polymer activities with $K$-uniform
exponential decay.

**Notation.** We work on the periodic hypercubic lattice
$\Lambda_k = (\mathbb{Z}/(L^k L_0)\mathbb{Z})^4$ at RG step
$k \geq 0$ with lattice spacing $a_k = a_0 \cdot L^k$
(blocking factor $L = 2$, dimension $d = 4$), gauge group
$G = \mathrm{SU}(N)$ ($N \geq 2$), and the KK-enhanced action
$S_{\mathrm{KK}}$ of Section 4.1. The Lie algebra $\mathfrak{su}(N)$
carries the inner product
$\langle X, Y \rangle = -2\,\mathrm{Tr}(XY)$, normalised so that long
roots have length $\sqrt{2}$. The inverse bare coupling is
$\beta = 2N/g_0^2$. The link variables
$V(\ell) \in \mathrm{SU}(N)$ for oriented links
$\ell \in \Lambda_k^1$ are the dynamical degrees of freedom; the
internal connections on $\mathbb{CP}^{N-1}$ are held fixed at their
KK-reduced values throughout the flow.


---


## The gradient flow equation

For a smooth function $S : \mathcal{M} \to \mathbb{R}$ and a link
$\ell \in \Lambda_k^1$, the left Lie derivative with respect to the
link variable $V(\ell)$ is the $\mathfrak{su}(N)$-valued quantity

$$\partial_{V,\ell}\,S \;:=\; \sum_{a=1}^{N^2-1}
  \left.\frac{d}{ds}\right|_{s=0}
  S\bigl[\ldots, e^{sT^a}V(\ell), \ldots\bigr]\,T^a
  \;\in\; \mathfrak{su}(N), \tag{L.1.1}$$

where $\{T^a\}$ is an orthonormal basis of $\mathfrak{su}(N)$.
The lattice Yang--Mills gradient flow is the system of ODEs

$$\partial_t V_t(\ell)
  = -g_0^2\,\bigl(\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]\bigr)
  \,V_t(\ell), \qquad
  V_0(\ell) = U(\ell), \tag{L.1.2}$$

for each oriented link $\ell \in \Lambda_k^1$ and flow time
$t \geq 0$. This is the negative gradient flow of $S_{\mathrm{KK}}$
with respect to the bi-invariant Riemannian metric on $\mathcal{M}$,
scaled by $g_0^2$. The right-hand side defines a smooth vector field
$\mathcal{X} : \mathcal{M} \to T\mathcal{M}$, and (L.1.2) reads
$\dot\gamma(t) = \mathcal{X}(\gamma(t))$ for the curve
$\gamma(t) = V_t \in \mathcal{M}$.


---


## Lemma L.1.1 (Flow well-posedness)

*Let $\Lambda_k$ be a finite periodic lattice, $G = \mathrm{SU}(N)$
with $N \geq 2$, and $S_{\mathrm{KK}} : \mathcal{M} \to \mathbb{R}$
the KK-enhanced lattice action of Section 4.1, with any choice of
parameters $(\beta, r_3, a, L)$. Then:*

*(i) (Global existence and uniqueness.) For every initial
configuration $U \in \mathcal{M}$, the gradient flow equation (L.1.2)
has a unique solution $V_t \in \mathcal{M}$ defined for all
$t \in [0, \infty)$.*

*(ii) (Smoothness in flow time.) The map $t \mapsto V_t(\ell)$ is
$C^\infty$ on $[0, \infty)$ for each link $\ell$.*

*(iii) (Smooth dependence on initial data.) The map $U \mapsto V_t$
is $C^\infty$ as a map $\mathcal{M} \to \mathcal{M}$ for each fixed
$t \geq 0$.*

*(iv) (Group-valued.) $V_t(\ell) \in \mathrm{SU}(N)$ for all
$t \geq 0$ and all $\ell$.*

*(v) (Action decrease.)*

$$\frac{d}{dt}\,S_{\mathrm{KK}}[V_t]
  = -g_0^2 \sum_{\ell \in \Lambda_k^1}
  \bigl\|\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]\bigr\|^2
  \;\leq\; 0. \tag{L.1.3}$$

*(vi) (Gauge covariance.) If $\Omega = \{g(x)\}_{x \in \Lambda_k^0}$
is a gauge transformation with $g(x) \in \mathrm{SU}(N)$, and $V_t$
solves (L.1.2) with initial data $U$, then
$V_t^\Omega(\ell) := g(x)\,V_t(\ell)\,g(y)^{-1}$ (where
$\ell = (x, \hat\mu)$, $y = x + \hat\mu$) solves (L.1.2) with initial
data $U^\Omega$.*


**Proof.** The argument assembles three standard ingredients from
the theory of ODEs on compact manifolds.

*Smoothness of the vector field.* The Wilson plaquette action
$S_{\mathrm{4D}}[V] = \beta\sum_P(1 - N^{-1}
\mathrm{Re}\,\mathrm{Tr}\,V_P)$ is polynomial in the matrix entries
of the link variables, hence $C^\infty$ on $\mathcal{M}$. Each KK
coupling term involves the adjoint action
$V \mapsto V^{-1}XV$ and trace operations, all of which are smooth
(indeed real-analytic) on $\mathrm{SU}(N)$. The KK mode sum converges
uniformly in the $C^\infty$ topology on $\mathcal{M}$ by the
exponential suppression from KK masses $m_n \to \infty$. Therefore the
vector field $\mathcal{X}$ defined by (L.1.2) is $C^\infty$ on
$\mathcal{M}$.

*Compactness of $\mathcal{M}$.* The group $\mathrm{SU}(N)$ is compact,
so $\mathcal{M} = \mathrm{SU}(N)^{|\Lambda_k^1|}$ is compact as a
finite product of compact spaces.

*Global existence (i), (iv).* By Picard--Lindel\"of on manifolds, the
$C^\infty$ vector field $\mathcal{X}$ admits a unique maximal integral
curve $\gamma : [0, T_{\max}) \to \mathcal{M}$ through any initial
point. If $T_{\max} < \infty$, compactness of $\mathcal{M}$ provides a
convergent subsequence $\gamma(t_n) \to q \in \mathcal{M}$ as
$t_n \nearrow T_{\max}$, and local existence at $q$ extends the
solution beyond $T_{\max}$, contradicting maximality. Hence
$T_{\max} = \infty$. Since $\mathcal{M} \subset
\mathrm{SU}(N)^{|\Lambda_k^1|}$, the solution remains group-valued for
all $t$.

*Smoothness (ii), (iii).* Since $\mathcal{X}$ is $C^\infty$,
bootstrapping via $\dot\gamma = \mathcal{X}(\gamma)$ yields $C^\infty$
regularity in $t$. The standard smooth-dependence-on-parameters theorem
for ODEs gives $C^\infty$ dependence of the flow map
$(t, U) \mapsto V_t$ jointly.

*Action decrease (v).* By the chain rule on the group manifold,

$$\frac{d}{dt}\,S_{\mathrm{KK}}[V_t]
  = \sum_\ell \bigl\langle \partial_{V,\ell}\,S_{\mathrm{KK}}[V_t],\;
  V_t(\ell)^{-1}\,\dot V_t(\ell)\bigr\rangle.$$

The flow equation gives
$V_t(\ell)^{-1}\dot V_t(\ell) =
-g_0^2\,\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]$, so

$$\frac{d}{dt}\,S_{\mathrm{KK}}[V_t]
  = -g_0^2\sum_\ell
  \bigl\|\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]\bigr\|^2
  \;\leq\; 0,$$

with equality if and only if $V_t$ is a critical point.

*Gauge covariance (vi).* The KK-enhanced action is gauge-invariant:
$S_{\mathrm{KK}}[V^\Omega] = S_{\mathrm{KK}}[V]$. The left Lie
derivative transforms in the adjoint representation:

$$\partial_{V^\Omega,\ell}\,S_{\mathrm{KK}}[V^\Omega]
  = g(x)\,\bigl(\partial_{V,\ell}\,S_{\mathrm{KK}}[V]\bigr)\,
  g(x)^{-1}. \tag{L.1.4}$$

To verify (L.1.4), write
$e^{sT^a}g(x) = g(x)\,e^{s\,\mathrm{Ad}_{g(x)^{-1}}(T^a)}$ and
use gauge invariance to absorb the gauge transformation. Define
$W_t(\ell) := g(x)\,V_t(\ell)\,g(y)^{-1}$. Then
$W_0 = U^\Omega$, and

$$\dot W_t(\ell) = g(x)\,\dot V_t(\ell)\,g(y)^{-1}
  = -g_0^2\,g(x)\,(\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t])\,
  g(x)^{-1}\cdot g(x)\,V_t(\ell)\,g(y)^{-1}
  = -g_0^2\,(\partial_{W,\ell}\,S_{\mathrm{KK}}[W_t])\,W_t(\ell),$$

using (L.1.4). By uniqueness (part (i)), $W_t$ is the unique flow with
initial data $U^\Omega$. $\square$


---


## Lemma L.1.2 (Flow preserves the small-field domain)

*Let $\Omega_s := \{V \in \mathcal{M} : \|F_{\mu\nu}(x)\| <
p(g_k)\;\;\forall\,P\}$ be Balaban's small-field domain at RG step
$k$, where $p(g_k) = g_k^{3/4}$ is the threshold function and
$F_{\mu\nu}(x)$ is the lattice field strength at plaquette $P$. Let
$V_0 \in \Omega_s$, and let $\{V_t\}_{t \geq 0}$ denote the
gradient-flow trajectory (L.1.2). Then $V_t \in \Omega_s$ for all
$t \geq 0$.*

*More precisely, there exist constants $C_S, C_A > 0$ depending on
$d$, $N$, $m_W$, and $\kappa$ but independent of $k$, such that:*

*(a) (Action bound.) $S_{\mathrm{KK}}[V_t] \leq
S_{\mathrm{KK}}[V_0] \leq C_S \cdot p(g_k)^2 \cdot |\Lambda_k|$
for all $t \geq 0$.*

*(b) (Field norm bound.)
$\|F^{(t)}\|_{L^2}^2 \leq (2/m_W^2)\,S_{\mathrm{KK}}[V_0]$
for all $t \geq 0$.*

*(c) (Pointwise bound.) $\|F_{\mu\nu}^{(t)}(x)\| < p(g_k)$
for all plaquettes $P$ and all $t \geq 0$.*


**Proof.** The proof chains three ingredients: monotone decrease of
the action (Lemma L.1.1(v)), the uniform action bound in $\Omega_s$
from Balaban's construction, and the quadratic coercivity from the
fluctuation mass $m_W > 0$.

*Step 1: Monotone decrease.* By Lemma L.1.1(v), the action is
non-increasing along the flow:

$$S_{\mathrm{KK}}[V_t] \leq S_{\mathrm{KK}}[V_0]
  \qquad \forall\,t \geq 0. \tag{L.1.5}$$

Every sublevel set $\{V : S_{\mathrm{KK}}[V] \leq E_0\}$ is therefore
flow-invariant.

*Step 2: Action bound in $\Omega_s$.* In the small-field domain, the
effective action at RG step $k$ has the form (Section 5.6, Part I):

$$S_k[V] = \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  + \sum_{X \in \mathcal{P}_k} K_k(X, V), \tag{L.1.6}$$

where each polymer activity satisfies
$|K_k(X,V)| \leq e^{-\kappa|X|}$ with $\kappa > 0$ independent of $k$
(Appendix K, Balaban CMP 109). The Yang--Mills term is bounded by
$\frac{3\,a_k^4\,|\Lambda_k^0|}{2\,g_k^2}\,p(g_k)^2\,(1 +
O(a_k^2 p(g_k)^2))$ using $\|F_{\mu\nu}\| < p(g_k)$ and the six
plaquette orientations per site. The polymer remainder is bounded by
$C_{\mathrm{KP}}(\kappa,d) \cdot |\Lambda_k^0|$ via the
Koteck\'y--Preiss convergence criterion (CMP 103). Combining:

$$S_k[V] \leq C_S \cdot p(g_k)^2 \cdot |\Lambda_k|
  \qquad \text{for all } V \in \Omega_s, \tag{L.1.7}$$

with $C_S$ depending on $d$, $N$, $m_W$, $\kappa$ but not on $k$.
Together with (L.1.5), this establishes part (a).

*Step 3: Quadratic coercivity.* The operator
$-D^2[V] + m_W^2$ on $L^2(\Lambda_k, \mathfrak{su}(N))$ satisfies
$\langle f, (-D^2[V] + m_W^2)f\rangle \geq m_W^2\,\|f\|^2$
(Appendix K, \S K.2). This coercivity yields the
action--field-strength inequality: for $V \in \Omega_s$,

$$S_{\mathrm{KK}}[V] \;\geq\;
  \frac{m_W^2}{2}\,\|F\|_{L^2}^2, \tag{L.1.8}$$

where $\|F\|_{L^2}^2 := \sum_P a_k^4\,\|F_{\mu\nu}(x)\|^2$.
Combining (L.1.5), (L.1.7), and (L.1.8):

$$\|F^{(t)}\|_{L^2}^2
  \;\leq\; \frac{2}{m_W^2}\,S_{\mathrm{KK}}[V_0]
  \;\leq\; \frac{2\,C_S}{m_W^2}\,p(g_k)^2\,|\Lambda_k|, \tag{L.1.9}$$

establishing part (b).

*Step 4: Pointwise bound via maximum principle.* The energy density
$E(t,x) := \frac{1}{4}G_{\mu\nu}^a(t,x)\,G_{\mu\nu}^a(t,x)$
satisfies the parabolic inequality

$$\partial_t E \;\leq\; \Delta E - 2\|D_\nu G_{\nu\mu}\|^2
  \;\leq\; \Delta E, \tag{L.1.10}$$

where $\Delta$ is the lattice Laplacian. The maximum principle for
the discrete heat equation on the finite lattice gives
$\sup_x E(t,x) \leq \sup_x E(0,x)$. Since the plaquette action
$s_P$ is a monotone function of $E$ near $V_P = \mathbf{1}$, we
obtain

$$\max_P\,\|F_{\mu\nu}^{(t)}(x)\| \;\leq\;
  \max_P\,\|F_{\mu\nu}^{(0)}(x)\| \;<\; p(g_k) \tag{L.1.11}$$

for $V_0 \in \Omega_s$. This is part (c), and the condition
$V_t \in \Omega_s$.

*$k$-independence of constants.* The constants $m_W$, $\kappa$,
$C_{\mathrm{KP}}$, $C_D$, and $\delta_0$ are all $k$-independent:
$m_W a_k$ is held fixed through the RG (Balaban CMP 109, \S 3);
$\kappa$ depends only on $L$, $d$, $G$, and $m_W$ (CMP 109, inductive
hypothesis IH3); and $C_{\mathrm{KP}}$ depends only on $\kappa$ and
$d$ (CMP 103). The bound (L.1.7) holds uniformly over all RG steps.
$\square$


---


## Lemma L.1.3 (Flowed polymer activity decay)

*Let $\Omega_s$ be Balaban's small-field domain at RG step $k$, and
let $V_0 \in \Omega_s$. The flowed polymer activity at flow time
$t \geq 0$ is defined by*

$$K_k^{(t)}(X, V) := K_k(X, V_t), \tag{L.1.12}$$

*where $V_t$ is the gradient-flow image of the initial configuration
$V$ and $K_k(X, \cdot)$ is the Balaban polymer activity for connected
polymer $X \in \mathcal{P}_k$ (Section 5.6, Part I). Then for all
$t \geq 0$, all $k \geq 0$, and all $X \in \mathcal{P}_k$:*

$$|K_k^{(t)}(X, V)| \;\leq\; e^{-\kappa(t)\,|X|}, \tag{L.1.13}$$

*where $|X|$ denotes the number of unit cells in the polymer $X$ and*

$$\kappa(t) \;\geq\; \kappa_B \;>\; 0, \tag{L.1.14}$$

*with $\kappa_B = \min(\kappa(G), \kappa_{\mathrm{cl}}^*)$ the
Balaban polymer decay constant from Appendix M, Lemma M.1.2. For KK
modes $n \geq 1$, the effective decay rate satisfies the stronger
bound*

$$\kappa^{\mathrm{KK}}(t)
  \;\geq\; \kappa_B + m_1 \cdot \ell_{\min}(X)
  \cdot \mathbf{1}_{n \geq 1}, \tag{L.1.15}$$

*where $\ell_{\min}(X)$ is the minimal spanning-tree length of $X$ and
$m_1 = 2\sqrt{N}/r_3$ is the lightest KK mass.*


**Proof.** The argument composes the domain preservation of Lemma
L.1.2 with the pointwise validity of Balaban's polymer estimates on
$\Omega_s$.

*Step 1: The flowed configuration lies in $\Omega_s$.* By Lemma
L.1.2, $V_0 \in \Omega_s$ implies $V_t \in \Omega_s$ for all
$t \geq 0$.

*Step 2: Balaban's estimates apply to $V_t$.* The polymer bound
$|K_k(X, V)| \leq e^{-\kappa|X|}$ (Appendix K; Balaban CMP 109,
Theorem 1) holds for every $V \in \Omega_s$, not merely for the
initial configuration. Since $V_t \in \Omega_s$ by Step 1:

$$|K_k^{(t)}(X, V)| = |K_k(X, V_t)|
  \;\leq\; e^{-\kappa|X|}. \tag{L.1.16}$$

Setting $\kappa(t) := \kappa$ gives $\kappa(t) \geq \kappa_B$ where
$\kappa_B := \min(\kappa(G), \kappa_{\mathrm{cl}}^*) > 0$ is the
$(k,K)$-uniform constant from Appendix M, Lemma M.1.2.

*Step 3: KK mass tower enhancement.* In the KK-enhanced theory, the
covariant propagator decomposes by KK mode:

$$G_k^{(n)}(V)
  = \bigl(-D^2[V] + m_W^2 + m_n^2\bigr)^{-1}, \tag{L.1.17}$$

with exponential decay (Appendix K, \S K.2; Balaban CMP 95,
Proposition 1.2):

$$|G_k^{(n)}(x,y;V)| \;\leq\;
  C_D\,e^{-(\delta_0 + m_n)|x-y|}. \tag{L.1.18}$$

For mode $n \geq 1$, the additional mass $m_n > 0$ strictly improves
the decay rate. This propagates through every step of the inductive
construction: the saddle-point evaluation, the Gaussian integration
(the spectral gap $m_W^2 + m_n^2$ strengthens the Neumann series
convergence), and the Mayer resummation (the Koteck\'y--Preiss criterion
converges faster at larger decay rates). Mode by mode:

$$|K_k^{(n)}(X, V_t)| \;\leq\;
  C_0\,e^{-\kappa|X|}\,e^{-m_n \cdot \ell_{\min}(X)}. \tag{L.1.19}$$

Summing over all KK modes:

$$|K_k(X, V_t)| \;\leq\; e^{-\kappa|X|}
  \Bigl(1 + C_0\sum_{n=1}^\infty e^{-m_n\,\ell_{\min}(X)}\Bigr).
  \tag{L.1.20}$$

The KK partition sum is bounded by the geometric series
$Z_{\mathrm{KK}} \leq (e^{m_1\,\ell_{\min}(X)} - 1)^{-1} < \infty$,
since $\ell_{\min}(X) \geq a_k > 0$ for every polymer. Writing
$C_{\mathrm{KK}} := 1 + C_0 Z_{\mathrm{KK}}$, the effective decay
rate satisfies $\kappa(t) \geq \kappa - (\ln C_{\mathrm{KK}})/|X|
\geq \kappa/2 > 0$ for all $|X| \geq |X|_0 :=
\lceil 2\ln C_{\mathrm{KK}}/\kappa \rceil$. The finitely many small
polymers with $|X| < |X|_0$ carry a bounded prefactor
$C_{\mathrm{KK}} \cdot e^{-\kappa|X|}$, which is absorbed by
adjusting the initial polymer bound. The lower bound (L.1.14)
follows. $\square$


---


## Lemma L.1.4 ($K$-uniformity of flowed constants)

*The constants $\kappa(t)$ and $C(t)$ appearing in Lemma L.1.3 are
$K$-uniform: they depend on $N$, the compactification data
$(R, r_3)$, and $t$, but not on the bare theory index $K$.*


**Proof.** $K$-uniformity of the flowed constants follows from
$K$-uniformity of the unflowed constants and the $K$-independence
of the gradient flow.

*Step 1: $K$-uniformity of the unflowed polymer decay.* By Appendix M,
Lemma M.1.2, the unflowed polymer activities satisfy
$|K_k^{(K)}(X, V)| \leq e^{-\kappa_B|X|}$ with $\kappa_B > 0$
independent of both $k$ and $K$. The three parameters governing the
bound---the polymer decay constant $\kappa$ (depending on $L$, $d$,
$G$), the fluctuation mass $m_W$ (fixed in lattice units:
$m_W a_k = 1$), and the Lipschitz constant $C_D = 2(N^2-1)$---are
all $K$-independent (Appendix M, Lemma M.1.2).

*Step 2: $K$-independence of the gradient flow.* The gradient-flow
equation (L.1.2) involves the combination
$g_0^2 \cdot \partial_V S_{\mathrm{KK}}$, where $S_{\mathrm{KK}} =
(1/g_0^2)S_{\mathrm{YM}} + \cdots$. The $g_0^2$ prefactor in the flow
equation cancels the $1/g_0^2$ in the action, so the flow equation for
$V_t$ on $\Omega_s$ is $K$-independent in form. The flow map
$V \mapsto V_t$ does not introduce any $K$-dependent parameters: if
$V \in \Omega_s$ (defined $K$-independently at step $k$), then
$V_t \in \Omega_s$ by Lemma L.1.2, and the bound (L.1.16) applies with
the same $K$-independent constants.

*Step 3: $K$-uniformity of the KK mass tower.* The KK masses $m_n$ are
determined by the internal geometry of $\mathbb{CP}^{N-1}$, with
$m_1 = 2\sqrt{N}/r_3$ depending only on $N$ and $r_3$. By the frozen
dilaton (Section 4.1; Theorem K.1 of Paper 1; Appendix N,
\S N.1.5), the compactification
radius $r_3$ is a fixed physical constant with fractional drift
$\Delta R/R_0 \sim 3 \times 10^{-30}$ per Hubble time. Therefore
$m_n$ is $K$-independent, and the KK mode sum constant
$C_{\mathrm{KK}}(N, r_3)$ depends on the internal geometry but not
on $K$.

Collecting Steps 1--3: for all $t \geq 0$, all $k \geq 0$, and all
$K \geq 0$,

$$|K_k^{(K,t)}(X, V)| \;\leq\; e^{-\kappa_B|X|}, \tag{L.1.21}$$

with $\kappa_B > 0$ independent of $k$, $K$, and $t$. $\square$


---


## Lemma L.1.5 (Flow contractivity on the KK background)

*Let the KK-enhanced lattice gauge theory be as in Section 4.1, with
gauge group $\mathrm{SU}(N)$, internal space
$\mathbb{CP}^{N-1}$, and compactification radius $r_3$. Let
$\{V_t\}_{t \geq 0}$ denote the gradient-flow trajectory (L.1.2) with
initial configuration $V_0 \in \Omega_s$. Then:*

*(a) (Monotone decrease.) The lattice Yang--Mills action satisfies*

$$\frac{d}{dt}\,S_{\mathrm{KK}}[V_t]
  = -g_0^2\sum_\ell
  \bigl\|\partial_{V,\ell}\,S_{\mathrm{KK}}[V_t]\bigr\|^2
  \;\leq\; 0 \tag{L.1.22}$$

*for all $t \geq 0$, with equality if and only if $V_t$ is a
classical solution.*

*(b) (Pointwise energy decrease.) The energy density
$E(t,x) := \frac{1}{4}G_{\mu\nu}^a(t,x)\,G_{\mu\nu}^a(t,x)$
satisfies $\sup_x E(t,x) \leq \sup_x E(0,x)$ for all $t \geq 0$.*

*(c) (Convergence in the $Q = 0$ sector.) In the topologically trivial
sector, the flow converges to the KK vacuum ($A = 0$ on
$\mathbb{CP}^{N-1}$). The Hessian at the vacuum satisfies*

$$\mathrm{Hess}_{A=0}\,S_{\mathrm{KK}}
  \;\geq\; \frac{2N}{r_3^2}\,\mathbb{1}, \tag{L.1.23}$$

*where $2N/r_3^2$ is the Weitzenb\"ock spectral gap on
$\mathbb{CP}^{N-1}$ (Appendix E), ensuring exponential convergence
of the flow to the vacuum.*

*(d) (Instanton suppression.) In the topological sector with second
Chern number $Q \neq 0$, the flow converges to the (anti-)self-dual
instanton with action $8\pi^2|Q|/g^2$. The contribution of
$Q \neq 0$ sectors to flowed correlators is suppressed by
$e^{-8\pi^2|Q|\beta/N}$.*


**Proof.** Parts (a) and (b) are established in the proof of Lemma
L.1.1 and Lemma L.1.2 respectively: (a) is equation (L.1.3), and (b)
follows from the maximum principle applied to (L.1.10)--(L.1.11).

*Part (c): Convergence in $Q = 0$.* The internal Hessian of
$S_{\mathrm{KK}}$ at the trivial connection decomposes via KK
reduction into a direct sum over KK modes $n \geq 0$. The $n = 0$
mode contributes the 4D pure Yang--Mills Hessian (non-negative by
gauge invariance). The $n \geq 1$ modes contribute
$\Delta_{\mathrm{Hodge}}^{\mathbb{CP}^{N-1}} + (n^2/r_3^2)\mathbb{1}$.
By the Weitzenb\"ock formula on $\mathbb{CP}^{N-1}$ (Appendix E):

$$\Delta_{\mathrm{Hodge}} = \nabla^*\nabla + \mathrm{Ric}
  \;\geq\; \frac{2N}{r_3^2}\,\mathbb{1},$$

since $\mathrm{Ric}_{\mathbb{CP}^{N-1}} = (2N/r_3^2)\,g$
(Appendix E). The additional KK mass $n^2/r_3^2$ only strengthens
the bound. In the $Q = 0$ sector, the trivial connection is the
unique global minimum of $S_{\mathrm{KK}}$ and a non-degenerate
minimum with Hessian bounded below by $2N/r_3^2 > 0$. By the
Lojasiewicz--Simon gradient inequality (Feehan, arXiv:1409.1525),
applied in its finite-dimensional form to the compact manifold
$\mathcal{M}$, the gradient flow converges to $A = 0$ with
exponential rate controlled by the spectral gap $2N/r_3^2$.

On the lattice the argument simplifies: $S_{\mathrm{KK}}$ is a
Lyapunov function (Lemma L.1.1(v)), the $\omega$-limit set consists
of critical points, and $A = 0$ is the unique critical point at the
minimum energy level in $Q = 0$. Convergence follows from standard
ODE theory on compact manifolds.

*Part (d): Instanton suppression.* In the sector $Q \neq 0$, the
Bogomolny bound gives $S_{\mathrm{YM}}[A] \geq 8\pi^2|Q|/g^2$, with
equality for (anti-)self-dual instantons. Monotone decrease
(Lemma L.1.1(v)) forces
$S_{\mathrm{YM}}[V_t] \searrow S_\infty \geq 8\pi^2|Q|/g^2$. The
self-dual instanton is the unique global minimum in the $Q$-sector,
and the Lojasiewicz--Simon inequality guarantees convergence.

The Boltzmann weight of the $Q$-sector in the path integral satisfies

$$\frac{Z_Q}{Z_0}
  \;\leq\; C_Q\,e^{-8\pi^2|Q|\beta/N}, \tag{L.1.24}$$

by the Bogomolny bound and the corollary to Theorem 4 (Section 4.4).
At physical couplings ($\beta \sim 6$, $N = 3$):
$e^{-8\pi^2\beta/N} = e^{-16\pi^2} \approx 10^{-69}$. The
correction to flowed correlators from $Q \neq 0$ sectors is beyond
all perturbative orders.

*Frozen dilaton consistency.* The internal geometry is frozen: the
Casimir potential $V(R) = c/R^4$ is exact to all perturbative orders
(Theorem K.1, Paper 1; Appendix N, \S N.1.5), and the compactification radius $r_3$ is fixed
with fractional drift $\Delta R/R_0 \sim 3 \times 10^{-30}$ per Hubble
time. The spectral gap $2N/r_3^2$ and the KK mass tower
$m_n$ are therefore rigid parameters. The vacuum isolation
of part (c) and the polymer convergence of Lemma L.1.3 hold with
$K$-uniform constants on this fixed background. $\square$


---


## Summary of cross-dependencies

The five lemmas form a directed acyclic graph of logical dependencies:

- **Lemma L.1.1** (well-posedness): no internal dependencies.
  Inputs: compactness of $\mathrm{SU}(N)$, smoothness of
  $S_{\mathrm{KK}}$, Picard--Lindel\"of on compact manifolds.

- **Lemma L.1.2** ($\Omega_s$ preservation): depends on
  Lemma L.1.1(v) (action decrease). External inputs: Balaban CMP 109
  (action bound in $\Omega_s$), Appendix K, \S K.2 (coercivity).

- **Lemma L.1.3** (flowed polymer decay): depends on Lemma L.1.2
  ($V_t \in \Omega_s$). External inputs: Balaban CMP 109, Theorem 1
  (polymer bound on $\Omega_s$); Appendix K, \S K.2 (propagator
  decay).

- **Lemma L.1.4** ($K$-uniformity): depends on Lemma L.1.3.
  External inputs: Appendix M, Lemma M.1.2 ($K$-uniform Balaban
  constants); frozen dilaton (Section 4.1; Theorem K.1, Paper 1;
  Appendix N, \S N.1.5 + \S N.3.1).

- **Lemma L.1.5** (contractivity): depends on Lemma L.1.1(v) and
  Lemma L.1.2. External inputs: Appendix E (Weitzenb\"ock bound);
  Section 4.4, Theorem 4 (mass gap and instanton suppression).
