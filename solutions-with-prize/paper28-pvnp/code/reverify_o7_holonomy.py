"""
reverify_o7_holonomy.py — Independent re-verification of O7-HOLONOMY entry
in the P vs NP transposition dictionary.

Claim: Polymorphism holonomy on constraint graphs distinguishes P from NPC.
  - P-time classes: known polymorphism gives H1 = 1.0 (trivial holonomy)
  - NPC classes: NO non-projection ternary op achieves H1 = 1.0 across
    all 30 random instances (non-trivial holonomy)

This script is written from scratch for independent verification.

Author: G Six, with Claude Opus 4.6. Date: 2026-04-12.
"""

import random
import itertools
import json
import sys
from collections import defaultdict

# =====================================================================
# CONFIG
# =====================================================================
N_VARS = 10
N_INSTANCES = 30
SEED = 2026_04_12  # Different seed from original test
random.seed(SEED)

# The 3 projections among 256 ternary Boolean ops:
# pi_1(a,b,c)=a (170), pi_2(a,b,c)=b (204), pi_3(a,b,c)=c (240)
PROJECTION_INDICES = {170, 204, 240}

# Negated projections: NOT a (15), NOT b (51), NOT c (85)
# These are "essentially unary" -- they depend on only one coordinate.
# In the CSP dichotomy theorem, what matters is whether a Taylor operation
# exists (an operation that is NOT essentially unary). Negated projections
# are essentially unary because they factor through a single coordinate
# followed by negation. They do NOT count as Taylor operations.
# NAE-SAT is closed under complement, so negated projections trivially preserve it.
NEGATED_PROJECTION_INDICES = {15, 51, 85}

# Constant operations: f=0 (index 0), f=1 (index 255)
CONSTANT_INDICES = {0, 255}

# All "essentially unary" operations: constants + projections + negated projections
# These are the 8 ternary Boolean ops that depend on at most 1 input variable.
# In the CSP dichotomy theorem, Taylor = NOT essentially unary.
ESSENTIALLY_UNARY = CONSTANT_INDICES | PROJECTION_INDICES | NEGATED_PROJECTION_INDICES
# = {0, 15, 51, 85, 170, 204, 240, 255}

# =====================================================================
# INSTANCE GENERATORS
# =====================================================================

def gen_2sat(n, m=None):
    """Random 2-SAT instance. ratio ~2.0"""
    if m is None:
        m = 2 * n
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 2)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def gen_horn(n, m=None):
    """Random Horn-SAT (at most 1 positive literal per clause), 3-literal."""
    if m is None:
        m = int(2.5 * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        # Horn: at most 1 positive literal
        n_pos = random.choice([0, 1])
        clause = []
        for i, v in enumerate(vs):
            if i < n_pos:
                clause.append(v)
            else:
                clause.append(-v)
        random.shuffle(clause)
        clauses.append(clause)
    return clauses

def gen_dual_horn(n, m=None):
    """Random Dual-Horn-SAT (at most 1 negative literal per clause), 3-literal."""
    if m is None:
        m = int(2.5 * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        # Dual-Horn: at most 1 negative literal
        n_neg = random.choice([0, 1])
        clause = []
        for i, v in enumerate(vs):
            if i < n_neg:
                clause.append(-v)
            else:
                clause.append(v)
        random.shuffle(clause)
        clauses.append(clause)
    return clauses

def gen_xor(n, m=None):
    """Random XOR-SAT (each clause is a XOR constraint), 3-literal."""
    if m is None:
        m = max(2, n // 2)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def gen_3sat(n, m=None):
    """Random 3-SAT. ratio ~4.0 (near threshold)."""
    if m is None:
        m = 4 * n
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def gen_nae3sat(n, m=None):
    """Random NAE-3-SAT. ratio ~2.5."""
    if m is None:
        m = int(2.5 * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

# =====================================================================
# SOLUTION ENUMERATION
# =====================================================================

def eval_clause_or(clause, assignment):
    """Standard OR-clause satisfaction."""
    for lit in clause:
        v = abs(lit)
        val = assignment[v-1]
        if (lit > 0 and val) or (lit < 0 and not val):
            return True
    return False

def eval_clause_xor(clause, assignment):
    """XOR-clause: the XOR of the literals' truth values must be True."""
    xor_val = False
    for lit in clause:
        v = abs(lit)
        val = assignment[v-1]
        lit_val = val if lit > 0 else (not val)
        xor_val ^= lit_val
    return xor_val

def eval_clause_nae(clause, assignment):
    """NAE-clause: not all literals have the same truth value."""
    vals = []
    for lit in clause:
        v = abs(lit)
        val = assignment[v-1]
        lit_val = val if lit > 0 else (not val)
        vals.append(lit_val)
    return not (all(vals) or not any(vals))

def enumerate_solutions(clauses, n, mode='or'):
    """Brute-force enumerate all solutions for n variables."""
    eval_fn = {'or': eval_clause_or, 'xor': eval_clause_xor, 'nae': eval_clause_nae}[mode]
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 == 1 for i in range(n))
        if all(eval_fn(c, assignment) for c in clauses):
            solutions.append(assignment)
    return solutions

# =====================================================================
# CONSTRAINT GRAPH & CYCLES
# =====================================================================

def build_constraint_graph(clauses, n):
    """Build undirected graph: variables are nodes, edge between vars sharing a clause."""
    edges = set()
    for clause in clauses:
        vars_in_clause = [abs(lit) for lit in clause]
        for i in range(len(vars_in_clause)):
            for j in range(i+1, len(vars_in_clause)):
                u, v = vars_in_clause[i], vars_in_clause[j]
                if u != v:
                    edges.add((min(u,v), max(u,v)))
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj, edges

def find_cycles(adj, n, max_length=5, max_cycles=50):
    """Find simple cycles of length 3, 4, 5 via DFS. Cap to avoid combinatorial explosion."""
    cycles_by_length = {3: [], 4: [], 5: []}
    nodes = sorted(adj.keys())

    # Length 3: triangles
    for u in nodes:
        for v in adj[u]:
            if v > u:
                for w in adj[v]:
                    if w > u and w in adj[u]:
                        cycles_by_length[3].append((u, v, w))
                        if len(cycles_by_length[3]) >= max_cycles:
                            break
                if len(cycles_by_length[3]) >= max_cycles:
                    break
        if len(cycles_by_length[3]) >= max_cycles:
            break

    # Length 4
    for u in nodes:
        for v in adj[u]:
            if v != u:
                for w in adj[v]:
                    if w != u and w != v:
                        for x in adj[w]:
                            if x > u and x != v and x != w and x in adj[u]:
                                cycles_by_length[4].append((u, v, w, x))
                                if len(cycles_by_length[4]) >= max_cycles:
                                    break
                        if len(cycles_by_length[4]) >= max_cycles:
                            break
                if len(cycles_by_length[4]) >= max_cycles:
                    break
        if len(cycles_by_length[4]) >= max_cycles:
            break

    # Length 5
    for u in nodes:
        for v in adj[u]:
            if v != u:
                for w in adj[v]:
                    if w != u and w != v:
                        for x in adj[w]:
                            if x != u and x != v and x != w:
                                for y in adj[x]:
                                    if y > u and y != v and y != w and y != x and y in adj[u]:
                                        cycles_by_length[5].append((u, v, w, x, y))
                                        if len(cycles_by_length[5]) >= max_cycles:
                                            break
                                if len(cycles_by_length[5]) >= max_cycles:
                                    break
                        if len(cycles_by_length[5]) >= max_cycles:
                            break
                if len(cycles_by_length[5]) >= max_cycles:
                    break
        if len(cycles_by_length[5]) >= max_cycles:
            break

    all_cycles = []
    for length in [3, 4, 5]:
        all_cycles.extend(cycles_by_length[length])
    return all_cycles, cycles_by_length

# =====================================================================
# POLYMORPHISM OPERATIONS
# =====================================================================

def op_median(a, b, c):
    return (a and b) or (b and c) or (a and c)

def op_and(a, b, c):
    return a and b and c

def op_or(a, b, c):
    return a or b or c

def op_xor(a, b, c):
    return a ^ b ^ c

def ternary_op_from_index(idx):
    """Return a ternary Boolean function from its truth table index (0-255).
    The truth table has 8 entries for (a,b,c) in {0,1}^3 ordered as
    (0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1).
    """
    def op(a, b, c):
        bit_idx = (int(a) << 2) | (int(b) << 1) | int(c)
        return bool((idx >> bit_idx) & 1)
    return op

def is_projection(idx):
    return idx in PROJECTION_INDICES

def is_essentially_unary(idx):
    return idx in ESSENTIALLY_UNARY

# =====================================================================
# HOLONOMY COMPUTATION
# =====================================================================

def compute_h1(solutions, polymorphism_fn, n):
    """H1 = closure fraction: for all triples of solutions, apply polymorphism
    bitwise and check if result is a solution."""
    if len(solutions) < 3:
        return None  # Not enough solutions to test
    sol_set = set(solutions)
    # Sample triples if too many
    num_sols = len(solutions)
    if num_sols <= 20:
        triples = list(itertools.combinations(range(num_sols), 3))
        # Also include triples with repetition (important for polymorphism definition)
        for i in range(num_sols):
            for j in range(num_sols):
                for k in range(num_sols):
                    if (i,j,k) not in [(a,b,c) for a,b,c in triples]:
                        triples.append((i,j,k))
        # Actually, let's be precise: test ALL ordered triples
        triples = list(itertools.product(range(num_sols), repeat=3))
    else:
        # Sample
        triples = [tuple(random.choices(range(num_sols), k=3)) for _ in range(5000)]

    closed = 0
    total = len(triples)
    for i, j, k in triples:
        s1, s2, s3 = solutions[i], solutions[j], solutions[k]
        result = tuple(polymorphism_fn(s1[v], s2[v], s3[v]) for v in range(n))
        if result in sol_set:
            closed += 1
    return closed / total if total > 0 else None

def check_op_preserves(solutions, op_fn, n):
    """Check if ternary op preserves the solution set (for ALL ordered triples)."""
    sol_set = set(solutions)
    num_sols = len(solutions)
    if num_sols < 1:
        return True  # vacuously true

    # For small solution sets, check all ordered triples
    if num_sols <= 15:
        for s1 in solutions:
            for s2 in solutions:
                for s3 in solutions:
                    result = tuple(op_fn(s1[v], s2[v], s3[v]) for v in range(n))
                    if result not in sol_set:
                        return False
        return True
    else:
        # Sample heavily
        for _ in range(10000):
            idx = random.choices(range(num_sols), k=3)
            s1, s2, s3 = solutions[idx[0]], solutions[idx[1]], solutions[idx[2]]
            result = tuple(op_fn(s1[v], s2[v], s3[v]) for v in range(n))
            if result not in sol_set:
                return False
        return True

# =====================================================================
# MAIN VERIFICATION
# =====================================================================

def generate_satisfiable_instances(gen_fn, n, num_instances, mode='or', max_attempts=200):
    """Generate instances that have at least 3 solutions (for meaningful triple tests)."""
    instances = []
    attempts = 0
    while len(instances) < num_instances and attempts < max_attempts * num_instances:
        attempts += 1
        clauses = gen_fn(n)
        sols = enumerate_solutions(clauses, n, mode=mode)
        if len(sols) >= 3:
            instances.append((clauses, sols))
    return instances

def run_p_time_verification():
    """Part (a): Verify P-time classes have H1=1.0 with known polymorphisms."""
    print("=" * 70)
    print("PART (a): P-TIME CLASSES — Known polymorphism closure")
    print("=" * 70)

    classes = [
        ("2-SAT",     gen_2sat,      'or',  op_median, "median"),
        ("Horn-SAT",  gen_horn,      'or',  op_and,    "AND"),
        ("Dual-Horn", gen_dual_horn, 'or',  op_or,     "OR"),
        ("XOR-SAT",   gen_xor,      'xor', op_xor,    "XOR"),
    ]

    results = {}
    for name, gen_fn, mode, poly_fn, poly_name in classes:
        print(f"\n--- {name} (polymorphism: {poly_name}) ---")
        instances = generate_satisfiable_instances(gen_fn, N_VARS, N_INSTANCES, mode=mode)
        print(f"  Generated {len(instances)} satisfiable instances with >=3 solutions")

        h1_values = []
        cycle_counts = {3: 0, 4: 0, 5: 0}
        for idx, (clauses, sols) in enumerate(instances):
            adj, edges = build_constraint_graph(clauses, N_VARS)
            all_cycles, by_len = find_cycles(adj, N_VARS)
            for L in [3, 4, 5]:
                cycle_counts[L] += len(by_len[L])

            h1 = compute_h1(sols, poly_fn, N_VARS)
            if h1 is not None:
                h1_values.append(h1)

        if h1_values:
            min_h1 = min(h1_values)
            max_h1 = max(h1_values)
            mean_h1 = sum(h1_values) / len(h1_values)
            all_perfect = all(h == 1.0 for h in h1_values)
        else:
            min_h1 = max_h1 = mean_h1 = None
            all_perfect = False

        print(f"  Cycles found: {cycle_counts}")
        print(f"  H1 values: min={min_h1}, max={max_h1}, mean={mean_h1:.6f}" if mean_h1 is not None else "  H1: insufficient data")
        print(f"  All H1 = 1.0? {'YES' if all_perfect else 'NO *** FAIL ***'}")

        results[name] = {
            'polymorphism': poly_name,
            'num_instances': len(instances),
            'h1_min': min_h1,
            'h1_max': max_h1,
            'h1_mean': mean_h1,
            'all_perfect': all_perfect,
            'cycle_counts': cycle_counts,
        }

    return results

def run_npc_verification():
    """Part (b) & (c): NPC classes — scan all 256 ternary ops."""
    print("\n" + "=" * 70)
    print("PART (b)+(c): NPC CLASSES — All 256 ternary operations")
    print("=" * 70)

    classes = [
        ("3-SAT",     gen_3sat,    'or'),
        ("NAE-3-SAT", gen_nae3sat, 'nae'),
    ]

    results = {}
    for name, gen_fn, mode in classes:
        print(f"\n--- {name} ---")
        instances = generate_satisfiable_instances(gen_fn, N_VARS, N_INSTANCES, mode=mode)
        print(f"  Generated {len(instances)} satisfiable instances with >=3 solutions")

        # For each instance, find which ops preserve solutions
        # Track separately: essentially unary vs Taylor (non-essentially-unary)
        per_instance_taylor_counts = []
        per_instance_taylor_ops = []
        per_instance_all_counts = []
        per_instance_all_ops = []

        for idx, (clauses, sols) in enumerate(instances):
            preserved_taylor = set()
            preserved_all = set()  # non-projection, including neg-proj
            for op_idx in range(256):
                if op_idx in PROJECTION_INDICES:
                    continue
                op_fn = ternary_op_from_index(op_idx)
                if check_op_preserves(sols, op_fn, N_VARS):
                    preserved_all.add(op_idx)
                    if not is_essentially_unary(op_idx):
                        preserved_taylor.add(op_idx)
            per_instance_taylor_counts.append(len(preserved_taylor))
            per_instance_taylor_ops.append(preserved_taylor)
            per_instance_all_counts.append(len(preserved_all))
            per_instance_all_ops.append(preserved_all)
            if (idx + 1) % 10 == 0:
                print(f"    Instance {idx+1}/{len(instances)}: {len(preserved_taylor)} Taylor ops, {len(preserved_all)} total non-proj ops")

        # Cross-instance intersection for Taylor ops
        if per_instance_taylor_ops:
            taylor_intersection = per_instance_taylor_ops[0].copy()
            for ops in per_instance_taylor_ops[1:]:
                taylor_intersection &= ops

            running_taylor = per_instance_taylor_ops[0].copy()
            taylor_shrinkage = [len(running_taylor)]
            for i in range(1, len(per_instance_taylor_ops)):
                running_taylor &= per_instance_taylor_ops[i]
                taylor_shrinkage.append(len(running_taylor))
        else:
            taylor_intersection = set()
            taylor_shrinkage = []

        # Cross-instance intersection for ALL non-projection ops (including neg-proj)
        if per_instance_all_ops:
            all_intersection = per_instance_all_ops[0].copy()
            for ops in per_instance_all_ops[1:]:
                all_intersection &= ops
        else:
            all_intersection = set()

        # Classify what survives cross-instance
        surviving_essentially_unary = all_intersection & ESSENTIALLY_UNARY
        surviving_taylor = all_intersection - ESSENTIALLY_UNARY

        print(f"\n  Per-instance accidental polymorphisms (Taylor only, excluding essentially unary):")
        print(f"    Min: {min(per_instance_taylor_counts)}")
        print(f"    Max: {max(per_instance_taylor_counts)}")
        print(f"    Mean: {sum(per_instance_taylor_counts)/len(per_instance_taylor_counts):.1f}")
        print(f"    Median: {sorted(per_instance_taylor_counts)[len(per_instance_taylor_counts)//2]}")

        print(f"\n  Per-instance accidental polymorphisms (all non-projection, including neg-proj):")
        print(f"    Min: {min(per_instance_all_counts)}")
        print(f"    Max: {max(per_instance_all_counts)}")
        print(f"    Mean: {sum(per_instance_all_counts)/len(per_instance_all_counts):.1f}")

        print(f"\n  Cross-instance intersection (across ALL {len(instances)} instances):")
        print(f"    Taylor ops surviving: {len(surviving_taylor)}")
        print(f"    Essentially unary surviving (neg-proj/const): {len(surviving_essentially_unary)} = {sorted(surviving_essentially_unary)}")
        if surviving_taylor:
            print(f"    *** KILL SIGNAL: {len(surviving_taylor)} Taylor ops survive cross-instance! ***")
            for op_idx in sorted(surviving_taylor):
                tt = format(op_idx, '08b')
                print(f"      Op {op_idx} (0b{tt})")
        else:
            print(f"    PASS: No Taylor (non-essentially-unary) op is consistent across all instances.")

        if surviving_essentially_unary:
            print(f"    Note: {len(surviving_essentially_unary)} essentially unary ops survive (expected for NAE-SAT due to complement closure)")

        print(f"\n  Taylor intersection shrinkage:")
        for i in range(0, len(taylor_shrinkage), 5):
            chunk = taylor_shrinkage[i:i+5]
            indices = list(range(i+1, i+1+len(chunk)))
            print(f"    After instances {indices}: {chunk}")

        results[name] = {
            'num_instances': len(instances),
            'per_instance_taylor_counts': per_instance_taylor_counts,
            'per_instance_all_counts': per_instance_all_counts,
            'taylor_intersection_count': len(surviving_taylor),
            'taylor_intersection_ops': sorted(surviving_taylor),
            'essentially_unary_surviving': sorted(surviving_essentially_unary),
            'taylor_shrinkage': taylor_shrinkage,
            'is_kill': len(surviving_taylor) > 0,
        }

    return results

def main():
    print("O7-HOLONOMY Independent Re-verification")
    print(f"Parameters: n={N_VARS}, instances={N_INSTANCES}, seed={SEED}")
    print(f"Date: 2026-04-12")
    print()

    p_results = run_p_time_verification()
    npc_results = run_npc_verification()

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print("\nP-time classes:")
    all_p_pass = True
    for name, r in p_results.items():
        status = "PASS" if r['all_perfect'] else "FAIL"
        if not r['all_perfect']:
            all_p_pass = False
        print(f"  {name}: H1={r['h1_min']:.6f}..{r['h1_max']:.6f}  [{status}]")

    print("\nNPC classes:")
    any_kill = False
    for name, r in npc_results.items():
        cnt = r['taylor_intersection_count']
        eu = r['essentially_unary_surviving']
        status = "KILL" if cnt > 0 else "PASS"
        if cnt > 0:
            any_kill = True
        print(f"  {name}: {cnt} Taylor ops across all instances  [{status}]")
        if eu:
            print(f"    (also {len(eu)} essentially unary ops survive: {eu} -- expected for complement-closed problems)")
        tc = r['per_instance_taylor_counts']
        print(f"    Per-instance Taylor polymorphisms: {min(tc)}..{max(tc)} (mean {sum(tc)/len(tc):.1f})")

    print()
    if all_p_pass and not any_kill:
        print("OVERALL VERDICT: O7-HOLONOMY CONFIRMED")
        print("  - All P-time classes: H1 = 1.0 with known polymorphism (trivial holonomy)")
        print("  - All NPC classes: 0 Taylor ops survive cross-instance test (non-trivial holonomy)")
        print("  - Accidental per-instance polymorphisms exist but vanish in intersection")
        print("  - For NAE-SAT: negated projections survive (complement closure), but these")
        print("    are essentially unary and do NOT constitute Taylor operations")
    elif any_kill:
        print("*** OVERALL VERDICT: KILL — Taylor ops survived cross-instance test ***")
    else:
        print("OVERALL VERDICT: PARTIAL FAILURE — check details above")

    return p_results, npc_results

if __name__ == '__main__':
    main()
