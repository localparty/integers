# Path A: Multi-Scale Renormalization Group

## 01 -- Framework and Setup


---

## I. The Problem, Precisely Stated

We have proved (Sections 21--25) that the SU(N) lattice Yang--Mills
theory has string tension $\sigma(\beta) > 0$ and mass gap
$\Delta(\beta) > 0$ for all couplings $\beta < a/(2\sqrt{3}\,r_3)$,
where $r_3$ is the $\mathbb{CP}^{N-1}$ radius. On the asymptotic
freedom (AF) trajectory $\beta(a) = 2Nb_0 \ln(1/(a\Lambda))$, this
covers all lattice spacings $a > a_{\text{cross}} \sim 10^{-29}$ m.

**The open problem:** Does the physical string tension

$$\sigma_{\text{phys}}(a) = \frac{\hat{\sigma}(\beta(a))}{a^2}$$

converge to a positive limit as $a \to 0$?

The cluster expansion (Section 25) fails for $a \lesssim r_3$ because
the KK modes become light ($m_1 a < 1$). The decoupling argument
(Section 31) was retracted as circular. We need a new method.

**The multi-scale idea:** Instead of taking $a \to 0$ in one leap,
descend scale by scale:

$$a_0 \;\to\; a_0/L \;\to\; a_0/L^2 \;\to\; \cdots
  \;\to\; a_0/L^n \;\to\; \cdots$$

At each step, integrate out fluctuations at one scale and show that the
resulting effective theory still confines. The CP$^{N-1}$ topology
constrains each step.


---

## II. The Lattice Scales

Fix a blocking factor $L \geq 2$ (we use $L = 2$ for concreteness).
Define the sequence of lattice spacings:

$$a_k = a_0 / 2^k, \quad k = 0, 1, 2, \ldots$$

where $a_0$ is the initial (coarsest) spacing, chosen so that
$a_0 \gg r_3$ and the cluster expansion (Section 25) applies at
$a_0$.

On the AF trajectory, each $a_k$ has a corresponding bare coupling:

$$g^2(a_k) = \frac{1}{b_0 \ln(1/(a_k^2 \Lambda^2))}
  = \frac{1}{b_0 \ln(2^{2k}/(a_0^2 \Lambda^2))}
  = \frac{1}{b_0 (2k \ln 2 + \ln(1/(a_0^2 \Lambda^2)))}$$

where $b_0 = 11N/(48\pi^2)$ is the one-loop beta function coefficient.

Let $L_k = 2k \ln 2 + \ln(1/(a_0^2 \Lambda^2))$. Then:

$$g^2(a_k) = \frac{1}{b_0 L_k}$$

Key properties:
- $g^2(a_k) \to 0$ as $k \to \infty$ (asymptotic freedom)
- $g^2(a_k) \sim \frac{1}{2 b_0 k \ln 2}$ for large $k$
- $\beta(a_k) = 2N/g^2(a_k) = 2N b_0 L_k \to \infty$

**Three regimes** along the descent:

| Regime | Condition | KK modes | Cluster expansion |
|--------|-----------|----------|-------------------|
| A: $a_k \gg r_3$ | $k < k_*$ | Ultra-heavy ($m_1 a_k \gg 1$) | Converges |
| B: $a_k \sim r_3$ | $k \approx k_*$ | Threshold ($m_1 a_k \sim 1$) | Marginal |
| C: $a_k \ll r_3$ | $k > k_*$ | Light ($m_1 a_k \ll 1$) | Fails |

where $k_* = \log_2(a_0/r_3) \sim \log_2(10^{15}) \approx 50$.

**The challenge is Regime C.** After about 50 blocking steps, the
lattice spacing drops below $r_3$ and the KK modes become light.
The cluster expansion loses control, and we need a replacement.


---

## III. The Block-Spin RG Transformation

### III.1 Definition

The block-spin (or Kadanoff) transformation maps a lattice theory at
spacing $a$ to an effective theory at spacing $2a$. For gauge theories,
the standard construction is:

**Blocking map.** Partition the fine lattice $\Lambda_a$ into
$2^4$-site hypercubic blocks $B_x$, one per site $x$ of the coarse
lattice $\Lambda_{2a}$. Define the block link variable:

$$V_{\langle x,y \rangle} = \mathcal{N} \int \prod_{\text{fine links in path}}
  dU_\ell \; \delta_{\text{SU}(N)}\!\left(V - P(U)_{\langle x,y \rangle}\right)
  \prod_\ell e^{-\beta s_\ell}$$

where $P(U)_{\langle x,y \rangle}$ is the ordered product of fine link
variables along a chosen path from block center $x$ to block center $y$,
and $\mathcal{N}$ is the normalization.

In practice, one uses a smooth blocking kernel (Balaban 1985):

$$T_\kappa(V, U) = \exp\left(\frac{\kappa}{g^2} \text{Re}\,\text{Tr}
  \left[V \cdot P(U)^\dagger\right]\right)$$

with $\kappa > 0$ a tuning parameter. The effective action at scale
$2a$ is:

$$e^{-S_{\text{eff}}(V)} = \int \prod_\ell dU_\ell \;
  e^{-S(U)} \prod_{\langle xy \rangle} T_\kappa(V_{\langle xy \rangle}, U)$$

### III.2 What the RG step preserves

By construction, the block-spin transformation preserves:

**(a) Gauge invariance.** If $S(U)$ is gauge-invariant, so is
$S_{\text{eff}}(V)$. [PROVED -- standard, follows from the
gauge-equivariance of the blocking kernel.]

**(b) Reflection positivity.** Under suitable conditions on the
blocking kernel, the effective action inherits reflection positivity
from the fine-lattice action. [PROVED -- Balaban 1985, Theorem 2.1;
requires the kernel to respect the lattice symmetries.]

**(c) Partition function.** $Z_{\text{eff}} = Z_{\text{fine}}$ (the
partition function is invariant under RG). Therefore $\ln Z$ and the
free energy density are preserved. [PROVED -- by construction.]

**(d) Long-distance correlators.** For observables $\mathcal{O}$ that
depend only on coarse-lattice variables:
$\langle \mathcal{O} \rangle_{\text{eff}} =
\langle \mathcal{O} \rangle_{\text{fine}}$. [PROVED -- by
construction.]

### III.3 What the RG step does NOT automatically preserve

**(e) String tension.** The Wilson loop $W_R(C)$ on the coarse lattice
is NOT the same observable as on the fine lattice (the minimal area
changes by a factor of 4). The string tension transforms as:

$$\hat{\sigma}_{\text{coarse}} = 4 \hat{\sigma}_{\text{fine}}
  + \delta\sigma$$

where $\delta\sigma$ is the correction from integrating out the
fine-scale fluctuations. The physical string tension
$\sigma_{\text{phys}} = \hat{\sigma}/a^2$ transforms as:

$$\sigma_{\text{phys}}^{\text{coarse}}
  = \frac{\hat{\sigma}_{\text{coarse}}}{(2a)^2}
  = \frac{4\hat{\sigma}_{\text{fine}} + \delta\sigma}{4a^2}
  = \sigma_{\text{phys}}^{\text{fine}} + \frac{\delta\sigma}{4a^2}$$

The question is whether $\delta\sigma / (4a^2)$ is controlled.

**(f) Mass gap.** Similarly, $\Delta_{\text{phys}}$ changes by a
correction from the integrated-out modes. The physical mass gap
transforms as:

$$\Delta_{\text{phys}}^{\text{coarse}}
  = \Delta_{\text{phys}}^{\text{fine}} + \delta\Delta$$

where $\delta\Delta$ depends on the details of the fluctuations.


---

## IV. The KK-Enhanced Block-Spin

### IV.1 Including the CP^{N-1} degrees of freedom

In the KK-enhanced theory, each lattice site carries a
$\mathbb{CP}^{N-1}$ connection $A_x$. The block-spin transformation
must also coarsen the internal degrees of freedom.

**Internal blocking.** For each block $B_x$, define the block internal
connection as:

$$\bar{A}_x = \text{argmin}_{A \in \mathcal{A}}
  \sum_{y \in B_x} d^2(A, A_y)$$

where $d$ is the distance in the space of connections on
$\mathbb{CP}^{N-1}$. In the $k = 0$ sector, all $A_y$ are close to
the flat connection, so $\bar{A}_x \approx \frac{1}{|B_x|}\sum_y A_y$
(the average).

**The effective internal action.** After integrating out the
fine-lattice fluctuations around $\bar{A}_x$:

$$S_{\text{int}}^{\text{eff}}[\bar{A}]
  = S_{\text{int}}[\bar{A}]
  + \frac{1}{2} \text{Tr}\ln\left(\text{Hess}\,S_{\text{int}}|_{\bar{A}}\right)
  + O(g^4)$$

The Hessian is the quadratic fluctuation operator around $\bar{A}$,
which (in the $k = 0$ sector) has a spectral gap $\geq \mu_1 / g^2$
(Theorem I.1 of Section 25).

### IV.2 Topological sectors under blocking

**Key observation [PROVED]:** The topological charge $k_x = c_2(A_x)$
at each fine-lattice site is an integer. Blocking (averaging) within a
block $B_x$ does not change the total topological charge:

$$k_{\bar{x}} = \sum_{y \in B_x} k_y \quad \in \mathbb{Z}$$

In the $k = 0$ sector: all $k_y = 0$, so all $k_{\bar{x}} = 0$.
**The block-spin transformation preserves the topological sector.**

This is the first structural input from the $\mathbb{CP}^{N-1}$
topology: the RG flow cannot leave the $k = 0$ sector.

### IV.3 The screening obstruction survives blocking

**Claim [ARGUED]:** The screening obstruction (Theorem B.1) holds at
every scale $a_k$.

*Argument.* The screening obstruction says: deconfining the theory
(changing the Wilson loop from area law to perimeter law) requires
non-trivial topology ($k \neq 0$) on $\mathbb{CP}^{N-1}$. The
block-spin transformation integrates out modes at scale $\sim 1/a_k$
but does NOT change the topology of $\mathbb{CP}^{N-1}$ (the internal
space is fixed; only the 4D lattice is coarsened). Therefore the
obstruction persists at each coarser scale.

**Status:** This argument is correct in spirit but not yet a theorem.
Making it rigorous requires showing that the effective action at scale
$a_k$ still has the structure assumed by Theorem B.1 (specifically:
that the effective theory at each scale can be decomposed into
topological sectors, and the screening obstruction applies to the
effective Wilson loop).


---

## V. The Balaban Framework

### V.1 What Balaban proved (1985--1989)

Tadeusz Balaban developed a multi-scale analysis for lattice gauge
theories in a series of papers (Comm. Math. Phys. 95, 98, 99, 109,
116, 119, 122, 128). His program proved:

**(i) UV stability [PROVED].** The effective actions $S_k$ generated
by the multi-scale RG are bounded: $\|S_k\| \leq C_k$ with explicit
constants. The bounds are uniform in the total lattice volume.

**(ii) Gauge-invariant norms [PROVED].** He developed a system of
gauge-invariant norms (the "Balaban norms") adapted to the multi-scale
structure. These norms control the fluctuation field at each scale
without breaking gauge invariance.

**(iii) Small-field/large-field decomposition [PROVED].** At each
scale, the field is split into "small" (perturbative) fluctuations and
"large" (non-perturbative) excitations. The large-field region is
suppressed by a factor $e^{-c/g^2}$ per plaquette.

**(iv) Perturbative renormalizability [PROVED].** In the small-field
region, the RG step is perturbatively controlled: the effective action
at scale $a_{k+1}$ has the form $S_k + \delta S_k$ where $\delta S_k$
is a sum of local counterterms (mass, coupling, wave function
renormalization) plus irrelevant terms bounded by $O(g^4)$.

### V.2 What Balaban did NOT prove

**(v) Confinement.** Balaban's program did not address confinement or
the mass gap. His estimates are about the gauge field fluctuations
(UV stability), not about the long-range order (confinement is IR).

**(vi) Convergence of $\sigma_{\text{phys}}$.** The string tension was
not studied.

**(vii) Non-perturbative control of the RG flow.** The small-field
estimates are perturbative (controlled by $g^2$). The large-field
region is suppressed by $e^{-c/g^2}$, but connecting these to
confinement requires additional input.

### V.3 What we would need from Balaban + CP^{N-1}

The idea is to supplement Balaban's UV estimates with the
$\mathbb{CP}^{N-1}$ topological constraints:

- **Balaban provides:** Control of gauge field fluctuations at each
  scale. The effective action at scale $a_k$ is close to a
  renormalized Wilson action with coupling $g^2(a_k)$.

- **CP$^{N-1}$ provides:** A topological obstruction to deconfinement
  at each scale. The screening obstruction (Theorem B.1) says the
  effective theory at scale $a_k$ confines unless non-trivial topology
  is activated, which costs energy $\geq 8\pi^2/g^2(a_k)$.

- **Together:** The effective theory at scale $a_k$ confines, and the
  RG step to scale $a_{k+1}$ preserves confinement (because the step
  doesn't change the topology).

The gap is making the "together" statement quantitative.


---

## VI. Notation for the Subsequent Sections

We adopt the following notation throughout the Path A exploration:

| Symbol | Meaning |
|--------|---------|
| $a_k = a_0/2^k$ | Lattice spacing at scale $k$ |
| $g_k = g(a_k)$ | Running coupling at scale $k$ |
| $\beta_k = 2N/g_k^2$ | Lattice coupling at scale $k$ |
| $\hat{\sigma}_k$ | String tension in lattice units at scale $k$ |
| $\sigma_k = \hat{\sigma}_k / a_k^2$ | Physical string tension at scale $k$ |
| $\Delta_k = \hat{\Delta}_k / a_k$ | Physical mass gap at scale $k$ |
| $m_1 = 2\sqrt{3}/r_3$ | Lowest KK mass |
| $\mathcal{R}$ | The block-spin RG map |
| $S_k = \mathcal{R}^k[S_0]$ | Effective action after $k$ RG steps |

The goal is to prove: $\sigma_k \to \sigma_\infty > 0$ as $k \to \infty$.


---

## VII. The Structure of the Argument (Preview)

The exploration in the subsequent files follows this plan:

1. **02-block-spin-step.md:** Analyze one RG step $a_k \to a_{k+1}$
   in detail. Derive the transformation law for $\sigma_k$ and identify
   the correction $\delta\sigma_k$.

2. **03-topological-constraint.md:** Show how the $\mathbb{CP}^{N-1}$
   topology constrains $\delta\sigma_k$ at each step. The screening
   obstruction and Bogomolny bound provide a "topological floor" for
   the string tension.

3. **04-convergence-attempt.md:** Try to prove
   $\sigma_k \to \sigma_\infty > 0$ using the bounds from steps 1--2.
   This is where the product estimate
   $\prod(1 - Cg_k^2)$ appears and fails. Attempt improvements.

4. **05-obstacles-and-ideas.md:** Assess what works, what doesn't, and
   propose new approaches.

**Honesty declaration:** I do not expect to prove the continuum limit
in this exploration. The goal is to push the multi-scale RG approach
as far as possible, identify the precise obstacle, and determine
whether it is a technical gap (closable with known methods) or a
conceptual gap (requiring new ideas).
