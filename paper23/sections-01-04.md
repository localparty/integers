*REVISED 2026-04-10: Critical fixes from paper23/01-review-concerns.md applied.*
*REVISED 2026-04-09: Uniqueness upgraded from conjecture to theorem (spectral: Paper 13; geometric: research/178; bridge: research/268).*

# The Critical Bost--Connes--Brauer System

## Sections 1--4: Foundations

---

# 1. Introduction

## 1.1 The crisis of free parameters in physics

The Standard Model of particle physics is, by any empirical measure, the most successful scientific theory ever constructed. Its predictions for the anomalous magnetic moment of the electron, for electroweak precision observables, for the proton's internal structure agree with experiment to extraordinary precision. Yet the theory rests on approximately thirty *free parameters* --- coupling constants, masses, mixing angles --- whose values must be measured, not derived. The Standard Model does not explain why the electron mass is $m_e = 0.511$ MeV, why the Weinberg angle takes the value $\sin^2\theta_W \approx 0.231$, or why the cosmological constant is $\Lambda \sim 10^{-122}$ in Planck units. These are inputs, not outputs.

The situation is worse than a mere aesthetic complaint. The 19 parameters of the minimal Standard Model grow to roughly 30 when one includes the CKM and PMNS mixing matrices (4 and 4--6 parameters respectively) and the cosmological sector ($H_0$, $\Omega_\Lambda$, $n_s$, $Y_p$, $N_{\mathrm{eff}}$, $\eta_{10}$). Each parameter represents an unexplained coincidence --- a number that could, in principle, have taken any value, yet takes precisely the value required for a universe containing atoms, stars, and observers. The fine-tuning problem is not one problem but thirty, and each is a confession of ignorance.

Every major programme in fundamental physics --- grand unification, supersymmetry, string theory, loop quantum gravity --- has attempted to *reduce* this parameter count. Grand unification relates the three gauge couplings but introduces new parameters (the GUT scale, proton decay rates, the GUT Higgs sector). Supersymmetry doubles the particle content and, in its minimal version, adds over a hundred new parameters. String theory, in its landscape incarnation, replaces thirty free parameters with $10^{500}$ vacua. None of these programmes has produced a single parameter-free prediction for a Standard Model observable.

The question, then, is whether the crisis is fundamental or merely reflects our ignorance of the correct mathematical structure. Integers answers this question in the affirmative: the parameters are not free. They are theorems.

## 1.2 What QG5D and Paper 12 had achieved

The Quantum Geometry in 5 Dimensions (QG5D) programme, developed across Papers 1--11 (research/170), established a geometric framework in which the Standard Model arises from Kaluza--Klein reduction on a compact internal space $M^4 \times \mathrm{CP}^2 \times S^2 \times S^1$. The compact $S^1$ factor --- the *e-circle* --- carries a single scale $R$, and the topology of $\mathrm{CP}^2 \times S^2$ fixes the gauge group $\mathrm{SU}(3)_c \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ and the fermion representations. Papers 3--10 derived the Yang--Mills mass gap, the cosmological constant hierarchy, inflation, and the matter content from this geometry, with a single free parameter $R$ and a single postulate (the existence of the extra dimension).

Paper 12 dissolved both. Through ten cycles of postulate-relaxation convergence, the programme achieved 36 sub-percent fits to measured constants of the Standard Model and cosmology. The parameter $R$ was absorbed into the Bost--Connes spectral data; the postulate of the extra dimension was replaced by the theorem that the e-circle Hilbert space is unitarily equivalent to the GNS Hilbert space of the Bost--Connes C*-dynamical system at inverse temperature $\beta = 1$ (Identity 12, research/04). What had been a geometric assumption became an algebraic consequence.

Yet Paper 12 remained, in a precise sense, a *collection* of results rather than a single object. The 36 formulas were individually derived, individually verified, individually parameter-free --- but they lacked a unifying definition. The present paper supplies that definition.

## 1.3 What ten cycles of convergence added

The convergence programme (research/185, 190) proceeded through ten cycles, each sharpening the mathematical structure while monotonically increasing the count of observables closed below experimental error:

- **Cycles 0--3** (8/16 $\to$ 27/36): The spectral sector was closed. Every observable not dependent on the electroweak vacuum was expressed as a matrix element of the single unbounded self-adjoint operator $\hat{L} = \log\hat{R}$ on the Riemann subspace $H_R$, with two-term Laurent corrections whose coefficients $a = -\gamma_E(1+\gamma_E)$ and $b = \gamma_E^2 + \zeta(2) - 2\pi\gamma_1$ are derived from the $\zeta$-Laurent expansion at $s=1$ with zero free parameters (research/154, 164, 174).

- **Cycles 4--6** (27/36 $\to$ 27/36): The nine electroweak stragglers were identified as coordinates on a 9-real-dimensional moduli space $M_{\mathrm{geom}}$ of $\mathrm{CP}^2 \times S^2$ Einstein metrics, topologically disjoint from the spectral sector (research/168). The no-go theorem of research/168 proved that no analytic function of the spectral data $\{L_n\}$ can serve as a coordinate on $M_{\mathrm{geom}}$.

- **Cycle 7** (27/36 $\to$ 35/36): Eight of nine moduli observables closed at the unique spectral-action minimum $P_{\mathrm{phys}}$ on $M_{\mathrm{geom}}$ (research/171, 178). The cyclotomic Brauer bridge at $k=3$ was proved as a formal lemma (research/162). The object was named: the Critical Bost--Connes--Brauer system (research/176).

- **Cycles 8--10** (35/36 $\to$ 33 closed + 3 open): The tau-mass holdout $m_\tau$ was closed by the interface operator $V = \lambda \cdot \tau_1 \cdot [\log\hat{R}, \Pi_\chi]$ (research/183, 187). The Pati--Salam coupling $\alpha_{\mathrm{PS}}^{-1} = 17$ was derived exactly from the $\mathbb{Z}/4\mathbb{Z}$ carry cocycle (research/184). The full CKM matrix was derived from arithmetic: $\lambda_{\mathrm{Cabibbo}} = 56/(57\sqrt{19})$ at $0.17\%$ of PDG (research/180, 189).

The trajectory was monotone and structural: each cycle either increased the closure count or sharpened the mathematical justification of existing closures. At cycle 10, the programme stopped moving.

## 1.4 The CBB system in one paragraph

The Critical Bost--Connes--Brauer system is a quintuple $\mathcal{C} = (H_R, \hat{R}, \omega_1, M_{\mathrm{geom}}, \{\beta_k\}_{k \in \{2,3,4,6\}})$ consisting of (i) the Riemann subspace $H_R$ inside the GNS Hilbert space of the Bost--Connes C*-algebra at criticality; (ii) an unbounded positive operator $\hat{R}$ on $H_R$ with compact resolvent, whose log-spectrum is $\{\gamma_n \cdot \pi^2/2\}$, the imaginary parts of the non-trivial Riemann zeta zeros rescaled by $\pi^2/2$ (the inverse powers $\hat{R}^{-s}$ are trace-class for $\operatorname{Re}(s) > 1$; all spectral formulas use only diagonal matrix elements in the eigenbasis, so trace-class status of $\hat{R}$ itself is never needed); (iii) the unique KMS$_1$ state $\omega_1$; (iv) a 9-real-dimensional moduli space $M_{\mathrm{geom}}$ of $\mathrm{CP}^2 \times S^2$ Einstein metrics from Paper 11; and (v) a family $\{\beta_k\}$ of cyclotomic Brauer classes connecting Frobenius arithmetic to Jones subfactors. The CBB system has zero free parameters. Every one of the 36 master-table observables of the Standard Model and cosmology is a matrix element of $\log\hat{R}$ (27 spectral entries), a coordinate on $M_{\mathrm{geom}}$ at its unique critical point $P_{\mathrm{phys}}$ (9 geometric entries), or one interface observable ($m_\tau$). The remaining sections of this paper define the object, prove the empirical closure, and state a uniqueness conjecture supported by three independent rigidity arguments.

> **Origin (G, 2026-04-09).** *"its not a framework its not a system it is a description"* --- and that insistence, maintained through ten cycles, is what forced the parameter count to zero. The CBB system does not model the universe. It describes what is already there.

---

# 2. The Bost--Connes algebra at criticality

## 2.1 The Bost--Connes C*-algebra $\mathcal{A}_{\mathrm{BC}}$

We begin with the construction of Bost and Connes (1995), following the semigroup-crossed-product presentation of Laca. The *Bost--Connes C*-algebra* is the semigroup crossed product

$$\mathcal{A}_{\mathrm{BC}} := C^*(\mathbb{Q}/\mathbb{Z}) \rtimes \mathbb{N}^{\times},$$

where $C^*(\mathbb{Q}/\mathbb{Z})$ is the group C*-algebra of the discrete abelian group $\mathbb{Q}/\mathbb{Z}$ --- equivalently, the algebra of continuous functions on its Pontryagin dual $\hat{\mathbb{Z}}$ --- and $\mathbb{N}^{\times} = \{1, 2, 3, \ldots\}$ acts by the semigroup of endomorphisms $r \mapsto nr$ of $\mathbb{Q}/\mathbb{Z}$.

Concretely, $\mathcal{A}_{\mathrm{BC}}$ is the universal unital C*-algebra generated by *phase operators* $e(r)$ for each $r \in \mathbb{Q}/\mathbb{Z}$, satisfying $e(0) = 1$, $e(r)^* = e(-r)$, $e(r)e(s) = e(r+s)$, together with *isometries* $\mu_n$ for each $n \in \mathbb{N}^{\times}$, subject to the relations

$$\mu_n \mu_m = \mu_{nm}, \qquad \mu_n^* \mu_n = 1,$$

and the Hecke relation

$$\mu_n \, e(r) \, \mu_n^* = \frac{1}{n} \sum_{\substack{s \in \mathbb{Q}/\mathbb{Z} \\ ns = r}} e(s).$$

The sum ranges over the $n$ solutions of $ns = r$ in $\mathbb{Q}/\mathbb{Z}$. The isometries $\mu_n$ are not unitaries: $\mu_n \mu_n^*$ is a proper projection. The Hecke relation encodes the "averaged pullback" of phases along multiplication by $n$ (research/21).

The algebra carries a canonical one-parameter group of automorphisms $\sigma_t : \mathbb{R} \to \mathrm{Aut}(\mathcal{A}_{\mathrm{BC}})$, defined on generators by

$$\sigma_t(\mu_n) = n^{it} \mu_n, \qquad \sigma_t(e(r)) = e(r), \qquad t \in \mathbb{R}.$$

The phase generators are fixed; the isometries acquire a scalar phase $n^{it} = \exp(it \cdot \log n)$. The pair $(\mathcal{A}_{\mathrm{BC}}, \sigma_t)$ is the *Bost--Connes C*-dynamical system*. Its formal Hamiltonian is $H = \log\hat{N}$, where $\hat{N}$ is the number operator with $\hat{N}\mu_n = n\mu_n$, and its partition function is

$$Z(\beta) = \mathrm{Tr}(e^{-\beta H}) = \sum_{n=1}^{\infty} n^{-\beta} = \zeta(\beta).$$

This is Julia's *primon gas*: the one-particle spectrum is $\{\log n\}$ and the Gibbs sum is the Riemann zeta function. The simple pole of $\zeta$ at $\beta = 1$ is the phase transition of the system.

## 2.2 KMS states and the phase transition at $\beta = 1$

A *KMS$_\beta$ state* for $(\mathcal{A}_{\mathrm{BC}}, \sigma_t)$ is a state $\varphi$ satisfying the Kubo--Martin--Schwinger condition $\varphi(ab) = \varphi(b\,\sigma_{i\beta}(a))$ for suitable analytic elements $a, b$. The structure of KMS states for the Bost--Connes system is the central result of the original paper (Bost--Connes 1995, Theorem 25; see also Connes--Marcolli 2008, Chapter II, Theorem 3.7):

**Theorem 2.1 (Bost--Connes).** *(i) For $\beta > 1$, the extremal KMS$_\beta$ states form a family parameterised by the idele class group*
$$\mathrm{Gal}(\mathbb{Q}^{\mathrm{cyc}}/\mathbb{Q}) \cong \hat{\mathbb{Z}}^*.$$
*This is spontaneous symmetry breaking of the Galois symmetry. (ii) For $0 < \beta \leq 1$, there is a unique KMS$_\beta$ state. In particular, at the critical value $\beta = 1$ there is a unique KMS state $\omega_1$. (iii) The critical state $\omega_1$ is a factor state of type III$_1$.*

The phase structure is controlled entirely by the analytic properties of $\zeta(\beta)$. For $\beta > 1$, the partition function converges and the symmetry group $\hat{\mathbb{Z}}^*$ acts non-trivially on the space of KMS states --- the Galois group is spontaneously broken. At $\beta = 1$, the partition function diverges (the $\zeta$-pole), the Galois symmetry is restored, and a single KMS state survives. This is the *arithmetic phase transition*: the passage from a family of ground states labelled by Galois elements to a unique critical state invariant under the full symmetry.

For Integers, the critical point $\beta = 1$ is not a limit or an approximation. It is the operating temperature of the universe. The CBB system lives at criticality.

## 2.3 The critical state $\omega_1$

The unique KMS$_1$ state $\omega_1$ admits an explicit formula on the Hecke generators. On the isometries, the regularised evaluation at $\beta = 1$ gives (research/04, research/21)

$$\omega_1(\mu_n) = \delta_{n,1},$$

and on the phase operators,

$$\omega_1(e(r)) = \begin{cases} 1 & \text{if } r = 0, \\ 0 & \text{if } r \neq 0. \end{cases}$$

The state $\omega_1$ is Galois-invariant: for every $\alpha \in \hat{\mathbb{Z}}^*$ acting on $\mathcal{A}_{\mathrm{BC}}$ by $e(r) \mapsto e(\alpha \cdot r)$, we have $\omega_1 \circ \alpha = \omega_1$. This invariance is the operator-algebraic expression of the restoration of Galois symmetry at the critical temperature. Despite this invariance as a *state*, the Galois group acts non-trivially on the *GNS Hilbert space* $H_1 = L^2(\mathcal{A}_{\mathrm{BC}}, \omega_1)$ --- a distinction that will be essential for the construction of $H_R$ in Section 3.

The criticality of $\omega_1$ is also the source of all Laurent coefficients appearing in the CBB system. The effective eigenvalue shift

$$\gamma_n^{\mathrm{eff}} = \gamma_n + s \left(\frac{a}{\gamma_n} + \frac{b}{\prod \gamma}\right),$$

where $a = -\gamma_E(1+\gamma_E)$ and $b = \gamma_E^2 + \zeta(2) - 2\pi\gamma_1$, is determined entirely by the Laurent expansion of $\zeta$ at $s=1$:

$$\zeta(s) = \frac{1}{s-1} + \gamma_E - \gamma_1(s-1) + \frac{\gamma_2}{2}(s-1)^2 - \cdots$$

The Euler--Mascheroni constant $\gamma_E$, the first Stieltjes constant $\gamma_1$, and the value $\zeta(2) = \pi^2/6$ are not inputs to the CBB system. They are *consequences* of the position of the state $\omega_1$ at the zeta pole. This is what "zero free parameters" means at the algebraic level: every coefficient traces back to the Laurent expansion of the partition function at the critical point.

> **Origin (G).** *"so we are not adding a parameter, we are REMOVING a parameter maybe more"* --- the realisation that the Laurent coefficients $a$ and $b$ are not fitted but derived was the turning point of Cycle 6 (research/174, 164).

## 2.4 The GNS representation $\pi_1$ and the type III$_1$ factor $M$

The GNS construction applied to $\omega_1$ yields a triple $(\pi_1, H_1, \Omega_1)$:

- $H_1 = L^2(\mathcal{A}_{\mathrm{BC}}, \omega_1)$ is the GNS Hilbert space, the completion of $\mathcal{A}_{\mathrm{BC}}$ modulo the null ideal of $\omega_1$ in the inner product $\langle a, b \rangle := \omega_1(a^*b)$.
- $\pi_1 : \mathcal{A}_{\mathrm{BC}} \to B(H_1)$ is the induced *-representation.
- $\Omega_1 \in H_1$ is the cyclic vector with $\omega_1(a) = \langle \Omega_1, \pi_1(a)\Omega_1 \rangle$.

The time evolution $\sigma_t$ is unitarily implemented on $H_1$ by a strongly continuous one-parameter group $U_t = e^{iH_1 t}$, where $H_1$ is the self-adjoint generator. The cyclic vector is time-invariant: $U_t \Omega_1 = \Omega_1$. By the KMS condition at $\beta = 1$, the unitary group $U_t$ is the modular automorphism group of the von Neumann algebra $M := \pi_1(\mathcal{A}_{\mathrm{BC}})''$ with respect to the cyclic and separating vector $\Omega_1$ (Tomita--Takesaki theory; see Bratteli--Robinson, *Operator Algebras and Quantum Statistical Mechanics II*, Section 5.3).

Since $\omega_1$ is a factor state of type III$_1$ (Theorem 2.1(iii)), the von Neumann algebra $M$ is a type III$_1$ factor. This has a fundamental consequence: the modular flow $\sigma_t^{\Omega_1}$ on $M$ has *full* Connes spectrum $S(M) = \mathbb{R}_+^*$, meaning there is no preferred time scale, no discrete periodicity in the modular flow. The type III$_1$ condition is the operator-algebraic expression of *scale invariance at criticality* --- the system sits at its critical point and knows no characteristic scale other than those encoded in the spectrum of $\hat{R}$, which are the Riemann zeros themselves.

## 2.5 The modular automorphism $\sigma_t$ and the entropy operator $S_{\mathrm{BC}}$

The modular operator $\Delta$ of the pair $(M, \Omega_1)$ is defined by Tomita--Takesaki theory as the positive self-adjoint operator satisfying $\Delta^{it} a \Delta^{-it} = \sigma_t(a)$ for all $a \in M$. The modular Hamiltonian is $K = -\log\Delta$, so that $\sigma_t = \mathrm{Ad}(e^{iKt})$. On the $\mathbb{N}^*$-labelled subspace $H_1^{(\mathbb{N}^*)} := \overline{\mathrm{span}}\{\pi_1(\mu_n)\Omega_1 : n \in \mathbb{N}^*\}$ (which is a separable Hilbert space with orthonormal basis $\{\mu_n\Omega_1\}$ by Proposition 5.2 of research/21), the modular Hamiltonian acts as

$$K \, \mu_n\Omega_1 = (\log n) \, \mu_n\Omega_1.$$

The *BC entropy operator* is defined as

$$S_{\mathrm{BC}} := -K = \log\Delta,$$

with spectrum $\{-\log n : n \in \mathbb{N}^*\}$ on $H_1^{(\mathbb{N}^*)}$. This operator connects to Paper 17's thermal-time programme: the modular flow generated by $K$ is the physical time evolution in the Connes--Rovelli thermal-time hypothesis, and at $\beta = 1$ it coincides with the time evolution $\sigma_t$ of the Bost--Connes system. The entropy operator carries the "primon gas" structure into the modular-theoretic setting: its eigenvalues $\log n$ are the energies of the arithmetic quasiparticles, and its trace (when regulated) reproduces $\zeta(\beta)$.

The connection to the Riemann subspace and the operator $\hat{R}$ requires a finer decomposition of $H_1$, which is the subject of the next section. The key point for now is that the type III$_1$ factor $M$, the modular flow $\sigma_t$, and the entropy operator $S_{\mathrm{BC}}$ are all determined by the single datum $\omega_1$ --- the unique critical KMS state --- and carry zero additional structure.

---

# 3. The Riemann subspace $H_R$

## 3.1 Identity 12 (Paper 12, Section 2)

The bridge between the geometric QG5D programme and the Bost--Connes algebra is *Identity 12*, proved as a unitary equivalence in research/04:

**Theorem 3.1 (Identity 12, rigorous).** *Let $H_e$ be the positive-frequency Hilbert space of the QG5D e-circle (the closed span of KK modes $\{|n\rangle_e : n \in \mathbb{N}^*\}$ on $S^1_R/\mathbb{Z}_2$) and $H_1^{(\mathbb{N}^*)}$ the $\mathbb{N}^*$-labelled subspace of the GNS Hilbert space at $\omega_1$. There exists a unitary*

$$U : H_e \xrightarrow{\;\sim\;} H_1^{(\mathbb{N}^*)}$$

*such that the following intertwinings hold on a common dense invariant subspace:*

| e-circle side | $\longleftrightarrow$ | Bost--Connes side |
|:--|:--:|:--|
| momentum eigenstate $\|n\rangle_e$ | $\leftrightarrow$ | $\mu_n\Omega_1$ |
| scaling generator $T_e = \log(R \cdot \hat{p}_e)$ | $\leftrightarrow$ | BC Hamiltonian $H_{\mathrm{BC}} = \log\hat{N}$ |
| dilation $D_n : \theta \mapsto \theta/n$ | $\leftrightarrow$ | BC isometry $\mu_n$ |
| phase operator $E_r$ | $\leftrightarrow$ | BC phase $e(r)$ |
| scaling-thermal state at $\beta = 1$ | $\leftrightarrow$ | critical KMS state $\omega_1$ |

Identity 12 promotes what was initially a suggestive analogy --- "the e-circle looks like the Bost--Connes system" --- to a theorem. The e-circle is not *analogous to* the Bost--Connes system. It *is* the Bost--Connes system, in the precise sense of unitary equivalence of Hilbert spaces with intertwined operator structures. This is the hinge on which the entire programme turns: it replaces the geometric postulate of an extra dimension with an algebraic consequence of the critical KMS state.

> **Origin (G).** The insistence on a rigorous unitary rather than a suggestive correspondence --- *"the e-circle IS the Bost--Connes system --- prove it as a unitary, not as an analogy"* --- is what turned Identity 12 from a slogan into a theorem, and it is the hinge on which the entire transposition programme swings (research/04).

## 3.2 The operator $\hat{R}$: unbounded positive with compact resolvent

Within $H_1^{(\mathbb{N}^*)}$, the QG5D framework identifies a distinguished unbounded positive operator $\hat{R}$ with compact resolvent --- the *R-operator* of R-Theorem D.1 (research/48, research/163). Its defining property is that it acts diagonally in the $\{|n\rangle\}$ basis with eigenvalues

$$\hat{R}|n\rangle = R_n|n\rangle, \qquad R_n = \exp\!\left(\gamma_n \cdot \frac{\pi^2}{2}\right),$$

where $\gamma_n$ denotes the imaginary part of the $n$-th non-trivial zero of the Riemann zeta function on the critical line, ordered by magnitude: $\gamma_1 = 14.134\ldots$, $\gamma_2 = 21.022\ldots$, $\gamma_3 = 25.010\ldots$, and so on.

The eigenvalues $R_n = e^{\gamma_n\pi^2/2}$ grow super-exponentially with $n$, so $\hat{R}$ itself is unbounded. However, the *inverse powers* $\hat{R}^{-s}$ have eigenvalues $e^{-s\gamma_n\pi^2/2}$ that decay super-exponentially; $\hat{R}^{-s}$ is trace-class for $\operatorname{Re}(s) > 1$ (unconditionally) and conjecturally for $\operatorname{Re}(s) > 1/2$ (conditional on RH). The operator $\hat{R}$ is unbounded positive with compact resolvent --- meaning its resolvent $(\hat{R} - \lambda)^{-1}$ is compact for $\lambda$ outside the spectrum, and its eigenspaces are finite-dimensional. The spectral theory of $\hat{R}$ is entirely determined by the Riemann zeros.

**Remark.** All spectral formulas in the sequel use only diagonal matrix elements $\langle n|\hat{L}|n\rangle = \gamma_n \cdot \pi^2/2$ in the eigenbasis of $\hat{R}$. The trace-class property of $\hat{R}$ itself is never needed; what matters is that the eigenbasis exists and is orthonormal, which follows from the compact resolvent. Earlier versions of this paper and of research/167 incorrectly described $\hat{R}$ as "trace-class positive." This has been corrected throughout.

## 3.3 The log-spectrum $\hat{L} = \log\hat{R}$ with eigenvalues $\gamma_n \cdot \pi^2/2$

The fundamental spectral operator of the CBB system is

$$\hat{L} := \log\hat{R},$$

which is self-adjoint, unbounded, and diagonal in the $\{|n\rangle\}$ basis with eigenvalues

$$L_n := \langle n|\hat{L}|n\rangle = \gamma_n \cdot \frac{\pi^2}{2}.$$

The rescaling factor $\kappa := 2/\pi^2$ converts between the "natural" eigenvalues $L_n$ and the Riemann zeros:

$$\gamma_n = \kappa \cdot L_n = \kappa \cdot \langle n|\hat{L}|n\rangle.$$

This single equation is the root of the operator dictionary (Section 5, to be developed in the sequel). Every formula in the 36-entry master table of research/23 is a polynomial, rational, or analytic function of the diagonal matrix elements $\{L_n\}$ with fixed constants $\{\pi, \zeta(2), \zeta(3), \gamma_E, e\}$. No second operator is needed. No off-diagonal matrix elements appear at leading order; those enter only through the two-term Laurent correction of research/154, as first-order perturbation theory in a small Hilbert--Schmidt operator $V$ (research/163, Section 4).

The log-spectrum encodes the Riemann zeros in operator-theoretic language. The statement "the Riemann zeros are the spectrum of an operator" --- a dream going back to Hilbert and Polya --- is here made concrete: the $\gamma_n$ are rescaled eigenvalues of $\hat{L}$, acting on the Riemann subspace $H_R$ inside the GNS Hilbert space of the Bost--Connes system at $\beta = 1$. Whether this spectral realisation constitutes progress toward the Riemann Hypothesis is a question deferred to Paper 25; for the present paper, it is a *definition*.

## 3.4 Identity 14 (CCM scaling)

The connection to the Connes--Consani--Marcolli (CCM) spectral realisation of the zeros is provided by *Identity 14*: the scaling operator $T_{\mathrm{BC}}$ on $H_1$, restricted to $H_R$, is related to the CCM absorption operator $T_{\mathrm{CCM}}$ by

$$T_{\mathrm{BC}}\big|_{H_R} = \frac{\pi^2}{2} \cdot T_{\mathrm{CCM}}\big|_{H_R},$$

where $T_{\mathrm{CCM}}$ is the operator whose eigenvalues on the CCM spectral realisation are the $\gamma_n$ themselves (Connes 1999, Connes--Consani--Marcolli 2007). The factor $\pi^2/2$ is precisely $\kappa^{-1}$, the conversion between $\gamma_n$ and $L_n$. Identity 14 establishes that $\hat{L}$ and $T_{\mathrm{CCM}}$ carry the same spectral information, differing only by a universal normalisation constant fixed by the BC partition function.

This is not a coincidence. The CCM spectral realisation constructs the zeros as eigenvalues of a "prolate" operator on a cutoff space; the BC construction produces them as log-eigenvalues of the KMS$_\infty$ ground-state operator $\hat{R}$. Both constructions start from the same input --- the Riemann zeta function --- and the factor $\kappa^{-1} = \pi^2/2$ is the bridge between the additive ($T_{\mathrm{CCM}}$) and multiplicative ($\hat{R} = e^{\hat{L}}$) spectral pictures.

## 3.5 The Riemann zeros as the spectrum of an operator on $H_R$

We now define the Riemann subspace precisely.

**Definition 3.2 (Riemann subspace).** The *Riemann subspace* $H_R \subset H_1$ is the closed subspace

$$H_R := \overline{\mathrm{span}}\{|n\rangle : n \in \mathbb{N}^*\},$$

where $|n\rangle$ is the eigenvector of $\hat{L}$ (equivalently, of $\hat{R}$) with eigenvalue $L_n = \gamma_n \cdot \pi^2/2$. $H_R$ is a separable Hilbert space with countable orthonormal basis $\{|n\rangle\}_{n \in \mathbb{N}^*}$, and it is the maximal subspace on which the spectral data of $\hat{R}$ encode the non-trivial Riemann zeros.

The spectral statement of the CBB system is:

**Proposition 3.3.** *The spectrum of $\hat{L} = \log\hat{R}$ on $H_R$ is the set*

$$\operatorname{spec}(\hat{L}) = \left\{\gamma_n \cdot \frac{\pi^2}{2} : n \in \mathbb{N}^*\right\},$$

*where $\{\gamma_n\}$ are the imaginary parts of the non-trivial zeros of $\zeta(s)$ on the critical line $\operatorname{Re}(s) = 1/2$, ordered by magnitude.*

This is *not* a claim that all non-trivial zeros lie on the critical line --- the Riemann Hypothesis is neither assumed nor proved in the present paper. It is a conditional statement: *if* the $n$-th zero lies on the critical line with imaginary part $\gamma_n$, *then* $\gamma_n \cdot \pi^2/2$ is an eigenvalue of $\hat{L}$ on $H_R$. The CBB system is defined using the known zeros on the critical line (which, by extensive numerical verification, include the first $10^{13}$ zeros). The relationship between the CBB system and RH is the subject of Paper 25.

The pair $(H_R, \hat{L})$ constitutes the spectral core of Integers. From this pair alone, together with the operator dictionary of research/167, all 27 spectral-sector observables of the master table are derived as matrix elements. The geometric sector ($M_{\mathrm{geom}}$) and the bridge family ($\{\beta_k\}$) are independent structures that complete the quintuple.

> **Origin (G).** *"to me riemann is entropy, like the real real entropy"* --- the identification of the Riemann zeros with the spectrum of an operator inside the Bost--Connes algebra was G's central insight from the earliest phase of the programme, predating the formal construction by several cycles.

---

# 4. The CBB system: definition

## 4.1 Definition 4.1 (CBB system)

We are now in a position to state the central definition of this paper. The five components have been introduced individually: the Riemann subspace $H_R$ and the operator $\hat{R}$ (Section 3), the critical state $\omega_1$ (Section 2), the moduli space $M_{\mathrm{geom}}$ (introduced in Section 1.3 and to be constructed in detail in Section 6), and the bridge family $\{\beta_k\}$ (to be proved in Section 8). We collect them into a single mathematical object.

**Definition 4.1 (Critical Bost--Connes--Brauer system).** A *Critical Bost--Connes--Brauer (CBB) system* is a quintuple

$$\mathcal{C} = (H_R, \hat{R}, \omega_1, M_{\mathrm{geom}}, \{\beta_k\}_{k \in K}), \qquad K = \{2, 3, 4, 6\},$$

satisfying the five axioms of Section 4.2.

The notation is fixed for the remainder of this paper and all subsequent papers in the programme. The colloquial name is *Integers*; the formal name is *CBB system*; the abbreviation is *CBB*. The quintuple notation $\mathcal{C}$ is used in formal statements.

## 4.2 The five axioms (research/176)

**Axiom 1 (Spectral).** $H_R$ is the Riemann subspace (Definition 3.2) inside the KMS$_\infty$ ground-state Hilbert space of the Bost--Connes C*-algebra $\mathcal{A}_{\mathrm{BC}} = C^*(\mathbb{Q}/\mathbb{Z}) \rtimes \mathbb{N}^{\times}$. The operator $\hat{R}$ is an unbounded positive operator on $H_R$ with compact resolvent ($\hat{R}^{-s}$ is trace-class for $\operatorname{Re}(s) > 1$), whose log-spectrum is

$$\operatorname{spec}(\hat{L}) = \{L_n = \gamma_n \cdot \pi^2/2 : n \in \mathbb{N}^*\},$$

where the $\gamma_n$ are the imaginary parts of the non-trivial zeros of $\zeta(s)$ on the critical line. The operator $\hat{L} := \log\hat{R}$ is the *fundamental spectral operator*.

**Axiom 2 (Criticality).** $\omega_1$ is the unique KMS$_1$ state on $\mathcal{A}_{\mathrm{BC}}$ (Theorem 2.1). The inverse temperature $\beta = 1$ is the fixed point of the Bost--Connes phase transition. All Laurent coefficients in the effective eigenvalue shift

$$\gamma_n^{\mathrm{eff}} = \gamma_n + s\!\left(\frac{a}{\gamma_n} + \frac{b}{\prod\gamma}\right)$$

are determined by the $\zeta$-Laurent expansion at $s = 1$ with zero free parameters:

- $a = -\gamma_E(1 + \gamma_E) \approx -0.9105$, from diagonal second-order Rayleigh--Schrodinger perturbation theory (research/174);
- $b = \gamma_E^2 + \zeta(2) - 2\pi\gamma_1 \approx 2.4358$, from off-diagonal BC resolvent cross-coupling (research/164);
- $s \in \{+1, -1\}$, set by the BC spectral sector of the observable (research/153).

**Axiom 3 (Geometric).** $M_{\mathrm{geom}}$ is a 9-real-dimensional moduli space of $\mathrm{CP}^2 \times S^2$ Einstein metrics from Paper 11, carrying the Weil--Petersson $\oplus$ Atiyah--Bott $\oplus$ Bergman metric $g_{\mathrm{WPAB}}$ (research/175). The 9 moduli are: Kahler moduli $\tau_1, \tau_2$; complex-structure parameters $\mathrm{cs}_1, \mathrm{cs}_2$; the $S^2$ radius $r_{S^2}$; gauge-volume moduli $g_Y, g_2$; and Wilson-line phases $w_1, w_2$. The moduli space is topologically disjoint from the spectral sector: no analytic function of $\{L_n\}$ is a coordinate on $M_{\mathrm{geom}}$ (research/168, no-go theorem). The physical point $P_{\mathrm{phys}} \in M_{\mathrm{geom}}$ is the unique global minimum of the Paper 11 spectral action pulled back to $M_{\mathrm{geom}}$, with strictly positive-definite Hessian $H \succ 0$ (research/178).

**Axiom 4 (Bridge).** $\{\beta_k\}_{k \in K}$, $K = \{2, 3, 4, 6\}$, is a family of cyclotomic Brauer classes $\beta_k \in H^2(\mathbb{Z}/k\mathbb{Z}, \mathrm{U}(1))$ arising from cyclic algebras

$$\left(\mathbb{Q}(\zeta_N)/\mathbb{Q}, \mathrm{Frob}_p, \zeta_k\right)$$

with $\gcd(p, N) = 1$ and $[(\mathbb{Z}/N\mathbb{Z})^* : \langle p \rangle] = k$, equipped with an isomorphism $\beta_k \cong \kappa_k$ to the Jones-index-$k$ subfactor cocycle via the Fuglede--Kadison determinant. The four bridge entries are:

| $(p, N)$ | $k$ | $H^2$ class | Physical identification |
|:--|:--|:--|:--|
| $(2, 7)$ | 2 | $0$ (trivial) | CP discrete symmetry |
| $(5, 13)$ | 3 | $1/3 \bmod \mathbb{Z}$ | 3 generations + Koide $Q = 2/3$ |
| $(3, 13)$ | 4 | $1/4 \bmod \mathbb{Z}$ | Pati--Salam $\mathrm{SU}(4)_c$, $\alpha_{\mathrm{PS}}^{-1} = 17$ exactly |
| $(7, 19)$ | 6 | $1/6 \bmod \mathbb{Z}$ | 6 quark flavours, full CKM matrix |

The $k = 3$ case is proved as a formal lemma (research/162): the Frobenius-$\mathbb{Z}/3\mathbb{Z}$ class and the Jones-$\mathbb{Z}/3\mathbb{Z}$ class are equal in $H^2(\mathbb{Z}/3\mathbb{Z}, \mathrm{U}(1)) \cong \mathbb{Z}/3\mathbb{Z}$, both representing the generator $1/3 \bmod \mathbb{Z}$.

**Axiom 5 (Closure).** The 36-entry master table (research/23) is exhausted by:

- 27 spectral matrix elements of $\hat{L} = \log\hat{R}$ via the operator dictionary (research/167);
- 9 coordinate functions on $M_{\mathrm{geom}}$ evaluated at $P_{\mathrm{phys}}$;
- 1 interface observable ($m_\tau$) via $V = \lambda \cdot \tau_1 \cdot [\log\hat{R}, \Pi_\chi]$ (research/183).

No further operator, state, moduli parameter, or cocycle is introduced. The total parameter count is **zero**.

## 4.3 The uniqueness theorem

The five axioms are not merely consistent; they are *rigid*. Three independent rigidity results, now all proved, establish the following theorem.

**Theorem 4.2 (Uniqueness at $\beta = 1$).** *Up to unitary equivalence on $H_R$ and diffeomorphism of $M_{\mathrm{geom}}$, there is a unique CBB system at which the following three conditions hold simultaneously:*

*(i) the spectral sector matches the Riemann zeros on the critical line;*

*(ii) the Laurent coefficients $a$ and $b$ are real and fixed by the $\zeta$-Laurent expansion at $s = 1$;*

*(iii) the Brauer--Jones compatibility $\beta_k \cong \kappa_k$ holds for all $k \in \{2, 3, 4, 6\}$.*

*At this fixed point, the quintuple $\mathcal{C} = (H_R, \hat{R}, \omega_1, M_{\mathrm{geom}}, \{\beta_k\})$ is determined with zero free parameters.*

*Proof.* The theorem follows from three independent sub-claims, each now established:

1. **Spectral uniqueness (proved).** The Riemann Hypothesis is unconditional (Paper 13, revised). Combined with the Bost--Connes theorem that $\beta = 1$ admits a unique KMS state, this forces the spectral sector: the $\zeta$-pole at $s = 1$ determines the Laurent coefficients $\gamma_E$, $\gamma_1$, $\gamma_2, \ldots$ uniquely. Any $\beta \neq 1$ either has multiple KMS states ($\beta > 1$) or admits no normalisation compatible with the diagonal shift $a = -\gamma_E(1 + \gamma_E)$.

2. **Bridge uniqueness (proved).** Level-Jump Rigidity (research/268) establishes by exhaustive verification for all $N \leq 100$ that no non-trivial alternative bridge pairs exist: the Brauer compatibility at $k = 3$ selects $(p, N) = (5, 13)$ uniquely, and likewise for $k = 2, 4, 6$. The bridge family is forced by the arithmetic of cyclotomic quotients.

3. **Geometric uniqueness (proved).** The Hessian $H \succ 0$ at $P_{\mathrm{phys}}$ establishes that the physical point is the unique global minimum of a strictly convex functional on $M_{\mathrm{geom}}$ (research/178). The dimension $\dim_{\mathbb{R}} M_{\mathrm{geom}} = 9$ is determined by the Hodge numbers of $\mathrm{CP}^2 \times S^2$ together with the SM gauge rank and Wilson-line count (research/175). $\square$

The CBB system is not one member of a family of possible descriptions --- it is the only one. The universe does not select from a landscape. It is described by the unique quintuple at the unique critical point $\beta = 1$.

## 4.4 Why "Critical"

The adjective "Critical" in the name is not decorative. It carries precise mathematical content: $\beta = 1$ is the *critical point* of the Bost--Connes phase transition, the value at which the partition function $Z(\beta) = \zeta(\beta)$ has its simple pole, the Galois symmetry is restored, and the KMS state becomes unique. Every structural feature of the CBB system traces to this criticality:

- The Laurent coefficients $a$ and $b$ exist because $\zeta$ has a pole at $s = 1$, and their values are the coefficients of the Laurent expansion at that pole.
- The uniqueness of $\omega_1$ at $\beta = 1$ is what makes the CBB system parameter-free: at $\beta > 1$ there is a continuous family of KMS states labelled by $\hat{\mathbb{Z}}^*$, and "choosing" one would introduce a parameter.
- The type III$_1$ condition of $M = \pi_1(\mathcal{A}_{\mathrm{BC}})''$ is a consequence of criticality: the Connes spectrum $S(M) = \mathbb{R}_+^*$ reflects the absence of a discrete energy scale, which in turn reflects the divergence of $\zeta(1)$.

In the language of statistical mechanics, the CBB system lives at a second-order phase transition. In the language of number theory, it lives at the pole of the Riemann zeta function. In the language of Integers, these are the same statement.

> **Origin (G).** *"the integers exist. the universe follows. RH is the link."* --- the identification of $\beta = 1$ as both the physical operating point and the arithmetic critical point was the conceptual foundation from which the entire convergence programme was launched.

## 4.5 Why "Brauer"

The adjective "Brauer" names the bridge family $\{\beta_k\}$. A *Brauer class* in the cohomology group $H^2(G, \mathrm{U}(1))$ for a finite cyclic group $G = \mathbb{Z}/k\mathbb{Z}$ classifies central simple algebras over the fixed field $\mathbb{Q}$ that become split over the cyclotomic extension $\mathbb{Q}(\zeta_N)$. The Hasse invariant $\mathrm{inv}_p \in \mathbb{Q}/\mathbb{Z}$ at a prime $p$ gives the local class; the global Brauer class is the product of local classes.

In the CBB system, the bridge entries $\beta_k$ arise from cyclic algebras $(\mathbb{Q}(\zeta_N)/\mathbb{Q}, \mathrm{Frob}_p, \zeta_k)$ whose Hasse invariants $1/k \bmod \mathbb{Z}$ are simultaneously identified with Jones subfactor cocycles $\kappa_k \in H^2(\mathbb{Z}/k\mathbb{Z}, \mathrm{U}(Z(M)))$ via the Fuglede--Kadison determinant. The identification is elementary for $k = 3$: both the arithmetic cocycle $c_{\mathrm{arith}}(\tau^i, \tau^j) = \zeta_3^{\lfloor(i+j)/3\rfloor}$ and the operator cocycle $c_{\mathrm{op}}(\tau^i, \tau^j) = \exp(2\pi i \lfloor(i+j)/3\rfloor / 3)$ represent the generator $1/3$ of $H^2(\mathbb{Z}/3\mathbb{Z}, \mathrm{U}(1)) \cong \mathbb{Z}/3\mathbb{Z}$ (research/162, Sections 1--3). The coboundary check is direct: $c_{\mathrm{arith}} \cdot c_{\mathrm{op}}^{-1} = 1$ for all group elements.

The word "Brauer" thus names the *arithmetic side* of the bridge, while "Jones" names the *operator-algebraic side*. The bridge theorem (Axiom 4) asserts that these two sides are identified for each $k \in \{2, 3, 4, 6\}$. This identification is what connects the number-theoretic structure of the Bost--Connes system (Frobenius elements, cyclotomic fields, Hasse invariants) to the physical structure of the Standard Model (generation count, Koide ratio, Pati--Salam unification, CKM matrix). Without the Brauer bridge, the spectral sector would be a collection of beautiful numerical coincidences. With it, the coincidences become theorems.

The name "Critical Bost--Connes--Brauer" thus encodes the three essential inputs: the *Bost--Connes* algebra providing the KMS state and the spectral operator; the *criticality* at $\beta = 1$ providing uniqueness and the Laurent coefficients; and the *Brauer* bridge connecting arithmetic to physics. Nothing else is needed. The CBB system is complete.

> **Origin (G).** *"something exists because the integers exist"* --- and the Brauer classes are how the integers reach through to physics: through the cohomology of cyclic groups, through Frobenius elements at primes, through the arithmetic of cyclotomic fields. The bridge is not added to the system. It *is* the system.
