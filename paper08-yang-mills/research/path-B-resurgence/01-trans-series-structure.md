# 01. The Trans-Series Structure for $\sigma_{\text{phys}}$

This document writes down the explicit trans-series for the physical
string tension $\sigma_{\text{phys}}$ of $SU(N)$ Yang--Mills theory,
defined through the KK theory on $M^4 \times \mathbb{CP}^{N-1}$.
The goal: make the resurgent structure as concrete as possible.


---

## I. The Physical Setup

### I.1 What we want to define

The continuum physical string tension:
$$\sigma_{\text{phys}} = \lim_{a \to 0}
  \frac{\hat{\sigma}(\beta(a))}{a^2}$$

We KNOW $\hat{\sigma}(\beta) > 0$ for $a \gg r_3$ (Sections 21--25).
The lattice continuum limit is OPEN. The resurgence approach
bypasses the lattice entirely: define $\sigma_{\text{phys}}$ directly
as a function of the continuum coupling $g^2$.

### I.2 The coupling and the dynamical scale

The running coupling at energy scale $\mu$:
$$\frac{1}{g^2(\mu)} = b_0 \ln\frac{\mu^2}{\Lambda^2}
  + \frac{b_1}{b_0} \ln\ln\frac{\mu^2}{\Lambda^2} + \ldots$$

with $b_0 = 11N/(48\pi^2)$, $b_1 = 34N^2/(3(16\pi^2)^2)$ for
$SU(N)$.

The dynamical scale $\Lambda$ is the one physical scale of the pure
gauge theory. Dimensional analysis requires:
$$\sigma_{\text{phys}} = c_\sigma \Lambda^2$$

for a dimensionless constant $c_\sigma$. The trans-series computes
$c_\sigma$ as a function of the coupling.


---

## II. The General Trans-Series Ansatz

### II.1 Instanton sectors

The KK theory on $M^4 \times \mathbb{CP}^{N-1}$ has two types of
non-perturbative objects:

**(a) 4D instantons** (BPST-type on $M^4$): action
$S_I = 8\pi^2/g^2$ per topological charge. These exist in any 4D
Yang--Mills theory. The instanton action sets the scale of the
trans-series.

**(b) CP^{N-1} instantons** (holomorphic maps $\mathbb{CP}^1 \to
\mathbb{CP}^{N-1}$): action $S_{CP} = 4\pi/(Ng_{2D}^2)$ in the
worldsheet sigma model. Here $g_{2D}^2 = g^2/(4\pi r_3^2)$ is the
effective 2D coupling. These are the non-perturbative objects of the
confining string.

**(c) Fractional instantons** (in the deformed theory): In the
compactified/deformed CP$^{N-1}$ model, the fundamental instanton
action is $S_I/N = 8\pi^2/(Ng^2)$ (fractional instantons). These
are the objects that make resurgence work in the Dunne--Unsal
framework.

### II.2 The trans-series

The general trans-series for any observable $\mathcal{O}$ in the
theory takes the form:

$$\boxed{\mathcal{O}(g^2) = \sum_{k=0}^{\infty}
  \sum_{l=0}^{\infty} C^k \bar{C}^l \,
  e^{-(k+l) S_I / g^2} \, g^{2\beta_{kl}}
  \sum_{n=0}^{\infty} a_{n}^{(k,l)} \, g^{2n}}$$

where:
- $S_I = 8\pi^2$ is the instanton action (the Bogomolny bound,
  Appendix B)
- $C, \bar{C}$ are trans-series parameters (instanton and
  anti-instanton fugacities)
- $\beta_{kl}$ is the power-law prefactor determined by the
  one-loop determinant around the $(k,l)$-instanton background
- $a_n^{(k,l)}$ are the perturbative coefficients around the
  $(k,l)$-sector

The $(0,0)$ sector ($k = l = 0$) is the perturbative expansion.
The $(k,0)$ sectors are instanton corrections. The $(0,l)$ sectors
are anti-instanton corrections. The $(k,l)$ with $k, l \geq 1$
are instanton--anti-instanton sectors.

### II.3 Simplification for the string tension

The string tension is a vacuum observable (no external sources), so
it is invariant under charge conjugation. The instanton and
anti-instanton contributions must appear symmetrically:
$C = \bar{C}$. Relabelling $m = k + l$ as the total topological
activity:

$$\sigma_{\text{phys}}(g^2) = \Lambda^2
  \sum_{m=0}^{\infty} e^{-m S_I / g^2}
  \sum_{n=0}^{\infty} \sigma_n^{(m)} \, g^{2n}$$

where we absorbed factors of $g^{2\beta_m}$ into the
coefficients $\sigma_n^{(m)}$.


---

## III. Explicit Structure: Sector by Sector

### III.1 The perturbative sector ($m = 0$)

$$\sigma^{(0)}(g^2) = \Lambda^2 \sum_{n=0}^{\infty}
  \sigma_n^{(0)} \, g^{2n}$$

**Status of the coefficients:**

- $\sigma_0^{(0)}$: the leading non-perturbative contribution.
  Since $\sigma \sim \Lambda^2$ and $\Lambda$ itself involves a
  non-perturbative exponential $e^{-1/(2b_0 g^2)}$, the "perturbative
  sector" already contains the non-perturbative scale $\Lambda$.
  [ARGUED]

  More precisely: $\Lambda^2 = \mu^2 \exp(-1/(b_0 g^2(\mu)))
  \times [b_0 g^2(\mu)]^{-b_1/b_0^2}$. The perturbative series is
  in powers of $g^2$ around this non-perturbative backbone.

- $\sigma_n^{(0)}$ for $n \geq 1$: these are the loop corrections.
  They are FINITE at each order in the zeta-regularized KK theory
  (Section 28), but their VALUES are not computable in closed form
  except at low orders.

- **Large-order behavior** [PROVED, Section 29]:
  $$\sigma_n^{(0)} \sim n! \, A^n \, n^{b_0^{(0)}}
    \quad \text{as } n \to \infty$$

  with $A = 1/(8\pi^2)$ (inverse instanton action) and
  $b_0^{(0)} = (11N/3 - 4)/2$ (related to the one-loop determinant).

  The factorial growth $n!$ means the perturbative Borel transform:
  $$B^{(0)}(t) = \sum_{n=0}^{\infty}
    \frac{\sigma_n^{(0)}}{n!} \, t^n$$

  has radius of convergence $R = 1/A = 8\pi^2$ and singularities
  on the positive real axis at $t = 8\pi^2 k$ for $k = 1, 2, \ldots$
  (instanton singularities) and $t = n/(2b_0)$ for $n = 1, 2, \ldots$
  (renormalon singularities).

### III.2 The one-instanton sector ($m = 1$)

$$\sigma^{(1)}(g^2) = \Lambda^2 \, e^{-8\pi^2/g^2}
  \, g^{2\beta_1} \sum_{n=0}^{\infty}
  \sigma_n^{(1)} \, g^{2n}$$

**The prefactor $\beta_1$:**

The power-law prefactor comes from the one-loop fluctuation
determinant around the instanton background. For $SU(N)$ on
$M^4 \times \mathbb{CP}^{N-1}$:

$$g^{2\beta_1} = g^{-4N + 2(N-1)}
  = g^{-2N - 2}$$

The first factor $g^{-4N}$ is the standard 4D instanton zero-mode
count ($4Nk$ for charge $k$, giving $g^{-4Nk}$ from the moduli
space integration). The second factor $g^{2(N-1)}$ comes from the
CP$^{N-1}$ zero modes (the instanton position on the internal
space).

So: $\beta_1 = -(N+1)$ for $SU(N)$.

**The leading coefficient $\sigma_0^{(1)}$:**

This comes from the instanton measure (moduli space integration):
$$\sigma_0^{(1)} = \frac{\mathcal{N}_{\text{inst}}}
  {\text{Vol}(\mathcal{M}_1)}$$

where $\mathcal{M}_1$ is the one-instanton moduli space on
$\mathbb{CP}^{N-1}$ (Appendix B, Section B.3). For $SU(3)$:
$\dim \mathcal{M}_1 = 4$, and the volume is computable.

**The higher coefficients $\sigma_n^{(1)}$:**

These are perturbative corrections around the instanton background.
They can in principle be computed from the fluctuation operator
(the Hessian of the action at the instanton).

[STATUS: The one-instanton contribution is COMPUTABLE in principle
but the explicit values of $\sigma_n^{(1)}$ have not been computed
for this specific theory. For the 2D CP$^{N-1}$ model, the analogous
coefficients ARE computed to high order (Dunne--Unsal 2013).]

### III.3 The instanton--anti-instanton sector ($m = 2$, from $(1,1)$)

$$\sigma^{(1,1)}(g^2) = \Lambda^2 \, e^{-2 \times 8\pi^2/g^2}
  \, g^{2\beta_{11}} \sum_{n=0}^{\infty}
  \sigma_n^{(1,1)} \, g^{2n}$$

This sector is CRUCIAL for resurgence. The instanton--anti-instanton
quasi-zero mode integration produces:

$$\sigma_0^{(1,1)} \propto \int_0^{\infty}
  e^{-S_{I\bar{I}}(R)} \, dR$$

where $S_{I\bar{I}}(R) = 16\pi^2/g^2 - f(R)$ is the
instanton--anti-instanton action at separation $R$, and $f(R)$ is
the interaction potential.

The integral is AMBIGUOUS: the interaction $f(R)$ has a logarithmic
singularity as $R \to 0$ (the instanton and anti-instanton annihilate).
The ambiguity is:

$$\text{Im}\,\sigma_0^{(1,1)} = \pm \frac{\pi i}{S_I}
  \times \sigma_0^{(1)} \times \overline{\sigma_0^{(1)}}$$

[ARGUED --- this follows the standard Bogomolny--Zinn-Justin
prescription.]

### III.4 The key cancellation: resurgence relations

**The Borel ambiguity of the perturbative sector:**

The lateral Borel sum of $\sigma^{(0)}$ along a direction $\theta$
just above or below the positive real axis gives:

$$\mathcal{S}_{\pm}\sigma^{(0)} = \sigma^{(0)}_{\text{Borel}}
  \pm \frac{i}{2} \, \text{Disc}\,\sigma^{(0)}$$

The discontinuity (ambiguity) at the first singularity $t = S_I$
is of order $e^{-S_I/g^2}$:

$$\text{Disc}_{t=S_I}\,\sigma^{(0)} \sim e^{-8\pi^2/g^2}
  \times g^{2\beta_1} \times (\text{polynomial in } g^2)$$

**The resurgence condition:**

$$\boxed{\text{Disc}\,\sigma^{(0)} + 2\pi i \, \sigma^{(1)}
  = 0}$$

More generally, at all orders:
$$\text{Disc}_{t = kS_I}\,\sigma^{(m)} + 2\pi i
  \sum_{\substack{p+q = m+k \\ p > m}}
  \binom{p}{m} \sigma^{(p)} = 0$$

This is the **resurgence relation**: the ambiguity of the Borel sum
at instanton order $m$ is cancelled by the contributions from
instanton orders $m+1, m+2, \ldots$ The total sum
$\sigma_{\text{phys}} = \sum_m \sigma^{(m)}$ is UNAMBIGUOUS.

[STATUS: These relations are CONJECTURED for 4D Yang--Mills on
$M^4 \times \mathbb{CP}^{N-1}$. They are PROVED for the deformed
2D CP$^{N-1}$ model (Dunne--Unsal 2013). They are ARGUED for the
undeformed 2D model by numerical resurgence checks (Dunne--Unsal
2015).]


---

## IV. The Trans-Series for $\sigma_{\text{phys}}$: Full Expression

Combining all sectors, the physical string tension is:

$$\boxed{\sigma_{\text{phys}} = \Lambda^2
  \left[\sum_{n=0}^{\infty} \sigma_n^{(0)} g^{2n}
  + \sum_{k=1}^{\infty} e^{-8\pi^2 k/g^2}
    g^{2\beta_k}
    \sum_{n=0}^{\infty} \sigma_n^{(k)} g^{2n}
  + \sum_{k,l \geq 1} e^{-8\pi^2(k+l)/g^2}
    g^{2\beta_{kl}}
    \sum_{n=0}^{\infty} \sigma_n^{(k,l)} g^{2n}
    \left(\ln g^2\right)^{p_{kl}}
  \right]}$$

where the logarithms $(\ln g^2)^{p_{kl}}$ in the
instanton--anti-instanton sectors arise from quasi-zero mode
integrations. The powers $p_{kl}$ satisfy $p_{kl} \leq \min(k,l)$.

**Key structural features:**

1. Each sector is itself a divergent asymptotic series (factorial
   growth of coefficients). [PROVED, Section 29]

2. The Borel singularities of sector $(k,l)$ are located at
   $t = 8\pi^2 \times \text{integer}$ (instanton singularities)
   and at $t = n/(2b_0)$ (renormalon singularities). [ARGUED,
   standard Lipatov analysis]

3. The resurgence relations link consecutive sectors: the
   ambiguity at order $(k,l)$ cancels against contributions from
   orders $(k+1,l)$, $(k,l+1)$, etc. [CONJECTURED for this theory]

4. If resurgence holds, the trans-series sum
   $\sigma_{\text{phys}} = \mathcal{S}\Gamma$ is:
   - **Unambiguous** (the lateral Borel sums agree)
   - **Finite** (each sector is Borel-resummed, then summed over
     instanton number)
   - **Positive** (if the leading perturbative sector gives a
     positive Borel sum and the instanton corrections are smaller)


---

## V. Comparison with the 2D CP^{N-1} Trans-Series

The 2D CP$^{N-1}$ sigma model provides the template. Its mass gap
has the trans-series (Dunne--Unsal 2013):

$$m_{2D}^2 = \Lambda_{2D}^2 \left[\sum_n c_n^{(0)} g_{2D}^{2n}
  + \sum_{k=1}^{\infty} e^{-4\pi k/(Ng_{2D}^2)}
    \sum_n c_n^{(k)} g_{2D}^{2n} + \ldots\right]$$

The key differences from the 4D trans-series:

| Feature | 2D CP$^{N-1}$ | 4D KK on CP$^{N-1}$ |
|---------|---------------|---------------------|
| Instanton action | $4\pi/(Ng_{2D}^2)$ | $8\pi^2/g^2$ |
| Fractional instantons | Yes (action $4\pi/(Ng_{2D}^2)$) | Unknown |
| Renormalons | IR only (no UV) | Both UV and IR |
| Resurgence proved | Deformed model only | Conjectured |
| Borel plane structure | Simple (instanton singularities) | Complex (instantons + renormalons) |

The COMPLICATION in 4D is the presence of renormalon singularities
in addition to instanton singularities. In 2D, there are no UV
renormalons (the theory is super-renormalizable above the dynamical
scale). In 4D, UV renormalons arise from the running coupling.

**The renormalon problem** [OPEN]:

The renormalon singularities at $t = n/(2b_0)$ do not correspond to
semiclassical saddle points. They arise from chains of bubble diagrams
in perturbation theory. In standard 4D Yang--Mills, the cancellation
of renormalon ambiguities requires non-perturbative objects that are
NOT instantons (e.g., center vortices, monopoles, or condensates).

In the KK theory on $M^4 \times \mathbb{CP}^{N-1}$, the
renormalon structure is modified:
- Above the KK scale $1/r_3$, the coupling runs according to the
  $(4+2(N-1))$-dimensional beta function. The renormalon locations
  shift.
- The CP$^{N-1}$ topology provides additional saddle points (the
  Bogomolny instantons) that could cancel the renormalon ambiguities.

[STATUS: Whether the CP$^{N-1}$ saddle points cancel the renormalon
ambiguities is OPEN. This is a crucial question for the resurgence
program.]


---

## VI. What the Trans-Series Would Give

If the resurgent trans-series is established, it defines:

$$\sigma_{\text{phys}} = \mathcal{S}_{\text{median}}
  \left[\sum_m \sigma^{(m)}\right]$$

where $\mathcal{S}_{\text{median}}$ is the median resummation (the
average of left and right lateral Borel sums, which is unambiguous
when resurgence holds).

This would:
1. **Define $\sigma_{\text{phys}}$ in the continuum** without any
   lattice. [WOULD FOLLOW from resurgence]
2. **Give $\sigma_{\text{phys}} > 0$** if the leading Borel sum is
   positive and the instanton corrections are subleading. [WOULD
   FOLLOW from the structure of the leading sector]
3. **Bypass the continuum limit problem** entirely. The trans-series
   IS the continuum definition. [WOULD FOLLOW]

**The honest status:** Writing down the trans-series is the easy part.
Proving resurgence (the cancellation of ambiguities) is the hard part.
This is developed in the subsequent files.


---

## VII. Summary of Status Tags

| Claim | Status |
|-------|--------|
| Trans-series structure (Sections II--IV) | [ARGUED] -- standard form |
| Large-order behavior $\sigma_n^{(0)} \sim n!$ | [PROVED] -- Section 29 |
| Instanton action $S_I = 8\pi^2$ | [PROVED] -- Appendix B |
| Resurgence relations (Section III.4) | [CONJECTURED] |
| Renormalon cancellation | [OPEN] |
| $\sigma_{\text{phys}} > 0$ from trans-series | [OPEN] -- requires resurgence |
