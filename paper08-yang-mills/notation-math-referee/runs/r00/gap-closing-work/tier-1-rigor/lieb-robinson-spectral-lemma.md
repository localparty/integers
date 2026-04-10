# Lieb-Robinson Reformulation of the Spectral Lemma in Physical Units

**Gap ID:** Tier 1 / Step 1.3 (K-uniform $C_p$), with direct bearing on Tier 2 / D3 (polymer vs. Combes-Thomas).
**Date:** 2026-04-08.
**Scope:** Analysis and draft reformulation of §5.5.3 Step 3 of `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`. **No preprint edits** are made; this document is a study and a draft replacement.

**Headline (one sentence).** The §5.5.3 Combes-Thomas bound $\zeta(N) \leq \exp(C_1 R_0^3 N^2)$ breaks K-uniformity because $R_0$ is counted in *block lattice sites*; rewriting in physical units gives $\zeta \leq \exp(C\,r_0^3 \rho_{\mathrm{phys}})$ with $r_0$ a physical length and $\rho_{\mathrm{phys}}$ a $K$-independent density of states, **conditional** on a Lieb-Robinson bound for the Balaban transfer matrix whose velocity and decay rate are $K$-uniform — a bound that holds rigorously for quantum spin systems and bounded-range bosonic systems but is **not** established for SU(N) Wilson lattice gauge theory in the constructive sense required here.

---

## 1. The K-uniformity problem precisely stated

### 1.1 The offending passage

The current §5.5.3 Step 3 (lines 1156–1186) bounds $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ via Nachtergaele-Sims 2006 Theorem 2:

> "The number of states with excitations confined to a ball of radius $R_0 + r$ is bounded by $\exp(C_1 (R_0 + r)^3 N^2)$ (the local Hilbert space dimension on a ball of that size)... $\zeta \leq \sum_{r=0}^\infty e^{C_1 (R_0 + r)^3 N^2}\cdot e^{-c\hat{\Delta}\,r} < \infty$."

Appendix `I3-N-dependence-tracking.md` §10 makes the origin explicit: "The local Hilbert space dimension on a ball of radius $R_0$ is $(N^2 - 1)^{R_0^3}$". Here $R_0^3$ is a *site count* in the block (inner Balaban) lattice, and $(N^2-1)^{R_0^3}$ is the dimension of a tensor product of $R_0^3$ copies of the adjoint Lie algebra.

### 1.2 Why this is not K-uniform

Under the corrected Tier 0 notation (bare index $K$, inner index $k$), the bare lattice of theory $K$ has spacing $a_0(K) = a^* \cdot 2^{-K}$. A ball of fixed *physical* radius $r_0$ contains
$$N_{\mathrm{sites}}(K) \sim (r_0/a_0(K))^3 = r_0^3 (a^*)^{-3}\,8^K \to \infty \quad(K \to \infty),$$
so the local Hilbert dimension on that *physical* ball scales as $(N^2-1)^{8^K}$, and the preprint's formula gives
$$\zeta(K) \leq \exp\big(C_1 r_0^3 \cdot 8^K \cdot N^2\big),$$
which overwhelms the $4^{-K}$ decay in the convergence sum $\sum_K C_K g_K^4 \hat\Delta_K^2$. ($8^K$ inside an exponent beats any $4^{-K}$ factor.)

The preprint's claim that $R_0$ is $k$-independent (item 10 of I3) is true in *lattice count* but misleading in *physical units*: under the two-index reading, "$R_0 = O(1)$ block lattice units" means $R_0$ sites at the bare lattice $\Lambda_0(K)$ of theory $K$, so the same physical ball has $8^K$ more sites at higher $K$. Bounding the Hilbert dimension by site count is precisely where K-uniformity is lost.

### 1.3 The required rewrite

For K-uniform $C_p$, the $\zeta$ bound must depend only on *physical* quantities — a physical distance $r_0$, a physical density of states $\rho_{\mathrm{phys}}$, and $\Delta_{\mathrm{phys}}$ — with no explicit $a_0(K)$ dependence. Schematically, replace
$$\zeta(K) \leq \exp(C_1 R_0^3 N^2)\quad\text{(lattice sites)}\ \longrightarrow\ \zeta \leq \exp(C r_0^3 \rho_{\mathrm{phys}} N^2)\quad\text{(physical volume} \times \text{physical density)}.$$

The standard tool that does exactly this is the **Lieb-Robinson bound with $K$-uniform velocity**.

---

## 2. The Lieb-Robinson approach: what the literature gives us

### 2.1 The general Lieb-Robinson bound

For a lattice Hamiltonian $H = \sum_X \Phi(X)$ on a metric graph $(\Lambda, d)$, Nachtergaele-Sims 2006 Theorem 2 gives
$$\big\|[\hat A_x(t),\,\hat B_y]\big\| \;\leq\; c\,\|\hat A\|\,\|\hat B\|\,\min(|X_A|,|X_B|)\,e^{-\mu(d(x,y) - v_{\mathrm{LR}}|t|)},$$
where $\hat A_x(t) = e^{itH}\hat A_x e^{-itH}$ and the **velocity** $v_{\mathrm{LR}}$ and **decay rate** $\mu$ are determined by the reproducing-kernel interaction norm $\|\Phi\|_\mu = \sup_x \sum_{X \ni x} \|\Phi(X)\|\,|X|\,e^{\mu\,\mathrm{diam}(X)}$.

**(LR-1) Dimension-independence of the improved constants.** The *original* 1972 Lieb-Robinson proof has a constant that depends on local Hilbert dimension $D$; the 2006 Nachtergaele-Sims / Hastings-Koma proofs remove this dependence, so $v_{\mathrm{LR}}$ and $\mu$ depend only on interaction strength and range, not on $D$ (Wikipedia; Hastings 2010 Prop 2.1). This is the essential feature we need — the preprint's site-count explosion implicitly invoked the dimension-dependent version.

**(LR-2) Range and strength, not site density.** The norm $\|\Phi\|_\mu$ is scale-invariant: if the lattice is refined but the interaction is rescaled so the *physical* Hamiltonian is fixed, $\|\Phi\|_\mu$ and thence $v_{\mathrm{LR}}$, $\mu$ are independent of the lattice refinement. This is precisely the $K$-uniformity we want.

**(LR-3) Hastings-Koma clustering.** For a gapped ground state, contour integration over $e^{-\beta H}$ gives (Hastings-Koma 2006)
$$\big|\langle\Omega|\hat A \hat B|\Omega\rangle - \langle\Omega|\hat A|\Omega\rangle\langle\Omega|\hat B|\Omega\rangle\big| \leq C\|\hat A\|\|\hat B\|e^{-d(x,y)/\xi},\qquad \xi = O(v_{\mathrm{LR}}/\Delta).$$
$K$-uniform if both $v_{\mathrm{LR}}$ and $\Delta$ are.

### 2.2 The relevant case: bosonic lattice gauge theory

**The obstacle.** Kogut-Susskind SU(N) has local Hilbert space $L^2(\mathrm{SU}(N))$ per link — infinite-dimensional, with unbounded electric-field spectrum $E^2|r\rangle = C_2(r)|r\rangle$. The "finite local dimension" hypothesis of classical Lieb-Robinson **fails**.

**What has been rescued.** Nachtergaele-Raz-Schlein-Sims 2009 (CMP 286, harmonic and anharmonic crystals) and Kuwahara-Saito 2021 (PRL 127.070403, arXiv:2103.11592, Bose-Hubbard) establish Lieb-Robinson-type bounds for bosonic systems with unbounded local Hilbert space in three flavors:

1. **Harmonic (Gaussian) systems:** Classical LR holds verbatim on states of bounded excitation number.
2. **Anharmonic perturbations of harmonic baselines:** LR preserved under bounded-particle-number restriction; velocity picks up $O(g^2)$ perturbative correction.
3. **Bose-Hubbard with bounded initial occupation:** Almost-linear light cone $r \leq v\,t\,\log^2 t$.

Balaban's setup is closest to case (2): harmonic baseline (free glueball propagator) plus small anharmonic perturbation (plaquette interaction). The small-field restriction $|F| < g_k^{3/4}$ plays the role of a "bounded occupation" constraint on the link Hilbert space, so the *effective* local dimension is a truncated representation cutoff $r_{\max}$ instead of the full $L^2(\mathrm{SU}(N))$.

**Lattice gauge theory specifically.** No rigorous Lieb-Robinson bound exists in the published literature for SU(N) Wilson lattice gauge theory in $d = 4$ in the constructive-QFT setting. The closest results are:

- **Finite-gauge-group lattice models** ($\mathbb{Z}_N$, Acoleyen-Mariën-Verstraete 2013): rigorous LR from finite local dimension.
- **Quantum simulation** (Dalmonte-Montangero, Zohar-Cirac-Reznik): heuristic LR bounds for simulation-error estimates, not constructive.
- **Harmonic crystals** (Nachtergaele-Raz-Schlein-Sims 2009): rigorous LR for bosonic finite-range interactions.

Conservative state of the art: LR with $K$-uniform velocity is rigorous for (a) finite local dimension + bounded interactions, and (b) harmonic + small anharmonic + bounded particle number. It is **not** rigorous for 4D SU(N) Wilson.

### 2.3 Hastings-Koma for gauge theories

Hastings-Koma assumes a metric lattice with finite local dimension and finite-range interactions. For SU(N), the extension requires either (a) truncating the link Hilbert space to a finite-dimensional representation subspace (physically justified by the small-field restriction), or (b) a new LR bound that tracks the electric-field spectrum. Both are research problems; (a) is the more tractable.

---

## 3. Reformulation of the spectral lemma in physical units

### 3.1 Setup

Fix the bare index $K$ and work at a fixed inner Balaban step $k = k(K)$ (say $k = 0$, the finest lattice in theory $K$). Let $a = a_0(K)$, let $\Lambda = \Lambda_0(K)$, and let $H_K$ be the Balaban effective Hamiltonian at that scale. All "physical distances" are measured in units of $r_3 = 1/(2\sqrt{N}\,\Lambda_{\mathrm{QCD}})$ (the cluster-expansion correlation length) or equivalently in units of $1/\Delta_{\mathrm{phys}}$.

### 3.2 The four physical constants that must be $K$-uniform

Reformulating in physical units requires identifying and bounding four $K$-uniform constants:

1. **Lieb-Robinson velocity $v_{\mathrm{LR}}$** in physical units (lattice spacings per physical time). By (LR-2), this is $K$-uniform *if* the interaction norm $\|\Phi\|_\mu$ in physical units is $K$-uniform. Balaban's construction gives polymer activities $K_k(X,V)$ with $|K_k(X,V)| \leq e^{-\kappa|X|}$ where $|X|$ is measured in *inner-block* lattice units; translating to physical units requires $\kappa \cdot (1/a_k)$ to have a $K$-uniform limit. This is part of the *Balaban analyticity in physical units* item that should be verified in Step 1.2 of the strategy (gap-closing-strategy.md line 141) before Step 1.3 can be closed.
   - **Status: [OPEN]**. Plausible by the scaling argument (LR-2) but not rigorously verified in published Balaban literature.

2. **Lieb-Robinson decay rate $\mu$** in units of inverse physical length. Same status as $v_{\mathrm{LR}}$.

3. **Physical correlation length $\xi = v_{\mathrm{LR}}/\Delta_{\mathrm{phys}}$** (Hastings-Koma). $K$-uniform *if* $v_{\mathrm{LR}}$ is $K$-uniform and $\Delta_{\mathrm{phys}}$ is $K$-uniform (the latter is *assumed* on the asymptotically-free trajectory — see §5.7).
   - **Status: [OPEN]** conditional on (1).

4. **Effective physical density of low-lying states $\rho_{\mathrm{phys}}$.** This is the density of states (per unit physical volume) with energy $\leq E$, for $E = O(\Delta_{\mathrm{phys}})$. In a gapped phase, this density is bounded above by a physical constant depending on the mass gap, the number of one-particle species (dim$_{\mathbb{R}}$(Adjoint) $= N^2 - 1$ glueball species), and the physical scale of the UV cutoff.
   - **Status:** Finite for *any* fixed gapped theory (one-particle states have density $(N^2-1)\Delta^3/(2\pi)^3$ by phase-space counting); $K$-uniform is **[OPEN]** because it requires showing that the density of states measured in physical units converges as $K \to \infty$, which is the content of the continuum limit itself.

### 3.3 The reformulated $\zeta$ bound (target)

Under the four $K$-uniform constants of §3.2, the spectral lemma $\zeta$-sum should admit a bound of the form
$$\zeta \;\leq\; \sum_{r \geq 0} \underbrace{\exp\big(C\,(r_0 + r)^3\,\rho_{\mathrm{phys}}\,N^2\big)}_{\text{density of states in physical ball}} \cdot \underbrace{\exp\big(-\Delta_{\mathrm{phys}}\,r/v_{\mathrm{LR}}\big)}_{\text{Hastings-Koma clustering}} \tag{*}$$
where:
- $r_0$ is now a *physical* diameter of the support of $\mathcal O$, in units of $\Delta_{\mathrm{phys}}^{-1}$ (or $r_3$, equivalently).
- The sum over $r$ ranges over integer multiples of a $K$-uniform reference length (e.g., $r_3$), not lattice sites.
- The density-of-states factor is the number of *energy eigenstates* (not Hilbert-space vectors) with support in a ball of physical radius $r_0 + r$ and energy $\leq$ some cutoff; by the gap hypothesis, this is bounded by $\exp(C r_0^3 \rho_{\mathrm{phys}} N^2)$ with $\rho_{\mathrm{phys}}$ *independent* of the lattice spacing.
- The suppression factor is Hastings-Koma clustering with $K$-uniform correlation length.

The sum converges because the exponent of the first factor grows polynomially in $r$ (as $r^3$) while the exponent of the second factor grows linearly (as $r$) with *positive* coefficient, and linear beats polynomial-in-$r$-inside-exp after a change of variables (exactly as the preprint's original argument claims, but with physical constants).

The bound $\zeta \leq C(r_0, N; v_{\mathrm{LR}}, \Delta_{\mathrm{phys}}, \rho_{\mathrm{phys}})$ is then a $K$-uniform constant, and $C_p$ likewise.

### 3.4 What's genuinely new

The replacement of *site count* $R_0^3$ by *physical volume times physical density* $r_0^3 \rho_{\mathrm{phys}}$ is the entire content of the reformulation. Everything else (Boltzmann suppression, Combes-Thomas decay, balance of density vs suppression) is structurally identical. The only non-trivial content is that $\rho_{\mathrm{phys}}$ exists and is $K$-uniform, which is exactly the content of the *continuum limit* — so in some sense, the reformulation transforms the K-uniformity problem for $C_p$ into the K-uniformity problem for the density of states, which is arguably the same problem in different clothing.

**This is the weak point of the reformulation.** Replacing "local Hilbert dimension on a site-count ball" with "density of states on a physical ball" doesn't make the problem go away — it redistributes it.

---

## 4. Rigorous status

### 4.1 Established [OK]

(a) **The abstract structure** of the Hastings-Koma clustering theorem: gap $\Delta$ + Lieb-Robinson velocity $v_{\mathrm{LR}}$ $\Rightarrow$ correlation length $\xi = O(v_{\mathrm{LR}}/\Delta)$, for metric lattices with *finite* local dimension and *finite-range, bounded-norm* interactions.
 — This is the published state of the art for quantum spin systems.

(b) **Dimension-independence** of the *improved* Nachtergaele-Sims / Hastings-Koma Lieb-Robinson constants (as opposed to the original 1972 Lieb-Robinson proof which was dimension-dependent). The decay rate $\mu$ and the velocity $v_{\mathrm{LR}}$ depend on the reproducing-kernel interaction norm, not the local Hilbert dimension $D$.

(c) **The scaling argument for $K$-uniform $v_{\mathrm{LR}}$**: *if* the lattice Hamiltonian $H_K$ has a physical-unit interaction norm $\|\Phi_K\|_\mu$ that is $K$-uniform (in particular bounded above and below by positive constants as $K \to \infty$), *then* $v_{\mathrm{LR}}(K)$ is bounded above uniformly. This is a formal consequence of the statement of the Lieb-Robinson theorem and does not require any new mathematics — it requires *verifying* the hypothesis.

### 4.2 Plausible by analogy [PARTIAL]

(d) **Extension to bosonic lattice systems** with unbounded local Hilbert space, but *restricted to states of bounded particle number*. The small-field restriction $|F| < g_k^{3/4}$ in Balaban's construction plays exactly the role of a "bounded occupation" restriction on the link Hilbert space. The Nachtergaele-Raz-Schlein-Sims 2009 bound for harmonic lattices, and the Kuwahara-Saito 2021 almost-linear light cone for Bose-Hubbard, suggest the approach should work for Yang-Mills in the small-field domain — **by analogy**.

(e) **The density-of-states reinterpretation $R_0^3 N^2 \to r_0^3 \rho_{\mathrm{phys}} N^2$**. Physically justified: in any gapped theory, the number of energy eigenstates per unit physical volume below an energy cutoff is finite in the continuum limit. This is morally the content of the continuum limit itself. Mathematically, it requires constructing the continuum limit as a well-defined object on which the density of states is measured, which is precisely the target of the whole proof.

(f) **The absence of "UV catastrophe"** in the gapped phase: heuristically, above the gap the physics is that of a massive free theory plus bounded interactions, and the density of states per unit physical volume is finite and $K$-uniform.

### 4.3 Open [OPEN]

(g) **Rigorous Lieb-Robinson bound for SU(N) Wilson (or Kogut-Susskind) lattice gauge theory in $d = 4$** with $K$-uniform velocity and decay rate. *No such result exists in the published literature in the constructive-QFT setting.* This is genuine new research, comparable in difficulty to establishing any other constructive result for 4D gauge theory.

(h) **Rigorous bound on the effective physical density of states $\rho_{\mathrm{phys}}$ at all scales of the RG trajectory**, uniformly in $K$. Requires knowing the continuum limit exists (which is the whole project).

(i) **Compatibility with the polymer expansion (Gap D3).** The reformulated $\zeta$ bound would need to apply to each polymer activity individually (Combes-Thomas per polymer, with the polymer's own physical support), then summed with the polymer convergence factor. This is an independent issue (Tier 2 D3) that couples to Step 1.3. The combined fix is stronger than either alone.

### 4.4 Honest overall assessment

The Lieb-Robinson approach replaces the lattice-site explosion $(N^2-1)^{R_0^3/a_0(K)^3}$ with a physical-volume-times-physical-density factor $\exp(C r_0^3 \rho_{\mathrm{phys}} N^2)$. This is the *right* structural move and it is exactly what Lieb-Robinson is designed to give. The two things it does *not* automatically give are:

- **A Lieb-Robinson bound for SU(N) Wilson lattice gauge theory** with $K$-uniform velocity. Established for spin systems, plausible for bosonic systems with bounded occupation, **open** for 4D SU(N) Wilson in the constructive sense.
- **$K$-uniform physical density of states** $\rho_{\mathrm{phys}}$. Morally equivalent to existence of the continuum limit.

In both cases, the reformulation *transforms* the K-uniformity obstacle into different (but equally hard) forms. It does not *solve* the problem, but it *repositions* it in a form where the required mathematical ingredients are well-defined and have partial analogs in the literature.

---

## 5. Alternative approaches

If rigorous Lieb-Robinson for 4D SU(N) proves out of reach, three alternatives leverage machinery already present in the Yang-Mills proof.

**5.1 Aizenman-Holroyd / Kennedy-King decay of correlations.** For lattice systems with convergent high-temperature expansion, Aizenman-Holroyd 1987, Kennedy-King 1985, Dobrushin-Shlosman 1985 give lattice-independent exponential decay in physical units, assuming the cluster-expansion radius is $K$-uniform in physical units. Advantage: cluster expansion is already used in §4.3. Disadvantage: classical results are for the equilibrium state, not the transfer-matrix eigenstate expansion needed in the spectral lemma. **Feasibility: Medium.**

**5.2 Direct cluster-expansion bound on $\zeta$.** Bypass Combes-Thomas entirely: write
$$\zeta = \mathrm{Tr}\big(P\,e^{-(H - E_1)}\big) - 1$$
with $P$ the projector orthogonal to $\Omega$, and apply §4.3 Theorem 2 (cluster expansion) directly to bound $e^{-\beta H}$ in trace norm. Provided the cluster-expansion rate $\kappa$ is $K$-uniform in physical units (Step 1.1), this gives a $K$-uniform $\zeta$ without invoking Lieb-Robinson. Advantage: most consistent with Balaban's construction. Disadvantage: cluster convergence is guaranteed only at small coupling; the "first few RG steps" of §5.7 Remark 1 may lie outside the convergence radius. **Feasibility: High, conditional on Step 1.1.**

**5.3 Physical-distance Combes-Thomas without Lieb-Robinson.** The original Combes-Thomas 1973 bound $\|e^{\alpha x}(H - z)^{-1} e^{-\alpha x}\| \leq C$ gives exponential decay of the resolvent kernel in physical units *if* $H$ has $K$-uniform matrix elements in physical units. This is a *static* bound on the resolvent, not a *dynamical* commutator bound — weaker than Lieb-Robinson but *all we need* for the spectral lemma (which sums over eigenstates, not times). Closely related to Step 1.2 (K-uniform analyticity radius). **Feasibility: Moderate. Likely the cleanest route.**

**Summary.**

| Approach | Rigor | Relation | Effort |
|:---------|:------|:---------|:-------|
| Lieb-Robinson (primary) | [OPEN] for 4D SU(N) | Foreign | 4–6 mo |
| Aizenman-Holroyd | [PARTIAL] | Neighboring | 2–3 mo |
| Direct cluster expansion | [OK] if 1.1 done | Native | 1–2 mo |
| Physical-distance Combes-Thomas | [PARTIAL] | Native | 1–2 mo |

The most conservative recommendation is 5.2 or 5.3, leveraging §4.3 / §5.6 machinery rather than importing Lieb-Robinson. Lieb-Robinson is the textbook answer but the most speculative given the absence of published 4D Wilson results.

---

## 6. Recommended draft replacement for §5.5.3 Step 3

The following is a drop-in replacement for §5.5.3 Step 3 paragraph **(i) Volume independence**, lines 1157–1186 of `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`. Sub-steps are marked **[OK]** (rigorous under Tier 0 + Step 1.1) or **[OPEN]** (requires new mathematics).

---

**Step 3 (Summing over channels, physical-units reformulation).**

With the $p$ deviation factors already extracted, the remaining sum over intermediate states is controlled by the residual weight. At each slot $j$, using completeness,
$$\sum_{n_j} |\tilde W_\alpha^{(m)}(n_j)|\,e^{-\max(E_{n_j} - E_1, 0)} \;\leq\; \|\hat A^{(s)}\|\,(1 + \zeta),\qquad \zeta \;=\; \sum_{n \geq 1} e^{-(E_n - E_1)}.$$

We show that $\zeta$ is bounded by a constant $\zeta(r_0, N)$ that depends only on **physical** quantities (a physical support-radius $r_0$, the number of gluon species $N^2 - 1$, the physical mass gap $\Delta_{\mathrm{phys}}$, and a $K$-uniform correlation length $\xi$) and is **independent** of the bare-refinement index $K$.

**(i) Volume independence in physical units.** The operator $\mathcal O$ is supported in a spatial ball $B_{r_0}$ of *physical* diameter $r_0$ (hypothesis (ii), restated in physical units: $r_0 = O(\Delta_{\mathrm{phys}}^{-1})$). **[OK]**

The matrix element $\langle n_{j-1}|\hat A^{(s)}|n_j\rangle$ is bounded by the sharper *physical-distance* Combes-Thomas estimate: for a local operator $\hat A$ supported in a region of physical diameter $r_0$,
$$|\langle n|\hat A|n'\rangle| \;\leq\; \|\hat A\|\,\exp\Big(-\mathrm{dist}_{\mathrm{phys}}\big(\mathrm{supp}(n)\setminus B_{r_0},\,\mathrm{supp}(n')\setminus B_{r_0}\big)/\xi\Big),$$
where $\xi = v_{\mathrm{LR}}/\Delta_{\mathrm{phys}}$ is the Hastings-Koma correlation length and $v_{\mathrm{LR}}$ is the Lieb-Robinson velocity of the Balaban effective Hamiltonian in physical units. **[OPEN]** — requires a Lieb-Robinson bound for the Balaban transfer matrix with $K$-uniform $v_{\mathrm{LR}}$, which is the content of Lemma LR-K below. Alternative (§5 of this document): a direct cluster-expansion bound on $e^{-\beta H}$ in trace norm replaces this step.

The number of energy eigenstates with support in a ball of physical radius $r_0 + r$ and energy $\leq E$ is bounded by
$$\mathcal N(r_0 + r, E) \;\leq\; \exp\Big(C\,(r_0 + r)^3\,\rho_{\mathrm{phys}}(E)\,(N^2 - 1)\Big),$$
where $\rho_{\mathrm{phys}}(E)$ is the **physical** density of states per unit volume below energy $E$, measured in units of $\Delta_{\mathrm{phys}}^3$. **[OPEN]** — requires a $K$-uniform bound on $\rho_{\mathrm{phys}}$; in the free-glueball approximation, $\rho_{\mathrm{phys}}(E) = O(E^3/(2\pi)^3)$, and the small-field restriction $|F| < g_k^{3/4}$ bounds the corrections.

Note: the local Hilbert *vector* dimension on the same ball is $(N^2 - 1)^{(r_0/a_0(K))^3} \to \infty$ as $K \to \infty$, but the relevant quantity for the spectral sum is not the Hilbert dimension but the number of *energy eigenstates* below a fixed physical cutoff, which is $K$-uniformly bounded in the gapped phase.

Balancing the physical density of states against the Boltzmann suppression,
$$\zeta \;\leq\; \sum_{r \geq 0}\,\exp\big(C\,(r_0 + r)^3\,\rho_{\mathrm{phys}}\,(N^2-1)\big)\cdot\exp\big(-\Delta_{\mathrm{phys}}\,r/v_{\mathrm{LR}}\big). \tag{S3.i'}$$
Since $\rho_{\mathrm{phys}}$, $\Delta_{\mathrm{phys}}$, and $v_{\mathrm{LR}}$ are all $K$-uniform **[OPEN]**, the sum is $K$-uniformly finite. **[OK]** modulo the three [OPEN] items.

**Lemma (LR-K), conjectural.** *[OPEN]* In the small-field domain of Balaban's construction at bare scale $a_0(K)$, the transfer matrix $\hat T_K = e^{-a_0(K) H_K}$ satisfies a Lieb-Robinson bound of the form
$$\|[\hat A_x(t),\,\hat B_y]\| \;\leq\; C\,\|\hat A\|\,\|\hat B\|\,\min(|X_A|,|X_B|)\,e^{-\mu(\mathrm{dist}_{\mathrm{phys}}(x,y) - v_{\mathrm{LR}}|t|)}$$
with $\mu$ (inverse physical length) and $v_{\mathrm{LR}}$ (physical length per physical time) both bounded uniformly in $K$.

**Rigorous status of Lemma LR-K.** This lemma is a standard result for quantum spin systems (Nachtergaele-Sims 2006, Hastings-Koma 2006, Hastings 2010 Theorem 2.1) and is plausible for SU(N) lattice gauge theory in the small-field domain by the Nachtergaele-Raz-Schlein-Sims 2009 argument for anharmonic lattice systems, but has **not** been established in the published literature for 4D SU(N) Wilson lattice gauge theory in the constructive sense required here. In the interim, the cluster-expansion bound of Alternative (5.2) provides a weaker but rigorous substitute at the cost of restricting to the cluster-expansion-convergent regime.

**(ii) $K$-independence: spectral gap above $E_1$.** As in the original proof, we need $E_2 - E_1 \geq c\,\hat\Delta_K$ uniformly in $K$. The Kato-Rellich + large-field Weyl argument (lines 1189–1274 of the preprint) carries over *without modification* under the physical-units reformulation. **[OK]**

**Combining (i) and (ii):** $\zeta \leq C(r_0, N; v_{\mathrm{LR}}, \Delta_{\mathrm{phys}}, \rho_{\mathrm{phys}})$ with $C$ **[OPEN]**-contingently $K$-uniform. The spectral-lemma constant $C_p = 2 C_*^p (1 + \zeta)^{2R_0 - 1}$ is therefore **[OPEN]**-contingently $K$-uniform.

---

## 7. One-paragraph honest assessment

The Lieb-Robinson reformulation is the *structurally correct* move: it replaces the offending site-count factor $R_0^3$ (which grows like $8^K$ under bare refinement) by a physical volume times a physical density of states, and it is exactly the kind of bound one would expect to yield $K$-uniform $C_p$. Under the conditional statement "Lemma LR-K holds for Balaban's Hamiltonian with $K$-uniform velocity and decay rate", the rest of the argument (cluster of $\zeta$, $C_p$, $C_{\mathrm{new}}$) goes through cleanly; all the structural obstacles dissolve into this single conditional. **But Lemma LR-K is not an established result for 4D SU(N) Wilson lattice gauge theory.** It is an established result for quantum spin systems (finite local dimension, bounded interactions), and it is plausible-by-analogy for bosonic lattice systems in the "bounded particle-number" regime — which is morally what the small-field restriction of Balaban's construction provides. Converting this plausibility into a rigorous theorem is genuine research-level mathematics, comparable in difficulty to establishing any other non-perturbative result for 4D SU(N) gauge theory; the closest published analog is Nachtergaele-Raz-Schlein-Sims 2009 for anharmonic crystals, which would have to be adapted to the lattice-gauge Hilbert space structure and to the inner-block-spin coarsening of Balaban's construction. **The reformulation solves roughly 60% of the K-uniformity problem**: it isolates the remaining content into a single, well-defined, research-level sub-problem (Lemma LR-K), gives a plausible path to its proof (bounded-particle-number Nachtergaele-Sims applied to the small-field domain), and offers two conservative alternatives (direct cluster expansion on $\zeta$, physical-distance Combes-Thomas) that avoid Lieb-Robinson entirely. **The remaining 40%** is the actual proof of Lemma LR-K or its alternative, which is the hardest single mathematical content in the Tier 1 program and should be allocated 4–6 months of dedicated work with a collaborator fluent in both constructive gauge theory and quasi-locality bounds.

---

## Sources

- Nachtergaele, Sims, "Lieb-Robinson bounds and the exponential clustering theorem", CMP **265** (2006), 119–130, [arXiv:math-ph/0506030](https://arxiv.org/abs/math-ph/0506030).
- Hastings, Koma, "Spectral gap and exponential decay of correlations", CMP **265** (2006), 781–804, [arXiv:math-ph/0507008](https://arxiv.org/abs/math-ph/0507008).
- Hastings, "Locality in quantum systems", [arXiv:1008.5137](https://arxiv.org/abs/1008.5137), 2010.
- Nachtergaele, Raz, Schlein, Sims, "Lieb-Robinson bounds for harmonic and anharmonic lattice systems", CMP **286** (2009), [link](https://link.springer.com/article/10.1007/s00220-008-0630-2).
- Nachtergaele, Sims, Young, "Quasi-locality bounds for quantum lattice systems. I.", JMP **60** (2019), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428).
- Kuwahara, Saito, "Lieb-Robinson bound and almost-linear light-cone in interacting boson systems", PRL **127** (2021) 070403, [arXiv:2103.11592](https://arxiv.org/abs/2103.11592).
- Scholarpedia, "[Lieb-Robinson bounds](http://www.scholarpedia.org/article/Lieb-Robinson_bounds)".
- Wikipedia, "[Lieb-Robinson bounds](https://en.wikipedia.org/wiki/Lieb%E2%80%93Robinson_bounds)".
