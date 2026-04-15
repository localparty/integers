"""
Independent re-verification of PATB-DIAGONAL entry.

Claim: A Taylor polymorphism f (satisfying f(x,...,x) = x) for a CSP Gamma
fixes the diagonal of the Boolean operator algebra. The separation is EXACT
at the language level: P-time Schaefer classes admit non-trivial Taylor
polymorphisms, while 3-SAT admits only projections.

Date: 2026-04-12
"""

import random
import itertools
from collections import defaultdict

random.seed(42)

# ============================================================
# Utility: enumerate all solutions to a CNF over n Boolean vars
# ============================================================

def all_solutions(clauses, n):
    """Brute-force enumerate all satisfying assignments for a CNF."""
    sols = []
    for bits in range(1 << n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        sat = True
        for clause in clauses:
            clause_sat = False
            for (var, sign) in clause:
                val = assignment[var]
                if sign:  # positive literal
                    clause_sat = clause_sat or (val == 1)
                else:     # negative literal
                    clause_sat = clause_sat or (val == 0)
            if not clause_sat:
                sat = False
                break
        if sat:
            sols.append(assignment)
    return sols


def is_solution(assignment, clauses):
    for clause in clauses:
        clause_sat = False
        for (var, sign) in clause:
            val = assignment[var]
            if sign:
                clause_sat = clause_sat or (val == 1)
            else:
                clause_sat = clause_sat or (val == 0)
        if not clause_sat:
            return False
    return True


# ============================================================
# (a) 2-SAT + median
# ============================================================

def generate_2sat_instance(n, m):
    """Generate a random 2-SAT instance with n vars and m clauses."""
    clauses = []
    for _ in range(m):
        v1, v2 = random.sample(range(n), 2)
        s1, s2 = random.choice([True, False]), random.choice([True, False])
        clauses.append([(v1, s1), (v2, s2)])
    return clauses


def median(a, b, c):
    return tuple(sorted([a[i], b[i], c[i]])[1] for i in range(len(a)))


def test_2sat():
    print("=" * 60)
    print("(a) 2-SAT + MEDIAN polymorphism")
    print("=" * 60)
    n = 10
    m = 20
    num_instances = 20

    all_pass_closure = True
    all_pass_taylor = True
    sol_counts = []
    triples_tested_total = 0

    tested = 0
    for trial in range(200):  # try up to 200 to get 20 satisfiable
        clauses = generate_2sat_instance(n, m)
        sols = all_solutions(clauses, n)
        if len(sols) < 2:
            continue

        sol_set = set(sols)
        sol_counts.append(len(sols))

        # Taylor identity: median(s,s,s) = s
        for s in sols:
            if median(s, s, s) != s:
                all_pass_taylor = False

        # Closure: median of any 3 solutions is a solution
        triples_tested = 0
        for s1, s2, s3 in itertools.combinations(sols, 3):
            m_val = median(s1, s2, s3)
            triples_tested += 1
            if m_val not in sol_set:
                all_pass_closure = False
        # Also test with repetition (ordered triples)
        for s1, s2, s3 in itertools.product(sols, repeat=3):
            m_val = median(s1, s2, s3)
            if m_val not in sol_set:
                all_pass_closure = False
            triples_tested += 1

        triples_tested_total += triples_tested
        tested += 1
        if tested >= num_instances:
            break

    print(f"  Instances tested: {tested}")
    print(f"  Solution counts: min={min(sol_counts)}, max={max(sol_counts)}, "
          f"mean={sum(sol_counts)/len(sol_counts):.1f}")
    print(f"  Total triples tested: {triples_tested_total}")
    print(f"  Taylor identity (median(s,s,s)=s): {'PASS' if all_pass_taylor else 'FAIL'}")
    print(f"  Closure under median: {'PASS' if all_pass_closure else 'FAIL'}")
    print()
    return all_pass_closure and all_pass_taylor


# ============================================================
# (b) Horn-SAT + AND
# ============================================================

def generate_horn_instance(n, m):
    """Generate random Horn clauses: at most 1 positive literal per clause."""
    clauses = []
    for _ in range(m):
        k = random.choice([2, 3])
        vars_ = random.sample(range(n), k)
        # At most 1 positive literal
        num_positive = random.choice([0, 1])
        signs = [False] * k
        if num_positive == 1:
            pos_idx = random.randint(0, k - 1)
            signs[pos_idx] = True
        clauses.append(list(zip(vars_, signs)))
    return clauses


def bitwise_and(a, b):
    return tuple(a[i] & b[i] for i in range(len(a)))


def test_horn_sat():
    print("=" * 60)
    print("(b) Horn-SAT + AND polymorphism")
    print("=" * 60)
    n = 10
    m = 20
    num_instances = 20

    all_pass_closure = True
    all_pass_taylor = True
    sol_counts = []
    pairs_tested_total = 0

    tested = 0
    for trial in range(200):
        clauses = generate_horn_instance(n, m)
        sols = all_solutions(clauses, n)
        if len(sols) < 2:
            continue

        sol_set = set(sols)
        sol_counts.append(len(sols))

        # Taylor identity: AND(s,s) = s (idempotent)
        for s in sols:
            if bitwise_and(s, s) != s:
                all_pass_taylor = False

        # Closure: AND of any 2 solutions is a solution
        pairs_tested = 0
        for s1, s2 in itertools.product(sols, repeat=2):
            a_val = bitwise_and(s1, s2)
            if a_val not in sol_set:
                all_pass_closure = False
            pairs_tested += 1

        pairs_tested_total += pairs_tested
        tested += 1
        if tested >= num_instances:
            break

    print(f"  Instances tested: {tested}")
    print(f"  Solution counts: min={min(sol_counts)}, max={max(sol_counts)}, "
          f"mean={sum(sol_counts)/len(sol_counts):.1f}")
    print(f"  Total pairs tested: {pairs_tested_total}")
    print(f"  Taylor identity (AND(s,s)=s): {'PASS' if all_pass_taylor else 'FAIL'}")
    print(f"  Closure under AND: {'PASS' if all_pass_closure else 'FAIL'}")
    print()
    return all_pass_closure and all_pass_taylor


# ============================================================
# (c) XOR-SAT + ternary XOR
# ============================================================

def generate_xorsat_instance(n, m):
    """Generate random XOR-SAT: each constraint is x_i XOR x_j XOR x_k = b."""
    # Represent as list of (vars, target_parity)
    constraints = []
    for _ in range(m):
        vars_ = random.sample(range(n), 3)
        parity = random.choice([0, 1])
        constraints.append((vars_, parity))
    return constraints


def xorsat_solutions(constraints, n):
    """Enumerate all solutions to an XOR-SAT instance."""
    sols = []
    for bits in range(1 << n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        sat = True
        for (vars_, parity) in constraints:
            xor_val = 0
            for v in vars_:
                xor_val ^= assignment[v]
            if xor_val != parity:
                sat = False
                break
        if sat:
            sols.append(assignment)
    return sols


def ternary_xor(a, b, c):
    return tuple(a[i] ^ b[i] ^ c[i] for i in range(len(a)))


def test_xor_sat():
    print("=" * 60)
    print("(c) XOR-SAT + ternary XOR polymorphism")
    print("=" * 60)
    n = 10
    m = 20
    num_instances = 20

    all_pass_closure = True
    all_pass_taylor = True
    sol_counts = []
    triples_tested_total = 0

    tested = 0
    for trial in range(500):
        # Use fewer constraints to ensure satisfiability (XOR is a linear system)
        m_actual = random.randint(3, 8)  # fewer constraints for satisfiability
        constraints = generate_xorsat_instance(n, m_actual)
        sols = xorsat_solutions(constraints, n)
        if len(sols) < 2:
            continue

        sol_set = set(sols)
        sol_counts.append(len(sols))

        # Taylor identity: s XOR s XOR s = s
        for s in sols:
            if ternary_xor(s, s, s) != s:
                all_pass_taylor = False

        # Closure: XOR of any 3 solutions is a solution
        triples_tested = 0
        for s1, s2, s3 in itertools.product(sols, repeat=3):
            x_val = ternary_xor(s1, s2, s3)
            if x_val not in sol_set:
                all_pass_closure = False
            triples_tested += 1
            if triples_tested > 500000:  # safety cap
                break

        triples_tested_total += triples_tested
        tested += 1
        if tested >= num_instances:
            break

    print(f"  Instances tested: {tested}")
    if sol_counts:
        print(f"  Solution counts: min={min(sol_counts)}, max={max(sol_counts)}, "
              f"mean={sum(sol_counts)/len(sol_counts):.1f}")
    print(f"  Total triples tested: {triples_tested_total}")
    print(f"  Taylor identity (s XOR s XOR s = s): {'PASS' if all_pass_taylor else 'FAIL'}")
    print(f"  Closure under ternary XOR: {'PASS' if all_pass_closure else 'FAIL'}")
    print()
    return all_pass_closure and all_pass_taylor


# ============================================================
# (d) Dual-Horn + OR
# ============================================================

def generate_dual_horn_instance(n, m):
    """Dual-Horn: at most 1 NEGATIVE literal per clause."""
    clauses = []
    for _ in range(m):
        k = random.choice([2, 3])
        vars_ = random.sample(range(n), k)
        # At most 1 negative literal
        num_negative = random.choice([0, 1])
        signs = [True] * k  # all positive
        if num_negative == 1:
            neg_idx = random.randint(0, k - 1)
            signs[neg_idx] = False
        clauses.append(list(zip(vars_, signs)))
    return clauses


def bitwise_or(a, b):
    return tuple(a[i] | b[i] for i in range(len(a)))


def test_dual_horn():
    print("=" * 60)
    print("(d) Dual-Horn + OR polymorphism")
    print("=" * 60)
    n = 10
    m = 20
    num_instances = 20

    all_pass_closure = True
    all_pass_taylor = True
    sol_counts = []
    pairs_tested_total = 0

    tested = 0
    for trial in range(200):
        clauses = generate_dual_horn_instance(n, m)
        sols = all_solutions(clauses, n)
        if len(sols) < 2:
            continue

        sol_set = set(sols)
        sol_counts.append(len(sols))

        # Taylor identity: OR(s,s) = s
        for s in sols:
            if bitwise_or(s, s) != s:
                all_pass_taylor = False

        # Closure: OR of any 2 solutions is a solution
        pairs_tested = 0
        for s1, s2 in itertools.product(sols, repeat=2):
            o_val = bitwise_or(s1, s2)
            if o_val not in sol_set:
                all_pass_closure = False
            pairs_tested += 1

        pairs_tested_total += pairs_tested
        tested += 1
        if tested >= num_instances:
            break

    print(f"  Instances tested: {tested}")
    print(f"  Solution counts: min={min(sol_counts)}, max={max(sol_counts)}, "
          f"mean={sum(sol_counts)/len(sol_counts):.1f}")
    print(f"  Total pairs tested: {pairs_tested_total}")
    print(f"  Taylor identity (OR(s,s)=s): {'PASS' if all_pass_taylor else 'FAIL'}")
    print(f"  Closure under OR: {'PASS' if all_pass_closure else 'FAIL'}")
    print()
    return all_pass_closure and all_pass_taylor


# ============================================================
# (e) 3-SAT LANGUAGE-LEVEL test
# ============================================================

def test_3sat_language_level():
    """
    The 3-SAT language consists of ALL possible 3-literal clauses over {0,1}.
    Each 3-variable clause excludes exactly 1 of the 8 assignments to 3 vars.
    So there are 8 relation types, each being a set of 7 out of 8 tuples.

    For each ternary Boolean function f with f(x,x,x) = x (Taylor),
    check if f preserves ALL 8 relation types simultaneously.
    """
    print("=" * 60)
    print("(e) 3-SAT language-level test")
    print("=" * 60)

    # All 8 assignments to 3 Boolean variables
    all_8 = list(itertools.product([0, 1], repeat=3))

    # The 8 relation types for 3-SAT: each excludes exactly one assignment
    relations_3sat = []
    for excluded in all_8:
        rel = set(t for t in all_8 if t != excluded)
        relations_3sat.append(rel)

    # Enumerate all 256 ternary Boolean functions f: {0,1}^3 -> {0,1}
    # f is specified by its truth table on the 8 inputs
    taylor_count = 0
    projection_count = 0
    non_trivial_taylor_preserving = 0

    projections = set()
    # Projection x: f(a,b,c) = a
    projections.add(tuple(a for a, b, c in all_8))
    # Projection y: f(a,b,c) = b
    projections.add(tuple(b for a, b, c in all_8))
    # Projection z: f(a,b,c) = c
    projections.add(tuple(c for a, b, c in all_8))

    taylor_functions = []

    for func_bits in range(256):
        # Truth table
        tt = tuple((func_bits >> i) & 1 for i in range(8))

        # Check Taylor: f(x,x,x) = x for x in {0,1}
        # (0,0,0) is index 0, (1,1,1) is index 7
        idx_000 = all_8.index((0, 0, 0))
        idx_111 = all_8.index((1, 1, 1))
        if tt[idx_000] != 0 or tt[idx_111] != 1:
            continue

        taylor_count += 1
        taylor_functions.append(tt)

        is_projection = (tt in projections)
        if is_projection:
            projection_count += 1

        # Check if f preserves all 8 relations
        def f_apply(a, b, c):
            """Apply f componentwise to three 3-tuples."""
            result = []
            for j in range(3):
                idx = all_8.index((a[j], b[j], c[j]))
                result.append(tt[idx])
            return tuple(result)

        preserves_all = True
        for rel in relations_3sat:
            rel_list = list(rel)
            # f preserves rel if for any a,b,c in rel, f(a,b,c) in rel
            for a, b, c in itertools.product(rel_list, repeat=3):
                result = f_apply(a, b, c)
                if result not in rel:
                    preserves_all = False
                    break
            if not preserves_all:
                break

        if preserves_all and not is_projection:
            non_trivial_taylor_preserving += 1
            print(f"  WARNING: Non-trivial Taylor function preserves all 3-SAT relations: {tt}")

    total_preserving = projection_count + non_trivial_taylor_preserving  # projections always preserve
    # Actually let's count projections that preserve too (they always do)
    # Re-count: total that preserve all
    total_preserving_count = 0
    for tt in taylor_functions:
        is_proj = (tt in projections)

        def f_apply2(a, b, c):
            result = []
            for j in range(3):
                idx = all_8.index((a[j], b[j], c[j]))
                result.append(tt[idx])
            return tuple(result)

        preserves_all = True
        for rel in relations_3sat:
            rel_list = list(rel)
            for a, b, c in itertools.product(rel_list, repeat=3):
                result = f_apply2(a, b, c)
                if result not in rel:
                    preserves_all = False
                    break
            if not preserves_all:
                break

        if preserves_all:
            total_preserving_count += 1

    print(f"  Total ternary Boolean Taylor functions: {taylor_count}")
    print(f"  Of which are projections: {projection_count}")
    print(f"  Non-trivial Taylor: {taylor_count - projection_count}")
    print(f"  Taylor functions preserving ALL 3-SAT relations: {total_preserving_count}")
    print(f"  Non-trivial Taylor preserving ALL 3-SAT relations: {non_trivial_taylor_preserving}")
    print(f"  CLAIM: only projections (3) preserve all 3-SAT relations.")
    print(f"  RESULT: {'CONFIRMED' if non_trivial_taylor_preserving == 0 and total_preserving_count == 3 else 'FAILED'}")
    print()
    return non_trivial_taylor_preserving == 0 and total_preserving_count == 3


# ============================================================
# (f) NAE-3-SAT language-level test
# ============================================================

def test_nae3sat_language_level():
    """
    NAE-3-SAT: a clause is satisfied if not all 3 literals have the same value.
    The NAE relation on 3 variables: all tuples EXCEPT (0,0,0) and (1,1,1).
    That's 6 tuples out of 8.

    NAE-3-SAT language: consider all possible NAE constraints on 3 variables
    with possible negations. This gives relations that exclude exactly 2
    complementary assignments.

    For a 3-variable NAE clause with signs (s1,s2,s3), the relation is:
    { (a,b,c) : not all of (a^(1-s1), b^(1-s2), c^(1-s3)) equal }
    """
    print("=" * 60)
    print("(f) NAE-3-SAT language-level test")
    print("=" * 60)

    all_8 = list(itertools.product([0, 1], repeat=3))

    # NAE-3-SAT relations: for each sign pattern (s1,s2,s3),
    # the relation excludes the two assignments where all signed literals agree.
    # With signs (s1,s2,s3), excluded are: all-true and all-false after signing.
    # So excluded: (s1,s2,s3) and (1-s1,1-s2,1-s3)
    nae_relations = set()
    for signs in itertools.product([0, 1], repeat=3):
        excluded1 = signs
        excluded2 = tuple(1 - s for s in signs)
        rel = frozenset(t for t in all_8 if t != excluded1 and t != excluded2)
        nae_relations.add(rel)

    nae_relations = [set(r) for r in nae_relations]

    print(f"  Distinct NAE-3-SAT relation types: {len(nae_relations)}")

    # Enumerate Taylor functions
    projections = set()
    projections.add(tuple(a for a, b, c in all_8))
    projections.add(tuple(b for a, b, c in all_8))
    projections.add(tuple(c for a, b, c in all_8))

    taylor_count = 0
    non_trivial_preserving = 0
    total_preserving = 0

    for func_bits in range(256):
        tt = tuple((func_bits >> i) & 1 for i in range(8))

        idx_000 = all_8.index((0, 0, 0))
        idx_111 = all_8.index((1, 1, 1))
        if tt[idx_000] != 0 or tt[idx_111] != 1:
            continue

        taylor_count += 1
        is_projection = (tt in projections)

        def f_apply(a, b, c):
            result = []
            for j in range(3):
                idx = all_8.index((a[j], b[j], c[j]))
                result.append(tt[idx])
            return tuple(result)

        preserves_all = True
        for rel in nae_relations:
            rel_list = list(rel)
            for a, b, c in itertools.product(rel_list, repeat=3):
                result = f_apply(a, b, c)
                if result not in rel:
                    preserves_all = False
                    break
            if not preserves_all:
                break

        if preserves_all:
            total_preserving += 1
            if not is_projection:
                non_trivial_preserving += 1
                print(f"  Non-trivial Taylor preserving all NAE relations: {tt}")

    print(f"  Total Taylor functions: {taylor_count}")
    print(f"  Taylor functions preserving ALL NAE-3-SAT relations: {total_preserving}")
    print(f"  Non-trivial Taylor preserving all: {non_trivial_preserving}")

    # NAE-3-SAT is NP-complete, so we expect only projections
    nae_pass = (non_trivial_preserving == 0 and total_preserving == 3)
    print(f"  CLAIM: only projections (3) preserve all NAE-3-SAT relations.")
    print(f"  RESULT: {'CONFIRMED' if nae_pass else 'FAILED'}")
    print()
    return nae_pass


# ============================================================
# (g) Verify P-time languages at the language level
# ============================================================

def test_ptime_language_level():
    """
    Verify that median preserves all 2-SAT relations,
    AND preserves all Horn-SAT relations,
    OR preserves all dual-Horn relations,
    XOR preserves all XOR-SAT relations.
    """
    print("=" * 60)
    print("(g) P-time language-level verification")
    print("=" * 60)

    all_8 = list(itertools.product([0, 1], repeat=3))
    all_4 = list(itertools.product([0, 1], repeat=2))

    # --- 2-SAT relations ---
    # A 2-SAT clause on vars (x,y) with signs is a relation on 2 vars
    # that excludes exactly 1 of the 4 assignments.
    relations_2sat = []
    for excluded in all_4:
        rel = set(t for t in all_4 if t != excluded)
        relations_2sat.append(rel)

    def median_tuple(a, b, c):
        return tuple(sorted([a[i], b[i], c[i]])[1] for i in range(len(a)))

    median_preserves = True
    for rel in relations_2sat:
        rel_list = list(rel)
        for a, b, c in itertools.product(rel_list, repeat=3):
            result = median_tuple(a, b, c)
            if result not in rel:
                median_preserves = False
                break
        if not median_preserves:
            break

    print(f"  2-SAT: median preserves all 2-clause relations: {'PASS' if median_preserves else 'FAIL'}")

    # --- Horn-SAT relations ---
    # Horn clause on k vars: at most 1 positive literal.
    # For 3-variable Horn: clauses like (NOT x OR NOT y OR z), (NOT x OR NOT y OR NOT z), etc.
    # Relations: sets of 3-tuples satisfying a Horn clause.
    # A 3-literal Horn clause has at most 1 positive literal.
    # Signs: at most 1 True in the sign tuple.
    horn_relations = set()
    for num_pos in [0, 1]:
        for pos_positions in itertools.combinations(range(3), num_pos):
            signs = [False] * 3
            for p in pos_positions:
                signs[p] = True
            # Clause: OR of signed literals
            rel_tuples = []
            for t in all_8:
                clause_sat = False
                for j in range(3):
                    if signs[j]:
                        clause_sat = clause_sat or (t[j] == 1)
                    else:
                        clause_sat = clause_sat or (t[j] == 0)
                if clause_sat:
                    rel_tuples.append(t)
            horn_relations.add(frozenset(rel_tuples))

    horn_relations = [set(r) for r in horn_relations]

    def and_tuple(a, b):
        return tuple(a[i] & b[i] for i in range(len(a)))

    and_preserves = True
    for rel in horn_relations:
        rel_list = list(rel)
        for a, b in itertools.product(rel_list, repeat=2):
            result = and_tuple(a, b)
            if result not in rel:
                and_preserves = False
                break
        if not and_preserves:
            break

    print(f"  Horn-SAT: AND preserves all Horn-clause relations: {'PASS' if and_preserves else 'FAIL'}")

    # --- Dual-Horn relations ---
    # Dual-Horn: at most 1 negative literal per clause.
    dhorn_relations = set()
    for num_neg in [0, 1]:
        for neg_positions in itertools.combinations(range(3), num_neg):
            signs = [True] * 3
            for p in neg_positions:
                signs[p] = False
            rel_tuples = []
            for t in all_8:
                clause_sat = False
                for j in range(3):
                    if signs[j]:
                        clause_sat = clause_sat or (t[j] == 1)
                    else:
                        clause_sat = clause_sat or (t[j] == 0)
                if clause_sat:
                    rel_tuples.append(t)
            dhorn_relations.add(frozenset(rel_tuples))

    dhorn_relations = [set(r) for r in dhorn_relations]

    def or_tuple(a, b):
        return tuple(a[i] | b[i] for i in range(len(a)))

    or_preserves = True
    for rel in dhorn_relations:
        rel_list = list(rel)
        for a, b in itertools.product(rel_list, repeat=2):
            result = or_tuple(a, b)
            if result not in rel:
                or_preserves = False
                break
        if not or_preserves:
            break

    print(f"  Dual-Horn: OR preserves all dual-Horn relations: {'PASS' if or_preserves else 'FAIL'}")

    # --- XOR-SAT relations ---
    # XOR-SAT on 3 vars: x XOR y XOR z = b for b in {0,1}
    xor_relations = []
    for b in [0, 1]:
        rel = set(t for t in all_8 if (t[0] ^ t[1] ^ t[2]) == b)
        xor_relations.append(rel)

    def xor_tuple(a, b, c):
        return tuple(a[i] ^ b[i] ^ c[i] for i in range(len(a)))

    xor_preserves = True
    for rel in xor_relations:
        rel_list = list(rel)
        for a, b, c in itertools.product(rel_list, repeat=3):
            result = xor_tuple(a, b, c)
            if result not in rel:
                xor_preserves = False
                break
        if not xor_preserves:
            break

    print(f"  XOR-SAT: ternary XOR preserves all XOR relations: {'PASS' if xor_preserves else 'FAIL'}")
    print()

    return median_preserves and and_preserves and or_preserves and xor_preserves


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("PATB-DIAGONAL Independent Re-verification")
    print("Date: 2026-04-12")
    print()

    results = {}

    results['2sat'] = test_2sat()
    results['horn'] = test_horn_sat()
    results['xor'] = test_xor_sat()
    results['dual_horn'] = test_dual_horn()
    results['3sat_lang'] = test_3sat_language_level()
    results['nae3sat_lang'] = test_nae3sat_language_level()
    results['ptime_lang'] = test_ptime_language_level()

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for key, val in results.items():
        print(f"  {key}: {'PASS' if val else 'FAIL'}")

    all_pass = all(results.values())
    print()
    print(f"OVERALL: {'ALL TESTS PASS' if all_pass else 'SOME TESTS FAILED'}")
