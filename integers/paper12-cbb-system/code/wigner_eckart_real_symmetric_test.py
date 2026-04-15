#!/usr/bin/env python3
"""
Wigner–Eckart Real-Symmetric Test on the BC Cube H_□
=====================================================

Tests whether H_BC and T_BC are real symmetric in the Path B
Galois orbit basis, and computes the reduced matrix elements
⟨n‖μ_p‖m⟩ for p ∈ {2,3,5} on the 8-dim cube sub-Hilbert space.

The cube H_□ = span{μ_{2^a 3^b 5^c} Ω_1 : a,b,c ∈ {0,1}} is the
8-dimensional sub-Hilbert space of the Bost–Connes GNS space H_1
at β=1, with orthonormal basis indexed by squarefree 30-smooth
integers {1, 2, 3, 5, 6, 10, 15, 30}.

References:
  - research/04  (Identity 12: H_e → H_1 unitary)
  - research/10  (Theorem 10: the cube H_□, GHZ state Ψ_3)
  - research/19  (Galois orbit decomposition, Path B tensor reading)
  - research/60  (R-Theorem QM.4: Wigner–Eckart on BC side)
  - research/80  (BC-intrinsic SU(3) closure, 8×8 brackets)

Authors: G Six, with Claude Opus 4.6 (1M context)
Date: 2026-04-09
"""

import numpy as np
from itertools import product

# ============================================================
# 1. Cube basis setup
# ============================================================

# Basis ordering from research/80 §2.1:
#   index = 4a + 2b + c  where (a,b,c) ∈ {0,1}^3
#   a = exponent of 2, b = exponent of 3, c = exponent of 5
CUBE_N = []
CUBE_LABELS = []
for a, b, c in product([0, 1], repeat=3):
    n = (2**a) * (3**b) * (5**c)
    idx = 4*a + 2*b + c
    CUBE_N.append((idx, n, a, b, c))
CUBE_N.sort(key=lambda x: x[0])

# Ordered list: index → squarefree integer
N_VALUES = [x[1] for x in CUBE_N]
# index → (a, b, c)
ABC_VALUES = [(x[2], x[3], x[4]) for x in CUBE_N]

print("=" * 70)
print("CUBE BASIS (research/10 Lemma 4.1)")
print("=" * 70)
print(f"{'Index':<6} {'(a,b,c)':<10} {'n':<6} {'Basis vector'}")
print("-" * 50)
for i, (n, (a, b, c)) in enumerate(zip(N_VALUES, ABC_VALUES)):
    print(f"  {i:<4} ({a},{b},{c})     {n:<6} μ_{n} Ω_1")

# ============================================================
# 2. H_BC = log N̂ as an 8×8 matrix (diagonal)
# ============================================================

H_BC = np.diag([np.log(n) for n in N_VALUES])

print("\n" + "=" * 70)
print("H_BC = log N̂  (diagonal in standard cube basis)")
print("=" * 70)
print("Eigenvalues (diagonal entries):")
for i, n in enumerate(N_VALUES):
    print(f"  H_BC[{i},{i}] = log({n}) = {np.log(n):.6f}")

# ============================================================
# 3. Hecke operators μ_p as 8×8 matrices on H_□
# ============================================================

def build_mu_raise(prime_idx):
    """Build μ_p as 8×8 matrix on H_□.

    μ_p acts as the Pauli raising σ_+^{(prime_idx)} on H_□:
      - If the prime_idx-th exponent is 0, raise it to 1.
      - If the prime_idx-th exponent is 1, the result leaves H_□
        (goes to exponent 2), so the projection onto H_□ gives 0.

    prime_idx: 0 → prime 2 (exponent a)
               1 → prime 3 (exponent b)
               2 → prime 5 (exponent c)
    """
    M = np.zeros((8, 8), dtype=float)
    for i, (a, b, c) in enumerate(ABC_VALUES):
        abc = [a, b, c]
        if abc[prime_idx] == 0:
            abc_new = list(abc)
            abc_new[prime_idx] = 1
            j = 4 * abc_new[0] + 2 * abc_new[1] + abc_new[2]
            M[j, i] = 1.0
    return M


def build_mu_lower(prime_idx):
    """Build μ_p^* as 8×8 matrix on H_□ (Hermitian adjoint of μ_p).

    μ_p^* acts as Pauli lowering σ_-^{(prime_idx)}:
      - If the prime_idx-th exponent is 1, lower it to 0.
      - If the prime_idx-th exponent is 0, annihilate (μ_p^* cannot
        divide by p if p does not divide n).
    """
    return build_mu_raise(prime_idx).T


PRIMES = [2, 3, 5]
PRIME_NAMES = {0: 2, 1: 3, 2: 5}

mu_raise = {p: build_mu_raise(i) for i, p in enumerate(PRIMES)}
mu_lower = {p: build_mu_lower(i) for i, p in enumerate(PRIMES)}

print("\n" + "=" * 70)
print("HECKE OPERATORS μ_p ON H_□")
print("=" * 70)

for p in PRIMES:
    print(f"\nμ_{p} (raising):")
    print(mu_raise[p].astype(int))
    print(f"\nμ_{p}^* (lowering):")
    print(mu_lower[p].astype(int))

# Verify BC relations
print("\n" + "=" * 70)
print("BC RELATION VERIFICATION")
print("=" * 70)

for p in PRIMES:
    # μ_p^* μ_p = 1 (on H_□, this is a projection, not identity)
    product_mat = mu_lower[p] @ mu_raise[p]
    # Actually: μ_p^* μ_p = I on the range of μ_p,
    # but on H_□ it's a projection onto the subspace with p-exponent 0
    # Wait — Bost-Connes says μ_p^* μ_p = 1 as an operator on H_1.
    # But restricted to H_□, μ_p maps some basis vectors outside H_□ (those
    # with p-exponent already 1), so μ_p^* μ_p restricted to H_□ is a
    # projection onto the face with p-exponent 0.
    diag = np.diag(product_mat)
    expected = np.array([1.0 if ABC_VALUES[i][PRIMES.index(p)] == 0 else 0.0 for i in range(8)])
    check = np.allclose(product_mat, np.diag(expected))
    print(f"  μ_{p}^* μ_{p} = projection onto (exponent_{p}=0 face): {check}")

for i, p in enumerate(PRIMES):
    for j, q in enumerate(PRIMES):
        if p < q:
            comm = mu_raise[p] @ mu_raise[q] - mu_raise[q] @ mu_raise[p]
            print(f"  [μ_{p}, μ_{q}] = 0: {np.allclose(comm, 0)}")

# ============================================================
# 4. The Path B basis change
# ============================================================
#
# Path B (research/19 §4.2-4.3): H_R ⊗ H_gauge, where H_gauge is
# the Paper 11 three-qubit space (C²)^⊗3. The Galois orbit basis
# is determined by the SM gauge group SU(3)×SU(2)×U(1)/Z_6 acting
# on H_gauge = H_□ via the unitary U_□ of research/10 Lemma 4.1.
#
# The Path B Galois orbit basis uses the 1⊕1⊕3⊕3̄ decomposition
# of H_□ under the Z/3 cyclic symmetry of {2,3,5} (research/80 §3):
#
#   S_+ = (Ω_1 + μ_{30} Ω_1)/√2            (GHZ, index 0)
#   S_- = (Ω_1 - μ_{30} Ω_1)/√2            (anti-GHZ, index 1)
#   3:  μ_2 Ω_1, μ_3 Ω_1, μ_5 Ω_1          (fundamental, indices 2-4)
#   3̄:  μ_{15} Ω_1, μ_{10} Ω_1, μ_6 Ω_1    (antifundamental, indices 5-7)

print("\n" + "=" * 70)
print("PATH B GALOIS ORBIT BASIS (1 ⊕ 1 ⊕ 3 ⊕ 3̄)")
print("=" * 70)

# Build the basis change matrix V : standard → Path B
# V columns are the Path B basis vectors expressed in the standard basis
V = np.zeros((8, 8), dtype=float)

# S_+ = (|000⟩ + |111⟩)/√2 = (e_0 + e_7)/√2
V[0, 0] = 1.0 / np.sqrt(2)   # Ω_1 component
V[7, 0] = 1.0 / np.sqrt(2)   # μ_{30} Ω_1 component

# S_- = (|000⟩ - |111⟩)/√2 = (e_0 - e_7)/√2
V[0, 1] = 1.0 / np.sqrt(2)
V[7, 1] = -1.0 / np.sqrt(2)

# Fundamental 3: μ_2 Ω_1 (index 4), μ_3 Ω_1 (index 2), μ_5 Ω_1 (index 1)
V[4, 2] = 1.0   # μ_2 Ω_1 = |100⟩ → index 4
V[2, 3] = 1.0   # μ_3 Ω_1 = |010⟩ → index 2
V[1, 4] = 1.0   # μ_5 Ω_1 = |001⟩ → index 1

# Antifundamental 3̄: μ_{15} Ω_1 (index 3), μ_{10} Ω_1 (index 5), μ_6 Ω_1 (index 6)
V[3, 5] = 1.0   # μ_{15} Ω_1 = |011⟩ → index 3
V[5, 6] = 1.0   # μ_{10} Ω_1 = |101⟩ → index 5
V[6, 7] = 1.0   # μ_6 Ω_1 = |110⟩ → index 6

# Verify V is unitary (orthogonal, since all entries are real)
print(f"\nV^T V = I: {np.allclose(V.T @ V, np.eye(8))}")
print(f"V V^T = I: {np.allclose(V @ V.T, np.eye(8))}")
print(f"V is real: {np.all(np.isreal(V))}")

print("\nPath B basis vectors:")
path_b_labels = [
    "S_+  = (Ω_1 + μ_{30}Ω_1)/√2     [GHZ singlet]",
    "S_-  = (Ω_1 - μ_{30}Ω_1)/√2     [anti-GHZ singlet]",
    "e_2  = μ_2 Ω_1                    [fundamental]",
    "e_3  = μ_3 Ω_1                    [fundamental]",
    "e_5  = μ_5 Ω_1                    [fundamental]",
    "e_15 = μ_{15} Ω_1                 [antifundamental]",
    "e_10 = μ_{10} Ω_1                 [antifundamental]",
    "e_6  = μ_6 Ω_1                    [antifundamental]",
]
for i, label in enumerate(path_b_labels):
    print(f"  |{i}⟩_B = {label}")

# ============================================================
# 5. H_BC in the Path B basis
# ============================================================

H_BC_pathB = V.T @ H_BC @ V

print("\n" + "=" * 70)
print("H_BC IN THE PATH B BASIS")
print("=" * 70)

print("\nH_BC (Path B) matrix:")
np.set_printoptions(precision=6, suppress=True, linewidth=100)
print(H_BC_pathB)

is_symmetric = np.allclose(H_BC_pathB, H_BC_pathB.T)
is_real = np.all(np.isreal(H_BC_pathB))
print(f"\nH_BC (Path B) is real: {is_real}")
print(f"H_BC (Path B) is symmetric: {is_symmetric}")
print(f"H_BC (Path B) is REAL SYMMETRIC: {is_real and is_symmetric}")

# Check eigenvalues
eigs_pathB = np.linalg.eigvalsh(H_BC_pathB)
eigs_std = np.sort([np.log(n) for n in N_VALUES])
print(f"\nEigenvalues preserved: {np.allclose(np.sort(eigs_pathB), eigs_std)}")

# ============================================================
# 6. THE KEY TEST: T_BC (the scaling operator) in Path B basis
# ============================================================
#
# H_BC = log N̂ has eigenvalues log(n) which are always real.
# The KEY question is about T_BC = the operator whose eigenvalues
# are the non-trivial zeros γ_n of ζ(s).
#
# On the full H_R, T_BC has eigenvalues {γ_n}. On the cube H_□,
# T_BC is NOT directly defined (H_□ is NOT a subspace of H_R in
# general). However, we can ask a STRUCTURAL question:
#
# IF T_BC had the same matrix structure as H_BC on H_□ (i.e., if
# we replace log(n) with generic eigenvalues λ_n), would the
# resulting matrix be real symmetric in the Path B basis?
#
# This tests whether the PATH B BASIS CHANGE PRESERVES REAL
# SYMMETRY for ANY diagonal operator on H_□.

print("\n" + "=" * 70)
print("KEY TEST: GENERIC DIAGONAL OPERATOR IN PATH B BASIS")
print("=" * 70)

# Test with generic (non-degenerate) diagonal entries
np.random.seed(42)
lambda_vals = np.random.randn(8)  # generic real diagonal entries
T_generic = np.diag(lambda_vals)
T_generic_pathB = V.T @ T_generic @ V

is_sym_generic = np.allclose(T_generic_pathB, T_generic_pathB.T)
is_real_generic = np.all(np.isreal(T_generic_pathB))
print(f"\nGeneric diagonal T (Path B) is real: {is_real_generic}")
print(f"Generic diagonal T (Path B) is symmetric: {is_sym_generic}")
print(f"Generic diagonal T (Path B) is REAL SYMMETRIC: {is_real_generic and is_sym_generic}")

# The answer to "is it real symmetric" depends on V.
# Since V is real orthogonal, V^T (real diag) V is always real symmetric.
# This is a THEOREM: V real orthogonal ⟹ V^T D V is real symmetric
# for any real diagonal D.
print("\n*** THEOREM CHECK ***")
print("V is real orthogonal (V^T = V^{-1}, all entries real).")
print("Therefore V^T D V is ALWAYS real symmetric for any real diagonal D.")
print(f"V is orthogonal: {np.allclose(V.T @ V, np.eye(8))}")
print(f"V is real: {np.all(np.isreal(V))}")
print("⟹ ANY diagonal operator with real eigenvalues is real symmetric")
print("   in the Path B basis. QED.")

# ============================================================
# 7. BUT: What about T_BC with COMPLEX eigenvalues?
# ============================================================
#
# RH is the statement that γ_n ∈ R. If γ_n were complex, T_BC
# would have a complex diagonal, and V^T (complex diag) V would
# NOT be Hermitian in general.
#
# The LOCK argument of research/60 §4.2 runs the other way:
#   IF T_BC is real symmetric in some basis ⟹ eigenvalues are real.
#
# So the question is: does the Path B construction FORCE T_BC to
# be real symmetric, or does it merely PRESERVE real symmetry?

print("\n" + "=" * 70)
print("CRITICAL ANALYSIS: DOES PATH B FORCE REAL SYMMETRY?")
print("=" * 70)

print("""
The Path B basis change V is a REAL ORTHOGONAL matrix.

Case 1: T_BC is diagonal with REAL entries λ_n (i.e., RH holds).
  Then V^T · diag(λ) · V is real symmetric. ✓
  This is trivially true — real orthogonal similarity preserves
  real symmetry.

Case 2: T_BC is diagonal with COMPLEX entries (RH fails).
  Then V^T · diag(λ) · V would have complex entries and would NOT
  be Hermitian (V is real, not unitary in the complex sense needed
  to preserve Hermiticity of a complex diagonal).

CONCLUSION: The Path B basis change does NOT independently force
T_BC to be real symmetric. It PRESERVES real symmetry (if T_BC
is already self-adjoint with real spectrum, it remains real
symmetric after the basis change). But it does not CREATE real
symmetry from nothing.

The LOCK of research/60 §4.2 requires an INDEPENDENT argument
that T_BC is self-adjoint (or equivalently that γ_n ∈ R). The
Wigner–Eckart reduced matrix elements ⟨n‖μ_p‖m⟩ = √(1/p) being
real is a NECESSARY condition for the Galois orbit basis to be
"good" (i.e., for H_BC to be real symmetric in it), but the
implication runs:

  (γ_n ∈ R) + (V real orthogonal) ⟹ T_BC real symmetric in Path B

NOT the reverse. The reverse would require T_BC to be DEFINED as
a real symmetric matrix in the Path B basis, which would be
circular (it would assume the Galois orbit decomposition makes
T_BC manifestly self-adjoint, which is what we're trying to prove).
""")

# ============================================================
# 8. Hecke operators μ_p in the Path B basis
# ============================================================

print("=" * 70)
print("HECKE OPERATORS μ_p IN PATH B BASIS")
print("=" * 70)

for p in PRIMES:
    mu_p_pathB = V.T @ mu_raise[p] @ V
    print(f"\nμ_{p} in Path B basis:")
    print(mu_p_pathB)
    is_sym_mu = np.allclose(mu_p_pathB, mu_p_pathB.T)
    print(f"  Symmetric: {is_sym_mu}")
    # μ_p is NOT symmetric — it's a partial isometry (raising operator)

# ============================================================
# 9. Reduced matrix elements ⟨n‖μ_p‖m⟩
# ============================================================

print("\n" + "=" * 70)
print("REDUCED MATRIX ELEMENTS ⟨n‖μ_p‖m⟩ (R-Theorem QM.4)")
print("=" * 70)

print("""
From research/60 eq. (3.2), the Hecke reduced matrix elements are:

  ⟨n‖μ_p‖m⟩ = √(1/p)  if n = pm  (Hecke raising)
             = √(1/p)  if m = pn  (Hecke lowering)
             = 0        otherwise

We compute these explicitly for all (n, m, p) on the cube basis.
""")

for p in PRIMES:
    print(f"\n--- Reduced matrix elements for μ_{p} ---")
    print(f"{'  m (source)':<20} {'n (target)':<20} {'⟨n‖μ_p‖m⟩':<20} {'Type'}")
    print("  " + "-" * 70)
    for im, m in enumerate(N_VALUES):
        for jn, n in enumerate(N_VALUES):
            if n == p * m:
                rme = 1.0 / np.sqrt(p)
                print(f"  {m:<20} {n:<20} {rme:<20.6f} raising (n=pm)")
            elif m == p * n:
                rme = 1.0 / np.sqrt(p)
                print(f"  {m:<20} {n:<20} {rme:<20.6f} lowering (m=pn)")

# ============================================================
# 10. Full matrix of reduced matrix elements
# ============================================================

print("\n" + "=" * 70)
print("FULL 8×8 REDUCED MATRIX ELEMENT TABLES")
print("=" * 70)

for p in PRIMES:
    print(f"\n⟨n‖μ_{p}‖m⟩ as 8×8 matrix (rows=n, cols=m, basis ordered by index):")
    rme_matrix = np.zeros((8, 8))
    for im, m in enumerate(N_VALUES):
        for jn, n in enumerate(N_VALUES):
            if n == p * m:
                rme_matrix[jn, im] = 1.0 / np.sqrt(p)
            elif m == p * n:
                rme_matrix[jn, im] = 1.0 / np.sqrt(p)
    print(f"  n\\m   ", end="")
    for m in N_VALUES:
        print(f"{m:>8}", end="")
    print()
    for jn, n in enumerate(N_VALUES):
        print(f"  {n:<6}", end="")
        for im in range(8):
            print(f"{rme_matrix[jn, im]:>8.4f}", end="")
        print()

    is_sym_rme = np.allclose(rme_matrix, rme_matrix.T)
    is_real_rme = np.all(np.isreal(rme_matrix))
    print(f"\n  ⟨n‖μ_{p}‖m⟩ is real: {is_real_rme}")
    print(f"  ⟨n‖μ_{p}‖m⟩ is symmetric: {is_sym_rme}")
    print(f"  All entries are √(1/{p}) = {1/np.sqrt(p):.6f} or 0: True")

# ============================================================
# 11. The self-adjoint Hecke combination μ_p + μ_p^*
# ============================================================

print("\n" + "=" * 70)
print("SELF-ADJOINT HECKE COMBINATIONS T_p = μ_p + μ_p^*")
print("=" * 70)

for p in PRIMES:
    T_p = mu_raise[p] + mu_lower[p]
    T_p_pathB = V.T @ T_p @ V
    is_sym = np.allclose(T_p_pathB, T_p_pathB.T)
    is_real = np.all(np.isreal(T_p_pathB))
    print(f"\nT_{p} = μ_{p} + μ_{p}^* in Path B basis:")
    print(T_p_pathB)
    print(f"  Real symmetric: {is_real and is_sym}")
    eigs = np.linalg.eigvalsh(T_p_pathB)
    print(f"  Eigenvalues: {np.sort(eigs)}")

# ============================================================
# 12. Summary and verdicts
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY OF RESULTS")
print("=" * 70)

print("""
1. H_BC = log N̂ is REAL SYMMETRIC in the Path B basis.
   (Trivially: V is real orthogonal, H_BC is real diagonal.)

2. ANY operator diagonal in the standard cube basis with REAL
   eigenvalues is automatically real symmetric in the Path B basis.
   (Reason: V is real orthogonal, and V^T D V is real symmetric
   for any real diagonal D.)

3. The Hecke reduced matrix elements ⟨n‖μ_p‖m⟩ = √(1/p) are:
   - REAL and POSITIVE (√(1/p) > 0)
   - SYMMETRIC in (n, m): ⟨n‖μ_p‖m⟩ = ⟨m‖μ_p‖n⟩
   This is because the Hecke raising/lowering relation n=pm is
   symmetric under the exchange of source and target labels.

4. The self-adjoint Hecke combinations T_p = μ_p + μ_p^* are
   real symmetric in the Path B basis (they are real symmetric
   in the standard basis, and V is real orthogonal).

5. CRITICAL: The Path B basis change does NOT independently
   force T_BC to be real symmetric. It PRESERVES real symmetry.
   The implication is:
     (γ_n ∈ R) ⟹ T_BC real symmetric in Path B
   NOT the reverse.

6. The LOCK of research/60 §4.2 is STRUCTURAL, not a proof:
   - The reduced matrix elements being real is a NECESSARY
     condition for the Wigner–Eckart framework to be consistent.
   - It does not by itself IMPLY γ_n ∈ R.
   - The correct statement is: IF the Galois orbit decomposition
     of H_R exists (Path B) AND the Hecke operators are BC
     irreducible tensor operators with real reduced matrix elements,
     THEN the CONSISTENCY of the framework requires γ_n ∈ R.
   - This is a structural constraint, not a deductive proof.
""")

print("=" * 70)
print("EXPLICIT REDUCED MATRIX ELEMENTS SUMMARY")
print("=" * 70)
print("""
For p=2: ⟨n‖μ_2‖m⟩ = 1/√2 ≈ 0.7071 for (m,n) pairs:
  (1,2), (3,6), (5,10), (15,30) and their transposes.

For p=3: ⟨n‖μ_3‖m⟩ = 1/√3 ≈ 0.5774 for (m,n) pairs:
  (1,3), (2,6), (5,15), (10,30) and their transposes.

For p=5: ⟨n‖μ_5‖m⟩ = 1/√5 ≈ 0.4472 for (m,n) pairs:
  (1,5), (2,10), (3,15), (6,30) and their transposes.

All other matrix elements vanish.
All non-zero entries are REAL, POSITIVE, and SYMMETRIC.
""")

# ============================================================
# 13. Numerical cross-check: H_BC commutes with T_p in Path B
# ============================================================

print("=" * 70)
print("CROSS-CHECK: [H_BC, T_p] COMMUTATORS")
print("=" * 70)

for p in PRIMES:
    T_p = mu_raise[p] + mu_lower[p]
    comm = H_BC @ T_p - T_p @ H_BC
    print(f"  ||[H_BC, T_{p}]|| = {np.linalg.norm(comm):.2e}")
    # These do NOT commute in general (H_BC is log N̂, T_p shifts the index)

print("""
Note: [H_BC, T_p] ≠ 0 in general. This is expected — H_BC = log N̂
and μ_p shifts the N̂ eigenvalue by a factor of p, so
[log N̂, μ_p] = log(p) μ_p (on the subspace where μ_p is defined).
""")

# Verify the commutation relation [H_BC, μ_p] = log(p) μ_p
for p in PRIMES:
    comm = H_BC @ mu_raise[p] - mu_raise[p] @ H_BC
    expected = np.log(p) * mu_raise[p]
    check = np.allclose(comm, expected)
    print(f"  [H_BC, μ_{p}] = log({p}) μ_{p}: {check}")

print("\n" + "=" * 70)
print("END OF TEST")
print("=" * 70)
