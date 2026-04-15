# 04. Can the Resurgent Sum Define $\sigma_{\text{phys}}$ Without a Lattice?

This is the core question. Even granting that the trans-series IS
resurgent, does the resurgent sum actually define a quantum field
theory with the right properties? This document examines what a
resurgent definition would give and what it would miss.


---

## I. What "Define" Means

### I.1 The Clay Problem requirements

The Clay Millennium Problem asks for:
1. A quantum Yang--Mills theory on $\mathbb{R}^4$ satisfying the
   Osterwalder--Schrader axioms (OS1)--(OS4)
2. With gauge group $SU(N)$ for any $N \geq 2$
3. With a mass gap $\Delta > 0$

A "definition" of the theory means: a construction that produces
the OS correlation functions
$\{S_n(x_1, \ldots, x_n)\}_{n=0}^{\infty}$ satisfying the axioms.

### I.2 What a trans-series gives

A resurgent trans-series for $\sigma_{\text{phys}}$ gives ONE NUMBER
(the string tension). The Clay Problem requires an INFINITE FAMILY
of correlation functions, each satisfying specific axioms.

So the trans-series for $\sigma$ alone is NOT sufficient. We need
the trans-series for ALL correlation functions simultaneously, and
we need them to satisfy the OS axioms.

### I.3 Upgrading to the full theory

The trans-series approach, if it works, defines the full theory
through the following chain:

(a) **The generating functional** $Z[J]$ has a trans-series in
$g^2$:
$$Z[J] = \sum_{m=0}^{\infty} e^{-mS_I/g^2}
  \sum_n Z_n^{(m)}[J] \, g^{2n}$$

(b) **Each coefficient $Z_n^{(m)}[J]$** is a functional of the
source $J$ that can be computed from Feynman diagrams (sector $m = 0$)
or from fluctuations around the $m$-instanton background
(sector $m \geq 1$).

(c) **The correlation functions** are obtained by functional
differentiation:
$$S_n(x_1, \ldots, x_n) = \frac{\delta^n \ln Z[J]}
  {\delta J(x_1) \cdots \delta J(x_n)}\bigg|_{J=0}$$

(d) **The OS axioms** must be verified for the resulting $S_n$.

This is the standard approach to defining a QFT by its perturbative
expansion. The NEW element is that the perturbative series is
RESUMMED (via the resurgent trans-series) to obtain non-perturbative
correlation functions.

[STATUS: This program is CONJECTURAL. No interacting 4D QFT has
been defined by resurgent resummation of its perturbative expansion.]


---

## II. The OS Axioms from Resurgence

### II.1 OS1: Analyticity (Euclidean covariance)

The Euclidean correlation functions $S_n$ must be distributions
on $(\mathbb{R}^4)^n$ that are:
- Symmetric under permutations
- Translation invariant
- Rotation invariant (Euclidean covariance)

**From resurgence:** Each sector of the trans-series preserves
Euclidean symmetry (the instanton background on
$\mathbb{CP}^{N-1}$ is invariant under the $M^4$ isometries).
The resurgent sum, being a limit of symmetric quantities, is
symmetric.

[STATUS: ARGUED -- Euclidean covariance is straightforward.]

### II.2 OS2: Reflection positivity

This is the HARD axiom. Reflection positivity (Euclidean version
of unitarity) requires:
$$\sum_{j,k} \bar{f}_j f_k \, S_{n_j+n_k}
  (\theta x_1^{(j)}, \ldots, \theta x_{n_j}^{(j)},
   x_1^{(k)}, \ldots, x_{n_k}^{(k)}) \geq 0$$

for all test functions $\{f_j\}$ and all reflection $\theta$
about a hyperplane.

**The problem:** Reflection positivity is NOT preserved by
arbitrary resummation procedures. The Borel sum of a series with
the right positivity properties at each order may NOT be positive.

**What we know:**
- The lattice theory at each finite $a$ satisfies reflection
  positivity (Osterwalder--Seiler 1978). [PROVED]
- The trans-series coefficients at each order satisfy reflection
  positivity (each Feynman diagram preserves it). [ARGUED]
- The resurgent sum is a SPECIFIC resummation (median Borel sum),
  which is NOT the same as the lattice limit.

**The key question:** Does the median Borel sum preserve reflection
positivity?

For CONVERGENT series: yes (the limit of positive quantities is
positive). For the resurgent sum: unknown in general.

**A possible route:** If the resurgent sum AGREES with the lattice
limit (when the lattice limit exists), then it inherits reflection
positivity from the lattice. But this is circular: it assumes the
lattice limit exists, which is what we are trying to avoid.

[STATUS: OPEN. Reflection positivity of the resurgent sum is the
deepest obstruction to the resurgence approach.]

### II.3 OS3: Exponential clustering (mass gap)

The mass gap requires:
$$|S_2(x, y) - S_1(x)S_1(y)| \leq C \, e^{-\Delta |x-y|}$$

**From resurgence:** The trans-series for the two-point function
has the form:
$$S_2(x, y) = \sum_m e^{-mS_I/g^2}
  \sum_n s_{2,n}^{(m)}(|x-y|) \, g^{2n}$$

Each sector has exponential decay (the perturbative sector decays
as $e^{-\Delta_0|x-y|}$ where $\Delta_0$ is the perturbative mass
from the KK tower; the instanton sectors decay even faster).

The resurgent sum of exponentially decaying functions is
exponentially decaying (the exponential bound is preserved by
Borel summation). Therefore:
$$\mathcal{S}[S_2](x,y) \leq C \, e^{-\Delta |x-y|}$$

with $\Delta = \min_m (\Delta_m + m S_I) > 0$.

[STATUS: ARGUED -- the mass gap is the EASIEST axiom to verify
from the trans-series, because exponential decay is preserved by
Borel summation.]

### II.4 OS4: Regularity

Technical axiom on the growth of correlation functions. This is
typically straightforward and follows from the same estimates that
give exponential clustering.

[STATUS: ARGUED -- follows from the same analysis as OS3.]


---

## III. The Reflection Positivity Problem in Detail

Since OS2 is the key obstacle, let me examine it more carefully.

### III.1 The problem statement

We need: for any test function $f$ supported in the half-space
$x_0 > 0$:
$$\langle \theta f, f \rangle = \int S_2(\theta x, y)
  \overline{f(x)} f(y) \, dx \, dy \geq 0$$

where $\theta(x_0, \vec{x}) = (-x_0, \vec{x})$ is time reflection.

### III.2 The perturbative sector

At each order in $g^2$, the perturbative correlator is the
sum of Feynman diagrams. Each diagram is a product of propagators,
and each propagator is reflection positive (the free propagator
$(\Delta + m^2)^{-1}$ is reflection positive for $m > 0$).

The SUM of diagrams at order $g^{2n}$ is reflection positive if
all coefficients are positive. This is NOT generally true: individual
diagrams can have either sign. But the FULL perturbative correlator
at order $g^{2n}$ is a physical quantity and satisfies reflection
positivity. [ARGUED -- this follows from the fact that the lattice
approximation at each order is reflection positive.]

### III.3 The instanton sector

The instanton contribution to $S_2$ involves:
$$S_2^{(1)}(x, y) = \int_{\mathcal{M}_1} d\mu_{\text{inst}}
  \, G^{(1)}(x, y; A_{\text{inst}})$$

where $G^{(1)}$ is the Green's function in the one-instanton
background and $d\mu_{\text{inst}}$ is the instanton measure.

Reflection positivity requires:
$$\int S_2^{(1)}(\theta x, y) \bar{f}(x) f(y) \, dx \, dy \geq 0$$

This is NOT automatic: the instanton background breaks the
Euclidean reflection symmetry (the instanton has a position, and
reflecting the instanton gives an anti-instanton).

The instanton-plus-anti-instanton contribution:
$$S_2^{(1)} + S_2^{(\bar{1})} = \int d\mu_I \, G^{(I)}
  + \int d\mu_{\bar{I}} \, G^{(\bar{I})}$$

After integrating over the instanton position, the SUM is
reflection-invariant. But reflection POSITIVITY requires more
than invariance.

[STATUS: OPEN. Reflection positivity of the instanton contribution
is not proved in general.]

### III.4 The resurgent sum

Even if each sector is individually reflection positive, the
median Borel sum may not be. The issue: the median sum involves
taking the AVERAGE of left and right lateral Borel sums:

$$\mathcal{S}_{\text{med}} = \frac{1}{2}(\mathcal{S}_+
  + \mathcal{S}_-)$$

If $\mathcal{S}_+$ and $\mathcal{S}_-$ are individually
reflection positive (which is not obvious), then their average is
also reflection positive (convex combination). But if they are
NOT individually positive (only their combination is), then
the median sum may or may not be positive.

**A cleaner approach:** Instead of the median sum, use the
REAL Borel sum (the principal value integral):

$$\mathcal{S}_{\text{PV}} = \text{P.V.} \int_0^\infty
  B(t) \, e^{-t/g^2} \, dt$$

The principal value is real (no imaginary ambiguity). But it is
NOT the same as the median sum, and it is not clear that it
defines the "correct" theory.

[STATUS: OPEN. The choice of resummation prescription and its
compatibility with reflection positivity is a fundamental open
problem.]


---

## IV. A Potential Resolution: The Constructive Approach

### IV.1 The idea

Instead of summing the trans-series abstractly, use it to
CONSTRUCT the theory step by step:

1. Start with the lattice theory at spacing $a_0$ (which is
   well-defined and satisfies all OS axioms). [PROVED]

2. Use the resurgent trans-series to compute the CHANGE in
   correlation functions as $a$ decreases from $a_0$ to
   $a_0/2$.

3. Iterate to obtain the theory at $a_0/2^k$ for all $k$.

4. Take $k \to \infty$ to obtain the continuum limit.

This hybrid approach uses the lattice for the DEFINITION (ensuring
all axioms) and the trans-series for the COMPUTATION (controlling
the continuum limit).

### IV.2 Why this helps

The advantage: at each step, the change in coupling is SMALL
(the coupling changes by $O(g^2)$ per RG step). The trans-series
is most reliable for small changes.

The perturbative series for the change
$\delta S_n = S_n(a/2) - S_n(a)$ converges FASTER than the
series for $S_n$ itself (because $\delta S_n$ is a correction,
not the full quantity). The resurgent trans-series for $\delta S_n$
has SMALLER coefficients and converges more rapidly.

[STATUS: ARGUED. This approach combines elements of Path A
(multi-scale RG) and Path B (resurgence). It is not fully
developed.]

### IV.3 The key estimate

At each RG step from $a$ to $a/2$:
$$\sigma(a/2) = \sigma(a) + \delta\sigma(a)$$

The change $\delta\sigma(a)$ has a trans-series:
$$\delta\sigma(a) = \sum_m e^{-mS_I/g^2(a)}
  \sum_n \delta\sigma_n^{(m)} g^{2n}(a)$$

If this trans-series is resurgent (which inherits from the full
theory's resurgence), then $\delta\sigma(a)$ is well-defined.

The RG evolution:
$$\sigma(a_0/2^k) = \sigma(a_0)
  + \sum_{j=0}^{k-1} \delta\sigma(a_0/2^j)$$

Convergence of this sum as $k \to \infty$ requires:
$$\sum_{j=0}^{\infty} |\delta\sigma(a_0/2^j)| < \infty$$

By asymptotic freedom, $g^2(a_0/2^j) \to 0$ as $j \to \infty$.
The leading term of $\delta\sigma$ is perturbative:
$\delta\sigma \sim c g^2(a) \sigma(a)$. Since
$\sum_j g^2(a_0/2^j) = \sum_j 1/(b_0 \ln(2^j/(a_0\Lambda)))
\sim \sum_j 1/(b_0 j \ln 2)$, which DIVERGES (harmonic series).

So the naive estimate fails. But this is the same divergence
encountered in Path A (Section A.5 of the three-paths document).

**The fix (if it exists):** The corrections are not simply
additive. The RG equation is MULTIPLICATIVE:
$$\sigma(a/2) = \sigma(a) \times (1 + c g^2(a) + O(g^4))$$

The product:
$$\frac{\sigma(a_0/2^k)}{\sigma(a_0)}
  = \prod_{j=0}^{k-1} (1 + c g^2(a_0/2^j) + O(g^4))$$

Taking the logarithm:
$$\ln\frac{\sigma(a_0/2^k)}{\sigma(a_0)}
  = \sum_{j=0}^{k-1} \ln(1 + cg^2(a_0/2^j))
  \approx c \sum_{j=0}^{k-1} g^2(a_0/2^j)$$

This sum diverges logarithmically:
$\sum_{j} g^2(a_j) \sim \sum_j 1/(b_0 j \ln 2) \to \infty$.

So $\sigma(a_0/2^k) \to 0$ or $\infty$ depending on the sign of
$c$. For asymptotically free theories, the sign is chosen so that
$\sigma_{\text{phys}} = \sigma(a)/a^2$ remains constant --
but this is EXACTLY the asymptotic scaling hypothesis, which is
what we are trying to prove.

[STATUS: The constructive approach hits the same wall as Path A.
The resurgent trans-series helps compute the corrections at each
step, but it does not close the convergence argument.]


---

## V. What the Resurgent Sum CAN Define

Setting aside the OS axioms for a moment, let us ask: what CAN
the resurgent trans-series define?

### V.1 The formal string tension

$$\sigma_{\text{formal}} = \mathcal{S}_{\text{med}}
  \left[\Lambda^2 \sum_m e^{-mS_I/g^2}
  \sum_n \sigma_n^{(m)} g^{2n}\right]$$

This is a FINITE, POSITIVE NUMBER (if the resurgence conjecture
holds). It is defined purely in the continuum, with no lattice.

**But:** It is a formal quantity. Without the OS axioms, it does
not correspond to a physical string tension in any quantum field
theory.

### V.2 The worldsheet-defined string tension

$$\sigma_{\text{ws}} = \frac{m_{2D}^2}{2\pi}$$

where $m_{2D}$ is the 2D CP$^{N-1}$ mass gap. If the 2D model
is resurgent, $m_{2D}$ is a well-defined positive number.

This is BETTER than $\sigma_{\text{formal}}$ because the 2D
model IS a well-defined quantum field theory (at least at large $N$
where it is exactly solvable). The 2D OS axioms are satisfied
(the 2D CP$^{N-1}$ model satisfies them -- it is a well-defined
2D QFT with a mass gap).

So $\sigma_{\text{ws}}$ is a physically meaningful quantity:
it is the string tension of the confining string whose worldsheet
theory is the 2D CP$^{N-1}$ model.

**The remaining question:** Is this confining string the string
of 4D Yang--Mills? That is the worldsheet connection of Paper 5.

### V.3 The honest answer

Can the resurgent sum define $\sigma_{\text{phys}}$ without a
lattice?

**Yes, in a limited sense:** The resurgent trans-series defines a
finite positive number $\sigma_{\text{formal}}$ or
$\sigma_{\text{ws}}$ that has the right qualitative properties
(positive, scales as $\Lambda^2$, matches lattice computations).

**No, in the full Clay Problem sense:** The resurgent trans-series
alone does not define the FULL quantum field theory (all
correlation functions satisfying all OS axioms). The key missing
ingredient is reflection positivity.

**The hybrid approach (Section IV) offers a path:** Use the lattice
for the definition and the trans-series for the computation. But
this requires solving the convergence problem of the multi-scale
RG, which is the same obstacle as in Path A.


---

## VI. Summary: The Resurgent Definition

| What the resurgent sum gives | Status |
|------------------------------|--------|
| A finite number $\sigma_{\text{formal}} > 0$ | [CONJECTURED] -- depends on resurgence conjecture |
| Agreement with lattice at finite $a$ | [ARGUED] -- asymptotic agreement |
| Euclidean covariance (OS1) | [ARGUED] -- straightforward |
| Reflection positivity (OS2) | [OPEN] -- the key obstruction |
| Mass gap / clustering (OS3) | [ARGUED] -- exponential decay preserved |
| A full QFT satisfying all OS axioms | [OPEN] -- requires OS2 |
| Bypassing the lattice entirely | [OPEN] -- OS2 blocks this |

**The bottom line:** Resurgence can likely COMPUTE $\sigma_{\text{phys}}$
(give its numerical value) but cannot DEFINE the full theory without
additional input (either the lattice or a new argument for reflection
positivity). The trans-series is a computational tool, not a
foundational one -- at least with current mathematical technology.
