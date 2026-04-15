#!/usr/bin/env python3
"""
pvnp_sv_thickness_k4.py
=======================
Test the revised Path B mechanism for P vs NPC separation.

"Thickness" of the non-projection polymorphism family, measured by the
singular-value spectrum tail weight, should cleanly separate P from NPC
and scale with n.

Part 1: SV spectrum at k=3 AND k=4 for n=6
Part 2: Scaling with n at fixed k=3

Pattern 4 (topological rigidity) predicts the SV spectrum shape is a
discrete invariant that locks in the P/NPC classification.
"""

import random
import itertools
import numpy as np
from collections import defaultdict

random.seed(42)
np.random.seed(42)

# ─────────────────────────────────────────────────────────────────
#  SAT instance generation
# ─────────────────────────────────────────────────────────────────

def random_ksat_instance(n, k, alpha):
    """Generate a random k-SAT instance with m = alpha * n clauses."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        variables = random.sample(range(n), k)
        signs = [random.choice([True, False]) for _ in range(k)]
        clauses.append(list(zip(variables, signs)))
    return clauses


def evaluate_clause(clause, assignment):
    """Check if a clause is satisfied by the assignment."""
    for var, positive in clause:
        if positive and assignment[var]:
            return True
        if not positive and not assignment[var]:
            return True
    return False


def find_all_solutions(clauses, n):
    """Brute-force enumerate all satisfying assignments."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause(c, assignment) for c in clauses):
            solutions.append(assignment)
    return solutions


# ─────────────────────────────────────────────────────────────────
#  Polymorphism testing
# ─────────────────────────────────────────────────────────────────

def is_polymorphism(f_table, k, solutions):
    """
    Check if a k-ary boolean function f is a polymorphism of the
    solution set.  f is a polymorphism iff for every k-tuple of
    solutions (s1,...,sk), applying f coordinate-wise yields another
    solution.
    """
    if len(solutions) == 0:
        return True
    n = len(solutions[0])
    # For efficiency: precompute the set of solutions
    sol_set = set(solutions)

    for combo in itertools.product(range(len(solutions)), repeat=k):
        # apply f coordinate-wise
        result = []
        for j in range(n):
            args = tuple(solutions[combo[i]][j] for i in range(k))
            idx = 0
            for bit in args:
                idx = (idx << 1) | bit
            result.append(f_table[idx])
        if tuple(result) not in sol_set:
            return False
    return True


def is_projection(f_table, k):
    """Check if f is a projection (dictator) function."""
    for proj_idx in range(k):
        match = True
        for inp in range(2**k):
            bits = []
            for i in range(k):
                bits.append((inp >> (k - 1 - i)) & 1)
            if f_table[inp] != bits[proj_idx]:
                match = False
                break
        if match:
            return True
    return False


def enumerate_polymorphisms(k, solutions):
    """
    Enumerate all k-ary boolean polymorphisms.
    Returns (projections, non_projections) as lists of function tables.
    """
    projections = []
    non_projections = []
    for bits in range(2**(2**k)):
        f_table = []
        for j in range(2**k):
            f_table.append((bits >> j) & 1)
        if is_polymorphism(f_table, k, solutions):
            if is_projection(f_table, k):
                projections.append(f_table)
            else:
                non_projections.append(f_table)
    return projections, non_projections


# ─────────────────────────────────────────────────────────────────
#  Operator matrix and SV spectrum
# ─────────────────────────────────────────────────────────────────

def build_operator_matrix_k3(f_table, solutions):
    """
    Build the averaged operator matrix T_f for a ternary polymorphism:
      T_f = (1/|Sol|^2) sum_{b,c in Sol} sum_a |f(a,b,c)><a|
    T_f is a 2^n x 2^n matrix.
    """
    if len(solutions) == 0:
        return None
    n = len(solutions[0])
    dim = 2**n
    T = np.zeros((dim, dim))

    for b in solutions:
        for c in solutions:
            for a_bits in range(dim):
                a = tuple((a_bits >> i) & 1 for i in range(n))
                # compute f(a,b,c) coordinate-wise
                result = []
                for j in range(n):
                    args = (a[j], b[j], c[j])
                    idx = (args[0] << 2) | (args[1] << 1) | args[2]
                    result.append(f_table[idx])
                result_idx = 0
                for j in range(n):
                    result_idx |= (result[j] << j)
                T[result_idx, a_bits] += 1.0

    T /= len(solutions)**2
    return T


def build_operator_matrix_k4(f_table, solutions):
    """
    Build the averaged operator matrix T_f for a quaternary polymorphism:
      T_f = (1/|Sol|^3) sum_{b,c,d in Sol} sum_a |f(a,b,c,d)><a|
    """
    if len(solutions) == 0:
        return None
    n = len(solutions[0])
    dim = 2**n
    T = np.zeros((dim, dim))

    for b in solutions:
        for c in solutions:
            for d in solutions:
                for a_bits in range(dim):
                    a = tuple((a_bits >> i) & 1 for i in range(n))
                    result = []
                    for j in range(n):
                        args = (a[j], b[j], c[j], d[j])
                        idx = (args[0] << 3) | (args[1] << 2) | (args[2] << 1) | args[3]
                        result.append(f_table[idx])
                    result_idx = 0
                    for j in range(n):
                        result_idx |= (result[j] << j)
                    T[result_idx, a_bits] += 1.0

    T /= len(solutions)**3
    return T


def sv_spectrum_analysis(non_proj_polys, solutions, k):
    """
    For a list of non-projection polymorphisms, build operator matrices,
    stack them as columns, compute SVD, and report metrics.
    """
    if len(solutions) == 0 or len(non_proj_polys) == 0:
        return {
            'num_non_proj': 0,
            'operator_rank': 0,
            'top_svs': [],
            'tail_weight': 0.0,
            'total_sv_sum': 0.0,
        }

    n = len(solutions[0])
    dim = 2**n

    # Build operator matrices and vectorize
    columns = []
    builder = build_operator_matrix_k3 if k == 3 else build_operator_matrix_k4

    for f_table in non_proj_polys:
        T = builder(f_table, solutions)
        columns.append(T.flatten())

    M = np.column_stack(columns)
    U, S, Vh = np.linalg.svd(M, full_matrices=False)

    # Tail weight: sum of SVs beyond rank 3 / total
    total = np.sum(S)
    if total < 1e-15:
        tail_weight = 0.0
    else:
        head = np.sum(S[:3]) if len(S) >= 3 else np.sum(S)
        tail_weight = (total - head) / total

    rank = np.sum(S > 1e-10)

    return {
        'num_non_proj': len(non_proj_polys),
        'operator_rank': int(rank),
        'top_svs': S[:min(10, len(S))].tolist(),
        'tail_weight': float(tail_weight),
        'total_sv_sum': float(total),
    }


# ─────────────────────────────────────────────────────────────────
#  Main experiment driver
# ─────────────────────────────────────────────────────────────────

def run_experiment(n, k, sat_type, alpha, num_instances=20):
    """Run the full experiment for given parameters."""
    results = []
    for inst in range(num_instances):
        ksat = 2 if sat_type == '2-SAT' else 3
        clauses = random_ksat_instance(n, ksat, alpha)
        solutions = find_all_solutions(clauses, n)

        if len(solutions) == 0:
            results.append(None)
            continue

        projs, non_projs = enumerate_polymorphisms(k, solutions)

        # Limit non-projections for k=4 if too many (memory)
        max_polys = 200
        if len(non_projs) > max_polys:
            non_projs_sample = random.sample(non_projs, max_polys)
        else:
            non_projs_sample = non_projs

        analysis = sv_spectrum_analysis(non_projs_sample, solutions, k)
        analysis['num_solutions'] = len(solutions)
        analysis['num_projections'] = len(projs)
        analysis['total_non_proj'] = len(non_projs)
        results.append(analysis)

    return results


def summarize_results(results, label):
    """Print summary statistics for a batch of results."""
    valid = [r for r in results if r is not None and r['num_non_proj'] > 0]
    if not valid:
        print(f"  {label}: No valid instances with non-projection polymorphisms")
        return None

    avg_non_proj = np.mean([r['total_non_proj'] for r in valid])
    avg_proj = np.mean([r['num_projections'] for r in valid])
    avg_solutions = np.mean([r['num_solutions'] for r in valid])
    avg_rank = np.mean([r['operator_rank'] for r in valid])
    avg_tail = np.mean([r['tail_weight'] for r in valid])
    std_tail = np.std([r['tail_weight'] for r in valid])
    avg_total_sv = np.mean([r['total_sv_sum'] for r in valid])

    # Collect top SVs (padded)
    max_len = 10
    all_svs = []
    for r in valid:
        svs = r['top_svs'][:max_len]
        svs += [0.0] * (max_len - len(svs))
        all_svs.append(svs)
    avg_svs = np.mean(all_svs, axis=0)

    print(f"  {label}:")
    print(f"    Valid instances:           {len(valid)}/{len(results)}")
    print(f"    Avg solutions:             {avg_solutions:.1f}")
    print(f"    Avg projections:           {avg_proj:.1f}")
    print(f"    Avg non-proj polymorphisms:{avg_non_proj:.1f}")
    print(f"    Avg operator rank:         {avg_rank:.1f}")
    print(f"    Avg total SV sum:          {avg_total_sv:.4f}")
    print(f"    Avg top 10 SVs:            {np.array2string(avg_svs, precision=4, separator=', ')}")
    print(f"    Avg tail weight:           {avg_tail:.6f} +/- {std_tail:.6f}")

    return {
        'avg_tail': avg_tail,
        'std_tail': std_tail,
        'avg_non_proj': avg_non_proj,
        'avg_rank': avg_rank,
        'n_valid': len(valid),
    }


# ═══════════════════════════════════════════════════════════════════
#  PART 1: k=3 and k=4 at n=6
# ═══════════════════════════════════════════════════════════════════

print("=" * 72)
print("PART 1: SV SPECTRUM AT k=3 AND k=4 FOR n=6")
print("=" * 72)

n = 6
num_instances = 20

for k in [3, 4]:
    print(f"\n{'─' * 72}")
    print(f"Arity k={k}  (enumerating {2**(2**k)} functions)")
    print(f"{'─' * 72}")

    if k == 4:
        # k=4 is expensive -- reduce instances for feasibility
        ni = 10
        print(f"  (Reduced to {ni} instances for k=4 feasibility)")
    else:
        ni = num_instances

    print(f"\n  2-SAT (alpha=1.5, n={n}):")
    res_2sat = run_experiment(n, k, '2-SAT', 1.5, ni)
    s2 = summarize_results(res_2sat, '2-SAT')

    print(f"\n  3-SAT (alpha=3.5, n={n}):")
    res_3sat = run_experiment(n, k, '3-SAT', 3.5, ni)
    s3 = summarize_results(res_3sat, '3-SAT')

    if s2 and s3:
        print(f"\n  ── KEY METRICS (k={k}) ──")
        ratio_tail = s2['avg_tail'] / s3['avg_tail'] if s3['avg_tail'] > 1e-15 else float('inf')
        ratio_count = s2['avg_non_proj'] / s3['avg_non_proj'] if s3['avg_non_proj'] > 1e-15 else float('inf')
        print(f"    Tail weight ratio (P/NPC):      {ratio_tail:.4f}")
        print(f"    Non-proj count ratio (P/NPC):   {ratio_count:.4f}")

        # Clean separation test
        tails_2sat = [r['tail_weight'] for r in res_2sat if r is not None and r['num_non_proj'] > 0]
        tails_3sat = [r['tail_weight'] for r in res_3sat if r is not None and r['num_non_proj'] > 0]
        if tails_2sat and tails_3sat:
            min_2sat = min(tails_2sat)
            max_3sat = max(tails_3sat)
            if min_2sat > max_3sat:
                threshold = (min_2sat + max_3sat) / 2
                print(f"    CLEAN SEPARATION: Yes!  Threshold T = {threshold:.6f}")
                print(f"      min(tail_P) = {min_2sat:.6f} > max(tail_NPC) = {max_3sat:.6f}")
            else:
                overlap_frac = np.mean([t >= min(tails_2sat) for t in tails_3sat])
                print(f"    CLEAN SEPARATION: No (overlap exists)")
                print(f"      min(tail_P) = {min_2sat:.6f}, max(tail_NPC) = {max_3sat:.6f}")
                print(f"      But avg_tail_P = {s2['avg_tail']:.6f} vs avg_tail_NPC = {s3['avg_tail']:.6f}")
    else:
        print(f"\n  (Insufficient data for key metrics at k={k})")


# ═══════════════════════════════════════════════════════════════════
#  PART 2: Scaling with n at fixed k=3
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("PART 2: SCALING WITH n AT FIXED k=3")
print("=" * 72)

scaling_data = {'2-SAT': {}, '3-SAT': {}}

for n_val in [6, 8, 10]:
    print(f"\n{'─' * 72}")
    print(f"n = {n_val}, k = 3")
    print(f"{'─' * 72}")

    # Adjust instances for larger n (feasibility)
    ni = 20 if n_val <= 8 else 10

    print(f"\n  2-SAT (alpha=1.5):")
    res_2sat = run_experiment(n_val, 3, '2-SAT', 1.5, ni)
    s2 = summarize_results(res_2sat, '2-SAT')

    print(f"\n  3-SAT (alpha=3.5):")
    res_3sat = run_experiment(n_val, 3, '3-SAT', 3.5, ni)
    s3 = summarize_results(res_3sat, '3-SAT')

    if s2:
        scaling_data['2-SAT'][n_val] = s2
    if s3:
        scaling_data['3-SAT'][n_val] = s3


# ═══════════════════════════════════════════════════════════════════
#  SCALING ANALYSIS
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("SCALING ANALYSIS")
print("=" * 72)

print("\nTail weight vs n:")
print(f"  {'n':>4s}  {'2-SAT tail':>14s}  {'3-SAT tail':>14s}  {'Ratio P/NPC':>14s}")
print(f"  {'─'*4}  {'─'*14}  {'─'*14}  {'─'*14}")

for n_val in [6, 8, 10]:
    tw2 = scaling_data['2-SAT'].get(n_val, {}).get('avg_tail', None)
    tw3 = scaling_data['3-SAT'].get(n_val, {}).get('avg_tail', None)
    s2 = f"{tw2:.6f}" if tw2 is not None else "N/A"
    s3 = f"{tw3:.6f}" if tw3 is not None else "N/A"
    if tw2 is not None and tw3 is not None and tw3 > 1e-15:
        ratio = tw2 / tw3
        sr = f"{ratio:.4f}"
    else:
        sr = "N/A"
    print(f"  {n_val:>4d}  {s2:>14s}  {s3:>14s}  {sr:>14s}")

print("\nNon-projection count vs n:")
print(f"  {'n':>4s}  {'2-SAT count':>14s}  {'3-SAT count':>14s}  {'Ratio P/NPC':>14s}")
print(f"  {'─'*4}  {'─'*14}  {'─'*14}  {'─'*14}")

for n_val in [6, 8, 10]:
    c2 = scaling_data['2-SAT'].get(n_val, {}).get('avg_non_proj', None)
    c3 = scaling_data['3-SAT'].get(n_val, {}).get('avg_non_proj', None)
    s2 = f"{c2:.1f}" if c2 is not None else "N/A"
    s3 = f"{c3:.1f}" if c3 is not None else "N/A"
    if c2 is not None and c3 is not None and c3 > 0:
        ratio = c2 / c3
        sr = f"{ratio:.4f}"
    else:
        sr = "N/A"
    print(f"  {n_val:>4d}  {s2:>14s}  {s3:>14s}  {sr:>14s}")


# Trend analysis
print("\nTrend analysis:")
for label in ['2-SAT', '3-SAT']:
    ns = sorted(scaling_data[label].keys())
    if len(ns) >= 2:
        tails = [scaling_data[label][n_val]['avg_tail'] for n_val in ns]
        diffs = [tails[i+1] - tails[i] for i in range(len(tails)-1)]
        trend = "INCREASING" if all(d > 0 for d in diffs) else (
                "DECREASING" if all(d < 0 for d in diffs) else "MIXED")
        print(f"  {label}: tail weights = {[f'{t:.6f}' for t in tails]} -> {trend}")


# ═══════════════════════════════════════════════════════════════════
#  PATTERN 4 VERDICT
# ═══════════════════════════════════════════════════════════════════

print("\n\n" + "=" * 72)
print("PATTERN 4 (TOPOLOGICAL RIGIDITY) VERDICT")
print("=" * 72)

# Check if there's clean separation at the largest n tested
all_tails_p = []
all_tails_npc = []
for n_val in scaling_data['2-SAT']:
    all_tails_p.append(scaling_data['2-SAT'][n_val]['avg_tail'])
for n_val in scaling_data['3-SAT']:
    all_tails_npc.append(scaling_data['3-SAT'][n_val]['avg_tail'])

if all_tails_p and all_tails_npc:
    avg_p = np.mean(all_tails_p)
    avg_npc = np.mean(all_tails_npc)
    print(f"\n  Overall avg tail weight  P:   {avg_p:.6f}")
    print(f"  Overall avg tail weight NPC:  {avg_npc:.6f}")

    if avg_p > avg_npc:
        print(f"\n  Direction: P has THICKER SV tail than NPC (ratio = {avg_p/avg_npc:.4f})")
        print("  Interpretation: P-time problems have richer non-projection polymorphism")
        print("  families, with SV mass spread into the tail -- consistent with the")
        print("  algebraic diversity that the Bulatov-Zhuk dichotomy predicts.")
    else:
        print(f"\n  Direction: NPC has thicker tail (ratio = {avg_npc/avg_p:.4f})")
        print("  This is the OPPOSITE of the naive expectation.")
        print("  Interpretation: needs revisiting the mechanism.")

    # Check if the ratio is growing with n
    ns_common = sorted(set(scaling_data['2-SAT'].keys()) & set(scaling_data['3-SAT'].keys()))
    if len(ns_common) >= 2:
        ratios = []
        for n_val in ns_common:
            t2 = scaling_data['2-SAT'][n_val]['avg_tail']
            t3 = scaling_data['3-SAT'][n_val]['avg_tail']
            r = t2 / t3 if t3 > 1e-15 else float('inf')
            ratios.append(r)
        print(f"\n  Tail-weight ratios at n = {ns_common}: {[f'{r:.4f}' for r in ratios]}")
        if all(ratios[i+1] > ratios[i] for i in range(len(ratios)-1)):
            print("  Ratio is GROWING with n -- supports the conjecture!")
        elif all(ratios[i+1] < ratios[i] for i in range(len(ratios)-1)):
            print("  Ratio is SHRINKING with n -- does NOT support the conjecture.")
        else:
            print("  Ratio trend is non-monotonic.")

print("\nDone.")
