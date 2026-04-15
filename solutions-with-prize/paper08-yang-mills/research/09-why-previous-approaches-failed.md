# 8. Why Previous Approaches Could Not Succeed

This section is not a criticism of previous work. It is an explanation of
why the mass gap problem is naturally hard in four dimensions and
naturally easy in eleven.


## 8.1 The Non-Perturbative Barrier

In four-dimensional Yang--Mills, the mass gap is a non-perturbative
phenomenon. Formally: expand the glueball mass in powers of $g^2$:

$$m_{\text{glueball}} = \Lambda_{\text{QCD}}
  = \mu \exp\left(-\frac{8\pi^2}{b_0 g^2(\mu)}\right)$$

where $b_0 = 11N/3$ is the one-loop beta function coefficient. This
expression has an essential singularity at $g = 0$:
$$\frac{d^n}{dg^n} e^{-c/g^2}\bigg|_{g=0} = 0 \quad
  \text{for all } n$$

The mass gap is zero at every order in perturbation theory. It is
invisible to Feynman diagrams. No resummation of the perturbative series
can produce it --- the information is simply not in the series.

**In the KK framework:** The mass gap comes from the topology of
$\mathbb{CP}^2$, which is visible at the classical level (it is a
property of the background geometry, not of quantum fluctuations). The
essential singularity $e^{-c/g^2}$ appears when one projects the
topological energy bound down to four dimensions and expresses it in
terms of the four-dimensional coupling. The non-perturbative character
is an artifact of the projection, not of the phenomenon.


## 8.2 The Lattice and the Continuum Limit

Wilson's lattice gauge theory (1974) is the most successful
non-perturbative approach to Yang--Mills. It confirms the mass gap
numerically to high precision. However, the rigorous program requires
three steps:

1. **Define the theory on a lattice** (done: Wilson action)
2. **Show the mass gap exists at finite lattice spacing** (done:
   Osterwalder--Seiler 1978 for the Wilson action at strong coupling)
3. **Take the continuum limit $a \to 0$ and show the gap survives**
   (NOT done)

Step 3 is the problem. Taking $a \to 0$ requires:
- Tuning the bare coupling $g_0(a) \to 0$ along the trajectory of
  asymptotic freedom
- Controlling all correlation functions in this limit
- Showing the limiting theory satisfies the OS axioms

The obstacle is that the lattice breaks $SO(4)$ invariance. Restoring it
requires showing that the lattice artifacts vanish in the limit ---
which requires precisely the kind of non-perturbative control that the
lattice was designed to avoid needing.

**In the KK framework:** There is no lattice. The theory is defined in
the continuum from the start. The "discretization" is not in spacetime
(which would break Euclidean invariance) but in the internal direction
(which produces the KK tower). $SO(4)$ invariance is exact at every
stage. There is no continuum limit to take.


## 8.3 Constructive QFT in Lower Dimensions

Rigorous constructions of Yang--Mills exist in lower dimensions:

- **2D:** Migdal (1975), Witten (1991, 1992). The theory is exactly
  solvable. There is a mass gap (the theory is topological in 2D).

- **3D:** Partial results. Balaban (1985--1989) established
  ultraviolet stability of the lattice theory. The full construction
  remains incomplete.

- **4D:** No rigorous construction exists.

The difficulty in going from 3D to 4D is not merely technical. In 4D,
the coupling is dimensionless (classically marginal), so the theory is
at the boundary of renormalizability. The beta function produces
logarithmic running, and the strong-coupling regime is reached at
energies $\sim \Lambda_{\text{QCD}}$. Controlling the theory across this
transition requires uniform estimates that are not available.

**In the KK framework:** The 4D theory is not constructed from scratch.
It is obtained by reduction from a well-defined higher-dimensional
theory. The strong-coupling regime of 4D Yang--Mills corresponds to the
topological sector of the $\mathbb{CP}^2$ gauge theory --- which is
controlled by the Bogomolny bound, not by perturbative estimates.


## 8.4 AdS/CFT

The gauge/gravity correspondence (Maldacena 1997) provides
non-perturbative definitions of certain gauge theories. In the prototypical
example, $\mathcal{N} = 4$ super Yang--Mills on $S^3 \times \mathbb{R}$
is dual to Type IIB string theory on $AdS_5 \times S^5$.

For confining theories, the holographic dual involves an IR cap-off of
the AdS geometry (e.g., the Witten model, Sakai--Sugimoto model). The
mass gap is visible in the discrete normalizable mode spectrum of the
capped geometry.

**Limitations:**
- Pure Yang--Mills on $\mathbb{R}^4$ does not have a known string dual
- AdS/CFT requires a negative cosmological constant (Yang--Mills lives
  in flat space)
- The holographic mass gap is established only within the holographic
  framework; transferring it to the field theory requires control of the
  $\alpha'$ and $g_s$ corrections

**Comparison with KK approach:** Both the AdS/CFT and KK approaches use
extra dimensions. The difference is that AdS/CFT uses extra dimensions as
a *dual description* (different theory, same physics), while the KK
approach uses ~~extra dimensions~~ the 4+1 coordinate structure as the *actual geometry* (same theory,
higher-dimensional). The KK approach does not require a duality --- it is
a direct embedding.
<!-- legacy 2026-04-15: self-description "extra dimensions" migrated to "4+1 coordinate structure" per north-star §0.10 entries 1-2, Intervention 8; other occurrences describe competing programmes and remain -->


## 8.5 The Root Cause

Every four-dimensional approach fails for the same reason: **the mass
gap is topological, but four-dimensional Yang--Mills has no access to
the topology that produces it.**

In four dimensions:
- The gauge field $A_\mu^a(x)$ lives on $\mathbb{R}^4$, which is
  contractible ($H_k(\mathbb{R}^4) = 0$ for $k > 0$)
- There is no non-contractible cycle to wrap
- Instantons exist (on $S^4$ or $\mathbb{R}^4$ with boundary conditions
  at infinity), but they are tunneling events, not stable configurations
- The mass gap arises from the instanton effects, but controlling them
  requires non-perturbative techniques that are not available

In eleven dimensions:
- The gauge field is a metric component on $M^4 \times \mathbb{CP}^2$
- $\mathbb{CP}^2$ has $H_2 = \mathbb{Z}$ (non-contractible cycle)
- Topological charge is quantized to integers
- The Bogomolny bound gives a strict energy lower bound
- No non-perturbative calculation is needed: the bound is an algebraic
  identity

The mass gap is easy in eleven dimensions because the topology is there.
It is hard in four dimensions because the topology has been projected out.

---

**Table: Comparison of Approaches**

| Approach | Arena | Obstacle | Status |
|----------|-------|----------|--------|
| Perturbation theory | 4D | Essential singularity at $g = 0$ | Cannot work |
| Lattice QCD | 4D discretized | Continuum limit unproven | Gap confirmed numerically |
| Constructive QFT | 4D rigorous | Strong-coupling control at $d = 4$ | Open |
| AdS/CFT | 5D+ (dual) | Not applicable to pure YM on $\mathbb{R}^4$ | Partial |
| Stochastic quantization | 4D + fictitious time | Same IR problems | Open |
| **KK embedding** | **11D (direct)** | **None: gap is topological** | **This paper** |
