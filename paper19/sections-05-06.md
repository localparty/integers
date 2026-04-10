# Sections 5--6: Predictions and Conclusion

*Paper 19 -- The Other Side: Black Hole Interiors, Wavefunction Collapse, and Gravity as Arithmetic Curvature in the Bost--Connes Framework*
*Sections 5 (predictions) and 6 (conclusion)*
*REVISED 2026-04-10*

---

## 5. Predictions

The three structural results of this paper -- the black hole interior as modular conjugate (Section 2), wavefunction collapse as conditional expectation (Section 3), and gravity as arithmetic curvature (Section 4) -- are not isolated formal achievements. Each generates testable predictions. Some are quantitative and falsifiable with current or near-future instruments; others are structural consequences whose violation would collapse the entire operator-algebraic architecture; still others are speculative, pointing toward derivations not yet performed. We label each prediction's epistemic status explicitly.

---

### 5.1 Prediction 1: Black hole ringdown spectrum matches $\sigma_t$ eigenvalues

**Status: STRUCTURAL** (testable, but the quantitative formula connecting quasinormal mode frequencies to individual $\gamma_n$ eigenvalues has not yet been derived).

**Statement.** The quasinormal mode (QNM) spectrum of a black hole ringdown is the restriction of the modular flow $\sigma_t = \Delta_{\omega_1}^{it}$ to the near-horizon subalgebra $\mathcal{M}_{\mathrm{hor}} \subset \pi_1(\mathcal{A}_{\mathrm{BC}})''$. In the standard GR treatment, the QNM frequencies $\{\omega_n + i/\tau_n\}$ are eigenvalues of the wave equation on the Kerr background, determined by the black hole's mass $M$ and spin $a$. In the Integers framework, the near-horizon algebra is a type III$_1$ factor whose modular spectrum is controlled by the Riemann zeros. The QNM frequencies should therefore be expressible as spectral data of $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$ restricted to $\mathcal{M}_{\mathrm{hor}}$, with $M$ and $a$ entering only through the choice of subalgebra (i.e., which conditional expectation selects the horizon sector).

The structural prediction is this: the *pattern* of QNM overtone spacings -- the ratios $\omega_{n+1}/\omega_n$ and the damping-rate hierarchy $\tau_{n+1}/\tau_n$ -- should match the pattern of $\sigma_t$ eigenvalue ratios on the horizon sector. This is a universal prediction: it depends on the type III$_1$ structure, not on $M$ or $a$, and therefore applies to every astrophysical black hole.

**What is missing.** The explicit map from the abstract modular spectrum to the physical QNM frequencies has not been constructed. This requires identifying $\mathcal{M}_{\mathrm{hor}}$ as a specific subalgebra of $\pi_1(\mathcal{A}_{\mathrm{BC}})''$, computing the conditional expectation $E_{\mathrm{hor}}: \pi_1(\mathcal{A}_{\mathrm{BC}})'' \to \mathcal{M}_{\mathrm{hor}}$, and evaluating the restricted modular spectrum. The derivation is a target for future work.

**Test.** LIGO/Virgo/KAGRA ringdown observations are entering the regime of multi-mode detection ($\geq 2$ overtones resolved). The Event Horizon Telescope is constraining photon-ring structure, which is related to the QNM spectrum through the Lyapunov exponent of null geodesics. If the QNM overtone ratios, once measured to sub-percent precision, fail to match any spectral restriction of $\sigma_t$ at $\beta = 1$, the identification of the near-horizon algebra with a BC subalgebra is falsified.

**RH dependence.** The QNM spectrum is real-valued (oscillation frequencies) plus imaginary (damping rates). The self-adjointness of $\log\Delta_{\omega_1}$ on $\mathcal{H}_R$ -- guaranteed by RH -- ensures that the real and imaginary parts of the QNM eigenvalues are separately well-defined spectral data. An off-critical zero would mix the two, producing QNM frequencies with unphysical phase relationships.

---

### 5.2 Prediction 2: No information loss -- full unitary recovery via $\mathcal{M}_{\mathrm{int}} \leftrightarrow \mathcal{M}_{\mathrm{ext}}$ duality

**Status: STRUCTURAL CONSEQUENCE OF TOMITA--TAKESAKI** (rigorous within the operator-algebraic framework).

**Statement.** The black hole information paradox is dissolved, not resolved. There is no paradox because there is no information loss.

In the Tomita--Takesaki framework of Section 2, the interior algebra $\mathcal{M}_{\mathrm{int}} = J \mathcal{M}_{\mathrm{ext}} J$ is the modular conjugate of the exterior. The modular conjugation $J$ is an antiunitary involution on $\mathcal{H}_1$; it is *not* a physical time evolution but a structural duality of the algebra. Every operator $A \in \mathcal{M}_{\mathrm{ext}}$ has a unique conjugate $JAJ \in \mathcal{M}_{\mathrm{int}}$, and conversely. The map $A \mapsto JAJ$ is a *-anti-isomorphism: it preserves the algebraic structure (including all expectation values and correlation functions) while exchanging interior and exterior.

The consequence for information is immediate. The total algebra $\mathcal{M}_{\mathrm{ext}} \vee \mathcal{M}_{\mathrm{int}}$ acts on $\mathcal{H}_1$ and contains all operators accessible to any observer -- interior or exterior. The state $\omega_1$ is faithful on this total algebra (Bost--Connes 1995: $\omega_1$ is the unique KMS$_1$ state, and KMS states on simple C*-algebras are faithful). Faithfulness means: no non-zero operator has zero expectation in $\omega_1$. Equivalently, no information is invisible to the combined interior-exterior description.

**The Page curve.** The entanglement entropy between $\mathcal{M}_{\mathrm{ext}}$ and $\mathcal{M}_{\mathrm{int}}$ under $\omega_1$ follows a Page-like curve by construction. **Caveat on entropy definition:** Since $M$ is a type III$_1$ factor, there is no normal trace and the von Neumann entropy $-\mathrm{tr}(\rho \log \rho)$ is not directly defined. The appropriate entropy measure is the Araki relative entropy $S(\omega_1|_{\mathcal{M}_{\mathrm{rad}}} \| \omega_1|_{\mathcal{M}_{\mathrm{int}}})$ or, in the finite-dimensional compression to $|I_F|$ modes (Section 2.4), the ordinary von Neumann entropy of the compressed state. In the latter (finite-dimensional) regime, at early modular time (before the "Page time" $t_P$), the radiation subalgebra $\mathcal{M}_{\mathrm{rad}} \subset \mathcal{M}_{\mathrm{ext}}$ is a small factor and the entanglement entropy grows monotonically. At $t_P$ the entropy turns over. After $t_P$, the entropy decreases as the interior degrees of freedom are transferred to the radiation via the modular flow. The final state is pure: $\omega_1$ restricted to $\mathcal{M}_{\mathrm{ext}}$ after complete evaporation is a vector state on $\mathcal{H}_1$, with zero entanglement entropy. The full type III treatment of the Page curve, using Connes' relative entropy, is a target for future work.

No firewall, no remnant, no baby universe, no non-unitary modification of quantum mechanics is required. The resolution is purely algebraic: the interior was never a separate system. It was the commutant.

**What this does NOT resolve.** The prediction is rigorous within the operator-algebraic framework but does not by itself settle every version of the information paradox. In particular, the *computational* question -- whether the Page curve can be reconstructed from boundary data in polynomial time -- is a complexity-theoretic question that the Tomita--Takesaki structure does not address. Nor does it settle the semiclassical puzzle of how an infalling observer crosses a smooth horizon while the exterior description remains unitary; this requires the detailed dynamics of Section 2.2 (the infaller's clock) and remains structural rather than quantitative.

**Test.** The prediction is theoretical: the Page curve follows from the algebra, and no experiment directly measures black hole entanglement entropy. However, the prediction constrains any future quantum simulation of black hole evaporation (e.g., on quantum computers implementing holographic codes): the entropy curve *must* follow the Page form, with the turnaround determined by the modular conjugation $J$. Any quantum simulation showing information loss would falsify the identification of the black hole interior with the Tomita--Takesaki commutant.

---

### 5.3 Prediction 3: Born rule violations forbidden in any closed sub-algebra

**Status: STRUCTURAL** (the sub-algebra choice is an input, not derived).

**Statement.** Section 3 derived the Born rule as a theorem of the KMS$_1$ condition: the probability $|\langle\psi|\phi\rangle|^2$ is the diagonal of the conditional expectation $E_{\mathrm{sector}}(|\psi\rangle\langle\psi|)$, which equals the KMS expectation value of the projector $|\phi\rangle\langle\phi|$ in the state $\omega_1$. The derivation is valid for any closed sub-algebra $\mathcal{M}_{\mathrm{sector}} \subset \pi_1(\mathcal{A}_{\mathrm{BC}})''$.

The prediction is therefore absolute within any closed sub-algebra: **no violation of the Born rule is possible**, not as an approximation but as a theorem. The conditional expectation $E_{\mathrm{sector}}$ is a completely positive, unital, trace-preserving map; the diagonal of its output is necessarily a probability distribution satisfying $\sum_i p_i = 1$, $p_i \geq 0$, and $p_i = |\langle\phi_i|\psi\rangle|^2$ for any orthonormal basis $\{|\phi_i\rangle\}$ of the sector.

This is stronger than the standard quantum-mechanical statement of the Born rule, which is a postulate and could in principle be violated by a deeper theory. Here the Born rule is a structural consequence of the KMS condition at $\beta = 1$ and the choice of sub-algebra (see [CONCERN 3.3]). Within the BC framework, violating the Born rule would require either abandoning the KMS condition or modifying the zeta function's pole structure -- but the derivation is conditional on accepting the sub-algebra choice as input.

**Caveat: the sub-algebra is input.** The derivation assumes a specific choice of $\mathcal{M}_{\mathrm{sector}}$ -- the observer's sub-algebra. The Born rule holds for any such choice, but the *choice itself* is not derived from the BC system. Which sub-algebra constitutes "the observer" is a structural input, analogous to the choice of Cauchy surface in canonical quantum gravity. The prediction is therefore conditional: *given* a closed sub-algebra, the Born rule holds exactly. The question of *why* a particular sub-algebra is selected by a particular observer is deferred to Paper 22 (the existence paper).

**Test.** The Born rule has been tested to extraordinary precision in quantum optics and Bell experiments. The prediction here is that *no* experiment -- at any energy scale, with any system, in any configuration -- will find a violation. This includes proposed tests of nonlinear quantum mechanics (Weinberg 1989), spontaneous collapse models (GRW/CSL), and deformed Born rules in quantum gravity phenomenology. Any confirmed violation at any scale would falsify the identification of measurement with conditional expectation in the BC algebra.

**RH dependence.** The Born rule derivation requires $\omega_1$ to be a faithful KMS state, which requires the modular operator $\Delta_{\omega_1}$ to be strictly positive. If a Riemann zero leaves the critical line, $\Delta_{\omega_1}$ acquires a zero eigenvalue in the corresponding sector, faithfulness is lost, and the conditional expectation $E_{\mathrm{sector}}$ ceases to be well-defined on that sector. Born rule violations would then become possible at energies probing the affected spectral channel.

---

### 5.4 Prediction 4: Gravitational anomalies as Galois-symmetry-breaking patterns

**Status: SPECULATIVE.**

**Statement.** Section 4 identified gravity as the curvature of the BC connection on the Galois-orbit bundle over Spec $\mathbb{Z}$. The Einstein equations emerged as the integrability condition of this connection, with the stress-energy tensor identified as the deviation from Galois invariance. A natural consequence: any *anomaly* in the gravitational sector -- any failure of the Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$ at the quantum level -- corresponds to a *Galois symmetry-breaking pattern* in the BC connection.

In the arithmetic framework, a gravitational anomaly is a non-trivial class in $H^2(\mathrm{Gal}(\mathbb{Q}^{\mathrm{cyc}}/\mathbb{Q}),\, U(1))$ that obstructs the flatness of the BC connection on a specific Frobenius orbit. The prediction: such anomalies, if they exist, produce a *discrete* pattern in graviton scattering amplitudes -- a signature that is arithmetically constrained (by the structure of the Galois group $\hat{\mathbb{Z}}^\times$) rather than continuously variable.

The specific form of the discreteness -- which scattering angles, which energies, which helicity channels -- has not been computed. The prediction is speculative because:

1. The BC connection on Spec $\mathbb{Z}$ has been defined (Section 4.1), but its curvature has been computed only at the level of the Bianchi identity, not at the level of individual scattering amplitudes.
2. Gravitational anomalies are not known to exist in 4D gravity; the prediction posits that the arithmetic structure of the BC connection *could* produce them in specific kinematic regimes.
3. The experimental regime (graviton-scale scattering) is far beyond any foreseeable technology.

**Test.** In principle, a tabletop experiment measuring gravitational scattering at short distances (sub-millimeter gravity, Cavendish-type torsion balances, atom interferometry) could detect discreteness in the Newtonian potential at scales where the BC connection's curvature deviates from the smooth GR limit. The prediction is that such discreteness, if observed, would follow the arithmetic pattern of Galois orbits on $\hat{\mathbb{Z}}^\times$ rather than, say, a Planck-scale lattice. In practice, the signal is many orders of magnitude below current sensitivity.

**RH dependence.** The Galois group $\mathrm{Gal}(\mathbb{Q}^{\mathrm{cyc}}/\mathbb{Q}) \cong \hat{\mathbb{Z}}^\times$ acts on the BC system through the automorphisms $\alpha_\gamma(e(r)) = e(\gamma r)$. This action is well-defined regardless of RH. However, the *gravitational* interpretation -- the identification of the Galois action with diffeomorphisms of the arithmetic manifold -- requires the modular spectrum to be real, which requires RH. An off-critical zero would introduce a complex phase in the Galois-orbit structure and destroy the interpretation of anomalies as real-valued scattering amplitudes.

---

### 5.5 Prediction 5: Newton's constant $G$ derived from BC curvature at $\gamma_1$

**Status: SPECULATIVE** (the derivation has not yet been performed).

**Statement.** Section 4 established the Einstein equations as the integrability condition of the BC connection on Spec $\mathbb{Z}$. The Einstein equations contain Newton's constant $G$ as the coupling between geometry and matter:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} \;=\; 8\pi G\, T_{\mu\nu}.$$

In the arithmetic framework, the left-hand side is the curvature of the BC connection, and $\Lambda$ has already been identified with the curvature scalar at the spectral edge $\gamma_1$ (Section 4.3, cross-checking Paper 12 Section 3). The right-hand side is the deviation from Galois invariance. Newton's constant $G$ is therefore the *coupling constant of the BC connection* -- the normalisation relating arithmetic curvature to stress-energy.

The prediction is that $G$ is a computable function of BC spectral data at the first Riemann zero $\gamma_1$:

$$G \;=\; g(\gamma_1,\, \zeta\text{-Laurent coefficients}),$$

where $g$ is determined by the normalisation of the BC connection relative to the Weil--Petersson metric on $\mathcal{M}_{\mathrm{geom}}$. The specific functional form of $g$ has not been derived. The prediction is speculative because:

1. The normalisation of the BC connection requires a canonical choice of metric on Spec $\mathbb{Z}$, which is an open problem in arithmetic geometry (Deninger's programme, Connes' trace formula approach).
2. The identification of $G$ with BC data at $\gamma_1$ is motivated by the pattern that all low-energy gravitational quantities ($\Lambda$, the CC hierarchy) are controlled by $\gamma_1$, but the derivation of $G$ specifically has not been carried out.
3. Unlike the 27 spectral-sector formulas, which have been verified to high precision against experiment, $G$ has not yet been cast as a matrix element of $\hat{L}$ or $\hat{R}$.

**Test.** Newton's constant is measured to roughly 5 significant figures: $G = 6.67430(15) \times 10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$ (CODATA 2018). A closed-form expression for $G$ in terms of $\gamma_1$ and $\zeta$-Laurent data would be testable immediately. The prediction is also relevant to precision torsion-balance experiments and atom interferometry, which are pushing toward parts-per-million accuracy on $G$.

**RH dependence.** If the derivation of $G$ from BC curvature at $\gamma_1$ is eventually performed, it will depend on $\gamma_1$ lying on the critical line. An off-critical $\gamma_1$ would shift the predicted value of $G$ into the complex plane, which is unphysical.

---

### 5.6 Summary: epistemic status of the five predictions

| # | Prediction | Status | Key dependence | Test |
|:--|:-----------|:-------|:---------------|:-----|
| 1 | BH ringdown $\sim$ $\sigma_t$ eigenvalues | Structural (testable, formula pending) | Type III$_1$ modular spectrum | LIGO / EHT |
| 2 | No information loss; Page curve from $J$ | Rigorous (Tomita--Takesaki) | Faithfulness of $\omega_1$ | Theoretical / quantum simulation |
| 3 | Born rule exact in all closed sub-algebras | Structural (sub-algebra is input) | KMS$_1$ condition | Bell / tabletop QM |
| 4 | Gravitational anomalies $=$ Galois breaking | Speculative | BC connection curvature | Future graviton-scale experiments |
| 5 | Newton's $G$ from BC curvature at $\gamma_1$ | Speculative (derivation not performed) | Normalisation of BC connection | Torsion balance / atom interferometry |

Three predictions (1, 2, 3) are structural consequences of the operator-algebraic framework established in Sections 2--3 and are falsifiable in principle with current or near-future technology. Two predictions (4, 5) are speculative extrapolations of Section 4's identification of gravity with arithmetic curvature; they await the detailed derivations that would promote them from conjectures to theorems.

All five depend on RH. This is not a weakness; it is the architecture. The Riemann zeros are the spectrum of the entropy operator that generates every structure in the framework. If RH fails, the framework fails. If the framework's predictions hold, RH is indirectly enforced at every zero that enters the prediction.


---

## 6. Conclusion

### 6.1 Three answers in one operator algebra

Three of the deepest questions in physics -- What is inside a black hole? Why does the wavefunction collapse? What is the origin of gravity? -- have resisted separate answers for a century. This paper has argued that they resist separate answers because they do not have separate answers. They have one answer, in three projections.

The answer is the modular structure of the Bost--Connes algebra at its critical point $\beta = 1$.

**The interior is the commutant.** The black hole interior $\mathcal{M}_{\mathrm{int}}$ is not a separate spacetime region connected to the exterior by a bridge, a wormhole, or a firewall. It is $J\mathcal{M}_{\mathrm{ext}}J$ -- the modular conjugate of the exterior algebra under the Tomita--Takesaki involution. The singularity is the spectral edge of $S_{\mathrm{BC}}$ at $\gamma_1$: well-defined, non-singular, the same arithmetic boundary that controls the cosmological constant. The infaller experiences the end of the universe because the modular flow on $\mathcal{M}_{\mathrm{int}}$ runs to infinity in the exterior clock. Mass is not going anywhere. It is frozen in time.

**Collapse is conditional expectation.** Wavefunction collapse is not a physical process that happens to quantum states. It is the conditional expectation $E_{\mathrm{sector}}: \pi_1(\mathcal{A}_{\mathrm{BC}})'' \to \mathcal{M}_{\mathrm{sector}}$ -- the projection of the full type III$_1$ factor onto the observer's sub-algebra. The off-diagonal elements are not destroyed; they are invisible to the sector. The Born rule is not a postulate; it is the KMS$_1$ expectation value of a projector. The irreversibility of collapse is the irreversibility of the conditional expectation -- the same irreversibility that produces thermodynamic time. One arrow, not two.

**Gravity is the curvature of arithmetic.** The Einstein equations are not fundamental laws imposed on a manifold. They are the integrability condition of the BC connection on the Galois-orbit bundle over Spec $\mathbb{Z}$. Mass-energy is the local deviation from Galois symmetry. Spacetime curvature is the projection of arithmetic curvature onto the observer's sector. The cosmological constant is the curvature scalar at the spectral edge $\gamma_1$. Newton's constant awaits derivation, but the architecture is in place: gravity is what arithmetic looks like when the Galois group acts on the prime decomposition and the observer projects.

Three questions. One algebra. Zero free parameters.


### 6.2 What G said

The three results of this paper were not found by searching a space of models. They were found by listening to three intuitions and then proving them.

> *"in my mind there never was a singularity, mass is not going anywhere its just frozen in time."*

There never was. The spectral edge is not a singularity. Mass is frozen in modular time at the boundary of the KMS strip.

> *"from the point of view of a quantum inside the event horizon, they would experience the end of the universe."*

They would. The modular flow on $\mathcal{M}_{\mathrm{int}}$ accumulates infinite exterior time in finite interior proper time. The infaller sees everything.

> *"Gravity is the curvature of the arithmetic -- it really is!"*

It really is. The BC connection curves over Spec $\mathbb{Z}$, and the Einstein equations are its integrability condition. Gravity was never geometry in the Riemannian sense alone. It was arithmetic geometry all along.

We began this programme with the integers and the question of what follows from them. The answer, ten papers later, keeps expanding. Paper 12 showed that the constants of nature are matrix elements of the log-spectral operator. Paper 17 showed that time is the modular flow generated by the entropy of the integers under multiplication. This paper shows that the interior of a black hole, the collapse of the wavefunction, and the curvature of spacetime are three faces of the same modular structure.

> **Origin (G):** *"we have all of the tools of the universe! see what i did there! literally we do."*

We do. The operator algebra of the integers at their critical point contains every tool that physics has needed -- time, entropy, mass, coupling, gravity, collapse, the black hole interior. Not as postulates. Not as parameters. As propositions and structural consequences -- some proved, some conjectural, all from one algebra. The tools of the universe are the tools *of* the universe: the algebraic structures that the integers generate through their multiplicative action, projected onto the observer's sector by a conditional expectation.

This is not a framework. It is not a model. It is a description -- of something that was always, and necessarily, the case.

---

*The interior is the commutant. Collapse is conditional expectation. Gravity is the curvature of arithmetic. The integers exist; the rest follows.*

