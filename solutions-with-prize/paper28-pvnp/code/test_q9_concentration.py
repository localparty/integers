#!/usr/bin/env python3
"""
Q9 — Concentration Strengthens Test
====================================
Tests whether the PU-distance d_k of polymorphism-averaged unitaries
INCREASES with arity k for P-time Schaefer classes (2-SAT, Horn-SAT),
and shows NO pattern for NPC classes (3-SAT).

Run 1 found: concentration strengthens (d_k increases with k).
Critic predicted: dilution (d_k decreases with k).
This script settles the question numerically.
"""

import numpy as np
from itertools import product
import json
import time
import sys

np.random.seed(42)

# ─────────────────────────────────────────────────────────────────
# 1. Instance generation and solution enumeration
# ─────────────────────────────────────────────────────────────────

def all_assignments(n):
    """All 2^n binary strings of length n."""
    return np.array(list(product([0, 1], repeat=n)), dtype=np.int8)

def random_2sat_instance(n, m):
    """Random 2-SAT: m clauses, each a disjunction of 2 literals."""
    clauses = []
    for _ in range(m):
        vs = np.random.choice(n, size=2, replace=False)
        signs = np.random.choice([0, 1], size=2)  # 0=positive, 1=negated
        clauses.append((vs, signs))
    return clauses

def random_horn_instance(n, m):
    """Random Horn-SAT: m clauses, each has at most 1 positive literal.
    Format: (positive_var_or_None, list_of_negated_vars)
    We store as general clauses for uniform evaluation."""
    clauses = []
    for _ in range(m):
        width = np.random.choice([2, 3])
        vs = np.random.choice(n, size=width, replace=False)
        # Horn: at most 1 positive literal
        signs = np.ones(width, dtype=int)  # all negated
        pos_idx = np.random.randint(width + 1)  # might be width = no positive
        if pos_idx < width:
            signs[pos_idx] = 0
        clauses.append((vs, signs))
    return clauses

def random_3sat_instance(n, m):
    """Random 3-SAT: m clauses of width 3."""
    clauses = []
    for _ in range(m):
        vs = np.random.choice(n, size=3, replace=False)
        signs = np.random.choice([0, 1], size=3)
        clauses.append((vs, signs))
    return clauses

def evaluate_clause(assignment, clause):
    """Check if assignment satisfies clause (vs, signs).
    Literal: if sign=0, variable must be 1; if sign=1, variable must be 0.
    Clause is OR of literals."""
    vs, signs = clause
    for v, s in zip(vs, signs):
        lit_val = assignment[v] if s == 0 else (1 - assignment[v])
        if lit_val == 1:
            return True
    return False

def enumerate_solutions(n, clauses):
    """Brute-force enumerate all solutions."""
    all_a = all_assignments(n)
    sols = []
    for a in all_a:
        if all(evaluate_clause(a, c) for c in clauses):
            sols.append(a)
    if len(sols) == 0:
        return None
    return np.array(sols, dtype=np.int8)

def generate_satisfiable_instances(n, num_instances, gen_func, clause_ratio=2.0):
    """Generate satisfiable instances, retrying until we get enough.
    Aim for instances with 5-200 solutions for meaningful statistics."""
    instances = []
    attempts = 0
    m = int(clause_ratio * n)
    while len(instances) < num_instances and attempts < 500:
        attempts += 1
        clauses = gen_func(n, m)
        sols = enumerate_solutions(n, clauses)
        if sols is not None and 3 <= len(sols) <= 200:
            instances.append((clauses, sols))
    return instances

# ─────────────────────────────────────────────────────────────────
# 2. Polymorphisms
# ─────────────────────────────────────────────────────────────────

def median_polymorphism(bits):
    """Majority/median: returns 1 if majority of inputs are 1.
    For even k, breaks ties toward 1 (doesn't matter much)."""
    return (np.sum(bits, axis=0) > len(bits) / 2).astype(np.int8)

def and_polymorphism(bits):
    """AND: returns 1 only if all inputs are 1."""
    return np.all(bits, axis=0).astype(np.int8)

def random_ternary_op(bits):
    """A random ternary function (no algebraic structure).
    Vectorized: XOR of all inputs plus some nonlinear mixing."""
    # Fast deterministic but non-algebraic function
    k = len(bits)
    # XOR all inputs, then flip based on AND of first two
    result = bits[0].copy()
    for i in range(1, k):
        result = result ^ bits[i]
    # Add nonlinear mixing: flip where first two inputs agree
    if k >= 2:
        mask = (bits[0] == bits[1])
        result[mask] = 1 - result[mask]
    return result

# ─────────────────────────────────────────────────────────────────
# 3. PU-distance computation
# ─────────────────────────────────────────────────────────────────

def compute_pu_distance(sols, polymorphism, k, n, max_tuples=5000):
    """
    Compute d_k = |1 - |<U_f>|| where:
    - For each s1 in Sol, compute U_f(s1) = mean over (s2,...,sk) tuples
      of exp(2*pi*i * hamming_agreement(f(s1,...,sk), s1) / n)
    - <U_f> = mean over s1 of U_f(s1)
    - d_k = |1 - |<U_f>||

    Returns d_k and auxiliary info.
    """
    num_sols = len(sols)

    # For each s1, compute average phase
    phases_per_s1 = []

    # Sample s1 from solutions (use all if feasible, else sample)
    s1_indices = range(num_sols) if num_sols <= 30 else np.random.choice(num_sols, 30, replace=False)

    for s1_idx in s1_indices:
        s1 = sols[s1_idx]

        # Number of (k-1)-tuples
        total_tuples = num_sols ** (k - 1)

        num_samples = min(total_tuples, max_tuples)
        # Batch: generate all index tuples at once
        if total_tuples <= max_tuples:
            # Enumerate all tuples via meshgrid
            grids = [np.arange(num_sols)] * (k - 1)
            idx_arrays = np.meshgrid(*grids, indexing='ij')
            idx_flat = np.stack([a.ravel() for a in idx_arrays], axis=1)  # (total, k-1)
        else:
            idx_flat = np.random.randint(0, num_sols, size=(num_samples, k - 1))

        # Process in batches to avoid memory blowup
        batch_size = 2000
        phase_sum = 0.0
        count = 0
        for b_start in range(0, len(idx_flat), batch_size):
            b_end = min(b_start + batch_size, len(idx_flat))
            batch_idx = idx_flat[b_start:b_end]
            batch_phases = np.zeros(b_end - b_start, dtype=complex)
            for t, combo in enumerate(batch_idx):
                bits = np.stack([s1] + [sols[j] for j in combo])
                f_result = polymorphism(bits)
                agreement = np.sum(f_result == s1)
                batch_phases[t] = np.exp(2j * np.pi * agreement / n)
            phase_sum += np.sum(batch_phases)
            count += (b_end - b_start)
        avg_phase = phase_sum / count

        phases_per_s1.append(avg_phase)

    # Grand average
    grand_avg = np.mean(phases_per_s1)
    d_k = abs(1.0 - abs(grand_avg))

    # Also compute std of phases as alternative measure
    phase_angles = np.angle(phases_per_s1)
    phase_std = np.std(phase_angles)

    return d_k, abs(grand_avg), phase_std

# ─────────────────────────────────────────────────────────────────
# 4. Main test
# ─────────────────────────────────────────────────────────────────

def run_test(name, gen_func, polymorphism, n_values, k_values,
             num_instances=20, clause_ratio=2.0):
    """Run the concentration test for a given CSP class."""
    results = {}

    for n in n_values:
        print(f"\n  n={n}:", flush=True)
        instances = generate_satisfiable_instances(n, num_instances, gen_func, clause_ratio)
        print(f"    Generated {len(instances)} satisfiable instances", flush=True)

        if len(instances) < 3:
            print(f"    WARNING: too few instances, adjusting clause ratio")
            # Try with fewer clauses
            for cr in [1.5, 1.0, 2.5, 3.0]:
                instances = generate_satisfiable_instances(n, num_instances, gen_func, cr)
                if len(instances) >= 5:
                    print(f"    Got {len(instances)} with ratio={cr}")
                    break

        results[n] = {}
        for k in k_values:
            dk_values = []
            mag_values = []
            std_values = []

            for inst_idx, (clauses, sols) in enumerate(instances):
                dk, mag, pstd = compute_pu_distance(sols, polymorphism, k, n)
                dk_values.append(dk)
                mag_values.append(mag)
                std_values.append(pstd)

            mean_dk = np.mean(dk_values)
            std_dk = np.std(dk_values)
            mean_mag = np.mean(mag_values)
            mean_pstd = np.mean(std_values)

            results[n][k] = {
                'mean_dk': float(mean_dk),
                'std_dk': float(std_dk),
                'mean_magnitude': float(mean_mag),
                'mean_phase_std': float(mean_pstd),
                'num_instances': len(instances),
            }

            print(f"    k={k}: d_k = {mean_dk:.6f} ± {std_dk:.6f}  "
                  f"|<U>| = {mean_mag:.6f}  phase_std = {mean_pstd:.6f}", flush=True)

    return results

def run_3sat_test(n_values, k_values, num_instances=20):
    """Special test for 3-SAT: try random ternary ops."""
    results = {}

    for n in n_values:
        print(f"\n  n={n}:", flush=True)
        instances = generate_satisfiable_instances(n, num_instances, random_3sat_instance, 3.0)
        if len(instances) < 3:
            instances = generate_satisfiable_instances(n, num_instances, random_3sat_instance, 2.5)
        print(f"    Generated {len(instances)} satisfiable instances", flush=True)

        results[n] = {}
        for k in k_values:
            dk_values = []
            mag_values = []

            for inst_idx, (clauses, sols) in enumerate(instances):
                # Try random ternary op (no true polymorphism for 3-SAT)
                dk, mag, pstd = compute_pu_distance(sols, random_ternary_op, k, n)
                dk_values.append(dk)
                mag_values.append(mag)

            mean_dk = np.mean(dk_values)
            std_dk = np.std(dk_values)
            mean_mag = np.mean(mag_values)

            results[n][k] = {
                'mean_dk': float(mean_dk),
                'std_dk': float(std_dk),
                'mean_magnitude': float(mean_mag),
                'num_instances': len(instances),
            }

            print(f"    k={k}: d_k = {mean_dk:.6f} ± {std_dk:.6f}  "
                  f"|<U>| = {mean_mag:.6f}", flush=True)

    return results

def check_monotonicity(results):
    """Check if d_k is monotonically increasing with k."""
    for n, data in results.items():
        ks = sorted(data.keys())
        dks = [data[k]['mean_dk'] for k in ks]
        increasing = all(dks[i] <= dks[i+1] for i in range(len(dks)-1))
        # Weaker: overall trend (last > first)
        trend = dks[-1] > dks[0]
        yield n, ks, dks, increasing, trend

def main():
    print("=" * 70)
    print("Q9 — CONCENTRATION STRENGTHENS TEST")
    print("=" * 70)

    n_values = [8, 10]
    k_values = [3, 5, 7, 9]

    all_results = {}

    # ── 2-SAT (median polymorphism) ──
    print("\n[1/3] 2-SAT with MEDIAN polymorphism")
    print("-" * 50)
    twosat_results = run_test(
        "2-SAT", random_2sat_instance, median_polymorphism,
        n_values, k_values, num_instances=20, clause_ratio=2.0
    )
    all_results['2-SAT'] = twosat_results

    # ── Horn-SAT (AND polymorphism) ──
    print("\n\n[2/3] Horn-SAT with AND polymorphism")
    print("-" * 50)
    horn_results = run_test(
        "Horn-SAT", random_horn_instance, and_polymorphism,
        n_values, k_values, num_instances=20, clause_ratio=2.0
    )
    all_results['Horn-SAT'] = horn_results

    # ── 3-SAT (no polymorphism) ──
    print("\n\n[3/3] 3-SAT with random ternary op (no polymorphism)")
    print("-" * 50)
    threesat_results = run_3sat_test(n_values, k_values, num_instances=20)
    all_results['3-SAT'] = threesat_results

    # ── Analysis ──
    print("\n" + "=" * 70)
    print("ANALYSIS")
    print("=" * 70)

    verdict_parts = []

    for name in ['2-SAT', 'Horn-SAT']:
        print(f"\n{name}:")
        for n, ks, dks, mono, trend in check_monotonicity(all_results[name]):
            status = "MONO-INCREASING" if mono else ("TREND-UP" if trend else "NO PATTERN")
            print(f"  n={n}: d_k = {['%.6f' % d for d in dks]}  => {status}")
            verdict_parts.append((name, n, mono, trend))

    print(f"\n3-SAT:")
    for n, ks, dks, mono, trend in check_monotonicity(all_results['3-SAT']):
        status = "MONO-INCREASING" if mono else ("TREND-UP" if trend else "NO PATTERN / FLAT")
        print(f"  n={n}: d_k = {['%.6f' % d for d in dks]}  => {status}")

    # Overall verdict
    p_time_pass = all(mono or trend for name, n, mono, trend in verdict_parts)

    if p_time_pass:
        verdict = "PASS"
    elif any(mono or trend for name, n, mono, trend in verdict_parts):
        verdict = "PARTIAL"
    else:
        verdict = "KILL"

    print(f"\n{'=' * 70}")
    print(f"VERDICT: {verdict}")
    print(f"{'=' * 70}")

    # Save raw results
    output = {
        'results': {},
        'verdict': verdict,
    }
    for name, data in all_results.items():
        output['results'][name] = {}
        for n, kdata in data.items():
            output['results'][name][str(n)] = {
                str(k): v for k, v in kdata.items()
            }

    json_path = __file__.replace('.py', '_results.json')
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nRaw results saved to {json_path}")

    return all_results, verdict

if __name__ == '__main__':
    t0 = time.time()
    all_results, verdict = main()
    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")
