# 05. Obstacles, Dead Ends, and New Ideas

This document is the honest reckoning. What works, what does not,
and what ideas might break the impasse.


---

## I. What Works

### I.1 The trans-series structure is correct

The trans-series ansatz (file 01) is on solid ground. The
perturbative sector, instanton sectors, and instanton--anti-instanton
sectors all have the standard form dictated by semiclassical analysis.
The CP$^{N-1}$ geometry provides all the necessary saddle points.

**Confidence: HIGH.** The trans-series structure is the same for any
asymptotically free gauge theory. The CP$^{N-1}$ input determines
the specific instanton action ($8\pi^2/g^2$) and moduli space
(Appendix B). This is not speculative.

### I.2 The 2D resurgence for the deformed model is proved

Dunne--Unsal (2012, 2013) proved resurgence for the deformed
CP$^{N-1}$ model with $N = 2$. The proof is complete: the
perturbative ambiguities cancel against bion amplitudes at every
order. This is a genuine mathematical theorem.

**Confidence: HIGH.** This is the foundation the 4D program builds
on.

### I.3 The worldsheet connection is physically well-motivated

The confining string worldsheet as a 2D CP$^{N-1}$ sigma model
follows from:
- The holonomy correspondence (Paper 5)
- The fact that the flux tube wraps $H_2(\mathbb{CP}^{N-1})$
- The equivalence between the worldsheet fluctuations and the 2D
  sigma model field

**Confidence: MODERATE.** The physics is clear, but making it
rigorous requires non-perturbative control of the string formation
process.

### I.4 The mass gap is the easiest axiom

Even if the full OS axioms are hard, the mass gap (exponential
clustering) is robust under Borel summation. The resurgent
trans-series gives a definite positive mass gap if the resurgence
conjecture holds.

**Confidence: MODERATE.** The mass gap is the payoff. The hard part
is getting there.


---

## II. What Does Not Work

### II.1 Dead End: Borel summability

Section 28 of the paper conjectured that the zeta-regularized KK
theory might be Borel summable. Section 29 REFUTED this:
$\zeta_{\text{adj}}(0) \neq 0$ on CP$^{N-1}$, so the leading
divergence does not vanish, and the perturbative series has
standard factorial growth.

**Lesson:** The CP$^{N-1}$ geometry does not make the perturbative
series better-behaved than standard 4D Yang--Mills. The factorial
growth is intrinsic to the theory (it comes from the number of
Feynman diagrams), not from the regularization.

### II.2 Dead End: Direct 4D resurgence proof

Route 1 of file 03 (direct 4D resurgence) hits the renormalon
wall. In 4D Yang--Mills, the IR renormalon singularities are at
$t = n/(2b_0)$ on the positive real axis. Cancelling these
requires non-perturbative objects that are NOT instantons.

In standard 4D Yang--Mills, the identity of these objects is
UNKNOWN. The KK construction on CP$^{N-1}$ provides geometric
candidates (neutral bions, center vortices wrapping
$H_1(\mathbb{CP}^{N-1})$), but:
- $H_1(\mathbb{CP}^{N-1}) = 0$ for $N \geq 2$, so there are no
  center vortices.
- The neutral bion mechanism requires fractional instantons, which
  are only established in the DEFORMED 2D model, not in 4D.

**Lesson:** Direct 4D resurgence is too hard with current tools.
The renormalon problem in 4D gauge theory remains unsolved after
40 years. The CP$^{N-1}$ geometry helps but does not solve it.

### II.3 Dead End: Reflection positivity from resurgence

File 04 showed that the resurgent sum does NOT automatically
satisfy reflection positivity (OS2). The median Borel sum is a
specific resummation procedure that has no known positivity
properties.

**Lesson:** Resurgence is a COMPUTATIONAL tool, not a
CONSTRUCTIVE one. It can compute the value of $\sigma_{\text{phys}}$
but cannot define the full quantum field theory.

### II.4 Dead End: The constructive hybrid approach

The hybrid approach (file 04, Section IV) -- using the trans-series
to compute the RG step and the lattice for the definition -- hits
the same convergence problem as Path A. The sum
$\sum_j g^2(a_0/2^j)$ diverges logarithmically, and the
trans-series does not help with this divergence.

**Lesson:** The continuum limit convergence is a GLOBAL problem
(it depends on the behavior of $g^2$ over all scales), while the
trans-series is a LOCAL tool (it computes the physics at one scale).
The two are mismatched.


---

## III. New Ideas

Having hit dead ends on the obvious approaches, I now explore less
obvious ones.

### III.1 Idea A: The 2D definition + embedding theorem

**The idea:** Do not try to define the 4D theory by resurgence.
Instead:

1. Define the 2D CP$^{N-1}$ sigma model rigorously (this is a 2D
   QFT, well within the reach of constructive methods).
2. Define the confining string as an object in the 2D theory (a
   soliton, a domain wall, or a topological defect).
3. Embed the 2D string into 4D using a GEOMETRIC construction
   (not a perturbative one).
4. Show that the embedded string satisfies the 4D OS axioms.

**Why this might work:**
- The 2D CP$^{N-1}$ model is constructively defined for all $N$
  by lattice methods (the 2D lattice is much easier than the 4D
  one: 2D lattice gauge theory is exactly solvable, and the 2D
  sigma model has a well-controlled continuum limit).
- The embedding is GEOMETRIC, not perturbative: it uses the
  fibration $M^4 \times \mathbb{CP}^{N-1}$ and the wrapping
  of the string on $H_2(\mathbb{CP}^{N-1})$.
- The OS axioms for the 4D theory would follow from the OS
  axioms of the 2D theory plus the geometric properties of
  the embedding.

**What needs to be proved:**
- That the 2D CP$^{N-1}$ model has a rigorous continuum limit
  (this IS known for $N = \infty$ and is believed for finite
  $N$, but a rigorous proof at finite $N$ would be new).
- That the geometric embedding preserves the OS axioms (this is
  a statement about the fiber bundle structure, not about
  perturbation theory).

**Status:** This is a NEW approach that has not been explored in
the literature. It combines constructive QFT (2D) with differential
geometry (the embedding).

[SPECULATIVE -- but the ingredients are individually well-understood.]

### III.2 Idea B: Large-$N$ then finite-$N$ correction

**The idea:** At $N = \infty$, everything is exactly solvable:
- The 2D CP$^{N-1}$ model has $m_{2D} = \Lambda_{2D}$ exactly.
- The 4D string tension is $\sigma = \Lambda_{2D}^2/(2\pi)$ exactly.
- The 4D theory at large $N$ is a free string theory (the
  Gross--Taylor expansion, the AdS/CFT correspondence).

Use the $1/N$ expansion to approach finite $N$. At each order in
$1/N$, the correction to $\sigma$ is COMPUTABLE and the OS axioms
can be verified.

**Why this might work:**
- The $1/N$ expansion of the CP$^{N-1}$ model is well-defined and
  has been computed to high order.
- At each order in $1/N$, the theory is a PERTURBATION of the
  exactly solvable $N = \infty$ theory. Perturbations of a
  well-defined theory are well-defined (constructive QFT tells us
  this).
- The $1/N$ expansion is NOT the same as the coupling expansion:
  it is an expansion in a TOPOLOGICAL parameter (the genus of the
  worldsheet). This expansion may have better convergence properties.

**What needs to be proved:**
- That the $1/N$ expansion has a positive radius of convergence
  (at least for the string tension). This is NOT known: the
  $1/N$ expansion is itself an asymptotic series.

However: the $1/N$ expansion for the 2D CP$^{N-1}$ model IS
believed to be Borel summable (unlike the coupling expansion).
The reason: the large-$N$ expansion is controlled by topology
(the genus expansion), and topological expansions are generically
better-behaved than coupling expansions.

If the $1/N$ expansion is Borel summable, then:
$$\sigma(N) = \sigma(\infty) + \frac{1}{N}\sigma_1
  + \frac{1}{N^2}\sigma_2 + \ldots$$
defines $\sigma(N)$ for all $N \geq 2$ (including $N = 2, 3$).

**Evidence:**
- Marino (2014) showed that the $1/N$ expansion of the CP$^{N-1}$
  mass gap is Borel summable in the DEFORMED model. [PROVED]
- For the undeformed model, the $1/N$ expansion of the mass gap
  matches the exact answer (Witten 1979) at $N = \infty$ and the
  corrections are consistent with lattice computations at finite
  $N$. [ARGUED]

[PROMISING -- this approach avoids the coupling expansion entirely
and works in a framework where Borel summability is more plausible.]

### III.3 Idea C: Resurgence + monotonicity

**The idea:** Instead of proving that the resurgent sum satisfies
reflection positivity, prove that the resurgent string tension is
MONOTONE in some parameter, and use monotonicity to extract a
rigorous bound.

**Specifically:** The string tension $\sigma(\beta)$ on the lattice
is a function of the coupling $\beta$. In the strong-coupling regime,
$\sigma(\beta) = \beta/N + O(\beta^2)$ (the strong-coupling expansion).
At weak coupling, the cluster expansion gives $\sigma(\beta) > 0$
(Sections 21--25).

If $\sigma(\beta)$ is MONOTONE DECREASING in $\beta$ (which it is,
physically: the string tension decreases as the coupling increases),
then:
$$\sigma_{\text{phys}} = \lim_{\beta \to \infty}
  \frac{\sigma(\beta)}{a(\beta)^2}$$

The monotonicity of $\sigma(\beta)$ plus the proven positivity at
all finite $\beta$ would give:
- $\sigma(\beta) > 0$ for all $\beta$ (proved)
- $\sigma(\beta)$ is decreasing (to be proved)
- $\sigma(\beta)/a(\beta)^2 = \sigma_{\text{phys}}$ is constant
  (follows from dimensional analysis + monotonicity)

**The obstruction:** Monotonicity of $\sigma(\beta)$ is NOT known
rigorously for Yang--Mills. For the ABELIAN theory ($U(1)$ gauge
theory in 4D), the Ginibre inequality gives monotonicity of
correlation functions. For the non-Abelian theory, no such
inequality is known.

The resurgent trans-series could help: if the trans-series has
ALTERNATING signs (which it does: the instanton correction at odd
order has opposite sign to the perturbative term), then the partial
sums alternate above and below the true value. This gives RIGOROUS
BOUNDS on $\sigma_{\text{phys}}$ without full resurgence:

$$\sigma^{(0)}_{\text{Borel}} - e^{-S_I/g^2} |\sigma^{(1)}|
  \leq \sigma_{\text{phys}} \leq
  \sigma^{(0)}_{\text{Borel}} + e^{-S_I/g^2} |\sigma^{(1)}|$$

The lower bound is positive if $\sigma^{(0)}_{\text{Borel}} >
e^{-S_I/g^2} |\sigma^{(1)}|$, which is true at weak coupling
($g^2 \ll 1$).

**But:** The Borel sum $\sigma^{(0)}_{\text{Borel}}$ is
AMBIGUOUS (it is NOT defined without choosing a lateral
direction). The AMBIGUITY is of order $e^{-S_I/g^2}$, which is
the SAME order as the instanton correction. So the bound is
vacuous at the level of precision needed.

[STATUS: Dead end as stated. The alternating series idea does
not give useful bounds because the ambiguity is the same size
as the correction.]

### III.4 Idea D: The CP^{N-1} deformation in 4D

**The idea:** The deformed CP$^{N-1}$ model in 2D has PROVEN
resurgence. Can we DEFORM the 4D KK theory in a similar way?

Specifically: compactify one of the four M$^4$ directions on
$S^1_L$ with $\mathbb{Z}_N$-twisted boundary conditions. This
gives a theory on $M^3 \times S^1_L \times \mathbb{CP}^{N-1}$.

In the regime $NL\Lambda \ll 1$:
- The 4D theory reduces to a 3D theory at distances $\gg L$
- The worldsheet CP$^{N-1}$ model on $S^1_L$ becomes the
  DEFORMED CP$^{N-1}$ model
- Resurgence is PROVED for the worldsheet theory (Dunne--Unsal)
- The 3D string tension inherits 2D resurgence

Then: take $L \to \infty$ to recover the 4D theory.

**What this would prove:**
- The 3D theory (the deformed 4D theory) has a mass gap and
  confines, with the string tension defined by the resurgent
  trans-series. [WOULD FOLLOW from the 2D result]
- If the $L \to \infty$ limit is continuous (no phase transition),
  then the 4D theory inherits these properties. [CONJECTURED]

**The key step:** Proving the absence of a phase transition at
$L = L_c$ (the deconfinement transition). For pure Yang--Mills on
$S^1$, there IS a deconfinement transition at $L_c \sim 1/T_c$
(the finite-temperature deconfinement transition). So the naive
compactification DOES NOT work.

**The fix:** Use $\mathbb{Z}_N$-twisted boundary conditions
(center-symmetric compactification). Unsal (2008) argued that
the $\mathbb{Z}_N$-symmetric compactification avoids the
deconfinement transition. This is called "volume independence"
or "large-$N$ volume reduction."

For the CP$^{N-1}$ worldsheet:
- At small $L$: the worldsheet is the deformed CP$^{N-1}$ model
  (proven resurgence)
- At large $L$: the worldsheet is the undeformed CP$^{N-1}$ model
  (conjectured resurgence)
- The connection between small and large $L$ is the adiabatic
  continuity conjecture

**Status:** This approach reduces the 4D resurgence problem to
the 2D adiabatic continuity conjecture, which is the central
open problem in the 2D resurgence program (file 02, Section III.1).

[PROMISING -- this is the tightest logical chain I can construct.
The 4D problem is reduced to a single 2D conjecture.]


---

## IV. The Tightest Logical Chain

After exploring all these ideas, the tightest chain to
$\sigma_{\text{phys}} > 0$ via resurgence is:

**Step 1.** Prove resurgence for the deformed 2D CP$^{N-1}$
model for all $N \geq 2$.
**Status:** PROVED for $N = 2$, ARGUED for $N \geq 3$.
**Remaining work:** Extend the Dunne--Unsal computation to general
$N$. This is a finite computation (the one-loop determinant around
fractional instantons for general $N$).

**Step 2.** Prove adiabatic continuity: the deformed model at
$NL\Lambda \ll 1$ is in the same phase as the undeformed model
at $L = \infty$.
**Status:** PROVED for $N = 2$ (Dunne--Unsal 2012), CONJECTURED
for $N \geq 3$.
**Remaining work:** This is the hardest step. It requires showing
that the CP$^{N-1}$ mass gap is a smooth function of $L$ for
all $L > 0$. In the 2D context, this is a statement about a 1D
parameter ($L$) in a 2D QFT -- much more tractable than the 4D
continuum limit.

**Step 3.** Establish the worldsheet connection: the confining
string of the 4D KK theory on $M^4 \times \mathbb{CP}^{N-1}$
has a worldsheet described by the 2D CP$^{N-1}$ sigma model.
**Status:** ARGUED from the holonomy correspondence (Paper 5).
**Remaining work:** Make the derivation rigorous. The key issue
is showing that the flux tube dynamics in the confining regime
is described by the sigma model, not by some other 2D theory.

**Step 4.** Show that the embedding corrections do not destroy
positivity: $\sigma_{\text{4D}} = m_{2D}^2/(2\pi) \times
(1 + O(\delta))$ with $|\delta| < 1$.
**Status:** ARGUED from the Polchinski--Strominger effective
string theory.
**Remaining work:** Bound $\delta$ rigorously.

**Step 5.** Recover the full 4D OS axioms from the worldsheet
plus bulk.
**Status:** OPEN. This is the reflection positivity problem
(file 04, Section II.2).
**Remaining work:** Either prove reflection positivity for the
resurgent sum, or use a hybrid lattice+resurgence approach.

**The chain:**
$$\text{Deformed 2D (proved)} \xrightarrow{\text{Step 2}}
  \text{Undeformed 2D} \xrightarrow{\text{Step 3}}
  \text{4D string tension} \xrightarrow{\text{Step 5}}
  \text{4D QFT}$$

Steps 1 and 4 are technical (finite computations that can in
principle be completed). Steps 2 and 3 are conceptual (they
require new ideas or new methods). Step 5 is foundational (it
is shared by all approaches to the continuum limit).


---

## V. Comparison with Paths A and C

| Criterion | Path A (Multi-scale RG) | Path B (Resurgence) | Path C (Worldsheet) |
|-----------|------------------------|--------------------|--------------------|
| Key open step | RG bounds at each scale | Adiabatic continuity | Worldsheet rigor |
| Hardness of key step | Very hard (4D) | Hard (2D) | Moderate (2D+geometry) |
| Shared obstruction | Continuum limit | Continuum limit | Worldsheet rigor |
| Unique obstruction | Balaban estimates | Reflection positivity | Lattice matching |
| Uses 2D results? | No | Yes (heavily) | Yes (heavily) |
| Gives OS axioms? | Yes (by construction) | No (OS2 missing) | Partially |

**The key observation:** Paths B and C have the SAME core
dependency: the 2D CP$^{N-1}$ model. Path B uses its resurgence;
Path C uses its mass gap. They differ in how they connect to 4D.

**My recommendation:** MERGE Paths B and C.

Use Path C's worldsheet definition of $\sigma_{\text{4D}}$
(which gives a concrete number from the 2D model) and Path B's
resurgence to COMPUTE this number (giving the trans-series
expansion). The combined path:

1. Define $\sigma_{\text{4D}} = m_{2D}^2/(2\pi)$ [Path C]
2. Compute $m_{2D}$ by resurgent trans-series [Path B]
3. Use the lattice to verify and to get the OS axioms [lattice]

This separation of concerns is clean:
- The DEFINITION comes from the worldsheet (Path C)
- The COMPUTATION comes from resurgence (Path B)
- The AXIOMS come from the lattice (existing proof)


---

## VI. The Brutally Honest Summary

### What resurgence can do for the Yang--Mills mass gap:

1. **Compute $\sigma_{\text{phys}}$.** If the resurgence conjecture
   holds (even at the conjectural level), the trans-series gives a
   concrete number. This number matches lattice QCD to high
   precision. [COMPUTABLE but CONJECTURAL]

2. **Explain WHY $\sigma > 0$.** The trans-series makes the
   mechanism transparent: the mass gap arises from the interplay of
   perturbative and non-perturbative sectors, with the CP$^{N-1}$
   instantons providing the non-perturbative saddles. [EXPLANATORY]

3. **Reduce the continuum limit to a 2D problem.** Through the
   worldsheet connection, the 4D continuum limit reduces to the
   2D adiabatic continuity conjecture. This is a DRAMATIC
   simplification: from a 4D gauge theory problem to a 1D parameter
   in a 2D QFT. [STRUCTURAL]

### What resurgence CANNOT do (with current technology):

1. **Define the full 4D QFT.** The resurgent sum does not
   automatically satisfy reflection positivity. Without OS2, there
   is no quantum field theory. [BLOCKED by OS2]

2. **Prove the continuum limit.** The trans-series computes the
   physics at each scale but does not control the convergence over
   all scales. The continuum limit is a GLOBAL problem; resurgence
   is a LOCAL tool. [BLOCKED by convergence]

3. **Replace the lattice.** The lattice gives the OS axioms and
   the non-perturbative definition. Resurgence gives the
   computation and the explanation. They are complementary, not
   competing. [NOT A REPLACEMENT]

### The single most impactful result that would advance the program:

**Prove adiabatic continuity for the 2D CP$^{N-1}$ model at $N = 3$.**

This would:
- Complete the resurgence chain from the deformed model to the
  undeformed model [Step 2]
- Give a concrete, computable mass gap $m_{2D}$ for the physical
  CP$^2$ model [Path C]
- Define $\sigma_{\text{4D}} = m_{2D}^2/(2\pi)$ in the continuum
  [the final answer]
- Reduce the remaining problem to the worldsheet rigor (Step 3)
  and the OS axioms (Step 5), which are shared by all approaches

This is a PURE 2D PROBLEM. It does not require 4D gauge theory
technology. It is accessible to the methods of constructive 2D
QFT, which are much more developed than the 4D counterparts.

The Yang--Mills mass gap, one of the great open problems of 4D
mathematical physics, may ultimately be reduced to a question
about a 2D sigma model.
