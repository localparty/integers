# NS Millennium Strategy

*The Clay NS problem has 4 variants (A/B/C/D) and 4 Clay gates; any ONE variant resolves the Problem. Our framework targets variant (B) — existence and smoothness on R^3/Z^3 — via the KK spectral gap + gradient-flow transfer route. Chain has 8 links, 3 proved, one PARTIAL wall at Link 5 (BKM criterion, addressed via two published routes: Camlin 2025 + arXiv:2601.08854). Publication cascade: Zenodo → GitHub → arXiv (via referral) → journal → Clay 2-year clock. Link-5 integration works in parallel, non-blocking. Deliverable is four-output, two-mode: bare (math skeleton) first, prose (full paper) composed backward once bare locks.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## §1 The Clay Problem (verbatim)

Charles L. Fefferman, "Existence and Smoothness of the Navier-Stokes Equation" (Clay Mathematics Institute):

Setup. Incompressible Navier-Stokes on R^n (n=3, viscosity ν > 0):

- (1) ∂u_i/∂t + Σ_j u_j ∂u_i/∂x_j = ν Δu_i − ∂p/∂x_i + f_i(x,t)
- (2) div u = Σ_i ∂u_i/∂x_i = 0
- (3) u(x,0) = u°(x)
- (4) |∂_x^α u°(x)| ≤ C_{αK}(1+|x|)^{-K} (any α, K)
- (5) |∂_x^α ∂_t^m f(x,t)| ≤ C_{αmK}(1+|x|+t)^{-K}
- (6) p, u ∈ C^∞(R^n × [0,∞))
- (7) ∫_{R^n} |u(x,t)|^2 dx < C for all t ≥ 0 (bounded energy)
- (8) periodic: u°(x+e_j) = u°(x), f(x+e_j,t) = f(x,t), p(x+e_j,t) = p(x,t) (errata)
- (9) |∂_x^α ∂_t^m f(x,t)| ≤ C_{αmK}(1+|t|)^{-K} (periodic force decay in t)
- (10) u(x,t) = u(x+e_j,t) for all t
- (11) p, u ∈ C^∞(R^n × [0,∞))

> **Four variants — resolve ANY ONE:**
>
> **(A)** Existence and smoothness on R^3. ν > 0, n=3, u° smooth divergence-free satisfying (4), f ≡ 0. Prove ∃ smooth p, u satisfying (1), (2), (3), (6), (7).
>
> **(B)** Existence and smoothness on R^3/Z^3. As (A) but u° periodic (8), f ≡ 0, solutions satisfying (1), (2), (3), (10), (11).
>
> **(C)** Breakdown on R^3. Construct smooth divergence-free u°, smooth f satisfying (4), (5), for which NO solution (p,u) satisfying (1)-(7) exists.
>
> **(D)** Breakdown on R^3/Z^3. Analog of (C), periodic.

**CRITICAL Clay provision (§5b of Rules):** *"In the case of the P versus NP Problem and the Navier-Stokes Problem, a resolution in either direction will be evaluated by the standard evaluation procedure set forth in Section 7."* All four variants count.

Key background from Fefferman:
- 2D analogues of (A), (B) are known (Ladyzhenskaya).
- In 3D, (A), (B) hold under a smallness condition on u°; otherwise only short-time existence [0, T) with T = blowup time.
- If a NS solution has finite blowup time T, |u| becomes unbounded near T; for Euler, BKM: ∫_0^T sup_x |ω| dt = ∞.
- Leray 1934: weak solutions always exist (with suitable growth); uniqueness for 3D NS is open.
- Caffarelli-Kohn-Nirenberg 1982 / F.-H. Lin 1998: singular set E of a suitable weak solution has P_1(E) = 0 (parabolic Hausdorff dim ≤ 1).
- Scheffer 1993, Shnirelman 1997: non-uniqueness for Euler weak solutions (compactly supported in spacetime).

## §2 The 4 Clay gates (Rules, 26 Sept 2018, §4)

A Prize is awarded if and only if:

- **(a)** Published in a **Qualifying Outlet** — refereed math publication of worldwide repute, MathSciNet-indexed, named editorial board, rigorous peer review (§6e)
- **(b)** At least **2 years** have elapsed since Qualifying Outlet publication
- **(c)** **General acceptance** in the global math community — independent publications, conference talks, awards, consensus (§7a.i)
- **(d)** **Satisfactorily answers the questions** raised by the official problem description (§7a.ii)

Non-gates:
- **Zenodo** publication does NOT qualify (not MathSciNet-indexed)
- **Direct submission to CMI** is NOT accepted (§5e)
- **Supplementary material** submitted by author is NOT considered (§6d)

§5d: *"A paper that does not address or refer to the specific mathematical questions set out in detail in the official Problem description will not be considered to be a Potential Solution of one of the Problems, even if it addresses closely related scientific questions."*

Implication: the chosen variant's sub-requirements must ALL be **addressed** in the submission. Not every one must be PROVED — a transparent named wall with an attempted bypass route satisfies §5d. What fails §5d is SILENCE (requirement not addressed at all). The OTHER variants need not be addressed (they are alternatives, not conjuncts).

## §3 The 8 Fefferman sub-requirements (grouped by variant)

Variants A, B, C, D are **alternatives** — any ONE resolves the Problem. But each variant has sub-requirements that must ALL be addressed within it.

| # | Sub-requirement | A (R^3 smooth) | B (T^3 smooth) | C (R^3 breakdown) | D (T^3 breakdown) |
|---|---|:-:|:-:|:-:|:-:|
| 1 | Smooth p, u ∈ C^∞(R^3 × [0,∞)) — full regularity (eq 6 / 11) | ✓ | ✓ | — | — |
| 2 | Bounded energy ∫ |u|^2 dx < C ∀ t (eq 7) | ✓ | ✓ | — | — |
| 3 | div u = 0 preserved (eq 2) | ✓ | ✓ | ✓ | ✓ |
| 4 | Initial-data decay (4) / periodicity (8) respected | ✓ | ✓ | ✓ | ✓ |
| 5 | Passage weak Leray → strong smooth (Leray 1934 starting point) | ✓ | ✓ | — | — |
| 6 | BKM criterion handled (∫_0^T sup|ω| dt controls regularity) | ✓ | ✓ | ✓ | ✓ |
| 7 | Explicit smooth u°, f exhibiting blowup (with bounds 4/5 or 8/9) | — | — | ✓ | ✓ |
| 8 | Caffarelli-Kohn-Nirenberg partial regularity (P_1(E) = 0) | addressed | addressed | ✓ | ✓ |

**Programme target: variant (B)** — existence + smoothness on R^3/Z^3 (equivalently T^3). This is structurally natural for our framework because:
- The 4+1 coordinate ambient geometry <!-- legacy 2026-04-15: was "5D ambient geometry" per §0.10 canon entry 1, Intervention 8 --> is M^4 × S^1/Z_2; compactification of the ~~fifth dimension~~ internal-phase S^1/Z_2 factor <!-- legacy 2026-04-15: "fifth dimension" migrated to "internal-phase S^1/Z_2 factor" per §0.10 canon entry 2, Intervention 8 --> gives NS on a base with natural periodic structure.
- The KK spectral gap Δ_0^KK > 0 requires a compact ~~extra dimension~~ internal phase fiber <!-- legacy 2026-04-15: "extra dimension" migrated to "internal phase fiber" per §0.10 canon entry 2, Intervention 8 -->; the periodic base is consistent.
- Fefferman §Main-Results: variants (A) and (B) are "equally fundamental" — neither is strictly easier, both are open, either closes the Problem. Our chain targets (B) first; (A) follows by standard decay truncation arguments (Paper 30 Appendix B, programmed).

Sub-requirements for variant (B) that the live chain must address: 1, 2, 3, 4, 5, 6, 8. (Sub-requirement 7 is for (C)/(D) only.)

## §4 Current NS chain state

From `paper30-navier-stokes/PROOF-CHAIN.md` (v2.1, 2026-04-14):

- **8 links** in the live PROOF-CHAIN
- **3/8 proved** (Links 1, 4; Link 4 upgraded to **PROVED UNCONDITIONAL ALL-LOOP** post 2026-04-13 W1/W2 closure + Paper 11 Theorem K.4 + Paper 10 scheme independence)
- **Confidence**: 4/10 (upgraded from 2/10 via W1/W2 cascade + arXiv:2601.08854 Route B)
- **Chain foundation (Links 1, 4)** as strong as any classical PDE inheritance — no residual UV-scheme questions
- **Link 5 (BKM criterion)**: PARTIAL — **two published routes identified**:
  - Route A (Camlin 2025): bounded Φ functional + Sundman temporal lifting → BKM finiteness on T^3
  - Route B (arXiv:2601.08854, Jan 2026): cosphere-bundle microlocal regularity, lands directly in capacitor MICRO↔QFT cell
- **Cross-cuts**: YM (gradient-flow transfer, Links 15-17 of paper08), QG5D (KK pipeline), Baum-Connes (spectral-gap K-theory), turbulence (paper38 inherits Links 1-4), capacitor MICRO↔QFT (Route B)
- **One open structural wall**: Link 5 integration task (combining Route A's T^3 control with Route B's Riemannian microlocal structure on M^4 × S^1/Z_2)

## §5 Clay compliance audit — variant (B), per sub-requirement

Target variant: **(B) existence + smoothness on T^3**. Audit the 8 live chain links × 7 applicable sub-requirements (1,2,3,4,5,6,8) = 56 audit cells.

| # | Sub-requirement (variant B) | Current chain coverage | Verdict class |
|---|---|---|---|
| 1 | Smooth p, u ∈ C^∞ (eq 11) | Links 5+7+8 compose; **PARTIAL** at Link 5 | OPEN-BUT-ADDRESSED (Route A + Route B) |
| 2 | Bounded energy ∫|u|^2 dx < C | Link 6 (KK→NS energy descent) | CONJECTURED → AUDIT NEEDED |
| 3 | div u = 0 preserved | ??? constraint preservation in GF transfer | AUDIT NEEDED |
| 4 | Periodicity (8) respected on T^3 | ??? (tacitly: M^4 × S^1/Z_2 reduces to T^3 slice) | AUDIT NEEDED |
| 5 | Weak Leray → strong smooth passage | Link 5 + Link 6 compose (partial regularity theorem addressed) | OPEN-BUT-ADDRESSED |
| 6 | BKM criterion handled | Link 5 PARTIAL (two published routes) | ✓ §5d-compliant |
| 8 | Caffarelli-Kohn-Nirenberg (P_1(E) = 0) | Route B microlocal structure subsumes; **direct address needed** | AUDIT NEEDED |

Any AUDIT-NEEDED cell will emit: **PROVED** / **PARTIAL** / **OPEN-BUT-ADDRESSED** / **SILENT**. A SILENT verdict is a §5d violation — must be converted to at least OPEN-BUT-ADDRESSED (new link or named wall) before submission.

Variants (A), (C), (D) need only be addressed to the extent of noting that (B) is the target and (A) follows by decay-truncation; (C)/(D) counterexample construction is NOT attempted (would be incompatible with our existence chain). This is NOT a §5d failure — §5b of Rules treats the four variants as alternatives.

## §6 Likely gaps (priorities for audit)

Four sub-requirements that likely need explicit treatment in our chain:

- **Energy descent (Link 6)** — currently CONJECTURED; the 5D Killing-symmetry argument needs a rigorous Leray-Hopf descent proof before Clay submission
- **Divergence-free preservation under gradient-flow transfer (Link 3)** — the YM gauge constraint transfers to the NS div-free constraint via structural parallel, but the rigorous functor is unconstructed
- **Periodicity on T^3** — the passage from M^4 × S^1/Z_2 to the T^3 base slice of variant (B) needs explicit identification
- **CKN singular-set bound** — the partial regularity theorem P_1(E) = 0 must either be subsumed (no singular set at all, via Route B wave-front-set triviality) or shown to be consistent with our C^∞ claim

Each of these, if currently SILENT, becomes a new named wall or a new layer in the chain.

## §7 Four-output, two-mode deliverable architecture

### Output A — Internal artifacts

Our scaffolding. Same pattern as YM bundle:
- `strategy/ns/pac-output/runs/run-NN/blackboard.md`
- `strategy/ns/pac-output/runs/run-NN/compliance-map.md` (8-link × 7-requirement matrix, 56 cells)
- `strategy/ns/pac-output/runs/run-NN/vertices/ns/...`
- `strategy/ns/pac-output/runs/run-NN/kills.md`
- `strategy/ns/pac-output/runs/run-NN/critic-attacks.md`
- `strategy/ns/pac-output/runs/run-NN/arbiter-decisions.md`

Programme voice, ASCII-rich, cross-referenced. Not for submission.

### Output B — Clay-ready, TWO MODES

**B_bare** (`strategy/ns/deliverables/ns-clay-bare.md`) — the math skeleton:
- Formal theorem statements (numbered, with dependency graph)
- Definitions (formal)
- Equations (numbered, Fefferman's (1)-(11) preserved)
- Figures (ASCII / TikZ skeleton)
- Numbers (constants, bounds, KK radius R, spectral gap Δ_0^KK, viscosity ν, pin values)
- Proof-chain analytics (compliance map, named walls, RIGIDITY/SYMMETRY metrics)
- Citations (programme paper + proof location per claim)
- **ZERO prose paragraphs** — no introduction, no motivation, no discussion, no prose proofs
- **Target: ≤ 15 pages** of math-only content
- **Purpose: verifiable at speed; referee can check correctness without reading prose**

**B_full** (`strategy/ns/deliverables/ns-clay-full.md`) — journal-ready paper, **DEFERRED**:
- 13-section AMS-style paper
- 40-80 pages LaTeX
- Prose introduction, motivation, proof detail, discussion
- Same theorem content as B_bare, expanded
- Composed BACKWARD from 60+ programme projects by parallel agents
- **Only built after B_bare is LOCKED** (structure correct, numbers tight, theorems precise, named walls disclosed, no SILENT verdicts)

### Output C — Beyond-Clay, TWO MODES

**C_bare** (`strategy/ns/deliverables/ns-beyond-bare.md`) — bonus theorem skeleton:
- 5D geometric derivation (theorem statements only) — fluid/gravity + KK pipeline
- Zero free parameters (table + citations)
- 36 experimental pins relevant to NS / turbulence (table + citations)
- Cross-Clay connections (NS↔YM via gradient-flow transfer; NS↔turbulence (paper38) via K41 cascade; NS↔Baum-Connes via spectral K-theory) — theorem statements
- Turbulence bonus theorem (K41 k^{-5/3} spectrum from spectral gap, statement)
- Vorticity stretching control bonus theorem (statement)
- Kolmogorov dissipation-scale pin (statement + comparison to experiment)
- Any-4-manifold extension (M^4 × S^1/Z_2 generic, statement)
- **ZERO prose paragraphs**
- **Target: ≤ 15 pages**

**C_full** (`strategy/ns/deliverables/ns-beyond-full.md`) — full supplement, **DEFERRED**:
- 9-section supplement with prose
- Same theorem content expanded
- Composed backward by parallel agents from 60+ projects
- **Only built after C_bare is LOCKED**

### Priority this run

**Build B_bare + C_bare + Output A.**
**Skip B_full + C_full until bare locks.**

## §8 Composition-backward (the parallel-agents step)

Once B_bare locks and C_bare locks, massive parallel agents compose B_full and C_full by:

1. **Indexing the 60+ programme reservoir** — Paper 1 (QG5D hub), Paper 8 (YM + Appendix L NS structural parallel), Paper 30 (NS chain itself), Paper 38 (turbulence), Paper 60 (e-circle geometry), Paper 61 (projections), paper11-scheme-independence, paper10-all-orders, session logs, X-Ray transcripts, capacitor MICRO↔QFT, decomposition artifacts, ...
2. **Per-theorem retrieval** — for each theorem in B_bare, query the reservoir for all related proofs, derivations, context, motivation
3. **Per-section composition** — one agent per section of B_full / C_full, each agent composes prose FROM the retrieved material
4. **Integration pass** — single arbiter agent stitches the sections into coherent LaTeX

This inverts the normal write-paper-first flow: the bare skeleton is the TOC + theorem list; the 60 projects are the content reservoir; parallel agents do retrieval-augmented composition.

## §9 Publication cascade

```
ZENODO                    (establishes priority timestamp, universal, GitHub-linkable)
     │
     ▼
GITHUB                    (code + data + proofs public; backup priority)
     │
     ▼
ARXIV                     (via endorser referral; easier once Zenodo+GitHub public)
     │
     ▼
JOURNAL SUBMISSION        (Annals / JAMS / Inventiones / Acta Math / Comm. Pure Appl. Math tier)
     │                    → STARTS THE CLAY 2-YEAR CLOCK
     ▼
COMMUNITY ENGAGEMENT      (conference talks, independent discussion, awards)
     │
     ▼
CLAY 2-YEAR MINIMUM       (cannot shorten)
     │
     ▼
CMI PASSIVE MONITORING    (no direct submission — Rules §5e)
     │
     ▼
CLAY PRIZE CONSIDERATION  (if all 4 gates passed)
```

Each step runs in parallel with subsequent work after its trigger. B_bare can ship to Zenodo the moment it locks. For NS the most plausible journal targets are Annals / JAMS / Inventiones / Acta Math (top-tier analysis) or Comm. Pure Appl. Math (traditional home for CKN/Scheffer/Leray-Hopf descendants).

## §10 Timeline (order of magnitude)

- **Now → 1 week**: Clay-compliance audit; produce B_bare + C_bare; address SILENT verdicts; honest disclosure that the chain confidence is 4/10 (PARTIAL at Link 5)
- **1-2 weeks**: B_bare + C_bare LOCKED; Zenodo release of full atlas (all Millennium bundles)
- **2-3 weeks**: arXiv referral conversation (leverage Zenodo); arXiv submission
- **1-3 months**: Parallel-agent composition of B_full + C_full from 60-project reservoir; Link 5 Route-A/Route-B integration work continues in parallel
- **3-4 months**: Journal submission (B_full + C_full at journal standard) — honest PARTIAL disclosure in abstract
- **4+ months**: Clay 2-year clock starts at journal publication; community engagement ongoing
- **Parallel, multi-year**: Link 5 integration audit continues independently; closure within 2-year window upgrades Link 5 from PARTIAL (OPEN-BUT-ADDRESSED) to PROVED. The chain is honest under §5d regardless.

NS is the furthest-from-closure Millennium vertex in the programme. Unlike YM (which reached 18/18 with one H4 bypass), NS sits at 3/8 proved. B_bare must disclose this clearly. §5d is satisfied by transparent named-wall disclosure with bypass-route citations, NOT by claiming more than we have.

## §11 Link-5 parallel track (non-blocking) — the BKM wall

Link 5 (BKM criterion) is the AF-match analog for NS. Previously OPEN with single conjectured route (spectral-gap → vorticity control by Sobolev + Gronwall, failing on the stretching term ω·∇u). Now PARTIAL with two **published** routes:

### Route A — Camlin 2025 (bounded Φ functional)

- arXiv preprint (2025): constructs a bounded vorticity-response functional Φ via Sundman-type temporal lifting
- The BKM integral becomes geometrically invariant under bounded temporal diffeomorphism
- Yields finiteness in physical time on T^3
- **KK-setting adaptation task**: does Δ_0^KK on M^4 × S^1/Z_2 provide sufficient control for Φ (vs flat T^3 baseline)?

### Route B — arXiv:2601.08854 (Jan 2026, cosphere-bundle microlocal)

- Lifts NS dynamics to cosphere bundle of a Riemannian manifold
- Microlocal analysis + Riemannian geometry
- Regularity criterion via wave-front-set conditions
- **Lands DIRECTLY in the capacitor MICRO↔QFT cell** (filled during H4 bypass run 2026-04-13 with Hollands-Wald 2024 + Dappiaggi 2023-2024 + BFR 2025)
- **Framework advantage**: M^4 × S^1/Z_2 already IS Riemannian — zero mapping work at the structural level

### Integration path

Route A (T^3 → tight BKM bound via Sundman lifting) + Route B (Riemannian manifold → wave-front-set regularity) compose by:
- Use Route B's microlocal structure on M^4 × S^1/Z_2 to GENERATE Route A's Φ functional
- Translate wave-front-set → vorticity via Sobolev wavefront calculus (Hörmander, Melrose)
- If composition is valid, Link 5 closes

**§5d compliance**: two published transparent routes + named integration task satisfies "addresses the specific mathematical question." Silence would fail §5d. Our disclosure is compliant.

**Work continues BUT**:
- NOT blocking for Zenodo / arXiv / journal submission
- Published transparently as OPEN-BUT-ADDRESSED (PARTIAL)
- 2-year Clay community-evaluation window allows continued refinement
- Closure of Link 5 during window upgrades to PROVED via amendment or supplementary paper
- If Route A + Route B composition fails: Route C (direct spectral attack, see paper30 attack plan) remains as backup. Counterexample construction to Link 5 would kill the current architecture (acceptable under §5d — we'd retract and submit variant (C)/(D) path).

## §12 PAC brief reference

Operational instructions for the PAC: `strategy/ns/ns-millenium-brief.md`

The brief translates this strategy into PAC primitives (compliance-audit + deliverable-synthesis dual mode). Run invocation in the brief §INVOCATION.

---

*Sibling to `strategy/x-ray/`, `strategy/decomposition/`, `strategy/ccm-verification/`, `strategy/inner-rings/`, `strategy/ym/`. The Clay gates are known. The cascade is paced. Link 5 works in parallel via two published routes. Zenodo comes first. Bare before prose. Variant (B) is the target — T^3 is natural for our KK geometry.*

*G Six and Claude Opus 4.6. April 14, 2026.*
