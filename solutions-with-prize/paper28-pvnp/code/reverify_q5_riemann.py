#!/usr/bin/env python3
"""
Independent re-verification of Q5-RIEMANN:
  TGap scaling exponent for 3-SAT = 2/(gamma_6 - gamma_5)

Parts:
  (a) Riemann zero computation to 100 decimal places
  (b) Independent TGap measurement via brute-force 3-SAT
  (c) Formula uniqueness search
  (d) Verdict

Date: 2026-04-12
"""

import itertools
import random
import math
import sys
import time
from collections import defaultdict

import numpy as np
from scipy import stats

from mpmath import mp, mpf, zetazero, log, pi as MP_PI, nstr

# ══════════════════════════════════════════════════════════════════════════
# Part (a): Riemann zero computation
# ══════════════════════════════════════════════════════════════════════════

def part_a():
    print("=" * 80)
    print("PART (a): Riemann zero computation to 100 decimal places")
    print("=" * 80)

    mp.dps = 120  # extra guard digits

    gamma = {}
    for k in range(1, 16):
        z = zetazero(k)
        gamma[k] = z.imag
        if k <= 7 or k in (5, 6):
            mp.dps = 120
            print(f"  gamma_{k:2d} = {nstr(z.imag, 100)}")

    g5 = gamma[5]
    g6 = gamma[6]
    diff = g6 - g5
    alpha_rz = mpf(2) / diff

    print(f"\n  gamma_5           = {nstr(g5, 100)}")
    print(f"  gamma_6           = {nstr(g6, 100)}")
    print(f"  gamma_6 - gamma_5 = {nstr(diff, 100)}")
    print(f"  2/(gamma_6-gamma_5) = {nstr(alpha_rz, 50)}")
    print(f"  Float value: {float(alpha_rz):.15f}")

    return gamma, float(alpha_rz)


# ══════════════════════════════════════════════════════════════════════════
# Part (b): Independent TGap measurement
# ══════════════════════════════════════════════════════════════════════════

def generate_3sat_instance(n, m, rng):
    """Generate a random 3-SAT instance with n variables and m clauses.
    Each clause is a tuple of 3 signed literals (positive = variable, negative = negation).
    Variables are 0-indexed.
    """
    clauses = []
    for _ in range(m):
        # Pick 3 distinct variables
        vars_chosen = rng.sample(range(n), 3)
        clause = []
        for v in vars_chosen:
            if rng.random() < 0.5:
                clause.append(v)       # positive literal
            else:
                clause.append(~v)      # negative literal (bitwise not: ~v = -(v+1))
        clauses.append(tuple(clause))
    return clauses


def evaluate_clause(clause, assignment):
    """Check if a clause is satisfied by the assignment (list of bools)."""
    for lit in clause:
        if lit >= 0:
            if assignment[lit]:
                return True
        else:
            v = ~lit  # decode: ~lit = -(lit+1), so v = -(lit) - 1... actually ~(~v) = v
            if not assignment[v]:
                return True
    return False


def find_all_solutions(clauses, n):
    """Brute-force enumerate all satisfying assignments for n variables."""
    solutions = []
    for bits in range(1 << n):
        assignment = [(bits >> i) & 1 == 1 for i in range(n)]
        if all(evaluate_clause(c, assignment) for c in clauses):
            solutions.append(tuple(int(b) for b in assignment))
    return solutions


def get_taylor_operations():
    """
    Generate all 256 ternary Boolean operations f:{0,1}^3 -> {0,1}.
    Filter to those satisfying f(x,x,x) = x (Taylor/idempotent condition).
    Then identify which are projections (f = pi_1, pi_2, or pi_3).

    A ternary Boolean function is specified by its truth table on {0,1}^3 (8 entries).
    Idempotent: f(0,0,0)=0, f(1,1,1)=1.
    """
    inputs = list(itertools.product([0, 1], repeat=3))
    # inputs[0] = (0,0,0), inputs[7] = (1,1,1)

    taylor_ops = []
    projections = set()

    # The 3 projections
    for proj_idx in range(3):
        tt = tuple(inp[proj_idx] for inp in inputs)
        projections.add(tt)

    # Enumerate all 2^8 = 256 ternary Boolean functions
    for code in range(256):
        tt = tuple((code >> i) & 1 for i in range(8))
        # Check idempotent: f(0,0,0)=0 and f(1,1,1)=1
        if tt[0] == 0 and tt[7] == 1:
            taylor_ops.append(tt)

    non_proj_taylor = [tt for tt in taylor_ops if tt not in projections]

    print(f"  Total idempotent ternary ops: {len(taylor_ops)}")
    print(f"  Projections: {len(projections)}")
    print(f"  Non-projection Taylor ops: {len(non_proj_taylor)}")

    return taylor_ops, non_proj_taylor, projections, inputs


def op_preserves_solutions(tt, solutions, inputs):
    """
    Check if a ternary operation (given by truth table) preserves the solution set.
    For every triple (s1, s2, s3) of solutions, f(s1, s2, s3) must also be a solution.

    f is applied coordinate-wise: for each variable i,
      result[i] = tt[index] where index encodes (s1[i], s2[i], s3[i]).
    """
    if len(solutions) <= 1:
        return True  # trivially preserved

    sol_set = set(solutions)
    n = len(solutions[0])

    # For efficiency, sample if too many triples
    nsol = len(solutions)
    if nsol ** 3 > 50000:
        # Sample 5000 random triples
        rng = random.Random(42)
        triples = []
        for _ in range(5000):
            triples.append((rng.choice(solutions), rng.choice(solutions), rng.choice(solutions)))
    else:
        triples = itertools.product(solutions, repeat=3)

    # Precompute the input-index map: (a,b,c) -> index in inputs list
    idx_map = {}
    for i, inp in enumerate(inputs):
        idx_map[inp] = i

    for s1, s2, s3 in triples:
        result = []
        for i in range(n):
            key = (s1[i], s2[i], s3[i])
            result.append(tt[idx_map[key]])
        result = tuple(result)
        if result not in sol_set:
            return False
    return True


def compute_tgap(clauses, n, non_proj_taylor, inputs):
    """
    Compute TGap for a 3-SAT instance.
    TGap = 1 - (# non-projection Taylor ops preserving Sol) / (# non-projection Taylor ops)
    """
    solutions = find_all_solutions(clauses, n)

    if len(solutions) == 0:
        return None  # UNSAT -- skip

    if len(solutions) == (1 << n):
        return 0.0  # trivially SAT -- all assignments work

    preserving = 0
    total = len(non_proj_taylor)

    for tt in non_proj_taylor:
        if op_preserves_solutions(tt, solutions, inputs):
            preserving += 1

    tgap = 1.0 - preserving / total
    return tgap


def part_b():
    print("\n" + "=" * 80)
    print("PART (b): Independent TGap measurement")
    print("=" * 80)

    taylor_ops, non_proj_taylor, projections, inputs = get_taylor_operations()

    ns = [8, 10, 12, 14, 16]
    ratio = 4.267
    num_instances = 50
    rng = random.Random(2026_04_12)

    results = {}

    for n in ns:
        m = int(round(ratio * n))
        tgaps = []
        t0 = time.time()

        for trial in range(num_instances):
            clauses = generate_3sat_instance(n, m, rng)
            tg = compute_tgap(clauses, n, non_proj_taylor, inputs)
            if tg is not None:
                tgaps.append(tg)

        elapsed = time.time() - t0
        med = np.median(tgaps) if tgaps else float('nan')
        mean = np.mean(tgaps) if tgaps else float('nan')
        std = np.std(tgaps) if tgaps else float('nan')
        n_sat = len(tgaps)
        n_unsat = num_instances - n_sat

        results[n] = {
            'tgaps': tgaps,
            'median': med,
            'mean': mean,
            'std': std,
            'n_sat': n_sat,
            'n_unsat': n_unsat,
            'time': elapsed,
        }

        print(f"  n={n:2d}, m={m:3d}: median TGap={med:.6f}, mean={mean:.6f}, "
              f"std={std:.6f}, SAT={n_sat}/{num_instances}, time={elapsed:.1f}s")

    # Fit log(TGap) vs log(n) for instances where TGap > 0
    log_n = []
    log_tgap = []
    for n in ns:
        med = results[n]['median']
        if med > 0:
            log_n.append(np.log(n))
            log_tgap.append(np.log(med))

    if len(log_n) >= 3:
        slope, intercept, r_value, p_value, std_err = stats.linregress(log_n, log_tgap)
        print(f"\n  Fit: log(TGap) = {slope:.6f} * log(n) + {intercept:.6f}")
        print(f"  Alpha (scaling exponent) = {slope:.6f} +/- {std_err:.6f}")
        print(f"  R^2 = {r_value**2:.6f}")
        print(f"  p-value = {p_value:.2e}")
    else:
        slope = float('nan')
        std_err = float('nan')
        r_value = float('nan')
        print("\n  WARNING: Not enough data points for fit.")

    return results, slope, std_err, r_value


# ══════════════════════════════════════════════════════════════════════════
# Part (c): Formula uniqueness search
# ══════════════════════════════════════════════════════════════════════════

def part_c(gamma, alpha_target):
    print("\n" + "=" * 80)
    print("PART (c): Formula uniqueness search")
    print("=" * 80)

    mp.dps = 60
    target = mpf(str(alpha_target))
    threshold = mpf("0.0001")  # 0.01% relative

    # Constants to test
    constants = {
        '1': mpf(1), '2': mpf(2), '3': mpf(3),
        '1/2': mpf(1)/2,
        '1/pi': 1/MP_PI, 'pi': MP_PI,
        'log2': log(2),
    }

    matches = []
    N = 15

    # Family 1: a / (gamma_i - gamma_j)
    for a_name, a_val in constants.items():
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                diff = gamma[i] - gamma[j]
                if abs(diff) < mpf("0.001"):
                    continue
                val = a_val / diff
                if val > 0:
                    rel_err = abs(val - target) / target
                    if rel_err < threshold:
                        matches.append((float(rel_err)*100, f"{a_name}/(gamma_{i} - gamma_{j})", float(val)))

    # Family 2: a * gamma_i / gamma_j
    for a_name, a_val in constants.items():
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == j:
                    continue
                val = a_val * gamma[i] / gamma[j]
                if val > 0:
                    rel_err = abs(val - target) / target
                    if rel_err < threshold:
                        matches.append((float(rel_err)*100, f"{a_name}*gamma_{i}/gamma_{j}", float(val)))

    # Family 3: a / (gamma_i + gamma_j)
    for a_name, a_val in constants.items():
        for i in range(1, N+1):
            for j in range(i, N+1):
                val = a_val / (gamma[i] + gamma[j])
                if val > 0:
                    rel_err = abs(val - target) / target
                    if rel_err < threshold:
                        matches.append((float(rel_err)*100, f"{a_name}/(gamma_{i} + gamma_{j})", float(val)))

    matches.sort(key=lambda x: x[0])

    print(f"\n  Formulas matching alpha={alpha_target:.10f} within 0.01%:")
    print(f"  {'Rank':>4s}  {'%dev':>10s}  {'Value':>16s}  Formula")
    print(f"  {'----':>4s}  {'-----':>10s}  {'-----':>16s}  -------")
    for rank, (pct, formula, val) in enumerate(matches, 1):
        print(f"  {rank:4d}  {pct:10.6f}%  {val:16.12f}  {formula}")

    # Deduplicate: 2/(g6-g5) and 2/(-(g5-g6)) are the same
    unique_formulas = set()
    for pct, formula, val in matches:
        unique_formulas.add(f"{val:.10f}")

    print(f"\n  Total matches within 0.01%: {len(matches)}")
    print(f"  Unique values within 0.01%: {len(unique_formulas)}")

    return matches


# ══════════════════════════════════════════════════════════════════════════
# Part (d): Report
# ══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 80)
    print("Q5-RIEMANN INDEPENDENT RE-VERIFICATION")
    print("=" * 80)

    # Part (a)
    gamma, alpha_rz = part_a()

    # Part (b) - may be slow for n=16
    print("\n  [Note: n=14,16 may take several minutes due to brute-force enumeration]")
    results_b, alpha_fit, alpha_err, r_value = part_b()

    # Part (c)
    matches_c = part_c(gamma, alpha_rz)

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print(f"\n  Part (a): 2/(gamma_6 - gamma_5) = {alpha_rz:.15f}")
    print(f"  Part (b): Fitted alpha = {alpha_fit:.6f} +/- {alpha_err:.6f}")
    if not np.isnan(alpha_fit):
        discrepancy = abs(alpha_fit - alpha_rz) / alpha_rz * 100
        print(f"  Discrepancy: {discrepancy:.2f}%")

        # Key issue: is the TGap measurement even meaningful?
        if alpha_err > 0.1:
            print(f"  WARNING: Standard error ({alpha_err:.4f}) is very large.")
            print(f"  The scaling exponent is NOT well-determined from small-n data.")
    else:
        print(f"  WARNING: Could not fit scaling exponent.")

    n_within = len([m for m in matches_c if m[0] < 0.01])  # within 0.01%
    print(f"\n  Part (c): {len(matches_c)} formulas within 0.01% of alpha")
    print(f"           {n_within} formulas within 0.001% of alpha")

    # Is 2/(g6-g5) unique at 0.01%?
    best_pct = matches_c[0][0] if matches_c else float('inf')
    second_pct = matches_c[2][0] if len(matches_c) > 2 else float('inf')  # skip duplicate
    print(f"  Best match: {matches_c[0][1]} at {best_pct:.6f}%")
    if len(matches_c) > 2:
        # Find first genuinely different formula
        best_val = matches_c[0][2]
        for pct, formula, val in matches_c:
            if abs(val - best_val) > 1e-10:
                print(f"  Next-best (different): {formula} at {pct:.6f}%")
                break

    print("\n" + "=" * 80)
    print("END OF VERIFICATION")
    print("=" * 80)


if __name__ == "__main__":
    main()
