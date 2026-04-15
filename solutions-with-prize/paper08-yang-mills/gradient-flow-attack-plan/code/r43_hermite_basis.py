"""R43: Re-run R38-R42 diagnostics in a HERMITE basis.

R42 diagnosed the μ_1 staircase and the even-simple property as
BAND-EDGE artifacts of the Fourier truncation on [-L/2, L/2]. The
recommendation (R42 §5, follow-up 1) was:

    "Repeat in a Hermite basis (which has no hard band edge).
     If the staircase vanishes there, that confirms the artifact
     diagnosis."

This file implements the Connes-Consani Weil quadratic form Q_W in a
scaled Hermite function basis

    φ_n(u) = σ^{-1/2} · h_n(u/σ),  h_n(x) = (2^n n! √π)^{-1/2} H_n(x) e^{-x²/2}

on L²(R), and re-runs the four diagnostics that gave Walls 28-35 plus
the random-ensemble control from R40 P4.

The underlying operator is the SAME as in R38 / R42: Q_W = Q_pole + Σ_p Q_p,
where each piece is a convolution operator on L²(R) with kernel

    k_pole(w) = 2 cosh(w/2) · 1_{|w| ≤ L}
    k_p(w)    = -Σ_{k≥1} (log p / p^{k/2}) · [δ(w − k log p) + δ(w + k log p)]

(The [-L/2,L/2] support of k_pole is retained so that at large Hermite
basis size we reproduce the R38 operator; what changes is the BASIS we
project it onto, which no longer has a hard band edge.)

Matrix elements in the Hermite basis are computed by quadrature on a
dense u-grid that is wide enough to contain the Hermite mass and fine
enough to resolve the largest log p atom.

Usage:
    python code/r43_hermite_basis.py              # full run
"""

import json
import os
import sys
import time
import numpy as np
from math import log, sqrt, pi
from scipy.special import eval_hermite

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)

from r41c_mu1_trajectory import primes_up_to
from r40p4_mechanism import gen_uniform, gen_Q_dependent, gen_resonant

GAMMAS = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
          37.586178, 40.918719, 43.327073, 48.005151, 49.773832]


# ---------------------------------------------------------------------------
# Hermite basis on a grid.
# ---------------------------------------------------------------------------

def hermite_basis_on_grid(N_basis, sigma, u_grid):
    """Return Phi[j, n] = phi_n(u_j) * sqrt(du), j = grid index, n = basis idx.

    phi_n(u) = sigma^{-1/2} * h_n(u/sigma), with h_n L²(R)-orthonormal.

    We use the stable recursion for h_n:
        h_0(x) = pi^{-1/4} e^{-x²/2}
        h_1(x) = sqrt(2) * x * h_0(x)
        h_{n+1}(x) = sqrt(2/(n+1)) * x * h_n(x) − sqrt(n/(n+1)) * h_{n-1}(x)
    which avoids the overflow of H_n(x).
    """
    du = float(u_grid[1] - u_grid[0])
    x = u_grid / sigma
    Ng = len(u_grid)
    Phi = np.empty((Ng, N_basis), dtype=float)
    h0 = (pi ** -0.25) * np.exp(-0.5 * x * x)
    Phi[:, 0] = h0
    if N_basis >= 2:
        Phi[:, 1] = np.sqrt(2.0) * x * h0
    for n in range(1, N_basis - 1):
        Phi[:, n + 1] = (np.sqrt(2.0 / (n + 1)) * x * Phi[:, n]
                         - np.sqrt(n / (n + 1.0)) * Phi[:, n - 1])
    Phi /= np.sqrt(sigma)
    Phi *= np.sqrt(du)
    return Phi  # approximately column-orthonormal: Phi.T @ Phi ≈ I


def make_grid(lam, sigma, N_basis, pad_sigma=6.0, n_per_sigma=40):
    """Build a u-grid wide enough for (i) the Hermite mass (sigma·sqrt(2N+1))
    and (ii) the band-limited pole kernel extent [-L, L], and fine enough
    for the highest-frequency prime atoms."""
    L = 2.0 * log(lam)
    hermite_extent = sigma * sqrt(2 * N_basis + 1) + pad_sigma * sigma
    half = max(hermite_extent, 1.5 * L)
    # Grid spacing: must resolve smallest atom-separation.  We use
    # du ≈ sigma / n_per_sigma so every Hermite oscillation has n_per_sigma points.
    du = sigma / n_per_sigma
    n_half = int(np.ceil(half / du))
    u = np.arange(-n_half, n_half + 1) * du
    return u, du, L


# ---------------------------------------------------------------------------
# Q_pole and Q_p in Hermite basis.
# ---------------------------------------------------------------------------

def q_pole_hermite(Phi, u_grid, L):
    """Q_pole[m,n] = <phi_m | K_pole | phi_n>
       K_pole f(u) = ∫ 2 cosh((u-v)/2) · 1_{|u-v|≤L} f(v) dv

    Since K_pole is a Toeplitz convolution, we compute it by FFT: form
    g_n(u) = (k_pole * phi_n)(u), then Q_pole[m,n] = <phi_m, g_n>.
    """
    du = float(u_grid[1] - u_grid[0])
    # Build the kernel k_pole(w) on the same grid w = u_grid (centred)
    w = u_grid.copy()
    k = np.where(np.abs(w) <= L, 2.0 * np.cosh(w / 2.0), 0.0)
    Ng, Nb = Phi.shape
    # Phi already has sqrt(du) absorbed; remove for function evaluation
    phi_vals = Phi / sqrt(du)   # phi_vals[j,n] = phi_n(u_j)
    # Convolution (k * phi_n)(u) = Σ_v k(u - v) phi_n(v) du'
    # via FFT.  Use 'same'-mode linear convolution.
    from scipy.signal import fftconvolve
    KPhi = np.empty_like(phi_vals)
    for n in range(Nb):
        KPhi[:, n] = fftconvolve(phi_vals[:, n], k, mode='same') * du
    # Q_pole[m,n] = ∫ phi_m(u) (K phi_n)(u) du = Σ_j phi_m(u_j) KPhi[j,n] du
    Qp = (phi_vals.T @ KPhi) * du
    Qp = 0.5 * (Qp + Qp.T)
    return Qp


def translation_matrix(Phi, u_grid, sigma, N_basis, a):
    """S_a[m,n] = ∫ phi_m(u) phi_n(u - a) du, computed by quadrature.

    Reuses the Hermite recursion: phi_n(u - a) evaluated at u_j equals
    phi_n at grid (u_j - a)/sigma. We build a second basis matrix at the
    shifted argument via the same recursion.
    """
    du = float(u_grid[1] - u_grid[0])
    # Evaluate phi_n on shifted grid.
    Phi_shift = hermite_basis_on_grid(N_basis, sigma, u_grid - a)  # has sqrt(du) baked
    # S[m,n] = Σ_j (Phi[j,m]/sqrt(du)) · (Phi_shift[j,n]/sqrt(du)) · du
    #        = Σ_j Phi[j,m] Phi_shift[j,n] / du · du  →  just Phi.T @ Phi_shift
    S = Phi.T @ Phi_shift
    return S  # (N_basis, N_basis)


def q_prime_contrib_hermite(Phi, u_grid, sigma, N_basis, p, L, cache):
    """Total -log contribution of prime p:
        Q_p = -Σ_{k≥1} (log p / p^{k/2}) · (S_{+k log p} + S_{-k log p})
    Only powers with k log p ≤ L are included (matches R38)."""
    log_p = log(p)
    Q = np.zeros((N_basis, N_basis))
    kmax = int(L / log_p)
    for k in range(1, kmax + 1):
        a = k * log_p
        if a > L:
            break
        coeff = log_p / (p ** (k / 2.0))
        # Symmetric part: S_a + S_{-a}. Use cache on |a|.
        key = round(a, 10)
        if key in cache:
            S_sym = cache[key]
        else:
            S_pos = translation_matrix(Phi, u_grid, sigma, N_basis, a)
            S_neg = translation_matrix(Phi, u_grid, sigma, N_basis, -a)
            S_sym = S_pos + S_neg
            cache[key] = S_sym
        Q -= coeff * S_sym
    Q = 0.5 * (Q + Q.T)
    return Q


# ---------------------------------------------------------------------------
# Even subspace in Hermite basis.
# ---------------------------------------------------------------------------
# Hermite functions have definite parity: phi_n even iff n even, odd iff n odd.
# So the "even subspace" projector is just the diagonal selector of even n's.

def even_eigs_hermite(Q, N_basis, tol=1e-10):
    """Diagonalise Q restricted to even-index rows/cols (parity eigenspaces)."""
    even_idx = np.arange(0, N_basis, 2)
    Qe = Q[np.ix_(even_idx, even_idx)]
    Qe = 0.5 * (Qe + Qe.T)
    vals, vecs = np.linalg.eigh(Qe)
    order = np.argsort(vals)
    return vals[order], vecs[:, order], even_idx


# ---------------------------------------------------------------------------
# Drivers: build full Q_W for a prime list, return sorted even eigenvalues.
# ---------------------------------------------------------------------------

def build_QW_hermite(lam, sigma, N_basis, primes, n_per_sigma=40, pad_sigma=6.0):
    u_grid, du, L = make_grid(lam, sigma, N_basis,
                              pad_sigma=pad_sigma, n_per_sigma=n_per_sigma)
    Phi = hermite_basis_on_grid(N_basis, sigma, u_grid)
    Q_pole = q_pole_hermite(Phi, u_grid, L)
    cache = {}
    Q_prime = np.zeros_like(Q_pole)
    for p in primes:
        Q_prime += q_prime_contrib_hermite(Phi, u_grid, sigma, N_basis, p, L, cache)
    Q = Q_pole + Q_prime
    return Q, Q_pole, Q_prime, Phi, u_grid


def trajectory_hermite(lam, sigma, N_basis, primes, n_per_sigma=40,
                       pad_sigma=6.0, want_vecs=False):
    """Add primes one at a time; track μ_1 on the even subspace."""
    u_grid, du, L = make_grid(lam, sigma, N_basis,
                              pad_sigma=pad_sigma, n_per_sigma=n_per_sigma)
    Phi = hermite_basis_on_grid(N_basis, sigma, u_grid)
    Q_pole = q_pole_hermite(Phi, u_grid, L)
    Q = Q_pole.copy()
    cache = {}
    rows = []
    vecs = {}
    for k, p in enumerate(primes, 1):
        Q += q_prime_contrib_hermite(Phi, u_grid, sigma, N_basis, p, L, cache)
        vals, vv, ev_idx = even_eigs_hermite(Q, N_basis)
        if len(vals) >= 2:
            mu1 = float(vals[0]); mu2 = float(vals[1])
        elif len(vals):
            mu1 = float(vals[0]); mu2 = float('nan')
        else:
            mu1 = float('nan'); mu2 = float('nan')
        rows.append({"N": k, "p_N": int(p), "mu1": mu1, "mu2": mu2,
                     "gap": mu2 - mu1})
        if want_vecs:
            vecs[k] = (mu1, vv[:, 0].tolist(), ev_idx.tolist())
    return rows, vecs


# ---------------------------------------------------------------------------
# Plateau / drop analytics (copied from r42 for comparability).
# ---------------------------------------------------------------------------

def detect_plateaus(rows, eps=0.05, min_len=3):
    mus = [r["mu1"] for r in rows]
    out = []
    i = 0; n = len(mus)
    while i < n:
        j = i
        while j + 1 < n and abs(mus[j+1] - mus[j]) < eps:
            j += 1
        if j - i + 1 >= min_len:
            seg = mus[i:j+1]
            out.append({"N_start": i+1, "N_end": j+1,
                        "mu_mean": float(np.mean(seg)),
                        "mu_std": float(np.std(seg))})
        i = j + 1
    return out


def detect_drops(rows, thresh=0.5):
    drops = []
    for k in range(1, len(rows)):
        d = rows[k]["mu1"] - rows[k-1]["mu1"]
        if d < -thresh:
            drops.append({"N": rows[k]["N"], "p_N": rows[k].get("p_N"),
                          "delta": float(d),
                          "mu1_after": float(rows[k]["mu1"])})
    return drops


# ---------------------------------------------------------------------------
# Baseline sanity check vs R38 Fourier builder.
# ---------------------------------------------------------------------------

def baseline_check():
    """At small N (5 primes), reproduce the R38 first-cut number (~ −13.10)
    in the Hermite basis and compare to a direct R38 Fourier call at the
    same (lam, primes)."""
    from r38_krein_rutman_rh import connes_consani_fourier_weil_matrix
    from r42_staircase import build_pole, prime_contrib
    from r41c_mu1_trajectory import even_projector

    lam = 10.0
    primes = [2, 3, 5, 7, 11]
    # --- Fourier reference (R38 semantics, exact) ---
    N_modes_ref = 80
    Qf, _, _, _ = connes_consani_fourier_weil_matrix(lam, N_modes_ref, primes)
    Pe, _ = even_projector(N_modes_ref)
    Qfe = Pe @ Qf @ Pe
    Qfe = 0.5 * (Qfe + Qfe.T)
    vals_f = np.sort(np.linalg.eigvalsh(Qfe))
    mu1_f = float(vals_f[np.abs(vals_f) > 1e-9][0])

    # --- Hermite at several (N_basis, sigma) ---
    L = 2.0 * log(lam)
    results = []
    for N_basis, sigma in [(60, L/4), (100, L/4), (140, L/4),
                           (100, L/6), (100, L/3)]:
        t0 = time.time()
        Q, Qp, Qpr, Phi, ug = build_QW_hermite(lam, sigma, N_basis, primes)
        vals, _, _ = even_eigs_hermite(Q, N_basis)
        mu1 = float(vals[0]) if len(vals) else float('nan')
        # Sanity: Hermite orthonormality
        ortho_err = float(np.max(np.abs(Phi.T @ Phi - np.eye(N_basis))))
        tr = float(np.trace(Q))
        results.append({"N_basis": N_basis, "sigma": sigma,
                        "mu1_even": mu1, "ortho_err": ortho_err,
                        "trace_Q": tr, "t": time.time() - t0})
    return {"fourier_mu1": mu1_f, "fourier_Nmodes": N_modes_ref,
            "lam": lam, "primes": primes, "hermite": results}


# ---------------------------------------------------------------------------
# (a) Even-simple stability, (b) μ_1 trajectory.
# ---------------------------------------------------------------------------

def diag_ab(lam=68.63, sigma=None, N_basis=120, max_primes=60):
    """μ_1, μ_2, gap for first max_primes primes, at (N_basis, sigma)."""
    if sigma is None:
        sigma = 2.0 * log(lam) / 4.0
    primes = primes_up_to(2000)[:max_primes]
    rows, _ = trajectory_hermite(lam, sigma, N_basis, primes)
    return {"lam": lam, "sigma": sigma, "N_basis": N_basis,
            "rows": rows,
            "plateaus": detect_plateaus(rows, eps=0.05, min_len=3),
            "drops": detect_drops(rows, thresh=0.5)}


# ---------------------------------------------------------------------------
# (c) N_basis stability — the killer test.
# ---------------------------------------------------------------------------

def diag_c_Nbasis(lam=68.63, sigma=None, N_primes=11,
                  Nb_list=(40, 60, 80, 100, 120, 160, 200)):
    if sigma is None:
        sigma = 2.0 * log(lam) / 4.0
    primes = primes_up_to(2000)[:N_primes]
    out = []
    for Nb in Nb_list:
        t0 = time.time()
        Q, _, _, _, _ = build_QW_hermite(lam, sigma, Nb, primes)
        vals, _, _ = even_eigs_hermite(Q, Nb)
        mu1 = float(vals[0]) if len(vals) else float('nan')
        mu2 = float(vals[1]) if len(vals) > 1 else float('nan')
        out.append({"N_basis": Nb, "mu1": mu1, "mu2": mu2,
                    "gap": mu2 - mu1, "t": time.time() - t0})
        print(f"  [diag C] N_basis={Nb:4d}  μ1={mu1:+.5f}  μ2={mu2:+.5f}  "
              f"gap={mu2-mu1:.3f}  [{out[-1]['t']:.1f}s]")
    return {"lam": lam, "sigma": sigma, "N_primes": N_primes, "rows": out}


# ---------------------------------------------------------------------------
# (d) σ stability.
# ---------------------------------------------------------------------------

def diag_d_sigma(lam=68.63, N_basis=120, N_primes=11,
                 sigma_factors=(0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6)):
    L = 2.0 * log(lam)
    primes = primes_up_to(2000)[:N_primes]
    out = []
    for f in sigma_factors:
        sigma = f * L
        t0 = time.time()
        Q, _, _, _, _ = build_QW_hermite(lam, sigma, N_basis, primes)
        vals, _, _ = even_eigs_hermite(Q, N_basis)
        mu1 = float(vals[0]) if len(vals) else float('nan')
        mu2 = float(vals[1]) if len(vals) > 1 else float('nan')
        out.append({"sigma": sigma, "sigma_over_L": f,
                    "mu1": mu1, "mu2": mu2, "gap": mu2 - mu1,
                    "t": time.time() - t0})
        print(f"  [diag D] sigma/L={f:.2f}  μ1={mu1:+.5f}  μ2={mu2:+.5f}  "
              f"gap={mu2-mu1:.3f}")
    return {"lam": lam, "L": L, "N_basis": N_basis, "N_primes": N_primes,
            "rows": out}


# ---------------------------------------------------------------------------
# Random ensemble re-test of even-simple.
# ---------------------------------------------------------------------------

def random_ensemble_even_simple(lam=68.63, sigma=None, N_basis=100,
                                N_atoms=20, n_trials=10, seed=2027):
    """For each ensemble (uniform, Q_dependent, resonant), build Q_W with
    the prescribed log-atoms in the Hermite basis and test whether the
    ground state of the even-subspace restriction is simple (gap > 1e-6)."""
    if sigma is None:
        sigma = 2.0 * log(lam) / 4.0
    L = 2.0 * log(lam)
    u_grid, du, _ = make_grid(lam, sigma, N_basis, pad_sigma=6.0, n_per_sigma=30)
    Phi = hermite_basis_on_grid(N_basis, sigma, u_grid)
    Q_pole = q_pole_hermite(Phi, u_grid, L)
    rng = np.random.default_rng(seed)
    ens = [("uniform", gen_uniform),
           ("Q_dependent", gen_Q_dependent),
           ("resonant", gen_resonant)]
    out = {}
    for name, gen in ens:
        results = []
        for t in range(n_trials):
            log_set = gen(N_atoms, lam, rng)
            log_set = [ell for ell in log_set if ell <= L - 1e-6]
            Q = Q_pole.copy()
            cache = {}
            for ell in log_set:
                coeff = 0.5 * ell * np.exp(-ell / 2)  # matches r42
                # one atom contribution: -coeff*(S_+ell + S_-ell)
                Sp = translation_matrix(Phi, u_grid, sigma, N_basis, ell)
                Sn = translation_matrix(Phi, u_grid, sigma, N_basis, -ell)
                Q -= coeff * (Sp + Sn)
            vals, _, _ = even_eigs_hermite(Q, N_basis)
            if len(vals) >= 2:
                mu1, mu2 = float(vals[0]), float(vals[1])
                simple = (mu2 - mu1) > 1e-6
            else:
                mu1 = float(vals[0]) if len(vals) else float('nan')
                mu2 = float('nan'); simple = None
            results.append({"trial": t, "n_atoms": len(log_set),
                            "mu1": mu1, "mu2": mu2, "gap": mu2 - mu1,
                            "simple": simple})
        frac_simple = sum(1 for r in results
                          if r["simple"]) / max(1, len(results))
        out[name] = {"trials": results, "frac_even_simple": frac_simple}
        print(f"  [random] {name:12s}  even-simple fraction = {frac_simple:.2f}")
    return out


# ---------------------------------------------------------------------------
# Main.
# ---------------------------------------------------------------------------

def main():
    report = {}
    print("=" * 72)
    print("R43 — Hermite basis rerun of R38-R42")
    print("=" * 72)

    print("\n[0] Baseline check vs R38 Fourier at small N")
    b = baseline_check()
    report["baseline"] = b
    print(f"  Fourier reference (N_modes={b['fourier_Nmodes']}):  μ1_even = {b['fourier_mu1']:+.5f}")
    for r in b["hermite"]:
        print(f"  Hermite N_basis={r['N_basis']:4d}  sigma={r['sigma']:.3f}  "
              f"μ1_even={r['mu1_even']:+.5f}  trace={r['trace_Q']:+.3e}  "
              f"ortho_err={r['ortho_err']:.1e}  [{r['t']:.1f}s]")

    print("\n[A,B] Even-simple + μ_1 trajectory at (lam=68.63, Nb=120)")
    ab = diag_ab(lam=68.63, N_basis=120, max_primes=60)
    report["diag_ab"] = ab
    mus = [r["mu1"] for r in ab["rows"]]
    gaps = [r["gap"] for r in ab["rows"]]
    print(f"  μ_1: N=1 → {mus[0]:+.4f},  N=5 → {mus[4]:+.4f},  "
          f"N=10 → {mus[9]:+.4f},  N=20 → {mus[19]:+.4f},  "
          f"N=40 → {mus[39]:+.4f},  N=60 → {mus[-1]:+.4f}")
    gap_min = min(gaps); idx_min = int(np.argmin(gaps)) + 1
    print(f"  min gap = {gap_min:.3e} at N={idx_min}")
    even_simple_all = all(g > 1e-6 for g in gaps)
    print(f"  all N even-simple: {even_simple_all}")
    print(f"  plateaus: {len(ab['plateaus'])}   drops: {len(ab['drops'])}")

    print("\n[C] N_basis stability at N_primes=11, (lam=68.63, sigma=L/4)")
    c = diag_c_Nbasis(lam=68.63, N_primes=11,
                      Nb_list=(40, 60, 80, 100, 140, 180))
    report["diag_c"] = c

    print("\n[D] sigma stability at N_basis=120, N_primes=11")
    L = 2.0 * log(68.63)
    d_rows = []
    for f in [0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]:
        sigma = f * L
        t0 = time.time()
        primes = primes_up_to(2000)[:11]
        Q, _, _, _, _ = build_QW_hermite(68.63, sigma, 120, primes)
        vals, _, _ = even_eigs_hermite(Q, 120)
        mu1 = float(vals[0]); mu2 = float(vals[1])
        d_rows.append({"sigma": sigma, "sigma_over_L": f,
                       "mu1": mu1, "mu2": mu2, "gap": mu2 - mu1,
                       "t": time.time() - t0})
        print(f"  sigma/L={f:.2f}  μ1={mu1:+.5f}  μ2={mu2:+.5f}  gap={mu2-mu1:.3f}")
    report["diag_d"] = {"L": L, "N_basis": 120, "N_primes": 11, "rows": d_rows}

    print("\n[Random ensembles] even-simple in Hermite")
    re = random_ensemble_even_simple(lam=68.63, N_basis=100,
                                     N_atoms=20, n_trials=6)
    report["random_ensembles"] = re

    out_path = os.path.join(CODE, "r43_hermite_basis.json")
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nSaved -> {out_path}")
    return report


if __name__ == "__main__":
    main()
