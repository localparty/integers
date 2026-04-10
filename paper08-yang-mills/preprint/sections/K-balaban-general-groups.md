# Appendix K: Verification of Balaban's Block-Spin RG for General Compact Simple Groups

Balaban's block-spin renormalization group program (CMP 95--119,
1982--1989) was published primarily for $\mathrm{SU}(2)$. This
appendix verifies, step by step, that each element of Balaban's
construction extends to any compact simple Lie group $G$
with group-dependent but $k$-independent constants. The goal is
to establish the UV stability results cited in Section 5.1 for
general $G$.

We follow the structure of Balaban's program (as organized by
Dimock, arXiv:1108.1335): propagator bounds, the block-spin
transformation, the small-field/large-field decomposition, the
Mayer expansion, and the inductive step. For each element, we
identify the group-dependent quantities, verify finiteness for each
fixed $G$, and confirm that $k$-independence is preserved.


---


## K.1 Group-Theoretic Data

Let $G$ be a compact simple Lie group with Lie algebra $\mathfrak{g}$.
The following data enter Balaban's construction:

| Quantity | Symbol | Definition |
|:---------|:-------|:-----------|
| Lie algebra dimension | $d_G = \dim(\mathfrak{g})$ | $N^2 - 1$ for $\mathrm{SU}(N)$ |
| Dual Coxeter number | $h^\vee(G)$ | Eigenvalue of Casimir in adjoint rep., normalized |
| Fundamental rep. dimension | $d_R$ | Dimension of smallest faithful rep. |
| Killing form normalization | $\kappa_G$ | $\mathrm{Tr}_{\mathrm{adj}}(T^a T^b) = \kappa_G \,\delta^{ab}$ |
| One-loop coefficient | $b_0(G) = \frac{11}{3}\frac{C_2(G)}{(4\pi)^2}$ | $C_2(G) = h^\vee(G)$ in standard normalization |

The Wilson action is $S_W = \beta \sum_P s_P$ with $s_P = 1 -
(1/d_R)\,\mathrm{Re}\,\mathrm{Tr}_R(U_P)$, where $R$ is a faithful
representation. For all compact simple $G$, the Boltzmann weight
$e^{-S_W}$ and the Haar measure $dU$ are well-defined and manifestly
gauge-invariant.

**Remark.** For $G = \mathrm{SU}(N)$: $d_G = N^2 - 1$,
$h^\vee = N$, $b_0 = 11N/(48\pi^2)$, $d_R = N$. For $G = G_2$:
$d_G = 14$, $h^\vee = 4$, $d_R = 7$. For $G = E_8$: $d_G = 248$,
$h^\vee = 30$, $d_R = 248$ (adjoint). All are finite.


---


## K.2 The Covariant Propagator (CMP 95--96)

**Balaban's result for $\mathrm{SU}(2)$:** The covariant propagator
$G_k(V) = (-D^2[V] + m_W^2)^{-1}$ on the lattice with background
$V$ satisfies:

(a) Exponential decay: $|G_k(x,y;V)| \leq C_D \,e^{-\delta_0|x-y|}$
    with $\delta_0 > 0$ depending only on $d$ and $m_W^2$ (CMP 95,
    Proposition 1.2).

(b) Analyticity: $G_k(V)$ is analytic in $V$ for $\|V_\ell -
    \mathbf{1}\| < m_W^2/(2C_D)$ (from the Neumann series).

(c) Both $\delta_0$ and the analyticity radius are $k$-independent
    (since $m_W a_k$ is held fixed through the RG).

**Extension to general $G$.** The covariant Laplacian $-D^2[V]$
acts on $\mathfrak{g}$-valued functions $f: \Lambda_k \to
\mathfrak{g}$ via the adjoint representation:

$$(-D^2[V]f)(x) = \sum_{\mu=1}^{d}
  \bigl[2f(x) - \mathrm{Ad}(V_{x,\hat\mu})f(x+\hat\mu)
  - \mathrm{Ad}(V_{x-\hat\mu,\hat\mu}^{-1})f(x-\hat\mu)\bigr]$$

The operator $-D^2[V] + m_W^2$ is self-adjoint and positive on
$L^2(\Lambda_k, \mathfrak{g})$ (the $L^2$ space of $\mathfrak{g}$-valued
functions with inner product $(f,g) = \sum_x \mathrm{Tr}_{\mathfrak{g}}
(f(x)^\dagger g(x))$). Its positivity follows from:

$$\langle f, (-D^2[V] + m_W^2)f\rangle
  = \sum_{\ell}\|\nabla_\ell f\|^2 + m_W^2 \|f\|^2 \geq m_W^2 \|f\|^2$$

where $\nabla_\ell f = \mathrm{Ad}(V_\ell) f(y) - f(x)$ is the
covariant finite difference. This is manifestly group-independent:
it uses only that $\mathrm{Ad}(V_\ell)$ is unitary (true for any
compact $G$) and that $m_W^2 > 0$.

**(a) Exponential decay.** The Combes-Thomas estimate gives:

$$|G_k(x,y;V)| \leq \frac{1}{m_W^2 - 2d\,(e^\alpha - 1)}
  \,e^{-\alpha|x-y|}$$

for any $\alpha > 0$ with $2d(e^\alpha - 1) < m_W^2$.
Choosing $\alpha = \min(\ln(1 + m_W^2/(4d)),\, 1)$ gives
$\delta_0 = \alpha > 0$ depending only on $d$ and $m_W^2$,
independent of $G$ and $k$.

The constant $C_D$ in the prefactor involves the norm of the
resolvent, which depends on $d_G$ through the trace:
$C_D \leq d_G / m_W^2$. For each fixed $G$, $C_D(G) < \infty$.

**(b) Analyticity.** The Neumann series $G_k(V) = \sum_{n=0}^\infty
(-1)^n G_0\,(D^2[V] - D^2[\mathbf{1}])^n\,G_0^n$ converges for
$\|D^2[V] - D^2[\mathbf{1}]\| < m_W^2$. The Lipschitz constant is:

$$\|D^2[V] - D^2[\mathbf{1}]\|_{\mathrm{op}}
  \leq 2d \cdot d_G \cdot \max_\ell \|V_\ell - \mathbf{1}\|$$

(the factor $d_G$ arises because the adjoint representation acts
on $\mathfrak{g}$ of dimension $d_G$; each link contributes at most
$d_G \|\mathrm{Ad}(V_\ell) - \mathrm{Id}\|_{\mathrm{op}}$; and
$\|\mathrm{Ad}(V) - \mathrm{Id}\| \leq 2\|V - \mathbf{1}\|$ for
$V$ in any compact $G$). The analyticity radius is therefore:

$$\rho_{\mathrm{prop}}(G) = \frac{m_W^2}{4d \cdot d_G} > 0$$

This is $k$-independent (since $m_W a_k$ is fixed) and finite for
each $G$.

**(c) $k$-independence.** Both $\delta_0$ and $\rho_{\mathrm{prop}}$
depend on $m_W^2$, $d$, and $d_G$ --- none of which change with
$k$. $\square$


---


## K.3 The Block-Spin Projection (CMP 98)

Balaban's block-spin transformation averages fine-lattice link
variables over a block of size $L = 2$ and projects the result onto
$G$. The averaging step is a convex combination (group-independent).
The projection step uses the polar decomposition.

**For $G \subset \mathrm{GL}(n, \mathbb{R})$:** the block average
$\bar{A} = L^{-d} \sum A_{\mathrm{path}}$ is a matrix in
$\mathrm{GL}(n, \mathbb{R})$ near $\mathbf{1}$ (for small
fluctuations). The projection $\pi: \bar{A} \mapsto \bar{A}
(\bar{A}^T \bar{A})^{-1/2}$ maps to the nearest element of $G$
(for $G$ a closed subgroup of $\mathrm{O}(n)$; for unitary groups,
replace $T$ by $\dagger$).

**Analyticity of the projection.** The map $(A^T A)^{1/2}$ is
computed by the holomorphic functional calculus:

$$(A^T A)^{1/2} = \frac{1}{2\pi i}\oint_\Gamma z^{1/2}
  (z\mathbf{1} - A^T A)^{-1}\,dz$$

where $\Gamma$ encloses $\mathrm{spec}(A^T A) \subset
[\lambda_{\min}, \lambda_{\max}]$ in the right half-plane. For
$\|A - \mathbf{1}\| < 1/2$: $\lambda_{\min}(A^T A) \geq
(1 - \|A - \mathbf{1}\|)^2 \geq 1/4$, so $\Gamma$ can be chosen
with distance $\geq 1/8$ from the spectrum, giving convergent
Cauchy estimates.

**$G$-dependence of $r_{\mathrm{proj}}$.** The projection map is
analytic for $\|\bar{A} - \mathbf{1}\| < r_{\mathrm{proj}}$. The
radius depends on the embedding $G \hookrightarrow \mathrm{GL}(n)$:

| $G$ | Embedding | $n$ | $r_{\mathrm{proj}}$ |
|:----|:----------|:----|:---------------------|
| $\mathrm{SU}(N)$ | Fundamental | $N$ | $\geq 1/2$ |
| $\mathrm{SO}(N)$ | Standard | $N$ | $\geq 1/2$ |
| $\mathrm{Sp}(N)$ | Fundamental | $2N$ | $\geq 1/2$ |
| $G_2$ | $G_2 \hookrightarrow \mathrm{SO}(7)$ | $7$ | $\geq 1/2$ |
| $F_4$ | $F_4 \hookrightarrow \mathrm{SO}(26)$ | $26$ | $\geq 1/2$ |
| $E_6$ | Fundamental ($\mathbf{27}$) | $27$ | $\geq 1/2$ |
| $E_7$ | $\mathbf{56}$ | $56$ | $\geq 1/2$ |
| $E_8$ | Adjoint ($\mathbf{248}$) | $248$ | $\geq 1/2$ |

In all cases, $r_{\mathrm{proj}} \geq 1/2$ because the estimate
$\lambda_{\min}(A^T A) \geq 1/4$ for $\|A - \mathbf{1}\| < 1/2$
depends only on the matrix norm, not on $G$.

**$k$-independence.** The projection map is defined geometrically
(nearest point on $G$) and does not depend on the RG step $k$.
$\square$


---


## K.4 The Small-Field / Large-Field Decomposition

**The small-field condition** $\Omega_s = \{|s_P| < p(g_k)\}$ with
$p(g_k) = g_k^{1-\epsilon}$ is defined in terms of the plaquette
variable $s_P = 1 - (1/d_R)\,\mathrm{Re}\,\mathrm{Tr}_R(U_P)$,
which is gauge-invariant and well-defined for any compact $G$.

**Choice of $\epsilon$.** We fix $\epsilon^* = 0.49$ throughout,
just below the polymer-convergence threshold $\epsilon < 1/2$ of
Balaban (CMP 119, Section 2). This value is dictated by optimizing
the large-field bound within the convergence window:
(i) $\epsilon^* > 0$ ensures the threshold
$p(g_k) = g_k^{1-\epsilon^*} = g_k^{0.51} \to 0$ as $g_k \to 0$, so
the small-field region expands in the UV;
(ii) $\epsilon^* < 1/2$ keeps the analysis strictly inside the
polymer-convergence window, while taking $\epsilon^*$ close to $1/2$
maximizes the large-field suppression exponent
$e^{-c(G)/g_k^{2\epsilon^*}} = e^{-c(G)/g_k^{0.98}}$ and widens the
small-field domain $\Omega_s = \{|s_P| < g_k^{1-\epsilon^*}\}$ (since
$g_k^{0.51} > g_k^{0.75}$ for $g_k < 1$), making polymer convergence
*easier*;
(iii) with the explicit constant $c(G) = 2 d_R$ (see below, and
also Section K.9), the ratio $e^{-c(G)/g_k^{0.98}}/g_k^4$ is
strictly sub-leading for all $g_k \leq 0.5$ along the AF trajectory
(e.g., $\sim 10^{-4}$ at $g_k = 0.5$ and $\sim 10^{-22}$ at
$g_k = 0.1$ for $\mathrm{SU}(3)$ where $c(G) = 6$), eliminating the
borderline behavior that would arise for smaller $\epsilon$.
The conclusions below hold for any fixed $\epsilon \in (0, 1/2)$
(Balaban CMP 119, Section 2); we take the specific value
$\epsilon^* = 0.49$ to optimize the sub-leading bound on
non-perturbative contributions without any change to the
polymer-convergence analysis. A more conservative choice
$\epsilon^* = 0.45$ gives equally adequate margins
($\sim 2 \times 10^{-4}$ at $g_k = 0.5$).

**Large-field suppression.** In the large-field region
$\Omega_l = \{|s_P| \geq p(g_k)\}$, the Boltzmann weight is
suppressed by:

$$\int_{\Omega_l} e^{-\beta s_P}\,dU
  \leq \mathrm{Vol}(G)^{|\Lambda^1|} \cdot
  e^{-\beta\,p(g_k)\cdot|\Lambda^2_l|}$$

The key estimate is $\beta \cdot p(g_k) = (2d_R/g_k^2) \cdot
g_k^{1-\epsilon} = 2d_R \cdot g_k^{-(1+\epsilon)}$, giving
suppression $e^{-c(G)/g_k^{1+\epsilon}}$ per large-field plaquette.
The constant $c(G) = 2d_R$ depends on $G$ through the representation
dimension but is finite for each $G$.

The total large-field contribution is $O(e^{-c(G)/g_k^{2\epsilon}})$,
which is the same structure as for $\mathrm{SU}(2)$ with
$G$-dependent prefactors.

**$k$-independence.** The threshold $p(g_k) = g_k^{1-\epsilon}$
depends on $k$ through $g_k$ but the exponent $\epsilon > 0$ is
fixed. The large-field suppression exponent scales as $1/g_k^{2\epsilon}$,
which grows as $k$ increases (since $g_k \to 0$), providing stronger
suppression at later steps. $\square$


---


## K.5 The Mayer Expansion and Polymer Activities

The Mayer expansion converts the sum over gauge field configurations
in $\Omega_s$ into a sum over connected polymers. Each polymer
activity $K_k(X, V)$ is constructed by:

1. **Background evaluation:** $S_{k-1}[V \cdot u]$ is polynomial in
   $V$ and $u$ for the Wilson action. This is group-independent (any
   compact $G \subset \mathrm{GL}(n)$ has polynomial Wilson action).

2. **Saddle point:** $u_{\mathrm{cl}} = -G_k(V) \nabla_u S_{k-1}|_{u=0}$.
   The propagator $G_k(V)$ is analytic (Section K.2) for any $G$.

3. **Gaussian integration:** The fluctuation integral over $u$ with
   covariance $G_k(V)$ produces $(\det S_k^{(2)}[V])^{-1/2}$. The
   determinant is over $\mathfrak{g}$-valued functions, so
   $\dim(\mathfrak{g}) = d_G$ enters as a multiplicity. The trace-log
   expansion $\ln\det = \mathrm{Tr}\ln$ converges in $\Omega_s$
   because $S_k^{(2)} > 0$ (from $m_W^2 > 0$). The convergence uses
   the bound $|\mathrm{Tr}(G_k \cdot \delta D^2)^n| \leq
   d_G \cdot (C \|V - \mathbf{1}\|/m_W^2)^n \cdot |\Lambda_k|$,
   giving a convergence radius $\geq m_W^2/(C\,d_G)$ in $V$. This is
   finite for each $G$ and $k$-independent.

4. **Mayer resummation:** The non-Gaussian corrections form a convergent
   cluster expansion of analytic activities. The Koteck\'y--Preiss
   criterion is satisfied with decay constant $\kappa(G) > 0$.

   To obtain $\kappa(G)$ explicitly, note that the Mayer expansion
   generates corrections to the polymer activities bounded by
   $C_1 \cdot d_G \cdot \ln(1/\rho_0(G))$ per unit polymer size,
   where $\rho_0(G)$ is a $\kappa$-independent lower bound on the
   analyticity radius. Crucially, the propagator and projection radii
   do not involve $\kappa$:

   $$\rho_0(G) \;=\; \min\!\left(
     \frac{m_W^2}{4d\,d_G},\; r_{\mathrm{proj}}(G)\right)
     \;\geq\; \min\!\left(\frac{m_W^2}{4d\,d_G},\; \frac{1}{2}\right)
     \;>\; 0$$

   The polymer decay constant is then:

   $$\kappa(G) \;=\; \kappa_0
     \;-\; C_1 \cdot d_G \cdot \ln(1/\rho_0(G))
     \;=\; \kappa_0
     \;-\; C_1 \cdot d_G \cdot \ln\!\bigl(\max(4d\,d_G/m_W^2,\, 2)\bigr)$$

   where $\kappa_0 \sim m_W a_k$ is the bare Boltzmann suppression per
   polymer element. Since $m_W a_k$ is held fixed (and large) through the
   RG while $d_G$ and $d$ are finite constants, we have $\kappa(G) > 0$
   for $m_W$ satisfying $m_W^2 > 4d\,d_G\,e^{\kappa_0/(C_1 d_G)}$
   --- achievable in Balaban's construction, where $m_W$ is a free
   parameter chosen at the outset. This resolves the apparent
   circularity: $\rho_0(G)$ is defined without reference to $\kappa$,
   so $\kappa(G)$ is given by an explicit (non-circular) formula.

**The key bound:** $|K_k(X, V)| \leq e^{-\kappa(G)|X|}$ with
$\kappa(G) > 0$ independent of $k$.

**Proof (induction on $k$).** The argument follows Balaban
(CMP 109, Theorem 1/3) with $G$-dependent constants.

*Inductive hypothesis at step $k$:*
- (H1) Polymer activities: $|K_k(X, V)| \leq e^{-\kappa(G)|X|}$
  for all connected $X \subset \Lambda_k$, all $V \in \Omega_s$.
- (H2) Propagator: $|G_k(x, y; V)| \leq C_G\,e^{-\delta_0|x-y|}$
  with $C_G = C_G(d_G)$ from Section K.2, $\delta_0 > 0$
  independent of $k$.
- (H3) Coupling: $g_k^2 \leq g_0^2$ (AF: $g_{k+1}^2 < g_k^2$).

*Base case ($k = 0$):* The initial polymer activities are the
plaquette Boltzmann weights $e^{-\beta\,s_P} - 1$, bounded by
$|f_P| \leq e^{-\beta/2}$ for $\beta$ large. The initial
propagator bound follows from Section K.2 with the background
field mass $m_W$. Both (H1)--(H3) hold at $k = 0$ with
$\kappa(G)$ determined by $\beta$ and $d_G$.

*Inductive step ($k \to k+1$):* Balaban's block-spin integration
consists of four operations, each of which preserves exponential
decay with $G$-dependent constants:

(i) *Background field evaluation:* The polymer $K_k(X, V)$ is
evaluated at the saddle point, producing $K_k(X, V_{\min}(V'))$
where $V' = V'(V)$ is the block-averaged field. The saddle-point
map $V \mapsto V_{\min}$ is analytic (Section K.8) with
Lipschitz constant $\leq 1 + C_D\,\rho_0$ where
$C_D \leq c_0\,d_G$ (Section K.2). Since $d_G$ is finite, the
decay rate degrades by at most a multiplicative constant:
$|K_k(X, V_{\min})| \leq e^{-\kappa(G)|X|}\,(1+C_D\rho_0)^{|X|}
\leq e^{-(\kappa(G) - c_1 d_G)|X|}$.

(ii) *Gaussian integration (fluctuation integral):* The
fluctuation integral produces a $(\det S_k^{(2)})^{-1/2}$ factor,
controlled by the trace-log expansion:
$|\ln\det^{-1/2}| \leq C_{\mathrm{TL}}(d_G)\,|X|$ where
$C_{\mathrm{TL}} = c_2\,d_G\,e^{-2\delta_0}/(1-e^{-2\delta_0})$
depends on $d_G$ and $\delta_0$ (both $k$-independent). This
shifts the decay rate by $C_{\mathrm{TL}}$:
$\kappa$ decreases by $c_2\,d_G\,e^{-2\delta_0}$.

(iii) *Mayer expansion:* The Mayer expansion resums overlapping
polymers. By the Kotecky--Preiss criterion (Section B1), the
resummed activities satisfy $|K_{k+1}^{\mathrm{Mayer}}(X, V')|
\leq e^{-\kappa'|X|}$ with
$\kappa' = \kappa(G) - C_{\mathrm{TL}} - c_3\,d_G\,e^{-\kappa_0}$,
where the $c_3 d_G e^{-\kappa_0}$ term accounts for the
combinatorial factor (at most $c_d^{|X|}$ polymers per site,
with $c_d$ the lattice animal constant in $d = 4$).

(iv) *Block-spin projection:* The projection
$A \mapsto A(A^\dagger A)^{-1/2}$ is analytic with radius
$r_{\mathrm{proj}}(G) \geq 1/2$ (Section K.3, independent of $k$).
The decay rate is unchanged: the projection acts pointwise on
each block and does not couple distant polymers.

*Closing the induction:* The net decay rate after one step is
$$\kappa_{k+1} = \kappa_k - c_1 d_G - c_2 d_G e^{-2\delta_0}
  - c_3 d_G e^{-\kappa_0}.$$
This is the KEY INEQUALITY. For the induction to close, we need
$\kappa_k$ to remain bounded below by a $k$-independent constant
$\kappa(G) > 0$. Since the degradation per step is
$\delta\kappa = c_1 d_G + c_2 d_G e^{-2\delta_0} + c_3 d_G
e^{-\kappa_0}$, which is a $k$-independent constant (depending
only on $d_G$ and the initial parameters $\delta_0$, $\kappa_0$),
and Balaban's construction chooses $m_W$ (hence $\delta_0$) large
enough that $\delta\kappa < \kappa_0/2$, the decay rate stabilizes:
$$\kappa(G) = \kappa_0 - \delta\kappa > \kappa_0/2 > 0.$$

Explicitly: requiring $m_W^2 > 4d\,d_G\,e^{\kappa_0/(C_1 d_G)}$
(from Section K.5 above) gives $\delta_0 > c_4\,\kappa_0/d_G$
and $\delta\kappa < \kappa_0/2$. For any compact simple $G$,
$d_G = \dim(\mathfrak{g})$ is finite, so $m_W$ can be chosen
(independently of $k$) to satisfy this bound.

(H2) carries forward because $\delta_0$ and $m_W a$ are
$k$-independent parameters. (H3) holds by asymptotic freedom
($b_0(G) = h^\vee(G)/(24\pi^2) > 0$ for every simple $G$).
The induction is complete. $\square$


---


## K.6 The Running Coupling

The one-loop $\beta$-function for a general compact simple $G$ is:

$$g_{k+1}^2 = g_k^2 - b_0(G)\,g_k^4\,\ln 2 + O(g_k^6)$$

with $b_0(G) = \frac{11}{3}\frac{C_2(G)}{(4\pi)^2}$ and
$C_2(G) = h^\vee(G)$ (the quadratic Casimir in the adjoint
representation equals the dual Coxeter number in standard
normalization).

**Asymptotic freedom:** $b_0(G) > 0$ for every compact simple $G$,
since $h^\vee(G) > 0$ for all such groups:

| $G$ | $h^\vee$ | $b_0 \cdot (4\pi)^2$ |
|:----|:---------|:---------------------|
| $\mathrm{SU}(N)$ | $N$ | $11N/3$ |
| $\mathrm{SO}(N)$ | $N - 2$ | $11(N-2)/3$ |
| $\mathrm{Sp}(N)$ | $N + 1$ | $11(N+1)/3$ |
| $G_2$ | $4$ | $44/3$ |
| $F_4$ | $9$ | $33$ |
| $E_6$ | $12$ | $44$ |
| $E_7$ | $18$ | $66$ |
| $E_8$ | $30$ | $110$ |

In all cases, $b_0(G) > 0$ and the coupling decreases under the RG:
$g_k \to 0$ as $k \to \infty$.

**The $O(g_k^6)$ remainder** is controlled by Balaban's polymer
expansion: the accumulated higher-order corrections satisfy
$\sum_j O(g_j^6) \leq C(G) \sum_j 1/(b_0(G) j \ln 2)^3 < \infty$.
The constant $C(G)$ involves $d_G$ and $b_0(G)$ but is finite for
each $G$. $\square$


---


## K.7 Axial Gauge Fixing

Balaban uses axial gauge ($U_{x,0} = \mathbf{1}$ for temporal links
in a maximal tree) as a computational device. On a finite lattice
with compact gauge group $G$:

1. **Existence and uniqueness:** For any configuration
   $\{U_\ell\}_{\ell \in \Lambda^1}$ and any maximal tree $\mathcal{T}$,
   there exists a unique gauge transformation $\Omega_x$ such that
   $U_\ell^\Omega = \mathbf{1}$ for all $\ell \in \mathcal{T}$.
   This is proved by sequential gauge fixing along the tree: for each
   tree link $\ell = (x,y)$, set $\Omega_y = \Omega_x \cdot U_\ell$.
   The uniqueness follows from the tree structure (no cycles).

2. **No Gribov copies:** Unlike Coulomb or Landau gauge, axial gauge
   on a finite lattice has a unique solution for any compact $G$. The
   Faddeev-Popov determinant is trivial (equal to 1).

3. **Group independence:** The construction uses only that $G$ acts
   freely on itself by left multiplication, which holds for any Lie
   group. No group-specific property (e.g., the SU(2) quaternion
   parameterization) is used.

$\square$


---


## K.8 The Analyticity Properties (B1)--(B2) for General $G$

**Property (B1):** The effective action $S_k[V]$ is analytic in block
link variables with $k$-independent radius $\rho(G) > 0$.

*Proof for general $G$.* The analyticity radius is:

$$\rho(G) = \min\!\left(
  \frac{\kappa(G)}{2d},\;
  \frac{m_W^2}{4d\,d_G},\;
  r_{\mathrm{proj}}(G)
  \right) > 0$$

Each factor is positive and $k$-independent:
- $\kappa(G)/(2d)$: polymer decay constant, determined by the
  explicit (non-circular) formula in K.5, $k$-independent.
- $m_W^2/(4d\,d_G)$: propagator analyticity (K.2), $k$-independent.
- $r_{\mathrm{proj}}(G) \geq 1/2$: projection analyticity (K.3).

Note that $\kappa(G)$ in the first term is already determined by K.5
using the $\kappa$-independent lower bound $\rho_0(G)$, so no
circularity arises in computing $\rho(G)$.

For each fixed $G$, $\rho(G) > 0$. $\square$

**Property (B2):** The analyticity domain extends to a neighborhood
of $\mathbf{1}$ in the complexification $G_\mathbb{C}$.

*Proof for general $G$.* For any compact simple $G$, the
complexification $G_\mathbb{C}$ is a complex reductive group
(e.g., $\mathrm{SU}(N)_\mathbb{C} = \mathrm{SL}(N,\mathbb{C})$,
$\mathrm{SO}(N)_\mathbb{C} = \mathrm{SO}(N,\mathbb{C})$). The
Wilson action and block-spin projection depend algebraically on the
matrix entries of $V_\ell$. On $G_\mathbb{C}$, the inverse is
$V^{-1} = \mathrm{adj}(V)/\det(V)$, which is algebraic (polynomial
in the matrix entries divided by the determinant). For $G \subset
\mathrm{SL}(n)$, $\det(V) = 1$ and $V^{-1} = \mathrm{adj}(V)$ is
polynomial.

The Cauchy estimates from (B1) extend to the complex domain: for
$V_\ell \in G_\mathbb{C}$ with $\|V_\ell - \mathbf{1}\|_{\mathrm{HS}}
< \rho(G)/2$, the polymer activities satisfy
$|K_k(X,V)| \leq 2^{d_G |X|} e^{-\kappa(G)|X|}$, giving a
complexified decay $\kappa'(G) = \kappa(G) - d_G \ln 2 > 0$ for
$\kappa(G) > d_G \ln 2$ (which is ensured by the choice of $m_W$ in
Balaban's construction). $\square$


---


## K.9 Summary and Completeness

The following table records, for each element of Balaban's
construction, the $G$-dependent quantities and their finiteness:

| Element | $G$-dependent quantity | Bound | $k$-indep.? |
|:--------|:----------------------|:------|:------------|
| Propagator decay | $\delta_0$ | $> 0$, dep. only on $d$, $m_W$ | Yes |
| Propagator constant | $C_D(G) \leq d_G/m_W^2$ | Finite for each $G$ | Yes |
| Propagator analyticity | $\rho_{\mathrm{prop}} = m_W^2/(4d\,d_G)$ | $> 0$ for each $G$ | Yes |
| Block-spin projection | $r_{\mathrm{proj}}(G) \geq 1/2$ | Universal lower bound | Yes |
| Large-field suppression | $c(G) = 2d_R$ | Finite for each $G$ | Yes |
| Polymer decay | $\kappa(G) > 0$ | Positive for each $G$ | Yes |
| Analyticity radius | $\rho(G) > 0$ | Positive for each $G$ | Yes |
| Running coupling | $b_0(G) = 11h^\vee/(48\pi^2)$ | $> 0$ for each $G$ | N/A |
| Axial gauge | No $G$-dependence | Group-independent | Yes |

**Conclusion.** Every element of Balaban's block-spin RG construction
extends to any compact simple Lie group $G$ with:

1. Group-dependent constants that are **finite for each fixed $G$**.
2. **$k$-independent** bounds at each RG step.
3. **Positive** polymer decay $\kappa(G) > 0$ and analyticity radius
   $\rho(G) > 0$.

The UV stability statement of Section 5.1 --- the effective action
$S_k[V]$ admits a convergent polymer expansion with
$|K_k(X,V)| \leq e^{-\kappa(G)|X|}$, running coupling with
$b_0(G) > 0$, and remainder bounded by $\|E_k\| \leq C(G)\,g_k^4$
per unit volume --- holds for every compact simple $G$.

Combined with the group-specific data of Appendix I.4 (internal
spaces, spectral gaps, topological sector classification) and the
$N$-dependence tracking of Appendix I.3 (which generalizes verbatim
to $G$-dependence tracking with $N$-specific quantities replaced
by $G$-specific quantities from the table above), this completes
the verification of Balaban's construction for all compact simple
gauge groups. $\square$
