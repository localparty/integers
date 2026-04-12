"""
Gap Alpha Multi-Slot Construction -- Node 1.3.5.2

SALVAGE S4: Multi-slot clone operator construction.

Context: Node 1.3.5.1 computed T_f with ONE live slot and (k-1) omega-averaged
slots. Result: KILLED (K-14). The omega-averaging concentrates onto the mean at
high arity, producing a rank-1 projector. Commutator norms INCREASE with k.

This node uses 2 LIVE slots + (k-2) averaged slots.

For a k-ary polymorphism f on solution set Sol(Gamma), define:

    T_f^{(2)}[s, (a,b)] = (1/|Sol|^{k-2}) * #{(c^(3),...,c^(k)) in Sol^{k-2} :
                            f(a, b, c^(3),...,c^(k)) = s}

This is a |Sol| x |Sol|^2 matrix. The two live slots (a,b) interact non-trivially
through f, preventing the rank-1 collapse.

Also tests the SYMMETRIZED version:
    T_f^{sym}[s,a] = (1/k) sum_{j=1}^{k} T_f^{(j)}[s,a]
where T_f^{(j)} places the live slot at position j and averages the rest.

Tests:
1. Random 2-SAT instances at n = 4, 6, 8, 10
2. T_maj^{(2)} -- the |Sol| x |Sol|^2 matrix (2 live slots)
3. Rank-1 collapse check
4. Reduced operators: for fixed b, T_f^{(2)}(.,b) is |Sol|x|Sol|. Commutator norms.
5. Arity scan: k = 3, 5, 7, 9, 11 with threshold-k polymorphisms
6. Symmetrized version T_f^{sym}

Author: Claude Opus 4.6 (1M context), Node 1.3.5.2
Date: 2026-04-11
"""

import numpy as np
from itertools import product as cartesian_product
import random
import sys
import time
from collections import defaultdict

random.seed(42)
np.random.seed(42)
np.set_printoptions(precision=6, suppress=True, linewidth=120)


# ============================================================
# 1. Instance generation (reused from 1.3.5.1)
# ============================================================

def generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4, max_attempts=500):
    """Generate a random 2-SAT instance with at least min_solutions solutions."""
    num_clauses = max(int(n * clause_ratio), 1)
    for attempt in range(max_attempts):
        clauses = []
        for _ in range(num_clauses):
            vars_ = random.sample(range(n), 2)
            signs = [random.choice([0, 1]) for _ in range(2)]
            clauses.append((vars_[0], signs[0], vars_[1], signs[1]))
        sols = enumerate_solutions_2sat(n, clauses)
        if len(sols) >= min_solutions:
            return n, clauses, sols
    return None


def evaluate_clause_2sat(assignment, clause):
    v0, s0, v1, s1 = clause
    lit0 = assignment[v0] if s0 == 1 else 1 - assignment[v0]
    lit1 = assignment[v1] if s1 == 1 else 1 - assignment[v1]
    return lit0 or lit1


def enumerate_solutions_2sat(n, clauses):
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause_2sat(assignment, c) for c in clauses):
            solutions.append(assignment)
    return solutions


# ============================================================
# 2. Polymorphism functions
# ============================================================

def coordinatewise_majority(a, b, c):
    """Coordinatewise majority of three binary tuples."""
    return tuple(int(a[i] + b[i] + c[i] >= 2) for i in range(len(a)))


def coordinatewise_threshold_k(inputs, k):
    """
    Coordinatewise threshold-k: output bit i = 1 iff at least ceil(k/2)
    of the k inputs have bit i = 1. This is the k-ary majority.
    For 2-SAT, threshold-k is always a polymorphism (preserves 2-SAT
    constraints for all k >= 3 odd).
    """
    n = len(inputs[0])
    threshold = (k + 1) // 2  # ceil(k/2)
    result = []
    for i in range(n):
        s = sum(inp[i] for inp in inputs)
        result.append(1 if s >= threshold else 0)
    return tuple(result)


def verify_polymorphism_threshold_k(solutions, k, num_samples=50000):
    """
    Verify threshold-k is a polymorphism: for all (a1,...,ak) in Sol^k,
    threshold_k(a1,...,ak) must be in Sol.
    Uses Monte Carlo for large k.
    """
    sol_set = set(solutions)
    S = len(solutions)
    total_tuples = S ** k

    if total_tuples <= 200000:
        # Exhaustive check
        violations = 0
        total = 0
        for combo in cartesian_product(solutions, repeat=k):
            total += 1
            result = coordinatewise_threshold_k(combo, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, total
    else:
        # Monte Carlo
        violations = 0
        for _ in range(num_samples):
            combo = [solutions[random.randint(0, S-1)] for _ in range(k)]
            result = coordinatewise_threshold_k(combo, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, num_samples


# ============================================================
# 3. Multi-slot T_f^{(2)}: 2 live slots + (k-2) averaged
# ============================================================

def compute_T_multislot_2live(solutions, k, num_mc_samples=None):
    """
    Compute T_f^{(2)} with 2 live slots (positions 0,1) and (k-2) averaged.

    T_f^{(2)}[s_idx, (a_idx, b_idx)] =
        (1/|Sol|^{k-2}) * #{(c3,...,ck) in Sol^{k-2} : f(a,b,c3,...,ck) = s}

    Returns: T as |Sol| x |Sol|^2 matrix (rows = output s, cols = (a,b) pairs)
    Also returns T reshaped as |Sol| x |Sol| x |Sol| tensor.
    """
    sol_list = list(solutions)
    sol_set = set(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n_avg = k - 2  # number of averaged slots

    # T[s, (a_idx * S + b_idx)] = count / normalization
    T = np.zeros((S, S * S), dtype=np.float64)

    if n_avg == 0:
        # k=2 case: no averaging, f(a,b) directly
        # But threshold-2 is just componentwise AND/OR, not majority
        # Skip this case
        raise ValueError("k must be >= 3 for 2 live + (k-2) averaged")

    if n_avg == 1:
        # k=3 majority: 1 averaged slot
        for a_idx, a in enumerate(sol_list):
            for b_idx, b in enumerate(sol_list):
                col_idx = a_idx * S + b_idx
                for c in sol_list:
                    inputs = [a, b, c]
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        s_idx = sol_to_idx[result]
                        T[s_idx, col_idx] += 1.0
        T /= S  # normalize by |Sol|^1
    else:
        # k >= 5: multiple averaged slots, use Monte Carlo if needed
        total_avg_tuples = S ** n_avg
        if num_mc_samples is None:
            num_mc_samples = min(total_avg_tuples, 50000)
        use_exact = (total_avg_tuples <= num_mc_samples)

        if use_exact:
            for a_idx, a in enumerate(sol_list):
                for b_idx, b in enumerate(sol_list):
                    col_idx = a_idx * S + b_idx
                    for avg_combo in cartesian_product(sol_list, repeat=n_avg):
                        inputs = [a, b] + list(avg_combo)
                        result = coordinatewise_threshold_k(inputs, k)
                        if result in sol_to_idx:
                            s_idx = sol_to_idx[result]
                            T[s_idx, col_idx] += 1.0
            T /= (S ** n_avg)
        else:
            # Monte Carlo averaging
            for a_idx, a in enumerate(sol_list):
                for b_idx, b in enumerate(sol_list):
                    col_idx = a_idx * S + b_idx
                    for _ in range(num_mc_samples):
                        avg_inputs = [sol_list[random.randint(0, S-1)]
                                      for _ in range(n_avg)]
                        inputs = [a, b] + avg_inputs
                        result = coordinatewise_threshold_k(inputs, k)
                        if result in sol_to_idx:
                            s_idx = sol_to_idx[result]
                            T[s_idx, col_idx] += 1.0
            T /= num_mc_samples

    # Reshape to tensor: T_tensor[s, a, b]
    T_tensor = T.reshape(S, S, S)
    return T, T_tensor


# ============================================================
# 4. Single-slot T_f^{(1)} (from 1.3.5.1, for comparison)
# ============================================================

def compute_T_singleslot(solutions, k, num_mc_samples=None):
    """
    Compute T_f^{(1)} with 1 live slot (position 0) and (k-1) averaged.

    T_f^{(1)}[s_idx, a_idx] = (1/|Sol|^{k-1}) * #{(b,...) in Sol^{k-1} :
                                f(a, b, ...) = s}

    Returns: |Sol| x |Sol| matrix.
    """
    sol_list = list(solutions)
    sol_set = set(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n_avg = k - 1

    T = np.zeros((S, S), dtype=np.float64)
    total_avg_tuples = S ** n_avg

    if num_mc_samples is None:
        num_mc_samples = min(total_avg_tuples, 100000)
    use_exact = (total_avg_tuples <= num_mc_samples)

    if use_exact:
        for a_idx, a in enumerate(sol_list):
            for avg_combo in cartesian_product(sol_list, repeat=n_avg):
                inputs = [a] + list(avg_combo)
                result = coordinatewise_threshold_k(inputs, k)
                if result in sol_to_idx:
                    s_idx = sol_to_idx[result]
                    T[s_idx, a_idx] += 1.0
        T /= (S ** n_avg)
    else:
        for a_idx, a in enumerate(sol_list):
            for _ in range(num_mc_samples):
                avg_inputs = [sol_list[random.randint(0, S-1)]
                              for _ in range(n_avg)]
                inputs = [a] + avg_inputs
                result = coordinatewise_threshold_k(inputs, k)
                if result in sol_to_idx:
                    s_idx = sol_to_idx[result]
                    T[s_idx, a_idx] += 1.0
        T /= num_mc_samples

    return T


# ============================================================
# 5. Symmetrized T_f^{sym}: average over all slot positions
# ============================================================

def compute_T_symmetrized(solutions, k, num_mc_samples=None):
    """
    Compute T_f^{sym}[s, a] = (1/k) sum_{j=1}^{k} T_f^{(j)}[s, a]
    where T_f^{(j)} puts the live slot at position j and averages the rest.

    Returns: |Sol| x |Sol| matrix (symmetric over slot positions).
    """
    sol_list = list(solutions)
    sol_set = set(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n_avg = k - 1

    T_sym = np.zeros((S, S), dtype=np.float64)
    total_avg_tuples = S ** n_avg

    if num_mc_samples is None:
        num_mc_samples = min(total_avg_tuples, 100000)
    use_exact = (total_avg_tuples <= num_mc_samples)

    for live_pos in range(k):
        T_j = np.zeros((S, S), dtype=np.float64)
        if use_exact:
            for a_idx, a in enumerate(sol_list):
                for avg_combo in cartesian_product(sol_list, repeat=n_avg):
                    # Build input: a goes at position live_pos,
                    # avg_combo fills the rest
                    inputs = list(avg_combo[:live_pos]) + [a] + \
                             list(avg_combo[live_pos:])
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        s_idx = sol_to_idx[result]
                        T_j[s_idx, a_idx] += 1.0
            T_j /= (S ** n_avg)
        else:
            for a_idx, a in enumerate(sol_list):
                for _ in range(num_mc_samples):
                    avg_inputs = [sol_list[random.randint(0, S-1)]
                                  for _ in range(n_avg)]
                    inputs = list(avg_inputs[:live_pos]) + [a] + \
                             list(avg_inputs[live_pos:])
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        s_idx = sol_to_idx[result]
                        T_j[s_idx, a_idx] += 1.0
            T_j /= num_mc_samples
        T_sym += T_j

    T_sym /= k  # Average over k slot positions
    return T_sym


# ============================================================
# 6. Analysis: rank, commutator norms, eigenvalues
# ============================================================

def analyze_matrix(M, label=""):
    """Analyze a square matrix: eigenvalues, rank, identity distance."""
    S = M.shape[0]
    eigenvalues = np.linalg.eigvals(M)
    eigenvalues_real = np.sort(np.real(eigenvalues))[::-1]

    trace = np.trace(M)
    scalar = trace / S
    M_minus_scalar_I = M - scalar * np.eye(S)
    dev_scalar = np.linalg.norm(M_minus_scalar_I, 'fro') / max(np.linalg.norm(M, 'fro'), 1e-15)

    M_minus_I = M - np.eye(S)
    dev_identity = np.linalg.norm(M_minus_I, 'fro')

    rank = np.linalg.matrix_rank(M, tol=1e-10)

    col_sums = M.sum(axis=0)
    row_sums = M.sum(axis=1)
    is_col_stochastic = np.allclose(col_sums, 1.0, atol=1e-8)
    is_row_stochastic = np.allclose(row_sums, 1.0, atol=1e-8)

    return {
        'label': label,
        'size': S,
        'rank': rank,
        'eigenvalues_real': eigenvalues_real,
        'lambda_1': eigenvalues_real[0] if len(eigenvalues_real) > 0 else None,
        'lambda_2': eigenvalues_real[1] if len(eigenvalues_real) > 1 else None,
        'lambda_min': eigenvalues_real[-1] if len(eigenvalues_real) > 0 else None,
        'trace': trace,
        'scalar_coefficient': scalar,
        'deviation_from_scalar_I': dev_scalar,
        'deviation_from_identity': dev_identity,
        'is_identity': dev_identity < 1e-10,
        'is_scalar_I': dev_scalar < 1e-10,
        'is_col_stochastic': is_col_stochastic,
        'is_row_stochastic': is_row_stochastic,
        'frobenius_norm': np.linalg.norm(M, 'fro'),
    }


def compute_commutator_norms_matrix(M, S):
    """
    Compute ||[M, y]||_2 for generators y = |i><j| (matrix units).
    Returns: max_norm, mean_norm
    """
    norms = []
    for i in range(S):
        for j in range(S):
            y = np.zeros((S, S), dtype=np.float64)
            y[i, j] = 1.0
            comm = M @ y - y @ M
            frob = np.linalg.norm(comm, 'fro')
            norm_2 = frob / np.sqrt(S)
            norms.append(norm_2)
    return max(norms), np.mean(norms)


def analyze_multislot_rank(T_tensor, S, label=""):
    """
    Analyze the multi-slot T^{(2)} tensor for rank-1 collapse.

    T_tensor[s, a, b] is S x S x S.
    The matrix form is S x S^2.

    Check:
    1. Rank of the S x S^2 matrix (if rank = 1, it's collapsed)
    2. For each fixed b, T(:,:,b) is an S x S matrix. Analyze its rank.
    3. Compare singular values of the S x S^2 matrix.
    """
    T_matrix = T_tensor.reshape(S, S * S)
    svs = np.linalg.svd(T_matrix, compute_uv=False)

    # Numerical rank
    tol = 1e-10
    rank = np.sum(svs > tol)

    # Ratio of second to first singular value (if rank-1, this -> 0)
    if svs[0] > 1e-15:
        sv_ratio = svs[1] / svs[0] if len(svs) > 1 else 0.0
    else:
        sv_ratio = 0.0

    # Per-b analysis
    per_b_ranks = []
    per_b_commutator_max = []
    per_b_commutator_mean = []
    for b_idx in range(S):
        T_b = T_tensor[:, :, b_idx]  # S x S matrix: T(:, :, b=fixed)
        r = np.linalg.matrix_rank(T_b, tol=1e-10)
        per_b_ranks.append(r)

        # Commutator norms for this slice
        max_c, mean_c = compute_commutator_norms_matrix(T_b, S)
        per_b_commutator_max.append(max_c)
        per_b_commutator_mean.append(mean_c)

    return {
        'label': label,
        'matrix_shape': (S, S * S),
        'numerical_rank': rank,
        'singular_values_top5': svs[:min(5, len(svs))].tolist(),
        'sv_ratio_2_to_1': sv_ratio,
        'per_b_ranks': per_b_ranks,
        'per_b_rank_mean': np.mean(per_b_ranks),
        'per_b_rank_min': min(per_b_ranks),
        'per_b_rank_max': max(per_b_ranks),
        'per_b_commutator_max': per_b_commutator_max,
        'per_b_commutator_mean': per_b_commutator_mean,
        'avg_over_b_commutator_max': np.mean(per_b_commutator_max),
        'avg_over_b_commutator_mean': np.mean(per_b_commutator_mean),
    }


# ============================================================
# 7. Main experiments
# ============================================================

def run_experiment_instance_scan():
    """
    Experiment 1: Instance-size scan at fixed arity k=3.
    Compare single-slot, multi-slot, and symmetrized constructions.
    """
    print("=" * 70)
    print("  EXPERIMENT 1: Instance-size scan (k=3 majority)")
    print("  Comparing: single-slot (K-14) vs multi-slot (2 live) vs symmetrized")
    print("=" * 70)

    n_values = [4, 6, 8, 10]
    k = 3
    results = []

    for n in n_values:
        print(f"\n{'#'*60}")
        print(f"  n = {n}, k = {k}")
        print(f"{'#'*60}")

        instance = generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4)
        if instance is None:
            print(f"  FAILED to generate instance at n={n}")
            continue

        n_vars, clauses, solutions = instance
        S = len(solutions)
        print(f"  Variables: {n_vars}, Clauses: {len(clauses)}, |Sol| = {S}")

        # Verify polymorphism
        is_poly, viol, total = verify_polymorphism_threshold_k(solutions, k)
        print(f"  Threshold-{k} polymorphism: {'PASS' if is_poly else 'FAIL'} ({viol}/{total} violations)")
        if not is_poly:
            print("  ERROR: threshold must be polymorphism for 2-SAT")
            continue

        t0 = time.time()

        # --- Single-slot (K-14 comparison) ---
        T_single = compute_T_singleslot(solutions, k)
        a_single = analyze_matrix(T_single, f"Single-slot k={k}")
        max_c_s, mean_c_s = compute_commutator_norms_matrix(T_single, S)

        # --- Multi-slot (2 live) ---
        T_multi, T_tensor = compute_T_multislot_2live(solutions, k)
        multi_analysis = analyze_multislot_rank(T_tensor, S, f"Multi-slot(2) k={k}")

        # --- Symmetrized ---
        T_sym = compute_T_symmetrized(solutions, k)
        a_sym = analyze_matrix(T_sym, f"Symmetrized k={k}")
        max_c_sym, mean_c_sym = compute_commutator_norms_matrix(T_sym, S)

        elapsed = time.time() - t0
        print(f"  Computation time: {elapsed:.1f}s")

        # Report
        print(f"\n  --- SINGLE-SLOT (K-14 baseline) ---")
        print(f"  Rank: {a_single['rank']}/{S}")
        print(f"  lambda_1={a_single['lambda_1']:.6f}, lambda_2={a_single['lambda_2']:.6f}, "
              f"lambda_min={a_single['lambda_min']:.6f}")
        print(f"  dev_scalar={a_single['deviation_from_scalar_I']:.6f}")
        print(f"  max||[T,y]||_2 = {max_c_s:.8f}")
        print(f"  mean||[T,y]||_2 = {mean_c_s:.8f}")

        print(f"\n  --- MULTI-SLOT (2 live) ---")
        print(f"  Matrix rank (SxS^2): {multi_analysis['numerical_rank']}/{S}")
        print(f"  SV ratio sigma_2/sigma_1: {multi_analysis['sv_ratio_2_to_1']:.6f}")
        print(f"  Top 5 singular values: {[f'{v:.6f}' for v in multi_analysis['singular_values_top5']]}")
        print(f"  Per-b ranks: min={multi_analysis['per_b_rank_min']}, "
              f"max={multi_analysis['per_b_rank_max']}, "
              f"mean={multi_analysis['per_b_rank_mean']:.1f}")
        print(f"  Avg over b: max||[T_b,y]||_2 = {multi_analysis['avg_over_b_commutator_max']:.8f}")
        print(f"  Avg over b: mean||[T_b,y]||_2 = {multi_analysis['avg_over_b_commutator_mean']:.8f}")

        print(f"\n  --- SYMMETRIZED ---")
        print(f"  Rank: {a_sym['rank']}/{S}")
        print(f"  lambda_1={a_sym['lambda_1']:.6f}, lambda_2={a_sym['lambda_2']:.6f}, "
              f"lambda_min={a_sym['lambda_min']:.6f}")
        print(f"  dev_scalar={a_sym['deviation_from_scalar_I']:.6f}")
        print(f"  max||[T_sym,y]||_2 = {max_c_sym:.8f}")
        print(f"  mean||[T_sym,y]||_2 = {mean_c_sym:.8f}")

        results.append({
            'n': n, 'S': S, 'k': k,
            'single_max_comm': max_c_s,
            'single_mean_comm': mean_c_s,
            'single_rank': a_single['rank'],
            'single_dev_scalar': a_single['deviation_from_scalar_I'],
            'single_lambda2': a_single['lambda_2'],
            'single_lambda_min': a_single['lambda_min'],
            'multi_rank': multi_analysis['numerical_rank'],
            'multi_sv_ratio': multi_analysis['sv_ratio_2_to_1'],
            'multi_per_b_rank_min': multi_analysis['per_b_rank_min'],
            'multi_per_b_rank_max': multi_analysis['per_b_rank_max'],
            'multi_avg_max_comm': multi_analysis['avg_over_b_commutator_max'],
            'multi_avg_mean_comm': multi_analysis['avg_over_b_commutator_mean'],
            'sym_max_comm': max_c_sym,
            'sym_mean_comm': mean_c_sym,
            'sym_rank': a_sym['rank'],
            'sym_dev_scalar': a_sym['deviation_from_scalar_I'],
            'sym_lambda2': a_sym['lambda_2'],
            'sym_lambda_min': a_sym['lambda_min'],
        })

    return results


def run_experiment_arity_scan():
    """
    Experiment 2: Arity scan at fixed instance size.
    k = 3, 5, 7, 9, 11 with threshold-k polymorphisms.
    Compare all three constructions.
    """
    print("\n\n" + "=" * 70)
    print("  EXPERIMENT 2: Arity scan (fixed instance, varying k)")
    print("  Comparing: single-slot vs multi-slot(2) vs symmetrized")
    print("=" * 70)

    # Use a moderate instance so computation is feasible
    n = 8
    instance = generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4)
    if instance is None:
        print("  FAILED to generate instance")
        return []

    n_vars, clauses, solutions = instance
    S = len(solutions)
    print(f"\n  Instance: n={n_vars}, clauses={len(clauses)}, |Sol|={S}")

    k_values = [3, 5, 7, 9, 11]
    results = []

    for k in k_values:
        print(f"\n{'#'*60}")
        print(f"  k = {k} (threshold-{k})")
        print(f"{'#'*60}")

        # Verify polymorphism
        is_poly, viol, total = verify_polymorphism_threshold_k(solutions, k)
        print(f"  Polymorphism: {'PASS' if is_poly else 'FAIL'} ({viol}/{total})")
        if not is_poly:
            print("  Threshold-k must be polymorphism for 2-SAT. Skipping.")
            continue

        t0 = time.time()

        # --- Single-slot ---
        T_single = compute_T_singleslot(solutions, k)
        a_single = analyze_matrix(T_single, f"Single k={k}")
        max_c_s, mean_c_s = compute_commutator_norms_matrix(T_single, S)

        # --- Multi-slot (2 live) ---
        mc_samples = min(S ** (k-2), 30000) if k > 3 else None
        T_multi, T_tensor = compute_T_multislot_2live(solutions, k,
                                                       num_mc_samples=mc_samples)
        multi_analysis = analyze_multislot_rank(T_tensor, S, f"Multi k={k}")

        # --- Symmetrized ---
        T_sym = compute_T_symmetrized(solutions, k)
        a_sym = analyze_matrix(T_sym, f"Sym k={k}")
        max_c_sym, mean_c_sym = compute_commutator_norms_matrix(T_sym, S)

        elapsed = time.time() - t0
        print(f"  Time: {elapsed:.1f}s")

        print(f"\n  Single-slot: rank={a_single['rank']}/{S}, "
              f"max||[T,y]||={max_c_s:.8f}, dev_scalar={a_single['deviation_from_scalar_I']:.6f}, "
              f"lambda_2={a_single['lambda_2']:.6f}, lambda_min={a_single['lambda_min']:.6f}")
        print(f"  Multi-slot:  SxS^2 rank={multi_analysis['numerical_rank']}/{S}, "
              f"sv_ratio={multi_analysis['sv_ratio_2_to_1']:.6f}, "
              f"per-b rank min/max={multi_analysis['per_b_rank_min']}/{multi_analysis['per_b_rank_max']}, "
              f"avg max||[T_b,y]||={multi_analysis['avg_over_b_commutator_max']:.8f}")
        print(f"  Symmetrized: rank={a_sym['rank']}/{S}, "
              f"max||[T,y]||={max_c_sym:.8f}, dev_scalar={a_sym['deviation_from_scalar_I']:.6f}, "
              f"lambda_2={a_sym['lambda_2']:.6f}, lambda_min={a_sym['lambda_min']:.6f}")

        results.append({
            'k': k, 'n': n, 'S': S,
            'single_max_comm': max_c_s,
            'single_mean_comm': mean_c_s,
            'single_rank': a_single['rank'],
            'single_dev_scalar': a_single['deviation_from_scalar_I'],
            'single_lambda2': a_single['lambda_2'],
            'single_lambda_min': a_single['lambda_min'],
            'multi_rank': multi_analysis['numerical_rank'],
            'multi_sv_ratio': multi_analysis['sv_ratio_2_to_1'],
            'multi_per_b_rank_min': multi_analysis['per_b_rank_min'],
            'multi_per_b_rank_max': multi_analysis['per_b_rank_max'],
            'multi_avg_max_comm': multi_analysis['avg_over_b_commutator_max'],
            'multi_avg_mean_comm': multi_analysis['avg_over_b_commutator_mean'],
            'sym_max_comm': max_c_sym,
            'sym_mean_comm': mean_c_sym,
            'sym_rank': a_sym['rank'],
            'sym_dev_scalar': a_sym['deviation_from_scalar_I'],
            'sym_lambda2': a_sym['lambda_2'],
            'sym_lambda_min': a_sym['lambda_min'],
        })

    return results


def run_experiment_second_instance_arity():
    """
    Experiment 3: Same arity scan on a SECOND instance (different random seed).
    Confirms the pattern is not instance-specific.
    """
    print("\n\n" + "=" * 70)
    print("  EXPERIMENT 3: Second-instance arity scan (confirmation)")
    print("=" * 70)

    # Different seed for the instance
    saved_state = random.getstate()
    random.seed(999)
    n = 8
    instance = generate_2sat_instance(n, clause_ratio=1.2, min_solutions=4)
    random.setstate(saved_state)

    if instance is None:
        print("  FAILED to generate second instance")
        return []

    n_vars, clauses, solutions = instance
    S = len(solutions)
    print(f"\n  Second instance: n={n_vars}, clauses={len(clauses)}, |Sol|={S}")

    k_values = [3, 5, 7, 9, 11]
    results = []

    for k in k_values:
        print(f"\n  --- k={k} ---")
        is_poly, viol, total = verify_polymorphism_threshold_k(solutions, k)
        if not is_poly:
            print(f"  Polymorphism FAIL. Skipping.")
            continue

        t0 = time.time()

        T_single = compute_T_singleslot(solutions, k)
        a_single = analyze_matrix(T_single)
        max_c_s, mean_c_s = compute_commutator_norms_matrix(T_single, S)

        mc_samples = min(S ** (k-2), 30000) if k > 3 else None
        T_multi, T_tensor = compute_T_multislot_2live(solutions, k,
                                                       num_mc_samples=mc_samples)
        multi_analysis = analyze_multislot_rank(T_tensor, S)

        T_sym = compute_T_symmetrized(solutions, k)
        a_sym = analyze_matrix(T_sym)
        max_c_sym, mean_c_sym = compute_commutator_norms_matrix(T_sym, S)

        elapsed = time.time() - t0
        print(f"  Time: {elapsed:.1f}s")

        print(f"  Single: max||[T,y]||={max_c_s:.8f}, rank={a_single['rank']}")
        print(f"  Multi:  avg_max||[T_b,y]||={multi_analysis['avg_over_b_commutator_max']:.8f}, "
              f"sv_ratio={multi_analysis['sv_ratio_2_to_1']:.6f}, rank={multi_analysis['numerical_rank']}")
        print(f"  Sym:    max||[T,y]||={max_c_sym:.8f}, rank={a_sym['rank']}")

        results.append({
            'k': k, 'n': n, 'S': S,
            'single_max_comm': max_c_s,
            'multi_avg_max_comm': multi_analysis['avg_over_b_commutator_max'],
            'multi_sv_ratio': multi_analysis['sv_ratio_2_to_1'],
            'multi_rank': multi_analysis['numerical_rank'],
            'sym_max_comm': max_c_sym,
            'sym_rank': a_sym['rank'],
            'sym_dev_scalar': a_sym['deviation_from_scalar_I'],
        })

    return results


# ============================================================
# 8. Synthesis and verdict
# ============================================================

def print_synthesis(inst_results, arity_results, arity2_results):
    """Print the final synthesis comparing all constructions."""
    print("\n\n" + "=" * 70)
    print("  SYNTHESIS: Multi-slot vs Single-slot vs Symmetrized")
    print("=" * 70)

    # --- Instance-size scaling table ---
    print("\n  TABLE 1: Instance-size scaling (k=3)")
    print(f"  {'n':>4s}  {'|Sol|':>5s}  "
          f"{'1-slot max':>12s}  {'2-slot avg':>12s}  {'sym max':>12s}  "
          f"{'2-slot rank':>11s}  {'sv_ratio':>8s}")
    print(f"  {'-'*4}  {'-'*5}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*11}  {'-'*8}")
    for r in inst_results:
        print(f"  {r['n']:4d}  {r['S']:5d}  "
              f"{r['single_max_comm']:12.8f}  "
              f"{r['multi_avg_max_comm']:12.8f}  "
              f"{r['sym_max_comm']:12.8f}  "
              f"{r['multi_rank']:4d}/{r['S']:4d}   "
              f"{r['multi_sv_ratio']:8.6f}")

    # --- Arity scaling table ---
    print("\n  TABLE 2: Arity scaling (fixed instance, primary)")
    print(f"  {'k':>4s}  {'|Sol|':>5s}  "
          f"{'1-slot max':>12s}  {'2-slot avg':>12s}  {'sym max':>12s}  "
          f"{'1-slot dev':>10s}  {'sym dev':>10s}  "
          f"{'sv_ratio':>8s}")
    print(f"  {'-'*4}  {'-'*5}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*8}")
    for r in arity_results:
        print(f"  {r['k']:4d}  {r['S']:5d}  "
              f"{r['single_max_comm']:12.8f}  "
              f"{r['multi_avg_max_comm']:12.8f}  "
              f"{r['sym_max_comm']:12.8f}  "
              f"{r['single_dev_scalar']:10.6f}  "
              f"{r['sym_dev_scalar']:10.6f}  "
              f"{r['multi_sv_ratio']:8.6f}")

    if arity2_results:
        print("\n  TABLE 3: Arity scaling (second instance, confirmation)")
        print(f"  {'k':>4s}  {'|Sol|':>5s}  "
              f"{'1-slot max':>12s}  {'2-slot avg':>12s}  {'sym max':>12s}  "
              f"{'sv_ratio':>8s}")
        print(f"  {'-'*4}  {'-'*5}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*8}")
        for r in arity2_results:
            print(f"  {r['k']:4d}  {r['S']:5d}  "
                  f"{r['single_max_comm']:12.8f}  "
                  f"{r['multi_avg_max_comm']:12.8f}  "
                  f"{r['sym_max_comm']:12.8f}  "
                  f"{r['multi_sv_ratio']:8.6f}")

    # --- Scaling analysis ---
    print("\n\n  SCALING ANALYSIS")
    print("  " + "-" * 60)

    if len(arity_results) >= 3:
        ks = np.array([r['k'] for r in arity_results], dtype=float)
        log_ks = np.log(ks)

        for label, key in [("Single-slot max||[T,y]||", 'single_max_comm'),
                           ("Multi-slot avg max||[T_b,y]||", 'multi_avg_max_comm'),
                           ("Symmetrized max||[T,y]||", 'sym_max_comm')]:
            vals = np.array([r[key] for r in arity_results])
            if all(v > 0 for v in vals):
                log_vals = np.log(vals)
                coeffs = np.polyfit(log_ks, log_vals, 1)
                slope = coeffs[0]
                r_squared = 1 - np.sum((log_vals - np.polyval(coeffs, log_ks))**2) / \
                            np.sum((log_vals - np.mean(log_vals))**2)

                direction = "INCREASING" if slope > 0.05 else ("DECREASING" if slope < -0.05 else "FLAT")
                print(f"  {label}:")
                print(f"    ~ k^{slope:+.4f}  (R^2 = {r_squared:.4f})  [{direction}]")

        # SV ratio trend (multi-slot specific)
        sv_ratios = [r['multi_sv_ratio'] for r in arity_results]
        print(f"\n  Multi-slot SV ratio sigma_2/sigma_1 trend:")
        for i, r in enumerate(arity_results):
            collapse = "RANK-1 COLLAPSE" if r['multi_sv_ratio'] < 0.01 else \
                       ("NEAR COLLAPSE" if r['multi_sv_ratio'] < 0.1 else "HEALTHY RANK")
            print(f"    k={r['k']:2d}: sigma_2/sigma_1 = {r['multi_sv_ratio']:.6f}  [{collapse}]")

    # --- Symmetrized specific analysis ---
    print("\n\n  SYMMETRIZED CONSTRUCTION ANALYSIS")
    print("  " + "-" * 60)
    if len(arity_results) >= 3:
        sym_devs = [r['sym_dev_scalar'] for r in arity_results]
        print(f"  Deviation from scalar * I with arity:")
        for r in arity_results:
            print(f"    k={r['k']:2d}: dev_scalar = {r['sym_dev_scalar']:.6f}")
        # Does symmetrization approach scalar?
        if sym_devs[-1] > sym_devs[0]:
            print(f"  Trend: INCREASING deviation from scalar (further from central)")
        elif sym_devs[-1] < sym_devs[0] * 0.5:
            print(f"  Trend: DECREASING deviation from scalar (approaching scalar = trivially central)")
        else:
            print(f"  Trend: ROUGHLY STABLE deviation from scalar")

    # --- Verdict ---
    print("\n\n" + "=" * 70)
    print("  VERDICT")
    print("=" * 70)

    # Check multi-slot
    if len(arity_results) >= 3:
        multi_comms = [r['multi_avg_max_comm'] for r in arity_results]
        multi_increasing = all(multi_comms[i] <= multi_comms[i+1] * 1.05
                               for i in range(len(multi_comms)-1))
        multi_decreasing = all(multi_comms[i] >= multi_comms[i+1] * 0.95
                               for i in range(len(multi_comms)-1))

        sym_comms = [r['sym_max_comm'] for r in arity_results]
        sym_increasing = all(sym_comms[i] <= sym_comms[i+1] * 1.05
                             for i in range(len(sym_comms)-1))
        sym_decreasing = all(sym_comms[i] >= sym_comms[i+1] * 0.95
                             for i in range(len(sym_comms)-1))

        sv_ratios = [r['multi_sv_ratio'] for r in arity_results]
        sv_collapsing = sv_ratios[-1] < sv_ratios[0] * 0.5

        single_comms = [r['single_max_comm'] for r in arity_results]

        print(f"\n  1. RANK-1 COLLAPSE (multi-slot):")
        if sv_collapsing:
            print(f"     SV ratio declines {sv_ratios[0]:.4f} -> {sv_ratios[-1]:.4f}: "
                  f"RANK COLLAPSE STILL OCCURS even with 2 live slots.")
            print(f"     The extra live slot DELAYS but does NOT PREVENT rank-1 collapse.")
        else:
            print(f"     SV ratio: {sv_ratios[0]:.4f} -> {sv_ratios[-1]:.4f}: "
                  f"NO rank-1 collapse. Multi-slot PREVENTS collapse.")

        print(f"\n  2. COMMUTATOR NORMS (arity scaling):")
        print(f"     Single-slot: {single_comms[0]:.6f} -> {single_comms[-1]:.6f} "
              f"({'INCREASING' if single_comms[-1] > single_comms[0] else 'DECREASING'})")
        print(f"     Multi-slot:  {multi_comms[0]:.6f} -> {multi_comms[-1]:.6f} "
              f"({'INCREASING' if multi_comms[-1] > multi_comms[0] else 'DECREASING'})")
        print(f"     Symmetrized: {sym_comms[0]:.6f} -> {sym_comms[-1]:.6f} "
              f"({'INCREASING' if sym_comms[-1] > sym_comms[0] else 'DECREASING'})")

        # Final verdict
        multi_saves = (not sv_collapsing) and multi_decreasing
        sym_saves = sym_decreasing and (sym_comms[-1] > 0.001)  # decreasing but non-trivial

        if multi_saves or sym_saves:
            which = []
            if multi_saves:
                which.append("multi-slot")
            if sym_saves:
                which.append("symmetrized")
            print(f"\n  VERDICT: CLOSES (via {' + '.join(which)})")
            print(f"  The multi-slot / symmetrized construction avoids K-14 rank-1 collapse")
            print(f"  and produces DECREASING commutator norms.")
            return "CLOSES"
        elif (not sv_collapsing) and (not multi_increasing):
            print(f"\n  VERDICT: INCONCLUSIVE")
            print(f"  Multi-slot prevents rank-1 collapse but commutator scaling is unclear.")
            print(f"  Need larger instances / arities to determine the trend.")
            return "INCONCLUSIVE"
        else:
            print(f"\n  VERDICT: KILLS (S4 multi-slot does not save Gap Alpha)")
            print(f"  Despite 2 live slots, the construction still exhibits:")
            if sv_collapsing:
                print(f"    - Rank collapse (SV ratio declining)")
            if not multi_decreasing:
                print(f"    - Non-decreasing commutator norms (multi-slot)")
            if not sym_decreasing:
                print(f"    - Non-decreasing commutator norms (symmetrized)")
            print(f"  K-14 extends to multi-slot constructions: the concentration of")
            print(f"  measure on the averaged slots dominates even with 2 live slots.")
            return "KILLS"
    else:
        print("\n  INSUFFICIENT DATA for verdict.")
        return "INCONCLUSIVE"


# ============================================================
# 9. Entry point
# ============================================================

def main():
    print("=" * 70)
    print("  GAP ALPHA MULTI-SLOT CONSTRUCTION -- Node 1.3.5.2")
    print("  Salvage S4: 2 live slots + (k-2) averaged")
    print("  Author: Claude Opus 4.6 (1M context)")
    print("  Date: 2026-04-11")
    print("=" * 70)
    print()
    print("  K-14 context: single-slot T_f with 1 live + (k-1) averaged")
    print("  produces rank-1 collapse. This script tests whether 2 live slots")
    print("  (and symmetrized construction) prevent the collapse.")
    print()

    # Run all experiments
    inst_results = run_experiment_instance_scan()
    arity_results = run_experiment_arity_scan()
    arity2_results = run_experiment_second_instance_arity()

    # Synthesis and verdict
    verdict = print_synthesis(inst_results, arity_results, arity2_results)

    print(f"\n\n  FINAL STATUS: {verdict}")
    print(f"  Node 1.3.5.2 complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
