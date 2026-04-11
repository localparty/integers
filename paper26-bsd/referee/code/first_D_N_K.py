"""First exploratory D_N^K over K = Q(i).

Purpose. Build the crudest possible Q_N^K-type Hermitian matrix from
Gaussian prime data, diagonalize it, and see whether *anything* about
its spectrum resembles the first non-trivial zeros of zeta_K.

This is not a rigorous port of Paper 13's construction. It is a toy
model built from the off-diagonal log-ratio kernel and a diagonal
Dedekind-Mangoldt term, with a few conventional variations from the
Paper-13 recipe thrown in to probe sensitivity.

Targets (imaginary parts of first zeros of zeta_K = zeta * L(chi_{-4})):
    L(chi_{-4}):   6.02, 10.24, 12.99, 16.34, 18.80, 21.55, ...
    zeta:         14.13, 21.02, 25.01, 30.42, 32.94, 37.59, ...
    merged:        6.02, 10.24, 12.99, 14.13, 16.34, 18.80, 21.02, 21.55, ...

Construction summary (baseline).
    (a) Gaussian prime ideals ordered by norm.
    (b) S = set of ideals with prime factors from the first N primes,
        truncated to the first M by norm.
    (c) Q_{ij} = -1/log(N_j/N_i) for N_i != N_j, 0 otherwise.
    (d) Q_{ii} = Lambda_K(a_i) / sqrt(N_i).
    (e) Symmetrize: Q <- (Q + Q^H)/2.
    (f) Eigenvalues sorted by |lambda|.

Variations explored:
    v1. diagonal sign flip  (c = -1)
    v2. diagonal halved     (c = 1/2)
    v3. archimedean shift   (diagonal -= 5.5)
    v4. rank-2 condensation around unit ideal index
    v5. prime-powers only   (drop composite smooths and drop unit)
    v6. larger M at N=5
    v7. Q analogue (rational primes, rational integers) as sanity check
    v8. same-norm off-diagonals regularized to epsilon/log(max_N)
"""

from __future__ import annotations

from itertools import product

import numpy as np
from sympy import factorint, isprime

# ---------------------------------------------------------------
# 1.  Gaussian prime enumeration (copied / adapted from
#     ccm_over_K_sanity.py so this file is self-contained)
# ---------------------------------------------------------------


def gaussian_primes_by_norm(max_norm: int):
    """Return list of (a, b, N(p)) for Gaussian primes p with norm <= max_norm.

    Same convention as ccm_over_K_sanity.py:
      - p = 2:        (1, 1)          ramified,  norm 2
      - p = 1 mod 4:  (a, b),(a,-b)   split,     norm p  (two primes)
      - p = 3 mod 4:  (p, 0)          inert,     norm p^2
    """
    primes = []
    for p in range(2, max_norm + 1):
        if not isprime(p):
            continue
        if p == 2:
            primes.append((1, 1, 2))
        elif p % 4 == 1:
            for a in range(1, int(p**0.5) + 1):
                b2 = p - a * a
                if b2 > 0:
                    b = int(round(b2**0.5))
                    if b * b == b2:
                        primes.append((a, b, p))
                        primes.append((a, -b, p))
                        break
        else:  # p = 3 mod 4
            if p * p <= max_norm:
                primes.append((p, 0, p * p))
    primes.sort(key=lambda t: (t[2], t[0], t[1]))
    return primes


# ---------------------------------------------------------------
# 2.  Smooth ideals: products of prime ideals from the first N primes
#     Each ideal is identified by the tuple of exponents
#     (k_1, k_2, ..., k_N) where k_j is the power of p_j in a.
# ---------------------------------------------------------------


def smooth_ideals(primes, M, max_exp=6):
    """Enumerate smooth ideals up to count M as tuples of (exponent tuple, norm).

    Includes the unit ideal exponent_tuple = (0,...,0) with norm 1.
    Ordered by norm, ties broken lexicographically.
    """
    norms = [p[2] for p in primes]
    N = len(primes)
    ideals = []
    # bounded exponent enumeration; keeps state small
    for expt in product(range(max_exp + 1), repeat=N):
        norm = 1
        for k, n in zip(expt, norms):
            norm *= n**k
        ideals.append((expt, norm))
    ideals.sort(key=lambda t: (t[1], t[0]))
    return ideals[:M]


def lambda_K_of_ideal(expt, primes):
    """Dedekind-Mangoldt: log N(p) if a = p^k (k >= 1), else 0.

    Unit ideal exponent_tuple (0,...,0) returns 0.
    """
    nonzero = [(i, k) for i, k in enumerate(expt) if k > 0]
    if len(nonzero) != 1:
        return 0.0
    i, _k = nonzero[0]
    return float(np.log(primes[i][2]))


# ---------------------------------------------------------------
# 3.  Build the Q matrix with a choice of variant
# ---------------------------------------------------------------


def build_Q(
    ideals,
    primes,
    *,
    diag_scale: float = 1.0,
    archimedean_shift: float = 0.0,
    cond_alpha: float = 0.0,
    cond_target_idx: int = 1,
    eps_same_norm: float = 0.0,
):
    """Assemble the Hermitian Q matrix.

    Parameters
    ----------
    diag_scale          scalar multiplying the Lambda_K/sqrt(N) diagonal
    archimedean_shift   scalar subtracted from diagonal (Paper 13 Estimate 1 motif)
    cond_alpha          strength of rank-2 condensation |0><0| + |0><k| + h.c.
    cond_target_idx     which basis element plays the role of e_p in the condensation
    eps_same_norm       nonzero -> regularize same-norm off-diagonals by eps/log(maxN)
    """
    M = len(ideals)
    norms = np.array([t[1] for t in ideals], dtype=float)
    Q = np.zeros((M, M), dtype=float)

    log_max = float(np.log(max(norms)))
    same_norm_value = eps_same_norm / log_max if (eps_same_norm and log_max > 0) else 0.0

    for i in range(M):
        for j in range(M):
            if i == j:
                Q[i, j] = diag_scale * lambda_K_of_ideal(ideals[i][0], primes) / np.sqrt(norms[i])
            else:
                ni, nj = norms[i], norms[j]
                if ni == nj:
                    Q[i, j] = same_norm_value
                else:
                    Q[i, j] = -1.0 / np.log(nj / ni)

    if archimedean_shift:
        Q -= archimedean_shift * np.eye(M)

    if cond_alpha and cond_target_idx < M:
        k = cond_target_idx
        Q[0, 0] += cond_alpha
        Q[0, k] += cond_alpha
        Q[k, 0] += cond_alpha

    Q = 0.5 * (Q + Q.conj().T)
    return Q


# ---------------------------------------------------------------
# 4.  Q analogue (rational primes, rational integers)
# ---------------------------------------------------------------


def build_Q_rational(n_primes: int, M: int, *, diag_scale: float = 1.0):
    rationals = [2, 3, 5, 7, 11, 13][:n_primes]
    # smooth rationals (=n_primes-smooth numbers)
    max_exp = 10
    smooths = set([1])
    for expt in product(range(max_exp + 1), repeat=n_primes):
        v = 1
        for k, p in zip(expt, rationals):
            v *= p**k
        smooths.add(v)
    smooths = sorted(smooths)[:M]
    norms = np.array(smooths, dtype=float)

    def lam(n):
        f = factorint(n)
        if len(f) != 1:
            return 0.0
        p, _k = next(iter(f.items()))
        return float(np.log(p))

    Q = np.zeros((M, M), dtype=float)
    for i in range(M):
        for j in range(M):
            if i == j:
                Q[i, j] = diag_scale * lam(smooths[i]) / np.sqrt(norms[i])
            else:
                ni, nj = norms[i], norms[j]
                if ni == nj:
                    Q[i, j] = 0.0
                else:
                    Q[i, j] = -1.0 / np.log(nj / ni)
    Q = 0.5 * (Q + Q.conj().T)
    return Q, smooths


# ---------------------------------------------------------------
# 5.  Compare eigenvalues to target gamma values
# ---------------------------------------------------------------

GAMMA_K_TARGETS = [6.0209, 10.2437, 12.9880, 14.1347, 16.3429, 18.8059, 21.0220, 21.5531]
GAMMA_Q_TARGETS = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862]


def sorted_by_abs(eigs):
    return sorted(eigs, key=lambda x: abs(x))


def closest_match(val, targets):
    return min((abs(val - t), t) for t in targets)


def report_match(eigs, targets, *, k=10):
    """For the k smallest-by-abs eigenvalues, find nearest target."""
    best = sorted_by_abs(eigs)[:k]
    out = []
    for e in best:
        delta, t = closest_match(abs(e), targets)
        out.append((e, t, delta))
    return out


def tabulate(lines):
    return "\n".join(lines)


# ---------------------------------------------------------------
# 6.  Drive the experiments
# ---------------------------------------------------------------


def run_experiment(title, Q, targets, *, show_k=12):
    eigs = np.linalg.eigvalsh(Q)
    eigs_sorted = sorted_by_abs(eigs)
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)
    print(f"  matrix size: {Q.shape[0]}x{Q.shape[0]}")
    print("  eigenvalues sorted by |lambda|:")
    for i, e in enumerate(eigs_sorted[:show_k], 1):
        print(f"    {i:>3}  {e:>12.5f}")
    print("  nearest target gamma:")
    matches = report_match(eigs, targets, k=show_k)
    for e, t, d in matches:
        tag = "HIT" if d < 0.5 else "    "
        print(f"    {tag}  lambda = {e:>12.5f}   target {t:>8.4f}   delta {d:>8.4f}")
    print()
    return eigs


def main():
    print("First exploratory D_N^K over K = Q(i)")
    print()

    primes_all = gaussian_primes_by_norm(200)
    print("Gaussian primes (first 8 by norm):")
    for i, (a, b, N) in enumerate(primes_all[:8], 1):
        sign = "+" if b >= 0 else "-"
        print(f"  p_{i} = ({a}{sign}{abs(b)}i)  norm {N}")
    print()

    # -----------------------------------------------------------
    # Baseline experiments: N = 3, 4, 5 Gaussian primes; M = 20, 30
    # -----------------------------------------------------------

    experiments = []

    for n_primes in [3, 4, 5]:
        primes_N = primes_all[:n_primes]
        for M in [20, 30]:
            ideals = smooth_ideals(primes_N, M)
            Q = build_Q(ideals, primes_N)
            title = f"K baseline  N_primes={n_primes}  M={M}"
            experiments.append((title, Q, GAMMA_K_TARGETS))

    # -----------------------------------------------------------
    # Variations at (N=5, M=30)
    # -----------------------------------------------------------

    n_primes = 5
    M = 30
    primes_N = primes_all[:n_primes]
    ideals = smooth_ideals(primes_N, M)

    Q_halfdiag = build_Q(ideals, primes_N, diag_scale=0.5)
    experiments.append(("K variation  diag_scale=0.5", Q_halfdiag, GAMMA_K_TARGETS))

    Q_negdiag = build_Q(ideals, primes_N, diag_scale=-1.0)
    experiments.append(("K variation  diag_scale=-1", Q_negdiag, GAMMA_K_TARGETS))

    Q_arch = build_Q(ideals, primes_N, archimedean_shift=5.5)
    experiments.append(("K variation  archimedean_shift=5.5", Q_arch, GAMMA_K_TARGETS))

    Q_cond = build_Q(ideals, primes_N, cond_alpha=1.0, cond_target_idx=1)
    experiments.append(("K variation  rank-2 condensation alpha=1", Q_cond, GAMMA_K_TARGETS))

    Q_eps = build_Q(ideals, primes_N, eps_same_norm=1.0)
    experiments.append(("K variation  same-norm eps=1/log(max)", Q_eps, GAMMA_K_TARGETS))

    # Prime-power-only subset
    pp_ideals = [it for it in ideals if lambda_K_of_ideal(it[0], primes_N) > 0]
    if len(pp_ideals) >= 5:
        Q_pp = build_Q(pp_ideals, primes_N)
        experiments.append(
            (f"K variation  prime-powers only (size={len(pp_ideals)})", Q_pp, GAMMA_K_TARGETS)
        )

    # Larger M at N=5
    ideals_big = smooth_ideals(primes_N, 50)
    Q_big = build_Q(ideals_big, primes_N)
    experiments.append(("K variation  N=5 M=50", Q_big, GAMMA_K_TARGETS))

    # Combined: halved diagonal + archimedean shift + condensation
    Q_combo = build_Q(
        ideals,
        primes_N,
        diag_scale=0.5,
        archimedean_shift=5.5,
        cond_alpha=1.0,
        cond_target_idx=1,
    )
    experiments.append(("K variation  combo (half+arch+cond)", Q_combo, GAMMA_K_TARGETS))

    # -----------------------------------------------------------
    # Rational Q sanity check
    # -----------------------------------------------------------

    Q_rat20, s20 = build_Q_rational(4, 20)
    experiments.append(("Q baseline  n_primes=4 M=20  (sanity)", Q_rat20, GAMMA_Q_TARGETS))

    Q_rat50, s50 = build_Q_rational(4, 50)
    experiments.append(("Q baseline  n_primes=4 M=50  (sanity)", Q_rat50, GAMMA_Q_TARGETS))

    Q_rat50_arch, _ = build_Q_rational(4, 50)
    Q_rat50_arch -= 5.5 * np.eye(Q_rat50_arch.shape[0])
    experiments.append(
        ("Q variation  n_primes=4 M=50 arch=5.5  (sanity)", Q_rat50_arch, GAMMA_Q_TARGETS)
    )

    # -----------------------------------------------------------
    # Run them all
    # -----------------------------------------------------------

    for title, Q, targets in experiments:
        run_experiment(title, Q, targets, show_k=12)

    # -----------------------------------------------------------
    # Concise best-match table across all experiments
    # -----------------------------------------------------------

    print()
    print("=" * 70)
    print("Concise best-match summary (best 3 |delta| per experiment)")
    print("=" * 70)
    for title, Q, targets in experiments:
        eigs = np.linalg.eigvalsh(Q)
        matches = report_match(eigs, targets, k=Q.shape[0])
        matches.sort(key=lambda m: m[2])
        top3 = matches[:3]
        line = " | ".join(
            f"lam={e:>8.3f}~>{t:>6.2f} (d={d:.3f})" for e, t, d in top3
        )
        print(f"  {title:<50}")
        print(f"     {line}")


if __name__ == "__main__":
    main()
