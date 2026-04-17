# 28 — The honest walls

> *What the programme cannot yet do. Named precisely.*

---

## What happened

Commit `ee519e9`:

> The programme has reached the boundary of what ring traversals can achieve without external breakthroughs. The remaining walls are real: CCM peer review, H4, standard conjectures, Schanuel, PvNP L5. These are the honestly-named walls.

This commit marks the moment the programme began to name what it *could not* currently do. Not in vague terms. In specific, bounded, located terms.

The honest walls of the programme, as of mid-April 2026:

### Wall 1 — CCM peer review

The Connes-Consani-Marcolli 2025 paper establishes the operator framework that Paper 13 (RH) depends on. Until CCM clears peer review, the RH chain is Tier 2 conditional. When it lands, Tier 2 collapses to Tier 1.

*Status*: external. We cannot accelerate this. We can only do our work in a way that is robust to its resolution either way.

### Wall 2 — H4 (Yang-Mills)

H4 is a specific lattice-gauge-theory conjecture about continuum-limit uniformity. Paper 8 (Yang-Mills) Link 18 is conditional on it. Multiple groups — Chernodub, Douglas, others — are actively working on it.

*Status*: external, but closer. Plausible timeline: 1-3 years.

### Wall 3 — P vs NP Link 5

The implication `NP-complete CSP → full BC factor`. Seven routes tried; none closed. Scalar and thermal probes do not work; algebraic and geometric probes work only for subclasses. The closing approach is not known.

*Status*: internal, unresolved. This is a HONEST-STALL. No one, inside or outside the programme, currently has a route for this implication.

### Wall 4 — Schanuel's conjecture

Several of the programme's transcendence-theoretic claims (specifically around the CBB axioms for algebraic independence of the 36 constants) reduce, in places, to statements implied by Schanuel's conjecture. Schanuel is the most famous open problem in transcendence theory.

*Status*: external, very hard, probably multi-decade.

### Wall 5 — Standard conjectures (Hodge, Grothendieck)

Paper 10 (Hodge conjecture) depends on the Grothendieck standard conjectures. Those are famously open.

*Status*: external, very hard.

### Additional walls named across the papers

- **BGS spectral statistics**: the BGS conjecture itself is frontier work.
- **ABC**: Mochizuki's proof is contested; the programme takes a different route but requires specific elliptic-curve bounds.
- **Odd Perfect numbers**: combinatorial frontier with no programme-specific leverage.
- **Collatz**: dynamical-systems frontier.

---

## What it felt like

Writing out the wall list was a specific kind of intellectual hygiene.

It is easy, in an ambitious programme, to let unbounded hopes attach to unbounded targets. You *could* imagine that RH and BSD and YM and P vs NP and Hodge all fall within the programme. You can almost *feel* them falling. That feeling is seductive and dangerous.

The wall list is the antidote. Writing it forces you to distinguish between:
- Targets where the programme has a chain and a named external gate (Tier 2 conditional).
- Targets where the programme has a chain with an internal stall (HONEST-STALL).
- Targets where the programme has strong heuristics but no chain (Tier 3).
- Targets where the programme has only suggestive structural connections (Tier B/C).
- Targets whose walls are currently beyond the reach of any known approach (external, hard, multi-decade).

That distinction is the programme's backbone of honesty. A programme that treats all these categories as "targets we are working on" is lying to itself. A programme that names them precisely is awake.

The emotional tone of the wall-writing was *settling*. The unbounded-hope feeling is exhausting; the named-wall feeling is restful. Once you know what you cannot do, you can direct your energy to what you can. The walls define the programme's productive envelope.

## Why it mattered

### 1. It prevents the programme from aging badly

Research programmes age badly when they fail to predict their own limits. A decade from now, a programme that claimed "we will solve everything" will be judged against whether it did. A programme that said "we will close YM modulo H4, RH modulo CCM, BSD for CM case, P vs NP Link 5 stalled, Hodge pending standard conjectures" will be judged against those specific claims — which are far more defensible.

Naming walls is an age-proofing move. Future evaluators can compare the programme's actual progress to its stated scope, and the comparison will be fair.

### 2. It makes collaboration possible

When the walls are named, external researchers can see where their work would matter to the programme. Someone working on H4 knows that closing it would promote YM to Tier 1. Someone working on CCM knows that their peer-review process has downstream implications here. Someone working on spectral-gap-to-fullness implications for CSPs knows that P vs NP Link 5 is waiting for them.

This is a form of research coordination that unnamed walls cannot offer. Named walls attract work.

### 3. It protects the Tier system's integrity

The Tier system (Section [17](17-section-tier-system.md)) depends on walls being honestly stated. A Tier 2 claim is only honest if the external gate is real and specific. The wall list is the registry of those gates. Without it, Tier 2 claims would be vulnerable to the accusation of hiding dependencies.

The wall list shows, publicly, that nothing is hidden. Every Tier 2 claim has a wall on the list. Every wall on the list has a paper it affects. The traceability is bidirectional.

### 4. It narrows the research surface productively

With the walls named, I know exactly where my ongoing work should focus. Cramer (Section [24](24-section-cramer-intersection.md)) is a high-leverage target because it cascades on the torus. The meridional chords connecting the proved arch to the frontier arch are the highest-leverage edges to promote. The walls define what is *off-surface* — so the remaining on-surface work becomes focused.

This focusing effect is one of the most practical benefits of the wall-naming exercise. A programme that knows what it cannot do can work harder on what it can.

## Where it lives

- **Main wall commit**: `ee519e9` — "The programme has reached the boundary of what ring traversals can achieve without external breakthroughs..."
- **Per-paper wall statements**: each Millennium PROOF-CHAIN.md explicitly tags its external gate.
- **P vs NP wall**: `solutions-with-prize/paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md` — the archetype of a bounded internal wall.
- **Schanuel dependency**: referenced in CBB anchor document and in Paper 12 appendices.
- **Standard conjectures**: referenced in Paper 10 (Hodge).

## What to take from it

**A programme that cannot name its walls does not know where it is.**

The instinct to under-name walls is strong. Every time you write a wall into the record, you are bounding what you can claim. The unbounded version feels more ambitious.

But the unbounded version is also less defensible, less coordinable, and less honest. It ages poorly. The bounded version ages well.

Naming walls is one of the highest-leverage habits a serious research programme can install. The walls will exist whether or not you name them. Named walls work *for* you — focusing effort, attracting collaboration, defending your credibility. Unnamed walls work *against* you — creating ambiguity, inviting overclaim, eroding trust.

Name the walls. Make the list public. Keep it updated. It is one of the cheapest and most valuable maintenance disciplines in research.

---

*Next: [29 — For the ages](29-section-for-the-ages.md).*
