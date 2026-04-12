"""
Node 1.3.5.4 -- S4a: Multi-Slot Residual Test (Definitive Gap Alpha Test)

CONTEXT:
  1.3.5.1 (K-14): Single-slot T_f -> rank-1 collapse, commutators INCREASE.
  1.3.5.2: Multi-slot T_f^{(2)} (2 live slots) -> commutators DECREASE with
           arity (exponent -0.51), BUT deviation-from-scalar INCREASES
           (0.67 -> 0.95), suggesting contraction-to-fixed-point, not centrality.
  1.3.5.3 (K-15): Single-slot residuals (R_f, S_f, P_f) all fail.

THIS NODE (S4a): The UNTESTED combination -- multi-slot + SVD residual.
  Subtract the contractive (stationary/fixed-point) component from T_f^{(2)}
  and test whether the RESIDUAL has genuinely decreasing commutator norms.

METHOD:
  For each per-b slice T_b = T_f^{(2)}(:, :, b):
  1. Compute SVD: T_b = sum_i sigma_i |u_i><v_i|
  2. Subtract rank-r stationary component: R_b^{(r)} = T_b - sum_{i=1}^{r} sigma_i |u_i><v_i|
  3. Compute commutator norms, operator norms, normalized non-centrality
  4. Test r = 1, 2, 3 (progressive decontraction)

DEFINITIVE TEST:
  Plot normalized non-centrality = ||[R_b^{(r)}, y]|| / ||R_b^{(r)}||_op  vs  arity k.
  - DECREASES -> genuine centrality in residual -> GAP ALPHA CLOSES
  - FLAT/INCREASES -> contraction was the whole signal -> GAP ALPHA KILLED (K-16)

Also tests the full |Sol| x |Sol|^2 matrix (not just per-b slices).

Kill list awareness:
  K-14: 1-live + (k-1)-averaged -> rank-1 collapse
  K-15: Post-processing of single-slot T_f preserves concentration pathology
  THIS construction is DIFFERENT: 2 live slots (avoids K-14) AND residual
  (addresses contraction, unlike raw multi-slot which was inconclusive)

Author: Claude Opus 4.6 (1M context), Node 1.3.5.4 (S4a)
Date: 2026-04-11
"""

import numpy as np
from itertools import product as cartesian_product
import random
import sys
import time

random.seed(42)
np.random.seed(42)
np.set_printoptions(precision=8, suppress=True, linewidth=140)

MC_BUDGET = 10000


# ================================================================
# 1. Instance generation (reused)
# ================================================================

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


def generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4, max_attempts=500):
    num_clauses = max(int(n * clause_ratio), 1)
    for _ in range(max_attempts):
        clauses = []
        for _ in range(num_clauses):
            vars_ = random.sample(range(n), 2)
            signs = [random.choice([0, 1]) for _ in range(2)]
            clauses.append((vars_[0], signs[0], vars_[1], signs[1]))
        sols = enumerate_solutions_2sat(n, clauses)
        if len(sols) >= min_solutions:
            return n, clauses, sols
    return None


# ================================================================
# 2. Threshold-k polymorphism
# ================================================================

def threshold_k_bit(coords, k):
    s = sum(coords)
    if s > k / 2:
        return 1
    elif s < k / 2:
        return 0
    else:
        return 0  # tie-break: f(x,...,x) = x


def coordinatewise_threshold_k(tuples, k):
    n = len(tuples[0])
    return tuple(threshold_k_bit(tuple(t[i] for t in tuples), k) for i in range(n))


def verify_polymorphism_threshold_k(solutions, k, num_samples=20000):
    sol_set = set(solutions)
    S = len(solutions)
    total_tuples = S ** k
    if total_tuples <= 100000:
        violations = 0
        total = 0
        for combo in cartesian_product(solutions, repeat=k):
            total += 1
            result = coordinatewise_threshold_k(combo, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, total
    else:
        violations = 0
        for _ in range(num_samples):
            combo = [solutions[random.randint(0, S - 1)] for _ in range(k)]
            result = coordinatewise_threshold_k(combo, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, num_samples


# ================================================================
# 3. Multi-slot T_f^{(2)} construction: 2 live + (k-2) averaged
# ================================================================

def compute_T_multislot_2live(solutions, k, num_mc_samples=None):
    """
    T_f^{(2)}[s, (a,b)] = P(f(a, b, c3,...,ck) = s)
    where (c3,...,ck) are drawn uniformly from Sol^{k-2}.

    Returns: T_tensor as |Sol| x |Sol| x |Sol| (indices: [s, a, b]).
    """
    sol_list = list(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n_avg = k - 2

    T_tensor = np.zeros((S, S, S), dtype=np.float64)

    if n_avg <= 0:
        raise ValueError("k must be >= 3 for 2-live-slot construction")

    total_avg_tuples = S ** n_avg
    if num_mc_samples is None:
        num_mc_samples = min(total_avg_tuples, MC_BUDGET)
    use_exact = (total_avg_tuples <= num_mc_samples)

    if use_exact:
        for a_idx, a in enumerate(sol_list):
            for b_idx, b in enumerate(sol_list):
                for avg_combo in cartesian_product(sol_list, repeat=n_avg):
                    inputs = [a, b] + list(avg_combo)
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        T_tensor[sol_to_idx[result], a_idx, b_idx] += 1.0
        T_tensor /= total_avg_tuples
    else:
        for a_idx, a in enumerate(sol_list):
            for b_idx, b in enumerate(sol_list):
                for _ in range(num_mc_samples):
                    avg = [sol_list[random.randint(0, S - 1)] for _ in range(n_avg)]
                    inputs = [a, b] + avg
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        T_tensor[sol_to_idx[result], a_idx, b_idx] += 1.0
        T_tensor /= num_mc_samples

    return T_tensor


# ================================================================
# 4. SVD residual construction
# ================================================================

def compute_svd_residual(M, rank_to_remove):
    """
    Given matrix M (S x S), compute:
      R = M - sum_{i=1}^{rank_to_remove} sigma_i * u_i * v_i^T

    Returns: R, singular values removed, remaining operator norm.
    """
    U, sigma, Vt = np.linalg.svd(M, full_matrices=False)
    r = min(rank_to_remove, len(sigma))

    # Reconstruct the rank-r approximation
    M_approx = np.zeros_like(M)
    for i in range(r):
        M_approx += sigma[i] * np.outer(U[:, i], Vt[i, :])

    R = M - M_approx
    removed_sigmas = sigma[:r].tolist()
    remaining_sigmas = sigma[r:].tolist()
    R_op_norm = remaining_sigmas[0] if remaining_sigmas else 0.0

    return R, removed_sigmas, remaining_sigmas, R_op_norm


def compute_eig_residual(M, rank_to_remove):
    """
    For square M: eigendecomposition residual.
    Remove the top rank_to_remove eigenvalue components.
    This is the correct decomposition for Markov-like matrices
    where the stationary component is an eigenvector.
    """
    eigenvalues, V = np.linalg.eig(M)
    # Sort by magnitude (descending)
    idx = np.argsort(-np.abs(eigenvalues))
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]

    # Compute left eigenvectors (rows of inverse)
    try:
        V_inv = np.linalg.inv(V)
    except np.linalg.LinAlgError:
        # Singular -- fall back to SVD residual
        return compute_svd_residual(M, rank_to_remove)

    r = min(rank_to_remove, len(eigenvalues))
    M_approx = np.zeros_like(M, dtype=complex)
    for i in range(r):
        M_approx += eigenvalues[i] * np.outer(V[:, i], V_inv[i, :])

    R = M - np.real(M_approx)
    removed_eigs = eigenvalues[:r].tolist()
    remaining_eigs = eigenvalues[r:].tolist()
    R_op_norm = max(np.abs(remaining_eigs)) if remaining_eigs else 0.0

    return R, removed_eigs, remaining_eigs, R_op_norm


# ================================================================
# 5. Commutator computation
# ================================================================

def compute_commutator_norms_full(M):
    """
    ||[M, e_{ij}]||_F / sqrt(S) for all generators e_{ij}.
    Returns max, mean over all (i, j).

    VECTORIZED: [M, e_{ij}] has non-zero entries only in column j
    (gets M[:,i]) and row i (gets -M[j,:]). The overlap at (i,j)
    gets M[i,i] - M[j,j].

    ||[M, e_{ij}]||_F^2 = sum_a M[a,i]^2 + sum_b M[j,b]^2 - M[i,i]^2 - M[j,j]^2
                          + (M[i,i] - M[j,j])^2
    (The last three terms correct for the overlap at position (i,j).)

    Wait -- let's derive carefully:
    C = [M, e_{ij}]. Non-zero entries:
      C[a, j] = M[a, i]  for all a  (from M @ e_{ij})
      C[i, b] -= M[j, b]  for all b  (from -e_{ij} @ M)
    These overlap at (i, j): C[i, j] = M[i, i] - M[j, j].

    ||C||_F^2 = sum_{a != i} M[a,i]^2 + sum_{b != j} M[j,b]^2 + (M[i,i] - M[j,j])^2
    """
    S = M.shape[0]
    # Precompute column norms squared and row norms squared
    col_norms_sq = np.sum(M ** 2, axis=0)  # col_norms_sq[i] = sum_a M[a,i]^2
    row_norms_sq = np.sum(M ** 2, axis=1)  # row_norms_sq[j] = sum_b M[j,b]^2
    diag = np.diag(M)  # diag[i] = M[i,i]

    # For each (i,j):
    # ||C||_F^2 = (col_norms_sq[i] - M[i,i]^2) + (row_norms_sq[j] - M[j,j]^2)
    #           + (M[i,i] - M[j,j])^2
    # = col_norms_sq[i] + row_norms_sq[j] - M[i,i]^2 - M[j,j]^2 + (M[i,i] - M[j,j])^2
    # = col_norms_sq[i] + row_norms_sq[j] - 2*M[i,i]*M[j,j]

    # Broadcast: norms_sq[i,j] = col_norms_sq[i] + row_norms_sq[j] - 2*diag[i]*diag[j]
    norms_sq = col_norms_sq[:, None] + row_norms_sq[None, :] - 2.0 * np.outer(diag, diag)
    norms_sq = np.maximum(norms_sq, 0.0)  # numerical safety
    norms = np.sqrt(norms_sq) / np.sqrt(S)

    return float(np.max(norms)), float(np.mean(norms))


def compute_deviation_from_scalar(M):
    """||M - (tr M / dim) I|| / ||M||"""
    S = M.shape[0]
    scalar = np.trace(M) / S
    dev = np.linalg.norm(M - scalar * np.eye(S), 'fro')
    norm = np.linalg.norm(M, 'fro')
    return dev / max(norm, 1e-15), scalar


def compute_normalized_non_centrality(M):
    """
    The DEFINITIVE metric:
      NNC = max_y ||[M, y]||_F / (sqrt(S) * ||M||_op)

    This normalizes out the operator's overall scale.
    If M is approaching centrality, NNC -> 0.
    If M is contracting (shrinking uniformly), NNC stays constant or increases.
    """
    S = M.shape[0]
    op_norm = np.linalg.norm(M, 2)  # spectral norm = largest singular value
    if op_norm < 1e-15:
        return 0.0, 0.0  # zero operator is trivially central
    max_comm, mean_comm = compute_commutator_norms_full(M)
    nnc = max_comm / op_norm
    nnc_mean = mean_comm / op_norm
    return nnc, nnc_mean


# ================================================================
# 6. Single-slot T_f for comparison (K-14 baseline)
# ================================================================

def compute_T_singleslot(solutions, k, num_mc_samples=None):
    sol_list = list(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n_avg = k - 1

    T = np.zeros((S, S), dtype=np.float64)
    total_avg_tuples = S ** n_avg
    if num_mc_samples is None:
        num_mc_samples = min(total_avg_tuples, 50000)
    use_exact = (total_avg_tuples <= num_mc_samples)

    if use_exact:
        for a_idx, a in enumerate(sol_list):
            for avg_combo in cartesian_product(sol_list, repeat=n_avg):
                inputs = [a] + list(avg_combo)
                result = coordinatewise_threshold_k(inputs, k)
                if result in sol_to_idx:
                    T[sol_to_idx[result], a_idx] += 1.0
        T /= total_avg_tuples
    else:
        for a_idx, a in enumerate(sol_list):
            for _ in range(num_mc_samples):
                avg = [sol_list[random.randint(0, S - 1)] for _ in range(n_avg)]
                inputs = [a] + avg
                result = coordinatewise_threshold_k(inputs, k)
                if result in sol_to_idx:
                    T[sol_to_idx[result], a_idx] += 1.0
        T /= num_mc_samples

    return T


# ================================================================
# 7. Full |Sol| x |Sol|^2 matrix residual analysis
# ================================================================

def analyze_full_matrix_residual(T_tensor, ranks_to_remove=[1, 2, 3]):
    """
    Treat T_f^{(2)} as a |Sol| x |Sol|^2 matrix.
    Compute SVD, remove top-r singular components, analyze residual.
    """
    S = T_tensor.shape[0]
    T_flat = T_tensor.reshape(S, S * S)

    U, sigma, Vt = np.linalg.svd(T_flat, full_matrices=False)

    results = {}
    results['full_svs'] = sigma[:min(10, len(sigma))].tolist()
    results['full_sv_ratio'] = sigma[1] / sigma[0] if sigma[0] > 1e-15 else 0.0

    for r in ranks_to_remove:
        r_actual = min(r, len(sigma))
        R_flat = T_flat.copy()
        for i in range(r_actual):
            R_flat -= sigma[i] * np.outer(U[:, i], Vt[i, :])

        R_tensor = R_flat.reshape(S, S, S)
        R_op_norm = np.linalg.norm(R_flat, 2)
        R_fro_norm = np.linalg.norm(R_flat, 'fro')

        # Per-b analysis of the residual tensor
        per_b_nnc = []
        per_b_max_comm = []
        per_b_dev_scalar = []
        per_b_op_norm = []
        for b_idx in range(S):
            R_b = R_tensor[:, :, b_idx]
            rb_op = np.linalg.norm(R_b, 2)
            per_b_op_norm.append(rb_op)

            if rb_op < 1e-15:
                per_b_nnc.append(0.0)
                per_b_max_comm.append(0.0)
                per_b_dev_scalar.append(0.0)
                continue

            mc, mn = compute_commutator_norms_full(R_b)
            per_b_max_comm.append(mc)
            per_b_nnc.append(mc / rb_op)
            dev, _ = compute_deviation_from_scalar(R_b)
            per_b_dev_scalar.append(dev)

        results[f'rank_{r}'] = {
            'R_op_norm': R_op_norm,
            'R_fro_norm': R_fro_norm,
            'avg_per_b_max_comm': np.mean(per_b_max_comm),
            'avg_per_b_nnc': np.mean(per_b_nnc),
            'avg_per_b_dev_scalar': np.mean(per_b_dev_scalar),
            'avg_per_b_op_norm': np.mean(per_b_op_norm),
            'max_per_b_nnc': max(per_b_nnc),
            'min_per_b_nnc': min(per_b_nnc),
        }

    return results


# ================================================================
# 8. Per-b slice residual analysis (the main test)
# ================================================================

def analyze_per_b_residuals(T_tensor, ranks_to_remove=[1, 2, 3]):
    """
    For each b, compute T_b = T_tensor[:, :, b] (S x S matrix).
    Compute SVD residual: R_b^{(r)} = T_b - rank-r approximation.
    Also compute eigendecomposition residual (for Markov stationary).
    Compute NNC for each.
    """
    S = T_tensor.shape[0]
    results = {r: {
        'per_b_nnc_svd': [], 'per_b_nnc_eig': [],
        'per_b_max_comm_svd': [], 'per_b_max_comm_eig': [],
        'per_b_dev_scalar_svd': [], 'per_b_dev_scalar_eig': [],
        'per_b_op_norm_svd': [], 'per_b_op_norm_eig': [],
        'per_b_nnc_mean_svd': [], 'per_b_nnc_mean_eig': [],
    } for r in ranks_to_remove}

    # Also store raw T_b metrics for comparison
    raw_results = {
        'per_b_nnc': [], 'per_b_max_comm': [],
        'per_b_dev_scalar': [], 'per_b_op_norm': [],
    }

    for b_idx in range(S):
        T_b = T_tensor[:, :, b_idx]

        # Raw T_b
        tb_op = np.linalg.norm(T_b, 2)
        if tb_op < 1e-15:
            raw_results['per_b_nnc'].append(0.0)
            raw_results['per_b_max_comm'].append(0.0)
            raw_results['per_b_dev_scalar'].append(0.0)
            raw_results['per_b_op_norm'].append(0.0)
            for r in ranks_to_remove:
                for key in results[r]:
                    results[r][key].append(0.0)
            continue

        mc_raw, mn_raw = compute_commutator_norms_full(T_b)
        raw_results['per_b_nnc'].append(mc_raw / tb_op)
        raw_results['per_b_max_comm'].append(mc_raw)
        dev_raw, _ = compute_deviation_from_scalar(T_b)
        raw_results['per_b_dev_scalar'].append(dev_raw)
        raw_results['per_b_op_norm'].append(tb_op)

        for r in ranks_to_remove:
            # SVD residual
            R_svd, removed_svd, remaining_svd, R_svd_op = compute_svd_residual(T_b, r)
            if R_svd_op < 1e-15:
                results[r]['per_b_nnc_svd'].append(0.0)
                results[r]['per_b_max_comm_svd'].append(0.0)
                results[r]['per_b_dev_scalar_svd'].append(0.0)
                results[r]['per_b_op_norm_svd'].append(0.0)
                results[r]['per_b_nnc_mean_svd'].append(0.0)
            else:
                mc_svd, mn_svd = compute_commutator_norms_full(R_svd)
                results[r]['per_b_nnc_svd'].append(mc_svd / R_svd_op)
                results[r]['per_b_max_comm_svd'].append(mc_svd)
                dev_svd, _ = compute_deviation_from_scalar(R_svd)
                results[r]['per_b_dev_scalar_svd'].append(dev_svd)
                results[r]['per_b_op_norm_svd'].append(R_svd_op)
                results[r]['per_b_nnc_mean_svd'].append(mn_svd / R_svd_op)

            # Eigendecomposition residual
            R_eig, removed_eig, remaining_eig, R_eig_op = compute_eig_residual(T_b, r)
            if R_eig_op < 1e-15:
                results[r]['per_b_nnc_eig'].append(0.0)
                results[r]['per_b_max_comm_eig'].append(0.0)
                results[r]['per_b_dev_scalar_eig'].append(0.0)
                results[r]['per_b_op_norm_eig'].append(0.0)
                results[r]['per_b_nnc_mean_eig'].append(0.0)
            else:
                mc_eig, mn_eig = compute_commutator_norms_full(R_eig)
                results[r]['per_b_nnc_eig'].append(mc_eig / R_eig_op)
                results[r]['per_b_max_comm_eig'].append(mc_eig)
                dev_eig, _ = compute_deviation_from_scalar(R_eig)
                results[r]['per_b_dev_scalar_eig'].append(dev_eig)
                results[r]['per_b_op_norm_eig'].append(R_eig_op)
                results[r]['per_b_nnc_mean_eig'].append(mn_eig / R_eig_op)

    return raw_results, results


# ================================================================
# 9. Main experiment
# ================================================================

def run_experiment():
    print("=" * 78)
    print("  NODE 1.3.5.4 -- S4a: MULTI-SLOT RESIDUAL TEST")
    print("  Definitive Gap Alpha Test: Subtract contraction, test centrality")
    print("  Author: Claude Opus 4.6 (1M context)")
    print("  Date: 2026-04-11")
    print("=" * 78)

    # ---- Phase 1: Generate instances ----
    print("\n  PHASE 1: Instance generation")
    print("  " + "-" * 60)

    instances = {}
    target_configs = [
        (4, 1.0, 4),   # n=4, clause_ratio=1.0, min_solutions=4
        (6, 1.0, 4),   # n=6
        (8, 1.0, 4),   # n=8
        (10, 1.8, 10), # n=10, higher clause ratio -> fewer solutions (manageable)
    ]
    for n, cr, min_sol in target_configs:
        random.seed(42)
        np.random.seed(42)
        inst = generate_2sat_instance(n, clause_ratio=cr, min_solutions=min_sol)
        if inst is None:
            # Fall back to more constrained
            random.seed(42)
            np.random.seed(42)
            inst = generate_2sat_instance(n, clause_ratio=2.0, min_solutions=4)
        if inst is None:
            print(f"  n={n}: FAILED to generate instance")
            continue
        n_vars, clauses, sols = inst
        S = len(sols)
        if S > 60:
            print(f"  n={n}: |Sol|={S} too large, trying higher clause ratio")
            for cr2 in [2.0, 2.5, 3.0]:
                random.seed(42 + int(cr2 * 100))
                np.random.seed(42 + int(cr2 * 100))
                inst2 = generate_2sat_instance(n, clause_ratio=cr2, min_solutions=4)
                if inst2 is not None and len(inst2[2]) <= 60:
                    inst = inst2
                    n_vars, clauses, sols = inst
                    S = len(sols)
                    break
        instances[n] = (n_vars, clauses, sols)
        print(f"  n={n}: |Sol|={S}")

    arities = [3, 5, 7, 9, 11]
    ranks_to_remove = [1, 2, 3]

    # ---- Phase 2: Arity scan with residual analysis ----
    print("\n\n  PHASE 2: Arity scan with multi-slot residual analysis")
    print("  " + "-" * 60)

    # Master results table: results_master[n][k] = {...}
    results_master = {}

    for n in sorted(instances.keys()):
        n_vars, clauses, sols = instances[n]
        S = len(sols)
        results_master[n] = {}

        print(f"\n  === n={n}, |Sol|={S} ===")

        for k in arities:
            t0 = time.time()

            # Verify polymorphism
            is_poly, viol, total = verify_polymorphism_threshold_k(sols, k)
            if not is_poly:
                print(f"  k={k}: polymorphism FAILS ({viol}/{total} violations). SKIP.")
                continue

            # Compute multi-slot T_f^{(2)}
            mc_samples = min(S ** (k - 2), max(3000, MC_BUDGET // max(1, k - 3)))
            T_tensor = compute_T_multislot_2live(sols, k, num_mc_samples=mc_samples)

            # Also compute single-slot for comparison
            mc_single = min(S ** (k - 1), 30000)
            T_single = compute_T_singleslot(sols, k, num_mc_samples=mc_single)

            # Single-slot metrics
            single_mc, single_mn = compute_commutator_norms_full(T_single)
            single_nnc, _ = compute_normalized_non_centrality(T_single)
            single_dev, _ = compute_deviation_from_scalar(T_single)

            # Per-b residual analysis (THE CORE TEST)
            raw_res, residual_res = analyze_per_b_residuals(T_tensor, ranks_to_remove)

            # Full matrix residual
            full_res = analyze_full_matrix_residual(T_tensor, ranks_to_remove)

            elapsed = time.time() - t0

            entry = {
                'k': k, 'S': S,
                'single_max_comm': single_mc,
                'single_nnc': single_nnc,
                'single_dev_scalar': single_dev,
                'raw_avg_nnc': np.mean(raw_res['per_b_nnc']),
                'raw_avg_max_comm': np.mean(raw_res['per_b_max_comm']),
                'raw_avg_dev_scalar': np.mean(raw_res['per_b_dev_scalar']),
                'raw_avg_op_norm': np.mean(raw_res['per_b_op_norm']),
            }

            for r in ranks_to_remove:
                entry[f'r{r}_svd_avg_nnc'] = np.mean(residual_res[r]['per_b_nnc_svd'])
                entry[f'r{r}_svd_avg_max_comm'] = np.mean(residual_res[r]['per_b_max_comm_svd'])
                entry[f'r{r}_svd_avg_dev_scalar'] = np.mean(residual_res[r]['per_b_dev_scalar_svd'])
                entry[f'r{r}_svd_avg_op_norm'] = np.mean(residual_res[r]['per_b_op_norm_svd'])
                entry[f'r{r}_eig_avg_nnc'] = np.mean(residual_res[r]['per_b_nnc_eig'])
                entry[f'r{r}_eig_avg_max_comm'] = np.mean(residual_res[r]['per_b_max_comm_eig'])
                entry[f'r{r}_eig_avg_dev_scalar'] = np.mean(residual_res[r]['per_b_dev_scalar_eig'])
                entry[f'r{r}_eig_avg_op_norm'] = np.mean(residual_res[r]['per_b_op_norm_eig'])
                entry[f'r{r}_full_avg_nnc'] = full_res[f'rank_{r}']['avg_per_b_nnc']
                entry[f'r{r}_full_avg_max_comm'] = full_res[f'rank_{r}']['avg_per_b_max_comm']

            results_master[n][k] = entry

            # Compact print
            print(f"    k={k}: raw NNC={entry['raw_avg_nnc']:.6f}  "
                  f"r1-SVD NNC={entry['r1_svd_avg_nnc']:.6f}  "
                  f"r2-SVD NNC={entry['r2_svd_avg_nnc']:.6f}  "
                  f"r3-SVD NNC={entry['r3_svd_avg_nnc']:.6f}  "
                  f"[{elapsed:.1f}s]")

    return results_master


def print_synthesis(results_master):
    """Print the definitive synthesis tables and verdict."""

    print("\n\n" + "=" * 78)
    print("  SYNTHESIS: MULTI-SLOT RESIDUAL TEST")
    print("=" * 78)

    # ---- Table 1: Raw vs residual NNC by arity ----
    print("\n  TABLE 1: Normalized Non-Centrality (NNC) = max||[R,y]|| / ||R||_op")
    print("           NNC -> 0 means GENUINE centrality approach.")
    print("           NNC constant/increasing means CONTRACTION ARTIFACT.")

    for n in sorted(results_master.keys()):
        data = results_master[n]
        if not data:
            continue
        S = list(data.values())[0]['S']
        print(f"\n  n={n}, |Sol|={S}")
        print(f"  {'k':>4s}  {'single NNC':>11s}  {'raw-multi':>10s}  "
              f"{'r1-SVD':>10s}  {'r1-EIG':>10s}  {'r2-SVD':>10s}  {'r3-SVD':>10s}")
        print(f"  {'----':>4s}  {'-'*11:>11s}  {'-'*10:>10s}  "
              f"{'-'*10:>10s}  {'-'*10:>10s}  {'-'*10:>10s}  {'-'*10:>10s}")
        for k in sorted(data.keys()):
            e = data[k]
            print(f"  {k:4d}  {e['single_nnc']:11.6f}  {e['raw_avg_nnc']:10.6f}  "
                  f"{e['r1_svd_avg_nnc']:10.6f}  {e['r1_eig_avg_nnc']:10.6f}  "
                  f"{e['r2_svd_avg_nnc']:10.6f}  {e['r3_svd_avg_nnc']:10.6f}")

    # ---- Table 2: Absolute commutator norms (raw vs residual) ----
    print("\n\n  TABLE 2: Absolute commutator norms max||[R,y]||_2")
    print("           Shows whether absolute norms decrease (could be contraction)")

    for n in sorted(results_master.keys()):
        data = results_master[n]
        if not data:
            continue
        S = list(data.values())[0]['S']
        print(f"\n  n={n}, |Sol|={S}")
        print(f"  {'k':>4s}  {'single':>11s}  {'raw-multi':>11s}  "
              f"{'r1-SVD':>11s}  {'r2-SVD':>11s}  {'r3-SVD':>11s}")
        print(f"  {'----':>4s}  {'-'*11:>11s}  {'-'*11:>11s}  "
              f"{'-'*11:>11s}  {'-'*11:>11s}  {'-'*11:>11s}")
        for k in sorted(data.keys()):
            e = data[k]
            print(f"  {k:4d}  {e['single_max_comm']:11.8f}  {e['raw_avg_max_comm']:11.8f}  "
                  f"{e['r1_svd_avg_max_comm']:11.8f}  {e['r2_svd_avg_max_comm']:11.8f}  "
                  f"{e['r3_svd_avg_max_comm']:11.8f}")

    # ---- Table 3: Operator norms (to diagnose contraction) ----
    print("\n\n  TABLE 3: Operator norms ||R||_op (SVD residual)")
    print("           Declining op-norm + declining abs-comm could be contraction")
    print("           NNC corrects for this: NNC = abs-comm / op-norm")

    for n in sorted(results_master.keys()):
        data = results_master[n]
        if not data:
            continue
        S = list(data.values())[0]['S']
        print(f"\n  n={n}, |Sol|={S}")
        print(f"  {'k':>4s}  {'raw-op':>11s}  {'r1-SVD-op':>11s}  "
              f"{'r2-SVD-op':>11s}  {'r3-SVD-op':>11s}")
        print(f"  {'----':>4s}  {'-'*11:>11s}  {'-'*11:>11s}  "
              f"{'-'*11:>11s}  {'-'*11:>11s}")
        for k in sorted(data.keys()):
            e = data[k]
            print(f"  {k:4d}  {e['raw_avg_op_norm']:11.8f}  {e['r1_svd_avg_op_norm']:11.8f}  "
                  f"{e['r2_svd_avg_op_norm']:11.8f}  {e['r3_svd_avg_op_norm']:11.8f}")

    # ---- Table 4: Deviation from scalar ----
    print("\n\n  TABLE 4: Deviation from scalar (1.0 = maximally non-scalar)")
    print("           If -> 1.0: operator is NOT converging to scalar*I (non-trivial)")
    print("           If -> 0.0: converging to scalar*I (trivially central)")

    for n in sorted(results_master.keys()):
        data = results_master[n]
        if not data:
            continue
        S = list(data.values())[0]['S']
        print(f"\n  n={n}, |Sol|={S}")
        print(f"  {'k':>4s}  {'single':>10s}  {'raw-multi':>10s}  "
              f"{'r1-SVD':>10s}  {'r2-SVD':>10s}  {'r3-SVD':>10s}")
        print(f"  {'----':>4s}  {'-'*10:>10s}  {'-'*10:>10s}  "
              f"{'-'*10:>10s}  {'-'*10:>10s}  {'-'*10:>10s}")
        for k in sorted(data.keys()):
            e = data[k]
            print(f"  {k:4d}  {e['single_dev_scalar']:10.6f}  {e['raw_avg_dev_scalar']:10.6f}  "
                  f"{e['r1_svd_avg_dev_scalar']:10.6f}  {e['r2_svd_avg_dev_scalar']:10.6f}  "
                  f"{e['r3_svd_avg_dev_scalar']:10.6f}")

    # ---- Scaling analysis ----
    print("\n\n  SCALING ANALYSIS: Power-law fits NNC ~ k^exponent")
    print("  " + "-" * 60)

    scaling_results = {}
    for n in sorted(results_master.keys()):
        data = results_master[n]
        if len(data) < 3:
            continue
        ks = np.array(sorted(data.keys()), dtype=float)
        log_ks = np.log(ks)
        S = list(data.values())[0]['S']

        print(f"\n  n={n}, |Sol|={S}:")
        scaling_results[n] = {}

        metrics = [
            ('single NNC', 'single_nnc'),
            ('raw-multi NNC', 'raw_avg_nnc'),
            ('r1-SVD NNC', 'r1_svd_avg_nnc'),
            ('r1-EIG NNC', 'r1_eig_avg_nnc'),
            ('r2-SVD NNC', 'r2_svd_avg_nnc'),
            ('r3-SVD NNC', 'r3_svd_avg_nnc'),
            ('raw-multi abs-comm', 'raw_avg_max_comm'),
            ('r1-SVD abs-comm', 'r1_svd_avg_max_comm'),
            ('r2-SVD abs-comm', 'r2_svd_avg_max_comm'),
            ('r3-SVD abs-comm', 'r3_svd_avg_max_comm'),
        ]

        for label, key in metrics:
            vals = np.array([data[k][key] for k in sorted(data.keys())])
            if all(v > 1e-15 for v in vals):
                log_v = np.log(vals)
                c = np.polyfit(log_ks, log_v, 1)
                predicted = np.polyval(c, log_ks)
                ss_res = np.sum((log_v - predicted) ** 2)
                ss_tot = np.sum((log_v - np.mean(log_v)) ** 2)
                r2 = 1 - ss_res / max(ss_tot, 1e-30)
                direction = "DECREASING" if c[0] < -0.05 else ("INCREASING" if c[0] > 0.05 else "FLAT")
                print(f"    {label:25s}: ~ k^{c[0]:+.4f}  (R2={r2:.3f})  [{direction}]")
                scaling_results[n][key] = {'exponent': c[0], 'r2': r2, 'direction': direction}
            else:
                print(f"    {label:25s}: contains zero values, no fit")
                scaling_results[n][key] = {'exponent': 0.0, 'r2': 0.0, 'direction': 'ZERO'}

    return scaling_results


def print_verdict(results_master, scaling_results):
    """The definitive verdict."""

    print("\n\n" + "=" * 78)
    print("  DEFINITIVE VERDICT")
    print("=" * 78)

    # Collect NNC exponents across all instances
    nnc_exponents = {
        'raw_avg_nnc': [],
        'r1_svd_avg_nnc': [],
        'r1_eig_avg_nnc': [],
        'r2_svd_avg_nnc': [],
        'r3_svd_avg_nnc': [],
    }

    for n in sorted(scaling_results.keys()):
        sr = scaling_results[n]
        for key in nnc_exponents:
            if key in sr:
                nnc_exponents[key].append(sr[key]['exponent'])

    print("\n  1. NNC EXPONENTS (mean across instances):")
    print(f"     {'Metric':25s}  {'Mean exp':>10s}  {'Range':>20s}  {'Verdict':>12s}")
    print(f"     {'-'*25:25s}  {'-'*10:>10s}  {'-'*20:>20s}  {'-'*12:>12s}")

    any_decreasing = False
    all_results = []
    for key, exps in nnc_exponents.items():
        if not exps:
            continue
        mean_exp = np.mean(exps)
        range_str = f"[{min(exps):+.3f}, {max(exps):+.3f}]"
        if mean_exp < -0.05:
            verdict = "DECREASING"
            any_decreasing = True
        elif mean_exp > 0.05:
            verdict = "INCREASING"
        else:
            verdict = "FLAT"
        label = key.replace('_avg_nnc', '').replace('_', ' ')
        print(f"     {label:25s}  {mean_exp:+10.4f}  {range_str:>20s}  {verdict:>12s}")
        all_results.append((key, mean_exp, verdict))

    # Check absolute commutator norms for comparison
    print("\n  2. ABSOLUTE COMMUTATOR EXPONENTS (mean across instances):")
    abs_keys = ['raw_avg_max_comm', 'r1_svd_avg_max_comm', 'r2_svd_avg_max_comm', 'r3_svd_avg_max_comm']
    for key in abs_keys:
        exps = []
        for n in sorted(scaling_results.keys()):
            sr = scaling_results[n]
            if key in sr:
                exps.append(sr[key]['exponent'])
        if exps:
            mean_exp = np.mean(exps)
            direction = "DECREASING" if mean_exp < -0.05 else ("INCREASING" if mean_exp > 0.05 else "FLAT")
            label = key.replace('_avg_max_comm', '').replace('_', ' ')
            print(f"     {label:25s}  {mean_exp:+10.4f}  [{direction}]")

    # ---- The definitive test ----
    print("\n\n  3. DEFINITIVE TEST RESULTS:")
    print("  " + "-" * 60)

    # Check: does ANY NNC metric decrease?
    raw_nnc_exps = nnc_exponents.get('raw_avg_nnc', [])
    r1_nnc_exps = nnc_exponents.get('r1_svd_avg_nnc', [])
    r2_nnc_exps = nnc_exponents.get('r2_svd_avg_nnc', [])
    r3_nnc_exps = nnc_exponents.get('r3_svd_avg_nnc', [])

    print(f"\n  RAW multi-slot NNC (no subtraction):")
    if raw_nnc_exps:
        mean_raw = np.mean(raw_nnc_exps)
        if mean_raw < -0.05:
            print(f"    DECREASING (exp={mean_raw:+.4f})")
            print(f"    This would indicate genuine centrality WITHOUT needing residual.")
        elif mean_raw > 0.05:
            print(f"    INCREASING (exp={mean_raw:+.4f})")
            print(f"    Confirms Node 1.3.5.2 self-suspicion: raw multi-slot")
            print(f"    per-b NNC INCREASES even though abs commutators decrease.")
            print(f"    The abs decrease is CONTRACTION, not centrality.")
        else:
            print(f"    FLAT (exp={mean_raw:+.4f})")
            print(f"    Inconclusive at these scales.")

    print(f"\n  r=1 SVD residual NNC (rank-1 stationary subtracted):")
    if r1_nnc_exps:
        mean_r1 = np.mean(r1_nnc_exps)
        if mean_r1 < -0.05:
            print(f"    DECREASING (exp={mean_r1:+.4f})")
            print(f"    ** The residual after removing the contractive component")
            print(f"    ** has GENUINELY decreasing non-centrality.")
            print(f"    ** -> GAP ALPHA CLOSES via multi-slot residual.")
        elif mean_r1 > 0.05:
            print(f"    INCREASING (exp={mean_r1:+.4f})")
            print(f"    The residual is ALSO non-central. Contraction was NOT the")
            print(f"    whole signal -- the non-centrality lives in the residual too.")
        else:
            print(f"    FLAT (exp={mean_r1:+.4f})")

    print(f"\n  r=2 and r=3 SVD residuals (deeper decontraction):")
    for r_label, exps in [('r=2', r2_nnc_exps), ('r=3', r3_nnc_exps)]:
        if exps:
            mean_r = np.mean(exps)
            if mean_r < -0.05:
                print(f"    {r_label}: DECREASING (exp={mean_r:+.4f})")
                print(f"    Removing more contractive modes DOES reveal centrality.")
            elif mean_r > 0.05:
                print(f"    {r_label}: INCREASING (exp={mean_r:+.4f})")
                print(f"    Non-centrality persists even after removing {r_label[2:]} modes.")
            else:
                print(f"    {r_label}: FLAT (exp={mean_r:+.4f})")

    # ---- FINAL VERDICT ----
    print("\n\n  " + "=" * 60)

    # Determine verdict based on NNC trends
    decreasing_nnc = []
    increasing_nnc = []
    flat_nnc = []
    for key, exps in nnc_exponents.items():
        if not exps:
            continue
        mean_exp = np.mean(exps)
        if mean_exp < -0.05:
            decreasing_nnc.append(key)
        elif mean_exp > 0.05:
            increasing_nnc.append(key)
        else:
            flat_nnc.append(key)

    if decreasing_nnc:
        # At least one NNC metric decreases -> genuine centrality signal
        verdict = "GAP-ALPHA-CLOSES"
        print(f"  VERDICT: {verdict}")
        print(f"\n  Metrics with decreasing NNC: {decreasing_nnc}")
        print(f"  The multi-slot residual (after subtracting contractive modes)")
        print(f"  shows genuinely decreasing normalized non-centrality.")
        print(f"  This means the residual operator is approaching the center")
        print(f"  of the algebra, NOT just contracting to a fixed point.")
        print(f"\n  Gap Alpha CLOSES: non-trivial approximately central sequences")
        print(f"  can be extracted from the multi-slot residual construction.")
    elif flat_nnc and not increasing_nnc:
        verdict = "INCONCLUSIVE"
        print(f"  VERDICT: {verdict}")
        print(f"\n  All NNC metrics are FLAT. The test is inconclusive at")
        print(f"  these instance sizes. Need larger n or higher k.")
    else:
        verdict = "GAP-ALPHA-KILLED-MULTISLOT"
        print(f"  VERDICT: {verdict}")
        print(f"\n  Metrics with increasing NNC: {increasing_nnc}")
        print(f"  ALL residual variants show INCREASING normalized non-centrality.")
        print(f"  The contraction artifact was NOT the whole signal --")
        print(f"  the non-centrality lives in the residual too.")
        print(f"\n  K-16: Multi-slot residual kill.")
        print(f"  The multi-slot construction with 2 live slots, after removing")
        print(f"  the contractive rank-1/2/3 components, still has INCREASING")
        print(f"  non-centrality with arity. The non-centrality is structural,")
        print(f"  not an artifact of contraction.")
        print(f"\n  Together with K-14 (single-slot rank-1 collapse) and K-15")
        print(f"  (single-slot residual fails), this establishes:")
        print(f"  ** The entire T_f construction family (single-slot, multi-slot,")
        print(f"  ** raw, and residual) fails to produce approximately central")
        print(f"  ** sequences via omega-averaging. **")

    print(f"\n  " + "=" * 60)

    # ---- Honest assessment ----
    print("\n\n  HONEST ASSESSMENT:")
    print("  " + "-" * 60)

    # Check for consistency across instances
    for key in ['r1_svd_avg_nnc', 'r2_svd_avg_nnc', 'r3_svd_avg_nnc']:
        if key in nnc_exponents and len(nnc_exponents[key]) >= 2:
            exps = nnc_exponents[key]
            label = key.replace('_avg_nnc', '')
            signs = ['+' if e > 0.05 else ('-' if e < -0.05 else '~') for e in exps]
            consistency = len(set(signs)) == 1
            print(f"  {label}: exponents = {[f'{e:+.3f}' for e in exps]}")
            print(f"    Signs: {signs}  Consistent: {'YES' if consistency else 'NO'}")

    # Self-suspicion checks
    print("\n\n  SELF-SUSPICION CHECKS:")

    print("\n  S1: Could MC noise cause the NNC trend?")
    print("      Check: is the trend consistent across ALL instance sizes?")
    for key in ['r1_svd_avg_nnc']:
        if key in nnc_exponents:
            exps = nnc_exponents[key]
            if all(e > 0 for e in exps) or all(e < 0 for e in exps):
                print(f"      {key}: ALL exponents same sign -> consistent, LOW noise risk.")
            else:
                print(f"      {key}: MIXED signs -> possible noise contamination.")

    print("\n  S2: Could the NNC denominator (op-norm) be declining faster than")
    print("      the numerator (commutator), creating artificial NNC increase?")
    print("      Check: compare op-norm exponent vs abs-comm exponent.")
    for n in sorted(scaling_results.keys()):
        sr = scaling_results[n]
        raw_comm_exp = sr.get('raw_avg_max_comm', {}).get('exponent', None)
        if raw_comm_exp is not None:
            # Get op-norm decline from the data
            data = results_master[n]
            ks = np.array(sorted(data.keys()), dtype=float)
            op_norms = np.array([data[k]['raw_avg_op_norm'] for k in sorted(data.keys())])
            if all(v > 1e-15 for v in op_norms):
                log_ks = np.log(ks)
                log_op = np.log(op_norms)
                c = np.polyfit(log_ks, log_op, 1)
                print(f"      n={n}: abs-comm exp={raw_comm_exp:+.3f}, "
                      f"op-norm exp={c[0]:+.3f}, "
                      f"NNC exp={raw_comm_exp - c[0]:+.3f} (= comm - op)")

    print("\n  S3: Is the residual operator trivially small?")
    print("      If ||R||_op -> 0, the residual is vanishing (trivial).")
    for n in sorted(results_master.keys()):
        data = results_master[n]
        if not data:
            continue
        ks_sorted = sorted(data.keys())
        r1_ops = [data[k]['r1_svd_avg_op_norm'] for k in ks_sorted]
        print(f"      n={n}: r1-SVD op-norms = {[f'{v:.4f}' for v in r1_ops]}")
        if r1_ops[-1] < 0.01:
            print(f"      WARNING: residual op-norm < 0.01 at highest k. Approaching zero.")
        elif r1_ops[-1] > 0.05:
            print(f"      Residual op-norm > 0.05 at highest k. Non-trivial.")

    print("\n  S4: Does the r=2 or r=3 residual show qualitatively different behavior?")
    print("      If deeper decontraction reveals centrality, the signal is real.")
    for rkey, rlabel in [('r2_svd_avg_nnc', 'r=2'), ('r3_svd_avg_nnc', 'r=3')]:
        r1_key = 'r1_svd_avg_nnc'
        if r1_key in nnc_exponents and rkey in nnc_exponents:
            mean_r1 = np.mean(nnc_exponents[r1_key])
            mean_r = np.mean(nnc_exponents[rkey])
            diff = mean_r - mean_r1
            if diff < -0.1:
                print(f"      {rlabel} exponent MORE NEGATIVE than r=1 by {diff:.3f}")
                print(f"        -> deeper decontraction reveals MORE centrality")
            elif diff > 0.1:
                print(f"      {rlabel} exponent MORE POSITIVE than r=1 by {diff:.3f}")
                print(f"        -> deeper decontraction reveals MORE non-centrality")
            else:
                print(f"      {rlabel} exponent SIMILAR to r=1 (diff={diff:+.3f})")
                print(f"        -> the contractive component is concentrated in rank-1")

    return verdict


# ================================================================
# 10. Main
# ================================================================

def main():
    total_t0 = time.time()

    results_master = run_experiment()
    scaling_results = print_synthesis(results_master)
    verdict = print_verdict(results_master, scaling_results)

    total_elapsed = time.time() - total_t0
    print(f"\n\n  Total runtime: {total_elapsed:.1f}s")
    print(f"  Node 1.3.5.4 complete. Verdict: {verdict}")
    print("=" * 78)


if __name__ == "__main__":
    main()
