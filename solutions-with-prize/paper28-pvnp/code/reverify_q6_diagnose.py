"""
Diagnostic: investigate the NAE-3-SAT k=5 hits and Horn/XOR zero-hits.

Key question: are the NAE-3-SAT hits false positives from insufficient
tuple coverage, or genuine polymorphisms?
"""

import random
import itertools
import math
import time

random.seed(2026_04_12)

def find_solutions_bruteforce(clauses, n, mode='or'):
    solutions = []
    for val in range(1 << n):
        bits = tuple((val >> (n - 1 - i)) & 1 for i in range(n))
        sat = True
        for clause in clauses:
            if mode == 'or':
                ok = any(
                    (lit > 0 and bits[abs(lit) - 1] == 1) or
                    (lit < 0 and bits[abs(lit) - 1] == 0)
                    for lit in clause
                )
                if not ok:
                    sat = False; break
            elif mode == 'xor':
                count = sum(
                    1 for lit in clause
                    if (lit > 0 and bits[abs(lit) - 1] == 1) or
                       (lit < 0 and bits[abs(lit) - 1] == 0)
                )
                if count % 2 == 0:
                    sat = False; break
            elif mode == 'nae':
                vals = set()
                for lit in clause:
                    v = bits[abs(lit) - 1]
                    if lit < 0:
                        v = 1 - v
                    vals.add(v)
                if len(vals) == 1:
                    sat = False; break
        if sat:
            solutions.append(bits)
    return solutions


def _gen_raw(n, csp_type, alpha=None):
    if csp_type == '2-SAT':
        m = int((alpha or 1.5) * n)
        clauses = []
        for _ in range(m):
            vs = random.sample(range(1, n + 1), 2)
            clause = [v if random.random() < 0.5 else -v for v in vs]
            clauses.append(clause)
        return clauses, 'or'
    elif csp_type == 'Horn':
        m = int((alpha or 2.0) * n)
        clauses = []
        for _ in range(m):
            width = random.randint(2, 3)
            vs = random.sample(range(1, n + 1), min(width, n))
            pos_idx = random.randint(0, len(vs) - 1)
            clause = [-v if i != pos_idx else v for i, v in enumerate(vs)]
            clauses.append(clause)
        return clauses, 'or'
    elif csp_type == 'Dual-Horn':
        m = int((alpha or 2.0) * n)
        clauses = []
        for _ in range(m):
            width = random.randint(2, 3)
            vs = random.sample(range(1, n + 1), min(width, n))
            neg_idx = random.randint(0, len(vs) - 1)
            clause = [v if i != neg_idx else -v for i, v in enumerate(vs)]
            clauses.append(clause)
        return clauses, 'or'
    elif csp_type == 'XOR-SAT':
        m = int((alpha or 0.5) * n)
        clauses = []
        for _ in range(m):
            vs = random.sample(range(1, n + 1), 3)
            clause = [v if random.random() < 0.5 else -v for v in vs]
            clauses.append(clause)
        return clauses, 'xor'
    elif csp_type == '3-SAT':
        m = int((alpha or 3.0) * n)
        clauses = []
        for _ in range(m):
            vs = random.sample(range(1, n + 1), 3)
            clause = [v if random.random() < 0.5 else -v for v in vs]
            clauses.append(clause)
        return clauses, 'or'
    elif csp_type == 'NAE-3-SAT':
        m = int((alpha or 1.5) * n)
        clauses = []
        for _ in range(m):
            vs = random.sample(range(1, n + 1), 3)
            clause = [v if random.random() < 0.5 else -v for v in vs]
            clauses.append(clause)
        return clauses, 'nae'


def gen_instance(n, csp_type, alpha=None):
    for attempt in range(200):
        clauses, mode = _gen_raw(n, csp_type, alpha)
        sols = find_solutions_bruteforce(clauses, n, mode)
        if len(sols) >= 5:
            return clauses, mode, sols
    raise RuntimeError(f"Could not generate satisfiable {csp_type} instance")


def check_tt_preserves_ALL_tuples(tt, solutions, k):
    """Exhaustively check if tt preserves Sol for ALL k-tuples of solutions.
    This is the ground-truth check (exponential in |Sol|^k but reliable).
    For small |Sol| this is feasible.
    """
    sol_set = set(solutions)
    n_bits = len(solutions[0])
    n_sols = len(solutions)

    # For |Sol|^k too large, sample exhaustively up to a limit
    if n_sols ** k > 500000:
        # Sample 500k tuples
        for _ in range(500000):
            tup = tuple(random.randint(0, n_sols - 1) for _ in range(k))
            patterns = []
            for b in range(n_bits):
                pat_idx = 0
                for j in range(k):
                    pat_idx = 2 * pat_idx + solutions[tup[j]][b]
                patterns.append(pat_idx)
            output = tuple((tt >> patterns[b]) & 1 for b in range(n_bits))
            if output not in sol_set:
                return False
        return True  # survived 500k random tuples
    else:
        for tup in itertools.product(range(n_sols), repeat=k):
            patterns = []
            for b in range(n_bits):
                pat_idx = 0
                for j in range(k):
                    pat_idx = 2 * pat_idx + solutions[tup[j]][b]
                patterns.append(pat_idx)
            output = tuple((tt >> patterns[b]) & 1 for b in range(n_bits))
            if output not in sol_set:
                return False
        return True


def build_projection_tts(k):
    tt_size = 1 << k
    proj_set = set()
    for proj_idx in range(k):
        tt = 0
        for j in range(tt_size):
            bit_val = (j >> (k - 1 - proj_idx)) & 1
            tt |= (bit_val << j)
        proj_set.add(tt)
    return proj_set


# =========================================================================
# DIAGNOSTIC 1: NAE-3-SAT false positive check
# =========================================================================
print("=" * 60)
print("DIAGNOSTIC 1: NAE-3-SAT k=5 hit verification")
print("=" * 60)

# Reproduce the exact instances and find the ones with hits
# We need to replay the same RNG sequence
random.seed(2026_04_12)

# Skip through 2-SAT (20), Horn (20), Dual-Horn (20), XOR-SAT (20), 3-SAT (20)
# to reach NAE-3-SAT
classes_before = ['2-SAT', 'Horn', 'Dual-Horn', 'XOR-SAT', '3-SAT']

# Actually, let's just re-find NAE instances with hits directly
# by using a fresh seed and searching
random.seed(2026_04_12)

# Replay ALL instances in order to keep RNG in sync
all_instances = {}
for csp_type in ['2-SAT', 'Horn', 'Dual-Horn', 'XOR-SAT', '3-SAT', 'NAE-3-SAT']:
    all_instances[csp_type] = []
    for i in range(20):
        clauses, mode, sols = gen_instance(10, csp_type)
        all_instances[csp_type].append((clauses, mode, sols))

# Now test NAE-3-SAT instances at k=5 with MORE samples and EXHAUSTIVE tuple checking
print("\nNAE-3-SAT instances (20 total, n=10):")
proj5 = build_projection_tts(5)

nae_total_hits = 0
for i, (clauses, mode, sols) in enumerate(all_instances['NAE-3-SAT']):
    n_sols = len(sols)
    # Sample 200k truth tables
    hits = []
    for _ in range(200000):
        tt = random.getrandbits(32)
        # Quick check with 5000 random tuples
        sol_set = set(sols)
        n_bits = len(sols[0])
        passed = True
        for _ in range(min(3000, n_sols ** 5)):
            tup = tuple(random.randint(0, n_sols - 1) for _ in range(5))
            patterns = []
            for b in range(n_bits):
                pat_idx = 0
                for j in range(5):
                    pat_idx = 2 * pat_idx + sols[tup[j]][b]
                patterns.append(pat_idx)
            output = tuple((tt >> patterns[b]) & 1 for b in range(n_bits))
            if output not in sol_set:
                passed = False
                break
        if passed:
            hits.append(tt)

    if hits:
        print(f"  Instance {i}: |Sol|={n_sols}, {len(hits)} candidate hits from 200k samples")
        # Verify each hit exhaustively
        for tt in hits:
            is_proj = tt in proj5
            # Full verification
            genuine = check_tt_preserves_ALL_tuples(tt, sols, 5)
            print(f"    tt={tt:#010x}, projection={is_proj}, "
                  f"exhaustive_check={'GENUINE' if genuine else 'FALSE POSITIVE'}")
            if genuine and not is_proj:
                nae_total_hits += 1
    if (i + 1) % 5 == 0:
        print(f"  ... checked {i+1}/20")

print(f"\nNAE-3-SAT genuine non-projection hits: {nae_total_hits}")

# =========================================================================
# DIAGNOSTIC 2: Horn and XOR-SAT -- are they truly zero at k=5?
# =========================================================================
print("\n" + "=" * 60)
print("DIAGNOSTIC 2: Horn k=4 polymorphisms (expected to be small)")
print("=" * 60)

# For Horn, check k=4 exhaustive with FULL tuple coverage
# |Sol|^4 can be large; with |Sol| ~ 29, that's 29^4 = 707K tuples
for i, (clauses, mode, sols) in enumerate(all_instances['Horn'][:3]):
    n_sols = len(sols)
    print(f"  Horn instance {i}: |Sol|={n_sols}")
    # k=4 exhaustive
    tt_size = 16
    n_possible = 65536
    sol_set = set(sols)
    n_bits = len(sols[0])

    # Check ALL tuples (n_sols^4)
    total_tuples = n_sols ** 4
    print(f"    Total 4-tuples: {total_tuples}")

    allowed = set(range(n_possible))
    count = 0
    for tup in itertools.product(range(n_sols), repeat=4):
        if not allowed:
            break
        patterns = []
        for b in range(n_bits):
            pat_idx = 0
            for j in range(4):
                pat_idx = 2 * pat_idx + sols[tup[j]][b]
            patterns.append(pat_idx)
        new_allowed = set()
        for tt in allowed:
            output = tuple((tt >> patterns[b]) & 1 for b in range(n_bits))
            if output in sol_set:
                new_allowed.add(tt)
        allowed = new_allowed
        count += 1
        if count % 100000 == 0:
            print(f"    ... {count}/{total_tuples} tuples, {len(allowed)} surviving TTs")

    proj4 = build_projection_tts(4)
    n_proj = len(allowed & proj4)
    print(f"    Final: {len(allowed)} preserving TTs, {len(allowed) - n_proj} non-projections")

print("\n" + "=" * 60)
print("DIAGNOSTIC 3: XOR-SAT structure check")
print("=" * 60)

# XOR-SAT solutions form an affine subspace of F_2^n
# The only polymorphisms of an affine subspace are affine functions
# At k=5, the affine polymorphisms are: XOR-based operations
for i, (clauses, mode, sols) in enumerate(all_instances['XOR-SAT'][:3]):
    n_sols = len(sols)
    print(f"  XOR-SAT instance {i}: |Sol|={n_sols}")

    # Check k=3 and k=4 exhaustively with full tuples
    for k in [3, 4]:
        tt_size_k = 1 << k
        n_possible_k = 1 << tt_size_k
        sol_set = set(sols)
        n_bits = len(sols[0])

        if n_sols ** k <= 200000:
            all_tuples = list(itertools.product(range(n_sols), repeat=k))
        else:
            # Sample
            all_tuples = [tuple(random.randint(0, n_sols - 1) for _ in range(k)) for _ in range(200000)]

        allowed = set(range(n_possible_k))
        for tup in all_tuples:
            if not allowed:
                break
            patterns = []
            for b in range(n_bits):
                pat_idx = 0
                for j in range(k):
                    pat_idx = 2 * pat_idx + sols[tup[j]][b]
                patterns.append(pat_idx)
            new_allowed = set()
            for tt in allowed:
                output = tuple((tt >> patterns[b]) & 1 for b in range(n_bits))
                if output in sol_set:
                    new_allowed.add(tt)
            allowed = new_allowed

        proj_k = build_projection_tts(k)
        n_proj = len(allowed & proj_k)
        print(f"    k={k}: {len(allowed)} preserving ({len(allowed) - n_proj} non-proj)")

        # List the non-projections
        if len(allowed) - n_proj > 0 and len(allowed) - n_proj <= 20:
            for tt in sorted(allowed - proj_k):
                print(f"      tt={tt:#0{tt_size_k // 4 + 2}x} = {bin(tt)}")
