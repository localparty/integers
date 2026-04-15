#!/usr/bin/env python3
"""
test_a1_j_duality.py — A1: Modular conjugation J-duality between P and NPC sectors

Conjecture (A1, strategy/10-amplification-entries.md):
  There exists an antiunitary-like map J that exchanges the P-time sector
  and the NPC sector of M_Bool. If J M_Bool^P J = M_Bool^{NPC}, then the
  two sectors are DUAL — related by a structural bijection analogous to
  the Tomita-Takesaki J exchanging M_int and M_ext in black hole physics.

Operationalization:
  We cannot compute the actual modular conjugation J on a type III_1 factor.
  Instead we test for a finite-dimensional analog: structural bijections
  between P-time solution spaces and NPC constraint structures.

Tests (n=8,10; 30 random instances each of 2-SAT and 3-SAT):
  1. Solution space profiles (|Sol|, Hamming distance distribution,
     connected components of Hamming-1 graph, adjacency spectrum)
  2. Constraint space profiles (clause count, clause overlap distribution,
     constraint graph Laplacian spectrum)
  3. J-duality test: cross-spectral comparison between 2-SAT solution
     graph eigenvalues and 3-SAT constraint graph eigenvalues
  4. Complement test: anti-solution set of 3-SAT vs P-time structure
  5. Spectral duality: product/sum relationships between paired spectra

Author: G Six, with Claude Opus 4.6. Date: 2026-04-11.
"""

import random
import itertools
import numpy as np
from collections import Counter, defaultdict
import json
import os
import warnings

warnings.filterwarnings("ignore")

random.seed(42)
np.random.seed(42)

N_INSTANCES = 30

# =====================================================================
#  CSP GENERATORS
# =====================================================================

def gen_2sat(n, ratio=2.0):
    """Generate a random 2-SAT instance at given clause/variable ratio."""
    m = int(ratio * n)
    return [[v if random.random() < 0.5 else -v
             for v in random.sample(range(1, n + 1), 2)]
            for _ in range(m)]

def gen_3sat(n, ratio=4.0):
    """Generate a random 3-SAT instance at given clause/variable ratio."""
    m = int(ratio * n)
    return [[v if random.random() < 0.5 else -v
             for v in random.sample(range(1, n + 1), 3)]
            for _ in range(m)]

# =====================================================================
#  SOLUTION ENUMERATION
# =====================================================================

def assignment_to_int(assignment, n):
    """Convert {1: True, 2: False, ...} to integer index."""
    val = 0
    for i in range(n):
        if assignment.get(i + 1, False):
            val |= (1 << i)
    return val

def int_to_assignment(val, n):
    """Convert integer to {1: True/False, ...} dict."""
    return {i + 1: bool(val & (1 << i)) for i in range(n)}

def evaluate_clause(clause, assignment):
    """Check if a single clause is satisfied."""
    for lit in clause:
        var = abs(lit)
        val = assignment.get(var, False)
        if (lit > 0 and val) or (lit < 0 and not val):
            return True
    return False

def evaluate_formula(clauses, assignment):
    """Check if all clauses are satisfied."""
    return all(evaluate_clause(c, assignment) for c in clauses)

def enumerate_solutions(clauses, n):
    """Brute-force enumerate all solutions for n-variable formula."""
    solutions = []
    for x in range(2**n):
        assignment = int_to_assignment(x, n)
        if evaluate_formula(clauses, assignment):
            solutions.append(x)
    return solutions

def enumerate_nonsolutions(clauses, n):
    """Enumerate the complement: all non-solutions."""
    solutions_set = set(enumerate_solutions(clauses, n))
    return [x for x in range(2**n) if x not in solutions_set]

# =====================================================================
#  SOLUTION SPACE PROFILE
# =====================================================================

def hamming_distance(a, b, n):
    """Hamming distance between two integers interpreted as n-bit strings."""
    xor = a ^ b
    return bin(xor).count('1')

def solution_space_profile(solutions, n):
    """
    Compute the full solution space profile:
      - |Sol|
      - Hamming distance distribution
      - Number of connected components in Hamming-1 graph
      - Eigenvalues of the adjacency matrix
      - Eigenvalues of the Laplacian
    """
    num_sol = len(solutions)
    profile = {
        "num_solutions": num_sol,
        "hamming_distribution": {},
        "num_components": 0,
        "adjacency_eigenvalues": [],
        "laplacian_eigenvalues": [],
    }

    if num_sol == 0:
        return profile

    if num_sol == 1:
        profile["hamming_distribution"] = {}
        profile["num_components"] = 1
        profile["adjacency_eigenvalues"] = [0.0]
        profile["laplacian_eigenvalues"] = [0.0]
        return profile

    # Hamming distance distribution
    hamming_counts = Counter()
    for i in range(num_sol):
        for j in range(i + 1, num_sol):
            d = hamming_distance(solutions[i], solutions[j], n)
            hamming_counts[d] += 1
    profile["hamming_distribution"] = dict(sorted(hamming_counts.items()))

    # Adjacency matrix (Hamming-1 graph)
    adj = np.zeros((num_sol, num_sol), dtype=float)
    for i in range(num_sol):
        for j in range(i + 1, num_sol):
            if hamming_distance(solutions[i], solutions[j], n) == 1:
                adj[i, j] = 1.0
                adj[j, i] = 1.0

    # Connected components via BFS
    visited = set()
    components = 0
    for start in range(num_sol):
        if start not in visited:
            components += 1
            queue = [start]
            visited.add(start)
            while queue:
                node = queue.pop(0)
                for neighbor in range(num_sol):
                    if neighbor not in visited and adj[node, neighbor] > 0:
                        visited.add(neighbor)
                        queue.append(neighbor)
    profile["num_components"] = components

    # Eigenvalues
    if num_sol <= 1500:  # computational guard
        adj_eigs = np.sort(np.real(np.linalg.eigvalsh(adj)))
        profile["adjacency_eigenvalues"] = adj_eigs.tolist()

        # Laplacian = D - A
        degree = np.diag(np.sum(adj, axis=1))
        laplacian = degree - adj
        lap_eigs = np.sort(np.real(np.linalg.eigvalsh(laplacian)))
        profile["laplacian_eigenvalues"] = lap_eigs.tolist()
    else:
        profile["adjacency_eigenvalues"] = []
        profile["laplacian_eigenvalues"] = []

    return profile

# =====================================================================
#  CONSTRAINT SPACE PROFILE
# =====================================================================

def constraint_space_profile(clauses, n):
    """
    Compute the constraint space profile:
      - Number of clauses m
      - Clause overlap distribution (shared variable pairs)
      - Constraint graph Laplacian eigenvalues
    """
    m = len(clauses)
    profile = {
        "num_clauses": m,
        "clause_overlap_distribution": {},
        "constraint_laplacian_eigenvalues": [],
    }

    if m == 0:
        return profile

    # Clause overlap: count how many variable pairs appear in multiple clauses
    pair_counts = Counter()
    for clause in clauses:
        vars_in_clause = sorted(set(abs(lit) for lit in clause))
        for i in range(len(vars_in_clause)):
            for j in range(i + 1, len(vars_in_clause)):
                pair_counts[(vars_in_clause[i], vars_in_clause[j])] += 1

    overlap_dist = Counter()
    for pair, count in pair_counts.items():
        overlap_dist[count] += 1
    profile["clause_overlap_distribution"] = dict(sorted(overlap_dist.items()))

    # Constraint graph: variables are nodes, edge if they share a clause
    # Weight = number of shared clauses
    adj = np.zeros((n, n), dtype=float)
    for clause in clauses:
        vars_in_clause = sorted(set(abs(lit) for lit in clause))
        for i in range(len(vars_in_clause)):
            for j in range(i + 1, len(vars_in_clause)):
                vi = vars_in_clause[i] - 1  # 0-indexed
                vj = vars_in_clause[j] - 1
                adj[vi, vj] += 1.0
                adj[vj, vi] += 1.0

    degree = np.diag(np.sum(adj, axis=1))
    laplacian = degree - adj
    eigs = np.sort(np.real(np.linalg.eigvalsh(laplacian)))
    profile["constraint_laplacian_eigenvalues"] = eigs.tolist()

    return profile

# =====================================================================
#  COMPLEMENT TEST (Test 4)
# =====================================================================

def ternary_majority(a, b, c):
    """Ternary majority vote, bitwise."""
    return (a & b) | (b & c) | (a & c)

def ternary_minority(a, b, c):
    """Ternary minority (dual majority)."""
    return ternary_majority(a, b, c) ^ ((a ^ b ^ c) & ~ternary_majority(a, b, c))

def check_taylor_closure(elements, n, num_samples=2000):
    """
    Check if a set of bitstrings is closed under various ternary Taylor
    operations (majority, Mal'cev-like). A P-time CSP's solution set must
    admit such closure.

    Returns dict of {operation_name: closure_fraction}.
    """
    if len(elements) < 3:
        return {"majority": 1.0, "minority": 1.0, "affine": 1.0}

    element_set = set(elements)
    results = {}

    # Test majority closure
    majority_closed = 0
    total = 0
    indices = list(range(len(elements)))
    for _ in range(min(num_samples, len(elements)**3)):
        i, j, k = random.choices(indices, k=3)
        a, b, c = elements[i], elements[j], elements[k]
        m = ternary_majority(a, b, c)
        total += 1
        if m in element_set:
            majority_closed += 1
    results["majority"] = majority_closed / total if total > 0 else 0.0

    # Test affine/XOR closure: a XOR b XOR c
    affine_closed = 0
    total = 0
    for _ in range(min(num_samples, len(elements)**3)):
        i, j, k = random.choices(indices, k=3)
        a, b, c = elements[i], elements[j], elements[k]
        x = a ^ b ^ c
        total += 1
        if x in element_set:
            affine_closed += 1
    results["affine"] = affine_closed / total if total > 0 else 0.0

    return results

def complement_test(clauses, n):
    """
    Test 4: Does the anti-solution set of 3-SAT have P-time structure?
    Check if {0,1}^n minus Sol(3-SAT) is closed under Taylor operations.
    """
    nonsolutions = enumerate_nonsolutions(clauses, n)
    num_nonsolutions = len(nonsolutions)
    closure = check_taylor_closure(nonsolutions, n)

    return {
        "num_nonsolutions": num_nonsolutions,
        "taylor_closure": closure,
    }

# =====================================================================
#  SPECTRAL DUALITY TESTS (Tests 3 and 5)
# =====================================================================

def normalize_spectrum(eigs):
    """Normalize eigenvalues to [0, 1] range."""
    if len(eigs) == 0:
        return np.array([])
    eigs = np.array(eigs)
    span = eigs[-1] - eigs[0]
    if span < 1e-12:
        return np.zeros_like(eigs)
    return (eigs - eigs[0]) / span

def interpolate_spectrum(eigs, num_points):
    """Interpolate a spectrum to a fixed number of points for comparison."""
    if len(eigs) == 0:
        return np.zeros(num_points)
    eigs = np.array(eigs, dtype=float)
    x_orig = np.linspace(0, 1, len(eigs))
    x_target = np.linspace(0, 1, num_points)
    return np.interp(x_target, x_orig, eigs)

def spectral_distance(spec1, spec2, num_points=50):
    """
    Compute distance between two spectra after normalizing and
    interpolating to the same grid.
    """
    s1 = interpolate_spectrum(normalize_spectrum(spec1), num_points)
    s2 = interpolate_spectrum(normalize_spectrum(spec2), num_points)
    return np.sqrt(np.mean((s1 - s2)**2))

def test_product_duality(eigs1, eigs2):
    """
    Test: is lambda_i * mu_i = constant?
    Returns (best_constant, relative_spread).
    """
    n1, n2 = len(eigs1), len(eigs2)
    if n1 == 0 or n2 == 0:
        return None, None

    # Interpolate to same length
    k = min(n1, n2, 50)
    s1 = interpolate_spectrum(np.array(eigs1), k)
    s2 = interpolate_spectrum(np.array(eigs2), k)

    products = s1 * s2
    # Skip near-zero entries
    mask = np.abs(products) > 1e-10
    if np.sum(mask) < 3:
        return None, None

    filtered = products[mask]
    mean_prod = np.mean(filtered)
    std_prod = np.std(filtered)
    relative_spread = std_prod / abs(mean_prod) if abs(mean_prod) > 1e-12 else float('inf')
    return float(mean_prod), float(relative_spread)

def test_sum_duality(eigs1, eigs2):
    """
    Test: is lambda_i + mu_i = constant?
    Returns (best_constant, relative_spread).
    """
    n1, n2 = len(eigs1), len(eigs2)
    if n1 == 0 or n2 == 0:
        return None, None

    k = min(n1, n2, 50)
    s1 = interpolate_spectrum(np.array(eigs1), k)
    s2 = interpolate_spectrum(np.array(eigs2), k)

    sums = s1 + s2
    mask = np.abs(sums) > 1e-10
    if np.sum(mask) < 3:
        return None, None

    filtered = sums[mask]
    mean_sum = np.mean(filtered)
    std_sum = np.std(filtered)
    relative_spread = std_sum / abs(mean_sum) if abs(mean_sum) > 1e-12 else float('inf')
    return float(mean_sum), float(relative_spread)

# =====================================================================
#  DISTRIBUTION COMPARISON
# =====================================================================

def distribution_to_vector(dist, max_key=None):
    """Convert {key: count} dict to normalized probability vector."""
    if not dist:
        return np.array([0.0])
    if max_key is None:
        max_key = max(dist.keys())
    vec = np.zeros(max_key + 1)
    total = sum(dist.values())
    if total == 0:
        return vec
    for k, v in dist.items():
        if k <= max_key:
            vec[k] = v / total
    return vec

def kl_divergence(p, q, epsilon=1e-10):
    """Symmetrized KL divergence."""
    p = np.array(p) + epsilon
    q = np.array(q) + epsilon
    p = p / np.sum(p)
    q = q / np.sum(q)
    kl_pq = np.sum(p * np.log(p / q))
    kl_qp = np.sum(q * np.log(q / p))
    return 0.5 * (kl_pq + kl_qp)

def wasserstein_1d(p, q):
    """1D Wasserstein distance between two discrete distributions."""
    max_len = max(len(p), len(q))
    pp = np.zeros(max_len)
    qq = np.zeros(max_len)
    pp[:len(p)] = p
    qq[:len(q)] = q
    # Normalize
    sp, sq = np.sum(pp), np.sum(qq)
    if sp > 0:
        pp /= sp
    if sq > 0:
        qq /= sq
    cdf_p = np.cumsum(pp)
    cdf_q = np.cumsum(qq)
    return np.sum(np.abs(cdf_p - cdf_q))

# =====================================================================
#  MAIN COMPUTATION
# =====================================================================

def run_instance(clauses, n, label):
    """Run all analyses on one instance."""
    solutions = enumerate_solutions(clauses, n)
    sol_profile = solution_space_profile(solutions, n)
    con_profile = constraint_space_profile(clauses, n)

    result = {
        "label": label,
        "n": n,
        "solution_profile": {
            "num_solutions": sol_profile["num_solutions"],
            "hamming_distribution": sol_profile["hamming_distribution"],
            "num_components": sol_profile["num_components"],
            "num_adjacency_eigs": len(sol_profile["adjacency_eigenvalues"]),
            "adjacency_spectral_range": (
                [sol_profile["adjacency_eigenvalues"][0],
                 sol_profile["adjacency_eigenvalues"][-1]]
                if sol_profile["adjacency_eigenvalues"] else None
            ),
            "num_laplacian_eigs": len(sol_profile["laplacian_eigenvalues"]),
            "laplacian_spectral_gap": (
                sol_profile["laplacian_eigenvalues"][1]
                if len(sol_profile["laplacian_eigenvalues"]) > 1 else None
            ),
        },
        "constraint_profile": {
            "num_clauses": con_profile["num_clauses"],
            "clause_overlap_distribution": con_profile["clause_overlap_distribution"],
            "constraint_spectral_gap": (
                con_profile["constraint_laplacian_eigenvalues"][1]
                if len(con_profile["constraint_laplacian_eigenvalues"]) > 1 else None
            ),
        },
        # Store raw spectra for cross-comparison
        "_sol_adj_eigs": sol_profile["adjacency_eigenvalues"],
        "_sol_lap_eigs": sol_profile["laplacian_eigenvalues"],
        "_con_lap_eigs": con_profile["constraint_laplacian_eigenvalues"],
        "_hamming_dist": sol_profile["hamming_distribution"],
        "_clause_overlap": con_profile["clause_overlap_distribution"],
    }

    return result

def run_complement_test_for_instance(clauses, n):
    """Run complement/Taylor test for a 3-SAT instance."""
    return complement_test(clauses, n)

def main():
    print("=" * 72)
    print("  A1: Modular conjugation J-duality between P and NPC sectors")
    print("=" * 72)

    all_results = {}

    for n in [8, 10]:
        print(f"\n{'='*72}")
        print(f"  n = {n}")
        print(f"{'='*72}")

        results_2sat = []
        results_3sat = []
        complement_results = []

        # Generate and analyze 2-SAT instances
        print(f"\n  Generating {N_INSTANCES} 2-SAT instances (n={n})...")
        for i in range(N_INSTANCES):
            clauses = gen_2sat(n)
            result = run_instance(clauses, n, f"2SAT_n{n}_{i}")
            results_2sat.append(result)
            if (i + 1) % 10 == 0:
                print(f"    2-SAT instance {i+1}/{N_INSTANCES}: "
                      f"|Sol| = {result['solution_profile']['num_solutions']}, "
                      f"components = {result['solution_profile']['num_components']}")

        # Generate and analyze 3-SAT instances
        print(f"\n  Generating {N_INSTANCES} 3-SAT instances (n={n})...")
        for i in range(N_INSTANCES):
            clauses = gen_3sat(n)
            result = run_instance(clauses, n, f"3SAT_n{n}_{i}")
            results_3sat.append(result)

            # Also do complement test
            comp = run_complement_test_for_instance(clauses, n)
            complement_results.append(comp)

            if (i + 1) % 10 == 0:
                print(f"    3-SAT instance {i+1}/{N_INSTANCES}: "
                      f"|Sol| = {result['solution_profile']['num_solutions']}, "
                      f"components = {result['solution_profile']['num_components']}")

        # ─────────────────────────────────────────────────────────────
        #  ANALYSIS 1: Solution space statistics
        # ─────────────────────────────────────────────────────────────
        print(f"\n  --- Test 1: Solution Space Profiles (n={n}) ---")

        sat2_sol_counts = [r["solution_profile"]["num_solutions"]
                           for r in results_2sat]
        sat3_sol_counts = [r["solution_profile"]["num_solutions"]
                           for r in results_3sat]
        sat2_components = [r["solution_profile"]["num_components"]
                           for r in results_2sat]
        sat3_components = [r["solution_profile"]["num_components"]
                           for r in results_3sat]
        sat2_gap = [r["solution_profile"]["laplacian_spectral_gap"]
                    for r in results_2sat
                    if r["solution_profile"]["laplacian_spectral_gap"] is not None]
        sat3_gap = [r["solution_profile"]["laplacian_spectral_gap"]
                    for r in results_3sat
                    if r["solution_profile"]["laplacian_spectral_gap"] is not None]

        print(f"    2-SAT: |Sol| mean={np.mean(sat2_sol_counts):.1f}, "
              f"median={np.median(sat2_sol_counts):.0f}, "
              f"components={np.mean(sat2_components):.1f}")
        print(f"    3-SAT: |Sol| mean={np.mean(sat3_sol_counts):.1f}, "
              f"median={np.median(sat3_sol_counts):.0f}, "
              f"components={np.mean(sat3_components):.1f}")
        if sat2_gap:
            print(f"    2-SAT spectral gap: mean={np.mean(sat2_gap):.4f}")
        if sat3_gap:
            print(f"    3-SAT spectral gap: mean={np.mean(sat3_gap):.4f}")

        # ─────────────────────────────────────────────────────────────
        #  ANALYSIS 2: Constraint space statistics
        # ─────────────────────────────────────────────────────────────
        print(f"\n  --- Test 2: Constraint Space Profiles (n={n}) ---")

        sat2_con_gap = [r["constraint_profile"]["constraint_spectral_gap"]
                        for r in results_2sat
                        if r["constraint_profile"]["constraint_spectral_gap"] is not None]
        sat3_con_gap = [r["constraint_profile"]["constraint_spectral_gap"]
                        for r in results_3sat
                        if r["constraint_profile"]["constraint_spectral_gap"] is not None]

        print(f"    2-SAT constraint Laplacian gap: mean={np.mean(sat2_con_gap):.4f}"
              if sat2_con_gap else "    2-SAT constraint gap: N/A")
        print(f"    3-SAT constraint Laplacian gap: mean={np.mean(sat3_con_gap):.4f}"
              if sat3_con_gap else "    3-SAT constraint gap: N/A")

        # ─────────────────────────────────────────────────────────────
        #  ANALYSIS 3: J-duality cross-spectral test
        # ─────────────────────────────────────────────────────────────
        print(f"\n  --- Test 3: J-Duality Cross-Spectral Comparison (n={n}) ---")

        # (a) 2-SAT solution spectrum vs 3-SAT constraint spectrum
        cross_distances_sol_con = []
        for r2 in results_2sat:
            for r3 in results_3sat:
                if r2["_sol_adj_eigs"] and r3["_con_lap_eigs"]:
                    d = spectral_distance(r2["_sol_adj_eigs"],
                                          r3["_con_lap_eigs"])
                    cross_distances_sol_con.append(d)

        # (b) 2-SAT solution spectrum vs 3-SAT solution spectrum (control)
        within_distances_sol = []
        for r2 in results_2sat:
            for r3 in results_3sat:
                if r2["_sol_adj_eigs"] and r3["_sol_adj_eigs"]:
                    d = spectral_distance(r2["_sol_adj_eigs"],
                                          r3["_sol_adj_eigs"])
                    within_distances_sol.append(d)

        # (c) 2-SAT constraint vs 3-SAT constraint (control)
        within_distances_con = []
        for r2 in results_2sat:
            for r3 in results_3sat:
                if r2["_con_lap_eigs"] and r3["_con_lap_eigs"]:
                    d = spectral_distance(r2["_con_lap_eigs"],
                                          r3["_con_lap_eigs"])
                    within_distances_con.append(d)

        if cross_distances_sol_con:
            print(f"    Cross: 2-SAT sol adj vs 3-SAT con Lap: "
                  f"mean dist = {np.mean(cross_distances_sol_con):.4f} "
                  f"+/- {np.std(cross_distances_sol_con):.4f}")
        if within_distances_sol:
            print(f"    Control: 2-SAT sol adj vs 3-SAT sol adj: "
                  f"mean dist = {np.mean(within_distances_sol):.4f} "
                  f"+/- {np.std(within_distances_sol):.4f}")
        if within_distances_con:
            print(f"    Control: 2-SAT con Lap vs 3-SAT con Lap: "
                  f"mean dist = {np.mean(within_distances_con):.4f} "
                  f"+/- {np.std(within_distances_con):.4f}")

        # J-duality test: cross distance should be SMALLER than controls
        # if there is a structural duality
        if cross_distances_sol_con and within_distances_sol:
            j_ratio = np.mean(cross_distances_sol_con) / np.mean(within_distances_sol)
            print(f"    J-ratio (cross/control_sol): {j_ratio:.4f}")
            print(f"    J-duality present if ratio << 1: "
                  f"{'POSSIBLE' if j_ratio < 0.5 else 'NOT FOUND'}")

        # ─────────────────────────────────────────────────────────────
        #  ANALYSIS 3b: Hamming distribution vs clause overlap
        # ─────────────────────────────────────────────────────────────
        print(f"\n  --- Test 3b: Distribution Duality (n={n}) ---")

        hamming_vs_overlap_distances = []
        for r2 in results_2sat:
            for r3 in results_3sat:
                h_dist = r2["_hamming_dist"]
                c_over = r3["_clause_overlap"]
                if h_dist and c_over:
                    max_k = max(max(h_dist.keys(), default=0),
                                max(c_over.keys(), default=0))
                    v1 = distribution_to_vector(h_dist, max_k)
                    v2 = distribution_to_vector(c_over, max_k)
                    w = wasserstein_1d(v1, v2)
                    hamming_vs_overlap_distances.append(w)

        # Control: 2-SAT hamming vs 2-SAT hamming (between different instances)
        hamming_self_distances = []
        for i in range(len(results_2sat)):
            for j in range(i + 1, len(results_2sat)):
                h1 = results_2sat[i]["_hamming_dist"]
                h2 = results_2sat[j]["_hamming_dist"]
                if h1 and h2:
                    max_k = max(max(h1.keys(), default=0),
                                max(h2.keys(), default=0))
                    v1 = distribution_to_vector(h1, max_k)
                    v2 = distribution_to_vector(h2, max_k)
                    w = wasserstein_1d(v1, v2)
                    hamming_self_distances.append(w)

        if hamming_vs_overlap_distances:
            print(f"    Cross: 2-SAT Hamming vs 3-SAT clause overlap: "
                  f"W1 = {np.mean(hamming_vs_overlap_distances):.4f} "
                  f"+/- {np.std(hamming_vs_overlap_distances):.4f}")
        if hamming_self_distances:
            print(f"    Control: 2-SAT Hamming vs 2-SAT Hamming: "
                  f"W1 = {np.mean(hamming_self_distances):.4f} "
                  f"+/- {np.std(hamming_self_distances):.4f}")

        if hamming_vs_overlap_distances and hamming_self_distances:
            dist_ratio = (np.mean(hamming_vs_overlap_distances)
                          / np.mean(hamming_self_distances))
            print(f"    Distribution duality ratio: {dist_ratio:.4f}")
            print(f"    Duality present if ratio ~ 1: "
                  f"{'POSSIBLE' if 0.5 < dist_ratio < 2.0 else 'NOT FOUND'}")

        # ─────────────────────────────────────────────────────────────
        #  ANALYSIS 4: Complement test
        # ─────────────────────────────────────────────────────────────
        print(f"\n  --- Test 4: Complement (Anti-Solution) Test (n={n}) ---")

        majority_closures = [c["taylor_closure"]["majority"]
                             for c in complement_results]
        affine_closures = [c["taylor_closure"]["affine"]
                           for c in complement_results]
        nonsol_counts = [c["num_nonsolutions"] for c in complement_results]

        print(f"    3-SAT anti-solutions: mean |nonSol| = "
              f"{np.mean(nonsol_counts):.1f}")
        print(f"    Majority closure: mean = {np.mean(majority_closures):.4f} "
              f"+/- {np.std(majority_closures):.4f}")
        print(f"    Affine closure: mean = {np.mean(affine_closures):.4f} "
              f"+/- {np.std(affine_closures):.4f}")

        # For comparison, test Taylor closure on 2-SAT SOLUTIONS
        sat2_majority_closures = []
        sat2_affine_closures = []
        for r2 in results_2sat[:10]:  # subset for speed
            sols = enumerate_solutions(
                gen_2sat(n), n)  # re-generate to get actual solutions list
            closure = check_taylor_closure(sols, n)
            sat2_majority_closures.append(closure["majority"])
            sat2_affine_closures.append(closure["affine"])

        if sat2_majority_closures:
            print(f"    2-SAT solutions majority closure: "
                  f"mean = {np.mean(sat2_majority_closures):.4f}")
            print(f"    2-SAT solutions affine closure: "
                  f"mean = {np.mean(sat2_affine_closures):.4f}")

        complement_is_taylor = np.mean(majority_closures) > 0.9
        print(f"    Anti-solution set admits Taylor operation: "
              f"{'YES' if complement_is_taylor else 'NO'}")

        # ─────────────────────────────────────────────────────────────
        #  ANALYSIS 5: Spectral duality (product/sum)
        # ─────────────────────────────────────────────────────────────
        print(f"\n  --- Test 5: Spectral Duality (n={n}) ---")

        product_spreads = []
        sum_spreads = []
        product_constants = []
        sum_constants = []

        for r2 in results_2sat:
            for r3 in results_3sat:
                if r2["_sol_lap_eigs"] and r3["_sol_lap_eigs"]:
                    pc, ps = test_product_duality(
                        r2["_sol_lap_eigs"], r3["_sol_lap_eigs"])
                    if pc is not None:
                        product_constants.append(pc)
                        product_spreads.append(ps)

                    sc, ss = test_sum_duality(
                        r2["_sol_lap_eigs"], r3["_sol_lap_eigs"])
                    if sc is not None:
                        sum_constants.append(sc)
                        sum_spreads.append(ss)

        if product_spreads:
            print(f"    Product duality (lambda_i * mu_i = C):")
            print(f"      Mean constant: {np.mean(product_constants):.4f}")
            print(f"      Mean relative spread: {np.mean(product_spreads):.4f}")
            print(f"      Perfect duality if spread << 0.1: "
                  f"{'POSSIBLE' if np.mean(product_spreads) < 0.1 else 'NOT FOUND'}")

        if sum_spreads:
            print(f"    Sum duality (lambda_i + mu_i = C):")
            print(f"      Mean constant: {np.mean(sum_constants):.4f}")
            print(f"      Mean relative spread: {np.mean(sum_spreads):.4f}")
            print(f"      Perfect duality if spread << 0.1: "
                  f"{'POSSIBLE' if np.mean(sum_spreads) < 0.1 else 'NOT FOUND'}")

        # ─────────────────────────────────────────────────────────────
        #  ANALYSIS 5b: Cross-sector spectral duality
        #   (2-SAT solution Laplacian vs 3-SAT constraint Laplacian)
        # ─────────────────────────────────────────────────────────────
        print(f"\n  --- Test 5b: Cross-Sector Spectral Duality (n={n}) ---")

        cross_product_spreads = []
        cross_sum_spreads = []

        for r2 in results_2sat:
            for r3 in results_3sat:
                if r2["_sol_lap_eigs"] and r3["_con_lap_eigs"]:
                    pc, ps = test_product_duality(
                        r2["_sol_lap_eigs"], r3["_con_lap_eigs"])
                    if pc is not None:
                        cross_product_spreads.append(ps)

                    sc, ss = test_sum_duality(
                        r2["_sol_lap_eigs"], r3["_con_lap_eigs"])
                    if sc is not None:
                        cross_sum_spreads.append(ss)

        if cross_product_spreads:
            print(f"    Cross product duality spread: "
                  f"{np.mean(cross_product_spreads):.4f}")
        if cross_sum_spreads:
            print(f"    Cross sum duality spread: "
                  f"{np.mean(cross_sum_spreads):.4f}")

        # Store results
        all_results[f"n={n}"] = {
            "sat2_sol_counts": sat2_sol_counts,
            "sat3_sol_counts": sat3_sol_counts,
            "sat2_components": sat2_components,
            "sat3_components": sat3_components,
            "sat2_sol_gap": sat2_gap,
            "sat3_sol_gap": sat3_gap,
            "sat2_con_gap": sat2_con_gap,
            "sat3_con_gap": sat3_con_gap,
            "cross_spectral_dist": (
                float(np.mean(cross_distances_sol_con))
                if cross_distances_sol_con else None),
            "control_spectral_dist_sol": (
                float(np.mean(within_distances_sol))
                if within_distances_sol else None),
            "control_spectral_dist_con": (
                float(np.mean(within_distances_con))
                if within_distances_con else None),
            "j_ratio": (
                float(j_ratio)
                if cross_distances_sol_con and within_distances_sol else None),
            "complement_majority": float(np.mean(majority_closures)),
            "complement_affine": float(np.mean(affine_closures)),
            "product_duality_spread": (
                float(np.mean(product_spreads)) if product_spreads else None),
            "sum_duality_spread": (
                float(np.mean(sum_spreads)) if sum_spreads else None),
            "cross_product_spread": (
                float(np.mean(cross_product_spreads))
                if cross_product_spreads else None),
            "cross_sum_spread": (
                float(np.mean(cross_sum_spreads))
                if cross_sum_spreads else None),
        }

    # ─────────────────────────────────────────────────────────────
    #  OVERALL VERDICT
    # ─────────────────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("  OVERALL VERDICT")
    print(f"{'='*72}")

    verdicts = {}

    # Test 3: J-duality spectral
    j_verdicts = []
    for key in all_results:
        jr = all_results[key].get("j_ratio")
        if jr is not None:
            j_verdicts.append(jr < 0.5)
    spectral_j_pass = all(j_verdicts) if j_verdicts else False
    verdicts["T3_spectral_J_duality"] = spectral_j_pass
    print(f"\n  T3 (Spectral J-duality): "
          f"{'PASS' if spectral_j_pass else 'FAIL'}")
    for key in all_results:
        jr = all_results[key].get("j_ratio")
        print(f"    {key}: j_ratio = {jr}")
    if not spectral_j_pass:
        print("    -> Cross-spectral distance is NOT smaller than controls.")
        print("    -> No evidence that 2-SAT solution spectrum resembles "
              "3-SAT constraint spectrum.")

    # Test 4: Complement Taylor closure
    complement_verdicts = []
    for key in all_results:
        maj = all_results[key].get("complement_majority", 0)
        complement_verdicts.append(maj > 0.9)
    complement_pass = all(complement_verdicts) if complement_verdicts else False
    verdicts["T4_complement_taylor"] = complement_pass
    print(f"\n  T4 (Complement Taylor closure): "
          f"{'PASS' if complement_pass else 'FAIL'}")
    for key in all_results:
        maj = all_results[key].get("complement_majority")
        aff = all_results[key].get("complement_affine")
        print(f"    {key}: majority_closure = {maj:.4f}, "
              f"affine_closure = {aff:.4f}")
    if not complement_pass:
        print("    -> Anti-solution set of 3-SAT is NOT closed under "
              "majority operation.")
        print("    -> Anti-solution set does NOT have P-time CSP structure.")

    # Test 5: Spectral product/sum duality
    product_verdicts = []
    sum_verdicts = []
    for key in all_results:
        ps = all_results[key].get("product_duality_spread")
        ss = all_results[key].get("sum_duality_spread")
        if ps is not None:
            product_verdicts.append(ps < 0.1)
        if ss is not None:
            sum_verdicts.append(ss < 0.1)
    product_pass = all(product_verdicts) if product_verdicts else False
    sum_pass = all(sum_verdicts) if sum_verdicts else False
    verdicts["T5_product_duality"] = product_pass
    verdicts["T5_sum_duality"] = sum_pass
    print(f"\n  T5a (Product spectral duality): "
          f"{'PASS' if product_pass else 'FAIL'}")
    print(f"  T5b (Sum spectral duality): "
          f"{'PASS' if sum_pass else 'FAIL'}")
    for key in all_results:
        ps = all_results[key].get("product_duality_spread")
        ss = all_results[key].get("sum_duality_spread")
        print(f"    {key}: product_spread = {ps}, sum_spread = {ss}")

    # Cross-sector spectral duality
    cross_verdicts = []
    for key in all_results:
        cps = all_results[key].get("cross_product_spread")
        css = all_results[key].get("cross_sum_spread")
        if cps is not None:
            cross_verdicts.append(cps < 0.1 or (css is not None and css < 0.1))
    cross_pass = any(cross_verdicts) if cross_verdicts else False
    verdicts["T5c_cross_sector_duality"] = cross_pass
    print(f"\n  T5c (Cross-sector duality): "
          f"{'PASS' if cross_pass else 'FAIL'}")

    # Overall J-duality verdict
    any_duality = any(verdicts.values())
    print(f"\n  {'='*60}")
    print(f"  OVERALL A1 J-DUALITY: {'PASS (partial)' if any_duality else 'FAIL'}")
    print(f"  {'='*60}")

    if not any_duality:
        print("""
  INTERPRETATION:
    No evidence of a finite-dimensional J-like duality between the P-time
    sector (2-SAT) and the NPC sector (3-SAT) at n=8,10 with 30 instances.

    Specifically:
    - The solution-space spectrum of 2-SAT does NOT resemble the
      constraint-space spectrum of 3-SAT (spectral cross-comparison fails).
    - The anti-solution set of 3-SAT is NOT closed under Taylor operations
      (majority/affine), so it does not have P-time CSP structure.
    - There is no lambda_i * mu_i = C or lambda_i + mu_i = C relationship
      between paired 2-SAT and 3-SAT Laplacian spectra.

    This does NOT kill the A1 conjecture in general — the modular conjugation
    J operates on the type III_1 factor M_Bool, not on finite solution spaces.
    But it shows that any J-duality does NOT descend to a simple structural
    bijection at the finite level.

    RECOMMENDATION: The J-duality, if it exists, must be an ASYMPTOTIC
    or infinite-dimensional phenomenon. Test A4 (heat kernel / Seeley-DeWitt)
    or A6 (KMS phase transition) instead, as these probe infinite-dimensional
    structure more directly.
""")
    else:
        passing = [k for k, v in verdicts.items() if v]
        print(f"\n  Partial duality detected in: {', '.join(passing)}")
        print("  Further investigation warranted.")

    # Save numerical summary
    summary = {
        "test": "A1_J_duality",
        "instances_per_class": N_INSTANCES,
        "n_values": [8, 10],
        "verdicts": verdicts,
        "overall": "PASS (partial)" if any_duality else "FAIL",
        "data": {}
    }
    for key in all_results:
        d = all_results[key]
        summary["data"][key] = {
            "sat2_sol_count_mean": float(np.mean(d["sat2_sol_counts"])),
            "sat3_sol_count_mean": float(np.mean(d["sat3_sol_counts"])),
            "sat2_components_mean": float(np.mean(d["sat2_components"])),
            "sat3_components_mean": float(np.mean(d["sat3_components"])),
            "j_ratio": d["j_ratio"],
            "complement_majority": d["complement_majority"],
            "complement_affine": d["complement_affine"],
            "product_duality_spread": d["product_duality_spread"],
            "sum_duality_spread": d["sum_duality_spread"],
        }

    return summary, all_results, verdicts


if __name__ == "__main__":
    summary, all_results, verdicts = main()
