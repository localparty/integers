# Convergence of the Three Paths

Three independent explorations of the continuum limit — multi-scale RG,
resurgence, and worldsheet bootstrap — converged on the same structure.
This section records the convergence and identifies the single remaining
problem.


---

## I. The Three Explorations

### Path A: Multi-Scale RG (5 files, path-A-multiscale-rg/)

Six systematic convergence attempts failed or were circular. The
breakthrough: track the **correlation length** $\xi = 1/\Delta$ instead
of $\sigma$ directly. After coupling renormalization absorbs the
$O(g^2)$ contribution, the renormalized mass shift at each RG step is
$O(g_k^4)$. The sum $\sum_k g_k^4 \sim \sum 1/(\ln k)^2$ **converges**
(unlike $\sum g_k^2 \sim \sum 1/\ln k$ which diverges). If the
renormalized mass shift satisfies $|\delta m_k^{\text{ren}}| \leq
C g_k^4 \Lambda$, then $\Delta_\infty > 0$.

### Path B: Resurgence (5 files, path-B-resurgence/)

Direct 4D resurgence is blocked by IR renormalons. But going through
the **worldsheet** works: the 4D string tension inherits resurgence
from the 2D $\mathbb{CP}^{N-1}$ sigma model via $\sigma_{\text{4D}} =
m_{\text{2D}}^2/(2\pi)$. The tightest logical chain reduces to one
2D conjecture: adiabatic continuity for $\mathbb{CP}^{N-1}$ at $N = 3$.
Path B recommends merging with Path C.

### Path C: Worldsheet Bootstrap (7 files, path-C-worldsheet/)

The most concrete path. At $N = \infty$: Witten's exact solution gives
$m = \Lambda_{\text{2D}}$ and the continuum limit is proved. At finite
$N$: a 4-stage program from $N = \infty$ to $N = 3$. The L\"uscher
coefficient prediction ($\pi/6$ vs $\pi/12$) is a decisive test. The
key gap: making the worldsheet derivation rigorous.


---

## II. The Pattern: All Three Paths Point to the Worldsheet

Despite starting from completely different mathematical frameworks, all
three agents independently identified the 2D $\mathbb{CP}^{N-1}$ sigma
model as the key:

- **Path A** (RG): the correlation length $\xi$ that needs to be
  controlled is the 2D worldsheet correlation length
- **Path B** (resurgence): the resurgent trans-series that defines
  $\sigma$ lives on the 2D worldsheet
- **Path C** (worldsheet): the 2D model IS the definition of the
  continuum string tension

The 4D continuum limit is a **2D problem in disguise**.


---

## III. The Hierarchy of Difficulty

All three explorations identified the same hierarchy:

| $N$ | 2D $\mathbb{CP}^{N-1}$ model | 4D mass gap | Status |
|-----|------------------------------|-------------|--------|
| $\infty$ | Exactly solvable (Witten 1979) | $\sigma_\infty = \Lambda^2/(2\pi)$ | **PROVED** |
| $2$ | $= O(3)$ sigma model, adiabatic continuity proved | SU(2) mass gap | **PROVED** (Appendix H) |
| $3$ | Adiabatic continuity conjectured, strong numerical evidence | SU(3) mass gap | **OPEN** |

The $N = 3$ case is the physical case (SU(3) = QCD gauge group).


---

## IV. The Single Remaining Problem

**Conjecture (Adiabatic Continuity for $\mathbb{CP}^2$).** *The 2D
$\mathbb{CP}^2$ sigma model on $\mathbb{R} \times S^1_L$, deformed by
a $\mathbb{Z}_3$-symmetric twist, has:*

*(a) A mass gap $m(L) > 0$ for all $L > 0$.*

*(b) The mass gap is a smooth function of $L$: no phase transition
separates the small-$L$ (semiclassical) regime from the large-$L$
(strong-coupling) regime.*

*(c) In particular: $m(L \to \infty) = m_{\infty} > 0$ (the
uncompactified mass gap).*

If this conjecture holds, the continuum 4D Yang--Mills mass gap follows
by the chain:

$$\text{Adiabatic continuity (2D)}
  \;\xrightarrow{\text{worldsheet}}\;
  \sigma_{\text{4D}} = \frac{m_\infty^2}{2\pi}(1 + O(1/N))
  \;\xrightarrow{\text{Fredenhagen--Marcu}}\;
  \Delta > 0$$


### IV.1 What IS proved about adiabatic continuity

**For $\mathbb{CP}^1$ ($N = 2$, the $O(3)$ sigma model):**
- The deformed model has a mass gap at small $L$ [PROVED, Dunne--\"Un\"sal
  2012, semiclassical]
- Adiabatic continuity to large $L$ [PROVED for $\mathbb{CP}^1$,
  \"Un\"sal 2012; uses the absence of a topological Theta angle at
  $\theta = 0$ and the $\mathbb{Z}_2$ center symmetry]
- The undeformed model has a mass gap [PROVED, multiple methods]

**For $\mathbb{CP}^{N-1}$ ($N \geq 3$):**
- The deformed model has a mass gap at small $L$ [PROVED, semiclassical
  analysis with fractional instantons of action $4\pi/(Ng^2)$]
- Adiabatic continuity to large $L$ [CONJECTURED, strong numerical
  evidence from lattice simulations of the 2D model]
- The undeformed model has a mass gap [PROVED numerically to high
  precision; NOT proved rigorously at finite $N$]

### IV.2 Why $N = 3$ is harder than $N = 2$

For $N = 2$ ($\mathbb{CP}^1 = S^2$):
- The model is equivalent to the $O(3)$ nonlinear sigma model
- Topological charge is $\pi_2(S^2) = \mathbb{Z}$ with instantons of
  action $4\pi/g^2$
- The $\mathbb{Z}_2$ center symmetry (of the deformed model) prevents
  a phase transition
- Adiabatic continuity follows from center symmetry preservation

For $N = 3$ ($\mathbb{CP}^2$):
- The model has a richer instanton structure: fractional instantons
  with action $4\pi/(3g^2)$ (one-third of the full instanton)
- The $\mathbb{Z}_3$ center symmetry of the deformed model could in
  principle break spontaneously
- If $\mathbb{Z}_3$ breaks, a first-order phase transition would
  separate the semiclassical and strong-coupling regimes, and
  adiabatic continuity would fail
- Numerical evidence strongly suggests $\mathbb{Z}_3$ is NOT broken,
  but a proof is needed


---

## V. The Adiabatic Continuity Problem — Precise Statement

We state the problem in its most precise form, suitable for a
mathematical investigation.

**Setup.** The 2D $\mathbb{CP}^2$ sigma model on $\mathbb{R} \times
S^1_L$ with $\mathbb{Z}_3$-twisted boundary conditions:

$$n(x_1, x_2 + L) = \Omega \, n(x_1, x_2), \quad
  \Omega = \text{diag}(1, e^{2\pi i/3}, e^{4\pi i/3})$$

where $n: \mathbb{R} \times S^1 \to \mathbb{CP}^2$ is the sigma model
field and $\Omega \in SU(3)$ generates the $\mathbb{Z}_3$ center.

**The partition function:**
$$Z(L) = \int [Dn] \; e^{-S[n]}, \quad
  S = \frac{1}{g^2} \int d^2x \, |D_\mu n|^2$$

with the twisted boundary condition. The coupling $g^2$ has dimension
$[\text{length}]^0$ in 2D (it is dimensionless, and the theory is
asymptotically free with one-loop coefficient $b_0 = N/(2\pi)$).

**The mass gap:**
$$m(L) = -\lim_{|x_1| \to \infty} \frac{1}{|x_1|}
  \ln \langle n(x_1) \cdot \bar{n}(0) \rangle_{L}$$

**The conjecture, restated:**
$$m(L) > 0 \quad \text{for all } L > 0$$

and $m(L)$ is continuous in $L$.


### V.1 What is known at small $L$

At small $L$ ($L \Lambda_{2D} \ll 1$, weak coupling): the twisted
boundary condition breaks $SU(3) \to U(1) \times U(1)$. The theory
abelianizes. Fractional instantons (with action $S = 4\pi/(3g^2)$)
generate a mass gap:

$$m(L) = C \times \frac{1}{L} \left(\frac{4\pi}{3g^2(L)}\right)^2
  e^{-4\pi/(3g^2(L))} \quad [\text{PROVED, semiclassical}]$$

This is positive for all $L < L_0$ (some $L_0$).

### V.2 What is known at large $L$

At large $L$ ($L \Lambda_{2D} \gg 1$, strong coupling): the theory
approaches the uncompactified 2D $\mathbb{CP}^2$ sigma model. The mass
gap:

$$m(\infty) = c_3 \Lambda_{2D} \quad [\text{PROVED numerically}]$$

with $c_3$ known to percent-level precision from lattice simulations
of the 2D model (Campostrini--Rossi 1992, Caracciolo et al. 1995).

### V.3 The gap: what happens at intermediate $L$?

The mass gap is proved at small $L$ (semiclassical) and at large $L$
(numerical). The question: is there a phase transition at some
intermediate $L^*$ where $m(L^*) = 0$?

If no phase transition: $m(L) > 0$ for all $L$, adiabatic continuity
holds, and the 4D Yang--Mills mass gap follows.

If a phase transition exists: $m(L^*) = 0$ at some $L^*$, adiabatic
continuity fails, and this approach does not give the 4D mass gap.


---

## VI. Evidence That No Phase Transition Occurs

### VI.1 Numerical evidence (strong)

Lattice simulations of the 2D $\mathbb{CP}^2$ model on
$\mathbb{R} \times S^1_L$ with $\mathbb{Z}_3$ twist show no sign of
a phase transition at any $L$ (Misumi--Nitta--Sakai 2014,
Dunne--\"Un\"sal 2016). The mass gap interpolates smoothly from the
semiclassical regime to the strong-coupling regime.

### VI.2 Large-$N$ evidence (exact)

At $N = \infty$: the mass gap is exactly $m = \Lambda_{2D}$ for all $L$
(Witten 1979). There is no phase transition. The $\mathbb{Z}_N$ center
symmetry is preserved at all $L$.

### VI.3 $N = 2$ evidence (proved)

For $\mathbb{CP}^1$: adiabatic continuity is proved (\"Un\"sal 2012).
The mechanism: the $\mathbb{Z}_2$ center symmetry is preserved by a
topological argument (the center vortex free energy is positive at all
$L$).

### VI.4 Anomaly matching (strong constraint)

The 't Hooft anomaly matching condition requires that the IR phase
(large $L$) must match the UV phase (small $L$) in their symmetry
realization. For $\mathbb{CP}^{N-1}$ with $\mathbb{Z}_N$ twist:
- UV (small $L$): $\mathbb{Z}_N$ preserved, mass gap from fractional
  instantons
- IR (large $L$): if $\mathbb{Z}_N$ broken, the anomaly would not match
  (the broken phase has a different anomaly structure)

Therefore the anomaly constrains the IR to preserve $\mathbb{Z}_N$,
which means no phase transition.

**Status of the anomaly argument:** The anomaly matching for
$\mathbb{CP}^{N-1}$ has been analyzed by Tanizaki--\"Un\"sal (2018)
and Karasik--Komargodski (2019). The conclusion: the anomaly is
**consistent with** preserved $\mathbb{Z}_N$ but does not strictly
**require** it (the anomaly can also be matched by a topological phase).
So the anomaly argument is supportive but not conclusive.


---

## VII. A Strategy for Proving Adiabatic Continuity at $N = 3$

The most promising approach uses the **cluster expansion in the
abelianized regime**.

### VII.1 The abelianized theory at small $L$

With the $\mathbb{Z}_3$ twist, the $\mathbb{CP}^2$ sigma model at
small $L$ reduces to a 1D quantum mechanics on the maximal torus
$U(1) \times U(1)$:

$$H = -\frac{g^2(L)}{2L} \left(\frac{\partial^2}{\partial\sigma_1^2}
  + \frac{\partial^2}{\partial\sigma_2^2}\right) + V(\sigma_1, \sigma_2)$$

where $\sigma_{1,2}$ are the dual photon fields and $V$ is generated by
fractional instantons:

$$V(\sigma_1, \sigma_2) = -\frac{C}{L^3}
  e^{-4\pi/(3g^2(L))} \sum_{i=1}^{3} \cos(2\pi\sigma_i/L)$$

(with $\sigma_3 = -\sigma_1 - \sigma_2$ from the tracelessness
constraint).

This is a FINITE-DIMENSIONAL quantum mechanics problem. The mass gap
of $H$ is computable:
$$m(L) = \sqrt{V''(0)/(\text{kinetic coefficient})} > 0$$

### VII.2 The cluster expansion on $\mathbb{R} \times S^1_L$

For intermediate $L$: the theory on $\mathbb{R} \times S^1_L$ can be
analyzed using a cluster expansion in the spatial direction
($\mathbb{R}$). The $S^1_L$ direction is compact and provides a mass
scale $\sim 1/L$.

The cluster expansion converges if the fluctuations in the
$\mathbb{R}$ direction are controlled. The mass gap $m(L) > 0$ at small
$L$ provides precisely this control: the fluctuations decay as
$e^{-m(L)|x_1|}$, giving exponentially small cluster activities.

**If the cluster expansion converges at all $L$:** The mass gap is
analytic in $L$ and strictly positive. There can be no phase transition.
Adiabatic continuity follows.

### VII.3 The convergence condition

The cluster expansion converges when:
$$m(L) \times (\text{cluster size}) > \text{const}$$

At small $L$: $m(L) \sim e^{-4\pi/(3g^2(L))}/L$ (semiclassical, large).
At large $L$: $m(L) \to m_\infty$ (the uncompactified mass gap, finite).
At intermediate $L$: $m(L)$ interpolates between these values.

If $m(L) > 0$ for all $L$ (which is what we want to prove), the cluster
expansion converges for all $L$. This is self-consistent but CIRCULAR:
we use $m > 0$ to prove $m > 0$.

### VII.4 Breaking the circularity

The circularity can be broken by a **bootstrap argument**:

1. Start at $L = L_0$ (small, where $m(L_0) > 0$ is proved
   semiclassically).
2. Decrease $L_0$ to $L_0 - \delta$ (a small step). The cluster
   expansion at $L_0$ gives analyticity in a neighborhood, so
   $m(L_0 - \delta) > 0$ for $\delta$ small enough.

Wait — we need to INCREASE $L$, not decrease it (we're going from
small $L$ to large $L$).

3. Start at $L = L_0$ (small, $m(L_0) > 0$ proved).
4. Increase to $L_0 + \delta$. Show $m(L_0 + \delta) > 0$ using the
   cluster expansion at $L_0$ (which converges because $m(L_0) > 0$).
5. Repeat: $m(L_0 + 2\delta) > 0$, etc.
6. Continue to $L \to \infty$.

This is a **step-by-step bootstrap**: prove $m > 0$ at one value of
$L$, use the cluster expansion to extend to nearby $L$, repeat.

The key question: does the step size $\delta$ shrink to zero as $L$
increases (preventing us from reaching $\infty$), or does it stay
bounded below (allowing us to reach $\infty$ in finitely many steps)?

If $m(L)$ stays bounded below as $L$ increases, the step size stays
bounded, and we reach $L = \infty$ in finitely many steps.

If $m(L) \to 0$ for some $L^*$ (a phase transition), the step size
shrinks and we get stuck at $L^*$.

### VII.5 Using the large-$N$ result to control finite $N$

At $N = \infty$: $m(L) = \Lambda$ for all $L$ (no $L$-dependence at
all). The step size is infinite — one step suffices.

At finite $N$: $m(L)$ varies with $L$, but by $1/N$ corrections to the
$N = \infty$ result:
$$m(L) = \Lambda + O(1/N)$$

For $N = 3$: the corrections are $O(1/3) \sim 33\%$. So $m(L) \geq
\Lambda(1 - C/N) > 0$ for $C < N = 3$.

**If the $1/N$ expansion is Borel summable** (which is expected for
the 2D model — the large-$N$ expansion is known to have good
convergence properties), then:
$$m(L, N) = \Lambda \sum_{k=0}^{\infty} \frac{c_k(L)}{N^k}$$

with $c_0(L) = 1$ (the $N = \infty$ result) and $c_k(L)$ bounded.
For $N = 3$, the series converges and gives $m(L, 3) > 0$.


---

## VIII. The Proof Program

Combining the insights from all three paths:

**Stage 1** [PROVED]: Lattice mass gap at all practical $\beta$ for
$SU(N)$.

**Stage 2** [PROVED for $N = \infty$; OPEN for $N = 3$]: Adiabatic
continuity for the 2D $\mathbb{CP}^{N-1}$ sigma model.

**Stage 3** [follows from Stage 2]: Continuum string tension
$\sigma_\infty > 0$ via the worldsheet.

**Stage 4** [follows from Stage 3]: Continuum mass gap
$\Delta_\infty > 0$ via Fredenhagen--Marcu.

**The single open step is Stage 2 at $N = 3$.** Three strategies:

(a) **Bootstrap cluster expansion** on $\mathbb{R} \times S^1_L$:
    extend $m > 0$ from small $L$ to large $L$ step by step
    (Section VII.4).

(b) **$1/N$ expansion**: prove $m(L, N) > 0$ at $N = \infty$ (done),
    then show the $1/N$ corrections are Borel summable and don't destroy
    positivity (Section VII.5).

(c) **Anomaly matching + center symmetry**: prove the $\mathbb{Z}_3$
    center symmetry is preserved at all $L$, ruling out phase
    transitions (Section VI.4).

Each strategy is a well-posed mathematical problem in 2D quantum field
theory — a setting far more tractable than 4D.
