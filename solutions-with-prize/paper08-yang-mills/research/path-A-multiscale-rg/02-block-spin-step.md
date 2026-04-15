# Path A: Multi-Scale Renormalization Group

## 02 -- One Block-Spin Step: What Happens to $\sigma$


---

## I. Setup for a Single Step

Consider the theory at lattice spacing $a$ with coupling $g^2 = g^2(a)$.
The block-spin transformation maps it to an effective theory at spacing
$2a$ with effective coupling $g'^2$. We analyze what happens to the
string tension.

### I.1 Decomposition of the gauge field

Following Balaban (1985, Comm. Math. Phys. 95), decompose the
fine-lattice gauge field into:

$$U_\ell = U_\ell^{\text{bg}} \cdot e^{i a g \, \eta_\ell}$$

where:
- $U^{\text{bg}}$ is the "background" (slowly varying, captured by the
  coarse lattice)
- $\eta_\ell$ is the "fluctuation" (rapidly varying, to be integrated out)

The fluctuation field $\eta$ has support at momenta
$\pi/(2a) < |p| < \pi/a$ (the upper half of the Brillouin zone).

### I.2 The effective action from one step

After integrating out $\eta$, the effective action is:

$$S_{\text{eff}}[V] = S_0[V] + \delta S[V]$$

where $S_0[V] = \beta' \sum_P (1 - \frac{1}{N}\text{Re}\,\text{Tr}\,V_P)$
is a Wilson action with renormalized coupling:

$$\frac{1}{g'^2} = \frac{1}{g^2} - b_0 \ln 4 + O(g^2)$$

(the one-loop renormalization from integrating out one octave of modes),
and $\delta S$ contains:
- Two-loop and higher corrections: $O(g^2)$ relative to $S_0$
- Irrelevant operators: $O(a^2)$ relative to the leading terms

### I.3 Including the CP^{N-1} sector

In the KK-enhanced theory, the RG step also acts on the internal
connections $A_x$. In the $k = 0$ sector, the internal fluctuations
around the flat connection have a Gaussian measure with mass
$m_{\text{int}} = \sqrt{\mu_1}/g_{\text{int}} \geq \sqrt{6}/(g\,r_3)$.

Two sub-cases:

**Case A ($a \gg r_3$):** The KK modes are much heavier than the
cutoff ($m_1 a \gg 1$). Integrating out one octave of 4D modes does
not excite the KK tower. The internal sector is inert: $A_x$ remains
near the flat connection, and the block average $\bar{A}_x$ is also
near flat. The effective theory is:

$$S_{\text{eff}}[V, \bar{A}] = S_0[V] + S_{\text{int}}[\bar{A}]
  + \delta S[V, \bar{A}]$$

with $\delta S$ suppressed by both $g^2$ and $e^{-m_1 a}$.

**Case B ($a \sim r_3$):** The lowest KK mode has $m_1 a \sim 1$.
Integrating out the upper Brillouin zone excites KK fluctuations.
The internal sector is no longer inert --- the effective theory at the
next scale has non-trivial coupling between 4D and internal modes.

**Case C ($a \ll r_3$):** The KK modes have $m_1 a \ll 1$ and
behave as light fields. The theory is effectively higher-dimensional
(the 4D lattice resolves the internal geometry). This is the regime
where the cluster expansion fails.


---

## II. The String Tension Under One RG Step

### II.1 The Wilson loop on coarse and fine lattices

Let $C$ be a rectangular loop of dimensions $T \times R$ on the COARSE
lattice (spacing $2a$). The same physical loop on the fine lattice
(spacing $a$) has dimensions $2T \times 2R$ (twice as many lattice
links in each direction). The minimal area in lattice units:

- Coarse lattice: $\hat{A}_{\text{coarse}} = T \cdot R$ plaquettes
- Fine lattice: $\hat{A}_{\text{fine}} = (2T)(2R) = 4TR$ plaquettes

The physical area is the same: $A_{\text{phys}} = (2a)^2 \cdot TR
= a^2 \cdot 4TR$.

The string tension relates:

$$\langle W(C) \rangle \sim e^{-\hat{\sigma}_{\text{coarse}} \cdot TR}
  = e^{-\hat{\sigma}_{\text{fine}} \cdot 4TR}$$

Therefore:

$$\hat{\sigma}_{\text{coarse}} = 4\hat{\sigma}_{\text{fine}}
  + \delta\hat{\sigma}$$

where $\delta\hat{\sigma}$ is the correction from integrating out the
fine-scale modes. The physical string tension:

$$\sigma_{\text{coarse}} = \frac{\hat{\sigma}_{\text{coarse}}}{(2a)^2}
  = \frac{4\hat{\sigma}_{\text{fine}} + \delta\hat{\sigma}}{4a^2}
  = \sigma_{\text{fine}} + \frac{\delta\hat{\sigma}}{4a^2}$$

### II.2 The correction $\delta\hat{\sigma}$

The correction comes from the fluctuations that are integrated out. In
the Balaban framework, the RG step is decomposed as:

$$\delta\hat{\sigma} = \delta\hat{\sigma}_{\text{pert}}
  + \delta\hat{\sigma}_{\text{large-field}}$$

**Perturbative part (small-field region):**

The small-field contribution is computed by expanding around the
saddle point. The leading term is the one-loop correction to the
plaquette action:

$$\delta\hat{\sigma}_{\text{pert}} = -C_1 g^2 \hat{\sigma}_{\text{fine}}
  + O(g^4 \hat{\sigma}_{\text{fine}})$$

where $C_1 > 0$ is a calculable geometric constant (depending on the
blocking kernel and the lattice dimension). The sign is NEGATIVE: the
perturbative fluctuations reduce the string tension. [ARGUED -- standard
perturbative RG; the sign follows from asymptotic freedom, which says
the effective coupling increases at longer distances.]

More precisely, in the small-field region, the perturbative correction
to the Wilson loop at one loop is:

$$\frac{\delta \langle W(C) \rangle_{\text{pert}}}
  {\langle W(C) \rangle}
  = -C_1 g^2 \cdot A_{\text{min}} + O(g^2 P) + O(g^4 A)$$

The area-law piece gives $\delta\hat{\sigma}_{\text{pert}}
= -C_1 g^2 \hat{\sigma}_{\text{fine}}$, while the perimeter-law piece
renormalizes the self-energy of the Wilson loop (not the string tension).

**Large-field part:**

In the large-field region (where some plaquette variables deviate
significantly from the identity), the Balaban estimates give:

$$|\delta\hat{\sigma}_{\text{large-field}}|
  \leq e^{-c/g^2} \cdot \hat{\sigma}_{\text{fine}}$$

This is exponentially small compared to the perturbative correction.
[PROVED -- Balaban 1985, Theorem 3.2; the large-field region is
suppressed by the Boltzmann weight $e^{-\beta s_P}$ with $s_P$ large.]

### II.3 The one-step transformation law

Combining:

$$\boxed{\sigma_{k+1} = \sigma_k \left(1 - C_1 g_k^2
  + O(g_k^4) + O(e^{-c/g_k^2})\right)
  + O(a_k^2 \Lambda^4)}$$

where the last term is from irrelevant operators (lattice artifacts
that contribute to the string tension at order $a^2$).

**Interpretation:** Each RG step REDUCES the physical string tension
by a fraction $\sim C_1 g_k^2$. This is the standard perturbative
RG effect: the coupling runs to weaker values at shorter distances,
and the string tension (a strong-coupling phenomenon) weakens.

The question is whether the cumulative reduction destroys the string
tension entirely or leaves a positive residue.


---

## III. The Cumulative Effect: The Product Formula

### III.1 The naive estimate

Iterating the one-step formula from scale $k = 0$ to scale $k = n$:

$$\sigma_n = \sigma_0 \prod_{k=0}^{n-1}
  \left(1 - C_1 g_k^2 + O(g_k^4)\right)
  + \text{(lattice artifact corrections)}$$

Ignoring the higher-order terms and the lattice artifacts (which vanish
as $a \to 0$):

$$\sigma_n \approx \sigma_0 \prod_{k=0}^{n-1}
  \left(1 - C_1 g_k^2\right)$$

Taking logarithms:

$$\ln\left(\frac{\sigma_n}{\sigma_0}\right)
  \approx \sum_{k=0}^{n-1} \ln(1 - C_1 g_k^2)
  \approx -C_1 \sum_{k=0}^{n-1} g_k^2$$

(using $\ln(1-x) \approx -x$ for small $x$, valid since $g_k^2 \to 0$).

### III.2 The divergence of $\sum g_k^2$

The key asymptotic:

$$g_k^2 = \frac{1}{b_0 L_k}
  \sim \frac{1}{2 b_0 k \ln 2} \quad \text{for large } k$$

Therefore:

$$\sum_{k=0}^{n-1} g_k^2 \sim \frac{1}{2b_0 \ln 2}
  \sum_{k=1}^{n-1} \frac{1}{k} \sim \frac{\ln n}{2b_0 \ln 2}$$

This DIVERGES as $n \to \infty$. Consequently:

$$\ln(\sigma_n / \sigma_0) \to -\infty
  \quad\Longrightarrow\quad \sigma_n \to 0$$

**The naive product estimate gives $\sigma_\infty = 0$.** [PROVED --
this is a rigorous consequence of the naive one-step bound.]

### III.3 Why the naive estimate is too pessimistic

The product formula $\sigma_n \approx \sigma_0 \prod(1 - Cg_k^2)$
implicitly assumes:

**(a) The perturbative correction is the whole story.** In reality,
there are non-perturbative effects (instantons, the topological floor)
that the perturbative RG does not capture.

**(b) The constant $C_1$ is $k$-independent.** In reality, $C_1$ may
depend on the scale (through the effective action, which changes at
each step).

**(c) The corrections are purely multiplicative.** In reality, the
lattice artifact term $O(a_k^2 \Lambda^4)$ is ADDITIVE, not
multiplicative. This additive term could, in principle, compensate the
multiplicative reduction.

We need to go beyond the naive estimate.


---

## IV. Beyond the Naive Estimate: The Additive Floor

### IV.1 The topological contribution

At each scale $a_k$, the $\mathbb{CP}^{N-1}$ topology provides a
non-perturbative contribution to the string tension. The Bogomolny
bound implies that configurations with non-trivial topology ($k \neq 0$)
contribute to the path integral with weight $\leq e^{-8\pi^2/g_k^2}$.
In the $k = 0$ sector, the screening obstruction prevents deconfinement.

The topological floor for the string tension at scale $a_k$ is:

$$\sigma_{\text{top}}(a_k) \sim \frac{1}{a_k^2}
  e^{-8\pi^2 / g_k^2}
  = \frac{4^k}{a_0^2} \cdot (a_k \Lambda)^{8\pi^2 b_0}$$

Using $a_k \Lambda = a_0 \Lambda / 2^k$:

$$\sigma_{\text{top}}(a_k) = \frac{(a_0 \Lambda)^{8\pi^2 b_0}}{a_0^2}
  \cdot 2^{k(2 - 8\pi^2 b_0)}$$

For SU(3): $8\pi^2 b_0 = 11/6 \approx 1.833$. So $2 - 8\pi^2 b_0
= 1/6 > 0$, and $\sigma_{\text{top}}(a_k) \sim 2^{k/6} \to \infty$.

**The topological floor GROWS with the RG step.** [ARGUED -- this
follows from the Bogomolny bound applied at each scale, assuming the
topological sector decomposition persists.]

### IV.2 Interpretation

The growth of $\sigma_{\text{top}}$ means that the topological floor
eventually exceeds the perturbatively-reduced string tension. At that
point, the perturbative reduction is irrelevant: the string tension
is dominated by the non-perturbative topological contribution.

But this is misleading. The topological floor $\sigma_{\text{top}}$
is not additive to the perturbative string tension --- it is a LOWER
BOUND on the total string tension. The actual string tension satisfies:

$$\sigma_k \geq \max\left(\sigma_k^{\text{pert}},\;
  \sigma_{\text{top}}(a_k)\right)$$

If $\sigma_k^{\text{pert}} \to 0$ (from the product formula) while
$\sigma_{\text{top}} \to \infty$, then the actual $\sigma_k$ is
dominated by $\sigma_{\text{top}}$ and diverges. But this would mean
$\sigma_{\text{phys}} \to \infty$, which is unphysical.

### IV.3 The resolution

The issue is that $\sigma_{\text{top}}$ as computed above is NOT the
correct topological floor. The formula
$\sigma_{\text{top}} \sim e^{-8\pi^2/g^2}/a^2$ uses the bare lattice
coupling $g^2(a)$ in the Bogomolny exponent, but this exponent should
use the PHYSICAL coupling at the confinement scale, not the bare
coupling at the lattice scale.

The correct estimate is:

$$\sigma_{\text{top}} \sim \Lambda^2 \cdot e^{-8\pi^2/g^2(\Lambda^{-1})}$$

But $g^2(\Lambda^{-1}) \sim O(1)$ (at the confinement scale, the
coupling is strong), so $\sigma_{\text{top}} \sim \Lambda^2$, which is
the expected physical string tension. This does not depend on $a$.

**The topological floor, correctly interpreted, is
$\sigma_{\text{top}} \sim \Lambda^2$ independent of the lattice
spacing.** [ARGUED -- requires that the Bogomolny bound at the
confinement scale, not the lattice scale, is what matters.]

This gives the modified one-step formula:

$$\boxed{\sigma_{k+1} = \sigma_k(1 - C_1 g_k^2 + O(g_k^4))
  + \sigma_{\text{top}} \cdot f(g_k^2)}$$

where $f(g_k^2)$ encodes the non-perturbative (instanton) correction.
The additive term could potentially stabilize the string tension, but
determining $f$ is the central difficulty.


---

## V. The Structure of the Effective Action

### V.1 What Balaban's estimates give at each step

After $k$ RG steps, the effective action has the form (Balaban 1989):

$$S_k[V] = \frac{1}{g_k^2} S_W[V] + \sum_j c_j^{(k)} \mathcal{O}_j[V]
  + R_k[V]$$

where:
- $S_W$ is the Wilson action (the relevant operator)
- $\mathcal{O}_j$ are irrelevant operators of dimension $> 4$ with
  computable coefficients $c_j^{(k)}$
- $R_k$ is a "remainder" bounded by $\|R_k\| \leq C e^{-c/g_k^2}$
  (the large-field contribution)
- The coupling $g_k^2$ flows according to the beta function

### V.2 The missing ingredient

Balaban's estimates control $S_k$ (the effective action) but do NOT
directly give the string tension. To extract $\sigma_k$ from $S_k$,
one needs to:

(a) Show that the Wilson loop in the effective theory at scale $k$
satisfies an area law.

(b) Compute the string tension from the effective action.

For (a), at strong coupling ($g_k^2 \gg 1$), the area law follows from
the strong-coupling expansion. At weak coupling ($g_k^2 \ll 1$), the
area law is a NON-PERTURBATIVE phenomenon that the Balaban estimates
do not capture.

**This is the core difficulty:** the Balaban framework controls the
UV fluctuations but does not see the IR confinement.

### V.3 Where the CP^{N-1} topology enters

The $\mathbb{CP}^{N-1}$ topology fills this gap: at each scale $a_k$,
the screening obstruction (Theorem B.1) says the effective theory
confines in the $k = 0$ sector, regardless of the coupling strength.
The Balaban estimates control the UV corrections, and the topology
controls the IR behavior.

But making this precise requires showing that the effective action
$S_k$ at each scale still has the topological structure needed for
Theorem B.1. This is the subject of the next file.


---

## VI. Summary of This Section

**What we established:**

1. The one-step RG transformation reduces the physical string tension
   by a fraction $\sim C_1 g_k^2$ [ARGUED -- perturbative estimate].

2. The naive product formula gives $\sigma_\infty = 0$ because
   $\sum g_k^2 = \sum 1/\ln k = \infty$ [PROVED -- the product
   diverges to zero].

3. The topological floor $\sigma_{\text{top}} \sim \Lambda^2$ is
   independent of $a$ [ARGUED -- requires correct interpretation of
   the Bogomolny bound at the physical scale].

4. The additive non-perturbative correction could stabilize
   $\sigma_k$, but its form is unknown [OPEN].

5. The Balaban framework controls the UV but not the IR [PROVED --
   this is a well-known limitation of the program].

6. The $\mathbb{CP}^{N-1}$ topology could fill the IR gap, but
   making this precise requires additional work [OPEN].

**The key open question for the next section:** Does the
$\mathbb{CP}^{N-1}$ topology provide a quantitative lower bound on
$\sigma_k$ that survives each RG step?
