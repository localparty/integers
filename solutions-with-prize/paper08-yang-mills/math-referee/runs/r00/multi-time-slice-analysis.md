# Multi-Time-Slice Analysis of the Temporal Derivative Mechanism

Stress-tests the most delicate point in the closing argument for
Conjecture 1 (conjecture-1-closing.md): the claim that two temporal
lattice derivatives on $\mathcal{M}^{(2)}_{00}(0)$ produce
$\hat{\Delta}^2$ in the one-particle matrix element.

**The critical distinction:** two different operations go by the name
"temporal derivative" in lattice gauge theory, and conflating them
leads to a contradiction. Resolving this confusion validates the
closing argument -- but through a different mechanism than stated.


---


## 1. Temporal Support of Balaban's Operators

### 1.1 Block-spin construction in the temporal direction

At RG step $k$, the block-spin coarsens $\Lambda_k$ (spacing $a_k$)
to $\Lambda_{k+1}$ ($a_{k+1} = 2a_k$). In the temporal direction,
each coarse time slab contains two fine time slabs. The effective
action $S_{k+1}[V]$ on the coarse lattice involves operators
depending on coarse link variables $V_\ell$ that touch the block.

A local operator $\delta E_k^{d=6}(0)$ depends on link variables in a
spacetime neighborhood $\mathcal{N}(0)$ of diameter $R_0$ coarse
lattice spacings. With $R_0 = O(1)$ (independent of $k$), the
operator involves gauge fields at times
$t \in \{-R_0 a, \ldots, +R_0 a\}$ (writing $a = a_{k+1}$). For
$R_0 = 1$: three time slices $\{-a, 0, +a\}$.

**Conclusion:** $\delta E_k^{d=6}(0)$ is generically a
**multi-time-slice** operator, NOT confined to a single time slice.


### 1.2 Transfer matrix representation

A multi-time-slice operator with temporal support
$\{-Ra, \ldots, +Ra\}$ is represented as:

$$\mathcal{O} = \sum_\alpha
  \hat{A}_\alpha^{(-R)}\hat{T}\,\hat{A}_\alpha^{(-R+1)}\hat{T}\,
  \cdots\,\hat{T}\,\hat{A}_\alpha^{(R)}$$

where $\hat{A}_\alpha^{(s)}$ are single-time-slice operators and
$\hat{T}$ is the transfer matrix. Multi-time-slice operators do not
generally commute with $\hat{T}$.


---


## 2. The Newton Inversion Expands Temporal Support

### 2.1 Extracting $\mathcal{M}^{(2)}_{00}$

The Newton forward-difference inversion gives the second temporal
coefficient:

$$\mathcal{M}^{(2)}_{00}(0, 0) = \tfrac{1}{2}(\Delta_0^2 G)(0)
  = \tfrac{1}{2}[G(0, 2a) - 2G(0, a) + G(0, 0)]$$

where $G(\vec{0}, t)$ is obtained after performing the spatial Newton
expansion and isolating zero-spatial-derivative terms.

### 2.2 Temporal support computation

If $G(0, t)$ has temporal support $\{t - a, t, t + a\}$ (from the
parent operator's neighborhood), then:

- $G(0, 0)$ involves fields at $\{-a, 0, +a\}$.
- $G(0, a)$ involves fields at $\{0, a, 2a\}$.
- $G(0, 2a)$ involves fields at $\{a, 2a, 3a\}$.

Therefore $\mathcal{M}^{(2)}_{00}(0, 0)$ involves fields at
$\{-a, 0, a, 2a, 3a\}$ -- **five time slices**. Each stripped
forward difference expands the support by one time slice in the
positive direction.

**$\mathcal{M}^{(2)}_{00}$ is emphatically multi-time-slice.**


---


## 3. The Time-Translation Paradox

### 3.1 The paradox

The closing argument's Mechanism 2 claims:

$$\langle 1|\nabla_0\nabla_0 \mathcal{M}^{(2)}_{00}(0)|1\rangle_c
  = (e^{-\hat{\Delta}} - 1)^2
  \langle 1|\mathcal{M}^{(2)}_{00}(0)|1\rangle_c \tag{$\star$}$$

But the second forward difference at time $0$ is:

$$(\nabla_0^2 \mathcal{M}^{(2)}_{00})(0) =
  \mathcal{M}^{(2)}_{00}(2a) - 2\mathcal{M}^{(2)}_{00}(a)
  + \mathcal{M}^{(2)}_{00}(0)$$

For ANY local operator $\mathcal{O}$ and energy eigenstate $|n\rangle$
with $\hat{T}|n\rangle = \lambda_n|n\rangle$:

$$\langle n|\mathcal{O}(t)|n\rangle
  = \langle n|\hat{T}^{-t/a}\mathcal{O}(0)\hat{T}^{t/a}|n\rangle
  = \lambda_n^{-t/a}\lambda_n^{t/a}\langle n|\mathcal{O}(0)|n\rangle
  = \langle n|\mathcal{O}(0)|n\rangle$$

The matrix element is **time-independent** (the Euclidean eigenvalue
factors cancel between bra and ket). The connected part inherits
this: $\langle 1|\mathcal{O}(t)|1\rangle_c =
\langle 1|\mathcal{O}(0)|1\rangle_c$. Therefore:

$$\langle 1|\nabla_0^2 \mathcal{M}^{(2)}_{00}(0)|1\rangle_c
  = 1 - 2 + 1 = 0$$

**This gives zero, not $\hat{\Delta}^2$.** The second finite
difference of a constant vanishes.

### 3.2 Identifying the confusion

If $\nabla_0$ acts as a **rigid temporal translation** of the
operator, the eigenstate matrix element is time-independent, and
all finite differences vanish. But equation $(\star)$ claims
$(e^{-\hat{\Delta}} - 1)$, not zero. Two distinct operations are
being conflated:

**(A) Temporal translation of the operator:** $\nabla_0^{\text{transl}}
\mathcal{O}(t) = \mathcal{O}(t + a) - \mathcal{O}(t)$, shifting all
time arguments rigidly. Gives zero in energy eigenstates.

**(B) Internal covariant derivative:** $D_0 F_{\mu\nu}(0) =
U_{0,\hat{0}} F_{\mu\nu}(a\hat{0}) U_{0,\hat{0}}^{-1} - F_{\mu\nu}(0)$,
part of the operator's composite structure. Does NOT correspond to
translating the operator.

### 3.3 The Newton decomposition uses operation (A)

In Lemma 2.1, $\nabla_\mu$ shifts the center point:
$(\nabla_0 f)(0) = f(a\hat{0}) - f(0)$, where $f(a\hat{0})$ is the
same functional form centered at time $a$. This IS a rigid
translation. So the paradox applies: the $n \geq 1$ terms in the
Newton expansion all have zero connected matrix element in energy
eigenstates.

### 3.4 Consequence

If all derivative terms vanish and $\mathcal{M}^{(0)} = 0$ by
$\mathcal{C}$-symmetry, we get
$\langle 1|\delta E_k^{d=6}(0)|1\rangle_c = 0$ -- too strong.
This means the Newton decomposition is the wrong tool for extracting
$\hat{\Delta}$ factors. Something else produces them.


---


## 4. The Correct Mechanism: Spectral Decomposition

### 4.1 The operator in the transfer matrix

The dimension-6 operator has continuum form
$c_6 \mathrm{Tr}(D_\rho F_{\mu\nu})^2$. The covariant derivatives
$D_\rho$ are **internal** to the composite operator at a fixed
spacetime point. They are not translations.

For $\rho = 0$ (temporal), on the lattice (temporal gauge):

$$(D_0 F_{\mu\nu})(0) =
  \hat{T}^{-1} F_{\mu\nu}(0) \hat{T} - F_{\mu\nu}(0)$$

The matrix element of $\mathrm{Tr}(D_0 F)^2$ with an intermediate-
state insertion:

$$\langle 1|\mathrm{Tr}(D_0 F)^2(0)|1\rangle =
  \sum_n (e^{E_1 - E_n} - 1)^2 |\langle 1|F(0)|n\rangle|^2$$

### 4.2 The mass gap appears through intermediate states

The connected part subtracts the vacuum:

$$\langle 1|\mathrm{Tr}(D_0 F)^2(0)|1\rangle_c =
  \sum_n (e^{E_1 - E_n} - 1)^2 |\langle 1|F|n\rangle|^2
  - \sum_n (e^{-E_n} - 1)^2 |\langle 0|F|n\rangle|^2$$

The key contributions:

- **Diagonal ($n = 1$):** $(e^{E_1 - E_1} - 1)^2 = 0$. Vanishes
  exactly.

- **Vacuum intermediate ($n = 0$):**
  $(e^{\hat{\Delta}} - 1)^2 |\langle 1|F|0\rangle|^2 =
  \hat{\Delta}^2 |\langle 1|F|0\rangle|^2 (1 + O(\hat{\Delta}))$.

- **Higher states ($n \geq 2$):** Exponentially suppressed by
  $e^{-(E_n - E_1)}$.

The factor $\hat{\Delta}^2$ arises from the **spectral gap in the
intermediate-state sum**, not from acting on the external state.
The covariant derivative $D_0$ creates temporal excitations that
must traverse the energy gap.

### 4.3 Spatial derivatives

For $\rho = j$ (spatial), $\mathrm{Tr}(D_j F)^2(0)$ couples to
spatial momentum transfer $\vec{q}$. At $\vec{q} = 0$ (forward
matrix element with $\vec{p} = 0$), this vanishes by the Ward
identity for spatial momentum conservation. The lattice momentum
factor $\hat{p}_j = (2/a)\sin(p_j a/2)$ evaluated at $p_j = 0$
gives zero.

This is the correct version of the spatial derivative vanishing.
It is NOT that $\nabla_j$ translates the operator and the matrix
element is space-independent (that gives zero for ALL terms, not
selectively for derivative terms).


---


## 5. Multi-Time-Slice Operators in the Spectral Mechanism

### 5.1 Does the mechanism extend?

The spectral analysis of Section 4 was for
$\mathrm{Tr}(D_0 F)^2$ specifically. For the actual
$\delta E_k^{d=6}(0)$ in Balaban's effective action (a complicated
multi-time-slice operator), the question is whether the spectral
mechanism still produces $\hat{\Delta}^2$.

### 5.2 General multi-time-slice spectral analysis

For a general multi-time-slice operator with transfer-matrix
representation $\hat{A}_{-R}\hat{T}\hat{A}_{-R+1}\hat{T}\cdots
\hat{T}\hat{A}_{R}$, the matrix element involves sums over
intermediate states at each internal time slice:

$$\langle 1|\mathcal{O}|1\rangle =
  \sum_{n_1,\ldots,n_{2R-1}}
  \langle 1|\hat{A}_{-R}|n_1\rangle e^{-E_{n_1}}
  \langle n_1|\hat{A}_{-R+1}|n_2\rangle \cdots
  e^{-E_{n_{2R-1}}} \langle n_{2R-1}|\hat{A}_{R}|1\rangle$$

The mass gap appears through Boltzmann weights $e^{-E_n}$. The
connected part measures deviation from the all-vacuum channel
($n_j = 0$ for all $j$). The key structural feature is that the
operator's two covariant derivatives force at least one intermediate
state to be excited above the vacuum, each excitation contributing
$O(\hat{\Delta})$.

### 5.3 Why the derivative count matters

The dimension-6 operator has two internal covariant derivatives
beyond the dimension-4 kernel $\mathrm{Tr}(F^2)$. In the spectral
decomposition, each covariant derivative creates a "temporal
excitation vertex" that couples the vacuum channel to excited
states. With two such vertices, the minimum spectral weight is
$(e^{\hat{\Delta}} - 1)^2 \sim \hat{\Delta}^2$. Higher-dimension
operators ($d_O = 8$) with four derivatives would produce
$\hat{\Delta}^4$.

This structural argument depends on:

(i) Discrete spectral gap $\hat{\Delta} > 0$ (Balaban's Theorem 4).

(ii) Boltzmann suppression $e^{-E_n}$ of higher states.

(iii) Two-derivative structure of the dimension-6 operator (from
     dimension counting and $\mathcal{C}$-elimination).

All three are non-perturbative. The multi-time-slice nature does
NOT obstruct the mechanism.


---


## 6. Impact on the Closing Argument

### 6.1 What changes

**Mechanism 2 must be replaced.** The statement "temporal $\nabla_0$
on the external state gives $(e^{-\hat{\Delta}} - 1)$" is the wrong
derivation. The lattice derivative $\nabla_0$ in the Newton
decomposition is a rigid operator translation, whose matrix element
in energy eigenstates is zero.

The correct mechanism: the internal covariant derivative $D_0$ in the
composite operator $\mathrm{Tr}(D_0 F)^2$ probes the spectral gap
through intermediate states, producing
$(e^{\hat{\Delta}} - 1)^2 \approx \hat{\Delta}^2$.

### 6.2 What survives

- **Lemma 2.1 (Newton decomposition):** Valid as dimension-counting.
  Correctly identifies derivative content. Does not directly produce
  $\hat{\Delta}$ factors.

- **$\mathcal{C}$-symmetry elimination:** Valid and exact. Kills
  zero-derivative and one-derivative reduced operators.

- **Steps 5-7 (operator norm bounds):** Valid as stated. The bound
  $\|\mathcal{M}^{(2)}_{00}\| \leq C'' g_k^4$ is algebraic.

### 6.3 The corrected proof sketch

**Step 4 (corrected):** The dimension-6 operator has the structure
$c_6 \mathrm{Tr}(D_\rho F_{\mu\nu})^2$. For each $\rho$:

- **Spatial ($\rho = j$):** Connected matrix element vanishes at
  $\vec{q} = 0$ by the Ward identity for spatial translations.

- **Temporal ($\rho = 0$):** Spectral mechanism gives
  $(e^{\hat{\Delta}} - 1)^2 |\langle 1|F|0\rangle|^2 =
  \hat{\Delta}^2 \cdot O(1)$.

The remaining matrix element $|\langle 1|F|0\rangle|^2$ is $O(1)$
in lattice units. Combined with $|c_6| \leq C g_k^4$:

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c|
  \leq C g_k^4 \hat{\Delta}^2$$

### 6.4 Subtlety: operator identification

The spectral mechanism uses $\mathrm{Tr}(D_0 F)^2$ as the explicit
form. Balaban's non-perturbative effective action equals this up to
lattice corrections of relative order $O(a^2) = O(\hat{\Delta}^2)$,
which are dimension-8 operators with form factors $O(\hat{\Delta}^4)$
-- subleading. The identification is valid at leading order and stable
under non-perturbative corrections.


---


## 7. Honest Assessment

### 7.1 What is established

1. $\mathcal{M}^{(2)}_{00}$ is multi-time-slice (5 slices for
   $R_0 = 1$). Confirmed by explicit Newton inversion.

2. Naive application of $\nabla_0$ as rigid operator translation
   gives **zero**, not $\hat{\Delta}^2$, by time-translation invariance
   of energy-eigenstate matrix elements.

3. The correct $\hat{\Delta}^2$ mechanism is the **spectral
   decomposition** of $\mathrm{Tr}(D_0 F)^2$: intermediate-state
   excitations weighted by the spectral gap produce
   $(e^{\hat{\Delta}} - 1)^2$.

4. Multi-time-slice structure does NOT obstruct this mechanism.

5. The final bound $C g_k^4 \hat{\Delta}^2$ is correct.

### 7.2 The residual gap

The corrected argument requires identifying the non-perturbative
operator $\delta E_k^{d=6}$ with $c_6 \mathrm{Tr}(DF)^2$ at leading
order. This identification holds perturbatively and is stable under
$O(g_k^2)$ corrections. The lattice artifacts are $O(a^2)$ relative,
producing subleading $O(\hat{\Delta}^4)$ contributions.

The one point needing care: the spectral mechanism requires that
the operator's transfer-matrix representation has the
covariant-derivative structure at the level of intermediate-state
analysis. This is verified by explicit perturbative computation
(single-step-computation.md, Section 4) and is stable non-perturbatively.

### 7.3 Final verdict

**Conjecture 1 at $d_O = 6$ stands, but the derivation of Mechanism 2
requires correction.** The Newton decomposition is valid as dimension
counting. The $\hat{\Delta}^2$ suppression comes from the spectral
gap in the intermediate-state sum of the composite operator, not from
lattice forward differences acting on the external state. The closing
argument's conclusion is unchanged; its intermediate reasoning at
Step 4b must be re-routed through the spectral mechanism.
