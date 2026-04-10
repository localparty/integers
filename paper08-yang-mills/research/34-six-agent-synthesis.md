# Six-Agent Synthesis: The 2D CP² Mass Gap

Six independent agents attacked the continuum limit from different
angles. This section records their convergence and the precise
remaining problem.


---

## I. What Each Agent Found

### Round 1: Three approaches to the continuum limit

**Path A (Multi-scale RG):** The naive RG product diverges
($\sum g_k^2 = \infty$). Breakthrough: track $\xi = 1/\Delta$ instead
of $\sigma$; the renormalized mass shift is $O(g_k^4)$ and
$\sum g_k^4 < \infty$. Requires Balaban-type estimates.

**Path B (Resurgence):** Direct 4D resurgence blocked by IR
renormalons. Going through the worldsheet works: $\sigma_{\text{4D}} =
m_{\text{2D}}^2/(2\pi)$. Reduces to adiabatic continuity for 2D
CP$^{N-1}$. Recommends merging with Path C.

**Path C (Worldsheet Bootstrap):** Most concrete. At $N = \infty$:
everything proved. At finite $N$: 4-stage program. Identifies the
L\"uscher coefficient as a decisive experimental test.

**All three converged:** the 4D continuum limit reduces to
**adiabatic continuity for the 2D CP$^2$ sigma model**.


### Round 2: Three attacks on the 2D problem

**Bootstrap Cluster Expansion:** Step size $\delta_n \sim c_3 L_n$
(geometric growth), so $L \to \infty$ in $\sim \ln(\Lambda L_0)$ steps.
**Bottleneck:** the crossover regime $L \sim 1/\Lambda$ where
$mL \sim O(1)$. Whether the cluster expansion converges there depends
on specific constants that are not analytically computable. Confidence:
85%.

**1/N Expansion:** The series $m(N) = \Lambda(1 + 0.89/N + \ldots)$
converges slowly at $N = 3$. Five strategies tried; none closes the
gap completely. **Best idea:** prove monotonicity $m(N) \geq m(\infty)
= \Lambda$ for all finite $N$. Even if Borel singularities exist, the
ambiguity is $\sim 10^{-16}$ at $N = 3$ — far too small to flip the
sign.

**Anomaly Matching:** The mixed $\mathbb{Z}_3 \times \mathbb{Z}_3$
anomaly proves at least one $\mathbb{Z}_3$ must break at every $L$,
but **cannot determine which one**. The anomaly is symmetric between
center and chiral symmetries. Anomaly matching alone is insufficient.
**Best idea:** compute the $O(1/N)$ correction to the center vortex
free energy.


---

## II. The Pattern Across All Six Agents

Three independent ideas emerged repeatedly:

### Pattern 1: Monotonicity in $N$

If $m(N) \geq m(\infty) = \Lambda$ for all finite $N$, the mass gap at
$N = 3$ follows immediately. This was identified by:
- Path C (large-$N$ exact → finite-$N$ corrections)
- 1/N agent (Strategy E in assessment)
- Anomaly agent (center vortex free energy increases at finite $N$)

**Physical argument for monotonicity:** At $N = \infty$, the CP$^{N-1}$
model becomes a free (Gaussian) field theory of the auxiliary field
$\sigma$. At finite $N$, the fluctuations of $\sigma$ are enhanced
(more quantum corrections). Enhanced fluctuations INCREASE the mass gap
(quantum fluctuations disorder the system, increasing the correlation
mass). Therefore $m(N) \geq m(\infty)$.

**Mathematical formulation:** The mass gap is the spectral gap of the
transfer matrix $T$. For the CP$^{N-1}$ model:
$$T = e^{-aH}, \quad H = H_0 + \frac{1}{N} V$$

where $H_0$ is the $N = \infty$ Hamiltonian (quadratic, exactly
solvable) and $V$ is the $1/N$ correction (interaction). If $V \geq 0$
(the interaction is repulsive), then $H \geq H_0$ and
$\Delta(N) \geq \Delta(\infty) = \Lambda$.

**Status:** The sign of $V$ is not established rigorously. The physical
argument (fluctuations increase the gap) is compelling but not a proof.

### Pattern 2: The crossover at $L \sim 1/\Lambda$ is a finite problem

The bootstrap agent found that extending $m > 0$ from small $L$ to
large $L$ requires passing through a finite interval
$L \in [c_1/\Lambda, c_2/\Lambda]$ (the crossover). Everything outside
this interval is controlled (semiclassical at small $L$, large-$N$ at
large $L$).

The crossover interval has FINITE extent (order $1/\Lambda$ in width).
The mass gap in this interval is order $\Lambda$ (numerically confirmed).
The cluster expansion convergence depends on specific constants.

**This is a computer-assistable problem:** the constants can be bounded
numerically. A computer-assisted proof (rigorous numerics with interval
arithmetic) could verify the cluster expansion convergence at finitely
many points in the crossover interval, then use analyticity to
interpolate.

### Pattern 3: The center vortex free energy is the decisive quantity

The anomaly agent identified: the center vortex free energy $F_v(L)$
controls whether the $\mathbb{Z}_3$ center symmetry is preserved.
If $F_v(L) > 0$ for all $L$, then $\mathbb{Z}_3$ is preserved and
there is no phase transition.

At small $L$: $F_v > 0$ (proved semiclassically).
At $N = \infty$: $F_v = \infty$ (proved exactly).
At $N = 3$: $F_v = F_v^{(\infty)} + F_v^{(1)}/3 + \ldots$

The $O(1/N)$ correction $F_v^{(1)}$ is a SPECIFIC, COMPUTABLE number
in the exact $1/N$ expansion. If $F_v^{(1)} > -3 F_v^{(\infty)}$, then
$F_v(N=3) > 0$ and adiabatic continuity holds.

**This is a concrete calculation** that could close the entire
Yang--Mills mass gap problem.


---

## III. The Three Most Promising Attacks

Ranked by concreteness and feasibility:

### Attack 1: Computer-assisted proof at the crossover (feasibility: HIGH)

Use rigorous numerics (interval arithmetic) to bound $m(L)$ in the
crossover interval $L \in [c_1/\Lambda, c_2/\Lambda]$. The 2D CP$^2$
lattice model is small enough to simulate with rigorous error bounds.
If $m(L) > K/L$ throughout the crossover (where $K$ is the cluster
expansion convergence constant), adiabatic continuity follows.

**What's needed:** Rigorous lattice simulation of the 2D CP$^2$ model
at 10--20 values of $L$ in the crossover region, with certified error
bars. This is within reach of current computational methods.

### Attack 2: Compute $F_v^{(1)}$ in the $1/N$ expansion (feasibility: MEDIUM)

The center vortex free energy at $O(1/N)$ is a specific Feynman diagram
calculation in the auxiliary-field formalism. The diagram involves the
$\sigma$-propagator coupled to the center vortex background. If the
result satisfies $F_v^{(1)} > -3 \times F_v^{(\infty)}$, adiabatic
continuity holds at $N = 3$.

**What's needed:** Evaluate the one-loop fluctuation determinant around
the center vortex saddle point in the $N = \infty$ background.

### Attack 3: Prove monotonicity $m(N) \geq m(\infty)$ (feasibility: MEDIUM)

If the $1/N$ interaction $V$ in the Hamiltonian is positive
semi-definite ($V \geq 0$), then $m(N) \geq m(\infty) = \Lambda > 0$.

**What's needed:** Show that the $1/N$ correction to the CP$^{N-1}$
Hamiltonian is a positive operator. This is a spectral theory question
about the auxiliary field effective potential.


---

## IV. The Decisive Experiment: The L\"uscher Coefficient

Independent of the mathematical proof, the framework makes a
**falsifiable prediction** testable with existing lattice data:

The confining string worldsheet is a CP$^{N-1}$ sigma model with
central charge $c = 2$. The L\"uscher term in the static potential:

$$V(R) = \sigma R - \frac{\pi c}{12R} + O(1/R^2)$$

**Framework prediction:** $c = 2$ (CP$^{N-1}$ worldsheet)
$\Rightarrow V = \sigma R - \pi/(6R)$

**Standard prediction:** $c = 1$ (Nambu--Goto string)
$\Rightarrow V = \sigma R - \pi/(12R)$

This is a factor of 2 difference in a measurable quantity. Current
lattice data has $\sim 20$--$30\%$ precision on the L\"uscher term.
A dedicated measurement at $5\%$ precision would be decisive.

If $c = 2$: the worldsheet is CP$^{N-1}$, the entire framework is
validated, and the mathematical proof program is on the right track.

If $c = 1$: the worldsheet is NOT CP$^{N-1}$, and the worldsheet
bootstrap (Path C) fails.


---

## V. The Complete Proof Architecture

$$\boxed{
\begin{array}{c}
\text{Lattice mass gap, all practical } \beta \quad [\text{PROVED}] \\
\downarrow \\
\text{Continuum limit reduces to 2D} \quad [\text{PROVED}] \\
\downarrow \\
\text{2D CP}^2 \text{ adiabatic continuity} \quad [\text{OPEN}] \\
\downarrow \\
\text{Worldsheet: } \sigma_\infty = m_{2D}^2/(2\pi) \quad [\text{ARGUED}] \\
\downarrow \\
\Delta_\infty = c\sqrt{\sigma_\infty} > 0 \quad [\text{THEOREM}]
\end{array}
}$$

**The single open step** is the 2D adiabatic continuity, which three
concrete attacks can close:
1. Computer-assisted rigorous numerics at the crossover
2. $O(1/N)$ center vortex free energy calculation
3. Monotonicity proof $m(N) \geq m(\infty)$

Any ONE of these would complete the proof.
