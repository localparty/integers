#!/usr/bin/env python3
"""
Refined OC-2 Riemann-Zero Parameter Search
============================================

Use the verified formula structure as a template:
    log(π × R_obs / l_P) = γ_1 × π² / 2

Test analogs for other parameters:
    log(P × k) = γ_n × (zeta/algebraic)
    P = (expression in γ_k, π, e, ζ)^(power)
    P = γ_i / γ_j (zero ratios)
    etc.

Focus on:
- Logarithmic relations
- Power laws in Riemann zeros
- Ratios of zeros
- Products with π, e, ζ
"""

import mpmath as mp
import numpy as np

# High precision
mp.dps = 50

PARAMS = {
    'omega_dm_b': (5.36, "Ω_DM/Ω_b"),
    'xi': (0.432, "ξ"),
    'N_eff': (3.35, "N_eff"),
    'sin2_theta_W': (0.232, "sin²θ_W"),
    'alpha_inv': (137.036, "1/α"),
    'm_p_m_e': (1836.15, "m_p/m_e"),
    'm_H_m_t': (0.728, "m_H/m_t"),
    'm_tau_m_mu': (16.82, "m_τ/m_μ"),
    'm_mu_m_e': (206.77, "m_μ/m_e"),
    'sqrt_sigma': (437.0, "√σ"),
    '17': (17.0, "17"),
    '9': (9.0, "9"),
}

def get_riemann_zeros(n):
    """First n Riemann zeros (just the imaginary part)."""
    return [mp.zetazero(i).imag for i in range(1, n + 1)]

def extract_log_structure(param_val, param_name):
    """
    For each parameter, try to find a log-based formula.
    Templates:
    1. log(P) = γ_n × π² / k
    2. log(P) = γ_n × ζ(2) × k
    3. log(P) = γ_n / γ_m
    4. log(P + c) = γ_n × something
    """
    matches = []
    
    gamma = get_riemann_zeros(5)
    pi = mp.pi
    e = mp.e
    gamma_E = mp.euler
    zeta_2 = mp.zeta(2)
    zeta_3 = mp.zeta(3)
    
    param = mp.mpf(param_val)
    
    # Template 1: log(P) = γ_n × π² / k
    log_param = mp.log(param)
    for k in range(1, 6):
        for i in range(5):
            formula_val = gamma[i] * pi ** 2 / k
            if abs(formula_val - log_param) < 0.1:
                error = abs(formula_val - log_param) / abs(log_param) if log_param != 0 else abs(formula_val)
                matches.append({
                    'type': 'log_template1',
                    'formula': f'log(P) = γ_{i+1} × π² / {k}',
                    'expected': float(param),
                    'computed': float(mp.exp(formula_val)),
                    'log_error': float(abs(formula_val - log_param)),
                    'error_pct': float(error * 100) if log_param != 0 else float(abs(formula_val)),
                })
    
    # Template 2: log(P) = γ_n × ζ(2) × k
    for k in range(1, 6):
        for i in range(5):
            formula_val = gamma[i] * zeta_2 * k
            if abs(formula_val - log_param) < 0.1:
                error = abs(formula_val - log_param) / abs(log_param) if log_param != 0 else abs(formula_val)
                matches.append({
                    'type': 'log_template2',
                    'formula': f'log(P) = γ_{i+1} × ζ(2) × {k}',
                    'expected': float(param),
                    'computed': float(mp.exp(formula_val)),
                    'log_error': float(abs(formula_val - log_param)),
                    'error_pct': float(error * 100) if log_param != 0 else float(abs(formula_val)),
                })
    
    # Template 3: log(P) = γ_i / γ_j
    for i in range(3):
        for j in range(3):
            if i != j:
                formula_val = gamma[i] / gamma[j]
                if abs(formula_val - log_param) < 0.1:
                    error = abs(formula_val - log_param) / abs(log_param) if log_param != 0 else abs(formula_val)
                    matches.append({
                        'type': 'log_zero_ratio',
                        'formula': f'log(P) = γ_{i+1} / γ_{j+1}',
                        'expected': float(param),
                        'computed': float(mp.exp(formula_val)),
                        'log_error': float(abs(formula_val - log_param)),
                        'error_pct': float(error * 100) if log_param != 0 else float(abs(formula_val)),
                    })
    
    return matches

def direct_formula_search(param_val, param_name):
    """
    Direct formula matching (not logarithmic).
    """
    matches = []
    tolerance = 0.01  # 1% tolerance
    
    gamma = get_riemann_zeros(5)
    pi = mp.pi
    e = mp.e
    gamma_E = mp.euler
    zeta_2 = mp.zeta(2)
    zeta_3 = mp.zeta(3)
    
    param = mp.mpf(param_val)
    
    # Test zero ratios: P = γ_i / γ_j
    for i in range(5):
        for j in range(5):
            if i != j:
                formula_val = gamma[i] / gamma[j]
                error = abs(formula_val - param) / param
                if error < tolerance:
                    matches.append({
                        'type': 'zero_ratio',
                        'formula': f'γ_{i+1} / γ_{j+1}',
                        'expected': float(param),
                        'computed': float(formula_val),
                        'error_pct': float(error * 100),
                    })
    
    # Test products: P = γ_i × (constant)
    for i in range(5):
        for const_name, const_val in [('π', pi), ('e', e), ('ζ(2)', zeta_2), ('ζ(3)', zeta_3)]:
            formula_val = gamma[i] * const_val
            error = abs(formula_val - param) / param
            if error < tolerance:
                matches.append({
                    'type': 'zero_times_const',
                    'formula': f'γ_{i+1} × {const_name}',
                    'expected': float(param),
                    'computed': float(formula_val),
                    'error_pct': float(error * 100),
                })
            
            # Also try division
            if const_val != 0:
                formula_val = gamma[i] / const_val
                error = abs(formula_val - param) / param
                if error < tolerance:
                    matches.append({
                        'type': 'zero_div_const',
                        'formula': f'γ_{i+1} / {const_name}',
                        'expected': float(param),
                        'computed': float(formula_val),
                        'error_pct': float(error * 100),
                    })
    
    # Test power relations: P = γ^k
    for k_num in range(1, 6):
        for k_denom in range(1, 6):
            power = mp.mpf(k_num) / mp.mpf(k_denom)
            for i in range(5):
                formula_val = gamma[i] ** power
                error = abs(formula_val - param) / param
                if error < tolerance:
                    matches.append({
                        'type': 'zero_power',
                        'formula': f'γ_{i+1} ^ ({k_num}/{k_denom})',
                        'expected': float(param),
                        'computed': float(formula_val),
                        'error_pct': float(error * 100),
                    })
    
    return matches

def main():
    print("=" * 80)
    print("REFINED OC-2 RIEMANN-ZERO PARAMETER SEARCH")
    print("=" * 80)
    print()
    
    gamma = get_riemann_zeros(5)
    print("First 5 Riemann zeros (imaginary parts):")
    for i, g in enumerate(gamma, 1):
        print(f"  γ_{i} = {g}")
    print()
    
    all_results = {}
    
    # Test each parameter
    for param_key, (param_val, param_desc) in PARAMS.items():
        print(f"\n{'='*80}")
        print(f"Testing: {param_desc} = {param_val}")
        print(f"{'='*80}")
        
        # Direct formula search
        direct_matches = direct_formula_search(param_val, param_desc)
        
        # Logarithmic structure search
        log_matches = extract_log_structure(param_val, param_desc)
        
        all_matches = direct_matches + log_matches
        
        if all_matches:
            print(f"\nFound {len(all_matches)} match(es):")
            # Sort by error
            all_matches.sort(key=lambda m: m['error_pct'])
            for i, match in enumerate(all_matches[:5], 1):  # Show top 5
                print(f"\n  {i}. {match['formula']}")
                print(f"     Type: {match['type']}")
                print(f"     Expected: {match['expected']:.8f}")
                print(f"     Computed: {match['computed']:.8f}")
                print(f"     Error: {match['error_pct']:.4f}%")
        else:
            print("\n  No matches found (< 1% precision)")
        
        all_results[param_key] = {
            'value': param_val,
            'matches': all_matches,
        }
    
    # Final summary
    print("\n" + "=" * 80)
    print("GLOBAL SUMMARY")
    print("=" * 80)
    
    fitted = [k for k, v in all_results.items() if v['matches']]
    unfitted = [k for k, v in all_results.items() if not v['matches']]
    
    print(f"\nFitted parameters: {len(fitted)}")
    if fitted:
        for key in fitted:
            best = min(all_results[key]['matches'], key=lambda m: m['error_pct'])
            print(f"  {key}: {best['formula']} ({best['error_pct']:.4f}%)")
    
    print(f"\nUnfitted parameters: {len(unfitted)}")
    for key in unfitted:
        print(f"  {key}")
    
    # Statistical assessment
    print("\n" + "=" * 80)
    print("STATISTICAL ASSESSMENT: Multiple Comparisons Problem")
    print("=" * 80)
    
    total_tests = len(PARAMS)
    fitted_count = len(fitted)
    
    # Very rough estimate: if we have 5 zeros × 4 constants × 5 powers × 5 combinations = 500+ formulas per param
    # At 1% error tolerance, we'd expect ~5 false positives per parameter by chance
    false_positive_rate = 0.05  # rough estimate
    expected_false_positives = total_tests * false_positive_rate
    
    print(f"\nTotal parameters tested: {total_tests}")
    print(f"Parameters with matches: {fitted_count}")
    print(f"Expected false positives (at ~5% rate): {expected_false_positives:.1f}")
    print(f"\nConclusion: {'STATISTICALLY SIGNIFICANT' if fitted_count > expected_false_positives + 2 else 'Likely noise / coincidence'}")

if __name__ == '__main__':
    main()
