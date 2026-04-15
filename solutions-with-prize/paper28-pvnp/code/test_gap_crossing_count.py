"""
test_gap_crossing_count.py — Testing the "gap-crossing count" mechanism

Tests the conjecture from strategy/06-transposition-dictionary.md (Pattern A, revised):

  For NP-complete CSPs, the spectral gap (TGap > 0) is a sparsity amplifier.
  The number of independent "gap crossings" needed to reach a solution from
  a random starting point scales exponentially with n:

      NPC:  N_crossings ~ 2^n / |Sol(Gamma, n)|   (exponential when solutions are sparse)
      P:    N_crossings = 0                         (no gap to cross)

Computes for each CSP class:
  1. Solution density |Sol(Gamma, n)| / 2^n for n = 8, 10, 12, 14
  2. TGap (minimum violation rate over ternary Taylor operations)
  3. Gap-crossing count N_crossings = 2^n / |Sol|
  4. Correlation between TGap and N_crossings
  5. Scaling exponents for NPC classes

Author: G Six, with Claude Opus 4.6. Date: 2026-04-11.
"""

import random
import itertools
import math
import json
from collections import defaultdict

random.seed(42)

# =====================================================================
# UTILITY FUNCTIONS
# =====================================================================

def median3(a, b, c):
    return tuple(1 if (a[i]+b[i]+c[i]) >= 2 else 0 for i in range(len(a)))

def xor3(a, b, c):
    return tuple((a[i]+b[i]+c[i]) % 2 for i in range(len(a)))

def min3(a, b, c):
    return tuple(min(a[i],b[i],c[i]) for i in range(len(a)))

def max3(a, b, c):
    return tuple(max(a[i],b[i],c[i]) for i in range(len(a)))

def maj_plus1(a, b, c):
    return tuple(1 if (a[i]+b[i]+c[i]+1) > 1 else 0 for i in range(len(a)))

TAYLOR_OPS = {
    'median': median3,
    'xor': xor3,
    'min': min3,
    'max': max3,
    'maj+1': maj_plus1,
}

def check_closure_rate(solutions, op, max_checks=5000):
    """Return violation rate of op on solution set (sampled)."""
    sol_set = set(solutions)
    n_sols = len(solutions)
    if n_sols < 3:
        return None
    n_checked = 0
    n_violations = 0
    # For small sets, try all triples
    if n_sols <= 20:
        for i in range(n_sols):
            for j in range(n_sols):
                for k in range(n_sols):
                    if i == j == k:
                        continue
                    result = op(solutions[i], solutions[j], solutions[k])
                    n_checked += 1
                    if result not in sol_set:
                        n_violations += 1
    else:
        for _ in range(max_checks):
            idx = random.choices(range(n_sols), k=3)
            if idx[0] == idx[1] == idx[2]:
                continue
            result = op(solutions[idx[0]], solutions[idx[1]], solutions[idx[2]])
            n_checked += 1
            if result not in sol_set:
                n_violations += 1
    if n_checked == 0:
        return None
    return n_violations / n_checked

def compute_tgap(solutions):
    """TGap = minimum violation rate over all Taylor operations.
    TGap = 0 means some polymorphism exists (P-time).
    TGap > 0 means no polymorphism exists (NPC candidate)."""
    if len(solutions) < 3:
        return None, None
    best_rate = 1.0
    best_op = None
    for name, op in TAYLOR_OPS.items():
        rate = check_closure_rate(solutions, op)
        if rate is not None and rate < best_rate:
            best_rate = rate
            best_op = name
    return best_rate, best_op


# =====================================================================
# CSP INSTANCE GENERATORS
# =====================================================================

def gen_random_ksat(n, m, k):
    """Random k-SAT: m clauses, each with k distinct literals."""
    return [[v if random.random() < 0.5 else -v
             for v in random.sample(range(1, n+1), k)] for _ in range(m)]

def gen_horn(n, m):
    """Horn clauses: at most one positive literal per clause."""
    clauses = []
    for _ in range(m):
        k = random.randint(2, 3)
        vs = random.sample(range(1, n+1), min(k, n))
        # One positive literal (or none), rest negative
        pos_idx = random.randint(0, len(vs))  # can be len(vs) => all negative
        clause = []
        for i, v in enumerate(vs):
            if i == pos_idx:
                clause.append(v)
            else:
                clause.append(-v)
        clauses.append(clause)
    return clauses

def find_solutions_sat(clauses, n):
    """Brute-force: all satisfying assignments of a SAT instance."""
    solutions = []
    for bits in itertools.product([0, 1], repeat=n):
        sat = True
        for clause in clauses:
            ok = any((lit > 0 and bits[abs(lit)-1] == 1) or
                     (lit < 0 and bits[abs(lit)-1] == 0) for lit in clause)
            if not ok:
                sat = False
                break
        if sat:
            solutions.append(bits)
    return solutions

def find_solutions_nae(clauses, n):
    """Brute-force: all NAE-satisfying assignments (not-all-equal)."""
    solutions = []
    for bits in itertools.product([0, 1], repeat=n):
        sat = True
        for clause in clauses:
            vals = set()
            for lit in clause:
                v = bits[abs(lit)-1]
                if lit < 0:
                    v = 1 - v
                vals.add(v)
            if len(vals) == 1:
                sat = False
                break
        if sat:
            solutions.append(bits)
    return solutions


# =====================================================================
# MAIN EXPERIMENT
# =====================================================================

N_INSTANCES = 100  # instances per (class, n) pair
NS = [8, 10, 12, 14]

# Store all results
all_results = {}

def run_csp_class(class_name, complexity, gen_func, solve_func, ns, n_instances):
    """Run the full experiment for one CSP class."""
    print(f"\n{'='*60}")
    print(f"  {class_name} ({complexity})")
    print(f"{'='*60}")
    print(f"{'n':>4s} {'|Sol| med':>10s} {'density med':>12s} {'TGap med':>10s} "
          f"{'N_cross med':>12s} {'best_op':>8s}")
    print("-" * 62)

    class_data = {}
    for n in ns:
        densities = []
        tgaps = []
        n_crossings_list = []
        best_ops_list = []
        n_sols_list = []

        for trial in range(n_instances):
            clauses = gen_func(n)
            solutions = solve_func(clauses, n)
            n_sol = len(solutions)

            if n_sol == 0:
                continue

            density = n_sol / (2**n)
            n_crossings = 2**n / n_sol if n_sol > 0 else float('inf')

            tgap, best_op = compute_tgap(solutions)
            if tgap is None:
                # Too few solutions for meaningful TGap
                tgap = float('nan')
                best_op = 'N/A'

            densities.append(density)
            tgaps.append(tgap)
            n_crossings_list.append(n_crossings)
            best_ops_list.append(best_op)
            n_sols_list.append(n_sol)

        if not densities:
            print(f"{n:4d} {'NO SAT INSTANCES':>50s}")
            continue

        # Compute medians
        densities.sort()
        tgaps_clean = sorted([t for t in tgaps if not math.isnan(t)])
        n_crossings_list.sort()
        n_sols_list.sort()

        med_density = densities[len(densities)//2]
        med_tgap = tgaps_clean[len(tgaps_clean)//2] if tgaps_clean else float('nan')
        med_ncross = n_crossings_list[len(n_crossings_list)//2]
        med_nsol = n_sols_list[len(n_sols_list)//2]

        # Most common best op
        from collections import Counter
        op_counts = Counter(best_ops_list)
        common_op = op_counts.most_common(1)[0][0]

        print(f"{n:4d} {med_nsol:10.0f} {med_density:12.6f} {med_tgap:10.4f} "
              f"{med_ncross:12.1f} {common_op:>8s}")

        class_data[n] = {
            'n': n,
            'median_n_sol': med_nsol,
            'median_density': med_density,
            'median_tgap': med_tgap,
            'median_n_crossings': med_ncross,
            'best_op': common_op,
            'all_densities': densities,
            'all_tgaps': tgaps_clean,
            'all_n_crossings': n_crossings_list,
            'n_instances_used': len(densities),
        }

    all_results[class_name] = {
        'complexity': complexity,
        'data': class_data,
    }
    return class_data


print("=" * 70)
print("GAP-CROSSING COUNT EXPERIMENT")
print("Testing: N_crossings = 2^n / |Sol| as complexity discriminator")
print("=" * 70)

# ----- 2-SAT (P) -----
run_csp_class(
    '2-SAT', 'P',
    gen_func=lambda n: gen_random_ksat(n, 2*n, 2),
    solve_func=find_solutions_sat,
    ns=NS, n_instances=N_INSTANCES,
)

# ----- Horn-SAT (P) -----
run_csp_class(
    'Horn-SAT', 'P',
    gen_func=lambda n: gen_horn(n, 2*n),
    solve_func=find_solutions_sat,
    ns=NS, n_instances=N_INSTANCES,
)

# ----- 3-SAT (NPC) at critical ratio -----
run_csp_class(
    '3-SAT', 'NPC',
    gen_func=lambda n: gen_random_ksat(n, int(4.267*n), 3),
    solve_func=find_solutions_sat,
    ns=NS, n_instances=N_INSTANCES,
)

# ----- NAE-3-SAT (NPC) -----
run_csp_class(
    'NAE-3-SAT', 'NPC',
    gen_func=lambda n: gen_random_ksat(n, 2*n, 3),
    solve_func=find_solutions_nae,
    ns=NS, n_instances=N_INSTANCES,
)


# =====================================================================
# ANALYSIS 1: TGap vs N_crossings correlation
# =====================================================================
print("\n\n" + "=" * 70)
print("ANALYSIS 1: TGap vs N_crossings — correlation table")
print("=" * 70)

print(f"\n{'Class':>12s} {'Complexity':>10s} {'n':>4s} {'TGap':>10s} {'N_cross':>12s} {'log2(N_cr)':>12s}")
print("-" * 66)

for cname, cresult in all_results.items():
    comp = cresult['complexity']
    for n in NS:
        if n in cresult['data']:
            d = cresult['data'][n]
            tgap = d['median_tgap']
            ncross = d['median_n_crossings']
            log2_ncross = math.log2(ncross) if ncross > 0 else 0
            print(f"{cname:>12s} {comp:>10s} {n:4d} {tgap:10.4f} {ncross:12.1f} {log2_ncross:12.2f}")


# =====================================================================
# ANALYSIS 2: Correlation between TGap and log2(N_crossings)
# =====================================================================
print("\n\n" + "=" * 70)
print("ANALYSIS 2: Pearson correlation TGap vs log2(N_crossings)")
print("=" * 70)

all_tgap_vals = []
all_log2_ncross = []
all_labels = []

for cname, cresult in all_results.items():
    for n in NS:
        if n in cresult['data']:
            d = cresult['data'][n]
            tgap = d['median_tgap']
            ncross = d['median_n_crossings']
            if not math.isnan(tgap) and ncross > 0:
                all_tgap_vals.append(tgap)
                all_log2_ncross.append(math.log2(ncross))
                all_labels.append(f"{cname}(n={n})")

# Pearson correlation
if len(all_tgap_vals) >= 3:
    n_pts = len(all_tgap_vals)
    mean_x = sum(all_tgap_vals) / n_pts
    mean_y = sum(all_log2_ncross) / n_pts
    cov_xy = sum((all_tgap_vals[i] - mean_x) * (all_log2_ncross[i] - mean_y)
                 for i in range(n_pts)) / n_pts
    var_x = sum((all_tgap_vals[i] - mean_x)**2 for i in range(n_pts)) / n_pts
    var_y = sum((all_log2_ncross[i] - mean_y)**2 for i in range(n_pts)) / n_pts
    if var_x > 0 and var_y > 0:
        r = cov_xy / math.sqrt(var_x * var_y)
        print(f"\n  Pearson r(TGap, log2(N_crossings)) = {r:.4f}")
        print(f"  (r > 0 means TGap and N_crossings co-vary as predicted)")
    else:
        r = None
        print("\n  Variance is zero in one variable — correlation undefined")
else:
    r = None
    print("\n  Too few data points for correlation")


# =====================================================================
# ANALYSIS 3: Separation test — does TGap=0 iff N_crossings=O(1)?
# =====================================================================
print("\n\n" + "=" * 70)
print("ANALYSIS 3: Separation test — P vs NPC dichotomy")
print("=" * 70)

p_tgaps = []
p_ncross = []
npc_tgaps = []
npc_ncross = []

for cname, cresult in all_results.items():
    comp = cresult['complexity']
    for n in NS:
        if n in cresult['data']:
            d = cresult['data'][n]
            tgap = d['median_tgap']
            ncross = d['median_n_crossings']
            if not math.isnan(tgap):
                if comp == 'P':
                    p_tgaps.append(tgap)
                    p_ncross.append(ncross)
                else:
                    npc_tgaps.append(tgap)
                    npc_ncross.append(ncross)

print(f"\n  P-time classes:")
if p_tgaps:
    print(f"    TGap range:       [{min(p_tgaps):.6f}, {max(p_tgaps):.6f}]")
    print(f"    N_crossings range: [{min(p_ncross):.1f}, {max(p_ncross):.1f}]")
else:
    print(f"    No data")

print(f"\n  NPC classes:")
if npc_tgaps:
    print(f"    TGap range:       [{min(npc_tgaps):.6f}, {max(npc_tgaps):.6f}]")
    print(f"    N_crossings range: [{min(npc_ncross):.1f}, {max(npc_ncross):.1f}]")
else:
    print(f"    No data")

# Check separation
tgap_separated = False
ncross_separated = False
if p_tgaps and npc_tgaps:
    tgap_gap = min(npc_tgaps) - max(p_tgaps)
    tgap_separated = tgap_gap > 0
    print(f"\n  TGap separation gap: {tgap_gap:+.6f} {'(CLEAN)' if tgap_separated else '(OVERLAP)'}")

if p_ncross and npc_ncross:
    ncross_gap = min(npc_ncross) - max(p_ncross)
    ncross_separated = ncross_gap > 0
    print(f"  N_crossings separation gap: {ncross_gap:+.1f} {'(CLEAN)' if ncross_separated else '(OVERLAP)'}")


# =====================================================================
# ANALYSIS 4: Scaling exponents for NPC classes
# =====================================================================
print("\n\n" + "=" * 70)
print("ANALYSIS 4: Scaling exponents — N_crossings(n) ~ C * 2^{alpha*n}")
print("=" * 70)

scaling_results = {}

for cname, cresult in all_results.items():
    if cresult['complexity'] != 'NPC':
        continue

    ns_used = []
    log2_ncross_vals = []
    tgap_vals = []

    for n in NS:
        if n in cresult['data']:
            d = cresult['data'][n]
            ncross = d['median_n_crossings']
            tgap = d['median_tgap']
            if ncross > 1 and not math.isnan(tgap):
                ns_used.append(n)
                log2_ncross_vals.append(math.log2(ncross))
                tgap_vals.append(tgap)

    if len(ns_used) < 2:
        print(f"\n  {cname}: insufficient data for scaling fit")
        continue

    # Linear regression: log2(N_crossings) = alpha * n + c
    n_pts = len(ns_used)
    mean_n = sum(ns_used) / n_pts
    mean_log = sum(log2_ncross_vals) / n_pts
    num = sum((ns_used[i] - mean_n) * (log2_ncross_vals[i] - mean_log) for i in range(n_pts))
    den = sum((ns_used[i] - mean_n)**2 for i in range(n_pts))
    if den > 0:
        alpha_fit = num / den
        c_fit = mean_log - alpha_fit * mean_n
        # R^2
        ss_res = sum((log2_ncross_vals[i] - alpha_fit * ns_used[i] - c_fit)**2 for i in range(n_pts))
        ss_tot = sum((log2_ncross_vals[i] - mean_log)**2 for i in range(n_pts))
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        print(f"\n  {cname}:")
        print(f"    Fit: log2(N_crossings) = {alpha_fit:.4f} * n + ({c_fit:.2f})")
        print(f"    => N_crossings ~ 2^({alpha_fit:.4f} * n)")
        print(f"    R^2 = {r2:.4f}")
        print(f"    Data points:")
        for i in range(n_pts):
            predicted = alpha_fit * ns_used[i] + c_fit
            print(f"      n={ns_used[i]:2d}: log2(N_cross)={log2_ncross_vals[i]:8.2f}  "
                  f"predicted={predicted:8.2f}  TGap={tgap_vals[i]:.4f}")

        scaling_results[cname] = {
            'alpha': alpha_fit,
            'c': c_fit,
            'r2': r2,
        }

    # Also fit TGap ~ n^beta (log-log regression)
    if all(t > 0 for t in tgap_vals) and len(ns_used) >= 2:
        log_ns = [math.log(n) for n in ns_used]
        log_tg = [math.log(t) for t in tgap_vals]
        mean_ln = sum(log_ns) / n_pts
        mean_lt = sum(log_tg) / n_pts
        num2 = sum((log_ns[i] - mean_ln) * (log_tg[i] - mean_lt) for i in range(n_pts))
        den2 = sum((log_ns[i] - mean_ln)**2 for i in range(n_pts))
        if den2 > 0:
            beta_fit = num2 / den2
            print(f"    TGap scaling: TGap ~ n^{beta_fit:.4f}")
            print(f"    (Compare with expected exponent ~ 0.43)")
            if cname in scaling_results:
                scaling_results[cname]['beta_tgap'] = beta_fit


# =====================================================================
# ANALYSIS 5: TGap scaling exponent for P-time classes
# =====================================================================
print("\n\n" + "=" * 70)
print("ANALYSIS 5: TGap for P-time classes (should be ~0)")
print("=" * 70)

for cname, cresult in all_results.items():
    if cresult['complexity'] != 'P':
        continue
    print(f"\n  {cname}:")
    for n in NS:
        if n in cresult['data']:
            d = cresult['data'][n]
            tgap = d['median_tgap']
            ncross = d['median_n_crossings']
            print(f"    n={n:2d}: TGap = {tgap:.6f}, N_crossings = {ncross:.1f}")


# =====================================================================
# VERDICT
# =====================================================================
print("\n\n" + "=" * 70)
print("VERDICT")
print("=" * 70)

# Criteria:
# 1. TGap = 0 for P, TGap > 0 for NPC (with clean separation)
# 2. N_crossings = O(1) for P, exponential for NPC
# 3. Positive correlation between TGap and log2(N_crossings)
# 4. Scaling exponent alpha > 0 for NPC

verdict_points = []

# Check 1: TGap separation
if p_tgaps and npc_tgaps:
    max_p_tgap = max(p_tgaps)
    min_npc_tgap = min(npc_tgaps)
    if max_p_tgap < 0.01 and min_npc_tgap > 0.01:
        verdict_points.append(("TGap separation (P near 0, NPC > 0)", "PASS"))
    elif tgap_separated:
        verdict_points.append(("TGap separation (clean gap exists)", "PASS"))
    else:
        verdict_points.append(("TGap separation", "FAIL" if max_p_tgap > min_npc_tgap else "PARTIAL"))

# Check 2: N_crossings separation
if p_ncross and npc_ncross:
    max_p_ncross = max(p_ncross)
    min_npc_ncross = min(npc_ncross)
    if max_p_ncross < 100 and min_npc_ncross > 100:
        verdict_points.append(("N_crossings separation (P small, NPC large)", "PASS"))
    elif ncross_separated:
        verdict_points.append(("N_crossings separation (clean gap)", "PASS"))
    else:
        verdict_points.append(("N_crossings separation", "FAIL"))

# Check 3: Correlation
if r is not None:
    if r > 0.5:
        verdict_points.append((f"TGap-N_crossings correlation (r={r:.3f})", "PASS"))
    elif r > 0:
        verdict_points.append((f"TGap-N_crossings correlation (r={r:.3f})", "PARTIAL"))
    else:
        verdict_points.append((f"TGap-N_crossings correlation (r={r:.3f})", "FAIL"))

# Check 4: Exponential scaling for NPC
for cname, sr in scaling_results.items():
    alpha = sr['alpha']
    r2 = sr['r2']
    if alpha > 0.3 and r2 > 0.9:
        verdict_points.append((f"{cname} exponential scaling (alpha={alpha:.3f}, R2={r2:.3f})", "PASS"))
    elif alpha > 0:
        verdict_points.append((f"{cname} exponential scaling (alpha={alpha:.3f}, R2={r2:.3f})", "PARTIAL"))
    else:
        verdict_points.append((f"{cname} exponential scaling (alpha={alpha:.3f})", "FAIL"))

# Overall verdict
n_pass = sum(1 for _, v in verdict_points if v == "PASS")
n_partial = sum(1 for _, v in verdict_points if v == "PARTIAL")
n_fail = sum(1 for _, v in verdict_points if v == "FAIL")

print("\n  Individual checks:")
for desc, result in verdict_points:
    marker = "[PASS]" if result == "PASS" else ("[PARTIAL]" if result == "PARTIAL" else "[FAIL]")
    print(f"    {marker:10s} {desc}")

print(f"\n  Summary: {n_pass} PASS, {n_partial} PARTIAL, {n_fail} FAIL out of {len(verdict_points)} checks")

if n_fail == 0 and n_pass >= 3:
    overall = "PASS"
elif n_fail == 0:
    overall = "PARTIAL PASS"
else:
    overall = "FAIL"

print(f"\n  OVERALL VERDICT: {overall}")
print(f"\n  The gap-crossing-count mechanism {'DOES' if overall != 'FAIL' else 'does NOT'} "
      f"distinguish P from NPC in the tested CSP classes.")


# =====================================================================
# Save structured results for the markdown report
# =====================================================================
report_data = {
    'classes': {},
    'correlation_r': r,
    'scaling': scaling_results,
    'verdict': overall,
    'verdict_points': verdict_points,
}
for cname, cresult in all_results.items():
    report_data['classes'][cname] = {
        'complexity': cresult['complexity'],
        'data': {}
    }
    for n, d in cresult['data'].items():
        report_data['classes'][cname]['data'][n] = {
            'median_n_sol': d['median_n_sol'],
            'median_density': d['median_density'],
            'median_tgap': d['median_tgap'],
            'median_n_crossings': d['median_n_crossings'],
            'best_op': d['best_op'],
            'n_instances': d['n_instances_used'],
        }

# We'll print the report data as well for the markdown generator
print("\n\n[REPORT DATA]")
# Serialize carefully (handle non-serializable types)
def safe_serialize(obj):
    if isinstance(obj, float):
        if math.isnan(obj):
            return "NaN"
        if math.isinf(obj):
            return "Inf"
    return obj

print(json.dumps(report_data, default=str, indent=2))
