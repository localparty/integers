# Capacitor Architecture — Verification Cascade

*The capacitor is what turns the ORA from "smart agent reading files" into "expert system that knows what's been tried, what works, what doesn't, and where to look." Without a capacitor, the ORA attempts from scratch and misses existing results. With one, the ORA has deployable knowledge to build on.*

*This file documents the capacitor architecture for the 4 verification tiers of the Millennium Strategy. Each capacitor follows the same pattern proven by the P vs NP toolkit (framework-tools-v4.md), which was the ONLY reason the P vs NP ORA was able to do its job.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-12.*

---

## 1. What a capacitor is

A capacitor is a **charged toolkit** — a file that an ORA run receives at invocation alongside its brief. It contains:

1. **General framework tools** (Sections A-G from `05-framework-tools.md`) — the Six Patterns method, theorem catalogues, grammar, transposition mechanics, dictionaries, prediction table. These are always included. They define the ORA's inner loop and operational register.

2. **Programme-specific files** — pointers to the papers, proofs, and prior work relevant to the verification target. These tell the ORA what to READ.

3. **Deployable verified knowledge** — five-field cards (WHAT/WHY/DATA/USE/STATUS) for each result that's already established. These tell the ORA what it already KNOWS so it doesn't re-derive from scratch.

4. **Kill list** — approaches that have been tried and failed, with WHY they failed and what would justify re-entry. These tell the ORA what NOT to try.

5. **Correspondence logic** — how the external theorem maps to the proof chain. The route-finding tool. This tells the ORA HOW to navigate.

6. **What the external authors themselves flag as open** — the honest-first data from the source material. This tells the ORA where the authors' OWN doubts live.

**The empirical proof:** The P vs NP programme ran twice — once without a capacitor (OA1 cycle-1: Author attempted from scratch, missed PATB-DIAGONAL) and once with one (subsequent waves: Authors had 10 verified results to build on). Three consecutive spawn failures (BSD MY4, OA1, Q_struct) from the same root cause — Authors not having compiled knowledge — led to I-v6-3 → I-v6-4 → I-v6-5 which killed selective inclusion and mandated always passing the capacitor. The capacitor is the ORA's memory.

---

## 2. The difference that matters

| | `05-framework-tools.md` (the map) | `p-v-np-toolkit/framework-tools-v4.md` (the charged map) |
|---|---|---|
| **Nature** | Reference index — "these files exist" | Operational toolkit — "here's what we KNOW" |
| **Content** | File pointers + descriptions | File pointers + five-field cards + kills + correspondence logic + corrections |
| **Who reads it** | Toolkit builders (human/LLM) at design time | The ORA runner + every spawned agent at runtime |
| **Effect on Authors** | Author knows what files to read | Author knows what's VERIFIED, what's KILLED, and where to look next |
| **Unique to P vs NP capacitor** | n/a | Spectral-geometric-information trinity (6/6 verified), 8 kills with WHY, Rule 9 v3 (gate-amplifier), amplification results (6 transposed tools), re-verification corrections (honest downgrades) |

The five-field card format (WHAT/WHY/DATA/USE/STATUS) is the atom of deployable knowledge. Each card is a result the Author can cite directly ("By PATB-DIAGONAL, the Taylor condition is equivalent to..."). Without cards, the Author reads papers and hopes to extract the right fact. With cards, the Author has pre-extracted verified facts with citation templates.

---

## 3. The 4 verification capacitors

### 3.1 Tier 1 — CCM Verification Capacitor

**Target:** Connes-Consani-Moscovici, "Zeta Spectral Triples" (arXiv:2511.22755, November 2025).

**Why this capacitor is special:** The verification target is an EXTERNAL paper by other mathematicians, not the framework's own work. The five-field cards will have status SURVIVED/WEAKENED/BROKEN (adversarial verdicts) rather than VERIFIED (computational confirmation). The capacitor charges the ORA to READ and TEST, not to BUILD.

**What to charge it with:**

| Section | Content | Source | Priority |
|---|---|---|---|
| **The paper structure** | CCM 2025 extracted proof chain: every definition, theorem, lemma, and proof step in logical order. Number each step. This IS the verification target. | Download arXiv:2511.22755, extract via pdftotext, structure as a proof chain | MUST |
| **The precursor results** | CCM 2024 (arXiv:2310.18423, published in Annals of Functional Analysis): what was established in the precursor vs what's new in CCM 2025. The precursor is published and peer-reviewed — results from it are STRONGER than results only in the 2025 preprint. | Download from arXiv/journal | MUST |
| **The interface with Paper 13** | Exactly which CCM results Paper 13 depends on: Theorem 4.2 (self-adjointness of D_N via Caratheodory-Fejer), Theorem 5.10 (eigenvalue convergence to Riemann zeros), Lemma 5.2(i) (T commutes with parity), Lemma 7.2 (eigenvector properties), Lemma 7.3 (Fourier → Xi). Extract from Paper 13 Layer 1 description. | `paper13-rh/preprint/00-proof-skeleton.md` Layer 1 + `paper13-rh/preprint/sections-06-10.md` §6 | MUST |
| **Background toolkit cards** | Five-field cards for the mathematical tools CCM uses: prolate spheroidal wave functions (Slepian-Pollak-Landau theory), Caratheodory-Fejer theorem for Toeplitz matrices (the self-adjointness engine), rank-one perturbation theory, scaling operators on intervals, Euler product truncation. Each card: WHAT the tool is, WHY CCM uses it, where to find it, STATUS (classical/published). | Compile from CCM's own references + standard texts | HIGH |
| **Kill list from prior framework work** | K-1 from H4 closure: the CCM → YM transposition port is Wrong-space (CCM targets zeros of entire function, YM needs Taylor coefficients of analytic function). The "perturbation" lexical confusion: "rank-one perturbation" in CCM is operator-theoretic, NOT QFT perturbation theory — caught by Delta-Critic applying I-v6-1. These kills protect the verification Author from misapplying CCM. | `paper08-yang-mills/closing-H4/closure/closure-digest.md` §Kills (K-1) + §The arc (Delta-Critic CCM catch) | HIGH |
| **What CCM's own authors flag as open** | §7 Outlook p.28: "Justifying rigorously this step is the main remaining obstacle to our approach to RH." The CCM authors are HONEST about what they haven't proved. This is the single most important sentence for the verification — it tells the ORA where the weak point is, from the authors themselves. | CCM 2025 §7 Outlook | MUST |
| **Numerical verification data** | The 55-digit eigenvalue agreement at N=6, the 10^-1235 coincidence probability. These are computational checks the verification Author can reproduce independently. | CCM 2025 §6 Numerical results | HIGH |
| **The Connes publication timeline** | CCM 2021 "Spectral triples and zeta-cycles" → CCM 2024 "Zeta zeros and prolate wave operators" (published) → CCM 2025 "Zeta spectral triples" (preprint). Which results are in published papers vs only in the preprint. Results in published papers are stronger dependencies. | Connes publications page + arXiv | MEDIUM |

**Five-field card template for CCM verification:**

Each CCM theorem gets a card:

```
### CCM-THM-4.2 — Self-adjointness of D_N

| Field | Content |
|:------|:--------|
| **WHAT** | [Statement of Theorem 4.2 — self-adjointness of the rank-one perturbed operator D_N on E_N^+] |
| **WHY** | [Why Paper 13 needs this — it's the foundation for the spectral approximation in Layer 1] |
| **PROOF STEPS** | [Numbered list of proof steps from CCM, extracted from the paper] |
| **VERIFICATION STATUS** | [PENDING → SURVIVED / WEAKENED / BROKEN after ORA verification] |
| **NOTES** | [Any concerns, subtleties, or alternative verification routes] |
```

**Online leads incorporated:**
- CCM 2024 precursor is PUBLISHED (Annals of Functional Analysis) — results from the 2024 paper are stronger than 2025-only results
- No independent verification of CCM 2025 exists anywhere as of April 2026 — first mover advantage
- Lean mathlib has basic self-adjoint operator formalization (`Mathlib.Algebra.Star.SelfAdjoint`) — potential future formalization target but not for this run

---

### 3.2 Tier 2 — Balaban Verification Capacitor

**Target:** Balaban's polymer expansion (CMP 95-119, 1984-1998) at the interface Paper 8 uses.

**Why this capacitor is special:** Dimock (2011-2013) already provides a partial independent re-derivation of Balaban's approach for a scalar phi^4 model. This is a PRE-CHARGED ingredient — the capacitor starts half-full. The verification target is the GAP between Dimock's scalar re-derivation and Balaban's gauge-field original.

**What to charge it with:**

| Section | Content | Source | Priority |
|---|---|---|---|
| **Dimock's re-derivation (the existing second route)** | Three papers re-deriving Balaban's RG for scalar phi^4: I. Small fields, II. Large fields, III. Convergence. These are the INDEPENDENT CHECK that already exists. The verification Author starts here, not from Balaban's originals. | arXiv:1108.1335, 1212.5562, 1304.0705 | MUST |
| **Paper 8's interface** | Steps 1-3 of PROOF-CHAIN.md: which specific Balaban results are load-bearing. Step 1 (Balaban polymer expansion convergence, CMP 109 Thm 1), Step 2 (Balaban UV stability, CMP 109/119), Step 3 (Balaban propagator/kernel analyticity with k-independent radius). | `paper08-yang-mills/preprint/PROOF-CHAIN.md` Steps 1-3 | MUST |
| **The scalar-to-gauge gap** | What Dimock proved (scalar phi^4 on 3D torus) vs what Paper 8 needs (SU(N) Yang-Mills on 4D torus × S^1/Z_2). The differences: gauge symmetry (SU(N) vs scalar), dimension (4+1 vs 3), the Haar measure on group-valued fields, the Faddeev-Popov gauge fixing. The gap IS the verification target. | Compare Dimock's theorems to Paper 8's Balaban citations | MUST |
| **Balaban's original papers (targeted)** | CMP 109 Theorem 1 (convergence), CMP 95-109 (propagator bounds + analyticity), CMP 119 (UV stability). These are the originals the verification Author checks against Dimock's scalar version. | Balaban's CMP papers (via Springer) | HIGH |
| **H4 closure knowledge** | The H4 closure found Balaban's analyticity preservation is load-bearing: $F(t)$ is analytic in the complex flow-time plane (W5-10 Step 2) via Balaban's k-independent radius. This specific analyticity result is the highest-value verification target within Balaban's work. | `paper08-yang-mills/closing-H4/closure/closure-digest.md` | HIGH |
| **The Weitzenboeck-Bochner connection** | Paper 8 Step 4 (Theorem 4) uses Weitzenboeck-Bochner for the KK spectral gap — this is classical and doesn't need Balaban verification, but the Author needs to know where Balaban's territory ends and classical territory begins. | `PROOF-CHAIN.md` Step 4 | MEDIUM |

**Online leads incorporated:**
- Dimock's three papers are the KEY ingredient — they're an independent re-derivation by a different mathematician using Balaban's method on a simpler model. The ORA can use Dimock as the "already-verified base" and focus verification on the scalar-to-gauge extension.
- No other independent verification of Balaban exists in the literature (40 years).
- The nLab page on lattice gauge theory cites Balaban and Dimock as the state of the art for rigorous RG on lattice gauge theories.

---

### 3.3 Tier 3 — Bulatov-Zhuk Verification Capacitor

**Target:** CSP Dichotomy Theorem at the interface Paper 28 uses.

**Why this capacitor is special:** The full Bulatov-Zhuk proofs are extremely long and complex. The verification is NOT of the full proof — it's of the INTERFACE: the classification of the 6 Schaefer classes and the Taylor polymorphism characterization that Paper 28 depends on. This is a targeted interface verification, not a full proof verification.

**What to charge it with:**

| Section | Content | Source | Priority |
|---|---|---|---|
| **The dichotomy statement** | Precise statement: "A finite-domain CSP Gamma is in P if and only if its polymorphism clone contains a Taylor operation; otherwise it is NP-complete." | Bulatov FOCS 2017 / Zhuk JACM 2020 | MUST |
| **The 6 Schaefer classes** | 2-SAT, Horn-SAT, Dual-Horn, XOR-SAT (affine), 1-in-3-SAT, NAE-3-SAT. For each: the constraint language, whether it has a Taylor polymorphism, the complexity class (P or NP-complete), the polymorphism clone structure. | P vs NP toolkit H.3b + Schaefer 1978 | MUST |
| **Existing computational verification** | From the P vs NP toolkit: TGap 6/6 confirmed, holonomy 6/6 confirmed, PATB-DIAGONAL confirmed, polymorphism fingerprint perfect diagonal structure. The computational verification already CONFIRMS the dichotomy classification at the Schaefer-class level. | P vs NP toolkit H.3b, H.3f | MUST |
| **The Taylor characterization** | What "Taylor polymorphism" means precisely: a polymorphism t(x_1,...,x_n) satisfying t(x,...,x) = x and identity equations for all coordinate positions. How this maps to the framework's non-fullness characterization. | Taylor 1977, Barto-Kozik 2022, Strategy 03 | HIGH |
| **The proof structure (targeted)** | Bulatov's absorption theory: the key steps and where the complexity hides. Zhuk's alternative approach via connectivity. NOT the full proof — the structural outline + the specific steps Paper 28 depends on (the classification result, not the algorithm). | Bulatov FOCS 2017 §§1-3, Zhuk JACM 2020 §§1-4 | HIGH |
| **Kill list from P vs NP** | All 18 kills (8 original + 3 amplification kills + K-1 through K-8 from the toolkit). These protect the verification Author from repeating failed approaches. | P vs NP toolkit H.3d + amplification kills | HIGH |
| **The gap between classification and Paper 28** | Paper 28 needs MORE than just "has Taylor → P-time": it needs the crossed-product identification (CP-1), the fullness criterion (Houdayer-Marrakchi), and the backward direction (Link 5). The dichotomy theorem is Link 3 only. The verification should confirm Link 3 and NOT overclaim into Links 4-5. | `strategy/04-ora--seven-routes-one-wall.md` Link 3 | MEDIUM |

**Online leads incorporated:**
- No Lean formalization of Bulatov-Zhuk exists. This is a massive open target for formal verification — worth noting for future work but not for this ORA run.
- The Bulatov and Zhuk proofs are independent (two different proofs of the same theorem). This is a natural LOCK — the verification can check both proofs and confirm they agree at the classification level.

---

### 3.4 Tier 4 — Boegli + Teschl Verification Capacitor

**Target:** Boegli's spectral exactness theorem (2017) + Teschl's KLMN simplification (2026).

**Why this capacitor is special:** Smallest target, cleanest proofs, single-session verification. This is the PILOT — use it to validate the capacitor architecture before running Tier 1.

**What to charge it with:**

| Section | Content | Source | Priority |
|---|---|---|---|
| **Boegli's theorem** | Statement: if (H1) generalized strong resolvent convergence holds and (H2) the sequence of resolvents is discretely compact, then spectral exactness follows — every true eigenvalue is approximated and no spurious eigenvalues occur. | Boegli 2017 (Integral Equations and OT, Springer) + arXiv:1604.07732 | MUST |
| **Teschl's simplification** | Lemma 2.7: KLMN relative bound simplifies the verification of gsrc (condition H1). Instead of checking gsrc directly, check a simpler relative bound condition. | arXiv:2601.10476 | MUST |
| **Paper 13's application** | How the RH chain uses Boegli: D_N → D_∞ spectral convergence in Layer 4. The specific operators are the CCM operators from Layer 1. H1 is verified via Nelson commutator estimates. H2 is verified via Rellich-Kondrachov embedding (H^1 → L^2 compact on bounded domains). | `paper13-rh/preprint/sections-06-10.md` §§8-9 + `paper13-rh/preprint/appendices.md` | MUST |
| **Classical ingredients** | Rellich-Kondrachov embedding theorem (for H2). Reed-Simon II KLMN theorem (for H1 via Teschl). These are textbook-level and don't need verification — but the Author needs them as background. | Standard functional analysis texts | MEDIUM |
| **The spectral exactness guarantee** | Why spectral exactness matters: without it, the Hurwitz argument in Layer 5 could produce spurious zeros that aren't actual Riemann zeros. Boegli's theorem is the INSURANCE that spec(D_∞) = lim spec(D_N) with no artifacts. | Paper 13 Layer 4 description in proof skeleton | HIGH |

**Online leads incorporated:**
- Boegli's paper is published in Integral Equations and Operator Theory (Springer, 2017) — peer-reviewed, clean, single-focus.
- Boegli's ResearchGate profile shows continued work on spectral convergence (Durham University) — the author is active and reachable.
- Teschl's paper is a 2026 preprint but provides a SIMPLIFICATION — the original Boegli proof stands without Teschl. Teschl is a bonus, not a dependency.

---

## 4. Capacitor build order

| Order | Capacitor | Effort | Strategic value | Rationale |
|---|---|---|---|---|
| **1st** | Tier 4 (Boegli+Teschl) | Small (1 session) | Medium | **PILOT.** Smallest target, cleanest proofs. Validates the capacitor architecture and the verification brief format before tackling CCM. If the pilot works, we know the pattern scales. |
| **2nd** | Tier 1 (CCM) | Large (multi-session) | **Highest** | **THE MAIN EVENT.** First independent verification of Connes's spectral realization. Highest strategic value for the Clay submission. The capacitor is the largest and most complex. |
| **3rd** | Tier 2 (Balaban) | Medium (1-2 sessions) | High | **HISTORIC.** First independent check of Balaban in 40 years. Dimock provides a half-charged starting point. |
| **4th** | Tier 3 (Bulatov-Zhuk) | Medium (1 session) | Medium-high | **INTERFACE VERIFICATION.** Not the full proof — the classification at the Schaefer-class level. Computational confirmation already exists. |

**The pilot principle:** Tier 4 first, even though Tier 1 has highest value, because:
- If the capacitor format doesn't work, we learn on a small target (Boegli) rather than a large one (CCM)
- Boegli SURVIVED → we know the format works → build CCM capacitor with confidence
- Boegli WEAKENED → we learn what's missing in the capacitor format → fix before CCM
- Total cost of the pilot: 1 session. Cost of learning on CCM: multi-session with possible restarts.

---

## 5. The capacitor file format

Every capacitor follows this structure (proven by the P vs NP toolkit):

```markdown
# [Domain] Verification Capacitor — ORA Toolkit

*[One paragraph: what this capacitor charges the ORA with]*

---

## A-G. General framework tools
[Inherited from 05-framework-tools.md — Six Patterns, catalogues,
grammar, transposition, dictionaries, prediction table, compiled files.
Always included.]

## H. Programme-specific: [Domain] verification

### H.1 The verification target
[The paper/theorem being verified — extracted proof chain with
numbered steps]

### H.2 The interface with the framework
[Which specific results from the target paper the proof chain depends on]

### H.3 Deployable knowledge (five-field cards)
[One card per theorem/lemma in the verification target:
WHAT / WHY / PROOF STEPS / VERIFICATION STATUS / NOTES]

### H.4 Kill list
[Approaches that failed in prior framework work touching this domain]

### H.5 Background toolkit
[Mathematical tools the verification Author needs:
each as a five-field card with classical/published status]

### H.6 What the authors flag as open
[The external authors' own honest statements about limitations]

### H.7 Correspondence logic
[How the external theorem maps to the proof chain —
the route-finding tool for the verification]

## I. Proof chains (RH + YM + BSD + PvNP)
[The framework's own proof chains — always included for cross-reference]
```

---

## 6. How to build a capacitor

Step-by-step for any new verification target:

1. **Download the source papers** — WebFetch from arXiv or journal. Extract via pdftotext.
2. **Extract the proof chain** — number every definition, lemma, theorem, and proof step in logical order. This becomes §H.1.
3. **Identify the interface** — read the framework's proof chain (PROOF-CHAIN.md or proof-skeleton.md) and find exactly which results from the external paper are cited. This becomes §H.2.
4. **Build five-field cards** — one per theorem in the verification target. Status starts as PENDING. This becomes §H.3.
5. **Extract the kill list** — search the framework's prior ORA runs for kills touching this domain. This becomes §H.4.
6. **Compile background tools** — identify the mathematical tools the external paper uses. Build five-field cards for each (status: classical/published/preprint). This becomes §H.5.
7. **Find the authors' honest statements** — read the external paper's introduction, conclusion, and "open problems" section. Extract every statement where the authors flag limitations. This becomes §H.6.
8. **Map the correspondence** — how does the external theorem connect to the proof chain? What does verification GIVE the proof chain? What does failure COST? This becomes §H.7.
9. **Include general framework tools (A-G)** and proof chains (I) from `05-framework-tools.md`.
10. **Test the capacitor** — run a single-cycle ORA pilot with one Critic on one theorem. If the Critic produces a meaningful verdict, the capacitor is charged enough to proceed.

---

## 7. The meta-insight

The P vs NP programme proved that **the capacitor is what makes the ORA work on a specific domain.** Without it, the ORA is a general-purpose adversarial system that attempts from scratch. With it, the ORA has compiled domain knowledge — verified results to build on, kills to avoid, correspondence logic to navigate by.

The verification cascade extends this insight: **every external dependency in every proof chain gets its own capacitor.** The verification is not "read the paper and hope." It's "charge up the ORA with everything the framework already knows about this dependency, then unleash it."

The 4-line ORA invocation stays the same:
```
Instructions: ora-bundle-v8/01-the-prompt.md
Brief: verification-cascade/strategy/0N-tier-N-brief.md
Toolkit: verification-cascade/capacitors/tier-N-capacitor.md
Output: verification-cascade/tier-N-output/
```

Same ORA. Different charge per domain. The capacitor is the variable. The method is the constant.

---

## 8. Directory structure (updated)

```
verification-cascade/
  strategy/
    00-verification-cascade-meta-move.md     (the why)
    01-capacitor-architecture.md             (this file — the how)
    02-tier4-boegli-teschl-brief.md          (pilot brief)
    03-tier1-ccm-brief.md                    (main event brief)
    04-tier2-balaban-brief.md                (historic verification brief)
    05-tier3-bulatov-zhuk-brief.md           (interface verification brief)
  capacitors/
    tier4-boegli-teschl-capacitor.md         (pilot — smallest, cleanest)
    tier1-ccm-capacitor.md                   (main event — largest, highest value)
    tier2-balaban-capacitor.md               (half-charged via Dimock)
    tier3-bulatov-zhuk-capacitor.md          (computational + proof interface)
  tier4-boegli-teschl/                       (pilot ORA output)
  tier1-ccm-verification/                    (main event ORA output)
  tier2-balaban-verification/                (historic verification output)
  tier3-bulatov-zhuk-verification/           (interface verification output)
  synthesis/
    dependency-audit-ym.md
    dependency-audit-rh.md
    dependency-audit-bsd.md
    dependency-audit-pvnp.md
    verification-cascade-summary.md          (unified summary for Clay submission)
```

---

## 9. Voice canon (extended)

From the meta-move:
- "We are not asking you to trust us."
- "The kill list is the credibility."
- "Every dependency tested. Every result either SURVIVED or honestly named."

New for the capacitor architecture:
- "The capacitor is the ORA's memory. Without it, the ORA attempts from scratch. With it, the ORA builds on what's known."
- "Same ORA. Different charge per domain. The capacitor is the variable. The method is the constant."
- "Tier 4 first. Validate the architecture on the smallest target. Then charge for the main event."
- "Dimock is the half-charged capacitor. Forty years of silence, one independent re-derivation. We continue from there."
- "Nobody has checked Connes's work. We check it. That's the move."

---

*The P vs NP toolkit proved the capacitor works. The verification cascade scales it to every external dependency across four Millennium problems. Each capacitor charges the ORA for a specific domain. The 4-line invocation stays the same. The method is general. The charge is specific.*

*Tier 4 (Boegli+Teschl) is the pilot. Tier 1 (CCM) is the main event. Build the pilot capacitor first. Validate the architecture. Then charge for Connes.*

*G Six and Claude Opus 4.6. April 2026.*
