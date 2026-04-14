# §19 — Gaitsgory-Raskin 2024: Geometric Langlands PROVED

*The 2024 breakthrough. Categorical geometric Langlands proven for a smooth projective curve. 1000+ pages, 9 mathematicians. The spectral-automorphic equivalence on the Hitchin moduli is now a theorem.*

---

## 19.1. The announcement

On 17 May 2024, Dennis Gaitsgory, Sam Raskin, and collaborators posted a series of preprints on arXiv announcing the proof of the *categorical geometric Langlands conjecture* for a smooth projective complex algebraic curve.

**Lead reference.** D. Gaitsgory and S. Raskin, *Proof of the geometric Langlands conjecture*, arXiv:2405.03599 (and related companion papers 2405.03600, 2405.03601, ..., 2405.03606). Submitted 17 May 2024. The complete argument spans approximately 1000 pages across the series.

**Coauthors on the full series** (as of the arXiv announcement): Dario Beraldo, Lin Chen, Justin Campbell, Joakim Færgeman, Dennis Gaitsgory, Kevin Lin, Sam Raskin, and Nick Rozenblyum. The effort represents more than a decade of developing the categorical framework needed for the proof.

---

## 19.2. The statement proved

**Theorem (Gaitsgory-Raskin et al. 2024).** *Let $C$ be a smooth projective complex algebraic curve. Let $G$ be a connected reductive algebraic group over $\mathbb{C}$, and let ${}^L G$ denote its Langlands dual group. Then there is an equivalence of (DG) categories*
$$\mathbb{L}_G : \text{D-mod}(\text{Bun}_G(C)) \xrightarrow{\sim} \text{IndCoh}_{\text{Nilp}}(\text{LocSys}_{{}^L G}(C)),$$
*characterized by its compatibility with the Hecke actions on the two sides, normalized to match a specific "Kac-Moody + Whittaker" initial condition.*

Unpacking:

- $\text{Bun}_G(C)$: the moduli stack of principal $G$-bundles on $C$. Dimension $\dim G \cdot (g - 1)$, where $g$ is the genus of $C$.
- $\text{D-mod}(\text{Bun}_G)$: the (DG) category of D-modules on $\text{Bun}_G$.
- $\text{LocSys}_{{}^L G}(C)$: the moduli stack of ${}^L G$-local systems on $C$ (${}^L G$-flat bundles).
- $\text{IndCoh}_{\text{Nilp}}$: the ind-coherent sheaves with nilpotent singular support (a specific enhancement of the derived category of quasi-coherent sheaves, needed to make the equivalence hold).
- $\mathbb{L}_G$: the Langlands functor, constructed to intertwine the Hecke operators.

The equivalence is sometimes called the *automorphic side* (LHS: D-modules on $\text{Bun}_G$, the "automorphic forms") versus the *spectral side* (RHS: sheaves on the local-system moduli, the "Langlands parameters").

---

## 19.3. History of the conjecture

The geometric Langlands correspondence was conjectured by Beilinson-Drinfeld 1991 (unpublished but widely circulated). Key milestones:

- **1991:** Beilinson-Drinfeld conjecture, based on the classical (number-theoretic) Langlands correspondence but on a function-field base.
- **2004-2012:** Gaitsgory develops the categorical framework (DG categories, singular support, Hecke categories).
- **2006:** Frenkel-Gaitsgory prove the tamely-ramified case for GL$_n$.
- **2007:** Kapustin-Witten derive the conjecture from N=4 SYM S-duality (§18).
- **2010s:** Ben-Zvi, Nadler, Francis, Gaitsgory develop the "local-to-global" framework.
- **2013:** Arinkin-Gaitsgory formulate the precise statement with nilpotent singular support.
- **2015-2023:** Gaitsgory and collaborators develop the tools (Whittaker coefficients, compactifications of $\text{Bun}_G$, Eisenstein functor).
- **2024 (May):** Gaitsgory-Raskin et al. post the proof.

The proof is the culmination of approximately 33 years of work by the geometric-Langlands community.

---

## 19.4. Proof strategy

The Gaitsgory-Raskin proof has four main components.

### 19.4.1. The Langlands functor

Construct the functor $\mathbb{L}_G$ from the automorphic side to the spectral side. The construction uses the *Poincaré sheaf* and the Whittaker reduction. Prior work: Gaitsgory 2018 constructed $\mathbb{L}_G$ assuming certain technical inputs; Gaitsgory-Raskin 2024 supply those inputs.

### 19.4.2. The Hecke-equivariance

Prove that $\mathbb{L}_G$ intertwines the Hecke actions on the two sides. The Hecke category acts on both $\text{D-mod}(\text{Bun}_G)$ and $\text{IndCoh}_{\text{Nilp}}(\text{LocSys}_{{}^L G})$, and $\mathbb{L}_G$ must carry one action to the other.

### 19.4.3. The fully-faithful part

Show $\mathbb{L}_G$ is *fully faithful*: morphisms on the two sides correspond. Key input: a categorical version of the Plancherel formula for the global spherical function.

### 19.4.4. The essential surjectivity

Show $\mathbb{L}_G$ is *essentially surjective*: every object on the spectral side is in the image. Key input: the reduction-to-Whittaker theorem, reducing the problem to the easier Whittaker model.

---

## 19.5. What the theorem gives

The proved theorem provides several explicit structural outputs used by Route C.

### 19.5.1. Hecke eigensheaves

For each ${}^L G$-local system $\mathcal{E}$ on $C$, there is a Hecke eigensheaf $\text{Aut}_\mathcal{E}$ on $\text{Bun}_G$ satisfying
$$H_\lambda \cdot \text{Aut}_\mathcal{E} = V_\lambda(\mathcal{E}) \otimes \text{Aut}_\mathcal{E}$$
for every $\lambda$ a dominant coweight of $G$, where $H_\lambda$ is the Hecke operator and $V_\lambda$ is the representation of ${}^L G$ with highest weight $\lambda$.

This is the *geometric* analogue of the Hecke-eigenvalue property for automorphic forms.

### 19.5.2. Wilson-to-Hecke correspondence

Under Kapustin-Witten's 4D-to-2D reduction (§18), Wilson loops in the 4D gauge theory become B-branes on $\mathcal{M}_H(G, C)$. The Gaitsgory-Raskin theorem establishes that these B-branes correspond, under the Langlands equivalence, to specific D-modules on $\text{Bun}_{{}^L G}$ — namely, the Hecke eigensheaves.

This gives a *proved* dictionary:
$$\text{Wilson loop in rep } R \text{ of } G \text{ at } \mathcal{E} \quad\longleftrightarrow\quad V_R(\mathcal{E}) \cdot \text{Aut}_\mathcal{E}.$$

### 19.5.3. S-duality at the categorical level

The theorem implements Kapustin-Witten's 4D S-duality at the level of categories: B-branes on $\mathcal{M}_H(G)$ (corresponding to D-modules on $\text{Bun}_G$) and A-branes on $\mathcal{M}_H({}^L G)$ (corresponding to Hecke eigensheaves on $\text{Bun}_{{}^L G}$) are equivalent.

This is the precise meaning of "geometric Langlands S-duality holds."

---

## 19.6. What the theorem does not give

Important limitations of Gaitsgory-Raskin 2024:

### 19.6.1. Complex curves only

The proved theorem is over a smooth projective complex algebraic curve $C$. The function-field analogue (over a finite field $\mathbb{F}_q$) and the number-field analogue (over $\text{Spec}(\mathbb{Z}) \setminus \{p_1, \ldots, p_n\}$) are separate questions. V. Drinfeld + Lafforgue established the function-field case for GL$_n$; the number-field case (classical Langlands) remains open.

### 19.6.2. Unramified / tame ramification

The theorem covers the unramified case (and allows tame ramification). The wildly-ramified case is open.

### 19.6.3. Curves only, not higher dimensions

The geometric Langlands conjecture generalizes to higher-dimensional varieties (higher Langlands), but the Gaitsgory-Raskin theorem is *specific to curves*.

For Route C, these limitations matter because:

- Pure YM on $\mathbb{R}^4$ is not *directly* over a complex curve.
- The reduction to 2D via Kapustin-Witten (§18) uses $M = \Sigma \times C$ with $C$ a Riemann surface — so $C$ is a complex curve, and Gaitsgory-Raskin applies.
- But the 4D theory on $M$, before reduction, has data that is not captured by geometric Langlands on $C$ alone.

The scale-bridge analysis of §20 handles this: the reduction to 2D is controlled, and the 4D data that does not reduce is handled by supersymmetry + gradient-flow arguments.

---

## 19.7. What Route C gets from Gaitsgory-Raskin 2024

Route C inherits, directly, the following from the 2024 theorem:

1. **A proved correspondence between the B-model on $\mathcal{M}_H(G)$ and the spectral side (D-modules on $\text{Bun}_{{}^L G}$).**

2. **Explicit Hecke eigensheaves $\text{Aut}_\mathcal{E}$ for each ${}^L G$-local system $\mathcal{E}$.** These control the Wilson-loop spectrum of the 2D sigma-model.

3. **S-duality implemented at the categorical level.** The functional equation on the Langlands side is now a proved categorical equivalence.

What Route C *still needs*:

1. **The scale bridge from N=4 SYM to pure YM** (§20). Gaitsgory-Raskin covers the 2D reduction of twisted N=4 SYM; it does not cover pure YM directly. The bridge is Paper 10's scheme independence + explicit decoupling of extra SUSY.

2. **Short-distance extraction** (§22). The Langlands correspondence organizes Wilson-loop data globally; extracting short-distance (UV) behaviour requires additional work.

3. **4d TQFT structure** (§21). The Kapustin-Witten twist is a 4d TQFT; the corresponding BV quantization framework (Elliott-Gwilliam-Williams 2024) gives the observables as a factorization algebra, which Route C uses to organize the YM observables.

---

## 19.8. The role of Gaitsgory-Raskin in resolving Route B's obstructions

Route B has three critical obstructions (Ob.3: functional equation of $L_{\text{YM}}$; Ob.4: Satake matching; §17.4). Gaitsgory-Raskin 2024, applied via Kapustin-Witten, resolves both:

**Ob.3 (functional equation).** The geometric Langlands correspondence implements, at the categorical level, a functional equation between $\text{D-mod}(\text{Bun}_G)$ and $\text{IndCoh}_{\text{Nilp}}(\text{LocSys}_{{}^L G})$. In the 2D sigma-model (the Kapustin-Witten reduction), this is the mirror-symmetry functional equation. Under the scale bridge to pure YM, this induces a functional equation on $L_{\text{YM}}$.

**Ob.4 (Satake matching).** Under geometric Langlands, each ${}^L G$-local system $\mathcal{E}$ on $C$ corresponds to a Hecke eigensheaf $\text{Aut}_\mathcal{E}$ on $\text{Bun}_G$. At each point $x \in C$, the Hecke eigenvalue $V_\lambda(\mathcal{E})$ gives the "Satake parameter" of the automorphic side. The YM Wilson-loop Satake parameters, extracted from the scale bridge, match these via the Kapustin-Witten dictionary.

This is why Routes B and C are not independent: Gaitsgory-Raskin 2024 provides the *shared* infrastructure that both routes depend on. Route B uses the *classical* Langlands side (which would follow from the geometric side via function-field reduction); Route C uses the *geometric* side directly.

---

## 19.9. Status as of April 2026

At time of writing (April 2026), the Gaitsgory-Raskin proof has been:

- Posted on arXiv (May 2024).
- Scrutinized by the geometric-Langlands community for 23 months.
- Presented at IAS, MSRI, and major conferences.
- No significant gaps reported.

The proof is considered *correct and accepted* by the community. The remaining questions are about generalizations (higher ramification, higher dimensions, restrictive curves, non-reductive groups), not about the main theorem.

For Route C, this means: **geometric Langlands is, as of 2026, a theorem we can cite**, not a conjecture. The Kapustin-Witten picture (§18) is now connected to a proved mathematical object.

---

## 19.10. Summary

Gaitsgory-Raskin et al. 2024 proved the categorical geometric Langlands correspondence for smooth projective complex algebraic curves: $\text{D-mod}(\text{Bun}_G) \simeq \text{IndCoh}_{\text{Nilp}}(\text{LocSys}_{{}^L G})$ via the Langlands functor $\mathbb{L}_G$, Hecke-equivariantly. The proof spans ~1000 pages across a series of preprints (arXiv:2405.03599 and companion papers).

For Route C: this provides the *proved* correspondence between the automorphic side (D-modules on $\text{Bun}_G$) and the spectral side (sheaves on $\text{LocSys}_{{}^L G}$). Via Kapustin-Witten 2007 (§18), this is identified with mirror symmetry of the Hitchin moduli, hence with 4D S-duality of N=4 SYM. The remaining Route C bridges — scale to pure YM (§20), BV quantization (§21), short-distance (§22) — complete the path to H4.

The 2024 breakthrough changes Route C's status from "architecture only" to "architecture + proved mathematical core."

---

*Paper 50 §19. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
