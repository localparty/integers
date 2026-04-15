"""
test_a6_phase_transition.py -- KMS phase transition at beta_c as the P/NPC boundary

Strategy 10, Entry A6: The Bost-Connes system has a phase transition at beta = 1
with spontaneous symmetry breaking. Does the CSP partition function
    Z_Gamma(beta) = sum_x exp(-beta * violations(x))
exhibit a critical beta_c where the specific heat C(beta) or susceptibility
chi(beta) diverges, and does this phase transition SEPARATE P-time from NPC?

Tests:
1. Compute Z(beta) for each CSP class by exact enumeration of all 2^n assignments
2. Compute specific heat C(beta) = beta^2 * Var_beta(violations)
3. Compute susceptibility chi(beta) = d^2(log Z)/d(beta)^2
4. Detect phase transitions: peak location beta_c, height, width
5. Critical test: does the transition structure separate P from NPC?
6. Finite-size scaling: does the peak grow with n for NPC (genuine transition)?
7. KMS connection: entropy S(beta=1) for each class

Author: G Six (originator), Claude Opus 4.6 (collaborator). Date: 2026-04-11.
"""

import random
import itertools
import math
import json
import sys
from collections import defaultdict

random.seed(42)

# =====================================================================
# PARAMETERS
# =====================================================================

BETA_VALUES = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0,
               8.0, 10.0, 15.0, 20.0, 50.0]

N_VALUES_MAIN = [10, 12]
N_VALUES_FSS = [8, 10, 12]     # finite-size scaling for 3-SAT
N_INSTANCES = 50

# Clause ratios: chosen near the critical regime for each class
# to maximise the chance of detecting phase structure
ALPHA_BY_CLASS = {
    '2-SAT':      2.0,   # near threshold for n=10-12
    'Horn-SAT':   3.0,   # well into constrained regime
    '3-SAT':      4.0,   # near but below alpha_c = 4.267
    'NAE-3-SAT':  2.0,   # near threshold ~2.11
}

# =====================================================================
# INSTANCE GENERATORS
# =====================================================================

def gen_random_ksat(n, m, k):
    """Generate random k-SAT instance: m clauses of width k on n variables."""
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n + 1), min(k, n))
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def gen_horn(n, m):
    """Generate random Horn clauses: at most one positive literal per clause."""
    clauses = []
    for _ in range(m):
        k = random.randint(2, 3)
        vs = random.sample(range(1, n + 1), min(k, n))
        pos_idx = random.randint(0, len(vs))  # may be out of range = all negative
        clause = []
        for i, v in enumerate(vs):
            if i == pos_idx:
                clause.append(v)
            else:
                clause.append(-v)
        clauses.append(clause)
    return clauses

# =====================================================================
# VIOLATION COUNTER -- the core energy function
# =====================================================================

def count_violations_sat(assignment, clauses):
    """Count number of violated clauses for a standard SAT instance."""
    v = 0
    for clause in clauses:
        ok = any((lit > 0 and assignment[abs(lit)-1] == 1) or
                 (lit < 0 and assignment[abs(lit)-1] == 0) for lit in clause)
        if not ok:
            v += 1
    return v

def count_violations_nae(assignment, clauses):
    """Count number of violated NAE clauses (all-equal counts as violated)."""
    v = 0
    for clause in clauses:
        vals = set()
        for lit in clause:
            val = assignment[abs(lit)-1]
            if lit < 0:
                val = 1 - val
            vals.add(val)
        if len(vals) == 1:
            v += 1
    return v

# =====================================================================
# PARTITION FUNCTION AND THERMODYNAMICS
# =====================================================================

def compute_violation_spectrum(clauses, n, mode='sat'):
    """Enumerate all 2^n assignments and return list of violation counts."""
    counter = count_violations_nae if mode == 'nae' else count_violations_sat
    violations = []
    for bits in itertools.product([0, 1], repeat=n):
        v = counter(bits, clauses)
        violations.append(v)
    return violations

def compute_thermodynamics(violations, betas):
    """
    Given violation counts for all 2^n assignments, compute thermodynamic
    quantities at each beta.

    Returns dict with keys: Z, F, E_mean, E_var, C, chi, S
    for each beta value.
    """
    results = {}
    violations = list(violations)
    N_configs = len(violations)

    for beta in betas:
        # Compute log-partition function with numerical stability
        # Z = sum_x exp(-beta * v(x))
        # Use log-sum-exp trick
        neg_beta_v = [-beta * v for v in violations]
        max_val = max(neg_beta_v)
        log_Z = max_val + math.log(sum(math.exp(x - max_val) for x in neg_beta_v))
        Z = math.exp(log_Z)

        # Boltzmann weights (normalized)
        weights = [math.exp(x - log_Z) for x in neg_beta_v]

        # <E> = <violations> under Boltzmann measure
        E_mean = sum(w * v for w, v in zip(weights, violations))

        # <E^2>
        E2_mean = sum(w * v * v for w, v in zip(weights, violations))

        # Variance
        E_var = E2_mean - E_mean * E_mean
        if E_var < 0:
            E_var = 0.0  # numerical noise guard

        # Specific heat: C(beta) = beta^2 * Var(E)
        C = beta * beta * E_var

        # Susceptibility: chi = d^2(log Z)/d(beta^2) = <E^2> - <E>^2 = Var(E)
        # (This IS the variance -- the second cumulant of the energy)
        chi = E_var

        # Entropy: S = beta * <E> + log Z
        S = beta * E_mean + log_Z

        # Free energy: F = -log Z / beta  (only for beta > 0)
        F = -log_Z / beta if beta > 0 else float('nan')

        results[beta] = {
            'Z': Z,
            'log_Z': log_Z,
            'F': F,
            'E_mean': E_mean,
            'E_var': E_var,
            'C': C,
            'chi': chi,
            'S': S,
        }

    return results

def find_peak(betas, values):
    """Find peak location, height, and FWHM of a curve."""
    if not values or all(v == 0 for v in values):
        return {'beta_c': None, 'peak_height': 0, 'fwhm': None}

    max_idx = max(range(len(values)), key=lambda i: values[i])
    peak_height = values[max_idx]
    beta_c = betas[max_idx]

    # FWHM: find half-maximum crossings
    half_max = peak_height / 2.0
    left_cross = betas[0]
    right_cross = betas[-1]

    for i in range(max_idx, -1, -1):
        if values[i] < half_max:
            if i + 1 < len(values):
                # Linear interpolation
                frac = (half_max - values[i]) / (values[i+1] - values[i]) if values[i+1] != values[i] else 0.5
                left_cross = betas[i] + frac * (betas[i+1] - betas[i])
            break

    for i in range(max_idx, len(values)):
        if values[i] < half_max:
            if i - 1 >= 0:
                frac = (half_max - values[i]) / (values[i-1] - values[i]) if values[i-1] != values[i] else 0.5
                right_cross = betas[i] - frac * (betas[i] - betas[i-1])
            break

    fwhm = right_cross - left_cross if right_cross > left_cross else None

    return {'beta_c': beta_c, 'peak_height': peak_height, 'fwhm': fwhm}

# =====================================================================
# MAIN COMPUTATION
# =====================================================================

def run_class(class_name, n, alpha, n_instances, betas, mode='sat'):
    """Run full thermodynamic analysis for one CSP class at given n."""
    m = int(alpha * n)
    k = 3
    if class_name == '2-SAT':
        k = 2

    print(f"  {class_name} n={n}, alpha={alpha}, m={m}, {n_instances} instances...")

    # Collect thermodynamics across instances
    all_thermo = []

    for inst in range(n_instances):
        if class_name == 'Horn-SAT':
            clauses = gen_horn(n, m)
        elif class_name == '2-SAT':
            clauses = gen_random_ksat(n, m, 2)
        elif class_name == '3-SAT':
            clauses = gen_random_ksat(n, m, 3)
        elif class_name == 'NAE-3-SAT':
            clauses = gen_random_ksat(n, m, 3)
        else:
            raise ValueError(f"Unknown class: {class_name}")

        viol_mode = 'nae' if class_name == 'NAE-3-SAT' else 'sat'
        violations = compute_violation_spectrum(clauses, n, mode=viol_mode)
        thermo = compute_thermodynamics(violations, betas)
        all_thermo.append(thermo)

    # Aggregate: compute median and mean of each quantity at each beta
    aggregated = {}
    for beta in betas:
        agg = {}
        for key in ['Z', 'log_Z', 'F', 'E_mean', 'E_var', 'C', 'chi', 'S']:
            vals = [t[beta][key] for t in all_thermo]
            vals_clean = [v for v in vals if not math.isnan(v) and not math.isinf(v)]
            if vals_clean:
                vals_clean.sort()
                median = vals_clean[len(vals_clean) // 2]
                mean = sum(vals_clean) / len(vals_clean)
                std = math.sqrt(sum((v - mean)**2 for v in vals_clean) / len(vals_clean))
            else:
                median = mean = std = 0.0
            agg[key] = {'median': median, 'mean': mean, 'std': std}
        aggregated[beta] = agg

    return aggregated, all_thermo


def main():
    print("=" * 72)
    print("A6: KMS PHASE TRANSITION -- CSP PARTITION FUNCTION ANALYSIS")
    print("=" * 72)

    all_results = {}

    # =====================================================================
    # PART 1-4: Main computation for all classes at n=10,12
    # =====================================================================

    for n in N_VALUES_MAIN:
        print(f"\n--- n = {n} (2^{n} = {2**n} configurations) ---")
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            alpha = ALPHA_BY_CLASS[cls]
            agg, raw = run_class(cls, n, alpha, N_INSTANCES, BETA_VALUES)
            key = f"{cls}_n{n}"
            all_results[key] = {
                'class': cls,
                'n': n,
                'alpha': alpha,
                'aggregated': agg,
            }

    # =====================================================================
    # PART 6: Finite-size scaling for 3-SAT
    # =====================================================================

    print(f"\n--- Finite-size scaling for 3-SAT ---")
    fss_results = {}
    for n in N_VALUES_FSS:
        alpha = ALPHA_BY_CLASS['3-SAT']
        agg, raw = run_class('3-SAT', n, alpha, N_INSTANCES, BETA_VALUES)
        fss_results[n] = agg

    # =====================================================================
    # ANALYSIS
    # =====================================================================

    print("\n" + "=" * 72)
    print("ANALYSIS")
    print("=" * 72)

    # ---- Table 1: Z(beta) for each class at n=12 ----
    print("\n--- Table 1: Partition function Z(beta) at n=12 ---")
    print(f"{'beta':>8}", end="")
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        print(f"  {cls:>14}", end="")
    print()
    for beta in BETA_VALUES:
        print(f"{beta:8.2f}", end="")
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n12"
            Z = all_results[key]['aggregated'][beta]['log_Z']['median']
            print(f"  {Z:14.4f}", end="")
        print()

    # ---- Table 2: Specific heat C(beta) ----
    print("\n--- Table 2: Specific heat C(beta) at n=12 ---")
    print(f"{'beta':>8}", end="")
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        print(f"  {cls:>14}", end="")
    print()
    for beta in BETA_VALUES:
        print(f"{beta:8.2f}", end="")
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n12"
            C = all_results[key]['aggregated'][beta]['C']['median']
            print(f"  {C:14.6f}", end="")
        print()

    # ---- Table 3: Susceptibility chi(beta) ----
    print("\n--- Table 3: Susceptibility chi(beta) at n=12 ---")
    print(f"{'beta':>8}", end="")
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        print(f"  {cls:>14}", end="")
    print()
    for beta in BETA_VALUES:
        print(f"{beta:8.2f}", end="")
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n12"
            chi = all_results[key]['aggregated'][beta]['chi']['median']
            print(f"  {chi:14.6f}", end="")
        print()

    # ---- Peak analysis ----
    print("\n--- Peak analysis ---")
    peak_data = {}
    for n in N_VALUES_MAIN:
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n{n}"
            agg = all_results[key]['aggregated']

            # Specific heat peak
            C_vals = [agg[b]['C']['median'] for b in BETA_VALUES]
            C_peak = find_peak(BETA_VALUES, C_vals)

            # Susceptibility peak (chi = variance, which is monotonic in beta
            # but C = beta^2 * chi may have a peak)
            chi_vals = [agg[b]['chi']['median'] for b in BETA_VALUES]
            chi_peak = find_peak(BETA_VALUES, chi_vals)

            peak_data[key] = {
                'C_peak': C_peak,
                'chi_peak': chi_peak,
            }

            complexity = 'P' if cls in ['2-SAT', 'Horn-SAT'] else 'NPC'
            print(f"\n{cls} (n={n}, {complexity}):")
            print(f"  C(beta) peak: beta_c = {C_peak['beta_c']}, "
                  f"height = {C_peak['peak_height']:.6f}, "
                  f"FWHM = {C_peak['fwhm']}")
            print(f"  chi(beta) peak: beta_c = {chi_peak['beta_c']}, "
                  f"height = {chi_peak['peak_height']:.6f}, "
                  f"FWHM = {chi_peak['fwhm']}")

    # ---- Peak comparison: P vs NPC ----
    print("\n--- Critical test: P vs NPC separation ---")
    print(f"\n{'Class':>14} {'Type':>5} {'n':>4}  {'C_peak_beta':>12} {'C_peak_ht':>12} "
          f"{'C_FWHM':>10} {'chi_peak_beta':>14} {'chi_peak_ht':>14}")

    for n in N_VALUES_MAIN:
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n{n}"
            cpeak = peak_data[key]['C_peak']
            xpeak = peak_data[key]['chi_peak']
            complexity = 'P' if cls in ['2-SAT', 'Horn-SAT'] else 'NPC'

            bc = cpeak['beta_c'] if cpeak['beta_c'] is not None else 'None'
            ch = cpeak['peak_height']
            fw = cpeak['fwhm'] if cpeak['fwhm'] is not None else 'None'
            xbc = xpeak['beta_c'] if xpeak['beta_c'] is not None else 'None'
            xch = xpeak['peak_height']

            print(f"{cls:>14} {complexity:>5} {n:>4}  {str(bc):>12} {ch:>12.6f} "
                  f"{str(fw):>10} {str(xbc):>14} {xch:>14.6f}")

    # ---- Sharpness metric ----
    print("\n--- Sharpness metric: peak_height / FWHM ---")
    for n in N_VALUES_MAIN:
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n{n}"
            cpeak = peak_data[key]['C_peak']
            complexity = 'P' if cls in ['2-SAT', 'Horn-SAT'] else 'NPC'
            if cpeak['fwhm'] and cpeak['fwhm'] > 0:
                sharpness = cpeak['peak_height'] / cpeak['fwhm']
            else:
                sharpness = float('inf')
            print(f"  {cls:>14} n={n} ({complexity}): sharpness = {sharpness:.6f}")

    # ---- Finite-size scaling ----
    print("\n--- Finite-size scaling: 3-SAT C(beta) peak vs n ---")
    fss_peaks = {}
    for n in N_VALUES_FSS:
        agg = fss_results[n]
        C_vals = [agg[b]['C']['median'] for b in BETA_VALUES]
        peak = find_peak(BETA_VALUES, C_vals)
        fss_peaks[n] = peak
        print(f"  n={n}: beta_c = {peak['beta_c']}, "
              f"peak_height = {peak['peak_height']:.6f}, "
              f"FWHM = {peak['fwhm']}")

    # Check scaling
    heights = [fss_peaks[n]['peak_height'] for n in N_VALUES_FSS]
    if heights[0] > 0 and heights[-1] > 0:
        ratio = heights[-1] / heights[0]
        n_ratio = N_VALUES_FSS[-1] / N_VALUES_FSS[0]
        # If peak ~ n^alpha, then alpha = log(height_ratio) / log(n_ratio)
        if ratio > 0:
            scaling_exp = math.log(ratio) / math.log(n_ratio)
        else:
            scaling_exp = 0
        print(f"\n  Peak height ratio (n={N_VALUES_FSS[-1]}/n={N_VALUES_FSS[0]}): "
              f"{ratio:.4f}")
        print(f"  Effective scaling exponent alpha (C_max ~ n^alpha): {scaling_exp:.4f}")
        if scaling_exp > 0.3:
            print(f"  --> GROWING peak: suggests genuine phase transition")
        elif scaling_exp < -0.3:
            print(f"  --> SHRINKING peak: crossover, not phase transition")
        else:
            print(f"  --> MARGINAL scaling: inconclusive at these sizes")
    else:
        scaling_exp = None
        print("  Could not determine scaling (zero peak heights)")

    # ---- KMS connection: S(beta=1) ----
    print("\n--- KMS connection: entropy S(beta=1) at the BC critical point ---")
    print(f"\n{'Class':>14} {'Type':>5}", end="")
    for n in N_VALUES_MAIN:
        print(f"  {'S(1) n='+str(n):>14}", end="")
    print()

    kms_data = {}
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        complexity = 'P' if cls in ['2-SAT', 'Horn-SAT'] else 'NPC'
        print(f"{cls:>14} {complexity:>5}", end="")
        s_vals = []
        for n in N_VALUES_MAIN:
            key = f"{cls}_n{n}"
            S = all_results[key]['aggregated'][1.0]['S']['median']
            s_vals.append(S)
            print(f"  {S:14.6f}", end="")
        print()
        kms_data[cls] = s_vals

    # Normalized entropy per variable
    print(f"\n{'Class':>14} {'Type':>5}", end="")
    for n in N_VALUES_MAIN:
        print(f"  {'S(1)/n n='+str(n):>14}", end="")
    print()
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        complexity = 'P' if cls in ['2-SAT', 'Horn-SAT'] else 'NPC'
        print(f"{cls:>14} {complexity:>5}", end="")
        for i, n in enumerate(N_VALUES_MAIN):
            s_per_n = kms_data[cls][i] / n
            print(f"  {s_per_n:14.6f}", end="")
        print()

    # ---- Detailed C(beta) curves for visual comparison ----
    print("\n--- Full C(beta) curves at n=12 ---")
    print(f"{'beta':>8}", end="")
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        print(f"  {cls:>14}", end="")
    print()
    for beta in BETA_VALUES:
        print(f"{beta:8.2f}", end="")
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n12"
            C = all_results[key]['aggregated'][beta]['C']['median']
            print(f"  {C:14.6f}", end="")
        print()

    # ---- Additional diagnostic: E(beta) curves ----
    print("\n--- Energy <violations>(beta) at n=12 ---")
    print(f"{'beta':>8}", end="")
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        print(f"  {cls:>14}", end="")
    print()
    for beta in BETA_VALUES:
        print(f"{beta:8.2f}", end="")
        for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
            key = f"{cls}_n12"
            E = all_results[key]['aggregated'][beta]['E_mean']['median']
            print(f"  {E:14.6f}", end="")
        print()

    # ---- Compute additional diagnostics ----

    # Ratio of C_peak for NPC / P at each n
    print("\n--- NPC/P peak height ratios ---")
    for n in N_VALUES_MAIN:
        for p_cls in ['2-SAT', 'Horn-SAT']:
            for npc_cls in ['3-SAT', 'NAE-3-SAT']:
                p_key = f"{p_cls}_n{n}"
                npc_key = f"{npc_cls}_n{n}"
                p_h = peak_data[p_key]['C_peak']['peak_height']
                npc_h = peak_data[npc_key]['C_peak']['peak_height']
                if p_h > 0:
                    ratio = npc_h / p_h
                else:
                    ratio = float('inf')
                print(f"  n={n}: C_peak({npc_cls}) / C_peak({p_cls}) = {ratio:.4f}")

    # ---- Entropy analysis at beta = 1 ----
    print("\n--- Entropy S(1) statistical separation ---")
    p_entropies_12 = []
    npc_entropies_12 = []
    for cls in ['2-SAT', 'Horn-SAT']:
        key = f"{cls}_n12"
        p_entropies_12.append(all_results[key]['aggregated'][1.0]['S']['mean'])
    for cls in ['3-SAT', 'NAE-3-SAT']:
        key = f"{cls}_n12"
        npc_entropies_12.append(all_results[key]['aggregated'][1.0]['S']['mean'])

    p_mean = sum(p_entropies_12) / len(p_entropies_12)
    npc_mean = sum(npc_entropies_12) / len(npc_entropies_12)
    print(f"  P-time mean S(1) at n=12:  {p_mean:.6f}")
    print(f"  NPC mean S(1) at n=12:     {npc_mean:.6f}")
    print(f"  Ratio NPC/P:               {npc_mean/p_mean:.6f}" if p_mean > 0 else "  P-time entropy is zero")

    # ---- Final detailed per-instance analysis: distribution of C_peak ----
    print("\n--- Per-instance C(beta) peak distribution at n=12 ---")
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        complexity = 'P' if cls in ['2-SAT', 'Horn-SAT'] else 'NPC'
        alpha = ALPHA_BY_CLASS[cls]
        n = 12
        m = int(alpha * n)

        # Re-run to collect per-instance peaks
        random.seed(42)
        inst_peaks = []
        for inst in range(N_INSTANCES):
            if cls == 'Horn-SAT':
                clauses = gen_horn(n, m)
            elif cls == '2-SAT':
                clauses = gen_random_ksat(n, m, 2)
            elif cls == '3-SAT':
                clauses = gen_random_ksat(n, m, 3)
            elif cls == 'NAE-3-SAT':
                clauses = gen_random_ksat(n, m, 3)

            viol_mode = 'nae' if cls == 'NAE-3-SAT' else 'sat'
            violations = compute_violation_spectrum(clauses, n, mode=viol_mode)
            thermo = compute_thermodynamics(violations, BETA_VALUES)
            C_vals = [thermo[b]['C'] for b in BETA_VALUES]
            peak = find_peak(BETA_VALUES, C_vals)
            inst_peaks.append(peak)

        heights = [p['peak_height'] for p in inst_peaks]
        betas_c = [p['beta_c'] for p in inst_peaks if p['beta_c'] is not None]
        fwhms = [p['fwhm'] for p in inst_peaks if p['fwhm'] is not None and p['fwhm'] > 0]

        mean_h = sum(heights) / len(heights) if heights else 0
        std_h = math.sqrt(sum((h - mean_h)**2 for h in heights) / len(heights)) if heights else 0

        beta_hist = defaultdict(int)
        for bc in betas_c:
            beta_hist[bc] += 1

        print(f"\n  {cls} ({complexity}):")
        print(f"    Peak height: mean = {mean_h:.6f}, std = {std_h:.6f}")
        if fwhms:
            print(f"    FWHM: mean = {sum(fwhms)/len(fwhms):.6f}")
        print(f"    Peak location histogram:")
        for bc in sorted(beta_hist.keys()):
            print(f"      beta_c = {bc:6.2f}: {beta_hist[bc]} / {N_INSTANCES} instances")

    # =====================================================================
    # VERDICT
    # =====================================================================

    print("\n" + "=" * 72)
    print("VERDICT")
    print("=" * 72)

    # Collect key metrics for the verdict
    # 1. Do NPC classes have sharper peaks than P?
    n12_sharpness = {}
    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        key = f"{cls}_n12"
        cpeak = peak_data[key]['C_peak']
        if cpeak['fwhm'] and cpeak['fwhm'] > 0:
            n12_sharpness[cls] = cpeak['peak_height'] / cpeak['fwhm']
        else:
            n12_sharpness[cls] = cpeak['peak_height']  # use raw height if FWHM undefined

    p_sharp = max(n12_sharpness.get('2-SAT', 0), n12_sharpness.get('Horn-SAT', 0))
    npc_sharp = min(n12_sharpness.get('3-SAT', 0), n12_sharpness.get('NAE-3-SAT', 0))

    # 2. Do peaks grow with n for NPC?
    fss_growing = False
    if len(fss_peaks) >= 2:
        h8 = fss_peaks.get(8, {}).get('peak_height', 0)
        h12 = fss_peaks.get(12, {}).get('peak_height', 0)
        if h8 > 0:
            fss_growing = (h12 / h8) > 1.1  # more than 10% growth

    # 3. Does S(1) separate P from NPC?
    s1_separates = False
    p_s1 = []
    npc_s1 = []
    for cls in ['2-SAT', 'Horn-SAT']:
        key = f"{cls}_n12"
        p_s1.append(all_results[key]['aggregated'][1.0]['S']['mean'] / 12)
    for cls in ['3-SAT', 'NAE-3-SAT']:
        key = f"{cls}_n12"
        npc_s1.append(all_results[key]['aggregated'][1.0]['S']['mean'] / 12)

    # Check if ranges are disjoint
    if min(p_s1) > max(npc_s1) or max(p_s1) < min(npc_s1):
        s1_separates = True

    # 4. Does beta_c differ between P and NPC?
    p_betas = []
    npc_betas = []
    for cls in ['2-SAT', 'Horn-SAT']:
        key = f"{cls}_n12"
        bc = peak_data[key]['C_peak']['beta_c']
        if bc is not None:
            p_betas.append(bc)
    for cls in ['3-SAT', 'NAE-3-SAT']:
        key = f"{cls}_n12"
        bc = peak_data[key]['C_peak']['beta_c']
        if bc is not None:
            npc_betas.append(bc)

    beta_c_separates = False
    if p_betas and npc_betas:
        if min(p_betas) > max(npc_betas) or max(p_betas) < min(npc_betas):
            beta_c_separates = True

    print("\nTest 1: NPC peaks sharper than P peaks?")
    print(f"  P sharpness (max):   {p_sharp:.6f}")
    print(f"  NPC sharpness (min): {npc_sharp:.6f}")
    if npc_sharp > p_sharp * 1.5:
        print(f"  --> YES: NPC is {npc_sharp/p_sharp:.2f}x sharper")
        test1 = True
    else:
        print(f"  --> NO: ratio = {npc_sharp/p_sharp:.4f}" if p_sharp > 0 else "  --> INCONCLUSIVE")
        test1 = False

    print(f"\nTest 2: 3-SAT C_peak grows with n (finite-size scaling)?")
    if fss_growing:
        print(f"  --> YES: peak grows from n=8 to n=12")
        if scaling_exp is not None:
            print(f"  Scaling exponent: {scaling_exp:.4f}")
        test2 = True
    else:
        print(f"  --> NO: peak does not grow significantly")
        test2 = False

    print(f"\nTest 3: S(beta=1)/n separates P from NPC?")
    print(f"  P range:   [{min(p_s1):.6f}, {max(p_s1):.6f}]")
    print(f"  NPC range: [{min(npc_s1):.6f}, {max(npc_s1):.6f}]")
    if s1_separates:
        print(f"  --> YES: ranges are disjoint")
        test3 = True
    else:
        print(f"  --> NO: ranges overlap")
        test3 = False

    print(f"\nTest 4: beta_c location separates P from NPC?")
    if p_betas and npc_betas:
        print(f"  P beta_c:   {p_betas}")
        print(f"  NPC beta_c: {npc_betas}")
    if beta_c_separates:
        print(f"  --> YES: locations are disjoint")
        test4 = True
    else:
        print(f"  --> NO: locations overlap")
        test4 = False

    n_pass = sum([test1, test2, test3, test4])
    print(f"\n{'='*72}")
    if n_pass >= 3:
        verdict = "PASS"
        print(f"OVERALL VERDICT: **PASS** ({n_pass}/4 tests positive)")
        print("The phase transition structure of Z_Gamma(beta) shows signatures")
        print("that distinguish P-time from NPC complexity classes.")
    elif n_pass >= 2:
        verdict = "PARTIAL"
        print(f"OVERALL VERDICT: **PARTIAL** ({n_pass}/4 tests positive)")
        print("Some phase transition signatures distinguish P from NPC,")
        print("but the evidence is not conclusive at these system sizes.")
    else:
        verdict = "FAIL"
        print(f"OVERALL VERDICT: **FAIL** ({n_pass}/4 tests positive)")
        print("The phase transition structure does NOT clearly separate")
        print("P-time from NPC at these system sizes.")

    print("\nNote: these are small systems (n<=12). The conjecture concerns")
    print("the thermodynamic limit n -> infinity. Finite-size effects may")
    print("mask the true asymptotic behavior.")
    print("=" * 72)

    # =====================================================================
    # SAVE JSON data
    # =====================================================================

    save_data = {
        'parameters': {
            'betas': BETA_VALUES,
            'n_values_main': N_VALUES_MAIN,
            'n_values_fss': N_VALUES_FSS,
            'n_instances': N_INSTANCES,
            'alpha_by_class': ALPHA_BY_CLASS,
        },
        'peak_analysis': {},
        'fss_peaks': {},
        'kms_entropy': {},
        'verdict': verdict,
        'test_results': {
            'test1_sharpness': test1,
            'test2_fss_growing': test2,
            'test3_s1_separation': test3,
            'test4_beta_c_separation': test4,
        },
    }

    for key, pd_item in peak_data.items():
        save_data['peak_analysis'][key] = {
            'C_peak': {k: (v if v is not None else 'null') for k, v in pd_item['C_peak'].items()},
            'chi_peak': {k: (v if v is not None else 'null') for k, v in pd_item['chi_peak'].items()},
        }

    for n_val, pk in fss_peaks.items():
        save_data['fss_peaks'][str(n_val)] = {k: (v if v is not None else 'null') for k, v in pk.items()}

    for cls in ['2-SAT', 'Horn-SAT', '3-SAT', 'NAE-3-SAT']:
        save_data['kms_entropy'][cls] = {}
        for n in N_VALUES_MAIN:
            key = f"{cls}_n{n}"
            save_data['kms_entropy'][cls][str(n)] = {
                'S': all_results[key]['aggregated'][1.0]['S']['mean'],
                'S_per_n': all_results[key]['aggregated'][1.0]['S']['mean'] / n,
            }

    # Save aggregated thermodynamic data
    save_data['thermodynamics'] = {}
    for key in all_results:
        save_data['thermodynamics'][key] = {}
        agg = all_results[key]['aggregated']
        for beta in BETA_VALUES:
            save_data['thermodynamics'][key][str(beta)] = {
                q: agg[beta][q]['median'] for q in ['log_Z', 'E_mean', 'E_var', 'C', 'chi', 'S']
            }

    json_path = '/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/code/results_a6_phase_transition.json'
    with open(json_path, 'w') as f:
        json.dump(save_data, f, indent=2, default=str)
    print(f"\nJSON data saved to {json_path}")

    return save_data, all_results, peak_data, fss_peaks, n12_sharpness


if __name__ == '__main__':
    save_data, all_results, peak_data, fss_peaks, n12_sharpness = main()
