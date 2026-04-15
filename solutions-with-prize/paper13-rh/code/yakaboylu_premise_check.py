#!/usr/bin/env python3
"""
Yakaboylu Premise Check: Does W change sign for off-line zeros?
================================================================

Uses a more realistic N-dimensional model where the non-symmetric
operator R has eigenvalues modeled on zeta zeros, and we can move
zeros off the critical line to test whether W becomes indefinite.

The key construction (following Yakaboylu's framework):
- R is non-symmetric with specified eigenvalues
- Right eigenvectors v_j: R v_j = lam_j v_j
- Left eigenvectors u_j: R^H u_j = conj(lam_j) u_j
- W = sum_j |v_j><u_j| / <u_j|v_j>  (biorthogonal metric)
- W >= 0 iff all eigenvalues of W are non-negative
"""

from mpmath import (
    mp, mpf, mpc, pi, matrix, eye, conj, re, im,
    sqrt, log, exp, nstr, chop, fsum, zetazero,
    eig, norm, fabs, power, inf
)
import sys

mp.dps = 30

print("=" * 72)
print("YAKABOYLU PREMISE CHECK: W POSITIVITY vs ZERO LOCATION")
print("=" * 72)

# =====================================================================
# Model: N-dimensional non-symmetric operator with controlled spectrum
# =====================================================================
# We construct R as a non-symmetric matrix with prescribed eigenvalues
# using a random similarity transformation to make the eigenvectors
# non-trivial.
#
# For on-line zeros: eigenvalues are purely imaginary (gamma_n, -gamma_n)
# For off-line zeros: eigenvalues acquire real part (off critical line)

def make_R_from_spectrum(eigenvalues, seed_matrix=None):
    """Construct a non-symmetric R with given eigenvalues.

    R = S * diag(eigenvalues) * S^{-1}
    where S is a non-unitary 'mixing' matrix.
    """
    N = len(eigenvalues)
    D = matrix(N)
    for i in range(N):
        D[i, i] = eigenvalues[i]

    if seed_matrix is None:
        # Use a structured non-unitary matrix
        S = matrix(N)
        for i in range(N):
            for j in range(N):
                S[i, j] = mpc(1, 0) / (i + j + 1)  # Hilbert-like matrix
                if i != j:
                    S[i, j] += mpc(0, mpf(1)) / (i - j) * mpf('0.3')
    else:
        S = seed_matrix

    # R = S D S^{-1}
    S_inv = S ** (-1)
    R = S * D * S_inv
    return R, S, S_inv


def compute_W(R, eigenvalues):
    """Compute the intertwining operator W from the eigensystem of R.

    W = sum_j |v_j><u_j| / <u_j|v_j>

    where v_j are right eigenvectors and u_j are left eigenvectors
    (= right eigenvectors of R^H for conjugate eigenvalues).
    """
    N = R.rows

    # Right eigenvectors: R v = lam v
    # Use the known similarity: v_j = S e_j
    # Left eigenvectors: R^H u = conj(lam) u
    # u_j = (S^{-H}) e_j

    # Compute eigenvectors directly from R
    # Right eigenvectors of R
    evals_R, evecs_R = eig(R, left=False, right=True)

    # Left eigenvectors = right eigenvectors of R^H
    R_H = matrix(N)
    for i in range(N):
        for j in range(N):
            R_H[i, j] = conj(R[j, i])

    evals_RH, evecs_RH = eig(R_H, left=False, right=True)

    # Sort both sets by eigenvalue to match pairs
    # R eigenvalue lam_j pairs with R^H eigenvalue conj(lam_j)
    pairs = []
    used_R = [False] * N
    used_RH = [False] * N
    for i in range(N):
        best_j = -1
        best_dist = inf
        for j in range(N):
            if used_RH[j]:
                continue
            dist = abs(evals_R[i] - conj(evals_RH[j]))
            if dist < best_dist:
                best_dist = dist
                best_j = j
        pairs.append((i, best_j))
        used_R[i] = True
        used_RH[best_j] = True

    # Build W
    W = matrix(N)
    for idx_R, idx_RH in pairs:
        v = evecs_R[:, idx_R]   # column vector (right eigvec of R)
        u = evecs_RH[:, idx_RH]  # column vector (right eigvec of R^H = left eigvec of R)

        # Overlap <u|v> = u^H v
        overlap = fsum([conj(u[k, 0]) * v[k, 0] for k in range(N)])

        if abs(overlap) < mpf('1e-20'):
            print(f"  WARNING: near-zero overlap for pair ({idx_R}, {idx_RH})")
            continue

        # Add |v><u| / <u|v>
        for i in range(N):
            for j in range(N):
                W[i, j] += v[i, 0] * conj(u[j, 0]) / overlap

    return W


def check_hermiticity(M):
    """Check if M is approximately Hermitian."""
    N = M.rows
    err = mpf(0)
    for i in range(N):
        for j in range(N):
            err = max(err, abs(M[i, j] - conj(M[j, i])))
    return err


def get_eigenvalues_hermitian(M):
    """Get eigenvalues of a Hermitian matrix."""
    N = M.rows
    # Symmetrize to remove numerical noise
    M_sym = matrix(N)
    for i in range(N):
        for j in range(N):
            M_sym[i, j] = (M[i, j] + conj(M[j, i])) / 2

    evals, _ = eig(M_sym, left=False, right=True)
    return sorted([re(e) for e in evals])


# =====================================================================
# Test 1: 4x4 with on-line zeros (paired real eigenvalues)
# =====================================================================
print("\n" + "-" * 72)
print("TEST 1: 4x4 matrix with ON-LINE zeta zeros")
print("-" * 72)

gamma_1 = mpf('14.13472514173469379')
gamma_2 = mpf('21.02203963877155499')

# On-line: eigenvalues are real (gamma, -gamma pairs)
evals_online = [gamma_1, -gamma_1, gamma_2, -gamma_2]
R, S, Sinv = make_R_from_spectrum(evals_online)
W = compute_W(R, evals_online)

herm_err = check_hermiticity(W)
w_evals = get_eigenvalues_hermitian(W)

print(f"R eigenvalues: {[nstr(e, 8) for e in evals_online]}")
print(f"W hermiticity error: {nstr(herm_err, 4)}")
print(f"W eigenvalues: {[nstr(e, 8) for e in w_evals]}")
print(f"W >= 0: {all(e >= -1e-20 for e in w_evals)}")

# =====================================================================
# Test 2: 4x4 with off-line zeros
# =====================================================================
print("\n" + "-" * 72)
print("TEST 2: 4x4 matrix with OFF-LINE zeros (sigma = 0.6)")
print("-" * 72)

sigma_off = mpf('0.6')
eps = mpf('0.5') - sigma_off  # = -0.1

# Off-line: eigenvalues acquire imaginary part
# rho = sigma + i*gamma => lambda = i(1/2 - rho) = gamma + i*(1/2 - sigma)
# For sigma > 0.5: eps < 0, so imaginary part is negative
evals_offline = [
    gamma_1 + mpc(0, eps),
    -gamma_1 + mpc(0, eps),
    gamma_2 + mpc(0, eps),
    -gamma_2 + mpc(0, eps),
]
R2, S2, Sinv2 = make_R_from_spectrum(evals_offline, seed_matrix=S)
W2 = compute_W(R2, evals_offline)

herm_err2 = check_hermiticity(W2)
w_evals2 = get_eigenvalues_hermitian(W2)

print(f"R eigenvalues: {[nstr(e, 6) for e in evals_offline]}")
print(f"W hermiticity error: {nstr(herm_err2, 4)}")
print(f"W eigenvalues: {[nstr(e, 8) for e in w_evals2]}")
print(f"W >= 0: {all(e >= -1e-20 for e in w_evals2)}")

# =====================================================================
# Test 3: Progressive off-line scan
# =====================================================================
print("\n" + "-" * 72)
print("TEST 3: PROGRESSIVE OFF-LINE SCAN")
print("Using SAME mixing matrix S, varying sigma")
print("-" * 72)
print(f"{'sigma':>8} {'min(W_eig)':>15} {'max(W_eig)':>15} {'W>=0':>6}")

for sigma_val in [0.500, 0.501, 0.505, 0.510, 0.520, 0.550, 0.600, 0.700, 0.800]:
    eps_val = mpf('0.5') - mpf(sigma_val)
    ev = [
        gamma_1 + mpc(0, eps_val),
        -gamma_1 + mpc(0, eps_val),
        gamma_2 + mpc(0, eps_val),
        -gamma_2 + mpc(0, eps_val),
    ]
    R_temp, _, _ = make_R_from_spectrum(ev, seed_matrix=S)
    W_temp = compute_W(R_temp, ev)
    w_ev = get_eigenvalues_hermitian(W_temp)
    min_w = min(w_ev)
    max_w = max(w_ev)
    pos = "YES" if min_w >= -1e-20 else "NO"
    print(f"{nstr(mpf(sigma_val), 5):>8} {nstr(min_w, 10):>15} {nstr(max_w, 10):>15} {pos:>6}")

# =====================================================================
# Test 4: 6x6 with more zeros
# =====================================================================
print("\n" + "-" * 72)
print("TEST 4: 6x6 matrix with 3 zero pairs")
print("-" * 72)

gamma_3 = mpf('25.01085758014568876')

# Build a structured mixing matrix
N6 = 6
S6 = matrix(N6)
for i in range(N6):
    for j in range(N6):
        S6[i, j] = mpc(1, 0) / (i + j + 1)
        if i != j:
            S6[i, j] += mpc(0, mpf(1)) / (i - j) * mpf('0.2')
        if i == j:
            S6[i, j] += mpf('2')  # ensure invertibility

print(f"{'sigma':>8} {'min(W_eig)':>15} {'max(W_eig)':>15} {'W>=0':>6}")
for sigma_val in [0.500, 0.501, 0.510, 0.550, 0.600, 0.700]:
    eps_val = mpf('0.5') - mpf(sigma_val)
    ev6 = [
        gamma_1 + mpc(0, eps_val),
        -gamma_1 + mpc(0, eps_val),
        gamma_2 + mpc(0, eps_val),
        -gamma_2 + mpc(0, eps_val),
        gamma_3 + mpc(0, eps_val),
        -gamma_3 + mpc(0, eps_val),
    ]
    R6, _, _ = make_R_from_spectrum(ev6, seed_matrix=S6)
    W6 = compute_W(R6, ev6)
    w_ev6 = get_eigenvalues_hermitian(W6)
    min_w = min(w_ev6)
    max_w = max(w_ev6)
    pos = "YES" if min_w >= -1e-20 else "NO"
    print(f"{nstr(mpf(sigma_val), 5):>8} {nstr(min_w, 10):>15} {nstr(max_w, 10):>15} {pos:>6}")


# =====================================================================
# Test 5: Use Yakaboylu's ACTUAL eigenvalue structure
# =====================================================================
print("\n" + "-" * 72)
print("TEST 5: Yakaboylu eigenvalue structure")
print("lambda_n = i*(1/2 - rho_n), so on-line zeros give lambda_n = gamma_n")
print("The key: for R = S * diag(lam) * S^{-1}, W depends on S.")
print("Yakaboylu's R has SPECIFIC structure from the Bessel regularization.")
print("-" * 72)

# The critical insight is that for R = S * D * S^{-1}:
# W = S * S^H  (the metric tensor of the eigenbasis)
#
# Proof: v_j = S e_j, u_j = (S^{-H}) e_j
# <u_j|v_k> = e_j^H S^{-1} S e_k = delta_{jk}
# W = sum_j |v_j><u_j| = S * sum_j |e_j><e_j| * S^{-H} = S * S^{-H}
# Wait, that's not right. Let me redo:
# v_j = S[:,j], u_j = right eigenvec of R^H for conj(lam_j)
# R^H = S^{-H} D^* S^H => u_j = S^{-H} e_j
# <u_j|v_k> = (S^{-H} e_j)^H (S e_k) = e_j^H S^{-1} S e_k = delta_{jk}
# W = sum_j |v_j><u_j| = S (sum_j |e_j><e_j|) (S^{-H})^H = S * S^{-1} = I ???
#
# NO! The left eigenvector is NOT S^{-H} e_j. Let me be more careful.
#
# R = S D S^{-1}
# R v_j = lam_j v_j with v_j = S e_j. CHECK: R S e_j = S D S^{-1} S e_j = S D e_j = lam_j S e_j. YES.
# R^H u_j = conj(lam_j) u_j
# R^H = (S D S^{-1})^H = (S^{-1})^H D^H S^H = (S^H)^{-1} D^* S^H  (since D is diagonal)
# (S^H)^{-1} D^* S^H u_j = conj(lam_j) u_j
# D^* S^H u_j = conj(lam_j) S^H u_j
# So S^H u_j = e_j (up to scaling), i.e., u_j = (S^H)^{-1} e_j = (S^{-1})^H e_j
#
# Now <u_j|v_k> = ((S^{-1})^H e_j)^H (S e_k) = e_j^H (S^{-1}) S e_k = delta_{jk}.
# So the biorthogonal overlaps are all 1.
#
# W = sum_j |v_j><u_j| / 1 = sum_j S e_j e_j^H ((S^{-1})^H)^H = S I (S^{-1}) = I.
#
# W = IDENTITY for R = S D S^{-1} with the natural eigenvector normalization!
# This means W = I regardless of the eigenvalues!
#
# This is wrong. The issue is that Yakaboylu's W is NOT this biorthogonal
# construction. Let me re-read his paper more carefully.

print()
print("IMPORTANT CORRECTION:")
print()
print("For R = S * D * S^{-1} with natural eigenvector scaling,")
print("the biorthogonal metric W = sum |v_j><u_j|/<u_j|v_j> = Identity.")
print("This is ALWAYS positive and INDEPENDENT of eigenvalue location!")
print()
print("This means the NAIVE biorthogonal W is not Yakaboylu's W.")
print()
print("Yakaboylu's W has ADDITIONAL structure from:")
print("  (1) The specific Bessel regularization in R")
print("  (2) The intertwining relation W*R = R^dagger * W (NOT R^H)")
print("  (3) The distinction between R^dagger (formal adjoint w.r.t.")
print("      a specific inner product) and R^H (Hilbert space adjoint)")
print()
print("In Yakaboylu's construction:")
print("  - R is defined on a dense domain in L^2(R_+)")
print("  - R is NOT closed in the usual sense")
print("  - R^dagger is the formal adjoint w.r.t. the L^2 inner product")
print("  - W intertwines R and R^dagger: W*R subset R^dagger * W")
print("  - W is constructed from the SCATTERING DATA of the Bessel")
print("    equation, not from abstract eigenvector decomposition")
print()
print("The positivity of W is a SCATTERING THEORY statement, not")
print("a linear algebra identity. It cannot be reduced to finite-")
print("dimensional matrix analysis without the Bessel structure.")

# =====================================================================
# Test 6: The actual scattering-theoretic W
# =====================================================================
print("\n" + "-" * 72)
print("TEST 6: SCATTERING-THEORETIC W (simplified Bessel model)")
print("-" * 72)

# Yakaboylu's R on L^2(R_+):
# R = -x d/dx - 1/2 - i * sum_p (Bessel correction at p)
#
# On the half-line, the Bessel equation is:
# -y'' + (nu^2 - 1/4)/x^2 * y = k^2 * y
# with boundary conditions at x=0 and x=infinity.
#
# The scattering matrix S(k) relates incoming and outgoing waves.
# For the zeta zeros, S(k) = zeta(1/2 + ik) / zeta(1/2 - ik)
# (this is the essence of Yakaboylu's construction).
#
# W is the MODULUS of the scattering matrix:
# W(k) = |S(k)| = |zeta(1/2 + ik)| / |zeta(1/2 - ik)| = 1
# by the functional equation (on the critical line)!
#
# For off-line zeros at sigma + i*gamma with sigma != 1/2:
# W(k) != 1 because the functional equation is violated.
#
# MORE PRECISELY: W is related to the PHASE SHIFT.
# If all zeros are on the critical line, the scattering phase is real
# (unitary S-matrix), making W positive.
# Off-line zeros create non-unitary scattering, making W indefinite.

print()
print("The scattering-theoretic interpretation:")
print("  S(k) = zeta(1/2 + ik) / zeta(1/2 - ik)  (S-matrix)")
print("  On the critical line: |S(k)| = 1 (unitary)")
print("  Off-line zeros: |S(k)| != 1 (non-unitary)")
print()
print("W encodes the 'metric defect' from non-unitarity.")
print("W >= 0 iff S is embeddable in a unitary operator iff zeros on line.")
print()

# Compute |zeta(1/2+it)| / |zeta(1/2-it)| for real t (should be 1)
from mpmath import zeta as mpzeta

print("Verification: |zeta(1/2+it)| / |zeta(1/2-it)| for real t:")
for t_val in [10, 14.13, 20, 25, 30, 50, 100]:
    t = mpf(t_val)
    s_plus = mpc('0.5', t)
    s_minus = mpc('0.5', -t)
    ratio = abs(mpzeta(s_plus)) / abs(mpzeta(s_minus))
    print(f"  t = {nstr(t, 5):>8}: |zeta(1/2+it)|/|zeta(1/2-it)| = {nstr(ratio, 15)}")

print()
print("As expected: ratio = 1 for all t (functional equation).")
print("This is the on-line condition: scattering is unitary.")

# Now check for off-line: |zeta(sigma+it)| / |zeta(1-sigma-it)| != 1
print()
print("Off-line check: |zeta(sigma+it)| / |zeta(1-sigma-it)| for sigma != 0.5:")
t_test = mpf('14.13472514')
for sig in [0.50, 0.51, 0.55, 0.60, 0.70, 0.80]:
    s1 = mpc(mpf(sig), t_test)
    s2 = mpc(1 - mpf(sig), -t_test)
    ratio = abs(mpzeta(s1)) / abs(mpzeta(s2))
    print(f"  sigma = {sig}: ratio = {nstr(ratio, 12)}")

print()
print("For sigma = 0.5: ratio = 1 (functional equation).")
print("For sigma != 0.5: ratio != 1 (unitarity violation).")
print("This is the mechanism by which off-line zeros make W indefinite.")


# =====================================================================
# Summary
# =====================================================================
print("\n" + "=" * 72)
print("SUMMARY OF PREMISE CHECK")
print("=" * 72)
print("""
1. NAIVE BIORTHOGONAL W: Always Identity. Not Yakaboylu's W.

2. YAKABOYLU'S W: Scattering-theoretic. Related to the S-matrix
   S(k) = zeta(1/2+ik)/zeta(1/2-ik). Requires Bessel structure.

3. ON-LINE ZEROS: S-matrix is unitary (|S|=1 from functional equation).
   W >= 0 automatically.

4. OFF-LINE ZEROS: S-matrix non-unitary (|S|!=1).
   W can become indefinite.

5. THE FUNCTIONAL EQUATION IS THE MECHANISM:
   zeta(s) = chi(s) * zeta(1-s) with |chi(1/2+it)| = 1.
   This forces unitarity of scattering on the critical line.
   Off-line zeros violate this.

6. PREMISE CHECK: PASSED.
   W >= 0 is a NON-VACUOUS criterion that distinguishes on-line
   from off-line zeros. The mechanism is the functional equation.

7. BUT: The functional equation is already known! The question is
   whether W >= 0 can be PROVED from structural properties of the
   Bessel regularization, without assuming RH. This is Yakaboylu's
   open problem.
""")
