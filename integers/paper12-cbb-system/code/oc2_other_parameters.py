#!/usr/bin/env python3
"""
OC-2 Riemann-Zero Parameter Search
===================================

Test whether other physical parameters in the QG5D framework follow the same
Riemann-zero structure as the cosmological constant:

    log(π × R_obs / l_P) = γ_1 × π² / 2  (verified: 0.014% precision)

Parameters to test:
1. Ω_DM / Ω_b ≈ 5.36 (dark matter to baryon ratio)
2. ξ = T_hidden/T_visible ≈ 0.432 (mirror brane temperature ratio)
3. N_eff ≈ 3.31-3.39 (effective neutrino species)
4. Weinberg angle: sin²θ_W ≈ 0.232
5. Fine structure constant: α ≈ 1/137.036
6. Proton mass / electron mass: m_p/m_e ≈ 1836.15
7. Higgs mass / top mass: m_H/m_t ≈ 0.728
8. Lepton mass ratios: m_τ/m_μ ≈ 16.82, m_μ/m_e ≈ 206.77
9. String tension √σ ≈ 437 MeV
10. The 17 in n_2/n_1 = -17/9 (GUT flux quantization)

Automated search: enumerate combinations of:
- γ_1, γ_2, γ_3, γ_4, γ_5 (first 5 Riemann zeros)
- π, e, γ_E (Euler-Mascheroni)
- ζ(2), ζ(3), ζ(4), ζ(5), ζ(-1), ζ(-3)
- Square roots, logs, simple ratios

Report matches with precision better than 1%.
"""

import mpmath as mp
import numpy as np
from itertools import combinations_with_replacement, permutations
import json

# High precision
mp.dps = 50

# Physical constants and parameters
PARAMS = {
    'omega_dm_b': (5.36, "Ω_DM/Ω_b (dark matter to baryon ratio)"),
    'xi': (0.432, "ξ = T_hidden/T_visible"),
    'N_eff_lower': (3.31, "N_eff (lower bound)"),
    'N_eff_upper': (3.39, "N_eff (upper bound)"),
    'N_eff_mid': (3.35, "N_eff (midpoint)"),
    'sin2_theta_W': (0.232, "sin²θ_W (Weinberg angle)"),
    'alpha_inv': (137.036, "1/α (fine structure constant)"),
    'm_p_m_e': (1836.15, "m_p/m_e"),
    'm_H_m_t': (0.728, "m_H/m_t"),
    'm_tau_m_mu': (16.82, "m_τ/m_μ"),
    'm_mu_m_e': (206.77, "m_μ/m_e"),
    'sqrt_sigma': (437.0, "√σ (string tension, MeV)"),
    'gut_ratio_num': (17.0, "17 (from n_2/n_1 = -17/9)"),
    'gut_ratio_denom': (9.0, "9 (from n_2/n_1 = -17/9)"),
}

# Riemann zeros (first 5)
def get_riemann_zeros(n):
    """Compute the first n non-trivial Riemann zeros."""
    zeros = []
    for i in range(1, n + 1):
        # Use mpmath's zetazero function
        z = mp.zetazero(i)
        zeros.append(z)
    return zeros

# Constants
def get_constants():
    return {
        'pi': mp.pi,
        'e': mp.e,
        'gamma_E': mp.euler,  # Euler-Mascheroni constant
    }

# Zeta function values
def get_zeta_values():
    return {
        'zeta_2': mp.zeta(2),
        'zeta_3': mp.zeta(3),
        'zeta_4': mp.zeta(4),
        'zeta_5': mp.zeta(5),
        'zeta_minus1': mp.zeta(-1),
        'zeta_minus3': mp.zeta(-3),
    }

def test_formula(param_value, param_name, gamma_vals, const_vals, zeta_vals):
    """
    Test various formula combinations against a parameter value.
    
    Formula types to search:
    1. P = γ_n × (geometric constant) + (correction)
    2. P = exp(γ_n × π / k)
    3. P = ζ(n) × (function of γ_k)
    4. P = (combination of γ_1, γ_2, π, e, ζ values)
    """
    
    matches = []
    tolerance = 0.01  # 1% precision threshold
    
    param_log = mp.log(mp.mpf(param_value))
    param_inv = mp.mpf(1) / mp.mpf(param_value)
    param_inv_log = mp.log(param_inv)
    
    # Type 1: P = γ_n × C (simple scalar multiple)
    for i, gamma in enumerate(gamma_vals):
        for const_name, const_val in const_vals.items():
            for zeta_name, zeta_val in zeta_vals.items():
                # Try: P = gamma × zeta × const
                formula_val = gamma * zeta_val * const_val
                error = abs((formula_val - param_value) / param_value)
                if error < tolerance:
                    matches.append({
                        'type': 'simple_product',
                        'formula': f'γ_{i+1} × {zeta_name} × {const_name}',
                        'expected': float(param_value),
                        'computed': float(formula_val),
                        'error_pct': float(error * 100),
                    })
                
                # Try: P = gamma / zeta / const
                if zeta_val != 0 and const_val != 0:
                    formula_val = gamma / (zeta_val * const_val)
                    error = abs((formula_val - param_value) / param_value)
                    if error < tolerance:
                        matches.append({
                            'type': 'simple_quotient',
                            'formula': f'γ_{i+1} / ({zeta_name} × {const_name})',
                            'expected': float(param_value),
                            'computed': float(formula_val),
                            'error_pct': float(error * 100),
                        })
    
    # Type 2: log(P) = γ_n × C
    for i, gamma in enumerate(gamma_vals):
        for const_name, const_val in const_vals.items():
            for zeta_name, zeta_val in zeta_vals.items():
                # Try: log(P) = γ × π² / 2, etc.
                formula_val = gamma * const_val ** 2 / zeta_val
                error = abs((formula_val - param_log) / param_log) if param_log != 0 else abs(formula_val)
                if error < tolerance and param_log != 0:
                    matches.append({
                        'type': 'logarithmic',
                        'formula': f'log(P) = γ_{i+1} × {const_name}² / {zeta_name}',
                        'expected': float(param_log),
                        'computed': float(formula_val),
                        'error_pct': float(error * 100),
                        'implies_P': float(mp.exp(formula_val)),
                    })
    
    # Type 3: P = exp(γ_n × C)
    for i, gamma in enumerate(gamma_vals):
        for const_name, const_val in const_vals.items():
            # Try: P = exp(γ × π / k) for small integer k
            for k in [1, 2, 3, 4, 5]:
                formula_val = mp.exp(gamma * const_val / k)
                error = abs((formula_val - param_value) / param_value)
                if error < tolerance:
                    matches.append({
                        'type': 'exponential',
                        'formula': f'exp(γ_{i+1} × {const_name} / {k})',
                        'expected': float(param_value),
                        'computed': float(formula_val),
                        'error_pct': float(error * 100),
                    })
    
    # Type 4: Ratios and combinations
    for i, gamma_i in enumerate(gamma_vals):
        for j, gamma_j in enumerate(gamma_vals):
            if i < j:
                # Try γ_i / γ_j
                formula_val = gamma_i / gamma_j
                error = abs((formula_val - param_value) / param_value)
                if error < tolerance:
                    matches.append({
                        'type': 'zero_ratio',
                        'formula': f'γ_{i+1} / γ_{j+1}',
                        'expected': float(param_value),
                        'computed': float(formula_val),
                        'error_pct': float(error * 100),
                    })
    
    # Type 5: Multiple zero combinations
    for i, gamma_i in enumerate(gamma_vals[:3]):  # Limit to first 3 for speed
        for j, gamma_j in enumerate(gamma_vals[:3]):
            if i != j:
                # Try γ_i × γ_j / constant
                for const_name, const_val in list(const_vals.items())[:2]:
                    formula_val = (gamma_i * gamma_j) / const_val
                    error = abs((formula_val - param_value) / param_value)
                    if error < tolerance:
                        matches.append({
                            'type': 'multi_zero',
                            'formula': f'γ_{i+1} × γ_{j+1} / {const_name}',
                            'expected': float(param_value),
                            'computed': float(formula_val),
                            'error_pct': float(error * 100),
                        })
    
    return matches

def main():
    print("=" * 80)
    print("OC-2 Riemann-Zero Parameter Search")
    print("=" * 80)
    print()
    
    # Compute Riemann zeros
    print("Computing first 5 Riemann zeros...")
    gamma_vals = get_riemann_zeros(5)
    print(f"γ_1 = {gamma_vals[0]}")
    print(f"γ_2 = {gamma_vals[1]}")
    print(f"γ_3 = {gamma_vals[2]}")
    print(f"γ_4 = {gamma_vals[3]}")
    print(f"γ_5 = {gamma_vals[4]}")
    print()
    
    const_vals = get_constants()
    zeta_vals = get_zeta_values()
    
    print("Constants:")
    for name, val in const_vals.items():
        print(f"  {name} = {val}")
    print()
    
    print("Zeta values:")
    for name, val in zeta_vals.items():
        print(f"  {name} = {val}")
    print()
    
    # Test each parameter
    results = {}
    
    for param_key, (param_val, param_desc) in PARAMS.items():
        print(f"\nTesting: {param_desc}")
        print(f"  Value: {param_val}")
        
        matches = test_formula(param_val, param_desc, gamma_vals, const_vals, zeta_vals)
        
        if matches:
            print(f"  Found {len(matches)} match(es):")
            for match in matches:
                print(f"    {match['formula']}")
                print(f"      Expected: {match['expected']:.6e}, Computed: {match['computed']:.6e}")
                print(f"      Error: {match['error_pct']:.3f}%")
        else:
            print(f"  No matches found (< 1% precision)")
        
        results[param_key] = {
            'value': param_val,
            'description': param_desc,
            'matches': matches,
        }
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    fitted_params = [k for k, v in results.items() if v['matches']]
    unfitted_params = [k for k, v in results.items() if not v['matches']]
    
    print(f"\nParameters that FIT a Riemann formula ({len(fitted_params)}):")
    for param_key in fitted_params:
        matches = results[param_key]['matches']
        print(f"  {param_key}: {len(matches)} formula(s)")
        best = min(matches, key=lambda m: m['error_pct'])
        print(f"    Best: {best['formula']} ({best['error_pct']:.3f}% error)")
    
    print(f"\nParameters that DON'T fit ({len(unfitted_params)}):")
    for param_key in unfitted_params:
        print(f"  {param_key}: {results[param_key]['description']}")
    
    # Save detailed results
    with open('/Users/gsix/quantum-geometry-in-5d-latex/next-frontier/code/oc2_results.json', 'w') as f:
        json.dump({
            'gamma_zeros': [str(g) for g in gamma_vals],
            'fitted_count': len(fitted_params),
            'unfitted_count': len(unfitted_params),
            'results': {k: {
                'value': v['value'],
                'description': v['description'],
                'matches': v['matches']
            } for k, v in results.items()}
        }, f, indent=2)
    
    print("\nDetailed results saved to: oc2_results.json")

if __name__ == '__main__':
    main()
