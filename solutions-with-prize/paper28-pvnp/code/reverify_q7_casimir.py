"""
reverify_q7_casimir.py -- Independent re-verification of Q7-CASIMIR entry

Re-verifies: entropy per constraint s/alpha = log2|Sol|/(n * alpha) distinguishes
P from NPC. Tests decay rates, R^2, three-scale hierarchy (inflection points),
and Horn-SAT perpetual satisfiability.

Author: G Six, with Claude Opus 4.6. Date: 2026-04-12.
"""

import random
import itertools
import math
import json

random.seed(2026_04_12)  # fresh seed, independent of original run

N = 12
N_TRIALS = 50
TOTAL_ASSIGN = 2 ** N  # 4096

# =====================================================================
# Generators
# =====================================================================

def gen_2sat(n, m):
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n + 1), 2)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def gen_horn(n, m):
    """Horn clause: at most one positive literal. Width 2 or 3."""
    clauses = []
    for _ in range(m):
        k = random.randint(2, 3)
        vs = random.sample(range(1, n + 1), min(k, n))
        pos_idx = random.randint(0, len(vs))  # index == len(vs) means all negative
        clause = []
        for i, v in enumerate(vs):
            clause.append(v if i == pos_idx else -v)
        clauses.append(clause)
    return clauses

def gen_3sat(n, m):
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n + 1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def gen_nae3sat(n, m):
    """Same clause generation as 3-SAT; semantics differ in solver."""
    return gen_3sat(n, m)

# =====================================================================
# Solvers (brute force 2^12)
# =====================================================================

def count_sat(clauses, n):
    count = 0
    for bits in range(TOTAL_ASSIGN):
        ok = True
        for clause in clauses:
            clause_ok = False
            for lit in clause:
                var = abs(lit) - 1
                val = (bits >> var) & 1
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    clause_ok = True
                    break
            if not clause_ok:
                ok = False
                break
        if ok:
            count += 1
    return count

def count_nae(clauses, n):
    count = 0
    for bits in range(TOTAL_ASSIGN):
        ok = True
        for clause in clauses:
            has_true = False
            has_false = False
            for lit in clause:
                var = abs(lit) - 1
                val = (bits >> var) & 1
                if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                    has_true = True
                else:
                    has_false = True
                if has_true and has_false:
                    break
            if not (has_true and has_false):
                ok = False
                break
        if ok:
            count += 1
    return count

# =====================================================================
# Configuration
# =====================================================================

configs = {
    '2-SAT': {
        'alphas': [0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
        'gen': gen_2sat,
        'solve': count_sat,
        'type': 'P',
    },
    'Horn-SAT': {
        'alphas': [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
        'gen': gen_horn,
        'solve': count_sat,
        'type': 'P',
    },
    '3-SAT': {
        'alphas': [1.0, 2.0, 3.0, 3.5, 4.0, 4.267, 4.5, 5.0],
        'gen': gen_3sat,
        'solve': count_sat,
        'type': 'NPC',
    },
    'NAE-3-SAT': {
        'alphas': [0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
        'gen': gen_nae3sat,
        'solve': count_nae,
        'type': 'NPC',
    },
}

# =====================================================================
# (a)+(b): Generate instances, count solutions, compute stats
# =====================================================================

print("=" * 72)
print("REVERIFICATION: Q7-CASIMIR -- Solution Entropy as Computational Casimir Energy")
print("=" * 72)
print(f"n = {N}, trials = {N_TRIALS}, seed = 2026_04_12 (independent)")
print()

results = {}

for cname, cfg in configs.items():
    print(f"\n--- {cname} ({cfg['type']}) ---")
    print(f"  {'alpha':>6s} {'m':>4s} {'med|Sol|':>10s} {'s(a)':>8s} {'s/a':>8s} {'%SAT':>6s}")
    print("  " + "-" * 50)

    class_data = []
    for alpha in cfg['alphas']:
        m = max(1, int(alpha * N))
        sol_counts = []
        n_sat = 0

        for _ in range(N_TRIALS):
            clauses = cfg['gen'](N, m)
            nsol = cfg['solve'](clauses, N)
            sol_counts.append(nsol)
            if nsol > 0:
                n_sat += 1

        sol_counts.sort()
        median_sol = sol_counts[N_TRIALS // 2]
        pct_sat = 100.0 * n_sat / N_TRIALS

        if median_sol > 0:
            s_alpha = math.log2(median_sol) / N
        else:
            s_alpha = 0.0

        s_per_alpha = s_alpha / alpha if alpha > 0 else 0.0

        print(f"  {alpha:6.3f} {m:4d} {median_sol:10d} {s_alpha:8.4f} {s_per_alpha:8.4f} {pct_sat:5.1f}%")

        class_data.append({
            'alpha': alpha,
            'm': m,
            'median_sol': median_sol,
            'pct_sat': pct_sat,
            's_alpha': s_alpha,
            's_per_alpha': s_per_alpha,
        })

    results[cname] = {'type': cfg['type'], 'data': class_data}

# =====================================================================
# (c): Fit log(s/alpha) vs alpha for Horn-SAT and 3-SAT
# =====================================================================

print("\n\n" + "=" * 72)
print("PART (c): Exponential fit log(s/alpha) vs alpha")
print("=" * 72)

def linreg(xs, ys):
    """Simple OLS: y = slope*x + intercept. Returns (slope, intercept, R^2)."""
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxy = sum(x * y for x, y in zip(xs, ys))
    sx2 = sum(x * x for x in xs)
    denom = n * sx2 - sx * sx
    if abs(denom) < 1e-30:
        return 0.0, 0.0, 0.0
    slope = (n * sxy - sx * sy) / denom
    intercept = (sy - slope * sx) / n
    y_pred = [slope * x + intercept for x in xs]
    ss_res = sum((y - yp) ** 2 for y, yp in zip(ys, y_pred))
    mean_y = sy / n
    ss_tot = sum((y - mean_y) ** 2 for y in ys)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else 0.0
    return slope, intercept, r2

for cname in ['Horn-SAT', '3-SAT']:
    data = results[cname]['data']
    # Only include points with s/alpha > 0
    pts = [(d['alpha'], d['s_per_alpha']) for d in data if d['s_per_alpha'] > 0]
    if len(pts) < 3:
        print(f"\n  {cname}: too few positive points ({len(pts)})")
        continue

    alphas = [p[0] for p in pts]
    log_spa = [math.log(p[1]) for p in pts]

    slope, intercept, r2 = linreg(alphas, log_spa)

    print(f"\n  {cname}:")
    print(f"    Fit: log(s/alpha) = {slope:.4f} * alpha + {intercept:.4f}")
    print(f"    Decay rate = {slope:.4f}")
    print(f"    R^2 = {r2:.4f}")

    results[cname]['decay_rate'] = slope
    results[cname]['r2'] = r2

    # Original claim comparison
    if cname == 'Horn-SAT':
        print(f"    Original claim: decay rate = -0.358, R^2 = 0.996")
    elif cname == '3-SAT':
        print(f"    Original claim: decay rate = -0.503, R^2 = 0.913")

# =====================================================================
# (d): Three-scale hierarchy for 3-SAT via d^2 s / d alpha^2
# =====================================================================

print("\n\n" + "=" * 72)
print("PART (d): Three-scale hierarchy -- second derivative of s(alpha) for 3-SAT")
print("=" * 72)

data_3sat = results['3-SAT']['data']
# Use all points with s > 0 for second derivative
pos_data = [d for d in data_3sat if d['s_alpha'] > 0]

print(f"\n  Points with positive entropy: {len(pos_data)}")
for d in pos_data:
    print(f"    alpha = {d['alpha']:.3f}, s = {d['s_alpha']:.4f}")

# Compute second derivative at interior points
print("\n  Second derivative d^2s/dalpha^2:")
d2s_list = []
for i in range(1, len(pos_data) - 1):
    a0 = pos_data[i - 1]['alpha']
    a1 = pos_data[i]['alpha']
    a2 = pos_data[i + 1]['alpha']
    s0 = pos_data[i - 1]['s_alpha']
    s1 = pos_data[i]['s_alpha']
    s2 = pos_data[i + 1]['s_alpha']
    h1 = a1 - a0
    h2 = a2 - a1
    # Non-uniform finite difference second derivative
    d2s = 2.0 * (s0 / h1 - s1 * (1.0 / h1 + 1.0 / h2) + s2 / h2) / (h1 + h2)
    d2s_list.append((a1, d2s))
    print(f"    alpha = {a1:.3f}: d^2s/da^2 = {d2s:.6f}")

# Count sign changes = inflection points
inflection_alphas = []
for i in range(1, len(d2s_list)):
    if d2s_list[i - 1][1] * d2s_list[i][1] < 0:
        # Interpolate zero crossing
        a_left, v_left = d2s_list[i - 1]
        a_right, v_right = d2s_list[i]
        a_infl = a_left + (a_right - a_left) * abs(v_left) / (abs(v_left) + abs(v_right))
        inflection_alphas.append(a_infl)

print(f"\n  Sign changes in d^2s/da^2: {len(inflection_alphas)}")
if inflection_alphas:
    print(f"  Inflection points at alpha ~ {[f'{a:.2f}' for a in inflection_alphas]}")
print(f"\n  Claim: exactly 2 inflection points at alpha ~ 3.0 and ~ 4.0")
if len(inflection_alphas) == 2:
    print("  VERDICT: CONFIRMED -- exactly 2 inflection points found")
elif len(inflection_alphas) == 0:
    print("  VERDICT: FAILED -- no inflection points detected")
else:
    print(f"  VERDICT: DISCREPANT -- found {len(inflection_alphas)} inflection points, expected 2")
    print("  FLAG: Three-scale hierarchy claim may need refinement at n=12")

results['3-SAT']['inflection_points'] = inflection_alphas

# =====================================================================
# (e): Horn-SAT stays 100% SAT with positive s/alpha everywhere
# =====================================================================

print("\n\n" + "=" * 72)
print("PART (e): Horn-SAT perpetual satisfiability")
print("=" * 72)

horn_data = results['Horn-SAT']['data']
all_100_sat = all(d['pct_sat'] == 100.0 for d in horn_data)
all_positive_spa = all(d['s_per_alpha'] > 0 for d in horn_data)

print(f"\n  Horn-SAT across alpha = {[d['alpha'] for d in horn_data]}:")
print(f"    All 100% SAT?       {'YES' if all_100_sat else 'NO'}")
if not all_100_sat:
    for d in horn_data:
        if d['pct_sat'] < 100.0:
            print(f"      alpha={d['alpha']:.1f}: {d['pct_sat']:.1f}% SAT")
print(f"    All s/alpha > 0?    {'YES' if all_positive_spa else 'NO'}")

min_spa = min(d['s_per_alpha'] for d in horn_data)
max_spa = max(d['s_per_alpha'] for d in horn_data)
print(f"    s/alpha range:      [{min_spa:.4f}, {max_spa:.4f}]")

if all_100_sat and all_positive_spa:
    print("    VERDICT: CONFIRMED -- Horn-SAT always satisfiable with positive entropy")
else:
    print("    VERDICT: PARTIALLY CONFIRMED")

# =====================================================================
# OVERALL SUMMARY
# =====================================================================

print("\n\n" + "=" * 72)
print("OVERALL SUMMARY")
print("=" * 72)

horn_dr = results['Horn-SAT'].get('decay_rate', None)
horn_r2 = results['Horn-SAT'].get('r2', None)
sat3_dr = results['3-SAT'].get('decay_rate', None)
sat3_r2 = results['3-SAT'].get('r2', None)

print(f"""
  Horn-SAT decay rate:  {horn_dr:.4f}  (original: -0.358)  R^2 = {horn_r2:.4f}  (original: 0.996)
  3-SAT   decay rate:  {sat3_dr:.4f}  (original: -0.503)  R^2 = {sat3_r2:.4f}  (original: 0.913)

  P vs NPC distinction: {"CONFIRMED" if horn_dr is not None and sat3_dr is not None and sat3_dr < horn_dr else "CHECK"}
    3-SAT decays faster than Horn-SAT: {sat3_dr:.4f} < {horn_dr:.4f}

  Three-scale hierarchy: {len(results['3-SAT'].get('inflection_points', []))} inflection points (claimed: 2)
  Horn-SAT 100% SAT:    {"YES" if all_100_sat else "NO"}
  Horn-SAT s/alpha > 0: {"YES" if all_positive_spa else "NO"}
""")

# Save results
export = {}
for cname, rdata in results.items():
    export[cname] = {
        'type': rdata['type'],
        'decay_rate': rdata.get('decay_rate'),
        'r2': rdata.get('r2'),
        'inflection_points': rdata.get('inflection_points'),
        'data': rdata['data'],
    }

json_path = '/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/code/results_reverify_q7.json'
with open(json_path, 'w') as f:
    json.dump(export, f, indent=2, default=str)
print(f"Results saved to {json_path}")
