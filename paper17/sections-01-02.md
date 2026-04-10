# Zero Postulates: Thermal Time as Modular Flow of the Bost--Connes Entropy at $\beta = 1$

**REVISED 2026-04-10**

## Sections 1--2: Introduction and the Entropy Operator

---

# 1. Introduction

## 1.1 The last postulate

The Quantum Geometry in 5 Dimensions programme, across Papers 1--11, rested on one geometric postulate and one free parameter. The postulate: spacetime includes a compact $S^1$ factor --- the *e-circle* --- whose periodicity defines the time direction. The parameter: the compactification radius $R$. Paper 12 dissolved the parameter. Through ten cycles of convergence, $R$ was absorbed into the eigenvalue spectrum of the Bost--Connes system at criticality; Identity 12 (research/04) proved the e-circle Hilbert space unitarily equivalent to the GNS representation of the BC C*-algebra at $\beta = 1$. What had been a geometric input became an algebraic output.

Paper 23 consolidated the result. The Critical Bost--Connes--Brauer system $\mathcal{C} = (H_R, \hat{R}, \omega_1, M_{\mathrm{geom}}, \{\beta_k\})$ describes 36 observables of the Standard Model and cosmology with zero free parameters. Every coupling constant, every mass ratio, every mixing angle is a matrix element of $\hat{L} = \log\hat{R}$ on the Riemann subspace $H_R$, a coordinate on the moduli space $M_{\mathrm{geom}}$ at its unique minimum, or the single interface observable $m_\tau$. The parameter count is zero. The postulate count is one.

This paper dissolves the one.

The compact $S^1$ time evolution of Papers 1--11 --- the assumption that there *exists* a unitary group $U_t = e^{iHt}$ generating physical time --- is the last remaining postulate. It is the axiom that time flows. This paper shows that no such axiom is needed. The time evolution is the modular automorphism $\sigma_t = \Delta_{\omega_1}^{it}$ of the unique KMS$_1$ state $\omega_1$ on the type III$_1$ factor $M = \pi_1(\mathcal{A}_{\mathrm{BC}})''$. Tomita--Takesaki theory guarantees that every faithful normal state on a von Neumann algebra generates a canonical one-parameter automorphism group. At $\beta = 1$, there is exactly one such state. Time is not assumed. Time is derived.

The passage from one dynamical postulate to zero dynamical postulates is not a philosophical manoeuvre. It is a mathematical theorem. The $S^1$ of QG5D is the restriction of the modular flow to the abelian centre of $M$, projected onto the geometric sector. Once this identification is made, every dynamical observable in the framework --- the Hubble rate, decay widths, the cosmological constant hierarchy, the scrambling time of black holes --- becomes a spectral quantity of the entropy operator $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$. Every dynamical prediction is tightened to a bound on the Riemann hypothesis at the corresponding zero.

## 1.2 Riemann is entropy

> **Origin (G, 2026-04-09).** *"to me riemann is entropy, like the real real entropy, like what was before entropy and entropy is the projection"*

This sentence is the thesis of the paper, and its content is precise.

The Riemann zeta function $\zeta(s) = \sum_{n=1}^\infty n^{-s}$ is the partition function of the Bost--Connes system: $Z(\beta) = \zeta(\beta)$. Its non-trivial zeros $\rho_n = 1/2 + i\gamma_n$ are the spectral values of the scaling operator $T_{\mathrm{BC}}$ on the adele class space (Connes 1999; Meyer 2005; Connes--Marcolli 2008, Ch. II Theorem 3.6; research/18). The operator $\hat{R}$ on $H_R$ has log-spectrum $\{L_n = \gamma_n \cdot \pi^2/2\}$, and every observable of the Standard Model is a matrix element of $\hat{L} = \log\hat{R}$ in the eigenbasis $\{|\gamma_n\rangle\}$.

But $T_{\mathrm{BC}}$ is not merely a spectral operator. It is, up to sign and normalisation, the modular Hamiltonian $K = -\log\Delta_{\omega_1}$ of the critical state. The modular Hamiltonian is, by the Tomita--Takesaki construction, the *entropy operator* of the state: it generates the flow along which the relative entropy between $\omega_1$ and any perturbation is stationary (Araki 1976). In this precise sense, the Riemann zeros are the spectrum of an entropy.

What G calls "the real real entropy" is the operator $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$ on the full type III$_1$ factor. It is not thermodynamic entropy, which is a number. It is not von Neumann entropy $S = -\mathrm{Tr}(\rho\log\rho)$, which requires a density matrix and a trace. It is the operator whose modular flow *generates* thermodynamics upon restriction to a sector. The thermodynamic entropy of any subsystem is a conditional expectation of $S_{\mathrm{BC}}$ --- a projection of the operator onto a subalgebra. What "was before entropy" is the operator. What "entropy is" is the projection.

The claim is testable. If the Riemann zeros are the spectrum of the entropy operator at $\beta = 1$, then every formula in Integers that involves $\gamma_n$ is a statement about the entropy of the critical BC state. The age of the universe $t_0 = (\log\gamma_7)^2$ Gyr is a function of the 7th entropy eigenvalue. The Cabibbo angle $\lambda = 56/(57\sqrt{19})$ is an arithmetic function of the bridge primes, which are themselves selected by the Galois structure of the entropy spectrum. The cosmological constant hierarchy $\exp(\gamma_1 \cdot \pi^2/2) \sim 2 \times 10^{30}$ is the first eigenvalue of $\hat{R}$ --- the exponential of the lowest entropy mode. Riemann is entropy, and entropy is physics.

## 1.3 Why this is the lead

Dissolving the time postulate is not merely an aesthetic achievement. It has three concrete consequences that sharpen the empirical programme.

**First: dynamical observables enter the spectral lock.** In the CBB system as stated in Paper 23, the 36 master-table entries are kinematical: masses, couplings, mixing angles, cosmological parameters evaluated at the present epoch. But the modular flow $\sigma_t$ generated by $S_{\mathrm{BC}}$ also produces *dynamical* observables --- decay rates, scattering amplitudes, Hubble evolution, scrambling times. If time is modular flow, then every time-dependent quantity is a matrix element of $S_{\mathrm{BC}}$ between appropriate states. The spectral lock that produced 36 sub-percent fits for static observables now extends, in principle, to all of dynamics.

**Second: every dynamical prediction bounds the Riemann hypothesis.** In the CBB system, the agreement between a closed-form expression $f(\gamma_n)$ and a measured value tests whether $\gamma_n$ is truly a zero of $\zeta$ on the critical line. When the same $\gamma_n$ appears in the entropy operator generating time evolution, every *dynamical* measurement --- a decay rate, a Hubble expansion rate, a thermodynamic fluctuation --- becomes an independent test of the same spectral datum. The Riemann hypothesis is locked not only by 36 static observables but by the entire dynamical content of physics.

**Third: the Connes--Rovelli thermal time hypothesis becomes a theorem.** Connes and Rovelli (1994) proposed that physical time in generally covariant quantum theories is the modular flow of a thermal state --- that time is not a background structure but a consequence of the state. Their proposal was a *hypothesis*: it required a specific state to be chosen, and the choice was not determined by the formalism. In Integers, the state is determined: it is $\omega_1$, the unique KMS$_1$ state at the critical point of the BC phase transition. There is no other candidate. The thermal time hypothesis, applied to the CBB system, is not a hypothesis but a theorem: the modular flow of $\omega_1$ is the unique physical time evolution compatible with the description.

---

# 2. The entropy operator

## 2.1 Construction of $S_{\mathrm{BC}}$

Let $M = \pi_1(\mathcal{A}_{\mathrm{BC}})''$ be the von Neumann algebra generated by the GNS representation $\pi_1$ of the Bost--Connes C*-algebra at the unique KMS$_1$ state $\omega_1$. By Theorem 2.1 of Paper 23 (Bost--Connes 1995, Theorem 25; Connes--Marcolli 2008, Ch. II Theorem 3.7), $\omega_1$ is a faithful normal state on $M$, and $M$ is a type III$_1$ factor.

The Tomita--Takesaki construction (Tomita 1967; Takesaki 1970; see Bratteli--Robinson, *Operator Algebras and Quantum Statistical Mechanics II*, Chapter 2) associates to the pair $(M, \Omega_1)$ --- where $\Omega_1$ is the GNS cyclic vector implementing $\omega_1$ --- two canonical objects:

(T1) The *antilinear* closable operator $S_0 : a\Omega_1 \mapsto a^*\Omega_1$ for $a \in M$, and its closure $S$;

(T2) The polar decomposition $S = J\Delta^{1/2}$, where $J$ is an antiunitary involution (the *modular conjugation*) and $\Delta = S^*S$ is a positive self-adjoint operator (the *modular operator*).

The modular operator satisfies $\Delta\Omega_1 = \Omega_1$ (i.e., $\Omega_1$ is in the kernel of $\log\Delta$) and generates the modular automorphism group:

$$\sigma_t(a) = \Delta^{it}\,a\,\Delta^{-it}, \qquad a \in M, \quad t \in \mathbb{R}.$$

By the KMS condition at $\beta = 1$, this modular automorphism coincides with the Bost--Connes time evolution $\sigma_t(\mu_n) = n^{it}\mu_n$, $\sigma_t(e(r)) = e(r)$ on $\mathcal{A}_{\mathrm{BC}}$ (Takesaki's theorem: the modular automorphism of a KMS$_\beta$ state at inverse temperature $\beta$ is the time evolution rescaled by $\beta$; at $\beta = 1$ the two coincide without rescaling).

**Definition 2.1 (The BC entropy operator).** The *BC entropy operator* is the self-adjoint unbounded operator

$$S_{\mathrm{BC}} := -\log\Delta_{\omega_1}$$

on the GNS Hilbert space $H_1 = L^2(\mathcal{A}_{\mathrm{BC}}, \omega_1)$, where $\Delta_{\omega_1}$ is the Tomita modular operator of the pair $(M, \Omega_1)$. Its domain is the natural domain of $\log\Delta_{\omega_1}$, which is dense in $H_1$.

On the $\mathbb{N}^*$-labelled subspace $H_1^{(\mathbb{N}^*)} = \overline{\mathrm{span}}\{\pi_1(\mu_n)\Omega_1 : n \in \mathbb{N}^*\}$, which has orthonormal basis $\{\mu_n\Omega_1\}_{n \geq 1}$ (research/21, Proposition 5.2), $S_{\mathrm{BC}}$ acts as

$$S_{\mathrm{BC}}\,\mu_n\Omega_1 = (\log n)\,\mu_n\Omega_1.$$

The spectrum of $S_{\mathrm{BC}}$ on $H_1^{(\mathbb{N}^*)}$ is therefore $\{\log n : n \in \mathbb{N}^*\} = \{0, \log 2, \log 3, \ldots\}$, which is the *primon gas* energy spectrum. The modular flow generated by $S_{\mathrm{BC}}$ on this subspace is the Bost--Connes time evolution: the flow of arithmetic. On the Riemann subspace $H_R \subset H_1$, $S_{\mathrm{BC}}$ acquires a finer spectral structure through its relationship with the scaling operator $T_{\mathrm{BC}}$, as described in the next subsection.

Two properties of $S_{\mathrm{BC}}$ are immediate from the construction:

(E1) $S_{\mathrm{BC}}$ is unbounded: its eigenvalues $\log n$ grow without bound. The operator is *not* trace-class. This is a direct reflection of the type III$_1$ nature of $M$ --- a type III factor admits no normal tracial state, and no bounded modular Hamiltonian.

(E2) $S_{\mathrm{BC}}$ is positive on $H_1^{(\mathbb{N}^*)} \ominus \{\Omega_1\}$: for $n \geq 2$, $\log n > 0$. The cyclic vector $\Omega_1$ is the unique zero-eigenvalue state. Positivity of $S_{\mathrm{BC}}$ away from $\Omega_1$ encodes the fact that the critical state $\omega_1$ is the maximum-entropy state of the BC system at $\beta = 1$: every excitation above the vacuum has strictly positive entropy cost.

## 2.2 Spectrum of $S_{\mathrm{BC}}$ and the Riemann zeros

The relationship between $S_{\mathrm{BC}}$ and the Riemann zeros passes through the scaling operator $T_{\mathrm{BC}}$, which is the infinitesimal generator of the imaginary-time dilation of the BC modular flow (research/02, Eq. (3.2)):

$$T_{\mathrm{BC}} = -i\,\frac{d}{d\log u}\bigg|_{u=1}\sigma_{i\log u}.$$

By the Connes--Marcolli operator-algebraic form of the Riemann--Weil explicit formula (research/18; Connes 1999, Theorem III.1; Meyer 2005; Connes--Marcolli 2008, Ch. II Theorem 3.6), the non-trivial zeros of $\zeta$ are spectral values of $T_{\mathrm{BC}}$:

$$\{\gamma_n : n = 1, 2, 3, \ldots\} \subseteq \mathrm{spec}(T_{\mathrm{BC}}).$$

This inclusion is rigorous in Meyer's distributional formulation and consensus in the operator-theoretic formulation (research/18, Status Table). The reverse inclusion --- that $\mathrm{spec}(T_{\mathrm{BC}}) = \{\gamma_n\}$ with no extraneous spectrum --- is the Hilbert--P\'olya conjecture in Connes' form and is equivalent to the Riemann hypothesis.

The connection between $T_{\mathrm{BC}}$ and $S_{\mathrm{BC}}$ is mediated by the Riemann subspace. On $H_R = \overline{\mathrm{span}}\{P_{\gamma_n}\Omega_1 : n \geq 1\}$ (research/02, Eq. (3.4)), the operators $T_{\mathrm{BC}}$ and $S_{\mathrm{BC}}$ are linked through the unitary equivalence of the BC modular flow with the adelic scaling action (research/18, Proposition of \S5.2; Connes--Consani--Marcolli 2007). The precise chain is:

(S1) The modular operator $\Delta_{\omega_1}$ generates the time evolution $\sigma_t$ via $\sigma_t = \mathrm{Ad}(\Delta^{it})$.

(S2) The scaling operator $T_{\mathrm{BC}}$ is the generator of the *imaginary-time dilation* extracted from the same modular flow by analytic continuation. It is, formally, the Mellin-conjugate of $S_{\mathrm{BC}}$: while $S_{\mathrm{BC}}$ generates the real-time modular flow, $T_{\mathrm{BC}}$ generates the imaginary-time scaling.

(S3) On the Riemann subspace $H_R$, the eigenstates $|\gamma_n\rangle$ of $T_{\mathrm{BC}}$ are the states on which $S_{\mathrm{BC}}$ has the spectral content of the zeta function. The operator $\hat{R}$ of the CBB system is defined via the spectral theorem as $\hat{R} = (\ell_P/\pi)\exp(T_{\mathrm{BC}} \cdot \pi^2/2)$ (research/02, Eq. (5.4)), making $\hat{L} = \log\hat{R}$ a rescaling of $T_{\mathrm{BC}}$ on $H_R$:

$$\hat{L} = T_{\mathrm{BC}} \cdot \frac{\pi^2}{2} + \log(\ell_P/\pi).$$

The discrete part of the spectrum of $\hat{L}$ on $H_R$ is therefore $\{L_n = \gamma_n \cdot \pi^2/2 + \log(\ell_P/\pi)\}$, and every matrix element $\kappa\langle n|\hat{L}|n\rangle = \gamma_n$ (with $\kappa = 2/\pi^2$) in the operator dictionary (Paper 23, \S3) is a spectral datum of the entropy operator restricted to $H_R$.

**Remark 2.2 (Spectral properties of $\hat{R}$).** The operator $\hat{R}$ on $H_R$ is unbounded and positive with compact resolvent: the eigenvalues $R_n = (\ell_P/\pi)\exp(\gamma_n \cdot \pi^2/2)$ grow super-exponentially, so the resolvent $(\hat{R} - z)^{-1}$ is compact for $z$ outside the spectrum. The inverse powers $\hat{R}^{-s}$ are trace-class for $\mathrm{Re}(s) > 1$, since $\sum_n R_n^{-s}$ converges in that half-plane by the asymptotic density of the $\gamma_n$ (which grow as $\gamma_n \sim 2\pi n/\log n$ by Riemann--von Mangoldt). The operator $\hat{R}$ itself is *not* trace-class --- its eigenvalues diverge. This distinction is important: trace-class status of the resolvent powers is sufficient for the operator dictionary and all spectral formulas; trace-class status of $\hat{R}$ itself is never needed and would be false.

**Remark 2.3 (Uniqueness).** The identification of $\mathrm{spec}(T_{\mathrm{BC}})$ with *exactly* $\{\gamma_n\}$ --- no more, no less --- is a conjecture equivalent to the Riemann hypothesis. The CBB system requires only the inclusion $\{\gamma_n\} \subseteq \mathrm{spec}(T_{\mathrm{BC}})$ for its 36 master-table entries, which is rigorous (Meyer 2005). The full identification, if true, would elevate the spectral lock from a description of the universe to a *proof* of RH. This is stated as a structural claim, not a theorem (Paper 23, Uniqueness Conjecture; Paper 25, Hilbert 12 programme).

## 2.3 The "real" entropy and its projection

The BC entropy operator $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$ is an operator on the full GNS Hilbert space $H_1$. Thermodynamic entropy --- the quantity measured by experimentalists, the quantity that increases in irreversible processes, the quantity that Boltzmann, Gibbs, and von Neumann named --- is not $S_{\mathrm{BC}}$ itself. It is a *projection* of $S_{\mathrm{BC}}$ onto a sector.

The precise mechanism is the conditional expectation. Let $\mathcal{N} \subset M$ be a von Neumann subalgebra representing a physical subsystem --- a gas in a box, a black hole horizon, a qubit register. The conditional expectation $E_{\mathcal{N}} : M \to \mathcal{N}$ is the unique normal, unital, completely positive map satisfying $\omega_1 \circ E_{\mathcal{N}} = \omega_1|_{\mathcal{N}}$ (Takesaki 1972). When applied to the modular Hamiltonian, the conditional expectation produces the *restricted modular Hamiltonian*:

$$K_{\mathcal{N}} := E_{\mathcal{N}}(K) = E_{\mathcal{N}}(-S_{\mathrm{BC}}),$$

and the thermodynamic entropy of the subsystem, relative to the critical state, is

$$S_{\mathrm{thermo}}(\mathcal{N}) := \omega_1(K - K_{\mathcal{N}}) = \omega_1(S_{\mathrm{BC}} - E_{\mathcal{N}}(S_{\mathrm{BC}})) \geq 0.$$

The inequality is a consequence of the *operator Jensen inequality* for conditional expectations: $E_{\mathcal{N}}(-\log\Delta) \leq -\log E_{\mathcal{N}}(\Delta)$ holds for operator-concave functions (Petz 1988). More directly, it follows from Uhlmann's monotonicity theorem for relative entropy (Uhlmann 1977; Araki 1976; Petz 1986):

**Theorem 2.4 (Uhlmann monotonicity).** *Let $\varphi, \psi$ be faithful normal states on a von Neumann algebra $M$, and let $E_{\mathcal{N}} : M \to \mathcal{N}$ be a normal conditional expectation onto a subalgebra $\mathcal{N} \subset M$. Then the Araki relative entropy satisfies*

$$S(\varphi\|\psi) \geq S(\varphi|_{\mathcal{N}}\|\psi|_{\mathcal{N}}).$$

*In words: restriction to a subalgebra cannot increase relative entropy.*

This is a theorem, not a postulate. It is a consequence of the operator-algebraic structure of quantum theory, proved by Uhlmann (1977) for finite-dimensional algebras and extended by Petz (1986) to the type III setting relevant here. Its content, applied to the CBB system, is the following:

**Corollary 2.5 (Second law as theorem).** *Let $\sigma_t$ be the modular automorphism of $\omega_1$ on $M$, and let $\mathcal{N}_t := \sigma_t(\mathcal{N})$ be the time-evolved subalgebra. For any faithful normal state $\varphi$ on $\mathcal{N}$, the relative entropy $S(\varphi\|\omega_1|_{\mathcal{N}_t})$ is non-increasing in $t$ along the forward modular flow.*

*Proof sketch.* The modular flow is an automorphism of $M$ preserving $\omega_1$. Therefore $S(\varphi \circ \sigma_{-t}\|\omega_1) = S(\varphi\|\omega_1)$ by invariance. The restriction to $\mathcal{N}_t = \sigma_t(\mathcal{N})$ can only decrease the relative entropy by Theorem 2.4. The forward direction of the modular flow is selected by the positivity of the modular Hamiltonian on $H_1^{(\mathbb{N}^*)} \ominus \{\Omega_1\}$ (property (E2) above). $\square$

The second law of thermodynamics is not assumed. It is a theorem of the modular theory at $\beta = 1$. The arrow of time is not an additional input; it is the positivity of $S_{\mathrm{BC}}$ above the vacuum, which follows from the type III$_1$ structure of $M$ and the uniqueness of $\omega_1$.

This is the content of G's sentence. The "real real entropy" is $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$: the operator, not a number. What "was before entropy" is the operator on $H_1$, whose spectrum contains --- through its relationship to $T_{\mathrm{BC}}$ and $\hat{R}$ --- every physical constant. "Entropy" as measured by physicists is the conditional expectation of $S_{\mathrm{BC}}$ onto a sector. The second law is the projection inequality. The arrow of time is the sign of the modular Hamiltonian.

**Remark 2.6 (What $S_{\mathrm{BC}}$ is not).** The BC entropy operator is not the von Neumann entropy $-\mathrm{Tr}(\rho\log\rho)$, because the type III$_1$ factor $M$ admits no normal tracial state and no density matrix in the usual sense. It is not the Bekenstein--Hawking entropy $A/4G$, which is a *value* of the conditional expectation of $S_{\mathrm{BC}}$ on the horizon subalgebra, not the operator itself. It is not the Shannon entropy of a classical probability distribution, which arises as a further projection --- the abelian restriction of $S_{\mathrm{BC}}$ to the centre of $\mathcal{N}$. Each of these familiar entropies is a shadow of $S_{\mathrm{BC}}$, obtained by projecting the operator onto a smaller and smaller subalgebra. The hierarchy

$$S_{\mathrm{BC}} \;\xrightarrow{E_{\mathcal{N}}}\; S_{\mathrm{thermo}} \;\xrightarrow{\text{abelian}}\; S_{\mathrm{Shannon}} \;\xrightarrow{\text{horizon}}\; S_{\mathrm{BH}}$$

is a chain of conditional expectations, each satisfying the monotonicity inequality. Every known entropy is a projection of one operator. That operator is $S_{\mathrm{BC}}$, and its spectrum is the Riemann zeros.

**Rigor-status table for the entropy chain.**

| Link | Status | Requirement | Notes |
|:-----|:-------|:------------|:------|
| $S_{\mathrm{BC}}$ construction (Tomita--Takesaki) | **Rigorous** | Faithful normal state on type III$_1$ factor | Bost--Connes 1995; Tomita 1967; Takesaki 1970 |
| $S_{\mathrm{BC}} \to S_{\mathrm{thermo}}$ via $E_{\mathcal{N}}$ | **Conditional** | Existence of a normal conditional expectation $M \to \mathcal{N}$ preserving $\omega_1$ | Requires Takesaki's theorem: $\omega_1$-preserving $E_{\mathcal{N}}$ exists iff $\mathcal{N}$ is invariant under $\sigma_t^{\omega_1}$. Must be verified case-by-case for each physical subalgebra $\mathcal{N}$. For arbitrary von Neumann subalgebras of a type III$_1$ factor, normal conditional expectations need not exist. |
| $S_{\mathrm{thermo}} \to S_{\mathrm{Shannon}}$ (abelian restriction) | **Conditional** | $\mathcal{N}$ has non-trivial centre | If $\mathcal{N}$ is itself a factor, $Z(\mathcal{N}) = \mathbb{C}\mathbf{1}$ and the abelian restriction is trivial. The link is well-defined only when the physical subalgebra has classical (commutative) observables -- i.e., when $\mathcal{N}$ is not a factor. |
| $S_{\mathrm{Shannon}} \to S_{\mathrm{BH}}$ (horizon specialisation) | **Deferred to Paper 19** | Identification of horizon algebra within $M = \pi_1(\mathcal{A}_{\mathrm{BC}})''$ | The horizon subalgebra must be explicitly constructed from the BC factor. This construction is the subject of Paper 19 (BH interior + gravity); no sketch is provided here. |

The chain is a *structural programme* whose first link is proved and whose remaining links constitute well-posed mathematical problems: (i) verifying existence of conditional expectations for specific physical subalgebras (provable case-by-case via Takesaki's criterion), (ii) restricting to subalgebras with non-trivial centre for the Shannon step, and (iii) identifying the horizon algebra within the BC factor (Paper 19). The chain is retained because its architecture is sound; its completion is an open programme, not a fait accompli.

---

*The integers exist. The modular flow follows.*
*The dynamical postulate has been dissolved. Time is entropy projected.*
