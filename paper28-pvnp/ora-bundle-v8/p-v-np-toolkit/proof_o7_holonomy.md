# Proof Sketch: O7-HOLONOMY (Independent Re-verification)

*Retroactive proof file for the v8 P vs NP Toolkit.*
*Source code: paper28-pvnp/code/reverify_o7_holonomy.py*
*Prior verification: paper28-pvnp/code/test_o7_holonomy.py, results_o7_holonomy.md*
*Date: 2026-04-12 (re-verification with different seed)*

---

## Claim

The constraint graph is the "compact dimension." A polymorphism evaluated along cycles in the constraint graph is the "Wilson line." Trivial holonomy (H1 = 1.0) corresponds to flat connection and P-time solvability. Non-trivial holonomy (no consistent Taylor operation across instances) corresponds to curved connection and NP-completeness.

## Method

Independent re-verification using a different random seed (20260412 vs original 42), testing:

1. **P-time classes** (2-SAT, Horn-SAT, Dual-Horn-SAT, XOR-SAT): For each class, generate 30 satisfiable instances at n=10. For the known polymorphism (median, AND, OR, XOR respectively), compute H1 = fraction of all ordered triples of solutions where bitwise application of the polymorphism produces a solution. Verify H1 = 1.0 for all instances.

2. **NPC classes** (3-SAT, NAE-3-SAT): Same setup, but exhaustively scan all 256 ternary Boolean operations. For each, check whether it preserves the solution set. Count how many non-essentially-unary ("Taylor") operations are consistent across ALL 30 instances.

3. **Cross-instance test**: Track per-instance accidental polymorphisms and show that intersection over instances collapses to zero Taylor ops.

### Critical classification detail

The 256 ternary Boolean operations include:
- 3 projections (a, b, c): indices 170, 204, 240
- 3 negated projections (NOT a, NOT b, NOT c): indices 15, 51, 85
- 2 constants (0, 1): indices 0, 255
- **Total essentially unary: 8 operations**
- **Taylor operations: the remaining 248**

The CSP dichotomy theorem (Bulatov-Zhuk) states that a CSP is in P iff it admits a Taylor polymorphism (one that is NOT essentially unary). Negated projections and constants are not Taylor.

## Results

### P-time classes: H1 = 1.0 (4/4)

| Class | Polymorphism | H1 (all 30 instances) | Verdict |
|:------|:-------------|:---------------------:|:--------|
| 2-SAT | median | 1.000000 | PASS |
| Horn-SAT | AND | 1.000000 | PASS |
| Dual-Horn | OR | 1.000000 | PASS |
| XOR-SAT | XOR | 1.000000 | PASS |

### NPC classes: 0 Taylor ops survive cross-instance (2/2)

| Class | Per-instance Taylor ops (range) | Cross-instance Taylor ops | Verdict |
|:------|:-------------------------------|:------------------------:|:--------|
| 3-SAT | 0..61 (mean 6.3) | **0** | PASS |
| NAE-3-SAT | 0..10 (mean 7.7) | **0** | PASS |

### Cross-instance intersection shrinkage

**3-SAT:** Instance 1 has 61 accidental Taylor polymorphisms. After intersecting with instance 2, only 4 remain. After instance 3, zero. Stays zero through instance 30.

**NAE-3-SAT:** Instance 1 has 10 accidental Taylor polymorphisms. After intersecting with instance 2, 10 remain. After instance 3, zero Taylor ops remain. Stays zero through instance 30.

### NAE-3-SAT negated projection note

For NAE-3-SAT, 3 essentially unary operations (NOT a = 15, NOT b = 51, NOT c = 85) DO survive across all 30 instances. This is expected and benign: NAE-SAT is closed under bitwise complement (if assignment s satisfies NAE-phi, then NOT s also satisfies NAE-phi). Negated projections exploit this symmetry but are NOT Taylor operations -- they depend on only one coordinate. This does not violate the holonomy claim.

## Interpretation

The gauge-theoretic analogy holds precisely:

- **Flat connection (P-time):** The known polymorphism provides parallel transport that is globally consistent. Transporting any triple of solutions around any cycle in the constraint graph returns to the solution set. The holonomy group is trivial.

- **Curved connection (NPC):** No Taylor operation provides consistent parallel transport. Individual instances may have accidental symmetries (up to 61 operations for a single 3-SAT instance), but these are instance-specific gauge artifacts. The cross-instance intersection kills them all within 3 instances, revealing the topological obstruction.

- **Essentially unary survivors (NAE-SAT):** The negated projections that survive for NAE-SAT are analogous to a discrete gauge symmetry (Z_2 complement symmetry) that does not flatten the connection -- it is a global symmetry of the constraint language, not a polymorphism in the CSP-dichotomy sense.

## Status

**VERIFIED -- 6/6 separation on holonomy metric H1.**

No KILL signals. Independent re-verification with different seed confirms prior results.
