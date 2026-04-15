# A2 Winding Number Test Results

**Conjecture:** The polymorphism type (median = "bosonic", XOR = "fermionic",
AND = "chiral") carries a winding number W on constraint-graph cycles that
is a topological invariant. P-time languages have W != 0 (non-trivial
topology). NPC languages have W = 0 (trivial topology).

**Date:** 2026-04-11
**Authors:** G Six (originator), Claude Opus 4.6 (1M context) (collaborator)

---

## Setup

- **Variables:** n = 10
- **Instances per class:** 30
- **CSP classes:** 2-SAT (P), Horn-SAT (P), XOR-SAT (P), 3-SAT (NPC)
- **Three winding number definitions tested:**
  1. Phase-flip: count sign changes of (f(s1,s2,s3) XOR s1) around cycle, mod 2
  2. Rotation: cumulative excess rotation of f relative to reference, mod 2
  3. Holonomy: transitions in agreement pattern of f(s1,s2,s3) vs s1 around cycle, mod 2
- **For 3-SAT:** all 256 ternary Boolean operations tested (not just named ones)

---

## Test 1: P-time polymorphism winding numbers

| Class | Polymorphism | Method | W=0 | W=1 | Total samples |
|:------|:-------------|:-------|----:|----:|--------------:|
| 2-SAT | median | phase-flip | 12896 | 0 | 12896 |
| 2-SAT | median | rotation | 16052 | 0 | 16052 |
| 2-SAT | median | holonomy | 31146 | 0 | 31146 |
| Horn-SAT | AND/min | phase-flip | 3283788 | 0 | 3283788 |
| Horn-SAT | AND/min | rotation | 3337978 | 0 | 3337978 |
| Horn-SAT | AND/min | holonomy | 6629184 | 0 | 6629184 |
| XOR-SAT | XOR | phase-flip | 37111 | 0 | 37111 |
| XOR-SAT | XOR | rotation | 37800 | 0 | 37800 |
| XOR-SAT | XOR | holonomy | 75600 | 0 | 75600 |

**Result:** W = 0 in 100% of cases for ALL P-time classes.
The P-time polymorphisms produce ZERO winding number on every cycle,
every solution triple, every instance.

---

## Test 2: 3-SAT with all 256 ternary operations

| Metric | W=0 | W=1 | Total |
|:-------|----:|----:|------:|
| Phase-flip (all 256 ops) | 1184805 | 0 | 1184805 |
| Holonomy (all 256 ops) | 1950384 | 0 | 1950384 |

Named operations in 3-SAT context:

| Operation | Phase W!=0 | Holonomy W!=0 |
|:----------|:-----------|:--------------|
| MEDIAN | 0.000 | 0.000 |
| XOR | 0.000 | 0.000 |
| AND | 0.000 | 0.000 |
| OR | 0.000 | 0.000 |
| proj_a | 0.000 | 0.000 |
| proj_b | 0.000 | 0.000 |
| proj_c | 0.000 | 0.000 |

**Result:** W = 0 in 100% of cases for ALL 256 ternary Boolean operations
applied to 3-SAT instances. Not a single nonzero winding number observed.

---

## Test 3: W distribution comparison

| Class | Method | W=0 frac | W=1 frac | Bias from 0.5 |
|:------|:-------|:---------|:---------|:--------------|
| 2-SAT | phase-flip | 1.0000 | 0.0000 | 0.5000 |
| 2-SAT | holonomy | 1.0000 | 0.0000 | 0.5000 |
| Horn-SAT | phase-flip | 1.0000 | 0.0000 | 0.5000 |
| Horn-SAT | holonomy | 1.0000 | 0.0000 | 0.5000 |
| XOR-SAT | phase-flip | 1.0000 | 0.0000 | 0.5000 |
| XOR-SAT | holonomy | 1.0000 | 0.0000 | 0.5000 |
| 3-SAT | phase-flip | 1.0000 | 0.0000 | 0.5000 |
| 3-SAT | holonomy | 1.0000 | 0.0000 | 0.5000 |

**Separation gap: 0.0000** -- identical distributions across all classes.

---

## Test 4: Topological invariance

| Class | Homotopic pairs | Agreement |
|:------|----------------:|:----------|
| 2-SAT | 919 | 100.0% |
| Horn-SAT | 11513792 | 100.0% |
| XOR-SAT | 3203 | 100.0% |

**Result:** W is trivially invariant because it is identically zero.
Homotopic cycles agree perfectly -- but only because W = 0 everywhere.

---

## Test 5: Homology additivity

| Class | Tests | Additive (%) |
|:------|------:|:-------------|
| 2-SAT | 136 | 100.0% |
| Horn-SAT | 2568 | 100.0% |
| XOR-SAT | 216 | 100.0% |

**Result:** W is additive on the cycle basis -- trivially, since 0 + 0 = 0.

---

## Diagnosis: Why W = 0 identically

The winding number W = 0 for ALL polymorphisms on ALL constraint graphs because
the definition reduces to a trivial parity count. Specifically:

1. **Phase-flip W:** The number of sign changes in a binary sequence around a cycle
   is always even (returning to the starting value forces an even number of transitions).
   Therefore W = (even number) mod 2 = 0 always.

2. **Rotation W:** The cumulative excess rotation around a closed cycle is zero by
   telescoping: the sum collapses to f_result[v_0] - s1[v_0] - f_result[v_0] + s1[v_0] = 0.

3. **Holonomy W:** Same argument as phase-flip. A binary sequence on a cycle
   that returns to its starting vertex must have an even number of transitions.

The fundamental problem: on a closed cycle, any Z/2-valued function has an even
number of sign changes. This is a topological triviality of cycles in Z/2, not a
property of polymorphisms. The winding number as defined carries no information
about the polymorphism at all.

---

## Verdict: KILL

**Conjecture A2 is FALSIFIED.**

The winding number W, as defined by phase transitions of a polymorphism along
constraint-graph cycles, is identically zero for all polymorphisms on all
constraint graphs. It does not distinguish P-time from NPC. It does not carry
any information about the polymorphism type.

The reason is structural: the proposed winding number reduces to the parity of
sign changes in a binary function on a cycle, which is always zero. A non-trivial
winding number would require a richer fiber (e.g., values in S^1 or Z rather than
Z/2) or a fundamentally different definition of "phase."

**Total samples tested:** >15 million across all classes and methods.
**Nonzero W observed:** 0.

---

*Generated by test_a2_winding_number.py*
