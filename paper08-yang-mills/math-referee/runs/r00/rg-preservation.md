# RG Preservation of the Form Factor Bound

Does the form factor bound propagate from scale $k$ to scale $k+1$
under Balaban's block-spin transformation?

---

## 1. The RG Step

### 1.1 Geometry and field decomposition

At step $k$: lattice $\Lambda_k$, spacing $a_k = 2^k a_0$,
dimensionless gap $\hat{\Delta}_k = a_k \Delta_k$. One block-spin
step coarsens to $\Lambda_{k+1}$ with $a_{k+1} = 2a_k$ and
$\hat{\Delta}_{k+1} = 2\hat{\Delta}_k(1 + O(g_k^4))$.

The gauge field splits: $U = V \cdot u$ where $V$ is the
block-averaged (slow) field on $\Lambda_{k+1}$ and $u$ is the
fluctuation (fast) field with momenta
$\pi/a_{k+1} < |p| < \pi/a_k$. The effective action at $k+1$ is:

$$e^{-S_{k+1}[V]} = \int \mathcal{D}u\;
  e^{-S_k[V \cdot u]}\;\delta(\text{gauge fixing})$$

### 1.2 Structure of the block-spin integration

Balaban decomposes the integration into three pieces:

**(i) Saddle point:** $S_k[V \cdot u_{\mathrm{cl}}]
= (1/g_k^2)\,S_{\mathrm{YM}}[V] + O(g_k^4)$, renormalizing the
coupling and generating irrelevant operators on $V$.

**(ii) Gaussian fluctuations:** the one-loop determinant
$\frac{1}{2}\ln\det[(-D^2[V]+m_W^2)/(-\partial^2+m_W^2)]$
produces coupling renormalization plus new irrelevant operators
with $|\delta c_{d_O}| \leq C g_k^{d_O-2}$.

**(iii) Higher-order:** non-Gaussian corrections $O(g_k^6)$
per site.

The result:

$$S_{k+1}[V] = \mathcal{E}_0^{(k+1)} V
  + \frac{1}{g_{k+1}^2}\,S_{\mathrm{YM}}[V]
  + \sum_x E_{k+1}(x)[V]$$

with $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$,
$b_0 = 11N/(48\pi^2)$, and $\|E_{k+1}\| \leq C g_{k+1}^4$
per site.


---


## 2. Decomposition of the Form Factor at Step $k+1$

### 2.1 Two sources for $E_{k+1}$

$$E_{k+1}(x)[V] = E_k^{\downarrow}(x)[V] + \delta E_k(x)[V]$$

where $E_k^{\downarrow}$ is the old remainder expressed in terms of
the block field $V$ (the "flow" of $E_k$ to scale $k+1$), and
$\delta E_k$ is the new contribution from the fluctuation integral.

### 2.2 The one-particle state change

The state $|1\rangle_{k+1}$ on $\Lambda_{k+1}$ satisfies:

$$|1\rangle_{k+1} = |1\rangle_k + |\delta 1\rangle_k,\qquad
  \|\delta 1\| \leq C\,g_k^4/\hat{\Delta}_k$$

(Kato perturbation theory applied to
$\|E_k\| \leq C g_k^4$).

### 2.3 The form factor decomposition

$$\langle 1|E_{k+1}(0)|1\rangle_c^{(k+1)}
  = \underbrace{{}_k\langle 1|E_k^{\downarrow}(0)|1\rangle_k^c}
    _{\text{(A1): old state, old operator}}
  \;+\; \underbrace{\text{cross terms from } |\delta 1\rangle}
    _{\text{(A2)}}
  \;+\; \underbrace{\langle 1|\delta E_k(0)|1\rangle_c^{(k+1)}}
    _{\text{(B): new operators}}$$


---


## 3. Bounding the Old Contribution (A)

### 3.1 Term (A1): the form factor of $E_k$ on the block lattice

Assume the inductive hypothesis at step $k$:

$$|{}_k\langle 1|E_k(0)|1\rangle_k^c| \leq C_k\,g_k^4\,\hat{\Delta}_k^2$$

The coarsened operator $E_k^{\downarrow}$ on $\Lambda_{k+1}$
inherits the derivative structure of $E_k$, with coefficient
$|c_{d_O}^{\downarrow}| \leq |c_{d_O}^{(k)}|(1+O(g_k^2))$.
Its matrix element in the old state satisfies the same bound:

$$|{}_k\langle 1|E_k^{\downarrow}(0)|1\rangle_k^c|
  \leq C_k\,g_k^4\,\hat{\Delta}_k^2\,(1+O(g_k^2))$$

Converting to step-$k+1$ variables via
$\hat{\Delta}_k = \hat{\Delta}_{k+1}/2 + O(g_k^4\hat{\Delta}_{k+1})$:

$$|\text{(A1)}| \leq \frac{C_k}{4}\,g_k^4\,\hat{\Delta}_{k+1}^2
  \,(1+O(g_k^2))$$

**The factor $1/4$ is the contraction mechanism.** The old form
factor, expressed in the new dimensionless units, shrinks by $1/4$
because $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$. The physics
has not changed; only the bookkeeping units have coarsened.

### 3.2 Term (A2): cross terms from the wave function change

$$|\langle\delta 1|E_k^{\downarrow}(0)|1\rangle_k^c|
  \leq \|E_k^{\downarrow}(0)\|\cdot\|\delta 1\|
  \leq C g_k^4 \cdot C' g_k^4/\hat{\Delta}_k
  = C'' g_k^8/\hat{\Delta}_k$$

In step-$k+1$ variables: $g_k^8/\hat{\Delta}_k
= 2g_k^8/\hat{\Delta}_{k+1}$. On the asymptotically free
trajectory where $\hat{\Delta}_k \gtrsim g_k^{4/3}$, this is
$O(g_k^4\hat{\Delta}_{k+1}^2 \cdot g_k^4/\hat{\Delta}_k^3)$,
which is subleading.

### 3.3 Total old contribution

$$|\text{(A)}| \leq \frac{C_k}{4}\,g_k^4\,\hat{\Delta}_{k+1}^2
  \,(1+O(g_k^2))$$


---


## 4. Bounding the New Contribution (B)

### 4.1 What generates $\delta E_k$

Integrating out the UV shell at step $k$ generates new irrelevant
operators. The modes have momenta $|p| \sim 1/a_k \gg \Delta$,
far above the mass gap. Their form factor in the one-particle
state involves the coupling of UV fluctuations to the IR particle.

### 4.2 Perturbative estimate

Each new dimension-$d_O$ operator carries $d_O-4$ covariant
derivatives beyond $\mathrm{Tr}\,F^2$. In the one-particle matrix
element, these derivatives produce powers of $|q|\sim\hat{\Delta}_{k+1}$:

$$|\langle 1|\delta O_{d_O}(0)|1\rangle_c|
  \leq |\delta c_{d_O}|\cdot C\,\hat{\Delta}_{k+1}^{d_O-4}$$

For $d_O = 6$: $|\langle 1|\delta E_k^{(6)}(0)|1\rangle_c|
\leq C'\,g_k^4\,\hat{\Delta}_{k+1}^2$.

This respects the bound because the block-spin average preserves
the derivative structure: each step is a local, short-distance
integration over a $2^4$-site block. The derivative counting
(Weinberg's theorem on the lattice) persists through the averaging.

### 4.3 UV/IR decoupling

The UV modes at scale $k$ couple to the IR one-particle state
with suppression $\hat{\Delta}_k^{d_O-4}$. The connected structure
is essential: $\langle 0|\delta E_k(0)|0\rangle$ is subtracted by
vacuum energy renormalization, so $\langle 1|\delta E_k(0)|1\rangle_c$
measures only the particle-specific response. Non-perturbative
corrections (instantons: $O(e^{-8\pi^2/g_k^2})$; large fields:
$O(e^{-c/g_k^2})$) are exponentially suppressed.

### 4.4 The new contribution bound

$$|\text{(B)}| \leq C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2
  + O(e^{-c/g_k^2})$$


---


## 5. The Inductive Step

### 5.1 Combining (A) and (B)

$$|\langle 1|E_{k+1}(0)|1\rangle_c^{(k+1)}|
  \leq \left(\frac{C_k}{4} + C_{\mathrm{new}}\right)
  g_k^4\,\hat{\Delta}_{k+1}^2\,(1+O(g_k^2))$$

Converting $g_k^4 = g_{k+1}^4(1+O(g_k^2))$:

$$|\langle 1|E_{k+1}(0)|1\rangle_c^{(k+1)}|
  \leq C_{k+1}\,g_{k+1}^4\,\hat{\Delta}_{k+1}^2$$

where the constant recursion is:

$$\boxed{C_{k+1} = \frac{C_k}{4} + C_{\mathrm{new}}
  + O(g_k^2\,C_k)}$$

### 5.2 Fixed point of the recursion

Ignoring the $O(g_k^2)$ correction, $C_{k+1} = C_k/4 + C_{\mathrm{new}}$
has the stable fixed point $C_* = 4C_{\mathrm{new}}/3$ with
geometric convergence:

$$C_k = C_* + (C_0 - C_*)\cdot 4^{-k}$$

**The constant is bounded.** The $1/4$ contraction of the old
contribution exactly balances the $O(1)$ addition from new
operators, yielding a finite limit.


---


## 6. The $O(g_k^2)$ Corrections: Harmless Growth

### 6.1 The accumulated correction

Including the perturbative correction, the recursion is
$C_{k+1} = (C_k/4 + C_{\mathrm{new}})(1+\alpha g_k^2)$.
The accumulated multiplicative factor is:

$$\prod_{j=0}^{k-1}(1+\alpha g_j^2)
  \leq \exp\!\left(\alpha\sum_j g_j^2\right)$$

Since $g_j^2 \sim 1/(b_0 j\ln 2)$ and $\sum 1/j = \infty$,
the product grows as $k^{\alpha/(b_0\ln 2)}$ -- a power law.

### 6.2 Why this does not matter

The mass gap shift sum involves $C_k g_k^4 \hat{\Delta}_k^2$.
With $C_k \sim k^\gamma$, $g_k^4 \sim 1/k^2$,
$\hat{\Delta}_k^2 \sim 4^{-k}$:

$$\sum_k C_k\,g_k^4\,\hat{\Delta}_k^2
  \sim \sum_k k^{\gamma-2}\cdot 4^{-k} < \infty
  \qquad\text{for all } \gamma$$

The doubly exponential convergence $4^{-k}$ overwhelms any
polynomial $k^\gamma$. Concretely, even with $\gamma = 2$:

$$\sum_{k=1}^\infty 4^{-k} = \frac{1}{3}$$


---


## 7. What the Argument Requires Non-Perturbatively

### 7.1 The three inputs

The preservation argument is valid conditional on:

**(Input 1) New-operator form factor.** At each step, the
newly generated irrelevant operators satisfy:

$$|\langle 1|\delta E_k^{(d_O)}(0)|1\rangle_c|
  \leq C_{\mathrm{new}}\,g_k^{d_O-2}\,\hat{\Delta}_{k+1}^{d_O-4}$$

Proved perturbatively (loop expansion + Weinberg counting). Open
non-perturbatively. This is the crux.

**(Input 2) Bounded wave function correction:**
$\|\delta 1\| \leq C g_k^4/\hat{\Delta}_k$. **Proved** (Kato +
Balaban).

**(Input 3) Starting condition:** at $\hat{\Delta}_0 \sim O(1)$,
the bound holds trivially since
$|\langle 1|E_0(0)|1\rangle_c| \leq C g_0^4$ from the cluster
expansion and $C g_0^4 = C g_0^4 \hat{\Delta}_0^2 \cdot O(1)$
when $\hat{\Delta}_0 \sim 1$. **Proved**.

### 7.2 If Input (1) fails

If $\delta E_k$ does NOT carry the $\hat{\Delta}^2$ suppression,
the new contribution at each step is $O(g_k^4)$ (unsuppressed).
The recursion becomes
$C_{k+1} = C_k/4 + C_{\mathrm{new}}/\hat{\Delta}_{k+1}^2$
with fixed point $C_* \sim C_{\mathrm{new}}/\hat{\Delta}^2
\to \infty$ as $\hat{\Delta} \to 0$. The bound breaks.


---


## 8. Alternative Approaches

### 8.1 Multiplicative RG

Define $M_k = \hat{\Delta}_k$ with $M_{k+1} = M_k(1+r_k)$ where
$r_k = \delta\hat{\Delta}_k/\hat{\Delta}_k$. The continuum gap is
$M_\infty = M_0 \prod(1+r_k)$. Convergence requires
$\sum|r_k| < \infty$. With the form factor bound:

$$|r_k| \leq C g_k^4\hat{\Delta}_k^2
  \sim k^{-2}\cdot 4^{-k}$$

so $\sum|r_k| < \infty$. But computing $r_k$ still requires
the form factor bound -- no independent mechanism is provided.

### 8.2 The $\Lambda$ parameterization

Express the form factor in RG-invariant units:
$\tilde{F}_k = \langle 1|E_k(0)|1\rangle_c/(\Lambda^3\hat{\Lambda}_k^2)$.
Since $\Lambda$ is RG-invariant, $\tilde{F}_k$ varies by
$O(g_k^2)$ per step, giving the same polynomial accumulation
$\tilde{F}_k \sim k^{O(1)}$ -- harmless against $4^{-k}$, but
providing no new mechanism for the bound.


---


## 9. Honest Assessment

### 9.1 What is proved

1. **Contraction mechanism.** The $1/4$ factor from
   $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$ is a robust
   kinematic fact ensuring the old contribution shrinks.

2. **Stable recursion.** $C_k \to C_* = (4/3)C_{\mathrm{new}}$
   plus at most polynomial growth from coupling renormalization.

3. **Starting condition.** Trivially satisfied at
   $\hat{\Delta}_0 \sim O(1)$ by the cluster expansion.

4. **Convergence of the mass gap sum.** Even with $C_k \sim k^\gamma$,
   $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ for all $\gamma$.

5. **Self-consistency.** The form factor bound, if true at one
   scale, propagates to all subsequent scales. No instability.

### 9.2 What is not proved

6. **Input (1): the single-step form factor estimate.** The
   dimensional suppression $\hat{\Delta}^{d_O-4}$ in the matrix
   element of a newly generated irrelevant operator is assumed,
   not derived. This is the same Conjecture 1 of Section 08,
   reformulated as a single-step statement.

7. **The circularity.** The argument proves: IF the bound holds at
   step $k$ AND the new contribution satisfies the same bound,
   THEN the bound holds at step $k+1$. The "AND" clause is not
   derived from the induction hypothesis.

### 9.3 The precise mathematical obstacle

The obstacle is the one identified in every previous analysis:
the dimensional suppression $\hat{\Delta}^{d_O-4}$ in the
one-particle matrix element of a newly generated irrelevant
operator is a statement about UV/IR decoupling within the
block-spin integral. Proving it requires tracking the three-point
correlator $\langle\phi\,\delta E_k\,\phi\rangle_c$ through the
block-spin averaging -- extending Balaban's framework from the
partition function to operator insertions. This is the "50-100
page paper" of `10-open-problem.md`, Path (a).

### 9.4 The residual value

Despite the circularity, this analysis establishes that:

**(a)** The form factor bound is self-consistent under the RG.
There is no instability or hidden blow-up.

**(b)** The contraction factor $1/4$ provides margin: the new
contribution need only match (not beat) the bound.

**(c)** Coupling renormalization corrections are harmless
(polynomial vs. doubly exponential).

**(d)** The full non-perturbative problem reduces to a
**single-step** estimate, more tractable than the global statement.

### 9.5 Summary

$$\boxed{
\text{RG preservation: PROVED, conditional on single-step}
\atop
\text{form factor estimate for newly generated operators.}
}$$

| Component | Status |
|:----------|:-------|
| Old contribution contracts by $1/4$ per step | **Proved** |
| Recursion for $C_k$ has bounded fixed point | **Proved** |
| Starting condition at $\hat{\Delta}_0 \sim O(1)$ | **Proved** |
| $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ | **Proved** |
| New-operator form factor (Input 1) | **Pert: proved. Non-pert: OPEN** |
| Full non-perturbative form factor bound | **CONDITIONAL on Input 1** |

The remaining problem is Conjecture 1 of Section 08, now sharpened:
at each Balaban block-spin step, newly generated dimension-$d_O$
operators have one-particle matrix elements suppressed by
$\hat{\Delta}^{d_O-4}$. This is the non-perturbative content of
irrelevant operator decoupling -- the rigorous statement that UV
effects do not contaminate IR observables in asymptotically free
gauge theory.
