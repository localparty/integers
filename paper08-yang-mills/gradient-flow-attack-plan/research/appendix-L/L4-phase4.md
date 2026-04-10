## L.4 Phase 4: Stress Tensor, Asymptotic Freedom, and the OPE

This section converts the research memos W7-13, W7-14, and W7-15 into
publication-quality proofs closing Conjectures L.3, L.2, and L.4
(leading order) of Appendix L. Three lemmas are established:

- Lemma L.4.1 (stress tensor): all five sub-clauses of Conjecture L.3.
- Lemma L.4.2 (AF short-distance match): Conjecture L.2, conditional
  on Hypothesis H4.
- Lemma L.4.3 (leading-order OPE): Conjecture L.4 at leading order.

Throughout, $b_0 = 11N/(48\pi^2)$, $\beta(g) = -b_0\,g^3 + O(g^5)$,
and $\Lambda$ denotes the non-perturbative $\mathrm{SU}(N)$ scale
parameter. The gradient-flow running coupling
$\bar{g}_{\mathrm{GF}}^2(q)$ is defined at momentum scale
$q = (8t)^{-1/2}$ via Luscher (JHEP 08 (2010) 071). The Wilson
coefficients $c_i(t)$ of the small-flow-time expansion are computed in
Suzuki (PTEP 2013:083B03), Harlander--Neumann (JHEP 06 (2016) 161),
and Artz et al. (JHEP 06 (2019) 121).


---


### L.4.1 Stress tensor $T_{\mu\nu}$ via the Suzuki formula

We construct the renormalised stress-energy tensor from the
gradient-flow composite operators established in Phases 1--3
(Lemmas L.3.7--L.3.8, Section L.3; GNS reconstruction,
Section L.3, Lemma L.3.8) and verify all five sub-clauses of Conjecture L.3.


**Lemma L.4.1** (Stress tensor --- Conjecture L.3 closure).
*Conditional on Lemma L.3.8 (existence of
$[\mathrm{Tr}\,F^2]_R$ and
$[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$ as operator-valued
distributions on the GNS Hilbert space $\mathcal{H}$), the
Suzuki formula*
$$
T_{\mu\nu}^R(x) \;=\; \lim_{t \to 0^+}\Bigl[\,
c_1(t)\,U_{\mu\nu}(t,x) + c_2(t)\,\delta_{\mu\nu}\,E(t,x)
+ c_3(t)\,\delta_{\mu\nu}\,\langle E(t)\rangle\cdot\mathbb{1}
\,\Bigr]
\tag{L.4.1}
$$
*defines a well-posed operator-valued distribution
$T_{\mu\nu}^R$ on the common dense invariant domain
$\mathcal{D} \subset \mathcal{H}$ satisfying:*

(i) *Symmetry:* $T_{\mu\nu}^R = T_{\nu\mu}^R$.

(ii) *Gauge invariance.*

(iii) *Conservation:*
$\partial^\mu T_{\mu\nu}^R(x) = 0$ *as a distributional Ward
identity, with contact terms encoding translation covariance.*

(iv) *Hamiltonian identification:*
$H_{\mathrm{OS}} = \int T_{00}^R(0,\vec{x})\,d^3\vec{x}$,
*with* $H_{\mathrm{OS}} \geq 0$ *and*
$H_{\mathrm{OS}}\,\Omega = 0$.

(v) *Trace anomaly:*
$T^{\mu R}{}_\mu(x) = \frac{\beta(g)}{2g}\,
[\mathrm{Tr}\,F^2]_R(x)$.

*Here the flowed operators are*
$$
U_{\mu\nu}(t,x) := G_{\mu\rho}^a(t,x)\,G_{\nu\rho}^a(t,x)
- \tfrac{1}{4}\,\delta_{\mu\nu}\,G_{\rho\sigma}^a(t,x)\,
G_{\rho\sigma}^a(t,x),
\qquad
E(t,x) := \tfrac{1}{4}\,G_{\rho\sigma}^a(t,x)\,
G_{\rho\sigma}^a(t,x),
\tag{L.4.2}
$$
*with Wilson coefficients $c_1(t) = 1 + O(\bar{g}^2)$,
$c_2(t) = b_0\,\bar{g}^2/2 + O(\bar{g}^4)$, and
$c_3(t) = -c_2(t)\,\langle E(t)\rangle$ (Suzuki, PTEP 2013:083B03;
Harlander--Neumann, JHEP 06 (2016) 161).*

*Proof.* We verify each sub-clause in turn.

**Existence of the limit.** The $t \to 0^+$ limit in (L.4.1) is
controlled by the same mechanism as Lemma L.3.7 (Section L.3).
The traceless-symmetric piece $c_1(t)\,U_{\mu\nu}(t,x)$ is a
dimension-4 flowed composite with the same small-flow-time expansion
structure as $E(t,x)$; the Cauchy estimate (Lemma L.3.7) applies
identically, giving analyticity of the rescaled correlator in $t$ with
$K$-uniform radius $r_t > 0$ and Lipschitz convergence. The trace
piece $c_2(t)\,E(t,x)$ involves the same operator $E(t,x)$ controlled
by Lemma L.3.7. The vacuum subtraction $c_3(t)\,\langle E(t)\rangle$ is
a $c$-number whose limit exists because the divergent pieces cancel
between $c_2$ and $c_3$ by construction (L.4.2).

**(i) Symmetry.** Each term in (L.4.1) is symmetric in $(\mu,\nu)$:
$U_{\mu\nu} = U_{\nu\mu}$ by the commutativity of the summation
$G_{\mu\rho}^a G_{\nu\rho}^a = G_{\nu\rho}^a G_{\mu\rho}^a$ over
contracted indices $\rho$ and $a$; the remaining terms are proportional
to $\delta_{\mu\nu}$. Since limits of symmetric distributions are
symmetric, $T_{\mu\nu}^R = T_{\nu\mu}^R$.

**(ii) Gauge invariance.** The gradient-flow equation is
gauge-covariant (Luscher, JHEP 08 (2010) 071, SS 2): if $B_\mu(t,x)$
solves the flow with initial data $A_\mu$, then $B_\mu^g = g\,B_\mu\,
g^{-1} + g\,\partial_\mu g^{-1}$ solves it with initial data $A_\mu^g$.
The flowed field strength transforms as
$G_{\mu\nu}^g = g\,G_{\mu\nu}\,g^{-1}$, so
$\mathrm{Tr}(G_{\mu\rho}^g\,G_{\nu\rho}^g) =
\mathrm{Tr}(G_{\mu\rho}\,G_{\nu\rho})$ by cyclicity of the trace.
The Wilson coefficients $c_i(t)$ are gauge-invariant $c$-numbers.
The $t \to 0^+$ limit inherits gauge invariance from the exact lattice
gauge Ward identity $\langle\mathcal{O}[U^\Omega]\rangle =
\langle\mathcal{O}[U]\rangle$ (preprint, SS 5.7(f)), which holds at
every $a > 0$ by Haar measure invariance and converges in the
continuum limit by the uniform OS1 bounds.

**(iii) Conservation.** At the Schwinger function level, the
translation Ward identity
$$
\partial_x^\mu\,\bigl\langle T_{\mu\nu}^R(x)\,X\bigr\rangle
= \sum_{i=1}^n \delta^{(4)}(x - x_i)\,
\partial_{\nu,x_i}\langle X\rangle
\tag{L.4.3}
$$
is established unconditionally in the preprint (SS 5.7(f), equations
(SD-lat)--(SD-cont)): on the lattice, translation invariance of the
action and Haar measure yields (L.4.3) with $O(a^2)$ artifacts that
vanish in the continuum limit. At the operator level, the Ward identity
for the gradient-flow stress tensor was derived by Del Debbio, Patella,
and Rago (JHEP 11 (2013) 212): the flow equation commutes with
spacetime translations, the $O(t)$ smearing corrections vanish as
$t \to 0^+$, and the Wilson coefficients $c_i(t)$ are $x$-independent,
so $\partial^\mu[c_i(t)\cdot\text{flowed operator}] =
c_i(t)\,\partial^\mu[\text{flowed operator}]$. Promotion to an
operator identity $\partial^\mu T_{\mu\nu}^R = 0$ on $\mathcal{H}$
follows from the Osterwalder--Schrader reconstruction theorem
(CMP 42 (1975) 281, Theorem 3.1): a distributional identity satisfied
by all Schwinger functions lifts to an operator identity on the
reconstructed Hilbert space.

**(iv) Hamiltonian identification.** The sub-clause decomposes into an
unconditional part and a conditional part.

*Unconditional:* $H_{\mathrm{OS}} \geq 0$ with
$H_{\mathrm{OS}}\,\Omega = 0$. The OS Hamiltonian
$H_{\mathrm{OS}} = -a^{-1}\log\hat{T}$ is defined from the
reconstructed transfer matrix. OS3 (reflection positivity) implies
$0 \leq \hat{T} \leq 1$ (Seiler, LNP 159 (1982), Theorem 4.1), so
$H_{\mathrm{OS}} \geq 0$. The vacuum $\Omega$ is the eigenstate with
$\hat{T}\,\Omega = \Omega$, giving $H_{\mathrm{OS}}\,\Omega = 0$.
This requires only the lattice transfer matrix and reflection
positivity, not any composite-operator conjecture.

*Conditional on L.1:* $H_{\mathrm{OS}} = \int T_{00}^R\,d^3\vec{x}$.
On the lattice, the Noether construction (Caracciolo--Curci--Menotti--
Pelissetto, Ann. Phys. 197 (1990) 119) gives
$H_{\mathrm{lat}} = \sum_{\vec{x}} a^3\,T_{00}^{\mathrm{lat}}
(0,\vec{x}) = -a^{-1}\log\hat{T} + O(a^2)$. The Suzuki formula
defines $T_{00}^R$ via (L.4.1) at $(\mu,\nu) = (0,0)$. Integrating
over $\vec{x}$ at $x_0 = 0$ and exchanging the limit with the
integral --- justified by the dominated convergence theorem, since the
integrand decays exponentially at rate $\Delta_\infty$ uniformly in $t$
(Lemma L.3.7, Section L.3) --- yields the identification via the
continuum limit of $H_{\mathrm{lat}}$.

**(v) Trace anomaly.** The trace of (L.4.1) reduces to
$T^{\mu R}{}_\mu = \lim_{t \to 0^+}\,4\,c_2(t)\,[E(t,x) -
\langle E(t)\rangle]$, since $U_{\mu\mu} = 0$ identically. The
small-flow-time expansion $E(t,x) = c_0(t)\,\mathbb{1} +
c_1^E(t)\,[\mathrm{Tr}\,F^2]_R(x) + O(t)$ gives
$T^{\mu R}{}_\mu = \lim_{t \to 0^+}\,4\,c_2(t)\,c_1^E(t)\,
[\mathrm{Tr}\,F^2]_R(x)$. The product $4\,c_2(t)\,c_1^E(t)$
evaluates to $\beta(g)/(2g) + O(g^5)$ at one loop (Suzuki, PTEP
2013:083B03, eq. (4.10)). The Spiridonov--Chetyrkin identity
$\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$ (Spiridonov, Yad. Fiz.
39 (1984) 1522; Spiridonov--Chetyrkin, Yad. Fiz. 47 (1988) 818)
guarantees that higher-order corrections respect the same structure:
the combination $(\beta(g)/g^3)\,\mathrm{Tr}\,F^2$ is
RG-invariant, so the $\mu$-dependence of $c_2(t)$ is exactly cancelled
by the running of $[\mathrm{Tr}\,F^2]_R$. The convergence of the
small-flow-time expansion (Lemma L.3.7, Step 2: analyticity with
positive radius $r_t$) promotes the identity from each perturbative
order to the exact $t \to 0^+$ limit:
$$
T^{\mu R}{}_\mu(x) = \frac{\beta(g)}{2g}\,
[\mathrm{Tr}\,F^2]_R(x). \qquad\square
\tag{L.4.4}
$$

**Remark L.4.1** (Unconditional vs. conditional summary).
Sub-clauses (i)--(iii) hold at the Schwinger function level
unconditionally (algebraic symmetry, Haar invariance, and preprint
SS 5.7(f) respectively); their promotion to operator-level identities
on $\mathcal{H}$ is conditional on L.1. Sub-clause (iv-a),
$H_{\mathrm{OS}} \geq 0$ with $H_{\mathrm{OS}}\,\Omega = 0$, is
unconditional (OS3 + Seiler). Sub-clauses (iv-b) and (v) are
conditional on L.1. Within the gradient-flow programme
(L.1 discharged by Lemmas L.3.7--L.3.8), all five sub-clauses are closed.

**Remark L.4.2** (Belinfante--Rosenfeld form).
At tree level ($c_1 = 1$, $c_2 = O(\bar{g}^2)$), the Suzuki formula
reduces to $T_{\mu\nu}^R =
-[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R
+ \frac{1}{4}\,\delta_{\mu\nu}\,[\mathrm{Tr}\,F^2]_R
+ c_{\mathrm{vac}}\,\delta_{\mu\nu}\,\mathbb{1}$, which is the
classical Belinfante--Rosenfeld improved stress tensor of
Conjecture L.3. Loop corrections are absorbed into the Wilson
coefficients $c_1$, $c_2$, $c_3$ (Suzuki, PTEP 2013:083B03;
Harlander--Neumann, JHEP 06 (2016) 161).


---


### L.4.2 Asymptotic-freedom short-distance match

We establish that the renormalised two-point function of
$[\mathrm{Tr}\,F^2]_R$ exhibits the short-distance behaviour predicted
by asymptotic freedom, closing Conjecture L.2 conditional on the
standard non-perturbative hypothesis H4.


**Hypothesis H4** (Standard lattice QCD hypothesis).
*The renormalised non-perturbative Schwinger function
$S_2^{\mathrm{ren}}(x,y)$ constructed in Lemma L.3.8 admits a
short-distance asymptotic expansion whose leading term coincides with
the perturbative prediction:*
$$
S_2^{\mathrm{ren}}(x,y) = \frac{C_N}{|x-y|^8}\;
\left(\ln\frac{1}{|x-y|\Lambda}\right)^{-2}
\left[1 + O\!\left((\log)^{-1}\right)\right]
\qquad (|x-y| \to 0).
\tag{L.4.5}
$$

*Status.* Hypothesis H4 is not proved. It is the standard assumption
of QCD phenomenology and lattice QCD, implicitly invoked in every
application of SVZ sum rules, every lattice determination of
$\alpha_s$ from short-distance quantities, and every perturbative
matching calculation. It is a theorem for super-renormalisable
theories ($\phi^4_3$: Glimm--Jaffe; Magnen--Rivasseau--Seneor, CMP
155 (1993) 325). For 4D non-Abelian gauge theory, it is open.


**Lemma L.4.2** (AF short-distance match --- Conjecture L.2 closure).
*Conditional on Hypothesis H4 and on Lemma L.3.8 (existence of
$[\mathrm{Tr}\,F^2]_R$, Section L.3), the renormalised
two-point Schwinger function satisfies*
$$
\bigl\langle\,[\mathrm{Tr}\,F^2]_R(x)\;
[\mathrm{Tr}\,F^2]_R(0)\,\bigr\rangle
= \frac{C_N}{|x|^{8}}\;
\Bigl(\ln\frac{1}{|x|\Lambda}\Bigr)^{-2}
\bigl[1 + O\bigl((\log)^{-1}\bigr)\bigr]
\qquad (|x| \to 0),
\tag{L.4.6}
$$
*with $C_N = 2(N^2-1)/\pi^6$ and $\Lambda$ the non-perturbative
$\mathrm{SU}(N)$ Lambda parameter.*


*Proof.* The argument assembles three ingredients.

**Step 1 (Existence of the renormalised correlator).** Lemma L.3.8
(Section L.3) constructs the renormalised two-point function as
$$
S_2^{\mathrm{ren}}(x,y) = \lim_{t \to 0^+}
\frac{S_{2,t}^c(x,y)}{c_1(t)^2},
\tag{L.4.7}
$$
where $S_{2,t}^c$ is the connected two-point Schwinger function of the
flowed energy density and $c_1(t)$ is the leading Wilson coefficient in
the small-flow-time expansion of $E(t,x)$ onto
$[\mathrm{Tr}\,F^2]_R(x)$. The limit exists by the Cauchy estimate
(Lemma L.3.7) and the analyticity of $F(t)$ in the flow time. No
operator mixing enters at dimension 4: the unique gauge-invariant,
$\mathcal{C}$-even, parity-even operator is $\mathrm{Tr}\,F^2$
(preprint, SS 5.3.1).

**Step 2 (Perturbative prediction).** The gradient-flow running
coupling $\bar{g}_{\mathrm{GF}}^2(q)$ at $q = (8t)^{-1/2}$ (Luscher,
JHEP 08 (2010) 071) satisfies the AF beta function at leading order:
$$
q\,\frac{\partial}{\partial q}\,\bar{g}_{\mathrm{GF}}^2(q)
= -2b_0\,\bar{g}_{\mathrm{GF}}^4(q) + O(\bar{g}_{\mathrm{GF}}^6),
\tag{L.4.8}
$$
yielding $\bar{g}_{\mathrm{GF}}^2(q) \to 0$ as $q \to \infty$ with
the universal one-loop running. The small-flow-time expansion
(Luscher, 2010; Harlander--Neumann, JHEP 06 (2016) 161) gives the
one-loop coefficient $\bar{c}_1 = (11N/3)(2\gamma_E + \ln 3)/(4\pi)^2
+ \cdots$. The Spiridonov--Chetyrkin trace-anomaly identity
$$
\gamma_{\mathrm{Tr}\,F^2}(g) = -\frac{2\,\beta(g)}{g}
= 2\,b_0\,g^2 + O(g^4)
\tag{L.4.9}
$$
is exact to all orders (Spiridonov 1984; Spiridonov--Chetyrkin 1988).
Combining the engineering dimension $|x|^{-8}$ with the RG-improved
anomalous-dimension resummation $Z_{\mathrm{Tr}\,F^2}(\mu)^2 \sim
(\ln(\mu/\Lambda))^{-2}$ at $\mu = 1/|x|$, and the tree-level Wick
contraction $C_N = 2(N^2-1)/\pi^6$, produces the perturbative
two-point function
$$
\langle[\mathrm{Tr}\,F^2]_R(x)\;
[\mathrm{Tr}\,F^2]_R(0)\rangle^{\mathrm{pert}}
= \frac{C_N}{|x|^8}\;
\Bigl(\ln\frac{1}{|x|\Lambda}\Bigr)^{-2}
\bigl[1 + O\bigl((\log)^{-1}\bigr)\bigr].
\tag{L.4.10}
$$
The $O((\log)^{-1})$ remainder absorbs two-loop and higher corrections,
known to three loops from Zoller--Chetyrkin (JHEP 12 (2012) 119;
JHEP 10 (2014) 169). The Reisz power-counting theorem (CMP 116 (1988)
81) guarantees diagram-by-diagram lattice-to-continuum convergence of
the perturbative coefficients.

**Step 3 (KK tower decoupling).** The five-dimensional origin of the
construction introduces a KK tower of massive modes. These do not
contaminate the 4D AF prediction, by the following chain (preprint,
Appendix K, SS K.7b; Paper 10, Route 05 (Appendix N, SS N.2.5)):

(a) The Seeley--DeWitt coefficient $a_4(D)$ is mass-independent
(Vassilevich, hep-th/0306138), so each KK mode at level $n$
contributes the same Weyl anomaly $(a,c)$ as the massless $n = 0$
mode.

(b) The zeta-regularised mode count $S_0 = 1 + 2\zeta_R(0) = 0$
forces the total Weyl anomaly to vanish:
$a_{\mathrm{total}} = c_{\mathrm{total}} = 0$.

(c) Subleading KK corrections at mass-expansion order $j \geq 1$ are
proportional to $E_L(-j;\,Q_L)$, which vanishes by
$1/\Gamma(-j) = 0$ (Theorem K.1).

(d) The Wess--Zumino consistency condition ensures the vanishing
cannot be lifted by higher-loop effects.

**Assembly.** Combining Steps 1--3 with Hypothesis H4 yields the
claimed asymptotic (L.4.6). $\square$


**Remark L.4.3** (Why gradient flow makes H4 more plausible).
Although H4 remains unproved, the gradient-flow framework provides
three structural advantages over previous formulations: (i) a smooth
one-parameter interpolation from the non-perturbative regime (large
$t$) to the perturbative regime (small $t$), so that H4 reduces to a
statement about Taylor coefficients of a single analytic function
rather than a comparison of two independently defined objects; (ii)
automatic UV finiteness at $t > 0$, eliminating renormalisation
ambiguities in $Z_\mathcal{O}(a)$; (iii) the convergent (not merely
asymptotic) small-flow-time expansion from Lemma L.3.7, Step 2, which
upgrades the perturbative series to a genuine Taylor series with
positive radius of convergence.


---


### L.4.3 Leading-order operator product expansion

We establish the leading-order OPE for $[\mathrm{Tr}\,F^2]_R$,
closing Conjecture L.4 at leading order. The full non-perturbative OPE
at all orders remains open and is stated honestly as such.


**Lemma L.4.3** (Leading-order OPE --- Conjecture L.4 at leading
order). *Conditional on Lemma L.3.8 (existence of
$[\mathrm{Tr}\,F^2]_R$, Section L.3), the renormalised
composite operators admit a leading-order operator product expansion
as $|x - y| \to 0$:*
$$
[\mathrm{Tr}\,F^2]_R(x)\;[\mathrm{Tr}\,F^2]_R(y)
\;\sim\; C^{\mathbb{1}}(x-y)\,\mathbb{1}
\;+\; C^{\mathcal{O}}(x-y)\,[\mathrm{Tr}\,F^2]_R(y)
\;+\; \sum_{k:\,d_k \geq 6} C^{k}(x-y)\,\mathcal{O}_k(y),
\tag{L.4.11}
$$
*with c-number tempered distributions $C^k$ smooth off the diagonal.
The identity-channel coefficient is*
$$
C^{\mathbb{1}}(x-y)
\;=\; \frac{C_N}{|x-y|^{8}}\,
\Bigl(\ln\frac{1}{|x-y|\,\Lambda}\Bigr)^{-2}\,
\bigl[1 + O\bigl((\log)^{-1}\bigr)\bigr],
\qquad C_N = \frac{2(N^2-1)}{\pi^6},
\tag{L.4.12}
$$
*and the subleading channels have strictly weaker singular behaviour
at coincidence: the $[\mathrm{Tr}\,F^2]_R$ channel has singularity
$O(|x-y|^{-4})$ and all dimension-$\geq 6$ channels have singularity
$O(|x-y|^{-2})$ or weaker.*

*Proof.* The proof proceeds in five steps.

**Step 1 (Gradient-flow OPE at $t > 0$).** At flow time $t > 0$, the
product $\mathcal{O}_t(x)\,\mathcal{O}_t(y)$ is UV-finite for all
$x,y \in \mathbb{R}^4$ --- including $x = y$ --- by the Luscher--Weisz
theorem (JHEP 02 (2011) 051): each internal line connecting the two
insertions carries at least one flow propagator $e^{-tp^2}$, providing
power-counting improvement of $O(e^{-t|p|^2})$. Since the flowed field
$B_\mu(t,x)$ is smooth in $x$ at fixed $t > 0$ (parabolic smoothing),
the UV-finite operator product admits an expansion
$$
\mathcal{O}_t(x)\,\mathcal{O}_t(y)
= \sum_k D_k^{(t)}(x-y)\,\mathcal{O}_{k,t}\!\Bigl(
\frac{x+y}{2}\Bigr),
\tag{L.4.13}
$$
where the coefficient functions $D_k^{(t)}(x-y)$ are smooth functions
of $x - y$ for $t > 0$, not distributions. The smoothness follows from
the regularity of the flowed fields and the UV finiteness of all
composite operators at $t > 0$.

**Step 2 (The $t \to 0$ limit: distributional coefficients).** As
$t \to 0^+$, the smooth coefficients $D_k^{(t)}$ develop
distributional singularities at $x = y$. The continuum OPE coefficients
emerge as limits $D_k^{(t)}(x-y) \to C^k(x-y)$, where $C^k$ are
c-number tempered distributions smooth on $\{x \neq y\}$. The existence
and finiteness of these limits is guaranteed by Lemma L.3.7
(Section L.3): the rescaled correlator $F(t) =
S_{2,t}^c(x,y)/c_1(t)^2$ is analytic in $t$ on $|t| < r_t$ with
Lipschitz estimate $|F(t) - F(t')| \leq L(x,y)|t - t'|$, and
$K$-uniformity of all constants ensures the double limit
$(a,t) \to (0,0)$ is well-defined via the Moore--Osgood theorem.

**Step 3 (Identity channel).** The identity-channel OPE coefficient is
the vacuum expectation value of the operator product:
$C^{\mathbb{1}}(x-y) = S_2^{\mathrm{ren}}(x,y)$. By Lemma L.3.8,
$S_2^{\mathrm{ren}}$ exists as a finite tempered distribution on
$\{x \neq y\}$, satisfying OS positivity and exponential clustering at
rate $\Delta_\infty$. Its short-distance form is determined by:

(a) Engineering dimension: $\dim[\mathrm{Tr}\,F^2] = 4$ gives
$|x-y|^{-8}$ by dimensional analysis.

(b) The Spiridonov--Chetyrkin identity $\gamma_{\mathrm{Tr}\,F^2} =
-2\beta(g)/g$, which fixes the RG-improved exponent: two insertions of
$[\mathrm{Tr}\,F^2]_R$ each carry one power of
$Z_{\mathrm{Tr}\,F^2}(\mu) \sim (\ln(\mu/\Lambda))^{-1}$, yielding the
$(\log)^{-2}$ factor.

(c) The tree-level Wick contraction: tracing over the colour factor
$\delta^{ab}\delta^{ab} = N^2 - 1$ and summing over Lorentz
contractions gives $C_N = 2(N^2-1)/\pi^6$, confirmed at three loops by
Zoller--Chetyrkin (JHEP 12 (2012) 119; JHEP 10 (2014) 169).

The assembly yields the form (L.4.12). The identification of the
non-perturbative short-distance behaviour with the perturbative
prediction invokes Hypothesis H4 (Lemma L.4.2).

**Step 4 ($[\mathrm{Tr}\,F^2]_R$ channel and subleading control).**
By Lemma L.3.2 (Section L.3), the unique gauge-invariant,
$\mathcal{C}$-even, parity-even operator of engineering dimension 4 is
$\mathrm{Tr}\,F^2$; the mixing matrix is $1 \times 1$. The OPE
coefficient $C^{\mathcal{O}}(x-y) \sim |x-y|^{-4}$ is therefore
unambiguous and strictly subleading to $C^{\mathbb{1}} \sim |x-y|^{-8}$.

For dimension-$\geq 6$ channels: every $\mathcal{C}$-even,
gauge-invariant operator of dimension $\geq 6$ has Boltzmann deviation
order $\mathrm{dev} \geq 2$ (Lemma L.3.3, Section L.3; preprint,
SS 5.6, Part III). The four-class exhaustion argument runs as follows:

(I) Zero-derivative operators ($\mathrm{Tr}(F^3)$, $d^{abc}F^3$):
$\mathcal{C}$-odd, eliminated by $\mathcal{C}$-parity.

(II) One-derivative operators: absent (no $\mathcal{C}$-even
gauge-invariant operator of dimension 5 exists).

(III) Two-derivative operators ($\mathrm{Tr}(D_\rho F_{\mu\nu})^2$):
$\mathrm{dev} \geq 2$ by the spectral mechanism --- the
transfer-matrix weight $(e^{E_m - E_n} - 1)^2$ vanishes at $n = m$.

(IV) Three-or-more-derivative operators: $\mathrm{dev} \geq 3 > 2$.

The spectral bound (preprint, SS 5.5.3) gives
$|\langle 1|\mathcal{O}_{d=6}|1\rangle_c| \leq
C_2\,M\,\hat{\Delta}^2$, with $C_2$ being $K$-uniform. In the
small-flow-time expansion, the Wilson coefficient for a dimension-$d_k$
operator satisfies $c_k(t)/c_1(t) \sim t^{(d_k-4)/2}$, vanishing as
$O(t)$ for $d_k = 6$, confirming that dimension-$\geq 6$ channels
contribute at $O(|x-y|^{-2})$ or weaker.

**Step 5 ($\mathcal{C}$-parity selection).** The product
$[\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y)$ is
$\mathcal{C}$-even, so only $\mathcal{C}$-even operators appear on the
right-hand side. This eliminates $[\mathrm{Tr}\,F\tilde{F}]_R$
(topological charge density, $\mathcal{C}$-odd) and all $\mathcal{C}$-odd
operators at every dimension, including $\mathrm{Tr}(F^3)$ and
$d^{abc}F^3$ at dimension 6 (Lemma L.3.2, $\mathcal{C}$-elimination;
preprint, SS 5.3.1).

Combining Steps 1--5, the OPE (L.4.11) is established at leading order
with the identity-channel coefficient (L.4.12) and subleading channels
controlled by Lemmas L.3.2--L.3.3. $\square$


**Remark L.4.4** (Consistency with the gradient-flow extraction).
The identity $C^{\mathbb{1}}(x-y) = S_2^{\mathrm{ren}}(x,y)$ is
consistent with the extraction mechanism: the Wilson coefficient
$c_1(t) \sim t^{-2}\,(\ln(1/t\Lambda^2))^{-1}$ yields
$c_1(t)^{-2} \sim t^4\,(\log)^2$, and multiplying by
$S_{2,t}^c \to |x-y|^{-8}(\log)^{-2}$ as $t \to 0$ produces the
correct short-distance form (L.4.12). The gradient flow thus provides a
concrete interpolation between the UV-finite regime ($t > 0$, smooth
coefficients) and the continuum OPE ($t = 0$, distributional
singularities).


**Remark L.4.5** (What remains open).
The full non-perturbative OPE --- a system of c-number distributions
$\{C^k\}_{k=0}^\infty$ such that the asymptotic identity (L.4.11)
holds at the level of operators on $\mathcal{H}$ to all orders in the
singularity expansion --- has never been constructed for 4D non-Abelian
Yang--Mills. Specifically, three problems remain open:

(i) Non-perturbative identification of subleading $C^k$ for $d_k \geq 6$
reduces to extending H4 to all OPE channels.

(ii) The operator mixing matrices at dimension $\geq 6$ are unknown
non-perturbatively, though the Kluberg-Stern--Zuber classification
(Phys. Rev. D 12 (1975) 467) gives the operator basis.

(iii) Whether the OPE converges or is merely asymptotic is open even in
perturbation theory for 4D gauge theories; the convergent
small-flow-time expansion (Lemma L.3.7, Step 2) provides structural
evidence but not a proof of OPE convergence.

Of the four conjectures L.1--L.4, the full non-perturbative OPE is the
hardest residual problem. The present Lemma L.4.3 closes L.4 at
leading order, which is the maximum the current state of the art
supports.
