# 04. IR Constraints: What the Anomaly Tells Us About the Large-L Phase

## I. The Question

As $L$ increases from $L \ll 1/\Lambda$ (semiclassical UV) to
$L \gg 1/\Lambda$ (strongly-coupled IR), can the pattern of
symmetry realization change? Specifically:

**Can there be a phase transition at some $L = L_*$ where
$\mathbb{Z}_3^{(C)}$ breaks and $\mathbb{Z}_3^{(\chi)}$ is
restored?**

The anomaly constrains but does not uniquely determine the answer.
This section develops the constraints as far as they go.


---

## II. The Four Anomaly-Consistent Scenarios

The mixed anomaly between $\mathbb{Z}_3^{(C)}$ and
$\mathbb{Z}_3^{(\chi)}$ requires at least one symmetry to be
broken (in a gapped phase). The logically possible scenarios for
the IR ($L \to \infty$) are:

### Scenario A: Adiabatic continuity (no transition)

- $\mathbb{Z}_3^{(C)}$: **preserved** at all $L$
- $\mathbb{Z}_3^{(\chi)}$: **broken** at all $L$
- **No phase transition** as a function of $L$

This is the desired result. The UV and IR are in the same phase.

### Scenario B: Center-breaking transition

- At $L = L_*$: $\mathbb{Z}_3^{(C)}$ breaks, $\mathbb{Z}_3^{(\chi)}$
  restores
- First-order transition (the two $\mathbb{Z}_3$ symmetries swap roles)

The anomaly allows this because the IR phase (C-broken, $\chi$-preserved)
matches the anomaly just as well as the UV phase.

### Scenario C: Both broken

- At some $L$: both $\mathbb{Z}_3^{(C)}$ and $\mathbb{Z}_3^{(\chi)}$
  are broken
- 9-fold vacuum degeneracy (or 3-fold with both broken to the
  same subgroup)

The anomaly allows this. It over-satisfies the constraint.

### Scenario D: Gapless phase

- At some $L_c$: the gap closes, producing a CFT
- The anomaly is matched by the conformal tower

This is possible in principle (the $\mathbb{CP}^{N-1}$ model
could have a gapless point) but highly non-generic. There is
no known mechanism that would produce a CFT at a specific $L$.


---

## III. Anomaly Constraints That Go Beyond Existence

### III.1 The anomaly polynomial and its rigidity

The anomaly is characterized by the class
$[\omega] \in H^3(B\mathbb{Z}_3 \times B\mathbb{Z}_3, U(1))
= \mathbb{Z}_3$, with $[\omega] = 1 \neq 0$.

**Rigidity.** The anomaly class is a discrete invariant. It cannot
change continuously. Therefore:

**CLAIM [PROVED].** The anomaly class $[\omega]$ is the same at
all values of $L$.

*Proof.* The anomaly is a property of the short-distance
(UV) degrees of freedom. Varying $L$ is a continuous
deformation of the theory that does not affect the anomaly
(no new degrees of freedom enter or leave the spectrum
as $L$ varies -- the theory is always the same
$\mathbb{CP}^2$ sigma model, just on a different geometry).
$\square$

This is a tautology (the anomaly is always the same because
the theory is always the same), but it is important: it means
every phase at every $L$ must match the same anomaly.

### III.2 Constraints on phase transitions

If there IS a phase transition at $L = L_*$, the anomaly
constrains what can happen:

**CLAIM [PROVED].** At a phase transition $L_*$, the following
are forbidden:

**(a) Transition to a trivially gapped symmetric phase.** Both
$\mathbb{Z}_3^{(C)}$ and $\mathbb{Z}_3^{(\chi)}$ preserved
with a unique gapped vacuum. [Forbidden by the anomaly.]

**(b) Partial restoration without compensation.** If
$\mathbb{Z}_3^{(\chi)}$ is restored at $L_*$, then either
$\mathbb{Z}_3^{(C)}$ must break, or the theory becomes gapless
or topological. [Required by anomaly matching.]

**CLAIM [NOT PROVED].** The anomaly does NOT forbid:

**(c) A first-order transition** where $\mathbb{Z}_3^{(\chi)}$
restores and $\mathbb{Z}_3^{(C)}$ simultaneously breaks.
The anomaly is matched on both sides of the transition.

**(d) A cascade of transitions** $L_1 < L_2 < \ldots$ where
the symmetry realization changes multiple times, as long as the
anomaly is matched at each stage.


### III.3 The Vafa-Witten-type argument (and why it fails here)

In 4D gauge theory, the Vafa-Witten theorem (1984) proves that
vector-like symmetries cannot be spontaneously broken. One might
hope for an analogous result for center symmetry.

**The Vafa-Witten theorem does not apply to center symmetry.**
The theorem requires the symmetry to act by positive operators
on the path integral measure. Center symmetry does NOT have this
property (it acts on the holonomy, which enters the action in a
non-positive-definite way).

More specifically, in the $\mathbb{CP}^{N-1}$ model, the center
transformation $z_j \mapsto \omega^j z_j$ does NOT preserve the
positivity of $e^{-S}$ because it changes the boundary conditions,
not the fields in the bulk. The Vafa-Witten positivity argument
breaks down.

**STATUS: The inapplicability of Vafa-Witten to center symmetry
is well known. [ESTABLISHED, see e.g. Kovtun-Unsal-Yaffe 2007]**


---

## IV. Attempting to Rule Out Scenario B

Scenario B (center-breaking transition) is the main threat to
adiabatic continuity. Here are arguments against it, with honest
assessments.

### IV.1 Argument from the effective potential

**The approach.** Compute the effective potential for the Polyakov
loop $P$ as a function of $L$ and check whether a minimum at
$P = 0$ (center-symmetric) persists to all $L$.

**At small $L$:** The one-loop perturbative potential is:
$$V_{\text{pert}}(P) = \frac{2}{\pi L^2} \sum_{n=1}^{\infty}
  \frac{|P_n|^2}{n^2}$$

where $P_n = \text{Tr}(\Omega^n)$ are the Polyakov loop
winding modes. For the $\mathbb{Z}_3$-symmetric holonomy,
$P_n = 0$ for $n \not\equiv 0 \bmod 3$. This is a minimum.

The fractional instanton potential reinforces this minimum
by generating a mass for fluctuations of $P$ around 0.

**At large $L$:** The perturbative calculation is unreliable
(strong coupling). The question is whether non-perturbative
effects can destabilize the center-symmetric minimum.

**Assessment: INCONCLUSIVE.** The effective potential approach
works at small $L$ but cannot be trusted at large $L$. This
is the fundamental difficulty.

### IV.2 Argument from large-N

**The approach.** At $N = \infty$, the $\mathbb{CP}^{N-1}$ model
is exactly solvable (Witten 1979). The mass gap is
$m = \Lambda$ independently of the compactification details.
Center symmetry is preserved at all $L$.

**Extrapolation to $N = 3$:** If the $N = \infty$ result extends
to finite $N$, center symmetry is preserved.

**Assessment: SUGGESTIVE but NOT a proof.** Large-$N$ solutions
can miss finite-$N$ phase transitions. The $\mathbb{Z}_3$ center
symmetry exists only at $N = 3$, so large-$N$ extrapolation
is indirect.

However: the large-$N$ result tells us that adiabatic continuity
is the generic behavior. A phase transition at finite $N$ would
require a non-perturbative mechanism that vanishes at large $N$.

### IV.3 Argument from lattice simulations

**The evidence.** Lattice simulations of the $\mathbb{CP}^2$
model with $\mathbb{Z}_3$ twist (Bonati et al. 2019, Berni
et al. 2021) show:

- $\langle P \rangle = 0$ at all simulated values of $L$
- No sign of a phase transition in the Polyakov loop susceptibility
- The mass gap varies smoothly with $L$

**Assessment: STRONG EVIDENCE but not a proof.** Lattice
simulations are numerical, not analytical. They could miss a
very weakly first-order transition or a transition at $L$ values
not simulated.

### IV.4 Argument from the anomaly + additional symmetry

**The idea.** If there were additional symmetries that
distinguished between Scenarios A and B, the anomaly could
become sufficient.

**Charge conjugation $\mathcal{C}$.** At $\theta = 0$, the
theory has $\mathcal{C}$ symmetry ($z \to \bar{z}$). Does
$\mathcal{C}$ provide additional constraints?

$\mathcal{C}$ acts as: $\hat{\chi} \to \hat{\chi}^{-1}$,
$\hat{C} \to \hat{C}$ (up to a choice of convention).
The anomaly involving $\mathcal{C}$ is:

$$H^3(B(\mathbb{Z}_3 \times \mathbb{Z}_3 \rtimes \mathbb{Z}_2),
  U(1)) = ?$$

This group cohomology is more complex. The $\mathbb{Z}_2$ action
on $\mathbb{Z}_3^{(\chi)}$ (by inversion) means the anomaly
lives in a twisted cohomology group. Computing this:

For $G = \mathbb{Z}_3 \times \mathbb{Z}_3$ with the
$\mathbb{Z}_2$ acting by $(a, b) \mapsto (a, -b)$:
$$H^3(BG^{\mathbb{Z}_2}, U(1)) = ?$$

This computation requires the Lyndon-Hochschild-Serre spectral
sequence for the extension $1 \to \mathbb{Z}_3 \times \mathbb{Z}_3
\to G_{\text{full}} \to \mathbb{Z}_2 \to 1$.

**I will not complete this computation here**, but note that
even if it provides additional constraints, it is unlikely to
uniquely fix the symmetry realization (since both Scenario A
and B are consistent with $\mathcal{C}$-symmetry).

**Assessment: UNLIKELY TO BE SUFFICIENT.**


---

## V. The Strongest Anomaly-Based Constraint

### V.1 Anomaly + gap $\Rightarrow$ SSB, but which SSB?

**Theorem (strongest anomaly statement for this problem).**
[PROVED]

*In the $\mathbb{Z}_3$-twisted $\mathbb{CP}^2$ model on
$\mathbb{R} \times S^1_L$, at every value of $L$:*

*If the theory is gapped, then either $\mathbb{Z}_3^{(C)}$ or
$\mathbb{Z}_3^{(\chi)}$ (or both) is spontaneously broken.*

*Proof.* Direct consequence of the mixed 't Hooft anomaly
(derived in 02-thooft-anomaly.md, Section III.2). $\square$

### V.2 What the anomaly cannot determine

**The anomaly CANNOT determine:**

1. **Which $\mathbb{Z}_3$ breaks.** Both options match the
   anomaly.

2. **Whether the pattern changes with $L$.** A swap from
   "$\chi$-broken, $C$-preserved" to "$C$-broken, $\chi$-preserved"
   is anomaly-consistent.

3. **The order of any phase transition.** The anomaly constrains
   the phases but not the transitions between them.

4. **Whether a gapless point exists.** The anomaly allows a
   gapless (CFT) phase at isolated values of $L$.


---

## VI. What Additional Input Could Complete the Proof

### VI.1 A monotonicity principle

If we could show that the free energy of a center vortex (the
defect that would break $\mathbb{Z}_3^{(C)}$) is monotonically
increasing (or bounded below by a positive constant) as a
function of $L$, adiabatic continuity would follow.

**The center vortex free energy** $F_v(L)$ is defined as:
$$e^{-F_v(L)} = \frac{Z_{\text{twisted}}}{Z_{\text{untwisted}}}$$

where $Z_{\text{twisted}}$ has a center vortex inserted.

- $F_v(L) > 0$: center symmetry preserved (vortex suppressed)
- $F_v(L) < 0$: center symmetry broken (vortex proliferates)

At small $L$: $F_v(L) \sim e^{-S_f}/(L\Lambda)^{1/3} > 0$
(semiclassical).

The question is whether $F_v(L)$ can become negative at large $L$.

### VI.2 A topological obstruction

If the space of vacua (as a function of $L$) has a topological
property that prevents the center-symmetric vacuum from
disappearing, adiabatic continuity would follow.

For example: if the vacuum manifold at each $L$ is connected
and the center-symmetric point is a global minimum that cannot
be continuously deformed to a center-breaking minimum without
crossing an energy barrier...

This is heuristic. Making it rigorous requires understanding
the non-perturbative effective potential at all $L$.

### VI.3 An inequality from reflection positivity

Reflection positivity of the 2D theory on $\mathbb{R} \times S^1$
gives inequalities relating correlation functions at different
$L$. If these inequalities could bound the Polyakov loop
susceptibility, they might rule out a phase transition.

**Specifically:** the Polyakov loop two-point function satisfies
(by reflection positivity in the $x^0$ direction):
$$|\langle P(x) P^\dagger(0) \rangle|^2
  \leq \langle P(x) P^\dagger(x) \rangle
  \langle P(0) P^\dagger(0) \rangle$$

This gives $|\langle P \rangle|^2 \leq \langle |P|^2 \rangle$.
But $\langle |P|^2 \rangle$ includes both connected and
disconnected parts, and the inequality does not constrain the
sign of $\langle P \rangle$ enough to rule out breaking.

**Assessment: INSUFFICIENT as stated.** Reflection positivity
gives correlation inequalities, but they are not sharp enough
to determine the phase.

### VI.4 Continuity of the mass gap + anomaly

**A potentially powerful approach:**

**CLAIM [CONDITIONAL].** If the mass gap $\Delta(L)$ is continuous
and strictly positive for all $L > 0$, then no phase transition
occurs and adiabatic continuity holds.

*Proof sketch.* A phase transition (change in symmetry
realization) in a gapped system requires the gap to close at the
transition point (for a second-order transition) or the
ground-state degeneracy to change discontinuously (for a
first-order transition).

For a first-order transition: the ground state jumps from the
$\chi$-broken phase (3-fold degeneracy in chiral sector) to
the $C$-broken phase (3-fold degeneracy in center sector).
This requires a level crossing where three new states become
degenerate with the vacuum. At the crossing point, the gap
between the true vacuum and the competing states vanishes.

**But:** in a finite-volume system ($S^1_L \times S^1_R$ with
$R \gg L$), there are no true phase transitions. The gap
$\Delta(L, R)$ is strictly positive and analytic in both $L$
and $R$ for all finite volumes. The phase transition, if it
exists, appears only in the $R \to \infty$ limit.

**Assessment: This approach connects the problem to the behavior
of $\Delta(L)$ in the thermodynamic limit, but does not by
itself prove continuity.**


---

## VII. Summary

**What the anomaly proves about the IR:**
1. At least one of $\{\mathbb{Z}_3^{(C)}, \mathbb{Z}_3^{(\chi)}\}$
   must be broken (or gapless/topological) at every $L$. [PROVED]
2. Both the confining phase (C-preserved) and deconfining phase
   (C-broken) are anomaly-consistent. [PROVED]

**What the anomaly does NOT prove:**
3. Which symmetry is broken at large $L$. [OPEN]
4. Whether a phase transition occurs. [OPEN]

**What additional input could close the gap:**
5. A monotonicity/positivity result for the center vortex free
   energy $F_v(L)$.
6. A proof that $\Delta(L) > 0$ continuously for all $L$.
7. A rigorous large-$N$ extrapolation with finite-$N$ error bounds.
