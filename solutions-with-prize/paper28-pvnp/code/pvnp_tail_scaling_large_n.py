#!/usr/bin/env python3
"""
pvnp_tail_scaling_large_n.py
============================
Push the SV tail weight scaling test to larger n (12, 14, 16).

Reproduces the methodology of pvnp_sv_thickness_k4.py:
  - Build T_f operators in the full 2^n-dimensional space
  - Vectorize each T_f, stack as columns of matrix M
  - Compute SVD of M; tail weight = sum(SVs beyond rank 3) / total

For n >= 12, the full 2^n x 2^n operator is too large to materialize.
Instead we use a PROJECTED operator: restrict T_f to the solution
subspace (|Sol| x |Sol| matrix), vectorize, and stack.

This is mathematically equivalent to the restriction of the original
operator to the solution subspace, which captures the polymorphism
structure faithfully.

For n=6,8,10: we recompute from scratch to validate against known data.
For n=12,14,16: new results.

random.seed(42) throughout.
"""

import numpy as np
import random
import itertools
import time
import signal
from scipy.optimize import curve_fit
from scipy.linalg import svd as scipy_svd

random.seed(42)
np.random.seed(42)

# ============================================================
# Timeout mechanism
# ============================================================
class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Timed out")

# ============================================================
# k-SAT instance generation and solution finding
# ============================================================
def random_ksat_instance(n, k, alpha):
    """Generate a random k-SAT instance with m = alpha * n clauses."""
    m = int(alpha * n)
    clauses = []
    for _ in range(m):
        variables = random.sample(range(n), k)
        signs = [random.choice([True, False]) for _ in range(k)]
        clauses.append(list(zip(variables, signs)))
    return clauses

def evaluate_clause(clause, assignment):
    for var, positive in clause:
        if positive and assignment[var]:
            return True
        if not positive and not assignment[var]:
            return True
    return False

def find_all_solutions(clauses, n):
    """Brute-force enumerate all satisfying assignments."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause(c, assignment) for c in clauses):
            solutions.append(assignment)
    return solutions

# ============================================================
# Polymorphism enumeration (ternary, k=3)
# ============================================================
def is_polymorphism_k3(f_table, solutions, sol_set):
    """
    Check if a ternary boolean function f is a polymorphism of Sol.
    f_table has 8 entries indexed by (a<<2 | b<<1 | c).
    """
    if len(solutions) == 0:
        return True
    n = len(solutions[0])
    for s1 in solutions:
        for s2 in solutions:
            for s3 in solutions:
                result = tuple(
                    f_table[(s1[j] << 2) | (s2[j] << 1) | s3[j]]
                    for j in range(n)
                )
                if result not in sol_set:
                    return False
    return True

def is_projection_k3(f_table):
    """Check if f is a projection: f(a,b,c) = a, b, or c."""
    # pi_1: f(a,b,c) = a  -> f_table[a<<2|b<<1|c] = a
    if all(f_table[(a << 2) | (b << 1) | c] == a
           for a in range(2) for b in range(2) for c in range(2)):
        return True
    # pi_2: f(a,b,c) = b
    if all(f_table[(a << 2) | (b << 1) | c] == b
           for a in range(2) for b in range(2) for c in range(2)):
        return True
    # pi_3: f(a,b,c) = c
    if all(f_table[(a << 2) | (b << 1) | c] == c
           for a in range(2) for b in range(2) for c in range(2)):
        return True
    return False

def enumerate_polymorphisms_k3(solutions):
    """Enumerate all ternary boolean polymorphisms of the solution set."""
    sol_set = set(solutions)
    projections = []
    non_projections = []
    for bits in range(256):  # 2^(2^3) = 256 ternary boolean functions
        f_table = [(bits >> j) & 1 for j in range(8)]
        if is_polymorphism_k3(f_table, solutions, sol_set):
            if is_projection_k3(f_table):
                projections.append(f_table)
            else:
                non_projections.append(f_table)
    return projections, non_projections

# ============================================================
# Operator construction -- FULL 2^n space (for small n)
# ============================================================
def build_operator_full(f_table, solutions, n):
    """
    Build T_f in full 2^n-dimensional space:
      T_f[result_idx, a_bits] = (1/|Sol|^2) * #{(b,c) in Sol^2 : f(a,b,c) = result}
    where f is applied coordinate-wise.
    """
    dim = 2**n
    T = np.zeros((dim, dim))
    for b in solutions:
        for c in solutions:
            for a_bits in range(dim):
                a = tuple((a_bits >> i) & 1 for i in range(n))
                result = tuple(
                    f_table[(a[j] << 2) | (b[j] << 1) | c[j]]
                    for j in range(n)
                )
                result_idx = sum(result[j] << j for j in range(n))
                T[result_idx, a_bits] += 1.0
    T /= len(solutions)**2
    return T

# ============================================================
# Operator construction -- PROJECTED to solution subspace
# ============================================================
def build_operator_projected(f_table, solutions, n):
    """
    Build T_f restricted to the solution subspace.
    T_f[i, a_idx] = (1/|Sol|^2) * #{(b,c) in Sol^2 : f(sol_a, b, c) = sol_i}

    This is an |Sol| x |Sol| matrix. a ranges over solutions,
    and we count how often applying f maps to each solution.
    """
    m = len(solutions)
    if m == 0:
        return np.zeros((1, 1))
    sol_set = {s: idx for idx, s in enumerate(solutions)}
    T = np.zeros((m, m))
    for b_idx in range(m):
        b = solutions[b_idx]
        for c_idx in range(m):
            c = solutions[c_idx]
            for a_idx in range(m):
                a = solutions[a_idx]
                result = tuple(
                    f_table[(a[j] << 2) | (b[j] << 1) | c[j]]
                    for j in range(n)
                )
                r_idx = sol_set.get(result, -1)
                if r_idx >= 0:
                    T[r_idx, a_idx] += 1.0
    T /= m * m
    return T

# ============================================================
# SV spectrum analysis
# ============================================================
def sv_spectrum_analysis(non_proj_polys, solutions, n, use_full=True):
    """
    Build operator matrices for each non-projection polymorphism,
    vectorize them, stack as columns, compute SVD.

    Tail weight = sum(SVs beyond rank 3) / sum(all SVs).
    """
    if len(solutions) == 0 or len(non_proj_polys) == 0:
        return {
            'num_non_proj': 0,
            'operator_rank': 0,
            'top_svs': [],
            'tail_weight': 0.0,
            'total_sv_sum': 0.0,
        }

    columns = []
    builder = build_operator_full if use_full else build_operator_projected

    for f_table in non_proj_polys:
        T = builder(f_table, solutions, n)
        columns.append(T.flatten())

    M = np.column_stack(columns)
    U, S, Vh = np.linalg.svd(M, full_matrices=False)

    total = np.sum(S)
    if total < 1e-15:
        tail_weight = 0.0
    else:
        head = np.sum(S[:3]) if len(S) >= 3 else np.sum(S)
        tail_weight = (total - head) / total

    rank = int(np.sum(S > 1e-10))

    return {
        'num_non_proj': len(non_proj_polys),
        'operator_rank': rank,
        'top_svs': S[:min(10, len(S))].tolist(),
        'tail_weight': float(tail_weight),
        'total_sv_sum': float(total),
    }

# ============================================================
# Run experiment for one (n, k_sat, alpha) configuration
# ============================================================
def run_experiment(n, k_sat, alpha, num_instances=15, timeout_sec=10, use_full=True):
    """Run the full experiment for given parameters."""
    results_list = []
    n_timeout = 0

    for inst in range(num_instances):
        clauses = random_ksat_instance(n, k_sat, alpha)

        # Find all solutions (with timeout for large n)
        try:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout_sec)
            solutions = find_all_solutions(clauses, n)
            signal.alarm(0)
        except TimeoutError:
            signal.alarm(0)
            n_timeout += 1
            results_list.append(None)
            continue
        except Exception:
            signal.alarm(0)
            results_list.append(None)
            continue

        if len(solutions) == 0:
            results_list.append(None)
            continue

        # For large solution sets, sample for polymorphism checking
        if len(solutions) > 40:
            # Full polymorphism enumeration with all solutions is O(|Sol|^3 * 256)
            # which can be huge. Sample to keep feasible.
            sol_sample = random.sample(solutions, 40)
        else:
            sol_sample = list(solutions)

        projs, non_projs = enumerate_polymorphisms_k3(sol_sample)

        if len(non_projs) == 0:
            results_list.append({
                'num_non_proj': 0,
                'operator_rank': 0,
                'top_svs': [],
                'tail_weight': 0.0,
                'total_sv_sum': 0.0,
                'num_solutions': len(solutions),
                'num_projections': len(projs),
                'total_non_proj': 0,
            })
            continue

        # For operator construction, use full space for small n, projected for large n
        # For the projected operator, use the sampled solutions
        if use_full and n <= 10:
            # Use full 2^n space -- only feasible for n <= 10 (2^10 = 1024)
            analysis = sv_spectrum_analysis(non_projs, sol_sample, n, use_full=True)
        else:
            # Use solution-subspace projection
            analysis = sv_spectrum_analysis(non_projs, sol_sample, n, use_full=False)

        analysis['num_solutions'] = len(solutions)
        analysis['num_projections'] = len(projs)
        analysis['total_non_proj'] = len(non_projs)
        results_list.append(analysis)

    return results_list, n_timeout

def summarize_results(results_list, n_timeout, label):
    """Print summary statistics."""
    valid = [r for r in results_list if r is not None and r.get('num_non_proj', 0) > 0]
    all_with_sol = [r for r in results_list if r is not None]

    print(f"\n  {label}:")
    print(f"    Instances attempted:       {len(results_list)}")
    print(f"    Timed out:                 {n_timeout}")
    print(f"    SAT instances:             {len(all_with_sol)}")
    print(f"    With non-proj polys:       {len(valid)}")

    if all_with_sol:
        avg_sol = np.mean([r['num_solutions'] for r in all_with_sol])
        print(f"    Avg |Sol|:                 {avg_sol:.1f}")
    else:
        avg_sol = 0
        print(f"    Avg |Sol|:                 N/A")

    if not valid:
        print(f"    --> No instances with non-projection polymorphisms")
        return None

    avg_non_proj = np.mean([r['total_non_proj'] for r in valid])
    avg_rank = np.mean([r['operator_rank'] for r in valid])
    avg_tail = np.mean([r['tail_weight'] for r in valid])
    std_tail = np.std([r['tail_weight'] for r in valid])

    # Collect top SVs
    all_svs = []
    for r in valid:
        svs = r['top_svs'][:6]
        svs += [0.0] * (6 - len(svs))
        all_svs.append(svs)
    avg_svs = np.mean(all_svs, axis=0)

    print(f"    Avg non-proj polymorphisms:{avg_non_proj:.1f}")
    print(f"    Avg operator rank:         {avg_rank:.1f}")
    print(f"    Avg top 6 SVs:             {np.array2string(avg_svs, precision=4, separator=', ')}")
    print(f"    Avg tail weight:           {avg_tail:.6f} +/- {std_tail:.6f}")

    return {
        'avg_tail': avg_tail,
        'std_tail': std_tail,
        'avg_non_proj': avg_non_proj,
        'avg_rank': avg_rank,
        'n_valid': len(valid),
        'avg_sol': avg_sol,
    }

# ============================================================
# Curve fitting
# ============================================================
def linear_floor(n, a, b):
    return a - b * n

def power_law(n, a, c):
    return a * n**(-c)

def exponential_collapse(n, a, b):
    return a * np.exp(-b * n)

def fit_and_extrapolate(ns, tails, label):
    """Fit models and extrapolate."""
    ns = np.array(ns, dtype=float)
    tails = np.array(tails, dtype=float)

    # Remove any zero or negative tails for log-based fits
    mask = tails > 1e-10

    print(f"\n{'='*60}")
    print(f"  FITTING: {label}")
    print(f"{'='*60}")
    print(f"  Data points: n = {ns.tolist()}, tail = {[f'{t:.4f}' for t in tails]}")

    extrap_ns = np.array([20, 30, 50], dtype=float)
    results = {}

    # Linear floor: tail = a - b*n
    try:
        popt, pcov = curve_fit(linear_floor, ns, tails, p0=[0.3, 0.01], maxfev=5000)
        a, b = popt
        residuals = tails - linear_floor(ns, *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((tails - np.mean(tails))**2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0
        print(f"\n  Linear floor: tail = {a:.4f} - {b:.4f}*n  (R^2 = {r2:.4f})")
        extrap = linear_floor(extrap_ns, *popt)
        for en, ev in zip(extrap_ns, extrap):
            print(f"    n={int(en):3d}: tail = {ev:.6f}")
        results['linear'] = (popt, r2, extrap)
    except Exception as e:
        print(f"\n  Linear floor fit failed: {e}")
        results['linear'] = None

    # Power law: tail = a * n^(-c)  (only fit on positive tails)
    if np.sum(mask) >= 2:
        try:
            popt, pcov = curve_fit(power_law, ns[mask], tails[mask], p0=[1.0, 0.5], maxfev=5000)
            a, c = popt
            residuals = tails[mask] - power_law(ns[mask], *popt)
            ss_res = np.sum(residuals**2)
            ss_tot = np.sum((tails[mask] - np.mean(tails[mask]))**2)
            r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0
            print(f"\n  Power law: tail = {a:.4f} * n^(-{c:.4f})  (R^2 = {r2:.4f})")
            extrap = power_law(extrap_ns, *popt)
            for en, ev in zip(extrap_ns, extrap):
                print(f"    n={int(en):3d}: tail = {ev:.6f}")
            results['power'] = (popt, r2, extrap)
        except Exception as e:
            print(f"\n  Power law fit failed: {e}")
            results['power'] = None
    else:
        print(f"\n  Power law: not enough positive data points")
        results['power'] = None

    # Exponential collapse: tail = a * exp(-b*n)  (only fit on positive tails)
    if np.sum(mask) >= 2:
        try:
            popt, pcov = curve_fit(exponential_collapse, ns[mask], tails[mask],
                                   p0=[0.5, 0.1], maxfev=5000)
            a, b = popt
            residuals = tails[mask] - exponential_collapse(ns[mask], *popt)
            ss_res = np.sum(residuals**2)
            ss_tot = np.sum((tails[mask] - np.mean(tails[mask]))**2)
            r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0
            print(f"\n  Exponential: tail = {a:.4f} * exp(-{b:.4f}*n)  (R^2 = {r2:.4f})")
            extrap = exponential_collapse(extrap_ns, *popt)
            for en, ev in zip(extrap_ns, extrap):
                print(f"    n={int(en):3d}: tail = {ev:.2e}")
            results['exponential'] = (popt, r2, extrap)
        except Exception as e:
            print(f"\n  Exponential fit failed: {e}")
            results['exponential'] = None
    else:
        print(f"\n  Exponential: not enough positive data points")
        results['exponential'] = None

    return results

# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("=" * 70)
    print("  SV TAIL WEIGHT SCALING TEST -- LARGE n")
    print("  Recomputing n=6,8,10 and extending to n=12, 14, 16")
    print("  Methodology: pvnp_sv_thickness_k4.py operator construction")
    print("=" * 70)

    all_ns = [6, 8, 10, 12, 14, 16]
    scaling_data = {'2-SAT': {}, '3-SAT': {}}

    for n in all_ns:
        print(f"\n\n{'#'*70}")
        print(f"  n = {n}  (2^n = {2**n})")
        print(f"{'#'*70}")

        # For n <= 10: use full 2^n space operators (matches original methodology)
        # For n >= 12: use projected operators (solution subspace)
        use_full = (n <= 10)

        # Adjust number of instances and timeout
        if n <= 10:
            ni = 20
            to = 10
        elif n <= 14:
            ni = 15
            to = 10
        else:
            ni = 15
            to = 15

        t0 = time.time()

        # 2-SAT (k=2, alpha=1.5)
        print(f"\n  Running 2-SAT (alpha=1.5) ...")
        t1 = time.time()
        res_2sat, to_2 = run_experiment(n, k_sat=2, alpha=1.5,
                                         num_instances=ni, timeout_sec=to,
                                         use_full=use_full)
        t2 = time.time()
        print(f"  Time: {t2-t1:.1f}s")
        s2 = summarize_results(res_2sat, to_2, f'2-SAT (n={n}, alpha=1.5)')
        if s2:
            scaling_data['2-SAT'][n] = s2

        # 3-SAT (k=3, alpha=3.5)
        print(f"\n  Running 3-SAT (alpha=3.5) ...")
        t1 = time.time()
        res_3sat, to_3 = run_experiment(n, k_sat=3, alpha=3.5,
                                         num_instances=ni, timeout_sec=to,
                                         use_full=use_full)
        t2 = time.time()
        print(f"  Time: {t2-t1:.1f}s")
        s3 = summarize_results(res_3sat, to_3, f'3-SAT (n={n}, alpha=3.5)')
        if s3:
            scaling_data['3-SAT'][n] = s3

        t3 = time.time()
        print(f"\n  Total time for n={n}: {t3-t0:.1f}s")

    # ============================================================
    # Combined results table
    # ============================================================
    print("\n\n" + "=" * 70)
    print("  COMBINED RESULTS TABLE")
    print("=" * 70)
    print(f"  {'n':>4s}  {'2-SAT tail':>12s}  {'3-SAT tail':>12s}  {'Ratio':>10s}  {'2SAT rank':>10s}  {'3SAT rank':>10s}")
    print(f"  {'-'*4}  {'-'*12}  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*10}")

    for n in all_ns:
        d2 = scaling_data['2-SAT'].get(n)
        d3 = scaling_data['3-SAT'].get(n)
        t2 = d2['avg_tail'] if d2 else None
        t3 = d3['avg_tail'] if d3 else None
        r2 = d2['avg_rank'] if d2 else None
        r3 = d3['avg_rank'] if d3 else None

        s_t2 = f"{t2:.6f}" if t2 is not None else "N/A"
        s_t3 = f"{t3:.6f}" if t3 is not None else "N/A"
        s_r2 = f"{r2:.1f}" if r2 is not None else "N/A"
        s_r3 = f"{r3:.1f}" if r3 is not None else "N/A"

        if t2 is not None and t3 is not None and t3 > 1e-10:
            ratio = t2 / t3
            s_ratio = f"{ratio:.2f}"
        elif t2 is not None and t3 is not None and t2 > 1e-10 and t3 < 1e-10:
            s_ratio = "INF"
        elif t2 is not None and t3 is not None:
            s_ratio = "~1"
        else:
            s_ratio = "N/A"

        print(f"  {n:4d}  {s_t2:>12s}  {s_t3:>12s}  {s_ratio:>10s}  {s_r2:>10s}  {s_r3:>10s}")

    # ============================================================
    # Build arrays for fitting
    # ============================================================
    fit_ns_2 = sorted(scaling_data['2-SAT'].keys())
    fit_tails_2 = [scaling_data['2-SAT'][n]['avg_tail'] for n in fit_ns_2]

    fit_ns_3 = sorted(scaling_data['3-SAT'].keys())
    fit_tails_3 = [scaling_data['3-SAT'][n]['avg_tail'] for n in fit_ns_3]

    # ============================================================
    # Curve fitting
    # ============================================================
    print("\n\n" + "#" * 70)
    print("  CURVE FITTING AND EXTRAPOLATION")
    print("#" * 70)

    fits_2sat = fit_and_extrapolate(fit_ns_2, fit_tails_2, "2-SAT tail weight")
    fits_3sat = fit_and_extrapolate(fit_ns_3, fit_tails_3, "3-SAT tail weight")

    # ============================================================
    # Predicted ratios at extrapolated n
    # ============================================================
    print("\n\n" + "=" * 70)
    print("  EXTRAPOLATED RATIOS")
    print("=" * 70)

    extrap_ns = [20, 30, 50]

    for model_2, model_3, desc in [
        ('linear', 'exponential', 'Linear(2-SAT) / Exp(3-SAT)'),
        ('power', 'power', 'Power(2-SAT) / Power(3-SAT)'),
        ('power', 'exponential', 'Power(2-SAT) / Exp(3-SAT)'),
    ]:
        if fits_2sat.get(model_2) is not None and fits_3sat.get(model_3) is not None:
            print(f"\n  Model: {desc}")
            _, _, extrap_2 = fits_2sat[model_2]
            _, _, extrap_3 = fits_3sat[model_3]
            for i, en in enumerate(extrap_ns):
                e2 = float(extrap_2[i])
                e3 = float(extrap_3[i])
                if abs(e3) > 1e-15:
                    ratio = e2 / e3
                    print(f"    n={int(en):3d}: 2-SAT={e2:.6f}, 3-SAT={e3:.2e}, ratio={ratio:.1f}")
                else:
                    print(f"    n={int(en):3d}: 2-SAT={e2:.6f}, 3-SAT=~0, ratio=INF")

    # ============================================================
    # Key predictions check
    # ============================================================
    print("\n\n" + "=" * 70)
    print("  KEY PREDICTIONS CHECK")
    print("=" * 70)

    # 1. 2-SAT tail stays above 0.05 at all tested n
    all_2sat_vals = [scaling_data['2-SAT'][n]['avg_tail'] for n in sorted(scaling_data['2-SAT'].keys())]
    if all_2sat_vals:
        min_2sat = min(all_2sat_vals)
        status = "CONFIRMED" if min_2sat > 0.05 else f"VIOLATED (min={min_2sat:.6f})"
        print(f"\n  [1] 2-SAT tail > 0.05 at all n?  {status}")

    # 2. 3-SAT tail drops below 0.01 by n=14
    t3_14 = scaling_data['3-SAT'].get(14, {})
    if isinstance(t3_14, dict) and 'avg_tail' in t3_14:
        val = t3_14['avg_tail']
        status = "CONFIRMED" if val < 0.01 else f"NOT YET (tail={val:.6f})"
        print(f"\n  [2] 3-SAT tail < 0.01 by n=14?  {status}")

    # 3. Ratio > 5 by n=14
    d2_14 = scaling_data['2-SAT'].get(14)
    d3_14 = scaling_data['3-SAT'].get(14)
    if d2_14 and d3_14:
        t2 = d2_14['avg_tail']
        t3 = d3_14['avg_tail']
        if t3 > 1e-10:
            ratio_14 = t2 / t3
            status = "CONFIRMED" if ratio_14 > 5 else f"NOT YET (ratio={ratio_14:.2f})"
            print(f"\n  [3] Ratio > 5 by n=14?  {status}")
            print(f"      Observed ratio: {ratio_14:.2f}")
        elif t2 > 1e-10:
            print(f"\n  [3] Ratio > 5 by n=14?  CONFIRMED (3-SAT tail ~ 0)")

    # 4. Ratio > 10 by n=16
    d2_16 = scaling_data['2-SAT'].get(16)
    d3_16 = scaling_data['3-SAT'].get(16)
    if d2_16 and d3_16:
        t2 = d2_16['avg_tail']
        t3 = d3_16['avg_tail']
        if t3 > 1e-10:
            ratio_16 = t2 / t3
            status = "CONFIRMED" if ratio_16 > 10 else f"NOT YET (ratio={ratio_16:.2f})"
            print(f"\n  [4] Ratio > 10 by n=16?  {status}")
            print(f"      Observed ratio: {ratio_16:.2f}")
        elif t2 > 1e-10:
            print(f"\n  [4] Ratio > 10 by n=16?  CONFIRMED (3-SAT tail ~ 0)")

    # 5. Extrapolated ratio at n=50
    if fits_2sat.get('power') is not None and fits_3sat.get('exponential') is not None:
        _, _, ext2 = fits_2sat['power']
        _, _, ext3 = fits_3sat['exponential']
        e3_50 = float(ext3[2])
        e2_50 = float(ext2[2])
        if abs(e3_50) > 1e-15:
            r50 = e2_50 / e3_50
            status = "CONFIRMED" if r50 > 100 else f"ratio={r50:.1f}"
        else:
            r50 = float('inf')
            status = "CONFIRMED (ratio=INF)"
        print(f"\n  [5] Extrapolated ratio > 100 at n=50?  {status}")

    # ============================================================
    # Detailed per-instance data
    # ============================================================
    print("\n\n" + "=" * 70)
    print("  DETAILED INSTANCE-LEVEL DATA")
    print("=" * 70)

    for n in all_ns:
        for k_sat, alpha, label in [(2, 1.5, '2-SAT'), (3, 3.5, '3-SAT')]:
            # We don't have the raw results stored globally, but the summaries
            # are printed above. This section is informational.
            d = scaling_data.get(label, {}).get(n)
            if d:
                print(f"\n  {label} n={n}: avg_tail={d['avg_tail']:.6f}, "
                      f"avg_rank={d['avg_rank']:.1f}, "
                      f"avg_non_proj={d['avg_non_proj']:.1f}, "
                      f"n_valid={d['n_valid']}, "
                      f"avg_sol={d.get('avg_sol', 'N/A')}")

    print("\n\nDone.")
