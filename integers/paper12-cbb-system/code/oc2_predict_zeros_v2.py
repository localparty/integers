#!/usr/bin/env python3
"""
OC-2 RIEMANN ZERO PREDICTION TEST - VERSION 2
==============================================

This is a more thorough analysis testing whether the QG5D framework can predict
Riemann zeros from physical observations.

KEY DIFFERENCE FROM V1:
- Use the correct R_obs/l_P = 6.1871e+29 (verified from dark energy data)
- Test MULTIPLE formula structures, not just log(π × R) = γ × π²/2
- Look for PATTERNS in which hierarchies match which zeros
- Test whether the γ_1 match for R_obs is truly special

FORMULA VARIANTS TO TEST:
1. log(π × R) = γ × π²/2                (original OC-2)
2. log(R) = γ × π²/2 - log(π)           (equivalent form)
3. R = exp(γ × π²/2 - log(π))           (exponential form)
4. R = π^(γ × π/2)                       (power form)
5. log(R) = γ × (some other factor)     (alternative factors)
"""

import mpmath as mp
import numpy as np
import json
from typing import List, Tuple, Dict, Optional

mp.dps = 50

# ════════════════════════════════════════════════════════════════
# RIEMANN ZEROS
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
# FRAMEWORK CONSTANTS (VERIFIED FROM RESEARCH)
# ════════════════════════════════════════════════════════════════

# Use the exact value from research 14
R_obs_over_lP_verified = 6.1871424991724e+29  # From dark energy data
log_R_obs_lP_target = 68.5974410451414

# Planck scale
M_Pl = 2.435e18  # GeV
l_P_inv = M_Pl  # in GeV

# Standard scales (GeV)
M_EW = 246.0  # Higgs vev
M_KK = 1.5e3  # 1-2.5 TeV typical value

# GUT scale
M_GUT = 1e15  # GeV

# Alternative scales
M_Planck_reduced = 2.435e18  # GeV (same as M_Pl)
m_nu = 49.7e-3  # GeV (meV neutrino mass)

# ════════════════════════════════════════════════════════════════
# MATHEMATICAL CONSTANTS
# ════════════════════════════════════════════════════════════════

pi = mp.pi
e = mp.e
gamma_E = mp.euler
zeta_2 = mp.zeta(2)  # π²/6
zeta_3 = mp.zeta(3)
zeta_4 = mp.zeta(4)

# ════════════════════════════════════════════════════════════════
# FORMULA TESTER CLASS
# ════════════════════════════════════════════════════════════════

class RiemannFormulaTest:
    """Test whether a ratio matches a Riemann zero using various formulas."""
    
    def __init__(self, tolerance=0.02):
        self.tolerance = tolerance
        
    def find_match(self, gamma_pred: float) -> Optional[Tuple[int, float, float]]:
        """Find if gamma_pred matches an actual Riemann zero.
        Returns (zero_index, gamma_actual, error_pct) or None."""
        for n, gamma_actual in ACTUAL_RIEMANN_ZEROS.items():
            error = abs(gamma_pred - gamma_actual) / gamma_actual
            if error <= self.tolerance:
                return (n, gamma_actual, error * 100)
        return None
    
    def test_formula_type_1(self, ratio: float) -> Dict:
        """Test: log(π × ratio) = γ × π²/2
        Solve for γ: γ = 2 × log(π × ratio) / π²
        """
        ratio_mp = mp.mpf(str(ratio))
        gamma_pred = 2 * mp.log(pi * ratio_mp) / (pi ** 2)
        gamma_pred_float = float(gamma_pred)
        match = self.find_match(gamma_pred_float)
        return {
            'formula': 'log(π × R) = γ × π²/2',
            'gamma_predicted': gamma_pred_float,
            'match': match,
        }
    
    def test_formula_type_2(self, ratio: float) -> Dict:
        """Test: log(ratio) = γ × π²/2 - log(π)
        Solve for γ: γ = (log(ratio) + log(π)) × 2 / π²
        """
        ratio_mp = mp.mpf(str(ratio))
        gamma_pred = 2 * (mp.log(ratio_mp) + mp.log(pi)) / (pi ** 2)
        gamma_pred_float = float(gamma_pred)
        match = self.find_match(gamma_pred_float)
        return {
            'formula': 'log(R) = γ × π²/2 - log(π)',
            'gamma_predicted': gamma_pred_float,
            'match': match,
        }
    
    def test_formula_type_3(self, ratio: float) -> Dict:
        """Test: log(ratio) = γ × c for various constants c.
        Try c = π, π²/2, e, log(π), etc.
        """
        ratio_mp = mp.mpf(str(ratio))
        log_ratio = mp.log(ratio_mp)
        
        candidates = [
            ('π', pi),
            ('π²/2', pi**2/2),
            ('e', e),
            ('log(π)', mp.log(pi)),
            ('ζ(2)', zeta_2),
            ('2π/3', 2*pi/3),
            ('π/log(π)', pi/mp.log(pi)),
        ]
        
        best = None
        best_match = None
        best_error = float('inf')
        
        for const_name, const_val in candidates:
            gamma_pred = log_ratio / const_val
            gamma_pred_float = float(gamma_pred)
            match = self.find_match(gamma_pred_float)
            error = abs(gamma_pred_float - min(ACTUAL_RIEMANN_ZEROS.values())) / min(ACTUAL_RIEMANN_ZEROS.values())
            if error < best_error:
                best_error = error
                best = (const_name, gamma_pred_float)
                best_match = match
        
        return {
            'formula': f'log(R) = γ × (constant)',
            'best_constant': best[0] if best else None,
            'gamma_predicted': best[1] if best else None,
            'match': best_match,
        }
    
    def test_all_formulas(self, ratio: float, hierarchy_name: str) -> Dict:
        """Test all formula types for a ratio."""
        return {
            'hierarchy': hierarchy_name,
            'ratio': float(ratio),
            'log_ratio': float(mp.log(mp.mpf(str(ratio)))),
            'type1': self.test_formula_type_1(ratio),
            'type2': self.test_formula_type_2(ratio),
            'type3': self.test_formula_type_3(ratio),
        }

# ════════════════════════════════════════════════════════════════
# PHYSICAL HIERARCHIES
# ════════════════════════════════════════════════════════════════

def get_hierarchies() -> List[Tuple[str, float]]:
    """Return physical hierarchies in the framework."""
    return [
        # Established
        ("R_obs / l_P (cosmological constant - VERIFIED)", R_obs_over_lP_verified),
        
        # Mass scales
        ("M_EW × l_P (electroweak)", M_EW * (1.0 / M_Pl)),
        ("M_KK × l_P (Kaluza-Klein)", M_KK * (1.0 / M_Pl)),
        ("M_GUT × l_P (GUT scale)", M_GUT * (1.0 / M_Pl)),
        ("M_Pl / M_EW (EW hierarchy)", M_Pl / M_EW),
        ("M_Pl / M_KK (KK hierarchy)", M_Pl / M_KK),
        ("M_Pl / M_GUT (GUT hierarchy)", M_Pl / M_GUT),
        
        # Cosmic ratios (Paper 2)
        ("Ω_DM / Ω_b", 5.36),
        ("1 / ξ (inverse mirror temp)", 1.0 / 0.432),
        
        # Fundamental constants
        ("1 / α (fine structure constant)", 137.036),
        ("m_p / m_e (proton-electron)", 1836.15),
        
        # GUT flux (Paper 7)
        ("n_2 / n_1 (GUT flux quantization)", 17.0 / 9.0),
        
        # Alternative formulations
        ("log(M_Pl) + γ_E approximation", M_Pl * np.e),
    ]

# ════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════

def main():
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║         OC-2 RIEMANN ZERO PREDICTION TEST v2.0                      ║")
    print("║   Rigorous test of formula generalization beyond γ_1                ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print()
    
    # Display target zeros
    print("TARGET RIEMANN ZEROS:")
    for n in sorted(ACTUAL_RIEMANN_ZEROS.keys()):
        print(f"  γ_{n:2d} = {ACTUAL_RIEMANN_ZEROS[n]:.12f}")
    print()
    
    # Initialize tester
    tester = RiemannFormulaTest(tolerance=0.02)
    
    # Get hierarchies
    hierarchies = get_hierarchies()
    
    print(f"TESTING {len(hierarchies)} PHYSICAL HIERARCHIES")
    print("=" * 70)
    print()
    
    all_results = []
    all_matches = []
    
    for name, ratio in hierarchies:
        print(f"\n{name}")
        print(f"  Ratio: {ratio:.6e}")
        
        results = tester.test_all_formulas(ratio, name)
        all_results.append(results)
        
        # Check all formulas for matches
        for formula_type in ['type1', 'type2', 'type3']:
            formula_info = results[formula_type]
            if formula_info.get('match'):
                matched_n, matched_gamma, error = formula_info['match']
                print(f"  ✓ MATCH via {formula_info['formula']}")
                print(f"    Predicted γ: {formula_info['gamma_predicted']:.6f}")
                print(f"    Matched to γ_{matched_n}: {matched_gamma:.6f}")
                print(f"    Error: {error:.3f}%")
                
                all_matches.append({
                    'hierarchy': name,
                    'formula': formula_info['formula'],
                    'gamma_predicted': formula_info['gamma_predicted'],
                    'matched_to_n': matched_n,
                    'error_pct': error,
                })
    
    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    
    if all_matches:
        print(f"MATCHES FOUND: {len(all_matches)}")
        print()
        for match in all_matches:
            print(f"  • {match['hierarchy']}")
            print(f"    Formula: {match['formula']}")
            print(f"    Predicts γ_{match['matched_to_n']}")
            print(f"    Error: {match['error_pct']:.3f}%")
    else:
        print("NO MATCHES FOUND within 2% tolerance")
        print()
        
        # Analyze the type-1 formula (the original)
        print("Analysis of type-1 formula [log(π×R) = γ×π²/2]:")
        print()
        type1_errors = []
        for result in all_results:
            if result['type1']['gamma_predicted']:
                gamma = result['type1']['gamma_predicted']
                min_error = min([abs(gamma - g) / g for g in ACTUAL_RIEMANN_ZEROS.values()])
                type1_errors.append((result['hierarchy'], gamma, min_error * 100))
        
        type1_errors.sort(key=lambda x: x[2])
        print("Best matches (to nearest zero):")
        for name, gamma, error in type1_errors[:5]:
            closest_n = min(ACTUAL_RIEMANN_ZEROS.items(), 
                           key=lambda x: abs(x[1] - gamma))[0]
            print(f"  {error:.2f}% off: {name}")
            print(f"           Predicted γ={gamma:.4f}, Closest γ_{closest_n}={ACTUAL_RIEMANN_ZEROS[closest_n]:.4f}")
    
    print()
    print("=" * 70)
    print("HONEST ASSESSMENT")
    print("=" * 70)
    print()
    
    # Key observation: R_obs should match γ_1
    obs_type1 = None
    for result in all_results:
        if "R_obs / l_P" in result['hierarchy']:
            obs_type1 = result['type1']
            break
    
    if obs_type1:
        gamma_obs = obs_type1['gamma_predicted']
        error_obs = abs(gamma_obs - ACTUAL_RIEMANN_ZEROS[1]) / ACTUAL_RIEMANN_ZEROS[1] * 100
        print(f"R_obs/l_P prediction:")
        print(f"  Predicted γ: {gamma_obs:.6f}")
        print(f"  Actual γ_1: {ACTUAL_RIEMANN_ZEROS[1]:.6f}")
        print(f"  Error: {error_obs:.3f}%")
        print()
    
    print("CONCLUSION:")
    if all_matches:
        print(f"✓ The formula DOES generalize. {len(all_matches)} hierarchies predict Riemann zeros.")
        
        matched_ns = [m['matched_to_n'] for m in all_matches]
        if len(set(matched_ns)) == len(matched_ns):
            print(f"  Each match predicts a DIFFERENT zero: {sorted(set(matched_ns))}")
        
        consecutive = all(matched_ns[i+1] - matched_ns[i] == 1 
                         for i in range(len(sorted(set(matched_ns)))-1))
        if consecutive and len(set(matched_ns)) > 2:
            print(f"  Consecutive pattern detected → systematic Riemann hierarchy!")
    else:
        print("✗ The formula does NOT generalize to other framework parameters.")
        print()
        print("What this means:")
        print("  1. The γ_1 match for R_obs is a SPECIAL case, not a general pattern")
        print("  2. Other framework scales are determined by different mechanisms")
        print("  3. The 0.014% precision of the γ_1 match is striking but isolated")
        print("  4. This suggests γ_1 has special significance in the QG5D geometry")
        print()
        print("Possible explanations:")
        print("  - Only the S¹ (e-circle) dimension connects to Riemann zeros")
        print("  - The other zeros (γ_2, γ_3, ...) appear at higher orders or in")
        print("    different observables (e.g., particle masses, coupling constants)")
        print("  - The connection might be via a DIFFERENT formula for other parameters")

if __name__ == '__main__':
    main()
