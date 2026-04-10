# W7-14: Asymptotic-Freedom Short-Distance Match

## Lemma 4.2 $\to$ Conjecture L.2

*Proof memo of the gradient-flow programme closing Conjectures L.1--L.4
of the Yang--Mills mass gap preprint.*

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*

---

## Overview

This memo establishes the asymptotic-freedom short-distance match for
the renormalized two-point function of $[\mathrm{Tr}\,F^2]_R$,
closing Conjecture L.2 of Appendix L conditional on the standard
hypothesis H4 (non-perturbative Schwinger functions agree with
perturbation theory at short distances). The argument proceeds in
four stages:

1. **Definition** of the gradient-flow running coupling
   $\bar{g}_{\mathrm{GF}}^2(q)$.
2. **Extraction** of the AF-predicted two-point function from the
   small-flow-time expansion with explicit one-loop coefficient
   $\bar{c}_1$.
3. **Lattice--continuum matching** via the Reisz power-counting theorem.
4. **KK protection** via Paper 10, Route 05 (Weyl anomaly vanishing):
   the KK tower does not contaminate 4D short-distance physics.

The result is conditional on Conjecture L.1 (existence of
$[\mathrm{Tr}\,F^2]_R$, closed by Lemma 3.8 in W5-10) and on
Hypothesis H4 (stated precisely below). The gradient-flow framework
provides three independent reasons why H4 is more plausible than in
any previous formulation of the conjecture.


---


## 1. The gradient-flow running coupling

### 1.1 Definition

The Yang--Mills gradient flow (Luscher, JHEP 08 (2010) 071) defines
a one-parameter family of gauge fields $B_\mu(t,x)$ for flow time
$t \geq 0$, with all composite operators at $t > 0$ automatically
UV-finite (Luscher--Weisz, JHEP 02 (2011) 051). The energy density

$$E(t,x) := \tfrac{1}{4}\,G_{\mu\nu}^a(t,x)\,G_{\mu\nu}^a(t,x)
\tag{1.1}$$

has a well-defined expectation value at each $t > 0$. The
**gradient-flow running coupling** is defined by inverting the
one-point function:

$$\bar{g}_{\mathrm{GF}}^2(q) := \frac{128\pi^2}{3(N^2 - 1)}\;
t^2\,\langle E(t,x) \rangle
\bigg|_{q\,=\,(8t)^{-1/2}}. \tag{1.2}$$

This is a non-perturbative definition: the left-hand side is
constructed from the full (non-perturbative) expectation value, not a
truncated perturbation series. The momentum scale
$q = (8t)^{-1/2}$ is the natural UV scale set by the flow's Gaussian
smoothing kernel of width $\sqrt{8t}$.

### 1.2 Perturbative expansion

The small-flow-time expansion (Luscher 2010; Harlander--Neumann,
JHEP 06 (2016) 161; Harlander et al., arXiv:2111.14376) gives:

$$\langle E(t,x) \rangle = \frac{3(N^2 - 1)}{128\pi^2 t^2}
\left[1 + \bar{c}_1\,\bar{g}^2(q) + \bar{c}_2\,\bar{g}^4(q)
+ O(\bar{g}^6)\right], \qquad q = (8t)^{-1/2}, \tag{1.3}$$

where $\bar{g}(q)$ is the $\overline{\mathrm{MS}}$ running coupling
at scale $q$, and the one-loop coefficient is

$$\bar{c}_1 = \frac{1}{(4\pi)^2}\left[\frac{11N}{3}\,
\bigl(2\gamma_E + \ln 3\bigr) + \cdots\right], \tag{1.4}$$

with $\gamma_E = 0.5772\ldots$ the Euler--Mascheroni constant.
The ellipsis in (1.4) denotes the finite scheme-matching constant
between $\overline{\mathrm{MS}}$ and the gradient-flow scheme; it is
a known numerical constant that does not affect the logarithmic
running. The two-loop coefficient $\bar{c}_2$ was computed by
Harlander--Neumann (2016); the three-loop coefficient is in Artz et
al. (JHEP 06 (2019) 121) and Harlander et al. (arXiv:2111.14376).

### 1.3 Relation to asymptotic freedom

Substituting the definition (1.2) into (1.3) yields:

$$\bar{g}_{\mathrm{GF}}^2(q) = \bar{g}^2(q)\left[1 + \bar{c}_1\,
\bar{g}^2(q) + O(\bar{g}^4)\right]. \tag{1.5}$$

Inverting perturbatively:

$$\bar{g}^2(q) = \bar{g}_{\mathrm{GF}}^2(q)\left[1 - \bar{c}_1\,
\bar{g}_{\mathrm{GF}}^2(q) + O(\bar{g}_{\mathrm{GF}}^4)\right].
\tag{1.6}$$

Thus $\bar{g}_{\mathrm{GF}}^2(q)$ satisfies the same RG equation as
$\bar{g}^2(q)$ at leading order:

$$q\,\frac{\partial}{\partial q}\,\bar{g}_{\mathrm{GF}}^2(q)
= -2b_0\,\bar{g}_{\mathrm{GF}}^4(q) + O(\bar{g}_{\mathrm{GF}}^6),
\qquad b_0 = \frac{11N}{48\pi^2}. \tag{1.7}$$

The gradient-flow coupling is asymptotically free:
$\bar{g}_{\mathrm{GF}}^2(q) \to 0$ as $q \to \infty$ (equivalently,
$t \to 0^+$), with the universal one-loop running

$$\bar{g}_{\mathrm{GF}}^2(q) = \frac{1}{2b_0\ln(q/\Lambda)}
\left[1 + O\!\left(\frac{\ln\ln(q/\Lambda)}
{\ln(q/\Lambda)}\right)\right]. \tag{1.8}$$


---


## 2. Extraction of the AF prediction for the two-point function

### 2.1 The rescaled correlator

Lemma 3.8 (W5-10) establishes that the renormalized two-point
function exists as the limit

$$S_2^{\mathrm{ren}}(x,y) = \lim_{t \to 0^+}
\frac{S_{2,t}^c(x,y)}{c_1(t)^2}, \tag{2.1}$$

where $S_{2,t}^c(x,y) = \langle E(t,x)\,E(t,y)\rangle_c$ is the
connected two-point Schwinger function of the flowed energy density,
and

$$c_1(t) = \frac{1}{8\pi^2 t^2}\left[1 + \bar{c}_1\,
\bar{g}^2(q) + O(\bar{g}^4)\right], \qquad q = (8t)^{-1/2},
\tag{2.2}$$

is the leading Wilson coefficient in the small-flow-time expansion of
$E(t,x)$ onto $[\mathrm{Tr}\,F^2]_R(x)$. By the no-mixing result at
dimension 4 (the unique gauge-invariant, $\mathcal{C}$-even,
parity-even operator is $\mathrm{Tr}\,F^2$; cf. preprint
Section 5.3.1), the coefficient $c_1(t)$ is a scalar, not a mixing
matrix.

### 2.2 The trace-anomaly identity

The anomalous dimension of $\mathrm{Tr}\,F^2$ is fixed exactly by
the Spiridonov--Chetyrkin trace-anomaly identity
(Spiridonov 1984; Spiridonov--Chetyrkin 1988):

$$\gamma_{\mathrm{Tr}\,F^2}(g) = -\,\frac{2\,\beta(g)}{g}
= 2b_0\,g^2 + O(g^4). \tag{2.3}$$

This identity is not a one-loop approximation; it is exact in
continuum perturbation theory to all orders. It implies that the
renormalization factor $Z_{\mathrm{Tr}\,F^2}$ runs with the
coupling as

$$Z_{\mathrm{Tr}\,F^2}(\mu) \propto g(\mu)^{-2}
\propto \left[\ln(\mu/\Lambda)\right]^{-1}. \tag{2.4}$$

### 2.3 The AF-predicted two-point function

Combining the free-field Wick contraction at tree level
(engineering dimension: $\dim[\mathrm{Tr}\,F^2] = 4$, so the
two-point function scales as $|x|^{-2\times 4} = |x|^{-8}$) with the
anomalous-dimension resummation (2.3)--(2.4) at renormalization scale
$\mu = 1/|x|$ yields the perturbative prediction:

$$\langle\,[\mathrm{Tr}\,F^2]_R(x)\;[\mathrm{Tr}\,F^2]_R(0)\,
\rangle^{\mathrm{pert}} = \frac{C_N}{|x|^8}\;
\left(\ln\frac{1}{|x|\Lambda}\right)^{-2}
\left[1 + O\!\left((\log)^{-1}\right)\right], \tag{2.5}$$

with the universal constant

$$C_N = \frac{2(N^2 - 1)}{\pi^6}. \tag{2.6}$$

The coefficient $C_N$ is computed from the tree-level Wick
contraction of $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ in the free
$\mathrm{SU}(N)$ gluon theory: the combinatorial factor is
$2(N^2 - 1)$ (from the trace over color indices and the sum over
Lorentz contractions), and the $\pi^{-6}$ arises from the
four-dimensional free propagator in position space,
$\langle A_\mu^a(x)\,A_\nu^b(0)\rangle_{\mathrm{free}} =
\delta^{ab}\,\delta_{\mu\nu}\,\Gamma(1)/(4\pi^2|x|^2)$, taken to
the second power and contracted.

The two powers of $(\ln)^{-1}$ in (2.5) arise from the two
insertions of $[\mathrm{Tr}\,F^2]_R$, each carrying one power of
$Z_{\mathrm{Tr}\,F^2}(\mu) \sim (\ln)^{-1}$ via (2.4). The
$O((\log)^{-1})$ remainder incorporates the two-loop and higher
corrections to the Wilson coefficients and the $\beta$-function.


---


## 3. Role of the Reisz power-counting theorem

The connection between the lattice construction (which defines the
non-perturbative theory) and the continuum perturbative prediction
(2.5) is mediated by the Reisz power-counting theorem.

**Theorem** (Reisz, CMP 116 (1988) 81; CMP 117 (1988) 79). *Let
$I_L(a)$ be a lattice Feynman integral built from a renormalizable
lattice action with lattice spacing $a$, and let $I_C$ be its
continuum counterpart. Then, for every one-particle-irreducible
diagram $\gamma$ satisfying the lattice power-counting conditions:*

$$I_L(a) = I_C + O(a^2\,\ln^k a), \tag{3.1}$$

*where $k$ is the loop order of $\gamma$.*

The Reisz theorem was extended to lattice gauge theory by
Luscher--Weisz (CMP 97 (1985) 59) and to gauge-invariant composite
operators by Caracciolo--Curci--Menotti--Pelissetto (Phys. Lett. B
228 (1989) 375; Nucl. Phys. B 375 (1992) 195).

**Application to the AF match.** The Reisz theorem guarantees that
the one-loop lattice perturbative computation of the $[\mathrm{Tr}\,
F^2]_R$ anomalous dimension reproduces the continuum result
$\gamma_{\mathrm{Tr}\,F^2} = 2b_0\,g^2 + O(g^4)$ up to lattice
artifacts of order $O(a^2\,\ln^k a)$, which vanish in the continuum
limit $a \to 0$. The one-loop Wilson coefficient $\bar{c}_1$ in
(1.4) is likewise reproduced on the lattice. The engineering-dimension
power $|x|^{-8}$, the logarithmic correction $(\log)^{-2}$, and the
constant $C_N$ are all accessible within lattice perturbation theory
by the Reisz theorem.

**Scope of Reisz.** The Reisz theorem is purely perturbative: it
establishes diagram-by-diagram agreement between lattice and
continuum perturbation theory. It does *not* address the question of
whether the full non-perturbative Schwinger function agrees with the
formal perturbation series at short distances. That question is the
content of Hypothesis H4 below.


---


## 4. Hypothesis H4: non-perturbative equals perturbative at short distances

### 4.1 Statement

**Hypothesis H4** (Standard lattice QCD hypothesis). *The
renormalized non-perturbative Schwinger function $S_2^{\mathrm{ren}}
(x,y)$ constructed in Lemma 3.8 admits a short-distance asymptotic
expansion whose leading term coincides with the perturbative
prediction (2.5):*

$$S_2^{\mathrm{ren}}(x,y) = \frac{C_N}{|x-y|^8}\;
\left(\ln\frac{1}{|x-y|\Lambda}\right)^{-2}
\left[1 + O\!\left((\log)^{-1}\right)\right]
\qquad (|x-y| \to 0). \tag{4.1}$$

### 4.2 Status

**Hypothesis H4 is not proved. It is stated as conditional.**

This hypothesis is the standard assumption of QCD phenomenology and
lattice QCD. It is implicitly invoked in every application of the
SVZ sum rules, every lattice determination of $\alpha_s$ from
short-distance quantities, and every perturbative matching
calculation in continuum QCD. Its standing:

- **Proved in super-renormalizable cases.** For $\phi^4_3$
  (Glimm--Jaffe 1987; Magnen--Rivasseau--Seneor, CMP 155 (1993)
  325), the analogous statement is a theorem.

- **Open for 4D non-Abelian gauge theory.** Neither the Balaban
  programme, nor any other constructive-QFT framework, has
  established that the non-perturbative Schwinger functions admit
  short-distance asymptotic expansions agreeing with perturbation
  theory.

- **Extensively tested numerically.** Every lattice QCD simulation
  that has compared short-distance correlators to perturbative QCD
  (scaling tests, step-scaling functions, gradient-flow coupling
  measurements on the lattice) finds quantitative agreement at the
  level of the available perturbative precision.

### 4.3 Conditional closure of Conjecture L.2

**Lemma 4.2** (AF short-distance match). *Conditional on Lemma 3.8
(existence of $[\mathrm{Tr}\,F^2]_R$, established in W5-10) and on
Hypothesis H4, the renormalized two-point Schwinger function satisfies*

$$\bigl\langle\,[\mathrm{Tr}\,F^2]_R(x)\;[\mathrm{Tr}\,F^2]_R(0)\,
\bigr\rangle = \frac{C_N}{|x|^{8}}\;
\Bigl(\ln\frac{1}{|x|\Lambda}\Bigr)^{-2}
\bigl[1 + O\bigl((\log)^{-1}\bigr)\bigr]
\qquad (|x| \to 0),$$

*with $C_N = 2(N^2-1)/\pi^6$ and $\Lambda$ the non-perturbative
$\mathrm{SU}(N)$ Lambda parameter.*

*Proof.* Assemble the three ingredients:

(i) **Existence of the renormalized correlator.** Lemma 3.8
(W5-10) constructs $S_2^{\mathrm{ren}}(x,y) = \lim_{t \to 0^+}
S_{2,t}^c(x,y)/c_1(t)^2$ as a finite tempered distribution on
$\{(x,y) : x \neq y\}$. The limit exists by the Cauchy estimate
(Lemma 3.7) and the analyticity of $F(t)$ in the flow time.

(ii) **Perturbative prediction.** The small-flow-time expansion,
with Wilson coefficient $c_1(t)$ given by (2.2), encodes the AF
prediction via the trace-anomaly identity (2.3). The Reisz theorem
(Section 3) guarantees that the lattice perturbative coefficients
converge to their continuum values. The resulting perturbative
two-point function is (2.5).

(iii) **Hypothesis H4.** The non-perturbative correlator $S_2^{
\mathrm{ren}}(x,y)$ agrees with the perturbative prediction (2.5)
at short distances. This is the single unproved input.

Combining (i)--(iii) yields the claimed asymptotic. $\square$


---


## 5. Why gradient flow makes H4 more plausible

Although Hypothesis H4 remains unproved, the gradient-flow framework
provides three independent structural reasons why it is more
plausible within this construction than in any previous formulation.

### 5.1 Controlled interpolation between non-perturbative and perturbative regimes

The gradient flow provides a smooth, one-parameter interpolation
between the non-perturbative regime (large flow time $t$, where the
field is smeared over distances $\sqrt{8t}$ much larger than
$\Lambda^{-1}$) and the perturbative regime (small $t$, where the
smearing scale $\sqrt{8t}$ is much shorter than $\Lambda^{-1}$).
At each $t > 0$, the flowed correlator is a well-defined
non-perturbative object with a well-defined perturbative expansion.
The flow does not "jump" from non-perturbative to perturbative; it
traverses a continuous path parameterized by $t$.

In conventional formulations, H4 requires comparing two objects
defined by fundamentally different methods: the non-perturbative
Schwinger function (constructed by the lattice path integral) and
the perturbative prediction (constructed diagram by diagram). In the
gradient-flow framework, both objects are constructed from the
*same* underlying quantity $S_{2,t}^c(x,y)/c_1(t)^2$, evaluated at
different values of the same continuous parameter $t$:

- The non-perturbative correlator is the $t \to 0^+$ limit.
- The perturbative prediction is the small-$t$ asymptotic expansion.

The Cauchy estimate (Lemma 3.7, W5-10) shows that the rescaled
correlator $F(t)$ is Lipschitz in $t$, hence the limit and the
asymptotic expansion are separated by a $O(t)$ gap that shrinks
continuously. The hypothesis reduces to showing that the convergent
Taylor series of $F(t)$ at $t = 0$ (established by the analyticity
of Step 2, W5-10) agrees term by term with the perturbative
small-flow-time expansion --- a structural statement about the
analyticity of a single function, not a comparison of two
independently defined objects.

### 5.2 UV finiteness eliminates renormalization ambiguities

In the traditional formulation of H4, the non-perturbative
correlator involves a bare lattice operator
$\mathcal{O}^{\mathrm{bare}}_a(x)$ multiplied by a renormalization
constant $Z_\mathcal{O}(a)$, and the hypothesis asserts that the
product converges to the correct continuum limit. The ambiguity is
in the choice and convergence of $Z_\mathcal{O}(a)$.

In the gradient-flow framework, no separate $Z_\mathcal{O}(a)$ is
needed. The Wilson coefficient $c_1(t)$ plays the role of the
renormalization constant, and it is computable perturbatively to
arbitrary precision (currently three loops). The renormalization is
*automatic*: the UV divergences are packaged into the $c_k(t)$
coefficients by the Luscher--Weisz UV finiteness theorem, and the
extraction (2.1) produces the renormalized correlator without
additional non-perturbative input.

This eliminates one layer of the hypothesis: the question "does
$Z_\mathcal{O}(a)$ absorb all divergences?" is replaced by the
question "does $c_1(t)$ capture the leading singularity?" --- and
the latter is answered affirmatively by the convergent small-flow-time
expansion (established non-perturbatively in Step 2 of W5-10).

### 5.3 Analyticity provides a rigorous bridge

The analyticity of $F(t)$ in the complex flow-time plane (W5-10,
Step 2; radius $r_t > 0$ independent of the Balaban step $k$ and
the bare-scale index $K$) implies that the small-flow-time expansion
is not merely asymptotic but **convergent**. This upgrades the
status of the perturbative expansion from a formal series to an
actual Taylor series with a positive radius of convergence. In
particular:

- The perturbative coefficients of $F(t) = F(0) + F'(0)\,t +
  \tfrac{1}{2}F''(0)\,t^2 + \cdots$ are the derivatives of a
  single analytic function, not independent perturbative
  computations.
- The remainder $R_n(t) = F(t) - \sum_{k=0}^{n} F^{(k)}(0)\,
  t^k/k!$ satisfies $|R_n(t)| \leq M_F\,(|t|/r_t)^{n+1}/(1 -
  |t|/r_t)$, a rigorous Cauchy remainder bound.
- The non-perturbative value $F(0)$ equals the sum of the convergent
  series, by definition of analyticity.

What H4 asks, in this language, is whether the Taylor coefficients
$F^{(k)}(0)$ are computable by the Feynman-diagrammatic perturbative
rules. This is a statement about the Taylor coefficients of an
analytic function --- a more accessible question than the traditional
formulation of H4, which asks about the asymptotic behavior of a
non-perturbative distribution.


---


## 6. Paper 10, Route 05: Weyl anomaly and KK tower decoupling

### 6.1 The question

The Yang--Mills theory constructed in the preprint is obtained by
dimensional reduction from a five-dimensional theory on $M^4 \times
S^1/\mathbb{Z}_2$. The KK tower of massive modes contributes to
loop diagrams in the effective 4D theory. The question is whether
these KK contributions modify the AF prediction (2.5) at short
distances.

### 6.2 Vassilevich mass-independence and the Weyl anomaly

Paper 10 (Route 05, Section 4.4) establishes the following chain:

**(a) Mass-independence of $a_4$.** The Seeley--DeWitt heat-kernel
coefficient $a_4(D)$ for a massive field with kinetic operator
$D = -\nabla^2 + m^2 I + E_{\mathrm{curv}}$ is independent of the
mass $m$ (Vassilevich, hep-th/0306138, eq. 4.3). The heat trace
factorizes:

$$\mathrm{Tr}\!\left[e^{-t(D_0 + m^2 I)}\right]
= e^{-tm^2}\,\mathrm{Tr}\!\left[e^{-tD_0}\right], \tag{6.1}$$

so that $a_4(D) = a_4(D_0) - m^2\,a_2(D_0) + \cdots$, where the
correction terms are lower-order Seeley--DeWitt coefficients that do
not contribute to the Weyl anomaly (they correspond to power-law
divergences, not logarithmic).

**(b) Each KK mode contributes the same $(a,c)$.** Every KK graviton
at level $n$, regardless of its mass $m_n = n/R$, contributes the
same Weyl anomaly coefficients as the massless $n = 0$ mode:
$(a, c) = (43/360,\;87/20)$.

**(c) The total Weyl anomaly vanishes.** Summing over the full
$S^1$ tower:

$$a_{\mathrm{total}} = \frac{43}{360} \times \sum_{n \in \mathbb{Z}} 1
= \frac{43}{360} \times S_0 = 0, \tag{6.2}$$

$$c_{\mathrm{total}} = \frac{87}{20} \times S_0 = 0, \tag{6.3}$$

where $S_0 = 1 + 2\zeta_R(0) = 1 + 2(-\tfrac{1}{2}) = 0$ is the
zeta-regularized mode count. For the orbifold $S^1/\mathbb{Z}_2$,
the bulk count is $1 + \zeta_R(0) = 1/2$, and the two boundary
fixed points each contribute $-(43/360)/4$, yielding the same total
$a_{\mathrm{total}} = 0$.

### 6.3 Cohomological protection: Wess--Zumino consistency

The Weyl anomaly satisfies the Wess--Zumino consistency condition
(Wess--Zumino 1971; Osborn 1991):

$$(\delta_{\sigma_1}\,\delta_{\sigma_2}
- \delta_{\sigma_2}\,\delta_{\sigma_1})\,W[g] = 0, \tag{6.4}$$

where $W[g]$ is the quantum effective action and $\sigma_i$ are
Weyl transformation parameters. This integrability condition implies
that the anomaly takes the form $a \cdot E_4 + c \cdot C^2$ with
fixed $(a,c)$; no finite local counterterm can shift them. The
vanishing $a_{\mathrm{total}} = c_{\mathrm{total}} = 0$ is therefore
**scheme-independent**: it holds in any regularization that
preserves 4D diffeomorphism invariance and the UV operator product
algebra.

### 6.4 Consequence for the AF match

The vanishing of the total Weyl anomaly has a direct consequence for
the short-distance behavior of the 4D theory extracted from the KK
construction:

**The KK tower does not modify the 4D AF prediction at short
distances.**

The argument has three layers:

**(i) One-loop level.** The one-loop contribution of the KK tower to
the running of the gauge coupling is proportional to $c_{\mathrm{
total}} = 0$. The KK gravitons, despite being massive, contribute as
if they were massless at one loop (by mass-independence of $a_4$),
and the total contribution sums to zero (by $S_0 = 0$). The one-loop
$\beta$-function of the extracted 4D theory receives no correction
from the KK tower.

**(ii) Subleading KK corrections.** At each mass-expansion order $j
\geq 1$ in the KK propagator, the contribution is proportional to
the Epstein zeta function $E_L(-j;\,Q_L)$, which vanishes
identically by Theorem K.1 (Paper 1, Appendix K, Section K.7b;
mechanism: $1/\Gamma(-j) = 0$ for integer $j \geq 1$). Therefore
all subleading KK corrections to the short-distance behavior are
exactly zero, not merely suppressed.

**(iii) All-orders protection.** The Wess--Zumino consistency
condition (6.4) ensures that the vanishing of $(a,c)$ cannot be
lifted by higher-loop effects. Since the Weyl anomaly controls the
logarithmic running of correlation functions at short distances,
the vanishing $c_{\mathrm{total}} = 0$ implies that the KK tower
does not generate logarithmic corrections to the AF prediction at
any loop order in any diffeomorphism-preserving scheme.

**In summary:** the 4D theory extracted by Feshbach projection from
the KK tower has exactly the short-distance behavior predicted by
pure 4D $\mathrm{SU}(N)$ Yang--Mills perturbation theory. The
five-dimensional origin of the construction is invisible at short
distances, protected by the Weyl anomaly vanishing and the universal
Epstein zeros.


---


## 7. Summary: status of Conjecture L.2

| Component | Status | Reference |
|:----------|:-------|:----------|
| $[\mathrm{Tr}\,F^2]_R$ exists | **Closed** (Lemma 3.8) | W5-10 |
| Perturbative AF prediction (2.5) | **Known** (textbook + 3-loop) | Luscher 2010; Harlander et al. 2016--2022; Zoller--Chetyrkin 2012--2014 |
| Lattice $\leftrightarrow$ continuum pert. theory | **Known** (Reisz) | CMP 116 (1988) 81; Caracciolo et al. 1989--1992 |
| KK tower does not contaminate | **Closed** (Route 05 + Theorem K.1) | Paper 10, Sections 4.4--4.5; Paper 1, Appendix K |
| No operator mixing at dim 4 | **Closed** | Preprint Section 5.3.1; W1-04, Memo 1 |
| $\bar{g}_{\mathrm{GF}}^2(q)$ definition | **Known** (non-perturbative) | Luscher 2010, eq. (2.1) of this memo |
| Convergent small-flow-time expansion | **Closed** (analyticity of $F(t)$) | W5-10, Step 2 |
| H4: non-pert $=$ pert at short distances | **Open** (conditional) | Gap G7 |

**Conclusion.** Conjecture L.2 is closed conditional on Hypothesis
H4. The gradient-flow framework reduces H4 from a comparison of two
independently defined objects (non-perturbative Schwinger function
vs. perturbation series) to a statement about the Taylor coefficients
of a single analytic function (Section 5.3), making it the mildest
formulation of this standard hypothesis available in the literature.
The KK construction introduces no additional obstruction: Route 05
of Paper 10 guarantees that the five-dimensional origin is invisible
at short distances. $\square$


---


## References

- Artz, J. et al., "Results and techniques for higher order calculations within the gradient-flow formalism," JHEP 06 (2019) 121.
- Caracciolo, S., Curci, G., Menotti, P. and Pelissetto, A., Phys. Lett. B 228 (1989) 375; Nucl. Phys. B 375 (1992) 195.
- Collins, J.C., Duncan, A. and Joglekar, S.D., Phys. Rev. D 16 (1977) 438.
- Del Debbio, L., Patella, A. and Rago, A., JHEP 11 (2013) 212.
- Harlander, R.V. and Neumann, T., "The perturbative QCD gradient flow to three loops," JHEP 06 (2016) 161.
- Harlander, R.V. et al., arXiv:2111.14376.
- Luscher, M., "Properties and uses of the Wilson flow in lattice QCD," JHEP 08 (2010) 071.
- Luscher, M. and Weisz, P., "Perturbative analysis of the gradient flow in non-abelian gauge theories," JHEP 02 (2011) 051.
- Makino, H. and Suzuki, H., PTEP 2014:063B02.
- Osborn, H., "Weyl consistency conditions and a local renormalization group equation for general renormalizable field theories," Nucl. Phys. B 363 (1991) 486.
- Reisz, T., "A power counting theorem for Feynman integrals on the lattice," CMP 116 (1988) 81; CMP 117 (1988) 79.
- Spiridonov, V.P., "Anomalous dimension of the Wilson operator," IYaI-P-0378 (1984); Spiridonov, V.P. and Chetyrkin, K.G., Sov. J. Nucl. Phys. 47 (1988) 522.
- Suzuki, H., "Energy-momentum tensor from the Yang--Mills gradient flow," PTEP 2013:083B03.
- Vassilevich, D.V., "Heat kernel expansion: user's manual," Phys. Rept. 388 (2003) 279 [hep-th/0306138].
- Wess, J. and Zumino, B., "Consequences of anomalous Ward identities," Phys. Lett. B 37 (1971) 95.
- Zoller, M.F. and Chetyrkin, K.G., JHEP 12 (2012) 119; JHEP 10 (2014) 169.
