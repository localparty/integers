# Boegli Spectral Exactness -- Verification Capacitor v1

*Charged toolkit for the Tier 4 pilot. Contains: domain knowledge, kill list, proof chain, correspondences, patterns, operations, escalation routes, and background toolkit cards. Single file -- no external reads needed at runtime beyond the target paper itself.*

*Generated: 2026-04-13. Target: Boegli 2017 (arXiv:1604.07732). Mode: VERIFY.*
*Charge level: 5 steps, 4 correspondences, 0 target-specific kills (first run), 36 imported framework kills.*

---

## META -- Capacitor state

| Field | Value |
|---|---|
| Version | v2 (post-run, repairs applied) |
| Target | Boegli 2017, IEOT 88, 559-599 |
| Also | Teschl et al. 2026, arXiv:2601.10476 (Lemma 2.7); Chatelin 1983 (Galerkin gnrc) |
| Mode | VERIFY (Tier A) — CLOSED |
| Steps in target | 5 |
| SURVIVED | 5 (all LOCKED) |
| WEAKENED | 0 (1 WEAKENED-CLOSABLE in run, repaired) |
| BROKEN | 0 |
| PENDING | 0 |
| Kills (target-specific) | 1 (K-T4-1) |
| Kills (imported) | 36 (from framework prior runs) |
| Escalations triggered | 0 |

---

## LEGEND

Standard abbreviations used throughout this capacitor. Read once, apply everywhere.

```
gsrc  := generalized strong resolvent convergence (Boegli Def 2.1)
DC    := discrete compactness (Boegli Def 2.4)
SE    := spectral exactness (no spurious + no missing eigenvalues)
SI    := spectral inclusion (spec(T) subset lim spec(T_n))
NSE   := no spurious eigenvalues (lim spec(T_n) subset spec(T))

KLMN  := Kato-Lions-Lax-Milgram-Nelson (self-adjointness via form bound)
RK    := Rellich-Kondrachov (compact Sobolev embedding)
CF    := Caratheodory-Fejer (Toeplitz self-adjointness)
CCM   := Connes-Consani-Moscovici (arXiv:2511.22755)
ITPFI := Infinite Tensor Product of Factors of type I

SP    := Spectral (domain/pillar)
GE    := Geometric (domain/pillar)
AL    := Algebraic (domain/pillar)
IN    := Information-theoretic (domain/pillar)

LB    := Load-Bearing (step whose failure collapses downstream)
RH    := Riemann Hypothesis
IEOT  := Integral Equations and Operator Theory
CMP   := Communications in Mathematical Physics
```

---

## KILLS

### Target-specific kills (Boegli)

```
K-T4-1: Direct-Teschl-2.7-invocation-with-Galerkin-projections
  WHAT: Citing Teschl Lemma 2.7 directly with J_n = P_N for gnrc
  WHY:  Standing hypothesis (2.1) requires ||J_n*J_n - I|| -> 0 in operator norm;
        fails for orthogonal projections onto proper subspaces (||P_N - I|| = 1 for all N)
  PATTERN: External-source-inconsistency
  RE-ENTRY: If Teschl publishes revised version with (2.2) as standing hypothesis,
            or if a gsrc variant of Lemma 2.7 is proved
  REPAIR: Use Chatelin Galerkin gnrc (1983, Ch. 3) instead. Keep Teschl for KLMN closability only.
```

### Imported framework kills (relevant subset)

These kills are from other chains. Most are irrelevant to the Boegli verification but are included for completeness and to prevent pattern-repetition.

**Directly relevant to the Boegli domain:**

```
K-RH-1: Coboundary-gap-v1-proof
  WHAT: Original v1 RH proof via cohomological approach
  WHY:  Gap in archimedean estimate (original proof incomplete)
  NOTE: Resolved via CCM + Boegli bypass (Layer 3+4 of RH chain).
        THIS is why Boegli is load-bearing -- it was the bypass route.

K-RH-2: Direct-Hilbert-space-RH-proof
  WHAT: Attempt to prove RH directly in Hilbert space without spectral realization
  WHY:  Circular (assumes spectral realization without proving it)
  NOTE: Irrelevant to Boegli verification but shows why CCM operators are needed.
```

**Other framework kills (for agent context, not directly relevant):**
- K-YM-1 through K-C3: Yang-Mills domain, irrelevant to operator theory verification
- K-PvNP-1 through K-PvNP-20: P vs NP domain, irrelevant
- K-BSD-1 through K-BSD-7: BSD domain, irrelevant

**The full 36-kill list is in the compiled ORA generator (03-ora-generator-compiled.md section 1).** Agents should reference it if pattern-matching is needed but should not spend tokens re-reading irrelevant kills.

---

## CHAIN -- 5 steps with dependencies and status

```
chain[5]{step,type,statement,deps,LB,status}:
  1*,Definition,"gsrc(Def2.1):norm-conv-of-resolvents-at-one-z-implies-conv-at-all-z",--,*,SURVIVED+LOCK
  2*,Theorem,"gsrc->SI:spec(T)-subset-lim-spec(T_n)(Thm2.3)",1,*,SURVIVED+LOCK
  3*,Theorem,"DC+gsrc->NSE:no-spurious-eigenvalues(Thm2.6:THE-MAIN-RESULT)",1;2,*,SURVIVED+LOCK
  4,Corollary,"Self-adjoint-specialization:T_n-s.a.->spectral-measure-conv(Thm2.4ii+Thm2.6-s.a.)",3,,SURVIVED+LOCK
  5*,Interface,"Chatelin-Galerkin-gnrc+Teschl-KLMN-closability(arXiv:2601.10476)",1,*,SURVIVED+LOCK(repaired)
```

Dependency adjacency:
```
1->2, 2->3, 1->5
3->4
3+5 -> RH.Layer4 (together they close the spectral exactness requirement)
```

Critical path: 1 -> 2 -> 3. If Step 3 SURVIVES, the main result is verified.
Secondary path: 1 -> 5. If Step 5 SURVIVES, the Teschl interface is verified.
Both paths required for RH Layer 4 security.

---

## CORRESPONDENCES -- Boegli's theorem mapped to 4 pillars

### Concept: gsrc (generalized strong resolvent convergence)

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | Norm convergence of (T_n-z)^{-1} to (T-z)^{-1} | Spectral convergence: resolvent norm controls spectrum | Boegli Def 2.1 |
| GE | Gromov-Hausdorff convergence of operator graphs | Graph(T_n) -> Graph(T) in the Grassmannian of H x H | Kato, Perturbation Theory IV.2 |
| AL | Directed system of operator domains: dom(T_1) -> dom(T_2) -> ... -> dom(T) | Algebraic convergence of domains in the inclusion order | Reed-Simon I, VIII.25 |
| IN | Channel capacity convergence: the channel T_n^{-1} approximates T^{-1} faithfully | Faithful state approximation: omega_n -> omega with no information loss | Quantum info: Wilde, Thm 11.9.5 |

### Concept: discrete compactness

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | Compact resolvent: (T-z)^{-1} is compact for z in rho(T) | Discrete spectrum with finite multiplicities | Boegli Def 2.4 |
| GE | Rellich-Kondrachov: H^1 embeds compactly into L^2 | Bounded domain with smooth boundary -> compact embedding | Adams-Fournier, Sobolev Spaces |
| AL | Ascending chain condition on eigenspaces | Each eigenspace is finite-dimensional; no accumulation except at infinity | Functional analysis folklore |
| IN | Finite channel capacity at each scale: I(X_n; Y_n) < C for all n | Uniform information bound prevents entropy blow-up | Shannon 1948 + RK analogy |

### Concept: spectral exactness

| Domain | Image | Key property | Reference |
|---|---|---|---|
| SP | spec(T) = lim spec(T_n): no ghosts, no gaps | The spectrum of the limit is the limit of the spectra | Boegli Thm 2.6 |
| GE | Hausdorff convergence of spectra as subsets of C | spec(T_n) -> spec(T) in the Hausdorff metric on compact subsets | Chatelin 1983, Ch. 3 |
| AL | Exact functor: the spectrum functor commutes with limits | lim(spec(-)) = spec(lim(-)) when DC holds | Category theory: exact sequences |
| IN | No information loss in the limit: lim I(X_n) = I(lim X_n) | The limit channel has the same capacity as the limit of channel capacities | Information continuity |

---

## PATTERNS -- Six Patterns analysis per load-bearing step

### Step 1* (gsrc definition): P4 (Topological Rigidity)

The gsrc definition is a **completeness condition**: norm convergence of resolvents at one point z propagates to all z in the connected component. This is topological rigidity -- the convergence at one point **locks** the convergence everywhere via the resolvent identity.

The resolvent identity: (T-z)^{-1} - (T-w)^{-1} = (z-w)(T-z)^{-1}(T-w)^{-1}

This is the mechanism. If ||(T_n-z)^{-1} - (T-z)^{-1}|| -> 0 at one z, the resolvent identity propagates the convergence to nearby w, and by connectedness, to the entire connected component.

**Attack angle**: check whether the propagation argument requires uniform bounds on ||(T_n-z)^{-1}||. If uniform bounds are assumed but not stated, that is an implicit hypothesis.

### Step 2* (spectral inclusion): P1 (Geometric Reinterpretation)

Spectral inclusion (spec(T) subset lim spec(T_n)) can be reinterpreted geometrically: the spectrum is a subset of C, and the inclusion is a containment of sets. The geometric picture: spec(T_n) are shrinking (or deforming) subsets of C, and in the limit, their closure contains spec(T).

The proof likely uses: if lambda is in spec(T), then (T-lambda) is not invertible, so ||(T-lambda)^{-1}|| = infinity, so by gsrc, ||(T_n-lambda_n)^{-1}|| must blow up for some sequence lambda_n -> lambda, which means lambda_n is near spec(T_n).

**Attack angle**: does the proof handle the case where lambda is in the continuous spectrum (not an eigenvalue) correctly? The RH proof only needs the point spectrum case, but the general theorem should handle all spectral types.

### Step 3* (no spurious eigenvalues): P6 (Projection Diagnosis)

Spurious eigenvalues are **artifacts of finite truncation**. They appear when the finite-dimensional approximation T_n has eigenvalues that do not correspond to any eigenvalue of the limit T. Discrete compactness kills them: any sequence of approximate eigenvectors must have a convergent subsequence, and the limit vector is an eigenvector of T.

This is P6: the "paradox" (spurious eigenvalues) is an artifact of "projecting away" the infinite-dimensional tail. Discrete compactness restores the tail (via compactness of the embedding).

**Attack angle**: the proof must show that discrete compactness forces convergent subsequences of eigenvectors, not just of arbitrary sequences. Check whether the proof correctly handles the case where eigenvalues have multiplicity > 1.

### Step 5* (Teschl interface): P4 (Topological Rigidity)

The KLMN condition a < 1 is a **quantized constraint**: the perturbation V must be strictly smaller than the unperturbed operator T in a precise sense. This is topological rigidity: the smallness condition is a gap condition (a < 1, not a <= 1), and gaps are topologically robust.

**Attack angle**: does Teschl's Lemma 2.7 produce gsrc in Boegli's exact sense (operator norm convergence of resolvents), or a weaker notion? If weaker, is the weaker notion sufficient for Boegli's Theorem 2.6?

---

## OPERATIONS -- Key operations in Boegli's proof

| Operation | Spectral | Geometric | Algebraic | Information |
|---|---|---|---|---|
| Resolvent (T-z)^{-1} | Central object: encodes all spectral data | Green's function / fundamental solution | Inverse element in the resolvent algebra | Channel: maps input z to output (T-z)^{-1} |
| Limit spec(T_n) -> spec(T) | Spectral convergence | Hausdorff convergence of subsets | Direct limit of spectra | Rate convergence of channels |
| Spectral projection E_lambda | Projection onto eigenspace | Restriction to fiber over lambda | Idempotent in endomorphism ring | Conditional expectation given eigenvalue |
| Compact embedding H^1 -> L^2 | Discrete compactness | Rellich-Kondrachov | Ascending chain on eigenspaces | Finite capacity per scale |
| Resolvent identity | Propagation tool for gsrc | Parallel transport of Green's function | Cocycle relation in resolvent algebra | Channel composition identity |
| Norm estimate ||(T-z)^{-1}|| | Distance from z to spectrum | Geometric distance in resolvent set | Norm in operator algebra | Signal-to-noise ratio |

---

## FRAMEWORK INTERFACE

### Boegli -> RH proof chain

| Boegli step | RH layer | What it provides |
|---|---|---|
| Step 1 (gsrc def) | Layer 4 setup | Defines the convergence notion used throughout Layer 4 |
| Step 2 (SI) | Layer 4 intermediate | Guarantees no Riemann zeros are missed in the limit |
| Step 3 (NSE = Thm 2.6) | **Layer 4 main** | Guarantees no spurious zeros contaminate the limit spectrum |
| Step 4 (s.a. specialization) | Layer 4 refinement | Applies since CCM operators D_N are self-adjoint |
| Step 5 (Teschl) | **Layer 4 verification route** | Provides the simplified path to checking gsrc for CCM operators |

**Combined**: Steps 3 + 5 together close RH Layer 4. Step 3 provides the general theorem. Step 5 provides the verification that the CCM operators satisfy the hypotheses.

### RH proof chain -> Boegli (what the RH proof feeds INTO Boegli)

| RH component | Boegli hypothesis verified |
|---|---|
| CF uniform decay (Layer 3.4) | H1 (gsrc): resolvent convergence |
| ITPFI form convergence (Layer 2) | H1 (gsrc): strengthens the convergence |
| Teschl Lemma 2.7 + KLMN bound | H1 (gsrc): simplified verification route |
| Uniform H^1 bound (Layer 3.3) | H2 (DC): Fourier cancellation gives uniform Sobolev bound |
| Rellich-Kondrachov on bounded domain | H2 (DC): compact embedding from H^1 to L^2 |

---

## ESCALATION ROUTES (pre-identified, per step)

### Step 1 (gsrc definition)

| Tier | Route | Source |
|---|---|---|
| B | Verify against Kato's original definition (Perturbation Theory, IV.2). If Boegli's differs, determine whether the difference matters for the RH application. | Kato 1966, 2nd ed. 1976 |
| C | Not applicable (definitions cannot be "constructed around" -- if the definition is ill-posed, use a different definition entirely) | -- |

### Step 2 (spectral inclusion)

| Tier | Route | Source |
|---|---|---|
| B | Stummel's approximation theory (1970s): spectral inclusion via collectively compact operators. Independent route to the same result. | Stummel, Diskrete Konvergenz linearer Operatoren, I-III |
| B | Vainikko's regular convergence: if T_n -> T regularly, then spec(T) subset lim spec(T_n). Check if gsrc implies regular convergence. | Vainikko, Funktionalanalysis der Diskretisierungsmethoden, 1976 |
| C | Prove spectral inclusion directly for CCM operators D_N using their explicit matrix structure, without any general theorem. | Paper 13 Layer 1 + finite matrix spectral theory |

### Step 3 (no spurious eigenvalues -- THE critical step)

| Tier | Route | Source |
|---|---|---|
| B | Chatelin's spectral approximation framework (1983): different approach to the same "no spurious eigenvalues" conclusion, using collectively compact convergence. | Chatelin, Spectral Approximation of Linear Operators, 1983 |
| B | Stummel-Vainikko discrete compactness: the 1970s theory predates Boegli and gives similar results under slightly different hypotheses. Check if RH hypotheses satisfy Stummel-Vainikko. | Stummel 1970-73, Vainikko 1976 |
| C | Construct spectral exactness directly from ITPFI structure: D_N operators are finite-dimensional (each E_N^+ is finite-dim), so spectral convergence might follow from finite matrix perturbation theory + the specific ITPFI structure, bypassing any general operator theory. | Paper 13 Layer 2 (ITPFI) + Kato Ch. II (finite-dim perturbation) |
| C | Use the explicit eigenvalue formulas for D_N (from CCM) to prove convergence directly, without routing through Boegli's abstract framework. | CCM 2025, Theorem 5.10 |

### Step 4 (self-adjoint specialization)

| Tier | Route | Source |
|---|---|---|
| B | Not needed -- Step 4 follows from Step 3. If Step 3 survives, Step 4 survives. | -- |
| C | Not needed. | -- |

### Step 5 (Teschl interface)

| Tier | Route | Source |
|---|---|---|
| B | Use Boegli's original gsrc definition directly (check gsrc for CCM operators without Teschl's simplification). Teschl is a CONVENIENCE, not a load-bearing dependency. | Boegli Def 2.1 + direct computation |
| B | Use Reed-Simon's Kato-Rellich perturbation theory (Thm X.12) to verify self-adjointness and resolvent convergence directly. | Reed-Simon II, Thm X.12 |
| C | Prove gsrc for CCM operators from first principles using the Nelson commutator theorem instead of KLMN. | Nelson 1959, Reed-Simon II Thm X.36 |

---

## BACKGROUND TOOLKIT -- Five-field cards

### TK-1: Resolvent convergence (norm)

| Field | Content |
|---|---|
| **WHAT** | If ||(T_n-z)^{-1} - (T-z)^{-1}|| -> 0 in operator norm for some z in rho(T), then the same holds for all z in the connected component of the common resolvent set containing z. |
| **WHY** | This is the propagation mechanism for gsrc. One-point convergence implies everywhere convergence via the resolvent identity. |
| **DATA** | Resolvent identity: R_T(z) - R_T(w) = (z-w)R_T(z)R_T(w). Neumann series: R_T(w) = sum_{k=0}^infty (z-w)^k R_T(z)^{k+1}, converging for |z-w| < ||R_T(z)||^{-1}. |
| **USE** | Foundation for Step 1 verification. Check that propagation argument is rigorous. |
| **STATUS** | ESTABLISHED (standard functional analysis, Kato Ch. IV) |

### TK-2: Rellich-Kondrachov compact embedding

| Field | Content |
|---|---|
| **WHAT** | On a bounded domain Omega in R^n with Lipschitz boundary, the Sobolev embedding W^{1,p}(Omega) -> L^q(Omega) is compact for q < p* (Sobolev conjugate) or q < infinity when p > n. In particular, H^1(Omega) -> L^2(Omega) is compact for bounded Omega. |
| **WHY** | This provides discrete compactness (hypothesis H2) for the CCM operators: if dom(D_N) has a uniform H^1 bound, the embedding into L^2 is compact, so bounded sequences have convergent subsequences. |
| **DATA** | Classical. See Adams-Fournier, Sobolev Spaces (2003), Thm 6.3. Also Brezis, Functional Analysis (2011), Thm 9.16. |
| **USE** | Background for Steps 3 and 5. Not itself a verification target (classical result). |
| **STATUS** | CLASSICAL (textbook-level, no verification needed) |

### TK-3: KLMN theorem (Kato-Lions-Lax-Milgram-Nelson)

| Field | Content |
|---|---|
| **WHAT** | Let T be self-adjoint and V be a symmetric operator with ||Vu|| <= a||Tu|| + b||u|| for all u in dom(T), with a < 1. Then T + V is self-adjoint on dom(T) and essentially self-adjoint on any core of T. |
| **WHY** | Teschl's Lemma 2.7 uses the KLMN bound (a < 1) to simplify the verification of gsrc. Instead of checking resolvent norm convergence directly, check the relative bound of the perturbation. |
| **DATA** | Reed-Simon II, Thm X.12 (Kato-Rellich). The KLMN extension: if the form bound a < 1, self-adjointness follows via the Friedrichs extension. See Reed-Simon II, Thm X.17. |
| **USE** | Background for Step 5. The KLMN bound is the bridge between Teschl and Boegli. |
| **STATUS** | CLASSICAL (textbook-level, no verification needed) |

### TK-4: Spectral projections and spectral measure

| Field | Content |
|---|---|
| **WHAT** | For a self-adjoint operator T, the spectral theorem gives T = integral lambda dE_lambda, where E_lambda is the spectral projection onto the eigenspace below lambda. The spectral measure mu_phi(S) = <phi, E(S) phi> encodes the distribution of spectrum relative to a vector phi. |
| **WHY** | Step 4 (self-adjoint specialization) involves spectral measure convergence. The Verifier needs to know what "spectral measure convergence" means precisely. |
| **DATA** | Reed-Simon I, Thm VIII.6 (spectral theorem). Spectral projections: E_lambda = (1/2pi i) oint_{|z-lambda|=epsilon} (T-z)^{-1} dz (Riesz integral). |
| **USE** | Background for Step 4. |
| **STATUS** | CLASSICAL |

### TK-5: Hurwitz's theorem (for context -- not a verification target)

| Field | Content |
|---|---|
| **WHAT** | If f_n -> f uniformly on compacts, f is not identically zero, and f_n have zeros only at z_n^{(k)}, then the zeros of f are limits of the zeros of f_n (and conversely, every limit point of zeros of f_n is a zero of f, unless f vanishes identically). |
| **WHY** | This is RH Layer 5, which depends on Layer 4 (Boegli). The connection: Boegli provides spec(D_infinity) = lim spec(D_N) at the operator level; Hurwitz provides the analogous statement at the zero-of-function level. Together they close the RH argument. |
| **DATA** | Hurwitz 1893. Standard complex analysis. See Conway, Functions of One Complex Variable II, Thm 2.5. |
| **USE** | Context only. Not a verification target in this run. |
| **STATUS** | CLASSICAL (130+ years old) |

### TK-6: Galerkin norm resolvent convergence (classical)

| Field | Content |
|---|---|
| **WHAT** | For operators with compact resolvent and Galerkin projections P_N with P_N → I strongly, the Galerkin resolvents converge in norm: ‖(P_N T P_N - z)^{-1} P_N - (T-z)^{-1}‖ → 0. |
| **WHY** | Provides gnrc for CCM operators WITHOUT needing Teschl's condition (2.1). Classical route that bypasses the WEAKENED citation. |
| **DATA** | Chatelin, *Spectral Approximation of Linear Operators*, 1983, Ch. 3. Also Stummel 1970--73, Vainikko 1976. |
| **USE** | Repair route for Step 5* WEAKENED verdict. Combined with second resolvent identity and ‖Δ_N‖ → 0, gives gnrc directly. |
| **STATUS** | CLASSICAL (textbook-level) |

### TK-7: ADVANCED — gsr suffices for spectral inclusion

| Field | Content |
|---|---|
| **WHAT** | Boegli's Theorem 2.3 (spectral inclusion) requires only gsr (strong resolvent convergence), not gnr (norm). The RH chain has more margin than needed at Step 2. |
| **WHY** | Discovered by V2. If gnrc ever becomes hard to verify, gsr is an easier fallback. |
| **DATA** | Boegli 2017, Thm 2.3 proof uses dominated convergence, not norm estimates. |
| **USE** | Amplification candidate: for future tiers, gsr may suffice where gnrc is hard to check. |
| **STATUS** | ESTABLISHED |

---

## AUTHORS' HONEST STATEMENTS

### From Boegli 2017

The paper is focused and does not flag open problems in the main results. The framework is presented as a generalization of existing spectral approximation theory (Stummel, Vainikko, Chatelin) to non-self-adjoint operators.

Key honest statements:
- The gsrc definition (Def 2.1) is noted as stronger than strong resolvent convergence -- the author is explicit about this distinction
- Theorem 2.6 requires BOTH hypotheses (gsrc AND discrete compactness) -- neither alone suffices
- The self-adjoint case (Thm 2.4(ii) + Thm 2.6 s.a. case) is noted as a simplification, not a separate theorem

**No red flags in the paper's own self-assessment.** The author does not flag gaps, open cases, or unresolved technical issues in the main results. This is consistent with a clean, focused paper.

### From Teschl et al. 2026

This is a preprint (not yet peer-reviewed as of April 2026). The authors note:
- Lemma 2.7 provides a SIMPLIFICATION of checking gsrc, not a new result
- The KLMN bound condition (a < 1) is sufficient but not necessary for gsrc
- The paper's main focus is elsewhere (on a different application); Lemma 2.7 is a tool

**Assessment**: Teschl's Lemma 2.7 is a convenience route. If it fails verification, the RH proof can verify gsrc directly via Boegli's original definition. Teschl is NOT load-bearing for the RH chain; it is load-bearing only for the simplified verification route.

---

## INDEX -- Source access pointers

```
@FETCH-1: arXiv:1604.07732 (Boegli 2017, full paper)
  URL: https://arxiv.org/abs/1604.07732
  Key sections: Def 2.1 (gsrc), Thm 2.3 (SI), Def 2.4 (DC), Thm 2.6 (SE), Cor 2.8 (s.a.)
  Download via: WebFetch https://arxiv.org/pdf/1604.07732

@FETCH-2: arXiv:2601.10476 (Teschl et al. 2026)
  URL: https://arxiv.org/abs/2601.10476
  Key sections: Lemma 2.7 (KLMN -> gsrc)
  Download via: WebFetch https://arxiv.org/pdf/2601.10476

@FETCH-3: Paper 13 RH proof chain (for framework interface)
  Path: paper13-rh/preprint/00-proof-skeleton.md
  Key sections: Layer 4 description

@FETCH-4: RH Sections 8-9 (where Boegli is applied)
  Path: paper13-rh/preprint/sections-06-10.md
  Key sections: section 8 (spectral exactness application), section 9 (Hurwitz)

@FETCH-5: Framework kills and corrections
  Path: paper13-rh/preprint/sections-11-14.md
  Key sections: Sections 11-14 (honest negatives, corrections, verification)
```

---

## HONEST ASSESSMENT

This is a published paper in a reputable journal. The proofs use standard functional analysis machinery. The author (Sabine Boegli, Durham University) is an active researcher in spectral theory with a track record of rigorous work in this area.

**Expect all 5 steps to SURVIVE.** The value of this pilot is in validating the verification cascade architecture, not in finding gaps in Boegli's work. If a step does SURVIVE, we know the architecture works and can proceed to Tier 1 (CCM) with confidence. If a step is WEAKENED, we have learned something valuable about both Boegli's theorem and our verification method.

The discipline is the product. The discovery, if any, is a bonus.

---

## MERGE LOG

| Date | Run | Cards added | Cards updated | Kills added | Escalations | Notes |
|---|---|---|---|---|---|---|
| 2026-04-13 | v1 build | 5 TK cards | 0 | 0 target-specific | 0 | Initial capacitor build |
| 2026-04-13 | v2 post-run | 2 TK cards (TK-6, TK-7) | Step statuses (all SURVIVED+LOCK), Step 4 ref fix, Step 5 repair | 1 (K-T4-1) | 0 | Run closed. All 5 steps SURVIVED+LOCK. Paper 13 Section 9.1 repaired. |
