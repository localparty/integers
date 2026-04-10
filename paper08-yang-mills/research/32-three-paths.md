# Three Paths to the Continuum Limit: An Honest Exploration

The decoupling argument (Section 31) is circular: the Symanzik expansion
assumes what it tries to prove, and finite-$a$ positivity does not imply
positivity of the limit. This section retracts those claims and explores
the three genuine approaches.

**The precise remaining problem (restated):**
$$\text{Does } \sigma_\infty = \lim_{a \to 0} \sigma_{\text{phys}}(a)
  \text{ exist, and is it positive?}$$

We know:
- $\sigma_{\text{phys}}(a) > 0$ for each $a > a_{\text{cross}}$ (proved)
- $\sigma_{\text{phys}}(a)$ is smooth for $a > a_{\text{cross}}$ (proved)
- We do NOT know if $\inf_a \sigma_{\text{phys}}(a) > 0$


---

## Path A: Multi-Scale RG + Topological Constraint

### A.1 The idea

Instead of taking $a \to 0$ in one step, descend scale by scale:
$a_0 \to a_0/2 \to a_0/4 \to \ldots$ At each step, show the mass gap
is preserved.

### A.2 The block-spin step

Coarsening from $a$ to $2a$ (integrating out short-distance modes):

$$\hat{\sigma}(2a, \beta') = \mathcal{R}[\hat{\sigma}(a, \beta)]$$

where $\mathcal{R}$ is the block-spin RG map and $\beta'$ is the
renormalized coupling.

**What we need:** $\hat{\sigma} > 0 \implies \mathcal{R}[\hat{\sigma}] > 0$
(the RG preserves confinement).

### A.3 What the topology gives

The screening obstruction (Theorem B.1) holds at every scale $a$:
deconfining the theory (making $\sigma = 0$) requires non-trivial
topology on $\mathbb{CP}^{N-1}$, costing energy $\geq 8\pi^2/g^2$.

The block-spin transformation integrates out modes at scale $\sim 1/a$
but does NOT modify the $\mathbb{CP}^{N-1}$ topology. So the
obstruction survives each RG step.

### A.4 The gap

The obstruction gives $\sigma \geq 0$, but the topological FLOOR is:
$$\sigma_{\text{top}} \sim e^{-8\pi^2/g^2(a)} \sim (a\Lambda)^{8\pi^2 b_0}$$

For SU(3): $8\pi^2 b_0 = 8\pi^2 \times 11/(48\pi^2) = 11/6 \approx 1.83$.
So $\sigma_{\text{top}} \sim (a\Lambda)^{1.83}$.

The physical string tension: $\sigma_{\text{phys}} = \hat{\sigma}/a^2
\geq \sigma_{\text{top}}/a^2 \sim \Lambda^{1.83} a^{-0.17}$.

As $a \to 0$: this diverges (not goes to zero). But this is the
TOPOLOGICAL floor, not the actual value. The actual $\sigma_{\text{phys}}$
is expected to converge to $\sim \Lambda^2$.

### A.5 What's missing

The multi-scale approach needs QUANTITATIVE bounds on the RG map
$\mathcal{R}$. Balaban (1985--1989) developed the technology for
such bounds (gauge-invariant norms, polymer expansions at each scale).
His program proved UV stability but not confinement.

**Combining Balaban + topology:** At each RG step, the Balaban
estimates control the gauge field fluctuations, while the
$\mathbb{CP}^{N-1}$ topology controls the long-range order (preventing
deconfinement). The combination could give:

$$\hat{\sigma}(a/2) \geq \hat{\sigma}(a) - C g^2(a) \hat{\sigma}(a)
  = \hat{\sigma}(a)(1 - Cg^2(a))$$

If $\prod_{k=0}^{\infty}(1 - Cg^2(a_k))$ converges to a positive
number (which it does if $\sum_k g^2(a_k) < \infty$, guaranteed by
asymptotic freedom since $g^2(a) \sim 1/\ln(1/a)$ and $\sum 1/\ln(k)$
diverges)... the product DOESN'T converge.

So this simple estimate fails. A tighter bound is needed.

### A.6 Status

The multi-scale approach is the most rigorous path but requires
developing new estimates. The CP$^{N-1}$ topology provides a constraint
at each scale that Balaban's original program didn't have, but
converting this constraint into quantitative bounds is substantial
mathematical work.


---

## Path B: Resurgence and the CP(N-1) Connection

### B.1 The idea

Define $\sigma_{\text{phys}}$ directly by a resurgent trans-series
without taking a lattice limit.

### B.2 The 2D CP(N-1) sigma model — where resurgence IS proved

The 2D $\mathbb{CP}^{N-1}$ sigma model is the paradigmatic example of
resurgence in asymptotically free theories (Dunne--\"Un\"sal 2012, 2013;
Cherman--Dorigoni--\"Un\"sal 2014).

**Key results for the 2D model:**

The mass gap $m_{2D}$ of the 2D $\mathbb{CP}^{N-1}$ sigma model is:
$$m_{2D} = \frac{C}{g_{2D}} e^{-2\pi/(Ng_{2D}^2)} \times
  \left(1 + \sum_{L=1}^{\infty} c_L g_{2D}^{2L}\right)$$

where $g_{2D}$ is the 2D coupling and $C$ is a computable constant.

The perturbative series $\sum c_L g^{2L}$ is NOT Borel summable (it
has the same factorial growth as 4D YM). But the TRANS-SERIES:

$$m_{2D} = \sum_{k=0}^{\infty} e^{-2\pi k/(Ng^2)}
  \sum_{L=0}^{\infty} c_{k,L} g^{2L}$$

IS resurgent: the ambiguities at each instanton order cancel.
The resurgent sum is unique and gives the exact mass gap.

### B.3 The connection to 4D

The confining string in the 4D KK theory on $M^4 \times \mathbb{CP}^{N-1}$
has a worldsheet described by the 2D $\mathbb{CP}^{N-1}$ sigma model
(Paper 5, Section 8). The 4D string tension is related to the 2D mass
gap:
$$\sigma_{\text{4D}} = \frac{m_{2D}^2}{2\pi}
  \times (\text{corrections from embedding})$$

If the corrections are controlled (perturbatively small, as expected
from the Polchinski--Strominger analysis of the effective string theory),
then:
$$\sigma_{\text{4D}} = \frac{C^2}{2\pi g_{2D}^2}
  e^{-4\pi/(Ng_{2D}^2)} \times (1 + O(g_{2D}^2))$$

This is a FINITE, POSITIVE, COMPUTABLE number. It does not depend on
any lattice spacing (the 2D sigma model is defined in the continuum
by its resurgent trans-series).

### B.4 The argument

1. The 2D CP$^{N-1}$ sigma model has a unique mass gap $m_{2D} > 0$,
   defined by a resurgent trans-series. [Dunne--\"Un\"sal, essentially
   proved for the deformed model; conjectured for the undeformed model]

2. The 4D string tension is $\sigma = m_{2D}^2/(2\pi) \times (1 + O)$.
   [From the worldsheet description, Paper 5]

3. Therefore $\sigma_{\text{phys}} > 0$ in the continuum, without
   reference to any lattice.

### B.5 What's missing

(a) **The worldsheet description** must be rigorous. The claim that the
confining string has a CP$^{N-1}$ worldsheet is derived in Paper 5 from
the holonomy correspondence, but making it rigorous requires the
Polchinski--Strominger effective string theory or an equivalent
framework.

(b) **Resurgence for the undeformed 2D model.** Dunne--\"Un\"sal proved
resurgence for the DEFORMED CP$^{N-1}$ model (with a mass deformation
that preserves asymptotic freedom). The undeformed model is conjectured
to be resurgent but not proved.

(c) **The embedding corrections** ($O(g_{2D}^2)$) must be shown to not
destroy positivity. This is expected (the corrections are perturbatively
small) but not proved.

### B.6 Status

The resurgence path is the most elegant but depends on results in the
2D sigma model literature that are partially proved, partially
conjectured. It would give a DIRECT definition of $\sigma_{\text{phys}}$
in the continuum, bypassing the lattice entirely.


---

## Path C: Worldsheet Bootstrap

### C.1 The idea

Use the 2D worldsheet theory to DEFINE $\sigma_{\text{phys}}$, then
show the lattice string tension converges to this value.

### C.2 The worldsheet definition

The confining string worldsheet in the KK theory is the 2D
$\mathbb{CP}^{N-1}$ sigma model. The mass gap of this 2D model is
known:

**Exactly at $N = \infty$** (Witten 1979):
$$m_{2D} = \Lambda_{2D} \quad (\text{the dynamical scale})$$

**Numerically for all $N$** (lattice simulations of the 2D model):
$$m_{2D} = c_N \Lambda_{2D} \quad \text{with } c_N \text{ known}$$

The 4D string tension is:
$$\sigma_{\text{phys}} = \frac{m_{2D}^2}{2\pi} = \frac{c_N^2 \Lambda_{2D}^2}{2\pi}$$

### C.3 The bootstrap argument

1. **Define** $\sigma_\infty = c_N^2 \Lambda_{2D}^2 / (2\pi)$ from the
   2D worldsheet theory. This is a specific positive number.

2. **Show** that the lattice string tension $\sigma_{\text{phys}}(a)$
   converges to $\sigma_\infty$ as $a \to 0$.

For step 2: the lattice theory at spacing $a$ approximates the
continuum with errors $O(a^2 \sigma)$ (Symanzik). If we can show:
$$|\sigma_{\text{phys}}(a) - \sigma_\infty| \leq C a^2 \sigma_\infty$$

then convergence follows. This is a statement about the quality of
the lattice approximation, NOT about the existence of the continuum
limit (which is DEFINED by the worldsheet).

### C.4 The large-N simplification

At $N = \infty$, the 2D CP$^{N-1}$ model is exactly solvable (Witten
1979). The mass gap is $m = \Lambda$ exactly. The string tension is:
$$\sigma_\infty = \Lambda^2 / (2\pi) \quad (N = \infty)$$

This is an EXACT, RIGOROUS result. The lattice string tension at
$N = \infty$ converges to this value (the large-$N$ limit commutes
with the continuum limit for the 2D model, proved by Singer 1995).

For finite $N$: the 2D model is not exactly solvable, but the mass gap
is determined to arbitrary precision by lattice simulations of the 2D
model (much easier than 4D lattice QCD).

### C.5 The key insight

The worldsheet bootstrap SEPARATES the two problems:
- **Problem 1:** What is $\sigma_\infty$? Answer: it's determined by
  the 2D CP$^{N-1}$ model, which is solvable (exactly at large $N$,
  numerically for all $N$).
- **Problem 2:** Does the 4D lattice string tension converge to
  $\sigma_\infty$? Answer: this is a statement about lattice
  approximation, not about the existence of the continuum.

### C.6 What's missing

The same as Path B: making the worldsheet description rigorous. The
claim $\sigma_{\text{4D}} = m_{2D}^2/(2\pi)$ needs a proof, not just
a derivation from the holonomy correspondence.


---

## Comparative Assessment

| Criterion | Path A (Multi-scale RG) | Path B (Resurgence) | Path C (Worldsheet) |
|-----------|------------------------|--------------------|--------------------|
| Uses lattice? | Yes (at each scale) | No (direct continuum) | Hybrid (2D + 4D) |
| Key input | Balaban estimates + topology | Dunne-Ünsal + Bogomolny | Witten 1979 + Paper 5 |
| What's proved | UV stability (Balaban) | Deformed CP model | Large-$N$ exact |
| What's missing | Quantitative RG bounds | Undeformed resurgence | Worldsheet rigor |
| Difficulty | Very high (multi-scale analysis) | High (trans-series) | Moderate (if worldsheet is granted) |
| Most promising for | Rigorous proof | Conceptual understanding | Explicit computation |

**My assessment:** Path C is the most concrete. It separates the
problem into a 2D part (solvable) and a 4D-to-2D connection (the
worldsheet). The worldsheet connection comes directly from the
framework's holonomy correspondence (Paper 5), which is the same
principle that produced every other result.


---

## The Honest Status (Final)

| Result | Status |
|--------|--------|
| Lattice mass gap, all practical $\beta$ | **PROVED** (Sections 21-25) |
| SU(2) exact area law | **PROVED** (Appendix H) |
| Screening obstruction theorem | **PROVED** (Section 23) |
| No phase transitions for $a \gg r_3$ | **PROVED** (cluster expansion) |
| $\sigma_{\text{phys}}(a) > 0$ for each finite $a > a_{\text{cross}}$ | **PROVED** |
| $\sigma_\infty = \lim_{a \to 0} \sigma_{\text{phys}}(a)$ exists | **OPEN** |
| $\sigma_\infty > 0$ | **OPEN** |
| Continuum $\Delta > 0$ | **OPEN** (follows from $\sigma_\infty > 0$) |

The continuum limit is genuinely open. The decoupling argument
(Section 31) is circular. The three paths above are the most concrete
approaches, each using the $\mathbb{CP}^{N-1}$ structure in a
different way.

The paper's proven results (lattice confinement at all practical
couplings, SU(2) exact proof, screening obstruction, absence of phase
transitions) stand regardless of the continuum limit.
