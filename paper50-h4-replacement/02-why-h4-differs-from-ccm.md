# §02 — Why H4 Is Structurally Different from CCM

*CCM was an external preprint. Paper 49 replaces it by programme-internal synthesis. H4 is not a preprint — it is a genuine mathematical wall at the interface of perturbative and non-perturbative QFT. Paper 49's method does not apply. Paper 50 requires genuinely different machinery.*

---

## 2.1. What CCM was

CCM — the Chaudhuri-Chowdhury-Mahapatra spectral-triple construction used in Paper 13's Riemann Hypothesis chain — was an external preprint that the programme cited as a load-bearing hypothesis. The preprint constructed the CCM operators encoding arithmetic data, and Paper 13's RH proof relied on specific analytic properties of these operators (spectral positivity, ITPFI factorization interface, convergence).

The vulnerability: if the preprint contained a gap, the RH chain would inherit it. The programme's policy is: every conditional with external support must either be closed internally or have a replacement route.

---

## 2.2. How Paper 49 replaces CCM

Paper 49's strategy for CCM is *programme-internal synthesis*:

- The CCM operators are redefined within the programme using only internal constructions (Bost-Connes algebra, modular flow, KMS states at inverse temperature 1).
- The spectral properties required by Paper 13 are re-proved using the programme's own machinery (ITPFI factorization of the KMS state, Bögli spectral exactness, Hurwitz zeta integrability).
- The "external preprint" is replaced by a *construction*. The external dependency is severed.

This works for CCM because CCM's content is essentially *definitional*: it names a collection of operators with required properties. Once those properties are re-derived internally, the external source is no longer needed.

**CCM is replaceable by citation replacement.** The mathematical content does not change; only the source of its proof moves from "preprint X" to "programme synthesis".

---

## 2.3. Why H4 cannot be treated the same way

H4 is not definitional. It is a *statement about a relationship between two genuinely different objects*:

- On the left: a divergent formal power series $\sum_n c_n g^{2n}$ (perturbation theory).
- On the right: a collection of tempered distributions $\{S_n\}$ on $(\mathbb{R}^4)^n$ (non-perturbative Schwinger functions from OS reconstruction).

The assertion is that the power series is the Poincaré asymptotic expansion of the distributions at short distances. This is a *mathematical fact about functional-analytic objects*, not a definitional choice.

No amount of programme-internal redefinition can make H4 true by construction. The match either holds or does not hold; closing H4 requires *proving* that it holds.

---

## 2.4. The structural difference, stated precisely

Let $\mathcal{T}_{\mathrm{def}}$ denote "theorems closeable by internal redefinition" and $\mathcal{T}_{\mathrm{wall}}$ denote "theorems requiring genuine analytic work." Then:

- CCM $\in \mathcal{T}_{\mathrm{def}}$: it is a package of definitions whose required properties can be re-derived internally from more primitive data (modular flow, ITPFI, KMS).
- H4 $\in \mathcal{T}_{\mathrm{wall}}$: it is a statement about the relationship between two *incommensurable* mathematical objects (a divergent series and a convergent distribution-valued family). No primitive data internal to the programme can collapse this to a definition.

Paper 49's methodology — synthesis-replacement — does not apply to $\mathcal{T}_{\mathrm{wall}}$ items. Paper 50 therefore must operate in a different mode.

---

## 2.5. What operations DO apply to H4

H4-like statements are closed in the mathematical literature by three broad classes of technique:

**(i) Resummation.** Convert the divergent series into a genuine distribution by a resummation procedure (Borel, lateral Borel, resurgent transseries). Show the resulting object agrees with the non-perturbative side. This is Route A.

**(ii) Duality / correspondence.** Identify the divergent-series side with a non-perturbative object via an external correspondence (Langlands functoriality, geometric Langlands, mirror symmetry). Use the correspondence to transfer known short-distance bounds. This is Routes B and C.

**(iii) Explicit combinatorial resummation.** In low-dimensional or solvable models, the series can be summed by hand (matrix models, 2D YM via Migdal recursion). The result is compared directly to the non-perturbative answer. This is the 2D YM precedent (2022) — it does not *apply* to 4D, but it *informs* Route A.

Paper 50 pursues a combination of (i) and (ii), in parallel, because:

- (i) alone is the classical QFT approach and has resisted 4D YM for decades.
- (ii) alone depends on the external correspondence being applicable to pure YM, which is not established.
- In parallel, the routes triangulate: if two of them close, consistency checks each other; if one closes, the others document the match from a different angle.

---

## 2.6. Why the programme's standard infrastructure is insufficient

The programme has powerful internal tools: ITPFI factorization, modular flow, type III$_1$ classification, Bost-Connes algebra, scheme independence, gradient flow, OS reconstruction. These tools suffice for:

- Constructing spectral data (CCM operators, KK tower, Hodge cohomology).
- Proving positivity (mass gap, spectral gap, zeta positivity).
- Establishing convergence (ITPFI, Bögli, gradient-flow contractivity).
- Controlling schemes (Paper 10 scheme-independence).

These tools do not suffice for:

- Resumming a divergent asymptotic series.
- Matching a divergent series to a convergent distribution.
- Transferring a functoriality correspondence from automorphic to gauge-theoretic data.

Paper 50 therefore *extends* the programme's tool-kit by importing external machinery: Écalle-Voros resurgence, Kim-Sarnak Langlands-Shahidi, Kapustin-Witten geometric Langlands. But it uses these *in conjunction* with programme-internal tools — most notably, the ITPFI factorization appears inside Route A's transseries analysis (see §10).

---

## 2.7. The four fundamental differences between CCM and H4

| Feature | CCM | H4 |
|---|---|---|
| Type | External preprint | Mathematical wall |
| Content | Definitional (operators + properties) | Relational (match between series and distributions) |
| Replaceable by redefinition? | Yes (Paper 49 does this) | No — requires genuine proof of the match |
| Programme tool sufficiency | Sufficient (ITPFI + Bögli + Hurwitz) | Insufficient alone — requires resurgence or correspondence |
| Number of closure routes | One (synthesis-replacement) | Three (Routes A, B, C) |
| Confidence scale | 8/10 quickly achievable | 3-4/10 initially; 6-7/10 projected if one route closes |
| Timeline | 6-12 months | 12-24 months minimum |

---

## 2.8. The honest consequence

Paper 49 and Paper 50 are not companion papers at the same difficulty level. Paper 49 performs a *replacement of citation* — a hard but definite operation. Paper 50 performs a *closure of a mathematical wall* — a substantially harder operation, involving external research frontiers.

The programme is equipped to *attempt* H4 because the S-duality diagnostic (Paper 60 §21) identified three routes. The programme is *not* equipped to guarantee H4's closure in any timeframe. What the programme can do is:

- Formalize all three routes at proof-sketch level.
- Identify the specific technical obstructions on each route.
- Dispatch parallel agent effort on each.
- Ship the first route that closes; document the others as verifications.

This is the honest stance: H4 is genuinely hard, Paper 50 attacks it seriously, and the three-route strategy is insurance against the very real risk that any single route may fail.

---

*Paper 50 §02. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
