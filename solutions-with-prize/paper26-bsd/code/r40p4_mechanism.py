"""
R40 Path 4: Why does even-simple hold for Q_W?
Three sub-tests on the R38 Fourier-basis Weil matrix builder, parametrized
by an arbitrary "log-spectrum" L_set replacing {log 2, log 3, log 5, ...}.

SUB-TEST 1: Diophantine non-resonance vs spectral gap (primes)
SUB-TEST 2: Random matrix controls (uniform / Q-dependent / resonant)
SUB-TEST 3: Sign-change (nodal) invariant of the lowest eigenfunction
"""

import numpy as np
from itertools import product
from math import log

np.set_printoptions(precision=4, suppress=True)

# ---------- Generalized Q_W builder (log-spectrum parametrized) ----------

def build_QW_from_logset(lam, N_modes, log_set, coeffs=None):
    """
    Build Q_W = Q_pole + Q_prime in the Fourier basis V_n = e^{2 pi i n u / L}
    with L = 2 log(lam), n = -N_modes..N_modes.

    Prime term replaced by a generic sum over "log-spectrum" ell in log_set with
    coefficient c(ell). If coeffs is None we use the Euler coefficient log(p)/p^{m/2}
    where ell = m log(p); here we treat each ell as an atomic "first power",
    assigning coeff = 0.5 * ell * exp(-ell/2) which mimics log(p)/sqrt(p) when
    ell=log(p). For the prime comparison we pass the true multi-power list.
    """
    L = 2.0 * log(lam)
    dim = 2 * N_modes + 1
    ns = np.arange(-N_modes, N_modes + 1)

    Q_pole = np.zeros((dim, dim))
    Q_prime = np.zeros((dim, dim))

    # Pole (unchanged)
    for a in range(dim):
        for b in range(dim):
            delta_n = ns[b] - ns[a]
            freq = 2 * np.pi * delta_n / L
            a_c = 0.5
            denom = a_c * a_c + freq * freq
            if denom > 1e-30:
                upper = L / 2
                val = (a_c * np.sinh(a_c * upper) * np.cos(freq * upper)
                       + freq * np.cosh(a_c * upper) * np.sin(freq * upper)) / denom
                val *= 2
            else:
                val = 2 * np.sinh(L / 4)
            Q_pole[a, b] = val / L

    if coeffs is None:
        coeffs = [0.5 * ell * np.exp(-ell / 2) for ell in log_set]

    for ell, c in zip(log_set, coeffs):
        if ell > L:
            continue
        for a in range(dim):
            for b in range(dim):
                delta_n = ns[b] - ns[a]
                phase = 2 * np.pi * delta_n * ell / L
                Q_prime[a, b] -= (2.0 * c / L) * np.cos(phase)

    Q = Q_pole + Q_prime
    Q = 0.5 * (Q + Q.T)
    return Q, ns


def build_QW_primes(lam, N_modes, primes):
    """Physical Q_W with true Euler prime powers (matches r38)."""
    L = 2.0 * log(lam)
    log_set = []
    coeffs = []
    for p in primes:
        lp = log(p)
        for m in range(1, int(L / lp) + 1):
            ell = m * lp
            if ell > L:
                break
            log_set.append(ell)
            coeffs.append(log(p) / p ** (m / 2.0))
    return build_QW_from_logset(lam, N_modes, log_set, coeffs)


# ---------- Even projection & analysis ----------

def even_projection(ns):
    dim = len(ns)
    P = np.zeros((dim, dim))
    for k in range(dim):
        n = ns[k]
        k_neg = int(np.where(ns == -n)[0][0])
        P[k, k] += 0.5
        P[k, k_neg] += 0.5
    return P


def analyze(Q, ns, tol=1e-10):
    P = even_projection(ns)
    Qe = P @ Q @ P
    vals, vecs = np.linalg.eigh(Qe)
    order = np.argsort(vals)
    vals = vals[order]
    vecs = vecs[:, order]
    keep = np.abs(vals) > tol
    v_nz = vals[keep]
    V_nz = vecs[:, keep]
    if len(v_nz) < 2:
        return dict(min=float('nan'), gap=float('nan'), simple=False,
                    nodal=-1, vec=None)
    mn = v_nz[0]
    gap = v_nz[1] - v_nz[0]
    # Eigenvector of lowest nonzero: evaluate in position space via inverse DFT
    vec_fourier = V_nz[:, 0]
    # Position-space sampling on u in [-L/2, L/2]
    N_pts = 401
    L = 1.0  # only the sign pattern matters; use unit interval
    us = np.linspace(-0.5, 0.5, N_pts)
    f = np.zeros(N_pts, dtype=complex)
    for k, n in enumerate(ns):
        f += vec_fourier[k] * np.exp(2j * np.pi * n * us)
    f = f.real
    # Count sign changes (skip tiny)
    eps = 1e-8 * max(abs(f).max(), 1e-12)
    signs = np.sign(np.where(np.abs(f) < eps, 0, f))
    sc = 0
    prev = 0
    for s in signs:
        if s == 0:
            continue
        if prev != 0 and s != prev:
            sc += 1
        prev = s
    return dict(min=float(mn), gap=float(gap), simple=bool(gap > 1e-8),
                nodal=sc, vec=f)


# ---------- Diophantine measure ----------

def diophantine_measure(log_set, K=3):
    """min |sum k_i ell_i| over nonzero integer vectors |k_i| <= K."""
    N = len(log_set)
    best = float('inf')
    for kv in product(range(-K, K + 1), repeat=N):
        if all(x == 0 for x in kv):
            continue
        s = sum(k * ell for k, ell in zip(kv, log_set))
        if abs(s) < best:
            best = abs(s)
    return best


# ---------- Sub-test 1: primes ----------

def subtest1_primes(lam=3.6, N_modes=24):
    print("\n" + "=" * 70)
    print("SUB-TEST 1  Diophantine non-resonance (primes)")
    print("=" * 70)
    primes_full = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    lim = lam * lam
    primes_full = [p for p in primes_full if p <= lim]
    rows = []
    print(f"{'N':>3} {'primes':<22} {'min':>12} {'gap':>12} {'simple':>7} "
          f"{'nodal':>6} {'dioph':>10}")
    for N in range(1, len(primes_full) + 1):
        ps = primes_full[:N]
        Q, ns = build_QW_primes(lam, N_modes, ps)
        A = analyze(Q, ns)
        d = diophantine_measure([log(p) for p in ps], K=3)
        rows.append((N, ps, A, d))
        print(f"{N:>3} {str(ps):<22} {A['min']:>12.4e} {A['gap']:>12.4e} "
              f"{str(A['simple']):>7} {A['nodal']:>6} {d:>10.4e}")
    return rows


# ---------- Sub-test 2: random controls ----------

def gen_uniform(N, lam, rng):
    return sorted(rng.uniform(log(2), 2 * log(lam), size=N).tolist())

def gen_Q_dependent(N, lam, rng):
    base = log(2)
    # integer multiples of log 2, shuffled subset
    mults = rng.choice(np.arange(1, max(N + 2, 6)), size=N, replace=False)
    vals = sorted((m * base for m in mults))
    # clip to fit under L
    return [v for v in vals if v <= 2 * log(lam) - 1e-6]

def gen_resonant(N, lam, rng):
    # start from irrational base, add near-integer combinations (force small dioph)
    base = rng.uniform(0.6, 1.2)
    out = [base]
    for _ in range(N - 1):
        k = rng.integers(-2, 3)
        j = rng.integers(0, len(out))
        cand = out[j] + k * base + rng.uniform(-1e-4, 1e-4)
        if 0.1 < cand < 2 * log(lam):
            out.append(cand)
        else:
            out.append(rng.uniform(0.1, 2 * log(lam)))
    return sorted(out)

def subtest2_random(lam=3.6, N_modes=24, N_primes=4, trials=40, seed=17):
    print("\n" + "=" * 70)
    print("SUB-TEST 2  Random log-spectrum controls")
    print("=" * 70)
    rng = np.random.default_rng(seed)
    ensembles = {
        'uniform': gen_uniform,
        'Q-dependent': gen_Q_dependent,
        'resonant': gen_resonant,
    }
    summary = {}
    print(f"{'ensemble':<14} {'simple%':>8} {'gap_med':>12} {'gap_min':>12} "
          f"{'dioph_med':>12} {'nodal_mode':>11}")
    for name, gen in ensembles.items():
        simples = 0
        gaps = []
        diophs = []
        nodals = []
        for t in range(trials):
            try:
                ls = gen(N_primes, lam, rng)
                if len(ls) < 2:
                    continue
                Q, ns = build_QW_from_logset(lam, N_modes, ls)
                A = analyze(Q, ns)
                if A['simple']:
                    simples += 1
                gaps.append(A['gap'])
                diophs.append(diophantine_measure(ls, K=3))
                nodals.append(A['nodal'])
            except Exception as e:
                continue
        gaps = np.array(gaps)
        diophs = np.array(diophs)
        nodals = np.array(nodals)
        mode = int(np.bincount(nodals[nodals >= 0]).argmax()) if len(nodals) else -1
        summary[name] = dict(simple_rate=simples / max(1, trials),
                             gap_med=float(np.median(gaps)),
                             gap_min=float(np.min(gaps)),
                             dioph_med=float(np.median(diophs)),
                             nodal_mode=mode,
                             nodals=nodals.tolist(),
                             gaps=gaps.tolist(),
                             diophs=diophs.tolist())
        print(f"{name:<14} {100*simples/trials:>7.1f}% {np.median(gaps):>12.4e} "
              f"{np.min(gaps):>12.4e} {np.median(diophs):>12.4e} {mode:>11}")
    return summary


# ---------- Sub-test 3: nodal count vs primes added ----------

def subtest3_nodal(lam=3.6, N_modes=24):
    print("\n" + "=" * 70)
    print("SUB-TEST 3  Nodal / sign-change invariant")
    print("=" * 70)
    primes_full = [2, 3, 5, 7, 11, 13]
    primes_full = [p for p in primes_full if p <= lam * lam]
    print(f"{'N':>3} {'primes':<22} {'nodal_even':>11}")
    rows = []
    for N in range(0, len(primes_full) + 1):
        ps = primes_full[:N]
        Q, ns = build_QW_primes(lam, N_modes, ps)
        A = analyze(Q, ns)
        rows.append((N, ps, A['nodal']))
        print(f"{N:>3} {str(ps):<22} {A['nodal']:>11}")
    return rows


if __name__ == "__main__":
    lam = 3.6
    N_modes = 22
    s1 = subtest1_primes(lam, N_modes)
    s2 = subtest2_random(lam, N_modes, N_primes=4, trials=40)
    s3 = subtest3_nodal(lam, N_modes)

    # Correlation: gap vs dioph among primes
    print("\n--- Correlation gap ~ dioph (primes, sub-test 1) ---")
    gs = np.array([r[2]['gap'] for r in s1 if np.isfinite(r[2]['gap'])])
    ds = np.array([r[3] for r in s1 if np.isfinite(r[3])])
    if len(gs) >= 3:
        c = np.corrcoef(gs, ds)[0, 1]
        print(f"Pearson corr(gap, dioph) = {c:+.4f}")
    print("Done.")
