# Path A: Multi-Scale Renormalization Group

## 03 -- How CP^{N-1} Topology Constrains Each RG Step


---

## I. The Topological Data at Each Scale

### I.1 Persistence of the topological decomposition

At the initial scale $a_0$, the KK-enhanced lattice theory has a
decomposition into topological sectors labeled by $k_x = c_2(A_x)$
at each site $x$. The cluster expansion (Section 25) proves confinement
in the $k = 0$ sector, and the Bogomolny bound suppresses $k \neq 0$.

**Claim [ARGUED]:** After $n$ RG steps (from $a_0$ to $a_n = a_0/2^n$),
the effective theory at scale $a_n$ still admits a decomposition into
topological sectors.

*Argument.* The topological charge $c_2(A_x)$ is an integer-valued
topological invariant. It is defined for connections on
$\mathbb{CP}^{N-1}$, which is the SAME manifold at every scale (the
RG acts on the 4D lattice, not on the internal space). The block
averaging of internal connections (Section 01, IV.2) preserves the
total charge within each block. Therefore the sector decomposition
persists.

**Subtlety:** What changes is the WEIGHT of each sector. At scale
$a_0$, the non-trivial sectors are suppressed by $e^{-8\pi^2/g_0^2}$
(Bogomolny bound with the bare coupling $g_0$). At scale $a_n$, the
effective coupling is $g_n^2 = 1/(b_0 L_n)$, and the suppression
becomes $e^{-8\pi^2/g_n^2} = e^{-8\pi^2 b_0 L_n}$.

Since $L_n = 2n \ln 2 + L_0$ grows with $n$: the suppression of
non-trivial sectors INCREASES with the RG step. The deeper we go into
the UV, the more suppressed the instantons are.

$$\text{Instanton weight at scale } a_n:
  \quad w_n = e^{-8\pi^2/g_n^2}
  = e^{-8\pi^2 b_0 L_n}
  \sim (a_n \Lambda)^{8\pi^2 b_0}$$

For SU(3): $8\pi^2 b_0 = 11/6$, so $w_n \sim (a_n \Lambda)^{11/6}$.
As $a_n \to 0$: $w_n \to 0$ (instantons are exponentially rare at
weak coupling). [PROVED -- standard instanton calculus.]

### I.2 The screening obstruction at each scale

The screening obstruction (Theorem B.1) says: in the $k = 0$ sector
of the theory at scale $a$, the Wilson loop satisfies an area law.
The deconfining alternative (perimeter law) requires $k \neq 0$, which
costs energy $\geq 8\pi^2/g^2$.

**At each RG scale $a_k$, this gives two facts:**

(F1) **The $k = 0$ sector confines** (screening obstruction):
$\sigma_0^{(k)} > 0$ where $\sigma_0^{(k)}$ is the string tension in
the $k = 0$ sector of the effective theory at scale $a_k$.

(F2) **The $k \neq 0$ correction is small** (Bogomolny):
$|\sigma^{(k)} - \sigma_0^{(k)}| \leq C \cdot e^{-8\pi^2/g_k^2}$.

Combining: $\sigma^{(k)} > 0$ for all $k$ large enough that
$C e^{-8\pi^2/g_k^2} < \sigma_0^{(k)}$.

**Status [ARGUED]:** (F1) is the content of the screening obstruction,
which is proved at the initial scale. Its persistence at every scale
requires that the effective theory still has the $\mathbb{CP}^{N-1}$
structure. (F2) is a direct application of the Bogomolny bound.


---

## II. Three Topological Mechanisms

The $\mathbb{CP}^{N-1}$ topology constrains the RG flow through three
distinct mechanisms.

### II.1 Mechanism 1: The energy barrier

**Statement [PROVED]:** The energy required to create a non-trivial
topological configuration ($k = 1$) at scale $a_k$ is:

$$E_{\text{barrier}}(a_k) = \frac{8\pi^2}{g_k^2}
  = 8\pi^2 b_0 L_k$$

This grows with $k$ (because $g_k^2 \to 0$). At each RG step, the
barrier INCREASES.

**Consequence:** The probability of the RG step creating a non-trivial
topological excitation is bounded by:

$$P(\text{create } k \neq 0 \text{ at step } n)
  \leq e^{-E_{\text{barrier}}(a_n)}
  = (a_n \Lambda)^{8\pi^2 b_0}$$

This probability vanishes as $n \to \infty$. The RG flow is trapped
in the $k = 0$ sector with increasing certainty.

### II.2 Mechanism 2: The flux tube topology

**Statement [ARGUED]:** In the $k = 0$ sector, the confining flux tube
between a quark-antiquark pair wraps the non-contractible cycle
$\mathbb{CP}^1 \subset \mathbb{CP}^{N-1}$. This wrapping is a
topological invariant of the flux tube configuration, separate from the
$c_2$ charge.

The RG step integrates out short-wavelength fluctuations of the flux
tube but does not change its topological wrapping. Therefore:

- If the flux tube exists at scale $a_k$ (wrapping $\mathbb{CP}^1$),
  it exists at scale $a_{k+1}$ (still wrapping $\mathbb{CP}^1$).
- The string tension may change (the tube fluctuates), but the tube
  cannot disappear (the wrapping is topologically protected).

**The flux tube is a topological soliton.** Its existence is guaranteed
by $\pi_2(\mathbb{CP}^{N-1}) = \mathbb{Z}$, and its stability follows
from the non-contractibility of the wrapping cycle.

**Status:** This argument is physically compelling but not yet formalized.
The difficulty is defining what "flux tube wrapping" means in the
lattice theory at each scale. In the continuum, it is well-defined
(the flux tube is a codimension-2 object with a winding number around
$\mathbb{CP}^1$). On the lattice, the winding number is defined only
modulo lattice artifacts.

### II.3 Mechanism 3: The spectral gap on CP^{N-1}

**Statement [PROVED]:** The Weitzenb\"ock spectral gap
$\mu_1 \geq 6/r_3^2$ holds on $\mathbb{CP}^{N-1}$ independently of
any lattice or coupling.

At each RG scale $a_k$, the internal fluctuations (in the $k = 0$
sector) are controlled by this spectral gap. The fluctuation mass is:

$$m_{\text{fluct}}(a_k) = \frac{\sqrt{\mu_1}}{g_k}
  = \frac{\sqrt{6}}{r_3 g_k}$$

Since $g_k \to 0$ as $k \to \infty$: **the fluctuation mass INCREASES
with the RG step.** The internal modes become MORE massive, not less.

This might seem contradictory to the statement that "KK modes become
light at small $a$." The resolution: the KK modes have physical mass
$m_1 = 2\sqrt{3}/r_3$ (independent of $a$ and $g$). What changes is
their mass IN LATTICE UNITS: $m_1 a_k \to 0$ as $a_k \to 0$. The
modes are not becoming lighter; the lattice is becoming finer.

The fluctuation mass $m_{\text{fluct}} = \sqrt{6}/(r_3 g_k) \sim
\sqrt{6b_0 L_k}/r_3$ grows without bound. In lattice units:
$m_{\text{fluct}} \cdot a_k = \sqrt{6b_0 L_k} \cdot a_k/r_3$,
which $\to 0$ for $a_k \ll r_3$ despite $m_{\text{fluct}} \to \infty$.

**The spectral gap controls the fluctuations in the internal space
at every scale, but it does NOT prevent the lattice from resolving
the internal geometry.** [PROVED for the spectral gap; ARGUED for its
implications.]


---

## III. Quantitative Bounds from the Topology

### III.1 The bound on $\delta\sigma$ from Mechanism 1

From Section 02, the one-step correction to the string tension is:

$$\delta\sigma_k = -C_1 g_k^2 \sigma_k + O(g_k^4 \sigma_k)
  + O(e^{-c/g_k^2} \sigma_k)$$

The topological constraint (Mechanism 1) adds a non-perturbative
correction. The $k = 0$ sector confines with string tension
$\sigma_0^{(k)}$, and the full string tension includes contributions
from the $k \neq 0$ sectors:

$$\sigma_k = \sigma_0^{(k)}
  \left(1 + O(e^{-8\pi^2/g_k^2})\right)$$

After one RG step:

$$\sigma_{k+1} = \sigma_0^{(k+1)}
  \left(1 + O(e^{-8\pi^2/g_{k+1}^2})\right)$$

The question is the relation between $\sigma_0^{(k)}$ and
$\sigma_0^{(k+1)}$.

### III.2 A lower bound from the screening obstruction

**Attempt 1: Direct application.**

The screening obstruction says $\sigma_0^{(k)} > 0$, but gives no
quantitative lower bound. It tells us the string tension is nonzero,
not how small it can be.

**Attempt 2: Connecting to the Weitzenb\"ock gap.**

The cluster expansion (Section 25) gives a QUANTITATIVE bound on
$\sigma_0$ when it converges. At scale $a_k$ with $a_k \gg r_3$:

$$\sigma_0^{(k)} \geq \alpha_k > 0$$

where $\alpha_k$ is the Koteck\'y--Preiss constant. Explicitly:

$$\alpha_k \sim e^{-C \beta_k}$$

for some $C > 0$. On the AF trajectory: $\beta_k \sim 2N b_0 L_k$, so:

$$\alpha_k \sim e^{-C' L_k} \sim (a_k \Lambda)^{C'}$$

This bound is non-trivial only for $a_k$ not too small (it vanishes as
$a_k \to 0$). So the cluster expansion bound on $\sigma_0$ does not
help with the continuum limit --- it gives a lower bound that itself
vanishes.

**Attempt 3: The Bogomolny bound as a floor.**

The Bogomolny bound gives a lower bound on the ACTION, not on the
string tension. The string tension is extracted from the Wilson loop,
which is a DIFFERENT observable. The connection is indirect:

- The Bogomolny bound says non-trivial configurations have action
  $\geq 8\pi^2/g^2$.
- The screening obstruction says deconfinement requires non-trivial
  configurations.
- Together: deconfinement requires action $\geq 8\pi^2/g^2$.
- But the converse (action $\geq 8\pi^2/g^2$ implies confinement with
  $\sigma \geq$ some bound) does NOT follow directly.

**The Bogomolny bound provides a qualitative obstruction to
deconfinement, not a quantitative lower bound on the string tension.**
[PROVED -- the obstruction is rigorous; the quantitative gap is open.]

### III.3 A sharper attempt: the 't Hooft loop

Consider the dual observable: the 't Hooft loop $T(C)$, which creates
a magnetic flux tube. In a confining theory, the 't Hooft loop satisfies
a PERIMETER law; in a deconfined theory, it satisfies an AREA law
('t Hooft 1978).

The product $W(C) T(C')$ satisfies a commutation relation
(the 't Hooft algebra):

$$W(C) T(C') = e^{2\pi i \, \text{link}(C, C')/N} \, T(C') W(C)$$

where $\text{link}(C, C')$ is the linking number.

In the $k = 0$ sector of the $\mathbb{CP}^{N-1}$ theory, the magnetic
flux is quantized in units of $2\pi/N$ on $\mathbb{CP}^1$. The
't Hooft loop creating one unit of magnetic flux has:

$$\langle T(C) \rangle_{k=0} \sim e^{-\mu |\partial C|}$$

where $\mu$ is the magnetic mass and $|\partial C|$ is the perimeter.
The perimeter law for $T$ is EQUIVALENT to the area law for $W$ (by
the 't Hooft algebra and cluster decomposition).

**Could we bound $\mu$ (the magnetic mass) using the topology?**

The magnetic flux on $\mathbb{CP}^1$ has a topological quantization:
$\Phi_{\text{mag}} = 2\pi k_m / N$ with $k_m \in \mathbb{Z}$.
The energy of a magnetic monopole (end of a magnetic flux tube) is:

$$E_{\text{mono}} \geq \frac{4\pi}{g^2 N} \cdot k_m$$

by the Bogomolny bound for the DUAL (magnetic) theory. The magnetic
mass $\mu$ is bounded below by $E_{\text{mono}}$:

$$\mu \geq \frac{4\pi}{g^2 N}$$

This gives a bound on the 't Hooft loop perimeter coefficient, which
in turn (by the 't Hooft algebra) constrains the Wilson loop area
coefficient:

$$\sigma \geq \frac{C}{(\mu + \sigma)^{d-2}} \cdot e^{-\mu R}$$

... but this is a self-referential inequality that does not close.

**Status [OPEN]:** The 't Hooft loop approach gives qualitative
constraints but does not produce a closed quantitative bound on
$\sigma$.


---

## IV. The Deformation Argument

### IV.1 A different strategy

Instead of bounding $\sigma_k$ from below at each step, consider
bounding the CHANGE $|\sigma_{k+1} - \sigma_k|$.

If we can show that the total change is finite:

$$\sum_{k=0}^{\infty} |\sigma_{k+1} - \sigma_k| < \infty$$

then $\sigma_k$ converges (it is a Cauchy sequence), and since
$\sigma_0 > 0$, the limit is nonzero if the total change is less than
$\sigma_0$.

From Section 02, the one-step change is:

$$|\sigma_{k+1} - \sigma_k|
  \leq C_1 g_k^2 \sigma_k + O(g_k^4 \sigma_k) + O(a_k^2 \Lambda^4)$$

The difficulty: this involves $\sigma_k$ on the right side. Without an
a priori lower bound on $\sigma_k$, we cannot bound the sum.

### IV.2 The bootstrap attempt

Assume $\sigma_k \leq M$ for all $k$ (an UPPER bound). Then:

$$|\sigma_{k+1} - \sigma_k| \leq C_1 g_k^2 M + O(a_k^2 \Lambda^4)$$

$$\sum_{k=0}^{\infty} |\sigma_{k+1} - \sigma_k|
  \leq C_1 M \sum_k g_k^2 + O(\Lambda^4) \sum_k a_k^2$$

The second sum converges: $\sum_k a_k^2 = a_0^2 \sum_k 4^{-k}
= 4a_0^2/3$. But the first sum diverges: $\sum_k g_k^2
= \sum 1/\ln k = \infty$.

**Even with an upper bound on $\sigma_k$, the total variation
diverges.** [PROVED -- the sum is explicitly divergent.]

### IV.3 What if $C_1$ is not constant?

The coefficient $C_1$ in the one-step formula is the one-loop RG
coefficient for the string tension. In general, $C_1$ depends on the
effective action at scale $k$ (not just on the coupling $g_k^2$).

**Possibility:** At each scale, the $\mathbb{CP}^{N-1}$ topology
modifies $C_1$. Specifically, the screening obstruction could cause
$C_1$ to be SMALLER than the perturbative value (because the topology
prevents the full perturbative reduction of $\sigma$).

If $C_1^{(k)} = C_1 g_k^{2\alpha}$ for some $\alpha > 0$, then:

$$\sum_k C_1^{(k)} g_k^2 = C_1 \sum_k g_k^{2+2\alpha}
  \sim \sum_k \frac{1}{k^{1+\alpha} (\ln 2)^{1+\alpha}}$$

This CONVERGES for $\alpha > 0$ (it is a p-series with $p = 1+\alpha > 1$).

**If the one-loop RG coefficient for the string tension decreases
faster than $g^2$ (i.e., the perturbative reduction is a higher-order
effect), then the product formula converges.** [OPEN -- this would
require showing that the string tension is protected by a
non-renormalization theorem at each scale.]


---

## V. The Topology-Enhanced RG Step

### V.1 What the topology actually does

Let me reconsider the structure of the one-step RG transformation in
the $k = 0$ sector.

The RG integrates out modes at scale $\sim 1/a_k$. In the $k = 0$
sector, the integrated-out modes are:
- 4D gauge field fluctuations with momenta $\pi/(2a_k) < |p| < \pi/a_k$
- Internal fluctuations around the flat connection on $\mathbb{CP}^{N-1}$

The 4D fluctuations reduce $\sigma$ (they screen the chromoelectric
flux). The internal fluctuations, however, are GAPPED (mass
$m_{\text{fluct}} \geq \sqrt{6}/(r_3 g_k)$) and contribute
differently.

In the cluster expansion framework, the internal fluctuations provide
a suppression factor $e^{-m_1 a_k}$ per bond. After one RG step, the
effective lattice spacing doubles, but the suppression per effective
bond changes:

$$e^{-m_1 (2a_k)} = e^{-2 m_1 a_k} = \left(e^{-m_1 a_k}\right)^2$$

The suppression INCREASES (each effective bond contains two fine bonds,
and the suppression factors multiply). This is specific to the
$k = 0$ sector.

**Key point [ARGUED]:** In the $k = 0$ sector, the RG step IMPROVES
the cluster expansion convergence. Each coarsening step doubles the
effective lattice spacing while quadrupling the bond suppression (in
the exponent). The effective cluster expansion parameter is:

$$\epsilon_k = e^{2\beta_k} \cdot e^{-m_1 a_k / 6}$$

After one RG step:

$$\epsilon_{k+1} = e^{2\beta_{k+1}} \cdot e^{-m_1 a_{k+1} / 6}
  = e^{2\beta_{k+1}} \cdot e^{-m_1 a_k / 12}$$

Using $\beta_{k+1} \approx \beta_k + 2N b_0 \ln 2$ (one-loop running):

$$\epsilon_{k+1} = e^{2(\beta_k + 2Nb_0 \ln 2)} \cdot e^{-m_1 a_k/12}
  = 4^{2Nb_0} \cdot e^{2\beta_k} \cdot e^{-m_1 a_k / 12}$$

For the cluster expansion to converge, we need $\epsilon_k < 1$, i.e.,
$m_1 a_k / 6 > 2\beta_k$. This is the condition from Section 25, and
it fails when $a_k$ drops below $r_3$.

### V.2 The crossover: what happens when $a_k \sim r_3$

At the critical step $k = k_*$ where $a_{k_*} \sim r_3$:
- The cluster expansion parameter $\epsilon_{k_*} \sim 1$
- The KK modes have $m_1 a_{k_*} \sim 1$
- The theory transitions from "4D with heavy spectators" to
  "higher-dimensional"

After this point ($k > k_*$), the cluster expansion based on
KK mode suppression no longer applies. We need a different
argument for the string tension.

### V.3 The deep UV: $a_k \ll r_3$

For $k \gg k_*$, the lattice spacing resolves the internal
$\mathbb{CP}^{N-1}$. The theory is effectively $(4 + 2N - 2)$-dimensional
with a lattice in all directions.

In this regime, the theory has TWO types of confinement mechanisms:
1. The 4D confinement from the $\mathbb{CP}^{N-1}$ topology (which
   we proved at larger $a$)
2. The asymptotic freedom of the $(4+2N-2)$-dimensional theory
   (but higher-dimensional YM is NOT asymptotically free!)

**Problem [OPEN]:** The higher-dimensional theory is NOT
asymptotically free (for $D > 4$, the YM coupling is irrelevant in
the UV). The notion of a continuum limit does not apply in the same
way. The theory at $a \ll r_3$ is a fundamentally different beast
from the theory at $a \gg r_3$.

This is the core difficulty of the multi-scale approach: the nature
of the theory changes qualitatively at $a \sim r_3$.


---

## VI. Summary: What the Topology Provides

| Mechanism | Quantitative bound | Scale dependence | Status |
|-----------|-------------------|------------------|--------|
| Energy barrier (Bogomolny) | $E \geq 8\pi^2/g_k^2$ | Increases with $k$ | PROVED |
| Flux tube topology ($\pi_2$) | $\sigma > 0$ (qualitative) | Scale-independent | ARGUED |
| Spectral gap (Weitzenb\"ock) | $\mu_1 \geq 6/r_3^2$ | Scale-independent | PROVED |
| Sector decomposition | $\sigma \geq \sigma_0(1 - Ce^{-8\pi^2/g^2})$ | Improves with $k$ | ARGUED |

**What the topology gives:** A qualitative guarantee that $\sigma_k > 0$
at each scale (the screening obstruction), and increasingly strong
suppression of non-trivial sectors.

**What the topology does NOT give:** A quantitative lower bound on
$\sigma_k$ that is uniform in $k$. The screening obstruction says
$\sigma > 0$ but not $\sigma > \epsilon$ for any specific $\epsilon$.

**The gap between qualitative and quantitative:** This is the essence
of the continuum limit problem. We know the theory confines at every
scale, but we cannot prove the string tension stays bounded away from
zero as $a \to 0$.
