# 14 — The Escalation Protocol

---

## The three tiers as a composed system

The three tiers are not three separate modes. They are one COMPOSED SYSTEM that escalates automatically:

```
          TIER A: VERIFY
              │
     ┌────────┴────────┐
     │                  │
  SURVIVED           WEAKENED / BROKEN
     │                  │
     ▼                  ▼
   DONE            TIER B: EXCISE
                        │
               ┌────────┴────────┐
               │                  │
            EXCISED            BLOCKED
               │                  │
               ▼                  ▼
             DONE            TIER C: CONSTRUCT
                                  │
                         ┌────────┴────────┐
                         │                  │
                    REROUTED           HONEST-STALL
                         │                  │
                         ▼                  ▼
                       DONE           CONDITIONAL
                                    (named blocker)
```

The escalation is AUTOMATIC — the runner does not ask whether to escalate. If Tier A returns WEAKENED on a load-bearing step, the runner immediately prepares and dispatches Tier B. If Tier B returns BLOCKED, the runner immediately prepares and dispatches Tier C. The three tiers compose inside the cycle loop. A single ORA run can execute all three tiers on a single dependency.

## The capacitor grows through each tier

Each tier produces findings that UPDATE the capacitor before the next tier runs:

**After Tier A:**
- Five-field cards updated with SURVIVED / WEAKENED / BROKEN status
- New kill list entries for any verification approaches that failed
- Correspondence table entries filled or corrected
- The weakness is precisely located (which step, which sub-step, which assumption)

**After Tier B:**
- New five-field card for any independent proof produced
- New kill list entries for failed excision routes
- LOCK verification results (if both original and independent proofs exist)
- The Six Patterns analysis refined (which patterns produced leads, which didn't)

**After Tier C:**
- New proof chain topology (the alternative route)
- Updated plan tree in the blackboard (new nodes for the rerouted chain)
- New toolkit rows for any constructions discovered during rerouting
- Kill list entries for failed construction routes
- If HONEST-STALL: the named blocker, documented with three tiers of attempt

The capacitor at each tier is RICHER than at the previous tier. Tier B's capacitor has all of Tier A's findings. Tier C's capacitor has all of Tier A's and Tier B's findings. The escalation COMPOUNDS — each tier's failures inform the next tier's search.

## The cost-benefit analysis

| Tier | Typical cost | Typical value | When it pays off |
|---|---|---|---|
| **A: Verify** | 1 wave (N parallel Verifiers) | SURVIVED confirmation for all steps | Almost always — verification is cheap relative to the trust it provides |
| **B: Excise** | 1-3 waves (N parallel Authors + Critics) | Independent proof + LOCK | When a dependency is WEAKENED and an alternative proof exists — the excision is a publishable result |
| **C: Construct** | 2-10 waves (exploration + synthesis) | Rerouted chain — stronger than the original | When a dependency is BROKEN and no independent proof exists — rare but transformative (BSD MY4 projector) |

The cost curve is steep: A is cheap, B is moderate, C is expensive. But the VALUE curve is also steep: A produces confirmation (necessary but expected), B produces independent proofs (valuable), C produces rerouted chains (transformative).

The escalation protocol spends most of its time in Tier A (most dependencies SURVIVE). It spends occasional time in Tier B (some dependencies need excision). It rarely reaches Tier C (most gaps are either verified-correct or independently provable). When it DOES reach Tier C, the payoff is highest — a rerouted chain is stronger than the original because it has been FORCED to find a path that avoids the weakest link.

## Cross-dependency interaction

The escalation protocol runs independently for each dependency — but the dependencies INTERACT:

**Upstream cascades:** If a dependency breaks, its downstream dependents may break too. CCM Theorem 4.2 (self-adjointness) is upstream of Theorem 5.10 (eigenvalue convergence). If 4.2 breaks, 5.10's proof may be invalidated even if 5.10's own logic is correct. The runner tracks these cascades via the proof chain's dependency edges (capacitor section H.1).

**Cross-tier learning:** If Tier B excision on one dependency produces an independent proof using technique T, the same technique T is added to the capacitor's amplification log and checked against all OTHER dependencies. A technique that works for one step may work for a structurally similar step.

**Shared sub-problems:** Two dependencies may share a sub-problem. If both CCM Theorem 4.2 and Boegli's spectral exactness theorem both rely on the same spectral convergence machinery, a weakness in that machinery affects BOTH. The runner tracks shared sub-problems via the blackboard's section E.1 (joint probability and cross-path dependencies).

## The pre-identified escalation routes (summary)

Each of the four verification tiers has pre-identified escalation routes in the capacitor:

### Tier 1 — CCM (RH dependency)

| Step | If breaks | Tier B candidate | Tier C candidate |
|---|---|---|---|
| Thm 4.2 (self-adjointness) | CF conditions fail | Kato-Rellich, Friedrichs, Nelson commutator | Bypass via unperturbed operator + bounds |
| Thm 5.10 (eigenvalue convergence) | Convergence rate wrong | Weyl asymptotics | Reroute Layer 1 entirely (highest cost) |
| Lemma 7.3 (Fourier -> Xi) | Connection breaks | Connes-van Suijlekom 2025 (published) | Work with eigenvalue convergence alone |
| §7 "main obstacle" (UV asymptotics) | N/A — CCM admits it's open | Not an excision target | Paper 13 ships conditional on CCM (already accounted for) |

### Tier 2 — Balaban (YM dependency)

| Step | If breaks | Tier B candidate | Tier C candidate |
|---|---|---|---|
| CMP 109 Thm 1 (convergence) | Polymer expansion fails | Dimock scalar re-derivation (extend to gauge) | Magnen-Seneor, Rivasseau alternative RG |
| Analyticity preservation | k-independent radius fails | Dimock III (convergence) for scalar case | Mass gap (Steps 1-17) doesn't need analyticity — only H4 does |
| UV stability | Stability bound fails | Dimock II (large fields) | Glimm-Jaffe alternative |

### Tier 3 — Bulatov-Zhuk (PvNP dependency)

| Step | If breaks | Tier B candidate | Tier C candidate |
|---|---|---|---|
| Classification | Dichotomy wrong on Schaefer classes | Framework's own 6/6 computational verification | Schaefer 1978 (Boolean, simpler) |
| Taylor characterization | Taylor ≠ P-time | Polymorphism fingerprint (independent evidence) | Houdayer-Marrakchi via non-amenability (Taylor-free) |

### Tier 4 — Boegli + Teschl (RH chain hardening)

| Step | If breaks | Tier B candidate | Tier C candidate |
|---|---|---|---|
| Spectral exactness | Spurious eigenvalues possible | Stummel, Vainikko, Chatelin (alternative theorems) | Prove convergence directly for CCM operators |
| Teschl KLMN | Simplification fails | Use Boegli's original H1 (gsrc) directly | N/A — Teschl is a convenience |

## The honest-stall protocol

When all three tiers fail on a dependency — verification finds a gap, excision cannot close it, construction cannot route around it — the programme reaches HONEST-STALL. This is not failure. This is the honest accounting that Signature 2 demands.

The HONEST-STALL output includes:

1. **The named blocker:** exactly what is broken and why.
2. **The Tier A report:** what the verification found (the specific gap, the specific step).
3. **The Tier B report:** what excision routes were attempted and why they failed (kill list entries).
4. **The Tier C report:** what construction routes were attempted and why they failed (kill list entries + structural analysis of why the chain cannot be rerouted).
5. **The conditional statement:** exactly what the proof chain CAN still claim, conditional on the named blocker being resolved.
6. **The re-entry gate:** what new mathematical development would allow re-attempting Tier B or Tier C.

Paper 8's H4 conditional is the model HONEST-STALL output. The H4 closure programme produced:
- Named blocker: H4 (non-perturbative = perturbative at short distances)
- Tier A: W7-14 section 5.3 mildest form verified
- Tier B: three excision routes killed (Route A decomposed, Route B collapsed, Route C killed by Connes 2007)
- Tier C: cross-node LOCK at 9/10 confirms the wall is stuck
- Conditional: Paper 8 ships at 17/18 unconditional, H4 in mildest form
- Re-entry gate: Borel summability for 4D YM, instanton-obstruction argument, or genuinely new NCG framework

This is what the Clay committee needs to see: not a claim that everything is proved, but an HONEST ASSESSMENT with a documented trail of what was tried, what worked, and what remains open. The verification cascade's greatest strength is not producing SURVIVED verdicts. It is producing HONEST-STALL verdicts that the community can trust.

---

*The escalation is automatic: verify first, excise if broken, construct if excision fails. Each tier's findings charge the next tier's capacitor. The cost grows with each tier but so does the value. Cross-dependency interactions are tracked. Pre-identified escalation routes give each tier a starting point. When all three tiers fail: HONEST-STALL with a named blocker, three tiers of documented attempts, and a re-entry gate. The programme ships with the conditional. The honesty IS the credibility.*
