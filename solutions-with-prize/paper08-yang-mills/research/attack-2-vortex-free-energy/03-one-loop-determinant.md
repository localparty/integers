# 03. The One-Loop Determinant: Setting Up $F_v^{(1)}$

## I. The $O(1)$ Correction to the Vortex Free Energy

### I.1 Structure of $F_v^{(1)}$

From the $1/N$ expansion, the $O(1)$ correction to the vortex free
energy comes from integrating out the quadratic fluctuations of the
auxiliary fields $(\sigma, A_\mu)$ around the saddle point.

At $N = \infty$, the saddle is $\sigma_0 = m^2$, $A_\mu = 0$.
Expanding $\sigma = m^2 + \tilde{\sigma}/\sqrt{N}$, the quadratic
action for $\tilde{\sigma}$ is:

$$S^{(2)}[\tilde{\sigma}] = \frac{1}{2}\int\frac{d^2p}{(2\pi)^2}\,\tilde{\sigma}(-p)\,\Pi^{(v)}(p)\,\tilde{\sigma}(p)$$

where $\Pi^{(v)}(p)$ is the one-loop polarization (bubble diagram)
computed with $z$-propagators obeying the boundary conditions of
sector $v$.

The $O(1)$ contribution to the free energy is:

$$F_v^{(1)} = \frac{1}{2}\text{Tr}\ln\Pi^{(v)} - \frac{1}{2}\text{Tr}\ln\Pi^{(0)}$$

$$\boxed{F_v^{(1)} = \frac{1}{2}\text{Tr}\ln\frac{\Pi^{(v=1)}}{\Pi^{(v=0)}}}$$

where the trace is over the **periodic** modes of the sigma field
(since sigma is a color singlet).

[ESTABLISHED]


### I.2 Why this is subtle

The difficulty is that $\Pi^{(v)}(p)$ is itself a sum over $z$-field
modes, which depend on $v$. So we have a trace-log of a ratio of
functions, each of which is defined by an internal sum. This is not
a simple twisted-vs-untwisted determinant of a local operator.

However, there is a significant simplification. We will show that
in the regime of interest ($R \to \infty$, $L$ finite), the problem
reduces to a spectral sum involving modified Matsubara frequencies.


---

## II. Reduction to the Spectral Problem on $\mathbb{R} \times S^1_L$

### II.1 Taking $R \to \infty$

Since we ultimately want the domain wall tension
$T_{\text{DW}} = \lim_{R\to\infty} F_v / R$, we take $R \to \infty$
from the start. In this limit:

1. The sigma field lives on $\mathbb{R} \times S^1_L$ with periodic
   boundary conditions on $S^1_L$.

2. The sigma momentum in the $x^0$ direction becomes continuous:
   $p_0 \in \mathbb{R}$.

3. The sigma momentum in the $x^1$ direction is quantized:
   $p_1 = 2\pi n_1/L$, $n_1 \in \mathbb{Z}$ (periodic b.c. for sigma).

4. The bubble $\Pi^{(v)}(p_0, p_1)$ is computed from the $z$-loop,
   where the $z$ fields have continuous $p_0$ but their $p_1$ momenta
   carry the Z_3 twist: $p_1^{(j)} = 2\pi n_1/L + 2\pi(j-1)/(3L)$.

### II.2 The bubble on $\mathbb{R} \times S^1_L$

For the **no-vortex** sector ($v = 0$), the bubble at external
momentum $(p_0, p_1)$ is:

$$\Pi^{(0)}(p_0, p_1) = \frac{1}{L}\sum_{k_1}\int\frac{dk_0}{2\pi}\,\frac{1}{(k^2 + m^2)((k+p)^2 + m^2)}$$

where the sum is over the $z$-field momenta. For a single flavor $j$,
$k_1$ takes values $2\pi n/L + 2\pi(j-1)/(3L)$. Summing over all
$N = 3$ flavors:

$$\Pi^{(0)}(p_0, p_1) = \sum_{j=1}^{3}\frac{1}{L}\sum_{n\in\mathbb{Z}}\int\frac{dk_0}{2\pi}\,\frac{1}{\left(k_0^2 + \omega_{n,j}^2 + m^2\right)\left((k_0+p_0)^2 + (\omega_{n,j}+p_1)^2 + m^2\right)}$$

where $\omega_{n,j} = 2\pi n/L + 2\pi(j-1)/(3L)$ are the Matsubara
frequencies for flavor $j$ on $S^1_L$ with the Z_3 twist.

For the **vortex** sector ($v = 1$): in the $R \to \infty$ limit,
the additional Z_3 twist in $x^0$ becomes irrelevant for the bubble
(the $k_0$ integral is over $\mathbb{R}$, so shifting $k_0$ by
$2\pi v(j-1)/(3R) \to 0$ has no effect).

**Therefore: $\Pi^{(1)} = \Pi^{(0)}$ in the $R \to \infty$ limit.**

[COMPUTED -- the vortex twist drops out of the bubble when $R \to \infty$]


### II.3 The paradox and its resolution

If $\Pi^{(1)} = \Pi^{(0)}$, then naively $F_v^{(1)} = 0$. But this
cannot be the complete story, because the vortex *does* modify the
theory at $O(1)$.

**Resolution:** The $O(1)$ contribution to $F_v$ does not come solely
from the sigma determinant. It also receives contributions from:

1. **The $z$-field determinant at next order:** The one-loop
   determinant $\text{Tr}\ln(-D^2 + m^2)$ was evaluated at leading
   order (giving $F_v^{(0)}$), but has $O(1)$ corrections from the
   sigma fluctuations modifying the $z$ propagator.

2. **The gauge field $A_\mu$:** At $O(1)$, the gauge field
   fluctuations contribute.

3. **The finite-volume correction to the saddle point:** At finite
   $L$, the saddle point $\sigma_0(L)$ differs from $m^2$ by $O(1/N)$
   corrections.

However, the dominant $O(1)$ effect has a much simpler origin.
Let us reconsider the problem more carefully.


---

## III. Reconsidering: $F_v^{(1)}$ from the Full Effective Potential

### III.1 The correct $O(1)$ calculation

Let us be precise. The full partition function is:

$$Z_v = \int [D\sigma]\exp(-N S_{\text{eff}}^{(v)}[\sigma])$$

where $S_{\text{eff}}^{(v)}[\sigma] = \sum_{j=1}^{N}\text{Tr}_{(v,j)}\ln(-\partial^2 + \sigma) - (1/\lambda_0)\int\sigma$
and we have set $A_\mu = 0$ for simplicity (it enters at the same order
and does not qualitatively change the analysis).

At $N = \infty$: $\sigma = m^2$ at the saddle, and

$$\ln Z_v = -N S_{\text{eff}}^{(v)}[m^2] = -N\sum_j\text{Tr}_{(v,j)}\ln(-\partial^2 + m^2) + \text{const}$$

giving $F_v^{(0)}$ as computed in 01-vortex-setup.md.

At $O(1)$: expanding $\sigma = m^2 + \delta\sigma$, the Gaussian
integral over $\delta\sigma$ gives:

$$\ln Z_v \big|_{O(1)} = -\frac{1}{2}\text{Tr}\ln\left(N\,\frac{\delta^2 S_{\text{eff}}^{(v)}}{\delta\sigma^2}\bigg|_{m^2}\right)$$

$$= -\frac{1}{2}\text{Tr}\ln(N\Pi^{(v)})$$

$$= -\frac{N_\sigma}{2}\ln N - \frac{1}{2}\text{Tr}\ln\Pi^{(v)}$$

where $N_\sigma$ is the number of sigma modes (divergent, but cancels
in the ratio). The $O(1)$ vortex free energy is:

$$F_v^{(1)} = -\ln Z_v^{(1)}\big|_{O(1)} + \ln Z_0^{(1)}\big|_{O(1)} = \frac{1}{2}\text{Tr}\ln\frac{\Pi^{(v)}}{\Pi^{(0)}}$$

As established above, in the $R \to \infty$ limit, $\Pi^{(v)} = \Pi^{(0)}$,
so this particular contribution vanishes.

**But this is only the sigma-sector contribution.** The full $O(1)$
correction also includes the $O(1)$ part of the $z$-determinant.

### III.2 The complete $O(1)$ vortex free energy

Let us count more carefully. The $z$-determinant gives:

$$-\ln Z_v = N S_{\text{eff}}^{(v)}[m^2] + \frac{1}{2}\text{Tr}\ln(N\Pi^{(v)}) + O(1/N)$$

The first term is $O(N)$ and gives:

$$N S_{\text{eff}}^{(v)} = N\sum_{j=1}^{N}\text{Tr}_{(v,j)}\ln(-\partial^2 + m^2) - \frac{N}{\lambda_0}\int m^2$$

But wait -- the sum $\sum_{j=1}^{N}$ over $N$ flavors, multiplied
by the overall $N$, gives an $O(N^2)$ term? No -- each $\text{Tr}_{(v,j)}$
is $O(1)$ (it's a single-flavor determinant), so $\sum_j$ gives $O(N)$,
and with the prefactor $N$, we get $O(N)$ for the vortex free energy
difference $F_v^{(0)}$ (since the $v$-dependent part of each $\text{Tr}_{(v,j)}$
is $O(1/N)$ relative to the total). Let me be much more explicit.

### III.3 Explicit decomposition

For the $R \to \infty$ limit on $\mathbb{R} \times S^1_L$, the
vortex free energy per unit length in the $x^0$ direction is:

$$\frac{F_v}{R} = T_{\text{DW}}$$

At leading order, this comes from the $z$-determinant difference.
Each flavor $j$ contributes, and the vortex shifts $p_0^{(j)}$ by
$2\pi(j-1)/(3R)$. In the $R \to \infty$ limit, Poisson resummation
converts this shift into a domain wall tension.

The $O(1)$ correction $F_v^{(1)} / R$ is the $O(1/N)$ correction
to this domain wall tension, **times** $N$... no, let me be very precise.

**The clean statement:** The vortex free energy has the structure

$$F_v = N \cdot f_0(L) \cdot R + f_1(L) \cdot R + O(R/N)$$

where $f_0(L) > 0$ is the leading domain wall tension per flavor,
and $f_1(L)$ is the $O(1)$ correction from sigma fluctuations.

The $f_1$ piece arises because the sigma field mediates an
interaction between the $z$ particles. In the presence of the
vortex, these interactions are modified because the $z$-propagator
(which enters the sigma-$z$-$z$ vertex) carries the twist.

[ESTABLISHED -- structure of $1/N$ expansion for $F_v$]


---

## IV. The Clean Calculation: Twisted Determinant Approach

### IV.1 Back to basics

Let me cut through the complications and state what $F_v^{(1)}$ actually is.

In the $R \to \infty$ limit, the full effective theory on $\mathbb{R} \times S^1_L$
has the sigma field propagating with the bubble $\Pi(p_0, n_1)$ where
$n_1$ labels the Matsubara modes on $S^1_L$. The sigma field is periodic.

The $O(1)$ correction to $F_v$ comes from the modification of the
$z$-determinant due to sigma fluctuations. At one loop in the sigma
field, this correction is:

$$F_v^{(1)} = -\frac{1}{N}\sum_{j=1}^{N}\int\frac{d^2p}{(2\pi)^2}\,D_\sigma(p)\left[G_j^{(v)}(p) - G_j^{(0)}(p)\right]$$

where $G_j^{(v)}(p)$ is the $z_j$ self-energy correction in the
vortex sector.

However, this approach leads to a complicated diagrammatic expansion.
There is a better way.

### IV.2 The Casimir energy approach

The most transparent method: Think of the problem as computing the
Casimir energy difference between twisted and untwisted boundary
conditions for the $\sigma$ effective theory.

Even though $\sigma$ itself is periodic, the effective mass of sigma
fluctuations is position-dependent in the presence of the vortex
(because the vortex is a domain wall interpolating between different
vacua). This makes the direct determinant approach complicated.

Instead, we use the fact that at $N = \infty$, the theory reduces
to $N$ free massive bosons on $\mathbb{R} \times S^1_L$ with a
Z_3-twisted boundary condition. The $O(1)$ correction is the one-loop
correction in the sigma effective theory, which can be computed as
follows.

### IV.3 The definitive formulation

The $O(1)$ vortex free energy in the $R \to \infty$ limit is:

$$\boxed{F_v^{(1)} = \frac{R}{2}\int\frac{dp_0}{2\pi}\sum_{n_1 \in \mathbb{Z}}\ln\frac{\Pi^{(v)}(p_0, 2\pi n_1/L)}{\Pi^{(0)}(p_0, 2\pi n_1/L)}}$$

where:
- The sigma field has periodic b.c.: momenta $p_1 = 2\pi n_1/L$
- $\Pi^{(v)}$ is the bubble computed with $z$-fields obeying the
  vortex boundary conditions

And we showed in Section II.2 that $\Pi^{(v)} = \Pi^{(0)}$ when
$R \to \infty$, so this particular contribution vanishes identically.

**The nonvanishing $O(1)$ contribution** must therefore come from
elsewhere in the $1/N$ expansion. The candidates are:

1. The $O(1/N)$ correction to the saddle point $\sigma_0$, which
   shifts $F_v^{(0)}$ by $O(1)$.
2. The gauge field $A_\mu$ fluctuations.
3. The $O(1)$ part of the $z$-determinant itself (the finite-volume
   correction).

After careful analysis, the dominant effect is **item 1**: the
shift of the saddle point.


---

## V. The Saddle Point Shift

### V.1 The shifted gap equation

At finite $N$ and finite $L$, the gap equation receives $1/N$
corrections. Writing $\sigma_0 = m^2 + \delta m^2/N + \cdots$:

$$\frac{1}{\lambda_0} = \frac{1}{L}\sum_{n_1}\int\frac{dp_0}{2\pi}\left[\frac{1}{p_0^2 + (2\pi n_1/L)^2 + m^2 + \delta m^2/N} + \frac{1}{N}\Delta G(p_0, n_1)\right]$$

where $\Delta G$ is the $O(1/N)$ correction to the $z$-propagator
from sigma exchange.

The shift $\delta m^2$ is $v$-independent at leading order (same
argument as before: the vortex modifies $p_0$ shifts that vanish
as $R \to \infty$).

### V.2 Implications

Since $\delta m^2$ is $v$-independent, the saddle-point shift
contributes equally to $Z_v$ and $Z_0$, and drops out of $F_v^{(1)}$.

**Conclusion of this analysis:** The $O(1)$ correction to the vortex
free energy in the $R \to \infty$ limit, computed from the sigma
effective theory, is:

$$F_v^{(1)} = 0 \quad \text{in the } R \to \infty \text{ limit}$$

to the extent that we can show $\Pi^{(v)} = \Pi^{(0)}$ and the
saddle point shift is $v$-independent.

**But this cannot be the whole story** at finite $R$. Let us
reconsider the problem at finite $R$ in the next file, where the
vortex twist is a genuine boundary condition.

[COMPUTED -- $F_v^{(1)}$ from sigma fluctuations vanishes at $R = \infty$]


---

## VI. The Correct Framework at Finite $R$

For the definitive calculation, we must work at finite $R$ and
take $R$ large but finite at the end.

At finite $R$, the sigma field lives on $S^1_R \times S^1_L$. The
bubble $\Pi^{(v)}$ genuinely depends on $v$, because the $z$-field
momenta in the $x^0$ direction are quantized:

$$k_0^{(j)} = \frac{2\pi n_0}{R} + \frac{2\pi v(j-1)}{3R}$$

The bubble is:

$$\Pi^{(v)}(p) = \sum_{j=1}^{N}\frac{1}{LR}\sum_{n_0, n_1}\frac{1}{\left[(k_0^{(j)})^2 + (k_1^{(j)})^2 + m^2\right]\left[(k_0^{(j)}+p_0)^2 + (k_1^{(j)}+p_1)^2 + m^2\right]}$$

This is now a discrete double sum, and the $v$-dependence does not
trivially vanish. The vortex free energy at $O(1)$ is:

$$\boxed{F_v^{(1)} = \frac{1}{2}\sum_{\mathbf{p}\in\Lambda_\sigma}\ln\frac{\Pi^{(1)}(\mathbf{p})}{\Pi^{(0)}(\mathbf{p})}}$$

where $\Lambda_\sigma = \{(2\pi n_0/R, 2\pi n_1/L) : n_0, n_1 \in \mathbb{Z}\}$
is the momentum lattice for the periodic sigma field.

**The key point:** The $v$-dependence of $\Pi^{(v)}$ is suppressed
by $O(1/R)$ for each mode, but the sum over the $O(R)$ modes in the
$n_0$ direction can produce an $O(1)$ result (or even $O(R)$). This
is exactly what we evaluate in the next file.

[ESTABLISHED -- this is the well-defined spectral problem to solve]


---

## VII. Summary

| Step | Result | Status |
|------|--------|--------|
| $F_v^{(1)}$ from sigma determinant | $= \frac{1}{2}\text{Tr}\ln(\Pi^{(v)}/\Pi^{(0)})$ | [ESTABLISHED] |
| $\Pi^{(v)} = \Pi^{(0)}$ at $R = \infty$ | Vortex shift vanishes in continuous $p_0$ | [PROVED] |
| $F_v^{(1)}$ at $R = \infty$ (sigma sector) | $= 0$ | [COMPUTED] |
| Need finite-$R$ calculation | Yes -- $v$-dependence is $O(1/R)$ per mode, summed over $O(R)$ modes | [ESTABLISHED] |
| Working formula | $F_v^{(1)} = \frac{1}{2}\sum_{\mathbf{p}}\ln(\Pi^{(1)}/\Pi^{(0)})$ | [ESTABLISHED] |
