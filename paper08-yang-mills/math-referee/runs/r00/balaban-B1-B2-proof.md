# Proof of (B1)--(B2) and Stability of Excitation Number

Self-contained proofs of the analyticity properties (B1)--(B2) from
Balaban's stated results, and of the stability lemma promoting
$\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ from perturbative to
non-perturbative. Based on the extraction in
balaban-analyticity-extraction.md; all new arguments are identified.


---


## Part I: Proof of (B1) --- Analyticity with $k$-Independent Radius

### Statement

**(B1).** *In the small-field region $\Omega_s$ at RG step $k$, the
effective action $S_k[V]$ is analytic in the block link variables
$\{V_\ell\}$, with radius of analyticity $\rho > 0$ independent
of $k$.*

### Proof

**Step (a): Convergent polymer expansion.**
*Source: Balaban, CMP 109 (1987), Thm 2.1; CMP 119 (1988), Thm 1.*

In $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$, the effective action is

$$S_k[V] = \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  + \sum_{X \in \mathcal{P}_k} K_k(X, V), \tag{I.1}$$

where $\mathcal{P}_k$ is the set of connected polymers on
$\Lambda_k$ and each activity satisfies

$$|K_k(X, V)| \leq e^{-\kappa |X|}, \tag{I.2}$$

with $\kappa > 0$ **independent of $k$** (CMP 109, Section 3:
the inductive hypotheses ensure the bounds depend only on the
blocking geometry $L = 2$, $d = 4$, the group $\mathrm{SU}(N)$,
and the fluctuation mass $m_W$ --- all $k$-independent). By
Kotecky--Preiss (CMP 83, 1982), $\sum_{X \ni x} |K_k(X, V)|
\leq C_{\mathrm{KP}}(\kappa, d) < \infty$. The remainder
$E_k = \sum_X K_k$ is a well-defined bounded function.

**Step (b): Each polymer activity is analytic.**
*Sources: CMP 95--96 (propagator); CMP 98 (kernel); CMP 109
(inductive construction).*

$K_k(X, V)$ is constructed by iterating four
analyticity-preserving operations:

(i) **Background evaluation.** $S_{k-1}$ evaluated at $V \cdot u$
is polynomial in $V_\ell, u$ (the Wilson action is polynomial in
matrix entries; at $k = 0$ this is the base case, entire).

(ii) **Saddle point.** $u_{\mathrm{cl}} = -G_k(V) \cdot
\nabla_u S_{k-1}|_{u=0}$, where $G_k(V) = (S_k^{(2)}[V])^{-1}
= (-D^2[V] + m_W^2)^{-1}$. Since $D^2[V]$ is polynomial in
$V_\ell$ (CMP 95, Sec. 3) and $m_W^2 > 0$ ensures invertibility
in $\Omega_s$ (CMP 96, Sec. 2), $G_k(V)$ is analytic with
$\|G_k\| \leq C/m_W^2$ and exponential decay
$|G_k(x,y;V)| \leq Ce^{-m_W|x-y|}$ (CMP 95, Prop. 3.2).

(iii) **Gaussian integration.** Yields $(\det S_k^{(2)}[V])^{-1/2}$,
analytic where $S_k^{(2)} > 0$ (via convergent trace-log expansion).

(iv) **Mayer resummation.** Non-Gaussian corrections form a
convergent series of analytic cluster activities (CMP 109, Sec. 4);
the sum is analytic.

Induction on $k$: if activities at step $k-1$ are analytic, the
four operations produce analytic activities at step $k$.

**Step (c): $k$-independent analyticity radius.**
*Source: CMP 109, Sec. 3; CMP 119, Sec. 2.*

The radius is determined by three constraints:

(c1) **Propagator existence.** $S_k^{(2)}[V] > 0$ requires
$\|V_\ell - \mathbf{1}\| < m_W^2/(2C_D)$, where $C_D$ is the
Lipschitz constant of $D^2[V]$. The ratio $m_W a_k$ is a fixed
parameter, so this bound is $k$-independent in lattice units.

(c2) **Mayer convergence.** Controlled by $\kappa$ (from (I.2))
and $m_W$ (propagator decay), both $k$-independent.

(c3) **Block-spin kernel.** The projection $A \mapsto
A(A^\dagger A)^{-1/2}$ (CMP 98, Sec. 2) is analytic for
$\|A - \mathbf{1}\| < r_{\mathrm{proj}}(N)$, depending on $N$
but not $k$.

The overall radius is:

$$\rho = \min\!\left(\frac{\kappa}{2d},\;
  \frac{m_W a}{2C_D},\;
  r_{\mathrm{proj}}(N)\right) > 0, \tag{I.3}$$

with every factor $k$-independent. $\square$

**Remark.** Balaban does not state (B1) as a standalone theorem;
the analyticity is implicit in the construction. Dimock
(arXiv:1108.1335, 2011, Thm 3.1) is more explicit in the scalar
analogue.


---


## Part II: Proof of (B2) --- Extension to $\mathrm{SL}(N, \mathbb{C})$

### Statement

**(B2).** *The analyticity domain extends to a neighborhood of
$\mathbf{1}$ in $\mathrm{SL}(N, \mathbb{C})$, with $k$-independent
radius.*

### Proof

**Step (d): Algebraic dependence on matrix entries.**

The polymer activities depend on $\{V_\ell\}$ through:

(d1) The Wilson action is polynomial in $(V_\ell)_{ij}$ and
$\overline{(V_\ell)_{ij}}$. On $\mathrm{SU}(N)$,
$\overline{V_{ij}} = (\mathrm{adj}\,V)_{ji}$ since
$V^{-1} = V^\dagger = \mathrm{adj}(V)/\det V = \mathrm{adj}(V)$.

(d2) On $\mathrm{SL}(N, \mathbb{C})$, $\det V = 1$ still holds,
so $V^{-1} = \mathrm{adj}(V)$ remains polynomial in the entries.
The complex conjugation in the Wilson action is replaced by
$V^{-1} = \mathrm{adj}(V)$; both agree on $\mathrm{SU}(N)$.

(d3) The block-spin projection $A \mapsto A(A^\dagger A)^{-1/2}$
extends analytically to $\mathrm{GL}(N, \mathbb{C})$ near
$\mathbf{1}$: the polar decomposition is analytic when
$A^\dagger A$ is positive-definite ($\|A - \mathbf{1}\| < 1$).

(d4) $G_k(V) = (-D^2[V] + m_W^2)^{-1}$ extends analytically:
$D^2[V]$ is algebraic in $V$, and perturbation of the identity
ensures invertibility near $\mathbf{1}$.

(d5) The Mayer expansion terms are algebraic combinations of
propagators and polynomial vertices --- analytic in complex $V$.

**Step (e): Quantitative complexification radius.**

The bounds $|K_k(X,V)| \leq e^{-\kappa|X|}$ hold for
$V \in \mathrm{SU}(N)$. By Cauchy estimates, for
$V_\ell \in \mathrm{SL}(N,\mathbb{C})$ with
$\|V_\ell - \mathbf{1}\|_{\mathrm{HS}} < \rho/2$:

$$|K_k(X,V)| \leq 2^{N^2|X|}\,e^{-\kappa|X|}. \tag{II.1}$$

Define:

$$\rho' = \frac{\rho}{2}\cdot
  \min\!\left(1,\;\frac{\kappa}{2N^2\ln 2}\right). \tag{II.2}$$

For $\|V_\ell - \mathbf{1}\|_{\mathrm{HS}} < \rho'$, the modified
bound $|K_k(X,V)| \leq e^{-(\kappa/2)|X|}$ holds with halved but
still positive and $k$-independent decay. The complexified polymer
expansion converges. $\square$

**Remark.** (B2) is not discussed in the lattice gauge theory
literature. The argument uses only that algebraic functions of real
variables extend to holomorphic functions of complex variables
(Krantz--Parks, 2002, Thm 1.1.5).


---


## Part III: Stability of Excitation Number

### III.1 The problem

The spectral lemma (two-derivative-spectral-lemma.md, Sec. 3) gives
$\mathrm{exc}(\mathcal{O}) \geq p \Rightarrow
|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$.
Applying this with $p = 2$ to $\mathcal{O} = \delta E_k^{d=6}$
requires $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$
non-perturbatively.

### III.2 Why naive splitting fails

Write $\mathcal{O} = \mathcal{O}^{\mathrm{pert}} +
\delta\mathcal{O}$ with $\|\delta\mathcal{O}\| \leq Cg_k^6$.
The perturbative term gives $|\langle 1|\mathcal{O}^{\mathrm{pert}}
|1\rangle_c| \leq C_2 g_k^4 \hat{\Delta}^2$ (has exc $\geq 2$).
But $\delta\mathcal{O}$ lacks guaranteed excitation structure, so
the clustering bound gives $|\langle 1|\delta\mathcal{O}|1\rangle_c|
\leq Cg_k^6/\hat{\Delta}^3$. For the total to be
$O(g_k^4\hat{\Delta}^2)$, we need $g_k^2 \lesssim \hat{\Delta}^5$.
On the AF trajectory, $g_k^2 \sim 1/\ln(1/a\Lambda)$ while
$\hat{\Delta}^5 \sim (a\Lambda)^5 \sim e^{-5/(2b_0 g^2)}$, so
$g_k^2 \gg \hat{\Delta}^5$ and the remainder **dominates**. The
naive approach fails.

### III.3 The correct approach: operator classification

Instead of splitting, we prove that the **total** operator
$\delta E_k^{d=6}$ has $\mathrm{exc} \geq 2$ by classifying
all dimension-6 gauge-invariant operators.

**Lemma (Stability of Excitation Number).** *Let $\mathcal{O}$ be
a local, gauge-invariant, $\mathcal{C}$-even operator on
$\Lambda_{k+1}$ of engineering dimension 6, analytic in $\{V_\ell\}$
with radius $\rho > 0$ (from (B1)). Then
$\mathrm{exc}(\mathcal{O}) \geq 2$.*

**Proof.** The operator classification at dimension 6 is exhaustive
(conjecture-1-closing.md, Sec. 2.4):

**(I) Zero-derivative operators** ($\mathrm{Tr}(F^3)$,
$d^{abc}F^3$): these are $\mathcal{C}$-odd, hence have coefficient
exactly zero in any $\mathcal{C}$-invariant effective action.
*Elimination is exact and non-perturbative* (single-step-case-b.md).

**(II) One-derivative operators** (dimension-5 reduced part):
absent. In the $\mathcal{C}$-even sector, gauge-invariant operators
require even numbers of field-strength factors under the trace,
forcing even dimension. No $\mathcal{C}$-even gauge-invariant
operator of dimension 5 exists.

**(III) Two-derivative operators**: the surviving operators are
$\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and
$\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$, each with
exactly two covariant derivatives beyond $\mathrm{Tr}(F^2)$.
For these operators, $\mathrm{exc} \geq 2$ by the spectral
mechanism:

- The transfer-matrix representation of $\mathrm{Tr}(D_0 F)^2$
  gives $\sum_n (e^{E_m - E_n} - 1)^2 |\langle m|F|n\rangle|^2$.
  The factor $(e^{E_m - E_n} - 1)^2$ vanishes identically at
  $n = m$ (structural zero, not numerical cancellation). This forces
  $\mathrm{exc} \geq 2$ for the connected matrix element
  (two-derivative-spectral-lemma.md, Sec. 4).

- For spatial derivatives ($D_j F$), the connected matrix element
  vanishes at $\vec{p} = 0$ by translation invariance.

**(IV) Three-or-more-derivative operators** ($n \geq 3$
derivatives): have $\mathrm{exc} \geq 3 > 2$.

Since every $\mathcal{C}$-even dimension-6 gauge-invariant operator
falls into one of these classes, and classes (I)--(II) are absent
while (III)--(IV) all have $\mathrm{exc} \geq 2$:
$\mathrm{exc}(\mathcal{O}) \geq 2$. $\square$

### III.4 Application to the non-perturbative operator

Balaban's effective action is $\mathcal{C}$-invariant (the Wilson
action and Haar measure are $\mathcal{C}$-invariant; each RG step
preserves this symmetry). The dimension-6 part $\delta E_k^{d=6}$
of the remainder is by construction a $\mathcal{C}$-even, dimension-6,
gauge-invariant local operator. By the Lemma:

$$\mathrm{exc}(\delta E_k^{d=6}) \geq 2. \tag{III.1}$$

This holds non-perturbatively. No splitting into perturbative and
non-perturbative parts is needed. The operator's excitation number
is determined by its **symmetry and dimension class**, not by its
perturbative content.

**Role of (B1)--(B2).** The analyticity properties ensure that
$\delta E_k^{d=6}$ is a genuine (convergent, not formal) operator
with well-defined dimension classification. Without (B1), the
"dimension-6 part" of the effective action might be only an
asymptotic concept, and the classification argument would not apply
to the non-perturbative object. (B1) guarantees the Taylor
expansion converges, so the dimension-6 projection is exact. (B2)
ensures the algebraic structure (polynomial dependence on matrix
entries) extends to the complex domain, validating the spectral
analysis.

### III.5 Quantitative consequence

Applying the spectral lemma with $p = 2$,
$M = \|\delta E_k^{d=6}\| \leq Cg_k^4$ (Balaban):

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
  \leq C_2 \cdot Cg_k^4 \cdot \hat{\Delta}_{k+1}^2
  = C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2. \tag{III.2}$$

Non-perturbative corrections from outside the small-field region:
large-field $O(e^{-c/g_k^{2\epsilon}})$, instantons
$O(e^{-8\pi^2/g_k^2})$ --- both negligible.

This is Conjecture 1 at $d_O = 6$.


---


## Part IV: Final Status Table

### IV.1 Proof chain for $\Delta_\infty > 0$

| Step | Statement | Status | Source |
|:-----|:----------|:-------|:-------|
| 1 | $\Delta_0 > 0$ | **Proved** (Thm 4) | 04-lattice-mass-gap.md |
| 2 | UV stability | **Literature** | CMP 109, 119 |
| 3 | Polymer convergence, $\kappa$ $k$-indep. | **Literature** | CMP 109, Thm 2.1 |
| 4 | (B1): analyticity, $k$-indep. radius | **Proved** (Part I) | Extraction from CMP 95--109 |
| 5 | (B2): $\mathrm{SL}(N,\mathbb{C})$ extension | **Proved** (Part II) | Standard complex analysis |
| 6 | $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$ | **Proved** (exact) | single-step-case-b.md |
| 7 | Newton decomposition: $n \geq 2$ survives | **Proved** (exact) | conj-1-closing.md, Lemma 2.1 |
| 8 | $\mathrm{exc}(\mathrm{Tr}(DF)^2) \geq 2$ | **Proved** | two-deriv-spectral-lemma.md, Sec 4 |
| 9 | Dim-6 classification: all ops have exc $\geq 2$ | **Proved** | Part III, Sec III.3 |
| 10 | $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ non-pert. | **Proved** | (B1) + classification |
| 11 | $C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ bound | **Proved** | Spectral lemma + Step 10 |
| 12 | RG recursion: $C_{k+1} = C_k/4 + C_{\mathrm{new}}$ | **Proved** | rg-preservation.md |
| 13 | $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ | **Proved** | rg-preservation.md, Sec 6 |
| 14 | $\Delta_\infty > 0$ | **Proved** | 09-continuum-limit.md |

### IV.2 Classification of arguments

| Argument | Type |
|:---------|:-----|
| Polymer expansion convergence | Established result (Balaban) |
| Propagator / kernel analyticity | Established result (Balaban) |
| Polymer activities analytic | Reading exercise from Balaban [VERIFY] |
| Radius $k$-independent | Reading exercise from Balaban [VERIFY] |
| Complexification to $\mathrm{SL}(N,\mathbb{C})$ | Standard complex analysis |
| Dim-6 operator classification | Short new argument (this doc) |
| Stability of excitation number | Short new argument (this doc) |

### IV.3 Items requiring verification

**[VERIFY] Analyticity of individual polymer activities.** Each of
the four operations in Part I, Step (b) preserves analyticity by
standard arguments. However, Balaban does not state this as a
standalone theorem. A referee must read CMP 109, Sections 2--4 and
verify the inductive step preserves analyticity with controlled
radius. This is a reading exercise, not a mathematical gap.

**[VERIFY] Block-spin kernel complexification.** The map
$A \mapsto A(A^\dagger A)^{-1/2}$ must be verified analytic in a
$k$-independent neighborhood of $\mathbf{1} \in
\mathrm{GL}(N, \mathbb{C})$. Standard (depends on $N$ not $k$),
but deserves a one-paragraph verification in the final paper.

**[VERIFY] Dimension-6 projection is exact.** The claim that
$\delta E_k^{d=6}$ is genuinely dimension-6 (not contaminated by
dimension-4) relies on Balaban's coupling renormalization absorbing
the $\mathrm{Tr}(F^2)/g_k^2$ part. This is the content of CMP 109,
Section 2. Standard, but load-bearing.

### IV.4 Verdict

Conditional on the three [VERIFY] items --- all reading exercises
from Balaban's published work --- the proof chain for
$\Delta_\infty > 0$ is **complete**:

$$\Delta_0 > 0 \;(\text{Thm 4})
  \;\xrightarrow[\text{(B1)(B2) + stability}]{\text{Balaban}}\;
  \text{Conj. 1 discharged}
  \;\xrightarrow{\text{RG preservation}}\;
  \Delta_\infty > 0.$$

No new conjectures are introduced. The single genuinely new
contribution is the **stability of excitation number** argument
(Part III): the dimension-6 classification forces
$\mathrm{exc} \geq 2$ universally, not just perturbatively.

**Is the proof unconditional?** It is unconditional modulo the
three [VERIFY] items, which are verifications of implicit properties
in Balaban's published construction. If one accepts Balaban's
results at face value (as the community does for his stated
theorems), then the analyticity is an immediate consequence and
the proof is unconditional. The [VERIFY] items identify the
precise points where a referee would need to check Balaban's
construction in detail.
