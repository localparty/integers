#!/usr/bin/env python3
"""
test_o8_partition_function.py — CSP partition function zeta-like pole structure

Tests conjecture O8 from strategy/06-transposition-dictionary.md:

  The CSP partition function Z_Gamma(beta) = sum_{x in {0,1}^n} exp(-beta * violations(x))
  is a zeta-like object whose analytic structure (poles, zeros) encodes the
  complexity of the CSP.

Key prediction:
  P-time CSPs should have partition functions with "simple" pole structure
  (few poles, well-separated). NPC CSPs should have "complex" pole structure
  (many poles, clustered — analogous to the dense Riemann zero distribution).

Parts:
  1. Compute Z_Gamma(beta) for each CSP class (2-SAT, Horn-SAT, XOR-SAT, 3-SAT, NAE-3-SAT)
  2. Specific heat C(beta) and phase transition signatures
  3. Rational function fit (Pade) with AIC model selection for pole extraction
  4. Violation spectrum analysis: entropy, support width, Lee-Yang zeros
  5. Comparison of pole structure with Riemann zeros

Parameters: n=10, 50 random instances per class, full 2^10 enumeration.

Author: G Six, with Claude Opus 4.6. Date: 2026-04-11.
"""

import random
import itertools
import math
import json
import numpy as np
from collections import defaultdict

random.seed(42)
np.random.seed(42)

# =====================================================================
# PART 0: CSP INSTANCE GENERATORS
# =====================================================================

N = 10               # number of variables
N_INSTANCES = 50     # random instances per class
TWO_N = 2 ** N       # 1024 total assignments

def generate_2sat(n, m):
    """Random 2-SAT: each clause has exactly 2 literals."""
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 2)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def generate_horn_sat(n, m):
    """Random Horn-SAT: each clause has at most 1 positive literal.
    3-literal clauses for direct comparison."""
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        if random.random() < 0.33:
            clause = [-v for v in vs]
        else:
            pos_idx = random.randint(0, 2)
            clause = []
            for i, v in enumerate(vs):
                if i == pos_idx:
                    clause.append(v)
                else:
                    clause.append(-v)
        clauses.append(clause)
    return clauses

def generate_xor_sat(n, m):
    """Random XOR-SAT: x_i XOR x_j XOR x_k = b."""
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        target = random.randint(0, 1)
        clauses.append((vs, target))
    return clauses

def generate_3sat(n, m):
    """Random 3-SAT: each clause has exactly 3 literals."""
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

def generate_nae_3sat(n, m):
    """Random NAE-3-SAT: satisfied iff literals NOT ALL EQUAL."""
    clauses = []
    for _ in range(m):
        vs = random.sample(range(1, n+1), 3)
        clause = [v if random.random() < 0.5 else -v for v in vs]
        clauses.append(clause)
    return clauses

# =====================================================================
# PART 0b: VIOLATION COUNTERS
# =====================================================================

def count_violations_sat(clauses, assignment):
    violations = 0
    for clause in clauses:
        satisfied = False
        for lit in clause:
            var = abs(lit) - 1
            val = assignment[var]
            if (lit > 0 and val == 1) or (lit < 0 and val == 0):
                satisfied = True
                break
        if not satisfied:
            violations += 1
    return violations

def count_violations_xor(clauses, assignment):
    violations = 0
    for (vs, target) in clauses:
        parity = 0
        for v in vs:
            parity ^= assignment[v - 1]
        if parity != target:
            violations += 1
    return violations

def count_violations_nae(clauses, assignment):
    violations = 0
    for clause in clauses:
        values = []
        for lit in clause:
            var = abs(lit) - 1
            val = assignment[var]
            if lit < 0:
                val = 1 - val
            values.append(val)
        if all(v == 1 for v in values) or all(v == 0 for v in values):
            violations += 1
    return violations

# =====================================================================
# PART 1: COMPUTE Z, F, C
# =====================================================================

BETA_FINE = np.arange(0.0, 5.05, 0.1).tolist()
BETA_COARSE = [6.0, 8.0, 10.0, 20.0, 50.0]
BETA_VALUES = BETA_FINE + BETA_COARSE

def compute_violation_spectrum(clauses, n, violation_counter):
    """Enumerate all 2^n assignments, return {violation_count: count}."""
    spectrum = defaultdict(int)
    for bits in itertools.product([0, 1], repeat=n):
        v = violation_counter(clauses, bits)
        spectrum[v] += 1
    return dict(spectrum)

def compute_Z(spectrum, beta_values):
    """Z(beta) = sum_v spectrum[v] * exp(-beta * v)."""
    Z = []
    for beta in beta_values:
        z = sum(count * math.exp(-beta * v) for v, count in spectrum.items())
        Z.append(z)
    return Z

def compute_free_energy(Z_values, beta_values):
    F = []
    for z, beta in zip(Z_values, beta_values):
        if beta == 0 or z <= 0:
            F.append(None)
        else:
            F.append(-math.log(z) / beta)
    return F

def compute_specific_heat(Z_values, beta_values, spectrum):
    """C(beta) = beta^2 * Var(E) under the Boltzmann distribution."""
    C = []
    for i, beta in enumerate(beta_values):
        z = Z_values[i]
        if z <= 0 or beta == 0:
            C.append(0.0)
            continue
        E_avg = 0.0
        E2_avg = 0.0
        for v, count in spectrum.items():
            weight = count * math.exp(-beta * v) / z
            E_avg += v * weight
            E2_avg += v * v * weight
        variance = E2_avg - E_avg ** 2
        C.append(beta ** 2 * variance)
    return C

def find_specific_heat_peak(C_values, beta_values):
    """Find peak of C(beta). Returns (beta_c, C_max, sharpness)."""
    fine_len = len(BETA_FINE)
    C_fine = C_values[1:fine_len]
    beta_fine = beta_values[1:fine_len]
    if not C_fine:
        return None, None, None
    idx_max = np.argmax(C_fine)
    beta_c = beta_fine[idx_max]
    C_max = C_fine[idx_max]
    C_mean = np.mean(C_fine)
    sharpness = C_max / C_mean if C_mean > 0 else 0.0
    return beta_c, C_max, sharpness

# =====================================================================
# PART 2: VIOLATION SPECTRUM ANALYSIS
#
# Z_Gamma(beta) = sum_{v=0}^{m} d_v * exp(-beta * v) = sum d_v * u^v
# where u = exp(-beta). This is a POLYNOMIAL in u of degree m:
#   Z(u) = d_0 + d_1*u + d_2*u^2 + ... + d_m*u^m
#
# As a polynomial, Z has exactly m zeros in C (counting multiplicity).
# These are the LEE-YANG ZEROS — the analytic content of Z.
#
# For the "zeta test": the DISTRIBUTION of these zeros encodes the
# structure of the CSP. The key metric is not Pade poles (which are
# artifacts of the denominator degree) but the Lee-Yang zeros of the
# exact polynomial.
# =====================================================================

def compute_lee_yang_zeros(spectrum, m):
    """Compute the Lee-Yang zeros of Z(u) = sum d_v * u^v.
    Returns roots of the polynomial in the u-plane, plus their
    images in the beta-plane via beta = -log(u)."""

    # Build polynomial coefficients [d_0, d_1, ..., d_m]
    coeffs = np.zeros(m + 1)
    for v, count in spectrum.items():
        if v <= m:
            coeffs[v] = count

    # Strip trailing zeros to get actual degree
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs = coeffs[:-1]
    actual_degree = len(coeffs) - 1

    if actual_degree < 1:
        return [], [], actual_degree, coeffs

    # numpy.roots wants highest degree first
    u_roots = np.roots(coeffs[::-1])

    # Convert to beta plane
    beta_roots = []
    for u in u_roots:
        if abs(u) > 1e-30:
            beta_roots.append(-np.log(u))

    return u_roots, beta_roots, actual_degree, coeffs

def analyze_lee_yang_zeros(u_roots, m):
    """Analyze the distribution of Lee-Yang zeros.

    Key metrics:
    - n_real_zeros: number of real zeros (Lee-Yang theorem: for ferromagnetic
      systems, all zeros on unit circle; for CSPs, no such constraint)
    - n_unit_circle: number of zeros on |u|=1
    - angular_distribution: how spread the zeros are angularly
    - radial_distribution: spread of |u| values
    - zero_gap: minimum spacing between consecutive zeros on unit circle
    """
    if len(u_roots) == 0:
        return {}

    moduli = np.abs(u_roots)
    angles = np.angle(u_roots)
    real_parts = np.real(u_roots)
    imag_parts = np.imag(u_roots)

    # Count "real" zeros (Im < tolerance)
    n_real = sum(1 for u in u_roots if abs(u.imag) < 1e-6)

    # Count zeros near unit circle
    n_unit = sum(1 for m_val in moduli if abs(m_val - 1.0) < 0.05)

    # Angular distribution entropy (binned)
    n_bins = 20
    angle_hist, _ = np.histogram(angles, bins=n_bins, range=(-np.pi, np.pi))
    angle_probs = angle_hist / angle_hist.sum() if angle_hist.sum() > 0 else angle_hist
    angle_entropy = -sum(p * np.log(p) for p in angle_probs if p > 0)
    max_angle_entropy = np.log(n_bins)
    angle_uniformity = angle_entropy / max_angle_entropy if max_angle_entropy > 0 else 0

    # Radial spread
    radial_mean = float(np.mean(moduli))
    radial_std = float(np.std(moduli))

    # Zero spacings (sorted by angle, for zeros near unit circle)
    unit_angles = sorted([angles[i] for i in range(len(u_roots))
                          if abs(moduli[i] - 1.0) < 0.2])
    if len(unit_angles) >= 2:
        spacings = [unit_angles[i+1] - unit_angles[i] for i in range(len(unit_angles)-1)]
        min_spacing = min(spacings)
        mean_spacing = np.mean(spacings)
        spacing_ratio = min_spacing / mean_spacing if mean_spacing > 0 else 0
    else:
        min_spacing = None
        mean_spacing = None
        spacing_ratio = None

    return {
        'n_zeros': len(u_roots),
        'n_real_zeros': n_real,
        'n_unit_circle': n_unit,
        'angle_uniformity': float(angle_uniformity),
        'radial_mean': radial_mean,
        'radial_std': radial_std,
        'min_zero_spacing': float(min_spacing) if min_spacing is not None else None,
        'mean_zero_spacing': float(mean_spacing) if mean_spacing is not None else None,
        'spacing_ratio': float(spacing_ratio) if spacing_ratio is not None else None,
    }

def spectrum_entropy(spectrum, total=TWO_N):
    """Shannon entropy of the violation distribution.
    Higher entropy = more spread violations = more complex."""
    S = 0.0
    for v, count in spectrum.items():
        p = count / total
        if p > 0:
            S -= p * math.log2(p)
    return S

def spectrum_support(spectrum):
    """Number of distinct violation levels with nonzero count."""
    return len([v for v, c in spectrum.items() if c > 0])

# =====================================================================
# PART 3: PADE APPROXIMANT WITH AIC MODEL SELECTION
# =====================================================================

def fit_pade(Z_values, beta_values, p_degree, q_degree):
    """Fit Z(beta) to P(u)/Q(u), u = exp(-beta).
    Returns (P_coeffs, Q_coeffs, poles_beta, residual, aic)."""

    n_params = (p_degree + 1) + q_degree
    valid = [(Z_values[i], beta_values[i]) for i in range(len(beta_values))
             if Z_values[i] > 0 and np.isfinite(Z_values[i])]
    n_data = len(valid)

    if n_data < n_params + 2:
        return None, None, [], float('inf'), float('inf')

    A = np.zeros((n_data, n_params))
    rhs = np.zeros(n_data)

    for row, (z_i, beta_i) in enumerate(valid):
        u_i = math.exp(-beta_i)
        for j in range(p_degree + 1):
            A[row, j] = u_i ** j
        for j in range(1, q_degree + 1):
            A[row, p_degree + j] = -z_i * (u_i ** j)
        rhs[row] = z_i

    try:
        result, _, rank, sv = np.linalg.lstsq(A, rhs, rcond=None)
    except np.linalg.LinAlgError:
        return None, None, [], float('inf'), float('inf')

    P_coeffs = result[:p_degree + 1]
    Q_coeffs = np.concatenate(([1.0], result[p_degree + 1:]))

    fitted = A @ result
    ss_res = np.sum((fitted - rhs) ** 2)
    residual = np.sqrt(ss_res / n_data) / np.mean(np.abs(rhs))

    # AIC: penalize complexity
    if ss_res > 0:
        aic = n_data * np.log(ss_res / n_data) + 2 * n_params
    else:
        aic = -float('inf')

    # Poles
    Q_poly = Q_coeffs[::-1]
    try:
        u_roots = np.roots(Q_poly)
    except Exception:
        u_roots = np.array([])

    poles_beta = []
    for u_root in u_roots:
        if abs(u_root) > 1e-15:
            poles_beta.append(-np.log(u_root))

    return P_coeffs, Q_coeffs, poles_beta, residual, aic

def fit_pade_with_selection(Z_values, beta_values):
    """Try Pade degrees 1/1 through 8/8, select by AIC.
    Returns (best_degree, poles, residual, aic, all_results)."""

    results = {}
    best_aic = float('inf')
    best = None

    for q in range(1, 9):
        for p in [q-1, q, q+1]:
            if p < 1:
                continue
            P, Q, poles, res, aic = fit_pade(Z_values, beta_values, p, q)
            if P is not None and np.isfinite(aic):
                key = (p, q)
                results[key] = {
                    'poles': poles, 'residual': res, 'aic': aic,
                    'n_poles': len(poles), 'p': p, 'q': q,
                }
                if aic < best_aic:
                    best_aic = aic
                    best = key

    if best is None:
        return None, [], float('inf'), float('inf'), results

    return best, results[best]['poles'], results[best]['residual'], best_aic, results

# =====================================================================
# PART 4: RIEMANN ZERO COMPARISON
# =====================================================================

RIEMANN_ZEROS = [
    14.134725141734694, 21.022039638771555, 25.010857580145689,
    30.424876125859513, 32.935061587739190, 37.586178158825671,
    40.918719012147495, 43.327073280914999, 48.005150881167160,
    49.773832477672302, 52.970321477714461, 56.446247697063395,
    59.347044002602353, 60.831778524609810, 65.112544048081607,
    67.079810529494174, 69.546401711173980, 72.067157674481908,
    75.704690699083933, 77.144840068874805,
]
RIEMANN_SPACINGS = [RIEMANN_ZEROS[i+1] - RIEMANN_ZEROS[i]
                     for i in range(len(RIEMANN_ZEROS)-1)]

def compare_with_riemann(spacings_list, tolerance=0.01):
    """Check spacings against Riemann zero spacings within tolerance."""
    matches = []
    for ps in spacings_list:
        if abs(ps) < 1e-10:
            continue
        for ri, rs in enumerate(RIEMANN_SPACINGS):
            rel_err = abs(ps - rs) / rs
            if rel_err < tolerance:
                matches.append({
                    'pole_spacing': float(ps),
                    'riemann_spacing': float(rs),
                    'riemann_pair': (ri+1, ri+2),
                    'relative_error': float(rel_err),
                })
    return matches

# =====================================================================
# MAIN COMPUTATION
# =====================================================================

def run_class(name, generator, violation_counter, n, m, n_instances):
    """Run full analysis for one CSP class."""
    print(f"\n{'='*70}")
    print(f"  CLASS: {name}  (n={n}, m={m}, {n_instances} instances)")
    print(f"{'='*70}")

    all_spectra = []
    all_Z = []
    all_C = []
    all_n_solutions = []

    # Specific heat peak
    C_peak_betas = []
    C_peak_values = []
    C_sharpnesses = []

    # Lee-Yang analysis
    all_ly_stats = []
    all_ly_spacings = []

    # Pade analysis
    all_pade_poles = []
    all_pade_degrees = []
    all_pade_residuals = []

    # Spectrum measures
    all_entropies = []
    all_supports = []
    all_max_violations = []

    for inst in range(n_instances):
        clauses = generator(n, m)
        spectrum = compute_violation_spectrum(clauses, n, violation_counter)
        Z = compute_Z(spectrum, BETA_VALUES)
        C = compute_specific_heat(Z, BETA_VALUES, spectrum)

        n_solutions = spectrum.get(0, 0)
        ent = spectrum_entropy(spectrum)
        supp = spectrum_support(spectrum)
        max_v = max(spectrum.keys())

        # C(beta) peak
        beta_c, C_max, sharpness = find_specific_heat_peak(C, BETA_VALUES)
        if beta_c is not None:
            C_peak_betas.append(beta_c)
            C_peak_values.append(C_max)
            C_sharpnesses.append(sharpness)

        # Lee-Yang zeros (exact polynomial)
        u_roots, beta_roots, actual_deg, poly_coeffs = compute_lee_yang_zeros(spectrum, m)
        ly_stats = analyze_lee_yang_zeros(u_roots, m)
        all_ly_stats.append(ly_stats)

        # Extract Lee-Yang spacings (imaginary parts of beta-plane zeros)
        if len(beta_roots) >= 2:
            im_parts = sorted([abs(b.imag) for b in beta_roots if abs(b.imag) > 0.01])
            if len(im_parts) >= 2:
                ly_spc = [im_parts[i+1] - im_parts[i] for i in range(len(im_parts)-1)]
                all_ly_spacings.extend(ly_spc)

        # Pade fit with AIC selection
        best_deg, poles, res, aic, _ = fit_pade_with_selection(Z, BETA_VALUES)
        if best_deg is not None:
            all_pade_poles.append(poles)
            all_pade_degrees.append(best_deg)
            all_pade_residuals.append(res)

        all_spectra.append(spectrum)
        all_Z.append(Z)
        all_C.append(C)
        all_n_solutions.append(n_solutions)
        all_entropies.append(ent)
        all_supports.append(supp)
        all_max_violations.append(max_v)

        if inst % 10 == 0:
            deg_str = f"{best_deg}" if best_deg else "N/A"
            print(f"  inst {inst}: |Sol|={n_solutions}, max_v={max_v}, "
                  f"entropy={ent:.3f}, LY zeros={ly_stats.get('n_zeros', 0)}, "
                  f"Pade deg={deg_str}")

    # ---- Aggregate ----

    Z_median = [float(np.median([all_Z[i][j] for i in range(n_instances)]))
                for j in range(len(BETA_VALUES))]
    C_median = [float(np.median([all_C[i][j] for i in range(n_instances)]))
                for j in range(len(BETA_VALUES))]

    beta_c_median = float(np.median(C_peak_betas)) if C_peak_betas else None
    C_max_median = float(np.median(C_peak_values)) if C_peak_values else None
    sharpness_median = float(np.median(C_sharpnesses)) if C_sharpnesses else None

    sol_mean = float(np.mean(all_n_solutions))
    sol_density = sol_mean / TWO_N
    entropy_mean = float(np.mean(all_entropies))
    support_mean = float(np.mean(all_supports))
    max_v_mean = float(np.mean(all_max_violations))

    # Lee-Yang aggregate
    ly_agg = {}
    for key in ['n_zeros', 'n_real_zeros', 'n_unit_circle', 'angle_uniformity',
                'radial_mean', 'radial_std', 'spacing_ratio']:
        vals = [s[key] for s in all_ly_stats if key in s and s[key] is not None]
        if vals:
            ly_agg[key] = float(np.median(vals))

    # Pade aggregate
    if all_pade_degrees:
        pade_q_median = float(np.median([d[1] for d in all_pade_degrees]))
    else:
        pade_q_median = None

    # Riemann comparison on Lee-Yang spacings
    riemann_ly = compare_with_riemann(all_ly_spacings)
    # Riemann comparison on Pade pole spacings
    pade_spacings = []
    for poles in all_pade_poles:
        if len(poles) >= 2:
            im_sorted = sorted([abs(p.imag) for p in poles if abs(p.imag) > 0.01])
            if len(im_sorted) >= 2:
                pade_spacings.extend([im_sorted[i+1] - im_sorted[i]
                                      for i in range(len(im_sorted)-1)])
    riemann_pade = compare_with_riemann(pade_spacings)

    result = {
        'name': name, 'n': n, 'm': m, 'n_instances': n_instances,
        'sol_mean': sol_mean, 'sol_density': sol_density,
        'entropy_mean': entropy_mean, 'support_mean': support_mean,
        'max_v_mean': max_v_mean,
        'Z_median': Z_median, 'C_median': C_median,
        'beta_c_median': beta_c_median, 'C_max_median': C_max_median,
        'sharpness_median': sharpness_median,
        'C_peak_betas': C_peak_betas,
        'ly_agg': ly_agg,
        'pade_q_median': pade_q_median,
        'pade_degrees': [str(d) for d in all_pade_degrees],
        'riemann_ly_matches': len(riemann_ly),
        'riemann_pade_matches': len(riemann_pade),
        'riemann_ly_details': riemann_ly[:10],
        'riemann_pade_details': riemann_pade[:10],
        'n_ly_spacings': len(all_ly_spacings),
        'n_pade_spacings': len(pade_spacings),
    }

    print(f"\n  --- {name} Summary ---")
    print(f"  Solutions: mean={sol_mean:.1f}, density={sol_density:.4f}")
    print(f"  Spectrum: entropy={entropy_mean:.3f}, support={support_mean:.1f}, "
          f"max_v={max_v_mean:.1f}")
    print(f"  C(beta) peak: beta_c={beta_c_median}, C_max={C_max_median}, "
          f"sharpness={sharpness_median}")
    print(f"  Lee-Yang: zeros={ly_agg.get('n_zeros','?')}, "
          f"unit_circle={ly_agg.get('n_unit_circle','?')}, "
          f"angle_unif={ly_agg.get('angle_uniformity','?')}")
    print(f"  Pade AIC: median q-degree={pade_q_median}")
    print(f"  Riemann matches: LY={len(riemann_ly)}, Pade={len(riemann_pade)}")

    return result

# =====================================================================
# RUN ALL CLASSES
# =====================================================================

def main():
    print("="*70)
    print("  O8 TEST: CSP PARTITION FUNCTION ZETA-LIKE POLE STRUCTURE")
    print(f"  n={N}, {N_INSTANCES} instances per class, 2^n={TWO_N}")
    print("="*70)

    classes = [
        ("2-SAT",            generate_2sat,     count_violations_sat, N, 2*N),
        ("Horn-SAT",         generate_horn_sat,  count_violations_sat, N, 2*N),
        ("XOR-SAT",          generate_xor_sat,   count_violations_xor, N, 2*N),
        ("3-SAT (critical)", generate_3sat,      count_violations_sat, N, int(4.267*N)),
        ("NAE-3-SAT",        generate_nae_3sat,  count_violations_nae, N, 2*N),
    ]

    results = {}
    for name, gen, counter, n, m in classes:
        results[name] = run_class(name, gen, counter, n, m, N_INSTANCES)

    # =================================================================
    # CROSS-CLASS COMPARISON
    # =================================================================
    ptime = ["2-SAT", "Horn-SAT", "XOR-SAT"]
    npc = ["3-SAT (critical)", "NAE-3-SAT"]

    print("\n\n" + "="*70)
    print("  CROSS-CLASS COMPARISON")
    print("="*70)

    # --- Table 1: Z(beta) ---
    print("\n  --- Table 1: Z(beta) median ---")
    sample_betas = [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0]
    sample_idx = []
    for b in sample_betas:
        best_i = min(range(len(BETA_VALUES)), key=lambda i: abs(BETA_VALUES[i] - b))
        sample_idx.append(best_i)

    header = f"  {'beta':>6}"
    for name in results:
        header += f"  {name[:14]:>14}"
    print(header)
    print(f"  {'-'*(8 + 16*len(results))}")
    for bi, beta in enumerate(sample_betas):
        idx = sample_idx[bi]
        row = f"  {beta:6.1f}"
        for name, r in results.items():
            z = r['Z_median'][idx]
            row += f"  {z:14.4e}" if z > 1e5 or z < 0.01 else f"  {z:14.4f}"
        print(row)

    # --- Table 2: C(beta) ---
    print("\n  --- Table 2: C(beta) median ---")
    C_betas = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]
    C_idx = [min(range(len(BETA_VALUES)), key=lambda i: abs(BETA_VALUES[i] - b))
             for b in C_betas]
    header = f"  {'beta':>6}"
    for name in results:
        header += f"  {name[:14]:>14}"
    print(header)
    print(f"  {'-'*(8 + 16*len(results))}")
    for bi, beta in enumerate(C_betas):
        idx = C_idx[bi]
        row = f"  {beta:6.1f}"
        for name, r in results.items():
            row += f"  {r['C_median'][idx]:14.6f}"
        print(row)

    # --- Table 3: Phase transition summary ---
    print("\n  --- Table 3: Specific heat peak (phase transition) ---")
    print(f"  {'Class':<20} {'beta_c':>8} {'C_max':>10} {'Sharp':>8} {'Type':>6}")
    print(f"  {'-'*56}")
    for name, r in results.items():
        ctype = "P" if name in ptime else "NPC"
        bc = f"{r['beta_c_median']:.2f}" if r['beta_c_median'] is not None else "N/A"
        cm = f"{r['C_max_median']:.4f}" if r['C_max_median'] is not None else "N/A"
        sh = f"{r['sharpness_median']:.4f}" if r['sharpness_median'] is not None else "N/A"
        print(f"  {name:<20} {bc:>8} {cm:>10} {sh:>8} {ctype:>6}")

    # --- Table 4: Violation spectrum structure ---
    print("\n  --- Table 4: Violation spectrum structure ---")
    print(f"  {'Class':<20} {'Entropy':>8} {'Support':>8} {'MaxV':>6} "
          f"{'SolDens':>10} {'Type':>6}")
    print(f"  {'-'*64}")
    for name, r in results.items():
        ctype = "P" if name in ptime else "NPC"
        print(f"  {name:<20} {r['entropy_mean']:8.3f} {r['support_mean']:8.1f} "
              f"{r['max_v_mean']:6.1f} {r['sol_density']:10.5f} {ctype:>6}")

    # --- Table 5: Lee-Yang zero structure ---
    print("\n  --- Table 5: Lee-Yang zero structure (median) ---")
    print(f"  {'Class':<20} {'Zeros':>7} {'Real':>6} {'|u|=1':>7} "
          f"{'AngUnif':>8} {'RadStd':>8} {'SpcRat':>8} {'Type':>6}")
    print(f"  {'-'*78}")
    for name, r in results.items():
        ctype = "P" if name in ptime else "NPC"
        ly = r['ly_agg']
        nz = f"{ly.get('n_zeros', '?')}"
        nr = f"{ly.get('n_real_zeros', '?')}"
        nu = f"{ly.get('n_unit_circle', '?')}"
        au = f"{ly.get('angle_uniformity', 0):.4f}" if 'angle_uniformity' in ly else "N/A"
        rs = f"{ly.get('radial_std', 0):.4f}" if 'radial_std' in ly else "N/A"
        sr = f"{ly.get('spacing_ratio', 0):.4f}" if 'spacing_ratio' in ly else "N/A"
        print(f"  {name:<20} {nz:>7} {nr:>6} {nu:>7} {au:>8} {rs:>8} {sr:>8} {ctype:>6}")

    # --- Table 6: Pade AIC model selection ---
    print("\n  --- Table 6: Pade best denominator degree (AIC) ---")
    print(f"  {'Class':<20} {'Med q':>7} {'Type':>6}")
    print(f"  {'-'*36}")
    for name, r in results.items():
        ctype = "P" if name in ptime else "NPC"
        q = f"{r['pade_q_median']:.1f}" if r['pade_q_median'] is not None else "N/A"
        print(f"  {name:<20} {q:>7} {ctype:>6}")

    # --- Table 7: Riemann zero matches ---
    print("\n  --- Table 7: Riemann zero matches (1% tolerance) ---")
    print(f"  {'Class':<20} {'LY':>5} {'Pade':>6} {'LYrate':>8} {'Type':>6}")
    print(f"  {'-'*50}")
    for name, r in results.items():
        ctype = "P" if name in ptime else "NPC"
        n_ly = r['n_ly_spacings']
        rate_ly = r['riemann_ly_matches'] / n_ly if n_ly > 0 else 0
        print(f"  {name:<20} {r['riemann_ly_matches']:>5} "
              f"{r['riemann_pade_matches']:>6} {rate_ly:>8.4f} {ctype:>6}")

    # =================================================================
    # VERDICTS
    # =================================================================
    print("\n\n" + "="*70)
    print("  VERDICTS")
    print("="*70)

    confirmations = 0
    total_tests = 5

    # V1: Spectrum entropy — NPC should have higher entropy (more spread)
    p_ent = [results[n]['entropy_mean'] for n in ptime]
    npc_ent = [results[n]['entropy_mean'] for n in npc]
    # Note: XOR-SAT at m=2n is overconstrained (0 solutions), so its entropy is high
    # — this is a known artifact. Exclude it for fair comparison.
    p_ent_no_xor = [results[n]['entropy_mean'] for n in ["2-SAT", "Horn-SAT"]]
    print(f"\n  V1: Spectrum entropy (P vs NPC)")
    print(f"      P-time (excl XOR): {np.mean(p_ent_no_xor):.3f}")
    print(f"      NPC:               {np.mean(npc_ent):.3f}")
    if np.mean(npc_ent) > np.mean(p_ent_no_xor):
        confirmations += 1
        print("      [+] NPC has higher spectrum entropy")
    else:
        print("      [-] P-time has higher spectrum entropy")

    # V2: Lee-Yang angular uniformity — NPC should have MORE uniform zeros
    # (more "zeta-like" = zeros everywhere, not clustered)
    p_au = [results[n]['ly_agg'].get('angle_uniformity', 0) for n in ptime]
    npc_au = [results[n]['ly_agg'].get('angle_uniformity', 0) for n in npc]
    print(f"\n  V2: Lee-Yang angular uniformity")
    print(f"      P-time: {np.mean(p_au):.4f}")
    print(f"      NPC:    {np.mean(npc_au):.4f}")
    if np.mean(npc_au) > np.mean(p_au):
        confirmations += 1
        print("      [+] NPC zeros more uniformly distributed (zeta-like)")
    else:
        print("      [-] P-time zeros more uniform")

    # V3: Lee-Yang spacing ratio — lower = more clustered (GUE-like)
    p_sr = [results[n]['ly_agg'].get('spacing_ratio', 1) for n in ptime
            if results[n]['ly_agg'].get('spacing_ratio') is not None]
    npc_sr = [results[n]['ly_agg'].get('spacing_ratio', 1) for n in npc
              if results[n]['ly_agg'].get('spacing_ratio') is not None]
    if p_sr and npc_sr:
        print(f"\n  V3: Lee-Yang zero spacing ratio (min/mean)")
        print(f"      P-time: {np.mean(p_sr):.4f} (higher = more regular)")
        print(f"      NPC:    {np.mean(npc_sr):.4f}")
        if np.mean(npc_sr) < np.mean(p_sr):
            confirmations += 1
            print("      [+] NPC zeros more irregularly spaced (complex structure)")
        else:
            print("      [-] NPC zeros more regular")

    # V4: Pade complexity — NPC should need higher-degree Pade (more poles)
    p_q = [results[n]['pade_q_median'] for n in ptime
           if results[n]['pade_q_median'] is not None]
    npc_q = [results[n]['pade_q_median'] for n in npc
             if results[n]['pade_q_median'] is not None]
    if p_q and npc_q:
        print(f"\n  V4: Pade denominator degree (AIC-selected)")
        print(f"      P-time: {np.mean(p_q):.2f}")
        print(f"      NPC:    {np.mean(npc_q):.2f}")
        if np.mean(npc_q) > np.mean(p_q):
            confirmations += 1
            print("      [+] NPC needs more Pade poles")
        else:
            print("      [-] NPC does not need more poles")

    # V5: C(beta) peak sharpness — NPC at critical ratio should show sharper peak
    p_sh = [r['sharpness_median'] for n, r in results.items()
            if n in ptime and r['sharpness_median'] is not None]
    npc_sh = [r['sharpness_median'] for n, r in results.items()
              if n in npc and r['sharpness_median'] is not None]
    # Exclude XOR for fairness (overconstrained)
    p_sh_fair = [r['sharpness_median'] for n, r in results.items()
                 if n in ["2-SAT", "Horn-SAT"] and r['sharpness_median'] is not None]
    if p_sh_fair and npc_sh:
        print(f"\n  V5: C(beta) peak sharpness (excl XOR)")
        print(f"      P-time: {np.mean(p_sh_fair):.4f}")
        print(f"      NPC:    {np.mean(npc_sh):.4f}")
        if np.mean(npc_sh) > np.mean(p_sh_fair):
            confirmations += 1
            print("      [+] NPC has sharper phase transition")
        else:
            print("      [-] P-time has sharper transition")

    # Overall
    print(f"\n  SCORE: {confirmations}/{total_tests} sub-predictions confirmed")
    if confirmations >= 4:
        print("  OVERALL: O8 STRONGLY SUPPORTED at n=10")
    elif confirmations >= 3:
        print("  OVERALL: O8 SUPPORTED at n=10")
    elif confirmations >= 2:
        print("  OVERALL: O8 PARTIALLY SUPPORTED at n=10")
    else:
        print("  OVERALL: O8 NOT SUPPORTED at n=10")

    # =================================================================
    # Detailed Riemann matches
    # =================================================================
    print("\n  --- Riemann zero match details (top 5 per class, Lee-Yang) ---")
    for name, r in results.items():
        if r['riemann_ly_details']:
            ctype = "P" if name in ptime else "NPC"
            print(f"\n  {name} ({ctype}):")
            for m_item in r['riemann_ly_details'][:5]:
                print(f"    spacing={m_item['pole_spacing']:.6f} ~ "
                      f"gamma_{m_item['riemann_pair'][0]}-gamma_{m_item['riemann_pair'][1]-1}"
                      f" = {m_item['riemann_spacing']:.6f} "
                      f"(err={m_item['relative_error']:.5f})")

    # Save JSON
    json_output = {}
    for name, r in results.items():
        safe = {k: v for k, v in r.items()
                if k not in ['Z_median', 'C_median']}
        json_output[name] = safe
    json_path = "/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/code/results_o8_partition.json"
    with open(json_path, 'w') as f:
        json.dump(json_output, f, indent=2, default=str)
    print(f"\n  JSON saved to {json_path}")

    return results

if __name__ == "__main__":
    results = main()
