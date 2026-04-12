"""
Gap Alpha Computation -- Node 1.3.5.1

Computes T_maj for 2-SAT and 3-SAT instances, measures commutator norms,
and determines whether Gap Alpha closes or is killed.

The clone operator T_maj is defined as:
    T_maj[s, a] = (1/|Sol|^2) * #{(b,c) in Sol^2 : maj(a,b,c) = s}

where maj is coordinatewise majority.

For 2-SAT: majority IS a polymorphism (maj(a,b,c) in Sol for all a,b,c in Sol).
For 3-SAT: majority is NOT a polymorphism (control experiment).

Author: Claude Opus 4.6 (1M context), Node 1.3.5.1
Date: 2026-04-11
"""

import numpy as np
from itertools import product as cartesian_product
import random
import json
import sys
from collections import defaultdict

random.seed(42)
np.set_printoptions(precision=6, suppress=True, linewidth=120)


# ============================================================
# 1. Instance generation
# ============================================================

def generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4, max_attempts=500):
    """Generate a random 2-SAT instance with at least min_solutions solutions."""
    num_clauses = int(n * clause_ratio)
    for attempt in range(max_attempts):
        clauses = []
        for _ in range(num_clauses):
            # Pick two distinct variables
            vars_ = random.sample(range(n), 2)
            # Each literal is positive or negated
            signs = [random.choice([0, 1]) for _ in range(2)]
            clauses.append((vars_[0], signs[0], vars_[1], signs[1]))

        # Enumerate solutions
        sols = enumerate_solutions_2sat(n, clauses)
        if len(sols) >= min_solutions:
            return n, clauses, sols
    return None


def generate_3sat_instance(n, clause_ratio=2.0, min_solutions=4, max_attempts=500):
    """Generate a random 3-SAT instance with at least min_solutions solutions."""
    num_clauses = int(n * clause_ratio)
    for attempt in range(max_attempts):
        clauses = []
        for _ in range(num_clauses):
            vars_ = random.sample(range(n), 3)
            signs = [random.choice([0, 1]) for _ in range(3)]
            clauses.append((vars_[0], signs[0], vars_[1], signs[1], vars_[2], signs[2]))

        sols = enumerate_solutions_3sat(n, clauses)
        if len(sols) >= min_solutions:
            return n, clauses, sols
    return None


def evaluate_clause_2sat(assignment, clause):
    """Evaluate a single 2-SAT clause."""
    v0, s0, v1, s1 = clause
    lit0 = assignment[v0] if s0 == 1 else 1 - assignment[v0]
    lit1 = assignment[v1] if s1 == 1 else 1 - assignment[v1]
    return lit0 or lit1


def evaluate_clause_3sat(assignment, clause):
    """Evaluate a single 3-SAT clause."""
    v0, s0, v1, s1, v2, s2 = clause
    lit0 = assignment[v0] if s0 == 1 else 1 - assignment[v0]
    lit1 = assignment[v1] if s1 == 1 else 1 - assignment[v1]
    lit2 = assignment[v2] if s2 == 1 else 1 - assignment[v2]
    return lit0 or lit1 or lit2


def enumerate_solutions_2sat(n, clauses):
    """Brute-force enumerate all solutions of a 2-SAT instance."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause_2sat(assignment, c) for c in clauses):
            solutions.append(assignment)
    return solutions


def enumerate_solutions_3sat(n, clauses):
    """Brute-force enumerate all solutions of a 3-SAT instance."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause_3sat(assignment, c) for c in clauses):
            solutions.append(assignment)
    return solutions


# ============================================================
# 2. Coordinatewise majority
# ============================================================

def coordinatewise_majority(a, b, c):
    """Compute coordinatewise majority of three binary tuples."""
    n = len(a)
    result = tuple(int(a[i] + b[i] + c[i] >= 2) for i in range(n))
    return result


# ============================================================
# 3. Polymorphism verification
# ============================================================

def verify_majority_polymorphism(solutions):
    """
    Verify that majority is a polymorphism: for all (a,b,c) in Sol^3,
    maj(a,b,c) must be in Sol.
    Returns (is_polymorphism, num_violations, total_triples).
    """
    sol_set = set(solutions)
    violations = 0
    total = 0
    for a in solutions:
        for b in solutions:
            for c in solutions:
                total += 1
                result = coordinatewise_majority(a, b, c)
                if result not in sol_set:
                    violations += 1
    return violations == 0, violations, total


# ============================================================
# 4. Compute T_maj
# ============================================================

def compute_T_maj(solutions):
    """
    Compute the clone operator T_maj.

    T_maj[s_idx, a_idx] = (1/|Sol|^2) * #{(b,c) in Sol^2 : maj(a,b,c) = s}

    Returns the |Sol| x |Sol| matrix T_maj, indexed by solution order.
    """
    sol_list = list(solutions)
    sol_set = set(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}

    T = np.zeros((S, S), dtype=np.float64)

    for a_idx, a in enumerate(sol_list):
        for b in sol_list:
            for c in sol_list:
                result = coordinatewise_majority(a, b, c)
                if result in sol_to_idx:
                    s_idx = sol_to_idx[result]
                    T[s_idx, a_idx] += 1.0

    T /= (S * S)  # Normalize by |Sol|^2
    return T


# ============================================================
# 5. Commutator norms
# ============================================================

def compute_commutator_norms(T_maj, solutions):
    """
    Compute ||[T_maj, y]||_2 for generators y = |s><s'| (matrix units).

    The generators of M_Bool^L (restricted to the solution space) are
    the matrix units |s><s'| for all pairs (s, s') in Sol x Sol.

    ||[T, y]||_2 = ||T*y - y*T||_F / sqrt(|Sol|)

    where ||.||_F is Frobenius norm and the division by sqrt(|Sol|)
    normalizes to the 2-norm in the tracial state.

    Returns: max_norm, mean_norm, all_norms_dict
    """
    S = len(solutions)
    norms = []
    norm_dict = {}

    for i in range(S):
        for j in range(S):
            # y = |i><j| = matrix with 1 at (i,j) and 0 elsewhere
            y = np.zeros((S, S), dtype=np.float64)
            y[i, j] = 1.0

            commutator = T_maj @ y - y @ T_maj
            frob_norm = np.linalg.norm(commutator, 'fro')
            # Normalize: ||.||_2 in the tracial state = ||.||_F / sqrt(dim)
            norm_2 = frob_norm / np.sqrt(S)
            norms.append(norm_2)
            norm_dict[(i, j)] = norm_2

    max_norm = max(norms)
    mean_norm = np.mean(norms)
    return max_norm, mean_norm, norm_dict


# ============================================================
# 6. Analysis functions
# ============================================================

def analyze_T_maj(T, label=""):
    """Analyze the structure of T_maj: eigenvalues, rank, identity test."""
    S = T.shape[0]
    eigenvalues = np.linalg.eigvals(T)
    eigenvalues_real = np.sort(np.real(eigenvalues))[::-1]

    # Is T proportional to identity?
    trace = np.trace(T)
    scalar = trace / S
    T_minus_scalar_I = T - scalar * np.eye(S)
    deviation_from_scalar = np.linalg.norm(T_minus_scalar_I, 'fro') / np.linalg.norm(T, 'fro')

    # Is T the identity?
    T_minus_I = T - np.eye(S)
    deviation_from_identity = np.linalg.norm(T_minus_I, 'fro')

    # Rank (numerical)
    rank = np.linalg.matrix_rank(T, tol=1e-10)

    # Is T doubly stochastic?
    col_sums = T.sum(axis=0)
    row_sums = T.sum(axis=1)
    is_col_stochastic = np.allclose(col_sums, 1.0, atol=1e-10)
    is_row_stochastic = np.allclose(row_sums, 1.0, atol=1e-10)

    return {
        'label': label,
        'size': S,
        'eigenvalues_real': eigenvalues_real,
        'trace': trace,
        'scalar_coefficient': scalar,
        'deviation_from_scalar_I': deviation_from_scalar,
        'deviation_from_identity': deviation_from_identity,
        'rank': rank,
        'is_identity': deviation_from_identity < 1e-10,
        'is_scalar_multiple_of_I': deviation_from_scalar < 1e-10,
        'is_col_stochastic': is_col_stochastic,
        'is_row_stochastic': is_row_stochastic,
        'frobenius_norm': np.linalg.norm(T, 'fro'),
    }


def print_analysis(analysis, T, max_commutator, mean_commutator):
    """Print a formatted analysis report."""
    print(f"\n{'='*70}")
    print(f"  {analysis['label']}")
    print(f"{'='*70}")
    print(f"  |Sol| = {analysis['size']}")
    print(f"  Rank = {analysis['rank']}")
    print(f"  Trace = {analysis['trace']:.6f}")
    print(f"  Scalar coefficient (trace/|Sol|) = {analysis['scalar_coefficient']:.6f}")
    print(f"  ||T - (trace/|Sol|)*I||_F / ||T||_F = {analysis['deviation_from_scalar_I']:.8f}")
    print(f"  ||T - I||_F = {analysis['deviation_from_identity']:.6f}")
    print(f"  T = Identity? {analysis['is_identity']}")
    print(f"  T = scalar * I? {analysis['is_scalar_multiple_of_I']}")
    print(f"  Column-stochastic? {analysis['is_col_stochastic']}")
    print(f"  Row-stochastic? {analysis['is_row_stochastic']}")
    print(f"  ||T||_F = {analysis['frobenius_norm']:.6f}")
    print(f"\n  Eigenvalues (real parts, top 10):")
    eigs = analysis['eigenvalues_real']
    for i, e in enumerate(eigs[:min(10, len(eigs))]):
        print(f"    lambda_{i} = {e:.8f}")
    if len(eigs) > 10:
        print(f"    ... ({len(eigs) - 10} more)")
        print(f"    lambda_min = {eigs[-1]:.8f}")

    print(f"\n  Commutator norms:")
    print(f"    max_y ||[T_maj, y]||_2 = {max_commutator:.8f}")
    print(f"    mean_y ||[T_maj, y]||_2 = {mean_commutator:.8f}")

    if analysis['size'] <= 16:
        print(f"\n  T_maj matrix:")
        print(T)


# ============================================================
# 7. Main computation
# ============================================================

def run_experiment(sat_type, n_values, generate_func, verify_poly=True):
    """Run the T_maj computation for a set of instance sizes."""
    results = []

    for n in n_values:
        print(f"\n{'#'*70}")
        print(f"  {sat_type}: n = {n}")
        print(f"{'#'*70}")

        instance = generate_func(n)
        if instance is None:
            print(f"  FAILED to generate satisfiable instance with >= 4 solutions at n={n}")
            results.append({'n': n, 'status': 'FAILED'})
            continue

        n_vars, clauses, solutions = instance
        S = len(solutions)
        print(f"  Variables: {n_vars}, Clauses: {len(clauses)}, Solutions: {S}")

        # Verify polymorphism property
        if verify_poly:
            print(f"  Verifying majority polymorphism (|Sol|^3 = {S**3} triples)...", end=" ", flush=True)
            is_poly, violations, total = verify_majority_polymorphism(solutions)
            if is_poly:
                print(f"PASS (0/{total} violations)")
            else:
                print(f"FAIL ({violations}/{total} violations)")
                if sat_type == "2-SAT":
                    print("  ERROR: majority MUST be a polymorphism for 2-SAT. Instance is buggy.")
                    results.append({'n': n, 'status': 'POLYMORPHISM_FAIL', 'violations': violations})
                    continue
                else:
                    print(f"  Expected: majority is NOT a polymorphism for {sat_type}.")
                    # For 3-SAT: compute T_maj anyway (but note it maps outside Sol)
                    # We compute the RESTRICTED T_maj: only count triples where maj(a,b,c) in Sol
                    pass
        else:
            is_poly = None

        # Compute T_maj
        print(f"  Computing T_maj ({S}x{S} matrix, {S**3} triple evaluations)...", end=" ", flush=True)
        T = compute_T_maj(solutions)
        print("done.")

        # Analyze
        analysis = analyze_T_maj(T, label=f"{sat_type} n={n}, |Sol|={S}")

        # Commutator norms
        print(f"  Computing commutator norms ({S**2} generators)...", end=" ", flush=True)
        max_comm, mean_comm, comm_dict = compute_commutator_norms(T, solutions)
        print("done.")

        # Print report
        print_analysis(analysis, T, max_comm, mean_comm)

        results.append({
            'n': n,
            'num_solutions': S,
            'num_clauses': len(clauses),
            'is_polymorphism': is_poly if verify_poly else None,
            'is_identity': analysis['is_identity'],
            'is_scalar_I': analysis['is_scalar_multiple_of_I'],
            'deviation_from_scalar_I': analysis['deviation_from_scalar_I'],
            'trace': analysis['trace'],
            'scalar_coeff': analysis['scalar_coefficient'],
            'rank': analysis['rank'],
            'max_commutator': max_comm,
            'mean_commutator': mean_comm,
            'eigenvalues_top5': list(analysis['eigenvalues_real'][:5]),
            'eigenvalue_min': float(analysis['eigenvalues_real'][-1]),
            'col_stochastic': analysis['is_col_stochastic'],
            'row_stochastic': analysis['is_row_stochastic'],
            'status': 'OK',
        })

    return results


def main():
    print("=" * 70)
    print("  GAP ALPHA COMPUTATION -- Node 1.3.5.1")
    print("  Clone operator T_maj for 2-SAT and 3-SAT")
    print("=" * 70)

    # --------------------------------------------------------
    # PART 1: 2-SAT (majority IS a polymorphism)
    # --------------------------------------------------------
    print("\n\n" + "=" * 70)
    print("  PART 1: 2-SAT (majority is a polymorphism)")
    print("=" * 70)

    n_values_2sat = [4, 6, 8, 10, 12]
    results_2sat = run_experiment(
        "2-SAT", n_values_2sat,
        lambda n: generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4),
        verify_poly=True
    )

    # --------------------------------------------------------
    # PART 2: 3-SAT CONTROL (majority is NOT a polymorphism)
    # --------------------------------------------------------
    print("\n\n" + "=" * 70)
    print("  PART 2: 3-SAT CONTROL (majority is NOT a polymorphism)")
    print("=" * 70)

    # For 3-SAT at larger n, enumeration becomes expensive
    # Use smaller sizes and lower clause ratio to get enough solutions
    n_values_3sat = [4, 6, 8, 10, 12]
    results_3sat = run_experiment(
        "3-SAT", n_values_3sat,
        lambda n: generate_3sat_instance(n, clause_ratio=2.0, min_solutions=4),
        verify_poly=True
    )

    # --------------------------------------------------------
    # PART 3: SCALING ANALYSIS
    # --------------------------------------------------------
    print("\n\n" + "=" * 70)
    print("  PART 3: SCALING ANALYSIS")
    print("=" * 70)

    print("\n  2-SAT Scaling:")
    print(f"  {'n':>4s}  {'|Sol|':>6s}  {'max||[T,y]||_2':>16s}  {'mean||[T,y]||_2':>16s}  {'dev_scalar':>12s}  {'T=I?':>6s}  {'T=cI?':>6s}")
    print(f"  {'-'*4}  {'-'*6}  {'-'*16}  {'-'*16}  {'-'*12}  {'-'*6}  {'-'*6}")
    for r in results_2sat:
        if r['status'] == 'OK':
            print(f"  {r['n']:4d}  {r['num_solutions']:6d}  {r['max_commutator']:16.8f}  {r['mean_commutator']:16.8f}  {r['deviation_from_scalar_I']:12.8f}  {'YES' if r['is_identity'] else 'NO':>6s}  {'YES' if r['is_scalar_I'] else 'NO':>6s}")

    print("\n  3-SAT Scaling (control):")
    print(f"  {'n':>4s}  {'|Sol|':>6s}  {'max||[T,y]||_2':>16s}  {'mean||[T,y]||_2':>16s}  {'dev_scalar':>12s}  {'T=I?':>6s}  {'T=cI?':>6s}  {'poly?':>6s}")
    print(f"  {'-'*4}  {'-'*6}  {'-'*16}  {'-'*16}  {'-'*12}  {'-'*6}  {'-'*6}  {'-'*6}")
    for r in results_3sat:
        if r['status'] == 'OK':
            poly_str = 'YES' if r['is_polymorphism'] else 'NO'
            print(f"  {r['n']:4d}  {r['num_solutions']:6d}  {r['max_commutator']:16.8f}  {r['mean_commutator']:16.8f}  {r['deviation_from_scalar_I']:12.8f}  {'YES' if r['is_identity'] else 'NO':>6s}  {'YES' if r['is_scalar_I'] else 'NO':>6s}  {poly_str:>6s}")

    # --------------------------------------------------------
    # PART 4: VERDICT
    # --------------------------------------------------------
    print("\n\n" + "=" * 70)
    print("  PART 4: VERDICT")
    print("=" * 70)

    # Check if T_maj is always the identity for 2-SAT
    ok_2sat = [r for r in results_2sat if r['status'] == 'OK']
    all_identity = all(r['is_identity'] for r in ok_2sat)
    all_scalar = all(r['is_scalar_I'] for r in ok_2sat)

    if all_identity:
        print("\n  KILL: T_maj = Identity for all 2-SAT instances.")
        print("  The omega-averaged construction produces the trivial central sequence.")
        print("  Gap Alpha is KILLED by identity collapse.")
        verdict = "GAP-ALPHA-KILLED (identity collapse)"
    elif all_scalar:
        print("\n  KILL: T_maj = scalar * I for all 2-SAT instances.")
        print("  The construction produces trivially central sequences (already scalar).")
        print("  Gap Alpha is KILLED by scalar collapse.")
        verdict = "GAP-ALPHA-KILLED (scalar collapse)"
    else:
        # T_maj is non-trivial. Check scaling of commutator norms.
        max_comms = [(r['n'], r['max_commutator']) for r in ok_2sat]
        if len(max_comms) >= 3:
            ns = [x[0] for x in max_comms]
            comms = [x[1] for x in max_comms]

            # Check if commutator norms decrease with n
            decreasing = all(comms[i] >= comms[i+1] for i in range(len(comms)-1))
            increasing = all(comms[i] <= comms[i+1] for i in range(len(comms)-1))

            # Fit log-log to check power law
            if all(c > 0 for c in comms):
                log_ns = np.log(np.array(ns, dtype=float))
                log_comms = np.log(np.array(comms, dtype=float))
                if len(log_ns) >= 2:
                    coeffs = np.polyfit(log_ns, log_comms, 1)
                    slope = coeffs[0]
                    print(f"\n  T_maj is NON-TRIVIAL (not scalar * I).")
                    print(f"  Commutator norm scaling: max||[T,y]||_2 ~ n^{slope:.3f}")
                    print(f"  Monotonically decreasing? {decreasing}")
                    print(f"  Monotonically increasing? {increasing}")

                    if slope < -0.1 and decreasing:
                        print(f"\n  EVIDENCE FOR GAP-ALPHA-CLOSED:")
                        print(f"  T_maj is non-trivial AND commutator norms DECREASE with n.")
                        print(f"  Scaling exponent: {slope:.3f} (negative = good for closure).")
                        verdict = f"GAP-ALPHA-CLOSING (exponent {slope:.3f})"
                    elif slope > 0.1 and increasing:
                        print(f"\n  EVIDENCE AGAINST GAP-ALPHA:")
                        print(f"  T_maj is non-trivial BUT commutator norms INCREASE with n.")
                        print(f"  Scaling exponent: {slope:.3f} (positive = bad for closure).")
                        verdict = f"GAP-ALPHA-KILLED (increasing commutator, exponent {slope:.3f})"
                    else:
                        print(f"\n  INCONCLUSIVE: Non-monotonic or near-zero scaling exponent.")
                        verdict = f"INCONCLUSIVE (exponent {slope:.3f})"
                else:
                    verdict = "INCONCLUSIVE (insufficient data points)"
            else:
                print("\n  Some commutator norms are zero -- need investigation.")
                verdict = "INCONCLUSIVE (zero commutator norms)"
        else:
            verdict = "INCONCLUSIVE (fewer than 3 successful instances)"

    # 3-SAT control comparison
    print(f"\n  3-SAT CONTROL:")
    ok_3sat = [r for r in results_3sat if r['status'] == 'OK']
    poly_3sat = [r for r in ok_3sat if r.get('is_polymorphism') is True]
    non_poly_3sat = [r for r in ok_3sat if r.get('is_polymorphism') is False]
    print(f"  Instances where majority IS a polymorphism: {len(poly_3sat)}/{len(ok_3sat)}")
    print(f"  Instances where majority is NOT a polymorphism: {len(non_poly_3sat)}/{len(ok_3sat)}")

    if non_poly_3sat:
        print(f"  Majority polymorphism FAILS for 3-SAT as expected -- control passes.")
    else:
        print(f"  WARNING: majority is a polymorphism for all tested 3-SAT instances.")
        print(f"  This may indicate clause ratio is too low (solutions too abundant).")

    # Final summary
    print(f"\n  {'='*60}")
    print(f"  FINAL VERDICT: {verdict}")
    print(f"  {'='*60}")

    # Dump raw data as JSON for the research node
    output_data = {
        'verdict': verdict,
        '2sat_results': [{k: v for k, v in r.items() if k != 'eigenvalues_top5' or True} for r in results_2sat],
        '3sat_results': [{k: v for k, v in r.items() if k != 'eigenvalues_top5' or True} for r in results_3sat],
    }
    print("\n\n--- RAW JSON DATA ---")
    # Convert numpy types for JSON serialization
    def convert(obj):
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return obj

    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            r = convert(obj)
            if r is not obj:
                return r
            return super().default(obj)

    print(json.dumps(output_data, indent=2, cls=NumpyEncoder))


if __name__ == "__main__":
    main()
