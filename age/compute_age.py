#!/usr/bin/env python3
"""
5D Framework Cosmological Predictions
======================================

Computes the age of the universe, sound horizon, CMB angular scale,
sigma_8, and other observables using the CAMB Boltzmann solver with
the 5D e-dimension framework's predicted parameters.

Compares against standard Planck LCDM.
"""

import numpy as np
import camb
from camb import model
import json
import os

# ============================================================
# CONSTANTS
# ============================================================
c_km_s = 2.998e5  # speed of light in km/s
Gyr_per_sec = 1.0 / (3.156e16)  # convert seconds to Gyr

# ============================================================
# SCENARIO DEFINITIONS
# ============================================================

scenarios = {}

# --- Scenario 0: Planck 2018 LCDM (baseline) ---
scenarios["Planck_LCDM"] = {
    "H0": 67.36,
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "mnu": 0.06,          # minimal neutrino mass (eV)
    "nnu": 3.044,         # standard N_eff
    "w": -1.0,
    "wa": 0.0,
    "label": "Planck 2018 LCDM (baseline)",
}

# --- Scenario 1: 5D Framework — Stabilized e-circle, w = -1 ---
# H_0 shifted by hidden-brane dark radiation (Delta_N_eff = 0.30)
# N_eff = 3.044 + 0.05 (tower) + 0.30 (mirror) = 3.39
# Same baryon density, same neutrino mass
scenarios["5D_stabilized"] = {
    "H0": 69.5,
    "ombh2": 0.02237,
    "omch2": 0.1200,      # same CDM density for now
    "mnu": 0.06,
    "nnu": 3.39,          # 3.044 + 0.05 + 0.30
    "w": -1.0,
    "wa": 0.0,
    "label": "5D Stabilized e-circle (w=-1, H0=69.5, Neff=3.39)",
}

# --- Scenario 2: 5D Framework — Thawing dilaton ---
scenarios["5D_thawing"] = {
    "H0": 69.5,
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "mnu": 0.06,
    "nnu": 3.39,
    "w": -0.85,
    "wa": -0.23,
    "label": "5D Thawing dilaton (w0=-0.85, wa=-0.23)",
}

# --- Scenario 3: 5D Framework — DESI-compatible dilaton ---
scenarios["5D_DESI"] = {
    "H0": 69.5,
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "mnu": 0.06,
    "nnu": 3.39,
    "w": -0.80,
    "wa": -0.30,
    "label": "5D DESI-compatible dilaton (w0=-0.80, wa=-0.30)",
}

# --- Scenario 4: 5D Framework — Minimal (tower only, no mirror) ---
scenarios["5D_minimal"] = {
    "H0": 67.7,           # small shift from tower Delta_N_eff = 0.05
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "mnu": 0.06,
    "nnu": 3.09,          # 3.044 + 0.05 (tower dynamics only)
    "w": -1.0,
    "wa": 0.0,
    "label": "5D Minimal (tower only, no mirror sector)",
}

# --- Scenario 5: 5D Framework — Lower Omega_m ---
# What if mirror matter production gives less DM?
scenarios["5D_low_omega"] = {
    "H0": 69.5,
    "ombh2": 0.02237,
    "omch2": 0.1050,      # less CDM (mirror matter production)
    "mnu": 0.06,
    "nnu": 3.39,
    "w": -0.85,
    "wa": -0.23,
    "label": "5D Thawing + lower Omega_cdm (reduced mirror production)",
}

# --- Scenario 6: 5D Framework — theta_* constrained ---
# Adjust Omega_cdm to MATCH the Planck theta_* = 1.04110 deg
# This is the "what Omega_m does the framework NEED?" test
scenarios["5D_theta_matched"] = {
    "H0": 69.5,
    "ombh2": 0.02237,
    "omch2": 0.1350,      # higher CDM to match theta_*
    "mnu": 0.06,
    "nnu": 3.39,
    "w": -0.85,
    "wa": -0.23,
    "label": "5D Thawing + Omega_cdm adjusted to match theta_*",
}

# --- Scenario 7: TRGB-centered ---
scenarios["TRGB_centered"] = {
    "H0": 69.8,
    "ombh2": 0.02237,
    "omch2": 0.1200,
    "mnu": 0.06,
    "nnu": 3.39,
    "w": -0.85,
    "wa": -0.23,
    "label": "5D at TRGB H0=69.8 (Freedman et al. 2024)",
}


def run_scenario(name, params):
    """Run CAMB for a given parameter set and return key observables."""

    # Set up CAMB parameters
    pars = camb.CAMBparams()

    # Standard neutrino setup: 1 massive + (nnu - 1) massless
    # CAMB's nnu parameter is the effective number of massless neutrino-like species
    # We have 1 massive neutrino + extra radiation
    nnu_standard = 3.044
    nnu_extra = params["nnu"] - nnu_standard  # extra radiation beyond SM

    pars.set_cosmology(
        H0=params["H0"],
        ombh2=params["ombh2"],
        omch2=params["omch2"],
        mnu=params["mnu"],
        num_massive_neutrinos=1,
        nnu=params["nnu"],  # total N_eff including extra
        tau=0.054,          # optical depth (Planck 2018)
    )

    # Dark energy equation of state
    if params["wa"] != 0.0:
        pars.set_dark_energy(w=params["w"], wa=params["wa"], dark_energy_model='ppf')
    else:
        pars.set_dark_energy(w=params["w"])

    # Initial power spectrum (Planck 2018 best-fit)
    pars.InitPower.set_params(As=2.1e-9, ns=0.9649)

    # Accuracy settings
    pars.set_accuracy(AccuracyBoost=1.5)

    # Want matter power spectrum for sigma_8
    pars.set_matter_power(redshifts=[0.0], kmax=2.0)

    # Want CMB power spectra
    pars.set_for_lmax(2500)

    # Run CAMB
    results = camb.get_results(pars)

    # Extract key observables
    derived = results.get_derived_params()

    # Age of the universe
    age = derived['age']  # in Gyr

    # Sound horizon at baryon drag
    rd = derived['rdrag']  # in Mpc

    # Angular size of sound horizon at last scattering
    theta_star = derived['thetastar']  # in radians * 100
    theta_star_deg = theta_star / 100.0 * (180.0 / np.pi)  # convert to degrees

    # Redshift of last scattering
    z_star = derived['zstar']

    # Redshift of baryon drag epoch
    z_drag = derived['zdrag']

    # sigma_8
    sigma8 = results.get_sigma8_0()

    # Omega values
    omega_m = (params["ombh2"] + params["omch2"] + params["mnu"]/93.14) / (params["H0"]/100.0)**2
    omega_lambda = 1.0 - omega_m - derived.get('omegak', 0.0)

    # S8
    S8 = sigma8 * np.sqrt(omega_m / 0.3)

    # Comoving distance to last scattering
    DA_star = results.angular_diameter_distance(z_star)

    # Lookback times at various redshifts (useful for JWST)
    # Age at redshift z = age_of_universe - lookback_time(z)
    # CAMB gives the age of the universe and we can compute ages at z
    z_test = [0, 2, 6, 10, 12, 14, 20]
    ages_at_z = {}
    for z in z_test:
        # Time since big bang at redshift z
        t_z = results.age_of_universe(z)  # Gyr (this is conformal time-based)
        ages_at_z[z] = t_z

    # Hubble parameter at various redshifts
    H_at_z = {}
    for z in [0, 0.5, 1.0, 2.0, 5.0]:
        H_at_z[z] = results.hubble_parameter(z)

    return {
        "name": name,
        "label": params["label"],
        "age_Gyr": age,
        "rd_Mpc": rd,
        "theta_star_deg": theta_star_deg,
        "theta_star_100rad": theta_star,
        "z_star": z_star,
        "z_drag": z_drag,
        "sigma8": sigma8,
        "S8": S8,
        "Omega_m": omega_m,
        "Omega_Lambda_eff": omega_lambda,
        "DA_star_Mpc": DA_star,
        "H0": params["H0"],
        "nnu": params["nnu"],
        "w0": params["w"],
        "wa": params["wa"],
        "ages_at_z": ages_at_z,
        "H_at_z": H_at_z,
    }


def print_results(res):
    """Pretty-print results for a scenario."""
    print(f"\n{'='*70}")
    print(f"  {res['label']}")
    print(f"{'='*70}")
    print(f"  Age of universe:     {res['age_Gyr']:.3f} Gyr")
    print(f"  Sound horizon r_d:   {res['rd_Mpc']:.2f} Mpc")
    print(f"  theta_* (deg):       {res['theta_star_deg']:.5f}")
    print(f"  theta_* (100*rad):   {res['theta_star_100rad']:.4f}")
    print(f"  z_* (recombination): {res['z_star']:.1f}")
    print(f"  z_drag:              {res['z_drag']:.1f}")
    print(f"  sigma_8:             {res['sigma8']:.4f}")
    print(f"  S8:                  {res['S8']:.4f}")
    print(f"  Omega_m:             {res['Omega_m']:.4f}")
    print(f"  Omega_Lambda (eff):  {res['Omega_Lambda_eff']:.4f}")
    print(f"  D_A(z_*):            {res['DA_star_Mpc']:.1f} Mpc")
    print(f"  H_0:                 {res['H0']:.1f} km/s/Mpc")
    print(f"  N_eff:               {res['nnu']:.3f}")
    print(f"  w_0:                 {res['w0']:.2f}")
    print(f"  w_a:                 {res['wa']:.2f}")

    print(f"\n  Time since Big Bang at various redshifts:")
    print(f"  {'z':>6} | {'t (Myr)':>10} | {'t (Gyr)':>10}")
    print(f"  {'-'*6}-+-{'-'*10}-+-{'-'*10}")
    for z in sorted(res['ages_at_z'].keys()):
        t = res['ages_at_z'][z]
        print(f"  {z:>6.0f} | {t*1000:>10.1f} | {t:>10.3f}")

    print(f"\n  Hubble parameter H(z):")
    print(f"  {'z':>6} | {'H(z) (km/s/Mpc)':>18}")
    print(f"  {'-'*6}-+-{'-'*18}")
    for z in sorted(res['H_at_z'].keys()):
        print(f"  {z:>6.1f} | {res['H_at_z'][z]:>18.2f}")


def comparison_table(all_results):
    """Print a comparison table across all scenarios."""

    planck = all_results["Planck_LCDM"]

    print(f"\n\n{'#'*70}")
    print(f"  COMPARISON TABLE: 5D Framework vs Planck LCDM")
    print(f"{'#'*70}\n")

    # Header
    header = f"{'Observable':<25}"
    for name in all_results:
        short = name[:12]
        header += f" | {short:>12}"
    print(header)
    print("-" * len(header))

    # Rows
    def row(label, key, fmt=".3f"):
        line = f"{label:<25}"
        for name, res in all_results.items():
            val = res[key]
            line += f" | {val:>12{fmt}}"
        return line

    print(row("Age (Gyr)", "age_Gyr", ".3f"))
    print(row("r_d (Mpc)", "rd_Mpc", ".2f"))
    print(row("theta_* (deg)", "theta_star_deg", ".5f"))
    print(row("sigma_8", "sigma8", ".4f"))
    print(row("S8", "S8", ".4f"))
    print(row("Omega_m", "Omega_m", ".4f"))
    print(row("H_0", "H0", ".1f"))
    print(row("N_eff", "nnu", ".3f"))
    print(row("w_0", "w0", ".2f"))
    print(row("w_a", "wa", ".2f"))

    # Differences from Planck
    print(f"\n\n{'='*70}")
    print(f"  DIFFERENCES FROM PLANCK LCDM")
    print(f"{'='*70}\n")

    for name, res in all_results.items():
        if name == "Planck_LCDM":
            continue
        print(f"\n  {res['label']}:")
        print(f"    Delta(Age) = {res['age_Gyr'] - planck['age_Gyr']:+.3f} Gyr")
        print(f"    Delta(r_d) = {res['rd_Mpc'] - planck['rd_Mpc']:+.2f} Mpc")
        print(f"    Delta(theta_*) = {(res['theta_star_deg'] - planck['theta_star_deg'])*3600:+.2f} arcsec")
        print(f"    Delta(sigma_8) = {res['sigma8'] - planck['sigma8']:+.4f}")
        print(f"    Delta(S8) = {res['S8'] - planck['S8']:+.4f}")

        # Time at z=14 comparison (JWST)
        if 14 in res['ages_at_z'] and 14 in planck['ages_at_z']:
            dt = (res['ages_at_z'][14] - planck['ages_at_z'][14]) * 1000  # Myr
            print(f"    Delta(t at z=14) = {dt:+.1f} Myr (JWST early galaxies)")


def jwst_analysis(all_results):
    """Detailed analysis of time available for early galaxy formation."""

    print(f"\n\n{'#'*70}")
    print(f"  JWST EARLY GALAXY ANALYSIS")
    print(f"  Time since Big Bang at high redshifts")
    print(f"{'#'*70}\n")

    print(f"  {'Scenario':<35} | {'z=10 (Myr)':>10} | {'z=12 (Myr)':>10} | {'z=14 (Myr)':>10} | {'z=20 (Myr)':>10}")
    print(f"  {'-'*35}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}")

    for name, res in all_results.items():
        ages = res['ages_at_z']
        short = name[:35]
        t10 = ages.get(10, 0) * 1000
        t12 = ages.get(12, 0) * 1000
        t14 = ages.get(14, 0) * 1000
        t20 = ages.get(20, 0) * 1000
        print(f"  {short:<35} | {t10:>10.1f} | {t12:>10.1f} | {t14:>10.1f} | {t20:>10.1f}")


def save_results(all_results, outdir):
    """Save results to JSON for later analysis."""
    serializable = {}
    for name, res in all_results.items():
        r = dict(res)
        # Convert numpy types to Python native
        for k, v in r.items():
            if isinstance(v, np.floating):
                r[k] = float(v)
            elif isinstance(v, dict):
                r[k] = {str(kk): float(vv) if isinstance(vv, np.floating) else vv
                        for kk, vv in v.items()}
        serializable[name] = r

    path = os.path.join(outdir, "results.json")
    with open(path, 'w') as f:
        json.dump(serializable, f, indent=2)
    print(f"\n  Results saved to {path}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=" * 70)
    print("  5D FRAMEWORK COSMOLOGICAL PREDICTIONS")
    print("  Using CAMB Boltzmann Solver")
    print("=" * 70)

    all_results = {}

    for name, params in scenarios.items():
        print(f"\n  Running: {name}...", end="", flush=True)
        try:
            res = run_scenario(name, params)
            all_results[name] = res
            print(f" done (age = {res['age_Gyr']:.3f} Gyr)")
        except Exception as e:
            print(f" FAILED: {e}")

    # Print detailed results for each scenario
    for name, res in all_results.items():
        print_results(res)

    # Print comparison table
    comparison_table(all_results)

    # JWST analysis
    jwst_analysis(all_results)

    # Save results
    save_results(all_results, os.path.dirname(os.path.abspath(__file__)))

    print("\n" + "=" * 70)
    print("  COMPUTATION COMPLETE")
    print("=" * 70)
