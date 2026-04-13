# 08 — What a Capacitor Is and Why It Matters

---

## The moment the capacitor was discovered

On April 11, 2026, the ORA ran its first verified cycle on the P vs NP programme. Author W1-3 was dispatched to attack node OA1 — the outerness question for the Boolean Bost-Connes factor. The Author was given a clear task, a correct kill list, a good REFRAME insight, and max effort. It searched the literature, found a real structural obstruction (the Kearnes-Szendrei-Tschantz theorem), and returned BLOCKED-DECOMPOSED. A correct verdict.

But the Author missed something. In a file called `07-toolkit-complete.md` — a file the Author never received — there were 10 verified computational results from a prior brainstorm session. One of them was PATB-DIAGONAL: "the Taylor condition is equivalent to fixing the diagonal of M_Bool^Gamma." This result directly addresses the outerness question the Author was working on. The Author spent 6 minutes searching the web for operator algebra results. With PATB-DIAGONAL in context, it would have started from a verified structural identification instead of a blank slate.

The same failure mode had appeared before. In the BSD MY4 run (April 10, 2026), Author M.1.1 attempted the dark-state bound from scratch because `paper13-rh/preprint/sections-06-10.md` was not in its spawn context. The answer — the entire BSD chain over K = Q(i) is structurally a transposition of the RH chain's CCM/ITPFI/Boegli/Hurwitz layers — was already written in a different alphabet. The Author didn't have the alphabet.

And it happened a third time. In the P vs NP run cycle 2, Author W2-1 on the Q_struct node received the spawn checklist (added after the first failure) but the runner classified the node as "P-vs-NP only" and missed that it was also a transposition + spectral-gap-style argument. The transposition mechanics file and the YM proof chain — both directly relevant — were not included.

Three consecutive failures. Same root cause: **the Author didn't have the compiled knowledge.**

The fix was not a better checklist. The fix was not a lookup table. The fix was: **always pass everything.** Let the Author self-select. The compiled knowledge — the toolkit, the verified results, the kill list, the correspondence logic — is always included. The Author knows its own node better than the runner.

That compiled knowledge, structured for an ORA agent to use, is the capacitor.

## What a capacitor contains

A capacitor is a markdown file that charges the ORA with domain-specific knowledge. It has a specific structure, evolved through four programmes:

**Layer 1 — File pointers (from YM v1):** Paths to the relevant papers, preprints, proof chains, research files. "Read these files." This is what every toolkit has always had. It is necessary but not sufficient — an Author with 50 file pointers and no guidance on which ones matter will read the wrong ones or read none.

**Layer 2 — Chain structure (from RH v2):** The proof chain decomposed into numbered steps with dependency edges. "Here is the logical structure." This tells the Author what connects to what — which steps are load-bearing, which steps are downstream, where the chain is vulnerable. The RH proof skeleton (6 layers with explicit dependency graph) was the first capacitor to include this.

**Layer 3 — Mid-run growth (from BSD v3):** The capacitor is not static. When the ORA discovers something during a run, the discovery is added to the capacitor for subsequent waves. G's projector P_k^p was discovered during the BSD MY4 run and immediately added to the toolkit. The next wave of Authors had the projector as a deployable result. The capacitor grew mid-run because the discovery was too valuable to defer.

**Layer 4 — Deployable cards with honest status (from PvNP v4):** Five-field cards (WHAT / WHY / DATA / USE / STATUS) for each verified result. Not just "this result exists" but "here is what it says, why it matters, what data supports it, how to cite it, and whether it's been re-verified." Plus honest corrections: when re-verification weakens a result (Q5-RIEMANN's fitted exponent didn't cleanly match at small n; Q6-OUTDIM's P-time side was only confirmed for 2-SAT), the card's status is DOWNGRADED and the correction is documented. The capacitor is honest about what it knows and what it doesn't.

These four layers compose into the capacitor's structure:

```
GENERAL FRAMEWORK TOOLS (Sections A-G)
  Six Patterns method (the inner-loop discipline)
  Theorem catalogues (canonical-name coordination)
  Predictive grammar (algebraic search prior)
  Transposition mechanics (cross-domain translation)
  Master dictionaries and anchors (operator dictionary)
  Master prediction table (empirical scoreboard)
  Compiled reference files (lower-priority)

PROGRAMME-SPECIFIC (Section H)
  H.1  Proof chain (numbered steps with status)
  H.2  Correspondence tables (spectral <-> geometric <-> algebraic <-> information)
  H.3  Six Patterns analysis (per load-bearing step)
  H.4  Grammar analysis (per formula/claim)
  H.5  Operations equivalence table
  H.6  Interface with framework proof chains
  H.7  Kill list (imported + domain-specific)
  H.8  Escalation routes (Tier B + Tier C per step)
  H.9  Authors' honest statements (what the external paper flags as open)
  H.10 Background toolkit (five-field cards for mathematical tools)
  H.11 Amplification log (cross-tier transfers — empty at v1)
  H.12 Corrections log (honest downgrades — empty at v1)

FRAMEWORK PROOF CHAINS (Section I)
  RH chain (6 layers)
  YM chain (18 steps)
  BSD chain (11 steps)
  PvNP chain (6 links)

MERGE LOG
  Date / Run / Cards added / Cards updated / Kills added / Escalations
```

## Why the capacitor changes everything

Without the capacitor, the ORA is a general-purpose adversarial system. It can read papers, dispatch agents, and produce verdicts. But it starts every task from scratch. Every Author must discover the relevant prior work by reading file pointers and hoping to find the right section. Every Critic must verify claims without knowing what's already been verified. Every Synthesis agent must find cross-lead patterns without knowing what patterns have been found before.

With the capacitor, the ORA is a DOMAIN EXPERT. The Author starts from 10 verified results instead of zero. The Critic knows which approaches have been killed and why. The Synthesis agent has the correspondence tables that reveal cross-domain patterns. The runner has pre-identified escalation routes for every weak point.

The difference is empirical, not theoretical:

- **BSD MY4 without capacitor**: Author attempted from scratch, missed existing answer written in different alphabet. Cost: 1 wasted agent cycle.
- **BSD MY4 with capacitor**: Route 3 closure found G's projector P_k^p — a single algebraic object that bypassed the wall. The projector was discovered because the Author had the RH chain template in context and could PORT instead of INVENT.

- **P vs NP OA1 without capacitor**: Author found the KST obstruction (real, valuable) but missed 10 verified results including PATB-DIAGONAL. Cost: 6 minutes of web searching for results that existed in a local file.
- **P vs NP subsequent waves with capacitor**: Authors cited PATB-DIAGONAL, Rule 9 v3, Q5-RIEMANN, and O7-HOLONOMY directly. No re-derivation. No web searching. Immediate access to the programme's compiled knowledge.

The capacitor is not an optimization. It is the difference between "smart agent on a new problem" and "expert continuing a research programme."

## The five-field card: the atom of deployable knowledge

The smallest unit of knowledge in the capacitor is the five-field card:

```
### [ENTRY NAME] — [one-line title]

| Field | Content |
|:------|:--------|
| **WHAT** | [What the result says — a precise statement] |
| **WHY**  | [Why it matters for the current programme — what it enables or blocks] |
| **DATA** | [The evidence — numerical results, computational verification, precision] |
| **USE**  | [How an Author should cite it — a sentence template with "By [ENTRY NAME], ..."] |
| **STATUS** | [VERIFIED / WEAKENED / CONFIRMED / PENDING / DOWNGRADED — honest current state] |
```

The card format was developed during the P vs NP programme. It is the format that makes knowledge DEPLOYABLE — an Author reading the card knows exactly what the result says, why it matters, what evidence supports it, how to cite it, and whether to trust it. Compare this to a file pointer: "read `paper28-pvnp/strategy/07-toolkit-complete.md`." The pointer says where to look. The card says what was found.

A capacitor for a CCM verification run would have cards like:

```
### CCM-THM-4.2 — Self-adjointness of D_N

| Field | Content |
|:------|:--------|
| **WHAT** | The operators D_N on E_N^+ are self-adjoint, obtained as rank-one
|          | perturbations of the prolate operator via Caratheodory-Fejer. |
| **WHY**  | Self-adjointness is the FLOOR of the RH proof — without it, the
|          | spectral approximation in Layer 1 has no foundation. |
| **DATA** | CCM 2025 Theorem 4.2, proved via CF extension theorem for Toeplitz
|          | matrices. Precursor in CCM 2024 (published, Annals Funct. Anal.). |
| **USE**  | "By CCM-THM-4.2, the operators D_N are self-adjoint on E_N^+
|          | via the Caratheodory-Fejer rank-one perturbation construction." |
| **STATUS** | **PENDING VERIFICATION** (the ORA has not yet tested this) |
```

After the verification run, the STATUS field updates:
- SURVIVED: the proof checks out, no gaps found
- WEAKENED: gaps found but repairable — with a note describing the gap
- BROKEN: fatal flaw — with a note describing the flaw and its impact

The card's status IS the verification result. The capacitor's collection of cards IS the verification audit.

## The capacitor vs the blackboard

Both the blackboard and the capacitor are persistent state. They serve different roles:

| | Blackboard | Capacitor |
|---|---|---|
| **Scope** | One run | Cross-run (persists between ORA invocations) |
| **Content** | Current programme state (live nodes, this run's kills, this run's metrics) | Compiled domain knowledge (verified results across ALL runs, correspondence tables, escalation routes) |
| **Created by** | The runner at bootstrap | The user or the ORA generator before invocation |
| **Updated by** | The runner during cycles | The runner during cycles AND the user between runs |
| **Purpose** | Operational state: "where are we NOW?" | Domain memory: "what do we KNOW?" |
| **Survives session end?** | Yes (archived in output directory) | Yes (in the capacitor directory) |
| **Survives programme close?** | Archived in lockdown snapshot | **GROWS** — the next run inherits the updated capacitor |

The blackboard is the run's WORKING memory. The capacitor is the programme's LONG-TERM memory. After an ORA run closes:

1. Read the run's closure-digest
2. Extract new five-field cards, new kills, updated statuses, new correspondences
3. Merge into the capacitor file
4. Increment the capacitor's version number
5. The next run starts with a more charged capacitor

This merge operation is the key. It turns the capacitor from a static input into a growing knowledge base. v1 is the generator's initial output. v2 is after the first verification run. v3 is after the second. Each version is more charged than the last — more cards, more kills, more correspondences, more honest corrections.

The blackboard dies with the run. The capacitor lives across runs. The programme's knowledge accumulates in the capacitor.

---

*The capacitor is the ORA's domain-specific memory. Without it, agents attempt from scratch. With it, agents have compiled knowledge — verified results to build on, kills to avoid, correspondence tables to navigate by, escalation routes to follow when stuck. Three consecutive failures taught the lesson: always pass everything. The five-field card is the atom. The dynamic capacitor is the molecule. The verification cascade is the organism.*
