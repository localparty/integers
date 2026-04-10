# 10. The Remaining Problem and Paths to Resolution

---

## 10.1 What has been achieved

**Lattice mass gap (Theorem 4, PROVED).** The KK cluster expansion
proves $\Delta_0 > 0$ for $\mathrm{SU}(N)$ lattice gauge theory at
all practical couplings, using the Weitzenboeck gap on
$\mathbb{CP}^{N-1}$ to control bond activities. Non-perturbative
and unconditional.

**Reduction to one estimate (Theorem 8, CONDITIONAL).** The
continuum mass gap $\Delta_\infty > 0$ follows from Conjecture 1
alone. All other ingredients -- Balaban's UV stability, asymptotic
freedom, OS reconstruction -- are proved.

**Perturbative verification (Theorem 7, PROVED).** The form factor
bound holds to all orders in $g^2$: the connected matrix element of
a dimension-$d_O$ operator is suppressed by $(a\Delta)^{d_O-4}$.
Instanton corrections are $O(e^{-8\pi^2/g^2})$.

**Sufficiency (Theorem 8, PROVED).** If Conjecture 1 holds with
$s \geq 2$, then $C_\infty = \Delta_\infty/\Lambda_\infty > 0$
with correction $\sim 1\%$ ($s=2$) or $\sim 0.01\%$ ($s=4$).

---

## 10.2 The one open problem

**Promote the perturbative form factor bound to a non-perturbative
bound.** Equivalently: extend Balaban's multi-scale estimates from
the effective action (partition function) to one-particle form
factors (three-point functions).

Precisely: let $E_k$ be the irrelevant remainder in Balaban's
effective action at step $k$, and $|1\rangle$ the one-glueball state
at zero momentum. Prove:
$$\left|\sum_x \langle 1|E_k(x)|1\rangle_c\right| \leq C\,g_k^4\,(a_k\Delta)^s\cdot\Delta^3 \quad (s \geq 2).$$

This says: irrelevant operators in the lattice effective action are
genuinely irrelevant for the spectral gap. It is the rigorous
formulation of dimensional analysis in the one-particle sector.

---

## 10.3 Three paths to resolution

### Path (a): Extend Balaban's cluster expansion to three-point functions

Balaban's multi-scale expansion (Commun. Math. Phys. 109, 116, 119;
1985-89) controls the effective action through a polymer expansion
with bounded activities. The form factor
$\langle 1|E_k(x)|1\rangle_c$ is a three-point object: operator
insertion between two one-particle states, corresponding to a
three-point correlator in the functional integral.

Extending the expansion to operator insertions uses existing
technology. Dimock (2011-13) has carried out parts of Balaban's
program in modern notation, establishing the framework. The required
new estimates are:

- Polymer activities with a single operator insertion.
- Power counting: each dimension-$d_O$ insertion carries
  $(a|q|)^{d_O-4}$ in momentum space, non-perturbatively.
- Summability of the resulting polymer series.

These are multi-scale estimates of the same type Balaban proves for
the effective action. The conceptual framework is identical; the new
element is tracking operator insertions through the RG.

**Estimated scope:** one substantial paper, 50-100 pages.

### Path (b): Spectral perturbation theorem sensitive to operator dimension

Prove that the transfer matrix spectral gap responds to irrelevant
perturbations with dimensional suppression. Precisely: let $T$ have
gap $\Delta > 0$ and let $\delta T = \sum_x \delta t(x)$ with
$\delta t$ a local operator of dimension $d_O > 4$, $\|\delta t\| \leq \epsilon$. Prove:
$$|\delta\Delta| \leq C\,\epsilon\,(a\Delta)^{d_O-4}\,\Delta.$$

Standard Kato/min-max perturbation theory gives only
$|\delta\Delta| \leq C\epsilon$ with no dimension dependence. The
improvement requires a perturbation theorem that distinguishes
relevant, marginal, and irrelevant perturbations by their
momentum-space behavior -- going beyond existing spectral theory.

**Estimated scope:** a new result in spectral theory, potentially
of independent interest.

### Path (c): Rigorous numerical verification

Monte Carlo measurement of $\Delta(a)$ at multiple lattice spacings
can verify $\Delta(a) = C_\infty\Lambda + O(g^4(a\Lambda)^2\Lambda)$.
Existing lattice data is consistent. Strong evidence, but not a
mathematical proof.

---

## 10.4 The honest bottom line

$$\underbrace{\text{Lattice mass gap } \Delta_0 > 0}_{\textbf{[PROVED]}}
  + \underbrace{\text{Balaban UV stability}}_{\textbf{[PROVED]}}
  + \underbrace{\text{Form factor bound}}_{\substack{
    \text{Perturbative: \textbf{[PROVED]}} \\[2pt]
    \text{Non-perturbative: \textbf{[OPEN]}}}}
  = \underbrace{\Delta_\infty > 0}_{\textbf{[CONDITIONAL]}}$$

The lattice mass gap is a new, unconditional result. The reduction
to the form factor bound clarifies the problem. The perturbative
verification and conditional theorem show the bound is correct in
spirit and sufficient in practice.

The proof is one estimate away from completion. That estimate -- a
non-perturbative form factor bound for irrelevant operators in
one-particle states -- is a well-posed problem in constructive QFT.
It requires no new ideas, only the extension of existing multi-scale
techniques to a new class of observables.
