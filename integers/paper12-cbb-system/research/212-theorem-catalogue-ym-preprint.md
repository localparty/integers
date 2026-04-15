# 212 — Theorem Catalogue: Yang-Mills Preprint

*Source: `/Users/gsix/yang-mills/preprint/`*
*Compiled: 2026-04-09*
*Purpose: Integers theorem catalogue — every theorem/lemma/proposition
in the YM mass gap preprint, with RH relevance scoring.*

---

## Notation

- **Status**: Proved / Conditional / Literature / Heuristic
- **RH relevance** (0--5): does this theorem use or constrain the
  T_BC operator structure that RH depends on?
  - 0 = no connection
  - 1 = tangential (same mathematical tools)
  - 2 = shares spectral scaffold (KK/Epstein machinery)
  - 3 = constrains operator properties used by BC algebra
  - 4 = directly involves BC-adjacent spectral data
  - 5 = theorem about T_BC or its spectrum

---

## I. Main Text Theorems (Sections 4--5)

### Theorem 1 — Internal spectral gap
- **Statement**: The Hessian of the internal YM action at $A=0$ on
  $\mathbb{CP}^{N-1}$ satisfies $\mathrm{Hess} \geq \mu_1/g_{\mathrm{int}}^2$
  with $\mu_1 \geq 2N/r_3^2$.
- **Status**: Proved (Weitzenboeck identity + Fubini-Study curvature)
- **Source**: Section 4.2
- **RH relevance**: 1 (spectral gap on internal space; same class of
  Laplacian estimates but on CP^{N-1}, not BC Hilbert space)

### Theorem 2 — Bond activity bound
- **Statement**: In the $k=0$ topological sector, bond activities satisfy
  $|g_{\langle xy\rangle}| \leq C_0 e^{-m_1 a}$ with
  $m_1 = 2\sqrt{N}/r_3$.
- **Status**: Proved
- **Source**: Section 4.3
- **RH relevance**: 0

### Theorem 3 — Cluster expansion convergence
- **Statement**: The cluster expansion converges absolutely when
  $2\beta + \alpha < m_1 a/6 - \ln(c_d K C_0^{1/6})$.
- **Status**: Proved (Kotecky-Preiss criterion)
- **Source**: Section 4.3
- **RH relevance**: 0

### Theorem 4 — Lattice mass gap
- **Statement**: For SU($N$) lattice gauge theory on $\Lambda_L$
  enhanced with $\mathbb{CP}^{N-1}$ harmonics in the $k=0$ sector,
  with $r_3/a < \sqrt{3/(4N)}$: the cluster expansion converges,
  free energy is analytic, correlators decay exponentially, string
  tension $\sigma_0 > 0$, and mass gap $\Delta_0 \geq c\sqrt{\sigma_0} > 0$.
- **Status**: Proved (assembles Theorems 1--3)
- **Source**: Section 4.4
- **RH relevance**: 1 (establishes the starting gap that the RG preserves)

### Theorem 5 — IR equivalence with standard Yang-Mills
- **Statement**: The standard SU($N$) Wilson lattice gauge theory has
  $\Delta_0^{\mathrm{std}} \geq \Delta_0^{\mathrm{KK}} - C e^{-m_1 a} > 0$
  in the regime $m_1 a \gg 1$.
- **Status**: Proved (reduced transfer matrix + Feshbach projection)
- **Source**: Section 4.5
- **RH relevance**: 2 (the KK scaffold removal mirrors the spectral
  scaffold structure that connects to BC; proves the scaffold is
  removable without destroying the gap)

### Theorem 6 — Lattice power counting (partial)
- **Statement**: The irrelevant remainder $E_k$ satisfies:
  (a) first moment vanishes (proved); (b) zeroth moment vanishes
  (operator identity, proved in Section 5.6); (c) $|\hat{E}_k(q)| \leq C g_k^4 |q|^2$.
- **Status**: Proved (parts a,b exact; part c conditional on a+b)
- **Source**: Section 5.2
- **RH relevance**: 0

### Theorem 7 — Perturbative form factor bound
- **Statement**: To all orders in $g_k$, the connected one-particle
  matrix element of $E_k$ satisfies
  $|\langle 1|E_k(0)|1\rangle_c| \leq C_7 g_k^4 \hat{\Delta}_{k+1}^2$.
- **Status**: Proved (perturbative, all orders)
- **Source**: Section 5.3
- **RH relevance**: 0

### Theorem 8 — Continuum mass gap
- **Statement**: The mass gap survives the continuum limit:
  $\Delta_\infty > 0$, with OS axioms holding for the limiting theory.
- **Status**: Proved (unconditional; Conjecture 1 discharged in Section 5.6)
- **Source**: Section 5.7
- **RH relevance**: 3 (the continuum QFT whose existence is proved
  here is the same QFT whose operator algebra contains the BC
  spectral data; existence of $\Delta_\infty > 0$ constrains the
  spectrum of any operator built from the YM fields)

---

## II. Lemmas in Theorem 5 proof (Section 4.5)

### Lemma 1 — Well-definedness of reduced transfer matrix
- **Statement**: The partial trace $\hat{T}_{\mathrm{red}}$ converges
  absolutely and is bounded, self-adjoint, positive, trace-class.
- **Status**: Proved
- **Source**: Section 4.5
- **RH relevance**: 0

### Lemma 2 — Trace-norm bound
- **Statement**: $\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_1
  \leq C e^{-m_1 a}$.
- **Status**: Proved
- **Source**: Section 4.5
- **RH relevance**: 0

### Lemma 3 — Spectral perturbation
- **Statement**: The spectral gap shifts by at most the trace-norm
  difference.
- **Status**: Proved
- **Source**: Section 4.5
- **RH relevance**: 0

### Lemma 4 — Spectral gap of $\hat{T}_{\mathrm{red}}$
- **Statement**: $\Delta_0^{\mathrm{red}} \geq \Delta_0^{\mathrm{KK}} - C' e^{-m_1 a}$.
- **Status**: Proved
- **Source**: Section 4.5
- **RH relevance**: 0

---

## III. Appendix D — Reflection Positivity

### Lemma D.1 — RP on Riemannian product manifolds
- **Statement**: Reflection positivity holds for product manifolds
  when the reflection acts only on one factor.
- **Status**: Proved
- **Source**: Appendix D
- **RH relevance**: 0

### Lemma D.2 — RP for the KK lattice theory
- **Statement**: The KK-enhanced lattice gauge theory partition function
  satisfies reflection positivity.
- **Status**: Proved (Osterwalder-Seiler 1978)
- **Source**: Appendix D
- **RH relevance**: 0

---

## IV. Appendix I — Technical Supplements

### Lemma I.1 — Operator extraction
- **Statement**: Balaban's effective action $S_k[V]$ admits a decomposition
  into vacuum energy + $S_{\mathrm{YM}}/g_k^2$ + dimension $>4$ operators
  + remainder, with $k$-independent coefficient bounds.
- **Status**: Proved
- **Source**: Appendix I, Section I.1
- **RH relevance**: 0

### Lemma I.2 — Lattice Symanzik classification
- **Statement**: On the $d=4$ hypercubic lattice, dimension-6
  $\mathcal{C}$-even gauge-invariant operators are spanned by
  $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and EOM-redundant operators only.
- **Status**: Proved
- **Source**: Appendix I, Section I.2
- **RH relevance**: 0

### Lemma I.3.1 — N-dependence convergence
- **Statement**: For each fixed $N \geq 2$, the sum
  $\sum_k C_k g_k^4 \hat{\Delta}_k^2$ converges.
- **Status**: Proved (Gronwall + doubly exponential decay)
- **Source**: Appendix I, Section I.3
- **RH relevance**: 0

### Theorem I.4.1 — Universal mass gap
- **Statement**: For any compact simple Lie group $G$, pure $G$
  Yang-Mills theory in 4D has $\Delta_\infty > 0$.
- **Status**: Proved (uses compact irreducible symmetric spaces $G/H$
  as internal manifolds + Weitzenboeck-Bochner for universal spectral gap)
- **Source**: Appendix I, Section I.4
- **RH relevance**: 2 (universality over all compact simple groups
  constrains the operator-algebraic structure; the BC algebra
  uses $\mathrm{SU}(N)$ specifically but the universality is a
  structural constraint)

### Proposition I.4.2 — Requirements on internal space
- **Statement**: Requirements (R1)--(R3) for the KK mechanism are
  satisfied by any compact irreducible symmetric space $G/H$ of compact type.
- **Status**: Proved (Weitzenboeck-Bochner theorem)
- **Source**: Appendix I, Section I.4
- **RH relevance**: 1

---

## V. Appendix J — Lattice Symanzik Basis

### Theorem J.1 — Dimension-6 classification
- **Statement**: Every local, gauge-invariant, $\mathcal{C}$-even
  operator of engineering dimension 6 on the $d=4$ lattice is a linear
  combination of $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and EOM-related operators.
- **Status**: Proved
- **Source**: Appendix J
- **RH relevance**: 0

---

## VI. Appendix L — Gradient-Flow Closure (Clay Conjectures L.1--L.4)

### Theorem L.0 — Gradient-flow closure
- **Statement**: The YM gradient flow on the KK-enhanced lattice, composed
  with Balaban analyticity and Epstein zeta vanishing, closes Conjectures
  L.1--L.4 (modulo H4 for AF-specific results).
- **Status**: Proved (unconditional for L.1(i-ii), L.3, L.4 structure;
  conditional on H4 for L.1(iii), L.2, L.4 AF form)
- **Source**: Appendix L, Section L.0
- **RH relevance**: 3 (the renormalised composite operators constructed
  here are the same operators from which T_BC matrix elements are built)

### Theorem L.6.1 — Unconditional closures
- **Statement**: L.1(i-ii), L.3(i-v), and L.4 non-perturbative structure
  hold unconditionally for SU($N$), $N \geq 2$.
- **Status**: Proved
- **Source**: Appendix L, Section L.6
- **RH relevance**: 3

### Theorem L.6.2 — Conditional closures
- **Statement**: Assuming H4, the anomalous dimension, short-distance
  asymptotics, and AF form of the OPE hold.
- **Status**: Conditional on H4
- **Source**: Appendix L, Section L.6
- **RH relevance**: 2

---

### Stage I: Flow well-posedness and small-field preservation

### Lemma L.1.1 — Flow well-posedness
- **Statement**: The YM gradient flow $\partial_t B_\mu = D_\nu G_{\nu\mu}$
  on the KK-enhanced lattice is globally well-posed, gauge-covariant,
  and the action is a Lyapunov function.
- **Status**: Proved
- **Source**: Appendix L, Section L.1
- **RH relevance**: 2 (flow = heat equation; the heat kernel is the
  same object controlling BC partition function asymptotics)

### Lemma L.1.2 — Flow preserves small-field domain
- **Statement**: The gradient flow preserves Balaban's small-field domain
  $\Omega_s$ for all $t \geq 0$.
- **Status**: Proved
- **Source**: Appendix L, Section L.1
- **RH relevance**: 1

### Lemma L.1.3 — Flowed polymer activity decay
- **Statement**: Flowed polymer activities satisfy exponential decay
  $|K_k^t(X,V)| \leq e^{-\kappa(t)|X|}$ with $\kappa(t) > 0$.
- **Status**: Proved
- **Source**: Appendix L, Section L.1
- **RH relevance**: 1

### Lemma L.1.4 — K-uniformity of flowed constants
- **Statement**: The constants $\kappa(t)$ and $C(t)$ in Lemma L.1.3
  are independent of the bare-scale index $K$.
- **Status**: Proved
- **Source**: Appendix L, Section L.1
- **RH relevance**: 1

### Lemma L.1.5 — Flow contractivity on KK background
- **Statement**: The gradient flow is contractive: action decreases
  monotonically, instanton contributions are exponentially suppressed,
  and the $\omega$-limit set consists of flat connections.
- **Status**: Proved
- **Source**: Appendix L, Section L.1
- **RH relevance**: 2 (contractivity of heat flow is a key property
  shared with the BC partition function analysis)

---

### Stage II: Continuum flowed limit

### Lemma L.2.1 — Cauchy estimate for flowed Schwinger functions
- **Statement**: Flowed Schwinger functions at fixed $t > 0$ form a
  Cauchy sequence in the continuum limit $a \to 0$.
- **Status**: Proved
- **Source**: Appendix L, Section L.2
- **RH relevance**: 1

### Lemma L.2.2 — Uniqueness of continuum flowed limit
- **Statement**: The continuum limit of flowed Schwinger functions is
  unique (not subsequential), via a Cauchy argument.
- **Status**: Proved
- **Source**: Appendix L, Section L.2
- **RH relevance**: 1

### Lemma L.2.3 — OS axioms for flowed Schwinger functions
- **Statement**: The continuum flowed Schwinger functions satisfy
  OS0--OS4 at each fixed $t > 0$.
- **Status**: Proved
- **Source**: Appendix L, Section L.2
- **RH relevance**: 2 (OS axioms are the foundation for the Hilbert
  space on which T_BC acts)

### Lemma L.2.4 — OS reconstruction at fixed flow time
- **Statement**: OS reconstruction uniquely determines a Hilbert space,
  Hamiltonian, and vacuum from the flowed Schwinger functions at fixed $t > 0$.
- **Status**: Proved
- **Source**: Appendix L, Section L.2
- **RH relevance**: 2

---

### Stage III: Small-flow-time limit and composite operators

### Lemma L.3.1 — Analyticity in $t$
- **Statement**: The flowed Schwinger functions are analytic in flow
  time $t$ with $(k,K)$-uniform radius.
- **Status**: Proved
- **Source**: Appendix L, Section L.3
- **RH relevance**: 3 (analyticity in flow time = analyticity in
  the heat kernel parameter; this is the same analytic structure
  that controls the BC partition function's critical behaviour)

### Lemma L.3.2 — No operator mixing at dimension 4
- **Statement**: The unique local, gauge-invariant, $\mathcal{C}$-even,
  parity-even operator of dimension 4 is $S_{\mathrm{YM}}$; no mixing
  occurs at this dimension.
- **Status**: Proved
- **Source**: Appendix L, Section L.3
- **RH relevance**: 0

### Lemma L.3.3 — Deviation order $\geq 2$ at dimension 6
- **Statement**: All $\mathcal{C}$-even, gauge-invariant dimension-6
  operators have deviation order $\mathrm{dev} \geq 2$.
- **Status**: Proved
- **Source**: Appendix L, Section L.3
- **RH relevance**: 0

### Lemma L.3.4 — KK mode sum vanishing at $t = 0$
- **Statement**: KK mode sums at $t = 0$ vanish by Theorem K.1
  (Epstein zeta at non-positive integers).
- **Status**: Proved
- **Source**: Appendix L, Section L.3
- **RH relevance**: 4 (the Epstein zeta vanishing $E_L(-j;Q) = 0$
  via $1/\Gamma(-j) = 0$ is structurally identical to the mechanism
  that controls the BC partition function at $\beta = 1$; both use
  the Gamma function poles at non-positive integers)

### Lemma L.3.5 — $\mathbb{Z}_2$ parity cancellation persists
- **Statement**: The $\mathbb{Z}_2$ cancellation between even and odd
  KK sectors persists at all flow times.
- **Status**: Proved
- **Source**: Appendix L, Section L.3
- **RH relevance**: 1

### Lemma L.3.6 — Goroff-Sagnotti coefficient vanishes
- **Statement**: The Goroff-Sagnotti counterterm coefficient vanishes
  in all regularisation schemes.
- **Status**: Proved
- **Source**: Appendix L, Section L.3
- **RH relevance**: 2 (scheme-independence via Wess-Zumino
  cohomological protection; similar cohomological constraints
  apply to the BC algebra)

### Lemma L.3.7 — Cauchy estimate (core estimate)
- **Statement**: The double limit $(a,t) \to (0,0)$ commutes; the
  small-flow-time expansion has $K$-uniform Lipschitz continuity
  and forms a Cauchy net.
- **Status**: Proved (Moore-Osgood theorem)
- **Source**: Appendix L, Section L.3
- **RH relevance**: 3 (this is the key technical lemma making the
  gradient flow programme rigorous; the same double-limit
  commutation is needed for the BC flow-time analysis)

### Lemma L.3.8 — Extraction of $[\mathrm{Tr}\,F^2]_R$
- **Statement**: The renormalised composite operator
  $[\mathrm{Tr}\,F^2]_R$ exists as an operator-valued distribution
  with finite tempered Schwinger functions satisfying OS positivity,
  Euclidean invariance, and clustering.
- **Status**: Proved (unconditional)
- **Source**: Appendix L, Section L.3
- **RH relevance**: 4 (the operator $[\mathrm{Tr}\,F^2]_R$ is a
  spectral observable of the QFT; in the Integers programme, T_BC
  matrix elements are built from precisely such renormalised
  composite operators. Its existence as an operator-valued
  distribution constrains the operator algebra that T_BC lives in.)

### Lemma L.3.9 — KK-to-4D projection for composite operators
- **Statement**: KK-enhanced composite operator Schwinger functions
  match 4D ones up to $O(e^{-m_1 r_{\min}})$ corrections.
- **Status**: Proved (Feshbach projection)
- **Source**: Appendix L, Section L.3
- **RH relevance**: 2

---

### Stage IV: Short-distance match and OPE

### Lemma L.4.1 — Stress-energy tensor via Suzuki formula
- **Statement**: $T_{\mu\nu}^R$ exists and satisfies symmetry, gauge
  invariance, distributional conservation, positive Hamiltonian
  identification ($H_{\mathrm{OS}} \geq 0$, $H_{\mathrm{OS}}\Omega = 0$),
  and the trace anomaly.
- **Status**: Proved (unconditional)
- **Source**: Appendix L, Section L.4
- **RH relevance**: 3 (the stress tensor determines the Hamiltonian
  $H_{\mathrm{OS}}$ whose spectral properties are ultimately connected
  to T_BC via the QG5D bridge)

### Lemma L.4.2 — Anomalous dimension and short-distance asymptotics
- **Statement**: $\gamma_{\mathrm{Tr}\,F^2} = 2b_0 g^2 + O(g^4)$
  and $S_2^{\mathrm{ren}} \sim C_N |x|^{-8} (\log)^{-2}$.
- **Status**: Conditional on H4
- **Source**: Appendix L, Section L.4
- **RH relevance**: 2

### Lemma L.4.3 — Leading-order OPE
- **Statement**: The identity-channel OPE coefficient is
  $C^{\mathbb{1}} = C_N |x|^{-8}(\log)^{-2}$; subleading channels
  are strictly weaker. AF form conditional on H4.
- **Status**: Proved (structure unconditional; AF form conditional on H4)
- **Source**: Appendix L, Section L.4
- **RH relevance**: 2

---

## VII. Appendix M — Gap Closures

### Lemma M.1.1 — K-uniform cluster expansion rate
- **Statement**: The cluster expansion of Theorem 4 converges with
  physical rate $\kappa_{\mathrm{cl}}^{\mathrm{phys}} = m_1/6$,
  independent of the bare-scale index $K$.
- **Status**: Proved
- **Source**: Appendix M, Section M.1
- **RH relevance**: 0

### Lemma M.1.2 — K-uniform Balaban analyticity radius
- **Statement**: Polymer activities satisfy $|K_k^{(K)}(X,V)| \leq
  e^{-\kappa_{\mathrm{B}}|X|}$ with $\kappa_{\mathrm{B}}$ independent
  of both $k$ and $K$.
- **Status**: Proved
- **Source**: Appendix M, Section M.1
- **RH relevance**: 0

### Theorem M.2.1 — Uniqueness of the continuum limit
- **Statement**: The Schwinger functions $S_n^{(a)}(f)$ converge (not
  just subsequentially) to unique tempered distributions as $a \to 0$.
- **Status**: Proved (Cauchy net + doubly exponential convergence)
- **Source**: Appendix M, Section M.2
- **RH relevance**: 3 (uniqueness of the continuum QFT means the
  operator algebra is unique, which constrains T_BC)

---

## VIII. Appendix N — QG5D Infrastructure

### Theorem K.1 — Universal Epstein vanishing (Paper 1)
- **Statement**: For any positive-definite quadratic form $Q$ in $L$
  variables, $E_L(-j; Q) = 0$ for all integers $j \geq 1$.
- **Status**: Proved (via $1/\Gamma(-j) = 0$)
- **Source**: Paper 1, Appendix K; reproduced in Appendix N, Section N.1.5
- **RH relevance**: 5 (the $1/\Gamma(-j) = 0$ mechanism is the SAME
  functional equation structure that controls the Riemann zeta at
  negative integers; the Epstein zeta is the multi-dimensional
  generalisation of the Riemann zeta; this vanishing is the
  number-theoretic core connecting the YM UV finiteness to the
  analytic structure of $\zeta(s)$)

### Theorem S.1 — Perturbative finiteness (Paper 1)
- **Statement**: The $L$-loop effective action for linearised 5D gravity
  on $M^4 \times S^1$ is finite at every order, with $S_0^{(L)} = 0$
  and all subleading KK sums holomorphic.
- **Status**: Proved
- **Source**: Paper 1, Appendix S; reproduced in Appendix N, Section N.1.6
- **RH relevance**: 3 (uses $\zeta_R(0) = -1/2$ and Epstein-Terras
  analytic continuation — the same zeta-function machinery)

### Theorem U.2a — Seeley-DeWitt coefficient vanishing (Paper 10)
- **Statement**: $a_2 = a_4 = 0$ for the Lichnerowicz operator on
  flat $M^4 \times S^1/\mathbb{Z}_2$.
- **Status**: Proved (all Vassilevich formula ingredients vanish on flat background)
- **Source**: Paper 10, Section 2.5; reproduced in Appendix N, Section N.2.1
- **RH relevance**: 3 (heat kernel coefficients control the BC
  partition function's high-temperature expansion; their vanishing
  is a constraint on the spectral geometry)

### Proposition 3.1 — $\mathbb{Z}_2$ parity cancellation (Paper 10)
- **Statement**: For each KK level $n \geq 1$,
  $f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0$ exactly.
- **Status**: Proved
- **Source**: Paper 10, Section 3.3; reproduced in Appendix N, Section N.2.2
- **RH relevance**: 2

### Lemma A1 — Vertex numerator KK-independence (Paper 10)
- **Statement**: The 5D three-graviton vertex numerator introduces no
  $n$-dependent terms at leading UV order after KK decomposition.
- **Status**: Proved
- **Source**: Paper 10, Section 4.6; reproduced in Appendix N, Section N.2.3
- **RH relevance**: 1

### Lemma A2 — Goroff-Sagnotti UV subleading (Paper 10)
- **Statement**: Graviphoton and radion contributions to the
  Goroff-Sagnotti operator are dimension-8 or higher, UV-subleading.
- **Status**: Proved
- **Source**: Paper 10, Section 4.6; reproduced in Appendix N, Section N.2.3
- **RH relevance**: 1

### Lemma A3 — KK loop sum (Paper 10)
- **Statement**: The internal KK loop sum gives
  $S_0 = 1 + 2\zeta_R(0) = 0$.
- **Status**: Proved
- **Source**: Paper 10, Section 4.6; reproduced in Appendix N, Section N.2.3
- **RH relevance**: 4 (directly uses $\zeta_R(0) = -1/2$)

### Theorem 1 (Paper 10) — Goroff-Sagnotti vanishing in all schemes
- **Statement**: The Goroff-Sagnotti coefficient $C_{\mathrm{GS}}$
  vanishes identically in all regularisation schemes.
- **Status**: Proved (unconditional within linearised 5D gravity)
- **Source**: Paper 10, Section 4.6; reproduced in Appendix N, Section N.2.4
- **RH relevance**: 3

### Theorem 4.3 — Weyl anomaly scheme-independence (Paper 10)
- **Statement**: $a_{\mathrm{total}} = c_{\mathrm{total}} = 0$ for the
  full KK graviton tower, in any scheme preserving diffeomorphism
  invariance and UV operator algebra.
- **Status**: Proved (Wess-Zumino consistency + $S_0 = 0$)
- **Source**: Paper 10, Section 4.5; reproduced in Appendix N, Section N.2.5
- **RH relevance**: 3 (Weyl anomaly = trace of stress tensor;
  its vanishing via $S_0 = 0$ is a direct consequence of $\zeta_R(0)$)

### Proposition A.1 — Frozen dilaton (Paper 6)
- **Statement**: The dilaton potential is $V(R) = +c/R^4$ with $c > 0$,
  exact to all perturbative orders; $\Delta R/R_0 \approx 3 \times 10^{-30}$.
- **Status**: Proved
- **Source**: Paper 6, Appendix A; reproduced in Appendix N, Section N.3
- **RH relevance**: 1

---

## IX. Hypothesis H4 (the single open input)

### Hypothesis H4 — Non-perturbative = perturbative at short distances
- **Statement**: The non-perturbative Schwinger functions constructed
  via Lemma L.3.8 admit a short-distance asymptotic expansion whose
  leading term matches the perturbative prediction.
- **Status**: Open (standard assumption of QCD phenomenology)
- **Source**: Appendix L, Section L.7
- **RH relevance**: 2

---

## X. Conjecture 1 (discharged)

### Conjecture 1 — Non-perturbative form factor bound
- **Statement**: $|\delta\hat{\Delta}_k| \leq C g_k^4 (a_k \Delta)^s$
  with $s \geq 2$, non-perturbatively.
- **Status**: Proved (discharged in Section 5.6 via (B1)-(B2) +
  dimension-6 classification)
- **Source**: Section 5.4 (stated), Section 5.6 (discharged)
- **RH relevance**: 0

---

## Summary Statistics

| Category | Count |
|:---------|------:|
| Main text theorems (1--8) | 8 |
| Lemmas in Theorem 5 proof | 4 |
| Appendix D lemmas | 2 |
| Appendix I lemmas/theorems | 5 |
| Appendix J theorems | 1 |
| Appendix L lemmas/theorems | 24 |
| Appendix M lemmas/theorems | 3 |
| Appendix N theorems (from Papers 1, 6, 10) | 10 |
| Hypotheses (open) | 1 |
| Conjectures (discharged) | 1 |
| **Total entries** | **59** |

### RH Relevance Distribution

| Score | Count | Key items |
|:------|------:|:----------|
| 5 | 1 | Theorem K.1 (Epstein vanishing via $1/\Gamma(-j)$) |
| 4 | 3 | Lemma L.3.4, Lemma L.3.8, Lemma A3 |
| 3 | 10 | Theorems 8, L.0, L.6.1, M.2.1, S.1, U.2a, 1(P10), 4.3(P10); Lemmas L.3.1, L.3.7, L.4.1 |
| 2 | 9 | Theorems 5, I.4.1, L.6.2; Lemmas L.1.5, L.2.3, L.2.4, L.3.6, L.3.9, L.4.2, L.4.3; Prop 3.1; H4 |
| 1 | 9 | Theorems 1, 4; Lemmas L.1.2--L.1.4, L.3.5; Props I.4.2, A.1; Lemmas A1, A2 |
| 0 | 27 | Remaining entries |
| **RH-relevant (score >= 3)** | **14** | |
