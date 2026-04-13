# 29 — The Self-Improving Architecture

---

## Five layers of self-improvement

The verification cascade is not a static system. It is a LEARNING SYSTEM with five layers of self-improvement, each operating on a different timescale:

### Layer 1: The self-healing ORA (within a run)

The ORA patches its own prompt during live runs. When a spawned agent catches a reproducible failure mode that the current prompt doesn't handle, the runner writes a changelog entry (I-v6-N), re-audits against anti-predictions A-1 through A-4, applies the patch, validates it inline, and continues.

**Timescale:** Within a single ORA run. Minutes to hours.

**What improves:** The prompt itself — new disciplines, new checks, new failure-mode defenses.

**Empirical evidence:** I-v6-1 (inference-from-source check) was born during the H4 closure run's Wave 1.5. The R.D.1 Critic caught an inference error the existing I-7 discipline didn't cover. The runner patched Step 5.5 Way 1 in place. The revision Agent validated the patch inline. The patch has been active in every subsequent run.

I-v6-2 (self-healing as first-class feature) was born from reflecting on HOW I-v6-1 was produced — it was triggered by an ad-hoc user directive, not by the prompt itself. The patch baked the self-healing capability into the prompt as section 14.10, making it reproducible without user directives.

The self-healing loop is RECURSIVE: I-v6-1 created I-v6-2, which formalized the mechanism that created I-v6-1. The bundle bootstraps its own improvement capability.

### Layer 2: The dynamic capacitor (across waves within a run)

The capacitor grows through the self-adjust/trim/amplify cycle after each wave. New five-field cards are added. Status fields are updated (PENDING -> VERIFIED, VERIFIED -> WEAKENED). Kill list entries accumulate. Correspondence table cells are filled.

**Timescale:** Wave-to-wave within a run. Hours.

**What improves:** The domain knowledge — what's verified, what's killed, what pathways exist, what escalation routes have been tried.

**Empirical evidence:** The BSD MY4 run's capacitor grew when G's projector was discovered mid-run. The P vs NP capacitor was CORRECTED when retroactive verification found Q5-RIEMANN needed downgrading (noisy measurement), Q6-OUTDIM was only partially verified (P-time side incomplete), and O8-PARTITION was a statistical fluctuation (Lee-Yang spacing not reproducible). The corrections STRENGTHENED the capacitor by making it honest.

### Layer 3: The capacitor across runs (across ORA invocations)

After each ORA run, the updated capacitor is MERGED with new findings. The next run starts with a more charged capacitor. The version number increments. The MERGE LOG documents what changed.

**Timescale:** Run-to-run. Days.

**What improves:** The accumulated knowledge across the programme's entire history. A capacitor at v4 has the knowledge from four runs, not just one.

**Empirical evidence:** The P vs NP toolkit evolved from v1 (10 five-field cards from the brainstorm session) through v2 (amplification results from 6 transposition tests) to v3 (retroactive verification corrections) to v4 (current — fully honest status on all entries). Each version was more accurate than the last because it incorporated findings from a run that tested the previous version's claims.

### Layer 4: Cross-tier amplification (across verification tiers)

When a technique or finding succeeds in one tier, it amplifies to all other tiers. Boegli verification methods amplify to CCM verification. An excision technique used on CCM amplifies as a candidate for Balaban. A kill found in Bulatov-Zhuk amplifies as a warning to any tier using similar algebraic arguments.

**Timescale:** Tier-to-tier. Weeks.

**What improves:** The METHOD — not just the knowledge, but the APPROACH to verification and excision.

**Empirical evidence:** Not yet empirically tested (the verification cascade hasn't run yet). The P vs NP amplification results (6 transposition tests from Papers 1, 3, 5, 7, 10, 19) demonstrate the PATTERN: transposing a tool from one paper to another produces new results (1 PASS, 1 FAIL, 3 KILLS, 1 confirmed dual gap). The same pattern is expected to work across verification tiers.

### Layer 5: The generator improvement (across capacitor builds)

Each capacitor build teaches the generator how to build better capacitors. The first capacitor (Tier 4 pilot) may be rough — some correspondence table entries may be generic, some Six Patterns analyses may be superficial. The second capacitor (Tier 1 CCM) incorporates lessons from the pilot: which steps of the generator process produced the most useful output, which steps wasted effort, what format changes make the capacitor more usable.

**Timescale:** Build-to-build. Weeks.

**What improves:** The GENERATOR itself — the 10-step process, the correspondence table format, the pattern analysis depth, the operations table scope.

**Empirical evidence:** The capacitor format evolved through four programmes (YM v1 -> RH v2 -> BSD v3 -> PvNP v4). Each evolution was a generator improvement. The generator prompt (Section 22) encodes the v4 format — but v5 will come from the first builds. The generator, like the ORA, heals itself.

## The compound effect

The five layers compound:

```
Run 1:
  ORA heals prompt (Layer 1)
  Capacitor grows (Layer 2)
  Merged back to capacitor (Layer 3)

Run 2:
  Starts with better prompt (from Layer 1)
  Starts with better capacitor (from Layer 3)
  ORA heals AGAIN (Layer 1, new failure modes)
  Capacitor grows AGAIN (Layer 2, new findings)
  Merged back (Layer 3)
  Amplifies to other tiers (Layer 4)

Run N:
  Starts with N-1 rounds of prompt healing
  Starts with N-1 rounds of capacitor growth
  Starts with N-1 rounds of cross-tier amplification
  Starts with N-1 rounds of generator improvement
```

Each layer improves independently. The improvements compound across layers. A run that benefits from all five layers simultaneously is qualitatively different from a run using the initial system. The 10th run of the verification cascade will have a prompt with 10 rounds of healing, a capacitor with 10 rounds of growth, and a generator with 10 rounds of refinement.

This compounding is not speculative. The ORA's history demonstrates it: v3 (original, 15 signatures) -> v6 (Layer L mining, 19 signatures, anti-overfit discipline) -> v7 (P vs NP toolkit, I-v6-3/4/5 spawn-checklist convergence) -> v8 (toolkit externalized, autonomous operation, effort levels baked in, self-healing first-class). Each version incorporated lessons from the previous version's runs. The verification cascade formalizes this improvement cycle and makes it SYSTEMATIC rather than ad-hoc.

## The ACE connection (revisited)

Microsoft's ACE framework (arXiv:2510.04618, ICLR 2026) provides external validation of this architecture:

> *"ACE optimizes contexts both offline (system prompts) and online (agent memory), consistently outperforming strong baselines: +10.6% on agents and +8.6% on finance, while significantly reducing adaptation latency and rollout cost. ACE can adapt effectively without labeled supervision and instead by leveraging natural execution feedback."*

The verification cascade's five layers map to ACE's concepts:

| ACE concept | Cascade equivalent | Layer |
|---|---|---|
| Online context optimization | Dynamic capacitor growth | Layer 2 |
| Offline context optimization | Prompt healing between runs | Layer 1 + 3 |
| Natural execution feedback | SURVIVED/WEAKENED/BROKEN verdicts | All layers |
| No labeled supervision needed | Kill list + honest downgrades | Layers 2-3 |
| Incremental updates | Self-adjust/trim/amplify cycle | Layer 2 |
| Prevents collapse | Anti-overfit discipline + kill list | All layers |

The key insight from ACE: **self-improving contexts outperform static contexts precisely because they incorporate execution feedback.** The verification cascade's five layers are five ways of incorporating execution feedback — prompt-level, knowledge-level, cross-run, cross-tier, and generator-level. Each layer increases the system's ability to learn from its own operation.

## What the self-improving architecture means for the Millennium strategy

The verification cascade will run 6-10 sessions across 4 tiers. By the end:

- The ORA prompt will have accumulated 6-10 rounds of self-healing patches, each addressing a failure mode discovered during actual verification
- The capacitors will have accumulated 6-10 rounds of growth, each adding verified results, kills, and filled correspondence entries
- The generator will have been refined 4 times (one per tier), each time producing better capacitors
- Cross-tier amplification will have transferred successful methods across all 4 tiers

The system that runs Tier 3 (Bulatov-Zhuk) will be qualitatively BETTER than the system that ran Tier 4 (Boegli pilot) — not because of a redesign, but because of 5 layers of accumulated improvement. This is the compound interest of the self-improving architecture.

---

*Five layers of self-improvement. The ORA heals its prompt (Layer 1). The capacitor grows through waves (Layer 2). The capacitor persists across runs (Layer 3). Methods amplify across tiers (Layer 4). The generator improves through builds (Layer 5). Each layer improves independently. The improvements compound. The 10th run is qualitatively better than the 1st — not by redesign but by accumulated learning. The system improves itself. The kill list compounds. The correspondences fill. The prompt heals. The method sharpens.*
