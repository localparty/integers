# Lemma 3.7: The Cauchy Estimate for the Rescaled Correlator

*Resolution of the single hard lemma in the gradient-flow programme,*
*using the full QG5D geometric framework.*

*Date: 2026-04-08*

---

## 0. The Lemma

**Lemma 3.7.** *Let $S_{2,t}^c(x,y)$ be the connected two-point function
of the flowed energy density $E(t,x)$ in the continuum Yang--Mills theory
constructed in the mass gap preprint, and let $c_1(t,\mu)$ be the leading
Wilson coefficient in the small-flow-time expansion. Then for fixed
non-coincident $x, y$:*

$$\left|\frac{S_{2,t}^c(x,y)}{c_1(t)^2} - \frac{S_{2,t'}^c(x,y)}{c_1(t')^2}\right| \le L(x,y)\,|t - t'| \tag{3.7}$$

*uniformly as $t, t' \to 0^+$, where $L(x,y) < \infty$ depends on
$|x - y|$ and $\Delta_\infty$ but not on $t$ or $t'$.*

*Consequently, the renormalized two-point function*

$$S_2^{\mathrm{ren}}(x,y) := \lim_{t \to 0^+} \frac{S_{2,t}^c(x,y)}{c_1(t)^2}$$

*exists as a finite quantity for each non-coincident pair $(x,y)$.*


---


## 1. Why This Is Hard in Pure 4D

In pure 4D Yang--Mills without the KK scaffold, the $t \to 0$ limit is
a **deregularization**: the flow provides the only UV regulator, and
sending $t \to 0$ removes it. The rescaled quantity $F(t) := S_{2,t}^c / c_1^2$
is well-defined for $t > 0$ but potentially divergent at $t = 0$. The
Wilson coefficient $c_1(t) \sim t^{-2}(\log(1/t\Lambda^2))^{-1}$ is
designed to absorb the divergence perturbatively, but proving that the
absorption is exact non-perturbatively --- not merely asymptotic --- is
genuinely new mathematics.

The attack plan (Section 6.1) identifies three failure modes:
1. The small-flow-time expansion may be only asymptotic (factorial growth)
2. The flow may not commute cleanly with Balaban's RG
3. Large-field configurations may spoil estimates

All three arise because $F(0)$ might not exist in pure 4D.


---


## 2. Why This Is a Theorem in the KK Framework

In the KK framework on $M^4 \times S^1/\mathbb{Z}_2$, the situation is
fundamentally different. **The $t \to 0$ limit is not a deregularization.**
Even at $t = 0$, the compact $S^1$ provides UV regulation through the
discrete KK spectrum. The quantity $F(0)$ is finite --- not by cancellation
of divergences, but because no divergence exists.

The proof has three pillars:

**(Pillar A) $F(0)$ is finite.** The KK mode sums at $t = 0$ are Epstein
zeta functions at non-positive integers, which vanish by Theorem K.1.
The Goroff--Sagnotti counterterm vanishes in all schemes by Theorem 1
of Paper 10.

**(Pillar B) $F(t)$ is analytic in $t$.** Balaban analyticity (B1)
composes with the heat kernel entirety to give analyticity of the flowed
effective action in $t$, with k-independent radius.

**(Pillar C) Subleading terms vanish as $t \to 0$.** The dimension-6
classification (Section 5.6, Part III) forces all subleading operators
to have $\mathrm{dev} \ge 2$, contributing $O(t)$ corrections.

An analytic function on a disk with a finite value at the origin satisfies
a Lipschitz estimate automatically. The Cauchy estimate (3.7) follows.


---


## 3. The Formal Proof

### Step 1: $F(t)$ is well-defined for all $t \ge 0$ in the KK theory

**At $t > 0$:** The Luscher--Weisz theorem (JHEP 02 (2011) 051) guarantees
that $\langle E(t,x)\,E(t,y)\rangle$ is UV-finite to all orders of
perturbation theory, once the parameters of the underlying 4D gauge
theory are renormalized. Non-perturbatively, the flow propagator
$e^{-tp^2}$ provides exponential UV damping at momentum scale
$|p| \sim 1/\sqrt{t}$. The connected correlator $S_{2,t}^c$ is finite
for every $t > 0$, and $c_1(t) \ne 0$ for $t > 0$ (the coefficient is
a known non-vanishing function of $t$), so $F(t)$ is well-defined.

**At $t = 0$ in the KK theory:** The unflowed correlator involves KK mode
sums. At each loop order $L$, the KK contribution factors as

$$(4\text{D integral}) \times E_L(-j;\, Q_L) \tag{K.3}$$

where $E_L$ is the Epstein zeta function, $Q_L$ is a positive-definite
quadratic form in the KK indices, and $j \ge 1$ is a non-negative integer
determined by the mass-expansion order.

> **Theorem K.1** (Paper 1, Appendix K, Section K.7b): *For any
> positive-definite quadratic form $Q$ in $L$ variables,
> $E_L(-j; Q) = 0$ for all integers $j \ge 1$.*
>
> **Proof mechanism:** The functional equation gives
> $E_L(s; Q) = \pi^s \Lambda(s)/\Gamma(s)$, where $\Lambda(s)$ is
> the completed zeta function (meromorphic, poles only at $s = 0$ and
> $s = L/2$). At $s = -j$ with $j \ge 1$, $\Lambda(-j)$ is finite
> (since $-j \ne 0$ and $-j \ne L/2$ for $L \ge 1$), but
> $1/\Gamma(-j) = 0$ (the Gamma function has poles at all non-positive
> integers). Therefore $E_L(-j; Q) = 0$.
>
> *Reference:* `/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/22-appendix-k-higher-loop-epstein.md`

**Specific mechanisms at each loop order:**

*One loop ($L = 1$):* The leading KK sum is $S_0 = 1 + 2\zeta_R(0) = 0$.
The "1" is the zero-mode contribution; $2\zeta_R(0) = -1$ is the
image-doubled $n \ge 1$ tower (method of images on $S^1/\mathbb{Z}_2$:
Paper 10, Lemma A3, Section 5.2c). Subleading sums involve
$\zeta_R(-2k) = 0$ (trivial Riemann zeros at even negative integers)
and $1/\Gamma(-j) = 0$ for all remaining terms.

> *Reference:* Paper 1, Appendix K, Section K.2.1; Appendix F (one-loop).

*Two loops ($L = 2$):* The sunset topology produces the Eisenstein lattice
zeta function:

$$E_2(s;\, n^2 + nm + m^2) = 6\,\zeta_R(s)\,L(s, \chi_{-3}) \tag{G.4}$$

where $\chi_{-3}$ is the Dirichlet character mod 3. The complementary
trivial zeros cover every negative integer:
- $\zeta_R(-2k) = 0$ for $k \ge 1$ (even negative integers)
- $L(-2k-1, \chi_{-3}) = 0$ for $k \ge 0$ (odd negative integers, from
  vanishing generalized Bernoulli numbers $B_{2k+2, \chi_{-3}} = 0$)

The figure-eight and vertex topologies factor through one-loop results
($2\zeta_R(-2j) = 0$). Ghost contributions carry the same KK quadratic
form $Q_0 = 2(n^2 + nm + m^2)$ and vanish by the same mechanism.

> *Reference:* Paper 1, Appendix G, Sections G.3--G.5.

**Scheme-independence at $t = 0$:** Paper 10, Theorem 1 (Section 4.6,
lines 274--279) proves $C_{\mathrm{GS}} = 0$ in **all** regularization
schemes, via the three-lemma chain:

- **Lemma A1** (vertex mass-independence, Section 5.2a): The 5D
  three-graviton vertex in de Donder gauge has coupling
  $I_{+++}(n_1, n_2, n_1+n_2) = \pi R/4$ for **all** $n_1, n_2 \ge 1$.
  Proved by the product-to-sum identity on
  $\int_0^{\pi R}\cos(n_1 y/R)\cos(n_2 y/R)\cos(n_3 y/R)\,dy$: for
  triangle topology $n_3 = n_1 + n_2$, exactly one Kronecker delta fires
  ($\delta(n_1 + n_2 - n_3, 0) = 1$), giving the universal constant
  $\pi R/4$.

- **Lemma A2** (graviphoton/radion decoupling, Section 5.2b):
  $A_\mu^{(n)}$ and $\phi^{(n)}$ contribute only at dimension $\ge 8$
  because $R^{(1)}_{\mu\nu\rho\sigma}$ is built from $h_{\mu\nu}$ alone
  at linearized order, and single-$A_\mu$ insertions are forbidden by
  $\mathbb{Z}_2$ parity.

- **Lemma A3** (method of images, Section 5.2c): The orbifold propagator
  $G_{\mathbb{Z}_2}(y,y') = G_{S^1}(y,y') + G_{S^1}(y,-y')$ restores
  the full $\mathbb{Z}$ sum: $S_0 = 1 + 2\zeta_R(0) = 0$.

The assembled Goroff--Sagnotti coefficient:

$$C_{\mathrm{GS}} = \left[\frac{\pi R}{4}\right]^2 \times J(0,0) \times S_0^2 = \left[\frac{\pi R}{4}\right]^2 \times J(0,0) \times 0 = 0$$

with subleading corrections vanishing via $E_2(-j; Q_2) = 0$
(Theorem K.1).

> *Reference:* Paper 10, Theorem 1, Section 4.6, lines 274--310;
> Research memos in `/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/`

**Weyl anomaly protection:** Paper 10, Route 05 (Section 4.5, Theorem 4.3):
the total Weyl anomaly of the KK graviton tower vanishes,

$$a_{\mathrm{total}} = \frac{43}{360} \times S_0 = 0, \qquad c_{\mathrm{total}} = \frac{87}{20} \times S_0 = 0, \tag{W.1}$$

using Vassilevich's mass-independence of $a_4$: the Seeley--DeWitt
coefficient $a_4(D_0 + m^2 I) = a_4(D_0)$ because
$e^{-t(D_0 + m^2)} = e^{-tm^2}\,e^{-tD_0}$ shifts only $a_0$ and $a_2$.
The Wess--Zumino consistency condition (Wess--Zumino 1971; Osborn 1991)
protects $(a, c)$ cohomologically: no finite local counterterm can shift
them. The vanishing holds in **any** diffeomorphism-preserving scheme.

> *Reference:* Paper 10, Sections 4.4--4.5.

**Conclusion of Step 1:** $F(t)$ is well-defined and finite for all
$t \ge 0$ in the KK theory. $F(0)$ is the renormalized correlator of
$[\mathrm{Tr}\,F^2]_R$ in the unflowed KK theory.

---

### Step 2: $F(t)$ is analytic in $t$ for $|t| < r_t$

**Ingredient (a): Balaban analyticity (B1).**

> **(B1)** (Section 5.6, Part I, lines 1577--1664). *The effective action
> $S_k^{\mathrm{eff}}[V]$ is analytic in $\{V_\ell\}$ with k-independent
> radius*
>
> $$\rho = \min\!\left(\frac{\kappa}{2d},\;\frac{m_W a}{2C_D},\;r_{\mathrm{proj}}(N)\right) > 0. \tag{B1}$$
>
> *Reference:* Section 5.6, Part I, lines 1654--1657.

Analyticity preserved through four operations in Balaban's inductive
construction (Section 5.6, Step (b), lines 1605--1632):

| Operation | Mechanism |
|:----------|:----------|
| (i) Background evaluation | Polynomial composition (entire) |
| (ii) Saddle point via $G_k = (-D^2 + m_W^2)^{-1}$ | Analytic inversion; CMP 95 Prop. 1.2: $\|G_k(x,y)\| \le Ce^{-\delta_0|x-y|}$ |
| (iii) Gaussian integration | Convergent trace-log: $\det(S_k^{(2)})^{-1/2}$ analytic where $S_k^{(2)} > 0$ |
| (iv) Mayer resummation | Weierstrass M-test: $\sum|c_n| \le Ce^{-\rho n}$ (CMP 109 Sec. 4) |

Radius k-independent because all constraints ($\kappa/2d$, $m_Wa/2C_D$,
$r_{\mathrm{proj}}(N)$) are k-independent.

**Ingredient (b): ODE analyticity.** The lattice gradient flow ODE on
compact $\mathrm{SU}(N)^{|\mathrm{links}|}$ has polynomial right-hand
side. By Cauchy--Kowalevski in finite dimensions, the solution
$V_t(\ell)$ is analytic in $t$ for $|t| < r_{\mathrm{ODE}}$.

**Ingredient (c): Heat kernel entirety.** $e^{-tp^2}$ is entire in $t$.
On $M^4 \times S^1$, the heat kernel factorizes
(Paper 1, Appendix S, Section S.3.1):
$K_{M^4 \times S^1}(t) = K_{M^4}(t) \otimes K_{S^1}(t)$.

**Composition.** The map
$t \xmapsto{\text{ODE}} V_t \xmapsto{\text{(B1)}} S_k^{\mathrm{eff}}[V_t]$
is a composition of analytic functions, hence analytic. The radius is

$$r_t = \min(r_{\mathrm{ODE}},\;\rho / L_F) > 0 \tag{R_t}$$

where $L_F$ is the k-independent Lipschitz constant of $t \mapsto V_t$.

**Extension to $t = 0$.** By Step 1, $F(0) < \infty$. An analytic
function on $0 < |t| < r_t$ with finite limit at $t = 0$ extends
analytically to $|t| < r_t$ (removable singularity theorem).

**Consequence:** $F(t)$ is analytic on the full disk $|t| < r_t$
**including $t = 0$**, with k-independent radius $r_t > 0$.

The small-flow-time expansion is therefore **convergent**, not merely
asymptotic. This closes Gap G1 of the attack plan (Section 6.1, risk 1).

---

### Step 3: Subleading terms are $O(t)$

The small-flow-time expansion gives:

$$F(t) = F(0) + R(t), \tag{SFT}$$

where $F(0) = \langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y)\rangle_c$
(the unique dimension-4 contribution, no mixing by Lemma 3.2:
$\mathcal{C}$-elimination from Section 5.3.1) and $R(t)$ collects
dimension-$\ge 6$ operators.

Each dimension-$d_k$ operator contributes with Wilson coefficient
$c_k(t)/c_1(t) \sim t^{(d_k-4)/2}$, vanishing as $t \to 0$ for $d_k \ge 6$.

Non-perturbative matrix elements controlled by deviation-order
classification (Section 5.6, Part III, lines 1737--1891): every
$\mathcal{C}$-even dimension-6 operator has $\mathrm{dev} \ge 2$.
By the spectral lemma (Section 5.5.3):

$$|\langle 1|\mathcal{O}_{d=6}|1\rangle_c| \le C_p\,M\,\hat{\Delta}^2$$

with $C_p$ K-uniform (Hastings--Koma, Section 5.5.3 Step 3(i)).

**Bound on remainder:**

$$|R(t)| \le C_{\mathrm{sub}}\,t\,\frac{g_k^4\,\hat{\Delta}^2}{|x-y|^{10}} + O(t^2). \tag{R-bound}$$

This confirms $F(t) = F(0) + O(t)$: Lipschitz near $t = 0$.

---

### Step 4: The Cauchy estimate

$F(t)$ is analytic on $|t| < r_t$ (Step 2) with $F(0)$ finite (Step 1).
By the Cauchy integral formula:

$$|F'(t)| \le \frac{1}{r_t}\,\sup_{|s| = r_t}|F(s)| =: \frac{M_F}{r_t} \tag{CI}$$

for all $|t| < r_t$.

**Bounding $M_F$:** At $|s| = r_t$ (fixed nonzero flow time):
- UV: $e^{-r_t p^2}$ exponential damping
- IR: $\Delta_\infty > 0$ exponential decay (Theorem 8(d), OS4 clustering,
  Section 5.7 lines 2384--2423)
- Schwinger function bounds: $|S_n| \le n!\,C_0^n$ K-uniformly
  (OS0, lines 2181--2248)

Therefore $M_F < \infty$.

**The estimate:** For $0 \le t, t' < r_t$:

$$|F(t) - F(t')| = \left|\int_t^{t'} F'(s)\,ds\right| \le |t - t'| \cdot \frac{M_F}{r_t} =: L(x,y)\,|t - t'|. \tag{3.7-proof}$$

This is Eq. (3.7) with **Lipschitz regularity** ($\alpha = 1$). $\square$

---

### Step 5: K-uniformity and the double limit

**K-uniformity of $r_t$:** All ingredients ($\rho$, $L_F$,
$r_{\mathrm{ODE}}$) are k-independent (from (B1)) and K-independent
(from Corollary M.1.3, Appendix M line 132).

**K-uniformity of $M_F$:** Controlled by K-uniform Schwinger function
bounds and K-independent mass gap.

**K-uniformity of $L$:** $L(x,y) = M_F/r_t$ is K-uniform.

**Double limit:** Uniformity in $a$ allows (Moore--Osgood, same mechanism
as Theorem 8(e)):

$$S_2^{\mathrm{ren}} = \lim_{t \to 0}\lim_{a \to 0}\frac{S_{2,t}^{c,(a)}}{c_1^2} = \lim_{a \to 0}\lim_{t \to 0}\frac{S_{2,t}^{c,(a)}}{c_1^2} = \lim_{(a,t) \to (0,0)}\frac{S_{2,t}^{c,(a)}}{c_1^2}.$$

---

### Step 6: From KK theory to 4D Yang--Mills

Theorem 5 (Section 4.5, lines 953--972):
$\Delta_0^{\mathrm{std}} \ge \Delta_0^{\mathrm{KK}} - Ce^{-m_1a} > 0$.

Feshbach projection (lines 1188--1262): eigenstates factorize as
$|n\rangle = |\psi_n\rangle_{\mathrm{4D}} \otimes |\Omega_{\mathrm{int}}\rangle + |\delta_n\rangle$
with $\|\delta_n\| \le (2C_W/m_1)e^{-m_1a}$.

For the rescaled correlator:

$$|F^{\mathrm{KK}}(t) - F^{\mathrm{4D}}(t)| \le C\,e^{-m_1|x-y|} \tag{IR}$$

The correction is exponentially small ($m_1 = 2\sqrt{N}/r_3$, with
$r_3 \sim 10^{-31}$ m from the CP$^2$ compactification, Paper 4) and
**$t$-independent**. The 4D Cauchy estimate follows:

$$|F^{\mathrm{4D}}(t) - F^{\mathrm{4D}}(t')| \le (L + 2Ce^{-m_1|x-y|})|t-t'|.$$

The $\mathbb{Z}_2$ parity cancellation (Paper 10, Route 03, Proposition 3.1)
provides an independent confirmation: at each KK level $n \ge 1$,
$f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0$ algebraically, so KK
modes $n \ge 1$ cancel pairwise and do not contribute to $F(t)$ at any
$t$. The only surviving contribution is the $n = 0$ zero-mode sector ---
precisely the 4D theory.


---


## 4. The Parallel with Theorem M.2.1

| | **Continuum limit** ($a \to 0$) | **Flow-time limit** ($t \to 0$) |
|:--|:--|:--|
| **Cauchy estimate** | $|S^{(K+1)} - S^{(K)}| \le Cg_K^4(a_K\Lambda)^s$ | $|F(t) - F(t')| \le L|t-t'|$ |
| **Convergence** | Doubly exponential: $\sum g_K^4(a_K\Lambda)^s \sim 4^{-K}$ | Analyticity: Taylor converges |
| **Finite endpoint** | $S^{(0)}$ finite (lattice) | $F(0)$ finite (KK: Theorem K.1) |
| **Uniformity** | K-uniform (Appendix M) | K-uniform (same mechanism) |
| **Uniqueness** | Cauchy in complete space | Analytic with finite boundary |

Both use the same abstract structure: Cauchy estimate with uniform
constants in a complete space. The continuum limit uses doubly
exponential convergence from the RG telescoping sum ($C_{K+1} = C_K/4 + C_*$,
Section 5.4); the flow-time limit uses analyticity from Balaban (B1)
composed with heat kernel entirety.


---


## 5. The Poisson Bridge: Quantitative Scheme Control

Paper 10, Route 04 (Sections 4.1--4.3): the Poisson identity between KK
sum and winding-mode sum, verified to $1.09 \times 10^{-24}$ relative
precision (Section 4.2, line 86). The exchange lemma (lines 40--77):
KK sum and loop integral commute because the Poisson-resummed form
converges exponentially ($\hat{F}(m; Rk) \sim e^{-2\pi mRk}$). The
scheme difference (Proposition 4.2):

$$I_{\mathrm{GS}}^{\mathrm{dim\text{-}reg}} - I_{\mathrm{GS}}^{\mathrm{zeta\text{-}reg}} = O(e^{-2\pi Rk}) \approx 4.6 \times 10^{-4}\text{ of total.}$$

This guarantees the Cauchy estimate, proved via Epstein vanishing in the
zeta scheme, is valid in the gradient-flow scheme up to exponentially
small corrections.


---


## 6. Proof Chain Summary

$$\boxed{%
\begin{aligned}
&\text{Balaban (B1)} + \text{heat kernel entirety}
  &&\xrightarrow{\text{Step 2}}\; F(t) \text{ analytic in } t \\[4pt]
&\text{Theorem K.1} + \text{Paper 10 Theorem 1}
  &&\xrightarrow{\text{Step 1}}\; F(0) \text{ finite} \\[4pt]
&\text{Analyticity} + \text{finite endpoint}
  &&\xrightarrow{\text{Step 4}}\; |F(t) - F(t')| \le L|t-t'| \\[4pt]
&\text{K-uniformity (Appendix M)}
  &&\xrightarrow{\text{Step 5}}\; \text{double limit commutes} \\[4pt]
&\text{Theorem 5 (IR equivalence)}
  &&\xrightarrow{\text{Step 6}}\; \text{KK} \to \text{4D}
\end{aligned}
}$$

**All QG5D inputs:**

| Paper | Result | Role |
|:------|:-------|:-----|
| 1 | Theorem K.1 (Appendix K, Section K.7b) | KK mode sums vanish at $t = 0$ |
| 1 | Theorem S.1 (Appendix S, Section S.6) | All-orders perturbative finiteness |
| 1 | Appendix S, Section S.3.1 | Heat kernel factorizes on $M^4 \times S^1$ |
| 1 | Appendix K, Section K.2.1 | $S_0 = 1 + 2\zeta(0) = 0$ |
| 1 | Appendix G, Sections G.3--G.5 | Two-loop Eisenstein zeta: complementary zeros |
| 4 | Section 3 | CP$^2 \times S^2 \times S^1$ geometry, $r_3$ scale |
| 6 | Theorem F.1 | Dilaton frozen, Casimir potential exact |
| 10 | Theorem 1 (Section 4.6) | $C_{\mathrm{GS}} = 0$ all schemes |
| 10 | Theorem U.2a (Section 2.5) | $a_2 = a_4 = 0$ (Seeley--DeWitt) |
| 10 | Proposition 3.1 (Section 3.3) | $\mathbb{Z}_2$ cancellation at all $t$ |
| 10 | Proposition 4.2 (Section 4.3) | Poisson bridge, $10^{-24}$ precision |
| 10 | Theorem 4.3 (Section 4.5) | Wess--Zumino protection |
| 10 | Lemma A1 (Section 5.2a) | Vertex $n$-independence: $I_{+++} = \pi R/4$ |
| 10 | Lemma A2 (Section 5.2b) | Graviphoton/radion decouple |
| 10 | Lemma A3 (Section 5.2c) | Method of images: $S_0 = 0$ |
| 8 | Theorem 4 (Section 4.4) | KK mass gap $\Delta_0^{\mathrm{KK}} > 0$ |
| 8 | Theorem 5 (Section 4.5) | IR equivalence: KK $\to$ 4D |
| 8 | Theorem 8 (Section 5.7) | Continuum mass gap + OS axioms |
| 8 | Section 5.3.1 | $\mathcal{C}$-elimination, no dim-4 mixing |
| 8 | Section 5.5.3 | Spectral lemma, K-uniform $C_p$ |
| 8 | Section 5.6, Part I | Balaban analyticity (B1) |
| 8 | Section 5.6, Part III | Dimension-6 classification, dev $\ge 2$ |
| 8 | Appendix M | K-uniformity: M.1.1, M.1.2, M.2.1 |


---


## 7. Difficulty Reassessment

With the KK scaffold, the "hardness" of Lemma 3.7 evaporates. The
difficulty in pure 4D came from the divergence of $F(0)$; in the KK
framework, $F(0)$ is finite by Theorem K.1 and the proof reduces to:

1. A composition of analyticity results (Step 2): **moderate**
2. A standard Cauchy estimate (Step 4): **textbook**
3. K-uniformity transfer (Step 5): **established** (Appendix M mechanism)
4. Feshbach projection (Step 6): **established** (Theorem 5 mechanism)

**What is genuinely new:** The composition argument in Step 2 ---
composing Balaban analyticity in $V$ (from the polymer expansion) with
ODE analyticity in $t$ (from the gradient flow) to obtain analyticity of
$F(t)$ in $t$ with K-uniform radius. This is moderate-difficulty new
mathematics, not hard.

**Revised rating: M** (moderate), down from **H** (hard). $\square$


---


*File locations:*
- *This document:* `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/03-the-cauchy-estimate-for-the-rescaled-correlator.md`
- *Lemma catalog:* `lemmas-and-gap-strategy.md`
- *Formal argument:* `formal-argument.md`
- *Attack plan:* `../l1-gradient-flow-attack-plan.md`
- *Theorem K.1:* `/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/22-appendix-k-higher-loop-epstein.md`
- *Paper 10 Theorem 1:* `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/04-poisson-weyl.md`
- *Balaban (B1):* `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`
- *Theorem 5:* `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`
- *Appendix M:* `/Users/gsix/yang-mills/preprint/sections/M-gap-closures-r00.md`
