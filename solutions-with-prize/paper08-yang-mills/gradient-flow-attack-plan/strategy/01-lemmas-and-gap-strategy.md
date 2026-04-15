# Bridge Lemmas and Gap Strategy

*Companion to `formal-argument.md`. This document states the precise*
*lemmas needed to bridge the QG5D results (Paper 10, gravity on*
*$M^4 \times S^1/\mathbb{Z}_2$) to the Yang--Mills gradient-flow*
*programme (gauge theory on $\Lambda \times \mathbb{CP}^{N-1}$),*
*with a strategy for each gap identified in the referee assessment.*

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*


---


## 0. The Bridge Problem

Paper 10's UV finiteness results are for:

- **Operator:** Lichnerowicz operator $\mathcal{L}$ for linearized
  ~~5D gravity~~ M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" --> in de Donder gauge.
- **Manifold:** $M^4 \times S^1/\mathbb{Z}_2$ (flat background).
- **Result:** $a_2(\mathcal{L}) = a_4(\mathcal{L}) = 0$.

The gradient-flow programme needs UV control for:

- **Operator:** Covariant Laplacian $-D^2[V] + m_W^2$ on
  $\mathfrak{su}(N)$-valued fields, plus the flowed field strength
  composite $\mathrm{Tr}\,F_t^2$.
- **Manifold:** $\Lambda_a \times \mathbb{CP}^{N-1}$
  (curved internal space, lattice base).
- **Result:** UV finiteness of flowed correlators as $a \to 0$,
  and existence of the $t \to 0^+$ limit.

These are **different operators on different manifolds**. The bridge
requires identifying which mechanisms transfer and which require
independent proofs.

**Key distinction:** Two independent UV regulation mechanisms
are available on $\Lambda \times \mathbb{CP}^{N-1}$:

1. **The gradient flow** ($e^{-tp^2}$ damping at $t > 0$).
2. **The KK mass tower** ($m_n = \sqrt{\lambda_n^{(1)}}/r_3$
   with $\lambda_n^{(1)} \geq 4N/r_3^2$).

Mechanism 1 is identical in gravity and gauge theory (the heat
kernel is universal). Mechanism 2 differs in detail ($S^1$ modes
vs. $\mathbb{CP}^{N-1}$ modes) but shares the structural feature:
a discrete tower of masses providing UV regulation at $t = 0$.

The bridge lemmas below establish that Mechanism 2 on
$\mathbb{CP}^{N-1}$ provides UV regulation **at least as strong**
as Mechanism 2 on $S^1/\mathbb{Z}_2$.


---


## 1. Bridge Lemma 1: Seeley--DeWitt Coefficients on $\mathbb{CP}^{N-1}$

### Statement

**Lemma B.1 (Seeley--DeWitt on the gauge-field Laplacian).**
*Let $\Delta_{\mathrm{gauge}} = -D^2[\mathbf{1}] + m_W^2$ be the
covariant Laplacian at the trivial connection on
$\mathbb{CP}^{N-1}$ with Fubini--Study metric, acting on
$\mathfrak{su}(N)$-valued 1-forms. Then:*

*(a) $a_0(\Delta_{\mathrm{gauge}}) = (N^2 - 1) \cdot
\mathrm{Vol}(\mathbb{CP}^{N-1}) / (4\pi)^{N-1} > 0.$*

*(b) $a_2(\Delta_{\mathrm{gauge}}) = (N^2-1) \int_{\mathbb{CP}^{N-1}}
\left(\frac{R}{6} - m_W^2\right) (4\pi)^{-(N-1)}\,d\mu \neq 0$
in general (the internal space is curved).*

*(c) Despite $a_2 \neq 0$, the KK mode sum
$\sum_n d_n e^{-t\lambda_n^{(1)}}$ converges for all $t > 0$ and
its $t \to 0^+$ behavior is controlled by the Weyl asymptotics
$N(\lambda) \sim C \lambda^{N-1}$, which is integrable against any
power of $e^{-t\lambda}$.*

### Why $a_2 \neq 0$ does not matter

Unlike the flat $S^1/\mathbb{Z}_2$ background (where $a_2 = a_4 = 0$
because all curvature invariants vanish), $\mathbb{CP}^{N-1}$ has
positive Ricci curvature $\mathrm{Ric} = 2N/r_3^2 \cdot g$, so
the Seeley--DeWitt coefficient $a_2$ is generically nonzero.

**This does not compromise the programme** because the UV finiteness
of flowed correlators at $t > 0$ does not require $a_2 = 0$. It
requires only that the heat kernel $e^{-t\Delta_{\mathrm{gauge}}}$
is trace-class for $t > 0$, which is automatic on compact manifolds.
The nonzero $a_2$ affects the **rate** of the $t \to 0^+$ singularity
but not the **existence** of the flowed theory at $t > 0$.

The role of Paper 10's $a_2 = a_4 = 0$ is more specific: it shows
that on the flat KK background, the Goroff--Sagnotti counterterm
vanishes. On $\mathbb{CP}^{N-1}$, the relevant statement is
different: the KK mass gap ($\mu_1 \geq 2N/r_3^2$) provides IR
regulation that, combined with the flow's UV regulation, makes the
flowed theory well-defined.

### Proof strategy

Compute $a_0, a_2, a_4$ for $\Delta_{\mathrm{gauge}}$ on
$\mathbb{CP}^{N-1}$ using the Vassilevich (2003) formulas with
the Fubini--Study curvature:

$$a_2 = \frac{1}{(4\pi)^{N-1}} \int_{\mathbb{CP}^{N-1}}
  \mathrm{tr}\left(\frac{R}{6}\,\mathbf{1}_{\mathfrak{g}}
  + E\right) d\mu,$$

where $E = \mathrm{Ric}$ (the endomorphism for the Weitzenböck
formula on 1-forms) and $R = 2N(2N-2)/r_3^2$ (the scalar curvature).
This is a finite computation using the known geometry of
$\mathbb{CP}^{N-1}$ and can be verified in sympy.

**Estimated effort:** 1--2 pages. Straightforward computation.


---


## 2. Bridge Lemma 2: KK Mode Sum Regularity at $t = 0$

### Statement

**Lemma B.2 (KK mode sum convergence on $\mathbb{CP}^{N-1}$).**
*Let $\{\lambda_n^{(1)}\}_{n \geq 1}$ be the eigenvalues of the
Hodge Laplacian on 1-forms on $(\mathbb{CP}^{N-1}, g_{\mathrm{FS}})$,
with degeneracies $d_n$, and let $m_n = \sqrt{\lambda_n^{(1)}}/r_3$.
Define the spectral zeta function*

$$\zeta_{\mathrm{gauge}}(s) = \sum_{n=1}^{\infty}
  d_n\,(\lambda_n^{(1)})^{-s}.$$

*(a) $\zeta_{\mathrm{gauge}}(s)$ converges for
$\mathrm{Re}(s) > N - 1$ and admits meromorphic continuation to
$\mathbb{C}$ with at most simple poles at $s = 1, 2, \ldots, N-1$.*

*(b) $\zeta_{\mathrm{gauge}}(0)$ and
$\zeta_{\mathrm{gauge}}'(0)$ are finite. In particular, the
zeta-regularized determinant
$\det'(\Delta_{\mathrm{gauge}}) = e^{-\zeta'_{\mathrm{gauge}}(0)}$
is well-defined and positive.*

*(c) For any polynomial $P(n)$ of degree $d$:*
$$\sum_{n=1}^{\infty} d_n\,P(n)\,e^{-t\lambda_n^{(1)}}
  = O(t^{-(N-1+d)/2}) \qquad \text{as } t \to 0^+,$$
*and the sum converges absolutely for all $t > 0$.*

*(d) At $t = 0$: the zeta-regularized mode sums $\sum_n d_n
\lambda_n^{-j}$ for integer $j \geq 1$ are finite (by meromorphic
continuation) and serve as the $\mathbb{CP}^{N-1}$ analogues of the
Epstein zeta values in Theorem K.1.*

### Why this is the correct substitute for Theorem K.1

On $S^1$, the KK spectrum is $m_n^2 = n^2/R^2$ and the mode sums
are Epstein zeta functions $E_1(-j; 1) = \sum_{n=1}^{\infty} n^{2j}$,
which vanish by Theorem K.1 for $j \geq 1$.

On $\mathbb{CP}^{N-1}$, the KK spectrum is
$\lambda_n^{(1)} = 4N(N+n-1)n/((N-1)r_3^2)$ (from
representation-theoretic formulas), with degeneracies growing as
$d_n \sim n^{2(N-2)}$. The mode sums are spectral zeta functions
$\zeta_{\mathrm{gauge}}(-j)$ for integer $j \geq 0$, which are
**finite** (by meromorphic continuation) but **not necessarily zero**.

The key difference: on $S^1/\mathbb{Z}_2$, the Epstein vanishing
$E_1(-j) = 0$ comes from the relation $1 + 2\zeta_R(0) = 0$
(the $\mathbb{Z}_2$ cancellation). On $\mathbb{CP}^{N-1}$, there is
no analogous vanishing — the mode sums are nonzero constants.

**This is not a problem.** The Epstein vanishing on $S^1$ was used in
Paper 10 to show the Goroff--Sagnotti counterterm is zero. For the
gradient-flow programme, what is needed is not the vanishing of mode
sums but their **finiteness** — the fact that the zeta-regularized
values $\zeta_{\mathrm{gauge}}(-j)$ are well-defined finite constants,
not divergent. This finiteness is guaranteed by the meromorphic
structure of spectral zeta functions on compact manifolds (Seeley 1967;
Minakshisundaram--Pleijel 1949).

### Proof strategy

1. **Eigenvalue formula:** Use the representation-theoretic spectrum
   of $\Delta_{\mathrm{Hodge}}$ on 1-forms on $\mathbb{CP}^{N-1}$
   (Ikeda--Taniguchi 1978; also derivable from the branching rules
   for $\mathrm{SU}(N) \supset \mathrm{SU}(N-1) \times \mathrm{U}(1)$).

2. **Meromorphic continuation:** Standard for spectral zeta functions
   on compact Riemannian manifolds (Seeley 1967). The poles are at
   $s = (2(N-1) - k)/2$ for $k = 0, 1, 2, \ldots$, i.e., at
   $s = N-1, N-3/2, \ldots$ Residues are Seeley--DeWitt coefficients.

3. **Numerical verification:** Compute $\zeta_{\mathrm{gauge}}(0)$
   and $\zeta_{\mathrm{gauge}}(-j)$ for $j = 1, 2, 3$ at $N = 2, 3$
   using the explicit eigenvalue formula and mpmath high-precision
   arithmetic. Compare with the Seeley--DeWitt prediction.

**Estimated effort:** 2--3 pages. The spectral theory is standard;
the $\mathbb{CP}^{N-1}$-specific computation is explicit.


---


## 3. Bridge Lemma 3: Flow Analyticity in $t$

### Statement

**Lemma B.3 (Analyticity of flowed polymer activities in flow time).**
*Let $K_k(X, V)$ be a polymer activity in Balaban's effective action
at RG step $k$, satisfying (B1): analyticity in $V$ with radius
$\rho > 0$ independent of $k$. Let $V(t)$ be the gradient-flow
evolution of $V$, satisfying*

$$\partial_t V_\ell(t) = -g_0^2\,(\partial_{V_\ell} S_W)\,V_\ell(t),
  \qquad V_\ell(0) = V_\ell. \tag{B3.1}$$

*Then the flowed polymer activity
$K_k^{(t)}(X) := K_k(X, V(t))$ is analytic in $t$ for
$|t| < t_*(k)$, where*

$$t_*(k) \geq \frac{\rho}{g_0^2\,C_{\mathrm{flow}}} > 0
  \tag{B3.2}$$

*with $C_{\mathrm{flow}} = \sup_{V \in \Omega_s}
\|\partial_{V_\ell} S_W\| < \infty$ ($k$- and $K$-independent in the
small-field domain).*

### Why this matters

If the flowed effective action is analytic in $t$ near $t = 0$, then
the small-flow-time expansion

$$K_k^{(t)}(X) = K_k^{(0)}(X)
  + t\,\partial_t K_k^{(0)}(X) + \frac{t^2}{2}\,\partial_t^2 K_k^{(0)}(X)
  + \cdots$$

**converges** (not merely asymptotic) for $|t| < t_*$. This
eliminates the primary risk of Phase 3 (the attack plan's "Risk 1:
small-flow-time expansion only asymptotic").

### Proof strategy

**Step 1 (ODE analyticity).** The gradient flow (B3.1) is an
autonomous ODE on the compact group manifold $\mathrm{SU}(N)$. By
the Cauchy--Kovalevskaya theorem, the solution $V(t)$ is analytic
in $t$ for $|t| < t_{\mathrm{ODE}}$, where $t_{\mathrm{ODE}}$ is
determined by the Lipschitz constant of the RHS. In the small-field
domain $\Omega_s$:

$$\|\partial_t V_\ell(t)\| = g_0^2\,\|(\partial_{V_\ell} S_W)
  V_\ell(t)\| \leq g_0^2 \cdot C_{\mathrm{flow}},$$

with $C_{\mathrm{flow}} \leq 4d \cdot \beta \cdot 2 = 32\beta$ (each
plaquette containing $\ell$ contributes at most $2\beta$ to the
gradient, and there are $2(d-1) = 6$ plaquettes per link in $d = 4$,
giving $C_{\mathrm{flow}} \leq 12\beta$). The ODE solution is
analytic for $|t| < 1/(g_0^2 C_{\mathrm{flow}})$.

**Step 2 (Composition).** By (B1), $K_k(X, \cdot)$ is analytic in
$V$ with radius $\rho > 0$ ($k$-independent). The map $t \mapsto V(t)$
is analytic (Step 1). The composition $t \mapsto K_k(X, V(t))$ is
analytic for $|t| < \min(t_{\mathrm{ODE}},\,
\rho / \sup_{|s| \leq t} \|dV(s)/ds\|)$.

Since $\|dV/ds\| \leq g_0^2 C_{\mathrm{flow}}$ uniformly in
$\Omega_s$, the analyticity radius in $t$ is:

$$t_* \geq \frac{\rho}{g_0^2\,C_{\mathrm{flow}}} > 0.$$

**Step 3 (Summation).** The polymer expansion $\sum_{X \ni x}
K_k^{(t)}(X)$ converges absolutely (by the Kotecký--Preiss criterion,
which holds at each $t$ since $|K_k^{(t)}(X)| \leq e^{-\kappa|X|}$
by the flow's contractivity). Absolute convergence of an analytic
family preserves analyticity: $\sum_{X \ni x} K_k^{(t)}(X)$ is
analytic in $t$ for $|t| < t_*$.

**Step 4 ($k$- and $K$-independence).** The radius $t_*$ depends on
$\rho$ ($k$-independent by (B1)), $g_0^2$ ($K$-dependent, but bounded
on the AF trajectory: $g_0^2 \leq g_{\max}^2 < \infty$), and
$C_{\mathrm{flow}}$ ($K$-independent: it depends on $\beta$ and $d$,
not on $a_0(K)$). Therefore $t_* \geq \rho/(g_{\max}^2 C_{\mathrm{flow}})
> 0$ uniformly in $k$ and $K$. $\square$

**Estimated effort:** 1--2 pages. The analytic ODE theory is standard;
the new content is verifying the radius bounds in Balaban's framework.


---


## 4. Bridge Lemma 4: KK-to-4D Projection for Composite Operators

### Statement

**Lemma B.4 (IR equivalence for composite operator matrix elements).**
*Let $\mathcal{O}(x)$ be a local gauge-invariant operator on the
lattice, and let $\mathcal{O}^{\mathrm{KK}}$ and
$\mathcal{O}^{\mathrm{std}}$ denote its expectations in the
KK-enhanced and standard lattice theories respectively. In the regime
$m_1 a \gg 1$:*

$$|\langle \mathcal{O}^{\mathrm{KK}}(x_1) \cdots
  \mathcal{O}^{\mathrm{KK}}(x_n) \rangle_c
  - \langle \mathcal{O}^{\mathrm{std}}(x_1) \cdots
  \mathcal{O}^{\mathrm{std}}(x_n) \rangle_c|
  \leq C_n\,e^{-m_1 a/2}
  \prod_{i} \|\mathcal{O}\|$$

*for connected correlators at physical separations
$|x_i - x_j| \gg a$, where $C_n$ depends on $n$ and $N$ but not
on $a/r_3$.*

### Why this is needed

Theorem 5 of the mass gap preprint projects the **spectrum**
(eigenvalues of the transfer matrix) from KK to standard theory.
For the gradient-flow programme, we also need to project **operator
matrix elements** — the Schwinger functions of composite operators
built from the flowed field strength.

### Proof strategy

The proof follows the same Feshbach mechanism as Theorem 5, extended
to matrix elements:

**Step 1.** The connected $n$-point function in the KK theory
decomposes via the partial trace over internal fields:

$$\langle \mathcal{O}(x_1) \cdots \mathcal{O}(x_n) \rangle_c^{\mathrm{KK}}
  = \langle \mathcal{O}(x_1) \cdots \mathcal{O}(x_n)
  \rangle_c^{\mathrm{red}} + O(e^{-m_1 a}),$$

where $\langle \cdot \rangle^{\mathrm{red}}$ is the expectation in
the reduced (partially traced) theory. This uses the same cluster
expansion that bounds $|\mathcal{Z}_{\mathrm{int}} /
\mathcal{Z}_{\mathrm{int}}^{(0)} - 1| \leq C e^{-m_1 a}$
(Lemma 2 of Theorem 5).

**Step 2.** For gauge-invariant operators $\mathcal{O}$ that depend
only on the 4D link variables $U$ (not on the internal connections
$A_x$), the reduced expectation equals the standard expectation up
to the measure deformation:

$$\langle \mathcal{O} \rangle^{\mathrm{red}}
  = \frac{\int \mathcal{O}[U]\,\hat{T}_{\mathrm{red}}^T(U)\,
  \prod dU_\ell}
  {\int \hat{T}_{\mathrm{red}}^T(U)\,\prod dU_\ell}.$$

The pointwise kernel bound from Theorem 5 (Lemma 2, Step 3) gives
$|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}| \leq
\bar{\epsilon}\,\hat{T}_{\mathrm{std}}$, which propagates to
correlation functions with the same $\bar{\epsilon} =
O(|\Lambda_t^1| e^{-m_1 a})$ error.

**Step 3.** For the flowed field strength $F_t$, the flow equation
is a deterministic ODE on $\mathrm{SU}(N)$; $\mathcal{O}_t(x) =
\mathrm{Tr}(F_t^2)(x)$ depends on $U_\ell$ for links $\ell$ within
a ball of radius $O(\sqrt{t})$ around $x$ (the flow's smoothing
radius). This is a local gauge-invariant operator satisfying the
hypotheses of Step 2.

**Step 4.** Combine Steps 1--3 for connected $n$-point functions.
The connected correlator involves cluster expansion techniques
(Penrose tree-graph identity) that preserve the $O(e^{-m_1 a/2})$
error per operator insertion. The factor $e^{-m_1 a/2}$ (rather than
$e^{-m_1 a}$) accounts for the volume factor $|\Lambda_t^1|$ absorbed
as in Theorem 5 Step 4.

**Estimated effort:** 2--3 pages. The mechanism is the same as
Theorem 5; the new content is verifying it extends to operator
insertions (not just partition function ratios).


---


## 5. Bridge Lemma 5: Flowed Correlator Cauchy Estimate

### Statement

**Lemma B.5 (Cauchy convergence of flowed Schwinger functions).**
*For each fixed $t > 0$, $n \geq 1$, and $f \in
\mathcal{S}(\mathbb{R}^{4n})$, the lattice flowed Schwinger
functions satisfy:*

$$|S_{n,t}^{(K+1)}(f) - S_{n,t}^{(K)}(f)|
  \leq C_n(t)\,\|f\|_{p_N}\,g_K^4\,(a_0(K)\Lambda)^s\,
  e^{-t/(a_0(K))^2} \tag{B5.1}$$

*where $s \geq 2$ (from the deviation order bound) and the factor
$e^{-t/a_0(K)^2}$ comes from the flow's UV smoothing. The sum
$\sum_K$ of the RHS converges faster than doubly exponentially.*

### Why this matters

This is the flowed analogue of the Cauchy argument in Theorem M.2.1.
The additional flow factor $e^{-t/a^2}$ provides super-exponential
improvement over the unflowed case, making convergence at fixed
$t > 0$ essentially trivial.

### Proof strategy

Adapt the telescoping argument of Section 5.4 to flowed correlators.
The RG step $K \to K+1$ changes the effective action by
$\delta S_K = O(g_K^4 \hat{\Delta}_K^s)$. The flowed correlator
at fixed $t > 0$ has additional suppression: the flow propagator
$e^{-tp^2}$ kills UV modes at $|p| > 1/\sqrt{t}$, and
$1/\sqrt{t} \ll 1/a_0(K)$ for $t \gg a_0(K)^2$ (which holds for
all but finitely many $K$, since $a_0(K) \to 0$). The UV modes that
drive the RG are precisely the modes suppressed by the flow, giving
the factor $e^{-t/a_0(K)^2}$.

For the finitely many $K$ where $a_0(K)^2 \geq t$ (the lattice is
coarser than the flow scale), the unflowed bound
$O(g_K^4 \hat{\Delta}_K^s)$ suffices, and the sum over these finitely
many terms is bounded.

**Estimated effort:** 1 page. Essentially a corollary of the existing
RG machinery plus the flow's UV suppression.


---


## 6. Master Lemma: The $t \to 0^+$ Limit Exists

### Statement

**Theorem B.6 (Existence of renormalized composite operator).**
*For the SU($N$) Yang--Mills theory constructed in the preprint
(Theorem 8, Section 5.7), the renormalized two-point function*

$$S_2^{\mathrm{ren}}(x, y) := \lim_{t \to 0^+}
  \frac{S_{2,t}^c(x, y)}{c_1(t)^2}$$

*exists as a finite tempered distribution on $\{(x,y) : x \neq y\}$,
where $c_1(t) = (8\pi^2 t^2)^{-1}[1 + \bar{c}_1 \bar{g}^2(q) +
O(\bar{g}^4)]$ with $q = (8t)^{-1/2}$ is the perturbative
small-flow-time coefficient (Lüscher 2010).*

### Proof structure (using the bridge lemmas)

**Step 1 (Flowed theory well-defined at $t > 0$).**
By Lemma B.5 + the OS axiom verification of Section 5.7(f), the
continuum flowed Schwinger functions $S_{n,t}(f)$ exist for all
$t > 0$, are unique (Cauchy convergence), and satisfy OS0'--OS4.

**Step 2 (Analyticity in $t$).**
By Lemma B.3, the flowed effective action is analytic in $t$ for
$|t| < t_* > 0$ ($k$- and $K$-independent). The continuum flowed
Schwinger functions inherit analyticity in $t$ (as limits of analytic
functions with uniform convergence from Lemma B.5). Therefore the
small-flow-time expansion converges for $0 < t < t_*$.

**Step 3 (Operator structure at small $t$).**
In the convergent small-flow-time expansion, the leading contribution
to $S_{2,t}^c(x,y)$ is from the unique dimension-4 operator
$\mathrm{Tr}\,F^2$ (no mixing — Section 5.3.1 of the preprint:
$S_{\mathrm{YM}}$ is the unique dim-4 gauge-invariant $\mathcal{C}$-even
operator). Subleading contributions are from dimension-$\geq 6$
operators, all with $\mathrm{dev} \geq 2$ (Section 5.6, Part III),
contributing $O(t \cdot g^4 \hat{\Delta}^2)$ to the rescaled
correlator.

**Step 4 (Rescaling absorbs the leading singularity).**
The leading singularity is $S_{2,t}^c(x,y) \sim c_1(t)^2 \cdot
\langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y) \rangle
+ O(t)$. Dividing by $c_1(t)^2$ removes the $t$-dependent prefactor.
The remainder is $O(t)$ by the convergent expansion (Step 2) and the
dimension-6 suppression (Step 3).

**Step 5 (The limit exists).**
$$\frac{S_{2,t}^c(x,y)}{c_1(t)^2}
  = \langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y) \rangle
  + O(t)$$

by Steps 2--4. As $t \to 0^+$, the $O(t)$ remainder vanishes and the
limit exists. The limit defines a finite tempered distribution on
$\{x \neq y\}$ because the OS0' bounds on the flowed Schwinger
functions (uniform in $t$ after rescaling) pass to the limit. $\square$

### What remains to make this rigorous

| Step | Status | What's needed |
|:-----|:-------|:-------------|
| 1 | Lemma B.5 (1 page) | Adapt Theorem M.2.1 to flowed correlators |
| 2 | Lemma B.3 (1--2 pages) | Verify ODE analyticity + composition |
| 3 | Already proved (§5.3, §5.6) | The dim-6 classification is in the preprint |
| 4 | Standard (Lüscher 2010) | The perturbative $c_1(t)$ is known to 3 loops |
| 5 | Follows from 1--4 | Assembly |

**Total new work for Theorem B.6:** ~5 pages of new lemmas
(B.1--B.5) plus ~3 pages of assembly = **~8 pages**.


---


## 7. Gap-by-Gap Strategy

### Gap G4(a): Local field operators (Conjecture L.1)

**Strategy:** Theorem B.6 constructs the renormalized two-point
function $S_2^{\mathrm{ren}}$. The operator
$[\mathrm{Tr}\,F^2]_R(x)$ is then defined as the operator-valued
distribution satisfying

$$\langle \Omega | [\mathrm{Tr}\,F^2]_R(f)\,
  [\mathrm{Tr}\,F^2]_R(g) | \Omega \rangle
  = S_2^{\mathrm{ren}}(f \otimes g).$$

The GNS reconstruction from $S_2^{\mathrm{ren}}$ (plus the
higher-point functions $S_n^{\mathrm{ren}}$ constructed analogously)
gives the operator on a common dense domain.

**Remaining sub-gaps:**
- Higher-point renormalized Schwinger functions $S_n^{\mathrm{ren}}$
  for $n \geq 3$: same method, with the small-flow-time expansion at
  each $n$ controlled by the linked cluster theorem and the
  $\mathrm{dev} \geq 2$ bound.
- Operators beyond $\mathrm{Tr}\,F^2$: higher Casimirs
  $\mathrm{Tr}\,F^n$ and operators with covariant derivatives
  $\mathrm{Tr}\,(DF)^2$ etc. Each has a lattice representative and
  the same gradient-flow construction applies.

**Estimated effort:** Theorem B.6 gives the $n = 2$ case. Extension
to all $n$ and all operator types: ~5 additional pages.

### Gap G4(b): AF short-distance match (Conjecture L.2)

**Strategy:** Automatic from the small-flow-time expansion. The
perturbative Wilson coefficients $c_k(t)$ (Lüscher 2010;
Harlander--Neumann 2016, 2022; Artz et al. 2019) encode the AF
prediction. Theorem B.6 Step 4 shows that
$S_2^{\mathrm{ren}}(x,y) = \lim_{t \to 0} S_{2,t}^c/c_1^2$
inherits the short-distance behavior from $c_1(t)$, which is
$c_1(t) \sim t^{-2}(\ln)^{-1}$. The resulting
$S_2^{\mathrm{ren}}(x,y) \sim |x-y|^{-8} (\ln)^{-2}$ is the
AF prediction.

**Remaining sub-gaps:** Verify that the non-perturbative remainder
(controlled by $\mathrm{dev} \geq 2$ operators) does not modify
the leading short-distance power. This follows from the fact that
dimension-$\geq 6$ operators contribute $O(|x-y|^{-6})$ or softer,
which is subleading to $|x-y|^{-8}$.

**Estimated effort:** ~2 pages beyond Theorem B.6.

### Gap G4(c): Stress tensor (Conjecture L.3)

**Strategy:** Apply Suzuki's formula (PTEP 2013:083B03):

$$T_{\mu\nu}^R(x) = \lim_{t \to 0^+}\left[
  c_1(t)\,U_{\mu\nu}(t,x) + c_2(t)\,\delta_{\mu\nu}\,E(t,x)
  + c_3(t)\,\delta_{\mu\nu}\,\langle E(t) \rangle\right]$$

where $U_{\mu\nu}(t,x)$ and $E(t,x)$ are specific flowed operators
and $c_1, c_2, c_3$ are perturbatively known coefficients.

Given the $t \to 0$ limit from Theorem B.6, this reduces to verifying:
1. Conservation $\partial^\mu T_{\mu\nu} = 0$: from lattice Ward
   identities (exact at each $a$, preserved in the limit).
2. Trace anomaly: from the Spiridonov--Chetyrkin identity +
   Theorem B.6.
3. Positivity $H_{\mathrm{OS}} \geq 0$: already proved (Section 5.7).

**Estimated effort:** ~3 pages beyond Theorem B.6.

### Gap G4(d): OPE (Conjecture L.4)

**Strategy:** At fixed $t > 0$, the operator product
$\mathcal{O}_t(x) \mathcal{O}_t(y)$ is UV-finite for all $x, y$.
The leading OPE channel is the identity operator (coefficient
$\sim |x-y|^{-8}$). The subleading channel is
$[\mathrm{Tr}\,F^2]_R$ (coefficient $\sim |x-y|^{-4}$). Higher
channels involve dim-$\geq 6$ operators with $\mathrm{dev} \geq 2$.

Taking $t \to 0$ using Theorem B.6 + analyticity in $t$ (Lemma B.3)
gives the OPE at leading order. Full OPE convergence (all orders)
requires controlling the tail of the sum, which is bounded by the
spectral gap (the mass gap $\Delta_\infty > 0$ provides the IR cutoff).

**Estimated effort:** ~5 pages for leading-order OPE; full OPE is
harder and may be a separate paper.


---


## 8. Implementation Order and Dependencies

```
B.1 (Seeley-DeWitt on CP^{N-1})     ──┐
                                       ├──→ B.2 (Mode sum regularity)
B.3 (Flow analyticity in t)          ──┤
                                       ├──→ Theorem B.6 (t → 0 limit)
B.4 (KK → 4D operator projection)   ──┤
                                       │
B.5 (Flowed Cauchy estimate)         ──┘

Theorem B.6 ──→ L.1 (composite operators)
             ──→ L.2 (AF matching)
             ──→ L.3 (stress tensor)
             ──→ L.4 (OPE, leading order)
```

**Parallelizable:** B.1, B.3, B.4, B.5 can all be proved
independently. B.2 uses B.1. Theorem B.6 uses all five.

**Total estimated new work:** ~20 pages of lemmas + assembly,
organized as 1--2 papers.

**Critical path:** B.3 (analyticity in $t$) → Theorem B.6 Step 2
→ Step 5. If B.3 fails (the flowed activities are not analytic in
$t$, only smooth), the small-flow-time expansion is asymptotic, and
the $t \to 0$ limit requires a separate Borel summability argument.
This is the one genuine risk that the QG5D scaffold does not
fully eliminate.

**Fallback if B.3 fails:** The flowed Schwinger functions at $t > 0$
still exist and satisfy OS axioms (Lemma B.5 alone suffices). The
family $\{[\mathrm{Tr}\,F^2]_t\}_{t > 0}$ then serves as a
one-parameter family of well-defined operators approaching the
local operator as $t \to 0$, with the correct AF divergence
structure. This is the "enhanced weak form of L.1" described in
Section 6.3 of `formal-argument.md` — already a substantial advance
over the literature.
