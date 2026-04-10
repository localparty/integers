"""R47 Lead 1: Is the γ_n subspectrum EXACTLY the even sector of Q_W?

Strategy: build the FULL Q_W in the Hermite basis (both even and odd rows/cols),
verify [Q_W, P_even] = 0 numerically, diagonalize the full operator, tag each
eigenvector by parity character, and ask: are the R46 γ_n-matching eigenvalues
even, odd, or mixed?

Key analytic observation we verify empirically:
    Hermite functions phi_n have parity (-1)^n.
    Q_pole kernel k_pole(w) = 2*cosh(w/2)*1_{|w|<=L} is EVEN in w.
    Q_p combines S_{+a} + S_{-a} which is EVEN.
    => [Q_W, P_even] = 0 exactly. Even/odd blocks decouple.

R46 restricted to even rows/cols via `even_eigs_hermite` BEFORE searching
for gamma_n. So every gamma_n match R46 reported is by construction an
EVEN eigenvalue. This script verifies this is not a numerical artifact
of basis leakage and checks the companion odd spectrum to see if ODD
eigenvalues ever land on a gamma_n.
"""
import json, os, sys, time
import numpy as np
from math import log, pi, exp, sqrt

CODE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE)
from r43_hermite_basis import build_QW_hermite, primes_up_to
from r45_large_lambda import choose_Nbasis

GAMMAS = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
          37.586178, 40.918719, 43.327073, 48.005151, 49.773832]

def saturated_primes(lam):
    L = 2.0 * log(lam)
    p_limit = int(exp(L)) + 1
    return [p for p in primes_up_to(p_limit) if log(p) <= L]

def parity_diag(N):
    """Return diag P_even (1 on even indices, 0 on odd)."""
    d = np.zeros(N)
    d[0::2] = 1.0
    return d

def analyze(lam, Nb, primes, sigma_factor=0.25, n_per_sigma=14, pad_sigma=3.0,
            label=""):
    L = 2.0 * log(lam)
    sigma = sigma_factor * L
    t0 = time.time()
    Q, _, _, _, _ = build_QW_hermite(lam, sigma, Nb, primes,
                                     n_per_sigma=n_per_sigma,
                                     pad_sigma=pad_sigma)
    Q = 0.5 * (Q + Q.T)
    # Parity commutator
    d = parity_diag(Nb)
    # P Q - Q P: (d[:,None]*Q) - (Q*d[None,:])
    comm = (d[:, None] * Q) - (Q * d[None, :])
    comm_norm = float(np.linalg.norm(comm))
    q_norm = float(np.linalg.norm(Q))
    # Largest off-parity entry: Q[m,n] with m even, n odd (should be 0)
    eo_block = Q[0::2, 1::2]
    eo_max = float(np.max(np.abs(eo_block)))
    # Full diagonalization
    vals, vecs = np.linalg.eigh(Q)
    order = np.argsort(vals)
    vals = vals[order]; vecs = vecs[:, order]
    # Parity character of each eigenvector: sum of |c_n|^2 over even n minus odd n
    ev_sq = vecs ** 2
    p_even = ev_sq[0::2, :].sum(axis=0)   # in [0,1]
    p_odd  = ev_sq[1::2, :].sum(axis=0)
    chi = p_even - p_odd  # +1 = pure even, -1 = pure odd
    # Classify
    tags = np.where(chi > 0.99, "E", np.where(chi < -0.99, "O", "M"))
    n_E = int((tags == "E").sum())
    n_O = int((tags == "O").sum())
    n_M = int((tags == "M").sum())
    # gamma_n matching: for each gamma, find closest eigenvalue (also -gamma)
    gamma_rows = []
    for n, g in enumerate(GAMMAS, 1):
        for target in (g, -g):
            k = int(np.argmin(np.abs(vals - target)))
            mu = float(vals[k])
            rel = abs(mu - target) / max(1e-12, abs(target))
            gamma_rows.append({
                "n": n, "gamma": g, "target": target,
                "idx": k, "mu": mu, "rel_err": rel,
                "chi": float(chi[k]), "tag": str(tags[k]),
            })
    # Fraction of gamma matches with tag=E, rel_err<1e-2
    good = [r for r in gamma_rows if r["rel_err"] < 1e-2]
    frac_even_good = (sum(1 for r in good if r["tag"] == "E") / len(good)) if good else None
    # Odd eigenvalues within rel_err 1e-3 of any gamma (both signs)
    odd_idx = np.where(tags == "O")[0]
    odd_near = 0
    for k in odd_idx:
        mu = vals[k]
        best = min(abs(abs(mu) - g) / g for g in GAMMAS)
        if best < 1e-3:
            odd_near += 1
    # Statistical separation: mean min-dist to +-gamma for even vs odd
    def min_gdist(v):
        return min(min(abs(v - g), abs(v + g)) for g in GAMMAS)
    even_idx = np.where(tags == "E")[0]
    # restrict to eigenvalues in the gamma range [-55, 55]
    mask_E = [k for k in even_idx if -55 < vals[k] < 55]
    mask_O = [k for k in odd_idx  if -55 < vals[k] < 55]
    mean_dE = float(np.mean([min_gdist(vals[k]) for k in mask_E])) if mask_E else None
    mean_dO = float(np.mean([min_gdist(vals[k]) for k in mask_O])) if mask_O else None
    dt = time.time() - t0
    print(f"[{label}] lam={lam} Nb={Nb} Np={len(primes)} "
          f"||[Q,P]||={comm_norm:.2e} ||Q||={q_norm:.2e} "
          f"eo_max={eo_max:.2e} E={n_E} O={n_O} M={n_M} "
          f"frac_even_good={frac_even_good} odd_near_gamma={odd_near} "
          f"<dE>={mean_dE} <dO>={mean_dO} [{dt:.1f}s]")
    return {
        "label": label, "lam": lam, "Nb": Nb, "Np": len(primes),
        "comm_norm": comm_norm, "q_norm": q_norm,
        "comm_rel": comm_norm / max(1e-30, q_norm),
        "eo_block_max": eo_max,
        "n_even": n_E, "n_odd": n_O, "n_mixed": n_M,
        "frac_even_of_good_gamma_matches": frac_even_good,
        "odd_near_gamma_count": odd_near,
        "mean_dist_even_to_gamma": mean_dE,
        "mean_dist_odd_to_gamma":  mean_dO,
        "gamma_rows": gamma_rows,
        "vals_min": float(vals[0]), "vals_max": float(vals[-1]),
        "time_s": dt,
    }

def main():
    out = {"runs": []}
    # PART 2+3+4: scan lambda at saturated primes
    lam_list = [40.0, 68.63, 100.0, 200.0, 300.0]
    for lam in lam_list:
        Nb = min(choose_Nbasis(lam), 700)
        primes = saturated_primes(lam)
        rec = analyze(lam, Nb, primes, label=f"sat_lam={lam}")
        out["runs"].append(rec)
    # PART 5: N_primes scan at lam=68.63
    lam = 68.63
    Nb = min(choose_Nbasis(lam), 700)
    full = saturated_primes(lam)
    for Np in [6, 11, 50, 100, len(full)]:
        primes = full[:Np]
        rec = analyze(lam, Nb, primes, label=f"Np={Np}_lam=68.63")
        out["runs"].append(rec)
    # PART 6: N_basis convergence at lam=68.63 Np=6 (CC case)
    primes6 = full[:6]
    for Nb in [400, 700, 1000, 1500]:
        rec = analyze(68.63, Nb, primes6, label=f"Nb={Nb}_CC6")
        out["runs"].append(rec)
    path = os.path.join(CODE, "r47l1_even_sector.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved -> {path}")

if __name__ == "__main__":
    main()
