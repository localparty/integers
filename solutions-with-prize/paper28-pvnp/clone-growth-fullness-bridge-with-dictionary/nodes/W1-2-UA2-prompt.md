# W1-2 Author Prompt — Node 1.2: UA2 (Non-Taylor → Linear Clone Growth)

**Effort:** medium

## Assignment

Prove **Theorem UA2**: For a Boolean constraint language L, if L does NOT admit a Taylor polymorphism, then |Clone_k(L)| ≤ 4k (linear growth).

## Context

**§C Bottleneck:** OA1 is the main bottleneck. UA2 is expected to be straightforward (direct from BZ).

**§J Voice canon:** "be hella explicit" / "honest partial proof over glossed completion"

**§D Toolkit rows:**
- BZ-DICHOTOMY: Non-Taylor ↔ NPC. Non-Taylor clone consists only of essentially unary operations.
- UA2-LINEAR-CLONE (status S, 80%): already structural. Your job is to close it to R (100%).

**§F Kill list:** No kills directly relevant.

## Strategy

By BZ, a non-Taylor Boolean clone contains only essentially unary operations. On {0,1}, an essentially unary k-ary operation f(x₁,...,x_k) depends on at most one coordinate. For each of k coordinates, choose one of {id, neg, const-0, const-1}. Plus the two constant functions. Total: 4k + 2. Growth is O(k).

**Your task**: write a rigorous proof. The argument is: (1) cite BZ for "non-Taylor ⟹ essentially unary clone", (2) enumerate essentially unary Boolean operations, (3) count: ≤ 4k + 2.

## Framework tools

Read `online-researcher-adversarial/ora-bundle-v7/05-framework-tools.md`. Key files:
- `paper12/research/214-the-method-six-patterns.md` — 6-step method
- `paper28-pvnp/strategy/07-toolkit-complete.md` — P vs NP toolkit

## Output

Write to `nodes/W1-2-UA2.md`. This should reach ADVANCED or CLOSED status.
