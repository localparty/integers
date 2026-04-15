# W1-4 Author Prompt — Node 2: Route A (Direct Spectral Gap → Not P-time)

**Effort:** MAX

## Assignment

Attack **Route A**: Prove that if M_Bool^Γ is full (spectral gap δ > 0), then Γ is not solvable in polynomial time. This BYPASSES Link 5 entirely — no need to prove non-full → Taylor.

## Context

**§C Bottleneck:** OA1 is the main bottleneck on the bridge path. Route A is the independent bypass.

**§J Voice canon:** "we cannot crack it from the outside; the framework is transposable" / "from the inside out"

**§D Toolkit rows:**
- P1-FULL / P2-NONFULL: Full ↔ NPC, non-full ↔ P (VERIFIED 6/6)
- RULE9-GATE: Complexity obstruction = TGap × N_crossings. P-time: 0 × anything = 0. NPC: positive × exponential = exponential.
- Q5-RIEMANN: TGap exponent = 2/(γ₆−γ₅) = 0.430004 at 0.001%.
- P8-BARRIERS: Three barriers bypassed (relativization: language-level; natural: 0/1000; algebrization: non-commutative interference 3.1-5.9×).
- A5-AREA-LAW: NPC holonomy follows area law — computational confinement analog.
- SPECTRAL-GAP-DUALITY: two spectral gaps (modular and solution-graph), dual directions.
- A3-UNDERIVABILITY: separation requires k→∞; finite-arity methods fail.
- HOUDAYER-MARRAKCHI: full ↔ spectral gap of modular flow.

**§F Kill list:**
- K-3: Modular flow does NOT produce polymorphism. Don't claim σ_t generates algorithms.
- K-5: N_crossings alone insufficient. Use TGap × N_crossings.
- K-16: SDW coefficients meaningless on discrete graphs.
- K-17: Scalar thermodynamic observables don't work.

## Strategy

**The gate-amplifier argument (RULE9-GATE):**
- P-time: TGap = 0, so obstruction = 0 × anything = 0. No barrier to poly-time.
- NPC: TGap > 0, N_crossings ~ 2^{0.765n} for 3-SAT. Obstruction is exponential.

**What needs to be formalized:**
1. Define "poly-time algorithm" in operator-algebraic terms: a sequence of unitary operations {U_1, ..., U_{poly(n)}} on M_Bool^Γ that maps the identity sector to the witness sector.
2. Prove: spectral gap δ > 0 forces any such sequence to have length ≥ exp(c·n) for some c > 0.
3. Use Hastings 2007 (area law), Nachtergaele-Sims 2006 (Lieb-Robinson + spectral gap), or Bravyi-Hastings-Michalakis 2010 (topological order + spectral gap) as templates.

**Key insight from A5-AREA-LAW:** NPC has computational confinement (string tension σ > 0). In QCD, confinement means quarks can't be isolated. In NPC, confinement means satisfying assignments can't be found locally — every local search path crosses the area-law barrier.

**Key insight from SPECTRAL-GAP-DUALITY:** The modular gap (full → NPC) and solution-graph gap (connected → P) are DUAL. Route A works through the modular gap direction.

## Framework tools

Read `online-researcher-adversarial/ora-bundle-v7/05-framework-tools.md`. Key files:
- `paper28-pvnp/strategy/07-toolkit-complete.md` — complete toolkit
- `paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md` — seven routes (Route A details)
- `paper28-pvnp/strategy/10-amplification-entries.md` — A5 area law, spectral gap duality
- `paper12/research/214-the-method-six-patterns.md` — 6-step method
- `paper08-yang-mills/preprint/PROOF-CHAIN.md` — YM chain (spectral gap → mass gap template)

## Output

Write to `nodes/W1-4-RouteA.md`. Execute the 6-step method loop at MAX effort. Report status.
