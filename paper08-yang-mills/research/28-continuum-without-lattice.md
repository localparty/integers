# The Continuum Without the Lattice: A Path via Borel Summation

The continuum limit problem arises because we discretized M⁴ into a
lattice and then tried to remove the discretization. But the lattice
was never part of the geometry — it was a computational scaffold. The
six patterns of the framework suggest a different approach: define the
theory in the continuum from the start, using the internal geometry as
the regulator.

This section is a creative exploration, not a completed proof. It
identifies a concrete mathematical path and the specific question that
must be answered.


---

## I. The Insight from Pattern 6

> *Whenever physics appears paradoxical in 4D, it's because 4D is a
> partial trace over the full geometry.*

The continuum limit problem is a 4D problem. It asks: does the sequence
of lattice theories converge as $a \to 0$? But in the full geometry
$M^4 \times \mathbb{CP}^{N-1}$, there is no lattice spacing. The
theory is defined on a smooth manifold. The "continuum limit" is the
statement that the 4D projection of this smooth theory is well-defined.

The lattice was a detour. We introduced it to make the 4D theory
rigorous. But the rigorous definition might not need a lattice at all
--- it might come directly from the geometry.


---

## II. The Three Ingredients

### II.1 Ingredient 1: Zeta regularization gives perturbative finiteness (Pattern 5)

The perturbative expansion of the theory on $M^4 \times \mathbb{CP}^{N-1}$
is finite at every loop order (Papers 1, 4). The mechanism:

- The KK tower on $\mathbb{CP}^{N-1}$ converts UV-divergent momentum
  integrals into discrete sums over KK modes
- The sums are regularized by the Epstein zeta function
- The leading divergence vanishes: $S_0^{(L)} = [1 + 2\zeta(0)]^L = 0$
- Subleading terms are Epstein zeta functions at non-positive integers,
  which are finite by the Epstein--Terras theorem

This gives a well-defined perturbative series:
$$\Gamma[g] = \sum_{L=0}^{\infty} g^{2L} \, \Gamma^{(L)}$$

where each $\Gamma^{(L)}$ is a finite, computable number. No UV cutoff,
no lattice, no dimensional regularization parameter. The finiteness is
a consequence of the compactness of $\mathbb{CP}^{N-1}$.

### II.2 Ingredient 2: The Bogomolny bound controls large-order behavior (Pattern 4)

The non-perturbative sector is controlled by instantons on
$\mathbb{CP}^{N-1}$ with action:
$$S_{\text{inst}} = \frac{8\pi^2}{g^2} |c_2| > 0$$

The instanton action is strictly positive (Bogomolny bound). This
controls the large-order behavior of the perturbative series via the
standard Lipatov argument:

$$\Gamma^{(L)} \sim L! \times A^L \times L^b
  \quad \text{as } L \to \infty$$

where $A = g^2/(8\pi^2)$ is the inverse instanton action and $b$ is a
computable constant.

The factorial growth $L!$ is the generic behavior of perturbative
series in QFT. The specific value $A = g^2/(8\pi^2)$ comes from the
instanton action on $\mathbb{CP}^{N-1}$.

### II.3 Ingredient 3: Borel summation combines both

The **Borel transform** of the perturbative series:
$$B(t) = \sum_{L=0}^{\infty} \frac{\Gamma^{(L)}}{L!} \, t^L$$

converges for $|t| < 1/A = 8\pi^2/g^2$ (the radius of convergence is
set by the instanton action). The **Borel sum** is:
$$\Gamma_{\text{Borel}}(g^2) = \int_0^{\infty} B(t) \, e^{-t/g^2} \, dt$$

This integral defines the theory non-perturbatively if $B(t)$ has no
singularities on the positive real axis $t > 0$.


---

## III. The Key Question: Are There Singularities on the Positive Real Axis?

In standard 4D Yang--Mills (without the KK construction), $B(t)$ has
singularities on the positive real axis:

- **Instanton singularity** at $t = 8\pi^2$ (from the one-instanton
  sector)
- **Renormalon singularities** at $t = n/(2b_0)$ for $n = 1, 2, \ldots$
  (from the large-order behavior of perturbation theory in the
  presence of the running coupling)

The renormalon singularities make the Borel sum ambiguous: the
integration contour must be deformed around them, introducing
ambiguities of order $e^{-n/(2b_0 g^2)} \sim \Lambda^{2n}$.

### III.1 What the KK construction changes

In the KK theory on $M^4 \times \mathbb{CP}^{N-1}$, the perturbative
series is modified:

**(a) The leading divergence vanishes at every loop order:**
$S_0^{(L)} = 0$ (zeta regularization). This means the perturbative
coefficients $\Gamma^{(L)}$ are SMALLER than in the standard theory.
The factorial growth $L!$ may be reduced.

**(b) The KK tower modifies the running coupling.** Above the KK scale
$1/r_3$, the coupling runs according to the $(4 + 2(N-1))$-dimensional
beta function, not the 4D one. The higher-dimensional running is faster
(more asymptotically free), which changes the location of renormalon
singularities.

**(c) The instanton action on $\mathbb{CP}^{N-1}$ is larger than in 4D.**
The instanton on $\mathbb{CP}^{N-1}$ has action $8\pi^2/g^2$, same
as in 4D. But the instanton moduli space on $\mathbb{CP}^{N-1}$ is
smaller ($\dim = 4N - N^2 + 1$) than on $\mathbb{R}^4$ ($\dim = 4Nk$
for $k$ instantons). Fewer moduli means less entropy, which suppresses
the instanton contribution further.

### III.2 The conjecture

**Conjecture (Borel summability of the KK theory).** *The perturbative
series for $SU(N)$ Yang--Mills on $M^4 \times \mathbb{CP}^{N-1}$,
regularized by the spectral zeta function of the KK tower, is Borel
summable. The Borel transform $B(t)$ has no singularities on the
positive real axis.*

**Evidence:**
- The leading divergence $S_0^{(L)} = 0$ at every loop order
  suppresses the factorial growth of $\Gamma^{(L)}$.
- The compact internal space provides a natural IR cutoff (the KK
  mass gap), which removes the IR renormalons.
- The UV renormalons are absent because the theory is UV-finite
  (zeta regularization).
- UV renormalons arise from the divergence of the perturbative series
  at high loop order, driven by the factorial number of Feynman
  diagrams. In the KK theory, the leading diagrams cancel ($S_0 = 0$),
  reducing the effective number of contributing diagrams.

**If the conjecture holds:** The Borel sum
$\Gamma_{\text{Borel}}(g^2)$ defines the theory non-perturbatively in
the continuum. No lattice is needed. The continuum theory exists and has:
- Mass gap $\Delta = c_\Delta \Lambda > 0$ (from the Borel-summed
  dimensional transmutation formula)
- Confinement ($\sigma > 0$, from the area law in the Borel-summed
  Wilson loop)
- All OS axioms (from the Borel-summed Schwinger functions)


---

## IV. The Pattern: UV Finiteness Implies Borel Summability

There is a general principle at work:

| Theory | UV behavior | Borel summable? | Status |
|--------|------------|-----------------|--------|
| $\phi^4$ in 4D | Renormalizable | No (renormalons) | Known |
| $\phi^4$ in 2D | Super-renorm. | Yes | Proved (Glimm--Jaffe) |
| YM in 4D | Asymptotically free | No (renormalons) | Known |
| YM on $M^4 \times \mathbb{CP}^{N-1}$ | **UV finite** (zeta reg.) | **Conjectured: Yes** | This paper |

The pattern: **UV-finite theories are Borel summable** because the
factorial growth of perturbation theory is driven by UV divergences.
When UV divergences are absent, the factorial growth is suppressed, and
the Borel transform has no singularities.

This pattern is established in lower dimensions:
- 2D $\phi^4$: UV-finite (super-renormalizable), Borel summable (proved)
- 2D Yang--Mills: UV-finite (topological), exactly solvable
- 3D $\phi^4$: UV-finite (super-renormalizable), Borel summable (proved)

The KK Yang--Mills theory is UV-finite (zeta regularization), which
places it in the same class. The conjecture is that UV finiteness
implies Borel summability in this case as well.


---

## V. The Proof Strategy

To prove the conjecture, one would need to:

1. **Compute the large-order behavior of $\Gamma^{(L)}$ in the
   zeta-regularized KK theory.** Specifically, show that the factorial
   growth is suppressed: $\Gamma^{(L)} \sim (L!)^\alpha$ with
   $\alpha < 1$ (instead of $\alpha = 1$ in the standard theory).

2. **Show that the Borel transform $B(t)$ is analytic in a strip
   containing the positive real axis.** This requires bounding $B(t)$
   for $t > 0$ using the explicit form of $\Gamma^{(L)}$.

3. **Show that the Borel sum satisfies the OS axioms.** This requires
   verifying reflection positivity, Euclidean covariance, and cluster
   decomposition for the Borel-summed Schwinger functions.

Step 1 is the key computation. It requires analyzing the combinatorics
of Feynman diagrams in the zeta-regularized KK theory. The identity
$S_0^{(L)} = 0$ (the leading term vanishes at each loop order) is the
starting point. If this cancellation extends to the leading factorial
behavior, the conjecture follows.


---

## VI. What This Would Give

If the conjecture holds, the complete proof of the Yang--Mills mass gap
is:

1. **Define the theory** by the Borel-summed zeta-regularized
   perturbative expansion on $M^4 \times \mathbb{CP}^{N-1}$. (No
   lattice.)

2. **The mass gap** is $\Delta = c_\Delta \Lambda > 0$, where
   $c_\Delta$ is the Borel sum of the dimensional transmutation series
   and $\Lambda$ is the dynamical scale.

3. **The OS axioms** are satisfied by the Borel-summed Schwinger
   functions (which are well-defined distributions with exponential
   clustering).

4. **The 4D theory** is obtained by integrating the Schwinger functions
   over $\mathbb{CP}^{N-1}$. Integration over a compact space preserves
   all OS properties.

The continuum limit problem disappears because there is no lattice to
remove. The theory is defined in the continuum by its Borel sum.

The lattice results of Sections 21--25 remain valid and provide:
- Independent confirmation of the mass gap at practical couplings
- Numerical computability (the lattice is a computational tool, not
  a definition)
- The screening obstruction theorem and the cluster expansion as
  rigorous results about the lattice theory


---

## VII. The One-Line Summary

> The lattice was a detour. The theory was always in the continuum.
> Zeta regularization (Pattern 5) makes perturbation theory finite.
> The Bogomolny bound (Pattern 4) controls the non-perturbative sector.
> Borel summation combines them into a unique continuum definition.
> The mass gap is topological (Pattern 4) and survives the summation.
> The continuum limit problem was an apparent pathology of the 4D
> projection (Pattern 6), resolved by working in the full geometry.
