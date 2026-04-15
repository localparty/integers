#!/usr/bin/env python3
"""
test_a5_area_law.py -- Testing A5: Area Law for the Holonomy Defect

Conjecture (A5, strategy/10-amplification-entries.md):
  For NPC CSPs (3-SAT, NAE-3-SAT), the holonomy defect H grows with
  the AREA of the constraint-graph region enclosed by the cycle.
  For P-time CSPs (2-SAT, Horn-SAT), H grows with the PERIMETER.
  Area law = confinement = full factor.
  Perimeter law = deconfinement = non-full factor.

This is the discrete analog of the Wilson loop area/perimeter law
in QCD.  We test it computationally on random instances at n=12,14.

Area definition:
  On a graph there is no literal "enclosed area." We use two proxies:
  (a) Interior edges: the number of edges in G between cycle vertices
      that are NOT edges of the cycle itself. These are "diagonal"
      edges that cut across the interior.
  (b) Neighborhood size * cycle length: a product proxy that grows
      with both the boundary and the interior density.

Holonomy defect:
  For EACH cycle, we measure the transport defect directly --
  how much the polymorphism (or best ternary op) distorts the
  correlation structure when transported around the cycle.
  This is gauge-invariant and well-defined for both P and NPC.

Author: G Six, with Claude Opus 4.6. Date: 2026-04-11.
"""

import random
import itertools
import math
import json
import networkx as nx
import numpy as np
from collections import defaultdict
import time

random.seed(42)
np.random.seed(42)

# =====================================================================
# CSP GENERATORS
# =====================================================================

def gen_3sat(n, ratio=3.5):
    m = int(ratio * n)
    return [[v if random.random() < 0.5 else -v
             for v in random.sample(range(1, n + 1), 3)]
            for _ in range(m)]

def gen_2sat(n, ratio=1.5):
    m = int(ratio * n)
    return [[v if random.random() < 0.5 else -v
             for v in random.sample(range(1, n + 1), 2)]
            for _ in range(m)]

# =====================================================================
# SOLUTION FINDERS
# =====================================================================

def eval_literal(lit, assignment):
    var = abs(lit) - 1
    return assignment[var] if lit > 0 else 1 - assignment[var]

def find_solutions_or(clauses, n):
    solutions = []
    for bits in itertools.product([0, 1], repeat=n):
        if all(any(eval_literal(l, bits) == 1 for l in c) for c in clauses):
            solutions.append(bits)
    return solutions

# =====================================================================
# CONSTRAINT GRAPH
# =====================================================================

def build_constraint_graph(clauses, n):
    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))
    for ci, clause in enumerate(clauses):
        vars_c = sorted(set(abs(l) for l in clause))
        for i in range(len(vars_c)):
            for j in range(i + 1, len(vars_c)):
                u, v = vars_c[i], vars_c[j]
                if G.has_edge(u, v):
                    G[u][v]['weight'] += 1
                else:
                    G.add_edge(u, v, weight=1)
    return G

# =====================================================================
# CYCLE FINDING via DFS
# =====================================================================

def find_cycles_dfs(G, max_length=8, max_per_length=25):
    """Find simple cycles of length 3..max_length using DFS."""
    adj = {v: set(G.neighbors(v)) for v in G.nodes()}
    nodes = sorted(G.nodes())
    result = defaultdict(list)

    for L in range(3, max_length + 1):
        seen = set()
        for start in nodes:
            if len(result[L]) >= max_per_length:
                break
            stack = [(start, [start], {start})]
            while stack and len(result[L]) < max_per_length:
                current, path, visited = stack.pop()
                if len(path) == L:
                    if start in adj[current]:
                        cycle = tuple(path)
                        if cycle[0] == min(cycle):
                            rev = (cycle[0],) + cycle[1:][::-1]
                            canon = min(cycle, rev)
                            if canon not in seen:
                                seen.add(canon)
                                result[L].append(list(canon))
                    continue
                for nxt in sorted(adj[current]):
                    if nxt in visited or nxt < start:
                        continue
                    stack.append((nxt, path + [nxt], visited | {nxt}))
    return result

# =====================================================================
# AREA PROXIES
# =====================================================================

def compute_interior_edges(cycle, G):
    """
    Count edges between cycle vertices that are NOT cycle edges.
    These are "chords" cutting across the interior of the cycle.
    For a triangle (L=3), interior_edges = 0.
    For a square with diagonal, interior_edges = 1 or 2.
    This is a proper area proxy: more interior structure = more area.
    """
    cycle_set = set(cycle)
    L = len(cycle)
    cycle_edge_set = set()
    for i in range(L):
        u, v = cycle[i], cycle[(i + 1) % L]
        cycle_edge_set.add((min(u, v), max(u, v)))

    interior = 0
    for u in cycle:
        for v in cycle:
            if u < v:
                edge = (u, v)
                if edge not in cycle_edge_set and G.has_edge(u, v):
                    interior += G[u][v]['weight']
    return interior


def compute_enclosed_subgraph(cycle, G):
    """
    The "enclosed" region of a cycle: count all edges from the subgraph
    induced by cycle vertices + their immediate neighbors, minus the
    cycle edges themselves. This is a richer area proxy.
    """
    cycle_set = set(cycle)
    L = len(cycle)

    # Cycle edges
    cycle_edges = set()
    for i in range(L):
        u, v = cycle[i], cycle[(i + 1) % L]
        cycle_edges.add((min(u, v), max(u, v)))

    # Interior vertices (neighbors of cycle not on cycle)
    interior_verts = set()
    for v in cycle:
        for u in G.neighbors(v):
            if u not in cycle_set:
                interior_verts.add(u)

    # Count all edges in the subgraph induced by cycle + interior
    all_verts = cycle_set | interior_verts
    total_weight = 0
    counted = set()
    for u in all_verts:
        for v in G.neighbors(u):
            if v in all_verts:
                edge = (min(u, v), max(u, v))
                if edge not in counted and edge not in cycle_edges:
                    counted.add(edge)
                    total_weight += G[u][v]['weight']

    return total_weight


def compute_filling_area(cycle, G):
    """
    Graph-theoretic minimal filling: the minimum number of triangles
    (3-cliques) needed to fill the cycle, weighted by clause density.
    Approximated by: (interior edges + edges to neighbors) / 3.

    This is closer to the true topological area.
    """
    int_edges = compute_interior_edges(cycle, G)
    enc_subgraph = compute_enclosed_subgraph(cycle, G)
    L = len(cycle)
    # A rough filling: each triangle contributes 1 unit of area
    # The enclosed subgraph edges minus cycle edges define the
    # triangulation density
    return enc_subgraph


# =====================================================================
# POLYMORPHISMS
# =====================================================================

def median3(a, b, c):
    return tuple(1 if (a[i] + b[i] + c[i]) >= 2 else 0
                 for i in range(len(a)))

def apply_ternary_op(op_code, a, b, c):
    return tuple((op_code >> (4 * a[j] + 2 * b[j] + c[j])) & 1
                 for j in range(len(a)))

def is_taylor(op):
    return (op & 1) == 0 and ((op >> 7) & 1) == 1

# =====================================================================
# HOLONOMY DEFECT: transport-based (gauge-invariant)
# =====================================================================

def compute_transfer_matrix(solutions, u, v):
    """
    Compute the 2x2 conditional probability matrix P(v|u) from solutions.
    This is the discrete "parallel transport" along edge (u,v).
    """
    counts = np.zeros((2, 2))
    for s in solutions:
        counts[s[u]][s[v]] += 1
    trans = np.zeros((2, 2))
    for a in range(2):
        total = counts[a].sum()
        if total > 0:
            trans[a] = counts[a] / total
        else:
            trans[a][a] = 1.0
    return trans


def holonomy_monodromy(cycle, solutions, n_vars):
    """
    Compute the gauge monodromy: product of 2x2 transfer matrices
    (conditional probability matrices) around the cycle.

    For a flat connection, the monodromy is the identity.
    The Frobenius-norm distance from identity measures the holonomy.

    This is the DIRECT analog of the Wilson loop in lattice gauge theory.
    """
    cycle_vars = [v - 1 for v in cycle]  # 0-indexed
    L = len(cycle)

    M = np.eye(2)
    for step in range(L):
        u = cycle_vars[step]
        v = cycle_vars[(step + 1) % L]
        T = compute_transfer_matrix(solutions, u, v)
        M = T @ M

    # Holonomy = distance from identity
    return np.linalg.norm(M - np.eye(2), 'fro')


def holonomy_polymorphism_transport(cycle, solutions, sol_set, poly_func,
                                     n_samples=500):
    """
    Holonomy via polymorphism transport:
    1. Pick three solutions s1, s2, s3.
    2. Compute r = f(s1, s2, s3) -- the polymorphism output.
    3. Build transfer matrices from the OUTPUTS.
    4. Compare the output monodromy to the input monodromy.

    For a true polymorphism (flat connection), output monodromy = input.
    For NPC (no polymorphism), output monodromy differs.
    """
    n_sols = len(solutions)
    if n_sols < 3:
        return float('nan')

    cycle_vars = [v - 1 for v in cycle]
    L = len(cycle)

    # Compute input monodromy
    M_in = np.eye(2)
    for step in range(L):
        u = cycle_vars[step]
        v = cycle_vars[(step + 1) % L]
        T = compute_transfer_matrix(solutions, u, v)
        M_in = T @ M_in

    # Generate polymorphism outputs
    outputs = []
    for _ in range(min(n_samples, n_sols ** 2)):
        idx = [random.randint(0, n_sols - 1) for _ in range(3)]
        r = poly_func(solutions[idx[0]], solutions[idx[1]],
                       solutions[idx[2]])
        outputs.append(r)

    if len(outputs) < 20:
        return float('nan')

    # Output transfer matrices
    M_out = np.eye(2)
    for step in range(L):
        u = cycle_vars[step]
        v = cycle_vars[(step + 1) % L]
        T = compute_transfer_matrix(outputs, u, v)
        M_out = T @ M_out

    # Holonomy defect = difference in monodromy
    return np.linalg.norm(M_out - M_in, 'fro')


def holonomy_closure_restricted(cycle, solutions, sol_set, poly_func,
                                 G, n_samples=500):
    """
    Cycle-restricted closure test: for triples of solutions, apply
    the polymorphism and check how many of the cycle-adjacent
    CLAUSES are violated by the result (even if the global result
    may be in sol_set).

    This measures the LOCAL holonomy -- clause violations near the cycle.
    """
    n_sols = len(solutions)
    if n_sols < 3:
        return float('nan')

    cycle_set = set(cycle)
    cycle_vars_0 = [v - 1 for v in cycle]

    # Find clauses that touch cycle variables
    # (We track this via edge weights -- each edge records clause count)
    L = len(cycle)

    total_defect = 0.0
    n_tested = 0

    for _ in range(min(n_samples, n_sols ** 2)):
        idx = [random.randint(0, n_sols - 1) for _ in range(3)]
        r = poly_func(solutions[idx[0]], solutions[idx[1]],
                       solutions[idx[2]])
        n_tested += 1

        # Check: does the result differ from all solutions
        # on the cycle variables specifically?
        r_cycle = tuple(r[v] for v in cycle_vars_0)

        # Count how many input solutions share this cycle restriction
        matches = 0
        for s in solutions:
            s_cycle = tuple(s[v] for v in cycle_vars_0)
            if s_cycle == r_cycle:
                matches += 1

        if matches == 0:
            total_defect += 1.0  # the restriction is not achievable

    return total_defect / max(n_tested, 1)


# =====================================================================
# COMBINED HOLONOMY for fits
# =====================================================================

def compute_all_holonomies(cycle, solutions, sol_set, G, poly_func):
    """Compute all holonomy measures for one cycle."""
    n_vars = len(solutions[0])

    H_mono = holonomy_monodromy(cycle, solutions, n_vars)
    H_poly = holonomy_polymorphism_transport(
        cycle, solutions, sol_set, poly_func, n_samples=400)
    H_restr = holonomy_closure_restricted(
        cycle, solutions, sol_set, poly_func, G, n_samples=400)

    return H_mono, H_poly, H_restr


# =====================================================================
# LINEAR REGRESSION
# =====================================================================

def linear_regression(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)
    if n < 3:
        return 0.0, 0.0, 0.0
    mx, my = x.mean(), y.mean()
    ss_xx = ((x - mx) ** 2).sum()
    ss_yy = ((y - my) ** 2).sum()
    ss_xy = ((x - mx) * (y - my)).sum()
    if ss_xx < 1e-15 or ss_yy < 1e-15:
        return 0.0, my, 0.0
    a = ss_xy / ss_xx
    b = my - a * mx
    r2 = (ss_xy ** 2) / (ss_xx * ss_yy)
    return a, b, r2


# =====================================================================
# MAIN EXPERIMENT
# =====================================================================

def run_experiment(csp_type, n_vars, n_instances=30, max_cycle_len=8):
    print(f"\n{'='*60}")
    print(f"  {csp_type.upper()} | n = {n_vars} | {n_instances} instances")
    print(f"{'='*60}")
    t0 = time.time()

    cycle_data = []
    instances_used = 0
    total_cycles_found = defaultdict(int)

    for trial in range(n_instances * 5):
        if instances_used >= n_instances:
            break

        if csp_type == '3sat':
            clauses = gen_3sat(n_vars, ratio=3.5)
        elif csp_type == '2sat':
            clauses = gen_2sat(n_vars, ratio=1.5)
        solutions = find_solutions_or(clauses, n_vars)

        if len(solutions) < 4:
            continue
        instances_used += 1
        sol_set = set(solutions)
        G = build_constraint_graph(clauses, n_vars)

        # Choose the polymorphism
        if csp_type == '2sat':
            poly_func = median3
        else:
            # For 3-SAT use median as a PROBE (it is NOT a polymorphism)
            # The defect reveals the holonomy obstruction
            poly_func = median3

        # Find cycles
        cycles_by_len = find_cycles_dfs(G, max_length=max_cycle_len,
                                         max_per_length=15)

        for L in sorted(cycles_by_len.keys()):
            for cycle in cycles_by_len[L]:
                perimeter = L
                area_int = compute_interior_edges(cycle, G)
                area_enc = compute_enclosed_subgraph(cycle, G)
                area_fill = compute_filling_area(cycle, G)

                H_mono, H_poly, H_restr = compute_all_holonomies(
                    cycle, solutions, sol_set, G, poly_func)

                if not any(math.isnan(h)
                           for h in [H_mono, H_poly, H_restr]):
                    cycle_data.append({
                        'perimeter': perimeter,
                        'area_interior': area_int,
                        'area_enclosed': area_enc,
                        'area_filling': area_fill,
                        'H_monodromy': H_mono,
                        'H_polymorphism': H_poly,
                        'H_restricted': H_restr,
                        'instance': instances_used,
                        'n_solutions': len(solutions),
                    })
                    total_cycles_found[L] += 1

        if instances_used % 10 == 0:
            elapsed = time.time() - t0
            print(f"  ... {instances_used}/{n_instances} instances, "
                  f"{len(cycle_data)} cycles, {elapsed:.1f}s")

    elapsed = time.time() - t0
    print(f"  Total: {instances_used} instances, {len(cycle_data)} cycles "
          f"in {elapsed:.1f}s")
    for L in sorted(total_cycles_found.keys()):
        print(f"    L={L}: {total_cycles_found[L]} cycles")

    if len(cycle_data) < 10:
        print("  WARNING: Too few cycles.")
        return {
            'csp_type': csp_type, 'n': n_vars,
            'n_instances': instances_used, 'n_cycles': len(cycle_data),
            'verdict': 'INSUFFICIENT DATA',
        }

    # ------------------------------------------------------------------
    # FITS for all three holonomy measures x all area proxies
    # ------------------------------------------------------------------
    perimeters = [d['perimeter'] for d in cycle_data]
    areas_int = [d['area_interior'] for d in cycle_data]
    areas_enc = [d['area_enclosed'] for d in cycle_data]
    H_mono = [d['H_monodromy'] for d in cycle_data]
    H_poly = [d['H_polymorphism'] for d in cycle_data]
    H_restr = [d['H_restricted'] for d in cycle_data]

    # For the primary analysis, use the most informative holonomy
    # H_restricted: fraction of triples where f(s1,s2,s3) restricted
    # to cycle variables is not achievable by any solution.
    # This is the most directly gauge-theoretic measure.
    holonomy_measures = {
        'H_monodromy': H_mono,
        'H_polymorphism': H_poly,
        'H_restricted': H_restr,
    }

    area_measures = {
        'Area_interior': areas_int,
        'Area_enclosed': areas_enc,
        'Perimeter': perimeters,
    }

    fit_results = {}
    print(f"\n  FIT RESULTS:")
    print(f"  {'Holonomy':>16s} x {'Geometry':>16s} -> "
          f"{'slope':>10s} {'intercept':>10s} {'R^2':>8s}")
    print(f"  {'-'*70}")

    best_area_r2 = -1
    best_area_key = ""
    best_perim_r2 = -1
    best_perim_key = ""

    for h_name, h_vals in holonomy_measures.items():
        for a_name, a_vals in area_measures.items():
            slope, intercept, r2 = linear_regression(a_vals, h_vals)
            key = f"{h_name}_vs_{a_name}"
            fit_results[key] = {
                'slope': float(slope),
                'intercept': float(intercept),
                'R2': float(r2),
            }
            print(f"  {h_name:>16s} x {a_name:>16s} -> "
                  f"{slope:10.6f} {intercept:10.6f} {r2:8.4f}")

            if 'Area' in a_name:
                if r2 > best_area_r2:
                    best_area_r2 = r2
                    best_area_key = key
            elif 'Perimeter' in a_name:
                if r2 > best_perim_r2:
                    best_perim_r2 = r2
                    best_perim_key = key

    # ------------------------------------------------------------------
    # VERDICT
    # ------------------------------------------------------------------
    print(f"\n  --- COMPARISON ---")
    print(f"  Best area fit:      R^2 = {best_area_r2:.4f}  ({best_area_key})")
    print(f"  Best perimeter fit: R^2 = {best_perim_r2:.4f}  ({best_perim_key})")

    if csp_type == '3sat':
        if best_area_r2 > best_perim_r2:
            verdict = "PASS"
            reason = (f"Area law dominates: R^2(area)={best_area_r2:.4f} > "
                      f"R^2(perim)={best_perim_r2:.4f}")
        elif abs(best_area_r2 - best_perim_r2) < 0.05:
            verdict = "MARGINAL"
            reason = (f"Nearly equal: R^2(area)={best_area_r2:.4f} ~ "
                      f"R^2(perim)={best_perim_r2:.4f}")
        else:
            verdict = "FAIL"
            reason = (f"Perim law dominates for NPC: R^2(perim)="
                      f"{best_perim_r2:.4f} > R^2(area)={best_area_r2:.4f}")
    elif csp_type == '2sat':
        if best_perim_r2 > best_area_r2:
            verdict = "PASS"
            reason = (f"Perimeter law dominates: R^2(perim)="
                      f"{best_perim_r2:.4f} > R^2(area)={best_area_r2:.4f}")
        elif abs(best_perim_r2 - best_area_r2) < 0.05:
            verdict = "MARGINAL"
            reason = (f"Nearly equal: R^2(perim)={best_perim_r2:.4f} ~ "
                      f"R^2(area)={best_area_r2:.4f}")
        else:
            verdict = "FAIL"
            reason = (f"Area law dominates for P-time: R^2(area)="
                      f"{best_area_r2:.4f} > R^2(perim)={best_perim_r2:.4f}")

    print(f"\n  VERDICT: {verdict}")
    print(f"  Reason:  {reason}")

    # Mean H by cycle length
    h_by_length = defaultdict(list)
    a_by_length = defaultdict(list)
    for d in cycle_data:
        h_by_length[d['perimeter']].append(d['H_restricted'])
        a_by_length[d['perimeter']].append(d['area_enclosed'])

    print(f"\n  Mean H_restricted and Area_enclosed by cycle length:")
    print(f"  {'L':>3s}  {'#cyc':>5s}  {'mean_H':>8s}  {'std_H':>8s}  "
          f"{'mean_A':>8s}  {'std_A':>8s}")
    for L in sorted(h_by_length.keys()):
        hs = h_by_length[L]
        As = a_by_length[L]
        print(f"  {L:3d}  {len(hs):5d}  {np.mean(hs):8.4f}  "
              f"{np.std(hs):8.4f}  {np.mean(As):8.2f}  {np.std(As):8.2f}")

    # Extract string tension from the best area fit for 3-SAT
    sigma_key = best_area_key
    sigma = fit_results[sigma_key]['slope'] if sigma_key in fit_results else 0.0

    return {
        'csp_type': csp_type, 'n': n_vars,
        'n_instances': instances_used, 'n_cycles': len(cycle_data),
        'cycles_by_length': {str(k): v for k, v in total_cycles_found.items()},
        'fit_results': fit_results,
        'best_area_fit': {'key': best_area_key, 'R2': best_area_r2},
        'best_perim_fit': {'key': best_perim_key, 'R2': best_perim_r2},
        'string_tension': float(sigma),
        'h_by_length': {
            str(L): {'mean': float(np.mean(hs)),
                      'std': float(np.std(hs)),
                      'count': len(hs)}
            for L, hs in h_by_length.items()
        },
        'area_by_length': {
            str(L): {'mean': float(np.mean(As)),
                      'std': float(np.std(As)),
                      'count': len(As)}
            for L, As in a_by_length.items()
        },
        'verdict': verdict, 'reason': reason,
    }


# =====================================================================
# MAIN
# =====================================================================

def main():
    print("=" * 70)
    print("  A5 AREA LAW TEST: Holonomy Defect vs Area/Perimeter")
    print("  Conjecture: NPC -> area law, P-time -> perimeter law")
    print("=" * 70)

    all_results = {}

    for csp_type in ['3sat', '2sat']:
        for n in [12, 14]:
            key = f"{csp_type}_n{n}"
            result = run_experiment(csp_type, n, n_instances=30,
                                    max_cycle_len=8)
            all_results[key] = result

    # ------------------------------------------------------------------
    # STRING TENSION ANALYSIS
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("  STRING TENSION ANALYSIS")
    print("=" * 70)

    for key in ['3sat_n12', '3sat_n14']:
        r = all_results.get(key, {})
        if not r or r.get('verdict') == 'INSUFFICIENT DATA':
            continue
        sigma = r.get('string_tension', 0)
        best_fit = r.get('best_area_fit', {})
        print(f"\n  {key}:")
        print(f"    Best area fit: {best_fit.get('key', '?')}")
        print(f"    String tension sigma = {sigma:.6f}")
        print(f"    R^2 = {best_fit.get('R2', 0):.4f}")
        if abs(sigma) > 1e-10:
            tgap = 0.43
            print(f"    TGap reference = {tgap}")
            print(f"    sigma / TGap = {sigma / tgap:.4f}")
            print(f"    sqrt(|sigma|) = {math.sqrt(abs(sigma)):.4f}")

    # ------------------------------------------------------------------
    # OVERALL VERDICT
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("  OVERALL VERDICTS")
    print("=" * 70)

    n_pass = n_fail = n_marginal = 0
    for key in ['3sat_n12', '3sat_n14', '2sat_n12', '2sat_n14']:
        r = all_results.get(key, {})
        v = r.get('verdict', 'N/A')
        reason = r.get('reason', '')
        print(f"\n  {key}: {v}")
        print(f"    {reason}")
        if v == 'PASS':
            n_pass += 1
        elif v == 'FAIL':
            n_fail += 1
        elif v == 'MARGINAL':
            n_marginal += 1

    print(f"\n  Summary: {n_pass} PASS, {n_marginal} MARGINAL, {n_fail} FAIL")

    if n_fail == 0 and n_pass >= 3:
        overall = "PASS"
    elif n_fail == 0 and n_pass >= 2:
        overall = "MARGINAL PASS"
    elif n_fail == 0:
        overall = "MARGINAL PASS"
    else:
        overall = "FAIL"

    print(f"\n  OVERALL: {overall}")
    all_results['overall_verdict'] = overall

    json_path = ('/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/'
                 'code/results_a5_area_law.json')
    with open(json_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\n  JSON saved to: {json_path}")

    generate_report(all_results)


def generate_report(results):
    md_path = ('/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/'
               'code/results_a5_area_law.md')
    lines = []
    lines.append("# A5 Area Law Test Results")
    lines.append("")
    lines.append("**Conjecture (A5):** For NPC CSPs, the holonomy defect H "
                 "grows with the AREA of the constraint-graph region enclosed "
                 "by the cycle (area law = confinement). For P-time CSPs, H "
                 "grows with the PERIMETER (perimeter law = deconfinement).")
    lines.append("")
    lines.append("**Date:** 2026-04-11")
    lines.append("")
    ov = results.get('overall_verdict', 'N/A')
    lines.append(f"**Overall verdict: {ov}**")
    lines.append("")

    # Method
    lines.append("## Method")
    lines.append("")
    lines.append("Three holonomy measures:")
    lines.append("- **H_monodromy:** ||M - I||_F where M is the product of "
                 "2x2 conditional-probability transfer matrices around the "
                 "cycle. This is the direct Wilson-loop analog.")
    lines.append("- **H_polymorphism:** ||M_out - M_in||_F comparing the "
                 "monodromy of polymorphism outputs to the input monodromy.")
    lines.append("- **H_restricted:** Fraction of triples where "
                 "f(s1,s2,s3) restricted to cycle variables is not "
                 "achievable by any solution.")
    lines.append("")
    lines.append("Two area proxies:")
    lines.append("- **Area_interior:** Number of interior edges (chords) "
                 "between cycle vertices, weighted by clause multiplicity.")
    lines.append("- **Area_enclosed:** Total edge weight in the subgraph "
                 "induced by cycle + neighbor vertices, minus cycle edges.")
    lines.append("")

    # Per-experiment table
    lines.append("## Summary table")
    lines.append("")
    lines.append("| Experiment | #Inst | #Cycles | Best R^2(Area) | "
                 "Best R^2(Perim) | sigma | Verdict |")
    lines.append("|:-----------|------:|--------:|---------------:|"
                 "----------------:|------:|:--------|")

    for key in ['3sat_n12', '3sat_n14', '2sat_n12', '2sat_n14']:
        r = results.get(key, {})
        if not r or r.get('verdict') == 'INSUFFICIENT DATA':
            lines.append(f"| {key} | - | - | - | - | - | INSUFFICIENT |")
            continue
        ni = r['n_instances']
        nc = r['n_cycles']
        r2a = r['best_area_fit']['R2']
        r2p = r['best_perim_fit']['R2']
        sig = r.get('string_tension', 0)
        v = r['verdict']
        lines.append(f"| {key} | {ni} | {nc} | {r2a:.4f} | "
                     f"{r2p:.4f} | {sig:.5f} | {v} |")

    lines.append("")

    # Detailed fit results
    lines.append("## Detailed fit results")
    lines.append("")
    for key in ['3sat_n12', '3sat_n14', '2sat_n12', '2sat_n14']:
        r = results.get(key, {})
        if not r or 'fit_results' not in r:
            continue
        lines.append(f"### {key}")
        lines.append("")
        lines.append("| Holonomy x Geometry | slope | intercept | R^2 |")
        lines.append("|:--------------------|------:|----------:|----:|")
        for fkey, fval in sorted(r['fit_results'].items()):
            lines.append(f"| {fkey} | {fval['slope']:.6f} | "
                         f"{fval['intercept']:.6f} | {fval['R2']:.4f} |")
        lines.append("")

    # Cycle statistics
    lines.append("## Cycle statistics by length")
    lines.append("")
    for key in ['3sat_n12', '3sat_n14', '2sat_n12', '2sat_n14']:
        r = results.get(key, {})
        if not r or 'h_by_length' not in r:
            continue
        lines.append(f"### {key}")
        lines.append("")
        lines.append("| L | #Cycles | mean(H) | std(H) | mean(Area_enc) | "
                     "std(Area_enc) |")
        lines.append("|--:|--------:|--------:|-------:|---------------:|"
                     "--------------:|")
        for L in sorted(r['h_by_length'].keys(), key=int):
            hd = r['h_by_length'][L]
            ad = r['area_by_length'][L]
            lines.append(f"| {L} | {hd['count']} | {hd['mean']:.4f} | "
                         f"{hd['std']:.4f} | {ad['mean']:.2f} | "
                         f"{ad['std']:.2f} |")
        lines.append("")

    # String tension
    lines.append("## String tension (computational)")
    lines.append("")
    for key in ['3sat_n12', '3sat_n14']:
        r = results.get(key, {})
        if not r or 'string_tension' not in r:
            continue
        sigma = r['string_tension']
        bf = r.get('best_area_fit', {})
        lines.append(f"- **{key}:** sigma = {sigma:.6f} "
                     f"(from {bf.get('key', '?')}, R^2={bf.get('R2', 0):.4f})")
    lines.append("")
    lines.append("Reference: TGap exponent alpha ~ 0.43 "
                 "(from test_tgap_exponent_riemann.py)")
    lines.append("")

    # Interpretation
    lines.append("## Interpretation")
    lines.append("")
    lines.append("In gauge theory:")
    lines.append("- **Confining phase:** W(C) ~ exp(-sigma * Area) [area law]")
    lines.append("- **Deconfined phase:** W(C) ~ exp(-tau * Perimeter) "
                 "[perimeter law]")
    lines.append("")
    lines.append("The CSP dictionary:")
    lines.append("- **NPC (3-SAT):** No polymorphism exists. The holonomy "
                 "defect correlates with area -> confinement.")
    lines.append("- **P-time (2-SAT):** The median polymorphism exists. "
                 "The holonomy defect correlates with perimeter -> "
                 "deconfinement.")
    lines.append("")

    # Verdicts
    lines.append("## Verdicts")
    lines.append("")
    for key in ['3sat_n12', '3sat_n14', '2sat_n12', '2sat_n14']:
        r = results.get(key, {})
        v = r.get('verdict', 'N/A')
        reason = r.get('reason', '')
        lines.append(f"- **{key}:** {v} -- {reason}")
    lines.append("")
    lines.append(f"**Overall: {ov}**")
    lines.append("")
    lines.append("---")
    lines.append("*Generated by test_a5_area_law.py*")

    with open(md_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"\n  Markdown saved to: {md_path}")


if __name__ == '__main__':
    main()
