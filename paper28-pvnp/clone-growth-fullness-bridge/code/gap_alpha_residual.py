"""
Node 1.3.5.3 -- Salvage S5: Normalized Residual Clone Operator

Attempts to salvage the clone operator approach (killed by K-14: rank-1 collapse)
by subtracting the rank-1 component that dominates at high arity.

Three variants tested:

  R_f  := T_f - |pi><1|          (rank-1 residual)
  S_f  := T_f / tr(T_f) * |Sol| - I   (trace-normalized)
  P_f  := spectral projection onto eigenvalues in [0.1, 0.6]  (non-trivial band)

Key question: does any variant produce ||[variant, y]||_2 -> 0 as k -> infty
while the variant itself is NOT converging to scalar * I ?

SUCCESS: some variant has decreasing commutator norms AND is not scalar.
KILL: all variants either (a) -> scalar*I (trivially central) or
      (b) commutator norms don't decrease (non-trivially non-central).

Author: Claude Opus 4.6 (1M context), Node 1.3.5.3
Date: 2026-04-11
"""

import numpy as np
import random
from itertools import product as cartesian_product
import sys
import time

random.seed(42)
np.set_printoptions(precision=8, suppress=True, linewidth=140)


# ==================================================================
# 1.  Instance generation (reused from gap_alpha_compute.py)
# ==================================================================

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
    num_clauses = int(n * clause_ratio)
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


# ==================================================================
# 2.  Threshold-k polymorphism (from gap_alpha_arity_scan.py)
# ==================================================================

def threshold_k(coords, k):
    s = sum(coords)
    if s > k / 2:
        return 1
    elif s < k / 2:
        return 0
    else:
        return 0  # tie-break preserves Taylor: f(x,...,x) = x


def coordinatewise_threshold_k(tuples, k):
    n = len(tuples[0])
    return tuple(threshold_k(tuple(t[i] for t in tuples), k) for i in range(n))


def verify_polymorphism_k(solutions, k, max_check=100000):
    sol_set = set(solutions)
    S = len(solutions)
    total_k = S ** k
    if total_k <= max_check:
        violations = 0
        total = 0
        for combo in cartesian_product(range(S), repeat=k):
            total += 1
            tuples = [solutions[i] for i in combo]
            result = coordinatewise_threshold_k(tuples, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, total
    else:
        num_samples = min(50000, total_k)
        violations = 0
        for _ in range(num_samples):
            tuples = [solutions[random.randint(0, S - 1)] for _ in range(k)]
            result = coordinatewise_threshold_k(tuples, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, num_samples


# ==================================================================
# 3.  Compute T_fk (clone operator with 1 live + (k-1) averaged)
# ==================================================================

def compute_T_fk(solutions, k, mc_budget=200000):
    """
    T_{f_k}[s, a] = (1/|Sol|^{k-1}) * #{(a2,...,ak) in Sol^{k-1} : f_k(a,a2,...,ak) = s}
    """
    sol_list = list(solutions)
    sol_set = set(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    T = np.zeros((S, S), dtype=np.float64)

    total_tuples = S ** (k - 1)

    if total_tuples <= 500000:
        for a_idx, a in enumerate(sol_list):
            for combo in cartesian_product(range(S), repeat=k - 1):
                aux = [sol_list[i] for i in combo]
                result = coordinatewise_threshold_k([a] + aux, k)
                if result in sol_to_idx:
                    T[sol_to_idx[result], a_idx] += 1.0
        T /= total_tuples
    else:
        samples_per_a = mc_budget // S
        for a_idx, a in enumerate(sol_list):
            for _ in range(samples_per_a):
                aux = [sol_list[random.randint(0, S - 1)] for _ in range(k - 1)]
                result = coordinatewise_threshold_k([a] + aux, k)
                if result in sol_to_idx:
                    T[sol_to_idx[result], a_idx] += 1.0
            T[:, a_idx] /= samples_per_a
    return T


# ==================================================================
# 4.  Commutator norms  ||[A, y]||_2  for all matrix-unit generators
# ==================================================================

def commutator_norms(A, S):
    """
    Returns (max_norm, mean_norm, all_norms) for generators y = |i><j|.
    ||[A,y]||_2 = ||A*y - y*A||_F / sqrt(S)
    """
    norms = np.empty(S * S, dtype=np.float64)
    idx = 0
    for i in range(S):
        for j in range(S):
            # [A, e_ij] = A e_ij - e_ij A
            # (A e_ij)_{pq} = A_{pi} delta_{jq}  => column j of A placed at column q=j: col p = A[:,i] at col j
            # (e_ij A)_{pq} = delta_{pi} A_{jq}  => row i of A placed at row p=i: row j of A at row i
            # Frobenius: sum_{p,q} |comm_{pq}|^2
            # Only nonzero entries: column j of (A e_ij) and row i of (e_ij A)
            # comm[:,j] += A[:,i];  comm[i,:] -= A[j,:]
            # All other entries are zero.
            # But these two contributions can overlap at (i,j).
            # Fast computation:
            col_i = A[:, i]  # length S
            row_j = A[j, :]  # length S
            # comm is zero except:
            #   comm[p, j] += A[p, i]  for all p     (from A @ e_ij)
            #   comm[i, q] -= A[j, q]  for all q     (from e_ij @ A)
            # These overlap at (i, j): comm[i,j] = A[i,i] - A[j,j]  ... wait, let me just do it directly.
            # Actually the overlap: comm[i,j] += A[i,i] and comm[i,j] -= A[j,j]... no.
            # Let me compute properly.
            # comm[p,q] = sum_r A[p,r]*e_ij[r,q] - sum_r e_ij[p,r]*A[r,q]
            #           = A[p,i]*delta_{jq} - delta_{pi}*A[j,q]
            # So comm[p,q] = A[p,i]*delta_{jq} - delta_{pi}*A[j,q]
            # Nonzero only when q=j OR p=i.
            # When q=j and p!=i: comm[p,j] = A[p,i]
            # When p=i and q!=j: comm[i,q] = -A[j,q]
            # When p=i and q=j: comm[i,j] = A[i,i] - A[j,j]
            # Frobenius^2 = sum_{p!=i} A[p,i]^2 + sum_{q!=j} A[j,q]^2 + (A[i,i]-A[j,j])^2
            frob_sq = 0.0
            for p in range(S):
                if p != i:
                    frob_sq += col_i[p] ** 2
            for q in range(S):
                if q != j:
                    frob_sq += row_j[q] ** 2
            frob_sq += (A[i, i] - A[j, j]) ** 2
            norms[idx] = np.sqrt(frob_sq) / np.sqrt(S)
            idx += 1
    return np.max(norms), np.mean(norms), norms


# ==================================================================
# 5.  Three residual constructions
# ==================================================================

def compute_stationary(T):
    """
    Left eigenvector pi of column-stochastic T for eigenvalue 1:
        pi^T T = pi^T,   sum(pi) = 1,  pi >= 0.
    """
    eigenvalues, eigenvectors = np.linalg.eig(T.T)
    # Find eigenvector for eigenvalue closest to 1
    idx = np.argmin(np.abs(eigenvalues - 1.0))
    pi = np.real(eigenvectors[:, idx])
    pi = np.abs(pi)  # ensure non-negative
    pi /= np.sum(pi)
    return pi


def compute_R_f(T):
    """
    R_f = T_f - |pi><1|
    Removes the rank-1 stationary component.
    pi = stationary distribution (left eigvec for eigenvalue 1)
    <1| = row vector of all 1s (right eigvec for eigenvalue 1 of col-stoch matrix)
    """
    S = T.shape[0]
    pi = compute_stationary(T)
    ones = np.ones(S)
    R = T - np.outer(pi, ones)
    return R, pi


def compute_S_f(T):
    """
    S_f = T_f * (|Sol| / tr(T_f)) - I
    Trace-normalized: rescale T so that its trace equals |Sol|, then subtract identity.
    """
    S = T.shape[0]
    tr = np.trace(T)
    if abs(tr) < 1e-15:
        return np.zeros_like(T), 0.0
    scale = S / tr
    S_op = T * scale - np.eye(S)
    return S_op, scale


def compute_P_f(T, band_low=0.1, band_high=0.6):
    """
    P_f = spectral projection of T onto eigenvalues in [band_low, band_high].
    Extracts the "non-trivial spectral band" -- not the leading eigenvalue 1
    and not the collapsing tail near 0.
    """
    eigenvalues, eigenvectors = np.linalg.eig(T)
    eigenvalues_real = np.real(eigenvalues)

    # Select eigenvalues in the band
    mask = (eigenvalues_real >= band_low) & (eigenvalues_real <= band_high)
    if not np.any(mask):
        # No eigenvalues in band -- try wider band
        mask = (eigenvalues_real >= 0.05) & (eigenvalues_real <= 0.7)
    if not np.any(mask):
        return np.zeros_like(T), 0

    # Spectral projection: sum of |v_i><v_i| for selected eigenvalues
    # Using the eigenvector matrix: P = V_sel @ V_sel^{-1}_sel ... but eigenvectors
    # may not be orthogonal. Use the Schur decomposition for a proper projection.
    # For a diagonalizable matrix: T = V D V^{-1}, P = V M V^{-1} where M_ii = lambda_i if selected, 0 otherwise.
    V = eigenvectors
    try:
        V_inv = np.linalg.inv(V)
    except np.linalg.LinAlgError:
        return np.zeros_like(T), 0

    D_masked = np.diag(eigenvalues * mask)
    P = np.real(V @ D_masked @ V_inv)
    n_selected = int(np.sum(mask))
    return P, n_selected


# ==================================================================
# 6.  Analysis of a single operator
# ==================================================================

def analyze_operator(A, label, S):
    """
    Analyze an operator A: eigenvalues, commutator norms, scalar deviation.
    Returns a dict of measurements.
    """
    eigvals = np.sort(np.real(np.linalg.eigvals(A)))[::-1]

    # Commutator norms
    max_cn, mean_cn, _ = commutator_norms(A, S)

    # Deviation from scalar * I
    tr = np.trace(A)
    scalar = tr / S
    dev_scalar_norm = np.linalg.norm(A - scalar * np.eye(S), 'fro')
    op_norm = np.linalg.norm(A, 'fro')
    dev_scalar_rel = dev_scalar_norm / op_norm if op_norm > 1e-15 else 0.0

    # Deviation from identity
    dev_id = np.linalg.norm(A - np.eye(S), 'fro')

    # Operator norm (spectral)
    spec_norm = np.max(np.abs(eigvals))

    # Rank
    rank = np.linalg.matrix_rank(A, tol=1e-10)

    return {
        'label': label,
        'eigvals_top5': eigvals[:min(5, len(eigvals))],
        'eigval_max': eigvals[0] if len(eigvals) > 0 else 0,
        'eigval_min': eigvals[-1] if len(eigvals) > 0 else 0,
        'max_commutator': max_cn,
        'mean_commutator': mean_cn,
        'trace': tr,
        'scalar_coeff': scalar,
        'dev_scalar_rel': dev_scalar_rel,
        'dev_scalar_abs': dev_scalar_norm,
        'dev_identity': dev_id,
        'spectral_norm': spec_norm,
        'frobenius_norm': op_norm,
        'rank': rank,
        'is_zero': op_norm < 1e-12,
        'is_scalar': dev_scalar_rel < 1e-8,
    }


def print_operator_analysis(a):
    print(f"    Eigenvalues (top 5): {a['eigvals_top5']}")
    print(f"    Eigenvalue max: {a['eigval_max']:.10f}")
    print(f"    Eigenvalue min: {a['eigval_min']:.10f}")
    print(f"    Spectral norm: {a['spectral_norm']:.10f}")
    print(f"    Rank: {a['rank']}")
    print(f"    ||A||_F: {a['frobenius_norm']:.10f}")
    print(f"    trace(A): {a['trace']:.10f}")
    print(f"    scalar = tr/S: {a['scalar_coeff']:.10f}")
    print(f"    ||A - scalar*I||_F / ||A||_F: {a['dev_scalar_rel']:.10f}")
    print(f"    ||A - I||_F: {a['dev_identity']:.10f}")
    print(f"    max ||[A, y]||_2: {a['max_commutator']:.10f}")
    print(f"    mean ||[A, y]||_2: {a['mean_commutator']:.10f}")
    print(f"    Is zero? {a['is_zero']}")
    print(f"    Is scalar * I? {a['is_scalar']}")


# ==================================================================
# 7.  Main experiment
# ==================================================================

def run_single_instance(n, solutions, arities, instance_label):
    """
    For a single 2-SAT instance, compute T_f, R_f, S_f, P_f at each arity k.
    Returns a list of result dicts.
    """
    S = len(solutions)
    print(f"\n{'#' * 78}")
    print(f"  {instance_label}: n={n}, |Sol|={S}")
    print(f"{'#' * 78}")

    all_results = []

    for k in arities:
        print(f"\n{'=' * 70}")
        print(f"  Arity k = {k}")
        print(f"{'=' * 70}")

        # Verify polymorphism
        is_poly, viol, total = verify_polymorphism_k(solutions, k)
        if not is_poly:
            print(f"  POLYMORPHISM FAILED ({viol}/{total} violations). Skipping k={k}.")
            continue
        print(f"  Polymorphism verified: 0/{total} violations")

        # Compute T_f
        t0 = time.time()
        T = compute_T_fk(solutions, k)
        dt = time.time() - t0
        print(f"  T_f computed in {dt:.1f}s")

        # -- T_f analysis (baseline from K-14) --
        print(f"\n  --- T_f (baseline, K-14 data) ---")
        a_T = analyze_operator(T, f"T_f k={k}", S)
        print_operator_analysis(a_T)

        # -- R_f = T_f - |pi><1| --
        R, pi = compute_R_f(T)
        print(f"\n  --- R_f = T_f - |pi><1| ---")
        print(f"    Stationary distribution pi: min={pi.min():.8f} max={pi.max():.8f} sum={pi.sum():.8f}")
        print(f"    pi uniformity (std/mean): {np.std(pi)/np.mean(pi):.6f}")
        a_R = analyze_operator(R, f"R_f k={k}", S)
        print_operator_analysis(a_R)

        # Verify R_f has eigenvalue 0 where T_f had eigenvalue 1
        print(f"    Verification: T_f leading eigenvalue = {a_T['eigval_max']:.10f}")
        print(f"    Verification: R_f leading eigenvalue = {a_R['eigval_max']:.10f}")
        # R_f should have the same non-leading eigenvalues as T_f
        T_eigs_sorted = np.sort(np.real(np.linalg.eigvals(T)))[::-1]
        R_eigs_sorted = np.sort(np.real(np.linalg.eigvals(R)))[::-1]
        print(f"    T_f eigenvalues: {T_eigs_sorted[:min(6,S)]}")
        print(f"    R_f eigenvalues: {R_eigs_sorted[:min(6,S)]}")

        # -- S_f = T_f * (S / tr(T_f)) - I --
        S_op, scale = compute_S_f(T)
        print(f"\n  --- S_f = T_f * (|Sol|/tr) - I ---")
        print(f"    Scale factor: {scale:.10f}")
        a_S = analyze_operator(S_op, f"S_f k={k}", S)
        print_operator_analysis(a_S)

        # -- P_f = spectral projection onto [0.1, 0.6] band --
        P_op, n_sel = compute_P_f(T, band_low=0.1, band_high=0.6)
        print(f"\n  --- P_f = spectral projection [0.1, 0.6] ---")
        print(f"    Eigenvalues selected: {n_sel}")
        a_P = analyze_operator(P_op, f"P_f k={k}", S)
        print_operator_analysis(a_P)

        # -- NORMALIZED R_f:  R_f / ||R_f||_F  (so we compare like for like) --
        if a_R['frobenius_norm'] > 1e-12:
            R_normed = R / a_R['frobenius_norm']
            a_Rn = analyze_operator(R_normed, f"R_f_normed k={k}", S)
            print(f"\n  --- R_f / ||R_f||_F (unit-normalized) ---")
            print_operator_analysis(a_Rn)
        else:
            a_Rn = None

        # Commutator comparison
        print(f"\n  --- COMMUTATOR COMPARISON at k={k} ---")
        print(f"    T_f:          max||[T_f, y]||_2 = {a_T['max_commutator']:.10f}")
        print(f"    R_f:          max||[R_f, y]||_2 = {a_R['max_commutator']:.10f}")
        print(f"    S_f:          max||[S_f, y]||_2 = {a_S['max_commutator']:.10f}")
        print(f"    P_f:          max||[P_f, y]||_2 = {a_P['max_commutator']:.10f}")
        if a_Rn is not None:
            print(f"    R_f_normed:   max||[Rn, y]||_2 = {a_Rn['max_commutator']:.10f}")
        print(f"    T_f scalar?:  {a_T['is_scalar']}")
        print(f"    R_f scalar?:  {a_R['is_scalar']}")
        print(f"    S_f scalar?:  {a_S['is_scalar']}")
        print(f"    P_f scalar?:  {a_P['is_scalar']}")

        # ratio: how much did R_f improve over T_f?
        if a_T['max_commutator'] > 1e-15:
            ratio_R = a_R['max_commutator'] / a_T['max_commutator']
            print(f"    Ratio ||[R_f,y]|| / ||[T_f,y]||: {ratio_R:.6f}")
        else:
            ratio_R = float('nan')

        result = {
            'k': k,
            'S': S,
            'n': n,
            'T_f': a_T,
            'R_f': a_R,
            'S_f': a_S,
            'P_f': a_P,
            'R_f_normed': a_Rn,
            'ratio_R_over_T': ratio_R,
            'pi_std_over_mean': float(np.std(pi) / np.mean(pi)),
        }
        all_results.append(result)

    return all_results


def scaling_analysis(results, variant_key, variant_name):
    """
    Analyze how commutator norms scale with k for a given variant.
    Returns (exponent, R^2, is_decreasing, is_scalar_at_all_k).
    """
    ks = np.array([r['k'] for r in results if r[variant_key] is not None], dtype=float)
    max_comms = np.array([r[variant_key]['max_commutator'] for r in results if r[variant_key] is not None])
    is_scalar = [r[variant_key]['is_scalar'] for r in results if r[variant_key] is not None]
    dev_scalar = [r[variant_key]['dev_scalar_rel'] for r in results if r[variant_key] is not None]

    if len(ks) < 3:
        return None

    # Power law fit: max_comm ~ k^exponent
    valid = max_comms > 1e-15
    if np.sum(valid) < 3:
        return {'exponent': float('nan'), 'R2': 0, 'decreasing': False,
                'all_scalar': all(is_scalar), 'ks': ks.tolist(),
                'max_comms': max_comms.tolist(), 'dev_scalar': dev_scalar}

    log_k = np.log(ks[valid])
    log_mc = np.log(max_comms[valid])
    coeffs = np.polyfit(log_k, log_mc, 1)
    predicted = np.polyval(coeffs, log_k)
    ss_res = np.sum((log_mc - predicted) ** 2)
    ss_tot = np.sum((log_mc - np.mean(log_mc)) ** 2)
    R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    decreasing = all(max_comms[i] >= max_comms[i + 1] for i in range(len(max_comms) - 1))

    return {
        'exponent': float(coeffs[0]),
        'R2': float(R2),
        'decreasing': decreasing,
        'all_scalar': all(is_scalar),
        'any_scalar': any(is_scalar),
        'ks': ks.tolist(),
        'max_comms': max_comms.tolist(),
        'dev_scalar': dev_scalar,
    }


def main():
    print("=" * 78)
    print("  NODE 1.3.5.3 -- SALVAGE S5: NORMALIZED RESIDUAL CLONE OPERATOR")
    print("  Three variants: R_f, S_f, P_f")
    print("  Tests at arities k = 3, 5, 7, 9, 11")
    print("  Instance sizes n = 4, 6, 8, 10")
    print("=" * 78)
    print()

    arities = [3, 5, 7, 9, 11]

    # ============================================================
    # PART 1: Multiple instance sizes at all arities
    # ============================================================
    all_instance_results = {}

    for n in [4, 6, 8, 10]:
        random.seed(42 + n)
        instance = generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4)
        if instance is None:
            print(f"FAILED to generate 2-SAT instance at n={n}")
            continue
        n_vars, clauses, solutions = instance
        label = f"2-SAT n={n}"
        results = run_single_instance(n_vars, solutions, arities, label)
        all_instance_results[n] = results

    # ============================================================
    # PART 2: SCALING ANALYSIS
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  PART 2: ARITY SCALING ANALYSIS")
    print("=" * 78)

    for n, results in all_instance_results.items():
        if not results:
            continue
        S = results[0]['S']
        print(f"\n  --- n={n}, |Sol|={S} ---")

        for vkey, vname in [('T_f', 'T_f (baseline)'), ('R_f', 'R_f (residual)'),
                            ('S_f', 'S_f (trace-norm)'), ('P_f', 'P_f (spectral proj)'),
                            ('R_f_normed', 'R_f_normed')]:
            sa = scaling_analysis(results, vkey, vname)
            if sa is None:
                print(f"    {vname}: insufficient data")
                continue
            print(f"\n    {vname}:")
            print(f"      Exponent (max||[.,y]|| ~ k^exp):  {sa['exponent']:.6f}")
            print(f"      R^2:                               {sa['R2']:.6f}")
            print(f"      Monotonically decreasing?          {sa['decreasing']}")
            print(f"      All arities scalar?                {sa['all_scalar']}")
            print(f"      Any arity scalar?                  {sa.get('any_scalar', 'N/A')}")
            print(f"      k values:  {sa['ks']}")
            print(f"      max||[.,y]||: {['%.8f' % x for x in sa['max_comms']]}")
            print(f"      dev_scalar:   {['%.8f' % x for x in sa['dev_scalar']]}")

    # ============================================================
    # PART 3: SUMMARY TABLE
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  PART 3: SUMMARY TABLE -- Commutator norms at each (n, k)")
    print("=" * 78)

    header = f"  {'n':>3s} {'|Sol|':>5s} {'k':>3s}  {'||[T_f,y]||':>13s} {'||[R_f,y]||':>13s} {'||[S_f,y]||':>13s} {'||[P_f,y]||':>13s} {'R/T ratio':>10s} {'R_f scalar?':>12s} {'S_f scalar?':>12s}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for n, results in sorted(all_instance_results.items()):
        for r in results:
            t_mc = r['T_f']['max_commutator']
            r_mc = r['R_f']['max_commutator']
            s_mc = r['S_f']['max_commutator']
            p_mc = r['P_f']['max_commutator']
            ratio = r['ratio_R_over_T']
            r_scal = 'YES' if r['R_f']['is_scalar'] else 'NO'
            s_scal = 'YES' if r['S_f']['is_scalar'] else 'NO'
            print(f"  {r['n']:3d} {r['S']:5d} {r['k']:3d}  {t_mc:13.8f} {r_mc:13.8f} {s_mc:13.8f} {p_mc:13.8f} {ratio:10.6f} {r_scal:>12s} {s_scal:>12s}")

    # ============================================================
    # PART 4: ARITY SCALING TABLE (fixed n=8 or largest available)
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  PART 4: ARITY SCALING (single instance, all k)")
    print("=" * 78)

    # Pick the largest instance with full arity data
    best_n = max(all_instance_results.keys())
    results = all_instance_results[best_n]
    if results:
        S = results[0]['S']
        print(f"\n  Instance: n={best_n}, |Sol|={S}")
        print(f"\n  {'k':>3s}  {'T_f max':>12s}  {'R_f max':>12s}  {'S_f max':>12s}  {'P_f max':>12s}  {'R_f dev_sc':>12s}  {'R_f rank':>8s}  {'R_f ||.||_F':>12s}")
        print(f"  {'---':>3s}  {'---':>12s}  {'---':>12s}  {'---':>12s}  {'---':>12s}  {'---':>12s}  {'---':>8s}  {'---':>12s}")
        for r in results:
            print(f"  {r['k']:3d}  {r['T_f']['max_commutator']:12.8f}  {r['R_f']['max_commutator']:12.8f}  "
                  f"{r['S_f']['max_commutator']:12.8f}  {r['P_f']['max_commutator']:12.8f}  "
                  f"{r['R_f']['dev_scalar_rel']:12.8f}  {r['R_f']['rank']:8d}  {r['R_f']['frobenius_norm']:12.8f}")

    # ============================================================
    # PART 5: THE CRITICAL TEST -- does R_f commutator decrease with k?
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  PART 5: THE CRITICAL TEST")
    print("=" * 78)

    for n, results in sorted(all_instance_results.items()):
        if len(results) < 3:
            continue
        S = results[0]['S']
        print(f"\n  n={n}, |Sol|={S}:")

        for vkey, vname in [('T_f', 'T_f'), ('R_f', 'R_f'), ('S_f', 'S_f'), ('P_f', 'P_f')]:
            ks = [r['k'] for r in results]
            mcs = [r[vkey]['max_commutator'] for r in results]
            devs = [r[vkey]['dev_scalar_rel'] for r in results]
            is_scal = [r[vkey]['is_scalar'] for r in results]

            decreasing = all(mcs[i] >= mcs[i+1] for i in range(len(mcs)-1))
            all_scalar = all(is_scal)
            converging_scalar = devs[-1] < devs[0] * 0.5 if devs[0] > 1e-12 else False

            status = "UNKNOWN"
            if decreasing and not all_scalar and not converging_scalar:
                status = "SUCCESS CANDIDATE"
            elif decreasing and (all_scalar or converging_scalar):
                status = "TRIVIALLY CENTRAL (scalar collapse)"
            elif not decreasing:
                status = "KILLED (commutator not decreasing)"

            print(f"    {vname}:  max_comm trend = {'DECREASING' if decreasing else 'NOT DECREASING'},  "
                  f"scalar? = {all_scalar},  converging to scalar? = {converging_scalar}  => {status}")
            print(f"           k={ks}, max_comm={['%.8f' % x for x in mcs]}")

    # ============================================================
    # PART 6: ADDITIONAL DIAGNOSTIC -- R_f eigenvalue structure
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  PART 6: R_f EIGENVALUE STRUCTURE")
    print("=" * 78)

    for n, results in sorted(all_instance_results.items()):
        print(f"\n  n={n}:")
        for r in results:
            print(f"    k={r['k']}: R_f eigenvalues = {r['R_f']['eigvals_top5']}")
            print(f"           R_f spectral norm = {r['R_f']['spectral_norm']:.10f}")
            print(f"           T_f 2nd eigenvalue = {r['T_f']['eigvals_top5'][1] if len(r['T_f']['eigvals_top5']) > 1 else 'N/A'}")

    # ============================================================
    # PART 7: RATIO ANALYSIS -- R_f commutator / R_f spectral norm
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  PART 7: NORMALIZED RATIO  max||[R_f,y]|| / ||R_f||_spec  vs k")
    print("  (If this ratio -> 0, R_f becomes relatively more central)")
    print("=" * 78)

    for n, results in sorted(all_instance_results.items()):
        print(f"\n  n={n}:")
        for r in results:
            sn = r['R_f']['spectral_norm']
            mc = r['R_f']['max_commutator']
            ratio = mc / sn if sn > 1e-15 else float('nan')
            print(f"    k={r['k']}: max||[R_f,y]||/||R_f||_spec = {ratio:.8f}  (mc={mc:.8f}, sn={sn:.8f})")

    # ============================================================
    # PART 8: INSTANCE-SIZE SCALING at fixed k=3
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  PART 8: INSTANCE-SIZE SCALING at fixed k=3")
    print("  Does R_f commutator norm decrease with n (at fixed arity)?")
    print("=" * 78)

    k3_data = []
    for n, results in sorted(all_instance_results.items()):
        k3 = [r for r in results if r['k'] == 3]
        if k3:
            r = k3[0]
            k3_data.append(r)
            print(f"  n={n}, |Sol|={r['S']}: T_f max_comm={r['T_f']['max_commutator']:.8f}, "
                  f"R_f max_comm={r['R_f']['max_commutator']:.8f}, "
                  f"S_f max_comm={r['S_f']['max_commutator']:.8f}")

    if len(k3_data) >= 3:
        ns = np.array([r['n'] for r in k3_data], dtype=float)
        for vkey, vname in [('T_f', 'T_f'), ('R_f', 'R_f'), ('S_f', 'S_f')]:
            mcs = np.array([r[vkey]['max_commutator'] for r in k3_data])
            valid = mcs > 1e-15
            if np.sum(valid) >= 3:
                log_n = np.log(ns[valid])
                log_mc = np.log(mcs[valid])
                coeffs = np.polyfit(log_n, log_mc, 1)
                print(f"\n  {vname} vs n: exponent = {coeffs[0]:.4f}")

    # ============================================================
    # FINAL VERDICT
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  FINAL VERDICT")
    print("=" * 78)

    # Gather all scaling data
    verdicts = {}
    for vkey, vname in [('T_f', 'T_f'), ('R_f', 'R_f'), ('S_f', 'S_f'), ('P_f', 'P_f')]:
        # Check across all instances
        all_killed = True
        any_success = False
        any_trivial = False
        for n, results in all_instance_results.items():
            if len(results) < 3:
                continue
            ks = [r['k'] for r in results]
            mcs = [r[vkey]['max_commutator'] for r in results]
            devs = [r[vkey]['dev_scalar_rel'] for r in results]
            is_scal = [r[vkey]['is_scalar'] for r in results]

            decreasing = all(mcs[i] >= mcs[i + 1] for i in range(len(mcs) - 1))
            all_scalar = all(is_scal)
            converging_scalar = devs[-1] < devs[0] * 0.5 if len(devs) > 0 and devs[0] > 1e-12 else False

            if decreasing and not all_scalar and not converging_scalar:
                any_success = True
                all_killed = False
            elif decreasing and (all_scalar or converging_scalar):
                any_trivial = True
                all_killed = False

        if any_success:
            verdicts[vname] = "SUCCESS CANDIDATE"
        elif any_trivial:
            verdicts[vname] = "TRIVIALLY CENTRAL (scalar collapse)"
        elif all_killed:
            verdicts[vname] = "KILLED (commutator not decreasing with k)"
        else:
            verdicts[vname] = "INCONCLUSIVE"

    print()
    for vname, verdict in verdicts.items():
        marker = ">>>" if "SUCCESS" in verdict else "   "
        print(f"  {marker} {vname:20s}: {verdict}")

    any_success = any("SUCCESS" in v for v in verdicts.values())
    all_killed = all("KILLED" in v for v in verdicts.values())
    any_trivial = any("TRIVIAL" in v for v in verdicts.values())

    print()
    if any_success:
        print("  ========================================================")
        print("  VERDICT: SUCCESS CANDIDATE FOUND")
        print("  At least one variant shows decreasing commutator norms")
        print("  while remaining non-scalar. Further investigation needed")
        print("  to confirm this is not a finite-size artifact.")
        print("  STATUS: CLOSES (pending large-n confirmation)")
        print("  ========================================================")
    elif all_killed:
        print("  ========================================================")
        print("  VERDICT: ALL VARIANTS KILLED")
        print("  No variant produces decreasing commutator norms with k.")
        print("  The rank-1 residual, trace normalization, and spectral")
        print("  projection all fail to salvage the clone operator approach.")
        print("  The entire 'clone operator -> approximately central'")
        print("  strategy is structurally dead.")
        print("  STATUS: KILLS (S5, and likely the entire T_f approach)")
        print("  ========================================================")
    elif any_trivial and not any_success:
        print("  ========================================================")
        print("  VERDICT: TRIVIALLY CENTRAL ONLY")
        print("  Some variants converge to scalar * I (trivially central)")
        print("  but none are both non-trivially and approximately central.")
        print("  The approach cannot produce the needed non-trivial")
        print("  approximately central sequences.")
        print("  STATUS: KILLS (the approach produces only trivial sequences)")
        print("  ========================================================")
    else:
        print("  ========================================================")
        print("  VERDICT: INCONCLUSIVE")
        print("  Not enough data to determine. Recommend testing at")
        print("  larger n and with more instances.")
        print("  STATUS: INCONCLUSIVE")
        print("  ========================================================")


if __name__ == "__main__":
    main()
