# Blackboard — H4 Excision Run (Tier B)

*Runner: ORA v8 (Claude Opus 4.6, 1M context). Capacitor: yang-mills-capacitor-v1.md.*
*Brief: ym-h4-excision-brief.md. Mode: EXCISE (Tier B).*
*Run directory: `verification-cascade/ora-generator/yang-mills-proof-chain/h4-excision-run/`*
*Session-open: 2026-04-13. Mode: autonomous parallel dispatch.*

---

## §A — North Star

Prove H4 independently — that the non-perturbative Schwinger functions agree with perturbation theory at short distances — thereby excising the H4 dependency from Step 18 of the YM proof chain. Four routes dispatched in parallel: (1) Analyticity + identity theorem, (2) Borel summability + Watson, (3) Instanton gas, (4) Large-N then finite-N.

## §B — Context

**Prior work (H4 closure run, 2026-04-11):** Three routes attempted and all blocked/killed:
- Route A (Taylor-coefficient identification): BLOCKED-DECOMPOSED. The identity theorem requires F^pert(t) to be analytic, which is not established. Decomposed into R.A.1a (perturbative flow-time analyticity) + R.A.1b (independent-point agreement), both OPEN.
- Route B (CCM 2025 port): KILLED (K-1). Lexical category error — CCM addresses rank-one perturbation of spectral triple, not QFT perturbation theory.
- Route C (spectral action + Identity 12): KILLED (K-2). Spectral action produces bare action at Lambda, not running coupling.
- Route D (editorial HONEST-STALL): SHIPPED. Paper 8 ships 17/18 unconditional.

**The structural LOCK at 9/10**: Taylor-coefficient identification is the attack surface, stuck across three independent pattern categories.

**This run's thesis**: The prior closure run attacked from the IDENTITY THEOREM side (comparing two functions). This run attacks from the CONSTRUCTION side — can we show the non-perturbative construction INHERENTLY produces perturbative-matching short-distance behavior? The four routes represent four independent mechanisms by which non-perturbative = perturbative at short distances.

## §C — Current bottleneck

**Cycle 1 dispatch**: All four routes dispatched simultaneously. The bottleneck is structural: H4 asks whether the perturbative projection faithfully captures the full theory at short distances. The difficulty IS the projection (P6). To close H4, we must show the projected-out structure (instantons, renormalons) is sub-leading.

**Key asset from Lemma L.3.7 Step 2**: F(t) is analytic on |t| < r_t INCLUDING at t=0, with (k,K)-uniform radius. The small-flow-time expansion is CONVERGENT (not merely asymptotic). This means the non-perturbative F(t) has a genuine convergent Taylor series F(t) = sum a_n t^n with |a_n| <= M_F/r_t^n. The question reduces to: are the Taylor coefficients {a_n} equal to the perturbative coefficients {f_n^pert}?

## §D — Toolkit (inherited from capacitor + prior run)

| Name | Status | Key property |
|---|---|---|
| F(t) analytic | PROVED (L.3.7) | Analytic on |t| < r_t, radius (k,K)-uniform |
| c_1(t) entire | PROVED (L.3.1(c)) | Wilson coefficient entire in t |
| Balaban analyticity (B1) | PROVED | k-independent radius rho > 0 |
| Reisz power-counting | ESTABLISHED | Lattice PT = continuum PT at each order |
| Bogomolny bound | ESTABLISHED | S_YM[A] >= 8pi^2|k|/g^2 |
| AF beta function | ESTABLISHED | beta(g) = -b_0 g^3 + O(g^5), b_0 = 11N/(48pi^2) |
| Spiridonov-Chetyrkin | ESTABLISHED | gamma_{Tr F^2} = -2beta(g)/g, exact to all orders |
| Hastings-Koma | ESTABLISHED | Exponential clustering at all RG scales |

## §E — Route status (FINAL)

| Route | Status | Verdict | Output |
|---|---|---|---|
| 1. Analyticity + Identity Theorem | **BLOCKED** | Same obstruction as prior Route A; F(0) = F^pert(0) IS H4 | 01-route-1-analyticity.md |
| 2. Borel Summability + Watson | **BLOCKED (K-3)** | IR renormalon at u=2; Watson requires sector analyticity | 02-route-2-borel.md |
| 3. Instanton Gas | **PARTIAL RESULT** | Instantons (|k|>=1) proved sub-leading O(|x|^{11N/6}); k=0 uncontrolled | 03-route-3-instanton.md |
| 4. Large-N then Finite-N | **BLOCKED (K-4)** | H4 at large N itself open; no rigorous 1/N expansion | 04-route-4-large-N.md |

**EXCISION VERDICT: HONEST-STALL.** See 05-excision-verdict.md.
**CAPACITOR PATCH:** See 06-capacitor-patch.md.

## §F — Kill list (inherited + new)

| Kill # | What | Pattern category | Source |
|---|---|---|---|
| K-1 | CCM 2025 port to YM | External-source-inconsistency + Wrong-space | Prior run |
| K-2 | Spectral action + Identity 12 | External-source-inconsistency + Vacuous | Prior run |
| K-meta | RH and H4 require incompatible NCG machinery | Architectural | Prior run |

## §K — Runner writes

[2026-04-13 cycle 1] REFRAME: The prior run asked "can we MATCH two functions?" This run asks "does the CONSTRUCTION force the match?" The gradient-flow construction builds F(t) from the Balaban polymer integral. The perturbative series is the formal Taylor expansion of F(t) at t=0. The construction ALREADY proves F(t) is analytic at t=0 with convergent Taylor series (L.3.7 Step 2). The question is whether each Taylor coefficient a_n = F^(n)(0)/n! is computable by Feynman rules. This is not a matching problem — it is a COMPUTABILITY problem for the derivatives of an already-constructed analytic function.

[2026-04-13 cycle 1 close] QUALITATIVE-THRESHOLD: All four routes dispatched, executed, and returned. Three BLOCKED, one PARTIAL RESULT. The instanton suppression partial result is genuine and worth adding to the preprint. But H4 stands. The wall is the wall. Seven routes tried across two runs, seven blocked by the same fundamental obstruction: the divergence of the g^2 perturbative series and the absence of a summation method that provably reconstructs the non-perturbative answer within the k = 0 topological sector. The LOCK tightens to 11/10. The only remaining direction is "does the Balaban polymer expansion converge to its perturbative truncation?" — a constructive QFT question that is more specific than generic Borel summability but still hard (8/10). Paper 8 ships as it is. The honest-stall holds.

[2026-04-13 final] COMMIT: 6 files written to h4-excision-run/. Capacitor patch drafted with 2 new kills (K-3, K-4), 3 new cards (15-17), 4 corrections. LOCK updated to 11/10. Mathematical closure probability downgraded from 0.74 to 0.31. Paper shipping probability unchanged at 0.993.
