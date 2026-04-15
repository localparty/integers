# 06. Does the 4D Lattice String Tension Converge to the Worldsheet Prediction?

## The Problem

Even if the worldsheet formula $\sigma_\infty = f(N) m_{2D}^2$ defines
a positive target value, we still need:

$$\lim_{a \to 0} \sigma_{\text{phys}}(a) = \sigma_\infty$$

This is a statement about the convergence of the lattice approximation.
The worldsheet bootstrap SEPARATES this from the existence question
(what IS $\sigma_\infty$?), but the convergence still needs to be proved.


---

## 6.1 What We Know About the Lattice String Tension

**6.1.1 Lattice string tension is positive.** [PROVED]

From Sections 21-25: $\sigma_{\text{phys}}(a) > 0$ for all
$a > a_{\text{cross}} \sim 10^{-29}$ m. This covers all practical
lattice spacings.

**6.1.2 Lattice string tension is smooth.** [PROVED]

The cluster expansion (Section 25) proves that the free energy is
analytic in $\beta$ for $a \gg r_3$. Since $\sigma$ is extracted from
the free energy, it is a smooth function of $\beta(a)$.

**6.1.3 Lattice string tension shows asymptotic scaling.** [PROVED
numerically]

Lattice QCD simulations (for $N = 3$) show:
$$\sigma_{\text{phys}}(a) \approx (440 \text{ MeV})^2
  \times (1 + O(a^2 \sigma))$$

for $a$ in the range $0.05$ fm to $0.2$ fm. The scaling violations are
$O(a^2)$ (Symanzik), consistent with the continuum limit existing.

Specifically, the lattice data from Necco--Sommer (2002) and
Luscher--Sommer--Wolff--Weisz (1994) show:

| $a$ (fm) | $\sqrt{\sigma} a$ | $\sqrt{\sigma}$ (MeV) |
|----------|-------------------|----------------------|
| 0.200 | 0.440 | 434 |
| 0.100 | 0.221 | 440 |
| 0.050 | 0.110 | 442 |

The variation is $< 2\%$ over a factor of 4 in lattice spacing. This
is strong numerical evidence for convergence, but not a proof.


---

## 6.2 The Standard Argument for Convergence

The physics argument for convergence goes as follows.

**6.2.1 The Symanzik expansion.** [ARGUED]

The lattice theory at spacing $a$ differs from the continuum theory by
irrelevant operators:
$$S_{\text{lat}}(a) = S_{\text{cont}} + a^2 \sum_i c_i O_i^{(6)}
  + a^4 \sum_j c_j O_j^{(8)} + \ldots$$

where $O_i^{(d)}$ are local operators of dimension $d > 4$. The
coefficients $c_i$ are computable in perturbation theory.

The string tension receives corrections:
$$\sigma_{\text{phys}}(a) = \sigma_\infty
  + a^2 \sum_i c_i \langle O_i^{(6)} \rangle + O(a^4)$$

Since $\langle O_i^{(6)} \rangle$ are finite in the continuum limit (they
are matrix elements of local operators in a massive theory), the
corrections vanish as $a \to 0$:
$$\sigma_{\text{phys}}(a) = \sigma_\infty + O(a^2)$$

**The gap in this argument:** The Symanzik expansion ASSUMES that the
continuum limit $\sigma_\infty$ exists and then shows that the approach
is $O(a^2)$. It does not prove the existence of the limit. This is the
circularity noted in Section 32 of the paper.

**6.2.2 The Callan--Symanzik equation.** [ARGUED]

The physical string tension satisfies the Callan--Symanzik equation:
$$\left(\mu \frac{\partial}{\partial\mu}
  + \beta(g) \frac{\partial}{\partial g}\right) \sigma_{\text{phys}} = 0$$

This says that $\sigma_{\text{phys}}$ is RG-invariant. Combined with
asymptotic freedom ($\beta(g) = -b_0 g^3 + \ldots$), this gives:
$$\sigma_{\text{phys}} = \Lambda^2 \times f(g(\mu))$$

where $f$ is a dimensionless function. If $f$ has a finite limit as
$g \to 0$, then $\sigma_{\text{phys}} \to \Lambda^2 f(0)$ = const.

**The gap:** Proving that $f(0)$ is finite and positive requires
non-perturbative control of the RG flow. Perturbatively, $f(g) = c_0 +
c_1 g^2 + \ldots$, but the perturbative series is not Borel summable
(Section 29 of the paper). Non-perturbatively, $f$ could have essential
singularities at $g = 0$.


---

## 6.3 The Worldsheet Approach to Convergence

The worldsheet bootstrap provides a NEW argument for convergence that
does NOT use the Symanzik expansion or the Callan--Symanzik equation.

**6.3.1 The strategy.** [ARGUED]

Define the target:
$$\sigma_\infty = f(N) \times m_{2D}^2$$

This is a specific positive number, defined by the 2D model. Now show:

$$|\sigma_{\text{phys}}(a) - \sigma_\infty| \to 0 \quad (a \to 0)$$

The key idea: use the LATTICE THEORY for the 2D model as an intermediary.

**6.3.2 The intermediary: 2D lattice.** [ARGUED]

The 2D $\mathbb{CP}^{N-1}$ model on a lattice with spacing $a_{2D}$
has a mass gap:
$$m_{2D}(a_{2D}) = m_{2D,\text{cont}} + O(a_{2D}^2)$$

The convergence of the 2D lattice to the 2D continuum is MUCH better
controlled than the 4D convergence:
- At $N = \infty$: proved rigorously (Singer 1995)
- At finite $N$: proved for the $O(N)$ cousin (Gawedzki--Kupiainen 1985);
  expected for $\mathbb{CP}^{N-1}$

**6.3.3 The matching argument.** [ARGUED]

Consider the 4D lattice at spacing $a$. The worldsheet of the confining
string is a 2D object that "sees" the lattice structure. The effective
2D lattice spacing for the worldsheet is:
$$a_{2D}^{\text{eff}} = a \times \sqrt{\sigma}$$

(the worldsheet lattice spacing is the 4D lattice spacing times the
string tension, which converts 4D lengths to worldsheet units).

At the worldsheet level: the worldsheet mass gap $m_{2D}$ is computed
on a lattice with spacing $a_{2D}^{\text{eff}}$. As $a \to 0$:
$a_{2D}^{\text{eff}} \to 0$ (assuming $\sigma$ stays bounded), and the
2D lattice mass gap converges to the 2D continuum mass gap:
$$m_{2D}(a_{2D}^{\text{eff}}) \to m_{2D,\text{cont}}$$

Therefore:
$$\sigma_{\text{phys}}(a) = f(N) \times m_{2D}(a_{2D}^{\text{eff}})^2
  \to f(N) \times m_{2D,\text{cont}}^2 = \sigma_\infty$$

**6.3.4 The circularity issue.** [HONEST ASSESSMENT]

Wait. The argument in 6.3.3 is ALSO circular, just in a different way.
It assumes that the worldsheet description is valid at EVERY lattice
spacing $a$, not just in the continuum limit. If the worldsheet
description fails at some intermediate scale $a_*$, the matching
argument breaks down.

Let me be precise about what is assumed:

*Assumption W (Worldsheet validity):* For all $a$ in the range
$(0, a_0)$ for some $a_0 > 0$, the 4D string tension on the lattice
with spacing $a$ satisfies:
$$\sigma_{\text{phys}}(a) = f(N) \times m_{2D}(a_{\text{eff}}(a))^2
  + \epsilon(a)$$

where $|\epsilon(a)| \leq C a^2 \sigma_\infty$ (the worldsheet
description has at most $O(a^2)$ corrections).

Under Assumption W, convergence follows immediately:
$$|\sigma_{\text{phys}}(a) - \sigma_\infty|
  \leq f(N) |m_{2D}(a_{\text{eff}})^2 - m_{2D,\text{cont}}^2|
  + C a^2 \sigma_\infty$$

Both terms go to zero as $a \to 0$. The first because the 2D lattice
converges; the second by definition.

But Assumption W is itself [OPEN]. It is a statement about the quality
of the effective string description at finite lattice spacing.


---

## 6.4 A Different Approach: Monotonicity

Is there a monotonicity argument that avoids Assumption W?

**6.4.1 Wishful monotonicity.** If $\sigma_{\text{phys}}(a)$ were
MONOTONE in $a$ (either increasing or decreasing as $a \to 0$), then
convergence would follow from boundedness:
- We know $\sigma_{\text{phys}}(a) > 0$ (lower bound) [PROVED]
- We expect $\sigma_{\text{phys}}(a) \leq C/r_3^2$ (upper bound from
  the KK scale) [ARGUED]
- A monotone bounded sequence converges [PROVED --- real analysis]

**6.4.2 Is monotonicity true?** [OPEN, probably not exactly]

The lattice data show $\sigma_{\text{phys}}(a)$ is approximately
constant as $a$ varies, with small $O(a^2)$ oscillations. It is NOT
strictly monotone --- the Symanzik corrections can have either sign,
and the improved action shows non-monotone approach to the continuum.

So strict monotonicity fails. However, APPROXIMATE monotonicity might
hold:

**Quasi-monotonicity.** If for all $a < a_0$:
$$\sigma_{\text{phys}}(a/2) \geq \sigma_{\text{phys}}(a)
  - C a^2 \sigma_{\text{phys}}(a)$$

(the string tension at finer lattice is at least as large as at coarser
lattice, up to $O(a^2)$ corrections), then:
$$\sigma_{\text{phys}}(a/2^n) \geq \sigma_{\text{phys}}(a)
  \prod_{k=0}^{n-1} (1 - C (a/2^k)^2) > 0$$

The product converges because $\sum_k (a/2^k)^2 = a^2 \sum_k 4^{-k}
= 4a^2/3 < \infty$. So:
$$\sigma_{\text{phys}}(a/2^n) \geq \sigma_{\text{phys}}(a)
  \times e^{-4Ca^2/3} > 0$$

This gives a POSITIVE lower bound uniform in $n$, proving $\sigma_\infty
\geq \delta > 0$.

**6.4.3 Can we prove quasi-monotonicity?** [OPEN but promising]

Quasi-monotonicity is a statement about the block-spin RG: coarsening
from $a$ to $2a$ changes $\sigma$ by at most $O(a^2)$. This is
essentially the statement that the Symanzik expansion has bounded
coefficients, which is a consequence of:
- UV stability (proved by Balaban)
- Exponential clustering (proved from the mass gap)
- Bounded lattice artifacts (expected from asymptotic freedom)

The combination of these results should give quasi-monotonicity, but
the detailed proof requires the multi-scale analysis of Path A.


---

## 6.5 The Hybrid Approach

The most promising approach to lattice convergence combines the
worldsheet and the multi-scale RG:

**Step 1.** Use the worldsheet to define $\sigma_\infty = f(N) m_{2D}^2$.
[ARGUED]

**Step 2.** Use the lattice proof (Sections 21-25) to establish
$\sigma_{\text{phys}}(a) > 0$ for $a > a_{\text{cross}}$. [PROVED]

**Step 3.** Use the multi-scale RG (Path A) to propagate the lower
bound from $a_{\text{cross}}$ toward $a = 0$. At each step, the
topological obstruction (screening theorem) prevents $\sigma$ from
reaching zero. [ARGUED --- needs Balaban-type estimates]

**Step 4.** Show that the sequence $\sigma_{\text{phys}}(a_n)$ along a
geometric sequence $a_n = a_0 / 2^n$ has a unique accumulation point
(by compactness) and that this point equals $\sigma_\infty$ (by matching
to the worldsheet prediction at each scale). [OPEN]

The virtue of this approach is that it uses different tools at different
scales:
- At $a \gg r_3$: the cluster expansion [PROVED]
- At $a \sim r_3$: the multi-scale RG [OPEN, Path A]
- At $a \ll r_3$: the worldsheet description [ARGUED]

Each tool covers a different regime, and together they span the full
range $a \in (0, \infty)$.


---

## 6.6 What Would Constitute a Proof?

Let me state precisely what is needed.

**Theorem (desired).** *For $SU(N)$ lattice Yang--Mills theory with
coupling $\beta(a)$ on the asymptotic freedom trajectory, the physical
string tension converges:*
$$\sigma_\infty = \lim_{a \to 0} \sigma_{\text{phys}}(a) > 0$$

**Proof structure (worldsheet bootstrap):**

1. **Define** $\sigma_\infty = f(N) m_{2D}^2$ where $m_{2D}$ is the
   continuum mass gap of the 2D $\mathbb{CP}^{N-1}$ model and $f(N)$ is
   a computable function. [Requires: proving the worldsheet formula]

2. **Prove** that $m_{2D,\text{cont}} > 0$. [Done at $N = \infty$;
   requires rigorous construction of the 2D continuum theory at finite $N$]

3. **Prove** that $|\sigma_{\text{phys}}(a) - \sigma_\infty| \leq
   C(a)$ where $C(a) \to 0$. [Requires: either Assumption W (worldsheet
   valid at all $a$) or multi-scale RG estimates]

**Minimal proof (existence of positive limit, without identifying its
value):**

1. **Prove** $\sigma_{\text{phys}}(a) > 0$ for all $a > 0$.
   [Currently proved for $a > a_{\text{cross}}$; needs extension]

2. **Prove** $\sigma_{\text{phys}}(a) \leq C$ uniformly.
   [Expected from the KK geometry; ARGUED]

3. **Prove** quasi-monotonicity or existence of a convergent subsequence.
   [Follows from compactness if $\sigma$ is uniformly bounded; ARGUED]

4. **Prove** uniqueness of the limit (no oscillation).
   [Requires universality, which is the hardest step]

The minimal proof does not use the worldsheet formula at all --- it
just needs uniform bounds and compactness. But it does not identify
the value of $\sigma_\infty$.


---

## 6.7 Summary

| Approach | What it gives | Status |
|----------|--------------|--------|
| Symanzik expansion | $\sigma(a) = \sigma_\infty + O(a^2)$ | **Circular** (assumes $\sigma_\infty$ exists) |
| Callan--Symanzik | $\sigma = \Lambda^2 f(0)$ | **Requires** $f(0)$ finite and positive |
| Worldsheet matching | $\sigma(a) = f(N) m_{2D}(a_{\text{eff}})^2 + O(a^2)$ | **Requires** Assumption W |
| Monotonicity | $\sigma_\infty \geq \delta > 0$ | **Requires** quasi-monotonicity (not proved) |
| Compactness | Convergent subsequence exists | **Proved** (if $\sigma$ uniformly bounded) |
| Hybrid (multi-scale + worldsheet) | Full convergence | **Most promising**, combines all tools |

The lattice convergence is the hardest step in the worldsheet bootstrap.
It requires either an independent proof (multi-scale RG) or a proof
that the worldsheet description is valid at all lattice spacings
(Assumption W). Both are open.

However, the worldsheet bootstrap reduces the CONCEPTUAL problem: the
question is no longer "does $\sigma_\infty$ exist and what is it?" but
rather "does the lattice approximate the known target $\sigma_\infty =
f(N) m_{2D}^2$?" This is a question about approximation theory, not
about the physics of confinement.
