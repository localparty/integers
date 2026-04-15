"""
Gap Alpha Multi-Slot Construction -- Node 1.3.5.2

SALVAGE S4: Multi-slot clone operator construction.

Context: Node 1.3.5.1 computed T_f with ONE live slot and (k-1) omega-averaged
slots. Result: KILLED (K-14). The omega-averaging concentrates onto the mean at
high arity, producing a rank-1 projector. Commutator norms INCREASE with k.

This node uses 2 LIVE slots + (k-2) averaged slots.

For a k-ary polymorphism f on solution set Sol(Gamma), define:

    T_f^{(2)}[s, (a,b)] = (1/|Sol|^{k-2}) * #{(c3,...,ck) in Sol^{k-2} :
                            f(a, b, c3,...,ck) = s}

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

random.seed(42)
np.random.seed(42)
np.set_printoptions(precision=6, suppress=True, linewidth=120)

# Global MC budget tuning -- keep total walltime feasible
MC_BUDGET_MULTI = 10000   # MC samples per (a,b) pair for multi-slot averaging
MC_BUDGET_SYM = 10000     # MC samples per (a) for symmetrized per-slot averaging


# ============================================================
# 1. Instance generation
# ============================================================

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

def coordinatewise_threshold_k(inputs, k):
    n = len(inputs[0])
    threshold = (k + 1) // 2
    result = []
    for i in range(n):
        s = sum(inp[i] for inp in inputs)
        result.append(1 if s >= threshold else 0)
    return tuple(result)


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
    T_f^{(2)}[s, (a,b)] = (1/|Sol|^{k-2}) * #{(c3,...,ck) in Sol^{k-2} :
                            f(a,b,c3,...,ck) = s}
    Returns: T as |Sol| x |Sol|^2 matrix, T_tensor as |Sol| x |Sol| x |Sol|.
    """
    sol_list = list(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n_avg = k - 2

    T = np.zeros((S, S * S), dtype=np.float64)

    if n_avg <= 0:
        raise ValueError("k must be >= 3")

    total_avg_tuples = S ** n_avg
    if num_mc_samples is None:
        num_mc_samples = min(total_avg_tuples, MC_BUDGET_MULTI)
    use_exact = (total_avg_tuples <= num_mc_samples)

    if use_exact:
        for a_idx, a in enumerate(sol_list):
            for b_idx, b in enumerate(sol_list):
                col = a_idx * S + b_idx
                for avg_combo in cartesian_product(sol_list, repeat=n_avg):
                    inputs = [a, b] + list(avg_combo)
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        T[sol_to_idx[result], col] += 1.0
        T /= (S ** n_avg)
    else:
        for a_idx, a in enumerate(sol_list):
            for b_idx, b in enumerate(sol_list):
                col = a_idx * S + b_idx
                for _ in range(num_mc_samples):
                    avg = [sol_list[random.randint(0, S-1)] for _ in range(n_avg)]
                    inputs = [a, b] + avg
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        T[sol_to_idx[result], col] += 1.0
        T /= num_mc_samples

    T_tensor = T.reshape(S, S, S)
    return T, T_tensor


# ============================================================
# 4. Single-slot T_f^{(1)} (K-14 comparison)
# ============================================================

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
        T /= (S ** n_avg)
    else:
        for a_idx, a in enumerate(sol_list):
            for _ in range(num_mc_samples):
                avg = [sol_list[random.randint(0, S-1)] for _ in range(n_avg)]
                inputs = [a] + avg
                result = coordinatewise_threshold_k(inputs, k)
                if result in sol_to_idx:
                    T[sol_to_idx[result], a_idx] += 1.0
        T /= num_mc_samples

    return T


# ============================================================
# 5. Symmetrized T_f^{sym}
# ============================================================

def compute_T_symmetrized(solutions, k, num_mc_samples=None):
    """
    T_f^{sym}[s, a] = (1/k) sum_{j=1}^{k} T_f^{(j)}[s, a]
    T_f^{(j)}: live slot at position j, (k-1) others averaged.
    """
    sol_list = list(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n_avg = k - 1

    T_sym = np.zeros((S, S), dtype=np.float64)
    total_avg_tuples = S ** n_avg
    if num_mc_samples is None:
        num_mc_samples = min(total_avg_tuples, MC_BUDGET_SYM)
    use_exact = (total_avg_tuples <= num_mc_samples)

    for live_pos in range(k):
        T_j = np.zeros((S, S), dtype=np.float64)
        if use_exact:
            for a_idx, a in enumerate(sol_list):
                for avg_combo in cartesian_product(sol_list, repeat=n_avg):
                    inputs = list(avg_combo[:live_pos]) + [a] + list(avg_combo[live_pos:])
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        T_j[sol_to_idx[result], a_idx] += 1.0
            T_j /= (S ** n_avg)
        else:
            for a_idx, a in enumerate(sol_list):
                for _ in range(num_mc_samples):
                    avg = [sol_list[random.randint(0, S-1)] for _ in range(n_avg)]
                    inputs = avg[:live_pos] + [a] + avg[live_pos:]
                    result = coordinatewise_threshold_k(inputs, k)
                    if result in sol_to_idx:
                        T_j[sol_to_idx[result], a_idx] += 1.0
            T_j /= num_mc_samples
        T_sym += T_j

    T_sym /= k
    return T_sym


# ============================================================
# 6. Analysis helpers
# ============================================================

def analyze_matrix(M, label=""):
    S = M.shape[0]
    eigenvalues = np.linalg.eigvals(M)
    eigenvalues_real = np.sort(np.real(eigenvalues))[::-1]
    trace = np.trace(M)
    scalar = trace / S
    dev_scalar = np.linalg.norm(M - scalar * np.eye(S), 'fro') / max(np.linalg.norm(M, 'fro'), 1e-15)
    dev_identity = np.linalg.norm(M - np.eye(S), 'fro')
    rank = np.linalg.matrix_rank(M, tol=1e-10)
    return {
        'label': label, 'size': S, 'rank': rank,
        'eigenvalues_real': eigenvalues_real,
        'lambda_1': eigenvalues_real[0] if len(eigenvalues_real) > 0 else None,
        'lambda_2': eigenvalues_real[1] if len(eigenvalues_real) > 1 else None,
        'lambda_min': eigenvalues_real[-1] if len(eigenvalues_real) > 0 else None,
        'trace': trace, 'scalar_coefficient': scalar,
        'deviation_from_scalar_I': dev_scalar,
        'deviation_from_identity': dev_identity,
    }


def compute_commutator_norms(M, S):
    """||[M, y]||_2 for generators y = |i><j|. Returns max, mean."""
    norms = []
    for i in range(S):
        for j in range(S):
            y = np.zeros((S, S))
            y[i, j] = 1.0
            comm = M @ y - y @ M
            norms.append(np.linalg.norm(comm, 'fro') / np.sqrt(S))
    return max(norms), np.mean(norms)


def analyze_multislot(T_tensor, S):
    """Analyze multi-slot tensor for rank collapse and per-b commutators."""
    T_matrix = T_tensor.reshape(S, S * S)
    svs = np.linalg.svd(T_matrix, compute_uv=False)
    rank = int(np.sum(svs > 1e-10))
    sv_ratio = svs[1] / svs[0] if len(svs) > 1 and svs[0] > 1e-15 else 0.0

    per_b_ranks = []
    per_b_comm_max = []
    per_b_comm_mean = []
    for b_idx in range(S):
        T_b = T_tensor[:, :, b_idx]
        per_b_ranks.append(np.linalg.matrix_rank(T_b, tol=1e-10))
        mx, mn = compute_commutator_norms(T_b, S)
        per_b_comm_max.append(mx)
        per_b_comm_mean.append(mn)

    return {
        'numerical_rank': rank,
        'singular_values_top5': svs[:min(5, len(svs))].tolist(),
        'sv_ratio_2_to_1': sv_ratio,
        'per_b_rank_min': min(per_b_ranks),
        'per_b_rank_max': max(per_b_ranks),
        'per_b_rank_mean': np.mean(per_b_ranks),
        'avg_over_b_comm_max': np.mean(per_b_comm_max),
        'avg_over_b_comm_mean': np.mean(per_b_comm_mean),
    }


# ============================================================
# 7. Experiments
# ============================================================

def run_instance_scan():
    """Experiment 1: Instance-size scan at k=3."""
    print("=" * 70)
    print("  EXPERIMENT 1: Instance-size scan (k=3 majority)")
    print("  Single-slot (K-14) vs Multi-slot (2 live) vs Symmetrized")
    print("=" * 70)

    results = []
    for n in [4, 6, 8, 10]:
        instance = generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4)
        if instance is None:
            print(f"  n={n}: FAILED to generate instance")
            continue
        n_vars, clauses, sols = instance
        S = len(sols)
        k = 3
        is_poly, _, _ = verify_polymorphism_threshold_k(sols, k)
        print(f"\n  n={n}, |Sol|={S}, poly={'PASS' if is_poly else 'FAIL'}")
        if not is_poly:
            continue

        t0 = time.time()
        T_s = compute_T_singleslot(sols, k)
        a_s = analyze_matrix(T_s)
        mc_s, mn_s = compute_commutator_norms(T_s, S)

        _, T_tensor = compute_T_multislot_2live(sols, k)
        m_a = analyze_multislot(T_tensor, S)

        T_sym = compute_T_symmetrized(sols, k)
        a_sym = analyze_matrix(T_sym)
        mc_sym, mn_sym = compute_commutator_norms(T_sym, S)
        elapsed = time.time() - t0

        print(f"  Single: rank={a_s['rank']}/{S}, max||[T,y]||={mc_s:.8f}, "
              f"lam2={a_s['lambda_2']:.6f}, dev_sc={a_s['deviation_from_scalar_I']:.6f}")
        print(f"  Multi:  rank={m_a['numerical_rank']}/{S}, sv_ratio={m_a['sv_ratio_2_to_1']:.6f}, "
              f"avg_max||[T_b,y]||={m_a['avg_over_b_comm_max']:.8f}")
        print(f"  Sym:    rank={a_sym['rank']}/{S}, max||[T,y]||={mc_sym:.8f}, "
              f"lam2={a_sym['lambda_2']:.6f}")
        print(f"  [{elapsed:.1f}s]")

        results.append({
            'n': n, 'S': S, 'k': k,
            'single_max_comm': mc_s, 'single_dev_scalar': a_s['deviation_from_scalar_I'],
            'single_lambda2': a_s['lambda_2'], 'single_lambda_min': a_s['lambda_min'],
            'single_rank': a_s['rank'],
            'multi_rank': m_a['numerical_rank'], 'multi_sv_ratio': m_a['sv_ratio_2_to_1'],
            'multi_avg_max_comm': m_a['avg_over_b_comm_max'],
            'multi_per_b_rank_min': m_a['per_b_rank_min'],
            'multi_per_b_rank_max': m_a['per_b_rank_max'],
            'sym_max_comm': mc_sym, 'sym_dev_scalar': a_sym['deviation_from_scalar_I'],
            'sym_lambda2': a_sym['lambda_2'], 'sym_lambda_min': a_sym['lambda_min'],
            'sym_rank': a_sym['rank'],
        })
    return results


def run_arity_scan(label, seed_offset=0, clause_ratio=1.0):
    """Experiment 2/3: Arity scan at fixed n=8."""
    saved = random.getstate()
    random.seed(42 + seed_offset)
    np.random.seed(42 + seed_offset)

    print(f"\n\n{'='*70}")
    print(f"  EXPERIMENT: Arity scan [{label}] (n=8, varying k)")
    print(f"{'='*70}")

    instance = generate_2sat_instance(8, clause_ratio=clause_ratio, min_solutions=4)
    random.setstate(saved)
    np.random.seed(42)

    if instance is None:
        print("  FAILED")
        return []
    n_vars, clauses, sols = instance
    S = len(sols)
    print(f"  Instance: n={n_vars}, |Sol|={S}")

    results = []
    for k in [3, 5, 7, 9, 11]:
        is_poly, viol, total = verify_polymorphism_threshold_k(sols, k)
        print(f"\n  k={k}: poly={'PASS' if is_poly else 'FAIL'} ({viol}/{total})")
        if not is_poly:
            continue

        t0 = time.time()

        # Tune MC budget based on k and S to stay feasible
        # Multi-slot: S^2 pairs, each needs mc_samples evaluations
        # Total evals ~ S^2 * mc_samples * k ops per eval
        mc_multi = min(S ** (k-2), max(3000, MC_BUDGET_MULTI // max(1, k-3)))
        mc_sym = min(S ** (k-1), max(3000, MC_BUDGET_SYM // max(1, k-3)))

        T_s = compute_T_singleslot(sols, k, num_mc_samples=min(S**(k-1), 30000))
        a_s = analyze_matrix(T_s)
        mc_s, _ = compute_commutator_norms(T_s, S)

        _, T_tensor = compute_T_multislot_2live(sols, k, num_mc_samples=mc_multi)
        m_a = analyze_multislot(T_tensor, S)

        T_sym = compute_T_symmetrized(sols, k, num_mc_samples=mc_sym)
        a_sym = analyze_matrix(T_sym)
        mc_sym_v, _ = compute_commutator_norms(T_sym, S)

        elapsed = time.time() - t0
        print(f"  Single: max||[T,y]||={mc_s:.8f}, dev_sc={a_s['deviation_from_scalar_I']:.6f}, "
              f"lam2={a_s['lambda_2']:.6f}, lam_min={a_s['lambda_min']:.6f}")
        print(f"  Multi:  sv_ratio={m_a['sv_ratio_2_to_1']:.6f}, rank={m_a['numerical_rank']}/{S}, "
              f"avg_max||[T_b,y]||={m_a['avg_over_b_comm_max']:.8f}")
        print(f"  Sym:    max||[T,y]||={mc_sym_v:.8f}, dev_sc={a_sym['deviation_from_scalar_I']:.6f}, "
              f"lam2={a_sym['lambda_2']:.6f}, lam_min={a_sym['lambda_min']:.6f}")
        print(f"  [{elapsed:.1f}s]")

        results.append({
            'k': k, 'S': S,
            'single_max_comm': mc_s, 'single_dev_scalar': a_s['deviation_from_scalar_I'],
            'single_lambda2': a_s['lambda_2'], 'single_lambda_min': a_s['lambda_min'],
            'multi_rank': m_a['numerical_rank'], 'multi_sv_ratio': m_a['sv_ratio_2_to_1'],
            'multi_avg_max_comm': m_a['avg_over_b_comm_max'],
            'sym_max_comm': mc_sym_v, 'sym_dev_scalar': a_sym['deviation_from_scalar_I'],
            'sym_lambda2': a_sym['lambda_2'], 'sym_lambda_min': a_sym['lambda_min'],
            'sym_rank': a_sym['rank'],
        })
    return results


# ============================================================
# 8. Synthesis
# ============================================================

def print_synthesis(inst_res, arity1, arity2):
    print("\n\n" + "=" * 70)
    print("  SYNTHESIS: Multi-slot vs Single-slot vs Symmetrized")
    print("=" * 70)

    print("\n  TABLE 1: Instance-size scaling (k=3)")
    print(f"  {'n':>4s} {'|Sol|':>5s}  {'1-slot max':>11s} {'2-slot avg':>11s} {'sym max':>11s}  "
          f"{'multi-rank':>10s} {'sv_ratio':>8s}")
    print(f"  {'-'*4} {'-'*5}  {'-'*11} {'-'*11} {'-'*11}  {'-'*10} {'-'*8}")
    for r in inst_res:
        print(f"  {r['n']:4d} {r['S']:5d}  {r['single_max_comm']:11.8f} "
              f"{r['multi_avg_max_comm']:11.8f} {r['sym_max_comm']:11.8f}  "
              f"{r['multi_rank']:4d}/{r['S']:<4d}  {r['multi_sv_ratio']:8.6f}")

    for label, data in [("TABLE 2: Arity scan (primary)", arity1),
                        ("TABLE 3: Arity scan (second instance)", arity2)]:
        if not data:
            continue
        print(f"\n  {label}")
        print(f"  {'k':>4s} {'|Sol|':>5s}  {'1-slot max':>11s} {'2-slot avg':>11s} {'sym max':>11s}  "
              f"{'1-slot dev':>10s} {'sym dev':>10s} {'sv_ratio':>8s}")
        print(f"  {'-'*4} {'-'*5}  {'-'*11} {'-'*11} {'-'*11}  {'-'*10} {'-'*10} {'-'*8}")
        for r in data:
            print(f"  {r['k']:4d} {r['S']:5d}  {r['single_max_comm']:11.8f} "
                  f"{r['multi_avg_max_comm']:11.8f} {r['sym_max_comm']:11.8f}  "
                  f"{r['single_dev_scalar']:10.6f} {r['sym_dev_scalar']:10.6f} "
                  f"{r['multi_sv_ratio']:8.6f}")

    # Scaling analysis
    print("\n\n  SCALING ANALYSIS (arity dependence)")
    print("  " + "-" * 60)
    for data_label, data in [("Primary", arity1), ("Second", arity2)]:
        if len(data) < 3:
            continue
        print(f"\n  [{data_label} instance, |Sol|={data[0]['S']}]")
        ks = np.array([r['k'] for r in data], dtype=float)
        log_ks = np.log(ks)

        for name, key in [("Single-slot  max||[T,y]||", 'single_max_comm'),
                          ("Multi-slot   avg max||[T_b,y]||", 'multi_avg_max_comm'),
                          ("Symmetrized  max||[T,y]||", 'sym_max_comm')]:
            vals = np.array([r[key] for r in data])
            if all(v > 0 for v in vals):
                log_v = np.log(vals)
                c = np.polyfit(log_ks, log_v, 1)
                r2 = 1 - np.sum((log_v - np.polyval(c, log_ks))**2) / \
                     max(np.sum((log_v - np.mean(log_v))**2), 1e-30)
                d = "INCREASING" if c[0] > 0.05 else ("DECREASING" if c[0] < -0.05 else "FLAT")
                print(f"    {name}: ~ k^{c[0]:+.4f}  (R^2={r2:.3f})  [{d}]")

        sv_ratios = [r['multi_sv_ratio'] for r in data]
        print(f"\n    Multi-slot SV ratio sigma_2/sigma_1:")
        for r in data:
            tag = ("RANK-1 COLLAPSE" if r['multi_sv_ratio'] < 0.01
                   else ("NEAR COLLAPSE" if r['multi_sv_ratio'] < 0.1 else "HEALTHY"))
            print(f"      k={r['k']:2d}: {r['multi_sv_ratio']:.6f}  [{tag}]")

    # Symmetrized analysis
    print("\n\n  SYMMETRIZED vs SINGLE-SLOT COMPARISON")
    print("  " + "-" * 60)
    if len(arity1) >= 2:
        print("  Are they the same operator?")
        for r in arity1:
            ratio = r['sym_max_comm'] / max(r['single_max_comm'], 1e-15)
            print(f"    k={r['k']:2d}: sym/single comm ratio = {ratio:.6f}")

    # Deviation from scalar
    print("\n  Deviation from scalar * I:")
    for data_label, data in [("Primary", arity1), ("Second", arity2)]:
        if not data:
            continue
        print(f"  [{data_label}]")
        for r in data:
            print(f"    k={r['k']:2d}: single={r['single_dev_scalar']:.6f}, "
                  f"sym={r['sym_dev_scalar']:.6f}")

    # VERDICT
    print("\n\n" + "=" * 70)
    print("  VERDICT")
    print("=" * 70)

    if len(arity1) >= 3:
        mc_single = [r['single_max_comm'] for r in arity1]
        mc_multi = [r['multi_avg_max_comm'] for r in arity1]
        mc_sym = [r['sym_max_comm'] for r in arity1]
        sv_r = [r['multi_sv_ratio'] for r in arity1]

        single_trend = mc_single[-1] - mc_single[0]
        multi_trend = mc_multi[-1] - mc_multi[0]
        sym_trend = mc_sym[-1] - mc_sym[0]
        sv_trend = sv_r[-1] - sv_r[0]

        print(f"\n  1. RANK-1 COLLAPSE (multi-slot):")
        print(f"     SV ratio: {sv_r[0]:.4f} (k={arity1[0]['k']}) -> {sv_r[-1]:.4f} (k={arity1[-1]['k']})")
        if sv_r[-1] < sv_r[0] * 0.3:
            print(f"     COLLAPSE occurs even with 2 live slots. K-14 extends.")
        elif sv_r[-1] < sv_r[0] * 0.7:
            print(f"     PARTIAL collapse. 2 live slots DELAY but may not prevent.")
        else:
            print(f"     NO collapse. 2 live slots PREVENT rank-1 convergence.")

        print(f"\n  2. COMMUTATOR NORM TRENDS:")
        for name, vals, trend in [("Single-slot", mc_single, single_trend),
                                  ("Multi-slot", mc_multi, multi_trend),
                                  ("Symmetrized", mc_sym, sym_trend)]:
            d = "INCREASING" if trend > 0.001 else ("DECREASING" if trend < -0.001 else "FLAT")
            print(f"     {name}: {vals[0]:.6f} -> {vals[-1]:.6f} [{d}]")

        print(f"\n  3. KEY OBSERVATION:")
        # Check if multi-slot commutator decreases even though single-slot increases
        if multi_trend < -0.001 and single_trend > 0.001:
            print(f"     CRITICAL: Multi-slot commutators DECREASE while single-slot INCREASES.")
            print(f"     The 2-live-slot construction REVERSES the K-14 pathology.")
        elif multi_trend < -0.001:
            print(f"     Multi-slot commutators decrease. Promising.")
        elif multi_trend > 0.001 and single_trend > 0.001:
            print(f"     Both single and multi-slot commutators increase.")
            print(f"     The K-14 pathology persists despite 2 live slots.")
        else:
            print(f"     Trends are mixed. Inconclusive at this scale.")

        # Check symmetrized == single-slot
        sym_eq_single = all(
            abs(r['sym_max_comm'] - r['single_max_comm']) < 0.01 * max(r['single_max_comm'], 1e-10)
            for r in arity1
        )
        if sym_eq_single:
            print(f"\n  4. SYMMETRIZED = SINGLE-SLOT (to within MC noise).")
            print(f"     The symmetrized construction is IDENTICAL to single-slot.")
            print(f"     Reason: threshold-k is already symmetric in all k inputs.")
            print(f"     Averaging over slot positions has no effect for symmetric f.")
        else:
            print(f"\n  4. Symmetrized differs from single-slot (non-trivial averaging).")

        # Final verdict
        multi_decreasing = multi_trend < -0.005
        sv_healthy = sv_r[-1] > 0.1
        single_increasing = single_trend > 0.005

        if multi_decreasing and sv_healthy:
            verdict = "CLOSES"
            print(f"\n  FINAL VERDICT: {verdict}")
            print(f"  Multi-slot avoids rank-1 collapse AND produces decreasing commutators.")
        elif sv_healthy and abs(multi_trend) < 0.005:
            verdict = "INCONCLUSIVE"
            print(f"\n  FINAL VERDICT: {verdict}")
            print(f"  No rank-1 collapse, but commutator trend is unclear at this scale.")
        else:
            verdict = "KILLS"
            print(f"\n  FINAL VERDICT: {verdict}")
            print(f"  S4 (multi-slot) does NOT save Gap Alpha.")
            if not sv_healthy:
                print(f"  Rank-1 collapse still occurs with 2 live slots.")
            if not multi_decreasing:
                print(f"  Multi-slot commutator norms do not decrease with arity.")

            # Specific kill mechanism
            if sv_r[-1] < 0.1 and single_trend > 0:
                print(f"\n  KILL MECHANISM (K-15): Multi-slot rank collapse.")
                print(f"  Even with 2 live slots, omega-averaging over (k-2) slots")
                print(f"  still concentrates. The extra live slot only delays the")
                print(f"  collapse from O(k) to O(k-1) auxiliary slots. The Law of")
                print(f"  Large Numbers dominates for k-2 >= 3 (i.e., k >= 5).")
            elif multi_trend > 0:
                print(f"\n  KILL MECHANISM (K-15): Multi-slot commutator increase.")
                print(f"  The per-b slices T(:,:,b) inherit increasing commutator")
                print(f"  norms from the concentration of the (k-2) averaged slots.")

        return verdict
    else:
        print("  INSUFFICIENT DATA")
        return "INCONCLUSIVE"


# ============================================================
# 9. Main
# ============================================================

def main():
    print("=" * 70)
    print("  GAP ALPHA MULTI-SLOT CONSTRUCTION -- Node 1.3.5.2")
    print("  Salvage S4: 2 live slots + (k-2) averaged")
    print("  Author: Claude Opus 4.6 (1M context)")
    print("  Date: 2026-04-11")
    print("=" * 70)
    print()

    inst_results = run_instance_scan()
    arity1 = run_arity_scan("Primary", seed_offset=0, clause_ratio=1.0)
    arity2 = run_arity_scan("Second", seed_offset=957, clause_ratio=1.2)

    verdict = print_synthesis(inst_results, arity1, arity2)
    print(f"\n  Node 1.3.5.2 complete. Status: {verdict}")
    print("=" * 70)


if __name__ == "__main__":
    main()
