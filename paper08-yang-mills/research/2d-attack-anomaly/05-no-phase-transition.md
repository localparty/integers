# 05. Arguments That No Phase Transition Occurs

## I. Scope

This document develops every argument I can find -- beyond pure
anomaly matching -- that the $\mathbb{Z}_3$-twisted $\mathbb{CP}^2$
model has no phase transition as a function of $L$. Each argument
is assessed for rigor.


---

## II. The Center Vortex Free Energy Argument

### II.1 Setup

Define the center vortex free energy on $S^1_L \times S^1_R$
(with $R \gg L$ playing the role of the "spatial" direction):
$$e^{-F_v(L)} = \frac{Z_v}{Z_0}$$

where $Z_0$ is the partition function with the standard
$\mathbb{Z}_3$ twist, and $Z_v$ has an additional center
vortex inserted (a defect in the $x^0$ direction that
multiplies the holonomy by $\omega$ when crossing).

**Interpretation:**
- $F_v(L) > 0$: center vortex is suppressed $\to$
  $\mathbb{Z}_3^{(C)}$ preserved (confined)
- $F_v(L) = 0$: center vortex is free $\to$
  $\mathbb{Z}_3^{(C)}$ at the boundary of breaking
- $F_v(L) < 0$: center vortex proliferates $\to$
  $\mathbb{Z}_3^{(C)}$ broken (deconfined)

### II.2 Small-$L$ calculation

At small $L$ ($L\Lambda \ll 1$), the vortex free energy can be
computed semiclassically. The vortex is a domain wall in the
$x^0$ direction interpolating between center sectors.

The leading contribution is from the tension of the domain wall:
$$F_v(L) = T_{\text{DW}} \cdot R$$

where $T_{\text{DW}}$ is the domain wall tension and $R$ is the
"spatial" extent. The domain wall tension at small $L$ is:
$$T_{\text{DW}} \sim \frac{1}{L} e^{-S_f/(2g^2)}
  = \frac{1}{L}(L\Lambda)^{1/(2N)}$$

For $N = 3$:
$$T_{\text{DW}} \sim \frac{1}{L}(L\Lambda)^{1/6}$$

**Result:** $F_v(L) = T_{\text{DW}} \cdot R > 0$ for all
$R > 0$. Center symmetry is preserved.

**STATUS: This calculation is reliable at small $L$. [PROVED
in the semiclassical regime]**

### II.3 Interpolation to large $L$

At large $L$ ($L\Lambda \gg 1$), the theory is equivalent to the
uncompactified $\mathbb{CP}^2$ model (which is known to be gapped
with mass $m \sim \Lambda$). In this regime:

**If the theory is in the confining phase** (center preserved):
$$F_v(L) \sim m \cdot R = \Lambda \cdot R > 0$$

**If the theory is in the deconfining phase** (center broken):
$$F_v(L) < 0$$

The question is whether $F_v(L)$ can change sign as $L$ varies.

### II.4 The interpolation argument

**CLAIM [ARGUED, not proved].** $F_v(L) > 0$ for all $L$.

**Heuristic argument:**

*Step 1.* At small $L$: $F_v(L)/R = T_{\text{DW}}(L) > 0$.
[PROVED]

*Step 2.* At $L = \infty$: the $\mathbb{CP}^2$ model on
$\mathbb{R}^2$ has a unique vacuum with mass gap $m = c\Lambda > 0$.
The theory is in the confined phase. $F_v(\infty)/R = m > 0$.

Wait -- this is circular. The statement that the uncompactified
theory is in the confined phase IS the statement that
$F_v(\infty) > 0$. We cannot use it as an input.

What we DO know at $L = \infty$:
- The uncompactified $\mathbb{CP}^2$ model has a mass gap.
  [PROVED at large $N$ (Witten 1979), strongly supported by
  lattice simulations at $N = 3$]
- The mass gap implies SOME symmetry is broken. But which one?

At $L = \infty$, the $S^1$ decompactifies. The $\mathbb{Z}_3$
twist becomes irrelevant in the deep IR (it affects the boundary
conditions, which decouple when $L \to \infty$). The relevant
symmetry is the $\mathbb{Z}_3^{(\chi)}$ chiral symmetry of the
uncompactified model.

The uncompactified $\mathbb{CP}^{N-1}$ model breaks
$\mathbb{Z}_N^{(\chi)}$ spontaneously (there are $N$ degenerate
vacua related by $\theta \to \theta + 2\pi/N$).
[ESTABLISHED for $N = 2$ (Haldane, Affleck); ARGUED for
general $N$ from the large-$N$ solution and instanton analysis]

**Therefore at $L = \infty$:** $\mathbb{Z}_3^{(\chi)}$ is broken,
and $\mathbb{Z}_3^{(C)}$ is not a meaningful symmetry (the $S^1$
is gone). The phase matches the small-$L$ pattern.

*Step 3.* Interpolation: the UV phase (small $L$) has
$\chi$-broken, $C$-preserved. The IR endpoint ($L = \infty$)
has $\chi$-broken. If $C$ were to break at some intermediate
$L_*$, there would need to be TWO transitions: one at $L_*$
(where $C$ breaks) and one at some $L_{**} > L_*$ (where the
$S^1$ decompactifies and $C$ ceases to be meaningful).

This double transition is anomaly-consistent but requires a
non-trivial mechanism that creates and then destroys a deconfined
phase in a finite interval $[L_*, L_{**}]$.

**Assessment: The interpolation argument makes a phase transition
seem unlikely (it would require two transitions, not one) but
does not rigorously exclude it.**


---

## III. The Large-N Extrapolation Argument

### III.1 Exact result at $N = \infty$

At $N = \infty$, the $\mathbb{CP}^{\infty}$ model is exactly
solvable (Witten 1979). The mass gap is $m = \Lambda$
independently of the compactification radius $L$, the boundary
conditions, and all other details.

**Why?** At $N = \infty$, the path integral is dominated by a
single saddle point (the large-$N$ master field). The saddle
point is unique and center-symmetric. There is no mechanism
for a phase transition.

### III.2 The $1/N$ expansion around $N = \infty$

At large but finite $N$, corrections are of order $1/N$:
$$F_v(L) = F_v^{(0)}(L) + \frac{1}{N} F_v^{(1)}(L)
  + O(1/N^2)$$

where $F_v^{(0)}(L) > 0$ (the large-$N$ result).

**If $F_v^{(1)}(L)$ is bounded:** Then for $N$ sufficiently
large, $F_v(L) > 0$ for all $L$, and there is no phase
transition.

**For $N = 3$:** The $1/N$ expansion gives $1/N = 1/3$, which
is not small. The expansion is at best qualitative.

**Assessment: The large-$N$ argument proves no phase transition
for $N \geq N_0$ (some $N_0$), but does not determine whether
$N_0 \leq 3$. SUGGESTIVE for $N = 3$ but NOT a proof.**

### III.3 Known results for small $N$

**$N = 2$ ($\mathbb{CP}^1$ model).** Adiabatic continuity is
PROVED (Dunne-Unsal 2012). The $\mathbb{Z}_2$ center symmetry
is preserved at all $L$. The proof uses a combination of:
- Semiclassical analysis at small $L$ (fractional instantons)
- Exact Bethe ansatz solution at $L = \infty$ (the $O(3)$
  sigma model is integrable)
- Continuity argument connecting the two regimes

**$N = 3$ ($\mathbb{CP}^2$ model).** The Bethe ansatz is NOT
available (the $\mathbb{CP}^2$ model is not integrable). This
is the fundamental obstacle.

**$N \geq 4$.** Same obstacle as $N = 3$.


---

## IV. The Integrability Argument for $N = 2$ and Its Failure at $N = 3$

### IV.1 Why $N = 2$ is special

The $\mathbb{CP}^1 \cong S^2$ model is equivalent to the $O(3)$
nonlinear sigma model, which is integrable (the Yang-Baxter
equation is satisfied). The exact S-matrix is known (Zamolodchikov-
Zamolodchikov 1979), and the mass gap is exactly:
$$m = \frac{8}{e} \Lambda$$

The integrability provides complete control over the spectrum at
ALL values of $L$ (via the thermodynamic Bethe ansatz).

### IV.2 Why $N = 3$ is not integrable

The $\mathbb{CP}^{N-1}$ model for $N \geq 3$ is NOT integrable
in the standard sense. There is no known Yang-Baxter equation
or exact S-matrix.

However: the $\mathbb{CP}^{N-1}$ model IS related to an
integrable spin chain via the Haldane conjecture. The $SU(N)$
spin chain with the fundamental representation at each site
is integrable (the $SU(N)$ Heisenberg model solves via nested
Bethe ansatz). The correspondence between the sigma model and
the spin chain is:

$$\text{CP}^{N-1} \text{ sigma model} \quad
  \longleftrightarrow \quad SU(N)
  \text{ Heisenberg antiferromagnet}$$

at the level of low-energy effective field theory.

For $N = 2$: the spin-1 Heisenberg chain has the Haldane gap,
matching the mass gap of the $O(3)$ sigma model. [PROVED
rigorously by Affleck-Kennedy-Lieb-Tasaki 1987 for the AKLT
model, and by Haldane's conjecture + numerical confirmation
for the Heisenberg model.]

For $N = 3$: the $SU(3)$ Heisenberg chain in the fundamental
representation is gapped with 3-fold degeneracy. [ARGUED from
large-$N$, confirmed by DMRG simulations.] This matches the
expected $\mathbb{Z}_3^{(\chi)}$-broken phase of the
$\mathbb{CP}^2$ model.

**But:** the spin chain correspondence gives information about
$L = \infty$ only. It does not control the $L$-dependence.


---

## V. The Gradient Flow / Monotonicity Argument

### V.1 The idea

The partition function $Z(L)$ of the $\mathbb{Z}_3$-twisted
$\mathbb{CP}^2$ model on $S^1_L \times S^1_R$ is a smooth
function of $L$. A phase transition manifests as a non-analyticity
of $\ln Z$ in the $R \to \infty$ limit.

Can we show $\ln Z$ (or some derived quantity) is convex/concave
in $L$, ruling out non-analyticity?

### V.2 The free energy density

$$f(L) = -\frac{1}{R} \ln Z(L)$$

in the $R \to \infty$ limit. The derivatives are:
$$\frac{\partial f}{\partial L} = \langle T_{11} \rangle$$

$$\frac{\partial^2 f}{\partial L^2}
  = -R \left(\langle T_{11}^2 \rangle
  - \langle T_{11} \rangle^2\right) \leq 0$$

where $T_{11}$ is the stress tensor component in the compact
direction.

**The free energy density is CONCAVE in $L$** (the second
derivative is non-positive, by the positivity of the variance).

### V.3 Does concavity help?

Concavity of $f(L)$ means $f$ has no upward cusps. A first-order
phase transition corresponds to a point where $f$ is non-smooth
(a corner, where the left and right derivatives differ).

Concavity does NOT forbid a corner (a concave function can have
downward corners). In fact, a first-order transition corresponds
precisely to a concave function with a corner where the slope
jumps.

**Assessment: Concavity of the free energy does not rule out
first-order transitions. INSUFFICIENT.**

### V.4 A refined monotonicity

Consider the center vortex free energy $F_v(L)/R = T_{\text{DW}}(L)$.
Can we show this is monotone in $L$?

At small $L$: $T_{\text{DW}}(L) \sim L^{-1}(L\Lambda)^{1/6}
\to \infty$ as $L \to 0$.

At large $L$: $T_{\text{DW}}(L) \sim m \sim \Lambda$ (if
the theory remains in the confined phase).

So $T_{\text{DW}}$ DECREASES from $\infty$ to $\Lambda$ as
$L$ goes from $0$ to $\infty$. If $T_{\text{DW}}$ is
monotonically decreasing, it remains positive.

**Can $T_{\text{DW}}(L)$ be non-monotone?** If it dips below
zero at some intermediate $L$ before returning to a positive
value, there would be two phase transitions (enter and exit
the deconfined phase).

A monotonicity result for $T_{\text{DW}}(L)$ would prove
adiabatic continuity. But I know of no theorem that establishes
such monotonicity.

**Assessment: A promising direction but requires a new
inequality. NOT PROVED.**


---

## VI. The Compactification Independence Argument

### VI.1 The idea (Unsal-Yaffe 2008)

For certain theories (specifically, gauge theories with
adjoint matter and $\mathbb{Z}_N$ center symmetry), the
large-$N$ volume independence theorem states:

*At $N = \infty$, expectation values of single-trace operators
are independent of the compactification radius $L$, as long as
center symmetry is unbroken.*

This is the Eguchi-Kawai reduction.

### VI.2 Application to $\mathbb{CP}^{N-1}$

The $\mathbb{CP}^{N-1}$ model at $N = \infty$ with center-
symmetric compactification satisfies volume independence:
$$\langle \mathcal{O} \rangle_{L}
  = \langle \mathcal{O} \rangle_{\infty}
  + O(1/N^2)$$

for all single-trace (gauge-invariant) observables $\mathcal{O}$.

**Key point:** Volume independence holds IF AND ONLY IF center
symmetry is unbroken. If center symmetry breaks at some $L_*$,
volume independence fails at $L_*$.

At $N = \infty$, center symmetry is ALWAYS unbroken (the
large-$N$ master field is center-symmetric). Therefore volume
independence holds at all $L$ at $N = \infty$.

### VI.3 Finite $N$ corrections

At finite $N$, volume independence becomes approximate:
$$\langle \mathcal{O} \rangle_L
  = \langle \mathcal{O} \rangle_\infty
  + O(1/N^2) + O(L^2 \Lambda^2 / N^2)$$

The corrections vanish at large $N$ but not at $N = 3$.

**The self-consistency argument:** Suppose center symmetry
breaks at $L_*$ for some $N_*$. Then volume independence fails
at $L_*$ for $N = N_*$. But volume independence holds exactly
at $N = \infty$. The failure at finite $N$ must be a $1/N$
effect. For $N = 3$, $1/N = 1/3$, which is substantial.

**Assessment: The volume independence argument strongly suggests
no phase transition at large $N$, but cannot rigorously exclude
it at $N = 3$. SUGGESTIVE.**


---

## VII. Assembling the Arguments

None of the individual arguments proves adiabatic continuity
for the $\mathbb{CP}^2$ model. But together they paint a
compelling (though not rigorous) picture:

| Argument | Conclusion | Rigor |
|----------|-----------|-------|
| Anomaly matching | One $\mathbb{Z}_3$ must break | **PROVED** |
| Semiclassical (small $L$) | $C$ preserved, $\chi$ broken | **PROVED** |
| Large $N$ ($N = \infty$) | No transition | **PROVED** |
| $N = 2$ (CP$^1$) | No transition | **PROVED** |
| Interpolation (small $L$ to $\infty$) | Transition requires double swap | **ARGUED** |
| Lattice simulations ($N = 3$) | No transition observed | **NUMERICAL** |
| Volume independence | Transition suppressed at large $N$ | **ARGUED** |
| Concavity of free energy | Insufficient | **INSUFFICIENT** |
| Domain wall tension monotonicity | Unproved | **OPEN** |

**The gap:** No single argument (or combination) rigorously
proves that $\mathbb{Z}_3^{(C)}$ is preserved at ALL $L$ for
$N = 3$. The missing ingredient is a non-perturbative bound
that connects the small-$L$ and large-$L$ regimes.
