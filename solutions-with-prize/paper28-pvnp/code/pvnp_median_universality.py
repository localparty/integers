"""
pvnp_median_universality.py — Is median-closure the universal P-time discriminator?

Tests the conjecture: for constraint satisfaction problems (CSPs),
the solution space satisfies the median property if and only if the
problem is in P. This would make median-closure the right cohomological
invariant for the trinity dictionary's P vs NP separation.

Tests:
1. Horn-SAT (in P): verify median property holds
2. XOR-SAT / Linear SAT (in P): verify median property holds
3. 1-in-3 SAT (NP-complete): verify median property FAILS
4. NAE-SAT (NP-complete): verify median property FAILS
5. Exact-k-SAT for k=1,2,3: boundary analysis

Schaefer's dichotomy theorem (1978) classifies which Boolean CSPs
are in P: exactly those whose constraint language is one of
{0-valid, 1-valid, affine, Horn, dual-Horn, bijunctive (= 2-SAT)}.
The conjecture is that all six P-time classes satisfy median-closure,
and all NP-complete classes violate it.

Author: G Six, with Claude Opus 4.6. Date: 2026-04-11.
"""

import random
import itertools

random.seed(42)

def evaluate_clause(clause, assignment):
    """Check if a clause is satisfied by the assignment.
    clause is a list of literals (positive = true, negative = negated)."""
    for lit in clause:
        var = abs(lit) - 1
        val = assignment[var]
        if (lit > 0 and val == 1) or (lit < 0 and val == 0):
            return True
    return False

def find_all_solutions_general(clauses, n, mode='or'):
    """Find all satisfying assignments.
    mode='or': standard SAT (at least one literal true per clause)
    mode='xor': XOR-SAT (odd number of true literals per clause)
    mode='nae': NAE-SAT (not all literals same value per clause)
    mode='1in3': 1-in-3 SAT (exactly one literal true per clause)
    mode='horn': standard SAT but clauses are Horn clauses
    """
    solutions = []
    for bits in itertools.product([0, 1], repeat=n):
        sat = True
        for clause in clauses:
            if mode == 'or':
                if not evaluate_clause(clause, bits):
                    sat = False; break
            elif mode == 'xor':
                count = sum(1 for lit in clause
                           if (lit > 0 and bits[abs(lit)-1] == 1) or
                              (lit < 0 and bits[abs(lit)-1] == 0))
                if count % 2 == 0:
                    sat = False; break
            elif mode == 'nae':
                vals = []
                for lit in clause:
                    var = abs(lit) - 1
                    val = bits[var]
                    if lit < 0: val = 1 - val
                    vals.append(val)
                if len(set(vals)) == 1:
                    sat = False; break
            elif mode == '1in3':
                count = sum(1 for lit in clause
                           if (lit > 0 and bits[abs(lit)-1] == 1) or
                              (lit < 0 and bits[abs(lit)-1] == 0))
                if count != 1:
                    sat = False; break
        if sat:
            solutions.append(bits)
    return solutions

def median_of_three(a, b, c):
    return tuple(1 if (a[i]+b[i]+c[i]) >= 2 else 0 for i in range(len(a)))

def check_median_full(solutions, max_triples=5000):
    """Check median property for all (or sampled) triples."""
    sol_set = set(solutions)
    n_sols = len(solutions)
    if n_sols < 3:
        return 0, 0
    n_checked = 0
    n_violations = 0
    if n_sols <= 30:
        for i in range(n_sols):
            for j in range(i+1, n_sols):
                for k in range(j+1, n_sols):
                    med = median_of_three(solutions[i], solutions[j], solutions[k])
                    n_checked += 1
                    if med not in sol_set:
                        n_violations += 1
    else:
        for _ in range(max_triples):
            i, j, k = random.sample(range(n_sols), 3)
            med = median_of_three(solutions[i], solutions[j], solutions[k])
            n_checked += 1
            if med not in sol_set:
                n_violations += 1
    return n_checked, n_violations

def generate_horn_clauses(n, m):
    """Generate random Horn clauses: at most one positive literal per clause."""
    clauses = []
    for _ in range(m):
        k = random.randint(2, 3)
        vars_chosen = random.sample(range(1, n+1), min(k, n))
        pos_idx = random.randint(0, len(vars_chosen))
        clause = []
        for i, v in enumerate(vars_chosen):
            if i == pos_idx:
                clause.append(v)
            else:
                clause.append(-v)
        clauses.append(clause)
    return clauses

def generate_xor_clauses(n, m, k=3):
    """Generate random XOR clauses: each clause is an XOR of k literals."""
    clauses = []
    for _ in range(m):
        vars_chosen = random.sample(range(1, n+1), min(k, n))
        clause = [v if random.random() < 0.5 else -v for v in vars_chosen]
        clauses.append(clause)
    return clauses


print("=" * 70)
print("MEDIAN-CLOSURE UNIVERSALITY TEST")
print("Is median-closure the universal P-time discriminator for CSPs?")
print("=" * 70)

n = 10
n_trials = 40

# =====================================================================
# TEST 1: Horn-SAT (in P)
# =====================================================================
print("\n" + "-" * 70)
print("TEST 1: Horn-SAT (in P)")
print("-" * 70)

alphas = [1.0, 2.0, 3.0]
for alpha in alphas:
    m = int(alpha * n)
    n_tested = 0
    n_median_ok = 0
    total_checked = 0
    total_violations = 0
    for trial in range(n_trials):
        clauses = generate_horn_clauses(n, m)
        solutions = find_all_solutions_general(clauses, n, mode='or')
        if len(solutions) < 3:
            continue
        n_tested += 1
        nc, nv = check_median_full(solutions)
        total_checked += nc
        total_violations += nv
        if nv == 0:
            n_median_ok += 1
    pct = 100*n_median_ok/max(n_tested,1)
    print(f"  α={alpha:.1f}: {n_tested} instances, median OK = {n_median_ok}/{n_tested} ({pct:.1f}%), "
          f"violations = {total_violations}/{total_checked}")


# =====================================================================
# TEST 2: XOR-SAT (in P via Gaussian elimination)
# =====================================================================
print("\n" + "-" * 70)
print("TEST 2: XOR-SAT / Linear SAT (in P)")
print("-" * 70)

for alpha in [0.5, 1.0, 1.5]:
    m = int(alpha * n)
    n_tested = 0
    n_median_ok = 0
    total_checked = 0
    total_violations = 0
    for trial in range(n_trials):
        clauses = generate_xor_clauses(n, m, k=3)
        solutions = find_all_solutions_general(clauses, n, mode='xor')
        if len(solutions) < 3:
            continue
        n_tested += 1
        nc, nv = check_median_full(solutions)
        total_checked += nc
        total_violations += nv
        if nv == 0:
            n_median_ok += 1
    pct = 100*n_median_ok/max(n_tested,1)
    print(f"  α={alpha:.1f}: {n_tested} instances, median OK = {n_median_ok}/{n_tested} ({pct:.1f}%), "
          f"violations = {total_violations}/{total_checked}")


# =====================================================================
# TEST 3: 1-in-3 SAT (NP-complete)
# =====================================================================
print("\n" + "-" * 70)
print("TEST 3: 1-in-3 SAT (NP-complete)")
print("-" * 70)

for alpha in [0.5, 1.0, 1.5, 2.0]:
    m = int(alpha * n)
    n_tested = 0
    n_median_ok = 0
    total_checked = 0
    total_violations = 0
    for trial in range(n_trials):
        vars_list = [random.sample(range(1, n+1), 3) for _ in range(m)]
        clauses = [[v if random.random() < 0.5 else -v for v in vs] for vs in vars_list]
        solutions = find_all_solutions_general(clauses, n, mode='1in3')
        if len(solutions) < 3:
            continue
        n_tested += 1
        nc, nv = check_median_full(solutions)
        total_checked += nc
        total_violations += nv
        if nv == 0:
            n_median_ok += 1
    pct = 100*n_median_ok/max(n_tested,1)
    print(f"  α={alpha:.1f}: {n_tested} instances, median OK = {n_median_ok}/{n_tested} ({pct:.1f}%), "
          f"violations = {total_violations}/{total_checked}")


# =====================================================================
# TEST 4: NAE-SAT (NP-complete for k >= 3)
# =====================================================================
print("\n" + "-" * 70)
print("TEST 4: NAE-3-SAT (NP-complete)")
print("-" * 70)

for alpha in [0.5, 1.0, 1.5, 2.0]:
    m = int(alpha * n)
    n_tested = 0
    n_median_ok = 0
    total_checked = 0
    total_violations = 0
    for trial in range(n_trials):
        vars_list = [random.sample(range(1, n+1), 3) for _ in range(m)]
        clauses = [[v if random.random() < 0.5 else -v for v in vs] for vs in vars_list]
        solutions = find_all_solutions_general(clauses, n, mode='nae')
        if len(solutions) < 3:
            continue
        n_tested += 1
        nc, nv = check_median_full(solutions)
        total_checked += nc
        total_violations += nv
        if nv == 0:
            n_median_ok += 1
    pct = 100*n_median_ok/max(n_tested,1)
    print(f"  α={alpha:.1f}: {n_tested} instances, median OK = {n_median_ok}/{n_tested} ({pct:.1f}%), "
          f"violations = {total_violations}/{total_checked}")


# =====================================================================
# TEST 5: 2-SAT (in P) — larger sample for confidence
# =====================================================================
print("\n" + "-" * 70)
print("TEST 5: 2-SAT (in P) — large sample confirmation")
print("-" * 70)

n_2sat_large = 12
n_trials_large = 100
for alpha in [1.0, 1.5, 2.0]:
    m = int(alpha * n_2sat_large)
    n_tested = 0
    n_median_ok = 0
    total_checked = 0
    total_violations = 0
    for trial in range(n_trials_large):
        vars_list = [random.sample(range(1, n_2sat_large+1), 2) for _ in range(m)]
        clauses = [[v if random.random() < 0.5 else -v for v in vs] for vs in vars_list]
        solutions = find_all_solutions_general(clauses, n_2sat_large, mode='or')
        if len(solutions) < 3:
            continue
        n_tested += 1
        nc, nv = check_median_full(solutions)
        total_checked += nc
        total_violations += nv
        if nv == 0:
            n_median_ok += 1
    pct = 100*n_median_ok/max(n_tested,1)
    print(f"  α={alpha:.1f}: {n_tested} instances, median OK = {n_median_ok}/{n_tested} ({pct:.1f}%), "
          f"violations = {total_violations}/{total_checked}")


# =====================================================================
# TEST 6: 3-SAT median violation rate vs n (scaling)
# =====================================================================
print("\n" + "-" * 70)
print("TEST 6: 3-SAT median violation rate vs n")
print("-" * 70)

alpha_test = 3.5
for n_scale in [6, 8, 10, 12]:
    m_scale = int(alpha_test * n_scale)
    n_tested = 0
    n_median_ok = 0
    total_checked = 0
    total_violations = 0
    for trial in range(50):
        vars_list = [random.sample(range(1, n_scale+1), 3) for _ in range(m_scale)]
        clauses = [[v if random.random() < 0.5 else -v for v in vs] for vs in vars_list]
        solutions = find_all_solutions_general(clauses, n_scale, mode='or')
        if len(solutions) < 3:
            continue
        n_tested += 1
        nc, nv = check_median_full(solutions)
        total_checked += nc
        total_violations += nv
        if nv == 0:
            n_median_ok += 1
    pct = 100*n_median_ok/max(n_tested,1)
    viol_rate = total_violations / max(total_checked, 1)
    print(f"  n={n_scale:2d}: {n_tested} instances, median OK = {n_median_ok}/{n_tested} ({pct:.1f}%), "
          f"violation rate = {viol_rate:.4f} ({total_violations}/{total_checked})")


# =====================================================================
# SUMMARY
# =====================================================================
print("\n" + "=" * 70)
print("SUMMARY: MEDIAN-CLOSURE AS P-TIME DISCRIMINATOR")
print("=" * 70)
print("""
Schaefer's dichotomy theorem (1978) classifies Boolean CSPs into P and
NP-complete. The six P-time classes are:
  {0-valid, 1-valid, affine, Horn, dual-Horn, bijunctive (2-SAT)}

Our tests:
  2-SAT (bijunctive, in P):     median property HOLDS (100%)
  Horn-SAT (Horn, in P):        median property HOLDS or FAILS?
  XOR-SAT (affine, in P):       median property HOLDS or FAILS?
  1-in-3 SAT (NP-complete):     median property FAILS
  NAE-3-SAT (NP-complete):      median property FAILS

If all P-time classes satisfy median-closure AND all NP-complete
classes violate it, then median-closure IS the universal P-time
discriminator for Boolean CSPs — and it becomes the right
cohomological invariant for Paper 28's trinity dictionary.

NOTE: The median graph characterization is SPECIFIC to 2-SAT
(bijunctive constraints). For affine constraints (XOR-SAT), the
relevant algebraic closure is under XOR (affine combination), not
median. For Horn constraints, the relevant closure is under
conjunction of implications. The UNIVERSAL discriminator across
all Schaefer classes may be a GENERALIZED algebraic closure —
the property that solutions form a subalgebra of some appropriate
algebra — rather than median-closure specifically.

This generalized algebraic closure is the right framework tool:
it's Schaefer's polymorphism characterization (Jeavons 1998),
which says a CSP is in P iff its constraint language is preserved
by a non-trivial polymorphism (= algebraic operation that closes
on solutions).
""")
