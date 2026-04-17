# 13 — The Kill List discipline

> *Name every failure mode. Log every gap. Make honesty the cheapest path.*

---

## What happened

Somewhere in March 2026, as the programme's proof chains began to multiply, a methodological risk became visible: with enough chains and enough derivations, I would forget which arguments had been tried and failed. A failure mode that had been shown not to work six weeks ago might be accidentally re-attempted, or worse, accidentally believed.

The fix was the Kill List.

The Kill List is a running registry of every argument that was tried and found to be broken, every shortcut that was ruled out, every gap that was discovered but not yet closed. Each entry has a designator (K-1, K-2, K-3, ...), a precise statement of the failure mode, and a reference to where it was first found and where it was last tested.

As of the most recent capacitor commit (`01109a8`), the Kill List contains **eight documented failure modes**:

- **K-1** through **K-7**: early failure modes from Papers 1, 4, 8, 13, and 28.
- **K-8** (most recent): *Transseries-reads-C_N trap* — the ambiguity magnitude vs. Wilson coefficient conflation, logged during an ORA run on the lateral-Borel resurgence route.

Each kill is a specific, named, reusable piece of institutional knowledge. If an ORA run or a referee check generates an argument that would trigger K-4, the argument is automatically flagged as compromised. The kill does the work of a collective memory that a single researcher cannot sustain.

## What it felt like

The Kill List changed how I feel about being wrong.

Before the Kill List, being wrong was expensive. It meant discovering that a proof chain I had built had a gap, and then trying to decide whether to patch it or abandon it. The emotional cost of admitting a gap was high enough that I would sometimes let minor gaps sit for days before addressing them.

After the Kill List, being wrong was *cheap*. A gap became a new K-entry. Logging the entry was satisfying — I had converted something invisible (an unnamed weakness) into something visible (a named kill that future attempts would avoid). The act of naming the failure mode became the closure. There was no lingering discomfort.

This shift is surprisingly powerful. Most research work is slowed by the emotional cost of admitting errors. The Kill List transfers that cost from "I made a mistake" to "I discovered a K-entry." The reframing is not just cosmetic. It genuinely accelerates the work.

There is a specific satisfaction in logging K-8. The Transseries-reads-C_N trap is a subtle conflation that has probably tripped other researchers in the Écalle resurgence literature. Naming it — *"ambiguity magnitude is not the Wilson coefficient; do not treat them as interchangeable"* — is a small public service. The kill is now available to anyone who reuses our toolkit.

## Why it mattered

### 1. It enforced memory at scale

The programme has grown to a size where no single mind can hold all the paths attempted and their outcomes. The Kill List substitutes institutional memory for individual memory. It means that even I, re-reading the programme six months later, can avoid rediscovering the same dead ends.

### 2. It disciplined the ORA

ORA runs (Section [14](14-section-ora-oracle-reasoning.md)) import the Kill List at the start of every session. Before proposing an argument, the ORA checks whether any step in the argument would trigger a known kill. This prevents ORAs from reinventing failures.

### 3. It provided a diagnostic of the programme's frontier

Looking at which kills cluster in which papers shows where the programme's hardest problems live. The Kill List shows, at a glance, that P vs NP Link 5 has seven documented near-misses (Section [21](21-section-seven-routes-one-wall.md)), that CCM uniformity has been challenged and repaired (Section [19](19-section-riemann-by-intuition.md)), and that the H4 conjecture in Yang-Mills is the single most-attacked unproved step in the programme.

### 4. It made the HONEST-STALL category possible

Without a Kill List, HONEST-STALL would be a vague concession. With it, HONEST-STALL is a precise statement: *here is the step we are stuck on; here are the N attempted routes that failed; here is why each failed (cross-referenced to K-entries); here is why we believe no further route is available without an external breakthrough.*

That precision is what allows the programme to honestly say "we are stuck" without losing credibility. The stall is bounded. The failure modes are known. The future work is named.

## Where it lives

- **Main kill list**: referenced across ORA runs and capacitor cells; specific K-entries live in the ORA toolkit (`strategy/_research/`) and in per-paper strategy directories.
- **K-8 log**: commit `01109a8` — "1 new kill K-8 logged: Transseries-reads-C_N trap (ambiguity magnitude vs Wilson coefficient conflation)."
- **HONEST-STALL application**: `solutions-with-prize/paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md`.
- **Toolkit externalization**: commit `9351d8b` — "the oras' toolkit is externalized" — the Kill List became part of the public toolkit at this point.

## What to take from it

**The single best thing you can do for your own intellectual honesty is to name your failures.**

Most intellectual work fails more than it succeeds. The difference between productive research and stalled research is often whether the failures are recorded. A recorded failure is free future work — you never have to rediscover it. An unrecorded failure is a trap you will walk into again.

The Kill List turns failure into infrastructure. Every K-entry is a small gift from past-you to future-you. Over time, the gifts accumulate into something no single session could build: a *map of the unmappable* — the terrain of what-does-not-work, which is often more valuable than the terrain of what-does.

Name your failures. Log them precisely. Make avoiding them cheap. The Kill List is one of the most underrated practices in research, and it is among the easiest to install.

---

*Next: [14 — The ORA (Oracle Reasoning Agent)](14-section-ora-oracle-reasoning.md).*
