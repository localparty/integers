#!/usr/bin/env python3
"""
pvnp_direct_out_test.py
=======================
Test the "one-step shortcut" hypothesis:
  Does exponential clone growth DIRECTLY imply non-discrete Out(M)?

Instead of constructing unitaries from individual polymorphisms and using
pigeonhole, we measure the "Out dimension" directly as the dimension of
the space spanned by all polymorphism-induced operators.

For each CSP class at n=6, arity k=3:
  1. Find all solutions Sol
  2. Enumerate all 256 ternary functions on {0,1}, find polymorphisms
  3. For each polymorphism f, construct operator T_f (averaged over anchors)
  4. Compute rank of matrix whose columns = vec(T_f)
  5. Analyze singular value spectrum

Prediction:
  P-time  -> operator rank grows with clone size (non-discrete Out)
  NPC     -> operator rank stays small (discrete Out)
"""

import numpy as np
from itertools import product
import time
import sys

np.set_printoptions(precision=4, linewidth=120)

# ──────────────────────────────────────────────────────────────────────
# CSP Generation
# ──────────────────────────────────────────────────────────────────────

def generate_random_2sat(n, alpha, rng):
    """Generate random 2-SAT instance (clauses are 2-literal disjunctions)."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = rng.choice(n, size=2, replace=False)
        signs = rng.choice([0, 1], size=2)
        clauses.append((vs, signs))
    return clauses, '2-SAT'

def generate_random_horn(n, alpha, rng):
    """Generate random Horn-SAT: each clause has at most one positive literal."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        k = 3
        vs = rng.choice(n, size=k, replace=False)
        # Horn: at most 1 positive literal
        signs = np.ones(k, dtype=int)  # all negated
        pos_idx = rng.choice(k + 1)  # k+1 means no positive literal
        if pos_idx < k:
            signs[pos_idx] = 0  # this one is positive (not negated)
        clauses.append((vs, signs))
    return clauses, 'Horn'

def generate_random_3sat(n, alpha, rng):
    """Generate random 3-SAT instance."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = rng.choice(n, size=3, replace=False)
        signs = rng.choice([0, 1], size=3)
        clauses.append((vs, signs))
    return clauses, '3-SAT'

def generate_random_nae3sat(n, alpha, rng):
    """Generate random NAE-3-SAT (not-all-equal)."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        vs = rng.choice(n, size=3, replace=False)
        signs = rng.choice([0, 1], size=3)
        clauses.append((vs, signs))
    return clauses, 'NAE-3-SAT'

# ──────────────────────────────────────────────────────────────────────
# Solution finding
# ──────────────────────────────────────────────────────────────────────

def find_all_solutions(clauses, n, csp_type):
    """Brute-force enumerate all satisfying assignments for n variables."""
    solutions = []
    for bits in product([0, 1], repeat=n):
        assignment = np.array(bits, dtype=int)
        sat = True
        for vs, signs in clauses:
            if csp_type == 'NAE-3-SAT':
                # NAE: not all literals have the same value
                lits = [(assignment[v] ^ s) for v, s in zip(vs, signs)]
                if len(set(lits)) == 1:
                    sat = False
                    break
            else:
                # Standard SAT: at least one literal true
                clause_sat = False
                for v, s in zip(vs, signs):
                    lit_val = assignment[v] ^ s
                    if lit_val == 1:
                        clause_sat = True
                        break
                if not clause_sat:
                    sat = False
                    break
        if sat:
            solutions.append(assignment)
    return solutions

# ──────────────────────────────────────────────────────────────────────
# Polymorphism enumeration (arity 3, domain {0,1})
# ──────────────────────────────────────────────────────────────────────

def enumerate_ternary_functions():
    """All 2^(2^3) = 256 ternary Boolean functions.
    Each function is a lookup table: f(a,b,c) for all (a,b,c) in {0,1}^3.
    """
    inputs = list(product([0, 1], repeat=3))  # 8 inputs
    functions = []
    for output_bits in product([0, 1], repeat=8):
        table = {}
        for inp, out in zip(inputs, output_bits):
            table[inp] = out
        functions.append(table)
    return functions, inputs

def is_polymorphism(func, solutions, n):
    """Check if ternary function f is a polymorphism of the relation defined by Sol.
    f is a polymorphism if for all a, b, c in Sol, f(a,b,c) is also in Sol
    (applied coordinate-wise).
    """
    sol_set = set(tuple(s) for s in solutions)
    # Check all triples of solutions
    for a in solutions:
        for b in solutions:
            for c in solutions:
                result = tuple(func[(a[i], b[i], c[i])] for i in range(n))
                if result not in sol_set:
                    return False
    return True

def find_polymorphisms(solutions, n):
    """Find all ternary polymorphisms preserving the solution set."""
    all_funcs, inputs = enumerate_ternary_functions()
    polys = []
    for func in all_funcs:
        if is_polymorphism(func, solutions, n):
            polys.append(func)
    return polys

# ──────────────────────────────────────────────────────────────────────
# Operator construction
# ──────────────────────────────────────────────────────────────────────

def construct_operator(func, solutions, n):
    """
    Construct T_f = (1/|Sol|^2) sum_{b,c in Sol} sum_{a in Sol} |f(a,b,c)><a|

    This is a |D|x|Sol| -> |D|x|Sol| operator where D = {0,1}^n.
    We work in the basis indexed by solutions.
    """
    num_sol = len(solutions)
    sol_list = [tuple(s) for s in solutions]
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    sol_set = set(sol_list)

    T = np.zeros((num_sol, num_sol), dtype=float)

    for b in solutions:
        for c in solutions:
            for a_idx, a in enumerate(solutions):
                result = tuple(func[(a[i], b[i], c[i])] for i in range(n))
                if result in sol_set:
                    r_idx = sol_to_idx[result]
                    T[r_idx, a_idx] += 1.0

    T /= (num_sol ** 2)
    return T

# ──────────────────────────────────────────────────────────────────────
# Main analysis
# ──────────────────────────────────────────────────────────────────────

def analyze_instance(clauses, csp_type, n, instance_id):
    """Full analysis for one CSP instance."""
    solutions = find_all_solutions(clauses, n, csp_type)
    num_sol = len(solutions)

    if num_sol < 2:
        return None  # Need at least 2 solutions for meaningful analysis

    # Find polymorphisms
    polys = find_polymorphisms(solutions, n)
    num_poly = len(polys)

    if num_poly == 0:
        return None

    # Construct operator for each polymorphism
    operators = []
    for func in polys:
        T = construct_operator(func, solutions, n)
        operators.append(T.flatten())  # vectorize

    # Stack into matrix: each column is a vectorized operator
    op_matrix = np.array(operators).T  # shape: (num_sol^2, num_poly)

    # Compute SVD
    U, sigma, Vt = np.linalg.svd(op_matrix, full_matrices=False)

    # Rank (using relative tolerance)
    tol = max(sigma) * max(op_matrix.shape) * np.finfo(float).eps
    rank = int(np.sum(sigma > tol))

    # Also compute rank at a more generous threshold
    rank_generous = int(np.sum(sigma > 1e-10))

    # Singular value spectrum analysis
    sigma_normalized = sigma / sigma[0] if sigma[0] > 0 else sigma

    # Decay rate: fit log(sigma) ~ -rate * index
    num_sv = min(len(sigma_normalized), rank_generous)
    if num_sv > 1:
        valid = sigma_normalized[:num_sv] > 1e-15
        if np.sum(valid) > 1:
            log_sigma = np.log10(sigma_normalized[:num_sv][valid])
            indices = np.arange(num_sv)[valid]
            if len(indices) > 1:
                coeffs = np.polyfit(indices, log_sigma, 1)
                decay_rate = -coeffs[0]
            else:
                decay_rate = np.inf
        else:
            decay_rate = np.inf
    else:
        decay_rate = np.inf

    # Top singular values (up to 8)
    top_sv = sigma_normalized[:min(8, len(sigma_normalized))]

    return {
        'num_sol': num_sol,
        'num_poly': num_poly,
        'rank': rank,
        'rank_generous': rank_generous,
        'rank_ratio': rank / num_poly if num_poly > 0 else 0,
        'decay_rate': decay_rate,
        'top_sv': top_sv,
        'op_matrix_shape': op_matrix.shape,
    }

def run_experiment(n=6, num_instances=20, seed_base=42):
    """Run the full experiment across all CSP types."""

    configs = [
        ('2-SAT',     1.5, generate_random_2sat),
        ('Horn',      2.0, generate_random_horn),
        ('3-SAT',     3.5, generate_random_3sat),
        ('NAE-3-SAT', 1.0, generate_random_nae3sat),
    ]

    all_results = {}

    for csp_name, alpha, generator in configs:
        print(f"\n{'='*70}")
        print(f"  {csp_name}  (alpha={alpha}, n={n}, k=3)")
        print(f"{'='*70}")

        results = []
        attempts = 0
        max_attempts = num_instances * 5
        rng = np.random.default_rng(seed_base)

        while len(results) < num_instances and attempts < max_attempts:
            attempts += 1
            clauses, ct = generator(n, alpha, rng)
            res = analyze_instance(clauses, ct, n, len(results))
            if res is not None:
                results.append(res)
                sys.stdout.write(f"  Instance {len(results):2d}: "
                                 f"|Sol|={res['num_sol']:4d}  "
                                 f"|Clone_3|={res['num_poly']:4d}  "
                                 f"OpRank={res['rank']:3d}  "
                                 f"Rank/Clone={res['rank_ratio']:.4f}  "
                                 f"SV-decay={res['decay_rate']:.3f}\n")
                sys.stdout.flush()

        all_results[csp_name] = results

        if len(results) < num_instances:
            print(f"  (only {len(results)} valid instances found in {attempts} attempts)")

    return all_results

def print_summary(all_results):
    """Print comprehensive summary tables."""

    print("\n\n")
    print("=" * 90)
    print("  SUMMARY: One-Step Shortcut — Operator Rank as Direct Out(M) Dimension Proxy")
    print("=" * 90)

    # Table 1: Main statistics
    print("\n" + "-" * 90)
    print(f"{'CSP Type':<12} {'Class':<5} {'|Sol|':>7} {'|Clone₃|':>10} "
          f"{'OpRank':>8} {'Rank/Clone':>11} {'SV-decay':>9}")
    print("-" * 90)

    summary = {}
    for csp_name in ['2-SAT', 'Horn', '3-SAT', 'NAE-3-SAT']:
        if csp_name not in all_results or not all_results[csp_name]:
            continue
        results = all_results[csp_name]

        complexity = 'P' if csp_name in ['2-SAT', 'Horn'] else 'NPC'

        sols = [r['num_sol'] for r in results]
        clones = [r['num_poly'] for r in results]
        ranks = [r['rank'] for r in results]
        ratios = [r['rank_ratio'] for r in results]
        decays = [r['decay_rate'] for r in results if r['decay_rate'] != np.inf]

        avg_sol = np.mean(sols)
        avg_clone = np.mean(clones)
        avg_rank = np.mean(ranks)
        avg_ratio = np.mean(ratios)
        avg_decay = np.mean(decays) if decays else float('inf')

        print(f"{csp_name:<12} {complexity:<5} {avg_sol:7.1f} {avg_clone:10.1f} "
              f"{avg_rank:8.1f} {avg_ratio:11.4f} {avg_decay:9.3f}")

        summary[csp_name] = {
            'class': complexity,
            'avg_sol': avg_sol,
            'avg_clone': avg_clone,
            'avg_rank': avg_rank,
            'avg_ratio': avg_ratio,
            'avg_decay': avg_decay,
            'std_rank': np.std(ranks),
            'std_ratio': np.std(ratios),
        }

    print("-" * 90)

    # Table 2: Separation analysis
    print("\n\n" + "-" * 90)
    print("  SEPARATION ANALYSIS: P vs NPC")
    print("-" * 90)

    p_ranks = []
    npc_ranks = []
    p_ratios = []
    npc_ratios = []
    p_decays = []
    npc_decays = []

    for csp_name, info in summary.items():
        results = all_results[csp_name]
        if info['class'] == 'P':
            p_ranks.extend([r['rank'] for r in results])
            p_ratios.extend([r['rank_ratio'] for r in results])
            p_decays.extend([r['decay_rate'] for r in results if r['decay_rate'] != np.inf])
        else:
            npc_ranks.extend([r['rank'] for r in results])
            npc_ratios.extend([r['rank_ratio'] for r in results if r['rank_ratio'] != np.inf])
            npc_decays.extend([r['decay_rate'] for r in results if r['decay_rate'] != np.inf])

    if p_ranks and npc_ranks:
        print(f"\n  Operator Rank:")
        print(f"    P-time  mean: {np.mean(p_ranks):8.2f}  (std: {np.std(p_ranks):.2f})")
        print(f"    NPC     mean: {np.mean(npc_ranks):8.2f}  (std: {np.std(npc_ranks):.2f})")
        rank_sep = np.mean(p_ranks) / np.mean(npc_ranks) if np.mean(npc_ranks) > 0 else float('inf')
        print(f"    Ratio P/NPC:  {rank_sep:8.2f}x")

    if p_ratios and npc_ratios:
        print(f"\n  Rank / Clone Size (fraction of independent operators):")
        print(f"    P-time  mean: {np.mean(p_ratios):8.4f}  (std: {np.std(p_ratios):.4f})")
        print(f"    NPC     mean: {np.mean(npc_ratios):8.4f}  (std: {np.std(npc_ratios):.4f})")

    if p_decays and npc_decays:
        print(f"\n  SV Decay Rate (steeper = more discrete):")
        print(f"    P-time  mean: {np.mean(p_decays):8.4f}  (std: {np.std(p_decays):.4f})")
        print(f"    NPC     mean: {np.mean(npc_decays):8.4f}  (std: {np.std(npc_decays):.4f})")
        decay_ratio = np.mean(npc_decays) / np.mean(p_decays) if np.mean(p_decays) > 0 else float('inf')
        print(f"    Ratio NPC/P:  {decay_ratio:8.2f}x  (>1 means NPC decays faster)")

    # Table 3: Top singular values comparison
    print("\n\n" + "-" * 90)
    print("  SINGULAR VALUE SPECTRA (mean across instances, normalized)")
    print("-" * 90)

    max_sv_len = 8
    print(f"\n  {'CSP':<12} {'Class':<5}", end="")
    for i in range(max_sv_len):
        print(f" {'σ'+str(i+1):>8}", end="")
    print()
    print("  " + "-" * 82)

    for csp_name in ['2-SAT', 'Horn', '3-SAT', 'NAE-3-SAT']:
        if csp_name not in all_results or not all_results[csp_name]:
            continue
        results = all_results[csp_name]
        complexity = 'P' if csp_name in ['2-SAT', 'Horn'] else 'NPC'

        # Average the top SVs
        all_sv = []
        for r in results:
            sv = list(r['top_sv'])
            sv.extend([0.0] * (max_sv_len - len(sv)))
            all_sv.append(sv[:max_sv_len])

        mean_sv = np.mean(all_sv, axis=0)
        print(f"  {csp_name:<12} {complexity:<5}", end="")
        for v in mean_sv:
            print(f" {v:8.4f}", end="")
        print()

    # Table 4: Detailed per-instance for one representative of each type
    print("\n\n" + "-" * 90)
    print("  DETAILED PER-INSTANCE (first 5 of each type)")
    print("-" * 90)
    print(f"  {'CSP':<12} {'Inst':<5} {'|Sol|':>6} {'|Clone₃|':>9} "
          f"{'OpRank':>7} {'Rank/Cln':>9} {'Matrix':>14}")
    print("  " + "-" * 75)

    for csp_name in ['2-SAT', 'Horn', '3-SAT', 'NAE-3-SAT']:
        if csp_name not in all_results:
            continue
        for i, r in enumerate(all_results[csp_name][:5]):
            shape_str = f"{r['op_matrix_shape'][0]}x{r['op_matrix_shape'][1]}"
            print(f"  {csp_name:<12} {i+1:<5} {r['num_sol']:6d} {r['num_poly']:9d} "
                  f"{r['rank']:7d} {r['rank_ratio']:9.4f} {shape_str:>14}")
        print()

    # Verdict
    print("\n" + "=" * 90)
    print("  VERDICT")
    print("=" * 90)

    if p_ranks and npc_ranks:
        p_mean_rank = np.mean(p_ranks)
        npc_mean_rank = np.mean(npc_ranks)
        p_mean_ratio = np.mean(p_ratios)
        npc_mean_ratio = np.mean(npc_ratios) if npc_ratios else 0

        clean_sep = (p_mean_rank > 2 * npc_mean_rank) if npc_mean_rank > 0 else (p_mean_rank > 0)

        if clean_sep:
            print(f"\n  CLEAN SEPARATION OBSERVED.")
            print(f"  P-time operator rank ({p_mean_rank:.1f}) >> NPC operator rank ({npc_mean_rank:.1f})")
            print(f"  The clone DIRECTLY produces a high-dimensional operator family for P-time CSPs,")
            print(f"  confirming the one-step shortcut: exponential clone -> non-discrete Out(M).")
        else:
            ratio = p_mean_rank / npc_mean_rank if npc_mean_rank > 0 else float('inf')
            print(f"\n  P-time / NPC operator rank ratio: {ratio:.2f}x")
            if ratio > 1.5:
                print(f"  Moderate separation: P-time has {ratio:.1f}x more independent operator directions.")
                print(f"  The shortcut shows a clear trend, though not as dramatic as clone size ratios.")
            elif ratio > 1.1:
                print(f"  Weak separation observed. The rank grows for P-time but only modestly.")
            else:
                print(f"  No clean separation in operator rank alone.")

        # Comment on rank ratio
        print(f"\n  Rank/Clone fraction:")
        print(f"    P-time:  {p_mean_ratio:.4f}  (fraction of polys that are independent operators)")
        print(f"    NPC:     {npc_mean_ratio:.4f}")

        if p_mean_ratio < npc_mean_ratio and npc_mean_ratio > 0:
            print(f"  Note: P-time has LOWER rank/clone ratio, meaning the clone has more")
            print(f"  'redundancy' -- but the ABSOLUTE rank is still higher. The extra")
            print(f"  polymorphisms are not all independent, but they still span MORE directions.")

    print()


# ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 90)
    print("  Direct Out(M) Test: Operator Rank from Polymorphism Clone")
    print("  n=6, k=3 (ternary), 20 instances per CSP class")
    print("=" * 90)

    t0 = time.time()
    results = run_experiment(n=6, num_instances=20, seed_base=42)
    elapsed = time.time() - t0

    print_summary(results)

    print(f"\n  Total runtime: {elapsed:.1f}s")
    print("=" * 90)
