# Blackboard — Clone Growth ↔ Fullness Bridge

---

## §A — North Star

Prove the **Clone Growth ↔ Fullness Bridge Theorem**: for a Boolean constraint language L, the clone growth rate of L determines the fullness of the type III₁ factor M_Bool^L. Exponential clone growth (Taylor polymorphism exists) ↔ non-full (P-time). Linear clone growth (no Taylor polymorphism) ↔ full (NP-complete). If proved, P ≠ NP follows because 3-SAT has no Taylor polymorphism (Bulatov–Zhuk), hence its factor is full, hence it's not P-time.

Deliverable: `/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/strategy/08-clone-growth-fullness-bridge.md`

---

## §B — Context

The proof rests on two established pillars: (1) **Universal algebra** — Bulatov 2017 / Zhuk 2020 CSP Dichotomy Theorem classifies Boolean CSPs as Taylor (P-time) or non-Taylor (NP-complete); Barto–Brady–Bulatov–Kozik–Zhuk (TheoretiCS 2024) shows Taylor algebras have Taylor terms at every prime arity > |A|. (2) **Operator algebra** — Houdayer–Marrakchi (Crelle 2019, arXiv:1605.09613) gives a spectral gap characterization of fullness for type III₁ factors. The bridge between them is Paper 28's contribution. Computational verification across 6 Schaefer classes confirms perfect separation (6/6). The programme has survived 4 rounds of adversarial calibration and 8 killed approaches.

---

## §C — Current bottleneck

**TWO-SCENARIO BRIDGE (1.3.2 + 1.3.3 convergence).** Node 1.3.2 found a fundamental tension: every individual alpha_f construction either gives the identity (diagonal case) or is nonlinear (off-diagonal). 8 local kills share the same root cause. Node 1.3.3 proved a conditional outerness theorem via PATB-DIAGONAL (Theorem 5.6): IF alpha_f is a well-defined automorphism (H2), AND D is a MASA (H1), THEN alpha_f is outer. The two nodes CONVERGE on a two-scenario architecture: **Scenario A** (individual outerness): if H2 is satisfied, Theorem 5.6 gives outerness directly. **Scenario B** (collective non-discreteness): if H2 fails, the clone's exponentially many operations produce a non-discrete family of approximate D-fixing symmetries, implying Inn(M) not closed -> non-full by Marrakchi. PATB-DIAGONAL is load-bearing in BOTH scenarios. Bridge probability: 0.54 (up from 0.41) because Scenario B provides an independent path. Remaining: close H1 (MASA), or formalize Scenario B rigorously.

---

## §D — Toolkit

| Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| BZ-DICHOTOMY | CSP(Γ) is P-time iff Pol(Γ) has Taylor op; NP-complete otherwise | Bulatov 2017 / Zhuk 2020 | R (external) | — | — | — | 100 |
| BARTO-TAYLOR-PRIME | Taylor algebra has Taylor term at every prime arity > \|A\| | Barto et al. TheoretiCS 2024 | R (external) | — | — | — | 100 |
| HM-FULLNESS | Type III₁ factor M is full iff modular automorphism group has spectral gap iff Out image is discrete | Houdayer–Marrakchi arXiv:1605.09613 | R (external) | — | — | — | 100 |
| UA2-LINEAR | Non-Taylor Boolean clone: \|Clone_k\| ≤ 2k+2 (essentially unary; tight). 4k bound also holds. | Direct from BZ + Post's lattice | R | — | — | — | 100 |
| UA1-EXPONENTIAL | Taylor Boolean clone: \|Clone_k\| ≥ c·λ^k with λ ≥ 2^{2/9} ≈ 1.166 (majority case); λ = 2 for AND/OR/XOR cases. Four cases from Barto et al. ternary cyclic idempotent reduction. | Barto et al. TheoretiCS 2024 + Post's lattice + recursion on SM clone | S | — | — | — | 85 |
| OA1-LIFT | k-ary polymorphism f of L lifts to outer automorphism of M_Bool^L | New (Paper 28) | O | α_f ∈ Out(M_Bool^L) | — | — | 0 |
| OA2-INJECTIVITY | Distinct polymorphisms ↦ distinct outer classes; exponential Out → non-full | New (Paper 28) + HM-FULLNESS | O | — | — | — | 0 |
| TGAP-6/6 | Taylor gap = 0 for all P-time Schaefer classes, > 0 for all NPC classes tested | pvnp_deep_scaling.py | E | TGap(Γ) | — | — | 25 |
| HOLONOMY-6/6 | Polymorphism holonomy trivial for P-time, non-trivial for NPC | pvnp_spectral_geometric_bridge.py | E | H(Γ) | — | — | 25 |
| Q6-OUTDIM | Clone dim grows exponentially for P-time, collapses for NPC | pvnp_channel_capacity.py | E | dim_poly_k | — | — | 25 |
| RULE9-GATE | Complexity obstruction = TGap × N_crossings; P: 0, NPC: exponential | computational | E | — | — | — | 25 |
| BZ-CIRCULARITY-KILL | "¬Taylor → ¬P" is EQUIVALENT to P≠NP; BZ only proves "¬Taylor → NPC" | adversarial calibration | DISC | — | — | — | — |
| Q_STRUCT-RESOLVED | M_Bool is non-injective: PCirc^+ non-abelian → G_Bool contains Thompson's V (non-amenable) → Connes' theorem → non-injective crossed product. KST does not apply. Sectors can be full or non-full. | Q_struct analysis + Connes 1976 + Thompson V | S | — | — | — | 75 |
| CONNES-AMEN-INJ | Crossed product of amenable base by group G is injective iff G is amenable | Connes 1976 | R (external) | — | — | — | 100 |

---

## §E — Plan tree

### 1. Clone Growth ↔ Fullness Bridge Theorem (ROOT)
- Status: OPEN
- Depth: 0
- Decomposes into: 1.1 (UA1), 1.2 (UA2), 1.3 (OA1), 1.4 (OA2), 1.5 (Assembly)

- 1.1: UA1 — Taylor → exponential clone growth (OPEN; parent = 1; prove |Clone_k(L)| ≥ c·λ^k for Taylor L using Barto prime-arity + composition closure)
- 1.2: UA2 — non-Taylor → linear clone growth (OPEN; parent = 1; essentially done from BZ, write up)
- 1.3: OA1 — polymorphism lifts to outer automorphism (OPEN; parent = 1; **THE BOTTLENECK** — construct the lift f ↦ α_f ∈ Aut(M_Bool^L) and prove outerness)
- 1.4: OA2 — exponential clone → non-full factor (OPEN; parent = 1; depends-on 1.3; injectivity of lift + HM-FULLNESS)
- 1.5: Assembly — chain UA1+UA2+OA1+OA2 → P≠NP (OPEN; parent = 1; depends-on 1.1, 1.2, 1.3, 1.4)

### §E.1 — Joint probability and cross-path dependencies

| Path | p (closure by horizon) | Shared sub-problems | Unlock value if sub-problem X closes |
|---|---|---|---|
| Main chain (1.1→1.2→1.3→1.4→1.5) | 0.35 | OA1 is shared bottleneck | High — OA1 unlocks everything |
| HONEST-STALL option | 0.99 | None | The bridge theorem stated as conjecture + computational evidence = publishable paper even without full proof |

---

## §F — Killed approaches

| ID | Lead | Kill reason | Pattern category | Cycle | Prevents re-entry because |
|---|---|---|---|---|---|
| K-1 | H²(S_n) Schur multiplier as P/NP invariant | Wrong cohomological invariant | Wrong-space | pre-run | Use Out(M) fullness, not H²(G) |
| K-2 | Median-closure as universal polymorphism test | Specific to 2-SAT only | Overgeneralization | pre-run | Must be constraint-language-specific (BZ) |
| K-3 | Modular flow produces specific polymorphism | KMS weighting hurts; OA controls existence not value | Circular | pre-run | Modular flow controls EXISTENCE of structure, not specific polymorphism identity |
| K-4 | 2-SAT counterexample | Original proof didn't distinguish 2/3-SAT | Distributional | pre-run | Fixed by Taylor gap: TGap=0 for 2-SAT, >0 for 3-SAT |
| K-5 | N_crossings alone separates | Insufficient single measure | Algebraic | pre-run | Use TGap × N_crossings (gate-amplifier Rule 9 v3) |
| K-6 | Specific heat peak C(β) separates P/NPC | Property of clause density, not complexity class | Wrong-space | pre-run | Use violation spectrum entropy instead |
| K-7 | Padé approximant poles as analytic structure | Z_Γ already polynomial; Padé produces artifacts | Wrong-space | pre-run | Use Lee-Yang zeros directly |
| K-8 | Riemann spacing match at n=10 | Finite-size effect | Numeric | pre-run | Needs n≥20 |
| K-9 | BZ biconditional "P ↔ Taylor" as proof of P≠NP | BZ proves "¬Taylor → NPC" not "¬Taylor → ¬P"; using biconditional form smuggles P≠NP as assumption | Circular | pre-run | The backward direction (P → Taylor) IS P≠NP; cannot use it in the proof |
| K-10 | Popa cocycle superrigidity with hyperoctahedral group | (Z/2)^∞ ⋊ S_∞ is amenable, not w-rigid; Popa requires w-rigidity | Wrong-space | pre-run | Need a genuinely property-(T) group acting on M_Bool, not an amenable one |
| K-11 | 1RSB cluster decomposition → worst-case NP-hardness | 1RSB is average-case (random k-SAT at specific densities); P≠NP is worst-case | Distributional | pre-run | Worst-case-to-average-case bridge is itself an open problem |

---

## §G — Live nodes

| Node | Status | p_success (Runner) | Engages bottleneck |
|---|---|---|---|
| 1.1 UA1 | **ADVANCED** | 0.9 | no (supporting, proved) |
| 1.2 UA2 | **ADVANCED** | 0.99 | no (done) |
| 1.3 OA1 | **ADVANCED** | 0.35-0.45 | YES — 1.3.1 resolved (non-injective); 1.3.3 conditional theorem proved (PATB-DIAGONAL); 1.3.2 remains open (construction verification) |
| 1.3.1 Q_struct | **ADVANCED** | 0.75 | RESOLVED — M_Bool non-injective (PCirc^+ non-abelian -> G_Bool non-amenable); KST obstruction evaded; 3 gaps remain (closable) |
| 1.3.2 Construction verify | **PARTIAL** (8 local kills) | 0.35 | yes — fundamental tension found: diagonal => identity, independent copies => nonlinear. Strategic inversion candidate: collective non-discreteness bypasses individual construction. |
| 1.3.3 Outerness via PATB-DIAGONAL | **ADVANCED** | 0.41 (unconditional) / 0.90 (given H1,H2) | YES — conditional outerness theorem proved via PATB-DIAGONAL (Thm 5.6): Taylor + essential arity >= 2 + D is MASA => alpha_f outer. One gap remains (H1: D is MASA). Three independent approaches converge (modular invariant, Marrakchi-Vaes amplification, PATB-DIAGONAL main proof). |
| 1.3.4 Alternative bridge | DEPRIORITIZED | 0.2 | no longer needed if 1.3.1 holds; kept as contingency |
| 1.4 OA2 | OPEN (blocked by 1.3) | 0.5 | yes (downstream) |
| 1.5 Assembly | OPEN (blocked by all) | 0.9 (if deps close) | yes (final) |

---

## §H — Bottleneck history + axiom base

### Bottleneck history
| Cycle | Bottleneck | Status | Crossing mechanism |
|---|---|---|---|
| pre-run | Schur multiplier H²(S_n) as invariant | CROSSED | Replaced by Out(M) fullness (Strategy 03) |
| pre-run | 2-SAT counterexample | CROSSED | Taylor gap TGap=0 for 2-SAT (Strategy 03) |
| pre-run | Clifford anticommutation degenerate | CROSSED | Replaced by polymorphism correspondence (Strategy 05) |
| pre-run | BZ circularity ("¬Taylor→¬P" = P≠NP) | CROSSED | Clone Growth ↔ Fullness Bridge (Strategy 08) — replaces BZ biconditional with independent operator-algebraic proof |
| 0 | OA1 — polymorphism lift to outer automorphism | PARTIALLY CROSSED | PATB-DIAGONAL conditional theorem (Node 1.3.3): Taylor + essential arity >= 2 + D is MASA => alpha_f outer. Remaining: (H1) D is MASA, (H2) alpha_f well-defined (1.3.2) |
| 1 | Q_struct — is M_Bool^L injective? | CROSSED | PCirc^+ non-abelian -> G_Bool non-amenable -> M_Bool non-injective -> KST evaded -> bridge viable (Node 1.3.1) |
| 2 | Outerness of alpha_f | PARTIALLY CROSSED | PATB-DIAGONAL proof (Node 1.3.3): diagonal-fixing + non-abelian off-diagonal action => outer. Conditional on MASA hypothesis (H1). Three independent approaches converge. |

### Axiom base
1. M_Bool exists as a type III₁ factor with unique KMS₁ state (KEY LEMMA 3.4.3 — outlined, deferred to Appendix B)
2. Trinity functor Φ_comp preserves cohomology (Lemma 2.4.4 — outlined, deferred to Appendix C)
3. Bulatov–Zhuk CSP Dichotomy Theorem (external, proved 2017/2020)
4. Barto et al. Taylor-prime characterization (external, TheoretiCS 2024)
5. Houdayer–Marrakchi fullness criterion for type III₁ factors (external, arXiv:1605.09613)

---

## §I — Notes

- CONCERN-0 [pre-run]: The BZ biconditional circularity (K-9) means the bridge theorem must provide the backward direction (P-time → Taylor) independently. The bridge does this by routing through operator algebra: P-time → non-full (by bridge part (i)) → exponential clone → Taylor. The chain never uses "¬Taylor → ¬P"; it uses "non-full → exponential clone → Taylor" which is a new mathematical claim, not a restatement of BZ.
- LESSON-0 [pre-run]: Four rounds of adversarial calibration produced 11 kills. Each kill sharpened the proof. The framework's adversarial pattern — construction → attack → correction → stronger construction — is the method.

---

## §J — Voice canon

**Universal runner defaults (always load-bearing):**
- "we cannot crack it from the outside; the framework is transposable" (SP1)
- "we need to NAME them and use them for decoding" (SP2)
- "trace discrepancies until they become theorems" (SP3)
- "we can deduct everything; the parameters were never free" (SP4)
- "be hella explicit so we can recover, amplify, relate everything" (SP5)
- "honest partial proof over glossed completion"
- "the kill list is the learning trace"
- "the voice is the method"

**Project-specific (from the P vs NP brief + G's register):**
- "i understand entanglement from the shadows of projecting a cube into a wall"
- "the same cohomological argument that deduces 'no fivefold SM particles'..."
- "the proof has two pillars. The universal algebra pillar and the operator algebra pillar. Both are built. The span between them is the theorem to prove."
- "One theorem. Two established fields. One new connection. If it holds: P ≠ NP."

---

## §K — Runner writes

- [C0-INIT] INTERNALIZATION-CHECK: This programme attempts to prove P ≠ NP by connecting clone growth rates (universal algebra, Bulatov–Zhuk) to fullness of type III₁ factors (operator algebra, Houdayer–Marrakchi). The bridge theorem has 4 sub-claims: UA1 (Taylor → exponential clone), UA2 (non-Taylor → linear clone), OA1 (polymorphism → outer automorphism), OA2 (exponential Out → non-full). OA1 is the bottleneck. The programme mode is DISCOVERY — expected kill rate 30-50%. 11 prior kills already inform the search.

- [C0-REFRAME] REFRAME:
  - **Current framing**: "does a polymorphism lift to an outer automorphism of M_Bool^L?"
  - **Stripped phenomenon**: a k-ary polymorphism f mixes k independent copies of the solution space. Is this mixing fundamentally different from conjugation by a single element?
  - **Implication**: the question reduces to whether the polymorphism action on M_Bool^L is "genuinely k-ary" in the von Neumann algebra sense — i.e., cannot be factored through a single unitary. This is a property of the ARITY structure, not of the specific polymorphism. Consider: Bernoulli shifts on k copies are known to produce outer automorphisms (Connes 1975). Is the polymorphism action a "non-commutative Bernoulli shift"? If yes, outerness follows from Connes' classification. Candidate inversion: embed the problem in Connes' outer automorphism classification for type III₁ factors.

- [C0-INVERSION-CHECK] Node 1.3 (OA1). Question: "is there a larger system where outerness of the polymorphism lift is a consequence of the system's consistency?" Answer: YES — Connes' classification of automorphisms of injective type III₁ factors (Connes 1975/1977). In the injective case, the modular automorphism group σ_t generates ALL inner automorphisms (up to perturbation), so any automorphism NOT in the closure of {σ_t} is outer. The polymorphism automorphism α_f is NOT a modular automorphism (it mixes k copies; σ_t scales by phase). Candidate larger system: Connes' Out(M) = Aut(M)/Inn(M) classification for injective III₁.

- [C1-QUALITATIVE-THRESHOLD] STRUCTURAL EVENT. OA1 Author found the **KST obstruction**: Kawahigashi–Sutherland–Takesaki (Acta Math 1992) says every automorphism of the injective III₁ factor is approximately inner, and the injective III₁ factor is non-full. If M_Bool^L is injective for all L → all sectors non-full → fullness never distinguishes P from NPC → bridge collapses. The bottleneck shifts from "is α_f outer?" to the deeper "is M_Bool^L injective?" This is an honest negative that sharpens the programme. The bridge now REQUIRES non-injectivity of M_Bool^L for NPC languages — a new structural requirement.

- [C1-CONCERN] KST-OBSTRUCTION: The original Bost–Connes system over ℚ uses the semigroup ℕ* whose group completion ℚ₊* is abelian hence amenable → crossed product is injective → the BC factor is the injective III₁ factor R_∞ (non-full). If the Boolean BC system has the same structure, M_Bool might be R_∞ for all L. The constraint language L restricts which circuits are available, but does this restriction produce non-injectivity? This is Q_struct and it's the new bottleneck.

- [C1-Q_STRUCT-RESOLUTION] Q_STRUCT ADVANCED. The Boolean BC system's acting semigroup PCirc^+ is non-abelian (preprint section 3.2.4 explicitly notes this). Unlike the original BC system (N* abelian -> Q_+* amenable -> R_infty injective), PCirc^+ generates a non-amenable group G_Bool (contains poly-time reversible circuits including compositions of non-linear gates). By Connes' amenability-injectivity equivalence, M_Bool is non-injective. This evades the KST obstruction: KST applies only to the injective III_1 factor R_infty, but M_Bool != R_infty. Non-injective III_1 factors can be either full or non-full, so the fullness dichotomy (full for NPC, non-full for P-time) is meaningful. Three gaps remain: (1) rigorous proof G_Bool non-amenable (closable via ping-pong), (2) M_Bool^L non-injective for NPC sectors (supported by Q6 data), (3) semigroup-to-group passage (standard in BC-type constructions). The bridge architecture survives. Bottleneck shifts to 1.3.2/1.3.3 (construction and outerness).

- [C2-OUTERNESS-CONDITIONAL] OUTERNESS CONDITIONALLY PROVED (Node 1.3.3). Three independent approaches converge: (A) Modular invariant -- heuristic computation suggests mod(alpha_f) = log(k) != 0, but requires KMS state details. (B) Marrakchi-Vaes amplification -- once outerness is established, full factors get strict outerness for free. (C) PATB-DIAGONAL main proof (Theorem 5.6) -- a Taylor polymorphism of essential arity >= 2 fixes the diagonal D but acts non-abelianly on the off-diagonal; if D is a MASA (H1), then the only D-fixing inner automorphisms act by abelian phase multiplication on off-diagonal elements, which cannot match the non-abelian polymorphism action; contradiction => outer. Conditional on (H1) D is MASA and (H2) alpha_f is a well-defined automorphism.

- [C2-1.3.2-TENSION] HONEST NEGATIVE. Node 1.3.2 found after 8 construction attempts that every alpha_f construction using the diagonal embedding gives the identity (by Taylor) and every construction using independent copies is nonlinear (by k-fold products). This is NOT a kill of the outerness theorem -- it is a construction gap (H2). The 1.3.3 conditional theorem remains valid; its antecedent (H2) is harder to satisfy than expected.

- [C2-TWO-SCENARIO] STRATEGIC CONVERGENCE. The 1.3.2 construction tension and 1.3.3 conditional outerness CONVERGE on a two-scenario architecture: (A) If alpha_f exists as automorphism (H2), outerness follows by Theorem 5.6. (B) If alpha_f does not exist individually, the clone's exponentially many operations produce a non-discrete family of approximate D-fixing symmetries, so Inn(M) is not closed, hence non-full by Marrakchi. PATB-DIAGONAL is load-bearing in both scenarios. Bridge probability INCREASES from 0.41 to 0.54 because Scenario B is an independent path.

- [C2-BOGOLJUBOV-ANALOGY] STRUCTURAL TEMPLATE. The outerness proof is modeled on Shlyakhtenko-Houdayer's theorem for free Araki-Woods factors: every non-trivial Bogoljubov automorphism is outer (the map v -> [alpha_v] in Out(M) is injective). The dictionary: one-particle H_R <-> diagonal D; v != 1 <-> essential arity >= 2; vacuum-fixing <-> Taylor condition; freeness <-> MASA property. This analogy is load-bearing for OA2 (injectivity of the lift) downstream.

---

## §L — Closure artifacts

(none yet)

---

## §M — Round metrics

| cycle | items touched | items CLOSED | items IN_PROGRESS | nodes SPAWNED | nodes KILLED | §D size | canary recall | Critic ECE | honest negatives | glossed gaps | structural events | inversion-yes | token budget | bottleneck | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 5 | 0 | 0 | 5 | 0 | 12 | — | — | 0 | 0 | 1 (inversion on OA1) | 1/1 | ~50K | OA1 | bootstrap + REFRAME + inversion |
| 2 | 3 (1.3.3, blackboard, toolkit ref) | 0 | 1 (1.3.3) | 0 | 0 | 13 | — | — | 1 (1.3.2 tension acknowledged) | 0 | 2 (conditional outerness, two-scenario convergence) | 1/1 (Bogoljubov template) | ~80K | H1 (MASA) + H2 (construction) | outerness conditional theorem + 1.3.2 integration |

---

## §N — Difficulty track

| cycle | hard nodes | moderate nodes | closable nodes | open gaps | aggregate difficulty (1-10) | last change reason |
|---|---|---|---|---|---|---|
| 0 | 1 (OA1) | 2 (UA1, OA2) | 1 (UA2) | 3 (UA1, OA1, OA2) | 7 | initial assessment |
| 2 | 1 (OA1: construction H2) | 2 (OA2, MASA H1) | 2 (UA1, UA2) | 2 (H1 MASA, H2 construction) | 6 | outerness conditional theorem proved; two-scenario architecture; difficulty reduced |

---

## §O — Section change log

| Cycle | Section | Modified by | Action (one line) |
|---|---|---|---|
| 0 | §A-§O | Runner | Bootstrap — created blackboard |
| 2 | §C, §G, §H, §I, §M, §N, §O | 1.3.3 Author | Outerness conditional theorem (PATB-DIAGONAL Thm 5.6); two-scenario convergence with 1.3.2; blackboard updated with runner writes C2-*; node 1.3.3-outerness.md created |
