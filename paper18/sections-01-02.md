# The Cosmic Ladder: Computing the First Moments of the Universe and the Generations of Stars from the Riemann Zeros

**REVISED 2026-04-10** — Propagated 3 critical + 5 major issues from independent review.

## Sections 1--2: Introduction and the Pre-Big-Bang Galois Phase

---

# 1. Introduction

## 1.1 The cosmic ladder concept

The Critical Bost--Connes--Brauer system $\mathcal{C} = (H_R, \hat{R}, \omega_1, M_{\mathrm{geom}}, \{\beta_k\})$ encodes the universe's history in its spectrum. Paper 23 established that the 36 observables of the Standard Model and cosmology are matrix elements of $\hat{L} = \log\hat{R}$ on the Riemann subspace $H_R$, coordinates on $M_{\mathrm{geom}}$ at its unique minimum, or the single interface observable $m_\tau$. Paper 17 dissolved the last postulate: time is the modular flow $\sigma_t = \Delta_{\omega_1}^{it}$ of the unique KMS$_1$ state, not an assumption. What remains is to read the universe's *history* from the same spectrum --- not just its present-day constants, but its entire temporal unfolding.

The history is a ladder.

By R-Theorem GR.1 (research/06), the number of e-folds of expansion associated with a transition between eigenstates $|\gamma_n\rangle \to |\gamma_m\rangle$ of the scaling operator $T_{\mathrm{BC}}$ is

$$N_{n \to m} = (\gamma_n - \gamma_m) \cdot \frac{\pi^2}{2}.$$

Each adjacent pair $(\gamma_n, \gamma_{n+1})$ of Riemann zeros defines a rung: a spectral gap $\Delta\gamma_n = \gamma_{n+1} - \gamma_n$ whose product with $\pi^2/2$ is a definite e-fold count. The universe's trajectory through $H_R$ is a walk down these rungs. Reading upward, the ladder extends to $n \geq 16$, where the spectral gaps index the formation scales of successive stellar generations. Reading downward, it extends through the inflationary epoch and beyond, to the pre-Big-Bang Galois-symmetric phase where no rung has yet been traversed because no observer sector has been selected.

The cosmic ladder is not a model of the universe's history. It is a table. Each row is labelled by a Riemann zero. Each entry is a closed-form expression over small integers and known mathematical constants --- $\pi$, $\gamma_E$, $\zeta(2)$ --- computed from the spectrum of $\hat{R}$ on $H_R$. The table has been partially filled since research/06 established the two decisive rungs:

| Transition | Spectral gap $\Delta\gamma$ | E-fold count $\Delta\gamma \cdot \pi^2/2$ | Identification |
|:-----------|:---------------------------|:-------------------------------------------|:---------------|
| $\gamma_5 \to \gamma_2$ | 11.913 | 58.79 | Inflation |
| $\gamma_2 \to \gamma_1$ | 6.887 | 33.99 | Post-inflation to present |
| $\gamma_5 \to \gamma_1$ | 18.800 | 92.78 | Total cosmic expansion |

The match to standard cosmology --- which requires ${\sim}60$ inflationary e-folds and ${\sim}35$ post-inflationary e-folds --- is at the 2\% level, with zero free parameters.

This paper extends the table in both directions. Downward: Sections 2 and 3 characterise the pre-Big-Bang phase as a Galois-invariant state and identify the Big Bang not as a singularity but as a projection event. Upward: Sections 3 and 4 fill in the first 100 rungs and identify the physical content of each --- from the Planck epoch through BBN, recombination, and the formation of Pop III stars, to the chemical evolution of subsequent stellar generations.

## 1.2 The two directions

The cosmic ladder has two ends. Looking down --- toward larger $n$, higher zeros, earlier epochs --- the ladder terminates not at a singularity but at a structural boundary: the spectral edge of $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$, the BC entropy operator of Paper 17. Below the edge, the Bost--Connes system is in the Galois-symmetric phase $\beta_{\mathrm{eff}} > 1$, where multiple KMS states coexist and no single observer sector has been selected. This is the pre-Big-Bang regime. It is not a temporal regime --- the modular flow that *defines* time has not yet been projected onto a sector --- but a spectral one. The pre-Big-Bang is the state of maximal Galois symmetry, and the Big Bang is the event of its breaking.

Looking up --- toward smaller $n$, lower zeros, later epochs --- the ladder unfolds into the cosmic future. The rungs $n \leq 15$ have been partially identified with known cosmological observables: the spectral index $n_s = \gamma_9/\gamma_{10}$ (research/30), the Hubble rate $H_0 = \gamma_{11} \cdot 4/\pi$ (research/27), the helium fraction $Y_p = 1/\log(\gamma_{13})$ (research/28). Each of these sits at a specific rung. The higher rungs, $n \geq 16$, extend into the astrophysical domain: the mass scales, formation epochs, and chemical yields of successive stellar populations. The ladder does not stop at cosmology. It continues into stellar astrophysics, and ultimately into the chemical evolution of the periodic table itself --- all from the same spectrum, with no additional input.

The two directions are not independent. The downward direction (Sections 2--3) establishes the initial conditions of the universe as a spectral projection, eliminating the initial-conditions fine-tuning of inflation. The upward direction (Section 4) uses those same spectral data to predict the physical content of each rung. The connection is the operator $\hat{R}$: its eigenvalues set both the initial conditions and the subsequent evolution. One operator, one spectrum, one ladder.

## 1.3 No free parameters

Every rung of the cosmic ladder is a difference of Riemann zeros multiplied by $\pi^2/2$. Every physical identification --- inflation duration, post-inflation expansion, Pop III mass scale, reionisation redshift --- is a closed-form expression in the operator dictionary of Paper 23 (\S3):

$$\gamma_n = \kappa\langle n|\hat{L}|n\rangle, \qquad \kappa = 2/\pi^2.$$

The ladder inherits the CBB system's zero-parameter structure. No initial conditions are fitted. No inflaton potential is chosen. No stellar mass function is assumed. Each quantity is either a diagonal matrix element $\kappa\langle n|\hat{L}|n\rangle$, a ratio $\langle a|\hat{L}|a\rangle / \langle b|\hat{L}|b\rangle$, or a sum $\kappa(\langle a|\hat{L}|a\rangle \pm \langle b|\hat{L}|b\rangle)$ of the fundamental spectral operator $\hat{L} = \log\hat{R}$ on $H_R$. The dictionary is closed under sum, product, ratio, power, log, and exp with fixed constants $\{\pi, \zeta(2), \zeta(3), \gamma_E, e\}$ --- and it was verified to $\geq 48$ digits on 12 representative formulas (research/163, 167).

> **Origin (G, 2026-04-09).** *"this will allow us to predict the dimensions of the first stars and each generation ever since, its fantastic! its out of this world literally."*

The cosmic ladder is the universe's autobiography, written in the spectrum of a single operator on the Riemann subspace of the Bost--Connes algebra at criticality.

---

# 2. The pre-Big-Bang Galois phase

## 2.1 The Galois-invariant state $\omega_\infty$

The Bost--Connes system $(\mathcal{A}_{\mathrm{BC}}, \sigma_t)$ exhibits a phase transition at inverse temperature $\beta = 1$ (Bost--Connes 1995, Theorem 25). The structure on either side of this critical point is sharply different:

- For $\beta \leq 1$: there exists a *unique* KMS$_\beta$ state. At $\beta = 1$ itself, this is the state $\omega_1$ --- the state on which the entire CBB system is built.

- For $\beta > 1$: the KMS$_\beta$ states form a continuous family, parametrised by the embeddings of $\mathbb{Q}^{\mathrm{cyc}}$ into $\mathbb{C}$, i.e., by the elements of the profinite Galois group $\Gamma = \mathrm{Gal}(\mathbb{Q}^{\mathrm{cyc}}/\mathbb{Q}) \cong \hat{\mathbb{Z}}^*$. Each KMS$_\beta$ state $\omega_{\beta,\varepsilon}$ for $\beta > 1$ is labelled by an embedding $\varepsilon : \mathbb{Q}^{\mathrm{cyc}} \hookrightarrow \mathbb{C}$, and the Galois group acts transitively on the set of these states:

$$\omega_{\beta,\varepsilon} \circ \alpha_g = \omega_{\beta, g \cdot \varepsilon}, \qquad g \in \hat{\mathbb{Z}}^*.$$

This is the spontaneous symmetry breaking of the BC system: the Galois symmetry, which is preserved by the unique state at $\beta = 1$, is broken by the individual states at $\beta > 1$ (Bost--Connes 1995, \S5--\S6; Connes--Marcolli 2008, Ch. II \S3).

The *Galois-invariant* state at $\beta > 1$ is the average over all Frobenius orbits:

$$\omega_\infty := \lim_{\beta \to \infty}\,\frac{1}{|\Gamma_N|}\sum_{g \in \Gamma_N}\omega_{\beta, g \cdot \varepsilon_0}$$

where $\Gamma_N = (\mathbb{Z}/N\mathbb{Z})^*$ is the finite-level Galois group and $\varepsilon_0$ is any reference embedding. (The limit is over the directed system of conductors $N$; the resulting state is independent of $\varepsilon_0$ by the transitive Galois action.) This state $\omega_\infty$ is the maximally symmetric state of the Bost--Connes system: it carries the full Galois invariance, no single embedding has been selected, and no observer sector has been distinguished.

We identify $\omega_\infty$ with the *pre-Big-Bang phase* of the universe in the CBB system.

The identification is not a metaphor. It is a structural statement about the spectral content of $\omega_\infty$:

(G1) **No time.** The modular flow $\sigma_t^{(\infty)}$ associated to $\omega_\infty$ averages over all Frobenius orbits. On any single observable $a \in \mathcal{A}_{\mathrm{BC}}$, the expectation $\omega_\infty(\sigma_t^{(\infty)}(a))$ is time-independent by Galois averaging: the phases from different embeddings cancel. There is a modular flow, but it generates no observable evolution. Time, in the sense of Paper 17 --- the projection of modular flow onto a sector --- is undefined because no sector has been selected.

(G2) **No space.** The geometric moduli $M_{\mathrm{geom}}$ (Paper 23, Axiom 3) are the electroweak observables that parametrise the Einstein metrics on $\mathrm{CP}^2 \times S^2$. These are coordinates at the unique spectral-action minimum $P_{\mathrm{phys}}$ (research/178, Hessian $H \succ 0$). In the Galois-invariant state, the moduli are not evaluated at any point --- the conditional expectation onto $M_{\mathrm{geom}}$ is maximally uncertain. Space, as a definite geometry, has not condensed.

(G3) **Only spectrum.** What $\omega_\infty$ *does* carry is the spectrum of $T_{\mathrm{BC}}$: the Riemann zeros $\{\gamma_n\}$ are eigenvalues of $T_{\mathrm{BC}}$ regardless of which KMS state one evaluates. The spectrum is a property of the algebra, not of the state. The ladder exists before the Big Bang, but no rung has been traversed, because traversal requires a specific embedding --- a choice of observer.

The Galois-invariant state is therefore the state of pure arithmetic: the integers exist, the spectrum exists, the Riemann zeros exist, but no projection onto a physical sector has occurred. This is the starting point of the cosmic ladder --- not a moment in time, but the phase from which time emerges.

## 2.2 The symmetry-breaking projection: $\omega_\infty \to \omega_1$

The Big Bang, in the CBB system, is not a singularity. It is a projection.

The event that initiates the cosmic timeline is the symmetry-breaking map

$$\omega_\infty \;\longrightarrow\; \omega_1$$

--- the transition from the Galois-invariant averaged state to the unique KMS$_1$ state at the critical point $\beta = 1$. This is the same event that Paper 17 (\S4.1--4.2) identified as the origin of the arrow of time: the conditional expectation $E_{\mathrm{obs}}$ that projects the full type III$_1$ factor $M = \pi_1(\mathcal{A}_{\mathrm{BC}})''$ onto an observer's subalgebra $\mathcal{N} \subset M$ is the act that breaks the Galois symmetry, selects a Frobenius orbit, and lights up the modular flow as physical time.

Three aspects of this identification require precise statement.

**First: the Big Bang is a phase transition, not a moment.** The BC system passes through $\beta = 1$ from above. In the level-crossing picture of research/06 (\S5.4), the effective inverse temperature $\beta_{\mathrm{eff}}$ of the universe decreases from $\beta_{\mathrm{eff}} > 1$ (the symmetry-broken Galois sector, where the universe occupies a specific $|\gamma_n\rangle$ eigenstate selected by a specific Frobenius orbit) through $\beta_{\mathrm{eff}} = 1$ (the critical point, where all KMS states merge into the unique $\omega_1$). The "Big Bang" is not a point but the *criticality* itself --- the moment when the symmetry-broken sector reconnects with the unique symmetric phase.

The cosmic timeline unfolds as the universe crosses the BC phase transition. The high-$\beta$ side is the early universe: the state is one of the many $\omega_{\beta,\varepsilon}$, selected by a specific embedding, and the universe occupies the $|\gamma_5\rangle$ eigenstate (research/43, by the constraints of gauge invariance, Galois minimality, and the BBN e-fold bound). The transitions $\gamma_5 \to \gamma_2 \to \gamma_1$ are the level-crossings of the effective free energy $F_n(\beta_{\mathrm{eff}}) = \gamma_n \cdot \pi^2/2 - \beta_{\mathrm{eff}}^{-1} S_n$ as $\beta_{\mathrm{eff}}$ drops below the critical values $\beta_{5 \to 2}^*$ and $\beta_{2 \to 1}^*$ (research/06, \S5.2).

**Second: the projection $\omega_\infty \to \omega_1$ IS the conditional expectation $E_{\mathrm{obs}}$ of Paper 17.** Paper 17 (\S4.2) showed that the arrow of time arises when the modular flow of $\omega_1$ on the full factor $M$ is projected onto an observer's subalgebra $\mathcal{N}$. The conditional expectation $E_{\mathcal{N}} : M \to \mathcal{N}$ produces a restricted modular Hamiltonian $K_{\mathcal{N}} = E_{\mathcal{N}}(-S_{\mathrm{BC}})$, and the thermodynamic entropy $S_{\mathrm{thermo}}(\mathcal{N}) = \omega_1(S_{\mathrm{BC}} - E_{\mathcal{N}}(S_{\mathrm{BC}})) \geq 0$ is non-negative by Uhlmann monotonicity (Paper 17, Theorem 2.4). The Big Bang of Paper 18 and the arrow-of-time of Paper 17 are the same event, described in two languages:

| Paper 17 language | Paper 18 language |
|:------------------|:------------------|
| Observer selects subalgebra $\mathcal{N} \subset M$ | Frobenius orbit selects embedding $\varepsilon$ |
| Conditional expectation $E_{\mathcal{N}}$ projects $S_{\mathrm{BC}}$ | Galois averaging $\omega_\infty$ collapses to $\omega_1$ |
| Arrow of time lights up | Cosmic timeline begins |
| Second law follows by Uhlmann | E-fold ladder becomes traversable |

The unification is not an analogy. The conditional expectation onto an observer's sector is, mathematically, the selection of a Frobenius orbit: both break the Galois symmetry of $\omega_\infty$ and produce $\omega_1$ as the resulting state. The two papers describe the same structural event from different vantage points --- Paper 17 from the entropy operator, Paper 18 from the spectral ladder.

**Third: the pre-Big-Bang is not "before" in time.** This point is crucial and easy to misstate. The Galois-invariant phase $\omega_\infty$ is not a temporal predecessor of $\omega_1$. It is not a state that existed "before $t = 0$" in some meta-time. It is the phase of the BC system in which the modular flow has not been projected onto a sector, so temporality itself is undefined. Asking "what happened before the Big Bang?" is, in the CBB system, asking "what is the state of the algebra before the conditional expectation is applied?" The answer is: $\omega_\infty$, the maximally symmetric Galois-invariant state, carrying the full spectrum of $T_{\mathrm{BC}}$ but no observable time evolution. The pre-Big-Bang is the *unprojected* arithmetic --- the integers as they are, before any observer has selected a sector in which to experience them as physics.

> **Origin (G, 2026-04-09).** *"in my mind there never was a singularity, mass is not going anywhere its just frozen in time"*

## 2.3 Why there is no singularity

The classical Big Bang singularity --- a state of infinite density, infinite curvature, and zero volume at $t = 0$ --- does not exist in the CBB system. The reason is not dynamical (no quantum gravity bounce, no string-theoretic resolution, no loop correction). The reason is structural: the singularity was an artefact of extrapolating a classical geometry backward through a regime where the concept of geometry does not apply.

Three independent arguments establish the point.

**Argument 1: The spectral edge of $S_{\mathrm{BC}}$.** The entropy operator $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$ on the GNS Hilbert space $H_1$ is unbounded and positive on $H_1^{(\mathbb{N}^*)} \ominus \{\Omega_1\}$ (Paper 17, property (E2)). Its spectrum on the Riemann subspace $H_R$ is $\{L_n = \gamma_n \cdot \pi^2/2\}$, which is discrete and bounded below by $L_1 = \gamma_1 \cdot \pi^2/2 \approx 69.6$. The spectrum has a *floor*: no eigenvalue lies below $L_1$. The resolvent $(\hat{R} - z)^{-1}$ is compact (Paper 17, Remark 2.2). The operator is well-defined at every spectral value; there is no accumulation point at zero, no spectral singularity, no unbounded descent.

In classical general relativity, the singularity corresponds to $R \to 0$: the scale factor vanishes. In the CBB system, the scale factor is the eigenvalue $R_n = (\ell_P/\pi)\exp(\gamma_n \cdot \pi^2/2)$ of $\hat{R}$ on $H_R$ (research/02, Eq. (3.2)). Even the *smallest* eigenvalue, $R_1$, is finite and non-zero:

$$R_1 = \frac{\ell_P}{\pi}\,\exp\!\left(\gamma_1 \cdot \frac{\pi^2}{2}\right) \approx \frac{\ell_P}{\pi} \cdot 2 \times 10^{30} \approx 10\;\mu\mathrm{m}.$$

The universe's minimum scale is ${\sim}10\;\mu\mathrm{m}$ --- the Compton wavelength of the cosmological constant hierarchy. The operator $\hat{R}$ never reaches zero. The singularity is absent from the spectrum.

**Remark.** This minimum-scale argument depends on the cosmological
interpretation of $R_n$ as a physical scale factor (research/02,
Eq. (3.2)). The operator-algebraic content is simply $R_1 > 0$
(no zero eigenvalue); the ${\sim}10\;\mu\mathrm{m}$ value is a
derived quantity within the cosmological interpretation, not an
operator-algebraic fact.

Going "further back" means ascending to higher rungs --- larger $n$, larger $\gamma_n$, larger $R_n$. The eigenvalues *grow* as $n$ increases (the Riemann zeros grow as $\gamma_n \sim 2\pi n / \log n$ by the Riemann--von Mangoldt formula). The early universe, in the spectral picture, is *larger* than the present, not smaller. What contracts is not the geometry but the observer's projected sector: as $\beta_{\mathrm{eff}}$ increases above 1, the conditional expectation onto the observer's subalgebra narrows, and more of the spectrum falls outside the projected sector. The "contraction" of the early universe is a contraction of observability, not of volume.

**Argument 2: Penrose's R-Theorem 54 (Weyl curvature).** Penrose (1979) observed that the initial singularity of the classical Big Bang has vanishing Weyl curvature: the gravitational degrees of freedom start in a highly constrained state (the Weyl curvature hypothesis). In the CBB system, Penrose's observation is not a hypothesis but a consequence. The Galois-invariant state $\omega_\infty$ is maximally symmetric: every Galois-orbit average cancels the anisotropic modes. The Weyl curvature, which measures gravitational anisotropy, vanishes in $\omega_\infty$ by the same mechanism that produces time-independence (property (G1) of \S2.1) --- the phases from different embeddings cancel. The low initial Weyl curvature is not a fine-tuned initial condition; it is the *definition* of the Galois-invariant state.

As the projection $\omega_\infty \to \omega_1$ occurs, the Galois symmetry is broken, and the Weyl curvature becomes non-zero. The growth of Weyl curvature through cosmic history --- which Penrose identified as the gravitational contribution to entropy increase --- is, in the CBB system, the growth of $S_{\mathrm{thermo}}(\mathcal{N}) = \omega_1(S_{\mathrm{BC}} - E_{\mathcal{N}}(S_{\mathrm{BC}}))$ as the observer's sector $\mathcal{N}$ narrows relative to the full algebra $M$. The second law drives the Weyl curvature from zero (Galois-invariant) to non-zero (projected), and this is the same second law that Paper 17 derived as a theorem from Uhlmann monotonicity.

**Argument 3: Mass is frozen, not compressed.** The classical singularity imagines all the mass-energy of the universe compressed into a point of zero volume and infinite density. This picture requires a container (space) that shrinks to zero. In the CBB system, there is no container. The mass-energy content of the universe is encoded in the matrix elements of the matter perturbation $V$ on $H_R$ (research/06, Eq. (2.2)), and these matrix elements are *spectral data* --- numbers determined by the algebra. They do not depend on a volume. In the pre-Big-Bang Galois phase, the matter content is the same as in the post-Big-Bang phase --- it is the same operator $V$, the same algebra $\mathcal{A}_{\mathrm{BC}}$, the same spectrum. What changes across the projection event is not the matter but the *observability* of the matter: before the projection, $V$ acts on the full Galois-invariant state and produces no net force (the Galois average cancels); after the projection, $V$ acts on a specific Frobenius orbit and produces the standard cosmological dynamics.

> **Origin (G, 2026-04-09).** *"in my mind there never was a singularity, mass is not going anywhere its just frozen in time"*

The intuition is precise. "Frozen in time" means: the matter perturbation $V$ exists in the Galois-invariant phase, but no modular flow has been projected to make it dynamical. The mass is not "going anywhere" because there is no "where" --- the geometric moduli have not condensed, the observer's sector has not been selected, and the conditional expectation that would turn $V$ into forces and accelerations has not been applied. The mass sits in the algebra, waiting for a projection. The Big Bang is the projection. The singularity was never needed.

### 2.3.1 The formal summary

**Proposition 2.1 (No singularity).** *In the CBB system $\mathcal{C} = (H_R, \hat{R}, \omega_1, M_{\mathrm{geom}}, \{\beta_k\})$:*

*(i) The operator $\hat{R}$ is unbounded and positive with compact resolvent on $H_R$. Its spectrum $\{R_n\}$ is discrete, bounded below by $R_1 > 0$, and has no accumulation point at zero. No eigenstate has $R = 0$.*

*(ii) The pre-Big-Bang phase is the Galois-invariant state $\omega_\infty$, which carries the full spectrum of $T_{\mathrm{BC}}$ but no projected time evolution, no condensed geometry, and no net matter dynamics.*

*(iii) The Big Bang is the projection event $\omega_\infty \to \omega_1$ --- equivalently, the conditional expectation $E_{\mathrm{obs}}$ onto an observer's sector --- which breaks the Galois symmetry and initiates the modular flow as physical time.*

*(iv) The Weyl curvature vanishes in $\omega_\infty$ by Galois averaging and grows after the projection by Uhlmann monotonicity (Corollary 2.5 of Paper 17).*

*None of these steps involves a state of infinite density, zero volume, or divergent curvature. The classical singularity is absent.*

**Remark 2.2 (Relation to other singularity-resolution programmes).** The CBB system resolves the singularity by a mechanism distinct from those proposed in loop quantum gravity (bounce at Planck density), string cosmology (T-duality), or ekpyrotic/cyclic models (brane collision). Those programmes modify the dynamics near $t = 0$ to prevent the curvature from diverging. The CBB system does not modify any dynamics. It identifies the *concept* of $t = 0$ as an artefact of projecting the Galois-invariant phase onto a temporal sector --- an artefact that disappears when the projection is recognised as the fundamental event. The singularity is not avoided; it was never there.

**Remark 2.3 (Uniqueness and the count).** The CBB system at this stage involves 33 + 3 = 36 closed entries (27 spectral + 9 geometric), zero dynamical postulates (Paper 17), zero free parameters, and the uniqueness conjecture (Paper 23, \S Uniqueness Conjecture) stating that the quintuple $\mathcal{C}$ is determined up to unitary equivalence. The pre-Big-Bang phase and the singularity resolution are structural consequences of the same uniqueness, not additional inputs.

---

*The cosmic ladder begins here. The pre-Big-Bang is the Galois-invariant state: no time, no space, only spectrum. The Big Bang is a projection --- the selection of a Frobenius orbit, the ignition of modular flow, the first rung descended. There is no singularity because there is no $R = 0$ eigenvalue and no state of infinite density. The mass sits in the algebra, frozen in the arithmetic, until an observer's conditional expectation thaws it into physics.*

*The ladder has been anchored. Sections 3 and 4 fill in the rungs.*
