#!/usr/bin/env python3
"""
pvnp_spectral_geometric_bridge.py
==================================
Spectral-Geometric Bridge for P vs NP

Tests whether the spectral measure (Taylor gap / TGap) and the geometric
measure (holonomy defect on the constraint graph) are correlated across
CSP instances — analogous to the spectral-geometric duality in Riemann
(zeros <-> primes via the explicit formula).

For each CSP class we generate random instances and compute:
  1. TGap  (spectral side)  — minimum violation rate of best Taylor operation
  2. Holonomy defect (geometric side) — fraction of short cycles where the
     best polymorphism fails to return to starting solution
  3. Pearson correlation between TGap and holonomy defect
  4. Best-fit relationship: linear, quadratic, logarithmic

CSP classes tested (n=10 variables, 40 instances each):
  - 2-SAT        (alpha = 1.5)
  - Horn-SAT     (alpha = 2.0)
  - 3-SAT        (alpha = 3.5)
  - NAE-3-SAT    (alpha = 1.0)
"""

import random
import itertools
import math
import numpy as np
from collections import defaultdict
from scipy import stats
from scipy.optimize import curve_fit

random.seed(42)
np.random.seed(42)

# ─── CSP instance generation ───────────────────────────────────────────────

def generate_2sat(n, num_clauses):
    """Generate a random 2-SAT instance: each clause has exactly 2 literals."""
    clauses = []
    for _ in range(num_clauses):
        vs = random.sample(range(n), 2)
        signs = [random.choice([True, False]) for _ in range(2)]
        clauses.append(list(zip(vs, signs)))
    return clauses

def generate_horn_sat(n, num_clauses):
    """Generate a random Horn-SAT instance: at most one positive literal per clause."""
    clauses = []
    for _ in range(num_clauses):
        k = random.choice([2, 3])
        vs = random.sample(range(n), k)
        # Make all negative except possibly the first
        signs = [False] * k
        if random.random() < 0.5:
            signs[0] = True  # at most one positive
        clause = list(zip(vs, signs))
        clauses.append(clause)
    return clauses

def generate_3sat(n, num_clauses):
    """Generate a random 3-SAT instance."""
    clauses = []
    for _ in range(num_clauses):
        vs = random.sample(range(n), 3)
        signs = [random.choice([True, False]) for _ in range(3)]
        clauses.append(list(zip(vs, signs)))
    return clauses

def generate_nae_3sat(n, num_clauses):
    """Generate a random NAE-3-SAT instance (stored as 3-SAT; NAE check done separately)."""
    return generate_3sat(n, num_clauses)

# ─── Solution finding (brute force for n=10) ──────────────────────────────

def clause_satisfied(clause, assignment):
    """Check if a standard SAT clause is satisfied."""
    for var, positive in clause:
        lit_val = assignment[var] if positive else (not assignment[var])
        if lit_val:
            return True
    return False

def nae_clause_satisfied(clause, assignment):
    """NAE: clause satisfied if literals are NOT all equal."""
    vals = []
    for var, positive in clause:
        vals.append(assignment[var] if positive else (not assignment[var]))
    return not (all(vals) or not any(vals))

def find_solutions(n, clauses, is_nae=False):
    """Brute-force find all satisfying assignments for n variables."""
    solutions = []
    check = nae_clause_satisfied if is_nae else clause_satisfied
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 == 1 for i in range(n))
        if all(check(c, assignment) for c in clauses):
            solutions.append(assignment)
    return solutions

# ─── Taylor operations (polymorphisms) ────────────────────────────────────

def op_median(a, b, c):
    return sorted([a, b, c])[1]

def op_xor(a, b, c):
    return a ^ b ^ c

def op_and(a, b, c):
    return a & b & c

def op_or(a, b, c):
    return a | b | c

def op_min(a, b, c):
    return min(a, b, c)

def op_max(a, b, c):
    return max(a, b, c)

OPERATIONS = {
    'median': op_median,
    'XOR': op_xor,
    'AND': op_and,
    'OR': op_or,
    'min': op_min,
    'max': op_max,
}

# ─── TGap computation (spectral side) ────────────────────────────────────

def compute_tgap(clauses, solutions, is_nae=False):
    """
    TGap = minimum violation rate of the best Taylor operation on solution triples.
    For each operation, apply it component-wise to all triples of solutions,
    and check what fraction of clauses the result violates.
    TGap = min over operations of (average violation rate over triples).
    """
    if len(solutions) < 3:
        # Not enough solutions — TGap is maximal (1.0)
        if len(solutions) == 0:
            return 1.0
        # With 1-2 solutions, use pairs/singletons with repetition
        pass

    check = nae_clause_satisfied if is_nae else clause_satisfied
    n_clauses = len(clauses)

    best_violation = 1.0

    for op_name, op in OPERATIONS.items():
        total_violations = 0
        total_tests = 0

        # Sample triples of solutions (with replacement if fewer than 3)
        sol_list = solutions if len(solutions) >= 3 else solutions * 3
        # Use up to 200 random triples for efficiency
        max_triples = min(200, len(sol_list)**3)
        n_triples = min(max_triples, 200)

        for _ in range(n_triples):
            s1 = random.choice(sol_list)
            s2 = random.choice(sol_list)
            s3 = random.choice(sol_list)

            # Apply operation component-wise
            result = tuple(op(int(s1[i]), int(s2[i]), int(s3[i])) != 0 for i in range(len(s1)))

            # Count violated clauses
            violated = sum(1 for c in clauses if not check(c, result))
            total_violations += violated
            total_tests += n_clauses

        if total_tests > 0:
            avg_violation = total_violations / total_tests
            best_violation = min(best_violation, avg_violation)

    return best_violation

# ─── Constraint graph and holonomy defect (geometric side) ────────────────

def build_constraint_graph(n, clauses):
    """
    Build constraint graph: variables = vertices, edge between two variables
    if they appear together in at least one clause.
    Edge weight = number of shared clauses.
    """
    adj = defaultdict(set)
    edge_clauses = defaultdict(list)

    for ci, clause in enumerate(clauses):
        vars_in_clause = [v for v, _ in clause]
        for i in range(len(vars_in_clause)):
            for j in range(i+1, len(vars_in_clause)):
                u, v = vars_in_clause[i], vars_in_clause[j]
                adj[u].add(v)
                adj[v].add(u)
                edge_clauses[(min(u,v), max(u,v))].append(ci)

    return adj, edge_clauses

def find_short_cycles(adj, n, max_length=6):
    """Find cycles of length <= max_length in the constraint graph using BFS."""
    cycles = set()
    nodes = list(adj.keys())

    for start in nodes:
        # BFS from start, tracking paths
        # Use DFS with depth limit for efficiency
        stack = [(start, [start], {start})]
        while stack:
            node, path, visited = stack.pop()
            if len(path) > max_length:
                continue
            for neighbor in adj[node]:
                if neighbor == start and len(path) >= 3:
                    # Found a cycle
                    cycle = tuple(sorted(path))  # canonical form
                    if cycle not in cycles:
                        cycles.add(cycle)
                elif neighbor not in visited and len(path) < max_length:
                    stack.append((neighbor, path + [neighbor], visited | {neighbor}))

    # Convert back to actual cycles (ordered)
    # For holonomy we need ordered cycles, so re-extract them
    ordered_cycles = []
    for start in nodes:
        stack = [(start, [start], {start})]
        while stack:
            node, path, visited = stack.pop()
            if len(path) > max_length:
                continue
            for neighbor in adj[node]:
                if neighbor == start and len(path) >= 3:
                    ordered_cycles.append(list(path))
                elif neighbor not in visited and len(path) < max_length:
                    stack.append((neighbor, path + [neighbor], visited | {neighbor}))

    # Deduplicate (same cycle can be found multiple times)
    seen = set()
    unique_cycles = []
    for c in ordered_cycles:
        key = tuple(sorted(c))
        if key not in seen:
            seen.add(key)
            unique_cycles.append(c)
        if len(unique_cycles) >= 500:  # cap for performance
            break

    return unique_cycles

def compute_holonomy_defect(clauses, solutions, adj, n, is_nae=False):
    """
    Holonomy defect: for each short cycle in the constraint graph,
    apply the best polymorphism along the cycle and check if the result
    returns to the starting solution.

    For each cycle [v0, v1, ..., vk, v0]:
      - Pick a starting solution s
      - At each edge (vi, vi+1), the polymorphism "transports" the assignment
        by applying the best operation to solutions that agree on the shared variables
      - If the final result != starting solution on the cycle variables, it's a defect

    Holonomy defect = fraction of (cycle, solution, operation) tests that show defect.
    """
    if len(solutions) < 3 or not adj:
        return 1.0 if len(solutions) == 0 else 0.5

    cycles = find_short_cycles(adj, n, max_length=6)
    if not cycles:
        return 0.0

    check = nae_clause_satisfied if is_nae else clause_satisfied

    total_tests = 0
    total_defects = 0

    # For each cycle, test holonomy
    for cycle in cycles:
        cycle_vars = set(cycle)

        for op_name, op in OPERATIONS.items():
            # Sample a few starting solutions
            n_samples = min(10, len(solutions))
            sampled_sols = random.sample(solutions, n_samples) if len(solutions) >= n_samples else solutions

            for start_sol in sampled_sols:
                # "Transport" around the cycle
                current = list(start_sol)

                for step in range(len(cycle)):
                    v_from = cycle[step]
                    v_to = cycle[(step + 1) % len(cycle)]

                    # Find solutions that agree with current on v_from
                    matching = [s for s in solutions if s[v_from] == current[v_from]]
                    if len(matching) < 2:
                        matching = list(solutions[:3]) if len(solutions) >= 3 else solutions * 2

                    # Pick two other solutions from matching
                    s2 = random.choice(matching)
                    s3 = random.choice(matching)

                    # Apply operation at the target variable
                    new_val = op(int(current[v_to]), int(s2[v_to]), int(s3[v_to])) != 0
                    current[v_to] = new_val

                # Check if we returned to start on cycle variables
                defect = any(current[v] != start_sol[v] for v in cycle_vars)
                total_defects += int(defect)
                total_tests += 1

    if total_tests == 0:
        return 0.0

    return total_defects / total_tests

# ─── Main experiment ──────────────────────────────────────────────────────

def run_experiment(csp_name, generator, n, alpha, num_instances, is_nae=False):
    """Run the spectral-geometric bridge experiment for one CSP class."""
    if csp_name == "2-SAT":
        clause_width = 2
    else:
        clause_width = 3
    num_clauses = int(alpha * n)

    tgaps = []
    holon_defects = []
    n_satisfiable = 0

    for i in range(num_instances):
        clauses = generator(n, num_clauses)
        solutions = find_solutions(n, clauses, is_nae=is_nae)

        if len(solutions) == 0:
            # Unsatisfiable — assign maximal values
            tgaps.append(1.0)
            holon_defects.append(1.0)
            continue

        n_satisfiable += 1

        # Spectral side: TGap
        tgap = compute_tgap(clauses, solutions, is_nae=is_nae)

        # Geometric side: holonomy defect
        adj, edge_clauses = build_constraint_graph(n, clauses)
        hdef = compute_holonomy_defect(clauses, solutions, adj, n, is_nae=is_nae)

        tgaps.append(tgap)
        holon_defects.append(hdef)

    return tgaps, holon_defects, n_satisfiable

def fit_models(x, y):
    """Fit linear, quadratic, and logarithmic models."""
    x = np.array(x)
    y = np.array(y)

    # Remove any NaN/inf
    mask = np.isfinite(x) & np.isfinite(y)
    x, y = x[mask], y[mask]

    if len(x) < 3:
        return {}

    results = {}

    # Linear: y = a*x + b
    try:
        slope, intercept, r, p, se = stats.linregress(x, y)
        results['linear'] = {'a': slope, 'b': intercept, 'R2': r**2, 'formula': f'TGap = {slope:.4f} * H + {intercept:.4f}'}
    except:
        pass

    # Quadratic: y = a*x^2 + b
    try:
        def quad(x, a, b):
            return a * x**2 + b
        popt, _ = curve_fit(quad, x, y, p0=[1, 0], maxfev=5000)
        y_pred = quad(x, *popt)
        ss_res = np.sum((y - y_pred)**2)
        ss_tot = np.sum((y - np.mean(y))**2)
        r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0
        results['quadratic'] = {'a': popt[0], 'b': popt[1], 'R2': r2, 'formula': f'TGap = {popt[0]:.4f} * H^2 + {popt[1]:.4f}'}
    except:
        pass

    # Logarithmic: y = a*log(1 + x) + b
    try:
        def logf(x, a, b):
            return a * np.log(1 + x) + b
        popt, _ = curve_fit(logf, x, y, p0=[1, 0], maxfev=5000)
        y_pred = logf(x, *popt)
        ss_res = np.sum((y - y_pred)**2)
        ss_tot = np.sum((y - np.mean(y))**2)
        r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0
        results['logarithmic'] = {'a': popt[0], 'b': popt[1], 'R2': r2, 'formula': f'TGap = {popt[0]:.4f} * log(1+H) + {popt[1]:.4f}'}
    except:
        pass

    return results

# ─── Execute ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    N = 10
    NUM_INSTANCES = 40

    experiments = [
        ("2-SAT",      generate_2sat,     1.5, False),
        ("Horn-SAT",   generate_horn_sat,  2.0, False),
        ("3-SAT",      generate_3sat,      3.5, False),
        ("NAE-3-SAT",  generate_nae_3sat,  1.0, True),
    ]

    print("=" * 78)
    print("SPECTRAL-GEOMETRIC BRIDGE FOR P vs NP")
    print("Testing correlation between TGap (spectral) and Holonomy Defect (geometric)")
    print(f"n = {N} variables, {NUM_INSTANCES} instances per class")
    print("=" * 78)

    all_results = {}

    for csp_name, gen, alpha, is_nae in experiments:
        print(f"\n{'─' * 78}")
        print(f"CSP class: {csp_name}  (alpha = {alpha}, clauses = {int(alpha * N)})")
        print(f"{'─' * 78}")

        tgaps, hdefs, n_sat = run_experiment(csp_name, gen, N, alpha, NUM_INSTANCES, is_nae=is_nae)

        tgaps_arr = np.array(tgaps)
        hdefs_arr = np.array(hdefs)

        print(f"  Satisfiable instances: {n_sat}/{NUM_INSTANCES}")
        print(f"  TGap   — mean: {np.mean(tgaps_arr):.6f}  std: {np.std(tgaps_arr):.6f}  "
              f"min: {np.min(tgaps_arr):.6f}  max: {np.max(tgaps_arr):.6f}")
        print(f"  HolDef — mean: {np.mean(hdefs_arr):.6f}  std: {np.std(hdefs_arr):.6f}  "
              f"min: {np.min(hdefs_arr):.6f}  max: {np.max(hdefs_arr):.6f}")

        # Pearson correlation
        if np.std(tgaps_arr) > 1e-12 and np.std(hdefs_arr) > 1e-12:
            r, p_val = stats.pearsonr(tgaps_arr, hdefs_arr)
            print(f"\n  Pearson correlation:  r = {r:.6f},  p-value = {p_val:.2e}")

            # Spearman rank correlation (more robust)
            rho, sp_pval = stats.spearmanr(tgaps_arr, hdefs_arr)
            print(f"  Spearman correlation: rho = {rho:.6f},  p-value = {sp_pval:.2e}")
        else:
            r = float('nan')
            print(f"\n  Correlation: UNDEFINED (zero variance in one or both measures)")
            if np.std(tgaps_arr) < 1e-12:
                print(f"    -> TGap is constant at {tgaps_arr[0]:.6f} (polymorphism preserves all solutions)")
            if np.std(hdefs_arr) < 1e-12:
                print(f"    -> HolDef is constant at {hdefs_arr[0]:.6f}")

        # Fit models
        print(f"\n  Explicit formula analog — fitting TGap = f(HolDef):")
        fits = fit_models(hdefs_arr, tgaps_arr)
        best_r2 = -1
        best_model = None
        for model_name, info in fits.items():
            tag = " <-- best" if info['R2'] > best_r2 else ""
            if info['R2'] > best_r2:
                best_r2 = info['R2']
                best_model = model_name
            print(f"    {model_name:12s}:  {info['formula']:45s}  R^2 = {info['R2']:.6f}{tag}")

        if best_model:
            print(f"  Best fit: {best_model} (R^2 = {best_r2:.6f})")

        all_results[csp_name] = {
            'tgaps': tgaps_arr,
            'hdefs': hdefs_arr,
            'correlation': r if (isinstance(r, float) and np.isfinite(r)) else float('nan'),
            'best_fit': best_model,
            'best_r2': best_r2,
            'n_sat': n_sat,
        }

    # ─── Cross-class summary ──────────────────────────────────────────────

    print(f"\n{'=' * 78}")
    print("CROSS-CLASS SUMMARY: Spectral-Geometric Bridge")
    print(f"{'=' * 78}")
    print(f"{'CSP':<12s} {'TGap mean':>10s} {'HolDef mean':>12s} {'Pearson r':>10s} {'Best fit':>12s} {'R^2':>8s} {'Class':>6s}")
    print("-" * 78)

    for csp_name in ["2-SAT", "Horn-SAT", "3-SAT", "NAE-3-SAT"]:
        res = all_results[csp_name]
        complexity = "P" if csp_name in ["2-SAT", "Horn-SAT"] else "NPC"
        corr_str = f"{res['correlation']:.4f}" if np.isfinite(res['correlation']) else "N/A"
        r2_str = f"{res['best_r2']:.4f}" if res['best_r2'] >= 0 else "N/A"
        bf_str = res['best_fit'] if res['best_fit'] else "N/A"
        print(f"{csp_name:<12s} {np.mean(res['tgaps']):>10.6f} {np.mean(res['hdefs']):>12.6f} "
              f"{corr_str:>10s} {bf_str:>12s} {r2_str:>8s} {complexity:>6s}")

    # ─── Key diagnostic ───────────────────────────────────────────────────

    print(f"\n{'=' * 78}")
    print("KEY DIAGNOSTIC: Does the bridge separate P from NPC?")
    print(f"{'=' * 78}")

    p_tgaps = np.concatenate([all_results["2-SAT"]['tgaps'], all_results["Horn-SAT"]['tgaps']])
    p_hdefs = np.concatenate([all_results["2-SAT"]['hdefs'], all_results["Horn-SAT"]['hdefs']])
    npc_tgaps = np.concatenate([all_results["3-SAT"]['tgaps'], all_results["NAE-3-SAT"]['tgaps']])
    npc_hdefs = np.concatenate([all_results["3-SAT"]['hdefs'], all_results["NAE-3-SAT"]['hdefs']])

    print(f"\n  P-class   (2-SAT + Horn-SAT):  TGap = {np.mean(p_tgaps):.6f} +/- {np.std(p_tgaps):.6f},  "
          f"HolDef = {np.mean(p_hdefs):.6f} +/- {np.std(p_hdefs):.6f}")
    print(f"  NPC-class (3-SAT + NAE-3-SAT): TGap = {np.mean(npc_tgaps):.6f} +/- {np.std(npc_tgaps):.6f},  "
          f"HolDef = {np.mean(npc_hdefs):.6f} +/- {np.std(npc_hdefs):.6f}")

    # Welch t-test for separation
    t_tgap, p_tgap = stats.ttest_ind(p_tgaps, npc_tgaps, equal_var=False)
    t_hdef, p_hdef = stats.ttest_ind(p_hdefs, npc_hdefs, equal_var=False)
    print(f"\n  Welch t-test (P vs NPC):")
    print(f"    TGap:    t = {t_tgap:+.4f},  p = {p_tgap:.2e}  {'*** SIGNIFICANT ***' if p_tgap < 0.01 else ''}")
    print(f"    HolDef:  t = {t_hdef:+.4f},  p = {p_hdef:.2e}  {'*** SIGNIFICANT ***' if p_hdef < 0.01 else ''}")

    # Combined discriminant
    print(f"\n  Combined spectral-geometric discriminant:")
    p_combined = p_tgaps + p_hdefs  # simple sum
    npc_combined = npc_tgaps + npc_hdefs
    t_comb, p_comb = stats.ttest_ind(p_combined, npc_combined, equal_var=False)
    print(f"    TGap + HolDef:  P = {np.mean(p_combined):.6f},  NPC = {np.mean(npc_combined):.6f}")
    print(f"    t = {t_comb:+.4f},  p = {p_comb:.2e}  {'*** SIGNIFICANT ***' if p_comb < 0.01 else ''}")

    # ─── Pool all instances: overall correlation ──────────────────────────

    print(f"\n{'=' * 78}")
    print("POOLED CORRELATION (all 160 instances)")
    print(f"{'=' * 78}")

    all_tgaps = np.concatenate([all_results[k]['tgaps'] for k in all_results])
    all_hdefs = np.concatenate([all_results[k]['hdefs'] for k in all_results])

    if np.std(all_tgaps) > 1e-12 and np.std(all_hdefs) > 1e-12:
        r_all, p_all = stats.pearsonr(all_tgaps, all_hdefs)
        rho_all, sp_all = stats.spearmanr(all_tgaps, all_hdefs)
        print(f"  Pearson  r   = {r_all:.6f}  (p = {p_all:.2e})")
        print(f"  Spearman rho = {rho_all:.6f}  (p = {sp_all:.2e})")

        fits_all = fit_models(all_hdefs, all_tgaps)
        print(f"\n  Explicit formula fits (pooled):")
        for model_name, info in fits_all.items():
            print(f"    {model_name:12s}:  {info['formula']:45s}  R^2 = {info['R2']:.6f}")
    else:
        print("  Cannot compute — zero variance in one measure.")

    print(f"\n{'=' * 78}")
    print("INTERPRETATION")
    print(f"{'=' * 78}")
    print("""
  The spectral-geometric bridge posits that TGap (measuring polymorphism
  violation = spectral obstruction) and holonomy defect (measuring failure
  of parallel transport around constraint cycles = geometric obstruction)
  are dual descriptions of the same underlying complexity.

  High correlation (r ~ 1) means: the spectral and geometric measures
  are indeed two faces of the same coin, analogous to how Riemann zeros
  and prime distribution are linked by the explicit formula.

  Significant P-vs-NPC separation in BOTH measures confirms that the
  bridge is not just a mathematical curiosity but captures genuine
  computational complexity.
""")
