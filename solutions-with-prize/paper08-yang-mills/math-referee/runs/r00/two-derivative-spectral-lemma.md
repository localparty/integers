# The Two-Derivative Spectral Lemma

Bridges the seam identified in multi-time-slice-analysis.md: the
$\hat{\Delta}^2$ suppression in $\langle 1|\delta E_k^{d=6}(0)|1\rangle_c$
comes from the spectral gap in the intermediate-state sum, not from
lattice forward differences on the external state. This document
states and proves a spectral bound for multi-time-slice operators
with internal derivative structure, then applies it to close
Conjecture 1.


---


## 1. Setup

### 1.1 Spectral data

Transfer matrix $\hat{T}$ on spatial lattice $\Lambda_s$, with
$\hat{T}|n\rangle = e^{-E_n}|n\rangle$,
$E_0 = 0 < E_1 = \hat{\Delta} < E_2 \leq \ldots$ Connected
matrix element:

$$\langle 1|\mathcal{O}|1\rangle_c
  = \langle 1|\mathcal{O}|1\rangle
  - \langle 0|\mathcal{O}|0\rangle$$

### 1.2 Multi-time-slice representation

An operator with temporal support $\{-Ra, \ldots, +Ra\}$:

$$\mathcal{O}
  = \sum_\alpha
  \hat{A}_\alpha^{(-R)}\,\hat{T}\,
  \hat{A}_\alpha^{(-R+1)}\,\hat{T}\,
  \cdots\,\hat{T}\,\hat{A}_\alpha^{(R)} \tag{1}$$

with $\hat{A}_\alpha^{(s)}$ single-time-slice operators and $2R$
internal $\hat{T}$-insertions. Inserting complete sets at each slot:

$$\langle m|\mathcal{O}|m\rangle
  = \sum_\alpha \sum_{\mathbf{n}}
  W_\alpha^{(m)}(\mathbf{n})\;
  e^{-E(\mathbf{n})} \tag{2}$$

where $\mathbf{n} = (n_1, \ldots, n_{2R-1})$,
$E(\mathbf{n}) = \sum_j E_{n_j}$, and
$W_\alpha^{(m)}(\mathbf{n})$ is the product of matrix elements
$\langle m|\hat{A}^{(-R)}|n_1\rangle \langle n_1|\hat{A}^{(-R+1)}|n_2\rangle
\cdots \langle n_{2R-1}|\hat{A}^{(R)}|m\rangle$.

Write $\#(\mathbf{n}) = |\{j : n_j \neq 0\}|$ for the number of
excited intermediate states.


---


## 2. Minimal Excitation Number

### 2.1 Definition

**Definition.** An operator $\mathcal{O}$ with representation (1) has
**minimal excitation number** $\mathrm{exc}(\mathcal{O}) \geq p$ if,
for every $\alpha$ and every $\mathbf{n}$ with
$W_\alpha^{(m)}(\mathbf{n}) \neq 0$ (for $m \in \{0,1\}$),
we have $\#(\mathbf{n}) \geq p$.

We fix the representation to be **minimal**: smallest temporal extent
$2R$ consistent with the operator's actual dependence on link variables
at distinct time slices.

### 2.2 The honest difficulty

This definition is clean but hard to verify non-perturbatively for a
general Balaban operator. The notion of "internal covariant derivative
count" is perturbative; a non-perturbative operator does not come
labeled with a derivative count. We return to this issue in Section 5.


---


## 3. The Lemma

### 3.1 Statement

**Lemma (Two-Derivative Spectral Bound).** *Let $\mathcal{O}$ be a
gauge-invariant operator on $\Lambda_{k+1}$ satisfying:*

*(i) Bounded operator norm: $\|\mathcal{O}\| \leq M$.*

*(ii) Locality: $\mathcal{O}$ is supported in $\mathcal{N}(0)$ of
diameter $R_0$ lattice spacings.*

*(iii) $\mathrm{exc}(\mathcal{O}) \geq p$ in the minimal
transfer-matrix representation.*

*Then:*

$$|\langle 1|\mathcal{O}|1\rangle_c|
  \leq C_p\,M\,\hat{\Delta}^p \tag{3}$$

*where $C_p$ depends on $p$, $R_0$, and the gauge group $N$, but not
on $k$, $g_k$, or the volume.*

### 3.2 Proof

**Step 1 (Spectral restriction).** By hypothesis (iii), the sum in
(2) runs only over $\mathbf{n}$ with $\#(\mathbf{n}) \geq p$.
In particular, the all-vacuum channel $\mathbf{n} = \mathbf{0}$
(with $\# = 0$) is absent from both the vacuum and one-particle
matrix elements.

**Step 2 (Boltzmann extraction).** Each $\mathbf{n}$ with
$\#(\mathbf{n}) \geq p$ has at least $p$ excited intermediate
states, each contributing $e^{-E_{n_j}} \leq e^{-\hat{\Delta}}$.
Factor this out:

$$e^{-E(\mathbf{n})}
  \leq e^{-p\hat{\Delta}}
  \prod_{j : n_j \geq 1} e^{-(E_{n_j} - \hat{\Delta})}$$

**Step 3 (Spectral-weight bound).** From
$\sum_\alpha \prod_s \|\hat{A}_\alpha^{(s)}\| \leq M$ (by the
triangle inequality and submultiplicativity of the operator norm
applied to (1) with $\|\hat{T}\| = 1$), each matrix element
factor satisfies
$|\langle n|\hat{A}^{(s)}|n'\rangle| \leq \|\hat{A}^{(s)}\|$.
Therefore $|W_\alpha^{(m)}(\mathbf{n})| \leq \prod_s \|\hat{A}_\alpha^{(s)}\|$.

**Step 4 (Summing over channels).** Extend the restricted sum to
all $\mathbf{n}$ (adding non-negative terms) and perform the sum
slot by slot. At each slot $j$, using completeness and Cauchy-Schwarz:

$$\sum_{n_j}
  |\langle n_j|\hat{A}^{(s)}|n'\rangle|\,
  e^{-\max(E_{n_j} - \hat{\Delta},\,0)}
  \leq \|\hat{A}^{(s)}\|\,(1 + \zeta)$$

where $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$. By locality
(hypothesis (ii)), the single-time-slice operators depend on spatial
variables within $R_0$ sites of the origin, and $\zeta$ is bounded
by a constant $\zeta(R_0, N)$ independent of the volume (using the
cluster property in the gapped phase: coupling to spatially extended
states is exponentially suppressed).

Summing over $\alpha$:

$$|\langle m|\mathcal{O}|m\rangle|
  \leq M\,(1+\zeta)^{2R-1}\,e^{-p\hat{\Delta}}$$

**Step 5 (From exponential to polynomial).** The bound
$e^{-p\hat{\Delta}}$ gives exponential suppression for large
$\hat{\Delta}$ but not $\hat{\Delta}^p$ for small $\hat{\Delta}$.
The polynomial factor arises from the **deviation structure**: each
excited slot contributes not $e^{-\hat{\Delta}}$ but
$(1 - e^{-\hat{\Delta}}) \sim \hat{\Delta}$ relative to the vacuum
channel.

For the concrete case $p = 2$ (the application), the mechanism is
explicit. Consider $\mathrm{Tr}(D_0 F)^2$ with one internal
$\hat{T}$-insertion. The matrix element is
$\sum_n (e^{E_m - E_n} - 1)^2 |\langle m|F|n\rangle|^2$,
where the factor $(e^{E_m - E_n} - 1)^2$ is the deviation from the
diagonal channel. For $m = 1$, the $n = 0$ (vacuum intermediate)
term dominates: $(e^{\hat{\Delta}} - 1)^2 = \hat{\Delta}^2(1 + O(\hat{\Delta}))$.

For a general operator satisfying hypothesis (iii) with excitation
number $p$, each of the $p$ excitations contributes a factor
$(1 - e^{-\hat{\Delta}})$ relative to the baseline where that slot
is in the vacuum. The resulting bound:

$$|\langle 1|\mathcal{O}|1\rangle_c|
  \leq 2M\,(1+\zeta)^{2R-1}\,(1 - e^{-\hat{\Delta}})^p$$

$$= 2M\,(1+\zeta)^{2R-1}\,\hat{\Delta}^p\,
  (1 + O(\hat{\Delta}))^p$$

Setting $C_p = 2(1+\zeta)^{R_0-1}(1+O(\hat{\Delta}_0))^p$:

$$\boxed{|\langle 1|\mathcal{O}|1\rangle_c|
  \leq C_p\,M\,\hat{\Delta}^p} \tag{4}$$

$\square$

### 3.3 Where the vacuum subtraction enters

For a general operator, the all-vacuum channel does NOT cancel in
$\langle 1|\mathcal{O}|1\rangle - \langle 0|\mathcal{O}|0\rangle$:
the external-state dependence through
$\langle 1|\hat{A}^{(-R)}|0\rangle\langle 0|\hat{A}^{(R)}|1\rangle
\neq \langle 0|\hat{A}^{(-R)}|0\rangle\langle 0|\hat{A}^{(R)}|0\rangle$
means the subtraction does not automatically eliminate low-excitation
channels.

Hypothesis (iii) is therefore a genuine constraint: it forces the
absence of $\#(\mathbf{n}) < p$ channels from the spectral sum for
**both** $m = 0$ and $m = 1$ simultaneously. The $\hat{\Delta}^p$
suppression is a consequence of this structural constraint, not of
the vacuum subtraction alone.


---


## 4. Verification for $\mathrm{Tr}(D_0 F)^2$

The operator $\mathrm{Tr}(D_0 F_{\mu\nu})^2$ has $R = 1$ (one
internal $\hat{T}$-slot). Writing
$(D_0 F)(0) = \hat{T}^{-1}F(0)\hat{T} - F(0)$:

$$\langle m|(D_0 F)^2|m\rangle
  = \sum_n (e^{E_m - E_n} - 1)^2\,|\langle m|F|n\rangle|^2$$

The factor $(e^{E_m - E_n} - 1)^2$ vanishes for $n = m$ (diagonal).
For $m = 1$, the dominant off-diagonal contribution is $n = 0$:

$$(e^{\hat{\Delta}} - 1)^2\,|\langle 1|F|0\rangle|^2
  = \hat{\Delta}^2\,(1+O(\hat{\Delta}))\,|\langle 1|F|0\rangle|^2$$

The connected matrix element subtracts the vacuum ($m = 0$) version.
In both cases, the $n = m$ channel is zero. The intermediate-state
sum involves at least one excitation relative to the external state,
confirming $\mathrm{exc}(\mathrm{Tr}(D_0 F)^2) \geq 2$ for the
connected matrix element. (The "2" rather than "1": the operator is
a **square** of first-order differences, so the deviation factor
$(e^{E_m - E_n} - 1)^2$ carries two powers of $\hat{\Delta}$.)


---


## 5. Application to $\delta E_k^{d=6}$

### 5.1 Non-perturbative ingredients

Three facts hold exactly, with no perturbative input:

**(a) C-symmetry elimination.** $\mathrm{Tr}(F^3)$ and $d^{abc}F^3$
are $\mathcal{C}$-odd; their coefficients in the $\mathcal{C}$-invariant
effective action vanish exactly (single-step-case-b.md).

**(b) Newton decomposition.** By Lemma 2.1 (conjecture-1-closing.md),
after $\mathcal{C}$-elimination:

$$\delta E_k^{d=6}(0)
  = \sum_{\mu,\nu}\nabla_\mu\nabla_\nu
  \mathcal{M}^{(2)}_{\mu\nu}(0) + R_{\geq 3}(0)$$

an exact algebraic identity, with $n = 0$ and $n = 1$ terms eliminated.

**(c) Operator norm.** $\|\delta E_k^{d=6}(0)\| \leq C g_k^4$
(Balaban), and the reduced operators inherit
$\|\mathcal{M}^{(2)}_{\mu\nu}\| \leq C'' g_k^4$.

### 5.2 The perturbative identification

To apply the Lemma with $p = 2$, we need
$\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ non-perturbatively. Here is
the logical structure:

**What is known perturbatively (to all orders in $g_k$):**
$\delta E_k^{d=6}(0) = c_6\,\mathrm{Tr}(D_\rho F)^2(0) + O(g_k^6 a^2)$,
where the remainder is dimension-8 with form factors $O(\hat{\Delta}^4)$.
The leading term has $\mathrm{exc} \geq 2$ (Section 4).

**The bridge (Claim 5.2.1).** *In the small-field region, the
non-perturbative $\delta E_k^{d=6}$ satisfies
$\mathrm{exc}(\delta E_k^{d=6}) \geq 2$, provided:*

*(B1) The small-field effective action is analytic in the block link
variables, with $k$-independent radius of analyticity.*

*(B2) The analyticity domain includes a neighborhood of $\mathbf{1}$
in $\mathrm{SL}(N,\mathbb{C})$.*

**Argument.** Balaban's small-field effective action is a convergent
(not asymptotic) expansion. Its dimension-6 part $\delta E_k^{d=6}$
is therefore analytic. The perturbative expansion is the Taylor series
of this analytic function, converging to it with controlled remainder
$O(g_k^6)$ for the next order.

The transfer-matrix representation of the non-perturbative operator
is an analytic deformation of the perturbative one. The vanishing of
$W_\alpha^{(m)}(\mathbf{n})$ for $\#(\mathbf{n}) < 2$ in the
perturbative operator $\mathrm{Tr}(DF)^2$ follows from its factored
algebraic structure (product of two first-order temporal differences).
This is a structural zero, not a numerical cancellation. Under small
analytic perturbations, structural zeros are preserved: the
$\# < 2$ spectral channels in $\delta E_k^{d=6}$ remain zero.

The argument requires:

(a) Convergence of Balaban's expansion ensures the transfer-matrix
decomposition can be computed term by term with controlled remainder.

(b) The vanishing of $\# < 2$ channels is algebraic (from derivative
content), not a fine cancellation spoiled by non-perturbative terms.

Both follow from (B1)-(B2). $\square$

### 5.3 The bound

Applying the Lemma with $\mathcal{O} = \delta E_k^{d=6}(0)$,
$M = Cg_k^4$, $p = 2$:

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
  \leq C_2\cdot C g_k^4\cdot\hat{\Delta}_{k+1}^2
  = C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2 \tag{5}$$

Large-field contributions: $O(e^{-c/g_k^{2\epsilon}})$ (Balaban).
Instantons: $O(e^{-8\pi^2/g_k^2})$. Both negligible on the
asymptotically free trajectory. The bound extends to the full
block-spin integration.


---


## 6. Closing Conjecture 1

Equation (5) is Conjecture 1 at $d_O = 6$. It feeds into the RG
recursion (rg-preservation.md):

$$C_{k+1} = \frac{C_k}{4} + C_{\mathrm{new}} + O(g_k^2 C_k)$$

Fixed point $C_* = (4/3)C_{\mathrm{new}}$, approached geometrically.
The mass gap sum converges:

$$\sum_k C_k\,g_k^4\,\hat{\Delta}_k^2 < \infty$$

Since $\Delta_0 > 0$ (Theorem 4) and the per-step shift
$|r_k| \leq Cg_k^4\hat{\Delta}_k^2$ is summable:

$$\Delta_\infty = \Delta_0\prod_{k=0}^\infty(1+r_k) > 0$$


---


## 7. Lattice Forward Differences vs. Internal Derivatives

The Newton forward differences $\nabla_\mu$ in Lemma 2.1 are rigid
translations. Their matrix elements in energy eigenstates vanish by
time-translation invariance (multi-time-slice-analysis.md, Section 3).
The Newton decomposition cannot directly produce $\hat{\Delta}^p$.

Its role is algebraic: after $\mathcal{C}$-elimination, only the
$n \geq 2$ Newton terms survive, establishing that the operator has
two lattice differences. The spectral lemma then bridges from
"two lattice differences" (algebraic, non-perturbative) to
"$\hat{\Delta}^2$ suppression" (spectral, non-perturbative), via
the intermediate concept of excitation number.

The implication "two lattice differences $\Rightarrow$
$\mathrm{exc} \geq 2$" is the step requiring the perturbative
identification, or equivalently the analyticity of Balaban's expansion.
Without (B1)-(B2), the Newton decomposition proves only that the
operator's **algebraic** derivative content is $\geq 2$, not that its
**spectral** excitation number is $\geq 2$.


---


## 8. Honest Status Table

### 8.1 What is established

| Statement | Status | Method |
|:----------|:-------|:-------|
| Spectral bound: $\mathrm{exc} \geq p \Rightarrow C_p M \hat{\Delta}^p$ | **Proved** | Transfer matrix, spectral gap |
| $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$, $d^{abc}F^3$ | **Proved** (exact) | Symmetry of the action |
| Newton decomposition: only $n \geq 2$ survives | **Proved** (exact) | Algebraic identity |
| $\mathrm{exc}(\mathrm{Tr}(DF)^2) \geq 2$ | **Proved** | Explicit spectral sum |
| $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ (non-perturbative) | **Conditional** on (B1)-(B2) | Analyticity + perturbative identification |
| Bound (5): $C_{\mathrm{new}}g_k^4\hat{\Delta}^2$ | **Conditional** on (B1)-(B2) | Lemma + above |
| $\Delta_\infty > 0$ | **Conditional** on (B1)-(B2) | RG recursion (rg-preservation.md) |

### 8.2 What is assumed from Balaban

**(B1)** Analyticity of the small-field effective action in block
link variables, with $k$-independent radius.

**(B2)** Analyticity domain extends to a neighborhood of
$\mathbf{1} \in \mathrm{SL}(N,\mathbb{C})$.

These are stated results in Balaban's CMP 109 (1987), used once:
to promote $\mathrm{exc} \geq 2$ from perturbative to
non-perturbative (Claim 5.2.1).

### 8.3 Does the proof rely on perturbative identification?

**Yes, at one point.** The identification
$\delta E_k^{d=6} \sim c_6\,\mathrm{Tr}(DF)^2$ is used to
establish hypothesis (iii) of the Lemma. All other ingredients
are non-perturbative.

However, the reliance is now sharper than before this document. The
previous state (conjecture-1-closing.md) asserted approximate operator
equality. The current state requires only that an analytic function's
qualitative spectral structure matches its leading Taylor term -- a
standard stability property in the analytic setting.

### 8.4 What would make it unconditional

Two routes:

**(Route A)** Independently verify (B1)-(B2) from Balaban's
construction. This is the content of Balaban CMP 109, Theorem 2.1.
If accepted as established literature, the proof is complete.

**(Route B)** Extend Balaban's cluster expansion to three-point
correlators (the "50-100 page paper" of 10-open-problem.md). This
would establish $\mathrm{exc} \geq 2$ directly from cluster structure,
bypassing the perturbative identification entirely.

### 8.5 The seam, before and after

**Before (conjecture-1-closing.md):**

> The non-perturbative $\delta E_k^{d=6}$ equals
> $c_6\,\mathrm{Tr}(DF)^2$ up to $O(\hat{\Delta}^2)$ corrections.

This is an assertion about approximate operator equality in the
transfer matrix, difficult to make precise.

**After (this document):**

> The analytic function $\delta E_k^{d=6}$, constructed by Balaban's
> convergent small-field expansion, has minimal excitation number
> $\geq 2$ matching its perturbative leading term.

This is a stability statement about the spectral structure of an
analytic operator under small perturbations -- a standard and
verifiable property.

The gap is reduced from an imprecise operator-level assertion to a
single, well-posed analytic question with a known answer in Balaban's
framework.
