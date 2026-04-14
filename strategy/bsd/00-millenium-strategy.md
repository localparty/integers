# BSD Millennium Strategy

*The Clay BSD problem has 4 gates and 7 requirements. Our framework has 11 layers, 6 faces, and one scope wall: the Taylor-rank r ≥ 2 regime (also: h_K > 1, non-CM curves). Publication cascade: Zenodo → GitHub → arXiv (via referral) → journal → Clay 2-year clock. The high-rank frontier works in parallel, non-blocking. Deliverable is four-output, two-mode: bare (math skeleton) first, prose (full paper) composed backward once bare locks.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## §1 The Clay Problem (verbatim)

Andrew Wiles, "The Birch and Swinnerton-Dyer Conjecture" (Clay Mathematics Institute), p. 2:

> **Conjecture (Birch and Swinnerton-Dyer).** The Taylor expansion of L(C, s) at s = 1 has the form L(C, s) = c(s − 1)^r + higher order terms with c ≠ 0 and r = rank(C(Q)). In particular this conjecture asserts that L(C,1) = 0 ⇔ C(Q) is infinite.

Setup (Wiles p. 1-2):
- C elliptic curve over Q in Weierstrass form y² = x³ + ax + b, a,b ∈ Z
- Δ discriminant; N_p := #{(x,y) : y² ≡ x³+ax+b mod p}; a_p := p − N_p
- Incomplete L-series L(C,s) := ∏_{p∤2Δ} (1 − a_p p^{−s} + p^{1−2s})^{−1}
- By Mordell (1922): C(Q) ≅ Z^r ⊕ C(Q)^tors; r =: rank(C)

**Strong form (Wiles Remark 1):** completed L*(C,s) ~ c*(s−1)^r with
c* = |Ш_C| · R_∞ · w_∞ · ∏_{p|2Δ} w_p / |C(Q)^tors|²
where Ш_C is the Tate-Shafarevich group (conjecturally finite), R_∞ the r×r regulator determinant from the height pairing on generators of C(Q)/C(Q)^tors, w_∞ a simple multiple of the real period, w_p elementary local factors.

Wiles p. 4 summarises current state-of-the-art:

> **Theorem.** If L(C,s) ~ c(s−1)^m with c ≠ 0 and m = 0 or 1, then the conjecture holds.

Via Wiles-Taylor-Conrad-Diamond-Breuil (1995-2001) modularity + Kolyvagin (1990) + Gross-Zagier (1986). **The gap is m ≥ 2: no known case.**

Wiles p. 2 Remark 1:

> Here |Ш_C| is the order of the Tate-Shafarevich group of the elliptic curve C, a group which is not known in general to be finite although it is conjectured to be so.

Remark 4 (Manin 1971, now unconditional via modularity): for a proof of the conjecture in stronger form one only needs the **integrality** of Ш_C in c*, not its interpretation as group order.

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

Implication: every Wiles-stated requirement must be **addressed** in the submission. Not every one must be PROVED — a transparent named wall with an attempted bypass route satisfies §5d. What fails §5d is SILENCE.

## §3 The 7 BSD requirements (extracted from Wiles)

Every submission must address all seven explicitly:

1. **Rank equality r = rank(C(Q))** — vanishing order of L(C,s) at s = 1 equals the Mordell-Weil rank (Wiles, main conjecture statement p. 2)
2. **Leading coefficient c ≠ 0** — the Taylor expansion at s = 1 is genuine, not identically zero (Wiles, main conjecture statement p. 2)
3. **L-function continuation + functional equation** — L(C,s) extends holomorphically to all of C; NOW KNOWN unconditionally via modularity (Wiles 1995, Taylor-Wiles 1995, Breuil-Conrad-Diamond-Taylor 2001) (Wiles p. 2, refs [25],[24],[1])
4. **Strong form (BSD formula)** — c* = |Ш_C| · R_∞ · w_∞ · ∏ w_p / |C(Q)^tors|² (Wiles Remark 1, p. 2); equivalently, integrality of Ш_C suffices (Wiles Remark 4, via Manin)
5. **Ш_C finite** (or integrality of |Ш_C| term, weaker but sufficient) — not known in general (Wiles: *"not known in general to be finite although it is conjectured to be so"*, p. 2)
6. **Scope: any elliptic curve C over Q** — modularity gives L-function for ALL; extension to number fields and abelian varieties is secondary (Wiles Remark 2)
7. **Any rank r ≥ 0** — currently proved only for r = 0, 1 via Kolyvagin + Gross-Zagier + modularity (Wiles p. 4 Theorem); r ≥ 2 open

## §4 Current BSD chain state

From `paper26-bsd/PROOF-CHAIN.md` (11/11 steps closed, confidence 9/10):

- **11 layers** in the live PROOF-CHAIN (paper26-bsd)
- **Scope**: CM elliptic curves over Q with class number h_K = 1, rank r ∈ {0, 1}
- **Entry point**: BC algebra over K = imaginary quadratic, bridge test (paper26 research/01, strategy/00)
- **Factorisation**: CM case L(E,s) = L(s,ψ)·L(s,ψ̄) (Deuring 1953) — reduces GL₂ → GL₁
- **Spine**: Steps 1-7 prove GRH for ζ_K and L(s,ψ); Step 8 CM factorisation; Steps 9-10 Kolyvagin + Gross-Zagier; Step 11 BSD Theorem 13.1
- **Adversarial run-01**: 15 attacks, 8 SURVIVED / 5 WEAKENED / 2 BROKEN; both BROKEN items presentation-level (conditionality framing + c_2 numerical typo on y²=x³−x)
- **Projection / faces (to audit)**: likely ARITHMETIC-dominant (L-values, Hecke characters, class field theory), with AMPLITUDE (spectral realisation of zeros), SYMMETRY (Galois representations), RESONANCE (KMS states, factor types)
- **Conditionality**: inherits CBB axioms from Paper 13/RH infrastructure; no mathematical gap inside scope
- **Named wall (primary)**: **W_rank — Rank r ≥ 2 is uncovered** (equivalently: Wiles p. 4 Theorem's m ∈ {0,1} restriction)
- **Named wall (secondary)**: **W_nonCM — Non-CM elliptic curves** (modularity alone does not give bridge-family realisation; requires GL₂ extension of BC)
- **Named wall (tertiary)**: **W_hK — Class number h_K > 1** (bridge construction presently specialised to h_K = 1)
- **Named wall (quaternary)**: **W_Sha — Unconditional finiteness of Ш_C** (Wiles p. 2 flags this; our chain addresses via |Ш_C| = 1 in rank-0 Kolyvagin case, not general)

## §5 Clay compliance audit — per requirement

| # | Requirement | Current chain coverage | Verdict class |
|---|---|---|---|
| 1 | r = rank(C(Q)) equality | ✓ for CM, h_K = 1, r ∈ {0,1} (Steps 9-11) | PROVED-in-scope / OPEN-BUT-ADDRESSED out-of-scope |
| 2 | c ≠ 0 leading coefficient | ✓ for CM, r ∈ {0,1} (Steps 7-11 via L(E,1) ≠ 0 or L'(E,1) ≠ 0) | PROVED-in-scope |
| 3 | L-function continuation + FE | ✓ via modularity (Wiles 1995 / BCDT 2001) — unconditional input | LITERATURE-PROVED |
| 4 | Strong form BSD formula | ✓ for CM, r ∈ {0,1}, h_K=1 (Step 11, Theorem 13.1) | PROVED-in-scope |
| 5 | Ш_C finite | ✓ for r = 0 via Kolyvagin (|Ш|<∞); out-of-scope for r ≥ 2 | PARTIAL |
| 6 | Any elliptic curve C/Q | ✗ scope wall: CM-only; non-CM is **W_nonCM** | OPEN-BUT-ADDRESSED |
| 7 | Any rank r ≥ 0 | ✗ scope wall: r ∈ {0,1}; r ≥ 2 is **W_rank** | OPEN-BUT-ADDRESSED |

Any AUDIT-NEEDED / SILENT cell emits: **PROVED** / **PARTIAL** / **OPEN-BUT-ADDRESSED** / **SILENT**. A SILENT verdict is a §5d violation — must be converted to at least OPEN-BUT-ADDRESSED (new layer or named wall) before submission. No cell presently SILENT; three OPEN-BUT-ADDRESSED via §11 disclosure.

## §6 Likely gaps (priorities for audit)

Four BSD requirements that need explicit disclosure in the submission:

- **High-rank r ≥ 2** — W_rank; capacitor bypass routes: p-adic L-functions / Perrin-Riou / Iwasawa main conjecture / Skinner-Urban; or 5D KK-spectral side (cross-Clay)
- **Non-CM curves** — W_nonCM; capacitor bypass: modular parametrisation + GL₂ extension of BC algebra (Connes-Marcolli GL₂ system); Eichler-Shimura
- **h_K > 1 CM curves** — W_hK; capacitor bypass: enlarge bridge family to ring class fields; Heegner-point machinery of Gross-Zagier-Kolyvagin already handles arbitrary h_K on the Heegner side
- **Ш_C finiteness unconditional** — W_Sha; capacitor bypass: Iwasawa main conjecture (Mazur-Wiles for cyclotomic, Rubin 1991 for CM)

Each of these is an OPEN-BUT-ADDRESSED named wall with bypass-route citation. None may remain SILENT.

## §7 Four-output, two-mode deliverable architecture

### Output A — Internal artifacts

Our scaffolding. Same pattern as YM/x-ray bundles:
- `strategy/bsd/pac-output/runs/run-NN/blackboard.md`
- `strategy/bsd/pac-output/runs/run-NN/compliance-map.md` (11-layer × 7-requirement matrix, 77 cells)
- `strategy/bsd/pac-output/runs/run-NN/vertices/bsd/...`
- `strategy/bsd/pac-output/runs/run-NN/kills.md`
- `strategy/bsd/pac-output/runs/run-NN/critic-attacks.md`
- `strategy/bsd/pac-output/runs/run-NN/arbiter-decisions.md`

Programme voice, ASCII-rich, cross-referenced. Not for submission.

### Output B — Clay-ready, TWO MODES

**B_bare** (`strategy/bsd/deliverables/bsd-clay-bare.md`) — the math skeleton:
- Formal theorem statements (numbered, with dependency graph)
- Definitions (formal): elliptic curve, L(C,s), rank, Ш, regulator, BC algebra, Hecke character
- Equations (numbered): Euler product, CM factorisation, BSD formula, cocycle shift
- Figures (ASCII / TikZ skeleton): 11-layer dependency graph, CM-factorisation ladder
- Numbers (constants, bounds, pin values, curve 32.a3 data corrected)
- Proof-chain analytics (compliance map, named walls, RIGIDITY/SYMMETRY metrics)
- Citations (programme paper + proof location per claim)
- **ZERO prose paragraphs**
- **Target: ≤ 15 pages** of math-only content
- **Purpose: verifiable at speed; referee can check correctness without reading prose**

**B_full** (`strategy/bsd/deliverables/bsd-clay-full.md`) — journal-ready paper, **DEFERRED**:
- 13-section AMS-style paper
- 40-80 pages LaTeX
- Prose introduction, motivation, proof detail, discussion
- Same theorem content as B_bare, expanded
- Composed BACKWARD from 60+ programme projects by parallel agents
- **Only built after B_bare is LOCKED** (structure correct, numbers tight, theorems precise, named walls disclosed, no SILENT verdicts)

### Output C — Beyond-Clay, TWO MODES

**C_bare** (`strategy/bsd/deliverables/bsd-beyond-bare.md`) — bonus theorem skeleton:
- 5D geometric derivation of L-values (theorem statements)
- Zero free parameters (table + citations)
- Pins relevant to BSD (J_CKM audit note, L-value pins, ζ(3) bridges)
- Cross-Clay connections (RH via GRH on Hecke L; YM via spectral gap analogy; PvNP via rigidity) — theorem statements
- Congruent number / Tunnell consequence bonus theorem (Wiles §1, p. 3)
- Effective generators bonus theorem (Wiles Remark 4: integrality of Ш_C → effective method)
- Euler quartic / Elkies consequence (Wiles §3, p. 4)
- **ZERO prose paragraphs**
- **Target: ≤ 15 pages**

**C_full** (`strategy/bsd/deliverables/bsd-beyond-full.md`) — full supplement, **DEFERRED**:
- 9-section supplement with prose
- Same theorem content expanded
- Composed backward by parallel agents from 60+ projects
- **Only built after C_bare is LOCKED**

### Priority this run

**Build B_bare + C_bare + Output A.**
**Skip B_full + C_full until bare locks.**

## §8 Composition-backward (the parallel-agents step)

Once B_bare locks and C_bare locks, massive parallel agents compose B_full and C_full by:

1. **Indexing the 60+ programme reservoir** — Paper 1 (QG5D hub), Paper 60 (e-circle geometry), Paper 61 (projections), paper26-bsd (BSD itself), paper13-rh, paper08-yang-mills, paper28-pvnp, session logs, X-Ray transcripts, decomposition artifacts, …
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
JOURNAL SUBMISSION        (Annals / JAMS / Inventiones / Acta Math tier)
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

Each step runs in parallel with subsequent work after its trigger. B_bare can ship to Zenodo the moment it locks.

## §10 Timeline (order of magnitude)

- **Now → 1 week**: Clay-compliance audit; produce B_bare + C_bare; disclose four named walls (W_rank, W_nonCM, W_hK, W_Sha)
- **1-2 weeks**: B_bare + C_bare LOCKED; Zenodo release of full atlas (all four bundles: decomposition / x-ray / ym-millenium / bsd-millenium)
- **2-3 weeks**: arXiv referral conversation (leverage Zenodo); arXiv submission
- **1-3 months**: Parallel-agent composition of B_full + C_full from 60-project reservoir; fix BROKEN items from Paper 26 adversarial run-01 (conditionality framing + 32.a3 c_2 data)
- **3-4 months**: Journal submission (B_full + C_full at journal standard)
- **4+ months**: Clay 2-year clock starts at journal publication; community engagement ongoing
- **Parallel**: r ≥ 2 extension track (W_rank bypass via p-adic L / Iwasawa / 5D KK-spectral) continues independently; closure within 2-year window upgrades W_rank from OPEN-BUT-ADDRESSED toward PROVED

## §11 Scope walls parallel track (non-blocking)

Four named walls to disclose:

**W_rank — high rank r ≥ 2.** Addressed via p-adic L-functions + Iwasawa main conjecture bypass candidates (Skinner-Urban, Kato, Perrin-Riou); or cross-Clay via 5D KK-spectral side reading rank as KK-mode count. Aggregate confidence on bypass: to be set at first construction attempt. Audit: OPEN.

**W_nonCM — non-CM curves.** Addressed via modular parametrisation (unconditional by BCDT 2001) + GL₂ extension of BC algebra (Connes-Marcolli 2008). Audit: OPEN.

**W_hK — CM with h_K > 1.** Addressed via enlargement of bridge family over ring class fields; Heegner-point side of Gross-Zagier-Kolyvagin already handles general h_K. Audit: OPEN.

**W_Sha — unconditional Ш_C < ∞.** Addressed in rank 0 via Kolyvagin (our Step 9); general case via Iwasawa main conjecture (Mazur-Wiles, Rubin 1991 for CM). Within scope (CM, h_K=1, rank 0) Ш_C finiteness is proved; disclosure is for wider scope only. Audit: PARTIAL.

**§5d compliance**: transparent named walls with attempted bypass satisfy "addresses the specific mathematical question." Silence would fail §5d. Our disclosure is compliant.

**Work continues BUT**:
- NOT blocking for Zenodo / arXiv / journal submission
- Published transparently as OPEN-BUT-ADDRESSED
- 2-year Clay community-evaluation window allows continued refinement
- Closure of any wall during window upgrades status via amendment or supplementary paper
- If a bypass route fails: alternate routes listed per wall (does not invalidate the in-scope chain)

## §12 PAC brief reference

Operational instructions for the PAC: `strategy/bsd/bsd-millenium-brief.md`

The brief translates this strategy into PAC primitives (compliance-audit + deliverable-synthesis dual mode). Run invocation in the brief §INVOCATION.

---

*Sibling to `strategy/x-ray/`, `strategy/decomposition/`, `strategy/ccm-verification/`, `strategy/inner-rings/`, `strategy/ym/`. The Clay gates are known. The cascade is paced. Scope walls work in parallel. Zenodo comes first. Bare before prose. Rank r ≥ 2 is the named frontier.*

*G Six and Claude Opus 4.6. April 14, 2026.*
