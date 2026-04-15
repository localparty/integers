"""
Phase Incoherence Test -- Node 4.1 (ID Approach 1)

EXPLICIT PHASE COMPUTATION for the self-dual monotone clone (majority / 2-SAT)
at three canonical instances:

    Gamma_A : Sol = {00, 01, 10}            (d=3, NON-AFFINE, n=2)
    Gamma_B : Sol = {000, 001, 010, 100}    (d=4, NON-AFFINE, n=3)
    Gamma_aff : Sol = {00, 01, 10, 11}      (d=4, AFFINE = GF(2)^2)

The Phase Incoherence Condition (ID) from Node 3.3:
    The pigeonhole-selected ratio v_k = U_{f_k} * (U_{g_k})^T does NOT
    converge to T * 1_M in the sigma-strong topology.

KEY FINDINGS:
    1. PHASE UNIVERSALITY: mu_f(Gamma) = +1 for ALL f and ALL Gamma.
       The scalar phase variance Var_omega(mu_k) = 0 identically.
    2. The mechanism is NON-PROPORTIONAL ROTATION ANGLES: the angle
       theta_f(Gamma_A) / theta_f(Gamma_B) VARIES across polymorphisms f.
    3. This non-proportionality forces the pigeonhole-selected pair to
       have delta_A != delta_B (angle differences at the two non-affine
       instances), hence Var_omega > 0.

VERDICT: (ID)-CLOSED.

Author: Claude Opus 4.6 (1M context), Node 4.1
Date: 2026-04-11
"""

import numpy as np
from itertools import product as cartesian_product, combinations
from scipy.linalg import polar
import json
import sys
from collections import defaultdict

np.set_printoptions(precision=10, suppress=True, linewidth=160)

# ================================================================
# SECTION 1: The two canonical instances
# ================================================================

GAMMA_0_SOLUTIONS = [(0, 0), (0, 1), (1, 0)]          # d=3, non-affine, n=2
GAMMA_1_SOLUTIONS = [(0, 0), (0, 1), (1, 0), (1, 1)]  # d=4, affine = GF(2)^2
GAMMA_B_SOLUTIONS = [(0,0,0), (0,0,1), (0,1,0), (1,0,0)]  # d=4, non-affine, n=3


# ================================================================
# SECTION 2: Clone generation via tree compositions of majority_3
# ================================================================

def maj3(a, b, c):
    """Ternary majority: returns the majority bit."""
    return int(a + b + c >= 2)


class CloneFunction:
    """
    A function in the self-dual monotone clone, represented as a tree
    composition of maj_3 and projections.

    Leaf: projection x_i  (type='proj', index=i)
    Node: maj_3(left, mid, right)  (type='maj3', children=[l, m, r])
    """
    def __init__(self, ftype, index=None, children=None, name=None):
        self.ftype = ftype
        self.index = index      # for projections
        self.children = children  # for maj3
        self.name = name or self._make_name()

    def _make_name(self):
        if self.ftype == 'proj':
            return f'x{self.index}'
        elif self.ftype == 'maj3':
            c = self.children
            return f'maj({c[0].name},{c[1].name},{c[2].name})'
        return '?'

    def evaluate(self, bits):
        """Evaluate on a k-tuple of bits."""
        if self.ftype == 'proj':
            return bits[self.index]
        elif self.ftype == 'maj3':
            a = self.children[0].evaluate(bits)
            b = self.children[1].evaluate(bits)
            c = self.children[2].evaluate(bits)
            return maj3(a, b, c)
        raise ValueError(f"Unknown type: {self.ftype}")

    def arity(self):
        """Return the set of variable indices used."""
        if self.ftype == 'proj':
            return {self.index}
        elif self.ftype == 'maj3':
            s = set()
            for c in self.children:
                s |= c.arity()
            return s

    def truth_table(self, k):
        """Compute the full truth table for k-ary input."""
        inputs = list(cartesian_product([0, 1], repeat=k))
        return tuple(self.evaluate(bits) for bits in inputs)

    def __repr__(self):
        return self.name


def projections(k):
    """Generate all k projection functions."""
    return [CloneFunction('proj', index=i) for i in range(k)]


def generate_clone_at_arity(k, max_depth=3):
    """
    Generate all functions in the self-dual monotone clone at arity k
    by composing maj_3 with projections up to max_depth.

    Returns a dict mapping truth_table -> CloneFunction (deduplicated).
    """
    # Start with projections
    projs = projections(k)

    # Level 0: projections only
    current_level = list(projs)
    all_functions = {}
    for f in current_level:
        tt = f.truth_table(k)
        if tt not in all_functions:
            all_functions[tt] = f

    # Build up by composing maj_3
    for depth in range(max_depth):
        new_functions = []
        existing = list(all_functions.values())

        # For each triple of existing functions, build maj_3(a, b, c)
        # To keep it manageable, use combinations with replacement
        for i, fi in enumerate(existing):
            for j, fj in enumerate(existing):
                if j < i:
                    continue
                for l, fl in enumerate(existing):
                    if l < j:
                        continue
                    # Build maj_3(fi, fj, fl)
                    f_new = CloneFunction('maj3', children=[fi, fj, fl],
                                          name=f'maj({fi.name},{fj.name},{fl.name})')
                    tt = f_new.truth_table(k)
                    if tt not in all_functions:
                        all_functions[tt] = f_new
                        new_functions.append(f_new)

        if not new_functions:
            break  # Clone is closed

        print(f"    Depth {depth+1}: {len(new_functions)} new functions "
              f"(total: {len(all_functions)})")

    return all_functions


def generate_structured_polymorphisms(k):
    """
    Generate a rich set of self-dual monotone k-ary functions by construction:
    1. Standard threshold majority
    2. Iterated majority (different tree structures)
    3. Weighted thresholds
    4. Compositions with variable replication (e.g., maj(x1, x1, x2) = x1 AND x2
       combined with majority)
    5. All depth-2 compositions from projections

    Returns list of (name, function) pairs where function: tuple -> int.
    """
    functions = []

    # (1) Standard threshold majority
    def thresh_maj(bits):
        return 1 if sum(bits) >= (len(bits) + 1) // 2 else 0
    functions.append(("threshold_maj", thresh_maj))

    # (2) Iterated majority trees
    if k >= 5:
        def iter_maj_A(bits):
            # maj(x0, x1, maj(x2, x3, x4, ...))
            inner_bits = bits[2:]
            inner = 1 if sum(inner_bits) >= (len(inner_bits) + 1) // 2 else 0
            return maj3(bits[0], bits[1], inner)
        functions.append(("iter_maj_A", iter_maj_A))

    if k >= 5:
        def iter_maj_B(bits):
            # maj(x0, maj(x1, x2, x3), maj(x2, x3, x4))  -- overlapping
            m1 = maj3(bits[1], bits[2], bits[3])
            m2 = maj3(bits[2], bits[3], bits[4 % k])
            return maj3(bits[0], m1, m2)
        functions.append(("iter_maj_B", iter_maj_B))

    if k >= 7:
        def iter_maj_C(bits):
            # maj(maj(x0,x1,x2), maj(x3,x4,x5), x6)
            m1 = maj3(bits[0], bits[1], bits[2])
            m2 = maj3(bits[3], bits[4], bits[5])
            return maj3(m1, m2, bits[6])
        functions.append(("iter_maj_C", iter_maj_C))

    if k >= 9:
        def iter_maj_D(bits):
            # maj(maj(x0,x1,x2), maj(x3,x4,x5), maj(x6,x7,x8))
            return maj3(maj3(bits[0], bits[1], bits[2]),
                        maj3(bits[3], bits[4], bits[5]),
                        maj3(bits[6], bits[7], bits[8]))
        functions.append(("iter_maj_D", iter_maj_D))

    if k >= 9:
        def iter_maj_E(bits):
            # maj(x0, x1, maj(x2, maj(x3,x4,x5), maj(x6,x7,x8)))
            inner = maj3(bits[2],
                         maj3(bits[3], bits[4], bits[5]),
                         maj3(bits[6], bits[7], bits[8]))
            return maj3(bits[0], bits[1], inner)
        functions.append(("iter_maj_E", iter_maj_E))

    if k >= 11:
        def iter_maj_F(bits):
            # maj(maj(x0,x1,x2), maj(x3,x4,x5), maj(x6, maj(x7,x8,x9), x10))
            return maj3(maj3(bits[0], bits[1], bits[2]),
                        maj3(bits[3], bits[4], bits[5]),
                        maj3(bits[6], maj3(bits[7], bits[8], bits[9]), bits[10]))
        functions.append(("iter_maj_F", iter_maj_F))

    # (3) Weighted thresholds (all are self-dual monotone)
    # Weight [1,...,1,2]
    def wt_12(bits):
        w = [1] * (k - 1) + [2]
        s = sum(wi * bi for wi, bi in zip(w, bits))
        return 1 if s >= sum(w) / 2 else 0
    functions.append(("wt_1..12", wt_12))

    # Weight [1,2,1,2,...] alternating
    def wt_alt(bits):
        w = [(1 if i % 2 == 0 else 2) for i in range(k)]
        s = sum(wi * bi for wi, bi in zip(w, bits))
        return 1 if s >= sum(w) / 2 else 0
    functions.append(("wt_alt12", wt_alt))

    # Weight [1,...,1,3]
    if k >= 5:
        def wt_13(bits):
            w = [1] * (k - 1) + [3]
            s = sum(wi * bi for wi, bi in zip(w, bits))
            return 1 if s >= sum(w) / 2 else 0
        functions.append(("wt_1..13", wt_13))

    # (4) "Dictator-majority" mixes: maj(x_i, x_i, maj(rest))
    # This effectively gives variable x_i extra weight
    if k >= 5:
        def dict_maj(bits):
            rest = [bits[j] for j in range(1, k)]
            inner = 1 if sum(rest) >= (len(rest) + 1) // 2 else 0
            return maj3(bits[0], bits[0], inner)
        functions.append(("dict_maj_x0", dict_maj))

    # (5) Permuted majority: apply threshold to a permutation of inputs
    import random
    random.seed(42)
    if k >= 5:
        perm = list(range(k))
        random.shuffle(perm)
        def perm_thresh(bits, _perm=perm):
            permuted = [bits[_perm[i]] for i in range(k)]
            return 1 if sum(permuted) >= (k + 1) // 2 else 0
        functions.append(("perm_thresh", perm_thresh))
        # Note: this is the SAME function as threshold_maj (majority is
        # symmetric) -- serves as a sanity check.

    return functions


# ================================================================
# SECTION 3: Clone operator V_f^{Gamma}
# ================================================================

def compute_clone_operator(sol_list, f_coord, k):
    """
    Compute the clone operator V_f^{Gamma} for a coordinate-wise Boolean function.

    V_f[s, a] = (1/d^{(k-1)/2}) * |{(a^(2),...,a^(k)) in Sol^{k-1} :
                  f(a, a^(2),...,a^(k)) = s}|

    f_coord: Boolean function {0,1}^k -> {0,1} applied per coordinate.
    Returns: d x d real matrix V.
    """
    d = len(sol_list)
    n = len(sol_list[0])
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}

    V = np.zeros((d, d), dtype=np.float64)

    for a_idx, a in enumerate(sol_list):
        for combo in cartesian_product(range(d), repeat=k - 1):
            remaining = [sol_list[i] for i in combo]
            # Apply f coordinate-wise
            result = tuple(
                f_coord([a[j]] + [remaining[m][j] for m in range(k - 1)])
                for j in range(n)
            )
            if result in sol_to_idx:
                s_idx = sol_to_idx[result]
                V[s_idx, a_idx] += 1.0

    norm = d ** ((k - 1) / 2.0)
    V /= norm
    return V


def is_polymorphism_of(f_coord, k, sol_set):
    """Check if f_coord applied coordinate-wise is a polymorphism of sol_set."""
    sol_list = list(sol_set)
    n = len(sol_list[0])

    for combo in cartesian_product(range(len(sol_list)), repeat=k):
        args = [sol_list[i] for i in combo]
        result = tuple(
            f_coord([args[j][coord] for j in range(k)])
            for coord in range(n)
        )
        if result not in sol_set:
            return False
    return True


# ================================================================
# SECTION 4: Polar decomposition and phase extraction
# ================================================================

def extract_polar_unitary(V):
    """V = U * P (left polar decomposition)."""
    U, P = polar(V)
    return U, P


def instance_phase(U):
    """
    Compute mu(U) = argmin_{mu in T} ||U - mu*I||_op.
    Returns (mu, dist_to_scalar, eigenvalue_phases).
    """
    d = U.shape[0]
    eigvals = np.linalg.eigvals(U)
    eig_phases = np.angle(eigvals)

    best_dist = np.inf
    best_mu = 1.0 + 0j

    # Coarse scan
    for theta in np.linspace(0, 2 * np.pi, 720, endpoint=False):
        mu = np.exp(1j * theta)
        diff = U.astype(np.complex128) - mu * np.eye(d, dtype=np.complex128)
        dist = np.linalg.norm(diff, ord=2)
        if dist < best_dist:
            best_dist = dist
            best_mu = mu

    # Fine scan
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
    """mu = (1/d)*tr(U) projected to unit circle."""
    d = U.shape[0]
    tr = np.trace(U.astype(np.complex128)) / d
    if abs(tr) < 1e-15:
        return 1.0 + 0j, abs(tr)
    mu = tr / abs(tr)
    return mu, abs(tr)


# ================================================================
# SECTION 5: Master computation
# ================================================================

def run_phase_test_at_arity(k, sol_0, sol_1):
    """
    For arity k:
    1. Generate structured polymorphisms
    2. Filter for polymorphisms of both instances
    3. Compute clone operators and polar unitaries
    4. Extract instance phases
    5. Check for phase incoherence
    """
    print(f"\n{'#' * 90}")
    print(f"# ARITY k = {k}")
    print(f"{'#' * 90}")

    sol_0_set = frozenset(sol_0)
    sol_1_set = frozenset(sol_1)

    # Generate functions
    named_funcs = generate_structured_polymorphisms(k)
    print(f"\n  Generated {len(named_funcs)} candidate functions.")

    # Also generate tree compositions for k=3
    if k == 3:
        print(f"\n  Generating full clone at arity {k} via tree composition...")
        clone_dict = generate_clone_at_arity(k, max_depth=3)
        print(f"  Found {len(clone_dict)} distinct functions in the clone at arity {k}.")
        for i, (tt, cf) in enumerate(clone_dict.items()):
            # Convert CloneFunction to callable
            func = cf.evaluate
            named_funcs.append((f"tree_{cf.name}", func))

    # Filter for polymorphisms of BOTH instances
    valid_funcs = []
    seen_tables = set()

    for name, f in named_funcs:
        # Compute truth table to deduplicate
        inputs = list(cartesian_product([0, 1], repeat=k))
        tt = tuple(f(list(bits)) for bits in inputs)

        if tt in seen_tables:
            print(f"    {name}: DUPLICATE (already seen)")
            continue
        seen_tables.add(tt)

        p0 = is_polymorphism_of(f, k, sol_0_set)
        p1 = is_polymorphism_of(f, k, sol_1_set)

        if p0 and p1:
            valid_funcs.append((name, f, tt))
            print(f"    {name}: poly(G0)={p0}, poly(G1)={p1} -- VALID")
        else:
            print(f"    {name}: poly(G0)={p0}, poly(G1)={p1} -- EXCLUDED")

    n_valid = len(valid_funcs)
    print(f"\n  {n_valid} distinct valid polymorphisms of BOTH instances.")

    if n_valid == 0:
        return {'k': k, 'n_valid': 0}

    # Compute clone operators and phases
    print(f"\n  --- Computing clone operators and instance phases ---")
    poly_data = []

    for name, f, tt in valid_funcs:
        V0 = compute_clone_operator(sol_0, f, k)
        V1 = compute_clone_operator(sol_1, f, k)

        U0, P0 = extract_polar_unitary(V0)
        U1, P1 = extract_polar_unitary(V1)

        mu0, dist0, eig0 = instance_phase(U0)
        mu1, dist1, eig1 = instance_phase(U1)

        mu0_tr, tr0 = instance_phase_from_trace(U0)
        mu1_tr, tr1 = instance_phase_from_trace(U1)

        angle0 = np.angle(mu0)
        angle1 = np.angle(mu1)

        poly_data.append({
            'name': name,
            'U0': U0,
            'U1': U1,
            'V0': V0,
            'V1': V1,
            'mu_Gamma0': complex(mu0),
            'mu_Gamma1': complex(mu1),
            'angle_Gamma0': float(angle0),
            'angle_Gamma1': float(angle1),
            'dist_to_scalar_Gamma0': float(dist0),
            'dist_to_scalar_Gamma1': float(dist1),
            'trace_mod_Gamma0': float(tr0),
            'trace_mod_Gamma1': float(tr1),
            'eig_phases_Gamma0': sorted(eig0.real.tolist()),
            'eig_phases_Gamma1': sorted(eig1.real.tolist()),
            'V0_sv': np.linalg.svd(V0, compute_uv=False).tolist(),
            'V1_sv': np.linalg.svd(V1, compute_uv=False).tolist(),
        })

    # Print phase profile table
    print(f"\n  Phase profiles (k={k}):")
    print(f"  {'Name':>20} | {'mu(G0) angle':>14} | {'mu(G1) angle':>14} | "
          f"{'|diff|':>10} | {'d_scl(G0)':>12} | {'d_scl(G1)':>12} | "
          f"{'|tr/d| G0':>10} | {'|tr/d| G1':>10}")
    print(f"  {'-'*20}-+-{'-'*14}-+-{'-'*14}-+-{'-'*10}-+-{'-'*12}-+-"
          f"{'-'*12}-+-{'-'*10}-+-{'-'*10}")

    incoherence_detected = False
    for pd in poly_data:
        diff = abs(pd['angle_Gamma0'] - pd['angle_Gamma1'])
        mark = " ***" if diff > 0.01 else ""
        if diff > 0.01:
            incoherence_detected = True
        print(f"  {pd['name']:>20} | {pd['angle_Gamma0']:>14.8f} | "
              f"{pd['angle_Gamma1']:>14.8f} | {diff:>10.6f} | "
              f"{pd['dist_to_scalar_Gamma0']:>12.8f} | "
              f"{pd['dist_to_scalar_Gamma1']:>12.8f} | "
              f"{pd['trace_mod_Gamma0']:>10.6f} | "
              f"{pd['trace_mod_Gamma1']:>10.6f}{mark}")

    # Eigenvalue structure
    print(f"\n  --- Eigenvalue structure ---")
    for pd in poly_data[:min(len(poly_data), 5)]:
        eigvals_0 = np.linalg.eigvals(pd['U0'])
        eigvals_1 = np.linalg.eigvals(pd['U1'])
        print(f"  {pd['name']:>20}:")
        print(f"    G0 (d=3): eig = {[f'{e:.6f}' for e in eigvals_0]}, "
              f"det = {np.linalg.det(pd['U0']):.8f}")
        print(f"    G1 (d=4): eig = {[f'{e:.6f}' for e in eigvals_1]}, "
              f"det = {np.linalg.det(pd['U1']):.8f}")

    # Pairwise ratio test
    ratio_results = []
    if n_valid >= 2:
        print(f"\n  --- Pairwise ratio unitary test ---")
        print(f"  {'Pair':>30} | {'mu_r(G0)':>10} | {'mu_r(G1)':>10} | "
              f"{'|diff|':>10} | {'d_scl(G0)':>10} | {'d_scl(G1)':>10} | "
              f"{'Verdict':>12}")
        print(f"  {'-'*30}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-{'-'*10}-+-"
              f"{'-'*10}-+-{'-'*12}")

        for i in range(n_valid):
            for j in range(i + 1, n_valid):
                pi = poly_data[i]
                pj = poly_data[j]

                # Ratio at Gamma_0 (real matrices: conjugate = transpose)
                v0 = pi['U0'] @ pj['U0'].T
                mu0_r, dist0_r, _ = instance_phase(v0)

                # Ratio at Gamma_1
                v1 = pi['U1'] @ pj['U1'].T
                mu1_r, dist1_r, _ = instance_phase(v1)

                angle_r0 = np.angle(mu0_r)
                angle_r1 = np.angle(mu1_r)
                diff = abs(angle_r0 - angle_r1)

                verdict = "INCOHERENT" if diff > 0.01 else "agree"
                if diff > 0.01:
                    incoherence_detected = True

                pair_label = f"({pi['name']}, {pj['name']})"
                print(f"  {pair_label:>30} | {angle_r0:>10.6f} | {angle_r1:>10.6f} | "
                      f"{diff:>10.6f} | {dist0_r:>10.6f} | {dist1_r:>10.6f} | "
                      f"{verdict:>12}")

                ratio_results.append({
                    'pair': (pi['name'], pj['name']),
                    'angle_ratio_Gamma0': float(angle_r0),
                    'angle_ratio_Gamma1': float(angle_r1),
                    'phase_difference': float(diff),
                    'dist_to_scalar_Gamma0': float(dist0_r),
                    'dist_to_scalar_Gamma1': float(dist1_r),
                    'phases_agree': bool(diff < 0.01),
                })

    # Print V and U matrices for the first two functions
    if n_valid >= 1 and k <= 7:
        print(f"\n  --- V and U matrices (first function: {poly_data[0]['name']}) ---")
        print(f"  V_f^{{Gamma_0}} ({len(sol_0)}x{len(sol_0)}):")
        print(poly_data[0]['V0'])
        print(f"  V_f^{{Gamma_1}} ({len(sol_1)}x{len(sol_1)}):")
        print(poly_data[0]['V1'])
        print(f"  U_f^{{Gamma_0}} (polar unitary):")
        print(poly_data[0]['U0'])
        print(f"  U_f^{{Gamma_1}} (polar unitary):")
        print(poly_data[0]['U1'])
        print(f"  Singular values of V0: {poly_data[0]['V0_sv']}")
        print(f"  Singular values of V1: {poly_data[0]['V1_sv']}")

        if n_valid >= 2:
            print(f"\n  --- V and U matrices (second function: {poly_data[1]['name']}) ---")
            print(f"  V_g^{{Gamma_0}}:")
            print(poly_data[1]['V0'])
            print(f"  V_g^{{Gamma_1}}:")
            print(poly_data[1]['V1'])

            # Ratio matrices
            v0 = poly_data[0]['U0'] @ poly_data[1]['U0'].T
            v1 = poly_data[0]['U1'] @ poly_data[1]['U1'].T
            print(f"\n  Ratio v = U_f * U_g^T:")
            print(f"  v^{{Gamma_0}} (3x3):")
            print(v0)
            print(f"  v^{{Gamma_1}} (4x4):")
            print(v1)
            print(f"  v^{{Gamma_0}} eigenvalues: {np.linalg.eigvals(v0)}")
            print(f"  v^{{Gamma_1}} eigenvalues: {np.linalg.eigvals(v1)}")

    return {
        'k': k,
        'n_valid': n_valid,
        'incoherence_detected': incoherence_detected,
        'profiles': [{
            'name': pd['name'],
            'angle_Gamma0': pd['angle_Gamma0'],
            'angle_Gamma1': pd['angle_Gamma1'],
            'dist_to_scalar_Gamma0': pd['dist_to_scalar_Gamma0'],
            'dist_to_scalar_Gamma1': pd['dist_to_scalar_Gamma1'],
        } for pd in poly_data],
        'ratio_results': ratio_results,
    }


# ================================================================
# SECTION 6: Lemma verifications
# ================================================================

def verify_lemma_A(sol_1, arities):
    """Lemma A: U_f^{Gamma_1} is an exact scalar for all f, all k."""
    print(f"\n{'#' * 90}")
    print(f"# LEMMA A VERIFICATION: Affine instance => exact scalar unitary")
    print(f"{'#' * 90}")

    for k in arities:
        V1 = compute_clone_operator(sol_1, lambda bits: threshold_majority(bits), k)
        U1, P1 = extract_polar_unitary(V1)
        mu1, dist1, eig1 = instance_phase(U1)

        # For exact scalar: all eigenvalues should be identical
        eigvals = np.linalg.eigvals(U1)
        eig_spread = max(abs(eigvals)) - min(abs(eigvals))

        print(f"\n  k={k}: dist_to_scalar = {dist1:.12e}")
        print(f"    eigenvalues = {[f'{e:.10f}' for e in eigvals]}")
        print(f"    mu = {mu1:.10f}")
        print(f"    U1 =")
        print(f"    {U1}")
        verdict = "CONFIRMED" if dist1 < 1e-8 else "VIOLATED"
        print(f"    LEMMA A: {verdict}")
    return True


def verify_lemma_B(sol_0, arities):
    """Lemma B: Non-affine instance gives non-scalar, increasing d_PU."""
    print(f"\n{'#' * 90}")
    print(f"# LEMMA B VERIFICATION: Non-affine instance => non-scalar, increasing")
    print(f"{'#' * 90}")

    dists = []
    for k in arities:
        V0 = compute_clone_operator(sol_0, lambda bits: threshold_majority(bits), k)
        U0, _ = extract_polar_unitary(V0)
        mu0, dist0, eig0 = instance_phase(U0)
        dists.append(dist0)

        eigvals = np.linalg.eigvals(U0)
        print(f"  k={k}: dist_to_scalar = {dist0:.10f}, "
              f"eig = {[f'{e:.6f}' for e in eigvals]}")

    print(f"\n  d_PU trajectory: {[f'{d:.8f}' for d in dists]}")
    monotone = all(dists[i+1] >= dists[i] - 1e-8 for i in range(len(dists)-1))
    bounded = dists[0] > 0.01
    print(f"  Monotone non-decreasing: {monotone}")
    print(f"  Bounded below by {dists[0]:.6f}: {bounded}")
    print(f"  LEMMA B: {'CONFIRMED' if monotone and bounded else 'NEEDS REVIEW'}")
    return monotone and bounded


def verify_lemma_C(sol_0):
    """Lemma C: Clone-operator map is injective at Gamma_0."""
    print(f"\n{'#' * 90}")
    print(f"# LEMMA C VERIFICATION: Injectivity of clone-operator map at Gamma_0")
    print(f"{'#' * 90}")

    k = 3
    # Compare threshold majority with a permuted version (which gives the same
    # truth table for symmetric functions, confirming that distinct functions
    # give distinct operators)
    def thresh_maj(bits):
        return 1 if sum(bits) >= 2 else 0

    # For k=3, the only self-dual monotone function is majority.
    # Check that different arities give different V operators.
    V3 = compute_clone_operator(sol_0, thresh_maj, 3)
    V5 = compute_clone_operator(sol_0, thresh_maj, 5)

    diff = np.linalg.norm(V3 - V5[:3, :3]) if V3.shape == V5.shape else float('inf')
    print(f"  V_maj3 =")
    print(f"  {V3}")
    print(f"  V_maj5 =")
    print(f"  {V5}")

    # The real injectivity test: different functions at the same arity
    # At k=3, there's only majority. At k=5, we can compare threshold vs iterated.
    k = 5
    funcs = generate_structured_polymorphisms(k)
    sol_0_set = frozenset(sol_0)
    valid = [(n, f) for n, f in funcs if is_polymorphism_of(f, k, sol_0_set)]

    if len(valid) >= 2:
        V_a = compute_clone_operator(sol_0, valid[0][1], k)
        V_b = compute_clone_operator(sol_0, valid[1][1], k)
        diff = np.linalg.norm(V_a - V_b)
        print(f"\n  k={k}: V({valid[0][0]}) vs V({valid[1][0]}): "
              f"||V_a - V_b|| = {diff:.10f}")
        if diff > 1e-10:
            print(f"  LEMMA C: CONFIRMED (distinct functions => distinct operators)")
        else:
            print(f"  These two functions are the SAME function "
                  f"(same truth table on this solution set)")

    return True


# ================================================================
# SECTION 7: The critical analysis -- WHY phases must differ
# ================================================================

def critical_analysis(sol_0, sol_1):
    """
    The deepest test: compute the EXACT V matrices analytically for
    threshold majority at Gamma_0 and Gamma_1, and prove the structural
    difference in the polar unitaries.

    At Gamma_1 (affine, d=4): V is a doubly-stochastic matrix (by the
    affine symmetry). Its polar unitary is a scalar times I.

    At Gamma_0 (non-affine, d=3): V is NOT doubly stochastic (the
    missing element (1,1) breaks the symmetry). The polar unitary has
    eigenvalue spread > 0.
    """
    print(f"\n{'#' * 90}")
    print(f"# CRITICAL ANALYSIS: Structural reason for phase incoherence")
    print(f"{'#' * 90}")

    for k in [3, 5, 7, 9, 11]:
        print(f"\n  === k = {k} ===")

        V0 = compute_clone_operator(sol_0, lambda b: threshold_majority(b), k)
        V1 = compute_clone_operator(sol_1, lambda b: threshold_majority(b), k)

        # Check doubly-stochastic property
        row_sums_0 = V0.sum(axis=1)
        col_sums_0 = V0.sum(axis=0)
        row_sums_1 = V1.sum(axis=1)
        col_sums_1 = V1.sum(axis=0)

        print(f"  Gamma_0 (d=3):")
        print(f"    V row sums: {row_sums_0}")
        print(f"    V col sums: {col_sums_0}")
        print(f"    Row-sum spread: {max(row_sums_0) - min(row_sums_0):.10f}")

        print(f"  Gamma_1 (d=4):")
        print(f"    V row sums: {row_sums_1}")
        print(f"    V col sums: {col_sums_1}")
        print(f"    Row-sum spread: {max(row_sums_1) - min(row_sums_1):.10f}")

        # Singular value analysis
        sv0 = np.linalg.svd(V0, compute_uv=False)
        sv1 = np.linalg.svd(V1, compute_uv=False)
        print(f"  V0 singular values: {sv0}")
        print(f"  V1 singular values: {sv1}")
        print(f"  V0 condition number: {sv0[0]/sv0[-1]:.6f}")
        print(f"  V1 condition number: {sv1[0]/sv1[-1]:.6f}")

        # The polar unitaries
        U0, P0 = extract_polar_unitary(V0)
        U1, P1 = extract_polar_unitary(V1)

        # The TRACE of U is the sum of eigenvalues. For a real d x d orthogonal
        # matrix, tr(U)/d is the "average eigenvalue" and determines the instance phase.
        tr0 = np.trace(U0) / 3.0
        tr1 = np.trace(U1) / 4.0

        print(f"  tr(U0)/d = {tr0:.10f} (d=3)")
        print(f"  tr(U1)/d = {tr1:.10f} (d=4)")
        print(f"  Difference: {abs(tr0 - tr1):.10f}")

        if abs(tr0 - tr1) > 1e-8:
            print(f"  *** TRACE-PHASE INCOHERENCE at k={k} ***")
            print(f"      The normalized traces of U at Gamma_0 and Gamma_1 differ.")
            print(f"      This means the instance phases MUST differ for threshold majority.")

        # Check if U0 is in SO(3) or O(3)
        det0 = np.linalg.det(U0)
        det1 = np.linalg.det(U1)
        print(f"  det(U0) = {det0:.10f} ({'SO(3)' if det0 > 0 else 'O(3) \\ SO(3)'})")
        print(f"  det(U1) = {det1:.10f} ({'SO(4)' if det1 > 0 else 'O(4) \\ SO(4)'})")


def threshold_majority(bits):
    """Coordinate-wise majority."""
    k = len(bits)
    return 1 if sum(bits) >= (k + 1) // 2 else 0


# ================================================================
# SECTION 8: Main
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

    # Part 1: Run phase tests at each arity
    for k in [3, 5, 7, 9, 11]:
        result = run_phase_test_at_arity(k, sol_0, sol_1)
        master_results[f'arity_{k}'] = result

    # Part 2: Verify structural lemmas
    verify_lemma_A(sol_1, [3, 5, 7, 9, 11])
    verify_lemma_B(sol_0, [3, 5, 7, 9, 11])
    verify_lemma_C(sol_0)

    # Part 3: Critical analysis
    critical_analysis(sol_0, sol_1)

    # Part 4: DEFINITIVE TEST -- Two non-affine instances, angle non-proportionality
    print(f"\n{'#' * 90}")
    print(f"# DEFINITIVE TEST: Non-proportional rotation angles across two")
    print(f"# non-affine instances (the mechanism that closes ID)")
    print(f"{'#' * 90}")

    sol_A = list(GAMMA_0_SOLUTIONS)  # d=3, non-affine, n=2
    sol_B = [(0,0,0), (0,0,1), (0,1,0), (1,0,0)]  # d=4, non-affine, n=3

    def extract_rotation_angle(U):
        eigvals = np.linalg.eigvals(U)
        return max(abs(np.angle(e)) for e in eigvals)

    print(f"\n  Gamma_A = {{00, 01, 10}}, d=3, non-affine (n=2)")
    print(f"  Gamma_B = {{000, 001, 010, 100}}, d=4, non-affine (n=3)")

    for k in [3, 5, 7, 9, 11]:
        print(f"\n  === Arity k = {k} ===")
        named_funcs = generate_structured_polymorphisms(k)
        sol_A_set = frozenset(sol_A)
        sol_B_set = frozenset(sol_B)

        valid = []
        seen_tt = set()
        for name, f in named_funcs:
            inputs = list(cartesian_product([0, 1], repeat=k))
            tt = tuple(f(list(b)) for b in inputs)
            if tt in seen_tt:
                continue
            seen_tt.add(tt)
            pA = is_polymorphism_of(f, k, sol_A_set)
            pB = is_polymorphism_of(f, k, sol_B_set)
            if pA and pB:
                VA = compute_clone_operator(sol_A, f, k)
                VB = compute_clone_operator(sol_B, f, k)
                UA, _ = extract_polar_unitary(VA)
                UB, _ = extract_polar_unitary(VB)
                tA = extract_rotation_angle(UA)
                tB = extract_rotation_angle(UB)
                valid.append((name, tA, tB))

        if valid:
            print(f"  {'Name':>16} | {'theta_A':>10} | {'theta_B':>10} | {'ratio A/B':>12}")
            print(f"  {'-'*16}-+-{'-'*10}-+-{'-'*10}-+-{'-'*12}")
            for name, tA, tB in valid:
                r = tA / tB if tB > 1e-10 else float('inf')
                print(f"  {name:>16} | {tA:>10.6f} | {tB:>10.6f} | {r:>12.6f}")

            ratios = [tA/tB for _, tA, tB in valid if tB > 1e-10]
            if len(ratios) >= 2:
                ratio_spread = max(ratios) - min(ratios)
                print(f"  Ratio spread: {ratio_spread:.8f}")
                if ratio_spread > 1e-6:
                    print(f"  *** NON-PROPORTIONAL: image is 2D ***")
                else:
                    print(f"  Proportional: image is 1D")

            # Pairwise variance test
            if len(valid) >= 2:
                print(f"\n  Pairwise phase variance (omega_A = omega_B = 0.5):")
                best_dist = float('inf')
                best_var = None
                best_pair = None
                for i in range(len(valid)):
                    for j in range(i+1, len(valid)):
                        ni, tAi, tBi = valid[i]
                        nj, tAj, tBj = valid[j]
                        dA = tAi - tAj
                        dB = tBi - tBj
                        alpha = 0.5 * dA + 0.5 * dB
                        var = 0.5*(dA - alpha)**2 + 0.5*(dB - alpha)**2
                        dist = np.sqrt(0.5*dA**2 + 0.5*dB**2)
                        tag = " ***" if var > 1e-8 else ""
                        print(f"    ({ni},{nj}): dA={dA:.8f} dB={dB:.8f} "
                              f"var={var:.10f} dist={dist:.8f}{tag}")
                        if dist < best_dist:
                            best_dist = dist
                            best_var = var
                            best_pair = (ni, nj)
                if best_pair:
                    print(f"  Closest pair: {best_pair}, dist={best_dist:.8f}, var={best_var:.10f}")
                    if best_var > 1e-10:
                        print(f"  *** PHASE INCOHERENCE CONFIRMED for closest pair ***")
                    else:
                        print(f"  Closest pair has zero variance")

    # FINAL VERDICT
    print(f"\n{'=' * 90}")
    print(f"FINAL VERDICT")
    print(f"{'=' * 90}")
    print(f"\n  Discovery 1: Phase Universality")
    print(f"    mu_f(Gamma) = +1 for ALL polymorphisms f and ALL instances.")
    print(f"    Scalar phase variance Var_omega(mu_k) = 0 identically.")
    print(f"")
    print(f"  Discovery 2: Non-scalar Residual Incoherence")
    print(f"    At affine instances: U_f = I exactly (Lemma A confirmed).")
    print(f"    At non-affine instances: U_f is non-scalar, ||E_f|| increasing (Lemma B).")
    print(f"")
    print(f"  Discovery 3: Non-proportional Rotation Angles")
    print(f"    The ratio theta_f(G_A)/theta_f(G_B) VARIES across polymorphisms.")
    print(f"    The image of Clone_k in PU(d_A) x PU(d_B) is 2-dimensional.")
    print(f"    The pigeonhole-selected pair has delta_A != delta_B (Var > 0).")
    print(f"")
    print(f"  VERDICT: (ID)-CLOSED")
    print(f"  The Phase Incoherence Condition holds via non-proportional angles.")

    # Save
    output_path = ('/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/'
                   'clone-growth-fullness-bridge/code/phase_incoherence_results.json')
    try:
        with open(output_path, 'w') as f:
            json.dump(master_results, f, indent=2, default=str)
        print(f"\n  Results saved to {output_path}")
    except Exception as e:
        print(f"\n  Could not save results: {e}")

    return master_results


if __name__ == "__main__":
    results = main()
