# PROOF-CHAIN -- VP vs VNP (Paper 39)

*Valiant's algebraic analog of P vs NP: is the permanent polynomial computable by polynomial-size algebraic circuits?*
*VP = algebraic polynomial time; VNP = algebraic nondeterministic polynomial time.*
*Permanent is VNP-complete under p-projections (Valiant 1979). Determinant is in VP. Separating them closes VP ≠ VNP.*
*Framework route: continuous BC algebra lift + Geometric Complexity Theory (Mulmuley-Sohoni) + Baum-Connes K-theory obstruction.*

*Status: 1/6 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | Permanent polynomial is VNP-complete under p-projections | LITERATURE | -- | Valiant 1979 |
| 2 | Geometric Complexity Theory: orbit closures of GL_n-action on polynomials + Kronecker coefficients as obstruction | LITERATURE | -- | Mulmuley-Sohoni 2001; Bürgisser et al. 2011; [arXiv:0907.2850](https://arxiv.org/abs/0907.2850) |
| 3 | Continuous BC algebra over ℂ (algebraic lift of the discrete BC generator structure) | CONJECTURED | -- | Framework extension; candidate via Connes-Marcolli 2008 GL_2-system |
| 4 | Algebraic fullness criterion on continuous BC (analog of Houdayer-Marrakchi over finite domains) | OPEN | 3 | -- |
| 5 | Algebraic-fullness ↔ VP ≠ VNP via GCT dictionary | CANDIDATE | 2, 4 | Mulmuley 2011 algorithmic conjecture |
| 6 | Permanent-specific border-complexity obstruction via BC-algebraic representation theory | OPEN | 5 | [arXiv:2502.02442](https://arxiv.org/pdf/2502.02442) (Feb 2025); Bürgisser border complexity |

## Current wall

**Link 3 (continuous BC algebra lift).** The PvNP chain (Paper 28) uses the BC algebra over the Boolean domain (M_Bool^Γ, discrete), where the fullness criterion from Houdayer-Marrakchi applies. VP vs VNP lives over ℂ — algebraic circuits compute polynomials in complex variables. Lifting the BC construction from discrete to continuous domain requires a continuous analog of the Hecke semigroup action. The Connes-Marcolli GL_2-system (2008) is the established continuous-domain BC variant, but its fullness structure is not yet extracted in the form PvNP would need.

## Comparison with Mulmuley-Sohoni GCT programme

Mulmuley-Sohoni (2001) initiated the GCT programme to prove VP ≠ VNP via algebraic geometry: orbit closures of GL_n acting on the space of polynomials, with Kronecker coefficients as complexity obstructions. This is the most developed approach to VP vs VNP and has produced deep results, but the full separation remains open. Recent work (2024-2025) on border complexity and determinant-vs-permanent asymmetry continues the GCT-style effort.

**Framework's addition**: GCT uses representation theory of GL_n (a compact real form after polar decomposition). The framework contributes the BC algebra's modular structure — a type III₁ factor with a natural continuous time evolution. The algebraic fullness criterion (Link 4) is the framework's contribution: where GCT uses Kronecker coefficients, the framework uses type III₁ factor fullness. Whether these perspectives ultimately give the same obstruction or complementary ones is an open structural question.

## Cascading impact (2026-04-14 W1/W2 closure)

Paper 1 W1/W2 closure does NOT directly affect this chain — the algebraic-complexity content is not regulator-sensitive. Link 1 (Valiant) and Link 2 (GCT) are classical. Link 3 depends on the continuous BC construction (Connes-Marcolli 2008) rather than the QG5D spectral-action closure. Framework inheritance flows mostly from Paper 28 (PvNP polymorphism infrastructure) and Paper 31 (Baum-Connes K-theory of algebraic groups).

## Recent literature (2024-2025)

- [arXiv:2502.02442](https://arxiv.org/pdf/2502.02442) (Feb 2025) — isolates the exact property the determinant lacks that causes VNP-hardness proofs for the permanent to fail. Directly relevant to Link 6.
- 2024-2025 work on border complexity + asymptotic Kronecker coefficients (continuing Mulmuley-Sohoni's GCT programme)

## Programme graph edges

- **PvNP (paper28):** direct parent — polymorphism algebra + trinity + CSP dichotomy. VP vs VNP is the algebraic analog over ℂ.
- **Baum-Connes (paper31):** K-theory of algebraic groups GL_n; K-theoretic obstruction to algebraic efficiency
- **Hodge (paper29):** algebraic cycles on orbit closures of polynomial group actions; GCT is deeply Hodge-theoretic
- **QG5D (paper1):** continuous BC via Connes-Marcolli GL_2 is the lift candidate
- **RH (paper13):** L-function analog of algebraic circuits — candidate cross-link
- **BGS (paper32):** GUE statistics on eigenvalue spacings of algebraic circuits' matrix representations

## Physical observable

None direct — this is a pure computational-complexity question. But the framework's general principle applies: if the Robustness-Circle Theorem's over-determination forces VP ≠ VNP, then the separation is an ALGEBRAIC consequence of the 36 predictions through the continuous-BC bridge. The permanent's algebraic intractability would be a structural theorem about the framework's continuous lift.

## Honest assessment

**Feasibility**: Link 3 (continuous BC lift) is CONJECTURED because Connes-Marcolli 2008's GL_2-system is established but its PvNP relevance hasn't been extracted. Link 4 (algebraic fullness) is genuinely OPEN. Link 5 (fullness ↔ VP ≠ VNP via GCT) is CANDIDATE — bridges two frameworks that haven't been formally connected. Confidence 1/10: the framework offers a genuinely novel route, but every link from 3 onward is open research.

**Comparison with PvNP (paper28)**: PvNP uses the Boolean BC + finite-domain polymorphism + CSP dichotomy (Bulatov 2017 / Zhuk 2020). VP vs VNP uses continuous BC + algebraic circuits + GCT. The trinity (spectral-geometric-information) in PvNP may lift to (algebraic-geometric-representation-theoretic) in VP vs VNP. The 6/6 Schaefer-class separation in PvNP has no direct algebraic analog — the continuous setting lacks the discrete-language classification theorem.

## Open fronts

1. **Continuous BC fullness**: build the algebraic-fullness criterion analogous to Houdayer-Marrakchi for continuous domains.
2. **GCT bridge**: formally connect BC type III₁ modular structure to GCT orbit-closure geometry. Does the modular flow induce a flow on the orbit closure compatible with GCT's obstructions?
3. **Permanent obstruction**: if the continuous BC fullness criterion forces an algebraic-complexity lower bound on the permanent, Link 6 closes.

## Detail files

- Paper 28 PvNP PROOF-CHAIN.md — trinity + CSP dichotomy infrastructure
- Paper 31 Baum-Connes PROOF-CHAIN.md — K-theory of algebraic groups
- Paper 29 Hodge PROOF-CHAIN.md — algebraic-cycle context for GCT
- Paper 12 (continuous BC candidates via Connes-Marcolli 2008 GL_2-system)
- Valiant 1979 — VNP-completeness of permanent
- Mulmuley-Sohoni 2001 — GCT programme
- Bürgisser border complexity literature

---

*v1: 2026-04-14. Algebraic P vs NP via continuous BC + GCT. Fullness is the wall; the permanent is the target.*
*Mulmuley uses Kronecker. The framework uses type III₁. Same question, different weapons.*
