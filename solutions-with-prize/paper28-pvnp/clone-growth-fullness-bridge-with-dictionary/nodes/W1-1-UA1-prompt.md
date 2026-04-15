# W1-1 Author Prompt — Node 1.1: UA1 (Taylor → Exponential Clone Growth)

**Effort:** medium

## Assignment

Prove **Theorem UA1**: For a Boolean constraint language L (domain {0,1}), if L admits a Taylor polymorphism, then |Clone_k(L)| ≥ c · λ^k for constants c > 0, λ > 1.

## Context

**§C Bottleneck:** OA1 (polymorphism lift) is the main bottleneck, but UA1 is a prerequisite for OA2.

**§J Voice canon:** "trace discrepancies until they become theorems" / "be hella explicit" / "One theorem. Two established fields. One new connection."

**§D Toolkit rows you must cite by name:**
- BARTO-ETAL-2024: Taylor algebra has Taylor term at every prime arity > |A|. For Boolean (|A|=2), this gives Taylor terms at every prime k > 2.
- Q6-OUTDIM: dim_poly_k grows exponentially for P-time (verified 6/6). At k=5: 2-SAT has 4,295 to 107M non-projection ops. 3-SAT has 0.

**§F Kill list:** No kills directly relevant to UA1.

## Strategy from the brief (Strategy 08 §5 Phase 1)

By BARTO-ETAL-2024, L has a Taylor term at every prime arity > 2. Each Taylor term generates new terms through composition with the language's basic operations. The composition closure grows at least as fast as the number of distinct compositions.

**Approach**: bound the composition closure from below. At each prime arity p > 2, there exists at least one Taylor term t_p. The compositions t_p ∘ (t_q, ..., t_q) at arity p·q generate terms at composite arities. Count distinct compositions to get exponential lower bound.

**Computational evidence** (Q6-OUTDIM): 2-SAT dim_poly goes 1 → 21 → 3,746 → 83M from k=2 to k=5. That's super-exponential growth, consistent with UA1.

## Framework tools

Read `online-researcher-adversarial/ora-bundle-v7/05-framework-tools.md` for the full index. Key files for this node:
- `paper12/research/214-the-method-six-patterns.md` — the 6-step method loop you execute
- `paper12/27-anchor-document.md` — operational stance
- `paper28-pvnp/strategy/07-toolkit-complete.md` — the complete P vs NP toolkit (Always-include)

## Output

Write to `nodes/W1-1-UA1.md`. Execute the 6-step method loop. Report status (ADVANCED / BLOCKED / BLOCKED-DECOMPOSED / KILLED).
