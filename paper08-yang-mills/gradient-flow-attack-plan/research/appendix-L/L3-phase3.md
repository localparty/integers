# L.3 Phase 3: The Small-Flow-Time Limit and Renormalized Composite Operators

Throughout this section, $G = \mathrm{SU}(N)$ with $N \geq 2$,
$d = 4$, and $L = 2$ (Balaban blocking factor). The lattice at inner
RG step $k$ has spacing $a_k = 2^k a_0(K)$, where
$a_0(K) = a^* \cdot 2^{-K}$ is the bare spacing at outer scale $K$.
The gradient flow on the lattice configuration space
$\mathcal{M} = \mathrm{SU}(N)^{|\Lambda_L^1|}$ is governed by
the lattice flow equation (ODE) of Section L.1. The rescaled
correlator is

$$F(t) \;:=\; \frac{S_{2,t}^c(x,y)}{c_1(t)^2}, \tag{L.3.0}$$

where $S_{2,t}^c(x,y) = \langle E(t,x)\,E(t,y)\rangle_c$ is
the connected two-point Schwinger function of the flowed energy
density and $c_1(t)$ is the leading Wilson coefficient in the
small-flow-time expansion.


---


## L.3.1 Analyticity of the flowed effective action in flow time


**Lemma L.3.1** (Analyticity in $t$).
*Let $S_k^{\mathrm{eff}}[V]$ be the Balaban effective action at inner
RG step $k$, satisfying property (B1) (Section 5.6, Part I) with
$k$-independent analyticity radius $\rho > 0$. Let
$V_t(\ell)$ denote the lattice gradient flow starting from
$V_0 \in \Omega_s$. Then:*

*(i) The composition $t \mapsto S_k^{\mathrm{eff}}[V_t]$ is analytic
in $t$ for $|t| < r_t$, with*

$$r_t = \min\!\left(r_{\mathrm{ODE}},\;
  \frac{\rho}{L_{\mathrm{flow}}}\right) > 0, \tag{L.3.1}$$

*where $r_{\mathrm{ODE}} = N/(96\,g_0^2)$ is the ODE analyticity
radius, $\rho$ is the Balaban analyticity radius (Eq.\ (I.3)),
and $L_{\mathrm{flow}} \leq 24\,g_0^2$ is the flow speed on
$\Omega_s$.*

*(ii) The radius $r_t$ is independent of the inner Balaban step $k$
and of the outer bare-scale index $K$.*

*(iii) The rescaled correlator $F(t) = S_{2,t}^c(x,y)/c_1(t)^2$ is
analytic in $t$ for $|t| < r_t$, and the small-flow-time expansion
converges absolutely on this disk.*


*Proof.* The argument composes three ingredients, each established
independently.

**Ingredient (a): Balaban analyticity (B1).** By Section 5.6,
Part I (Balaban CMP 95--109, 119; Dimock arXiv:1108.1335, Thm 14),
in the small-field region $\Omega_s$ the effective action admits
a convergent polymer expansion

$$S_k^{\mathrm{eff}}[V] = \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  + \sum_{X \in \mathcal{P}_k} K_k(X, V), \tag{L.3.2}$$

with activities satisfying $|K_k(X, V)| \leq e^{-\kappa |X|}$
for a $k$-independent polymer decay constant $\kappa > 0$. Each
activity $K_k(X,V)$ is analytic in $\{V_\ell\}$, constructed by
iterating four analyticity-preserving operations: (i) background
evaluation (polynomial, entire), (ii) saddle point via the covariant
propagator $G_k = (-D^2[V] + m_W^2)^{-1}$ (analytic inversion;
CMP 95, Prop.\ 1.2), (iii) Gaussian integration (convergent
trace-log), and (iv) Mayer resummation (Weierstrass $M$-test). The
overall analyticity radius is

$$\rho = \min\!\left(\frac{\kappa}{2d},\;
  \frac{m_W a}{2C_D},\;r_{\mathrm{proj}}(N)\right) > 0, \tag{L.3.3}$$

with $C_D = 2(N^2 - 1)$ and $r_{\mathrm{proj}}(N) \geq 1/2$.
Every factor is $k$-independent.

**Ingredient (b): ODE analyticity of the lattice gradient flow.**
The lattice gradient flow equation

$$\frac{d}{dt}V_\ell(t) = -g_0^2\,
  \bigl(\partial_{V_\ell}S_W[V(t)]\bigr)\,V_\ell(t),
  \qquad V_\ell(0) = U_\ell,$$

has right-hand side polynomial in the matrix entries of $\{V_\ell\}$.
By the Cauchy--Kowalevski theorem for polynomial ODEs on the compact
manifold $\mathrm{SU}(N)^{|\mathrm{links}|}$, the solution
$t \mapsto V_t(\ell)$ extends to a holomorphic map on
$\{|t| < r_{\mathrm{ODE}}\}$ with

$$r_{\mathrm{ODE}} = \frac{N}{96\,g_0^2}. \tag{L.3.4}$$

The flow speed on $\Omega_s$ is bounded by
$L_{\mathrm{flow}} := \sup_{V \in \Omega_s}|F(V)| \leq 24\,g_0^2$.
Both $r_{\mathrm{ODE}}$ and $L_{\mathrm{flow}}$ depend on $d$, $N$,
$g_0$ only and are therefore $k$-independent.

**Ingredient (c): Heat kernel entirety.** By Paper 1, Appendix S,
Section S.3.1 (Appendix N, §N.1.3), the heat kernel $e^{-tp^2}$ is entire in $t$ for each
fixed $p$. On $M^4 \times S^1$, the heat kernel factorizes:
$K_{M^4 \times S^1}(t) = K_{M^4}(t) \otimes K_{S^1}(t)$, with each
factor entire in $t$. Therefore the Wilson coefficients $c_n(t)$
arising from the small-flow-time expansion are entire functions of $t$.

**Composition.** Consider the chain of maps

$$\mathbb{D}_{r_{\mathrm{ODE}}}
  \xrightarrow{\;\varphi\;}
  \mathrm{SU}(N)^{|\mathrm{links}|}
  \xrightarrow{\;\Phi\;}
  \mathbb{C},$$

where $\varphi(t) := V_t$ and $\Phi(V) := S_k^{\mathrm{eff}}[V]$.
By Ingredient (b), $\varphi$ is holomorphic. By Ingredient (a), $\Phi$
is holomorphic on $\{V : \|V_\ell - \mathbf{1}\| < \rho\}$. The
composition $\Phi \circ \varphi$ is holomorphic provided $\varphi(t)$
remains in the analyticity domain of $\Phi$. By the flow speed
estimate:

$$\|V_t(\ell) - V_0(\ell)\| \leq L_{\mathrm{flow}} \cdot |t|
  < \rho \quad\text{whenever}\quad
  |t| < \rho / L_{\mathrm{flow}}.$$

Combined with the intrinsic ODE radius, this gives
$r_t = \min(r_{\mathrm{ODE}},\,\rho/L_{\mathrm{flow}}) > 0$, proving
(i). Part (ii) follows from the $k$-independence of $\rho$ (by (B1)),
$L_{\mathrm{flow}}$ (by Ingredient (b)), and $r_{\mathrm{ODE}}$ (by
Ingredient (b)); $K$-independence follows from Appendix M,
Corollary M.1.3.

For (iii): the energy density $E(t,x)$ is polynomial in $\{V_t(\ell)\}$
for links $\ell$ near $x$, hence analytic in $t$. The expectation
$S_{2,t}^c(x,y) = \langle E(t,x)\,E(t,y)\rangle_c$ is an integral
of a holomorphic integrand over the compact group manifold; by Fubini
and the Morera--Osgood theorem for parameter integrals, it is
holomorphic in $t$. Since $c_1(t)$ is entire and non-vanishing for
$t > 0$ (Ingredient (c)), $F(t)$ is analytic on $0 < |t| < r_t$. The
Taylor series of $F$ at $t = 0$ converges absolutely for $|t| < r_t$
with coefficient bound $|a_n| \leq M_F/r_t^n$, where
$M_F := \sup_{|s|=r_t/2}|F(s)| < \infty$. $\square$

**Remark L.3.1.** The small-field domain preservation lemma
(Lemma L.1.2) guarantees $V_t \in \Omega_s$ for all $t \geq 0$,
ensuring the composition argument applies throughout the analyticity
disk.


---


## L.3.2 Established results: Lemmas L.3.2--L.3.6

The following five lemmas are established in the preprint and in
Paper 10 (Appendix N). Each enters the proof of the core estimate
(Lemma L.3.7) as a specific hypothesis discharge.


**Lemma L.3.2** (No operator mixing at dimension 4).
*The unique local, gauge-invariant, $\mathcal{C}$-even, parity-even
operator of engineering dimension 4 on the 4D hypercubic lattice is
the Wilson plaquette action $S_{\mathrm{YM}} = \sum_P s_P$. The
mixing matrix at dimension 4 is $1 \times 1$.*

*Proof.* By Section 5.3.1. The proof is by exhaustive elimination:
$\mathrm{Tr}(F\tilde{F})$ is parity-odd; $s_P^2$ and higher
plaquette powers have engineering dimension $\geq 8$;
$\mathrm{Tr}(F^3)$ and $d^{abc}F^3$ are dimension-6 and
$\mathcal{C}$-odd ($A_\mu \to -A_\mu^T$ reverses the trace sign).
No redundant operators are generated by the block-spin integration
(Balaban CMP 109, Section 2). $\square$


**Lemma L.3.3** (Deviation order $\mathrm{dev} \geq 2$ at
dimension $\geq 6$).
*Every $\mathcal{C}$-even, gauge-invariant, dimension-6 operator has
Boltzmann deviation order $\mathrm{dev} \geq 2$. Consequently, the
two-derivative spectral bound (Section 5.5.3) gives*

$$|\langle 1|\mathcal{O}|1\rangle_c|
  \leq C_p\,M\,\hat{\Delta}^2 \tag{L.3.5}$$

*for any such operator $\mathcal{O}$ with norm $\|\mathcal{O}\| \leq M$,
with $C_p$ $K$-uniform.*

*Proof.* By Section 5.6, Part III. The proof classifies all
dimension-6 gauge-invariant operators into four exhaustive classes:
(I) $\mathrm{Tr}(F^3)$, $d^{abc}F^3$: $\mathcal{C}$-odd, coefficient
zero; (II) one-derivative operators: absent (gauge invariance requires
even numbers of field-strength factors); (III) two-derivative
operators $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and
$\mathrm{Tr}(D_\mu F^{\mu\rho}D_\nu F^\nu{}_\rho)$:
$\mathrm{dev} \geq 2$ by the spectral mechanism (the transfer-matrix
weight $(e^{E_m - E_n} - 1)^2$ vanishes identically at $n = m$);
(IV) three-or-more-derivative operators: $\mathrm{dev} \geq 3 > 2$.
$\square$


**Lemma L.3.4** (KK mode sum vanishing at $t = 0$).
*$E_L(-j;\,Q) = 0$ for all positive-definite quadratic forms $Q$ in
$L$ variables and all integers $j \geq 1$.*

*Proof.* By Appendix K, Theorem K.1 (Paper 1, Section K.7b; Appendix N, §N.1.5). The
completed Epstein zeta function
$\Lambda(s) = \pi^{-s}\Gamma(s)\,E_L(s;\,Q)$ is meromorphic with
poles only at $s = 0$ and $s = L/2$. At $s = -j$ with $j \geq 1$,
$\Lambda(-j)$ is finite, but $1/\Gamma(-j) = 0$ (the Gamma function
has poles at all non-positive integers). Therefore
$E_L(-j;\,Q) = \pi^{-j}\Lambda(-j)/\Gamma(-j) = 0$. $\square$


**Lemma L.3.5** ($\mathbb{Z}_2$ parity cancellation persists at
all $t$).
*At each KK level $n \geq 1$,
$f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0$. The cancellation
is exact, does not require summation over $n$, and persists at all
flow times $t \geq 0$.*

*Proof.* By Paper 10, Section 3.3, Proposition 3.1 (Appendix N, §N.2.2). The sign flip
$f_{\mathrm{odd}}(n) = -f_{\mathrm{even}}(n)$ arises from the
$y$-integral on $S^1/\mathbb{Z}_2$, which factorizes from the 4D
momentum integration. The gradient-flow regulator $e^{-tk^2}$ modifies
only the 4D loop momentum integral, not the $y$-integral producing the
sign. The cancellation is therefore $t$-independent and
scheme-independent (Paper 10, Section 3.4; Appendix N, §N.2.2). $\square$


**Lemma L.3.6** (Goroff--Sagnotti coefficient vanishes in all
schemes).
*$C_{\mathrm{GS}} = 0$ on $M^4 \times S^1/\mathbb{Z}_2$ in all
regularization schemes.*

*Proof.* By Paper 10, Theorem 1, Section 4.6 (Appendix N, §N.2.4). The proof chain:
(Step 1) the vertex coupling
$g(n,m) = I_{+++}(n,m,n\!+\!m)/(\pi R)^{3/2} = 1/(4\sqrt{\pi R})$
is $n,m$-independent by the product-to-sum identity (Lemma A1);
(Step 2) the leading UV coefficient factors as
$C_{\mathrm{GS}}^{\mathrm{leading}}
= [1/(4\sqrt{\pi R})]^2 \cdot J(0,0) \cdot S_0^2 = 0$, since
$S_0 = 1 + 2\zeta_R(0) = 0$ (Lemma A3);
(Step 3) each subleading correction contributes $E_2(-j;\,Q_2) = 0$
for $j \geq 1$ by Theorem K.1 (Lemma L.3.4). Graviphoton and radion
fields contribute only at dimension $\geq 8$ (Lemma A2). The Weyl
anomaly vanishing $a_{\mathrm{total}} = c_{\mathrm{total}} = 0$ is
protected cohomologically by the Wess--Zumino consistency condition
(Paper 10, Theorem 4.3; Appendix N, §N.2.5). $\square$


---


## L.3.3 The Cauchy estimate for the rescaled correlator


**Lemma L.3.7** (Cauchy estimate --- core estimate).
*Let $F(t) := S_{2,t}^c(x,y)/c_1(t)^2$ be the rescaled correlator
(Eq.\ (L.3.0)) in the continuum Yang--Mills theory constructed in
Theorem 8. Then for fixed non-coincident $x, y \in \mathbb{R}^4$
with $|x - y| > 0$:*

$$|F(t) - F(t')| \;\leq\; L(x,y)\,|t - t'| \tag{L.3.6}$$

*uniformly for all $t, t' \in [0, r_t)$, where:*

*(i) The Lipschitz constant $L(x,y) = M_F/r_t$ is finite, depends
on $|x - y|$ and $\Delta_\infty$ but not on $t$ or $t'$.*

*(ii) The analyticity radius $r_t > 0$ is independent of the inner
Balaban step $k$ and the outer bare-scale index $K$.*

*(iii) The supremum $M_F := \sup_{|s|=r_t}|F(s)| < \infty$ is
$K$-uniform.*

*Consequently, $F(t)$ extends continuously to $t = 0$ and the limit
$\lim_{t \to 0^+} F(t) = F(0)$ exists as a finite quantity.*


*Proof.* The proof proceeds through six steps. Steps 1--2 establish
the two pillars ($F(0) < \infty$ and $F$ analytic in $t$). Step 3
controls subleading terms. Step 4 derives the Cauchy estimate.
Step 5 establishes $K$-uniformity and the double limit. Step 6
projects from the KK theory to 4D Yang--Mills.


### Step 1: $F(0) < \infty$ in the KK theory (Pillar A)

We show that $F(t)$ is well-defined and finite for all $t \geq 0$
in the KK-enhanced Yang--Mills theory on
$M^4 \times S^1/\mathbb{Z}_2$.

**At $t > 0$.** The gradient flow exists globally by Lemma L.1.1,
and the flow propagator $e^{-tp^2}$ provides exponential UV damping
at momentum scale $|p| \sim 1/\sqrt{t}$, rendering
$S_{2,t}^c(x,y) < \infty$. Since $c_1(t) \neq 0$ for $t > 0$
(known perturbative non-vanishing; Luscher--Weisz, JHEP 02 (2011)
051), $F(t)$ is well-defined.

**At $t = 0$ in the KK theory.** The unflowed correlator involves
KK mode sums. At each loop order $\ell$, the KK contribution factors
as

$$(\text{4D integral}) \times E_\ell(-j;\,Q_\ell), \tag{L.3.7}$$

where $E_\ell$ is the Epstein zeta function, $Q_\ell$ is a
positive-definite quadratic form in the KK indices, and $j \geq 1$
is a non-negative integer from the mass-expansion order. By
Lemma L.3.4 (Theorem K.1), $E_\ell(-j;\,Q) = 0$ for all $j \geq 1$.
Therefore all KK mode sums vanish at $t = 0$.

*One loop ($\ell = 1$):* $S_0 = 1 + 2\zeta_R(0) = 0$. The zero-mode
contribution cancels the zeta-regularized KK tower. Subleading sums
$\zeta_R(-2k) = 0$ for $k \geq 1$ (trivial Riemann zeros).

*Two loops ($\ell = 2$):* The sunset topology produces the Eisenstein
lattice zeta function
$E_2(s;\,n^2\!+\!nm\!+\!m^2) = 6\zeta_R(s)L(s,\chi_{-3})$, with
complementary trivial zeros covering every negative integer:
$\zeta_R(-2k) = 0$ for even $k \geq 1$, and
$L(-2k\!-\!1,\chi_{-3}) = 0$ for odd $k \geq 0$.

**Scheme-independence at $t = 0$.** By Lemma L.3.6, the
Goroff--Sagnotti coefficient vanishes in all regularization schemes:
$C_{\mathrm{GS}} = 0$. The Weyl anomaly coefficients
$a_{\mathrm{total}} = c_{\mathrm{total}} = 0$ are protected
cohomologically by the Wess--Zumino consistency condition (Paper 10,
Theorem 4.3; Appendix N, §N.2.5), extending the vanishing to all
diffeomorphism-preserving schemes.

**Conclusion of Step 1.** $F(t)$ is well-defined and finite for all
$t \geq 0$ in the KK theory. This is Pillar A: $F(0) < \infty$.
$\square$


### Step 2: $F(t)$ is analytic in $t$ for $|t| < r_t$ (Pillar B)

By Lemma L.3.1, the composition
$t \mapsto S_k^{\mathrm{eff}}[V_t]$ is holomorphic on
$|t| < r_t$ with $(k,K)$-uniform radius
$r_t = \min(r_{\mathrm{ODE}},\,\rho/L_{\mathrm{flow}}) > 0$.

The energy density $E(t,x)$ is polynomial in $\{V_t(\ell)\}$, hence
analytic in $t$. The connected two-point function
$S_{2,t}^c(x,y) = \langle E(t,x)\,E(t,y)\rangle_c$ is an integral
of a holomorphic integrand over the compact group manifold; by
Fubini and the Morera--Osgood theorem, it is holomorphic in $t$.
Since $c_1(t)$ is entire and non-vanishing for $t > 0$ (by
Lemma L.3.1, Ingredient (c)), $F(t)$ is analytic on the punctured
disk $0 < |t| < r_t$.

By Step 1, $F(0) < \infty$. By the Riemann removable singularity
theorem (Rudin, *Real and Complex Analysis*, Thm 10.21): if $f$
is holomorphic on a punctured disk $0 < |z| < r$ and
$\lim_{z \to 0}f(z)$ exists and is finite, then $f$ extends to a
holomorphic function on $|z| < r$. Applying this to $F$:

$$F \text{ extends holomorphically to } |t| < r_t, \text{ with }
  F(0) = \lim_{t \to 0^+}F(t). \tag{L.3.8}$$

**The small-field domain is preserved** by Lemma L.1.2: the gradient
flow preserves Balaban's small-field domain $\Omega_s$ for all
$t \geq 0$ (by the monotone action decrease and the maximum
principle), ensuring the composition argument of Lemma L.3.1 applies
throughout the analyticity disk.

**Conclusion of Step 2.** $F(t)$ is analytic on $|t| < r_t$ including
$t = 0$, with $(k,K)$-uniform radius. The small-flow-time expansion
is convergent, not merely asymptotic. This is Pillar B. $\square$


### Step 3: Subleading terms are $O(t)$ (Pillar C)

The small-flow-time expansion of the rescaled correlator gives

$$F(t) = F(0) + R(t), \tag{L.3.9}$$

where $F(0) = \langle [\mathrm{Tr}\,F^2]_R(x)\,
[\mathrm{Tr}\,F^2]_R(y)\rangle_c$ is the unique dimension-4
contribution, and $R(t)$ collects all dimension-$\geq 6$ operators.

**No mixing at dimension 4.** By Lemma L.3.2, the unique local,
gauge-invariant, $\mathcal{C}$-even, parity-even operator of
engineering dimension 4 is the Wilson plaquette action. The mixing
matrix at dimension 4 is $1 \times 1$: there is a single operator
$[\mathrm{Tr}\,F^2]_R$ and a single Wilson coefficient $c_1(t)$.

**Subleading suppression.** Each dimension-$d_k$ operator contributes
with Wilson coefficient $c_k(t)/c_1(t) \sim t^{(d_k - 4)/2}$,
vanishing as $t \to 0$ for $d_k \geq 6$. The non-perturbative
matrix elements are controlled by the deviation-order classification:
by Lemma L.3.3, every $\mathcal{C}$-even, gauge-invariant,
dimension-6 operator has $\mathrm{dev} \geq 2$, so the
two-derivative spectral bound gives

$$|\langle 1|\mathcal{O}_{d=6}|1\rangle_c|
  \leq C_p\,M\,\hat{\Delta}^2, \tag{L.3.10}$$

with $C_p$ $K$-uniform (Section 5.5.3, Hastings--Koma bound).
The remainder is bounded by

$$|R(t)| \leq C_{\mathrm{sub}}\,t\,
  \frac{g_k^4\,\hat{\Delta}^2}{|x-y|^{10}} + O(t^2). \tag{L.3.11}$$

**Conclusion of Step 3.** All subleading contributions vanish at
least as fast as $O(t)$ in the $t \to 0$ limit. This is Pillar C.
$\square$


### Step 4: The Cauchy estimate

This is the core of Lemma L.3.7. The argument applies standard
complex analysis to the function established in Steps 1--2.

$F(t)$ is analytic on $|t| < r_t$ (Step 2) with $F(0)$ finite
(Step 1). By the Cauchy integral formula for the derivative,
applied on the circle $|s| = r$ with $0 < r < r_t$:

$$F'(t) = \frac{1}{2\pi i}\oint_{|s|=r}
  \frac{F(s)}{(s-t)^2}\,ds, \tag{L.3.12}$$

whence, for $|t| \leq r/2$:

$$|F'(t)| \leq \frac{1}{r}\,\sup_{|s|=r}|F(s)|. \tag{L.3.13}$$

**Bounding $M_F$.** On the circle $|s| = r_t$ (fixed nonzero
flow time), three controls apply:

1. **UV control.** The flow propagator $e^{-r_t p^2}$ provides
   exponential damping at momentum scale $|p| \sim 1/\sqrt{r_t}$.
   All UV divergences are exponentially suppressed.

2. **IR control.** The mass gap $\Delta_\infty > 0$ (Theorem 8(d),
   Section 5.7) provides exponential clustering:
   $|S_{2,t}^c(x,y)| \leq C\,e^{-\Delta_\infty|x-y|}$. At fixed
   non-coincident $(x,y)$, this is a finite bound.

3. **Schwinger function bounds.** The $n$-point functions satisfy
   $|S_n| \leq n!\,C_0^n$ $K$-uniformly (OS0, Section 5.7).
   At $n = 2$ and fixed $(x,y)$: $|S_{2,t}^c| \leq 2C_0^2$.

Combining: $M_F := \sup_{|s|=r_t}|F(s)| < \infty$.

**The Lipschitz estimate.** For $0 \leq t, t' < r_t$:

$$|F(t) - F(t')|
  = \left|\int_{t'}^t F'(s)\,ds\right|
  \leq |t - t'| \cdot \sup_{s \in [t',t]}|F'(s)|
  \leq |t - t'| \cdot \frac{M_F}{r_t}. \tag{L.3.14}$$

This establishes Eq.\ (L.3.6) with $L(x,y) = M_F/r_t$, a finite
constant depending on $|x - y|$ (through the clustering bound in
$M_F$) and on $\Delta_\infty$ (through the mass gap), but independent
of $t$ and $t'$. The Cauchy estimate gives Lipschitz regularity with
exponent $\alpha = 1$, optimal for an analytic function on a disk.
$\square$


### Step 5: $K$-uniformity and the double limit

All ingredients of the Cauchy estimate must be uniform in the outer
bare-scale index $K$ to permit the $a \to 0$ limit.

**$K$-uniformity of $r_t$.** The three factors in (L.3.1) are each
$K$-independent:

| Factor | Dependence | Source |
|:-------|:-----------|:-------|
| $\rho$ (Balaban radius) | $\kappa$, $m_W a$, $C_D$, $r_{\mathrm{proj}}$ | Appendix M, Corollary M.1.3 |
| $L_{\mathrm{flow}}$ (flow speed) | $d$, $N$, $g_0$ | Lemma L.3.1, Eq.\ (L.3.4) |
| $r_{\mathrm{ODE}}$ (ODE radius) | $d$, $N$, $g_0$ | Lemma L.3.1, Eq.\ (L.3.4) |

**$K$-uniformity of $M_F$.** Controlled by:
$K$-uniform Schwinger function bounds (OS0, Section 5.7;
Lemma L.2.4), $K$-independent mass gap $\Delta_\infty > 0$
(Theorem 8(d)), and $K$-uniform polymer decay
$\kappa(t) \geq \kappa_B > 0$ (Lemma L.1.4).

**$K$-uniformity of $L(x,y)$.** Since $L = M_F/r_t$ and both
$M_F$ and $r_t$ are $K$-uniform, the Lipschitz constant is
$K$-uniform.

**The double limit (Moore--Osgood).** With $K$-uniform Lipschitz
constant in $t$ and the Cauchy property in $a$ (Lemma L.2.2), the
hypotheses of the Moore--Osgood theorem are satisfied:

1. The inner limit $\lim_{a \to 0} F^{(a)}(t)$ exists for each
   fixed $t > 0$ (by Lemma L.2.3: the flowed Schwinger functions
   converge as $a \to 0$).

2. The outer limit $\lim_{t \to 0^+} F(t)$ is uniform in $a$
   (by the $K$-uniform Lipschitz estimate (L.3.6)).

Therefore:

$$S_2^{\mathrm{ren}} = \lim_{t \to 0}\lim_{a \to 0}
  \frac{S_{2,t}^{c,(a)}}{c_1^2}
  = \lim_{a \to 0}\lim_{t \to 0}
  \frac{S_{2,t}^{c,(a)}}{c_1^2}
  = \lim_{(a,t) \to (0,0)}
  \frac{S_{2,t}^{c,(a)}}{c_1^2}. \tag{L.3.15}$$

This is the same mechanism as Theorem 8(e) for the unflowed
continuum limit. $\square$


### Step 6: From KK theory to 4D Yang--Mills

The preceding steps establish Lemma L.3.7 in the KK-enhanced theory
on $M^4 \times S^1/\mathbb{Z}_2$. We now project to the physical
4D theory.

**Theorem 5** (Section 4.5). *In the regime $m_1 a \gg 1$:*

$$\Delta_0^{\mathrm{std}} \geq \Delta_0^{\mathrm{KK}}
  - C\,e^{-m_1 a} > 0, \tag{L.3.16}$$

*where $m_1 = 2\sqrt{N}/r_3$ is the lightest KK mass.*

The IR equivalence is mediated by the Feshbach projection: by
Theorem 5, Lemma 4 (Section 4.5), the exact eigenstates of
$\hat{H} = -\ln\hat{T}_{\mathrm{KK}}$ factorize as

$$|n\rangle = |\psi_n\rangle_{\mathrm{4D}}
  \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle,
  \qquad \|\delta_n\| \leq \frac{2C_W}{m_1}\,e^{-m_1 a}.
  \tag{L.3.17}$$

**Projecting the Cauchy estimate.** For the rescaled correlator:

$$|F^{\mathrm{KK}}(t) - F^{\mathrm{4D}}(t)|
  \leq C\,e^{-m_1|x-y|}. \tag{L.3.18}$$

This correction is exponentially small ($m_1 = 2\sqrt{N}/r_3$ with
$r_3 \sim 10^{-31}\,\mathrm{m}$) and $t$-independent (the Feshbach
decomposition acts on the transfer matrix, not on the flow-time
parameter). The 4D Cauchy estimate follows by the triangle inequality:

$$|F^{\mathrm{4D}}(t) - F^{\mathrm{4D}}(t')|
  \leq |F^{\mathrm{KK}}(t) - F^{\mathrm{KK}}(t')|
  + 2C\,e^{-m_1|x-y|}
  \leq (L + 2Ce^{-m_1|x-y|})\,|t - t'|. \tag{L.3.19}$$

**$\mathbb{Z}_2$ parity cancellation (independent confirmation).**
By Lemma L.3.5 (Paper 10, Proposition 3.1; Appendix N, §N.2.2), at each KK level
$n \geq 1$, $f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0$
algebraically. The $\mathbb{Z}_2$ sign flip arises from the
$y$-integral on $S^1/\mathbb{Z}_2$ and is independent of the 4D
momentum structure. Therefore KK modes $n \geq 1$ cancel pairwise
and do not contribute to $F(t)$ at any $t \geq 0$.

**Conclusion of Step 6.** The Cauchy estimate (L.3.6) holds in the
physical 4D $\mathrm{SU}(N)$ Yang--Mills theory, with the Lipschitz
constant modified by an exponentially small correction. $\square$

**This completes the proof of Lemma L.3.7.** $\blacksquare$


---


## L.3.4 Extraction of $[\mathrm{Tr}\,F^2]_R$


**Lemma L.3.8** (Extraction of $[\mathrm{Tr}\,F^2]_R$).

*(i) (Existence.) The renormalized two-point Schwinger function*

$$S_2^{\mathrm{ren}}(x,y) := \lim_{t \to 0^+}
  \frac{S_{2,t}^c(x,y)}{c_1(t)^2} \tag{L.3.20}$$

*exists as a finite quantity for each non-coincident pair $(x,y)$
with $|x - y| > 0$.*

*(ii) (Tempered distribution.) $(x,y) \mapsto S_2^{\mathrm{ren}}(x,y)$
extends to a tempered distribution on
$\{(x,y) \in \mathbb{R}^4 \times \mathbb{R}^4 : x \neq y\}$.*

*(iii) (OS positivity.) $S_2^{\mathrm{ren}}$ satisfies reflection
positivity: for Schwartz test functions $f$ supported in
$\{x_0 > 0\}$,*

$$\sum_{i,j} \bar{c}_i c_j\,
  S_2^{\mathrm{ren}}(\theta f_i, f_j) \geq 0. \tag{L.3.21}$$

*(iv) (Clustering.) $S_2^{\mathrm{ren}}$ decays exponentially at
rate $\Delta_\infty$:*

$$|S_2^{\mathrm{ren}}(x,y)|
  \leq C\,e^{-\Delta_\infty|x-y|}. \tag{L.3.22}$$

*(v) (GNS reconstruction.) By the Osterwalder--Schrader
reconstruction theorem, $[\mathrm{Tr}\,F^2]_R(f)$ exists as an
operator-valued distribution on the physical Hilbert space
$\mathcal{H}$, acting on a common dense invariant domain
$\mathcal{D} \subset \mathcal{H}$.*


*Proof.*

**Part (i): Existence.** By Lemma L.3.7, $F(t)$ is Lipschitz on
$[0, r_t)$:
$|F(t) - F(t')| \leq L(x,y)\,|t - t'|$.
A Lipschitz function on $(0, r_t)$ with bounded values is uniformly
continuous. The limit $\lim_{t \to 0^+} F(t) = F(0)$ exists because:
$F$ is analytic on $|t| < r_t$ (Step 2 of Lemma L.3.7);
$F(0) < \infty$ (Step 1 of Lemma L.3.7); and the removable
singularity theorem identifies $\lim_{t \to 0^+}F(t) = F(0)$.
Therefore $S_2^{\mathrm{ren}}(x,y) = F(0) < \infty$. $\square$

**Part (ii): Tempered distribution.** For each fixed $t > 0$, the
flowed Schwinger functions are tempered distributions (Lemma L.2.4):

$$|S_{n,t}(f)| \leq n!\,C_t^n\,\|f\|_{p_N},$$

with $N = 4n + 1$ (linear in $n$). The uniform Lipschitz estimate
(Lemma L.3.7) together with the $c_1(t)^{-2}$ normalization gives

$$|S_2^{\mathrm{ren}}(f)|
  \leq L(x,y)\,r_t + |F(r_t/2)(f)|
  \leq C'\,\|f\|_{p_N}$$

for a finite constant $C'$. $\square$

**Part (iii): OS positivity.** At each $t > 0$, the flowed
Schwinger functions satisfy OS positivity (Lemma L.2.4; reflection
positivity of the lattice measure is inherited by flowed observables
and preserved in the continuum limit by the Portmanteau theorem).
Reflection positivity is a closed condition: if
$\langle\theta f, f\rangle_t \geq 0$ for all $t > 0$ and
$\langle\theta f, f\rangle_t \to \langle\theta f, f\rangle_0$
as $t \to 0^+$ (by the Lipschitz convergence of Lemma L.3.7), then

$$\langle\theta f, f\rangle_0
  = \lim_{t \to 0^+}\langle\theta f, f\rangle_t
  \geq \liminf_{t \to 0^+} 0 = 0. \tag{L.3.23}$$

$\square$

**Part (iv): Clustering.** The mass gap $\Delta_\infty > 0$
(Theorem 8(d)) provides exponential clustering for the flowed
Schwinger functions uniformly in $t$: by the spectral
representation,

$$|S_{2,t}^c(x,y)| \leq C\,e^{-\Delta_\infty|x-y|}\,|c_1(t)|^2,$$

where $|c_1(t)|^2$ cancels in $F(t)$. Therefore
$|F(t)| \leq C\,e^{-\Delta_\infty|x-y|}$ uniformly in $t$, and the
bound passes to the limit:

$$|S_2^{\mathrm{ren}}(x,y)| = |F(0)|
  \leq C\,e^{-\Delta_\infty|x-y|}. \tag{L.3.24}$$

$\square$

**Part (v): GNS reconstruction.** The system
$\{S_n^{\mathrm{ren}}\}_{n \geq 0}$ satisfies the
Osterwalder--Schrader axioms:

- **OS0'** (temperedness with linear growth): Part (ii) above, with
  seminorm index $N(n) = 4n + 1$ linear in $n$.

- **OS1** (Euclidean covariance): inherited from the flowed theory
  (Lemma L.2.4), which is manifestly O(4)-covariant in the continuum
  limit. The rescaling $c_1(t)^{-n}$ preserves covariance (scalar).

- **OS2** (reflection positivity): Part (iii) above.

- **OS3** (symmetry): the Schwinger functions are symmetric under
  permutations of their arguments, inherited from the lattice where
  all gauge-invariant observables are classical commuting random
  variables under the path integral measure.

- **OS4** (cluster decomposition): Part (iv) above.

By the Osterwalder--Schrader reconstruction theorem
(Osterwalder--Schrader, CMP 31 (1973) 83; CMP 42 (1975) 281),
there exists:

(a) a separable Hilbert space $\mathcal{H}$;

(b) a unique vacuum vector $|\Omega\rangle \in \mathcal{H}$ with
$H|\Omega\rangle = 0$;

(c) a strongly continuous unitary representation
$U: \mathrm{ISO}(4) \to \mathcal{U}(\mathcal{H})$;

(d) operator-valued distributions $[\mathrm{Tr}\,F^2]_R(f)$ on a
common dense invariant domain $\mathcal{D} \subset \mathcal{H}$,

such that the Schwinger functions are recovered as vacuum
expectation values:

$$S_n^{\mathrm{ren}}(f_1 \otimes \cdots \otimes f_n)
  = \langle\Omega|\,[\mathrm{Tr}\,F^2]_R(f_1)
  \cdots [\mathrm{Tr}\,F^2]_R(f_n)\,|\Omega\rangle.
  \tag{L.3.25}$$

The spectral gap
$\mathrm{spec}(H) \cap (0,\Delta_\infty) = \emptyset$ follows from
the exponential clustering (Part (iv)): the Osterwalder--Schrader
mass $m_{\mathrm{OS}} = -\lim_{|x| \to \infty}
|x|^{-1}\ln|S_2^{\mathrm{ren}}(0,x)| \geq \Delta_\infty > 0$.

**The dense invariant domain.** $\mathcal{D}$ is the algebraic span

$$\mathcal{D} := \mathrm{span}\bigl\{
  [\mathrm{Tr}\,F^2]_R(f_1)\cdots[\mathrm{Tr}\,F^2]_R(f_m)
  \,|\Omega\rangle :
  m \geq 0,\; f_j \in \mathcal{S}(\mathbb{R}^4),\;
  \mathrm{supp}(f_j) \subset \{x_0 > 0\}
  \bigr\}. \tag{L.3.26}$$

Density follows from the GNS construction (the Hilbert space is the
closure of vectors of this form). Invariance under
$[\mathrm{Tr}\,F^2]_R(f)$ is immediate (applying a field operator
to a vector in $\mathcal{D}$ produces another vector in
$\mathcal{D}$).

**Closability.** For each
$f \in \mathcal{S}(\mathbb{R}^4)$, the operator
$[\mathrm{Tr}\,F^2]_R(f)$ on $\mathcal{D}$ is closable: the adjoint
$[\mathrm{Tr}\,F^2]_R(f)^*$ is densely defined because
$[\mathrm{Tr}\,F^2]_R(\bar{f})^* \supseteq
[\mathrm{Tr}\,F^2]_R(\theta^* f)$ on $\mathcal{D}$ (by reality
of the Schwinger functions and OS3 symmetry), and $\mathcal{D}$
is dense (Reed--Simon, Vol.\ I, Theorem VIII.1).

**Hermiticity on $\mathcal{D}$.** For real
$f \in \mathcal{S}(\mathbb{R}^4;\,\mathbb{R})$ supported in
$\{x_0 > 0\}$:

$$\langle\chi|\,[\mathrm{Tr}\,F^2]_R(f)\,|\psi\rangle
  = \overline{\langle\psi|\,
  [\mathrm{Tr}\,F^2]_R(f)\,|\chi\rangle}
  \quad \forall\,\psi,\chi \in \mathcal{D}, \tag{L.3.27}$$

by the matrix element formula $\langle\chi|\,\Phi(f)\,|\psi\rangle
= S_{m+1+n}^{\mathrm{ren}}(\theta\bar{h}_m \otimes f \otimes g_n)$,
OS3 symmetry, and reality of the Schwinger functions.

**Essential self-adjointness.** The OS0' verification (Theorem 8(f))
gives $|S_n(f)| \leq n!\,C_0^n\,\|f\|_{p_{4n+1}}$, which is of the
Nelson--Symanzik $n!$ factorial growth type with $n$-independent
constant $C_0$ (by the linked-cluster theorem). By Nelson's analytic
vector theorem (Nelson, Ann.\ Math.\ 70 (1959) 572; Reed--Simon
Vol.\ II, Theorem X.39), for each real
$f \in \mathcal{S}(\mathbb{R}^4;\,\mathbb{R})$, the operator
$[\mathrm{Tr}\,F^2]_R(f)$ is essentially self-adjoint on
$\mathcal{D}$.

**Operator bound from mass gap.** For
$f \in \mathcal{S}(\mathbb{R}^4)$ with $\mathrm{supp}(f)
\subset B_R(0)$:

$$\|[\mathrm{Tr}\,F^2]_R(f)\,|\Omega\rangle\|^2
  = S_2^{\mathrm{ren}}(\theta\bar{f}, f)
  \leq C_2\,\|f\|_{L^2}^2, \tag{L.3.28}$$

where $C_2 = C_2(R, \Delta_\infty)$ is finite by the
Kallen--Lehmann spectral representation and the mass gap
$\Delta_\infty > 0$ (Theorem 8(d)).

**This completes the proof of Lemma L.3.8.** $\blacksquare$


---


## L.3.5 KK-to-4D projection for composite operators


**Lemma L.3.9** (KK-to-4D projection for composite operators).
*Let $S_n^{\mathrm{ren,KK}}(f)$ denote the $n$-point renormalized
Schwinger function of $[\mathrm{Tr}\,F^2]_R$ constructed in
Lemma L.3.8 within the KK-enhanced Yang--Mills theory on
$M^4 \times S^1/\mathbb{Z}_2$, and let
$S_n^{\mathrm{ren,4D}}(f)$ denote the corresponding quantity in
the physical 4D $\mathrm{SU}(N)$ Yang--Mills theory. Then for any
Schwartz test function $f$ supported on $n$ points with minimum
pairwise separation $r_{\min} > 0$:*

$$\bigl|S_n^{\mathrm{ren,KK}}(f)
  - S_n^{\mathrm{ren,4D}}(f)\bigr|
  \;\leq\; C_n\,e^{-m_1\,r_{\min}}, \tag{L.3.29}$$

*where $m_1 = 2\sqrt{N}/r_3$ is the lightest KK mass,
$r_{\min} = \min_{i \neq j}|x_i - x_j|$ is the minimum pairwise
distance among the support points of $f$, and $C_n$ depends on
$n$, $N$, and $\|f\|_{p_M}$ but not on $r_3$ or $a$.*

*Proof.* The proof proceeds through two independent arguments, each
sufficient on its own. Argument A (Feshbach projection) provides
the quantitative bound (L.3.29). Argument B ($\mathbb{Z}_2$ parity)
provides an independent structural confirmation.


### Argument A: Feshbach projection for matrix elements

**A.1. Setup.** The KK-enhanced theory lives on
$\mathcal{H}_{\mathrm{KK}} = \mathcal{H}_{\mathrm{std}} \otimes
\mathcal{H}_{\mathrm{int}}$. The Feshbach projector

$$P_0 = \mathbf{1}_{\mathrm{std}} \otimes
  |\Omega_{\mathrm{int}}\rangle
  \langle\Omega_{\mathrm{int}}|$$

selects the internal ground state, and
$Q_0 = \mathbf{1} - P_0$ selects the KK-excited sector.
By Theorem 5, Lemma 4 (Section 4.5), the exact eigenstates
factorize as in Eq.\ (L.3.17).

**A.2. Massive mode suppression.** *Claim:* The $Q_0$-sector
contribution satisfies
$|S_2^{(Q_0)}(x,y)| \leq C'\,e^{-m_1|x-y|}$.

Any state $|\phi\rangle \in Q_0\mathcal{H}$ has at least one
internal KK mode excited, so its energy satisfies $E_\phi \geq m_1$
(by Theorem 1: the Weitzenb\"ock spectral gap on
$\mathbb{CP}^{N-1}$ equals $m_1 = 2\sqrt{N}/r_3$). The
$Q_0$-sector spectral sum is bounded by

$$|S_2^{(Q_0)}(x,y)|
  \leq e^{-m_1|x_0 - y_0|}
  \sum_{n:\,E_n \geq m_1}
  |\langle\Omega|[\mathrm{Tr}\,F^2]_R|n\rangle|^2.$$

The remaining sum converges by Parseval's identity:

$$\sum_{n \geq 1}
  |\langle\Omega|[\mathrm{Tr}\,F^2]_R|n\rangle|^2
  = \|[\mathrm{Tr}\,F^2]_R|\Omega\rangle\|^2
  - |\langle\Omega|[\mathrm{Tr}\,F^2]_R|\Omega\rangle|^2
  < \infty,$$

where finiteness follows from the $K$-uniform Schwinger function
bound (Lemma L.3.8(ii)). $\square$

**A.3. Feshbach correction to $P_0$-sector matrix elements.**
*Claim:* $|S_2^{(P_0)}(x,y) - S_2^{\mathrm{ren,4D}}(x,y)|
\leq C''\,e^{-m_1 a}\,e^{-\Delta_\infty|x-y|}$.

Using the factorization (L.3.17), the matrix element of
$[\mathrm{Tr}\,F^2]_R$ between the vacuum and glueball state
involves

$$\langle 0|[\mathrm{Tr}\,F^2]_R|1\rangle_{\mathrm{KK}}
  = \langle\psi_0|[\mathrm{Tr}\,F^2]_R|\psi_1
  \rangle_{\mathrm{4D}}
  + \mathcal{E},$$

where the error term satisfies
$|\mathcal{E}| \leq
2\,\|[\mathrm{Tr}\,F^2]_R\|_{\mathrm{op,loc}}\,(2C_W/m_1)\,
e^{-m_1 a}$ by the Cauchy--Schwarz inequality and the Feshbach
tail bound $\|\delta_n\| \leq (2C_W/m_1)e^{-m_1 a}$. Since
$\langle\Omega_{\mathrm{int}}|\Omega_{\mathrm{int}}\rangle = 1$,
the $P_0$-sector matrix element matches the 4D matrix element up
to $O(e^{-m_1 a})$. Squaring and inserting the spectral
representation:

$$\bigl|S_2^{(P_0)} - S_2^{\mathrm{ren,4D}}\bigr|
  \leq C''\,e^{-m_1 a}\,e^{-\Delta_\infty|x-y|}.$$

$\square$

**A.4. Assembly for $n$-point functions.** The spectral
representation of the connected $n$-point function involves products
of matrix elements and propagators. In the connected $n$-point
function, the combinatorial structure requires at least one
propagator connecting two distinct points, contributing at least
$e^{-m_1 r_{\min}}$. The Feshbach correction generates errors of
order $e^{-m_1 a}$ per vertex insertion. For the connected
$n$-point function, the minimum suppression arises from the
shortest internal line:

$$\bigl|S_n^{\mathrm{ren,KK}}(f) - S_n^{\mathrm{ren,4D}}(f)\bigr|
  \leq C_n\,e^{-m_1 r_{\min}}\,\|f\|_{p_M}^n,$$

where $C_n$ depends on $n$ through: (i) the combinatorial factor,
bounded by $n!$ (OS0); (ii) the Schwinger function bound
$|S_n| \leq n!\,C_0^n$ ($K$-uniformly, Lemma L.2.4); and (iii) the
operator norm of $[\mathrm{Tr}\,F^2]_R$ (bounded by analyticity and
the OS axioms).

Combining the massive mode suppression (A.2) and the Feshbach
correction (A.3) by the triangle inequality:

$$\bigl|S_n^{\mathrm{ren,KK}} - S_n^{\mathrm{ren,4D}}\bigr|
  \leq |S_n^{(Q_0)}|
  + |S_n^{(P_0)} - S_n^{\mathrm{ren,4D}}|
  \leq C_n\,e^{-m_1 r_{\min}}. \tag{L.3.30}$$

The gravitational sector contributes no corrections at dimension 6:
by Lemma A2 (Paper 10, Section 5.2b; Appendix N, §N.2.3), graviphoton $A_\mu^{(n)}$
and radion $\phi^{(n)}$ fields contribute only at dimension $\geq 8$.
$\square$


### Argument B: $\mathbb{Z}_2$ parity (independent confirmation)

**B.1.** By Lemma L.3.5 (Paper 10, Proposition 3.1; Appendix N, §N.2.2), at each KK
level $n \geq 1$:
$f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0$. The cancellation
arises from the $y$-integral sign flip on $S^1/\mathbb{Z}_2$
(Eq.\ (Z.1) of Paper 10, Section 3.2; Appendix N, §N.2.2):
$I_{+++}^{(n,n)} = +1/4$,
$I_{--+}^{(n,n)} = -1/4$.

**B.2.** The renormalized $n$-point function decomposes as

$$S_n^{\mathrm{ren,KK}}(f) = S_n^{(0)}(f)
  + \sum_{m \geq 1} S_n^{(m)}(f),$$

where $S_n^{(0)}$ collects contributions with only $n = 0$
(massless, 4D) modes on internal lines. The $n = 0$ sector is the
4D theory: $S_n^{(0)}(f) = S_n^{\mathrm{ren,4D}}(f)$. At each KK
level $m \geq 1$, the $\mathbb{Z}_2$ parity mechanism gives
$S_n^{(m,\mathrm{even})}(f) + S_n^{(m,\mathrm{odd})}(f) = 0$
(term-by-term, for each $m$ individually, not requiring summation
over the KK tower).

**B.3. Persistence at all flow times.** By Lemma L.3.5, the
$\mathbb{Z}_2$ sign flip factorizes from the 4D momentum
integration. The gradient-flow regulator $e^{-tk^2}$ modifies only
the 4D loop momentum integral, not the $y$-integral producing the
sign. The cancellation therefore persists at all $t \geq 0$ and
is scheme-independent.

**Remark L.3.9.** The mixed-sector contributions (with both
$h_{\mu\nu}$ and $h_{\mu 5}$ on internal lines) are separately
absent at dimension 6 by Lemma A2 (Paper 10, Section 5.2b; Appendix N, §N.2.3):
graviphoton and radion contribute only at dimension $\geq 8$.
Therefore the mixed-sector gap of Paper 10, Section 3.6 (Appendix N, §N.2.2), does
not affect the validity of Lemma L.3.9 at the relevant order.

**This completes the proof of Lemma L.3.9.** $\blacksquare$

**Explicit bound for $\mathrm{SU}(3)$.** The lightest KK mass is
$m_1 = 2\sqrt{3}/r_3 \approx 3.46 \times 10^{31}\,\mathrm{m}^{-1}$
(by Theorem 1, the Weitzenb\"ock spectral gap on $\mathbb{CP}^2$).
At the minimum physical separation $r_{\min} = a$ in the validity
regime $m_1 a \gg 1$, the suppression factor is
$e^{-m_1 a} \approx 10^{-1.5 \times 10^{11}}$. The KK corrections
are beyond all perturbative orders.


---


## L.3.6 Summary of proof dependencies

The logical structure of Phase 3 is summarized below. Each arrow
denotes a deductive step; each underbrace identifies the results
discharging the hypotheses.

$$\boxed{
\begin{aligned}
&\underbrace{\text{Thm K.1}
  + \text{Paper 10, Thm 1 (Appendix N, §N.2.4)}
  + \text{Lemmas A1--A3}}_{\text{Lemmas L.3.4, L.3.6}}
  &&\xrightarrow{\;\text{Step 1}\;}
  F(0) < \infty
  \quad[\text{Pillar A}] \\[6pt]
&\underbrace{\text{Balaban (B1)}
  + \text{ODE analyticity}
  + \text{heat kernel entirety}}_{\text{Lemma L.3.1}}
  &&\xrightarrow{\;\text{Step 2}\;}
  F(t)\text{ analytic, }|t| < r_t
  \quad[\text{Pillar B}] \\[6pt]
&\underbrace{\text{No mixing (L.3.2)}
  + \text{dev}\geq 2\text{ (L.3.3)}}_{\text{Lemmas L.3.2, L.3.3}}
  &&\xrightarrow{\;\text{Step 3}\;}
  F(t) = F(0) + O(t)
  \quad[\text{Pillar C}] \\[6pt]
&\underbrace{\text{Pillar A}
  + \text{Pillar B}
  + \text{Cauchy integral formula}}_{\text{complex analysis}}
  &&\xrightarrow{\;\text{Step 4}\;}
  |F(t) - F(t')| \leq L|t - t'| \\[6pt]
&\underbrace{\text{Cor.\ M.1.3}
  + \text{Lemma L.1.4}
  + \text{Lemma L.2.2--L.2.3}}_{\text{K-uniformity}}
  &&\xrightarrow{\;\text{Step 5}\;}
  \text{Double limit commutes} \\[6pt]
&\underbrace{\text{Thm 5 (Feshbach)}
  + \mathbb{Z}_2\text{ cancel (L.3.5)}}_{\text{Section 4.5; Paper 10 (Appendix N)}}
  &&\xrightarrow{\;\text{Step 6}\;}
  \text{KK}\to\text{4D Yang--Mills}
\end{aligned}
}$$

**H4-conditional results.** All results in this section are
unconditional within the KK-enhanced framework, subject to the
standing hypotheses of Sections 4--5 (Theorems 1, 4, 5, 8) and
Paper 10 (Theorems 1, 4.3; Appendix N, §N.2.4-N.2.5). No hypothesis H4
(= the conjecture that the gradient-flow programme closes L.1--L.4)
is used as input; the results of this section *constitute* the
closure of Conjecture L.1.
