"""
Area Law String Tension at Larger System Sizes -- Node 2.4 (Sub-gap E-1)

Closes E-1: does the string tension sigma(L, n) converge to a positive
limit as n -> infinity?

Method:
  1. Generate random k-SAT instances at n = 14, 16, 18, 20.
  2. Enumerate solutions (n <= 16) or sample via SAT solver + WalkSAT (n > 16).
  3. Compute holonomy defect H(L) for constraint-graph cycles of length L = 3..8.
     H(L) = 1 - (fraction of (a,b,c) in Sol^3 where majority(a,b,c) is in Sol).
     This is the GLOBAL holonomy defect (measures non-polymorphism rate).
     H_restricted(C) restricts to clauses touching cycle C.
  4. Fit H_restricted vs cycle area to extract string tension sigma.
  5. Fit sigma(n) = sigma_inf + c/n^beta to test convergence.

Controls:
  - 2-SAT: should have sigma = 0 at all n (majority IS a polymorphism -> flat connection)
  - Horn-SAT: should have sigma = 0 at all n (majority IS a polymorphism)

Prior data (A5):
  - 3-SAT: sigma = 0.00170 (n=12), sigma = 0.00132 (n=14)
  - 2-SAT: sigma = 0 at all n
  - H_restricted grows: 0.007 (L=3) to 0.071 (L=8) at n=12

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
    from pysat.solvers import Glucose4
    PYSAT_AVAILABLE = True
except ImportError:
    PYSAT_AVAILABLE = False
    print("WARNING: pysat not available. n > 16 will use heuristic sampling only.")

random.seed(42)
np.random.seed(42)
np.set_printoptions(precision=8, suppress=True, linewidth=130)

# ============================================================
# Configuration
# ============================================================

NUM_INSTANCES = 15           # instances per (type, n)
CYCLE_LENGTHS = [3, 4, 5, 6, 7, 8]
MC_TRIPLES = 8000            # triples sampled per cycle (MC mode)
WALKSAT_RESTARTS = 500       # restarts for solution sampling
ALPHA_3SAT = 3.5             # clause ratio (below threshold, to ensure enough solutions)
ALPHA_2SAT = 1.0
ALPHA_HORN = 2.0
N_VALUES = [14, 16, 18, 20]
ENUM_THRESHOLD = 16          # enumerate for n <= this

# Approximate area for cycles of length L in a random constraint graph
# (from A5 data calibration; matches L=3: ~1, L=8: ~17)
AREA_TABLE = {3: 1.0, 4: 2.5, 5: 5.0, 6: 8.0, 7: 12.0, 8: 17.0}


# ============================================================
# 1. Clause evaluation
# ============================================================

def eval_clause(assignment, clause):
    """Evaluate a k-SAT clause. clause = [(var, sign), ...].
    sign=1 means positive literal, sign=0 means negated."""
    return any(
        (assignment[v] if s == 1 else 1 - assignment[v])
        for v, s in clause
    )

def satisfies(assignment, clauses):
    return all(eval_clause(assignment, c) for c in clauses)


# ============================================================
# 2. Instance generation
# ============================================================

def generate_ksat_instance(n, k, alpha, min_solutions=4, max_attempts=2000):
    """Random k-SAT at clause-to-variable ratio alpha."""
    m = int(n * alpha)
    for _ in range(max_attempts):
        clauses = []
        for _ in range(m):
            vs = random.sample(range(n), k)
            signs = [random.choice([0, 1]) for _ in range(k)]
            clauses.append(list(zip(vs, signs)))

        if n <= ENUM_THRESHOLD:
            sols = enumerate_solutions(n, clauses)
            if len(sols) >= min_solutions:
                return clauses, sols
        else:
            # large n: quick SAT check + find a few solutions to verify multiplicity
            if PYSAT_AVAILABLE:
                sat, sol0 = check_sat(n, clauses)
                if sat:
                    # Quick check: find min_solutions via WalkSAT (faster than blocking)
                    quick = walksat_sample(n, clauses, num_samples=min_solutions, max_flips=5000)
                    if len(quick) >= min_solutions:
                        return clauses, None
            else:
                a = tuple(random.randint(0, 1) for _ in range(n))
                if satisfies(a, clauses):
                    return clauses, None
    return None, None


def generate_horn_instance(n, alpha=ALPHA_HORN, min_solutions=8, max_attempts=2000):
    """Random Horn-SAT (at most one positive literal per clause)."""
    m = int(n * alpha)
    for _ in range(max_attempts):
        clauses = []
        for _ in range(m):
            k = random.choice([2, 3])
            vs = random.sample(range(n), k)
            signs = [0] * k  # all negative
            if random.random() < 0.5:
                signs[0] = 1  # at most one positive
            clauses.append(list(zip(vs, signs)))

        if n <= ENUM_THRESHOLD:
            sols = enumerate_solutions(n, clauses)
            if len(sols) >= min_solutions:
                return clauses, sols
        else:
            if PYSAT_AVAILABLE:
                sat, _ = check_sat(n, clauses)
                if sat:
                    quick = walksat_sample(n, clauses, num_samples=min_solutions, max_flips=5000)
                    if len(quick) >= min_solutions:
                        return clauses, None
    return None, None


# ============================================================
# 3. Solution enumeration
# ============================================================

def enumerate_solutions(n, clauses):
    """Brute-force enumerate all solutions (n <= 16)."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if satisfies(assignment, clauses):
            solutions.append(assignment)
    return solutions


# ============================================================
# 4. SAT solver interface
# ============================================================

def clauses_to_cnf(n, clauses):
    """Convert to pysat format (1-indexed)."""
    cnf = []
    for clause in clauses:
        lits = [(v + 1) if s == 1 else -(v + 1) for v, s in clause]
        cnf.append(lits)
    return cnf


def check_sat(n, clauses):
    """Quick SAT check, returns (bool, assignment_or_None)."""
    cnf = clauses_to_cnf(n, clauses)
    with Glucose4() as solver:
        for cl in cnf:
            solver.add_clause(cl)
        if solver.solve():
            model = solver.get_model()
            # model is list of signed integers (1-indexed); convert to 0/1 tuple
            assignment = [0] * n
            for lit in model:
                v = abs(lit) - 1
                if 0 <= v < n:
                    assignment[v] = 1 if lit > 0 else 0
            return True, tuple(assignment)
        return False, None


def enumerate_solutions_sat(n, clauses, max_solutions=5000):
    """Enumerate solutions using blocking clauses."""
    cnf = clauses_to_cnf(n, clauses)
    solutions = []
    with Glucose4() as solver:
        for cl in cnf:
            solver.add_clause(cl)
        while solver.solve() and len(solutions) < max_solutions:
            model = solver.get_model()
            assignment = [0] * n
            for lit in model:
                v = abs(lit) - 1
                if 0 <= v < n:
                    assignment[v] = 1 if lit > 0 else 0
            assignment = tuple(assignment)
            solutions.append(assignment)
            block = [-(v + 1) if assignment[v] == 1 else (v + 1) for v in range(n)]
            solver.add_clause(block)
    return solutions


# ============================================================
# 5. WalkSAT solution sampler (optimized)
# ============================================================

def _build_var_clause_index(n, clauses):
    """Precompute: for each variable, which clause indices contain it."""
    idx = [[] for _ in range(n)]
    for ci, clause in enumerate(clauses):
        for v, _ in clause:
            idx[v].append(ci)
    return idx


def _count_unsat(assignment, clauses):
    """Count unsatisfied clauses."""
    return sum(1 for c in clauses if not eval_clause(assignment, c))


def walksat_sample(n, clauses, num_samples=200, max_flips=5000, noise=0.5):
    """Sample diverse solutions via WalkSAT with optimized greedy step.
    Uses variable-clause index for O(degree) flip evaluation instead of O(m).
    """
    found = set()
    solutions = []
    var_idx = _build_var_clause_index(n, clauses)
    m = len(clauses)

    restarts = max(num_samples * 4, 300)
    for _ in range(restarts):
        if len(solutions) >= num_samples:
            break
        assignment = [random.randint(0, 1) for _ in range(n)]

        # Precompute sat status for each clause
        sat_status = [eval_clause(assignment, c) for c in clauses]
        num_unsat = sum(1 for s in sat_status if not s)

        for _ in range(max_flips):
            if num_unsat == 0:
                t = tuple(assignment)
                if t not in found:
                    found.add(t)
                    solutions.append(t)
                # Perturb
                for _ in range(max(1, n // 5)):
                    v = random.randint(0, n - 1)
                    assignment[v] ^= 1
                    for ci in var_idx[v]:
                        old = sat_status[ci]
                        new = eval_clause(assignment, clauses[ci])
                        sat_status[ci] = new
                        if old and not new:
                            num_unsat += 1
                        elif not old and new:
                            num_unsat -= 1
                break  # restart after finding solution

            # Pick random unsatisfied clause
            unsat_list = [i for i in range(m) if not sat_status[i]]
            if not unsat_list:
                break
            ci = random.choice(unsat_list)
            clause = clauses[ci]

            if random.random() < noise:
                # Random walk
                v, _ = random.choice(clause)
            else:
                # Greedy: pick variable whose flip minimizes unsat
                best_v, best_delta = None, m + 1
                for v, _ in clause:
                    # Evaluate delta by checking only affected clauses
                    delta = 0
                    assignment[v] ^= 1
                    for ci2 in var_idx[v]:
                        old = sat_status[ci2]
                        new = eval_clause(assignment, clauses[ci2])
                        if old and not new:
                            delta += 1
                        elif not old and new:
                            delta -= 1
                    assignment[v] ^= 1
                    if delta < best_delta:
                        best_delta = delta
                        best_v = v
                v = best_v

            # Apply flip
            assignment[v] ^= 1
            for ci2 in var_idx[v]:
                old = sat_status[ci2]
                new = eval_clause(assignment, clauses[ci2])
                sat_status[ci2] = new
                if old and not new:
                    num_unsat += 1
                elif not old and new:
                    num_unsat -= 1

    return solutions


def get_solutions(n, clauses, existing_sols=None, target=300):
    """Get solutions via enumeration or sampling."""
    if existing_sols is not None:
        return existing_sols

    if n <= ENUM_THRESHOLD:
        return enumerate_solutions(n, clauses)

    solutions, sol_set = [], set()

    # For large n, SAT solver enumeration is slow due to blocking clauses.
    # Use a small budget (100) to seed, then WalkSAT for bulk sampling.
    if PYSAT_AVAILABLE:
        budget = min(100, target)
        for s in enumerate_solutions_sat(n, clauses, max_solutions=budget):
            if s not in sol_set:
                sol_set.add(s)
                solutions.append(s)

    # WalkSAT for the bulk of solution sampling
    for s in walksat_sample(n, clauses, num_samples=target):
        if s not in sol_set:
            sol_set.add(s)
            solutions.append(s)

    return solutions


# ============================================================
# 6. Constraint graph and cycle finder
# ============================================================

def build_constraint_graph(n, clauses):
    """Build variable co-occurrence graph."""
    adj = defaultdict(set)
    var_clauses = defaultdict(set)

    for ci, clause in enumerate(clauses):
        vs = [v for v, _ in clause]
        for v in vs:
            var_clauses[v].add(ci)
        for i in range(len(vs)):
            for j in range(i + 1, len(vs)):
                adj[vs[i]].add(vs[j])
                adj[vs[j]].add(vs[i])

    return adj, var_clauses


def find_cycles(adj, n, length, max_cycles=30):
    """Find simple cycles of given length via bounded DFS."""
    cycles_found = []
    seen = set()
    nodes = list(range(n))
    random.shuffle(nodes)

    for start in nodes:
        if len(cycles_found) >= max_cycles:
            break
        stack = [(start, [start], frozenset([start]))]
        while stack and len(cycles_found) < max_cycles:
            node, path, visited = stack.pop()
            if len(path) == length:
                if start in adj.get(node, set()):
                    canon = canonical_cycle(path)
                    if canon not in seen:
                        seen.add(canon)
                        cycles_found.append(list(path))
                continue
            if len(path) >= length:
                continue
            for nb in adj.get(node, set()):
                if nb not in visited or (nb == start and len(path) == length - 1):
                    if nb == start and len(path) == length - 1:
                        canon = canonical_cycle(path)
                        if canon not in seen:
                            seen.add(canon)
                            cycles_found.append(list(path))
                    elif nb not in visited:
                        stack.append((nb, path + [nb], visited | {nb}))
    return cycles_found


def canonical_cycle(path):
    """Canonical form for a cycle (rotation + direction invariant)."""
    t = tuple(path)
    m = min(t)
    idx = t.index(m)
    rotated = t[idx:] + t[:idx]
    rev = (rotated[0],) + tuple(reversed(rotated[1:]))
    return min(rotated, rev)


# ============================================================
# 7. Holonomy defect computation -- CORRECT DEFINITION
# ============================================================
#
# From Node 1.3.5.13 and A5:
#
# H_f(C) = 1 - |{(a,b,c) in Sol^3 : f(a,b,c) restricted to C is consistent}| / |Sol|^3
#
# where "consistent" = satisfies all constraints that TOUCH the cycle variables.
#
# For majority f = coordinatewise majority:
#   maj(a,b,c)[i] = 1 if a[i]+b[i]+c[i] >= 2 else 0
#
# A cycle C is a set of variables. A constraint "touches" C if >= 2 of its
# variables are in C. We check the majority restricted to C against all
# such touching constraints.
#
# This is the RESTRICTED holonomy. The GLOBAL holonomy (maj not in Sol at all)
# is always >= H_restricted.

def majority(a, b, c):
    """Coordinatewise majority."""
    return tuple(int(a[i] + b[i] + c[i] >= 2) for i in range(len(a)))


def compute_H_restricted(cycle_vars, clauses, solutions, sol_set=None, mc_budget=MC_TRIPLES):
    """Compute restricted holonomy defect for a cycle.

    H_restricted = fraction of (a,b,c) triples from Sol^3 where
    majority(a,b,c) restricted to cycle_vars violates at least one
    constraint that touches the cycle.

    "Touches" = at least 2 of the clause's variables are in cycle_vars.
    """
    cycle_set = set(cycle_vars)

    # Find touching constraints
    touching = []
    for clause in clauses:
        clause_vars = set(v for v, _ in clause)
        if len(clause_vars & cycle_set) >= 2:
            touching.append(clause)

    if not touching:
        return 0.0

    S = len(solutions)
    if S < 2:
        return 0.0

    # Determine whether to enumerate or sample
    if S**3 <= mc_budget:
        # Exact enumeration
        violations = 0
        total = S * S * S
        for a in solutions:
            for b in solutions:
                for c in solutions:
                    m = majority(a, b, c)
                    if not all(eval_clause(m, cl) for cl in touching):
                        violations += 1
        return violations / total
    else:
        # Monte Carlo
        violations = 0
        for _ in range(mc_budget):
            a = random.choice(solutions)
            b = random.choice(solutions)
            c = random.choice(solutions)
            m = majority(a, b, c)
            if not all(eval_clause(m, cl) for cl in touching):
                violations += 1
        return violations / mc_budget


def compute_H_global(clauses, solutions, sol_set, mc_budget=MC_TRIPLES):
    """Global holonomy defect = fraction of triples where maj is NOT a solution."""
    S = len(solutions)
    if S < 2:
        return 0.0

    if S**3 <= mc_budget:
        violations = 0
        total = S**3
        for a in solutions:
            for b in solutions:
                for c in solutions:
                    m = majority(a, b, c)
                    if m not in sol_set:
                        violations += 1
        return violations / total
    else:
        violations = 0
        for _ in range(mc_budget):
            a = random.choice(solutions)
            b = random.choice(solutions)
            c = random.choice(solutions)
            m = majority(a, b, c)
            if m not in sol_set:
                violations += 1
        return violations / mc_budget


# ============================================================
# 8. String tension extraction
# ============================================================

def extract_string_tension(H_values, areas):
    """Fit H = sigma * Area + offset using linear regression.
    Returns sigma (slope), R2, and fit details.
    """
    H = np.array(H_values, dtype=float)
    A = np.array(areas, dtype=float)

    mask = np.isfinite(H) & np.isfinite(A) & (A > 0)
    if mask.sum() < 2:
        return 0.0, 0.0, {}

    slope, intercept, r, p, se = linregress(A[mask], H[mask])
    sigma = max(slope, 0.0)
    R2 = r**2

    return sigma, R2, {
        'slope': slope, 'intercept': intercept, 'R2': R2,
        'p_value': p, 'se': se,
        'H': H[mask].tolist(), 'A': A[mask].tolist(),
    }


def extract_perimeter_tension(H_values, lengths):
    """Fit H = sigma_p * L + offset (perimeter law control)."""
    H = np.array(H_values, dtype=float)
    L = np.array(lengths, dtype=float)
    mask = np.isfinite(H) & np.isfinite(L)
    if mask.sum() < 2:
        return 0.0, 0.0
    slope, intercept, r, p, se = linregress(L[mask], H[mask])
    return max(slope, 0.0), r**2


# ============================================================
# 9. Finite-size scaling
# ============================================================

def fit_sigma_convergence(n_vals, sigma_vals):
    """Fit sigma(n) to determine sigma_inf.
    Model A: sigma = sigma_inf + c/n^2         (YM finite-size correction)
    Model B: sigma = a * n^(-alpha)             (power-law to zero)
    Model C: sigma = sigma_inf + c/n^beta       (general)
    """
    n = np.array(n_vals, dtype=float)
    s = np.array(sigma_vals, dtype=float)
    mask = s > 1e-10
    if mask.sum() < 3:
        return {'status': 'insufficient_data', 'sigma_inf_best': 0.0}

    n_f, s_f = n[mask], s[mask]
    ss_tot = np.sum((s_f - s_f.mean())**2)
    results = {}

    # Model A: sigma_inf + c/n^2
    try:
        def mA(x, si, c): return si + c / x**2
        popt, pcov = curve_fit(mA, n_f, s_f, p0=[0.0005, 0.3],
                               bounds=([-0.01, -100], [0.1, 100]))
        pred = mA(n_f, *popt)
        R2 = 1 - np.sum((s_f - pred)**2) / ss_tot if ss_tot > 0 else 0
        results['model_A'] = {
            'sigma_inf': float(popt[0]), 'c': float(popt[1]),
            'R2': float(R2),
            'sigma_inf_se': float(np.sqrt(pcov[0, 0])) if pcov[0, 0] > 0 else 0,
        }
    except Exception as e:
        results['model_A'] = {'error': str(e)}

    # Model B: a * n^(-alpha)
    try:
        def mB(x, a, alpha): return a * x**(-alpha)
        popt, pcov = curve_fit(mB, n_f, s_f, p0=[0.5, 1.5],
                               bounds=([1e-6, 0.01], [1e4, 10]))
        pred = mB(n_f, *popt)
        R2 = 1 - np.sum((s_f - pred)**2) / ss_tot if ss_tot > 0 else 0
        results['model_B'] = {
            'a': float(popt[0]), 'alpha': float(popt[1]),
            'R2': float(R2),
            'sigma_inf': 0.0,  # power law -> 0
        }
    except Exception as e:
        results['model_B'] = {'error': str(e)}

    # Model C: sigma_inf + c/n^beta
    try:
        def mC(x, si, c, beta): return si + c / x**beta
        popt, pcov = curve_fit(mC, n_f, s_f, p0=[0.0003, 0.5, 2.0],
                               bounds=([-0.01, -1e3, 0.1], [0.1, 1e3, 10]),
                               maxfev=20000)
        pred = mC(n_f, *popt)
        R2 = 1 - np.sum((s_f - pred)**2) / ss_tot if ss_tot > 0 else 0
        results['model_C'] = {
            'sigma_inf': float(popt[0]), 'c': float(popt[1]),
            'beta': float(popt[2]), 'R2': float(R2),
            'sigma_inf_se': float(np.sqrt(pcov[0, 0])) if pcov[0, 0] > 0 else 0,
        }
    except Exception as e:
        results['model_C'] = {'error': str(e)}

    # Pick best
    best, best_R2 = None, -1
    for k in ['model_A', 'model_B', 'model_C']:
        if k in results and 'R2' in results[k] and results[k]['R2'] > best_R2:
            best_R2 = results[k]['R2']
            best = k

    sigma_inf = 0.0
    if best and 'sigma_inf' in results[best]:
        sigma_inf = results[best]['sigma_inf']

    results['best_model'] = best
    results['best_R2'] = best_R2
    results['sigma_inf_best'] = sigma_inf
    results['status'] = 'ok'
    return results


# ============================================================
# 10. Main computation loop
# ============================================================

def run_one_type(sat_label, n_values, gen_func):
    """Run area law computation for one SAT type across all n."""
    print(f"\n{'='*78}")
    print(f"  {sat_label}: Area Law / String Tension")
    print(f"{'='*78}")

    all_results = {}

    for n in n_values:
        t0 = time.time()
        print(f"\n  --- n = {n} ---")

        sigmas, H_profiles = [], []

        for inst in range(NUM_INSTANCES):
            sys.stdout.write(f"    [{inst+1}/{NUM_INSTANCES}] ")
            sys.stdout.flush()

            clauses, sols = gen_func(n)
            if clauses is None:
                print("FAIL(gen)")
                continue

            solutions = get_solutions(n, clauses, sols, target=1500)
            if not solutions or len(solutions) < 3:
                print(f"|Sol|={len(solutions) if solutions else 0} skip")
                continue

            sol_set = set(solutions)
            adj, var_clauses = build_constraint_graph(n, clauses)

            # Global holonomy defect (for reference)
            H_global = compute_H_global(clauses, solutions, sol_set, mc_budget=5000)

            # Restricted holonomy for each cycle length
            H_by_L = {}
            for L in CYCLE_LENGTHS:
                cycles = find_cycles(adj, n, L, max_cycles=25)
                if not cycles:
                    continue
                H_vals = []
                for cyc in cycles:
                    H = compute_H_restricted(cyc, clauses, solutions, sol_set)
                    H_vals.append(H)
                H_by_L[L] = np.mean(H_vals)

            if len(H_by_L) < 3:
                print(f"|Sol|={len(solutions)} cycles<3")
                continue

            # Extract string tension: H_restricted vs Area (A5-calibrated areas)
            lengths_used = sorted(H_by_L.keys())
            H_vals = [H_by_L[l] for l in lengths_used]
            areas = [AREA_TABLE.get(l, l * (l - 1) / 6.0) for l in lengths_used]

            sigma, R2, details = extract_string_tension(H_vals, areas)
            sigma_p, R2_p = extract_perimeter_tension(H_vals, lengths_used)

            sigmas.append(sigma)
            H_profiles.append({
                'H_by_L': {int(k): float(v) for k, v in H_by_L.items()},
                'sigma': float(sigma),
                'R2_area': float(R2),
                'R2_perim': float(R2_p),
                'H_global': float(H_global),
                'num_sol': len(solutions),
            })

            print(f"|Sol|={len(solutions):5d} H_glob={H_global:.4f} "
                  f"sigma={sigma:.6f} R2a={R2:.3f} R2p={R2_p:.3f}")

        # Aggregate
        if sigmas:
            sm, ss, smed = np.mean(sigmas), np.std(sigmas), np.median(sigmas)
            # Aggregate H profile
            agg_H = defaultdict(list)
            for p in H_profiles:
                for L, h in p['H_by_L'].items():
                    agg_H[L].append(h)
            avg_H = {L: float(np.mean(v)) for L, v in agg_H.items()}

            all_results[n] = {
                'sigma_mean': float(sm), 'sigma_std': float(ss),
                'sigma_median': float(smed),
                'num_instances': len(sigmas),
                'avg_H_by_L': avg_H,
                'instance_data': H_profiles,
            }
            dt = time.time() - t0
            print(f"\n  n={n}: sigma = {sm:.6f} +/- {ss:.6f} "
                  f"(med {smed:.6f}), {len(sigmas)} inst, {dt:.1f}s")
        else:
            all_results[n] = {
                'sigma_mean': 0.0, 'sigma_std': 0.0,
                'num_instances': 0, 'avg_H_by_L': {},
            }
            print(f"\n  n={n}: NO valid instances")

    return all_results


# ============================================================
# 11. Main
# ============================================================

def main():
    print("=" * 78)
    print("  AREA LAW STRING TENSION -- LARGE-n COMPUTATION")
    print("  Sub-gap E-1: sigma(L, n) -> sigma_inf > 0 ?")
    print("=" * 78)
    print(f"  pysat: {PYSAT_AVAILABLE}")
    print(f"  n: {N_VALUES}  |  instances/n: {NUM_INSTANCES}")
    print(f"  cycle lengths: {CYCLE_LENGTHS}")
    print(f"  MC triples: {MC_TRIPLES}")
    print(f"  alpha(3-SAT)={ALPHA_3SAT}, alpha(2-SAT)={ALPHA_2SAT}, alpha(Horn)={ALPHA_HORN}")
    print(f"  area calibration (from A5): {AREA_TABLE}")

    # ---- 3-SAT ----
    print("\n\n" + "#" * 78)
    print("  3-SAT (NPC) -- expected sigma > 0")
    print("#" * 78)
    r3 = run_one_type("3-SAT", N_VALUES,
                      lambda n: generate_ksat_instance(n, 3, ALPHA_3SAT, min_solutions=4))

    # ---- 2-SAT control ----
    print("\n\n" + "#" * 78)
    print("  2-SAT (P-time) -- expected sigma = 0")
    print("#" * 78)
    r2 = run_one_type("2-SAT", N_VALUES,
                      lambda n: generate_ksat_instance(n, 2, ALPHA_2SAT, min_solutions=8))

    # ---- Horn-SAT control ----
    print("\n\n" + "#" * 78)
    print("  Horn-SAT (P-time) -- expected sigma = 0")
    print("#" * 78)
    rh = run_one_type("Horn-SAT", N_VALUES,
                      lambda n: generate_horn_instance(n, ALPHA_HORN, min_solutions=8))

    # ============================================================
    # 12. Convergence analysis for 3-SAT (including prior data)
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  CONVERGENCE ANALYSIS")
    print("=" * 78)

    prior = {12: 0.00170}   # A5 prior (n=12 only; n=14 will come from new data)
    all_n, all_sigma = [], []
    for n in sorted(set(list(prior.keys()) + N_VALUES)):
        if n in prior and n not in r3:
            all_n.append(n); all_sigma.append(prior[n])
        elif n in r3 and r3[n]['num_instances'] > 0:
            all_n.append(n); all_sigma.append(r3[n]['sigma_mean'])
        elif n in prior:
            all_n.append(n); all_sigma.append(prior[n])

    print(f"\n  3-SAT sigma(n) data:")
    print(f"  {'n':>4}  {'sigma':>12}  source")
    for n, s in zip(all_n, all_sigma):
        src = "prior(A5)" if n in prior and n not in N_VALUES else "new"
        if n in prior and n in N_VALUES:
            src = f"new (prior was {prior[n]:.5f})"
        print(f"  {n:4d}  {s:12.6f}  {src}")

    conv = {}
    if len([s for s in all_sigma if s > 1e-10]) >= 3:
        conv = fit_sigma_convergence(all_n, all_sigma)
        print(f"\n  Model fits:")
        for mk in ['model_A', 'model_B', 'model_C']:
            if mk in conv and 'error' not in conv[mk]:
                m = conv[mk]
                parts = [f"{k}={v:.6f}" if isinstance(v, float) else f"{k}={v}"
                         for k, v in m.items()]
                print(f"    {mk}: {', '.join(parts)}")
            elif mk in conv:
                print(f"    {mk}: ERROR -- {conv[mk].get('error','?')}")

        print(f"\n  Best model: {conv.get('best_model')}")
        print(f"  Best R2: {conv.get('best_R2', 0):.6f}")
        print(f"  sigma_inf: {conv.get('sigma_inf_best', 0):.8f}")
    else:
        print("  Insufficient nonzero points for convergence fit")

    # ============================================================
    # 13. Summary
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  SUMMARY TABLE")
    print("=" * 78)
    hdr = f"  {'Type':>10} {'n':>4} {'sigma':>10} {'std':>10} {'R2a':>6} {'R2p':>6} {'#':>3}"
    print(hdr)
    print("  " + "-" * len(hdr.strip()))

    for label, res in [("3-SAT", r3), ("2-SAT", r2), ("Horn-SAT", rh)]:
        for n in N_VALUES:
            if n in res and res[n]['num_instances'] > 0:
                r = res[n]
                r2as = [d['R2_area'] for d in r.get('instance_data', []) if 'R2_area' in d]
                r2ps = [d['R2_perim'] for d in r.get('instance_data', []) if 'R2_perim' in d]
                print(f"  {label:>10} {n:4d} {r['sigma_mean']:10.6f} "
                      f"{r['sigma_std']:10.6f} {np.mean(r2as) if r2as else 0:6.3f} "
                      f"{np.mean(r2ps) if r2ps else 0:6.3f} {r['num_instances']:3d}")
            else:
                print(f"  {label:>10} {n:4d} {'---':>10} {'---':>10} {'---':>6} {'---':>6} {'0':>3}")

    # ============================================================
    # 14. H(L) profiles for 3-SAT
    # ============================================================
    print("\n\n  H_restricted(L) profile for 3-SAT:")
    hdr2 = f"  {'n':>4}"
    for L in CYCLE_LENGTHS:
        hdr2 += f" {'L='+str(L):>9}"
    print(hdr2)
    for n in N_VALUES:
        if n in r3 and r3[n]['num_instances'] > 0:
            row = f"  {n:4d}"
            for L in CYCLE_LENGTHS:
                h = r3[n]['avg_H_by_L'].get(L, None)
                row += f" {h:9.5f}" if h is not None else f" {'---':>9}"
            print(row)

    # ============================================================
    # 15. Ratio analysis
    # ============================================================
    print("\n\n  Successive ratios sigma(n+delta)/sigma(n):")
    for i in range(len(all_n) - 1):
        n1, n2 = all_n[i], all_n[i + 1]
        s1, s2 = all_sigma[i], all_sigma[i + 1]
        if s1 > 1e-10:
            print(f"    sigma({n2})/sigma({n1}) = {s2/s1:.4f}")

    # ============================================================
    # 16. VERDICT
    # ============================================================
    print("\n\n" + "=" * 78)
    print("  VERDICT on Sub-gap E-1")
    print("=" * 78)

    # Control check
    ctrl_ok = True
    for label, res in [("2-SAT", r2), ("Horn-SAT", rh)]:
        for n in N_VALUES:
            if n in res and res[n]['num_instances'] > 0:
                if res[n]['sigma_mean'] > 0.0005:
                    ctrl_ok = False
                    print(f"  WARNING: {label} n={n} sigma={res[n]['sigma_mean']:.6f} > 0")

    print(f"  P-time controls (sigma=0): {'PASS' if ctrl_ok else 'FAIL'}")

    sigma_inf = conv.get('sigma_inf_best', 0)
    sigma_last = all_sigma[-1] if all_sigma else 0

    if len(all_sigma) >= 3 and sigma_last > 0 and sigma_inf > 0 and ctrl_ok:
        verdict = "SUPPORTED"
        print(f"\n  *** SUB-GAP E-1: SUPPORTED ***")
        print(f"  sigma_inf = {sigma_inf:.6f} > 0")
        print(f"  sigma remains positive through n={all_n[-1]}")
        print(f"  Correlation length bound: xi <= {1/(2*sigma_inf):.0f}")
    elif sigma_last > 0 and ctrl_ok:
        verdict = "PLAUSIBLE"
        print(f"\n  *** SUB-GAP E-1: PLAUSIBLE ***")
        print(f"  sigma positive at all tested n, but fit inconclusive")
    else:
        verdict = "NOT_SUPPORTED"
        print(f"\n  *** SUB-GAP E-1: NOT SUPPORTED ***")

    # ============================================================
    # 17. Save JSON
    # ============================================================
    output = {
        'metadata': {
            'node': '2.4-E1-string-tension', 'date': '2026-04-11',
            'alpha_3sat': ALPHA_3SAT, 'alpha_2sat': ALPHA_2SAT,
            'alpha_horn': ALPHA_HORN, 'num_instances': NUM_INSTANCES,
            'mc_triples': MC_TRIPLES, 'area_table': AREA_TABLE,
        },
        '3sat': {}, '2sat': {}, 'horn': {},
        'convergence': conv if conv else {},
        'verdict': verdict,
        'all_n': all_n, 'all_sigma': all_sigma,
    }
    for key, res in [('3sat', r3), ('2sat', r2), ('horn', rh)]:
        for n in N_VALUES:
            if n in res:
                r = res[n]
                output[key][str(n)] = {
                    'sigma_mean': float(r['sigma_mean']),
                    'sigma_std': float(r['sigma_std']),
                    'sigma_median': float(r.get('sigma_median', 0)),
                    'num_instances': int(r['num_instances']),
                    'avg_H_by_L': {str(k): float(v)
                                   for k, v in r.get('avg_H_by_L', {}).items()},
                }

    outpath = '/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/' \
              'clone-growth-fullness-bridge/code/area_law_large_n_results.json'
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\n  Results: {outpath}")

    return output


if __name__ == "__main__":
    main()
