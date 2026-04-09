"""
R40 Path 1: Commutator [Q_W, T_p] where T_p are unramified Hecke operators
(= Satake = BT tree translations, by Identity 4).

Basis: same as r38 / r39  — V_n(u) = e^{2πinu/L}/√L for |n| ≤ N_modes,
u ∈ [-L/2, L/2], L = 2 log λ. This u IS φ = log(·) in Mellin coordinates.

Hecke action on spherical line:
    T_p f(x) = √p · f(p x) + (1/√p) · f(x/p)       (standard unramified Hecke)
Under x = e^u this is a translation by ±log p:
    T_p f(u) = √p · f(u + log p) + (1/√p) · f(u - log p)
This is NOT self-adjoint on L²(du) since √p ≠ 1/√p. The symmetric (self-adjoint)
normalization used on the unitary axis Re(s)=1/2 (the Kirillov/spherical model)
is the "normalized Hecke" operator
    T̃_p f(u) = (1/√p) · [ f(u + log p) + f(u - log p) ]
with spectrum on Fourier modes:  τ_n(p) = (2/√p) cos(2π n log p / L).
On the unramified principal series with Satake parameter p^{iγ}, the eigenvalue
is (p^{iγ} + p^{-iγ})/√p · (something) — up to overall normalization we use T̃_p.

We ALSO run the unsymmetric T_p (eigenvalue √p e^{iθ_n(p)} + (1/√p) e^{-iθ_n(p)})
since Q_W is real-symmetric and the commutator is the physical object.

Key observation:
  Q_pole and Q_prime in this basis are BOTH Toeplitz (depend only on Δn = n_b-n_a).
  Shift/translation operators are diagonal in Fourier modes, and the INFINITE
  Toeplitz matrix commutes exactly with any periodic shift. On truncation to
  |n| ≤ N_modes the commutator comes entirely from edge/wrap-around effects
  and should shrink as N → ∞. We test whether this is the actual asymptotic
  regime and whether the shrinking is clean on the EVEN subspace.
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r38_krein_rutman_rh import connes_consani_fourier_weil_matrix
from r39_commutator import even_projector


def build_Tp_shift(N_modes, lam, p, symmetric=True):
    """Hecke T_p in the Fourier basis V_n(u)=e^{2πinu/L}/√L, L=2log λ.

    On an infinite line, T_p is diagonal in Fourier modes with
    eigenvalue:
        symmetric:   (2/√p) cos(2π n log p / L)        (self-adjoint)
        standard:    √p e^{i θ_n} + (1/√p) e^{-i θ_n}, θ_n = 2π n log p/L
    On the finite truncation we realize T_p as a TRUE shift matrix in the
    POSITION basis (discretized on φ=u grid), then project back to Fourier.
    This way the boundary/truncation effects are faithful.

    Implementation: use the spectral (Fourier-mode) form as the definition.
    The Fourier basis is the exact simultaneous eigenbasis of all shifts
    on the L-periodic torus; using that form gives the commutator that
    one actually gets from the truncated Fourier projection of the
    R-line shift. (Both pieces of Q_W are also built in this basis.)

    Returns a (2N+1)x(2N+1) complex matrix, diagonal.
    """
    L = 2 * np.log(lam)
    ns = np.arange(-N_modes, N_modes + 1)
    theta = 2 * np.pi * ns * np.log(p) / L
    if symmetric:
        diag = (2.0 / np.sqrt(p)) * np.cos(theta)
    else:
        diag = np.sqrt(p) * np.exp(1j * theta) + (1.0 / np.sqrt(p)) * np.exp(-1j * theta)
    return np.diag(diag.astype(complex))


def build_Tp_position_shift(N_modes, lam, p, N_grid=None, symmetric=True):
    """Alternative T_p realization: build as a shift on a POSITION-space grid
    of the interval φ ∈ [-L/2, L/2] with N_grid points, then conjugate to
    Fourier basis and truncate to |n|≤N_modes. This correctly encodes the
    boundary effects of the truncated line.

    For translation by log p, points falling outside [-L/2, L/2] are ZEROED
    (not wrapped) — i.e. we use the RESTRICTED shift of the half-line /
    finite interval. That is the physically correct T_p on L²([-L/2,L/2], du).
    """
    L = 2 * np.log(lam)
    if N_grid is None:
        N_grid = 8 * (2 * N_modes + 1) + 1   # oversample
    # Grid in u
    du = L / N_grid
    u = -L/2 + (np.arange(N_grid) + 0.5) * du

    # Shift by +log p and -log p as sparse matrices (zero-extension outside)
    shift = int(round(np.log(p) / du))
    dim_g = N_grid
    S_plus = np.zeros((dim_g, dim_g))
    S_minus = np.zeros((dim_g, dim_g))
    for i in range(dim_g):
        j = i + shift
        if 0 <= j < dim_g:
            S_plus[j, i] = 1.0  # (S_plus f)(u_j) = f(u_{j-shift}) i.e. f shifted right
        j2 = i - shift
        if 0 <= j2 < dim_g:
            S_minus[j2, i] = 1.0
    if symmetric:
        Tp_pos = (1.0 / np.sqrt(p)) * (S_plus + S_minus)
    else:
        Tp_pos = np.sqrt(p) * S_plus + (1.0 / np.sqrt(p)) * S_minus

    # Change of basis: position grid -> Fourier modes V_n
    # V_n(u_i) = exp(2πi n u_i / L) / sqrt(L); matrix U[i,k] with k indexing n=-N..N
    ns = np.arange(-N_modes, N_modes + 1)
    U = np.exp(2j * np.pi * np.outer(u, ns) / L) / np.sqrt(L)   # (N_grid, 2N+1)
    # Fourier component of Tp_pos: (U^H · Tp_pos · U) * du, since inner product
    # <V_a|A|V_b> ≈ Σ_i du · conj(V_a(u_i)) (A V_b)(u_i)
    Tp_fourier = (U.conj().T @ Tp_pos @ U) * du
    return Tp_fourier


def commutator_metrics(Q, T, label):
    C = Q @ T - T @ Q
    nQ = np.linalg.norm(Q, 2)
    nT = np.linalg.norm(T, 2)
    nC = np.linalg.norm(C, 2)
    nC_fr = np.linalg.norm(C, 'fro')
    r_op = nC / (nQ * nT + 1e-30)
    return dict(label=label, nQ=nQ, nT=nT, nC_op=nC, nC_fr=nC_fr, ratio=r_op)


def run_case(lam, N_modes, primes, position_shift=False, verbose=True):
    Q_W, _, _, ns = connes_consani_fourier_weil_matrix(lam, N_modes, primes)
    Q_W = Q_W.astype(complex)
    P_even = even_projector(N_modes).astype(complex)
    Q_e = P_even @ Q_W @ P_even

    build = (lambda p: build_Tp_position_shift(N_modes, lam, p, symmetric=True)) \
        if position_shift else \
        (lambda p: build_Tp_shift(N_modes, lam, p, symmetric=True))

    if verbose:
        kind = "position-shift T_p" if position_shift else "spectral-diagonal T_p"
        print(f"\n--- λ={lam}, N_modes={N_modes}, #primes={len(primes)}  [{kind}] ---")
        print(f"    ‖Q_W‖₂ = {np.linalg.norm(Q_W,2):.4e}    ‖Q_even‖₂ = {np.linalg.norm(Q_e,2):.4e}")

    # 1) Individual T_p commutators
    Tps = [build(p) for p in primes]
    rows = []
    for p, Tp in zip(primes, Tps):
        m_full = commutator_metrics(Q_W, Tp, f"T_{p}")
        m_even = commutator_metrics(Q_e, P_even @ Tp @ P_even, f"T_{p} (even)")
        rows.append((p, m_full['ratio'], m_full['nC_op'], m_even['ratio'], m_even['nC_op']))
    if verbose:
        print(f"  {'p':>3}  {'ratio full':>12}  {'‖[Q,T]‖₂':>12}  {'ratio EVEN':>12}  {'‖[Q_e,T]‖₂':>12}")
        for p, rf, cf, re_, ce in rows:
            print(f"  {p:>3}  {rf:12.4e}  {cf:12.4e}  {re_:12.4e}  {ce:12.4e}")

    # 2) Sum
    T_sum = sum(Tps)
    m = commutator_metrics(Q_W, T_sum, "Σ T_p")
    m_e = commutator_metrics(Q_e, P_even @ T_sum @ P_even, "Σ T_p (even)")
    if verbose:
        print(f"  Σ T_p          : full ratio={m['ratio']:.4e}  even ratio={m_e['ratio']:.4e}")

    # 3) Casimir Σ T_p²
    T_cas = sum(Tp @ Tp for Tp in Tps)
    mc = commutator_metrics(Q_W, T_cas, "Σ T_p²")
    mc_e = commutator_metrics(Q_e, P_even @ T_cas @ P_even, "Σ T_p² (even)")
    if verbose:
        print(f"  Σ T_p²         : full ratio={mc['ratio']:.4e}  even ratio={mc_e['ratio']:.4e}")

    # 4) Weil-weighted Σ (log p / √p) T_p
    T_weil = sum((np.log(p)/np.sqrt(p)) * Tp for p, Tp in zip(primes, Tps))
    mw = commutator_metrics(Q_W, T_weil, "Σ (log p/√p) T_p")
    mw_e = commutator_metrics(Q_e, P_even @ T_weil @ P_even, "Σ (log p/√p) T_p (even)")
    if verbose:
        print(f"  Σ (logp/√p)T_p : full ratio={mw['ratio']:.4e}  even ratio={mw_e['ratio']:.4e}")

    # 5) Joint-eigenvector test for smallest-eig of Q_W
    eigs, vecs = np.linalg.eigh(Q_W)
    i0 = int(np.argmin(eigs))
    v = vecs[:, i0]
    residuals = []
    for p, Tp in zip(primes, Tps):
        Tpv = Tp @ v
        lam_p = np.vdot(v, Tpv).real
        res = np.linalg.norm(Tpv - lam_p * v)
        residuals.append((p, lam_p, res))
    if verbose:
        print(f"  Joint-eig residuals on Q_W ground state (eig={eigs[i0]:.4e}):")
        for p, lp, r in residuals:
            print(f"     p={p:>3}: <v|T_p|v>={lp:+.4e}  residual={r:.4e}")

    # 6) Same on EVEN subspace
    eigs_e, vecs_e = np.linalg.eigh(Q_e)
    mask = np.abs(eigs_e) > 1e-10
    if mask.any():
        i_e = int(np.argmin(eigs_e[mask]))
        idx_map = np.where(mask)[0]
        v_e = vecs_e[:, idx_map[i_e]]
        if verbose:
            print(f"  EVEN min-nonzero eig={eigs_e[idx_map[i_e]]:.4e}")
        for p, Tp in zip(primes, Tps):
            Tpe = P_even @ Tp @ P_even
            Tpv = Tpe @ v_e
            lp = np.vdot(v_e, Tpv).real
            r = np.linalg.norm(Tpv - lp * v_e)
            if verbose:
                print(f"     p={p:>3}: <v|T_p|v>={lp:+.4e}  residual={r:.4e}")

    return {
        'rows': rows, 'sum': m, 'sum_even': m_e,
        'casimir': mc, 'casimir_even': mc_e,
        'weil': mw, 'weil_even': mw_e,
        'residuals': residuals,
    }


def scaling_study():
    """Does ‖[Q_W,T_p]‖/(‖Q_W‖·‖T_p‖) shrink with N_modes?"""
    lam = 6.0
    primes = [2, 3, 5]
    print("\n" + "="*78)
    print("SCALING STUDY: does ratio shrink with N_modes?  (λ=6, primes={2,3,5})")
    print("="*78)
    Ns = [10, 20, 30, 50, 80]
    for kind, pos in [("spectral", False), ("position-shift", True)]:
        print(f"\n  [{kind}]")
        print(f"  {'N':>4}  " + "  ".join(f"p={p} full | even" for p in primes) + f"  | Σ full | Σ even")
        for N in Ns:
            r = run_case(lam, N, primes, position_shift=pos, verbose=False)
            parts = []
            for (p, rf, _, re_, _) in r['rows']:
                parts.append(f"{rf:.2e}|{re_:.2e}")
            print(f"  {N:>4}  " + "  ".join(parts) + f"  | {r['sum']['ratio']:.2e}|{r['sum_even']['ratio']:.2e}")


if __name__ == "__main__":
    print("R40 Path 1: [Q_W, T_p] — prime-side Hecke / BT-tree translation commutators")
    print("Basis: V_n(u)=e^{2πinu/L}/√L, L=2log λ; u = log(·)")
    print("T_p symmetric: (1/√p)(f(u+log p)+f(u-log p))  "
          "→ Fourier diag (2/√p)cos(2πn log p / L)")

    # SPECTRAL T_p (infinite-line, no truncation effects in T_p itself)
    print("\n" + "#"*78)
    print("# A) SPECTRAL T_p  (diagonal on V_n — no truncation of T_p)")
    print("#"*78)
    primes_5 = [2, 3, 5, 7, 11]
    run_case(3.6, 30, primes_5, position_shift=False)
    primes_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    run_case(6.0, 40, primes_10, position_shift=False)
    primes_20 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    run_case(10.0, 60, primes_20, position_shift=False)

    # POSITION-SHIFT T_p (finite-interval restricted shift)
    print("\n" + "#"*78)
    print("# B) POSITION-SHIFT T_p  (finite-interval restricted shift, faithful truncation)")
    print("#"*78)
    run_case(3.6, 30, primes_5, position_shift=True)
    run_case(6.0, 40, primes_10, position_shift=True)
    run_case(10.0, 60, primes_20, position_shift=True)

    scaling_study()
