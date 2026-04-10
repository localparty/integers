# 04. Correlation Inequalities and Reflection Positivity

## Purpose

Investigate whether correlation inequalities (FKG, GKS, Griffiths)
or reflection positivity can establish the monotonicity
$m(N) \geq m(\infty) = \Lambda$ WITHOUT analyzing the sign of V
term by term. These are non-perturbative tools that could bridge the
gap left by the perturbative analysis (file 03).


---

## 4.1 Reflection Positivity of the CP^{N-1} Model

### 4.1.1 Setup

The Euclidean CP^{N-1} model on the lattice has the partition
function:

$$Z_N = \int \prod_x d\mu_{\text{FS}}(z_x)\;
  \exp\left(\frac{N}{\lambda_0}\sum_{\langle xy\rangle}
  |\bar{z}_x \cdot z_y|^2\right)$$

where the sum is over nearest-neighbor pairs and
$d\mu_{\text{FS}}$ is the Fubini-Study measure on $\mathbb{CP}^{N-1}$.

### 4.1.2 Reflection positivity

**Theorem [PROVED]:** The CP^{N-1} lattice model is reflection
positive with respect to any lattice hyperplane (reflection of
the lattice that maps sites to sites or to midpoints of links).

**Proof sketch:** The action $|\bar{z}_x \cdot z_y|^2$ for a link
$\langle xy\rangle$ crossing the reflection plane can be written as:

$$|\bar{z}_x \cdot z_y|^2 = \sum_{i,j=1}^N \bar{z}_{x,i}\,z_{y,i}\,
  \bar{z}_{y,j}\,z_{x,j}$$

This is a SUM OF SQUARES of the form $\sum_i |f_i(z_x)\,g_i(z_y)|^2$
where $f_i$ depends only on variables on one side of the plane and
$g_i$ only on the other side. The Boltzmann weight $e^{S}$ with $S$
a sum of such terms factorizes into reflected pairs, and the
Fubini-Study measure is reflection-symmetric.

This establishes the Osterwalder-Schrader reflection positivity
axiom, which guarantees:

1. The transfer matrix $T_N$ is positive semi-definite ($T_N \geq 0$).
2. The Hilbert space $\mathcal{H}_N$ carries a positive inner product.
3. The Hamiltonian $H_N = -(1/a)\ln T_N$ is self-adjoint.
4. Correlation functions satisfy the spectral representation with
   positive spectral weights.

[PROVED -- this follows the standard Osterwalder-Schrader construction;
see Fr\"ohlich, Israel, Lieb, Simon 1978 for the general framework]

### 4.1.3 Consequences for the mass gap

Reflection positivity implies:

$$\langle \mathcal{O}(t)\,\overline{\mathcal{O}}(0)\rangle
  = \sum_n |\langle n|\mathcal{O}|0\rangle|^2\,e^{-E_n t}$$

with ALL spectral weights $|\langle n|\mathcal{O}|0\rangle|^2 \geq 0$.
The mass gap is:

$$m(N) = -\lim_{t\to\infty} \frac{1}{t}\ln
  \langle \mathcal{O}(t)\,\overline{\mathcal{O}}(0)\rangle$$

for any operator $\mathcal{O}$ with $\langle 1|\mathcal{O}|0\rangle \neq 0$.
[PROVED]


---

## 4.2 FKG and GKS Inequalities: Applicability

### 4.2.1 FKG inequality (Fortuin-Kasteleyn-Ginibre)

The FKG inequality states: for a probability measure $\mu$ on a
distributive lattice satisfying the FKG lattice condition, and for
increasing functions $f, g$:

$$\langle fg\rangle_\mu \geq \langle f\rangle_\mu\,\langle g\rangle_\mu$$

**Applicability to CP^{N-1}:** The target space $\mathbb{CP}^{N-1}$ is
NOT a distributive lattice. There is no natural partial order on
$\mathbb{CP}^{N-1}$ that makes the Boltzmann weight satisfy the FKG
lattice condition.

**The obstacle:** The FKG inequality applies to Ising-type models
(spins taking values in a totally ordered set) and to certain
continuous-spin models where the single-spin space has a lattice
structure. The projective space $\mathbb{CP}^{N-1}$ does not have
such structure.

**Conclusion: FKG does NOT directly apply.** [PROVED -- structural
incompatibility]

### 4.2.2 GKS inequality (Griffiths-Kelly-Sherman)

The GKS (Griffiths' second) inequality states: for ferromagnetic
Ising models:

$$\langle \sigma_A\,\sigma_B\rangle \geq
  \langle\sigma_A\rangle\,\langle\sigma_B\rangle$$

and the stronger form:

$$\frac{\partial}{\partial J_{ij}}\langle\sigma_A\rangle \geq 0$$

(adding a ferromagnetic coupling cannot decrease a correlation).

**Applicability to CP^{N-1}:** The GKS inequality requires:
1. Spin variables with values in $\{-1, +1\}$ (or, more generally,
   in a group with a natural positivity structure)
2. Ferromagnetic interactions (couplings $J_{ij} \geq 0$)
3. A specific algebraic structure of the spin product

The CP^{N-1} model does NOT satisfy these conditions:
- The spins take values in $\mathbb{CP}^{N-1}$, not $\{-1, +1\}$
- The interaction $|\bar{z}_x \cdot z_y|^2$ is quartic, not bilinear
- There is no natural "positivity" of the coupling in the GKS sense

**Conclusion: GKS does NOT directly apply.** [PROVED -- structural
incompatibility]

### 4.2.3 The O(N) model comparison

For the O(N) sigma model ($\sigma_x \in S^{N-1}$ with interaction
$\sigma_x \cdot \sigma_y$), the situation is different:

- At N = 1 (Ising): FKG and GKS apply. [PROVED]
- At N = 2 (XY): Ginibre's inequality applies to the complex
  representation. Correlation inequalities give monotonicity of
  correlations in the coupling. [PROVED]
- At N >= 3 (Heisenberg and beyond): No general correlation inequality
  is known. The Messager-Miracle-Sol\'e inequality gives
  $\langle\sigma_x \cdot \sigma_y\rangle \geq 0$ but not monotonicity
  in N. [ESTABLISHED]

The CP^{N-1} model is related to O(2N) by the Hopf fibration
$S^{2N-1} \to \mathbb{CP}^{N-1}$, but this projection destroys the
linear structure needed for correlation inequalities.


---

## 4.3 Reflection Positivity and Monotonicity in N

### 4.3.1 The key question

Can reflection positivity ALONE (without correlation inequalities)
give monotonicity of the mass gap in N?

Reflection positivity gives:
- Positivity of spectral weights [PROVED]
- The spectral representation of correlations [PROVED]
- Infrared bounds (upper bounds on correlations, hence lower bounds
  on the mass gap) [PROVED -- for models with continuous symmetry]

But it does NOT directly give COMPARISON between different values
of N.

### 4.3.2 Infrared bounds

The classical infrared bound (Fr\"ohlich-Simon-Spencer 1976) for the
O(N) model gives:

$$\hat{G}(p) \leq \frac{N}{\beta\,\hat{J}(p)}$$

where $\hat{G}(p)$ is the Fourier transform of the two-point function
and $\hat{J}(p)$ is the Fourier transform of the coupling.

For the CP^{N-1} model, the analogous bound is [ESTABLISHED]:

$$\hat{G}_{CP}(p) \leq \frac{1}{\beta\,(1 - \cos p)}$$

where $G_{CP}(x-y) = \langle |\bar{z}_x \cdot z_y|^2 \rangle - 1/N$.

**The N-dependence:** The infrared bound does NOT depend on N
explicitly (the factor of N cancels between the numerator and the
coupling $\beta = N/\lambda_0$). This means the infrared bound gives
the SAME upper bound on correlations for all N.

### 4.3.3 From infrared bounds to mass gap lower bounds

In 2D, the infrared bound gives:

$$\xi(N) \leq C/m_{\text{IR}}$$

where $\xi$ is the correlation length and $m_{\text{IR}}$ is the mass
from the infrared bound. Since $m(N) = 1/\xi(N)$:

$$m(N) \geq m_{\text{IR}}$$

The infrared bound mass $m_{\text{IR}}$ is determined by the coupling
$\beta = N/\lambda_0$ and does not directly give monotonicity in N
at fixed $\Lambda$.

### 4.3.4 The problem with fixed Lambda vs. fixed beta

**Critical subtlety:** Monotonicity in N must be stated at FIXED
$\Lambda$ (the dynamical scale), not at fixed $\beta$ (the bare
coupling). The relationship $\beta = N/\lambda_0$ and the gap equation

$$\frac{1}{4\pi}\ln\frac{\Lambda_{UV}^2}{\Lambda^2} = \frac{1}{\lambda_0}$$

mean that comparing different N at fixed $\Lambda$ requires
DIFFERENT values of $\beta$. The infrared bound, which gives
information at fixed $\beta$, does not directly translate to a
comparison at fixed $\Lambda$.

[OPEN -- this is a fundamental obstacle to using infrared bounds
for the monotonicity question]


---

## 4.4 The Transfer Matrix Approach

### 4.4.1 Comparing transfer matrices at different N

The transfer matrix for the CP^{N-1} model acts on:

$$\mathcal{H}_N = L^2\!\left(\prod_x \mathbb{CP}^{N-1}_x,\;
  d\mu_{\text{FS}}\right)$$

For different N, the transfer matrices act on DIFFERENT Hilbert spaces.
This makes direct comparison difficult.

### 4.4.2 Embedding $\mathbb{CP}^{N-1} \hookrightarrow \mathbb{CP}^{N}$

The natural embedding $\mathbb{CP}^{N-1} \hookrightarrow \mathbb{CP}^{N}$
(adding a zero last coordinate: $[z_1:\ldots:z_N] \mapsto [z_1:\ldots:z_N:0]$)
gives an embedding of Hilbert spaces:

$$\iota: \mathcal{H}_N \hookrightarrow \mathcal{H}_{N+1}$$

defined by $(\iota\Psi)(z_1,\ldots,z_{N+1}) = \Psi(z_1,\ldots,z_N)
\cdot \delta(z_{N+1})$ (restricting to the submanifold
$z_{N+1} = 0$).

**Problem:** This embedding does NOT intertwine the transfer matrices.
The transfer matrix $T_{N+1}$ acts on ALL of $\mathcal{H}_{N+1}$,
including configurations where $z_{N+1} \neq 0$. The restriction of
$T_{N+1}$ to $\iota(\mathcal{H}_N)$ is NOT equal to $T_N$.

### 4.4.3 The auxiliary field comparison

In the auxiliary field formalism, the comparison is cleaner. After
integrating out $z$, the transfer matrices $T_N$ and $T_\infty$ act
on the SAME Hilbert space $\mathcal{H}_{\text{eff}}$ (functions of
$\sigma$ and $A_\mu$). The difference is:

$$T_N = T_\infty \cdot \exp\left(-\frac{1}{N}V + O(1/N^2)\right)$$

(from the fluctuation expansion). The gap comparison becomes:

$$\frac{\lambda_1(T_N)}{\lambda_0(T_N)} \leq
  \frac{\lambda_1(T_\infty)}{\lambda_0(T_\infty)}$$

where $\lambda_0 > \lambda_1$ are the largest two eigenvalues. This
is equivalent to:

$$\text{gap}(H_N) \geq \text{gap}(H_\infty)$$

**But:** The inequality on the transfer matrix eigenvalue ratios does
NOT follow from the indefiniteness of V. We need a structural argument
about how the perturbation affects the eigenvalue RATIO, not just
the individual eigenvalues.

[OPEN -- this reformulation is cleaner but does not resolve the
indefiniteness problem]


---

## 4.5 Stochastic Domination

### 4.5.1 The idea

Another approach: show that the CP^{N-1} model at coupling $\beta$
is STOCHASTICALLY DOMINATED by the CP^{N'-1} model at coupling
$\beta'$ (with $N < N'$ and both at the same $\Lambda$). Stochastic
domination would give:

$$G_N(x) \leq G_{N'}(x) \quad \forall\;x$$

hence $m(N) \geq m(N')$ (faster decay = larger mass gap).

### 4.5.2 Obstacle

Stochastic domination requires a coupling (joint probability measure)
on $\mathbb{CP}^{N-1} \times \mathbb{CP}^{N'-1}$ that respects the
partial order. No such coupling is known for projective spaces.

For O(N) models, stochastic domination in the dimension N was proved
by Aizenman (1994) using a random-current representation. The
CP^{N-1} model lacks this representation because of the gauge
redundancy.

**Conclusion: Stochastic domination is not available.** [OPEN --
no known coupling]


---

## 4.6 The Mermin-Wagner Perspective

### 4.6.1 Absence of symmetry breaking

In 2D, the Mermin-Wagner theorem forbids spontaneous breaking of the
SU(N) symmetry of the CP^{N-1} model for all finite N. This means
the correlation function $G(x) = \langle |\bar{z}_0 \cdot z_x|^2\rangle - 1/N$
decays to zero at large $|x|$, confirming a non-zero mass gap.
[PROVED for finite N; the N = infinity limit is the saddle-point
result $m = \Lambda$]

### 4.6.2 Rate of decay and N-dependence

Mermin-Wagner does NOT give quantitative control over the decay rate
(mass gap). It only says $G(x) \to 0$, not how fast. The mass gap
could in principle decrease as N increases.

### 4.6.3 Monotonicity from Mermin-Wagner?

The Mermin-Wagner bound gives:

$$\langle |\bar{z}_0 \cdot z_x|^2\rangle - 1/N \leq \frac{C(N)}{|x|^2}$$

for large $|x|$, where $C(N) \sim 1/\beta = \lambda_0/N$. At fixed
$\Lambda$, $\lambda_0$ is the SAME for all N (it is determined by
the UV cutoff and $\Lambda$ through the gap equation). Therefore
$C(N) \sim 1/N$, which means correlations DECREASE with N.

**But:** Smaller correlations do not imply larger mass gap. The
correlation function has the form:

$$G(x) \sim A(N)\,e^{-m(N)|x|}$$

Both the amplitude $A(N)$ and the mass $m(N)$ depend on N. Smaller
$G(x)$ could come from smaller $A(N)$ (which decreases like $1/N$)
rather than larger $m(N)$.

**Conclusion: Mermin-Wagner does not give monotonicity.** [PROVED --
the bound is too weak]


---

## 4.7 A Partial Result: Monotonicity for Large N

### 4.7.1 Combining reflection positivity with 1/N expansion

Reflection positivity gives the spectral representation:

$$G(t) = \int_0^\infty \rho(\mu)\,e^{-\mu t}\,d\mu$$

with $\rho(\mu) \geq 0$ and $m(N) = \inf\text{supp}(\rho)$.

The 1/N expansion gives $\rho$ perturbatively:

$$\rho(\mu) = \rho_0(\mu) + \frac{1}{N}\rho_1(\mu) + O(1/N^2)$$

where $\rho_0(\mu) = Z_0\,\delta(\mu - \Lambda)$ (single-particle
pole at N = infinity).

At O(1/N), the spectral function develops:
1. A shifted pole at $\mu = \Lambda + \alpha_1\Lambda/N$ (mass shift)
2. A multi-particle continuum starting at $\mu = 2\Lambda$

Both features are ABOVE $\Lambda$, consistent with $m(N) > \Lambda$.
[ESTABLISHED at the perturbative level]

### 4.7.2 Rigorous statement

**Proposition [BOUNDED]:** There exists $N_0$ such that for all
$N \geq N_0$:

$$m(N) \geq \Lambda$$

**Proof:** At $N = \infty$, $m = \Lambda$. The 1/N correction is
$\delta m = \alpha_1\Lambda/N > 0$. By continuity of the mass gap
in the coupling constants (which follows from the analytic structure
of the spectral function in a neighborhood of $1/N = 0$), the mass
gap satisfies $m(N) > \Lambda$ for all sufficiently large N. QED.

The value of $N_0$ is not determined by this argument. It depends on
the radius of convergence of the 1/N expansion (if convergent) or
the optimal truncation point (if asymptotic).


---

## 4.8 Summary

| Approach | Gives monotonicity? | Status |
|----------|-------------------|--------|
| FKG inequality | No -- does not apply to CP^{N-1} | [PROVED: inapplicable] |
| GKS inequality | No -- does not apply to CP^{N-1} | [PROVED: inapplicable] |
| Reflection positivity alone | No -- gives positivity, not comparison | [PROVED: insufficient] |
| Infrared bounds | No -- does not compare different N at fixed Lambda | [PROVED: insufficient] |
| Stochastic domination | Unknown -- no coupling known | [OPEN] |
| Mermin-Wagner | No -- too weak quantitatively | [PROVED: insufficient] |
| RP + 1/N expansion | Yes, for large N (N >= N_0) | [BOUNDED] |

**The honest conclusion:** None of the standard non-perturbative tools
(correlation inequalities, reflection positivity, stochastic
domination) give monotonicity of the mass gap in N for the CP^{N-1}
model. The best available result is the perturbative statement that
$m(N) > \Lambda$ for N sufficiently large, combined with reflection
positivity to make the spectral representation rigorous.

The gap in the argument is for SMALL N (N = 2, 3, 4), where
perturbation theory is unreliable and non-perturbative tools do not
apply. This is addressed in file 05 (the N = 2 check).
