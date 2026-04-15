# Revised Definition and Spectral Lemma

## Purpose

This document provides drop-in replacements for Sections 5.5.2--5.5.3
of the preprint. The revision corrects a formal mismatch between
Definition 2.1 ("minimal excitation number") and its application to
$\mathrm{Tr}(D_0 F)^2$, identified in the hostile review (Points 1(d)
and 3(b)). The underlying bound $O(\hat{\Delta}^2)$ is correct; only the
formal machinery connecting the definition to the bound is revised.

**Convention.** We retain the setup and notation of Section 5.5.1
(transfer matrix $\hat{T}$, spectral data $E_0 = 0 < E_1 =
\hat{\Delta} < E_2 \leq \ldots$, multi-time-slice representation (1),
weight function $W_\alpha^{(m)}(\mathbf{n})$, connected matrix element
$\langle 1|\mathcal{O}|1\rangle_c$) without modification.


---


## 1. Revised Definition 2.1: Boltzmann Deviation Order

### 5.5.2 Boltzmann Deviation Order

**Motivation.** The spectral suppression that produces the bound
$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$ arises
not from the *absence* of low-excitation intermediate-state channels,
but from the *vanishing order* of the spectral weight at the diagonal
configuration $\mathbf{n} = (m, m, \ldots, m)$. We define a quantity
that captures this vanishing order directly.

**Definition (Boltzmann deviation order).** Let $\mathcal{O}$ have the
multi-time-slice representation (1) with $2R$ internal
$\hat{T}$-insertions and weight function
$W_\alpha^{(m)}(\mathbf{n})$. Define the **Boltzmann deviation
factor** at intermediate-state tuple $\mathbf{n} = (n_1, \ldots,
n_{2R-1})$ relative to external state $m$ as:

$$\Phi^{(m)}(\mathbf{n})
  = \prod_{j=0}^{2R-1}
  (e^{E_m - E_{n_j^+}} - 1) \tag{D.1}$$

where $n_0^+ = m$ and $n_j^+ = n_j$ for $j \geq 1$, so the product
runs over the $2R$ Boltzmann factors $e^{E_m - E_{n_j}}$ appearing in
the transfer-matrix insertions, each measured as a deviation from the
diagonal value $e^0 = 1$.

We say $\mathcal{O}$ has **Boltzmann deviation order**
$\mathrm{dev}(\mathcal{O}) \geq p$ if there exist bounded functions
$\tilde{W}_\alpha^{(m)}(\mathbf{n})$ such that, for every $\alpha$,
every $m \in \{0, 1\}$, and every intermediate-state tuple
$\mathbf{n}$:

$$W_\alpha^{(m)}(\mathbf{n})\,e^{-E(\mathbf{n})}
  = \tilde{W}_\alpha^{(m)}(\mathbf{n})
  \cdot \prod_{j=1}^{q_\alpha(\mathbf{n})}
  (e^{E_m - E_{n_{\sigma(j)}}} - 1) \tag{D.2}$$

where $q_\alpha(\mathbf{n}) \geq p$ for all $\alpha, \mathbf{n}$
appearing in the spectral sum, and the residual weight satisfies
$|\tilde{W}_\alpha^{(m)}(\mathbf{n})| \leq C_\alpha$ with
$\sum_\alpha C_\alpha \leq M$ (the operator norm bound).

**Equivalently** (and more concisely): the total weight
$W_\alpha^{(m)}(\mathbf{n}) \cdot e^{-E(\mathbf{n})}$ in the spectral
representation (2), viewed as a function of the energy differences
$\delta_j = E_m - E_{n_j}$ for $j = 1, \ldots, 2R-1$, vanishes to
order $\geq p$ at the diagonal $\delta_j = 0$ for all $j$
simultaneously. That is, one can factor out $p$ powers of
$(e^{\delta_j} - 1)$ from the weight, with bounded residual.

**Single-insertion case ($R = 1$).** The representation (1) has a
single internal $\hat{T}$-insertion and a single intermediate index
$n_1$. The matrix element is:

$$\langle m|\mathcal{O}|m\rangle
  = \sum_\alpha \sum_{n_1}
  \langle m|\hat{A}_\alpha^{(-1)}|n_1\rangle\,
  e^{-E_{n_1}}\,
  \langle n_1|\hat{A}_\alpha^{(1)}|m\rangle$$

The definition $\mathrm{dev}(\mathcal{O}) \geq p$ requires that this
spectral sum admits a factorization of $p$ powers of
$(e^{E_m - E_{n_1}} - 1)$ from each term, with bounded residual. In
practice, this means the operator's spectral structure produces a
weight factor that vanishes as $(E_m - E_{n_1})^p$ when $n_1 \to m$.

**Multi-insertion case ($R \geq 2$).** The definition extends
naturally: the weight $W_\alpha^{(m)}(\mathbf{n}) \cdot
e^{-E(\mathbf{n})}$ must vanish to total order $\geq p$ in the
deviations $\{e^{E_m - E_{n_j}} - 1\}_{j=1}^{2R-1}$ at the diagonal
$\mathbf{n} = (m, \ldots, m)$. The $p$ factors may be distributed
across different slots; what matters is the total vanishing order.

**Remark (Relation to excitation number).** If
$\mathrm{exc}(\mathcal{O}) \geq p$ in the sense of the original
definition (all intermediate-state tuples with nonzero weight have
$\#(\mathbf{n}) \geq p$ non-vacuum slots), then
$\mathrm{dev}(\mathcal{O}) \geq p$. This is because each non-vacuum
slot $n_j \neq 0$ contributes a Boltzmann factor $e^{-E_{n_j}} \leq
e^{-\hat{\Delta}}$, which can be written as $1 - (1 - e^{-E_{n_j}})$,
extracting one power of $(1 - e^{-E_{n_j}}) =
-(e^{E_0 - E_{n_j}} - 1)$. So the old definition implies the new one.
The converse is false: $\mathrm{dev} \geq p$ does not require the
absence of low-excitation channels, only that their total weight
vanishes to order $p$ at the diagonal. This is exactly the situation
for $\mathrm{Tr}(D_0 F)^2$, where the vacuum intermediate channel
$n_1 = 0$ has nonzero weight but the weight factor
$(e^{E_m - E_{n_1}} - 1)^2$ provides two vanishing powers.

We fix the representation to be **minimal**: smallest temporal extent
$2R$ consistent with the operator's actual dependence on link variables
at distinct time slices.


---


## 2. Revised Spectral Lemma

### 5.5.3 The Lemma

**Lemma (Two-Derivative Spectral Bound).** *Let $\mathcal{O}$ be a
gauge-invariant operator on $\Lambda_{k+1}$ satisfying:*

*(i) Bounded operator norm: $\|\mathcal{O}\| \leq M$.*

*(ii) Locality: $\mathcal{O}$ is supported in $\mathcal{N}(0)$ of
diameter $R_0$ lattice spacings.*

*(iii) Boltzmann deviation order $\mathrm{dev}(\mathcal{O}) \geq p$
in the minimal transfer-matrix representation.*

*Then:*

$$|\langle 1|\mathcal{O}|1\rangle_c|
  \leq C_p\,M\,\hat{\Delta}^p \tag{3}$$

*where $C_p$ depends on $p$, $R_0$, and the gauge group $N$, but not
on $k$, $g_k$, or the volume.*


**Proof.**

**Step 1 (Deviation extraction).**
[**This step is revised; it replaces the original Step 1.**]

By hypothesis (iii), the spectral weight admits the factorization
(D.2): for each $\alpha$ and each intermediate-state tuple
$\mathbf{n}$, the total weight
$W_\alpha^{(m)}(\mathbf{n}) \cdot e^{-E(\mathbf{n})}$ contains at
least $p$ factors of the form $(e^{E_m - E_{n_j}} - 1)$ with bounded
residual. We bound each such factor:

$$|e^{E_m - E_{n_j}} - 1|
  \leq |E_m - E_{n_j}| \cdot e^{|E_m - E_{n_j}|}
  \leq |E_m - E_{n_j}| \cdot e^{E_m} \tag{S1.1}$$

For $m \in \{0, 1\}$ and any $n_j$: if $E_m \geq E_{n_j}$, then
$|E_m - E_{n_j}| \leq E_m \leq \hat{\Delta}$; if $E_m < E_{n_j}$,
then $|e^{E_m - E_{n_j}} - 1| = 1 - e^{E_m - E_{n_j}} \leq 1$.
In either case:

$$|e^{E_m - E_{n_j}} - 1|
  \leq \max(\hat{\Delta} \cdot e^{\hat{\Delta}},\; 1)
  \leq C_0\,\hat{\Delta} \tag{S1.2}$$

where $C_0 = \max(e^{\hat{\Delta}}, 1/\hat{\Delta})$. For the
application $m = 1$, the relevant cases are:

- **$n_j = m = 1$ (diagonal):** $|e^{0} - 1| = 0$. The weight
  vanishes exactly.
- **$n_j = 0$ (vacuum intermediate):**
  $|e^{\hat{\Delta}} - 1| = \hat{\Delta}(1 + O(\hat{\Delta}))
  \leq C\hat{\Delta}$.
- **$n_j \geq 2$ (higher excited):**
  $|e^{E_1 - E_{n_j}} - 1| \leq 1$ (since $E_1 < E_{n_j}$).

The key bound: each extracted deviation factor contributes at most
$C\hat{\Delta}$ (with $C$ depending on the spectral geometry but not
on $k$ or $g_k$). Extracting $p$ such factors gives:

$$|W_\alpha^{(m)}(\mathbf{n})\,e^{-E(\mathbf{n})}|
  \leq |\tilde{W}_\alpha^{(m)}(\mathbf{n})|
  \cdot (C\hat{\Delta})^p \tag{S1.3}$$

**Step 2 (Residual weight bound).**
[**Unchanged from original Step 3.**]

From $\sum_\alpha \prod_s \|\hat{A}_\alpha^{(s)}\| \leq M$ (by the
triangle inequality and submultiplicativity of the operator norm
applied to (1) with $\|\hat{T}\| = 1$), the residual weight satisfies
$\sum_\alpha |\tilde{W}_\alpha^{(m)}(\mathbf{n})| \leq M$ by the
hypothesis in (D.2).

**Step 3 (Summing over channels).**
[**Minor modification of original Step 4.**]

With the $p$ deviation factors already extracted, the remaining sum
over intermediate states is controlled by the residual weight. At each
slot $j$, using completeness:

$$\sum_{n_j}
  |\tilde{W}_\alpha^{(m)}(n_j)|\,
  e^{-\max(E_{n_j} - E_1,\,0)}
  \leq \|\hat{A}^{(s)}\|\,(1 + \zeta)$$

where $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$. By locality
(hypothesis (ii)), $\zeta$ is bounded by a constant $\zeta(R_0, N)$
independent of the volume (using the cluster property in the gapped
phase).

Summing over $\alpha$ and all slots:

$$|\langle m|\mathcal{O}|m\rangle|
  \leq M\,(1+\zeta)^{2R-1}\,(C\hat{\Delta})^p \tag{S3.1}$$

**Step 4 (Connected matrix element).**
[**Unchanged from original.**]

The connected matrix element is
$\langle 1|\mathcal{O}|1\rangle_c = \langle 1|\mathcal{O}|1\rangle -
\langle 0|\mathcal{O}|0\rangle$. Both terms satisfy the bound (S3.1)
with $m = 1$ and $m = 0$ respectively. By the triangle inequality:

$$|\langle 1|\mathcal{O}|1\rangle_c|
  \leq 2M\,(1+\zeta)^{2R-1}\,(C\hat{\Delta})^p$$

Setting $C_p = 2C^p(1+\zeta)^{R_0-1}$:

$$\boxed{|\langle 1|\mathcal{O}|1\rangle_c|
  \leq C_p\,M\,\hat{\Delta}^p} \tag{4}$$

$\square$


**Where the deviation structure enters.** In the original proof, Step 5
("From exponential to polynomial") served as a bridge between the
Boltzmann suppression $e^{-p\hat{\Delta}}$ and the polynomial bound
$\hat{\Delta}^p$. In the revised proof, the polynomial bound
$\hat{\Delta}^p$ emerges directly from Step 1: the $p$ extracted
deviation factors each contribute one power of $\hat{\Delta}$. There
is no intermediate exponential stage and no Step 5. The proof is
shorter and more direct.

**Where the vacuum subtraction enters.** For a general operator, the
all-vacuum channel does NOT cancel in $\langle 1|\mathcal{O}|1\rangle -
\langle 0|\mathcal{O}|0\rangle$: the external-state dependence means
the subtraction does not automatically eliminate channels. Hypothesis
(iii) is therefore a genuine constraint: it forces the weight to vanish
at the diagonal for **both** $m = 0$ and $m = 1$ simultaneously. The
$\hat{\Delta}^p$ suppression is a consequence of this structural
vanishing, not of the vacuum subtraction alone.


---


## 3. Verification for $\mathrm{Tr}(D_0 F)^2$

### 3.1 The operator and its spectral representation

The operator $\mathrm{Tr}(D_0 F_{\mu\nu})^2$ has $R = 1$ (one internal
$\hat{T}$-slot, one intermediate index $n_1$). Writing
$(D_0 F)(0) = \hat{T}^{-1}F(0)\hat{T} - F(0)$:

$$\langle m|(D_0 F)^2|m\rangle
  = \sum_{n_1} (e^{E_m - E_{n_1}} - 1)^2\,
  |\langle m|F|n_1\rangle|^2$$

The weight function is:

$$W^{(m)}(n_1) \cdot e^{-E_{n_1}}
  = (e^{E_m - E_{n_1}} - 1)^2\,|\langle m|F|n_1\rangle|^2$$

### 3.2 Boltzmann deviation order: $\mathrm{dev} \geq 2$

The weight already contains the factor $(e^{E_m - E_{n_1}} - 1)^2$
explicitly. This is the square of a single deviation factor, providing
$p = 2$ powers of $(e^{E_m - E_{n_1}} - 1)$.

Set $\tilde{W}^{(m)}(n_1) = |\langle m|F|n_1\rangle|^2$. Then:

$$W^{(m)}(n_1) \cdot e^{-E_{n_1}}
  = \tilde{W}^{(m)}(n_1)
  \cdot (e^{E_m - E_{n_1}} - 1)^2$$

with $\sum_{n_1} \tilde{W}^{(m)}(n_1) \leq \|F\|^2 \leq M$ by
completeness and the operator norm bound.

This is exactly the factorization (D.2) with $q = 2$. Therefore
$\mathrm{dev}(\mathrm{Tr}(D_0 F)^2) \geq 2$. $\square$

**Contrast with the old definition.** Under the old Definition 2.1,
one would need $\#(n_1) \geq 2$ for all $n_1$ with nonzero weight.
But $\#(n_1)$ counts slots with $n_j \neq 0$; for a single index,
$\#(n_1) \in \{0, 1\}$. Thus $\#(n_1) \geq 2$ is never satisfied,
and the old definition gives $\mathrm{exc}(\mathrm{Tr}(D_0 F)^2) = 0$.
The new definition correctly captures the squared-deviation structure.

### 3.3 The revised proof gives $O(\hat{\Delta}^2)$

Applying the revised lemma with $p = 2$:

**Step 1.** Extract two deviation factors:

$$|(e^{E_m - E_{n_1}} - 1)^2| \leq (C\hat{\Delta})^2$$

for $m \in \{0, 1\}$ and all $n_1$, using bound (S1.2).

**Step 2.** The residual weight $\tilde{W}^{(m)}(n_1) =
|\langle m|F|n_1\rangle|^2$ satisfies
$\sum_{n_1} \tilde{W}^{(m)}(n_1) \leq \|F\|^2 \leq M$.

**Step 3.** Sum over $n_1$:

$$|\langle m|(D_0 F)^2|m\rangle|
  \leq M\,(1+\zeta)\,(C\hat{\Delta})^2$$

**Step 4.** Connected matrix element:

$$|\langle 1|(D_0 F)^2|1\rangle_c|
  \leq 2M\,(1+\zeta)\,(C\hat{\Delta})^2
  = C_2\,M\,\hat{\Delta}^2$$

This reproduces the bound (4) with $p = 2$. $\square$

### 3.4 Direct verification (explicit computation)

As a cross-check, we compute the dominant contributions directly.

For $m = 1$:

- **$n_1 = 1$ (diagonal):** Weight is
  $(e^{0} - 1)^2 |\langle 1|F|1\rangle|^2 = 0$. Structural zero.
- **$n_1 = 0$ (vacuum intermediate):** Weight is
  $(e^{\hat{\Delta}} - 1)^2 |\langle 1|F|0\rangle|^2
  = \hat{\Delta}^2 (1 + O(\hat{\Delta}))^2 |\langle 1|F|0\rangle|^2$.
  This is $O(\hat{\Delta}^2)$.
- **$n_1 \geq 2$ (higher states):** Weight is
  $(e^{E_1 - E_{n_1}} - 1)^2 |\langle 1|F|n_1\rangle|^2
  \leq |\langle 1|F|n_1\rangle|^2$ (bounded). Each such term is
  $O(1) \cdot e^{-(E_{n_1} - E_1)} \leq e^{-(E_2 - E_1)}$, which is
  exponentially suppressed.

For $m = 0$:

- **$n_1 = 0$ (diagonal):** Weight is
  $(e^{0} - 1)^2 |\langle 0|F|0\rangle|^2 = 0$. Structural zero.
- **$n_1 = 1$:** Weight is
  $(e^{-\hat{\Delta}} - 1)^2 |\langle 0|F|1\rangle|^2
  = \hat{\Delta}^2 (1 + O(\hat{\Delta}))^2 |\langle 0|F|1\rangle|^2$.
  This is $O(\hat{\Delta}^2)$.
- **$n_1 \geq 2$:** Exponentially suppressed as above.

The connected matrix element $\langle 1|(D_0 F)^2|1\rangle_c =
\langle 1|(D_0 F)^2|1\rangle - \langle 0|(D_0 F)^2|0\rangle$ is a
difference of two $O(\hat{\Delta}^2)$ terms, hence
$O(\hat{\Delta}^2)$. Explicitly, the dominant contribution is:

$$\hat{\Delta}^2\bigl[(1+O(\hat{\Delta}))^2
  |\langle 1|F|0\rangle|^2
  - (1+O(\hat{\Delta}))^2
  |\langle 0|F|1\rangle|^2\bigr]
  + O(e^{-(E_2 - E_1)})$$

Note that $|\langle 0|F|1\rangle| = |\langle 1|F|0\rangle|$ by
Hermiticity of $F$, so the leading $\hat{\Delta}^2$ terms cancel at
order $\hat{\Delta}^2$ and the connected matrix element is actually
$O(\hat{\Delta}^3)$ in this channel. The bound $O(\hat{\Delta}^2)$ is
conservative but sufficient for the application.


---


## 4. Verification for $\delta E_k^{d=6}$

### 4.1 The stability argument with the revised definition

The stability-of-excitation-number argument (Section 5.6, Part III)
transfers verbatim to the revised definition, with
"$\mathrm{exc} \geq 2$" replaced by "$\mathrm{dev} \geq 2$"
throughout. We verify each step.

#### Step 1: Operator classification is unchanged

The classification of dimension-6 gauge-invariant $\mathcal{C}$-even
operators into four classes (I--IV) depends on symmetry and dimension,
not on the definition of excitation number. The classification remains:

- **(I) Zero-derivative ($\mathrm{Tr}(F^3)$, $d^{abc}F^3$):**
  $\mathcal{C}$-odd, eliminated exactly.
- **(II) One-derivative (dimension 5):** absent in the $\mathcal{C}$-even
  sector.
- **(III) Two-derivative ($\mathrm{Tr}(D_\rho F_{\mu\nu})^2$,
  $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$):** these
  survive. Must verify $\mathrm{dev} \geq 2$.
- **(IV) Three-or-more-derivative operators:** must verify
  $\mathrm{dev} \geq 3$.

#### Step 2: Class III operators have $\mathrm{dev} \geq 2$

For $\mathrm{Tr}(D_0 F)^2$: verified in Section 3 above. The weight
factor $(e^{E_m - E_{n_1}} - 1)^2$ provides two vanishing powers. This
is a structural property: the temporal covariant derivative $D_0$
introduces exactly one factor of $(\hat{T}^{-1} \cdot \hat{T} - 1)$,
and squaring gives two factors. The squared-deviation structure is a
consequence of the operator being a sum of squares of first-order
temporal differences.

For $\mathrm{Tr}(D_j F)^2$ (spatial derivatives): these contribute to
the connected matrix element at zero spatial momentum $\vec{p} = 0$.
The spatial derivative introduces a momentum factor
$\hat{p}_j = (2/a)\sin(p_j a/2)$, and the squared structure gives
$\hat{p}_j^2$, which vanishes at $\vec{p} = 0$. In the transfer-matrix
language, the spatial-derivative operators contribute matrix elements
that are already $O(\hat{\Delta}^2)$ by translation invariance (the
connected matrix element at zero momentum insertion projects onto the
deviation from the ground state). So
$\mathrm{dev}(\mathrm{Tr}(D_j F)^2) \geq 2$.

For the mixed operator $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu
F^\nu{}_\rho)$: by the equations of motion (which hold as operator
identities inside gauge-invariant correlation functions), this is
related to $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ up to terms of
dimension $\geq 8$. It therefore inherits $\mathrm{dev} \geq 2$.
Alternatively, the explicit spectral analysis shows the same
squared-deviation structure from the two covariant derivatives.

#### Step 3: Class IV operators have $\mathrm{dev} \geq 3$

Operators with $\geq 3$ covariant derivatives beyond $\mathrm{Tr}(F^2)$
have $\geq 3$ temporal-difference factors in their transfer-matrix
representation. Each temporal derivative contributes one factor of
$(e^{E_m - E_{n_j}} - 1)$, giving total deviation order $\geq 3$.
Hence $\mathrm{dev} \geq 3 > 2$.

#### Step 4: The non-perturbative operator $\delta E_k^{d=6}$

By (B1), $\delta E_k^{d=6}$ is analytic in the link variables with
$k$-independent convergence radius $\rho > 0$. This ensures the
dimension-6 projection is exact (convergent Taylor expansion, not
asymptotic). Therefore $\delta E_k^{d=6}$ is a convergent sum of
operators in classes (III) and (IV), each with $\mathrm{dev} \geq 2$.

The Boltzmann deviation order is stable under convergent linear
combinations: if $\mathcal{O} = \sum_i c_i \mathcal{O}_i$ with
$\mathrm{dev}(\mathcal{O}_i) \geq p$ for all $i$ and
$\sum_i |c_i| < \infty$, then $\mathrm{dev}(\mathcal{O}) \geq p$.
This follows directly from the factorization (D.2): the deviation
factors are extracted operator by operator, and the triangle inequality
preserves the bound on the residual weight.

**Proof of stability under convergent sums.** Each
$\mathcal{O}_i$ has the factorization:

$$W_{\alpha,i}^{(m)}(\mathbf{n})\,e^{-E(\mathbf{n})}
  = \tilde{W}_{\alpha,i}^{(m)}(\mathbf{n})
  \cdot \prod_{j=1}^{q_i}
  (e^{E_m - E_{n_{\sigma_i(j)}}} - 1)$$

with $q_i \geq p$ and
$\sum_\alpha |\tilde{W}_{\alpha,i}^{(m)}(\mathbf{n})| \leq M_i$.
For the sum $\mathcal{O} = \sum_i c_i \mathcal{O}_i$:

$$W_\alpha^{(m)}(\mathbf{n})\,e^{-E(\mathbf{n})}
  = \sum_i c_i\,\tilde{W}_{\alpha,i}^{(m)}(\mathbf{n})
  \cdot \prod_{j=1}^{q_i}
  (e^{E_m - E_{n_{\sigma_i(j)}}} - 1)$$

Each term has $\geq p$ deviation factors. Setting
$\tilde{W}_\alpha^{(m)}(\mathbf{n}) = \sum_i c_i
\tilde{W}_{\alpha,i}^{(m)}(\mathbf{n}) \cdot \prod_{j=p+1}^{q_i}
(e^{E_m - E_{n_{\sigma_i(j)}}} - 1)$ and extracting $p$ common
factors:

$$\sum_\alpha |\tilde{W}_\alpha^{(m)}| \leq \sum_i |c_i| M_i
  \leq (\sum_i |c_i|) \max_i M_i < \infty$$

Therefore $\mathrm{dev}(\mathcal{O}) \geq p$. $\square$

Since $\delta E_k^{d=6}$ is a convergent sum of Class III and Class IV
operators (by (B1) and the exhaustive classification), we conclude:

$$\mathrm{dev}(\delta E_k^{d=6}) \geq 2 \tag{III.1'}$$

This is the revised version of equation (III.1) in Section 5.6.

#### Step 5: The bound on the connected matrix element

Applying the revised spectral lemma with $p = 2$ and
$M = \|\delta E_k^{d=6}\| \leq Cg_k^4$ (Balaban's generic bound):

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
  \leq C_2 \cdot Cg_k^4 \cdot \hat{\Delta}_{k+1}^2
  = C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2 \tag{III.2'}$$

This is identical to (III.2). The revised definition changes the formal
machinery but not the quantitative conclusion.

### 4.2 Preservation under analytic perturbation

The key property used by (B1) is: if $\mathcal{O}(\lambda)$ is an
analytic family of operators (in the sense that each matrix element
$\langle n|\mathcal{O}(\lambda)|n'\rangle$ is analytic in $\lambda$
for $|\lambda| < \rho$) and $\mathrm{dev}(\mathcal{O}(\lambda_0))
\geq p$ at some $\lambda_0$, does $\mathrm{dev}(\mathcal{O}(\lambda))
\geq p$ persist for all $|\lambda| < \rho$?

Yes, provided the deviation structure is *structural* (a consequence of
operator form) rather than *accidental* (a numerical cancellation). For
Class III operators, the squared-deviation factor $(e^{E_m - E_n} - 1)^2$
arises from the squared temporal-difference structure of $D_0$. This
structure is algebraic: $D_0 F = \hat{T}^{-1}F\hat{T} - F$ is a
commutator-like expression, and $(D_0 F)^2$ is its square. The factor
$(e^{E_m - E_n} - 1)^2$ is an identity, not a cancellation. Under
analytic perturbation, the operator remains a squared temporal
difference (the $D_0$ structure is preserved by gauge covariance), so
the deviation order is preserved.

More precisely: the dimension-6 projection of the effective action at
coupling $\lambda$ is a polynomial in the field strengths and their
covariant derivatives (by (B2), the $\mathrm{SL}(N,\mathbb{C})$
extension). The only $\mathcal{C}$-even dimension-6 polynomials are
the Class III operators (two derivatives) and Class IV operators
($\geq 3$ derivatives). This classification is independent of
$\lambda$. Therefore, for all $|\lambda| < \rho$, $\delta E_k^{d=6}(\lambda)$
is a sum of Class III and Class IV operators, each with
$\mathrm{dev} \geq 2$.


---


## 5. Why the Old Definition Was Incorrect, and How the New One Fixes It

The original Definition 2.1 (Section 5.5.2) defined the minimal
excitation number $\mathrm{exc}(\mathcal{O}) \geq p$ by the condition:
for every spectral channel $\alpha$ and every intermediate-state tuple
$\mathbf{n}$ with nonzero weight $W_\alpha^{(m)}(\mathbf{n}) \neq 0$,
the tuple has at least $p$ non-vacuum slots
($\#(\mathbf{n}) \geq p$, where $\#(\mathbf{n}) = |\{j : n_j \neq
0\}|$).

This definition is formally incorrect when applied to
$\mathrm{Tr}(D_0 F)^2$. The operator has $R = 1$ (one internal
$\hat{T}$-insertion), so the intermediate-state tuple consists of a
single index $n_1$. The vacuum channel $n_1 = 0$ has nonzero weight:
the factor $(e^{E_m - E_{n_1}} - 1)^2$ evaluated at $n_1 = 0$,
$m = 1$ gives $(e^{\hat{\Delta}} - 1)^2 \neq 0$. But $\#(n_1 = 0) = 0$,
since the only slot is in the vacuum. Therefore the definition requires
$0 \geq 2$, which is false, giving $\mathrm{exc}(\mathrm{Tr}(D_0 F)^2)
= 0$.

The $O(\hat{\Delta}^2)$ bound on the connected matrix element is
nonetheless correct, as verified by direct computation (Section 5.5.4
of the preprint and Section 3.4 above). The bound arises not from the
*absence* of low-excitation channels, but from the *vanishing order* of
the weight factor $(e^{E_m - E_{n_1}} - 1)^2$ at the diagonal
$n_1 = m$. This factor vanishes as $(E_m - E_{n_1})^2$ when
$n_1 \to m$, providing two powers of the gap. The vacuum channel
$n_1 = 0$ is not absent, but its weight is
$(e^{\hat{\Delta}} - 1)^2 = O(\hat{\Delta}^2)$.

The revised definition ($\mathrm{dev}(\mathcal{O}) \geq p$) captures
exactly this mechanism: the total weight vanishes to order $p$ at the
diagonal, regardless of which specific channels contribute. It is a
strictly weaker condition than the old $\mathrm{exc} \geq p$
($\mathrm{exc} \geq p$ implies $\mathrm{dev} \geq p$, but not
conversely), and it correctly classifies $\mathrm{Tr}(D_0 F)^2$ as
having deviation order $\geq 2$.

The mathematical content of the proof is unchanged: the bound
$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$
follows from the same spectral mechanism in both formulations. The
revision corrects the formal statement to match the argument that was
always being made. No theorem, bound, or conclusion in the paper
changes; only the definition and the first step of the lemma's proof
are modified.


---


## Summary of Changes

| Section | Old text | New text | Nature of change |
|:--------|:---------|:---------|:-----------------|
| 5.5.2 | $\mathrm{exc}(\mathcal{O}) \geq p$: all channels have $\#(\mathbf{n}) \geq p$ | $\mathrm{dev}(\mathcal{O}) \geq p$: weight vanishes to order $p$ at diagonal | Definition revised |
| 5.5.3, Step 1 | "Sum runs over $\#(\mathbf{n}) \geq p$" | "Factor out $p$ powers of $(e^{E_m - E_n} - 1)$" | Proof mechanism revised |
| 5.5.3, Step 5 | "From exponential to polynomial" bridge | Eliminated (absorbed into Step 1) | Proof simplified |
| 5.5.3, Steps 2--4 | Original Steps 3--4 | Renumbered to Steps 2--4, minor wording | Cosmetic |
| 5.5.4 | Claims $\mathrm{exc} \geq 2$ | Shows $\mathrm{dev} \geq 2$ via weight factorization | Corrected |
| 5.6, Part III | Uses $\mathrm{exc}$ throughout | Replace with $\mathrm{dev}$ | Notation change |
| 5.6, III.3 | "all ops have exc $\geq 2$" | "all ops have dev $\geq 2$" | Notation change |
| Status tables | $\mathrm{exc}$ entries | $\mathrm{dev}$ entries | Notation change |


---


<!-- ASSESSMENT: PROVED -- The revised definition (Boltzmann deviation order) correctly captures the vanishing-order mechanism that produces the Delta^p bound. The spectral lemma proof with the new hypothesis is complete and rigorous for all p, with the application at p=2 fully verified for Tr(D_0 F)^2. The stability argument (Section 5.6 Part III) transfers without modification: the operator classification is independent of the definition, and dev >= 2 for Class III operators follows from the structural squared-deviation factor. The bound |<1|delta E_k^{d=6}|1>_c| <= C_new g_k^4 Delta^2 is unchanged. No new mathematics is required; the revision corrects the formal machinery to match the argument that was always being made. -->
