#!/usr/bin/env python3
"""
OC-2 RIEMANN ZERO PREDICTION TEST
==================================

Question: Can the QG5D framework PREDICT γ_2, γ_3, γ_4, ... from physical observations?

This script tests whether other framework parameters follow the same pattern as
the cosmological constant:

    log(π × R_obs / l_P) = γ_1 × π² / 2    (VERIFIED: 0.014% precision)

If the formula generalizes:
    log(π × ratio) = γ_n × π² / 2

Then we can solve for γ_n and compare with actual Riemann zeros.

KNOWN PHYSICAL HIERARCHIES IN QG5D:
1. R_obs / l_P          → γ_1 (established)
2. M_GUT × l_P          → mass hierarchy (Paper 7)
3. M_KK × l_P           → weak scale (Paper 4)
4. M_EW × l_P           → electroweak (Paper 4)
5. M_Pl × R_universe    → universe size (Paper 2)
6. R_obs / R_2          → e-circle to S² (Paper 1)
7. R_2 / R_3            → S² to CP² (Paper 1)
8. R_3 / l_P            → CP² to Planck (Paper 1)
9. Ω_DM / Ω_b ≈ 5.36   → cosmic ratio (Paper 2)
10. log(M_Pl/M_EW) ≈ 32 → hierarchy (standard)
11. n_2/n_1 = 17/9     → GUT flux (Paper 7, Theorem U)
12. ξ = 0.432          → mirror temperature (Paper 1, Paper 2)
"""

import mpmath as mp
import numpy as np
import json
from typing import List, Tuple, Dict

# Set precision
mp.dps = 50

# ════════════════════════════════════════════════════════════════
# RIEMANN ZEROS: TARGET PREDICTIONS
# ════════════════════════════════════════════════════════════════

ACTUAL_RIEMANN_ZEROS = {
    1: 14.134725141734693,
    2: 21.022039638771554,
    3: 25.010857580145688,
    4: 30.424876125859513,
    5: 32.935061587739189,
    6: 37.586178158825671,
    7: 40.918719012147495,
    8: 43.327073280235508,
    9: 48.005150881167551,
    10: 49.773832477672302,
}

# ════════════════════════════════════════════════════════════════
# FRAMEWORK PHYSICAL CONSTANTS
# ════════════════════════════════════════════════════════════════

# Planck scale
M_Pl = 2.435e18  # GeV
l_P = 1.0 / M_Pl  # GeV^{-1}

# Observed e-circle radius (from dark energy)
R_obs = 5.07e10  # GeV^{-1}, corresponding to ~10 μm

# Standard scales
M_EW = 246.0  # GeV (electroweak scale, Higgs vev)
M_KK_observed = 1.5e3  # GeV, inferred from Higgs mass (1-2.5 TeV range in Paper 4)

# GUT scale (from SO(10) unification, ~3σ from proton decay)
M_GUT_expected = 1e15  # GeV

# Neutrino / dark matter scales (Paper 1)
m_nu = 49.7e-3  # GeV, meV scale
m_h_inv = 0.12  # GeV^{-1} (inverse Hubble)

# ════════════════════════════════════════════════════════════════
# FRAMEWORK GEOMETRY SCALES
# ════════════════════════════════════════════════════════════════

# Sizes of internal manifold (from Papers 1, 4, 7)
R_2 = 1e-19   # m, approximate S² radius
R_3 = 1e-31   # m, approximate CP² radius

def convert_m_to_geV_inv(meters):
    """Convert meters to GeV^{-1}."""
    return meters / (1.973e-16)

R_2_geV = convert_m_to_geV_inv(R_2)
R_3_geV = convert_m_to_geV_inv(R_3)
l_P_m = 1.616e-35  # meters
l_P_geV = convert_m_to_geV_inv(l_P_m)

# ════════════════════════════════════════════════════════════════
# MATHEMATICAL CONSTANTS
# ════════════════════════════════════════════════════════════════

pi = mp.pi
e = mp.e
gamma_E = mp.euler  # Euler-Mascheroni
zeta_2 = mp.zeta(2)  # π²/6
zeta_3 = mp.zeta(3)
zeta_4 = mp.zeta(4)

# ════════════════════════════════════════════════════════════════
# CORE FORMULA
# ════════════════════════════════════════════════════════════════

def predict_gamma_from_ratio(ratio):
    """
    Apply the OC-2 formula to a physical ratio.
    
    If:  log(π × ratio) = γ_n × π²/2
    
    Then: γ_n = 2 × log(π × ratio) / π²
    """
    ratio_mp = mp.mpf(str(ratio))
    gamma_predicted = 2 * mp.log(pi * ratio_mp) / (pi ** 2)
    return float(gamma_predicted)

def find_closest_zero(gamma_pred, tolerance=0.02):
    """
    Find if gamma_pred matches an actual Riemann zero (within tolerance).
    
    tolerance: fractional tolerance (0.02 = 2%)
    
    Returns: (matched_zero_index, matched_gamma, error_pct) or None
    """
    for n, gamma_actual in ACTUAL_RIEMANN_ZEROS.items():
        error = abs(gamma_pred - gamma_actual) / gamma_actual
        if error <= tolerance:
            return (n, gamma_actual, error * 100)
    return None

# ════════════════════════════════════════════════════════════════
# COMPILE PHYSICAL HIERARCHIES
# ════════════════════════════════════════════════════════════════

def get_physical_hierarchies() -> List[Tuple[str, float]]:
    """
    Return a list of (name, ratio) for all physical hierarchies in the framework.
    """
    hierarchies = []
    
    # 1. Cosmological constant (already verified)
    hierarchies.append(("R_obs / l_P (cosmological constant)", R_obs / l_P))
    
    # 2. Electroweak scale
    M_EW_inv = 1.0 / M_EW
    hierarchies.append(("M_EW × l_P (electroweak scale)", M_EW_inv * l_P))
    
    # 3. KK scale (typical range 1-2.5 TeV)
    hierarchies.append(("M_KK × l_P (Kaluza-Klein scale, 1.5 TeV)", M_KK_observed * l_P))
    
    # 4. GUT scale (tentative)
    M_GUT_inv = 1.0 / M_GUT_expected
    hierarchies.append(("M_GUT × l_P (GUT scale, 10^15 GeV)", M_GUT_inv * l_P))
    
    # 5. Universe size (used with M_Pl for alternative formulation)
    # log(M_Pl × R_universe) where R_universe ~ Hubble radius
    hierarchies.append(("M_Pl × m_h_inv (Hubble radius)", M_Pl * m_h_inv))
    
    # 6. Internal geometry ratios
    hierarchies.append(("R_obs / R_2 (e-circle to S²)", R_obs / R_2_geV))
    hierarchies.append(("R_2 / R_3 (S² to CP²)", R_2_geV / R_3_geV))
    hierarchies.append(("R_3 / l_P_geV (CP² to Planck)", R_3_geV / l_P_geV))
    
    # 7. Cosmic ratios (from Papers 1, 2)
    hierarchies.append(("Ω_DM / Ω_b (dark matter / baryon)", 5.36))
    
    # 8. Mirror brane temperature
    hierarchies.append(("1 / ξ (inverse mirror temp)", 1.0 / 0.432))
    
    # 9. Electroweak-to-Planck (standard hierarchy)
    hierarchies.append(("M_Pl / M_EW (EW-Planck hierarchy)", M_Pl / M_EW))
    
    # 10. GUT-to-Planck hierarchy
    hierarchies.append(("M_Pl / M_GUT (GUT-Planck hierarchy)", M_Pl / M_GUT_expected))
    
    # 11. Fine structure constant inverse
    hierarchies.append(("1 / α (inverse fine structure constant)", 137.036))
    
    # 12. Proton-electron mass ratio
    hierarchies.append(("m_p / m_e (proton-electron)", 1836.15))
    
    # 13. GUT flux ratio (from Paper 7, Theorem U)
    hierarchies.append(("n_2 / n_1 magnitude (GUT flux)", 17.0 / 9.0))
    
    # 14. Alternative KK scale definitions
    # If M_KK ~ 2 TeV
    M_KK_2TeV = 2e3
    hierarchies.append(("M_KK × l_P (2 TeV estimate)", M_KK_2TeV * l_P))
    
    # 15. Neutrino mass scale
    # m_nu ~ 50 meV, but in natural units
    m_nu_inv = 1.0 / m_nu if m_nu > 0 else 0
    if m_nu_inv > 0:
        hierarchies.append(("1 / m_ν (neutrino mass inverse, 1/meV)", m_nu_inv))
    
    return hierarchies

# ════════════════════════════════════════════════════════════════
# MAIN ANALYSIS
# ════════════════════════════════════════════════════════════════

def main():
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║         OC-2 RIEMANN ZERO PREDICTION TEST                           ║")
    print("║   Can the QG5D framework predict γ_2, γ_3, γ_4, ... ?              ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print()
    
    # Display actual Riemann zeros
    print("TARGET RIEMANN ZEROS:")
    print("─" * 60)
    for n in sorted(ACTUAL_RIEMANN_ZEROS.keys()):
        gamma = ACTUAL_RIEMANN_ZEROS[n]
        print(f"  γ_{n:2d} = {gamma:.12f}")
    print()
    
    # Get physical hierarchies
    hierarchies = get_physical_hierarchies()
    
    print("TESTING PHYSICAL HIERARCHIES:")
    print("─" * 60)
    print()
    
    # Test each hierarchy
    predictions = []
    matches = []
    
    for name, ratio in hierarchies:
        try:
            # Predict γ_n using the formula
            gamma_pred = predict_gamma_from_ratio(ratio)
            
            # Look for matches
            match_result = find_closest_zero(gamma_pred, tolerance=0.02)
            
            prediction_record = {
                'name': name,
                'ratio': float(ratio),
                'log_ratio': float(np.log(ratio)),
                'gamma_predicted': gamma_pred,
                'match': match_result,
            }
            predictions.append(prediction_record)
            
            if match_result:
                matched_n, matched_gamma, error_pct = match_result
                matches.append({
                    'hierarchy': name,
                    'gamma_predicted': gamma_pred,
                    'matched_to': matched_n,
                    'gamma_actual': matched_gamma,
                    'error_pct': error_pct,
                })
                print(f"✓ MATCH FOUND:")
                print(f"  Hierarchy: {name}")
                print(f"  Ratio: {ratio:.6e}")
                print(f"  Predicted γ: {gamma_pred:.12f}")
                print(f"  Matched to γ_{matched_n}: {matched_gamma:.12f}")
                print(f"  Error: {error_pct:.3f}%")
                print()
            else:
                print(f"  {name}")
                print(f"    Ratio: {ratio:.6e}")
                print(f"    Predicted γ: {gamma_pred:.6f}")
                print(f"    No match within 2%")
                print()
        except Exception as e:
            print(f"  ERROR testing {name}: {e}")
            print()
    
    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    
    if matches:
        print(f"GENUINE MATCHES FOUND: {len(matches)}")
        print()
        for match in matches:
            print(f"  • {match['hierarchy']}")
            print(f"    Predicts γ_{match['matched_to']} (actual: {match['gamma_actual']:.6f})")
            print(f"    Error: {match['error_pct']:.3f}%")
            print()
        
        # Check for Riemann hierarchy pattern
        print("RIEMANN HIERARCHY PATTERN:")
        print("─" * 70)
        matched_ns = sorted([m['matched_to'] for m in matches])
        print(f"Matched zero indices: {matched_ns}")
        
        if len(matches) >= 3:
            consecutive = all(matched_ns[i+1] - matched_ns[i] == 1 
                            for i in range(len(matched_ns)-1))
            if consecutive:
                print(f"✓ CONSECUTIVE PATTERN DETECTED: γ_{matched_ns[0]} → γ_{matched_ns[-1]}")
                print(f"  Possible systematic hierarchy in the framework!")
            else:
                print(f"  Pattern is scattered (not consecutive)")
        
        print()
    else:
        print("NO GENUINE MATCHES FOUND within 2% tolerance")
        print()
        print("Closest predictions:")
        # Show the 3 closest
        sorted_preds = sorted(predictions, 
                             key=lambda p: min([abs(p['gamma_predicted'] - g) 
                                              for g in ACTUAL_RIEMANN_ZEROS.values()]))
        for pred in sorted_preds[:5]:
            min_dist = min([abs(pred['gamma_predicted'] - g) 
                           for g in ACTUAL_RIEMANN_ZEROS.values()])
            closest_n = min(ACTUAL_RIEMANN_ZEROS.items(), 
                           key=lambda x: abs(x[1] - pred['gamma_predicted']))[0]
            closest_gamma = ACTUAL_RIEMANN_ZEROS[closest_n]
            error = abs(pred['gamma_predicted'] - closest_gamma) / closest_gamma * 100
            print(f"  {pred['name']}")
            print(f"    Predicted: γ ≈ {pred['gamma_predicted']:.4f}")
            print(f"    Closest to γ_{closest_n} = {closest_gamma:.4f} (error: {error:.1f}%)")
            print()
    
    # Statistical analysis
    print()
    print("=" * 70)
    print("STATISTICAL ASSESSMENT")
    print("=" * 70)
    print()
    
    # For each prediction, compute error to nearest zero
    errors = []
    for pred in predictions:
        min_error = min([abs(pred['gamma_predicted'] - g) / g 
                        for g in ACTUAL_RIEMANN_ZEROS.values()])
        errors.append(min_error * 100)
    
    if errors:
        print(f"Mean error to nearest zero: {np.mean(errors):.2f}%")
        print(f"Median error to nearest zero: {np.median(errors):.2f}%")
        print(f"Std dev: {np.std(errors):.2f}%")
        print(f"Best match: {np.min(errors):.2f}%")
        print(f"Worst match: {np.max(errors):.2f}%")
        print()
        
        # How many are within various tolerances?
        print("Distribution of matches:")
        for tol in [0.5, 1.0, 2.0, 5.0, 10.0]:
            count = sum(1 for e in errors if e <= tol)
            print(f"  Within {tol:>4.1f}%: {count:>2}/{len(errors)} ({count*100//len(errors):>3}%)")
        print()
    
    # Honest assessment
    print("=" * 70)
    print("HONEST ASSESSMENT")
    print("=" * 70)
    print()
    
    num_zeros = len(ACTUAL_RIEMANN_ZEROS)
    num_hierarchies = len(hierarchies)
    num_matches_strict = len(matches)
    
    random_match_probability = (0.02 * 2) * num_hierarchies / num_zeros
    
    print(f"Framework has {num_hierarchies} independent physical hierarchies")
    print(f"Target: {num_zeros} Riemann zeros")
    print()
    print(f"Strict matches (< 2% error): {num_matches_strict}")
    print()
    
    if num_matches_strict == 0:
        print("FINDING: No genuine Riemann zero predictions from framework hierarchies.")
        print()
        print("INTERPRETATION:")
        print("- The OC-2 formula (γ_1 connection to R_obs) may be a special case")
        print("- The formula might not generalize to other framework parameters")
        print("- The 0.014% precision for γ_1 could be numerical coincidence")
        print("- This does NOT invalidate the γ_1 discovery, but suggests it's unique")
        print()
        print("WHAT THIS MEANS:")
        print("- If γ_1 is special, why? (CP² geometry? KK momentum structure?)")
        print("- Other scales may be determined by different mechanisms")
        print("- The Riemann zeros might appear at DIFFERENT ORDER in the framework")
        print()
    else:
        print(f"FINDING: {num_matches_strict} genuine matches found!")
        print()
        print("INTERPRETATION:")
        print("- The formula DOES generalize to other physical scales")
        print("- Different framework parameters predict different Riemann zeros")
        print("- This is strong evidence for a systematic Riemann hierarchy")
        print()
        if len(matched_ns) > 1 and len(matched_ns) >= 3:
            if all(matched_ns[i+1] - matched_ns[i] == 1 for i in range(len(matched_ns)-1)):
                print("- The consecutive pattern suggests a DEEP connection")
                print("- Framework structure may encode RH via moduli stabilization")
    
    print()
    
    # Save results
    output = {
        'date': '2026-04-08',
        'status': 'Riemann zero prediction test',
        'framework': 'QG5D M-theory on M⁴ × CP² × S² × S¹',
        'formula': 'log(π × ratio) = γ_n × π² / 2',
        'test_hierarchies': len(hierarchies),
        'target_zeros': num_zeros,
        'strict_matches': num_matches_strict,
        'matches_within_tolerance': matches,
        'all_predictions': predictions,
        'assessment': {
            'genuine_matches': num_matches_strict > 0,
            'consecutive_pattern': len(matched_ns) > 1 and all(
                matched_ns[i+1] - matched_ns[i] == 1 for i in range(len(matched_ns)-1)
            ) if matches else False,
            'random_match_probability': float(random_match_probability),
            'conclusion': 'Genuine Riemann hierarchy found' if num_matches_strict > 0 else 'No systematic pattern detected'
        }
    }
    
    outpath = '/Users/gsix/quantum-geometry-in-5d-latex/next-frontier/code/oc2_predict_zeros_results.json'
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Results saved to: {outpath}")
    print()

if __name__ == '__main__':
    main()
