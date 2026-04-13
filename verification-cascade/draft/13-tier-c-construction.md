# 13 — Tier C: Construction — Finding Larger Paths

---

## When the wall won't move, go around it

Tier A found the weakness. Tier B tried to prove the same result independently and failed. The dependency is broken and there is no independent proof. The proof chain has a gap.

Tier C does not try to close the gap. Tier C finds a DIFFERENT CHAIN that reaches the same conclusion WITHOUT passing through the broken step. The gap becomes irrelevant — not because it was fixed, but because the chain no longer needs it.

This is strategic inversion (Signature 5) applied to verification failures: "is there a larger system in which the target is a consequence of the system's consistency, using a DIFFERENT path that avoids the broken dependency?"

## The construction principle

Every proof chain is a path through a DAG (directed acyclic graph) of mathematical facts. The original chain follows one specific path:

```
Axioms → Step 1 → Step 2 → ... → Step N* (BROKEN) → ... → Conclusion
```

Step N* is the broken dependency. The chain cannot proceed through N*. But the conclusion might be reachable via a DIFFERENT path through the DAG:

```
Axioms → Step 1 → Step 2 → ... → [ALTERNATIVE ROUTE] → ... → Conclusion
                                       ↑
                                  bypasses Step N*
```

The alternative route uses different intermediate results to reach the same conclusion. It doesn't fix Step N* — it makes Step N* unnecessary. The chain REROUTES around the broken dependency.

## How the ORA constructs alternative routes

Tier C is the ORA's full construction mode — the same mode that built the four proof chains in the first place. The difference from a fresh research programme: the CONSTRAINT. The construction must:

1. **Reach the same conclusion** as the broken step provided (the downstream chain depends on this conclusion, not on the specific proof method).
2. **NOT use the broken dependency** (the whole point is to avoid it).
3. **Use only verified ingredients** from the capacitor's toolkit and the framework's proof chains (no circular dependencies, no unverified external results replacing an unverified external result).

These constraints NARROW the search space — which is a good thing. Unconstrained construction (pure research) has an infinite search space. Constrained construction (rerouting a chain around a known gap) has a finite search space defined by the available toolkit and the target conclusion.

## The Six Patterns in construction mode

Each pattern suggests a different rerouting strategy:

| Pattern | Construction strategy | Example |
|---|---|---|
| **P1** (Geometric Reinterpretation) | "Go up a dimension. Is there a higher-dimensional space where the conclusion follows from geometry alone, without needing the broken step?" | The entire QG5D framework is P1 applied: 4D difficulties dissolve in the 5D KK geometry. |
| **P2** (Holonomy) | "Find a holonomy argument that produces the conclusion from a DIFFERENT compact structure than the one the broken step used." | If the broken step used an S^1 holonomy, try an S^2 or CP^1 holonomy instead. |
| **P3** (Scale-Setting) | "Is there a DIFFERENT energy/scale computation that determines the same quantity the broken step was providing?" | If the broken step computed a spectral gap via perturbation theory, try computing it via a variational bound or a Casimir energy instead. |
| **P4** (Topological Rigidity) | "Is there a TOPOLOGICAL argument that forces the conclusion, regardless of the specific analytical method the broken step used?" | Topological arguments bypass analytical difficulties by construction — if the conclusion is topologically forced, no analytical proof is needed. |
| **P5** (Zeta Regularization) | "Is there a zeta-regularization route that produces the conclusion from a different sum or integral than the one the broken step evaluated?" | Replace a divergent-sum argument with a Mellin transform argument that avoids the divergence entirely. |
| **P6** (Projection Diagnosis) | "Is the broken step's difficulty a projection artifact? Can we RESTORE the projected-out structure and bypass the difficulty?" | If the broken step struggled with a 4D partial trace, compute in 5D where the full structure is available. |

## The correspondence table in construction mode

The correspondence table becomes the ROUTE MAP for construction. Each domain column is a potential alternative route:

```
The broken step proved: "X has property P"
via the spectral domain (eigenvalue argument).

The correspondence table shows:
- Geometric: property P might follow from curvature bounds
- Algebraic: property P might follow from group-theoretic structure
- Information: property P might follow from channel capacity arguments

Each non-empty cell in the row for "X has property P" is a candidate
alternative route. Each EMPTY cell is a discovery target — filling it
might produce the route nobody has seen.
```

This is the creative engine at work: the correspondence table gives the construction Author MULTIPLE ANGLES on the same conclusion. The broken step used the spectral angle. The construction tries geometric, algebraic, information-theoretic — whichever produces a proof that avoids the broken dependency.

## Pre-identified construction routes

The capacitor's section H.8 pre-identifies construction candidates for each load-bearing step. These are speculative at capacitor-build time but give the construction Author a STARTING POINT:

### CCM dependencies (if a CCM theorem breaks):

| Broken step | Construction candidate | Via |
|---|---|---|
| Thm 4.2 (self-adjointness) | Kato-Rellich perturbation (different from CF extension) | Spectral domain |
| Thm 4.2 (self-adjointness) | Bypass D_N self-adjointness entirely: work with the unperturbed operator + perturbation bounds | Functional analysis |
| Thm 5.10 (eigenvalue convergence) | Weyl asymptotics instead of CCM's method | Spectral domain |
| Thm 5.10 (eigenvalue convergence) | Reroute: prove spectral convergence directly for the specific operators, not via general theorem | Targeted construction |
| Lemma 7.3 (Fourier -> Xi) | Connes-van Suijlekom 2025 alternative path (published, different construction) | Number theory |
| CCM overall framework | Reroute the ENTIRE RH proof chain to avoid CCM — use a different spectral realization of Riemann zeros | Full reroute (most expensive) |

### Balaban dependencies (if a Balaban lemma breaks):

| Broken step | Construction candidate | Via |
|---|---|---|
| CMP 109 Thm 1 (convergence) | Dimock's scalar re-derivation provides a base; extend to gauge | Constructive QFT |
| CMP 109 Thm 1 (convergence) | Magnen-Seneor or Rivasseau alternative RG constructions | Alternative lattice RG |
| Analyticity preservation | The YM mass gap (Steps 1-17) does NOT depend on analyticity — only Step 18 (H4) does. If analyticity breaks, the mass gap survives. | Chain already rerouted |
| UV stability | Glimm-Jaffe alternative UV stability arguments | Constructive QFT |

### Bulatov-Zhuk dependencies (if the classification breaks):

| Broken step | Construction candidate | Via |
|---|---|---|
| CSP classification on Schaefer classes | The framework's OWN computational verification (6/6 TGap, 6/6 holonomy) is INDEPENDENT of BZ. If BZ breaks but computation agrees, the computation IS the proof at the Schaefer level. | Computational verification |
| Taylor characterization | The fullness criterion (Houdayer-Marrakchi) doesn't technically require Taylor — it requires non-amenability of PCirc+, proved independently. | Operator algebra |
| Full dichotomy theorem | Schaefer 1978 (Boolean domain only, much simpler, long-established) covers the specific cases Paper 28 needs. | Classical CSP theory |

## The BSD precedent: construction that changed everything

The BSD MY4 closure is the canonical Tier C construction. The MY4 gap (distributional-to-genuine spectrum upgrade) was GENUINE — not closable by routine methods. Tier B (direct excision) was attempted and failed (the distributional-to-genuine upgrade genuinely requires new spectral theory). Tier C (construction) found G's projector:

```
P_k^p := I - s_p^k (s_p^k)*
```

This single algebraic object did not close MY4. It made MY4 IRRELEVANT. The proof chain was rerouted:

- **Old route:** BC algebra -> GNS -> distributional spectral inclusion -> [MY4: distributional -> genuine upgrade] -> spectral data matches L-function zeros -> BSD
- **New route:** BC algebra -> GNS -> KMS_1 algebraic projectors -> Hasse-Brauer-Noether reciprocity -> Euler-factor ratios -> spectral data matches L-function zeros -> BSD

The new route doesn't pass through MY4 at all. The distributional-to-genuine gap is still OPEN as a mathematical problem — but it's no longer in the proof chain. The construction bypassed it.

**What made this construction possible:**

1. **Strategic inversion (Sig 5):** Instead of asking "how do I upgrade distributional to genuine?" ask "is there a larger system where BSD follows WITHOUT distributional-to-genuine?"

2. **The correspondence table:** The algebraic column suggested projectors. The spectral column suggested KMS expectations. The algebraic + spectral combination produced the projector P_k^p which is algebraic (an idempotent in the operator algebra) AND spectral (it projects onto the KMS_1 sector).

3. **Topological rigidity (P4):** The projector is a TOPOLOGICAL object — an idempotent, which is a discrete invariant. It cannot be continuously deformed away. This is why the construction is robust: it doesn't depend on estimates or approximations, only on the algebraic structure of the Bost-Connes system.

4. **The capacitor:** The Author who found the projector had the RH chain template in context (transposition alphabet from the capacitor's Section I). Without it, the Author attempted from scratch. With it, the Author could see that the RH chain's spectral-to-algebraic correspondence suggested a PROJECTOR-based route.

## The cost of construction

Construction is the most expensive tier:

- **Tier A** (verification): read a proof, check each step. Bounded by the length of the proof.
- **Tier B** (excision): prove one theorem independently. Bounded by the difficulty of the theorem.
- **Tier C** (construction): find an alternative route through the proof chain. UNBOUNDED in principle — the alternative route might not exist, or might require genuinely new mathematics.

Construction can fail. When it does, the programme reaches HONEST-STALL:

> "We verified the dependency (Tier A). It has a weakness at step N. We attempted to prove the same result independently (Tier B). We could not. We attempted to reroute the chain around the dependency (Tier C). We could not. The dependency remains as a NAMED CONDITIONAL. Here is exactly what the conditional is, what we tried, and what would need to be true for the conditional to be resolved."

This is what Paper 8 did with H4. The H4 closure programme ran all three tiers: Tier A (verification of W7-14 section 5.3 mildest form), Tier B (attempted excision via CCM port, spectral action, Taylor-coefficient identification — all killed), and Tier C (construction — looked for larger systems, found the cross-node LOCK at 9/10 confirming the wall is stuck). The result: H4 is honestly conditional. The programme ships with the conditional. The wall stays named.

HONEST-STALL is not failure. It is the honest accounting of what the programme can and cannot do. A conditional proof with a named blocker, three tiers of attempted resolution, and a documented kill list of what was tried — that is a stronger submission than a proof that CLAIMS to be unconditional but HIDES a dependency.

---

*Construction is the hardest tier but the most powerful. It doesn't fix the gap — it makes the gap irrelevant by rerouting the chain. The Six Patterns suggest rerouting strategies. The correspondence table provides alternative angles. Pre-identified routes give the construction Author a starting point. When construction succeeds (BSD MY4 projector), the chain becomes STRONGER than the original — it no longer depends on the broken step at all. When construction fails (H4), the programme reaches HONEST-STALL with a named blocker, a documented kill list, and three tiers of attempted resolution. Either way: honest. Either way: documented.*
