# 02. Auxiliary Field Formalism and Sigma Propagator

## I. The D'Adda--Di Vecchia--Luscher Formulation

### I.1 Starting point

The CP^{N-1} model in 2D has the Lagrangian:

$$\mathcal{L} = |D_\mu z|^2, \qquad D_\mu = \partial_\mu - i A_\mu, \qquad |z|^2 = 1$$

where $A_\mu = -i \bar{z} \cdot \partial_\mu z$ is the composite U(1) gauge
field and $z = (z_1, \ldots, z_N)$ lives on $S^{2N-1}$ projected to
$\mathbb{CP}^{N-1}$.

We enforce the constraint $|z|^2 = 1$ with a Lagrange multiplier
$\sigma(x)$:

$$\mathcal{L} = |D_\mu z|^2 + \sigma(|z|^2 - 1)$$

and promote $A_\mu$ and $\sigma$ to independent integration variables.
The partition function is:

$$Z = \int [Dz][D\bar{z}][D\sigma][DA_\mu] \exp\left(-\int d^2x \left[\bar{z}(-D^2 + \sigma)z - \sigma\right]\right)$$

[ESTABLISHED -- D'Adda, Di Vecchia, Luscher 1978]


### I.2 Integrating out $z$: the Hubbard--Stratonovich step

The $z$ integral is Gaussian. Each of the $N$ components contributes
identically (up to boundary condition shifts from the Z_3 twist), giving:

$$Z = \int [D\sigma][DA_\mu] \exp\left(-N S_{\text{eff}}[\sigma, A]\right)$$

$$S_{\text{eff}}[\sigma, A] = \text{Tr}\ln(-D^2 + \sigma) - \frac{1}{\lambda_0}\int d^2x\, \sigma$$

where $\lambda_0 = g^2 N$ is the 't Hooft coupling (held fixed as
$N \to \infty$) and the trace is over a single flavor with the
appropriate boundary conditions. The factor of $N$ in front makes this
a large-$N$ saddle point problem.

[ESTABLISHED]

---

## II. Saddle Point at $N = \infty$

### II.1 The gap equation

Setting $A_\mu = 0$ (justified at leading order) and $\sigma = \sigma_0 = \text{const}$,
the saddle point equation $\delta S_{\text{eff}}/\delta \sigma = 0$ reads:

$$\frac{1}{\lambda_0} = \int \frac{d^2p}{(2\pi)^2} \frac{1}{p^2 + \sigma_0}$$

The integral is UV-divergent and requires regularization. Using a UV
cutoff $\Lambda_{\text{UV}}$:

$$\frac{1}{\lambda_0} = \frac{1}{4\pi}\ln\frac{\Lambda_{\text{UV}}^2}{\sigma_0}$$

Defining the dynamical mass scale via dimensional transmutation:

$$\Lambda^2 \equiv \Lambda_{\text{UV}}^2 \, e^{-4\pi/\lambda_0}$$

the gap equation yields:

$$\boxed{\sigma_0 = m^2 = \Lambda^2}$$

The $z$ fields acquire a dynamical mass $m = \Lambda$ through
dimensional transmutation. This mass is non-perturbative in the
coupling $\lambda_0$.

[PROVED -- standard large-$N$ result, see Witten 1979]


### II.2 Independence from vortex sector

A critical point: at $N = \infty$, the saddle point value
$\sigma_0 = m^2$ is **independent of the boundary conditions**
(vortex or no vortex). This is because $\sigma_0$ is determined
by the gap equation, which involves the UV-dominated momentum integral.
The twist modifies IR momenta (shifts of order $1/L$ or $1/R$) but
does not affect the UV divergence that determines $\sigma_0$.

More precisely: the gap equation on $S^1_L \times S^1_R$ reads

$$\frac{1}{\lambda_0} = \frac{1}{LR}\sum_{n_0, n_1}\frac{1}{p_{n_0}^2 + p_{n_1}^2 + \sigma_0}$$

The vortex shifts $p_{n_0} \to p_{n_0} + 2\pi v(j-1)/(3R)$. For
$R \to \infty$, these shifts are $O(1/R)$ and vanish, leaving
$\sigma_0$ unchanged.

[PROVED -- the saddle point is twist-independent at $N = \infty$]


---

## III. Fluctuations Around the Saddle: The Sigma Propagator

### III.1 Expanding around the saddle

Write $\sigma(x) = m^2 + \frac{1}{\sqrt{N}}\tilde{\sigma}(x)$.
(The $1/\sqrt{N}$ is chosen so that $\tilde{\sigma}$ has $O(1)$
fluctuations.) The effective action expanded to quadratic order in
$\tilde{\sigma}$ gives the inverse sigma propagator.

The one-loop polarization bubble (the $z$ loop with two $\sigma$
insertions) in infinite volume is:

$$\Pi(p) = \int \frac{d^2k}{(2\pi)^2} \frac{1}{(k^2 + m^2)((k+p)^2 + m^2)}$$

This is the standard one-loop bubble integral in 2D:

$$\Pi(p) = \frac{1}{4\pi} \frac{1}{\sqrt{p^2(p^2 + 4m^2)}} \cdot 2\,\text{arcsinh}\!\left(\frac{|p|}{2m}\right)$$

Wait -- let me be more careful. The exact result of the bubble in 2D is:

$$\Pi(p) = \frac{1}{2\pi\sqrt{p^2(p^2 + 4m^2)}}\,\ln\frac{\sqrt{p^2 + 4m^2} + \sqrt{p^2}}{\sqrt{p^2 + 4m^2} - \sqrt{p^2}}$$

This simplifies. Denoting $|p| = p$ and using $\text{arcsinh}(x) = \ln(x + \sqrt{1+x^2})$:

$$\Pi(p) = \frac{1}{2\pi\sqrt{p^2 + 4m^2}\cdot p}\,\cdot\,2\,\text{arcsinh}\!\left(\frac{p}{2m}\right)$$

### III.2 The sigma propagator

The full sigma propagator at leading order in $1/N$ is:

$$D_\sigma(p) = \frac{1}{N\,\Pi(p)}$$

For the physics we care about (the vortex free energy at $O(1)$),
we need $D_\sigma$ at momenta $p \sim 1/L$, where $L$ is the
compactification scale. In the regime $m L \gg 1$ (which is where
adiabatic continuity is hardest to prove), the relevant momenta
satisfy $p \ll m$, so we can expand:

For $p \ll 2m$:

$$\Pi(p) \approx \frac{1}{2\pi \cdot 2m \cdot p}\cdot 2\cdot \frac{p}{2m} = \frac{1}{4\pi m^2}$$

More carefully, expanding $\text{arcsinh}(p/(2m))$ for small $p/(2m)$:

$$\text{arcsinh}\!\left(\frac{p}{2m}\right) = \frac{p}{2m} - \frac{1}{6}\left(\frac{p}{2m}\right)^3 + \cdots$$

$$\Pi(p) = \frac{1}{2\pi\sqrt{4m^2 + p^2}\cdot p}\cdot 2\left[\frac{p}{2m} - \frac{p^3}{48m^3} + \cdots\right]$$

$$= \frac{1}{2\pi m\sqrt{4m^2 + p^2}}\left[1 - \frac{p^2}{24m^2} + \cdots\right]$$

$$\approx \frac{1}{4\pi m^2}\left(1 - \frac{p^2}{8m^2} + \cdots\right)\left(1 - \frac{p^2}{24m^2} + \cdots\right)$$

$$= \frac{1}{4\pi m^2}\left(1 - \frac{p^2}{6m^2} + \cdots\right)$$

So:

$$D_\sigma(p) = \frac{1}{N\,\Pi(p)} \approx \frac{4\pi m^2}{N}\left(1 + \frac{p^2}{6m^2} + \cdots\right)$$

### III.3 The exact propagator for general $p$

For the full calculation, we need the exact form. The sigma
propagator is:

$$\boxed{D_\sigma(p) = \frac{1}{N}\cdot\frac{2\pi\, p\,\sqrt{p^2 + 4m^2}}{\text{arcsinh}(p/(2m))}}$$

At $p = 0$: $D_\sigma(0) = 4\pi m^2/N$.

For $p \gg 2m$: $D_\sigma(p) \approx \frac{2\pi p^2}{N\,\ln(p/m)}$.

**Key property:** The sigma field is *not* a propagating particle in
the usual sense. It has no pole on the real axis. The "sigma propagator"
is actually the resummed bubble chain, and $\sigma$ acts as a
collective mode mediating interactions between the $z$ particles.

The sigma field has a two-particle threshold at $p^2 = -4m^2$
(i.e., it can decay into a $z\bar{z}$ pair when the invariant mass
exceeds $2m$). There is no stable sigma particle.

[COMPUTED -- the bubble integral and propagator are standard; see
e.g. Campostrini-Rossi 1992 or D'Adda-Di Vecchia-Luscher 1978]


---

## IV. Role of the Sigma Field in the Vortex Calculation

### IV.1 The $O(1)$ correction mechanism

At $N = \infty$, the sigma field is frozen at its saddle value
$\sigma_0 = m^2$. The vortex free energy is $O(N)$ and positive
(established in 01-vortex-setup.md).

At $O(1)$ (next-to-leading order in $1/N$), the sigma field
fluctuates. These fluctuations modify the vortex free energy through:

1. **The sigma determinant itself:** The quadratic fluctuation
   determinant of $\sigma$ depends on the boundary conditions.
   The vortex modifies the $z$-propagator, which enters the bubble
   $\Pi(p)$, which sets $D_\sigma$.

2. **Back-reaction on $z$:** The fluctuating $\sigma$ mediates
   an effective interaction $\sim (1/N)\bar{z}z \cdot D_\sigma \cdot \bar{z}z$
   between the $z$ particles, modifying their contribution to $F_v$.

The dominant contribution at $O(1)$ is:

$$F_v^{(1)} = \frac{1}{2}\left[\text{Tr}_{(1)}\ln D_\sigma^{-1} - \text{Tr}_{(0)}\ln D_\sigma^{-1}\right]$$

where the traces are over the sigma field modes with the boundary
conditions **induced** by the vortex.

### IV.2 Boundary conditions for sigma

What boundary conditions does $\sigma$ obey? Since
$\sigma \sim \bar{z}\cdot z$ is a color singlet, it is **periodic**
in both directions, regardless of the vortex.

However, the inverse propagator $\Pi(p)$ itself depends on the
boundary conditions of the $z$ fields that run in the loop. With
the vortex present, the $z$ propagator is modified, so
$\Pi^{(v)}(p) \neq \Pi^{(0)}(p)$ at finite volume.

This is the key subtlety: the sigma field has periodic boundary
conditions, but its dynamics (its propagator) depend on whether
the vortex is present, through the $z$-loop.

[ESTABLISHED -- this is the structure of the $1/N$ expansion]


---

## V. Summary

| Quantity | Expression | Status |
|----------|-----------|--------|
| Saddle point | $\sigma_0 = m^2 = \Lambda^2$ | [PROVED] |
| Saddle independent of vortex | Yes, at $N = \infty$ | [PROVED] |
| Sigma propagator (exact) | $D_\sigma(p) = \frac{2\pi p\sqrt{p^2+4m^2}}{N\,\text{arcsinh}(p/(2m))}$ | [COMPUTED] |
| Sigma propagator ($p \ll m$) | $D_\sigma \approx 4\pi m^2/N$ | [COMPUTED] |
| Sigma boundary conditions | Periodic (color singlet) | [ESTABLISHED] |
| $F_v^{(1)}$ structure | Determinant ratio of sigma with modified bubble | [ESTABLISHED] |
