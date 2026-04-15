"""
test_a2_winding_number.py -- Winding number of polymorphisms on constraint-graph cycles

Strategy A2 conjecture: the polymorphism type carries a winding number W
on constraint-graph cycles that is a topological invariant.
  - P-time languages have W != 0 (non-trivial topology = non-full).
  - NPC languages have W = 0 (trivial topology = full = rigid).

For each CSP class (2-SAT, Horn-SAT, XOR-SAT, 3-SAT) at n=10 with
30 random instances per class:

1. Build the constraint hypergraph, extract cycles.
2. For each cycle and polymorphism, compute the winding number W.
3. Test whether W distinguishes P-time from NPC.
4. Test topological invariance: W is the same for homotopic cycles.

Author: G Six, with Claude Opus 4.6 (1M context). Date: 2026-04-11.
"""

import random
import itertools
import math
from collections import defaultdict, deque

random.seed(42)

# =====================================================================
# POLYMORPHISM DEFINITIONS
# =====================================================================

def median3(a, b, c):
    """Majority vote: the P-time polymorphism for 2-SAT."""
    return tuple(1 if (a[i]+b[i]+c[i]) >= 2 else 0 for i in range(len(a)))

def xor3(a, b, c):
    """Ternary XOR (affine): the P-time polymorphism for XOR-SAT."""
    return tuple((a[i]+b[i]+c[i]) % 2 for i in range(len(a)))

def min3(a, b, c):
    """Ternary AND: the P-time polymorphism for Horn-SAT."""
    return tuple(min(a[i],b[i],c[i]) for i in range(len(a)))

def apply_ternary_table(table, a, b, c):
    """Apply an arbitrary ternary Boolean function from its truth table.
    table is an 8-element tuple: table[4*a_i + 2*b_i + c_i] for bits a_i,b_i,c_i."""
    return tuple(table[4*a[i] + 2*b[i] + c[i]] for i in range(len(a)))


# =====================================================================
# INSTANCE GENERATORS
# =====================================================================

def gen_2sat_instance(n, alpha=1.5):
    """Random 2-SAT instance."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 2)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses, 'or'

def gen_horn_instance(n, alpha=2.0):
    """Random Horn-SAT instance (at most one positive literal per clause)."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        k = random.randint(2, 3)
        vs = random.sample(range(1, n+1), min(k, n))
        pos_idx = random.randint(0, len(vs) - 1)
        clause = [-v if i != pos_idx else v for i, v in enumerate(vs)]
        clauses.append(clause)
    return clauses, 'or'

def gen_xor_instance(n, alpha=0.5):
    """Random XOR-SAT instance."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses, 'xor'

def gen_3sat_instance(n, alpha=3.5):
    """Random 3-SAT instance."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses, 'or'


# =====================================================================
# SAT SOLVER (brute force for n=10)
# =====================================================================

def find_solutions(clauses, n, mode='or'):
    """Enumerate all solutions by brute force."""
    solutions = []
    for bits in itertools.product([0, 1], repeat=n):
        sat = True
        for clause in clauses:
            if mode == 'or':
                ok = any((lit > 0 and bits[abs(lit)-1] == 1) or
                         (lit < 0 and bits[abs(lit)-1] == 0) for lit in clause)
                if not ok:
                    sat = False; break
            elif mode == 'xor':
                count = sum(1 for lit in clause
                            if (lit > 0 and bits[abs(lit)-1] == 1) or
                               (lit < 0 and bits[abs(lit)-1] == 0))
                if count % 2 == 0:
                    sat = False; break
        if sat:
            solutions.append(bits)
    return solutions


# =====================================================================
# CONSTRAINT GRAPH CONSTRUCTION
# =====================================================================

def build_constraint_graph(clauses, n):
    """Build the constraint graph: vertices are variables 0..n-1,
    edges connect variables that appear in the same clause.
    Returns adjacency list."""
    adj = defaultdict(set)
    for clause in clauses:
        vars_in_clause = [abs(lit) - 1 for lit in clause]
        for i in range(len(vars_in_clause)):
            for j in range(i+1, len(vars_in_clause)):
                u, v = vars_in_clause[i], vars_in_clause[j]
                adj[u].add(v)
                adj[v].add(u)
    return adj


# =====================================================================
# CYCLE FINDING
# =====================================================================

def find_all_short_cycles(adj, n, max_length=8):
    """Find all simple cycles of length <= max_length in the constraint graph.
    Uses DFS-based cycle enumeration."""
    cycles = []

    for start in range(n):
        # BFS/DFS to find short cycles starting from 'start'
        # Only find cycles where 'start' is the minimum vertex (avoids duplicates)
        stack = [(start, [start], {start})]
        while stack:
            current, path, visited = stack.pop()
            if len(path) > max_length:
                continue
            for neighbor in sorted(adj.get(current, set())):
                if neighbor == start and len(path) >= 3:
                    # Found a cycle
                    cycles.append(tuple(path))
                elif neighbor not in visited and neighbor > start and len(path) < max_length:
                    stack.append((neighbor, path + [neighbor], visited | {neighbor}))

    # Deduplicate: normalize each cycle to start with smallest vertex,
    # and choose the lexicographically smaller direction
    unique = set()
    result = []
    for c in cycles:
        # Normalize: rotate so smallest element is first
        min_idx = c.index(min(c))
        rotated = c[min_idx:] + c[:min_idx]
        # Also consider reverse
        rev = (rotated[0],) + tuple(reversed(rotated[1:]))
        key = min(rotated, rev)
        if key not in unique:
            unique.add(key)
            result.append(key)

    return result


def find_independent_cycle_basis(adj, n):
    """Find a cycle basis using a spanning tree.
    Each non-tree edge creates exactly one fundamental cycle.
    These cycles form a basis for the cycle space (first homology group)."""
    visited = [False] * n
    parent = [-1] * n
    depth = [0] * n
    tree_edges = set()
    non_tree_edges = []
    fundamental_cycles = []

    # Find connected component containing vertex 0
    # (or the first vertex with neighbors)
    start = -1
    for v in range(n):
        if adj.get(v):
            start = v
            break
    if start == -1:
        return [], []

    # BFS to build spanning tree
    queue = deque([start])
    visited[start] = True
    while queue:
        u = queue.popleft()
        for v in sorted(adj.get(u, set())):
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                tree_edges.add((min(u,v), max(u,v)))
                queue.append(v)
            else:
                edge = (min(u,v), max(u,v))
                if edge not in tree_edges and edge not in [(min(e[0],e[1]),max(e[0],e[1])) for e in non_tree_edges]:
                    non_tree_edges.append((u,v))

    # For each non-tree edge (u,v), find the fundamental cycle
    # by tracing paths from u and v back to their LCA
    for u, v in non_tree_edges:
        # Trace path from u to root
        path_u = []
        x = u
        while x != -1:
            path_u.append(x)
            x = parent[x]
        path_u_set = set(path_u)

        # Trace path from v until hitting path_u (= LCA)
        path_v = []
        x = v
        while x not in path_u_set and x != -1:
            path_v.append(x)
            x = parent[x]
        lca = x

        # Build cycle: path from u to lca + reverse path from v to lca
        cycle_part_u = []
        x = u
        while x != lca:
            cycle_part_u.append(x)
            x = parent[x]
        cycle_part_u.append(lca)

        cycle_part_v = []
        x = v
        while x != lca:
            cycle_part_v.append(x)
            x = parent[x]

        cycle = tuple(cycle_part_u + list(reversed(cycle_part_v)))
        if len(cycle) >= 3:
            fundamental_cycles.append(cycle)

    return fundamental_cycles, non_tree_edges


# =====================================================================
# WINDING NUMBER COMPUTATION
# =====================================================================

def compute_winding_number(cycle, solutions, poly_func, n):
    """Compute the winding number of a polymorphism around a cycle.

    Given a cycle C = (v_0, v_1, ..., v_{L-1}) and a ternary polymorphism f:

    1. Pick three solutions s1, s2, s3.
    2. Compute f_result = f(s1, s2, s3).
    3. For each edge (v_i, v_{i+1 mod L}):
       - The "phase" is whether the polymorphism FLIPS the value at v_{i+1}
         relative to the majority/reference solution.
       - Specifically: phase_i = sign(f_result[v_{i+1}] XOR ref[v_{i+1}])
         where ref = s1 (the first solution, as reference).
    4. The winding number W = number of sign changes in the phase sequence
       as we go around the cycle, mod 2.

    This captures whether the polymorphism introduces a topological twist
    (odd number of phase flips) or not (even number = contractible).

    Returns: W (0 or 1), and the raw phase sequence for diagnostics.
    """
    L = len(cycle)
    if len(solutions) < 3:
        return None, []

    # Use multiple triples and accumulate
    winding_numbers = []

    # Sample up to 50 triples of solutions
    n_sols = len(solutions)
    n_triples = min(50, n_sols * (n_sols-1) * (n_sols-2) // 6)
    triples_tried = set()

    for _ in range(n_triples * 3):  # oversample to get enough unique triples
        if len(triples_tried) >= n_triples:
            break
        idx = tuple(sorted(random.sample(range(n_sols), 3)))
        if idx in triples_tried:
            continue
        triples_tried.add(idx)
        i, j, k = idx
        s1, s2, s3 = solutions[i], solutions[j], solutions[k]

        # Check that the three solutions actually differ at some cycle vertex
        differs_on_cycle = False
        for v in cycle:
            if not (s1[v] == s2[v] == s3[v]):
                differs_on_cycle = True
                break
        if not differs_on_cycle:
            continue

        # Compute f(s1, s2, s3)
        f_result = poly_func(s1, s2, s3)

        # Compute phase at each cycle vertex:
        # phase[i] = f_result[v_i] XOR s1[v_i]  (1 if flipped, 0 if not)
        phases = [f_result[cycle[i]] ^ s1[cycle[i]] for i in range(L)]

        # Count phase transitions around the cycle
        n_flips = 0
        for i in range(L):
            if phases[i] != phases[(i+1) % L]:
                n_flips += 1

        # Winding number = parity of the number of phase transitions
        W = n_flips % 2
        winding_numbers.append(W)

    return winding_numbers


def compute_winding_number_v2(cycle, solutions, poly_func, n):
    """Alternative winding number: measures the cumulative rotation
    of the polymorphism image relative to the identity along the cycle.

    For each edge (v_i, v_{i+1}):
      delta_i = f(s1,s2,s3)[v_{i+1}] - f(s1,s2,s3)[v_i]
                - (s1[v_{i+1}] - s1[v_i])
    This is the "excess rotation" at each edge.
    W = sum of delta_i around the cycle (mod 2).

    This is a more geometric definition: it measures whether the
    polymorphism accumulates a net rotation around the cycle.
    """
    L = len(cycle)
    if len(solutions) < 3:
        return None

    winding_numbers = []
    n_sols = len(solutions)
    n_triples = min(50, max(10, n_sols * (n_sols-1) * (n_sols-2) // 6))
    triples_tried = set()

    for _ in range(n_triples * 3):
        if len(triples_tried) >= n_triples:
            break
        idx = tuple(sorted(random.sample(range(n_sols), 3)))
        if idx in triples_tried:
            continue
        triples_tried.add(idx)
        i, j, k = idx
        s1, s2, s3 = solutions[i], solutions[j], solutions[k]

        f_result = poly_func(s1, s2, s3)

        # Compute cumulative phase rotation
        total_delta = 0
        for i in range(L):
            v_curr = cycle[i]
            v_next = cycle[(i+1) % L]
            # Rotation of f relative to reference s1
            delta = (f_result[v_next] - f_result[v_curr]) - (s1[v_next] - s1[v_curr])
            total_delta += delta

        W = abs(total_delta) % 2
        winding_numbers.append(W)

    return winding_numbers


def compute_winding_holonomy(cycle, solutions, poly_func, n):
    """Holonomy-based winding number.

    Think of the polymorphism as a parallel transport operator along the
    constraint graph. For a cycle C = (v_0, ..., v_{L-1}):

    1. Start with solution s at v_0.
    2. At each edge (v_i, v_{i+1}), the polymorphism f acts on the
       local "fiber" (the set of possible values at v_{i+1}).
    3. After going around the entire cycle, we return to v_0.
       The holonomy is whether the fiber value has been flipped.

    Concretely:
    - Pick three solutions s1, s2, s3 that differ at v_0.
    - f(s1,s2,s3) either agrees or disagrees with s1 at v_0.
    - Track the "agreement pattern" around the cycle.
    - The winding number is the number of agreement-to-disagreement
      transitions mod 2.

    This is closest to the spin-statistics connection: a particle
    (= solution) transported around a loop picks up a phase (= sign).
    """
    L = len(cycle)
    if len(solutions) < 3:
        return None

    winding_numbers = []
    n_sols = len(solutions)
    n_triples = min(100, max(20, n_sols * (n_sols-1) * (n_sols-2) // 6))
    triples_tried = set()

    for _ in range(n_triples * 3):
        if len(triples_tried) >= n_triples:
            break
        idx = tuple(sorted(random.sample(range(n_sols), 3)))
        if idx in triples_tried:
            continue
        triples_tried.add(idx)
        i, j, k = idx
        s1, s2, s3 = solutions[i], solutions[j], solutions[k]

        f_result = poly_func(s1, s2, s3)

        # Agreement pattern: does f agree with s1 at each cycle vertex?
        agreement = [1 if f_result[cycle[i]] == s1[cycle[i]] else 0
                     for i in range(L)]

        # Count transitions in agreement pattern around the cycle
        transitions = 0
        for i in range(L):
            if agreement[i] != agreement[(i+1) % L]:
                transitions += 1

        # The holonomy winding number
        W = transitions % 2
        winding_numbers.append(W)

    return winding_numbers


# =====================================================================
# ALL 256 TERNARY BOOLEAN OPERATIONS
# =====================================================================

def enumerate_all_ternary_ops():
    """Generate all 256 ternary Boolean functions.
    Each is specified by a truth table: an 8-tuple indexed by (a,b,c) in
    {0,1}^3, giving f(a,b,c) in {0,1}.
    Returns list of (table, name) pairs."""
    ops = []
    for bits in range(256):
        table = tuple((bits >> i) & 1 for i in range(8))
        # Classify
        name = f"op_{bits:03d}"
        # Check if it's a known operation
        if table == (0, 0, 0, 1, 0, 1, 1, 1):  # median
            name = "MEDIAN"
        elif table == (0, 1, 1, 0, 1, 0, 0, 1):  # XOR
            name = "XOR"
        elif table == (0, 0, 0, 0, 0, 0, 0, 1):  # AND
            name = "AND"
        elif table == (0, 1, 1, 1, 1, 1, 1, 1):  # OR
            name = "OR"
        # Check if projection
        is_proj = False
        if table == (0, 0, 0, 0, 1, 1, 1, 1):
            name = "proj_a"; is_proj = True
        elif table == (0, 0, 1, 1, 0, 0, 1, 1):
            name = "proj_b"; is_proj = True
        elif table == (0, 1, 0, 1, 0, 1, 0, 1):
            name = "proj_c"; is_proj = True
        ops.append((table, name, is_proj))
    return ops


# =====================================================================
# MAIN TEST
# =====================================================================

N_VAR = 10
N_INSTANCES = 30

csp_generators = {
    '2-SAT': (gen_2sat_instance, median3, 'median'),
    'Horn-SAT': (gen_horn_instance, min3, 'AND/min'),
    'XOR-SAT': (gen_xor_instance, xor3, 'XOR'),
    '3-SAT': (gen_3sat_instance, None, 'none'),
}


print("=" * 72)
print("A2 WINDING NUMBER TEST")
print("Conjecture: polymorphism type carries a winding number on")
print("constraint-graph cycles that is a topological invariant.")
print("=" * 72)


# =====================================================================
# TEST 1: Winding numbers for P-time classes with their polymorphisms
# =====================================================================

print("\n" + "=" * 72)
print("TEST 1: Winding numbers for P-time polymorphisms on cycles")
print("=" * 72)

all_results = {}

for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT']:
    gen_func, poly_func, poly_name = csp_generators[csp_name]
    print(f"\n--- {csp_name} with {poly_name} polymorphism ---")

    instance_stats = []
    all_W_values = []
    all_W_v2_values = []
    all_W_hol_values = []
    n_instances_with_cycles = 0
    n_cycles_total = 0

    for trial in range(N_INSTANCES):
        clauses, mode = gen_func(N_VAR)
        solutions = find_solutions(clauses, N_VAR, mode=mode)
        if len(solutions) < 3:
            continue

        adj = build_constraint_graph(clauses, N_VAR)
        fund_cycles, _ = find_independent_cycle_basis(adj, N_VAR)
        all_cycles = find_all_short_cycles(adj, N_VAR, max_length=7)

        if not all_cycles:
            continue

        n_instances_with_cycles += 1
        n_cycles_total += len(all_cycles)

        for cycle in all_cycles:
            W_list = compute_winding_number(cycle, solutions, poly_func, N_VAR)
            W_v2_list = compute_winding_number_v2(cycle, solutions, poly_func, N_VAR)
            W_hol_list = compute_winding_holonomy(cycle, solutions, poly_func, N_VAR)

            if W_list:
                all_W_values.extend(W_list)
            if W_v2_list:
                all_W_v2_values.extend(W_v2_list)
            if W_hol_list:
                all_W_hol_values.extend(W_hol_list)

    # Statistics
    if all_W_values:
        w0 = all_W_values.count(0)
        w1 = all_W_values.count(1)
        total = len(all_W_values)
        frac_nonzero = w1 / total
        print(f"  Phase-flip winding:   W=0: {w0}/{total} ({100*w0/total:.1f}%)  "
              f"W=1: {w1}/{total} ({100*w1/total:.1f}%)")
    else:
        frac_nonzero = None
        print(f"  Phase-flip winding:   no data")

    if all_W_v2_values:
        w0 = all_W_v2_values.count(0)
        w1 = all_W_v2_values.count(1)
        total = len(all_W_v2_values)
        frac_nonzero_v2 = w1 / total
        print(f"  Rotation winding:     W=0: {w0}/{total} ({100*w0/total:.1f}%)  "
              f"W=1: {w1}/{total} ({100*w1/total:.1f}%)")
    else:
        frac_nonzero_v2 = None
        print(f"  Rotation winding:     no data")

    if all_W_hol_values:
        w0 = all_W_hol_values.count(0)
        w1 = all_W_hol_values.count(1)
        total = len(all_W_hol_values)
        frac_nonzero_hol = w1 / total
        print(f"  Holonomy winding:     W=0: {w0}/{total} ({100*w0/total:.1f}%)  "
              f"W=1: {w1}/{total} ({100*w1/total:.1f}%)")
    else:
        frac_nonzero_hol = None
        print(f"  Holonomy winding:     no data")

    print(f"  Instances with cycles: {n_instances_with_cycles}")
    print(f"  Total cycles tested:   {n_cycles_total}")

    all_results[csp_name] = {
        'frac_nonzero_phase': frac_nonzero,
        'frac_nonzero_rot': frac_nonzero_v2,
        'frac_nonzero_hol': frac_nonzero_hol,
        'n_instances': n_instances_with_cycles,
        'n_cycles': n_cycles_total,
        'W_phase': all_W_values,
        'W_rot': all_W_v2_values,
        'W_hol': all_W_hol_values,
    }


# =====================================================================
# TEST 2: Winding numbers for 3-SAT with ALL 256 ternary operations
# =====================================================================

print("\n" + "=" * 72)
print("TEST 2: 3-SAT winding numbers over all 256 ternary operations")
print("=" * 72)

all_ternary_ops = enumerate_all_ternary_ops()

# Collect 3-SAT instances
print("\nGenerating 3-SAT instances...")
sat3_instances = []
for trial in range(N_INSTANCES * 2):  # oversample to get enough
    if len(sat3_instances) >= N_INSTANCES:
        break
    clauses, mode = gen_3sat_instance(N_VAR)
    solutions = find_solutions(clauses, N_VAR, mode=mode)
    if len(solutions) < 3:
        continue
    adj = build_constraint_graph(clauses, N_VAR)
    all_cycles = find_all_short_cycles(adj, N_VAR, max_length=6)
    if all_cycles:
        sat3_instances.append((clauses, solutions, adj, all_cycles))

print(f"  Got {len(sat3_instances)} instances with cycles")

# For each operation, compute winding numbers across all instances
op_winding_stats = {}
n_ops_tested = 0

# Test all 256 operations but report key ones
key_op_indices = []
all_W_3sat_phase = []
all_W_3sat_hol = []

for table, op_name, is_proj in all_ternary_ops:
    poly_func = lambda a, b, c, t=table: apply_ternary_table(t, a, b, c)

    W_phase_all = []
    W_hol_all = []

    for clauses, solutions, adj, cycles in sat3_instances:
        # Test on up to 5 cycles per instance (for speed)
        for cycle in cycles[:5]:
            W_list = compute_winding_number(cycle, solutions, poly_func, N_VAR)
            W_hol = compute_winding_holonomy(cycle, solutions, poly_func, N_VAR)
            if W_list:
                W_phase_all.extend(W_list)
            if W_hol:
                W_hol_all.extend(W_hol)

    if W_phase_all:
        frac_nz_phase = W_phase_all.count(1) / len(W_phase_all)
    else:
        frac_nz_phase = None

    if W_hol_all:
        frac_nz_hol = W_hol_all.count(1) / len(W_hol_all)
    else:
        frac_nz_hol = None

    op_winding_stats[op_name] = {
        'frac_nz_phase': frac_nz_phase,
        'frac_nz_hol': frac_nz_hol,
        'n_samples_phase': len(W_phase_all),
        'n_samples_hol': len(W_hol_all),
    }
    all_W_3sat_phase.extend(W_phase_all)
    all_W_3sat_hol.extend(W_hol_all)
    n_ops_tested += 1

print(f"\n  Tested {n_ops_tested} ternary operations")

# Report overall 3-SAT statistics
if all_W_3sat_phase:
    w0 = all_W_3sat_phase.count(0)
    w1 = all_W_3sat_phase.count(1)
    total = len(all_W_3sat_phase)
    frac_3sat_nz_phase = w1 / total
    print(f"  Overall phase-flip:   W=0: {w0}/{total} ({100*w0/total:.1f}%)  "
          f"W=1: {w1}/{total} ({100*w1/total:.1f}%)")
else:
    frac_3sat_nz_phase = None

if all_W_3sat_hol:
    w0 = all_W_3sat_hol.count(0)
    w1 = all_W_3sat_hol.count(1)
    total = len(all_W_3sat_hol)
    frac_3sat_nz_hol = w1 / total
    print(f"  Overall holonomy:     W=0: {w0}/{total} ({100*w0/total:.1f}%)  "
          f"W=1: {w1}/{total} ({100*w1/total:.1f}%)")
else:
    frac_3sat_nz_hol = None

all_results['3-SAT'] = {
    'frac_nonzero_phase': frac_3sat_nz_phase,
    'frac_nonzero_hol': frac_3sat_nz_hol,
    'n_instances': len(sat3_instances),
}

# Report named operations specifically
print("\n  Named operations in 3-SAT context:")
for op_name in ['MEDIAN', 'XOR', 'AND', 'OR', 'proj_a', 'proj_b', 'proj_c']:
    if op_name in op_winding_stats:
        s = op_winding_stats[op_name]
        phase_str = f"{s['frac_nz_phase']:.3f}" if s['frac_nz_phase'] is not None else "N/A"
        hol_str = f"{s['frac_nz_hol']:.3f}" if s['frac_nz_hol'] is not None else "N/A"
        print(f"    {op_name:>8s}:  phase W!=0 = {phase_str}  "
              f"holonomy W!=0 = {hol_str}")


# =====================================================================
# TEST 3: Distribution analysis -- does W concentrate differently?
# =====================================================================

print("\n" + "=" * 72)
print("TEST 3: Distribution analysis of W across classes")
print("=" * 72)

print(f"\n{'Class':>12s} {'method':>12s} {'W=0 frac':>10s} {'W=1 frac':>10s} {'bias':>8s}")
print("-" * 56)

for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT', '3-SAT']:
    r = all_results[csp_name]
    for method, key in [('phase-flip', 'frac_nonzero_phase'),
                        ('holonomy', 'frac_nonzero_hol')]:
        frac = r.get(key)
        if frac is not None:
            w0_frac = 1 - frac
            bias = abs(frac - 0.5)
            print(f"{csp_name:>12s} {method:>12s} {w0_frac:10.4f} {frac:10.4f} {bias:8.4f}")
        else:
            print(f"{csp_name:>12s} {method:>12s} {'N/A':>10s} {'N/A':>10s} {'N/A':>8s}")


# =====================================================================
# TEST 4: Topological invariance -- same W for homotopic cycles
# =====================================================================

print("\n" + "=" * 72)
print("TEST 4: Topological invariance of W")
print("  Testing: do homotopic cycles give the same W?")
print("=" * 72)

def are_homotopic(cycle1, cycle2, adj):
    """Two cycles are homotopic if one can be deformed into the other
    by a sequence of elementary moves. Two cycles sharing L-1 vertices
    in order (differing by a single "triangle flip") are homotopic
    if the bypassed vertex is adjacent to the replacement vertex.

    More practically: cycles that bound the same region of the graph
    are homotopic. We test a weaker condition: cycles in the same
    homology class (same boundary in Z/2Z) should have the same W
    if W is a genuine topological invariant."""
    s1 = set(cycle1)
    s2 = set(cycle2)
    # Symmetric difference should be small for "nearby" cycles
    sym_diff = s1.symmetric_difference(s2)
    shared = s1.intersection(s2)
    return len(sym_diff) <= 2 and len(shared) >= max(len(cycle1), len(cycle2)) - 1


print("\nFor each P-time class, find pairs of homotopic cycles")
print("and check if their winding numbers agree.\n")

for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT']:
    gen_func, poly_func, poly_name = csp_generators[csp_name]
    n_homotopic_pairs = 0
    n_agree = 0
    n_disagree = 0
    n_instances_checked = 0

    for trial in range(N_INSTANCES):
        clauses, mode = gen_func(N_VAR)
        solutions = find_solutions(clauses, N_VAR, mode=mode)
        if len(solutions) < 3:
            continue

        adj = build_constraint_graph(clauses, N_VAR)
        all_cycles = find_all_short_cycles(adj, N_VAR, max_length=7)
        if len(all_cycles) < 2:
            continue

        n_instances_checked += 1

        # Compute W for each cycle (using a fixed set of solution triples)
        cycle_W_map = {}
        for cycle in all_cycles:
            W_list = compute_winding_holonomy(cycle, solutions, poly_func, N_VAR)
            if W_list:
                # Use the majority W value as "the" winding number
                w0_count = W_list.count(0)
                w1_count = W_list.count(1)
                dominant_W = 0 if w0_count >= w1_count else 1
                cycle_W_map[cycle] = dominant_W

        # Check homotopic pairs
        cycles_list = list(cycle_W_map.keys())
        for i in range(len(cycles_list)):
            for j in range(i+1, len(cycles_list)):
                c1, c2 = cycles_list[i], cycles_list[j]
                if are_homotopic(c1, c2, adj):
                    n_homotopic_pairs += 1
                    if cycle_W_map[c1] == cycle_W_map[c2]:
                        n_agree += 1
                    else:
                        n_disagree += 1

    if n_homotopic_pairs > 0:
        agree_rate = n_agree / n_homotopic_pairs
        print(f"  {csp_name}: {n_homotopic_pairs} homotopic pairs found "
              f"({n_instances_checked} instances)")
        print(f"    Agreement: {n_agree}/{n_homotopic_pairs} ({100*agree_rate:.1f}%)")
        print(f"    Disagreement: {n_disagree}/{n_homotopic_pairs}")
    else:
        print(f"  {csp_name}: no homotopic pairs found ({n_instances_checked} instances)")
        agree_rate = None

    all_results[csp_name]['homotopy_agree_rate'] = agree_rate if n_homotopic_pairs > 0 else None
    all_results[csp_name]['n_homotopic_pairs'] = n_homotopic_pairs


# =====================================================================
# TEST 5: Fundamental cycle basis -- is W a homology invariant?
# =====================================================================

print("\n" + "=" * 72)
print("TEST 5: W on fundamental cycle basis (homology test)")
print("  If W is a genuine H_1 invariant, it defines a cohomology class")
print("  in H^1(constraint_graph, Z/2Z).")
print("=" * 72)

print("\nFor each P-time class: compute W on the fundamental cycle basis")
print("and check if composite cycles have W = sum of basis Ws (mod 2).\n")

for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT']:
    gen_func, poly_func, poly_name = csp_generators[csp_name]
    n_tests = 0
    n_additive = 0
    n_non_additive = 0
    n_instances_with_basis = 0

    for trial in range(N_INSTANCES):
        clauses, mode = gen_func(N_VAR)
        solutions = find_solutions(clauses, N_VAR, mode=mode)
        if len(solutions) < 3:
            continue

        adj = build_constraint_graph(clauses, N_VAR)
        fund_cycles, non_tree_edges = find_independent_cycle_basis(adj, N_VAR)

        if len(fund_cycles) < 2:
            continue

        n_instances_with_basis += 1

        # Compute W for each fundamental cycle
        basis_W = {}
        for idx, cycle in enumerate(fund_cycles):
            W_list = compute_winding_holonomy(cycle, solutions, poly_func, N_VAR)
            if W_list:
                w0_count = W_list.count(0)
                w1_count = W_list.count(1)
                basis_W[idx] = 0 if w0_count >= w1_count else 1

        # Test additivity: for pairs of fundamental cycles that share
        # a subpath, the composite cycle's W should be the XOR of the
        # individual Ws (since we're working mod 2).
        for i in range(len(fund_cycles)):
            for j in range(i+1, len(fund_cycles)):
                if i not in basis_W or j not in basis_W:
                    continue
                c1 = set(fund_cycles[i])
                c2 = set(fund_cycles[j])
                shared = c1.intersection(c2)
                if len(shared) >= 2:  # They share a subpath
                    # The composite cycle has vertices in symmetric difference + shared endpoints
                    composite_verts = c1.symmetric_difference(c2) | shared
                    # Build the composite cycle from the constraint graph
                    composite_cycles = find_all_short_cycles(
                        {v: adj[v].intersection(composite_verts) for v in composite_verts},
                        N_VAR, max_length=len(fund_cycles[i]) + len(fund_cycles[j])
                    )
                    for comp_cycle in composite_cycles:
                        W_comp_list = compute_winding_holonomy(
                            comp_cycle, solutions, poly_func, N_VAR)
                        if W_comp_list:
                            w0 = W_comp_list.count(0)
                            w1 = W_comp_list.count(1)
                            W_comp = 0 if w0 >= w1 else 1
                            expected = (basis_W[i] + basis_W[j]) % 2
                            n_tests += 1
                            if W_comp == expected:
                                n_additive += 1
                            else:
                                n_non_additive += 1
                            break  # One composite test per pair

    if n_tests > 0:
        rate = n_additive / n_tests
        print(f"  {csp_name}: {n_tests} additivity tests "
              f"({n_instances_with_basis} instances)")
        print(f"    Additive (W_comp = W_1 + W_2 mod 2): "
              f"{n_additive}/{n_tests} ({100*rate:.1f}%)")
        print(f"    Non-additive: {n_non_additive}/{n_tests}")
    else:
        rate = None
        print(f"  {csp_name}: no additivity tests possible "
              f"({n_instances_with_basis} instances with basis)")

    all_results[csp_name]['additivity_rate'] = rate
    all_results[csp_name]['n_additivity_tests'] = n_tests


# =====================================================================
# TEST 6: Concentration test -- is the W distribution DIFFERENT
#          for P-time vs NPC?
# =====================================================================

print("\n" + "=" * 72)
print("TEST 6: Statistical concentration test (P-time vs NPC)")
print("=" * 72)

print("\nThe conjecture predicts:")
print("  P-time: W concentrated at nonzero value (non-trivial topology)")
print("  NPC:    W concentrated at 0 or uniformly distributed (trivial topology)")

# For each method, check if the W distributions separate P from NPC
for method_name, key in [('Phase-flip', 'W_phase'), ('Holonomy', 'W_hol')]:
    print(f"\n  Method: {method_name}")
    p_fracs = []
    npc_frac = None

    for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT']:
        W_data = all_results[csp_name].get(key, [])
        if W_data:
            frac_1 = W_data.count(1) / len(W_data)
            p_fracs.append((csp_name, frac_1))
            print(f"    {csp_name}: W=1 fraction = {frac_1:.4f} (n={len(W_data)})")

    # For 3-SAT, compute per-operation statistics
    if method_name == 'Holonomy':
        npc_vals = all_W_3sat_hol
    else:
        npc_vals = all_W_3sat_phase

    if npc_vals:
        npc_frac = npc_vals.count(1) / len(npc_vals)
        print(f"    3-SAT (all ops): W=1 fraction = {npc_frac:.4f} (n={len(npc_vals)})")

    # Check separation
    if p_fracs and npc_frac is not None:
        p_mean = sum(f for _, f in p_fracs) / len(p_fracs)
        separation = abs(p_mean - npc_frac)
        print(f"    P-time mean W=1 fraction: {p_mean:.4f}")
        print(f"    NPC W=1 fraction: {npc_frac:.4f}")
        print(f"    Separation: {separation:.4f}")

        if separation > 0.15:
            print(f"    --> MEANINGFUL SEPARATION (gap = {separation:.4f})")
        elif separation > 0.05:
            print(f"    --> WEAK SEPARATION (gap = {separation:.4f})")
        else:
            print(f"    --> NO SEPARATION (gap = {separation:.4f})")


# =====================================================================
# VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("VERDICT")
print("=" * 72)

# Criterion 1: P-time should have W != 0 concentrated
p_time_nonzero = True
p_time_data = {}
for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT']:
    r = all_results[csp_name]
    # Check if there's a significant deviation from 50% (random)
    for key in ['frac_nonzero_phase', 'frac_nonzero_hol']:
        frac = r.get(key)
        if frac is not None:
            bias = abs(frac - 0.5)
            p_time_data[(csp_name, key)] = (frac, bias)

# Criterion 2: NPC should have W = 0 or W random (no concentration at nonzero)
r_3sat = all_results.get('3-SAT', {})
npc_phase = r_3sat.get('frac_nonzero_phase')
npc_hol = r_3sat.get('frac_nonzero_hol')

# Criterion 3: Topological invariance for P-time
topo_invariant = True
for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT']:
    r = all_results[csp_name]
    agree = r.get('homotopy_agree_rate')
    if agree is not None and agree < 0.8:
        topo_invariant = False

# Decision logic
print("\n1. P-time winding number concentration:")
any_p_concentrated = False
for (csp_name, method), (frac, bias) in p_time_data.items():
    status = "concentrated" if bias > 0.1 else "random-like"
    print(f"   {csp_name} ({method}): frac(W=1)={frac:.4f}, bias={bias:.4f} -> {status}")
    if bias > 0.1:
        any_p_concentrated = True

print(f"\n2. NPC winding number:")
npc_random = True
if npc_phase is not None:
    npc_phase_bias = abs(npc_phase - 0.5)
    print(f"   3-SAT (phase): frac(W=1)={npc_phase:.4f}, bias={npc_phase_bias:.4f}")
    if npc_phase_bias > 0.2:
        npc_random = False
if npc_hol is not None:
    npc_hol_bias = abs(npc_hol - 0.5)
    print(f"   3-SAT (holonomy): frac(W=1)={npc_hol:.4f}, bias={npc_hol_bias:.4f}")
    if npc_hol_bias > 0.2:
        npc_random = False

print(f"\n3. Topological invariance:")
for csp_name in ['2-SAT', 'Horn-SAT', 'XOR-SAT']:
    r = all_results[csp_name]
    agree = r.get('homotopy_agree_rate')
    n_pairs = r.get('n_homotopic_pairs', 0)
    if agree is not None:
        print(f"   {csp_name}: {100*agree:.1f}% agreement ({n_pairs} homotopic pairs)")
    else:
        print(f"   {csp_name}: no homotopic pairs found")

# For the separation to be meaningful, we need:
# (a) P-time W distribution significantly different from random (bias > 0.1)
# (b) NPC W distribution close to random or concentrated at 0
# (c) The two distributions are significantly different
# (d) W is topologically invariant (homotopic cycles give same W)

p_concentrated = any_p_concentrated
npc_trivial = npc_random

# Check separation
separates = False
for method_key, npc_key in [('frac_nonzero_phase', npc_phase),
                             ('frac_nonzero_hol', npc_hol)]:
    if npc_key is None:
        continue
    p_vals = [all_results[c].get(method_key) for c in ['2-SAT', 'Horn-SAT', 'XOR-SAT']
              if all_results[c].get(method_key) is not None]
    if p_vals:
        p_mean = sum(p_vals) / len(p_vals)
        if abs(p_mean - npc_key) > 0.1:
            separates = True

print(f"\n{'='*72}")
if p_concentrated and npc_trivial and separates and topo_invariant:
    verdict = "PASS"
    print(f"VERDICT: PASS")
    print(f"  The winding number W distinguishes P-time from NPC:")
    print(f"  - P-time polymorphisms produce concentrated W (non-trivial topology)")
    print(f"  - NPC operations produce random/zero W (trivial topology)")
    print(f"  - W is topologically invariant (homotopic cycles agree)")
elif p_concentrated and separates:
    verdict = "WEAK PASS"
    print(f"VERDICT: WEAK PASS")
    print(f"  The winding number shows some separation but:")
    if not topo_invariant:
        print(f"  - Topological invariance is NOT confirmed")
    if not npc_trivial:
        print(f"  - NPC winding numbers are not trivial")
elif not separates:
    verdict = "KILL"
    print(f"VERDICT: KILL")
    print(f"  The winding number does NOT separate P-time from NPC.")
    print(f"  The W distribution is statistically indistinguishable between classes.")
    print(f"  Conjecture A2 is FALSIFIED by this computational test.")
else:
    verdict = "INCONCLUSIVE"
    print(f"VERDICT: INCONCLUSIVE")
    print(f"  Insufficient data or mixed signals.")

print(f"{'='*72}")

# Store verdict
all_results['verdict'] = verdict
