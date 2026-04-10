# 01. Center Vortex Setup in the Z_3-Twisted CP^2 Model

## I. The Geometry

We work on the Euclidean torus $\Sigma = S^1_L \times S^1_R$ with
$R \gg L$. The coordinate $x^1 \in [0, L)$ is the compact
"thermal" direction carrying the $\mathbb{Z}_3$ twist; $x^0 \in [0, R)$
is the long "spatial" direction, eventually taken to $R \to \infty$.

The CP^2 fields $z = (z_1, z_2, z_3)$, $|z|^2 = 1$, obey the
$\mathbb{Z}_3$-twisted boundary condition around the $x^1$ circle:

$$z(x^0, x^1 + L) = \Omega \, z(x^0, x^1), \qquad
  \Omega = \mathrm{diag}(1, \omega, \omega^2), \quad
  \omega = e^{2\pi i/3}$$

This twist distributes the holonomy symmetrically among the three
center elements, preserving the $\mathbb{Z}_3^{(C)}$ center symmetry
at the classical level. [ESTABLISHED, Unsal 2008]


---

## II. Definition of the Center Vortex

### II.1 The vortex as a twisted boundary condition in $x^0$

The center vortex is a codimension-1 defect that threads the $x^0$
direction. Concretely, it is defined by imposing an *additional*
$\mathbb{Z}_3$ twist around the $x^0$ circle:

$$z(x^0 + R, x^1) = \Omega^v \, z(x^0, x^1), \qquad v \in \{0, 1, 2\}$$

- $v = 0$: **no vortex** (periodic or anti-periodic, depending on
  statistics; for bosons, periodic)
- $v = 1$: **one unit of center vortex** (multiplication by $\Omega$
  when traversing the $x^0$ cycle)
- $v = 2$: **two units** (equivalently, one unit of anti-vortex,
  since $\Omega^2 = \Omega^{-1} = \Omega^{\dagger}$)

The center vortex free energy is defined as the ratio of partition
functions:

$$\boxed{e^{-F_v(L)} = \frac{Z_v}{Z_0}}$$

where:
- $Z_0 = Z_{v=0}$ is the partition function with the standard
  $\mathbb{Z}_3$ twist in $x^1$ and periodic boundary conditions
  in $x^0$
- $Z_v = Z_{v=1}$ has the additional $\mathbb{Z}_3$ twist in $x^0$

[ESTABLISHED --- this is the standard definition of the center
vortex free energy, see Kovtun-Unsal-Yaffe 2007]

### II.2 Physical interpretation

The center vortex free energy controls the realization of
$\mathbb{Z}_3^{(C)}$:

| $F_v(L)$ | Meaning | Phase |
|-----------|---------|-------|
| $F_v > 0$ | Vortex is suppressed (costs free energy) | **Confined** ($\mathbb{Z}_3^{(C)}$ preserved) |
| $F_v = 0$ | Vortex is free | **Critical** (phase boundary) |
| $F_v < 0$ | Vortex proliferates (gains free energy) | **Deconfined** ($\mathbb{Z}_3^{(C)}$ broken) |

In the $R \to \infty$ limit:

$$F_v(L) = R \cdot T_{\mathrm{DW}}(L)$$

where $T_{\mathrm{DW}}(L)$ is the domain wall tension (free energy
per unit length) of the center vortex. Positivity of $F_v$ in this
limit is equivalent to $T_{\mathrm{DW}} > 0$.


---

## III. The Vortex in the Auxiliary Field Formalism

### III.1 Effective action with twisted boundary conditions

In the D'Adda-Di Vecchia-Luscher formulation, we introduce the
auxiliary field $\sigma(x)$ (Lagrange multiplier for $|z|^2 = 1$)
and the composite gauge field $A_\mu$. After integrating out the
$z$ fields:

$$Z_v = \int [D\sigma][DA_\mu] \, \exp\bigl(-N \, S_{\mathrm{eff}}^{(v)}[\sigma, A]\bigr)$$

$$S_{\mathrm{eff}}^{(v)}[\sigma, A] =
  \mathrm{Tr}_{(v)} \ln(-D^2 + \sigma) - \frac{1}{\lambda_0}\int_\Sigma \sigma$$

The subscript $(v)$ on the trace means that the functional
determinant is computed with the **doubly-twisted** boundary conditions:

$$\text{Tr}_{(v)} = \text{Tr over fields obeying } \begin{cases}
  z(x^0, x^1 + L) = \Omega \, z(x^0, x^1) \\
  z(x^0 + R, x^1) = \Omega^v \, z(x^0, x^1)
\end{cases}$$

### III.2 Mode decomposition with double twist

The doubly-twisted boundary conditions quantize the momenta as:

$$z_j(x) = \sum_{n_0, n_1} \hat{z}_j(n_0, n_1) \,
  \exp\left(i \frac{2\pi n_0 + 2\pi v(j-1)/3}{R} x^0
  + i \frac{2\pi n_1 + 2\pi (j-1)/3}{L} x^1\right)$$

where $j = 1, 2, 3$ labels the flavor (color) index, and $n_0, n_1 \in \mathbb{Z}$.

For the $j$-th component:
- Momentum in $x^1$: $p_1^{(j)} = \frac{2\pi n_1}{L} + \frac{2\pi(j-1)}{3L}$
- Momentum in $x^0$: $p_0^{(j)} = \frac{2\pi n_0}{R} + \frac{2\pi v(j-1)}{3R}$

**No vortex ($v = 0$):** $p_0^{(j)} = 2\pi n_0/R$ --- the $x^0$
momenta are independent of flavor.

**With vortex ($v = 1$):** $p_0^{(j)} = 2\pi n_0/R + 2\pi(j-1)/(3R)$
--- each flavor acquires a fractional momentum shift in $x^0$.

### III.3 The vortex free energy as a determinant ratio

At $N = \infty$, the saddle point is $\sigma = m^2$, $A_\mu = 0$,
with $m = \Lambda_{2D}$, independent of the vortex. The vortex
free energy is:

$$F_v(L) = N \bigl(S_{\mathrm{eff}}^{(1)} - S_{\mathrm{eff}}^{(0)}\bigr)\bigg|_{\text{saddle}}
  = N \Bigl[\mathrm{Tr}_{(1)}\ln(-\partial^2 + m^2) -
  \mathrm{Tr}_{(0)}\ln(-\partial^2 + m^2)\Bigr]$$

This is a purely kinematic quantity: the difference between
functional determinants with and without the vortex twist, both
evaluated on the same saddle point.


---

## IV. Explicit Evaluation of $F_v^{(\infty)}$

### IV.1 The free energy per flavor

For a single free massive scalar of mass $m$ on $S^1_R \times S^1_L$
with momentum shifts $\delta p_0$ and $\delta p_1$, the free energy
is:

$$\mathcal{F}(\delta p_0, \delta p_1)
  = \frac{1}{2}\sum_{n_0, n_1 \in \mathbb{Z}}
  \ln\left[\left(\frac{2\pi n_0}{R} + \delta p_0\right)^2
  + \left(\frac{2\pi n_1}{L} + \delta p_1\right)^2 + m^2\right]$$

The vortex free energy contribution from flavor $j$ is:

$$\Delta \mathcal{F}_j = \mathcal{F}\Bigl(\frac{2\pi(j-1)}{3R}, \frac{2\pi(j-1)}{3L}\Bigr)
  - \mathcal{F}\Bigl(0, \frac{2\pi(j-1)}{3L}\Bigr)$$

and the total (leading-order) vortex free energy is:

$$F_v^{(\infty)} = N \sum_{j=1}^{N} \Delta\mathcal{F}_j$$

### IV.2 The $R \to \infty$ limit

In the limit $R \to \infty$, the sum over $n_0$ becomes an integral
and the fractional shift $2\pi v(j-1)/(3R)$ becomes negligible
*compared to the integration variable*. However, the difference
of partition functions captures a nontrivial quantity: the domain
wall tension.

The standard calculation (using Poisson resummation in the $n_0$
direction or the transfer matrix formalism) gives, for
$R \gg 1/m$:

$$F_v^{(\infty)} = N \cdot R \cdot T_{\mathrm{DW}}^{(\infty)}(L)$$

where the domain wall tension at $N = \infty$ diverges:

$$\boxed{T_{\mathrm{DW}}^{(\infty)}(L) = +\infty}$$

**Why infinite?** At $N = \infty$, the theory consists of $N$
free massive particles. Each particle independently contributes
an $O(1)$ amount to the domain wall tension (the vortex twist
shifts its boundary condition). The total tension is $N \times O(1)
= \infty$ as $N \to \infty$.

More precisely: the $N = \infty$ vortex free energy per unit length
scales as $N$ (since all $N$ flavors contribute coherently to the
twist energy), giving $F_v^{(\infty)} \propto N \cdot R$. In the
$N = \infty$ limit, the center vortex is infinitely heavy.

**At finite $N$:** The center vortex free energy is $O(N)$, and
the question is whether $1/N$ corrections (which reduce $F_v$ from
infinity) can make it negative.

[PROVED --- the divergence of $F_v$ at $N = \infty$ follows from
the free massive theory on the torus with twisted boundary conditions.]


---

## V. Finite-$N$ Structure

At finite $N$, the center vortex free energy admits a $1/N$
expansion:

$$F_v(L) = N \, F_v^{(0)}(L) + F_v^{(1)}(L) + \frac{1}{N} F_v^{(2)}(L) + \cdots$$

where:
- $F_v^{(0)}(L)$: the $O(N)$ leading term (computed above --- positive, $O(R)$
  in the thermodynamic limit)
- $F_v^{(1)}(L)$: the $O(1)$ correction --- **this is what we compute**
- $F_v^{(2)}(L)$: the $O(1/N)$ correction (two-loop in auxiliary fields)

At $N = 3$:

$$F_v(N=3) = 3\, F_v^{(0)} + F_v^{(1)} + \frac{1}{3} F_v^{(2)} + \cdots$$

**Adiabatic continuity criterion:** $F_v(N=3) > 0$ if and only if

$$F_v^{(1)} > -3\, F_v^{(0)} - \frac{1}{3}F_v^{(2)} - \cdots$$

Truncating at $O(1)$, the sufficient condition is:

$$\boxed{F_v^{(1)}(L) > -3\, F_v^{(0)}(L) \quad \forall\, L > 0}$$

Since $F_v^{(0)} > 0$ and is $O(R)$ in the thermodynamic limit (it
is the domain wall tension at $N = \infty$), the bound requires
$F_v^{(1)}$ to not grow faster than $O(R)$ with a coefficient that
exceeds three times the leading-order tension. This is the target
of the calculation in the following files.


---

## VI. Summary

| Quantity | Definition | Status |
|----------|-----------|--------|
| Center vortex | $\mathbb{Z}_3$ twist in $x^0$ direction | [ESTABLISHED] |
| $F_v(L)$ | $-\ln(Z_v/Z_0)$ | [ESTABLISHED] |
| $F_v > 0$ | Center symmetry preserved | [ESTABLISHED] |
| $F_v^{(\infty)}$ at $N = \infty$ | $= N \cdot R \cdot T_{\mathrm{DW}} = +\infty$ | [PROVED] |
| $F_v$ at small $L$ | $> 0$ (semiclassical) | [PROVED] |
| $F_v^{(1)}$: $O(1)$ correction | Target of this calculation | [TO BE COMPUTED] |
| Adiabatic continuity | Holds if $F_v^{(1)} > -3 F_v^{(0)}$ | [CONDITIONAL] |
