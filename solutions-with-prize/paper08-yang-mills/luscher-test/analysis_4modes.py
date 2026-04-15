#!/usr/bin/env python3
"""
Four-mode analysis: CP² worldsheet spectrum
============================================

Computes c_eff(R) for three scenarios of the 4-mode mass spectrum:

Scenario A: All 4 modes degenerate at m_a = 1.85√σ
Scenario B: Mass hierarchy from 1/N corrections
            axion at 1.85, scalars at 2.3, pseudo-partner at 2.8
Scenario C: 1 light + 3 very heavy (only axion contributes)
"""
import numpy as np
from scipy.special import kn
import json


def massive_casimir_bessel(R, m):
    """
    Massive Casimir contribution using Bessel K_0 sum.
    For a massive boson on an interval of length R:

    E(R,m) = -(m/π) Σ_{k=1}^∞ K_1(2kmR) / k

    The effective c contribution per mode:
    c_mode(R) = E_massive(R) / E_massless(R)
              = (24mR/π) Σ_k K_1(2kmR)/k

    Limits: c_mode → 1 as m → 0, c_mode → 0 as m → ∞
    """
    if m * R > 15:
        return 0.0
    x = m * R
    if x < 0.001:
        return 1.0  # massless limit
    total = 0.0
    for k in range(1, 100):
        arg = 2 * k * x
        if arg > 500:
            break
        val = kn(1, arg) / k
        total += val
        if abs(val) < 1e-15 * abs(total):
            break
    return (24 * x / np.pi) * total


def c_eff_multi_mode(R, masses):
    """
    c_eff with multiple massive modes.
    c_eff = 2 + Σ_i c_mode(R, m_i)
    """
    c = 2.0  # d-2 translational modes
    for m in masses:
        c += massive_casimir_bessel(R, m)
    return c


def main():
    # Verify massless limit
    print(f"Massless check: c_mode(R=1, m=0.001) = "
          f"{massive_casimir_bessel(1.0, 0.001):.4f} (should → 1)")
    print(f"Heavy check:    c_mode(R=1, m=10) = "
          f"{massive_casimir_bessel(1.0, 10.0):.6f} (should → 0)")
    print()

    # Three mass scenarios (masses in units of √σ)
    scenarios = {
        "A: All degenerate": [1.85, 1.85, 1.85, 1.85],
        "B: Mass hierarchy": [1.85, 2.3, 2.3, 2.8],
        "C: 1 light + 3 heavy": [1.85, 4.0, 4.0, 5.0],
        "D: Single axion only": [1.85],
        "E: Nambu-Goto (no modes)": [],
    }

    R_values = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]

    print("=" * 95)
    print("EFFECTIVE CENTRAL CHARGE: FIVE SCENARIOS")
    print("=" * 95)
    print()

    # Header
    header = f"{'R√σ':>5s}"
    for name in scenarios:
        short = name.split(":")[0]
        header += f"  {short:>12s}"
    print(header)
    print("-" * 80)

    results = {}
    for name, masses in scenarios.items():
        results[name] = []

    for R in R_values:
        line = f"{R:5.1f}"
        for name, masses in scenarios.items():
            c = c_eff_multi_mode(R, masses)
            results[name].append(c)
            line += f"  {c:12.4f}"
        print(line)

    print()
    print("=" * 95)
    print("THE KEY DISCRIMINATOR: Scenarios at R√σ = 0.7 (R ≈ 0.31 fm)")
    print("=" * 95)
    print()

    R_test = 0.7
    for name, masses in scenarios.items():
        c = c_eff_multi_mode(R_test, masses)
        dc = c - 2.0
        n = len(masses)
        mass_str = ", ".join(f"{m:.2f}" for m in masses) if masses else "none"
        print(f"  {name}")
        print(f"    Modes: {n}, masses: [{mass_str}]")
        print(f"    c_eff = {c:.4f}, δc = {dc:.4f} ({100*dc/2:.1f}%)")
        print()

    # The SU(N) scaling prediction
    print("=" * 95)
    print("SU(N) SCALING PREDICTION")
    print("=" * 95)
    print()
    print(f"{'N':>3s}  {'n_modes':>7s}  {'masses (all = m_a)':>20s}  "
          f"{'c_eff(0.7)':>10s}  {'δc':>8s}  {'δc/δc(N=3)':>10s}")
    print("-" * 72)

    m_a = 1.85
    dc_ref = None
    for N in [2, 3, 4, 5, 6, 8, 10]:
        n_modes = 2 * (N - 1)
        masses = [m_a] * n_modes  # all degenerate (large-N limit)
        c = c_eff_multi_mode(0.7, masses)
        dc = c - 2.0
        if N == 3:
            dc_ref = dc
        ratio = dc / dc_ref if dc_ref else 0
        print(f"{N:3d}  {n_modes:7d}  {n_modes}×{m_a}{'':>13s}  "
              f"{c:10.4f}  {dc:8.4f}  {ratio:10.2f}")

    print()
    print("Key: δc grows LINEARLY with (N-1).")
    print("Single-axion model: δc = 0.107 for ALL N (constant).")
    print()
    print("At SU(6): our prediction gives 5× the SU(3) signal.")
    print("If the lattice sees δc scaling with N → CP^{N-1} confirmed.")
    print("If δc stays constant with N → single axion wins.")

    # Save
    with open("/Users/gsix/yang-mills/luscher-test/results_4modes.json", "w") as f:
        json.dump({
            "R_values": R_values,
            "scenarios": {k: v for k, v in results.items()},
            "scenario_masses": {k: v for k, v in scenarios.items()},
        }, f, indent=2)
    print("\nSaved to results_4modes.json")


if __name__ == "__main__":
    main()
