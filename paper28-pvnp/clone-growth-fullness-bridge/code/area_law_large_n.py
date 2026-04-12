"""
Area Law String Tension at Larger System Sizes -- Node 2.4 (Sub-gap E-1)

Closes E-1: does the string tension sigma(L, n) converge to a positive
limit as n -> infinity?

Strategy:
  - For n = 14, 16: full enumeration of Sol (feasible: 2^16 = 65536)
  - For n = 18, 20: SAT-solver-guided Monte Carlo sampling of Sol
  - Compute holonomy defect H(L) for constraint-graph cycles L = 3..8
  - Fit H vs cycle area to extract sigma(n)
  - Fit sigma(n) = sigma_inf + c / n^beta to test convergence

Controls:
  - 2-SAT: should have sigma = 0 at all n (flat connection)
  - Horn-SAT: should have sigma = 0 at all n (flat connection)

Author: Claude Opus 4.6 (1M context), Node 2.4 E-1
Date: 2026-04-11
"""

import numpy as np
from itertools import combinations
from collections import defaultdict
import random
import json
import sys
import time
from scipy.optimize import curve_fit
from scipy.stats import linregress

try:
    from pysat.solvers import Minisat22, Glucose4
    from pysat.formula import CNF
    PYSAT_AVAILABLE = True
except ImportError:
    PYSAT_AVAILABLE = False
    print("WARNING: pysat not available. n >= 18 will use heuristic sampling.")

random.seed(42)
np.random.seed(42)
np.set_printoptions(precision=8, suppress=True, linewidth=130)

# ============================================================
# 0. Constants and configuration
# ============================================================

# Number of random instances per (type, n)
NUM_INSTANCES = 10
# Cycle lengths to probe
CYCLE_LENGTHS = [3, 4, 5, 6, 7, 8]
# Monte Carlo samples for holonomy at large n
MC_SAMPLES_SOL = 2000          # solution samples for MC
MC_SAMPLES_TRIPLES = 5000      # (a, b, c) triples per cycle
# Number of WalkSAT restarts for solution sampling
WALKSAT_RESTARTS = 200
# Clause ratios
ALPHA_3SAT = 4.0               # near threshold for 3-SAT
ALPHA_2SAT = 1.0               # underconstrained for 2-SAT
ALPHA_HORN = 2.0               # for Horn-SAT
# Instance sizes
N_VALUES = [14, 16, 18, 20]
# Threshold for full enumeration vs sampling
ENUM_THRESHOLD = 17            # enumerate for n <= 16

# ============================================================
# 1. Clause evaluation
# ============================================================

def eval_clause_ksat(assignment, clause):
    """Evaluate a k-SAT clause. clause = [(var, sign), ...].
    sign=1 means positive literal, sign=0 means negated."""
    return any(
        (assignment[v] if s == 1 else 1 - assignment[v])
        for v, s in clause
    )

def eval_all_clauses(assignment, clauses):
    """Check if assignment satisfies all clauses."""
    return all(eval_clause_ksat(assignment, c) for c in clauses)


# ============================================================
# 2. Instance generation
# ============================================================

def generate_3sat_instance(n, alpha=ALPHA_3SAT, min_solutions=4, max_attempts=1000):
    """Random 3-SAT at clause-to-variable ratio alpha.
    Returns (clauses, solutions_or_None).
    For n <= ENUM_THRESHOLD, enumerates all solutions.
    For n > ENUM_THRESHOLD, returns clauses only (solutions found later by sampling).
    """
    m = int(n * alpha)
    for attempt in range(max_attempts):
        clauses = []
        for _ in range(m):
            vs = random.sample(range(n), 3)
            signs = [random.choice([0, 1]) for _ in range(3)]
            clauses.append(list(zip(vs, signs)))

        if n <= ENUM_THRESHOLD:
            sols = enumerate_solutions(n, clauses)
            if len(sols) >= min_solutions:
                return clauses, sols
        else:
            # For large n, check satisfiability with SAT solver
            if PYSAT_AVAILABLE:
                sat, _ = check_sat_pysat(n, clauses)
                if sat:
                    return clauses, None
            else:
                # Try random assignments
                found = False
                for _ in range(1000):
                    a = tuple(random.randint(0, 1) for _ in range(n))
                    if eval_all_clauses(a, clauses):
                        found = True
                        break
                if found:
                    return clauses, None
    return None, None


def generate_2sat_instance(n, alpha=ALPHA_2SAT, min_solutions=8, max_attempts=1000):
    """Random 2-SAT instance."""
    m = int(n * alpha)
    for attempt in range(max_attempts):
        clauses = []
        for _ in range(m):
            vs = random.sample(range(n), 2)
            signs = [random.choice([0, 1]) for _ in range(2)]
            clauses.append(list(zip(vs, signs)))

        if n <= ENUM_THRESHOLD:
            sols = enumerate_solutions(n, clauses)
            if len(sols) >= min_solutions:
                return clauses, sols
        else:
            if PYSAT_AVAILABLE:
                sat, _ = check_sat_pysat(n, clauses)
                if sat:
                    return clauses, None
            else:
                return clauses, None
    return None, None


def generate_horn_instance(n, alpha=ALPHA_HORN, min_solutions=8, max_attempts=1000):
    """Random Horn-SAT instance (each clause has at most one positive literal)."""
    m = int(n * alpha)
    for attempt in range(max_attempts):
        clauses = []
        for _ in range(m):
            k = random.choice([2, 3])
            vs = random.sample(range(n), k)
            # Horn: at most one positive literal
            # Format: all negative except possibly the first
            signs = [0] * k
            if random.random() < 0.5:
                signs[0] = 1  # one positive literal
            clauses.append(list(zip(vs, signs)))

        if n <= ENUM_THRESHOLD:
            sols = enumerate_solutions(n, clauses)
            if len(sols) >= min_solutions:
                return clauses, sols
        else:
            if PYSAT_AVAILABLE:
                sat, _ = check_sat_pysat(n, clauses)
                if sat:
                    return clauses, None
            else:
                return clauses, None
    return None, None


# ============================================================
# 3. Solution enumeration (n <= 16)
# ============================================================

def enumerate_solutions(n, clauses):
    """Brute-force enumerate all solutions."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if eval_all_clauses(assignment, clauses):
            solutions.append(assignment)
    return solutions


# ============================================================
# 4. SAT solver interface (pysat)
# ============================================================

def clauses_to_cnf(n, clauses):
    """Convert our clause format to pysat CNF format.
    pysat uses 1-indexed variables: var v with sign s ->
      positive literal: v+1, negative literal: -(v+1)
    """
    cnf_clauses = []
    for clause in clauses:
        lits = []
        for v, s in clause:
            if s == 1:
                lits.append(v + 1)
            else:
                lits.append(-(v + 1))
        cnf_clauses.append(lits)
    return cnf_clauses


def check_sat_pysat(n, clauses):
    """Check satisfiability and return one solution if SAT."""
    cnf_clauses = clauses_to_cnf(n, clauses)
    with Glucose4() as solver:
        for cl in cnf_clauses:
            solver.add_clause(cl)
        if solver.solve():
            model = solver.get_model()
            assignment = tuple(1 if model[i] > 0 else 0 for i in range(n))
            return True, assignment
        return False, None


def enumerate_solutions_sat(n, clauses, max_solutions=5000):
    """Use SAT solver to enumerate solutions (with blocking clauses)."""
    cnf_clauses = clauses_to_cnf(n, clauses)
    solutions = []
    with Glucose4() as solver:
        for cl in cnf_clauses:
            solver.add_clause(cl)
        while solver.solve() and len(solutions) < max_solutions:
            model = solver.get_model()
            assignment = tuple(1 if model[i] > 0 else 0 for i in range(n))
            solutions.append(assignment)
            # Add blocking clause to exclude this solution
            block = [-(v + 1) if assignment[v] == 1 else (v + 1) for v in range(n)]
            solver.add_clause(block)
    return solutions


# ============================================================
# 5. WalkSAT solution sampler (for approximate uniform sampling)
# ============================================================

def walksat_sample(n, clauses, num_samples=MC_SAMPLES_SOL, max_flips=10000, noise=0.4):
    """Sample solutions via WalkSAT with random restarts.
    Not perfectly uniform, but covers the solution space reasonably well.
    """
    solutions_set = set()
    solutions = []

    for restart in range(max(num_samples * 2, WALKSAT_RESTARTS)):
        if len(solutions) >= num_samples:
            break

        # Random initial assignment
        assignment = list(random.randint(0, 1) for _ in range(n))

        for flip in range(max_flips):
            # Find unsatisfied clauses
            unsat = []
            for ci, clause in enumerate(clauses):
                if not eval_clause_ksat(assignment, clause):
                    unsat.append(ci)

            if not unsat:
                # Found a solution
                sol_tuple = tuple(assignment)
                if sol_tuple not in solutions_set:
                    solutions_set.add(sol_tuple)
                    solutions.append(sol_tuple)
                # Perturb and continue to find more solutions
                num_perturb = max(1, n // 4)
                for _ in range(num_perturb):
                    idx = random.randint(0, n - 1)
                    assignment[idx] = 1 - assignment[idx]
                continue

            # Pick a random unsatisfied clause
            ci = random.choice(unsat)
            clause = clauses[ci]

            if random.random() < noise:
                # Random walk: flip a random variable in the clause
                v, s = random.choice(clause)
                assignment[v] = 1 - assignment[v]
            else:
                # Greedy: flip the variable that minimizes unsatisfied clauses
                best_v = None
                best_unsat = len(clauses) + 1
                for v, s in clause:
                    assignment[v] = 1 - assignment[v]
                    num_unsat = sum(
                        1 for c in clauses if not eval_clause_ksat(assignment, c)
                    )
                    assignment[v] = 1 - assignment[v]
                    if num_unsat < best_unsat:
                        best_unsat = num_unsat
                        best_v = v
                if best_v is not None:
                    assignment[best_v] = 1 - assignment[best_v]

    return solutions


def get_solutions(n, clauses, existing_sols=None):
    """Get solutions: enumerate if small, sample if large."""
    if existing_sols is not None:
        return existing_sols

    if n <= ENUM_THRESHOLD:
        return enumerate_solutions(n, clauses)

    # For large n, combine SAT solver enumeration with WalkSAT sampling
    solutions = []
    sol_set = set()

    # Phase 1: SAT solver enumeration (up to a budget)
    if PYSAT_AVAILABLE:
        enum_sols = enumerate_solutions_sat(n, clauses, max_solutions=min(MC_SAMPLES_SOL, 3000))
        for s in enum_sols:
            if s not in sol_set:
                sol_set.add(s)
                solutions.append(s)
        print(f"    SAT solver found {len(solutions)} solutions")

    # Phase 2: WalkSAT sampling for diversity
    walk_sols = walksat_sample(n, clauses, num_samples=MC_SAMPLES_SOL)
    for s in walk_sols:
        if s not in sol_set:
            sol_set.add(s)
            solutions.append(s)
    print(f"    Total unique solutions: {len(solutions)}")

    return solutions


# ============================================================
# 6. Constraint graph construction
# ============================================================

def build_constraint_graph(n, clauses):
    """Build the constraint graph.
    Nodes = variables (0..n-1).
    Edges = pairs of variables that co-occur in some clause.
    Also track which clauses each edge participates in (for area estimation).
    """
    adjacency = defaultdict(set)  # var -> set of neighbor vars
    edge_clauses = defaultdict(set)  # (v1, v2) -> set of clause indices
    var_clauses = defaultdict(set)   # var -> set of clause indices

    for ci, clause in enumerate(clauses):
        vars_in_clause = [v for v, s in clause]
        for v in vars_in_clause:
            var_clauses[v].add(ci)
        for i in range(len(vars_in_clause)):
            for j in range(i + 1, len(vars_in_clause)):
                v1, v2 = min(vars_in_clause[i], vars_in_clause[j]), \
                          max(vars_in_clause[i], vars_in_clause[j])
                adjacency[v1].add(v2)
                adjacency[v2].add(v1)
                edge_clauses[(v1, v2)].add(ci)

    return adjacency, edge_clauses, var_clauses


def find_cycles(adjacency, n, target_length, max_cycles=50):
    """Find simple cycles of a given length in the constraint graph.
    Uses DFS with bounded depth.
    """
    cycles_found = []
    visited_cycles = set()
    nodes = list(range(n))
    random.shuffle(nodes)

    for start in nodes:
        if len(cycles_found) >= max_cycles:
            break
        # DFS from start, looking for paths of length target_length that return
        stack = [(start, [start], {start})]
        while stack and len(cycles_found) < max_cycles:
            node, path, visited = stack.pop()
            if len(path) == target_length:
                # Check if we can close the cycle
                if start in adjacency.get(node, set()):
                    # Normalize cycle: start with smallest node, then choose direction
                    cycle = tuple(path)
                    # Canonical form: rotate so min element is first
                    min_idx = cycle.index(min(cycle))
                    rotated = cycle[min_idx:] + cycle[:min_idx]
                    # Choose direction (smaller second element)
                    reversed_cycle = (rotated[0],) + tuple(reversed(rotated[1:]))
                    canonical = min(rotated, reversed_cycle)
                    if canonical not in visited_cycles:
                        visited_cycles.add(canonical)
                        cycles_found.append(list(path))
                continue
            if len(path) >= target_length:
                continue
            neighbors = list(adjacency.get(node, set()))
            random.shuffle(neighbors)
            for nb in neighbors:
                if nb == start and len(path) == target_length - 1:
                    # Can close the cycle at the right length
                    # Check via the closing step above
                    path_new = path + [nb]
                    cycle = tuple(path)
                    min_idx = cycle.index(min(cycle))
                    rotated = cycle[min_idx:] + cycle[:min_idx]
                    reversed_cycle = (rotated[0],) + tuple(reversed(rotated[1:]))
                    canonical = min(rotated, reversed_cycle)
                    if canonical not in visited_cycles:
                        visited_cycles.add(canonical)
                        cycles_found.append(list(path))
                elif nb not in visited and nb != start:
                    stack.append((nb, path + [nb], visited | {nb}))

    return cycles_found


# ============================================================
# 7. Area estimation for cycles
# ============================================================

def estimate_cycle_area(cycle, var_clauses, clauses):
    """Estimate the area enclosed by a cycle in the constraint graph.

    Area = number of clauses whose variables are ALL contained within
    the set of variables on or "inside" the cycle.

    For a simple approximation on non-planar graphs:
    Area ~ number of clauses that involve ONLY variables in the cycle
    plus a fraction of clauses that share 2+ variables with the cycle.

    A better proxy (used here): for a cycle of length L, the effective
    area scales as L*(L-1)/2 (triangulation of the enclosed region),
    normalized by the graph density. We use the clause-count proxy:

    Area(C) = sum over clauses c of (fraction of c's variables in C)^2
    """
    cycle_vars = set(cycle)
    area = 0.0
    for ci, clause in enumerate(clauses):
        clause_vars = set(v for v, s in clause)
        overlap = len(clause_vars & cycle_vars)
        total = len(clause_vars)
        if total > 0:
            # Contribution: fraction of clause variables in the cycle, squared
            # This weights clauses fully inside the cycle more heavily
            frac = overlap / total
            area += frac * frac
    return area


def estimate_cycle_area_combinatorial(cycle_length):
    """Combinatorial area estimate for a cycle of length L.
    For a regular polygon of L sides inscribed in a constraint graph,
    the enclosed area scales as L^2 / (4*pi) ~ L^2 / 12.57.
    We use the simpler approximation: A ~ L*(L-1)/6
    (number of non-adjacent pairs, divided by 2 for double-counting).
    This matches the A5 data:
      L=3: A~1, L=4: A~2, L=5: A~3.3, L=6: A~5, L=7: A~7, L=8: A~9.3
    """
    return cycle_length * (cycle_length - 1) / 6.0


# ============================================================
# 8. Holonomy defect computation
# ============================================================

def coordinatewise_majority(a, b, c):
    """Compute coordinatewise majority of three binary tuples."""
    return tuple(int(a[i] + b[i] + c[i] >= 2) for i in range(len(a)))


def restrict_to_cycle(assignment, cycle_vars):
    """Restrict an assignment to the variables in a cycle."""
    return tuple(assignment[v] for v in cycle_vars)


def compute_holonomy_defect_exact(cycle, clauses, solutions, sol_set=None):
    """Compute holonomy defect for a cycle using exact solution enumeration.

    H(C) = fraction of (a, b, c) in Sol^3 where maj(a,b,c)
    restricted to the cycle variables violates some clause
    that involves cycle variables.

    More precisely: we check if the majority of three solutions,
    restricted to the cycle's variable scope, is consistent with
    all constraints touching the cycle.
    """
    if sol_set is None:
        sol_set = set(solutions)

    cycle_vars = list(cycle)
    cycle_var_set = set(cycle_vars)

    # Find clauses relevant to this cycle (all variables in the clause are in the cycle)
    relevant_clauses = []
    for clause in clauses:
        clause_vars = set(v for v, s in clause)
        if clause_vars.issubset(cycle_var_set):
            relevant_clauses.append(clause)

    if not relevant_clauses:
        # No clause is fully contained in this cycle
        # Use partial constraint: clauses with >= 2 variables in cycle
        for clause in clauses:
            clause_vars = set(v for v, s in clause)
            if len(clause_vars & cycle_var_set) >= 2:
                relevant_clauses.append(clause)

    if not relevant_clauses:
        return 0.0

    S = len(solutions)
    if S == 0:
        return 0.0

    # For small solution sets, enumerate all triples
    if S <= 100:
        violations = 0
        total = 0
        for a in solutions:
            for b in solutions:
                for c in solutions:
                    total += 1
                    maj = coordinatewise_majority(a, b, c)
                    # Check if majority satisfies the relevant clauses
                    if not all(eval_clause_ksat(maj, cl) for cl in relevant_clauses):
                        violations += 1
        return violations / total if total > 0 else 0.0
    else:
        # Monte Carlo sampling of triples
        violations = 0
        total = MC_SAMPLES_TRIPLES
        for _ in range(total):
            a = random.choice(solutions)
            b = random.choice(solutions)
            c = random.choice(solutions)
            maj = coordinatewise_majority(a, b, c)
            if not all(eval_clause_ksat(maj, cl) for cl in relevant_clauses):
                violations += 1
        return violations / total


def compute_holonomy_defect_mc(cycle, clauses, solutions):
    """Monte Carlo holonomy defect for large solution sets."""
    return compute_holonomy_defect_exact(cycle, clauses, solutions)


# ============================================================
# 9. String tension extraction
# ============================================================

def extract_string_tension(H_values, areas, cycle_lengths):
    """Extract string tension sigma from H vs Area data.

    Fit H(L) = sigma * A(L) + offset
    Also fit H(L) = sigma_p * L + offset_p (perimeter law, control)

    Returns sigma, R2_area, sigma_p, R2_perimeter, fit_details
    """
    H = np.array(H_values, dtype=float)
    A = np.array(areas, dtype=float)
    L = np.array(cycle_lengths, dtype=float)

    # Filter out zero-length data
    mask = H > 0
    if mask.sum() < 2:
        return 0.0, 0.0, 0.0, 0.0, {'status': 'insufficient_nonzero_data'}

    # Area law fit: H = sigma * A
    # Use linear regression (with intercept for robustness)
    if len(A[mask]) >= 2:
        slope_a, intercept_a, r_a, p_a, se_a = linregress(A[mask], H[mask])
        R2_area = r_a ** 2
        sigma = max(slope_a, 0.0)  # string tension must be non-negative
    else:
        sigma, R2_area, intercept_a, se_a = 0.0, 0.0, 0.0, 0.0

    # Perimeter law fit: H = sigma_p * L
    if len(L[mask]) >= 2:
        slope_p, intercept_p, r_p, p_p, se_p = linregress(L[mask], H[mask])
        R2_perimeter = r_p ** 2
        sigma_p = max(slope_p, 0.0)
    else:
        sigma_p, R2_perimeter = 0.0, 0.0

    fit_details = {
        'sigma_area': sigma,
        'R2_area': R2_area,
        'intercept_area': intercept_a,
        'se_area': se_a,
        'sigma_perimeter': sigma_p,
        'R2_perimeter': R2_perimeter,
        'H_values': H.tolist(),
        'areas': A.tolist(),
        'cycle_lengths': L.tolist(),
    }

    return sigma, R2_area, sigma_p, R2_perimeter, fit_details


# ============================================================
# 10. Finite-size scaling of sigma(n)
# ============================================================

def fit_sigma_convergence(n_values, sigma_values):
    """Fit sigma(n) = sigma_inf + c / n^beta to determine if sigma_inf > 0.

    Also fits:
      Model A: sigma(n) = sigma_inf + c / n^2  (fixed beta=2, YM analog)
      Model B: sigma(n) = a * n^(-alpha)         (power-law decay to 0)
      Model C: sigma(n) = sigma_inf + c / n^beta  (free beta)
    """
    n_arr = np.array(n_values, dtype=float)
    s_arr = np.array(sigma_values, dtype=float)

    results = {}

    # Filter out zeros
    mask = s_arr > 0
    if mask.sum() < 2:
        return {'status': 'insufficient_data', 'sigma_inf_best': 0.0}

    n_fit = n_arr[mask]
    s_fit = s_arr[mask]

    # Model A: sigma = sigma_inf + c / n^2
    try:
        def model_a(n, sigma_inf, c):
            return sigma_inf + c / n**2
        popt_a, pcov_a = curve_fit(model_a, n_fit, s_fit, p0=[0.001, 0.1],
                                   bounds=([-0.01, -10], [0.1, 10]))
        s_pred_a = model_a(n_fit, *popt_a)
        ss_res_a = np.sum((s_fit - s_pred_a)**2)
        ss_tot = np.sum((s_fit - s_fit.mean())**2)
        R2_a = 1 - ss_res_a / ss_tot if ss_tot > 0 else 0.0
        results['model_A'] = {
            'sigma_inf': popt_a[0],
            'c': popt_a[1],
            'beta': 2.0,
            'R2': R2_a,
            'sigma_inf_se': np.sqrt(pcov_a[0, 0]) if pcov_a[0, 0] > 0 else 0.0,
        }
    except Exception as e:
        results['model_A'] = {'error': str(e)}

    # Model B: sigma = a * n^(-alpha)  (tests sigma -> 0 hypothesis)
    try:
        def model_b(n, a, alpha):
            return a * n**(-alpha)
        popt_b, pcov_b = curve_fit(model_b, n_fit, s_fit, p0=[0.1, 1.0],
                                   bounds=([0.0, 0.0], [100, 10]))
        s_pred_b = model_b(n_fit, *popt_b)
        ss_res_b = np.sum((s_fit - s_pred_b)**2)
        R2_b = 1 - ss_res_b / ss_tot if ss_tot > 0 else 0.0
        results['model_B'] = {
            'a': popt_b[0],
            'alpha': popt_b[1],
            'R2': R2_b,
        }
    except Exception as e:
        results['model_B'] = {'error': str(e)}

    # Model C: sigma = sigma_inf + c / n^beta  (general)
    try:
        def model_c(n, sigma_inf, c, beta):
            return sigma_inf + c / n**beta
        popt_c, pcov_c = curve_fit(model_c, n_fit, s_fit, p0=[0.0005, 0.1, 2.0],
                                   bounds=([-0.01, -10, 0.1], [0.1, 100, 10]),
                                   maxfev=10000)
        s_pred_c = model_c(n_fit, *popt_c)
        ss_res_c = np.sum((s_fit - s_pred_c)**2)
        R2_c = 1 - ss_res_c / ss_tot if ss_tot > 0 else 0.0
        results['model_C'] = {
            'sigma_inf': popt_c[0],
            'c': popt_c[1],
            'beta': popt_c[2],
            'R2': R2_c,
            'sigma_inf_se': np.sqrt(pcov_c[0, 0]) if pcov_c[0, 0] > 0 else 0.0,
        }
    except Exception as e:
        results['model_C'] = {'error': str(e)}

    # Determine best model
    best_model = None
    best_R2 = -1
    for key in ['model_A', 'model_B', 'model_C']:
        if key in results and 'R2' in results[key]:
            if results[key]['R2'] > best_R2:
                best_R2 = results[key]['R2']
                best_model = key

    # Extract sigma_inf from best model
    sigma_inf_best = 0.0
    if best_model == 'model_A':
        sigma_inf_best = results['model_A']['sigma_inf']
    elif best_model == 'model_B':
        sigma_inf_best = 0.0  # power-law model has sigma_inf = 0
    elif best_model == 'model_C':
        sigma_inf_best = results['model_C']['sigma_inf']

    results['best_model'] = best_model
    results['best_R2'] = best_R2
    results['sigma_inf_best'] = sigma_inf_best
    results['status'] = 'ok'

    return results


# ============================================================
# 11. Main computation for one SAT type
# ============================================================

def run_area_law_computation(sat_type, n_values, generate_func, label=""):
    """Run the full area law / string tension computation for one SAT type."""
    print(f"\n{'='*80}")
    print(f"  {label}: Area Law String Tension Computation")
    print(f"  SAT type: {sat_type}, n = {n_values}")
    print(f"{'='*80}")

    all_results = {}

    for n in n_values:
        t0 = time.time()
        print(f"\n  --- n = {n} ---")

        instance_sigmas = []
        instance_H_data = []

        for inst_idx in range(NUM_INSTANCES):
            print(f"    Instance {inst_idx + 1}/{NUM_INSTANCES}...", end="", flush=True)

            clauses, sols = generate_func(n)
            if clauses is None:
                print(" FAILED to generate instance")
                continue

            # Get solutions
            solutions = get_solutions(n, clauses, sols)
            if not solutions or len(solutions) < 2:
                print(f" only {len(solutions) if solutions else 0} solutions, skipping")
                continue

            # Build constraint graph
            adjacency, edge_clauses, var_clauses = build_constraint_graph(n, clauses)

            # Compute holonomy defect for each cycle length
            H_by_length = {}
            areas_by_length = {}

            for L in CYCLE_LENGTHS:
                cycles = find_cycles(adjacency, n, L, max_cycles=20)
                if not cycles:
                    continue

                H_values_for_L = []
                area_values_for_L = []

                for cycle in cycles:
                    # Compute holonomy defect
                    H = compute_holonomy_defect_exact(cycle, clauses, solutions)
                    H_values_for_L.append(H)

                    # Estimate area
                    area = estimate_cycle_area(cycle, var_clauses, clauses)
                    area_values_for_L.append(area)

                if H_values_for_L:
                    H_by_length[L] = np.mean(H_values_for_L)
                    areas_by_length[L] = np.mean(area_values_for_L)

            # Extract string tension
            if len(H_by_length) >= 3:
                lengths_used = sorted(H_by_length.keys())
                H_vals = [H_by_length[l] for l in lengths_used]
                area_vals = [areas_by_length[l] for l in lengths_used]

                sigma, R2_area, sigma_p, R2_perim, details = \
                    extract_string_tension(H_vals, area_vals, lengths_used)

                instance_sigmas.append(sigma)
                instance_H_data.append({
                    'H_by_length': {int(k): v for k, v in H_by_length.items()},
                    'areas_by_length': {int(k): v for k, v in areas_by_length.items()},
                    'sigma': sigma,
                    'R2_area': R2_area,
                    'R2_perim': R2_perim,
                    'num_solutions': len(solutions),
                })
                print(f" sigma={sigma:.6f}, R2_area={R2_area:.4f}, |Sol|={len(solutions)}")
            else:
                print(f" insufficient cycle data ({len(H_by_length)} lengths)")

        # Aggregate across instances for this n
        if instance_sigmas:
            sigma_mean = np.mean(instance_sigmas)
            sigma_std = np.std(instance_sigmas)
            sigma_median = np.median(instance_sigmas)

            # Average H by cycle length across instances
            avg_H_by_length = defaultdict(list)
            avg_area_by_length = defaultdict(list)
            for data in instance_H_data:
                for L, H in data['H_by_length'].items():
                    avg_H_by_length[L].append(H)
                for L, A in data['areas_by_length'].items():
                    avg_area_by_length[L].append(A)

            avg_H = {L: np.mean(vals) for L, vals in avg_H_by_length.items()}
            avg_A = {L: np.mean(vals) for L, vals in avg_area_by_length.items()}

            all_results[n] = {
                'sigma_mean': sigma_mean,
                'sigma_std': sigma_std,
                'sigma_median': sigma_median,
                'num_instances': len(instance_sigmas),
                'avg_H_by_length': {int(k): float(v) for k, v in avg_H.items()},
                'avg_area_by_length': {int(k): float(v) for k, v in avg_A.items()},
                'instance_data': instance_H_data,
            }

            elapsed = time.time() - t0
            print(f"\n  n={n}: sigma = {sigma_mean:.6f} +/- {sigma_std:.6f} "
                  f"(median {sigma_median:.6f}), "
                  f"{len(instance_sigmas)} instances, {elapsed:.1f}s")
        else:
            all_results[n] = {'sigma_mean': 0.0, 'sigma_std': 0.0,
                              'num_instances': 0}
            print(f"\n  n={n}: NO valid instances")

    return all_results


# ============================================================
# 12. Main
# ============================================================

def main():
    print("=" * 80)
    print("  AREA LAW STRING TENSION -- LARGE-n COMPUTATION")
    print("  Sub-gap E-1: Does sigma(L, n) -> sigma_inf > 0 as n -> infinity?")
    print("=" * 80)
    print(f"\n  pysat available: {PYSAT_AVAILABLE}")
    print(f"  n values: {N_VALUES}")
    print(f"  Instances per (type, n): {NUM_INSTANCES}")
    print(f"  Cycle lengths: {CYCLE_LENGTHS}")
    print(f"  MC samples (solutions): {MC_SAMPLES_SOL}")
    print(f"  MC samples (triples): {MC_SAMPLES_TRIPLES}")
    print(f"  Enumeration threshold: n <= {ENUM_THRESHOLD}")

    # ---- 3-SAT (NPC) ----
    print("\n\n" + "#" * 80)
    print("  3-SAT (NPC) -- should have sigma > 0")
    print("#" * 80)

    results_3sat = run_area_law_computation(
        "3-SAT", N_VALUES,
        lambda n: generate_3sat_instance(n, alpha=ALPHA_3SAT, min_solutions=4),
        label="3-SAT"
    )

    # ---- 2-SAT (P-time control) ----
    print("\n\n" + "#" * 80)
    print("  2-SAT (P-time) -- should have sigma = 0")
    print("#" * 80)

    results_2sat = run_area_law_computation(
        "2-SAT", N_VALUES,
        lambda n: generate_2sat_instance(n, alpha=ALPHA_2SAT, min_solutions=8),
        label="2-SAT"
    )

    # ---- Horn-SAT (P-time control) ----
    print("\n\n" + "#" * 80)
    print("  Horn-SAT (P-time) -- should have sigma = 0")
    print("#" * 80)

    results_horn = run_area_law_computation(
        "Horn-SAT", N_VALUES,
        lambda n: generate_horn_instance(n, alpha=ALPHA_HORN, min_solutions=8),
        label="Horn-SAT"
    )

    # ============================================================
    # 13. Convergence analysis for 3-SAT
    # ============================================================
    print("\n\n" + "=" * 80)
    print("  CONVERGENCE ANALYSIS: sigma(n) -> sigma_inf ?")
    print("=" * 80)

    # Include prior data points
    prior_sigma = {12: 0.00170, 14: 0.00132}
    all_n = sorted(set(list(prior_sigma.keys()) + N_VALUES))
    all_sigma = []

    for n in all_n:
        if n in prior_sigma and n not in results_3sat:
            all_sigma.append(prior_sigma[n])
        elif n in results_3sat:
            all_sigma.append(results_3sat[n]['sigma_mean'])
        elif n in prior_sigma:
            all_sigma.append(prior_sigma[n])

    print(f"\n  3-SAT string tension data:")
    print(f"  {'n':>4s}  {'sigma':>12s}")
    print(f"  {'----':>4s}  {'--------':>12s}")
    for n, s in zip(all_n, all_sigma):
        source = "(prior)" if n in prior_sigma and n not in N_VALUES else "(new)"
        print(f"  {n:4d}  {s:12.6f}  {source}")

    # Fit convergence models
    if len(all_sigma) >= 3:
        conv_results = fit_sigma_convergence(all_n, all_sigma)

        print(f"\n  Convergence fit results:")
        for model_key in ['model_A', 'model_B', 'model_C']:
            if model_key in conv_results:
                m = conv_results[model_key]
                if 'error' in m:
                    print(f"    {model_key}: ERROR - {m['error']}")
                else:
                    print(f"    {model_key}:")
                    for k, v in m.items():
                        print(f"      {k}: {v:.8f}" if isinstance(v, float) else f"      {k}: {v}")

        print(f"\n  Best model: {conv_results.get('best_model', 'none')}")
        print(f"  Best R2: {conv_results.get('best_R2', 0):.6f}")
        print(f"  sigma_inf (best): {conv_results.get('sigma_inf_best', 0):.8f}")

        # Explicit test: is sigma_inf > 0?
        sigma_inf = conv_results.get('sigma_inf_best', 0)
        if sigma_inf > 0:
            print(f"\n  *** RESULT: sigma_inf = {sigma_inf:.6f} > 0 ***")
            print(f"  *** Sub-gap E-1 is SUPPORTED: string tension converges to positive limit ***")
        else:
            print(f"\n  *** RESULT: sigma_inf = {sigma_inf:.6f} <= 0 ***")
            print(f"  *** Sub-gap E-1 is NOT SUPPORTED by this data ***")
    else:
        conv_results = {'status': 'insufficient_data'}
        print("\n  Insufficient data for convergence analysis")

    # ============================================================
    # 14. Controls: 2-SAT and Horn-SAT should show sigma = 0
    # ============================================================
    print("\n\n" + "=" * 80)
    print("  CONTROL CHECK: P-time classes should have sigma = 0")
    print("=" * 80)

    for label, results in [("2-SAT", results_2sat), ("Horn-SAT", results_horn)]:
        print(f"\n  {label}:")
        for n in N_VALUES:
            if n in results and results[n]['num_instances'] > 0:
                s = results[n]['sigma_mean']
                print(f"    n={n}: sigma = {s:.8f}")
            else:
                print(f"    n={n}: no data")

    # ============================================================
    # 15. Summary table
    # ============================================================
    print("\n\n" + "=" * 80)
    print("  SUMMARY TABLE")
    print("=" * 80)

    print(f"\n  {'Type':>10s} | {'n':>4s} | {'sigma':>12s} | {'sigma_std':>12s} | {'R2_area':>8s} | {'#inst':>6s}")
    print(f"  {'-'*10:>10s}-+-{'-'*4:>4s}-+-{'-'*12:>12s}-+-{'-'*12:>12s}-+-{'-'*8:>8s}-+-{'-'*6:>6s}")

    for label, results in [("3-SAT", results_3sat), ("2-SAT", results_2sat),
                           ("Horn-SAT", results_horn)]:
        for n in N_VALUES:
            if n in results and results[n]['num_instances'] > 0:
                r = results[n]
                # Compute average R2 from instance data if available
                r2s = []
                for idata in r.get('instance_data', []):
                    if 'R2_area' in idata:
                        r2s.append(idata['R2_area'])
                avg_r2 = np.mean(r2s) if r2s else 0.0
                print(f"  {label:>10s} | {n:4d} | {r['sigma_mean']:12.6f} | "
                      f"{r['sigma_std']:12.6f} | {avg_r2:8.4f} | {r['num_instances']:6d}")
            else:
                print(f"  {label:>10s} | {n:4d} | {'---':>12s} | {'---':>12s} | {'---':>8s} | {'0':>6s}")

    # ============================================================
    # 16. Holonomy profile H(L) for 3-SAT
    # ============================================================
    print("\n\n" + "=" * 80)
    print("  HOLONOMY PROFILE H(L) for 3-SAT")
    print("=" * 80)

    print(f"\n  {'n':>4s} | ", end="")
    for L in CYCLE_LENGTHS:
        print(f"{'H(L='+str(L)+')':>10s} | ", end="")
    print()

    for n in N_VALUES:
        if n in results_3sat and results_3sat[n]['num_instances'] > 0:
            r = results_3sat[n]
            print(f"  {n:4d} | ", end="")
            for L in CYCLE_LENGTHS:
                if L in r['avg_H_by_length']:
                    print(f"{r['avg_H_by_length'][L]:10.6f} | ", end="")
                else:
                    print(f"{'---':>10s} | ", end="")
            print()

    # ============================================================
    # 17. Ratio analysis: sigma(n+2)/sigma(n)
    # ============================================================
    print("\n\n" + "=" * 80)
    print("  RATIO ANALYSIS: sigma(n+2) / sigma(n)")
    print("=" * 80)

    print(f"\n  3-SAT string tension progression:")
    for i in range(len(all_n) - 1):
        n1, n2 = all_n[i], all_n[i+1]
        s1, s2 = all_sigma[i], all_sigma[i+1]
        if s1 > 0:
            ratio = s2 / s1
            print(f"    sigma({n2})/sigma({n1}) = {s2:.6f}/{s1:.6f} = {ratio:.4f}")

    # ============================================================
    # 18. Save results
    # ============================================================
    output = {
        'metadata': {
            'node': '2.4-E1-string-tension',
            'date': '2026-04-11',
            'author': 'Claude Opus 4.6 (1M context)',
            'alpha_3sat': ALPHA_3SAT,
            'alpha_2sat': ALPHA_2SAT,
            'alpha_horn': ALPHA_HORN,
            'num_instances': NUM_INSTANCES,
            'mc_samples_sol': MC_SAMPLES_SOL,
            'mc_samples_triples': MC_SAMPLES_TRIPLES,
            'cycle_lengths': CYCLE_LENGTHS,
            'n_values': N_VALUES,
        },
        '3sat': {},
        '2sat': {},
        'horn': {},
        'convergence': {},
    }

    for n in N_VALUES:
        for key, results in [('3sat', results_3sat), ('2sat', results_2sat),
                             ('horn', results_horn)]:
            if n in results:
                r = results[n]
                output[key][str(n)] = {
                    'sigma_mean': float(r['sigma_mean']),
                    'sigma_std': float(r['sigma_std']),
                    'sigma_median': float(r.get('sigma_median', 0)),
                    'num_instances': int(r['num_instances']),
                    'avg_H_by_length': {str(k): float(v)
                                        for k, v in r.get('avg_H_by_length', {}).items()},
                    'avg_area_by_length': {str(k): float(v)
                                           for k, v in r.get('avg_area_by_length', {}).items()},
                }

    if conv_results.get('status') == 'ok':
        output['convergence'] = {
            'all_n': [int(x) for x in all_n],
            'all_sigma': [float(x) for x in all_sigma],
            'sigma_inf_best': float(conv_results.get('sigma_inf_best', 0)),
            'best_model': conv_results.get('best_model', ''),
            'best_R2': float(conv_results.get('best_R2', 0)),
            'models': {},
        }
        for mk in ['model_A', 'model_B', 'model_C']:
            if mk in conv_results and 'error' not in conv_results[mk]:
                output['convergence']['models'][mk] = {
                    k: float(v) if isinstance(v, (float, np.floating)) else v
                    for k, v in conv_results[mk].items()
                }

    results_path = '/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/' \
                   'clone-growth-fullness-bridge/code/area_law_large_n_results.json'
    with open(results_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results saved to: {results_path}")

    # ============================================================
    # 19. VERDICT
    # ============================================================
    print("\n\n" + "=" * 80)
    print("  VERDICT on Sub-gap E-1")
    print("=" * 80)

    # Collect all 3-SAT sigmas
    three_sat_sigmas = {}
    for n, s in zip(all_n, all_sigma):
        three_sat_sigmas[n] = s

    # Check controls
    control_pass = True
    for label, results in [("2-SAT", results_2sat), ("Horn-SAT", results_horn)]:
        for n in N_VALUES:
            if n in results and results[n]['num_instances'] > 0:
                if results[n]['sigma_mean'] > 0.0005:
                    control_pass = False

    # Check 3-SAT convergence
    if len(all_sigma) >= 4:
        # Check if sigma is still positive at largest n
        sigma_largest = all_sigma[-1]
        sigma_inf = conv_results.get('sigma_inf_best', 0)

        # Check if ratio sigma(n+2)/sigma(n) is stabilizing
        ratios = []
        for i in range(len(all_sigma) - 1):
            if all_sigma[i] > 0:
                ratios.append(all_sigma[i+1] / all_sigma[i])

        ratio_trend = "stabilizing" if len(ratios) >= 3 and \
            abs(ratios[-1] - ratios[-2]) < abs(ratios[-2] - ratios[-3]) else "unclear"

        print(f"\n  3-SAT string tension at n={all_n[-1]}: sigma = {sigma_largest:.6f}")
        print(f"  Extrapolated sigma_inf: {sigma_inf:.6f}")
        print(f"  Successive ratios: {[f'{r:.4f}' for r in ratios]}")
        print(f"  Ratio trend: {ratio_trend}")
        print(f"  Controls (2-SAT, Horn-SAT) sigma=0: {'PASS' if control_pass else 'FAIL'}")

        if sigma_inf > 0 and sigma_largest > 0 and control_pass:
            print(f"\n  *** SUB-GAP E-1: SUPPORTED ***")
            print(f"  sigma(n) converges to sigma_inf = {sigma_inf:.6f} > 0")
            print(f"  The string tension is positive in the thermodynamic limit.")
            print(f"  This supports the area law route (E) to Gap Beta.")
            print(f"  Correlation length xi_L <= 1/(2*sigma_inf) = {1/(2*sigma_inf):.1f}")
            verdict = "SUPPORTED"
        elif sigma_largest > 0 and control_pass:
            print(f"\n  *** SUB-GAP E-1: PLAUSIBLE but fit inconclusive ***")
            print(f"  sigma remains positive at all tested n, but the fit is not decisive.")
            verdict = "PLAUSIBLE"
        else:
            print(f"\n  *** SUB-GAP E-1: NOT SUPPORTED by current data ***")
            verdict = "NOT_SUPPORTED"
    else:
        verdict = "INSUFFICIENT_DATA"
        print("\n  Insufficient data for a verdict")

    output['verdict'] = verdict
    with open(results_path, 'w') as f:
        json.dump(output, f, indent=2)

    return output


if __name__ == "__main__":
    main()
