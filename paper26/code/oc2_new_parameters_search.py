#!/usr/bin/env python3
"""
OC-2: COMPREHENSIVE TEST OF 25+ NEW FRAMEWORK PARAMETERS vs RIEMANN ZEROS
==========================================================================

Tests particle physics, neutrino, CKM, and cosmology parameters against
the discovered Riemann formulas. Systematic extension of the 12-parameter
search documented in Research 21.
"""

from mpmath import mp, zetazero, im, mpf, log, pi, e, euler, zeta
import json
from pathlib import Path

mp.dps = 100

print("=" * 90)
print("OC-2: 25-PARAMETER SEARCH vs RIEMANN ZEROS")
print("=" * 90)
print()

# ════════════════════════════════════════════════════════════════
# Riemann zeros γ_1 ... γ_15
# ════════════════════════════════════════════════════════════════

print("Computing Riemann zeros γ_1...γ_15 at 100 decimal precision...")
gamma = {}
for n in range(1, 16):
    gamma[n] = im(zetazero(n))

# ════════════════════════════════════════════════════════════════
# Constants
# ════════════════════════════════════════════════════════════════

constants = {
    "1": mpf(1),
    "π": pi,
    "e": e,
    "γ_E": euler,
    "log(2)": log(2),
    "log(π)": log(pi),
    "ζ(2)": zeta(2),
    "ζ(3)": zeta(3),
    "ζ(4)": zeta(4),
    "2π": 2*pi,
    "π/2": pi/2,
    "π²/2": pi**2/2,
    "π²/6": pi**2/6,
    "π/4": pi/4,
}

# ════════════════════════════════════════════════════════════════
# Parameters to test (25 total)
# ════════════════════════════════════════════════════════════════

params = {
    # PARTICLE PHYSICS MASSES (10)
    "m_W [GeV]": mpf("80.379"),
    "m_Z [GeV]": mpf("91.1876"),
    "m_H [GeV]": mpf("125.10"),
    "m_t [GeV]": mpf("172.76"),
    "m_b [GeV]": mpf("4.18"),
    "m_c [GeV]": mpf("1.275"),
    "m_W/m_Z": mpf("0.881"),
    "m_t/m_b": mpf("41.33"),
    "m_t/m_W": mpf("2.149"),
    "v [GeV]": mpf("246"),

    # NEUTRINO (4)
    "Δm²_atm/Δm²_sol": mpf("33.33"),  # ratio of atmospheric to solar
    "sin²(θ_12)": mpf("0.307"),
    "sin²(θ_23)": mpf("0.546"),
    "sin²(θ_13)": mpf("0.022"),

    # CKM (4)
    "V_us": mpf("0.224"),
    "V_cb": mpf("0.041"),
    "V_us/V_cb": mpf("5.46"),
    "J_CKM × 1e5": mpf("3.18"),

    # COSMOLOGY (4)
    "H_0 [km/s/Mpc]": mpf("67.4"),
    "n_s": mpf("0.965"),
    "α_s(M_Z)": mpf("0.118"),
    "1/α_s(M_Z)": mpf("8.475"),

    # GAUGE COUPLINGS (3)
    "1/α_2(M_Z)": mpf("29.57"),  # weak
    "1/α_3(M_Z)": mpf("8.475"),  # strong
    "g²/4π (electroweak)": mpf("0.034"),
}

print(f"Testing {len(params)} parameters against Riemann formulas...")
print()

# ════════════════════════════════════════════════════════════════
# Search function
# ════════════════════════════════════════════════════════════════

def err_pct(computed, target):
    if abs(float(target)) < 1e-15:
        return float('inf')
    return abs(float(computed - target) / float(target)) * 100

def search_param(param_val):
    matches = []

    # Powers γ_n^p
    exponents = [mpf(1)/mpf(2), mpf(1)/mpf(3), mpf(1)/mpf(4),
                 mpf(2)/mpf(3), mpf(3)/mpf(4), mpf(5)/mpf(4),
                 mpf(1), mpf(2), mpf(1)/mpf(5), mpf(4)/mpf(5)]
    for n in range(1, 16):
        for exp in exponents:
            try:
                computed = gamma[n] ** exp
                e_pct = err_pct(computed, param_val)
                if e_pct < 1.0:
                    matches.append((f"γ_{n}^({float(exp):.4f})", computed, e_pct))
            except:
                pass

    # γ_n × constant and γ_n / constant
    for n in range(1, 16):
        for cn, cv in constants.items():
            try:
                c1 = gamma[n] * cv
                e1 = err_pct(c1, param_val)
                if e1 < 1.0:
                    matches.append((f"γ_{n} × {cn}", c1, e1))
                if abs(float(cv)) > 1e-10:
                    c2 = gamma[n] / cv
                    e2 = err_pct(c2, param_val)
                    if e2 < 1.0:
                        matches.append((f"γ_{n} / {cn}", c2, e2))
            except:
                pass

    # log(γ_n) × constant
    for n in range(1, 16):
        for cn, cv in constants.items():
            try:
                computed = log(gamma[n]) * cv
                e_pct = err_pct(computed, param_val)
                if e_pct < 1.0:
                    matches.append((f"log(γ_{n}) × {cn}", computed, e_pct))
            except:
                pass

    # Pairs γ_n × γ_m / constant
    for n in range(1, 11):
        for m in range(n+1, 12):
            for cn, cv in constants.items():
                if abs(float(cv)) < 1e-10:
                    continue
                try:
                    computed = gamma[n] * gamma[m] / cv
                    e_pct = err_pct(computed, param_val)
                    if e_pct < 1.0:
                        matches.append((f"γ_{n} × γ_{m} / {cn}", computed, e_pct))
                except:
                    pass

    # γ_n / γ_m
    for n in range(1, 12):
        for m in range(1, 12):
            if n == m:
                continue
            try:
                computed = gamma[n] / gamma[m]
                e_pct = err_pct(computed, param_val)
                if e_pct < 1.0:
                    matches.append((f"γ_{n} / γ_{m}", computed, e_pct))
            except:
                pass

    matches.sort(key=lambda x: x[2])
    return matches[:3]  # top 3

# ════════════════════════════════════════════════════════════════
# Run search
# ════════════════════════════════════════════════════════════════

all_results = {}
for pname, pval in params.items():
    matches = search_param(pval)
    all_results[pname] = matches

# ════════════════════════════════════════════════════════════════
# Report
# ════════════════════════════════════════════════════════════════

print(f"\n{'='*90}")
print("RESULTS: Sub-1% matches")
print(f"{'='*90}\n")

best_matches = []
no_matches = []

for pname, matches in all_results.items():
    if matches:
        best_formula, best_val, best_err = matches[0]
        best_matches.append((best_err, pname, best_formula, best_val))
    else:
        no_matches.append(pname)

best_matches.sort()

if best_matches:
    print(f"FOUND {len(best_matches)} parameters with sub-1% matches:\n")
    print(f"{'Error':>10}  {'Parameter':<35}  Formula")
    print("-" * 90)
    for err, pname, formula, val in best_matches:
        print(f"{err:>9.4f}%  {pname:<35}  {formula}")

print(f"\nNo sub-1% match for {len(no_matches)} parameters:")
for pname in no_matches:
    print(f"  - {pname}")

# ════════════════════════════════════════════════════════════════
# Save JSON
# ════════════════════════════════════════════════════════════════

output_path = Path("/Users/gsix/quantum-geometry-in-5d-latex/next-frontier/code/oc2_new_parameters_results.json")

results_json = {
    "timestamp": "2026-04-09",
    "parameters_tested": len(params),
    "parameters_matched": len(best_matches),
    "best_matches": [
        {
            "error_percent": float(err),
            "parameter": pname,
            "formula": formula,
            "computed_value": str(val),
        }
        for err, pname, formula, val in best_matches
    ],
    "no_match": no_matches,
}

with open(output_path, 'w') as f:
    json.dump(results_json, f, indent=2)

print(f"\nResults saved: {output_path}")
print("=" * 90)
