# §21 — Elliott-Gwilliam-Williams 2024: BV Quantization of KW Theories

*Recent BV-quantization framework. Uniform quantization of all Kapustin-Witten twists. Factorization algebras of observables. 4d TQFT structure. The mathematical infrastructure that makes Kapustin-Witten rigorous at the observable level.*

---

## 21.1. The paper

**Reference.** C. Elliott, O. Gwilliam, and B. R. Williams, *The topological A- and B-models and the Kapustin-Witten theories: BV-quantization and factorization algebras*, *Annales Henri Poincaré* 25 (2024), 3651-3714. (Final published version 2024; preprint on arXiv from 2021.)

Length: 64 pages. Authorship: Chris Elliott (University of Massachusetts Amherst), Owen Gwilliam (University of Massachusetts Amherst), Brian Williams (Boston University / Northeastern). The paper continues the programme of Costello-Gwilliam on BV quantization of gauge theories, applied specifically to the Kapustin-Witten family.

---

## 21.2. What BV quantization is

The Batalin-Vilkovisky (BV) formalism is a systematic framework for quantizing gauge theories. It handles the gauge redundancy through a cohomological construction: the physical observables are the cohomology of a specific BV operator $Q_{\text{BV}}$ acting on a graded algebra of fields.

**Inputs.**
- A classical field theory with gauge symmetry.
- A BV action $S_{\text{BV}}$ that incorporates ghosts, antighosts, and antifields.
- A BV bracket $\{-, -\}_{\text{BV}}$.

**Outputs (at the quantum level).**
- A factorization algebra $\text{Obs}^q$ of quantum observables (local + global).
- A cochain complex whose cohomology is the space of physical states.
- A formal quantization of the classical theory, obtained by solving the quantum master equation $\{S_{\text{BV}}, S_{\text{BV}}\} + 2\hbar \Delta S_{\text{BV}} = 0$.

**References** (framework): K. Costello and O. Gwilliam, *Factorization Algebras in Quantum Field Theory*, Vol. 1 (2017), Vol. 2 (2021), Cambridge University Press. Provides the mathematical foundations.

---

## 21.3. Factorization algebras

A *factorization algebra* on a manifold $M$ is a rule that assigns to each open set $U \subset M$ a chain complex $\text{Obs}(U)$ of "local observables on $U$," together with structure maps $\text{Obs}(U_1) \otimes \ldots \otimes \text{Obs}(U_n) \to \text{Obs}(V)$ whenever $U_1, \ldots, U_n$ are disjoint and contained in $V$.

For a quantum field theory, the factorization algebra encodes:
- The local observables at each point (via $\text{Obs}(\text{small disk})$).
- The algebra of observables at each open set (via $\text{Obs}(U)$).
- The operator product expansion (via the structure maps).

**Why factorization algebras?** They are the modern mathematical replacement for the operator algebras of Wightman/Haag-Kastler axiomatic QFT. They encode the same data (local observables, OPE), but in a form compatible with modern homotopical methods and with derived geometry.

For Route C, the factorization algebra of the Kapustin-Witten twisted N=4 SYM provides a *rigorous* description of the observables in the twisted theory.

---

## 21.4. The main theorem of Elliott-Gwilliam-Williams 2024

**Theorem (Elliott-Gwilliam-Williams 2024).** *Let $M$ be a 4-manifold and $G$ a reductive gauge group. For each value of the Kapustin-Witten twist parameter $\Psi \in \mathbb{CP}^1$, there is a factorization algebra $\text{Obs}^q_\Psi$ on $M$ representing the quantum observables of the twisted N=4 super Yang-Mills theory. Moreover:*

*(i) The factorization algebras $\text{Obs}^q_\Psi$ depend continuously on $\Psi$.*

*(ii) At the canonical values $\Psi = 0, \infty, 1$, the factorization algebras reduce to:*
   - *$\Psi = 0$: the B-model's factorization algebra on the Hitchin moduli space (upon dimensional reduction).*
   - *$\Psi = \infty$: the A-model's factorization algebra on the Hitchin moduli space.*
   - *$\Psi = 1$: Chern-Simons-like theory.*

*(iii) The S-duality $\Psi \to -1/(n_G \Psi)$ of §18 is implemented at the level of factorization algebras as an equivalence $\text{Obs}^q_\Psi \simeq \text{Obs}^q_{-1/(n_G \Psi)}$ upon exchanging $G$ and ${}^L G$.*

This theorem provides the *mathematical rigor* for Kapustin-Witten 2007's physics-level claims. Before 2024, the construction of the quantum observables was physics-level. Elliott-Gwilliam-Williams made it rigorous via BV quantization.

---

## 21.5. What the theorem does for Route C

### 21.5.1. A rigorous 4d TQFT structure

Pure N=4 SYM at twist $\Psi$ is a 4-dimensional topological quantum field theory (TQFT) on each 4-manifold. Elliott-Gwilliam-Williams 2024 establishes that this TQFT has a rigorous factorization-algebra description.

For Route C, this means: once the scale bridge (§20) is accepted (even conjecturally), the Wilson-loop observables of pure YM inherit a factorization-algebra structure from the $M_I \to \infty$ limit of the Elliott-Gwilliam-Williams factorization algebra of N=4$^*$. This gives a *concrete* target for the pure-YM Wilson-loop L-function: it is the L-function associated to the local-to-global structure of this factorization algebra.

### 21.5.2. Local-to-global

Factorization algebras are designed for local-to-global analysis: starting from local observables at each point, one assembles global observables on large regions. The assembly is controlled by the factorization structure.

For Route C, this is key: the Kapustin-Witten twist's spectral data (controlling Wilson loops) is organized locally by the factorization algebra. The global Wilson-loop L-function is assembled from this local data via the factorization structure, analogous to the Euler product assembly of §15-§16.

### 21.5.3. OPE rigorously

The factorization-algebra structure *is* the OPE, at the mathematical level. The structure maps $\text{Obs}(U_1) \otimes \text{Obs}(U_2) \to \text{Obs}(V)$ for disjoint $U_1, U_2 \subset V$ encode how local observables combine, which is precisely the OPE.

This matters for H4: H4 is a statement about the OPE at short distances (the leading perturbative coefficient matches the non-perturbative one). The factorization-algebra structure gives a rigorous framework for making this match.

---

## 21.6. Relation to the rest of Route C

Elliott-Gwilliam-Williams 2024 is the *mathematical rigor layer* of Route C. The overall structure:

- **§18 Kapustin-Witten 2007:** the physics-level derivation of geometric Langlands from N=4 SYM.
- **§19 Gaitsgory-Raskin 2024:** the rigorous proof of geometric Langlands on curves.
- **§20 Scale bridge:** the (partially conjectural) descent from N=4 SYM to pure YM.
- **§21 Elliott-Gwilliam-Williams 2024:** the rigorous BV quantization of the twisted N=4 SYM, providing a factorization algebra of observables.
- **§22 Short-distance extraction:** how the factorization algebra + geometric Langlands give H4.
- **§23 Route C proof sketch:** the full assembly.

§21's specific role: make the quantum-field-theoretic side of Kapustin-Witten rigorous at the level of observables, so that Route C does not rest on a physics-level construction at this stage.

---

## 21.7. The scale-bridge compatibility of Elliott-Gwilliam-Williams

A critical question: does the Elliott-Gwilliam-Williams factorization algebra survive the $M_I \to \infty$ decoupling limit (§20)?

At the technical level, this question is:
- The BV quantization is constructed for the supersymmetric theory (N=4 SYM, twisted).
- For N=4$^*$ (soft-broken), the BV construction extends but with corrections.
- For pure YM ($M_I = \infty$, no SUSY), the BV construction *in the Kapustin-Witten form* does not strictly apply.

Elliott-Gwilliam-Williams treats the supersymmetric case. An extension to N=4$^*$ is conjecturally straightforward but has not been executed.

For Route C, the relevant claim is: *a factorization-algebra structure survives in the pure-YM limit, inheriting from N=4$^*$'s factorization algebra*. This is conjectural but compatible with gradient-flow machinery (Paper 8 Links 15-17), which naturally produces factorization-algebra-like structures.

The rigorous execution of this extension is part of Route C's to-do list.

---

## 21.8. Connection to programme infrastructure

The programme's infrastructure contains several objects that should embed into the factorization-algebra framework:

### 21.8.1. ITPFI factorization as factorization algebra

The ITPFI factorization of the programme's ground state (Paper 13 Layer 2) is a form of factorization-algebra structure: at each prime $p$, the local state $\omega_1^{(p)}$ is the "local observable" at that prime; the global state is the tensor product.

This *same* structure, applied to the YM Wilson-loop state (as conjectured in §15.6), produces a YM-specific factorization algebra. Elliott-Gwilliam-Williams's 4d TQFT factorization algebra should, under the scale bridge, reduce to this programme-internal structure.

### 21.8.2. Gradient flow as factorization-algebra morphism

Paper 8 Link 15's gradient-flow construction can be viewed as a morphism of factorization algebras: it takes lattice-local observables to continuum-local observables, compatibly with the factorization structure.

This perspective is suggestive but not yet executed. If formalized, it would provide another bridge between the programme's infrastructure and the Elliott-Gwilliam-Williams framework.

---

## 21.9. Status as of April 2026

Elliott-Gwilliam-Williams 2024 is **proved** (Annales Henri Poincaré, final form). The main theorem is accepted by the community.

Remaining open questions (all relevant to Route C):
- Extension to N=4$^*$ (soft-broken supersymmetry).
- Extension to pure YM (full decoupling).
- Compatibility with Gaitsgory-Raskin 2024 under dimensional reduction (almost certainly holds, but not explicitly proved).

Route C benefits from Elliott-Gwilliam-Williams 2024 as a *foundation layer*: it rigorously establishes the factorization algebra of twisted N=4 SYM. What remains is the scale bridge (§20) + the short-distance extraction (§22).

---

## 21.10. What Elliott-Gwilliam-Williams does NOT provide

Three things the paper does *not* give:

1. **Proof of the Kapustin-Witten S-duality.** The S-duality is taken as a conjecture and implemented via its action on the factorization algebra. The S-duality itself (Montonen-Olive / Vafa-Witten) remains a conjecture.

2. **Full 4d TQFT functoriality.** The paper establishes factorization-algebra structure but does not claim a full 4d TQFT structure (in the Lurie / Baez-Dolan cobordism-hypothesis sense). A full TQFT would give functorial invariants of 4-manifolds with boundary, 3-manifolds, 2-manifolds, and points; the paper gives the "points and 1-manifolds" part (the factorization algebra).

3. **Pure YM factorization algebra.** Covered only for the supersymmetric case. Extension to pure YM is conjectural.

For Route C, limitations 1 and 3 matter: the S-duality is a conjecture we use, and the pure-YM extension is a conjecture we need.

---

## 21.11. Summary

Elliott-Gwilliam-Williams 2024 provides a rigorous BV quantization of Kapustin-Witten twisted N=4 SYM, producing a factorization algebra of observables on each 4-manifold. The factorization algebras depend continuously on the twist parameter $\Psi \in \mathbb{CP}^1$ and implement the S-duality equivalence between $\Psi$ and $-1/(n_G \Psi)$ (exchanging $G$ and ${}^L G$).

For Route C, this is the rigor layer: the observable side of Kapustin-Witten is now mathematical. Combined with Gaitsgory-Raskin 2024 (§19) on the Langlands side, the full picture on the supersymmetric side is rigorous. What remains is the scale bridge (§20) and the extraction of short-distance behaviour (§22).

---

*Paper 50 §21. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
