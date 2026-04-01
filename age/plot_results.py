#!/usr/bin/env python3
"""
Generate plots comparing 5D framework cosmological predictions vs Planck LCDM.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt
import camb
import json
import os

# Load results
outdir = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# Color scheme
# ============================================================
colors = {
    "Planck_LCDM":     "#2c3e50",  # dark blue-gray
    "5D_stabilized":   "#e74c3c",  # red
    "5D_thawing":      "#e67e22",  # orange
    "5D_DESI":         "#f39c12",  # gold
    "5D_minimal":      "#95a5a6",  # gray
    "5D_low_omega":    "#27ae60",  # green
    "TRGB_centered":   "#8e44ad",  # purple
}

# ============================================================
# Plot 1: Age comparison bar chart
# ============================================================
def plot_ages():
    fig, ax = plt.subplots(figsize=(12, 6))

    names = ["Planck_LCDM", "5D_minimal", "5D_stabilized", "5D_thawing",
             "5D_DESI", "TRGB_centered", "5D_low_omega"]
    labels = [
        "Planck LCDM\n(baseline)",
        "5D Minimal\n(tower only)",
        "5D Stabilized\n(w=-1, mirror)",
        "5D Thawing\n(w=-0.85)",
        "5D DESI\n(w=-0.80)",
        "5D TRGB\n(H0=69.8)",
        "5D Low-Omega\n(less mirror DM)",
    ]

    with open(os.path.join(outdir, "results.json")) as f:
        results = json.load(f)

    ages = [results[n]["age_Gyr"] for n in names]
    cols = [colors.get(n, "#333") for n in names]

    bars = ax.barh(range(len(names)), ages, color=cols, alpha=0.85, height=0.6)

    # Add age labels on bars
    for i, (bar, age) in enumerate(zip(bars, ages)):
        ax.text(age - 0.3, i, f"{age:.2f} Gyr", va='center', ha='right',
                color='white', fontweight='bold', fontsize=11)

    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel("Age of Universe (Gyr)", fontsize=12)
    ax.set_title("Age of the Universe: 5D Framework vs Planck LCDM", fontsize=14, fontweight='bold')

    # Add reference lines
    ax.axvline(x=13.797, color='#2c3e50', linestyle='--', alpha=0.5, label='Planck LCDM = 13.80 Gyr')
    ax.axvline(x=12.5, color='gray', linestyle=':', alpha=0.3, label='Oldest globular clusters ~12.5 Gyr')

    ax.set_xlim(12.5, 14.2)
    ax.legend(loc='lower right', fontsize=9)
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "plot_ages.png"), dpi=150)
    print("  Saved: plot_ages.png")


# ============================================================
# Plot 2: S8 tension diagram
# ============================================================
def plot_s8():
    fig, ax = plt.subplots(figsize=(10, 6))

    with open(os.path.join(outdir, "results.json")) as f:
        results = json.load(f)

    # Observational data
    obs = [
        ("Planck 2018 (CMB)", 0.832, 0.013, "#2c3e50"),
        ("DES Y3 (WL)", 0.776, 0.017, "#3498db"),
        ("KiDS-1000 (WL)", 0.759, 0.024, "#2ecc71"),
        ("HSC Y3 (WL)", 0.763, 0.020, "#9b59b6"),
    ]

    y_obs = list(range(len(obs)))
    for i, (name, val, err, col) in enumerate(obs):
        ax.errorbar(val, i, xerr=err, fmt='o', color=col, markersize=10,
                    capsize=5, label=name, zorder=10)

    # Framework predictions
    y_offset = len(obs) + 0.5
    fw_scenarios = ["5D_stabilized", "5D_thawing", "5D_DESI", "5D_low_omega"]
    fw_labels = ["5D Stabilized", "5D Thawing (w=-0.85)", "5D DESI (w=-0.80)", "5D Low Omega_m"]

    for i, (scen, label) in enumerate(zip(fw_scenarios, fw_labels)):
        s8 = results[scen]["S8"]
        ax.plot(s8, y_offset + i, 's', color=colors.get(scen, 'red'),
                markersize=12, zorder=10, label=f"{label}: S8={s8:.3f}")

    ax.set_yticks(list(range(len(obs))) + [y_offset + i for i in range(len(fw_scenarios))])
    ax.set_yticklabels([o[0] for o in obs] + fw_labels, fontsize=9)
    ax.set_xlabel("S8 = sigma_8 * sqrt(Omega_m / 0.3)", fontsize=12)
    ax.set_title("S8 Tension: 5D Framework Predictions vs Observations", fontsize=14, fontweight='bold')

    # Planck band
    ax.axvspan(0.832 - 0.013, 0.832 + 0.013, alpha=0.1, color='#2c3e50', label='Planck 1-sigma')
    # WL band
    ax.axvspan(0.759 - 0.024, 0.776 + 0.017, alpha=0.1, color='#2ecc71', label='Weak lensing range')

    ax.set_xlim(0.65, 0.90)
    ax.invert_yaxis()
    ax.legend(loc='lower left', fontsize=7, ncol=2)

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "plot_s8.png"), dpi=150)
    print("  Saved: plot_s8.png")


# ============================================================
# Plot 3: Expansion history H(z)
# ============================================================
def plot_Hz():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    scenarios_to_plot = {
        "Planck_LCDM": {"H0": 67.36, "ombh2": 0.02237, "omch2": 0.1200,
                        "mnu": 0.06, "nnu": 3.044, "w": -1.0, "wa": 0.0},
        "5D_thawing": {"H0": 69.5, "ombh2": 0.02237, "omch2": 0.1200,
                       "mnu": 0.06, "nnu": 3.39, "w": -0.85, "wa": -0.23},
        "5D_DESI": {"H0": 69.5, "ombh2": 0.02237, "omch2": 0.1200,
                    "mnu": 0.06, "nnu": 3.39, "w": -0.80, "wa": -0.30},
        "5D_low_omega": {"H0": 69.5, "ombh2": 0.02237, "omch2": 0.1050,
                         "mnu": 0.06, "nnu": 3.39, "w": -0.85, "wa": -0.23},
    }

    z_arr = np.linspace(0, 3, 200)

    for name, params in scenarios_to_plot.items():
        pars = camb.CAMBparams()
        pars.set_cosmology(H0=params["H0"], ombh2=params["ombh2"],
                          omch2=params["omch2"], mnu=params["mnu"],
                          nnu=params["nnu"], tau=0.054)
        if params["wa"] != 0:
            pars.set_dark_energy(w=params["w"], wa=params["wa"], dark_energy_model='ppf')
        else:
            pars.set_dark_energy(w=params["w"])
        pars.InitPower.set_params(As=2.1e-9, ns=0.9649)
        results = camb.get_results(pars)

        H_values = [results.hubble_parameter(z) for z in z_arr]
        col = colors.get(name, '#333')

        # Absolute H(z)
        ax1.plot(z_arr, H_values, color=col, linewidth=2, label=name.replace('_', ' '))

        # Ratio to LCDM
        if name == "Planck_LCDM":
            H_lcdm = np.array(H_values)
        else:
            ratio = np.array(H_values) / H_lcdm
            ax2.plot(z_arr, ratio, color=col, linewidth=2, label=name.replace('_', ' '))

    ax1.set_xlabel("Redshift z", fontsize=12)
    ax1.set_ylabel("H(z) [km/s/Mpc]", fontsize=12)
    ax1.set_title("Expansion History H(z)", fontsize=14, fontweight='bold')
    ax1.legend(fontsize=9)
    ax1.set_xlim(0, 3)

    ax2.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5)
    ax2.set_xlabel("Redshift z", fontsize=12)
    ax2.set_ylabel("H(z) / H_LCDM(z)", fontsize=12)
    ax2.set_title("Ratio to Planck LCDM", fontsize=14, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.set_xlim(0, 3)
    ax2.set_ylim(0.97, 1.08)

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "plot_Hz.png"), dpi=150)
    print("  Saved: plot_Hz.png")


# ============================================================
# Plot 4: Dark energy equation of state w(z)
# ============================================================
def plot_wz():
    fig, ax = plt.subplots(figsize=(10, 6))

    z_arr = np.linspace(0, 5, 200)

    # w(z) = w0 + wa * z/(1+z)
    scenarios_w = {
        "Planck LCDM (w=-1)": (-1.0, 0.0, "#2c3e50"),
        "5D Thawing dilaton (w0=-0.85)": (-0.85, -0.23, "#e67e22"),
        "5D DESI-compatible (w0=-0.80)": (-0.80, -0.30, "#f39c12"),
        "DESI DR2 best-fit (w0=-0.75)": (-0.75, -0.75, "#e74c3c"),
    }

    for label, (w0, wa, col) in scenarios_w.items():
        w_z = w0 + wa * z_arr / (1 + z_arr)
        ax.plot(z_arr, w_z, color=col, linewidth=2.5, label=label)

    ax.axhline(y=-1, color='gray', linestyle=':', alpha=0.5)
    ax.axhline(y=-1/3, color='gray', linestyle=':', alpha=0.3)
    ax.text(4.5, -0.95, 'w = -1 (cosmological constant)', fontsize=8, color='gray')
    ax.text(4.5, -0.28, 'w = -1/3 (acceleration boundary)', fontsize=8, color='gray')

    ax.set_xlabel("Redshift z", fontsize=12)
    ax.set_ylabel("w(z) = P/rho", fontsize=12)
    ax.set_title("Dark Energy Equation of State: 5D Dilaton vs DESI", fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, loc='lower left')
    ax.set_xlim(0, 5)
    ax.set_ylim(-2.0, -0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "plot_wz.png"), dpi=150)
    print("  Saved: plot_wz.png")


# ============================================================
# Plot 5: Key parameter comparison summary
# ============================================================
def plot_summary():
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    with open(os.path.join(outdir, "results.json")) as f:
        results = json.load(f)

    scenarios = ["Planck_LCDM", "5D_minimal", "5D_stabilized", "5D_thawing",
                 "5D_DESI", "TRGB_centered"]
    short_labels = ["Planck", "5D Min", "5D Stab", "5D Thaw", "5D DESI", "5D TRGB"]
    cols = [colors.get(s, '#333') for s in scenarios]

    params = [
        ("age_Gyr", "Age (Gyr)", [13.797], ["Planck"]),
        ("rd_Mpc", "Sound Horizon r_d (Mpc)", [147.10], ["Planck"]),
        ("sigma8", "sigma_8", [0.811], ["Planck"]),
        ("S8", "S8", [0.832, 0.776], ["Planck CMB", "DES WL"]),
        ("Omega_m", "Omega_m", [0.315], ["Planck"]),
        ("H0", "H_0 (km/s/Mpc)", [67.4, 73.0, 69.8], ["Planck", "SH0ES", "TRGB"]),
    ]

    for idx, (key, title, ref_vals, ref_labels) in enumerate(params):
        ax = axes[idx // 3][idx % 3]
        values = [results[s][key] for s in scenarios]

        bars = ax.bar(range(len(scenarios)), values, color=cols, alpha=0.85)
        ax.set_xticks(range(len(scenarios)))
        ax.set_xticklabels(short_labels, fontsize=8, rotation=30)
        ax.set_title(title, fontsize=11, fontweight='bold')

        # Reference lines
        ref_colors = ['#2c3e50', '#e74c3c', '#8e44ad', '#27ae60']
        for rv, rl, rc in zip(ref_vals, ref_labels, ref_colors):
            ax.axhline(y=rv, color=rc, linestyle='--', alpha=0.5, linewidth=1)

        # Add value labels on bars
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                    f'{val:.2f}', ha='center', va='bottom', fontsize=7)

    plt.suptitle("5D Framework Cosmological Predictions: Summary",
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "plot_summary.png"), dpi=150, bbox_inches='tight')
    print("  Saved: plot_summary.png")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("\n  Generating plots...")
    plot_ages()
    plot_s8()
    plot_Hz()
    plot_wz()
    plot_summary()
    print("\n  All plots generated.")
