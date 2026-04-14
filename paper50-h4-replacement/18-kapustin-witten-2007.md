# §18 — Kapustin-Witten 2007: N=4 SYM Topological Twist → Geometric Langlands

*The foundational paper. N=4 super Yang-Mills, topologically twisted on a 4-manifold $M = \Sigma \times C$, reduces (upon shrinking $C$) to a 2D sigma-model on $\Sigma$ whose target is the Hitchin moduli space. Electric-magnetic duality of the 4D theory becomes geometric Langlands duality of the 2D sigma-model. The canonical parameter $\Psi \in \mathbb{CP}^1$ interpolates between the A-model and B-model. The origin of Route C.*

---

## 18.1. The paper

**Reference.** A. Kapustin and E. Witten, *Electric-Magnetic Duality And The Geometric Langlands Program*, *Communications in Number Theory and Physics* 1 (2007), 1-236. Originally posted as hep-th/0604151 (April 2006).

Length: 236 pages. Authorship: Anton Kapustin (Caltech) and Edward Witten (IAS). Citation count: ~2000 as of 2026. The paper is one of the canonical references in mathematical physics; it is the starting point for virtually all subsequent work connecting gauge theory to geometric Langlands.

---

## 18.2. The N=4 super Yang-Mills theory

N=4 super Yang-Mills on 4-dimensional Minkowski (or Euclidean) space is the maximally supersymmetric gauge theory. Its field content is:

- A gauge field $A_\mu$ in the adjoint representation of the gauge group $G$.
- Six scalar fields $\phi^I$ ($I = 1, \ldots, 6$) in the adjoint representation.
- Four Majorana-Weyl fermions $\lambda^a$ ($a = 1, \ldots, 4$) in the adjoint representation.

The action is
$$S_{N=4} = \frac{1}{g^2} \int d^4 x \, \text{Tr}\left( \frac{1}{2} F_{\mu\nu} F^{\mu\nu} + D_\mu \phi^I D^\mu \phi^I + [\phi^I, \phi^J]^2 + \text{fermion terms}\right),$$
plus a theta term $\frac{i\theta}{8\pi^2} \int \text{Tr}(F \wedge F)$.

The theory has two dimensionless parameters: the coupling $g$ and the theta angle $\theta$. These combine into a single complex coupling
$$\tau = \frac{\theta}{2\pi} + \frac{4\pi i}{g^2}.$$

### 18.2.1. S-duality of N=4 SYM

Montonen-Olive (1977), sharpened by Vafa-Witten (1994) and others, conjectured: N=4 SYM is invariant under the modular transformation
$$\tau \to -\frac{1}{\tau}$$
provided the gauge group $G$ is replaced by its Langlands dual ${}^L G$.

Combined with the obvious $\tau \to \tau + 1$ periodicity (shifting $\theta$ by $2\pi$), this gives an $\text{SL}_2(\mathbb{Z})$ action on the moduli space of couplings. The S-transformation $\tau \to -1/\tau$ is *electric-magnetic duality*: it exchanges Wilson loops (electric operators) with 't Hooft loops (magnetic operators) and, simultaneously, $G$ with ${}^L G$.

This S-duality is the gauge-theoretic ancestor of the functional equation $s \leftrightarrow 1 - s$ of the programme's S-duality (Paper 60 §21). The same $\text{SL}_2(\mathbb{Z})$ that acts on the torus of the programme acts on the coupling space of N=4 SYM.

---

## 18.3. The topological twist

On a general 4-manifold $M$, N=4 SYM does not canonically make sense as a topological theory: the fields depend on the metric. Kapustin-Witten introduce a family of *topological twists* — procedures that modify the theory to make certain correlators metric-independent.

The twist depends on a parameter $t \in \mathbb{CP}^1$. The twisted theory on $M$ has:
- A BRST operator $Q_t$ (depending on $t$) that squares to zero.
- Correlators of $Q_t$-closed operators are metric-independent (topological invariants of $M$, or of the cycle supporting the operator).
- Specific values of $t$ produce specific 2D structures upon dimensional reduction.

### 18.3.1. The canonical parameter $\Psi$

Kapustin-Witten define
$$\Psi = \tau + \frac{t - t^{-1}}{t + t^{-1}} \cdot \frac{\bar\tau - \tau}{2}$$
and use $\Psi \in \mathbb{CP}^1$ as the canonical parameter (independent of the split of $\tau$ into $t$ and the physical coupling).

The S-duality of the untwisted theory, $\tau \to -1/\tau$, becomes on the twisted theory
$$\Psi \to -\frac{1}{n_G \Psi},$$
where $n_G$ is a gauge-group-dependent factor (= 1 for simply-laced groups like $\text{SU}(N)$; = 2 for $\text{SO}(2n+1)$; = 3 for $G_2$). This is geometric Langlands S-duality.

### 18.3.2. The three canonical values

Three values of $\Psi$ produce distinguished 2D structures:

| Value of $\Psi$ | 2D structure | Name |
|---|---|---|
| $\Psi = 0$ | B-model on $\mathcal{M}_H(G)$ | B-side |
| $\Psi = \infty$ | A-model on $\mathcal{M}_H({}^L G)$ | A-side |
| $\Psi = 1$ | Chern-Simons theory | Self-dual / Donaldson-like |

The B-model at $\Psi = 0$ and the A-model at $\Psi = \infty$ are related by S-duality (exchanging $G \leftrightarrow {}^L G$). This is the geometric Langlands correspondence in the Kapustin-Witten picture.

---

## 18.4. Dimensional reduction to 2D

Consider the 4-manifold $M = \Sigma \times C$, where $\Sigma$ is a 2-manifold (later the "spacetime" of the 2D theory) and $C$ is a Riemann surface (later the "geometric" direction). Shrink $C$ to zero size.

The twisted N=4 SYM on $M$ becomes, in the $C \to 0$ limit, a 2D sigma-model on $\Sigma$ with target
$$\mathcal{M}_H(G, C) = \text{Hitchin moduli space of stable Higgs bundles on } C \text{ with structure group } G.$$

The Hitchin moduli space $\mathcal{M}_H(G, C)$ is the moduli of pairs $(E, \phi)$, where $E$ is a holomorphic $G$-bundle on $C$ and $\phi$ is a Higgs field (a holomorphic 1-form with values in the adjoint bundle). It is a hyperkähler manifold of complex dimension $\dim G \cdot (g - 1)$, where $g$ is the genus of $C$.

### 18.4.1. The sigma-model structure

The 2D sigma-model on $\Sigma$ with target $\mathcal{M}_H(G, C)$ has:
- A twist parameter $\Psi$ (inherited from the 4D twist).
- At $\Psi = 0$: it is the B-model on $\mathcal{M}_H(G, C)$.
- At $\Psi = \infty$: it is the A-model on $\mathcal{M}_H({}^L G, C)$.

Mirror symmetry between the A-model on $\mathcal{M}_H({}^L G, C)$ and the B-model on $\mathcal{M}_H(G, C)$ is the 2D manifestation of 4D S-duality.

### 18.4.2. Categories of boundary conditions

The A-model and B-model each have a category of boundary conditions (D-branes):
- B-branes on $\mathcal{M}_H(G, C)$: the derived category of coherent sheaves $D^b \text{Coh}(\mathcal{M}_H(G))$.
- A-branes on $\mathcal{M}_H({}^L G, C)$: the Fukaya category $\text{Fuk}(\mathcal{M}_H({}^L G))$.

Mirror symmetry asserts an equivalence of categories
$$D^b \text{Coh}(\mathcal{M}_H(G)) \simeq \text{Fuk}(\mathcal{M}_H({}^L G)).$$

Via a further specialization (to A-branes of "coisotropic" type, Beilinson-Drinfeld 1991), this equivalence produces the geometric Langlands correspondence
$$D^b \text{Coh}(\mathcal{M}_H(G)) \simeq D\text{-mod}(\text{Bun}_{{}^L G}),$$
where $\text{Bun}_{{}^L G}$ is the moduli stack of ${}^L G$-bundles on $C$ and $D\text{-mod}$ denotes the derived category of D-modules.

This is the *geometric Langlands correspondence*, first conjectured by Beilinson-Drinfeld 1991 in a purely mathematical language, here derived (at the physics level of rigor) from 4D S-duality.

---

## 18.5. Wilson loops and 't Hooft loops

The key operators in 4D gauge theory are Wilson loops and 't Hooft loops.

**Wilson loops.** $W_R(L) = \text{Tr}_R \mathcal{P} \exp \oint_L A$, for $L$ a 1-cycle in $M$ and $R$ a representation of $G$.

**'t Hooft loops.** $T_\mu(L)$, defined by a singular gauge transformation with magnetic flux $\mu$ (a cocharacter of $G$) along $L$.

Under S-duality, Wilson and 't Hooft loops exchange: $W_R^G \leftrightarrow T_{\mu(R)}^{{}^L G}$, where $\mu(R)$ is the cocharacter of ${}^L G$ corresponding to the representation $R$ of $G$ (via the Langlands duality of representations).

In the 2D dimensional reduction:
- Wilson loops on $\Sigma$ become B-branes supported on specific subvarieties of $\mathcal{M}_H(G)$.
- 't Hooft loops on $\Sigma$ become A-branes supported on specific Lagrangians in $\mathcal{M}_H({}^L G)$.

The S-duality exchange Wilson ↔ 't Hooft becomes the mirror symmetry exchange B-brane ↔ A-brane, which under the Beilinson-Drinfeld specialization produces the Hecke correspondence of geometric Langlands.

---

## 18.6. Beilinson-Drinfeld specialization

Beilinson-Drinfeld 1991 (unpublished manuscript, widely circulated) gave the first construction of the geometric Langlands correspondence via *Hecke eigensheaves*: for each local system $\mathcal{E}$ on $C$ with structure group ${}^L G$, they constructed a Hecke eigensheaf $\text{Aut}_\mathcal{E}$ on $\text{Bun}_G$ satisfying the geometric Hecke eigenequation.

The Kapustin-Witten derivation recovers this: under the mirror symmetry of the Hitchin moduli spaces, the B-brane corresponding to a skyscraper sheaf on $\mathcal{M}_H({}^L G)$ (at a point corresponding to a local system $\mathcal{E}$) maps to an A-brane that, under Beilinson-Drinfeld's further specialization, is the Hecke eigensheaf $\text{Aut}_\mathcal{E}$.

The identification is:
$$\text{Hecke eigensheaf for } \mathcal{E} = \text{S-dual of Wilson operator for } \mathcal{E}.$$

This is the *content* of geometric Langlands in Kapustin-Witten's picture.

---

## 18.7. What Kapustin-Witten proved and did not prove

**What they proved** (at the physics level of rigor):

1. N=4 SYM admits a family of topological twists parametrized by $\Psi \in \mathbb{CP}^1$.
2. On $M = \Sigma \times C$ with $C$ shrunk, the twisted theory reduces to a 2D sigma-model with target $\mathcal{M}_H(G, C)$.
3. S-duality of the 4D theory induces mirror symmetry of the 2D sigma-model.
4. Via Beilinson-Drinfeld specialization, mirror symmetry on $\mathcal{M}_H$ produces geometric Langlands.

**What they did not prove** (requiring later mathematical work):

1. The S-duality itself (Montonen-Olive, Vafa-Witten conjecture). Remains a conjecture; has been extensively verified but not proved.
2. The rigorous 2D sigma-model construction on a hyperkähler target. Partial (via Frenkel-Gaitsgory, Ben-Zvi-Nadler).
3. The geometric Langlands correspondence itself. Proved by *Gaitsgory-Raskin 2024* (§19).

Kapustin-Witten provided the *architecture*. Mathematical execution took another 17 years.

---

## 18.8. Structural consequences for Route C

For Route C, the Kapustin-Witten picture provides three structural inputs:

### 18.8.1. The S-duality as functional equation

The 4D S-duality $\tau \to -1/\tau$ is the gauge-theoretic incarnation of the functional equation $s \to 1 - s$. On the Route B side, this appears as the functional equation of the YM L-function (Route B §17 Step 3, Obstruction 3). On the Route C side, this is a *known* feature of N=4 SYM.

If pure YM is the scale-bridge limit of twisted N=4 SYM (§20), then pure YM inherits a functional equation from N=4 SYM's S-duality. This is how Route C resolves Ob.3 of Route B.

### 18.8.2. The Wilson-loop spectrum via geometric Langlands

Wilson loops in the 4D twisted theory become B-branes on $\mathcal{M}_H(G, C)$ in the 2D reduction. Via geometric Langlands, B-branes correspond to D-modules on $\text{Bun}_{{}^L G}$. The Wilson-loop spectrum is therefore organized by the D-module category on the moduli stack of ${}^L G$-bundles.

This is the Route C analogue of the "automorphic side" of Langlands: instead of cuspidal automorphic representations of GL$_n(\mathbb{A}_\mathbb{Q})$, we have D-modules on $\text{Bun}_{{}^L G}$. The correspondence is what Gaitsgory-Raskin 2024 proved.

### 18.8.3. The canonical parameter $\Psi$ as bookkeeping

The parameter $\Psi$ labels *which* reduction is being taken. Different $\Psi$ produce different 2D theories (B-model, A-model, Chern-Simons, etc.). For H4, the relevant $\Psi$ is the one producing the sigma-model whose correlators match the YM short-distance expansion under the scale bridge.

Identifying the right $\Psi$ for pure YM is part of the scale-bridge analysis (§20).

---

## 18.9. What changed after Gaitsgory-Raskin 2024

The Kapustin-Witten picture, until 2024, was *conjectural* on the mathematical side: geometric Langlands was a conjecture. Kapustin-Witten provided compelling physics-level evidence, but a rigorous mathematical proof was missing.

Gaitsgory-Raskin 2024 (§19) *proved* geometric Langlands (for the appropriate version: categorical geometric Langlands for non-ramified/tame ramification on a smooth projective curve, building on a decade of work). This changes the status of Route C dramatically:

- **Before 2024:** Kapustin-Witten provides a physics-level path from N=4 SYM to geometric Langlands. Geometric Langlands is a conjecture.
- **After 2024:** Kapustin-Witten provides a physics-level path from N=4 SYM to a *proven* theorem. The main remaining conjectural piece is the scale bridge from N=4 SYM to pure YM (§20).

Route C's feasibility is a direct consequence of the 2024 breakthrough.

---

## 18.10. Summary

Kapustin-Witten 2007 established the gauge-theoretic derivation of geometric Langlands: topologically twisted N=4 SYM on $M = \Sigma \times C$ reduces (upon shrinking $C$) to a 2D sigma-model on $\mathcal{M}_H(G, C)$; 4D S-duality induces 2D mirror symmetry; via Beilinson-Drinfeld, mirror symmetry produces the geometric Langlands correspondence. The canonical parameter $\Psi$ labels which twist is taken; Wilson loops become B-branes on $\mathcal{M}_H$, which via geometric Langlands correspond to D-modules on $\text{Bun}_{{}^L G}$.

For Route C, Kapustin-Witten provides:
- The S-duality (= functional equation) as a known feature of N=4 SYM.
- The Wilson-loop spectrum organized by geometric Langlands data.
- The architecture connecting gauge theory to Langlands duality.

The remaining bridges are: §19 (Gaitsgory-Raskin 2024 — the proven correspondence), §20 (the scale bridge N=4 → pure YM), §21 (Elliott-Gwilliam-Williams BV quantization), §22 (short-distance extraction), §23 (Route C proof sketch).

---

*Paper 50 §18. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
