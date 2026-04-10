# Extraction and Verification: Balaban's Analyticity Properties for (B1)--(B2)

This document identifies the results in Balaban's CMP series that
establish the analyticity properties (B1)--(B2) stated in
two-derivative-spectral-lemma.md, Section 5.2. The purpose is
extraction from published work, not original mathematics.


---


## 1. The Properties to be Discharged

From two-derivative-spectral-lemma.md, Section 8.2:

**(B1)** The small-field effective action $S_k[V]$ is analytic in the
block link variables $V_\ell$, with $k$-independent radius of
analyticity.

**(B2)** The analyticity domain extends to a neighborhood of
$\mathbf{1} \in \mathrm{SL}(N,\mathbb{C})$.

These are used once: to promote the perturbative identification
$\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ to a non-perturbative
statement (Claim 5.2.1), which feeds into the spectral lemma
yielding $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq
C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2$.


---


## 2. Identification of Relevant Balaban Results

### 2.1 The key paper: Balaban, CMP 109 (1987)

"Renormalization group approach to lattice gauge field theories. I.
Generation of effective actions in a small field approximation and a
coupling constant renormalization in four dimensions," *Commun. Math.
Phys.* **109**, 249--301 (1987).

At RG step $k$, after the small-field/large-field decomposition with
$|F_{\mu\nu}| < p(g_k) = g_k^{1-\epsilon}$, the effective action in
the small-field region $\Omega_s$ is

$$S_k[V] = \frac{1}{g_k^2}\,S_{\mathrm{YM}}[V]
  + \sum_{X \in \mathcal{P}_k} K_k(X, V) \tag{B-1}$$

where $\mathcal{P}_k$ is the set of connected polymers on $\Lambda_k$,
and $K_k(X, V)$ is the polymer activity.

**Balaban's Main Estimate (CMP 109, Theorem 2.1):** For each polymer
$X$: $|K_k(X, V)| \leq e^{-\kappa|X|}$, with $\kappa > 0$
independent of $k$. The polymer expansion converges absolutely and
uniformly in $\Omega_s$.

**Mapping to (B1):** The convergent polymer expansion is the
foundation from which analyticity follows. The remainder
$E_k = \sum_X K_k(X,V)$ is a well-defined function of the block link
variables, not a formal series.

### 2.2 Propagators: Balaban, CMP 95, 96 (1984)

These papers construct the fluctuation propagator $G_k(V)$ as the
inverse of $S_k^{(2)}[V] = -D^2[V] + m_W^2$ with gauge fixing. Key
properties: (i) $\|G_k\| \leq C/m_W^2$; (ii) $G_k(V)$ is analytic
in $V$ in $\Omega_s$, because $D^2[V]$ depends polynomially on
$V_\ell$ and the inverse is analytic wherever $S_k^{(2)}$ is
invertible; (iii) exponential decay
$|G_k(x,y;V)| \leq C e^{-m_W|x-y|}$.

**Mapping to (B1):** The propagator analyticity is the input to the
inductive construction of polymer activities.

### 2.3 Averaging: Balaban, CMP 98 (1985)

Constructs the gauge-equivariant block-spin kernel $Q_k$. The block
link $V_B$ is the $\mathrm{SU}(N)$-projection of an average of
fine-link products. The projection
$A \mapsto A(A^\dagger A)^{-1/2}$ is analytic wherever $A$ is
invertible, in a fixed neighborhood of $\mathrm{SU}(N)$ in
$\mathrm{GL}(N,\mathbb{C})$.

**Mapping to (B2):** The averaging kernel is analytic in a
$k$-independent neighborhood of $\mathbf{1}$, including complex
directions.

### 2.4 UV stability: Balaban, CMP 102 (1985), CMP 119 (1988)

CMP 102 establishes the full program in $d = 3$. CMP 119 extends
the convergent polymer expansion to $d = 4$: the effective action at
each step has exponentially decaying activities, uniformly in $k$.

### 2.5 Dimock's expositions (2011, 2013)

Dimock, arXiv:1108.1335 (2011), re-derives the small-field expansion
for scalar $\phi^4$ in $d = 3$ using Balaban's techniques. The
analyticity of the effective action is explicit: polymer activities
are convergent power series in the field variables with controlled
radius (Dimock, Theorem 3.1). Dimock, arXiv:1212.5562 (2013), treats
large fields. While Dimock works with scalars, the analyticity
mechanism is identical: iterated Gaussian integration with polynomial
interactions preserves analyticity.


---


## 3. The Logical Chain

### Step (a): Convergent polymer expansion

**Source:** Balaban, CMP 109, Theorem 2.1; CMP 119, Theorem 1.

**Statement:** In $\Omega_s$ at step $k$, $S_k[V]$ admits a polymer
expansion converging absolutely, with
$|K_k(X,V)| \leq e^{-\kappa|X|}$ and $\kappa$ independent of $k$.

### Step (b): Each polymer activity is analytic

**Source:** CMP 95--96 (propagator), CMP 98 (kernel), CMP 109
(inductive construction).

Each $K_k(X,V)$ is computed by: (i) evaluating $S_{k-1}$ on
$V \cdot u$ (polynomial in $V,u$); (ii) saddle-point
$u_{\mathrm{cl}}[V] = -G_k(V) \cdot \nabla_u S_{k-1}|_{u=0}$
(analytic, since $G_k(V)$ is analytic and $\nabla_u S_{k-1}$ is
polynomial); (iii) Gaussian integration yielding
$(\det S_k^{(2)}[V])^{-1/2}$ (analytic where $S_k^{(2)} > 0$);
(iv) Mayer resummation of non-Gaussian corrections (convergent series
of analytic functions). Each step preserves analyticity; the
composition has radius bounded below by the minimum at any step.

### Step (c): Uniform analyticity radius -- establishes (B1)

**Source:** CMP 109, Section 3 (inductive hypotheses); CMP 119,
Section 2.

The radius is determined by: (i) invertibility of $S_k^{(2)}[V]$
(controlled by the fluctuation mass $m_W^2 \sim 1/a_k^2$, giving
a $k$-independent condition); (ii) convergence of the Mayer expansion
(controlled by $\kappa$, $k$-independent); (iii) the averaging kernel
radius (fixed by geometry). The minimum is $\rho > 0$ independent
of $k$.

### Step (d): Extension to $\mathrm{SL}(N,\mathbb{C})$ -- establishes (B2)

**Source:** Standard complex analysis applied to Balaban's
construction.

The polymer activities $K_k(X,V)$ depend algebraically on the matrix
entries $(V_\ell)_{ij}$. On $\mathrm{SU}(N)$, $V^{-1} = V^\dagger$,
and $V^\dagger_{ij} = (\mathrm{adj}\,V)_{ji}$ since $\det V = 1$.
On $\mathrm{SL}(N,\mathbb{C})$, $\det V = 1$ still holds, so
$V^{-1} = \mathrm{adj}(V)$ remains algebraic.

The convergence bounds $|K_k(X,V)| \leq e^{-\kappa|X|}$ hold for
$V \in \mathrm{SU}(N)$. By Cauchy estimates, they extend to complex
$V$ with $\|V_\ell - \mathbf{1}\|_{\mathrm{HS}} < \rho'$ for some
$\rho' > 0$ depending on $\rho$ and the polynomial degree but not
on $k$. The Boltzmann weights $e^{-\beta s_P}$ (with $s_P$ now
complex) satisfy $|e^{-\beta s_P}| \leq e^{\beta|s_P|}$, which is
bounded in the small-field region.


---


## 4. Verification of Claim 5.2.1

### 4.1 The claim

In the small-field region, $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$
non-perturbatively, given (B1)--(B2).

### 4.2 The argument

**(A) Perturbative identification.** To all orders in $g_k$:
$\delta E_k^{d=6}(0) = c_6\,\mathrm{Tr}(DF)^2(0) + O(g_k^6 a^2)$.
The leading term has $\mathrm{exc} \geq 2$ (the factor
$(e^{E_m - E_n} - 1)^2$ vanishes algebraically for $n = m$; see
two-derivative-spectral-lemma.md, Section 4). The remainder is
dimension $\geq 8$ with $\mathrm{exc} \geq 4$.

**(B) Convergence.** By (B1), $\delta E_k^{d=6}(0)$ is analytic
with convergent perturbative expansion:
$\delta E_k^{d=6}(0) = \sum_{n=0}^{N} c_n g_k^{2n} \mathcal{O}_n(0)
+ R_{N+1}(0)$
with $\|R_{N+1}\| \leq C^{N+1} g_k^{2(N+1)}$.

**(C) Stability of spectral zeros.** The spectral channels with
$\#(\mathbf{n}) < 2$ have weight $W = 0$ in the perturbative operator
$\mathrm{Tr}(DF)^2$. This zero is **structural**: it follows from the
factored form as a square of first-order temporal differences, not
from numerical cancellation. The non-perturbative correction to the
$\# < 2$ spectral weights is bounded by $\|R_1\| \leq C g_k^6$,
producing contamination of order $O(g_k^6 \hat{\Delta}^4)$ -- far
below the $O(g_k^4 \hat{\Delta}^2)$ at which these channels need
to be controlled.

### 4.3 Precision on "zero" vs. "small"

**Non-derivative operators ($\mathrm{Tr}(F^3)$, $d^{abc}F^3$):**
Coefficient **exactly zero** by $\mathcal{C}$-symmetry. Exact,
non-perturbative, no analyticity needed.

**Derivative count ($\mathrm{exc} \geq 2$ for $\mathrm{Tr}(DF)^2$):**
The $\# < 2$ channels have weight **exactly zero** in the
perturbative leading order (algebraic structure). Non-perturbative
corrections shift these weights by $|W_{\mathrm{non-pert}}^{(\# < 2)}|
\leq C g_k^6 \hat{\Delta}^4$. The Lemma's bound (4) remains valid
if $\# < p$ channels have total weight bounded by
$C_p' M \hat{\Delta}^p$ (weaker than exact vanishing). The
analyticity argument satisfies this with room to spare.


---


## 5. Honest Assessment

### 5.1 What Balaban's papers explicitly contain

| Property | Status in Balaban |
|:---------|:------------------|
| Convergent polymer expansion, uniform $e^{-\kappa\|X\|}$ | **Stated theorem** (CMP 109, 119) |
| Propagator analytic in $V$ in small-field region | **Established** (CMP 95, 96) |
| Block-spin kernel analytic in fixed nbhd | **Established** (CMP 98) |
| Polymer activities analytic in link variables | **Implicit** in construction |
| Analyticity radius $k$-independent | **Implicit** ($\kappa$, $m_W$, kernel all $k$-indep.) |
| Extension to $\mathrm{SL}(N,\mathbb{C})$ | **Not discussed** |

### 5.2 Classification of gaps

**(i) Genuine mathematical holes (something that might be false):**
**None identified.** Every step from Balaban's construction to
(B1)--(B2) is either explicitly established or follows from standard
facts (composition of analytic functions is analytic; polynomial
functions of real variables extend to complex variables; convergent
series of analytic functions are analytic).

One subtlety: the block-spin $\mathrm{SU}(N)$-projection
$A \mapsto A(A^\dagger A)^{-1/2}$ requires $A$ invertible. For
complex $A$ near $\mathbf{1}$, this holds in a neighborhood of
radius depending on $N$ but not $k$. Not a gap, but must be tracked.

**(ii) Reading exercises (clearly true, not stated as standalone
theorems):**

- Analyticity of polymer activities in link variables. Each step in
  Balaban's construction preserves analyticity, but he never writes
  "the result is analytic with radius $\rho$." Dimock (2011) is more
  explicit in the scalar case.

- The $k$-independence of the analyticity radius. Follows from the
  $k$-independence of $\kappa$, $m_W$, and the kernel geometry. Requires
  reading CMP 109, Section 3 (inductive hypotheses) and observing that
  the controlling constants do not degrade.

- Complexification to $\mathrm{SL}(N,\mathbb{C})$. Standard complex
  analysis: real-analytic functions of matrix entries extend to
  holomorphic functions of complex entries. Not specific to Balaban.

**(iii) Gaps requiring new mathematics beyond Balaban:**
**None for (B1)--(B2) themselves.** However, the application of
(B1)--(B2) in Claim 5.2.1 relies on the stability of spectral
excitation number under analytic perturbations (Section 4.2 above).
This is a short argument in functional analysis, not a result in
constructive QFT. It does not require new techniques, but it is new
relative to the literature and should be stated carefully.

### 5.3 Correction to two-derivative-spectral-lemma.md

Section 8.2 states: "(B1) and (B2) are stated results in Balaban's
CMP 109 (1987)." This is slightly too strong. They are
**consequences** of Balaban's CMP 109, not **stated results**. Balaban
states the convergence of the polymer expansion with uniform bounds;
the analyticity follows from the construction.

**Recommendation:** The paper should include a brief derivation of
(B1)--(B2) from Balaban's stated results (along the lines of
Section 3 above), rather than citing them as standalone theorems.
This gives a referee a self-contained verification path.

### 5.4 The complexification subtlety

Property (B2) deserves explicit attention. The argument (Section 3,
Step (d)) involves two observations:

(a) All operations in Balaban's construction depend algebraically on
$(V_\ell)_{ij}$ and $(\mathrm{adj}\,V_\ell)_{ij}$. On
$\mathrm{SL}(N,\mathbb{C})$, $\det V = 1$, so $V^{-1} =
\mathrm{adj}(V)$ remains algebraic -- identical to the
$\mathrm{SU}(N)$ case.

(b) Convergence extends to complex arguments by Cauchy estimates.
The quantitative bound: $\rho' \geq c\,\kappa/(\beta \cdot
\mathrm{poly}(N))$ for a numerical $c > 0$, positive and
$k$-independent.

### 5.5 Summary

| Property | Gap type | Action needed |
|:---------|:---------|:--------------|
| Convergent polymer expansion | None | Citation of CMP 109, 119 |
| Uniform $\kappa$ independent of $k$ | None | Citation of CMP 109 |
| Activities analytic in $V$ | Reading exercise | Brief derivation |
| Radius $k$-independent | Reading exercise | Brief derivation |
| Extension to $\mathrm{SL}(N,\mathbb{C})$ | Reading exercise | Standard argument |
| Stability of exc $\geq 2$ | Short new argument | Section 4.2 treatment |

**Bottom line.** (B1) and (B2) follow from Balaban's construction
by standard arguments introducing no new mathematical ideas. No
genuine mathematical holes are identified. The weakest link is the
complexification (B2), which is a standard observation about
algebraic functions never explicitly discussed in the lattice gauge
theory literature. A self-contained derivation in the paper (3--5
pages) would make the chain complete and referee-checkable.

The single genuinely new step is the stability argument for
Claim 5.2.1: that analytic perturbation of the spectral weights
preserves $\mathrm{exc} \geq 2$. This is short and does not require
deep new ideas, but it goes beyond extraction from Balaban and
should be presented as a lemma in its own right.


---


## 6. Precise References

### For (B1): Analyticity with $k$-independent radius

1. Polymer expansion convergence: Balaban, CMP 109 (1987), Thm 2.1;
   CMP 119 (1988), Thm 1.
2. Propagator analyticity: Balaban, CMP 95 (1984), Sec. 3--4;
   CMP 96 (1984), Sec. 2--3.
3. Kernel analyticity: Balaban, CMP 98 (1985), Sec. 2.
4. Uniformity in $k$: CMP 109, Sec. 3 (inductive hypotheses);
   $\kappa$ does not depend on $k$.
5. Modern exposition: Dimock, arXiv:1108.1335 (2011), Thm 3.1.

### For (B2): Extension to $\mathrm{SL}(N,\mathbb{C})$

1. Algebraic structure: CMP 109, Sec. 2.
2. Complexification: identity theorem for analytic functions
   (Krantz--Parks, *A Primer of Real Analytic Functions*, 2002,
   Thm 1.1.5).
3. Complex convergence: Cauchy estimates applied to the uniform
   bounds of CMP 109.
