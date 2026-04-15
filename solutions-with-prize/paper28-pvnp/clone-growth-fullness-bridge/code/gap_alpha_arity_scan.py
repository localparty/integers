"""
Gap Alpha Arity Scan -- the critical test.

The first computation showed that commutator norms decrease with instance size n,
but this is the trivial dimension-dilution effect (~ 1/sqrt(|Sol|)).

The REAL question for Gap Alpha is: at FIXED instance (fixed n, fixed Sol),
does ||[T_{f_k}, y]||_2 decrease as the arity k of the polymorphism increases?

For 2-SAT, we have Taylor polymorphisms at every odd arity k = 3, 5, 7, 9, ...
by composing majority:
  - k=3: maj(a,b,c)
  - k=5: maj(a, maj(b,c,d), maj(e,f,g))  -- but this has arity 7, not 5

Actually, for 2-SAT the correct approach: construct explicit k-ary Taylor
polymorphisms at arity k by iterated composition. The simplest family:

  f_3(a,b,c) = maj(a,b,c)
  f_5(a,b,c,d,e) = maj(a, maj(b,c,d), e)    -- arity 5 Taylor term
  f_7(a,b,c,d,e,f,g) = maj(a, maj(b,c,d), maj(e,f,g))  -- arity 7

But there are also DIRECT Taylor terms at every prime arity > 2 by Barto et al.
For the Boolean domain {0,1}, a natural family: threshold functions.

  f_k(x_1,...,x_k) = 1 if sum(x_i) > k/2, 0 otherwise

This is the (strict) majority for each arity k. It is Taylor: f_k(x,...,x) = x.
And for 2-SAT, threshold functions ARE polymorphisms (they preserve all 2-clauses).

Proof: a 2-clause (x_i OR x_j) is satisfied iff x_i + x_j >= 1.
If a^(1),...,a^(k) all satisfy it, then sum_l a^(l)_i + sum_l a^(l)_j >= k.
So at least one of sum a^(l)_i or sum a^(l)_j is > k/2, hence at least
one of f_k(a^(1)_i,...,a^(k)_i) or f_k(a^(1)_j,...,a^(k)_j) is 1.
So f_k(a^(1),...,a^(k)) satisfies the clause.

Author: Claude Opus 4.6 (1M context), Node 1.3.5.1
Date: 2026-04-11
"""

import numpy as np
import random
from itertools import product as cartesian_product
import sys

random.seed(42)
np.set_printoptions(precision=6, suppress=True, linewidth=120)


def generate_2sat_instance(n, clause_ratio=1.0, min_solutions=4, max_attempts=500):
    """Generate a random 2-SAT instance with at least min_solutions solutions."""
    num_clauses = int(n * clause_ratio)
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


def enumerate_solutions_2sat(n, clauses):
    """Brute-force enumerate all solutions of a 2-SAT instance."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause_2sat(assignment, c) for c in clauses):
            solutions.append(assignment)
    return solutions


def evaluate_clause_2sat(assignment, clause):
    v0, s0, v1, s1 = clause
    lit0 = assignment[v0] if s0 == 1 else 1 - assignment[v0]
    lit1 = assignment[v1] if s1 == 1 else 1 - assignment[v1]
    return lit0 or lit1


def threshold_k(coords, k):
    """
    k-ary threshold function (generalized majority).
    Returns 1 if sum(coords) > k/2, 0 if sum(coords) < k/2.
    For odd k: standard majority.
    For even k: use strict threshold > k/2.

    coords: tuple of k binary values
    """
    s = sum(coords)
    if s > k / 2:
        return 1
    elif s < k / 2:
        return 0
    else:
        # Tie-breaking: use 0 (this makes it Taylor: f(x,...,x) = x for x in {0,1})
        # Actually for even k, f(0,...,0)=0 and f(1,...,1)=1, so Taylor holds.
        # For the tie case (s = k/2), we need to break ties.
        # Standard: use "median" convention = 0 for ties.
        return 0


def coordinatewise_threshold_k(tuples, k):
    """
    Apply threshold_k coordinatewise to k binary tuples.
    tuples: list of k tuples, each of length n.
    Returns: tuple of length n.
    """
    n = len(tuples[0])
    result = []
    for i in range(n):
        coords = tuple(t[i] for t in tuples)
        result.append(threshold_k(coords, k))
    return tuple(result)


def verify_polymorphism_k(solutions, k):
    """
    Verify that threshold_k is a polymorphism for the given solution set.
    For large k and large |Sol|, we sample instead of exhaustive check.
    """
    sol_set = set(solutions)
    S = len(solutions)

    if S**k <= 100000:
        # Exhaustive check
        violations = 0
        total = 0
        # For efficiency, iterate using indices
        for combo in cartesian_product(range(S), repeat=k):
            total += 1
            tuples = [solutions[i] for i in combo]
            result = coordinatewise_threshold_k(tuples, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, total
    else:
        # Sampling
        num_samples = 50000
        violations = 0
        for _ in range(num_samples):
            tuples = [solutions[random.randint(0, S-1)] for _ in range(k)]
            result = coordinatewise_threshold_k(tuples, k)
            if result not in sol_set:
                violations += 1
        return violations == 0, violations, num_samples


def compute_T_fk(solutions, k, max_tuples=None):
    """
    Compute the clone operator T_{f_k} for arity-k threshold function.

    T_{f_k}[s, a] = (1/|Sol|^{k-1}) * #{(a^(2),...,a^(k)) in Sol^{k-1} :
                                          f_k(a, a^(2),...,a^(k)) = s}

    For large k and |Sol|, we use sampling.
    """
    sol_list = list(solutions)
    sol_set = set(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}

    T = np.zeros((S, S), dtype=np.float64)

    total_tuples = S ** (k - 1)

    if total_tuples <= 500000:
        # Exact computation
        for a_idx, a in enumerate(sol_list):
            for combo in cartesian_product(range(S), repeat=k-1):
                aux_tuples = [sol_list[i] for i in combo]
                all_tuples = [a] + aux_tuples
                result = coordinatewise_threshold_k(all_tuples, k)
                if result in sol_to_idx:
                    s_idx = sol_to_idx[result]
                    T[s_idx, a_idx] += 1.0
        T /= total_tuples
    else:
        # Monte Carlo estimation
        num_samples = max_tuples if max_tuples else min(200000, total_tuples)
        for a_idx, a in enumerate(sol_list):
            samples_per_a = num_samples // S
            for _ in range(samples_per_a):
                aux_tuples = [sol_list[random.randint(0, S-1)] for _ in range(k-1)]
                all_tuples = [a] + aux_tuples
                result = coordinatewise_threshold_k(all_tuples, k)
                if result in sol_to_idx:
                    s_idx = sol_to_idx[result]
                    T[s_idx, a_idx] += 1.0
            T[:, a_idx] /= samples_per_a

    return T


def compute_commutator_norms(T, S):
    """Compute max and mean commutator norms."""
    norms = []
    for i in range(S):
        for j in range(S):
            y = np.zeros((S, S))
            y[i, j] = 1.0
            comm = T @ y - y @ T
            norm_2 = np.linalg.norm(comm, 'fro') / np.sqrt(S)
            norms.append(norm_2)
    return max(norms), np.mean(norms)


def main():
    print("=" * 70)
    print("  GAP ALPHA ARITY SCAN -- The Critical Test")
    print("  Fixed instance, varying arity k = 3, 5, 7, 9, 11")
    print("=" * 70)

    # Use a FIXED 2-SAT instance at n=8 (manageable size)
    random.seed(42)
    instance = generate_2sat_instance(8, clause_ratio=1.0, min_solutions=8)
    if instance is None:
        print("FAILED to generate instance")
        return

    n, clauses, solutions = instance
    S = len(solutions)
    print(f"\nFixed instance: n={n}, |Sol|={S}")
    print(f"Clauses: {len(clauses)}")

    arities = [3, 5, 7, 9, 11]
    results = []

    for k in arities:
        print(f"\n{'='*60}")
        print(f"  Arity k = {k}")
        print(f"{'='*60}")

        # Verify polymorphism
        print(f"  Verifying threshold-{k} is a polymorphism...", end=" ", flush=True)
        is_poly, violations, total = verify_polymorphism_k(solutions, k)
        if is_poly:
            print(f"PASS ({total} checked, 0 violations)")
        else:
            print(f"FAIL ({violations}/{total} violations)")
            print(f"  ERROR: threshold-{k} should be a polymorphism for 2-SAT!")
            continue

        # Compute T_{f_k}
        total_k = S ** (k-1)
        is_exact = total_k <= 500000
        print(f"  Computing T_{{f_{k}}} ({S}x{S}, {total_k} tuples, {'exact' if is_exact else 'Monte Carlo'})...", end=" ", flush=True)
        T = compute_T_fk(solutions, k)
        print("done.")

        # Eigenvalues
        eigenvalues = np.sort(np.real(np.linalg.eigvals(T)))[::-1]

        # Commutator norms
        print(f"  Computing commutator norms...", end=" ", flush=True)
        max_comm, mean_comm = compute_commutator_norms(T, S)
        print("done.")

        # Is column-stochastic?
        col_sums = T.sum(axis=0)
        is_col_stoch = np.allclose(col_sums, 1.0, atol=1e-6)

        # Deviation from scalar
        trace = np.trace(T)
        scalar = trace / S
        T_dev = T - scalar * np.eye(S)
        dev_scalar = np.linalg.norm(T_dev, 'fro') / np.linalg.norm(T, 'fro')

        # Deviation from identity
        dev_identity = np.linalg.norm(T - np.eye(S), 'fro')

        print(f"  Results:")
        print(f"    Column-stochastic: {is_col_stoch}")
        print(f"    lambda_1 (leading): {eigenvalues[0]:.8f}")
        print(f"    lambda_2: {eigenvalues[1]:.8f}")
        print(f"    Spectral gap (1-lambda_2): {1-eigenvalues[1]:.8f}")
        print(f"    lambda_min: {eigenvalues[-1]:.8f}")
        print(f"    trace/|Sol|: {scalar:.8f}")
        print(f"    ||T - scalar*I||/||T||: {dev_scalar:.8f}")
        print(f"    ||T - I||: {dev_identity:.8f}")
        print(f"    max ||[T, y]||_2: {max_comm:.8f}")
        print(f"    mean ||[T, y]||_2: {mean_comm:.8f}")

        results.append({
            'k': k,
            'leading_eig': eigenvalues[0],
            'second_eig': eigenvalues[1],
            'spectral_gap': 1 - eigenvalues[1],
            'min_eig': eigenvalues[-1],
            'scalar_coeff': scalar,
            'dev_scalar': dev_scalar,
            'dev_identity': dev_identity,
            'max_comm': max_comm,
            'mean_comm': mean_comm,
            'col_stochastic': is_col_stoch,
        })

    # --------------------------------------------------------
    # SCALING ANALYSIS
    # --------------------------------------------------------
    print("\n\n" + "=" * 70)
    print("  ARITY SCALING ANALYSIS (fixed n={}, |Sol|={})".format(n, S))
    print("=" * 70)

    print(f"\n  {'k':>4s}  {'max||[T,y]||':>14s}  {'mean||[T,y]||':>14s}  {'1-lambda_2':>12s}  {'lambda_min':>12s}  {'dev_scalar':>12s}  {'||T-I||':>10s}")
    print(f"  {'-'*4}  {'-'*14}  {'-'*14}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*10}")
    for r in results:
        print(f"  {r['k']:4d}  {r['max_comm']:14.8f}  {r['mean_comm']:14.8f}  {r['spectral_gap']:12.8f}  {r['min_eig']:12.8f}  {r['dev_scalar']:12.8f}  {r['dev_identity']:10.6f}")

    # Key question: does max_comm decrease with k?
    ks = np.array([r['k'] for r in results], dtype=float)
    max_comms = np.array([r['max_comm'] for r in results])
    mean_comms = np.array([r['mean_comm'] for r in results])
    dev_ids = np.array([r['dev_identity'] for r in results])

    if len(ks) >= 3:
        # Fit power law
        log_k = np.log(ks)
        log_mc = np.log(max_comms)
        coeffs = np.polyfit(log_k, log_mc, 1)
        r_sq = 1 - np.sum((log_mc - np.polyval(coeffs, log_k))**2) / np.sum((log_mc - np.mean(log_mc))**2)

        print(f"\n  max||[T_{{f_k}}, y]||_2 vs k (power law):")
        print(f"    Exponent: {coeffs[0]:.4f}")
        print(f"    R^2: {r_sq:.6f}")

        # Fit exponential
        coeffs_exp = np.polyfit(ks, log_mc, 1)
        r_sq_exp = 1 - np.sum((log_mc - np.polyval(coeffs_exp, ks))**2) / np.sum((log_mc - np.mean(log_mc))**2)
        print(f"\n  max||[T_{{f_k}}, y]||_2 vs k (exponential fit):")
        print(f"    Rate: exp({coeffs_exp[0]:.4f} * k)")
        print(f"    R^2: {r_sq_exp:.6f}")

        # Does ||T - I|| decrease with k?
        print(f"\n  ||T_{{f_k}} - I|| vs k:")
        log_dev = np.log(dev_ids)
        coeffs_dev = np.polyfit(log_k, log_dev, 1)
        r_sq_dev = 1 - np.sum((log_dev - np.polyval(coeffs_dev, log_k))**2) / np.sum((log_dev - np.mean(log_dev))**2)
        print(f"    Exponent: {coeffs_dev[0]:.4f}")
        print(f"    R^2: {r_sq_dev:.6f}")

        decreasing_comm = all(max_comms[i] >= max_comms[i+1] for i in range(len(max_comms)-1))
        decreasing_dev = all(dev_ids[i] >= dev_ids[i+1] for i in range(len(dev_ids)-1))

        print(f"\n  Commutator norms monotonically decreasing? {decreasing_comm}")
        print(f"  ||T-I|| monotonically decreasing? {decreasing_dev}")

        if decreasing_comm and coeffs[0] < -0.1:
            print(f"\n  GAP ALPHA EVIDENCE: CLOSING")
            print(f"  The commutator norm DECREASES with arity k at FIXED instance size.")
            print(f"  This is the genuine concentration effect, not dimension dilution.")
            print(f"  Rate: ~ k^{{{coeffs[0]:.3f}}}")
        elif not decreasing_comm:
            print(f"\n  GAP ALPHA EVIDENCE: NON-MONOTONIC")
            print(f"  The commutator norm does not decrease monotonically with k.")
        else:
            print(f"\n  GAP ALPHA EVIDENCE: INCONCLUSIVE")
            print(f"  Decrease is too slow to confirm concentration.")

    # Also run on a second instance to check instance-independence
    print("\n\n" + "=" * 70)
    print("  SECOND INSTANCE (verification of instance-independence)")
    print("=" * 70)

    random.seed(123)
    instance2 = generate_2sat_instance(8, clause_ratio=1.0, min_solutions=8)
    if instance2 is None:
        print("FAILED to generate second instance")
        return

    n2, clauses2, solutions2 = instance2
    S2 = len(solutions2)
    print(f"  Second instance: n={n2}, |Sol|={S2}")

    results2 = []
    for k in [3, 5, 7, 9]:
        is_poly, _, _ = verify_polymorphism_k(solutions2, k)
        if not is_poly:
            print(f"  k={k}: polymorphism FAILED, skipping")
            continue

        T2 = compute_T_fk(solutions2, k)
        max_c2, mean_c2 = compute_commutator_norms(T2, S2)
        dev_id2 = np.linalg.norm(T2 - np.eye(S2), 'fro')

        results2.append({'k': k, 'max_comm': max_c2, 'dev_identity': dev_id2})
        print(f"  k={k}: max||[T,y]||_2 = {max_c2:.8f}, ||T-I|| = {dev_id2:.6f}")

    if len(results2) >= 3:
        ks2 = np.array([r['k'] for r in results2], dtype=float)
        mc2 = np.array([r['max_comm'] for r in results2])
        log_k2 = np.log(ks2)
        log_mc2 = np.log(mc2)
        coeffs2 = np.polyfit(log_k2, log_mc2, 1)
        print(f"\n  Second instance: max||[T,y]||_2 ~ k^{coeffs2[0]:.4f}")
        decr2 = all(mc2[i] >= mc2[i+1] for i in range(len(mc2)-1))
        print(f"  Monotonically decreasing? {decr2}")


if __name__ == "__main__":
    main()
