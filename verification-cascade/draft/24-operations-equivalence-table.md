# 24 — The Operations Equivalence Table

---

## The translation dictionary for mathematical operations

The correspondence table (Section 15) maps CONCEPTS across domains — "the mass gap" looks like a spectral gap spectrally, a curvature bound geometrically, a polymer convergence algebraically. But concepts are not enough. An ORA agent needs to know how OPERATIONS translate — how to convert a proof STEP from one domain to another.

The operations equivalence table is this translation dictionary. Every mathematical operation used in a proof chain has equivalents in each active domain. When an agent knows the spectral form of an operation but needs the geometric form, the table provides the translation. When a proof step uses a commutator (spectral) and the agent needs to verify it as curvature (geometric), the table says: "[A,B] = AB-BA in the spectral domain IS the curvature R in the geometric domain."

## The master table

| Operation | Spectral | Geometric | Algebraic | Information |
|---|---|---|---|---|
| **Inner product** | Trace-class pairing: Tr(A*B) | Metric integration: integral of omega wedge *omega | Hom-space pairing: Hom(A,B) | Mutual information: I(X;Y) |
| **Tensor product** | Hilbert space tensor: H_1 tensor H_2 | Cartesian product: M_1 x M_2 | Algebra tensor: A tensor B | Joint distribution: P(X,Y) |
| **Direct sum** | Orthogonal decomposition: H = H_1 perp-sum H_2 | Disjoint union: M_1 disjoint-union M_2 | Module direct sum: M = M_1 direct-sum M_2 | Independent sources: H(X,Y) = H(X) + H(Y) |
| **Quotient** | Spectral restriction to invariant subspace | Orbifold: M/G | Ideal quotient: A/I | Conditional entropy: H(X|Y) |
| **Limit** | Spectral convergence: spec(T_n) -> spec(T) | Gromov-Hausdorff: d_GH(M_n, M) -> 0 | Direct/inverse limit: lim A_n | Rate-distortion: R(D) as D -> 0 |
| **Duality** | Adjoint: T <-> T* | Poincare duality: H^k <-> H^{n-k} | Pontryagin duality: G <-> G-hat | Source-channel duality: C_source <-> C_channel |
| **Gap / Distance** | Spectral gap: Delta = inf spec(H) \ {0} | Injectivity radius: r_inj(M) | Kazhdan constant: kappa(G) | Capacity gap: C - R |
| **Trace** | Operator trace: Tr(T) | Volume: Vol(M) | Dimension: dim(V) | Entropy: H(X) |
| **Commutator** | [A,B] = AB - BA | Curvature: R(X,Y) = nabla_X nabla_Y - nabla_Y nabla_X - nabla_{[X,Y]} | Lie bracket: [X,Y] in the Lie algebra | Interference: I(X;Y|Z) - I(X;Y) |
| **Projection** | Spectral projection: E_lambda | Restriction to submanifold: i*omega | Idempotent: e^2 = e | Conditional expectation: E[X|Y] |
| **Exponential** | Semigroup: e^{tA} | Exponential map: exp_p : T_pM -> M | Group exponential: exp : g -> G | Generating function: sum p_n z^n |
| **Derivative** | Commutator with generator: [H, .] | Covariant derivative: nabla_X | Derivation: d : A -> A | Score function: d/d(theta) log p(x;theta) |
| **Integration** | Trace against measure: integral T d mu | Integration of forms: integral_M omega | Averaging over group: integral_G f(g) dg | Expectation: E[X] = integral x dP(x) |
| **Conjugation** | Unitary conjugation: U T U* | Gauge transformation: A -> g A g^{-1} + g dg^{-1} | Inner automorphism: a -> u a u^{-1} | Channel action: rho -> sum K_i rho K_i* |
| **Fixed point** | Eigenvalue 1: T psi = psi | Fixed point of flow: phi_t(p) = p | Invariant element: g . a = a for all g | Maximum entropy state: argmax H(X) |
| **Completion** | Hilbert space completion | Cauchy completion of metric space | Algebraic closure / completion | Shannon limit |

## How agents use the table

**Scenario 1: Spectral proof step needs geometric verification.**

An agent verifying a proof step about the spectral gap Delta > 0 of a transfer matrix reads the "Gap / Distance" row:

- Spectral: Delta = inf spec(H) \ {0} — the proof claims this is positive
- Geometric: r_inj(M) — the injectivity radius of the corresponding manifold

The geometric check: if the spectral gap corresponds to the injectivity radius, the agent can verify Delta > 0 by showing r_inj > 0, which may be easier (geometric positivity is often visible from curvature bounds, while spectral positivity requires functional analysis).

**Scenario 2: Algebraic construction needs spectral translation.**

An agent in Tier B excision has independently proved a result using algebraic methods (a group-theoretic argument producing an idempotent e^2 = e). The "Projection" row translates: the algebraic idempotent corresponds to a spectral projection E_lambda. The agent translates the algebraic proof to spectral language, producing a second route (LOCK).

**Scenario 3: Information-theoretic bound constrains a spectral claim.**

An agent verifying a claim about operator trace reads the "Trace" row:

- Spectral: Tr(T) — the proof computes this
- Information: H(X) — the trace corresponds to entropy

If the claimed trace violates an entropy bound (e.g., H(X) <= log dim — the maximum entropy for a finite system), the claim is WRONG. The information-theoretic column provides a CONSTRAINT CHECK that the spectral computation alone cannot.

## Domain-specific extensions

When Tier 2 or Tier 3 domains are activated, the operations table grows with domain-specific entries:

### Operator algebra extensions (activated for CCM verification)

| Operation | OA form | Connection to pillars |
|---|---|---|
| Modular automorphism | sigma_t(a) = Delta^{it} a Delta^{-it} | Spectral: spectrum of log Delta. Geometric: KMS flow on state space. |
| Conditional expectation | E_N : M -> N (unique trace-preserving) | Info: E[X|Y]. Algebraic: projection onto subalgebra. |
| Jones index | [M:N] = dim_N(L^2(M)) | Algebraic: dim. Geometric: volume ratio. Info: channel capacity of inclusion. |
| Crossed product | M rtimes_alpha G | Algebraic: semidirect product. Geometric: total space of bundle. |

### Number theory extensions (activated for CCM and BSD verification)

| Operation | NT form | Connection to pillars |
|---|---|---|
| Euler product | prod_p (1 - p^{-s})^{-1} | Spectral: product over spectral points. Algebraic: product in Hecke algebra. |
| Functional equation | xi(s) = xi(1-s) | Geometric: reflection symmetry. Info: source-channel duality of zeta. |
| Hecke operator | T_p f(z) = sum f((az+b)/d) | Spectral: eigenvalue equation. Algebraic: algebra action. |
| L-function | L(s, chi) = sum chi(n) n^{-s} | Spectral: spectral zeta. Algebraic: character trace. Info: twisted partition function. |

### Constructive QFT extensions (activated for Balaban verification)

| Operation | CQFT form | Connection to pillars |
|---|---|---|
| Block-spin RG | T_k : fields at scale k -> fields at scale k+1 | Spectral: spectral decimation. Geometric: coarse-graining of lattice. |
| Polymer expansion | Z = sum_{polymers} w(gamma) | Algebraic: formal power series. Info: cluster expansion of partition function. |
| UV cutoff removal | lim_{Lambda -> inf} Z_Lambda | Spectral: limit of truncated spectra. Geometric: continuum limit. |

## The table as a problem-solving tool

The operations equivalence table is not just a reference — it is a PROBLEM-SOLVING TOOL with a specific workflow:

1. **Identify the operation** the proof step performs (e.g., "takes a commutator")
2. **Read the row** for that operation (Commutator row)
3. **Identify the domain** the proof works in (e.g., spectral: [A,B])
4. **Read across** to the other domains (geometric: curvature R; algebraic: Lie bracket; information: interference)
5. **Choose the domain** where the operation is EASIEST to verify or where alternative tools exist
6. **Translate the proof step** into the chosen domain
7. **Verify or re-derive** in the translated domain
8. **Translate back** if needed (the correspondence preserves truth)

This workflow turns a STUCK agent into a SEARCHING agent. "I can't verify this commutator spectrally" becomes "let me verify this as curvature geometrically." The table provides the dictionary for the translation. The correspondence ensures the translation is truth-preserving.

## Empty cells and the creativity frontier

Some cells in the operations table are empty — operations that have known forms in some domains but not others. Each empty cell is a RESEARCH TARGET:

- Modular automorphism with no known information-theoretic form: finding it would connect von Neumann algebra dynamics to information theory
- Euler product with no known geometric form: finding it would connect prime factorization to geometry (a Langlands-type correspondence)
- Block-spin RG with no known algebraic form: finding it would connect constructive QFT to abstract algebra

Filling an empty cell is a mathematical result. The verification cascade produces these results as byproducts — when an agent translates a proof step into a new domain and discovers that the operation doesn't have a known form there, the agent has identified a GAP in the mathematical literature. If the agent then FILLS the gap (by constructing the form), that is a new correspondence — a publishable result.

---

*The operations equivalence table translates PROOF STEPS between domains. Inner product, tensor product, quotient, limit, duality, gap, trace, commutator, projection — each mapped across all active domains. When an agent is stuck in one domain, read across the row and try another. Domain-specific extensions activate with Tier 2/3 domains. Empty cells are research targets — filling them IS mathematics. The table is not a reference. It is a problem-solving workflow: identify the operation, read the row, translate, verify, translate back.*
