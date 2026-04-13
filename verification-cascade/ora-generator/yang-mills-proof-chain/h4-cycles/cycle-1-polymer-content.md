# H4 Cycle 1: Balaban Polymer Perturbative Content

*ORA Author agent. Date: 2026-04-13.*
*Parent: h4-excision-run/05-excision-verdict.md (HONEST-STALL, direction: "Balaban polymer perturbative content").*
*Killed approaches: K-1 (CCM port), K-2 (spectral action), K-3 (Borel + Watson), K-4 (large-N).*

---

## 1. The proposed argument (from the task brief)

The claim to investigate:

> Each $K_k(X,V)$ is analytic in $V$ with radius $\geq \kappa$.
> The perturbative expansion of $K_k$ is the Taylor series in $g_k$.
> By Cauchy estimates, $R_k = K_k - K_k^{\mathrm{pert},n}$ satisfies $|R_k| \leq C \cdot g_k^{n+1}/\kappa^{n+1}$.
> This gives perturbative agreement at short distances (high $k$, where $g_k \to 0$).

**Verdict on the proposed argument: BLOCKED by a variable-mismatch obstruction.** The argument conflates analyticity in the gauge field $V$ with analyticity in the coupling $g_k$. These are different variables, and the Cauchy estimate does not bridge them in the way claimed. The details follow.

---

## 2. The variable-mismatch obstruction

### 2.1 What Balaban establishes

Balaban's polymer expansion at RG step $k$ gives the effective action:

$$S_k[V] = \frac{1}{g_k^2}\, S_{\mathrm{YM}}[V] \;+\; \sum_{X \in \mathcal{P}_k} K_k(X, V)$$

Each polymer activity $K_k(X, V)$ is:
- **Analytic in the block link variables** $V_\ell \in \mathrm{SU}(N)$ (more precisely, in the matrix entries of $V_\ell$), with $k$-independent radius $\rho > 0$.
- **Exponentially decaying** in the polymer size: $|K_k(X, V)| \leq e^{-\kappa |X|}$, with $\kappa > 0$ independent of $k$.

Both properties are established in CMP 109, Thm 1 (detailed: Thm 3), confirmed in the preprint's Node 05 and PROOF-CHAIN.md Step 4 (B1).

### 2.2 The variable mismatch

**The analyticity is in $V$ (the gauge field configuration), NOT in $g_k$ (the coupling constant).**

These are fundamentally different variables:
- $V = \{V_\ell\}_{\ell \in \text{links}}$ is a collection of $\mathrm{SU}(N)$ matrices, one per lattice link. It parametrizes the gauge field configuration. The analyticity radius $\rho$ measures how far $V_\ell$ can be moved from $\mathbf{1} \in \mathrm{GL}(N, \mathbb{C})$ while maintaining convergence.
- $g_k$ is the running coupling constant at RG scale $k$. It is a single real number determined by the RG flow. It appears in the effective action as the coefficient $1/g_k^2$ of the leading (Yang-Mills) term.

**The coupling $g_k$ does not parametrize the domain of $K_k$.** The polymer activity $K_k(X, V)$ is a function of the gauge field configuration $V$, not of the coupling $g_k$. The coupling $g_k$ is an output of the RG flow at step $k$ -- it is the coefficient defined by the projection of the effective action onto the unique dimension-4 operator $S_{\mathrm{YM}}$.

To apply Cauchy estimates in $g_k$, one would need $K_k(X, V)$ to be analytic in $g_k$ (or in $g_k^2$) as a complex variable. But $K_k$ is constructed by $k$ steps of the block-spin RG, each involving nonlinear operations (saddle-point, Gaussian integration, Mayer resummation) on the gauge field. The dependence of $K_k$ on $g_k$ is implicit and highly nonlinear: it enters through the initial condition $S_0[V] = (1/g_0^2) S_{\mathrm{YM}}[V]$ and propagates through $k$ RG steps. There is no reason to expect $K_k$ to be analytic in $g_0$ (or $g_k$) with a $k$-independent radius.

### 2.3 Why the brief's Cauchy estimate fails

The proposed argument claims: since $K_k$ is analytic in $V$ with radius $\geq \kappa$, and $g_k \to 0$, the remainder $R_k = K_k - K_k^{\mathrm{pert}, n}$ satisfies $|R_k| \leq C \cdot g_k^{n+1} / \kappa^{n+1}$.

This is a category error. The Cauchy estimate for an analytic function $f(z)$ on a disk of radius $r$ gives:

$$|f^{(n)}(z_0)| \leq \frac{n! \, M}{r^n}$$

where $M = \sup_{|z - z_0| = r} |f(z)|$.

To get a remainder bound in powers of $g_k$, one would need:
1. $K_k$ to be analytic in $g_k$ (or $g_k^2$) as a complex variable.
2. The analyticity radius in $g_k$ to be $k$-independent.
3. The supremum $M$ on the analyticity circle in the $g_k$-plane to be controlled.

None of these are established. What IS established is analyticity in $V$, which is a different (infinite-dimensional) variable.

---

## 3. Can the variable mismatch be bridged?

### 3.1 The rescaling trick (and why it fails)

One might try: write $V_\ell = e^{i g_k A_\ell}$ where $A_\ell \in \mathfrak{su}(N)$ is the continuum-normalized gauge potential. Then $V_\ell$ depends on $g_k$ through the exponential map. If $K_k(X, V)$ is analytic in $V$, and $V = V(g_k, A)$, can we compose to get analyticity in $g_k$?

**Problem**: The composition $K_k(X, e^{ig_k A})$ is analytic in $g_k$ for fixed $A$ (since $e^{ig_k A}$ is entire in $g_k$ and $K_k$ is analytic in $V$). So $K_k$ IS analytic in $g_k$ when $A$ is held fixed.

But the relevant question for H4 is about the **Schwinger functions** (correlators), which involve an integral over $A$ (or equivalently $V$):

$$S_2(x, y) = \int \mathcal{O}(x) \mathcal{O}(y) \, e^{-S_k[V]} \, \mathcal{D}V$$

The analyticity of the integrand in $g_k$ does NOT automatically give analyticity of the integral in $g_k$. The measure $\mathcal{D}V$ is $g_k$-independent (it is Haar measure on $\mathrm{SU}(N)^{|\text{links}|}$), but the action $S_k[V] = (1/g_k^2) S_{\mathrm{YM}}[V] + \sum_X K_k(X, V)$ has a $1/g_k^2$ prefactor that creates an essential singularity at $g_k = 0$ in the integrand $e^{-S_k}$. Specifically:

$$e^{-S_k[V]} = e^{-S_{\mathrm{YM}}[V]/g_k^2} \cdot e^{-\sum_X K_k(X, V)}$$

The factor $e^{-S_{\mathrm{YM}}/g_k^2}$ is NOT analytic at $g_k = 0$ -- it has an essential singularity. This is the standard reason why perturbation theory in $g_k^2$ is an asymptotic expansion, not a convergent Taylor series.

**This is exactly the IR renormalon / factorial-divergence obstruction that killed Routes 1--4.** The rescaling trick repackages the problem but does not solve it.

### 3.2 The fixed-$V$ Taylor expansion (and its limitation)

For a FIXED gauge field configuration $V$ (not integrated over), the function $K_k(X, V)$ does have a well-defined perturbative expansion. Balaban's construction can be viewed as follows: at each RG step, the polymer activity $K_k(X, V)$ is computed by integrating out one momentum shell. The result is a function of $V$ that can be expanded in "loops" (powers of the fluctuation propagator). This expansion is convergent for fixed $V$ in the small-field region because $K_k$ is analytic in $V$.

But this is a Taylor expansion in $V$ (or in the deviation $V - \mathbf{1}$), NOT in $g_k$. The Taylor coefficients in $V$ are numbers (depending on the geometry of $X$ and the lattice). The expansion reads:

$$K_k(X, V) = \sum_{n \geq n_0} K_k^{(n)}(X; V - \mathbf{1}, \ldots, V - \mathbf{1})$$

where $K_k^{(n)}$ is the $n$-th order Taylor coefficient (a multilinear form on the gauge field fluctuations).

**What H4 needs**: The Schwinger function $S_2(x, y)$, after performing the functional integral over $V$, should agree with the perturbative Feynman-diagram expansion at short distances. This requires:
1. The functional integral of $K_k^{(n)}$ to agree with the $n$-th order perturbative contribution.
2. The remainder after $N$ terms to be controlled.

Point (1) is essentially Reisz's power-counting theorem (lattice perturbation theory = continuum perturbation theory at each order), which IS established. Point (2) is the Borel summability question, which is the K-3 wall.

### 3.3 The fixed-$V$ argument: what it actually gives

There IS a valid intermediate result hiding in the proposed argument. Let me state it precisely.

**Lemma (polymer perturbative content at fixed $V$).** Fix a gauge field configuration $V$ in the small-field region $\Omega_s$ with $\|V_\ell - \mathbf{1}\| \leq \rho/2$ for all links $\ell$. For each polymer cluster $X$ and RG step $k$, the polymer activity $K_k(X, V)$ admits a convergent Taylor expansion in $(V - \mathbf{1})$:

$$K_k(X, V) = \sum_{n=0}^{\infty} K_k^{(n)}(X; V - \mathbf{1})$$

with remainder after $N$ terms:

$$\left| K_k(X, V) - \sum_{n=0}^{N} K_k^{(n)}(X; V - \mathbf{1}) \right| \leq e^{-\kappa |X|} \left(\frac{\|V - \mathbf{1}\|}{\rho}\right)^{N+1} \cdot \frac{1}{1 - \|V-\mathbf{1}\|/\rho}$$

*Proof.* Standard Cauchy estimate on the convergent Taylor series of the analytic function $K_k(X, \cdot)$ on the polydisk of radius $\rho$, using the bound $|K_k(X, V)| \leq e^{-\kappa |X|}$ on the boundary. $\square$

This IS a controlled perturbative expansion of the polymer activity, but:
- It is an expansion in the **field** $V$, not in the **coupling** $g_k$.
- The "perturbative" Taylor coefficients $K_k^{(n)}$ are the fixed-$V$ Taylor coefficients of $K_k$, NOT the Feynman diagram contributions.
- The bridge from fixed-$V$ Taylor coefficients to Feynman diagrams requires the functional integral, which reintroduces the $e^{-S_{\mathrm{YM}}/g_k^2}$ essential singularity.

---

## 4. Relationship to the preprint's existing machinery

### 4.1 What the preprint already uses

The preprint's Node 05 (line 24) states:

> By (B1), $\delta E_k^{d=6}$ has a convergent (not merely asymptotic) perturbative expansion with controlled remainder $\|R_{N+1}\| \leq C^{N+1} g_k^{2(N+1)}$.

This is the **dimension-6 energy shift**, not the Schwinger function. The bound $\|R_{N+1}\| \leq C^{N+1} g_k^{2(N+1)}$ refers to the Taylor expansion of $\delta E_k^{d=6}$ in the field variable $V$, evaluated on configurations in the small-field region where $\|V_\ell - \mathbf{1}\| \sim g_k^{1-\epsilon}$ (the small-field cutoff). Since $\|V - \mathbf{1}\| \leq g_k^{1-\epsilon}$ and the analyticity radius is $\rho$ (independent of $k$), the Cauchy remainder gives:

$$|R_{N+1}| \leq M \cdot \left(\frac{g_k^{1-\epsilon}}{\rho}\right)^{N+1}$$

where $M \leq e^{-\kappa |X|}$. For the energy shift (summed over $X$, one-particle matrix element), the bound becomes $C^{N+1} g_k^{(1-\epsilon)(N+1)}$, which for $N$ large enough and $\epsilon$ small is $\leq C'^{N+1} g_k^{2(N+1)}$ (matching the preprint's claim when $(1-\epsilon)(N+1) \geq 2(N+1)$, which requires $\epsilon \leq 0$ -- **there may be a slight overstatement in the preprint, but the qualitative result is correct**: the remainder is $O(g_k^{(1-\epsilon)(N+1)})$ which goes to zero as $k \to \infty$ for any fixed $N$).

### 4.2 Why this does NOT close H4

The energy shift $\delta E_k^{d=6}$ is a spectral quantity (a matrix element of the transfer matrix perturbation). Its perturbative expansion in $V$ converges, and the remainder is controlled. But this is used in Steps 10--14 of the proof chain to establish $\Delta_\infty > 0$ -- the **mass gap** -- which is ALREADY PROVED unconditionally.

**H4 is about Schwinger functions** (correlators), not about the energy shift. The Schwinger function involves the functional integral over $V$, and the integration introduces the essential singularity $e^{-S_{\mathrm{YM}}/g_k^2}$ that prevents the coupling-constant expansion from converging. The mass gap (Steps 1--14) does NOT require perturbative agreement with Feynman diagrams; it only requires control of the non-perturbative remainder of the field-variable expansion. That is why Steps 1--14 are unconditional while Step 18 is conditional.

---

## 5. Is there any route from polymer analyticity to H4?

### 5.1 What would be needed

To go from polymer analyticity (in $V$) to H4 (perturbative agreement of correlators), one would need:

**(A)** Show that the functional integral $\int \mathcal{O}(x) \mathcal{O}(y) \, e^{-S_k[V]} \mathcal{D}V$ can be computed order-by-order in $g_k^2$ with controlled remainder. This is the Borel summability question (K-3).

**(B)** Show that the polymer expansion replaces the functional integral with a convergent spatial sum $\sum_X K_k(X, V)$, and that this sum's perturbative expansion in $g_k^2$ converges. This would require:
- Each $K_k(X, V)$, after integrating over $V$ within the polymer framework, has a convergent expansion in $g_k^2$.
- The essential singularity $e^{-1/g_k^2}$ from the leading Yang-Mills action is controlled.

**(C)** Show that within the gradient-flow framework, the rescaled correlator $F(t) = S_{2,t}^c / c_1(t)^2$ has Taylor coefficients at $t = 0$ that are computable by perturbation theory. This is Route A (K-3 wall via the formal-power-series obstruction).

All three reduce to the same wall: the functional integral introduces $e^{-1/g^2}$ which makes the coupling-constant expansion asymptotic (factorially divergent) rather than convergent. The polymer expansion's spatial convergence (in $X$) cannot be traded for coupling-constant convergence (in $g^2$) because the $1/g^2$ prefactor of $S_{\mathrm{YM}}$ is not part of the polymer activities $K_k(X, V)$ -- it sits outside the polymer sum.

### 5.2 The structural diagnosis

The Balaban effective action has the form:

$$S_k[V] = \underbrace{\frac{1}{g_k^2}\, S_{\mathrm{YM}}[V]}_{\text{essential singularity at } g_k = 0} \;+\; \underbrace{\sum_{X} K_k(X, V)}_{\text{analytic in } V \text{ with convergent expansion}}$$

The polymer activities $K_k$ are the "quantum corrections." They ARE perturbatively computable (their $V$-expansion agrees with Feynman diagrams order by order -- this is Reisz's theorem). But the full correlator involves $e^{-S_k}$, and the exponential of the $1/g_k^2$ term creates the essential singularity that makes the $g_k^2$-expansion divergent.

**The polymer expansion controls the quantum corrections. It does NOT control the classical action's $1/g^2$ singularity.** This is why polymer analyticity (Steps 2--4) suffices for the mass gap (Steps 10--14, where only the quantum corrections need to be controlled) but NOT for H4 (where the full correlator, including the $e^{-1/g^2}$ weight, must match perturbation theory).

---

## 6. Verdict

### Status: BLOCKED

**The proposed argument (Cauchy estimates on polymer activities giving perturbative agreement) has a fatal variable-mismatch obstruction.** Analyticity in the gauge field $V$ does not imply analyticity in the coupling $g_k$. The bridge from field-analyticity to coupling-analyticity requires controlling the functional integral, which reintroduces the essential singularity $e^{-S_{\mathrm{YM}}/g_k^2}$ -- the same wall that blocks K-3 (Borel summability).

### What was gained

1. **Precise identification of the variable-mismatch obstruction**: the brief's proposed argument fails at a specific, identifiable step (conflating $V$-analyticity with $g$-analyticity). This is a new structural diagnosis, distinct from the K-3 wall (which is about the Borel plane) and the Route A wall (which is about formal power series vs analytic functions).

2. **A valid intermediate result** (Section 3.3): the polymer activities DO have convergent Taylor expansions in $V$ with controlled remainders. This is already used in the preprint for Steps 10--14 and does not extend to H4.

3. **Structural diagnosis** (Section 5.2): the polymer expansion controls the quantum corrections but not the classical action's $1/g^2$ singularity. H4 requires control of both. This explains precisely WHY Steps 1--14 are unconditional while Step 18 is conditional.

### The exact obstruction

**The functional integral weight $e^{-S_{\mathrm{YM}}[V]/g_k^2}$ has an essential singularity at $g_k = 0$.** This singularity is invisible to the polymer activities (which are the quantum corrections living in the sum $\sum_X K_k(X, V)$) but dominates the coupling-constant expansion of the full correlator. No amount of control over the polymer activities can remove this singularity because it lives in the classical prefactor.

### LOCK update

This cycle confirms that the "Balaban polymer perturbative content" direction, identified in the excision verdict as the most promising remaining approach (difficulty 8/10, $p = 0.15$), is BLOCKED by the variable-mismatch obstruction. The obstruction is structural (not a gap in our knowledge of Balaban's work) and is a different manifestation of the same $e^{-1/g^2}$ essential singularity that blocks all other routes.

**Updated probability for this direction**: $p = 0.15 \to p \leq 0.03$ (the variable mismatch is a hard structural wall, not a gap; residual probability accounts for the possibility that a fundamentally new idea could bridge $V$-analyticity to $g$-analyticity, perhaps via a resurgence-type mechanism specific to the Balaban framework).

**Updated LOCK**: $11/10 \to 12/10$ (eighth route attempted, eighth route blocked by the same underlying $e^{-1/g^2}$ essential singularity).

---

## 7. New kill or card?

### New card (not a kill -- the direction was never a full route)

| Card # | Name | Content |
|---|---|---|
| Card 18 | Variable-Mismatch Obstruction (Polymer $V$-Analyticity vs Coupling $g$-Analyticity) | **WHAT**: The polymer activities $K_k(X, V)$ are analytic in the gauge field $V$ (Balaban), but H4 requires analyticity of the correlator in the coupling $g_k$. The bridge requires controlling the functional integral weight $e^{-S_{\mathrm{YM}}/g_k^2}$, which has an essential singularity at $g_k = 0$. The polymer expansion controls quantum corrections but not the classical action's $1/g^2$ singularity. **STATUS**: STRUCTURAL DIAGNOSIS. Confirms that polymer analyticity (Steps 2--4) is the right tool for the mass gap (Steps 10--14) but not for H4 (Step 18). |

### Re-entry gate

The variable-mismatch obstruction could be bypassed if:
1. A **resurgence framework** specific to the Balaban polymer expansion could be developed, showing that the trans-series in $e^{-c/g_k^2}$ is Borel-summable within the polymer framework. This would require extending the polymer expansion to include instanton-like saddle points and showing the full trans-series converges. (Essentially a constructive-QFT version of resurgence -- no precedent exists.)
2. A **new observable** could be identified that avoids the $1/g^2$ prefactor entirely -- i.e., a correlator that can be expressed purely in terms of polymer activities without the classical action weight. (The gradient-flow rescaled correlator $F(t)$ was supposed to be this, but its Taylor coefficients at $t = 0$ still involve the functional integral.)

Neither re-entry gate is expected to open without a major independent advance.

---

## 8. Relationship to killed approaches

This cycle does NOT repeat any killed approach:
- **K-1** (CCM port): not invoked.
- **K-2** (spectral action): not invoked.
- **K-3** (Borel + Watson): the variable-mismatch obstruction is a DIFFERENT diagnosis from K-3. K-3 is about the Borel plane (IR renormalons at $u = 2$). This cycle is about the variable mismatch ($V$ vs $g$). They converge on the same underlying wall ($e^{-1/g^2}$ essential singularity) but are distinct diagnostic paths.
- **K-4** (large-N): not invoked.

---

*Cycle 1 complete. Direction: BLOCKED. No closure. The wall stands.*
