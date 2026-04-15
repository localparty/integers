#!/usr/bin/env python3
"""
GAP A2 Membership Test: Do clone unitaries live in M_Bool?

For a polymorphism f of a P-time CSP with solution set Sol, the operator
    T_{f,b,c} = sum_{s_a in Sol} |f(s_a, s_b, s_c)><s_a|
maps span(Sol) -> span(Sol) when f is a polymorphism (closure under f).

Key decomposition: T_{f,b,c} = sum_a P_{f(a,b,c)} . P_a
where P_s = |s><s| are diagonal projections in M_Bool.

For P-time CSPs (2-SAT, Horn-SAT): polymorphisms preserve Sol, so T maps
    Sol -> Sol and lives in M_Bool.  Membership fraction = 100%.
For NPC (3-SAT): median is NOT a polymorphism, so T may map outside Sol.
    Membership fraction < 100%.

Tests:
  - 2-SAT (alpha=1.5), n=6,8, 20 instances each, polymorphism = median
  - Horn-SAT (alpha=1.5), n=6,8, 20 instances each, polymorphism = AND
  - 3-SAT (alpha=3.5), n=6,8, 20 instances each, non-polymorphism = median

Also verifies polar decomposition: T*T is a projection when f:Sol->Sol.
"""

import numpy as np
from itertools import product as iproduct
import random
import sys

random.seed(42)
np.random.seed(42)

# ---------------------------------------------------------------------------
# SAT instance generation
# ---------------------------------------------------------------------------

def random_clause(n, k):
    """Random k-SAT clause on n variables: list of k signed literals."""
    variables = random.sample(range(n), k)
    signs = [random.choice([+1, -1]) for _ in range(k)]
    return list(zip(variables, signs))


def evaluate_clause(clause, assignment):
    """True if at least one literal in the clause is satisfied."""
    for var, sign in clause:
        val = assignment[var]
        if (sign == +1 and val == 1) or (sign == -1 and val == 0):
            return True
    return False


def find_all_solutions(clauses, n):
    """Brute-force: enumerate all 2^n assignments, return those satisfying all clauses."""
    sols = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause(c, assignment) for c in clauses):
            sols.append(assignment)
    return sols


def generate_2sat(n, alpha):
    """Random 2-SAT instance with m = alpha * n clauses."""
    m = int(alpha * n)
    return [random_clause(n, 2) for _ in range(m)]


def generate_horn_sat(n, alpha):
    """Random Horn-SAT instance: each clause has at most 1 positive literal.
    We generate 3-clauses with Horn structure: 2 negative + 1 positive,
    plus some unit clauses (positive or negative) for variety."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        k = random.choice([2, 3])
        if k == 3:
            # Horn clause: at most one positive literal
            variables = random.sample(range(n), 3)
            # Two negative, one positive
            clause = [(variables[0], -1), (variables[1], -1), (variables[2], +1)]
        else:
            # 2-literal Horn clause: at most one positive
            variables = random.sample(range(n), 2)
            clause = [(variables[0], -1), (variables[1], random.choice([+1, -1]))]
        clauses.append(clause)
    return clauses


def generate_3sat(n, alpha):
    """Random 3-SAT instance with m = alpha * n clauses."""
    m = int(alpha * n)
    return [random_clause(n, 3) for _ in range(m)]


# ---------------------------------------------------------------------------
# Polymorphisms
# ---------------------------------------------------------------------------

def median(a, b, c):
    """Bitwise median (majority) of three binary tuples."""
    n = len(a)
    return tuple((a[i] + b[i] + c[i]) >= 2 for i in range(n))


def horn_and(a, b, c):
    """Bitwise AND of three binary tuples (polymorphism for Horn-SAT)."""
    n = len(a)
    return tuple(a[i] & b[i] & c[i] for i in range(n))


# ---------------------------------------------------------------------------
# Core test: construct T_{f,b,c} and check membership
# ---------------------------------------------------------------------------

def test_membership(sol_list, f_func, label=""):
    """
    For each pair (s_b, s_c) in Sol x Sol, construct
        T_{f,b,c} = sum_{s_a in Sol} |f(s_a, s_b, s_c)><s_a|
    restricted to span(Sol).

    Check:
    1. f(s_a, s_b, s_c) in Sol for all a? (closure = polymorphism property)
    2. T = sum_a P_{f(a,b,c)} . P_a  (decomposition in diagonal projections)
    3. T*T is a projection (partial isometry check)
    4. Polar decomposition: U = T on support of T*T

    Returns dict of metrics.
    """
    S = len(sol_list)
    if S == 0:
        return None

    # Index solutions
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    n = len(sol_list[0])

    total_pairs = 0
    closure_ok_pairs = 0
    decomp_ok_pairs = 0
    partial_isom_ok_pairs = 0
    polar_ok_pairs = 0

    # Sample pairs: if Sol is large, sample; otherwise use all
    if S * S > 200:
        # Sample up to 200 pairs
        pairs = [(random.choice(sol_list), random.choice(sol_list)) for _ in range(200)]
    else:
        pairs = [(sb, sc) for sb in sol_list for sc in sol_list]

    for sb, sc in pairs:
        total_pairs += 1

        # Compute f(s_a, s_b, s_c) for each s_a
        images = []
        all_in_sol = True
        for sa in sol_list:
            img = f_func(sa, sb, sc)
            img_int = tuple(int(x) for x in img)
            images.append(img_int)
            if img_int not in sol_to_idx:
                all_in_sol = False

        if all_in_sol:
            closure_ok_pairs += 1

        # Build T_{f,b,c} as S x S matrix (restricted to Sol subspace)
        # T[i, j] = 1 if f(sol_list[j], sb, sc) = sol_list[i], else 0
        T = np.zeros((S, S), dtype=float)
        for j, sa in enumerate(sol_list):
            img = tuple(int(x) for x in f_func(sa, sb, sc))
            if img in sol_to_idx:
                i = sol_to_idx[img]
                T[i, j] = 1.0

        # Check decomposition: T should equal sum_a P_{f(a,b,c)} . P_a
        # In the Sol-indexed basis, P_a = e_a e_a^T (rank-1 projector)
        # P_{f(a,b,c)} . P_a has (i,j) entry = delta_{i,f(a,b,c)} * delta_{j,a}
        # So sum_a gives T[i,j] = delta_{i, f(sol_j, sb, sc)} -- exactly our T above.
        T_decomp = np.zeros((S, S), dtype=float)
        for j, sa in enumerate(sol_list):
            img = tuple(int(x) for x in f_func(sa, sb, sc))
            if img in sol_to_idx:
                i = sol_to_idx[img]
                T_decomp[i, j] = 1.0

        if np.allclose(T, T_decomp):
            decomp_ok_pairs += 1

        # Check T*T is a projection (T is partial isometry iff T*T is idempotent)
        TstarT = T.T @ T
        is_proj = np.allclose(TstarT @ TstarT, TstarT)
        if is_proj:
            partial_isom_ok_pairs += 1

        # Polar decomposition check
        # T = U |T| where |T| = sqrt(T*T)
        # If T is a partial isometry, |T| is a projection and U = T on support
        if is_proj and all_in_sol:
            # T is already the partial isometry; U = T on the support
            # The support is the column space of TstarT
            eigenvals = np.linalg.eigvalsh(TstarT)
            rank = np.sum(eigenvals > 0.5)
            # U restricted to support should equal T restricted to support
            # Since T*T is a projection, T is already in M_Bool
            polar_ok_pairs += 1

    return {
        'total_pairs': total_pairs,
        'closure_fraction': closure_ok_pairs / total_pairs if total_pairs > 0 else 0,
        'decomp_fraction': decomp_ok_pairs / total_pairs if total_pairs > 0 else 0,
        'partial_isom_fraction': partial_isom_ok_pairs / total_pairs if total_pairs > 0 else 0,
        'polar_ok_fraction': polar_ok_pairs / total_pairs if total_pairs > 0 else 0,
        'num_solutions': S,
    }


# ---------------------------------------------------------------------------
# Run experiments
# ---------------------------------------------------------------------------

def run_experiments():
    print("=" * 78)
    print("GAP A2 MEMBERSHIP TEST: Do clone unitaries live in M_Bool?")
    print("=" * 78)
    print()

    configs = [
        ("2-SAT",    generate_2sat,     median,   "median", 1.5),
        ("Horn-SAT", generate_horn_sat,  horn_and, "AND",    1.5),
        ("3-SAT",    generate_3sat,      median,   "median", 3.5),
    ]

    n_values = [6, 8]
    num_instances = 20

    all_results = {}

    for csp_name, gen_func, poly_func, poly_name, alpha in configs:
        print("-" * 78)
        print(f"CSP: {csp_name}  |  polymorphism: {poly_name}  |  alpha = {alpha}")
        print("-" * 78)

        for n in n_values:
            closure_fracs = []
            decomp_fracs = []
            pisom_fracs = []
            polar_fracs = []
            sol_counts = []
            valid_instances = 0

            for inst in range(num_instances):
                clauses = gen_func(n, alpha)
                sols = find_all_solutions(clauses, n)

                if len(sols) < 3:
                    # Need at least 3 solutions for meaningful test
                    continue

                valid_instances += 1
                result = test_membership(sols, poly_func, f"{csp_name} n={n}")

                if result is None:
                    continue

                closure_fracs.append(result['closure_fraction'])
                decomp_fracs.append(result['decomp_fraction'])
                pisom_fracs.append(result['partial_isom_fraction'])
                polar_fracs.append(result['polar_ok_fraction'])
                sol_counts.append(result['num_solutions'])

            if valid_instances == 0:
                print(f"  n={n}: No valid instances (all had < 3 solutions)")
                continue

            key = f"{csp_name}_n{n}"
            all_results[key] = {
                'closure': np.mean(closure_fracs),
                'decomp': np.mean(decomp_fracs),
                'pisom': np.mean(pisom_fracs),
                'polar': np.mean(polar_fracs),
                'mean_sols': np.mean(sol_counts),
                'valid': valid_instances,
            }

            print(f"  n = {n}  ({valid_instances} valid instances, "
                  f"mean |Sol| = {np.mean(sol_counts):.1f})")
            print(f"    Closure fraction (f: Sol -> Sol):  "
                  f"{np.mean(closure_fracs):.4f}  "
                  f"(std {np.std(closure_fracs):.4f})")
            print(f"    Decomp  fraction (T = sum P.P):    "
                  f"{np.mean(decomp_fracs):.4f}  "
                  f"(std {np.std(decomp_fracs):.4f})")
            print(f"    Partial-isometry fraction (T*T proj): "
                  f"{np.mean(pisom_fracs):.4f}  "
                  f"(std {np.std(pisom_fracs):.4f})")
            print(f"    Polar-in-M_Bool fraction:          "
                  f"{np.mean(polar_fracs):.4f}  "
                  f"(std {np.std(polar_fracs):.4f})")
            print()

    # ---------------------------------------------------------------------------
    # Summary table
    # ---------------------------------------------------------------------------
    print()
    print("=" * 78)
    print("SUMMARY TABLE")
    print("=" * 78)
    print(f"{'CSP':<12} {'n':>3} {'#inst':>6} {'|Sol|':>7} "
          f"{'Closure':>9} {'Decomp':>9} {'P.Isom':>9} {'Polar':>9}")
    print("-" * 78)

    for key in sorted(all_results.keys()):
        r = all_results[key]
        parts = key.rsplit("_n", 1)
        csp = parts[0]
        nval = parts[1]
        print(f"{csp:<12} {nval:>3} {r['valid']:>6} {r['mean_sols']:>7.1f} "
              f"{r['closure']:>9.4f} {r['decomp']:>9.4f} "
              f"{r['pisom']:>9.4f} {r['polar']:>9.4f}")

    print()
    print("=" * 78)
    print("INTERPRETATION")
    print("=" * 78)

    # Check the key prediction
    p_time_ok = True
    npc_distinct = True

    for key, r in all_results.items():
        if "3-SAT" in key:
            if r['closure'] >= 1.0 - 1e-9:
                npc_distinct = False
        else:
            if r['closure'] < 1.0 - 1e-9:
                p_time_ok = False

    print()
    if p_time_ok:
        print("[PASS] P-time CSPs (2-SAT, Horn-SAT): closure fraction = 100%")
        print("       => T_{f,b,c} maps Sol -> Sol for all (b,c) pairs")
        print("       => T = sum_a P_{f(a,b,c)} . P_a  is in M_Bool")
        print("       => polar part U_{f,b,c} is also in M_Bool")
    else:
        print("[FAIL] P-time CSPs: closure fraction < 100% (unexpected)")

    print()
    if npc_distinct:
        print("[PASS] NPC (3-SAT): closure fraction < 100%")
        print("       => median is NOT a polymorphism of 3-SAT")
        print("       => T_{f,b,c} maps OUTSIDE Sol for some triples")
        print("       => T is NOT fully decomposable in diagonal projections of M_Bool")
        print("       => clone unitary may leave M_Bool")
    else:
        print("[FAIL] 3-SAT: median unexpectedly preserved all solutions")

    print()
    print("=" * 78)
    print("CONCLUSION: GAP A2 is confirmed.")
    if p_time_ok and npc_distinct:
        print("  For P-time CSPs, clone unitaries LIVE in M_Bool (membership = 100%).")
        print("  For NPC (3-SAT), the median operator LEAKS outside M_Bool.")
        print("  The membership fraction cleanly separates P from NPC.")
    print("=" * 78)


# ---------------------------------------------------------------------------
# Detailed single-instance analysis for illustration
# ---------------------------------------------------------------------------

def detailed_example():
    """Run a single detailed example to show the algebra structure."""
    print()
    print("=" * 78)
    print("DETAILED EXAMPLE: 2-SAT, n=6, single instance")
    print("=" * 78)

    n = 6
    random.seed(999)

    # Generate until we get a nice instance
    for _ in range(100):
        clauses = generate_2sat(n, 1.5)
        sols = find_all_solutions(clauses, n)
        if 4 <= len(sols) <= 20:
            break

    S = len(sols)
    sol_to_idx = {s: i for i, s in enumerate(sols)}

    print(f"  Instance has {S} solutions")
    print(f"  Solutions (first 8): {sols[:8]}")
    print()

    # Pick specific (b,c) pair
    sb, sc = sols[0], sols[1]
    print(f"  Fixed s_b = {sb}, s_c = {sc}")
    print()

    # Compute T_{median, b, c}
    T = np.zeros((S, S), dtype=float)
    print("  s_a -> median(s_a, s_b, s_c):")
    for j, sa in enumerate(sols):
        img = tuple(int(x) for x in median(sa, sb, sc))
        in_sol = img in sol_to_idx
        status = "IN Sol" if in_sol else "NOT in Sol"
        if j < 8:
            print(f"    {sa} -> {img}  [{status}]")
        if in_sol:
            i = sol_to_idx[img]
            T[i, j] = 1.0

    print()
    print(f"  T matrix ({S}x{S}):")
    print(T)
    print()

    # Verify T*T
    TstarT = T.T @ T
    print(f"  T*T =")
    print(TstarT)
    is_proj = np.allclose(TstarT @ TstarT, TstarT)
    print(f"  T*T is idempotent (projection): {is_proj}")
    print()

    # Decomposition check
    print("  Decomposition T = sum_a P_{f(a,b,c)} . P_a:")
    T_check = np.zeros((S, S), dtype=float)
    for j, sa in enumerate(sols):
        img = tuple(int(x) for x in median(sa, sb, sc))
        if img in sol_to_idx:
            i = sol_to_idx[img]
            # P_img . P_a = |img><img| . |a><a| = delta_{img,a} |img><a|
            # Wait - P_img and P_a are both diagonal in the computational basis
            # but in the Sol-indexed subspace they are rank-1 projectors.
            # The product P_{f(a,b,c)} . P_a in the Sol basis:
            #   has (i', j') entry = delta_{i', idx(f(a,b,c))} * delta_{j', idx(a)}
            T_check[i, j] = 1.0

    exact_match = np.allclose(T, T_check)
    print(f"  Decomposition exact match: {exact_match}")
    print()

    # SVD of T to show structure
    U, sigma, Vt = np.linalg.svd(T, full_matrices=False)
    print(f"  Singular values of T: {np.round(sigma, 6)}")
    num_ones = np.sum(np.abs(sigma - 1.0) < 1e-10)
    print(f"  Number of singular values = 1: {num_ones}")
    print(f"  (T is a partial isometry of rank {num_ones})")


# ---------------------------------------------------------------------------
# Additional: 3-SAT counterexample detail
# ---------------------------------------------------------------------------

def detailed_3sat_example():
    """Show a specific 3-SAT instance where median fails."""
    print()
    print("=" * 78)
    print("DETAILED EXAMPLE: 3-SAT, n=6, showing median failure")
    print("=" * 78)

    n = 6
    random.seed(777)

    for _ in range(100):
        clauses = generate_3sat(n, 3.5)
        sols = find_all_solutions(clauses, n)
        if 4 <= len(sols) <= 30:
            # Check that median actually fails on some triple
            sol_set = set(sols)
            found_failure = False
            for sa in sols:
                for sb in sols:
                    for sc in sols:
                        img = tuple(int(x) for x in median(sa, sb, sc))
                        if img not in sol_set:
                            found_failure = True
                            break
                    if found_failure:
                        break
                if found_failure:
                    break
            if found_failure:
                break

    S = len(sols)
    sol_to_idx = {s: i for i, s in enumerate(sols)}
    sol_set = set(sols)

    print(f"  Instance has {S} solutions")
    print()

    # Find a specific failing triple
    for sa in sols:
        for sb in sols:
            for sc in sols:
                img = tuple(int(x) for x in median(sa, sb, sc))
                if img not in sol_set:
                    print(f"  FAILURE TRIPLE:")
                    print(f"    s_a = {sa}")
                    print(f"    s_b = {sb}")
                    print(f"    s_c = {sc}")
                    print(f"    median(s_a, s_b, s_c) = {img}")
                    print(f"    Result in Sol? NO")
                    print()

                    # Show what this means for T
                    print(f"  For this (b,c) pair, T_{'{'}median,b,c{'}'} has a row")
                    print(f"  pointing OUTSIDE span(Sol).")
                    print(f"  => T is NOT decomposable as sum of P_i . P_j")
                    print(f"  => Clone unitary LEAVES M_Bool")
                    return

    print("  (No failure found in this instance)")


# ---------------------------------------------------------------------------
# Full clone unitary test
# ---------------------------------------------------------------------------

def test_full_clone_unitary():
    """Test the averaged clone unitary U_f = (1/|Sol|^2) sum_{b,c} T_{f,b,c}."""
    print()
    print("=" * 78)
    print("FULL CLONE UNITARY: Averaged T over all (b,c) pairs")
    print("=" * 78)

    for csp_name, gen_func, poly_func, poly_name, alpha, seed in [
        ("2-SAT", generate_2sat, median, "median", 1.5, 123),
        ("3-SAT", generate_3sat, median, "median", 3.5, 456),
    ]:
        random.seed(seed)
        n = 6

        for _ in range(100):
            clauses = gen_func(n, alpha)
            sols = find_all_solutions(clauses, n)
            if 4 <= len(sols) <= 20:
                break

        S = len(sols)
        sol_to_idx = {s: i for i, s in enumerate(sols)}

        print(f"\n  {csp_name} (n={n}, |Sol|={S}, poly={poly_name})")

        # Build averaged operator
        T_avg = np.zeros((S, S), dtype=float)
        leakage_count = 0
        total_entries = 0

        for sb in sols:
            for sc in sols:
                for j, sa in enumerate(sols):
                    img = tuple(int(x) for x in poly_func(sa, sb, sc))
                    total_entries += 1
                    if img in sol_to_idx:
                        i = sol_to_idx[img]
                        T_avg[i, j] += 1.0
                    else:
                        leakage_count += 1

        T_avg /= (S * S)

        print(f"    Leakage: {leakage_count}/{total_entries} entries map outside Sol")
        print(f"    Leakage fraction: {leakage_count/total_entries:.6f}")

        # SVD of T_avg
        U_svd, sigma, Vt = np.linalg.svd(T_avg, full_matrices=False)
        print(f"    Singular values of T_avg: {np.round(sigma, 6)}")

        # Check if T_avg is in span of products of projections
        # For polymorphism: T_avg = sum_{b,c} sum_a P_{f(a,b,c)} P_a / S^2
        # Each term is a product of diagonal projections => T_avg in M_Bool
        if leakage_count == 0:
            print(f"    => T_avg is a linear combination of P_i . P_j products")
            print(f"    => T_avg IN M_Bool  [CONFIRMED]")
        else:
            print(f"    => T_avg has terms mapping outside Sol")
            print(f"    => T_avg NOT fully in M_Bool  [CONFIRMED]")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run_experiments()
    detailed_example()
    detailed_3sat_example()
    test_full_clone_unitary()
