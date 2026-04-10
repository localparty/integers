# The Gradient-Flow Route to Full Clay Compliance

## 1. Executive Summary

Conjectures L.1--L.4 of the Yang--Mills mass gap preprint state the four Jaffe--Witten structural requirements beyond the mass gap itself: renormalized composite operators 

(L.1), asymptotic-freedom short-distance matching 

(L.2), the stress-energy tensor 

(L.3), and the operator product expansion 

(L.4). All four reduce to a single bottleneck: the non-perturbative construction of 
renormalized gauge-invariant composite operators on the GNS Hilbert space (L.1). 

The Yang--Mills gradient flow, introduced by Luscher (2010) and proved UV-finite to all orders in perturbation theory by Luscher--Weisz (2011), provides the cleanest available route to closing L.1. The key insight is that composite operators built from the flowed gauge field $B_\mu(t,x)$ at flow time $t > 0$ are automatically UV-finite without additional renormalization; the renormalized local operator $[\mathrm{Tr}\,F^2]_R(x)$ can then be extracted via the small-flow-time expansion as $t \to 0^+$, with Wilson coefficients computable perturbatively (Suzuki 2013, Harlander--Neumann et al. 2016--2022). The new mathematics required is to embed the gradient flow into Balaban's polymer expansion framework and prove non-perturbative UV finiteness and convergence of the small-flow-time limit. Once L.1 is in hand, L.2 follows from the small-flow-time expansion's automatic AF matching, L.3 follows from Suzuki's gradient-flow stress tensor formula, and L.4 follows at leading order. Estimated effort: 9--12 months of focused research for L.1, plus 3--6 months for L.2--L.4 assembly.


---


## 2. What the Gradient Flow Is

### 2.1 The flow equation

The Yang--Mills gradient flow is the following parabolic PDE on gauge fields. In the **continuum**, define $B_\mu(t,x)$ for flow time $t \geq 0$ and spacetime point $x \in \mathbb{R}^4$ by

$$\partial_t B_\mu(t,x) = D_\nu G_{\nu\mu}(t,x), \qquad B_\mu(0,x) = A_\mu(x), \tag{2.1}$$

where $G_{\mu\nu}(t,x) = \partial_\mu B_\nu - \partial_\nu B_\mu + [B_\mu, B_\nu]$ is the field-strength tensor of the flowed field and $D_\nu G_{\nu\mu} = \partial_\nu G_{\nu\mu} + [B_\nu, G_{\nu\mu}]$ is the gauge-covariant Laplacian acting on the connection. Equation (2.1) is the gradient of the Yang--Mills action functional $S_{\mathrm{YM}}[B] = -\frac{1}{2}\int \mathrm{Tr}(G_{\mu\nu}G^{\mu\nu})\,d^4x$ with respect to the $L^2$ metric on the space of connections. The flow drives the field toward a local minimum of the action --- a classical Yang--Mills connection --- smoothing out UV fluctuations at scale $\sqrt{8t}$.

On the **lattice**, the flow acts on link variables $V_t(\ell) \in \mathrm{SU}(N)$ via

$$\partial_t V_t(\ell) = -g_0^2\,\bigl(\partial_{V,\ell} S_W[V_t]\bigr)\,V_t(\ell), \qquad V_0(\ell) = U(\ell), \tag{2.2}$$

where $S_W$ is the Wilson plaquette action and $\partial_{V,\ell}$ denotes the Lie-algebra-valued derivative with respect to the link $V_t(\ell)$. Equation (2.2) is the lattice analogue of the steepest-descent flow on the gauge-field configuration space; it has the same smoothing properties as (2.1) and converges to it in the continuum limit. Well-posedness of (2.2) on the compact group manifold $\mathrm{SU}(N)^{|\text{links}|}$ is immediate from the Picard--Lindelof theorem on compact manifolds: the right-hand side is a smooth vector field on a compact Lie group, so global existence and uniqueness hold for all $t \geq 0$.

**Gauge covariance.** Both the continuum and lattice flow equations are gauge-covariant: if $B_\mu(t,x)$ solves (2.1) with initial data $A_\mu$, then $B_\mu^g(t,x) := g(x) B_\mu(t,x) g(x)^{-1} + g(x) \partial_\mu g(x)^{-1}$ solves (2.1) with initial data $A_\mu^g$. Consequently, gauge-invariant observables at flow time $t > 0$ are well-defined without gauge fixing.


### 2.2 Key property: UV finiteness at $t > 0$

The central result of Luscher and Weisz (arXiv:1101.0963, JHEP 02 (2011) 051) is:

> **Theorem (Luscher--Weisz 2011, perturbative).** *Let $\mathcal{O}_1(t_1, x_1), \ldots, \mathcal{O}_n(t_n, x_n)$ be local gauge-invariant composite operators built from the flowed field $B_\mu(t,x)$ and its derivatives, evaluated at positive flow times $t_1, \ldots, t_n > 0$. Then the correlation function $\langle \mathcal{O}_1(t_1, x_1) \cdots \mathcal{O}_n(t_n, x_n) \rangle$ is UV-finite to all orders of perturbation theory, once the parameters of the underlying 4D gauge theory (coupling $g$, masses, gauge-fixing) are renormalized in the standard way. No additional operator renormalization is needed.*

The proof strategy treats the flow as defining a $(4+1)$-dimensional field theory on $\mathbb{R}^4 \times [0,\infty)$, where the flow-time direction introduces Feynman rules with a flow propagator $K(t,p) = e^{-tp^2}$ (the heat kernel). This exponential damping factor suppresses UV modes with $|p| \gg 1/\sqrt{t}$, providing an effective UV cutoff at momentum scale $\sim 1/\sqrt{t}$. The key technical step is a power-counting argument: every loop integral involving at least one flow propagator converges by an additional power of $e^{-tp^2}$ relative to the unflowed case. The only divergences come from the underlying 4D theory (loops entirely at $t = 0$), which are absorbed by the standard renormalization.

**What this means for composite operators:** The operator $E(t,x) := \frac{1}{4} G_{\mu\nu}^a(t,x) G_{\mu\nu}^a(t,x)$ at $t > 0$ is UV-finite without any $Z$-factor. Its expectation value $\langle E(t,x) \rangle$ is a finite, scheme-independent physical quantity at each $t > 0$. This is the "magic property" that makes the gradient flow useful for constructing renormalized composites: the UV divergences that plague local operators at $t = 0$ are smoothed out by the flow.

**Perturbative vs. non-perturbative.** The Luscher--Weisz result is proved to all orders of perturbation theory. It is **not** a non-perturbative theorem. Proving UV finiteness non-perturbatively --- showing that the flowed correlators have a well-defined continuum limit at fixed $t > 0$ without additional renormalization, at the level of the full lattice path integral --- is one of the key new results required by the present programme (see Section 3.4).


### 2.3 The small-flow-time expansion

As $t \to 0^+$, flowed composite operators can be expanded in terms of renormalized local operators at $t = 0$ with $t$-dependent Wilson coefficients. For the gauge-field energy density:

$$\langle E(t,x) \rangle = \frac{3(N^2 - 1)}{128\pi^2 t^2}\left[1 + \bar{c}_1\,\bar{g}^2(\mu) + \bar{c}_2\,\bar{g}^4(\mu) + O(\bar{g}^6)\right], \tag{2.3}$$

where $\bar{g}(\mu)$ is the $\overline{\mathrm{MS}}$ coupling at scale $\mu = (8t)^{-1/2}$. The leading $t^{-2}$ behavior reflects the engineering dimension of $E$ (dimension 4, hence $\langle E \rangle \sim t^{-d/2} = t^{-2}$ in $d = 4$). The one-loop coefficient was computed by Luscher (2010); two- and three-loop coefficients by Harlander, Neumann, and collaborators (arXiv:1606.03756, JHEP 06 (2016) 161; arXiv:2111.14376).

More generally, the small-flow-time expansion of a flowed composite operator $\tilde{\mathcal{O}}(t,x)$ takes the form

$$\tilde{\mathcal{O}}(t,x) = \sum_k c_k(t,\mu)\,[\mathcal{O}_k]_R(x) + O(t), \tag{2.4}$$

where $\{[\mathcal{O}_k]_R\}$ are the renormalized local operators at $t = 0$ of dimension $\leq \dim(\tilde{\mathcal{O}})$, ordered by scaling dimension, and $c_k(t,\mu)$ are Wilson coefficients with known perturbative expansions. The expansion (2.4) is the bridge between the UV-finite flowed world ($t > 0$) and the renormalized local operators ($t = 0$) that Jaffe--Witten demands.

Inverting (2.4) gives the prescription for extracting the renormalized operator:

$$[\mathrm{Tr}\,F^2]_R(x) = \lim_{t \to 0^+} \frac{\tilde{\mathcal{O}}(t,x) - \langle \tilde{\mathcal{O}}(t) \rangle \cdot \mathbb{1}}{c_1(t,\mu)}, \tag{2.5}$$

where $c_1(t,\mu) \sim t^{-2} \cdot (\text{AF logs})$ absorbs the divergent vacuum piece. This is the gradient-flow analogue of multiplicative renormalization, with the flow time $t$ playing the role of the UV regulator and $c_1(t)$ playing the role of $Z_\mathcal{O}(a)$.


---


## 3. How the Gradient Flow Closes L.1 (Renormalized Composite Operators)

### 3.1 The construction

Define the flowed gauge-field energy density at flow time $t > 0$:

$$\mathcal{O}_t(x) := \frac{1}{4}\,G_{\mu\nu}^a(t,x)\,G_{\mu\nu}^a(t,x) = E(t,x). \tag{3.1}$$

This operator has the following properties, each essential for closing L.1:

1. **Gauge invariance.** The flow (2.1) preserves gauge covariance, so $\mathcal{O}_t(x)$ is gauge-invariant for each $t > 0$. No gauge fixing or BRST cohomology is needed.

2. **UV finiteness (perturbative).** By the Luscher--Weisz theorem (Section 2.2), all correlators $\langle \mathcal{O}_t(x_1) \cdots \mathcal{O}_t(x_n) \rangle$ at $t > 0$ are UV-finite to all orders in perturbation theory.

3. **Spacetime locality.** Although the flow smears the gauge field over a ball of radius $\sim \sqrt{8t}$ in field space, the operator $\mathcal{O}_t(x)$ is still a local functional of $B_\mu(t, \cdot)$ evaluated at the single spacetime point $x$. In the GNS Hilbert space, $\mathcal{O}_t(x)$ is an element of the local algebra associated with the ball $B(x, \sqrt{8t})$.

4. **Boundedness.** On the lattice, $\mathcal{O}_t(x)$ is a bounded function of the (compact) link variables. On a finite lattice, it defines a bounded operator on $\mathcal{H}$ via the GNS reconstruction.

5. **OS positivity.** Since $\mathcal{O}_t(x)$ is a positive-definite real function of the gauge field (it is a sum of squares), the flowed Schwinger functions inherit OS positivity from the lattice measure.

**The gradient flow thus provides a one-parameter family of bona fide operators on $\mathcal{H}$, indexed by $t > 0$, that are UV-finite, gauge-invariant, and local.** The remaining task is to take the $t \to 0^+$ limit to recover a local operator at $t = 0$ in the Jaffe--Witten sense.


### 3.2 The continuum limit at fixed $t > 0$

At fixed flow time $t > 0$, take the lattice spacing $a \to 0$. The claim: the lattice flowed correlator

$$S_{n,t}^{(a)}(x_1, \ldots, x_n) := \langle \mathcal{O}_t^{(a)}(x_1) \cdots \mathcal{O}_t^{(a)}(x_n) \rangle_a \tag{3.2}$$

converges as $a \to 0$ to a well-defined continuum distribution $S_{n,t}(x_1, \ldots, x_n)$ for all non-coincident spacetime points. The convergence is controlled by three ingredients:

**(a) UV regulation by the flow.** At $t > 0$, the flow provides an effective UV cutoff at momentum scale $\Lambda_t \sim 1/\sqrt{t}$. This means the lattice-to-continuum limit involves modes with $|p| \lesssim \Lambda_t$ only; modes at $|p| \sim 1/a \gg \Lambda_t$ are exponentially suppressed by the heat kernel $e^{-tp^2}$. Concretely, in momentum space the flow propagator contributes a factor $e^{-tp^2}$ to each internal line connected to flow time $t$, guaranteeing exponential convergence of the lattice sum to its continuum integral.

**(b) IR regulation by the mass gap.** The preprint's existing result $\Delta_\infty > 0$ controls IR divergences: the connected correlator $S_{n,t}^c$ decays as $e^{-\Delta_\infty\,\mathrm{diam}(\{x_i\})}$ at large separations. This is inherited from the unflowed Schwinger functions and is independent of $t$.

**(c) Lattice-to-continuum convergence of the flow equation.** The lattice flow (2.2) converges to the continuum flow (2.1) as $a \to 0$ at fixed $t > 0$, with discretization errors $O(a^2)$. This was established perturbatively by Makino--Suzuki (arXiv:1403.4772, PTEP 2014:063B02) and follows from the smoothness of the continuum flow solution at $t > 0$ combined with standard lattice PDE convergence theory. Non-perturbatively on the lattice, the flow is a well-defined deterministic ODE on a compact manifold (Section 2.1), so the convergence question reduces to showing that the lattice path-integral average of the flowed observable converges --- which is a statement about the lattice measure, not the flow itself.

**What needs to be proved (new mathematics).** Show that the lattice-to-continuum limit of $S_{n,t}^{(a)}$ at fixed $t > 0$ exists, using the existing Balaban--RG machinery augmented by the flow's UV smoothing. The key estimate: for Schwartz test functions $f_1, \ldots, f_n$,

$$\bigl| S_{n,t}^{(a_1)}(f_1, \ldots, f_n) - S_{n,t}^{(a_2)}(f_1, \ldots, f_n) \bigr| \leq C(t,n)\,|a_1^2 - a_2^2|^\alpha \tag{3.3}$$

for some $\alpha > 0$ and $C(t,n) < \infty$ depending on $t$ but not on $a_1, a_2$. The flow's exponential UV smoothing $e^{-tp^2}$ should make this estimate **easier** to prove than the analogous estimate for unflowed Schwinger functions (which the preprint establishes via the RG telescoping sum of Section 5.4).


### 3.3 The $t \to 0^+$ limit and the local operator

The small-flow-time expansion (2.4)--(2.5) connects flowed operators to renormalized local operators. For the two-point function:

$$S_{2,t}(x,y) = \langle \mathcal{O}_t(x)\,\mathcal{O}_t(y) \rangle = c_0(t)^2\,\langle \mathbb{1} \rangle + 2\,c_0(t)\,c_1(t)\,\langle [\mathrm{Tr}\,F^2]_R(y) \rangle + c_1(t)^2\,\langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y) \rangle + \cdots \tag{3.4}$$

where $c_0(t) \sim t^{-2}$ (vacuum coefficient) and $c_1(t) \sim t^{-2} (\log(1/t\Lambda^2))^{-1}$ (coefficient of $[\mathrm{Tr}\,F^2]_R$). The connected correlator at leading order gives:

$$S_{2,t}^c(x,y) \approx c_1(t)^2\,\langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y) \rangle_c + (\text{higher-dim. operators}). \tag{3.5}$$

Inverting:

$$\langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y) \rangle_c = \lim_{t \to 0^+} \frac{S_{2,t}^c(x,y)}{c_1(t)^2}. \tag{3.6}$$

**This defines the renormalized two-point function without explicit $Z_\mathcal{O}(a)$.** The gradient flow does the renormalization automatically: the UV-divergent pieces are packaged into the perturbatively computable coefficients $c_k(t)$, and the limit extracts the finite renormalized correlator.

**For the operator itself**, the GNS reconstruction applied to the family of renormalized Schwinger functions $\{S_n^{\mathrm{ren}}\}$ yields $[\mathrm{Tr}\,F^2]_R(f)$ as an operator-valued distribution on $\mathcal{H}$. OS positivity is preserved because $c_1(t) > 0$ and the flowed Schwinger functions are OS-positive.


### 3.4 What needs to be proved (the new mathematics)

The gradient-flow route requires three genuinely new estimates, organized by increasing difficulty:

**Estimate 1 (Flowed polymer activities).** Define the gradient flow on the gauge field configurations appearing in Balaban's polymer expansion at each RG scale $k$. Show that the flow preserves the polymer expansion structure: the flowed polymer activities $K_k^{(t)}(X,V)$ satisfy

$$|K_k^{(t)}(X,V)| \leq e^{-\kappa(t)\,|X|} \tag{3.7}$$

with $\kappa(t) \geq \kappa_B > 0$ for all $t > 0$ and all $k$, where $\kappa_B$ is Balaban's polymer decay constant. The flow-time dependence of $\kappa(t)$ should be controlled: $\kappa(t) \to \kappa_B$ as $t \to 0$ and $\kappa(t) \geq \kappa_B$ for all $t > 0$ (the flow improves, not degrades, the polymer expansion convergence). This leverages the fact that the gradient flow is a contraction on the space of gauge-field configurations with respect to the Yang--Mills energy norm.

**Estimate 2 (Non-perturbative UV finiteness at fixed $t > 0$).** Prove that the continuum limit of the flowed correlator $S_{n,t}^{(a)}$ exists as $a \to 0$ at fixed $t > 0$, using the flowed polymer expansion of Estimate 1. The key new input relative to the existing unflowed continuum limit is the flow propagator's exponential suppression $e^{-tp^2}$, which provides an additional UV regulator beyond Balaban's small-field/large-field decomposition. Concretely, in the Balaban RG framework, the fluctuation integral at scale $k$ involves the propagator $G_k = (-D^2 + m_W^2)^{-1}$; with the flow, this is replaced by $G_k^{(t)} = e^{-t(-D^2)} G_k$, which has strictly better UV behavior:

$$|G_k^{(t)}(x,y)| \leq C(t)\,e^{-(\delta_0 + t/a_k^2)|x-y|} \tag{3.8}$$

for some $C(t) < \infty$. The extra $t/a_k^2$ in the exponent is the flow's contribution to the exponential decay.

**Estimate 3 (The $t \to 0^+$ limit).** Prove that the rescaled connected correlator $S_{2,t}^c(x,y)/c_1(t)^2$ converges as $t \to 0^+$ to a finite tempered distribution $S_2^{\mathrm{ren}}(x,y)$. This is the hardest step. The difficulty: as $t \to 0$, the flow's UV smoothing disappears, and one must show that the perturbative small-flow-time expansion (2.4) accurately captures the leading singularity structure of the non-perturbative correlator. What is needed:

- Control of operator mixing: the small-flow-time expansion involves a sum over local operators of increasing dimension, and the sum must converge (or at least be asymptotic with controlled remainder) non-perturbatively.
- Analyticity of the flowed effective action in $t$ near $t = 0$: this would follow from Balaban's analyticity (B1) combined with the analyticity of the heat kernel $e^{-tp^2}$ in $t$.
- The dimension-6 classification of Section 5.6 of the preprint forces all higher-dimension operators to have $\mathrm{dev} \geq 2$, providing non-perturbative suppression of the subleading terms in the small-flow-time expansion by factors of $g_k^4 \hat{\Delta}^2$ via the spectral lemma.


### 3.5 What is already in the literature

| Result | Status | Reference |
|:-------|:-------|:----------|
| Continuum flow equation well-posedness (smooth manifolds) | Rigorous: short-time existence in 4D | Struwe, Calc. Var. PDE 2 (1994) 123; Rade, J. Reine Angew. Math. 431 (1992) 123 (2D, 3D) |
| Lattice flow equation well-posedness | Rigorous (trivial: ODE on compact manifold) | Luscher, JHEP 08 (2010) 071 |
| Global existence on lattice | Rigorous (compact $\mathrm{SU}(N)$) | Luscher 2010; Chatterjee, arXiv:1803.01950 |
| UV finiteness at $t > 0$ (perturbative, all orders) | Proved | Luscher--Weisz, JHEP 02 (2011) 051 |
| UV finiteness at $t > 0$ (non-perturbative) | **Open** | --- |
| Small-flow-time expansion (one loop) | Known | Luscher, JHEP 08 (2010) 071 |
| Small-flow-time expansion (two loops) | Known | Harlander--Neumann, JHEP 06 (2016) 161 |
| Small-flow-time expansion (three loops) | Known | Artz et al., JHEP 06 (2019) 121; Harlander et al., arXiv:2111.14376 |
| $T_{\mu\nu}$ via gradient flow (perturbative) | Complete | Suzuki, PTEP 2013:083B03 |
| $T_{\mu\nu}$ via gradient flow (lattice, perturbative) | Complete | Makino--Suzuki, PTEP 2014:063B02 |
| $T_{\mu\nu}$ Ward identities via gradient flow | Complete | Del Debbio--Patella--Rago, JHEP 11 (2013) 212 |
| Global existence + convergence near minimizers (4D, smooth) | Rigorous | Feehan, arXiv:1409.1525 (Lojasiewicz--Simon) |
| Gradient flow in Balaban's framework | **NEW (this programme)** | --- |
| $K$-uniform flowed polymer activities | **NEW (this programme)** | --- |
| Non-perturbative $t \to 0^+$ limit | **NEW (this programme)** | --- |


---


## 4. How L.2--L.4 Follow from L.1

### 4.1 L.2 (AF short-distance match)

The small-flow-time expansion directly encodes the asymptotic-freedom prediction. At one loop, the expansion of $\langle E(t,x) \rangle$ gives (Luscher 2010):

$$\langle E(t,x) \rangle = \frac{3(N^2-1)}{128\pi^2 t^2}\left[1 + \bar{c}_1\,\bar{g}^2(q) + O(\bar{g}^4)\right], \qquad q = (8t)^{-1/2}, \tag{4.1}$$

where $\bar{g}(q)$ is the $\overline{\mathrm{MS}}$ running coupling at scale $q$, and $\bar{c}_1 = (11N/3)(2\gamma_E + \ln 3)/(4\pi)^2 + \cdots$ is a known numerical constant. This defines a non-perturbative running coupling $\bar{g}_{\mathrm{GF}}^2(q)$ via the gradient flow, which agrees with the AF $\beta$-function to the computed order.

For the two-point function, the renormalized correlator extracted via (3.6) automatically inherits the AF prediction:

$$\langle [\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y) \rangle \sim \frac{C_N}{|x-y|^8}\left(\ln\frac{1}{|x-y|\Lambda}\right)^{-2}\bigl[1 + O((\log)^{-1})\bigr] \tag{4.2}$$

as $|x - y| \to 0$, with $C_N = 2(N^2-1)/\pi^6$. The $|x-y|^{-8}$ power comes from the engineering dimension of $\mathrm{Tr}\,F^2$ (dimension 4); the $(\log)^{-2}$ factor comes from the running of $\alpha_s(1/|x-y|)$ and the trace-anomaly identity $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$, which gives the two powers of $g^{-2}$ in the Wilson coefficient $c_1(t)$.

**The AF matching is thus automatic once the flowed operator exists.** No separate argument is needed beyond the perturbative small-flow-time expansion and the Reisz power-counting theorem relating lattice and continuum perturbation theory (CMP 116 (1988) 81). The residual gap is the standard "non-perturbative = perturbative at short distances" hypothesis (Hypothesis H4 of G4b), which is ubiquitous in lattice QCD but not rigorously proved. However, within the gradient-flow framework, this hypothesis gains additional support: the flow provides a smooth interpolation between the non-perturbative theory (at large $t$) and the perturbative regime (at small $t$), with the interpolation controlled by the heat-kernel smoothing.


### 4.2 L.3 (Stress tensor)

Suzuki (arXiv:1304.0533, PTEP 2013:083B03) gave the definitive gradient-flow construction of the renormalized stress-energy tensor. Define flowed operators:

$$U_{\mu\nu}(t,x) := G_{\mu\rho}^a(t,x)\,G_{\nu\rho}^a(t,x) - \frac{1}{4}\delta_{\mu\nu}\,G_{\rho\sigma}^a(t,x)\,G_{\rho\sigma}^a(t,x), \tag{4.3}$$
$$E(t,x) := \frac{1}{4}\,G_{\rho\sigma}^a(t,x)\,G_{\rho\sigma}^a(t,x). \tag{4.4}$$

Then the renormalized energy-momentum tensor is:

$$T_{\mu\nu}^R(x) = \lim_{t \to 0^+}\Bigl[\,c_1(t)\,U_{\mu\nu}(t,x) + c_2(t)\,\delta_{\mu\nu}\,E(t,x) + c_3(t)\,\delta_{\mu\nu}\,\langle E(t,x) \rangle \cdot \mathbb{1}\,\Bigr], \tag{4.5}$$

where the coefficients $c_i(t)$ are perturbatively computable Wilson coefficients. At leading order (Suzuki 2013):

- $c_1(t) = 1 + O(\bar{g}^2)$: the traceless-symmetric piece needs only multiplicative matching.
- $c_2(t) = O(\bar{g}^2)$: the trace piece (trace anomaly) enters at one loop.
- $c_3(t)$: the vacuum subtraction constant, fixed by $\langle \Omega | T_{\mu\nu} | \Omega \rangle = 0$.

At the non-perturbative level, the coefficients $C_1 = 1$, $C_2 = -1/4$, $C_3 = 1/4$, $C_4 = 0$ are the tree-level matching constants relating the four dimension-4 operators to the two irreducible representations under the hypercubic group $H(4)$ (Harlander et al., arXiv:2111.14376).

**Key properties of the gradient-flow stress tensor:**

1. **Conservation $\partial^\mu T_{\mu\nu} = 0$.** Follows from translation invariance of the gradient-flow measure combined with the Ward identity derived by Del Debbio--Patella--Rago (arXiv:1306.1173, JHEP 11 (2013) 212). The gradient-flow formulation makes this particularly clean: the Ward identity is a consequence of the infinitesimal translation invariance of the flow equation itself.

2. **Trace anomaly $T_\mu^\mu = (\beta(g)/(2g))[\mathrm{Tr}\,F^2]_R$.** Follows from the small-flow-time expansion of $c_2(t)\,E(t,x)$, which produces the correct trace-anomaly coefficient via the Collins--Duncan--Joglekar mechanism (Phys. Rev. D 16 (1977) 438) and the Spiridonov--Chetyrkin identity.

3. **Positivity $H_{\mathrm{OS}} \geq 0$.** Already established unconditionally from OS reconstruction (preprint Section 5.6), independent of any composite-operator conjecture.

4. **Identification $H_{\mathrm{OS}} = \int T_{00}\,d^3\vec{x}$.** Conditional on L.1; follows from the standard transfer-matrix argument once $T_{00}$ exists as an operator-valued distribution.

**Closability estimate:** Given L.1, L.3 is the easiest of the four conjectures. The Suzuki formula (4.5) provides an explicit, UV-automatically-finite construction. The only non-trivial residual beyond L.1 is promoting the perturbative Ward identity to an exact distributional identity on $\mathcal{H}$, which is of strictly less difficulty than L.1 itself. Estimated additional effort: 2--3 months.


### 4.3 L.4 (OPE)

At flow time $t > 0$, the product $\mathcal{O}_t(x)\,\mathcal{O}_t(y)$ is a well-defined UV-finite operator for all $x, y$ (including $x = y$), because both factors are smeared by the flow. The gradient-flow OPE is therefore:

$$\mathcal{O}_t(x)\,\mathcal{O}_t(y) = \sum_k D_k^{(t)}(x-y)\,\mathcal{O}_{k,t}\!\Bigl(\frac{x+y}{2}\Bigr), \tag{4.6}$$

where the coefficient functions $D_k^{(t)}(x-y)$ are smooth (not distributional!) for $t > 0$. Taking $t \to 0^+$ recovers the continuum OPE with distributional coefficients:

$$[\mathrm{Tr}\,F^2]_R(x)\,[\mathrm{Tr}\,F^2]_R(y) \sim C^{\mathbb{1}}(x-y)\,\mathbb{1} + C^{\mathcal{O}}(x-y)\,[\mathrm{Tr}\,F^2]_R(y) + \sum_{k \geq 6} C^k(x-y)\,\mathcal{O}_k(y). \tag{4.7}$$

The leading identity-channel coefficient is precisely the renormalized two-point function:

$$C^{\mathbb{1}}(x-y) = \frac{C_N}{|x-y|^8}\left(\ln\frac{1}{|x-y|\Lambda}\right)^{-2}\bigl[1 + O((\log)^{-1})\bigr], \tag{4.8}$$

which is the AF-predicted form of (4.2). Subleading channels involve $[\mathrm{Tr}\,F^2]_R$ (power $|x-y|^{-4}$, related to the gluon condensate in SVZ phenomenology) and dimension-6 operators ($|x-y|^{-2}$ and regular). The perturbative coefficients are known to three loops from Zoller--Chetyrkin (JHEP 12 (2012) 119; JHEP 10 (2014) 169).

**What the gradient flow provides for L.4:** The flow gives a natural regularization of the OPE: at $t > 0$, the operator product is well-defined, and the OPE coefficients $D_k^{(t)}$ are smooth functions computable by Wick contractions of the flowed fields. The $t \to 0$ limit of $D_k^{(t)}$ yields the continuum OPE coefficients $C^k$. This provides a constructive route to the OPE that avoids the abstract existence arguments of Bostelmann (phase-space nuclearity) or Hollands--Wald (perturbative curved-spacetime OPE).

**Residual difficulty.** The full non-perturbative OPE (all channels, all orders) remains the hardest of the four conjectures even with the gradient-flow approach. The leading-order statement (4.8) is accessible once L.1 and L.2 are in hand; the full channel decomposition including dimension-$\geq 6$ mixing matrices is a separate research programme. The honest deliverable for a Clay submission is the leading-order OPE conjecture (4.7)--(4.8), with the full OPE stated as an open problem.


---


## 5. Step-by-Step Research Plan

### 5.1 Phase 1: Lattice gradient flow within Balaban's framework (months 1--3)

**Goal:** Define the lattice gradient flow on Balaban's effective action at each RG scale and prove it preserves the polymer expansion structure.

**Concrete mathematical tasks:**

1. **Flow on background + fluctuation decomposition.** At Balaban's $k$-th RG step, the gauge field decomposes as $U = V \cdot e^{ia_k A}$ where $V$ is the background (block-spin) field and $A$ is the fluctuation. Define the gradient flow on $A$ at fixed $V$:
$$\partial_t A_\mu^{(k)} = -\frac{\delta S_k^{\mathrm{eff}}[V, A^{(k)}]}{\delta A_\mu^{(k)}}, \qquad A_\mu^{(k)}(0) = A_\mu. \tag{5.1}$$
Show this is well-posed on Balaban's small-field domain $\Omega_s$ (where $\|A\| < \varepsilon_k$) and that the flow maps $\Omega_s$ into itself.

2. **Flowed polymer activities.** For each polymer $X$ in Balaban's expansion, define the flowed activity $K_k^{(t)}(X,V)$ by evaluating the flow at time $t$. Prove the exponential decay estimate (3.7): $|K_k^{(t)}(X,V)| \leq e^{-\kappa(t)|X|}$ with $\kappa(t) \geq \kappa_B$. The key input is that the flow is a contraction (the Yang--Mills energy is non-increasing along the flow), combined with the existing polymer convergence estimates of Balaban CMP 109.

3. **$K$-uniformity of flowed constants.** Prove that the flow-time-dependent constants in (3.7) are $K$-uniform (independent of the bare theory index $K$), using the same mechanism as the existing $K$-uniformity proof (Appendix M of the preprint): the physical constants $\kappa_B$, $m_W$, $C_D$ depend only on the gauge group, not on the bare coupling.

**Deliverable:** A rigorous theorem: "The lattice gradient flow preserves the polymer expansion of Balaban's effective action with $K$-uniform exponential decay estimates."

**Difficulty assessment:** Moderate. The flow is a deterministic ODE on a compact manifold, and Balaban's polymer expansion is already established. The new content is the compatibility of the two structures.


### 5.2 Phase 2: Continuum limit of flowed correlators (months 3--6)

**Goal:** Prove that $\langle \mathcal{O}_t(x_1) \cdots \mathcal{O}_t(x_n) \rangle_a \to \langle \mathcal{O}_t(x_1) \cdots \mathcal{O}_t(x_n) \rangle$ as $a \to 0$ at fixed $t > 0$.

**Concrete mathematical tasks:**

1. **Cauchy estimate for flowed Schwinger functions.** Prove the Cauchy estimate (3.3) using the flowed polymer expansion of Phase 1. The argument parallels the preprint's RG telescoping sum (Section 5.4) but with the additional UV factor $e^{-tp^2}$ from the flow propagator. The flow factor improves the convergence rate from $O(g_k^4)$ (unflowed) to $O(g_k^4 \cdot e^{-t/a_k^2})$ (flowed), making the telescoping sum converge doubly exponentially fast.

2. **Uniqueness of the continuum limit.** Show that the limit is unique (not just subsequential) using the same Cauchy argument as Theorem M.2.1 of the preprint, adapted to flowed correlators. The flow's additional UV smoothing should make this straightforward.

3. **OS axiom verification for flowed Schwinger functions.** Verify that the continuum flowed Schwinger functions satisfy OS0--OS4 at each fixed $t > 0$. OS3 (reflection positivity) is inherited from the lattice measure; OS1 (temperedness) is guaranteed by the exponential UV smoothing; OS2 (Euclidean invariance) follows from the rotational invariance of the continuum flow equation; OS4 (symmetry) is trivial.

**Deliverable:** A rigorous theorem: "The continuum limit of the lattice gradient-flow Schwinger functions exists at each fixed $t > 0$, is unique, and satisfies the OS axioms."

**Difficulty assessment:** Moderate-to-hard. This is the flowed analogue of the preprint's main continuum limit theorem (Section 5.7), but with better UV behavior. The new content is adapting the Balaban--RG machinery to accommodate the flow.


### 5.3 Phase 3: Small-flow-time expansion and the $t \to 0$ limit (months 6--9)

**Goal:** Prove that the rescaled flowed correlator converges as $t \to 0^+$ to a well-defined renormalized Schwinger function.

**Concrete mathematical tasks:**

1. **Non-perturbative small-flow-time expansion.** Prove that the flowed effective action $S_k^{\mathrm{eff}}[V, A^{(t)}]$ admits an expansion in powers of $t$ with coefficients that are local gauge-invariant functionals of $V$ and $A$, with remainder controlled by the polymer expansion. The leading term at $t = 0$ is the unflowed effective action; the $O(t)$ correction involves the Laplacian of the effective action (from the heat equation).

2. **Control of operator mixing.** At dimension 4, the only gauge-invariant, $\mathcal{C}$-even, parity-even scalar operator is $\mathrm{Tr}\,F^2$ (the preprint's dimension-6 classification of Section 5.6). This forces the small-flow-time expansion to have a simple structure: the mixing matrix at dimension 4 is $1 \times 1$, so no mixing occurs. At dimension 6 and above, mixing is more complex, but the spectral lemma's $\mathrm{dev} \geq 2$ bound provides non-perturbative suppression of all higher-dimension contributions by factors of $O(g_k^4 \hat{\Delta}^2) = O(t)$ in physical units.

3. **The limiting estimate.** Prove that for fixed non-coincident $x, y$:
$$\frac{S_{2,t}^c(x,y)}{c_1(t)^2} - \frac{S_{2,t'}^c(x,y)}{c_1(t')^2} = O(|t - t'|^\alpha) \tag{5.2}$$
for some $\alpha > 0$, uniformly as $t, t' \to 0^+$. This Cauchy estimate would guarantee the existence of the limit. The argument requires controlling the $t$-derivative of $S_{2,t}^c/c_1^2$, which involves the flow equation applied to the correlator and the $t$-derivative of $c_1(t)$. Both are expressible in terms of known perturbative quantities plus non-perturbative remainders controlled by the polymer expansion.

**Deliverable:** A rigorous theorem: "The renormalized two-point function $S_2^{\mathrm{ren}}(x,y) = \lim_{t \to 0^+} S_{2,t}^c(x,y)/c_1(t)^2$ exists as a finite tempered distribution on $\{(x,y) : x \neq y\}$."

**Difficulty assessment:** Hard. This is the crux of the entire programme. The key risk is that the small-flow-time expansion may be only asymptotic (not convergent) non-perturbatively, and the extracted operator may not be unique. See Section 6 for risk assessment.


### 5.4 Phase 4: Assembly --- stress tensor, OPE, AF match (months 9--12)

**Goal:** Given the renormalized $[\mathrm{Tr}\,F^2]_R$ from Phase 3, construct $T_{\mu\nu}$ via Suzuki's formula, verify the AF match, and state the leading-order OPE.

**Concrete mathematical tasks:**

1. **Stress tensor.** Apply Suzuki's formula (4.5) with the non-perturbatively constructed flowed operators from Phases 1--2 and the $t \to 0$ limit from Phase 3. Verify: symmetry (algebraic), gauge invariance (inherited from flow), conservation (Ward identity from Del Debbio--Patella--Rago), trace anomaly (Spiridonov--Chetyrkin + Phase 3), $H_{\mathrm{OS}} = \int T_{00}\,d^3\vec{x}$ (transfer-matrix argument).

2. **AF short-distance match.** Quote the small-flow-time expansion at one loop (Luscher 2010) and the Reisz power-counting theorem (CMP 116--117) to establish that the renormalized two-point function has the AF-predicted short-distance form (4.2). State the non-perturbative-equals-perturbative hypothesis (H4) as a conditional; note that the gradient-flow framework makes it more plausible by providing a controlled interpolation.

3. **Leading-order OPE.** Extract the identity-channel OPE coefficient $C^{\mathbb{1}}(x-y)$ from $S_2^{\mathrm{ren}}(x,y)$ and verify it matches (4.8). State the subleading channels as conjectural, with perturbative coefficients from Zoller--Chetyrkin.

4. **Higher operators.** Extend the construction to $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$ (needed for $T_{\mu\nu}$) and $[\mathrm{Tr}(D_\rho F_{\mu\nu})^2]_R$ (dimension 6, needed for OPE subleading channels). The gradient-flow construction applies identically; the dimension-6 case involves mixing matrices that can be controlled at one loop.

**Deliverable:** A paper (or section of a paper) establishing L.2--L.4 conditional on L.1 (Phase 3), with explicit constructions via the gradient flow.

**Difficulty assessment:** Moderate. This is largely assembly of established perturbative results on top of the non-perturbative infrastructure from Phases 1--3.


---


## 6. Risk Assessment

### 6.1 What could go wrong

The main risk is in **Phase 3** (the $t \to 0^+$ limit). Three specific failure modes:

1. **The small-flow-time expansion is only asymptotic.** The perturbative expansion (2.4) may not converge non-perturbatively; the coefficients $c_k(t)$ grow factorially at high order (as is typical for perturbative series in QFT). If the expansion is only asymptotic, the extracted operator $[\mathrm{Tr}\,F^2]_R$ may not be uniquely defined --- different resummation schemes could yield different operators.

2. **The flow does not commute cleanly with Balaban's RG.** The gradient flow and Balaban's block-spin RG are both smoothing operations on the gauge field, but they act in different ways (continuous heat-kernel smoothing vs. discrete block averaging). If the two do not commute or interact cleanly, the polymer expansion at flow time $t$ may not inherit the $K$-uniform estimates of the unflowed expansion.

3. **Large-field contributions.** Balaban's polymer expansion is controlled in the small-field domain $\Omega_s$. The gradient flow may map large-field configurations into the small-field domain (good!) or may amplify instanton-like configurations near saddle points of the action (bad!). The contribution of instanton sectors to flowed correlators needs separate analysis.


### 6.2 Mitigation

1. **Asymptotic expansion: Borel summability.** In the gradient-flow context, the small-flow-time expansion has better convergence properties than generic perturbative series, because the flow provides an additional exponential suppression $e^{-tp^2}$ of UV modes. The Balaban framework's analyticity (B1) --- polymer activities are analytic in a $k$-independent disk --- may extend to analyticity in the flow time $t$, which would promote the asymptotic expansion to a convergent one. If analyticity in $t$ can be proved, Borel summability is automatic.

2. **Flow-RG interplay.** The gradient flow at flow time $t$ is equivalent (at leading order) to an RG blocking step at scale $\sqrt{8t}$. This suggests a natural embedding: define the flow time at each RG scale $k$ as $t_k = c \cdot a_k^2$ for a fixed constant $c$, so that the flow and the RG operate at the same scale. This "scale-matched" flow should commute with Balaban's RG up to controlled corrections.

3. **Instantons.** The gradient flow drives the field toward a minimum of the Yang--Mills action. For the vacuum sector (topological charge $Q = 0$), the minimum is the trivial connection $A = 0$, and the flow contracts toward it. For the instanton sector ($Q \neq 0$), the flow converges to the self-dual instanton solution, which has finite action. In either case, the flow maps configurations toward the small-field domain, not away from it. The instanton contribution to flowed correlators is exponentially suppressed by $e^{-8\pi^2|Q|/g^2}$ and does not affect the perturbative small-flow-time expansion at any finite order.


### 6.3 Fallback

If the $t \to 0$ limit cannot be fully controlled, a weaker but still valuable result is available:

> **Weak form of L.1.** *Renormalized composite operators exist at flow time $t > 0$ for all $t$ in a neighborhood of $t = 0$, as operator-valued distributions on the GNS Hilbert space. The family $\{\mathcal{O}_t\}_{t > 0}$ has the correct AF-predicted divergence structure as $t \to 0$: the two-point function satisfies $\langle \mathcal{O}_t(x) \mathcal{O}_t(y) \rangle \sim c_1(t)^2 \cdot C_N |x-y|^{-8} (\log)^{-2}$ at short distances, with the perturbative coefficient $c_1(t)$ and constant $C_N$ of (4.2).*

This weak form does not provide a pointwise operator at $t = 0$, but it provides a family of UV-regularized operators with the correct AF behavior and controlled $t$-dependence. Under a generous reading of Jaffe--Witten section 4 --- "local quantum field operators in correspondence with the gauge-invariant local polynomials in the curvature" --- the flow-regularized family $\{\mathcal{O}_t\}$ at small $t$ may be accepted as the required "correspondence," since the flow smearing at scale $\sqrt{8t}$ is physically negligible at scales $\gg \sqrt{8t}$. This is analogous to the standard lattice-QCD practice of using gradient-flow-smeared operators as physical observables.

A pessimistic reading of Jaffe--Witten would reject this and demand a pointwise $t = 0$ operator. In that case, the weak form would still represent significant progress: it would establish the existence of a one-parameter deformation of the theory with UV-finite composite operators, reducing the remaining problem to a single limiting argument.


---


## 7. What Exists vs. What's New

| Result | Status | Reference |
|:-------|:-------|:----------|
| Gradient flow PDE well-posedness (lattice) | Rigorous (ODE on compact $\mathrm{SU}(N)$) | Luscher, JHEP 08 (2010) 071 |
| Gradient flow PDE well-posedness (continuum, 4D) | Short-time existence rigorous | Struwe, Calc. Var. PDE 2 (1994) 123 |
| Global existence near minimizers (4D, smooth) | Rigorous (Lojasiewicz--Simon) | Feehan, arXiv:1409.1525 |
| UV finiteness at $t > 0$ (perturbative, all orders) | Proved | Luscher--Weisz, JHEP 02 (2011) 051 |
| UV finiteness at $t > 0$ (non-perturbative) | **Open** | --- |
| Small-flow-time expansion (perturbative, 1 loop) | Known | Luscher, JHEP 08 (2010) 071 |
| Small-flow-time expansion (perturbative, 2 loop) | Known | Harlander--Neumann, JHEP 06 (2016) 161 |
| Small-flow-time expansion (perturbative, 3 loop) | Known | Artz et al., JHEP 06 (2019) 121 |
| Small-flow-time expansion (non-perturbative) | **Open** | --- |
| $T_{\mu\nu}$ via gradient flow (perturbative formula) | Complete (Suzuki's formula) | Suzuki, PTEP 2013:083B03 |
| $T_{\mu\nu}$ lattice implementation | Complete | Makino--Suzuki, PTEP 2014:063B02 |
| $T_{\mu\nu}$ Ward identities via gradient flow | Complete | Del Debbio--Patella--Rago, JHEP 11 (2013) 212 |
| Lattice $\to$ continuum for flowed correlators | Perturbative only | Makino--Suzuki 2014; Reisz CMP 116--117 |
| Gradient flow in Balaban's framework | **NEW (this programme)** | --- |
| $K$-uniform flowed polymer activities | **NEW (this programme)** | --- |
| Continuum limit of flowed Schwinger functions | **NEW (this programme)** | --- |
| Non-perturbative $t \to 0^+$ limit | **NEW (this programme)** | --- |
| Non-perturbative $T_{\mu\nu}$ on $\mathcal{H}$ | **NEW (this programme)** | --- |
| Leading-order non-perturbative OPE | **NEW (this programme)** | --- |

**Summary of novelty.** The perturbative gradient-flow literature (2010--2024) is mature and provides all the formulas needed for the small-flow-time expansion, the stress tensor, and the OPE coefficients. What is entirely missing --- and what this programme provides --- is the **non-perturbative** counterpart: embedding the gradient flow into a constructive (Balaban-type) framework, proving non-perturbative UV finiteness at $t > 0$, and controlling the $t \to 0$ limit. The perturbative literature provides the roadmap; the constructive-QFT literature (Balaban, the present preprint) provides the non-perturbative infrastructure; the new mathematics is the bridge between them.


---


## 8. Estimated Timeline and Dependencies

```
Month:  1    2    3    4    5    6    7    8    9    10   11   12
        |----Phase 1----|----Phase 2---------|---Phase 3----|--Phase 4--|
        [flow in Balaban] [continuum limit    ] [$t->0$ limit] [assembly ]
                          [at fixed t > 0     ]              [T, OPE,AF]
```

**Dependencies:**
- Phase 2 depends on Phase 1 (needs flowed polymer activities).
- Phase 3 depends on Phase 2 (needs continuum flowed correlators).
- Phase 4 depends on Phase 3 (needs renormalized local operators).
- Phases 1 and 2 can partially overlap: the polymer activity estimates (Phase 1) and the continuum limit argument (Phase 2) can be developed in parallel once the basic framework is set up.

**Critical path:** Phase 1 $\to$ Phase 3. Phase 3 (the $t \to 0$ limit) is the bottleneck and the hardest step. If Phase 3 succeeds, Phase 4 is mostly assembly. If Phase 3 fails, the fallback (Section 6.3) still delivers a publishable result from Phases 1--2.

**Output:**
- Phases 1--2: one paper on "Gradient flow in constructive Yang--Mills theory: non-perturbative UV finiteness."
- Phase 3: one paper on "Renormalized composite operators via gradient flow in 4D Yang--Mills theory."
- Phase 4: one paper or appendix on "Stress tensor, OPE, and AF matching via gradient flow."

**Total estimated effort:** 9--12 months for a focused researcher or small team with expertise in both constructive QFT (Balaban-type estimates) and the gradient-flow literature. The programme is realistic for a Clay submission timeline, given that the mass gap proof is already complete.


---


## 9. References

### Foundational gradient-flow papers
- [L10] M. Luscher, "Properties and uses of the Wilson flow in lattice QCD," JHEP 08 (2010) 071, arXiv:1006.4518.
- [LW11] M. Luscher and P. Weisz, "Perturbative analysis of the gradient flow in non-abelian gauge theories," JHEP 02 (2011) 051, arXiv:1101.0963.
- [L11] M. Luscher, "Chiral symmetry and the Yang--Mills gradient flow," arXiv:1302.5246 (published as JHEP 04 (2013) 123).
- [L13] M. Luscher, "Future applications of the Yang--Mills gradient flow in lattice QCD," PoS LATTICE2013 (2013) 016, arXiv:1308.5598.

### Stress tensor via gradient flow
- [S13] H. Suzuki, "Energy-momentum tensor from the Yang--Mills gradient flow," PTEP 2013 (2013) 083B03, arXiv:1304.0533.
- [MS14] H. Makino and H. Suzuki, "Lattice energy-momentum tensor from the Yang--Mills gradient flow --- including fermions," PTEP 2014 (2014) 063B02, arXiv:1403.4772.
- [DPR13] L. Del Debbio, A. Patella, and A. Rago, "Space-time symmetries and the Yang--Mills gradient flow," JHEP 11 (2013) 212, arXiv:1306.1173.

### Higher-order perturbative coefficients
- [HN16] R. V. Harlander and T. Neumann, "The perturbative QCD gradient flow to three loops," JHEP 06 (2016) 161, arXiv:1606.03756.
- [AHNS19] J. Artz, R. V. Harlander, F. Lange, T. Neumann, and M. Steinhauser, "Results and techniques for higher order calculations within the gradient-flow formalism," JHEP 06 (2019) 121, arXiv:1905.00882.
- [H22] R. V. Harlander et al., "The gradient flow at higher orders in perturbation theory," arXiv:2111.14376.

### Rigorous PDE results
- [R92] J. Rade, "On the Yang--Mills heat equation in two and three dimensions," J. Reine Angew. Math. 431 (1992) 123--163.
- [St94] M. Struwe, "The Yang--Mills flow in four dimensions," Calc. Var. PDE 2 (1994) 123--150.
- [F14] P. M. N. Feehan, "Global existence and convergence of solutions to gradient systems and applications to Yang--Mills gradient flow," arXiv:1409.1525.

### Probabilistic and constructive approaches
- [C18] S. Chatterjee, "Yang--Mills for probabilists," Probability and Analysis in Interacting Physical Systems, Springer PROMS 283 (2019) 1--16, arXiv:1803.01950.
- [B84--89] T. Balaban, "Renormalization group approach to lattice gauge field theories," CMP 95 (1984) -- CMP 119 (1989), series of papers.
- [D11] J. Dimock, "The renormalization group according to Balaban, I. Small fields," Rev. Math. Phys. 25 (2013) 1330010, arXiv:1108.1335.

### Perturbative composite operators and OPE
- [KSZ75] H. Kluberg-Stern and J.-B. Zuber, "Renormalization of non-Abelian gauge theories in a background-field gauge. II. Gauge-invariant operators," Phys. Rev. D 12 (1975) 3159.
- [S84] V. P. Spiridonov, "Anomalous dimension of the pion operator at the non-trivial point $4-\epsilon$," Yad. Fiz. 39 (1984) 1522 (Sov. J. Nucl. Phys. 39 (1984) 961).
- [CDJ77] J. C. Collins, A. Duncan, and S. D. Joglekar, "Trace and dilatation anomalies in gauge theories," Phys. Rev. D 16 (1977) 438.
- [ZC12] M. F. Zoller and K. G. Chetyrkin, "OPE of the pseudo-scalar gluonium correlator in massless QCD to three-loop order," JHEP 12 (2012) 119.
- [SVZ79] M. A. Shifman, A. I. Vainshtein, and V. I. Zakharov, "QCD and resonance physics," Nucl. Phys. B 147 (1979) 385, 448.

### Lattice perturbation theory
- [R88] T. Reisz, "A power counting theorem for Feynman integrals on the lattice," CMP 116 (1988) 81; "Renormalization of lattice Feynman integrals with massless propagators," CMP 117 (1988) 79.
- [CCMP89] S. Caracciolo, G. Curci, P. Menotti, and A. Pelissetto, "The energy-momentum tensor on the lattice: the scalar case," Nucl. Phys. B 309 (1988) 612; Phys. Lett. B 228 (1989) 375.
- [Cap03] S. Capitani, "Lattice perturbation theory," Phys. Rep. 382 (2003) 113, hep-lat/0211036.

### Hollands--Wald and rigorous OPE
- [HW01] S. Hollands and R. M. Wald, "Local Wick polynomials and time-ordered products of quantum fields in curved spacetime," CMP 223 (2001) 289.
- [HW10] S. Hollands and R. M. Wald, "Axiomatic quantum field theory in curved spacetime," CMP 293 (2010) 85.
- [Ho07] S. Hollands, "The operator product expansion for perturbative quantum field theory in curved spacetime," CMP 273 (2007) 1.
- [Bo05] H. Bostelmann, "Phase space properties and the short distance structure in quantum field theory," J. Math. Phys. 46 (2005) 082304.
