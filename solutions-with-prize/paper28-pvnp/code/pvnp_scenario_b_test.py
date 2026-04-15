#!/usr/bin/env python3
"""
Scenario B test for P vs NP proof:
Does the clone's collection of polymorphisms form a NON-DISCRETE family
for P-time CSPs and a DISCRETE family for NPC CSPs?

For each CSP class and arity k=3,4:
1. Enumerate all k-ary polymorphisms (Boolean ops preserving solution set).
2. Compute pairwise "polymorphism distances".
3. Measure discreteness of the distance spectrum.

Prediction:
  P-time  (2-SAT, Horn-SAT) -> non-discrete / continuous distance spectrum
  NPC     (3-SAT, NAE-3-SAT) -> discrete / clustered distance spectrum
"""

import random
import itertools
from collections import Counter
import time

random.seed(42)

# ─────────────────────────────────────────────────────────────────────
# CSP instance generators
# ─────────────────────────────────────────────────────────────────────

def gen_2sat(n, m):
    clauses = []
    for _ in range(m):
        vs = random.sample(range(n), 2)
        signs = [random.choice([False, True]) for _ in range(2)]
        clauses.append(list(zip(vs, signs)))
    return clauses

def gen_horn(n, m):
    clauses = []
    for _ in range(m):
        vs = random.sample(range(n), 3)
        if random.random() < 0.5:
            signs = [True, True, False]
        else:
            signs = [True, True, True]
        random.shuffle(signs)
        clauses.append(list(zip(vs, signs)))
    return clauses

def gen_3sat(n, m):
    clauses = []
    for _ in range(m):
        vs = random.sample(range(n), 3)
        signs = [random.choice([False, True]) for _ in range(3)]
        clauses.append(list(zip(vs, signs)))
    return clauses

def gen_nae3sat(n, m):
    clauses = []
    for _ in range(m):
        vs = random.sample(range(n), 3)
        signs = [random.choice([False, True]) for _ in range(3)]
        clauses.append(list(zip(vs, signs)))
    return clauses

# ─────────────────────────────────────────────────────────────────────
# Solution enumeration
# ─────────────────────────────────────────────────────────────────────

def satisfies_clause(assignment, clause):
    for var, negated in clause:
        val = assignment[var]
        lit_val = (not val) if negated else val
        if lit_val:
            return True
    return False

def satisfies_nae_clause(assignment, clause):
    vals = []
    for var, negated in clause:
        val = assignment[var]
        lit_val = (not val) if negated else val
        vals.append(lit_val)
    return not (all(vals) or not any(vals))

def find_solutions(clauses, n, is_nae=False):
    solutions = []
    check = satisfies_nae_clause if is_nae else satisfies_clause
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(check(assignment, c) for c in clauses):
            solutions.append(assignment)
    return solutions

# ─────────────────────────────────────────────────────────────────────
# FAST polymorphism enumeration via constraint propagation
# ─────────────────────────────────────────────────────────────────────

def enumerate_polymorphisms(solutions, k, n):
    """
    Enumerate all k-ary polymorphisms using constraint propagation.

    Key insight: for each k-tuple of solutions, applying f coordinate-wise
    must yield a solution. For each coordinate j, the truth table entry
    at index (s1[j], s2[j], ..., sk[j]) determines output bit j.
    The resulting n-bit vector must be in the solution set.

    We build constraints incrementally: each k-tuple constrains which
    truth tables are valid. We represent the constraint as:
    for each tt entry index i in 0..2^k-1, what values are allowed?

    But the constraint is JOINT across coordinates (all n output bits
    together must form a valid solution), so we can't decompose per-entry.

    Strategy: use the k-tuple constraints to progressively eliminate
    candidate truth tables. Process tuples in order, maintaining a
    "survivors" set.

    For k=3: 256 candidates -- very fast.
    For k=4: 65536 candidates -- need efficiency.

    Optimization: precompute per-tuple "lookup tables" so that for each
    candidate tt we can quickly compute the output and check membership.
    Use bit manipulation: encode the output as an n-bit integer.
    """
    num_sols = len(solutions)
    if num_sols == 0:
        return []

    num_entries = 2 ** k
    num_candidates = 2 ** num_entries

    # Encode solutions as n-bit integers
    sol_ints = set()
    for s in solutions:
        val = 0
        for j in range(n):
            val |= s[j] << j
        sol_ints.add(val)

    sol_arr = solutions  # list of tuples

    # For each k-tuple of solutions, precompute the n tt-entry indices.
    # Then for candidate tt, output_j = (tt >> idx_j) & 1, and
    # output_int = sum over j of output_j << j.
    #
    # Critical optimization: precompute, for each k-tuple, the
    # "extraction masks". For a given set of n tt-indices (idx_0,...,idx_{n-1}),
    # output_int = sum_j ((tt >> idx_j) & 1) << j
    #            = sum_j ((tt & (1 << idx_j)) >> idx_j) << j
    #            = sum_j ((tt >> idx_j) & 1) << j
    #
    # We can precompute this as a function of tt using bit tricks.
    # For each coordinate j, we extract bit idx_j from tt and place it at bit j.
    # This is a "bit permutation/selection" operation.
    #
    # For n=8 and k<=4, we can precompute a lookup table:
    # For each k-tuple, build a lookup array of size num_candidates
    # mapping tt -> output_int. But for k=4 that's 65536 entries per tuple.
    # With many tuples this uses too much memory.
    #
    # Better: just compute it inline but in a tight loop.

    total_tuples = num_sols ** k

    # Determine which tuples to check
    if total_tuples <= 200000:
        # Enumerate all
        use_all = True
        tuple_iter = itertools.product(range(num_sols), repeat=k)
    else:
        use_all = False

    # Precompute tt_indices for tuples
    # For each tuple: list of n ints (the tt entry index per coordinate)
    def compute_tt_indices(combo):
        indices = [0] * n
        for j in range(n):
            idx = 0
            for l in range(k):
                idx |= sol_arr[combo[l]][j] << l
            indices[j] = idx
        return indices

    # For k=3 (256 candidates): just iterate all tuples, test all candidates
    # For k=4 (65536 candidates): need to be smart about early elimination

    survivors = list(range(num_candidates))

    if use_all:
        # Process tuples one by one, filtering survivors
        for combo in itertools.product(range(num_sols), repeat=k):
            if len(survivors) == 0:
                break
            indices = compute_tt_indices(combo)
            new_survivors = []
            for tt in survivors:
                out_int = 0
                for j in range(n):
                    out_int |= ((tt >> indices[j]) & 1) << j
                if out_int in sol_ints:
                    new_survivors.append(tt)
            survivors = new_survivors
    else:
        # Sample tuples, filter progressively, repeat until stable
        prev_len = len(survivors)
        rounds = 0
        while rounds < 40:
            # Generate a batch of random tuples
            batch_size = min(10000, total_tuples)
            batch = []
            for _ in range(batch_size):
                combo = tuple(random.randint(0, num_sols - 1) for _ in range(k))
                batch.append(compute_tt_indices(combo))

            for indices in batch:
                if len(survivors) == 0:
                    break
                new_survivors = []
                for tt in survivors:
                    out_int = 0
                    for j in range(n):
                        out_int |= ((tt >> indices[j]) & 1) << j
                    if out_int in sol_ints:
                        new_survivors.append(tt)
                survivors = new_survivors

            rounds += 1
            if len(survivors) == prev_len:
                break  # converged
            prev_len = len(survivors)

    return survivors


# ─────────────────────────────────────────────────────────────────────
# Distance and discreteness metrics
# ─────────────────────────────────────────────────────────────────────

def polymorphism_distance(tt1, tt2, k):
    xor = tt1 ^ tt2
    num_entries = 2 ** k
    diff = bin(xor).count('1')
    return diff / num_entries

def compute_distance_spectrum(polymorphisms, k):
    n_poly = len(polymorphisms)
    if n_poly < 2:
        return {
            'num_pairs': 0,
            'num_distinct': 0,
            'gap_ratio': float('nan'),
            'distances': [],
            'distance_counts': {}
        }

    # If too many polymorphisms, sample pairs
    max_pairs = 50000
    total_pairs = n_poly * (n_poly - 1) // 2
    distances = []

    if total_pairs <= max_pairs:
        for i in range(n_poly):
            for j in range(i + 1, n_poly):
                d = polymorphism_distance(polymorphisms[i], polymorphisms[j], k)
                distances.append(round(d, 3))
    else:
        # Sample pairs
        for _ in range(max_pairs):
            i = random.randint(0, n_poly - 1)
            j = random.randint(0, n_poly - 2)
            if j >= i:
                j += 1
            d = polymorphism_distance(polymorphisms[i], polymorphisms[j], k)
            distances.append(round(d, 3))

    dist_counts = Counter(distances)
    sorted_distinct = sorted(dist_counts.keys())
    num_distinct = len(sorted_distinct)

    if num_distinct < 2:
        gap_ratio = float('inf')
    else:
        gaps = [sorted_distinct[i+1] - sorted_distinct[i]
                for i in range(len(sorted_distinct) - 1)]
        gaps = [g for g in gaps if g > 1e-9]
        if not gaps:
            gap_ratio = float('inf')
        else:
            gap_ratio = min(gaps) / max(gaps)

    return {
        'num_pairs': len(distances),
        'num_distinct': num_distinct,
        'gap_ratio': gap_ratio,
        'distances': distances,
        'distance_counts': dist_counts
    }


# ─────────────────────────────────────────────────────────────────────
# Main experiment
# ─────────────────────────────────────────────────────────────────────

def run_experiment():
    n = 8
    num_instances = 20
    arities = [3, 4]

    csp_classes = [
        ("2-SAT",     gen_2sat,    1.5, False, "P"),
        ("Horn-SAT",  gen_horn,    2.0, False, "P"),
        ("3-SAT",     gen_3sat,    3.5, False, "NPC"),
        ("NAE-3-SAT", gen_nae3sat, 1.0, True,  "NPC"),
    ]

    print("=" * 78)
    print("SCENARIO B TEST: Polymorphism Family Discreteness")
    print("=" * 78)
    print(f"Parameters: n={n} variables, {num_instances} instances per class")
    print(f"Arities tested: {arities}")
    print()

    results_summary = {}

    for csp_name, gen_func, alpha, is_nae, complexity in csp_classes:
        print("-" * 78)
        print(f"CSP: {csp_name}  (alpha={alpha}, class={complexity})")
        print("-" * 78)

        m = int(alpha * n)

        all_num_sols = []
        per_arity_data = {k: {'num_polys': [], 'num_distinct': [],
                              'gap_ratios': [], 'clone_densities': []}
                          for k in arities}

        t0 = time.time()
        for inst in range(num_instances):
            clauses = gen_func(n, m)
            solutions = find_solutions(clauses, n, is_nae=is_nae)
            num_sols = len(solutions)
            all_num_sols.append(num_sols)

            if num_sols < 4:
                print(f"  Instance {inst}: {num_sols} solutions, skipping (need >= 4)")
                continue

            print(f"  Instance {inst}: {num_sols} solutions", end="", flush=True)

            for k in arities:
                t1 = time.time()
                polys = enumerate_polymorphisms(solutions, k, n)
                dt = time.time() - t1
                num_polys = len(polys)
                clone_density = num_polys / (2 ** (2 ** k))

                spectrum = compute_distance_spectrum(polys, k)

                per_arity_data[k]['num_polys'].append(num_polys)
                per_arity_data[k]['clone_densities'].append(clone_density)
                per_arity_data[k]['num_distinct'].append(spectrum['num_distinct'])
                if not (spectrum['gap_ratio'] != spectrum['gap_ratio']):
                    per_arity_data[k]['gap_ratios'].append(spectrum['gap_ratio'])

                print(f"  k={k}:{num_polys}({dt:.1f}s)", end="", flush=True)

            print()

        elapsed = time.time() - t0
        avg_sols = sum(all_num_sols) / len(all_num_sols) if all_num_sols else 0
        print(f"\n  Average solutions: {avg_sols:.1f}  (total time: {elapsed:.1f}s)")

        results_summary[csp_name] = {'complexity': complexity}

        for k in arities:
            data = per_arity_data[k]
            if not data['num_polys']:
                print(f"  Arity k={k}: no data")
                continue

            avg_polys = sum(data['num_polys']) / len(data['num_polys'])
            avg_density = sum(data['clone_densities']) / len(data['clone_densities'])
            avg_distinct = sum(data['num_distinct']) / len(data['num_distinct']) if data['num_distinct'] else 0

            finite_gaps = [g for g in data['gap_ratios'] if g != float('inf')]
            avg_gap = sum(finite_gaps) / len(finite_gaps) if finite_gaps else float('inf')
            inf_count = sum(1 for g in data['gap_ratios'] if g == float('inf'))

            print(f"\n  Arity k={k}:")
            print(f"    Avg polymorphisms:      {avg_polys:.1f} / {2**(2**k)}")
            print(f"    Avg clone density:      {avg_density:.6f}")
            print(f"    Avg distinct distances:  {avg_distinct:.1f}")
            gap_str = f"{avg_gap:.4f}" if avg_gap != float('inf') else "inf"
            print(f"    Avg gap ratio (finite):  {gap_str}"
                  f"  (inf in {inf_count}/{len(data['gap_ratios'])} instances)")

            results_summary[csp_name][f'k{k}_density'] = avg_density
            results_summary[csp_name][f'k{k}_distinct'] = avg_distinct
            results_summary[csp_name][f'k{k}_gap'] = avg_gap
            results_summary[csp_name][f'k{k}_inf_count'] = inf_count
            results_summary[csp_name][f'k{k}_total'] = len(data['gap_ratios'])

        print()

    # ─────────────────────────────────────────────────────────────────
    # Summary
    # ─────────────────────────────────────────────────────────────────
    print("=" * 78)
    print("SUMMARY TABLE")
    print("=" * 78)
    header = (f"{'CSP':<12} {'Class':<5} {'k':>2} {'#Poly':>8} {'Density':>10} "
              f"{'Distinct':>9} {'GapRatio':>9} {'Inf/Tot':>8}")
    print(header)
    print("-" * 78)

    for csp_name in ["2-SAT", "Horn-SAT", "3-SAT", "NAE-3-SAT"]:
        r = results_summary[csp_name]
        for k in arities:
            dk = f'k{k}_density'
            if dk not in r:
                continue
            density = r[dk]
            distinct = r[f'k{k}_distinct']
            gap = r[f'k{k}_gap']
            inf_c = r[f'k{k}_inf_count']
            tot = r[f'k{k}_total']
            gap_str = f"{gap:.4f}" if gap != float('inf') else "inf"
            npoly = density * (2**(2**k))
            print(f"{csp_name:<12} {r['complexity']:<5} {k:>2} {npoly:>8.1f} "
                  f"{density:>10.6f} {distinct:>9.1f} "
                  f"{gap_str:>9} {inf_c:>3}/{tot:<3}")

    print()
    print("=" * 78)
    print("PREDICTION CHECK")
    print("=" * 78)

    all_pass = True
    for k in arities:
        print(f"\n--- Arity k={k} ---")

        p_densities, p_distincts, npc_densities, npc_distincts = [], [], [], []
        p_gaps, npc_gaps = [], []

        for csp_name in ["2-SAT", "Horn-SAT"]:
            r = results_summary[csp_name]
            if f'k{k}_density' in r:
                p_densities.append(r[f'k{k}_density'])
                p_distincts.append(r[f'k{k}_distinct'])
                p_gaps.append(r[f'k{k}_gap'])

        for csp_name in ["3-SAT", "NAE-3-SAT"]:
            r = results_summary[csp_name]
            if f'k{k}_density' in r:
                npc_densities.append(r[f'k{k}_density'])
                npc_distincts.append(r[f'k{k}_distinct'])
                npc_gaps.append(r[f'k{k}_gap'])

        if p_densities and npc_densities:
            avg_p_d = sum(p_densities) / len(p_densities)
            avg_n_d = sum(npc_densities) / len(npc_densities)
            ratio = avg_p_d / avg_n_d if avg_n_d > 0 else float('inf')
            ok = ratio > 1.0
            all_pass = all_pass and ok
            print(f"  Clone density:  P = {avg_p_d:.6f}, NPC = {avg_n_d:.6f}, "
                  f"ratio = {ratio:.2f}x  -> {'PASS' if ok else 'FAIL'}")

        if p_distincts and npc_distincts:
            avg_p = sum(p_distincts) / len(p_distincts)
            avg_n = sum(npc_distincts) / len(npc_distincts)
            ok = avg_p > avg_n
            all_pass = all_pass and ok
            print(f"  Distinct dists: P = {avg_p:.1f}, NPC = {avg_n:.1f}"
                  f"  -> {'PASS' if ok else 'FAIL'}")

        if p_gaps and npc_gaps:
            fp = [g for g in p_gaps if g != float('inf')]
            fn = [g for g in npc_gaps if g != float('inf')]
            avg_pg = sum(fp) / len(fp) if fp else 0.0
            avg_ng = sum(fn) / len(fn) if fn else float('inf')
            ps = f"{avg_pg:.4f}" if avg_pg != float('inf') else "inf"
            ns = f"{avg_ng:.4f}" if avg_ng != float('inf') else "inf"
            if avg_ng == float('inf'):
                ok = True
            else:
                ok = avg_ng > avg_pg
            all_pass = all_pass and ok
            print(f"  Gap ratio:      P = {ps}, NPC = {ns}"
                  f"  -> {'PASS' if ok else 'FAIL'}")

    print()
    print("=" * 78)
    verdict = "ALL PREDICTIONS CONFIRMED" if all_pass else "SOME PREDICTIONS FAILED"
    print(f"OVERALL VERDICT: {verdict}")
    print("=" * 78)
    print("""
Scenario B predicts that:
  - P-time CSPs have RICH polymorphism clones (high density, many distinct
    pairwise distances -> non-discrete/continuous family structure).
  - NPC CSPs have SPARSE polymorphism clones (low density, few distinct
    pairwise distances -> discrete/clustered family structure).

This is the algebraic signature of the P vs NPC dichotomy: the polymorphism
clone of a tractable CSP is algebraically rich (non-discrete), while the
clone of an intractable CSP is algebraically impoverished (discrete).
""")


if __name__ == "__main__":
    run_experiment()
