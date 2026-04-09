"""
R39 Track A: Commutator [Q_W, L] where L is the image of the KK Laplacian
Δ_KK = -d²/dφ² under the exponential map φ → u = e^φ.

Derivation:
  φ = log u  ⇒  d/dφ = u d/du
  Δ_KK = -(d/dφ)² = -(u d/du)(u d/du) = -u d/du - u² d²/du²
  So  L = -u² ∂_u² - u ∂_u   on L²(R₊, du/u).
  Equivalently  L = -(u∂_u)²,  eigenfunctions u^{iτ} ↦ τ².

In the Fourier basis used by r38 (V_n(φ) = e^{2πinφ/L}/√L on φ ∈ [-L/2, L/2]
with L = 2 log λ), L is DIAGONAL with eigenvalues (2π n / L)².  This basis IS
the simultaneous eigenbasis of -d²/dφ², so we can compute [Q_W, L] cleanly.

Reuses connes_consani_fourier_weil_matrix from r38 (imported).
"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r38_krein_rutman_rh import connes_consani_fourier_weil_matrix


def build_L_diag(N_modes, lam):
    """KK Laplacian image L = -(u∂_u)² in the Fourier basis V_n.
    Eigenvalue on V_n is (2π n / L_phi)² with L_phi = 2 log λ."""
    L_phi = 2 * np.log(lam)
    ns = np.arange(-N_modes, N_modes + 1)
    return np.diag((2 * np.pi * ns / L_phi) ** 2), ns


def even_projector(N_modes):
    dim = 2 * N_modes + 1
    ns = np.arange(-N_modes, N_modes + 1)
    P = np.zeros((dim, dim))
    for k in range(dim):
        n = ns[k]
        k_neg = int(np.where(ns == -n)[0][0])
        P[k, k] += 0.5
        P[k, k_neg] += 0.5
    return P


def commutator_report(lam, N_modes, primes, label=""):
    Q_W, Q_pole, Q_prime, _ = connes_consani_fourier_weil_matrix(lam, N_modes, primes)
    L_op, ns = build_L_diag(N_modes, lam)

    C = Q_W @ L_op - L_op @ Q_W
    nQ = np.linalg.norm(Q_W, 2)
    nL = np.linalg.norm(L_op, 2)
    nC_op = np.linalg.norm(C, 2)
    nC_fr = np.linalg.norm(C, 'fro')
    nQ_fr = np.linalg.norm(Q_W, 'fro')
    nL_fr = np.linalg.norm(L_op, 'fro')

    print(f"\n=== {label}  λ={lam}, N_modes={N_modes}, #primes={len(primes)} ===")
    print(f"  ‖Q_W‖₂      = {nQ:.6e}")
    print(f"  ‖L‖₂        = {nL:.6e}")
    print(f"  ‖[Q_W,L]‖₂  = {nC_op:.6e}")
    print(f"  ‖[Q_W,L]‖_F = {nC_fr:.6e}")
    print(f"  ‖Q_W‖·‖L‖   = {nQ*nL:.6e}")
    print(f"  ratio op    = {nC_op/(nQ*nL+1e-30):.6e}")
    print(f"  ratio Frob  = {nC_fr/(nQ_fr*nL_fr+1e-30):.6e}")

    # Joint eigenvector check: does Q_W's smallest-eig vector also (nearly) diagonalize L?
    eigs_Q, vecs_Q = np.linalg.eigh(Q_W)
    idx_min = int(np.argmin(np.abs(eigs_Q - eigs_Q.min())))
    v = vecs_Q[:, idx_min]
    Lv = L_op @ v
    proj = float(np.dot(v, Lv))            # <v|L|v>
    Lv_perp = Lv - proj * v
    residual = float(np.linalg.norm(Lv_perp))
    print(f"  Q_W min-eig vector: <v|L|v> = {proj:.6e}, ‖(L-<v|L|v>)v‖ = {residual:.6e}")

    # EVEN subspace
    P = even_projector(N_modes)
    Q_e = P @ Q_W @ P
    L_e = P @ L_op @ P  # L is already even-symmetric since (n)² = (-n)²
    C_e = Q_e @ L_e - L_e @ Q_e
    print(f"  EVEN subspace: ‖[Q_e,L_e]‖₂ = {np.linalg.norm(C_e,2):.6e}, "
          f"‖[Q_e,L_e]‖_F = {np.linalg.norm(C_e,'fro'):.6e}")

    # Joint diagonalization on even: smallest-nonzero eigvec of Q_e
    eQ, vQ = np.linalg.eigh(Q_e)
    mask = np.abs(eQ) > 1e-10
    if mask.any():
        eQ_nz = eQ[mask]; vQ_nz = vQ[:, mask]
        i0 = int(np.argmin(eQ_nz))
        v0 = vQ_nz[:, i0]
        Lv0 = L_e @ v0
        p0 = float(np.dot(v0, Lv0))
        r0 = float(np.linalg.norm(Lv0 - p0 * v0))
        print(f"  EVEN min-nonzero Q_e eigvec: <v|L|v> = {p0:.6e}, residual = {r0:.6e}")

    return dict(nQ=nQ, nL=nL, nC_op=nC_op, nC_fr=nC_fr,
                ratio_op=nC_op/(nQ*nL+1e-30), ratio_fr=nC_fr/(nQ_fr*nL_fr+1e-30))


if __name__ == "__main__":
    print("R39 Track A: [Q_W, L] commutator analysis")
    print("L = image of -d²/dφ² under φ → u = e^φ  ⇒  L = -u²∂_u² - u∂_u = -(u∂_u)²")
    print("In the Fourier basis V_n(φ)=e^{2πinφ/L_phi}/√L_phi, L = diag((2πn/L_phi)²)")

    lam = 3.6
    primes_5 = [2, 3, 5, 7, 11]   # "5 primes" as in r38
    for N in [20, 30, 50]:
        commutator_report(lam, N, primes_5, label=f"5 primes")

    primes_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    commutator_report(lam=6.0, N_modes=40, primes=primes_10, label="10 primes")

    primes_20 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    commutator_report(lam=10.0, N_modes=60, primes=primes_20, label="20 primes")
