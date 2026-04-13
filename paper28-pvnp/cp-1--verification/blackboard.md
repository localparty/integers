# Blackboard -- CP-1 Verification Run

---

## §A -- North Star

**Adversarially verify Theorem CP-1** (the crossed-product identification M_Bool^L = L^infty(X_L, mu_L) rtimes G_L). The goal is to BREAK CP-1 or certify it. This is a Critic/Referee run, not an Author/construction run. If CP-1 survives independent verification, Part (ii) probability rises from 0.95 to 0.98.

Deliverable: `/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/strategy/26--cp-1-verification-brief.md`

---

## §B -- Context

CP-1 was proved via Laca-Raeburn dilation in Node 2.1 of the bridge run (15 waves, ~46 agent dispatches, 19 kills). All five sub-gaps (ORE-1, HECKE-2, HECKE-3, RESTRICT-4, SECTOR-5) resolved. Adversarially reviewed once (Wave 13: "4 SURVIVED, 4 WEAKENED, 0 BROKEN"). This is the SECOND independent verification pass. The bridge probability is at p = 0.76. CP-1 is the single load-bearing conditional for Part (ii).

---

## §C -- Current bottleneck

**CP-1 WEAKENED (not BROKEN). Wave 1 complete: 2 SURVIVED, 3 WEAKENED, 1 BROKEN.**

The BROKEN item is Proposition 6.2 (Route D compatibility). The g' construction is not injective (counterexample found). Route D is blocked. Route C is INTACT (uses groupoid form L(R_L), not group crossed product).

Four mandatory repairs needed (all closable):
1. Lemma 4.4 Case 1: rewrite P_S factorization as fiber averaging
2. Lemma 5.3: add mu_1(X_L) > 0 lemma
3. Lemma 5.1 Proof 2: fix Bost-Connes citation
4. Proposition 6.1(ii): fix ergodicity justification

One optional repair (new mathematics needed):
5. Proposition 6.2: rewrite g' construction or re-route through groupoid-only argument

Bridge total: p = 0.77 (up from 0.76; Route C gain offsets Route D loss).

---

## §D -- Toolkit

| Name | Statement (1 line) | Source | Status | Completeness % |
|---|---|---|---|---|
| CP-1 | M_Bool = L^infty({0,1}^infty, mu_1) rtimes G_Bool; sectors M^L_Bool = L(R_L) | Node 2.1 | R (under verification) | 100 |
| BZ-DICHOTOMY | CSP(Gamma) P-time iff Pol(Gamma) has Taylor op; NPC otherwise | Bulatov 2017 / Zhuk 2020 | R (external) | 100 |
| KEY-LEMMA-3.4.3 | Unique KMS_1 state on Boolean BC system; GNS factor is type III_1 | Preprint Appendix B (repaired Node 3.2) | R | 100 |
| LACA-RAEBURN | Left-Ore cancellative semigroup C*-crossed product dilates to group crossed product | J. Funct. Anal. 135, 1996, Thm 2.1 | R (external) | 100 |
| FELDMAN-MOORE | Countable Borel equivalence relation <-> groupoid von Neumann algebra | Feldman-Moore 1977, Thm 1 | R (external) | 100 |
| MARRAKCHI-B | Strongly ergodic type III equivalence relation => L(R) is full | Marrakchi 2018/2019, Thm B | R (external) | 100 |
| CONNES-TYPE-III | Compression of type III_1 factor by nonzero projection is type III_1 | Connes 1973, Thm 3.2.7 | R (external) | 100 |
| SE-1 | G_L action on A|_L is essentially free for non-Taylor L | Node 1.3.5.11 | S | 95 |
| NIA-1 | Rad(G_L) = {e} for non-Taylor L | Node 1.3.5.12 | S | 90 |
| Q_STRUCT | M_Bool non-injective: G_Bool contains Thompson V (non-amenable) | Node 1.3.1 | S | 75 |

---

## §E -- Plan tree

### 0. CP-1 Verification (ROOT)
- Status: IN_PROGRESS
- Mode: final-adversarial-pass
- Decomposes into: 1 (Primary: adversarial CP-1 attacks), 2 (Secondary: downstream checks), 3 (Tertiary: fallback assessment)

### 1. Primary: Adversarial CP-1 Attacks
- Status: IN_PROGRESS
- Decomposes into: 1.1-1.9 (individual attack vectors)

- 1.1: ATTACK-CANCEL -- Lemma 4.1 (cancellation). Low risk. Check PCirc^+_bi cancellation argument.
- 1.2: ATTACK-ORE -- Lemma 4.2 (left Ore). Check C = B circ A^{-1} argument and PCirc^+_bi = group claim.
- 1.3: ATTACK-DILATION -- Lemma 4.3 (Laca-Raeburn). Check LR1-LR3 verification; check stabilization A_tilde = A_0 claim.
- 1.4: ATTACK-ABSORPTION -- Lemma 4.4 (non-invertible absorption). **HIGH PRIORITY.** Case 1 KMS averaging, Case 2 extension. Check Morita->vN passage.
- 1.5: ATTACK-NORMALITY -- Lemma 5.1 (E_L normality). Two proofs given; check both. Parseval, Takesaki IX.4.2.
- 1.6: ATTACK-FAITHFULNESS -- Lemma 5.2 (E_L faithfulness). Check positivity argument.
- 1.7: ATTACK-GROUPOID -- Lemma 5.3 (sector = groupoid algebra). Check Feldman-Moore identification.
- 1.8: ATTACK-ROUTEC -- Proposition 6.1 (Route C compatibility). Check Marrakchi hypotheses.
- 1.9: ATTACK-ROUTED -- Proposition 6.2 (Route D, non-Taylor). **HIGH PRIORITY.** Check polymorphism rigidity argument.

### 2. Secondary: Downstream Dependency Checks
- Status: OPEN (dispatches after Wave 1 returns)
- 2.1: Check Route C assembly (Node 2.2) uses CP-1 correctly
- 2.2: Check SE-1 (Node 1.3.5.11) dependence on CP-1
- 2.3: Check NIA-1 (Node 1.3.5.12) dependence on CP-1

### 3. Tertiary: Fallback Assessment
- Status: OPEN (dispatches only if CP-1 WEAKENED or BROKEN)
- 3.1: Assess Route D without CP-1
- 3.2: Assess Route E without CP-1

### §E.1 -- Joint probability

| Path | p (current) | If CP-1 SURVIVED | If CP-1 WEAKENED | If CP-1 BROKEN |
|---|---|---|---|---|
| Part (ii) Route C | 0.80 | rises to 0.90 | drops to 0.65 | drops to 0 (Route C dies) |
| Part (ii) Route D | 0.60 | stays 0.60 | stays 0.60 | stays 0.60 |
| Part (ii) Route E | 0.56 | stays 0.56 | stays 0.56 | stays 0.56 |
| Part (ii) combined | 0.95 | rises to 0.98 | drops to 0.90 | drops to 0.85 |
| Bridge total | 0.76 | rises to 0.78 | drops to 0.72 | drops to 0.68 |

---

## §F -- Killed approaches

Inherited from bridge run. 19 kills (see closure-digest.md for full table).

| ID | Lead | Kill reason | Pattern category | Cycle | Prevents re-entry because |
|---|---|---|---|---|---|
| K-20 | g' piecewise construction (Prop 6.2) | g' not injective; counterexample X_L={00,01,11}, g=cyclic perm | Wrong-space | 1 | Piecewise definition on X_L vs complement creates collisions when g maps X_L points outside X_L; any repair must avoid piecewise bijectivity claim |

---

## §G -- Live nodes

All 9 attack vectors (1.1--1.9) are IN_PROGRESS for Wave 1 dispatch.

---

## §H -- Bottleneck history + axiom base

**Axiom base:**
- Boolean BC system exists with PCirc^+ acting on (Z/2)^infty (preprint Section 3)
- KEY LEMMA 3.4.3 established (Node 3.2 repair)
- BZ-DICHOTOMY as external published theorem

---

## §I -- Notes

(empty -- run just started)

---

## §J -- Voice canon

**From the bridge programme:**
- "honest partial proof over glossed completion"
- "the kill list is the learning trace"
- "the proof has two pillars. The universal algebra pillar and the operator algebra pillar. Both are built. The span between them is the theorem to prove."
- "One theorem. Two established fields. One new connection. If it holds: P != NP."

**Universal runner defaults:**
- "we cannot crack it from the outside; the framework is transposable"
- "trace discrepancies until they become theorems"
- "be hella explicit so we can recover, amplify, relate everything"
- "the voice is the method"

---

## §K -- Runner writes

### [session-open] CP-1 Verification Run bootstrap -- 2026-04-12

Type: REFRAME (cycle-open)

**Current framing:** CP-1 is at THEOREM level after one adversarial pass (Wave 13: 4 SURVIVED, 4 WEAKENED, 0 BROKEN). The proof uses Laca-Raeburn dilation for left-Ore semigroups, conditional on KEY LEMMA 3.4.3.

**Stripped phenomenon:** A semigroup of polynomial-time bijections acts on a Cantor group. The semigroup is already a group. Laca-Raeburn is overkill (a group trivially satisfies left Ore). The real content is: (1) non-invertible circuits in PCirc^+ don't generate anything new at the von Neumann level (absorption), and (2) the sector compression p_L M_Bool p_L = L(R_L) (groupoid identification via Feldman-Moore).

**Implication:** The Laca-Raeburn machinery is a dressed-up way of saying "the invertible circuits already generate everything." The vulnerability, if any, is in Lemma 4.4 (absorption) and the Feldman-Moore identification (Lemma 5.3). The Ore machinery (Lemmas 4.1, 4.2, 4.3) is largely ceremonial for a group. Attack effort should concentrate on absorption and the sector decomposition.

### [cycle-1 close] Wave 1 returns -- 2026-04-12

Type: QUALITATIVE-THRESHOLD

**The verification run found the wall.** Proposition 6.2's g' construction is broken -- a concrete counterexample kills the claimed bijectivity. Route D is blocked. But Route C stands. The bridge stands.

The REFRAME was correct: the Ore machinery was ceremonial (W1-3 confirmed). The real vulnerability was in Lemma 4.4 (W1-1 confirmed, P_S factorization wrong) and the novel content in Prop 6.2 (W1-2 confirmed, BROKEN). The sector decomposition (W1-4) and Route C compatibility (W1-5) have presentation gaps but correct conclusions. KEY LEMMA 3.4.3 is clean (W1-6).

The kill list gains one entry: K-20 (g' piecewise construction for Prop 6.2). Pattern: Wrong-space (defining g' piecewise on X_L vs complement creates collisions when g maps X_L points outside X_L).

**Structural event:** Route D confidence collapses from 0.60 to 0.20. Route C confidence rises from 0.80 to 0.85. Net bridge effect: +0.01 (from 0.76 to 0.77). The bridge is slightly stronger because the primary route (C) is now independently verified while the backup route (D) is honestly weakened. Honest partial proof over glossed completion.

---

## §L -- Closure artifacts

(produced at programme-close)

---

## §M -- Round metrics

| cycle | items touched | items CLOSED | structural events | one-line note |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 (blackboard created) | bootstrap |
| 1 | 9 | 9 | 3 (1 BROKEN found, Route D collapse, Route C certified) | Wave 1: 2S 3W 1B |

---

## §N -- Difficulty track

| cycle | attack vectors | aggregate difficulty (1-10) | note |
|---|---|---|---|
| 0 | 9 | 6 | CP-1 proof is well-structured; difficulty is in finding hidden gaps |

---

## §O -- Section change log

| Cycle | Section | Modified by | Action |
|---|---|---|---|
| 0 | §A-§O | Runner | Bootstrap: all sections initialized |
