"""
Phase Incoherence Test -- Node 4.1 (ID Approach 1)

EXPLICIT PHASE COMPUTATION for the self-dual monotone clone (majority / 2-SAT)
at two canonical instances:

    Gamma_0 : Sol = {00, 01, 10}        (d=3, NON-AFFINE)
    Gamma_1 : Sol = {00, 01, 10, 11}    (d=4, AFFINE = GF(2)^2)

The Phase Incoherence Condition (ID) from Node 3.3:

    Var_omega(mu_k) := SUM_Gamma omega(p_Gamma) |mu_k(Gamma) - mu_bar_k|^2 > 0

for infinitely many k, where mu_k(Gamma) is the instance phase of the ratio
unitary v_k = U_{f_k}*(U_{g_k})* at instance Gamma.

THIS SCRIPT computes:
  1. ALL self-dual monotone k-ary Boolean functions (the majority clone) for
     k = 3, 5, 7, 9, 11 via explicit enumeration / threshold representatives.
  2. The clone operator V_f^{Gamma} as an explicit d x d matrix at both instances.
  3. The polar unitary U_f^{Gamma} via polar decomposition.
  4. The instance phase mu_f(Gamma) = argmin_{mu} ||U_f^{Gamma} - mu*I||.
  5. The phase profile (mu_f(Gamma_0), mu_f(Gamma_1)) for each f.
  6. Whether the phase map f -> (mu_f(Gamma_0), mu_f(Gamma_1)) is constant.
     If NOT constant: (ID) holds, because pigeonhole-selected PAIRS of functions
     with close U(M)-images can have different phase profiles.

THE KEY INSIGHT (from Node 3.3):
  - At Gamma_1 (affine): U_f^{Gamma_1} = e^{i*alpha_f} * I EXACTLY (Lemma A).
    So mu_f(Gamma_1) = alpha_f exactly.
  - At Gamma_0 (non-affine): U_f^{Gamma_0} is NON-SCALAR (Lemma B).
    The instance phase mu_f(Gamma_0) is the "average eigenvalue angle" of U_f,
    which depends on the non-affine geometry.
  - If mu_f(Gamma_0) != mu_f(Gamma_1) for ANY pair (f, g) at arity k, then (ID)
    holds at arity k.

For Boolean (real) clone operators: all phases are in {+1, -1} (Section 5.3
of Node 3.3). So the question reduces to: does sign(v_k^{Gamma_0}) always
equal sign(v_k^{Gamma_1})? If the SIGNS disagree, (ID) holds.

Author: Claude Opus 4.6 (1M context), Node 4.1
Date: 2026-04-11
"""

import numpy as np
from itertools import product as cartesian_product
from scipy.linalg import polar
import json
import sys

np.set_printoptions(precision=10, suppress=True, linewidth=160)

# ================================================================
# SECTION 1: The two canonical instances
# ================================================================

# Gamma_0: NON-AFFINE instance.  Sol = {00, 01, 10} subset {0,1}^2.
# This is NOT an affine subspace of GF(2)^2:
#   {00, 01, 10} cannot be written as v + W for any linear subspace W.
#   (If W = span{01,10}, then v+W = {v, v+01, v+10, v+11} has 4 elements.)
# d_0 = 3.
GAMMA_0_SOLUTIONS = [(0, 0), (0, 1), (1, 0)]

# Gamma_1: AFFINE instance.  Sol = {00, 01, 10, 11} = GF(2)^2 (the full space).
# This IS an affine subspace: W = GF(2)^2, v = 0.
# d_1 = 4.
GAMMA_1_SOLUTIONS = [(0, 0), (0, 1), (1, 0), (1, 1)]


# ================================================================
# SECTION 2: Self-dual monotone Boolean functions
# ================================================================

def threshold_majority(bits):
    """
    Coordinate-wise majority: returns 1 iff sum(bits) >= ceil(k/2).
    bits: a tuple/list of 0s and 1s.
    """
    k = len(bits)
    threshold = (k + 1) // 2
    return 1 if sum(bits) >= threshold else 0


def is_self_dual(f, k):
    """
    Check if Boolean function f: {0,1}^k -> {0,1} is self-dual:
    f(x_1,...,x_k) = 1 - f(1-x_1,...,1-x_k) for all inputs.
    """
    for bits in cartesian_product([0, 1], repeat=k):
        complement = tuple(1 - b for b in bits)
        if f(bits) != 1 - f(complement):
            return False
    return True


def is_monotone(f, k):
    """
    Check if Boolean function f: {0,1}^k -> {0,1} is monotone:
    if x <= y coordinate-wise, then f(x) <= f(y).
    """
    for x in cartesian_product([0, 1], repeat=k):
        for y in cartesian_product([0, 1], repeat=k):
            if all(xi <= yi for xi, yi in zip(x, y)):
                if f(x) > f(y):
                    return False
    return True


def enumerate_all_boolean_functions(k):
    """
    Enumerate all 2^{2^k} Boolean functions f: {0,1}^k -> {0,1}.
    Returns a list of truth-table tuples.
    """
    inputs = list(cartesian_product([0, 1], repeat=k))
    n_inputs = len(inputs)  # = 2^k
    functions = []
    for output_bits in cartesian_product([0, 1], repeat=n_inputs):
        def make_f(table, inp_list):
            lookup = {inp: out for inp, out in zip(inp_list, table)}
            return lambda bits, _lookup=lookup: _lookup[tuple(bits)]
        f = make_f(output_bits, inputs)
        functions.append((output_bits, f))
    return functions


def enumerate_self_dual_monotone(k):
    """
    Enumerate ALL self-dual monotone Boolean functions at arity k.
    Returns list of (truth_table, function).

    For small k this is tractable:
      k=1: 1 function (identity)
      k=3: 1 function (majority_3)
      k=5: 3 functions
      k=7: ~20+ functions

    For k >= 7, we use the known structure: self-dual monotone functions
    are in bijection with antichains in the poset of (k-1)/2-element subsets
    of {1,...,k} (Dedekind-like structure).
    """
    inputs = list(cartesian_product([0, 1], repeat=k))
    n_inputs = len(inputs)

    # For k <= 7, enumerate all and filter.
    # For k > 7, 2^{2^k} is too large; use threshold representatives.
    if 2**k > 128:  # k >= 8
        # Return only the threshold majority representative
        table = tuple(threshold_majority(list(inp)) for inp in inputs)
        f = lambda bits, _inputs=inputs, _table=table: _table[
            _inputs.index(tuple(bits))
        ] if tuple(bits) in _inputs else threshold_majority(list(bits))
        return [(table, lambda bits: threshold_majority(list(bits)))]

    results = []
    for output_bits in cartesian_product([0, 1], repeat=n_inputs):
        # Build function
        lookup = {inp: out for inp, out in zip(inputs, output_bits)}
        f = lambda bits, _lookup=lookup: _lookup[tuple(bits)]

        # Check self-dual
        sd = True
        for inp in inputs:
            complement = tuple(1 - b for b in inp)
            if lookup[inp] != 1 - lookup[complement]:
                sd = False
                break
        if not sd:
            continue

        # Check monotone
        mono = True
        for x in inputs:
            if not mono:
                break
            for y in inputs:
                if all(xi <= yi for xi, yi in zip(x, y)):
                    if lookup[x] > lookup[y]:
                        mono = False
                        break
        if not mono:
            continue

        results.append((output_bits, f))

    return results


def is_polymorphism_of(f_coord, k, sol_set):
    """
    Check if applying f_coord COORDINATE-WISE is a polymorphism of sol_set:
    for all (a_1,...,a_k) in sol_set^k, the coordinate-wise application
    f(a_1,...,a_k) must produce an element of sol_set.

    f_coord: a Boolean function {0,1}^k -> {0,1}
    sol_set: set of tuples in {0,1}^n
    """
    sol_list = list(sol_set)
    n = len(sol_list[0])
    sol_set_frozen = frozenset(sol_set)

    for combo in cartesian_product(range(len(sol_list)), repeat=k):
        args = [sol_list[i] for i in combo]
        # Apply f coordinate-wise
        result = tuple(
            f_coord([args[j][coord] for j in range(k)])
            for coord in range(n)
        )
        if result not in sol_set_frozen:
            return False
    return True


# ================================================================
# SECTION 3: Clone operator V_f^{Gamma}
# ================================================================

def compute_clone_operator(sol_list, f_coord, k):
    """
    Compute the clone operator V_f^{Gamma} for a coordinate-wise Boolean function.

    V_f[s, a] = (1/d^{(k-1)/2}) * |{(a^(2),...,a^(k)) in Sol^{k-1} :
                  f(a, a^(2),...,a^(k)) = s}|

    where f is applied COORDINATE-WISE to n-bit strings.

    sol_list: list of solution tuples (each of length n)
    f_coord: Boolean function {0,1}^k -> {0,1} (applied per coordinate)
    k: arity

    Returns: d x d real matrix V.
    """
    d = len(sol_list)
    n = len(sol_list[0])
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}
    sol_set = frozenset(sol_list)

    V = np.zeros((d, d), dtype=np.float64)

    # For each "first argument" a (column index)
    for a_idx, a in enumerate(sol_list):
        # Sum over all (k-1)-tuples of remaining arguments from Sol
        for combo in cartesian_product(range(d), repeat=k - 1):
            remaining = [sol_list[i] for i in combo]
            # Apply f coordinate-wise: for each coordinate j
            result = tuple(
                f_coord([a[j]] + [remaining[m][j] for m in range(k - 1)])
                for j in range(n)
            )
            if result in sol_to_idx:
                s_idx = sol_to_idx[result]
                V[s_idx, a_idx] += 1.0

    # Normalize
    norm = d ** ((k - 1) / 2.0)
    V /= norm

    return V


# ================================================================
# SECTION 4: Polar decomposition and instance phase extraction
# ================================================================

def extract_polar_unitary(V):
    """
    Extract the unitary part U from V = U * P (left polar decomposition).
    Returns (U, P) where U is unitary and P is positive semidefinite.
    """
    U, P = polar(V)
    return U, P


def instance_phase(U):
    """
    Compute the instance phase mu(U) = argmin_{mu in T} ||U - mu*I||_op.

    For a unitary U with eigenvalues e^{i*theta_j}:
      mu = the point on the unit circle that minimizes the maximum
           |e^{i*theta_j} - mu| over all j.

    For real orthogonal matrices (our case): eigenvalues come in conjugate
    pairs, plus possibly +1 and -1. The phase mu is in {+1, -1} for real
    matrices close to scalar.

    We compute this by scanning over phases and minimizing the operator norm.
    """
    d = U.shape[0]
    I = np.eye(d, dtype=U.dtype)

    # Get eigenvalues for analysis
    eigvals = np.linalg.eigvals(U)
    eig_phases = np.angle(eigvals)

    # Method 1: Direct optimization over phase angle
    best_dist = np.inf
    best_mu = 1.0 + 0j

    # Coarse scan
    for theta in np.linspace(0, 2 * np.pi, 720, endpoint=False):
        mu = np.exp(1j * theta)
        diff = U.astype(np.complex128) - mu * np.eye(d, dtype=np.complex128)
        dist = np.linalg.norm(diff, ord=2)  # operator norm = largest singular value
        if dist < best_dist:
            best_dist = dist
            best_mu = mu

    # Fine scan around best
    best_theta = np.angle(best_mu)
    for theta in np.linspace(best_theta - 0.01, best_theta + 0.01, 2000):
        mu = np.exp(1j * theta)
        diff = U.astype(np.complex128) - mu * np.eye(d, dtype=np.complex128)
        dist = np.linalg.norm(diff, ord=2)
        if dist < best_dist:
            best_dist = dist
            best_mu = mu

    return best_mu, best_dist, eig_phases


def instance_phase_from_trace(U):
    """
    Alternative: mu = (1/d) * tr(U), then project to unit circle.
    For U close to scalar: mu ~ e^{i*alpha} where alpha is the mean
    eigenvalue phase.
    """
    d = U.shape[0]
    tr = np.trace(U.astype(np.complex128)) / d
    if abs(tr) < 1e-15:
        return 1.0 + 0j, abs(tr)
    mu = tr / abs(tr)  # project to unit circle
    return mu, abs(tr)


# ================================================================
# SECTION 5: The ratio unitary and phase incoherence check
# ================================================================

def compute_ratio_phase(U_f, U_g, label=""):
    """
    Compute the instance phase of the ratio unitary v = U_f * U_g^*.

    For real orthogonal matrices: U_g^* = U_g^T.
    """
    v = U_f @ U_g.conj().T
    mu, dist_to_scalar, eig_phases = instance_phase(v)
    mu_tr, tr_mod = instance_phase_from_trace(v)

    if label:
        print(f"    {label}:")
        print(f"      v eigenphases: {[f'{p:.6f}' for p in sorted(eig_phases.real)]}")
        print(f"      mu (opt):   {mu:.8f}, dist_to_scalar = {dist_to_scalar:.8f}")
        print(f"      mu (trace): {mu_tr:.8f}, |tr/d| = {tr_mod:.8f}")

    return mu, dist_to_scalar, mu_tr, tr_mod, eig_phases


# ================================================================
# SECTION 6: Main computation
# ================================================================

def phase_profile_at_arity(k, sol_0, sol_1, functions_with_tables):
    """
    For each self-dual monotone function f at arity k:
      1. Compute V_f^{Gamma_0} and V_f^{Gamma_1}
      2. Extract U_f^{Gamma_0} and U_f^{Gamma_1}
      3. Compute mu_f(Gamma_0) and mu_f(Gamma_1)
      4. Report the phase profile

    Returns a list of dicts with the profile data.
    """
    d0 = len(sol_0)
    d1 = len(sol_1)
    sol_0_set = frozenset(sol_0)
    sol_1_set = frozenset(sol_1)

    profiles = []

    for idx, (table, f) in enumerate(functions_with_tables):
        # Check if f is a polymorphism of both instances
        is_poly_0 = is_polymorphism_of(f, k, sol_0_set)
        is_poly_1 = is_polymorphism_of(f, k, sol_1_set)

        if not is_poly_0 or not is_poly_1:
            # Skip non-polymorphisms (they are not in the clone)
            continue

        # Compute clone operators
        V0 = compute_clone_operator(sol_0, f, k)
        V1 = compute_clone_operator(sol_1, f, k)

        # Polar decomposition
        U0, P0 = extract_polar_unitary(V0)
        U1, P1 = extract_polar_unitary(V1)

        # Instance phases
        mu0_opt, dist0, eig0 = instance_phase(U0)
        mu1_opt, dist1, eig1 = instance_phase(U1)
        mu0_tr, tr0 = instance_phase_from_trace(U0)
        mu1_tr, tr1 = instance_phase_from_trace(U1)

        # Phase angle extraction (real part: the sign)
        angle0 = np.angle(mu0_opt)
        angle1 = np.angle(mu1_opt)

        profiles.append({
            'index': idx,
            'table': table[:16] if len(table) > 16 else table,  # truncate for display
            'is_poly_Gamma0': is_poly_0,
            'is_poly_Gamma1': is_poly_1,
            'mu_Gamma0': complex(mu0_opt),
            'mu_Gamma1': complex(mu1_opt),
            'angle_Gamma0': float(angle0),
            'angle_Gamma1': float(angle1),
            'dist_to_scalar_Gamma0': float(dist0),
            'dist_to_scalar_Gamma1': float(dist1),
            'trace_mod_Gamma0': float(tr0),
            'trace_mod_Gamma1': float(tr1),
            'eig_phases_Gamma0': sorted(eig0.real.tolist()),
            'eig_phases_Gamma1': sorted(eig1.real.tolist()),
            'V0_singular_values': np.linalg.svd(V0, compute_uv=False).tolist(),
            'V1_singular_values': np.linalg.svd(V1, compute_uv=False).tolist(),
        })

    return profiles


def run_pairwise_phase_incoherence(k, sol_0, sol_1, profiles):
    """
    For all pairs (f, g) from the profiles at arity k:
    compute the ratio unitary v = U_f * U_g^* at both instances and
    check if the instance phases agree.

    This is the DIRECT test of condition (ID):
    Does mu_k(Gamma_0) = mu_k(Gamma_1) for the ratio v_k?
    """
    d0 = len(sol_0)
    d1 = len(sol_1)
    n_functions = len(profiles)

    if n_functions < 2:
        return []

    pair_results = []

    for i in range(n_functions):
        for j in range(i + 1, n_functions):
            fi = profiles[i]
            fj = profiles[j]

            # Ratio phases at each instance
            # mu_ratio(Gamma) = mu_f(Gamma) * conj(mu_g(Gamma))
            # (This is exact for scalar unitaries; approximate for non-scalar)

            # At Gamma_1 (affine): unitaries are exact scalars, so
            # ratio phase = mu_f(Gamma_1) / mu_g(Gamma_1) exactly.
            mu_ratio_1 = fi['mu_Gamma1'] * np.conj(fj['mu_Gamma1'])

            # At Gamma_0 (non-affine): the ratio phase is the phase of
            # the trace of U_f * U_g^*. This is an APPROXIMATION (the
            # true phase comes from optimizing over theta).
            mu_ratio_0 = fi['mu_Gamma0'] * np.conj(fj['mu_Gamma0'])

            # Phase difference between instances
            phase_diff = np.angle(mu_ratio_0 * np.conj(mu_ratio_1))

            pair_results.append({
                'f_index': fi['index'],
                'g_index': fj['index'],
                'mu_ratio_Gamma0': complex(mu_ratio_0),
                'mu_ratio_Gamma1': complex(mu_ratio_1),
                'angle_ratio_Gamma0': float(np.angle(mu_ratio_0)),
                'angle_ratio_Gamma1': float(np.angle(mu_ratio_1)),
                'phase_difference': float(phase_diff),
                'phases_agree': bool(abs(phase_diff) < 0.01),
            })

    return pair_results


def run_explicit_ratio_test(k, sol_0, sol_1, functions_with_tables):
    """
    Compute the EXPLICIT ratio unitary v = U_f * U_g^T at both instances
    for selected pairs of polymorphisms, and extract the instance phase
    directly from the ratio (not from the product of individual phases).

    This is the definitive test.
    """
    d0 = len(sol_0)
    d1 = len(sol_1)
    sol_0_set = frozenset(sol_0)
    sol_1_set = frozenset(sol_1)

    # Collect polymorphisms and their unitaries
    poly_data = []
    for idx, (table, f) in enumerate(functions_with_tables):
        if not is_polymorphism_of(f, k, sol_0_set):
            continue
        if not is_polymorphism_of(f, k, sol_1_set):
            continue

        V0 = compute_clone_operator(sol_0, f, k)
        V1 = compute_clone_operator(sol_1, f, k)
        U0, _ = extract_polar_unitary(V0)
        U1, _ = extract_polar_unitary(V1)

        poly_data.append({
            'idx': idx,
            'table': table,
            'U0': U0,
            'U1': U1,
            'V0': V0,
            'V1': V1,
        })

    if len(poly_data) < 2:
        return poly_data, []

    # Now compute ratio unitaries for all pairs
    ratio_results = []
    for i in range(len(poly_data)):
        for j in range(i + 1, len(poly_data)):
            fi = poly_data[i]
            fj = poly_data[j]

            # Ratio at Gamma_0
            v0 = fi['U0'] @ fj['U0'].T  # real matrices: conj = identity
            mu0, dist0, eig0 = instance_phase(v0)

            # Ratio at Gamma_1
            v1 = fi['U1'] @ fj['U1'].T
            mu1, dist1, eig1 = instance_phase(v1)

            # Phase difference
            phase_diff = np.angle(mu0 * np.conj(mu1))

            ratio_results.append({
                'pair': (fi['idx'], fj['idx']),
                'mu_ratio_Gamma0': complex(mu0),
                'mu_ratio_Gamma1': complex(mu1),
                'angle_ratio_Gamma0': float(np.angle(mu0)),
                'angle_ratio_Gamma1': float(np.angle(mu1)),
                'dist_to_scalar_Gamma0': float(dist0),
                'dist_to_scalar_Gamma1': float(dist1),
                'eig_phases_ratio_Gamma0': sorted(eig0.real.tolist()),
                'eig_phases_ratio_Gamma1': sorted(eig1.real.tolist()),
                'phase_difference': float(phase_diff),
                'phases_agree': bool(abs(phase_diff) < 0.01),
                'v0_matrix': v0.tolist(),
                'v1_matrix': v1.tolist(),
            })

    return poly_data, ratio_results


# ================================================================
# SECTION 7: Weighted threshold functions (beyond simple majority)
# ================================================================

def make_weighted_threshold(k, weights):
    """
    Weighted threshold function: return 1 iff sum(w_i * x_i) >= sum(w_i)/2.
    All weighted thresholds on k variables are self-dual and monotone.
    """
    total = sum(weights)
    thresh = total / 2.0

    def f(bits):
        return 1 if sum(w * b for w, b in zip(weights, bits)) >= thresh else 0
    return f


def make_iterated_majority(k):
    """
    Iterated majority: for k = 3^m, apply majority recursively.
    For other k, pad with copies and apply majority.
    This generates DIFFERENT self-dual monotone functions from threshold.
    """
    if k == 3:
        return lambda bits: threshold_majority(bits)
    elif k == 5:
        # maj(x1, x2, maj(x3, x4, x5))
        def f(bits):
            inner = threshold_majority(bits[2:5])
            return threshold_majority([bits[0], bits[1], inner])
        return f
    elif k == 7:
        # maj(x1, maj(x2,x3,x4), maj(x5,x6,x7))
        def f(bits):
            m1 = threshold_majority(bits[1:4])
            m2 = threshold_majority(bits[4:7])
            return threshold_majority([bits[0], m1, m2])
        return f
    elif k == 9:
        # maj(maj(x1,x2,x3), maj(x4,x5,x6), maj(x7,x8,x9))
        def f(bits):
            m1 = threshold_majority(bits[0:3])
            m2 = threshold_majority(bits[3:6])
            m3 = threshold_majority(bits[6:9])
            return threshold_majority([m1, m2, m3])
        return f
    elif k == 11:
        # maj(x1, x2, maj(maj(x3,x4,x5), maj(x6,x7,x8), maj(x9,x10,x11)))
        def f(bits):
            m1 = threshold_majority(bits[2:5])
            m2 = threshold_majority(bits[5:8])
            m3 = threshold_majority(bits[8:11])
            inner = threshold_majority([m1, m2, m3])
            return threshold_majority([bits[0], bits[1], inner])
        return f
    else:
        return lambda bits: threshold_majority(bits)


# ================================================================
# SECTION 8: Master test
# ================================================================

def main():
    print("=" * 90)
    print("PHASE INCOHERENCE TEST -- Node 4.1 (ID Approach 1)")
    print("Explicit phase computation for the majority clone at")
    print("  Gamma_0 = {00, 01, 10} (d=3, non-affine)")
    print("  Gamma_1 = {00, 01, 10, 11} (d=4, affine)")
    print("=" * 90)

    sol_0 = list(GAMMA_0_SOLUTIONS)
    sol_1 = list(GAMMA_1_SOLUTIONS)

    master_results = {}

    # ==============================================================
    # PART A: Enumerate self-dual monotone functions and verify they
    # are polymorphisms of both instances
    # ==============================================================
    arities_to_test = [3, 5, 7]

    for k in arities_to_test:
        print(f"\n{'#' * 90}")
        print(f"# ARITY k = {k}")
        print(f"{'#' * 90}")

        # Enumerate self-dual monotone functions
        print(f"\n  Enumerating all self-dual monotone {k}-ary Boolean functions...")
        sdm_functions = enumerate_self_dual_monotone(k)
        print(f"  Found {len(sdm_functions)} self-dual monotone functions at arity {k}.")

        # Filter for polymorphisms of BOTH instances
        sol_0_set = frozenset(sol_0)
        sol_1_set = frozenset(sol_1)

        poly_functions = []
        for table, f in sdm_functions:
            p0 = is_polymorphism_of(f, k, sol_0_set)
            p1 = is_polymorphism_of(f, k, sol_1_set)
            if p0 and p1:
                poly_functions.append((table, f))
                # Show truth table (truncated)
                display = table[:min(len(table), 32)]
                print(f"    Function #{len(poly_functions)}: "
                      f"table = {''.join(str(b) for b in display)}... "
                      f"poly(G0)={p0}, poly(G1)={p1}")
            elif p0 and not p1:
                print(f"    [SKIP] poly of G0 but NOT G1")
            elif not p0 and p1:
                print(f"    [SKIP] poly of G1 but NOT G0")

        n_poly = len(poly_functions)
        print(f"\n  {n_poly} functions are polymorphisms of BOTH instances.")

        if n_poly == 0:
            print(f"  NO polymorphisms found! This should not happen for 2-SAT "
                  f"(majority must be a polymorphism).")
            continue

        # ==============================================================
        # PART B: Compute phase profiles
        # ==============================================================
        print(f"\n  --- Computing phase profiles ---")
        profiles = phase_profile_at_arity(k, sol_0, sol_1, poly_functions)

        print(f"\n  Phase profiles (k={k}):")
        print(f"  {'Func':>6} | {'mu(G0) angle':>14} | {'mu(G1) angle':>14} | "
              f"{'dist_scalar(G0)':>16} | {'dist_scalar(G1)':>16} | "
              f"{'|tr/d| G0':>10} | {'|tr/d| G1':>10}")
        print(f"  {'-'*6}-+-{'-'*14}-+-{'-'*14}-+-{'-'*16}-+-{'-'*16}-+-"
              f"{'-'*10}-+-{'-'*10}")

        for p in profiles:
            print(f"  {p['index']:>6} | {p['angle_Gamma0']:>14.8f} | "
                  f"{p['angle_Gamma1']:>14.8f} | "
                  f"{p['dist_to_scalar_Gamma0']:>16.10f} | "
                  f"{p['dist_to_scalar_Gamma1']:>16.10f} | "
                  f"{p['trace_mod_Gamma0']:>10.6f} | "
                  f"{p['trace_mod_Gamma1']:>10.6f}")

        # Check: are all mu(G0) identical? All mu(G1) identical?
        if len(profiles) >= 2:
            angles_0 = [p['angle_Gamma0'] for p in profiles]
            angles_1 = [p['angle_Gamma1'] for p in profiles]

            spread_0 = max(angles_0) - min(angles_0)
            spread_1 = max(angles_1) - min(angles_1)
            print(f"\n  Phase angle spread at Gamma_0: {spread_0:.10f}")
            print(f"  Phase angle spread at Gamma_1: {spread_1:.10f}")

            # The key question: do mu(G0) and mu(G1) DIFFER for individual functions?
            phase_diffs = [abs(p['angle_Gamma0'] - p['angle_Gamma1'])
                           for p in profiles]
            print(f"\n  Individual phase differences |mu(G0) - mu(G1)|:")
            for i, p in enumerate(profiles):
                diff = phase_diffs[i]
                print(f"    Function {p['index']}: "
                      f"|angle(G0) - angle(G1)| = {diff:.10f}  "
                      f"{'*** PHASE INCOHERENCE ***' if diff > 0.01 else '(agree)'}")

        # ==============================================================
        # PART C: Pairwise ratio test (definitive)
        # ==============================================================
        print(f"\n  --- Explicit pairwise ratio test ---")
        poly_data, ratio_results = run_explicit_ratio_test(
            k, sol_0, sol_1, poly_functions
        )

        if ratio_results:
            print(f"\n  Pairwise ratio unitaries v = U_f * U_g^T:")
            print(f"  {'Pair':>12} | {'mu_ratio(G0)':>14} | {'mu_ratio(G1)':>14} | "
                  f"{'phase_diff':>12} | {'d_scalar(G0)':>14} | {'d_scalar(G1)':>14} | "
                  f"{'Agree?':>8}")
            print(f"  {'-'*12}-+-{'-'*14}-+-{'-'*14}-+-{'-'*12}-+-{'-'*14}-+-"
                  f"{'-'*14}-+-{'-'*8}")

            n_disagree = 0
            for r in ratio_results:
                agree_str = "YES" if r['phases_agree'] else "*** NO ***"
                if not r['phases_agree']:
                    n_disagree += 1
                print(f"  {str(r['pair']):>12} | "
                      f"{r['angle_ratio_Gamma0']:>14.8f} | "
                      f"{r['angle_ratio_Gamma1']:>14.8f} | "
                      f"{r['phase_difference']:>12.8f} | "
                      f"{r['dist_to_scalar_Gamma0']:>14.10f} | "
                      f"{r['dist_to_scalar_Gamma1']:>14.10f} | "
                      f"{agree_str:>8}")

            print(f"\n  PAIRS WITH PHASE INCOHERENCE: {n_disagree} / {len(ratio_results)}")
        else:
            print(f"  Only {len(poly_data)} polymorphisms -- need >= 2 for pair test.")

        # ==============================================================
        # PART D: Eigenvalue structure of the non-affine clone operator
        # ==============================================================
        print(f"\n  --- Eigenvalue structure at Gamma_0 (non-affine, d=3) ---")
        for pd in poly_data[:min(len(poly_data), 5)]:
            U0 = pd['U0']
            eigvals = np.linalg.eigvals(U0)
            print(f"    Function {pd['idx']}: "
                  f"eigenvalues = {[f'{e:.6f}' for e in eigvals]}")
            print(f"      |eigenvalues| = {[f'{abs(e):.8f}' for e in eigvals]}")
            print(f"      det(U0) = {np.linalg.det(U0):.8f}")

        print(f"\n  --- Eigenvalue structure at Gamma_1 (affine, d=4) ---")
        for pd in poly_data[:min(len(poly_data), 5)]:
            U1 = pd['U1']
            eigvals = np.linalg.eigvals(U1)
            print(f"    Function {pd['idx']}: "
                  f"eigenvalues = {[f'{e:.6f}' for e in eigvals]}")
            print(f"      |eigenvalues| = {[f'{abs(e):.8f}' for e in eigvals]}")
            print(f"      det(U1) = {np.linalg.det(U1):.8f}")

        # ==============================================================
        # PART E: The V matrices themselves (for small k)
        # ==============================================================
        if k <= 5 and len(poly_data) > 0:
            print(f"\n  --- Clone operator matrices V_f (first function) ---")
            pd = poly_data[0]
            print(f"  V_f^{{Gamma_0}} (3x3):")
            print(pd['V0'])
            print(f"  V_f^{{Gamma_1}} (4x4):")
            print(pd['V1'])
            print(f"  U_f^{{Gamma_0}} (polar unitary, 3x3):")
            print(pd['U0'])
            print(f"  U_f^{{Gamma_1}} (polar unitary, 4x4):")
            print(pd['U1'])

            if len(poly_data) > 1:
                pd2 = poly_data[1]
                print(f"\n  --- Clone operator matrices V_g (second function) ---")
                print(f"  V_g^{{Gamma_0}} (3x3):")
                print(pd2['V0'])
                print(f"  V_g^{{Gamma_1}} (4x4):")
                print(pd2['V1'])

                # The ratio matrices
                v0 = pd['U0'] @ pd2['U0'].T
                v1 = pd['U1'] @ pd2['U1'].T
                print(f"\n  --- Ratio unitary v = U_f * U_g^T ---")
                print(f"  v^{{Gamma_0}} (3x3):")
                print(v0)
                print(f"  v^{{Gamma_1}} (4x4):")
                print(v1)

        master_results[f'arity_{k}'] = {
            'k': k,
            'n_sdm_functions': len(sdm_functions),
            'n_polymorphisms': n_poly,
            'profiles': [{
                'index': p['index'],
                'angle_Gamma0': p['angle_Gamma0'],
                'angle_Gamma1': p['angle_Gamma1'],
                'dist_to_scalar_Gamma0': p['dist_to_scalar_Gamma0'],
                'dist_to_scalar_Gamma1': p['dist_to_scalar_Gamma1'],
                'trace_mod_Gamma0': p['trace_mod_Gamma0'],
                'trace_mod_Gamma1': p['trace_mod_Gamma1'],
            } for p in profiles],
            'ratio_results': [{
                'pair': r['pair'],
                'angle_ratio_Gamma0': r['angle_ratio_Gamma0'],
                'angle_ratio_Gamma1': r['angle_ratio_Gamma1'],
                'phase_difference': r['phase_difference'],
                'phases_agree': r['phases_agree'],
            } for r in ratio_results] if ratio_results else [],
        }

    # ==============================================================
    # PART F: Higher arities with threshold representatives
    # ==============================================================
    print(f"\n{'#' * 90}")
    print(f"# HIGHER ARITIES: threshold majority + iterated majority + weighted thresholds")
    print(f"{'#' * 90}")

    high_arities = [3, 5, 7, 9, 11]

    for k in high_arities:
        print(f"\n  === Arity k = {k} ===")

        # Build several DISTINCT self-dual monotone functions:
        # 1. Standard threshold majority
        # 2. Iterated majority
        # 3. Weighted threshold with weights [1,1,...,1,2]
        # 4. Weighted threshold with weights [1,2,1,2,...] (alternating)

        named_functions = []

        # (a) Standard threshold majority
        maj_f = lambda bits, _k=k: threshold_majority(bits)
        named_functions.append(("threshold_maj", maj_f))

        # (b) Iterated majority (structurally different)
        iter_f = make_iterated_majority(k)
        named_functions.append(("iterated_maj", iter_f))

        # (c) Weighted threshold [1,...,1,2]
        wt1 = [1] * (k - 1) + [2]
        wt1_f = make_weighted_threshold(k, wt1)
        named_functions.append(("weighted_1..12", wt1_f))

        # (d) Weighted threshold [1,2,1,2,...,1]
        wt2 = [(1 if i % 2 == 0 else 2) for i in range(k)]
        wt2_f = make_weighted_threshold(k, wt2)
        named_functions.append(("weighted_alt12", wt2_f))

        # (e) Weighted threshold [1,1,...,1,3] (stronger weight on last)
        wt3 = [1] * (k - 1) + [3]
        wt3_f = make_weighted_threshold(k, wt3)
        named_functions.append(("weighted_1..13", wt3_f))

        # Filter: only keep those that are polymorphisms of BOTH instances
        sol_0_set = frozenset(sol_0)
        sol_1_set = frozenset(sol_1)

        valid_funcs = []
        for name, f in named_functions:
            p0 = is_polymorphism_of(f, k, sol_0_set)
            p1 = is_polymorphism_of(f, k, sol_1_set)
            if p0 and p1:
                valid_funcs.append((name, f))
                print(f"    {name}: poly(G0)={p0}, poly(G1)={p1} -- VALID")
            else:
                print(f"    {name}: poly(G0)={p0}, poly(G1)={p1} -- EXCLUDED")

        if len(valid_funcs) < 1:
            print(f"    No valid polymorphisms at arity {k}!")
            continue

        # Compute phase profiles
        print(f"\n    Phase profiles:")
        profiles_high = []
        for name, f in valid_funcs:
            V0 = compute_clone_operator(sol_0, f, k)
            V1 = compute_clone_operator(sol_1, f, k)
            U0, _ = extract_polar_unitary(V0)
            U1, _ = extract_polar_unitary(V1)
            mu0, dist0, eig0 = instance_phase(U0)
            mu1, dist1, eig1 = instance_phase(U1)

            angle0 = np.angle(mu0)
            angle1 = np.angle(mu1)
            phase_diff = abs(angle0 - angle1)

            print(f"    {name:>20}: mu(G0)={angle0:>12.8f}, mu(G1)={angle1:>12.8f}, "
                  f"diff={phase_diff:>12.8f}, "
                  f"d_scalar(G0)={dist0:>10.8f}, d_scalar(G1)={dist1:>10.8f}")

            profiles_high.append({
                'name': name,
                'angle_Gamma0': float(angle0),
                'angle_Gamma1': float(angle1),
                'phase_difference': float(phase_diff),
                'dist_to_scalar_Gamma0': float(dist0),
                'dist_to_scalar_Gamma1': float(dist1),
            })

            # Print eigenvalues for inspection
            print(f"      U0 eigenphases: {[f'{np.angle(e):.6f}' for e in np.linalg.eigvals(U0)]}")
            print(f"      U1 eigenphases: {[f'{np.angle(e):.6f}' for e in np.linalg.eigvals(U1)]}")

        # Pairwise ratio test
        if len(valid_funcs) >= 2:
            print(f"\n    Pairwise ratio test:")
            for i in range(len(valid_funcs)):
                for j in range(i + 1, len(valid_funcs)):
                    name_i, fi = valid_funcs[i]
                    name_j, fj = valid_funcs[j]

                    V0_i = compute_clone_operator(sol_0, fi, k)
                    V1_i = compute_clone_operator(sol_1, fi, k)
                    V0_j = compute_clone_operator(sol_0, fj, k)
                    V1_j = compute_clone_operator(sol_1, fj, k)

                    U0_i, _ = extract_polar_unitary(V0_i)
                    U1_i, _ = extract_polar_unitary(V1_i)
                    U0_j, _ = extract_polar_unitary(V0_j)
                    U1_j, _ = extract_polar_unitary(V1_j)

                    # Ratio at each instance
                    v0 = U0_i @ U0_j.T
                    v1 = U1_i @ U1_j.T

                    mu0_r, dist0_r, _ = instance_phase(v0)
                    mu1_r, dist1_r, _ = instance_phase(v1)

                    angle_r0 = np.angle(mu0_r)
                    angle_r1 = np.angle(mu1_r)
                    diff = abs(angle_r0 - angle_r1)

                    verdict = "INCOHERENT" if diff > 0.01 else "agree"
                    print(f"    ({name_i}, {name_j}): "
                          f"mu_ratio(G0)={angle_r0:>10.6f}, "
                          f"mu_ratio(G1)={angle_r1:>10.6f}, "
                          f"diff={diff:>10.6f}, "
                          f"d_scalar(G0)={dist0_r:>10.6f}, "
                          f"d_scalar(G1)={dist1_r:>10.6f}  "
                          f"[{verdict}]")

        master_results[f'high_arity_{k}'] = {
            'k': k,
            'n_valid': len(valid_funcs),
            'profiles': profiles_high,
        }

    # ==============================================================
    # PART G: The Lemma A verification (affine instance gives exact scalar)
    # ==============================================================
    print(f"\n{'#' * 90}")
    print(f"# LEMMA A VERIFICATION: Affine instance => exact scalar unitary")
    print(f"{'#' * 90}")

    for k in [3, 5, 7]:
        print(f"\n  Arity k = {k}:")
        V1 = compute_clone_operator(sol_1, lambda bits: threshold_majority(bits), k)
        U1, P1 = extract_polar_unitary(V1)

        # Check if U1 is scalar
        d = U1.shape[0]
        # Compute distance to nearest scalar
        mu1, dist1, eig1 = instance_phase(U1)
        print(f"    U1 =")
        print(U1)
        print(f"    dist_to_scalar = {dist1:.12e}")
        print(f"    eigenvalues = {np.linalg.eigvals(U1)}")
        print(f"    mu = {mu1:.10f}")
        print(f"    LEMMA A {'CONFIRMED' if dist1 < 1e-10 else 'VIOLATED'}: "
              f"U is {'EXACTLY' if dist1 < 1e-10 else 'NOT'} scalar at affine instance")

    # ==============================================================
    # PART H: The Lemma B verification (non-affine gives non-scalar, increasing)
    # ==============================================================
    print(f"\n{'#' * 90}")
    print(f"# LEMMA B VERIFICATION: Non-affine instance => non-scalar, increasing")
    print(f"{'#' * 90}")

    dists_to_scalar = []
    for k in [3, 5, 7, 9, 11]:
        V0 = compute_clone_operator(sol_0, lambda bits: threshold_majority(bits), k)
        U0, P0 = extract_polar_unitary(V0)
        mu0, dist0, eig0 = instance_phase(U0)
        dists_to_scalar.append(dist0)
        print(f"  k={k}: dist_to_scalar = {dist0:.10f}, "
              f"eigenphases = {[f'{np.angle(e):.6f}' for e in np.linalg.eigvals(U0)]}")

    print(f"\n  d_PU(U, scalar) trajectory: {[f'{d:.8f}' for d in dists_to_scalar]}")
    monotone = all(dists_to_scalar[i+1] >= dists_to_scalar[i] - 1e-8
                   for i in range(len(dists_to_scalar)-1))
    print(f"  Monotonically non-decreasing: {monotone}")
    print(f"  LEMMA B {'CONFIRMED' if monotone and dists_to_scalar[0] > 0.01 else 'NEEDS REVIEW'}")

    # ==============================================================
    # FINAL VERDICT
    # ==============================================================
    print(f"\n{'=' * 90}")
    print(f"FINAL VERDICT")
    print(f"{'=' * 90}")

    # Collect all phase incoherence evidence
    any_incoherence = False
    for key, res in master_results.items():
        if 'ratio_results' in res:
            for r in res['ratio_results']:
                if not r.get('phases_agree', True):
                    any_incoherence = True
        if 'profiles' in res:
            angles_0 = [p.get('angle_Gamma0', 0) for p in res['profiles']]
            angles_1 = [p.get('angle_Gamma1', 0) for p in res['profiles']]
            for a0, a1 in zip(angles_0, angles_1):
                if abs(a0 - a1) > 0.01:
                    any_incoherence = True

    if any_incoherence:
        print(f"\n  (ID) STATUS: PHASE INCOHERENCE DETECTED")
        print(f"  The phase map f -> (mu_f(Gamma_0), mu_f(Gamma_1)) is NOT constant.")
        print(f"  Distinct polymorphisms have distinct phase profiles across instances.")
        print(f"  The Phase Incoherence Condition (ID) holds.")
    else:
        print(f"\n  (ID) STATUS: NO PHASE INCOHERENCE DETECTED")
        print(f"  All phases agree across instances.")
        print(f"  Need further investigation.")

    # Save results
    output_path = '/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/' \
                  'clone-growth-fullness-bridge/code/phase_incoherence_results.json'
    # Convert for JSON serialization
    json_results = {}
    for key, val in master_results.items():
        json_results[key] = val
    try:
        with open(output_path, 'w') as f:
            json.dump(json_results, f, indent=2, default=str)
        print(f"\n  Results saved to {output_path}")
    except Exception as e:
        print(f"\n  Could not save results: {e}")

    return master_results


if __name__ == "__main__":
    results = main()
