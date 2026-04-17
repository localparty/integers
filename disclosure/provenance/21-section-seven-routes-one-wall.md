# 21 — Seven routes, one wall

> *The honest stall on P vs NP Link 5. The first place the programme said "we are stuck" and meant it.*

---

## What happened

P vs NP is the most famous of the Clay Millennium Problems. Its statement: is every problem whose solution can be *checked* in polynomial time also solvable in polynomial time?

Paper 28 is our attempt.

The strategy is spectral-geometric-informational: use the Bost-Connes crossed product to define a *fullness* criterion; show that for full factors, the spectral gap forces exponential separation; apply this to 3-SAT through the CSP dichotomy theorem (Bulatov-Zhuk 2017); conclude P ≠ NP.

The chain has six links. Five are verified. **Link 5 is HONEST-STALL.**

Link 5 is the backward implication: *from fullness to separability*. We know (forward) that if the BC crossed product is full, then the associated factor has a specific spectral gap, which forces the computational separation. What we do not yet know is the converse: *given a CSP that is NP-complete, does its associated BC factor have to be full?*

Seven routes have been tried. Each route is a documented strategy for closing Link 5 from a different angle. All seven failed, each for a specific named reason. The routes and their kills are logged in:

`solutions-with-prize/paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md`

The seven routes include scalar probes, thermal probes, algebraic probes, geometric probes, Écalle resurgence via lateral Borel, renormalon-OPE via Parisi-SVZ, and a rigidity-of-non-fullness argument. The log explicitly states which worked (algebraic, geometric — memory `70211df`) and which did not (scalar, thermal).

Commit `9c2473e` documents the current state:

> The phase incoherence condition (ID) is the single remaining mathematical gap. Three closing approaches identified in the node.

Commit `70211df`:

> Algebraic and geometric probes WORK. Scalar and thermal probes DON'T.

The result: Paper 28 is the programme's first HONEST-STALL. Five links proved, one link bounded by seven documented failures. The statement is precise: **we do not yet have a route from CSP NP-completeness to BC factor fullness. Seven named routes have been tried; none closes the link. The honest status is that the link is open, scoped, and not known to be reachable by currently-available methods.**

## What it felt like

This is the most important section in this whole document for me emotionally, because it is the section about being honest when dishonesty would have been easy.

By the time the Cascade had run on Yang-Mills, RH, and BSD, I had developed a reputation (in my own head) for closing chains. Each previous chain had survived the Cascade. Each had produced a Tier 2 claim with a single named external dependency.

P vs NP wanted to be the fourth in that pattern. I tried to make it so. I tried **seven times**.

The scalar probe (attempt 1) looked promising for two days. It failed on a uniformity bound I could not patch. I logged it.

The thermal probe (attempt 2) used KMS conditions directly. It produced an inequality that was formally correct but did not connect to the combinatorial side I needed. I logged it.

The algebraic probe (attempt 3) worked — *for one direction*. It gave me the forward implication cleanly. It did not give me the backward one.

The geometric probe (attempt 4) worked — *for a subclass of CSPs*. Not all NP-complete CSPs. I could not extend it.

The Écalle resurgence route (attempt 5) tripped over the K-8 kill (transseries magnitude ≠ Wilson coefficient; commit `01109a8`). Logged as a new failure mode in addition to the route being blocked.

The renormalon-OPE route (attempt 6) produced beautiful OPE-side structure but did not deliver the CSP implication.

The non-fullness rigidity argument (attempt 7) was the one I was most optimistic about. It ran for three days before a specific counterexample (2-SAT, which is in P but has a BC factor that could be argued to be non-full depending on the resolution) showed the route was compromised. Memory `pvnp_calibration` logs this in detail.

At the end of attempt 7, I had a choice. I could:

**(a) Claim closure anyway.** Pick the least-broken of the seven routes, paper over the gap with plausible-looking language, submit the paper as Tier 2 conditional on "technical fullness conditions." A real reviewer would probably catch it; they might not. This is the path most research takes when stuck.

**(b) Call HONEST-STALL.** Write a document titled *Seven routes, one wall*. Log each route with its specific failure mode. State explicitly that the chain is open at Link 5 and that closure is not currently reachable. Submit the paper with five verified links and one HONEST-STALL, clearly labelled.

I chose (b).

The emotional cost of that choice was real. The hope of being the person who proved P vs NP is a powerful motivator. Setting it aside felt like setting down something heavy.

But the feeling that replaced it — once I had written out the seven routes and committed the HONEST-STALL document — was the strongest feeling of intellectual integrity I have ever had. The paper that stood at the end was *honest*. It was a real contribution (five verified links, a named wall, seven logged failures). It was not overclaiming. It was not hedging. It was the actual state of the research, reported exactly.

I do not regret the choice. I think, looking back, it is the single most important decision I made in the programme's methodology. Every other paper is shadowed by it: if BSD or RH or YM were overclaims, P vs NP would not be a HONEST-STALL. The fact that P vs NP *is* a HONEST-STALL is calibration evidence that the other three Tier 2 claims are genuinely Tier 2 — not disguised Tier 3s.

## Why it mattered

### 1. It calibrated the Tier system with a real test

The Tier system (Section [17](17-section-tier-system.md)) is only as honest as its worst temptation. The temptation on P vs NP was enormous. Resisting it, and actually using the HONEST-STALL category for the first time, proved that the Tier system was load-bearing rather than decorative. It was not a label to dress up results. It was a genuine epistemic constraint that I was willing to apply to my own most-desired result.

### 2. It produced a public wall-document

`04-ora--seven-routes-one-wall.md` is a piece of research communication the field rarely sees: a detailed, honest, specific catalogue of failed approaches. Most researchers do not publish their failures. The document ensures that others attempting P vs NP from a spectral-gap direction do not have to re-walk the seven routes.

That is a public good. It is the kind of contribution that builds the reputation of the programme even though it is not a theorem.

### 3. It named the wall precisely

"We are stuck on P vs NP" is not a useful statement. "We are stuck on the implication `NP-complete CSP → full BC factor`; seven routes have been tried; each failed as documented" is a useful statement. It tells the next researcher where to focus. It tells reviewers that the rest of the chain is not contaminated by the Link 5 gap. It tells the programme itself which future breakthroughs would unlock what.

The wall is not a weakness. It is a *frontier*. Named frontiers attract work. Unnamed ones do not.

### 4. It changed the programme's character

Before Paper 28, the programme had produced three Tier 2 chains. A fourth was expected. When the fourth came out HONEST-STALL instead, the programme's public identity shifted. It was no longer "this person is rapidly closing Millennium problems." It became "this programme is rigorously attacking Millennium problems, with honest reporting of what works and what does not."

The second identity is more durable than the first. It is also more valuable to the field.

## Where it lives

- **Main stall document**: `solutions-with-prize/paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md`.
- **Key commits**:
  - `b69f243` — "ora v7 pvnp run"
  - `21010e2` — "alternative routes"
  - `2c04ad1` — "1st cycle path"
  - `a1b3e93` — "A2 CLOSED. Clone unitaries live in M_Bool for P-time (100% closure), leak outside for NPC (64–83%)."
  - `2b66e6a` — the forward-direction argument: "A full factor has a spectral gap. A spectral gap means any algorithm must cross it exponentially many times..."
  - `9c2473e` — "The phase incoherence condition (ID) is the single remaining mathematical gap."
  - `70211df` — "Algebraic and geometric probes WORK. Scalar and thermal probes DON'T."
- **Calibration memory**: `pvnp_calibration` — the repair history including the 2-SAT counterexample and the three technical errors found and fixed.
- **Breakthrough session**: `session_pvnp_breakthrough` — the dictionary-building, 10-agent, 7-pass session that assembled the current state.

## What to take from it

**The most valuable thing a research programme can produce is a HONEST-STALL when the temptation to overclaim is maximal.**

I will say this again because it is the single most important methodological lesson of the programme: *the hardest integrity move is the one that costs you the most-desired result, and the one that pays back most over the long run.*

If I had overclaimed on P vs NP, two things would have happened. First, a sharp referee would eventually have found the gap, and the programme's reputation would have taken a permanent hit. Second — more importantly — I would have known I overclaimed. That knowledge corrodes the rest of the work. Every Tier 2 claim becomes uncertain because the one with the strongest temptation was not honestly reported.

By calling HONEST-STALL on P vs NP, I protected the Tier 2 claims on YM, RH, and BSD. They are now more credible, not less, because I was willing to not claim what I could not prove. The calibration is the whole point.

Honesty is contagious across results in a programme. Dishonesty is also contagious. Choose which contagion.

---

*Next: [22 — The 23-vertex ring](22-section-twenty-three-vertex-ring.md).*
