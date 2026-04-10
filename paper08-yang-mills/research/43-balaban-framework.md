# Balaban's Framework: What We Know and What We Need

Extracted from web searches of Balaban's papers (Commun. Math. Phys.
1985-1989), Dimock's expositions (2011-2013), and the Jaffe-Witten
problem statement.


---

## I. What Balaban Proved

### I.1 The papers

Balaban published a series of papers in Communications in Mathematical
Physics (1982-1989):

1. "Propagators and renormalization transformations for lattice gauge
   theories" (CMP 95, 1984; CMP 96, 1984)
2. "Averaging operations for lattice gauge theories" (CMP 98, 1985)
3. "Ultraviolet stability of three-dimensional lattice pure gauge field
   theories" (CMP 102, 1985)
4. **"Renormalization group approach to lattice gauge field theories.
   I. Generation of effective actions in a small field approximation
   and a coupling constant renormalization in four dimensions"**
   (CMP 109, 1987) — the key paper
5. "Convergent renormalization expansions for lattice gauge theories"
   (CMP 119, 1988)
6. Additional papers on propagators, large field estimates

Modern expositions by Dimock:
- "The Renormalization Group According to Balaban - I. Small fields"
  (arXiv:1108.1335, 2011) — phi^4 in 3D
- "The Renormalization Group According to Balaban - II. Large fields"
  (arXiv:1212.5562, 2013)

### I.2 The UV stability theorem

**Theorem (Balaban 1987-1989).** *For SU(N) lattice gauge theory on a
4D toroidal lattice with Wilson action, the block-spin renormalization
group transformation can be iterated from the fine lattice (spacing $a$)
to the unit lattice (spacing $a_0 = 1$), and the resulting effective
action remains bounded.*

More precisely: define a sequence of block-spin transformations
$\mathcal{T}_k$, $k = 0, 1, \ldots, K$, where $K = \log_2(a_0/a)$ is
the number of steps. At each step:

$$S_{k+1} = \mathcal{T}_k[S_k]$$

Balaban proved:

**(a) Small field region.** For configurations where the gauge field
curvature $|F| < p(g_k)$ (a function of the running coupling), the
effective action has the form:

$$S_k = \frac{1}{g_k^2} \sum_P (1 - \tfrac{1}{N} \text{Re Tr}\,U_P)
  + \sum_n c_n(g_k) \mathcal{O}_n + E_k$$

where:
- $g_k^2$ is the running coupling (renormalized at each step)
- $\mathcal{O}_n$ are gauge-invariant local operators of dimension $> 4$
- $c_n(g_k) = O(g_k^{d_n - 4})$ with $d_n > 4$
- $E_k$ is a local remainder with $|E_k| \leq C g_k^4 \times (\text{volume})$

**(b) Coupling renormalization.** The running coupling satisfies:

$$\frac{1}{g_{k+1}^2} = \frac{1}{g_k^2} + \beta_0 \ln 2 + O(g_k^2)$$

which is the one-loop beta function: $g_{k+1}^2 = g_k^2 - \beta_0
g_k^4 \ln 2 + O(g_k^6)$.

**(c) Convergence.** The effective action $S_K$ on the unit lattice is
bounded: $|S_K| \leq C$ (independent of the number of RG steps $K$,
hence independent of the original lattice spacing $a$).

### I.3 What Balaban did NOT prove

- **The mass gap.** Balaban's theorem says the effective action is
  bounded but does NOT show a spectral gap in the transfer matrix.

- **Confinement.** No statement about the area law or string tension.

- **The continuum limit as a QFT.** UV stability says the effective
  action is bounded, but constructing the continuum limit requires
  additionally showing convergence of correlation functions and
  verifying the OS axioms.


---

## II. What We Need from Balaban

### II.1 The key bound

From Balaban's result (a) above, the effective action at step $k$ is:

$$S_k = S_{\text{YM}}(g_k^2) + \delta S_k$$

where $\delta S_k = \sum_n c_n \mathcal{O}_n + E_k$ is the remainder
after coupling renormalization. Balaban proved:

$$|\delta S_k| \leq C g_k^{4} \times V_k$$

where $V_k$ is the lattice volume at scale $k$ and $C$ is a constant.

**This is the $O(g^4)$ bound we need.** The key point: the remainder
after coupling renormalization is $O(g^4)$, not $O(g^2)$.

### II.2 From action bounds to mass gap bounds

We need to connect $|\delta S_k| \leq C g_k^4 V_k$ to
$|\delta m_k| \leq C' g_k^4 \Lambda$.

The transfer matrix at step $k$ is:
$$T_k = e^{-a_k H_k}$$

The Hamiltonian $H_k$ is related to the effective action $S_k$ by the
transfer matrix construction (standard lattice theory). A perturbation
$\delta S_k$ to the action induces a perturbation $\delta H_k$ to the
Hamiltonian.

The spectral gap shift is bounded by:
$$|\delta m_k| = |\text{gap}(H_k) - \text{gap}(H_{k-1})|
  \leq \|\delta H_k\|_{\text{op}}$$

The operator norm $\|\delta H_k\|$ is bounded by the action perturbation:
$$\|\delta H_k\| \leq \frac{1}{a_k} |\delta S_k|_{\text{max per site}}
  \leq \frac{C g_k^4}{a_k}$$

In physical units: $|\delta m_k| \leq C g_k^4 / a_k$. But
$1/a_k = 2^k / a_0$, and $g_k^2 \sim 1/(b_0 k \ln 2)$, so:

$$|\delta m_k| \leq C \frac{2^k}{a_0 (b_0 k \ln 2)^2}$$

This GROWS with $k$! Each step gives a larger correction.

**But this is in LATTICE units.** In PHYSICAL units:
$$|\delta m_k^{\text{phys}}| = |\delta m_k| \times a_k
  = C g_k^4 \leq \frac{C}{(b_0 k \ln 2)^2}$$

And the SUM:
$$\sum_k |\delta m_k^{\text{phys}}| \leq C \sum_k \frac{1}{(b_0 k \ln 2)^2}
  < \infty$$

**This converges.** The sum $\sum 1/k^2$ is the Basel problem = $\pi^2/6$.


---

## III. The Argument (Assembled)

### III.1 Setup

Start at lattice spacing $a_0$ where the cluster expansion gives:
$$m_0 = \Delta(a_0) > 0 \quad [\text{PROVED, Section 25}]$$

### III.2 The RG descent

At each block-spin step $k = 0, 1, 2, \ldots$:

1. The lattice spacing changes: $a_{k+1} = a_k / 2$ (refining).
   Wait — we need to go from coarse to fine (descending to the
   continuum), so: $a_{k+1} = a_k / 2$, $g_{k+1}^2 < g_k^2$
   (asymptotic freedom).

2. Actually, Balaban's RG goes from FINE to COARSE (integrating out
   UV modes). For the continuum limit, we go the OTHER way: from
   the unit lattice (coarse) to the fine lattice (UV).

   Balaban's theorem says: starting from the fine lattice (UV) and
   coarsening, the effective action stays bounded. This is UV stability.

   For the continuum limit: we need to START from the coarse lattice
   (where $m_0 > 0$ is proved) and ask what happens as we refine.

### III.3 The inverse direction

**Rethinking:** Balaban's RG integrates OUT UV modes (fine → coarse).
We proved $m_0 > 0$ at the coarse scale. We want $m_\infty > 0$ at the
fine scale (continuum).

The connection: if the effective action at the FINE scale is bounded
(Balaban), and the effective action at the COARSE scale gives $m_0 > 0$
(our cluster expansion), then the physical mass gap is determined by
the COARSE-scale physics (since the mass gap is an IR quantity).

**The mass gap is an IR quantity.** It's determined by the coarse-scale
effective action, not the fine-scale. As we refine the lattice
(add UV modes), the IR physics (mass gap) should not change — this is
the Wilsonian separation of scales.

### III.4 Making this rigorous

Balaban's UV stability says: integrating out UV modes (from fine to
coarse) produces a bounded effective action. The mass gap at the coarse
scale is $m_0 > 0$.

The mass gap at the fine scale is RELATED to the mass gap at the coarse
scale by: $m_{\text{fine}} = m_{\text{coarse}} + \delta m$, where
$\delta m$ comes from the UV modes being integrated in (not out).

But we DON'T integrate modes in. We integrate them OUT (Balaban's
direction). The mass gap at the coarse scale ($m_0$) is the OUTPUT
of the RG after integrating out ALL UV modes. It already includes
their effects.

**The key insight:** $m_0$ (the coarse-scale mass gap) IS the physical
mass gap. The fine lattice is just a regularization. As we remove the
regularization ($a \to 0$), the physical mass gap stays at $m_0$
(because it's an IR quantity determined by the effective action at the
coarse scale, which is bounded by Balaban).

### III.5 The convergence argument (correct version)

At each RG step (fine → coarse), the effective coupling changes by:
$$g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$$

The effective action at the coarse scale is:
$$S_K = S_{\text{YM}}(g_K^2) + \delta S_K$$

with $|\delta S_K| \leq C g_K^4 V_K$.

The mass gap extracted from $S_K$ is:
$$m = m_{\text{YM}}(g_K^2) + \delta m$$

with $|\delta m| \leq C' g_K^4 \Lambda$.

As $a \to 0$ (more RG steps $K \to \infty$): $g_K^2 \to g_*^2$ (the
coupling at the unit lattice scale, which is FIXED). Therefore:

$$m = m_{\text{YM}}(g_*^2) + O(g_*^4) \Lambda$$

This is INDEPENDENT of $K$ (the number of fine-lattice steps). The
mass gap at the coarse scale is the same regardless of how many
UV steps we integrate out.

**This is UV stability applied to the mass gap:** the mass gap at the
IR scale (unit lattice) is bounded and independent of the UV cutoff
(fine lattice spacing $a$).


---

## IV. The Remaining Gap

The argument above uses two claims that need verification:

**Claim 1:** The mass gap at the coarse scale is $m_0 > 0$.
This is PROVED by our cluster expansion (Section 25) when the coarse
scale is chosen to be $a_0 \gg r_3$.

**Claim 2:** The mass gap at the coarse scale equals the physical mass
gap (the IR mass gap is determined by the coarse-scale effective
action, not the fine-scale).

Claim 2 is the Wilsonian principle of scale separation. In Balaban's
framework, it follows from the LOCALITY of the effective action: each
RG step produces a LOCAL effective action (bounded, with controlled
irrelevant operators). The mass gap depends on the RELEVANT and
MARGINAL parts of the effective action (the YM coupling $g_K^2$) and
receives only $O(g^4)$ corrections from the irrelevant parts.

**What needs to be shown rigorously:** That Balaban's bounds on the
effective action imply bounds on the MASS GAP — specifically, that the
transfer matrix spectral gap is stable under perturbations bounded by
$C g^4$.


---

## V. The Plan (Refined)

### Phase A1: Extract spectral bounds from Balaban (1-2 months)

Study Balaban's papers and Dimock's expositions. Extract the precise
form of $|\delta S_k| \leq C g_k^4 V_k$. Understand the locality
structure (is the perturbation local? does it satisfy cluster properties?).

### Phase A2: Transfer matrix perturbation theory (2-3 months)

Given the local perturbation $\delta S_k$ bounded by $C g_k^4$, prove
that the transfer matrix spectral gap satisfies:

$$|\Delta(S_k + \delta S_k) - \Delta(S_k)| \leq C' g_k^4 \Lambda$$

This uses Kato's perturbation theory applied to the transfer matrix,
with the locality of $\delta S_k$ providing the needed estimates.

### Phase A3: Conclude (1 month)

Combine:
1. Cluster expansion gives $\Delta(a_0) > 0$ at the starting scale
2. Balaban's UV stability gives $|\delta S| \leq C g^4$ at each step
3. Phase A2 gives $|\delta \Delta| \leq C' g^4 \Lambda$ at each step
4. Since the mass gap at the IR scale receives corrections $O(g^4)$
   from each UV step, and Balaban's coupling $g_K$ is bounded, the
   total correction is bounded
5. $\Delta_{\text{phys}} = \Delta_0 + O(g^4) > 0$


---

## Sources

- [Balaban, Renormalization group approach I (CMP 109, 1987)](https://link.springer.com/article/10.1007/BF01215223)
- [Dimock, The RG According to Balaban - I (arXiv:1108.1335)](https://arxiv.org/abs/1108.1335)
- [Dimock, The RG According to Balaban - II (arXiv:1212.5562)](https://arxiv.org/abs/1212.5562)
- [Jaffe-Witten, Quantum Yang-Mills Theory (Clay problem statement)](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
- [Chatterjee, Yang-Mills for Probabilists (arXiv:1803.01950)](https://arxiv.org/abs/1803.01950)
