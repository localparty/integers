# P vs NP — Official Problem Statement

**Author of official statement:** Stephen Cook, "The P versus NP Problem"
**Source:** https://www.claymath.org/wp-content/uploads/2022/06/pvsnp.pdf
**Local copy:** `../00-clay-rules/pvnp-cook.pdf`
**Text extract:** `../00-clay-rules/pvnp-cook.txt`
**Retrieved:** 2026-04-14

---

## §1 Statement of the Problem (verbatim)

> The P versus NP problem is to determine whether every language accepted by some nondeterministic algorithm in polynomial time is also accepted by some (deterministic) algorithm in polynomial time. To define the problem precisely it is necessary to give a formal model of a computer. The standard computer model in computability theory is the Turing machine, introduced by Alan Turing in 1936.

Cook defines P over a finite alphabet Σ, |Σ| ≥ 2:

> P = {L | L = L(M) for some Turing machine M that runs in polynomial time}

with T_M(n) ≤ n^k + k for some fixed k. NP is defined via polynomial-time checking relations:

> A language L over Σ is in NP iff there is k ∈ N and a polynomial-time checking relation R such that for all w ∈ Σ*, w ∈ L ⟺ ∃y(|y| ≤ |w|^k and R(w, y)).

> **Problem Statement. Does P = NP?**

> It is easy to see that the answer is independent of the size of the alphabet Σ (we assume |Σ| ≥ 2)…. For |Σ| = 1 the problem is still open, although it is possible that P = NP in this case but not in the general case.

## Clay §5(b) special clause

> In the case of the P versus NP Problem and the Navier-Stokes Problem, a resolution in either direction will be evaluated by the standard evaluation procedure set forth in Section 7.

Either P = NP (constructive algorithm or non-constructive proof) OR P ≠ NP (lower bound / separation) wins.

## Cook's later sections (context, not requirements)

Cook's §§2-5 cover history, NP-completeness theory, proposed lines of attack (oracles, relativization, natural proofs, algebrization, geometric complexity theory), and explicit hard problems. These are scholarly context; they do NOT redefine the question.

## Known obstructions (Cook §4-§5)

Any proof must bypass:
- **Relativization** (Baker-Gill-Solovay) — technique must distinguish oracle worlds.
- **Natural proofs** (Razborov-Rudich) — a "natural" lower-bound technique cannot work unless strong one-way functions fail.
- **Algebrization** (Aaronson-Wigderson) — generalization of relativization.

These are not requirements, but a successful proof must be non-relativizing, non-natural, non-algebrizing (in the technical senses).
